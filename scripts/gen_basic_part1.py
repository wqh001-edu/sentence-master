# -*- coding: utf-8 -*-
"""
基础学习分类生成器 Part 1:
1. basic-phonetics: 国际音标48发音秘诀 (10章 x 15句 = 150句)
2. basic-1000words: 零基础核心高频1000词造句 (10章 x 15句 = 150句)
3. basic-patterns: 英语五大基本句型大突破 (10章 x 15句 = 150句)
4. basic-tenses: 零基础日常时态速成 (10章 x 15句 = 150句)
共 4 门课程，40 章，600 句。
"""

COURSE_BASIC_PHONETICS = {
    "meta": {
        "id": "basic-phonetics",
        "title": "国际音标48发音秘诀",
        "category": "basic",
        "categoryName": "基础学习",
        "coverGradient": "from-teal-500 to-emerald-700",
        "icon": "🗣️",
        "description": "专为零基础与口语提升学习者打造的 48 国际音标系统突破课，从长短元音对比到清浊辅音咬字，夯实纯正发音基本功。",
        "difficulty": "beginner",
        "tags": ["基础学习", "国际音标", "发音技巧", "口语突破"]
    },
    "chapters": [
        {
            "title": "第1章：长短元音对比 /iː/ 与 /ɪ/",
            "description": "掌握舌位高低与肌肉紧张度，区分 seat 与 sit，feel 与 fill。",
            "sentences": [
                {"en": "Please take a comfortable seat by the window.", "cn": "请坐在靠窗那张舒适的座位上。"},
                {"en": "Sit down quietly and listen to the lecture.", "cn": "安安静静坐下，认真倾听讲座内容。"},
                {"en": "I feel deeply inspired by your wonderful courage.", "cn": "你那超凡的勇气让我深受鼓舞与启发。"},
                {"en": "Fill this glass with clean drinking water, please.", "cn": "请把这个玻璃杯倒满清澈的饮用水。"},
                {"en": "He will lead the team across the high mountain pass.", "cn": "他将带领整个队伍穿过险峻的高山隘口。"},
                {"en": "Keep the heavy iron lid firmly on the cooking pot.", "cn": "把沉重的铁锅盖严严实实盖在锅上。"},
                {"en": "Fresh green tea leaves release a subtle fragrance.", "cn": "新鲜的绿茶嫩叶散发出淡淡幽香。"},
                {"en": "He lives in a charming rural cottage near the lake.", "cn": "他在湖畔一座景色宜人的乡村小木屋里定居。"},
                {"en": "The giant freight ship sails across the calm ocean.", "cn": "巨大的货轮在风平浪静的大洋上破浪前行。"},
                {"en": "A tiny flock of sheep grazed upon the grassy slope.", "cn": "一小群绵羊在青草茵茵的山坡上悠闲吃草。"},
                {"en": "We reached the mountain peak right before sunrise.", "cn": "我们在旭日东升之前准时登上了山峰之巅。"},
                {"en": "Pick fresh ripe apples from the orchard trees.", "cn": "亲手从果园的果树上采摘新鲜成熟的红苹果。"},
                {"en": "Clean teeth every morning to ensure good dental health.", "cn": "每天清晨刷牙清洁牙齿，确保牙齿健康无病。"},
                {"en": "He hit the baseball hard into the outer outfield.", "cn": "他一记重击，将棒球狠狠击打到了外野深处。"},
                {"en": "Accurate vowel length gives clarity to spoken English.", "cn": "精准把控元音的长短时值，赋予英语口语无与伦比的清晰度。"}
            ]
        },
        {
            "title": "第2章：圆唇元音对比 /uː/ 与 /ʊ/",
            "description": "嘴唇收圆与后缩技巧，区分 food 与 foot，fool 与 full。",
            "sentences": [
                {"en": "Nutritious organic food keeps your mind and body active.", "cn": "富含营养的有机食物能让你时刻保持身心充沛活力。"},
                {"en": "Walk forward one step at a time on your own two feet.", "cn": "用你自己的双脚，脚踏实地一步一个脚印向前迈进。"},
                {"en": "Only a fool ignores sound advice from experienced mentors.", "cn": "唯有愚蠢鲁莽之人才会对经验丰富长辈的良策置若罔闻。"},
                {"en": "The library shelf is completely full of classic literature.", "cn": "图书馆的书架上摆满了汗牛充栋的中外传世经典文学。"},
                {"en": "The cool morning breeze refreshed our tired spirits.", "cn": "清晨凉爽怡人的拂面微风，唤醒了我们疲惫的心神。"},
                {"en": "Read an inspiring book before switching off your bedroom lamp.", "cn": "在关掉卧室台灯安歇之前，细心研读一本励志好书。"},
                {"en": "The crescent moon shone bright above the misty valley.", "cn": "一弯明媚的月牙，高悬在薄雾缭绕的山谷上方熠熠生辉。"},
                {"en": "He took off his wet winter boots beside the stone hearth.", "cn": "他在石头壁炉旁脱下了湿漉漉的冬日高筒皮靴。"},
                {"en": "Smooth wooden furniture brings warmth into any living room.", "cn": "光滑温润的实木家具，能为任何一间客厅增添融融暖意。"},
                {"en": "She stood firmly on the platform waiting for the morning train.", "cn": "她稳稳伫立在月台上，静静等候清晨班次的列车进站。"},
                {"en": "Stir the warm vegetable soup slowly with a wooden spoon.", "cn": "用一柄小木勺，慢条斯理地轻轻搅动热气腾腾的蔬菜汤。"},
                {"en": "He pulled the heavy door open to welcome the weary travelers.", "cn": "他奋力拉开厚重的宅门，热情迎接入夜风尘仆仆的旅人。"},
                {"en": "Choose the path that aligns with your highest moral values.", "cn": "勇敢抉择那条与你崇高道德价值观完全契合的宽广坦途。"},
                {"en": "A good habit practiced daily produces extraordinary mastery over time.", "cn": "一个每天躬行践履的好习惯，天长日久必将造就非凡的精湛造诣。"},
                {"en": "Relax your facial muscles when practicing round vowel sounds.", "cn": "在练习圆唇后元音发音时，请保持面部肌肉放松自如。"}
            ]
        },
        {
            "title": "第3章：开口元音对比 /æ/ 与 /e/",
            "description": "下颌开合度与蝴蝶音 /æ/ 突破，区分 bad 与 bed，man 与 men。",
            "sentences": [
                {"en": "Do not let a bad experience discourage your noble ambition.", "cn": "千万不要让一次糟糕挫折的经历，浇灭你心中崇高的抱负。"},
                {"en": "Make your bed neatly as soon as you wake up in the morning.", "cn": "每天清晨一觉醒来，第一时间把自己的床铺收拾平整。"},
                {"en": "A wise man listens carefully before expressing his opinion.", "cn": "一位睿智通达的君子，总是在深思熟虑倾听之后再发表见解。"},
                {"en": "Ten brave men worked together to rebuild the village bridge.", "cn": "十名英勇的汉子齐心协力并肩作战，重建了村庄的断桥。"},
                {"en": "Pack your leather travel bag with all necessary study gear.", "cn": "把你皮质旅行包里装满所有不可或缺的学习必备物品。"},
                {"en": "Beg forgiveness with a sincere and repentant humble heart.", "cn": "怀揣一颗赤诚悔悟的谦卑之心，真诚乞求对方的原谅。"},
                {"en": "He drew a detailed map of the uncharted mountain territory.", "cn": "他亲手绘制了一幅标注详尽的未知崇山峻岭地形图。"},
                {"en": "Set clear, achievable goals for this upcoming study term.", "cn": "为即将到来的这一崭新学期，设定清晰明确可行的小目标。"},
                {"en": "The clever cat caught a brown mouse in the dark barn.", "cn": "机警敏捷的猫咪在昏暗的谷仓里，一下子逮住了一只灰褐老鼠。"},
                {"en": "Let your natural curiosity guide your pursuit of wisdom.", "cn": "让你天生拥有的求知好奇心，指引你去探寻博大精深的智慧。"},
                {"en": "Put on your warm woolen cap before stepping out in the snow.", "cn": "在踏步走向皑皑白雪之前，别忘了戴好你温暖的羊毛毡帽。"},
                {"en": "Tell the honest truth even when confronting uncomfortable facts.", "cn": "即便在直面令人难堪窘迫的现实面前，也务必坚守诚实真理。"},
                {"en": "A bright lamp illuminates the scholar's late-night desk.", "cn": "一盏明亮的案头台灯，照亮了苦读学者深夜挑灯奋战的书桌。"},
                {"en": "Check your spelling accuracy carefully after finishing each line.", "cn": "在拼写完成每一行句子之后，都要仔仔细细校对拼写的准确度。"},
                {"en": "Drop your jaw wider to produce the authentic butterfly vowel sound.", "cn": "将下颌向下适度拉伸打开，才能发出标准纯正的蝴蝶大开口元音。"}
            ]
        },
        {
            "title": "第4章：中元音与卷舌音 /ʌ/, /ə/, /ɜːr/",
            "description": "英语最核心弱读元音 schwa /ə/ 与强调重读音。",
            "sentences": [
                {"en": "The bright sun warms the fertile fields in early spring.", "cn": "初春明媚的太阳，温暖着这一方生机盎然的沃野田畴。"},
                {"en": "A cup of hot herbal tea calms the racing human mind.", "cn": "一杯热气腾腾的草本香茗，能抚平现代人纷乱浮躁的心绪。"},
                {"en": "Love and mutual trust form the solid foundation of true peace.", "cn": "彼此相爱与由衷信任，构筑起了世间真正长久和平的坚固基石。"},
                {"en": "The early bird catches the nutritious morning worm.", "cn": "早起的鸟儿有虫吃，时不我待才能在人生中占尽先机。"},
                {"en": "Hard work always earns honest praise and lasting respect.", "cn": "辛勤耕耘的汗水，终将赢得坦荡诚恳的赞誉与经久不息的敬重。"},
                {"en": "Learn to speak with confidence and natural inner conviction.", "cn": "学会带着从容不迫的笃定自信与源自内心的坚定信念开口说话。"},
                {"en": "The little girl wore a lovely purple dress to the concert.", "cn": "那个小女孩身着一袭优雅迷人的紫色小礼服出席音乐会。"},
                {"en": "Turn obstacles into stepping stones toward ultimate triumph.", "cn": "将横亘在眼前的重重羁绊，淬炼成通向最终辉煌胜利的踏脚石。"},
                {"en": "The schwa sound is the most frequent unstressed vowel in English.", "cn": "非重读央元音 schwa 是英语语音系统中使用最为频繁的弱读元音。"},
                {"en": "About ten thousand people gathered to listen to the speech.", "cn": "大约有上万人扶老携幼聚拢在一起，聆听这场振奋人心的演说。"},
                {"en": "Mother prepared a delicious homemade dinner for the family.", "cn": "勤劳的母亲为全家人张罗准备了一顿可口的丰盛家常晚餐。"},
                {"en": "Never judge another person without understanding their struggle.", "cn": "在真正设身处地洞悉他人的艰难挣扎之前，切勿妄下评判断语。"},
                {"en": "Run forward with courageous determination toward your dreams.", "cn": "怀揣着坚韧勇毅的决绝魄力，大步流星奔向你心中的远大梦想。"},
                {"en": "Observe how unstressed syllables rhythmically glide by in speech.", "cn": "仔细体味连贯语流中弱读音节如行云流水般轻盈掠过的韵律感。"},
                {"en": "Mastering central vowels elevates your spoken accent immediately.", "cn": "精熟驾驭中元音发音要领，能让你的英语口语纯正度瞬间实现质的跃升。"}
            ]
        },
        {
            "title": "第5章：双元音滑音魅力 /aɪ/, /eɪ/, /ɔɪ/",
            "description": "饱满滑动，掌握 high, day, boy 的发音韵律。",
            "sentences": [
                {"en": "Aim high and never settle for an ordinary, mediocre existence.", "cn": "志存高远，永远不要向庸庸碌碌、平淡无奇的平庸生活妥协低头。"},
                {"en": "Time and tide wait for no man in this fleeting life.", "cn": "光阴荏苒岁月如梭，滚滚东逝的江水在浮生中从不为任何人驻足停留。"},
                {"en": "Light shines brightest in the deepest, most silent darkness.", "cn": "璀璨的光华，往往在最深沉、最万籁俱寂的幽暗中闪耀得最为夺目。"},
                {"en": "Make today an extraordinary masterpiece of focused effort.", "cn": "倾注全神贯注的心血汗水，把今天雕琢成一幅卓越非凡的传世杰作。"},
                {"en": "Patience and practice pave the royal way to fluency.", "cn": "持之以恒的耐性与扎扎实实的苦练，能铺就通往语言纯熟的康庄大道。"},
                {"en": "Great achievements require unwavering faith and persistent sweat.", "cn": "任何宏大伟业的筑就，都需要坚如磐石的坚定信念与持之以恒的辛勤汗水。"},
                {"en": "The joyful boy clapped his hands with uninhibited delight.", "cn": "那个满心欢喜的小男孩忘情地拍击着双手，脸上洋溢着由衷的欢愉。"},
                {"en": "Good books bring immense joy to a thoughtful, reflective mind.", "cn": "开卷有益的经典良书，能给深思沉潜的心灵带去不可估量的精神愉悦。"},
                {"en": "Make a deliberate choice to live each day with honor.", "cn": "做出清醒自决的崇高抉择，把生命中的每一个日子都活得庄严有尊严。"},
                {"en": "Voices joined together in an inspiring chorus of celebration.", "cn": "万千嘹亮的嗓音汇聚成海，共同唱响了一曲振奋人心的欢庆大合唱。"},
                {"en": "Glide smoothly from the first vowel sound into the second.", "cn": "发双元音时，务必圆润饱满、行云流水地从第一个元音滑向第二个。"},
                {"en": "Play your violin with expressive passion and clean technique.", "cn": "以充沛激昂的热忱情感与洗练精准的运弓指法，奏响你的小提琴。"},
                {"en": "A bright smile breaks through dark clouds of anxiety.", "cn": "一抹温暖灿烂的微笑，足以冲破心头笼罩的一切焦虑与阴霾。"},
                {"en": "Never compromise on the core principles that define you.", "cn": "在那些定义你立身之本的核心价值原则面前，永远绝不妥协退让。"},
                {"en": "Diphthongs require ample time and full jaw glide to sound authentic.", "cn": "双元音需要赋予其充足的时值与完整的下颌滑动，方能听起来浑厚地道。"}
            ]
        },
        {
            "title": "第6章：双元音收口音 /aʊ/ 与 /oʊ/",
            "description": "口型由大变小，区分 now 与 no，house 与 boat。",
            "sentences": [
                {"en": "Now is the exact right moment to embark on your journey.", "cn": "立足当下，此时此刻正是你启程踏上崭新漫漫征途的最佳黄金契机。"},
                {"en": "A proud stone house stands firmly atop the windy hill.", "cn": "一座巍峨挺拔的坚固石屋，在朔风呼啸的山巅傲然伫立。"},
                {"en": "He climbed down the steep rocky mountain trail safely.", "cn": "他步履沉稳化险为夷，平安顺遂地从陡峭崎岖的岩石山道上攀爬下山。"},
                {"en": "Loud thunder echoed through the dark, cavernous valley.", "cn": "惊天动地的炸雷声，在幽深昏暗的山谷绝壁之间轰然回荡。"},
                {"en": "Count your many blessings with a humble, grateful heart.", "cn": "怀揣一颗谦卑感恩的心灵，细细数点生活中降临在你身上的万千福泽。"},
                {"en": "Go forward boldly without fear of temporary stumbling blocks.", "cn": "大步流星勇敢向前迈进，浑然无惧道路上偶遇的短暂磕绊与挫折。"},
                {"en": "A small wooden boat sailed into the tranquil harbor at dusk.", "cn": "黄昏日暮时分，一叶小巧的木舟轻巧平稳地驶入了宁静祥和的港湾。"},
                {"en": "Keep the golden flame of hope burning brightly within you.", "cn": "让你胸膛中那一簇象征希望的金色火种，永远熊熊燃烧永不熄灭。"},
                {"en": "Pure white snow gently coated the rooftops of the village.", "cn": "纯洁无瑕的皑皑白雪，悄无声息地为整个古老村庄的屋脊披上了素裹。"},
                {"en": "Follow the narrow trail until it opens into the meadow.", "cn": "沿着这条蜿蜒狭窄的小径一路前行，直到眼前豁然开朗展现出辽阔草甸。"},
                {"en": "Round your lips progressively as you conclude the vowel glide.", "cn": "在双元音滑音收尾的一刹那，有意识地让双唇逐渐收拢成小圆孔状。"},
                {"en": "He spoke with a mellow, resonant tone that captivated all.", "cn": "他以醇厚磁性、充满共鸣的沉稳嗓音娓娓道来，深深吸引了所有人。"},
                {"en": "Show kindness and compassion to every stranger on the road.", "cn": "向旅途中邂逅的每一位陌生赶路人，主动展现出你的善良与体贴关怀。"},
                {"en": "Old memories glow like warm embers in the evening breeze.", "cn": "往昔珍贵的美好回忆，在暮色微风中宛如温暖的炉火余烬般静静泛光。"},
                {"en": "Controlled mouth movement creates crisp, intelligible English syllables.", "cn": "严格规范自如的唇齿开合运动，能铸就清晰利落、极富辨识度的发音。"}
            ]
        },
        {
            "title": "第7章：咬舌音 /θ/ 与 /ð/ 专项攻坚",
            "description": "舌尖微露轻触上齿，突破 think, thank, this, that 纯正发音。",
            "sentences": [
                {"en": "Think deeply and critically before arriving at a final verdict.", "cn": "在对事物做出最终的定论判断之前，务必进行深刻而严密的辩证思考。"},
                {"en": "I thank you from the bottom of my heart for your guidance.", "cn": "我发自肺腑最深处，由衷感谢您长期以来给予我的悉心栽培与点拨。"},
                {"en": "Speaking the truth requires supreme courage and moral conviction.", "cn": "敢于挺身直言不讳讲出事实真相，需要超凡的无畏勇气与道德魄力。"},
                {"en": "Three determined scholars published a groundbreaking research paper.", "cn": "三位志同道合、矢志不渝的求索学者，联袂发表了一篇开创性的学术论文。"},
                {"en": "Breathe in pure mountain air and exhale all lingering anxiety.", "cn": "深深吸入一口甘甜清冽的高山清新空气，将心头残留的焦虑彻底吐尽。"},
                {"en": "This is the noble vision that inspires our collective journey.", "cn": "正是这一宏伟远大的崇高愿景，鼓舞着我们所有人风雨同舟携手并进。"},
                {"en": "That memorable evening marked the turning point of his career.", "cn": "那个令人毕生难忘的夜晚，成为了他整个人生职业生涯的历史性转折点。"},
                {"en": "They walked together through stormy weather without a complaint.", "cn": "他们并肩风雨同舟踏平风浪，一路上没有哪怕半句毫无意义的抱怨牢骚。"},
                {"en": "My loving mother and father sacrificed much for my education.", "cn": "我慈爱的父亲母亲为了让我接受最优质的教育，默默倾尽了半生心血。"},
                {"en": "Smooth leather boots protect feet from thorns and jagged rocks.", "cn": "光滑坚实的厚皮革靴子，能保护双脚免受荆棘与锋利碎石的刺伤。"},
                {"en": "Place your tongue tip gently between your upper and lower teeth.", "cn": "把你的舌尖极其轻柔地放置在上下门齿之间，让气流从齿缝间摩擦而出。"},
                {"en": "Distinguish clearly between unvoiced /θ/ and voiced /ð/ sounds.", "cn": "清清楚楚区分不震动声带的清齿擦音 /θ/ 与震动声带的浊齿擦音 /ð/。"},
                {"en": "Healthy habits and wealth of mind are true foundations of peace.", "cn": "健康的日常作息与内心深处的精神富足，才是人生真正的泰然安宁之基。"},
                {"en": "Faith moves mountains when backed by persistent daily action.", "cn": "当心中笃定的信念辅以日复一日的实际行动时，便拥有移山填海的伟力。"},
                {"en": "Never substitute the /s/ or /z/ sound for the dental fricative.", "cn": "千万切忌偷懒用普通齿龈音 /s/ 或 /z/ 来敷衍替代正统的咬舌摩擦音。"}
            ]
        },
        {
            "title": "第8章：爆破音与送气清浊对比 /p, b/, /t, d/, /k, ɡ/",
            "description": "强气流与声带震动，区分 pet 与 bet，ten 与 den，coat 与 goat。",
            "sentences": [
                {"en": "Practice every single sentence with relentless focus and precision.", "cn": "以毫不松懈的专注定力与严苛的标准，精益求精练习每一个地道句子。"},
                {"en": "Build a rock-solid foundation of basic vocabulary and grammar.", "cn": "为自己的语言大厦，夯筑起一座坚如磐石的核心词汇与基础语法基座。"},
                {"en": "Time and patience transform rough stones into sparkling diamonds.", "cn": "漫长时间的洗礼与耐性的雕琢，能将粗糙的顽石淬炼成璀璨夺目的钻石。"},
                {"en": "Dare to dream daring dreams and pursue them with bold steps.", "cn": "敢于确立最具挑战性的雄伟梦想，并以大刀阔斧的果敢步伐奋力追寻。"},
                {"en": "Keep moving forward steadily even when facing severe headwinds.", "cn": "即便迎面遭遇极其险恶的刺骨逆风，也依然要坚定不移沉稳向前迈进。"},
                {"en": "Give credit generously to teammates who helped achieve the goal.", "cn": "把功绩与荣誉毫无保留地归功于那些鼎力相助达成目标的团队伙伴们。"},
                {"en": "Put on your warm winter coat before leaving the heated room.", "cn": "在踏出暖气融融的房间之前，提前穿好你那件御寒保暖的厚大衣。"},
                {"en": "The brave mountain goat leaped across the dangerous rocky chasm.", "cn": "那只勇猛矫健的野山羊纵身一跃，轻而易举跨越了万丈深渊的危险峡谷。"},
                {"en": "Clear aspiration drives continuous improvement across every field.", "cn": "清晰远大的崇高志向，在任何专业领域都是驱动个人持续精进的引擎。"},
                {"en": "Be proud of your honest work and continuous personal growth.", "cn": "为你自己付出的踏实劳动，以及一天天取得的实质性成长而自豪。"},
                {"en": "A sudden burst of compressed air characterizes the voiceless stops.", "cn": "口腔内积蓄的气流瞬间爆破喷涌而出，是发好清爆破辅音的灵魂特征。"},
                {"en": "Feel the vocal cords vibrating inside your throat on voiced stops.", "cn": "发浊爆破辅音时，用手摸摸喉部，真切感受声带强烈的振动与共鸣。"},
                {"en": "Mastering stops prevents confusion between closely paired words.", "cn": "牢牢掌握爆破音发音法则，能从源头上杜绝形近词在听辨中的混淆不清。"},
                {"en": "Great speakers enunciate final consonant sounds with distinct clarity.", "cn": "卓越非凡的演讲大师，在处理单词尾缀辅音时往往咬字极其清晰交代分明。"},
                {"en": "Clean pronunciation builds an immediate bridge of trust with listeners.", "cn": "字正腔圆的标准地道发音，能在你与聆听者之间瞬间建立起信任的纽带。"}
            ]
        },
        {
            "title": "第9章：鼻辅音与流音 /m, n, ŋ/, /l, r/",
            "description": "鼻腔共鸣、舌侧音 /l/ 与卷舌音 /r/ 区分，让发音浑厚通透。",
            "sentences": [
                {"en": "Make a clear mental roadmap of your educational objectives.", "cn": "为你的人生求学奋斗目标，绘制出一张清晰明了的内心思维路线图。"},
                {"en": "Knowledge is the ultimate power that liberates the human soul.", "cn": "博大精深的科学学识，是解放人类灵魂枷锁、赋予人生自由的至高伟力。"},
                {"en": "The morning singing of woodland birds fills our hearts with joy.", "cn": "清晨林间小鸟婉转清脆的琅琅啼鸣，让我们的心田充盈着无尽的喜悦。"},
                {"en": "Look on the bright side of every challenging situation in life.", "cn": "无论面对生活中何等棘手艰难的复杂局面，始终望向充满光明的一面。"},
                {"en": "Read great literature to expand your vocabulary and inner depth.", "cn": "多读传世经典文学，以成倍拓宽你的核心词汇储备与深刻精神厚度。"},
                {"en": "A clear stream flows gently through the lush green meadow.", "cn": "一条清澈见底的蜿蜒小溪，在青翠欲滴的广袤草甸间轻柔潺潺流淌。"},
                {"en": "Right decisions emerge from quiet reflection and careful thought.", "cn": "明智而万全的正确决断，往往脱胎于平心静气的沉潜自省与深思熟虑。"},
                {"en": "Light travels faster than sound across the infinite universe.", "cn": "在广袤无垠的浩瀚宇宙中，光线传播的速度远远凌驾于声音之上。"},
                {"en": "Listen closely to the advice of mentors who walked the path.", "cn": "虚心侧耳倾听那些曾经踏过荆棘之路的先贤长辈们所给出的良箴诤言。"},
                {"en": "Never confuse the lateral liquid /l/ with the rhotic glide /r/.", "cn": "在发音时，切勿将舌尖抵住上齿龈的舌侧音 /l/ 与悬空后缩的卷舌音 /r/ 混为一谈。"},
                {"en": "Direct airflow completely through nasal passages when producing /ŋ/.", "cn": "在发出后鼻音 /ŋ/ 的瞬间，将软腭下垂使全部气流从鼻腔共鸣激荡而出。"},
                {"en": "Pronounce the final dark /l/ sound with smooth velar resonance.", "cn": "在发单词词尾的舌后软腭化辅音 dark /l/ 时，带出浑厚通透的舌根共振。"},
                {"en": "A rich resonant voice commands attention and projects authority.", "cn": "浑厚饱满、充满共鸣的磁性嗓音，能瞬间吸引全场目光并彰显威严自信。"},
                {"en": "Regular phonetic drills build muscle memory for flawless speech.", "cn": "规律系统的语音微调训练，能塑造出肌肉记忆，促成无可挑剔的流利表达。"},
                {"en": "Articulate each consonant with surgical accuracy and effortless ease.", "cn": "以如同手术刀般精密的准确度，从容不迫、游刃有余地交代好每一个辅音。"}
            ]
        },
        {
            "title": "第10章：语流中的连读、弱读与节奏律动",
            "description": "连读 liaison、失爆、弱读与英语重音节律综合实战。",
            "sentences": [
                {"en": "Turn it on, pick it up, and take it easy, my friend.", "cn": "打开它，拾起它，放轻松慢慢来，我亲爱的朋友。"},
                {"en": "English is a stress-timed language with a rhythmic musical beat.", "cn": "英语是一门以重音计时、节拍错落有致、充满音乐律动美感的语言。"},
                {"en": "Function words like articles and prepositions are naturally reduced.", "cn": "冠词、介词等结构虚词在日常语流中，往往自然而然进行柔和的弱读。"},
                {"en": "Content words carrying vital information receive full emphasis.", "cn": "而承载着关键核心信息的实词动词与名词，则必须赋予饱满的重读重音。"},
                {"en": "Link the consonant at the end of a word to the vowel next.", "cn": "当前一个单词以辅音结尾而后一个单词以元音开头时，顺畅进行自然连读。"},
                {"en": "Stop making excuses and start creating meaningful daily progress.", "cn": "停止寻找任何苍白无力的借口，立刻着手去创造扎实富有意义的每日进步。"},
                {"en": "Would you like a cup of tea or a cold glass of fresh water?", "cn": "您是想来一杯热茶，还是想喝一杯清凉爽口的鲜榨纯净水呢？"},
                {"en": "Practice makes perfect when guided by accurate scientific methods.", "cn": "只要有科学严谨的方法作为前行指南，日复一日的练习必将换来熟能生巧。"},
                {"en": "Intonation rises gently on questions and falls firmly on statements.", "cn": "一般疑问句在句尾语调通常温和上扬，而陈述句则以坚定的降调沉稳收尾。"},
                {"en": "Shadowing native recordings trains your vocal cords to mimic cadence.", "cn": "坚持跟读原汁原味的母语录音，能训练你的声带肌肉完美模仿其语调起伏。"},
                {"en": "Read aloud with passion, varying your volume, pitch, and speed.", "cn": "大声朗读并倾注充沛的情感，有意识地调节音量的大小、音调的高低与语速快慢。"},
                {"en": "Smooth blending of sounds creates the illusion of effortless fluency.", "cn": "行云流水般的声音融会贯通，能营造出毫不费力、地道纯熟的母语般语感。"},
                {"en": "You have thoroughly mastered all fundamental English phonetic rules!", "cn": "你已经彻底融会贯通了英语全部四十八个国际音标的核心发音法则！"},
                {"en": "Speak proudly with your authentic voice and inspire the world.", "cn": "自豪大胆地用你饱满从容的声音开口说话，用你的语言去鼓舞整个世界！"},
                {"en": "Your phonetic journey is the golden foundation of lifelong eloquence.", "cn": "你在语音音标上所迈出的这坚实一步，是你通向终身出口成章的黄金基石。"}
            ]
        }
    ]
}

print("COURSE_BASIC_PHONETICS ready")
