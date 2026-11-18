import React, { useState, useEffect, useRef } from 'react';
import { Mic, MicOff, Volume2, Sparkles, RotateCcw, CheckCircle } from 'lucide-react';
import type { SentenceItem, UserSettings } from '../types';
import { speakText } from '../utils/tts';
import { createSpeechRecognizer, evaluateSpokenText } from '../utils/speechRecognition';
import type { SpeechEvalResult } from '../utils/speechRecognition';

interface SpeakingEvalModalProps {
  sentence: SentenceItem;
  settings: UserSettings;
  onNext: () => void;
}

export const SpeakingEvalModal: React.FC<SpeakingEvalModalProps> = ({
  sentence,
  settings,
  onNext
}) => {
  const [isRecording, setIsRecording] = useState(false);
  const [evalResult, setEvalResult] = useState<SpeechEvalResult | null>(null);
  const [errorMsg, setErrorMsg] = useState('');

  const recognizerRef = useRef<any>(null);

  useEffect(() => {
    setEvalResult(null);
    setErrorMsg('');
    setIsRecording(false);
  }, [sentence]);

  const startRecording = () => {
    setErrorMsg('');
    setEvalResult(null);

    const recognizer = createSpeechRecognizer(
      (text, isFinal) => {
        if (isFinal) {
          setIsRecording(false);
          const result = evaluateSpokenText(sentence.english, text);
          setEvalResult(result);
        }
      },
      (err) => {
        console.error('Speech recognition error:', err);
        setIsRecording(false);
        setErrorMsg('未能获取麦克风声音或浏览器暂未授权，请检查权限。');
      }
    );

    if (!recognizer) {
      setErrorMsg('当前浏览器不支持原生语音识别，建议使用 Chrome 或 Edge 浏览器。');
      return;
    }

    try {
      recognizer.start();
      recognizerRef.current = recognizer;
      setIsRecording(true);
    } catch (e) {
      console.error(e);
      setIsRecording(false);
    }
  };

  const stopRecording = () => {
    if (recognizerRef.current) {
      recognizerRef.current.stop();
      setIsRecording(false);
    }
  };

  return (
    <div className="w-full max-w-2xl mx-auto py-8 px-4 flex flex-col items-center text-center animate-fade-in">
      {/* 模式标志 */}
      <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-purple-50 text-purple-700 text-xs font-bold border border-purple-100 mb-4">
        <Sparkles className="w-3.5 h-3.5" />
        <span>口语跟读与 AI 发音评测</span>
      </div>

      {/* 目标句子卡片 */}
      <div className="w-full p-6 sm:p-8 rounded-3xl bg-white border-2 border-slate-200/90 shadow-sm mb-6">
        <h2 className="text-xl sm:text-2xl font-bold text-slate-800 leading-snug">
          {sentence.english}
        </h2>
        <p className="text-sm sm:text-base text-slate-500 mt-2 font-medium">
          {sentence.chinese}
        </p>

        {sentence.phonetic && (
          <p className="text-xs text-brand-600 mt-2 font-mono">{sentence.phonetic}</p>
        )}

        <button
          onClick={() => speakText(sentence.english, { rate: settings.speechRate, accent: settings.accent })}
          className="mt-4 inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-brand-50 hover:bg-brand-100 text-brand-700 text-xs font-bold transition-all card-pressable"
        >
          <Volume2 className="w-4 h-4" />
          <span>听原声范读</span>
        </button>
      </div>

      {/* 录音麦克风大按钮 */}
      <div className="my-4">
        <button
          onClick={isRecording ? stopRecording : startRecording}
          className={`w-20 h-20 rounded-full flex items-center justify-center text-white shadow-xl transition-all card-pressable ${
            isRecording
              ? 'bg-rose-500 scale-110 animate-pulse shadow-rose-500/40 ring-8 ring-rose-100'
              : 'bg-brand-600 hover:bg-brand-700 shadow-brand-500/30'
          }`}
          title={isRecording ? '点击结束录音' : '点击开始跟读'}
        >
          {isRecording ? <MicOff className="w-8 h-8" /> : <Mic className="w-8 h-8" />}
        </button>
        <p className="text-xs font-bold text-slate-400 mt-3">
          {isRecording ? '正在倾听... 请朗读上方句子' : '点击麦克风开启录音跟读'}
        </p>
      </div>

      {/* 错误提示 */}
      {errorMsg && (
        <div className="p-3 rounded-2xl bg-rose-50 text-rose-600 text-xs border border-rose-200 max-w-md my-2">
          {errorMsg}
        </div>
      )}

      {/* 实时转写与打分结果 */}
      {evalResult && (
        <div className="w-full p-6 rounded-3xl bg-white border border-slate-200 shadow-sm mt-4 animate-slide-up">
          <div className="flex items-center justify-center gap-2 mb-3">
            <span className="text-2xl font-black text-slate-800">
              综合评分：
              <span className={evalResult.score >= 80 ? 'text-emerald-500' : evalResult.score >= 60 ? 'text-amber-500' : 'text-rose-500'}>
                {evalResult.score} 分
              </span>
            </span>
          </div>

          <div className="flex flex-wrap items-center justify-center gap-2 text-base font-bold my-4">
            {evalResult.words.map((w, idx) => (
              <span
                key={idx}
                className={`px-2.5 py-1 rounded-xl text-sm ${
                  w.status === 'correct'
                    ? 'bg-emerald-100 text-emerald-800 border border-emerald-200'
                    : w.status === 'imperfect'
                    ? 'bg-amber-100 text-amber-800 border border-amber-200'
                    : 'bg-rose-100 text-rose-800 border border-rose-200'
                }`}
                title={`你读的是：${w.spokenWord || '(未识别到)'}`}
              >
                {w.targetWord}
              </span>
            ))}
          </div>

          <p className="text-xs text-slate-400 mt-2">
            绿色：发音精准 · 橙色：尚可 · 红色：需加强
          </p>

          <div className="mt-5 flex items-center justify-center gap-3">
            <button
              onClick={startRecording}
              className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              <span>重新评测</span>
            </button>
            <button
              onClick={onNext}
              className="flex items-center gap-1.5 px-5 py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-600 text-white text-xs font-bold shadow-md shadow-emerald-500/20 card-pressable"
            >
              <CheckCircle className="w-4 h-4" />
              <span>下一句</span>
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
