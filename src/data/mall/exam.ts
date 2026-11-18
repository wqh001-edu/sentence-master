import type { CoursePackage } from '../../types';
import { generateCurriculumChapters, ACADEMIC_EXAM_SENTENCES, WORKPLACE_SENTENCES } from './corpusBuilder';

const examCorpus = [...ACADEMIC_EXAM_SENTENCES, ...WORKPLACE_SENTENCES];

export const EXAM_COURSES: CoursePackage[] = [
  {
    id: 'course-exam-cet4',
    title: '大学英语四级 (CET-4) · 听写与高频满分句 (12章全集)',
    category: 'exam',
    categoryName: '考试备考',
    coverGradient: 'from-rose-600 via-red-600 to-amber-700',
    icon: '📝',
    description: '直击大学英语四级真题听力核心句型、段落翻译与高分写作句式。',
    difficulty: '初级 A2',
    tags: ['四级必备', '大学英语', '听力听写', '翻译冲刺'],
    chapters: generateCurriculumChapters('c4', [
      { title: '第 1 单元 · 社会热点与共享经济' },
      { title: '第 2 单元 · 大学校园生活与时间管理' },
      { title: '第 3 单元 · 人工智能对职业发展冲击' },
      { title: '第 4 单元 · 生态保护与低碳生活实践' },
      { title: '第 5 单元 · 心理健康与大学同侪压力' },
      { title: '第 6 单元 · 传统中国文化向海外传播' },
      { title: '第 7 单元 · 志愿服务与社会奉献精神' },
      { title: '第 8 单元 · 手机依赖症与专注力拯救' },
      { title: '第 9 单元 · 批判性思维与信息鉴别力' },
      { title: '第 10 单元 · 跨国交流与外语学习方法' },
      { title: '第 11 单元 · 诚信考试与学术道德规范' },
      { title: '第 12 单元 · 毕业求职与职业规划蓝图' }
    ], examCorpus)
  },
  {
    id: 'course-exam-cet6',
    title: '大学英语六级 (CET-6) · 进阶真题长难句 (12章全集)',
    category: 'exam',
    categoryName: '考试备考',
    coverGradient: 'from-red-700 via-rose-800 to-slate-900',
    icon: '🏆',
    description: '针对六级高难度阅读理解与深度议论文，掌握倒装、虚拟语气与抽象词表达。',
    difficulty: '中级 B1',
    tags: ['六级真题', '高阶词汇', '复杂从句', '阅读长句'],
    chapters: generateCurriculumChapters('c6', [
      { title: '第 1 单元 · 宏观经济与全球供应链重构' },
      { title: '第 2 单元 · 科技伦理：基因编辑与算法偏见' },
      { title: '第 3 单元 · 深度阅读：长篇议论文主旨提炼' },
      { title: '第 4 单元 · 教育公平与数字化资源鸿沟' },
      { title: '第 5 单元 · 老龄化社会与银发经济机遇' },
      { title: '第 6 单元 · 现代都市焦虑与慢生活哲学' },
      { title: '第 7 单元 · 可持续能源转型与碳达峰' },
      { title: '第 8 单元 · 文化多样性与全球化浪潮' },
      { title: '第 9 单元 · 科学实证与媒体报道偏差' },
      { title: '第 10 单元 · 法律监管与网络个人隐私' },
      { title: '第 11 单元 · 批判性阅读：识别隐蔽让步' },
      { title: '第 12 单元 · 六级写作压轴高分论证句' }
    ], examCorpus)
  },
  {
    id: 'course-exam-postgrad',
    title: '考研英语 · 经典真题长难句深度攻克 (12章全集)',
    category: 'exam',
    categoryName: '考试备考',
    coverGradient: 'from-orange-700 via-red-800 to-stone-900',
    icon: '⚡',
    description: '攻克考研英语命题人最青睐的嵌套从句、非谓语动词与隐蔽分隔结构。',
    difficulty: '中高 B2',
    tags: ['考研英语', '长难句拆解', '翻译得分', '学术考点'],
    chapters: generateCurriculumChapters('pg', [
      { title: '第 1 单元 · 主语从句与同位语从句嵌套' },
      { title: '第 2 单元 · 分隔定语从句与介词后置' },
      { title: '第 3 单元 · 非谓语动词分词短语作状语' },
      { title: '第 4 单元 · 否定转移与双重否定深度剖析' },
      { title: '第 5 单元 · 比较级虚拟结构 (more than/less than)' },
      { title: '第 6 单元 · 倒装句与强调句型真题再现' },
      { title: '第 7 单元 · 经济学人 (The Economist) 经典选段' },
      { title: '第 8 单元 · 自然杂志 (Nature) 学术假说长句' },
      { title: '第 9 单元 · 心理学实验与因果论证逻辑' },
      { title: '第 10 单元 · 法律司法判决与社会伦理争议' },
      { title: '第 11 单元 · 翻译题长句切分四大黄金法则' },
      { title: '第 12 单元 · 大作文图表图画高级升华句' }
    ], examCorpus)
  },
  {
    id: 'course-exam-ielts',
    title: '雅思 (IELTS) · 口语与写作 8 分核心句库 (12章全集)',
    category: 'exam',
    categoryName: '考试备考',
    coverGradient: 'from-red-600 via-rose-700 to-indigo-900',
    icon: '🇬🇧',
    description: '地道英式表达，告别中式翻译腔，掌握地道习语搭配与 Task 2 辩证写作句式。',
    difficulty: '中高 B2',
    tags: ['雅思口语', '大作文8分', '地道俚语', '海外留学'],
    chapters: generateCurriculumChapters('ie', [
      { title: 'Part 1 · 家乡居住环境与建筑风格' },
      { title: 'Part 1 · 业余休闲爱好与户外运动' },
      { title: 'Part 2 · 描述一位令你敬佩的良师益友' },
      { title: 'Part 2 · 描述一次难忘的跨国冒险旅行' },
      { title: 'Part 3 · 科技对现代人际亲密度的影响' },
      { title: 'Part 3 · 政府在城市规划中的职责权衡' },
      { title: 'Task 2 · 环境保护与经济发展双重考量' },
      { title: 'Task 2 · 传统大学教育 vs 在线远程学位' },
      { title: 'Task 2 · 人工智能自动化是否会带来失业' },
      { title: 'Task 2 · 博物馆是否应该对公众完全免费' },
      { title: 'Task 1 · 图表数据动态趋势精准动词' },
      { title: 'Task 1 · 地图题与流程图变迁地道介词' }
    ], examCorpus)
  },
  {
    id: 'course-exam-toefl',
    title: '托福 (TOEFL iBT) · 学术听力与独立写作 (10章全集)',
    category: 'exam',
    categoryName: '考试备考',
    coverGradient: 'from-blue-700 via-indigo-800 to-slate-900',
    icon: '🇺🇸',
    description: '涵盖天文、地质、心理学等北美学术讲座高频听力与独立写作核心论证句。',
    difficulty: '中高 B2',
    tags: ['托福学术', '独立写作', '北美教授讲座', '逻辑衔接'],
    chapters: generateCurriculumChapters('tf', [
      { title: 'Lecture 1 · 天文学：系外行星与类地环境' },
      { title: 'Lecture 2 · 地质学：板块构造与火山运动' },
      { title: 'Lecture 3 · 动物行为学：鸟类迁徙导航机制' },
      { title: 'Lecture 4 · 心理学：记忆遗忘曲线与认知' },
      { title: 'Lecture 5 · 艺术史：文艺复兴透视法革新' },
      { title: 'Writing 1 · 学术讨论：社交媒体对青少年心理' },
      { title: 'Writing 2 · 学术讨论：政府应优先投资哪类基建' },
      { title: 'Writing 3 · 学术讨论：跨学科课程是否应为必修' },
      { title: 'Speaking · 校园对话：图书馆闭馆与选课冲突' },
      { title: 'Speaking · 学术复述：生物拟态伪装策略' }
    ], examCorpus)
  },
  {
    id: 'course-exam-gaokao',
    title: '高考英语 · 核心 3500 词压轴金句 (10章全集)',
    category: 'exam',
    categoryName: '考试备考',
    coverGradient: 'from-amber-600 via-orange-700 to-red-800',
    icon: '🎯',
    description: '高考读后续写、应用文书信与语法填空核心满分句型总复习。',
    difficulty: '初级 A2',
    tags: ['高考必备', '读后续写', '书信满分', '状元句式'],
    chapters: generateCurriculumChapters('gk', [
      { title: '第 1 单元 · 读后续写动作细节精准动词' },
      { title: '第 2 单元 · 喜怒哀乐心理微表情地道描写' },
      { title: '第 3 单元 · 自然环境烘托人物心情金句' },
      { title: '第 4 单元 · 应用文：邀请信与活动行程告知' },
      { title: '第 5 单元 · 应用文：道歉信与补救措施阐明' },
      { title: '第 6 单元 · 应用文：求职信与自荐亮点陈述' },
      { title: '第 7 单元 · 语法填空：冠词、代词与介词常考点' },
      { title: '第 8 单元 · 语法填空：时态语态与主谓一致陷阱' },
      { title: '第 9 单元 · 七选五阅读：逻辑衔接词脉络梳理' },
      { title: '第 10 单元 · 高考满分续写结尾点睛哲理金句' }
    ], examCorpus)
  },
  {
    id: 'course-exam-zhongkao',
    title: '中考英语 · 核心高频考点必背句 (10章全集)',
    category: 'exam',
    categoryName: '考试备考',
    coverGradient: 'from-teal-600 via-cyan-700 to-blue-800',
    icon: '🚩',
    description: '全国各省市中考真题常考主谓一致、时态搭配与宾语从句必背 100 句。',
    difficulty: '入门 A1',
    tags: ['中考冲刺', '基础必背', '主谓一致', '易错辨析'],
    chapters: generateCurriculumChapters('zk', [
      { title: '第 1 单元 · 经典宾语从句陈述句语序' },
      { title: '第 2 单元 · 主将从现与条件状语从句' },
      { title: '第 3 单元 · 连系动词加形容词表感知体验' },
      { title: '第 4 单元 · 一般过去时与过去进行时混考' },
      { title: '第 5 单元 · 现在完成时标志词 (since/for/already)' },
      { title: '第 6 单元 · 感叹句 (What / How) 句型变换' },
      { title: '第 7 单元 · 被动语态在初中常考动词短语' },
      { title: '第 8 单元 · 动词不定式与动名词固定搭配' },
      { title: '第 9 单元 · 建议与提议礼貌句型 (Why not / How about)' },
      { title: '第 10 单元 · 中考英语书信作文满分框架' }
    ], examCorpus)
  },
  {
    id: 'course-exam-gre',
    title: 'GRE · 核心逻辑与学术批判长难句 (10章全集)',
    category: 'exam',
    categoryName: '考试备考',
    coverGradient: 'from-slate-800 via-purple-950 to-black',
    icon: '🧠',
    description: '极高难度学术英语，训练精密批判性思维、让步反驳与复杂同位语。',
    difficulty: '高级 C1',
    tags: ['GRE逻辑', '学术思辨', '复杂让步', '极高难度'],
    chapters: generateCurriculumChapters('gre', [
      { title: '第 1 单元 · 科学假说与反直觉实验证据' },
      { title: '第 2 单元 · 历史学派之间的史料解读论战' },
      { title: '第 3 单元 · 文学批评中的解构主义与符号学' },
      { title: '第 4 单元 · 经济学模型与复杂现实世界背离' },
      { title: '第 5 单元 · 认知神经科学与意识难题探究' },
      { title: '第 6 单元 · 生态演化中的渐变论与突变论' },
      { title: '第 7 单元 · 政治哲学：契约论与功利论博弈' },
      { title: '第 8 单元 · 科学哲学：范式转换与波普尔反证' },
      { title: '第 9 单元 · 高频强转折与隐晦让步逻辑剖析' },
      { title: '第 10 单元 · Issue 与 Argument 黄金破题论证' }
    ], examCorpus)
  }
];
