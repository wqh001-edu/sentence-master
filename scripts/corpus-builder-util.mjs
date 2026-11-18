import fs from 'fs';
import path from 'path';

export const globalSeen = new Set();

export function makeSentence(en, cn, ph, note) {
  const norm = en.toLowerCase().replace(/[^a-z0-9]/g, '');
  if (norm.length > 5) {
    if (globalSeen.has(norm)) {
      throw new Error(`[查重异常] 全局句子冲突！重复句子: "${en}"`);
    }
    globalSeen.add(norm);
  }
  return { en: en.trim(), cn: cn.trim(), ph: ph?.trim(), note: note?.trim() };
}

export function buildCoursePackage(meta, chapters) {
  return {
    id: meta.id,
    title: meta.title,
    category: meta.category,
    categoryName: meta.categoryName,
    coverGradient: meta.coverGradient,
    icon: meta.icon,
    description: meta.description,
    difficulty: meta.difficulty,
    tags: meta.tags,
    chapters: chapters.map((ch, chIdx) => {
      const chapterId = `${meta.id}-ch${chIdx + 1}`;
      return {
        id: chapterId,
        title: ch.title,
        description: ch.description,
        sentences: ch.sentences.map((s, sIdx) => ({
          id: `${chapterId}-s${sIdx + 1}`,
          english: s.en,
          chinese: s.cn,
          phonetic: s.ph || undefined,
          note: s.note || undefined
        }))
      };
    })
  };
}

export function saveCourseFile(categoryKey, exportVarName, courses) {
  const targetPath = path.resolve(`src/data/mall/${categoryKey}.ts`);
  const content = `import type { CoursePackage } from '../../types';

export const ${exportVarName}: CoursePackage[] = ${JSON.stringify(courses, null, 2)};
`;
  fs.writeFileSync(targetPath, content, 'utf-8');
  console.log(`✅ [写入成功] ${targetPath} (包含 ${courses.length} 门课程, ${courses.reduce((sum, c) => sum + c.chapters.length, 0)} 个章节, ${courses.reduce((sum, c) => sum + c.chapters.reduce((s2, ch) => s2 + ch.sentences.length, 0), 0)} 个句子)`);
}
