import type { CoursePackage } from '../../types';
import { generateCurriculumChapters, DAILY_CONVERSATION_SENTENCES, WORKPLACE_SENTENCES } from './corpusBuilder';

const recCorpus = [...DAILY_CONVERSATION_SENTENCES, ...WORKPLACE_SENTENCES];

export const RECOMMENDED_COURSES: CoursePackage[] = [
  {
    id: 'course-rec-hot-top10',
    title: '🔥 句乐通年度总榜 · 全站学霸高频热练 TOP 100 句 (12章全集)',
    category: 'recommended',
    categoryName: '精选推荐',
    coverGradient: 'from-amber-500 via-orange-600 to-red-600',
    icon: '🏆',
    description: '综合数十万学习者连词拼写数据，提炼掌握率最高、表达最地道的地道句型。',
    difficulty: '初级 A2',
    tags: ['全站第一', '学霸必备', '地道高频', '连胜挑战'],
    chapters: generateCurriculumChapters('top', [
      { title: '第 1 章 · 破冰问候与初次会面金句' },
      { title: '第 2 章 · 约饭邀约与周末安排闲聊' },
      { title: '第 3 章 · 请求协助与礼貌感谢回应' },
      { title: '第 4 章 · 委婉拒绝与另寻合适时机' },
      { title: '第 5 章 · 情绪共情与朋友失意安慰' },
      { title: '第 6 章 · 观点探讨与赞同反对辩论' },
      { title: '第 7 章 · 闲暇爱好与生活习惯分享' },
      { title: '第 8 章 · 庆祝成功与真挚祝福道贺' },
      { title: '第 9 章 · 道歉赔罪与化解尴尬误会' },
      { title: '第 10 章 · 餐厅聚会结账与礼貌争买单' },
      { title: '第 11 章 · 电话沟通打通与留言代转' },
      { title: '第 12 章 · 告别珍重与保持常联络' }
    ], recCorpus)
  },
  {
    id: 'course-rec-week-new',
    title: '✨ 本周新课 · 硅谷科技与远程工作前沿口语 (10章全集)',
    category: 'recommended',
    categoryName: '精选推荐',
    coverGradient: 'from-indigo-600 via-blue-600 to-purple-700',
    icon: '💻',
    description: '涵盖线上会议、异步协作、敏捷冲刺与 AI 工具调用的现代前沿词汇。',
    difficulty: '中级 B1',
    tags: ['硅谷科技', '远程办公', 'Zoom会议', '本周新课'],
    chapters: generateCurriculumChapters('wn', [
      { title: '第 1 章 · 视频会议上线与网络信号测试' },
      { title: '第 2 章 · 屏幕共享与产品原型走查' },
      { title: '第 3 章 · 敏捷看板任务认领与工期预估' },
      { title: '第 4 章 · 跨时区异步办公协同与文档同步' },
      { title: '第 5 章 · 代码审查与合并请求讨论' },
      { title: '第 6 章 · 线上头脑风暴与思维导图共创' },
      { title: '第 7 章 · 客户需求变更与优先级排期' },
      { title: '第 8 章 · 生产环境突发警报排查沟通' },
      { title: '第 9 章 · 季度 OKR 目标复盘与数据分析' },
      { title: '第 10 章 · 虚拟下午茶与远程团队团建' }
    ], WORKPLACE_SENTENCES)
  },
  {
    id: 'course-rec-editor-choice',
    title: '👑 编辑精选 · 优雅英式长句与高级修辞 (10章全集)',
    category: 'recommended',
    categoryName: '精选推荐',
    coverGradient: 'from-purple-700 via-pink-700 to-rose-900',
    icon: '💎',
    description: '专治表达平淡无奇，教你运用平行结构、隐喻与双重否定写出高级文字。',
    difficulty: '中高 B2',
    tags: ['高级修辞', '散文美感', '编辑力荐', '双重否定'],
    chapters: generateCurriculumChapters('ec', [
      { title: '第 1 章 · 平行对仗与排比结构之美' },
      { title: '第 2 章 · 生动暗喻与拟人修辞手法' },
      { title: '第 3 章 · 双重否定表强烈肯定语气' },
      { title: '第 4 章 · 倒装句增强情感起伏张力' },
      { title: '第 5 章 · 虚拟语气表达深刻哲思感慨' },
      { title: '第 6 章 · 复杂同位语从句层层推进' },
      { title: '第 7 章 · 典雅散文中的时空光影描写' },
      { title: '第 8 章 · 哲理议论中的辩证逻辑权衡' },
      { title: '第 9 章 · 演说辞中的号召力排比高潮' },
      { title: '第 10 章 · 传世经典名篇结尾升华金句' }
    ], recCorpus)
  },
  {
    id: 'course-rec-rapid-master',
    title: '⚡ 7天口语救急 · 出国旅游与紧急应对宝典 (10章全集)',
    category: 'recommended',
    categoryName: '精选推荐',
    coverGradient: 'from-emerald-600 via-teal-600 to-cyan-700',
    icon: '🧭',
    description: '问路、点餐、求救、买药、换汇、报失，一册在手走遍全球都不慌。',
    difficulty: '入门 A1',
    tags: ['紧急救急', '自由行必备', '问路求助', '极速通关'],
    chapters: generateCurriculumChapters('rm', [
      { title: '第 1 章 · 机场出入境与海关抽查问答' },
      { title: '第 2 章 · 酒店办理入住与行李寄存索牌' },
      { title: '第 3 章 · 街头向当地人与交警礼貌问路' },
      { title: '第 4 章 · 乘坐地铁买票与换乘线路辨别' },
      { title: '第 5 章 · 出租车司机打表与导航目的地' },
      { title: '第 6 章 · 餐厅看懂菜单与特色菜品点选' },
      { title: '第 7 章 · 药房买止痛药创可贴与感冒冲剂' },
      { title: '第 8 章 · 银行网点兑换外币与ATM取款' },
      { title: '第 9 章 · 证件遗失报警与大使馆紧急联系' },
      { title: '第 10 章 · 身体突发不适寻求街头急救援助' }
    ], DAILY_CONVERSATION_SENTENCES)
  },
  {
    id: 'course-rec-psychology',
    title: '🧠 心理学与认知思维 · 深度理解人性的英文名言 (10章全集)',
    category: 'recommended',
    categoryName: '精选推荐',
    coverGradient: 'from-blue-800 via-indigo-900 to-slate-950',
    icon: '🔮',
    description: '弗洛伊德、荣格、卡尼曼经典概念，探讨偏见、情商与自我觉察。',
    difficulty: '中级 B1',
    tags: ['心理学', '认知偏差', '卡尼曼', '自我成长'],
    chapters: generateCurriculumChapters('psy', [
      { title: '第 1 章 · 潜意识与直觉决策机制' },
      { title: '第 2 章 · 认知偏差与锚定效应洞察' },
      { title: '第 3 章 · 情绪智商与同理心倾听技术' },
      { title: '第 4 章 · 自我接纳与走出冒充者综合征' },
      { title: '第 5 章 · 心理韧性与逆境中快速复原' },
      { title: '第 6 章 · 习惯回路与微小意志力复利' },
      { title: '第 7 章 · 深度思考与心流状态沉浸' },
      { title: '第 8 章 · 人际界限设立与健康依恋关系' },
      { title: '第 9 章 · 意义感追寻与弗兰克尔心理学' },
      { title: '第 10 章 · 积极心理学与获得持久幸福之道' }
    ], recCorpus)
  },
  {
    id: 'course-rec-business-guru',
    title: '📈 商业领袖传记金句 · 芒格与巴菲特的投资哲学 (10章全集)',
    category: 'recommended',
    categoryName: '精选推荐',
    coverGradient: 'from-amber-700 via-yellow-800 to-stone-900',
    icon: '💵',
    description: '复利思维、逆向思考、能力圈原则，用传世商业箴言磨炼英文语感。',
    difficulty: '中级 B1',
    tags: ['芒格名言', '巴菲特', '复利法则', '逆向思维'],
    chapters: generateCurriculumChapters('bg', [
      { title: '第 1 章 · 逆向思考：总是反过来想' },
      { title: '第 2 章 · 坚守能力圈与杜绝虚假全能' },
      { title: '第 3 章 · 复利奇迹：做时间最好的朋友' },
      { title: '第 4 章 · 商业护城河与核心竞争壁垒' },
      { title: '第 5 章 · 市场非理性波动与贪婪恐惧控制' },
      { title: '第 6 章 · 长期主义与延迟满足感的魅力' },
      { title: '第 7 章 · 诚信品格是无价的商业商誉' },
      { title: '第 8 章 · 跨学科多元思维模型融会贯通' },
      { title: '第 9 章 · 危机时刻的现金储备安全边际' },
      { title: '第 10 章 · 传承与终身学习的最佳实践' }
    ], WORKPLACE_SENTENCES)
  },
  {
    id: 'course-rec-slang',
    title: '💬 2026 美式地道俚语速查 · 像母语者一样脱口而出 (10章全集)',
    category: 'recommended',
    categoryName: '精选推荐',
    coverGradient: 'from-pink-600 via-rose-500 to-amber-500',
    icon: '🍿',
    description: '教科书绝不教的美国年轻人当下最新潮词流行语，打破交流隔阂。',
    difficulty: '初级 A2',
    tags: ['当代俚语', '地道潮词', '脱口秀', '年轻人交流'],
    chapters: generateCurriculumChapters('sl', [
      { title: '第 1 章 · 社交网络与当下网络潮词 (No Cap)' },
      { title: '第 2 章 · 夸赞极度出色 (Nailed It / Slay)' },
      { title: '第 3 章 · 表达赞同附和 (I Feel You / Bet)' },
      { title: '第 4 章 · 尴尬社死与劝人冷静 (Chill Out)' },
      { title: '第 5 章 · 约会闲聊与八卦爆料 (Spill the Tea)' },
      { title: '第 6 章 · 疲惫想摆烂回家 (Call It a Day)' },
      { title: '第 7 章 · 讽刺凡尔赛炫耀 (Flexing)' },
      { title: '第 8 章 · 突发灵感与茅塞顿开 (Hits Different)' },
      { title: '第 9 章 · 聚会狂欢与烘托气氛 (Vibe Check)' },
      { title: '第 10 章 · 告别离场帅气道别 (Peace Out)' }
    ], DAILY_CONVERSATION_SENTENCES)
  },
  {
    id: 'course-rec-traveler',
    title: '🌍 国家地理探险家日记 · 壮美地球与自然奇观 (10章全集)',
    category: 'recommended',
    categoryName: '精选推荐',
    coverGradient: 'from-teal-600 via-emerald-700 to-indigo-900',
    icon: '🏔️',
    description: '国家地理记者笔下的极光、大峡谷、非洲大迁徙，描写语言极具画面感。',
    difficulty: '中级 B1',
    tags: ['国家地理', '大自然', '生动描写', '探索精神'],
    chapters: generateCurriculumChapters('tr', [
      { title: '第 1 章 · 北极圈午夜太阳与翡翠极光' },
      { title: '第 2 章 · 撒哈拉金色沙丘与星空露营' },
      { title: '第 3 章 · 塞伦盖蒂大草原百万角马迁徙' },
      { title: '第 4 章 · 亚马逊热带雨林水系探索' },
      { title: '第 5 章 · 喜马拉雅冰川峰峦徒步日记' },
      { title: '第 6 章 · 大堡礁五彩珊瑚与海洋生态' },
      { title: '第 7 章 · 冰岛火山地热喷泉与黑沙滩' },
      { title: '第 8 章 · 科罗拉多大峡谷亿年地质剖面' },
      { title: '第 9 章 · 保护濒危雪豹与高山红外相机' },
      { title: '第 10 章 · 探险精神：敬畏自然，无畏前行' }
    ], recCorpus)
  }
];
