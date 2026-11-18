import React from 'react';
import { BookmarkCheck, Volume2, Trash2, Play, X } from 'lucide-react';
import type { SentenceItem, Lesson } from '../types';
import { speakText } from '../utils/tts';

interface MistakeBookModalProps {
  isOpen: boolean;
  onClose: () => void;
  mistakeSentences: SentenceItem[];
  onRemoveMistake: (id: string) => void;
  onStartMistakePractice: (mistakeLesson: Lesson) => void;
}

export const MistakeBookModal: React.FC<MistakeBookModalProps> = ({
  isOpen,
  onClose,
  mistakeSentences,
  onRemoveMistake,
  onStartMistakePractice
}) => {
  if (!isOpen) return null;

  const handleStartPractice = () => {
    if (mistakeSentences.length === 0) return;
    const mistakeLesson: Lesson = {
      id: `mistake-lesson-${Date.now()}`,
      title: '🎯 专项错题特训营',
      description: `针对您在练习中出现错误的 ${mistakeSentences.length} 个难句进行强化突破。`,
      category: 'custom',
      sentences: mistakeSentences
    };
    onStartMistakePractice(mistakeLesson);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-xs animate-fade-in">
      <div className="bg-white rounded-3xl w-full max-w-2xl max-h-[85vh] flex flex-col shadow-2xl border border-slate-100 overflow-hidden animate-slide-up">
        {/* 头部 */}
        <div className="px-6 py-4 border-b border-slate-100 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <BookmarkCheck className="w-5 h-5 text-rose-500" />
            <h3 className="text-lg font-bold text-slate-800">
              错题本与弱项归集 ({mistakeSentences.length})
            </h3>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-xl text-slate-400 hover:text-slate-600 hover:bg-slate-100 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* 错题列表 */}
        <div className="p-4 sm:p-6 overflow-y-auto space-y-3">
          {mistakeSentences.length === 0 ? (
            <div className="py-12 text-center text-slate-400">
              <span className="text-4xl block mb-2">🎉</span>
              <p className="font-bold text-slate-600">太棒了！当前没有任何错题记录</p>
              <p className="text-xs text-slate-400 mt-1">在拼写中答错的句子会自动归集到这里进行复习</p>
            </div>
          ) : (
            mistakeSentences.map((sent) => (
              <div
                key={sent.id}
                className="p-4 rounded-2xl border border-slate-200/80 bg-slate-50/50 hover:bg-white hover:border-brand-200 hover:shadow-xs transition-all flex items-start justify-between gap-3"
              >
                <div className="flex-1">
                  <p className="font-bold text-slate-800 text-sm sm:text-base leading-snug">
                    {sent.english}
                  </p>
                  <p className="text-xs sm:text-sm text-slate-500 mt-1">
                    {sent.chinese}
                  </p>
                  {sent.note && (
                    <p className="text-xs text-amber-700 bg-amber-50 px-2 py-0.5 rounded-md inline-block mt-1.5">
                      💡 {sent.note}
                    </p>
                  )}
                </div>

                <div className="flex items-center gap-1.5 shrink-0 mt-0.5">
                  <button
                    onClick={() => speakText(sent.english)}
                    className="p-2 rounded-xl text-brand-600 hover:bg-brand-50 transition-colors"
                    title="听发音"
                  >
                    <Volume2 className="w-4 h-4" />
                  </button>
                  <button
                    onClick={() => onRemoveMistake(sent.id)}
                    className="p-2 rounded-xl text-slate-400 hover:text-rose-600 hover:bg-rose-50 transition-colors"
                    title="移出错题本"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>
              </div>
            ))
          )}
        </div>

        {/* 底部 */}
        {mistakeSentences.length > 0 && (
          <div className="px-6 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
            <span className="text-xs text-slate-500">
              多练易错题，突破肌肉记忆瓶颈
            </span>
            <button
              onClick={handleStartPractice}
              className="flex items-center gap-2 px-5 py-2.5 rounded-2xl bg-rose-600 hover:bg-rose-700 text-white text-xs sm:text-sm font-bold shadow-md shadow-rose-500/20 transition-all card-pressable"
            >
              <Play className="w-4 h-4 fill-white" />
              <span>开始错题强化特训</span>
            </button>
          </div>
        )}
      </div>
    </div>
  );
};
