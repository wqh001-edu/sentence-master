import type { Lesson } from '../types';
import { newConcept1Sentences } from './newConcept1';
import { newConcept2Sentences } from './newConcept2';
import { newConcept3Sentences } from './newConcept3';
import { dailySpokenSentences } from './dailySpoken';
import { movieQuotesSentences } from './movieQuotes';

export const PRESET_LESSONS: Lesson[] = [
  {
    id: 'lesson-nc1',
    title: '《新概念英语》第一册 · 基础句型',
    description: '涵盖日常衣食住行问候、物主代词、简单时态等 12 句核心精选，打牢语感根基。',
    category: 'new_concept',
    sentences: newConcept1Sentences
  },
  {
    id: 'lesson-nc2',
    title: '《新概念英语》第二册 · 经典核心篇',
    description: '涵盖情态动词、完成时、倒装句、宾语从句等进阶结构，突破连词成句思维瓶颈。',
    category: 'new_concept',
    sentences: newConcept2Sentences
  },
  {
    id: 'lesson-nc3',
    title: '《新概念英语》第三册 · 高阶表达篇',
    description: '精选长难句、优美定语从句与同位语从句，锤炼原汁原味的母语级流利表达。',
    category: 'new_concept',
    sentences: newConcept3Sentences
  },
  {
    id: 'lesson-spoken',
    title: '实用日常与地道口语 300 句精选',
    description: '地道习语、沟通救急、职场与生活高频表达，告别中式硬翻。',
    category: 'daily_spoken',
    sentences: dailySpokenSentences
  },
  {
    id: 'lesson-movie',
    title: '经典影视原声与人生金句',
    description: '《阿甘正传》《肖申克的救赎》《星际穿越》等传世台词，情境感染力强。',
    category: 'movie_quotes',
    sentences: movieQuotesSentences
  }
];

export const STORAGE_CUSTOM_LESSONS_KEY = 'jlt_custom_lessons';

export function loadAllLessons(): Lesson[] {
  if (typeof window === 'undefined') return PRESET_LESSONS;
  try {
    const raw = localStorage.getItem(STORAGE_CUSTOM_LESSONS_KEY);
    if (!raw) return PRESET_LESSONS;
    const customList: Lesson[] = JSON.parse(raw);
    return [...PRESET_LESSONS, ...customList];
  } catch (e) {
    console.error('Failed to load custom lessons:', e);
    return PRESET_LESSONS;
  }
}

export function saveCustomLesson(lesson: Lesson) {
  try {
    const raw = localStorage.getItem(STORAGE_CUSTOM_LESSONS_KEY);
    const customList: Lesson[] = raw ? JSON.parse(raw) : [];
    const existingIdx = customList.findIndex(l => l.id === lesson.id);
    if (existingIdx >= 0) {
      customList[existingIdx] = lesson;
    } else {
      customList.push(lesson);
    }
    localStorage.setItem(STORAGE_CUSTOM_LESSONS_KEY, JSON.stringify(customList));
  } catch (e) {
    console.error('Failed to save custom lesson:', e);
  }
}
