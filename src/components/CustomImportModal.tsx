import React, { useState } from 'react';
import { PlusCircle, X, Check } from 'lucide-react';
import type { Lesson, SentenceItem } from '../types';

interface CustomImportModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSaveLesson: (lesson: Lesson) => void;
}

export const CustomImportModal: React.FC<CustomImportModalProps> = ({
  isOpen,
  onClose,
  onSaveLesson
}) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [rawText, setRawText] = useState('');

  if (!isOpen) return null;

  const handleParseAndSave = () => {
    if (!title.trim()) {
      alert('请输入题库或课文标题');
      return;
    }
    if (!rawText.trim()) {
      alert('请粘贴文本内容');
      return;
    }

    const sentences: SentenceItem[] = [];
    const lines = rawText.split('\n').map(l => l.trim()).filter(Boolean);

    let i = 0;
    while (i < lines.length) {
      const line = lines[i];

      if (line.includes('|') || line.includes('——') || line.includes('\t')) {
        const delimiter = line.includes('|') ? '|' : (line.includes('——') ? '——' : '\t');
        const parts = line.split(delimiter).map(p => p.trim());
        if (parts.length >= 2) {
          sentences.push({
            id: `custom-sent-${Date.now()}-${sentences.length}`,
            english: parts[0],
            chinese: parts[1]
          });
        }
        i++;
      } else {
        const nextLine = lines[i + 1];
        const isCurrentEnglish = /^[a-zA-Z0-9\s.,!?'"—–]+$/.test(line);

        if (nextLine && isCurrentEnglish) {
          sentences.push({
            id: `custom-sent-${Date.now()}-${sentences.length}`,
            english: line,
            chinese: nextLine
          });
          i += 2;
        } else {
          sentences.push({
            id: `custom-sent-${Date.now()}-${sentences.length}`,
            english: line,
            chinese: '（自定义练习句子）'
          });
          i++;
        }
      }
    }

    if (sentences.length === 0) {
      alert('未识别到有效句子，请检查格式');
      return;
    }

    const newLesson: Lesson = {
      id: `custom-lesson-${Date.now()}`,
      title: title.trim(),
      description: description.trim() || `包含 ${sentences.length} 个自建练习句子`,
      category: 'custom',
      sentences
    };

    onSaveLesson(newLesson);
    onClose();
  };

  const handleFillDemo = () => {
    setTitle('地道口语碎碎念小辑');
    setDescription('我自己整理的 3 个高频表达');
    setRawText(`It never crossed my mind.|我压根儿就没往那方面想过。
I will keep my fingers crossed for you.|我会为你祈祷好运的！
Practice makes perfect.|熟能生巧。`);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-xs animate-fade-in">
      <div className="bg-white rounded-3xl w-full max-w-xl max-h-[90vh] flex flex-col shadow-2xl border border-slate-100 overflow-hidden animate-slide-up">
        {/* 头部 */}
        <div className="px-6 py-4 border-b border-slate-100 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <PlusCircle className="w-5 h-5 text-brand-600" />
            <h3 className="text-lg font-bold text-slate-800">导入自定义题库</h3>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-xl text-slate-400 hover:text-slate-600 hover:bg-slate-100 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* 表单主体 */}
        <div className="p-6 overflow-y-auto space-y-4">
          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5">
              题库/教材标题
            </label>
            <input
              type="text"
              placeholder="例如：老友记第一季经典对白"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full px-4 py-2.5 rounded-xl border border-slate-200 text-sm focus:outline-hidden focus:border-brand-500 focus:ring-2 focus:ring-brand-100 transition-all"
            />
          </div>

          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5">
              简介描述 (可选)
            </label>
            <input
              type="text"
              placeholder="例如：生词和日常常用搭配集"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="w-full px-4 py-2.5 rounded-xl border border-slate-200 text-sm focus:outline-hidden focus:border-brand-500 focus:ring-2 focus:ring-brand-100 transition-all"
            />
          </div>

          <div>
            <div className="flex items-center justify-between mb-1.5">
              <label className="block text-xs font-bold text-slate-700">
                粘贴句子文本内容
              </label>
              <button
                type="button"
                onClick={handleFillDemo}
                className="text-xs text-brand-600 hover:text-brand-800 font-semibold"
              >
                填入示例
              </button>
            </div>
            <textarea
              rows={8}
              placeholder={`支持格式（每行一条，用 | 隔开中英文）：\nNever give up, never surrender.|绝不轻言放弃，绝不屈服。\n\n或两两成对：\n第一行英文\n第二行中文翻译`}
              value={rawText}
              onChange={(e) => setRawText(e.target.value)}
              className="w-full px-4 py-3 rounded-2xl border border-slate-200 text-sm font-mono focus:outline-hidden focus:border-brand-500 focus:ring-2 focus:ring-brand-100 transition-all leading-relaxed"
            />
          </div>
        </div>

        {/* 底部按钮 */}
        <div className="px-6 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-end gap-3">
          <button
            onClick={onClose}
            className="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-200 text-sm font-semibold transition-colors"
          >
            取消
          </button>
          <button
            onClick={handleParseAndSave}
            className="flex items-center gap-1.5 px-5 py-2.5 rounded-xl bg-brand-600 hover:bg-brand-700 text-white text-sm font-bold shadow-md shadow-brand-500/20 transition-all card-pressable"
          >
            <Check className="w-4 h-4" />
            <span>生成并开始练习</span>
          </button>
        </div>
      </div>
    </div>
  );
};
