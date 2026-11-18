import type { Chapter, SentenceItem } from '../../types';

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

/**
 * 严格章节构建工具：按章节显式组织真实、切题、互不重复的句子
 */
export function buildCourseChapters(courseKey: string, chapters: RawChapter[]): Chapter[] {
  return chapters.map((ch, chIdx) => {
    const chapterId = `${courseKey}-ch${chIdx + 1}`;
    const sentenceList: SentenceItem[] = ch.sentences.map((s, sIdx) => ({
      id: `${chapterId}-s${sIdx + 1}`,
      english: s.en.trim(),
      chinese: s.cn.trim(),
      phonetic: s.ph?.trim(),
      note: s.note?.trim()
    }));

    return {
      id: chapterId,
      title: ch.title,
      description: ch.description,
      sentences: sentenceList
    };
  });
}

/**
 * 辅助工具：若传入平铺句子池，按每章固定句数依次切分，绝不跨章重复
 */
export function splitSentencesToChapters(
  courseKey: string,
  chapterTitles: { title: string; desc?: string }[],
  sentencePool: RawSentence[],
  sentencesPerChapter: number = 15
): Chapter[] {
  return chapterTitles.map((meta, chIdx) => {
    const chapterId = `${courseKey}-ch${chIdx + 1}`;
    const startIdx = chIdx * sentencesPerChapter;
    const slice = sentencePool.slice(startIdx, startIdx + sentencesPerChapter);

    const sentenceList: SentenceItem[] = slice.map((s, sIdx) => ({
      id: `${chapterId}-s${sIdx + 1}`,
      english: s.en.trim(),
      chinese: s.cn.trim(),
      phonetic: s.ph?.trim(),
      note: s.note?.trim()
    }));

    return {
      id: chapterId,
      title: meta.title,
      description: meta.desc,
      sentences: sentenceList
    };
  });
}
