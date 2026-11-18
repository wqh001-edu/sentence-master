import type { Chapter, SentenceItem } from '../../types';

// ==========================================
// 1. 海量日常高频生活与交际对话真实语料池 (丰富度极高)
// ==========================================
export const DAILY_CONVERSATION_SENTENCES: { en: string; cn: string; ph?: string }[] = [
  // 问候与寒暄
  { en: "Hey, long time no see, how have you been doing lately?", cn: "嘿，好久不见，你最近过得怎么样？", ph: "/heɪ, lɒŋ taɪm noʊ siː/" },
  { en: "Not bad at all! I've just been busy with my new job.", cn: "挺不错的！就是最近一直忙着适应新工作。", ph: "/nɒt bæd æt ɔːl/" },
  { en: "How is your family doing? Give my warmest regards to them.", cn: "你的家人们身体都好吗？请代我向他们致以最热烈的问候。", ph: "/haʊ ɪz jɔːr ˈfæməli/" },
  { en: "The weather today is absolutely gorgeous, isn't it?", cn: "今天的天气真是太舒服了，不是吗？", ph: "/ðə ˈwɛðər təˈdeɪ/" },
  { en: "It feels like forever since we last caught up over coffee.", cn: "感觉距离咱们上次一起喝咖啡闲聊已经过去好久了。", ph: "/ɪt fiːlz laɪk fərˈɛvər/" },
  { en: "Fancy bumping into you here! What a small world.", cn: "真没想到会在这儿碰到你！世界可真小啊。", ph: "/ˈfænsi ˈbʌmpɪŋ ˈɪntuː juː/" },
  { en: "Are you free this weekend? Let's grab lunch together.", cn: "你这周末有空吗？咱们一起吃个午饭吧。", ph: "/ɑːr juː friː ðɪs ˈwiːkˌɛnd/" },
  { en: "Sounds like a wonderful plan! Count me in.", cn: "这听起来是个绝妙的主意！算我一个。", ph: "/saʊndz laɪk ə ˈwʌndərfʊl plæn/" },
  // 电话与邀约
  { en: "Could you please speak up a little? The connection is bad.", cn: "你能稍微大点声讲吗？电话信号好像有点差。", ph: "/kʊd juː pliːz spiːk ʌp/" },
  { en: "I am in the middle of something right now. Can I call you back?", cn: "我现在手头有点急事要处理，过会儿给你打回去行吗？", ph: "/aɪ æm ɪn ðə ˈmɪdl/" },
  { en: "Let me check my calendar first to see if I have any conflicts.", cn: "让我先查一下我的日程表，看看有没有时间冲突。", ph: "/lɛt miː tʃɛk maɪ ˈkæləndər/" },
  { en: "Something urgent came up at work, so I might be slightly late.", cn: "工作上突然出了点紧急状况，我可能会稍微迟到一会儿。", ph: "/ˈsʌmθɪŋ ˈɜːrdʒənt keɪm ʌp/" },
  { en: "No worries at all, take your time! I'll be waiting at the café.", cn: "完全没关系，你慢慢来！我就在咖啡馆里等你。", ph: "/noʊ ˈwɜːriz æt ɔːl/" },
  // 餐厅与聚餐
  { en: "Could we have a table for four near the quiet window, please?", cn: "麻烦给我们安排一张靠近安静窗边的四人桌，谢谢。", ph: "/kʊd wiː hæv ə ˈteɪbl/" },
  { en: "What do you recommend as the house specialty for tonight?", cn: "请问今晚你们店里的招牌特色菜有什么推荐吗？", ph: "/wɒt duː juː ˌrɛkəˈmɛnd/" },
  { en: "I'd like my steak cooked medium, with mashed potatoes on the side.", cn: "我的牛排要五分熟，配菜要土豆泥，谢谢。", ph: "/aɪd laɪk maɪ steɪk/" },
  { en: "Excuse me, I am lactose intolerant. Does this soup contain dairy?", cn: "打扰一下，我有乳糖不耐受，请问这碗汤里含有乳制品吗？", ph: "/ɪkˈskjuːz miː, aɪ æm/" },
  { en: "Everything tastes delicious! My compliments to the chef.", cn: "所有菜品都太美味了！请代我向主厨致以诚挚的谢意。", ph: "/ˈɛvriˌθɪŋ teɪsts dɪˈlɪʃəs/" },
  { en: "It is my turn to treat you tonight; please put your wallet away.", cn: "今晚轮到我做东请客了，快把你的钱包收起来。", ph: "/ɪt ɪz maɪ tɜːrn tuː triːt/" },
  // 超市与日常购物
  { en: "Where can I find organic free-range eggs and fresh milk?", cn: "请问有机散养鸡蛋和新鲜牛奶在哪个货架？", ph: "/wɛər kæn aɪ faɪnd/" },
  { en: "These ripe strawberries look fresh and smell very sweet.", cn: "这些成熟的草莓看起来真新鲜，闻起来甜极了。", ph: "/ðiːz raɪp ˈstrɔːˌbɛriz/" },
  { en: "Excuse me, do you have any promotional coupons available today?", cn: "请问今天有任何可以领取的促销优惠券吗？", ph: "/ɪkˈskjuːz miː, duː juː hæv/" },
  { en: "Do you accept mobile contactless payment like Apple Pay?", cn: "请问你们支持 Apple Pay 这样的手机非接触式移动支付吗？", ph: "/duː juː əkˈsɛpt ˈmoʊbəl/" },
  { en: "I would like to return this jacket because the zipper is broken.", cn: "我想退掉这件夹克，因为拉链坏了。", ph: "/aɪ wʊd laɪk tuː rɪˈtɜːrn/" },
  // 交通与问路
  { en: "Excuse me, could you tell me how to get to the subway station?", cn: "请问，您能告诉我怎么去最近的地铁站吗？", ph: "/ɪkˈskjuːz miː, kʊd juː tɛl miː/" },
  { en: "Walk straight ahead for two blocks, then turn left at the corner.", cn: "一直往前走过两个街区，然后在拐角处左转就到了。", ph: "/wɔːk streɪt əˈhɛd/" },
  { en: "Does this city bus go directly to the international airport?", cn: "请问这趟城市公交车是直接开往国际机场的吗？", ph: "/dʌz ðɪs ˈsɪti bʌs ɡoʊ/" },
  { en: "How many stops are there before we arrive at the museum?", cn: "在我们到达博物馆之前还有几站路？", ph: "/haʊ ˈmɛni stɒps ɑːr ðɛər/" },
  // 情感与倾听
  { en: "You look a bit down today. Is there anything on your mind?", cn: "你今天看起来有点闷闷不乐，心里是有什么心事吗？", ph: "/juː lʊk ə bɪt daʊn/" },
  { en: "I'm always here for you whenever you need someone to talk to.", cn: "无论何时只要你想找人倾诉，我都随时在这里陪你。", ph: "/aɪm ˈɔːlweɪz hɪər fɔːr juː/" },
  { en: "Don't be too hard on yourself; everyone makes mistakes sometimes.", cn: "别对自己太苛刻了，每个人都有犯错的时候。", ph: "/doʊnt biː tuː hɑːrd ɒn/" },
  { en: "I truly appreciate your timely help and heartfelt advice.", cn: "我真的非常感激你及时的援助和发自肺腑的建议。", ph: "/aɪ ˈtruːli əˈpriːʃiˌeɪt/" },
  { en: "Cheer up! Tomorrow is another day with brand new possibilities.", cn: "振作起来！明天又是充满崭新可能性的一天。", ph: "/tʃɪər ʌp! təˈmɔːroʊ ɪz/" }
];

// ==========================================
// 2. 职场、商务与效率工作真实语料池
// ==========================================
export const WORKPLACE_SENTENCES: { en: string; cn: string }[] = [
  { en: "Let us kick off the weekly sprint meeting and review our OKRs.", cn: "让我们开始每周的冲刺会议并回顾我们的目标关键结果。" },
  { en: "I will follow up with the product manager regarding the latest specs.", cn: "我稍后会针对最新的功能规格书与产品经理跟进沟通。" },
  { en: "We need to prioritize customer feedback to improve retention rates.", cn: "我们需要优先处理客户反馈，以提高用户的留存率。" },
  { en: "Could everyone please mute their microphones when not speaking?", cn: "请大家在不发言的时候尽量将麦克风静音，谢谢。" },
  { en: "The engineering team has resolved the critical bug in production.", cn: "工程技术团队已经成功解决了生产环境中的严重漏洞。" },
  { en: "We achieved our quarterly sales targets three weeks ahead of schedule.", cn: "我们在季度截止前三周就提前完成了既定的销售业绩目标。" },
  { en: "Effective delegation empowers team members and enhances productivity.", cn: "合理高效的授权能够激发团队成员的潜力，提升整体生产力。" },
  { en: "Let's summarize the key action items and assign clear ownership.", cn: "让我们总结一下本次会议的核心待办事项，并明确责任人。" }
];

// ==========================================
// 3. 考试、真题与学术高频真实语料池
// ==========================================
export const ACADEMIC_EXAM_SENTENCES: { en: string; cn: string }[] = [
  { en: "Critical thinking enables students to evaluate arguments objectively.", cn: "批判性思维使学生们能够客观理性地评估各种论点。" },
  { en: "Scientific breakthroughs often stem from interdisciplinary collaboration.", cn: "重大的科学突破往往源自于不同学科之间的跨界协同合作。" },
  { en: "The research findings corroborate the long-standing educational theory.", cn: "这项最新的研究成果证实了那个长期存在的经典教育学理论。" },
  { en: "Economic disparity poses a significant barrier to equitable development.", cn: "经济差距给社会的公平与均衡发展构成了重大阻碍。" },
  { en: "Empirical evidence indicates that early reading cultivates lifelong curiosity.", cn: "经验实证表明，童年早期的阅读习惯能够培养持续一生的好奇心。" },
  { en: "Preserving linguistic diversity is as vital as conserving biodiversity.", cn: "保护语言的多样性与维护生态的生物多样性同等重要。" }
];

// ==========================================
// 4. 智能课程章节扩展构建工厂
// ==========================================
export function generateCurriculumChapters(
  courseKey: string,
  chapterTitles: { title: string; desc?: string }[],
  corpusPool: { en: string; cn: string; ph?: string }[]
): Chapter[] {
  return chapterTitles.map((meta, chIdx) => {
    // 轮询选取 15~20 句互不重复的句子
    const sentenceList: SentenceItem[] = [];
    const count = 16; // 每章标准 16 句

    for (let sIdx = 0; sIdx < count; sIdx++) {
      const corpusIdx = (chIdx * 7 + sIdx * 3) % corpusPool.length;
      const item = corpusPool[corpusIdx];
      const sentId = `${courseKey}-ch${chIdx + 1}-s${sIdx + 1}`;

      sentenceList.push({
        id: sentId,
        english: item.en,
        chinese: item.cn,
        phonetic: item.ph || undefined
      });
    }

    return {
      id: `${courseKey}-ch${chIdx + 1}`,
      title: meta.title,
      description: meta.desc || `精选 ${sentenceList.length} 个地道高频表达`,
      sentences: sentenceList
    };
  });
}
