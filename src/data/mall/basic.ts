import type { CoursePackage } from '../../types';
import { generateCurriculumChapters, DAILY_CONVERSATION_SENTENCES } from './corpusBuilder';

const basicCorpus = [...DAILY_CONVERSATION_SENTENCES];

export const BASIC_COURSES: CoursePackage[] = [
  {
    id: 'course-basic-phonics',
    title: '48个国际音标拼读 · 零基础精准发音 (12章全集)',
    category: 'basic',
    categoryName: '基础学习',
    coverGradient: 'from-emerald-500 via-teal-600 to-cyan-800',
    icon: '🗣️',
    description: '从单元音、双元音到辅音连缀，彻底告别中式方言发音与哑巴英语。',
    difficulty: '入门 A1',
    tags: ['音标拼读', '元音辅音', '连读爆破', '零基础'],
    chapters: generateCurriculumChapters('ph', [
      { title: '第 1 章 · 前元音 /iː/ 与 /ɪ/ 精准舌位辨析' },
      { title: '第 2 章 · 开口元音 /æ/ 与中元音 /e/ 夸张发音' },
      { title: '第 3 章 · 后元音 /uː/ 与 /ʊ/ 唇形圆扁训练' },
      { title: '第 4 章 · 央元音 /ə/ 弱读技巧与中性舌位' },
      { title: '第 5 章 · 合口双元音 /eɪ/, /aɪ/, /ɔɪ/ 滑动规律' },
      { title: '第 6 章 · 集中双元音 /ɪə/, /eə/, /ʊə/ 英美音差异' },
      { title: '第 7 章 · 爆破音 /p/, /b/, /t/, /d/, /k/, /ɡ/ 气流强弱' },
      { title: '第 8 章 · 摩擦音 /f/, /v/, /θ/, /ð/ 咬舌与唇齿' },
      { title: '第 9 章 · 破擦音 /tʃ/, /dʒ/, /tr/, /dr/ 爆破结合' },
      { title: '第 10 章 · 鼻音 /m/, /n/, /ŋ/ 咽腔共鸣感知' },
      { title: '第 11 章 · 舌侧音 /l/ 清音与浊音发音位置' },
      { title: '第 12 章 · 单词重音、连读规则与失爆技巧' }
    ], basicCorpus)
  },
  {
    id: 'course-basic-1000words',
    title: '核心高频 1000 词 · 语境造句实战突破 (12章全集)',
    category: 'basic',
    categoryName: '基础学习',
    coverGradient: 'from-teal-600 via-emerald-700 to-green-900',
    icon: '💡',
    description: '不再机械孤立背单词，将最核心 1000 词放入自然整句中快速形成肌肉记忆。',
    difficulty: '入门 A1',
    tags: ['核心千词', '极速造句', '词汇网络', '初学者必备'],
    chapters: generateCurriculumChapters('b1k', [
      { title: '第 1 组 · 动作与认知高频动词 (1-100)' },
      { title: '第 2 组 · 日常居家与生活物品名词 (101-200)' },
      { title: '第 3 组 · 性格、情绪与外貌形容词 (201-300)' },
      { title: '第 4 组 · 时间、频率与空间副词 (301-400)' },
      { title: '第 5 组 · 沟通、交流与人际互动动词 (401-500)' },
      { title: '第 6 组 · 城市、交通与出行方位词 (501-600)' },
      { title: '第 7 组 · 美食、餐饮与身体健康词 (601-700)' },
      { title: '第 8 组 · 购物、金钱与商业数字词 (701-800)' },
      { title: '第 9 组 · 校园、工作与学习技能词 (801-900)' },
      { title: '第 10 组 · 自然、天气与环保生态词 (901-1000)' },
      { title: '第 11 组 · 核心千词实战造句综合提升' },
      { title: '第 12 组 · 高频词盲听盲拼综合大通关' }
    ], basicCorpus)
  },
  {
    id: 'course-basic-5patterns',
    title: '英语五大基本句型 · 骨架构建完全指南 (10章全集)',
    category: 'basic',
    categoryName: '基础学习',
    coverGradient: 'from-cyan-600 via-blue-700 to-indigo-900',
    icon: '🏗️',
    description: '主谓、主谓宾、主系表、主谓双宾与主谓宾补，一网打尽所有英语句法底层。',
    difficulty: '入门 A1',
    tags: ['五大句型', '语法底层', '主系表', '双宾语'],
    chapters: generateCurriculumChapters('pat', [
      { title: '第 1 讲 · 句型一：主语 + 不及物动词 (S + V)' },
      { title: '第 2 讲 · 句型二：主语 + 及物动词 + 宾语 (S + V + O)' },
      { title: '第 3 讲 · 句型三：主语 + 系动词 + 表语 (S + V + P)' },
      { title: '第 4 讲 · 句型四：主语 + 动词 + 间接宾语 + 直接宾语' },
      { title: '第 5 讲 · 句型五：主语 + 动词 + 宾语 + 宾语补足语' },
      { title: '第 6 讲 · There be 存在句型与主谓一致' },
      { title: '第 7 讲 · 祈使句与感叹句句型结构转换' },
      { title: '第 8 讲 · 一般疑问句与特殊疑问句变换' },
      { title: '第 9 讲 · 复杂修饰语拓展句子主干骨架' },
      { title: '第 10 讲 · 五大句型造句实战纠错与自测' }
    ], basicCorpus)
  },
  {
    id: 'course-basic-tenses',
    title: '英语核心八大时态 · 图解与造句速成 (10章全集)',
    category: 'basic',
    categoryName: '基础学习',
    coverGradient: 'from-blue-600 via-indigo-700 to-purple-900',
    icon: '⏳',
    description: '彻底分清现在完成时、过去完成时、将来进行时与过去进行时。',
    difficulty: '初级 A2',
    tags: ['时态大盘点', '完成时', '进行时', '时间状语'],
    chapters: generateCurriculumChapters('ten', [
      { title: '第 1 讲 · 一般现在时：真理规律与日常习惯' },
      { title: '第 2 讲 · 现在进行时：眼前动作与近期规划' },
      { title: '第 3 讲 · 一般过去时：过去事实与历史叙事' },
      { title: '第 4 讲 · 过去进行时：过去特定时刻背景画面' },
      { title: '第 5 讲 · 一般将来时：will 与 be going to 微妙区别' },
      { title: '第 6 讲 · 现在完成时：过去动作对现在的深远影响' },
      { title: '第 7 讲 · 过去完成时：过去的过去时间参照' },
      { title: '第 8 讲 · 将来进行时：未来特定时间正在发生' },
      { title: '第 9 讲 · 过去将来时：故事叙事中的预见视角' },
      { title: '第 10 讲 · 八大时态混合造句对比大练兵' }
    ], basicCorpus)
  },
  {
    id: 'course-basic-prepositions',
    title: '介词与空间方位 · 介词短语地道搭配 (10章全集)',
    category: 'basic',
    categoryName: '基础学习',
    coverGradient: 'from-amber-600 via-emerald-600 to-teal-800',
    icon: '🧭',
    description: '告别 in/on/at/with/by 乱用，建立立体空间感与时间感知。',
    difficulty: '初级 A2',
    tags: ['介词精讲', '固定搭配', '空间方位', '时间介词'],
    chapters: generateCurriculumChapters('prep', [
      { title: '第 1 讲 · 时间介词 at, on, in 边界划分法则' },
      { title: '第 2 讲 · 空间介词 in, on, under, above, below' },
      { title: '第 3 讲 · 方向与运动介词 to, towards, into, out of' },
      { title: '第 4 讲 · 穿越介词 across, through, along 意象对比' },
      { title: '第 5 讲 · 工具与手段介词 with, by, in, through' },
      { title: '第 6 讲 · 抽象介词 beyond, despite, regarding' },
      { title: '第 7 讲 · 动词 + 介词高频固定短语搭配 (look/take/get)' },
      { title: '第 8 讲 · 形容词 + 介词固定结构 (good at/proud of)' },
      { title: '第 9 讲 · 介词短语充当定语与状语位置' },
      { title: '第 10 讲 · 介词易错题型强化专项通关' }
    ], basicCorpus)
  },
  {
    id: 'course-basic-conjunctions',
    title: '连接词与复合句 · 让表达自然连贯 (10章全集)',
    category: 'basic',
    categoryName: '基础学习',
    coverGradient: 'from-purple-600 via-indigo-700 to-blue-900',
    icon: '🔗',
    description: '逻辑连接词 however, therefore, moreover, although 使句子不再碎成单句。',
    difficulty: '初级 A2',
    tags: ['逻辑连接', '转折因果', '递进对比', '书面语感'],
    chapters: generateCurriculumChapters('conj', [
      { title: '第 1 讲 · 并列连词 and, but, or, so 逻辑顺畅' },
      { title: '第 2 讲 · 因果从句 because, since, as, for' },
      { title: '第 3 讲 · 让步状语从句 although, though, even if' },
      { title: '第 4 讲 · 条件状语从句 if, unless, as long as' },
      { title: '第 5 讲 · 时间状语从句 when, while, as soon as' },
      { title: '第 6 讲 · 结果与目的状语从句 so that, in order that' },
      { title: '第 7 讲 · 比较状语从句 as...as, not so...as' },
      { title: '第 8 讲 · 副词性连接词 however, therefore, moreover' },
      { title: '第 9 讲 · 关联词组 not only...but also, either...or' },
      { title: '第 10 讲 · 段落逻辑衔接与句间过渡实战' }
    ], basicCorpus)
  },
  {
    id: 'course-basic-modals',
    title: '情态动词的微妙语气 · 礼貌与推测的艺术 (10章全集)',
    category: 'basic',
    categoryName: '基础学习',
    coverGradient: 'from-rose-500 via-amber-600 to-orange-700',
    icon: '🎭',
    description: '掌握 could, would, might, must 的不同确定程度与委婉语气。',
    difficulty: '初级 A2',
    tags: ['情态动词', '委婉请求', '逻辑推测', '语气艺术'],
    chapters: generateCurriculumChapters('mod', [
      { title: '第 1 讲 · 表达能力与许可：can, could, may, might' },
      { title: '第 2 讲 · 义务与责任：must, have to, should, ought to' },
      { title: '第 3 讲 · 委婉礼貌请求：Would you / Could you please' },
      { title: '第 4 讲 · 对现在的肯定与否定推测：must be vs can\'t be' },
      { title: '第 5 讲 · 对过去发生事实的推测：must have done' },
      { title: '第 6 讲 · 本该做却未做：should have done 惋惜语气' },
      { title: '第 7 讲 · 本不必做却做了：needn\'t have done' },
      { title: '第 8 讲 · 敢于与意愿：dare 与 would rather than' },
      { title: '第 9 讲 · 习惯性动作：used to do vs would do' },
      { title: '第 10 讲 · 情态动词情境对话综合自测' }
    ], basicCorpus)
  },
  {
    id: 'course-basic-passive',
    title: '被动语态专项 · 客观地道表达的核心钥匙 (10章全集)',
    category: 'basic',
    categoryName: '基础学习',
    coverGradient: 'from-indigo-600 via-slate-700 to-slate-900',
    icon: '⚙️',
    description: '英语重物称、汉语重人称。掌握被动语态是写出地道英文的必备门槛。',
    difficulty: '初级 A2',
    tags: ['被动语态', '客观表达', '科学叙事', '新闻文体'],
    chapters: generateCurriculumChapters('pass', [
      { title: '第 1 讲 · 被动语态底层构造：be + 过去分词 (done)' },
      { title: '第 2 讲 · 一般现在时与一般过去时被动语态' },
      { title: '第 3 讲 · 一般将来时被动语态：will be done' },
      { title: '第 4 讲 · 进行时被动语态：is/was being done' },
      { title: '第 5 讲 · 完成时被动语态：has/have been done' },
      { title: '第 6 讲 · 含有情态动词的被动语态结构' },
      { title: '第 7 讲 · 双宾语动词的被动语态转换法则' },
      { title: '第 8 讲 · 复合宾语动词中省略 to 的恢复 (make/hear)' },
      { title: '第 9 讲 · 形式主动但意义被动的特殊动词 (sell/read)' },
      { title: '第 10 讲 · 科技论文与新闻播报被动句实战' }
    ], basicCorpus)
  }
];
