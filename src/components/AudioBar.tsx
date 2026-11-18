import React from 'react';
import { Volume2, HelpCircle, ArrowRight, RotateCcw } from 'lucide-react';
import type { UserSettings } from '../types';

interface AudioBarProps {
  currentIndex: number;
  totalSentences: number;
  isFinished: boolean;
  showHint: boolean;
  settings: UserSettings;
  onReplayAudio: () => void;
  onToggleHint: () => void;
  onNextSentence: () => void;
  onPrevSentence: () => void;
  onUpdateSettings: (updater: (prev: UserSettings) => UserSettings) => void;
}

export const AudioBar: React.FC<AudioBarProps> = ({
  currentIndex,
  totalSentences,
  isFinished,
  showHint,
  settings,
  onReplayAudio,
  onToggleHint,
  onNextSentence,
  onPrevSentence,
  onUpdateSettings
}) => {
  const speeds = [0.75, 1.0, 1.25];

  const handleCycleSpeed = () => {
    const nextIdx = (speeds.indexOf(settings.speechRate) + 1) % speeds.length;
    onUpdateSettings(prev => ({ ...prev, speechRate: speeds[nextIdx] }));
  };

  const handleToggleAccent = () => {
    onUpdateSettings(prev => ({
      ...prev,
      accent: prev.accent === 'en-US' ? 'en-GB' : 'en-US'
    }));
  };

  return (
    <div className="fixed bottom-0 left-0 right-0 z-30 bg-white/95 backdrop-blur-md border-t border-slate-200/90 py-3 px-4 shadow-lg">
      <div className="max-w-4xl mx-auto flex items-center justify-between gap-2 sm:gap-4">
        {/* 左侧：发音播放与语音微调 */}
        <div className="flex items-center gap-1.5 sm:gap-2">
          {/* 发音重播主按钮 */}
          <button
            onClick={onReplayAudio}
            className="flex items-center gap-1.5 px-3 sm:px-4 py-2 sm:py-2.5 rounded-2xl bg-brand-50 hover:bg-brand-100 text-brand-700 font-bold text-xs sm:text-sm border border-brand-200/80 transition-all card-pressable"
            title="播放/重播英文原音 (Ctrl + 空格)"
          >
            <Volume2 className="w-4 h-4 text-brand-600" />
            <span className="hidden sm:inline">听发音</span>
          </button>

          {/* 语速调节 */}
          <button
            onClick={handleCycleSpeed}
            className="px-2.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition-colors"
            title="切换发音语速"
          >
            {settings.speechRate}x
          </button>

          {/* 英音 / 美音 */}
          <button
            onClick={handleToggleAccent}
            className="px-2.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition-colors"
            title="切换美音(US) / 英音(UK)"
          >
            {settings.accent === 'en-US' ? '美音' : '英音'}
          </button>

          {/* 查看提示 */}
          <button
            onClick={onToggleHint}
            className={`p-2 rounded-xl transition-colors ${
              showHint
                ? 'bg-amber-100 text-amber-700'
                : 'bg-slate-100 hover:bg-slate-200 text-slate-600'
            }`}
            title="揭晓参考答案 (Tab)"
          >
            <HelpCircle className="w-4 h-4" />
          </button>
        </div>

        {/* 中间：关卡进度指示器 */}
        <div className="flex items-center gap-2 text-xs sm:text-sm font-semibold text-slate-500">
          <div className="w-20 sm:w-28 h-2 rounded-full bg-slate-100 overflow-hidden border border-slate-200/60">
            <div
              className="h-full bg-brand-500 rounded-full transition-all duration-300"
              style={{ width: `${((currentIndex + 1) / totalSentences) * 100}%` }}
            />
          </div>
          <span className="tabular-nums">
            {currentIndex + 1} / {totalSentences}
          </span>
        </div>

        {/* 右侧：下一题 / 下一句 */}
        <div className="flex items-center gap-2">
          {currentIndex > 0 && (
            <button
              onClick={onPrevSentence}
              className="p-2 sm:px-3 sm:py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-600 text-xs font-semibold transition-colors"
              title="上一句"
            >
              <RotateCcw className="w-4 h-4" />
            </button>
          )}

          <button
            onClick={onNextSentence}
            className={`flex items-center gap-1.5 px-4 sm:px-6 py-2 sm:py-2.5 rounded-2xl font-bold text-xs sm:text-sm transition-all card-pressable ${
              isFinished
                ? 'bg-emerald-500 hover:bg-emerald-600 text-white shadow-md shadow-emerald-500/20 animate-pulse'
                : 'bg-slate-900 hover:bg-slate-800 text-white'
            }`}
          >
            <span>{isFinished ? '下一句 (Enter)' : '跳过此句'}</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
};
