import React, { useState, useEffect, useRef } from 'react';
import { Play, Pause, Eye, EyeOff } from 'lucide-react';
import type { SentenceItem, UserSettings } from '../types';
import { speakText, stopSpeaking } from '../utils/tts';

interface ListeningModeViewProps {
  sentences: SentenceItem[];
  settings: UserSettings;
  onJumpToPractice: (index: number) => void;
}

export const ListeningModeView: React.FC<ListeningModeViewProps> = ({
  sentences,
  settings,
  onJumpToPractice
}) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [pauseDuration] = useState(1.5); // 句间停留秒数
  const [hideEnglish, setHideEnglish] = useState(false);
  const [hideChinese, setHideChinese] = useState(false);
  const [singleLoop, setSingleLoop] = useState(false);

  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const playCurrent = (idx = currentIndex) => {
    const sent = sentences[idx];
    if (!sent) return;

    speakText(sent.english, {
      rate: settings.speechRate,
      accent: settings.accent,
      onEnd: () => {
        if (!isPlaying) return;
        timerRef.current = setTimeout(() => {
          if (singleLoop) {
            playCurrent(idx);
          } else {
            const nextIdx = (idx + 1) % sentences.length;
            setCurrentIndex(nextIdx);
            playCurrent(nextIdx);
          }
        }, pauseDuration * 1000);
      }
    });
  };

  useEffect(() => {
    if (isPlaying) {
      playCurrent(currentIndex);
    } else {
      stopSpeaking();
      if (timerRef.current) clearTimeout(timerRef.current);
    }
    return () => {
      stopSpeaking();
      if (timerRef.current) clearTimeout(timerRef.current);
    };
  }, [isPlaying, currentIndex, singleLoop, pauseDuration]);

  const togglePlay = () => {
    setIsPlaying(prev => !prev);
  };

  return (
    <div className="w-full max-w-3xl mx-auto py-6 px-4">
      {/* 顶部控制栏 */}
      <div className="flex flex-wrap items-center justify-between gap-3 p-4 bg-white rounded-3xl border border-slate-200 shadow-sm mb-6">
        <div className="flex items-center gap-2">
          <button
            onClick={togglePlay}
            className={`flex items-center gap-2 px-5 py-2.5 rounded-2xl font-bold text-white shadow-md transition-all card-pressable ${
              isPlaying ? 'bg-amber-500 hover:bg-amber-600' : 'bg-brand-600 hover:bg-brand-700'
            }`}
          >
            {isPlaying ? <Pause className="w-4 h-4 fill-white" /> : <Play className="w-4 h-4 fill-white" />}
            <span>{isPlaying ? '暂停精听' : '开始自动连播'}</span>
          </button>

          <button
            onClick={() => setSingleLoop(prev => !prev)}
            className={`px-3 py-2 rounded-xl text-xs font-bold border transition-colors ${
              singleLoop
                ? 'bg-brand-100 text-brand-700 border-brand-300'
                : 'bg-slate-50 text-slate-600 border-slate-200'
            }`}
          >
            单句循环
          </button>
        </div>

        {/* 显隐控制与句间停留 */}
        <div className="flex items-center gap-2 text-xs">
          <button
            onClick={() => setHideEnglish(prev => !prev)}
            className="flex items-center gap-1 px-2.5 py-1.5 rounded-xl bg-slate-100 text-slate-700 hover:bg-slate-200 font-medium"
          >
            {hideEnglish ? <EyeOff className="w-3.5 h-3.5" /> : <Eye className="w-3.5 h-3.5" />}
            <span>{hideEnglish ? '隐藏英文' : '显示英文'}</span>
          </button>

          <button
            onClick={() => setHideChinese(prev => !prev)}
            className="flex items-center gap-1 px-2.5 py-1.5 rounded-xl bg-slate-100 text-slate-700 hover:bg-slate-200 font-medium"
          >
            {hideChinese ? <EyeOff className="w-3.5 h-3.5" /> : <Eye className="w-3.5 h-3.5" />}
            <span>{hideChinese ? '隐藏中文' : '显示中文'}</span>
          </button>
        </div>
      </div>

      {/* 句子精听列表与焦点卡片 */}
      <div className="space-y-3">
        {sentences.map((sent, idx) => {
          const isCurrent = idx === currentIndex;
          return (
            <div
              key={sent.id}
              onClick={() => {
                setCurrentIndex(idx);
                speakText(sent.english);
              }}
              className={`p-5 rounded-3xl border-2 transition-all cursor-pointer ${
                isCurrent
                  ? 'border-brand-500 bg-brand-50/40 shadow-md scale-[1.01]'
                  : 'border-slate-100 bg-white hover:border-slate-200 opacity-70'
              }`}
            >
              <div className="flex items-start justify-between gap-3">
                <div className="flex-1">
                  <p className={`text-base sm:text-lg font-bold leading-snug ${
                    isCurrent ? 'text-brand-900' : 'text-slate-700'
                  } ${hideEnglish && !isCurrent ? 'blur-sm select-none' : ''}`}>
                    {sent.english}
                  </p>
                  <p className={`text-sm text-slate-500 mt-1.5 ${
                    hideChinese && !isCurrent ? 'blur-sm select-none' : ''
                  }`}>
                    {sent.chinese}
                  </p>
                  {sent.phonetic && isCurrent && (
                    <p className="text-xs text-brand-600 mt-1 font-mono">{sent.phonetic}</p>
                  )}
                </div>

                <div className="flex items-center gap-2 shrink-0">
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      onJumpToPractice(idx);
                    }}
                    className="px-3 py-1.5 rounded-xl bg-white hover:bg-brand-50 text-brand-600 text-xs font-bold border border-slate-200 shadow-xs transition-all"
                  >
                    去拼写
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
