# -*- coding: utf-8 -*-
from builder_core import build_course

def get_music_part3():
    courses = []

    # 4. 《阿黛尔》(Adele) · 10 章全集
    courses.append(build_course({
        "id": "course-mus-adele",
        "title": "《阿黛尔》(Adele) · 深情灵魂乐与治愈天籁 (10章全集)",
        "category": "music",
        "categoryName": "音乐英语",
        "coverGradient": "from-teal-800 via-emerald-900 to-slate-900",
        "icon": "🎙️",
        "description": "格莱美横扫天后，Rolling in the Deep、Someone Like You、Hello 灵魂嗓音全收录。",
        "difficulty": "中级 B1",
        "tags": ["阿黛尔", "灵魂乐", "天籁之音", "治愈心碎"]
    }, [
        {
            "title": "第 1 首 · Rolling in the Deep · 怒火滔天与复仇烈焰",
            "description": "重型军鼓打击乐与灵魂嘶吼，面对背叛者的绝地反击与尊严觉醒。",
            "sentences": [
                {"en": "There's a fire starting in my heart, reaching a fever pitch and it's bringing me out the dark.", "cn": "有一团烈焰正在我心房深处熊熊燃起，疯狂攀升至狂热沸点，正猛烈拉扯着我彻底挣脱万丈黑暗的泥潭！"},
                {"en": "Finally, I can see you crystal clear; go ahead and sell me out and I'll lay your ship bare.", "cn": "终于，我终于能够一眼将你看得清清楚楚、透透彻彻；你大可尽管在背后出卖老娘，而我必定会把你那艘破船拆得精光底朝天！"},
                {"en": "See how I'll leave with every piece of you; don't underestimate the things that I will do.", "cn": "好好瞪大双眼看着老娘是如何夺走原本属于你的一切体面决然离去的；永远绝不要低估我为了捍卫尊严所能做出的疯狂狠绝报复！"},
                {"en": "The scars of your love remind me of us; they keep me thinking that we almost had it all.", "cn": "你留下的那些纵横交错的爱之伤疤始终在刺痛警醒我：它们让我无数次恍惚以为，我们曾经差点就携手拥有一切！"},
                {"en": "The scars of your love, they leave me breathless; I can't help feeling we could have had it all.", "cn": "你那有毒的爱留下的惨烈伤痕，痛得让我窒息屏息；我忍不住在心底痛惜哀叹：我们原本差一点就能圆满拥有一切！"},
                {"en": "Rolling in the deep; you had my heart inside of your hand, and you played it to the beat.", "cn": "在深不见底的情海深渊中翻江倒海翻滚！你曾将我毫无防备的赤诚真心玩弄于股掌之间，甚至轻浮地伴着轻浮节拍肆意践踏耍弄！"},
                {"en": "Baby, I have no story to be told, but I've heard one on you and I'm gonna make your head burn.", "cn": "宝贝，我或许行事低调没什么风流往事供外人八卦；但我可是亲耳打听到了不少关于你那些肮脏勾当的丑事，老娘定要让你悔不当初焦头烂额！"},
                {"en": "Think of me in the depths of your despair; make a home down there, as mine sure won't be shared.", "cn": "在往后深陷绝望泥潭的凄惨深渊里好好在噩梦中想起我吧；在那暗无天日的冰冷谷底安营扎寨过你的余生吧，老娘的温暖神殿绝不容你染指分毫！"},
                {"en": "Throw your soul through every open door; count your blessings to find what you look for.", "cn": "任由你那漂泊无依的肮脏灵魂在每一个敞开的门扉间穿梭流浪乞讨吧；好好在指缝间数数你所剩无几的福分，看看到底能否寻得你所谓的虚荣！"},
                {"en": "Turn my sorrow into treasured gold; you'll pay me back in kind and reap just what you sow.", "cn": "我必将亲手把曾经受过的锥心剧痛与屈辱泪水，千锤百炼锻造成璀璨夺目的无价黄金；你必将为自己的背叛付出惨痛代价，亲手吞下你亲手播下的恶果！"},
                {"en": "We could have had it all, rolling in the deep, but you threw away the masterpiece.", "cn": "我们本该携手傲立在幸福的巅峰之巅，在深沉浩瀚的爱意中翻涌共鸣，而你却像个有眼无珠的蠢货一样亲手摔碎了这尊旷世绝伦的艺术神作！"},
                {"en": "You had my heart inside of your hand, but you played it with reckless cruelty.", "cn": "你曾将我最毫无防备的滚烫心脏捧在掌心，可你却任性妄为地用最轻蔑残忍的手段将其当成廉价皮球肆意踢踏！"},
                {"en": "Adele's thunderous stomp-and-clap arrangement reinvented twentieth-century British blues.", "cn": "阿黛尔那震耳欲聋、势如破竹的跺脚踏步与击掌节拍编曲，以摧枯拉朽之势彻底颠覆并复兴了二十世纪英伦经典蓝调灵魂乐！"},
                {"en": "Grief transformed into righteous fury is the catalyst for absolute emotional sovereignty.", "cn": "直面背叛的心碎哀伤一旦在尊严的烈火中淬炼升华成大义凛然的正义狂怒，便化作了夺回自我情感绝对主权的终极催化剂！"},
                {"en": "Rolling in the deep; never underestimate a wounded woman who found her roar.", "cn": "在深渊烈焰中涅槃翻腾吧；永远不要低估一个从背叛废墟中彻底觉醒、寻回了女王般惊天咆哮声浪的孤勇女人！"}
            ]
        },
        {
            "title": "第 2 首 · Someone Like You · 像你一样的旧爱与释怀告别",
            "description": "极简大三角钢琴慢板，参加前任婚礼时的克制泪水与无条件祝愿。",
            "sentences": [
                {"en": "I heard that you're settled down, that you found a girl and you're married now.", "cn": "我辗转听说你如今终于彻底收心安顿下来了，听说你寻觅到了心仪的姑娘，如今已然携手步入了婚姻殿堂。"},
                {"en": "I heard that your dreams came true; guess she gave you things I didn't give to you.", "cn": "我听说你过往所有的锦绣夙愿如今皆已如愿以偿成真；想必她一定惠赐给了你那些当年我倾尽全力也未能给你的安稳吧。"},
                {"en": "Old friend, why are you so shy? Ain't like you to hold back or hide from the light.", "cn": "我的老朋友啊，为何此时此刻在宴席重逢时你却显得如此羞涩局促？这可一点都不像昔日那个向来雷厉风行、从不躲避聚光灯的你啊。"},
                {"en": "I hate to turn up out of the blue, uninvited, but I couldn't stay away, I couldn't fight it.", "cn": "我打心底里极其讨厌自己这般冒失突兀地不请自来、不速之客，但我心头的执念却让我无论如何也无法按捺住脚步，我终究没能战胜心魔。"},
                {"en": "I had hoped you'd see my face and that you'd be reminded that for me, it isn't over.", "cn": "我曾卑微地奢望你能在这张熟悉的脸庞上瞥见一丝过往，能借此提醒你：在我们这场未完的故事里，对我而言它其实从未画上句号。"},
                {"en": "Never mind, I'll find someone like you; I wish nothing but the best for you too.", "cn": "没关系的千万别自责，我终会在这茫茫人海中寻觅到一个像你一样体贴的好男儿；我也由衷衷心祝福你们新婚燕尔、一生美满幸福！"},
                {"en": "Don't forget me, I beg, I remember you said: Sometimes it lasts in love, but sometimes it hurts instead.", "cn": "求求你千万不要在漫长岁月里彻底将我遗忘，我依然刻骨铭心牢记你曾说过的那句箴言：有时候爱情能历经风雨厮守一生，但有时候它却唯独留下一地凄凉心碎。"},
                {"en": "Sometimes it lasts in love, but sometimes it hurts instead.", "cn": "有时候炽热的爱意能换来白头偕老的美眷，但有时候它所赐予的，却唯有无尽的苦涩创痛。"},
                {"en": "You know how the time flies; only yesterday was the time of our lives.", "cn": "你心里比谁都清楚这光阴岁月流逝得究竟有多么无情飞快；仿佛就在昨天，我们还在青春最明媚的金色年华里纵情相拥欢歌。"},
                {"en": "We were born and raised in a summer haze, bound by the surprise of our glory days.", "cn": "我们在盛夏温热朦胧的薄雾之中相遇并共同成长蜕变，被那段不可思议的光辉岁月里所有的惊喜与狂欢紧紧捆绑在一起。"},
                {"en": "Nothing compares, no worries or cares; regrets and mistakes, they're memories made.", "cn": "世间再没有任何风景能够与昔日的我们相提并论，曾经毫无顾忌、心无旁骛；所有的悔恨交加与惨痛过失，如今终究皆化作了记忆画卷上不可磨灭的厚重笔墨。"},
                {"en": "Who would have known how bittersweet this would taste?", "cn": "当年在那场大雨倾盆的初遇之际，又有谁能未卜先知预料到今日的离别回味，竟会是这般五味杂陈、苦涩难当？"},
                {"en": "Never mind, I'll find someone like you; let go of the past and let healing wash over the soul.", "cn": "没关系的放下吧，我必将昂首阔步寻觅到属于我的崭新幸福；从容放手过往的所有执念吧，任由心灵疗愈的清泉彻底洗涤抚平心头的创伤。"},
                {"en": "Her voice cracking on the final chorus carries the weight of universal heartbreak.", "cn": "她在最后副歌高潮处那一声情难自禁的轻微哽咽沙哑破音，沉甸甸地承载起了全人类共同直面爱而不得时最真实、最撕心裂肺的心碎重量。"},
                {"en": "I wish nothing but the best for you, my love; walk into your tomorrow with my silent blessing.", "cn": "除了世间最美好的祝愿，我再无他求，我曾深爱过的人啊；带着我润物细无声的永恒沉默祝福，去大步奔赴属于你的崭新明天吧！"}
            ]
        },
        {
            "title": "第 3 首 · Hello · 跨越千山万水的电话问候",
            "description": "孤独钢琴前奏，跨越数载光阴向昔日伤害过的人真诚致歉与内心和解。",
            "sentences": [
                {"en": "Hello, it's me; I was wondering if after all these years you'd like to meet to go over everything.", "cn": "喂你好啊，正是我；我一直在心头暗自琢磨惶惑：在历经了这整整漫长的数年岁月沧海桑田之后，你是否还愿意同我重逢相见，把当年的一切都摊开说清？"},
                {"en": "They say that time's supposed to heal ya, but I ain't done much healing.", "cn": "这世上所有人都异口同声劝导说时间是抚平治愈一切创伤的良药，可我心头的伤口，却似乎从未真正结痂愈合过分毫。"},
                {"en": "Hello, can you hear me? I'm in California dreaming about who we used to be when we were younger and free.", "cn": "喂你好，你能听清我的声音吗？我此刻正身处加利福尼亚的温暖阳光下，神游般怀念追忆着当年年少轻狂、自由自在、无忧无虑的我们。"},
                {"en": "I've forgotten how it felt before the world fell at our feet.", "cn": "我仿佛早已彻底忘却了在那场不可思议的喧嚣名利席卷倾倒在我们的脚下之前，平静的生活究竟是何等踏实纯粹的滋味。"},
                {"en": "There's such a difference between us and a million miles.", "cn": "横亘在如今我们彼此心智与生活轨迹之间的鸿沟是如此天差地别，仿佛相隔着整整上百万英里的遥远光年。"},
                {"en": "Hello from the other side! I must've called a thousand times to tell you I'm sorry for everything that I've done.", "cn": "隔着这漫长岁月与彼岸长河向你致以一声遥远的问候！我曾千百次在深夜颤抖着按下拨号键，只为当面向你由衷道一声：对不起，为了我当年犯下的一切过失！"},
                {"en": "But when I call, you never seem to be home.", "cn": "然而每当我鼓足毕生勇气拨通那串号码时，电话那头传来的却永远只是无人应答的冰冷忙音，你似乎早已不在那处避风港了。"},
                {"en": "Hello from the outside! At least I can say that I've tried to tell you I'm sorry for breaking your heart.", "cn": "从这被世俗名利高墙彻底隔绝的外界向你致以一声真诚问候！至少在今天我能昂首坦荡告诉自己：我曾拼尽全力向你亲口致歉，为了当年残忍摔碎你的滚烫真心！"},
                {"en": "But it don't matter, it clearly doesn't tear you apart anymore.", "cn": "但这一切挽留如今或许早已微不足道无关紧要了，显而易见，过往的那些陈年旧伤，再也绝不可能让你感到半分撕心裂肺的痛楚了。"},
                {"en": "Hello, how are you? It's so typical of me to talk about myself, I'm sorry, I hope that you're well.", "cn": "喂你好，你最近过得还好吗？我这人向来就是这副自私自利的坏毛病，一开口就只顾着唠叨自己的琐事，真的很抱歉，我发自肺腑企盼你一切安好。"},
                {"en": "Did you ever make it out of that town where nothing ever happened?", "cn": "你后来是否当真如愿以偿彻底逃离搬出了那座日复一日死气沉沉、从未发生过任何新鲜事物的偏僻破败小镇？"},
                {"en": "It's no secret that the both of us are running out of time.", "cn": "这从来不是什么不可告人的隐秘秘密：我们彼此青春年华里的充裕时间，早已在冷战与沉默中无情消耗殆尽了。"},
                {"en": "The sweeping, cinematic chorus explodes with majestic orchestral power.", "cn": "副歌那段排山倒海、荡气回肠的宏伟管弦乐交响合奏，以摧枯拉朽的电影史诗级质感轰然爆发倾泻而出！"},
                {"en": "Reaching out across the divide of years is an act of profound spiritual vulnerability.", "cn": "敢于在时过境迁数年之后主动跨越漫漫心结鸿沟伸手求和，乃是一种直面灵魂最脆弱处的大勇之举。"},
                {"en": "Hello from the other side; may we find peace in the quiet spaces between our words.", "cn": "隔着这彼岸长河道一声珍重问候；愿我们在这千言万语未曾吐露的字里行间死寂空白深处，终能觅得各自内心的永恒安宁。"}
            ]
        },
        {
            "title": "第 4 首 · Set Fire to the Rain · 暴风雨中点燃烈火的决绝",
            "description": "弦乐狂澜与磅礴高音，面对谎言在倾盆大雨中将过往彻底焚为灰烬。",
            "sentences": [
                {"en": "I let it fall, my heart, and as it fell you rose to claim it.", "cn": "我曾任由我那颗毫无防备的滚烫心脏自高空直直坠落，而正当它急速下坠之际，你却适时从天而降强势宣告了对它的占有主权。"},
                {"en": "It was dark and I was over, until you kissed my lips and you saved me.", "cn": "当时我的周遭一片至暗死寂、我整个人生几乎快要万念俱灰彻底玩完，直到你温存俯身亲吻了我的双唇，奇迹般将我从绝望深渊中一把抢救拉回！"},
                {"en": "My hands, they were strong, but my knees were far too weak to stand in your arms without falling to your feet.", "cn": "我的双手骨骼原本是何等刚劲有力，但每当落入你温暖的怀抱之中时，我的双膝却总是彻底发软无力，甚至忍不住想要当场跪倒在你的脚边臣服。"},
                {"en": "But there's a side to you that I never knew, never knew.", "cn": "然而在你那副温情脉脉的皮囊之下，却隐藏着一面我在此之前从始至终从未真正看清、从未真正领教过的恐怖阴暗面！"},
                {"en": "All the things you'd say, they were never true, never true, and the games you'd play, you would always win.", "cn": "那些昔日从你嘴里吐露出的甜言蜜语山盟海誓，从头到尾竟全都是彻头彻尾的弥天大谎；而在你精心设计的那些两性情感博弈游戏里，你总是自鸣得意笑到最后！"},
                {"en": "But I set fire to the rain, watched it pour as I touched your face.", "cn": "但我偏要迎着漫天倾盆暴雨悍然点燃熊熊烈火！我一边任凭暴雨如注狂暴倾泻冲刷着我触摸你脸庞的指尖，一边冷眼看着烈火在雨中狂暴蔓延！"},
                {"en": "Well, it burned while I cried, cause I heard it screaming out your name, your name!", "cn": "那烈焰在冰冷的雨水中疯狂燃烧，而我在暴雨中痛哭流涕，只因我分明听见那呼啸的狂风烈火，正在声嘶力竭疯狂咆哮着你的大名！"},
                {"en": "When I'm with you I could stay there, close my eyes, feel you're here forever.", "cn": "每当我依偎在你身侧的时光里，我多么渴望时光能够就此彻底凝固停滞；闭上双眼，坚信你必定会永生永世驻守在我身旁。"},
                {"en": "You and me together, nothing gets better.", "cn": "只要你我二人心手相连并肩依偎，这辽阔天地间便再也没有任何光景能比这更加美妙无瑕。"},
                {"en": "Cause I knew that was the last time, the last time!", "cn": "只因我灵魂深处比谁都清醒明白：那缠绵的一夜，已然注定是我们今生今世最后的告别诀别！"},
                {"en": "Sometimes I wake up by the door, that heart you caught must be waiting for you.", "cn": "有时候我总在夜半惊魂梦回中恍惚在房门口幽幽醒来，那颗当年被你轻巧凌空接住的心脏，此刻仿佛依旧在痴痴苦等你的归来。"},
                {"en": "Even now when already we are through, I can't help myself from looking for you.", "cn": "哪怕事到如今我们二人早已恩断义绝彻底形同陌路，我却依然无可救药地会在茫茫人海中下意识搜寻寻觅你的身影。"},
                {"en": "The paradoxical imagery of burning rain embodies the impossibility of reconciling passion with deceit.", "cn": "在倾盆暴雨中点燃烈火这一充满自相矛盾的绝妙修辞意象，深刻入骨地具象化了炽热真爱与虚伪背叛之间绝不可调和的撕裂痛苦。"},
                {"en": "Let the illusion turn to ashes beneath the downpour; release the ghost and step into the clearing.", "cn": "就任凭这虚妄的幻象在倾盆暴雨的洗礼冲刷下彻底化为冰冷的焦黑灰烬吧；超度释怀心中的执念幽灵，昂首阔步踏入阳光明媚的开阔旷野！"},
                {"en": "I set fire to the rain; let the flames cleanse the sacred temple of my sovereign self.", "cn": "我在暴风雨中决绝点燃烈火！任凭这至纯至阳的炽热烈焰，彻底洗涤净化属于我神圣独立主权的纯洁心灵神殿！"}
            ]
        },
        {
            "title": "第 5 首 · Skyfall · 绝地天幕与向死而生",
            "description": "007系列同名奥斯卡金奖主题曲，沉稳低音管乐与大将风范的向死而生。",
            "sentences": [
                {"en": "This is the end; hold your breath and count to ten.", "cn": "这便是万物的终局了；屏住呼吸吧，在心底冷静从容地倒数倒计时十秒。"},
                {"en": "Feel the earth move and then hear my heart burst again.", "cn": "去真切感受脚下坚实的大地正发生剧烈的地动山摇，紧接着，去静静倾听我胸膛深处那颗孤勇心脏再次破壁爆裂的轰鸣。"},
                {"en": "For this is the end; I've drowned and dreamt this moment, so overdue I owe them.", "cn": "只因这宿命的终局早已如期而至；我曾无数次深陷溺水梦魇中反复推演过这一绝命时刻，这场生死清算早已迟到了太久，我欠这一战一个交代。"},
                {"en": "Swept away, I'm stolen, a thousand fathoms deep beneath the waves.", "cn": "被无情席卷吞噬，被彻底剥夺了一切生机，沉沦坠落于波涛之下千万英寻深不见底的万丈深渊深处。"},
                {"en": "Let the sky fall, when it crumbles, we will stand tall, face it all together at Skyfall.", "cn": "哪怕这天幕轰然坍塌崩裂，哪怕这苍穹彻底化为齑粉残垣，我们亦将挺直脊梁巍然并肩屹立，在天幕庄园的焦土之巅直面一切狂风暴雨！"},
                {"en": "Skyfall is where we start, a thousand miles and poles apart.", "cn": "“天幕庄园”正是我们命运最初启航扬帆的神圣源头起点，哪怕横跨千万光阴哩数与两极天堑也休想将其割裂阻断。"},
                {"en": "Where worlds collide and days are dark; you may have my number, you can take my name, but you'll never have my heart.", "cn": "在文明与野蛮激烈碰撞、黑夜遮蔽天日的至暗时刻；你或许能夺走我的军情代号，你或许能剥夺抹去我的俗世姓名，但你休想征服老子钢铁般的心脏！"},
                {"en": "Let the sky fall, when it crumbles, we will stand tall.", "cn": "任凭天崩地裂吧，任凭世界粉碎崩塌吧，我们必将昂首挺立如参天青松！"},
                {"en": "Where you go, I go, what you see, I see; I know I'd never be me without the security of your loving arms.", "cn": "无论你踏足何方我必誓死相随，凡你双眸所及之处我必同仇敌忾；我深知倘若剥离了你温暖双臂筑起的坚固堡垒，我便再也无法成为今日这个完整不屈的我。"},
                {"en": "Put your hand in my hand and we'll stand tall.", "cn": "将你的手掌紧紧交扣在我的掌心之中吧，我们必将并肩傲然挺立在天地之间！"},
                {"en": "The vintage James Bond brass fanfares and minor ninth chords evoke espionage nobility.", "cn": "纯正复古的詹姆斯·邦德经典管乐号角齐鸣编曲，配上深邃神秘的减小九度幽暗和弦，瞬间营造出了一种顶格特工的高贵悲壮肃杀气场。"},
                {"en": "Heritage is not a static relic of stone; it is the battlefield where we make our final stand.", "cn": "先祖留给我们的神圣遗泽，绝不是陈列在博物馆玻璃罩里冷冰冰的僵化石雕；它是我们在穷途末路之际誓死捍卫信仰的终极决战堡垒！"},
                {"en": "Stand tall amidst the falling embers; loyalty outlives physical structures and government treaties.", "cn": "在漫天飘零落下的滚烫余烬中傲然挺直脊梁吧；纯粹的忠诚与骨气，将远远超越冰冷的钢筋水泥建筑与官僚政府的条约纸屑万世长存！"},
                {"en": "Let the sky fall, let the foundations shake; true courage is forged when all earthly safety dissolves.", "cn": "任由苍穹塌陷吧，任凭大地基石剧烈震颤吧；唯有当世俗所有的安稳退路统统瓦解成灰之时，真正的向死而生大勇方能破茧而出！"},
                {"en": "Face it all together at Skyfall; our legacy is written in the fire of defiance.", "cn": "在天幕之巅并肩直面一切惊涛骇浪吧；我们名垂青史的神圣传奇，早已用不屈抗争的炽热烈火永远铭刻在历史天地之间！"}
            ]
        }
    ]))

    return courses
