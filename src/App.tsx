import { useState, useMemo } from 'react';
import { Header } from './components/Header';
import { SentenceDisplay } from './components/SentenceDisplay';
import { SlotArea } from './components/SlotArea';
import { WordPool } from './components/WordPool';
import { TypingInput } from './components/TypingInput';
import { AudioBar } from './components/AudioBar';
import { GrammarAnalysisCard } from './components/GrammarAnalysisCard';
import { SentenceExpansionCard } from './components/SentenceExpansionCard';
import { CourseMallModal } from './components/CourseMallModal';
import { CustomImportModal } from './components/CustomImportModal';
import { MistakeBookModal } from './components/MistakeBookModal';
import { SettingsModal } from './components/SettingsModal';
import { ListeningModeView } from './components/ListeningModeView';
import { SpeakingEvalModal } from './components/SpeakingEvalModal';
import { ReadingModeView } from './components/ReadingModeView';

import type { CoursePackage, Chapter, SentenceItem, UserSettings, UserStats, Lesson } from './types';
import { ALL_COURSES } from './data/mall';
import { saveCustomLesson } from './data/lessons';
import { useLocalStorage } from './hooks/useLocalStorage';
import { usePracticeState } from './hooks/usePracticeState';

export function App() {
  // 当前正在学习的课程包与章节
  const [currentCourseId, setCurrentCourseId] = useLocalStorage<string>('jlt_current_course_id', ALL_COURSES[0].id);
  const [currentChapterId, setCurrentChapterId] = useLocalStorage<string>('jlt_current_chapter_id', ALL_COURSES[0].chapters[0].id);
  const [currentIndex, setCurrentIndex] = useState(0);

  // 弹窗状态
  const [isMallModalOpen, setIsMallModalOpen] = useState(false);
  const [isSettingsModalOpen, setIsSettingsModalOpen] = useState(false);
  const [isCustomImportModalOpen, setIsCustomImportModalOpen] = useState(false);
  const [isMistakeModalOpen, setIsMistakeModalOpen] = useState(false);

  // 用户设置
  const [settings, setSettings] = useLocalStorage<UserSettings>('jlt_user_settings', {
    autoSpeak: true,
    speechRate: 1.0,
    accent: 'en-US',
    soundEffects: true,
    splitMode: 'word',
    practiceMode: 'translate',
    showGrammar: true // 默认开启对标截图的句法成分展示
  });

  // 用户统计
  const [stats, setStats] = useLocalStorage<UserStats>('jlt_user_stats', {
    streak: 0,
    bestStreak: 0,
    correctCount: 0,
    mistakeCount: 0,
    finishedSentenceIds: [],
    mistakeSentenceIds: [],
    chapterProgress: {},
    lastStudied: {
      courseId: ALL_COURSES[0].id,
      chapterId: ALL_COURSES[0].chapters[0].id,
      chapterTitle: ALL_COURSES[0].chapters[0].title,
      courseTitle: ALL_COURSES[0].title,
      sentenceIndex: 0,
      updatedAt: Date.now()
    }
  });

  // 找到当前课程包
  const currentCourse = useMemo(() => {
    return ALL_COURSES.find(c => c.id === currentCourseId) || ALL_COURSES[0];
  }, [currentCourseId]);

  // 找到当前章节
  const currentChapter = useMemo(() => {
    return currentCourse.chapters.find(ch => ch.id === currentChapterId) || currentCourse.chapters[0];
  }, [currentCourse, currentChapterId]);

  // 当前练习的句子数组
  const currentSentences = currentChapter.sentences;

  // 确保下标不越界
  const safeIndex = Math.min(currentIndex, Math.max(0, currentSentences.length - 1));

  // 练习核心状态机
  const {
    currentSentence,
    targetTokens,
    slotTokens,
    poolTokens,
    typedInput,
    isShaking,
    showHint,
    isFinished,
    handleSelectToken,
    handleReturnToken,
    handleKeyTyping,
    toggleHint,
    replayAudio
  } = usePracticeState({
    sentences: currentSentences,
    currentIndex: safeIndex,
    settings,
    onUpdateStats: (updater) => {
      setStats(prev => {
        const next = updater(prev);
        // 同步更新章节完成进度
        const currentChapDone = (prev.chapterProgress?.[currentChapter.id] || 0) + 1;
        return {
          ...next,
          chapterProgress: {
            ...prev.chapterProgress,
            [currentChapter.id]: Math.min(currentSentences.length, currentChapDone)
          },
          lastStudied: {
            courseId: currentCourse.id,
            chapterId: currentChapter.id,
            chapterTitle: currentChapter.title,
            courseTitle: currentCourse.title,
            sentenceIndex: safeIndex,
            updatedAt: Date.now()
          }
        };
      });
    },
    onNext: () => handleNextSentence()
  });

  // 下一句
  const handleNextSentence = () => {
    if (safeIndex < currentSentences.length - 1) {
      setCurrentIndex(safeIndex + 1);
    } else {
      alert(`🎉 太棒了！您已完整完成【${currentChapter.title}】的全部练习！`);
      setCurrentIndex(0);
    }
  };

  // 上一句
  const handlePrevSentence = () => {
    if (safeIndex > 0) {
      setCurrentIndex(safeIndex - 1);
    }
  };

  // 从课程商城选择特定章节练习
  const handleSelectChapterToPractice = (course: CoursePackage, chapter: Chapter) => {
    setCurrentCourseId(course.id);
    setCurrentChapterId(chapter.id);
    setCurrentIndex(0);

    // 记录最近学习
    setStats(prev => ({
      ...prev,
      lastStudied: {
        courseId: course.id,
        chapterId: chapter.id,
        chapterTitle: chapter.title,
        courseTitle: course.title,
        sentenceIndex: 0,
        updatedAt: Date.now()
      }
    }));
  };

  // 保存自定义题库
  const handleSaveCustomLesson = (newLesson: Lesson) => {
    saveCustomLesson(newLesson);
    alert('自建题库保存成功！');
  };

  // 错题库中的所有句子
  const mistakeSentences = useMemo(() => {
    const allKnownSentences: SentenceItem[] = ALL_COURSES.flatMap(c => c.chapters.flatMap(ch => ch.sentences));
    const set = new Set(stats.mistakeSentenceIds);
    return allKnownSentences.filter(s => set.has(s.id));
  }, [stats.mistakeSentenceIds]);

  // 从错题本移除单句
  const handleRemoveMistake = (id: string) => {
    setStats(prev => ({
      ...prev,
      mistakeSentenceIds: prev.mistakeSentenceIds.filter(mId => mId !== id)
    }));
  };

  // 开始错题专项特训
  const handleStartMistakePractice = (mistakeLesson: Lesson) => {
    saveCustomLesson(mistakeLesson);
    setIsMistakeModalOpen(false);
  };

  // 错题重置或学习统计重置
  const handleResetStats = () => {
    setStats({
      streak: 0,
      bestStreak: 0,
      correctCount: 0,
      mistakeCount: 0,
      finishedSentenceIds: [],
      mistakeSentenceIds: [],
      chapterProgress: {}
    });
  };

  // 跳转到拼写练习特定句子
  const handleJumpToPractice = (idx: number) => {
    setCurrentIndex(idx);
    setSettings(prev => ({ ...prev, practiceMode: 'translate' }));
  };

  return (
    <div className="min-h-screen bg-surface-bg flex flex-col font-sans">
      {/* 顶部导航与状态栏 */}
      <Header
        currentCourseTitle={currentCourse.title}
        currentChapterTitle={currentChapter.title}
        settings={settings}
        stats={stats}
        onOpenMallModal={() => setIsMallModalOpen(true)}
        onOpenSettingsModal={() => setIsSettingsModalOpen(true)}
        onOpenCustomImportModal={() => setIsCustomImportModalOpen(true)}
        onOpenMistakeModal={() => setIsMistakeModalOpen(true)}
        onUpdateSettings={setSettings}
      />

      {/* 主体交互区域 */}
      <main className="flex-1 flex flex-col pb-32">
        {/* 1. 中译英模式 & 听写模式 */}
        {(settings.practiceMode === 'translate' || settings.practiceMode === 'dictation') && currentSentence && (
          <div className="max-w-4xl w-full mx-auto px-4 flex flex-col items-center justify-center flex-1">
            {/* 中文释义与提示 */}
            <SentenceDisplay
              sentence={currentSentence}
              practiceMode={settings.practiceMode}
              showHint={showHint}
              onReplayAudio={replayAudio}
              onToggleHint={toggleHint}
            />

            {/* 拼写槽位区 */}
            <SlotArea
              targetTokens={targetTokens}
              slotTokens={slotTokens}
              typedInput={typedInput}
              isShaking={isShaking}
              isFinished={isFinished}
              onReturnToken={handleReturnToken}
            />

            {/* 打字状态与键盘交互监听 */}
            <TypingInput
              typedInput={typedInput}
              isFinished={isFinished}
              onKeyTyping={handleKeyTyping}
              onReturnLastToken={() => {
                if (slotTokens.length > 0) {
                  handleReturnToken(slotTokens[slotTokens.length - 1]);
                }
              }}
              onNextSentence={handleNextSentence}
              onReplayAudio={replayAudio}
              onToggleHint={toggleHint}
              slotTokens={slotTokens}
            />

            {/* 乱序词块卡片池（手动打字时平滑隐藏，支持快捷键 H 或点击恢复查看提示） */}
            <WordPool
              poolTokens={poolTokens}
              isFinished={isFinished}
              typedInput={typedInput}
              onSelectToken={handleSelectToken}
            />

            {/* 单词语法成分分析卡片（仅在拼写完成后才展示，输入过程中严格隐藏防剧透） */}
            {isFinished && settings.showGrammar && (
              <GrammarAnalysisCard
                sentence={currentSentence}
                showGrammar={settings.showGrammar}
                onToggleShowGrammar={() => setSettings(prev => ({ ...prev, showGrammar: !prev.showGrammar }))}
              />
            )}

            {/* 句子拼写完成后自动展开的“串记 · 联想 · 扩展”模块 */}
            <SentenceExpansionCard
              sentence={currentSentence}
              isFinished={isFinished}
              onNextSentence={handleNextSentence}
            />
          </div>
        )}

        {/* 2. 听力精听磨耳朵模式 */}
        {settings.practiceMode === 'listening' && (
          <ListeningModeView
            sentences={currentSentences}
            settings={settings}
            onJumpToPractice={handleJumpToPractice}
          />
        )}

        {/* 3. 口语评测模式 */}
        {settings.practiceMode === 'speaking' && currentSentence && (
          <SpeakingEvalModal
            sentence={currentSentence}
            settings={settings}
            onNext={handleNextSentence}
          />
        )}

        {/* 4. 篇章阅读模式 */}
        {settings.practiceMode === 'reading' && (
          <ReadingModeView
            sentences={currentSentences}
            settings={settings}
            onJumpToPractice={handleJumpToPractice}
          />
        )}
      </main>

      {/* 底部发音与快捷控制栏（在拼写/听写模式下常驻） */}
      {(settings.practiceMode === 'translate' || settings.practiceMode === 'dictation') && (
        <AudioBar
          currentIndex={safeIndex}
          totalSentences={currentSentences.length}
          isFinished={isFinished}
          showHint={showHint}
          settings={settings}
          onReplayAudio={replayAudio}
          onToggleHint={toggleHint}
          onNextSentence={handleNextSentence}
          onPrevSentence={handlePrevSentence}
          onUpdateSettings={setSettings}
        />
      )}

      {/* 课程包商城三级弹窗 */}
      <CourseMallModal
        isOpen={isMallModalOpen}
        onClose={() => setIsMallModalOpen(false)}
        stats={stats}
        onSelectChapterToPractice={handleSelectChapterToPractice}
      />

      {/* 自建题库导入弹窗 */}
      <CustomImportModal
        isOpen={isCustomImportModalOpen}
        onClose={() => setIsCustomImportModalOpen(false)}
        onSaveLesson={handleSaveCustomLesson}
      />

      {/* 错题本弹窗 */}
      <MistakeBookModal
        isOpen={isMistakeModalOpen}
        onClose={() => setIsMistakeModalOpen(false)}
        mistakeSentences={mistakeSentences}
        onRemoveMistake={handleRemoveMistake}
        onStartMistakePractice={handleStartMistakePractice}
      />

      {/* 设置弹窗 */}
      <SettingsModal
        isOpen={isSettingsModalOpen}
        onClose={() => setIsSettingsModalOpen(false)}
        settings={settings}
        stats={stats}
        onUpdateSettings={setSettings}
        onResetStats={handleResetStats}
      />
    </div>
  );
}

export default App;
