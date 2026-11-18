import React from 'react';
import { ArrowLeft, BookOpen, CheckCircle, Play, Sparkles, X } from 'lucide-react';
import type { CoursePackage, Chapter } from '../types';

interface CourseDetailModalProps {
  course: CoursePackage;
  onBack: () => void;
  onClose: () => void;
  onSelectChapter: (course: CoursePackage, chapter: Chapter) => void;
  chapterProgressRecord?: Record<string, number>;
}

export const CourseDetailModal: React.FC<CourseDetailModalProps> = ({
  course,
  onBack,
  onClose,
  onSelectChapter,
  chapterProgressRecord = {}
}) => {
  const totalSentences = course.chapters.reduce((sum, ch) => sum + ch.sentences.length, 0);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-5 bg-slate-900/60 backdrop-blur-sm animate-fade-in">
      <div className="bg-white rounded-3xl w-full max-w-2xl max-h-[90vh] flex flex-col shadow-2xl border border-slate-100 overflow-hidden animate-slide-up">
        {/* 顶部课程横幅 */}
        <div className={`p-6 sm:p-8 bg-gradient-to-r ${course.coverGradient} text-white relative shrink-0`}>
          <div className="flex items-center justify-between mb-4">
            <button
              onClick={onBack}
              className="flex items-center gap-1 px-3 py-1.5 rounded-xl bg-white/20 hover:bg-white/30 backdrop-blur-md text-white text-xs font-bold transition-all"
            >
              <ArrowLeft className="w-4 h-4" />
              <span>返回商城</span>
            </button>
            <button
              onClick={onClose}
              className="p-1.5 rounded-xl bg-white/20 hover:bg-white/30 backdrop-blur-md text-white transition-all"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          <div className="flex items-start gap-4">
            <span className="text-4xl sm:text-5xl shrink-0 p-3 bg-white/15 backdrop-blur-md rounded-2xl shadow-inner">
              {course.icon}
            </span>
            <div className="flex-1">
              <div className="flex items-center gap-2 mb-1.5">
                <span className="px-2.5 py-0.5 rounded-full bg-white/25 backdrop-blur-md text-[11px] font-bold text-white tracking-wide">
                  {course.categoryName}
                </span>
                <span className="px-2.5 py-0.5 rounded-full bg-black/20 text-[11px] font-bold text-amber-200">
                  {course.difficulty}
                </span>
              </div>
              <h2 className="text-xl sm:text-2xl font-extrabold text-white leading-tight">
                {course.title}
              </h2>
              <p className="text-xs sm:text-sm text-white/80 mt-2 line-clamp-2 leading-relaxed">
                {course.description}
              </p>
              <div className="flex items-center gap-4 mt-3 text-xs font-semibold text-white/90">
                <span>共 {course.chapters.length} 个章节</span>
                <span>•</span>
                <span>包含 {totalSentences} 句地道原声表达</span>
              </div>
            </div>
          </div>
        </div>

        {/* 章节目录列表 */}
        <div className="flex-1 p-4 sm:p-6 overflow-y-auto space-y-3 bg-slate-50/50">
          <div className="flex items-center justify-between px-1 mb-2">
            <h4 className="font-extrabold text-slate-800 text-sm flex items-center gap-2">
              <BookOpen className="w-4 h-4 text-brand-600" />
              <span>章节目录 · 点击直接开始逐句练习</span>
            </h4>
            <span className="text-xs text-slate-400">支持任意章节自由切换</span>
          </div>

          {course.chapters.map((chapter, idx) => {
            const completedCount = chapterProgressRecord[chapter.id] || 0;
            const isCompleted = completedCount >= chapter.sentences.length && chapter.sentences.length > 0;

            return (
              <div
                key={chapter.id}
                onClick={() => onSelectChapter(course, chapter)}
                className="group p-4 rounded-2xl bg-white hover:bg-brand-50/40 border border-slate-200/80 hover:border-brand-300 shadow-xs hover:shadow-md transition-all cursor-pointer flex items-center justify-between gap-3 card-pressable"
              >
                <div className="flex items-center gap-3.5 flex-1 min-w-0">
                  <div className="w-8 h-8 rounded-xl bg-slate-100 group-hover:bg-brand-100 text-slate-600 group-hover:text-brand-700 font-extrabold text-xs flex items-center justify-center shrink-0 transition-colors">
                    {idx + 1}
                  </div>
                  <div className="truncate">
                    <h5 className="font-bold text-slate-800 group-hover:text-brand-700 text-sm sm:text-base truncate transition-colors">
                      {chapter.title}
                    </h5>
                    {chapter.description && (
                      <p className="text-xs text-slate-400 mt-0.5 truncate">
                        {chapter.description}
                      </p>
                    )}
                    <div className="flex items-center gap-2 mt-1.5 text-[11px] text-slate-500 font-medium">
                      <span className="flex items-center gap-1">
                        <Sparkles className="w-3 h-3 text-amber-500" />
                        {chapter.sentences.length} 句
                      </span>
                      {completedCount > 0 && (
                        <span className="text-emerald-600 font-bold">
                          • 已学 {completedCount}/{chapter.sentences.length}
                        </span>
                      )}
                    </div>
                  </div>
                </div>

                <div className="shrink-0 flex items-center gap-2">
                  {isCompleted ? (
                    <div className="flex items-center gap-1 text-emerald-600 font-bold text-xs bg-emerald-50 px-2.5 py-1 rounded-xl border border-emerald-200">
                      <CheckCircle className="w-4 h-4" />
                      <span>已掌握</span>
                    </div>
                  ) : (
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        onSelectChapter(course, chapter);
                      }}
                      className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-brand-600 hover:bg-brand-700 text-white font-bold text-xs shadow-md shadow-brand-500/20 transition-all card-pressable"
                    >
                      <Play className="w-3.5 h-3.5 fill-white" />
                      <span>练这章</span>
                    </button>
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
