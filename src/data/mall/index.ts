import type { CoursePackage, CourseCategory, DifficultyLevel, Chapter } from '../../types';
import { CATEGORIES } from './categories';
import { TEXTBOOK_COURSES } from './textbook';
import { EXAM_COURSES } from './exam';
import { SCENES_COURSES } from './scenes';
import { MOVIES_COURSES } from './movies';
import { BASIC_COURSES } from './basic';
import { READING_COURSES } from './reading';
import { MUSIC_COURSES } from './music';
import { KIDS_COURSES } from './kids';
import { RECOMMENDED_COURSES } from './recommended';

export { CATEGORIES };
export const COURSE_CATEGORIES = CATEGORIES;

// 汇聚 9 大分类所有 72+ 个精品课程包
export const ALL_COURSES: CoursePackage[] = [
  ...RECOMMENDED_COURSES,
  ...TEXTBOOK_COURSES,
  ...EXAM_COURSES,
  ...BASIC_COURSES,
  ...SCENES_COURSES,
  ...MOVIES_COURSES,
  ...READING_COURSES,
  ...MUSIC_COURSES,
  ...KIDS_COURSES
];

/**
 * 根据分类筛选课程
 */
export function getCoursesByCategory(category: CourseCategory): CoursePackage[] {
  return ALL_COURSES.filter(c => c.category === category);
}

/**
 * 根据 ID 获取特定课程包
 */
export function getCourseById(courseId: string): CoursePackage | undefined {
  return ALL_COURSES.find(c => c.id === courseId);
}

/**
 * 根据课程 ID 和 章节 ID 获取具体章节
 */
export function getChapter(courseId: string, chapterId: string): Chapter | undefined {
  const course = getCourseById(courseId);
  if (!course) return undefined;
  return course.chapters.find(ch => ch.id === chapterId);
}

/**
 * 多条件搜索与筛选课程包
 */
export function searchCourses(query: string, category?: CourseCategory, difficulty?: DifficultyLevel): CoursePackage[] {
  let list = ALL_COURSES;

  if (category) {
    list = list.filter(c => c.category === category);
  }

  if (difficulty) {
    list = list.filter(c => c.difficulty === difficulty);
  }

  if (query.trim()) {
    const q = query.trim().toLowerCase();
    list = list.filter(c => 
      c.title.toLowerCase().includes(q) ||
      c.description.toLowerCase().includes(q) ||
      c.tags.some(t => t.toLowerCase().includes(q))
    );
  }

  return list;
}
