// 练习模式：中译英、听写（听音拼写）、听力（磨耳朵）、口语评测、阅读模式
export type PracticeMode = 'translate' | 'dictation' | 'listening' | 'speaking' | 'reading';

// 拆分粒度：从单词练、从语块练、只练整句、自定义拆分
export type SplitMode = 'word' | 'chunk' | 'sentence' | 'custom';

// 交互偏好
export type InputPreference = 'hybrid' | 'keyboard' | 'touch';

// 语法成分类型（对标句乐部截图）
export type SyntacticRole = '主语' | '谓语' | '宾语' | '状语' | '定语' | '表语' | '同位语' | '补足语' | '独立成分';

// 单词语法详情
export interface WordGrammar {
  word: string;               // 英文单词
  phonetic?: string;          // 国际音标，如 /heɪ/
  pos?: string;               // 词性，如 感叹词、名词、动词、形容词、副词、助动词、限定词
  role?: SyntacticRole;       // 句子成分：状语、谓语、主语、宾语等
  meaning?: string;           // 单词在句中的中文释义
  note?: string;              // 深入语法注解，如 "be (过去分词): 构成现在完成时"
  explanation?: string;       // 中文深入语法与用法解析
  example?: string;           // 经典英文例句
  exampleCn?: string;         // 例句中文翻译
  family?: string[];          // 派生词族
  synonyms?: string[];        // 近义/同义词
  antonyms?: string[];        // 反义词
  collocations?: { phrase: string; meaning: string }[]; // 常用搭配
}

// 串记 · 联想 · 扩展数据接口
export interface SentenceExpansion {
  // 1. 串记：核心词族派生链
  wordFamily?: {
    root: string;             // 词根词源
    chain: string[];          // 衍生链，如 ["care (v./n.)", "careful (adj.)", "carefully (adv.)", "careless (adj.)"]
  };
  // 2. 联想：与本句语境高度相关的 3-5 个词汇
  associations?: {
    word: string;
    phonetic?: string;
    meaning: string;
  }[];
  // 3. 扩展：高频短语搭配、同义/反义表达及地道例句
  extensions?: {
    phrase: string;
    meaning: string;
    example: string;
    exampleCn: string;
  }[];
}

// 句子单元
export interface SentenceItem {
  id: string;
  english: string;
  chinese: string;
  phonetic?: string;          // 整句音标
  customChunks?: string[];    // 自定义拆分语块
  note?: string;              // 句型小贴士
  wordsGrammar?: WordGrammar[];// 单词级语法信息
  expansion?: SentenceExpansion; // 串记·联想·扩展
}

// 章节单元
export interface Chapter {
  id: string;
  title: string;
  description?: string;
  sentences: SentenceItem[];
}

// 课程商城 9 大分类
export type CourseCategory = 
  | 'recommended'   // 推荐（热门榜、本周新课、编辑精选）
  | 'textbook'      // 教材同步（人教、外研、牛津、新概念）
  | 'exam'          // 考试备考（中考、高考、四级、六级、考研、雅思、托福）
  | 'kids'          // 少儿英语（自然拼读、字母启蒙、童话故事）
  | 'basic'         // 基础学习（音标入门、高频千词、基础句型）
  | 'scenes'        // 场景英语（机场、酒店、西餐、就医、面试）
  | 'reading'       // 阅读听力（短篇故事、名人演讲、慢速新闻）
  | 'movies'        // 影视英语（美剧名台词、经典电影、动画名场面）
  | 'music';        // 音乐英语（流行金曲、欧美老歌）

// 难度等级
export type DifficultyLevel = '入门 A1' | '初级 A2' | '中级 B1' | '中高 B2' | '高级 C1';

// 课程包单元（三级结构第二级）
export interface CoursePackage {
  id: string;
  title: string;
  category: CourseCategory;
  categoryName: string;
  coverGradient: string;      // 渐变封面背景色
  icon: string;               // 封面 Emoji 或图标
  description: string;
  difficulty: DifficultyLevel;
  tags: string[];             // 标签
  chapters: Chapter[];        // 章节列表
}

// 兼容旧接口的轻量课程
export interface Lesson {
  id: string;
  title: string;
  description: string;
  category: string;
  sentences: SentenceItem[];
}

// 练习中的词块单元
export interface ChunkToken {
  id: string;
  text: string;
  fullText: string;
  cleanText: string;
  trailingPunctuation: string;
  grammar?: WordGrammar;      // 关联的语法信息
}

// 用户学习统计与设置
export interface UserSettings {
  autoSpeak: boolean;         // 切句时自动发音
  speechRate: number;         // 发音语速 0.75 - 1.5
  accent: 'en-US' | 'en-GB';  // 美音或英音
  soundEffects: boolean;      // 答题音效开关
  splitMode: SplitMode;       // 当前切分模式
  practiceMode: PracticeMode; // 当前练习模式
  showGrammar: boolean;       // 是否常驻展示语法成分解析
}

export interface UserStats {
  streak: number;
  bestStreak: number;
  correctCount: number;
  mistakeCount: number;
  finishedSentenceIds: string[];
  mistakeSentenceIds: string[];
  // 课程学习进度记录：courseId -> chapterId -> completedCount
  chapterProgress?: Record<string, number>;
  // 最近学习记录
  lastStudied?: {
    courseId: string;
    chapterId: string;
    chapterTitle: string;
    courseTitle: string;
    sentenceIndex: number;
    updatedAt: number;
  };
}
