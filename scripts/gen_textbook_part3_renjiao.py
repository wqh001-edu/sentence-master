# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))

from builder_core import build_course

def get_renjiao_courses():
    courses = []

    # -------------------------------------------------------------------------
    # 4. 人教版初中七年级 (10章)
    # -------------------------------------------------------------------------
    rj7_meta = {
        "id": "course-tb-rj7",
        "title": "《人教版初中七年级英语》(Grade 7) · 阳光校园与青少年成长生活 (10章全集)",
        "category": "textbook",
        "categoryName": "教材同步",
        "coverGradient": "from-emerald-500 via-green-600 to-teal-700",
        "icon": "🎒",
        "description": "义务教育新课标同步，紧扣七年级上下册核心交际，轻松掌握初中英语词汇与句型基石。",
        "difficulty": "初级入门 A1-A2",
        "tags": ["人教七年级", "初中同步", "课标基础", "中考起步"]
    }
    rj7_chapters = [
        {
            "title": "Unit 1 · My name's Gina · 初登初中校园自我介绍与结交新友",
            "description": "迈入初中校门第一天，礼貌自我介绍、询问姓名与互留联系方式。",
            "sentences": [
                {"en": "Good morning! My name's Gina, and it is wonderful to meet you here.", "cn": "早上好！我的名字叫吉娜，今天能在崭新的初中校园与大家相逢结识，我感到非常荣幸与高兴。"},
                {"en": "Hello, I'm Alan; what is your full name and what telephone number do you use?", "cn": "你好，我是艾伦；请问你的全名叫什么，平日里你最常用的联系电话号码又是多少呢？"},
                {"en": "His first name is Jack, but all his close friends call him Jackie for short.", "cn": "他的教名叫杰克，但在日常学习生活中，所有跟他要好的同窗好友都亲切地唤他的小名“杰基”。"},
                {"en": "Her family name is Smith, and she comes from a bustling metropolitan city.", "cn": "她的家族姓氏是史密斯，她本身来自一座充满蓬勃生机、车水马龙的繁华现代化大都会都市。"},
                {"en": "Is that friendly boy sitting in the first row of our classroom your classmate?", "cn": "请问端坐在我们这间明亮教室正数第一排正中央的那位面带灿烂笑容的阳光大男孩，是你的同班同学吗？"},
                {"en": "Yes, he is; we have been inseparable companions since our early elementary school days.", "cn": "是的正是他；早在懵懂无忧的小学求学时代起，我们俩便已然结成了形影不离、无话不谈的挚友莫逆之交。"},
                {"en": "Making new friends with a cheerful smile helps newcomers settle quickly into junior high.", "cn": "用真诚洋溢的温暖笑靥去主动结识新同窗新朋友，能够极大帮助每一位初一新生以最快速度适应融入崭新的初中校园生活。"},
                {"en": "Please write down your contact information clearly on the classroom student directory roster.", "cn": "劳驾请将你本人的准确家庭住址与有效联系电话号码，工工整整誊写登记在咱们班级的通讯录花名册之上。"},
                {"en": "Polite introductions lay the foundation for years of fruitful academic and personal collaboration.", "cn": "落落大方、文明得体的自我引荐与破冰寒暄，为未来数年间同窗同舟共济、互学互鉴的深厚同窗情谊奠定了最坚实的基石。"},
                {"en": "The homeroom teacher welcomed each adolescent with encouraging words and genuine maternal warmth.", "cn": "班主任老师在讲台前以和蔼可亲的鼓励话语与宛如慈母般的真挚温情，逐一满怀欣慰地迎接拥抱着每一位踏入校门的青葱少年。"},
                {"en": "Remember to greet your teachers respectfully whenever you cross paths in the school corridors.", "cn": "在课间楼道走廊与校道上每一次同辛勤育人的师长迎面相逢时，请务必时刻牢记停步恭敬致以诚挚的问候。"},
                {"en": "Exchange notebooks to verify that telephone digits and spelling of names are completely accurate.", "cn": "不妨大方同新同桌交换翻阅一下彼此手头的笔记本，以此仔细核验彼此姓名的英文字母拼写与电话号码位数的准确无误。"},
                {"en": "Junior high school opens an exhilarating new chapter filled with discovery, friendship, and intellectual growth.", "cn": "初中生活的大幕已然盛大拉开，它将为你开启一段写满未知探索、纯真莫逆友谊与智识飞跃蜕变的崭新壮美青春篇章！"},
                {"en": "Approach every stranger as a future friend waiting to share life's adventures with you.", "cn": "怀揣着一腔赤诚将身旁的每一位陌路新同窗，都视作一位即将在漫漫人生求索征程中同你携手并肩、共经风雨的未来挚友吧！"},
                {"en": "A courteous greeting is the golden key that unlocks the door to a harmonious classroom community.", "cn": "一声温文尔雅、礼貌谦和的友善问候，永远是那把能够轻而易举开启通往团结友爱、和谐融洽班级大家庭大门的心灵金钥匙！"}
            ]
        },
        {
            "title": "Unit 2 · This is my sister · 幸福全家福合影与亲人家庭树介绍",
            "description": "展示珍藏家庭全家福，详述三代同堂家庭成员与温馨亲情纽带。",
            "sentences": [
                {"en": "This is a warm family portrait taken during our grandfather's eightieth birthday celebration.", "cn": "这是一张在今年初春我们为慈爱的祖父隆重庆祝八十大寿盛宴期间，全家人其乐融融拍摄下的温馨全家福彩色合影。"},
                {"en": "These are my beloved parents who have supported my academic dreams with tireless devotion.", "cn": "站在正中央的这两位便是我至亲至爱的父母双亲，多年来正是他们二老以无怨无悔的倾情付出，全力托举捍卫着我的求学梦想。"},
                {"en": "That gentle woman holding the baby on the sofa is my aunt Mary, a pediatrician.", "cn": "那位正怀抱着襁褓婴孩、仪态端庄安详端坐在客厅皮质沙发正中央的温婉女性，正是我在市儿童医院当儿科专家的亲姑母玛丽。"},
                {"en": "Those energetic boys playing soccer in the garden background are my mischievous twin cousins.", "cn": "在照片背景后花园草坪上挥汗如雨、不知疲倦飞奔踢着足球的那两名生龙活虎的虎头少年，便是我那对调皮捣蛋的同胞孪生堂弟。"},
                {"en": "Is this elegant young lady standing proudly beside the piano your elder sister, Jenny?", "cn": "请问亭亭玉立、气质超凡脱俗，神采飞扬傲然依偎在那架古典立式黑色钢琴身侧的优雅妙龄女郎，便是你的亲姐姐珍妮吗？"},
                {"en": "No, that is my cousin Kate; she is currently training to become a concert flutist.", "cn": "不，那位其实是我的表姐凯特；她眼下正在国家级音乐学院接受严苛的专业深造，立志日后成长为一名优秀的管弦乐长笛演奏家。"},
                {"en": "Family ties provide an unshakeable anchor throughout the stormy seasons of human existence.", "cn": "无论世事如何风云变幻沧海桑田，血浓于水、休戚与共的家庭亲情纽带，永远是我们漫长人生航程中面对惊涛骇浪时最坚不可摧的避风定海神针。"},
                {"en": "Respecting ancestors and cherishing siblings fosters empathy and deep generational continuity.", "cn": "尊崇孝悌之道、深情关爱同胞手足兄弟姐妹，不仅能滋养出一个人的同理仁爱之心，更能维系维系起生生不息、世代传承的家族崇高精神家风。"},
                {"en": "Our grandparents often gather the grandchildren around the fireplace to narrate inspiring ancestral histories.", "cn": "每逢大雪纷飞的周末阖家团聚时，祖父母总喜欢将承欢膝下的一众孙辈们团团召集在温暖的壁炉篝火四周，向我们深情娓娓讲述先辈们当年的奋斗家史。"},
                {"en": "Demonstrative pronouns like 'this', 'that', 'these', and 'those' clarify spatial and relational proximity.", "cn": "诸如'this'、'that'、'these'以及'those'等基础指示代词的娴熟运用，能够在语言表述中清晰精准地区分物质空间方位的远近与人际血缘亲疏关系。"},
                {"en": "Keep the family photograph safely displayed in a carved wooden frame on the study desk.", "cn": "将这张弥足珍贵的全家福底片精心镶嵌装裱在一只精美的纯木雕花相框内部，长久端正摆放在书房的书桌案头，日夜伴我求索奋进。"},
                {"en": "Express gratitude openly to your parents for the quiet sacrifices they make every single day.", "cn": "请学会大方坦然地向你的父母双亲亲口道一声由衷的感激吧，由衷感恩他们每天在平凡起居柴米油盐之中为你所默默承受做出的无私牺牲与托举。"},
                {"en": "A harmonious domestic household serves as a child's first school of virtue, compassion, and courage.", "cn": "一个和睦融洽、书香四溢、上慈下孝的幸福原生家庭环境，永远是天下每一个懵懂孩童学习知书达礼、锤炼品格与树立无畏勇气的至高人生第一学堂！"},
                {"en": "Cherish every shared meal around the dining table; these ordinary moments become life's most golden treasures.", "cn": "用心去深情珍视每一顿阖家老小团坐围拢在餐桌旁推杯换盏的平淡便饭吧；这每一个看似微不足道的寻常瞬间，日后都必将沉淀为生命中最千金不换的无价黄金记忆！"},
                {"en": "May every family be a blessed haven of unconditional love, laughter, and lifelong mutual support.", "cn": "祈愿天底下千千万万个平凡而伟大的家庭，都能化作一座充盈着无条件大爱、欢声笑语与毕生守望相助的心灵神圣乐土避风港！"}
            ]
        },
        {
            "title": "Unit 3 · Is this your pencil? · 失物招领箱与书包文具归整",
            "description": "寻找遗失铅笔橡皮文具盒，查看失物招领箱与养成物归原位好习惯。",
            "sentences": [
                {"en": "Excuse me, is this yellow wooden pencil with the green eraser tip yours, David?", "cn": "劳驾打扰一下戴维，请问这支尾端嵌有浅绿色橡皮擦头的黄色木质铅笔，是你刚才不慎掉落遗失的吗？"},
                {"en": "No, it isn't mine; my pencil is dark blue and has my initials carved on it.", "cn": "不，那绝不是我的；我平日里惯用的那支自动铅笔通体呈深海湛蓝色，并且笔杆上还特意亲手刻有我本人姓名的英文缩写字样。"},
                {"en": "Whose red dictionary is that lying abandoned under the teacher's wooden podium desk?", "cn": "静静被遗忘遗弃在讲台木质讲桌正下方地板死角处的那本厚重大红色英汉双解词典，究竟是哪位粗心同学的？"},
                {"en": "I think it belongs to Mary; she was searching frantically for it before the English lesson.", "cn": "依我推测那多半应当是属于玛丽同学的私人物件；今天第一节英语大课正式开打上课铃之前，我曾亲眼瞧见她在课桌抽屉里心急如焚地四处翻找它。"},
                {"en": "Let us take all these unclaimed stationery items directly to the lost-and-found notice board.", "cn": "咱们快趁着课间休息把教室里这些暂时无人认领的散落文具零碎，统统统一护送到设在学校门厅正中央的“失物招领公告箱”处妥善保管吧。"},
                {"en": "If you have lost your school ID card or pencil case, please call the school office.", "cn": "各位同窗倘若不慎在校园操场或走廊里遗失了自己的实名制学生校园卡抑或多功能文具盒，请务必第一时间拨打电话联系教务总务处失物招领处前台。"},
                {"en": "Labeling your personal textbooks and school supplies prevents confusing mix-ups in busy classrooms.", "cn": "在新学期开学伊始便在每一本新教科书与每一样随身学习文具显眼处端正贴上姓名专属标签，能有效规避在人多嘈杂的大班级里发生拿错混淆。"},
                {"en": "Possessive pronouns such as 'mine', 'yours', 'hers', and 'theirs' eliminate redundant noun repetition.", "cn": "诸如'mine'、'yours'、'hers'以及'theirs'等名词性物主代词的灵活切换配搭，在语法修辞上彻底杜绝消解了机械单调重复提及名词词组的冗余累赘弊病。"},
                {"en": "A neat pencil box containing sharpened pencils, a sturdy ruler, and a clean eraser inspires focus.", "cn": "一只被收拾打理得井井有条、内整齐码放着削好铅笔、结实透明直尺与干净橡皮的文具盒，总能在无声之中赋予学子全神贯注沉浸学习的强大专注心力场。"},
                {"en": "Returning lost items promptly demonstrates high moral integrity and builds mutual trust among peers.", "cn": "在拾得他人遗失的财物器物后第一时间毫不犹豫物归原主，不仅充分彰显出一个莘莘学子崇高正直的高尚道德情操，更在同窗集体之间筑牢了坚不可摧的信任城墙。"},
                {"en": "The school monitor pinned a detailed lost-and-found bulletin upon the corkboard in the hallway.", "cn": "班长细致地用彩色图钉将一份手写字迹工整的“失物寻物招领启事简报”，牢牢钉在了走廊拐角处的软木宣传栏正中央以广而告之。"},
                {"en": "Cultivate the lifelong habit of organizing your learning tools neatly before retiring for sleep.", "cn": "从小立志用心培养起每逢深夜临睡就寝之前、必先将次日清晨所需的全部书本课业工具分门别类归整收拾妥当的受益终生良好自律习惯吧！"},
                {"en": "Carelessness in small material belongings frequently mirrors an undisciplined mental disposition.", "cn": "在对待微小随身日常物件上的马虎大意丢三落四毛病，往往反向深刻折射出一个人在精神世界管理与意志力上的散漫失控与不自律。"},
                {"en": "Honesty in handling minor objects prepares a youth for stewardship of immense civic responsibilities.", "cn": "一个在面对区区半截断铅笔的归属权衡上都能做到心如明镜、不贪不昧的清正少年，日后方才真正有资格去承担驾驭关乎天下黎民苍生的宏大公民历史道义重任！"},
                {"en": "May your study desk be a temple of orderliness where clarity of intellect reigns supreme.", "cn": "祈愿你平日伏案求索的书桌案头，永远是一座纤尘不染、条理井然的心灵神圣殿堂，任由澄明深邃的智识灵感火花在其中自由无拘无束地激荡驰骋！"}
            ]
        },
        {
            "title": "Unit 4 · Where's my schoolbag? · 整洁书桌与房间物品收纳好习惯",
            "description": "寻找课本棒球帽子，熟练掌握方位介词与房间收纳收整自律习惯。",
            "sentences": [
                {"en": "Where is my heavy canvas schoolbag? I left it on the dining table yesterday.", "cn": "我那只沉甸甸的军绿色加厚帆布大书包究竟被随手搁置在什么角落了？我分明清清楚楚记得昨晚自己随手将它平放在客厅的实木大餐桌之上了呀。"},
                {"en": "It is not on the table; it is under the chair right next to the bookcase.", "cn": "书桌台面上根本空空如也连半个包影都没有；你快低头瞧瞧，它此刻正委屈巴巴缩在紧挨着楠木大书架旁边的实木扶手椅正下方地板上呢！"},
                {"en": "Are my history notebooks and red fountain pen in the desk drawer or on the bed?", "cn": "请问我那两本密密麻麻记满笔记的中国近代史课堂笔记本与红墨水钢笔，眼下究竟是被收纳在书桌抽屉深处，还是散落在卧室床榻被褥之上？"},
                {"en": "Your notebooks are neatly stacked on the desk, but your keys are in your jacket pocket.", "cn": "你的两本历史课本早已整整齐齐码放在了书桌正中央台面上，但你那串叮当乱响的门禁钥匙，却依然被你遗忘落在了深秋夹克衫的内侧贴身口袋深处。"},
                {"en": "Prepositions of place such as 'in', 'on', 'under', and 'behind' pinpoint spatial locations with accuracy.", "cn": "诸如'in'（在……内部）、'on'（在……表面之上）、'under'（在……垂直正下方）以及'behind'（在……背后隐秘处）等核心空间方位介词，能够以无可挑剔的精准度完成三维物理方位的空间锚定定点！"},
                {"en": "A cluttered room full of scattered clothes and misplaced textbooks scatters mental clarity.", "cn": "一间被胡乱抛洒散落的脏衣服、乱七八糟的教科书试卷塞得满满当当的脏乱差房间，会在不知不觉中悄然严重侵蚀分散一个人原本清明澄澈的心智专注力。"},
                {"en": "Designate a fixed, permanent home for every essential daily tool you own and use regularly.", "cn": "为你手中所拥有的、日常需要频繁使用的每一样核心学习用具与随身工具，在书房居室内统统划定开辟出一个固定恒久、雷打不动的专属专属安歇“家园”。"},
                {"en": "She tidied her bedside table, putting her eyeglasses and alarm clock in their proper places.", "cn": "她耐心地俯下身躯将自己的床头小几整理打理得一尘不染，把近视眼镜与老式机械发条闹钟分别极其妥帖安稳地归位摆放在各自的固定位置之上。"},
                {"en": "The baseball cap was hanging from the wooden peg behind the bedroom oak door.", "cn": "那顶红蓝相间的刺绣棒球运动鸭舌帽，此刻正牢牢悬挂系在卧室纯橡木房门正后方的复古木质挂衣钩圆木桩之上。"},
                {"en": "Developing spatial organization skills during adolescence directly enhances academic efficiency.", "cn": "在青葱青少年起步成长期有意识锤炼提升自己对物理立体空间的科学收纳规划能力，能以最立竿见影的奇效直接成倍倍增日常课业学术攻坚的综合执行效率！"},
                {"en": "His mother smiled warmly upon inspecting the orderly rows of reference books on his shelves.", "cn": "当慈爱的母亲推门走进书房，亲眼端详审视着书架隔板上被儿子分门别类码放得如钢铁方阵般整整齐齐的典籍参考书时，脸上由衷绽放出了欣慰自豪的温暖笑意。"},
                {"en": "Order in your immediate physical environment reflects an orderly, disciplined inner mindset.", "cn": "一个人眼前身处的一方方寸物理微观环境所展现出的秩序井然质感，往往最为直接真实地生动映射折射出其内心精神世界所达到的高度自律与宁静从容。"},
                {"en": "Take five mindful minutes every evening to restore all dispersed items to their designated stations.", "cn": "每逢夕阳西下夜幕低垂之际，不妨慷慨腾出区区五分钟平心静气的禅意光阴，专心致志将全天散落流离在各处的零碎物件统统耐心完璧归赵护送回其指定归宿。"},
                {"en": "Clear horizontal surfaces allow the intellect to focus on complex problem-solving without distraction.", "cn": "一片被彻底清空杂物、宽敞开阔洁净如洗的书桌水平操作台面，能让智识的雄鹰毫无后顾之忧、全身心翱翔聚焦于攻克最为艰深的学术思想硬骨头难题！"},
                {"en": "May your living space be an oasis of serene order where peace and purposeful industry flourish.", "cn": "祈愿你日夜栖居的一方小小书房居室天地，永远是一片杜绝一切杂乱喧嚣、秩序井然的宁静绿洲港湾，任由心灵的安详与奋发图强的学术硕果在其中生生不息、繁茂盛开！"}
            ]
        },
        {
            "title": "Unit 5 · Do you have a soccer ball? · 操场挥汗如雨与课后体育竞技",
            "description": "邀约同窗组队踢球、排球网球体育器材借用与挥洒热血青春。",
            "sentences": [
                {"en": "Do you have a standard leather soccer ball in your locker, or should we borrow one?", "cn": "请问你的个人储物更衣柜里眼下正好存有一只标准缝线真皮足球吗，还是说咱们此刻需要移步前往体育器材保管室去临时登记借上一只？"},
                {"en": "I don't have a soccer ball, but my brother has three durable basketballs in the garage.", "cn": "我手头眼下恰好没有现成的足球可用，但我亲哥哥前不久刚在车库置办购置了整整三颗抓地力极佳的耐磨加厚牛皮室外篮球。"},
                {"en": "Let us organize an exciting friendly football match on the school playground this afternoon.", "cn": "择日不如撞日，咱们趁着今天下午课后放学的黄金大课间时光，在学校塑胶大操场茵茵绿茵场上风风火火筹办组织一场扣人心弦的班级同窗友谊足球对抗争霸赛吧！"},
                {"en": "Does your athletic classmate Jane play tennis skillfully with her new carbon fiber racket?", "cn": "请问你们班上那位极富体育运动天赋特长的高挑女同学简，平日里挥舞起她新买的那柄超轻碳纤维网球拍打起发球截击来，身手究竟算不算得上炉火纯青？"},
                {"en": "Yes, she does; she practices her serve and backhand relentlessly for two hours every evening.", "cn": "那是自然绝对毋庸置疑的；她每天风雨无阻披星戴月在网球场上咬紧牙关高强度反复刻苦淬炼她的暴力正手发球与单臂反手拉弧线战术，一练便是足足两个小时起步！"},
                {"en": "Regular physical exercise strengthens cardiovascular endurance and dispels academic fatigue.", "cn": "持之以恒、周而复始的有规律体育强身健体运动锻炼，不仅能极大筑牢提升人体的心肺综合耐力素质，更能快刀斩乱麻般彻底扫除驱散终日伏案攻读所堆积下的沉重课业疲惫。"},
                {"en": "Team sports teach adolescents the indispensable virtues of selflessness, strategy, and mutual trust.", "cn": "需要多人并肩协同作战的集体球类竞技运动，总能在潜移默化之中为意气风发的青春少年们，深刻上好关于舍己为公集体主义荣誉感、临阵战术机变与将后背托付给战友的互信人生必修大课！"},
                {"en": "Simple present tense questions employing auxiliary 'do' and 'does' govern athletic inquiries smoothly.", "cn": "大量借助助动词'do'与'does'所构筑成型的一般现在时态疑问句与否定句式法则，在日常体育器材借阅与运动技能探讨交流语境中展现出了行云流水般的实用交际魅力。"},
                {"en": "He laced up his spiked running cleats tightly before sprinting across the verdant soccer pitch.", "cn": "在纵身如离弦之箭般全速破空冲刺横越那片如茵苍翠的足球绿茵草坪之前，他深吸一口气俯下身躯，将脚上那双锋利钉鞋的鞋带咬牙死死系紧勒牢。"},
                {"en": "The referee blew the brass whistle loudly to commence the championship match under blue skies.", "cn": "当职的金牌国家级主裁判员在蔚蓝如洗的万里晴空注视之下，运足丹田之气猛然吹响了手中金灿灿的黄铜哨音，宣告本届校运会绿茵总决赛世纪大战正式开球！"},
                {"en": "Cheer enthusiastically for your school team while maintaining genuine respect for worthy opponents.", "cn": "在看台观众席上请务必倾尽全力为你本校的健儿摇旗呐喊擂鼓助威吧，但与此同时更切记时刻在胸膛深处对赛场另一端可敬可畏的拼搏对手抱持一份由衷的君子礼貌尊重！"},
                {"en": "A healthy mind thrives most vigorously within the robust temple of a resilient, exercised body.", "cn": "一个真正充满勃勃生机、富于创造力与深邃智慧的崇高灵魂心智，永远唯独只会在那一具历经汗水反复淬炼锻打、体魄强健如松柏的坚韧肉身神殿深处方能盛大绽放！"},
                {"en": "Victory in sports is sweet, but sportsmanship exhibited during defeat defines true character.", "cn": "在竞技体育争锋对抗中摘金夺银的凯旋滋味固然美妙如甘怡，然而在遭遇惨烈败北甚至饮恨痛失冠军的关键时刻所坦然昂首展现出的君子风度与虽败犹荣傲骨，方才真正定义了一个人不可磨灭的伟大人格！"},
                {"en": "Step away from sedentary screens and let your limbs feel the exhilarating rhythm of athletic motion.", "cn": "果断从那些令人意志消沉、久坐伤身的电子冰冷荧光屏前毅然抽身站立起来吧，张开双臂投身旷野，任由你青春年轻的四肢百骸去真真切切感受体育奔腾律动所激荡出的狂喜心跳澎湃吧！"},
                {"en": "May your youth be punctuated by joyful perspiration, steadfast teamwork, and unyielding vigor.", "cn": "祈愿你这一趟轰轰烈烈的青葱韶华岁月，永远被淋漓酣畅的滚烫汗水、坚不可摧的同生共死团队协作荣辱与共，以及那股永不服输、誓与天公试比高的磅礴少年意气所填满照亮！"}
            ]
        },
        {
            "title": "Unit 6 · Do you like bananas? · 营养均衡饮食与果蔬健康指南",
            "description": "探讨三餐健康饮食偏好、拒绝垃圾食品与践行金字塔膳食平衡。",
            "sentences": [
                {"en": "Do you like eating sweet yellow bananas and crunchy red apples for your daily breakfast?", "cn": "请问你在平日里享用每日清晨营养早餐之时，骨子里偏爱品尝甘甜软糯的金黄香蕉，还是更中意大口咀嚼鲜嫩多汁的香脆红富士苹果？"},
                {"en": "Yes, I love all kinds of fresh seasonal fruits, but I do not like greasy fried chicken.", "cn": "是的没错，我对大自然四季更迭所馈赠出的各色新鲜时令瓜果可以说是发自肺腑的热爱，但我打心眼里却极度排斥反感那些在重油重辣里反复油炸出锅的油腻炸鸡垃圾食品。"},
                {"en": "Does your athletic elder brother enjoy raw vegetable salads topped with extra virgin olive oil?", "cn": "请问你那位热爱挥汗如雨健身长跑的体育生亲哥哥，平日里究竟是否热衷于享用淋上了特级初榨橄榄油与黑胡椒碎的生鲜有机果蔬沙拉？"},
                {"en": "He dislikes broccoli and celery intensely, but he consumes massive amounts of lean beef and eggs.", "cn": "他对盘中的绿西兰花与脆西芹可以说是深恶痛绝避之不及，但在日常增肌食谱中，他每天都需要以惊人的吞吐量大口摄入极为海量的精瘦红牛肉与水煮白水蛋。"},
                {"en": "A balanced nutritional intake consisting of fiber, complex carbohydrates, and proteins fuels active teens.", "cn": "由高活性天然膳食纤维、慢碳水化合物与优质活性蛋白质科学配比构筑的黄金平衡营养摄入膳食金字塔，乃是为正在拔节长个子的生机勃勃初中少年提供全天候澎湃体能续航的生命燃料源泉！"},
                {"en": "Countable nouns like 'apple' and 'hamburger' take plural endings, while uncountable nouns like 'milk' do not.", "cn": "诸如'apple'（苹果）与'hamburger'（汉堡包）等可数名词需要根据数量严谨遵循规则或不规则复数词尾形态变化法则，而诸如'milk'（牛奶）与'beef'（牛肉）等不可数物质名词则永远保持绝对单数形式。"},
                {"en": "Avoid habitual overconsumption of sugary carbonated sodas to protect both dental enamel and metabolism.", "cn": "在日常生活饮食中务必时刻警惕并坚决摒弃杜绝长期酗饮高糖碳酸饮料与勾兑奶茶的恶劣生活方式，以此终身守护好我们脆弱的牙釉质防线与人体胰岛素内分泌代谢平衡！"},
                {"en": "The school cafeteria served a colorful array of steamed dumplings, leafy greens, and tomato soup.", "cn": "今天中午学校示范性标准化大食堂的供餐窗口前，热气腾腾地为全校学子整齐罗列摆出了色香味俱全的花式蒸水饺、清炒时令碧绿小青菜以及营养开胃的现熬番茄蛋花汤。"},
                {"en": "Nutritional habits formed during early adolescence cast profound lifelong shadows over adult longevity.", "cn": "在少年早熟成长关键发育期所悄然筑就养成的每一条日常饮食生活起居膳食习惯，都将在未来数十年的成年乃至晚年岁月长河中，对一个人的机体免疫力寿命长短投射下举足轻重的深远影响！"},
                {"en": "Drink at least eight glasses of clean, lukewarm water daily to optimize biological brain cognition.", "cn": "坚持确保每天至少足额足量科学摄入八大杯清纯温热的白开水甘泉，能够以最具科学实证依据的方式全天候最大化优化激活我们大脑神经中枢的逻辑认知运算敏捷度！"},
                {"en": "She packed a homemade whole-wheat sandwich and sliced carrots inside her eco-friendly bento box.", "cn": "每天清晨离家上学之前，她都会亲自动手为自己精心现做一份夹满了生菜番茄的低卡全麦健康三明治，并将切得细细匀称的新鲜胡萝卜条整整齐齐码装收纳进随身携带的环保便当盒内。"},
                {"en": "Treat food not as a mindless instrument of instant gratification, but as sacred physical fuel.", "cn": "切莫庸俗地将一日三餐口腹之欲仅仅视作一种麻痹神经多巴胺、不假思索追求瞬间多巴胺快感的廉价动物性发泄工具，而当怀揣着敬畏之心将其视作支撑我们肉身凡胎行走人间、践行宏大抱负的神圣能量燃料！"},
                {"en": "Mindful eating with slow, deliberate mastication aids gastrointestinal digestion and prevents overeating.", "cn": "带着从容专注的禅意心境细嚼慢咽、在口腔中让每一口食物都得到充分唾液淀粉酶消化分解的优雅进餐节律，能极大减轻肠胃负担并从根本上规避暴饮暴食对胰腺内脏所带来的病理损伤。"},
                {"en": "Gratitude for the agrarian hands that planted and harvested your daily meals enriches spiritual health.", "cn": "每当执筷端碗面对盘中一粥一饭之时，常怀一颗由衷感念天下千万农人兄弟面朝黄土背朝天躬身春耕秋收之不易的敬畏感恩之心，方能真正大滋大养我们内在灵魂的精神福报！"},
                {"en": "May your plate be a vibrant rainbow of vitality, nourishing both mental genius and physical resilience.", "cn": "祈愿你每天摆在案头餐桌前的餐盘，永远是一方斑斓绚烂、充满五彩缤纷自然生机的大自然生命调色盘，日夜深情滋养灌溉着你过人的聪慧才智与坚不可摧的百炼钢铁体魄！"}
            ]
        },
        {
            "title": "Unit 7 · How much are these socks? · 跳蚤市场选购衣物与理财消费",
            "description": "校园跳蚤市场买卖旧衣、询问价格尺码与树立青年理性消费观。",
            "sentences": [
                {"en": "How much are these warm woolen socks, and do you have them in navy blue?", "cn": "请问摆在货架显眼位置上的这几双加厚保暖羊毛袜售价究竟是几许一双，另外你们摊位上目前存货里还配有深沉庄重的海军藏青配色款式吗？"},
                {"en": "They are only two dollars a pair today because of our annual charity clearance sale.", "cn": "只因今天恰逢我们全校一年一度隆重举行的爱心助学慈善义卖清仓大集市特惠酬宾日，所以这批原装纯羊毛袜统统破例只卖区区两美元一双的历史吐血白菜价！"},
                {"en": "How much is that oversized purple cotton sweater hanging against the wall display?", "cn": "请问高高悬挂在靠墙立面展示架正中央的那件宽松版型、印有复古英文字母印花图案的深紫色纯棉连帽套头卫衣，标价究竟要多少大洋一件？"},
                {"en": "It is twenty-five dollars; it is made of exceptionally soft organic combed fleece fabric.", "cn": "那件高档卫衣公道实价承惠二十五美元整；整件衣衫全幅采用手感极其温润细腻、亲肤透气的高品质天然有机精梳摇粒绒面料精工剪裁缝制而成。"},
                {"en": "We take these three pairs of striped socks and the woolen scarf, please.", "cn": "太划算满意了！请劳驾替我们麻利打包结算收下这三双红白条纹相间的运动棉袜，以及挂在柜台旁的那条保暖羊毛针织围巾吧。"},
                {"en": "The student volunteers collected proceeds to purchase library books for underprivileged rural schools.", "cn": "在义卖大棚前忙前忙后负责收银记账的青年学生志愿者骨干们，当场郑重将全天所得的每一笔义卖善款收入悉心封存入专用铁皮保险箱，专款专用用于为偏远山区贫困小学捐资筹建爱心希望图书室。"},
                {"en": "Inquiring about prices using 'how much is' for singulars and 'how much are' for plurals forms core commerce.", "cn": "针对单数商品物件精准调用'how much is'、针对复数成对货品娴熟运用'how much are'展开砍价询盘问价，构成了中英文跨文化商贸日常基础交易的绝对核心基石句型！"},
                {"en": "Financial literacy cultivated in youth protects individuals against the seductive perils of consumer debt.", "cn": "在年少青葱懵懂时期便通过实战亲身体验、在心田深处及早播种下科学理性财商认知与记账消费规划观念，能为青年人构筑起一道在日后步入名利繁华浮躁社会时足以终身抵御各类透支消费信贷毒瘤侵害的金钟罩铁布衫！"},
                {"en": "Distinguish ruthlessly between genuine physical needs and transient, impulse-driven material wants.", "cn": "在每一次冲动想要掏出钱包或刷脸支付的生死毫厘之间，学会极其冷酷清醒、毫不留情地在内心天平上精准劈开划清“肉身凡胎维持生存发展的绝对刚性必需品”同“虚荣心作祟、转瞬即逝的虚浮伪欲望”之间的本质天堑分野！"},
                {"en": "The second-hand flea market promoted ecological sustainability through practical garment reuse and recycling.", "cn": "在这场校园二手跳蚤集市的推杯换盏交易之间，通过将闲置衣物与图书用具转手给真正亟需之人的务实闭环流通，以生动实践深刻践行落地了绿色低碳、物尽其用的崇高现代生态环保循环文明理念！"},
                {"en": "She carefully checked her coin purse and calculated the exact change owed to the customer.", "cn": "她端坐在收银台前极其细致耐心地拉开手工零钱包拉链，借着台灯光晕心算口算反复复核无误后，分文不差将应找零的每一枚崭新硬币礼貌双手奉还递到顾客掌心之中。"},
                {"en": "True personal elegance stems from the refinement of character, never from the vanity of expensive designer labels.", "cn": "一个人浑身上下所能展现出的真正的、令全场为之动容脱帽的高贵优雅气质风骨，从来全都是发自肺腑源于其骨子里的品格修养与如兰谈吐，而绝非靠那些暴发户式堆砌大牌Logo的昂贵奢侈品外壳所能装点！"},
                {"en": "Budget your pocket money prudently, allocating portions for essential spending, long-term savings, and generous charity.", "cn": "精打细算科学打理掌控好你手中的每一分压岁钱与零花钱吧，将有限的资金科学切分为“日常刚性课业开支”、“终身不动产长期应急储蓄”以及“扶危济困慷慨慈善公益捐赠”三大黄金资金池！"},
                {"en": "A thrifty lifestyle frees financial resources to invest in intellectual enrichment and meaningful life experiences.", "cn": "克勤克俭、崇尚质朴极简的节俭生活方式，能在人生的漫漫旅途长河中为你源源不断沉淀腾挪出海量宝贵的真金白银现金流，去全力投资押注在滋养你的智识认知升级与那些真正洗涤心灵的深刻生命非凡体验之上！"},
                {"en": "May your financial judgment remain sober, ethical, and generous throughout your mortal journey across markets.", "cn": "祈愿你这一生在穿行于光怪陆离、尔虞我诈的残酷世俗市场洪流洗礼之中，内在的商业经济决策判断力永远保持清醒冷峻、恪守道德良知底线，并永远对天下苦难受难苍生怀揣着一颗慷慨悲悯的倾囊相助仁爱之心！"}
            ]
        },
        {
            "title": "Unit 8 · When is your birthday? · 生日聚会筹备与四季月份日历",
            "description": "询问生日日期、学习十二月份与序数词用法，筹划温馨感恩生日派对。",
            "sentences": [
                {"en": "When is your birthday, and how do you usually commemorate the special day with loved ones?", "cn": "请问你的降生诞辰大喜之日究竟是在哪一月哪一天，平日里你又是如何同身畔挚爱的至亲亲友与知己同窗携手共同纪念度过这个非凡难忘的特殊吉日的呢？"},
                {"en": "My birthday is on October twelfth; we usually celebrate by baking a cake together at home.", "cn": "我的公历生日恰好正是在金秋时节十月十二日那一天；按照我们全家的多年惯例，每逢那夜我们阖家老小总会围拢在厨房烤箱四周，齐心协力亲手烘焙烤制一只大蛋糕以示庆贺。"},
                {"en": "Is your grandfather's eighty-fifth birthday in January or does it fall in late December?", "cn": "请问你家中那位德高望重的慈祥老祖父的八十五岁古稀大寿吉庆之日，究竟是排在开年正月元月份，还是恰好恰巧坐落在岁末腊月十二月下旬的时节呢？"},
                {"en": "His birthday is on January first; we host a magnificent New Year family feast every year.", "cn": "老人家的降生吉日恰好正逢元旦一月一日与天地同庆的良辰吉时；正因如此，每逢那一天我们全族上下海内外上百口族人，都会千里迢迢赶回老宅老祠堂欢聚一堂，隆重操办盛大无匹的跨年祭祖兼贺寿宗族大寿宴！"},
                {"en": "Ordinal numbers such as 'first', 'second', 'third', and 'twelfth' designate precise chronological dates.", "cn": "诸如'first'（第一）、'second'（第二）、'third'（第三）以及特异形态变化的'twelfth'（第十二）等序数词的高阶规范运用，专门用于在人类历法时间线上对年月日具体日期的精准锚定指代。"},
                {"en": "The twelve months of the Gregorian calendar reflect deep mythological and agricultural Roman history.", "cn": "现代全球通用的公历纪年法体系下的整整十二个月份英文命名渊源，其背后深深刻骨铭心地折射承载着古罗马帝国时期波澜壮阔的神话宇宙诸神崇拜与古代农耕四时物候更迭的厚重文明密码！"},
                {"en": "A birthday should serve not merely as an excuse for indulgence, but as a day of solemn maternal thanksgiving.", "cn": "一个人的生辰诞辰吉日，从来绝不该仅仅沦为一场只顾自己推杯换盏纵情狂欢暴饮暴食的借口，而更理当成为一个庄严向当年九死一生将我们带到这个大千世界的伟大生身母亲顶礼膜拜、跪谢母难生恩的神圣感恩受难日！"},
                {"en": "She circled the date with red ink on the wall calendar to ensure she would not forget her mother's anniversary.", "cn": "她庄重无比地手握饱蘸大红墨水的钢笔，在书房悬挂的精美月历牌上将那一天重重画上了一个醒目的大圆圈，以此督促警醒自己千千万万绝不可遗忘淡漠了慈母的结婚纪念周年大日。"},
                {"en": "Adolescents plan surprise birthday gatherings by compiling heartfelt handwritten letters from every single classmate.", "cn": "天真烂漫的初中同窗伙伴们为了给过生日的同桌策划一场终身难忘的巨大惊喜，在暗中悄悄分工协作串联，挨个搜集汇编了全班每一位同学亲笔蘸着真情手写的字字滚烫祝福信札长卷！"},
                {"en": "Preposition 'in' precedes months alone, while preposition 'on' precedes specific calendar dates.", "cn": "在英语时间介词的严谨语法世界中，介词'in'专门负责统御单列出现的泛指年份或月份（如 in October），而唯有一旦出现精确定格到某月某日具体某一天之时，则必须当机立断果断换用介词'on'执掌乾坤（如 on October 12th）！"},
                {"en": "The passage of each completed birthday marks the relentless forward march of mortal human time.", "cn": "每当生日蛋糕上那一簇簇跳动摇曳的生日蜡烛被一口气轻吹熄灭的刹那，它无情而庄严地标志着我们作为凡胎肉身在奔腾不息的浩瀚时空大河长卷中，又无可逆转地向前踏出了一圈向成熟进军的不可逆生命刻度年轮！"},
                {"en": "Honor the gift of life by reviewing whether the preceding year witnessed genuine intellectual and moral progress.", "cn": "唯有在生辰烛火前平心静气、闭目虔诚深刻复盘反思拷问自己在刚刚过去的这整整三百六十五个日夜沧桑中，究竟是否在智识思想底蕴与道德人格修养上取得了无可辩驳的坚实精进，方才配得上由衷礼赞上苍赐予我们这一副血肉之躯的神圣生命恩典！"},
                {"en": "Simple handwritten birthday greetings penned with raw emotional sincerity outshine lavish commercial gifts.", "cn": "一张普普通通甚至略显粗糙、但通篇却字斟句酌蘸满了纯真挚友由衷深情与肺腑赤诚的手写生日卡片手札，其所蕴藏的心灵震撼穿透力，足以轻而易举秒杀艳压那些堆砌在名牌礼品盒里冷冰冰的昂贵商业工业快餐铜臭礼物！"},
                {"en": "Celebrate the anniversary of your arrival on this planet by dedicating yourself anew to serving your community.", "cn": "去以一种崭新的崇高精神境界来隆重纪念你当年降生踏足这座蓝色美丽星球的伟大周年吧——那就是在心头庄严重新向苍天宣誓：在新的一岁生命年华里，我必将更加义无反顾地将自己的毕生所学与热血，全情奉献给滋养庇护我的国家与父老乡亲！"},
                {"en": "May every passing year sculpt your character into a masterpiece of wisdom, kindness, and indomitable courage.", "cn": "祈愿伴随着日历牌上一页页流金岁月的无情飞速撕去，奔腾不息的时光神工雕刻刀，终将把你的人格心智彻底精雕细琢锻打成一座饱经风霜却熠熠生辉、融汇了无上智慧、博大慈悲仁爱与顶天立地不可战胜无畏勇气的千秋传世精神杰作！"}
            ]
        },
        {
            "title": "Unit 9 · My favorite subject is science · 探索宇宙奥秘与最喜爱学科",
            "description": "探讨课程表最爱学科理由、感念授业解惑恩师，树立科学探索强国理想。",
            "sentences": [
                {"en": "What is your favorite academic subject at school, and why do you find it so intellectually stimulating?", "cn": "在初中课程表所开设的琳琅满目各大学术学科门类之中，究竟哪一门课才是深得你芳心、被你奉为至爱的核心王牌学科，而你又是究竟出于何等由衷缘由发掘出它竟然具有这般引人入胜、令人心驰神往的思想智识穿透力？"},
                {"en": "My favorite subject is natural science because our passionate teacher conducts fascinating laboratory experiments.", "cn": "我打心眼里最痴迷热爱的学科非自然科学大课莫属，只因我们那位学富五车、讲起课来神采飞扬充满极强感染力的骨干名师，总能在每一节课上带领我们亲自动手开展各种令人大开眼界拍案叫绝的奇妙物理化学前沿实验室实验！"},
                {"en": "He dislikes memorizing historical dates, but he adores geography because studying world maps fuels his wanderlust.", "cn": "他平日里对死记硬背历史试卷上那些密密麻麻的干瘪年代数字感到头疼不已、枯燥乏味，但他却对世界地理大课爱到了骨髓深处，只因在课堂上细细端详摩挲五彩斑斓的全球立体地形地貌大沙盘，总能疯狂点燃他在未来有朝一日踏遍五洲四海远走高飞的无尽探索雄心！"},
                {"en": "Why does Alice consider rigorous mathematics to be the supreme queen of all human analytical sciences?", "cn": "究竟是何等魔力与逻辑魅力，促使冰雪聪明的爱丽丝同学在心头坚定不移地将推演严密、毫无半点含糊其辞的高等数学大厦，奉为整个人类一切严谨逻辑理性分析实证科学领域皇冠之巅最至高无上、统御乾坤的璀璨女王桂冠？"},
                {"en": "She believes mathematical logic provides the universal grammar that explains every physical law in the cosmos.", "cn": "只因在她那颗天才般的少女理智深处坚信不疑：深邃优雅的高等数学推演逻辑骨架，构成了整个人类文明用以精准破译、完美阐释浩瀚大千宇宙深处一切物理运行底层铁律与星体轨迹的至高通用宇宙语言语法！"},
                {"en": "Inquiring about preferences using 'what is your favorite' and explaining causes with 'because' anchors structured exposition.", "cn": "借助'what is your favorite'（什么是你最热爱的至爱）展开逻辑发问立论，紧接着无缝调遣引导因果从句的黄金连词'because'（只因……）展开层层递进的事实论据因果链条严密拆解，构成了现代学术说明论说文体最核心稳健的文风骨架基石！"},
                {"en": "A truly inspiring teacher does not merely transmit standardized facts, but ignites an eternal flame of wonder.", "cn": "一位名垂青史、真正拥有立德树人教育灵魂的伟大启蒙导师，在三尺讲台之上所终身致力于躬身践行的，从来绝非仅仅只是照本宣科机械单向度灌输填鸭应试大纲上的冰冷死知识点；而是以自己滚烫的灵魂之火，去彻底点燃照亮莘莘学子胸膛深处那簇对未知浩瀚世界永不熄灭的纯真惊奇探索火苗！"},
                {"en": "The physics instructor demonstrated electromagnetic induction using simple copper wire coils and bar magnets.", "cn": "今天上午那位治学严谨的高级物理教师在讲台上屏息凝神，仅仅凭借着几团平平无奇的纯铜漆包线自制线圈与两根普通的红蓝条形强磁铁棒，便在全班同学目瞪口呆的见证下，出神入化现场实机演示验证了伟大法拉第电磁感应定律那巧夺天工的传世物理奇迹神迹！"},
                {"en": "Dedicate focused study hours to the foundational subjects that unlock your apex cognitive potential.", "cn": "毫不犹豫将你青春最充沛饱满的黄金专注自习研读光阴，孤注一掷全神贯注全力倾注押注在那些能够为你彻底破壁解锁、终极引爆你人类大脑巅峰认知推演潜能的底层基础核心硬核主干学科之上吧！"},
                {"en": "Humanities and hard sciences are not hostile adversaries, but complementary wings lifting the human spirit.", "cn": "承载着人性温度与道德伦理关怀的文史哲人文社科学科，同推演冷峻精确的数理化天地硬核自然科学前沿，从来绝非什么水火不容、非此即彼的敌对派系阵营；而是恰恰好似大鹏展翅扶摇直上九万里苍穹云霄时，那一左一右相辅相成、缺一不可的强健神圣精神腾飞双翼！"},
                {"en": "The literature seminar debated Shakespearean character motivation with fierce analytical sophistication.", "cn": "在下午举行的校际高级英语经典文学研讨研读大课之上，全班各学术攻坚兴趣学习小组围绕着莎士比亚传世悲剧四大名著核心主人公在灵魂深处的阴暗欲望挣扎与心理潜意识动机抉择，展开了一场针尖对麦芒、极具思想学术交锋烈度的高阶辩论大厮杀！"},
                {"en": "Approach challenging subjects that initially frustrate you with humble patience and unyielding intellectual grit.", "cn": "面对那些在初学乍练门槛阶段常常撞得你头破血流、令你心灰意冷倍感挫败煎熬的艰难晦涩硬骨头学科门类时，请务必时刻在胸膛深处端正调动起最谦逊敬畏的求索耐心，以及一股咬定青山不放松、纵使百转千回也誓死将其生吞活剥彻底拿下的钢铁学术硬骨头狠劲！"},
                {"en": "Genuine passion for learning transforms laborious academic homework into a jubilant odyssey of mental discovery.", "cn": "发自灵魂骨髓深处对求知与真理的至死不渝纯真热爱激荡，拥有一种能够将一切枯燥乏味、沉重如山的面壁课业家庭作业苦役，瞬间奇迹般华丽蜕变升华为一场在浩瀚无垠知识星空宇宙深处乘风破浪、欢呼雀跃的狂喜心灵探险大远征！"},
                {"en": "Listen intently to the diverse perspectives articulated by your peers during seminar debates.", "cn": "在群雄舌战学术争鸣的大课堂讨论交锋时分，学会以海纳百川的博大胸襟与绝对专注的学者风范，屏气凝神用心去倾听领会端坐在四周同侪学子基于不同逻辑思维盲区所独立推演吐露出的多元独家学术视角真知灼见！"},
                {"en": "May your academic quest be an unending celebration of truth, beauty, and philosophical wonder.", "cn": "祈愿你这一趟跨越漫漫书山题海苦旅的崇高学术求索终身大征程，永远是一场向着世间颠扑不破的客观真理、纯正高雅的宇宙和谐之美，以及对浩瀚存在之谜深怀无尽哲学惊叹的永不落幕的不朽精神加冕狂欢盛典！"}
            ]
        },
        {
            "title": "Unit 10 · Can you play the guitar? · 校园社团招新与才艺特长汇演",
            "description": "音乐美术象棋体育社团百团大战招新，各展所长登台亮相与青春才艺盛典。",
            "sentences": [
                {"en": "Can you play the acoustic guitar melodiously, or do you excel at playing classical grand piano?", "cn": "请问你在闲暇之余能够抱起木吉他行云流水扫弦弹奏出悠扬动听的民谣旋律，还是说你更早在名师指点下便已然出神入化精通在九尺大三角钢琴黑白琴键之上独奏行云流水的古典传世名篇？"},
                {"en": "I cannot play musical instruments well, but I can sing soprano beautifully and I love theatrical acting.", "cn": "我平生在抚弄摆弄各类复杂西洋民族乐器器物上确实略逊一筹稍显笨拙，但我天生拥有一副清脆嘹亮、直插云霄的天籁女高音纯正歌喉，并且我对登台在聚光灯下全情投入塑造舞台戏剧人物角色可以说是酷爱到了骨髓深处。"},
                {"en": "We are recruiting enthusiastic new members for our prestigious student English drama society.", "cn": "我们目前正代表着全校享有盛誉的王牌明星学生社团——“青年英语戏剧莎士比亚话剧研习公社”，面向全校初一全体新入学的师弟师妹们，大张旗鼓不拘一格隆重招募选拔一批满腔热忱、敢想敢拼的新生代骨干新血液！"},
                {"en": "Can your athletic best friend swim freestyle rapidly, or does he prefer joining the competitive chess guild?", "cn": "请问你身畔那位生龙活虎、浑身肌肉线条饱满的铁哥们死党，究竟是擅长在蔚蓝波涛翻滚的国际标准恒温泳池里劈波斩浪高速狂飙自由泳，还是说他打心眼里更情有独钟于端坐在静寂无声的棋盘案头前、毅然加入勾心斗角暗流涌动的校级国际象棋大师竞技公社呢？"},
                {"en": "Modal auxiliary 'can' expressing physical capability and learned talent empowers vibrant youth recruitment discourse.", "cn": "情态动词'can'专门用于精准赋能表征人类先天身心运动生理机能极限与后天刻苦淬炼习得的专业才艺禀赋造诣，在整篇朝气蓬勃的校园社团招新纳新话语大体系构建中展现出了所向披靡的修辞号召力！"},
                {"en": "Extracurricular clubs cultivate vital leadership, project management, and collaborative communication competencies.", "cn": "丰富多彩的课外学生社团自主自治组织淬炼，总能在毫无应试应酬包袱的纯粹实践熔炉之中，全方位深度孵化培育出一个青年人受用一生的战略领导力、复杂大型文体活动项目统筹落地执行力以及跨界协同沟通的大智慧！"},
                {"en": "The school courtyard buzzed with electric youthful excitement during the annual autumn club recruitment carnival.", "cn": "在全校一年一度隆重拉开帷幕的“金秋学生社团百团大战招新嘉年华狂欢大集市”期间，整座被五彩缤纷彩旗气球装点一新的学校中心大花园林荫广场之上，处处激荡洋溢着令人血脉偾张、青春荷尔蒙爆棚的欢声笑语与无穷活力！"},
                {"en": "Talent undiscovered is like unpolished jade buried deep within an inaccessible granite mountain.", "cn": "天底下任何未经后天勇敢登台亮相、未经世面风雨大场面反复打磨淬炼的绝世才华天赋，都好似一块被永久深锁幽禁在万仞绝壁花岗岩绝顶地心腹地深处、无人问津的粗粝暗淡璞玉废石！"},
                {"en": "She painted a magnificent landscape banner using Chinese ink to decorate the calligraphy society booth.", "cn": "她端坐在招新展位案头前气定神闲饱蘸浓墨，以力透纸背的苍劲笔锋一气呵成当场挥毫泼墨勾勒绘就了一幅气吞山河、水墨淋漓的泼墨山水巨幅迎新宣纸横幅，用以隆重装饰装点中华传统书画篆刻研习社的迎新门脸！"},
                {"en": "Do not allow self-conscious timid hesitation to prevent you from auditioning for the school orchestra.", "cn": "千千万万莫要因骨子里那份瞻前顾后、唯恐在旁人面前出丑露怯的自卑羞怯犹豫心魔作祟，而硬生生错失断送掉本该属于你鼓起天大勇气毅然登台参与全校交响乐团声部主奏席位残酷盲听终极试音选拔的神圣人生机遇！"},
                {"en": "Every teenager possesses unique latent gifts waiting to be nurtured within a welcoming, supportive community.", "cn": "放眼红尘大千世界，这凡间每一个看似平淡无奇、内敛少言的青葱少年少女躯体深处，无一例外统统深埋潜藏着独一无二、惊才绝艳的潜在璀璨天赋宝藏，唯独静候着在一个充满包容大爱、鼓励试错的温暖社团大家庭沃土深处破土发芽！"},
                {"en": "Stage fright dissipates instantly the moment you lose yourself entirely in the joyous service of the art.", "cn": "一切在临登大台前令你双腿打战、冷汗直流的所谓“高台畏惧心理心魔”，在你毅然决然挺直脊梁迈上聚光灯中心、全副身心彻底忘我沉醉臣服于手中艺术神圣召唤的惊天一秒瞬间，必将如烈日下的晨霜般瞬间灰飞烟灭烟消云散！"},
                {"en": "Collaborative artistic creation binds diverse young souls into a harmonious, resonant symphony of collective joy.", "cn": "跨学科、跨领域的青年学子携手并肩同台进行文艺艺术联合创作演出，能以润物细无声的神奇魔法，将来自不同班级背景、性格迥异的年轻灵魂，紧密熔铸编织成一曲同频共振、撼人心魄的集体欢欣不朽交响华彩！"},
                {"en": "Step boldly onto the platform and share your authentic light; the universe celebrates your distinctive creative voice.", "cn": "昂首阔步挺起胸膛勇敢迈步踏上那座属于你自己的生命大舞台中央吧，毫无保留大方倾情释放分享出你灵魂底层最本真纯粹的夺目光辉吧；整座辽阔浩瀚的宇宙星河，此刻都在屏住呼吸由衷为你那独一无二的非凡创造力绝唱长啸而鼓掌欢呼喝彩！"},
                {"en": "May your junior high years be a glorious tapestry woven with daring creative exploration and lifelong camaraderie.", "cn": "祈愿你这一趟轰轰烈烈的初中求学黄金韶华岁月，永远是一卷由敢为人先的先锋艺术勇敢探索、以及同生共死历经沧海桑田依然长青的莫逆同窗兄弟战友情谊，所携手飞针走线共同织就出的绝美鎏金锦绣史诗长卷！"}
            ]
        }
    ]
    courses.append(build_course(rj7_meta, rj7_chapters))

    return courses

if __name__ == "__main__":
    print("Testing Renjiao...")
    c = get_renjiao_courses()
    print("Renjiao Grade 7 course:", len(c))
