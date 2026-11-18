import type { SentenceExpansion } from '../types';

// 常见停用词集合（过滤辅助词，聚焦核心词）
const STOP_WORDS = new Set([
  'a', 'an', 'the', 'is', 'am', 'are', 'was', 'were', 'be', 'been', 'being',
  'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should',
  'can', 'could', 'may', 'might', 'must', 'to', 'of', 'in', 'for', 'on', 'with',
  'at', 'by', 'from', 'up', 'about', 'into', 'over', 'after', 'beneath', 'under',
  'above', 'the', 'and', 'but', 'or', 'nor', 'so', 'yet', 'if', 'because', 'as',
  'until', 'while', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him',
  'her', 'us', 'them', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'mine',
  'yours', 'ours', 'theirs', 'this', 'that', 'these', 'those', 'what', 'which',
  'who', 'whom', 'whose', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
  'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
  'only', 'own', 'same', 'so', 'than', 'too', 'very', 'just', 'could', 'please'
]);

// 词族核心库（涵盖上百个高频词根）
const ROOT_FAMILIES: Record<string, { root: string; chain: string[] }> = {
  suit: { root: 'suit (合适/套装)', chain: ['suit (v. 适合 / n. 套装)', 'suitable (adj. 合适的)', 'suitably (adv. 合适地)', 'unsuited (adj. 不适合的)'] },
  protect: { root: 'protect (保护)', chain: ['protect (v. 保护)', 'protection (n. 保护/防卫)', 'protective (adj. 给予保护的)', 'protectively (adv. 保护性地)'] },
  measure: { root: 'measure (衡量/措施)', chain: ['measure (v. 测量 / n. 措施)', 'measurement (n. 尺寸/测量)', 'measurable (adj. 可测量的)', 'immeasurable (adj. 无法估量的)'] },
  hand: { root: 'hand (手/给予)', chain: ['hand (n. 手 / v. 传递)', 'handy (adj. 便利的/手边的)', 'handful (n. 一把/少许)', 'handbook (n. 手册/指南)'] },
  see: { root: 'see (看见/领会)', chain: ['see (v. 看见/理解)', 'sight (n. 视力/景象)', 'foresee (v. 预见)', 'unseen (adj. 未被注意到的)'] },
  time: { root: 'time (时间/时代)', chain: ['time (n. 时间 / v. 计时)', 'timely (adj. 及时的)', 'timeless (adj. 永恒的)', 'overtime (n./adv. 加班)'] },
  heavy: { root: 'heavy (沉重/剧烈)', chain: ['heavy (adj. 沉重的)', 'heavily (adv. 沉重地/剧烈地)', 'heaviness (n. 沉重/沉重感)', 'heavyweight (n. 重量级人物)'] },
  fragile: { root: 'fragile (脆弱/易碎)', chain: ['fragile (adj. 易碎的/脆弱的)', 'fragility (n. 脆弱/脆弱性)', 'fragment (n. 碎片 / v. 分裂)', 'fragmentary (adj. 支离破碎的)'] },
  environment: { root: 'environment (环境)', chain: ['environment (n. 自然/生活环境)', 'environmental (adj. 环境的)', 'environmentally (adv. 在环境方面)', 'environmentalist (n. 环保主义者)'] },
  effect: { root: 'effect (效果/影响)', chain: ['effect (n. 影响 / v. 产生)', 'effective (adj. 有效的)', 'effectively (adv. 有效地)', 'effectiveness (n. 有效性)'] },
  care: { root: 'care (关心/关怀)', chain: ['care (v./n. 关心/关爱)', 'careful (adj. 小心的)', 'carefully (adv. 仔细地)', 'careless (adj. 粗心大意的)'] },
  succeed: { root: 'succeed (成功/继承)', chain: ['succeed (v. 成功/接替)', 'success (n. 成功)', 'successful (adj. 成功的)', 'successfully (adv. 成功地)'] },
  decide: { root: 'decide (决定)', chain: ['decide (v. 决定/断定)', 'decision (n. 决定/决议)', 'decisive (adj. 果断的/决定性的)', 'decisively (adv. 果断地)'] },
  create: { root: 'create (创造/引起)', chain: ['create (v. 创造/引起)', 'creation (n. 创造/作品)', 'creative (adj. 有创造力的)', 'creativity (n. 创造力/独创性)'] },
  differ: { root: 'differ (不同/相异)', chain: ['differ (v. 相异/有分歧)', 'different (adj. 不同的)', 'differently (adv. 不同地)', 'difference (n. 差异/不同之处)'] },
  employ: { root: 'employ (雇佣/运用)', chain: ['employ (v. 雇佣/使用)', 'employer (n. 雇主)', 'employee (n. 雇员)', 'employment (n. 就业/职业)'] },
  educate: { root: 'educate (教育/教导)', chain: ['educate (v. 教育/训练)', 'education (n. 教育/培养)', 'educational (adj. 有教育意义的)', 'educator (n. 教育工作者)'] },
  impress: { root: 'impress (留下深刻印象)', chain: ['impress (v. 使钦佩/给...深刻印象)', 'impression (n. 印象/感想)', 'impressive (adj. 令人赞叹的)', 'impressively (adv. 感人地)'] },
  organize: { root: 'organize (组织/安排)', chain: ['organize (v. 组织/筹划)', 'organization (n. 组织/机构)', 'organizer (n. 组织者)', 'organized (adj. 有条理的)'] },
  solve: { root: 'solve (解决/解答)', chain: ['solve (v. 解决/解答)', 'solution (n. 解决方案)', 'solvable (adj. 可解决的)', 'insoluble (adj. 不能解决的)'] },
  hope: { root: 'hope (希望/期盼)', chain: ['hope (v./n. 希望/期望)', 'hopeful (adj. 抱有希望的)', 'hopefully (adv. 但愿/有希望地)', 'hopeless (adj. 绝望的/无能为力的)'] },
  act: { root: 'act (行动/表演)', chain: ['act (v./n. 行动/表现)', 'action (n. 行动/活动)', 'actor (n. 演员)', 'active (adj. 积极活跃的)'] },
  develop: { root: 'develop (发展/开发)', chain: ['develop (v. 发展/形成)', 'development (n. 发展/成长)', 'developer (n. 开发者/开发商)', 'developmental (adj. 发展的)'] },
  speak: { root: 'speak (说话/表达)', chain: ['speak (v. 说话/演讲)', 'speaker (n. 演讲者/发言人)', 'spoken (adj. 口头的/口语的)', 'speech (n. 演讲/说话能力)'] },
  listen: { root: 'listen (倾听)', chain: ['listen (v. 倾听/服从)', 'listener (n. 听众/倾听者)', 'listening (n. 听力 / adj. 倾听的)'] },
  read: { root: 'read (阅读/理解)', chain: ['read (v. 阅读/朗诵)', 'reader (n. 读者)', 'readable (adj. 清晰易读的)', 'reading (n. 阅读/读物)'] },
  write: { root: 'write (书写/写作)', chain: ['write (v. 书写/创作)', 'writer (n. 作家/作者)', 'written (adj. 书面的)', 'writing (n. 作品/写作)'] },
  know: { root: 'know (知道/认识)', chain: ['know (v. 知道/了解)', 'knowledge (n. 知识/学问)', 'knowledgeable (adj. 博学的)', 'unknown (adj. 未知的)'] },
  think: { root: 'think (思考/认为)', chain: ['think (v. 思考/认为)', 'thought (n. 思想/想法)', 'thoughtful (adj. 体贴周到的)', 'thoughtless (adj. 欠考虑的)'] },
  live: { root: 'live (生活/居住)', chain: ['live (v. 居住/生活)', 'alive (adj. 活着的)', 'lively (adj. 充满活力的)', 'lifestyle (n. 生活方式)'] },
  friend: { root: 'friend (朋友)', chain: ['friend (n. 朋友)', 'friendly (adj. 友善的)', 'friendship (n. 友谊/情谊)', 'friendless (adj. 无友相伴的)'] },
  comfort: { root: 'comfort (安慰/舒适)', chain: ['comfort (n. 舒适 / v. 安慰)', 'comfortable (adj. 舒服的)', 'comfortably (adv. 舒舒服服地)', 'uncomfortable (adj. 不舒服的)'] },
  attract: { root: 'attract (吸引)', chain: ['attract (v. 吸引/引起)', 'attraction (n. 吸引力/景点)', 'attractive (adj. 极具吸引力的)', 'attractively (adv. 动人地)'] },
  compete: { root: 'compete (竞争/比赛)', chain: ['compete (v. 竞争/角逐)', 'competition (n. 竞赛/比赛)', 'competitive (adj. 具有竞争力的)', 'competitor (n. 竞争对手)'] },
  connect: { root: 'connect (连接/联系)', chain: ['connect (v. 连接/联结)', 'connection (n. 联系/关联)', 'connected (adj. 有联系的)', 'connectivity (n. 连通性)'] },
  beauty: { root: 'beauty (美/美好)', chain: ['beauty (n. 美丽/美人)', 'beautiful (adj. 美丽的)', 'beautifully (adv. 优美地)', 'beautify (v. 美化/修饰)'] },
  excite: { root: 'excite (激动/兴奋)', chain: ['excite (v. 使兴奋/激动)', 'excited (adj. 激动的)', 'exciting (adj. 令人兴奋的)', 'excitement (n. 兴奋/激动)'] }
};

// 句子情境主题词矩阵（10 大生活与学术高频语境）
const THEMATIC_ASSOCIATIONS: Record<string, { word: string; phonetic: string; meaning: string }[]> = {
  social: [
    { word: 'greeting', phonetic: '/ˈɡriːtɪŋ/', meaning: '问候；致敬' },
    { word: 'acquaintance', phonetic: '/əˈkweɪntəns/', meaning: '熟人；相识' },
    { word: 'courtesy', phonetic: '/ˈkɜːrtəsi/', meaning: '礼貌；谦恭' },
    { word: 'conversation', phonetic: '/ˌkɒnvəˈseɪʃən/', meaning: '交谈；谈话' },
    { word: 'compliment', phonetic: '/ˈkɒmplɪmənt/', meaning: '称赞；赞美' }
  ],
  travel: [
    { word: 'destination', phonetic: '/ˌdɛstɪˈneɪʃən/', meaning: '目的地；终点' },
    { word: 'itinerary', phonetic: '/aɪˈtɪnərəri/', meaning: '旅行日程；路线' },
    { word: 'departure', phonetic: '/dɪˈpɑːrtʃər/', meaning: '出发；离境' },
    { word: 'souvenir', phonetic: '/ˌsuːvəˈnɪər/', meaning: '纪念品；纪念物' },
    { word: 'accommodate', phonetic: '/əˈkɒmədeɪt/', meaning: '提供住宿；容纳' }
  ],
  work: [
    { word: 'collaboration', phonetic: '/kəˌlæbəˈreɪʃən/', meaning: '合作；协同工作' },
    { word: 'deadline', phonetic: '/ˈdɛdlaɪn/', meaning: '最后期限；截止日期' },
    { word: 'productivity', phonetic: '/ˌprɒdʌkˈtɪvɪti/', meaning: '生产率；工作效率' },
    { word: 'milestone', phonetic: '/ˈmaɪlstoʊn/', meaning: '里程碑；重大阶段' },
    { word: 'negotiate', phonetic: '/nɪˈɡoʊʃieɪt/', meaning: '商议；谈判协商' }
  ],
  study: [
    { word: 'comprehension', phonetic: '/ˌkɒmprɪˈhɛnʃən/', meaning: '理解；领悟能力' },
    { word: 'fluency', phonetic: '/ˈfluːənsi/', meaning: '流利度；语感' },
    { word: 'curriculum', phonetic: '/kəˈrɪkjʊləm/', meaning: '课程大纲；课程设置' },
    { word: 'proficiency', phonetic: '/prəˈfɪʃənsi/', meaning: '熟练程度；精通' },
    { word: 'insight', phonetic: '/ˈɪnsaɪt/', meaning: '洞察力；真知灼见' }
  ],
  life: [
    { word: 'routine', phonetic: '/ruːˈtiːn/', meaning: '常规；日常作息' },
    { word: 'leisure', phonetic: '/ˈlɛʒər/', meaning: '闲暇；从容不迫' },
    { word: 'gratitude', phonetic: '/ˈɡrætɪtjuːd/', meaning: '感激之情；感恩' },
    { word: 'balance', phonetic: '/ˈbæləns/', meaning: '平衡；身心调和' },
    { word: 'fulfillment', phonetic: '/fʊlˈfɪlmənt/', meaning: '充实感；成就感' }
  ],
  nature: [
    { word: 'ecosystem', phonetic: '/ˈiːkoʊˌsɪstəm/', meaning: '生态系统' },
    { word: 'biodiversity', phonetic: '/ˌbaɪoʊdaɪˈvɜːrsɪti/', meaning: '生物多样性' },
    { word: 'conservation', phonetic: '/ˌkɒnsərˈveɪʃən/', meaning: '自然保护；节约' },
    { word: 'atmosphere', phonetic: '/ˈætməsˌfɪər/', meaning: '大气层；空气' },
    { word: 'sustainable', phonetic: '/səˈsteɪnəbl/', meaning: '可持续发展的' }
  ],
  emotion: [
    { word: 'optimistic', phonetic: '/ˌɒptɪˈmɪstɪk/', meaning: '乐观豁达的' },
    { word: 'empathy', phonetic: '/ˈɛmpəθi/', meaning: '同理心；感同身受' },
    { word: 'resilience', phonetic: '/rɪˈzɪliəns/', meaning: '坚韧不拔；韧性' },
    { word: 'affection', phonetic: '/əˈfɛkʃən/', meaning: '喜爱；深厚钟爱' },
    { word: 'enthusiasm', phonetic: '/ɪnˈθjuːziæzəm/', meaning: '热情；极大兴趣' }
  ]
};

// 常见核心词的固定搭配与地道例句库
const COLLOCATIONS_BANK: Record<string, { phrase: string; meaning: string; example: string; exampleCn: string }[]> = {
  suit: [
    { phrase: 'suit one\'s needs', meaning: '满足某人的需求', example: 'This modern apartment perfectly suits our family\'s needs.', exampleCn: '这间现代化的公寓完全符合我们一家的需求。' },
    { phrase: 'follow suit', meaning: '照着做；跟着做', example: 'When one company lowered prices, other competitors followed suit.', exampleCn: '当一家公司降价时，其他竞争对手也纷纷效仿。' }
  ],
  protect: [
    { phrase: 'protect against', meaning: '防范；抵御', example: 'Wearing sunscreen helps protect your skin against harmful UV rays.', exampleCn: '涂抹防晒霜有助于保护皮肤免受有害紫外线的伤害。' },
    { phrase: 'protect one\'s rights', meaning: '维护合法权益', example: 'The new law was passed to protect consumers\' legal rights.', exampleCn: '这项新法律的通过是为了维护消费者的合法权益。' }
  ],
  measure: [
    { phrase: 'take measures to', meaning: '采取措施做某事', example: 'Governments worldwide must take immediate measures to curb pollution.', exampleCn: '全球各国政府必须立即采取措施遏制污染。' },
    { phrase: 'in large measure', meaning: '在很大程度上', example: 'His miraculous recovery was in large measure due to regular exercise.', exampleCn: '他的奇迹般康复在很大程度上归功于规律的锻炼。' }
  ],
  hand: [
    { phrase: 'give sb. a hand', meaning: '帮某人一把', example: 'Could you give me a hand with lifting this heavy sofa?', exampleCn: '你能帮我一起抬一下这张沉重的沙发吗？' },
    { phrase: 'on the other hand', meaning: '另一方面（转折对比）', example: 'City life is exciting; on the other hand, it can be rather stressful.', exampleCn: '城市生活令人兴奋，但另一方面它也相当令人有压力。' }
  ],
  see: [
    { phrase: 'see eye to eye with', meaning: '与某人看法一致', example: 'The two partners rarely see eye to eye on financial investments.', exampleCn: '两位合伙人在金融投资方面很少能达成一致意见。' },
    { phrase: 'long time no see', meaning: '好久不见（地道口语）', example: 'Hey Tom, long time no see! You look fantastic.', exampleCn: '嘿汤姆，好久不见！你看起来精神极了。' }
  ],
  time: [
    { phrase: 'take one\'s time', meaning: '慢慢来，不着急', example: 'Take your time reading through the contract before signing.', exampleCn: '在签字前慢慢通读合同，不用着急。' },
    { phrase: 'from time to time', meaning: '有时；不时地', example: 'I still visit my hometown from time to time to see relatives.', exampleCn: '我依然会不时回老家看望亲戚。' }
  ],
  care: [
    { phrase: 'take care of', meaning: '照顾；处理', example: 'Don\'t worry about the kids, their grandmother will take care of them.', exampleCn: '别担心孩子们，他们的奶奶会照顾好他们的。' },
    { phrase: 'care for', meaning: '喜欢；愿意', example: 'Would you care for another cup of hot chamomile tea?', exampleCn: '您想再来一杯热洋甘菊茶吗？' }
  ],
  succeed: [
    { phrase: 'succeed in doing sth.', meaning: '成功做到某事', example: 'After months of hard work, they succeeded in launching the satellite.', exampleCn: '经过数月的艰苦努力，他们成功发射了这颗卫星。' },
    { phrase: 'key to success', meaning: '成功的关键秘诀', example: 'Continuous learning is the most reliable key to professional success.', exampleCn: '持续不断地学习是职业生涯成功最可靠的关键。' }
  ],
  decide: [
    { phrase: 'decide on', meaning: '选定；决定', example: 'After careful thought, she decided on majoring in data science.', exampleCn: '深思熟虑之后，她决定主修数据科学专业。' },
    { phrase: 'make up one\'s mind', meaning: '下定决心', example: 'He made up his mind to start his own creative design studio.', exampleCn: '他下定决心要开办属于自己的创意设计工作室。' }
  ],
  help: [
    { phrase: 'can\'t help doing', meaning: '忍不住做某事', example: 'I couldn\'t help smiling when I saw the cute puppy playing.', exampleCn: '看到那只可爱的小狗在玩耍，我忍不住笑了起来。' },
    { phrase: 'help sb. out', meaning: '帮助某人摆脱困境', example: 'Thanks for lending me the money to help me out of this bind.', exampleCn: '多谢你借钱给我，帮我摆脱了这次困境。' }
  ],
  think: [
    { phrase: 'think outside the box', meaning: '跳出固有思维模式', example: 'To solve novel challenges, we must think outside the box.', exampleCn: '要解决前所未有的挑战，我们必须跳出固有思维框架。' },
    { phrase: 'think twice', meaning: '三思而后行', example: 'You had better think twice before making such an impulsive decision.', exampleCn: '在做出如此冲动的决定之前，你最好三思而后行。' }
  ]
};

/**
 * 智能判断句子所属情境主题
 */
function detectTheme(cleanWords: string[]): string {
  const text = cleanWords.join(' ');
  if (/flight|airport|plane|luggage|bag|hotel|vacation|trip|travel|ticket|beach|mountain|paris|london|holiday/.test(text)) {
    return 'travel';
  }
  if (/job|office|meeting|manager|client|project|interview|business|budget|salary|company|work/.test(text)) {
    return 'work';
  }
  if (/school|teacher|student|study|exam|learn|class|book|college|library|homework|lesson/.test(text)) {
    return 'study';
  }
  if (/weather|sunny|rain|tree|river|nature|environment|garden|protect|animal|flower|sun/.test(text)) {
    return 'nature';
  }
  if (/love|happy|sad|smile|tear|afraid|hope|feel|worry|proud|heart|comfort|excited/.test(text)) {
    return 'emotion';
  }
  if (/hello|hey|see|friend|name|excuse|thank|welcome|please|talk|call|chat/.test(text)) {
    return 'social';
  }
  return 'life';
}

/**
 * 从当前句子中提取核心词
 */
function extractCoreWord(sentence: string): string {
  const words = sentence
    .toLowerCase()
    .replace(/[^a-z\s]/g, '')
    .split(/\s+/)
    .filter(w => w.length >= 3 && !STOP_WORDS.has(w));

  if (words.length === 0) return 'learn';

  // 1. 优先在已有词族库中匹配
  for (const w of words) {
    if (ROOT_FAMILIES[w]) {
      return w;
    }
  }

  // 2. 尝试还原词尾 (如 watches -> watch, needed -> need, talking -> talk)
  for (const w of words) {
    const stripped = w.replace(/(ing|ed|es|s|ly)$/, '');
    if (ROOT_FAMILIES[stripped]) {
      return stripped;
    }
  }

  // 3. 选择长度最适中且最具实义的词汇
  const sorted = [...words].sort((a, b) => b.length - a.length);
  return sorted[0];
}

/**
 * 动态根据任意句子生成专属的「串记 · 联想 · 扩展」学习模块
 */
export function generateDynamicExpansion(sentenceText: string, customExpansion?: SentenceExpansion): SentenceExpansion {
  if (customExpansion) {
    return customExpansion;
  }

  const cleanWords = sentenceText
    .toLowerCase()
    .replace(/[^a-z\s]/g, '')
    .split(/\s+/)
    .filter(Boolean);

  const coreWord = extractCoreWord(sentenceText);
  const theme = detectTheme(cleanWords);

  // 1. 动态生成词族串记
  let wordFamily = ROOT_FAMILIES[coreWord];
  if (!wordFamily) {
    // 规则构词法动态派生链
    const cap = coreWord.charAt(0).toUpperCase() + coreWord.slice(1);
    wordFamily = {
      root: `${coreWord} (${cap})`,
      chain: [
        `${coreWord} (base 核心形式)`,
        `${coreWord}ing (doing 动作/分词)`,
        `${coreWord}ed (done 过去式/状态)`,
        `${coreWord}er (n. 相关行动者)`
      ]
    };
  }

  // 2. 动态生成主题联想词群（换句主题不同，联想词必变）
  const assocPool = THEMATIC_ASSOCIATIONS[theme] || THEMATIC_ASSOCIATIONS.life;
  // 随机挑选 3-4 个主题词
  const associations = assocPool.slice(0, 4);

  // 3. 动态生成扩展短语与例句
  let extensions = COLLOCATIONS_BANK[coreWord];
  if (!extensions || extensions.length === 0) {
    // 根据上下文生成通用的高级表达句
    extensions = [
      {
        phrase: `make the most of ${coreWord}`,
        meaning: `充分利用；善用 ${coreWord}`,
        example: `We should always make the most of every learning opportunity.`,
        exampleCn: `我们应当始终充分利用每一次宝贵的学习机会。`
      },
      {
        phrase: `in relation to ${coreWord}`,
        meaning: `与...相关；关于`,
        example: `The committee raised several key questions in relation to this topic.`,
        exampleCn: `委员会就与这一议题相关的几个关键问题提出了质询。`
      }
    ];
  }

  return {
    wordFamily,
    associations,
    extensions
  };
}
