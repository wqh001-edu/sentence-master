import React from 'react';
import { 
  ShoppingBag,
  Flame, 
  Settings as SettingsIcon, 
  Sparkles, 
  Headphones, 
  Languages, 
  Mic, 
  FileText,
  BookmarkCheck,
  PlusCircle,
  Layers
} from 'lucide-react';
import type { PracticeMode, SplitMode, UserSettings, UserStats } from '../types';

interface HeaderProps {
  currentCourseTitle: string;
  currentChapterTitle?: string;
  settings: UserSettings;
  stats: UserStats;
  onOpenMallModal: () => void;
  onOpenSettingsModal: () => void;
  onOpenCustomImportModal: () => void;
  onOpenMistakeModal: () => void;
  onUpdateSettings: (updater: (prev: UserSettings) => UserSettings) => void;
}

export const Header: React.FC<HeaderProps> = ({
  currentCourseTitle,
  currentChapterTitle,
  settings,
  stats,
  onOpenMallModal,
  onOpenSettingsModal,
  onOpenCustomImportModal,
  onOpenMistakeModal,
  onUpdateSettings
}) => {
  const modes: { id: PracticeMode; label: string; icon: React.ReactNode }[] = [
    { id: 'translate', label: '中译英', icon: <Languages className="w-4 h-4" /> },
    { id: 'dictation', label: '听写模式', icon: <Headphones className="w-4 h-4" /> },
    { id: 'listening', label: '听力精听', icon: <Sparkles className="w-4 h-4" /> },
    { id: 'speaking', label: '口语评测', icon: <Mic className="w-4 h-4" /> },
    { id: 'reading', label: '阅读模式', icon: <FileText className="w-4 h-4" /> },
  ];

  const splits: { id: SplitMode; label: string }[] = [
    { id: 'word', label: '从单词练' },
    { id: 'chunk', label: '从语块练' },
    { id: 'sentence', label: '只练整句' },
    { id: 'custom', label: '自定义' },
  ];

  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs">
      <div className="max-w-6xl mx-auto px-4 py-2.5 flex flex-col gap-2">
        {/* 顶部主工具栏 */}
        <div className="flex items-center justify-between gap-3">
          {/* Logo 与课程商城入口 */}
          <div className="flex items-center gap-2 sm:gap-3.5 min-w-0">
            <div className="flex items-center gap-1.5 font-bold text-lg text-slate-800 shrink-0">
              <span className="text-2xl">🧩</span>
              <span className="hidden sm:inline bg-gradient-to-r from-brand-600 to-indigo-600 bg-clip-text text-transparent font-extrabold tracking-tight">
                句乐通
              </span>
            </div>

            {/* 课程商城入口大按钮 */}
            <button
              onClick={onOpenMallModal}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-2xl bg-gradient-to-r from-brand-50 to-indigo-50 hover:from-brand-100 hover:to-indigo-100 text-brand-800 text-xs sm:text-sm font-extrabold transition-all border border-brand-200/80 shadow-xs truncate max-w-[200px] sm:max-w-xs card-pressable"
              title="点击进入全能课程商城选课"
            >
              <ShoppingBag className="w-4 h-4 text-brand-600 shrink-0" />
              <div className="flex items-center gap-1.5 truncate">
                <span className="truncate">{currentCourseTitle}</span>
                {currentChapterTitle && (
                  <span className="text-[11px] text-brand-600 font-normal truncate hidden md:inline">
                    · {currentChapterTitle}
                  </span>
                )}
              </div>
            </button>
          </div>

          {/* 右侧：语法标注开关、连胜打卡、错题本、导入与设置 */}
          <div className="flex items-center gap-1.5 sm:gap-2.5 shrink-0">
            {/* 语法成分分析开关 */}
            <button
              onClick={() => onUpdateSettings(prev => ({ ...prev, showGrammar: !prev.showGrammar }))}
              className={`flex items-center gap-1 px-2.5 py-1 rounded-xl text-xs font-bold border transition-all ${
                settings.showGrammar
                  ? 'bg-indigo-600 text-white border-indigo-700 shadow-xs'
                  : 'bg-slate-100 text-slate-600 border-slate-200 hover:bg-slate-200'
              }`}
              title="一键开启/折叠句法成分分析卡片"
            >
              <Layers className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">语法分析</span>
              <span>{settings.showGrammar ? '开' : '关'}</span>
            </button>

            {/* 连胜计数器 */}
            <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-amber-50 text-amber-700 text-xs font-bold border border-amber-200 shadow-xs">
              <Flame className="w-4 h-4 text-amber-500 fill-amber-500 animate-bounce" />
              <span>{stats.streak} 连胜</span>
            </div>

            {/* 错题本入口 */}
            <button
              onClick={onOpenMistakeModal}
              className="relative p-2 rounded-xl text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-colors"
              title="错题本与弱项强化"
            >
              <BookmarkCheck className="w-5 h-5 text-rose-500" />
              {stats.mistakeSentenceIds.length > 0 && (
                <span className="absolute -top-1 -right-1 px-1.5 py-0.2 bg-rose-500 text-white rounded-full text-[10px] font-bold">
                  {stats.mistakeSentenceIds.length}
                </span>
              )}
            </button>

            {/* 自定义导入 */}
            <button
              onClick={onOpenCustomImportModal}
              className="p-2 rounded-xl text-slate-600 hover:text-brand-600 hover:bg-slate-100 transition-colors hidden sm:block"
              title="一键粘贴导入自定义句子"
            >
              <PlusCircle className="w-5 h-5" />
            </button>

            {/* 设置按钮 */}
            <button
              onClick={onOpenSettingsModal}
              className="p-2 rounded-xl text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-colors"
              title="练习与发音偏好设置"
            >
              <SettingsIcon className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* 模式与拆分粒度选择器栏（响应式滚动条） */}
        <div className="flex items-center justify-between gap-3 overflow-x-auto no-scrollbar pt-1 pb-0.5 border-t border-slate-100">
          {/* 五大核心练习模式 */}
          <div className="flex items-center gap-1 shrink-0 bg-slate-100/90 p-0.5 rounded-xl border border-slate-200/50">
            {modes.map(m => {
              const active = settings.practiceMode === m.id;
              return (
                <button
                  key={m.id}
                  onClick={() => onUpdateSettings(prev => ({ ...prev, practiceMode: m.id }))}
                  className={`flex items-center gap-1 px-2.5 py-1 rounded-lg text-xs font-semibold transition-all ${
                    active
                      ? 'bg-white text-brand-700 shadow-xs scale-100'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  {m.icon}
                  <span>{m.label}</span>
                </button>
              );
            })}
          </div>

          {/* 四大拆分粒度 */}
          {(settings.practiceMode === 'translate' || settings.practiceMode === 'dictation') && (
            <div className="flex items-center gap-1 shrink-0 bg-slate-100/90 p-0.5 rounded-xl border border-slate-200/50">
              {splits.map(s => {
                const active = settings.splitMode === s.id;
                return (
                  <button
                    key={s.id}
                    onClick={() => onUpdateSettings(prev => ({ ...prev, splitMode: s.id }))}
                    className={`px-2.5 py-1 rounded-lg text-xs font-medium transition-all ${
                      active
                        ? 'bg-white text-brand-700 shadow-xs font-bold'
                        : 'text-slate-600 hover:text-slate-900'
                    }`}
                  >
                    {s.label}
                  </button>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </header>
  );
};
