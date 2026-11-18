# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))
from builder_core import build_course, save_ts_file
import music_part1

# 导入披头士
def get_all_music():
    courses = []
    
    # 1. 披头士
    courses.extend(music_part1.get_music_part1())
    
    # 2. 泰勒·斯威夫特 (Taylor Swift)
    courses.append(build_course({
        "id": "course-mus-swift",
        "title": "《泰勒·斯威夫特》(Taylor Swift) · 叙事民谣与流行诗篇 (10章全集)",
        "category": "music",
        "categoryName": "音乐英语",
        "coverGradient": "from-rose-500 via-pink-600 to-purple-800",
        "icon": "✨",
        "description": "十三座格莱美奖得主，Love Story、Blank Space、All Too Well 叙事天花板全收录。",
        "difficulty": "中级 B1",
        "tags": ["霉霉", "叙事歌词", "流行天后", "治愈失恋"]
    }, [
        {
            "title": "第 1 首 · Love Story · 罗密欧与朱丽叶的圆满救赎",
            "description": "无畏时代的青春浪漫神话，打破悲剧宿命的阳台纯真告白。",
            "sentences": [
                {"en": "We were both young when I first saw you; I close my eyes and the flashback starts.", "cn": "当我初次遇见你的那一年，我们都还年少懵懂；闭上双眼，往事回忆便如潮水般涌上心头。"},
                {"en": "I'm standing there on a balcony in summer air, seeing the lights make their way to the ball.", "cn": "我静静伫立在夏夜微风拂面的阳台之巅，遥望远方城堡舞会的流光溢彩渐渐苏醒点亮。"},
                {"en": "See you make your way through the crowd and say hello; little did I know.", "cn": "注视着你穿过熙熙攘攘的喧嚣人群款款走来，向我微笑道一声你好；当时年幼的我怎会料到。"},
                {"en": "That you were Romeo, you were throwing pebbles, and my daddy said: Stay away from Juliet.", "cn": "原来你就是我的罗密欧，你正往我窗台投掷小石子，而我固执的父亲却厉声喝令：离我家朱丽叶远点！"},
                {"en": "And you were crying on the staircase, begging me: Please don't go.", "cn": "你曾无助地瘫坐在幽暗的旋转楼梯台阶上，眼眶泛红哀求我：求你千万别放手离去。"},
                {"en": "Romeo, take me somewhere we can be alone; I'll be waiting, all that's left to do is run.", "cn": "罗密欧啊，快快带我私奔到只有我们两人的世外桃源吧；我一直在苦苦守候，剩下的唯有不顾一切逃离凡尘！"},
                {"en": "You'll be the prince and I'll be the princess; it's a love story, baby, just say yes.", "cn": "你将是我的无畏王子，而我便是你的掌上公主；这是一出童话般的爱情传奇，亲爱的，请你点头答应吧！"},
                {"en": "So I sneak out to the garden to see you; we keep quiet cause we're dead if they knew.", "cn": "于是我趁着夜色偷偷溜进寂静的花园草坪同你幽会；我们屏住呼吸蹑手蹑脚，只因一旦被家人撞破便死无葬身之地。"},
                {"en": "So close your eyes, escape this town for a little while, oh, oh.", "cn": "所以快快闭上双眸吧，暂时忘却烦恼，随我短暂逃离这充满偏见的冰冷小镇。"},
                {"en": "Cause you were Romeo, I was a scarlet letter, and my daddy said: Stay away from Juliet.", "cn": "只因你是被世俗不容的罗密欧，而我宛如承受非议的红字罪人，父亲严厉告诫：绝不许靠近朱丽叶半步！"},
                {"en": "But you were everything to me, I was begging you: Please don't go.", "cn": "但在我心灵深处你就是我不可分割的整座宇宙，我曾泪流满面苦苦哀求你：千万别抛下我离去。"},
                {"en": "I got tired of waiting, wondering if you were ever coming around.", "cn": "我渐渐在漫长无期的苦等中感到身心俱疲，暗自惶惑你是否当真还会如约骑着白马归来。"},
                {"en": "My faith in you was fading when I met you on the outskirts of town and said.", "cn": "正当我心中的笃定信念一点点快要消耗殆尽时，我却在小镇寂寥荒凉的郊外路口与你奇迹般不期而遇，我含泪轻语："},
                {"en": "Romeo, save me, I've been feeling so alone; I keep waiting for you, but you never come.", "cn": "罗密欧，快拯救我脱离苦海吧，这段漫长孤寂的岁月我熬得好苦；我日夜在此守候，为何却迟迟不见你的身影？"},
                {"en": "He knelt to the ground and pulled out a ring and said: Marry me, Juliet, you'll never have to be alone.", "cn": "他单膝扑通一声跪倒在尘土草地上，颤抖着掏出一枚璀璨戒指深情宣告：嫁给我吧朱丽叶，从今往后你再也无需独自一人承受孤独！"}
            ]
        },
        {
            "title": "第 2 首 · Blank Space · 空白格里的致命迷恋",
            "description": "反讽媒体塑造的黑寡妇疯女人人设，满分自嘲与流行电音神专。",
            "sentences": [
                {"en": "Nice to meet you, where you been? I could show you incredible things.", "cn": "很高兴遇见你，此前你都躲在哪儿逍遥呢？我能领你领略足以令人瞠目结舌的人间奇景。"},
                {"en": "Magic, madness, heaven, sin; saw you there and I thought: Oh my God, look at that face.", "cn": "魔幻、疯狂、神圣天堂与致命原罪；在人群中瞥见你的那一瞬我暗自惊呼：天呐瞧瞧那张绝世俊脸！"},
                {"en": "You look like my next mistake; love's a game, wanna play?", "cn": "你看起来活脱脱就是我即将犯下的下一个美丽人生大错；爱情不过是一场高风险游戏，敢不敢入局玩一把？"},
                {"en": "New money, suit and tie; I can read you like a magazine.", "cn": "暴发新贵的气派，笔挺考究的西装配领带；我只需扫上一眼，便能如翻阅时尚杂志般把你看个底朝天。"},
                {"en": "Ain't it funny rumors fly? And I know you heard about me.", "cn": "漫天飞舞的流言蜚语难道不可笑荒诞吗？而且我心知肚明，你早在坊间听闻过关于我的种种疯批恶名。"},
                {"en": "So hey, let's be friends; I'm dying to see how this one ends.", "cn": "所以嘿，咱们先从交个朋友开始吧；我真迫不及待想亲眼看看这次的孽缘究竟会以何等惨烈收场。"},
                {"en": "Grab your passport and my hand; I can make the bad guys good for a weekend.", "cn": "抓紧你的跨国护照并握紧我的手；老娘有能耐让最桀骜不驯的坏小子在周末乖乖变成体贴绅士。"},
                {"en": "So it's gonna be forever, or it's gonna go down in flames.", "cn": "所以这场狂欢要么会是一场刻骨铭心的永恒传奇，要么便注定在一片熊熊烈焰火海中同归于尽、彻底玉石俱焚！"},
                {"en": "You can tell me when it's over, if the high was worth the pain.", "cn": "待到大幕彻底落下的那一天你大可告诉我：当初那场令人上头沉沦的快感，究竟值不抵那痛彻心扉的代价！"},
                {"en": "Got a long list of ex-lovers; they'll tell you I'm insane.", "cn": "我手头可攥着一长串写满昔日旧爱名字的前任名单；他们每一个人都会咬牙切齿警告你：那女人是个彻头彻尾的疯子！"},
                {"en": "Cause you know I love the players, and you love the game.", "cn": "因为你心里清楚老娘向来就偏爱棋逢对手的情场高手，而你则无可救药地沉迷于这场猫鼠博弈！"},
                {"en": "Cause we're young and we're reckless; we'll take this way too far.", "cn": "只因我们正值青春肆意、行事鲁莽不计后果；我们必将在这条疯狂歧途上越陷越深、彻底失控！"},
                {"en": "It'll leave you breathless, or with a nasty scar.", "cn": "它要么会让你沉醉得屏息窒息、欲罢不能，要么便会残忍在你心口留下一道终生难以愈合的丑陋伤疤。"},
                {"en": "Got a long list of ex-lovers, they'll tell you I'm insane.", "cn": "我那串前任名单上的受害者们，一定会异口同声劝你趁早死心别招惹我。"},
                {"en": "But I've got a blank space, baby, and I'll write your name.", "cn": "但我掌心的名册上正好还空余着一个空白格，亲爱的，老娘这就大笔一挥写上你的大名！"}
            ]
        },
        {
            "title": "第 3 首 · All Too Well · 记忆犹新的深秋红围巾",
            "description": "乐评人公认叙事天花板，长篇枫叶红围巾与十倍慢镜头的破碎之痛。",
            "sentences": [
                {"en": "I walked through the door with you, the air was cold, but something about it felt like home somehow.", "cn": "我和你并肩迈入那扇熟悉的房门，屋外的空气寒冷料峭，但不知为何，这里的一切却让我恍惚有种回到家的踏实归属感。"},
                {"en": "And I left my scarf there at your sister's house, and you've still got it in your drawer even now.", "cn": "当年我不小心把我那条红色围巾落在了你姐姐家里，而时至今日，它依然被你静静锁在卧室的抽屉深处。"},
                {"en": "Autumn leaves falling down like pieces into place, and I can picture it after all these days.", "cn": "秋日的枫叶如拼图归位般一片片旋转飘落，即便岁月流转沧海桑田，那些画面在我脑海中依然清晰如昨。"},
                {"en": "And I know it's long gone and that magic's not here no more, and I might be okay, but I'm not fine at all.", "cn": "我深知那段青葱岁月早已灰飞烟灭、昔日的魔法奇迹再难重现，我或许表面上风平浪静，但我内心深处其实一点也不好。"},
                {"en": "Cause there we are again on that little town street; you almost ran the red cause you were looking over at me.", "cn": "只因那一幕幕再次浮现眼前：漫步在偏僻小镇空旷的街道上，你只顾转头含情脉脉看着我，差点一头闯过了红灯。"},
                {"en": "Wind in my hair, I was there, I remember it all too well.", "cn": "清凉微风拂过我的发丝，那时的我真切陪伴在你身侧，那所有的一切，我至今依然记忆犹新、历历在目！"},
                {"en": "Photo album on the counter, your cheeks were turning red; you used to be a little kid with glasses in a twin-sized bed.", "cn": "柜台上散落翻开的泛黄家庭老相册，你害羞得双颊瞬间泛起红晕；照片里的你曾经还是个戴着小近视镜、蜷缩在单人小床上的稚气孩童。"},
                {"en": "And your mother's telling stories about you on the tee-ball team, you taught me about your past, thinking your future was me.", "cn": "你的母亲坐在身旁满脸自豪絮絮叨叨讲着你少棒队当年的趣事，你将你的童年往事对我倾囊相告，满心笃定我就是你未来的唯一归宿。"},
                {"en": "And I know it's long gone and there was nothing else I could do, and I forget about you long enough to forget why I needed to.", "cn": "我深知繁华落尽早已无可挽回，我用尽全力拼命遗忘关于你的一切，直到我甚至快要忘记当初究竟为何非要逼自己去忘记。"},
                {"en": "Time won't fly, it's like I'm paralyzed by it; I'd like to be my old self again, but I'm still trying to find it.", "cn": "漫漫时间在此刻仿佛彻底停滞不再流逝，我就像被痛苦彻底麻痹全身；我多么渴望能重新找回昔日那个无忧无虑的自己，可我依然在苦苦追寻无果。"},
                {"en": "After plaid shirt days and nights when you made me your own, now you mail back my things and I walk home alone.", "cn": "那些并肩度过身披格子衬衫的温存日子、那些你在耳畔将我占为己有的缠绵长夜终究成了过客，如今你冷冰冰将旧物邮寄归还，我独自一人走在空荡荡的归家雨路上。"},
                {"en": "You kept my old scarf from that very first week, cause it reminds you of innocence and it smells like me.", "cn": "你唯独舍不得寄回我头一周落下的那条旧围巾，只因它始终在提醒你曾经那份未被世俗污染的纯真，而且上面依然残留着我的体温与气息。"},
                {"en": "You can't get rid of it cause you remember it all too well, yeah.", "cn": "你哪怕扔掉全世界也绝不舍得丢掉它，只因你心里同我一样，对过往的一切始终记忆犹新、至死难忘！"},
                {"en": "You call me up again just to break me like a promise, so casually cruel in the name of being honest.", "cn": "你大半夜再次打电话过来，仅仅是为了像随手撕毁誓言那样将我再次摔得粉碎；打着所谓坦诚直白的伪善名义，行使着最轻描淡写却残忍至极的心灵凌迟！"},
                {"en": "I'm a crumpled up piece of paper lying here, cause I remember it all, all, all too well.", "cn": "我就如同一张被你随手揉皱成团狠狠丢弃在角落里的废纸废屑，只因那过往的一切点点滴滴，我至今依然痛彻心扉、历历在目！"}
            ]
        },
        {
            "title": "第 4 首 · Shake It Off · 甩掉烦恼与做真实的自己",
            "description": "横扫全球冠军单曲，面对键盘侠与恶意批评，踏着萨克斯铜管放肆热舞。",
            "sentences": [
                {"en": "I stay out too late, got nothing in my brain; that's what people say, that's what people say.", "cn": "说我天天深夜在外面玩得不着家，说我脑瓜里空空如也毫无内涵；外头闲言碎语就是这么传的，长舌妇们就是这么嘀咕的！"},
                {"en": "I go on too many dates, but I can't make them stay; at least that's what people say.", "cn": "说我约会谈恋爱太频繁换得太勤，却一个也留不住男人；反正媒体看客们天天就是这么风言风语的！"},
                {"en": "But I keep cruising, can't stop, won't stop moving; it's like I got this music in my mind saying: It's gonna be alright.", "cn": "但我根本不以为意大步流星向前迈进，绝不驻足、休想阻止我狂欢的舞步；仿佛脑海深处始终有一支欢快旋律在对我说：一切都会好起来的！"},
                {"en": "Cause the players gonna play, play, play, play, play.", "cn": "只因情场浪子们爱怎么花天酒地玩弄手段就由他们去吧！"},
                {"en": "And the haters gonna hate, hate, hate, hate, hate.", "cn": "而心胸狭隘的键盘侠黑粉们爱怎么恶语中伤谩骂就由他们去喷吧！"},
                {"en": "Baby, I'm just gonna shake, shake, shake, shake, shake; shake it off, shake it off!", "cn": "亲爱的宝贝，老娘只需要踏着鼓点痛快甩甩甩，把所有的负能量与流言蜚语统统甩到九霄云外去！"},
                {"en": "Heartbreakers gonna break, break, break, break, break.", "cn": "薄情寡义的负心汉们爱怎么伤人自尊心碎一地就由他们去吧！"},
                {"en": "And the fakers gonna fake, fake, fake, fake, fake.", "cn": "虚情假意的伪善之徒爱怎么装模作样戴面具就由他们去演吧！"},
                {"en": "Baby, I'm just gonna shake, shake, shake, shake, shake; shake it off, shake it off!", "cn": "而老娘自始至终只会潇洒抖抖双肩大步起舞，把那些乌烟瘴气通通甩在身后踩得粉碎！"},
                {"en": "I never miss a beat, I'm lightning on my feet, and that's what they don't see.", "cn": "我踏下的每一个节拍从不踩空，我的舞步轻盈矫健宛如一道撕裂黑夜的霹雳闪电，而这些惊人天赋恰恰是盲目看客们有眼无珠看不见的。"},
                {"en": "I'm dancing on my own, I make the moves up as I go, and that's what they don't know.", "cn": "我独自一人在属于我自己的盛大舞台上忘情独舞，随心所欲即兴自创着属于我的炫酷动作，而这些真正的从容自信是庸俗之辈永远无法参透的。"},
                {"en": "Hey, hey, hey, just think while you've been getting down and out about the liars and the dirty, dirty cheats of the world.", "cn": "嘿！快好好醒醒脑子想一想：每当你在夜深人静时为这世间那些道貌岸然的骗子与肮脏卑劣的背叛者伤心欲绝消沉萎靡时——"},
                {"en": "You could have been getting down to this sick beat!", "cn": "你本该抓紧大好青春年华，迎着这带感爆棚的神级动感节拍肆意狂欢尽情放飞自我！"},
                {"en": "My ex-man brought his new girlfriend; she's like: Oh my god, but I'm just gonna shake it.", "cn": "我的倒霉前男友带着他新交的小女友当面耀武扬威显摆；那姑娘眼珠子瞪得溜圆满脸挑衅，而老娘连眼皮都没眨一下，只是冲他们灿然一笑抖了抖风衣！"},
                {"en": "Shake it off, shake it off, never allow the poison of small minds to dull your radiant sparkle.", "cn": "统统甩掉它，大步向前看吧；永远绝不要允许那些心胸狭窄阴暗鼠辈的流言毒素，掩盖折损了你浑身散发出的璀璨夺目光彩！"}
            ]
        },
        {
            "title": "第 5 首 · Cardigan · 羊毛开衫与失落的青春记忆",
            "description": "民谣专辑 Folklore 核心主打，古朴钢琴、绿苔森林与旧开衫的温暖救赎。",
            "sentences": [
                {"en": "Vintage tee, brand new phone, high heels on cobblestones.", "cn": "身上套着件复古古董做旧T恤，手里攥着崭新的智能手机，脚上踩着细高跟嗒嗒敲击在湿漉漉的鹅卵石铺就的老街上。"},
                {"en": "When you are young, they assume you know nothing.", "cn": "当你年纪尚轻稚气未脱时，这世上所有傲慢的成年人都自以为是地断定你对人世间的真谛一无所知。"},
                {"en": "Sequin smile, black lipstick, sensual politics.", "cn": "唇边挂着如亮片般璀璨耀眼却暗藏锋芒的微笑，涂抹着深沉叛逆的黑色唇膏，熟稔游走于情感博弈的暗涌漩涡之间。"},
                {"en": "When you are young, they assume you know nothing, but I knew you.", "cn": "每逢年少轻狂之时，世人总武断认为我们涉世未深少不更事；但我心里比谁都清楚：我曾彻头彻尾懂透了你的灵魂。"},
                {"en": "Dancin' in your Levi's, drunk under a streetlight, I knew you.", "cn": "穿着泛旧的李维斯牛仔裤在昏黄的路灯光晕之下微醺纵情曼舞，那一夜，我曾如此真切看清了你的全部。"},
                {"en": "Hand under my sweatshirt, baby, kiss it better, I knew you.", "cn": "温存的掌心轻轻滑入我的卫衣下摆，轻吻着伤痕温语抚慰创痛，我曾坚定深信你就是我一生的港湾。"},
                {"en": "And when I felt like I was an old cardigan under someone's bed, you put me on and said I was your favorite.", "cn": "每当我觉得自己仿佛是一件被旁人遗弃在床底下蒙尘落灰的破旧羊毛开衫时，唯独只有你小心翼翼将我轻轻捡起披在肩头，温柔告诉我：我始终是你的挚爱！"},
                {"en": "A friend to all is a friend to none; chase two girls, lose the one.", "cn": "对所有人逢迎讨好博取好感的人，最终往往不配拥有任何一个交心挚友；妄图同时追逐两条小鹿的人，终将两手空空痛失真爱。"},
                {"en": "When you are young, they assume you know nothing, but I knew you'd linger like a tattoo kiss.", "cn": "年少无知时外人总笑我们幼稚冲动，但我骨子里早有预感：你留下的印记，必将如同一道洗不掉的文身热吻般烙印余生。"},
                {"en": "I knew you'd haunt all of my what-ifs, the smell of smoke would hang around this long.", "cn": "我心知肚明你日后必将如同幽灵般长久萦绕在我每一个“如果当初”的假设叹息之中，那淡淡的烟草香气竟然会在岁月深处回荡这么久。"},
                {"en": "Cause I knew everything when I was young; I knew I'd curse you for the longest time.", "cn": "因为其实早在年少时我内心便洞悉了一切；我清楚预见到自己将在往后漫长岁月中千百次在泪水中诅咒埋怨你的不辞而别。"},
                {"en": "Chasin' shadows in the grocery line, I knew you'd miss me once the thrill expired.", "cn": "在下班超市排队结账的无聊队伍里恍惚追寻着昔日故人的虚幻残影，我早就算准：一旦你一时图新鲜的狂躁刺激彻底褪去，你必定会追悔莫及疯了般思念起我。"},
                {"en": "And you'd be standin' in my front porch light, and I knew you'd come back to me.", "cn": "而最终的某一天，你必将失魂落魄重新伫立在我家门前那盏微弱明亮的门廊暖灯之下，我从始至终坚信你必定会回头乞求原谅！"},
                {"en": "And you'd come back to me, and you'd come back to me, and you'd come back.", "cn": "你终将浪子回头重归故里，你必定会重新回到我的身侧，乞求重修旧好。"},
                {"en": "You put me on and said I was your favorite; the old cardigan sheltered a wounded, resilient heart.", "cn": "你曾将我轻轻穿在身上，柔声告诉我我是你的独家偏爱；那件温暖的旧开衫，静静呵护着一颗曾被摔得粉碎却又顽强愈合的滚烫之心。"}
            ]
        },
        {
            "title": "第 6 首 · Anti-Hero · 午夜审判与最大的问题是我自己",
            "description": "午夜专辑现象级自省之作，深夜三点的内在审判与巨大的自省幽默感。",
            "sentences": [
                {"en": "I have this thing where I get older, but just never wiser; midnights become my afternoons.", "cn": "我身上有这么个无可救药的怪毛病：年龄一年比一年苍老渐长，心智却从不见得长了半分智慧；深更半夜反而成了我思维最活跃的清醒午后。"},
                {"en": "When my depression works the graveyard shift, all of the people I've ghosted stand there in the room.", "cn": "每当内心的重度抑郁症开始接管值守午夜坟场夜班时，那些所有曾被我不告而别冷暴力断联的旧识故人，便会齐刷刷如幽灵般伫立在我的房间凝视着我。"},
                {"en": "I should not be left to my own devices; they come with prices and vices, I end up in crisis.", "cn": "绝不该放任我独自一人在房间里胡思乱想瞎折腾；那些任性的念头往往伴随着沉痛的代价与恶习，最终总会以我陷入灭顶心理危机惨淡收场。"},
                {"en": "Tale as old as time: I wake up screaming from dreaming one day I'll watch as you're leaving.", "cn": "这出焦虑老掉牙的桥段简直亘古不变：我总会在噩梦中尖叫惊醒，梦见在未来的某一天，我只能眼睁睁看着你头也不回决绝离开我的背影。"},
                {"en": "Cause you got tired of my scheming, for the last time.", "cn": "只因你终于对我那机关算尽的小算盘与神经质彻底感到厌烦透顶，忍无可忍做了最终的离别了断。"},
                {"en": "It's me, hi, I'm the problem, it's me; at tea time, everybody agrees.", "cn": "没错正是在下，嗨你好啊，这一切灾难的罪魁祸首根源就是我本人；每逢下午茶闲聊八卦时分，全天下所有人对此都出奇一致高度认同！"},
                {"en": "I'll stare directly at the sun, but never in the mirror; it must be exhausting always rooting for the anti-hero.", "cn": "我宁愿冒着双目失明的危险去直视头顶刺目的烈日骄阳，也绝不敢勇敢抬眼端详穿衣镜中的真实自我；日复一日为我这种浑身毛病的反英雄摇旗呐喊打气，想必一定令你们感到筋疲力尽、心力交瘁吧！"},
                {"en": "Sometimes I feel like everybody is a sexy baby, and I'm a monster on the hill.", "cn": "有时候我打心底里觉得周遭所有人都出落得娇媚迷人、纯洁无害，而唯独只有我像个盘踞在荒凉山巅之上的丑陋吃人巨兽。"},
                {"en": "Too big to hang out, slowly lurching toward your favorite city, pierced through the heart, but never killed.", "cn": "庞大笨重到无法融入体面的社交圈子，步履蹒跚跌跌撞撞向着你们最向往的繁华都市挪动，胸膛被千万把正义利剑扎穿刺透，却无论如何也死不瞑目。"},
                {"en": "Did you hear my covert narcissism I disguise as altruism like some kind of congressman?", "cn": "你们是否当真听出了我骨子里那股隐蔽狡黠的自恋虚荣？我平日里总爱把它精心伪装成大公无私的利他奉献，活脱脱像个在电视里拉选票的虚伪政客！"},
                {"en": "I have this dream my daughter-in-law kills me for the money, she thinks I left them in the will.", "cn": "我老是做一个荒诞离奇的恐怖噩梦：梦见我未来的儿媳妇为了争夺巨额遗产蓄意将我谋杀下毒，满心以为我在遗嘱里给他们留下了金山银山。"},
                {"en": "The family gathers round and reads it and then someone screams out: She's laughing up at us from hell!", "cn": "全家亲戚簇拥聚拢在律师身旁当众宣读遗产分配，紧接着有人气急败坏尖叫咆哮：那老巫婆死后正在地狱深处咧着嘴嘲笑戏弄咱们呢！"},
                {"en": "It's me, hi, I'm the problem, it's me.", "cn": "不用瞎猜了就是我，嗨！整起悲剧最大的毒瘤问题就是我本人，非我莫属。"},
                {"en": "Self-awareness mixed with dark humor becomes the sharpest scalpel to dissect psychological insecurity.", "cn": "高度清醒的自我剖析审视，一旦与辛辣刻薄的黑色自嘲幽默相交织融汇，便化作了一柄解剖内心深处自卑不安全感的最锋利手术刀。"},
                {"en": "It must be exhausting always rooting for the anti-hero; accept your flaws and dance with the shadows.", "cn": "永远去粉一个自相矛盾的叛逆反英雄想必一定很累很疲惫吧；坦然接纳自己所有的残缺与阴暗，才能在黑夜中与内心的阴影从容共舞。"}
            ]
        },
        {
            "title": "第 7 首 · Cruel Summer · 残酷夏日与滚烫的爱意咆哮",
            "description": "时代巡演全场万人嘶吼神曲，桥段咆哮声嘶力竭，夏日隐秘恋情的极致张力。",
            "sentences": [
                {"en": "Fever dream high in the quiet of the night, you know that I caught it.", "cn": "在夏夜寂静无声的沉睡深处，心头泛起一阵如高烧梦魇般炽热滚烫的狂乱悸动，你心里清楚我早已深陷其中无可救药。"},
                {"en": "Bad, bad boy, shiny toy with a price, you know that I bought it.", "cn": "坏透了的坏小子，宛如橱窗里标着昂贵标价的耀眼华丽玩物，你明知道我毫不犹豫掏出全部身家将你买下。"},
                {"en": "Killing me slow, out the window, I'm always waiting for you to be waiting below.", "cn": "这折磨慢刀子割肉般一点点将我蚕食凌迟，推开窗棂俯瞰空旷街道，我日夜都在奢望你会悄然驻足伫立在楼下守候。"},
                {"en": "Devils roll the dice, angels roll their eyes, what doesn't kill me makes me want you more.", "cn": "地狱的恶魔正肆意投掷着命运的骰子，天堂的炽天使们无奈地翻着白眼；凡是未能将我彻底置于死地的致命折磨，只会让我对你的渴望变得更加疯狂病态！"},
                {"en": "And it's new, the shape of your body; it's blue, the feeling I've got.", "cn": "每一次拥抱你修长挺拔的躯体都有崭新的心跳触感；而弥漫在我心头挥之不去的阴郁情绪，是一抹深不见底的湛蓝忧郁。"},
                {"en": "And it's ooh, whoa, oh, it's a cruel summer; it's cool, that's what I tell 'em, no rules in breakable heaven.", "cn": "噢天呐，这是一场多么残酷苦涩的折磨盛夏啊；但我对旁人故作云淡风轻宣称我很酷无所谓，在这座随时可能粉碎坍塌的虚幻天堂里本就毫无章法规则可言。"},
                {"en": "Hang your head low in the glow of the vending machine; I'm not dying.", "cn": "在走廊自动售货机泛着幽幽荧光的角落里你深深垂下落寞的头颅；我坚强得很，老娘死不了！"},
                {"en": "We say that we'll just screw it up in the end, but you're keeping me in this agonizing holding pattern.", "cn": "我们总是在嘴上悲观赌咒说咱们早晚会把一切搞砸彻底玩完，但你的一举一动却让我深陷这备受煎熬的悬停等待中欲罢不能。"},
                {"en": "I'm drunk in the back of the car, and I cried like a baby coming home from the bar.", "cn": "我烂醉如泥瘫倒在出租车的后座真皮皮椅上，宛如一个在深夜从酒吧回家的受委屈巨婴般撕心裂肺号啕大哭！"},
                {"en": "Said: I'm fine, but it wasn't true; I don't wanna keep secrets just to keep you!", "cn": "我逢人便硬撑说我没事我很好，可那分明全是自欺欺人的弥天大谎；老娘再也不想靠着委曲求全藏匿秘密，来苟延残喘维系挽留你！"},
                {"en": "And I snuck in through the garden gate every night that summer just to seal my fate.", "cn": "在那个焦躁残酷夏天的每一个夜深人静夜晚，我都像个做贼的小偷一样偷偷潜入花园铁门，只为亲手将自己的万劫不复宿命彻底封印！"},
                {"en": "And I screamed for whatever it's worth: I LOVE YOU, AIN'T THAT THE WORST THING YOU EVER HEARD?", "cn": "我拼尽胸膛全部气力迎着漫天狂风声嘶力竭放声咆哮：老子深爱着你！难道这不正是你这辈子所听过的最可怕、最糟糕的灾难噩耗吗？！(全场封神怒吼)"},
                {"en": "He looks up, grinning like a devil; he whispered that he loved me too.", "cn": "他缓缓抬起那张英俊的脸庞，唇角泛起如恶魔般得逞的妖魅坏笑；紧接着贴近我耳畔轻声呢喃回应：傻瓜，我也同样深爱着你。"},
                {"en": "The vocal bridge erupts with the explosive catharsis of repressed, forbidden passion.", "cn": "这段副歌过渡桥段的嗓音情感爆发，宛如压抑已久的禁忌烈焰地火骤然冲破地壳，喷薄出令人窒息的心灵宣泄快感。"},
                {"en": "It's a cruel summer, but passion forged in secret fire burns hotter than daylight.", "cn": "这固然是一场残酷煎熬的盛夏苦旅，但唯有在那暗无天日的隐秘地火中千锤百炼锻造出的炽热真爱，才远比白昼阳光还要烈焰焚天！"}
            ]
        },
        {
            "title": "第 8 首 · Lover · 属于我们的麦田与暖光长相厮守",
            "description": "浪漫复古三拍子慢华尔兹，粉红云霞、暖黄灯光与向全世界宣告私有主权。",
            "sentences": [
                {"en": "We could leave the Christmas lights up 'til January; this is our place, we make the rules.", "cn": "我们可以任由绚烂的圣诞彩灯一直悬挂点缀到次年一月隆冬；这里是我们专属的温馨私密天地，所有规矩全由我们自己说了算！"},
                {"en": "And there's a dazzling haze, a mysterious way about you, dear.", "cn": "亲爱的，在你举手投足的周身轮廓之外，始终萦绕着一抹令人目眩神迷的梦幻薄雾与神秘莫测的高雅神韵。"},
                {"en": "Have I known you twenty seconds or twenty years?", "cn": "凝视着你的双眼，我恍惚常常陷入沉思：我究竟是刚刚与你相识了区区二十秒，还是早已同你在三生三世里缠绵厮守了整整二十年？"},
                {"en": "Can I go where you go? Can we always be this close forever and ever?", "cn": "无论你未来的脚步踏足何方，我能否都有幸形影相随陪伴你身侧？我们是否能够如同此时此刻这般亲密无间，一生一世长相厮守、永不分离？"},
                {"en": "And ah, take me out, and take me home; you're my, my, my, my lover.", "cn": "噢，挽起我的手带我盛装出席漫步人间，然后领着我重回温馨归宿；你就是我独一无二、生生世世的至爱伴侣！"},
                {"en": "We could let our friends crash in the living room; this is our place, we make the call.", "cn": "我们可以毫无顾忌邀请投缘的莫逆挚友在客厅地毯上随性留宿通宵长谈；这里是我们遮风避雨的家园，一切抉择全凭我们的心意定夺。"},
                {"en": "And I'm highly suspicious that everyone who sees you wants you; I've loved you three summers now, honey, but I want 'em all.", "cn": "我总免不了神经质般高度戒备：每一个亲眼目睹过你迷人风采的人都会不可遏制地爱上你；亲爱的，虽然我已陪伴你度过了三个绚烂盛夏，但我贪心想要承包你的余生所有寒暑！"},
                {"en": "Can I go where you go? Can we always be this close forever and ever?", "cn": "我能否永远追随你奔赴天涯海角？我们能否一生一世都保持如此这般的耳鬓厮磨、心有灵犀？"},
                {"en": "Ladies and gentlemen, will you please stand? With every guitar string scar on my hand, I take this magnetic force of a man to be my lover.", "cn": "现场在座的各位尊贵女士们先生们，请大家全体起立为我们见证！凭借着我手上因弹奏吉他琴弦磨出的每一道岁月茧疤为誓，我郑重接纳眼前这位散发着无穷引力魅力的男儿成为我的终身伴侣！"},
                {"en": "My heart's been borrowed and yours has been blue; all's well that ends well to end up with you.", "cn": "我的心扉曾经漂泊借宿于错的人之手，而你过往的岁月也曾饱尝忧郁阴霾；然而这世间只要最终能与你修成正果白头偕老，一切曾经受过的苦难便皆化作了甘之如饴的圆满恩赐！"},
                {"en": "Swear to be overdramatic and true to my lover.", "cn": "我庄严起誓：在我的挚爱面前，我愿毫无保留展露我所有的抓马情绪，并奉献出我此生最赤诚纯真的忠贞！"},
                {"en": "And you'll save all your dirtiest jokes for me, and at every table, I'll save you a seat.", "cn": "而你也必须把那些最无厘头、最荤素不忌的幽默笑话独家留给我一人听；在往后人生的每一张宴席餐桌前，我都会雷打不动为你身畔预留一个专属坐席！"},
                {"en": "The gentle 6/8 waltz tempo evokes timeless vintage romance and acoustic intimacy.", "cn": "舒缓起伏的八分之六拍传统复古慢华尔兹圆舞曲节拍，完美唤醒勾勒出了一种跨越时代鸿沟的古雅浪漫情怀与纯粹民谣亲密感。"},
                {"en": "True domestic bliss is celebrating the sacred mundane alongside the person who anchors your soul.", "cn": "人间真正的世俗天伦之乐，莫过于同那个能彻底安抚你浮躁灵魂的知心伴侣，并肩在柴米油盐的琐碎烟火平凡日子里，品味出神圣伟大的幸福滋味。"},
                {"en": "You're my, my, my, my lover; forever and ever, my heart is your permanent home.", "cn": "你是我此生生生世世的至爱伴侣；执子之手与子偕老，我的心房，将永远是你遮风避雨的终极永久港湾！"}
            ]
        },
        {
            "title": "第 9 首 · Champagne Problems · 香槟难题与落荒而逃的求婚夜",
            "description": "冬夜大学校园里的拒绝求婚悲剧，天鹅绒戒指盒与各自珍重的人生抉择。",
            "sentences": [
                {"en": "You booked the night train for a reason, so you could sit there in this hurt.", "cn": "你之所以特意执拗预订了那趟深夜开行的末班长途绿皮火车，就是为了能独自一人在晃荡的车厢里品尝这锥心刺骨的失落之痛。"},
                {"en": "Bustling crowds or silent sleepers, you're not sure which is worse.", "cn": "车窗外是熙熙攘攘的喧嚣人流，车厢内是沉睡不语的死寂乘客；你甚至迷茫吃不准这二者之中究竟哪一种更让你感到窒息痛苦。"},
                {"en": "Because I dropped your hand while dancing, left you out there standing crestfallen on the landing.", "cn": "只因在方才那场华尔兹旋转的至高点，我却毫无征兆松开了你紧握的温热手掌，任由你神情落魄、面如死灰地呆呆僵立在楼梯转角的平台阴影里。"},
                {"en": "Champagne problems; your mom's ring in your pocket, my soft-spoken 'no' that shattered the festive room.", "cn": "所谓上流社会的“香槟难题”；你裤兜里原本紧紧揣着你母亲祖传的昂贵钻戒，而我那句轻声细语吐露出的冰冷拒绝，却瞬间将整个满堂欢庆的屋宇震得粉碎。"},
                {"en": "Your sister splashed out on the bottle of Dom Pérignon, now she's drinking it from the neck alone in the kitchen.", "cn": "你的亲姐姐为了今晚的大喜庆典不惜一掷千金订购了昂贵的唐·培里侬顶级香槟，而此时此刻，她却只能独自一人蜷缩在厨房水槽边对着冰冷瓶口对嘴猛灌借酒浇愁。"},
                {"en": "Your mom's speech to the family was completely ruined; she had prepared toasts to the brilliant future bride.", "cn": "你母亲原本精心背诵多日的感人家族答谢祝词彻底化作了尴尬泡影；她事先甚至早已热情洋溢地准备好向全场宾客隆重介绍她这位未来的杰出儿媳妇。"},
                {"en": "How evergreen, our group of friends was whispering in horror: She would have made such a lovely bride, what a shame she's fucked in the head.", "cn": "往日同窗好友们在走廊窃窃私语倒吸冷气：她本该出落成一位多么明艳动人的端庄新娘啊，只可惜这姑娘脑瓜子纯属坏掉了彻底疯癫了，真是太丢人现眼了！"},
                {"en": "I never was ready so I watch you go; sometimes you just don't know the answer 'til someone's on their knees.", "cn": "我骨子里从始至终就根本没有做好步入婚姻坟墓的准备，所以我只能眼睁睁放任你转身离去；有时候一个人若非被逼到对方单膝跪地求婚的绝境边缘，甚至连你自己都无法参透内心的真实答案。"},
                {"en": "The flaws in a relationship often remain invisible until illuminated by the harsh spotlight of a proposal.", "cn": "两性亲密关系中深藏暗涌的致命裂痕与价值观分歧，往往在平日里被粉饰太平掩盖得天衣无缝，直到被求婚仪式那盏刺目无情的聚光灯骤然照亮！"},
                {"en": "One day, a girl will hold your hand and she will look at that heirloom ring and say yes with unhesitating tears.", "cn": "终有一天，会有另一个好姑娘深情握紧你的双手，她会满怀热泪凝视着那枚祖传家宝钻戒，毫不犹豫、满心笃定地点头答应嫁给你！"},
                {"en": "She'll patch up your tapestry that I shredded with my doubt, and she'll make you forget the winter night you bled on the rug.", "cn": "她会亲手用温柔细线重新缝补好当年被我的迟疑决绝撕成碎布条的斑斓人生挂毯，她会让你彻底忘却那个你曾跪在地毯上心碎淌血的酷寒冬夜。"},
                {"en": "You won't remember my face or the sound of my voice when her golden laughter fills your quiet hallways.", "cn": "当那个对的人银铃般清脆欢畅的笑声充盈溢满你空旷清幽的走廊玄关时，你记忆深处早已不会再记起我的容颜，或是听到我那令人作呕的推脱辞藻。"},
                {"en": "No harm was intended, yet the polite rejection inflicted catastrophic damage on an innocent soul.", "cn": "虽然施加拒绝的一方并无刻意蓄谋害人之心，但那声体面礼貌的回绝，却实打实给一颗赤诚无辜的滚烫心灵造成了毁灭性的核爆级惨烈重创。"},
                {"en": "Some love stories are destined to remain incomplete elegies etched on a freezing platform in upstate New York.", "cn": "有些轰轰烈烈的爱情传奇，生来注定就只能沦为一首未完成的凄美挽歌，被永远冰封镌刻在纽约州北部那个大雪纷飞的寒夜站台长凳之上。"},
                {"en": "You'll find the real thing and it will feel effortless; sleep peacefully tonight, my friend, the debt is paid.", "cn": "你终将寻觅到属于你命中注定的真正良缘，而且那份爱意降临时必定水到渠成、毫不费力；今夜请务必安详入眠吧我的故友，你我前世今生的欠债羁绊，今夜已尽数两讫结清。"}
            ]
        },
        {
            "title": "第 10 首 · The Archer · 弓箭手与灵魂深处的脆弱自白",
            "description": "合成器极简心跳律动，关于防御机制、创伤后应激与渴望被真正看见的孤勇。",
            "sentences": [
                {"en": "Combat, I'm ready for combat; I say I don't want that, but what if I do?", "cn": "战斗，随时做好浴血搏杀的万全戒备；我嘴上千百次矢口否认宣称自己讨厌冲突内耗，但倘若我内心深处其实渴望开战呢？"},
                {"en": "Cause cruelty wins in the movies; I've got a hundred thrown-out speeches I almost said to you.", "cn": "只因在那些经典的现实残酷电影里，心狠手辣的冷血恶人往往笑到了最后；我肚子里积压了上百篇原本差点就要当面对你声泪俱下倾诉的废弃腹稿。"},
                {"en": "Easy they come, easy they go; I jump from the train, I ride off alone.", "cn": "那些口口声声说爱我的人来得轻巧容易，走得更是毫无留恋干脆利落；我索性在飞驰的列车上半途决然跳车，独自一人策马扬鞭策马奔向苍凉荒原。"},
                {"en": "I never grew up, it's getting so old; help me hold onto you.", "cn": "我仿佛永远被困在童年的创伤里从未真正心智成熟长大，这出逃避现实的无聊把戏我自己都厌倦作呕了；请你伸出温暖双手，帮我紧紧拉住你不要放手！"},
                {"en": "I've been the archer, I've been the prey; who could ever leave me, darling? But who could stay?", "cn": "在漫长残忍的人世狩猎场里，我曾化身张弓搭箭冷酷无情的凶残猎手，也曾沦为任人宰割仓皇奔逃的绝望猎物；这世间有谁当真能舍得彻底舍弃我呢亲爱的？可又有谁真正有耐心能长久留守在我身旁呢？！"},
                {"en": "Dark side, I search for your dark side; cause what if I'm alright, right, right, right here?", "cn": "阴暗面，我总是在神经质般病态搜寻窥探着你人格深处可能藏匿的阴暗面；因为倘若我眼下的状态其实安然无恙，我又该如何说服自己相信这幸福是真实的？"},
                {"en": "And I cut off my nose just to spite my face, then I hate my reflection for years and years.", "cn": "我常常干出那种为了跟旁人赌气斗狠而不惜自残自毁、杀敌一千自损八百的蠢事，随后又在漫长数年里厌恶痛恨镜子里的这副丑陋皮囊。"},
                {"en": "I wake in the night, I pace like a ghost; the room is on fire, invisible smoke.", "cn": "我总在夜半惊魂梦回中惊慌醒来，如同一具游魂野鬼般在空荡荡的房间里焦躁踱步；整个卧室仿佛早已燃起了熊熊大火，弥漫着凡人肉眼不可见的窒息浓烟。"},
                {"en": "And all of my heroes die all alone; help me hold onto you.", "cn": "而我从小到大在书中膜拜敬仰的所有孤勇大英雄，他们生前无一不是在万念俱灰的极度孤独中孤苦伶仃悲惨离世；求求你抱紧我，帮我握紧你的手！"},
                {"en": "I've been the archer, I've been the prey; who could ever leave me, darling? But who could stay?", "cn": "我既曾是冷血放箭的弓箭手，也曾是泣血逃亡的惊弓之鸟；试问天下谁能彻底离弃我？可放眼人世又有谁能不离不弃生死相依？"},
                {"en": "All the king's horses and all the king's men couldn't put me together again.", "cn": "哪怕调集倾动全王国所有的威武战马与精锐重甲禁卫军团，也休想有能耐把我这颗早已摔得粉身碎骨的残破心脏重新拼凑粘合如初！(经典鹅妈妈童谣隐喻)"},
                {"en": "Cause all of my enemies started out friends; help me hold onto you.", "cn": "只因我此生遭遇过所有恨我入骨的仇敌宿敌，当年在最开始相识时，全都是与我推杯换盏无话不谈的挚友手足；求你帮我拉住你！"},
                {"en": "Every defense mechanism is built to protect a soft vulnerability from being violated again.", "cn": "一个人在周身筑起的每一层看似冰冷多刺、拒人千里之外的防御铜墙铁壁，其底层初衷无一不是为了守护心底最柔软处免遭再次蹂躏撕碎。"},
                {"en": "They see right through me, they see right through me; can you see me? I see you.", "cn": "他们自以为能看穿我的一切伪装，他们自鸣得意洞悉我的全部虚实；而眼前的你当真能看清面具下真实的我吗？——我能看清你，我始终在深情注视着你。"},
                {"en": "I've been the archer, but tonight I put the arrows away; take my trembling hand and walk beside me.", "cn": "我曾是百发百中、杀人诛心的冷血弓箭手，但在今夜，我心甘情愿收起弓弦利箭；请握紧我颤抖的手掌，与我并肩漫步在真实的阳光之下。"}
            ]
        }
    ]))

    return courses
