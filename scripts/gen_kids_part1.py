# -*- coding: utf-8 -*-
"""
少儿英语生成器 Part 1:
1. kids-phonics: 自然拼读字母探险 (10章 x 15句 = 150句)
2. kids-daily: 宝宝日常英语交流 (10章 x 15句 = 150句)
3. kids-fairytale: 迪士尼经典童话小剧场 (10章 x 15句 = 150句)
4. kids-animals: 奇妙动物王国大百科 (10章 x 15句 = 150句)
共 4 门课程，40 章，600 句地道儿童英文。
"""

COURSE_KIDS_PHONICS = {
    "meta": {
        "id": "kids-phonics",
        "title": "自然拼读字母探险",
        "category": "kids",
        "categoryName": "少儿英语",
        "coverGradient": "from-amber-400 to-orange-500",
        "icon": "🔤",
        "description": "专为幼少儿设计的自然拼读启蒙课，从 26 个英文字母纯正发音到短元音 CVC 拼读趣味闯关。",
        "difficulty": "beginner",
        "tags": ["少儿英语", "自然拼读", "字母发音", "启蒙启智"]
    },
    "chapters": [
        {
            "title": "第1章：字母 A & B 的神奇发音",
            "description": "认识大写字母 A、B 与基础自然拼读规则。",
            "sentences": [
                {"en": "A is for apple, sweet and red.", "cn": "A 代表苹果，又甜又红。"},
                {"en": "The little ant climbs up the green tree.", "cn": "小蚂蚁爬上了绿色的树。"},
                {"en": "An astronaut travels to the shining stars.", "cn": "宇航员向着闪亮的星辰旅行。"},
                {"en": "The airplane flies high above the clouds.", "cn": "飞机在白云高处翱翔。"},
                {"en": "An alligator rests quietly by the clear river.", "cn": "短吻鳄在清澈的河边静静休息。"},
                {"en": "B is for bear, big and furry.", "cn": "B 代表大熊，身躯高大毛茸茸。"},
                {"en": "The yellow bus stops at our school gate.", "cn": "黄色的校车停在我们的学校门口。"},
                {"en": "The cheerful bird sings a lovely song.", "cn": "欢快的小鸟唱起悦耳的歌。"},
                {"en": "Kick the colorful ball into the goal.", "cn": "把彩色的球踢进球门里。"},
                {"en": "Open your favorite picture book together.", "cn": "一起打开你最喜爱的图画书。"},
                {"en": "The butterfly dances softly in the garden.", "cn": "蝴蝶在花园里轻盈地飞舞。"},
                {"en": "Baby plays with soft building blocks.", "cn": "小宝宝在玩柔软的积木玩具。"},
                {"en": "A busy bee buzzes around sweet flowers.", "cn": "忙碌的蜜蜂在甜甜的花丛周围嗡嗡叫。"},
                {"en": "Bake a round birthday cake for everyone.", "cn": "为大家烤制一个圆圆的生日蛋糕。"},
                {"en": "The brave boy wears a blue cape.", "cn": "勇敢的小男孩披着蓝色的斗篷。"}
            ]
        },
        {
            "title": "第2章：字母 C & D 的动物乐园",
            "description": "掌握辅音 C 和 D 的趣味动物词汇与句型。",
            "sentences": [
                {"en": "C is for cat, soft and quiet.", "cn": "C 代表小猫，温顺又安静。"},
                {"en": "The cute cat sleeps on the warm rug.", "cn": "可爱的小猫睡在温暖的地毯上。"},
                {"en": "The red car zooms along the straight road.", "cn": "红色的小汽车沿着笔直的马路飞驰。"},
                {"en": "Eat crunchy carrots to stay healthy and strong.", "cn": "吃脆脆的胡萝卜保持身体健康强壮。"},
                {"en": "The friendly cow gives us fresh milk.", "cn": "友善的奶牛为我们提供新鲜牛奶。"},
                {"en": "Put on your warm winter cap outside.", "cn": "去室外时戴上你温暖的冬帽。"},
                {"en": "The smart camel walks across the desert.", "cn": "聪明的骆驼漫步穿过沙漠。"},
                {"en": "D is for dog, loyal and playful.", "cn": "D 代表小狗，忠诚又活泼。"},
                {"en": "The friendly duck swims in the pond.", "cn": "友善的鸭子在池塘里游泳。"},
                {"en": "A playful dolphin jumps over the ocean waves.", "cn": "调皮的海豚跃过了海浪。"},
                {"en": "The little deer runs through the green forest.", "cn": "小鹿奔跑着穿过绿色的森林。"},
                {"en": "Beat the toy drum with rhythm and joy.", "cn": "伴随着节奏和喜悦敲响玩具小鼓。"},
                {"en": "Open the front door and say hello.", "cn": "推开前门，热情地说声你好。"},
                {"en": "The shiny coin dropped into the piggy bank.", "cn": "闪亮的硬币掉进了小猪储蓄罐。"},
                {"en": "Look at the colorful drawing on the easel.", "cn": "看着画架上那幅五彩斑斓的画作。"}
            ]
        },
        {
            "title": "第3章：字母 E & F 的魔法森林",
            "description": "探索元音 E 与清辅音 F 的纯正自然拼读。",
            "sentences": [
                {"en": "E is for elephant, proud and strong.", "cn": "E 代表大象，威武又强壮。"},
                {"en": "The giant elephant has a long trunk.", "cn": "巨大的大象有一根长长的鼻子。"},
                {"en": "Birds hatch out of tiny speckled eggs.", "cn": "小鸟从带斑点的小蛋里孵化出来。"},
                {"en": "The eagle soars high in the blue sky.", "cn": "雄鹰在蔚蓝的天空中展翅翱翔。"},
                {"en": "Turn on your active imagination every day.", "cn": "每天开启你充满活力的小脑瓜。"},
                {"en": "F is for fox, quick and clever.", "cn": "F 代表小狐狸，敏捷又聪明。"},
                {"en": "The silver fish glides through the cool lake.", "cn": "银色的小鱼在清凉的湖水中滑行。"},
                {"en": "The green frog hops onto a lily pad.", "cn": "绿色的小青蛙跳上了一片睡莲叶。"},
                {"en": "Pick fresh flowers in the sunny meadow.", "cn": "在阳光明媚的草地上采摘新鲜的花朵。"},
                {"en": "My happy family enjoys dinner together.", "cn": "我快乐的一家人开心地共进晚餐。"},
                {"en": "The soft feather floats gently in the air.", "cn": "柔软的羽毛在空中轻柔地飘浮。"},
                {"en": "Blow the cheerful paper flute with glee.", "cn": "欢天喜地地吹响快乐的纸长笛。"},
                {"en": "The bright fireworks light up the night.", "cn": "绚烂的烟火点亮了整个夜空。"},
                {"en": "Farmers feed their animals early in morning.", "cn": "农夫们清晨早早起来喂养动物。"},
                {"en": "Follow the trail of fairy footprints forward.", "cn": "跟随着小精灵的足迹向前探索。"}
            ]
        },
        {
            "title": "第4章：字母 G & H 的微笑花园",
            "description": "跟读 G 与 H 发音，练习日常身边事物。",
            "sentences": [
                {"en": "G is for giraffe, tall and kind.", "cn": "G 代表长颈鹿，高大又善良。"},
                {"en": "The gentle giraffe eats green leaves peacefully.", "cn": "温顺的长颈鹿安静地吃着绿叶。"},
                {"en": "Juicy sweet grapes grow on the sunny vine.", "cn": "鲜美甘甜的葡萄长在向阳的藤架上。"},
                {"en": "The cheerful girl waters her potted plants.", "cn": "欢快的小女孩给她的盆栽浇水。"},
                {"en": "Golden sunshine warms the sleepy morning earth.", "cn": "金灿灿的阳光温暖了初醒的大地。"},
                {"en": "Play a delightful tune on your guitar.", "cn": "在你的小吉他上弹奏一首愉快的乐曲。"},
                {"en": "H is for horse, galloping across the field.", "cn": "H 代表骏马，在田野上飞驰奔腾。"},
                {"en": "Put on a cozy sun hat before going out.", "cn": "外出之前戴上一顶舒适的遮阳帽。"},
                {"en": "Give mom a big warm hug every morning.", "cn": "每天清晨给妈妈一个大大的温暖拥抱。"},
                {"en": "The sweet honey comes from hard-working bees.", "cn": "甜甜的蜂蜜来自勤劳的小蜜蜂。"},
                {"en": "Home is full of laughter and gentle care.", "cn": "家是一个洋溢着欢笑与温柔关爱的地方。"},
                {"en": "Listen to the happy heartbeat inside you.", "cn": "倾听你胸膛里快乐跳动的心跳声。"},
                {"en": "High mountains kiss the gentle fluffy clouds.", "cn": "高高的群山轻吻着柔软蓬松的白云。"},
                {"en": "Hand in hand we walk along the park path.", "cn": "我们手拉着手走在公园的小径上。"},
                {"en": "Healthy habits keep our smile shining bright.", "cn": "健康的生活习惯让我们的笑容格外灿烂。"}
            ]
        },
        {
            "title": "第5章：字母 I & J 的缤纷冒险",
            "description": "探索元音 I 与爆破音 J 的拼读奥妙。",
            "sentences": [
                {"en": "I is for igloo, built of sparkling snow.", "cn": "I 代表雪屋，用闪烁的白雪砌成。"},
                {"en": "The colorful iguana rests on a warm rock.", "cn": "色彩斑斓的鬣蜥在温暖的岩石上小憩。"},
                {"en": "Dip your pen into the dark purple ink.", "cn": "把你的钢笔蘸进深紫色的墨水里。"},
                {"en": "Insect wings shimmer under the bright sunshine.", "cn": "昆虫的翅膀在明媚的阳光下闪闪发亮。"},
                {"en": "An exciting island awaits our brave discovery.", "cn": "一座令人兴奋的小岛等待着我们勇敢的探索。"},
                {"en": "J is for jaguar, swift and graceful.", "cn": "J 代表美洲豹，敏捷又优雅。"},
                {"en": "The glass jar is full of strawberry jam.", "cn": "玻璃罐里装满了甜甜的草莓酱。"},
                {"en": "The little kangaroo jumps with joyful bounds.", "cn": "小袋鼠欢快地一蹦一跳。"},
                {"en": "Put on your warm fleece jacket for recess.", "cn": "课间休息时穿上你暖和的抓绒夹克。"},
                {"en": "The playful monkey eats a ripe banana.", "cn": "调皮的小猴子吃着成熟的香蕉。"},
                {"en": "Jellyfish drift peacefully in the deep blue ocean.", "cn": "水母在深蓝的大海里悠闲地漂流。"},
                {"en": "Sing and rejoice with every joyful note.", "cn": "伴着每一个快乐的音符欢歌雀跃。"},
                {"en": "The circus juggler tossed three silver balls.", "cn": "杂技演员在空中抛接着三个银球。"},
                {"en": "Jump high into the soft pile of leaves.", "cn": "高高跳进那堆柔软的落叶堆里。"},
                {"en": "A cheerful jigsaw puzzle reveals a castle.", "cn": "一副有趣的拼图展现出一座奇妙的城堡。"}
            ]
        },
        {
            "title": "第6章：字母 K & L 的国王城堡",
            "description": "掌握辅音 K 与边音 L 的词汇和基础句。",
            "sentences": [
                {"en": "K is for kite, flying in the spring breeze.", "cn": "K 代表风筝，在春天的微风中翱翔。"},
                {"en": "The playful kitten chases a ball of yarn.", "cn": "顽皮的小猫咪追赶着毛线球。"},
                {"en": "The wise king wears a golden sparkling crown.", "cn": "睿智的国王戴着闪耀的纯金皇冠。"},
                {"en": "Turn the golden key to open the treasure box.", "cn": "转动金钥匙，打开神秘的宝藏箱。"},
                {"en": "The mother kangaroo carries her baby safely.", "cn": "袋鼠妈妈安全地将宝宝护在育儿袋里。"},
                {"en": "L is for lion, the majestic king of beasts.", "cn": "L 代表狮子，威风凛凛的百兽之王。"},
                {"en": "Green leaves dance in the gentle summer wind.", "cn": "绿色的树叶在柔和的夏风中轻舞。"},
                {"en": "A yellow lemon tastes sour and wonderfully refreshing.", "cn": "黄色的柠檬吃起来酸溜溜，令人神清气爽。"},
                {"en": "Turn on the cozy lamp beside your bed.", "cn": "打开你床头那盏温馨舒适的小台灯。"},
                {"en": "The woolly lamb plays across the clover field.", "cn": "毛茸茸的小羊在三叶草地里欢快玩耍。"},
                {"en": "Sweet pink lollipops bring smiles to everyone.", "cn": "甜甜的粉色棒棒糖让每个人都绽放笑容。"},
                {"en": "Listen closely to the gentle rustling stream.", "cn": "静静地侧耳倾听小溪潺潺的流水声。"},
                {"en": "Ladders help builders reach up to high roofs.", "cn": "梯子帮助建筑工人们攀上高高的屋顶。"},
                {"en": "Lighthouse beams guide boats across dark waters.", "cn": "灯塔的光束指引着船只驶过漆黑的水面。"},
                {"en": "Laugh out loud with your best friends.", "cn": "和你最好的伙伴们一起开怀大笑。"}
            ]
        },
        {
            "title": "第7章：字母 M & N 的月夜星空",
            "description": "鼻音 M 与 N 的拼读发音与优美夜晚句型。",
            "sentences": [
                {"en": "M is for moon, glowing in the night sky.", "cn": "M 代表月亮，在漆黑的夜空里发光。"},
                {"en": "The curious monkey swings from branch to branch.", "cn": "好奇的小猴子在树枝之间荡来荡去。"},
                {"en": "Drink a glass of warm milk before bedtime.", "cn": "睡前喝一杯温热可口的牛奶。"},
                {"en": "Snowy mountains stand tall against the horizon.", "cn": "皑皑白雪覆盖的崇山峻岭屹立在天际线上。"},
                {"en": "A little mouse nibbles a slice of cheese.", "cn": "一只小老鼠细细啃咬着一片奶酪。"},
                {"en": "Sweet music fills our warm classroom today.", "cn": "今天温馨的教室里回荡着优美的音乐。"},
                {"en": "N is for nest, resting safely in branches.", "cn": "N 代表鸟巢，安全地筑在茂密的树枝间。"},
                {"en": "The kind nurse takes good care of children.", "cn": "亲切的护士阿姨细心照顾着生病的小朋友。"},
                {"en": "Crack open the crunchy nut with two hands.", "cn": "用双手用力剥开那颗脆脆的坚果。"},
                {"en": "Nine colorful balloons float up into the sky.", "cn": "九只色彩缤纷的彩色气球飞向了天空。"},
                {"en": "The quiet night brings sweet dreams to all.", "cn": "安静祥和的夜晚为所有人带来了香甜的美梦。"},
                {"en": "Write your name neatly on the first page.", "cn": "在第一页上工工整整写下你的名字。"},
                {"en": "A cozy needle weaves a warm woolen scarf.", "cn": "灵巧的织针编织出一条温暖的羊毛围巾。"},
                {"en": "Nature gives us clean air and fresh water.", "cn": "大自然赋予了我们清新的空气与甘甜的泉水。"},
                {"en": "Say good night and close your sleepy eyes.", "cn": "道一声晚安，轻轻合上困倦的双眼。"}
            ]
        },
        {
            "title": "第8章：字母 O & P 的海洋巡航",
            "description": "元音 O 与爆破音 P 的海洋动植物认知。",
            "sentences": [
                {"en": "O is for octopus, with eight flexible arms.", "cn": "O 代表章鱼，拥有八条灵活有力的触手。"},
                {"en": "The wise owl hooted in the ancient oak.", "cn": "聪慧的老猫头鹰在古老的橡树上啼鸣。"},
                {"en": "Juicy sweet oranges grow in sunny groves.", "cn": "多汁可口的橙子生长在阳光明媚的果园里。"},
                {"en": "The ocean waves crash gently on golden sand.", "cn": "大海的浪花轻柔地拍打着金色的沙滩。"},
                {"en": "Open your backpack and find your notebook.", "cn": "打开你的小书包，找出你的笔记本。"},
                {"en": "P is for panda, chewing green bamboo shoots.", "cn": "P 代表大熊猫，嘴里咀嚼着青翠的竹笋。"},
                {"en": "The colorful parrot repeats what we say.", "cn": "那只羽毛艳丽的鹦鹉模仿着我们说的话。"},
                {"en": "Eat crisp green peas at dinner tonight.", "cn": "今晚晚饭时品尝爽口嫩绿的豌豆。"},
                {"en": "Draw a picture with bright colored pencils.", "cn": "用色彩明艳的彩色铅笔绘制一幅画。"},
                {"en": "The little penguin waddles across the ice.", "cn": "小企鹅摇摇摆摆地走在洁白的冰面上。"},
                {"en": "Plant a flower seed in the brown soil.", "cn": "在褐色的泥土里种下一粒花朵的种子。"},
                {"en": "The playful puppy wags its tail happily.", "cn": "活泼可爱的小狗欢快地摇着尾巴。"},
                {"en": "Piano keys make beautiful flowing melodies.", "cn": "钢琴的琴键弹奏出如行云流水般的优美旋律。"},
                {"en": "Pick up your toys after you finish playing.", "cn": "玩耍完毕之后记得把你的玩具收纳整齐。"},
                {"en": "Polite words make everyone around us glad.", "cn": "有礼貌的言语让身边的每一个人都心花怒放。"}
            ]
        },
        {
            "title": "第9章：字母 Q & R 的彩虹王国",
            "description": "字母组合 Qu 与卷舌辅音 R 的拼读律动。",
            "sentences": [
                {"en": "Q is for queen, ruling with grace and wisdom.", "cn": "Q 代表女王，用优雅与智慧治理国度。"},
                {"en": "The queen wears a magnificent velvet robe.", "cn": "女王身着一件华贵无比的丝绒长袍。"},
                {"en": "Be quiet while the baby is sleeping.", "cn": "小宝宝睡觉的时候请保持安静。"},
                {"en": "The brown quail walked through tall grasses.", "cn": "棕色的鹌鹑信步走过高高的草丛。"},
                {"en": "Answer the teacher's question with confidence.", "cn": "自信从容地回答老师提出的问题。"},
                {"en": "R is for rainbow, shining after spring showers.", "cn": "R 代表彩虹，在春雨过后光芒闪烁。"},
                {"en": "A cute rabbit nibbles a crunchy orange carrot.", "cn": "可爱的小兔子咀嚼着清脆甜美的胡萝卜。"},
                {"en": "Rain falls gently on flower petals outside.", "cn": "雨水淅淅沥沥地轻落在户外的花瓣上。"},
                {"en": "The rocket blasted off into deep outer space.", "cn": "火箭呼啸升空，飞向深邃的外太空。"},
                {"en": "The little red robot cleans the bedroom floor.", "cn": "红色的小机器人把卧室的地板打扫得干干净净。"},
                {"en": "Run across the playground with pure joy.", "cn": "满怀纯真的欢喜在操场上尽情奔跑。"},
                {"en": "Read an exciting story before going to sleep.", "cn": "在进入梦乡之前阅读一个引人入胜的精彩故事。"},
                {"en": "Rivers flow swiftly toward the endless ocean.", "cn": "江河奔流不息，汇入无边无际的汪洋大海。"},
                {"en": "Red apples hang low from sturdy branches.", "cn": "红彤彤的苹果沉甸甸地挂在结实的树枝上。"},
                {"en": "Remember to smile and greet your neighbors.", "cn": "记得带上微笑，热情地向邻居们问好。"}
            ]
        },
        {
            "title": "第10章：字母 S 到 Z 的终极星际派对",
            "description": "完成最后字母拼读闯关，巩固完整字母发音系统。",
            "sentences": [
                {"en": "S is for sun, giving warmth and golden light.", "cn": "S 代表太阳，播撒无尽的温暖与金光。"},
                {"en": "The tiny snail slides across the dewy leaf.", "cn": "小蜗牛缓缓滑过挂满露珠的绿叶。"},
                {"en": "T is for tiger, pacing through the tall grass.", "cn": "T 代表老虎，威风凛凛地踱步穿过高草丛。"},
                {"en": "The big green turtle swims in the coral reef.", "cn": "绿色的大海龟在五彩斑斓的珊瑚礁里游动。"},
                {"en": "U is for umbrella, keeping us dry in rain.", "cn": "U 代表雨伞，在倾盆大雨中为我们遮风挡雨。"},
                {"en": "The magical unicorn has a glittering horn.", "cn": "神奇的独角兽头顶长着一支晶莹闪烁的犄角。"},
                {"en": "V is for violin, singing sweet melodic notes.", "cn": "V 代表小提琴，奏出甘醇悦耳的动人音符。"},
                {"en": "W is for whale, diving into deep ocean waters.", "cn": "W 代表巨鲸，潜入幽深蔚蓝的大洋深处。"},
                {"en": "The winter wind blows softly through the pines.", "cn": "冬日的风在青翠的松林间轻轻呼啸。"},
                {"en": "X is for xylophone, playing colorful clear tones.", "cn": "X 代表木琴，敲击出清脆空灵的五彩乐调。"},
                {"en": "Y is for yacht, sailing smoothly on the bay.", "cn": "Y 代表游艇，在宁静的港湾里平稳航行。"},
                {"en": "Yellow sunflowers turn to face the bright sun.", "cn": "金黄的向日葵转过头去迎着灿烂的太阳。"},
                {"en": "Z is for zebra, wearing black and white stripes.", "cn": "Z 代表斑马，身披黑白相间的条纹花纹。"},
                {"en": "Visit the happy animals at the sunny zoo.", "cn": "在阳光普照的动物园里探望快乐的小动物们。"},
                {"en": "You have mastered all twenty-six English letters!", "cn": "你已经精通了全部二十六个英文字母的发音！"}
            ]
        }
    ]
}

print("COURSE_KIDS_PHONICS ready")
