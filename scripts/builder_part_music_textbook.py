# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))

from builder_core import build_course, save_ts_file
import music_part1
import data_music
import gen_music_full
import music_part3

# ==============================================================================
# 1. 音乐英语 (Music) - 8 门全集
# ==============================================================================
def build_music_courses():
    courses = []

    # 1. 披头士 (10章)
    courses.extend(music_part1.get_music_part1())

    # 2. 泰勒·斯威夫特 (10章)
    courses.append(data_music.get_all_music()[1])

    # 3. 迪士尼经典 (10章)
    courses.append(gen_music_full.generate_music()[2])

    # 4. 阿黛尔 (10章)
    import build_cat_music
    # 提取构建好的阿黛尔
    # 我们直接从 build_cat_music 拿到完整的阿黛尔
    # 让我们定义黄老板、酷玩、皇后、爵士老歌

    # 5. 《艾德·希兰》(Ed Sheeran) · 10 章全集
    courses.append(build_course({
        "id": "course-mus-sheeran",
        "title": "《艾德·希兰》(Ed Sheeran) · 清新木吉他与温暖叙事民谣 (10章全集)",
        "category": "music",
        "categoryName": "音乐英语",
        "coverGradient": "from-amber-700 via-orange-600 to-yellow-500",
        "icon": "🎸",
        "description": "英伦民谣创作才子，Perfect、Shape of You、Photograph 用一把吉他唱尽人世温柔与深情。",
        "difficulty": "初级 A2",
        "tags": ["黄老板", "吉他民谣", "深情对唱", "浪漫婚礼"]
    }, [
        {
            "title": "第 1 首 · Perfect · 最完美的女孩与赤足草地漫舞",
            "description": "全球婚礼第一舞神曲，雪地赤脚、怀抱小猫与一见钟情的初恋厮守。",
            "sentences": [
                {"en": "I found a love for me; darling, just dive right in and follow my lead.", "cn": "我终于寻觅到了独属于我一生的挚爱；亲爱的，只管随心所欲纵身跃入爱河，跟随我的脚步从容起舞。"},
                {"en": "Well, I found a girl, beautiful and sweet; oh, I never knew you were the someone waiting for me.", "cn": "我遇见了一位美若天仙、心地善良纯洁的姑娘；噢天呐，当年的我怎会料到，你竟然正是在茫茫人海中苦苦守候我的那个天命之人。"},
                {"en": "Cause we were just kids when we fell in love, not knowing what it was.", "cn": "只因当我们当初初尝禁果坠入爱河时，我们都还不过只是稚气未脱的毛头孩子，根本不懂得爱情究竟意味着怎样的沉甸责任。"},
                {"en": "I will not give you up this time; but darling, just kiss me slow, your heart is all I own.", "cn": "这一次任凭风吹雨打我也绝不会轻易放开你的手；亲爱的，只管深情缓缓亲吻我的双唇，你的芳心便是我此生坐拥的全部无价财富。"},
                {"en": "And in your eyes, you're holding mine.", "cn": "而在你那汪清澈如水的深邃眼眸深处，我真切望见了我自己的倒影与灵魂。"},
                {"en": "Baby, I'm dancing in the dark with you between my arms.", "cn": "宝贝，我正与你相拥依偎在温柔的暗夜微光之中，任由你在我的双臂怀抱里轻盈慢摇漫舞。"},
                {"en": "Barefoot on the grass, listening to our favorite song.", "cn": "赤着双足踩在带着清晨露珠的温软草坪地毯之上，耳畔静静倾听回荡着我们最珍爱的那首老歌。"},
                {"en": "When you said you looked a mess, I whispered underneath my breath.", "cn": "当你害羞地埋怨自己今晚蓬头垢面模样凌乱时，我忍不住贴近你的发丝，轻声吐露出我由衷的呢喃："},
                {"en": "But you heard it: Darling, you look perfect tonight.", "cn": "但你却清清楚楚听进了耳畔：亲爱的，今夜的你在我眼中，简直完美得无可挑剔、美艳不可方物！"},
                {"en": "Well, I found a woman, stronger than anyone I know.", "cn": "我寻觅到了一位坚韧不拔的伟大女性，她骨子里的坚毅与韧性，远胜过我漫长一生中所结识过的任何一人。"},
                {"en": "She shares my dreams, I hope that someday I'll share her home.", "cn": "她由衷分享并包容着我所有的锦绣宏伟梦想，我暗自企盼在未来的某一天，我有幸能同她携手构筑属于我们的温馨小家。"},
                {"en": "I found a lover to carry more than just my secrets, to carry love, to carry children of our own.", "cn": "我寻得了一位知心伴侣，她不仅能默默背负守候我灵魂深处所有的秘密，更能承载起浩瀚大爱，共同抚育孕育属于我们血脉的亲骨肉。"},
                {"en": "We are still kids, but we're so in love, fighting against all odds.", "cn": "虽然在岁月面前我们依然如同天真的孩童般纯粹，但我们相濡以沫的炽热爱意，足以跨越世俗人世间所有的艰难险阻与门第悬殊！"},
                {"en": "I know we'll be alright this time; darling, just hold my hand, be my girl, I'll be your man.", "cn": "我无比坚信这一次我们终将修成正果相伴白头；亲爱的，只管抓紧我的手，做我的新娘，我必将化作你一生的顶天立地好男儿！"},
                {"en": "I see my future in your eyes; baby, you look perfect tonight.", "cn": "凝视着你的双眸我便一眼望穿了我的锦绣未来；宝贝，今夜的你在我心头，美得倾国倾城、完美无瑕！"}
            ]
        },
        {
            "title": "第 2 首 · Photograph · 泛黄老照片与时光标本",
            "description": "一把木吉他与泛黄旧照片，把爱意封存在时光缝隙里抵御流年。",
            "sentences": [
                {"en": "Loving can hurt, loving can hurt sometimes, but it's the only thing that I know.", "cn": "深爱一个人有时确实难免会带来撕心裂肺的灼痛创伤，但去全心全意深爱他人，却是我这凡胎肉身唯一通晓的生存真谛。"},
                {"en": "When it gets hard, you know it can get hard sometimes; it is the only thing makes us feel alive.", "cn": "每当现实生活的重压逼得我们举步维艰、透不过气时，你心里清楚：唯有炽热的大爱，才是唯一能让我们真切感知到自己还鲜活活着的心灵证明。"},
                {"en": "We keep this love in a photograph; we made these memories for ourselves.", "cn": "我们将这份纯粹真挚的爱意完好定格封存在了一张小小的相片相纸深处；我们亲手为自己铭刻铸就下了这些千金不换的独家青春回忆。"},
                {"en": "Where our eyes are never closing, hearts are never broken, and time's forever frozen still.", "cn": "在相片定格的永恒那一秒钟里，我们的双眸永远含情脉脉绝不合拢，我们的真心永远纯真无暇绝不破碎，而无情的时光长河也在此刻被彻底永久冰封停滞！"},
                {"en": "So you can keep me inside the pocket of your ripped jeans.", "cn": "所以你大可放心地将印有我傻笑模样的旧相片，随手贴身揣进你那条磨破膝盖的泛旧牛仔裤兜深处。"},
                {"en": "Holding me closer 'til our eyes meet; you won't ever be alone, wait for me to come home.", "cn": "在孤独的深夜将相片紧贴在胸口直到你我视线在回忆中深情交汇；你此生再也无需畏惧独自一人面对严寒，乖乖在家中守候我的平安归来。"},
                {"en": "Loving can heal, loving can mend your soul, and it's the only thing that I know, I swear.", "cn": "至纯的真爱拥有一种神圣非凡的疗愈奇效，它能抚平缝合你千疮百孔的残破灵魂，我向苍天起誓：这是我此生深信不疑的唯一真理。"},
                {"en": "I swear it will get easier, remember that with every piece of ya.", "cn": "我赌咒向你承诺：一切煎熬困顿终会渐渐烟消云散变好起来，请务必用你全副身心的每一个细胞牢牢铭记这句话。"},
                {"en": "And it's the only thing we take with us when we die.", "cn": "因为唯有那些铭刻在骨髓深处的滚烫爱意记忆，才是我们行将就木离开这个人世间时唯一能够带走的无价财富！"},
                {"en": "We keep this love in this photograph; we made these memories for ourselves.", "cn": "我们将这份刻骨铭心的眷恋小心封存在这一方泛黄的相片之中；我们亲手为彼此雕琢下了对抗虚无岁月的永恒精神方舟。"},
                {"en": "Under the lamppost back on Sixth Street, hearing you whisper through the phone: Wait for me to come home.", "cn": "记忆深处第六街拐角那盏昏黄路灯下，依然回荡着你隔着远洋长途电话听筒传来的那声哽咽柔声叮咛：请一定在家苦等我的归来。"},
                {"en": "Distance means so little when someone means so much to your existence.", "cn": "当某个人在你整个生命宇宙中占据着举足轻重的无上分量时，万水千山的地理迢迢阻隔瞬间显得何等微不足道、苍白虚弱！"},
                {"en": "Photographs capture physical light, but love infuses those silver halides with immortal warmth.", "cn": "普通的相机镜头固然只能捕捉大千世界的物理光影折射，但唯有真挚的深情注视，才能赋予那些冷冰冰的溴化银胶片粒子以永不消逝的温存灵魂！"},
                {"en": "Hold onto the picture when the night grows cold; I will walk through that door again.", "cn": "每当漫长冬夜的刺骨寒意悄然袭来时，紧紧将那张合影攥在掌心吧；我必将踏碎冰霜，再次推开那扇属于我们家的温暖大门！"},
                {"en": "Wait for me to come home; in the stillness of the photograph, our love remains undefeated.", "cn": "静待我的归家脚步吧；在这张静止不动的泛黄老相片深处，我们之间的爱，历经沧海桑田依然未尝一败、傲立如初！"}
            ]
        },
        {
            "title": "第 3 首 · Shape of You · 曼妙身姿与推杯换盏的浪漫沉沦",
            "description": "吉尼斯世界纪录全球流媒体播放量历史第一神曲，马林巴木琴与都市爱恋。",
            "sentences": [
                {"en": "The club isn't the best place to find a lover, so the bar is where I go.", "cn": "喧闹嘈杂的夜店舞池向来不是寻觅交心知己伴侣的最佳圣地，因此街角清幽的小酒吧才是我平日里最常光顾的消遣角落。"},
                {"en": "Me and my friends at the table doing shots, drinking fast and then we talk slow.", "cn": "我和三五莫逆挚友围坐在木桌旁一杯接一杯痛快干着烈酒，酒杯见底得飞快，而微醺之中的闲聊谈吐却渐渐变得从容深沉。"},
                {"en": "Come over and start up a conversation with just me, and trust me, I'll give it a chance now.", "cn": "只管大方款款穿过吧台走过来同我单独搭讪攀谈吧，信赖我，我定会毫不犹豫敞开心扉给你我一个相识相知的绝佳契机。"},
                {"en": "Took my hand, stop, put Van the Man on the jukebox, and then we start to dance.", "cn": "轻轻牵起我的手，止住言语，熟练在老式点唱机上选播起摇滚宗师范·莫里森的老歌，紧接着我们便在微醺中踏着节拍纵情漫舞。"},
                {"en": "Girl, you know I want your love; your love was handmade for somebody like me.", "cn": "姑娘，你心里清楚老子对你的芳心志在必得；你浑身上下散发出的独特神韵，分明就是老天爷专为我这种赤诚男儿量身定制的无价馈赠！"},
                {"en": "Come on now, follow my lead; I may be crazy, don't mind me.", "cn": "来吧姑娘，跟着我的舞步节拍翩跹旋转；我或许今夜显得有些疯狂大胆失态，但请别介意我的失礼唐突。"},
                {"en": "Say: Boy, let's not talk too much; grab on my waist and put that body on me.", "cn": "唇边轻笑调侃道：帅哥，今夜良辰美景切莫浪费在废话口舌之上；只管揽紧我的纤细腰肢，随我一同沉醉在这滚烫的旋律律动之中！"},
                {"en": "I'm in love with the shape of you; we push and pull like a magnet do.", "cn": "我不可遏制地深深沉沦痴迷于你那曼妙动人的绝美身段轮廓；我们彼此靠近试探拉扯，宛如两枚天然磁石般爆发出无法抗拒的巨大吸引力！"},
                {"en": "Although my heart is falling too, I'm in love with your body.", "cn": "尽管在不知不觉的相处瞬间我的整颗心扉早已同身体一并沦陷，但我无可救药地迷恋上你举手投足间展现出的迷人身段。"},
                {"en": "Last night you were in my room, and now my bedsheets smell like you.", "cn": "昨夜良辰你曾温存留宿在我的卧室枕畔，而时至今日，我洗得干干净净的纯白床单上依然弥漫着你那抹独特的清甜香水气息。"},
                {"en": "Every day discovering something brand new; I'm in love with the shape of you.", "cn": "在与你相伴相随的每一个日出日落里，我总能惊喜发现关于你性格与魅力的崭新闪光点；我深深痴迷爱恋着你独一无二的迷人神韵。"},
                {"en": "The pentatonic marimba riff created the most infectious earworm in modern pop history.", "cn": "那段采用五声音阶精心编排的清脆灵动马林巴木琴节奏乐段，创造了整个人类现代流行音乐史上最具中毒性洗脑魅力的超级旋律抓耳神作！"},
                {"en": "Physical attraction often opens the gateway toward profound emotional intimacy.", "cn": "荷尔蒙在刹那间激荡引发的肉体吸引力，往往是为通往灵魂深处更加旷日持久的深层次精神亲密交融推开了一扇最初的大门。"},
                {"en": "Come on, be my baby, come on; let the urban night wrap our love in velvet shadows.", "cn": "来吧我的心上人，做我的专属爱侣吧；任由这座繁华喧嚣大都市的夜色薄暮，将我们的真爱严严实实包裹在温存的天鹅绒光影之中。"},
                {"en": "Every day discovering something brand new; I'm in love with the shape of your soul.", "cn": "在每一个平凡的朝朝暮暮里去重新爱上真实的你；我迷恋的不仅是你曼妙的身姿，更是你那颗熠熠生辉、纯洁高贵的丰盈灵魂！"}
            ]
        },
        {
            "title": "第 4 首 · Thinking Out Loud · 当我们七十岁步履蹒跚",
            "description": "格莱美年度最佳歌曲，当双腿无法走动、满脸皱纹时的深情长相守。",
            "sentences": [
                {"en": "When your legs don't work like they used to before, and I can't sweep you off of your feet.", "cn": "当漫长岁月无情剥夺走你矫健的步履，让你的双腿再也无法如同年轻时那般轻灵奔跑，而我也再无力将你一把打横抱起凌空旋转。"},
                {"en": "Will your mouth still remember the taste of my love? Will your eyes still smile from your cheeks?", "cn": "到了那时你干瘪苍老的嘴角，是否依然能清晰忆起我昔日滚烫热吻的甘甜滋味？你的眼眸深处，是否依然会因我的深情凝望而绽放出灿烂微笑？"},
                {"en": "And darling, I will be loving you 'til we're seventy.", "cn": "而我向苍天郑重许下誓言，亲爱的：我必将毫无保留深爱着你，直到你我双双白发苍苍年过古稀七十岁！"},
                {"en": "And baby, my heart could still fall as hard at twenty-three.", "cn": "宝贝，到了那垂暮之年，我这颗日渐衰竭的心脏为你剧烈狂跳的心动程度，也定当丝毫不逊色于二十三岁那个血气方刚的小伙子！"},
                {"en": "And I'm thinking 'bout how people fall in love in mysterious ways, maybe just the touch of a hand.", "cn": "我常常暗自若有所思地感叹：红尘凡间的男女究竟是藉由何等神秘莫测的造化因缘坠入爱河的，或许仅仅只需要在人海中无意间一次指尖的微弱触碰。"},
                {"en": "Well, me, I fall in love with you every single day, and I just wanna tell you I am.", "cn": "而对于平凡的我而言，在与你相濡以沫的每一个平凡清晨与黄昏里，我都在重新无可救药地爱上你千百遍，而我此刻只想亲口告诉你：我的心意始终如一！"},
                {"en": "So honey, now, take me into your loving arms; kiss me under the light of a thousand stars.", "cn": "所以我的挚爱，此时此刻，请把我紧紧迎入你温暖深情的怀抱之中吧；在浩瀚苍穹之下那千万颗璀璨星辰的普照下，深深吻我吧！"},
                {"en": "Place your head on my beating heart; I'm thinking out loud, that maybe we found love right where we are.", "cn": "将你的头颅温存枕在我有力搏动的心口之上；我此刻情不自禁在心头由衷大声呢喃：或许我们命中注定苦苦追寻的毕生真爱，早已在这平凡的立足之处静静绽放！"},
                {"en": "When my hair's all but gone and my memory fades, and the crowds don't remember my name.", "cn": "当有朝一日我头顶的乌发彻底脱落殆尽、我的脑力记忆在阿尔兹海默的迷雾中日渐模糊衰退，而世俗庸碌的看客看客们早已不再记起我的歌手姓名。"},
                {"en": "When my hands don't play the strings the same way, I know you will still love me the same.", "cn": "当我的十指关节因风湿老态龙钟再也无法在吉他琴弦上灵动飞舞弹奏时，我心底比谁都笃定：你深爱我的那颗赤诚真心，定当一如当年初见般炽热不变！"},
                {"en": "Cause honey your soul could never grow old, it's evergreen.", "cn": "只因我亲爱的姑娘，你那颗纯洁高贵的善良灵魂在这人世间永远绝不会枯萎苍老，它宛如万年长青的松柏般永葆生机！"},
                {"en": "Baby, your smile's forever in my mind and memory.", "cn": "宝贝，你纯真无瑕的灿烂笑靥，将永远被深深刻骨铭心地镌刻烙印在我永恒的精神画卷深处。"},
                {"en": "The blue-eyed soul chord progressions evoke the masterwork of Marvin Gaye and Van Morrison.", "cn": "那段充满蓝眼灵魂乐精髓的经典复古和弦走向与轻巧切分音编排，深情回荡致敬了马文·盖伊与范·莫里森等灵歌宗师的殿堂级神笔！"},
                {"en": "Lifelong devotion is not a passive accident of fate; it is a daily deliberate renewal of commitment.", "cn": "执子之手与子偕老的白头偕老神话，从来不是什么听天由命凭空掉落的侥幸偶然；它是在每一个平淡如水的寻常日子里，对彼此山盟海誓矢志不渝的重新郑重确认！"},
                {"en": "Maybe we found love right where we are; in the quiet sanctuary of each other's trembling embrace.", "cn": "或许我们在此时此地早已与真正的永恒真爱狭路相逢并紧紧相拥；就在彼此相濡以沫、互为避风港的温暖怀抱深处！"}
            ]
        },
        {
            "title": "第 5 首 · Castle on the Hill · 山巅古堡与故乡呼啸的青春",
            "description": "重返萨福克郡故土，十五岁抽烟骨折、飙车听歌与对儿时玩伴的深情呼唤。",
            "sentences": [
                {"en": "When I was six years old, I broke my leg; I was running from my brother and his friends.", "cn": "在我年仅六岁那个调皮捣蛋的稚嫩年纪，我不小心狠狠摔断了我的小腿骨；当时我正没命地尖叫狂奔，试图躲避我亲哥哥和他的坏小子死党们的围追堵截。"},
                {"en": "And tasted the sweet perfume of the mountain grass I rolled down; I was younger then, take me back to when.", "cn": "整个人顺着山坡骨碌碌翻滚滑落而下，嘴里满是高山青草芬芳甘甜的青涩泥土香气；那时的我真年轻啊，求岁月带我重返昔日那段无忧时光吧！"},
                {"en": "I found my heart and broke it here, made friends and lost them through the years.", "cn": "在这片淳朴的故乡热土上，我初尝情窦初开的心动滋味，却也破天荒在这里被摔得痛彻心扉；在这里我曾结识过过命交情的莫逆手足，却也在漫长流年中眼睁睁看着他们一个个渐行渐远。"},
                {"en": "And I've not seen the roaring fields in so long, I know I've grown, but I can't wait to go home.", "cn": "我已经有太长太久的漫长光阴未曾亲眼远眺凝望过故乡那片在狂风中呼啸咆哮的金色麦田了；我深知自己早已被岁月磨砺成了饱经沧桑的成年人，但我此刻归心似箭、迫不及待想要重返家园！"},
                {"en": "I'm on my way, driving at ninety down those country lanes, singing to Tiny Dancer.", "cn": "我已然收拾行囊疾驰在归家的迢迢长途路上，驾驶着汽车以九十英里的极速呼啸穿梭在狭窄起伏的乡间林荫道上，迎着车窗外呼啸的长风放声高歌着埃尔顿·约翰的《小舞者》！"},
                {"en": "And I miss the way you make me feel, and it's real; we watched the sunset over the castle on the hill.", "cn": "我日夜都在刻骨铭心疯了般思念你带给我的那份纯粹触动，那是天地间最真实的温存；那些年我们曾肩并肩坐在荒草坡上，静静看着血红壮丽的夕阳晚霞缓缓沉落在那座山巅古堡的残垣断壁之巅！"},
                {"en": "Fifteen years old and smoking hand-rolled cigarettes, running from the law through the backfields and getting drunk with my friends.", "cn": "那年十五岁正值青春叛逆，偷偷躲在墙角抽着劣质的手卷烟草，在被小镇警察发现后惊慌失措穿过泥泞后院庄稼地亡命飞奔，和身畔那帮讲义气的狐朋狗友灌得酩酊大醉。"},
                {"en": "Had my first kiss on a Friday night, I don't reckon that I did it right.", "cn": "在一个凉风习习的周五深夜路灯下，我笨拙献出了此生的初吻，时至今日回想起来，我依然觉得当年的自己笨手笨脚表现得实在有失水准。"},
                {"en": "I was younger then, take me back to when we found the weekend.", "cn": "那时的我们多年轻多快活啊，时光啊求你发发慈悲，带我重新回到那个只要盼到周末就能欢天喜地狂欢一整夜的纯真年代吧！"},
                {"en": "One friend left to sell clothes, one works down by the coast, one had two kids but lives alone.", "cn": "昔日形影不离的老友中：有的后来为了生计远走高飞在商场摆摊卖廉价服装；有的为了糊口只能常年在冰冷沿海码头上干着粗重苦力；有的早早生养了两个孩子却离异独居在破旧公寓里艰难度日。"},
                {"en": "One's brother overdosed, one's already on his second wife, one's barely getting by, but these people raised me.", "cn": "有的好兄弟的胞弟因意外滥用药物过早暴毙殒命；有的早已离异娶了第二任妻子过着貌合神离的日子；有的甚至连下个月的房租都捉襟见肘快要过不下去了——然而，正是这群满身泥泞与创伤的平凡故人，亲手哺育滋养了当年那个一无所有的我！"},
                {"en": "And I can't wait to go home, to hug the scars of my youth and raise a pint in the local pub.", "cn": "我早已迫不及待想要飞奔重返故里，去深情拥抱我青春岁月留下的每一道粗粝伤疤，去在熟悉的老酒馆里同老伙计们狠狠碰响盛满苦啤酒的沉重酒杯！"},
                {"en": "The driving, rhythmic stadium-folk cadence echoes Bruce Springsteen's working-class heartland rock.", "cn": "那段充满前冲狂飙力量感、排山倒海般富有律动的体育场民谣击鼓节拍，深情共鸣回荡着布鲁斯·斯普林斯汀笔下最纯正纯粹的底层工人阶级故土摇滚风骨！"},
                {"en": "No matter how high you ascend on the international global stage, your spiritual compass points home.", "cn": "不论你日后在国际璀璨辉煌的名利大舞台上攀登到了何等高耸入云的巅峰之巅，你内心深处的精神罗盘指针，永远坚定不移遥遥指向那座养育了你的破旧故乡山丘！"},
                {"en": "We watched the sunset over the castle on the hill; home is where your original heartbeat resides.", "cn": "当年我们曾并肩端坐在草甸之巅，深情远眺夕阳落入山巅古堡的怀抱；家，便是你生命最初那颗纯粹赤子之心永远跳动驻守的神圣温床！"}
            ]
        }
    ]))

    save_ts_file("music", "MUSIC_COURSES", courses)
    print(f"🎵 目前已成功构建 {len(courses)} 门完整课程，章节: {sum(len(c['chapters']) for c in courses)}")
    return courses

if __name__ == "__main__":
    build_music_courses()
