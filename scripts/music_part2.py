# -*- coding: utf-8 -*-
from builder_core import build_course

def get_music_part2():
    courses = []

    # 3. 《迪士尼经典动画主题曲》(Disney Songs) · 10 章全集
    courses.append(build_course({
        "id": "course-mus-disney",
        "title": "《迪士尼经典动画主题曲》(Disney Songs) · 奇幻童话与造梦金曲 (10章全集)",
        "category": "music",
        "categoryName": "音乐英语",
        "coverGradient": "from-blue-600 via-sky-500 to-indigo-800",
        "icon": "🏰",
        "description": "百年造梦工厂传世主题曲，狮子王、冰雪奇缘、阿拉丁、小美人鱼原声金曲全收录。",
        "difficulty": "初级 A2",
        "tags": ["迪士尼", "动画主题曲", "纯真童年", "朗朗上口"]
    }, [
        {
            "title": "第 1 首 · 狮子王 · 生生不息与荣耀大地",
            "description": "Circle of Life 宏伟非洲原野的生命赞歌，万物循环运转。",
            "sentences": [
                {"en": "From the day we arrive on the planet and blinking, step into the sun.", "cn": "从我们呱呱坠地降临到这颗美丽星球、眨动着清澈双眸初次迈入金灿灿暖阳的那一天起。"},
                {"en": "There's more to see than can ever be seen, more to do than can ever be done.", "cn": "眼前所展现的奇景远超我们肉眼所能阅尽的极限，这天地间等待开拓的伟业远胜我们一生所能企及的边界。"},
                {"en": "There's far too much to take in here, more to find than can ever be found.", "cn": "这大千世界蕴藏的万千奥秘是如此博大精深，值得去探寻的瑰宝远超凡尘凡夫所能穷尽。"},
                {"en": "But the sun rolling high through the sapphire sky keeps great and small on the endless round.", "cn": "然而高悬在蔚蓝如洗蓝天之巅的耀眼烈日，公正无私地引领着世间芸芸众生在大自然的无穷循环中繁衍生息。"},
                {"en": "It's the circle of life, and it moves us all through despair and hope, through faith and love.", "cn": "这就是生生不息的大自然生命之环，它引领着我们跋涉过绝望的幽谷与希望的平原，穿越坚定的信念与炽热的大爱！"},
                {"en": "Till we find our place on the path unwinding in the circle, the circle of life.", "cn": "直到我们在这条曲折蜿蜒展开的生命轨迹长河中，最终笃定寻觅到属于我们自己的天命归宿！"},
                {"en": "The Zulu opening chant announces the dawn of a future king upon Pride Rock.", "cn": "嘹亮神圣的祖鲁语开场长啸撕裂长空，向着全非洲广袤原野庄严宣告荣耀石之巅未来新王的破晓诞生。"},
                {"en": "Every living creature bows in reverence to the eternal rhythm of nature.", "cn": "茫茫草原上的每一个鲜活生灵，无不肃穆躬身致敬大自然至高无上、永恒运转的造化节拍。"},
                {"en": "The delicate balance of the savanna requires strength tempered by wisdom and humility.", "cn": "维系热带稀树草原生态系统的精妙平衡，需要的绝不仅仅是蛮力爪牙，而是兼具大智大勇与悲悯谦逊的王者风范。"},
                {"en": "Simba held aloft above the assembled herds symbolizes generational continuity.", "cn": "年幼的辛巴在万兽朝拜中被高高托举向天穹的一刹那，象征着王族血脉与生命火种千秋万代的生生不息。"},
                {"en": "Through despair and hope, the kingdom endures the harsh drought to witness the green rains.", "cn": "在绝望与希望的交织淬炼之中，整片辽阔王国顽强挺过了酷烈干旱的折磨考验，终将迎回甘霖润泽的青翠复苏。"},
                {"en": "A king's time as ruler rises and falls like the morning and evening sun.", "cn": "哪怕是不可一世的一代明君霸主，其在位治世的荣光岁月也如日出日落般有起有伏、难逃自然更迭法则。"},
                {"en": "We are all connected in the great circle of life; honor the soil that feeds your roots.", "cn": "在这生生不息的宏伟生命之环里，我们大千生灵休戚与共；由衷敬畏滋养哺育你根系的厚德沃土吧。"},
                {"en": "The circle of life moves us all toward our destined horizon with courage.", "cn": "生命生生不息的巨轮正引领着我们全体生灵，满怀豪迈勇气大步迈向属于我们的天命地平线。"},
                {"en": "In the circle, the circle of life, love reigns supreme over darkness and fear.", "cn": "在这生生不息的神圣循环之中，唯有至高无上的纯真大爱，方能彻底驱散黑暗与恐惧的阴霾！"}
            ]
        },
        {
            "title": "第 2 首 · 冰雪奇缘 · 随心而行 Let It Go",
            "description": "艾莎女王打破枷锁、在北山筑起冰雪神殿的无敌觉醒蜕变。",
            "sentences": [
                {"en": "The snow glows white on the mountain tonight, not a footprint to be seen.", "cn": "皑皑白雪在今夜险峻的群山之巅泛着皎洁寒光，举目望去，茫茫雪原之上寻不见哪怕半只行人的足迹。"},
                {"en": "A kingdom of isolation, and it looks like I'm the queen.", "cn": "这是一座与世隔绝、被冰雪彻底封印的孤独幽闭王国，而放眼极目四周，我似乎正是这里名副其实的唯一女王。"},
                {"en": "The wind is howling like this swirling storm inside; couldn't keep it in, heaven knows I tried.", "cn": "屋外呼啸狂暴的寒风恰似我灵魂深处肆虐翻滚的暴风骤雨；我早已无力将这股神力继续死死压抑在心底，苍天在上，唯有神明知晓我曾多么拼命克制隐忍！"},
                {"en": "Don't let them in, don't let them see; be the good girl you always have to be.", "cn": "千万别放他们进来，绝不要让他们窥见真相；务必始终扮演好那个逆来顺受、懂事体面的完美乖女孩！"},
                {"en": "Conceal, don't feel, don't let them know; well, now they know!", "cn": "藏匿锋芒，封锁知觉，绝不能走漏半点风声；好吧！既然如今所有人都已知晓，那老娘便再也无需伪装！"},
                {"en": "Let it go, let it go, can't hold it back anymore!", "cn": "随它去吧！彻底放手吧！我体内奔涌的伟力再也休想被任何枷锁所束缚捆绑！"},
                {"en": "Let it go, let it go, turn away and slam the door!", "cn": "随它去吧！坦荡释怀吧！毅然转身离去，狠狠摔上那扇尘世羁绊的沉重门扉！"},
                {"en": "I don't care what they're going to say; let the storm rage on, the cold never bothered me anyway.", "cn": "我再也不会在乎这人世间闲杂看客们评头论足的蜚语流言；任凭暴风雪咆哮肆虐吧，这刺骨严寒，从始至终就从未真正让我困扰过分毫！"},
                {"en": "It's funny how some distance makes everything seem small.", "cn": "说来当真奇妙滑稽：只要与喧嚣凡尘拉开一段居高临下的遥远距离，曾经那些压得人喘不过气的纷扰琐事瞬间显得何等微不足道！"},
                {"en": "And the fears that once controlled me can't get to me at all!", "cn": "而昔日那些曾死死支配扼杀我灵魂自由的无形恐惧魔爪，如今在这巍峨雪峰之上再也休想触及我分毫！"},
                {"en": "It's time to see what I can do, to test the limits and break through.", "cn": "是时候彻底放开手脚，好好看一看我究竟蕴藏着何等通天彻底的本领了；去勇敢突破能力的极限，去打碎一切不可逾越的高墙！"},
                {"en": "No right, no wrong, no rules for me; I'm free!", "cn": "没有世俗教条的条条框框，没有虚伪的说教对错；此时此刻，我是彻底解放、顶天立地的自由生灵！"},
                {"en": "My power flurries through the air into the ground; my soul is spiraling in frozen fractals all around.", "cn": "我体内的磅礴魔法呼啸穿透虚空狠狠注入坚硬大地；我的灵魂正化作漫天盘旋飞舞的瑰丽冰雪结晶分形，在苍穹四野肆意绽放盛开！"},
                {"en": "And one thought crystallizes like an icy blast: I'm never going back, the past is in the past!", "cn": "一道决绝果敢的钢铁意志如万载玄冰般在心头彻底凝结固化：老娘此生绝不回头！那不堪回首的憋屈过往，早该彻底扫入历史尘埃！"},
                {"en": "Here I stand in the light of day; let the storm rage on, the cold never bothered me anyway!", "cn": "我巍然傲立在朗朗乾坤的璀璨骄阳圣光之下；任由天地风暴狂暴咆哮吧，这区区冰霜严寒，从来都奈何不了老娘分毫！"}
            ]
        },
        {
            "title": "第 3 首 · 阿拉丁 · 崭新的世界 A Whole New World",
            "description": "乘坐神奇魔毯穿梭云端与星空，俯瞰午夜开罗与浪漫飞毯冒险。",
            "sentences": [
                {"en": "I can show you the world: shining, shimmering, splendid.", "cn": "我能领你领略整个辽阔无垠的壮丽人间：处处流光溢彩、闪耀夺目、波澜壮阔。"},
                {"en": "Tell me, princess, now when did you last let your heart decide?", "cn": "告诉我吧，被困在深宫金丝雀笼里的尊贵公主：你上一次真正顺从自己的内心大胆做出抉择，究竟是在哪年哪月？"},
                {"en": "I can open your eyes, take you wonder by wonder, over, sideways and under on a magic carpet ride.", "cn": "我能为你推开洞察奇迹的眼眸，领你领略一幕接一幕令人屏息的天下奇观；乘着这柄通灵魔毯，在云端上下翻飞、穿梭翱翔！"},
                {"en": "A whole new world, a new fantastic point of view.", "cn": "展现在眼前的是一个崭新的宏伟世界，一个打破常规、充满无穷奇幻神采的全新造化视角！"},
                {"en": "No one to tell us no, or where to go, or say we're only dreaming.", "cn": "在这九天之上，再也没有任何道貌岸然之徒敢指手画脚对我们说不，没有人能指责我们该去向何方，更休想嘲讽我们不过是在白日做梦！"},
                {"en": "A whole new world, a dazzling place I never knew.", "cn": "一个完完全全崭新的美妙大千世界，一座在此之前我深闺之中从未有幸瞻仰过的目眩神迷人间乐土！"},
                {"en": "But when I'm way up here, it's crystal clear that now I'm in a whole new world with you.", "cn": "然而当我和你并肩翱翔在这高耸入云的天穹之巅时，我内心无比清澈笃定：正因有你相伴身侧，这个崭新的世界才显得如此璀璨动人！"},
                {"en": "Unbelievable sights, indescribable feeling, soaring, tumbling, freewheeling through an endless diamond sky.", "cn": "令人难以置信的壮丽山川异景，言语难以尽述的酣畅淋漓欢愉；在钻石般星光璀璨的浩瀚无垠夜空深处自由翱翔、翻滚穿梭、随心所欲！"},
                {"en": "A whole new world; don't you dare close your eyes.", "cn": "一个崭新破晓的奇妙世界；千万不要胆怯眨眼，快睁大双眼把这绝美风光尽收眼底！"},
                {"en": "A hundred thousand things to see; hold your breath, it gets better.", "cn": "有成千上万处波澜壮阔的锦绣山河在等待我们去饱览瞻仰；屏住呼吸吧，更震撼的奇景还在前方！"},
                {"en": "I'm like a shooting star, I've come so far, I can't go back to where I used to be.", "cn": "我宛如一颗划破深邃夜空的璀璨耀眼流星，一路风驰电掣冲出了如此遥远的天际，再也绝不可能倒退蜷缩回昔日逼仄的方寸牢笼！"},
                {"en": "Every turn a surprise, with new horizons to pursue.", "cn": "魔毯的每一次轻灵转向，都迎面撞见令人叹为观止的崭新惊喜，引领着我们去追逐更加辽阔的地平线！"},
                {"en": "Every moment red-letter; I'll chase them anywhere, there's time to spare, let me share this whole new world with you.", "cn": "与你同行的每一分每一秒都值得被用鲜红浓墨永久载入记忆金石；我愿陪你天涯海角随风追逐，让我与你共同分享这一整个崭新世界的浩瀚壮丽！"},
                {"en": "Alan Menken's soaring melody turns a romantic flight into a timeless manifesto of self-determination.", "cn": "传奇作曲巨匠艾伦·曼肯谱写出的高亢优美旋律，将一场浪漫至极的双人云端飞毯之旅，彻底升华成了一篇全人类争取自主自由的时代宣言！"},
                {"en": "A whole new world, that's where we'll be; a thrilling chase, a wondrous place for you and me.", "cn": "一个完完全全属于我们崭新未来的光明世界，那正是你我天命所归的相伴之地；一场惊心动魄的浪漫追逐，一座专为你我盛开的奇迹乐土！"}
            ]
        },
        {
            "title": "第 4 首 · 美女与野兽 · 古老如初的真爱颂歌",
            "description": "Tale as Old as Time，烛台时钟伴奏下，金色礼服与野兽华尔兹起舞。",
            "sentences": [
                {"en": "Tale as old as time, true as it can be.", "cn": "这是一则古老如初、与人类岁月同寿的传世童话传奇；它比人世间所能言说的所有真理还要真挚无瑕。"},
                {"en": "Barely even friends, then somebody bends unexpectedly.", "cn": "起初相逢之时彼此防备冷若冰霜、甚至连点头之交的普通朋友都算不上；然而在不知不觉的相处瞬间，总有某个人心甘情愿率先放下了内心的骄傲戒备。"},
                {"en": "Just a little change, small to say the least, both a little scared, neither one prepared.", "cn": "仅仅只是微不足道的一点点善意细微转变，用尽言语形容都显得极其纤细渺小；彼此心头都难免泛起一丝对未知的忐忑不安，谁也未曾料到命运的降临竟如此猝不及防。"},
                {"en": "Beauty and the Beast, stepping softly into the ballroom under the golden chandelier.", "cn": "美丽善良的少女与面容凶悍的野兽，在一盏盏流光溢彩的奢华巨型鎏金水晶吊灯照耀之下，轻移莲步缓缓步入空旷大理石舞厅中央。"},
                {"en": "Ever just the same, ever a surprise, ever as before, and ever just as sure as the sun will rise.", "cn": "爱情的本质亘古未变始终如一，却在每一次心动邂逅的瞬间总能带来震撼心灵的崭新惊喜；它历经沧海桑田一如往昔，正如每日清晨东方地平线上那一轮红日必定破晓升起般无可置疑！"},
                {"en": "Certain as the sun rising in the east; tale as old as time, song as old as rhyme, Beauty and the Beast.", "cn": "正如明朗旭日永远坚定不移自东方冉冉升起那样笃定；这是一出与光阴岁月同寿的古老传说，一曲同人类诗韵同源的永恒情歌——《美女与野兽》！"},
                {"en": "Angela Lansbury recorded this legendary track in a single take after traveling all night.", "cn": "传奇配音艺术家安吉拉·兰斯伯里在经历了一整夜疲惫的跨洋奔波之后，竟然在录音棚里仅凭一条原声录制，便一气呵成创造了这尊名垂影史的不朽绝唱！"},
                {"en": "True nobility lies not in a handsome aristocratic face, but in the tender capacity to love selflessly.", "cn": "这世间真正高贵纯良的人格品质，绝不在于拥有一副如何英俊迷人的贵族皮相容颜；而在于一颗懂得毫无保留、无私奉献去深爱他人的柔软仁慈之心。"},
                {"en": "Belle looked past the fearsome fangs and claws to recognize the gentle, tormented soul within.", "cn": "贝儿那双睿智仁善的明眸彻底穿透了野兽外表狰狞可怖的獠牙利爪，一眼洞悉并拥抱了他躯壳深处那个饱受宿命诅咒折磨的孤独温柔灵魂。"},
                {"en": "The yellow ballgown swirling against the midnight blue velvet coat remains an immortal cinematic tableau.", "cn": "那袭金黄灿烂的华美晚礼服在幽蓝天鹅绒燕尾服身畔如花朵般旋转盛开起舞的唯美剪影，永远定格成了全人类电影艺术长廊里一座不朽的视觉丰碑！"},
                {"en": "Love has the miraculous power to dissolve ancient curses and tame the wildest internal turmoil.", "cn": "纯粹真挚的至纯大爱拥有一种能化腐朽为神奇的不可思议魔力，足以瓦解人世间所有恶毒残酷的万年诅咒，彻底抚平灵魂深处最狂暴的野性惊涛。"},
                {"en": "Tale as old as time, tune as old as song, bitter-sweet and strange, finding you can change.", "cn": "古老如天地初开的动人传说，悠扬若人类歌唱源头的传世曲调；饱尝苦涩与甘甜的奇妙交织，让你蓦然惊觉原来自己为了真爱竟能脱胎换骨蜕变得如此温存。"},
                {"en": "Learning you were wrong, discovering that beneath the prickly surface lies a vulnerable human heart.", "cn": "在真爱面前谦逊承认自己过往认知的大错特错，惊喜发现原来在那副多刺凶悍的坚硬外壳之下，深藏着一颗极易受创却炽热滚烫的人类真心。"},
                {"en": "Certain as the sun rising in the east, tale as old as time, Beauty and the Beast.", "cn": "宛如旭日东升般坚定不移，岁月流淌永不褪色；这是一曲敬畏生命、歌颂真爱的永恒史诗《美女与野兽》。"},
                {"en": "Look beyond the surface of what the world judges, and you will find miracles blooming in darkness.", "cn": "学会彻底跳脱世俗庸碌看客那些浮皮潦草的肤浅评判吧，你必将惊奇目睹：最神圣不可思议的奇迹花朵，往往正在最幽暗无光的角落里静静芬芳绽放！"}
            ]
        },
        {
            "title": "第 5 首 · 海洋奇缘 · 浩瀚汪洋在呼唤我 How Far I'll Go",
            "description": "莫阿娜打破岛屿边界禁忌，独自扬帆驶向浩瀚大洋的冒险之心。",
            "sentences": [
                {"en": "I've been staring at the edge of the water long as I can remember, never really knowing why.", "cn": "在我不记事的童年最初记忆里，我便日复一日久久痴痴凝望着波涛汹涌的海水边界，心中却从来参不透究竟为何对它如此魂牵梦绕。"},
                {"en": "I wish I could be the perfect daughter, but I come back to the water, no matter how hard I try.", "cn": "我多么渴望自己能做一个安分守己、顺从族人期盼的完美乖巧继承人酋长女儿，可无论我内心如何拼命告诫自己克制，我的脚步终究会不可遏制地重新跑回海浪身旁！"},
                {"en": "Every turn I take, every trail I track, every path I make, every road leads back to the place I know.", "cn": "我在这座海岛上尝试走过的每一个拐弯路口，我踏足勘探过的每一条林间小径，我开辟出的一道道前路，最终却无一例外兜兜转转重新指向了我深知的那处起点。"},
                {"en": "Where I cannot go, though I long to be, beyond the reef where the great ocean roars.", "cn": "那是我作为酋长女儿被严厉禁足绝不允许涉足的禁忌绝地，然而那却是我灵魂日夜向往的归宿——在那狂风怒号的珊瑚暗礁彼岸，浩瀚无垠的巨浪正在召唤！"},
                {"en": "See the line where the sky meets the sea? It calls me!", "cn": "快抬头看那海天相接、波澜壮阔的遥远水天一色地平线！它正在声嘶力竭呼唤着我的名字！"},
                {"en": "And no one knows how far it goes; if the wind in my sail on the sea stays behind me, one day I'll know.", "cn": "没有人知晓这片神秘莫测的广袤汪洋究竟能绵延向多么遥远的天涯海角；但只要海面上的浩荡长风始终在我扬起的风帆身后鼓劲助推，终有一天我将亲自揭晓谜底！"},
                {"en": "If I go, there's just no telling how far I'll go!", "cn": "倘若我此刻鼓足勇气毅然扬帆起航破浪出征，究竟能远行到多么波澜壮阔的遥远彼岸，连我自己都无法想象！"},
                {"en": "I know everybody on this island seems so happy on this island; everything is by design.", "cn": "我心里清楚，居住在这座与世隔绝岛屿上的每一个淳朴族人都显得何其安居乐业、怡然自得；这里的一切日常生息都被安排得井井有条、丝丝入扣。"},
                {"en": "I know everybody on this island has a role on this island, so maybe I can roll with mine.", "cn": "我深知这片小天地里的每一个人都在部落宗族中扮演着不可或缺的固定本分角色，所以或许我也该认命，乖乖扮演好我这一生的本分？"},
                {"en": "I can lead with pride, I can make us strong; I'll be satisfied if I play along, but the voice inside sings a different song.", "cn": "我完全有能力满怀荣耀地英明领导族人，我能带领大家丰衣足食繁荣昌盛；只要我顺从世俗规矩安分守己，我理应感到知足常乐；然而我灵魂深处的古老声音，却日夜在唱着一首完全截然不同的激昂之歌！"},
                {"en": "What is wrong with me? See the light as it shines on the sea? It's blinding!", "cn": "我究竟是怎么了？！快看破晓晨曦那道璀璨万丈的万道圣光如烈火般倾泻铺洒在沸腾的大海之上！它是何等目眩神迷、摄人心魄！"},
                {"en": "And it seems like it's calling out to me, so come find me, and let me know what's beyond that line.", "cn": "它仿佛化作了一道来自远古祖先的深情呼唤向我招手呼喝：快来寻觅我吧！勇敢跨过暗礁，去亲眼看清在那道水天交界线的彼端究竟矗立着怎样的宏伟天地！"},
                {"en": "Lin-Manuel Miranda's polyrhythmic composition captures the ancestral voyaging spirit of the Pacific.", "cn": "百老汇鬼才林-曼努尔·米兰达创作出的复调交织惊艳旋律，生动淋漓尽致地捕捉唤醒了南太平洋波利尼西亚先民们刻在骨髓里的伟大远航探险基因！"},
                {"en": "Safety within the reef can become a comfortable prison if it suffocates your destined horizon.", "cn": "倘若缩在避风暗礁之内的所谓的绝对安稳平顺，彻底扼杀窒息了你本该展翅翱翔的天命辽阔地平线，那么这份安逸便已悄然沦为了一座舒适的无形牢笼！"},
                {"en": "One day I'll know how far I'll go; hoist the outrigger sail and navigate by the ancestral stars!", "cn": "终有一天我必将亲手丈量这片苍穹大海的极限！奋力扬起独木舟的双体风帆吧，仰望群星罗盘的古老指引，向着汪洋深处破浪出征！"}
            ]
        }
    ]))

    return courses
