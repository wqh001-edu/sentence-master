import React from 'react';
import { Book, CheckCircle2, Sparkles, X } from 'lucide-react';
import type { Lesson } from '../types';

interface BookSelectorModalProps {
  isOpen: boolean;
  lessons: Lesson[];
  currentLessonId: string;
  onSelectLesson: (lesson: Lesson) => void;
  onClose: () => void;
}

export const BookSelectorModal: React.FC<BookSelectorModalProps> = ({
  isOpen,
  lessons,
  currentLessonId,
  onSelectLesson,
  onClose
}) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-xs animate-fade-in">
      <div className="bg-white rounded-3xl w-full max-w-xl max-h-[85vh] flex flex-col shadow-2xl border border-slate-100 overflow-hidden animate-slide-up">
        {/* 头部 */}
        <div className="px-6 py-4 border-b border-slate-100 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Book className="w-5 h-5 text-brand-600" />
            <h3 className="text-lg font-bold text-slate-800">精选教材与语料库</h3>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-xl text-slate-400 hover:text-slate-600 hover:bg-slate-100 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* 课程列表 */}
        <div className="p-4 sm:p-6 overflow-y-auto space-y-3">
          {lessons.map((lesson) => {
            const isSelected = lesson.id === currentLessonId;
            return (
              <div
                key={lesson.id}
                onClick={() => {
                  onSelectLesson(lesson);
                  onClose();
                }}
                className={`p-4 rounded-2xl border-2 transition-all cursor-pointer flex items-start justify-between gap-3 ${
                  isSelected
                    ? 'border-brand-500 bg-brand-50/40 shadow-xs'
                    : 'border-slate-100 hover:border-slate-300 hover:bg-slate-50/60'
                }`}
              >
                <div className="flex-1">
                  <div className="flex items-center gap-2">
                    <h4 className="font-bold text-slate-800 text-sm sm:text-base">
                      {lesson.title}
                    </h4>
                    {lesson.category === 'new_concept' && (
                      <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-100 text-amber-700">
                        经典教材
                      </span>
                    )}
                    {lesson.category === 'custom' && (
                      <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-purple-100 text-purple-700">
                        自建题库
                      </span>
                    )}
                  </div>
                  <p className="text-xs text-slate-500 mt-1 line-clamp-2 leading-relaxed">
                    {lesson.description}
                  </p>
                  <div className="flex items-center gap-3 mt-2 text-xs font-semibold text-slate-400">
                    <span className="flex items-center gap-1">
                      <Sparkles className="w-3.5 h-3.5 text-brand-500" />
                      共 {lesson.sentences.length} 句
                    </span>
                  </div>
                </div>

                <div className="shrink-0 mt-1">
                  {isSelected ? (
                    <CheckCircle2 className="w-5 h-5 text-brand-600" />
                  ) : (
                    <div className="w-5 h-5 rounded-full border-2 border-slate-200" />
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
