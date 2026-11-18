# -*- coding: utf-8 -*-
"""
少儿英语生成器 Part 2:
包含:
2. kids-daily: 宝宝日常英语交流 (10章 x 15句 = 150句)
3. kids-fairytale: 迪士尼经典童话双语小剧场 (10章 x 15句 = 150句)
4. kids-animals: 奇妙动物王国大百科 (10章 x 15句 = 150句)
"""

COURSE_KIDS_DAILY = {
    "meta": {
        "id": "kids-daily",
        "title": "宝宝日常英语交流",
        "category": "kids",
        "categoryName": "少儿英语",
        "coverGradient": "from-teal-400 to-emerald-500",
        "icon": "🏡",
        "description": "专为亲子家庭量身定制的高频生活情境对话，涵盖起床、穿衣、就餐、洗漱、户外游戏等温馨日常。",
        "difficulty": "beginner",
        "tags": ["少儿英语", "亲子日常", "生活口语", "习惯养成"]
    },
    "chapters": [
        {
            "title": "第1章：清晨起床与问候",
            "description": "阳光明媚的清晨问候与起床洗漱日常句子。",
            "sentences": [
                {"en": "Good morning, my sweet and precious baby!", "cn": "早上好，我最甜美可爱的小宝贝！"},
                {"en": "Time to wake up, the warm sun is already shining.", "cn": "该起床啦，温暖的太阳早就升起来了。"},
                {"en": "Stretch your arms and take a deep breath.", "cn": "伸展一下你的双臂，做个深呼吸吧。"},
                {"en": "Give mommy a gentle kiss on the cheek.", "cn": "给妈妈脸上一个轻轻甜甜的吻。"},
                {"en": "Let us take off your cozy night pajamas.", "cn": "让我们脱下你舒适温暖的睡衣吧。"},
                {"en": "Put on your slippers so your feet stay warm.", "cn": "穿上你的小拖鞋，这样脚丫才不会受凉。"},
                {"en": "Walk over to the bathroom and wash your face.", "cn": "走到卫生间，用温水把小脸洗干净。"},
                {"en": "Squeeze a tiny bit of sweet toothpaste onto your brush.", "cn": "在牙刷上挤一点点甜甜的儿童牙膏。"},
                {"en": "Brush your teeth carefully from top to bottom.", "cn": "从上到下仔仔细细地把牙齿刷干净。"},
                {"en": "Rinse your mouth with clean warm water now.", "cn": "现在用温水咕噜咕噜把嘴巴漱干净。"},
                {"en": "Look at yourself in the mirror with a big smile.", "cn": "看着镜子里的自己，露出一张灿烂的笑脸。"},
                {"en": "Dry your hands and face with this soft towel.", "cn": "用这条柔软干净的毛巾把脸和手擦干。"},
                {"en": "Comb your hair neatly before going to eat.", "cn": "在去吃早餐之前把头发梳理整齐。"},
                {"en": "You look fresh and ready for an exciting day.", "cn": "你看起来神采奕奕，准备好迎接精彩的一天了。"},
                {"en": "Let us walk together down to the kitchen table.", "cn": "让我们一起手牵手走到餐桌旁去吧。"}
            ]
        },
        {
            "title": "第2章：美味营养的早餐时光",
            "description": "早餐点心、牛奶、水果与餐桌礼仪口语句型。",
            "sentences": [
                {"en": "What would you love to eat for breakfast today?", "cn": "今天早餐你想吃些什么美味的点心呀？"},
                {"en": "Would you like warm milk or fresh orange juice?", "cn": "你想喝温热的牛奶还是鲜榨的橙汁呢？"},
                {"en": "Here is a freshly toasted slice of whole-wheat bread.", "cn": "这是一片刚烤好的全麦土司面包。"},
                {"en": "Spread sweet strawberry jam across the bread.", "cn": "把甜甜的草莓果酱均匀涂抹在面包上。"},
                {"en": "Be careful, the boiled egg is still very warm.", "cn": "小心一点哦，这颗刚煮好的鸡蛋还热乎着呢。"},
                {"en": "Peel the egg shell gently with your small fingers.", "cn": "用你的小手指轻轻把蛋壳剥下来。"},
                {"en": "Chew your food slowly before you swallow it.", "cn": "把食物慢慢嚼碎嚼细之后再吞下去哦。"},
                {"en": "Drink your milk to help your bones grow strong.", "cn": "把牛奶喝光光，这样小骨骼才能长得强壮。"},
                {"en": "Wipe your little mouth with a clean paper napkin.", "cn": "用干净的小餐巾纸擦一擦嘴巴。"},
                {"en": "Thank you for finishing all your yummy vegetables.", "cn": "谢谢你把碗里美味的绿色蔬菜全都吃光啦。"},
                {"en": "May I have another slice of sweet red apple, please?", "cn": "我可以再吃一片甜脆红苹果吗，谢谢？"},
                {"en": "Always remember to sit nicely at the dining table.", "cn": "在餐桌前要时刻记住坐得端端正正。"},
                {"en": "Say thank you to daddy for cooking breakfast.", "cn": "对亲手做早餐的爸爸真诚地说一声谢谢。"},
                {"en": "My little tummy is full and feeling very happy.", "cn": "我的小肚皮饱饱的，感觉开心极了。"},
                {"en": "Let us help clear the empty bowls away together.", "cn": "让我们一起动手把空碗筷收拾整理好吧。"}
            ]
        },
        {
            "title": "第3章：挑选衣服与整齐穿戴",
            "description": "穿衣服、系鞋带、戴帽子与天气匹配穿搭。",
            "sentences": [
                {"en": "Which cute t-shirt do you want to wear today?", "cn": "今天你想穿哪一件可爱的小T恤呢？"},
                {"en": "Put your head through the shirt opening first.", "cn": "先把小脑袋从领口里钻出来。"},
                {"en": "Slide your right arm into this sleeve smoothly.", "cn": "把你的右胳膊顺顺利利地伸进衣袖里。"},
                {"en": "Pull your soft pants up around your waist.", "cn": "把柔软舒服的小裤子提至腰间。"},
                {"en": "Fasten the buttons from the bottom to the top.", "cn": "从下往上逐一把小纽扣工整系好。"},
                {"en": "Put on your clean cotton socks on both feet.", "cn": "两只小脚丫分别穿上干净透气的棉线袜。"},
                {"en": "Step into your blue sneakers and fasten the straps.", "cn": "穿上你的蓝色运动鞋，把魔术贴粘牢。"},
                {"en": "Tie your shoelaces into a neat butterfly bow.", "cn": "把鞋带打成一个漂亮的蝴蝶结形状。"},
                {"en": "It is windy today, so take a warm zip-up jacket.", "cn": "今天外面风很大，带上一件保暖的拉链夹克。"},
                {"en": "Zip up your jacket all the way to your collar.", "cn": "把夹克的拉链一直拉到衣领的位置。"},
                {"en": "Put on your warm woolen gloves before stepping out.", "cn": "踏出门之前别忘了戴上你温暖的羊毛手套。"},
                {"en": "Your colorful outfit looks absolutely wonderful today.", "cn": "你今天这一身五彩斑斓的打扮简直太帅气了。"},
                {"en": "Check your backpack to make sure your water bottle is packed.", "cn": "检查一下你的小书包，确认水壶已经装好了。"},
                {"en": "Look in the mirror and give a proud wave.", "cn": "看一看穿衣镜，骄傲地挥挥小手。"},
                {"en": "Now we are totally prepared for the kindergarten bus.", "cn": "现在我们已经完全准备好去坐幼儿园校车啦。"}
            ]
        },
        {
            "title": "第4章：收拾书包与上学路上",
            "description": "上学准备、交通安全、与同伴老师打招呼。",
            "sentences": [
                {"en": "Pack your drawing crayons into the pencil case.", "cn": "把你的画画蜡笔装进文具盒里。"},
                {"en": "Put your favorite storybook into the front pocket.", "cn": "把你最喜欢的童话故事书放进书包前袋。"},
                {"en": "Remember to pack your clean handkerchief and tissue.", "cn": "记得带上干净的小手帕和纸巾。"},
                {"en": "Hold mommy's hand tightly when walking on the street.", "cn": "在马路上走的时候一定要紧紧握住妈妈的手。"},
                {"en": "Look both ways carefully before crossing the zebra path.", "cn": "过斑马线之前一定要先向左右仔细看清楚。"},
                {"en": "Red light means stop, and green light means go.", "cn": "红灯亮起要停步，绿灯亮起才可以通行。"},
                {"en": "Wave enthusiastically to the friendly school crossing guard.", "cn": "热情地向路口维护交通的护导员叔叔招招手。"},
                {"en": "The yellow school bus is honking cheerfully at us.", "cn": "黄色的校车正在欢快地按着喇叭呼唤我们。"},
                {"en": "Step onto the bus stairs carefully one by one.", "cn": "一步一个脚印稳稳地踏上校车的台阶。"},
                {"en": "Find your assigned seat and buckle your seatbelt securely.", "cn": "找到指定的座位，把安全带牢牢扣好。"},
                {"en": "Wave goodbye through the window to your parents.", "cn": "透过车窗向窗外的爸爸妈妈微笑着挥手告别。"},
                {"en": "Say a cheerful hello to your classmates on the bus.", "cn": "向车上的同班小同学们亲切地打个招呼。"},
                {"en": "Look at the colorful shops rolling past outside.", "cn": "看着窗外一家家色彩鲜艳的小店铺飞驰而过。"},
                {"en": "Here we are arriving safely at the kindergarten.", "cn": "看，我们已经平安顺利抵达幼儿园大门口啦。"},
                {"en": "Greet your teacher with a clear and polite voice.", "cn": "用洪亮有礼貌的声音向迎上来的老师问好。"}
            ]
        },
        {
            "title": "第5章：幼儿园里的趣味活动",
            "description": "手工折纸、拼图积木、音乐舞蹈与课堂互动。",
            "sentences": [
                {"en": "Let us sit together in a warm circle on the carpet.", "cn": "让我们一起围成一个温暖的圆圈坐在地毯上。"},
                {"en": "Today our teacher is going to read a magical tale.", "cn": "今天老师要为大家朗读一个奇幻的魔法故事。"},
                {"en": "Raise your right hand if you know the right answer.", "cn": "如果你知道正确的答案，请举起你的右手。"},
                {"en": "Take turns to share your ideas with other children.", "cn": "轮流和其他小朋友分享你脑海中的奇思妙想。"},
                {"en": "Let us build a tall castle using colored wooden blocks.", "cn": "让我们用五颜六色的积木搭建一座高高的城堡。"},
                {"en": "Be careful not to let the tall tower tumble over.", "cn": "小心一点哦，别让高耸的积木塔倒塌了。"},
                {"en": "Cut the colored paper carefully along the dotted line.", "cn": "沿着虚线小巧而认真地剪裁彩纸。"},
                {"en": "Use non-toxic glue to stick the bright paper flowers.", "cn": "用无毒的胶棒把鲜艳的纸花牢牢粘贴好。"},
                {"en": "Wash your hands thoroughly with soap after painting.", "cn": "画完水彩画之后，要用洗手液把双手洗得干干净净。"},
                {"en": "Sing along to the joyful rhythm of the kindergarten song.", "cn": "伴随着幼儿园欢快的节拍一起引吭高歌。"},
                {"en": "Clap your hands twice and stomp your little feet.", "cn": "拍两下手掌，然后欢快地跺一跺双脚。"},
                {"en": "Spin around once and strike a funny freeze pose.", "cn": "原地转个圈，然后摆出一个滑稽的定格姿势。"},
                {"en": "Share your favorite coloring crayons with your desk partner.", "cn": "和你同桌的小伙伴一起分享彩笔。"},
                {"en": "Everyone clapped proudly for the great artwork.", "cn": "大家纷纷为这幅出色的集体画作热烈鼓掌。"},
                {"en": "Help the teacher collect all the drawing tools neatly.", "cn": "帮助老师把所有的绘画工具整齐地收回盒中。"}
            ]
        },
        {
            "title": "第6章：户外乐园与游乐场嬉戏",
            "description": "秋千、滑梯、跷跷板、捉迷藏与同伴友爱。",
            "sentences": [
                {"en": "It is outdoor playtime under the sunny blue sky.", "cn": "现在是晴空万里下的户外自由游戏时间啦。"},
                {"en": "Wait patiently in line for your turn on the slide.", "cn": "在滑梯前耐心地排好队，轮到自己再上去。"},
                {"en": "Hold on to the handrails tightly as you climb up.", "cn": "当你往上攀爬时，双手一定要牢牢抓紧扶手。"},
                {"en": "Whoosh! Sliding down fast brings endless giggles.", "cn": "嗖！飞快地滑下溜滑梯，带来阵阵欢笑。"},
                {"en": "Push me gently on the big swing, higher and higher.", "cn": "在秋千上轻轻推我一把吧，荡得更高一点。"},
                {"en": "I feel like I am flying up to touch the clouds.", "cn": "我感觉自己仿佛飞到了半空，能够摸到云彩。"},
                {"en": "Let us balance together on the colorful seesaw.", "cn": "让我们一起在彩色的跷跷板上保持平衡吧。"},
                {"en": "Up we go into the air, and down we glide to earth.", "cn": "我们忽而腾空而起，忽而缓缓降落地面。"},
                {"en": "Who wants to play hide-and-seek behind the big trees?", "cn": "有谁想在大树后面玩捉迷藏的游戏呀？"},
                {"en": "Cover your eyes with your hands and count to twenty.", "cn": "用双手蒙住双眼，大声数到二十。"},
                {"en": "Ready or not, here I come to look for you!", "cn": "藏好了没有呀，我要来找你们啦！"},
                {"en": "I found you hiding behind the wooden garden bench.", "cn": "我找到你啦，你就藏在花园的长木椅后面。"},
                {"en": "Run across the green grass without stumbling down.", "cn": "奔跑在青青的草坪上，注意脚下别摔倒了。"},
                {"en": "Help up your friend if they accidentally fall over.", "cn": "如果小伙伴不小心跌倒了，赶快伸手扶他起来。"},
                {"en": "Playtime is always so full of sunshine and laughter.", "cn": "户外游戏的时光总是充溢着无尽的阳光与欢声笑语。"}
            ]
        },
        {
            "title": "第7章：温馨午睡与美梦时刻",
            "description": "脱鞋、盖小被子、听睡前故事与小憩充电。",
            "sentences": [
                {"en": "After running and playing, our bodies need some rest.", "cn": "奔跑玩耍过后，我们的小身体需要好好休息啦。"},
                {"en": "Take off your shoes and place them neatly in the cubby.", "cn": "脱下你的鞋子，整整齐齐地摆放在鞋柜格子里。"},
                {"en": "Lie down quietly on your soft kindergarten cot.", "cn": "安静地平躺在你柔软舒适的午睡小床上。"},
                {"en": "Pull the cozy fleece blanket up over your shoulders.", "cn": "拉起保暖的抓绒小毯子，轻轻盖过你的肩头。"},
                {"en": "Hug your soft plush teddy bear in your arms.", "cn": "把你毛茸茸的小泰迪熊紧紧抱在怀里。"},
                {"en": "Close your sleepy eyes and listen to gentle music.", "cn": "轻轻闭上困倦的双眼，倾听舒缓轻柔的催眠曲。"},
                {"en": "The teacher draws the curtains to dim the sunlight.", "cn": "老师把窗帘轻轻拉上，遮挡住刺眼的阳光。"},
                {"en": "Breathe softly in and out as you drift to sleep.", "cn": "随着轻柔平稳的呼吸，缓缓沉入香甜的梦乡。"},
                {"en": "Dream of flying with sweet colorful butterflies.", "cn": "在美梦里和五彩斑斓的美丽蝴蝶一起翩翩起舞。"},
                {"en": "Dream of sailing a wooden boat across calm seas.", "cn": "在梦境中驾驶着一叶木舟横渡平静无波的蔚蓝大海。"},
                {"en": "Sleep gives your brain energy to learn and play more.", "cn": "充足的睡眠赋予大脑充沛的精力去学习和游戏。"},
                {"en": "The room is quiet and peaceful like a serene forest.", "cn": "整个房间宁静安详，宛如一处与世隔绝的静谧森林。"},
                {"en": "Wake up refreshed when the bell chimes softly.", "cn": "当温和的铃声轻柔响起时，精神饱满地醒来。"},
                {"en": "Fold your little blanket into a neat square shape.", "cn": "把你的小毯子整整齐齐地叠成一块小方块。"},
                {"en": "Put on your shoes and get ready for afternoon fun.", "cn": "穿好小鞋子，准备迎接丰富多彩的下午时光。"}
            ]
        },
        {
            "title": "第8章：下午茶点与分享之美",
            "description": "小点心、水果拼盘、清洗小手与友善分享。",
            "sentences": [
                {"en": "It is afternoon snack time for all good children.", "cn": "现在是所有乖宝宝们享用下午美味茶点的时间啦。"},
                {"en": "First, let us sing the soap-and-water washing song.", "cn": "首先，让我们唱起肥皂洗手的欢快小歌。"},
                {"en": "Rub your palms and wash between all your fingers.", "cn": "搓洗你的手心，仔仔细细把每个手指缝洗干净。"},
                {"en": "Dry your hands thoroughly under the warm air dryer.", "cn": "把手放到暖风烘手机下面完全烘干。"},
                {"en": "Today we have sweet bananas and crispy whole crackers.", "cn": "今天我们有香甜软糯的香蕉和酥脆可口的全麦饼干。"},
                {"en": "Please pass a cracker to your neighbor sitting beside you.", "cn": "请把一块香脆饼干递给你身旁坐着的小同桌。"},
                {"en": "Sharing good food makes everything taste twice as sweet.", "cn": "和小伙伴分享美食会让一切尝起来加倍甘甜。"},
                {"en": "Drink your freshly made apple juice sip by sip.", "cn": "一口一口小口小口地品尝这杯现榨的苹果汁。"},
                {"en": "No running around while you have food in your mouth.", "cn": "嘴里有食物的时候绝对不可以四处乱跑乱跳哦。"},
                {"en": "Eat neatly without dropping crumbs onto the carpet.", "cn": "吃点心时要规规整整，不要把碎屑掉在地毯上。"},
                {"en": "Can I have some more water, please, dear teacher?", "cn": "亲爱的老师，我可以再喝一点温水吗，谢谢？"},
                {"en": "Thank you for the delicious and refreshing snacks.", "cn": "非常感谢老师为我们准备的这顿美味可口的点心。"},
                {"en": "Throw the fruit peel into the green trash bin.", "cn": "把吃剩下的香蕉皮扔进绿色的分类垃圾桶里。"},
                {"en": "Wipe the table clean with a damp sponge cloth.", "cn": "用湿润的海绵抹布把小餐桌擦得锃亮发光。"},
                {"en": "You are a very responsible and caring little helper.", "cn": "你真是一个有责任心又体贴入微的得力小帮手。"}
            ]
        },
        {
            "title": "第9章：傍晚回家与玩具归位",
            "description": "整理玩具、分类归纳、晚饭与家庭欢聚。",
            "sentences": [
                {"en": "Look at the clock, it is time to pack up for home.", "cn": "看一看墙上的挂钟，到了收拾妥当准备回家的时间啦。"},
                {"en": "Put all the wooden toy blocks back into their wooden box.", "cn": "把所有散落的木质积木重新归类放回木盒子里。"},
                {"en": "Stack the storybooks neatly on the low library shelf.", "cn": "把图画绘本整齐有序地叠放在低矮的书架上面。"},
                {"en": "Return the colored pencils to the pencil holder.", "cn": "把彩色铅笔逐一插回笔筒里摆放端正。"},
                {"en": "Pick up your jacket and backpack from your personal locker.", "cn": "从你个人的小储物柜里取出你的夹克衫和小书包。"},
                {"en": "Check underneath the chair to make sure nothing is left.", "cn": "低头检查一下椅子底下，确认没有遗忘任何个人物品。"},
                {"en": "Daddy and mommy are waiting outside with open arms.", "cn": "爸爸和妈妈正站在门外张开双臂等候着你呢。"},
                {"en": "Run over and give them the biggest warmest hug.", "cn": "欢快地飞奔过去，给他们一个世上最大的拥抱。"},
                {"en": "Tell them all the wonderful things you learned today.", "cn": "向他们细数你今天在学校学到的所有神奇好玩的事。"},
                {"en": "We made pretty paper lanterns and sang a new tune.", "cn": "我们动手做出了漂亮的纸灯笼，还学唱了一首新歌。"},
                {"en": "Say goodbye to your teacher until tomorrow morning.", "cn": "向你的老师挥手道别，明天清晨咱们再见。"},
                {"en": "Hold hands warmly as you walk home together.", "cn": "手拉着手，洋溢着暖暖的温情一起走在回家的路上。"},
                {"en": "The evening sunset paints the wide sky in orange hues.", "cn": "傍晚绚丽的晚霞把辽阔的天空染成了醉人的橘红色。"},
                {"en": "I love my happy family more than all the stars.", "cn": "我爱我快乐的温馨小家，胜过夜空中所有的繁星。"},
                {"en": "Let us hurry home to enjoy a delicious warm dinner.", "cn": "让我们加快脚步赶回家，享用香气四溢的丰盛晚餐吧。"}
            ]
        },
        {
            "title": "第10章：洗澡刷牙与晚安物语",
            "description": "泡泡浴、刷牙换睡衣、睡前故事与甜美晚安。",
            "sentences": [
                {"en": "The warm bath water is filled with fluffy white bubbles.", "cn": "温热的洗澡水里漂浮着白茫茫、软绵绵的泡泡。"},
                {"en": "Play with the little yellow rubber duck in the tub.", "cn": "在大浴缸里和那只黄色的小橡皮鸭子一起戏水玩耍。"},
                {"en": "Wash your hair with gentle tear-free shampoo.", "cn": "用温和不刺激双眼的儿童洗发水清洗头发。"},
                {"en": "Wrap yourself in a giant fluffy bath towel.", "cn": "把自己严严实实裹进那条巨大的毛茸茸浴巾里。"},
                {"en": "Put on your soft, clean dinosaur pajamas.", "cn": "穿上你那套柔软干净、印着小恐龙的睡衣。"},
                {"en": "Brush every tooth carefully so no cavities appear.", "cn": "仔仔细细刷好每一颗牙齿，不给小蛀虫留任何可乘之机。"},
                {"en": "Climb into your comfortable bed beneath the warm quilt.", "cn": "钻进暖融融的被窝，舒舒服服地躺在大床上。"},
                {"en": "Pick one enchanting bedtime story for us to read.", "cn": "挑一本引人入胜的睡前故事书，咱们一起来读吧。"},
                {"en": "Once upon a time in a faraway magical kingdom...", "cn": "从前在很遥远很遥远的一个奇妙魔法王国里……"},
                {"en": "The brave little prince made friends with a kind dragon.", "cn": "勇敢的小王子和一条善良温和的飞龙结为了挚友。"},
                {"en": "Your eyes are growing heavier and heavier now.", "cn": "你的小眼皮现在变得越来越沉、越来越想睡觉啦。"},
                {"en": "Mommy kisses your forehead with endless tender love.", "cn": "妈妈俯下身子，带着无尽的温情轻吻你的额头。"},
                {"en": "Switch off the big lamp and leave the tiny nightlight on.", "cn": "关掉大吊灯，只留下一盏温馨微弱的小夜灯。"},
                {"en": "Sleep tight, sweet dreams, and see you tomorrow morning.", "cn": "睡个好觉，做个甜甜的美梦，明天早上见。"},
                {"en": "I love you to the moon and back forever.", "cn": "我对你的深爱，像横跨地球与月球的距离那样永恒绵长。"}
            ]
        }
    ]
}

COURSE_KIDS_FAIRYTALE = {
    "meta": {
        "id": "kids-fairytale",
        "title": "迪士尼经典童话双语小剧场",
        "category": "kids",
        "categoryName": "少儿英语",
        "coverGradient": "from-purple-400 to-pink-500",
        "icon": "🏰",
        "description": "精选白雪公主、灰姑娘、小红帽、丑小鸭等传世童话，用纯正生动的浅显英文演绎经典，点燃少儿想象力。",
        "difficulty": "beginner",
        "tags": ["少儿英语", "童话故事", "经典绘本", "睡前故事"]
    },
    "chapters": [
        {
            "title": "第1章：白雪公主与七个小矮人",
            "description": "经典童话白雪公主、魔镜与森林小木屋的梦幻启程。",
            "sentences": [
                {"en": "Once upon a time, a lovely princess was born with skin as white as snow.", "cn": "从前，一位可爱的公主降生了，她的皮肤如雪花一般纯白洁净。"},
                {"en": "Everyone in the whole kingdom called her Princess Snow White.", "cn": "整个王国的子民都亲切地称呼她为白雪公主。"},
                {"en": "The jealous queen had a magical mirror on her wall.", "cn": "心怀嫉妒的王后墙上挂着一面会说话的神奇魔镜。"},
                {"en": "Mirror, mirror on the wall, who is the fairest of them all?", "cn": "墙上的魔镜啊魔镜，谁才是世间最美丽的女子？"},
                {"en": "The truth-telling mirror replied that Snow White was the fairest.", "cn": "从不撒谎的魔镜如实回答，白雪公主才是世上最美丽的人。"},
                {"en": "Frightened by the queen, Snow White ran into the deep forest.", "cn": "受惊的白雪公主一路奔逃，跑进了深邃茂密的森林深处。"},
                {"en": "Friendly woodland animals guided her to a tiny cozy cottage.", "cn": "林间友善的小动物们指引着她，来到了一座温馨小巧的木屋前。"},
                {"en": "Inside the cottage stood seven small chairs and seven little beds.", "cn": "木屋里面摆放着七把小椅子和七张小巧精致的床。"},
                {"en": "Snow White cleaned the dusty tables and fell fast asleep.", "cn": "白雪公主擦洗干净落满灰尘的桌椅，随后甜甜地睡着了。"},
                {"en": "Seven hard-working dwarfs returned home from the diamond mine.", "cn": "七个辛勤劳作的小矮人从钻石矿井收工回到了家中。"},
                {"en": "They gasped in surprise to find a sleeping beauty in their room.", "cn": "他们惊奇地倒吸一口气，发现自己房间里躺着一位熟睡的佳人。"},
                {"en": "Snow White awoke and smiled warmly at the friendly dwarfs.", "cn": "白雪公主醒了过来，对着善良的小矮人们露出了温暖的微笑。"},
                {"en": "They welcomed her joyfully to live safely in their woodland home.", "cn": "他们欣喜若狂地欢迎她留下来，在森林小木屋里平安生活。"},
                {"en": "Singing and dancing filled the cozy forest cottage every evening.", "cn": "每个夜晚，小木屋里都充盈着欢快的歌声与翩翩的舞姿。"},
                {"en": "True kindness and love protected Snow White from all wickedness.", "cn": "纯真无邪的善意与爱心，保护着白雪公主远离一切邪恶险阻。"}
            ]
        },
        {
            "title": "第2章：灰姑娘与水晶鞋奇迹",
            "description": "辛德瑞拉的善良、仙女教母与午夜钟声的奇妙传说。",
            "sentences": [
                {"en": "Cinderella was a gentle and kind girl who worked hard every day.", "cn": "灰姑娘是个性情温柔善良的女孩，每天都勤勤恳恳地操劳家务。"},
                {"en": "Though her stepmother was unkind, Cinderella remained hopeful and cheerful.", "cn": "尽管继母待她十分苛刻，灰姑娘却依然心怀希望、笑对生活。"},
                {"en": "The royal prince invited all young maidens to a grand palace ball.", "cn": "王室的英俊王子向全国所有妙龄少女发出了盛大宫廷舞会的请柬。"},
                {"en": "Cinderella wept softly because she had no lovely dress to wear.", "cn": "灰姑娘悄悄抽泣起来，因为她连一件拿得出手的体面礼服都没有。"},
                {"en": "Suddenly, a sparkling fairy godmother appeared before her eyes.", "cn": "刹那间，一位周身泛着璀璨星光的仙女教母赫然出现在她眼前。"},
                {"en": "With a wave of her magic wand, a pumpkin became a golden carriage.", "cn": "随着魔法棒的轻轻一挥，一颗大南瓜转眼间变成了一辆金光闪闪的马车。"},
                {"en": "Four little mice transformed into four majestic white horses.", "cn": "四只不起眼的小老鼠幻化成了四匹威风凛凛的白色骏马。"},
                {"en": "Cinderella's ragged clothes changed into a dazzling silk ballgown.", "cn": "灰姑娘身上破旧的衣衫瞬间变成了一袭耀眼夺目的真丝舞会盛装。"},
                {"en": "On her feet shone a pair of exquisite glass slippers.", "cn": "她的脚上穿上了一双晶莹剔透、精美绝伦的水晶鞋。"},
                {"en": "Remember, the magic spell breaks when the clock strikes twelve!", "cn": "一定要牢记，当时钟敲响午夜十二点时，魔法便会全部失效！"},
                {"en": "At the grand ball, the prince danced exclusively with Cinderella.", "cn": "在盛大的舞会上，王子只邀请了灰姑娘一人共舞。"},
                {"en": "As the midnight bells chimed, Cinderella hurried down the palace stairs.", "cn": "当午夜钟声敲响之际，灰姑娘慌慌张张地跑下了宫殿的长阶。"},
                {"en": "In her great rush, she left behind a sparkling glass slipper.", "cn": "在万分仓皇之中，她不慎遗落了一只闪闪发亮的水晶鞋。"},
                {"en": "The prince traveled across the whole kingdom searching for its owner.", "cn": "王子踏遍了整个王国的每一寸土地，苦苦寻觅水晶鞋真正的主人。"},
                {"en": "The glass slipper fit Cinderella perfectly, and they lived happily ever after.", "cn": "水晶鞋与灰姑娘的脚严丝合缝，自此他们幸福美满地生活在了一起。"}
            ]
        },
        {
            "title": "第3章：小红帽与神秘大森林",
            "description": "小红帽穿过森林看望外婆的寓言故事与警示。",
            "sentences": [
                {"en": "Little Red Riding Hood loved wearing her bright crimson velvet cloak.", "cn": "小红帽最喜欢穿她那件鲜艳夺目的深红色丝绒斗篷。"},
                {"en": "Her mother packed a basket of fresh bread and berry jam.", "cn": "母亲为她打点好了一篮新鲜的面包和自制的浆果果酱。"},
                {"en": "Take this nourishing food to your grandmother who feels unwell.", "cn": "把你篮子里的这些滋补点心带给身体欠佳的外婆尝尝。"},
                {"en": "Stay on the straight path and never talk to strangers.", "cn": "一定要走在大路上，千万别和半路上遇到的陌生人搭讪。"},
                {"en": "The forest was filled with singing birds and colorful wildflowers.", "cn": "茂密的森林里处处回荡着鸟儿的鸣啭，盛开着五颜六色的野花。"},
                {"en": "A sly wolf watched the girl from behind a leafy oak.", "cn": "一只狡猾的大灰狼躲在一棵枝繁叶茂的橡树后面偷偷窥视着小女孩。"},
                {"en": "Good morning, little girl, where are you going on this sunny day?", "cn": "早上好啊，小姑娘，在这个阳光明媚的好天气里你要去向何方？"},
                {"en": "I am going to visit my dear grandmother on the other side of woods.", "cn": "我要穿过这片树林，去探望住在对面的亲爱外婆。"},
                {"en": "The sneaky wolf ran fast ahead to grandmother's wooden cabin.", "cn": "狡诈的大灰狼飞快地抄近路奔跑，直奔外婆居住的林间小木屋。"},
                {"en": "A brave and watchful woodsman was chopping timber nearby.", "cn": "一位英勇警觉的樵夫当时正在离木屋不远的近处砍伐木料。"},
                {"en": "When Red Riding Hood arrived, she noticed grandmother looked very unusual.", "cn": "当小红帽走进木屋时，她猛然察觉外婆的长相显得十分怪异。"},
                {"en": "Grandmother, what extraordinarily big ears and sharp teeth you have!", "cn": "外婆，您的耳朵怎么这么大，牙齿怎么长得如此尖锐呀！"},
                {"en": "Hearing her frightened scream, the noble woodsman rushed into the room.", "cn": "听到小红帽惊恐的呼救声，高尚勇敢的樵夫立刻破门而入冲进屋内。"},
                {"en": "He chased the greedy wolf far away into the darkest mountains.", "cn": "他一举把贪婪凶恶的大灰狼远远赶进了最幽深偏僻的荒山野岭。"},
                {"en": "Red Riding Hood learned to always obey her mother's wise advice.", "cn": "小红帽从此懂得了要时刻听从母亲饱含智慧的谆谆叮嘱。"}
            ]
        },
        {
            "title": "第4章：丑小鸭与白天鹅的蜕变",
            "description": "丑小鸭饱经冷眼挫折，终成优雅白天鹅的励志篇章。",
            "sentences": [
                {"en": "Near an ancient farmyard, a mother duck waited for her eggs to hatch.", "cn": "在一处古老农庄的池塘边，鸭妈妈满怀期待地等待着鸭蛋孵化。"},
                {"en": "One by one, adorable yellow ducklings cracked open their shells.", "cn": "一只又一只惹人怜爱的小黄鸭破壳而出，钻出了蛋壳。"},
                {"en": "The largest egg took much longer than all the rest.", "cn": "然而最大的一颗蛋孵化的时间却比其他所有的蛋都要漫长得多。"},
                {"en": "Out stepped a clumsy, gray bird with awkward giant feet.", "cn": "最终钻出来的是一只笨拙灰暗、长着一双巨大蹼足的怪鸟。"},
                {"en": "The other farmyard animals made fun of his unusual feathers.", "cn": "农庄里的其他小动物纷纷嘲笑他那身奇特难看的灰色羽毛。"},
                {"en": "They called him the Ugly Duckling and chased him away.", "cn": "他们刻薄地叫他丑小鸭，毫不留情地把他赶出了家园。"},
                {"en": "The lonely duckling swam across cold rivers during the freezing winter.", "cn": "在冰封大地的漫长寒冬里，形单影只的丑小鸭孤独地游过冰冷的河流。"},
                {"en": "He suffered through frosty winds and hidden dangers with patience.", "cn": "他以坚韧不拔的耐性，独自硬扛过凛冽刺骨的寒风与潜伏的凶险。"},
                {"en": "When gentle spring arrived, warm sunshine melted the thick ice.", "cn": "当温煦柔和的春姑娘降临人间，明媚的暖阳融化了厚厚的坚冰。"},
                {"en": "A flock of magnificent, snow-white swans landed on the water.", "cn": "一群体态婀娜、通体雪白的高贵天鹅从天而降，降落在碧波荡漾的水面上。"},
                {"en": "The poor duckling bent his head low toward the clear stream.", "cn": "可怜的丑小鸭自卑地将头深深埋向清澈如镜的溪流。"},
                {"en": "To his utter astonishment, his reflection was no longer gray or awkward.", "cn": "令他万分震惊的是，水中的倒影再也不是那只笨拙丑陋的灰鸟。"},
                {"en": "He had transformed into a graceful, breathtakingly beautiful swan.", "cn": "他竟然不知不觉蜕变成了一只体态高贵、美得惊心动魄的白天鹅。"},
                {"en": "The other swans circled around him, welcoming their magnificent new brother.", "cn": "其他天鹅纷纷环绕在他身旁，热情洋溢地接纳这位英俊非凡的新伙伴。"},
                {"en": "Never judge someone before seeing the beauty blooming from within.", "cn": "永远不要轻率评判任何人，直到看见他们灵魂深处绽放出的至美光华。"}
            ]
        },
        {
            "title": "第5章：睡美人与玫瑰荆棘庄园",
            "description": "奥罗拉公主、沉睡魔咒与真爱破晓的经典咏流传。",
            "sentences": [
                {"en": "The king and queen celebrated the joyful birth of Princess Aurora.", "cn": "国王和王后举国欢庆奥罗拉小公主的平安降生。"},
                {"en": "Three benevolent fairies gifted her with beauty, song, and sweet grace.", "cn": "三位心怀慈爱的仙子分别赠予她惊世容颜、天籁歌喉与优雅气质。"},
                {"en": "A wicked fairy cast a dark spell over the innocent child.", "cn": "然而邪恶的女巫却对无辜的女婴施下了一道阴森可怖的诅咒。"},
                {"en": "She declared that Aurora would prick her finger on a spinning wheel.", "cn": "女巫恶狠狠地宣称，奥罗拉有朝一日必将被纺车的针尖刺破手指。"},
                {"en": "A kind fairy altered the spell into a peaceful hundred-year slumber.", "cn": "一位善良的仙子巧妙更改了魔咒，将其化为一场长达百年的安详沉睡。"},
                {"en": "On her sixteenth birthday, the prediction sadly came to pass.", "cn": "在她十六岁生日那天，可怕的预言不幸残酷地应验了。"},
                {"en": "The beautiful princess fell asleep, along with the entire castle.", "cn": "绝色倾城的公主陷入了沉睡，整座古老城堡的一切生灵也一同沉睡过去。"},
                {"en": "Thick briars and fragrant wild roses grew to protect the fortress.", "cn": "茂密的荆棘与芬芳的野玫瑰拔地而起，将整座城堡固若金汤地环护在内。"},
                {"en": "Many decades passed while legends of the sleeping beauty spread far.", "cn": "几十年光阴荏苒，睡美人的神秘传奇故事传遍了千山万水。"},
                {"en": "A brave prince rode through the treacherous thorn bushes fearless of pain.", "cn": "一位英勇无畏的王子骑着战马穿透危机四伏的荆棘丛，浑然不惧皮肉之苦。"},
                {"en": "He climbed the spiral stairs and found the peaceful princess resting.", "cn": "他沿着旋转石阶拾级而上，终于见到了那位安详静卧的绝世公主。"},
                {"en": "He knelt gently beside her and kissed her pale cheek.", "cn": "他在床前轻柔跪下，满怀深情地亲吻了她那苍白的面颊。"},
                {"en": "The hundred-year curse shattered instantly like fragile glass.", "cn": "长达百年的恶毒诅咒刹那间如脆弱的琉璃般粉碎瓦解。"},
                {"en": "Aurora opened her sparkling eyes and smiled into his loving gaze.", "cn": "奥罗拉缓缓睁开明眸，迎着他满含深情的凝视绽放笑颜。"},
                {"en": "The whole kingdom awakened to a glorious dawn of everlasting joy.", "cn": "整座王国从沉睡中全然苏醒，迎来了一场永恒欢悦的璀璨破晓。"}
            ]
        },
        {
            "title": "第6章：三只小猪与勤劳盖房记",
            "description": "草屋、木屋与坚固砖房的劳动智慧寓言。",
            "sentences": [
                {"en": "Three cheerful little pigs set out into the world to build their homes.", "cn": "三只欢蹦乱跳的小猪踏上了闯荡世界的旅途，去建造属于自己的家园。"},
                {"en": "The first little pig was lazy and built his shack with light straw.", "cn": "第一只小猪生性懒惰，图省事用轻飘飘的稻草搭了一座简陋草棚。"},
                {"en": "The second little pig built his cabin quickly out of dry sticks.", "cn": "第二只小猪赶着去玩耍，匆匆忙忙用干燥的树枝拼成了一间木屋。"},
                {"en": "The third little pig worked diligently to lay solid brick upon brick.", "cn": "第三只小猪则勤勤恳恳，一块砖接着一块砖扎扎实实地砌造坚固砖房。"},
                {"en": "He mixed strong cement so his chimney stood firm and tall.", "cn": "他调配好坚硬的水泥，让自家的壁炉烟囱伫立得坚固挺拔。"},
                {"en": "A big hungry wolf came prowling around the straw cottage.", "cn": "一只饥肠辘辘的大灰狼蹑手蹑脚地在稻草小屋外四处徘徊张望。"},
                {"en": "Little pig, little pig, let me come inside your house!", "cn": "小猪啊小猪，快点开开门放我进屋去！"},
                {"en": "Not by the hair on my chinny chin chin, replied the pig.", "cn": "不行不行，连我下巴上的一根毛你都休想碰到，小猪大声回绝。"},
                {"en": "The wolf huffed and puffed and blew the straw house away.", "cn": "大灰狼猛吸一口气又用力一吹，直接把整座稻草房吹得无影无踪。"},
                {"en": "The first pig ran in terror to his brother's wooden cabin.", "cn": "第一只小猪吓得魂飞魄散，拼命奔向二哥的树枝小木屋。"},
                {"en": "The big bad wolf blew down the fragile stick house as well.", "cn": "恶狼故技重施，又一口气把脆弱不堪的树枝木屋给彻底吹垮了。"},
                {"en": "Both trembling pigs dashed into the third brother's brick residence.", "cn": "两只瑟瑟发抖的小猪急忙飞奔冲进了三弟坚固的砖头宅院里。"},
                {"en": "The wolf huffed and puffed until he was blue, but the brick walls stood unyielding.", "cn": "恶狼吸气吹气直到憋得满脸通红，坚不可摧的砖墙却依然纹丝不动。"},
                {"en": "He tried slipping down the chimney, but fell into a pot of boiling water.", "cn": "它妄图从烟囱偷偷溜进去，却扑通一声跌进了滚烫的开水锅里。"},
                {"en": "Honest hard work and patience build a fortress that withstands any storm.", "cn": "脚踏实地的勤劳汗水与无与伦比的坚韧，才能铸就经得起任何风暴的坚固堡垒。"}
            ]
        },
        {
            "title": "第7章：小美人鱼爱丽儿的海底心愿",
            "description": "探索神秘亚特兰蒂卡、人鱼歌喉与陆地世界的向往。",
            "sentences": [
                {"en": "Deep beneath turquoise waves lived Ariel, a curious mermaid princess.", "cn": "在碧蓝澄澈的波涛深处，住着一位名叫爱丽儿、对一切满怀好奇的人鱼公主。"},
                {"en": "She had flowing crimson hair and the sweetest singing voice in the sea.", "cn": "她有一头瀑布般的红色秀发，拥有全大海最甜美动听的天籁歌喉。"},
                {"en": "While her sisters loved pearl palaces, Ariel dreamed of the land above.", "cn": "尽管姐姐们沉醉于珍珠宫殿的奢华，爱丽儿心中却无时无刻不在憧憬着陆地。"},
                {"en": "She collected human treasures like forks and mirrors in her hidden grotto.", "cn": "她在自己的秘密岩洞里珍藏着叉子、镜子等各色人类生活的小物件。"},
                {"en": "Her wise companion Sebastian the crab warned her against surface dangers.", "cn": "她身边的睿智伙伴红蟹赛巴斯汀常常告诫她海面世界的凶险莫测。"},
                {"en": "One stormy night, a magnificent sailing ship wrecked upon sharp reef.", "cn": "在一个电闪雷鸣的风暴之夜，一艘华丽的帆船不幸在锋利的暗礁上触礁沉没。"},
                {"en": "Ariel swam swiftly into raging waters and rescued the unconscious prince.", "cn": "爱丽儿奋不顾身地游进狂暴汹涌的海浪，救起了陷入昏迷的年轻王子。"},
                {"en": "She pulled him safely onto warm golden sands and sang softly to him.", "cn": "她将他平安拖上温暖的金黄沙滩，俯在他身旁轻柔地唱起了动人情歌。"},
                {"en": "Before the prince opened his eyes, she dove back into ocean swells.", "cn": "就在王子缓缓睁开双眼的前一刹那，她依依不舍地潜回了浩瀚的海水之中。"},
                {"en": "The prince never forgot the enchanting melody that saved his life.", "cn": "王子从此终生难忘那曲拯救了他宝贵生命的绝美空灵之歌。"},
                {"en": "Ariel sacrificed her golden voice to gain human feet from sea witch.", "cn": "为了追寻心中的真爱，爱丽儿不惜向海巫献出天籁歌喉换取了一双人类的双腿。"},
                {"en": "Every step on land felt like walking over razor-sharp thorns.", "cn": "踩在干燥陆地上的每一步，都如同行走在刀锋针尖上一般剧痛难忍。"},
                {"en": "Yet her gentle smile and expressive eyes won the prince's heart completely.", "cn": "然而她那温柔坚定的微笑与会说话的灵动双眸，彻底打动了王子的心扉。"},
                {"en": "King Triton saw her pure devotion and blessed her human journey.", "cn": "川顿国王目睹了女儿矢志不渝的纯真挚爱，终于欣慰地为她的人间旅程送上祝福。"},
                {"en": "Love builds an unbreakable bridge between two completely different worlds.", "cn": "真挚深沉的爱，足以在两个截然不同的辽阔世界之间架起坚不可摧的心灵桥梁。"}
            ]
        },
        {
            "title": "第8章：木偶奇遇记与诚实的力量",
            "description": "匹诺曹、老木匠盖比特与长鼻子谎言的顿悟。",
            "sentences": [
                {"en": "Kindly carpenter Geppetto carved a puppet out of seasoned pine wood.", "cn": "慈祥的老木匠盖比特用一块风干的松木，雕刻出了一个精巧的小木偶。"},
                {"en": "He named the puppet Pinocchio and wished upon an evening star.", "cn": "他给木偶起名叫匹诺曹，并在夜空那一颗明亮的许愿星下许下了心愿。"},
                {"en": "The Blue Fairy arrived and breathed living breath into the wooden boy.", "cn": "蓝仙女悄然降临，向木偶男孩吹了一口赋予生命的灵气。"},
                {"en": "Prove yourself brave, truthful, and unselfish, and you will become a real boy.", "cn": "只要你能证明自己勇敢、诚实且无私，你就会变成一个真正的人类男孩。"},
                {"en": "Jiminy Cricket became Pinocchio's official conscience to guide his decisions.", "cn": "小蟋蟀吉米尼成为了匹诺曹的正式良知顾问，在关键抉择中指引他的方向。"},
                {"en": "Instead of going to school, Pinocchio was lured away by mischievous foxes.", "cn": "可匹诺曹非但没有去上学，反而被狡诈顽皮的狐狸诱骗拐走了。"},
                {"en": "Whenever Pinocchio told a lie, his wooden nose grew longer and longer.", "cn": "每当匹诺曹撒出一句谎言，他的木头长鼻子就会刷刷地变长好大一截。"},
                {"en": "He cried in embarrassment when branches sprouted from his very nose.", "cn": "当他的鼻尖上甚至长出了小嫩枝时，他羞愧万分地失声痛哭起来。"},
                {"en": "I promise to speak only the honest truth from now on, he cried.", "cn": "我向您保证，从今往后我一定只讲大实话，他抽泣着发誓。"},
                {"en": "Hearing his genuine repentance, the Blue Fairy restored his normal wooden nose.", "cn": "听到他发自肺腑的真诚忏悔，蓝仙女将他过长的鼻子恢复了原貌。"},
                {"en": "When Geppetto was swallowed by a monstrous whale, Pinocchio swam to rescue him.", "cn": "当得知老父亲盖比特被一头巨鲸吞入腹中时，匹诺曹义无反顾游入巨浪营救。"},
                {"en": "He built a smoky fire inside the whale's belly to trigger a giant sneeze.", "cn": "他在鲸鱼肚子里燃起滚滚浓烟，引发了巨鲸惊天动地的一记大喷嚏。"},
                {"en": "Father and son escaped safely on a raft through rolling stormy waves.", "cn": "父子俩乘着木筏，在狂风巨浪中化险为夷平安脱险。"},
                {"en": "Because he sacrificed himself to save his father, the Blue Fairy made him human.", "cn": "因为他舍生忘死救出了至亲父亲，蓝仙女欣慰地将他变成了真正的人类男孩。"},
                {"en": "Honesty, courage, and love are the greatest treasures a person can hold.", "cn": "诚实正直、无畏勇气与至纯爱意，是一个人此生所能拥有的最宝贵财富。"}
            ]
        },
        {
            "title": "第9章：阿拉丁神灯与飞毯奇缘",
            "description": "神灯精灵、三个愿望与少年阿拉丁的正义与勇气。",
            "sentences": [
                {"en": "In a sun-drenched desert marketplace lived a clever street boy named Aladdin.", "cn": "在一处阳光普照的荒漠集市里，住着一位聪明机智的流浪少年阿拉丁。"},
                {"en": "Accompanied by his pet monkey Abu, Aladdin shared his bread with hungry orphans.", "cn": "在宠物小猴阿布的陪伴下，阿拉丁慷慨地将自己仅有的口粮分给饥饿的孤儿。"},
                {"en": "An evil sorcerer tricked him into entering the Cave of Wonders.", "cn": "一个阴险的邪恶巫师诱骗阿拉丁，让他只身深入神秘莫测的奇迹洞穴。"},
                {"en": "Inside the cavern glowed heaps of glittering jewels and golden coins.", "cn": "洞穴深处堆积如山的璀璨珠宝与金币散发着令人目眩神迷的光辉。"},
                {"en": "On top of a stone pillar sat an old, dusty oil lamp.", "cn": "在一根耸立的石柱顶端，静静搁置着一盏布满灰尘的古老油灯。"},
                {"en": "When Aladdin rubbed the tarnished lamp, brilliant blue smoke billowed outward.", "cn": "当阿拉丁用衣角擦拭那盏昏暗的油灯时，一股绚烂夺目的蓝烟喷涌而出。"},
                {"en": "A giant, booming Genie appeared, ready to grant three magical wishes.", "cn": "一个身材魁梧、嗓音洪亮的神灯精灵显现出来，随时准备实现三个神奇心愿。"},
                {"en": "Aladdin asked to be transformed into a wealthy prince to woo Princess Jasmine.", "cn": "阿拉丁请求精灵将自己变成一位家财万贯的英俊王子，以此追求茉莉公主。"},
                {"en": "Together, Aladdin and Jasmine soared across midnight skies on a flying magic carpet.", "cn": "阿拉丁与茉莉公主坐上一张飞天魔毯，在午夜皎洁的星空下展翅翱翔。"},
                {"en": "A whole new world opened before their marveling eyes above palace minarets.", "cn": "一个崭新辽阔的宏大世界，在宫殿高耸的塔楼之上向他们震撼敞开。"},
                {"en": "Yet Aladdin soon discovered that false titles cannot buy genuine affection.", "cn": "然而阿拉丁很快领悟到，虚假的头衔根本换不来发自肺腑的真挚爱情。"},
                {"en": "He stood proudly as his true self and defeated the sorcerer's treacherous plot.", "cn": "他勇敢亮出自己真实的本色，最终彻底挫败了阴险巫师篡夺王位的诡计。"},
                {"en": "For his final wish, Aladdin selflessly set the loyal Genie free forever.", "cn": "在最后一个心愿面前，阿拉丁无私地许愿让忠诚陪伴的精灵永远重获自由。"},
                {"en": "The Sultan embraced Aladdin, declaring that nobility lies in the character, not wealth.", "cn": "苏丹国王深情拥抱了阿拉丁，盛赞高贵存在于崇高的人格之中而非财富。"},
                {"en": "True royalty is born of courage, integrity, and a generous heart.", "cn": "真正无可替代的高贵，永远孕育自无畏的勇气、坚守的正道与宽仁的胸怀。"}
            ]
        },
        {
            "title": "第10章：美女与野兽的真爱玫瑰",
            "description": "贝儿姑娘、被诅咒的古堡与穿透外貌的灵魂之美。",
            "sentences": [
                {"en": "In a peaceful French village lived Belle, a bright girl who adored reading books.", "cn": "在一座安宁祥和的法国小镇里住着贝儿，一位热爱读书、聪慧非凡的美丽姑娘。"},
                {"en": "Her father Maurice was an eccentric inventor who lost his way in a blizzard.", "cn": "她的父亲莫里斯是一位古怪的发明家，在暴风雪肆虐的荒野中迷失了方向。"},
                {"en": "Maurice took shelter inside a dark enchanted castle guarded by a roaring beast.", "cn": "莫里斯躲进了一座受魔法诅咒的阴暗古堡避难，却被咆哮的怪兽囚禁其中。"},
                {"en": "To save her elderly father, courageous Belle offered to take his place as prisoner.", "cn": "为了营救年迈体弱的慈父，勇敢坚强的贝儿毅然提出由自己代替父亲成为囚徒。"},
                {"en": "The Beast was once a haughty prince cursed by an enchantress for his cruelty.", "cn": "那头野兽曾是一位傲慢冷酷的王子，因缺乏仁爱之心被女巫施加了恶毒咒语。"},
                {"en": "A magical glass dome protected a glowing red rose with falling petals.", "cn": "一个魔法玻璃罩悉心保护着一朵娇艳欲滴、正逐片凋落花瓣的红色玫瑰。"},
                {"en": "If he could learn to love and earn love before the last petal fell, the curse would break.", "cn": "若能在最后一片花瓣凋零前学会去爱并赢得真爱，魔咒方能彻底解除。"},
                {"en": "Belle was enchanted by the palace's grand library with thousands of gilded volumes.", "cn": "贝儿被古堡内拥有数以万计烫金典籍的宏伟藏书馆深深震撼与吸引。"},
                {"en": "Underneath the Beast's frightening exterior beat a tender and lonely heart.", "cn": "在野兽令人胆寒的凶悍外表之下，实际上跳动着一颗渴望温情与孤独的心。"},
                {"en": "They shared quiet meals, fed winter birds, and danced in the grand ballroom.", "cn": "他们安详共进晚餐，在雪地里喂养小鸟，在宏大的舞厅内优雅起舞。"},
                {"en": "Tale as old as time, true tune as old as song, beauty within shines supreme.", "cn": "古老宛如岁月的传奇，真挚宛如歌谣的旋律，内在的纯美最终绽放无上光芒。"},
                {"en": "When a jealous hunter attacked the castle, the Beast defended Belle with his life.", "cn": "当心怀嫉妒的猎人率众围攻古堡时，野兽拼尽最后一口气以死捍卫贝儿的安全。"},
                {"en": "Weeping softly over the dying Beast, Belle whispered: I truly love you.", "cn": "伏在奄奄一息的野兽胸前，贝儿泪如雨下轻声倾诉：我发自内心深爱着你。"},
                {"en": "The final rose petal touched the stone, and golden light engulfed the entire tower.", "cn": "最后一片玫瑰花瓣轻触石台的瞬间，耀眼夺目的金光将整座钟楼彻底笼罩。"},
                {"en": "The Beast transformed into a handsome prince, proving that love conquers all darkness.", "cn": "野兽蜕变成了一位英俊非凡的王子，有力印证了真爱足以战胜一切世间黑暗。"}
            ]
        }
    ]
}

COURSE_KIDS_ANIMALS = {
    "meta": {
        "id": "kids-animals",
        "title": "奇妙动物王国大百科",
        "category": "kids",
        "categoryName": "少儿英语",
        "coverGradient": "from-lime-400 to-green-600",
        "icon": "🦁",
        "description": "走入大草原、热带雨林与极地冰原，探秘狮子、海豚、大熊猫、企鹅等野生动物习性与地道趣味英语表达。",
        "difficulty": "beginner",
        "tags": ["少儿英语", "自然科普", "动物百科", "趣味认知"]
    },
    "chapters": [
        {
            "title": "第1章：非洲草原百兽之王狮子",
            "description": "探索非洲草原、狮群家族与雄狮威严习性。",
            "sentences": [
                {"en": "The lion is known across the world as the majestic king of the jungle.", "cn": "狮子闻名于世，被世人尊称为威风凛凛的丛林之王。"},
                {"en": "Male lions boast a thick golden mane that protects their necks.", "cn": "雄狮拥有浓密金黄的威武鬃毛，能够在搏击中保护脖颈。"},
                {"en": "A family of lions living together is called a proud lion pride.", "cn": "生活在一起的狮子大家庭，在英文中被称作骄傲的狮群。"},
                {"en": "Lionesses are the chief hunters who coordinate skillfully across grassy plains.", "cn": "母狮是家族里的核心狩猎者，在大草原上配合得天衣无缝。"},
                {"en": "A lion's powerful roar can be heard five miles away in the distance.", "cn": "雄狮一声震撼天地的咆哮，甚至在五英里开外的远方都能听得一清二楚。"},
                {"en": "Lion cubs love tumbling and wrestling playfully with their siblings.", "cn": "小狮子们最喜欢和兄弟姐妹们一起打滚嬉闹、玩扑咬摔跤游戏。"},
                {"en": "Lions spend up to twenty hours a day resting under shady acacia trees.", "cn": "在遮阳的金合欢树下，狮子每天有长达二十个小时都在惬意打盹小憩。"},
                {"en": "Their golden amber eyes have exceptional night vision for stalking prey.", "cn": "他们琥珀色的金黄双眼拥有超凡的夜视能力，利于在夜幕中潜行跟踪。"},
                {"en": "A lion's padded paws allow it to sneak up completely silently.", "cn": "狮子脚下厚实柔软的肉垫，使它能够在接近猎物时做到完全悄无声息。"},
                {"en": "Zebras and antelopes stay constantly alert when lions are on the prowl.", "cn": "当狮子开始在旷野巡猎时，斑马和羚羊无不时刻处于高度警戒之中。"},
                {"en": "Lions are the only wild cat species that live in cooperative social groups.", "cn": "狮子是野生猫科动物中唯一一种过着群体互助社会化生活的动物。"},
                {"en": "Mother lions nurse and protect each other's young cubs tenderly.", "cn": "母狮们会温柔地彼此轮流喂哺和守护群落里所有年幼的小狮崽。"},
                {"en": "The golden savannah sunset outlines the magnificent silhouette of the lion.", "cn": "金灿灿的草原落日，勾勒出雄狮那令人肃然起敬的巍峨雄姿轮廓。"},
                {"en": "Wildlife conservation programs work tirelessly to preserve wild lion habitats.", "cn": "野生动物保护工程正在孜孜不倦地致力于保全野生狮子的天然栖息地。"},
                {"en": "Respect the raw power and untamed beauty of this African icon.", "cn": "让我们共同心怀敬畏，去尊重这头非洲传奇物种原始的伟力与野性之美。"}
            ]
        },
        {
            "title": "第2章：温顺巨兽非洲象与长鼻子",
            "description": "陆地最大哺乳动物、象群迁徙与母系社会智慧。",
            "sentences": [
                {"en": "The African elephant is the largest living land mammal on planet Earth.", "cn": "非洲象是当今地球上现存体型最为庞大的陆地哺乳动物。"},
                {"en": "An elephant's remarkable trunk contains over forty thousand separate muscles.", "cn": "大象神奇的长鼻子里，竟然包含着四万多块独立灵活的肌肉群。"},
                {"en": "They use their long trunks to breathe, drink, trumpet, and grasp objects.", "cn": "它们用长鼻子来呼吸、吸水、发出嘹亮的号角声以及抓取各种物体。"},
                {"en": "Large flapping ears help keep elephants cool beneath the blazing tropical sun.", "cn": "扑扇着如蒲扇般的大耳朵，能帮助大象在炎炎烈日下给身体降温。"},
                {"en": "Elephants live in tightly knit matriarchal families led by the oldest female.", "cn": "象群过着紧密团结的母系氏族生活，由年纪最大、经验最丰富的母象统领。"},
                {"en": "The wise matriarch remembers migration paths and hidden waterholes for decades.", "cn": "充满智慧的象群首领在长达数十年的岁月里，始终牢记迁徙路线与隐蔽水源。"},
                {"en": "Baby elephants love spraying themselves with cool water and mud baths.", "cn": "象宝宝特别喜欢用鼻子吸取清凉的水喷洒全身，或者痛痛快快洗个泥巴澡。"},
                {"en": "The dry mud creates a natural sunscreen that protects their thick skin.", "cn": "风干的泥浆在大象厚实的皮肤表面，形成了一层纯天然的防晒保护层。"},
                {"en": "Elephants communicate over vast distances using low-frequency seismic rumbles.", "cn": "大象能够利用人类耳朵听不到的超低频次声波震动，在超远距离外沟通交流。"},
                {"en": "These gentle giants display profound empathy, mourning their departed family members.", "cn": "这些温顺的庞然大物拥有深刻的同理心，甚至会围着逝去的家庭成员哀思默哀。"},
                {"en": "An adult elephant can consume hundreds of pounds of vegetation every single day.", "cn": "一头成年大象每天需要进食数百磅的草木枝叶来维持身体能量。"},
                {"en": "Their strong ivory tusks are actually elongated incisor teeth used for digging.", "cn": "它们坚硬的长象牙实际上是极度延长的门齿，常用于挖掘树根和水源。"},
                {"en": "Poaching has threatened elephant populations, prompting global protective bans.", "cn": "非法的偷猎曾严重威胁大象的生存繁衍，促成了全球性的严厉保护禁令。"},
                {"en": "Elephants play an indispensable role as ecosystem engineers in their wild habitats.", "cn": "在其原生栖息地中，大象扮演着不可或缺的生态系统工程师的关键角色。"},
                {"en": "Watching an elephant herd cross the river at dawn is an unforgettable sight.", "cn": "在破晓拂晓时分亲眼目睹整个象群列队横渡大河，是一幅毕生难忘的壮阔奇景。"}
            ]
        },
        {
            "title": "第3章：大熊猫的青竹家园与滚滚日常",
            "description": "中国国宝大熊猫、吃竹子、爬树与黑白毛皮奥秘。",
            "sentences": [
                {"en": "The giant panda is a beloved national treasure native to China's bamboo forests.", "cn": "大熊猫是人见人爱、原产于中国高山翠竹林里的国宝级动物。"},
                {"en": "Pandas are easily recognized worldwide by their distinctive black-and-white coats.", "cn": "大熊猫凭借其黑白分明的标志性毛色皮草，在全世界范围内赢得了极高的辨识度。"},
                {"en": "Black patches around their eyes make their expressions look adorably charming.", "cn": "眼睛周围那一圈黑黑的眼圈，让它们的憨态表情显得格外惹人怜爱。"},
                {"en": "A giant panda spends up to twelve hours a day munching on green bamboo.", "cn": "一只大熊猫每天有长达十二个小时的时间，都在津津有味地咀嚼着青翠的竹子。"},
                {"en": "Bamboo makes up more than ninety-nine percent of a wild panda's daily diet.", "cn": "翠竹占据了一只野生大熊猫日常全部膳食结构的百分之九十九以上。"},
                {"en": "They possess an enlarged wrist bone that functions like an opposable sixth thumb.", "cn": "它们的腕骨处长有一块特别增大的骨骼，功能宛如对生的第六根大拇指便于抓握竹枝。"},
                {"en": "Despite their chunky bodies, pandas are extraordinarily skilled at climbing tall trees.", "cn": "别看它们的身躯胖乎乎圆滚滚，大熊猫其实是一等一的爬树高手。"},
                {"en": "Young panda cubs love somersaulting down grassy slopes in playful joy.", "cn": "年幼的熊猫幼崽最爱在青青草坡上一溜烟翻滚着跟头，玩得不亦乐乎。"},
                {"en": "Newborn panda cubs are tiny, pink, and hairless, weighing just a few ounces.", "cn": "刚出生的熊猫宝宝身形极其娇小脆弱，通体粉红无毛，体重仅仅只有几盎司。"},
                {"en": "Mother pandas cradle their delicate infants with immense gentle devotion.", "cn": "熊猫妈妈会用宽大温柔的手臂将脆弱的幼崽搂入怀中，倾注无尽的舐犊深情。"},
                {"en": "Pandas have a round face shape due to powerful jaw muscles for chewing fiber.", "cn": "大熊猫之所以长着圆溜溜的大脸盘，是因为用来咀嚼坚硬竹纤维的咬肌极度发达。"},
                {"en": "China has created expansive national nature reserves to protect wild panda habitats.", "cn": "中国建立起了面积辽阔的国家级自然保护区，全方位保卫野生大熊猫的原生家园。"},
                {"en": "Global conservation efforts have successfully moved pandas off the endangered list.", "cn": "全球通力协作的保护成果，已经成功让大熊猫从濒危物种名录降级为易危。"},
                {"en": "Panda diplomacy has built bridges of friendship and goodwill among many nations.", "cn": "作为和平友好的文化使者，大熊猫外交在世界各国人民之间架起了坚固的友谊桥梁。"},
                {"en": "Every funny tumble of a chubby panda brings pure joy to visitors.", "cn": "胖嘟嘟的大熊猫每一次笨拙可爱的翻滚，都能给现场的游客带来最纯粹的快乐。"}
            ]
        },
        {
            "title": "第4章：南极冰原绅士小企鹅",
            "description": "极地严寒、企鹅抱团取暖与海洋潜水绝技。",
            "sentences": [
                {"en": "Penguins are flightless marine birds that live primarily in the icy Southern Hemisphere.", "cn": "企鹅是丧失了飞行能力的海洋鸟类，主要繁衍生息在冰天雪地的南半球极地地区。"},
                {"en": "Their sleek black-and-white plumage resembles a formal black tuxedo suit.", "cn": "它们光溜溜的黑白羽毛，酷似人类出席正式晚宴时所穿戴的黑色燕尾服。"},
                {"en": "Emperor penguins are the largest of all seventeen living penguin species.", "cn": "在现存全部十七种企鹅物种当中，帝企鹅是体型最为硕大魁梧的一种。"},
                {"en": "Penguins use their rigid, paddle-like flippers to fly gracefully underwater.", "cn": "企鹅利用其如坚硬划桨般的前肢双翼，在深水里如同优雅飞行一般破浪穿梭。"},
                {"en": "Dense waterproof feathers and thick layers of blubber keep them warm in freezing gales.", "cn": "极其浓密的防水羽毛与厚实的皮下脂肪层，使它们在刺骨的暴风雪中依然温暖如春。"},
                {"en": "Thousands of penguins huddle tightly together in colossal circles to block wind.", "cn": "成千上万只企鹅紧密地依偎挤在一起，形成庞大的圆圈来共同抵御极寒的狂风。"},
                {"en": "Penguins on the outer edge gradually rotate into the toasty warm center.", "cn": "处在寒风肆虐最外圈的企鹅，会循序渐进地轮换到温暖如蒸笼的核心区域。"},
                {"en": "A mother penguin lays a single egg and transfers it carefully to father's feet.", "cn": "企鹅妈妈产下一枚珍贵的蛋之后，会万分小心地将其转交至企鹅爸爸的脚背上。"},
                {"en": "The devoted father balances the egg beneath his warm brooding pouch for months.", "cn": "尽职尽责的企鹅爸爸将蛋稳稳托在脚背上，用温暖的腹部育儿褶包裹数月之久。"},
                {"en": "He endures freezing Antarctic blizzards without eating until the chick hatches.", "cn": "在企鹅幼鸟破壳孵化出来之前，企鹅爸爸顶着南极暴风雪滴水未进坚守岗位。"},
                {"en": "Penguins waddle awkwardly on land but toboggan quickly across slick snow on their bellies.", "cn": "企鹅在陆地上走起路来摇摇摆摆，但在光滑的冰雪上却能肚皮贴地飞速滑行。"},
                {"en": "They dive hundreds of meters deep into ocean waters to catch krill and silver fish.", "cn": "它们能够一口气潜入深达数百米的深邃大洋，捕食鲜美的磷虾和小银鱼。"},
                {"en": "Leopard seals and killer whales are the primary natural predators of adult penguins.", "cn": "海豹和凶猛的虎鲸，是成年企鹅在极地冰洋中面临的主要天敌。"},
                {"en": "Fluffy gray penguin chicks chirp loudly to identify their returning parents.", "cn": "毛茸茸的灰色小企鹅发出响亮的欢叫声，在千万群体中精准辨认归来的父母。"},
                {"en": "The resilience of penguins in the harshest climate on Earth inspires human hearts.", "cn": "企鹅在地球上最严酷极寒气候下展现出的超凡生命韧性，深深震撼着人类的心灵。"}
            ]
        },
        {
            "title": "第5章：深海精灵海豚的智慧之歌",
            "description": "海洋高智商哺乳动物、回声定位与跃水特技。",
            "sentences": [
                {"en": "Dolphins are extraordinarily intelligent marine mammals that belong to the whale family.", "cn": "海豚是属于鲸类家族的一员，是公认智商极高的高等海洋哺乳动物。"},
                {"en": "They breathe air through a single blowhole situated right on top of their heads.", "cn": "它们通过位于头顶正上方的一个单独喷气孔，在跃出水面时畅快呼吸空气。"},
                {"en": "Dolphins navigate murky waters and hunt fish using sophisticated biosonar echolocation.", "cn": "海豚利用极其精密复杂的生物声呐回声定位系统，在浑浊幽暗的深水中导航与捕鱼。"},
                {"en": "They emit clicking sounds that bounce off objects, revealing size, shape, and speed.", "cn": "它们发出的清脆咔哒声在碰到物体反弹而回时，能精准获悉物体的尺寸、形状与航速。"},
                {"en": "Bottlenose dolphins live in close cooperative pods that hunt and play together.", "cn": "宽吻海豚生活在紧密协作的群落当中，大家一同捕食猎物并嬉戏打闹。"},
                {"en": "Dolphins leap gracefully out of the water, performing breathtaking aerial acrobatics.", "cn": "海豚常常优雅地腾空跃出蔚蓝的海面，在半空中表演令人屏息赞叹的特技翻滚。"},
                {"en": "Scientists believe that leaping serves to communicate, shed parasites, or express sheer joy.", "cn": "科学家们推测，海豚跃水可能是为了远程交流、摆脱体表寄生虫或者纯粹宣泄喜悦。"},
                {"en": "Each dolphin has a unique signature whistle that acts just like a human name.", "cn": "每一只海豚都拥有一声属于自己的独门哨鸣声，其功能就宛如人类的姓名一样独特。"},
                {"en": "When a mother dolphin calls, her calf recognizes her specific whistle immediately.", "cn": "当海豚妈妈发出呼唤时，小海豚能够在一瞬间准确分辨出母亲特定的口哨音调。"},
                {"en": "Dolphins exhibit remarkable empathy, frequently rescuing injured comrades or even humans.", "cn": "海豚展现出了惊人的同理心与救助天性，屡次有托举保护受伤同伴甚至遇溺人类的壮举。"},
                {"en": "They sleep with only one hemisphere of their brain resting at a time.", "cn": "海豚在睡眠时每次只让半边大脑休息，另一边大脑保持警觉以随时浮出水面呼吸。"},
                {"en": "Their smooth rubbery skin reduces friction, allowing them to swim at incredible speeds.", "cn": "它们光滑如橡胶般的奇妙皮肤能大幅降低流体阻力，使它们能以惊人的高速飞驰。"},
                {"en": "Dolphins enjoy riding the bow waves created by large cargo ships and sailing yachts.", "cn": "海豚特别喜欢借着大型货轮和帆船船头激起的巨大浪涌，在波峰间惬意冲浪。"},
                {"en": "Protecting marine environments from plastic pollution ensures dolphins thrive safely.", "cn": "保护海洋环境免受塑料垃圾的污染毒害，是确保海豚家族平安繁衍的关键基石。"},
                {"en": "The playful smile of a swimming dolphin warms the hearts of ocean lovers everywhere.", "cn": "一只游弋海豚那仿佛与生俱来的欢快笑靥，温暖着大洋两岸每一位海洋爱好者的心。"}
            ]
        },
        {
            "title": "第6章：长颈鹿的云端视野与长颈奇观",
            "description": "世界上最高陆生动物、高枝采食与温顺性格。",
            "sentences": [
                {"en": "The giraffe is the tallest living terrestrial mammal roaming our natural world.", "cn": "长颈鹿是漫步在我们大自然世界里、现存身材最为高耸入云的陆生哺乳动物。"},
                {"en": "An adult male giraffe can stand up to nineteen feet above the grassy terrain.", "cn": "一头成年的雄性长颈鹿，其挺立的高度可达惊人的十九英尺之多。"},
                {"en": "Remarkably, a giraffe's long neck contains exactly seven cervical vertebrae, just like humans.", "cn": "令人称奇的是，长颈鹿长长的脖颈里和人类完全一样，不多不少正好由七块颈椎骨组成。"},
                {"en": "Their long blue-black tongue can extend twenty inches to strip thorns from acacia branches.", "cn": "它们长达二十英寸的蓝黑色舌头格外灵巧，能熟练避开金合欢树上锋利的硬刺卷取树叶。"},
                {"en": "A thick protective saliva coats their mouths so sharp prickles cause no injury.", "cn": "口腔内分泌的厚厚黏稠唾液，使它们在吞咽布满利刺的枝叶时丝毫不受损伤。"},
                {"en": "Giraffes have enormous hearts weighing over twenty-five pounds to pump blood up high.", "cn": "长颈鹿拥有一颗重达二十五磅以上的巨大心脏，用以将血液泵送至高高的脑部。"},
                {"en": "Special pressure valves in their neck arteries prevent fainting when they lower their heads.", "cn": "颈部动脉中精密的压力调节阀门，能确保它们低头饮水时不至于因血压过高而晕厥。"},
                {"en": "Every giraffe possesses a totally unique coat pattern, much like human fingerprints.", "cn": "每一只长颈鹿身上的斑纹图案都绝无雷同，宛如人类独一无二的指纹一样独具特色。"},
                {"en": "Because of their lofty height, giraffes can spot distant predators long before others.", "cn": "凭借得天独厚的高空视野，长颈鹿能在天敌尚在远方潜行时就率先敏锐发觉。"},
                {"en": "Giraffes require very little sleep, often napping standing up for just minutes.", "cn": "长颈鹿所需的睡眠时间极少，常常只是站立着打上短短几分钟的盹来充充电。"},
                {"en": "Newborn giraffe calves drop six feet to the ground at birth without harm.", "cn": "刚出生的长颈鹿幼崽降生时会从六英尺高的空中直坠落地，但浑身柔软安然无恙。"},
                {"en": "Within an hour of being born, the determined baby calf learns to stand and walk.", "cn": "在降生短短一个小时之内，坚毅的小长颈鹿就能靠自己的力量站立并迈出第一步。"},
                {"en": "Giraffes are gentle herbivores that live peacefully alongside zebras and gazelles.", "cn": "长颈鹿是性情极其温和的食草动物，同斑马和羚羊等邻居和睦相处、各取所需。"},
                {"en": "Habitat fragmentation poses challenges to their vast seasonal roaming territories.", "cn": "栖息地的碎片化分割，给长颈鹿大范围的季节性巡游活动带来了严峻的现实挑战。"},
                {"en": "A silhouette of giraffes striding gracefully across the African sunset is pure poetry.", "cn": "长颈鹿漫步横跨在非洲金色晚霞下的优雅剪影，宛如大自然谱写出的一首无声至美诗篇。"}
            ]
        },
        {
            "title": "第7章：热带雨林霸主美洲豹与迷彩花纹",
            "description": "南美亚马逊雨林、潜水捕猎与玫瑰斑纹之美。",
            "sentences": [
                {"en": "The jaguar is the largest and most powerful feline predator in the Americas.", "cn": "美洲豹是美洲大陆上体型最硕大、捕食威慑力最强悍的顶级猫科猛兽。"},
                {"en": "They thrive in the dense, lush river valleys of the Amazon tropical rainforest.", "cn": "它们繁衍生息在南美亚马逊热带雨林郁郁葱葱、水源丰茂的丛林河谷深处。"},
                {"en": "Jaguars possess a gorgeous golden coat adorned with distinctive black rosettes.", "cn": "美洲豹身披一身华美绝伦的金黄皮毛，点缀着宛如黑玫瑰般的圈状斑纹。"},
                {"en": "Inside each rosette pattern on a jaguar sits one or more tiny dark spots.", "cn": "与花豹不同，美洲豹每一个玫瑰圈环形斑纹内部，都点缀着一两个精巧的暗黑斑点。"},
                {"en": "This natural camouflage allows the predator to blend seamlessly into dappled jungle shade.", "cn": "这种天造地设的斑驳迷彩保护色，让美洲豹能够完美融入丛林斑驳的树影之间。"},
                {"en": "Unlike most other cats who avoid water, jaguars are exceptional swimmers.", "cn": "与绝大多数对水敬而远之的猫科动物截然不同，美洲豹是一位技艺超群的潜泳健将。"},
                {"en": "They hunt along murky riverbanks, catching caimans, turtles, and large fish with ease.", "cn": "它们常常沿着浑浊的河岸巡猎，轻而易举便能捕杀凶猛的凯门鳄、龟类和大鱼。"},
                {"en": "A jaguar's bite force is pound-for-pound the strongest of any big cat on Earth.", "cn": "按体型比例衡量，美洲豹的咬合力堪称地球上所有大型猫科猛兽当中的王者。"},
                {"en": "Their teeth can pierce through thick turtle shells and armored reptile scales.", "cn": "其锋利如钢锥的牙齿，能够轻而易举咬穿坚硬厚实的龟甲与爬行动物的骨板铠甲。"},
                {"en": "Jaguars are solitary hunters that patrol vast jungle territories marked with scent.", "cn": "美洲豹是独来独往的独行侠，依靠留下气味标记来巡视管理其广袤的领地。"},
                {"en": "Ancient indigenous civilizations revered the mighty jaguar as a supernatural guardian spirit.", "cn": "美洲古老的原生土著文明对强悍的美洲豹顶礼膜拜，将其奉为通灵的神圣守护兽。"},
                {"en": "Mother jaguars raise two cubs in secluded dens hidden behind thick waterfalls.", "cn": "母美洲豹会在掩映在奔腾瀑布后的隐蔽岩穴里，悉心哺育抚养两只小幼崽。"},
                {"en": "Deforestation threatens the integrity of their critical biodiversity corridors.", "cn": "雨林树木的肆意砍伐，严重威胁到了美洲豹至关重要的生物多样性生态走廊。"},
                {"en": "Preserving Amazonian ecosystems protects not only jaguars, but global climate balance.", "cn": "保护亚马逊雨林生态系统，不仅拯救了美洲豹，更为维系全球气候平衡立下汗马功劳。"},
                {"en": "The emerald eyes of a resting jaguar gleam with untamed prehistoric majesty.", "cn": "一只伏在古树上小憩的美洲豹那双翡翠色的眼眸，闪烁着未被驯服的史前威严。"}
            ]
        },
        {
            "title": "第8章：澳洲丛林萌宠考拉与桉树叶",
            "description": "有袋类动物、吃桉树叶睡觉与憨态可掬的考拉。",
            "sentences": [
                {"en": "The koala is an iconic Australian marsupial loved worldwide for its cuddly appearance.", "cn": "考拉是澳大利亚最具代表性的特有有袋类动物，因其憨态可掬的外表风靡全球。"},
                {"en": "Koalas have fluffy rounded ears, a leathery black nose, and thick gray fur.", "cn": "考拉长着圆滚滚毛茸茸的大耳朵、皮质温润的黑鼻子以及厚实柔软的灰毛。"},
                {"en": "They spend almost their entire lives clinging securely to eucalyptus tree branches.", "cn": "它们一生中几乎绝大部分的光阴，都紧紧攀附在桉树的高高枝丫上度过。"},
                {"en": "A koala's hands have two opposable thumbs that provide a rock-solid gripping grasp.", "cn": "考拉的前爪上神奇地长着两个对生的大拇指，能提供如铁钳般牢不可破的抓握力。"},
                {"en": "Sharp curved claws help them climb vertical tree trunks with effortless ease.", "cn": "锋利弯曲的爪尖，能帮助它们轻而易举地攀爬垂直光滑的笔直树干。"},
                {"en": "Eucalyptus leaves constitute virtually the entire specialized diet of a wild koala.", "cn": "有毒难嚼的桉树叶，几乎构成了野生考拉全部赖以生存的专属主食。"},
                {"en": "Their specialized digestive system neutralizes toxins found within tough eucalyptus leaves.", "cn": "考拉体内高度特化的超长消化系统，能够彻底中和化解桉树叶中所含的烈性毒素。"},
                {"en": "Because leaves provide very low energy, koalas sleep up to twenty hours each day.", "cn": "由于桉树叶所能提供的能量极其匮乏，考拉每天必须昏睡长达二十个小时以节约体能。"},
                {"en": "The name koala is thought to mean no drink in indigenous Australian languages.", "cn": "在澳洲土著的古老语言里，考拉这个名字被认为蕴含着不喝水的独特寓意。"},
                {"en": "They obtain nearly all their necessary hydration directly from moisture in fresh leaves.", "cn": "它们生存所需的一切水分，几乎完全直接汲取自新鲜桉树叶内部蕴含的水分。"},
                {"en": "A newborn baby koala, called a joey, is no bigger than a jellybean at birth.", "cn": "刚出生的考拉宝宝被称为乔伊，降生时的体型只有一颗软糖般微小娇嫩。"},
                {"en": "The tiny joey crawls into its mother's pouch where it nurses safely for six months.", "cn": "幼小的乔伊凭本能爬入母亲的育儿袋内，在袋中安全吮吸乳汁长达六个月之久。"},
                {"en": "Older joeys ride piggyback on their mother's shoulders as they learn to navigate trees.", "cn": "半大的考拉宝宝会舒舒服服趴在母亲的后背上，跟着妈妈一道学习在树冠间穿行。"},
                {"en": "Bushfires and urban expansion present serious threats to remaining wild koala habitats.", "cn": "频发的丛林山火与城市的无序扩张，给野生考拉现存的家园带来了严峻的现实挑战。"},
                {"en": "Watching a gentle koala munch peacefully on eucalyptus leaves warms the human soul.", "cn": "看着一只温顺软萌的小考拉慢条斯理地嚼着桉树叶，总能让人们的心灵倍感治愈。"}
            ]
        },
        {
            "title": "第9章：天空翱翔霸主金雕与千里眼",
            "description": "猛禽俯冲狩猎、双眼视力与高空筑巢绝技。",
            "sentences": [
                {"en": "The golden eagle is one of the most formidable birds of prey in the northern hemisphere.", "cn": "金雕是北半球整个天空中捕食战斗力最为强悍勇猛的顶级猛禽之一。"},
                {"en": "With a magnificent wingspan exceeding seven feet, they glide effortlessly on thermal currents.", "cn": "凭借超过七英尺的硕大双翼展翅，金雕能够毫不费力地借助上升热气流在高空翱翔。"},
                {"en": "The golden-brown plumage on the back of their heads glows brilliantly in sunlight.", "cn": "其脑后与颈项上那一圈金褐色的华美羽毛，在阳光照耀下宛如纯金般熠熠生辉。"},
                {"en": "A golden eagle's vision is up to eight times sharper than that of a human being.", "cn": "金雕那双洞察秋毫的千里眼，其视敏度比正常人类的双眼要敏锐锋利整整八倍以上。"},
                {"en": "They can spot a tiny hare scampering across fields from over two miles in the sky.", "cn": "它们在高达两英里的天际巡弋时，便能瞬间捕捉到草地上奔逃的一只野兔。"},
                {"en": "When diving toward its target, a golden eagle can reach speeds over one hundred fifty miles an hour.", "cn": "当其收拢双翼以毁灭之势向下俯冲时，飞行速度能够飙升至每小时一百五十英里以上。"},
                {"en": "Their massive razor-sharp talons exert crushing force equivalent to a canine jaw.", "cn": "其粗壮如铁钩般的锋利利爪所施加的粉碎性抓力，足以媲美强壮猎犬的猛烈咬合。"},
                {"en": "Golden eagles build colossal nests called eyries high atop inaccessible rocky cliff ledges.", "cn": "金雕在险峻陡峭、人迹罕至的高山悬崖绝壁顶端，构筑庞大而坚固的巨型鹰巢。"},
                {"en": "Mated pairs often stay loyal to one another for life, sharing nest-building duties.", "cn": "结为夫妻的金雕伴侣往往终生相濡以沫忠贞不渝，共同分担修筑鹰巢抚养雏鸟的重任。"},
                {"en": "They add fresh sticks to their eyrie each year, creating homes weighing several hundred pounds.", "cn": "它们年复一年往巢穴中增添结实的新鲜树枝，打造出重达数百磅的巍峨空中城堡。"},
                {"en": "Parents teach young eaglets how to master wind drafts and execute precision dives.", "cn": "雕爸爸和雕妈妈会手把手传授幼鹰如何精准驾驭风向气流，如何完成致命精准俯冲。"},
                {"en": "Golden eagles symbolize courage, freedom, and strength across many ancient cultural mythologies.", "cn": "在许多古老文明的图腾与神话中，金雕始终是无畏勇气、辽阔自由与至强力量的象征。"},
                {"en": "They play a vital ecological role by keeping rodent and hare populations healthy and balanced.", "cn": "通过控制啮齿动物与野兔的数量规模，金雕在生态平衡中发挥着不可替代的中流砥柱作用。"},
                {"en": "Legal protections and reintroduction projects help secure the future of these majestic raptors.", "cn": "健全的法律保护措施与野化放归工程，为保全这些雄浑猛禽的生存繁衍奠定了坚实基础。"},
                {"en": "A golden eagle soaring across snowy mountain peaks is the ultimate portrait of wild majesty.", "cn": "一只展翅翱翔在皑皑雪峰之上的威武金雕，是大自然野性与尊严最为纯粹的终极写照。"}
            ]
        },
        {
            "title": "第10章：大堡礁奇幻珊瑚礁与小丑鱼",
            "description": "海底世界、共生小丑鱼、海葵触手与海洋保护。",
            "sentences": [
                {"en": "The Great Barrier Reef off Australia is the largest living structure visible from outer space.", "cn": "坐落在澳大利亚东北海岸的大堡礁，是地球上从外太空都能清晰目睹的最大的生命结构体。"},
                {"en": "Billions of tiny coral polyps constructed this underwater wonder over thousands of years.", "cn": "数以亿计的微小珊瑚虫历经千百年的漫长岁月，聚沙成塔构筑起这座浩瀚的海底奇迹。"},
                {"en": "Clownfish are famous reef inhabitants known for their vivid orange bodies and white stripes.", "cn": "小丑鱼是珊瑚礁里声名远播的原住民，因其鲜艳的橙红底色与三道白斑纹而闻名遐迩。"},
                {"en": "They live in a fascinating symbiotic partnership with venomous sea anemones.", "cn": "它们与浑身布满致命毒素的海葵触手，维系着一段令人叹为观止的奇妙共生盟友关系。"},
                {"en": "A specialized layer of mucus coats the clownfish skin, making it immune to anemone stings.", "cn": "一层特化的保护性黏液包裹着小丑鱼的体表，使其对海葵的剧毒刺细胞完全免疫无伤。"},
                {"en": "The stinging anemone protects tiny clownfish from hungry predators like snappers.", "cn": "长满毒刺的海葵如同忠诚卫士，保护着弱小的小丑鱼免遭笛鲷等掠食大鱼的吞食。"},
                {"en": "In return, energetic clownfish clean debris and chase away butterflyfish that eat anemone tentacles.", "cn": "作为投桃报李的回报，勤快的小丑鱼会清理碎屑残渣，并赶跑企图啄食海葵触手的蝴蝶鱼。"},
                {"en": "A single coral reef supports over one thousand five hundred different species of colorful fish.", "cn": "一片生机盎然的珊瑚礁，能够同时庇护哺育超过一千五百种形形色色的各色斑斓鱼类。"},
                {"en": "Majestic green sea turtles glide through azure waters, grazing peacefully on seagrass beds.", "cn": "威严的大海龟在碧绿的海水中悠然滑行，悠闲自在地啃食着丰茂的海草床。"},
                {"en": "Vibrant parrotfish crunch on dead coral, producing fine white sand that forms tropical beaches.", "cn": "色彩斑斓的鹦鹉鱼啃食着老化的珊瑚，排泄出洁白细腻的沙粒，形成了美丽的白色沙滩。"},
                {"en": "Gentle manta rays with giant winged fins perform graceful looping acrobatics in blue currents.", "cn": "长着巨幅羽翼胸鳍的温和蝠鲼，在蔚蓝的水流之中上演着优美绝伦的凌空翻滚杂技。"},
                {"en": "Rising sea temperatures cause coral bleaching, threatening the delicate foundation of reef life.", "cn": "海水温度的持续异常升高会导致珊瑚白化死亡，给整个珊瑚礁脆弱的生态基石带来灭顶之灾。"},
                {"en": "Marine protected sanctuaries help restore coral ecosystems and maintain fish populations.", "cn": "设立海洋自然保护禁渔区，有助于加速珊瑚生态系统的自我恢复并维持鱼类种群的繁荣。"},
                {"en": "Every tiny creature from microscopic plankton to giant reef sharks has a sacred role to play.", "cn": "从显微镜下的浮游生物到庞大的礁鲨，珊瑚世界里的每一个微小生灵都肩负着神圣的使命。"},
                {"en": "Exploring the kaleidoscope of life on a coral reef leaves travelers in speechless wonder.", "cn": "探索珊瑚礁那如万花筒般绚烂多彩的宏大生命画卷，总能让每一位旅人惊叹得语塞失声。"}
            ]
        }
    ]
}

print("COURSE_KIDS_DAILY, FAIRYTALE, ANIMALS ready")
