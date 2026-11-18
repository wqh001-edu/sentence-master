# -*- coding: utf-8 -*-
"""
少儿英语生成器 Part 4:
7. kids-songs: 经典英文儿歌欢唱启蒙 (10章 x 15句 = 150句)
8. kids-nature: 小小探索家探索大自然 (10章 x 15句 = 150句)
"""

COURSE_KIDS_SONGS = {
    "meta": {
        "id": "kids-songs",
        "title": "经典英文儿歌欢唱启蒙",
        "category": "kids",
        "categoryName": "少儿英语",
        "coverGradient": "from-rose-400 to-pink-600",
        "icon": "🎵",
        "description": "精选一闪一闪小星星、伦敦大桥、宾果小狗等数十首全球传唱经典的英文儿歌韵律，在欢快节奏中掌握纯正语感。",
        "difficulty": "beginner",
        "tags": ["少儿英语", "英文儿歌", "韵律语感", "趣味欢唱"]
    },
    "chapters": [
        {
            "title": "第1章：一闪一闪小星星 (Twinkle, Twinkle, Little Star)",
            "description": "传唱全球的经典摇篮曲，优美夜空与钻石繁星韵律。",
            "sentences": [
                {"en": "Twinkle, twinkle, little star, how I wonder what you are!", "cn": "一闪一闪小星星，我多么好奇你究竟是什么！"},
                {"en": "Up above the world so high, like a diamond in the sky.", "cn": "高高挂在天边，宛如一颗悬在天空中的璀璨钻石。"},
                {"en": "When the blazing sun is gone, when he nothing shines upon.", "cn": "当炽热的太阳落山离去，当这世间再无阳光照耀大地。"},
                {"en": "Then you show your little light, twinkle, twinkle, through the night.", "cn": "这时你就展现出你微弱的星光，整夜一闪一闪照亮人间。"},
                {"en": "Then the traveler in the dark thanks you for your tiny spark.", "cn": "漆黑夜幕中赶路的游子，由衷感谢你散发出的这一抹微芒。"},
                {"en": "He could not see which way to go if you did not twinkle so.", "cn": "如果你不这样闪烁发光，他甚至不知该走向何方。"},
                {"en": "In the dark blue sky you keep, often through my curtains peep.", "cn": "在深蓝色的夜空里你彻夜守候，时常透过我的窗帘悄悄探看。"},
                {"en": "For you never shut your eye till the morning sun is in the sky.", "cn": "因为你从不合拢闪烁的眼睛，直到晨曦的暖阳升上碧空。"},
                {"en": "As your bright and tiny spark lights the traveler in the dark.", "cn": "正是你那明亮微小的火花，在茫茫黑夜中照亮了旅人的征途。"},
                {"en": "Though I know not what you are, twinkle, twinkle, little star.", "cn": "虽然我尚且不知你究竟是什么，闪耀吧闪耀吧，神奇的小星星。"},
                {"en": "Sing this soothing lullaby softly as you drift off to sleep.", "cn": "在安详步入梦乡之际，轻声哼唱这首舒缓温柔的催眠曲。"},
                {"en": "The calm midnight breeze carries your sweet voice across the hills.", "cn": "宁静的午夜清风，将你甜美动人的歌声吹送过连绵的山丘。"},
                {"en": "Countless sparkling stars keep watch over all sleeping children.", "cn": "数以万计闪烁的繁星，默默守护着大地上所有熟睡的小朋友。"},
                {"en": "Close your sleepy eyes in peace and dream of golden constellations.", "cn": "安详地合上困倦的双眼，在美梦中翱翔于金色的星座之间。"},
                {"en": "Music fills the night sky with everlasting harmony and tender wonder.", "cn": "美妙的音乐用永恒的和谐与温柔的奇迹，浸润了整座浩瀚夜空。"}
            ]
        },
        {
            "title": "第2章：公共汽车的车轮转呀转 (The Wheels on the Bus)",
            "description": "动感十足的巴士出行儿歌，模拟车轮、雨刷、喇叭与乘客动作。",
            "sentences": [
                {"en": "The wheels on the yellow bus go round and round all through town.", "cn": "黄色校车的大轮子骨碌碌转呀转，一路欢快穿行过整座城镇。"},
                {"en": "Round and round, round and round, rolling smoothly along the street.", "cn": "转呀转，转呀转，稳稳当当、平平稳稳地在马路上飞驰。"},
                {"en": "The wipers on the front bus window go swish, swish, swish in rain.", "cn": "大巴士车窗前的雨刷器在雨水中刷呀刷，刷呀刷。"},
                {"en": "Swish, swish, swish, clearing away falling raindrops with ease.", "cn": "刷呀刷，刷呀刷，轻而易举把所有落下的雨滴统统刮得干干净净。"},
                {"en": "The shiny horn on the friendly bus goes beep, beep, beep loudly.", "cn": "友善校车上响亮的喇叭哔哔哔，清脆欢快地按个不停。"},
                {"en": "Beep, beep, beep, alerting everyone that the school bus is here.", "cn": "哔哔哔，大声告诉大家校车已经准时停靠在站台啦。"},
                {"en": "The doors on the bright bus open and shut to let friends in.", "cn": "明亮的大客车门开呀开关呀关，迎接着一个个上车的小伙伴。"},
                {"en": "Open and shut, open and shut, welcoming every smiling face.", "cn": "开呀开，关呀关，热情迎接着每一张绽放笑靥的小脸庞。"},
                {"en": "The people on the morning bus go up and down over bumpy roads.", "cn": "清晨坐在颠簸路段上的乘客们，随着车身忽上忽下欢快起伏。"},
                {"en": "Up and down, up and down, laughing together as the bus rides along.", "cn": "上上下下，蹦蹦跳跳，伴着车轮的律动大家一路欢声笑语不断。"},
                {"en": "The driver on the bus says: Please move on back, step inside.", "cn": "校车司机叔叔和蔼地招呼道：“请大家往后走，坐稳扶好。”"},
                {"en": "The sweet little babies on the bus go wah, wah, wah for attention.", "cn": "车上可爱的小宝宝哇哇哇地叫着，想要吸引妈妈的注意。"},
                {"en": "The gentle mothers on the bus go shh, shh, shh to calm them.", "cn": "温柔的妈妈们嘘嘘嘘地轻声细语，抚慰着怀里哭闹的宝宝。"},
                {"en": "Sing and perform all these fun actions with your joyful hands.", "cn": "用你欢快舞动的小手，一边唱一边模仿做出这些逗趣的动作吧。"},
                {"en": "Every ride on this happy bus is a journey of pure delight.", "cn": "搭乘这趟快乐校车的每一次旅程，都是一趟纯真无邪的美妙欢愉之旅。"}
            ]
        },
        {
            "title": "第3章：老麦克唐纳有个农场 (Old MacDonald Had a Farm)",
            "description": "世界经典农场儿歌，学唱各种小动物叫声与农场欢腾场面。",
            "sentences": [
                {"en": "Old MacDonald had a vast green farm, E-I-E-I-O!", "cn": "老麦克唐纳有一个绿油油的大农庄，咿呀咿呀哟！"},
                {"en": "And on his farm he had some cows, E-I-E-I-O!", "cn": "在他的农庄里养了一群大奶牛，咿呀咿呀哟！"},
                {"en": "With a moo-moo here and a moo-moo there, chewing sweet clover.", "cn": "这里哞哞叫，那里哞哞叫，嘴里大口咀嚼着甘甜的三叶草。"},
                {"en": "Here a moo, there a moo, everywhere a contented moo-moo.", "cn": "这里一声哞，那里一声哞，到处都是心满意足的哞哞叫声。"},
                {"en": "And on his farm he had some cheerful ducks, E-I-E-I-O!", "cn": "在他的农庄里还养了一群欢快的小鸭子，咿呀咿呀哟！"},
                {"en": "With a quack-quack here and a quack-quack there in the muddy pond.", "cn": "在泥泞清凉的池塘里，这里嘎嘎叫，那里嘎嘎叫。"},
                {"en": "Here a quack, there a quack, paddling fast with webbed feet.", "cn": "这里一声嘎，那里一声嘎，用脚蹼飞快地划动着水花。"},
                {"en": "And on his farm he had some pink playful pigs, E-I-E-I-O!", "cn": "在他的农庄里养着几只粉嘟嘟的可爱小猪，咿呀咿呀哟！"},
                {"en": "With an oink-oink here and an oink-oink there, rolling in soft straw.", "cn": "这里哼哼叫，那里哼哼叫，在松软的干草堆里滚来滚去。"},
                {"en": "And on his farm he had a loyal sheepdog running across fields.", "cn": "在农场广袤的田野上，还有一条奔跑如风的忠诚牧羊犬。"},
                {"en": "With a woof-woof here and a woof-woof there, guarding every sheep.", "cn": "这里汪汪叫，那里汪汪叫，尽职尽责守护着羊群的安全。"},
                {"en": "Woolly white sheep reply with a gentle baa-baa under the sun.", "cn": "毛茸茸的白绵羊在阳光下，温顺地发出柔和的咩咩回应。"},
                {"en": "Farmers feed their livestock with immense devotion and care every day.", "cn": "勤劳的农场主们倾注无尽的关爱，日复一日精心喂养家畜。"},
                {"en": "Old MacDonald smiles proudly at his noisy, thriving rural haven.", "cn": "老麦克唐纳注视着自己热闹非凡、生机勃勃的农庄，笑逐颜开。"},
                {"en": "Sing along loudly and imitate the lively sounds of all creatures.", "cn": "放声欢快齐唱，生动模仿出所有这些生灵热闹活泼的叫声吧。"}
            ]
        },
        {
            "title": "第4章：小农夫养了一只小狗叫宾果 (B-I-N-G-O)",
            "description": "经典节奏拍手拼字儿歌，训练字母拼写与节奏专注力。",
            "sentences": [
                {"en": "There was a farmer who had a dog, and Bingo was his name-o.", "cn": "从前有个老农夫养了一条小狗，小狗的名字就叫做宾果。"},
                {"en": "B-I-N-G-O, B-I-N-G-O, B-I-N-G-O, and Bingo was his name-o!", "cn": "B-I-N-G-O，B-I-N-G-O，B-I-N-G-O，宾果就是它的名字呀！"},
                {"en": "Clap your hands for letter B, and sing out the rest of the letters.", "cn": "用双手拍击一下代表字母 B，然后大声唱出其余的每一个字母。"},
                {"en": "(Clap)-I-N-G-O, (Clap)-I-N-G-O, wagging its tail with cheerful glee.", "cn": "（拍手）-I-N-G-O，它兴高采烈地摇摆着毛茸茸的尾巴。"},
                {"en": "Now clap your hands two times for B and I with perfect timing.", "cn": "现在随着准确的节拍，为字母 B 和 I 连续欢快拍手两次。"},
                {"en": "(Clap)-(Clap)-N-G-O, bouncing across the green lawn happily.", "cn": "（拍手）-（拍手）-N-G-O，欢天喜地在绿茵茵的草坪上蹦跳。"},
                {"en": "Add another clap for letter N as the musical rhythm speeds up.", "cn": "随着音乐节奏的欢快加快，再为字母 N 增添一声响亮的击掌。"},
                {"en": "(Clap)-(Clap)-(Clap)-G-O, chasing after golden autumn butterflies.", "cn": "（拍手）-（拍手）-（拍手）-G-O，追逐着金秋飞舞的花蝴蝶。"},
                {"en": "Four claps in a row now: (Clap)-(Clap)-(Clap)-(Clap)-O!", "cn": "现在连续拍手四次啦：（拍手）-（拍手）-（拍手）-（拍手）-O！"},
                {"en": "Finally, clap all five times without speaking a single spoken letter.", "cn": "在最后一段里，不念出任何字母，连续击掌整整五次！"},
                {"en": "(Clap)-(Clap)-(Clap)-(Clap)-(Clap), and Bingo was his famous name-o!", "cn": "（拍手）-（拍手）-（拍手）-（拍手）-（拍手），宾果就是它响当当的名字！"},
                {"en": "Bingo is a loyal companion who loves playing fetch with sticks.", "cn": "小狗宾果是一位极其忠诚的伙伴，最喜欢玩捡飞盘和木棍的游戏。"},
                {"en": "This rhythmic song sharpens your concentration and spelling skills.", "cn": "这首节奏鲜明的经典儿歌，能极大地锻炼你的专注力与字母拼写功底。"},
                {"en": "Everyone in the classroom bursts into laughter and enthusiastic applause.", "cn": "整间教室里爆发出小同伴们欢畅的笑声，以及热烈持久的掌声。"},
                {"en": "Singing and spelling together makes English learning pure delight.", "cn": "将欢唱歌谣与精准拼词融为一体，能让英语学习化作纯粹的快乐。"}
            ]
        },
        {
            "title": "第5章：伦敦大桥要塌了 (London Bridge Is Falling Down)",
            "description": "历史悠久的英国传统童谣，建筑材料、拱桥与游戏互动。",
            "sentences": [
                {"en": "London Bridge is falling down, falling down, falling down.", "cn": "伦敦大桥要塌下来了，要塌下来了，要塌下来了。"},
                {"en": "London Bridge is falling down, my fair lady.", "cn": "伦敦大桥要塌下来了，我美丽的贵妇人。"},
                {"en": "Build it up with wood and clay, wood and clay, wood and clay.", "cn": "用结实的木材和泥土重新把它造起来，木材和泥土。"},
                {"en": "Wood and clay will wash away, wash away, wash away.", "cn": "可是木材和泥土会被滚滚的河水冲垮冲走，冲垮冲走。"},
                {"en": "Build it up with bricks and stone, bricks and stone, bricks and stone.", "cn": "用坚硬的砖块和厚重的巨石重新建造它，砖块和巨石。"},
                {"en": "Bricks and stone will stand so strong, stand so strong, stand so strong.", "cn": "砖块和巨石筑就的桥墩屹立不倒坚如磐石，坚如磐石。"},
                {"en": "Set a watchman to guard the bridge throughout the stormy night.", "cn": "安排一位警觉的守桥人，在风雨交加的漫漫长夜里值班守护。"},
                {"en": "Give him a pipe to smoke all night, my fair lady.", "cn": "给他一支烟斗，伴他度过这漫长孤寂的守夜时光，美丽的夫人。"},
                {"en": "Two children form a high archway with their raised hands.", "cn": "两个小朋友手拉着手高高举起手臂，搭建起一座高耸的拱桥。"},
                {"en": "Other children march underneath the singing arch in a circle.", "cn": "其余的小朋友排成一条长队，伴着歌声欢快地从桥拱底下穿过。"},
                {"en": "When the final lyric ends, the arch drops to catch a friend.", "cn": "当最后一句歌词唱毕，高高拱起的双手瞬间落下扣住一位伙伴。"},
                {"en": "Laughter fills the school playground as captured friends giggle.", "cn": "当被“抓获”的小伙伴笑作一团时，欢声笑语洒满了整个操场。"},
                {"en": "Traditional folk songs connect children across centuries and oceans.", "cn": "这些历久弥新的传统民谣歌谣，跨越数百年光阴连接着千万孩子的心。"},
                {"en": "London Bridge stands tall across the sparkling River Thames today.", "cn": "如今，崭新宏伟的伦敦大桥依然巍然横跨在波光粼粼的泰晤士河之上。"},
                {"en": "Singing history through rhyme is an unforgettable way to learn.", "cn": "伴着押韵的欢快儿歌传唱历史，是一种令人毕生难忘的高效求学之道。"}
            ]
        },
        {
            "title": "第6章：玛丽有只小羊羔 (Mary Had a Little Lamb)",
            "description": "经典童真儿歌，白雪般纯洁的羊羔与校园趣味跟随。",
            "sentences": [
                {"en": "Mary had a little lamb, little lamb, little lamb.", "cn": "玛丽养了一只可爱的小羊羔，小羊羔，小羊羔。"},
                {"en": "Mary had a little lamb, its fleece was white as snow.", "cn": "玛丽养了一只小羊羔，它身上的羊毛洁白如同漫天飘落的白雪。"},
                {"en": "And everywhere that Mary went, the lamb was sure to go.", "cn": "无论小玛丽走到天涯海角，那只小羊羔一定会寸步不离紧紧相随。"},
                {"en": "It followed her to school one day, which was against the rule.", "cn": "有一天它竟然跟着她一路溜进了学校，这可是严重违反校规的。"},
                {"en": "It made the children laugh and play to see a lamb at school.", "cn": "看见教室里竟然出现了一只真羊，逗得全班同学哄堂大笑欢呼雀跃。"},
                {"en": "And so the teacher turned it out, but still it lingered near.", "cn": "于是老师只能把它请出门外，然而它依然守候在窗外不肯离去。"},
                {"en": "It waited patiently about till Mary did appear.", "cn": "它在教室门外耐心地守候等待着，直到小玛丽重新走出教室的身影出现。"},
                {"en": "Why does the lamb love Mary so? The eager children cry.", "cn": "“为什么小羊羔会这般深爱玛丽呢？”好奇的小朋友们纷纷大声询问。"},
                {"en": "Why, Mary loves the lamb, you know, the kindly teacher replied.", "cn": "“这还不明白吗，因为玛丽平日里最疼爱这只小羊呀，”慈爱的老师回答道。"},
                {"en": "Love and affection always bring back true devotion in return.", "cn": "你发自内心付出的关爱与温情，终将换来对方毫无保留的由衷依恋。"},
                {"en": "The gentle lamb nibbled green grass by the schoolhouse fence.", "cn": "温顺的小羊羔在校舍木栅栏旁，安详地啃食着嫩绿多汁的青草。"},
                {"en": "Mary patted its soft woolly head with boundless gentle care.", "cn": "玛丽伸出温柔的小手，满含宠溺地轻轻抚摸着它毛茸茸的小脑袋。"},
                {"en": "Animals know who treats them with true respect and tender warmth.", "cn": "大自然的万千生灵天生懂得，谁才是真正以善意和温情体贴对待它们的人。"},
                {"en": "This sweet melody was the first recorded human voice in history.", "cn": "这首甘美动听的儿歌旋律，正是人类录音史上爱迪生留存的第一段人声。"},
                {"en": "A tender heart creates lifelong bonds with nature's creatures.", "cn": "一颗温柔仁爱的心灵，能与大自然的生灵结下相伴一生的深厚羁绊。"}
            ]
        },
        {
            "title": "第7章：划呀划，小船儿荡悠悠 (Row, Row, Row Your Boat)",
            "description": "经典轮唱曲目，顺流而下、生活如梦的悠然境界。",
            "sentences": [
                {"en": "Row, row, row your boat gently down the stream.", "cn": "划呀划，划着你的小木船，顺着小溪从容漂流而下。"},
                {"en": "Merrily, merrily, merrily, merrily, life is but a dream.", "cn": "快快乐乐，欢欢喜喜，人生宛如一场美好绮丽的美梦。"},
                {"en": "Dip your wooden oars into the crystal-clear rippling water.", "cn": "把你的两支木桨轻轻浸入晶莹剔透、泛着层层微澜的溪水中。"},
                {"en": "Pull together with steady rhythm to glide past green meadows.", "cn": "伴随着沉稳均匀的节拍整齐划水，小船悠然滑过一片片绿油油的草甸。"},
                {"en": "Row, row, row your boat out across the calm blue lake.", "cn": "划呀划，划着你的小木船，飘荡在风平浪静的蔚蓝大湖中央。"},
                {"en": "If you see a crocodile, don't forget to scream!", "cn": "如果你不小心看到了一条大鳄鱼，千万别忘了大声尖叫哦！"},
                {"en": "Sing this timeless round in three harmonious separate groups.", "cn": "分成三个声部配合默契地轮唱这首经久不衰的传世轮唱曲。"},
                {"en": "The first group starts singing, and the second follows close behind.", "cn": "第一个小组率先开嗓，第二个小组紧随其后如影相随巧妙衔接。"},
                {"en": "Voices blend together like ripples expanding upon mirror water.", "cn": "童声交融辉映，宛如平静如镜的水面上层层向外扩散的优雅涟漪。"},
                {"en": "Green weeping willows dip their trailing branches along banks.", "cn": "岸边依依垂柳轻垂柔丝，青翠的枝桠宛如轻触着过往的水波。"},
                {"en": "Colorful dragonflies hover above floating white water lily blossoms.", "cn": "五彩斑斓的小蜻蜓在水面上盛开的洁白睡莲花瓣上方轻盈悬停。"},
                {"en": "Keep paddling onward with hope, joy, and peace in your heart.", "cn": "心中怀揣着光明、喜悦与平和，坚定不移地奋力向着前方划动双桨。"},
                {"en": "Life's journey is best enjoyed when flowing gently with the current.", "cn": "漫漫人生的风景旅程，唯有在顺应自然从容不迫的漂流中才最富诗意。"},
                {"en": "Singing in rounds teaches us the magic of musical collaboration.", "cn": "学会轮唱重唱的精妙配合，能让我们深切领略到音乐协作的神奇魔力。"},
                {"en": "Rest your oars and listen to the whisper of the flowing river.", "cn": "收起船桨静静坐好，倾听奔流不息的江水在两岸诉说着的低语。"}
            ]
        },
        {
            "title": "第8章：如果有快乐你就拍拍手 (If You're Happy and You Know It)",
            "description": "最具互动性的少儿律动操，拍手、跺脚与大声欢呼。",
            "sentences": [
                {"en": "If you are happy and you know it, clap your hands!", "cn": "如果感到快乐你就拍拍手，拍拍你的小双手！"},
                {"en": "Clap, clap! Let the whole room echo with cheerful applause.", "cn": "啪啪！让整个房间都回荡起欢快响亮的掌声。"},
                {"en": "If you are happy and you know it, stomp your feet!", "cn": "如果感到快乐你就跺跺脚，欢快地跺跺双脚！"},
                {"en": "Stomp, stomp! Shake the floor with your energetic tapping feet.", "cn": "咚咚！用你充满活力的有力步伐让地板都跟着震颤。"},
                {"en": "If you are happy and you know it, shout: Hurray!", "cn": "如果感到快乐你就大声喊出来：“万岁！万岁！”"},
                {"en": "Hurray! Raise both arms high into the air with radiant triumph.", "cn": "万岁！把双臂高高举向空中，展现出无比灿烂豪迈的胜利姿态。"},
                {"en": "If you are happy and you know it, turn around in place.", "cn": "如果感到快乐你就转个圈，在原地轻快地转上一圈。"},
                {"en": "Spin gracefully on your toes and flash a gigantic bright smile.", "cn": "踮起脚尖优雅地转一圈，脸上绽放出一抹巨大而灿烂的微笑。"},
                {"en": "If you are happy and you know it, do all three together!", "cn": "如果感到快乐你就三个动作一起来，全套做上一遍！"},
                {"en": "Clap, clap! Stomp, stomp! Shout out loud: Hurray!", "cn": "拍拍手！跺跺脚！放开嗓子大声呼喊：“万岁！”"},
                {"en": "Joy expressed openly brings immense sunshine to everyone around.", "cn": "毫不掩饰、大大方方抒发内心的快乐，能把耀眼的阳光播撒给身边的每一个人。"},
                {"en": "Movement and song unite our hearts in spontaneous celebration.", "cn": "欢腾的律动与嘹亮的歌声，让我们在自发的狂欢庆典中紧紧心心相印。"},
                {"en": "No matter how shy you feel, this rhythm will make you dance.", "cn": "不论你平时有多么内向害羞，这一段欢快的节拍必定能让你跟着舞动起来。"},
                {"en": "Laughter is infectious, spreading faster than morning light.", "cn": "开怀的大笑极具感染力，它的传播速度比初升的晨曦日光还要迅捷。"},
                {"en": "Keep happiness dancing alive inside your chest every single day.", "cn": "在以后的每一个日子里，让你胸膛里的快乐精灵永远充满活力地跳跃！"}
            ]
        },
        {
            "title": "第9章：叮咚钟声，猫咪掉井里啦 (Ding Dong Bell)",
            "description": "传统英伦叙事童谣，批评恶作剧、赞扬营救爱心。",
            "sentences": [
                {"en": "Ding, dong, bell, pussy's in the well!", "cn": "叮，咚，钟声响，小猫咪掉进了古井里！"},
                {"en": "Who put her in? Little Johnny Flynn.", "cn": "是谁把它推进井里去的？是那个淘气顽皮的约翰尼·弗林。"},
                {"en": "What a naughty boy was that, to drown poor pussy cat.", "cn": "真是个顽劣不驯的淘气包，竟然妄图淹死可怜无辜的小猫咪。"},
                {"en": "Who pulled her out? Good Little Tommy Stout.", "cn": "又是谁奋不顾身把它救上来的？是正直善良的小汤米·斯托特。"},
                {"en": "What a noble boy was that, who brought her food to eat.", "cn": "真是个崇高优秀的男子汉，不仅救了猫咪还端来鲜美口粮喂它。"},
                {"en": "The poor dripping kitten shivered cold beside the brick well.", "cn": "湿漉漉的可怜小猫咪浑身滴着水珠，在砖石井台旁瑟瑟发抖。"},
                {"en": "Tommy wrapped the wet cat gently in his own warm woolen coat.", "cn": "善良的汤米用自己身上温暖的羊毛大衣，轻轻把浑身湿透的猫咪包裹起来。"},
                {"en": "He took her home to sit beside the crackling stone fireplace.", "cn": "他把猫咪带回了温暖的家，抱到劈啪作响的壁炉旁帮它烤干绒毛。"},
                {"en": "Cruelty to harmless living creatures is disgraceful and wrong.", "cn": "以虐待无辜弱小的生命为乐，是极其可耻且大错特错的不道德行径。"},
                {"en": "True bravery is protecting those who cannot defend themselves.", "cn": "真正的英勇无畏，在于毫不犹豫挺身而出保护那些无力自卫的弱小生灵。"},
                {"en": "The grateful kitten purred softly, rubbing its head on Tommy's palm.", "cn": "感恩的小猫咪发出舒服温存的呼噜声，用小脑袋亲昵地蹭着汤米的手心。"},
                {"en": "A good deed shines like a radiant candle in a dark world.", "cn": "一项仁爱纯良的善行，宛如暗夜里点亮的一盏明灯，散发出无尽的光辉。"},
                {"en": "Always be a brave helper like Tommy, never a bully like Johnny.", "cn": "要时刻像汤米一样做一个勇于助人的小英雄，绝不要做欺凌弱小的恶作剧者。"},
                {"en": "Rhymes teach us profound moral wisdom wrapped in easy verses.", "cn": "看似简单的琅琅童谣，实则将深邃崇高的道德哲理包裹在质朴的诗篇里。"},
                {"en": "Love and defend all innocent animals with a steadfast heart.", "cn": "以一颗坚如磐石的仁爱之心，爱护并捍卫天地间所有无辜纯良的动物生灵。"}
            ]
        },
        {
            "title": "第10章：静静睡吧，摇篮在树梢 (Rock-a-bye Baby)",
            "description": "经典摇篮曲终章，自然微风与母亲怀抱的极致温柔。",
            "sentences": [
                {"en": "Rock-a-bye baby, on the leafy treetop.", "cn": "摇呀摇，睡吧小宝贝，摇篮安歇在茂密的树梢顶端。"},
                {"en": "When the soft wind blows, the gentle cradle will rock.", "cn": "当和煦轻柔的微风吹拂而过，小小的摇篮就会轻柔地摇晃。"},
                {"en": "When the sturdy bough bends, the cradle will swing.", "cn": "当结实的粗树枝轻轻随风弯曲，摇篮就会像秋千一样飘荡。"},
                {"en": "Sleep peacefully, my darling, under the angel's silver wing.", "cn": "安详地睡吧，我最心爱的宝贝，沉浸在天使银白色羽翼的庇护下。"},
                {"en": "Mother holds you securely in her loving, tender arms.", "cn": "母亲用她那双充满爱意、温暖有力的手臂，稳稳地把你护在怀中。"},
                {"en": "No harm can come near you while you rest in love.", "cn": "当你沉浸在深沉的爱意中入睡时，世间没有任何凶险能靠近你半步。"},
                {"en": "Listen to the quiet rustling of leafy branches in the dark.", "cn": "静静聆听夜幕里繁茂树枝在微风吹拂下发出的沙沙低语。"},
                {"en": "The silver crescent moon smiles warmly down upon your crib.", "cn": "银色的一弯月牙在夜空展颜微笑，温柔凝视着你小巧的婴儿床。"},
                {"en": "Let go of all daytime play and drift into blissful dreamland.", "cn": "放下白日里所有的喧闹嬉戏，缓缓沉入那片无忧无虑的美丽梦乡。"},
                {"en": "You have sung and mastered ten legendary English nursery rhymes.", "cn": "你已经以超凡的领悟力，熟练唱熟并掌握了整整十首传世英文童谣！"},
                {"en": "These sweet verses will stay in your heart for decades to come.", "cn": "这些甘甜动人的美妙诗行，必将在未来的漫长岁月里时刻陪伴在你的心间。"},
                {"en": "Rhythm and melody are the golden wings of language learning.", "cn": "节奏与旋律，是语言求学之路上那一对能带你自由翱翔的黄金羽翼。"},
                {"en": "May your childhood be full of song, innocence, and wonder.", "cn": "愿你童年岁月里的每一天，都充盈着欢歌、纯真以及对大千世界的惊叹。"},
                {"en": "Good night, sweet singer, dream under the sparkling constellation.", "cn": "晚安，小小歌唱家，在漫天闪烁的璀璨星光下做一个香甜的美梦吧。"},
                {"en": "Awaken tomorrow ready to conquer new horizons of melody.", "cn": "明朝醒来之时，以饱满昂扬的姿态继续去征服更多崭新的优美旋律！"}
            ]
        }
    ]
}

COURSE_KIDS_NATURE = {
    "meta": {
        "id": "kids-nature",
        "title": "小小探索家探索大自然",
        "category": "kids",
        "categoryName": "少儿英语",
        "coverGradient": "from-emerald-400 to-teal-600",
        "icon": "🌲",
        "description": "面向幼少儿的自然启蒙课，从四季更迭、日月星辰到花草树木、雨雪风雷，用最纯净的地道英语领略自然之美。",
        "difficulty": "beginner",
        "tags": ["少儿英语", "自然科普", "四季风物", "探索启蒙"]
    },
    "chapters": [
        {
            "title": "第1章：太阳先生与灿烂阳光",
            "description": "太阳公公、日出拂晓、光合作用与温暖的一天。",
            "sentences": [
                {"en": "The glorious golden sun rises brightly in the eastern sky.", "cn": "光芒万丈的金色太阳，在东方辽阔的地平线上灿烂升起。"},
                {"en": "Good morning, Mr. Sun, thank you for your warm rays.", "cn": "早上好，太阳公公，非常感谢您赐予大地的温暖光芒。"},
                {"en": "Sunlight wakes up sleeping flowers and makes green grass grow.", "cn": "灿烂的阳光唤醒了沉睡中的娇艳花朵，让绿草茵茵茁壮成长。"},
                {"en": "Without the sun's golden heat, our Earth would be freezing cold.", "cn": "如果没有太阳散发出的无私热量，我们的地球将是一片冰封严寒的荒原。"},
                {"en": "Put on a sun hat and sunscreen when playing outdoors midday.", "cn": "正午在户外奔跑玩耍时，记得戴好遮阳帽并涂抹好防晒霜。"},
                {"en": "Look at your funny shadow stretching across the pavement.", "cn": "看你那被阳光拉长、投射在人行道地砖上的滑稽可爱小影子。"},
                {"en": "In the morning, your shadow is long; at noon, it grows short.", "cn": "清晨时分你的影子拉得长长的；到了正午时分，它就缩得短短的。"},
                {"en": "Green leaves use sunlight to make food in a process called photosynthesis.", "cn": "绿色的树叶利用阳光制造养分，这个奇妙的过程在科学上被称作光合作用。"},
                {"en": "Golden rays filter through leafy tree branches, creating dancing light dots.", "cn": "金灿灿的光柱透过枝繁叶茂的树梢洒下，在地表形成跳跃的光斑。"},
                {"en": "A beautiful sunset paints evening clouds in shades of crimson and orange.", "cn": "一抹绚丽的日落晚霞，把傍晚的云彩染成了火红与橙黄交织的锦缎。"},
                {"en": "The sun dips gently below the horizon, signaling nightfall.", "cn": "太阳缓缓沉入地平线之下，向大地上所有的生灵发出夜幕降临的信号。"},
                {"en": "Rest well, golden sun, we look forward to greeting you tomorrow.", "cn": "好好休息吧，金色的太阳，我们热切期盼着明天拂晓与您再次相逢。"},
                {"en": "Solar panels convert pure sunlight into clean electrical power.", "cn": "屋顶上的太阳能电池板，能将纯净的阳光直接转化为清洁的电能。"},
                {"en": "Sunflowers follow the sun's journey across the sky all day long.", "cn": "金黄的向日葵在一整天的时间里，始终追随着太阳在天际移动的轨迹。"},
                {"en": "The sun is the faithful center of our vast solar neighborhood.", "cn": "太阳是我们辽阔的太阳系大家族当中，恒久忠诚的引力与能量中心。"}
            ]
        },
        {
            "title": "第2章：神奇雨水与雨后彩虹",
            "description": "雨滴落下、泥土芳香、穿雨鞋踩水坑与七色彩虹。",
            "sentences": [
                {"en": "Pitter-patter falls the gentle spring rain outside the window.", "cn": "窗外淅淅沥沥落下了温润柔和的春雨，敲打着玻璃沙沙作响。"},
                {"en": "Dark gray rain clouds gather together high up in the stormy sky.", "cn": "深灰色厚重的雨云，在高高的暴风雨天空顶端迅速聚拢在一起。"},
                {"en": "Open up your bright colorful umbrella to stay cozy and dry.", "cn": "撑开你色彩鲜艳的雨伞，确保自己在雨幕中保持干爽舒适。"},
                {"en": "Slip into your tall yellow rubber boots and go outside.", "cn": "换上你高筒的亮黄色橡胶小雨靴，兴高采烈地迈步走向户外。"},
                {"en": "Splish, splash! Jumping into shallow puddles brings immense childhood fun.", "cn": "扑通，啪嗒！一脚踩进浅浅的小水坑里，带来童年无尽的狂欢乐趣。"},
                {"en": "Fresh rain washes dusty city streets and green forest leaves clean.", "cn": "纯净的雨水把布满灰尘的城市街道与绿色的森林树叶洗刷得一尘不染。"},
                {"en": "Take a deep breath of the wonderfully fresh, earthy smell of wet soil.", "cn": "深深呼吸一口湿润泥土在雨水滋润下，散发出的奇妙自然清香。"},
                {"en": "Tiny worms come out to play on the wet sidewalk after rain.", "cn": "雨过天晴之后，细小的小蚯蚓纷纷钻出泥土来到湿漉漉的地面上散步。"},
                {"en": "The rain clouds part as warm sunshine breaks through the mist.", "cn": "厚重的雨云渐渐散去，温暖的阳光穿透薄雾重新普照人间。"},
                {"en": "Look up! A breathtaking rainbow spans across the clearing sky.", "cn": "快抬头看！一条美得令人窒息的七色彩虹，高高横跨在逐渐放晴的天际。"},
                {"en": "Red, orange, yellow, green, blue, indigo, and violet shine side by side.", "cn": "红、橙、黄、绿、蓝、靛、紫，七种绚丽色带并排在穹顶上熠熠生辉。"},
                {"en": "Water drops act like millions of tiny crystal prisms bending light.", "cn": "空气中漂浮的无数细小水滴，宛如数以百万计的水晶棱镜在折射光线。"},
                {"en": "Rain is an essential part of Earth's natural water cycle.", "cn": "充沛的降水，是维持地球大自然生生不息的水循环系统的核心基石。"},
                {"en": "Without rain, rivers would dry up and plants could not thrive.", "cn": "如果没有甘霖雨露的滋润，江河将会枯竭，草木也将无法繁茂生长。"},
                {"en": "Every rainy day prepares the earth for a burst of vibrant flowers.", "cn": "每一个细雨霏霏的日子，都在为大地孕育一场百花齐放的盛大生机做足准备。"}
            ]
        },
        {
            "title": "第3章：呼呼吹拂的风先生",
            "description": "微风、狂风、放风筝与风力发电大风车。",
            "sentences": [
                {"en": "You cannot see the wind, but you can feel it blow.", "cn": "你肉眼看不到风的形体，但你能真真切切感受到它的吹拂与抚摸。"},
                {"en": "A gentle summer breeze cools our foreheads on a hot afternoon.", "cn": "炎炎夏日的午后，一阵柔和清凉的微风轻拂过我们满是汗水的额头。"},
                {"en": "Listen to the green leaves whispering secrets in the gusting wind.", "cn": "静听阵风吹拂而过时，绿色的树叶在枝头窃窃私语倾诉着小秘密。"},
                {"en": "The strong autumn wind shakes yellow acorns from high tree branches.", "cn": "强劲的金秋大风，把挂在高高树梢上的金黄橡果纷纷摇落到地面。"},
                {"en": "Take your diamond kite out to the vast, open grassy park.", "cn": "带着你心爱的菱形大风筝，奔向那片开阔平坦的青青草地公园。"},
                {"en": "Run fast against the wind and watch your kite climb up high.", "cn": "迎着风大步飞奔，亲眼看着你的风筝迎风直上直冲云霄。"},
                {"en": "Dancing ribbons on the kite's tail flutter against the blue sky.", "cn": "风筝长长尾巴上系着的五彩丝带，在蔚蓝的高空迎风起舞翩翩翻飞。"},
                {"en": "Wind fills the white canvas sails of ships, driving them across oceans.", "cn": "大风鼓满了帆船洁白的风帆，推动着巨轮乘风破浪横跨辽阔大洋。"},
                {"en": "Giant white wind turbines turn slowly on distant green hilltops.", "cn": "一座座高耸的白色风力发电机大叶片，在远方的青山之巅缓缓旋转。"},
                {"en": "Wind power produces clean, renewable electricity without emitting any smoke.", "cn": "风力发电能够源源不断产出清洁的可再生电能，完全不排放一丝有害浓烟。"},
                {"en": "Birds spread their broad wings and glide effortlessly upon wind currents.", "cn": "大鸟张开宽大的双翼，毫不费力地借助迎面吹拂的气流自由滑翔。"},
                {"en": "The winter wind howls through dark chimneys during stormy nights.", "cn": "在暴风雪肆虐的冬夜里，刺骨的狂风在漆黑的烟囱深处呼呼作响。"},
                {"en": "Dandelion seeds float away like tiny parachutes carried by wind.", "cn": "蒲公英的白色种子被微风轻轻托起，宛如一朵朵小降落伞飘向远方。"},
                {"en": "Wind carries plant pollen across valleys to pollinate spring flowers.", "cn": "大风越过崇山峻岭，把植物的花粉撒向四方，为春天的花朵授粉授精。"},
                {"en": "Respect the invisible mighty breath of our living planet Earth.", "cn": "让我们共同心怀敬畏，去感悟这颗生机盎然的地球那看不见的磅礴呼吸。"}
            ]
        },
        {
            "title": "第4章：春暖花开与万物复苏",
            "description": "春天来了、积雪融化、种子发芽与雏鸟孵化。",
            "sentences": [
                {"en": "Spring is a magical season when nature awakens from long winter slumber.", "cn": "春天是一个充满神奇魔力的季节，大自然在此时从漫长的冬眠中苏醒。"},
                {"en": "Warm golden sunshine melts away the thick blanket of winter snow.", "cn": "温暖如阳的金色日光，渐渐融化了大地身上那层厚厚的冬雪棉被。"},
                {"en": "Clear melted water trickles down mountain slopes into laughing streams.", "cn": "消融的清冽雪水顺着山坡涓涓流淌，汇入了欢声笑语的小溪流。"},
                {"en": "Tiny green shoots push through brown soil to greet the light.", "cn": "嫩绿稚嫩的小萌芽顶破肥沃的褐色泥土，争相探出头来迎接光明。"},
                {"en": "Pink cherry blossoms burst into glorious bloom across the gardens.", "cn": "粉嫩的樱花在各大公园的花园里竞相绽放，汇成一片如云似霞的胜景。"},
                {"en": "Cheerful robins and sparrows build sturdy nests in leafy trees.", "cn": "欢快鸣啭的知更鸟与小麻雀，在枝繁叶茂的大树上筑起结实的爱巢。"},
                {"en": "Mother birds lay speckled eggs and warm them with endless love.", "cn": "鸟妈妈产下一窝带着漂亮斑点的小鸟蛋，用无尽的爱心将它们暖暖包裹。"},
                {"en": "Crack! Fragile shells break as hungry baby chicks chirp for food.", "cn": "咔嚓！脆弱的蛋壳裂开了，嗷嗷待哺的雏鸟探出头来唧唧喳喳索要口粮。"},
                {"en": "Fuzzy yellow bees buzz enthusiastically from flower to sweet flower.", "cn": "毛茸茸的金色蜜蜂嗡嗡叫着，兴高采烈地穿梭在每朵甜美的花蕊之间。"},
                {"en": "Farmers plow the fertile fields to sow seeds for autumn harvest.", "cn": "农夫们辛勤耕耘着肥沃的田野，为金秋的丰硕收成播撒下希望的种子。"},
                {"en": "Children shed their heavy winter coats to run freely on lawns.", "cn": "孩子们纷纷脱下厚重笨拙的冬装，换上轻便衣裳在草坪上自由狂奔。"},
                {"en": "Every branch and leaf sings a joyous anthem of fresh beginnings.", "cn": "每一根抽芽的枝丫与每一片嫩叶，都在欢畅奏响崭新开端的赞美诗篇。"},
                {"en": "The air smells sweetly of damp earth and blooming jasmine petals.", "cn": "空气中弥漫着湿润泥土的芳香，以及初绽茉莉花瓣的淡淡甘醇。"},
                {"en": "Spring teaches us that life always triumphs over the coldest darkness.", "cn": "明媚的春天启示着我们：生生不息的生命，终将战胜一切最严酷的寒冬黑暗。"},
                {"en": "Open your heart to hope as the natural world blossoms anew.", "cn": "随着大自然万物重新绽放出磅礴生机，敞开你的心扉去拥抱无限希望。"}
            ]
        },
        {
            "title": "第5章：盛夏蝉鸣与绿意盎然",
            "description": "夏天、雷阵雨、萤火虫、知了鸣叫与海滨游泳。",
            "sentences": [
                {"en": "Summer arrives with long sunny days and balmy evening breezes.", "cn": "盛夏伴随着漫长明媚的白昼与温润如酒的拂面晚风，悄然降临人间。"},
                {"en": "Cicadas sing loudly from the high canopy of leafy oak trees.", "cn": "知了在茂密如盖的高高橡树冠顶端，不知疲倦地扯着嗓子大声高歌。"},
                {"en": "Dense green trees offer welcome shade from the blazing midday heat.", "cn": "绿树浓荫密密匝匝，为炎炎烈日暴晒下的人们提供了一处处清凉的避暑港湾。"},
                {"en": "Swim in the cool, crystal-clear water of the community pool.", "cn": "跳进社区游泳池清凉透亮、晶莹剔透的水波中，尽情畅游戏水。"},
                {"en": "Eat a giant slice of chilled, sweet, and juicy red watermelon.", "cn": "大口大口品尝一块刚切开的冰镇、甘甜又多汁的鲜红大西瓜。"},
                {"en": "Sudden afternoon thunderstorms bring flashes of lightning and rolling thunder.", "cn": "午后突如其来的雷阵雨，伴随着划破天际的闪电与轰隆隆滚过的雷鸣。"},
                {"en": "Cool raindrops refresh the scorching earth in a dramatic downpour.", "cn": "清凉甘冽的雨点在倾盆大雨中从天而降，痛快洗礼着酷热焦灼的燥热大地。"},
                {"en": "At dusk, sparkling fireflies flicker like fairy lanterns in bushes.", "cn": "黄昏日暮时分，闪烁的萤火虫在灌木丛间闪烁微光，宛如小仙子的引路灯笼。"},
                {"en": "Catch a glowing firefly gently in your hands and let it go.", "cn": "用双手轻轻将一只发光的萤火虫合入掌心观瞧片刻，随后放归自由。"},
                {"en": "Walk barefoot on warm golden beach sands listening to waves.", "cn": "光着小脚丫漫步在海滩温暖细腻的细沙上，倾听浪涛拍岸的宏大涛声。"},
                {"en": "Collect smooth seashells and build giant sandcastles by the tide.", "cn": "捡拾光滑圆润的漂亮海贝，在潮涨潮落的海岸边筑造高大的沙雕城堡。"},
                {"en": "Summer nights are filled with the tranquil symphony of chirping crickets.", "cn": "夏日的夜晚充溢着草丛深处促织鸣虫那宁静悠扬的天然交响乐章。"},
                {"en": "Gaze up at the brilliant Milky Way stretching across midnight skies.", "cn": "抬头仰望那条波澜壮阔、横贯在午夜穹顶正中央的璀璨银河大峡谷。"},
                {"en": "Summer is a joyful celebration of life operating at full throttle.", "cn": "盛夏是大自然全部生命动能开足马力、全速奔腾运转的狂欢盛宴。"},
                {"en": "Treasure every golden sun-drenched memory of this vibrant season.", "cn": "珍藏在这段生机勃勃的金色年华里，所留下的每一份沐浴阳光的美好回忆。"}
            ]
        },
        {
            "title": "第6章：金秋落叶与五谷丰登",
            "description": "秋风吹过、落叶变色、松鼠储粮与大自然调色盘。",
            "sentences": [
                {"en": "Autumn paints the mountain forests in rich gold, scarlet, and amber.", "cn": "金秋的大自然挥动画笔，将高山林海装点成了浓郁的纯金、猩红与琥珀色。"},
                {"en": "Crisp morning air signals that the harvest season has truly begun.", "cn": "清晨清脆凉爽的清新空气，向世人宣告五谷丰登的金秋收获季已然来临。"},
                {"en": "Deciduous leaves lose their green chlorophyll and reveal hidden pigments.", "cn": "落叶乔木的树叶逐渐褪去了绿色的叶绿素，显露出深藏于内的绚烂色素。"},
                {"en": "A swirling breeze sends dry leaves tumbling and dancing to the ground.", "cn": "一阵旋风拂过，干燥金黄的落叶在半空中盘旋起舞，翻滚着落向大地。"},
                {"en": "Jump with giggles into a giant pile of freshly raked dry leaves.", "cn": "伴随着欢声笑语，纵身一跃跳进那堆刚被耙拢在一起的厚厚落叶堆中。"},
                {"en": "Crunch! Dry autumn leaves crackle pleasantly beneath your walking shoes.", "cn": "沙沙！脚下干燥的秋叶在你的运动鞋底，发出令人心情舒畅的脆响。"},
                {"en": "Fuzzy squirrels hurry around burying brown acorns for winter survival.", "cn": "毛茸茸的小松鼠忙碌地东奔西走，把一颗颗坚硬的橡果掩埋备荒。"},
                {"en": "Migratory wild geese form a majestic V-formation heading toward south.", "cn": "成群结队南飞过冬的大雁，在万里长空排成威武壮观的人字形长队。"},
                {"en": "Apple orchards are heavy with red fruit ready for picking.", "cn": "红彤彤的苹果沉甸甸挂满果园枝头，静候着果农们开开心心采摘入筐。"},
                {"en": "Round orange pumpkins ripen proudly across sprawling farmland patches.", "cn": "一个个硕大圆润的亮橙色大南瓜，自豪地成熟在广阔连绵的农田地头。"},
                {"en": "Farmers drive giant combine harvesters across golden fields of wheat.", "cn": "农夫们驾驶着庞大的联合收割机，在金黄色的麦浪麦田间大步驰骋。"},
                {"en": "Autumn evenings invite us to gather around warm fireplaces at home.", "cn": "秋意渐浓的微凉夜晚，召唤着全家人围坐在温暖舒适的壁炉旁畅叙天伦。"},
                {"en": "Nature prepares to rest and conserve its vital energy for winter.", "cn": "大自然开始从容地准备休养生息，为即将到来的严冬储备充沛的元气。"},
                {"en": "Change is a natural law of beauty that enriches the universe.", "cn": "周而复始、生生不息的轮转蜕变，是大自然造就大美壮阔的永恒定律。"},
                {"en": "Be grateful for the bountiful harvest that nourishes our bodies.", "cn": "对这片生养我们、以丰厚硕果滋养我们身心的大自然沃土，常怀无尽感恩。"}
            ]
        },
        {
            "title": "第7章：银装素裹的冰雪冬天",
            "description": "白雪飘落、堆雪人、打雪仗与冬眠动物。",
            "sentences": [
                {"en": "Winter arrives in a quiet flurry of delicate, sparkling snowflakes.", "cn": "冬天在漫天飞舞、轻盈剔透、晶莹闪烁的细碎雪花中悄然而至。"},
                {"en": "Each individual snowflake has a unique six-sided crystalline pattern.", "cn": "每一片飘落的雪花，都拥有世间绝无雷同的六角形晶体对称几何图案。"},
                {"en": "A pure white blanket of snow covers rooftops, lawns, and tree branches.", "cn": "一层洁白无瑕的厚重雪毯，将屋顶、草坪与树枝严严实实覆盖遮盖。"},
                {"en": "Bundle up in a thick down coat, woolen scarf, and warm mittens.", "cn": "把自己严严实实裹进厚羽绒服里，围上羊毛围巾，戴好保暖的连指手套。"},
                {"en": "Roll two giant balls of sticky snow to build a jolly snowman.", "cn": "在雪地里滚出两个大大的结实雪球，动手堆起一个圆头圆脑的可爱雪人。"},
                {"en": "Use a crunchy orange carrot for his nose and black buttons for eyes.", "cn": "用一根脆脆的红萝卜当作小雪人的长鼻子，用黑纽扣当作它的大眼睛。"},
                {"en": "Tie an old striped scarf around the snowman's plump cold neck.", "cn": "把一条旧的条纹围巾系在雪人圆滚滚、冰冰凉凉的胖脖子上。"},
                {"en": "Snowballs fly across the snowy playground in friendly, laughing battles.", "cn": "白花花的雪球在雪地操场上飞舞穿梭，带来一场场充满欢笑的雪仗大战。"},
                {"en": "Bears and hedgehogs sleep deeply inside cozy winter dens all season.", "cn": "黑熊和刺猬一整个冬季都在隐蔽温暖的洞穴里深沉冬眠，养精蓄锐。"},
                {"en": "Evergreen pine trees stand proud and green beneath heavy white snowdrifts.", "cn": "四季常青的青松翠柏在沉甸甸的皑皑积雪压顶之下，依然傲雪挺立苍翠欲滴。"},
                {"en": "Lakes and quiet ponds freeze solid into slick sheets of natural ice.", "cn": "湖泊与宁静的池塘冻得结结实实，化作了一面面光滑如镜的纯天然滑冰场。"},
                {"en": "Slide across the frozen pond wearing shiny, sharp ice skates.", "cn": "穿上锃亮锋利的冰刀溜冰鞋，在冰封坚固的湖面上如飞燕般轻盈滑行。"},
                {"en": "Warm steam rises from hot mugs of cocoa sipped by the fireside.", "cn": "手捧热腾腾的浓香热可可坐在火炉边细品，袅袅的暖热雾气升腾而起。"},
                {"en": "Winter's stillness allows the earth to rest before spring's awakening.", "cn": "隆冬时节万籁俱寂的宁静，是为了让大地在春天觉醒前得到充分休憩。"},
                {"en": "The sparkling magic of winter creates a wonderland of peaceful beauty.", "cn": "冬日晶莹剔透的银色魔力，构筑起了一片宛如人间仙境般的静谧至美。"}
            ]
        },
        {
            "title": "第8章：浩瀚夜空与皎洁月亮",
            "description": "月相变化、新月满月、流星雨与太空探险梦想。",
            "sentences": [
                {"en": "The night sky is a vast velvet canvas studded with diamond stars.", "cn": "无垠的夜空宛如一块辽阔的黑色丝绒大幕布，上面点缀着无尽的钻石繁星。"},
                {"en": "The silver moon shines serenely, illuminating the sleeping landscape below.", "cn": "银色的月亮宁静安详地发光，照亮了下方沉睡中的群山、河流与田野。"},
                {"en": "The moon does not produce light; it reflects the sun's brilliance.", "cn": "月亮本身并不发光，它只是忠实反射着太阳照射过来的明亮光芒。"},
                {"en": "Over twenty-nine days, the moon cycles through all its shifting phases.", "cn": "在长达二十九天多的周期里，月亮周而复始地经历着阴晴圆缺的全部月相。"},
                {"en": "A slim crescent moon resembles a golden boat sailing across black seas.", "cn": "一弯初升的细细蛾眉月，酷似一艘在漆黑天海间扬帆远航的金黄色小舟。"},
                {"en": "A full moon glows like a gigantic, flawless pearl in the sky.", "cn": "当满月高悬当空时，它宛如一颗悬浮在天际正中央的无瑕巨大夜明珠。"},
                {"en": "Ancient astronomers grouped bright stars into imaginative constellations.", "cn": "古老的天文学家把一颗颗明亮的星辰串联在一起，勾勒出了富有想象力的星座。"},
                {"en": "Look up to find the Big Dipper pointing toward the North Star.", "cn": "抬头仰望星空，找到那柄清晰的北斗七星勺子，它正指引着北极星的方向。"},
                {"en": "A streak of dazzling light marks a falling shooting star crossing space.", "cn": "一道耀眼炫目的璀璨光痕掠过天际，那是一颗划破深空的绚烂流星。"},
                {"en": "Close your eyes and make a secret wish upon the shooting star.", "cn": "赶紧轻轻闭上双眼，迎着那颗稍纵即逝的流星许下一个美好的心愿吧。"},
                {"en": "Brave astronauts have walked upon the cratered, dusty lunar surface.", "cn": "英勇无畏的宇航员曾亲身踏上月球那布满环形山、覆满尘埃的荒凉表面。"},
                {"en": "Giant optical telescopes peer deep into remote galaxies billions of miles away.", "cn": "庞大的光学天文望远镜深情凝望着数十亿英里开外的遥远古老星系。"},
                {"en": "The universe is infinitely grand, sparking eternal wonder in human hearts.", "cn": "浩瀚宇宙无边无际博大精深，在人类心灵深处激荡起永不磨灭的探索赞叹。"},
                {"en": "Night reminds us that darkness is merely the backdrop for brilliant stars.", "cn": "静谧的黑夜提醒着我们：幽暗只不过是用来衬托星辰璀璨光芒的宏大背景。"},
                {"en": "Dream among the constellations tonight and awaken inspired for tomorrow.", "cn": "今夜伴着漫天浩瀚的群星入梦，明日醒来时胸中将充盈着追求真理的灵感。"}
            ]
        },
        {
            "title": "第9章：森林大家庭与参天大树",
            "description": "树根、树干、树皮、年轮与森林生态系统。",
            "sentences": [
                {"en": "Trees are ancient, silent guardians that nurture life across the world.", "cn": "大树是古老而沉默寡言的坚强卫士，在世界各地默默庇护哺育着无数生灵。"},
                {"en": "Deep underground, strong root networks anchor the tree against violent storms.", "cn": "在大地深处，强壮庞大的根系网络牢牢抓紧泥土，护卫大树抵御狂风暴雨。"},
                {"en": "Roots absorb life-giving water and rich minerals from the damp soil.", "cn": "密密麻麻的根尖从潮湿的泥土中，全力汲取维持生命所需的水分与丰富矿物质。"},
                {"en": "The tall wooden trunk acts like a giant highway transporting sap upward.", "cn": "高高耸立的坚固木质树干，宛如一条贯通上下的超级高速公路输送着生命树液。"},
                {"en": "Tough outer bark protects the inner wood from insects, cold, and fire.", "cn": "坚韧的外层树皮如钢铁铠甲，保护着内部稚嫩的木质部免受虫害、严寒与火灾。"},
                {"en": "Inside a tree trunk, annual growth rings reveal the history of each year.", "cn": "在被截断的树干横截面里，一圈圈年轮如实记载着它经历过的每一个春秋风霜。"},
                {"en": "Wide rings show years of plenty, while narrow rings indicate severe droughts.", "cn": "宽阔舒展的年轮代表雨顺风调的丰盛年份，而紧凑狭窄的年轮则昭示着严酷干旱。"},
                {"en": "Spreading leafy branches provide cozy nesting homes for birds and squirrels.", "cn": "向四周舒展蔓延的枝桠，为无数的鸟儿与敏捷的小松鼠提供了安居筑巢的家园。"},
                {"en": "Green leaves inhale carbon dioxide and exhale clean, oxygen-rich air.", "cn": "绿色的树叶无私吸入二氧化碳，呼出清新甘甜、富含氧气的纯净新鲜空气。"},
                {"en": "Fallen autumn leaves decompose into rich humus, feeding forest floor creatures.", "cn": "凋零的落叶腐烂化作肥沃的腐殖质，为森林地表的小昆虫与真菌提供无尽养料。"},
                {"en": "Old hollow trees provide safe winter hibernation dens for woodland animals.", "cn": "那些上了年纪的空心老树，为林间的野生动物提供了避寒越冬的安全冬眠洞穴。"},
                {"en": "Forests act as Earth's giant lungs, stabilizing global rainfall and climate.", "cn": "广袤的森林堪称我们地球巨大的绿色双肺，维系着全球降雨与气候的稳定平衡。"},
                {"en": "Planting a single tree today gifts shade and fresh air to future generations.", "cn": "今天亲手种下一棵小树苗，是在为未来的子子孙孙赠送一份浓荫与清新空气。"},
                {"en": "Walk respectfully among ancient redwoods, listening to their tranquil wisdom.", "cn": "心怀由衷敬畏漫步在千年古红杉林之间，侧耳倾听它们在岁月中沉淀的宁静智慧。"},
                {"en": "Protect the forests, for in their survival lies the future of all humanity.", "cn": "竭尽全力保卫大森林吧，因为整个人类的前途命运，正深植于森林的繁荣生息之中。"}
            ]
        },
        {
            "title": "第10章：地球母亲守护者誓言",
            "description": "保护环境、节约用水、垃圾分类与小小环保卫士誓言。",
            "sentences": [
                {"en": "Planet Earth is our shared home, a vibrant oasis in deep outer space.", "cn": "地球是我们所有生命共同相依的唯一家园，是深邃外太空中一座生机勃勃的绿洲。"},
                {"en": "Majestic blue oceans, lush green continents, and pure skies sustain us all.", "cn": "碧蓝壮阔的大洋、郁郁葱葱的大陆与澄澈纯净的苍穹，共同滋养着我们全人类。"},
                {"en": "We must become loving caretakers who protect nature's delicate balance.", "cn": "我们每一个人都必须成为心怀大爱的守护者，细心呵护大自然这微妙脆弱的平衡。"},
                {"en": "Turn off the water tap tightly while brushing your teeth each morning.", "cn": "每天清晨在刷牙时随手拧紧水龙头，不让宝贵的生命之水白白流失分毫。"},
                {"en": "Every single drop of clean fresh water is a precious gift to be saved.", "cn": "每一滴甘洌纯净的新鲜淡水，都是需要我们倍加珍惜爱护的无价天赐之礼。"},
                {"en": "Switch off lights and unplug electronics when leaving an empty room.", "cn": "在离开空无一人的房间时，随手关掉所有电灯并拔下不用电器的电源插头。"},
                {"en": "Reduce, reuse, and recycle paper, glass, plastic, and metal responsibly.", "cn": "以高度负责的态度做好减量使用、重复利用以及纸张、玻璃、塑料的垃圾回收。"},
                {"en": "Carry your own cloth shopping tote bag instead of using disposable plastics.", "cn": "外出购物时自带结实耐用的布购物袋，坚决抵制使用一次性白色塑料袋。"},
                {"en": "Walk or ride your bicycle for short trips to keep air clean and clear.", "cn": "短途出行时选择步行或骑脚踏车代步，用实际行动保持城市空气清新明澈。"},
                {"en": "Plant trees, flowers, and vegetable gardens to green our neighborhoods.", "cn": "栽植树木花草，打造家庭果蔬小菜园，为我们的社区增添更多盎然生机。"},
                {"en": "Pick up scattered litter in parks to protect wild animals from harm.", "cn": "主动随手捡拾公园草坪上散落的垃圾废品，保护野生小动物免受误食侵害。"},
                {"en": "Love and respect every living creature from the tiny ant to giant whales.", "cn": "由衷热爱并尊重世间每一个鲜活的生命，从小小的蚂蚁直至大洋中的巨鲸。"},
                {"en": "You have completed all eighty chapters of this junior English series!", "cn": "你已经以超凡的毅力与才智，全面攻克完成了这套少儿英语全部八十个精彩章节！"},
                {"en": "You possess the language skills and kind heart to make a true difference.", "cn": "你不仅掌握了纯熟地道的语言技能，更拥有一颗足以重塑世界的大爱之心。"},
                {"en": "Go forward boldly as a proud guardian of nature, knowledge, and truth!", "cn": "昂首阔步勇毅前行吧，作为大自然、崇高学识与真理的骄傲护卫者！"}
            ]
        }
    ]
}

print("COURSE_KIDS_SONGS, NATURE ready")
