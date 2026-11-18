import React from 'react';
import type { ChunkToken } from '../types';

interface SlotAreaProps {
  targetTokens: ChunkToken[];
  slotTokens: ChunkToken[];
  typedInput: string;
  isShaking: boolean;
  isFinished: boolean;
  onReturnToken: (token: ChunkToken) => void;
}

export const SlotArea: React.FC<SlotAreaProps> = ({
  targetTokens,
  slotTokens,
  typedInput,
  isShaking,
  isFinished,
  onReturnToken
}) => {
  const currentIndex = slotTokens.length;

  return (
    <div
      className={`w-full max-w-3xl min-h-[100px] sm:min-h-[120px] p-4 sm:p-6 rounded-3xl bg-white border-2 transition-all flex flex-wrap items-center justify-center gap-2 sm:gap-3 ${
        isShaking
          ? 'border-rose-400 bg-rose-50/30 animate-shake'
          : isFinished
          ? 'border-emerald-400 bg-emerald-50/20 shadow-md shadow-emerald-500/5'
          : 'border-slate-200/90 shadow-sm'
      }`}
    >
      {targetTokens.map((target, idx) => {
        const isFilled = idx < slotTokens.length;
        const isCurrentActive = idx === currentIndex && !isFinished;
        const filledToken = isFilled ? slotTokens[idx] : null;

        if (isFilled && filledToken) {
          return (
            <button
              key={`filled-${filledToken.id}-${idx}`}
              onClick={() => onReturnToken(filledToken)}
              disabled={isFinished}
              className={`group relative px-3 sm:px-4 py-2 sm:py-2.5 rounded-2xl font-bold text-sm sm:text-base border-2 transition-all transform animate-pop ${
                isFinished
                  ? 'bg-emerald-500 text-white border-emerald-600 shadow-sm'
                  : 'bg-emerald-50 text-emerald-800 border-emerald-300 hover:bg-rose-50 hover:text-rose-700 hover:border-rose-300 card-pressable cursor-pointer'
              }`}
              title={isFinished ? '' : '点击撤回此词块'}
            >
              <span>{filledToken.fullText}</span>
              {!isFinished && (
                <span className="hidden group-hover:block absolute -top-1.5 -right-1.5 bg-rose-500 text-white rounded-full w-4 h-4 text-[10px] leading-4 text-center font-bold shadow-xs">
                  ×
                </span>
              )}
            </button>
          );
        }

        if (isCurrentActive) {
          return (
            <div
              key={`active-${target.id}`}
              className="relative px-3 sm:px-4 py-2 sm:py-2.5 rounded-2xl border-2 border-dashed border-brand-500 bg-brand-50/50 min-w-[70px] sm:min-w-[90px] flex items-center justify-center transition-all animate-pulse shadow-xs"
            >
              {typedInput ? (
                <span className="font-bold text-sm sm:text-base text-brand-700 font-mono tracking-wide">
                  {typedInput}
                  <span className="inline-block w-1.5 h-4 ml-0.5 bg-brand-600 animate-bounce align-middle" />
                </span>
              ) : (
                <div className="flex items-center gap-1 text-xs text-brand-500 font-semibold">
                  <span className="w-1.5 h-1.5 rounded-full bg-brand-500 animate-ping" />
                  <span>待输入</span>
                </div>
              )}
            </div>
          );
        }

        // 未填写的空槽位（预留轮廓）
        return (
          <div
            key={`empty-${target.id}-${idx}`}
            className="px-3 sm:px-4 py-2 sm:py-2.5 rounded-2xl border-2 border-dashed border-slate-200/80 bg-slate-50/60 min-w-[60px] sm:min-w-[75px] h-10 sm:h-11 flex items-center justify-center opacity-70"
          >
            <span className="text-[10px] font-bold text-slate-300 select-none">
              {idx + 1}
            </span>
          </div>
        );
      })}
    </div>
  );
};
