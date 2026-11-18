import sys, os
sys.path.append(os.path.dirname(__file__))
from builder_core import build_course, save_ts_file

def generate_movies():
    courses = []

    # 1. 《老友记》(Friends)
    courses.append(build_course({
        "id": "course-mov-friends",
        "title": "《老友记》(Friends) · 地道纽约日常口语精选 (10章全集)",
        "category": "movies",
        "categoryName": "影视英语",
        "coverGradient": "from-amber-500 via-orange-600 to-red-700",
        "icon": "☕",
        "description": "六位老友十年嬉笑怒骂，最真实、最鲜活的美国年轻人高频生活口语与地道幽默。",
        "difficulty": "初级 A2",
        "tags": ["美剧天花板", "老友记", "地道口语", "幽默诙谐"]
    }, [
        {
            "title": "第 1 季 · Central Perk 咖啡馆红沙发闲聊",
            "description": "逃婚的瑞秋闯入咖啡馆，六人组十年传奇正式启航。",
            "sentences": [
                {"en": "Welcome to the real world! It sucks. You're gonna love it.", "cn": "欢迎来到现实世界！它很糟糕，但你会爱上它的。"},
                {"en": "How you doin'?", "cn": "你好啊？/ 最近怎么样？(乔伊搭讪名句)"},
                {"en": "There's nothing to tell! He's just some guy I work with.", "cn": "真的没什么好说的！他只是我公司的一个普通男同事。"},
                {"en": "I don't want to be single, okay? I just want to be married again!", "cn": "我不想单身，好吗？我只想再次步入婚姻！"},
                {"en": "And I just want a million dollars!", "cn": "那我还想要一百万美元呢！"},
                {"en": "You can't live off your parents your whole life.", "cn": "你总不能一辈子都靠你的父母生活吧。"},
                {"en": "This is the first time I've ever made coffee in my life.", "cn": "这是我这辈子第一次亲手煮咖啡。"},
                {"en": "You got me through a lot of hard times in college.", "cn": "大学那会儿多亏有你陪我度过了好多艰难时刻。"},
                {"en": "I can't believe what I'm hearing right now.", "cn": "我简直不敢相信我现在耳朵里听到的这些话。"},
                {"en": "Does he have a hump? A hump and a hairpiece?", "cn": "他驼背吗？长了个驼峰还戴着假发？"},
                {"en": "Stop hitting on her! It's her wedding day.", "cn": "别再搭讪她了！今天可是她结婚的大日子。"},
                {"en": "I have this recurring dream where I am in school naked.", "cn": "我老是做一个重复的梦，梦见自己光着身子在学校上课。"},
                {"en": "It feels like someone reached down my throat and pulled out my heart.", "cn": "那种感觉就像有人伸手卡住我的喉咙，硬生生把我的心给掏了出来。"},
                {"en": "You are an independent woman now, Rachel.", "cn": "瑞秋，你现在可是一个独立自主的女性了。"},
                {"en": "I'll be there for you, because you're there for me too.", "cn": "我会陪伴在你身边，因为你也始终陪伴着我。"}
            ]
        },
        {
            "title": "第 2 季 · 莫妮卡的强迫症与厨房厨艺",
            "description": "洁癖大厨莫妮卡的严苛家规与温暖牌美食。",
            "sentences": [
                {"en": "I need you to be careful with the new wooden table.", "cn": "我对你们只有一个要求：千万小心我新买的这张木桌。"},
                {"en": "If you spill anything on the carpet, you clean it immediately.", "cn": "要是把任何东西洒在地毯上，你必须立刻擦干净。"},
                {"en": "Rules help control the fun!", "cn": "有严谨的规则才能掌控快乐！"},
                {"en": "I am not a control freak; I just like things organized.", "cn": "我才不是什么控制狂，我只是喜欢所有东西井井有条。"},
                {"en": "I made freshly baked chocolate chip cookies for everyone.", "cn": "我给大家烤了刚出炉的巧克力碎曲奇饼干。"},
                {"en": "Do not put your feet on the coffee table, please.", "cn": "请千万别把你的脚大摇大摆翘在咖啡茶几上。"},
                {"en": "Cooking is the only way I know how to show love.", "cn": "下厨烹饪是我表达爱意最擅长的方式。"},
                {"en": "You don't understand how much pressure I am under.", "cn": "你根本无法体会我现在承受着多么巨大的压力。"},
                {"en": "Everything in this kitchen has its designated place.", "cn": "这个厨房里的每一件器具都有它专属的指定位置。"},
                {"en": "Could you please use a coaster under that glass?", "cn": "请问你能在那只玻璃杯底下垫一张杯垫吗？"},
                {"en": "I stay up late scrubbing the grout between bathroom tiles.", "cn": "我大半夜不睡觉，蹲在地上擦浴室瓷砖之间的缝隙。"},
                {"en": "My parents are coming over, so everything must be flawless.", "cn": "我爸妈待会儿要过来，所以屋里的一切必须无可挑剔。"},
                {"en": "Nobody appreciates how hard I work to keep this place clean.", "cn": "根本没有人懂得欣赏我为了维持这里的整洁付出了多少心血。"},
                {"en": "Taste this sauce and tell me if it needs more garlic.", "cn": "尝一口这个酱汁，告诉我需不需要再多加点大蒜。"},
                {"en": "You are the most stubborn sister in the world.", "cn": "你真是全天底下最固执倔强的妹妹。"}
            ]
        },
        {
            "title": "第 3 季 · 乔伊的试镜经历与演员梦想",
            "description": "大胃王兼百折不挠的百老汇肥皂剧演员乔伊。",
            "sentences": [
                {"en": "Joey doesn't share food!", "cn": "乔伊从不和别人分享食物！(经典名场面)"},
                {"en": "I got an audition for a daytime soap opera tomorrow.", "cn": "我明天有一场日间肥皂剧的试镜选拔。"},
                {"en": "Acting is not just memorizing lines; it's living the part.", "cn": "演戏不仅仅是背背台词，而是真正活在那个角色里。"},
                {"en": "Can I have some of those French fries on your plate?", "cn": "我能尝两根你盘子里炸得金黄的薯条吗？"},
                {"en": "You know you love me, so don't even try to deny it.", "cn": "你知道你心里是喜欢我的，所以别试图否认了。"},
                {"en": "I need to practice my dramatic angry face in the mirror.", "cn": "我得在镜子面前好好练习一下我充满戏剧张力的愤怒表情。"},
                {"en": "My agent said they are looking for a handsome Italian doctor.", "cn": "我的经纪人说他们正在物色一位英俊的意大利裔男医生。"},
                {"en": "Pizza is good any time of day or night.", "cn": "不管白天还是黑夜，披萨随时都是最棒的美食。"},
                {"en": "I don't care about the money, I just love performing.", "cn": "我根本不在乎能赚多少钱，我只是发自内心地热爱表演。"},
                {"en": "Why does everyone else make life look so simple?", "cn": "为什么其他所有人都能把生活过得看起来那么轻松？"},
                {"en": "You are the best roommate a guy could ever ask for.", "cn": "你是一个男人所能奢求的最好的室友了。"},
                {"en": "I forgot my line right in front of the casting director.", "cn": "我在选角导演面前突然把准备好的台词忘得一干二净。"},
                {"en": "Always look on the bright side, no matter what happens.", "cn": "无论发生什么事，永远要看向事情光明的一面。"},
                {"en": "Can we order two large meat lover pizzas right now?", "cn": "咱们现在能立刻点两份大号肉食者大满贯披萨吗？"},
                {"en": "Never give up on your passion, even when it gets tough.", "cn": "永远不要放弃你的热爱，哪怕前路极其艰难坎坷。"}
            ]
        },
        {
            "title": "第 4 季 · 钱德勒式冷幽默与标志性讽刺",
            "description": "毒舌暖男钱德勒用笑声包裹防御的经典独白。",
            "sentences": [
                {"en": "I'm not great at the advice. Can I interest you in a sarcastic comment?", "cn": "我不太擅长给建议，给你来两句讽刺冷幽默你感兴趣吗？"},
                {"en": "Could I BE wearing any more clothes?", "cn": "我还能再多穿几件衣服吗？(讽刺模仿经典句)"},
                {"en": "I make jokes when I'm uncomfortable.", "cn": "我一感到尴尬或不自在就会忍不住讲笑话。"},
                {"en": "I'm hopeless and awkward and desperate for love!", "cn": "我既绝望又笨拙，而且极其渴望得到真爱！"},
                {"en": "Hi, I'm Chandler. I make jokes when I am terrified.", "cn": "嗨，我是钱德勒。一感到害怕我就开始胡乱贫嘴。"},
                {"en": "Until I was twenty-five, I thought the only response was silence.", "cn": "在我二十五岁之前，我还以为对一切的唯一反应就是沉默。"},
                {"en": "If I were a guy... wait, did I just say that out loud?", "cn": "要是我也是个男的...等等，我刚才大声把心里话说出来了？"},
                {"en": "What is wrong with me? Don't answer that question.", "cn": "我到底是怎么了？先别急着回答这个问题。"},
                {"en": "I am glad we are having this completely bizarre conversation.", "cn": "我真高兴咱们能进行这场彻底荒诞古怪的对话。"},
                {"en": "You don't need to yell at me; I'm already fragile enough.", "cn": "你用不着冲我大喊大叫，我幼小的心灵已经足够脆弱了。"},
                {"en": "Commitment is a terrifying word for people like me.", "cn": "对于像我这种人来说，‘长相厮守的承诺’简直是个可怕的词汇。"},
                {"en": "Can we skip to the part where everything works out?", "cn": "咱们能不能直接快进到大团圆结局那个部分？"},
                {"en": "I don't know what my actual job title is at work.", "cn": "在公司上班这么多年，我甚至不知道我的具体职称到底叫什么。"},
                {"en": "You are the only person who can tolerate my eccentricities.", "cn": "你是全天下唯一一个能够容忍我这堆古怪脾气的人。"},
                {"en": "Sometimes laughter is the only shield we have left.", "cn": "有时候，幽默的笑声是我们抵御外界仅存的盾牌了。"}
            ]
        },
        {
            "title": "第 5 季 · 罗斯古生物学博物馆日常笑料",
            "description": "恐龙学者罗斯·盖勒的严肃较真与感情波折。",
            "sentences": [
                {"en": "Pivot! Pivot! Pivot!", "cn": "转弯！抬高角度！转弯！(搬沙发名场面)"},
                {"en": "We were on a break!", "cn": "我们当时明明已经在协议冷战分手了！(世纪争论)"},
                {"en": "I am a paleontologist, which means I study dinosaurs.", "cn": "我是一名古生物学家，这意味着我整天都在研究恐龙化石。"},
                {"en": "Someone at work ate my Thanksgiving leftover sandwich with the moist maker.", "cn": "单位里有人偷吃了我带去的热带夹心感恩节火鸡三明治。"},
                {"en": "I have been in love with Rachel since the ninth grade.", "cn": "其实从初中九年级开始，我就一直深深暗恋着瑞秋了。"},
                {"en": "Why does science have to be so difficult for people to grasp?", "cn": "为什么科学原理对于普通大众来说就那么难以理解呢？"},
                {"en": "I am fine! Totally fine! Everything is absolutely fine!", "cn": "我好得很！完全没事！一切都好得不能再好了！"},
                {"en": "Do not touch the fossil display; it took three years to assemble.", "cn": "千万别碰那个恐龙化石展柜，足足花了我三年时间才拼装好。"},
                {"en": "I am getting married again, and this time it will last.", "cn": "我要再次结婚了，而且这一次我们一定会白头偕老。"},
                {"en": "Can we talk about something other than my romantic disasters?", "cn": "咱们能聊点别的吗？别老揪着我那些糟糕透顶的情史不放。"},
                {"en": "My sister has been competitive since the day she was born.", "cn": "我这个亲妹妹，从她出生的第一天起骨子里就充满了胜负欲。"},
                {"en": "Accuracy is the foundation of any respectable scientific research.", "cn": "严谨求实是任何令人尊重的科学研究最根本的基石。"},
                {"en": "You don't just throw away a ten-year friendship over an argument.", "cn": "你总不能因为一场口角争执，就把十年的深厚友谊轻易抛弃吧。"},
                {"en": "She's your lobster. It's a known fact that lobsters mate for life.", "cn": "她是你的命中注定。众所周知龙虾坠入爱河就会相伴终生。"},
                {"en": "I will never lose hope when it comes to true love.", "cn": "只要涉及到真正的挚爱，我永远都不会放弃希望。"}
            ]
        },
        {
            "title": "第 6 季 · 菲比吉他弹唱与奇特灵感",
            "description": "古灵精怪的大自然女孩菲比带来的纯粹快乐。",
            "sentences": [
                {"en": "Smelly cat, smelly cat, what are they feeding you?", "cn": "臭臭猫，臭臭猫，他们到底在喂你吃什么？(传世神曲)"},
                {"en": "They don't know that we know they know we know!", "cn": "他们不知道我们已经知道他们知道我们知道！(经典绕口令)"},
                {"en": "I don't even have a 'pla'!", "cn": "我甚至连个'计'都还没有，更别说完整的'计划'了！"},
                {"en": "My mother told me that tree leaves whisper secrets at night.", "cn": "我妈妈曾经告诉我，深夜里树上的叶子都在互诉悄悄话。"},
                {"en": "I will play my acoustic guitar in front of the coffee shop.", "cn": "我要在咖啡馆门前的台阶上弹着我的木吉他卖唱。"},
                {"en": "You have very negative aura surrounding you today.", "cn": "你今天整个人周身都笼罩着一股极其负能量的气场。"},
                {"en": "Animals understand compassion far better than human beings do.", "cn": "在感知同理心这方面，动物往往比人类纯粹深刻得多。"},
                {"en": "I made this bizarre painting out of discarded mannequin parts.", "cn": "我用别人丢弃的服装假人模特零件组装成了这幅奇特装置画。"},
                {"en": "You should follow your intuition instead of overthinking logic.", "cn": "你应该跟随内心的敏锐直觉，而不是把大脑过度陷在逻辑里。"},
                {"en": "Nothing in this magical universe happens completely by coincidence.", "cn": "在这个奇妙的宇宙中，没有任何事情是纯粹出于偶然巧合的。"},
                {"en": "I might be weird, but at least I am completely authentic.", "cn": "我也许在外人看来古灵精怪，但至少我活得完完全全坦率真诚。"},
                {"en": "Let's all hold hands and send positive energy to the universe.", "cn": "让我们大家手牵着手，一起向浩瀚的宇宙输送积极正念吧。"},
                {"en": "If you want the rainbow, you have to tolerate the heavy rain.", "cn": "如果你渴望看见绚丽的彩虹，你就必须经受得住漫天倾盆大雨。"},
                {"en": "I am writing a brand new folk song about street pigeons.", "cn": "我正在创作一首全新的民谣歌曲，主题是关于街头觅食的鸽子。"},
                {"en": "Love is the only song that everyone in the room knows.", "cn": "爱是整个房间里唯一一首每个人都会哼唱的旋律。"}
            ]
        },
        {
            "title": "第 7 季 · 瑞秋时尚圈打拼与职场升职",
            "description": "从娇生惯养的大小姐到雷夫·罗伦时尚总监的蜕变。",
            "sentences": [
                {"en": "I am tired of everyone treating me like an empty shoe box.", "cn": "我受够了身边所有人都把我当成一个徒有其表的空鞋盒看待。"},
                {"en": "I got hired as an assistant buyer at Bloomingdale's!", "cn": "我被布鲁明戴尔百货正式录用为时尚采购助理了！"},
                {"en": "Fashion is not just clothes; it is how you present your spirit.", "cn": "时尚不仅仅是身上的衣裳，它是你向世界展示精神风貌的方式。"},
                {"en": "I poured coffee for two straight years to get this breakthrough.", "cn": "为了等到今天这个职场突破，我老老实实端了整整两年的咖啡。"},
                {"en": "Do you like this lavender silk blouse for the interview?", "cn": "你觉得这件薰衣草紫色的丝绸衬衫适合穿去参加面试吗？"},
                {"en": "Hard work finally pays off if you stay persistent enough.", "cn": "只要你足够坚持不懈，付出的辛勤汗水终究会得到丰厚回报。"},
                {"en": "I have to prepare the quarterly runway presentation by Monday.", "cn": "我必须在下周一前准备好下季度时装秀的走秀方案幻灯片。"},
                {"en": "Never let anyone make you feel small in a conference room.", "cn": "在会议室里，永远别让任何人有贬低你或让你感到自卑的机会。"},
                {"en": "I made my own money, and I bought my own shoes.", "cn": "我自己靠双手赚到了钱，我自己买下了梦寐以求的高跟鞋。"},
                {"en": "Balance between a bustling career and genuine personal life is hard.", "cn": "在繁忙飞奔的事业与真实温暖的个人生活之间保持平衡实属不易。"},
                {"en": "Paris offered me an incredible dream job in high fashion.", "cn": "巴黎时尚总部向我抛出了一份令人难以置信的高定梦想职位。"},
                {"en": "My heart tells me that my real home is here in New York.", "cn": "但我内心的声音告诉我，我真正的归宿就在纽约这座城市。"},
                {"en": "Friends are the family that you choose for yourself.", "cn": "朋友，就是你自己亲自为自己挑选的家人。"},
                {"en": "I got off the plane!", "cn": "我从去巴黎的飞机上走下来了！(全剧高泪点)"},
                {"en": "I don't want to live without you ever again.", "cn": "往后的余生里，我再也不想过没有你在身边的日子了。"}
            ]
        },
        {
            "title": "第 8 季 · 感恩节橄榄球赛与吃火鸡插曲",
            "description": "一年一度充满火药味与欢笑的感恩节保留节目。",
            "sentences": [
                {"en": "Thanksgiving without delicious food is not a real holiday at all.", "cn": "没有一桌丰盛可口的美食，感恩节根本算不上真正的节日。"},
                {"en": "Who won the legendary Geller Cup football trophy last year?", "cn": "去年那场激烈的盖勒杯家族橄榄球争夺赛到底是谁赢了？"},
                {"en": "I baked a traditional pumpkin pie with a hint of cinnamon.", "cn": "我亲手烘焙了一个带有淡淡肉桂香气的传统南瓜派。"},
                {"en": "Joey finished an entire nineteen-pound roast turkey by himself.", "cn": "乔伊一个人竟然把整只足足十九磅重的烤火鸡全吃光了。"},
                {"en": "We are all thankful for having each other through thick and thin.", "cn": "我们由衷感恩能够彼此相守，风雨同舟携手走过岁岁年年。"},
                {"en": "Touchdown! Monica scored against the boys once again.", "cn": "达阵得分！莫妮卡再一次在球场上把男生们给打得落花流水。"},
                {"en": "Put the turkey on your head to cheer me up, please.", "cn": "求求你，把那只大火鸡套在头上逗我开心一下好不好？"},
                {"en": "Family holidays are always chaotic, loud, and full of warmth.", "cn": "家庭聚会永远都是乱成一团、吵吵闹闹，但也饱含无尽温情。"},
                {"en": "Pass the homemade cranberry sauce down to this end of the table.", "cn": "请把那碗自制的蔓越莓果酱递到餐桌这头来，谢谢。"},
                {"en": "I burned the sweet potatoes because I was too competitive.", "cn": "因为我一心光顾着在橄榄球场上争胜负，把烤箱里的红薯给烤糊了。"},
                {"en": "Nothing brings old friends closer together than a holiday tradition.", "cn": "没有什么能比一项温存的节日传统更能让老朋友们紧紧依偎了。"},
                {"en": "Let us go around the table and each name what we appreciate most.", "cn": "让我们围着餐桌转一圈，每个人都说一件自己最心怀感激的事。"},
                {"en": "I appreciate that you never let me face darkness alone.", "cn": "我最感激的是，你从未让我一个人孤零零地去面对黑暗。"},
                {"en": "Can we have leftover cold turkey sandwiches for the next three days?", "cn": "接下来整整三天咱们都能顿顿吃剩下的冷火鸡三明治了吗？"},
                {"en": "Every Thanksgiving with you six is an unforgettable memory.", "cn": "和你们六个人度过的每一个感恩节，都是终生难忘的美好回忆。"}
            ]
        },
        {
            "title": "第 9 季 · 伦敦婚礼与跨国旅行冒险",
            "description": "大本钟、双层红巴士与啼笑皆非的婚礼意外。",
            "sentences": [
                {"en": "London, baby! We are finally here in the United Kingdom!", "cn": "伦敦，宝贝！我们终于踏上英国这片土地了！(乔伊欢呼)"},
                {"en": "Look at the double-decker red buses crossing Tower Bridge.", "cn": "快看那些穿行在伦敦塔桥上的红色标志性双层大巴车。"},
                {"en": "Mind the gap between the train platform and the carriage.", "cn": "请注意列车车厢与站台之间的空隙。(伦敦地铁名广播)"},
                {"en": "I take thee, Rachel... wait, I meant Emily!", "cn": "我愿意娶你，瑞秋...等等，我本来想说的是艾米莉！(名场面)"},
                {"en": "How could you say the wrong name at your own wedding altar?", "cn": "你怎么可能在自己神圣的婚礼仪式宣誓上念错新娘的名字？"},
                {"en": "Big Ben is ticking away, just like my patience today.", "cn": "大本钟正在滴答作响，正如我今天逐渐消磨殆尽的耐心一样。"},
                {"en": "I bought this ridiculously oversized British flag hat on the street.", "cn": "我在伦敦街头的小摊上买下了这顶滑稽至极的巨幅米字旗高帽。"},
                {"en": "Traveling overseas always brings out the funniest side of people.", "cn": "跨国长途旅行总是能轻而易举激发出人们性格中最逗趣的一面。"},
                {"en": "A cup of warm English Earl Grey tea cures any travel fatigue.", "cn": "一杯温热纯正的英式格雷伯爵红茶足以驱散所有的旅途奔波疲惫。"},
                {"en": "Sometimes the biggest mistakes lead to the truest awakenings.", "cn": "有时候，最无可挽回的错误反而会引领人们走向最真实的心灵觉醒。"},
                {"en": "We walked through Hyde Park talking about what our future holds.", "cn": "我们漫步在海德公园林荫道上，畅谈着未知的未来会是何种模样。"},
                {"en": "The cobblestone streets here carry hundreds of years of rich history.", "cn": "这里的每一块青石板路面，都承载着数百年沉淀的厚重历史印记。"},
                {"en": "Never board an airplane unless you are completely sure of your destination.", "cn": "除非你心里百分之百确信自己的终点所在，否则永远不要草率登机。"},
                {"en": "No matter how far we wander, we always find our way back home.", "cn": "无论我们漫游流浪到多远的天涯海角，我们总能找到回家的方向。"},
                {"en": "Friendship is the passport that works in every corner of the world.", "cn": "真挚的友谊，就是通向世界上任何一个角落都永远有效的护照。"}
            ]
        },
        {
            "title": "第 10 季 · 搬离公寓与十年的真挚告别",
            "description": "紫色大门、金色猫眼相框，六位老友的温情谢幕。",
            "sentences": [
                {"en": "This apartment has witnessed every single milestone of our youth.", "cn": "这间公寓见证了我们整个青春岁月里每一个不可磨灭的里程碑。"},
                {"en": "Where should we leave our keys before we walk out the purple door?", "cn": "在走出这扇紫色大门之前，我们应该把钥匙留在哪里呢？"},
                {"en": "Should we get some coffee at Central Perk one last time together?", "cn": "咱们要不要最后一次一起去 Central Perk 咖啡馆喝杯咖啡？"},
                {"en": "Sure. Where? (Chandler's last iconic joke of the series)", "cn": "当然好啊。去哪儿喝呢？(钱德勒全剧全剧终最后一句标志性冷幽默)"},
                {"en": "The empty apartment echoing our footsteps feels surreal and poignant.", "cn": "空荡荡的房间里回荡着我们的脚步声，让人感到恍惚而又感伤。"},
                {"en": "Ten incredible years of laughter, tears, and unconditional support.", "cn": "整整十年充满欢声笑语、泪水与彼此无条件支持的不可思议岁月。"},
                {"en": "A new chapter is beginning for all of us with new families and homes.", "cn": "随着全新家庭的建立与乔迁，我们所有人的崭新人生篇章正徐徐拉开。"},
                {"en": "I promise you that nothing will ever change our bond.", "cn": "我向你郑重保证，任何时光变迁都绝不可能改变我们之间的深厚羁绊。"},
                {"en": "The golden picture frame around the peephole will always stay.", "cn": "门镜猫眼周围那个金色的相框，将永远定格在属于我们的记忆里。"},
                {"en": "Thank you for being my anchor when the world felt overwhelming.", "cn": "由衷感谢你，当这整个世界让我感到不堪重负时，你始终是我的锚。"},
                {"en": "We grew up together in the heart of this magnificent city.", "cn": "我们在这座繁华壮丽的城市心脏地带，彼此扶持着共同长大成人。"},
                {"en": "Don't cry because it is over; smile because it happened so beautifully.", "cn": "不要因为落幕而哭泣；为它曾经如此美妙绝伦地发生过而微笑吧。"},
                {"en": "Hold on to the lessons, the inside jokes, and the endless hugs.", "cn": "紧紧握住那些受用一生的教诲、只有我们才懂的默契玩笑与拥抱。"},
                {"en": "Goodbye, Apartment 20. You were the warmest home we ever knew.", "cn": "再见了，20号公寓。你曾是我们此生所知晓的最温暖的港湾。"},
                {"en": "I will love you guys for the rest of my life.", "cn": "在我的余生里，我将永远深深地爱着你们大家。"}
            ]
        }
    ]))

    # 2. 《阿甘正传》(Forrest Gump)
    courses.append(build_course({
        "id": "course-mov-gump",
        "title": "《阿甘正传》(Forrest Gump) · 传世经典台词精选 (10章全集)",
        "category": "movies",
        "categoryName": "影视英语",
        "coverGradient": "from-emerald-600 via-teal-700 to-slate-900",
        "icon": "🍫",
        "description": "纯真善良的心灵史诗，朴素字句中饱含深刻的人生哲理、奔跑力量与母爱大智慧。",
        "difficulty": "入门 A1",
        "tags": ["奥斯卡金奖", "人生哲理", "慢速感悟", "至简之美"]
    }, [
        {
            "title": "第 1 幕 · 绿荫长椅上的巧克力盒人生",
            "description": "公车站绿荫长椅上，阿甘讲述妈妈关于人生的至理名言。",
            "sentences": [
                {"en": "Life was like a box of chocolates. You never know what you're gonna get.", "cn": "生活就像一盒巧克力，你永远不知道下一块会是什么味道。"},
                {"en": "My mama always said, stupid is as stupid does.", "cn": "我妈妈总是说，蠢人做蠢事，做蠢事的才是真正的傻子。"},
                {"en": "Hello, my name's Forrest, Forrest Gump. Do you want a chocolate?", "cn": "你好，我的名字叫阿甘，福雷斯特·阿甘。你想来颗巧克力吗？"},
                {"en": "I could eat about a million and a half of these sweet treats.", "cn": "像这么好吃的甜点，我一口气能吃上一百五十万颗。"},
                {"en": "Mama said you can tell an awful lot about a person by their shoes.", "cn": "妈妈说，你只要看一个人脚上穿的鞋子，就能知道关于他的很多事情。"},
                {"en": "Where they going, where they've been, all the roads they walked.", "cn": "他们要去往何方，他们曾经去过何处，他们走过的所有漫长道路。"},
                {"en": "I wear these magic shoes because my back is as crooked as a politician.", "cn": "我穿着这些神奇的矫正铁鞋，因为我的脊梁骨弯得像政客一样。"},
                {"en": "She always had a way of explaining things so I could understand.", "cn": "妈妈总有办法把复杂深奥的大道理，解释得让我轻松听懂。"},
                {"en": "Remember what I told you, Forrest: you're no different than anybody else.", "cn": "记住我对你说过的话，阿甘：你和天底下其他任何人没有任何不同。"},
                {"en": "Don't ever let anybody tell you that they're better than you.", "cn": "永远不要让任何人告诉你，他们天生就比你优秀高贵。"},
                {"en": "If God intended everybody to be the same, he'd have given us all braces on our legs.", "cn": "如果上帝真打算让所有人都一模一样，他就会给我们所有人的腿上都装上铁支架了。"},
                {"en": "I was born with a strong heart and two good hands.", "cn": "我生来就拥有一颗坚韧善良的心，以及两只勤劳完好的双手。"},
                {"en": "You have got to put the past behind you before you can move on.", "cn": "你必须把过去的一切放下，才能轻装上阵大步向前迈进。"},
                {"en": "That is what my mama always told me when times were rough.", "cn": "每当日子变得艰辛苦涩的时候，这就是我妈妈常常对我说的话。"},
                {"en": "Miracles happen every day. Some people don't think so, but they do.", "cn": "奇迹每天都在发生。有些人不这么认为，但它们确实在真真切切地发生着。"}
            ]
        },
        {
            "title": "第 2 幕 · 奔跑穿过阿拉巴马绿草地",
            "description": "珍妮的一声呼喊，挣脱铁支架，跑向自由与速度的奇迹。",
            "sentences": [
                {"en": "Run, Forrest, run! Run as fast as your legs can carry you!", "cn": "跑，阿甘，快跑！迈开步子拼命跑，跑得越快越好！"},
                {"en": "Now you wouldn't believe it if I told you, but I could run like the wind blows.", "cn": "我说出来你可能不会相信，但我跑起来的时候就像疾风掠过一样快。"},
                {"en": "Those braces on my legs broke into little pieces and fell off behind me.", "cn": "我腿上的那些金属铁支架全都崩裂成碎片，一路散落在我的身后。"},
                {"en": "From that day on, if I was going somewhere, I was running!", "cn": "从那一刻起，无论我要去往哪里，我都是用双腿全速奔跑着去的！"},
                {"en": "The bullies in the pickup truck could never catch up with me again.", "cn": "皮卡车上的那些坏小子们再也追不上奔跑中的我了。"},
                {"en": "I ran right through the green cornfields under the wide Alabama sky.", "cn": "我飞奔穿过阿拉巴马广袤苍穹下一望无际的翠绿玉米地。"},
                {"en": "When I got tired, I slept; when I got hungry, I ate.", "cn": "累了我就找地方睡觉；饿了我就吃口干粮填饱肚子。"},
                {"en": "There was no particular reason to run; I just felt like doing it.", "cn": "奔跑并没有什么特别崇高的理由；我只是心里想这么做而已。"},
                {"en": "Sometimes people need a simple direction to follow in this noisy world.", "cn": "在这个喧嚣嘈杂的世界上，人们有时只需要一个简单纯粹的前进方向。"},
                {"en": "I ran all the way across the college football field for a touchdown.", "cn": "我一路飞奔贯穿大学橄榄球赛场，直接冲刺完成了一次精彩绝伦的达阵。"},
                {"en": "Coach Bryant said that boy sure is a running fool.", "cn": "传奇教练布莱恩特由衷感叹道：那小子真是一个天生为奔跑而狂的飞人。"},
                {"en": "Running gave me peace when everything else around me felt chaotic.", "cn": "当周围的一切都陷入混乱失序时，唯有纯粹的奔跑能带给我内心的宁静。"},
                {"en": "You don't need a map when you have courage pumping in your chest.", "cn": "当你胸膛里跳动着无畏的勇气时，你根本不需要什么详细的地图指南。"},
                {"en": "Keep your eyes on the clear blue horizon and never look back.", "cn": "把你的目光坚定投向那片清澈蔚蓝的地平线，永不回头。"},
                {"en": "Every step forward takes you closer to where your destiny waits.", "cn": "向前迈出的每一个坚实步伐，都让你离属于你的命运更近一步。"}
            ]
        },
        {
            "title": "第 3 幕 · 妈妈教给我的生活大智慧",
            "description": "深沉伟大的母爱，为阿甘的一生奠定了温厚明亮的底色。",
            "sentences": [
                {"en": "Mama always said that dying was a part of life. I sure wish it wasn't.", "cn": "妈妈总是说死亡也是生命的一部分。我真希望事实不是这样。"},
                {"en": "She was the smartest lady I ever knew in my whole entire life.", "cn": "她是我这辈子所认识的最有智慧、最了不起的女士。"},
                {"en": "You have got to find out what your destiny is on your own, Forrest.", "cn": "阿甘，你必须靠你自己的双脚和内心，去探寻属于你的命运究竟是什么。"},
                {"en": "I happen to believe you make your own destiny through everyday kindness.", "cn": "而我坚信，是你日常每一次微小的善良抉择，铸就了你自己的命运。"},
                {"en": "Death is just a peaceful rest after a long and meaningful journey.", "cn": "在一场漫长而充实的旅程之后，死亡不过是一次平静安详的安歇。"},
                {"en": "She did not complain once, even when the sickness took her energy.", "cn": "哪怕重病耗尽了她所有的力气，她也从未开口抱怨过一次。"},
                {"en": "A mother's love protects you like an invisible suit of strong armor.", "cn": "母亲的爱就像一套坚不可摧的无形盔甲，时刻庇佑着你前行。"},
                {"en": "I sat beside her bed holding her gentle, weathered hand until dark.", "cn": "我静静坐在她的病床边，紧紧握着她那双温柔而饱经风霜的手直到天黑。"},
                {"en": "She told me I had made her proud every single day of her life.", "cn": "她告诉我，在我生命里的每一天，我都让她深感无比的骄傲自豪。"},
                {"en": "True wealth is not measured by dollars, but by how many souls you touch.", "cn": "真正的财富绝不能用金钱多寡来衡量，而是看你曾经温暖触动过多少心灵。"},
                {"en": "I miss her dearly, but her loving voice still guides my wandering steps.", "cn": "我深深地思念着她，但她充满慈爱的声音依然指引着我前行的漫漫步伐。"},
                {"en": "A clean conscience brings the sweetest and most restful sleep at night.", "cn": "一颗光明磊落、问心无愧的良心，能带来夜晚最甘甜安稳的睡眠。"},
                {"en": "Treat everyone with respect, from the street sweeper to the president.", "cn": "从街头的清洁工到一国之总统，用同等的尊严与敬意对待遇见的每一个人。"},
                {"en": "The love you give away freely is the only treasure you keep forever.", "cn": "你慷慨无私奉献出去的爱，是你在世间能够永远保留的唯一宝藏。"},
                {"en": "Her lessons remain carved deep inside my grateful and humble heart.", "cn": "她的教诲如刀刻斧凿般，深深铭印在我那颗充满感恩与谦卑的心中。"}
            ]
        },
        {
            "title": "第 4 幕 · 丹中尉与捕虾船暴风雨洗礼",
            "description": "在肆虐的巨浪与狂风暴雨中，丹中尉与上帝和解重获新生。",
            "sentences": [
                {"en": "Lieutenant Dan, what are you doing out here in the pouring rain?", "cn": "丹中尉，狂风暴雨下得这么大，你一个人跑出来在甲板上做什么？"},
                {"en": "He was challenging God Almighty right from the top of the ship's mast.", "cn": "他爬到捕虾船桅杆的最高处，正面向上帝全能的主发出愤怒的挑战呐喊。"},
                {"en": "You call this a storm? Blow harder, you coward of the seas!", "cn": "你把这叫做风暴？刮得再猛烈点啊，你这片大海上的胆小鬼！(丹中尉怒吼)"},
                {"en": "The hurricane destroyed every single shrimp boat in the bay except ours.", "cn": "那场凶猛的飓风摧毁了海湾里所有的捕虾船，除了我们这一艘奇迹幸存。"},
                {"en": "After the storm passed, there was a calm and peaceful silence on the water.", "cn": "当暴风雨狂怒退去之后，海面上迎来了一片辽阔宁静祥和的沉寂。"},
                {"en": "Lieutenant Dan never said it aloud, but I think he made his peace with God.", "cn": "丹中尉从未把心事说出口，但我认为他就在那一刻与上帝握手言和了。"},
                {"en": "He swam in the warm ocean water with a bright and serene smile.", "cn": "他在温暖碧绿的海水里自在畅游，脸上洋溢着灿烂而释怀的安详微笑。"},
                {"en": "A broken spirit can heal if you give it enough faith and patience.", "cn": "一颗破碎受创的心灵只要得到足够的信念与耐心呵护，终究能够痊愈重获生机。"},
                {"en": "We caught so many fresh pink shrimps that we filled fifty large barrels.", "cn": "我们捕捞到了数不胜数的肥美大粉虾，足足装满了五十只大木桶。"},
                {"en": "Bubba Gump Shrimp Corporation became a household name across the land.", "cn": "‘阿甘虾业公司’的名号迅速传遍大江南北，成为了家喻户晓的招牌。"},
                {"en": "A promise made to a brother in arms is a sacred vow that never dies.", "cn": "对战壕里生死与共的好兄弟许下的承诺，是一份至死不渝的神圣誓言。"},
                {"en": "I gave Bubba's sweet mama her half of the company profits.", "cn": "我把公司赚来的一半丰厚利润，原封不动地全部送交给了布巴亲爱的妈妈。"},
                {"en": "He said thank you for saving my life in the thick jungle of Vietnam.", "cn": "他轻声对我说：谢谢你在越南密林深处拼上性命救回了我的这条命。"},
                {"en": "Sometimes a ferocious tempest is the only thing that cleanses the soul.", "cn": "有时候，唯有一场狂暴残酷的暴风雨洗礼，才能彻底洗净一个人蒙尘的灵魂。"},
                {"en": "True brotherhood is forged through trials of fire, blood, and salt water.", "cn": "真正的兄弟手足情深，是在烈火、鲜血与咸涩海水的重重淬炼中铸就的。"}
            ]
        },
        {
            "title": "第 5 幕 · 珍妮的吉他与追寻爱与自由",
            "description": "那只像小鸟一样渴望展翅高飞的珍妮，阿甘一生唯一的挚爱。",
            "sentences": [
                {"en": "Dear God, make me a bird so I can fly far, far away from here.", "cn": "亲爱的上帝，请把我变成一只小鸟吧，好让我能展翅飞离这里，飞得远远的。"},
                {"en": "You will always be my girl, Jenny, no matter where life takes you.", "cn": "珍妮，无论生活的浪潮把你带向何方，你永远都是我最珍爱的好姑娘。"},
                {"en": "I may not be a smart man, but I know what love is.", "cn": "我也许不是个绝顶聪明的大人物，但我心里懂得什么是真正的爱。(经典催泪)"},
                {"en": "She sang folk songs softly with her acoustic guitar on the quiet porch.", "cn": "她坐在宁静的走廊门廊上，伴着手中的木吉他轻柔浅唱着动人的民谣。"},
                {"en": "Every time she came back home, it was like the sunshine returned to Greenbow.", "cn": "每当她疲惫归家的时候，就仿佛灿烂温煦的阳光重新照耀着绿荫小镇。"},
                {"en": "I waited for her by the big oak tree through summer, autumn, and winter.", "cn": "我在那棵参天大橡树下默默守候着她，历经盛夏、清秋与漫长寒冬。"},
                {"en": "Why don't you love me, Jenny? I am always right here waiting for you.", "cn": "珍妮，你为什么不能试着爱我呢？我一直都在这里默默等候着你啊。"},
                {"en": "Her life was filled with stormy wandering, but her heart remained gentle.", "cn": "她的一生颠沛流离、饱经风霜磨难，但她的内心深处依然保有一份纯真与温柔。"},
                {"en": "We walked barefoot together in the dewy grass just like when we were little children.", "cn": "我们脱掉鞋子光着脚丫并肩漫步在挂满露珠的草地上，就像小时候无忧无虑的孩提模样。"},
                {"en": "Forgiveness is the supreme gift you give to both the other person and yourself.", "cn": "由衷的宽恕与释怀，是你赠予对方、也赠予自己最崇高珍贵的解脱礼物。"},
                {"en": "She gave me the greatest treasure in the universe: our precious little boy.", "cn": "她赋予了我整个宇宙中最无可比拟的无价瑰宝：我们可爱聪颖的小阿甘。"},
                {"en": "I buried her under our favorite oak tree where the breeze whispers softly.", "cn": "我将她安葬在我们最深爱的那棵大橡树下，那里终年回荡着微风的轻柔耳语。"},
                {"en": "I miss you every day, Jenny, and I talk to you whenever I look at the stars.", "cn": "珍妮，我每一天都在深深想念着你；每当我抬头仰望繁星，我就在心里和你细语。"},
                {"en": "Love never dies; it simply transforms into an eternal guiding light.", "cn": "爱永远不会消亡；它只是化作了一束永恒照亮前方道路的温润指路明灯。"},
                {"en": "You were the music that accompanied my soul through this long life.", "cn": "在这个漫长的一生中，你就是那支始终伴随着我孤独灵魂翩跹起舞的动人乐章。"}
            ]
        },
        {
            "title": "第 6 幕 · 白羽毛飘落与宁静致远的心",
            "description": "片头与片尾那一根随风翩跹飘落的纯白羽毛。",
            "sentences": [
                {"en": "I don't know if Mama was right or if Lieutenant Dan was right.", "cn": "我不知道究竟是我妈妈说得对，还是丹中尉说得更接近真相。"},
                {"en": "I don't know if we each have a destiny, or if we're all just floating around accidental-like on a breeze.", "cn": "我不知道我们每个人命中是否都有既定宿命，还是我们都只是像微风中的羽毛一样偶然随风飘荡。"},
                {"en": "But I think, maybe it's both. Maybe both is happening at the same time.", "cn": "但是我想，也许两者都有道理吧。也许这两者同时在我们的生命里发生着。"},
                {"en": "The yellow school bus stopped right in front of our little country house.", "cn": "那辆明黄色的学校校车，稳稳停靠在我们乡村木屋的大门正前方。"},
                {"en": "Little Forrest carried his backpack proudly, just as smart as a whip.", "cn": "小阿甘骄傲地背着他的小书包，那副机灵聪明的模样简直像闪电一样讨人喜爱。"},
                {"en": "You go ahead and show the world what a brilliant mind you have, son.", "cn": "去吧儿子，昂首阔步走向外面的世界，向大家展示你拥有一颗多么璀璨聪慧的心灵。"},
                {"en": "I will be right here waiting for you when the afternoon bell rings.", "cn": "当下午放学的清脆钟声敲响时，爸爸就在这里寸步不离地守候着你归来。"},
                {"en": "The white feather floated gently from between the pages of the curious book.", "cn": "那根纯白的羽毛从那本神奇的童话书书页缝隙中，轻盈优雅地飘浮而起。"},
                {"en": "It twirled in the crisp morning air and drifted up toward the azure sky.", "cn": "它在清晨清冽纯净的微风中欢快打着旋儿，缓缓升腾飞向蔚蓝辽阔的高空。"},
                {"en": "Life's deepest beauty often resides in the quietest, unheralded moments.", "cn": "生命中最深沉隽永的大美，往往就静静隐匿在那些无声无息、不为人知的质朴瞬间。"},
                {"en": "Keep your heart pure, your step steady, and your conscience crystal clear.", "cn": "永远保持内心的纯洁如初、步伐的稳健笃定，以及良知的冰清玉洁。"},
                {"en": "Kindness is a currency that never loses its purchasing power in heaven.", "cn": "纯粹的善良是一张在任何天堂与人间都永远不会贬值流通的硬通货。"},
                {"en": "A humble man who loves deeply can change the entire world without knowing it.", "cn": "一个心怀深沉大爱、谦卑质朴的平凡人，往往在不知不觉中便悄然改变了整个世界。"},
                {"en": "The wind bloweth where it listeth, and thou hearest the sound thereof.", "cn": "风随着意思吹拂，你能听见它轻柔的呼吸，却不知它从何处来，往何处去。"},
                {"en": "Rest in peace, sweet soul; your story will be told for generations to come.", "cn": "安息吧，善良纯真的灵魂；关于你的美丽传奇，必将被后世一代又一代深情传唱。"}
            ]
        },
        {
            "title": "第 7 幕 · 乒乓球外交与专注力的奇迹",
            "description": "只要眼睛死死盯着球，平凡人也能创造惊艳世界的专注奇迹。",
            "sentences": [
                {"en": "They gave me a ping pong paddle and told me to never take my eye off the ball.", "cn": "他们在军医院里塞给我一副乒乓球拍，严厉叮嘱我眼睛绝对不要离开那个球半分。"},
                {"en": "No matter what happens around you, keep your eye on that little white ball.", "cn": "无论周围发生了什么天崩地裂的事，死死盯住那个弹跳旋转的小白球就对了。"},
                {"en": "Now, for some reason, ping pong came very natural to me right from the start.", "cn": "不知道出于什么神奇缘故，乒乓球这项运动从一开始就如同我与生俱来的本能一样自如。"},
                {"en": "I played against the wall for hours until my wrist grew stronger than iron.", "cn": "我一个人对着光秃秃的水泥墙壁连续击球数小时，直到手腕磨炼得比钢铁还要坚韧有力。"},
                {"en": "The sound of the ball hitting the wooden table became my favorite rhythmic beat.", "cn": "乒乓球清脆撞击木质球台的声音，渐渐成为了我耳畔最陶醉喜爱的节奏节拍。"},
                {"en": "Someone said I played like a machine that never ran out of electricity.", "cn": "有人惊呼说我打起球来就像一台永不断电、精准无误的永动机一样可怕。"},
                {"en": "I was chosen to travel all the way across the globe to China for diplomacy.", "cn": "我竟然被军方选拔为代表团成员，千里迢迢跨越重洋远赴中国开展乒乓体育外交。"},
                {"en": "Sports have a wonderful way of uniting people who do not speak the same language.", "cn": "体育竞技拥有一种不可思议的魔力，能把语言不通、文化悬殊的人们紧紧联结在一起。"},
                {"en": "The Chinese players were exceptionally polite and had lightning-fast reflexes.", "cn": "中国队的选手们不仅待人谦逊知礼，而且挥拍反击的敏捷反应快得宛如闪电。"},
                {"en": "Focus is the secret weapon that turns ordinary talent into extraordinary mastery.", "cn": "极致的专注力，就是把凡夫俗子的平庸天赋蜕变为惊世绝伦造诣的终极秘诀。"},
                {"en": "I didn't care about the fame; I just liked hearing that satisfying click-clack sound.", "cn": "我压根就不在乎什么举世盛名；我只是单纯喜欢听那令人心旷神怡的乒乓脆响罢了。"},
                {"en": "A simple paddle and dedication can build bridges across vast cultural chasms.", "cn": "一块简简单单的木球拍加上纯粹的执着投入，足以在截然不同的文明鸿沟之上架起理解之桥。"},
                {"en": "When you eliminate all external distractions, the impossible suddenly becomes achievable.", "cn": "当你摒除掉内心所有繁杂的外在纷扰时，原先看似天方夜谭的不可能瞬间迎刃而解。"},
                {"en": "President Nixon invited our entire ping pong team to the White House.", "cn": "尼克松总统亲自在白宫椭圆形办公室热情接见了我们乒乓球代表队全体成员。"},
                {"en": "Do whatever you are doing with complete passion and zero hidden motives.", "cn": "做你当下正在做的事，怀揣百分之百纯粹的热忱，心中不掺杂任何功利的杂质。"}
            ]
        },
        {
            "title": "第 8 幕 · 华盛顿纪念碑前的水中拥抱",
            "description": "万人集会反战演讲，水池两端奔向彼此的世纪重逢。",
            "sentences": [
                {"en": "There was a crowd of over one hundred thousand people standing near the reflecting pool.", "cn": "在华盛顿林肯纪念堂倒影池畔，聚集了超过十万名浩浩荡荡的人群。"},
                {"en": "The microphone cable was unplugged, but my message of peace remained true.", "cn": "演讲话筒的电缆线虽然被人恶意拔掉了，但我关于和平的朴素心声却真诚无欺。"},
                {"en": "Suddenly I heard a sweet, familiar voice shouting my name across the crowd.", "cn": "突然间，我穿透嘈杂纷乱的人声鼎沸，听到了一声甜美而熟悉的嗓音在呼唤着我的名字。"},
                {"en": "Forrest! Forrest! She was wading into the waist-deep reflecting pool toward me.", "cn": "阿甘！阿甘！珍妮脱了鞋，不顾一切趟进齐腰深的倒影水池中向我飞奔而来。"},
                {"en": "Jenny! I jumped right into the splashing water without a second thought.", "cn": "珍妮！我连想都没想，纵身一跃跳进了水花四溅的池塘迎着她奔去。(传世催泪画面)"},
                {"en": "We met right in the center of the pool and held each other tight.", "cn": "我们在池水的最中央紧紧相撞相遇，用尽全副力气紧紧相拥抱在一起。"},
                {"en": "The entire crowd of strangers erupted into thunderous cheering and applause.", "cn": "四周成千上万原本素不相识的庞大人群，瞬间爆发出如雷鸣般震天的欢呼与热烈掌声。"},
                {"en": "In that single breathtaking moment, all the pain and separation disappeared forever.", "cn": "在那个令人屏息沉沦的瞬间，往昔所有苦难折磨与残酷别离全都化作云烟彻底烟消云散。"},
                {"en": "Her soaked clothes and wet hair were the most beautiful sight I ever beheld.", "cn": "她被池水浸湿的衣衫与贴在颊边的发丝，是我这辈子所凝望过的最动人美丽的风景。"},
                {"en": "Love has the power to silence wars, heal wounds, and unite divided souls.", "cn": "真挚的大爱拥有一种神圣威能，足以让战火止息、抚平疮痍创伤，并让分崩离析的灵魂合而为一。"},
                {"en": "I felt like my heart would burst with an abundance of pure gratitude.", "cn": "那一刻我直觉得自己的胸膛快要被那决堤般丰盈纯粹的感恩之情给融化撑爆了。"},
                {"en": "No ocean is too deep and no distance is too far for true devotion.", "cn": "对于矢志不渝的深情挚爱而言，纵使刀山火海也不算深邃，天涯海角也不算遥远。"},
                {"en": "We walked hand in hand under the autumn trees along the Potomac river.", "cn": "我们在波托马克河畔金黄的秋树林荫下，十指相扣紧紧依偎着并肩漫步。"},
                {"en": "Hold on to the ones who see your soul even when you are invisible.", "cn": "牢牢握紧那个即使在全世界都对你视而不见时、依然能一眼望穿你纯洁灵魂的人。"},
                {"en": "Some memories shine so bright that time itself cannot diminish their luster.", "cn": "有些温存的记忆在岁月长河中是如此璀璨夺目，连时光老人都无法夺走它的熠熠光华。"}
            ]
        },
        {
            "title": "第 9 幕 · 苹果电脑股票与财富的真谛",
            "description": "丹中尉投资了一家卖水果的公司，钱够用就好，多出来的去帮别人。",
            "sentences": [
                {"en": "Lieutenant Dan got me invested in some kind of fruit company.", "cn": "丹中尉帮我把赚来的钱，投资到了一家听起来像是专门卖水果的高科技公司里。(苹果电脑)"},
                {"en": "He called me up and told me that we didn't have to worry about money no more.", "cn": "他特意给我打电话兴奋地告诉我：我们这辈子再也用不着为钱发愁了。"},
                {"en": "And I said, that's good! One less thing to worry about.", "cn": "我听了憨憨一笑回答道：那挺好的！这下心里又少了一件需要挂念的烦心事啦。"},
                {"en": "Mama always told me that there's only so much fortune a man really needs.", "cn": "我妈妈生前总爱对我说，一个人活在这世上，真正能够消耗享用的财富其实只有那么一丁点。"},
                {"en": "The rest of the wealth is just for showing off to vanity.", "cn": "其余堆积如山的财富，不过是拿来在人前炫耀空虚浮华的虚荣心罢了。"},
                {"en": "So I gave a big pile of money to build the church and hospital.", "cn": "所以我拿出了好大一笔巨款，捐赠修建了镇上的新教堂以及免费医疗综合医院。"},
                {"en": "And I gave Bubba's family enough money so they never had to work in other kitchens.", "cn": "我还给了布巴家人一大笔终生衣食无忧的信托资金，让他们再也不用去别人的厨房当下人受累了。"},
                {"en": "I still cut the grass on the football field for free every weekend.", "cn": "每个周末我依然开着我的绿色小除草机，无偿自愿为大学橄榄球场修剪平整翠绿的草坪。"},
                {"en": "Mowing the lawn smells like fresh earth and gives my mind a pleasant rest.", "cn": "修剪草坪散发出的那股清新泥土与草汁芬芳，总能让我的大脑得到最舒畅适意的休憩。"},
                {"en": "Money cannot buy you true happiness, authentic friends, or peaceful dreams.", "cn": "金钱买不来由衷的快乐，买不来推心置腹的挚友，更买不来深夜宁静香甜的美梦。"},
                {"en": "Use what you have been blessed with to lift up those who are struggling.", "cn": "善用上帝厚赐于你的充裕福祉，去扶起托举那些深陷泥潭苦苦挣扎的苦难同胞。"},
                {"en": "Simplicity of lifestyle is the true hallmark of inner spiritual sophistication.", "cn": "生活方式的质朴至简，才是一个人心灵深处崇高超然精神境界的真正标尺。"},
                {"en": "I never considered myself rich; I just consider myself abundantly blessed.", "cn": "我从未觉得自己是个所谓的大富翁；我只觉得自己是一个被上天浩荡恩典眷顾的幸运儿。"},
                {"en": "Generosity expands your capacity to experience profound joy in living.", "cn": "慷慨施舍给予他人，能成倍成倍开拓你在这人世间感知丰盈喜悦的心灵容量。"},
                {"en": "The best things in life are indeed entirely free for all open hearts.", "cn": "这世上最弥足珍贵的美好之物，对于所有敞开心扉的人而言，原本就是完全免费的。"}
            ]
        },
        {
            "title": "第 10 幕 · 穿越全美大洲的无止境奔跑",
            "description": "三年两个月十四天十六个小时，跑过山川、大海与沙漠红岩。",
            "sentences": [
                {"en": "That day, for no particular reason, I decided to go for a little run.", "cn": "那天，并没有什么特别的原因，我只是心血来潮决定出门小跑那么一小段路。"},
                {"en": "So I ran to the end of the driveway, and then across the whole town.", "cn": "于是我跑到了自家庭院车道的尽头，接着一口气跑穿了整座小镇。"},
                {"en": "When I got to the Atlantic Ocean, I turned around and headed for the Pacific.", "cn": "当我一路跑到辽阔的大西洋海边时，我想既然都到了，不如转身向着太平洋奔跑吧。"},
                {"en": "I ran for three years, two months, fourteen days, and sixteen hours.", "cn": "我整整跑了三年零两个月十四天又十六个小时，穿越了全美壮美的山川河流。"},
                {"en": "I saw the crimson sun setting behind the majestic Monument Valley desert rocks.", "cn": "我曾亲眼目睹落日余晖如烈火般，将纪念碑山谷巍峨耸立的沙漠红岩染得通红。"},
                {"en": "I saw clear mountain lakes in the Rockies that looked like polished crystal glass.", "cn": "我曾见过落基山脉间清澈见底的高山冰川湖泊，澄澈纯净宛如经由大师精心抛光的天然水晶玻璃。"},
                {"en": "Crowds of people began running behind me, thinking I had all the answers.", "cn": "浩浩荡荡的人群开始自发跟随奔跑在我身后，盲目以为我拥有解答这世间所有人生困惑的终极答案。"},
                {"en": "They asked me if I was running for world peace or women's rights.", "cn": "他们蜂拥上前追问我：你这么苦苦奔跑是为了呼吁世界和平，还是为了女权平等事业？"},
                {"en": "I just told them, I just felt like running.", "cn": "我只是转过头坦然告诉他们：我只是自己心里想跑而已，就这么简单。"},
                {"en": "Then one bright sunny morning in the desert, I stopped right in my tracks.", "cn": "直到在辽阔荒漠一个万里无云阳光明媚的清晨，我突然毫无征兆地在原地收住了脚步。"},
                {"en": "I'm pretty tired. I think I'll go home now.", "cn": "我感觉跑得挺累的了。我想我现在该收拾行李回家去啦。(经典急刹幽默)"},
                {"en": "Sometimes in life, you just run until the sorrow in your heart settles down.", "cn": "人这一生有时就是这样，你拼尽全力地狂奔，直到心头积郁的那团悲伤悄然尘埃落定。"},
                {"en": "You don't have to carry a profound philosophy to make a memorable journey.", "cn": "你并不需要身负多么深奥晦涩的大哲学，照样能踏出一段令人肃然起敬的壮丽史诗之旅。"},
                {"en": "Listen to the quiet voice within that tells you when it is time to turn around.", "cn": "用心倾听内心那道微弱而笃定的声音，它自会在最恰当的时机告诉你该何时驻足转身回家。"},
                {"en": "Home is wherever the people you love are waiting with open arms.", "cn": "无论行至何处，只要有你深爱的人张开双臂翘首以盼的地方，那就是家。"}
            ]
        }
    ]))

    # 3. 《肖申克的救赎》(Shawshank)
    courses.append(build_course({
        "id": "course-mov-shawshank",
        "title": "《肖申克的救赎》(Shawshank) · 希望与信念赞歌 (10章全集)",
        "category": "movies",
        "categoryName": "影视英语",
        "coverGradient": "from-stone-700 via-zinc-800 to-black",
        "icon": "🕊️",
        "description": "IMDb 影史排名第一神作，摩根·弗里曼沉稳独白，字字珠玑，直击灵魂的自由与希望。",
        "difficulty": "中级 B1",
        "tags": ["影史第一", "坚韧信念", "灵魂独白", "自由希望"]
    }, [
        {
            "title": "第 1 篇 · 高墙耸立与习惯的体制化",
            "description": "老囚徒瑞德对于监狱围墙与体制化异化最深刻的剖析。",
            "sentences": [
                {"en": "These walls are funny. First you hate them, then you get used to them.", "cn": "这些高墙很有趣。起初你恨它，接着你逐渐习惯它。"},
                {"en": "Enough time passes, you get so you depend on them. That's institutionalized.", "cn": "等足够长的时间过去，你会变得在精神上深深依赖它。这就叫做体制化。"},
                {"en": "In here, a man who knows how to obtain things is an invaluable resource.", "cn": "在这个与世隔绝的高墙牢笼里，一个通晓搞到稀缺紧俏物资门道的人是一笔宝贵财富。"},
                {"en": "They send you here for life, and that's exactly what they take from you.", "cn": "他们判处你终身监禁把你扔进这里，而他们剥夺走的，恰恰就是你的整个人生。"},
                {"en": "Hope is a dangerous thing. Hope can drive a man insane.", "cn": "希望是个危险至极的东西。希望往往会把一个困兽般绝望的人逼得彻底发疯。"},
                {"en": "It has got no use on the inside; you had better get used to that idea.", "cn": "希望在这堵高墙里面没有任何立足之地；你最好趁早趁早习惯并接受这个残酷现实。"},
                {"en": "Andy Dufresne came to Shawshank in the spring of nineteen forty-seven.", "cn": "安迪·杜弗兰是在一九四七年的明媚春天，被押解来到这所肖申克监狱服刑的。"},
                {"en": "He strolled around the yard like a man walking in a quiet park without a care in the world.", "cn": "他在杂乱吵闹的放风操场上信步漫步，闲适得宛如一个在静谧公园里无忧无虑散步的绅士。"},
                {"en": "He had a quiet jacket of invisible armor wrapped around him at all times.", "cn": "他的身上无时无刻不在若隐若现披裹着一层坚固而宁静的无形甲胄。"},
                {"en": "The hardest part of prison is not the stone walls, but the loss of your own mind.", "cn": "监狱生活最残酷折磨人的部分绝非冰冷坚硬的石墙，而是你自己独立心智与尊严的丧失。"},
                {"en": "Routine can either extinguish your soul or preserve your discipline.", "cn": "周而复始枯燥的铁窗规训，既能将你的灵魂彻底磨灭，亦能磨砺你严谨自律的风骨。"},
                {"en": "Keep a small corner of your spirit untouched by external misery.", "cn": "在你的精神世界深处永远保留一块净土，任凭外界苦难滔天也绝不被其染指分毫。"},
                {"en": "Time moves like slow molasses when you are staring at gray iron bars.", "cn": "当你日复一日凝视着眼前冰冷的灰色铁窗栅栏时，时光流淌得慢如粘稠的糖浆。"},
                {"en": "A free man can never truly be conquered by a prison system.", "cn": "一个在内心深处保有一方自由天地的人，永远无法被任何铁窗体制彻底征服。"},
                {"en": "Remember that the mind is a realm of infinite sovereignty.", "cn": "请时刻谨记：人类的自由心智，是享有无限绝对主权的辽阔王国。"}
            ]
        },
        {
            "title": "第 2 篇 · 屋顶涂柏油与喝冰啤酒的微风",
            "description": "春日清晨工厂厂房屋顶，战胜恐惧赢回如同自由人的尊严。",
            "sentences": [
                {"en": "We were working on the roof of the license plate factory in late spring.", "cn": "那是在暮春时节，我们顶着烈日在一座车牌翻新工厂的大平房屋顶上挥汗涂抹柏油。"},
                {"en": "The sun was beating down, and the smell of hot tar filled our lungs.", "cn": "炽热的骄阳无情炙烤着大地，滚烫刺鼻的柏油焦味直往我们干涸的肺叶里钻。"},
                {"en": "Andy took a bold step forward to offer the captain financial advice.", "cn": "安迪冒着被狱警当场推下悬崖摔得粉身碎骨的巨大危险，挺身而出为狱警队长提供税务筹划建议。"},
                {"en": "Do you trust your wife? That simple question almost got him killed.", "cn": "你信任你的妻子吗？——这句开门见山的直白提问，当时几乎让他命丧黄泉。"},
                {"en": "He bargained for three cold beers apiece for each of his fellow inmates.", "cn": "他据理力争，为一起在屋顶干脏活累活的狱友兄弟们每人赢得了三瓶冰镇啤酒的犒劳。"},
                {"en": "We sat drinking cold suds with the warm breeze washing over our sunburnt shoulders.", "cn": "我们围坐在屋顶边缘畅饮着泛起洁白泡沫的冰镇啤酒，任由温暖宜人的初夏微风拂过晒伤的双肩。"},
                {"en": "For twenty precious minutes, we felt like free men resting on our own roof.", "cn": "在整整二十分钟弥足珍贵的时光里，我们仿佛感觉自己是休憩在自家屋顶上的堂堂自由人。"},
                {"en": "Andy sat with a quiet, enigmatic smile watching the rest of us drink.", "cn": "安迪自己滴酒不沾，只是抱着双膝坐在一旁，脸上带着温和而神秘的微笑凝望着我们开怀畅饮。"},
                {"en": "He didn't drink alcohol; he just wanted to feel a sense of normalcy.", "cn": "他并不嗜好酒精；他只是渴望在铁窗苦难之中，替我们重新找回一丝做正常人的尊严与温度。"},
                {"en": "Dignity is a fragile flame that must be sheltered in hostile environments.", "cn": "人的尊严是一簇极其脆弱的微光火苗，在严酷敌对的恶劣逆境里必须竭力用心呵护。"},
                {"en": "A true master uses intellectual prowess rather than physical violence to prevail.", "cn": "一个真正的大师级智者，从来都是运用超群绝伦的智识而非野蛮暴力来克敌制胜。"},
                {"en": "Even in the darkest gulag, moments of sublime grace can blossom.", "cn": "哪怕在人间最黑暗绝望的集中营里，崇高神圣的优雅风骨亦能奇迹般凌寒绽放。"},
                {"en": "That cold beer tasted like pure, unadulterated liberty.", "cn": "那一瓶瓶冰镇啤酒的滋味，品尝起来就像是纯粹至极、不掺杂任何杂质的自由甘露。"},
                {"en": "Never surrender your innate ability to create unexpected wonder.", "cn": "永远不要缴械放弃你在困厄之中创造意想不到奇迹的与生俱来的天赋能力。"},
                {"en": "The memory of that warm afternoon remained etched forever in our weary souls.", "cn": "那个温暖午后微风微醺的画面，成为了永远镌刻在我们疲惫灵魂深处的永恒记忆。"}
            ]
        },
        {
            "title": "第 3 篇 · 图书馆里莫扎特的费加罗婚礼",
            "description": "紧闭播音室铁门，莫扎特的咏叹调回荡在整座监狱上空。",
            "sentences": [
                {"en": "I have no idea to this day what those two Italian ladies were singing about.", "cn": "直到今天，我也全然不知那两位意大利歌唱家女士在咏叹调里唱的究竟是些什么词句。"},
                {"en": "Truth is, I don't want to know. Some things are best left unspoken.", "cn": "但事实是，我压根就不想去深究。世间有些极致的美妙事物，最好还是留白莫言。"},
                {"en": "Their voices soared higher and farther than anybody in a grey place dares to dream.", "cn": "她们宛如天籁的嗓音凌空翱翔，飞扬得比这片灰色泥沼里任何人敢于梦寐以求的边界还要高远。"},
                {"en": "It was like some beautiful bird flapped into our drab little cage.", "cn": "那景象仿佛是一只斑斓绝伦的九天神鸟，猝不及防扇动羽翼飞入了我们灰暗狭窄的铁笼。"},
                {"en": "It made these stone walls dissolve into thin air for a fleeting second.", "cn": "它让肖申克高耸坚硬的万丈石墙，在转瞬之间彻底消融瓦解化作了无形清气。"},
                {"en": "Every last man in Shawshank felt a taste of divine freedom.", "cn": "肖申克大院里站着的每一个受苦受难的囚徒，都在那一刹那尝到了神圣自由的甘甜滋味。"},
                {"en": "Andy locked the broadcasting room door and leaned back in his swivel chair.", "cn": "安迪从里面反锁了广播控制室的厚重铁门，安详悠然地仰靠在旋转办公椅里闭目倾听。"},
                {"en": "He knew solitary confinement was coming, but he simply did not care.", "cn": "他心里很清楚等待自己的将是暗无天日的关禁闭惩罚，但他早已将其视作浮云完全不在乎。"},
                {"en": "Music is something inside you that they can never touch or take away.", "cn": "音乐是深藏于你灵魂内里最隐秘角落的瑰宝，任凭他们权势滔天也休想触碰或夺走半分。"},
                {"en": "In solitary, the music kept him company through the endless pitch-black nights.", "cn": "在黑不见五指的禁闭单人小黑屋里，正是这段天籁旋律陪伴着他度过了漫漫长夜。"},
                {"en": "Great art possesses the power to emancipate human spirits under any oppression.", "cn": "人类伟大的艺术瑰宝，拥有一种能够在任何严酷暴政压迫下彻底解放精神枷锁的神力。"},
                {"en": "You can lock a man's body, but his imagination remains boundless.", "cn": "你可以锁闭囚禁一个凡人的肉躯皮囊，但他的浩瀚想象力却永远如同星海般辽阔无垠。"},
                {"en": "The warden was pounding furiously on the glass, but the soprano sang on.", "cn": "典狱长在玻璃窗外气急败坏地疯狂拍打砸击，但那悠扬婉转的女高音依然高亢回荡长空。"},
                {"en": "Courage is demonstrating grace under the immediate threat of harsh retaliation.", "cn": "所谓真正的非凡勇气，就是即便面临狂风骤雨般的报复威胁，依然能够从容展现优雅。"},
                {"en": "That golden afternoon proved that beauty will forever conquer brute force.", "cn": "那个金黄灿烂的午后用事实雄辩地证明：人间至纯的大美，必将永远战胜蛮荒的暴力。"}
            ]
        },
        {
            "title": "第 4 篇 · 地质小石锤与十九年的凿壁",
            "description": "一把原本需要六百年才能凿穿的雕刻小锤，在坚韧的信念下创造奇迹。",
            "sentences": [
                {"en": "Andy asked me for a rock hammer, no bigger than six inches long.", "cn": "安迪私底下向我打听一把地质小石锤，长度不过短短六英寸大小。"},
                {"en": "I told him it would take six hundred years to tunnel through that thick prison wall.", "cn": "我直言不讳地警告他：要想用这么一把小玩意儿挖穿坚硬的花岗岩石墙，至少得花上整整六百年。"},
                {"en": "Geology is the study of pressure and time; that's all it takes.", "cn": "地质学本质上就是关于压强与漫长时光的学问；成就非凡大事，唯此二者足矣。"},
                {"en": "A small chisel in persistent hands can move the most formidable mountains.", "cn": "一把毫不起眼的微小凿刀握在矢志不渝的手中，终有一天能移平世间最巍峨险峻的高山。"},
                {"en": "Every morning in the exercise yard, he scattered pockets full of wall debris.", "cn": "每天清晨在操场放风散步时，他不动声色地将衣兜里装满的石墙碎屑泥沙抖落在操场泥土中。"},
                {"en": "Patience is not passive waiting; it is active endurance toward a resolute vision.", "cn": "真正的旷世耐心绝非消极被动的苦等；而是一种朝着既定宏伟愿景脚踏实地的韧性坚守。"},
                {"en": "Nineteen long years of silent scratching beneath the Rita Hayworth poster.", "cn": "在丽塔·海华丝巨幅电影海报的遮掩下，十九个漫漫寒暑如一日悄无声息地微弱刮凿。"},
                {"en": "He carved lovely chess pieces out of soft alabaster stones in the evening.", "cn": "每当夜幕降临，他还就着微弱的煤油灯光，把捡来的雪花软石细细雕琢成精美的小象棋子。"},
                {"en": "A sharp mind finds creative solutions where ordinary eyes see only despair.", "cn": "一颗敏锐机警的心智总能在绝处寻觅逢生契机，而平庸浅薄的凡胎肉眼却只能看到绝望。"},
                {"en": "Never underestimate a quiet soul armed with unwavering purpose.", "cn": "永远不要低估一个沉默寡言、却怀揣着不可动摇崇高目标的坚韧灵魂。"},
                {"en": "The stone gave way millimeter by millimeter to the steadfast will of a free man.", "cn": "在一介自由人坚如磐石的伟力意志面前，坚硬千年的花岗岩每一天都在毫米之间退让。"},
                {"en": "Discipline is choosing between what you desire now and what you desire most.", "cn": "所谓崇高的自律，就是在你当下贪恋的蝇头微利与你此生最渴望的终极宏愿之间做出决断。"},
                {"en": "He kept his secret safe from the guards, the inmates, and the darkness.", "cn": "他将这个足以惊天动地的惊天大秘密，妥善瞒过了狱警、囚徒以及无边无际的黑夜。"},
                {"en": "Hope is not wishful thinking; hope is a daily chisel against an immovable barrier.", "cn": "希望绝不是好高骛远的空想；希望就是日复一日向着看似不可动摇的高墙挥动凿击。"},
                {"en": "The storm of justice was quietly brewing behind that paper picture on the wall.", "cn": "一曲正义复仇与奔向光明的风暴交响乐，正悄然在墙上那张薄薄的画卷背后汹涌酝酿。"}
            ]
        },
        {
            "title": "第 5 篇 · 穿过五百码污浊下水道的救赎",
            "description": "爬过五个足球场长度的人间污秽，在暴雨雷鸣中张开双臂迎接新生。",
            "sentences": [
                {"en": "Andy Dufresne crawled through five hundred yards of foul filth I can't even stomach imagining.", "cn": "安迪·杜弗兰爬过了整整五百码连我想一想都忍不住恶心作呕的污浊恶臭下水道管。"},
                {"en": "Five hundred yards: that is the length of nearly five football fields combined.", "cn": "整整五百码的漫长距离啊：那几乎相当于五个正规美式足球场连缀起来的漫长总和。"},
                {"en": "He crawled through sewage pipe and came out clean on the other side.", "cn": "他独自匍匐爬过暗无天日充满污秽的排污死水管道，却在另一端纯洁无瑕地重获了新生。"},
                {"en": "The pouring rain washed away the prison grime from his skin and clothes.", "cn": "漫天倾盆瓢泼的大雨无情浇灌而下，彻底冲刷洗净了他身上残存的所有铁窗牢狱污垢。"},
                {"en": "He tore off his prison shirt and raised both arms into the lightning sky.", "cn": "他奋力撕扯掉那件象征耻辱囚徒身份的蓝白条纹衬衫，在电闪雷鸣中昂首向苍天张开双臂。(影史第一名场面)"},
                {"en": "That is the iconic posture of a resurrected soul reclaiming divine sovereignty.", "cn": "那是灵魂重获新生涅槃、向浩瀚宇宙重新宣告自己神圣主权的最壮美传世姿态。"},
                {"en": "He was finally free, truly and utterly free beneath God's tempest.", "cn": "在上帝暴风雨洗礼的苍穹之下，他终于彻彻底底、不折不扣地成为了一个自由的人。"},
                {"en": "Sometimes you have to wade through hell to reach the gates of paradise.", "cn": "人这一生有时就是这样，你必须只身蹚过炼狱深渊，方能真正叩响通往天堂的大门。"},
                {"en": "No corruption could stain the crystal purity of his indomitable heart.", "cn": "尘世间任何黑暗龌龊的贪腐罪恶，都休想玷污他那颗坚韧纯澈如琉璃般的赤子之心。"},
                {"en": "The warden opened the empty cell the next morning and stared in disbelief.", "cn": "翌日清晨典狱长亲自推开空无一人的死寂牢房，目瞪口呆地陷入了不可思议的惊骇之中。"},
                {"en": "Salvation lay within, inscribed on the hollow pages of the Holy Bible.", "cn": "得救之道就在其中——那柄暗藏在《圣经》镂空书页间的小石锤无情嘲讽着伪善罪恶。"},
                {"en": "Justice may sleep for a season, but its lightning strike is inevitable and absolute.", "cn": "天道正义也许会偶尔沉睡一季，但它的晴空霹雳轰鸣一击必将到来，且绝对无可逃遁。"},
                {"en": "He outsmarted a corrupt empire using nothing but patience and meticulous intellect.", "cn": "他仅仅凭借着超凡脱俗的坚韧耐心与缜密无缺的高超智识，彻底击垮了一个腐朽残暴的帝国。"},
                {"en": "The taste of freedom in your lungs is sweeter than anything this earth possesses.", "cn": "当你大口将久违的自由空气吸入肺腑之中时，其甘冽香甜胜过这凡尘俗世所拥有的一切。"},
                {"en": "A bird whose wings were made for soaring can never be constrained by iron.", "cn": "那些天生便注定要振翅高翔于九霄云外的灵禽神鸟，钢铁囚笼休想困住它哪怕一分一秒。"}
            ]
        },
        {
            "title": "第 6 篇 · 橡树下的铁盒子与给瑞德的信",
            "description": "在巴克斯顿开满野花的大橡树石墙下，埋藏着关于未来的希望之约。",
            "sentences": [
                {"en": "There is a big hayfield up near Buxton; you will find a magnificent oak tree there.", "cn": "在巴克斯顿附近有一片开阔辽远的干草牧场；你会在那里找到一棵独一无二的壮丽大橡树。"},
                {"en": "It has got a long stone wall along the edge, looking like something out of a Robert Frost poem.", "cn": "在草场边缘绵延着一道古老的黑色矮石墙，静谧得宛如直接从罗伯特·弗罗斯特的优美抒情诗篇中走出来的一样。"},
                {"en": "At the base of that wall, there is a rock that has no earthly business in a Maine field.", "cn": "在那道石墙的最基部，埋藏着一块本不该出现在缅因州田野里的奇特黑色火山玻璃岩石。"},
                {"en": "Underneath that volcanic rock lies a small black metal box containing a key.", "cn": "在深埋的那块火山岩石正下方，静静安放着一只盛放着关键钥匙的漆黑金属铁盒子。"},
                {"en": "Dear Red: if you are reading this, it means you got out and found the stone.", "cn": "亲爱的瑞德：如果你此刻正在阅读这封信，这意味着你已经重获自由，并顺利找到了这块基石。"},
                {"en": "And if you have come this far, maybe you're willing to come a little further.", "cn": "既然你已经坚持跋涉走了这么远的路程，那么也许你愿意再迈出步伐，与我相约走得更远一些。"},
                {"en": "You remember the name of the quiet coastal town in Mexico, don't you?", "cn": "你一定还牢牢铭记着那个位于墨西哥沿岸静谧温暖的海滨小镇的名字，不是吗？"},
                {"en": "Zihuatanejo: warm waters, endless blue, and a place where past sins are forgotten.", "cn": "芝华塔尼欧：温暖蔚蓝的海水、无边无际的晴空，以及一个能让往昔所有罪孽痛苦尽皆遗忘的原乡。"},
                {"en": "I could use a good man to help me get my project on the boat moving.", "cn": "我的木头捕鱼船修复工程迫切需要一个像你这样靠谱忠诚的好帮手来共同搭把手。"},
                {"en": "I'll be keeping an eye out for you every single afternoon on the beach.", "cn": "在每天下午暖阳下的金色沙滩上，我都会久久驻足远眺，期盼着你归来的身影。"},
                {"en": "Remember, Red: hope is a good thing, maybe the best of things.", "cn": "记住啊，瑞德：希望是件美好的东西，甚至可以说是这人间至善至纯的事物。"},
                {"en": "And no good thing ever dies.", "cn": "而世间所有美好的至善之物，是永远永远都不会消逝磨灭的。(传世金句)"},
                {"en": "I hope you are strong, I hope you find joy, and I hope to see you soon.", "cn": "我由衷祈愿你身强体健，祈愿你重获欢愉，更热切祈愿能在不久的将来与你再次把酒言欢。"},
                {"en": "Your friend, Andy.", "cn": "你一生最挚爱的老朋友，安迪·杜弗兰手书。"},
                {"en": "A promise kept across decades of hardship is the holiest monument of friendship.", "cn": "历经数十载风霜苦难而矢志坚守的一纸诺言，是人类友谊丰碑上最圣洁不朽的勋章。"}
            ]
        },
        {
            "title": "第 7 篇 · 太平洋的蓝：芝华塔尼欧海滩",
            "description": "坐上一辆开往边境的长途大巴，去拥抱梦中碧蓝无垠的太平洋。",
            "sentences": [
                {"en": "Get busy living, or get busy dying.", "cn": "忙着去活，或者忙着去死。(全片振聋发聩之声)"},
                {"en": "That is goddamn right. I have made my choice for the remainder of my days.", "cn": "这话说得太他妈千真万确了。对于我行将就木的余生，我已经做出了属于我自己的决断。"},
                {"en": "For the second time in my life, I committed a crime: breaking my parole conditions.", "cn": "这是我这辈子第二次犯下罪行：公然违反假释监督条例，跨越州界奔赴远方。"},
                {"en": "I doubt they'll put up any roadblocks for an old crook like me.", "cn": "但我很怀疑他们是否真会为了我这么一个风烛残年的老犯人，大动干戈设立什么路障通缉。"},
                {"en": "I find I am so excited, I can barely sit still or hold a single thought in my head.", "cn": "我发觉自己竟然兴奋激动得坐立难安，脑海中浮想联翩几乎无法定下神来思考任何单一念头。"},
                {"en": "I think it is the excitement only a truly free man can feel in his veins.", "cn": "我想，这种在血管里激荡沸腾的颤栗与喜悦，唯有真正挣脱枷锁的自由人才能深切体悟。"},
                {"en": "A free man starting at the beginning of a long journey whose conclusion is uncertain.", "cn": "一个自由人，正屹立在一段漫长旅程的全新起点上，而旅途的终局虽然未定，却充满无限可能。"},
                {"en": "I hope I can make it across the southern border without incident.", "cn": "我衷心祈求自己能够平平安安顺顺利利穿越南部国境线。"},
                {"en": "I hope to see my dear friend Andy and shake his warm hand in the sunshine.", "cn": "我热切期盼着能亲眼见到我亲爱的挚友安迪，在和煦阳光下紧紧握一握他那双温暖有力的手。"},
                {"en": "I hope the Pacific Ocean is as blue as it has been in all my wildest dreams.", "cn": "我由衷期盼那片浩瀚无垠的太平洋海水，正如在我往昔所有最绚烂梦境中那样澄澈蔚蓝。"},
                {"en": "I hope.", "cn": "我怀抱希望。(影史最美独白终句)"},
                {"en": "The bus drove along the dusty highway toward freedom and endless horizons.", "cn": "长途大巴沿着扬起尘土的开阔公路全速飞驰，奔向光明自由与无边无际的金色地平线。"},
                {"en": "On that blindingly white tropical shore, two old friends embraced under the warm Mexican sky.", "cn": "在那片耀眼洁白的热带沙滩上，两位历尽沧桑的老友在墨西哥明媚温暖的晴空下紧紧相拥。"},
                {"en": "No words were necessary; the ocean surf sang the anthem of their redemption.", "cn": "此时此刻千言万语皆成多余；浩荡翻涌的太平洋白浪，正为他们的苦难救赎高唱永恒赞歌。"},
                {"en": "True freedom is discovering a place where your spirit can breathe without fear.", "cn": "所谓真正的自由，就是在天地之间觅得一处港湾，让你的灵魂得以无所畏惧地大口呼吸。"}
            ]
        },
        {
            "title": "第 8 篇 · 典狱长诺顿的伪善与审判",
            "description": "手握圣经心如毒蝎，正义的审判如雷霆降临肖申克。",
            "sentences": [
                {"en": "I believe in two things: discipline and the Bible. Here you will receive both.", "cn": "在肖申克我只信仰两件事：铁的纪律和圣经。在这里你们两样都将领受。(典狱长伪善开场白)"},
                {"en": "His judgment cometh and that right soon.", "cn": "主的审判即将临到，且必速速临到。(办公室讽刺挂牌)"},
                {"en": "Behind the mask of Christian piety was a cold and calculating greed.", "cn": "在虚伪虔诚的基督徒伪装面具之下，潜藏着一颗阴险算计、贪婪成性的蛇蝎之心。"},
                {"en": "He forced Andy to launder hundreds of thousands of dollars in dirty kickbacks.", "cn": "他仗着滔天权势，强迫精通财务的安迪替他洗白数以数十万计的肮脏承包回扣黑金。"},
                {"en": "Tommy Williams told the absolute truth about who murdered Andy's wife.", "cn": "年轻囚犯汤米·威廉姆斯吐露了关于到底是谁残忍杀害安迪妻子的全部铁证真相。"},
                {"en": "The ruthless warden silenced the innocent young witness without a single hesitation.", "cn": "残暴狠毒的典狱长为了封口掩盖丑闻，毫无半分犹豫便痛下杀手除掉了年轻无辜的证人。"},
                {"en": "Tyrants mistakenly believe their power can suppress the righteous truth forever.", "cn": "独裁暴君总是狂妄盲目地以为，凭借手中的强权就能永久将正义真相一手遮天掩盖压制。"},
                {"en": "Andy took the phantom ledger book and shipped the evidence directly to the newspapers.", "cn": "安迪在越狱时带走了记载所有受贿罪证的幽灵账本，并将全套铁证如山直接寄给了波士顿各大报社。"},
                {"en": "The headlines exposed decades of brutal corruption inside Shawshank's gray walls.", "cn": "头条重磅新闻将肖申克灰色石墙内隐匿数十载的血腥贪腐内幕，大白于天下人眼前。"},
                {"en": "State police sirens echoed outside the warden's locked office door.", "cn": "全州巡警尖锐刺耳的警笛呼啸声，如丧钟般回荡在典狱长反锁的办公室大门之外。"},
                {"en": "He looked at the framed verse on the wall as his wicked kingdom crumbled.", "cn": "在他罪恶的独立王国轰然倒塌崩解之际，他绝望地凝视着墙上那块曾用以粉饰太平的圣经牌匾。"},
                {"en": "A coward takes his own life when faced with public exposure of guilt.", "cn": "当不得不赤裸裸直面昭然若揭的滔天罪行与公义审判时，懦夫选择了饮弹自尽。"},
                {"en": "Evil carries within itself the seeds of its own inescapable destruction.", "cn": "所有的罪孽邪恶，其自身骨髓里原本就孕育着走向无可逃遁自我灭亡的毁灭种子。"},
                {"en": "No amount of embezzled wealth can purchase pardon for a murdered innocent.", "cn": "任凭你侵吞搜刮了多少金山银山，也休想用不义之财买得残害无辜性命的救赎宽恕。"},
                {"en": "Integrity outlives tyranny every single time in the grand arc of history.", "cn": "在滚滚向前的人类漫长历史长河之中，光明浩然正气必将每一次都彻底熬死残暴专制。"}
            ]
        },
        {
            "title": "第 9 篇 · 伯鲁克斯的告别与体制化的悲剧",
            "description": "老图书管理员伯鲁克斯被假释后的迷茫与社会脱节之殇。",
            "sentences": [
                {"en": "Brooks Hatlen was here.", "cn": "老布鲁克斯曾到此一游。(墙板上催人泪下的刻字)"},
                {"en": "He spent fifty long years behind these walls; the outside world terrified him.", "cn": "他在这堵铁窗高墙内度过了整整五十个春秋；外面日新月异的现实世界让他感到惊恐万状。"},
                {"en": "The world went and got itself in a big damn hurry while I was locked away.", "cn": "在我被与世隔绝锁闭在里面的这大半辈子间，整个外面的世界变得匆匆忙忙、急躁得要命。"},
                {"en": "Automobiles everywhere, people moving fast, never stopping to look at the trees.", "cn": "满大街川流不息都是飞驰的汽车，行人们脚步匆匆疾驰而过，从来没有人停下脚步看一眼树木。"},
                {"en": "In here, he was an educated librarian who had respect and purpose.", "cn": "在监狱高墙这方小天地里，他是一位受人尊崇、通晓图书管理、满怀人生意义的智者老爷爷。"},
                {"en": "Out there, he was just an old paroled felon with arthritis and bad hips.", "cn": "可一旦被放逐到外面广阔的人海中，他不过是一个患有严重关节炎、连重物都拎不动的假释糟老头。"},
                {"en": "He bagged groceries at the supermarket, his hands shaking with constant anxiety.", "cn": "他在连锁超市里替顾客装纸袋杂货，双手因内心深处挥之不去的惶恐不安而止不住颤抖。"},
                {"en": "Every night he lay awake listening to sirens, longing for the quiet security of his old cell.", "cn": "每个夜晚他孤身一人躺在昏暗的廉租房小床上听着窗外呼啸的警笛，发疯般渴望回到过去牢房那份熟悉的宁静安稳。"},
                {"en": "He fed the wild pigeons in the park, hoping his pet bird Jake was doing well.", "cn": "他天天跑到街心公园给野鸽子喂面包屑，心里暗暗期盼着自己曾经亲手放生的飞鸟杰克一切安好。"},
                {"en": "A man can become so attached to his chains that freedom feels like exile.", "cn": "一个人有时竟会对自己身上的锁链产生如此深入骨髓的依恋，以至于自由降临的那一刻，反而感觉像是一场残忍的流放。"},
                {"en": "He put on his best suit, carved his simple farewell, and stepped into eternity.", "cn": "他穿戴整齐自己体面完好的那一套旧西装，在横梁木板上刻下了质朴的遗言告别，从容迈入了永恒之中。"},
                {"en": "Institutionalization is a silent tragedy that claims the heart before the body fails.", "cn": "所谓体制化是一桩无声无息的人间悲剧，在你的肉躯彻底朽烂之前，它早已悄悄杀死了你的心灵。"},
                {"en": "We wept for Brooks because we knew his tragic fate could easily be our own.", "cn": "我们所有在押的囚友都为老布的悲惨谢幕痛哭流涕，因为我们心知肚明，他的悲剧下场随时可能降临在我们每一个人头上。"},
                {"en": "True rehabilitation must restore a human being's independence, not just extinguish their past.", "cn": "真正人道健全的刑罚再造，必须重新赋予一个人独立自足的生存能力，而非仅仅将其往昔连根拔除抹杀。"},
                {"en": "May his gentle soul finally discover the peace that eluded him on earth.", "cn": "愿他善良温厚的脆弱灵魂，终能在天国寻得那份在这薄情尘世间苦苦追寻而不得的永久宁静。"}
            ]
        },
        {
            "title": "第 10 篇 · 唯有希望与美好的事物永不消逝",
            "description": "重温影史第一神作核心独白总复盘，让信念穿越漫漫风雨。",
            "sentences": [
                {"en": "Some birds aren't meant to be caged, that's all. Their feathers are just too bright.", "cn": "世上有些鸟儿是注定关不住的，它们的每一片羽毛都闪耀着太夺目灿烂的光辉。(传世总结)"},
                {"en": "And when they fly away, the part of you that knows it was a sin to lock them up does rejoice.", "cn": "当它们展开双翼傲然飞向长空时，你内心深处明白将其关进铁笼本就是一种罪孽的那部分良知，必会由衷感到欣慰欢喜。"},
                {"en": "Still, the place you live in is that much more drab and empty that they're gone.", "cn": "然而，它们一旦展翅飞走之后，你所栖身的这个灰暗角落，却也因它们的离去而显得格外死寂空虚落寞。"},
                {"en": "I guess I just miss my friend.", "cn": "我想，我只是太想念我那位了不起的老朋友罢了。(全剧最真挚男儿深情)"},
                {"en": "A man needs something to believe in, or the winter of the soul will freeze him whole.", "cn": "人这一辈子总得坚信点什么崇高的东西，否则心灵漫漫的刺骨寒冬终将把他整个人彻底冻僵窒息。"},
                {"en": "Fear can hold you prisoner; hope can set you free.", "cn": "恐惧能将你永远囚禁在黑暗牢笼之中；而希望，能赋予你翱翔长空的绝对自由。(传世箴言)"},
                {"en": "No matter how thick the stone walls of your circumstance may appear today.", "cn": "无论你当下人生所遭遇的现实逆境石墙看起来是多么坚不可摧、厚重绝望。"},
                {"en": "A determined spirit backed by patience will carve through any mountain.", "cn": "一个心怀坚韧决绝、拥有无限耐心的顽强灵魂，终将凿穿劈开横亘在眼前的一切艰难险阻。"},
                {"en": "Live with honor, treat your brothers with compassion, and never accept defeat.", "cn": "活出凛然的尊严与傲骨，用无私的同理心善待身边的同伴手足，永远不要向厄运低头认输。"},
                {"en": "Keep digging your tunnel quietly while the rest of the world is fast asleep.", "cn": "当整个浮躁的世界都在昏睡懈怠之际，静下心来，默默在黑暗深处挖掘属于你自己的光明通道。"},
                {"en": "The dawn comes slowly, but its brilliant rays are inexorable and unstoppable.", "cn": "破晓的拂晓黎明虽然步履迟缓，但它喷薄而出的万道璀璨霞光，却势不可挡、万物莫御。"},
                {"en": "Pack your bags of courage and prepare yourself for the call of the great Pacific blue.", "cn": "收拾好你那装满无畏勇气的行囊吧，随时准备好去迎接远方那片属于你的湛蓝太平洋的深情呼唤。"},
                {"en": "Walk tall as if you already own the boundless sky above your head.", "cn": "挺起胸膛昂首阔步吧，就宛如你早已真正拥有了头顶那片浩瀚无垠的蔚蓝晴空一样。"},
                {"en": "To all who suffer in darkness: may your redemption arrive like gentle, cleansing rain.", "cn": "致所有在漫漫长夜与黑暗磨难中受苦忍耐的人们：愿属于你们的救赎甘霖，如春风化雨般降临凡间。"},
                {"en": "Hope is eternal, and the free spirit of mankind will triumph forevermore.", "cn": "希望永存人间，人类追求自由解放的不屈精神，必将万世长存、永铸辉煌！"}
            ]
        }
    ]))

    # 4. 《寻梦环游记》(Coco)
    courses.append(build_course({
        "id": "course-mov-coco",
        "title": "《寻梦环游记》(Coco) · 爱与记忆温情原声 (10章全集)",
        "category": "movies",
        "categoryName": "影视英语",
        "coverGradient": "from-orange-500 via-amber-600 to-purple-800",
        "icon": "🎸",
        "description": "皮克斯奥斯卡双奖神作，墨西哥万寿菊之桥，探讨死亡、音乐、梦想与家庭的永恒羁绊。",
        "difficulty": "入门 A1",
        "tags": ["皮克斯神作", "爱与记忆", "音乐梦想", "催泪温情"]
    }, [
        {
            "title": "第 1 幕 · 万寿菊之桥与亡灵节传统",
            "description": "铺满金黄万寿菊花瓣的绚烂桥梁，连通着生者与逝者的思念。",
            "sentences": [
                {"en": "Día de Muertos is the one night of the year our ancestors come to visit us.", "cn": "亡灵节是一年之中我们逝去先祖们跨越生死重返人间探望我们的唯一夜晚。"},
                {"en": "The marigold bridge connects the Land of the Living with the Land of the Dead.", "cn": "那座铺满万寿菊金黄花瓣的璀璨桥梁，连通着生者的人间与亡灵的国度。"},
                {"en": "If our photo is not placed on the ofrenda, we cannot cross over the flower bridge.", "cn": "如果我们的相片没有被供奉在灵坛祭台上，我们就无法迈步跨过那座花瓣桥。"},
                {"en": "Never underestimate the unbreakable spiritual bonds of Mexican ancestral heritage.", "cn": "永远不要轻视墨西哥古老先祖遗风血脉相承中那坚不可摧的精神羁绊。"},
                {"en": "Candles flicker along the quiet cobblestone path to guide lost souls back home.", "cn": "跳跃的烛光沿着静谧古老的青石小径摇曳生姿，指引着迷途的魂灵安然回家。"},
                {"en": "Music has been forbidden in our shoemaking household for generations.", "cn": "在由曾曾祖母亲手创办的制鞋家族门第中，音乐早已被严厉禁绝了数代人之久。"},
                {"en": "I don't care about making shoes; my beating heart yearns only for sweet melodies.", "cn": "我根本不在乎怎样做皮鞋；我胸膛里跳动的心脏唯独对甜美的旋律魂牵梦绕。"},
                {"en": "Ernesto de la Cruz was the greatest musical artist Mexico ever produced.", "cn": "埃内斯托·德拉库斯是墨西哥大地上有史以来诞生过的最伟大的音乐艺术家。"},
                {"en": "He seized his artistic moment, and I am determined to seize mine as well.", "cn": "他牢牢把握住了属于他自己的艺术高光时刻，而我也决意抓住属于我的闪耀瞬间。"},
                {"en": "Strumming that skull-adorned white guitar transported me into another mystical dimension.", "cn": "当我情不自禁拨动那把雕刻着骷髅花纹的白色吉他琴弦时，奇迹般穿越进了另一个神秘维度。"},
                {"en": "The skeletons walking among the living are kind, festive, and full of joyful vitality.", "cn": "那些在人间穿行的骷髅亡灵们个个善良热忱、盛装打扮，洋溢着欢快蓬勃的生机。"},
                {"en": "Respecting your lineage does not mean you must sacrifice your personal calling.", "cn": "尊崇孝敬你的家族血脉，绝不意味着你必须残忍牺牲你自己内心的神圣天职召唤。"},
                {"en": "Every petal on this radiant pathway carries a loving prayer from the earth.", "cn": "在这条绚丽夺目的桥梁小径上，每一片飘落的花瓣都承载着人间尘世深情的祈祷。"},
                {"en": "The celebration of remembrance turns natural human grief into everlasting joy.", "cn": "这一场关于追思与缅怀的盛大庆典，将人类本能的伤感悲痛转化为了永恒的欢欣喜悦。"},
                {"en": "A boy with a passionate dream can soften even the most stubborn ancestral traditions.", "cn": "一个心怀炽热纯真梦想的小男孩，终能感化融解这世间最顽固刻板的家族陈规旧习。"}
            ]
        },
        {
            "title": "第 2 幕 · 真正的死亡是被世人遗忘",
            "description": "探讨生命的终极真相：肉体的消逝不是终点，彻底遗忘才是真正的死亡。",
            "sentences": [
                {"en": "The real death is that no one in the living world remembers you anymore.", "cn": "所谓真正的死亡，是活着的现实世界里再也没有一个人心怀思念记挂着你了。(传世名言)"},
                {"en": "Our existence in this magical twilight realm depends entirely upon mortal memories.", "cn": "我们在这座奇幻暮色国度里的继续存在，完完全全仰仗着凡尘俗世人们心头的记忆。"},
                {"en": "When there is no one left to tell your story, you disappear like gentle stardust.", "cn": "当人世间再也没有人留存传述关于你的故事时，你就会如温润的星尘般彻底消散无痕。"},
                {"en": "Héctor wanted only one thing: to see his darling little daughter Coco one last time.", "cn": "埃克托尔漂泊孤寂的灵魂别无所求：唯求能最后看一眼他凡间挚爱的小女儿可可。"},
                {"en": "He sang lullabies softly by her bedside before boarding the fatal traveling train.", "cn": "在踏上那趟宿命般不归路的离家火车之前，他曾在女儿床边轻声哼唱过无数动听的摇篮曲。"},
                {"en": "Selfish ambition blinded De la Cruz into poisoning his truest musical collaborator.", "cn": "自私虚荣的野心蒙蔽了德拉库斯的双眼，竟残忍下毒谋害了他最真诚的音乐创作合伙人。"},
                {"en": "Plagiarizing another artist's soul songs is the foulest theft known to humanity.", "cn": "将另一位艺术家倾注灵魂创作的心血名曲据为己有剽窃盗用，是全人类最可耻的盗窃。"},
                {"en": "Truth may be concealed beneath glamour, but genuine authenticity always rises to light.", "cn": "真相或许会被浮华虚妄的聚光灯暂时掩盖，但纯真赤诚的光芒必将破晓穿透阴霾。"},
                {"en": "A painted guitar cannot disguise the hollow heart of an opportunistic villain.", "cn": "一把描金画彩的精美吉他，掩盖不了一个投机钻营恶棍空洞丑陋的内心。"},
                {"en": "The songs that conquer eternity are written from genuine familial devotion.", "cn": "那些能够真正征服沧桑永恒的传世颂歌，无一例外皆脱胎于对家人真挚纯粹的深情。"},
                {"en": "Never judge a grandfather by his ragged clothes or desperate social station.", "cn": "永远不要仅凭一个人衣衫褴褛的外表，或是落魄潦倒的处境去评判一位长辈的崇高灵魂。"},
                {"en": "Love outlasts fame, wealth, monuments, and all earthly physical structures.", "cn": "爱比浮名虚誉、金银财宝、巍峨纪念碑以及尘世间所有肉眼可见的物理建筑都要恒久远长。"},
                {"en": "Every photograph preserved in an album is a lifeline against total oblivion.", "cn": "珍藏在家庭相册里的每一张泛黄老照片，都是抵御彻底虚无遗忘的一根神圣生命纽带。"},
                {"en": "To be remembered with affection is the supreme achievement of any mortal lifespan.", "cn": "能在死后依然被后人满怀深情地铭记缅怀，是任何凡人短暂一生所能达成的至高荣耀。"},
                {"en": "Sing with your pure spirit, and your melody will cross the boundary of life and death.", "cn": "用你纯洁无瑕的心灵歌唱吧，你的歌声必将跨越生与死那道不可逾越的森严界限。"}
            ]
        },
        {
            "title": "第 3 幕 · 曾曾祖母的祝福与无条件的爱",
            "description": "伊梅尔达曾曾祖母解除音乐禁令，给予米格尔不附加任何条件的深情祝福。",
            "sentences": [
                {"en": "I give you our ancestral blessing to return home, with no conditions attached.", "cn": "我赋予你跨越阴阳重返人间的家族先祖神圣祝福，而且这一次，不附加任何苛刻条件！"},
                {"en": "Family always comes first, but your heartfelt passion belongs to your core self.", "cn": "家人永远处于至高无上的第一位，但你心底炽热的热爱同样属于你最核心的本真自我。"},
                {"en": "The giant winged Alebrije named Pepita leaped across the neon rooftop towers.", "cn": "那只长着斑斓巨翼、名为佩皮塔的神圣灵兽大猫，威风凛凛腾空跃过霓虹闪烁的塔楼尖顶。"},
                {"en": "Spiritual spirit guides guard our families through dangerous subterranean labyrinths.", "cn": "神圣灵兽守护使者会在凶险莫测的地下迷宫深渊中，一路护佑守卫着我们家族的血脉后人。"},
                {"en": "Forgiveness does not erase historical betrayal, but it unties emotional chains.", "cn": "宽恕与释怀虽然无法抹杀往昔残酷的背叛伤痕，却能彻底解开彼此心头深锁的情感枷锁。"},
                {"en": "She sang with thunderous vocal power and reclaimed her joy upon the grand festival stage.", "cn": "在盛大的庆典舞台中央，她重新展露惊艳全场的磅礴歌喉，寻回了久违深藏的由衷欢愉。"},
                {"en": "A fractured family can reunite across generations when honest communication happens.", "cn": "当坦率真诚的心灵沟通真正发生时，哪怕四分五裂分崩离析的家族亦能跨越数代重归于好。"},
                {"en": "Hold onto the sacred petal until dawn breaks across the misty horizon.", "cn": "把那枚浸润着先祖祝福的神圣万寿菊花瓣紧紧握在掌心，直到晨曦破晓照亮薄雾地平线。"},
                {"en": "Our ancestors watch over our steps with proud and encouraging celestial eyes.", "cn": "长眠在天国的历代先祖们，正用充满自豪骄傲与温厚鼓励的目光，静静注视着我们迈出的每一步。"},
                {"en": "Traditional craftsmanship and artistic expression can flourish harmoniously together.", "cn": "严谨务实的传统手工制鞋技艺与奔放热烈的音乐艺术表达，原本就可以在这世间比翼齐飞。"},
                {"en": "A grandmother's protective ferocity is born out of profound maternal tenderness.", "cn": "一位长辈看似泼辣严苛的家庭保护欲，归根结底皆源自于骨子里那份深沉无私的母性至爱。"},
                {"en": "No rift is too wide for a genuine musical apology to mend.", "cn": "世间再深不见底的情感裂痕，也抵不过一首发自肺腑赤诚的音乐道歉所带来的神奇愈合。"},
                {"en": "Celebrate the ancestors who paved the bumpy road for your current flourishing life.", "cn": "为那些曾经在泥泞坎坷中开辟荒野道路、方才换来你今日富足安宁生活的先祖们欢庆致敬吧。"},
                {"en": "Family loyalty is not a prison cell; it is the protective soil for your roots.", "cn": "对家族的忠诚与眷恋绝非禁锢你的牢笼；它恰恰是你茁壮成长、生生不息的最深厚沃土。"},
                {"en": "Step through the golden petal mist and carry our undying blessings to the sunlit world.", "cn": "大步迈过那团金黄灿烂的花瓣朝雾吧，将我们永不磨灭的炽烈祝福带回阳光普照的人间！"}
            ]
        },
        {
            "title": "第 4 幕 · 《Remember Me》唤醒可可曾祖母的记忆",
            "description": "拨动琴弦低声吟唱，那首父亲写给女儿的摇篮曲唤醒了沉睡的温暖记忆。",
            "sentences": [
                {"en": "Remember me though I have to say goodbye; remember me, don't let it make you cry.", "cn": "请记住我，虽然我不得不踏上离别的路途；请记住我，不要让思念使你眼眶泛起泪花。(影史名曲)"},
                {"en": "For even if I'm far away, I hold you in my heart; I sing a secret song to you.", "cn": "因为纵使我身在千山万水之外，我依然将你深拥在心间；在每一个思念的夜晚为你轻唱这首私密的歌。"},
                {"en": "The elderly grandmother's clouded eyes suddenly sparkled with vivid, loving recognition.", "cn": "风烛残年、眼神浑浊的可可曾祖母眼眸中，忽然奇迹般闪烁起清晰璀璨、饱含深情的相认光芒。"},
                {"en": "My papa used to sing that song to me when I was just a little girl in braids.", "cn": "我的亲生爸爸在我还是个扎着麻花小辫子的小姑娘时，总喜欢坐在床头给我唱这首歌。"},
                {"en": "She pulled the hidden torn photograph piece from her wooden dresser drawer.", "cn": "她伸出颤巍巍的苍老双手，从梳妆台木抽屉深处取出了那张珍藏了一生的泛黄缺失相片残角。"},
                {"en": "A daughter never forgets the melodic tenderness of a devoted, loving father.", "cn": "一个女儿哪怕在垂暮之年，也绝对不会遗忘父亲当年那份倾注于旋律之中的极致温存。"},
                {"en": "The entire household wept tears of redemption, joy, and breathtaking clarity.", "cn": "聚集在房门前的一整个大家庭所有人，都在那一刹那流下了关于救赎、释怀与大团圆的喜悦泪水。"},
                {"en": "Music unlocked the sealed treasury of her fading childhood recollections.", "cn": "纯粹动人的音符与歌声，奇迹般叩开了她原本行将彻底消逝衰退的童年温存记忆宝库。"},
                {"en": "Héctor's soul was saved from fading away in the Land of the Dead at that exact instant.", "cn": "就在这千钧一发的同一瞬间，埃克托尔飘摇脆弱的灵魂从亡灵国度彻底烟消云散的边缘被奇迹拯救了。"},
                {"en": "A song composed with pure paternal devotion possesses the strength to defy time itself.", "cn": "一首饱含纯真崇高父爱的传世乐章，拥有一种足以抗衡无情光阴冲刷的超凡伟力。"},
                {"en": "Family bonds are restored not by harsh discipline, but by shared vulnerable tenderness.", "cn": "让家庭关系重归于好的终极灵药，绝非严苛教条的规训，而是彼此坦诚展露那份柔软的温存。"},
                {"en": "The letters he wrote to his beloved daughter proved his innocence beyond all doubt.", "cn": "那一叠珍藏数十载写给挚爱女儿的亲笔家书手稿，毋庸置疑地向世人洗刷昭雪了他的全部清白。"},
                {"en": "Her wrinkled face lit up with the radiant smile of a happy young child once more.", "cn": "她那张布满岁月沟壑的慈祥面庞上，再一次绽放出了宛如无忧无虑孩童般的灿烂明媚笑容。"},
                {"en": "Love preserved in a simple lullaby is the most resilient force in the universe.", "cn": "封存在一首简单朴素摇篮曲之中的深沉大爱，是这浩瀚宇宙之中最具坚韧生命力的无敌力量。"},
                {"en": "Sing proudly, little Miguel; your guitar has mended generations of broken hearts.", "cn": "昂首骄傲地放声歌唱吧，小米格尔；你手中的吉他琴弦，已经奇迹般缝合了数代人破碎的心灵。"}
            ]
        },
        {
            "title": "第 5 幕 · 永恒的家族羁绊与祭台合影",
            "description": "一年后的亡灵节，一家人在绚烂的节日庆典中欢歌笑语，爱永不落幕。",
            "sentences": [
                {"en": "The following year, Héctor's portrait was proudly displayed at the very center of the altar.", "cn": "在翌年崭新的亡灵节上，埃克托尔手持吉他的神采飞扬相片，被骄傲端正地供奉在灵坛最中央。"},
                {"en": "Coco joined her loving parents on the other side, dancing joyfully among the stars.", "cn": "慈祥的老曾祖母可可也已经安详踏上了彼岸归途，在群星闪耀的繁花国度里与父母欢快起舞相拥。"},
                {"en": "Little sister joined the family band, tapping her tiny feet to the energetic rhythm.", "cn": "刚刚学会走路的可爱小妹妹也加入了家庭乐队，迈着蹒跚的小步子随着欢快奔放的节拍律动。"},
                {"en": "The guitar and the shoemaking hammer now hang together in peace on the workshop wall.", "cn": "如今，象征艺术梦想的吉他与象征踏实勤劳的制鞋铁锤，在工坊墙壁上相得益彰地并肩悬挂。"},
                {"en": "Never be afraid to honor your uniqueness while cherishing your ancestral heritage.", "cn": "在深情珍视你的家族血脉传统的同时，永远不要畏惧去勇敢活出属于你自己的独特个性和风采。"},
                {"en": "The dead are never truly absent; they walk beside us in every note we play.", "cn": "逝去的至亲挚爱从未真正离开；在我们指尖弹拨出的每一个动人音符中，他们都始终陪伴在身旁。"},
                {"en": "Festive papel picado paper banners flutter merrily in the warm autumn afternoon breeze.", "cn": "色彩缤纷艳丽的墨西哥镂空剪纸拉花彩旗，在温暖惬意的深秋午后微风中欢快翻飞起舞。"},
                {"en": "True family means supporting each other's dreams even when they look unfamiliar.", "cn": "所谓真正的家人，就是即便彼此的梦想看起来是如此陌生新奇，依然会义无反顾给予全力支持。"},
                {"en": "A proud culture of remembrance ensures that love survives death for thousands of years.", "cn": "一种懂得敬畏与缅怀的崇高文化传统，能确保人间大爱在肉躯消亡后依然生生不息传承千年。"},
                {"en": "Our home is alive with music, delicious tamales, sweet laughter, and everlasting gratitude.", "cn": "我们的庭院屋舍如今洋溢着悠扬乐声、喷香的玉米粽美食、爽朗的欢声笑语与无尽感恩。"},
                {"en": "Pass down the authentic family legends from old elders to innocent babes in arms.", "cn": "把家族中那些跌宕起伏的真实传奇故事，代代相传讲给怀抱里天真懵懂的后代儿孙倾听吧。"},
                {"en": "When we embrace our ancestors' souls, we discover the strongest foundations of identity.", "cn": "当我们由衷张开臂膀拥抱先祖的深沉灵魂时，我们便寻得了自我认同最坚不可摧的崇高基石。"},
                {"en": "Death is not an insurmountable abyss; death is merely a golden bridge paved with memories.", "cn": "死亡绝非深不见底的绝望天堑；死亡不过是一座由后世深情思念铺就的金黄花瓣桥梁罢了。"},
                {"en": "Sing with pure happiness, for our ancestral roots run deeper than the ancient earth.", "cn": "满怀纯粹极致的幸福放声歌唱吧，因为我们家族的血脉深根，比这片古老辽阔的大地还要深邃！"},
                {"en": "Un Poco Loco! Let your spirit soar with joyful laughter that echoes into eternity.", "cn": "有点疯狂又何妨！让你的自由灵魂伴随着爽朗欢快的笑声凌空翱翔，永远回荡在天地之间！"}
            ]
        },
        {
            "title": "第 6 幕 · 德拉库斯的虚伪神殿与真相大白",
            "description": "光鲜亮丽的豪华派对神殿，隐藏着谋杀同伴窃取歌曲的卑劣罪证。",
            "sentences": [
                {"en": "The lavish mansion of Ernesto de la Cruz was glittering with hollow golden luxury.", "cn": "埃内斯托·德拉库斯金碧辉煌的奢华宫殿豪宅里，处处闪烁着空洞虚饰的黄金浮华。"},
                {"en": "Adoring fans cheered loudly, unaware that their musical idol was a calculating murderer.", "cn": "台下狂热崇拜的如潮粉丝疯狂欢呼尖叫，全然不知他们的音乐偶像私底下竟是一个精于算计的杀人犯。"},
                {"en": "He toasted Héctor with poisoned tequila to steal his notebook of brilliant songs.", "cn": "当年他正是用一杯掺了致命剧毒的龙舌兰烈酒，毒杀了埃克托尔，借此盗窃了他写满传世金曲的日记本。"},
                {"en": "A manufactured celebrity persona will always disintegrate before undeniable factual evidence.", "cn": "一个人为精心包装制造的名流偶像人设，在铁证如山的铁一般事实面前注定会土崩瓦解。"},
                {"en": "Miguel confronted the arrogant idol on the massive stadium stage before millions of viewers.", "cn": "小男孩米格尔在能够容纳数万人的巨型体育场大舞台上，当着数以百万计观众的面当众揭露了伪君子。"},
                {"en": "The backstage camera broadcasted his villainous confession onto the monumental television screens.", "cn": "后台隐藏的摄像机镜头将他恶贯满盈的丑陋自白，一字不漏实时同步直播到了万众瞩目的巨幅大屏幕上。"},
                {"en": "The horrified crowd gasped as the glamorous facade crashed into eternal disgrace.", "cn": "全场瞠目结舌的庞大人群爆发出倒吸凉气的惊呼声，昔日耀眼的光环瞬间跌入万劫不复的耻辱深渊。"},
                {"en": "No amount of theatrical fireworks can disguise the toxic stench of a compromised soul.", "cn": "任凭你燃放多少绚烂夺目的舞台烟火，也休想掩盖一颗彻底腐烂堕落灵魂散发出的刺鼻恶臭。"},
                {"en": "He tossed young Miguel off the high parapet to silence the righteous witness.", "cn": "丧心病狂的凶手甚至亲手将年幼的米格尔从高高的观景台边缘猛推而下，妄图杀人灭口。"},
                {"en": "Pepita caught the falling boy in midair with extraordinary feline agility and precision.", "cn": "神圣灵兽佩皮塔以不可思议的高超灵猫敏捷身手凌空飞扑，在万米高空死死接住了坠落的少年。"},
                {"en": "The giant church bell fell and crushed the fleeing fraud beneath its heavy bronze rim.", "cn": "悬挂在神殿高处的巨型古铜钟轰然坠落，将仓皇抱头鼠窜的骗子死死砸压在沉重的青铜钟罩之下。"},
                {"en": "Poetic justice operates with mathematical exactness across both heaven and earth.", "cn": "天道昭昭的善恶终极报应，无论是在人间凡尘还是在九泉之下，其运行裁决都精准得毫厘不爽。"},
                {"en": "True talent shines humbly, while stolen glory inevitably destroys its possessor.", "cn": "真正的绝世天赋总是谦逊而深邃地发光，而巧取豪夺来的虚妄荣耀终将反噬毁灭其占有者。"},
                {"en": "The deceived public tore down the grand statues they had mistakenly erected for a criminal.", "cn": "大梦初醒的受骗公众愤怒地亲手推倒砸碎了他们当年为这个罪犯误立的所有巨幅大理石雕像。"},
                {"en": "Honor belongs only to the pure-hearted creators who pour their genuine tears into song.", "cn": "人世间真正的崇高荣誉，永远只属于那些将自己滚烫真挚的泪水与心血注入旋律的纯粹创造者。"}
            ]
        },
        {
            "title": "第 7 幕 · 灵兽佩皮塔与迷途寻踪",
            "description": "翱翔于暮色霓虹天际的羽翼神兽，守护纯洁灵魂脱离险境。",
            "sentences": [
                {"en": "Pepita tracked the scent of her family member through the labyrinth of the twilight metropolis.", "cn": "神兽佩皮塔沿着血脉亲人的熟悉气味，轻巧穿梭在这座暮色大都市错综复杂的悬空迷宫之中。"},
                {"en": "Her vibrant wings glowed with magenta, turquoise, gold, and incandescent emerald hues.", "cn": "她那一双遮天蔽日的斑斓巨翼上，流转着洋红、绿松石蓝、流金与璀璨翡翠般绚烂的神圣光晕。"},
                {"en": "Ancient Mexican folk artists sculpted Alebrijes to represent our protective spirit guides.", "cn": "古代墨西哥民间手艺人用木雕描摹出灵兽阿莱布里赫的奇幻模样，代表庇佑我们的守护神使者。"},
                {"en": "A loyal companion will follow you through the dark shadows without showing fear.", "cn": "一个至死不渝的忠诚伙伴会毫不犹豫紧随你涉足最幽暗的深渊阴影，内心没有半分畏缩恐惧。"},
                {"en": "Dante the hairless street dog revealed his true noble identity as a winged spirit guide.", "cn": "那只看似傻乎乎脱毛的街头流浪狗但丁，在危机时刻露出了它身为长着翅膀守护灵兽的崇高真身。"},
                {"en": "Never judge an ally by mundane awkwardness; profound spiritual beauty lies deep within.", "cn": "永远不要凭世俗眼光中的笨拙外表去评判一个同盟战友；深邃神圣的超凡之美深藏在其内心。"},
                {"en": "She roared a warning cry that rattled the glass windows of the grand exhibition palace.", "cn": "她昂首发出一声震撼苍穹的警示怒吼，震得整座宏伟艺术展览宫殿的巨大玻璃窗嗡嗡作响颤动。"},
                {"en": "Gentle hands stroked her magnificent feathered mane as tears of relief flowed freely.", "cn": "温柔稚嫩的双手深情抚摸着她那华美绝伦的羽翼鬃毛，释怀脱险的喜悦泪水忍不住夺眶而出。"},
                {"en": "Creativity transforms traditional folk mythology into modern emotional cinematic magic.", "cn": "极致卓越的艺术创造力，将古老沉淀的民间神话传说蜕变转化为了现代震撼心灵的光影电影魔法。"},
                {"en": "We are guided by invisible animal spirits that sense our innermost moral intentions.", "cn": "在我们冥冥前行的旅程中，始终有无形的灵兽神使在暗中指引，它们能敏锐洞悉我们内心的善恶抉择。"},
                {"en": "Climb onto her broad shoulder, hold on tight, and fly above the luminous clouds.", "cn": "爬上她宽阔坚实的肩膀吧，紧紧抱住鬃毛，展翅翱翔在那片被万家灯火映照得流光溢彩的云海之巅。"},
                {"en": "Courage is contagious when supported by loyal and formidable kindred companions.", "cn": "当身边有坚贞不屈、强大威严的同生共死挚友全力相伴时，无畏的勇气便会如燎原之火般蔓延传递。"},
                {"en": "The mystical creatures of ancient folklore teach us that loyalty transcends species boundaries.", "cn": "古老民间传说中的神奇圣兽用行动昭示我们：崇高忠诚的真谛，早已彻底超越了物种物象的樊篱。"},
                {"en": "A true guardian appears precisely at the moment when hope seems completely extinguished.", "cn": "一位真正的神圣守护使者，总会在你内心的希望火苗看似即将被彻底扑灭的那一刹那奇迹降临。"},
                {"en": "Soar high into the starry Mexican sky, for freedom belongs to the faithful and brave.", "cn": "向着繁星点点的墨西哥浩瀚夜空展翅高翔吧，因为神圣自由永远垂青那些坚贞不渝、勇往直前的勇士！"}
            ]
        },
        {
            "title": "第 8 幕 · 音乐天分与家族反抗的破冰",
            "description": "米格尔阁楼暗室里的秘密吉他世界，梦想与家庭责任的碰撞交锋。",
            "sentences": [
                {"en": "I hid my acoustic guitar in the secret attic behind the dusty family shoe storage racks.", "cn": "我把亲手制作的木吉他秘密藏在满是灰尘的家族鞋料储藏架背后的阁楼隐秘暗室里。"},
                {"en": "I taught myself how to play chords by watching worn-out VHS tapes of Ernesto's classic films.", "cn": "我一遍又一遍倒带观摩德拉库斯经典老电影的磨损录像带，无师自通摸索学会了吉他各种和弦指法。"},
                {"en": "When my abuelita smashed my handmade guitar on the stone patio, my soul shattered completely.", "cn": "当严厉的奶奶当着全家人的面把我在石头天井里狠狠砸得粉碎时，我的整个灵魂彻底崩塌瓦解了。"},
                {"en": "Why must I choose between making you proud and pursuing what makes my spirit sing?", "cn": "为什么我非得在成为让你们骄傲的孝顺孙子，与追随让我灵魂欢快歌唱的神圣热爱之间痛苦二选一？"},
                {"en": "A child's artistic potential should be nurtured with tender encouragement, not crushed with generational fear.", "cn": "一个孩童与生俱来的艺术潜质应当用温存鼓励去悉心呵护浇灌，而非用上一代人内心的恐惧去蛮横扼杀。"},
                {"en": "Running into the dark graveyard night was a desperate cry for my creative autonomy.", "cn": "在那清冷漆黑的夜晚不顾一切冲向墓园，是我为了捍卫自己艺术创造自主权所发出的绝望呐喊。"},
                {"en": "Passionate rebellion often marks the painful birth of genuine adult individuality.", "cn": "一次充满炽热痛苦的反叛抗争，往往标志着一个人真正成熟独立人格的艰难阵痛破茧新生。"},
                {"en": "Music was never the villain; it was the unhealed grief of abandonment that caused the hurt.", "cn": "音乐从来都不是什么罪恶深重的元凶；当年被爱人抛弃后久久未能愈合的创伤之痛，才是真正的心结根源。"},
                {"en": "She banned songs because hearing a melody tore open the fresh agony in her heart.", "cn": "曾曾祖母当年之所以严厉禁绝一切歌声，只因任何一段旋律都会狠狠撕裂开她心口那道鲜血淋漓的剧痛伤痕。"},
                {"en": "True family love matures when adults learn to listen to the authentic voices of youth.", "cn": "当家族中的长辈们终于学会伏下身子，倾听年轻后生内心最本真的声音时，家庭之爱方才真正走向成熟。"},
                {"en": "I will never hide my music again; it is the truest gift God placed inside my soul.", "cn": "往后的岁月里我再也不会东躲西藏隐匿我的音乐了；它就是上帝亲手安放在我灵魂深处的最美馈赠。"},
                {"en": "A guitar without strings is silent, but a boy without dreams has lost his living spark.", "cn": "一把没有装弦的吉他是沉默无声的，但一个被剥夺了梦想的少年，却等于彻底熄灭了生命的光彩。"},
                {"en": "Stand up for your authentic self, even when the people you love misunderstand your path.", "cn": "勇敢捍卫你最本真纯粹的自我吧，哪怕当下你最深爱的至亲至爱对你选择的崎岖道路充满了误解与疑虑。"},
                {"en": "Harmony in a home is created when diverse talents blend like an intricate musical chord.", "cn": "一个家庭真正的和谐美满，在于让形形色色的独特天赋如同一支精密交响和弦般，彼此辉映交织成趣。"},
                {"en": "Play your song loud and clear; the universe is ready to hear your heartfelt melody.", "cn": "大声而清晰地奏响属于你的生命乐章吧；这浩瀚辽阔的宇宙早已张开怀抱，随时准备倾听你深情的旋律！"}
            ]
        },
        {
            "title": "第 9 幕 · 墨西哥小镇圣塞西莉亚的风情",
            "description": "漫步在色彩斑斓的阳光小镇，感受浓郁的拉美文化与温厚市井烟火气。",
            "sentences": [
                {"en": "Santa Cecilia is a charming town bathed in radiant golden Mexican sunshine all year round.", "cn": "圣塞西莉亚是一座终年沐浴在墨西哥温暖明媚、流光溢彩金色阳光之中的迷人魅力小城镇。"},
                {"en": "Shoemakers diligently hammer leather soles while street mariachi bands trumpet lively serenades.", "cn": "制鞋师傅们在作坊里专注地敲打着坚韧的皮革鞋底，而街头的流浪乐手乐队正吹奏着欢快的欢庆小夜曲。"},
                {"en": "The fragrance of sweet churros, roasted corn, and fresh tamales wafts through the bustling plaza.", "cn": "香甜的吉事果、烤得金黄的玉米棒与热气腾腾的鲜美玉米粽香气，在热闹喧嚣的中心广场上空四溢飘散。"},
                {"en": "Every colorful house has bright orange marigolds blooming proudly along its clay window ledges.", "cn": "每一栋色彩鲜艳的粉刷民居红陶窗台上，都娇艳盛开着一丛丛傲然绽放的金黄万寿菊花束。"},
                {"en": "Traditional artisanal trades provide an honorable livelihood grounded in patience and honest labor.", "cn": "世代相传的质朴手工传统手艺，为市井百姓提供了扎根于勤勉耐心与诚实劳作的体面尊严生计。"},
                {"en": "Generations of families live under one roof, sharing meals, stories, laughter, and wisdom.", "cn": "数代同堂的大家庭其乐融融生活在同一个屋檐下，共同分享着一日三餐、陈年往事、欢声笑语与人生大智慧。"},
                {"en": "Community solidarity is the invisible glue that holds small cultural towns together in times of trial.", "cn": "邻里乡亲之间守望相助的团结温情，是在逆境风霜面前将文化古镇紧紧凝聚在一起的无形强力纽带。"},
                {"en": "Children kick soccer balls across the sunbaked stone square while church bells chime the hour.", "cn": "孩童们在被艳阳晒得温热的青石广场上欢快追逐踢着足球，与此同时古老教堂的悠扬钟声正敲响报时。"},
                {"en": "A rich cultural tapestry is woven from everyday rituals, folk art, and warm human hospitality.", "cn": "一部斑斓厚重的璀璨文化长卷，正是由这些日复一日的平实生活仪式、民间质朴艺术与好客温情交织织就的。"},
                {"en": "Respect for the elders is woven into the very fabric of daily Mexican civic etiquette.", "cn": "对家族长辈先贤发自肺腑的敬重爱戴，早已深入骨髓般融汇在墨西哥日常世俗文明礼仪的每一个细微处。"},
                {"en": "The festive costumes woven from rich indigenous textiles burst with vibrant geometric patterns.", "cn": "用本土原住民传统纺织手艺精心缝制的节日盛装，绽放着充满蓬勃原始生命力的明艳几何图腾纹样。"},
                {"en": "Music is the rhythmic heartbeat that pulsates through the joyful cobblestone streets.", "cn": "动人的音乐，正是那穿透流淌在这一条条欢欣鼓舞青石街道深处的蓬勃起伏节律心跳。"},
                {"en": "Life in a close-knit village offers a serene refuge from the relentless chaos of the modern metropolis.", "cn": "生活在这样一个民风淳朴、紧密相连的乡土古镇里，能为人们提供一处远离现代都市喧嚣浮躁的安详心灵避风港。"},
                {"en": "Treasure the modest simplicity of your hometown, for its values will anchor your wandering soul.", "cn": "倍加珍视你故土家园那份质朴无华的纯真吧，因为无论你走到哪里，它的精神内核都将是锚定你漂泊灵魂的定盘星。"},
                {"en": "The celebration of heritage is an active declaration of pride in who we truly are.", "cn": "对自身血脉文化的盛大传承与庆祝，正是向浩瀚世界堂堂正正宣告我们究竟是谁的最自豪宣言！"}
            ]
        },
        {
            "title": "第 10 幕 · 欢庆亡灵节大合唱与人生哲思",
            "description": "全剧最高潮大合唱，米格尔手抱吉他领唱，唱出爱、生命与重逢的赞歌。",
            "sentences": [
                {"en": "Say that I'm crazy or call me a fool, but nothing can stop the music in my soul!", "cn": "就算说我疯疯癫癫，或者骂我是个傻瓜蛋，但也休想阻挡我灵魂深处奔涌而出的炽热音乐！(高潮欢唱)"},
                {"en": "The dead and the living sing together as the veil between worlds turns whisper thin.", "cn": "当横亘在阴阳两界之间的神秘面纱变得如蝉翼般轻薄时，逝者与生者并肩相拥，共同放声高唱欢庆赞歌。"},
                {"en": "Love transcends death because memory is an eternal spiritual bridge that never decays.", "cn": "大爱之所以能够彻底超越肉躯的死亡，只因真挚的记忆是一座永不风化腐朽的崇高精神永恒桥梁。"},
                {"en": "Every ancestor who walked before you contributed a golden thread to your living destiny.", "cn": "每一个曾经在你之前跋涉走过漫漫人生路途的先辈，都为铸就你今日鲜活明亮的命运轨迹贡献了一缕金线。"},
                {"en": "To live in hearts we leave behind is not to die; it is to conquer physical mortality.", "cn": "活在我们身后深爱之人的滚烫心扉里，根本不算真正逝去；那是战胜了血肉之躯有限寿命的终极永恒。"},
                {"en": "A smile shared across a candlelit holiday table heals centuries of ancestral misunderstandings.", "cn": "在烛光摇曳的节日餐桌前相视绽放的一抹温存微笑，足以瞬间抚平治愈横亘在数代先祖之间数百年的隔阂误解。"},
                {"en": "Music gives words a pair of soaring wings and gives the solitary soul a loving home.", "cn": "动人的音乐赋予了干瘪苍白的文字一双展翅高飞的雄鹰羽翼，更为孤独漂泊的心灵觅得了一处温暖的归宿港湾。"},
                {"en": "Never fear the inevitable autumn of life, for spring blossoms eternally in the memory of those who love you.", "cn": "永远不要畏惧生命终将迎来的萧瑟深秋，因为在那些深深爱着你的人的温暖记忆里，明媚的暖春永远盛开不败。"},
                {"en": "We honor our past not out of blind dogma, but out of vibrant, celebratory gratitude for existence.", "cn": "我们之所以深情致敬过往历史，绝非出于盲目僵化的教条，而是对上苍赐予我们鲜活生命的由衷感恩赞美。"},
                {"en": "Strum the final chord with triumphant joy; let the music fill every corner of the plaza!", "cn": "满怀胜利凯旋的无上欢愉，用力扫落这终章的最后一个灿烂和弦吧；让悠扬欢快的旋律溢满广场的每一个角落！"},
                {"en": "Our roots are deep, our wings are wide, and our ancestral blessings are eternal.", "cn": "我们的文化深根深植沃土，我们的梦想羽翼广阔翱翔，而长辈先祖的神圣福祉庇佑万世长存、永无止境。"},
                {"en": "The golden marigold petals glow softly in the twilight, guiding our hearts back to where we belong.", "cn": "金黄的万寿菊花瓣在暮色暮霭中散发着柔和神圣的光芒，默默指引着我们的心，重新回归属于我们的精神故里。"},
                {"en": "Keep the light of memory burning bright, and no precious soul will ever be lost in darkness.", "cn": "让记忆的明灯在心头永远熊熊燃烧吧，如此这般，这世间便再也没有任何一个珍贵的灵魂会迷失在冰冷黑暗之中。"},
                {"en": "Adios, until we meet again on that radiant, flower-paved bridge beneath the cosmic stars.", "cn": "再会了，直到未来的某一天，我们再次相约相聚在浩瀚星河之下那座繁花盛开、流光溢彩的神圣桥梁之上。"},
                {"en": "Remember me, and let love echo through the generations like an everlasting symphony.", "cn": "请永远记住我，让这人世间至纯至真至善的大爱，如同一曲永不落幕的宏伟交响乐章般，世代激荡回响！"}
            ]
        }
    ]))

    return courses

if __name__ == "__main__":
    courses = generate_movies()
    save_ts_file("movies", "MOVIES_COURSES", courses)
