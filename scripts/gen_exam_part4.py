# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))

from builder_core import build_course

def get_exam_part4_courses():
    courses = []

    # -------------------------------------------------------------------------
    # 7. 中考英语高频考点与满分作文黄金句型 (10章) - 严格每章15句，共150句
    # -------------------------------------------------------------------------
    zk_meta = {
        "id": "course-ex-zhongkao",
        "title": "《中考英语高频考点与满分作文黄金句型》(Zhongkao English) · 核心提分宝典 (10章全集)",
        "category": "exam",
        "categoryName": "考试备考",
        "coverGradient": "from-emerald-600 via-teal-700 to-cyan-800",
        "icon": "🏆",
        "description": "紧扣全国中考英语新课标热点主题，全方位打磨宾语从句、状语从句、动名词与满分书信议论文表达。",
        "difficulty": "初级入门 A2",
        "tags": ["中考英语", "新课标", "满分作文", "中考核心", "语法提分"]
    }
    zk_chapters = [
        {
            "title": "Unit 1 · 个人成长与自我优势探索 · 做最自信阳光的自己",
            "description": "探讨发掘自身潜能、克服自卑胆怯、勇于登台表达与树立青春自信。",
            "sentences": [
                {"en": "Every teenager possesses unique talents waiting to be discovered through patient practice and persistent exploration.", "cn": "每一个青葱少年身上都潜藏着独一无二的天赋与潜能，正静静等待着通过坚持不懈的练习与探索破土绽放。"},
                {"en": "Overcoming shyness requires stepping outside comfortable routines and speaking up boldly before classmates during morning presentations.", "cn": "战胜内心的羞涩胆怯，需要我们勇敢迈出舒适圈，在清晨课前演讲时落落大方地在全班同窗面前大胆发表见解。"},
                {"en": "Setting specific, achievable weekly study targets prevents feeling overwhelmed by the approaching high school entrance exam.", "cn": "为自己量身设立具体清晰、触手可及的每周复习小目标，能够有效避免在中考大关步步逼近时手足无措、倍感焦虑。"},
                {"en": "My English teacher constantly reminds us that making mistakes in homework is the secret stepping stone to perfection.", "cn": "我的英语老师时常和蔼地叮嘱我们：在平时作业练习中犯错，恰恰是通往日后考场炉火纯青的隐秘宝贵跳板。"},
                {"en": "Keeping a reflective personal diary helps adolescents sort out confusing emotions and celebrate small daily breakthroughs.", "cn": "坚持每天在日记本里工整记录下自己的心路历程，能够帮助初中生厘清纷乱思绪，并深情庆祝每一个微小的自我突破。"},
                {"en": "Learning to play the acoustic guitar taught me that patience and steady finger repetition conquer difficult chords.", "cn": "学习弹奏木吉他的宝贵经历深深启发了我：唯有持之以恒的耐性与反反复复的手指练习，方能彻底降伏复杂的和弦。"},
                {"en": "Do not measure your worth by comparing yourself with others; focus on becoming better than you were yesterday.", "cn": "千万不要盲目在同他人的横向攀比中丈量自身的身价；专心致志让自己今天比昨天更有长进，才是最大的智慧！"},
                {"en": "Developing intrinsic self-motivation allows dedicated students to complete assignments conscientiously without parental reminders.", "cn": "在内心深处呵护培育自驱自律的学习发动机，能够让勤奋的学子无需父母长辈督促催促，便能一丝不苟完成课业。"},
                {"en": "A cheerful, friendly smile is the golden passport that opens doors to new friendships across the campus.", "cn": "一抹真诚洋溢、如沐春风的灿烂微笑，永远是敲开校园新同窗心扉、结识知心好友的最佳黄金通行证。"},
                {"en": "Reading inspirational biographies of great scientists during study breaks renews our determination to conquer academic hurdles.", "cn": "在紧张课业间隙翻阅先贤科学家自强不息的励志传记，能够为我们重新注入战胜学业重峦叠嶂的澎湃钢铁斗志。"},
                {"en": "Expressing sincere gratitude to classmates who assist us builds a warm, harmonious classroom atmosphere.", "cn": "向每一次伸出援手答疑解惑的热心同桌致以发自肺腑的由衷道谢，能够共同营造出团结互助的温馨班集体氛围。"},
                {"en": "Organizing revision notes with colorful highlighters and mind maps makes complex historical timelines crystal clear.", "cn": "巧妙运用彩色荧光笔与思维导图提炼复习笔记，能够让错综复杂的历史事件脉络在眼前变得井井有条、一目了然。"},
                {"en": "Believe firmly in your hidden potential; the darkest night will inevitably give way to the brilliant golden morning.", "cn": "请坚信你自己血脉深处那股未曾觉醒的巨大潜能吧；哪怕最漆黑寒冷的长夜，也终将无可阻挡地迎来万丈灿烂朝阳！"},
                {"en": "Youth is not a time of life, but a state of mind characterized by daring courage and endless hope.", "cn": "青春从来不仅仅是一段短暂的韶华岁月，而是一种以大无畏的探索勇气与对未来满怀憧憬为底色的壮美精神状态！"},
                {"en": "Stride proudly toward your high school dreams; you are capable of achieving far more than you ever imagined.", "cn": "昂首阔步迈向你梦寐以求的重点高中大门吧；你所能爆发出的惊人力量，远远超越你过去对自身的一切想象！"}
            ]
        },
        {
            "title": "Unit 2 · 家庭亲情与感恩父母奉献 · 报答三春晖的温暖",
            "description": "探讨理解父母唠叨背后的深沉大爱、分担家务、共度温馨周末与感恩孝道。",
            "sentences": [
                {"en": "Parents' seemingly endless nagging is often the awkward, affectionate armor disguising their deep concern for our future.", "cn": "父母平日里那些看似没完没了的碎碎念唠叨，实则往往是他们用来包裹掩盖对我们前途命运无微不至牵挂的拙朴深情盔甲。"},
                {"en": "Cooking a simple tomato and egg noodle soup for my mother after work brought proud tears to her eyes.", "cn": "在母亲下班拖着疲惫身躯进门时为她端上一碗热气腾腾的西红柿鸡蛋打卤面，让操劳一生的妈妈眼眶里泛起了欣慰的泪花。"},
                {"en": "Father's weathered calloused hands carried heavy construction loads so that I could sit in bright, modern classrooms comfortably.", "cn": "正是父亲那一双在工地风霜中磨出厚茧的粗粝双手扛起了一袋袋水泥重担，才稳稳托举换来了今天我在明亮宽敞教室里的安心苦读。"},
                {"en": "Spending Sunday afternoons walking through neighborhood parks with grandparents strengthens precious intergenerational bonds.", "cn": "利用周日下午陪着白发苍苍的爷爷奶奶漫步街心公园绿荫步道，让两代人之间血浓于水的亲情纽带愈发深厚而温暖。"},
                {"en": "Learning to listen patiently to parents' childhood stories bridges emotional communication barriers between two generations.", "cn": "学会心平气和地俯下身子倾听父母讲述他们童年时代的艰苦岁月往事，能够轻而易举跨越代际沟通中曾存在的无形隔阂。"},
                {"en": "Household chores such as washing dinner dishes and sweeping floors should be shared equitably by teenage family members.", "cn": "饭后主动挽起袖子洗净碗筷、拿起扫帚打扫地板家务，本就是每一个正在茁壮成长的初中少年不可推卸的家庭责任。"},
                {"en": "A handwritten Mother's Day greeting card holds far more emotional warmth than expensive commercial store purchases.", "cn": "一张在灯下用彩笔亲笔工工整整写满由衷感恩话语的母亲节贺卡，其承载的温情分量远胜任何昂贵的商业流水线礼物。"},
                {"en": "Family dinner conversations where everyone puts down mobile phones foster intimate mutual understanding and genuine laughter.", "cn": "在晚餐全家围坐的温馨时刻大家自觉放下手机屏幕促膝畅谈，能够催生出心照不宣的亲情默契与此起彼伏的开怀欢笑。"},
                {"en": "We should remember to hug our parents tightly and say 'I love you' before heading out to school each morning.", "cn": "在每天清晨背上书包迈出家门求学之前，别忘了给身旁的爸爸妈妈一个大大的拥抱，深情说上一声“我爱你们”。"},
                {"en": "Forgiving occasional parental strictness allows teenagers to appreciate the protective boundaries established for their safety.", "cn": "学会体谅理解父母偶有的严苛管教，能让我们明白：那些看似不近人情的严格家规，实则是为我们遮风挡雨的爱之结界。"},
                {"en": "Watching old family photograph albums on rainy evenings brings back forgotten golden memories of carefree babyhood.", "cn": "在细雨绵绵的夜晚同家人围坐翻开沉甸甸的老相册，一张张泛黄彩色照片重新唤醒了童年被全家捧在手心里的甜蜜回忆。"},
                {"en": "True filial piety consists of treating aging parents with gentle patience and unwavering respect throughout all seasons.", "cn": "真正意义上的大孝之道，从来在于一年四季寒来暑往之中，始终用温柔体恤的耐心与毫不打折的敬重去陪伴风烛残年的长辈。"},
                {"en": "A harmonious domestic hearth provides the secure emotional harbor from which confident adolescents venture out into the world.", "cn": "一个充满欢声笑语、和睦温馨的家庭避风港，是滋养赋能自信少年无所畏惧迈向外部浩瀚大千世界的最坚实心理大后方！"},
                {"en": "Cherish the quiet moments spent beside your parents; their unconditional love is the greatest blessing of mortal life.", "cn": "请倍加珍惜依偎在父母身旁的每一个平凡静谧晨昏吧；那份毫无保留的深沉大爱，是红尘尘世赐予我们最神圣的无价至宝！"},
                {"en": "Honor your mother and father through your upright character, diligent study, and compassionate heart forever.", "cn": "用你堂堂正正的昂首品格、脚踏实地的勤奋学业以及悲悯众生的善良心肠，去由衷告慰报答那份浩荡如海的父母深恩吧！"}
            ]
        },
        {
            "title": "Unit 3 · 校园友谊与合作学习 · 同舟共济的同窗深情",
            "description": "探讨互帮互助攻克难题、化解同伴矛盾、共同进步与珍惜三年同窗情谊。",
            "sentences": [
                {"en": "True friendship does not mean never having disagreements, but possessing the maturity to resolve conflicts through honest dialogue.", "cn": "真正纯洁崇高的校园友谊从来绝不意味着两人之间永远毫无争吵分歧；而在于拥有通过坦诚谈心把话说开、化干戈为玉帛的成熟胸襟。"},
                {"en": "Forming peer study pairs allows classmates to test each other on English vocabulary and clarify confusing physics diagrams.", "cn": "在班级里自发结成同桌一帮一互助学习对子，能够让彼此在课后互相抽背英语单词，并一起把黑板上复杂的物理受力分析图彻底吃透。"},
                {"en": "When I fell and scraped my knee during sports day, my faithful friend carried me to the clinic immediately.", "cn": "在学校秋季运动会八百米跑道上我不慎摔破膝盖鲜血直流的危急关头，我最要好的同窗好友二话不说立刻背起我飞奔校医室。"},
                {"en": "Celebrating a classmate's stellar examination triumph without jealousy demonstrates the noble purity of authentic school companionship.", "cn": "看到好同伴在期末红榜上勇夺第一时发自肺腑为对方鼓掌欢呼而不带半点嫉妒酸意，生动展现了同窗深情最纯粹无瑕的高贵风骨。"},
                {"en": "Exchanging colorful handwritten graduation memory books preserves unforgettable moments of laughter shared in middle school corridors.", "cn": "在初三毕业季郑重交换亲笔书写的同学录留念册，将这整整三年间在楼道走廊里并肩留下的欢声笑语与热泪定格为永恒。"},
                {"en": "A dependable companion stands by your side during gloomy rainy days, offering silent umbrellas and listening ears unconditionally.", "cn": "一个靠谱坚定的莫逆同窗会在你遭遇挫折、心情阴霾落雨的至暗时刻默默撑伞陪伴在侧，无条件递上纸巾并耐心做你的倾听者。"},
                {"en": "Group classroom debates on environmental conservation teach teenagers to respect diverse analytical perspectives while refining oral logic.", "cn": "围绕低碳环保议题开展的班级分组辩论赛，不仅极大地磨砺了同学们的英语口语辩驳逻辑，更教会了大家学会兼听则明的包容胸怀。"},
                {"en": "Sharing notes generously with classmates recovering from influenza at home reflects the warmth of our unified class collective.", "cn": "主动将课堂笔记工整复印并送给因患重感冒发烧在家隔离休养的同窗好友，处处彰显着我们这个班级大家庭守望相助的融融暖意。"},
                {"en": "Campus friendships forged through shared sweat on the basketball court outlast the final examination and remain vibrant for decades.", "cn": "在校园水泥篮球场上迎着夕阳挥汗如雨、并肩传球防守所打磨出的兄弟战友情，能够远远跨越中考考场，在未来数十年风雨岁月中历久弥新！"},
                {"en": "Gossiping behind others' backs poisons trust; ethical students defend absent friends against ungrounded rumors boldly.", "cn": "在人背后嚼舌根传闲话会彻底腐蚀同学间的信任防线；一个有品德的正直学子会在同伴不在场时挺身而出，断然击碎反驳不实谣言！"},
                {"en": "Studying together beneath campus willow trees during spring lunch hours makes the burden of revision feel as light as breeze.", "cn": "初春中午在校园垂柳绿荫下同挚友席地而坐共同背诵古诗文名篇，让繁重的中考冲刺复习在微风拂面中显得格外轻松欢快。"},
                {"en": "A word of sincere praise from a respected classmate can kindle self-belief in a discouraged heart instantly.", "cn": "来自身旁要好同伴一句发自肺腑的真诚鼓励与夸赞，往往能在瞬间重新点燃一颗在模拟考失利后心灰意冷年轻心房的自信火种。"},
                {"en": "Three memorable years of middle school camaraderie bind our youthful hearts together with golden threads of shared memory.", "cn": "这难忘充实的整整三年初中求学时光，用共同拼搏欢笑的金丝银线，将我们这群少年的滚烫心房紧紧连缀编织在了一起！"},
                {"en": "A true friend is someone who walks in when the whole rest of the world walks out; cherish such souls with all your heart.", "cn": "真正的至交知己，乃是当全世界都背弃你离场时依然坚定推门朝你大步走来的那个人；请倾尽毕生真情，好好呵护珍惜这样的同伴吧！"},
                {"en": "May your friendships burn as warm beacons throughout life; side by side, there is no summit you cannot conquer together.", "cn": "祈愿你这三年铸就的纯真同窗友谊化作照亮余生的温暖灯塔；只要手挽着手心连着心，世间便绝无你们携手无法登顶的险峰！"}
            ]
        },
        {
            "title": "Unit 4 · 兴趣爱好与课外特长发展 · 拥抱多元充实的课余天地",
            "description": "探讨音乐合唱、书法绘画、科技编程、集邮天文等特长对心灵的滋养。",
            "sentences": [
                {"en": "Cultivating personal hobbies provides teenagers with healthy emotional outlets to unwind after grueling hours of textbook revision.", "cn": "在紧张繁重的专业课本复习之余主动培养几门健康的业余兴趣爱好，能够为初中生构筑起宣泄身心压力、安顿心灵的优质解压阀。"},
                {"en": "Playing the violin in our school orchestra taught me how divergent musical parts harmonize into breathtaking classical symphonies.", "cn": "在学校管弦乐团里担任小提琴手的难忘排练历练，让我深刻领悟到不同声部的乐器究竟是如何在指挥棒下天衣无缝交融成壮美交响乐的。"},
                {"en": "Traditional ink brush painting cultivates quiet meditative patience, training the restless teenage eye to appreciate spatial balance.", "cn": "研墨挥毫修习传统国画水墨艺术，能够深度滋养沉静笃定的冥想心性，训练年轻浮躁的目光学会领略中国画留白虚实之美。"},
                {"en": "Learning basic Python programming logic exercises analytical problem-solving skills through designing simple interactive games.", "cn": "学习基础的Python计算机编程逻辑代码，通过亲手编写设计简单有趣的互动小游戏，极大磨砺了青少年的抽象条理分析思维。"},
                {"en": "Amateur astronomy enthusiasts who set up telescopes on suburban hills behold the craters of the moon with awe.", "cn": "在晴朗夜晚同小伙伴在近郊山顶支起天文望远镜的业余天文爱好者们，屏息凝神亲眼见证月球环形山的凹凸奇境，心生由衷震撼。"},
                {"en": "Collecting postage stamps from around the globe opens miniature colorful windows into foreign geography, botany, and historical monuments.", "cn": "珍藏整理一枚枚来自世界五洲四海的微型小邮票，宛如推开了一扇扇五彩斑斓的神奇小视窗，尽情饱览异国地理风光与名胜古迹。"},
                {"en": "Participating in our campus drama society builds expressive spoken English confidence through acting out Shakespearean dialogues.", "cn": "积极踊跃登上校园英语戏剧社舞台排演莎翁经典名剧独白，在身临其境的角色扮演中全方位夯实了英语口语表达的从容底气。"},
                {"en": "Crafting intricate clay pottery on a spinning wheel connects urban youth with the tactile joy of physical material manipulation.", "cn": "在飞速旋转的陶艺转盘上用掌心细细感知泥土的温润与延展，让现代都市少年重新找回了双手创造器物的本真触觉喜悦。"},
                {"en": "Hobbies should not be pursued merely for competitive trophy hunting, but for the pure, unadulterated joy of creative exploration.", "cn": "培养课外特长爱好从来绝不应当沦为功利考级刷奖状的工具，而理应全凭内心最纯粹、毫无杂质的对未知创造的狂喜与热爱！"},
                {"en": "Balancing academic studies with passionate extracurricular pursuits molds versatile, flourishing adolescents with rich interior lives.", "cn": "把文化课专业学业与充满热情的课外特长爱好平衡得张弛有度，能够为国家培育出全面发展、精神世界丰盈饱满的新时代栋梁少年！"},
                {"en": "Reading historical adventure novels before bedtime expands historical imagination far beyond dry examination curriculum outlines.", "cn": "在睡前沉浸于波澜壮阔的历史探险文学名著之中，能够让青少年的历史跨度想象力远远突破干瘪考纲试卷的逼仄藩篱。"},
                {"en": "Learning photography forces one to search for extraordinary angles of natural beauty hidden within ordinary schoolyard corners.", "cn": "拿起单反相机学习摄影艺术，逼迫我们学会用善于发现美的眼睛，去定格捕捉校园操场转角处那些平日被忽略的绝美光影细节。"},
                {"en": "Cooking exotic dishes over the weekend rewards the palate while teaching practical lessons in kitchen chemistry and timing.", "cn": "利用周末时光对照菜谱亲手为家人烹调一两道拿手特色大菜，不仅犒劳了大快朵颐的味蕾，更在烟火气中上了一堂生动的厨房化学实战课。"},
                {"en": "A life enriched by diverse hobbies is an unassailable castle against boredom, depression, and shallow digital distractions.", "cn": "一个被丰富多彩的雅趣爱好所深情丰盈充实的生命，是一座坚不可摧的心灵城堡，足以百毒不侵抵御世俗一切无聊空虚与数字算法的诱惑！"},
                {"en": "Find that which makes your heart sing with joy; pursue it with dedication, and your world will be painted in radiant colors forever.", "cn": "去全力找寻那件能让你的灵魂与心脏发出由衷喜悦歌唱的真爱特长吧；带着执着去深耕它，你的整个生命宇宙自此必将永远斑斓璀璨！"}
            ]
        },
        {
            "title": "Unit 5 · 体育锻炼与健康生活作息 · 强健体魄为强国奠基",
            "description": "探讨阳光长跑、足球篮球团队精神、告别熬夜与践行规律健康作息。",
            "sentences": [
                {"en": "Daily participation in vibrant outdoor physical exercise builds cardiovascular endurance while relieving accumulated exam anxieties effectively.", "cn": "坚持每天走向阳光明媚的户外田径场投入大汗淋漓的体育锻炼，不仅能强健心肺耐力，更能立竿见影化解排解备考中累积的心头焦虑。"},
                {"en": "The midday sun shining down upon the soccer pitch witnesses our passionate team passing drills and thunderous celebratory cheers.", "cn": "正午温暖和煦的阳光洒在绿茵足球场上，深情见证着我们整支班级球队默契精妙的传切配合与破门得分时震天动地的欢呼狂喜！"},
                {"en": "Prioritizing eight hours of restful nocturnal sleep enhances memory consolidation far more than frantic midnight cramming sessions.", "cn": "雷打不动确保每晚八小时规律充裕的安详睡眠，在巩固日间记忆神经突触方面所带来的益处，远远胜过熬夜到凌晨两点的疲劳战术。"},
                {"en": "Playing competitive basketball matches instills the values of unselfish teamwork, swift tactical adaptation, and sportsmanship under pressure.", "cn": "在火药味十足的班级篮球对抗赛中摸爬滚打，能够深刻淬炼出大局为重的无私团队协作、毫秒级的战术应变以及逆境下的崇高体育风尚。"},
                {"en": "Skipping nutritious breakfasts causes mid-morning blood sugar crashes, severely impairing cognitive focus during difficult mathematics lectures.", "cn": "因赶时间而习惯性不吃营养早餐的恶习，会导致课间血糖急剧断崖式下跌，严重摧毁并涣散在复杂数学逻辑课上应有的专注力。"},
                {"en": "Skipping rope for fifteen minutes daily improves motor coordination while serving as an accessible, cost-effective cardio workout.", "cn": "每天抽出短短十五分钟在阳台或走廊坚持摇绳跳绳，不仅极大跃升了手脚运动协调性，更是一项随时随地开展的高效燃脂有氧王牌。"},
                {"en": "Physical education classes are not marginal distractions, but foundational pillars that cultivate physical grit alongside mental resilience.", "cn": "在基础教育大纲中体育课绝非可有可无的边缘副科，而是为国家栋梁锻造钢铁体魄同锤炼抗挫折心理防线并驾齐驱的至高基石！"},
                {"en": "Trading sedentary video gaming hours for vigorous badminton matches with parents revitalizes physical joints and brightens vision.", "cn": "果断放弃周末窝在沙发上刷手机打网游的颓废久坐恶习，陪同父母痛痛快快打上一场大汗淋漓的羽毛球赛，让身心骨骼重焕无限活力。"},
                {"en": "Drinking ample warm water throughout demanding school days aids biological metabolic clearance and prevents fatigue headaches.", "cn": "在紧凑充实的在校求学期间养成随时主动多次饮用温开水的健康习惯，能够加速机体代谢废物排毒，彻底告别脱水性疲劳偏头痛。"},
                {"en": "Sports teach teenagers how to win with humble dignity and, more crucially, how to accept defeat with graceful determination.", "cn": "竞技体育大舞台教会青少年最宝贵的功课，莫过于在斩获冠军时学会谦逊低调不骄不躁；而在遭遇落败失利时，更能昂首坦然微笑再战！"},
                {"en": "Brisk jogging around the campus track under evening dusk clears mental cobwebs and recharges enthusiasm for evening self-study.", "cn": "在暮色四合夕阳斜照的校园跑道上呼吸着清凉晚风痛快慢跑几圈，瞬间涤荡了白昼所有的精神疲惫，为晚自习攻坚加满活力电池。"},
                {"en": "Ergonomic classroom posture with straight spines prevents chronic myopia progression and spinal curvature issues among adolescents.", "cn": "在课桌前时刻保持脊梁骨挺拔笔直的端正坐姿，能够有效遏制初中生近视度数的加深蔓延，誓死捍卫青少年的脊椎健康与昂首英姿。"},
                {"en": "A sound mind can reside only within a sound physical body; physical fitness is the vehicle carrying all your academic dreams.", "cn": "大千世界中最清醒敏锐的智慧心智，从来唯独安详栖息在百炼成钢的健康体魄深处；强健的体魄，乃是承载你一切宏伟锦绣梦想的坚固战车！"},
                {"en": "Physical exercise is not a wasteful expense of energy, but the highest investment in vitality, resilience, and lifelong happiness.", "cn": "坚持挥汗如雨的体育锻炼从来不是在无端挥霍浪费精力，而是一个人对自己一生生命活力、心理抗逆力与终身幸福的最划算投资！"},
                {"en": "Run with passion, sweat with pride, and build a body forged of iron; for upon your strong shoulders rests the tomorrow of our nation!", "cn": "迎着朝阳尽情奔跑吧，为了荣耀肆意挥洒汗水，锻造出一副无坚不摧的钢铁体魄——因为在我们青年一代强健的脊梁之上，正托举着伟大的祖国！"}
            ]
        },
        {
            "title": "Unit 6 · 资源节约与垃圾分类绿色校园 · 践行低碳微生活",
            "description": "探讨随手关灯关水、光盘行动拒绝舌尖浪费、垃圾精准分类与绿色环保校园。",
            "sentences": [
                {"en": "Sorting waste diligently into recyclable, food, hazardous, and other bins represents our daily civic duty toward environmental conservation.", "cn": "在垃圾投放点前一丝不苟将废弃物精准分类投入可回收物、厨余垃圾、有害垃圾与其他垃圾四色垃圾桶，是我们对生态家园最质朴的日常公民担当。"},
                {"en": "The nationwide 'Clean Your Plate' campaign encourages school dining halls to eliminate food waste by ordering moderate meal portions.", "cn": "在全国各大中小学校园餐厅如火如荼开展的“光盘行动”，大力倡导按需点餐、厉行节约的文明美德，坚决向一切舌尖上的粮食浪费大声说不！"},
                {"en": "Turning off taps tightly while brushing teeth prevents gallons of precious purified municipal drinking water from pouring into sewers.", "cn": "在晨起洗漱刷牙涂抹牙膏的片刻随手把水龙头拧紧关死，举手之劳便能阻止成加仑洁净珍贵的人工自来水白白哗哗流失进下水道！"},
                {"en": "Using both sides of blank scrap paper for mathematical rough calculation spares ancient forests from being clear-cut for paper mills.", "cn": "在演算错综复杂的数理推导草稿题时坚持把每一张白纸正反双面统统写满用尽，在细微举手投足间，便为大自然的大片原始原始森林挡住了砍伐伐木斧！"},
                {"en": "Carrying durable, reusable fabric shopping bags to neighborhood supermarkets drastically reduces single-use plastic pollution across town.", "cn": "每次同父母前往街坊大超市采购日用品时坚持随身携带结实耐用的环保布袋，能够从源头大刀阔斧斩断泛滥成灾的一次性塑料袋白色污染。"},
                {"en": "Turning off classroom air conditioning units and overhead lights before leaving ensures campus energy conservation targets are met.", "cn": "在放学离开班级教室锁门前的最后一秒自觉伸手按下开关关掉日光灯与立式空调，以实际行动确保绿色校园节能减排责任指标的刚性落地。"},
                {"en": "Renting shared public bicycles for short commuting journeys slashes urban automobile carbon emissions while providing gentle exercise.", "cn": "在城市一到三公里以内的短途通勤中积极扫码骑行绿色公共共享单车，不仅立竿见影砍削了机动车尾气排放，更在微风拂面中锻炼了身体。"},
                {"en": "Donating outgrown winter coats and unused storybooks to underprivileged mountain schools gives old possessions meaningful second lives.", "cn": "将自己穿不下的厚实保暖冬季旧羽绒服与翻阅过的少儿名著故事书打包洗净捐赠给偏远山区希望小学，让旧物品绽放出充满大爱的崭新二次生命。"},
                {"en": "Rechargeable batteries and used fluorescent tubes must be discarded exclusively into designated red hazardous collection barrels.", "cn": "废弃的充电锂电池、含汞纽扣电池与废旧日光灯荧光灯管，必须依法依规百分之百精准投放进专用的红色有害垃圾分类回收收集箱中！"},
                {"en": "Setting domestic air conditioning thermostats to twenty-six degrees Celsius during summer strikes an optimal balance between comfort and low-carbon living.", "cn": "在炎炎盛夏将室内居家与教室空调制冷温度统一恒定设置在最为科学舒适的二十六摄氏度，在舒爽宜人的同时兼顾了低碳节能环保大局。"},
                {"en": "Planting flowering shrubs and evergreen saplings around school borders transforms barren asphalt corners into humming pollinator sanctuaries.", "cn": "在每年植树节同师生一起在校园围墙边沿亲手栽下一株株四季常青的树苗与花灌木，让原本光秃秃的沥青操场转角蜕变为了蜂蝶起舞的生态小乐园。"},
                {"en": "Saying no to disposable wooden chopsticks when ordering takeout meals protects tens of thousands of hectares of birch trees annually.", "cn": "在点外卖用餐时主动勾选“无需一次性木筷餐具”选项，全社会千百万人聚沙成塔的坚持，每年足以挽救数以万公顷计的茂密桦木森林免遭砍伐！"},
                {"en": "Environmental conservation is not a grand, unattainable slogan; it blossoms through the quiet accumulation of our humble daily habits.", "cn": "生态环保从来绝不是一句写在红幅标语上高高在上、脱离实际的空洞口号；它在千家万户千万人每一个微小朴素生活细节的自律坚守中盛大绽放！"},
                {"en": "Treat every drop of water, every kilowatt of electricity, and every grain of rice as sacred gifts borrowed from future generations.", "cn": "请把眼前每一滴自来水、每一度电能以及碗里的每一粒白米饭，统统视作我们当代人从子孙后代那里暂时借来的珍贵神圣恩赐，倍加由衷爱惜吧！"},
                {"en": "Let our green footprints cover the earth; cherish nature with devotion, and our mother planet will embrace us with abundant life forever.", "cn": "且让我们把无愧于天地的绿色低碳足迹深深烙印在祖国大地上吧；用至诚之心去深情呵护自然，地球母亲必将用万物丰茂的壮美怀抱永远深情拥抱我们！"}
            ]
        },
        {
            "title": "Unit 7 · 遵守校规校纪与安全防范常识 · 平安校园护航青春成长",
            "description": "探讨遵守交通红绿灯、防溺水防诈骗、防火防震演练与营造清朗校园环境。",
            "sentences": [
                {"en": "Strict adherence to campus safety regulations and municipal traffic codes forms the non-negotiable prerequisite for personal well-being.", "cn": "严格恪守校纪校规各项安全行为准则与文明市政道路交通红绿灯法规，是保障我们每一个青少年生命健康茁壮成长的绝对前提与护身金钟罩。"},
                {"en": "Never swim alone in unsupervised rural reservoirs, abandoned quarry lakes, or turbulent rivers during sultry summer vacations.", "cn": "在酷暑难耐的长夏暑假期间，千千万万切记：绝对严禁在无大人看护监护、无专业救生员值守的偏远野外水库、废弃采石水坑或湍急野河中私自下水游泳！"},
                {"en": "Practicing fire evacuation drills with wet towels covering noses and mouths prepares students to escape smoke-filled corridors safely.", "cn": "在全校消防应急疏散演练中一丝不苟手拿湿毛巾捂紧口鼻、弯腰低姿小跑撤离，能让我们在未来面对真实火灾浓烟滚滚的险境时从容逃生。"},
                {"en": "Always dismount from bicycles and observe left and right road conditions vigilantly when crossing busy pedestrian zebra lines.", "cn": "在骑行单车途经人潮车流汹涌的大十字路口斑马线时，必须自觉提前下车推行，并左右转头仔细观察左右两侧来车动向确认安全。"},
                {"en": "Campus anti-bullying zero-tolerance policies ensure that every adolescent enjoys learning in a secure, supportive, and respectful sanctuary.", "cn": "校园内部坚决对任何形式的言语侮辱、肢体暴力校园欺凌行径推行铁腕“零容忍”重拳问责制度，誓死确保每一位学子皆能在一片安全温馨尊严的圣所里读书求索。"},
                {"en": "Never reveal private home addresses, parent identification numbers, or bank account SMS verification codes to unfamiliar callers online.", "cn": "在互联网聊天交友与接听陌生来电时时刻筑牢防诈骗心墙：绝对严禁向任何陌生人透露家庭真实住址、父母身份证号以及银行短信动态验证码！"},
                {"en": "Electrical sockets inside science laboratories must never be touched with wet hands to avoid catastrophic electric shock injuries.", "cn": "在理化生实验室开展实验攻关操作期间，绝对严禁用沾满水渍的湿手去直接触碰任何高压仪器插头电源插座，坚决杜绝致命触电恶性事故发生。"},
                {"en": "Wearing certified safety helmets correctly when riding electric scooters cushions the head effectively during unexpected traffic collisions.", "cn": "在搭乘或骑行电动车时必须规规矩矩佩戴好符合国家安全质检标准的头盔并牢牢系紧下颌搭扣，能在突发交通碰撞倒地时为脆弱头部构筑起坚实救命安全气囊。"},
                {"en": "During sudden earthquake shocks, immediately crouch beneath sturdy desks and protect heads firmly until initial tremors subside.", "cn": "在遭遇突发地震地动山摇的惊魂生死瞬间，必须以秒速迅速就地双手抱头蜷缩躲避在坚固桌椅三角支撑区域下方，直到第一波剧烈主震完全过去！"},
                {"en": "Reporting suspicious strangers wandering along dark campus perimeter fences to security guards prevents potential criminal trespassing.", "cn": "在晚自习放学途经校园昏暗偏僻围墙死角若发现行迹可疑鬼祟闲杂人员，理应第一时间机警报告给门岗值班安保特警叔叔，将安全隐患扼杀在萌芽期。"},
                {"en": "Food safety requires checking expiration dates printed on snack packaging scrupulously, avoiding unhygienic roadside street vendor carts.", "cn": "严把病从口入的食品安全关，要求我们在小卖部选购零食时必须睁大双眼仔细查验包装袋上的生产日期与保质期，坚决对校门口三无流动露天脏摊说不！"},
                {"en": "Obeying laboratory safety protocols including wearing safety goggles prevents accidental acid chemical splashes from blinding vision.", "cn": "做化学实验时严格遵照实验室操作规程规规矩矩佩戴好防化学飞溅护目镜，能够誓死捍卫双眼免遭意外浓酸强碱飞溅所造成的终身双目失明惨剧。"},
                {"en": "Safety is the golden anchor holding the ship of life steady; neglect it for a single second, and regrets echo through a lifetime.", "cn": "安全意识是稳稳锚定住生命远航巨轮免遭触礁沉没的万钧黄金铁锚；哪怕因为麻痹大意仅仅松懈了短短一秒钟，换来的便可能是抱憾终生的无尽血泪！"},
                {"en": "Rules and boundaries are engineered not to shackle your freedom, but to build an unshakeable protective fortress around your youth.", "cn": "学校规章制度与安全红线从来绝非是为了捆绑束缚你飞翔的自由翅膀，而是为了在你风华正茂的灿烂青春四周，筑起一座阻挡风雨侵害的钢铁铜墙铁壁！"},
                {"en": "Cherish your precious life and watch over your peers; may every youth return home safely beneath the peaceful evening twilight.", "cn": "请深情敬畏生命并时刻同身旁同窗守望相助吧；祈愿天底下每一位少年，在每一个黄昏日落霞光漫天的美好时刻，皆能平安健康归家阖家团圆！"}
            ]
        },
        {
            "title": "Unit 8 · 志愿服务与关爱社会弱势群体 · 赠人玫瑰手有余香",
            "description": "探讨敬老院义务劳动、关爱特殊儿童、城市环保志愿行与奉献精神。",
            "sentences": [
                {"en": "Volunteering is not an ostentatious display of pity, but an egalitarian act of human communion that elevates both giver and receiver.", "cn": "投身公益志愿服务从来绝不是高高在上施舍怜悯的虚荣表演，而是一场平等待人、心手相牵的崇高生命对话，在同时间升华涤荡了付出者与受助者双方的心灵。"},
                {"en": "Visiting rural nursing homes on weekends to peel fresh oranges and chat with lonely elderly widows brings smiles to wrinkled cheeks.", "cn": "利用周末时光结伴走进偏远乡镇敬老院为孤寡老人亲手剥一个甘甜多汁的新鲜蜜橘、搬把小凳促膝拉拉家常，让饱经风霜的苍老面庞重新洋溢起开怀笑容。"},
                {"en": "Reading fairy tales patiently to children with hearing impairments in special education academies sparks vibrant imaginative wonder.", "cn": "在特殊教育辅读学校活动室里用极大的耐心配合手语为听障残障孩童逐字逐句朗读经典童话，在孩子清澈纯净的目光深处点亮了一盏斑斓的想象力明灯。"},
                {"en": "Youth volunteers assisting traffic police at pedestrian crossings during morning rush hours guide elderly pedestrians across safely.", "cn": "头戴小红帽的青年志愿者们在早高峰十字路口主动配合交警叔叔挥旗执勤，小心翼翼搀扶着腿脚不便的白发阿婆安全平稳穿过繁忙斑马线。"},
                {"en": "Organizing weekend charity bazaars on campus raises funds to purchase warm woolen gloves and stationary sets for children in mountainous villages.", "cn": "在校园林荫道精心组织义卖跳蚤市场大集，将义卖所筹集的每一分爱心善款如数换成一双双保暖羊毛手套与全套水彩画笔，如期寄往大山深处的希望小学。"},
                {"en": "Cleaning up plastic bottles and cigarette butts scattered across public mountain trails restores the pristine wilderness to its natural splendor.", "cn": "利用节假日自备垃圾夹与环保垃圾袋沿山间徒步古道沿途弯腰捡拾丢弃的塑料矿泉水瓶与烟头，用弯腰的质朴善举让绿水青山重现纤尘不染的原生态秀美。"},
                {"en": "Teaching silver-haired senior citizens how to navigate smartphone medical appointment apps helps them bridge frustrating digital technology divides.", "cn": "在社区活动中心手把手、不厌其烦地耐心教导银发白发老爷爷老奶奶如何操作手机微信预约挂号就医与扫码乘车，帮老人们跨越数字鸿沟。"},
                {"en": "Serving warm soup bowls at community soup kitchens on freezing winter evenings warms the shivering bodies of homeless laborers.", "cn": "在天寒地冻的数九寒冬夜晚主动走进爱心社区爱心粥铺为饥肠辘辘的环卫工与流浪者端上一碗滚烫的牛肉热粥，驱散了一整天的刺骨寒意。"},
                {"en": "Writing braille letters to blind peers establishes heartfelt pen-pal friendships that transcend physical visual sensory limitations.", "cn": "亲手摸索盲文打字机为盲童学校的盲人伙伴工工整整打印寄去一封封充满鼓励的盲文信件，构筑起了一座座超越视觉感官藩篱的纯真同窗笔友之桥。"},
                {"en": "Volunteering cultivates mature civic empathy, shifting youthful perspectives away from narcissistic selfishness toward collective social welfare.", "cn": "投身志愿服务的洗礼过程，能够深度淬炼出成熟的现代公民同理共情大爱，果断将青少年的目光从自私狭隘的一己私利中拔升出来，投向更加辽阔的人间冷暖大局。"},
                {"en": "Donating pocket money saved from skipping sugary soft drinks helps replenish animal shelter dog food pantries across the district.", "cn": "把平时嘴馋省下来的零花钱悉数积攒起来定向捐给民间流浪动物救助基地用于采购爱心狗粮，在举手投足间拯救了一只只无家可归的毛孩子。"},
                {"en": "Recording audio versions of middle school literature textbooks creates a rich listening library for visually challenged students across the province.", "cn": "利用周末走进专业录音室字正腔圆深情朗读录制初中语文名家散文名作有声读物，为全省数以千计的视障视弱学子搭建起了一座声音的文学圣殿。"},
                {"en": "Roses given to others leave a lingering fragrance in your hands; true wealth is measured by the love you distribute across the world.", "cn": "“赠人玫瑰，手有余香”——一个人行走在人世间真正的富足与高贵，从来绝不取决于你在名下囤积了多少财宝，而唯独丈量于你向这个人间慷慨播撒了多少真爱！"},
                {"en": "A single spark of voluntary kindness can kindle a blazing bonfire of hope that banishes the winter chill from a despairing soul.", "cn": "一抹微不足道、出于纯善志愿之心的微小善举火花，往往能在无形之中点燃一簇熊熊燃烧的希望篝火，彻底驱散一个在绝境长夜中受苦受难灵魂心头的刺骨寒冬！"},
                {"en": "Step forward with open arms and an eager heart; in serving others, you will uncover the grandest, most luminous version of your own soul.", "cn": "张开你热情的双臂、怀揣一颗赤诚之心走向需要帮助的街坊同胞吧——因为在弯腰奉献服务他人的伟大实践深处，你终将邂逅那个最顶天立地、最璀璨夺目的全新自己！"}
            ]
        },
        {
            "title": "Unit 9 · 传统节日文化体验与庆祝 · 传承中华千古民俗",
            "description": "探讨除夕包饺子、端午赛龙舟吃粽子、中秋赏月吃月饼与重阳登高的文化意蕴。",
            "sentences": [
                {"en": "Wrapping savory pork and cabbage dumplings with family members on Chinese New Year's Eve symbolizes wealth, reunion, and auspicious beginnings.", "cn": "在辞旧迎新的除夕年夜饭前夕围坐案板四周同全家人一起包猪肉白菜水饺，不仅寓意着招财进宝更深情象征着阖家团圆与万象更新吉祥如意。"},
                {"en": "Dragon boat regattas during the Dragon Boat Festival witness paddlers thrusting oars in unison to beating drums, commemorating Qu Yuan's patriotic sacrifice.", "cn": "端午佳节江面之上百舸争流的龙舟竞渡盛会，伴随着震耳欲聋的咚咚战鼓，划手们同频共振整齐劈波斩浪，庄严告慰缅怀爱国诗人屈原的殉国忠魂！"},
                {"en": "Admiring the radiant full moon while savoring lotus-seed mooncakes on Mid-Autumn Festival brings back sweet memories of faraway hometown kin.", "cn": "中秋佳节之夜仰头赏鉴夜空中宛如碧玉盘般的皎洁满月、细品清甜可口的白莲蓉双黄月饼，让游子心田深处泛起对远方故乡至亲的无尽思念与温馨祝福。"},
                {"en": "Tying colorful five-strand silk threads around children's wrists during dragon boat festivities serves as a traditional talisman warding off evil pestilence.", "cn": "端午民俗中在孩童稚嫩的手腕脚踝处郑重系上五彩斑斓的五彩绳丝线，承载着数千年来祖先祈愿孩子百毒不侵、远离疫疠灾害的深情护身符祈愿。"},
                {"en": "Ascending high hills and pinning cornelian sprigs on clothes during Double Ninth Festival honors ancestral wisdom while celebrating elder longevity.", "cn": "九九重阳佳节携手登高远眺插茱萸、饮菊花美酒，在寄情祖国大好秋景的同时，深情表达了对天地先祖的由衷敬畏与对天下长辈松柏延年的美好祝愿。"},
                {"en": "Guessing ingenious riddles pinned beneath crimson paper lanterns during the Lantern Festival exercises youthful wit amid vibrant neighborhood carnivals.", "cn": "元宵佳节千家万户张灯结彩的红灯笼长廊下挤满了争相猜灯谜的少男少女，在热闹非凡的街坊狂欢中极大磨砺了中华汉字语言文化的机敏智慧。"},
                {"en": "Pasting brilliant scarlet spring couplets and upside-down 'Fu' characters onto wooden doorways invites good fortune to bless the household across coming seasons.", "cn": "大年三十清晨亲手将字迹苍劲的大红春联与倒贴的烫金“福”字端端正正张贴在门楣两侧，满怀憧憬祈愿新的一年福星高照、五谷丰登、家宅平安。"},
                {"en": "Traditional festival cuisines do not merely satisfy biological appetites, but serve as tangible carriers of cultural identity across generations.", "cn": "中华传统节庆名点佳肴从来绝非仅仅是为了填饱咕咕叫的口腹食欲，而是作为有温度的舌尖物质文化载体，代代相传维系着全球华夏儿女共同的文化身份认同！"},
                {"en": "Lighting floating water lanterns along ancient town canals on the Ghost Festival sends prayers of peace to ancestors resting in eternal tranquility.", "cn": "中元节夜晚在古镇幽深河道石桥之下点燃一盏盏荷花水灯任其顺水漂流向远方，将后人对沉睡在安详彼岸先辈祖先的深切追思化作漫漫水面的点点微光。"},
                {"en": "Eating sticky sweet laba porridge cooked with eight auspicious grains marks the festive prelude heralding the rapid countdown to Spring Festival.", "cn": "在寒冬腊八节清晨喝上一碗用大米、红豆、莲子等八种五谷杂粮慢火熬煮黏稠的香甜腊八粥，欢快吹响了迎接农历新春大年的迎新号角！"},
                {"en": "Making handmade osmanthus-flower cakes during autumn holidays teaches students the agricultural patience required to harvest natural seasonal gifts.", "cn": "在金秋长假里在庭院桂花树下收集落花亲手烘焙桂花糕点，让青少年在甜蜜香气中体悟大自然应季而作应时而食的农耕生态智慧。"},
                {"en": "Traditional holidays provide precious cultural anchors that prevent modern people from drifting aimlessly in the fast-paced currents of globalization.", "cn": "源远流长的中华传统岁时节庆宛如沉入岁月大河之中的万钧文化铁锚，防止现代都市人在日新月异、快节奏全球化大工业洪流中彻底迷失自我精神原乡！"},
                {"en": "Every traditional festival is a living museum and a spiritual bridge, connecting our beating hearts with the memories of our ancestors across millennia.", "cn": "每一个流传千年的传统节日皆是一座没有围墙的鲜活博物馆与一座神圣精神立交桥，将我们今天胸膛深处的滚烫心跳同数千年前先贤祖先的记忆深情相连！"},
                {"en": "Inherit these golden holiday traditions with deep pride and loving devotion; for within these ancient customs breathes the immortal soul of China.", "cn": "请怀揣着无上的民族自豪与虔诚大爱去精心呵护传承好这一幕幕节庆文化传统吧——因为正是在这些古老风俗的最深处，安详栖息着我们中华民族不死的璀璨灵魂！"},
                {"en": "Celebrate the richness of our culture, cherish the warmth of family reunion, and pass the torch of Chinese heritage down from age to age forever.", "cn": "尽情赞美我们博大精深的璀璨文明吧，深情珍惜每一次阖家团圆的人间温情，让中华优秀传统文化的灿烂薪火世世代代薪火相传、生生不息、永放光芒！"}
            ]
        },
        {
            "title": "Unit 10 · 憧憬未来高中新起点与立下报国宏图志 · 奔向辉煌新征程",
            "description": "探讨初中毕业谢师礼、迈入重点高中新起点、树立强国有我少年抱负中考满分作文终局升华句。",
            "sentences": [
                {"en": "Standing at the graduation crossroads, we bow deeply to our devoted teachers, whose chalk dust painted the majestic sunrise of our youthful minds.", "cn": "庄严伫立在初中毕业的人生十字路口高台上，我们含泪向讲台前呕心沥血的辛勤恩师们深深鞠下九十度大躬——正是老师们飞扬的三尺粉笔灰，亲手染白了两鬓，却在我们稚嫩心田深处画就了一抹壮美的青春朝阳！"},
                {"en": "Senior high school beckons with deeper academic inquiries, laboratory discoveries, and higher summits waiting for our audacious youthful feet to scale.", "cn": "崭新的重点高中大门正以更加深邃的学术探究、更加前沿的科学实验室奥秘，以及更加崇高巍峨的学业险峰，深情号召召唤着我们大无畏的青春脚步去奋力征服攀登！"},
                {"en": "A nation is strong only when its youth are strong; we vow to anchor our personal ambitions within the grand architecture of national rejuvenation.", "cn": "“少年强则国强，少年智则国智”——我们庄严立誓：坚决将个人的青云之志与微小理想，深深扎根并熔铸进中华民族伟大复兴的壮美历史丰碑大厦深处！"},
                {"en": "The final examination hall is not a terrifying battlefield, but a splendid coronation pavilion where three years of sweat bloom into glorious laurel wreaths.", "cn": "六月中考的考场大殿从来绝非是一个令人胆战心惊的修罗绞肉场；而理应是一座神圣庄严的凯旋加冕大礼堂——正是在这里，我们三千个伏案晨昏的滚烫血汗，将华丽绽放为属于胜者的金色月桂冠！"},
                {"en": "Let your fountain pen become your sharpest sword, turning test sheets into your conquest map; stride across the threshold with head held high.", "cn": "且让你手中的钢笔墨水笔尖化作你手中最锋利的破阵宝剑吧，把每一张白纸黑字的试卷开辟为你征服命运的锦绣地图；昂起头颅，大步跨过考场大门！"},
                {"en": "True excellence is not about outshining your classmates, but about surpassing the limitations of your yesterday self with quiet, unshakeable persistence.", "cn": "世间真正的登峰造极卓越风骨，从来不是在考场上去压倒身旁的同桌同伴；而永远在于用沉静坚如磐石的执着自律，彻底击碎并超越昨日那个有局限的旧自己！"},
                {"en": "Every late night spent grappling with challenging physics theorems has secretly equipped you with the intellectual armor of future scientists and engineers.", "cn": "回首初三那些为了死磕物理压轴大题而鏖战长夜的无数个不眠之夜，实则早已在不知不觉中，为你提前穿戴披挂上了未来成为顶尖科学家与卓越工程师的坚固智识铁甲！"},
                {"en": "Pack your schoolbag with optimism, pack your heart with gratitude, and step forward fearlessly into the boundless golden landscape of tomorrow.", "cn": "在行囊中装满从容乐观的阳光，在胸膛深处装满由衷的温情与感恩，大踏步无所畏惧地迈向那片属于我们明天的无垠金色锦绣前程吧！"},
                {"en": "The bell that signals the conclusion of middle school is simultaneously the opening trumpet heralding the grandest chapter of your blooming life.", "cn": "当象征着初中求学生涯圆满画上句号的终考铃声划破六月天际鸣响之际，它同时间正是拉开你人生最壮丽璀璨青春大戏盛大上演的第一记破晓凯旋号角！"},
                {"en": "Cherish the memory of these chalk-scented classrooms, the friendships forged in sweat, and the fearless dreams whispered into evening breezes.", "cn": "请永远铭记这间充斥着淡淡粉笔墨香的初三教室、铭记球场上挥汗如雨铸就的生死同窗契约，以及在每一个夏日微风晚自习窗前向苍天许下的狂傲远大梦想吧！"},
                {"en": "Our motherland calls upon our generation to master core scientific breakthroughs; we will answer her summons with unwavering courage and brilliance.", "cn": "伟大的祖国正呼唤召唤着我们新一代青年学子勇挑重担、去攻克前沿核心卡脖子科学技术高峰；我们必将用铁一般的担当与绝世才华，向母亲交出满分答卷！"},
                {"en": "No mountain is too steep to climb for the determined; no river is too wide to cross for the united heart of our youth.", "cn": "在志存高远、百折不挠的追梦少年脚下，世间绝无不可攀登的万仞绝顶险峰；在我们紧密团结同舟共济的青春胸膛面前，天下绝无无法跨越的惊涛骇浪！"},
                {"en": "May your examination results be as radiant as the summer sun; may your senior high journey be as magnificent as the soaring eagle.", "cn": "祈愿你中考揭榜时的喜报战绩宛如盛夏骄阳般璀璨夺目金光万道；祈愿你即将盛大开启的三年重点高中新征程，宛如大鹏展翅击水三千里般气吞山河！"},
                {"en": "Farewell, dear junior high days! Forward, brave youthful warriors! The grandest sunrise in human history is waiting just beyond the horizon for you!", "cn": "别了，我们无悔热血的初中三年青葱岁月！向前冲锋吧，英勇无畏的少年英豪们！人类历史上最壮美的一轮喷薄朝阳，正在不远处的绚烂地平线尽头引颈翘首期盼着你的登临加冕！"},
                {"en": "Rise, conquer, and shine; let the brilliant name of Chinese youth be inscribed with golden letters across the sky forever!", "cn": "挺起胸膛，去征服命运、去璀璨绽放吧——且让我们中国当代热血好少年的光辉大名，化作烫金的大字，永远庄严镌刻在我们共和国浩瀚无垠的辽阔苍穹之巅！"}
            ]
        }
    ]
    courses.append(build_course(zk_meta, zk_chapters))

    # -------------------------------------------------------------------------
    # 8. GRE 核心学术词汇与高阶逻辑思辨 (10章) - 严格每章15句，共150句
    # -------------------------------------------------------------------------
    gre_meta = {
        "id": "course-ex-gre",
        "title": "《GRE 核心学术词汇与高阶逻辑思辨精读》(GRE Verbal Reasoning) · 批判性思维天花板 (10章全集)",
        "category": "exam",
        "categoryName": "考试备考",
        "coverGradient": "from-zinc-900 via-neutral-800 to-stone-950",
        "icon": "🏛️",
        "description": "专攻 GRE Verbal Reasoning 填空与长难阅读，深剖哲学实在论、解构主义、认识论断裂与高阶学术修辞。",
        "difficulty": "专家级 C2",
        "tags": ["GRE核心", "GRE Verbal", "批判性思维", "逻辑长难句", "学术天花板"]
    }
    gre_chapters = [
        {
            "title": "Unit 1 · 科学实在论与经验主义反实在论的本体论交锋",
            "description": "探讨科学实体真实性、悲观归纳论、工具主义与拯救现象GRE高阶长难句分析。",
            "sentences": [
                {"en": "Scientific realists maintain that empirically successful theories warrant ontological commitment to the unobservable entities postulated by their mathematical frameworks.", "cn": "科学实在论者坚定断言：在经验实证预测上取得耀眼成功的科学理论，理所当然赋予并要求我们对其纯数学模型推导中所假设预设的那些“不可直接肉眼观测微观实体”进行严肃的本体论承诺！"},
                {"en": "Constructive empiricists, spearheaded by Bas van Fraassen, counter that science aims solely at empirical adequacy rather than metaphysical truth concerning subatomic realms.", "cn": "以巴斯·范·弗拉森为宗师的建构经验主义学派则针锋相对驳斥指出：人类科学大厦的全部终极合理旨归，仅仅在于追求理论对于外在经验表象的“经验充分性（Empirical Adequacy）”，而绝非为了去狂妄敲定亚原子微观世界深处的形而上学终极真理。"},
                {"en": "The pessimistic induction argument underscores that historically revered paradigms—from phlogiston to luminiferous aether—were ultimately discarded, casting doubt upon current ontological orthodoxies.", "cn": "令实在论者寝食难安的“悲观元归纳论辩（Pessimistic Meta-induction）”残酷向世人证明：在人类科学史上曾被无数泰斗大师奉为圭臬的皇皇理论——从燃素说直至发光以太说——最终无一幸免统统被后世无情扔进了历史垃圾堆，这不得不令每一个清醒者对当今主流正统理论的本体论真理宣称打上一个大大的问号！"},
                {"en": "The no-miracles argument asserts that the astounding technological predictive power of modern quantum mechanics would constitute a cosmic miracle if theories were not approximately true.", "cn": "而实在论阵营最具杀伤力的杀手锏——著名的“无奇迹论证（No-Miracles Argument）”则掷地有声大声疾呼：如果现代量子电动力学所呈现出的那令人瞠目结舌、精确到小数点后数十位的惊天技术预测精度不是因为该理论已然无限逼近了客观物质实在真理，那么现代前沿科技的全面爆发就必须被荒谬定性为一场不可思议的宇宙大魔法奇迹！"},
                {"en": "Underdetermination theses demonstrate that for any given set of empirical observational data, infinite logically incompatible yet empirically equivalent theoretical explanations can be formulated.", "cn": "著名的“迪昂-蒯因经验证据对理论的不充分决定性假说（Underdetermination）”从数理逻辑底层无可辩驳地宣告：面对现实世界中任何一组给定的有限经验观测数据集合，在形式逻辑上均永远能够构想炮制出无数套在内在逻辑上截然相反冲突、但在解释外在数据上却完全平起平坐等价的异质竞争理论假说！"},
                {"en": "Instrumentalism reduces sophisticated theoretical terminology to convenient calculative fictions, stripping ontological substance from electrons and wave functions entirely.", "cn": "走上极端的工具主义（Instrumentalism）哲学思潮，极其冷酷地将物理学殿堂中那些繁复精妙的高阶理论概念与数学物理方程，粗暴阉割贬低为纯粹为了方便人类进行工程计算而人为捏造出的“实用计算虚构工具”，彻底将电子与薛定谔波函数剔除出了客观真实存在的本体论户籍！"},
                {"en": "Structural realists attempt an epistemological compromise, conceding that unobservable theoretical entities may perish while mathematical relations between phenomena survive epochal revolutions.", "cn": "为了打破实在论与反实在论的世纪僵局，“结构实在论者（Structural Realism）”试图开辟一条精妙的认识论中间折中路线：他们坦然承认理论所设定的微观物质实体客体完全有可能随着时代洗牌而灰飞烟灭，然而统领物理现象背后深层内在逻辑结构的“数学物理关系与拓扑几何定律”，却能在一次次沧海桑田的科学范式大革命中历久弥新、永恒不灭！"},
                {"en": "Incommensurability doctrines stipulate that competing scientific paradigms cannot be adjudicated through neutral objective algorithms because their very conceptual vocabularies lack translation.", "cn": "托马斯·库恩那令正统学界闻风丧胆的“范式不可通约性定理（Incommensurability）”石破天惊地宣告：在历史舞台上分庭抗礼的两大异质科学范式，从来绝不可能指望诉诸任何所谓绝对客观中立的裁判算法予以分出高下是非——因为在深层本体论语境巨变之下，双方赖以立论的整个概念术语词典本身，已然彻底丧失了跨范式无损翻译互通的逻辑基石！"},
                {"en": "Entity realists argue that when experimental physicists manipulate electrons through particle accelerators to engineer novel phenomena, their tangible existence is settled beyond academic dispute.", "cn": "以伊恩·哈金为代表的先锋“实体实在论者”则以实验物理学家的务实底气一剑封喉地反驳道：当顶尖高能物理学家已然能够驾轻就熟在大型粒子对撞机中精准操纵引导电子束去轰击喷淋出全新物理现象时，电子作为一个真实客观实体的硬核存在性，便早已在实验台的物理操作中盖棺定论，远远超越了书斋哲学家们无休止的口水辩难！"},
                {"en": "Epistemic humility demands acknowledging that our current empirical models may represent transient approximation milestones along an asymptotic, endless voyage of cosmic comprehension.", "cn": "人类面对浩瀚苍茫深邃宇宙所必须恪守的最高“认识论谦逊（Epistemic Humility）”庄严要求我们清醒坦承：当代人类引以为傲的最高精尖前沿科学理论模型，归根结底不过仅仅只是人类渺小心智在沿着一条无限逼近客观真理的渐近线万里求索大征途上、所偶然拾阶而上的一个充满暂态局限性的过渡阶段里程碑！"},
                {"en": "Epistemic contextualism highlights that justification standards fluctuate across divergent discursive contexts, refuting foundationalist epistemic architectures.", "cn": "认识论语境主义前沿学说深刻揭示：知识辩护合理性标准在不同的学术话语语境中呈现出高度动态浮动特征，彻底瓦解击碎了笛卡尔式寻求绝对不可动摇确凿阿基米德支点的基础主义知识大厦构想。"},
                {"en": "The Duhem-Quine holism thesis reminds us that theoretical hypotheses are never tested in isolation, but face the tribunal of experience as an interconnected web.", "cn": "迪昂-蒯因整体论原则警醒我们：任何单一的科学假说从来绝不可能脱离大系统被单独拎出来孤立接受检验；面对经验法庭严酷审判的，永远是由基础定律、辅助假设乃至仪器校准参数共同编织成的一整张休戚与共的致密知识巨网！"},
                {"en": "Theory-ladenness of observation dictates that sensory observations are inextricably imbued with the theoretical assumptions of the observer.", "cn": "观察渗透理论（Theory-ladenness）的经典认识论洞见揭示：人类感官在显微镜与望远镜前所“观测”到的一切原始视网膜数据，从发生那一瞬间起，便已然不可逆地深深浸润并被观察者大脑中先入为主的理论假设所结构化重塑！"},
                {"en": "Pragmatist epistemologies measure scientific truth not by correspondence with a noumenal reality, but by successful experimental coping within the phenomenal lifeworld.", "cn": "先锋实用主义认识论测量科学理论真理成色的试金石，绝非看其究竟是否在形而上学上同那个高高在上不可捉摸的“物自体实在”达成神秘镜像对应，而唯独丈量于其能否在现象生活世界中赋予人类解决实际危机与生存挑战的破局实操功力！"},
                {"en": "Science remains humankind's most sublime intellectual monument, forever sailing between the Scylla of dogmatic certainty and the Charybdis of nihilistic despair.", "cn": "人类科学探索大航海事业永远是这颗蔚蓝星球上最荡气回肠的智识丰碑——在波澜壮阔的惊涛骇浪深处，它手握理性的舵盘，永远在教条自负绝对确定性的斯库拉礁石同虚无主义绝望怀疑论的卡律布狄斯大漩涡之间，以绝美的姿态破浪勇毅前行！"}
            ]
        },
        {
            "title": "Unit 2 · 政治哲学中的契约论演进与正义分配原则",
            "description": "探讨霍布斯利维坦自然状态、罗尔斯无知之幕、诺齐克持有正义与社群主义批判。",
            "sentences": [
                {"en": "Thomas Hobbes posited that the pre-political state of nature was a nightmarish theater of perpetual war where human life was solitary, poor, nasty, brutish, and short.", "cn": "托马斯·霍布斯在其划时代政治哲学巨著《利维坦》中冷酷断言：在国家政治契约诞生之前的原始自然状态，乃是一方一切人对一切人的永恒全面残酷内战修罗场，在那里人与人互为豺狼，人类苟且的生命状态注定只能是“孤僻、穷困、卑污、残暴且短命”！"},
                {"en": "John Locke's social contract theory grounded legitimate governmental sovereignty in the fiduciary obligation to protect inalienable natural rights to life, liberty, and estate.", "cn": "约翰·洛克的自由主义社会契约论学说，将国家公共公权力统治的一切合法性底线根基，毫不妥协地牢牢锚定在政府作为受托人必须恪尽职守誓死捍卫公民个体生命权、自由权以及私人财产所有权这一不可剥夺不可让渡的神圣天赋自然权利底线之上！"},
                {"en": "Jean-Jacques Rousseau lamented that man was born free yet everywhere found himself chained by corrupt institutional hierarchies, advocating submission to the general will.", "cn": "让-雅克·卢梭曾发出撼动整个人类历史的泣血哀叹：“人人生而自由平等，却无往不在封建专制等级制度的沉重枷锁镣铐之中！”——他力主建立真正民主共和政体，号令全体公民以崇高的公民自律决然臣服统摄于至高无上的公意（General Will）的大旗之下！"},
                {"en": "John Rawls revolutionary veil of ignorance thought experiment compels deliberators to architect principles of justice from an original position of absolute impartiality.", "cn": "约翰·罗尔斯名垂青史的“无知之幕（Veil of Ignorance）”划时代思想实验，以惊天大智慧强制逼迫所有参与顶层宪制设计的立法协商者，必须在彻底剥离遗忘自身在真实社会中所可能落入的阶级出身、财富智商与家庭门第的“原初绝对无偏私状态”下，合谋推演正义法则！"},
                {"en": "The difference principle mandates that socio-economic inequalities are morally permissible only if they operate to the maximum benefit of the least advantaged societal members.", "cn": "罗尔斯正义理论核心皇冠上的明珠——著名的“差别原则（Difference Principle）”以钢铁般的崇高正义律条严正宣判：任何社会经济制度层面所默许存在的贫富不平等与阶层分化，唯有且必须建立在一个神圣的刚性先决条件之上——那就是该项制度安排必须以最极限的方式全面致力于最大化增进全社会处于最不利最弱势底层群体的根本福祉！"},
                {"en": "Robert Nozick's libertarian entitlement theory violently rejected patterned distribution schemes, defending minimal state apparatuses that guard against force and fraud exclusively.", "cn": "罗伯特·诺齐克所扛鼎创立的右翼自由意志主义“持有正义所有权资格理论”，对任何带有财富再分配色彩的福利主义模式发起了雷霆万钧般的口诛笔伐与决绝抗辩，死死捍卫除了防范暴力掠夺与商业欺诈履约之外绝不干预市场经济的所谓“守夜人式极小国家模型”！"},
                {"en": "Communitarian philosophers such as Michael Sandel criticized Rawlsian liberalism for constructing an 'unencumbered self' detached from historical communitarian moral attachments.", "cn": "以迈克尔·桑德尔为代表的社群主义政治哲学巨匠们，以极其犀利的手术刀利刃狠狠刺破了罗尔斯自由主义哲学的命门弊端——痛斥其在虚构理论模型中凭空捏造构建出了一个彻底割裂剥离了自身历史文化传统、乡土人伦温情与道德血脉联结的冰冷空洞的所谓“无拘无束的孤立自我（Unencumbered Self）”！"},
                {"en": "Utilitarian doctrines championing the greatest happiness principle are vulnerable to the devastating critique that they countenance sacrificing vulnerable individuals for aggregate pleasure.", "cn": "功利主义伦理学那套宣称“追求最广大受众最大幸福化”的庸俗算术逻辑，在现代政治法学法庭上屡屡遭遇致命的道德破产审判：其底层逻辑在极端情形下竟然能够冠冕堂皇为“为了所谓集体总福利的最大化而合谋残忍牺牲碾压极少数无辜弱势个体的基本人权”公然辩护张目！"},
                {"en": "The concept of positive liberty advocates state interventions ensuring citizens possess substantive real-world material capabilities to achieve self-realization.", "cn": "以以赛亚·伯林为代表所阐发的“积极自由（Positive Liberty）”崇高法理范畴大声疾呼：国家公共权力绝不能仅仅局限于消极不干预，而必须主动以社会主义国家的大爱担当发起制度性兜底干预，确保每一个底层寒门公民均实打实享有推开大学校门、享有基本生存保障与登顶自我实现的物质能力武器！"},
                {"en": "Political legitimacy cannot be purchased through economic efficiency metrics alone, but requires democratic accountability that respects every human being as an end.", "cn": "一个执政政权的至高政治合法性，从来绝不可能单凭在统计报表上刷出多么耀眼的纸面经济增长柱状图便能廉价收买购买；它永远庄严苛求着毫无阴暗角落的民主法治问责制，要求政治权力的每一次行使，必须将大地上每一个活生生的鲜活人民群众，视作至高无上的终极目的本身而非实现野心的冰冷工具！"},
                {"en": "Deliberative democracy theories demand that political decisions be legitimized through uncoerced public reasoning among equal citizens in transparent public spheres.", "cn": "协商民主前沿政治哲学大厦坚定主张：现代公共重大决策的终极合法性，唯有在全体平等的公民得以在毫无专制暴力威逼利诱的透明公共领域里，通过充分理性公共辩论协商方得确立。"},
                {"en": "Legal positivism maintains that legal validity is determined by social conventions of institutional enactment rather than moral goodness.", "cn": "法律实证主义学派以近乎冷酷的理性逻辑坚决主张将法律与道德作严格的二元剥离——法条的刚性法律效力，全然取决于其是否由享有合法主权的立法机构按法定程序庄严颁布，而绝非取决于其在形而上学层面是否符合所谓纯善先验道德。"},
                {"en": "Natural law traditions counter that unjust statutory edicts lack true legal character, asserting that lex iniusta non est lex across historical eras.", "cn": "而源远流长的西方自然法正义传统则以气吞山河的正义之剑断然宣告：“恶法非法（Lex iniusta non est lex）”——任何严重背离人类永恒良知公义、践踏基本人伦尊严的暴虐统治暴政敕令，从其签署出炉的那一刻起，便彻底丧失了称其为法律的全部神圣资格！"},
                {"en": "Republican conceptions of non-domination insist that freedom requires not merely the absence of actual interference, but protection against arbitrary subjugation.", "cn": "古典共和主义关于“免于支配（Non-domination）”的深刻自由意涵强调指出：真正的自由境界，绝不仅仅是指在当下这一秒没有遭受棍棒殴打干涉；而在于拥有宪制保障制度铠甲，确保自己永远不必在任何专横主子的脸色喜怒无常之下卑躬屈膝、提心吊胆偷生！"},
                {"en": "The perpetual quest for a just commonwealth remains humanity's sacred calling, illuminating our restless moral pilgrimage across centuries of historical storms.", "cn": "在天地之间永不停歇地追寻、探索并用鲜血与智慧去亲手筑起一座大公无私的天下为公正义城邦，是人类文明最庄严神圣的不死使命，它如同一簇永恒闪耀在历史惊涛骇浪深处的璀璨北极星，永远深情照亮着我们跨越数千年风雨沧桑的道德朝圣大远征！"}
            ]
        },
        {
            "title": "Unit 3 · 历史编纂学与叙事客观性的后现代解构",
            "description": "探讨兰克如实直书客观史学、海登·怀特元史学叙事构作与历史真相重构长难句。",
            "sentences": [
                {"en": "Leopold von Ranke's foundational nineteenth-century historiography established the rigorous methodological imperative to reconstruct the past 'as it essentially occurred'.", "cn": "利奥波德·冯·兰克在十九世纪史学界所确立并开宗立派的近代科学史学奠基实证方法论，曾向全天下历史学家立下了一条如摩西十诫般不可逾越的神圣铁律——必须不带半点主观私心杂念、以严谨史料档案考据去绝对原汁原味还原历史“本来的真实面目（Wie es eigentlich gewesen）”！"},
                {"en": "Archival positivists championed primary documentary records as unvarnished empirical relics capable of speaking for themselves without ideological contamination.", "cn": "狂热迷信实证文献档案实证主义史学泰斗们，曾天真地将深锁在皇家档案馆里的原始一手档案卷宗文书奉若神明，盲目迷信这些带着岁月尘埃的羊皮纸残片能够超越时代偏见、毫无遮掩地让历史真相在阳光下自发口吐真言。"},
                {"en": "Postmodern metahistory pioneered by Hayden White decisively dismantled the illusion of historical objectivity by analyzing historical texts as literary artifacts.", "cn": "海登·怀特名垂青史的先锋经典巨著《元史学》横空出世，以石破天惊的批判利刃无情彻底打碎粉碎了所谓“历史客观中立性”的神话画皮——通过以文学批评的显微镜解剖史书文本，无可辩驳地揭示出一切皇皇历史巨著本质上皆是被作者赋予了深层诗学修辞编织的语言文学造物！"},
                {"en": "Historical narrative construction inevitably deploys deep linguistic tropes—metaphor, metonymy, synecdoche, and irony—to configure historical chronicles into meaningful moral dramas.", "cn": "任何历史学家在提笔将浩瀚零散的史料断片串联编织成有头有尾的连续叙事史册之时，皆在潜意识中不可遏制地深度调度调配了四大核心深层诗学修辞转义手法——隐喻、借代、提喻与反讽，从而将原本冰冷混沌的历史事实强行塑形编织成了带有明确价值评判的道德剧情大戏！"},
                {"en": "The ideological selection of which primary documents are preserved within state archives reflects the hegemon's deliberate erasure of marginalized subaltern voices.", "cn": "历朝历代国家最高权力机关在主权档案馆深处对于“究竟准予哪些官方诏书公文得以永久封存、又对哪些民间异端竹简予以焚烧销毁”的冷酷筛选过滤机理，无一不是统治阶层在幕后利用国家机器对底层边缘弱势群体血泪呐喊声音所实施的一场场处心积虑的蓄意历史抹杀！"},
                {"en": "Annales school historians rejected traditional diplomatic obsession with charismatic kings, shifting analytical focus toward the geological 'longue durée' and material structures.", "cn": "法国年鉴学派史学大师们以大无畏的学术革命，决绝唾弃了传统正统史学对帝王将相宫廷政变与外交条约战争的病态狭隘痴迷，大刀阔斧将整部历史解剖的聚光灯，全面转移聚焦至以数百年为尺度的地理气候生态变迁“长时段（Longue Durée）”与最底层柴米油盐物质文明基础设施架构深处！"},
                {"en": "E.H. Carr famously observed that historical facts resemble fish swimming in a vast ocean; what the historian catches depends entirely on which part of the sea he chooses to fish.", "cn": "爱德华·卡尔当年在那篇传世名篇《什么是历史》中留下了令后世拍案叫绝的经典隐喻断言：“客观历史事实恰似一条条畅游在浩瀚无垠大洋深处的游鱼；历史学家最终究竟能打捞捕捉到何种鱼获，自始至终全然绝非取决于鱼群本身，而完全取决于该历史学家究竟处心积虑选择把渔船开到哪一片特定海域下网！”"},
                {"en": "Microhistory approaches analyze localized, seemingly trivial everyday legal records to reconstruct the mental universe of ordinary peasants across historical epochs.", "cn": "风靡全球史学界的“微观史学（Microhistory）”先锋研究范式，另辟蹊径专挑那些散落在宗教裁判所审判卷宗里看似微不足道的乡间磨坊主、铁匠等升斗小民的日常口供记录展开抽丝剥茧式深剖，在显微镜下惊艳重构出欧洲中世纪寻常农夫脑海深处那一整座光怪陆离的心智大宇宙！"},
                {"en": "Presentism threatens historical understanding when contemporary analysts project modern moral criteria anachronistically upon historical actors trapped within distinct cosmological paradigms.", "cn": "让当代严肃史学警钟长鸣的恶性“当下主义偏见（Presentism）”毒瘤，特指当今那些不学无术的浮浅评论家在跨越时空审判古人时，极其傲慢荒谬地把二十一世纪当代社会的价值观与道德法庭刻度尺，生搬硬套强加于数千年前受制于特定物质技术与迷信桎梏的古人头颅之上！"},
                {"en": "Totalizing meta-narratives claiming to unveil universal historical destinies are challenged by fragmented histories that illuminate the irreducible contingency of events.", "cn": "那些妄图凭借一套放之四海而皆准的宏大黑格尔式目的论哲学教条去强行包打天下、宣称窥破了全人类历史所谓“终极机械铁律宿命”的宏大叙事神话，在当代已被海量充满异质性、生动展现人类历史大拐点处处充满偶然性变数与历史能动性的鲜活断片史实击得千疮百孔！"},
                {"en": "Colonial archives structured through administrative classifications codify subjugated populations into stereotyped racial taxonomies serving bureaucratic policing.", "cn": "殖民帝国在海外总督府所建立的殖民档案体系，巧妙借由冰冷行政权力将形形色色的被征服原住民野蛮规训压缩进一套套刻板恶毒的种族等级分类抽屉，全然沦为服务于维稳绞杀的官僚机器利刃。"},
                {"en": "Oral history methodologies empower disenfranchised working-class communities to transmit collective traumatic memories that elite print cultures suppressed.", "cn": "开创性的现代民间口述史学采风范式，以深情的大爱笔触，强有力赋能了数以千万计在主流印刷精英典章中被剥夺话语权的工农平民，得以亲口将那些在历史惊涛骇浪中受尽苦难的集体创伤记忆原汁原味抢救留存！"},
                {"en": "Historical revisionism is not an unprincipled crime, but the legitimate intellectual duty of scholars re-evaluating evidentiary archives in light of newly excavated sources.", "cn": "真正意义上的史学学术修正主义，绝非是什么见不得人的欺师灭祖罪愆；而恰恰是一个严谨学者在面对地底下最新破土而出的出土文献铁证面前，必须勇于与时俱进、以大无畏学术求真勇气对既成定论展开自我革命的崇高学术天职！"},
                {"en": "The pursuit of historical truth resembles approaching a mathematical asymptote; absolute confluence remains unreachable, yet disciplined approximation remains moral duty.", "cn": "对客观历史真理的终生苦苦求索，恰如在笛卡尔坐标系中无限逼近一条终极渐近线——尽管绝对的一百零分历史全景重现注定人力不可企及；然而以最严苛考据无限无限逼近那段历史的真实体温，却永远是每一个史家在良知长夜中不可亵渎的唯一道德灯塔！"},
                {"en": "History is not a cemetery of cold, forgotten bones, but a sacred mirror holding the trembling reflection of our present struggles and future hopes.", "cn": "整部人类历史从来绝非是一座横陈着冰冷死人白骨的荒凉大乱葬岗；它乃是一面高悬在天地苍穹深处的至高明镜——正是在那波光流转的镜面最深处，深情倒映着我们当下所有人正在滚烫经历的苦难挣扎，与我们全人类对未来不灭的星空希望！"}
            ]
        },
        {
            "title": "Unit 4 · 认知科学中心身问题与涌现论心智哲学",
            "description": "探讨笛卡尔实体二元论、还原物理主义、功能主义计算隐喻与感受质主观鸿沟。",
            "sentences": [
                {"en": "René Descartes classical substance dualism bifurcated reality into res extensa—extended physical matter—and res cogitans—non-spatial, thinking mental substance.", "cn": "勒内·笛卡尔名垂千古的“实体二元论（Substance Dualism）”哲学体系，以大刀阔斧的形而上学之剑将整个人类存在宇宙一分为二：一方是受制于机械几何物理定律、拥有空间体积延展的“广延实体（Res Extensa）”，另一方则是完全超脱于三维时空之外、拥有纯粹自由自觉意向性的神圣“思维实体（Res Cogitans）”！"},
                {"en": "The mind-body problem interrogates how immaterial, non-physical psychological intentions can exert causal mechanical leverage upon biological motor neurons.", "cn": "在哲学界巍然耸立数百年至今仍未彻底攻克的“心身问题（Mind-Body Problem）”核心深渊叩问：完全不具备物理质量、不占据任何三维空间体积的主观意识心理意图，究竟究竟是如何得以跨越物理鸿沟、在肉身的大脑神经元突触放电中精准撬动杠杆并支配凡胎肉身行动的？！"},
                {"en": "Reductive physicalism maintains that mental states are strictly identical with localized neurochemical brain events, eliminating dualist metaphysics entirely.", "cn": "还原物理主义（Reductive Physicalism）旗帜鲜明主张将心智完全还原为物质，断言人类心田深处的一切爱恨情仇与灵魂思想，在微观物理层面上百分之百严格等同于特定大脑皮层神经网络内部神经递质与生化电信号的微观物理事件，誓要将一切二元论形而上学鬼神扫地出门！"},
                {"en": "Eliminative materialists such as the Churchlands argue that our intuitive 'folk psychology' incorporating beliefs and desires will be abolished by neurobiology.", "cn": "以丘奇兰德夫妇为旗手的“取消唯物主义（Eliminative Materialism）”激进哲学狂人甚至公开宣称：人类日常口口相传、自古相沿成习的所谓“信念、愿望、痛苦、狂喜”等民俗心理学常识词汇，终将在未来成熟精准的高维神经脑生物学面前被彻底像当年“燃素说”一般宣告纯属伪概念并被永久取缔废除！"},
                {"en": "Functionalism conceptualizes the human mind as algorithmic software instantiated upon the biological hardware wetware of the organic brain.", "cn": "风靡当代认知科学界的“功能主义（Functionalism）”学派，巧妙将人类大脑心智解构隐喻为一套高度抽象脱耦的算法软件操作系统，而颅骨深处那团充满水分与蛋白质的生物有机神经突触肉身，不过仅仅充当着支撑该智能算法运转的底层“湿件硬件（Wetware）”载体而已！"},
                {"en": "Multiple realizability theorems posit that identical computational mental states can be implemented across biological neurons, silicon microchips, or alien chemistries.", "cn": "“多重可实现性定理（Multiple Realizability）”从数学与算法底层大胆宣告：同一种高阶认知思维计算状态，完全可以在碳基生物大脑、硅基半导体微芯片芯片，乃至由未知奇异化学元素构成的地外星际生命机体之上被完全等价无损地实现与运行！"},
                {"en": "Thomas Nagel's iconic philosophical treatise 'What Is It Like to Be a Bat?' demonstrated that subjective phenomenal experience resists third-person reduction.", "cn": "托马斯·内格尔名垂青史的经典哲学诘问巨著《成为一只蝙蝠究竟是怎样的一种体验？》以无可辩驳的逻辑向世人证明：第一人称主观“感知体验感受（Phenomenal Consciousness）”，在原理上永远具有无法被任何客观第三人称科学仪器测量与物理还原公式所彻底吞噬消解的认识论鸿沟！"},
                {"en": "The hard problem of consciousness articulated by David Chalmers asks why informational neurobiological processing should be accompanied by inner felt experience.", "cn": "当代心智哲学泰斗大卫·查尔默斯振聋发聩抛出的“意识难题（The Hard Problem of Consciousness）”直击灵魂深处：为什么当大脑神经元在进行极其复杂的物理信息计算与电信号传递加工时，非要在当事人内心深处极其奢侈地伴生出那一抹如饮甘霖、能被自我感受到的主观“内省内在体验质感”？！"},
                {"en": "Frank Jackson's Mary's Room thought experiment proves that physical omniscience fails to encompass qualitative qualia such as the phenomenal sensation of red.", "cn": "弗兰克·杰克逊著名的“黑白玛丽房间”思想实验设计了一位精通全宇宙一切色彩神经物理波长知识、却终生生活在黑白单色房间里的超级科学家玛丽；当她首次推开房门亲眼目睹一朵鲜红娇艳的红玫瑰那一瞬间，她无疑顿悟斩获了关于“红色究竟是何种感官质感（Qualia）”的全新知识——以铁证击碎了唯物理论的盲目傲慢！"},
                {"en": "Emergentism proposes that when simple biological components achieve critical organizational complexity, novel mental properties arise that defy constituent reduction.", "cn": "博大精深的“涌现论（Emergentism）”高维系统科学哲学指出：当无数极其平淡无奇、毫无意识的微观神经元细胞按照极其精密错综复杂的高阶拓扑网络层层组织架构在一起时，便会在整体临界点爆发式“涌现”出任何微观零散零件所根本不具备的、不可还原的崭新主观心智涌现奇迹！"},
                {"en": "Panpsychism offers a radical metaphysical alternative, suggesting that rudimentary consciousness represents an intrinsic, ubiquitous feature of all fundamental physical matter.", "cn": "在当代学术前沿卷土重来的“泛心论（Panpsychism）”前卫哲学思潮大胆设想：哪怕是构成全宇宙最基础的微观夸克与轻子，其内在最深层本征属性深处，自始至终皆微弱安详潜伏沉睡着最原始微观维度的“原初意识火星”，全宇宙本就是一个生机盎然的觉醒生命整体！"},
                {"en": "The illusion of a centralized Cartesian theater where an internal homunculus observes sensory screens is dismantled by distributed neural processing architectures.", "cn": "当代认知神经科学彻底粉碎了解剖学深处所谓存在一个微小内部小人坐在“笛卡尔内省大剧院”正中央凝视屏幕的幼稚神话——现实大脑内部乃是由数以百计分布在各个皮层、各司其职又彼此激荡共振的并行分布式异步信息流网络在共同织就意识交响！"},
                {"en": "Cognitive neuroscience reveals that human decision-making is not a purely rational algorithmic deduction, but is deeply entangled with somatic emotional markers.", "cn": "安东尼奥·达马西奥前沿神经实验表明：人类的任何所谓理性决断，从来绝非纯粹基于冷冰冰的数理逻辑推演；深植在躯体肉身骨髓深处的“情绪躯体标记（Somatic Markers）”，在暗中为理性指南针定海神针般校准着生死抉择的方向。"},
                {"en": "Consciousness is the golden mirror through which the dark, silent universe awakens to witness, contemplate, and marvel at its own magnificent architecture.", "cn": "人类至高无上的自我主观自觉意识，乃是浩瀚茫茫宇宙历经数十亿年演化神工所亲手磨砺出的一面至高无上的黄金明镜——正是在这面明镜深处，原本漆黑、冰冷、死寂的物质宇宙，终于破天荒如梦初醒般睁开了双眼，深情凝望、沉思并由衷惊叹于其自身的瑰丽壮美！"},
                {"en": "We are stardust that learned to think, to suffer, to yearn, and to love; in the crucible of mind, physical matter transcends its own mortality.", "cn": "我们人类是学会了思考、学会了痛哭、学会了渴望并学会了深情大爱的宇宙星尘；在人类深邃的心智与灵魂大熔炉深处，原本平淡无奇的物理物质，终于以令人泪目的神圣姿态，彻底超越战胜了其自身的有限与死亡！"}
            ]
        },
        {
            "title": "Unit 5 · 演化生物学中的适应主义范式批判与中性突变论",
            "description": "探讨古尔德圣马可教堂拱肩隐喻、木村资生中性演化、表型可塑性与间断平衡论。",
            "sentences": [
                {"en": "The pan-selectionist adaptationist programme within evolutionary biology assumed that every anatomical trait represents an optimized adaptation crafted by natural selection.", "cn": "在传统极端达尔文主义阵营中大行其道的“泛选择论适应主义大纲（Adaptationist Programme）”，曾狂妄武断地默认假设：生物机体表面所呈现出的每一个哪怕最微不足道的解剖学性状特征，皆百分之百是自然选择神功为了应对特定生存环境而精雕细琢出的极致最优适应杰作！"},
                {"en": "Stephen Jay Gould and Richard Lewontin dismantled adaptationist hubris through their landmark critique invoking the architectural spandrels of San Marco.", "cn": "斯蒂芬·杰·古尔德与理查德·列万廷联袂发表名垂青史的划时代论文《圣马可教堂的拱肩与庞格罗斯范式》，以极其震撼的威尼斯圣马可大教堂穹顶下那些完全因建筑工程力学需要而天然伴生出现的“三角拱肩（Spandrels）”为精妙隐喻，彻底粉碎了泛选择论的狂妄画皮！"},
                {"en": "Biological spandrels are phenotypic by-products that emerge as mechanical structural consequences of developmental constraints rather than direct adaptations.", "cn": "生物演化中的“演化拱肩（Spandrels）”现象无可辩驳地揭秘：生物体身上大量的复杂表型特征，在本质上不过仅仅只是生物发育力学底层系统约束下所必然伴生出的“次生结构物理副产品”，根本从来未曾受过自然选择的专门青睐定制！"},
                {"en": "Motoo Kimura's revolutionary neutral theory of molecular evolution demonstrated that the overwhelming majority of genetic mutations are evolutionary neutral drifting randomly.", "cn": "日本遗传学巨匠木村资生所开创的革命性“分子演化中性学说（Neutral Theory）”以铁一般的数据向全球科学界宣告：在漫长的生命演化银河深处，绝大多数在DNA分子水平上所爆发的基因突变，根本不涉及任何优胜劣汰的利害生杀，而是在“中性遗传漂变（Genetic Drift）”的随机掷骰子中自由流淌！"},
                {"en": "Random genetic drift exerts disproportionate evolutionary momentum within small founder populations, fixing neutral alleles independent of adaptive Darwinian fitness.", "cn": "在遭遇瓶颈期规模急剧萎缩的小种群或拓荒奠基者先锋部落之中，纯粹由概率偶发性主导的“随机遗传漂变”往往会爆发出压倒一切的惊天演化动力，甚至将毫无适应优势的中性突变等位基因强行在全种群中实现百分之百的纯合固定！"},
                {"en": "Evo-devo research reveals that massive morphological diversifications result not from novel structural genes, but from shifts within ancient regulatory genetic switches.", "cn": "现代前沿“演化发育生物学（Evo-Devo）”震撼向世人揭秘：自然界千姿百态、天差地别的宏观物种形态大爆炸大分化，绝大多数根本不需要去从零凭空发明什么崭新的结构蛋白基因，而仅仅是在胚胎期对那些跨物种保守了数亿年之久的古代“基因调控开关（Hox Genes）”实施了不同时空节点的精妙微操！"},
                {"en": "The punctuated equilibrium model posits that species experience prolonged intervals of stasis interrupted by rapid bursts of speciation in peripheries.", "cn": "古尔德与埃尔德雷奇联袂提出的“间断平衡论（Punctuated Equilibrium）”，彻底推翻了传统进化论关于生物演化永远是匀速平缓爬行的陈腐教条——指出物种在其漫长演化史的绝大多数时间里皆安详沉睡在长达数百万年的“演化停滞静止期”，而唯独在极边缘孤立生境遭遇突变时爆发短暂而剧烈的“暴风雨式极速成种大跃进”！"},
                {"en": "Phenotypic plasticity enables a single identical genotype to unfurl divergent physiological morphologies when exposed to divergent environmental triggers.", "cn": "令人叹为观止的“表型可塑性（Phenotypic Plasticity）”大智慧生动向世人展现：完全拥有百分之百相同DNA基因组的孪生生命个体，在面对大自然截然不同温度、光照或天敌刺激的诱导下，能够宛如魔术师般自由伸展绽放出完全判若两物的差异化生理与形态结构！"},
                {"en": "Phylogenetic inertia acts as an evolutionary constraint, locking developmental pathways into ancestral body plans inherited from distant Cambrian ancestors.", "cn": "深刻烙印在每一个生命胚胎深处的“系统发育惰性与历史系统约束（Phylogenetic Inertia）”，像一把无形的古老枷锁，将现代物种的发育演进路线死死锁定禁锢在早在五亿年前寒武纪大爆发时期祖先便早已奠定定型的基础“解剖构架蓝图（Bauplan）”深处！"},
                {"en": "Evolution is not an omnipotent divine engineer optimizing bespoke perfection, but a resourceful bricoleur improvising survival from pre-existing historical scraps.", "cn": "法国生物学大师弗朗索瓦·雅各布曾留下名垂青史的经典判词：生命漫长而伟大的演化大工匠，从来绝非是一位在图纸前追求尽善尽美绝对完美的“全知全能神圣工程师”；而永远是一位在残砖碎瓦垃圾堆里翻箱倒柜、利用祖先遗留下的既有历史废旧零件修修补补拼凑凑合出一番生存活路的“机智补锅匠（Bricoleur）”！"},
                {"en": "Epigenetic inheritance mechanisms involving DNA methylation demonstrate that ancestral environmental exposures can transmit phenotypic adjustments transgenerationally without altering genomic sequences.", "cn": "前沿表观遗传学机制清晰表明：DNA胞嘧啶甲基化与组蛋白修饰，使得祖辈在苦难风霜中所经历的饥荒或逆境表型代偿印记，得以在毫不改变DNA碱基序列的前提下跨代向子孙后代实行跨代精准传递！"},
                {"en": "Symbiogenesis championed by Lynn Margulis established that eukaryotic cells originated through endosymbiotic engulfment of ancestral respiring bacteria.", "cn": "林·马古利斯名垂青史的“内共生学说（Endosymbiosis）”无可辩驳地确立：人类与万物真核细胞的伟大破晓问世，本质上是一场远古厌氧宿主细胞将古老好氧呼吸细菌一口吞入腹中后所结成的休戚与共、生死相依的伟大细胞器共生奇迹！"},
                {"en": "Altruistic behaviors in social organisms defy selfish gene reductionism, necessitating multi-level selection frameworks operating simultaneously across individuals and groups.", "cn": "在群居动物与人类社会中广泛闪耀的无私舍身利他崇高行为，彻底击碎了庸俗自私的单基因决定论，在学术上迫切呼唤我们引入涵盖个体竞争与群体合作双轨并行的“多层级选择宏伟演化框架（Multi-level Selection）”！"},
                {"en": "Nature is not a totalitarian assembly line churning out uniform machines, but a boundless, chaotic wilderness celebrating the endless variety of life.", "cn": "大自然从来绝非是一座冰冷死板、千篇一律流水线倾销标准化克隆工具人的极权大工厂；而是一方浩瀚磅礴、充满野性变数、在风雨狂澜中深情歌颂生命无限多样生机与韧性的神圣大荒野！"},
                {"en": "There is grandeur in this view of life; from so simple a beginning, endless forms most beautiful and most wonderful have been, and are being, evolved.", "cn": "查尔斯·达尔文在《物种起源》终局篇章中留下了令全人类热泪盈眶的不朽赞歌：“生命在这样一种宏伟博大的视角审视之下显得何等庄严神圣——正是从一个如此纯净质朴的最初微弱起点启程，在这颗蔚蓝星球上，曾经孕育、并且至今依然在不断演进盛开着无数最绝美、最令人叹为观止的无尽生命华章！”"}
            ]
        },
        {
            "title": "Unit 6 · 艺术美学与文学理论中的形式主义、互文性与解构批判",
            "description": "探讨巴赫金复调小说对话理论、克里斯蒂娃互文性、新批评细读法与德里达延异长难句。",
            "sentences": [
                {"en": "Russian Formalism asserted that the primary purpose of literary art is to defamiliarize habitual perception, revitalizing the stone to make it feel stony once again.", "cn": "俄国形式主义文学理论先驱什克洛夫斯基庄严确立了一条传世美学宗旨：真正的文学艺术至高神圣天职，正是为了以精妙的艺术化手法果断打破并终结人类感官日久麻木的习惯性感知定势，以此彻底打破现实的坚冰，“去让一块顽石重新恢复其宛如刀刻斧凿般的坚硬岩石质感！”"},
                {"en": "The Anglo-American New Criticism framework championed close reading techniques that treated the poetic text as a self-contained, autonomous verbal icon.", "cn": "英美“新批评派（New Criticism）”学术阵营大声疾呼并推行炉火纯青的“文本细读法（Close Reading）”，坚决主张彻底剥离作者的生平八卦与时代时代背景干扰，将诗歌文本自身庄严奉为一座自圆其说、自足自足的“独立自主的语词图腾圣像（Verbal Icon）”！"},
                {"en": "The intentional fallacy and affective fallacy warned against anchoring literary interpretation either within the author's psychological design or the reader's emotional reactions.", "cn": "新批评派泰斗维姆萨特与门罗·比尔兹利联手抛出的“意图谬见（Intentional Fallacy）”与“感受谬见（Affective Fallacy）”两大传世戒律，三令五申告诫学术界：一部文学杰作的文本客观审美评价，绝不能自作多情锚定在原作者隐秘的创作心理初衷深处，更绝不能沦落随波逐流于不同读者千奇百怪、浮于表面的主观情绪宣泄狂欢！"},
                {"en": "Mikhail Bakhtin's dialogic theory revealed that Dostoevsky's novels represent polyphonic masterworks where divergent characters embody autonomous philosophical consciousnesses.", "cn": "米哈伊尔·巴赫金名垂青史的“对话主义与复调小说理论”，以惊世骇俗的洞察力向世人揭秘：陀思妥耶夫斯基的旷世经典巨著绝非作者个人独断专行的单向思想灌输独白；而是一曲惊天地泣鬼神的多声部“复调交响乐杰作”——书中的每一个人物灵魂，皆作为一个拥有完全独立自主意志与形而上学自省意识的平等对话主体巍然耸立！"},
                {"en": "Julia Kristeva's formulation of intertextuality established that every text represents a dynamic absorption and transformation of a vast mosaic of pre-existing texts.", "cn": "茱莉亚·克里斯蒂娃惊艳创立的“互文性（Intertextuality）”前沿文学哲学范式庄严确立：天地间任何一部看似孤立横空出世的文本杰作，在微观肌理最深处，自始至终皆是一场对过往人类漫长文明史中数以万计既有先验文本与符号碎片的大规模吸收、重组、移置与再创造马赛克璀璨拼图！"},
                {"en": "Jacques Derrida's deconstructive strategy deployed 'différance' to expose how meaning in linguistic sign systems is perpetually deferred along an endless chain of signifiers.", "cn": "雅克·德里达那柄令整个西方形而上学哲学大厦闻风丧胆的解构主义绝世神兵，巧妙凭借造词法铸就了兼具“空间差异”与“时间延宕”双重玄机的“延异（Différance）”核心概念利刃，无情曝光了语言符号世界深处的赤裸真相——词语所指的绝对绝对终极真理，永远在无穷无尽的能指长链跳跃游移中被永久延宕、永不可及！"},
                {"en": "The carnivalesque in medieval folk culture provided an ephemeral yet radical realm where ecclesiastical hierarchies and feudal boundaries were playfully inverted.", "cn": "深植于欧洲中世纪与文艺复兴民间土壤中的“狂欢化（Carnivalesque）”民间狂欢节文化精神，破天荒开辟了一方虽短暂却极具颠覆颠覆力量的神圣狂欢自由乐土——在这里，教廷权威的森严规训与封建贵族的森严阶级门第，在民间泼辣的笑声、颠倒的王冠与泥泞的戏谑中被彻底颠覆解构！"},
                {"en": "Hermeneutic circle dynamics demonstrate that understanding the meaning of a textual part requires reference to the whole, which itself is known through parts.", "cn": "博大精深的伽达默尔“解释学诠释学循环（Hermeneutic Circle）”哲学动力学深刻揭示：一个人若试图彻底读懂并领悟文本中某一个微观词句的幽微深意，必须时刻参照把握整部巨著宏观的总体思想宏旨；然而唯独通过对每一个微观局部的抽丝剥茧深读，宏观总体的宏伟面目方能在我们心头破晓显现！"},
                {"en": "Reader-response theory shifted the locus of literary art from the static printed page toward the active psychological performance enacted by the reader.", "cn": "接受美学与读者反应批评理论的大胆破局，破天荒把文学审美艺术的真正发生神圣发生地，从冰冷印着铅字的白纸黑字静态书页之上，毅然决然大跨越转移到了广大读者在翻阅沉思中用自身心智血肉去积极参与破译再创造的鲜活心理剧场舞台！"},
                {"en": "Literature does not provide passive moral prescriptions; it constructs complex linguistic crucibles wherein contradictory human truths collide in beauty.", "cn": "人类真正伟大的传世传世经典文学，从来绝非是为了向世人廉价兜售几条道貌岸然的道德劝诫小药丸；它乃是人类凭借语言文字的无双造化，在天地之间所亲手构筑起的一座座神圣壮美的复杂审美大熔炉——正是在这里，那些在现实中不可调和的人性悖论、血泪挣扎与深沉大爱，在震撼心灵的艺术大美中璀璨相撞！"},
                {"en": "The concept of negative capability celebrates a poet's supreme capacity to dwell in uncertainties, mysteries, and doubts without irritable grasping after certainty.", "cn": "约翰·济慈名留青史的“消极感受力（Negative Capability）”美学至高境界，由衷礼赞一个真正伟大诗人的最高风骨——那就是能够气定神闲、从容安详地长年栖居于扑朔迷离的未解之谜、不确定性与巨大疑云深处，而绝不心急气躁、廉价仓促地去向世俗乞求任何教条确凿的冰冷现成答案！"},
                {"en": "Structuralist narratology identifies underlying actantial models and narrative grammars that govern mythological tales across diverse geographic continents.", "cn": "结构主义叙事学以严谨的解剖刀功力，在横跨五洲四海不同文明民间神话的千姿百态表象之下，精准提炼打捞出了统御人类叙事底层的深层行动元模型与不变的叙事普遍语法。"},
                {"en": "Subaltern literary studies amplify the muted testimonies of colonized subjects whose historical agony was sanitized within imperial archives.", "cn": "底层文学批评与后殖民批评利刃，以深情的大爱笔触，强有力向世界扩音放大了那些被殖民帝国官方档案文书曾精心洗白粉饰抹杀的数以千万计被压迫被剥削劳苦大众的泣血证词！"},
                {"en": "Poetry is the supreme alchemy of human speech, transmuting the base metal of mundane experience into the shimmering gold of ontological wonder.", "cn": "传世诗歌从来都是人类语言艺术的至高点金术——正是在那诗行平仄韵律的玄妙化境深处，凡尘俗世中最平平无奇、粗粝琐碎的苦难经验，被奇迹般彻底点化熔铸升华为了闪烁着存在论神圣惊奇之光的璀璨黄金！"},
                {"en": "In reading true literary genius, we do not escape our mortal world, but return to it with eyes cleansed of dust, able to love it more deeply.", "cn": "在深读古往今来那些旷世文学巨匠的手笔之时，我们从来绝非是在懦弱逃避现实红尘；而是带着一双被艺术之泉彻底荡涤洗净了尘埃的澄澈眼眸重新深情回归人世间，以比以往任何时刻都更加赤诚、更加慈悲的姿态，去深爱我们脚下这个不完美却壮丽无比的苦难人间！"}
            ]
        },
        {
            "title": "Unit 7 · 逻辑学中的归谬批判、形式谬误与非形式论证重构",
            "description": "探讨演绎三段论有效性、归谬法反证逻辑、假两难推理与稻草人谬误解构长难句。",
            "sentences": [
                {"en": "Reductio ad absurdum demonstrates the falsity of an opponent's initial premise by rigorously proving that its logical consequences terminate in contradiction.", "cn": "在古希腊逻辑辩驳术中享有崇高威名的“归谬法（Reductio Ad Absurdum）”，通过顺水推舟、严丝合缝地沿着对手所自诩正确的初始前提进行数理推演，以无可辩驳的形式逻辑铁证证明其最终必将不可避免地撞车推导出一组自相矛盾、荒谬绝伦的结论，从而在源头上彻底宣告其前提的破产死刑！"},
                {"en": "Deductive syllogistic validity guarantees that if premises are true, the conclusion follows with apodictic necessity independent of personal beliefs.", "cn": "严谨的古典三段论演绎逻辑的“形式有效性（Validity）”，以近乎冷酷的数学必然性向世人庄严保证：只要大前提与小前提在现实中铁证如山为真，那么其所推导出的终极结论便以绝对必然性自然成立，绝不以世间任何人的主观信仰或偏见好恶为转移！"},
                {"en": "The straw man fallacy misrepresents an interlocutor's nuanced position into an oversimplified caricature to engineer an easy, deceptive refutation.", "cn": "辩论场上极其卑劣下流的“稻草人谬误（Straw Man Fallacy）”，特指辩手在理屈词穷之时故意闭眼不看对方真实缜密的高维立论细节，而是无耻地将对方的观点蓄意歪曲、矮化、极端化成一个千疮百孔的弱智假靶子，而后当着全场观众的面得意洋洋地乱棍将其打翻！"},
                {"en": "The fallacy of affirming the consequent commits an elementary logical blunder by presuming that because the conditional outcome occurred, the antecedent was realized.", "cn": "形式逻辑初学者极易踩坑的“肯定后件谬误（Affirming the Consequent）”，极其愚蠢地犯下了因果倒置的逻辑大忌——荒谬地自以为仅仅因为“如果P那么Q”中的Q在现实中已然发生，便武断铁嘴断言推导出前面的P必定已经在历史中必然发生！"},
                {"en": "False dilemma tactics manipulate audiences by presenting complex multi-factorial issues as binary zero-sum choices while concealing moderate alternatives.", "cn": "令人防不胜防的“假两难推理陷阱（False Dilemma）”，通过在话语修辞中极其险恶地将错综复杂、充满丰富中间地带谱系的复杂社会命题，粗暴极端化阉割为“非黑即白、非此即彼”的二选一零和绝境，以此刻意遮蔽并扼杀一切理性温和的中庸破局可行性方案！"},
                {"en": "The slippery slope argument asserts without empirical justification that taking a modest initial step will trigger a catastrophic avalanche of horrific consequences.", "cn": "臭名昭著的“滑坡谬误（Slippery Slope）”，在毫无起码实证证据链条支撑的前提下，凭借耸人听闻的恐吓话术，疯狂恐吓受众盲信：只要在当下迈出了微不足道的第一步微小改革试验，就必然会像多米诺骨牌雪崩般一路刹不住车滑向万劫不复的末日绝境深渊！"},
                {"en": "Ad hominem abusive attacks bypass analytical engagement with arguments entirely, resorting to slanderous character assassinations targeting proponents.", "cn": "在学术讨论与公共理性论辩中被正人君子所深恶痛绝的“人身攻击谬误（Ad Hominem）”，在面对对方无可辩驳的钢铁论据面前彻底丧失了正面交锋的勇气，转而恼羞成怒下作地诉诸人身毁谤、大搞诛心之论与人格抹黑！"},
                {"en": "Begging the question, or petitio principii, constructs a circular argument where the controversial conclusion is smuggled into premises.", "cn": "经典的“乞题谬误与循环论证（Begging the Question）”，在论证结构深处玩弄着拙劣的偷梁换柱把戏——极其隐秘狡黠地将那条本身尚在风口浪尖亟待严格证明的争议结论，早已神不知鬼不觉暗度陈仓偷渡包装进了其所谓的前提论据之中，自说自话自证其罪！"},
                {"en": "Post hoc ergo propter hoc fallacies confuse mere temporal succession with causal necessity, attributing causality to unrelated preceding events.", "cn": "在民间迷信中大行其道的“后此即因此谬误（Post Hoc Ergo Propter Hoc）”，粗暴弱智地将事物在时间先后顺序上的偶发相继发生，天真盲信等同于两者之间必然存在着铁律般的因果物理纽带——公鸡打鸣在太阳破晓之前，并不等于太阳是被公鸡啼叫所召唤唤醒的！"},
                {"en": "Soundness in deductive reasoning demands both formal validity of structural inferences and unshakeable empirical truth of constituent premises.", "cn": "在严谨分析哲学与数理逻辑殿堂中，“论证的可靠性（Soundness）”树立了无可争议的最高黄金金标准——它庄严要求一个无懈可击的完美推论，不仅必须在形式推理的骨架结构上做到天衣无缝、绝无漏洞，更必须在其每一个前置大前提小前提上，做到经得起铁证如山实证检验的绝对真理！"},
                {"en": "The genetic fallacy mistakenly judges the epistemic validity of a proposition based solely upon its historical origins rather than inherent merit.", "cn": "“发生学谬误（Genetic Fallacy）”荒谬地以某个思想学说最初发源诞生的历史污点或卑微草莽渊源，便盲目一棍子将其在当下所蕴藏的内在真理光芒全盘抹杀否定。"},
                {"en": "Equivocation fallacies exploit lexical ambiguities by surreptitiously shifting the semantic definition of a key term mid-argument.", "cn": "在辩论中玩弄“偷换概念歧义谬误（Equivocation）”的无良辩手，在论证推进的中途神不知鬼不觉悄悄篡改偷换了核心关键词的内在定义内涵，以此制造出水落石出的虚妄胜利假象。"},
                {"en": "Appeals to ignorance presume that a hypothesis is true simply because it has not yet been conclusively disproven by science.", "cn": "臭名昭著的“诉诸无知谬误（Appeal to Ignorance）”，荒唐无知地断言：某一个荒诞不经的怪力乱神命题只要尚未在眼下被当代科学在实验中斩钉截铁彻底反驳证实为伪，就必须被全社会全盘接纳为真理！"},
                {"en": "Rigorous logical analysis acts as a cognitive antiseptic, cleansing human discourse of rhetorical deceits and demagogic manipulation.", "cn": "严谨无情的现代形式逻辑与批判性审辨分析工具，充当着现代文明社会的崇高“认知强效消毒剂”——它能以秋风扫落叶之势，无情荡涤荡清人类公共政治讨论空间中的一切修辞欺诈、诡辩陷阱与狂热煽动！"},
                {"en": "Let your mind be a temple of reason and your speech a beacon of clarity; for in the light of truth alone can human spirit stand free.", "cn": "且让你的心智化作一座纯净神圣的理性圣殿、让你的言论化作一道划破长夜迷雾的澄澈明灯吧——因为唯有在毫无矫饰的客观真理与严密逻辑光芒照耀之下，人类的灵魂方能真正昂首傲立于天地之间、拥抱绝对自由！"}
            ]
        },
        {
            "title": "Unit 8 · 现代社会学中的异化危机、科层制铁笼与反思性现代性",
            "description": "探讨韦伯科斯制合理化铁笼、吉登斯风险社会、鲍曼流动的现代性与哈贝马斯交往行为长难句。",
            "sentences": [
                {"en": "Max Weber's sociological diagnosis warned that relentless instrumental rationalization would trap modern humanity within an 'iron cage' of bureaucratic disenchantment.", "cn": "现代社会学开山鼻祖马克斯·韦伯以近乎先知般的沉痛声音向全人类敲响警钟：以功利算计为导向的工具理性（Instrumental Rationality）在现代社会的狂飙突进，终将以冷酷的科层制流水线规训，将现代人类的灵魂死死锁死在一个丧失了诗意神性与终极价值的“理性铁笼（Iron Cage）”深处！"},
                {"en": "Bureaucratic institutions prioritize formal procedural efficiency and depersonalized record-keeping, reducing living human subjects into fungible case files.", "cn": "现代大型科层制官僚行政机器与跨国托拉斯，将形式主义流程效率与去人格化冷血档案核算推向至高王座，极其残忍地将每一个有血有肉有尊严的鲜活求助市民，无情矮化折叠为一串串冰冷代码与可随意替换的冰冷业务编号！"},
                {"en": "Zygmunt Bauman's concept of 'liquid modernity' illuminates how solid, permanent social bonds and lifelong institutional commitments have dissolved into fleeting relationships.", "cn": "当代社会学泰斗齐格蒙·鲍曼名垂青史的“流动现代性（Liquid Modernity）”理论深刻洞察指出：昔日坚若磐石、历久弥新的传统家庭邻里社会共同体纽带与终身职业承诺，在今天已被资本流动大潮彻底液化解构溶蚀为了一段段转瞬即逝、用完即弃的脆弱快餐式人际弱连接！"},
                {"en": "Ulrich Beck's risk society framework demonstrates that late-modern industrial civilizations manufacture apocalyptic technological and ecological hazards that evade territorial borders.", "cn": "乌尔里希·贝克振聋发聩的“风险社会（Risk Society）”学说以铁一般的事实向全人类敲响警报：进入后工业时代的现代文明，正在其科技狂飙突进的大后方自发批量制造着动辄席卷全球、彻底击穿任何主权国家地理疆界防线的核辐射、基因变异与全球气候大雪崩等灭顶系统性灾难！"},
                {"en": "Jürgen Habermas championed communicative action theory, proposing that democratic societies must insulate civic life-worlds from being colonized by market money and administrative power.", "cn": "当代哲人尤尔根·哈贝马斯以宏大的学术手笔创立了“交往行为理论”，大声疾呼现代法治民主文明社会必须构筑起绝对铜墙铁壁般的制度防火墙，坚决誓死守卫属于平凡百姓日常生活的“交往生活世界”，坚决防止其遭受商业资本金钱逻辑与行政官僚强权的野蛮殖民吞噬！"},
                {"en": "The commodification of emotional labor compels service professionals to fake synthetic smiles, creating painful psychological dissonance between authentic feelings and workplace performances.", "cn": "现代服务业与数字化职场对“情绪劳动（Emotional Labor）”的大规模资本商品化异化，残酷逼迫数以亿计的基层一线工人在打卡上岗那一秒起必须机械伪造出标准职业微笑，在灵魂最深处诱发了真实自我情感同虚伪职业表演之间撕心裂肺的慢性认知失调剧痛！"},
                {"en": "Michel Foucault's panoptic discipline models explain how modern disciplinary architectures enforce self-surveillance across citizens who internalize the invisible gaze of authority.", "cn": "米歇尔·福柯那令人毛骨悚然的“全景敞视建筑规训模型（Panopticism）”深刻揭秘了现代社会统治权力的高阶神技：通过在空间与网络中布设无处不在的隐形审视眼睛，迫使每一个置身其中的个体在潜意识深处将公权力的威慑目光内化为严苛的自我审查，心甘情愿沦为自我监禁的囚徒！"},
                {"en": "Anthony Giddens characterized reflexive modernity as a runaway juggernaut where continuous institutional self-monitoring generates unpredictable, uncontainable manufactured risks.", "cn": "安东尼·吉登斯将我们身处其中的反思性晚期现代性生动隐喻为一辆失控狂奔的“诸神战车（Juggernaut）”——全社会对自身运行数据的全天候反思监控与动态微操，反倒以令人窒息的态势在系统深处源源不断催生出更多超脱于人类控制治理能力之外的人造失控巨大风险！"},
                {"en": "Individualization sociological processes liberate subjects from traditional community taboos only to abandon them to navigate systemic structural risks in complete isolation.", "cn": "现代社会狂飙突进的“个体化大浪潮”，虽然表面上将每一个现代人从传统封建宗族清规戒律的枷锁中彻底赎身解放出来；然而其最为残忍的阴暗面，却恰恰在于把每一个单打独斗、赤身裸体的原子化个体，彻底抛弃流放在狂风暴雨的系统性失业、破产与疾病风险之中任由其自生自灭！"},
                {"en": "Sociology awakens humankind from naturalized delusions, revealing that oppressive institutional arrangements are human creations that can be remade through collective solidarity.", "cn": "现代批判社会学以最清醒的启蒙之光驱散照亮了人类心智中的宿命论幻觉，以事实昭告天下：世间一切看似天经地义、森严压迫的制度机器与社会不公架构，归根结底统统是由人类历史自身所亲手缔造的人造物；这也意味着——全人类只要手挽着手紧密团结在一起，便绝对拥有彻底砸碎并亲手重塑一个崭新美好世界的无上伟力！"},
                {"en": "The erosion of social capital chronicled by Robert Putnam illustrates how privatized digital domestic lives dissolve voluntary civic association fabrics.", "cn": "罗伯特·帕特南在名著《独自打保龄》中令人心碎地记录了现代“社会资本”的断崖式大坍塌——高度私密化的数字娱乐彻底消解瓦解了维系公民社会自治民主协商的志愿社团基层网络。"},
                {"en": "McDonaldization processes characterized by calculability and predictability homogenize human service cultures into soulless mechanical assembly lines worldwide.", "cn": "席卷全球的“麦当劳化（McDonaldization）”商业模式凭借可量化计算性与绝对可预测性，极其冷酷地将千姿百态的人类在地文化温情服务，粗暴整齐划一打磨成了毫无灵魂的人间流水线！"},
                {"en": "Reflexive historical sociology challenges teleological developmentalism, proving that modernization paths outside the West cultivate distinctive indigenous modernities.", "cn": "具有深邃批判自省意识的现代历史社会学断然打破了西方中心主义的线性目的论现代化神话，以铁一般的事实证明：广大非西方古老文明完全有底气探索走出独具自身灿烂文明风骨的中国式现代化新路径！"},
                {"en": "A society that measures civilizational worth purely by economic growth rates while ignoring loneliness is a wealthy desert starving for meaning.", "cn": "一个仅仅把冷冰冰的GDP经济增长率当作衡量文明成色唯一刻度、却对千千万万公民灵魂深处的极度孤独苦难视若无睹的社会，本质上不过是一座金玉其外败絮其中、在精神旷野深处饥渴死去的流沙荒漠！"},
                {"en": "Let collective human solidarity break the cold bars of the iron cage; reconstruct modern life into an inclusive garden of dignity and communion.", "cn": "且让我们以全人类休戚与共的崇高钢铁团结大爱，去亲手劈碎那座冰冷窒息的理性铁笼囚牢吧——在废墟之上，深情将现代人世间重新构筑重绘为一方人人享有尊严、四海皆兄弟的美丽温暖锦绣伊甸园！"}
            ]
        },
        {
            "title": "Unit 9 · 伦理学中的道德实在论、反实在论与道德相对主义反思",
            "description": "探讨摩尔非自然主义直觉论、麦凯错误论道德虚无、康德绝对命令与品德伦理学长难句。",
            "sentences": [
                {"en": "Moral realism posits that objective moral facts exist independently of subjective human beliefs, cultural conventions, or evolutionary psychology adaptations.", "cn": "元伦理学殿堂中的“道德实在论（Moral Realism）”坚定捍卫指出：客观的善恶是非道德事实，在宇宙本体论深处如万有引力定律一般确凿存在，自始至终超然独立于任何人类个体的主观私欲信念、特定部落的文化民俗，乃至生物进化心理学的实用主义偏好！"},
                {"en": "G.E. Moore's open question argument sought to demonstrate that defining the ethical concept 'good' through natural properties like pleasure commits a naturalistic fallacy.", "cn": "乔治·爱德华·摩尔以划时代的“开放性问题论证（Open Question Argument）”向伦理学界庄严宣告：任何企图将“善（Goodness）”这一至高无上、不可拆解的纯粹概念，功利化等同还原为“令人愉悦或有利于生存”等自然物理特性的鲁莽尝试，皆不可饶恕地触犯了严重的“自然主义谬误（Naturalistic Fallacy）”！"},
                {"en": "J.L. Mackie's iconoclastic error theory argued that moral claims systematically aim at objective truth, but because objective moral values are metaphysically queer, all are false.", "cn": "J.L.麦凯在《伦理学：发明对与错》中抛出石破天惊的“道德错误论（Error Theory）”冷酷论证道：人类语言中的一切道德善恶断言在句法上固然都在煞有介事地追求某种客观真理，然而因为所谓“客观道德属性”在物理宇宙中乃是一种荒诞不经的怪力乱神形而上学古怪之物（Argument from Queerness），因此世间一切道德断言在严格逻辑上统统皆是全盘虚妄的弥天大谎！"},
                {"en": "Moral relativism contends that ethical validity is strictly contingent upon localized cultural consensus, precluding external trans-cultural normative criticism.", "cn": "大行其道的“文化相对主义（Moral Relativism）”伦理学思潮断言：任何道德是非善恶标准的合法性，百分之百死死受制于特定地域部族内部的文化约定俗成；这一论调在客观上以险恶姿态，在法理上彻底封杀剥夺了全人类跨越文化边界去谴责纳粹屠杀或残害女性等滔天反人类暴行的道德正义资格！"},
                {"en": "Immanuel Kant's categorical imperative demands that agents act only according to maxims that could be willed simultaneously as universal laws binding all rational beings.", "cn": "伊曼努尔·康德名垂青史的“绝对命令（Categorical Imperative）”庄严号令每一个觉醒的理性个体：在尘世间行事做人立言立行，必须且唯独遵循这样一条崇高行动准则——那就是你当下的行动律令，必须同时能够经受住被你心甘情愿确立为全天下所有理性存在者皆必须普遍遵行的一体无差别的永恒普遍法则！"},
                {"en": "Deontological frameworks strictly prohibit treating persons merely as instrumental means, commanding absolute reverence for human dignity as an end in itself.", "cn": "康德主义义务论伦理学框架以铁血般的崇高神圣法则厉声禁绝世间一切将他人仅仅当作实现自身私利功利手段的卑劣行径，庄严下达最高命令：必须且永远在任何时刻，将每一个有血有肉有灵魂的凡人生命尊严，视作至高无上的绝对目的本身！"},
                {"en": "Aristotelian virtue ethics shifts analytical focus away from rigid rule adherence toward cultivating stable character excellences that achieve eudaimonia.", "cn": "亚里士多德所开创的“德性伦理学（Virtue Ethics）”巍峨范式，果断将伦理学探索的聚光灯从刻板遵守冰冷教条戒律，大刀阔斧转移至在日常柴米油盐岁月中精心雕琢涵养一身沉静笃定的“卓越品格美德”，以求最终加冕人类生命的至臻终极繁盛与极乐（Eudaimonia）！"},
                {"en": "The doctrine of the mean posits that virtue resides within an optimal golden equilibrium situated between the vices of deficiency and excess.", "cn": "西方先哲亚里士多德与东方至圣先师孔子不谋而合的“中庸之道（Doctrine of the Mean）”大智慧深刻指出：真正的至善美德，从来永远安详栖居在克服了“不及”之懦弱与“过犹不及”之鲁莽的至臻黄金平衡点深处——勇敢乃是介于懦弱与莽撞之间的神圣平衡！"},
                {"en": "Emotivism developed by A.J. Ayer reduced moral claims to non-cognitive emotional ejaculations akin to cheering or booing at athletic stadiums.", "cn": "逻辑实证主义旗手艾耶尔那套令人啼笑皆非的“情绪主义伦理学（Emotivism）”，极其荒谬地将人类崇高的善恶道德宣称，彻底贬低阉割为没有任何真假认知内涵的下意识情感呜咽——将“杀人是邪恶的”贬低等同于在足球场上看球时发出一声“嘘——下台！”的无脑倒好喝倒彩！"},
                {"en": "Moral progress across historical epochs—exemplified by the abolition of chattel slavery and female enfranchisement—provides compelling empirical support for moral realism.", "cn": "回望人类数千年波澜壮阔的道德觉醒长河，黑奴奴隶制在全人类范畴内的彻底废除、以及女性平权获得完全公民普选权等惊天动地的历史跨越，以无可辩驳的铁证向世人昭示：人类文明确实存在着清晰可见的“道德大进步轨道”——这正是道德实在论最不可撼动的硬核实证护城河！"},
                {"en": "The problem of moral luck exposes the unsettling reality that our ethical assessments of individuals are heavily contaminated by events outside their control.", "cn": "托马斯·内格尔与伯纳德·威廉斯提出的“道德运气难题（Moral Luck）”，令人不安地揭露了现实司法审判与日常道德评判中令人心惊肉跳的阴暗现实：世人对一个人道德功过是非的盖棺定论，往往在极大程度上被完全游离脱轨于当事人自身主观意志掌控之外的纯粹偶发运气所深度污染操弄！"},
                {"en": "Care ethics pioneered by Carol Gilligan illuminates an alternative moral orientation rooted in relational responsibility, empathy, and contextual responsiveness.", "cn": "由卡罗尔·吉利根所开创的“关怀伦理学（Ethics of Care）”，破天荒为全人类推开了一扇崭新的道德大门——决然打破传统男性视角下冷冰冰的抽象权利正义数学算计，将根系深扎在充满温情脉脉的人际关系连带责任、无私同理心以及对具体困境的深情响应深处！"},
                {"en": "Moral anti-realism risks disarming human rights advocacy against tyranny, leaving dissidents with nothing more than subjective preference against totalitarian violence.", "cn": "道德反实在论一旦滑向不可救药的相对主义泥潭，其最凶险的政治恶果，正在于在残酷专制极权暴政面前将全人类的人权大厦彻底解除武装——逼得那些舍身求法的义士在面对刽子手的屠刀时，手里竟然拿不出任何比“个人主观审美偏好”更硬核的正义武器！"},
                {"en": "Ethics is not an arbitrary cultural fiction fabricated to police the masses, but the sacred compass without which human civilization devours itself.", "cn": "人类崇高的伦理道德与良知公义，从来绝非是什么统治阶级为了驯服百姓而凭空捏造出的虚妄统治话术；它是人类文明在茫茫宇宙长夜中破浪远航最不可或缺的神圣罗盘——一旦亲手将其砸碎丢弃，整个人类文明必将在自私与戾气的厮杀中自相残杀、自我毁灭殆尽！"},
                {"en": "Two things fill my mind with ever-new wonder and awe: the starry heavens above me and the moral law within me.", "cn": "伊曼努尔·康德在《实践理性批判》终局留下了震撼人类心灵数百年、响彻宇宙长空的永恒墓志铭：“这世间唯有两样崇高事物，每当我们以越来越持久与虔诚的心灵去深情仰望思索时，便会愈发让我们的心房充溢着历久弥新、由衷敬畏的至高震撼与崇高战栗——那就是我头顶那片灿若星河的无垠浩瀚星空，与我内心深处那座坚如磐石、永放光芒的庄严道德律令！”"}
            ]
        },
        {
            "title": "Unit 10 · 人类文明终极叩问：技术奇点、费米悖论与大过滤器假说",
            "description": "探讨卡尔达肖夫三级文明假说、冯诺依曼自复制探测器、大过滤器与人类宇宙学责任。",
            "sentences": [
                {"en": "Enrico Fermi's famous paradox encapsulates the chilling cosmic silence: if intelligent extraterrestrial civilizations are theoretically abundant, where is everybody?", "cn": "物理学巨擘恩里科·费米在午餐漫谈中脱口而出的著名“费米悖论（Fermi Paradox）”，以近乎冰冷的口吻道出了浩瀚宇宙令人脊背发凉的死寂长夜：“既然在概率推演上地外智慧生命本该如过江之鲫般繁衍遍布银河，那么——他们所有人究竟究竟都身在何方？！”"},
                {"en": "The Great Filter hypothesis conjectures that an insurmountable evolutionary barrier exists along the path from prebiotic chemistry to interstellar colonization.", "cn": "令天体物理学家心惊肉跳的“大过滤器假说（The Great Filter）”残酷推演断言：在从最原始的无机化学浓汤分子自我演化一路狂飙至跨星际深空殖民文明的漫长征途之上，大自然必然早已在暗中布设下了一道几乎不可逾越、让绝大多数物种粉身碎骨的灭顶“终极死神过滤器”！"},
                {"en": "Nick Bostrom warned that discovering fossilized multicellular life upon Mars would constitute the most terrifying archaeological discovery in human history.", "cn": "牛津大学人类未来研究所哲学家尼克·博斯特罗姆曾发出振聋发聩的惊天警告：一旦人类未来在火星地层深处真正发掘出古老复杂多细胞生物化石，那将毋庸置疑构成人类文明史上最令人头皮发麻、最绝望恐怖的考古大灾难——因为这意味着凶险致命的大过滤器正死死横亘在人类未来的道路前方！"},
                {"en": "Nikolai Kardashev classified hypothetical cosmic civilizations across three tiers based upon the energy harness scale: planetary, stellar, and galactic.", "cn": "苏联天文学家尼古拉·卡尔达肖夫以宏大宇宙视角，根据文明驾驭调度能源的物理能级尺度，将宇宙智慧文明严整划分为三大经典能级台阶：完全掌控本行星全部地表地热能源的I型行星级文明、完全包裹母恒星建造戴森球的II型恒星级文明，直至掌控整个银河系千亿星辰浩瀚能源的III型星系级超级霸主！"},
                {"en": "Von Neumann self-replicating probes exponentially traversing planetary systems could colonize an entire spiral galaxy within mere millions of years.", "cn": "冯·诺依曼数学家构想的“自复制深空星际探测器”大军，凭借其抵达陌生星系便就地采矿三维打印复制两艘新飞船的指数级几何裂变扩张模型，仅仅需要数百万年光阴——在地质时间尺度上不过弹指一挥间——便足以将整个庞大银河系每一个恒星系统尽数殖民插旗！"},
                {"en": "The technological singularity hypothesis predicts that recursive self-improving artificial superintelligence will ignite an explosive intelligence explosion outstripping human comprehension.", "cn": "令无数科学家既热血沸腾又惊恐万状的“技术奇点（Technological Singularity）”假说预言：一旦前沿强人工智能具备了自主改写底层代码算法、实现指数级“递归式自我迭代进化”的能力，一场瞬间将全人类心智理解极限远远甩在尘埃深处的“超级智力大爆炸”必将呼啸降临人间！"},
                {"en": "The simulation hypothesis mathematically explores whether our observed physical universe is an ancestor simulation running on a post-human supercomputer.", "cn": "“虚拟宇宙模拟假说（Simulation Hypothesis）”以冷峻的统计概率数学严密论证推演指出：如果我们未来的后人类文明有朝一日拥有了在超级量子计算机中模拟祖先宇宙的无穷算力，那么在纯概率学维度上，我们眼下自诩身处其中的这个物理现实世界，几乎百分之百不过仅仅是运行在更高阶云端服务器内部的一段微观模拟代码而已！"},
                {"en": "The Drake equation formalizes the probabilistic estimation of active, communicative extraterrestrial civilizations within our Milky Way galaxy.", "cn": "著名的“德雷克方程（Drake Equation）”，通过将恒星形成速率、类地行星比例、生命诞生概率直至文明能够安然度过自我毁灭危机的平均技术寿命等核心参数进行相乘连乘，为人类定量测算银河系中潜在可通信的地外文明总数搭建起了第一座科学数理模型灯塔。"},
                {"en": "Existential risks—threats that imperil the entire future potential of Earth-originating intelligent life—demand unprecedented global risk governance.", "cn": "“人类存在性生存风险（Existential Risks）”——即那些动辄可能在瞬间将源自地球的人类全部智慧生命火种连根拔起彻底抹杀的终极天灾与人造科技浩劫，迫切呼唤全人类各大主权大国必须以大格局彻底打破狭隘地缘政治偏见，携手构筑起全人类命运共同体的最高安全统筹治理防火墙！"},
                {"en": "The cosmic horizon problem in Big Bang cosmology necessitated the development of cosmic inflation theory, explaining the isotropic temperature of deep space.", "cn": "现代宇宙大爆炸标准模型中所不可避免遭遇的“视界难题”，强有力催生了划时代的“宇宙暴胀理论（Cosmic Inflation）”——以时空在奇点破晓后万亿分之一秒内超光速指数级暴胀拉平的惊天创举，完美解密了解释了全天宇宙深空微波背景辐射呈现出近乎绝对各向同性恒温的宇宙之谜！"},
                {"en": "Anthropic cosmological principles remind us that the physical constants of our universe are exquisitely fine-tuned to permit the emergence of conscious observers.", "cn": "博大精深的“人择宇宙学原理（Anthropic Principle）”时刻警醒敲打着人类：我们头顶浩瀚宇宙中那一系列精妙绝伦、稍微挪动小数点后几十位便会导致恒星无法点燃生命无法诞生的“物理基本常数组合”，已然被造物主微操微调至尽善尽美，方才奇迹般恩赐允许了我们这群自觉意识观察者的诞生！"},
                {"en": "The dark forest hypothesis in speculative astro-sociology envisions the cosmos as a predatory wilderness where revealing one's coordinates invites immediate eradication.", "cn": "在当代科幻史诗哲学中震撼全球的“黑暗森林假说”，将整座冰冷浩瀚的宇宙深空冷酷描绘为一座潜伏着无数持枪带弹猎人的死亡丛林——在这里，任何一个天真浪漫向虚空中公开发射广播呼叫自身文明坐标的幼稚文明，皆难逃瞬间引来降维打击彻底被从宇宙抹杀的灭顶浩劫！"},
                {"en": "Humankind carries the solemn ontological responsibility of serving as the conscious custodian of life's flame within a silent cosmos.", "cn": "在这片辽阔无垠、深邃冰冷、万籁俱寂的浩瀚宇宙长夜深处，我们人类作为目前已知唯一的自觉生命奇迹，肩负着至高无上、神圣不可推卸的本体论历史使命——那就是誓死充当好小心翼翼呵护守护大自然这一抹脆弱生命火种的忠贞宇宙守护者！"},
                {"en": "Let us transcend our petty terrestrial quarrels and gaze outward with unified courage; for our ultimate destiny is written across the stars.", "cn": "且让我们彻底跳出并超越世俗凡尘中那些狭隘可笑的地面零和博弈与内耗争吵吧，携起手来，以整个人类物种铜墙铁壁般的团结胆魄张开双臂向着浩瀚深空并肩眺望吧——因为我们全人类文明最波澜壮阔的终极归宿与宿命，正庄严由金色的大字书写刻录在浩瀚银河的璀璨群星之间！"},
                {"en": "Stand firm upon the shores of the cosmic ocean; the voyage of mind has just begun, and the endless light of tomorrow awaits our sails.", "cn": "昂首庄严屹立在浩瀚无边宇宙大洋的金色滩头之上吧；人类自由灵性心智与智慧的伟大远航长征才不过刚刚盛大扬帆起航，那片属于我们明天的无垠灿烂曙光，正深情等候着我们的凯旋风帆破浪向前！"}
            ]
        }
    ]
    courses.append(build_course(gre_meta, gre_chapters))

    return courses

if __name__ == "__main__":
    print("测试考试分类 Part 4 (中考 + GRE)...")
    c = get_exam_part4_courses()
    print(f"成功构建课程数: {len(c)}")
