import type { CoursePackage } from '../../types';
import { generateCurriculumChapters, DAILY_CONVERSATION_SENTENCES } from './corpusBuilder';

const textbookCorpus = [...DAILY_CONVERSATION_SENTENCES];

export const TEXTBOOK_COURSES: CoursePackage[] = [
  {
    id: 'course-nc1',
    title: '《新概念英语》第一册 · 基础全景突破 (12章全集)',
    category: 'textbook',
    categoryName: '教材同步',
    coverGradient: 'from-blue-600 via-indigo-600 to-indigo-800',
    icon: '📘',
    description: '全球公认经典英语教材初级篇。涵盖发音、基础时态、代词与高频日常交流句型。',
    difficulty: '入门 A1',
    tags: ['新概念', '零基础', '经典语法', '日常会话'],
    chapters: generateCurriculumChapters('nc1', [
      { title: '第 1 单元 · 初次见面与随身物品 (Lessons 1-12)' },
      { title: '第 2 单元 · 职业国籍与家庭成员 (Lessons 13-24)' },
      { title: '第 3 单元 · 正在进行时与房间方位 (Lessons 25-36)' },
      { title: '第 4 单元 · 一般现在时与作息习惯 (Lessons 37-48)' },
      { title: '第 5 单元 · 一般过去时与旅行度假 (Lessons 49-60)' },
      { title: '第 6 单元 · 询问时间与情态动词 (Lessons 61-72)' },
      { title: '第 7 单元 · 购物询价与可数不可数 (Lessons 73-84)' },
      { title: '第 8 单元 · 现在完成时与人生经历 (Lessons 85-96)' },
      { title: '第 9 单元 · 比较级与最高级全解析 (Lessons 97-108)' },
      { title: '第 10 单元 · 被动语态与客观叙事 (Lessons 109-120)' },
      { title: '第 11 单元 · 条件状语与未来规划 (Lessons 121-132)' },
      { title: '第 12 单元 · 宾语从句与间接引语 (Lessons 133-144)' }
    ], textbookCorpus)
  },
  {
    id: 'course-nc2',
    title: '《新概念英语》第二册 · 进阶骨架句型 (12章全集)',
    category: 'textbook',
    categoryName: '教材同步',
    coverGradient: 'from-indigo-600 via-purple-600 to-indigo-900',
    icon: '📗',
    description: '掌握复合句、倒装句、非谓语动词与现在完成时，构建牢固英语语法骨架。',
    difficulty: '初级 A2',
    tags: ['新概念', '进阶句型', '故事语法', '初中必背'],
    chapters: generateCurriculumChapters('nc2', [
      { title: '第 1 单元 · 经典叙事与动词时态 (Lessons 1-8)' },
      { title: '第 2 单元 · 过去完成时与事件先后 (Lessons 9-16)' },
      { title: '第 3 单元 · 条件状语从句与主将从现 (Lessons 17-24)' },
      { title: '第 4 单元 · 倒装结构与强烈语气表达 (Lessons 25-32)' },
      { title: '第 5 单元 · 动名词与动词不定式区别 (Lessons 33-40)' },
      { title: '第 6 单元 · 定语从句连接词精准运用 (Lessons 41-48)' },
      { title: '第 7 单元 · 被动语态在故事中的转换 (Lessons 49-56)' },
      { title: '第 8 单元 · 间接引语与时态人称变化 (Lessons 57-64)' },
      { title: '第 9 单元 · 虚拟语气在现实中的表达 (Lessons 65-72)' },
      { title: '第 10 单元 · 介词短语在句首的灵活运用 (Lessons 73-80)' },
      { title: '第 11 单元 · 并列复合句与让步状语从句 (Lessons 81-88)' },
      { title: '第 12 单元 · 经典课文总复习综合自测 (Lessons 89-96)' }
    ], textbookCorpus)
  },
  {
    id: 'course-nc3',
    title: '《新概念英语》第三册 · 高阶母语流利表达 (10章全集)',
    category: 'textbook',
    categoryName: '教材同步',
    coverGradient: 'from-purple-700 via-pink-600 to-indigo-900',
    icon: '📕',
    description: '涵盖英美地道文化、长难句结构、优美散文与同位语从句，冲刺母语级表达。',
    difficulty: '中高 B2',
    tags: ['新概念', '长难句', '高阶表达', '写作典范'],
    chapters: generateCurriculumChapters('nc3', [
      { title: '第 1 单元 · 纪实报道与美洲狮目击 (Unit 1)' },
      { title: '第 2 单元 · 现代考古与远古文明探索 (Unit 2)' },
      { title: '第 3 单元 · 荒岛求生与人性坚韧赞歌 (Unit 3)' },
      { title: '第 4 单元 · 航空飞行与跨大洋冒险 (Unit 4)' },
      { title: '第 5 单元 · 动物智能与深海鲸豚研究 (Unit 5)' },
      { title: '第 6 单元 · 现代医学与人类寿命延长 (Unit 6)' },
      { title: '第 7 单元 · 艺术鉴赏与伪造艺术品骗局 (Unit 7)' },
      { title: '第 8 单元 · 城市化扩张与生态平衡维护 (Unit 8)' },
      { title: '第 9 单元 · 工业革命与科技伦理抉择 (Unit 9)' },
      { title: '第 10 单元 · 哲学随笔与人生沉思集萃 (Unit 10)' }
    ], textbookCorpus)
  },
  {
    id: 'course-pep-7',
    title: '人教版初中英语 · 七年级核心考点句 (10章全集)',
    category: 'textbook',
    categoryName: '教材同步',
    coverGradient: 'from-emerald-600 via-teal-600 to-cyan-800',
    icon: '🎒',
    description: '紧扣教育部新课标人教版七年级上下册，打牢初中词汇与句式基本功。',
    difficulty: '入门 A1',
    tags: ['人教版', '初一', '同步教材', '中考基础'],
    chapters: generateCurriculumChapters('pep7', [
      { title: 'Unit 1 · 结识新朋友与个人介绍' },
      { title: 'Unit 2 · 家庭树与亲属关系称谓' },
      { title: 'Unit 3 · 教室与随身文具辨析' },
      { title: 'Unit 4 · 房间方位与介词短语' },
      { title: 'Unit 5 · 体育运动与课外俱乐部' },
      { title: 'Unit 6 · 营养三餐与果蔬喜好' },
      { title: 'Unit 7 · 服装店购物与价格询问' },
      { title: 'Unit 8 · 生日聚会与月份序数词' },
      { title: 'Unit 9 · 最喜欢的学科与作息表' },
      { title: 'Unit 10 · 动物园参观与特征描述' }
    ], textbookCorpus)
  },
  {
    id: 'course-pep-8',
    title: '人教版初中英语 · 八年级核心提分句 (10章全集)',
    category: 'textbook',
    categoryName: '教材同步',
    coverGradient: 'from-teal-600 via-emerald-600 to-green-800',
    icon: '🏫',
    description: '全面覆盖形容词比较级、最高级、一般将来时与动词不定式。',
    difficulty: '初级 A2',
    tags: ['人教版', '初二', '比较级', '提分必备'],
    chapters: generateCurriculumChapters('pep8', [
      { title: 'Unit 1 · 假期出游与自然风景感悟' },
      { title: 'Unit 2 · 生活好习惯与运动频率 (often/never)' },
      { title: 'Unit 3 · 好朋友性格与外貌特征对比' },
      { title: 'Unit 4 · 城镇最好的影院与餐厅评价' },
      { title: 'Unit 5 · 新年决心与个人未来规划' },
      { title: 'Unit 6 · 制作美味香蕉奶昔与祈使句' },
      { title: 'Unit 7 · 未来世界与人工智能畅想' },
      { title: 'Unit 8 · 接受与谢绝聚会邀请信函' },
      { title: 'Unit 9 · 过去进行时叙述偶发意外' },
      { title: 'Unit 10 · 条件状语从句处理生活难题' }
    ], textbookCorpus)
  },
  {
    id: 'course-pep-9',
    title: '人教版初中英语 · 九年级中考冲刺句 (10章全集)',
    category: 'textbook',
    categoryName: '教材同步',
    coverGradient: 'from-amber-600 via-orange-600 to-red-800',
    icon: '🎓',
    description: '中考定语从句、宾语从句、被动语态高频得分必考点句。',
    difficulty: '初级 A2',
    tags: ['人教版', '初三', '中考冲刺', '语法大纲'],
    chapters: generateCurriculumChapters('pep9', [
      { title: 'Unit 1 · 如何成为高效自主学习者' },
      { title: 'Unit 2 · 中国传统佳节与团聚习俗' },
      { title: 'Unit 3 · 礼貌问路与宾语从句应用' },
      { title: 'Unit 4 · 昔日与今日的巨大成长转变' },
      { title: 'Unit 5 · 传统工艺品与中国制造被动语态' },
      { title: 'Unit 6 · 改变人类历史的重大发明' },
      { title: 'Unit 7 · 青少年规则与家庭成长边界' },
      { title: 'Unit 8 · 侦探破案与情态动词推测' },
      { title: 'Unit 9 · 定语从句表达音乐喜好' },
      { title: 'Unit 10 · 跨文化社交礼仪与习俗禁忌' }
    ], textbookCorpus)
  },
  {
    id: 'course-fltrp-high',
    title: '外研版高中英语 · 必修一核心篇章句 (10章全集)',
    category: 'textbook',
    categoryName: '教材同步',
    coverGradient: 'from-blue-700 via-cyan-700 to-slate-900',
    icon: '📖',
    description: '高中英语新起点，围绕高中生活、友谊、旅行与自然灾害展开。',
    difficulty: '中级 B1',
    tags: ['外研版', '高中必修', '高考核心', '长句精析'],
    chapters: generateCurriculumChapters('fltrp', [
      { title: 'Unit 1 · 迈入高中新校园与破冰结交' },
      { title: 'Unit 2 · 探索英语语言的演变历程' },
      { title: 'Unit 3 · 家庭羁绊与代际沟通艺术' },
      { title: 'Unit 4 · 携手面对突发自然灾害自救' },
      { title: 'Unit 5 · 深入大自然与濒危物种保护' },
      { title: 'Unit 6 · 地球无国界与全球环保倡议' },
      { title: 'Unit 7 · 课外体育运动与奥林匹克精神' },
      { title: 'Unit 8 · 传统戏剧戏剧与世界多元艺术' },
      { title: 'Unit 9 · 科技改变生活与未来交通' },
      { title: 'Unit 10 · 青年担当与社会志愿服务' }
    ], textbookCorpus)
  },
  {
    id: 'course-oxford',
    title: '牛津实用英语 · 纯正英伦思维进阶 (10章全集)',
    category: 'textbook',
    categoryName: '教材同步',
    coverGradient: 'from-indigo-800 via-slate-800 to-blue-950',
    icon: '🏛️',
    description: '牛津大学出版社严谨体系，培养地道英式用词与精准语法习惯。',
    difficulty: '中级 B1',
    tags: ['牛津英语', '英式思维', '严谨语法', '原版精选'],
    chapters: generateCurriculumChapters('ox', [
      { title: 'Chapter 1 · 国际文化差异与跨界包容' },
      { title: 'Chapter 2 · 全球化时代的城市建筑与遗产' },
      { title: 'Chapter 3 · 媒体伦理与真相求证之辨' },
      { title: 'Chapter 4 · 人类行为学与社会群体心理' },
      { title: 'Chapter 5 · 现代文学作品中的批判意识' },
      { title: 'Chapter 6 · 法律条文中的严谨因果界定' },
      { title: 'Chapter 7 · 哲学沉思：道德与功利权衡' },
      { title: 'Chapter 8 · 天文探索与地外生命可能性' },
      { title: 'Chapter 9 · 生态危机与极地冰川消融' },
      { title: 'Chapter 10 · 终身学习与批判性思维培养' }
    ], textbookCorpus)
  }
];
