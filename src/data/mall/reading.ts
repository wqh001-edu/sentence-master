import type { CoursePackage } from '../../types';
import { generateCurriculumChapters, ACADEMIC_EXAM_SENTENCES } from './corpusBuilder';

const readingCorpus = [...ACADEMIC_EXAM_SENTENCES];

export const READING_COURSES: CoursePackage[] = [
  {
    id: 'course-read-jobs',
    title: '史蒂夫·乔布斯斯坦福演讲 · 改变世界的求知心 (10章全集)',
    category: 'reading',
    categoryName: '阅读听力',
    coverGradient: 'from-slate-800 via-zinc-900 to-black',
    icon: '🍎',
    description: '“Stay Hungry, Stay Foolish”——世界演讲史上的旷世名篇，句句发人深省。',
    difficulty: '中级 B1',
    tags: ['名校演讲', '乔布斯', '求知若饥', '人生抉择'],
    chapters: generateCurriculumChapters('jb', [
      { title: '第 1 篇 · 串联生命中的点点滴滴 (The First Story)' },
      { title: '第 2 篇 · 旁听大学英文书法课的意外馈赠' },
      { title: '第 3 篇 · 爱与失去：三十岁被自己创立的公司解雇' },
      { title: '第 4 篇 · 重新出发的轻盈与创办皮克斯的辉煌' },
      { title: '第 5 篇 · 伟大的工作唯有源自于你发自内心的热爱' },
      { title: '第 6 篇 · 死亡认知：摆脱世俗虚荣的最佳解药' },
      { title: '第 7 篇 · 时间极其有限，切莫虚度去过别人的生活' },
      { title: '第 8 篇 · 遵循内心的直觉与勇气之声' },
      { title: '第 9 篇 · 全球概览年鉴停刊号的清晨告别' },
      { title: '第 10 篇 · 求知若饥，虚怀若愚 (Stay Hungry, Stay Foolish)' }
    ], readingCorpus)
  },
  {
    id: 'course-read-aesop',
    title: '《伊索寓言》(Aesop\'s Fables) · 纯真哲理短篇 (10章全集)',
    category: 'reading',
    categoryName: '阅读听力',
    coverGradient: 'from-amber-600 via-yellow-600 to-orange-800',
    icon: '🦊',
    description: '《龟兔赛跑》《农夫与蛇》《狐狸与葡萄》，言简意赅的古希腊传世智慧。',
    difficulty: '入门 A1',
    tags: ['伊索寓言', '寓言故事', '简单过去时', '经典智慧'],
    chapters: generateCurriculumChapters('as', [
      { title: '第 1 篇 · 龟兔赛跑：慢而稳者终将致胜' },
      { title: '第 2 篇 · 狐狸与葡萄：吃不到便说酸的心态' },
      { title: '第 3 篇 · 农夫与蛇：不要对恶劣本性心存侥幸' },
      { title: '第 4 篇 · 狼来了：谎言会摧毁宝贵的信任' },
      { title: '第 5 篇 · 乌鸦喝水：智慧与耐心胜过蛮力' },
      { title: '第 6 篇 · 城市老鼠与乡下老鼠：安宁胜过繁华' },
      { title: '第 7 篇 · 北风与太阳：温暖的力量胜于暴烈' },
      { title: '第 8 篇 · 狮子与老鼠：弱小者亦能施以援手' },
      { title: '第 9 篇 · 牧童与金斧头：诚实是永恒的美德' },
      { title: '第 10 篇 · 蚂蚁与蚱蜢：未雨绸缪方能度过严冬' }
    ], readingCorpus)
  },
  {
    id: 'course-read-ted',
    title: 'TED 殿堂级高分演讲 · 洞察思想的火花 (10章全集)',
    category: 'reading',
    categoryName: '阅读听力',
    coverGradient: 'from-rose-600 via-red-700 to-slate-900',
    icon: '🎙️',
    description: '涵盖公众演讲技巧、脆弱的力量、习惯的养成等全球收看破千万的演讲金句。',
    difficulty: '中级 B1',
    tags: ['TED演讲', '思维认知', '沟通表达', '前沿思想'],
    chapters: generateCurriculumChapters('td', [
      { title: '第 1 讲 · 布琳·布朗：脆弱与不完美的力量' },
      { title: '第 2 讲 · 詹姆斯·克利尔：原子习惯的惊人复利' },
      { title: '第 3 讲 · 西蒙·斯涅克：从“为什么”开始思考' },
      { title: '第 4 讲 · 艾米·卡迪：肢体语言塑造你的内心' },
      { title: '第 5 讲 · 肯·罗宾逊：学校正在扼杀创造力吗' },
      { title: '第 6 讲 · 蒂姆·厄本：揭秘重度拖延症的大脑' },
      { title: '第 7 讲 · 罗伯特·瓦丁格：哈佛 75 年幸福生活研究' },
      { title: '第 8 讲 · 苏珊·凯恩：内向性格者在嘈杂世界的价值' },
      { title: '第 9 讲 · 凯利·麦格尼格尔：如何化压力为你的朋友' },
      { title: '第 10 讲 · 汉斯·罗斯林：用真实客观数据破除全球偏见' }
    ], readingCorpus)
  },
  {
    id: 'course-read-little-prince',
    title: '《小王子》(The Little Prince) · 诗意法兰西中英双语 (10章全集)',
    category: 'reading',
    categoryName: '阅读听力',
    coverGradient: 'from-blue-600 via-indigo-700 to-purple-900',
    icon: '🌹',
    description: '献给所有曾经是孩子的大人，优美纯净的治愈系文学金句。',
    difficulty: '初级 A2',
    tags: ['小王子', '治愈美文', '玫瑰与狐狸', '文学名著'],
    chapters: generateCurriculumChapters('lp', [
      { title: '第 1 节 · 六岁时画的那条吞下大象的蟒蛇' },
      { title: '第 2 节 · 撒哈拉沙漠中相遇：请为我画一只羊' },
      { title: '第 3 节 · B612 小行星上的三座火山与猴面包树' },
      { title: '第 4 节 · 骄傲而脆弱的独一无二的红玫瑰' },
      { title: '第 5 节 · 独自旅行：国王、自负者与点灯人' },
      { title: '第 6 节 · 降落地球：五千朵玫瑰的盛大花园' },
      { title: '第 7 节 · 狐狸的秘密：实质性的东西眼睛是看不见的' },
      { title: '第 8 节 · 驯服意味着建立起彼此生命中的独一羁绊' },
      { title: '第 9 节 · 沙漠深处的清泉：用脚步寻找心中的甘甜' },
      { title: '第 10 节 · 仰望繁星：所有的星星都像五亿个小风铃在笑' }
    ], readingCorpus)
  },
  {
    id: 'course-read-voa',
    title: 'VOA 慢速标准英语 · 国际热点新闻精听 (10章全集)',
    category: 'reading',
    categoryName: '阅读听力',
    coverGradient: 'from-cyan-700 via-blue-800 to-slate-950',
    icon: '📡',
    description: '语速适中（每分钟约 90 词），词汇控制在 1500 词内，听力入门黄金材料。',
    difficulty: '初级 A2',
    tags: ['VOA慢速', '新闻精听', '国际热点', '标准美音'],
    chapters: generateCurriculumChapters('va', [
      { title: '第 1 篇 · 全球可再生绿色清洁能源飞速崛起' },
      { title: '第 2 篇 · 人工智能与深海生物多样性探测' },
      { title: '第 3 篇 · 全球老龄化健康护理体系发展动态' },
      { title: '第 4 篇 · 发展中国家农村互联网覆盖重大突破' },
      { title: '第 5 篇 · 联合国气候大会碳中和承诺实施追踪' },
      { title: '第 6 篇 · 新型防旱耐盐碱作物培育农业革新' },
      { title: '第 7 篇 · 国际空间站新一期多国科学实验展开' },
      { title: '第 8 篇 · 世界文化遗产古迹数字化保护成果' },
      { title: '第 9 篇 · 现代城市垃圾分类循环利用优秀范例' },
      { title: '第 10 篇 · 全球教育减贫项目给女孩带来的希望' }
    ], readingCorpus)
  },
  {
    id: 'course-read-classic-novels',
    title: '英美经典小说节选 · 简·爱与呼啸山庄 (10章全集)',
    category: 'reading',
    categoryName: '阅读听力',
    coverGradient: 'from-stone-700 via-amber-900 to-slate-900',
    icon: '🏰',
    description: '十九世纪英国文学明珠，品读细腻的人物心理描写与经典对白。',
    difficulty: '中高 B2',
    tags: ['简爱', '古典文学', '英伦名著', '深度文学'],
    chapters: generateCurriculumChapters('nv', [
      { title: '第 1 篇 · 盖茨黑德府红房子里的幼年反抗' },
      { title: '第 2 篇 · 洛伍德慈善学校里的艰难求学生涯' },
      { title: '第 3 篇 · 桑菲尔德庄园初遇罗切斯特先生' },
      { title: '第 4 篇 · 暴风雨夜书房里的平等灵魂交谈' },
      { title: '第 5 篇 · 阁楼疯女人的秘密与婚礼变故' },
      { title: '第 6 篇 · 荒原流浪与圣约翰的宗教邀请' },
      { title: '第 7 篇 · 听见夜风中的深情呼唤返回桑菲尔德' },
      { title: '第 8 篇 · 废墟重逢：读者，我嫁给了他' },
      { title: '第 9 篇 · 呼啸山庄：希斯克利夫荒野咆哮' },
      { title: '第 10 篇 · 傲慢与偏见：达西先生彭伯里雨中告白' }
    ], readingCorpus)
  },
  {
    id: 'course-read-biography',
    title: '达芬奇与富兰克林传 · 跨学科通才的思考笔记 (10章全集)',
    category: 'reading',
    categoryName: '阅读听力',
    coverGradient: 'from-amber-800 via-orange-900 to-stone-950',
    icon: '📜',
    description: '沃特·艾萨克森笔下的传记巨著，探寻人类历史上顶尖好奇心与创造力。',
    difficulty: '中级 B1',
    tags: ['大师传记', '富兰克林', '通才思维', '非虚构阅读'],
    chapters: generateCurriculumChapters('bi', [
      { title: '第 1 章 · 永无止境的好奇心：观察啄木鸟的舌头' },
      { title: '第 2 章 · 蒙娜丽莎神秘微笑背后的面部解剖' },
      { title: '第 3 章 · 水流漩涡观察与飞行器机械草图' },
      { title: '第 4 章 · 本杰明·富兰克林自律十三条美德清单' },
      { title: '第 5 章 · 雷雨天风筝引雷与电学实验重大发现' },
      { title: '第 6 章 · 印刷学徒到开创公共图书馆先河' },
      { title: '第 7 章 · 撰写《穷查理年鉴》中的民间智慧格言' },
      { title: '第 8 章 · 跨大西洋外交博弈与签署独立宣言' },
      { title: '第 9 章 · 科学与艺术交汇处迸发的永恒灵感' },
      { title: '第 10 章 · 终身成长：不为自己设立专业边界' }
    ], readingCorpus)
  },
  {
    id: 'course-read-podcasts',
    title: '海外热门英语播客 · 对话世界文化与生活 (10章全集)',
    category: 'reading',
    categoryName: '阅读听力',
    coverGradient: 'from-purple-800 via-indigo-900 to-black',
    icon: '🎧',
    description: '还原真实母语者之间的无障碍对谈、插话、赞同与幽默反问。',
    difficulty: '中级 B1',
    tags: ['播客听力', '自然对话', '口语连读', '流行文化'],
    chapters: generateCurriculumChapters('pd', [
      { title: 'Episode 1 · 现代极简主义生活方式践行者访谈' },
      { title: 'Episode 2 · 深度睡眠与清晨高效精力的神经学机制' },
      { title: 'Episode 3 · 数字游民 (Digital Nomad) 环球远程旅行' },
      { title: 'Episode 4 · 独立播客主如何从零打造百万收听节目' },
      { title: 'Episode 5 · 咖啡狂热爱好者的世界精品豆地图' },
      { title: 'Episode 6 · 心理健康：面对职场倦怠时的科学解压' },
      { title: 'Episode 7 · 个人财务自由与早期退休 (FIRE) 运动' },
      { title: 'Episode 8 · 未来城市规划与十五分钟生活圈构想' },
      { title: 'Episode 9 · 语言习得专家揭秘成年人流利外语秘诀' },
      { title: 'Episode 10 · 听众来信互动问答与年度走心总结' }
    ], readingCorpus)
  }
];
