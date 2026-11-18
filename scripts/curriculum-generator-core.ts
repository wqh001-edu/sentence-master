import * as fs from 'fs';
import * as path from 'path';

console.log('🚀 开始全量重构「句乐通 · 课程与语料商城」高品质切题语料库...\n');

// 全局正规化去重 Set
const globalSeenSentences = new Set<string>();

export interface SentenceMeta {
  en: string;
  cn: string;
  ph?: string;
  note?: string;
}

export interface ChapterMeta {
  title: string;
  description?: string;
  sentences: SentenceMeta[];
}

export interface CourseMeta {
  id: string;
  title: string;
  category: string;
  categoryName: string;
  coverGradient: string;
  icon: string;
  description: string;
  difficulty: string;
  tags: string[];
  chapters: ChapterMeta[];
}

/**
 * 校验并确保句子全局唯一
 */
export function checkUnique(en: string, loc: string): void {
  const norm = en.toLowerCase().replace(/[^a-z0-9]/g, '');
  if (norm.length > 5) {
    if (globalSeenSentences.has(norm)) {
      throw new Error(`[致命冲突] 重复句子出现在 ${loc}: "${en}"`);
    }
    globalSeenSentences.add(norm);
  }
}
