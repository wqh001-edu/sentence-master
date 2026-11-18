# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))

from builder_core import build_course

def get_textbook_part2_courses():
    courses = []

    # -------------------------------------------------------------------------
    # 3. 新概念英语第三册 (10章)
    # -------------------------------------------------------------------------
    nce3_meta = {
        "id": "course-tb-nce3",
        "title": "《新概念英语第三册》(NCE 3) · 典雅散文与思想深度思辨 (10章全集)",
        "category": "textbook",
        "categoryName": "教材同步",
        "coverGradient": "from-purple-700 via-indigo-800 to-slate-900",
        "icon": "🖋️",
        "description": "英语高阶修辞与思想表达天花板，培养地道英式笔触、精炼散文长难句与深度人文思辨。",
        "difficulty": "中高级 B2",
        "tags": ["新概念三册", "高阶修辞", "典雅散文", "英语思维"]
    }
    nce3_chapters = [
        {
            "title": "第 1 课 · A Puma at Large · 乡村美洲狮出没谜云与山林追踪",
            "description": "伦敦以南乡村频现美洲狮踪迹，专家实地勘查扑朔迷离的野生猛兽悬案。",
            "sentences": [
                {"en": "Pumas are large, cat-like animals which are found in America.", "cn": "美洲狮是一种原产于美洲大陆、体型庞大且具有典型猫科动物特征的凶猛肉食动物。"},
                {"en": "When reports came into London zoo that a wild puma had been spotted forty-five miles south of London, they were not taken seriously.", "cn": "当有紧急目击简报传至伦敦动物园称，有人在伦敦以南四十五英里处的乡间旷野赫然目击到一只野生美洲狮时，起初动物学专家们并未将其当真。"},
                {"en": "However, as the evidence began to accumulate, experts from the Zoo felt obliged to investigate.", "cn": "然而随着来自各方民间无可辩驳的证据开始层层汇聚叠加，动物园的权威资深专家们终于意识到有责任义务亲自奔赴实地展开调查。"},
                {"en": "The description given by people who claimed to have seen the puma were extraordinarily similar.", "cn": "那些言之凿凿宣称亲眼目睹过美洲狮真容的目击乡民所给出的形态特征描述，竟然惊人地高度吻合、别无二致。"},
                {"en": "The hunt for the puma began in a small village where a woman picking blackberries saw a large cat only five yards away.", "cn": "这场声势浩大的山林搜捕大搜寻，最初肇始于一座偏僻幽静的小村落——当时一位正在灌木丛中采摘野黑莓的村妇，赫然发现距离自己仅仅五码之遥的草丛里正潜伏着一头巨大猫科猛兽！"},
                {"en": "The animal immediately ran away when she began screaming hysterically for help.", "cn": "当那名惊恐万分的妇人当场失声发出歇斯底里的救命尖叫呼号时，那只警觉敏捷的动物立刻如闪电般转身窜入密林逃之夭夭。"},
                {"en": "A search was organized by the police, but no trace of the beast was found until paw prints were discovered by a river bank.", "cn": "当地警方随后立即牵头组织开展了地毯式大搜山，然而自始至终未曾发现猛兽半点踪影，直到数日后才在清澈的河岸湿泥中辨认出数枚巨大肉垫爪印。"},
                {"en": "Scientists confirmed that the tracks were undeniably made by a fully grown adult feline of extraordinary stature.", "cn": "动物学科学家们在现场勘查石膏拓印后郑重确认：这些深陷泥淖的清晰脚印，无可争议正是一头体型极为魁梧庞大的成年雄性猫科猛兽所留下的！"},
                {"en": "The mystery of how a solitary exotic predator could survive unnoticed in the English countryside captivated national imagination.", "cn": "一头孤身涉险的异国蛮荒猛兽究竟究竟是如何得以神不知鬼不觉长期潜伏隐匿于英格兰平原丘陵的未解谜云，彻底引爆了全英公众的狂热猜想！"},
                {"en": "Sophisticated complex sentences employing participial clauses and restrictive relatives set the gold standard of literary prose.", "cn": "通篇大量交织采用现在分词短语作状语以及限制性定语从句的高阶典雅长难句架构，树立了现代英文纪实散文写作无可逾越的黄金美学标杆！"},
                {"en": "Farmers reported sleepless nights guarding their sheep pens against the invisible shadow stalking the hedgerows.", "cn": "四周农庄的农场主们纷纷反映，为了死守自家羊圈免遭那道潜伏游弋在茂密树篱灌木阴影深处的无形幽灵猎杀，他们已彻夜荷枪实弹难眠数日。"},
                {"en": "Nature possesses an uncanny capacity to reclaim space right under the nose of industrialized civilization.", "cn": "大自然那野性未驯的神奇力量，总能在大工业文明自以为高枕无忧的眼皮子底下，以令人猝不及防的方式强行夺回属于它自己的领地！"},
                {"en": "The wild creature vanished as mysteriously as it had arrived, leaving behind legends that outlived official reports.", "cn": "那头神出鬼没的蛮荒生灵最终宛如它当初凭空降临那般神秘莫测地人间蒸发了，只在乡野田埂间留下了经久不衰、远比官方调查报告更脍炙人口的传世江湖传奇。"},
                {"en": "Maintain a healthy reverence for the untamable mysteries that lurk beyond the periphery of human comprehension.", "cn": "对于那些潜伏盘踞在人类理性狭隘认知地平线边界之外的不可知荒蛮奥秘，永远当常怀一份由衷的敬畏与谦逊。"},
                {"en": "Precision of vocabulary and nuance of tone elevate journalistic reportage into enduring narrative art.", "cn": "字斟句酌的精辟词汇锻造与拿捏得当的幽微叙事语调，将一篇寻常的田野新闻调查采风，成功升华成了一篇历久弥新的传世叙事散文杰作！"}
            ]
        },
        {
            "title": "第 2 课 · Thirteen Equals One · 教堂古钟深夜十三响与恶作剧",
            "description": "古老教堂塔楼半夜敲响十三声丧钟，神父提灯夜探揭开钟表匠秘密。",
            "sentences": [
                {"en": "Our vicar is always raising money for one cause or another, but he has never managed to get enough money to have the church clock repaired.", "cn": "我们教区的牧师先生整日里总在为了各种各样的慈善名目四处奔走募捐化缘，然而他经年累月却自始至终未能筹集到足够充裕的善款来彻底大修那座古旧的老教堂塔钟。"},
                {"en": "The big clock, which used to strike the hours day and night, had been damaged many years ago and had been silent ever since.", "cn": "那座昔日里曾寒暑不息、昼夜为全镇居民准点鸣响报时的雄伟巨钟，早在许多许多年以前便已身遭重创损毁，自那之后便一直陷入了漫长死寂。"},
                {"en": "One night, however, our vicar woke up with a start: the clock was striking the hours!", "cn": "然而就在某一个万籁俱寂的深夜里，我们那位睡梦中的牧师先生却骤然被惊得浑身猛一激灵惊醒过来：教堂塔楼上的那口大钟，竟然破天荒再次轰鸣敲响了！"},
                {"en": "Looking at his watch, he saw that it was one o'clock, but the bell struck thirteen times before it stopped.", "cn": "他急忙就着烛光低头瞥了一眼自己的怀表，上面赫然显示分明正是深夜一点钟整，然而那口老铜钟却足足狂敲了整整十三记沉重钟鸣才堪堪作罢！"},
                {"en": "Armed with a heavy torch, the vicar went up into the clock tower to see what was going on.", "cn": "心中惊骇疑惑交加的牧师手持一把沉甸甸的强光手电筒，咬紧牙关大步迈上盘旋石阶，深入阴森昏暗的钟楼腹地去一探究竟。"},
                {"en": "In the torchlight, he caught sight of a figure whom he immediately recognized as Bill Wilkins, our local grocer.", "cn": "在手电筒晃动的雪白光柱照射之下，他赫然捕捉到了一道鬼祟忙碌的身影，并一眼当场便认出了对方正是镇上开杂货铺的比尔·威尔金斯！"},
                {"en": "Whatever are you doing up here at this unearthly hour, Bill? asked the vicar in utter astonishment.", "cn": "“你这大半夜半夜三更深更半夜的究竟是在这鬼地方瞎折腾些什么勾当，比尔？”牧师满脸目瞪口呆、惊诧万分地失声质问道。"},
                {"en": "I'm trying to repair this bell, answered Bill; I've been working on it for weeks, and while I was adjusting the striking mechanism, it struck thirteen.", "cn": "“我这不想着替大伙把这口老钟修好嘛，”比尔不好意思地挠头讪讪笑答道，“我瞒着大家在这鼓捣它好几个星期了，刚才在调试敲钟杠杆凸轮连杆机构时，手一滑它就失控连敲了十三下！”"},
                {"en": "Well, said the vicar smilingly, thirteen is one too many, but it's still better than nothing!", "cn": "“哎呀，”牧师闻言不由得忍俊不禁、会心莞尔一笑道，“半夜一点敲上十三下虽然确实显得有些离谱过头，但不管怎么讲，总归总比彻彻底底一声不吭的死寂要强得多啊！”"},
                {"en": "The humorous dialogue illustrates the warm eccentricity and grassroots solidarity of English village life.", "cn": "这番妙趣横生、令人捧腹的机智夜探对话，生动勾勒出了英格兰传统乡村熟人社会那份独具魅力的怪诞人情味与草根守望相助。"},
                {"en": "Mechanical clocks with complex pendulum weights demand delicate kinetic recalibration by skilled horologists.", "cn": "依靠沉重铅坠重锤下坠驱动的古典机械大钟内部复杂的擒纵摆轮齿轮组，向来需要技艺精湛的钟表匠付出极尽幽微的力学动态精细校准。"},
                {"en": "Dramatic irony and temporal markers heighten suspense before resolving into cozy neighborhood camaraderie.", "cn": "戏剧性反差讽刺手法与精准时间推进状语的交相辉映，在悬疑惊悚氛围推至峰巅的刹那，举重若轻地将其消融化作一团温馨怡人的邻里欢笑。"},
                {"en": "Imperfect goodwill offered with humility often achieves more genuine spiritual comfort than flawless professional detachment.", "cn": "以一颗谦卑笨拙的赤诚之心所奉献出的并不完美的小小善意，往往反倒比那些冷冰冰、无可挑剔的专业说教更能抚慰人间的凡尘心灵！"},
                {"en": "The old church tower bell resumed its vigilance, reminding the valley that hope can be resurrected from silence.", "cn": "饱经风霜的古老教堂塔钟终于在沉睡多年后重振雄风恢复了守望，长鸣的钟声在向整座山谷庄严昭示：希望永远能在死寂绝境中破土重生！"},
                {"en": "Rejoice in the well-intentioned endeavors of ordinary citizens who labor selflessly to mend communal heritage.", "cn": "由衷为那些在暗处默默无闻、为了抢救守护公共文化遗产而无私奉献汗水热忱的平凡市井英雄击节欢呼赞叹吧！"}
            ]
        },
        {
            "title": "第 3 课 · An Unknown Goddess · 远古爱琴海女神石雕考古惊世重现",
            "description": "考古学家在爱琴海岛屿发掘三千五百年前米诺斯文明古代女神黏土雕像。",
            "sentences": [
                {"en": "How would you feel if you had to live alone on a small island for months on end?", "cn": "倘若命运迫使你不得不孤身一人长年累月在远离尘嚣的海外孤岛荒原上与世隔绝度日，你的内心究竟会作何感想？"},
                {"en": "In 1960, an American archaeologist, Dr. John Caskey, began excavations on the island of Kea in the Aegean Sea.", "cn": "早在公元1960年，美国著名古典考古学泰斗约翰·卡斯基博士率领科考队，正式在希腊爱琴海深处的基亚岛拉开了大规模考古发掘的宏伟序幕。"},
                {"en": "The island, so small that it is barely visible on maps, turned out to have been an important trade station in antiquity.", "cn": "这座在常规航海地图上渺小到近乎用放大镜都难以辨认的荒凉弹丸小岛，在遥远的上古蛮荒时代，竟然曾是一座沟通地中海各大航线的关键国际贸易枢纽！"},
                {"en": "The team dug down through centuries of debris until they unearthed a magnificent city from the Bronze Age.", "cn": "考古发掘队员们挥镐挥铲层层穿透了厚达数十米、沉淀了数千年岁月沧桑的历史瓦砾断层，直到一座令人叹为观止的青铜时代宏伟城邦废墟重见天日。"},
                {"en": "Inside the ruins of a temple, they made a breathtaking discovery: fragments of life-sized clay statues of women.", "cn": "在一座古老异教神庙的残垣断壁祭坛深处，他们破天荒迎来了一项足以震惊世界考古史的惊天神迹大发现：大量与真人等身大小的古代女性陶土雕像残骸碎片！"},
                {"en": "Carefully assembling the broken pottery shards over months of painstaking labor, they reconstructed an astonishing goddess.", "cn": "在历经长达数月之久披星戴月、屏息凝神的一丝不苟手工拼对拼贴抢救之后，他们终于奇迹般复原出了一尊令人心驰神往的史前上古女神绝美神像！"},
                {"en": "The statue depicted a graceful woman wearing a full, flounced skirt, with her hands resting serenely upon her slender hips.", "cn": "整尊雕像惟妙惟肖生动刻画了一位身姿绰约高贵的绝代佳人——她身着华美繁复的多层荷叶边褶皱宽大拖地长裙，一双温润柔荑从容安详地搭在纤细的腰际两侧。"},
                {"en": "Dating back to the fifteenth century B.C., this clay masterpiece revealed intimate links to the sophisticated Minoan culture of Crete.", "cn": "经放射性碳十四精密测定，这尊问世于公元前十五世纪的陶塑艺术巅峰神作，无可辩驳地揭示出它同古希腊克里特岛米诺斯高度繁盛海洋文明之间血脉相连的深邃渊源！"},
                {"en": "Her enigmatic smile, preserved through three and a half millennia of subterranean silence, seemed to mock the transience of human vanity.", "cn": "她唇角那一抹在暗无天日的地下深处长眠了整整三千五百年依然温润如初的神秘莫测微笑，仿佛在冷眼从容俯瞰嘲弄着人世间一切帝王将相虚幻名利的稍纵即逝。"},
                {"en": "Archaeological excavation serves as humanity's profoundest dialogue across the unfathomable abyss of deep historical time.", "cn": "跨越数千载时光深渊的田野考古发掘发掘，本质上是人类现代心灵同浩瀚不可测的历史深处所展开的一场最庄严崇高的形而上学心灵深度对话。"},
                {"en": "The master ceramicists of the Aegean possessed a technical mastery of clay firing that rivaled Renaissance sculptors.", "cn": "活跃在远古爱琴海诸岛上的史前陶艺巨匠们所掌握的高温泥土陶制烧结锻造绝技，其炉火纯青的造诣，丝毫不逊色于文艺复兴全盛时代的米开朗基罗！"},
                {"en": "Past conditionals and passive transformations intertwine seamlessly to convey scientific authority and historical grandeur.", "cn": "虚拟语气过去条件句与被动语态句型的交相辉映天衣无缝融合，为全篇注入了严谨扎实的科学权威质感与荡气回肠的恢弘历史厚重感！"},
                {"en": "Every shard recovered from the earth whispers forgotten prayers offered by long-extinct civilizations to cosmic deities.", "cn": "从沉睡千年泥土中被小心翼翼唤醒拂去尘埃的每一枚残破陶片，都在向今人幽幽低语着早已灰飞烟灭的远古人类对浩瀚星空宇宙神明的虔诚祈祷祭词。"},
                {"en": "Artifacts of enduring beauty conquer physical decay, ensuring the immortality of ancient artistic souls.", "cn": "真正凝聚了人类永恒精神之美的不朽艺术文物器物，终将彻底战胜物质肉身的一切物理腐朽衰亡，确保古代巨匠的璀璨灵魂万世长存！"},
                {"en": "Gaze upon the reconstructed goddess with reverent awe; in her clay eyes reflects the undying dawn of human culture.", "cn": "怀揣着虔诚战栗的由衷敬畏去瞻仰凝视这尊被复原重生的远古女神吧；在她那一双泥塑眼眸的深邃倒影深处，正普照着整个人类文明黎明初现时不灭的破晓曙光！"}
            ]
        },
        {
            "title": "第 4 课 · The Double Life of Alfred Bloggs · 垃圾工的高贵伪装与体面双重人生",
            "description": "清洁工阿尔弗雷德瞒着妻子每日换西装上班，维持体面高级白领伪装。",
            "sentences": [
                {"en": "These days, people who do manual work often earn more money than clerks who work in offices.", "cn": "时至今日在现代都市职场中，那些凭借一把力气在第一线挥汗如雨从事体力劳作的蓝领工匠，其月薪收入往往远胜过整日端坐在写字楼隔间格子间里的普通白领文员。"},
                {"en": "People who work in offices are frequently referred to as 'white-collar workers' for the simple reason that they usually wear a suit and tie to work.", "cn": "端坐在写字楼办公室里的白领职员之所以常常被大众冠以“白领阶层”的雅号，原因极其单纯直白：仅仅是因为他们平日里上班总是西装革履、打着笔挺领带而已。"},
                {"en": "Such can be the curiosity of the human mind that a great many people would accept less pay for the hollow privilege of wearing nice clothes.", "cn": "然而人类心智深处对于虚荣面子的扭曲执念往往就是这般令人啼笑皆非：竟有数以万计的人宁肯甘愿拿着极其微薄的薪水，也要死死换取那份能够每天穿戴得光鲜亮丽的虚妄体面特权！"},
                {"en": "Alfred Bloggs worked as a dustman for eight long years, yet his wife was convinced he was an important junior executive in a major corporation.", "cn": "阿尔弗雷德·布洛格斯老老实实在市政环卫局干了整整八年苦脏累的掏垃圾清运工人，然而他的结发发妻却自始至终坚信自己的丈夫是一家跨国大财团里的重要中层管理精英！"},
                {"en": "Every morning, he left his home dressed in a smart black suit, carrying a polished leather briefcase.", "cn": "每天清晨在离家出门上班时，他总是打扮得整整齐齐，身穿一套笔挺考究的纯黑西装，手中威严拎着一只打磨光亮的真皮公文皮包。"},
                {"en": "Upon arriving at the city depot, he immediately changed into greasy overalls and spent his day collecting domestic rubbish from back alleys.", "cn": "然而只要前脚一迈进市政清洁工车队的中转站车库大门，他便会以闪电般速度换上一身油渍斑斑的粗布工装连体裤，随后开着垃圾车在城里阴暗逼仄的后街窄巷深处风吹日晒掏掏了一整天的臭烘烘生活垃圾。"},
                {"en": "Before heading home at five o'clock, he took a shower, slipped back into his suit, and returned to his wife as an exhausted executive.", "cn": "而在下午五点整准时收工回家之前，他必定会在公共浴室痛痛快快洗个滚烫的热水澡，重新体面换上那身帅气西装，随后以一副刚在董事会开完烧脑高阶会议的身心俱疲高级白领姿态昂首阔步踏入家门。"},
                {"en": "He kept this elaborate deception up for nearly a decade, earning superior wages while preserving the fragile vanity of his domestic peace.", "cn": "他凭借着这套煞费苦心、天衣无缝的伪装戏码，在长达近十年的风雨岁月中既赚取到了令人艳羡的丰厚高额薪金报酬，又在妻子面前保全了维系家庭平静所必需的脆弱虚荣体面。"},
                {"en": "The social stigma historically attached to manual sanitation labor reveals the deeply hypocritical prejudices of modern snobbery.", "cn": "长期以来世俗偏见强加在城市环卫市政基础体力劳动者头上的无形社会阶层歧视烙印，极其深刻无情地揭露暴露出了现代人虚荣势利眼目光的极度伪善与荒唐！"},
                {"en": "Syntactic parallel structures contrasting manual earning power with white-collar pretense drive the biting social satire.", "cn": "通篇将蓝领真金白银的真实购买力同白领死要面子活受罪的做作做派形成鲜明工整对照的排比句型，赋予了整篇讽刺杂文入木三分的辛辣批判锋芒！"},
                {"en": "Honest labor in the service of public hygiene deserves identical societal respect as financial ledger calculation.", "cn": "为了维护整座大都市千万人公共卫生洁净而默默躬身劳作的每一份诚实汗水，在社会地位的人格尊严天平上，理应享有同坐在空调房里算计金融财务账本完全对等的神圣尊重！"},
                {"en": "The polished briefcase containing only an apple, sandwiches, and a clean towel epitomized the tragicomic absurdity of class anxiety.", "cn": "那只在人前被擦拭得锃亮的高级真皮公文包内部，私底下实际不过仅仅装着一只红富士苹果、两片自制三明治与一条干毛巾——这一细节，极其传神地将阶层焦虑的黑色滑稽荒诞推向了极致！"},
                {"en": "True self-worth is measured by the integrity of your character and the diligence of your hands, not the cut of your cloth.", "cn": "一个男子汉顶天立地真正的自我无上价值，唯有用你骨子里的正直人品与双手的勤勉坚韧来客观度量，而绝非仅仅取决于你身上那袭西装剪裁面料的贵贱！"},
                {"en": "Shed the paralyzing terror of what the neighbors might think; authentic living begins where superficial posturing terminates.", "cn": "彻底打碎抛弃那种整日唯恐隔壁邻居说三道四看不起你的窒息恐惧心魔吧；当你敢于彻底终结一切虚浮表演伪装的那一刻起，真实洒脱的人生方才宣告真正启航！"},
                {"en": "All work that elevates human dignity and sanitizes communal life is fundamentally noble and worthy of unreserved pride.", "cn": "凡是能够滋养升华人类尊严体面、洁净庇护公共社会家园的一切诚实汗水劳动，在本质上皆是至高无上、值得全人类毫无保留由衷自豪骄傲的伟大壮举！"}
            ]
        },
        {
            "title": "第 5 课 · The Facts · 荒岛遇难漂流与绝境生还的真理纪实",
            "description": "加勒比海客轮海难沉没，几名幸存者荒岛求生写就荒野奇迹。",
            "sentences": [
                {"en": "Editors of newspapers and magazines often go to great lengths to ensure their articles are factually accurate.", "cn": "各大主流报纸与权威学术刊物的主编总编们，往往在幕后甘愿付出常人难以想象的巨大艰辛努力，以誓死确保自己刊印发行的每一篇报道在客观事实上都做到绝对严谨精准、万无一失。"},
                {"en": "They employ large teams of researchers to verify names, dates, and historical details before publishing any human interest story.", "cn": "在向全社会公开发表任何一篇扣人心弦的传奇人物纪实特写之前，他们必定会不惜重金组建庞大的事实核查团队，对文中的每一个姓名、年份日期与历史细节展开地毯式倒查考证。"},
                {"en": "A dramatic case occurred when an ocean liner struck a submerged coral reef in the Caribbean and went down rapidly.", "cn": "当年曾发生过这样一桩惊心动魄的真实海难：一艘跨国豪华远洋客轮在加勒比海深邃水域不幸触礁，撞上了暗藏海面之下的凶险珊瑚暗礁，并在极短时间内迅速倾覆沉没海底！"},
                {"en": "For days, the world feared that all passengers had drowned in the stormy shark-infested waters.", "cn": "在随后的漫长煎熬数日里，全世界各国民众的心统统提到了嗓子眼，万分揪心深怕所有落水受难船员乘客早已在这片暴风狂澜席卷、鲨鱼疯狂出没的死神水域中全军覆没溺亡殆尽。"},
                {"en": "Then came the sensational telegram: four survivors had washed ashore on a deserted, uncharted volcanic atoll.", "cn": "然而就在千钧一发之际，前方搜救前线突然发回了一封惊天动地的绝密加急电报：有整整四名命悬一线的奇迹幸存者，成功被海浪冲刷推送到了附近一座荒无人烟、航海图上甚至未曾标注的火山珊瑚环礁之上！"},
                {"en": "The shipwreck survivors sustained life by collecting rainwater in turtle shells and foraging for coconuts.", "cn": "这几位历劫余生的海难幸存勇士们，凭借着令人惊叹的生存本能，用就地搜集来的巨大海龟龟壳收集天降甘霖雨水解渴，并在密林中艰难攀爬采摘野生成熟椰子充饥度日。"},
                {"en": "When a passing cargo vessel finally spotted their smoke signals, the survivors were rushed to a medical facility in Kingston.", "cn": "当一艘偶然途经涉事海域的远洋跨国货轮终于敏锐捕捉到他们在孤岛峭壁之巅点燃的求救滚滚狼烟信号时，这几位脱险的英雄被以最高级别紧急专机一路护送疾驰送往金斯敦市的顶尖医疗中心实施抢救。"},
                {"en": "Journalists swarmed the harbor, but rigorous editors refused to print rumors until every detail of survival was cross-examined.", "cn": "来自全球各大媒体机构的无冕之王记者们如潮水般疯狂涌向港口码头抢夺头条，然而那些坚守职业操守底线的严谨主编们，却铁面无私坚决拒绝刊发任何道听途说的江湖传闻，硬生生顶住流量压力，直到幸存者所口述的每一个求生细节都被交叉互证核实得严丝合缝！"},
                {"en": "The discipline of rigorous factual verification distinguishes responsible journalism from sensationalist modern misinformation.", "cn": "对客观物理事实进行掘地三尺严丝合缝的一丝不苟核查求证自律纪律，乃是衡量负责任崇高严肃新闻媒体同当今那些捕风捉影、毫无底线的眼球经济网络黄色假新闻之间最根本的道德天堑分野！"},
                {"en": "Complex passive reportage patterns like 'it was reported that' and 'are said to have been' dominate factual prose.", "cn": "诸如'it was reported that'以及'are said to have been'等大量高规格的间接引述被动语态严谨句型，在全篇为新闻纪实文学注入了无懈可击的客观公信力与庄重法理质感！"},
                {"en": "Human adaptability in the face of sudden elemental catastrophe proves the indomitable resilience of our species.", "cn": "人类在直面天地自然狂暴灾变惊涛骇浪生死关头时所瞬间迸发出的超凡敏捷适应自救潜能，铁证如山地雄辩证明了我们这一生物物种百折不挠的坚不可摧生命韧性！"},
                {"en": "Truth does not demand theatrical embellishment; unadorned reality possesses its own supreme narrative gravity.", "cn": "铁一般的铁血客观事实真相，从来根本不需要任何画蛇添足的煽情戏剧化添油加醋夸张修饰；洗尽铅华的赤裸真实本身，便自拥有一种能够震慑全人类灵魂的最至高无上叙事万有引力！"},
                {"en": "The shipwrecked castaways survived through mutual cooperation, sharing every precious drop of moisture equally.", "cn": "几位落难孤岛的受难者之所以能够奇迹般战胜死神携手生还，全赖他们在绝境中建立起的绝对无私互助信任同盟——甘苦与共、将每一滴维系生机的珍贵淡水甘泉分秒不差公平分配给身畔的同胞手足！"},
                {"en": "Commit your intellect to the relentless pursuit of verifiable facts in an era saturated with seductive illusions.", "cn": "在这一个被各色巧言令色、充满诱惑的信息茧房与虚假幻象所彻底泛滥淹没的信息爆炸数字时代，请务必让你的理智头脑永远坚定不移献身于对真理实证真相的不懈求索！"},
                {"en": "Stand firmly upon verified ground; for truth alone withstands the turbulent erosion of speculative opinion.", "cn": "把你的双足深扎在经得起千锤百炼客观实证考验的坚实大地基石之上吧；因为放眼寰宇唯有颠扑不破的真理，方能真正抵御消融时代一切流言蜚语主观臆断的汹涌侵蚀！"}
            ]
        },
        {
            "title": "第 6 课 · Smash-and-Grab · 珠宝橱窗飞车抢劫与闹市惊天追捕",
            "description": "劫匪驱车强撞闹市高级珠宝店橱窗，抢劫名钻后在闹市上演生死追车狂飙。",
            "sentences": [
                {"en": "The smash-and-grab raid is very common in big industrialized cities across the western world.", "cn": "利用重型坚固车辆强行野蛮冲撞撞碎沿街商铺巨幅橱窗、在数秒内席卷名贵货品的“飞车撞窗抢劫狂潮”，在西方世界各大现代化工业大都市里曾一度屡见不鲜、极为猖獗。"},
                {"en": "It is not performed by sophisticated safe-breakers who pick intricate combination locks in darkness.", "cn": "策划实施这类恶性暴恐罪案的亡命徒，向来根本绝非那些自命不凡、擅长在幽暗午夜凭借听诊器细细破解精密机械密码锁的所谓“飞天神偷雅贼”。"},
                {"en": "Instead, it is executed by reckless gangs who rely entirely on violent momentum and blinding speed.", "cn": "恰恰相反，它完全是由一帮丧心病狂的亡命暴徒团伙凭借着泰山压顶般的狂暴物理冲击动能与闪电般令人窒息的作案速度，所实施的一场极其野蛮粗暴的狂暴洗劫！"},
                {"en": "A large stolen car is driven headlong into the reinforced plate glass window of an elite jewelry shop.", "cn": "一辆预先经过特殊钢板非法改装加固的大马力被盗重型豪华轿车，在众目睽睽之下加足马力，宛如脱轨列车般悍然一头正面暴烈撞向顶级高端珠宝店那扇价值昂贵的钢化防弹巨幅橱窗玻璃！"},
                {"en": "Within thirty seconds, masked perpetrators scoop trays of diamonds into canvas sacks before escaping.", "cn": "在短短不到三十秒钟的电光火石之间，数名头戴黑色头套面具的武装劫匪如饿狼扑食般将装满夺目钻石名表的展示托盘疯狂扫入粗帆布麻袋，随后跳上接应车辆扬长而去！"},
                {"en": "An infamous raid occurred in the West End when an iron-nosed saloon shattered a boutique frontage at noon.", "cn": "当年在伦敦西区繁华商业腹地曾上演过一桩震惊全球的惊天大劫案：正值正午十二点熙熙攘攘车水马龙之际，一辆车头焊接了重型铁轨防撞梁的装甲轿车悍然将一家百年名表定制珠宝行的整面沿街门脸撞得轰然粉碎！"},
                {"en": "The gang tossed dense smoke canisters into the arcade to disorient pursuing pedestrians and security guards.", "cn": "行凶得手的暴徒团伙随手向繁华步行街回廊深处疯狂抛掷出多枚军用级浓烟发烟催泪弹，以此制造遮天蔽日的视线迷雾，极大扰乱拖延了身后奋起直追的见义勇为路人市民与全副武装的商场安保警卫！"},
                {"en": "Metropolitan police squad cars gave chase immediately, their sirens wailing through congested thoroughfares.", "cn": "伦敦大都会警察局数辆大排量特勤巡逻拦截警车在接到无声警报的那一秒便全油门呼啸杀出，凄厉尖锐的刺耳警笛警报声瞬间响彻回荡在整条拥堵不堪的繁华主干道上空！"},
                {"en": "The psychological terror inflicted by public daylight robbery undermines the fundamental social contract of security.", "cn": "在光天化日之下公然持械实施闹市抢劫所制造释放的巨大公众心理恐慌阴影，在根本上严重撕裂践踏了维系现代法治社会正常运转不可或缺的基本安全契约基石！"},
                {"en": "Vivid action verbs such as 'shatter', 'smash', 'scoop', and 'swerve' inject relentless cinematic velocity into the narrative.", "cn": "诸如'shatter'（轰然粉碎）、'smash'（暴烈撞击）、'scoop'（疯狂席卷扫荡）以及'swerve'（极限漂移变向）等极富视觉张力的大量高质动词排山倒海般涌现，为整篇叙事注入了令人血脉偾张、窒息停摆的顶级电影好莱坞大片速度感！"},
                {"en": "Modern structural architects now reinforce luxury retail facades with anti-ram ballistic bollards embedded deep in concrete.", "cn": "现代商业建筑结构工程师如今全面吸取惨痛教训，在各大奢侈品旗舰店沿街橱窗外缘深处数十米地下浇筑嵌入了能够正面拦截数十吨重卡全力撞击的军工级防爆液压升降立柱！"},
                {"en": "No amount of stolen material wealth can ever purchase insulation from the relentless machinery of justice.", "cn": "无论通过丧心病狂的不义掠夺巧取豪夺到多么堆积如山的物质财富，在法网恢恢的铁血国家刑侦机器面前，也生生世世绝无法为你买下一丝一毫能够逃避正义严惩的避罪天堂！"},
                {"en": "The getaway vehicle was ultimately trapped in an alley, its occupants surrounded by armed tactical units.", "cn": "那辆一路横冲直撞亡命狂飙的逃窜匪车最终在一条被重重焊死的死胡同深处被逼入绝境熄火抛锚，车内所有负隅顽抗的凶残劫匪在不到三秒钟内便被荷枪实弹的王牌特警突击战术小队团团包围生擒活捉！"},
                {"en": "Violent shortcuts to prosperity inevitably terminate in catastrophic incarceration or violent destruction.", "cn": "企图依靠丧尽天良的暴力犯罪捷径去攫取人间荣华富贵的荒谬妄想，其最终宿命结局无可逃遁地唯独只有两条：要么在暗无天日的阴森铁窗下抱恨终天，要么在穷途末路的毁灭火光中化作齑粉！"},
                {"en": "True wealth is built upon lawful creation and ethical contribution, never upon the violent dispossession of others.", "cn": "放眼寰宇人类文明史上一切名垂青史的崇高财富传奇，从来全都是堂堂正正建立在遵纪守法的诚实创造与对人类社会的道德积极贡献基石之上，而决绝不可能是靠烧杀抢掠践踏他人骨血所能筑就！"}
            ]
        },
        {
            "title": "第 7 课 · Mutilated Ladies · 损毁纸币兑换局与残钞拼接艺术",
            "description": "英格兰银行设立专门微缩拼接实验室，为百姓全额抢救兑换残损纸币。",
            "sentences": [
                {"en": "Has it ever happened to you that you tore a banknote by accident and wondered if it was still valid?", "cn": "在你的日常生活中是否曾不幸经历过这般窝心事：一不小心失手将一张大面额钞票生生撕扯成了两半，随后整日里提心吊胆惶惑不安地琢磨它究竟是否依然还能照常合法流通使用？"},
                {"en": "In Britain, all damaged banknotes are eventually sent to a special department of the Bank of England.", "cn": "在整个大不列颠联合王国内部，一切在民间流通过程中遭遇不幸意外损毁残破的面额纸币，最终都会被集中送往位于伦敦英格兰银行总部内设的一个极为机密神圣的特殊鉴识部门。"},
                {"en": "This extraordinary team of experts is colloquially known as the 'Mutilated Banknote Division'.", "cn": "这一支由多位全球顶级鉴识科学专家泰斗级大师组成的奇特精英团队，在英格兰民间老百姓口中被亲切诙谐地赞誉为“残损钞票拯救局”。"},
                {"en": "Every year, they examine hundreds of thousands of banknotes that have been chewed by dogs, burned in ovens, or washed in laundry machines.", "cn": "在每一年周而复始的光阴岁月里，这群大师们需要借助高倍显微镜过目鉴识成千上万张惨遭家养恶犬撕咬咀嚼得稀烂、在烤箱烘焙中被严重炭化焦黑、抑或被糊涂马虎的主人不慎塞进滚筒洗衣机洗成一团烂纸浆的各色残破纸币！"},
                {"en": "Provided that at least half of a banknote can be reconstructed, the Bank of England will generously pay out its full face value.", "cn": "只要送来鉴识的受损钞票残片能够被大师们精准拼对还原出哪怕略微超过一半（即法定基准百分之五十一）的原始物理版面面积，英格兰银行便将毫不犹豫、极其慷慨地当场按照票面足额真金白银全额予以全额刚性兑付！"},
                {"en": "One memorable claim involved an elderly lady who had hidden her life savings of five hundred pounds inside an electric fire.", "cn": "在浩如烟海的历史索赔理赔卷宗中曾记录下这样一桩令人啼笑皆非又心酸动容的真实案例：一位独居孤寡老太太，处心积虑将自己省吃俭用积攒了一辈子、整整五百英镑的养老保命积蓄，偷偷藏匿塞进了一台老式电烤炉取暖器的金属夹层深处！"},
                {"en": "Her daughter, unaware of the treasure, switched the appliance on during a bitter winter chill, turning the banknotes into charcoal ashes.", "cn": "数月后老人的亲闺女登门探望，在对取暖器内暗藏万贯家财毫不知情的前提下，顺手随手按下了电热丝开关以抵御刺骨寒冬，结果在短短数分钟内便将老母亲这五百张崭新纸币统统烤焦碳化成了一堆酥脆易碎的黑炭残渣！"},
                {"en": "Forensic experts spent three weeks using micro-tweezers and specialized chemicals to identify the serial numbers, restoring the grandmother's fortune.", "cn": "鉴识局的国宝级痕迹修复大师们整整连续奋战了三周光阴，凭借着高倍医用显微镊子与独家特种化学还原试剂，在炭化废墟中一毫米一毫米奇迹般辨认拼对出了每一张钞票的核心防伪流水暗码，最终分文不差将老人的一生积蓄完好无损全额如数奉还！"},
                {"en": "A nation's sovereign currency represents an inviolable legal contract of trust between the state and the common citizen.", "cn": "一个主权国家的法定货币契约信用，代表着国家最高政权同最平凡普通平民苍生之间所缔结下的神圣不可侵犯、坚如磐石的法理信任契约红线！"},
                {"en": "Conditionals and modal auxiliary verbs like 'provided that' and 'can be' frame the legal parameters of monetary restitution.", "cn": "诸如'provided that'（在……前提条件下）以及情态动词'can be'（能够被……）等极具法学严密思辨性的语法结构，精准构筑确立了国家货币法定刚性兑付的法理边界！"},
                {"en": "Patience and meticulous scientific dedication restore hope to impoverished citizens facing financial devastation.", "cn": "在显微镜前甘坐冷板凳、日复一日的一丝不苟科学专注奉献，能在寻常百姓遭遇灭顶之灾经济创伤的心碎深渊面前，为他们亲手重新托举点亮重获新生的温暖希望之火！"},
                {"en": "Paper fibers embedded with cotton and linen withstand physical torture far better than synthetic substitutes.", "cn": "深层融入了高纯度天然长绒棉与纯亚麻优质韧性植物纤维的传统高档印钞专属纸张，其抗物理撕扯揉搓与化学耐受力，远远超出那些廉价脆弱的纯化学合成塑料替代品！"},
                {"en": "Behind the formidable stone facade of the central bank beat hearts genuinely devoted to public service.", "cn": "在中央国家银行那巍峨森严、看似冷冰冰的坚厚花岗岩罗马柱石墙立面深处，实则终日有力跳动着一群全心全意甘为孺子牛、俯首深情服务普罗大众的温暖赤诚真心！"},
                {"en": "Handle currency with practical care, but know that institutional integrity stands ready to catch you if honest misfortune strikes.", "cn": "在日常起居中虽当细心爱惜保管法定货币纸钞，但更请在心底永远牢记：一旦天有不测风云诚实的不幸灾祸猝不及防降临之际，国家法治信用的巍峨臂膀，必定时刻严阵以待为你遮风挡雨兜底承托！"},
                {"en": "Trust is the supreme currency of any civilization; honor it meticulously in both small coins and grand treaties.", "cn": "彼此之间毫不动摇的崇高信任，永远是屹立在整个人类文明殿堂之巅的最珍贵无上硬通货；不论是面对区区一枚铜板硬币的兑换，亦或面对一纸关乎天下苍生福祉的千秋盟约，都当以战战兢兢的虔诚态度万世恪守！"}
            ]
        },
        {
            "title": "第 8 课 · A Famous Monastery · 圣伯纳德修道院名犬雪山搜救传奇",
            "description": "阿尔卑斯山脉圣伯纳德山口修道院修道士与名犬守望雪山雪崩搜救。",
            "sentences": [
                {"en": "The Great St Bernard Pass connects Switzerland to Italy through the formidable peaks of the Alps.", "cn": "举世闻名的大圣伯纳德山口，横跨阿尔卑斯山脉那雄浑巍峨、常年积雪封冻的万丈崇山险峰，自古便是扼守连通瑞士同意大利半岛的咽喉战略大动脉要道。"},
                {"en": "At eight thousand feet above sea level, it lies buried under deep drifts of snow for nearly eight months of the year.", "cn": "这座海拔高达惊人的整整八千英尺（两千四百余米）之巅的极寒雪山口，在一整年中几乎长达八个月的漫长极昼严冬里，全都被死死深埋在数米深的恐怖雪崩流沙暴风雪积雪之下。"},
                {"en": "In the eleventh century, St Bernard of Menthon founded an Augustinian hospice to shelter weary pilgrims traversing the dangerous route.", "cn": "早在遥远的公元十一世纪盛期，天主教圣徒门通的圣伯纳德毅然在此创建了一座奥古斯丁修道院收容所，誓死为翻越这座鬼门关的千千万万疲惫落难朝圣信徒提供一处温暖的避风神圣庇护所。"},
                {"en": "For centuries, the dedicated monks, accompanied by specially bred large mastiffs, have patrolled the treacherous passes during blizzards.", "cn": "在漫长近千年的沧桑岁月长河中，那些看破红尘将生死置之度外的虔诚修道士们，日夜牵引着体型魁梧、嗅觉逆天的特种大型圣伯纳德搜救名犬，在零下数十度的狂暴白毛风暴雪绝境中巡山踏勘搜救！"},
                {"en": "These legendary dogs possess an extraordinary olfactory ability to locate human beings buried beneath thirty feet of compacted avalanche ice.", "cn": "这些名垂青史的神犬体内蕴藏着一种令现代科学都叹为观止的超凡嗅觉导航天赋——它们竟然能够精准定位嗅出被深埋压死在厚达整整三十英尺冰冷绝望雪崩冰层下的人类微弱呼吸热气！"},
                {"en": "Equipped with small casks of restorative brandy strapped around their collars, the dogs would dig out victims and keep them warm.", "cn": "那些忠勇双全的名犬脖圈颈项上常年牢牢佩挂着装满救命回阳白兰地烈酒的小木桶，在嗅出遇难者后奋力用前爪掘开冰窟，用自己滚烫硕大的厚重毛皮肉身死死覆在冻僵旅人胸膛上以体温为对方续命！"},
                {"en": "If a traveler was too injured to walk, one dog would race back through howling winds to summon the brothers of the monastery.", "cn": "倘若遭遇摔断筋骨、重伤垂危无法自主爬行站立的遇难旅人，其中一只机敏忠诚的神犬便会以命相搏破雪狂奔返回修道院狂吠示警，引得全体手持担架木铲的修道士兄弟们火速破雪出征实施接力救援！"},
                {"en": "The most famous dog, Barry, saved forty human lives during his heroic twelve-year service before dying peacefully of old age.", "cn": "在所有名垂青史的搜救犬中战功最显赫显赫的当属传奇神犬“巴里”——在它长达十二年披肝沥胆的英雄服役生涯中，竟然破天荒亲爪从死神指缝里硬生生抢回了整整四十条鲜活的人类同胞性命！"},
                {"en": "The partnership between selfless human compassion and canine loyalty reaches its sublime spiritual zenith high upon the Alpine summits.", "cn": "人类舍己为人、大爱无疆的人道主义崇高慈悲，同忠犬至死不渝的忠贞纯粹灵性天性，在这阿尔卑斯山之巅冰天雪地的绝境炼狱之中，达成了震烁古今的人神共泣崇高精神峰巅！"},
                {"en": "Participle phrases modifying subject actions and descriptive geographical compound adjectives create a solemn, epic cadence.", "cn": "修饰主语行动的分词短语与大量极具地理空间穿透力的复合形容词纵横交织，为整篇史诗传记注入了如同管风琴长鸣般肃穆庄严的史诗崇高韵律！"},
                {"en": "Modern motorized snowmobiles and search helicopters have now replaced the canine sentinels, but the legend of St Bernard dogs remains immortal.", "cn": "尽管在科技高度发达的当今时代，动力强劲的极地履带式雪地摩托与全天候热成像搜救直升机早已全面接替了昔日犬巡的肉身哨兵使命，然而圣伯纳德神犬的旷世救难神话却早已万古长青！"},
                {"en": "In the freezing altitudes where nature demonstrates its most indifferent cruelty, human brotherhood shines with its warmest fire.", "cn": "恰恰正是在大自然毫无顾忌地宣泄展现其最冷酷无情、冰冷嗜血杀戮严寒的万仞雪山绝顶之巅，人类守望相助的手足骨肉温存大爱，方才绽放出了凡尘间最璀璨夺目、最暖人心房的不灭篝火！"},
                {"en": "Barry's preserved body rests honored in the Natural History Museum of Bern, celebrated forever as the guardian angel of the pass.", "cn": "英雄神犬巴里的尊贵遗骸如今被怀揣最高敬意精心制作成标本，永久供奉安息在伯尔尼自然历史博物馆的荣耀殿堂深处，作为全人类永远顶礼膜拜的雪山守护加护天使名垂青史！"},
                {"en": "When storms of adversity threaten to freeze your faith in human goodness, remember the silent monks and faithful hounds of the Alps.", "cn": "每当现实命运的残酷暴风雪企图彻底冰封扼杀你对人性真善美的笃定信念时，请务必在心底深情重温忆起那些曾在阿尔卑斯绝顶冰雪中默默守望的修道士与忠犬吧！"},
                {"en": "True sanctity requires no gilded palace; it is found shivering upon the snowy ridge, digging with bare hands to save a stranger.", "cn": "至高无上的神圣圣洁从来绝不需要在金碧辉煌的深宫大殿中粉墨登场；它真切示现在寒风呼啸的雪山之巅，那一双双在刺骨严寒中冻得皮开肉绽、却拼死赤手空拳在冰窟中刨挖抢救陌路同胞的血肉之躯掌心之中！"}
            ]
        },
        {
            "title": "第 9 课 · Flying Cats · 摩天大楼猫咪坠落奇迹与高空物理学",
            "description": "纽约兽医研究猫从高空坠落惊人奇迹，揭示猫科动物终极降落伞效应。",
            "sentences": [
                {"en": "Cats have always possessed a legendary reputation for surviving perilous falls that would prove fatal to humans.", "cn": "自远古时代起家猫生灵便在人类民间神话中坐拥着“九命不死”的赫赫传奇威名——它们总能从那些足以令人类粉身碎骨的万丈高空绝险坠落中奇迹般死里逃生、毫发无损。"},
                {"en": "In the urban jungle of New York City, high-rise apartment living has provided veterinary scientists with an unprecedented laboratory.", "cn": "在摩天大楼林立如林的现代大都会纽约水泥丛林深处，高层超高层公寓住宅普及的独特居住形态，却在无意间为现代兽医病理学科学家们提供了一个史无前例的天然高空物理生物学试验场。"},
                {"en": "Dr. Wayne Whitney and Dr. Cheryl Mehlhaff conducted an exhaustive survey of one hundred and thirty-two feline high-rise falls.", "cn": "韦恩·惠特尼博士与谢丽尔·梅尔哈夫博士联手针对大都会地区总计发生过的一百三十二起家猫从高楼窗台失足坠落的真实临床医疗病历，展开了一场掘地三尺的详实统计大调研。"},
                {"en": "Most of the falls occurred when cats, distracted by passing pigeons or insects, lost their precarious footing on narrow window ledges.", "cn": "绝大多数惨烈的高空坠楼惨剧，全都是因为好奇心过盛的猫咪被窗外展翅掠过的鸽子或飞虫过度吸引分神，在光滑逼仄的窗台外沿边缘不慎失足滑脱所致。"},
                {"en": "The survey revealed an astonishing statistical paradox: cats falling from between two and six floors suffered significantly worse injuries than those falling from higher floors.", "cn": "这场详尽的医学统计调研赫然揭示出了一个颠覆凡俗人类物理常识的惊天大悖论：从二层至六层中低楼层失足跌落的猫咪所遭受的骨折创伤程度，竟然显著严重恶劣于那些从七层乃至三十层以上高耸入云超高空坠落的猫咪！"},
                {"en": "Incredibly, one resilient cat fell thirty-two stories onto concrete pavement and survived with only a chipped tooth and a collapsed lung.", "cn": "在所有惊世骇俗的临床纪录中最令人不可思议的一例是：一只意志极其坚韧顽强的家猫不幸从整整三十二层摩天大厦之巅直线下坠，以泰山压顶之势狠狠砸在坚硬冰冷的水泥人行道上，然而它最终竟然奇迹般生还，浑身上下仅仅只磕裂了一颗乳牙并伴有轻微肺萎缩！"},
                {"en": "The explanation lies in biomechanical aerodynamics: after falling a certain distance, cats reach their terminal velocity of sixty miles per hour.", "cn": "这一看似违背天理的超自然奇迹，其真正的科学真相深植于生物力学与流体空气动力学的精妙机理：在自由落体加速下坠达到一定距离阈值后，猫咪在空气阻力平衡下将达到其终极匀速速度——约合每小时六十英里（九十六公里）。"},
                {"en": "At that critical juncture, the cat stops accelerating, relaxes its muscles, spreads its limbs outward like a parachute, and absorbs impact evenly across its torso.", "cn": "正是在这一命悬一线的决定性物理拐点时刻，彻底丧失加速度超重恐慌的猫咪反而奇迹般彻底放松了周身紧绷的肌肉骨骼神经，将四肢如降落伞伞盖般向外呈大字型优雅延展铺展，从而将最终触地时的巨大冲击力以最大受力面积极其均匀平摊地卸卸载到了全身体干肌肉群之上！"},
                {"en": "Nature's ingenious anatomical design transforms an apex hunter into an aerodynamic parachutist capable of miraculous survival.", "cn": "造物主大自然巧夺天工的绝妙解剖学生理构架设计，在生死存亡的眨眼之间，轻而易举将一个地面的捕食杀手瞬间华丽蜕变成了一名能够创造高空物理缓冲奇迹的超凡翼装飞行跳伞家！"},
                {"en": "The use of statistical precision, physiological cause-and-effect clauses, and engaging scientific exposition creates an educational masterpiece.", "cn": "严谨精确的统计学实证数据分析、逻辑缜密的生理学生物物理因果论证从句与引人入胜的科普散文叙事笔触融会贯通，共同构筑了一篇不可多得的传世科普文学殿堂级标杆！"},
                {"en": "Panic stiffens human musculature into brittle vulnerability, whereas feline biological intuition surrenders fluidly to the physics of falling.", "cn": "发自本能的盲目惊恐往往会将人类的肉身骨骼肌肉僵化硬化成极度脆弱易碎的受害受击体，而猫科生灵那铭刻在基因深处的古老生物学智慧本能，却懂得如流水般顺水推舟、从容顺应臣服于高空自由落体的空气动力学客观规律！"},
                {"en": "Installing durable safety netting on high-rise balconies remains an essential ethical duty for every loving urban pet guardian.", "cn": "在享受超高层摩天公寓绝美高空视野的同时，在窗台阳台全面安装牢固耐用的防坠安全防护网，永远是每一位真正心怀大爱、有担当的合格都市铲屎官不可推卸的根本道德责任底线！"},
                {"en": "Even nine legendary lives must not be recklessly gambled against the unforgiving laws of gravitational acceleration.", "cn": "纵然造化神迹赋予了猫科生灵堪称拥有九条命的超凡生存韧性，但在残酷冷峻、从不讲任何情面的万有引力万物物理铁律面前，也千千万万万不可被拿来肆意挥霍当儿戏博弈！"},
                {"en": "Learn from the falling cat the wisdom of serene relaxation: when downward momentum is inevitable, spread your spirit wide to absorb the shock.", "cn": "让我们从这群从天而降的空中飞猫身上汲取一份大智若愚的心灵从容释怀智慧吧：当命运不可阻挡的下坠逆境狂澜无可逃避之际，坦然展开你精神的羽翼与胸襟吧，以最大的从容去从容化解卸去人世一切冲击波创伤！"},
                {"en": "In the grand laboratory of biological evolution, the most modest domestic creatures conceal wonders that continue to humble modern science.", "cn": "在生命漫长数十亿年繁衍演化的浩瀚宏伟生物学试验殿堂深处，哪怕最不起眼、蜷缩在壁炉前打着呼噜的平凡家养生灵体内，亦潜藏着足以让当代现代科学永远为之由衷折服叹服的至高生命奇迹瑰宝！"}
            ]
        },
        {
            "title": "第 10 课 · The Press · 新闻媒体新闻自由与公众知情权博弈",
            "description": "探讨报刊媒体监督公权力、挖掘真相与维系民主现代社会不可或缺的第四权力。",
            "sentences": [
                {"en": "In democratic societies, the press is frequently acknowledged as the indispensable 'Fourth Estate' of constitutional government.", "cn": "在现代文明民主宪政社会形态构架中，享有独立采写特权的新闻媒体舆论报刊界，常年被举世公认为同立法、行政与司法三权并驾齐驱、不可或缺的神圣“第四权力”独立支柱。"},
                {"en": "Newspapers possess the awesome democratic capacity to inform millions of citizens simultaneously on critical matters of public interest.", "cn": "现代报刊新闻传媒坐拥着一种令人生畏的强大民主凝聚伟力——能够在同一时空维度内，分秒不差将关乎国家前途命运与公众切身福祉的重大公共议题头条真相，精准普及传递给数以千万计的主权公民。"},
                {"en": "Investigative journalists often spend grueling months uncovering corporate corruption and holding powerful political leaders accountable.", "cn": "那些甘愿冒着生命危险深入虎穴的真正严肃调查记者们，往往在幕后默默付出数月乃至数年披肝沥胆的艰辛暗访取证努力，誓死挖出跨国财阀内部的腐败黑幕勾当，并义无反顾将位高权重的政坛巨鳄牢牢钉在公众道德问责的审判席上！"},
                {"en": "Without a free and courageous press, abuses of executive authority would remain shrouded in impenetrable official secrecy.", "cn": "倘若彻底丧失了一支享有充分言论自由、铁骨铮铮毫不畏惧权势的新闻记者队伍，公权力野蛮肆虐的滥用与官商勾结的阴暗内幕，必将被永远密不透风地深锁幽禁在官僚体制那冰冷森严的绝密黑幕深渊之中！"},
                {"en": "However, the immense commercial power of the press carries with it dangerous temptations toward sensationalism and intrusion into private lives.", "cn": "然而水能载舟亦能覆舟，现代大众传媒在商业资本裹挟下所展现出的巨大垄断统治伟力，在其硬币的另一面，却也无情滋生出了为了疯狂收割眼球流量而走向毫无道德底线的恶俗炒作造谣与对公民私人私密空间的残暴粗暴践踏！"},
                {"en": "Paparazzi employing intrusive telephoto lenses demonstrate how journalistic liberty can degenerate into predatory voyeurism.", "cn": "那些手持重型长焦大炮镜头、如无头苍蝇般无孔不入疯狂跟拍偷拍的恶劣狗仔队行径，极其生动露骨地向全人类昭示了：当原本神圣高尚的新闻采写自由一旦走向道德失控堕落异化，将会以何等丑陋的面孔沦为一场嗜血残暴的变态窥淫狂欢！"},
                {"en": "The ongoing ethical tension between the public's right to know and the individual's right to privacy demands rigorous judicial vigilance.", "cn": "在公众合理行使获悉公共事务真相的“知情权”，同每一个公民个体神圣不可侵犯的“隐私权与人格尊严”之间所长久横亘爆发的剧烈伦理张力博弈，向来需要整个国家法治司法体系打起十二分精神进行毫不松懈的严密平衡与裁决守护！"},
                {"en": "Newspaper editors bear a grave moral responsibility to distinguish between genuine public interest and prurient public curiosity.", "cn": "手握版面审定生杀大权的主流报刊总编主编们，在良心深处肩负着极其沉重严肃的历史道德责任底线——必须以大无畏的职业定力，精准辨析划清“关乎苍生福祉的公共利益大义”同“庸俗看客猎奇窥私的低级窥探趣味”之间的楚河汉界！"},
                {"en": "The transition from mechanical printing presses to digital algorithmic feeds has fundamentally disrupted the traditional editorial gatekeeping process.", "cn": "从古登堡金属活字凸版印刷机时代跨步飞跃至由人工智能算法推荐信息流主导的现代自媒体数字信息纪元，这一颠覆性的技术巨变在根本上彻底打破解构了解构了传统严肃编辑部把关人的权威过滤门槛！"},
                {"en": "Disinformation spreads six times faster than verified truth across algorithmic social media platforms.", "cn": "经过全球顶级智库实证大数据严密测算显示：那些蓄意炮制捏造、专门迎合挑动大众非理性情绪的劣质虚假谣言信息在社交算法平台上的裂变扩散传播速度，竟然令人发指地达到了被权威事实核查澄清后的客观真实真理的整整六倍之巨！"},
                {"en": "Literary devices balancing balanced conditional assertions and contrasting concessive clauses demonstrate the nuanced intellectual maturity of this text.", "cn": "通篇游刃有余运用工整平衡的条件论述假定从句与逻辑严密的让步转折从句（although, whereas, nonetheless），将这篇政论文思想交锋的深邃成熟思辨风骨展现得淋漓尽致、无可挑剔！"},
                {"en": "Cultivating discerning media literacy has become the supreme democratic prerequisite for every autonomous modern citizen.", "cn": "在这一个被各色信息垃圾与精心编织的认知作战舆论陷阱所包围的现代大变局时代，用心培养出一双能够穿透迷雾辨析真伪的火眼金睛“媒介素养认知鉴别力”，已然成为了每一个独立自由现代主权公民立身处世的最根本民主前提基石！"},
                {"en": "A vibrant democracy does not demand uniform consensus; it requires a cacophony of diverse viewpoints grounded in verified facts.", "cn": "一个真正充满勃勃生机、百花齐放的健全成熟民主宪政机体，从来绝不强求整齐划一、千人一面的机械思想共识；它真正渴求的，是一座百家争鸣、大鸣大放，但其基石始终坚如磐石深扎在铁证如山客观事实之中的广阔公共论辩精神原野！"},
                {"en": "Protect the independence of principled journalists who risk their safety to deliver truth to the public square.", "cn": "像守护眼睛一样去深情呵护捍卫那些不惜赌上个人身家性命与职业前途、冒死深入一线为全天下黎民百姓带回客观事实真相的有良知的新闻工作者们的独立人格与职业尊严吧！"},
                {"en": "For darkness and tyranny flourish only in the silent suffocating void where the beacon of a free press has been snuffed out.", "cn": "因为古往今来人类文明沧桑史早已无数次给出了血淋淋的深刻警示：幽暗的专制暴虐与万劫不复的深渊，永远唯独只会在那一汪连自由新闻与批判良知的长明灯塔都被彻底野蛮掐灭扑灭的死寂窒息虚空中疯狂滋生蔓延！"}
            ]
        }
    ]
    courses.append(build_course(nce3_meta, nce3_chapters))

    return courses

if __name__ == "__main__":
    print("Testing part 2...")
    c = get_textbook_part2_courses()
    print("Part 2 courses:", len(c))
