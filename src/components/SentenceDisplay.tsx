import React, { useState } from 'react';
import { Volume2, Eye, EyeOff, Info, HelpCircle } from 'lucide-react';
import type { SentenceItem, PracticeMode } from '../types';

interface SentenceDisplayProps {
  sentence: SentenceItem;
  practiceMode: PracticeMode;
  showHint: boolean;
  onReplayAudio: () => void;
  onToggleHint: () => void;
}

export const SentenceDisplay: React.FC<SentenceDisplayProps> = ({
  sentence,
  practiceMode,
  showHint,
  onReplayAudio,
  onToggleHint
}) => {
  const [revealChineseInDictation, setRevealChineseInDictation] = useState(false);
  const [showGrammarNote, setShowGrammarNote] = useState(false);

  const isDictation = practiceMode === 'dictation';

  return (
    <div className="w-full flex flex-col items-center text-center my-4 sm:my-6 transition-all">
      {/* 听写模式下的听音指示器 */}
      {isDictation && (
        <div className="mb-2 flex items-center gap-2 px-3 py-1 bg-indigo-50 text-indigo-700 text-xs font-semibold rounded-full border border-indigo-100 animate-pulse">
          <Volume2 className="w-3.5 h-3.5" />
          <span>正在盲听模式：请仔细辨音拼出整句</span>
        </div>
      )}

      {/* 主中文句子卡片 */}
      <div className="relative group max-w-2xl px-4 py-2">
        <h2 className={`text-xl sm:text-2xl md:text-3xl font-bold text-slate-800 leading-snug tracking-tight transition-all ${
          isDictation && !revealChineseInDictation && !showHint
            ? 'blur-sm select-none hover:blur-none cursor-pointer'
            : ''
        }`}
        onClick={() => isDictation && setRevealChineseInDictation(true)}
        title={isDictation ? '点击揭晓中文提示' : ''}
        >
          {sentence.chinese}
        </h2>

        {/* 快捷朗读与提示按钮组 */}
        <div className="flex items-center justify-center gap-3 mt-2">
          <button
            onClick={onReplayAudio}
            className="p-1.5 rounded-lg text-slate-400 hover:text-brand-600 hover:bg-slate-100 transition-colors"
            title="播放/重播英文发音"
          >
            <Volume2 className="w-4 h-4" />
          </button>
          
          <button
            onClick={onToggleHint}
            className={`p-1.5 rounded-lg transition-colors ${
              showHint ? 'text-amber-600 bg-amber-50' : 'text-slate-400 hover:text-amber-600 hover:bg-slate-100'
            }`}
            title="查看参考答案"
          >
            <HelpCircle className="w-4 h-4" />
          </button>

          {isDictation && !showHint && (
            <button
              onClick={() => setRevealChineseInDictation(prev => !prev)}
              className="text-xs text-slate-400 hover:text-slate-600 flex items-center gap-1 transition-colors"
            >
              {revealChineseInDictation ? (
                <>
                  <EyeOff className="w-3.5 h-3.5" /> 隐藏中文
                </>
              ) : (
                <>
                  <Eye className="w-3.5 h-3.5" /> 偷看中文
                </>
              )}
            </button>
          )}
        </div>
      </div>

      {/* 音标或完整答案揭晓区 */}
      {showHint && (
        <div className="mt-3 px-4 py-2.5 rounded-2xl bg-amber-50/90 border border-amber-200/80 max-w-xl animate-slide-up shadow-xs">
          <div className="text-xs font-semibold text-amber-800 mb-1 flex items-center justify-center gap-1">
            <HelpCircle className="w-3.5 h-3.5" />
            <span>参考答案</span>
          </div>
          <p className="text-base sm:text-lg font-bold text-amber-950 font-mono tracking-wide">
            {sentence.english}
          </p>
          {sentence.phonetic && (
            <p className="text-xs text-amber-700 mt-1 font-mono">{sentence.phonetic}</p>
          )}
        </div>
      )}

      {/* 语法点 / 课外拓展小贴士 */}
      {sentence.note && (
        <div className="mt-2">
          {showGrammarNote ? (
            <div className="px-3 py-1.5 rounded-xl bg-slate-100 text-slate-600 text-xs max-w-md mx-auto flex items-center justify-between gap-2 border border-slate-200 animate-slide-up">
              <span className="text-left">{sentence.note}</span>
              <button 
                onClick={() => setShowGrammarNote(false)}
                className="text-slate-400 hover:text-slate-600 font-bold ml-1 text-sm"
              >
                ×
              </button>
            </div>
          ) : (
            <button
              onClick={() => setShowGrammarNote(true)}
              className="text-[11px] text-slate-400 hover:text-brand-600 flex items-center gap-1 mx-auto transition-colors"
            >
              <Info className="w-3 h-3" />
              <span>查看语法搭配要点</span>
            </button>
          )}
        </div>
      )}
    </div>
  );
};
