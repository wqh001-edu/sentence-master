# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))
from builder_core import build_course, save_ts_file
import music_part1
import data_music

def generate_music():
    print("🎵 正在生成【音乐英语】8 门全集课程...")
    courses = []
    
    # 1. 披头士 (已在 music_part1 中完成 10 章)
    courses.extend(music_part1.get_music_part1())
    
    # 2. 泰勒·斯威夫特 (已在 data_music 中完成 10 章)
    courses.append(data_music.get_all_music()[1])
    
    # 3. 迪士尼经典动画主题曲 (10章)
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
            "title": "第 1 首 · 狮子王 · Circle of Life 生生不息",
            "description": "非洲大草原万兽朝拜，生命轮回与生生不息的宏伟壮歌。",
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
            "title": "第 2 首 · 冰雪奇缘 · Let It Go 随心而行",
            "description": "艾莎女王打破世俗枷锁，在北山冰川之上放声高唱自由觉醒。",
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
            "title": "第 3 首 · 阿拉丁 · A Whole New World 崭新的世界",
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
            "title": "第 4 首 · 美女与野兽 · Beauty and the Beast 传世真爱",
            "description": "大理石舞厅水晶吊灯下，金色长裙与野兽翩跹起舞的纯真爱情。",
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
            "title": "第 5 首 · 海洋奇缘 · How Far I'll Go 汪洋之召唤",
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
        },
        {
            "title": "第 6 首 · 小美人鱼 · Part of Your World 那个属于你的世界",
            "description": "爱丽儿在海底秘密藏宝洞，渴望用鱼尾换取双腿走入陆地人间。",
            "sentences": [
                {"en": "Look at this stuff, isn't it neat? Wouldn't you think my collection's complete?", "cn": "快瞧瞧这琳琅满目的神奇藏品，难道它们不够巧夺天工别致吗？难道换作是你，不会认定我的珍藏早已丰饶完备了吗？"},
                {"en": "Wouldn't you think I'm the girl, the girl who has everything?", "cn": "难道换作任何一个旁人冷眼旁观，不会由衷认定我就是那个坐拥天下万千宠爱、什么都不缺的受眷顾女孩吗？"},
                {"en": "Look at this trove, treasures untold; how many wonders can one cavern hold?", "cn": "快好好打量这整座洞穴深处堆积如山、难以计数的海底无价秘宝吧；试问这世间有哪一座石洞，能够同时容纳下如此浩繁壮丽的奇珍异兽与文明遗物？"},
                {"en": "Looking around here, you'd think: Sure, she's got everything.", "cn": "放眼环顾周遭这片熠熠生辉的宝库，换作谁都会笃定慨叹：没错啊，她早已坐拥了一切！"},
                {"en": "I've got gadgets and gizmos a-plenty; I've got whozits and whatzits galore.", "cn": "我手头收集了数不胜数的奇巧人类发明小机械与精巧零件；我网罗了成打成打叫不上名目的人类日常稀罕物件。"},
                {"en": "You want thingamabobs? I've got twenty! But who cares? No big deal, I want more.", "cn": "你想要稀奇古怪的人类小玩意儿吗？我这儿随手就能翻出二十件！但这又有什么值得夸耀的呢？这根本不算什么，我灵魂深处渴望得到的是更伟大的天地！"},
                {"en": "I wanna be where the people are; I wanna see, wanna see 'em dancin'.", "cn": "我多么渴望能亲自踏足前往那片人类熙熙攘攘群居的陆地故土；我渴望能亲眼端详、亲眼目睹他们在月光之下纵情曼妙起舞的身姿！"},
                {"en": "Walking around on those, what do you call 'em? Oh, feet!", "cn": "踩着那两根神奇支撑身躯的骨肉支柱漫步街头，人们管那玩意儿叫什么来着？——噢对了，是双脚！"},
                {"en": "Flippin' your fins, you don't get too far; legs are required for jumpin', dancin'.", "cn": "整天无休止地扑棱着滑腻冰冷的鱼尾鳍，你在海浪深处根本远行不了多远；唯有拥有一双真正的人类双腿，才能畅快淋漓地欢快蹦跳、旋转起舞！"},
                {"en": "Strollin' along down a, what's that word again? Street!", "cn": "手挽着手悠然自得漫步徜徉在那条开阔平坦的通途之上，那个词儿叫什么来着？——街道！"},
                {"en": "Up where they walk, up where they run, up where they stay all day in the sun.", "cn": "在那个高悬于海浪之上的向阳世界里，人们在清风中并肩漫步，人们在草甸上欢畅奔跑，人们整日整夜尽情沐浴在金灿灿的温暖日光之中！"},
                {"en": "Wanderin' free, wish I could be part of that world.", "cn": "无拘无束、自由自在地穿行于天地日月之间，我多么卑微而炽热地企盼着：有朝一日，我也能成为那个鲜活世界里的一部分！"},
                {"en": "What would I give if I could live out of these waters? What would I pay to spend a day warm on the sand?", "cn": "倘若真能让我跳脱挣脱出这片冰冷刺骨的海水牢笼，哪怕倾尽我所有的青春与歌喉我又有何吝惜？只要能换来在滚烫温软的沙滩上惬意沉睡一天，我愿付出任何沉痛代价！"},
                {"en": "Bet'cha on land they understand, bet they don't reprimand their daughters.", "cn": "我敢赌咒发誓，陆地上的人类必定心智开明通达事理，他们绝不会像海皇父亲那样成天无休止训斥压制女儿对探索未知的纯真渴望！"},
                {"en": "Bright young women, sick of swimmin', ready to stand; I want to be part of your world!", "cn": "一位朝气蓬勃、心智觉醒的聪慧少女，早已彻底厌倦了在暗无天日的海底徒劳游弋；她早已做好了昂首挺胸挺立在大地之上的万全准备——我渴望成为属于你的那个世界的一部分！"}
            ]
        },
        {
            "title": "第 7 首 · 泰山 · You'll Be in My Heart 你永驻我心",
            "description": "菲尔·柯林斯奥斯卡金奖摇滚抒情，大猩猩母亲抚育人类弃儿的跨物种大爱。",
            "sentences": [
                {"en": "Come stop your crying, it will be all right; just take my hand, hold it tight.", "cn": "来吧我的小宝贝，快擦干你惊恐的泪水，一切都会化险为夷好起来的；握紧我的手掌，紧紧抓住不要放开。"},
                {"en": "I will protect you from all around you; I will be here, don't you cry.", "cn": "我必将化作铜墙铁壁誓死捍卫你的周全，替你阻挡周遭丛林里所有的凶禽猛兽；有我在此守护，别哭了孩子。"},
                {"en": "For one so small, you seem so strong; my arms will hold you, keep you safe and warm.", "cn": "对于一个如此娇小玲珑的脆弱小生灵而言，你骨子里展现出的顽强生命力却显得何其坚韧英勇；我的双臂将紧紧将你拥入怀中，护你一生平安温暖。"},
                {"en": "This bond between us can't be broken; I will be here, don't you cry.", "cn": "我们母子之间因缘际会铸就的这道神圣血脉灵魂羁绊，这世间任何强权与猛兽皆休想将其斩断撕碎；我始终在身侧守候，别怕别哭。"},
                {"en": "Cause you'll be in my heart; yes, you'll be in my heart from this day on, now and forever more.", "cn": "只因从此时此刻这神圣的一秒钟起，你便将永远驻留在我的心房正中央；没错，从今往后直到世界的尽头，你永生永世驻我心间！"},
                {"en": "You'll be in my heart, no matter what they say; you'll be here in my heart, always.", "cn": "你将永远是我心头至高无上的珍宝，不论部落族群里的冷嘲热讽与非议怎么说；你将永远端坐在我滚烫的心灵神殿深处，至死不渝！"},
                {"en": "Why can't they understand the way we feel? They just don't trust what they can't explain.", "cn": "族人们究竟为何就是无法理解包容我们之间纯粹无瑕的情感？那些顽固之辈，不过只是本能地恐惧排斥他们认知局限所无法解释的神圣奇迹罢了！"},
                {"en": "I know we're different, but deep inside us we're not that different at all.", "cn": "我当然清清楚楚知道你我物种相貌大相径庭，但在我们跳动的胸膛皮囊深处，那一颗懂得爱与被爱的心脏其实根本毫无二致！"},
                {"en": "And you'll be in my heart, yes, you'll be in my heart from this day on, now and forever more.", "cn": "你将永远是我生命中最神圣的骨肉牵挂，从今往后风雨同舟，今生今世万古长青。"},
                {"en": "Don't listen to them, cause what do they know? We need each other, to have, to hold.", "cn": "把那些自私排外的闲言碎语当成耳旁穿堂风吧，他们那点狭隘的见识懂得什么世间真爱！我们需要彼此相濡以沫，在这浩瀚天地间执手相拥。"},
                {"en": "They'll see in time, I know; we'll show them together, because a mother's devotion defies biology.", "cn": "在漫长岁月流转之中他们终将看清真相；我们将携手向全世界证明：一位母亲超越物种界限的炽热奉献，足以改写自然生物学的教条界限！"},
                {"en": "Phil Collins composed the rhythm track with dynamic Afro-pop polyrhythms and power ballad drumming.", "cn": "菲尔·柯林斯巧妙地将激昂澎湃的非洲流行复调节奏鼓点，与排山倒海般充满力量张力的重型摇滚情歌鼓浪浑然天成熔铸于一炉。"},
                {"en": "When destiny calls you, you must be strong; I may not be with you, but you gotta hold on.", "cn": "当属于你真正的人生成长天命召唤你时，你必须学会独自挺直脊梁变得顶天立地；有朝一日我或许无法继续陪你前行，但你务必坚强挺住！"},
                {"en": "They'll see, I know; we'll show them together.", "cn": "那些昔日质疑冷笑的看客终将心悦诚服；我们将并肩用时间向整座荒野丛林展现奇迹。"},
                {"en": "Always, from this day on, now and forever more, you'll be in my heart; always beside you.", "cn": "永远永远，自今日黎明起直至时间尽头，你永驻我心，而我的祝福守护，将如影随形一生常伴！"}
            ]
        },
        {
            "title": "第 8 首 · 寻梦环游记 · Remember Me 请记住我",
            "description": "埃克托弹着吉他写给女儿可可的摇篮曲，死亡不是终点，遗忘才是。",
            "sentences": [
                {"en": "Remember me, though I have to say goodbye; remember me, don't let it make you cry.", "cn": "请永远记住我，虽然此时此刻我不得不含泪同你挥手道别；请深情记住我，绝不要任凭离别的感伤让你眼眶泛起泪花。"},
                {"en": "For even if I'm far away, I hold you in my heart; I sing a secret song to you each night we are apart.", "cn": "因为哪怕未来我远行流浪在天涯海角的遥远异邦，我依然会将你深情珍藏在我心房最柔软处；在每一个与你分离的清冷漫漫长夜，我都会在心底为你哼唱这支专属的摇篮曲。"},
                {"en": "Remember me, though I have to travel far; remember me each time you hear a sad guitar.", "cn": "请一定记住我，纵使我身负宿命不得不远渡重洋跋涉万里；每当你耳畔再次悠扬回荡起略带感伤的吉他琴弦轻拨，就请在心头再次深情忆起我的容颜。"},
                {"en": "Know that I'm with you the only way that I can be, until you're in my arms again, remember me.", "cn": "请务必坚信：我始终在用我所能企及的唯一神圣方式——化作春风细雨长相陪伴在你身侧，直到在未来的某一天你重新扑入我的怀抱，请永远记住我！"},
                {"en": "The lullaby transforms from a father's intimate bedroom blessing into a stadium-sized anthem of remembrance.", "cn": "这首质朴的摇篮曲，从一位平凡父亲在床榻前对幼女附耳低语的温存祝福，最终奇迹般蜕变升华成了一曲响彻阴阳两界、震撼寰宇的旷世追思赞歌。"},
                {"en": "Physical death is merely the departure of the breath; the second, ultimate death occurs when the last living soul forgets your name.", "cn": "肉体的心跳骤停不过只是区区血肉皮囊的吐气离世；而宇宙间真正残忍至极的终极死亡，是当这世间最后一位深爱你的活人彻底从记忆中抹去了你的姓名。"},
                {"en": "Miguel sang through his tears to his great-grandmother Coco, awakening her fading dementia with the melody of love.", "cn": "小米格尔抱着斑驳的古董木吉他满含热泪深情呼唤歌唱，奇迹般用这支刻骨铭心的爱之旋律，彻底唤醒了曾祖母可可阿兹海默症那片行将枯萎的记忆荒原。"},
                {"en": "Her cloudy, cataract-covered eyes suddenly ignited with recognition, softly singing along with her long-lost papa.", "cn": "老太太那双早已浑浊无光的白内障眼眸深处，刹那间重新点燃了相认的璀璨神采，颤颤巍巍跟着节拍，轻声同合唱着阔别了整整一个世纪的亲生父亲当年的歌谣。"},
                {"en": "Memory is the sacred golden thread that ties the living to the ancestors across the marigold bridge.", "cn": "血浓于水的记忆，正是一根将阳间生者与黄泉先祖牢牢紧系贯通的神圣黄金丝线，在万寿菊铺就的流光拱桥之上搭建起永恒的精神沟通要道。"},
                {"en": "No one is truly gone as long as their story is retold with warmth around the holiday table.", "cn": "只要一个人的生平传奇与温存音容依然被后辈家人围坐在节日烛光餐桌前深情传颂，他便在这世间从未真正离去分毫！"},
                {"en": "Héctor's tragic murder by a jealous partner was erased, restored to his rightful place of honor.", "cn": "埃克托当年惨遭嫉贤妒能的恶毒搭档下毒谋杀的百年沉冤终得昭雪平反，这位伟大的音乐宗师终于在家族宗祠祠堂里夺回了他名垂青史的神圣尊荣。"},
                {"en": "Sing it with tenderness; love is the only currency that retains its value in the afterlife.", "cn": "满怀着至纯的温存轻声慢唱吧；因为唯有大爱，才是这大千世界万千财富中唯一一种能在死后世界依然熠熠生辉、保值万世的神圣硬通货！"},
                {"en": "Until you're in my arms again, remember me; our souls are bound by an everlasting melody.", "cn": "直到未来你我再次在繁星花海之畔紧紧相拥的那一刻，请永远记住我；我们的灵魂，早已被这首永不落幕的仙乐神曲紧紧捆绑融为一体。"},
                {"en": "The marigold petals shimmer in the candle glow, welcoming our loved ones home for one precious night.", "cn": "万寿菊鲜艳金黄的花瓣在摇曳跳动的烛光之中闪烁生辉，温情指引迎接我们逝去已久的挚爱亲朋，在这难能可贵的一夜重返人间故里。"},
                {"en": "Remember me; let love echo through the generations like an everlasting symphony.", "cn": "请永远记住我；让这人世间至纯至善的大爱，如同一曲永不落幕的宏伟交响乐章般，世代激荡回响！"}
            ]
        },
        {
            "title": "第 9 首 · 玩具总动员 · You've Got a Friend in Me 挚友同行",
            "description": "兰迪·纽曼经典乡村布鲁斯，牛仔胡迪与巴斯光年跨越二十年的神仙友谊。",
            "sentences": [
                {"en": "You've got a friend in me; you've got a friend in me.", "cn": "你始终拥有我这个肝胆相照的莫逆挚友；无论何时何地，我都是你最坚实靠谱的知心朋友！"},
                {"en": "When the road looks rough ahead, and you're miles and miles from your nice warm bed.", "cn": "每当前方的人生漫漫长路显得如此坎坷崎岖泥泞，而你距离自己温暖舒适的床榻还有千里万里之遥。"},
                {"en": "You just remember what your old pal said: Boy, you've got a friend in me.", "cn": "你只要在心头牢牢忆起老伙计对你许下的郑重诺言：小子，只要有我在，你就永远拥有一个至死不渝的患难挚友！"},
                {"en": "Yeah, you've got a friend in me, through thick and thin.", "cn": "没错！无论遭遇顺境狂欢还是逆境磨难，我都甘愿陪你同甘共苦、休戚与共到底！"},
                {"en": "You've got troubles, and I've got 'em too; there isn't nothing I wouldn't do for you.", "cn": "你身陷泥潭烦恼缠身，而我头上也同样顶着数不清的麻烦；但只要你开口，这世上就没有哪一件为你两肋插刀的事是老子不愿去办的！"},
                {"en": "We stick together and we see it through, cause you've got a friend in me.", "cn": "咱们俩紧紧抱团扎在一处，誓要把所有坎坷风雨硬生生踩在脚下熬出头，只因老子生来就是你一辈子的挚友！"},
                {"en": "Some other folks might be a little bit smarter than I am, bigger and stronger too, maybe.", "cn": "这世上别的大块头或许个顶个在智商上比我这破牛仔要精明伶俐得多，或许身板比我更魁梧健硕、力大无穷。"},
                {"en": "But none of them will ever love you the way I do, it's me and you, boy.", "cn": "但放眼天下芸芸众生，却绝没有哪一个人能够如同老子这般毫无保留、全心全意深爱着你；并肩看淡人世风云的，从始至终唯独只有你和我，好兄弟！"},
                {"en": "And as the years go by, our friendship will never die.", "cn": "哪怕岁月无情如白驹过隙般飞速流逝、青葱少年终将长大成人，我们之间历经烈火淬炼的兄弟情谊也绝不会磨灭消亡！"},
                {"en": "You're gonna see it's our destiny: you've got a friend in me.", "cn": "你终将亲眼见证这是冥冥之中命运为我们铸就的神圣天命：你的一生，永远有我这个生死相随的挚友同行！"},
                {"en": "Randy Newman's ragtime piano stride and gravelly vocals deliver pure American nostalgia.", "cn": "兰迪·纽曼那标志性的拉格泰姆爵士大跨度钢琴步法与略带沧桑沙哑的慵懒质朴烟嗓，近乎无可挑剔地传递出了纯正美式情怀的纯真乡愁。"},
                {"en": "Andy writing his name in permanent marker under Woody's boot created an unbreakable covenant.", "cn": "当年幼小的小主人安迪用永远擦不掉的黑色马克笔在胡迪牛仔长靴鞋底工工整整写下自己大名的一刻，便缔结下了一道不可违背的神圣终身契约。"},
                {"en": "To the world you might just be a plaything, but to a child you are a living anchor of imagination.", "cn": "放眼冰冷功利的人世间，你或许不过只是一只由廉价塑料与棉花缝制的流水线玩偶；但在一个纯真孩子的眼中，你却是一尊承载浩瀚奇思妙想的鲜活精神灯塔！"},
                {"en": "So long, partner, Woody whispered as Andy drove away to university, letting go with grace.", "cn": "再会了，老搭档！当长大成人的安迪驾车驶向大学校园远去时，胡迪站在门廊长椅上摘下牛仔帽轻声温言道别，展现出了从容放手的至高博大境界。"},
                {"en": "You've got a friend in me; true loyalty asks for no possession, only the joy of standing guard.", "cn": "你始终拥有我这个莫逆挚友；世间最纯粹崇高的忠诚从来不奢求自私占有，而仅仅只在于能有幸伫立身侧默默为你镇守一生的无上欣慰！"}
            ]
        },
        {
            "title": "第 10 首 · 木偶奇遇记 · When You Wish Upon a Star 愿望成真之星",
            "description": "迪士尼标志性开场城堡片头曲，向夜空最亮的星辰许下最虔诚的愿望。",
            "sentences": [
                {"en": "When you wish upon a star, makes no difference who you are.", "cn": "当你怀揣一颗纯真虔诚的心，向着夜空中最耀眼的璀璨星辰许下深切心愿时；无论你出身贫贱富贵、不论你身居何种凡尘境遇，皆毫无任何分别。"},
                {"en": "Anything your heart desires will come to you.", "cn": "只要是你灵魂深处真正渴求向往的崇高梦想，终有一天都将奇迹般如约降临到你的身侧！"},
                {"en": "If your heart is in your dream, no request is too extreme.", "cn": "只要你的全副身心与炽热灵魂彻底倾注融入你的梦想之中，这世间便绝没有任何夙愿会显得过于遥不可及、狂妄苛刻！"},
                {"en": "When you wish upon a star, as dreamers do.", "cn": "只要像普天下所有执着孤勇的真正梦想家那样，虔诚仰望星空，许下你最纯粹的誓言！"},
                {"en": "Fate is kind; she brings to those who love the sweet fulfillment of their secret longing.", "cn": "上苍的命运之神向来是仁慈宽厚的；她必将慷慨惠赐给那些心中怀揣至纯大爱之人，以如愿以偿实现心底隐秘夙愿的甘甜圆满奖赏！"},
                {"en": "Like a bolt out of the blue, fate steps in and sees you through.", "cn": "宛如万里晴空之中骤然划过的一道神圣奇迹霹雳，命运之神便会从容降临人间，一路引领守护你踏碎荆棘度过万难！"},
                {"en": "When you wish upon a star, your dreams come true.", "cn": "只要你满怀信念向着那颗神圣之星由衷许愿，你所有的绚烂梦想终将化作现实的奇迹！"},
                {"en": "This composition became the quintessential musical signature for the entire Walt Disney Company.", "cn": "这首空灵圣洁的传世乐章，最终毫无争议地当选成为了整个华特迪士尼造梦帝国在全球观众心目中无可替代的标志性音乐徽章名片！"},
                {"en": "Cliff Edwards' gentle falsetto as Jiminy Cricket gave voice to humanity's yearning for guidance.", "cn": "克里夫·爱德华兹为小蟋蟀吉米尼配音所献唱的轻柔空灵假音唱腔，近乎天籁般道尽了全人类在迷茫尘世中苦苦渴求良知明灯指引的心灵呐喊。"},
                {"en": "A wooden puppet with strings can become a real, breathing boy through honesty, courage, and unselfishness.", "cn": "哪怕只是一个被无形丝线操纵摆布的卑微提线木偶，只要他能在诱惑磨难中学会恪守诚实守信、勇敢抗争与无私大爱，便终能蜕变成一个顶天立地的真正血肉好男儿！"},
                {"en": "The twinkling chimes introduce the iconic Cinderella Castle silhouette before every Disney feature.", "cn": "在每一部迪士尼经典大片银幕亮起的最开端，那串如梦似幻、流光溢彩的清脆星光风铃声，总会伴着仙德瑞拉童话城堡的宏伟剪影如约而至。"},
                {"en": "Never extinguish the child of wonder residing deep within the chambers of your adult cynicism.", "cn": "永远绝不要亲手掐灭那个在你日渐世俗老练、充满犬儒怀疑的成人躯壳深处，依然对这大千世界满怀天真好奇与敬畏的纯真孩童！"},
                {"en": "Hope is the metaphysical anchor that holds the human spirit steady amidst turbulent celestial storms.", "cn": "对未来的无限希望，乃是维系人类崇高精神在狂暴动荡的凡尘惊涛骇浪中始终锚定不翻船的终极形而上神圣锚链！"},
                {"en": "When you wish upon a star, makes no difference who you are; your dreams come true.", "cn": "向着那颗神圣的指路明灯许下你的宏伟夙愿吧，苍天面前人人平等；只要笃定前行，你所有的梦想，终将在这壮丽的人间如愿以偿！"},
                {"en": "Believe in the magic of your own resilience, and the universe will align to pave your way.", "cn": "深信你自己体内蕴藏的百折不挠坚韧魔法奇迹吧，冥冥之中整个宇宙的繁星轨迹，皆将为你俯首让道、铺就锦绣前程！"}
            ]
        }
    ]))

    return courses
