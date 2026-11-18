# -*- coding: utf-8 -*-
"""
少儿英语生成器 Part 3:
5. kids-colors: 魔法色彩与数字乐园 (10章 x 15句 = 150句)
6. kids-manners: 懂礼貌好宝宝习惯养成 (10章 x 15句 = 150句)
7. kids-songs: 经典英文儿歌欢唱启蒙 (10章 x 15句 = 150句)
8. kids-nature: 小小探索家探索大自然 (10章 x 15句 = 150句)
共 4 门课程，40 章，600 句。
"""

COURSE_KIDS_COLORS = {
    "meta": {
        "id": "kids-colors",
        "title": "魔法色彩与数字乐园",
        "category": "kids",
        "categoryName": "少儿英语",
        "coverGradient": "from-yellow-400 to-amber-600",
        "icon": "🎨",
        "description": "专为幼童打造的颜色认知与数数乐园，趣味结合日常生活常见物品，轻松掌握英语基础数词与色彩词汇。",
        "difficulty": "beginner",
        "tags": ["少儿英语", "数字启蒙", "颜色认知", "趣味互动"]
    },
    "chapters": [
        {
            "title": "第1章：红与绿的交通信号灯",
            "description": "认知红色与绿色，理解交通安全常识与身边红绿色物品。",
            "sentences": [
                {"en": "Red is the vibrant color of a juicy ripe strawberry.", "cn": "红色是一颗多汁鲜嫩的成熟草莓所拥有的鲜亮色彩。"},
                {"en": "The bright red traffic light warns cars to come to a stop.", "cn": "明亮刺眼的红灯亮起，警示所有汽车必须完全停下。"},
                {"en": "A shiny red firetruck rushes past with loud sounding sirens.", "cn": "一辆锃亮的红色消防车呼啸而过，警笛声响彻云霄。"},
                {"en": "Pick five sweet red cherries from the orchard tree.", "cn": "从果园的果树上亲手采摘五颗甘甜红润的车厘子。"},
                {"en": "She wears a lovely red ribbon tied in her curls.", "cn": "她的卷发上系着一条极其惹人喜爱的小红丝带。"},
                {"en": "Green is the peaceful color of fresh spring grass.", "cn": "绿色是春天大地上郁郁葱葱的新生嫩草所具有的宁静色彩。"},
                {"en": "The green traffic light signals pedestrians that it is safe to walk.", "cn": "绿色的信号灯亮起，告诉行人现在可以安全通行了。"},
                {"en": "A little green frog hops into the clear pond.", "cn": "一只绿色的小青蛙扑通一声跃入了清澈见底的池塘里。"},
                {"en": "Look at the tall green pine trees covering the hill.", "cn": "看那高大挺拔的青松翠柏，漫山遍野披上了绿装。"},
                {"en": "Crunchy green cucumbers make our lunch salad delicious.", "cn": "爽脆可口的绿黄瓜让我们的午餐沙拉变得分外美味。"},
                {"en": "One shiny red apple sits beside two crunchy green pears.", "cn": "一颗红彤彤的苹果摆放在两只清脆的绿梨旁边。"},
                {"en": "Mix red paint with yellow paint to create glowing orange.", "cn": "把红色的颜料和黄色的颜料融合，调配出温暖的橘黄色。"},
                {"en": "Paint a big green garden surrounded by red roses.", "cn": "画一座郁郁葱葱的绿色大花园，周围环绕着娇艳的红玫瑰。"},
                {"en": "Red and green stand together across the Christmas holiday.", "cn": "在温馨的圣诞节日里，红与绿总是携手相伴相映成趣。"},
                {"en": "Colors make our beautiful world come alive with wonder.", "cn": "大千世界因绚丽色彩而生机勃发，充满了奇妙的魔力。"}
            ]
        },
        {
            "title": "第2章：蓝天与金黄太阳之歌",
            "description": "认知蓝色与黄色，从辽阔天空到温暖阳光的描摹。",
            "sentences": [
                {"en": "Blue is the tranquil color of the infinite morning sky.", "cn": "蓝色是清晨那片浩瀚无垠的辽阔晴空所蕴含的深邃宁静之色。"},
                {"en": "The endless deep blue ocean sparkles beneath gentle sunshine.", "cn": "无边无际的深蓝大海在柔和的阳光照耀下波光粼粼闪闪发亮。"},
                {"en": "A beautiful blue jay rests upon the garden fence.", "cn": "一只羽毛艳丽的蓝松鸦静静栖息在花园的木栅栏上。"},
                {"en": "Slip into your favorite pair of comfortable blue denim jeans.", "cn": "套上你平时最心爱、最舒适合身的那条深蓝牛仔裤。"},
                {"en": "Blow huge blue soap bubbles that drift into the air.", "cn": "吹出一个个巨大的蓝色肥皂泡泡，看它们轻盈漂浮在半空中。"},
                {"en": "Yellow is the joyful color of radiant golden sunshine.", "cn": "黄色是璀璨温暖的金色暖阳所散发出的满载欢悦之色。"},
                {"en": "The yellow school bus stops to pick up neighborhood children.", "cn": "亮黄色的校车缓缓停稳，接送社区里准备上学的小朋友们。"},
                {"en": "A field of tall yellow sunflowers turns toward the light.", "cn": "一大片亭亭玉立的黄色向日葵整齐划一地迎着朝阳昂首绽放。"},
                {"en": "Peel a sweet ripe yellow banana for afternoon snack.", "cn": "剥开一根香甜软糯的熟透黄香蕉，作为可口的下午茶点心。"},
                {"en": "A cute yellow rubber duck floats around the warm bath.", "cn": "一只可爱的小黄鸭橡皮玩具在温热的浴缸里四处漂浮游荡。"},
                {"en": "When you mix blue and yellow, magical green appears.", "cn": "当你把纯净的蓝与明艳的黄混合在一起，神奇的绿色便展现眼前。"},
                {"en": "Three bright yellow ducklings follow their mother in line.", "cn": "三只毛茸茸的嫩黄色小鸭子排着整齐的队伍紧随鸭妈妈身后。"},
                {"en": "The blue bird sings from high up in the leafy canopy.", "cn": "那只蓝色的小鸟在高高茂密的绿色树冠顶端放声高歌。"},
                {"en": "Yellow stars glow brightly against the midnight blue horizon.", "cn": "金黄的繁星在深蓝色的午夜地平线上空璀璨发光。"},
                {"en": "Use blue and yellow crayons to draw a sunny coastline.", "cn": "用蓝色和黄色的彩色蜡笔，绘制出一幅阳光明媚的海岸风光画。"}
            ]
        },
        {
            "title": "第3章：从一数到五的数字乐园",
            "description": "数字 1 到 5 的拼写认知，结合手指与可爱玩偶。",
            "sentences": [
                {"en": "One is the single golden sun warming our Earth.", "cn": "1 代表那一轮在天空中独一无二、温暖我们地球的金色太阳。"},
                {"en": "I have one little nose right in the middle of my face.", "cn": "我的脸庞正中间端端正正长着一只可爱的小鼻子。"},
                {"en": "Two is the pair of sparkling eyes you use to see.", "cn": "2 代表你用来看清美丽世界的这一双明亮清澈的大眼睛。"},
                {"en": "Put on two clean cotton socks, one for each foot.", "cn": "穿上两只干净纯棉的袜子，左脚一只，右脚一只。"},
                {"en": "Three is the number of sides on every triangle shape.", "cn": "3 代表每一个等边三角形四周不多不少正好具备的三条边。"},
                {"en": "Three little kittens lost their warm woolen mittens in snow.", "cn": "三只调皮的小猫咪在冰天雪地里不小心弄丢了保暖的羊毛手套。"},
                {"en": "Four is the sturdy legs supporting our wooden kitchen table.", "cn": "4 代表支撑着我们家木质餐桌平稳伫立的四条结实桌腿。"},
                {"en": "A small car has four round rubber wheels that roll fast.", "cn": "一辆小汽车底下长着四个飞速向前转动的橡胶大轮子。"},
                {"en": "Five is the fingers dancing cheerfully on your open hand.", "cn": "5 代表你张开的小手掌上欢快跳跃舞动的五根手指头。"},
                {"en": "A twinkling star has five sharp points pointing outward.", "cn": "一颗闪烁的金色五角星，向着五方伸展出锐利的尖角。"},
                {"en": "Count out loud together: one, two, three, four, five!", "cn": "让我们大家一起大声数出来：一、二、三、四、五！"},
                {"en": "One brave puppy plays with two colorful bouncing balls.", "cn": "一只勇敢的小狗正在和两颗五颜六色的弹力小球开心玩耍。"},
                {"en": "Three sweet cupcakes are decorated with four pink candles.", "cn": "三只香喷喷的小纸杯蛋糕上面，插着四根粉红色的生日蜡烛。"},
                {"en": "Five little birds perch peacefully upon the telephone wire.", "cn": "五只不知名的小鸟安安静静地并排站在高高的电线上小憩。"},
                {"en": "Practice counting every day to make numbers your best friends.", "cn": "每天认真练习数数，让数字成为你终生相伴的最亲密伙伴。"}
            ]
        },
        {
            "title": "第4章：从六到十的数字台阶",
            "description": "数字 6 到 10 的递增认知，配合生活趣味物品。",
            "sentences": [
                {"en": "Six is the tiny legs on every busy little insect.", "cn": "6 代表大自然中每一只忙忙碌碌的微小昆虫身上长着的六条腿。"},
                {"en": "A pack of colored pencils contains six vibrant shades.", "cn": "这盒全新的彩色铅笔里面，不多不少正好装有六种绚丽的色调。"},
                {"en": "Seven is the number of breathtaking colors in a rainbow.", "cn": "7 代表雨后横跨天际的美丽彩虹当中包含的七彩斑斓之色。"},
                {"en": "There are seven days that make up a complete week.", "cn": "七个晨昏轮转的明媚日子，恰好构成了完整充实的一个星期。"},
                {"en": "Eight is the flexible suction arms of a clever octopus.", "cn": "8 代表一只聪明的大章鱼在深海游动时舞动的八条吸盘触手。"},
                {"en": "A spooky black spider spins a web with eight legs.", "cn": "一只漆黑灵巧的小蜘蛛用它的八条长腿编织出一张精巧的蛛网。"},
                {"en": "Nine is the delicious donuts arranged in a baker's box.", "cn": "9 代表点心师的烘焙盒子里整整齐齐码放着的九只香甜甜甜圈。"},
                {"en": "Count nine glittering stars shining above the mountain ridge.", "cn": "数一数高耸的山脊上方，夜空中清晰闪烁着的九颗璀璨星辰。"},
                {"en": "Ten is the total of all the toes on your two feet.", "cn": "10 代表你两只小脚丫加在一起总共拥有的十个圆润脚趾头。"},
                {"en": "Clap your hands together ten times with great gusto.", "cn": "满怀欢快与激情，高高举起双手连续击掌十次！"},
                {"en": "Let us count backwards from ten all the way to one.", "cn": "让我们从十开始，倒着一直数回到一：十、九、八……一！"},
                {"en": "Six yellow ducklings swim past seven white water lilies.", "cn": "六只毛茸茸的小鸭子欢快地游过七朵洁白优雅的池塘睡莲。"},
                {"en": "Eight playful squirrels hide nine brown acorns in trees.", "cn": "八只活泼的小松鼠把九颗油亮的橡果秘密藏匿在茂密的树洞里。"},
                {"en": "Ten bright balloons soar high into the endless blue sky.", "cn": "十只色彩艳丽的气球飘飘荡荡，飞向了广袤无垠的蔚蓝晴空。"},
                {"en": "Congratulations on mastering the first ten numbers in English!", "cn": "热烈祝贺你已经完完全全精熟掌握了英语中最初的十个核心数字！"}
            ]
        },
        {
            "title": "第5章：紫色与粉色的魔法王国",
            "description": "认知高雅紫色与温柔粉色，体验童话色彩意境。",
            "sentences": [
                {"en": "Purple is the majestic color worn by noble kings and queens.", "cn": "紫色是古老传说中尊贵的国王与女王们常穿戴的尊贵华美之色。"},
                {"en": "A cluster of sweet purple grapes grows along the wooden arbor.", "cn": "一串串甘甜爽口的深紫色葡萄，沿着古朴的木葡萄架垂挂下来。"},
                {"en": "Delicate purple lavender flowers release a soothing fragrance.", "cn": "娇艳优雅的紫色薰衣草花朵散发出令人心旷神怡的舒缓芬芳。"},
                {"en": "The fairy waved her wand, leaving a trail of purple sparkles.", "cn": "小仙女轻轻挥动魔法棒，在空中留下一道如梦似幻的紫色星尘。"},
                {"en": "Draw a mystical purple butterfly landing on a lilac petal.", "cn": "画一只神秘灵动的紫色蝴蝶，正轻轻落在丁香花的花瓣尖上。"},
                {"en": "Pink is the gentle color of blossoming peach flower petals.", "cn": "粉色是春天枝头上含苞初放的粉嫩桃花花瓣所展示的温柔之色。"},
                {"en": "The newborn baby girl sleeps peacefully under a soft pink blanket.", "cn": "新降生的小女婴在柔软粉嫩的毛毯下安详静卧，睡得正香。"},
                {"en": "She enjoys a scoop of delicious strawberry ice cream in a cup.", "cn": "她正心满意足地品尝着纸杯里那一颗香甜诱人的粉色草莓冰淇淋。"},
                {"en": "A tall pink flamingo stands gracefully on one long slender leg.", "cn": "一只修长的粉色火烈鸟仅凭一只纤细的独腿，优雅自若地伫立水间。"},
                {"en": "Fold a lovely pink origami heart to give to your mother.", "cn": "用彩纸亲手折叠一颗可爱的粉红色爱心，作为礼物送给最爱的妈妈。"},
                {"en": "Purple and pink look magical together in sunset cloud paintings.", "cn": "在晚霞晕染的云朵油画里，紫与粉交相辉映，美得宛如童话梦境。"},
                {"en": "Mix white with red to create your very own pastel pink shade.", "cn": "把纯洁的白色与鲜艳的红色轻轻调和，便能调出你专属的浅粉色。"},
                {"en": "The enchanted princess wears a velvet gown of royal purple.", "cn": "童话里的奇迹公主身披一袭由皇家尊贵深紫织就的高档丝绒礼服。"},
                {"en": "Five pink balloons float beside six purple paper flowers.", "cn": "五只粉色的可爱气球，紧紧依偎在六朵手工制作的紫色纸花旁。"},
                {"en": "Your colorful imagination makes every dream shine twice as bright.", "cn": "你五彩缤纷的天马行空想象力，能让你心中的每一个梦想加倍闪耀。"}
            ]
        },
        {
            "title": "第6章：黑与白与灰色的世界",
            "description": "黑白灰中性色认知、斑马、熊猫与水墨意境。",
            "sentences": [
                {"en": "Black is the mysterious shade of the deep midnight sky.", "cn": "黑色是夜深人静万籁俱寂时，深邃无垠的夜幕所笼罩的神秘之色。"},
                {"en": "The friendly black cat purrs softly as you pet its back.", "cn": "那只通体乌黑的温顺小黑猫，在你轻抚其脊背时舒服地打着呼噜。"},
                {"en": "Dip your wooden calligraphy brush into dark black ink.", "cn": "把你的羊毫毛笔轻轻蘸进乌黑发亮、散发清香的传统墨汁里。"},
                {"en": "Black piano keys produce sharp and flat musical notes.", "cn": "钢琴上那一排排黑色的琴键，敲击出变幻莫测的半音与升降乐调。"},
                {"en": "White is the pure, clean color of fresh winter snowfall.", "cn": "白色是冬日初降的皑皑白雪所展现出的至纯至洁、不染纤尘之色。"},
                {"en": "Fluffy white clouds drift lazily across the summer sky.", "cn": "一朵朵白茫茫蓬松松的云朵，慵懒自得地漫步飘浮在夏日的天空中。"},
                {"en": "Drink a glass of wholesome white milk every single morning.", "cn": "每天清晨坚持喝下一大杯营养丰富、色泽洁白纯正的新鲜牛奶。"},
                {"en": "The graceful white swan glides across the glassy calm lake.", "cn": "那只高贵优雅的白天鹅如行云流水般，滑过平静如明镜的湖面。"},
                {"en": "Gray is the balanced neutral shade between deep black and pure white.", "cn": "灰色是介于深邃纯黑与无瑕纯白之间、从容平和的中立调和之色。"},
                {"en": "A gentle gray elephant flaps its large ears to stay cool.", "cn": "一头温顺的大灰象忽闪着宽大的两只蒲扇耳，为自己驱除酷暑。"},
                {"en": "The wise gray dolphin leaps with joy above ocean waves.", "cn": "那只睿智聪颖的灰色海豚满怀欢欣，一次次凌空跃出层层浪花。"},
                {"en": "A wild zebra wears bold stripes of alternating black and white.", "cn": "一匹野生斑马身上披着黑白分明、粗细相间的醒目条纹天然大衣。"},
                {"en": "The chubby giant panda is famous for its black and white fur.", "cn": "憨态可掬的国宝大熊猫，正是以其黑白两色相映成趣的皮毛享誉全球。"},
                {"en": "Contrast between dark and light brings depth to every sketch.", "cn": "明与暗、黑与白的强烈对比，赋予了每一幅素描画深刻的立体感。"},
                {"en": "Every color under the sun has its own special beauty to share.", "cn": "日光普照下的每一种色彩，都拥有其独一无二、无可替代的特殊魅力。"}
            ]
        },
        {
            "title": "第7章：橙色与褐色的秋日丰收",
            "description": "认知橙色与褐色，体验落叶、南瓜与秋日大地之美。",
            "sentences": [
                {"en": "Orange is the warm, cheerful color of delicious autumn pumpkins.", "cn": "橙色是秋日田野里圆滚滚、沉甸甸的美味大南瓜所具有的欢快暖意之色。"},
                {"en": "The evening sky glows with brilliant bands of gold and orange.", "cn": "落日黄昏的苍穹之上，翻滚流淌着金黄与亮橙交织的绚烂晚霞。"},
                {"en": "Peel a sweet, juicy mandarin orange to share with your family.", "cn": "剥开一只清甜多汁的蜜橘，和坐在身旁的家人们一起开开心心分享。"},
                {"en": "Crunchy orange carrots are rich in vitamins that protect your eyes.", "cn": "清脆甘甜的红萝卜富含丰富维生素，能悉心呵护你的明亮双眼。"},
                {"en": "A playful little fox with bright orange fur runs through bushes.", "cn": "一只长着一身鲜亮橘色浓密皮毛的小狐狸，机敏地穿行在灌木丛间。"},
                {"en": "Brown is the rich, fertile color of the nourishing earth.", "cn": "褐色是孕育了世间万物生灵的肥沃泥土所散发出的敦厚沉稳之色。"},
                {"en": "Sturdy tree trunks are covered in protective rough brown bark.", "cn": "高大坚固的古树主干表面，包裹着一层用于御寒防虫的粗糙棕树皮。"},
                {"en": "A fuzzy brown teddy bear sits patiently on your cozy bed.", "cn": "一只毛茸茸的棕色泰迪熊玩具，乖巧安详地坐在你温馨的小床上。"},
                {"en": "Sip a cup of hot chocolate made from roasted brown cacao beans.", "cn": "细细品尝一杯由烘焙深棕可可豆精心研磨冲调出来的香浓热巧克力。"},
                {"en": "Crunchy brown acorns fall from the majestic ancient oak tree.", "cn": "一颗颗棕褐色的坚硬小橡果，从枝繁叶茂的高大橡树顶端噼啪坠落。"},
                {"en": "Autumn leaves transform from green into brilliant orange and rusty brown.", "cn": "秋天的树叶褪去了盛夏的翠绿，蜕变幻化成了漫山遍野的火橙与铁褐。"},
                {"en": "Seven orange pumpkins sit in a row beside eight brown baskets.", "cn": "七只圆滚滚的橙色大南瓜排成一排，整齐摆放在八只棕色竹编竹篓旁。"},
                {"en": "The little squirrel buries its brown nuts beneath fallen leaves.", "cn": "勤劳敏捷的小松鼠把积攒过冬的褐色坚果，悄悄埋藏在金黄的落叶底下。"},
                {"en": "Earth tones give our homes a sense of deep comfort and safety.", "cn": "这种回归大地的沉稳色调，赋予了我们的居所一份无与伦比的安全与依恋。"},
                {"en": "Nature paints with all colors to welcome the harvest season.", "cn": "大自然挥毫泼洒世间全部色彩，热情欢庆五谷丰登的金秋丰收时节。"}
            ]
        },
        {
            "title": "第8章：认识基础几何图形",
            "description": "圆形、正方形、三角形、长方形与生活实物匹配。",
            "sentences": [
                {"en": "A circle is perfectly round with no corners and no straight lines.", "cn": "圆形是一个没有棱角、没有笔直线条，处处皆圆润对称的完美图形。"},
                {"en": "The golden sun and the full moon are wonderful examples of circles.", "cn": "天空中的金色太阳与皎洁满月，都是大自然赋予我们最奇妙的圆形例证。"},
                {"en": "A coin, a clock face, and a pizza pie are all circular shapes.", "cn": "一枚小硬币、一个大挂钟的钟盘以及一张香喷喷的披萨饼全都是圆形。"},
                {"en": "A square has four straight sides of completely equal length.", "cn": "正方形拥有四条长短完完全全对等、笔直挺拔的边框线条。"},
                {"en": "A wooden building block and a picture frame can be square.", "cn": "一块小巧的木质积木或者一个精美的照片相框，往往都呈现出正方形。"},
                {"en": "A triangle has three sharp corners and three straight sides.", "cn": "三角形天生具有三个锐利的边角，以及三条紧紧相连的笔直边线。"},
                {"en": "A crunchy slice of watermelon can be cut into a triangle.", "cn": "把甘甜多汁的大西瓜切下一块来，往往就是一块规整诱人的三角形。"},
                {"en": "The roof of a cozy house often looks like a steady triangle.", "cn": "一座座遮风避雨的温馨房屋屋顶，通常都搭建成结构极其稳固的三角形。"},
                {"en": "A rectangle has four sides, with opposite sides being equal.", "cn": "长方形拥有四条对边长度分别严格相等、棱角分明的笔直线框。"},
                {"en": "Your classroom blackboard and your storybook are rectangles.", "cn": "你每天注视的教室大黑板以及手中的故事绘本，全都是标准的长方形。"},
                {"en": "An oval is an elongated circle that looks just like a bird's egg.", "cn": "椭圆形是一个被轻轻拉长了的圆形，外形轮廓酷似一枚小小的鸟蛋。"},
                {"en": "Look around your bedroom to spot all these fascinating shapes.", "cn": "快抬起头环顾一下你的卧室，找一找身边隐藏的所有奇妙几何图形吧。"},
                {"en": "Shapes and colors combine to build everything we see and touch.", "cn": "千变万化的几何形态与斑斓色彩相结合，构筑起了我们所目睹的一切事物。"},
                {"en": "Can you draw a yellow circle inside a big blue square?", "cn": "你能在蔚蓝色的巨大正方形正中心，画出一枚金灿灿的完美圆形吗？"},
                {"en": "Geometry turns everyday observation into an exciting adventure.", "cn": "生动有趣的几何知识，能把日常生活的细致观察变成一场激动人心的冒险。"}
            ]
        },
        {
            "title": "第9章：数数游戏与大小比较",
            "description": "比较大与小、多与少、高与矮，结合数字进阶。",
            "sentences": [
                {"en": "The elephant is big and heavy, while the tiny mouse is small.", "cn": "大象的身躯庞大又沉重，而那只小巧玲珑的老鼠则身材娇小。"},
                {"en": "A giant watermelon is much bigger than a single round grape.", "cn": "一颗硕大沉重的大西瓜，体量远比一颗圆溜溜的葡萄大得多。"},
                {"en": "The tall giraffe stretches high to reach green canopy leaves.", "cn": "高高耸立的长颈鹿能够轻松伸长脖颈，够到高耸树冠上的嫩绿树叶。"},
                {"en": "The little turtle is short and stays close to the grassy ground.", "cn": "小乌龟的身材矮小笨拙，走起路来紧紧贴着青青草地缓缓爬行。"},
                {"en": "Five shiny red apples are more than three juicy green pears.", "cn": "五颗红彤彤的鲜苹果在数量上，明显多于三只清脆的绿香梨。"},
                {"en": "Two fluffy white clouds are fewer than seven twinkling stars.", "cn": "天空中两朵孤零零的白云，在数量上少于七颗闪烁的耀眼星辰。"},
                {"en": "This wooden ruler is long, but this pencil stub is very short.", "cn": "这把笔直的木格尺很长，但是这根用短了的小铅笔头却非常短小。"},
                {"en": "Compare the heights of your classmates when standing in line.", "cn": "当大家在走廊排成一纵队时，比一比班上各位小同学的个头高矮。"},
                {"en": "Which balloon floats higher into the breezy afternoon sky?", "cn": "猜一猜哪一只彩色的气球，能在微风拂面的午后天空中飞得更高？"},
                {"en": "Count the steps as you climb up the wooden staircase at home.", "cn": "当你一步步登上家里的木质楼梯台阶时，一步一个脚印大声数出来。"},
                {"en": "Ten is greater than eight, and three is smaller than six.", "cn": "10 在数学量级上大于 8，而数字 3 则明显小于数字 6。"},
                {"en": "Group your toy building blocks from the smallest to the largest.", "cn": "把你的玩具积木从小到大，按体量大小依次整整齐齐排成一条龙。"},
                {"en": "Understanding sizes and quantities makes our minds sharper.", "cn": "准确理解尺寸与数量之间的对应关系，能让我们的小脑瓜变得更加敏捷。"},
                {"en": "Every tiny baby step adds up to a giant leap over time.", "cn": "日积月累走出的每一个微小稚嫩的足迹，终将汇聚成跨越山海的惊人飞跃。"},
                {"en": "Learning to measure and count is a superpower for young minds.", "cn": "掌握测量与数数的本领，是小读者们开启智慧宝库的一项超级超能力。"}
            ]
        },
        {
            "title": "第10章：五彩缤纷大联欢派对",
            "description": "融合色彩、数字、图形与生活欢庆场景。",
            "sentences": [
                {"en": "Today we are throwing a giant rainbow party for our friends.", "cn": "今天我们要为所有的好伙伴们，举办一场盛大热闹的彩虹狂欢派对！"},
                {"en": "Hang ten colorful paper lanterns along the garden fence.", "cn": "沿着花园的木栅栏，高高挂起十只五彩斑斓的精美小纸灯笼。"},
                {"en": "Inflate five bright red balloons and five sky-blue balloons.", "cn": "吹起五只鲜艳火红的气球，再吹起五只蔚蓝如洗的晴空色气球。"},
                {"en": "Decorate the long table with a bright yellow floral tablecloth.", "cn": "在长餐桌上铺上一块绣着明艳黄花的漂亮大桌布。"},
                {"en": "Stack three square chocolate cakes beside four round apple pies.", "cn": "把三块方形浓香巧克力蛋糕，端正摆放在四盘圆形苹果派旁边。"},
                {"en": "Pour sweet pink lemonade into eight clear crystal glasses.", "cn": "把酸甜可口的粉色柠檬汽水，小心注入八只晶莹剔透的水晶玻璃杯中。"},
                {"en": "Wear your favorite colorful party hat shaped like a cone.", "cn": "戴上你平时最喜爱的锥形彩色生日派对小尖帽。"},
                {"en": "Play a cheerful clapping game where everyone dances to music.", "cn": "大家一起玩欢快的拍手传花小游戏，伴着音乐尽情载歌载舞。"},
                {"en": "Count how many smiling friends are gathered in the room today.", "cn": "快数一数今天整个大房间里，总共汇聚了多少张洋溢着欢笑的小脸蛋。"},
                {"en": "Cut the rainbow cake into twelve delicious, equal triangular slices.", "cn": "把这块松软诱人的大彩虹蛋糕，仔仔细细切成十二块等大的三角形切片。"},
                {"en": "Blow out all the sparkling birthday candles in one giant puff.", "cn": "深吸一口气，一口气把蛋糕上所有闪烁的生日蜡烛通通吹灭。"},
                {"en": "Sing the happy birthday anthem together with loud, joyful voices.", "cn": "大家一起扯开嗓门，用响亮欢畅的童声齐声高唱生日快乐歌。"},
                {"en": "Colors, numbers, and cheerful shapes surround us every day.", "cn": "绚烂的色彩、神奇的数字与多姿的几何，每分每秒都环绕在我们身边。"},
                {"en": "You have mastered all colors and numbers with flying colors!", "cn": "你已经以超凡出众的优异表现，彻底精熟掌握了所有的颜色与数字！"},
                {"en": "Keep exploring the wonderful world of English with boundless curiosity.", "cn": "怀揣着永无止境的好奇心，继续无畏探索绚丽博大的精彩英语世界吧！"}
            ]
        }
    ]
}

COURSE_KIDS_MANNERS = {
    "meta": {
        "id": "kids-manners",
        "title": "懂礼貌好宝宝习惯养成",
        "category": "kids",
        "categoryName": "少儿英语",
        "coverGradient": "from-blue-400 to-indigo-600",
        "icon": "🌟",
        "description": "专为培养高情商、讲文明懂礼貌好宝宝设计的习惯养成课程，涵盖礼貌用语、餐桌礼仪、排队守序与关爱他人。",
        "difficulty": "beginner",
        "tags": ["少儿英语", "习惯养成", "礼貌用语", "情商启蒙"]
    },
    "chapters": [
        {
            "title": "第1章：神奇礼貌用语魔法词",
            "description": "掌握 please, thank you, sorry, excuse me 四大黄金礼貌词。",
            "sentences": [
                {"en": "Please is a golden key that opens doors of kindness everywhere.", "cn": "“请”是一把黄金铸就的魔法钥匙，能在任何地方叩开友善的大门。"},
                {"en": "Always say please whenever you ask someone for assistance.", "cn": "每当你需要请求别人为你提供帮助时，一定要先礼貌地说一声“请”。"},
                {"en": "Thank you shows sincere gratitude for love and helpful deeds.", "cn": "“谢谢”表达的是发自肺腑的由衷感恩，感谢他人付出的关爱与善举。"},
                {"en": "Remember to say thank you when you receive a lovely gift.", "cn": "当别人递给你一份心意满满的可爱礼物时，千万别忘了说声“谢谢”。"},
                {"en": "Excuse me is the polite phrase to use when passing by.", "cn": "当你想从别人身边穿行借过时，“借光打扰一下”是最得体的礼貌用语。"},
                {"en": "Say excuse me before interrupting an adult conversation politely.", "cn": "在礼貌打断大人们正在进行的交谈之前，先温和地道一声“打扰一下”。"},
                {"en": "I am sorry expresses honest regret when we make mistakes.", "cn": "当我们无心犯下过错或失误时，“对不起”能表达最真挚坦诚的歉意。"},
                {"en": "Saying sorry sincerely helps heal hurt feelings and restores friendship.", "cn": "真诚地道一声对不起，能够抚平被伤害的心灵，让友谊重归于好。"},
                {"en": "You are welcome is the gracious response to a warm thank you.", "cn": "“不客气不用谢”，是对他人热情致谢最优雅从容的温和回应。"},
                {"en": "These four magic words make the whole world friendlier and brighter.", "cn": "这四句神奇的魔法礼貌用语，能让整个世界变得更加友善与温暖。"},
                {"en": "Smile warmly as you speak each courteous phrase out loud.", "cn": "当你大声说出每一句礼貌用语时，脸上记得带上一抹温暖真挚的笑意。"},
                {"en": "Polite words are easy to learn and bring immense happiness.", "cn": "彬彬有礼的文明语言学起来毫不费力，却能给身边所有人带来极大的快乐。"},
                {"en": "Practice using polite words at home, at school, and in parks.", "cn": "无论在家里、在学校还是在公园里，都要坚持主动使用这些礼貌用语。"},
                {"en": "A polite child earns the deep respect and love of everyone.", "cn": "一个讲文明懂礼貌的好孩子，走到哪里都能赢得大家的由衷尊重与喜爱。"},
                {"en": "Make courteous speech your natural daily habit from today on.", "cn": "从今天起，让优雅文明的言谈举止化作你习以为常的日常良好习惯。"}
            ]
        },
        {
            "title": "第2章：温文尔雅的小绅士小淑女餐桌礼仪",
            "description": "餐前洗手、端坐进餐、细嚼慢咽与餐桌感谢。",
            "sentences": [
                {"en": "Wash your hands thoroughly with soap before sitting at the table.", "cn": "在坐到餐桌旁准备就餐之前，先用洗手液把双手仔仔细细洗干净。"},
                {"en": "Wait for everyone to be seated before taking your first bite.", "cn": "在吃第一口食物之前，耐心等候同桌的所有长辈和同伴完全就座。"},
                {"en": "Unfold your cloth napkin and place it gently on your lap.", "cn": "轻轻展开你的布餐巾，平平整整地平铺在自己的大腿膝盖上方。"},
                {"en": "Sit upright on your chair without slouching over your plate.", "cn": "在餐椅上端端正正坐直身体，切忌趴在或歪倒在自己的餐盘上方。"},
                {"en": "Chew your food quietly with your mouth closed at all times.", "cn": "咀嚼口中的食物时时刻闭紧双唇，不要发出吧唧嘴的声响。"},
                {"en": "Never speak while you have food inside your mouth.", "cn": "当嘴里还塞着饭菜的时候，千万不要急着开口大声讲话。"},
                {"en": "Please pass the salt bowl, said the polite young boy.", "cn": "“请把那个盛盐的小碗递给我一下好吗”，懂礼貌的小男孩轻声请求。"},
                {"en": "Hold your fork and spoon gently with steady, clean fingers.", "cn": "用平稳干净的小手指，端端正正地持握好你的餐叉和小勺子。"},
                {"en": "Take manageable small bites so you can swallow food comfortably.", "cn": "每次只取适量的小口食物，这样才能从容舒服、不易噎着地慢慢吞咽。"},
                {"en": "Do not reach across another person's plate to grab food.", "cn": "绝对不要把胳膊横跨伸过别人的餐盘上方，去争抢远处的食物。"},
                {"en": "Thank the chef and your family for preparing this delicious meal.", "cn": "由衷感谢大厨和家人为我们精心烹饪准备的这一顿丰盛美味佳肴。"},
                {"en": "Ask to be excused politely before leaving the dinner table.", "cn": "在准备起身离开餐桌之前，记得礼貌地征得长辈的同意。"},
                {"en": "Carry your empty plate and utensils over to the kitchen sink.", "cn": "主动端起自己吃得干干净净的空盘子和餐具，送到厨房水槽中去。"},
                {"en": "Wipe your hands and mouth clean before running off to play.", "cn": "在欢天喜地跑去玩耍之前，记得把自己的小手和嘴巴擦得干干净净。"},
                {"en": "Good table manners show high self-respect and consideration for others.", "cn": "优雅端庄的餐桌礼仪，彰显的是高度的自我尊重以及对同行者的体贴关怀。"}
            ]
        },
        {
            "title": "第3章：玩具分享与团队合作的快乐",
            "description": "轮流玩耍、爱护公物、化解小矛盾与齐心协力。",
            "sentences": [
                {"en": "Sharing your favorite toys doubles the fun and joy of playing.", "cn": "大方分享你最心爱的玩具，能让玩耍的快乐与欢笑在一瞬间翻倍。"},
                {"en": "May I please take a turn playing with the wooden train set?", "cn": "我可以轮流玩一会儿这套精致的木质小火车玩具吗，谢谢？"},
                {"en": "Waiting for your turn patiently shows incredible maturity and patience.", "cn": "心平气和、耐心地排队等候轮到自己，展现出令人赞叹的懂事与耐性。"},
                {"en": "Handle delicate toys gently so they do not break or get lost.", "cn": "轻拿轻放那些精细的玩具，这样它们才不会被摔坏或者无端遗失。"},
                {"en": "Two heads work together much better than one when building towers.", "cn": "在齐心协力搭建高耸积木塔时，两颗小脑袋合作远胜过一个人单打独斗。"},
                {"en": "If your friend feels sad, offer them a warm comforting smile.", "cn": "如果身旁的小伙伴感到沮丧难过，请主动向他送上一记温暖的抚慰微笑。"},
                {"en": "Never snatch toys away from another child's hands forcefully.", "cn": "绝对不要强行从别的小朋友手里硬生生抢夺他正在玩的玩具。"},
                {"en": "Use calm, gentle words to resolve minor disagreements peacefully.", "cn": "用平心静气、温和理性的言语，从容和平地化解小伙伴之间的小摩擦。"},
                {"en": "Let us take turns sliding down the big yellow slide outside.", "cn": "让我们排好队一个接一个，轮流从户外那架黄色大滑梯上滑下去。"},
                {"en": "Thank you for sharing your colored crayons with me today.", "cn": "非常感谢你今天如此大方地把你这盒彩色蜡笔借给我一起使用。"},
                {"en": "Clean up all scattered toys and put them neatly back into bins.", "cn": "玩耍结束之后，把散落一地的玩具收拾利索，整整齐齐放回收纳箱。"},
                {"en": "Teamwork turns a hard task into a swift and joyful celebration.", "cn": "团队通力协作，能把一项看似艰巨的苦差事变成一场迅速而快乐的盛会。"},
                {"en": "True friends support one another through thick and thin.", "cn": "真正的好朋友无论顺境还是逆境，始终都会同心协力彼此扶持。"},
                {"en": "A generous heart is the greatest treasure a child can possess.", "cn": "一颗慷慨豁达、乐于分享的宽仁之心，是小读者此生最值得骄傲的至宝。"},
                {"en": "Together we make our classroom a welcoming and loving family.", "cn": "齐心协力携手并肩，我们共同把这间教室打造成了一个充满爱的温暖大家庭。"}
            ]
        },
        {
            "title": "第4章：公共场所的守序小模范",
            "description": "图书馆轻声细语、排队守序、爱护花草与垃圾入桶。",
            "sentences": [
                {"en": "Speak in a soft, whispering voice inside the public library.", "cn": "走进安静严肃的公共图书馆，要用轻柔温和的耳语声音低声交谈。"},
                {"en": "Walk quietly on your tiptoes so you do not disturb readers.", "cn": "轻轻踮起脚尖放慢脚步，切勿大吵大闹打扰到其他正在专心阅读的人。"},
                {"en": "Stand patiently in a straight line while waiting for the bus.", "cn": "在车站等候公共汽车进站时，安安静静、耐心地排成一条整齐的直线。"},
                {"en": "Do not push or shove others when boarding public transportation.", "cn": "在搭乘公共交通工具登车时，绝对不可以推搡或拥挤身边的其他乘客。"},
                {"en": "Offer your seat politely to elderly passengers or pregnant mothers.", "cn": "主动有礼貌地把自己的座位，让给上了年纪的长辈或行动不便的孕妇阿姨。"},
                {"en": "Never pluck fresh blossoms or snap branches in the city park.", "cn": "在漫步城市公园时，千万不可随意采摘娇嫩的花朵或折断花草树枝。"},
                {"en": "Walk gently on designated paths without trampling green lawns.", "cn": "老老实实走在指定的小石板路上，不要随意踩踏践踏那片绿油油的草坪。"},
                {"en": "Always dispose of fruit peels and candy wrappers into trash cans.", "cn": "随手吃完的果皮和糖纸，一定要毫无例外地扔进身边的垃圾桶分类箱内。"},
                {"en": "If you see litter on the ground, help pick it up responsibly.", "cn": "如果你看到地上散落着废纸杂物，以高度的责任心主动捡起扔进垃圾桶。"},
                {"en": "Cover your mouth with a tissue or your elbow when coughing.", "cn": "当忍不住想咳嗽或打喷嚏时，务必用纸巾或自己的手肘衣袖遮掩口鼻。"},
                {"en": "Wash your hands promptly after blowing your nose outside.", "cn": "在户外擤完鼻涕之后，尽快找地方用洗手液把双手清洗干净。"},
                {"en": "Hold the door open courteously for the person walking behind you.", "cn": "推门而过时，体贴有礼貌地顺手帮走在自己身后的人多扶一会儿大门。"},
                {"en": "Keep public spaces clean, tidy, and peaceful for all citizens.", "cn": "爱护公共空间，为所有的广大市民维系一处干净整洁、安宁祥和的环境。"},
                {"en": "Good citizenship begins with small, considerate daily actions.", "cn": "卓越非凡的公民道德素养，正是发轫于日常生活中一个个微小体贴的善举。"},
                {"en": "You are a shining shining role model in our modern society.", "cn": "你的一言一行，堪称我们现代文明社会当中一颗熠熠生辉的耀眼小模范！"}
            ]
        },
        {
            "title": "第5章：尊敬长辈与孝亲友爱",
            "description": "听父母教导、问候爷爷奶奶、体贴家人与主动分担。",
            "sentences": [
                {"en": "Listen attentively when your loving parents offer wise advice.", "cn": "当慈爱的父母为你提供饱含人生智慧的谆谆教导时，务必侧耳倾听。"},
                {"en": "Greet your grandparents with a warm embrace and respectful voice.", "cn": "用深情的拥抱和恭敬温和的语调，向家中的爷爷奶奶外公外婆亲切问好。"},
                {"en": "Help grandfather find his reading glasses when he misplaces them.", "cn": "当老爷爷一时想不起把老花镜放在哪里时，主动耐心地帮他四处找找。"},
                {"en": "Pour a warm cup of fragrant tea for tired mother returning from work.", "cn": "为下班归来一脸倦容的辛劳母亲，懂事地端上一杯温润甘甜的热茶。"},
                {"en": "Rub father's sore shoulders gently to help him relax.", "cn": "用稚嫩的小手轻轻帮疲惫的父亲揉揉酸痛的肩膀，帮他舒缓放松。"},
                {"en": "Never shout or speak disrespectfully to your elders at home.", "cn": "在家里绝对不可以对着长辈大吼大叫，或者用无礼轻慢的言辞顶撞长辈。"},
                {"en": "Take off your outdoor shoes and place them neatly at the entryway.", "cn": "回到家中换下室外的鞋子，工工整整地摆放在玄关鞋架的最底层。"},
                {"en": "Help fold clean laundry and pair up socks on laundry day.", "cn": "在洗衣服的日子里，主动协助家人叠好干净衣物，给棉袜逐一配对。"},
                {"en": "Set the dinner table with bowls and chopsticks before mealtime.", "cn": "在开饭之前，主动把碗筷整整齐齐地摆放在餐桌的每个座位前。"},
                {"en": "Show deep patience when grandparents tell stories from their youth.", "cn": "当爷爷奶奶满怀深情地忆及他们年轻时的往昔岁月时，展现出极大的耐心。"},
                {"en": "Remember family birthdays and create handmade greeting cards with love.", "cn": "牢记家中每一位亲人的生日，用满满的爱心亲手绘制温馨的生日贺卡。"},
                {"en": "Say good night and kiss your parents before going to sleep.", "cn": "在钻进被窝进入梦乡之前，向爸爸妈妈道一声晚安并送上一个香甜的吻。"},
                {"en": "Family love is the deepest anchor supporting your life journey.", "cn": "血浓于水的家庭深爱，是你漫漫人生求索征途当中最坚若磐石的避风港湾。"},
                {"en": "Honoring your parents brings long life, joy, and peace of mind.", "cn": "孝敬双亲、尊师重道，能给一个人的心灵带来无尽的长久福泽与泰然宁静。"},
                {"en": "Your caring filial heart makes your home radiant with warm sunshine.", "cn": "你那一颗懂得感恩孝亲的赤子之心，让你的温馨小家时刻洋溢着如阳春般的暖意。"}
            ]
        },
        {
            "title": "第6章：诚实守信的小勇士",
            "description": "勇敢认错、不撒谎、拾金不昧与言出必行。",
            "sentences": [
                {"en": "Honesty is the most priceless gem that shines within human character.", "cn": "诚实正直是一个人崇高的人格殿堂深处，最为璀璨夺目、价值连城的无价之宝。"},
                {"en": "Always tell the honest truth, even when doing so feels difficult.", "cn": "即便有时候讲出事实真相会令人万分艰难忐忑，也务必要坚持讲大实话。"},
                {"en": "If you accidentally break a ceramic bowl, admit your mistake bravely.", "cn": "如果不小心失手打碎了一只瓷碗，勇敢坦荡地站出来承认自己的过失。"},
                {"en": "A brave child takes responsibility for their actions without excuses.", "cn": "一个勇敢担当的好孩子，从不为自己的失误寻找任何虚假的推脱借口。"},
                {"en": "Never tell lies to cover up mistakes, for lies multiply like weeds.", "cn": "绝对不要妄图用谎言去遮掩过失，因为谎言会像野草一样滋生泛滥成灾。"},
                {"en": "Return lost items promptly to their rightful owner or the teacher.", "cn": "拾获他人遗失的物品时，尽快物归原主或者如数转交给老师妥善处理。"},
                {"en": "Keep your promises faithfully once you give your solemn word.", "cn": "一旦你郑重许下了诺言，就必须信守誓言、言出必行、一诺千金。"},
                {"en": "Trust takes a long time to build but can vanish in a single moment.", "cn": "人与人之间的真诚信任需要漫长岁月的辛苦沉淀，但往往一瞬间便能轰然崩塌。"},
                {"en": "Cheating in games or classroom quizzes destroys true accomplishment.", "cn": "在游戏或者课堂小测验中投机取巧作弊，会彻底摧毁真正的成就与尊严。"},
                {"en": "Be proud of your honest efforts, regardless of the final score.", "cn": "无论最终的卷面分数高低，都为自己付出过的踏实诚恳的努力而自豪。"},
                {"en": "A person of integrity sleeps with a peaceful and clear conscience.", "cn": "一个光明磊落、恪守操守的正人君子，每晚入睡时心中都充满了坦荡与安宁。"},
                {"en": "Praise your friends when they demonstrate remarkable courage and honesty.", "cn": "当身旁的小伙伴展现出难能可贵的勇气与诚实时，毫不吝啬地为他喝彩点赞。"},
                {"en": "Truthfulness is the bedrock of lifelong friendship and respect.", "cn": "讲求诚信求真务实，是铸就历久弥坚的终身友谊与受人尊崇的基石。"},
                {"en": "Stand up for the truth even when standing completely alone.", "cn": "即便在身旁空无一人独力难支的艰难时刻，也要义无反顾为真理挺身而出。"},
                {"en": "Your honest heart lights up a path of honor wherever you travel.", "cn": "你那一颗赤诚坦荡的心灵，无论走到天涯海角都能为你照亮尊严与荣耀的大道。"}
            ]
        },
        {
            "title": "第7章：关爱与保护弱小生命",
            "description": "爱护小动物、关爱弱者、同理心与善良的萌芽。",
            "sentences": [
                {"en": "Treat all animals, large and small, with gentleness and deep respect.", "cn": "对待这世间所有大大小小的动物生灵，都要心怀温柔与由衷的尊重。"},
                {"en": "Never pull a cat's tail or tease a dog while it is eating food.", "cn": "绝对不要去拉扯小猫咪的尾巴，也不要在小狗狗专心进食时故意去挑逗它。"},
                {"en": "Feed the wild birds with wholesome breadcrumbs during chilly winters.", "cn": "在凛冽严寒的冬日里，用营养的全麦面包屑去喂养忍饥挨冻的野鸟。"},
                {"en": "Fill a shallow bowl with fresh water for thirsty backyard creatures.", "cn": "在后院里放置一个盛满纯净清水的小浅碗，方便口渴的小动物随时饮水。"},
                {"en": "Support a classmate who feels shy, left out, or struggles to learn.", "cn": "热情主动地去扶持那些性格内向害羞、被冷落或者在学习上遇到困难的同学。"},
                {"en": "Invite the lonely boy standing by the fence to join your game.", "cn": "真诚邀请那位孤单站在栅栏旁发呆的小男孩，加入到你们的欢乐游戏中来。"},
                {"en": "Stand firmly against bullying, protecting those who cannot defend themselves.", "cn": "旗帜鲜明地坚决抵制任何欺凌行为，挺身保护那些无力自卫的弱小同伴。"},
                {"en": "Words can wound deeper than swords, so speak only words of healing.", "cn": "粗暴恶劣的话语伤人甚至深过利剑，因此我们口中所出的必须是温暖疗愈之词。"},
                {"en": "Help an injured insect off the busy footpath into the soft grass.", "cn": "把误入人来人往喧闹步道而受伤的小昆虫，小心移步放回安全的青草丛中。"},
                {"en": "Kindness does not require wealth; it requires only a loving human heart.", "cn": "行善积德根本无需坐拥万贯家财，它所需要的仅仅是一颗懂得去爱的仁慈之心。"},
                {"en": "A gentle touch brings comfort to a frightened, trembling shelter puppy.", "cn": "一次温柔深情的抚摸，便能给一只受惊吓瑟瑟发抖的收容所幼犬带去无尽安慰。"},
                {"en": "Celebrate the unique differences that make each individual special.", "cn": "由衷赞赏并尊重那些让每一个生命个体各不相同、熠熠生辉的独特个性。"},
                {"en": "Empathy is feeling another's sorrow inside your own loving heart.", "cn": "真正的同理心，就是把你深爱之人的哀伤真切地感受在自己的心坎之中。"},
                {"en": "By lifting others up, you elevate your own spirit to great heights.", "cn": "在弯下腰伸出双手扶起他人的过程中，你自己的精神境界也登临崇高顶峰。"},
                {"en": "The world becomes heaven on earth when kindness guides every human deed.", "cn": "当仁善与仁爱指引着人类的每一个行动时，人间便化作了至善至美的美丽天堂。"}
            ]
        },
        {
            "title": "第8章：安全自护与警惕意识",
            "description": "过马路安全、不跟陌生人走、背诵父母电话与紧急求助。",
            "sentences": [
                {"en": "Safety is your top priority in every outdoor adventure and activity.", "cn": "在每一次户外冒险与探索活动中，人身安全始终是你排在第一位的头等大事。"},
                {"en": "Memorize your parents' mobile phone numbers and your home address clearly.", "cn": "清清楚楚、滚瓜烂熟地牢牢背诵下父母的手机号码以及自家的家庭住址。"},
                {"en": "Never accept candy, sweet drinks, or toys from unfamiliar strangers.", "cn": "绝对不要接受任何不熟悉的陌生人递给你的糖果、甜饮料或者诱人的玩具。"},
                {"en": "Never walk away with a stranger, no matter what excuse they invent.", "cn": "无论陌生人编造出多么看似合理的托辞借口，绝对不要跟陌生人离开半步。"},
                {"en": "If a stranger grabs you, shout loudly: You are not my father!", "cn": "如果有不怀好意的陌生人企图硬拉你，用尽全身力气大声呼喊：“你不是我爸爸！”"},
                {"en": "Look left, look right, and look left again before crossing any street.", "cn": "在横穿任何一条马路之前，先看左、再看右、再看左，彻底确认安全再通行。"},
                {"en": "Always hold an adult's hand firmly while walking through crowded markets.", "cn": "走在人流如织拥挤喧闹的集市街头时，务必紧紧握住大人的手绝不松开。"},
                {"en": "Wear a certified protective helmet whenever you ride your bicycle or scooter.", "cn": "无论何时骑乘你的脚踏车或滑板车，都必须规范佩戴通过质量认证的护头头盔。"},
                {"en": "Fasten your knee pads and elbow pads to prevent scrapes and bruises.", "cn": "把护膝和护肘穿戴严实，全方位防止意外摔倒造成皮肉擦伤或挫伤。"},
                {"en": "Never touch electrical outlets, dangling wires, or sharp kitchen knives.", "cn": "绝对不要伸手触摸带电的插座插孔、悬空的电线或者锋利的厨房刀具。"},
                {"en": "Stay far away from open cooking fires, boiling pots, and hot stoves.", "cn": "时刻与熊熊燃烧的炉火明火、滚沸的热汤锅以及高温灶台保持安全距离。"},
                {"en": "Know the emergency telephone number to summon police officers or firefighters.", "cn": "熟练掌握遭遇紧急险情时，呼叫人民警察或消防救援队伍的紧急求助热线。"},
                {"en": "If you get lost in a shopping mall, find a security guard immediately.", "cn": "在大型购物商场万一不慎走失，立刻寻找身着制服的商场安保叔叔寻求帮助。"},
                {"en": "Your personal body is precious, private, and belongs entirely to you alone.", "cn": "你自己的身体是无比珍贵尊严的个人隐私，百分之百独属于你一个人。"},
                {"en": "Smart safety habits ensure you enjoy endless healthy, joyful years ahead.", "cn": "聪明警醒的安全自护好习惯，能保卫你尽情畅享未来漫长岁月的健康与幸福。"}
            ]
        },
        {
            "title": "第9章：整洁自律与自己的事情自己做",
            "description": "整理床铺、按时作息、自己洗袜子与自立自强。",
            "sentences": [
                {"en": "Independence begins with doing your own small daily chores independently.", "cn": "自立自强的人生辉煌开端，正是从独立自主完成自己的点滴日常小事做起。"},
                {"en": "Make your bed neatly every morning as soon as your feet hit the floor.", "cn": "每天清晨双脚刚一落地，第一件事就是把自己的小被褥整理得平平整整。"},
                {"en": "Hang up your coat in the wardrobe rather than dropping it on chairs.", "cn": "回到家把大衣整齐挂进衣柜里，而不是随手扔在房间的椅子或沙发上。"},
                {"en": "Sort your storybooks neatly by height and theme upon your bookshelves.", "cn": "按照高矮尺寸与故事主题，把绘本整整齐齐分类码放在自己的小书架上。"},
                {"en": "Put dirty clothing directly into the laundry basket in the washroom.", "cn": "脱下来的换洗脏衣服，毫不犹豫地直接投进卫生间的脏衣收纳筐里。"},
                {"en": "Learn to wash your own small socks and handkerchiefs with soap foam.", "cn": "学着用肥皂泡沫，亲手把自己的小袜子和手帕搓洗得一尘不染洁白如新。"},
                {"en": "Pack your school backpack thoughtfully the night before every school day.", "cn": "在每一个上学日的头天夜晚，深思熟虑地把第二天所需的书包文具收拾妥当。"},
                {"en": "Sharpen your pencils and check your eraser so you are fully prepared.", "cn": "把铅笔削得尖尖的，检查好橡皮擦，以做足百分之百准备的从容姿态迎接上课。"},
                {"en": "Manage your screen time wisely, turning off devices without being told.", "cn": "明智自律地管理电子屏幕的使用时间，无需长辈再三催促自觉主动关掉设备。"},
                {"en": "Stick to a consistent bedtime so your brain and body rest completely.", "cn": "坚持恪守规律的就寝作息时间，让你的大脑中枢和全身骨骼肌肉得到彻底休息。"},
                {"en": "A tidy room creates a calm, organized, and creative state of mind.", "cn": "一个干净整洁井井有条的房间，能滋养出一颗从容不迫、充满创造力的心境。"},
                {"en": "Self-discipline is the supreme bridge between your wishes and accomplishments.", "cn": "高度的自律与自制力，是架设在你美好的美好心愿与实质成就之间的最高桥梁。"},
                {"en": "Be proud of every task you finish entirely on your own strength.", "cn": "为你完完全全凭借自己的双手独立完成的每一项小小任务，而感到无比自豪。"},
                {"en": "You are growing up into a capable, responsible, and self-reliant youth.", "cn": "你正在一天天茁壮成长为一个有担当、有能力且能够独当一面的优秀少年。"},
                {"en": "Keep building solid habits that will serve you throughout your lifetime.", "cn": "持续铸牢这些优秀的自律习惯，它们必将成为让你终生获益无穷的宝贵基石。"}
            ]
        },
        {
            "title": "第10章：感恩生命与心怀大爱",
            "description": "感恩大自然、感恩生活、乐于助人与快乐成长总结。",
            "sentences": [
                {"en": "Gratitude unlocks the absolute fullness and hidden richness of life.", "cn": "常怀一颗感恩之心，能彻底开启生命那无与伦比的丰盈厚度与深邃富足。"},
                {"en": "Give thanks for the golden sun that warms the fertile Earth each dawn.", "cn": "由衷感谢每个拂晓破晓时分，把无私暖意与光明播撒在沃土之上的金色太阳。"},
                {"en": "Give thanks for fresh pure water that quenches thirst and sustains living things.", "cn": "由衷感谢那甘洌纯净、润物无声，滋润万物生灵生命生息的澄澈泉水。"},
                {"en": "Give thanks for delicious wholesome meals shared with the family we adore.", "cn": "由衷感谢我们能够与挚爱的至亲家人围坐在一起，共享的每顿营养美味佳肴。"},
                {"en": "Give thanks for wise teachers who patiently illuminate the path of knowledge.", "cn": "由衷感谢那些谆谆善诱、循循善诱，以满腔热忱为我们点亮知识大道的辛勤良师。"},
                {"en": "Give thanks for true loyal friends who stand beside us in games and study.", "cn": "由衷感谢那些在学习与游戏中始终与我们并肩作战、不离不弃的知心好友。"},
                {"en": "A thankful heart sees blessings, miracles, and beauty in everyday moments.", "cn": "一颗感恩的心，总能在平平常常的日常点滴中洞察到无尽的恩赐、奇迹与至美。"},
                {"en": "Say kind loving words to your parents every single morning and evening.", "cn": "在每一个清晨与每一个夜晚，都亲切地对爸爸妈妈说上几句饱含温情的贴心话。"},
                {"en": "Plant a green flower seed and nurture it with water and tender patience.", "cn": "亲手种下一粒绿色花卉的种子，用甘甜的清水与温柔的恒心耐心呵护它抽芽。"},
                {"en": "Express gratitude through noble actions, helping others with a generous soul.", "cn": "用崇高磊落的实际行动去践行感恩，以慷慨无私的胸怀去随时扶持身边他人。"},
                {"en": "Joy multiplies when shared freely with those who need it most.", "cn": "当快乐被毫无保留地分享给那些身处逆境最渴望温暖的人时，快乐便会成倍放大。"},
                {"en": "You have completed this entire curriculum of noble manners and virtues.", "cn": "你已经以极其优异的表现，全面攻克完成了这套培养崇高礼仪与美德的全部课程！"},
                {"en": "Carry these golden virtues with you like a shining banner of light.", "cn": "愿你将这些金子般熠熠生辉的崇高美德时刻随身携带，宛如一面上扬的明澈旗帜。"},
                {"en": "You are destined to illuminate the world with your radiant loving kindness.", "cn": "你注定要用你那一身温暖如阳的仁厚与善良，把整个广阔的大千世界彻底照亮！"},
                {"en": "Step proudly forward into a magnificent tomorrow filled with boundless promise.", "cn": "昂首阔步，无比自豪自信地迈入那个充满无限希望与锦绣前程的宏大明天！"}
            ]
        }
    ]
}

print("COURSE_KIDS_COLORS, MANNERS ready")
