import type { CoursePackage, Chapter } from '../../src/types/index';

// 全局正规化去重 Set
export const globalSeen = new Set<string>();

export interface RawSentence {
  en: string;
  cn: string;
  ph?: string;
  note?: string;
}

export interface RawChapter {
  title: string;
  description?: string;
  sentences: RawSentence[];
}

export interface RawCourse {
  id: string;
  title: string;
  category: CoursePackage['category'];
  categoryName: string;
  coverGradient: string;
  icon: string;
  description: string;
  difficulty: CoursePackage['difficulty'];
  tags: string[];
  chapters: RawChapter[];
}

/**
 * 校验句子全局唯一性，规范化后去除标点与空格
 */
export function registerSentence(en: string, courseTitle: string, chapterTitle: string): void {
  const norm = en.toLowerCase().replace(/[^a-z0-9]/g, '');
  if (norm.length > 5) {
    if (globalSeen.has(norm)) {
      throw new Error(`[查重阻断] 句子重复出现！\n重复文本: "${en}"\n所在位置: 《${courseTitle}》- ${chapterTitle}`);
    }
    globalSeen.add(norm);
  }
}

/**
 * 将 RawCourse 转换为符合 CoursePackage 结构的真实对象，并为每一句分配唯一 ID
 */
export function buildCourse(raw: RawCourse): CoursePackage {
  const chapters: Chapter[] = raw.chapters.map((ch, chIdx) => {
    const chapterId = `${raw.id}-ch${chIdx + 1}`;
    ch.sentences.forEach(s => registerSentence(s.en, raw.title, ch.title));

    return {
      id: chapterId,
      title: ch.title,
      description: ch.description,
      sentences: ch.sentences.map((s, sIdx) => ({
        id: `${chapterId}-s${sIdx + 1}`,
        english: s.en.trim(),
        chinese: s.cn.trim(),
        phonetic: s.ph?.trim(),
        note: s.note?.trim()
      }))
    };
  });

  return {
    id: raw.id,
    title: raw.title,
    category: raw.category,
    categoryName: raw.categoryName,
    coverGradient: raw.coverGradient,
    icon: raw.icon,
    description: raw.description,
    difficulty: raw.difficulty,
    tags: raw.tags,
    chapters: chapters
  };
}

/**
 * 将 CoursePackage 数组序列化为美观规范的 TypeScript 代码
 */
export function serializeCoursesToTs(exportVarName: string, courses: CoursePackage[]): string {
  return `import type { CoursePackage } from '../../types';

export const ${exportVarName}: CoursePackage[] = ${JSON.stringify(courses, null, 2)};
`;
}
