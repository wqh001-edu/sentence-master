# -*- coding: utf-8 -*-
from builder_core import build_course

def get_music_part1():
    courses = []

    # 1. 《披头士乐队》(The Beatles) · 10 章全集
    courses.append(build_course({
        "id": "course-mus-beatles",
        "title": "《披头士乐队》(The Beatles) · 摇滚史诗与英伦时代金曲 (10章全集)",
        "category": "music",
        "categoryName": "音乐英语",
        "coverGradient": "from-amber-600 via-yellow-600 to-emerald-700",
        "icon": "🎸",
        "description": "利物浦四人组改写全球流行音乐史，Hey Jude、Yesterday、Let It Be 诗意歌词全收录。",
        "difficulty": "初级 A2",
        "tags": ["披头士", "摇滚经典", "时代金曲", "诗意歌词"]
    }, [
        {
            "title": "第 1 首 · Hey Jude · 抚平伤痛与向爱敞开心扉",
            "description": "保罗·麦卡特尼写给约翰·列侬幼子朱利安的温暖抚慰神曲。",
            "sentences": [
                {"en": "Hey Jude, don't make it bad; take a sad song and make it better.", "cn": "嘿，朱迪，别沮丧气馁；哪怕是一首忧伤的歌，也能让它变得更加明亮动听。"},
                {"en": "Remember to let her into your heart, then you can start to make it better.", "cn": "记住要勇敢敞开心扉将她迎入心底，唯有如此，生活才会慢慢好起来。"},
                {"en": "Hey Jude, don't be afraid; you were made to go out and get her.", "cn": "嘿，朱迪，不要心生畏惧；你生来就注定要昂首阔步去赢得属于你的挚爱。"},
                {"en": "The minute you let her under your skin, then you begin to make it better.", "cn": "当你真切感受到她的温存渗入肌肤骨髓的那一秒，美好的人生便就此拉开序幕。"},
                {"en": "And anytime you feel the pain, hey Jude, refrain; don't carry the world upon your shoulders.", "cn": "每当你被刺骨的伤痛紧紧包围时，嘿朱迪，请适时放手止步；千万别把整个世界的沉重枷锁统统扛在自己单薄的双肩之上。"},
                {"en": "For well you know that it's a fool who plays it cool by making his world a little colder.", "cn": "因为你心里比谁都清楚：唯有自欺欺人的傻瓜，才会靠着故作冷漠高傲，把自己的生活天地变得更加荒凉冰冷。"},
                {"en": "Hey Jude, don't let me down; you have found her, now go and get her.", "cn": "嘿，朱迪，千万别让我失望；既然你已在茫茫人海中寻觅到了她，现在就勇敢去追吧！"},
                {"en": "You have found her, now go and get her, make a start from the very beginning.", "cn": "既然你已经在人群中觅得了她，现在就勇敢迈步启程，去开辟崭新的生活吧。"},
                {"en": "So let it out and let it in, hey Jude, begin; you're waiting for someone to perform with.", "cn": "把胸中的郁闷宣泄而出，迎入崭新的空气；嘿朱迪，启程吧，你其实一直在静待那个与你携手登台合奏一生的伴侣。"},
                {"en": "And don't you know that it's just you, hey Jude, you'll do, the movement you need is on your shoulder.", "cn": "难道你当真不知道能拯救你的人只有你自己吗？嘿朱迪，你一定行！你所渴望的每一步跨越，全凭你自己的臂膀奋起挥动！"},
                {"en": "The movement you need is on your shoulder, carrying hope and resilience forward.", "cn": "你所需要的变革与力量就担在你的肩头，承载着希望与坚韧勇往直前。"},
                {"en": "Better, better, better, better, better, yeah!", "cn": "越来越好，越来越明媚，去拥抱更加灿烂的明天吧！"},
                {"en": "Na, na, na, na-na-na na, na-na-na na, hey Jude!", "cn": "啦，啦，啦，全场大合唱这跨越时代的治愈欢歌，嘿朱迪！"},
                {"en": "A timeless anthem of unconditional love, compassion, and shared healing.", "cn": "这是一曲跨越世纪长河、承载着无条件大爱、悲悯与集体心灵疗愈的不朽赞歌。"},
                {"en": "Music has the transcendental power to transform personal tragedy into universal solace.", "cn": "动人的音乐拥有一种超凡入圣的奇妙伟力，足以将孤立无援的个人悲剧化作全人类共同的精神慰藉。"}
            ]
        },
        {
            "title": "第 2 首 · Yesterday · 昨天与昨日的无忧时光",
            "description": "吉尼斯世界纪录被翻唱次数最多的名曲，保罗吉他独奏与弦乐四重奏。",
            "sentences": [
                {"en": "Yesterday, all my troubles seemed so far away.", "cn": "在昨日的温柔时光里，我心头所有的烦恼忧愁仿佛都远在天涯海角。"},
                {"en": "Now it looks as though they're here to stay; oh, I believe in yesterday.", "cn": "而如今风雨飘摇，它们却好似驻足不走与我如影随形；噢，我多么渴望能够重回昨天。"},
                {"en": "Suddenly, I'm not half the man I used to be.", "cn": "仿佛就在骤然之间，我已然丧失了昔日那个意气风发男儿的一半自信与神采。"},
                {"en": "There's a shadow hanging over me; oh, yesterday came suddenly.", "cn": "有一抹挥之不去的阴郁黑影长久笼罩在我的头顶；噢，残酷的昨日变迁来得竟是这般猝不及防。"},
                {"en": "Why she had to go, I don't know, she wouldn't say.", "cn": "她究竟为何毅然决然弃我而去，我至今百思不得其解，而她也自始至终未曾吐露半句。"},
                {"en": "I said something wrong, now I long for yesterday.", "cn": "定是我当年无心说错了什么混账话，才落得如今我只能在孤灯下日夜苦苦追忆昨天。"},
                {"en": "Yesterday, love was such an easy game to play.", "cn": "在昨天，爱情宛如一场轻松愉快、信手拈来的纯真游戏。"},
                {"en": "Now I need a place to hide away; oh, I believe in yesterday.", "cn": "而此时此刻，我却只想在这冰冷人世间寻觅一处能让我逃避现实的隐秘角落；噢，我多么坚信昨天。"},
                {"en": "The melancholic solo acoustic guitar arpeggios perfectly frame the heartbreak.", "cn": "那把略带忧郁感伤的古典木吉他独奏分解和弦，近乎无可挑剔地烘托勾勒出了失恋的锥心之痛。"},
                {"en": "George Martin's elegant string quartet arrangement elevates the ballad into high art.", "cn": "传奇制作人乔治·马丁操刀编曲的典雅弦乐四重奏，一举将这首民谣小调升华成了殿堂级的高雅艺术。"},
                {"en": "Memory is both a golden sanctuary and a bittersweet prison for the human soul.", "cn": "记忆对于脆弱的人类心灵而言，既是一座繁花似锦的黄金庇护所，也是一座五味杂陈的苦涩牢笼。"},
                {"en": "We rarely appreciate the peace of the present until it slips irrevocably into the past.", "cn": "在现实生活中，我们极少懂得真正珍惜当下的安宁美好，直到它无可挽回地沉入泛黄的历史长河。"},
                {"en": "Why she had to go, I don't know, she wouldn't say.", "cn": "她究竟为何决然离开，我一无所知，她也从未给出答案。"},
                {"en": "I said something wrong, now I long for yesterday.", "cn": "想必是我言语唐突犯下了大错，才让我如今在悔恨中日夜渴望昨日重现。"},
                {"en": "Yesterday, love was such an easy game to play; oh, I believe in yesterday.", "cn": "在昨天，相爱曾是何等纯粹自然的一桩幸事；噢，我至死深信昨日的美好！"}
            ]
        },
        {
            "title": "第 3 首 · Let It Be · 随它去吧与智慧之光",
            "description": "梦见已故母亲玛丽带来的宽慰，在迷茫幽暗的岁月里顺其自然、心向光明。",
            "sentences": [
                {"en": "When I find myself in times of trouble, Mother Mary comes to me.", "cn": "每当我身陷人生风雨飘摇、四面楚歌的动荡艰难时刻，母亲玛丽总会温柔来到我的梦境身旁。"},
                {"en": "Speaking words of wisdom, let it be.", "cn": "在她唇边轻吐出充满无上智慧的慈爱箴言：孩子，且由它去吧，顺其自然。"},
                {"en": "And in my hour of darkness, she is standing right in front of me.", "cn": "而在我人生最至暗绝望、伸手不见五指的晦暗时刻，她依旧慈眉善目伫立在我的眼前。"},
                {"en": "Speaking words of wisdom, let it be.", "cn": "谆谆教导着平复心灵的智慧密语：随它去吧，一切顺其自然。"},
                {"en": "Let it be, let it be, let it be, let it be; whisper words of wisdom, let it be.", "cn": "随它去吧，放下执念，顺应天地造化；轻声呢喃着智慧良言，坦然接纳现实。"},
                {"en": "And when the broken-hearted people living in the world agree, there will be an answer, let it be.", "cn": "当这世间千千万万饱尝心碎苦难的无辜苍生心意相通达成共鸣时，迷雾终将散去迎来答案：且由它去吧。"},
                {"en": "For though they may be parted, there is still a chance that they will see; there will be an answer, let it be.", "cn": "虽然相爱之人此刻或许被迫天各一方被现实拆散，但冥冥之中依然有重逢相见的希望；命运终会给出答案，顺其自然。"},
                {"en": "And when the night is cloudy, there is still a light that shines on me.", "cn": "哪怕今夜的天穹乌云翻滚、阴霾密布，依然会有一缕穿透云层的明灯静静沐浴照耀在我身侧。"},
                {"en": "Shine until tomorrow, let it be.", "cn": "它将彻夜长明一直照亮至灿烂黎明的降临，由它去吧，坦荡如水。"},
                {"en": "I wake up to the sound of music, Mother Mary comes to me.", "cn": "我在优美清脆的琴声乐章之中悠然苏醒，梦中的母亲再次向我投来温暖慈爱的笑意。"},
                {"en": "Speaking words of wisdom, let it be.", "cn": "口中依旧轻语着永恒安详的智慧：凡事顺其自然，莫向外求。"},
                {"en": "Billy Preston's soulful Hammond organ chords wash over the chorus like a warm embrace.", "cn": "比利·普雷斯顿弹奏的灵魂乐风琴和弦如暖流般流淌过副歌，宛如一个宽广包容的温暖拥抱。"},
                {"en": "Acceptance is not defeat; it is the spiritual tranquility that allows resilience to grow.", "cn": "学会坦然接纳与顺其自然绝非懦弱认输；它是让心灵归于沉静祥和、让坚韧意志重新生根发芽的肥沃沃土。"},
                {"en": "There will be an answer; let the turbulent river flow until the water clears.", "cn": "一切纷扰终将迎来答案；且放手任凭汹涌湍急的河流自行奔涌，直到泥沙沉淀、水落石出。"},
                {"en": "Let it be, let it be, let it be; whisper words of wisdom, let it be.", "cn": "随它去吧，放下焦虑，且由它去吧；在心头轻声颂念那句智慧箴言：一切皆是最好的安排。"}
            ]
        },
        {
            "title": "第 4 首 · Across the Universe · 穿梭宇宙与无休止的文字流淌",
            "description": "约翰·列侬最具禅意与诗意哲思的迷幻杰作，梵文真言吉祥颂。",
            "sentences": [
                {"en": "Words are flowing out like endless rain into a paper cup.", "cn": "无休止的字句宛如一场永不停歇的细雨，连绵不断地淌入一只脆弱薄小的纸杯之中。"},
                {"en": "They slither wildly as they slip away across the universe.", "cn": "它们在滑落飞驰横渡浩瀚大千宇宙的征程中，如蛇信般狂野蜿蜒盘旋穿梭。"},
                {"en": "Pools of sorrow, waves of joy are drifting through my opened mind, possessing and caressing me.", "cn": "一汪汪幽暗的悲伤水潭与一阵阵欢欣的喜悦狂澜，静静漂流穿行过我敞开的心灵原野，轻抚拥抱着我的灵魂。"},
                {"en": "Jai guru deva, om; nothing's gonna change my world.", "cn": "致敬崇高的神圣导师，唵（宇宙之音）；这凡尘间没有任何狂风暴雨能够动摇改变我的内心世界。"},
                {"en": "Nothing's gonna change my world; nothing's gonna change my world.", "cn": "再也没有任何事物能扰乱我宁静的心湖；这世间万物休想改变我的内心世界！"},
                {"en": "Images of broken light which dance before me like a million eyes, they call me on and on across the universe.", "cn": "那万千破碎折射的光斑浮影宛如无数只灵动的眼眸般在我面前翩跹起舞，一声声深情呼唤引领我横渡整个大千宇宙。"},
                {"en": "Thoughts meander like a restless wind inside a letter box.", "cn": "思绪如同一股被困在逼仄邮箱深处躁动不安的夜风，在方寸之间无休止地蜿蜒打转回旋。"},
                {"en": "They tumble blindly as they make their way across the universe.", "cn": "它们在向着茫茫宇宙彼岸奋力冲锋的迢迢旅途中，跌跌撞撞盲目翻滚前行。"},
                {"en": "Jai guru deva, om; inner stillness is the greatest sanctuary in existence.", "cn": "梵音缭绕，敬奉至高神圣；心灵内在的从容入定，乃是这大千尘世间最神圣不可侵犯的至高殿堂。"},
                {"en": "Sounds of laughter, shades of life are ringing through my open ears, inciting and inviting me.", "cn": "银铃般的欢声笑语与斑斓多姿的生命阴晴圆缺，悠扬穿透我倾听的双耳，热情挑逗并盛情邀请着我纵情入世。"},
                {"en": "Limitless, undying love which shines around me like a million suns, it calls me on and on across the universe.", "cn": "无边无际、万世不朽的浩瀚大爱宛如千万个烈日骄阳般在我身畔璀璨普照，长久呼唤引领我横越整片浩瀚宇宙！"},
                {"en": "Lennon considered this lyric one of the purest pieces of poetry he ever composed.", "cn": "列侬生前将这首词作奉为他毕生创作生涯中在文学艺术意境上最纯粹纯洁、最接近神性的诗意篇章。"},
                {"en": "The Sanskrit mantra grounds the mind in transcendental, meditative peace.", "cn": "那段古老而神秘的梵文吉祥真言，能够让浮躁的心智彻底沉淀在超凡入圣、天人合一的静谧禅境之中。"},
                {"en": "Let your consciousness expand beyond the mundane horizons of petty material squabbles.", "cn": "放开你被世俗琐碎绑架的狭隘视野吧，任由你的精神意念超凡跃升，自由翱翔在超越凡尘琐事的浩瀚星河之上。"},
                {"en": "Nothing's gonna change my world; love radiates across the celestial sphere eternally.", "cn": "休想有任何外力能够撼动我内心的宁静神殿；真理与大爱将在天穹诸界永远生生不息、普照大千！"}
            ]
        },
        {
            "title": "第 5 首 · Here Comes the Sun · 严冬散尽与暖阳破冰",
            "description": "乔治·哈里森在埃里克·克莱普顿后花园弹吉他写下的治愈神曲。",
            "sentences": [
                {"en": "Here comes the sun, doo-doo-doo-doo; here comes the sun, and I say: It's all right.", "cn": "瞧啊，温暖的太阳升起来了！瞧啊，金灿灿的阳光普照大地，我由衷欢呼道：一切都会好起来的！"},
                {"en": "Little darling, it's been a long, cold, lonely winter.", "cn": "亲爱的小家伙，我们刚刚熬过了一场多么漫长严酷、寒冷刺骨且孤独寂寥的凛冬岁月啊。"},
                {"en": "Little darling, it feels like years since it's been here.", "cn": "亲爱的小宝贝，那久违的春日暖阳仿佛已经与我们阔别了整整几个漫长的世纪之久。"},
                {"en": "Here comes the sun, here comes the sun, and I say: It's all right.", "cn": "太阳升起来了，灿烂的曙光终于冲破阴霾破冰而至，我笑着告诉身畔的你：一切灾难都已过去！"},
                {"en": "Little darling, the smiles returning to the faces.", "cn": "亲爱的小家伙，快看街上行人的脸颊上，久违温存的灿烂微笑正一朵朵重新绚烂绽放。"},
                {"en": "Little darling, it seems like years since it's been here.", "cn": "亲爱的小宝贝，那些充满希望的欢声笑语，仿佛也同严冬一样阔别了我们太久太久。"},
                {"en": "Here comes the sun, and I say: It's all right.", "cn": "太阳高高升起了，我轻声告诉你：寒冬已过，万物皆安。"},
                {"en": "Sun, sun, sun, here it comes; warm rays thawing the frozen soil.", "cn": "暖阳，骄阳，炽热的生命之光，瞧它正带着勃勃生机扑面而来，温柔消融着冻结如铁的冰霜沃土。"},
                {"en": "Little darling, I feel that ice is slowly melting.", "cn": "亲爱的小家伙，我分明已经能够真切听见、真切感受到那深藏在心底的坚冰正一寸寸悄然融化。"},
                {"en": "Little darling, it seems like years since it's been clear.", "cn": "亲爱的小宝贝，这般碧空如洗、万里无云的明媚晴朗好天气，仿佛我们已经苦苦企盼了整整数年。"},
                {"en": "Here comes the sun, here comes the sun, and I say: It's all right.", "cn": "太阳升起来了，曙光普照人间，我由衷欢唱：一切都会好起来的！"},
                {"en": "Harrison wrote this luminous acoustic masterpiece playing hooky from boardroom business meetings.", "cn": "哈里森当年正是为了逃避苹果唱片公司那些令人窒息、勾心斗角的无休止董事会纠纷，才偷偷溜进好友花园写下了这首旷世杰作。"},
                {"en": "The seven-eight time signature subtly shifts, creating a bright skipping rhythm of joy.", "cn": "八分之七拍与偶数节拍之间灵动精妙的切分音转换，勾勒出了一种如小鹿欢畅轻快跳跃般的纯粹欢愉节奏。"},
                {"en": "No winter lasts forever; no spring skips its destined chronological turn.", "cn": "这人世间没有任何一场残酷的风雪严冬能够永远肆虐称霸；也绝没有任何一个生机盎然的暖春会缺席它的归期。"},
                {"en": "It's all right; step out into the golden morning and let your heart thaw.", "cn": "一切安好，万物复苏；让我们勇敢迈步踏入金灿灿的晨曦暖阳之中，彻底融化心中所有冰霜阴霾！"}
            ]
        },
        {
            "title": "第 6 首 · In My Life · 岁月留痕与一生挚爱",
            "description": "列侬回望故乡利物浦的车站与故人，世间风景无数，唯你不可替代。",
            "sentences": [
                {"en": "There are places I'll remember all my life, though some have changed.", "cn": "在这片辽阔天地之间，有那么几处故土角落我将铭刻终生不忘，尽管时光荏苒它们早已物是人非。"},
                {"en": "Some forever, not for better; some have gone and some remain.", "cn": "有些变迁令人唏嘘，并非变得更好；有些曾经熟悉的老街已彻底灰飞烟灭，有些则依旧坚守伫立。"},
                {"en": "All these places had their moments with lovers and friends I still can recall.", "cn": "所有这些承载着青春记忆的街角巷尾，都曾定格过我与昔日爱侣和莫逆挚友共度的难忘光辉岁月。"},
                {"en": "Some are dead and some are living; in my life, I've loved them all.", "cn": "昔日同行的故人中如今有的早已黄土白骨长眠地下，有的依然健在人世；回首我这一生，我曾全心全意深爱过他们每一个人。"},
                {"en": "But of all these friends and lovers, there is no one compares with you.", "cn": "然而放眼所有这些在我生命画卷中穿梭走过的故人挚友与昔日红颜，却没有任何一个人能够与你相提并论！"},
                {"en": "And these memories lose their meaning when I think of love as something new.", "cn": "每当我在心灵深处将我们此刻的真挚大爱奉为全新圣洁的神圣存在时，那些过往的泛黄记忆都瞬间黯然失色。"},
                {"en": "Though I know I'll never lose affection for people and things that went before.", "cn": "虽然我心里清楚我永远绝不会丧失对过往岁月里相逢过的人与物那份深情眷恋。"},
                {"en": "I know I'll often stop and think about them, in my life I love you more.", "cn": "我也深知未来的我依然会时常驻足停下脚步深情回望他们，但在我这一生之中，我更深爱的是你！"},
                {"en": "George Martin recorded the baroque piano solo at half-speed, creating a harpsichord texture.", "cn": "传奇制作人乔治·马丁在录音时特意采用了半速降速录制巴洛克风格钢琴独奏，从而营造出了一种如羽管键琴般典雅复古的奇妙质感。"},
                {"en": "Nostalgia is an honorable emotion when tempered by genuine devotion to the living present.", "cn": "对过往青春的怀旧追思本是一种崇高美好的情感，但唯有当它与对当下鲜活生活的全情投入交织融汇时，才显弥足珍贵。"},
                {"en": "In my life, I love you more; no comparison can diminish this sacred vow.", "cn": "回首我这一生跌宕起伏，我独爱你至深；没有任何世俗的衡量与对比，能够折损冲淡这句神圣的山盟海誓。"},
                {"en": "People enter our journey to shape our character, but only one anchors our destiny.", "cn": "无数过客匆匆闯入我们的人生旅程，只为磨砺雕琢我们的性格心智；但唯独只有一人，能真正化作守护我们命运的沉稳锚链。"},
                {"en": "Treasure every scar and every companion that walked beside you through the rain.", "cn": "由衷珍视你在漫长风雨岁月中留下的每一道伤疤吧，也深深感恩每一个曾打着雨伞陪你踏过泥泞的并肩之人。"},
                {"en": "Though the scenery shifts with the seasons, true loyalty remains unaltered like bedrock.", "cn": "纵然窗外的良辰美景伴随着四季更迭而沧海桑田，但坚贞不渝的赤诚誓约却如山川基岩般万世长存！"},
                {"en": "In my life, I've loved them all, but in my life, I love you more.", "cn": "回眸我这一生漫漫长路，我曾坦荡深爱过沿途的所有故人，但在这滚烫一生里，我爱你胜过世间万物！"}
            ]
        },
        {
            "title": "第 7 首 · Something · 举手投足间的绝美爱情",
            "description": "弗兰克·辛纳屈盛赞为有史以来最伟大的情歌，哈里森写给妻子帕蒂·贝克。",
            "sentences": [
                {"en": "Something in the way she moves attracts me like no other lover.", "cn": "她举手投足、款款漫步之间所流露出的那份超凡脱俗的神韵，深深吸引着我，世间没有任何红颜能够与她相媲美。"},
                {"en": "Something in the way she woos me; I don't want to leave her now, you know I believe and how.", "cn": "她温存软语脉脉含情打动我的奇妙方式；让我此刻无论如何也舍不得离开她身侧半步，你知道我对这份爱坚信不疑。"},
                {"en": "Somewhere in her smile she knows that I don't need no other lover.", "cn": "在她唇边绽放那一抹温存浅笑的深处，她心里比谁都清楚：我今生今世再也无需寻觅任何其他的伴侣。"},
                {"en": "Something in her style that shows me; I don't want to leave her now, you know I believe and how.", "cn": "她举手投足间那抹与生俱来的独特韵味清晰昭示着我；我此生只想与她长相厮守寸步不离，你深知我的爱意何其坚定。"},
                {"en": "You're asking me will my love grow; I don't know, I don't know.", "cn": "你含情脉脉地柔声问我：我们之间的深厚爱意日后是否还会继续疯长？——这我可真不敢断言，我确实无法预知未来。"},
                {"en": "You stick around, now it may show; I don't know, I don't know.", "cn": "只要你愿意一生常伴在我身侧，答案或许便会在漫长岁月中水落石出；我无法用言语保证，让时间去证明吧。"},
                {"en": "Something in the way she knows and all I have to do is think of her.", "cn": "她心灵深处那份洞悉一切的默契心意是如此神奇，以至于我所需要做的全部，仅仅只是在心头深情思念起她。"},
                {"en": "Something in the things she shows me; I don't want to leave her now, you know I believe and how.", "cn": "她向我娓娓展现出的那一幕幕世间纯美光景；让我此刻哪怕一分一秒也绝不愿同她分离，我的心早已非她莫属。"},
                {"en": "Frank Sinatra famously declared this track the greatest love song of the past fifty years.", "cn": "传奇歌王弗兰克·辛纳屈曾公开赞誉这首名作为：过去整整半个世纪以来全人类所创作出的最伟大的情歌巅峰！"},
                {"en": "Harrison's fluid guitar solo speaks with the expressive nuance of a human voice weeping.", "cn": "哈里森那段行云流水般优美深情的吉他独奏滑音，倾诉表达出的细腻情感宛如人类歌喉在动情啜泣。"},
                {"en": "True romantic fascination transcends mere physical aesthetics; it resides in a person's aura.", "cn": "人世间真正让人魂牵梦绕、甘愿沉沦的浪漫倾心，绝不仅仅停留在皮相容貌的浅薄层面；它深深植根于一个人的灵魂气场之中。"},
                {"en": "Uncertainty about tomorrow only makes the devotion of the present hour more precious.", "cn": "对未来岁月未知的敬畏与忐忑，恰恰让此时此刻毫无保留的深情托付变得更加弥足珍贵。"},
                {"en": "She carries a quiet grace that disarms cynicism and awakens dormant poetry in the soul.", "cn": "她浑身上下散发着一种润物细无声的高雅从容，足以瞬间缴械世间所有的冷酷犬儒，唤醒灵魂深处沉睡已久的诗意。"},
                {"en": "Love without possession; devotion without coercion; a pure expression of gratitude for existence.", "cn": "不带占有欲的炽热深爱，不施加任何道德绑架强求的赤诚托付；这是一曲对茫茫人海中能与她相遇由衷感恩的纯粹礼赞。"},
                {"en": "Something in the way she moves; I don't want to leave her now, you know I believe and how.", "cn": "她举手投足漫步之间的那抹绝代风华；令我此刻沉沦其中绝不愿离去，你知道我对她的一往情深何其坚定！"}
            ]
        },
        {
            "title": "第 8 首 · Blackbird · 黑鸟展翅与重获自由之歌",
            "description": "保罗为支持美国民权运动而作，在寂静深夜练习振翅高飞。",
            "sentences": [
                {"en": "Blackbird singing in the dead of night, take these broken wings and learn to fly.", "cn": "在万籁俱寂的漆黑深夜里凄美啼鸣的黑鸟啊，快快抖落身上的创伤，振动这双残破折断的双翼，学着展翅高飞吧！"},
                {"en": "All your life, you were only waiting for this moment to arise.", "cn": "在你漫长屈辱痛苦的一生之中，你从始至终唯独只是在隐忍等待着这一觉醒腾飞的神圣黎明时刻！"},
                {"en": "Blackbird singing in the dead of night, take these sunken eyes and learn to see.", "cn": "在深夜的无边黑暗中孤傲啼唱的黑鸟啊，快快睁开你那双饱尝风霜、深深凹陷的双眸，重新学着看清这辽阔天地吧！"},
                {"en": "All your life, you were only waiting for this moment to be free.", "cn": "在你漫长的一生之中，你一直在咬牙苦苦煎熬等待着这一刻——迎来重获自由的破茧新生！"},
                {"en": "Blackbird, fly! Blackbird, fly, into the light of a dark black night.", "cn": "黑鸟，振翅高飞吧！黑鸟，迎风翱翔吧，穿透这漆黑深邃的暗夜，向着黎明破晓的璀璨曙光勇往直前！"},
                {"en": "Blackbird singing in the dead of night, take these broken wings and learn to fly.", "cn": "黑鸟在子夜的冷风中坚定高歌，带上你饱经创伤的翅膀，去学会征服狂暴的长空！"},
                {"en": "All your life, you were only waiting for this moment to arise.", "cn": "你受尽苦难的漫长一生，皆是为了静待今日破晓腾飞的这一伟大历史瞬间。"},
                {"en": "McCartney composed this acoustic gem inspired by the struggles of the Civil Rights movement.", "cn": "麦卡特尼当年正是深受美国南部黑人民权抗争运动英勇风骨的深刻感召启发，才创作了这颗民谣璀璨明珠。"},
                {"en": "The rhythmic tapping throughout the recording is Paul's boot marking tempo on the wooden floor.", "cn": "整首录音室母带里贯穿始终的清脆富有节奏的叩击声，正是保罗脚上那双皮靴在地板上打出的沉稳拍子。"},
                {"en": "Oppression can shatter the physical feathers, but it can never extinguish the innate impulse toward liberty.", "cn": "残暴的强权压迫固然能打断鸟儿肉体上的羽毛翅膀，但它却休想扼杀生灵骨子里对自由奔放的崇高本能向往！"},
                {"en": "Every broken spirit retains the latent capability to heal, ascend, and soar above systemic injustice.", "cn": "这人世间每一个残破不堪、饱受摧残的受苦灵魂，体内都永远保留着自我疗愈、昂首崛起并傲然飞越体制不公的惊人潜能！"},
                {"en": "You were not born to remain caged in the dark canopy of historical oppression forever.", "cn": "你降临到这个壮丽的人世间，绝不是为了永远被囚禁在历史压迫制造的冰冷黑暗牢笼里苟活残喘！"},
                {"en": "Into the light of a dark black night, spread your wings and embrace the untamed sky.", "cn": "向着那刺破浓墨暗夜的曙光吧，尽情舒展你的双翼，去拥抱属于你的广袤苍穹！"},
                {"en": "A simple acoustic guitar and a tapping foot produced an enduring worldwide anthem of human dignity.", "cn": "一把朴素的木吉他，配上一只打着节拍的皮靴，竟奇迹般孕育出了一曲名垂青史、响彻全人类捍卫尊严的不朽颂歌。"},
                {"en": "All your life, you were only waiting for this moment to arise; fly free, blackbird, fly!", "cn": "你这一生漫长苦难的隐忍煎熬，皆是为了等待此时此刻的破晓觉醒；翱翔吧，黑鸟，向着自由去展翅高飞吧！"}
            ]
        },
        {
            "title": "第 9 首 · A Day in the Life · 浮生一日与惊世骇俗的交响乐",
            "description": "披头士巅峰概念专辑《佩珀中士》终曲，报纸新闻、平凡日常与四十人大管弦狂潮。",
            "sentences": [
                {"en": "I read the news today, oh boy, about a lucky man who made the grade.", "cn": "我今天在报纸上读到了一条轰动头条新闻，噢天呐，说的是一个年轻有为、刚刚取得傲人成就的体面幸运儿。"},
                {"en": "And though the news was rather sad, well, I just had to laugh; I saw the photograph.", "cn": "虽然那则车祸讣告读来颇令人伤感，但我却忍不住发出了一声荒诞的苦笑；只因我亲眼看到了报纸上印着的那张大照片。"},
                {"en": "He blew his mind out in a car; he didn't notice that the lights had changed.", "cn": "他驾驶着轿车狂飙突进把自己的脑袋撞得稀巴烂；当时他甚至根本没有留意到路口的交通指示红绿灯早已变了。"},
                {"en": "A crowd of people stood and stared; they'd seen his face before, nobody was really sure if he was from the House of Lords.", "cn": "一大群闲得发慌的围观路人站在马路边指指点点、看客般围观发呆；大家都觉得这张死者面孔眼熟得很，但谁也吃不准他究竟是不是某位贵族院的大老爷。"},
                {"en": "I'd love to turn you on, Lennon sang, as a forty-piece orchestra built into an avant-garde sonic swell.", "cn": "我多么渴望能彻底唤醒你们麻木的心智啊！列侬高亢唱诵道，此时四十人编制的庞大管弦乐团爆发出了前卫狂暴的音浪洪流！"},
                {"en": "Woke up, fell out of bed, dragged a comb across my head.", "cn": "早晨睡眼惺忪醒来，从床上跌跌撞撞爬起，胡乱抓起一把梳子在乱蓬蓬的头顶上随手扒拉两下。"},
                {"en": "Found my way downstairs and drank a cup, and looking up, I noticed I was late.", "cn": "摸索着下楼一口气灌下一大杯热茶，抬头瞥见挂钟的一刹那，我才惊觉自己赶早班车早已彻底迟到了。"},
                {"en": "Found my coat and grabbed my hat, made the bus in seconds flat.", "cn": "抓起大衣套上帽子夺门而出，在关门的最后生死几秒钟里，连滚带爬狼狈窜上了那辆双层红色公交巴士。"},
                {"en": "Made my way upstairs and had a smoke, and somebody spoke and I went into a dream.", "cn": "顺着狭窄的旋梯爬上巴士二层顶层点燃一支香烟，耳畔飘来旁人杂乱无章的闲言碎语，而我的思绪已然神游飘入虚无梦境之中。"},
                {"en": "I read the news today, oh boy: four thousand holes in Blackburn, Lancashire.", "cn": "今天我又在报纸版面上读到了一条荒诞奇闻，天呐：说是兰开夏郡的布莱克本镇马路上，竟然密密麻麻坑坑洼洼破损了整整四千个大泥坑！"},
                {"en": "And though the holes were rather small, they had to count them all; now they know how many holes it takes to fill the Albert Hall.", "cn": "虽然那些小泥坑一个个平平无奇微不足道，但市政官僚们却非要逐一清点统计一遍；如今他们终于自鸣得意算清了填满皇家阿尔伯特音乐厅究竟需要多少坑洞泥土！"},
                {"en": "The collision of Lennon's existential dread with McCartney's brisk morning routine created modern high art.", "cn": "列侬关于生死无常的存在主义哲学冷峻拷问，与麦卡特尼轻快滑稽的赶早班车凡尘日常迎面轰然相撞，碰撞出了改写流行音乐史的现代高雅艺术奇迹。"},
                {"en": "The final colossal E-major piano chord sustained for forty-two seconds, echoing into eternity.", "cn": "在终曲高潮处，三架大三角钢琴联手重重砸下的那一记惊天动地、持续共鸣回荡了长达四十二秒的庞大E大调和弦，久久回响在永恒时空深处。"},
                {"en": "It forced a generation of rock musicians to recognize that albums could be profound philosophical masterpieces.", "cn": "正是这尊无可匹敌的音乐里程碑，以泰山压顶之势逼迫整整一代摇滚音乐人深刻醒悟：一张黑胶唱片，完全可以是一部承载深刻哲学思辨的旷世绝伦艺术长卷！"},
                {"en": "I'd love to turn you on; awaken from the sleepwalk of mindless consumer routine and look around.", "cn": "我多么渴望能彻底唤醒你们那颗沉睡的心灵啊；快快从浑浑噩噩、毫无生机的庸常消费主义梦游长廊中睁开双眼，好好审视一番这个波澜壮阔的世界吧！"}
            ]
        },
        {
            "title": "第 10 首 · All You Need Is Love · 爱是一切所求与终极答案",
            "description": "全球首次卫星电视直播面向全球四亿观众献唱，披头士留给人类最伟大的精神遗产。",
            "sentences": [
                {"en": "There's nothing you can do that can't be done; nothing you can sing that can't be sung.", "cn": "这人世间没有任何你想做的事是真正无法办到的；也绝没有任何你想唱的歌是真正无法放声歌唱的。"},
                {"en": "Nothing you can say, but you can learn how to play the game; it's easy.", "cn": "没有什么话是你不能表达的，你尽可以从容学会玩转这人世间的处世规则；其实一切远比你想象的要简单轻松。"},
                {"en": "Nothing you can make that can't be made; no one you can save that can't be saved.", "cn": "没有任何你渴望铸就的伟业是绝不可能被创造出来的；也没有任何一个你渴望拯救的受苦之人是真正无可救药的。"},
                {"en": "Nothing you can do, but you can learn how to be you in time; it's easy.", "cn": "你无需强求面面俱到，你只需要在岁月沉淀中慢慢学会从容坦荡做真实的你自己；信赖自己，这其实容易得很。"},
                {"en": "All you need is love; all you need is love.", "cn": "你所需要的一切唯独只有爱；全人类所苦苦追寻的一切唯独只有爱！"},
                {"en": "All you need is love, love; love is all you need.", "cn": "唯有爱才是你一生的归宿与解药，大爱无疆；爱，便是一切你所必需的终极答案！"},
                {"en": "There's nothing you can know that isn't known; nothing you can see that isn't shown.", "cn": "这浩瀚天地间没有任何知识奥秘是永远无法被人类探知的；也没有任何天地景象是永远无法被肉眼瞻仰的。"},
                {"en": "There's nowhere you can be that isn't where you're meant to be; it's easy.", "cn": "你无论漫步身处何方，那里便正是命运早已精心为你安排驻足的天命之所；放平心态顺应造化，这其实简单至极。"},
                {"en": "Broadcast live via satellite to four hundred million people across thirty-one countries simultaneously.", "cn": "一九六七年夏天，披头士四人组通过人类历史上首颗全球通讯卫星直播，同时向遍布全球三十一个国家的一共四亿电视观众面对面深情献唱。"},
                {"en": "The marching French national anthem intro and snippets of Bach blended into a joyous celebration.", "cn": "雄壮威武的法国国歌小号前奏引子，与巧妙穿插融入其中的巴赫古典交响变奏相映成趣，汇聚成了一场普天同庆的和平大狂欢。"},
                {"en": "In a fractured world torn apart by ideological proxy wars, they offered a radical, simple universal truth.", "cn": "在一个被意识形态偏见与冷战代理人战争肆意撕裂得满目疮痍的动荡世界里，他们却反其道而行之，奉献出了一条最为返璞归真、洗尽铅华的终极普世真理。"},
                {"en": "Love is not a transactional commodity; love is the binding energetic glue of the entire cosmos.", "cn": "真正的至爱绝不是什么待价而沽、利益交换的世俗商品；爱是贯穿维系整个大千宇宙生生不息、和谐运转的终极精神引力黏合剂！"},
                {"en": "She loves you, yeah, yeah, yeah; yesterday's melodies echoed playfully in the joyful fade-out.", "cn": "她深深爱着你，耶，耶，耶！在终章渐渐淡出的欢快合唱声浪中，曾经风靡全球的昔日旋律幽默风趣地穿插回响。"},
                {"en": "The four lads from Liverpool permanently altered the cultural landscape of civilization with their musical genius.", "cn": "这四位来自英格兰利物浦平凡港口工人家庭的毛头小伙子，凭借着天马行空的惊世音乐才华，永远彻底重塑了整个人类现代文明的精神文化版图。"},
                {"en": "All you need is love; let the timeless message resound across all human hearts forever.", "cn": "你所追寻的全部唯独只有爱；让这句跨越世纪、超越种族国界的永恒真理，在全人类的心灵深处万世长久激荡回响！"}
            ]
        }
    ]))

    return courses
