import React, { useEffect, useRef } from 'react';
import { Keyboard } from 'lucide-react';
import type { ChunkToken } from '../types';

interface TypingInputProps {
  typedInput: string;
  isFinished: boolean;
  onKeyTyping: (input: string) => void;
  onReturnLastToken: () => void;
  onNextSentence: () => void;
  onReplayAudio: () => void;
  onToggleHint: () => void;
  slotTokens: ChunkToken[];
}

export const TypingInput: React.FC<TypingInputProps> = ({
  typedInput,
  isFinished,
  onKeyTyping,
  onReturnLastToken,
  onNextSentence,
  onReplayAudio,
  onToggleHint,
  slotTokens
}) => {
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      const activeEl = document.activeElement;
      if (activeEl && (activeEl.tagName === 'INPUT' || activeEl.tagName === 'TEXTAREA') && activeEl !== inputRef.current) {
        return;
      }

      if (isFinished && e.key === 'Enter') {
        e.preventDefault();
        onNextSentence();
        return;
      }

      if (e.key === ' ' && e.ctrlKey) {
        e.preventDefault();
        onReplayAudio();
        return;
      }

      if (e.key === 'Tab') {
        e.preventDefault();
        onToggleHint();
        return;
      }

      if (e.key === 'Backspace') {
        if (typedInput.length > 0) {
          onKeyTyping(typedInput.slice(0, -1));
        } else if (slotTokens.length > 0) {
          onReturnLastToken();
        }
        return;
      }

      if (e.key === ' ') {
        e.preventDefault();
        if (typedInput.trim().length > 0) {
          onKeyTyping(typedInput.trim());
        }
        return;
      }

      if (e.key.length === 1 && !e.ctrlKey && !e.altKey && !e.metaKey) {
        if (/[a-zA-Z0-9'\-]/.test(e.key)) {
          onKeyTyping(typedInput + e.key);
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [typedInput, isFinished, onKeyTyping, onReturnLastToken, onNextSentence, onReplayAudio, onToggleHint, slotTokens]);

  return (
    <div className="w-full max-w-md flex flex-col items-center justify-center my-2">
      <div className="flex items-center gap-2">
        <button
          onClick={() => inputRef.current?.focus()}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-500 hover:text-slate-700 text-xs transition-colors"
          title="点击呼出手机键盘或聚焦打字"
        >
          <Keyboard className="w-3.5 h-3.5" />
          <span>支持键盘盲打 (按空格切换，Tab看提示)</span>
        </button>
        <input
          ref={inputRef}
          type="text"
          value={typedInput}
          onChange={(e) => onKeyTyping(e.target.value)}
          className="opacity-0 w-1 h-1 pointer-events-none absolute"
          autoCapitalize="off"
          autoCorrect="off"
          autoComplete="off"
          spellCheck="false"
        />
      </div>
    </div>
  );
};
