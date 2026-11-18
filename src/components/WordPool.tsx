import React, { useState, useEffect } from 'react';
import { Eye, EyeOff } from 'lucide-react';
import type { ChunkToken } from '../types';

interface WordPoolProps {
  poolTokens: ChunkToken[];
  isFinished: boolean;
  typedInput: string;
  onSelectToken: (token: ChunkToken) => void;
}

export const WordPool: React.FC<WordPoolProps> = ({
  poolTokens,
  isFinished,
  typedInput,
  onSelectToken
}) => {
  // 当用户在打字输入时是否手动强制揭示候选词
  const [forceShowWhileTyping, setForceShowWhileTyping] = useState(false);

  // 当用户打完一个词清空 typedInput 时，重置手动强制状态
  useEffect(() => {
    if (!typedInput) {
      setForceShowWhileTyping(false);
    }
  }, [typedInput]);

  // 全局快捷键 H：切换词卡提示
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.key === 'h' || e.key === 'H') && (e.ctrlKey || e.altKey || (!typedInput && e.target === document.body))) {
        e.preventDefault();
        setForceShowWhileTyping(prev => !prev);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [typedInput]);

  if (isFinished) {
    return (
      <div className="w-full max-w-2xl min-h-[70px] flex items-center justify-center py-3">
        <div className="flex items-center gap-2 text-emerald-600 font-bold text-sm sm:text-base animate-slide-up">
          <span className="text-xl">🎉</span>
          <span>整句拼写正确！查看下方联想扩展，或按 [Enter] 进入下一句</span>
        </div>
      </div>
    );
  }

  // 是否正在键盘盲打输入（且未点击强制展示提示）
  const isTypingActive = typedInput.trim().length > 0;
  const isPoolHidden = isTypingActive && !forceShowWhileTyping;

  return (
    <div className="w-full max-w-2xl flex flex-col items-center justify-center my-2 transition-all duration-300">
      {/* 打字中被隐藏时的轻量提示条与恢复按钮 */}
      {isTypingActive && (
        <div className="mb-2 animate-fade-in flex items-center gap-2">
          <button
            onClick={() => setForceShowWhileTyping(prev => !prev)}
            className={`flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold transition-all shadow-xs ${
              forceShowWhileTyping
                ? 'bg-amber-100 text-amber-800 border border-amber-300'
                : 'bg-white/80 hover:bg-white text-slate-500 hover:text-brand-600 border border-slate-200'
            }`}
            title="打字时默认隐藏卡片防剧透，点击可随时偷看 (或按快捷键 H)"
          >
            {forceShowWhileTyping ? (
              <>
                <EyeOff className="w-3.5 h-3.5 text-amber-600" />
                <span>隐藏选词卡片 (专注盲打)</span>
              </>
            ) : (
              <>
                <Eye className="w-3.5 h-3.5 text-brand-500" />
                <span>显示选词卡片 (卡壳求助)</span>
              </>
            )}
          </button>
          {!forceShowWhileTyping && (
            <span className="text-[11px] text-slate-400">正在盲打模式，已隐藏选词卡片</span>
          )}
        </div>
      )}

      {/* 词块卡片池主容器（具备平滑折叠、透明淡入淡出动画，不破坏页面布局） */}
      <div
        className={`w-full flex flex-wrap items-center justify-center gap-2.5 sm:gap-3.5 transition-all duration-300 origin-top ${
          isPoolHidden
            ? 'opacity-0 max-h-0 overflow-hidden py-0 pointer-events-none scale-95 -translate-y-2'
            : 'opacity-100 max-h-96 py-3 scale-100 translate-y-0'
        }`}
      >
        {poolTokens.map((token) => (
          <button
            key={`pool-${token.id}`}
            onClick={() => onSelectToken(token)}
            className="px-4 sm:px-5 py-2 sm:py-2.5 rounded-2xl bg-white hover:bg-slate-50 text-slate-800 font-bold text-sm sm:text-base border-2 border-slate-200/90 shadow-xs card-pressable active:scale-95 transition-all select-none"
          >
            {token.fullText}
          </button>
        ))}
      </div>
    </div>
  );
};
