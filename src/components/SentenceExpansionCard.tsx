import React, { useState } from 'react';
import { Sparkles, Volume2, Link2, Compass, ChevronDown, ChevronUp, ArrowRight } from 'lucide-react';
import type { SentenceItem } from '../types';
import { generateDynamicExpansion } from '../utils/dynamicExpansion';
import { speakText } from '../utils/tts';

interface SentenceExpansionCardProps {
  sentence: SentenceItem;
  isFinished: boolean;
  onNextSentence: () => void;
}

export const SentenceExpansionCard: React.FC<SentenceExpansionCardProps> = ({
  sentence,
  isFinished,
  onNextSentence
}) => {
  const [isCollapsed, setIsCollapsed] = useState(false);

  if (!isFinished) return null;

  const expansion = generateDynamicExpansion(sentence.english, sentence.expansion ?? undefined);

  return (
    <div className="w-full max-w-3xl mx-auto my-5 px-3 animate-slide-up">
      <div className="bg-gradient-to-br from-indigo-50/90 via-white to-purple-50/80 rounded-3xl border-2 border-indigo-200/80 shadow-xl overflow-hidden transition-all">
        {/* 卡片头部 */}
        <div
          onClick={() => setIsCollapsed(prev => !prev)}
          className="px-6 py-4 flex items-center justify-between cursor-pointer select-none bg-white/70 border-b border-indigo-100"
        >
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-2xl bg-gradient-to-tr from-brand-600 to-purple-600 text-white shadow-sm">
              <Sparkles className="w-4 h-4" />
            </div>
            <div>
              <h3 className="font-extrabold text-slate-800 text-base sm:text-lg flex items-center gap-2">
                <span>串记 · 联想 · 扩展</span>
                <span className="text-xs px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-bold">
                  举一反三
                </span>
              </h3>
              <p className="text-xs text-slate-500 mt-0.5">
                强化肌肉记忆，构建词汇与地道表达知识网络
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2 text-slate-400">
            <span className="text-xs font-semibold hidden sm:inline">
              {isCollapsed ? '展开' : '折叠'}
            </span>
            {isCollapsed ? <ChevronDown className="w-5 h-5" /> : <ChevronUp className="w-5 h-5" />}
          </div>
        </div>

        {/* 展开内容主体 */}
        {!isCollapsed && (
          <div className="p-5 sm:p-6 space-y-6">
            {/* 1. 串记：核心词族派生链 */}
            {expansion.wordFamily && (
              <div className="rounded-2xl bg-white/90 p-4 border border-slate-200/70 shadow-xs">
                <div className="flex items-center gap-2 mb-2.5 text-xs font-bold text-indigo-700">
                  <Link2 className="w-4 h-4" />
                  <span>【串记 · 词族派生链】 核心词根：{expansion.wordFamily.root}</span>
                </div>
                <div className="flex flex-wrap items-center gap-2">
                  {expansion.wordFamily.chain.map((item, idx) => (
                    <div
                      key={idx}
                      className="group flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-50 hover:bg-indigo-50 border border-slate-200 hover:border-indigo-300 transition-colors"
                    >
                      <span className="text-xs sm:text-sm font-bold text-slate-800">{item}</span>
                      <button
                        onClick={() => speakText(item.split(' ')[0])}
                        className="text-slate-400 group-hover:text-indigo-600 transition-colors"
                        title="朗读该词"
                      >
                        <Volume2 className="w-3.5 h-3.5" />
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* 2. 联想：语境同主题词群 */}
            {expansion.associations && expansion.associations.length > 0 && (
              <div className="rounded-2xl bg-white/90 p-4 border border-slate-200/70 shadow-xs">
                <div className="flex items-center gap-2 mb-2.5 text-xs font-bold text-purple-700">
                  <Compass className="w-4 h-4" />
                  <span>【联想 · 主题高频词群】 拓展词汇储备</span>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                  {expansion.associations.map((assoc, idx) => (
                    <div
                      key={idx}
                      className="flex items-center justify-between p-2.5 rounded-xl bg-slate-50 border border-slate-200/70"
                    >
                      <div>
                        <div className="flex items-center gap-2">
                          <span className="text-xs sm:text-sm font-bold text-slate-800">{assoc.word}</span>
                          {assoc.phonetic && (
                            <span className="text-[11px] text-slate-400 font-mono">{assoc.phonetic}</span>
                          )}
                        </div>
                        <p className="text-xs text-slate-500 mt-0.5">{assoc.meaning}</p>
                      </div>
                      <button
                        onClick={() => speakText(assoc.word)}
                        className="p-1.5 rounded-lg text-slate-400 hover:text-purple-600 hover:bg-purple-50 transition-colors"
                        title="朗读"
                      >
                        <Volume2 className="w-3.5 h-3.5" />
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* 3. 扩展：地道搭配短语与例句 */}
            {expansion.extensions && expansion.extensions.length > 0 && (
              <div className="rounded-2xl bg-white/90 p-4 border border-slate-200/70 shadow-xs">
                <div className="flex items-center gap-2 mb-2.5 text-xs font-bold text-emerald-700">
                  <Sparkles className="w-4 h-4" />
                  <span>【扩展 · 固定搭配与实用例句】 地道母语级应用</span>
                </div>
                <div className="space-y-3">
                  {expansion.extensions.map((ext, idx) => (
                    <div
                      key={idx}
                      className="p-3 rounded-xl bg-slate-50 border border-slate-200/80 hover:border-emerald-300 transition-colors"
                    >
                      <div className="flex items-center justify-between">
                        <span className="text-xs sm:text-sm font-bold text-slate-800">
                          {ext.phrase} · <span className="text-xs text-slate-500 font-normal">{ext.meaning}</span>
                        </span>
                        <button
                          onClick={() => speakText(ext.example)}
                          className="p-1 text-slate-400 hover:text-emerald-600 transition-colors"
                          title="朗读例句"
                        >
                          <Volume2 className="w-3.5 h-3.5" />
                        </button>
                      </div>
                      <p className="text-xs sm:text-sm text-slate-700 font-medium mt-1">
                        {ext.example}
                      </p>
                      <p className="text-xs text-slate-400 mt-0.5">
                        {ext.exampleCn}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* 底部进入下一句快捷指引 */}
            <div className="pt-2 flex items-center justify-end">
              <button
                onClick={onNextSentence}
                className="flex items-center gap-1.5 px-6 py-2.5 rounded-2xl bg-brand-600 hover:bg-brand-700 text-white font-bold text-xs sm:text-sm shadow-md shadow-brand-500/20 card-pressable"
              >
                <span>下一句练习 (Enter)</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
