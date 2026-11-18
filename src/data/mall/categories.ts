import type { CourseCategory } from '../../types';

export interface CategoryMeta {
  id: CourseCategory;
  name: string;
  icon: string;
  description: string;
  gradient: string;
}

export const CATEGORIES: CategoryMeta[] = [
  {
    id: 'recommended',
    name: '精选推荐',
    icon: '🔥',
    description: '热门排行榜 · 本周新课 · 编辑特选高分课程',
    gradient: 'from-amber-500 to-orange-600'
  },
  {
    id: 'textbook',
    name: '教材同步',
    icon: '📚',
    description: '新概念英语全套 · 人教版 · 外研版 · 牛津英语体系',
    gradient: 'from-blue-600 to-indigo-700'
  },
  {
    id: 'exam',
    name: '考试备考',
    icon: '🎯',
    description: '中考 · 高考 · 四六级 · 考研 · 雅思 · 托福高频句',
    gradient: 'from-rose-500 to-red-700'
  },
  {
    id: 'basic',
    name: '基础学习',
    icon: '🌱',
    description: '零基础音标 · 核心 1000 词造句 · 基础五大句型',
    gradient: 'from-emerald-500 to-teal-700'
  },
  {
    id: 'scenes',
    name: '场景英语',
    icon: '✈️',
    description: '机场出行 · 酒店住宿 · 西餐厅 · 涉外面试 · 看病就医',
    gradient: 'from-cyan-500 to-blue-600'
  },
  {
    id: 'movies',
    name: '影视英语',
    icon: '🎬',
    description: '老友记 · 摩登家庭 · 经典奥斯卡电影 · 动画名场面',
    gradient: 'from-purple-600 to-indigo-800'
  },
  {
    id: 'reading',
    name: '阅读听力',
    icon: '📖',
    description: '短篇原版故事 · 名人传记与演讲 · 慢速精听美文',
    gradient: 'from-amber-600 to-yellow-700'
  },
  {
    id: 'music',
    name: '音乐英语',
    icon: '🎵',
    description: '欧美流行金曲 · 经典怀旧老歌 · 从动听歌词学语法',
    gradient: 'from-pink-500 to-rose-600'
  },
  {
    id: 'kids',
    name: '少儿英语',
    icon: '🧸',
    description: '自然拼读启蒙 · 童话绘本 · 日常亲子英文交流',
    gradient: 'from-lime-500 to-green-600'
  }
];
