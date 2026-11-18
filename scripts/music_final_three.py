# -*- coding: utf-8 -*-
from builder_core import build_course

def get_music_final_three():
    courses = []

    # 6. 《酷玩乐队》(Coldplay) · 10 章全集
    courses.append(build_course({
        "id": "course-mus-coldplay",
        "title": "《酷玩乐队》(Coldplay) · 英伦哲思摇滚与体育场天籁赞歌 (10章全集)",
        "category": "music",
        "categoryName": "音乐英语",
        "coverGradient": "from-indigo-600 via-purple-700 to-pink-600",
        "icon": "🌟",
        "description": "二十一世纪全球最畅销乐队，Yellow、Viva La Vida、Fix You 宏伟生命哲思与震撼全场大合唱。",
        "difficulty": "中级 B1",
        "tags": ["酷玩乐队", "英伦摇滚", "治愈哲思", "现场封神"]
    }, [
        {
            "title": "第 1 首 · Yellow · 漫天星斗皆为你绚烂闪耀",
            "description": "成名封神抒情摇滚，克里斯·马汀在多塞特海滩阴雨漫步的纯情告白。",
            "sentences": [
                {"en": "Look at the stars, look how they shine for you, and everything you do.", "cn": "快抬头凝望夜空中漫天浩瀚的璀璨繁星吧，瞧瞧它们是如何专为你一人、以及你所做的每一件善举而熠熠生辉闪烁的！"},
                {"en": "Yeah, they were all yellow, glowing with pure devotion.", "cn": "是啊，那满天的繁星皆染上了金灿灿的温暖金黄，在苍穹深处散发着至纯至善的赤诚神圣光晕。"},
                {"en": "I came along, I wrote a song for you, and all the things you do, and it was called Yellow.", "cn": "我跨越千山万水跋涉而来，怀揣着无尽深情专为你和你的点点滴滴谱写下了一曲传世长歌，而它的名字，便叫做《黄色》。"},
                {"en": "So then I took my turn, oh what a thing to have done, and it was all yellow.", "cn": "轮到我登台向全世界坦白心迹，噢天呐当年我竟奇迹般完成了这出不可思议的壮举，而满心满眼所见之处，皆尽是那抹温暖治愈的金黄！"},
                {"en": "Your skin, oh yeah, your skin and bones, turn into something beautiful.", "cn": "你的每一寸肌肤骨骼、你的整个血肉之躯，都在大爱的光芒洗礼下，奇迹般蜕变升华成了这人世间最不可思议的美妙造化！"},
                {"en": "And you know, you know I love you so; you know I love you so.", "cn": "而你心里是清楚的，你比谁都明白我对你的爱意究竟有多么刻骨铭心；你深知我爱你胜过爱这世间万物！"},
                {"en": "I swam across, I jumped across for you, oh what a thing to do.", "cn": "我曾为你奋不顾身横渡波涛汹涌的滔天恶浪，我曾为你毫不犹豫跃过万丈深渊天堑，噢为了你，哪怕上刀山下火海我又有何畏惧！"},
                {"en": "Cause you were all yellow; look at how you illuminate my dark horizon.", "cn": "只因你的存在便是一轮照亮一切的破晓暖阳；快瞧瞧你是如何以一己之力，彻底照亮驱散了我整个人生原本暗无天日的阴霾地平线！"},
                {"en": "I drew a line, I drew a line for you, oh what a thing to do, and it was all yellow.", "cn": "我在沙滩上为你画下一道坚不可摧的守护防线，噢这是何等神圣崇高的决然抉择，而天地四野，尽数沉醉在那片绚烂的金黄之中。"},
                {"en": "Your skin, oh yeah, your skin and bones, turn into something beautiful.", "cn": "你的每一寸温存肌肤，你的每一根坚韧骨骼，皆已化作了天地造化神明笔下最圣洁纯粹的绝美艺术结晶。"},
                {"en": "And you know, for you I'd bleed myself dry; for you I'd bleed myself dry.", "cn": "而你心里深知：只要是为了护你一生平安喜乐，我心甘情愿为你流尽胸膛深处的最后一滴滚烫热血！"},
                {"en": "It's true, look how they shine for you; look how they shine for you.", "cn": "这一切皆是千真万确的铁石誓言，快抬头看看满天的繁星吧，瞧瞧它们是何等痴迷、何等炽热地在为你长久璀璨闪耀！"},
                {"en": "The soaked rainwear on Studland Bay video established their anti-rockstar authenticity.", "cn": "在英格兰斯塔德兰湾冷冽雨中身披湿漉漉黄色雨衣一镜到底漫步浅唱的传世MV，瞬间奠定了他们反叛浮夸商业包装、回归质朴本真的殿堂级音乐风骨！"},
                {"en": "Devotion without self-interest elevates ordinary human affection into a spiritual sanctuary.", "cn": "毫无保留、不掺杂任何自私算计的赤诚奉献，足以将凡尘俗世中最寻常的男女情爱，彻底升华蜕变成为一座庇护灵魂的精神圣殿！"},
                {"en": "Look at the stars, look how they shine for you; in the darkest night, you are my eternal beacon.", "cn": "仰望星空吧，瞧那漫天群星皆因你而灿烂；纵使漫步在至暗无光的深夜，你亦是我心头永不熄灭的破晓灯塔！"}
            ]
        },
        {
            "title": "第 2 首 · Viva La Vida · 生命万岁与失落的王冠",
            "description": "路易十六走上断头台的历史回眸，弦乐四重奏奔涌下的权力哲思。",
            "sentences": [
                {"en": "I used to rule the world; seas would rise when I gave the word.", "cn": "我曾经是执掌天下生杀大权的至高无上统治君王；当年我只需在王座之巅轻轻吐露一字号令，漫天狂暴的沧海怒涛亦会应声为我翻涌咆哮！"},
                {"en": "Now in the morning I sleep alone, sweep the streets I used to own.", "cn": "而如今在破晓寒冬的凄清晨曦里，我只能蜷缩在阴暗地牢角落里独自一人沉睡，白天沦落到只能拿起扫帚去清扫那些昔日完全臣服在我脚下的王都街巷。"},
                {"en": "I used to roll the dice, feel the fear in my enemy's eyes.", "cn": "在呼风唤雨的峥嵘岁月里，我曾肆意投掷着决定万千苍生命运的征战骰子，冷眼端详着对立阵营的仇敌眼中流露出的绝望恐惧颤抖。"},
                {"en": "Listen as the crowd would sing: Now the old king is dead, long live the king!", "cn": "耳畔曾久久回荡倾听着成千上万广场臣民排山倒海的狂热朝拜欢呼：旧王已死，新皇万岁！新皇万岁！"},
                {"en": "One minute I held the key, next the walls were closed on me.", "cn": "前一分钟我还手握着开启整座帝国至高权柄之门的金色钥匙，而后一秒钟，冰冷残酷的囚室石壁便轰然合拢将我死死封印！"},
                {"en": "And I discovered that my castles stand upon pillars of salt and pillars of sand.", "cn": "而在这大起大落的万劫深渊之中我终于大彻大悟痛彻惊觉：我昔日苦心经营、自以为坚不可摧的宏伟宫殿城堡，原来从始至终不过只是脆弱地奠基矗立在松散的盐柱与流沙之上！"},
                {"en": "I hear Jerusalem bells a-ringing, Roman cavalry choirs are singing.", "cn": "我分明听见耶路撒冷那古老神圣的铜钟正在为我悠扬长鸣敲响丧钟，古罗马重甲铁骑军团的宏伟唱诗班正在苍穹深处放声哀唱。"},
                {"en": "Be my mirror, my sword and shield, my missionaries in a foreign field.", "cn": "做我的明澈鉴戒之镜吧，做我浴血搏杀的利剑与坚不可摧的护盾吧，做我远赴异邦开疆拓土、布道天下的忠诚使徒吧！"},
                {"en": "For some reason I can't explain, once you'd gone there was never, never an honest word.", "cn": "不知究竟出于何种言语难以言说的诡谲因缘，自打当年你拂袖决然离去的那一刻起，我身畔的朝堂重臣口中便再也、再也未曾吐露过哪怕半句肺腑真言！"},
                {"en": "And that was when I ruled the world.", "cn": "而那些众叛亲离、被奸佞谎言死死包围蒙蔽的荒诞悲凉岁月，却偏偏正是我君临天下、统治世界的巅峰时刻！"},
                {"en": "It was a wicked and wild wind blew down the doors to let me in.", "cn": "是一阵邪恶狂暴、摧枯拉朽的历史革命飓风猛然吹塌轰碎了那扇紧闭的宫廷沉重铁门，将落魄的我连同宿命一并席卷卷入了时代风暴的漩涡正中央。"},
                {"en": "Shattered windows and the sound of drums, people couldn't believe what I'd become.", "cn": "满地破碎四溅的彩绘玻璃与震耳欲聋的激昂战鼓声响彻云霄，昔日匍匐跪拜的平民百姓难以置信地瞪大双眼，无法相信眼前这个沦为阶下囚的落魄汉竟会是我当年的模样！"},
                {"en": "Revolutionaries wait for my head on a silver plate; just a puppet on a lonely string.", "cn": "热血沸腾的革命断头台行刑者们正在翘首以盼，等着将老子的项上人头盛放在冰冷的纯银托盘中向广场示众；回首我这一生，不过只是个被命运无形丝线随意摆弄戏弄的孤独提线木偶罢了！"},
                {"en": "Oh, who would ever want to be king? Power is an intoxicating poison that suffocates the soul.", "cn": "噢天呐！这大千尘世间究竟还有哪一个愚蠢狂妄之徒，会当真不知死活地渴望去登上那把饮鸩止渴的孤独王座？！世俗的至高权力不过是一杯令人神魂颠倒、却最终足以将你灵魂生生扼杀窒息的绝命鸩酒！"},
                {"en": "I hear Jerusalem bells a-ringing; let the vanity of empires crumble, Viva la Vida!", "cn": "我耳畔清晰听见圣城耶路撒冷的古钟在为我长鸣祈祷；任由这凡尘间一切过眼云烟的虚妄帝国基业轰然崩塌瓦解吧，生命万岁！纵情高歌生命本身的壮丽万岁！"}
            ]
        },
        {
            "title": "第 3 首 · Fix You · 让我来治愈你破碎的心房",
            "description": "风琴慢板与吉他雷霆爆发，写给痛失至亲的妻子，在至暗时刻化作指路明灯。",
            "sentences": [
                {"en": "When you try your best, but you don't succeed; when you get what you want, but not what you need.", "cn": "每当你早已拼尽了浑身最后一丝力气去抗争，却终究未能如愿以偿赢得胜利；每当你费尽周折终于夺得了你朝思暮想的事物，却蓦然惊觉那根本不是你灵魂深处真正渴求的归宿。"},
                {"en": "When you feel so tired, but you can't sleep; stuck in reverse.", "cn": "每当你的身心早已疲惫不堪到了崩溃边缘，可深夜合上双眸却无论如何也无法安详入眠；整个人生轨迹仿佛被死死卡死在了挂着倒挡的绝望逆境漩涡深处。"},
                {"en": "And the tears come streaming down your face, when you lose something you can't replace.", "cn": "滚烫的泪水止不住地如决堤洪流般划过你绝望无助的面庞，只因你刚刚在这冷酷人世间，永远痛失了那件你穷尽余生所有财富也绝无法替代的挚爱骨肉。"},
                {"en": "When you love someone, but it goes to waste; could it be worse?", "cn": "每当你毫无保留将毕生炽热大爱倾囊托付于人，最终换来的却唯有被肆意践踏挥霍的凄凉结局；试问这大千尘世间，还能有比这更令人万念俱灰的绝境吗？"},
                {"en": "Lights will guide you home, and ignite your bones, and I will try to fix you.", "cn": "漫天的温存明灯必将穿透幽暗迷雾一路引领你平安归家，去重新点燃淬炼你早已冰封冻结的血肉筋骨，而我，必将竭尽我生命的全部力量去亲手治愈抚平你破碎的心房！"},
                {"en": "And high up above or down below, when you're too in love to let it go.", "cn": "无论你此刻身处九天之巅的狂喜云端、亦或是跌落进万丈深渊的炼狱谷底；每当你爱得太深太炽热以至于无论如何也舍不得体面放手时。"},
                {"en": "But if you never try you'll never know just what you're worth.", "cn": "但是倘若你因畏惧受伤而从始至终连一次迈开脚步去闯荡的勇气都没有，你便这辈子都永远无法真正参透你自己究竟蕴藏着何等无价的高贵价值！"},
                {"en": "Lights will guide you home, and ignite your bones, and I will try to fix you.", "cn": "指路的明灯必将照亮你归家的漫漫坦途，去重新温暖复活你冰冷的胸膛，而我，定当全力以赴去缝合你所有的创伤！"},
                {"en": "Tears stream down your face, I promise you I will learn from my mistakes.", "cn": "泪水止不住地从你憔悴的脸颊滚落，我向苍天起誓向你郑重承诺：我必定会从我过往犯下的所有盲目过失中痛定思痛、吸取教训。"},
                {"en": "Tears stream down your face, and I, I will never abandon your side in the dark.", "cn": "泪水滑落过你的脸庞，而我……而我无论经历世事如何变迁，也绝不会在最漆黑绝望的至暗风暴时刻抛弃背离你的身侧！"},
                {"en": "Jonny Buckland's soaring distorted guitar solo breaks through the grief like dawn breaking over mountains.", "cn": "吉他手强尼·巴克兰德手中那把电吉他在高潮处骤然拔地而起的惊天高亢过载独奏，宛如破晓黎明那一缕刺破重重阴霾的万丈金光，以雷霆之势撕裂了一切悲伤绝望！"},
                {"en": "Composed using a vintage harmonium given to Bruce Paltrow, the song is a living monument to filial grief.", "cn": "这首传世神曲正是借助岳父生前遗留下的那台古董簧风琴的浑厚音色所亲手谱就，它是一座为抚平丧亲剧痛而庄严矗立在天地间的巍峨永恒精神纪念碑！"},
                {"en": "Healing does not mean erasing the scar; it means surrounding the wound with unshakeable devotion.", "cn": "心灵真正的痊愈疗愈从来不意味着自欺欺人地抹去那道伤疤；它的真谛在于：用坚如磐石、永不褪色的赤诚深情，将那道伤痕严严实实温柔包裹呵护！"},
                {"en": "Lights will guide you home, and ignite your bones, and I will try to fix you.", "cn": "真爱的圣光必将化作明灯指引你回归温馨的避风港湾，去彻底点燃融化你体内冰封的热血，而我，将用我一生的深情去抚慰治愈你的灵魂！"},
                {"en": "Walk forward into the clearing; no darkness is absolute when love stands as your sentinel.", "cn": "昂首阔步迈向那片阳光普照的开阔原野吧；当这世间有真爱如钢铁卫士般誓死为你镇守后方时，便再也没有任何一场长夜会是绝对无法战胜的！"}
            ]
        },
        {
            "title": "第 4 首 · The Scientist · 回到最初的起点与逆流而上",
            "description": "经典黑白倒放MV神作，纯钢琴扫弦，没有人说过相爱会如此艰难。",
            "sentences": [
                {"en": "Come up to meet you, tell you I'm sorry; you don't know how lovely you are.", "cn": "我跨越千山万水只为赶来同你相见，亲口向你由衷道一声对不起；你心里根本无法想象，当年的你在我眼中究竟是何等娇艳动人、无可替代。"},
                {"en": "I had to find you, tell you I need you, tell you I set you apart.", "cn": "我必须在茫茫人海中重新寻觅到你的踪迹，亲口向你倾诉我内心深处对你是多么依赖渴望，向你郑重表白：在我一生相逢过的芸芸众生之中，你始终是我唯一的独家偏爱。"},
                {"en": "Tell me your secrets and ask me your questions, oh, let's go back to the start.", "cn": "向我坦白倾诉你所有的隐秘心事吧，尽管向我抛出你心底所有的困惑疑问吧，噢求你，让我们放下防备，重新携手重返命运最初相遇的起点吧！"},
                {"en": "Running in circles, coming up tails, heads on a science apart.", "cn": "我们总是在原地无休止地盲目打转兜圈子，抛出的命运硬币每次落下的结果总是那般残酷不顺，即便用尽世间所有精密严谨的科学定律，也无法参透我们之间情感分崩离析的终极密码。"},
                {"en": "Nobody said it was easy; it's such a shame for us to part.", "cn": "从一开始就从来没有任何人断言过相濡以沫会是一件轻松平顺的易事；我们两个明明深爱着彼此的人最终落得如此分道扬镳的残局，当真是这人世间最大的莫大遗憾！"},
                {"en": "Nobody said it was easy, no one ever said it would be this hard.", "cn": "从来没有人说过相爱很容易，但也从来没有任何长辈曾警告过我们：两颗炽热的心想要修成正果厮守一生，竟会艰难煎熬到如此令人痛彻心扉的极境！"},
                {"en": "Oh, take me back to the start.", "cn": "噢老天爷啊，求你发发慈悲，带我重新回到那个我们初次邂逅、未受伤害的最初清晨吧！"},
                {"en": "I was just guessing at numbers and figures, pulling your puzzles apart.", "cn": "我昔日总是愚蠢地像个自命不凡的书呆子一样，成天试图用冰冷机械的数字公式与逻辑推演去揣摩你的心思，自以为是地妄图去强行拆解你心灵深处那座精妙复杂的谜题迷宫。"},
                {"en": "Questions of science, science and progress, do not speak as loud as my heart.", "cn": "所谓理性科学的深奥命题、所谓时代进步与工业文明的宏大叙事，在这一刻所发出的声响，却无论如何也比不过我胸膛深处这颗为你疯狂跳动的心脏所爆发出的深情呐喊！"},
                {"en": "Tell me you love me, come back and haunt me, oh and I rush to the start.", "cn": "快亲口告诉我你依然深深爱着我吧，即便化作午夜缠绕我梦境的深情幽灵我也甘之如饴，噢我此刻愿不顾一切拔足狂奔，飞奔重返我们最初相爱的起点！"},
                {"en": "The innovative reverse-chronology music video required Chris Martin to learn the entire song backwards.", "cn": "那支开创时代先河的整部全片倒放时空逆流的经典MV，竟然逼着主唱克里斯·马汀足足闭关数周，硬生生把整首英文歌词从最后一个发音字母倒背如流倒着唱了出来！"},
                {"en": "Intellectual overthinking is the greatest destroyer of instinctive emotional communion.", "cn": "在大脑中过度用冰冷理智进行得失利弊的权衡算计与逻辑推演，往往是摧毁两个人之间浑然天成、纯粹直觉式灵魂相通共鸣的最大罪魁祸首！"},
                {"en": "I had to find you; love is not a scientific equation to be solved, but a mystery to be inhabited.", "cn": "我必须找到你！爱情从来不是一道冷冰冰摆在黑板上等待被严密求解的物理微积分算式，而是一座唯有用全副身心去虔诚栖息体验的崇高造化奥秘！"},
                {"en": "Nobody said it was easy, but true devotion considers the grueling ascent worth every drop of blood.", "cn": "世间从来没人宣称过厮守会轻松平坦，但一颗九死不悔的赤诚之心却坚信：为了攀登至与你并肩看日出的终极幸福之巅，沿途洒下的每一滴滚烫热血与汗水皆物超所值！"},
                {"en": "Take me back to the start; wipe the slate clean and let love begin again in innocence.", "cn": "带我重返那个未被世俗污染的起点吧；把过往所有的猜忌与隔阂彻底一笔勾销擦拭干净，让我们在最初的纯真与赤诚之中，重新坠入爱河！"}
            ]
        },
        {
            "title": "第 5 首 · Clocks · 时钟滴答与时光流逝的困顿",
            "description": "降E大调标志性琶音琴音，格莱美年度制作，人在时光长河中的挣扎与救赎。",
            "sentences": [
                {"en": "Lights go out and I can't be saved; tides that I tried to swim against have brought me down upon my knees.", "cn": "四周的璀璨明灯接连熄灭，而我似乎早已无药可救在劫难逃；那些我曾不自量力试图逆流抗争的汹涌狂暴潮汐，终究还是将我彻底击溃打倒、重重逼跪在泥泞之中。"},
                {"en": "So I beg, I take, I borrowed and I broke.", "cn": "于是我在这绝境中苦苦乞求，我疯狂掠夺索取，我向岁月拼命借贷透支，最终却亲手将周遭原本珍视的一切摔得粉碎。"},
                {"en": "Closing walls and ticking clocks, gonna come back and take you home.", "cn": "步步紧逼、不断向内坍塌压迫的四面高墙，以及墙上那一记记如死神脚步般冰冷滴答作响的时钟节拍；我必定会战胜心魔破茧归来，亲手将你带回属于我们的温暖家园。"},
                {"en": "I could not stop that you now know, singing: Come out upon my seas, cursed missed opportunities.", "cn": "我当年终究未能阻挡宿命的悲剧演进，而你如今也已然知晓了一切真相，在心底凄然高唱：踏上我这片风雨飘摇的沧海吧，那些被时代诅咒、抱憾痛失的宝贵机缘啊！"},
                {"en": "Am I part of the cure, or am I part of the disease?", "cn": "直面这场席卷一切的心灵灾难浩劫，我究竟算得上是拯救救赎众生的良药解药之一，还是我本人从一开始，便恰恰正是这场病入膏肓的绝症毒瘤祸根？！(哲学终极拷问)"},
                {"en": "Singing: You are, you are, you are the anchor that keeps my drifting vessel from capsizing.", "cn": "在狂风骤雨中放声歌唱：唯独只有你，唯独只有你，才是我生命中唯一一座能让我这艘在惊涛骇浪中随波逐流的危舟免遭彻底倾覆灭顶的神圣沉稳锚链！"},
                {"en": "Confusion that never stops, closing walls and ticking clocks.", "cn": "灵魂深处经久不息、永无休止上演的剧烈迷茫困顿，周围步步紧逼令人窒息的高墙，以及那无情流逝滴答作响的岁月时钟。"},
                {"en": "Gonna come back and take you home; I could not stop that you now know.", "cn": "我必定会杀出重围披荆斩棘归来带你回家；那些往日犯下的惨痛过失如今已水落石出大白于天下。"},
                {"en": "Singing: Come out upon my seas, cursed missed opportunities, am I a part of the cure or the disease?", "cn": "高歌呼唤：来渡我这片惊涛骇浪之海吧，缅怀那些痛失的年华机缘，拷问自己在这场历史大局中究竟是解药还是毒药？"},
                {"en": "And nothing else compares; oh, nothing else compares to the sacred illumination of your truth.", "cn": "放眼这大千凡尘天地之间，再没有任何世俗事物能够与你相提并论；噢，这世间万物皆休想同你身上散发出的真理圣光相媲美！"},
                {"en": "The iconic circular, syncopated piano arpeggio became one of the most recognizable riffs in twentieth-first-century music.", "cn": "那段充满无限循环魔性美感、采用精妙切分音编排的降E大调经典钢琴分解琶音旋律，毫无争议地当选成为了整个二十一世纪流行音乐史上辨识度最高的超级图腾神作！"},
                {"en": "Time is an unrelenting river that washes away empires, egos, and calculated strategies.", "cn": "无情奔涌的时间长河是一头不舍昼夜的冷酷巨兽，它能以摧枯拉朽之势冲刷抹平人世间所有显赫一时的不可一世帝国、狂妄膨胀的个人虚荣以及机关算尽的战术机谋。"},
                {"en": "In the face of existential uncertainty, love is the solitary compass that maintains true north.", "cn": "直面对抗人世间不可捉摸的存在主义荒诞与巨大迷茫困顿之时，唯有纯粹的大爱，才是唯一能在这迷雾苍穹下为你长久坚守真正磁北极方位的神圣罗盘！"},
                {"en": "You are the anchor amidst the ticking clocks; hold fast until the storm expends its fury.", "cn": "在那无情滴答作响的时钟催促声浪之中，你便是我永恒的精神抛锚之所；咬紧牙关坚定守候吧，直到这场天地的狂暴狂怒彻底耗尽它最后的力气！"},
                {"en": "Am I part of the cure? Yes, by choosing to love unconditionally, you become the healing of the world.", "cn": "我究竟是否算得上这世间的救赎良药？答案是无比斩钉截铁的：只要你毅然决然选择去毫无保留、不求回报地深爱大千苍生，你本人，便已化作了普照救赎这个残破世界的崇高良药！"}
            ]
        },
        {
            "title": "第 6 首 · Paradise · 暴风雨过后的伊甸乐园",
            "description": "交响弦乐与高亢合唱，小女孩在梦境中战翅翱翔逃离残酷现实。",
            "sentences": [
                {"en": "When she was just a girl she expected the world, but it flew away from her reach.", "cn": "当她当年还不过只是个不谙世事的天真稚气小女孩时，她曾满心欢喜憧憬期盼着整座世界都会对她报以温柔善意，然而那座繁华绚烂的理想世界，却早已在现实的风雨中呼啸飞离了她所能企及的指尖。"},
                {"en": "So she ran away in her sleep and dreamed of paradise, every time she closed her eyes.", "cn": "于是现实受挫碰壁的她，只能每夜在甜美的梦乡中悄然出逃，在她每一次沉沉闭上双眸的香甜时刻，在心头苦苦构筑梦见属于她的伊甸乐园。"},
                {"en": "When she was just a girl she expected the world, but it caught in the teeth of the storm.", "cn": "当她还是个懵懂小女孩时曾对生活怀揣着无穷美妙的期许，可残酷冰冷的人生际遇，却无情将那些斑斓美梦死死绞杀在了暴风雨锋利的机械巨齿之间。"},
                {"en": "And bullet holes in her dreams; life had torn the fabric of her innocence.", "cn": "在她原本色彩斑斓的纯真梦想画卷之上，布满了现实冷枪暗箭打出的狰狞弹孔；残酷的成年人世界，已然将她纯洁无瑕的心灵织物撕扯得千疮百孔。"},
                {"en": "In the night, the stormy night, she'd close her eyes; in the night, the stormy night, away she'd fly.", "cn": "在每一个狂风骤雨呼啸撕扯的酷寒深夜里，她都会选择安静合上噙满泪水的双眼；在那雷电交加的暴风雨之夜，她的灵魂便会展开无形的羽翼，迎着风暴高高飞翔远遁！"},
                {"en": "And dream of para-para-paradise, para-para-paradise, every time she closed her eyes.", "cn": "去放肆畅游梦想着那座繁花似锦、再无苦难与眼泪的神圣伊甸乐园，在她每一次阖上双眸的深情时刻。"},
                {"en": "Lalala, hear the orchestral strings lift the child above the factory smoke of existence.", "cn": "啦啦啦，去静静倾听那宛如天籁般腾空而起的壮阔交响管弦乐浪潮吧，它正以万钧伟力，将这个苦难的孩子从凡尘间充满污浊工业硝烟的苟活深渊中一把高高托举腾空！"},
                {"en": "Still lying underneath the stormy skies, she said: Oh, I know the sun must set to rise.", "cn": "虽然肉身此刻依然被迫无助地瘫睡在电闪雷鸣的暴风雨苍穹之下，但她的嘴角却扬起了一抹坚毅从容的微笑轻语道：噢我心里比谁都坚信——落日残阳之所以坠入黑夜，纯粹只是为了在明朝黎明更加壮烈辉煌地重新破晓喷薄升起！"},
                {"en": "This could be paradise, para-para-paradise; transform your suffering into imaginative resilience.", "cn": "只要心向光明，这里便完全可以成为人人向往的神圣伊甸乐园；学会将你肉身遭受的所有苦难煎熬，彻底转化为心灵深处无穷无尽的坚韧奇思妙想吧！"},
                {"en": "The elephant costume music video in South Africa highlights playful freedom amidst hardship.", "cn": "在南非广袤荒原公路上一名乐手身着笨拙滑稽的玩偶毛绒大象装奋力骑着独轮车奔跑逃亡的传世经典MV，以荒诞不羁的幽默风骨，生动彰显了在残酷逆境中对纯粹自由的决绝追逐！"},
                {"en": "Adversity cannot imprison a mind that possesses the divine architecture of hope.", "cn": "世俗人世间最险恶的厄运逆境，也休想有能耐将一颗脑海深处早已构筑起崇高希望神圣殿堂的心灵永远囚禁捆绑在牢笼之中！"},
                {"en": "Para-para-paradise, every tear shed on earth waters the blooming garden of the soul.", "cn": "向着那座繁花盛开的理想乐园奋勇前行吧；你在尘世间洒下的每一滴委屈热泪，皆在暗中悄然浇灌哺育着你灵魂深处那座即将迎风盛开的花园！"},
                {"en": "She flew above the dark tempestuous clouds, where the celestial stars shone in absolute serene silence.", "cn": "她振翅翱翔穿透了那层遮天蔽日、电闪雷鸣的翻滚雷暴黑云，在天穹之巅的极境之上，漫天星辰正散发着纯洁安详、万籁俱寂的永恒圣洁银辉。"},
                {"en": "I know the sun must set to rise; greet tomorrow with open arms and an unbowed spirit.", "cn": "我坚信夕阳沉落必迎朝阳破晓；让我们敞开双臂、怀揣着绝不向命运屈服下跪的傲岸昂扬风骨，去拥抱每一个崭新的灿烂明天！"},
                {"en": "This could be paradise, and paradise is wherever your spirit refuses to be broken.", "cn": "人间处处皆可化作神圣乐园，而真正的伊甸天堂，便正是你那颗无论遭遇何等摧残蹂躏也誓死绝不肯被粉碎屈服的高贵灵魂所在之处！"}
            ]
        },
        {
            "title": "第 7 首 · A Sky Full of Stars · 繁星满天的夜空与无畏献祭",
            "description": "与 AVICII 联手打造的电子舞曲与浩瀚星河，因你太耀眼我甘愿为你粉身碎骨。",
            "sentences": [
                {"en": "Cause you're a sky, cause you're a sky full of stars; I'm gonna give you my heart.", "cn": "只因在我的眼中你便是一整片繁星璀璨的浩瀚无垠夜空，只因你浑身上下洒满了银河的星辉；我甘愿将我滚烫跳动的心脏，毫无保留完整奉献于你！"},
                {"en": "Cause you're a sky, cause you're a sky full of stars; cause you light up the path.", "cn": "只因你宛如一整座漫天繁星闪烁的壮阔苍穹；只因你散发出的纯白圣光，彻底照亮了我脚下原本杀机四伏的坎坷前路！"},
                {"en": "I don't care, go on and tear me apart; I don't care if you do.", "cn": "我不在乎！你尽可以尽管将我这副凡胎肉躯撕成千千万万块碎片；即便你当真这般心狠手辣，老子也甘之如饴毫不介意！"},
                {"en": "Cause in a sky, cause in a sky full of stars, I think I saw you.", "cn": "只因在这片星光璀璨、流光溢彩的无垠星海深处，我真切望见了我寻觅一生的那个神圣身影！"},
                {"en": "Cause you're a sky, you're a sky full of stars; such a heavenly view, you're such a heavenly view.", "cn": "只因你是一整座繁星满天的宏伟夜空；那是何等超凡脱俗、宛如神明天堂般令人屏息凝神的绝代旷世盛景！你是何等神圣不可方物的人间奇迹！"},
                {"en": "The driving, uplifting four-on-the-floor EDM beat produced by Avicii ignites stadium euphoria.", "cn": "由已故瑞典电音天才制作人AVICII亲手操刀编曲编排的四四拍强劲前冲EDM重低音鼓浪节拍，瞬间点燃引爆了全球数十万人体育场馆狂欢合唱的巅峰多巴胺狂喜！"},
                {"en": "Surrendering your ego completely to the radiance of an inspiring beloved is a form of spiritual transcendence.", "cn": "在一位浑身散发着纯洁浩瀚光芒的挚爱面前心甘情愿缴械自己所有的世俗傲慢小我，乃是一种通往精神崇高涅槃超脱的神圣升华之境。"},
                {"en": "Tear me apart; let the light penetrate the fractures of my mortal shell.", "cn": "哪怕将我摔得粉碎也无妨；任由你神圣的至纯光芒，透过我血肉之躯所有的龟裂缝隙，深深穿透照亮我灵魂的最暗角！"},
                {"en": "I want to die in your arms tonight, suspended in the cosmic constellation of your grace.", "cn": "我今夜甚至渴望能安详融化在你的温暖双臂怀抱深处，静静悬浮停滞在你那宛如天体星座般浩瀚神圣的温存优雅之中。"},
                {"en": "Grief melts away under the pulsating lasers and confetti showers of collective stadium joy.", "cn": "漫天飞舞的彩色碎纸屑如暴风雪般倾泻飘落，在狂暴跃动的高能激光束交织掩映之下，万千凡尘看客所有的孤寂心碎瞬间被彻底融化洗涤一空！"},
                {"en": "You're a sky full of stars; my compass spins freely in the gravity of your celestial orbit.", "cn": "你是一整片繁星密布的浩瀚苍穹；在属于你天体引力轨道的强大万有引力捕获之下，我心中的世俗指南针早已心甘情愿任性地自由疯狂旋转！"},
                {"en": "No darkness can claim a soul that chooses to become one with the radiant constellation of love.", "cn": "这世间没有任何冰冷幽暗的黑洞深渊，能够妄图吞噬霸占一颗毅然决然选择与浩瀚大爱的璀璨星宿融为一体的孤勇灵魂！"},
                {"en": "Dance beneath the diamond firmament; your heartbeat is synchronized with the cosmic pulse.", "cn": "在这钻石般晶莹剔透的神圣夜空穹顶之下尽情欢畅起舞吧；你的每一次心跳搏动，早已与整个大千宇宙生生不息的原始节拍完美共振同频！"},
                {"en": "Go on and tear me apart; in my shattered fragments, only gratitude and adoration remain.", "cn": "尽管放手将我撕扯成满天齑粉碎屑吧；在那散落一地的残存碎片之中，唯独留存下的，唯有我对上苍能让我遇见你的无尽感恩与由衷膜拜！"},
                {"en": "You're such a heavenly view; shine across my horizon until time itself dissolves into starlight.", "cn": "你宛如神明天堂垂眸人间的旷世绝美风景；请继续在我的天际线上永恒璀璨普照吧，直到时光岁月本身彻底风化消散成漫天不朽的星光！"}
            ]
        },
        {
            "title": "第 8 首 · Adventure of a Lifetime · 一生仅此一次的壮丽冒险",
            "description": "放克吉他律动与印度热带风情，让生命重新苏醒，体验脉搏狂跳的活着滋味。",
            "sentences": [
                {"en": "Turn your magic on, umi say, everything you want's a dream away.", "cn": "施展释放出你体内潜藏已久的神奇魔法吧，正如古老智者所谆谆教诲的那样：你所渴望的一切宏伟夙愿，距离你不过仅仅只隔着一层敢不敢大胆做梦的微弱薄纱！"},
                {"en": "We are legends, every day; that's what she told him.", "cn": "在我们活着的每一个看似平淡无奇的日出日落里，我们每一个人皆完全有能力成为名垂青史的不朽传奇；这正是那位充满智慧的红颜知己当年贴在他耳畔深情勉励的名言。"},
                {"en": "Turn your magic on, to me he'd say; everything you want's a dream away.", "cn": "快快彻底唤醒你骨子里的非凡神通吧，他曾无数次向我由衷倾诉：只要敢想敢拼，这人间所有的锦绣前程皆在前方静候你的凯旋！"},
                {"en": "Under this pressure, under this weight, we are diamonds taking shape.", "cn": "哪怕头顶背负着排山倒海般令人窒息的沉重世俗生活重压，哪怕肩头扛着千钧磨难重担；但你可千万别忘了——唯有在最恐怖的高温高压千锤百炼之下，稀世纯净的璀璨钻石方能破茧成型！(全曲封神哲思)"},
                {"en": "I feel my heart beating, I feel my heart beat; oh, you make me feel like I'm alive again.", "cn": "我真切感受到我胸膛深处沉睡已久的心脏正在剧烈狂跳，我听见那鲜活有力的生命脉搏正在奔腾咆哮；噢天呐，正因有你的出现，你让我破天荒头一次真真切切重新体味到了老子还鲜活活着的狂喜滋味！"},
                {"en": "Alive again; oh, you make me feel like I'm alive again.", "cn": "重获新生！彻底活过来了！噢正是你那双温柔的大手，将我这具行尸走肉彻底从麻木的泥潭中一把拉回，让我重新焕发出了无限生机！"},
                {"en": "Said: I can't go on, not in this way; I'm a dream that died by light of day.", "cn": "我昔日曾万念俱灰地自暴自弃哀叹：我再也无法像一条丧家之犬一样苟延残喘苦撑下去了；我就像一具在刺目白昼阳光的无情照射下枯萎破灭的冰冷幻梦。"},
                {"en": "Gonna hold up half the sky and say: Only I own me.", "cn": "而如今老娘偏要傲然挺立昂首挺胸独力擎起半边苍穹，向着傲慢的整个世界掷地有声庄严宣告：这天底下唯独只有我自己，才是我身体与命运的至高唯一主人！"},
                {"en": "I feel my heart beating, I feel my heart beat; you make me feel like I'm alive again.", "cn": "我真切听见了胸膛里热血沸腾的脉搏跳动；正是你重新点燃了我灵魂深处的火种，让我再次品尝到了鲜活生命的无上甘甜！"},
                {"en": "The Nile Rodgers inspired buoyant disco-funk guitar riff propels irresistible kinetic groove.", "cn": "那段深受传奇吉他放克宗师尼罗·罗杰斯灵感启发的欢快迪斯科放克切音吉他旋律，以摧枯拉朽之势驱动起了一种让人根本无法按捺住起舞冲动的磅礴动能律动！"},
                {"en": "Monotony is spiritual asphyxiation; passion is the oxygen that resuscitates the soul.", "cn": "日复一日循规蹈矩的枯燥庸俗，是对崇高心灵最残忍的无声扼杀窒息；而发自肺腑的炽热激情与向往，才是能让你垂死灵魂彻底起死回生的无价纯氧！"},
                {"en": "If we've only got this life, this adventure, then I want to share it all with you.", "cn": "倘若我们在浩瀚轮回长河中仅仅有幸拥有眼前这区区短短几十载的人间漫步旅途，拥有这仅此一次的壮丽人生大冒险，那么我愿毫无保留将我所有的悲欢离合统统与你携手共享！"},
                {"en": "We are diamonds taking shape; let the crushing pressure forge your unbreakable resilience.", "cn": "我们每一个人皆是正在高压熔炉中淬炼成型的璀璨钻石；任凭现实生活沉重的巨石迎面狠狠砸来吧，它只会将你骨子里的坚不可摧风骨打磨得愈发流光溢彩！"},
                {"en": "Alive again! Step out of the tomb of routine and embark on the adventure of a lifetime.", "cn": "彻底活过来了！勇敢推开并踏出那座名为‘循规蹈矩日常’的冰冷精神坟墓吧，昂首阔步，去奔赴这场属于你一生仅此一次的波澜壮阔伟大冒险！"},
                {"en": "Turn your magic on; we are legends in the making beneath the radiant morning sun.", "cn": "释放你体内所有的神通魔力吧；在破晓喷薄而出的明媚朝阳之下，我们每一个人，皆正在以不可阻挡之势书写着名垂青史的不朽传奇篇章！"}
            ]
        },
        {
            "title": "第 9 首 · Hymn for the Weekend · 周末圣歌与生命甘霖的狂欢",
            "description": "碧昂斯伴唱与孟买洒红节色彩风暴，让干涸的心灵沐浴在生命的狂欢甘霖中。",
            "sentences": [
                {"en": "Drink from me, drink from me, then we'll shoot across the sky; symphony, then we'll shoot across the sky.", "cn": "来吧尽情痛饮我体内的生命甘霖吧，大口畅饮吧，随后我们将化作两道撕裂黑夜的璀璨闪电呼啸并肩穿梭过九天长空；奏响这壮阔无匹的宏伟交响乐章，让我们如流行般划破苍穹！"},
                {"en": "Pour on a foundation; gotta drink from the fountain of living passion.", "cn": "在这片辽阔的人生厚土之上浇灌奠定起属于我们的坚固基石；我们必须俯身开怀畅饮那座奔涌不息的鲜活激情生命泉眼喷涌出的甘甜泉水。"},
                {"en": "Oh, angel sent from up above, you know you make my world light up.", "cn": "噢上苍神明特意派遣降临到我身旁的纯洁天使啊，你心里比谁都清楚：正是你的回眸浅笑，瞬间彻底照亮了我整座原本暗无天日的灰暗世界！"},
                {"en": "When I was down, when I was hurt, you came to lift me up.", "cn": "每当我身陷人生泥潭跌落谷底消沉萎靡之际，每当我被残酷现实打得皮开肉绽遍体鳞伤之时，唯独只有你毫不犹豫从天而降，伸出温暖有力的双手将我一把高高拉起！"},
                {"en": "Life is a drink and love's a drug, oh now I think I must be miles high.", "cn": "这人世间的鲜活生命是一壶令人欲罢不能的甘冽美酒，而至纯的真爱则是一剂让人彻底沉沦神魂颠倒的神奇良药，噢此时此刻我只觉自己的神智早已飘上了九万英里的辽阔云端！"},
                {"en": "When I was a river dried up, you came to rain a flood.", "cn": "当年我就如同一条早已彻底干涸见底、布满龟裂黄沙的枯竭死河，正是你的深情降临，宛如一场滔天破晓的狂暴暴雨洪流般，瞬间让我的生命重获生机！"},
                {"en": "You said: Drink from me, drink from me, when I was so thirsty.", "cn": "你在我耳畔温存呼唤：只管尽情畅饮我的一切吧我的爱人，尽情痛饮吧，当我曾在这片精神荒原上渴得嗓子冒烟快要干枯致死之际。"},
                {"en": "Pour on a symphony, now I just can't get enough; put your wings on me, when I was so heavy.", "cn": "任由这场磅礴跌宕的宏伟交响乐如暴风雨般倾泻浇灌在我心头吧，我此刻贪婪得根本不知满足；当我的躯壳曾沉重得宛如灌了生铅寸步难行时，是你亲手将一双洁白无瑕的飞翔羽翼轻柔披在了我的肩头！"},
                {"en": "Got me feeling drunk and high, so high, so high; oh, I think I must be miles high.", "cn": "你让我整个人彻底陶醉在微醺与狂喜的极乐云端之中，飘飘欲仙、高耸入云，直插天际；噢天呐，我此刻必定已然神游遨游在九霄云外的万丈高空！"},
                {"en": "Filmed during the exuberant Holi festival of colors in Mumbai, the visuals vibrate with spiritual ecstacy.", "cn": "在印度孟买盛大热烈的传统洒红节期间实景拍摄的传世经典MV，漫天飞舞扬起的五彩斑斓绚烂彩色粉末与欢腾人群交相辉映，处处震颤洋溢着超凡脱俗的心灵狂喜神圣气场！"},
                {"en": "Beyoncé's majestic operatic vocal runs elevate the chorus into a modern gospel hymn.", "cn": "流行天后碧昂斯那宛如歌剧女武神般高亢雄浑、荡气回肠的惊世真声长音转音伴唱，瞬间将整首副歌升华锻造成了一曲足以洗涤全人类灵魂的现代福音赞美诗！"},
                {"en": "Celebrate the weekend not merely as temporal respite, but as a sacred liturgical renewal of the human joy.", "cn": "绝不要仅仅把周末当成肉体逃避繁重苦工的苟且喘息片刻；要将其奉为一次让全人类欢愉本能重新得以神圣洗礼、焕发新生的庄严精神庆典！"},
                {"en": "When you are a dried-up riverbed, open your heart to the flood of communal grace.", "cn": "每当你觉得自己快要沦为一条干涸龟裂的荒凉河床时，果断敞开你的心扉吧，去迎接拥抱那场由大爱与集体善意汇聚而成的滔天甘霖倾盆洪流！"},
                {"en": "Drink from the fountain of unconditional love, and watch your arid wilderness transform into an emerald oasis.", "cn": "在无条件真爱喷涌而出的生命神泉前开怀痛饮吧；好好亲眼看着你内心那片原本寸草不生的荒芜沙漠，在一夜之间不可思议地蜕变成一座郁郁葱葱的翡翠绿洲！"},
                {"en": "So high, so high; let the exuberant melody lift you above the mundane gravity of earthly sorrows.", "cn": "高高飞翔吧，向着九霄云端翱翔吧！任由这激昂欢畅的天籁旋律，将你彻底高高托举拔离这凡尘俗世间所有沉重琐碎的哀伤引力束缚！"}
            ]
        },
        {
            "title": "第 10 首 · Everglow · 心底永不熄灭的温存微光",
            "description": "极简独奏钢琴与克里斯·马汀前妻格温妮丝伴唱，纪念逝去但永恒温暖的故人。",
            "sentences": [
                {"en": "Oh, they say people come, say people go; this particular diamond was extra special.", "cn": "噢人们总在叹息说这人世间的过客来来往往熙熙攘攘，缘聚缘散皆是寻常；但曾经陪伴在我身畔的那颗独一无二的稀世璀璨钻石，却比这世间任何瑰宝都要非凡高贵。"},
                {"en": "And though you might be gone, and the world may not know, still I see you celestial.", "cn": "尽管此时此刻你肉身的步履或许已然远行离去消散在风中，尽管这冷漠喧嚣的凡尘世俗或许早已忘却了你的音容，但在我的灵魂眼眸深处，我依然真切望见你如天神般圣洁高贵永存！"},
                {"en": "Like a lion you ran, a goddess you rolled; like an eagle circle and your colors unfold.", "cn": "你曾如威严勇猛的森林雄狮般在这大地上骄傲昂首狂奔，你曾如超凡脱俗的九天神女般在这凡尘间翩跹漫步；你如展翅翱翔的苍鹰般在天穹盘旋回转，任由你斑斓绚丽的生命华彩尽情绽放舒展！"},
                {"en": "Now they've ceased, but we've granted you to hold; but there's a light that the world cannot take.", "cn": "如今那一切轰轰烈烈的传奇篇章终究归于平静死寂，但我们曾心甘情愿将最深沉的真爱托付于你掌心；而且有一抹神圣的微光，是这世间任何强权与死神皆休想夺走的！"},
                {"en": "When I'm cold, cold; when I'm cold, cold, there's a light that you give me when I'm in shadow.", "cn": "每当我在刺骨严寒中冻得浑身发抖瑟瑟战栗之际，每当我深陷孤立无援的漫长阴霾长夜之时，是你生前曾赐予我的那抹温存圣光，始终在暗处默默守护温暖着我！"},
                {"en": "There's a feeling within me, an everglow.", "cn": "有一股浩瀚神圣的温存暖流正在我心房最深处长久激荡流淌，那是一抹永不熄灭、万古长青的永恒微光！"},
                {"en": "Like brothers in blood, or sisters who ride, and we swore on that night we'd be friends 'til we die.", "cn": "我们曾宛如血浓于水的结拜手足亲骨肉，曾如同策马并肩驰骋天涯的同道挚友；在那个漫天繁星的难忘长夜，我们曾指天誓日赌咒发誓：此生同生共死直到生命终结！"},
                {"en": "But the changing of winds and the car crashes through; oh, I'm so heavy, but the world was made for you.", "cn": "然而命运突如其来的诡谲变幻长风无情呼啸吹散了一切，飞来横祸的惨烈车祸梦魇般撕裂了所有山盟海誓；噢我此刻的心情是何等沉重如铁，但这壮丽的人间，分明当年是专为你量身打造的秀场啊！"},
                {"en": "So if you love someone, you should let them know, oh, the light that you left me will never leave.", "cn": "所以倘若你心头此刻正深爱着某个人，请务必立刻大声告诉他你的心意千万莫留遗憾；噢你临终前深情留给我的那缕神圣光明，此生此世必将与我如影随形、至死不弃！"},
                {"en": "Muhammad Ali's speech about dedication and love plays softly in the stadium fade-out.", "cn": "拳王穆罕默德·阿里生前关于无私奉献与大爱真谛的那段铿锵有力的珍贵历史演讲原声录音，在万人体育馆大合唱渐渐散去的终曲淡出中，悠扬深情地回荡在天穹深处。"},
                {"en": "The melancholic piano ballad centers on the bittersweet glow that remains after an irreplaceable soul departs.", "cn": "这首感人至深、百转千回的古典大三角钢琴抒情挽歌，将全副心神死死聚焦于一位无可替代的至亲挚友离世长眠之后，在幸存者心头所长久遗留下的那份交织着苦涩与无上温存的神圣微光。"},
                {"en": "Grief is the price we pay for the privilege of experiencing transcendent companionship.", "cn": "直面至亲离世所承受的心碎哀伤，乃是我们在有限的人生岁月里，曾有幸深度品尝过那段超凡脱俗、灵魂相契的崇高神仙陪伴所必须奉献付出的沉痛神圣代价！"},
                {"en": "When I'm cold, there's a light that you give me; an everglow that defies the finality of the grave.", "cn": "每当漫长冬夜刺骨的寒意袭来，你赐予我的那抹微光便会在心头悄然亮起；这是一抹足以彻底嘲弄击溃死神冰冷墓碑终结教条的永恒不朽余晖！"},
                {"en": "Cherish the living while their laughter rings in your ears; speak your love before the sunset claims the sky.", "cn": "趁着挚爱之人的清脆欢声笑语依然在耳畔清晰回荡之际，去加倍由衷珍视身畔的眼前人吧；在残阳血落彻底被黑夜吞噬之前，大声吐露出你所有的爱意吧！"},
                {"en": "There's a light within me, an everglow; you walk with me through the shadows, undefeated and beloved.", "cn": "有一道神圣的温存微光在我心房深处万古长青；在穿越往后一切幽暗长夜的孤勇征途上，你始终与我并肩同行，未尝一败，永远被我奉为挚爱！"}
            ]
        }
    ]))

    return courses
