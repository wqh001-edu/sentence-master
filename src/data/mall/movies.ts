import type { CoursePackage } from '../../types';
import { generateCurriculumChapters, DAILY_CONVERSATION_SENTENCES } from './corpusBuilder';

const movieCorpus = [...DAILY_CONVERSATION_SENTENCES];

export const MOVIES_COURSES: CoursePackage[] = [
  {
    id: 'course-mov-friends',
    title: '《老友记》(Friends) · 地道纽约日常口语精选 (12章全集)',
    category: 'movies',
    categoryName: '影视英语',
    coverGradient: 'from-amber-500 via-orange-600 to-red-700',
    icon: '☕',
    description: '六位老友十年嬉笑怒骂，最真实、最鲜活的美国年轻人高频生活口语。',
    difficulty: '初级 A2',
    tags: ['美剧天花板', '老友记', '地道口语', '幽默诙谐'],
    chapters: generateCurriculumChapters('fr', [
      { title: '第 1 季 · Central Perk 咖啡馆红沙发闲聊' },
      { title: '第 2 季 · 莫妮卡的强迫症与厨房厨艺' },
      { title: '第 3 季 · 乔伊的试镜经历与演员梦想' },
      { title: '第 4 季 · 钱德勒式冷幽默与标志性讽刺' },
      { title: '第 5 季 · 罗斯古生物学博物馆日常笑料' },
      { title: '第 6 季 · 菲比吉他弹唱与奇特灵感' },
      { title: '第 7 季 · 瑞秋时尚圈打拼与职场升职' },
      { title: '第 8 季 · 感恩节橄榄球赛与吃火鸡插曲' },
      { title: '第 9 季 · 伦敦婚礼与跨国旅行冒险' },
      { title: '第 10 季 · 搬离公寓与十年的真挚告别' },
      { title: '特辑 1 · 经典高频俚语与习语脱口而出' },
      { title: '特辑 2 · 盲听对白连读失爆快速识别' }
    ], movieCorpus)
  },
  {
    id: 'course-mov-modern-family',
    title: '《摩登家庭》(Modern Family) · 美式家庭生活对话 (10章全集)',
    category: 'movies',
    categoryName: '影视英语',
    coverGradient: 'from-blue-500 via-indigo-600 to-purple-800',
    icon: '🏡',
    description: '三代人爆笑温馨日常，涵盖育儿、夫妻调侃、职场求生与亲情羁绊。',
    difficulty: '初级 A2',
    tags: ['摩登家庭', '生活会话', '亲子表达', '当代俚语'],
    chapters: generateCurriculumChapters('mf', [
      { title: '第 1 单元 · 菲比式的乐观老爸哲学' },
      { title: '第 2 单元 · 克莱尔的控制狂与家庭日程' },
      { title: '第 3 单元 · 歌洛莉亚浓郁哥伦比亚口音幽默' },
      { title: '第 4 单元 · 杰的铁汉柔情与人生箴言' },
      { title: '第 5 单元 · 卡姆与米奇尔的戏剧化日常' },
      { title: '第 6 单元 · 孩子们的高中毕业与叛逆期' },
      { title: '第 7 单元 · 万圣节变装派对与整蛊恶作剧' },
      { title: '第 8 单元 · 暑假全家露营房车旅行' },
      { title: '第 9 单元 · 亲子代际沟通冲突与温馨化解' },
      { title: '第 10 单元 · 家人永不分离的终身契约' }
    ], movieCorpus)
  },
  {
    id: 'course-mov-gump',
    title: '《阿甘正传》(Forrest Gump) · 传世经典台词精选 (10章全集)',
    category: 'movies',
    categoryName: '影视英语',
    coverGradient: 'from-emerald-600 via-teal-700 to-slate-900',
    icon: '🍫',
    description: '纯真善良的心灵史诗，朴素字句中饱含深刻的人生哲理与时代变迁。',
    difficulty: '入门 A1',
    tags: ['奥斯卡金奖', '人生哲理', '慢速感悟', '至简之美'],
    chapters: generateCurriculumChapters('fg', [
      { title: '第 1 幕 · 绿荫长椅上的巧克力盒人生' },
      { title: '第 2 幕 · 奔跑穿过阿拉巴马绿草地' },
      { title: '第 3 幕 · 妈妈教给我的生活大智慧' },
      { title: '第 4 幕 · 乒乓球外交与专注力的奇迹' },
      { title: '第 5 幕 · 丹中尉与捕虾船暴风雨洗礼' },
      { title: '第 6 幕 · 珍妮的吉他与追寻爱与自由' },
      { title: '第 7 幕 · 穿越全美大洲的无止境奔跑' },
      { title: '第 8 幕 · 华盛顿纪念碑前的水中拥抱' },
      { title: '第 9 幕 · 苹果电脑股票与财富的真谛' },
      { title: '第 10 幕 · 白羽毛飘落与宁静致远的心' }
    ], movieCorpus)
  },
  {
    id: 'course-mov-shawshank',
    title: '《肖申克的救赎》(Shawshank) · 希望与信念赞歌 (10章全集)',
    category: 'movies',
    categoryName: '影视英语',
    coverGradient: 'from-stone-700 via-zinc-800 to-black',
    icon: '🕊️',
    description: 'IMDb 影史排名第一神作，摩根·弗里曼沉稳独白，句句直击灵魂。',
    difficulty: '中级 B1',
    tags: ['影史第一', '坚韧信念', '灵魂独白', '自由希望'],
    chapters: generateCurriculumChapters('sw', [
      { title: '第 1 篇 · 高墙耸立与习惯的体制化' },
      { title: '第 2 篇 · 屋顶涂柏油与喝冰啤酒的微风' },
      { title: '第 3 篇 · 图书馆里莫扎特的费加罗婚礼' },
      { title: '第 4 篇 · 地质小石锤与十九年的凿壁' },
      { title: '第 5 篇 · 穿过五百码污浊下水道的救赎' },
      { title: '第 6 篇 · 暴雨中张开双臂迎接新生自由' },
      { title: '第 7 篇 · 橡树下的铁盒子与给瑞德的信' },
      { title: '第 8 篇 · 太平洋的蓝：芝华塔尼欧海滩' },
      { title: '第 9 篇 · 唯有希望与美好的事物永不消逝' },
      { title: '第 10 篇 · 影史第一神作核心独白总复盘' }
    ], movieCorpus)
  },
  {
    id: 'course-mov-coco',
    title: '《寻梦环游记》(Coco) · 爱与记忆温情原声 (10章全集)',
    category: 'movies',
    categoryName: '影视英语',
    coverGradient: 'from-orange-500 via-pink-600 to-purple-800',
    icon: '🎸',
    description: '皮克斯动画巅峰之作，探讨亲情、梦想与永恒记忆的温暖催泪台词。',
    difficulty: '入门 A1',
    tags: ['皮克斯动画', '亲情记忆', '催泪感动', '地道发音'],
    chapters: generateCurriculumChapters('co', [
      { title: '第 1 幕 · 制鞋世家与被禁止的音乐梦' },
      { title: '第 2 幕 · 万寿菊金桥与亡灵世界的奇观' },
      { title: '第 3 幕 · 流浪乐手埃克托的秘密约定' },
      { title: '第 4 幕 · 歌神德拉库斯的虚伪面具揭穿' },
      { title: '第 5 幕 · 水底岑诺特天井里的亲生父女' },
      { title: '第 6 幕 · 为可可太奶奶轻唱《请记住我》' },
      { title: '第 7 幕 · 真正的死亡是被人世间所遗忘' },
      { title: '第 8 幕 · 家族祖先的无条件祝福与爱' },
      { title: '第 9 幕 · 音乐是连接生者与逝者的红线' },
      { title: '第 10 幕 · 阖家欢聚亡灵节吉他大合唱' }
    ], movieCorpus)
  },
  {
    id: 'course-mov-interstellar',
    title: '《星际穿越》(Interstellar) · 穿越时空的爱与宇宙 (10章全集)',
    category: 'movies',
    categoryName: '影视英语',
    coverGradient: 'from-indigo-950 via-slate-900 to-black',
    icon: '🪐',
    description: '诺兰硬核科幻经典，融合科学探索、诗性台词与超越五维时空的深情。',
    difficulty: '中高 B2',
    tags: ['诺兰科幻', '星际穿越', '狄兰托马斯', '深邃哲思'],
    chapters: generateCurriculumChapters('in', [
      { title: '第 1 幕 · 枯萎病危机与地球沙尘暴肆虐' },
      { title: '第 2 幕 · 手表指针跳动的重力摩斯密码' },
      { title: '第 3 幕 · 穿越土星虫洞的四维时空隧道' },
      { title: '第 4 幕 · 米勒星球一小时等于人间七年' },
      { title: '第 5 幕 · 巨浪排山倒海与争分夺秒撤离' },
      { title: '第 6 幕 · 曼恩博士的背叛与生存本能' },
      { title: '第 7 幕 · 永不言弃对接失控旋转的空间站' },
      { title: '第 8 幕 · 跌入黑洞卡冈图雅的五维超立方体' },
      { title: '第 9 幕 · 爱是唯一能超越时空维度的存在' },
      { title: '第 10 幕 · 不要温和地走入那个良夜' }
    ], movieCorpus)
  },
  {
    id: 'course-mov-harry-potter',
    title: '《哈利·波特》(Harry Potter) · 霍格沃茨魔法金句 (10章全集)',
    category: 'movies',
    categoryName: '影视英语',
    coverGradient: 'from-amber-700 via-stone-800 to-emerald-950',
    icon: '⚡',
    description: 'J.K.罗琳经典英式魔幻世界，邓布利多校长的睿智箴言与三人组友谊。',
    difficulty: '初级 A2',
    tags: ['哈利波特', '魔法世界', '邓布利多', '英式发音'],
    chapters: generateCurriculumChapters('hp', [
      { title: '第 1 章 · 九又四分之三站台与霍格沃茨特快' },
      { title: '第 2 章 · 分院帽的抉择与格兰芬多剑' },
      { title: '第 3 章 · 魔杖选择巫师：奥利凡德魔杖店' },
      { title: '第 4 章 · 魁地奇金色飞贼与扫帚飞行' },
      { title: '第 5 章 · 厄里斯魔镜映射出内心最深渴望' },
      { title: '第 6 章 · 密室蛇佬腔与凤凰福克斯之泪' },
      { title: '第 7 章 · 守护神咒呼神护卫：呼唤最美回忆' },
      { title: '第 8 章 · 三强争霸赛与迷宫中的火焰杯' },
      { title: '第 9 章 · 斯内普教授的永恒誓言：Always' },
      { title: '第 10 章 · 决战霍格沃茨与大难不死的男孩' }
    ], movieCorpus)
  },
  {
    id: 'course-mov-marvel',
    title: '漫威电影宇宙 (MCU) · 超级英雄热血高光台词 (10章全集)',
    category: 'movies',
    categoryName: '影视英语',
    coverGradient: 'from-red-600 via-amber-600 to-slate-900',
    icon: '🛡️',
    description: '钢铁侠、美队、雷神最让影迷热血沸腾的高光台词，激情练听写。',
    difficulty: '初级 A2',
    tags: ['漫威宇宙', '超级英雄', '钢铁侠', '热血高光'],
    chapters: generateCurriculumChapters('mv', [
      { title: '第 1 章 · 我就是钢铁侠：凡人之躯比肩神明' },
      { title: '第 2 章 · 我能陪你耗上一整天：美队的坚守' },
      { title: '第 3 章 · 复仇者联盟集合：纽约大战集结' },
      { title: '第 4 章 · 银河护卫队的无厘头星际歌单' },
      { title: '第 5 章 · 瓦坎达万岁：黑豹的王者气魄' },
      { title: '第 6 章 · 雷神之锤的真正力量源自雷霆内心' },
      { title: '第 7 章 · 灭霸响指与一千四百万分之一的生机' },
      { title: '第 8 章 · 终局之战传送门打开全员到齐' },
      { title: '第 9 章 · 我爱你三千遍：托尼的告别全息影' },
      { title: '第 10 章 · 终点亦是旅途的一部分' }
    ], movieCorpus)
  }
];
