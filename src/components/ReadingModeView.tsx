import React, { useState } from 'react';
import { Volume2, Play, BookOpen } from 'lucide-react';
import type { SentenceItem, UserSettings } from '../types';
import { speakText } from '../utils/tts';

interface ReadingModeViewProps {
  sentences: SentenceItem[];
  settings: UserSettings;
  onJumpToPractice: (index: number) => void;
}

export const ReadingModeView: React.FC<ReadingModeViewProps> = ({
  sentences,
  settings,
  onJumpToPractice
}) => {
  const [selectedWord, setSelectedWord] = useState<string | null>(null);

  const handleWordClick = (word: string, e: React.MouseEvent) => {
    e.stopPropagation();
    const clean = word.replace(/[^a-zA-Z]/g, '');
    if (!clean) return;
    setSelectedWord(clean);
    speakText(clean, { rate: settings.speechRate, accent: settings.accent });
  };

  return (
    <div className="w-full max-w-3xl mx-auto py-6 px-4">
      {/* 顶部说明 */}
      <div className="p-4 rounded-3xl bg-white border border-slate-200/80 shadow-xs mb-6 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <BookOpen className="w-5 h-5 text-brand-600" />
          <div>
            <h3 className="text-sm font-bold text-slate-800">篇章沉浸阅读</h3>
            <p className="text-xs text-slate-400">点击单词即时朗读查音，点击“拼写”强化肌肉记忆</p>
          </div>
        </div>

        {selectedWord && (
          <div className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-brand-50 border border-brand-200 animate-pop">
            <span className="text-xs font-bold text-brand-700">正在查词: {selectedWord}</span>
            <button
              onClick={() => speakText(selectedWord)}
              className="text-brand-600 hover:text-brand-800"
            >
              <Volume2 className="w-3.5 h-3.5" />
            </button>
          </div>
        )}
      </div>

      {/* 句子段落流 */}
      <div className="space-y-4">
        {sentences.map((sent, idx) => {
          const words = sent.english.split(' ');
          return (
            <div
              key={sent.id}
              className="p-5 rounded-3xl bg-white border border-slate-200/90 hover:border-brand-300 hover:shadow-xs transition-all group"
            >
              <div className="flex items-start justify-between gap-3">
                <div className="flex-1">
                  {/* 可点击的交互式单词流 */}
                  <div className="text-base sm:text-lg font-semibold text-slate-800 leading-relaxed">
                    {words.map((w, wIdx) => (
                      <span
                        key={wIdx}
                        onClick={(e) => handleWordClick(w, e)}
                        className="inline-block hover:text-brand-600 hover:underline cursor-pointer mr-1.5 transition-colors rounded px-0.5"
                      >
                        {w}
                      </span>
                    ))}
                  </div>

                  <p className="text-sm text-slate-500 mt-2 font-medium">
                    {sent.chinese}
                  </p>

                  {sent.note && (
                    <p className="text-xs text-amber-700 bg-amber-50 px-2 py-0.5 rounded-md inline-block mt-2">
                      💡 {sent.note}
                    </p>
                  )}
                </div>

                <div className="flex items-center gap-2 shrink-0 opacity-80 group-hover:opacity-100 transition-opacity">
                  <button
                    onClick={() => speakText(sent.english, { rate: settings.speechRate, accent: settings.accent })}
                    className="p-2 rounded-xl text-slate-500 hover:text-brand-600 hover:bg-brand-50 transition-colors"
                    title="整句朗读"
                  >
                    <Volume2 className="w-4 h-4" />
                  </button>
                  <button
                    onClick={() => onJumpToPractice(idx)}
                    className="flex items-center gap-1 px-3 py-1.5 rounded-xl bg-brand-50 hover:bg-brand-100 text-brand-700 text-xs font-bold transition-colors"
                  >
                    <Play className="w-3 h-3 fill-brand-700" />
                    <span>去拼</span>
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
