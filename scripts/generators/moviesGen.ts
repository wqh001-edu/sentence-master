import { buildCourse, type RawCourse } from './common';
import type { CoursePackage } from '../../src/types/index';

export function getMoviesCourses(): CoursePackage[] {
  // 1. 老友记
  const rawFriends: RawCourse = {
    id: 'course-mov-friends',
    title: '《老友记》(Friends) · 地道纽约日常口语精选 (10章全集)',
    category: 'movies',
    categoryName: '影视英语',
    coverGradient: 'from-amber-500 via-orange-600 to-red-700',
    icon: '☕',
    description: '六位老友十年嬉笑怒骂，最真实、最鲜活的美国年轻人高频生活口语与地道幽默。',
    difficulty: '初级 A2',
    tags: ['美剧天花板', '老友记', '地道口语', '幽默诙谐'],
    chapters: [
      {
        title: '第 1 季 · Central Perk 咖啡馆红沙发闲聊',
        description: '逃婚的瑞秋闯入咖啡馆，六人组十年传奇正式启航。',
        sentences: [
          { en: "Welcome to the real world! It sucks. You're gonna love it.", cn: "欢迎来到现实世界！它很糟糕，但你会爱上它的。" },
          { en: "How you doin'?", cn: "你好啊？/ 最近怎么样？(乔伊搭讪名句)" },
          { en: "There's nothing to tell! He's just some guy I work with.", cn: "真的没什么好说的！他只是我公司的一个普通男同事。" },
          { en: "I don't want to be single, okay? I just want to be married again!", cn: "我不想单身，好吗？我只想再次步入婚姻！" },
          { en: "And I just want a million dollars!", cn: "那我还想要一百万美元呢！" },
          { en: "You can't live off your parents your whole life.", cn: "你总不能一辈子都靠你的父母生活吧。" },
          { en: "This is the first time I've ever made coffee in my life.", cn: "这是我这辈子第一次亲手煮咖啡。" },
          { en: "You got me through a lot of hard times in college.", cn: "大学那会儿多亏有你陪我度过了好多艰难时刻。" },
          { en: "I can't believe what I'm hearing right now.", cn: "我简直不敢相信我现在耳朵里听到的这些话。" },
          { en: "Does he have a hump? A hump and a hairpiece?", cn: "他驼背吗？长了个驼峰还戴着假发？" },
          { en: "Stop hitting on her! It's her wedding day.", cn: "别再搭讪她了！今天可是她结婚的大日子。" },
          { en: "I have this recurring dream where I am in school naked.", cn: "我老是做一个重复的梦，梦见自己光着身子在学校上课。" },
          { en: "It feels like someone reached down my throat and pulled out my heart.", cn: "那种感觉就像有人伸手卡住我的喉咙，硬生生把我的心给掏了出来。" },
          { en: "You are an independent woman now, Rachel.", cn: "瑞秋，你现在可是一个独立自主的女性了。" },
          { en: "I'll be there for you, because you're there for me too.", cn: "我会陪伴在你身边，因为你也始终陪伴着我。" }
        ]
      },
      {
        title: '第 2 季 · 莫妮卡的强迫症与厨房厨艺',
        description: '洁癖大厨莫妮卡的严苛家规与温暖牌美食。',
        sentences: [
          { en: "I need you to be careful with the new wooden table.", cn: "我对你们只有一个要求：千万小心我新买的这张木桌。" },
          { en: "If you spill anything on the carpet, you clean it immediately.", cn: "要是把任何东西洒在地毯上，你必须立刻擦干净。" },
          { en: "Rules help control the fun!", cn: "有严谨的规则才能掌控快乐！" },
          { en: "I am not a control freak; I just like things organized.", cn: "我才不是什么控制狂，我只是喜欢所有东西井井有条。" },
          { en: "I made freshly baked chocolate chip cookies for everyone.", cn: "我给大家烤了刚出炉的巧克力碎曲奇饼干。" },
          { en: "Do not put your feet on the coffee table, please.", cn: "请千万别把你的脚大摇大摆翘在咖啡茶几上。" },
          { en: "Cooking is the only way I know how to show love.", cn: "下厨烹饪是我表达爱意最擅长的方式。" },
          { en: "You don't understand how much pressure I am under.", cn: "你根本无法体会我现在承受着多么巨大的压力。" },
          { en: "Everything in this kitchen has its designated place.", cn: "这个厨房里的每一件器具都有它专属的指定位置。" },
          { en: "Could you please use a coaster under that glass?", cn: "请问你能在那只玻璃杯底下垫一张杯垫吗？" },
          { en: "I stay up late scrubbing the grout between bathroom tiles.", cn: "我大半夜不睡觉，蹲在地上擦浴室瓷砖之间的缝隙。" },
          { en: "My parents are coming over, so everything must be flawless.", cn: "我爸妈待会儿要过来，所以屋里的一切必须无可挑剔。" },
          { en: "Nobody appreciates how hard I work to keep this place clean.", cn: "根本没有人懂得欣赏我为了维持这里的整洁付出了多少心血。" },
          { en: "Taste this sauce and tell me if it needs more garlic.", cn: "尝一口这个酱汁，告诉我需不需要再多加点大蒜。" },
          { en: "You are the most stubborn sister in the world.", cn: "你真是全天底下最固执倔强的妹妹。" }
        ]
      },
      {
        title: '第 3 季 · 乔伊的试镜经历与演员梦想',
        description: '大胃王兼百折不挠的百老汇肥皂剧演员乔伊。',
        sentences: [
          { en: "Joey doesn't share food!", cn: "乔伊从不和别人分享食物！(经典名场面)" },
          { en: "I got an audition for a daytime soap opera tomorrow.", cn: "我明天有一场日间肥皂剧的试镜选拔。" },
          { en: "Acting is not just memorizing lines; it's living the part.", cn: "演戏不仅仅是背背台词，而是真正活在那个角色里。" },
          { en: "Can I have some of those French fries on your plate?", cn: "我能尝两根你盘子里炸得金黄的薯条吗？" },
          { en: "You know you love me, so don't even try to deny it.", cn: "你知道你心里是喜欢我的，所以别试图否认了。" },
          { en: "I need to practice my dramatic angry face in the mirror.", cn: "我得在镜子面前好好练习一下我充满戏剧张力的愤怒表情。" },
          { en: "My agent said they are looking for a handsome Italian doctor.", cn: "我的经纪人说他们正在物色一位英俊的意大利裔男医生。" },
          { en: "Pizza is good any time of day or night.", cn: "不管白天还是黑夜，披萨随时都是最棒的美食。" },
          { en: "I don't care about the money, I just love performing.", cn: "我根本不在乎能赚多少钱，我只是发自内心地热爱表演。" },
          { en: "Why does everyone else make life look so simple?", cn: "为什么其他所有人都能把生活过得看起来那么轻松？" },
          { en: "You are the best roommate a guy could ever ask for.", cn: "你是一个男人所能奢求的最好的室友了。" },
          { en: "I forgot my line right in front of the casting director.", cn: "我在选角导演面前突然把准备好的台词忘得一干二净。" },
          { en: "Always look on the bright side, no matter what happens.", cn: "无论发生什么事，永远要看向事情光明的一面。" },
          { en: "Can we order two large meat lover pizzas right now?", cn: "咱们现在能立刻点两份大号肉食者大满贯披萨吗？" },
          { en: "Never give up on your passion, even when it gets tough.", cn: "永远不要放弃你的热爱，哪怕前路极其艰难坎坷。" }
        ]
      },
      {
        title: '第 4 季 · 钱德勒式冷幽默与标志性讽刺',
        description: '毒舌暖男钱德勒用笑声包裹防御的经典独白。',
        sentences: [
          { en: "I'm not great at the advice. Can I interest you in a sarcastic comment?", cn: "我不太擅长给建议，给你来两句讽刺冷幽默你感兴趣吗？" },
          { en: "Could I BE wearing any more clothes?", cn: "我还能再多穿几件衣服吗？(讽刺模仿经典句)" },
          { en: "I make jokes when I'm uncomfortable.", cn: "我一感到尴尬或不自在就会忍不住讲笑话。" },
          { en: "I'm hopeless and awkward and desperate for love!", cn: "我既绝望又笨拙，而且极其渴望得到真爱！" },
          { en: "Hi, I'm Chandler. I make jokes when I am terrified.", cn: "嗨，我是钱德勒。一感到害怕我就开始胡乱贫嘴。" },
          { en: "Until I was twenty-five, I thought the only response was silence.", cn: "在我二十五岁之前，我还以为对一切的唯一反应就是沉默。" },
          { en: "If I were a guy... wait, did I just say that out loud?", cn: "要是我也是个男的...等等，我刚才大声把心里话说出来了？" },
          { en: "What is wrong with me? Don't answer that question.", cn: "我到底是怎么了？先别急着回答这个问题。" },
          { en: "I am glad we are having this completely bizarre conversation.", cn: "我真高兴咱们能进行这场彻底荒诞古怪的对话。" },
          { en: "You don't need to yell at me; I'm already fragile enough.", cn: "你用不着冲我大喊大叫，我幼小的心灵已经足够脆弱了。" },
          { en: "Commitment is a terrifying word for people like me.", cn: "对于像我这种人来说，‘长相厮守的承诺’简直是个可怕的词汇。" },
          { en: "Can we skip to the part where everything works out?", cn: "咱们能不能直接快进到大团圆结局那个部分？" },
          { en: "I don't know what my actual job title is at work.", cn: "在公司上班这么多年，我甚至不知道我的具体职称到底叫什么。" },
          { en: "You are the only person who can tolerate my eccentricities.", cn: "你是全天下唯一一个能够容忍我这堆古怪脾气的人。" },
          { en: "Sometimes laughter is the only shield we have left.", cn: "有时候，幽默的笑声是我们抵御外界仅存的盾牌了。" }
        ]
      },
      {
        title: '第 5 季 · 罗斯古生物学博物馆日常笑料',
        description: '恐龙学者罗斯·盖勒的严肃较真与感情波折。',
        sentences: [
          { en: "Pivot! Pivot! Pivot!", cn: "转弯！抬高角度！转弯！(搬沙发名场面)" },
          { en: "We were on a break!", cn: "我们当时明明已经在协议冷战分手了！(世纪争论)" },
          { en: "I am a paleontologist, which means I study dinosaurs.", cn: "我是一名古生物学家，这意味着我整天都在研究恐龙化石。" },
          { en: "Someone at work ate my Thanksgiving leftover sandwich with the moist maker.", cn: "单位里有人偷吃了我带去的热带夹心感恩节火鸡三明治。" },
          { en: "I have been in love with Rachel since the ninth grade.", cn: "其实从初中九年级开始，我就一直深深暗恋着瑞秋了。" },
          { en: "Why does science have to be so difficult for people to grasp?", cn: "为什么科学原理对于普通大众来说就那么难以理解呢？" },
          { en: "I am fine! Totally fine! Everything is absolutely fine!", cn: "我好得很！完全没事！一切都好得不能再好了！" },
          { en: "Do not touch the fossil display; it took three years to assemble.", cn: "千万别碰那个恐龙化石展柜，足足花了我三年时间才拼装好。" },
          { en: "I am getting married again, and this time it will last.", cn: "我要再次结婚了，而且这一次我们一定会白头偕老。" },
          { en: "Can we talk about something other than my romantic disasters?", cn: "咱们能聊点别的吗？别老揪着我那些糟糕透顶的情史不放。" },
          { en: "My sister has been competitive since the day she was born.", cn: "我这个亲妹妹，从她出生的第一天起骨子里就充满了胜负欲。" },
          { en: "Accuracy is the foundation of any respectable scientific research.", cn: "严谨求实是任何令人尊重的科学研究最根本的基石。" },
          { en: "You don't just throw away a ten-year friendship over an argument.", cn: "你总不能因为一场口角争执，就把十年的深厚友谊轻易抛弃吧。" },
          { en: "She's your lobster. It's a known fact that lobsters mate for life.", cn: "她是你的命中注定。众所周知龙虾坠入爱河就会相伴终生。" },
          { en: "I will never lose hope when it comes to true love.", cn: "只要涉及到真正的挚爱，我永远都不会放弃希望。" }
        ]
      },
      {
        title: '第 6 季 · 菲比吉他弹唱与奇特灵感',
        description: '古灵精怪的大自然女孩菲比带来的纯粹快乐。',
        sentences: [
          { en: "Smelly cat, smelly cat, what are they feeding you?", cn: "臭臭猫，臭臭猫，他们到底在喂你吃什么？(传世神曲)" },
          { en: "They don't know that we know they know we know!", cn: "他们不知道我们已经知道他们知道我们知道！(经典绕口令)" },
          { en: "I don't even have a 'pla'!", cn: "我甚至连个'计'都还没有，更别说完整的'计划'了！" },
          { en: "My mother told me that tree leaves whisper secrets at night.", cn: "我妈妈曾经告诉我，深夜里树上的叶子都在互诉悄悄话。" },
          { en: "I will play my acoustic guitar in front of the coffee shop.", cn: "我要在咖啡馆门前的台阶上弹着我的木吉他卖唱。" },
          { en: "You have very negative aura surrounding you today.", cn: "你今天整个人周身都笼罩着一股极其负能量的气场。" },
          { en: "Animals understand compassion far better than human beings do.", cn: "在感知同理心这方面，动物往往比人类纯粹深刻得多。" },
          { en: "I made this bizarre painting out of discarded mannequin parts.", cn: "我用别人丢弃的服装假人模特零件组装成了这幅奇特装置画。" },
          { en: "You should follow your intuition instead of overthinking logic.", cn: "你应该跟随内心的敏锐直觉，而不是把大脑过度陷在逻辑里。" },
          { en: "Nothing in this magical universe happens completely by coincidence.", cn: "在这个奇妙的宇宙中，没有任何事情是纯粹出于偶然巧合的。" },
          { en: "I might be weird, but at least I am completely authentic.", cn: "我也许在外人看来古灵精怪，但至少我活得完完全全坦率真诚。" },
          { en: "Let's all hold hands and send positive energy to the universe.", cn: "让我们大家手牵着手，一起向浩瀚的宇宙输送积极正念吧。" },
          { en: "If you want the rainbow, you have to tolerate the heavy rain.", cn: "如果你渴望看见绚丽的彩虹，你就必须经受得住漫天倾盆大雨。" },
          { en: "I am writing a brand new folk song about street pigeons.", cn: "我正在创作一首全新的民谣歌曲，主题是关于街头觅食的鸽子。" },
          { en: "Love is the only song that everyone in the room knows.", cn: "爱是整个房间里唯一一首每个人都会哼唱的旋律。" }
        ]
      },
      {
        title: '第 7 季 · 瑞秋时尚圈打拼与职场升职',
        description: '从娇生惯养的大小姐到雷夫·罗伦时尚总监的蜕变。',
        sentences: [
          { en: "I am tired of everyone treating me like an empty shoe box.", cn: "我受够了身边所有人都把我当成一个徒有其表的空鞋盒看待。" },
          { en: "I got hired as an assistant buyer at Bloomingdale's!", cn: "我被布鲁明戴尔百货正式录用为时尚采购助理了！" },
          { en: "Fashion is not just clothes; it is how you present your spirit.", cn: "时尚不仅仅是身上的衣裳，它是你向世界展示精神风貌的方式。" },
          { en: "I poured coffee for two straight years to get this breakthrough.", cn: "为了等到今天这个职场突破，我老老实实端了整整两年的咖啡。" },
          { en: "Do you like this lavender silk blouse for the interview?", cn: "你觉得这件薰衣草紫色的丝绸衬衫适合穿去参加面试吗？" },
          { en: "Hard work finally pays off if you stay persistent enough.", cn: "只要你足够坚持不懈，付出的辛勤汗水终究会得到丰厚回报。" },
          { en: "I have to prepare the quarterly runway presentation by Monday.", cn: "我必须在下周一前准备好下季度时装秀的走秀方案幻灯片。" },
          { en: "Never let anyone make you feel small in a conference room.", cn: "在会议室里，永远别让任何人有贬低你或让你感到自卑的机会。" },
          { en: "I made my own money, and I bought my own shoes.", cn: "我自己靠双手赚到了钱，我自己买下了梦寐以求的高跟鞋。" },
          { en: "Balance between a bustling career and genuine personal life is hard.", cn: "在繁忙飞奔的事业与真实温暖的个人生活之间保持平衡实属不易。" },
          { en: "Paris offered me an incredible dream job in high fashion.", cn: "巴黎时尚总部向我抛出了一份令人难以置信的高定梦想职位。" },
          { en: "My heart tells me that my real home is here in New York.", cn: "但我内心的声音告诉我，我真正的归宿就在纽约这座城市。" },
          { en: "Friends are the family that you choose for yourself.", cn: "朋友，就是你自己亲自为自己挑选的家人。" },
          { en: "I got off the plane!", cn: "我从去巴黎的飞机上走下来了！(全剧高泪点)" },
          { en: "I don't want to live without you ever again.", cn: "往后的余生里，我再也不想过没有你在身边的日子了。" }
        ]
      },
      {
        title: '第 8 季 · 感恩节橄榄球赛与吃火鸡插曲',
        description: '一年一度充满火药味与欢笑的感恩节保留节目。',
        sentences: [
          { en: "Thanksgiving without delicious food is not a real holiday at all.", cn: "没有一桌丰盛可口的美食，感恩节根本算不上真正的节日。" },
          { en: "Who won the legendary Geller Cup football trophy last year?", cn: "去年那场激烈的盖勒杯家族橄榄球争夺赛到底是谁赢了？" },
          { en: "I baked a traditional pumpkin pie with a hint of cinnamon.", cn: "我亲手烘焙了一个带有淡淡肉桂香气的传统南瓜派。" },
          { en: "Joey finished an entire nineteen-pound roast turkey by himself.", cn: "乔伊一个人竟然把整只足足十九磅重的烤火鸡全吃光了。" },
          { en: "We are all thankful for having each other through thick and thin.", cn: "我们由衷感恩能够彼此相守，风雨同舟携手走过岁岁年年。" },
          { en: "Touchdown! Monica scored against the boys once again.", cn: "达阵得分！莫妮卡再一次在球场上把男生们给打得落花流水。" },
          { en: "Put the turkey on your head to cheer me up, please.", cn: "求求你，把那只大火鸡套在头上逗我开心一下好不好？" },
          { en: "Family holidays are always chaotic, loud, and full of warmth.", cn: "家庭聚会永远都是乱成一团、吵吵闹闹，但也饱含无尽温情。" },
          { en: "Pass the homemade cranberry sauce down to this end of the table.", cn: "请把那碗自制的蔓越莓果酱递到餐桌这头来，谢谢。" },
          { en: "I burned the sweet potatoes because I was too competitive.", cn: "因为我一心光顾着在橄榄球场上争胜负，把烤箱里的红薯给烤糊了。" },
          { en: "Nothing brings old friends closer together than a holiday tradition.", cn: "没有什么能比一项温存的节日传统更能让老朋友们紧紧依偎了。" },
          { en: "Let us go around the table and each name what we appreciate most.", cn: "让我们围着餐桌转一圈，每个人都说一件自己最心怀感激的事。" },
          { en: "I appreciate that you never let me face darkness alone.", cn: "我最感激的是，你从未让我一个人孤零零地去面对黑暗。" },
          { en: "Can we have leftover cold turkey sandwiches for the next three days?", cn: "接下来整整三天咱们都能顿顿吃剩下的冷火鸡三明治了吗？" },
          { en: "Every Thanksgiving with you six is an unforgettable memory.", cn: "和你们六个人度过的每一个感恩节，都是终生难忘的美好回忆。" }
        ]
      },
      {
        title: '第 9 季 · 伦敦婚礼与跨国旅行冒险',
        description: '大本钟、双层红巴士与啼笑皆非的婚礼意外。',
        sentences: [
          { en: "London, baby! We are finally here in the United Kingdom!", cn: "伦敦，宝贝！我们终于踏上英国这片土地了！(乔伊欢呼)" },
          { en: "Look at the double-decker red buses crossing Tower Bridge.", cn: "快看那些穿行在伦敦塔桥上的红色标志性双层大巴车。" },
          { en: "Mind the gap between the train platform and the carriage.", cn: "请注意列车车厢与站台之间的空隙。(伦敦地铁名广播)" },
          { en: "I take thee, Rachel... wait, I meant Emily!", cn: "我愿意娶你，瑞秋...等等，我本来想说的是艾米莉！(名场面)" },
          { en: "How could you say the wrong name at your own wedding altar?", cn: "你怎么可能在自己神圣的婚礼仪式宣誓上念错新娘的名字？" },
          { en: "Big Ben is ticking away, just like my patience today.", cn: "大本钟正在滴答作响，正如我今天逐渐消磨殆尽的耐心一样。" },
          { en: "I bought this ridiculously oversized British flag hat on the street.", cn: "我在伦敦街头的小摊上买下了这顶滑稽至极的巨幅米字旗高帽。" },
          { en: "Traveling overseas always brings out the funniest side of people.", cn: "跨国长途旅行总是能轻而易举激发出人们性格中最逗趣的一面。" },
          { en: "A cup of warm English Earl Grey tea cures any travel fatigue.", cn: "一杯温热纯正的英式格雷伯爵红茶足以驱散所有的旅途奔波疲惫。" },
          { en: "Sometimes the biggest mistakes lead to the truest awakenings.", cn: "有时候，最无可挽回的错误反而会引领人们走向最真实的心灵觉醒。" },
          { en: "We walked through Hyde Park talking about what our future holds.", cn: "我们漫步在海德公园林荫道上，畅谈着未知的未来会是何种模样。" },
          { en: "The cobblestone streets here carry hundreds of years of rich history.", cn: "这里的每一块青石板路面，都承载着数百年沉淀的厚重历史印记。" },
          { en: "Never board an airplane unless you are completely sure of your destination.", cn: "除非你心里百分之百确信自己的终点所在，否则永远不要草率登机。" },
          { en: "No matter how far we wander, we always find our way back home.", cn: "无论我们漫游流浪到多远的天涯海角，我们总能找到回家的方向。" },
          { en: "Friendship is the passport that works in every corner of the world.", cn: "真挚的友谊，就是通向世界上任何一个角落都永远有效的护照。" }
        ]
      },
      {
        title: '第 10 季 · 搬离公寓与十年的真挚告别',
        description: '紫色大门、金色猫眼相框，六位老友的温情谢幕。',
        sentences: [
          { en: "This apartment has witnessed every single milestone of our youth.", cn: "这间公寓见证了我们整个青春岁月里每一个不可磨灭的里程碑。" },
          { en: "Where should we leave our keys before we walk out the purple door?", cn: "在走出这扇紫色大门之前，我们应该把钥匙留在哪里呢？" },
          { en: "Should we get some coffee at Central Perk one last time together?", cn: "咱们要不要最后一次一起去 Central Perk 咖啡馆喝杯咖啡？" },
          { en: "Sure. Where? (Chandler's last iconic joke of the series)", cn: "当然好啊。去哪儿喝呢？(钱德勒全剧全剧终最后一句标志性冷幽默)" },
          { en: "The empty apartment echoing our footsteps feels surreal and poignant.", cn: "空荡荡的房间里回荡着我们的脚步声，让人感到恍惚而又感伤。" },
          { en: "Ten incredible years of laughter, tears, and unconditional support.", cn: "整整十年充满欢声笑语、泪水与彼此无条件支持的不可思议岁月。" },
          { en: "A new chapter is beginning for all of us with new families and homes.", cn: "随着全新家庭的建立与乔迁，我们所有人的崭新人生篇章正徐徐拉开。" },
          { en: "I promise you that nothing will ever change our bond.", cn: "我向你郑重保证，任何时光变迁都绝不可能改变我们之间的深厚羁绊。" },
          { en: "The golden picture frame around the peephole will always stay.", cn: "门镜猫眼周围那个金色的相框，将永远定格在属于我们的记忆里。" },
          { en: "Thank you for being my anchor when the world felt overwhelming.", cn: "由衷感谢你，当这整个世界让我感到不堪重负时，你始终是我的锚。" },
          { en: "We grew up together in the heart of this magnificent city.", cn: "我们在这座繁华壮丽的城市心脏地带，彼此扶持着共同长大成人。" },
          { en: "Don't cry because it is over; smile because it happened so beautifully.", cn: "不要因为落幕而哭泣；为它曾经如此美妙绝伦地发生过而微笑吧。" },
          { en: "Hold on to the lessons, the inside jokes, and the endless hugs.", cn: "紧紧握住那些受用一生的教诲、只有我们才懂的默契玩笑与拥抱。" },
          { en: "Goodbye, Apartment 20. You were the warmest home we ever knew.", cn: "再见了，20号公寓。你曾是我们此生所知晓的最温暖的港湾。" },
          { en: "I will love you guys for the rest of my life.", cn: "在我的余生里，我将永远深深地爱着你们大家。" }
        ]
      }
    ]
  };

  return [buildCourse(rawFriends)];
}
