import React, { useState, useRef, useEffect } from 'react';
import { Volume2, ChevronDown, ChevronUp, Layers, BookOpen, GitFork, Link as LinkIcon, Sparkles } from 'lucide-react';
import type { WordGrammar, SentenceItem } from '../types';
import { parseSentenceGrammar, getRoleTheme } from '../utils/grammarParser';
import { speakText } from '../utils/tts';

interface GrammarAnalysisCardProps {
  sentence: SentenceItem;
  showGrammar: boolean;
  onToggleShowGrammar: () => void;
}

export const GrammarAnalysisCard: React.FC<GrammarAnalysisCardProps> = ({
  sentence,
  showGrammar,
  onToggleShowGrammar
}) => {
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null);
  const [arrowLeftPercent, setArrowLeftPercent] = useState<number>(50);

  const scrollContainerRef = useRef<HTMLDivElement>(null);
  const wordCardRefs = useRef<(HTMLDivElement | null)[]>([]);

  const wordGrammarList = parseSentenceGrammar(sentence.english, sentence.wordsGrammar ?? undefined, sentence.chinese);

  // 当选中的单词改变时，自动将选中的单词平滑居中，并计算指示箭头位置
  useEffect(() => {
    if (selectedIndex === null || !wordCardRefs.current[selectedIndex] || !scrollContainerRef.current) {
      return;
    }

    const cardEl = wordCardRefs.current[selectedIndex];
    const containerEl = scrollContainerRef.current;

    if (cardEl && containerEl) {
      // 1. 平滑将卡片滚动至水平视口中心
      cardEl.scrollIntoView({
        behavior: 'smooth',
        inline: 'center',
        block: 'nearest'
      });

      // 2. 计算卡片在容器可视窗口内的相对水平百分比（用于箭头定位）
      const updateArrow = () => {
        const cardRect = cardEl.getBoundingClientRect();
        const containerRect = containerEl.getBoundingClientRect();
        const relativeX = (cardRect.left + cardRect.width / 2) - containerRect.left;
        const clampedPercent = Math.max(8, Math.min(92, (relativeX / containerRect.width) * 100));
        setArrowLeftPercent(clampedPercent);
      };

      // 稍微延时等待 scrollIntoView 平滑执行
      const timer = setTimeout(updateArrow, 150);
      return () => clearTimeout(timer);
    }
  }, [selectedIndex]);

  // 重置选中状态
  useEffect(() => {
    setSelectedIndex(null);
  }, [sentence.id]);

  const selectedWord: WordGrammar | null = selectedIndex !== null ? wordGrammarList[selectedIndex] : null;

  return (
    <div className="w-full max-w-4xl mx-auto my-3 px-2 sm:px-4">
      {/* 语法解析卡片开关工具栏 */}
      <div className="flex items-center justify-between px-2 mb-2">
        <button
          onClick={onToggleShowGrammar}
          className="flex items-center gap-1.5 text-xs font-bold text-slate-400 hover:text-brand-400 transition-colors"
        >
          <Layers className="w-3.5 h-3.5 text-brand-500" />
          <span>句法成分分析 {showGrammar ? '(已开启)' : '(已收起)'}</span>
          {showGrammar ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
        </button>

        {showGrammar && (
          <span className="text-[11px] text-slate-400">
            点击单词查看全中文详析、例句与词汇扩展
          </span>
        )}
      </div>

      {/* 核心卡片容器：深度对标句乐部截图设计 */}
      {showGrammar && (
        <div className="relative p-4 sm:p-6 rounded-3xl bg-[#111317] border border-slate-800 shadow-2xl animate-slide-up">
          {/* 横向滚动词卡区 */}
          <div
            ref={scrollContainerRef}
            className="overflow-x-auto no-scrollbar scroll-smooth py-2"
          >
            <div className="flex items-end justify-center gap-2.5 sm:gap-3.5 min-w-max mx-auto px-4">
              {wordGrammarList.map((item, idx) => {
                const theme = getRoleTheme(item.role);
                const isSelected = selectedIndex === idx;

                return (
                  <div
                    key={`gram-${idx}-${item.word}`}
                    ref={(el) => {
                      wordCardRefs.current[idx] = el;
                    }}
                    onClick={() => {
                      if (selectedIndex === idx) {
                        // 再次点击同一单词朗读
                        speakText(item.word);
                      } else {
                        setSelectedIndex(idx);
                        speakText(item.word);
                      }
                    }}
                    className={`group relative flex flex-col items-center p-2.5 sm:p-3 rounded-2xl transition-all cursor-pointer select-none min-w-[76px] sm:min-w-[90px] ${
                      isSelected
                        ? 'bg-[#222733] border-brand-500 shadow-lg shadow-brand-500/10 scale-105 ring-2 ring-brand-500/50'
                        : 'bg-[#181b20] hover:bg-[#20242b] border border-slate-800/80 hover:border-slate-700'
                    }`}
                  >
                    {/* 1. 顶部成分胶囊药丸 (状语 / 谓语 / 主语 / 宾语等) */}
                    {item.role && (
                      <span
                        className={`px-2 py-0.5 rounded-full text-[10px] font-bold border ${theme.badgeBg} ${theme.badgeText} ${theme.badgeBorder} mb-2 tracking-wide`}
                      >
                        {item.role}
                      </span>
                    )}

                    {/* 2. 国际音标 */}
                    <span className="text-[11px] text-slate-400 font-mono tracking-tight mb-0.5">
                      {item.phonetic || ''}
                    </span>

                    {/* 3. 单词文本与彩色粗下划线 */}
                    <div className="flex flex-col items-center">
                      <span className="text-base sm:text-lg font-bold text-white tracking-wide font-sans">
                        {item.word}
                      </span>
                      {/* 彩色下划线 */}
                      <div className={`w-full mt-1.5 border-b-2 sm:border-b-[2.5px] ${theme.underlineColor}`} />
                    </div>

                    {/* 4. 释义与词性标签（保证 100% 中文） */}
                    <div className="mt-2 flex flex-col items-center text-center max-w-[85px]">
                      <span className="text-xs text-slate-200 font-medium truncate w-full" title={item.meaning}>
                        {item.meaning || '核心词'}
                      </span>
                      <span className="text-[10px] text-slate-400 mt-0.5 font-normal truncate w-full">
                        {item.pos || '实词'}
                      </span>
                    </div>

                    {/* 特殊语法注解提示角标 */}
                    {item.note && (
                      <div className="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse shadow" />
                    )}
                  </div>
                );
              })}
            </div>
          </div>

          {/* 选中的单词：全中文「单词详解」面板（置于滚动容器外部，始终居中显示在可视区域内，带指示小三角） */}
          {selectedWord && (
            <div className="relative mt-4 animate-fade-in">
              {/* 指向当前选中单词的小三角形指示标 */}
              <div
                className="absolute -top-2 w-0 h-0 border-x-8 border-x-transparent border-b-8 border-b-[#1a1f29] transition-all duration-300"
                style={{ left: `calc(${arrowLeftPercent}% - 8px)` }}
              />

              <div className="p-4 sm:p-5 rounded-2xl bg-[#171b22] border border-slate-700/80 text-left shadow-2xl">
                {/* 顶部标题行 */}
                <div className="flex items-start justify-between gap-3 pb-3 border-b border-slate-800">
                  <div className="flex flex-wrap items-center gap-2">
                    <span className="text-xl font-bold text-white tracking-wide">{selectedWord.word}</span>
                    {selectedWord.phonetic && (
                      <span className="text-xs text-brand-400 font-mono px-2 py-0.5 rounded-md bg-brand-950/40 border border-brand-800/40">
                        {selectedWord.phonetic}
                      </span>
                    )}
                    <span className="px-2 py-0.5 rounded-md text-xs font-medium bg-slate-800 text-slate-200">
                      {selectedWord.pos}
                    </span>
                    <span className="px-2 py-0.5 rounded-md text-xs font-semibold bg-brand-950/80 text-brand-300 border border-brand-700/50">
                      句中充当：{selectedWord.role}
                    </span>
                  </div>

                  <div className="flex items-center gap-2 shrink-0">
                    <button
                      onClick={() => speakText(selectedWord.word)}
                      className="p-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 transition-colors flex items-center gap-1 text-xs"
                      title="朗读该单词"
                    >
                      <Volume2 className="w-4 h-4 text-brand-400" />
                      <span className="hidden sm:inline">发音</span>
                    </button>
                    <button
                      onClick={() => setSelectedIndex(null)}
                      className="p-1 text-slate-500 hover:text-slate-300 text-sm font-bold ml-1"
                      title="关闭详解"
                    >
                      ✕
                    </button>
                  </div>
                </div>

                {/* 中文释义与语法作用 */}
                <div className="mt-3 space-y-2.5">
                  <div className="flex items-start gap-2">
                    <span className="text-xs font-bold text-slate-400 shrink-0 mt-0.5">中文释义：</span>
                    <span className="text-sm font-semibold text-amber-300">{selectedWord.meaning}</span>
                  </div>

                  {selectedWord.explanation && (
                    <div className="flex items-start gap-2">
                      <span className="text-xs font-bold text-slate-400 shrink-0 mt-0.5">语法剖析：</span>
                      <p className="text-xs text-slate-300 leading-relaxed">{selectedWord.explanation}</p>
                    </div>
                  )}

                  {selectedWord.note && (
                    <div className="p-2.5 rounded-xl bg-amber-950/30 border border-amber-800/40 text-amber-200 text-xs flex items-center gap-2">
                      <Sparkles className="w-4 h-4 text-amber-400 shrink-0" />
                      <span>{selectedWord.note}</span>
                    </div>
                  )}

                  {/* 双语地道例句 */}
                  {selectedWord.example && (
                    <div className="mt-3 pt-3 border-t border-slate-800/80">
                      <div className="flex items-center justify-between mb-1">
                        <span className="text-xs font-bold text-slate-400 flex items-center gap-1">
                          <BookOpen className="w-3.5 h-3.5 text-brand-400" />
                          经典例句
                        </span>
                        <button
                          onClick={() => speakText(selectedWord.example || '')}
                          className="text-[11px] text-brand-400 hover:text-brand-300 flex items-center gap-1"
                        >
                          <Volume2 className="w-3 h-3" /> 听例句
                        </button>
                      </div>
                      <p className="text-xs text-white font-medium">{selectedWord.example}</p>
                      {selectedWord.exampleCn && (
                        <p className="text-xs text-slate-400 mt-0.5">{selectedWord.exampleCn}</p>
                      )}
                    </div>
                  )}

                  {/* 扩展模块：词族派生、同/反义词、高频短语 */}
                  <div className="mt-3 pt-3 border-t border-slate-800/80 grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                    {/* 词族派生 */}
                    {selectedWord.family && selectedWord.family.length > 0 && (
                      <div className="bg-[#12151b] p-2.5 rounded-xl border border-slate-800">
                        <span className="font-bold text-slate-400 flex items-center gap-1 mb-1.5">
                          <GitFork className="w-3.5 h-3.5 text-cyan-400" /> 词族派生链
                        </span>
                        <div className="flex flex-wrap gap-1.5">
                          {selectedWord.family.map((f, i) => (
                            <span
                              key={i}
                              onClick={() => speakText(f)}
                              className="px-2 py-0.5 rounded-md bg-slate-800/80 hover:bg-slate-700 text-cyan-300 cursor-pointer transition-colors"
                            >
                              {f}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}

                    {/* 近义词 / 反义词 */}
                    {((selectedWord.synonyms && selectedWord.synonyms.length > 0) || (selectedWord.antonyms && selectedWord.antonyms.length > 0)) && (
                      <div className="bg-[#12151b] p-2.5 rounded-xl border border-slate-800">
                        <span className="font-bold text-slate-400 mb-1.5 block">同义 / 反义扩展</span>
                        <div className="space-y-1">
                          {selectedWord.synonyms && selectedWord.synonyms.length > 0 && (
                            <div className="flex items-center gap-1.5 flex-wrap">
                              <span className="text-[10px] text-emerald-400 bg-emerald-950/60 px-1.5 py-0.5 rounded">近义</span>
                              {selectedWord.synonyms.map((s, i) => (
                                <span
                                  key={i}
                                  onClick={() => speakText(s)}
                                  className="text-slate-300 hover:text-white cursor-pointer underline decoration-dotted"
                                >
                                  {s}
                                </span>
                              ))}
                            </div>
                          )}
                          {selectedWord.antonyms && selectedWord.antonyms.length > 0 && (
                            <div className="flex items-center gap-1.5 flex-wrap">
                              <span className="text-[10px] text-rose-400 bg-rose-950/60 px-1.5 py-0.5 rounded">反义</span>
                              {selectedWord.antonyms.map((a, i) => (
                                <span
                                  key={i}
                                  onClick={() => speakText(a)}
                                  className="text-slate-300 hover:text-white cursor-pointer underline decoration-dotted"
                                >
                                  {a}
                                </span>
                              ))}
                            </div>
                          )}
                        </div>
                      </div>
                    )}

                    {/* 高频搭配 */}
                    {selectedWord.collocations && selectedWord.collocations.length > 0 && (
                      <div className="sm:col-span-2 bg-[#12151b] p-2.5 rounded-xl border border-slate-800">
                        <span className="font-bold text-slate-400 flex items-center gap-1 mb-1.5">
                          <LinkIcon className="w-3.5 h-3.5 text-amber-400" /> 常用短语搭配
                        </span>
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                          {selectedWord.collocations.map((col, i) => (
                            <div
                              key={i}
                              onClick={() => speakText(col.phrase)}
                              className="flex items-center justify-between p-1.5 rounded-lg bg-slate-800/50 hover:bg-slate-800 transition-colors cursor-pointer"
                            >
                              <span className="font-medium text-amber-300">{col.phrase}</span>
                              <span className="text-slate-400 text-[11px]">{col.meaning}</span>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};
