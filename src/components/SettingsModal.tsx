import React from 'react';
import { Settings as SettingsIcon, Volume2, Music, RotateCcw, X, Download, Upload } from 'lucide-react';
import type { UserSettings, UserStats } from '../types';

interface SettingsModalProps {
  isOpen: boolean;
  onClose: () => void;
  settings: UserSettings;
  stats: UserStats;
  onUpdateSettings: (updater: (prev: UserSettings) => UserSettings) => void;
  onResetStats: () => void;
}

export const SettingsModal: React.FC<SettingsModalProps> = ({
  isOpen,
  onClose,
  settings,
  stats,
  onUpdateSettings,
  onResetStats
}) => {
  if (!isOpen) return null;

  const handleExportData = () => {
    const data = {
      settings,
      stats,
      customLessons: localStorage.getItem('jlt_custom_lessons'),
      timestamp: new Date().toISOString()
    };
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `julebu_backup_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleImportData = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (event) => {
      try {
        const parsed = JSON.parse(event.target?.result as string);
        if (parsed.customLessons) {
          localStorage.setItem('jlt_custom_lessons', parsed.customLessons);
        }
        alert('数据恢复成功，请刷新页面生效！');
        window.location.reload();
      } catch (err) {
        alert('备份文件格式有误');
      }
    };
    reader.readAsText(file);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-xs animate-fade-in">
      <div className="bg-white rounded-3xl w-full max-w-lg shadow-2xl border border-slate-100 overflow-hidden animate-slide-up">
        {/* 头部 */}
        <div className="px-6 py-4 border-b border-slate-100 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <SettingsIcon className="w-5 h-5 text-slate-700" />
            <h3 className="text-lg font-bold text-slate-800">学习与系统偏好</h3>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-xl text-slate-400 hover:text-slate-600 hover:bg-slate-100 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* 设置项列表 */}
        <div className="p-6 space-y-4">
          {/* 自动发音开关 */}
          <div className="flex items-center justify-between p-3 rounded-2xl bg-slate-50 border border-slate-100">
            <div className="flex items-center gap-3">
              <div className="p-2 rounded-xl bg-indigo-100 text-indigo-700">
                <Volume2 className="w-4 h-4" />
              </div>
              <div>
                <p className="text-sm font-bold text-slate-800">切句时自动朗读</p>
                <p className="text-xs text-slate-400">切换新句子时自动播放纯正真人发音</p>
              </div>
            </div>
            <input
              type="checkbox"
              checked={settings.autoSpeak}
              onChange={(e) => onUpdateSettings(prev => ({ ...prev, autoSpeak: e.target.checked }))}
              className="w-5 h-5 accent-brand-600 cursor-pointer"
            />
          </div>

          {/* 交互音效反馈 */}
          <div className="flex items-center justify-between p-3 rounded-2xl bg-slate-50 border border-slate-100">
            <div className="flex items-center gap-3">
              <div className="p-2 rounded-xl bg-emerald-100 text-emerald-700">
                <Music className="w-4 h-4" />
              </div>
              <div>
                <p className="text-sm font-bold text-slate-800">答题音效反馈</p>
                <p className="text-xs text-slate-400">答对清脆叮咚、连胜升级、答错微颤蜂鸣</p>
              </div>
            </div>
            <input
              type="checkbox"
              checked={settings.soundEffects}
              onChange={(e) => onUpdateSettings(prev => ({ ...prev, soundEffects: e.target.checked }))}
              className="w-5 h-5 accent-brand-600 cursor-pointer"
            />
          </div>

          {/* 备份与同步 */}
          <div className="p-3 rounded-2xl bg-slate-50 border border-slate-100 flex items-center justify-between">
            <div>
              <p className="text-sm font-bold text-slate-800">数据备份与跨端迁移</p>
              <p className="text-xs text-slate-400">一键导出进度与题库为 JSON 文件</p>
            </div>
            <div className="flex items-center gap-2">
              <button
                onClick={handleExportData}
                className="flex items-center gap-1 px-3 py-1.5 rounded-xl bg-white border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-100"
              >
                <Download className="w-3.5 h-3.5" /> 导出
              </button>
              <label className="flex items-center gap-1 px-3 py-1.5 rounded-xl bg-white border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-100 cursor-pointer">
                <Upload className="w-3.5 h-3.5" /> 恢复
                <input type="file" accept=".json" onChange={handleImportData} className="hidden" />
              </label>
            </div>
          </div>

          {/* 重置进度 */}
          <div className="pt-2">
            <button
              onClick={() => {
                if (confirm('确认清空所有学习历史与连胜记录吗？')) {
                  onResetStats();
                }
              }}
              className="flex items-center gap-1.5 text-xs text-rose-500 hover:text-rose-700 font-semibold transition-colors mx-auto"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              <span>清空练习进度与重置连胜</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
