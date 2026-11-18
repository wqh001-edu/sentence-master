import { useState, useEffect, useCallback, useMemo } from 'react';
import confetti from 'canvas-confetti';
import type { SentenceItem, ChunkToken, UserSettings, UserStats } from '../types';
import { tokenizeSentence, shuffleTokens, cleanWord } from '../utils/chunker';
import { playCorrectSound, playSentenceCompleteSound, playErrorSound, playCardClickSound } from '../utils/sound';
import { speakText, stopSpeaking } from '../utils/tts';

interface UsePracticeProps {
  sentences: SentenceItem[];
  currentIndex: number;
  settings: UserSettings;
  stats?: UserStats;
  onUpdateStats: (updater: (prev: UserStats) => UserStats) => void;
  onNext?: () => void;
}

export function usePracticeState({
  sentences,
  currentIndex,
  settings,
  onUpdateStats
}: UsePracticeProps) {
  const currentSentence = sentences[currentIndex] || null;

  // 目标词块序列（按原句顺序）
  const targetTokens: ChunkToken[] = useMemo(() => {
    if (!currentSentence) return [];
    return tokenizeSentence(currentSentence.english, settings.splitMode, currentSentence.customChunks);
  }, [currentSentence, settings.splitMode]);

  // 已放置到槽位的词块
  const [slotTokens, setSlotTokens] = useState<ChunkToken[]>([]);

  // 待选词块池（打乱后的剩余卡片）
  const [poolTokens, setPoolTokens] = useState<ChunkToken[]>([]);

  // 当前键盘输入的临时字符
  const [typedInput, setTypedInput] = useState<string>('');

  // 抖动动画状态（打错时触发）
  const [isShaking, setIsShaking] = useState(false);

  // 答案揭晓/提示状态
  const [showHint, setShowHint] = useState(false);

  // 本句是否已答完
  const [isFinished, setIsFinished] = useState(false);

  // 本句错误次数计数（用于错题归集）
  const [currentMistakeCount, setCurrentMistakeCount] = useState(0);

  // 切题或模式切换时重置状态
  useEffect(() => {
    if (!currentSentence) return;
    setSlotTokens([]);
    setPoolTokens(shuffleTokens(targetTokens));
    setTypedInput('');
    setIsShaking(false);
    setShowHint(false);
    setIsFinished(false);
    setCurrentMistakeCount(0);

    // 如果开启了自动发音，或者处于听写模式，则主动朗读句子
    if (settings.autoSpeak || settings.practiceMode === 'dictation') {
      speakText(currentSentence.english, {
        rate: settings.speechRate,
        accent: settings.accent
      });
    }

    return () => {
      stopSpeaking();
    };
  }, [currentSentence, targetTokens, settings.splitMode, settings.practiceMode, settings.autoSpeak, settings.speechRate, settings.accent]);

  // 触发错误抖动与提示音
  const triggerError = useCallback(() => {
    setIsShaking(true);
    playErrorSound(settings.soundEffects);
    setCurrentMistakeCount(prev => prev + 1);

    // 发生错误，重置连击
    onUpdateStats(prev => {
      const isAlreadyInMistakes = currentSentence && prev.mistakeSentenceIds.includes(currentSentence.id);
      return {
        ...prev,
        streak: 0,
        mistakeCount: prev.mistakeCount + 1,
        mistakeSentenceIds: (currentSentence && !isAlreadyInMistakes)
          ? [...prev.mistakeSentenceIds, currentSentence.id]
          : prev.mistakeSentenceIds
      };
    });

    setTimeout(() => {
      setIsShaking(false);
    }, 400);
  }, [settings.soundEffects, currentSentence, onUpdateStats]);

  // 处理整句拼写完成
  const handleSentenceComplete = useCallback(() => {
    setIsFinished(true);
    playSentenceCompleteSound(settings.soundEffects);

    // 庆祝撒花
    try {
      confetti({
        particleCount: 50,
        spread: 60,
        origin: { y: 0.7 },
        colors: ['#4f46e5', '#10b981', '#f59e0b', '#ec4899']
      });
    } catch {
      // ignore
    }

    // 完整纯正英文复读一遍
    if (currentSentence) {
      speakText(currentSentence.english, {
        rate: settings.speechRate,
        accent: settings.accent
      });
    }

    // 更新统计数据
    onUpdateStats(prev => {
      const newStreak = prev.streak + 1;
      const best = Math.max(prev.bestStreak, newStreak);
      const isNewFinish = currentSentence && !prev.finishedSentenceIds.includes(currentSentence.id);
      return {
        ...prev,
        streak: newStreak,
        bestStreak: best,
        correctCount: prev.correctCount + 1,
        finishedSentenceIds: (currentSentence && isNewFinish)
          ? [...prev.finishedSentenceIds, currentSentence.id]
          : prev.finishedSentenceIds
      };
    });
  }, [settings.soundEffects, settings.speechRate, settings.accent, currentSentence, onUpdateStats]);

  // 点击/选择词块
  const handleSelectToken = useCallback((token: ChunkToken) => {
    if (isFinished) return;

    const expectedIndex = slotTokens.length;
    const expectedToken = targetTokens[expectedIndex];

    // 判断选中的 token 是否是当前需要放置的下一个词
    if (expectedToken && expectedToken.id === token.id) {
      // 匹配成功
      playCorrectSound(settings.soundEffects);
      const nextSlots = [...slotTokens, token];
      setSlotTokens(nextSlots);
      setPoolTokens(prev => prev.filter(t => t.id !== token.id));
      setTypedInput('');

      // 检查是否完成整句
      if (nextSlots.length === targetTokens.length) {
        handleSentenceComplete();
      }
    } else {
      // 匹配失败
      triggerError();
    }
  }, [isFinished, slotTokens, targetTokens, settings.soundEffects, handleSentenceComplete, triggerError]);

  // 退回已填入的词块（点击槽位中的词）
  const handleReturnToken = useCallback((token: ChunkToken) => {
    if (isFinished) return;
    playCardClickSound(settings.soundEffects);
    setSlotTokens(prev => prev.filter(t => t.id !== token.id));
    setPoolTokens(prev => [...prev, token]);
    setTypedInput('');
  }, [isFinished, settings.soundEffects]);

  // 电脑端：处理键盘输入匹配
  const handleKeyTyping = useCallback((input: string) => {
    if (isFinished) return;

    const expectedIndex = slotTokens.length;
    const expectedToken = targetTokens[expectedIndex];
    if (!expectedToken) return;

    const cleanExpected = expectedToken.cleanText;
    const cleanTyped = cleanWord(input);

    // 如果打字内容与目标词完全相同
    if (cleanTyped === cleanExpected) {
      // 找到 poolTokens 中对应的 token 移入槽位
      const matchedToken = poolTokens.find(t => t.id === expectedToken.id) || expectedToken;
      handleSelectToken(matchedToken);
      setTypedInput('');
    } else {
      setTypedInput(input);
    }
  }, [isFinished, slotTokens.length, targetTokens, poolTokens, handleSelectToken]);

  // 提示答案
  const toggleHint = useCallback(() => {
    setShowHint(prev => !prev);
    if (!showHint && currentSentence) {
      speakText(currentSentence.english, {
        rate: settings.speechRate,
        accent: settings.accent
      });
    }
  }, [showHint, currentSentence, settings.speechRate, settings.accent]);

  // 重听发音
  const replayAudio = useCallback(() => {
    if (currentSentence) {
      speakText(currentSentence.english, {
        rate: settings.speechRate,
        accent: settings.accent
      });
    }
  }, [currentSentence, settings.speechRate, settings.accent]);

  return {
    currentSentence,
    targetTokens,
    slotTokens,
    poolTokens,
    typedInput,
    isShaking,
    showHint,
    isFinished,
    currentMistakeCount,
    setTypedInput,
    handleSelectToken,
    handleReturnToken,
    handleKeyTyping,
    triggerError,
    toggleHint,
    replayAudio,
    handleSentenceComplete
  };
}
