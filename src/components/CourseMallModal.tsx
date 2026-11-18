import React, { useState, useMemo } from 'react';
import { 
  Search, 
  X, 
  Play, 
  RotateCcw, 
  Layers, 
  Sparkles
} from 'lucide-react';
import type { CoursePackage, CourseCategory, DifficultyLevel, Chapter, UserStats } from '../types';
import { CATEGORIES, ALL_COURSES, searchCourses } from '../data/mall';
import { CourseDetailModal } from './CourseDetailModal';

interface CourseMallModalProps {
  isOpen: boolean;
  onClose: () => void;
  stats: UserStats;
  onSelectChapterToPractice: (course: CoursePackage, chapter: Chapter) => void;
}

export const CourseMallModal: React.FC<CourseMallModalProps> = ({
  isOpen,
  onClose,
  stats,
  onSelectChapterToPractice
}) => {
  const [selectedCategory, setSelectedCategory] = useState<CourseCategory | 'all'>('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedDifficulty, setSelectedDifficulty] = useState<DifficultyLevel | 'all'>('all');
  const [detailCourse, setDetailCourse] = useState<CoursePackage | null>(null);

  const difficulties: (DifficultyLevel | 'all')[] = ['all', '入门 A1', '初级 A2', '中级 B1', '中高 B2', '高级 C1'];

  // 课程包过滤计算
  const filteredCourses = useMemo(() => {
    return searchCourses(
      searchQuery,
      selectedCategory === 'all' ? undefined : selectedCategory,
      selectedDifficulty === 'all' ? undefined : selectedDifficulty
    );
  }, [searchQuery, selectedCategory, selectedDifficulty]);

  // 最近学习的课程与章节定位
  const lastStudied = stats.lastStudied;
  const lastStudiedCourse = useMemo(() => {
    if (!lastStudied) return null;
    return ALL_COURSES.find(c => c.id === lastStudied.courseId) || null;
  }, [lastStudied]);

  if (!isOpen) return null;

  const handleOpenDetail = (course: CoursePackage) => {
    setDetailCourse(course);
  };

  const handleSelectChapter = (course: CoursePackage, chapter: Chapter) => {
    setDetailCourse(null);
    onSelectChapterToPractice(course, chapter);
    onClose();
  };

  return (
    <>
      <div className="fixed inset-0 z-40 flex items-center justify-center p-2 sm:p-5 bg-slate-900/60 backdrop-blur-md animate-fade-in">
        <div className="bg-white rounded-3xl w-full max-w-5xl h-[92vh] flex flex-col shadow-2xl border border-slate-100 overflow-hidden animate-slide-up">
          {/* 1. 商城头部栏 */}
          <div className="px-5 sm:px-8 py-4 border-b border-slate-100 flex items-center justify-between gap-3 bg-white/95">
            <div className="flex items-center gap-2.5">
              <span className="text-2xl sm:text-3xl">🏛️</span>
              <div>
                <h2 className="text-lg sm:text-xl font-extrabold text-slate-800">
                  句乐通 · 课程与语料商城
                </h2>
                <p className="text-xs text-slate-400 hidden sm:block">
                  9大分类 · 72+ 精品课程包 · 全真实地道英美原声语料
                </p>
              </div>
            </div>

            {/* 搜索框 */}
            <div className="flex items-center gap-2 flex-1 max-w-xs sm:max-w-md mx-2">
              <div className="relative w-full">
                <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
                <input
                  type="text"
                  placeholder="搜索课程、关键词、考点..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full pl-9 pr-4 py-2 rounded-2xl bg-slate-100 focus:bg-white text-xs sm:text-sm border border-transparent focus:border-brand-500 focus:ring-2 focus:ring-brand-100 focus:outline-hidden transition-all"
                />
                {searchQuery && (
                  <button
                    onClick={() => setSearchQuery('')}
                    className="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 text-xs"
                  >
                    ✕
                  </button>
                )}
              </div>
            </div>

            <button
              onClick={onClose}
              className="p-2 rounded-2xl text-slate-400 hover:text-slate-700 hover:bg-slate-100 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* 2. 横向滑动的 9 大分类导航 Tabs */}
          <div className="px-5 sm:px-8 py-2.5 bg-slate-50/70 border-b border-slate-100 overflow-x-auto no-scrollbar flex items-center gap-2 shrink-0">
            <button
              onClick={() => setSelectedCategory('all')}
              className={`flex items-center gap-1.5 px-4 py-2 rounded-2xl text-xs sm:text-sm font-bold whitespace-nowrap transition-all card-pressable ${
                selectedCategory === 'all'
                  ? 'bg-slate-900 text-white shadow-sm'
                  : 'bg-white text-slate-600 hover:bg-slate-100 border border-slate-200/80'
              }`}
            >
              <span>🌐</span>
              <span>全部课程 ({ALL_COURSES.length})</span>
            </button>

            {CATEGORIES.map((cat) => {
              const isActive = selectedCategory === cat.id;
              return (
                <button
                  key={cat.id}
                  onClick={() => setSelectedCategory(cat.id)}
                  className={`flex items-center gap-1.5 px-4 py-2 rounded-2xl text-xs sm:text-sm font-bold whitespace-nowrap transition-all card-pressable ${
                    isActive
                      ? 'bg-brand-600 text-white shadow-md shadow-brand-500/20'
                      : 'bg-white text-slate-600 hover:bg-slate-100 border border-slate-200/80'
                  }`}
                >
                  <span>{cat.icon}</span>
                  <span>{cat.name}</span>
                </button>
              );
            })}
          </div>

          {/* 3. 难度快速筛选器 */}
          <div className="px-5 sm:px-8 py-2 border-b border-slate-100 flex items-center justify-between gap-2 overflow-x-auto no-scrollbar text-xs">
            <div className="flex items-center gap-1.5 shrink-0 text-slate-500 font-semibold">
              <Layers className="w-3.5 h-3.5 text-brand-600" />
              <span>按难度筛选：</span>
            </div>
            <div className="flex items-center gap-1.5 shrink-0">
              {difficulties.map((diff) => {
                const isActive = selectedDifficulty === diff;
                return (
                  <button
                    key={diff}
                    onClick={() => setSelectedDifficulty(diff)}
                    className={`px-3 py-1 rounded-xl font-bold transition-all ${
                      isActive
                        ? 'bg-brand-100 text-brand-800 border border-brand-300'
                        : 'text-slate-500 hover:text-slate-800 hover:bg-slate-100'
                    }`}
                  >
                    {diff === 'all' ? '全部难度' : diff}
                  </button>
                );
              })}
            </div>
          </div>

          {/* 4. 课程包网格内容主体 */}
          <div className="flex-1 p-5 sm:p-8 overflow-y-auto space-y-6">
            {/* 快捷入口：继续上次学习 */}
            {lastStudied && lastStudiedCourse && (
              <div className="p-4 sm:p-5 rounded-3xl bg-gradient-to-r from-brand-600 to-indigo-700 text-white shadow-lg flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 animate-slide-up">
                <div className="flex items-center gap-3.5">
                  <span className="text-3xl p-2.5 bg-white/15 rounded-2xl">
                    {lastStudiedCourse.icon}
                  </span>
                  <div>
                    <div className="flex items-center gap-2">
                      <span className="px-2 py-0.5 rounded-full bg-white/20 text-[10px] font-bold text-amber-200">
                        上次学习进度
                      </span>
                      <span className="text-xs text-white/80">
                        {lastStudiedCourse.title}
                      </span>
                    </div>
                    <h4 className="text-base sm:text-lg font-extrabold text-white mt-0.5">
                      {lastStudied.chapterTitle || '当前章节'}
                    </h4>
                  </div>
                </div>

                <button
                  onClick={() => {
                    const chapter = lastStudiedCourse.chapters.find(c => c.id === lastStudied.chapterId) || lastStudiedCourse.chapters[0];
                    handleSelectChapter(lastStudiedCourse, chapter);
                  }}
                  className="flex items-center gap-2 px-5 py-2.5 rounded-2xl bg-white text-brand-700 font-extrabold text-xs sm:text-sm shadow-md hover:bg-slate-50 transition-all card-pressable shrink-0"
                >
                  <RotateCcw className="w-4 h-4" />
                  <span>一键继续学习</span>
                </button>
              </div>
            )}

            {/* 课程列表卡片网格 */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-5">
              {filteredCourses.map((course) => {
                const totalSents = course.chapters.reduce((sum, ch) => sum + ch.sentences.length, 0);

                return (
                  <div
                    key={course.id}
                    onClick={() => handleOpenDetail(course)}
                    className="group relative rounded-3xl bg-white border border-slate-200/80 hover:border-brand-300 shadow-xs hover:shadow-xl transition-all cursor-pointer flex flex-col overflow-hidden card-pressable"
                  >
                    {/* 封面渐变上部 */}
                    <div className={`p-4 bg-gradient-to-r ${course.coverGradient} text-white flex items-center justify-between`}>
                      <span className="text-3xl p-2 bg-white/15 backdrop-blur-md rounded-2xl">
                        {course.icon}
                      </span>
                      <span className="px-2.5 py-1 rounded-full bg-black/25 text-[11px] font-bold text-amber-200">
                        {course.difficulty}
                      </span>
                    </div>

                    {/* 课程信息主体 */}
                    <div className="p-5 flex-1 flex flex-col justify-between">
                      <div>
                        <div className="flex items-center gap-2 mb-1.5">
                          <span className="text-xs text-brand-600 font-bold">
                            {course.categoryName}
                          </span>
                        </div>
                        <h3 className="font-extrabold text-slate-800 group-hover:text-brand-600 text-base leading-snug line-clamp-1 transition-colors">
                          {course.title}
                        </h3>
                        <p className="text-xs text-slate-500 mt-2 line-clamp-2 leading-relaxed">
                          {course.description}
                        </p>
                      </div>

                      {/* 底部信息与标签 */}
                      <div className="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs text-slate-400 font-medium">
                        <span className="flex items-center gap-1 text-slate-600 font-bold">
                          <Sparkles className="w-3.5 h-3.5 text-amber-500" />
                          {course.chapters.length} 章节 · {totalSents} 句
                        </span>
                        <span className="text-brand-600 font-bold group-hover:translate-x-0.5 transition-transform flex items-center gap-1">
                          查看目录 <Play className="w-3 h-3 fill-brand-600" />
                        </span>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>

            {filteredCourses.length === 0 && (
              <div className="py-20 text-center text-slate-400">
                <span className="text-4xl block mb-2">🔍</span>
                <p className="font-bold text-slate-600">未找到符合条件的课程包</p>
                <p className="text-xs text-slate-400 mt-1">请尝试更换分类或调整搜索关键字</p>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* 课程包详情抽屉 */}
      {detailCourse && (
        <CourseDetailModal
          course={detailCourse}
          onBack={() => setDetailCourse(null)}
          onClose={() => setDetailCourse(null)}
          onSelectChapter={handleSelectChapter}
          chapterProgressRecord={stats.chapterProgress}
        />
      )}
    </>
  );
};
