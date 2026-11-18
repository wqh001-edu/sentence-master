# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))

from builder_core import build_course, save_ts_file, preload_existing_mall_files

def get_textbook_courses():
    courses = []
    
    # -------------------------------------------------------------------------
    # 1. 新概念英语第一册 (10章)
    # -------------------------------------------------------------------------
    nce1_meta = {
        "id": "course-tb-nce1",
        "title": "《新概念英语第一册》(NCE 1) · 基础入门语音与地道日常对话 (10章全集)",
        "category": "textbook",
        "categoryName": "教材同步",
        "coverGradient": "from-blue-600 via-cyan-600 to-teal-500",
        "icon": "📘",
        "description": "英语初学者第一课，从零掌握基础语音、经典日常对话与纯正英式交际。",
        "difficulty": "入门零基础 A1",
        "tags": ["新概念一册", "零基础", "经典教材", "口语起步"]
    }
    nce1_chapters = [
        {
            "title": "第 1 课 · Excuse me! · 借光问询与手提包失物招领",
            "description": "礼貌打扰、确认失物与由衷感谢的英伦经典交际。",
            "sentences": [
                {"en": "Excuse me! Yes? Is this your handbag?", "cn": "劳驾打扰一下！什么事？这是您的手提包吗？"},
                {"en": "Pardon? Is this your handbag? Yes, it is.", "cn": "对不起您说什么？请问这是您的手提包吗？是的，正是我的。"},
                {"en": "Thank you very much. You're very welcome.", "cn": "真是太感谢您了。完全不用客气，举手之劳。"},
                {"en": "Polite greetings form the cornerstone of civilized daily conversation.", "cn": "得体礼貌的问候语构成了现代文明日常交际的坚实基石。"},
                {"en": "Always remember to keep your belongings within sight in public spaces.", "cn": "在公共场合务必时刻留意保管好自己的随身物品，莫使其脱离视线。"},
                {"en": "A simple 'excuse me' opens doors to friendly communication.", "cn": "一声简单的“劳驾打扰”，便能为善意友好的沟通交流敞开大门。"},
                {"en": "She checked the contents of the bag and breathed a sigh of relief.", "cn": "她仔细清点了皮包内的物件，由衷松了一口气。"},
                {"en": "Honesty among strangers restores faith in community warmth.", "cn": "陌生人之间的拾金不昧，重新点燃了人们对社会温情的信任。"},
                {"en": "Could you please tell me where the cloakroom is located?", "cn": "能否劳驾请问您一下，衣帽间具体位于什么方位？"},
                {"en": "Small acts of integrity leave lasting ripples of goodwill.", "cn": "微不足道的正直善举，往往能在人世间荡漾起持久温暖的善意涟漪。"},
                {"en": "The gentleman tipped his hat and handed back the lost property.", "cn": "那位绅士微微脱帽致意，将遗失的物件完好奉还。"},
                {"en": "A calm, pleasant tone of voice puts everyone at ease.", "cn": "平和愉悦的谈吐语调，能够让在场的每一个人都倍感舒适安详。"},
                {"en": "Every beginner journey begins with mastering courteous inquiries.", "cn": "每一趟初学者的语言求索之旅，都是从熟练掌握礼貌的问询开始起步的。"},
                {"en": "Gratitude expressed sincerely deepens mutual respect between people.", "cn": "发自肺腑的由衷谢意，能够深化人与人之间崇高的相互尊重。"},
                {"en": "Carry these foundational courtesy phrases wherever you travel.", "cn": "无论你今后行至天涯海角何方，都请随身带好这些最基础的文明礼貌金句。"}
            ]
        },
        {
            "title": "第 2 课 · Sorry, sir. · 歉意礼貌与衣帽间大衣号码牌",
            "description": "寄存衣物、出示号牌与取错大衣时的机智沟通。",
            "sentences": [
                {"en": "My coat and my umbrella please. Here is my ticket.", "cn": "请把我的大衣和雨伞取给我。这是我的寄存号牌。"},
                {"en": "Thank you, sir. Number five. Here's your umbrella and your coat.", "cn": "谢谢您，先生。这是五号牌。这是您的雨伞和大衣。"},
                {"en": "This is not my coat! Sorry, sir. Is this your coat?", "cn": "这绝不是我的大衣！非常抱歉先生。请问这一件是您的吗？"},
                {"en": "No, it isn't. That is my coat over there.", "cn": "不，这一件也不是。挂在那边角落里的才是我的大衣。"},
                {"en": "Here you are, sir. Thank you very much indeed.", "cn": "给您先生，拿好了。真是太感谢您了，万分感激。"},
                {"en": "Check your cloakroom ticket carefully before stepping away from the counter.", "cn": "在离开衣帽间柜台前，务必仔细核对清楚手头的寄存号码凭证。"},
                {"en": "Mistakes happen frequently in crowded winter cloakrooms.", "cn": "在熙熙攘攘拥挤的冬季衣帽间里，忙乱中拿错衣物是在所难免的寻常事。"},
                {"en": "A polite apology instantly defuses potential frustration.", "cn": "一句得体真诚的道歉，瞬间便能化解潜在的焦躁与不快。"},
                {"en": "The heavy woolen overcoat kept him warm during the damp London evening.", "cn": "那件厚实的粗花呢羊毛大衣，在伦敦潮湿阴冷的冬夜里为他驱散了周身寒意。"},
                {"en": "Patience and understanding turn awkward mix-ups into pleasant encounters.", "cn": "多一份从容耐心与包容谅解，尴尬的差错亦能化作愉悦的心灵邂逅。"},
                {"en": "He double-checked the brass number tag against his receipt.", "cn": "他再次对照收据，反复核验确认了手中的黄铜号码牌编号。"},
                {"en": "Civil service with a warm smile brightens a rainy winter day.", "cn": "洋溢着温暖笑脸的文明服务，足以驱散阴雨连绵冬日的满身萧瑟。"},
                {"en": "Keep calm when personal belongings are momentarily misplaced.", "cn": "当随身私人物件暂时发生错拿时，请务必保持沉着冷静。"},
                {"en": "Clarity of description resolves confusion far quicker than impatience.", "cn": "清晰准确的物件特征描述，化解困惑的效率远胜过急躁发脾气。"},
                {"en": "Polite society thrives on the delicate balance of consideration and courtesy.", "cn": "现代文明社会的优雅运转，全赖体谅他人与谦恭守礼之间微妙的和谐平衡。"}
            ]
        },
        {
            "title": "第 3 课 · Nice to meet you · 新生初识与国籍职业引荐",
            "description": "介绍同窗、询问国籍与校园多元文化背景初体验。",
            "sentences": [
                {"en": "This is Sophie Dupont. Sophie is a new student from France.", "cn": "这位是索菲·杜邦。索菲是来自法国的一位新同学。"},
                {"en": "Sophie, this is Hans. He is German. Nice to meet you.", "cn": "索菲，这位是汉斯。他是德国人。非常高兴能与你相识。"},
                {"en": "Nice to meet you, too. Are you an architect, Hans?", "cn": "我也非常荣幸能认识你。请问汉斯，你是一名建筑师吗？"},
                {"en": "No, I am not. I am a keyboard engineer.", "cn": "不，我不是建筑师。我是一名键盘软件工程师。"},
                {"en": "Diversity of languages and cultures enriches our international classroom.", "cn": "多元化的语言与文化背景，极大丰富了我们这间国际课堂的精神底蕴。"},
                {"en": "Introduce friends warmly by highlighting their background and interests.", "cn": "向他人引荐新朋友时，不妨大方介绍其地域背景与兴趣特长以拉近距离。"},
                {"en": "A firm handshake accompanied by warm eye contact conveys confidence.", "cn": "一次坚定有力的握手并配合温暖真诚的目光注视，能传递出非凡的自信与坦荡。"},
                {"en": "She speaks three European languages with remarkable fluency.", "cn": "她能够以令人惊叹的纯正流利度，熟练操持三种欧洲语言。"},
                {"en": "Cultural curiosity builds enduring bridges across national boundaries.", "cn": "对异域文明抱持真诚的求知欲，能在跨越国界疆域之间构筑起永恒的心灵桥梁。"},
                {"en": "Learning how people describe their professions expands practical vocabulary.", "cn": "学习人们如何准确描述各自的职业身份，能够有效拓宽实用的词汇储备。"},
                {"en": "Classrooms where mutual curiosity thrives foster deep global friendships.", "cn": "在充满相互求知与包容氛围的课堂里，最容易孕育出深厚的跨国友谊。"},
                {"en": "Pronounce international names respectfully to demonstrate genuine courtesy.", "cn": "以尊重谨慎的态度准确念诵外国友人的姓名，是彰显真正教养的无声细节。"},
                {"en": "Every unique personal heritage brings a fresh perspective to conversation.", "cn": "每一份独一无二的个人成长底蕴，都能为日常谈吐对话带来崭新的观察视角。"},
                {"en": "Meeting peers from diverse continents broadens our intellectual horizons.", "cn": "同来自五洲四海的同龄知己相遇相知，极大开阔了我们的精神思想视界。"},
                {"en": "Treasure every cross-cultural encounter as an opportunity for mutual learning.", "cn": "将每一次跨文化的萍水相逢，都视若增进互学互鉴、共同成长的宝贵造化。"}
            ]
        },
        {
            "title": "第 4 课 · Are you a teacher? · 身份问答与校园多元角色",
            "description": "探讨师生身份、专业分工与校园多元学术岗位。",
            "sentences": [
                {"en": "Are you a teacher at this language academy?", "cn": "请问您是这所语言学院里任教的一位专职老师吗？"},
                {"en": "No, I am a student studying contemporary English literature.", "cn": "不，我并不是老师。我是这里攻读当代英国文学的一名求学学生。"},
                {"en": "Is that gentleman over there the headmaster of the school?", "cn": "请问端坐在那边长椅上的那位老绅士，便是这所学校的校长先生吗？"},
                {"en": "Yes, he is. He oversees all academic programs with immense dedication.", "cn": "是的正是他。他以极其崇高的敬业精神，总揽协调着全校所有的教学教研项目。"},
                {"en": "Every member of our school community plays a vital role in education.", "cn": "我们校园大家庭中的每一位成员，都在立德树人的教育事业中扮演着举足轻重的角色。"},
                {"en": "Clear role identification prevents misunderstandings in university administration.", "cn": "分工明确的岗位职责界定，能够有效避免大学日常行政运转中的沟通误解。"},
                {"en": "The professor held office hours to answer students' grammatical questions.", "cn": "这位资深教授特意安排了课后答疑时间，悉心解答学子们提出的语法疑难点。"},
                {"en": "Librarians guide researchers toward rare manuscripts and digital archives.", "cn": "图书馆管理员耐心地指引学术研究人员去查阅珍贵的古籍手稿与数字化档案。"},
                {"en": "Ask clarifying questions whenever you are uncertain about administrative procedures.", "cn": "每当你对学校的某项行政规程心存疑惑时，务必及时礼貌提问加以核实确认。"},
                {"en": "Academic mentorship shapes the intellectual trajectory of young scholars.", "cn": "师长学者们悉心的学术指点，深刻塑造着青年学子一生的求索心路轨迹。"},
                {"en": "Staff members worked tirelessly to organize the annual literature seminar.", "cn": "学院全体教职员工废寝忘食协同奋战，全力组织筹备一年一度的文学研讨盛会。"},
                {"en": "Cultivate a profound respect for every educator dedicated to passing on knowledge.", "cn": "对于每一位毕生致力于知识薪火传承的辛勤教育工作者，当永葆由衷的敬意。"},
                {"en": "The registrar verified her enrollment credentials with meticulous attention to detail.", "cn": "教务长以一丝不苟的严谨态度，逐项审核确认了她的正式入学注册凭证。"},
                {"en": "Lifelong learners understand that everyone we meet is our teacher in some respect.", "cn": "终身学习者心里深知：在漫长人生道路上相遇的每一个人，在某些领域皆是我们的良师。"},
                {"en": "Inquire with genuine humility and listen with attentive mindfulness.", "cn": "带着由衷的谦逊去求索问询，以全神贯注的心境去倾听他人的真知灼见。"}
            ]
        },
        {
            "title": "第 5 课 · How are you today? · 晨间问候与身体康泰关切",
            "description": "寒暄身体状况、分享就医叮嘱与互致温暖关怀。",
            "sentences": [
                {"en": "Good morning, Mr. Blake! How are you feeling today?", "cn": "早上好，布莱克先生！请问您今天身体感觉怎么样？"},
                {"en": "I am very well today, thank you; and how are you?", "cn": "我今天感觉十分硬朗矍铄，多谢您的挂念；您近来一切可好？"},
                {"en": "I'm fine too, though my voice is slightly raspy from a seasonal cold.", "cn": "我也挺好的，虽然因为换季偶感风寒，嗓音略微有些沙哑低沉。"},
                {"en": "A warm morning greeting sets an optimistic tone for the entire working day.", "cn": "一句温馨洋溢的清晨问候，能为整个繁忙的工作日奠定积极乐观的精神基调。"},
                {"en": "Remember to drink plenty of warm water when recovering from illness.", "cn": "在抱恙休养恢复期间，切记要多饮温开水以润肺利咽。"},
                {"en": "Inquiring about someone's wellbeing expresses genuine human compassion.", "cn": "由衷关切询问他人的身体健康状况，是彰显人性慈悲与温情的最真挚流露。"},
                {"en": "The pharmacist recommended rest, herbal tea, and peaceful sleep.", "cn": "药剂师由衷建议他近期应当多卧床歇息，饮用草本花茶并保持宁静睡眠。"},
                {"en": "Wellness is the essential foundation upon which all daily productivity rests.", "cn": "充沛健康的体魄与精神风貌，乃是支撑一切日常工作效率的最根本基石。"},
                {"en": "She offered her colleague a steaming mug of honey lemon water.", "cn": "她贴心地为抱恙的同侪递上一大杯热气腾腾、清香扑鼻的蜂蜜柠檬温水。"},
                {"en": "Listen attentively when someone confides their physical discomfort.", "cn": "当身边有人向你坦诚倾诉其身体的不适与疲惫时，请务必用心专注倾听。"},
                {"en": "Fresh autumn air and brisk walks contribute greatly to mental restoration.", "cn": "金秋时节清冽的新鲜空气与大步漫步，极大有助于抚平心智焦虑与重获生机。"},
                {"en": "Take time to nurture your body before exhaustion takes its heavy toll.", "cn": "在身体因过度透支而轰然崩溃之前，请务必留出充足的闲暇时间调养身心。"},
                {"en": "A supportive workplace environment values the holistic health of every individual.", "cn": "一个充满关怀包容的理想工作氛围，必定将每一个个体的身心综合健康置于首位。"},
                {"en": "Gentle inquiries about health demonstrate that we view peers as people first.", "cn": "对同僚健康的柔声关切昭示着：我们首先将彼此视作有血有肉的人，而非冰冷工具。"},
                {"en": "May vitality and serene peace accompany your steps throughout the week.", "cn": "愿蓬勃充沛的生命生机与祥和宁静的心境，陪伴你从容走过这整整一周的岁月。"}
            ]
        },
        {
            "title": "第 6 课 · Is this your shirt? · 纯白衬衫与衣物归属辨析",
            "description": "洗衣房取衣、辨析颜色尺码与衣着穿搭讲究。",
            "sentences": [
                {"en": "Is this white shirt yours, or does it belong to your brother?", "cn": "请问这件纯白色的纯棉衬衫是您的，还是属于您亲哥哥的？"},
                {"en": "No, it is not mine; mine has pearlescent blue buttons on the cuffs.", "cn": "不，这绝不是我的；我那件衬衫的袖口上镶嵌着晶莹剔透的珠光蓝色纽扣。"},
                {"en": "Whose tie is that lying draped over the back of the dining chair?", "cn": "随意搭在餐厅高背椅靠背上的那条真丝领带究竟是谁的？"},
                {"en": "It belongs to my father; he wore it to the formal banquet yesterday.", "cn": "那是属于我父亲的；他昨天正是系着那条领带出席了隆重盛大的正式晚宴。"},
                {"en": "Paying close attention to wardrobe details reflects personal tidiness.", "cn": "对日常衣橱穿搭细节的悉心打理，生动映照出一个人的自律修养与整洁品格。"},
                {"en": "Distinguishing possessive pronouns is crucial for accurate English expression.", "cn": "精确辨析各类物主代词的用法，是实现严谨准确英语日常表达的关键枢纽。"},
                {"en": "She ironed the crisp cotton collar with meticulous precision.", "cn": "她以极其细致熟练的熨烫技法，将那挺括的纯棉衬衫衣领熨烫得平整如新。"},
                {"en": "Keep clean garments neatly folded inside the wooden wardrobe drawers.", "cn": "将洗涤干净的贴身衣物细心叠放整齐，稳妥收纳在实木衣柜的抽屉深处。"},
                {"en": "Color coordination conveys professionalism in business and academic settings.", "cn": "和谐考究的色彩搭配协调，能在商务社交与学术殿堂中传递出非凡的专业风范。"},
                {"en": "He double-checked the laundry receipt before leaving the dry cleaner.", "cn": "在迈步跨出干洗店大门之前，他仔细复核了手中的取衣凭证单据编号。"},
                {"en": "Proper care prolongs the durability and visual beauty of fine fabrics.", "cn": "科学得当的日常洗涤养护，能够极大延长上乘面料的经久耐用度与光泽质感。"},
                {"en": "Label personal attire clearly during school residential camps.", "cn": "在参加学校寄宿集训营期间，务必在个人随身衣物标签上清晰标注好自己的名字。"},
                {"en": "An organized wardrobe saves valuable time during hurried weekday mornings.", "cn": "井井有条、分类明晰的衣橱收纳，能在匆忙紧凑的工作日清晨为你节省宝贵光阴。"},
                {"en": "Dressing with thoughtful dignity demonstrates respect for those you meet.", "cn": "着装得体大方、举止优雅端庄，乃是对你所遇见的每一个人最直接的无声尊重。"},
                {"en": "Orderliness in small material things mirrors inner mental tranquility.", "cn": "在微小物质器物整理上所展现出的条理性，恰恰折射出一个人内心的笃定安详。"}
            ]
        },
        {
            "title": "第 7 课 · A quiet afternoon · 客厅静谧下午茶与家庭相册",
            "description": "家庭客厅茶叙、翻阅老旧相册与追忆往昔岁月。",
            "sentences": [
                {"en": "The afternoon sunlight filtered softly through the lace parlor curtains.", "cn": "午后的金色阳光透过客厅素雅的蕾丝窗纱，轻柔斑驳地洒在地板地毯之上。"},
                {"en": "Would you care for a cup of Earl Grey tea with milk and sugar?", "cn": "请问您想来上一杯调配了香浓牛奶与方糖的经典格雷伯爵红茶吗？"},
                {"en": "Yes, please; hot tea is delightful on such a crisp autumn afternoon.", "cn": "太好了请务必给我来一杯；在这样凉风习习的清爽秋日午后，热茶最为暖心怡人。"},
                {"en": "She brought down the leather-bound family album from the attic bookshelf.", "cn": "她特意从阁楼书架最高处取下了那本沉甸甸、用小牛皮装订的厚重家庭相册。"},
                {"en": "Old black-and-white portraits capture the quiet grace of departed ancestors.", "cn": "泛黄古旧的黑白全家福肖像，深情定格记录下了逝去先辈们那一抹沉静高雅的风骨。"},
                {"en": "Grandmother smiled as she pointed out her childhood home by the coast.", "cn": "祖母脸上浮现出温暖怀恋的笑靥，指尖深情抚过照片里她儿时依山傍海的故居小木屋。"},
                {"en": "Afternoon tea served as a sacred pause in the bustling rhythm of British life.", "cn": "考究正统的英式下午茶，曾是英国人繁忙喧嚣生活节奏之中不可或缺的灵性休憩。"},
                {"en": "Porcelain cups clinked gently against matching saucers during the conversation.", "cn": "在轻声细语的推心置腹闲聊间，细腻的骨瓷茶杯同配套托盘发出清脆悦耳的微响。"},
                {"en": "Preserving generational memories binds families together across shifting decades.", "cn": "悉心守护并传承家族代际间的温存记忆，能将四散的亲人在变迁流年中紧密相系。"},
                {"en": "He listened spellbound to tales of wartime resilience and neighborly charity.", "cn": "他听得如痴如醉出神，完全沉浸在长辈讲述的战时坚韧互助与邻里仁爱传奇故事之中。"},
                {"en": "Photographs freeze time, yet love continues to grow through every recollection.", "cn": "摄影镜头固然将流金岁月彻底冰封定格，然而大爱却在每一次重温追忆中生生不息。"},
                {"en": "The mantelpiece clock ticked with steady, comforting reassurance.", "cn": "壁炉上方那座老式自鸣钟发出沉稳有节奏的滴答声响，带给人抚慰心灵的笃定安宁。"},
                {"en": "Hospitality extended with quiet grace makes any modest cottage feel like a sanctuary.", "cn": "以从容典雅风范倾情展现的热情好客，足以让任何朴素农舍都化作温馨的心灵圣殿。"},
                {"en": "Take time to sit quietly with elders and absorb their accumulated wisdom.", "cn": "多抽空静静端坐在家族长辈膝前促膝长谈吧，去用心汲取他们毕生积淀的处世智慧。"},
                {"en": "Cherish peaceful afternoons where conversation flows without hurry or pretense.", "cn": "用心珍视那些谈吐间毫无浮躁催促、毫无虚伪矫饰，唯有真情流淌的静谧午后时光。"}
            ]
        },
        {
            "title": "第 8 课 · Which glass? · 斟满威士忌与酒杯选择的艺术",
            "description": "餐后小酌、挑选合适玻璃杯与款待挚友佳客。",
            "sentences": [
                {"en": "Which glass should I use to serve this aged Scottish single-malt whisky?", "cn": "请问我究竟应当选用哪一只特制酒杯，来盛倒这款陈年苏格兰单一麦芽威士忌？"},
                {"en": "Please hand me the heavy crystal tumbler on the middle cabinet shelf.", "cn": "劳驾请把摆放在餐边酒柜中间隔板上的那只厚重雕花水晶古典杯递给我。"},
                {"en": "This tall slender glass is meant for sparkling mineral water or lemonade.", "cn": "这只高挑纤细的平底玻璃高脚杯，是专门用来盛放含气矿泉水或鲜榨柠檬水的。"},
                {"en": "A courteous host knows how to select the proper vessel for each beverage.", "cn": "一位体贴周到的优雅东道主，必定深谙如何为每一款佳酿饮品挑选最为契合的器皿。"},
                {"en": "Clinking glasses in celebration cements lasting bonds between true companions.", "cn": "在推杯换盏的欢声笑语中举杯相庆，能将知心挚友之间的深厚情谊锤炼得坚如磐石。"},
                {"en": "He poured a modest measure and held the amber liquid against the candle flames.", "cn": "他克制地斟出适量美酒，将杯中泛着璀璨琥珀色光泽的佳酿举向摇曳的烛光审视。"},
                {"en": "Moderation in spirits ensures that evening fellowship remains delightful.", "cn": "适量微醺、浅尝辄止的饮酒节制，方能确保夜色中的老友雅聚自始至终愉悦尽兴。"},
                {"en": "The clear chime of lead-free crystal resonated across the polished mahogany table.", "cn": "无铅水晶玻璃器皿发出的清脆悦耳鸣响，在打磨光亮的红木餐桌上方悠扬回荡。"},
                {"en": "Etiquette around dining reveals a culture's reverence for companionship.", "cn": "环绕在餐桌杯盘之间的细腻待客礼仪，深刻揭示出一个文化对人际温存陪伴的敬畏。"},
                {"en": "She placed decorative paper coasters beneath every glass to protect the wood.", "cn": "她细致地在每一只玻璃杯底下都垫上了一枚雕花防烫纸质杯垫，以呵护实木桌面。"},
                {"en": "Good vintage drinks taste superior when enjoyed in appreciative, unhurried company.", "cn": "陈年佳酿唯有在懂酒、从容不迫的知己同好相伴品鉴之下，方能迸发出最醇厚风味。"},
                {"en": "Raise your glass in honor of friendship that survives time and distance.", "cn": "让我们高举酒杯，由衷致敬那份跨越流金岁月洗礼与万水千山阻隔依然长青的莫逆友谊！"},
                {"en": "Each glass design serves an aerodynamic purpose in releasing subtle aromas.", "cn": "每一款酒杯形态弧度的巧妙设计，都在空气动力学上为了聚拢释放微妙酒香而服务。"},
                {"en": "The art of hospitality lies in anticipating the comfort of your guests.", "cn": "东方与西方待客之道的终极最高艺术，全在于设身处地提前为来宾的舒适周全着想。"},
                {"en": "Sip slowly, savor deeply, and cultivate gratitude for good cheer and fellowship.", "cn": "细细小口啜饮，深深用心品味；常怀感恩之心，去拥抱欢聚时分所洋溢的真纯友善。"}
            ]
        },
        {
            "title": "第 9 课 · Don't drop it! · 厨房易碎瓷盘与家务协作叮嘱",
            "description": "餐后洗碗清理、传递名贵瓷器与家庭日常安全提醒。",
            "sentences": [
                {"en": "Be extremely careful with that porcelain serving platter; don't drop it!", "cn": "端拿那只名贵的大号骨瓷餐盘时务必打起十二分精神；千千万万莫要失手摔碎了！"},
                {"en": "Don't worry, mother; I am gripping it firmly with both oven mitts.", "cn": "您大可放宽心母亲；我这双手戴着隔热棉手套，早已稳稳将它抓牢抱紧了。"},
                {"en": "Where should I stack these delicate teacups after drying them thoroughly?", "cn": "在用干布将这些精致娇贵的茶杯彻底擦拭干爽之后，我究竟应当将它们码放在何处？"},
                {"en": "Place them gently inside the glass-fronted cabinet on the top shelf.", "cn": "请将它们极其轻手轻脚地摆放进那台玻璃推门实木橱柜的最上层储物隔板里。"},
                {"en": "Household chores become joyful when shared cooperatively by the whole family.", "cn": "当阖家老小同心协力分工协作料理家务琐碎时，平淡的劳作亦能化作欢声笑语。"},
                {"en": "Clear communication in a bustling kitchen prevents accidents and breakages.", "cn": "在锅碗瓢盆忙乱的厨房重地中保持沟通明晰，能够有效规避意外滑落磕碰与损坏。"},
                {"en": "She dried the vintage soup tureen with a lint-free linen cloth.", "cn": "她拿起一块不掉毛絮的纯亚麻洗碗布，细心擦拭着那只祖传的古典雕花大汤盅。"},
                {"en": "Handle heirlooms with reverent mindfulness, honoring the hands that held them before.", "cn": "以虔诚敬畏的心境轻柔摩挲传家器物吧，由衷致敬昔日曾深情抚弄过它们的先辈双手。"},
                {"en": "He swept the kitchen tile floor clean of every stray crumb and droplet.", "cn": "他手持扫帚将厨房的地砖地面彻底清扫得干干净净，不留半点散落的面包屑与水渍。"},
                {"en": "A well-maintained kitchen reflects an orderly, harmonious domestic lifestyle.", "cn": "一间被收拾得井井有条、一尘不染的洁净厨房，生动折射出主家和谐自律的生活品格。"},
                {"en": "Teach children practical responsibility through age-appropriate domestic tasks.", "cn": "通过分配合适年龄段的寻常家务杂务，潜移默化培养孩子受用一生的独立担当精神。"},
                {"en": "Praise careful effort to encourage confidence in young family helpers.", "cn": "对家中年幼小帮手们小心翼翼付出的勤勉努力多加由衷赞赏，能够极大树立其自信心。"},
                {"en": "The warm steam rising from the soapy sink brought cozy domestic comfort.", "cn": "洗碗水槽中升腾而起的带着肥皂清香的温润水汽，营造出一派温馨惬意的居家乐趣。"},
                {"en": "Cooperation at home strengthens the unspoken bonds of mutual affection.", "cn": "在家庭屋檐下守望相助的默契协同，能将亲人之间无言的心灵纽带锻造得愈发坚韧。"},
                {"en": "May every home be a peaceful sanctuary where care and safety reign supreme.", "cn": "祈愿天底下每一个平凡的家园，都能化作一座关怀备至、平安喜乐永驻的心灵港湾。"}
            ]
        },
        {
            "title": "第 10 课 · Goodbye and thanks · 告别晚宴与诚挚感激之辞",
            "description": "晚宴告辞、感谢盛情款待与互道珍重期盼重逢。",
            "sentences": [
                {"en": "Thank you for a truly magnificent evening; the dinner was delicious.", "cn": "万分感谢您今夜为我们呈现的如此美妙绝伦的晚宴盛宴；每一道佳肴都美味至极。"},
                {"en": "It was our absolute pleasure to have you; thank you for coming.", "cn": "能够邀得您阖府光临寒舍，实在是我们至高无上的荣幸；感谢您的欣然赴约。"},
                {"en": "We must be leaving now; it is getting late and tomorrow is a busy workday.", "cn": "我们此刻不得不依依惜别起身告辞了；夜色已深，明日又将迎来紧凑忙碌的工作日。"},
                {"en": "Please give our warmest regards to your parents when you arrive home.", "cn": "在您平安抵家之后，请务必代我们向您的高堂父母转达我们最诚挚由衷的亲切问候。"},
                {"en": "Drive safely along the country roads; the night fog is gathering quickly.", "cn": "沿着乡间曲折小道驱车夜行务必注意安全；夜幕下的浓重夜雾正在迅速蔓延汇聚。"},
                {"en": "Parting words should be spoken with heartfelt sincerity and gratitude.", "cn": "告别离席时的叮咛致意之词，应当发自肺腑、洋溢着最真挚由衷的感激与温存。"},
                {"en": "They exchanged warm embraces on the front porch under the amber porch light.", "cn": "在门廊前那一盏散发着柔和琥珀色微光的廊灯映照下，故友们依依不舍紧紧深情相拥。"},
                {"en": "True hospitality leaves guests feeling deeply valued and spiritually refreshed.", "cn": "真正的待客最高境界，能让每一位归去的宾客都真切感知到自己备受珍视且如沐春风。"},
                {"en": "He buttoned his winter trench coat against the brisk midnight air.", "cn": "他迎着午夜清冽刺骨的凉风，将身上的深冬风衣排扣一颗颗扣紧御寒。"},
                {"en": "Fond memories of shared meals linger long after the feast concludes.", "cn": "同席共餐推杯换盏所留下的温馨余韵，在晚宴落幕曲终人散后依旧长久流淌在心头。"},
                {"en": "Keep the light on until the departing guests have driven safely out of the lane.", "cn": "在离席的贵客彻底驾车安全驶出悠长小巷之前，请长久保留门前的那一盏守望路灯。"},
                {"en": "Reciprocal invitations sustain deep social bonds between cherished households.", "cn": "家家户户之间你来我往、礼尚往来的真诚回请，让挚友莫逆之交在流年中历久弥坚。"},
                {"en": "Expressing appreciation for hospitality is a fundamental hallmark of high culture.", "cn": "对主人倾注的心血与盛情款待由衷表达深切感激，是衡量一个人崇高教养的基本标尺。"},
                {"en": "Until we meet again, may peace and prosperity dwell within your household.", "cn": "在后会有期、再次欢聚重逢之前，祈愿福绥与康泰永远充盈驻留在您温馨的府邸深处。"},
                {"en": "Goodbye for now; safe journeys and goodnight to all our dear friends.", "cn": "暂且互道一声珍重道别吧；祝一路顺风平安顺遂，向我们所有亲爱的挚友道一声晚安好梦。"}
            ]
        }
    ]
    courses.append(build_course(nce1_meta, nce1_chapters))
    
    # -------------------------------------------------------------------------
    # 2. 新概念英语第二册 (10章)
    # -------------------------------------------------------------------------
    nce2_meta = {
        "id": "course-tb-nce2",
        "title": "《新概念英语第二册》(NCE 2) · 经典故事与英美文化叙事 (10章全集)",
        "category": "textbook",
        "categoryName": "教材同步",
        "coverGradient": "from-indigo-600 via-blue-700 to-sky-600",
        "icon": "📖",
        "description": "亚历山大原版传世经典，通过诙谐幽默故事与严谨语法构架，彻底突破中级英语门槛。",
        "difficulty": "初级进阶 A2",
        "tags": ["新概念二册", "亚历山大", "经典叙事", "语法骨架"]
    }
    nce2_chapters = [
        {
            "title": "第 1 课 · A Private Conversation · 戏院包厢私语与怒斥无礼看客",
            "description": "在剧院包厢遭遇大声喧哗，忍无可忍愤怒斥责却遭遇滑稽反转。",
            "sentences": [
                {"en": "Last week I went to the theatre; I had a very good seat.", "cn": "上个星期我去剧院看了一场戏；我买到的戏票座位相当不错。"},
                {"en": "The play was very interesting, but I did not enjoy it at all.", "cn": "舞台上上演的剧目十分扣人心弦引人入胜，然而我却自始至终丝毫没有享受到看戏的乐趣。"},
                {"en": "A young man and a young woman were sitting behind me.", "cn": "有一位年轻小伙子和一位妙龄年轻女子，当时恰巧就端坐在我的正后方席位上。"},
                {"en": "They were talking loudly; I got very angry because I could not hear the actors.", "cn": "他们一直在肆无忌惮大声交头接耳；这让我怒火中烧，因为嘈杂的私语让我根本听不清台上演员在讲什么。"},
                {"en": "I turned round and looked at them angrily, but they did not pay any attention.", "cn": "我气愤地猛然转过头狠狠瞪了他们一眼，然而他们却置若罔闻，根本不予理会。"},
                {"en": "In the end, I could not bear it any longer; I turned round again.", "cn": "到了最后我实在忍无可忍，憋了一肚子火气的我再次猛然转过身去。"},
                {"en": "I can't hear a word! I said angrily.", "cn": "“我连台上演员讲的一个字都听不清了！”我强压着怒火厉声抗议道。"},
                {"en": "It's none of your business, the young man said rudely; this is a private conversation!", "cn": "“这关你屁事，用得着你在这多管闲事吗？”那个无礼小伙子竟蛮横反诘道，“我们现在正在进行的是私人谈话！”"},
                {"en": "Theater etiquette demands silence so that the audience may immerse in the drama.", "cn": "正统的剧院观剧礼仪要求全场保持肃静，以便全体观众都能沉浸在舞台戏剧张力之中。"},
                {"en": "Humorous misunderstandings often arise from conflicting perspectives on shared public space.", "cn": "令人啼笑皆非的荒诞误解，往往肇始于人们在共享公共空间维权认知上的戏剧性错位。"},
                {"en": "Irony serves as the primary literary device propelling this celebrated opening narrative.", "cn": "充满英伦黑色幽默的讽刺反转，作为核心文学修辞手法，有力驱动着这篇名篇的叙事推进。"},
                {"en": "Consideration for fellow patrons distinguishes refined behavior in civil society.", "cn": "设身处地为身旁的同场观众着想，是区分一个人在现代文明社会中是否具备优雅修养的试金石。"},
                {"en": "The absurdity of claiming private conversation in a crowded theater delighted generations of readers.", "cn": "在座无虚席的公共戏院里大言不惭宣称自己在进行私人私语的滑稽荒谬，逗乐了一代又一代的英语学子。"},
                {"en": "Mastering past continuous and simple past contrasts begins with this lively anecdote.", "cn": "熟练掌握过去进行时态与一般过去时态的精妙对撞，正是从品读这则生动有趣的轶事正式拉开序幕。"},
                {"en": "Always respect the shared auditory environment of artistic performance spaces.", "cn": "请务必时刻尊重公共艺术演出场馆内那份需要所有人共同用心守护的纯净声学环境。"}
            ]
        },
        {
            "title": "第 2 课 · Breakfast or Lunch? · 彻夜长眠至正午与周末早餐之惑",
            "description": "周末睡懒觉至正午，面对姑母来电误将午餐当早餐的诙谐幽默。",
            "sentences": [
                {"en": "It was Sunday; I never get up early on Sundays.", "cn": "那天恰逢星期日；在慵懒的星期天里，我从来都是习惯睡大觉、绝不早起的。"},
                {"en": "I sometimes stay in bed until lunchtime on leisurely weekends.", "cn": "在从容不迫的悠闲周末假期里，我有时甚至甘愿一直赖床赖到正午吃午饭的光景。"},
                {"en": "Last Sunday I got up very late; I looked out of the window.", "cn": "上个星期天我起床起得格外晚；我打着哈欠懒洋洋地举目望向窗外的大街。"},
                {"en": "It was dark outside; 'What a day!' I thought, 'It is raining again.'", "cn": "窗外的天色显得异常阴暗昏沉；“这见鬼的鬼天气！”我暗自咕哝道，“怎么天又在下暴雨了。”"},
                {"en": "Just then, the telephone rang; it was my aunt Lucy.", "cn": "恰在此时，客厅里的电话铃声突兀急促地大作起来；来电的原是我的亲姑母露西。"},
                {"en": "I've just arrived by train, she said; I'm coming to see you.", "cn": "“我刚乘长途火车抵达城里，”她在听筒那头热络宣称道，“我眼下正动身前往探望你呢。”"},
                {"en": "But I'm still having breakfast, I said in sleepy bewilderment.", "cn": "“可是我眼下还在吃早点呢，”我顶着一头蓬乱鸡窝头、睡眼惺忪困惑不解地回答道。"},
                {"en": "What are you doing? she asked; I'm having breakfast, I repeated.", "cn": "“你刚才说你在干什么？”她惊讶拔高声调追问道；“我正在吃早饭呢，”我耐着性子再次重复了一遍。"},
                {"en": "Dear me, she said, do you always get up so late? It's one o'clock in the afternoon!", "cn": "“天哪我的小祖宗，”她失声惊呼道，“你难道天天都起得这般晚吗？现在明明都已经是下午一点大中午了！”"},
                {"en": "Losing track of time during deep restorative sleep is a universal weekend indulgence.", "cn": "在深沉解乏的酣睡中彻底丧失了对时间流逝的感知，乃是全世界打工人共同的心灵周末放纵。"},
                {"en": "The clash between generational punctuality and youthful languor generates charming comedic relief.", "cn": "老一辈人刻板守时的晨起习惯，同青年一辈晚起慵懒习性的激烈碰撞，催生了妙趣横生的喜剧色彩。"},
                {"en": "British weather often blurs the boundary between morning dawn and gloomy twilight.", "cn": "英伦三岛那阴沉多雨的多变气候，常常模糊了清晨曙光同萧索黄昏之间的清晰界线。"},
                {"en": "Contrast between present continuous actions and habitual states is clearly demonstrated.", "cn": "正在进行的动作表述同生活常态习惯之间的语法对比，在这篇小品文中得到了淋漓尽致的典范呈现。"},
                {"en": "Cherish peaceful weekend mornings where the clock ceases to dictate your waking breath.", "cn": "用心珍视那些闹钟指针再也无法左右支配你呼吸起卧节律的宁静周末清晨吧。"},
                {"en": "A late breakfast savored without hurry remains one of life's simplest, purest joys.", "cn": "一顿无需赶时间、由着性子细嚼慢咽的迟到早午餐，永远是平凡岁月里最朴实纯粹的人生至乐。"}
            ]
        },
        {
            "title": "第 3 课 · Please Send Me a Card · 意大利炎夏旅居与明信片心结",
            "description": "旅居意大利卡普里岛，整日受寄明信片心魔折磨的旅途烦恼。",
            "sentences": [
                {"en": "Postcards always spoil my holidays; last summer, I went to Italy.", "cn": "寄明信片这档子琐事，总会在不知不觉中彻底搅黄破坏掉我的整个美好假期；去年盛夏，我启程前往意大利旅居度夏。"},
                {"en": "I visited museums and sat in public gardens with great delight.", "cn": "在那里我流连忘返参观了无数世界级的历史艺术博物馆，满怀惬意地在市民花园的绿荫长椅上流连休憩。"},
                {"en": "A friendly waiter taught me a few words of Italian every morning.", "cn": "每天清晨在街角咖啡馆里，一位面带亲切笑容的友善侍应生，总会热心教我说上几句地道的意大利日常俚语。"},
                {"en": "Then he lent me a little book; I read a few lines, but I did not understand a word.", "cn": "后来他好心借给我一本薄薄的意大利语入门小册子；我硬着头皮读了区区几行，结果发现自己根本一个字也看不懂。"},
                {"en": "Every day I thought about postcards; my holidays passed quickly, but I did not send any cards to my friends.", "cn": "旅途中的每一天我都在为还没寄明信片而焦虑心焦；假期时光如白驹过隙飞速溜走，可我却自始至终连哪怕一张卡片都未曾寄出。"},
                {"en": "On the last day I made a big decision; I got up early and bought thirty-seven postcards.", "cn": "在假期的最后一天我咬紧牙关做出了一个重大决断；我破天荒起了一个大早，一口气豪气买下了整整三十七张风景明信片。"},
                {"en": "I spent the whole day in my room, but I did not write a single line.", "cn": "我把自己关在昏暗逼仄的旅馆房间里苦坐硬憋了整整一整天，最终却连哪怕一行字也未能写得出来！"},
                {"en": "In the end, I wrote thirty-seven cards with a simple signature: 'Greetings from Capri.'", "cn": "到了最后精神崩溃的我，索性给这三十七张卡片统统草草签上了千篇一律的一句话：“卡普里岛致意，祝安。”"},
                {"en": "Obligation often casts an unnecessary shadow over the spontaneous joy of travel.", "cn": "外界人情世故的无形道德义务枷锁，常常会给一场本该随性潇洒的漫游之旅平添沉重无谓的心灵阴霾。"},
                {"en": "The ritual of sending vacation postcards captured the nostalgic texture of pre-digital travel.", "cn": "在邮筒前亲手投递手写明信片的仪式感，完美定格记录下了前数字化时代远洋漫游的复古质感。"},
                {"en": "Procrastination turns delightful friendly gestures into agonizing administrative burdens.", "cn": "无休止的拖延症恶疾，往往能轻而易举将原本充满温情善意的人际问候，异化沦为痛苦折磨的沉重心理负担。"},
                {"en": "Capri's azure waters and dramatic limestone cliffs deserved unhurried contemplation.", "cn": "卡普里岛那汪湛蓝澄澈的碧海波涛与刀削斧劈般的壮美石灰岩绝壁，本该得到旅人从容不迫的深情凝眸凝望。"},
                {"en": "Simple past irregular verb forms are beautifully demonstrated throughout this honest travelogue.", "cn": "不规则动词的一般过去时态变化形式，在这篇真诚坦率、充满自嘲的旅行手记中得到了绝妙展现。"},
                {"en": "Travel to enrich your own soul rather than merely to satisfy external social expectations.", "cn": "去漫游远方是为了滋养升华你自己的精神灵魂，而绝非仅仅为了满足取悦外界世俗的社交期许。"},
                {"en": "True friends appreciate your safe return far more than a rushed cardboard souvenir.", "cn": "真正情深义重的莫逆之交，所在乎珍惜的永远是你的平安归来，而非一张仓促盖章的硬纸片纪念品。"}
            ]
        },
        {
            "title": "第 4 课 · An Exciting Trip · 澳洲自驾环游大冒险与兄弟重逢",
            "description": "弟弟来信讲述驾驶二手车穿越澳大利亚内陆的惊险壮游。",
            "sentences": [
                {"en": "I have just received a letter from my brother, Tim.", "cn": "我刚刚收到了由我远在重洋之外的亲弟弟蒂姆亲笔寄来的一封厚重航空信札。"},
                {"en": "He is in Australia; he has been there for six months.", "cn": "他目前正身处辽阔的澳大利亚大陆；他在那片广袤的新大陆上定居旅居至今已满整整半年光阴了。"},
                {"en": "Tim is an engineer; he is working for a big mining firm and he has already visited a great number of different places in Australia.", "cn": "蒂姆本身是一名优秀的采矿工程技术专家；他目前效力于一家大型跨国矿业巨头，并已在澳洲各地走访探勘过了无数令人叹为观止的名胜风土。"},
                {"en": "He has just bought an Australian car and has gone to Alice Springs, a small town in the center of Australia.", "cn": "他最近刚在当地购置了一辆结实皮实的二手澳式越野汽车，眼下已然马不停蹄长途自驾深入到了位于澳洲红色心脏腹地的小镇爱丽斯泉。"},
                {"en": "He will soon visit Darwin; from there, he will fly to Perth, my brother has never been abroad before, so he is finding this trip very exciting.", "cn": "他很快便将北上寻访达尔文港；随后将从那里搭乘航班直飞西南重镇珀斯，我的弟弟昔日从未有过任何跨国远行的经验，因而他发觉这趟壮游简直刺激过瘾到了极点。"},
                {"en": "The Australian Outback challenges travellers with vast distances and extreme wilderness.", "cn": "广袤苍凉的澳大利亚红色内陆荒原，以关山难越的极遥远距离与严酷蛮荒的原始生态，无情考验着每一位探险勇士的胆魄。"},
                {"en": "Letters delivered across continents carried emotional weight in eras before instant messaging.", "cn": "在即时通讯软件尚未问世的纯真年代，一封漂洋过海历经千辛万苦投递而来的厚实家书，承载着万金不换的深沉情感分量。"},
                {"en": "Present perfect tense markers such as 'just', 'already', and 'never' shine brightly here.", "cn": "诸如'just'、'already'与'never'等现在完成时态的核心时间标志副词，在本文的字里行间展现出了极强的语法示范魅力。"},
                {"en": "Driving through Alice Springs brings travelers into direct contact with ancient indigenous cultures.", "cn": "驱车穿行过爱丽斯泉的红色荒原沙土，能让行者同这片古老大地上延续数万年的原住民神圣图腾文明狭路相逢。"},
                {"en": "Youthful adventures beyond familiar borders foster self-reliance and global perspectives.", "cn": "青年时期敢于毅然跨越熟悉舒适区疆界的远征冒险，能极大淬炼出一个人的独立自主生存能力与博大全球视野。"},
                {"en": "Engineering projects in remote terrains demand robust technical resilience and adventurous spirits.", "cn": "在人迹罕至的荒凉极地开展宏大工程建设，向来不仅需要过硬扎实的专业技术功底，更需要敢为人先的无畏冒险精神！"},
                {"en": "He shared photographs of sprawling red sandstone monoliths rising dramatically above the desert plain.", "cn": "他在来信中附寄了多张彩色照片：那是一座座拔地而起、巍峨孤傲屹立在荒凉沙漠戈壁平原之巅的巨大红色砂岩巨石奇观。"},
                {"en": "Family ties remain unbreakable across thousands of miles of ocean and uncharted territory.", "cn": "血浓于水的亲情同胞手足纽带，哪怕跨越数万海里的浩瀚汪洋与未知的险恶蛮荒疆土，历经沧海桑田依然坚不可摧！"},
                {"en": "Embrace the vastness of the natural world whenever the chance to wander arises.", "cn": "每当命运的恩赐赋予你远走高飞浪迹天涯的契机时，只管张开你的双臂，全心全意去拥抱大自然鬼斧神工的辽阔壮美吧！"},
                {"en": "Every adventurous journey undertaken in youth becomes a golden reservoir of strength for adulthood.", "cn": "在年少轻狂岁月里所经历的每一趟披荆斩棘的冒险远征，都必将化作日后步入成年世界时一座取之不尽用之不竭的心灵力量黄金宝库！"}
            ]
        },
        {
            "title": "第 5 课 · No Wrong Turn · 鸽子信使与跨海秘密商业密码",
            "description": "车库老板利用信鸽跨越海峡传递紧急汽车零件密码。",
            "sentences": [
                {"en": "Mr. James Scott has a garage in Silbury and now he has just bought another garage in Pinhurst.", "cn": "詹姆斯·斯科特先生在锡尔伯里镇坐拥一家汽车修理厂，而眼下他刚刚在邻近的平赫斯特镇又盘下并开设了另一家新车库。"},
                {"en": "Pinhurst is only five miles from Silbury, but Mr. Scott cannot get a telephone for his new garage, so he has just bought twelve pigeons.", "cn": "平赫斯特距锡尔伯里两地之间相距不过仅仅五英里之遥，但斯科特先生因电信局线路紧张始终未能为他的新修理厂申请装上电话机，情急之下他索性一口气购置了十二只通人性的信鸽。"},
                {"en": "Yesterday, a pigeon carried the first message from Pinhurst to Silbury.", "cn": "就在昨天，其中一只训练有素的信鸽，成功完成了从平赫斯特向前总店锡尔伯里运送投递第一封紧急信函的重任。"},
                {"en": "The bird covered the distance in three minutes; up to now, Mr. Scott has sent a great many requests for spare parts and other urgent messages from one garage to the other.", "cn": "这只灵动的飞鸟以迅雷不及掩耳之势在区区三分钟内便飞越了整段路程；截止到目前为止，斯科特先生已凭借它们在两家车库之间成功传递了无数批汽车备用零部件采购调拨申请与其它紧急公文。"},
                {"en": "In this way, he has begun his own private 'telephone' service.", "cn": "正是凭借着这手巧夺天工的奇招妙策，他竟然歪打正着创立出了一套独属于他自己名下的私人飞鸽专线通讯网络体系！"},
                {"en": "Homing pigeons have served human communication reliably since ancient antiquity.", "cn": "信鸽凭借其令人惊叹的归巢导航天赋，自上古蛮荒时代起便一直在人类通信历史上扮演着极其可靠的信使神兵角色。"},
                {"en": "Innovative entrepreneurs always discover ingenious workarounds when facing infrastructural shortages.", "cn": "敢想敢干的真正创业先驱，在遭遇外部基础设施短缺瓶颈的严峻考验时，总能凭借非凡巧思寻觅出绝处逢生的破局良方！"},
                {"en": "Present perfect aspect highlights continuous results flowing into current operational success.", "cn": "现在完成时态所蕴藏的语法内涵，生动有力地凸显了过去持续采取的行动成果向当下卓越运营战果的自然流动交汇。"},
                {"en": "Small cylindrical canisters tied securely to avian legs protected confidential orders from rainwater.", "cn": "紧紧绑扎固定在信鸽纤细脚爪之上的微型圆柱铝合金密信金属小筒，万无一失地保护着机密采购订单免受半点风雨雨水浸湿。"},
                {"en": "Resourcefulness triumphs over bureaucratic delays every single time in commercial enterprise.", "cn": "在分秒必争的商业战场竞争中，随机应变的务实智慧，永远都能毫不留情地以绝对压倒性优势战胜傲慢官僚体制的办事拖沓延误！"},
                {"en": "The magnetic orientation abilities of migratory birds continue to astonish modern biophysicists.", "cn": "候鸟体内所蕴藏的利用地磁场精准导航定位的神奇超凡生理机制，时至今日依然让现代生物物理学家们惊叹不已、叹为观止。"},
                {"en": "A low-tech solution executed with precision often outshines costly sophisticated infrastructure.", "cn": "一项被执行落地得严丝合缝、极致精妙的极简低技术解决方案，其最终成效往往反倒能远远艳压那些劳民伤财的昂贵高科技排场！"},
                {"en": "The feathered messengers returned safely to their roost at sunset, awaiting their next dispatch.", "cn": "暮色四合夕阳斜照时分，那些披着整齐羽翼的忠诚飞翔信使们安然归巢栖息在横木之上，静静整装待发静候着下一次破空领命出征。"},
                {"en": "Never underestimate the ancient wisdom encoded in biological partnerships with the animal kingdom.", "cn": "千千万万莫要短视低估了千百年来人类在同大自然动物生灵伙伴休戚与共的跨物种深度协作中所沉淀下的古老智慧瑰宝！"},
                {"en": "Adaptability remains the supreme competitive advantage in an ever-shifting economic landscape.", "cn": "因时制宜、随机应变的敏捷适应力，永远是置身于瞬息万变经济市场大风大浪中立于不败之地的至高核心竞争王牌！"}
            ]
        },
        {
            "title": "第 6 课 · Percy Buttons · 流浪叫花子与独家拉弦琴报恩",
            "description": "老乞丐珀西·巴顿斯三十年如一日乞讨馅饼并拉琴报恩。",
            "sentences": [
                {"en": "I have just moved to a house in Bridge Street; yesterday a beggar knocked at my front door.", "cn": "我前不久刚刚乔迁搬迁到了位于大桥街的一所新居；就在昨天，一位流浪行乞的乞丐突然叩响了我的正门大门。"},
                {"en": "He asked me for a meal and a glass of beer; in return for this, the beggar stood on his head and sang songs.", "cn": "他向我卑微讨要一顿热乎饭菜与一杯解渴的大麦啤酒；而作为知恩图报的回馈，这位老乞丐竟然当场就地倒立拿大顶，并神采飞扬引吭高歌起来。"},
                {"en": "I gave him a meal; he ate the food and drank the beer, then he put a piece of cheese in his pocket and went away.", "cn": "我心生怜悯慨然赠予了他一顿丰盛便饭；他狼吞虎咽风卷残云吃尽了餐食饮尽了啤酒，随后又将一小块硬干酪揣入衣兜，从容扬长而去。"},
                {"en": "Later a neighbor told me about him; his name is Percy Buttons.", "cn": "事后一位热心肠的邻里街坊向我娓娓道出了关于他的传奇底细；他的大名叫作珀西·巴顿斯。"},
                {"en": "He calls at every house in the street once a month and always asks for a meal and a glass of beer.", "cn": "三十年来他每个月必定风雨无阻挨家挨户拜访这条街上的每一座宅邸，而每次所讨要的无一例外全都是一顿饭食与一杯啤酒。"},
                {"en": "Eccentric local personalities become cherished folklore figures in traditional English villages.", "cn": "在传统的英格兰乡绅古朴村镇里，形形色色行事古怪却心地善良的江湖奇人异士，往往会慢慢沉淀为整个社区津津乐道的心灵图腾民间传说。"},
                {"en": "Charity offered without patronizing condescension honors the inherent dignity of vulnerable souls.", "cn": "剥离掉一切居高临下施舍傲慢姿态的纯真慷慨慈善义举，方能真正由衷守护那些落魄受难灵魂底层仅存的人格尊严。"},
                {"en": "Indefinite and definite articles work in seamless harmony to introduce and anchor narrative characters.", "cn": "不定冠词与定冠词的巧妙交替呼应配合，在这篇小说中天衣无缝地完成了对核心叙事角色的惊艳登场引荐与语义锚定巩固。"},
                {"en": "The beggar's performance represented a proud refusal to accept charity entirely empty-handed.", "cn": "老乞丐那看似滑稽的倒立卖艺高歌献礼，恰恰展现出一个底层草民誓死不愿平白无故吃白食、绝不两手空空接受怜悯的高贵傲骨风骨！"},
                {"en": "Reciprocal human transactions can assume delightfully unconventional expressions beyond monetary exchange.", "cn": "人与人之间投桃报李、礼尚往来的温情因果互动，完全能够挣脱世俗冷冰冰的金钱铜臭交易逻辑，化作令人心花怒放的奇妙诗意示现。"},
                {"en": "Neighborhood communities thrive when they accommodate harmless idiosyncrasies with warm amusement.", "cn": "当一个成熟街坊社区懂得怀揣着温暖莞尔的宽容胸襟，去主动包容善待那些人畜无害的市井怪癖癖好时，人间的温情方才真正繁茂生生不息！"},
                {"en": "He folded the remaining cheese carefully inside brown greaseproof paper before heading to the next cottage.", "cn": "在精神抖擞迈向下一家农舍门廊之前，他小心翼翼用深褐色的防油纸将剩余的干酪包裹包裹得严严实实揣入怀中。"},
                {"en": "Traditions born of small domestic routines outlast the shifting rise and fall of grand empires.", "cn": "肇始于民间市井平凡琐碎起居柴米油盐之中的温存风俗惯例，其所蕴藏的生命力之顽强，往往反倒能远远熬过无数豪门显赫帝国的兴衰荣辱！"},
                {"en": "Offer kindness freely to the wanderers who knock unexpectedly upon your threshold in this life.", "cn": "在这短暂仓促的漫漫人世苦旅中，慷慨大度去善待那些毫无预警猝不及防叩响你门扉阶梯的萍水相逢流浪过客吧！"},
                {"en": "For in entertaining solitary strangers, we sometimes welcome unexpected angels into our humble midst.", "cn": "因为古老圣训早已明言：在以诚相待款待孤身一人的异乡陌路穷途之士时，我们往往在不经意间，将上苍暗中派来试炼人心的乔装天使迎入了寒舍之中！"}
            ]
        },
        {
            "title": "第 7 课 · Too Late · 侦探破获飞天大盗与失窃钻石真相",
            "description": "苏格兰场侦探在机场严密布控，识破包裹掉包并截获无价钻石。",
            "sentences": [
                {"en": "The plane was late and detectives were waiting at the airport all morning.", "cn": "那一架由南非直飞而来的国际航班严重晚点延误了，苏格兰场的资深刑侦便衣探员们在机场海关停机坪整整焦灼严阵以待潜伏了一整个上午。"},
                {"en": "They were expecting a valuable parcel of diamonds from South Africa.", "cn": "他们正在高度戒备翘首以待一批由南非钻石矿区直运而至、价值连城的稀世未切割原石巨钻绝密包裹。"},
                {"en": "A few hours earlier, someone had told the police that thieves would try to steal the diamonds.", "cn": "就在短短数小时前，警署曾收到一通绝密急电线报告密称：一个国际跨国飞天神偷犯罪团伙正处心积虑密谋在机场交接环节铤而走险强行截胡窃取这批钻石！"},
                {"en": "When the plane arrived, some of the detectives were waiting inside the main building while others were waiting on the airfield.", "cn": "当涉事客机平稳降落滑入跑道的那一秒，一部分荷枪实弹的探员奉命严密封锁驻守在机场航站楼主航站楼大厅内部，而另一组突击警力则如猎鹰般潜伏在停机坪跑道四周！"},
                {"en": "Two men took the parcel off the plane and carried it into the Customs House.", "cn": "两名身着地勤制服的行李装卸工小心翼翼从机舱腹部卸下了那个特制贵重包裹，快步将它一路护送扛入了海关报关查验大厅深处。"},
                {"en": "While two detectives were keeping guard at the door, two others opened the parcel; to their surprise, the precious parcel was full of ordinary stones and sand!", "cn": "正当两名持枪探员如两尊铁塔般严阵以待扼守在查验室大门两侧警戒之际，另外两名资深鉴识探长当场撕开封条开箱验货；令全场所有人目瞪口呆倒吸一口凉气的是：那只本该盛满稀世粉钻的贵重包裹内部，竟然空空如也，塞得满满当当的尽是些一文不值的寻常碎石与烂沙砾！"},
                {"en": "Undercover security protocols require absolute secrecy to protect high-value transatlantic shipments.", "cn": "针对高价值跨大西洋贵重战略物资押运交接的安全安保特勤条例，在每一个环节都对绝对保密有着近乎严苛到极致的铁血要求。"},
                {"en": "Past perfect tense masterfully establishes the chronology of the criminal conspiracy before police arrival.", "cn": "过去完成时态（had done）的鬼斧神工精妙运用，入木三分地确立理顺了犯罪团伙在警方部署到场前早已暗中金蝉脱壳掉包的缜密时间线逻辑！"},
                {"en": "Professional diamond syndicates operate with military precision across international transit hubs.", "cn": "那些盘踞在暗处作祟的国际顶尖珠宝盗窃跨国财阀大盗，其作案时的战术协同与时间卡点之精准，丝毫不逊色于最正规精锐的特战军团！"},
                {"en": "The detectives realized with cold dread that the diversion had succeeded hours before wheels touched down.", "cn": "几名带队老探长此时此刻脑中如遭雷击、脊背发凉，他们瞬间恍然大悟：对方精心设计的调虎离山李代桃僵暗度陈仓毒计，早在飞机机轮尚未降落触地前数小时便早已大功告成！"},
                {"en": "High-stakes heists demand thorough forensic investigation to uncover insider complicity within airport ground crew.", "cn": "面对这种惊天动地的国际大案要案，必须立即启动最高规格的痕迹刑侦法医全面倒查排查，誓死挖出潜伏在机场地面地勤内部吃里扒外的黑手内鬼同谋！"},
                {"en": "The empty wooden crate bore faint scuff marks around the tamper-evident brass hinges.", "cn": "那只看似完好无损的实木特质空板条箱四周，在防拆卸黄铜合页边缘极隐秘处，依然依稀残留着被极细微特种撬杠撬动破坏过的物理划痕。"},
                {"en": "Constant vigilance remains the only safeguard against sophisticated modern criminal syndicates.", "cn": "在魔高一尺道高一丈的残酷刑侦暗战搏杀之中，时刻紧绷神经的长久戒备与警觉，乃是抵御现代高科技犯罪团伙渗透侵袭的唯一生命防线！"},
                {"en": "Appearances can be deceiving; verify physical evidence before proclaiming operational victory.", "cn": "大千世界表象之下的假象往往最擅长瞒天过海；在向世人宣告大获全胜之前，务必先用无可辩驳的坚实物理铁证验明正身！"},
                {"en": "Justice may experience frustrating temporary setbacks, but relentless pursuit eventually closes the net.", "cn": "正义的伸张在破案追凶征程中有时难免会遭遇令人扼腕叹息的暂时挫败挫折，但天网恢恢疏而不漏，持之以恒的铁血追击终将把狂徒彻底绳之以法！"}
            ]
        },
        {
            "title": "第 8 课 · The Best and the Worst · 乡村后花园竞赛与邻里幽默",
            "description": "每年村里评选最美花园，乔的菜园年年垫底却乐在其中。",
            "sentences": [
                {"en": "Joe Sanders has the most beautiful garden in our town.", "cn": "在我们这座风景如画的英格兰小镇上，乔·桑德斯先生拥有一座名动四方、公认全镇最美艳绝伦的私人后花园。"},
                {"en": "Nearly everybody enters for 'The Nicest Garden Competition' each year, but Joe wins every time.", "cn": "每逢一年一度暮春盛夏时节，镇上几乎全镇家家户户的园艺好手都会踊跃报名竞逐“全镇最佳花园桂冠大奖赛”，然而乔每一次都能毫无争议蝉联拔得头筹。"},
                {"en": "Bill Frith's garden is larger than Joe's; Bill works harder than Joe and grows more flowers and vegetables, but Joe's garden is more interesting.", "cn": "同村比尔·弗里斯的花园在物理占地面积上其实比乔的大得多；比尔在田间地头付出的汗水与辛劳也远比乔更为勤勉卖力，他培植出的鲜花与果蔬产量更是压倒性胜出，然而乔的花园在造景艺术意境上却远比比尔的更为生动有趣、引人入胜。"},
                {"en": "He has made neat paths and has built a wooden bridge over a pool.", "cn": "他在繁花掩映深处精心铺砌出了几条蜿蜒整洁的青石小径，并在波光粼粼的荷花锦鲤池塘上方匠心独运架设了一座雅致的弧形纯木拱桥。"},
                {"en": "I like gardens too, but I do not like hard work; every year I enter for the garden competition too, and I always win a little prize for the worst garden in the town!", "cn": "我平生骨子里也极度热爱花园绿意，但我打心眼里却打死也不愿去面朝黄土背朝天吃苦流汗干重活；因此每年我也照例没脸没皮跑去报名参加这场花园争霸赛，而其最终结果也向来十分稳定：我每年都能稳稳抱回一座全镇官方认证评选出的“最烂最糟花园奖”专属特别纪念小奖杯！"},
                {"en": "Comparative and superlative forms of adjectives are celebrated through this hilarious community rivalry.", "cn": "形容词比较级与最高级的系统语法规律与妙用，在这场令人捧腹开怀的小镇邻里园艺争锋记叙中得到了极其华美精妙的展现！"},
                {"en": "Landscape design transcends mere agricultural abundance through aesthetic harmony and compositional balance.", "cn": "真正的顶级庭园造景景观艺术，绝非单纯取决于农副作物产量的简单堆砌，而是藉由美学上的比例调和与构图意境的浑然天成实现超凡脱俗！"},
                {"en": "Healthy competition fosters neighborhood pride and transforms routine gardening into shared community art.", "cn": "充满善意幽默的良性民间赛事较量，不仅极大激发培育了邻里街坊的家园自豪感，更将枯燥乏味的日常侍弄花草升华为全社区共享的精神艺术盛宴！"},
                {"en": "Self-deprecating wit enables people to celebrate their limitations with cheerful humility.", "cn": "高级的自嘲幽默智慧，能让一个人以豁达开朗、童叟无欺的谦逊姿态，去坦然拥抱并大方庆祝自己技不如人的凡庸小缺点。"},
                {"en": "The wooden footbridge reflected gracefully in the still waters, surrounded by climbing English roses.", "cn": "那座古朴清雅的木质小拱桥，在平静如镜的水面上投下优雅的倒影，四周被攀藤缠绕、吐露芬芳的英国古典月季团团簇拥。"},
                {"en": "Gardening requires an exquisite dialogue between human patience and the natural rhythm of soil and seasons.", "cn": "园艺之道，本质上是人类耐心的持久坚守与大地泥土芬芳以及四时节气更迭规律之间展开的一场极度深情高雅的心灵对话。"},
                {"en": "Winning the wooden spoon prize with a cheerful grin demonstrates a truly admirable sense of proportion.", "cn": "能够满面春风、咧嘴欢笑去大方登台认领“垫底倒数第一名”的安慰奖，展现出一个人对人世间虚名得失极其超脱清醒、难能可贵的通透豁达！"},
                {"en": "Cultivating soil with love brings peace to restless urban minds weary of artificial complexities.", "cn": "怀揣着对生命的深情去躬身耕耘泥土培植芳草吧，它能为那些早已厌倦了现代都市虚浮矫饰的躁动疲惫心智，带去洗尽铅华的终极心灵安宁。"},
                {"en": "Beauty exists not only in pristine symmetry, but in the wild, unkempt corners that make us laugh.", "cn": "天地间的真美，绝不仅唯独存在于被修剪得无可挑剔的对称盆景之中；在那些杂草丛生、令人忍俊不禁的荒唐狂野角落里，同样盛开着未经雕琢的纯真生命奇迹！"},
                {"en": "May your own inner garden bloom with effortless joy, whether crowned champion or cherished jester.", "cn": "祈愿你内心深处的那座精神花园，亦能永远无拘无束自在绽放，不论有朝一日是加冕为独占鳌头的王者，亦或甘当为世人博得一笑的快乐弄臣！"}
            ]
        },
        {
            "title": "第 9 课 · A Cold Welcome · 大本钟新年倒计时停摆与寒风惊魂",
            "description": "除夕夜在大本钟下守岁倒计时，大钟停摆却未敲响的冰冷跨年夜。",
            "sentences": [
                {"en": "On Wednesday evening, we went to the Town Hall to welcome the New Year.", "cn": "就在那个寒风凛冽的星期三除夕深夜，我们相约携手涌向市政厅大楼门前的广袤广场，满怀期待共同守候跨年迎新的神圣钟声。"},
                {"en": "It was a cold night and it was raining heavily, but large crowds of people had gathered under the huge clock.", "cn": "那夜天气极度阴冷彻骨且正下着瓢泼暴雨，然而数以万计的人潮洪流依然前赴后继汇聚在市政厅那座巍峨参天的巨型大钟塔楼正下方。"},
                {"en": "It would strike twelve in twenty minutes' time; fifteen minutes passed, and then, at five to twelve, the clock stopped.", "cn": "再过短短二十分钟那座百年大钟便将敲响宣告午夜零点来临的沉重钟鸣；十五分钟光阴在焦急守候中悄然流逝，然而就在距离十二点仅差五分钟的节骨眼上，钟面上的巨大指针竟然彻底罢工停摆了！"},
                {"en": "The big minute hand did not move; we waited and waited, but nothing happened.", "cn": "那根重达数百磅的粗壮金属分针自此纹丝不动；全场数万人屏住呼吸在狂风暴雨中苦等又苦等，然而天地间却死寂一片，什么都没有发生。"},
                {"en": "Suddenly, a shout went up from the crowd; someone looked at his watch and shouted: 'It's two minutes past twelve! The clock has stopped!'", "cn": "骤然之间人群中爆发出了一阵惊恐的喧嚣大哗；一位看客低头瞥见自己手腕上的机械手表惊慌失措失声尖叫道：“现在明明早都已经是零点过两分了！市政厅的大钟居然坏了停住了！”"},
                {"en": "At that moment, everybody began to laugh and sing; the frozen crowd burst into life despite the silent bells.", "cn": "就在那一刹那，全场紧绷的观众们在片刻愕然之后突然集体哄堂大笑并放声高歌起来；纵然神圣的大钟金钟保持着诡异的死寂，但被冰冻的人群却瞬间爆发出前所未有的狂欢澎湃生机！"},
                {"en": "Public rituals uniting communities at the turn of the calendar mark our collective passage through mortal time.", "cn": "在日历岁月跨年交替更迭之际凝聚全城百姓的公共守岁盛大仪式，庄严烙印记录着我们整个人类族群穿越凡尘流金岁月的集体精神脚印。"},
                {"en": "Prepositions of time such as 'at', 'in', and 'on' are showcased with crystal-clear syntactic precision.", "cn": "诸如'at'、'in'与'on'等核心时间介词的高阶语法规范与精妙配搭，在这篇记叙文中得到了如水晶般清澈剔透的标准示范！"},
                {"en": "Mechanical fallibility reminding humanity that manufactured chronometers remain subordinate to organic time.", "cn": "百年精密机械自鸣钟的关键时刻偶发失灵意外，在冥冥之中仿佛在向狂妄的人类发出善意警示：人造的金属计时工具，在奔腾不息的宇宙自然时光大河面前永远居于末节！"},
                {"en": "Raincoats rustled and breath formed pale clouds in the freezing midnight metropolitan air.", "cn": "人群身上的油布雨衣在风中沙沙作响，口鼻间呼出的滚烫哈气在冰冷刺骨的午夜大都会空气中凝结成了一团团白蒙蒙的雾霭。"},
                {"en": "Laughter transforms an anticlimactic disappointment into an indelible collective memory.", "cn": "豁达包容的开怀大笑，能在眨眼之间将一场原本大失所望的大扫兴意外，奇迹般蜕变为一道在集体记忆长河中永不褪色的温存欢乐烙印！"},
                {"en": "Strangers linked arms beneath the darkened clock face, harmonizing the ancient verses of Auld Lang Syne.", "cn": "素昧平生的陌路行人们在那张漆黑停摆的巨大钟盘下方自发挽起手臂，齐声合唱起那曲苍凉高亢的苏格兰千古骊歌《友谊地久天长》！"},
                {"en": "Celebrate the arrival of the future with joyful resilience, regardless of whether circumstances unfold precisely to plan.", "cn": "怀揣着蓬勃向上的坚韧与欢愉去张开双臂迎接未知未来的降临吧，无论现实的大戏最终是否当真能分秒不差按照我们预设的完美剧本上演！"},
                {"en": "Cold winds cannot extinguish the warmth radiating from fellowship grounded in shared hope.", "cn": "任凭漫天呼啸而过的刺骨寒风吹拂，也生生世世绝无法扑灭植根在对未来的共同希望之中的人间同胞手足温存余温！"},
                {"en": "Happy New Year to all who brave the storm; may your internal compass point steadfastly toward courage and love.", "cn": "谨向天底下所有敢于顶风冒雨无惧风暴前行的勇敢行者道一声新年胜意；祈愿你内心深处的精神罗盘，永远坚定不移指向大爱与无畏！"}
            ]
        },
        {
            "title": "第 10 课 · Not for Jazz · 祖传羽管键琴与古董乐器抢救记",
            "description": "古董羽管键琴屡遭现代爵士乐摧残，被锁进客厅并严禁弹奏流行曲。",
            "sentences": [
                {"en": "We have an old musical instrument; it is called a clavichord.", "cn": "我们家中世世代代珍藏着一件十分古老罕见的传统西洋乐器；它的古典学名叫作击弦羽管键琴。"},
                {"en": "It was made in Germany in 1681; our clavichord is kept in the living room.", "cn": "它早在公元1681年便由德意志顶尖工匠在莱茵河畔纯手工精工雕琢问世；时至今日，我们这件祖传传家宝被安详陈设在客厅的显赫显眼位置。"},
                {"en": "It has belonged to our family for a long time; the instrument was bought by my grandfather many years ago.", "cn": "它在漫长历史岁月中属于我们家族世代传承已历经数代光阴；这一件古董乐器最初是由我的曾祖父在许多许多年以前花重金在欧陆典当行悉心购藏得来的。"},
                {"en": "Recently it was damaged by a visitor; she tried to play jazz on it!", "cn": "然而就在最近这段时间里，它却不幸遭遇了一场毁灭性的重创飞来横祸：一位登门造访的女宾客，竟然妄图在这一件娇贵古琴上疯狂猛砸弹奏现代狂躁爵士乐！"},
                {"en": "She struck the delicate keys too hard and two of the strings were broken.", "cn": "她粗鲁猛烈敲击那些象牙琴键的力道实在太生猛狂暴，以至于琴腹深处两根历经三百年沧桑的古老羊肠琴弦当场应声崩断！"},
                {"en": "My father was shocked; now we are not allowed to touch it.", "cn": "我那平日里温文尔雅的父亲当场大惊失色、痛心疾首；从那以后，他严厉下达禁令：全家任何晚辈与闲杂外人自此统统被严禁再触碰琴键哪怕分毫！"},
                {"en": "It is being repaired by a friend of my father's who specializes in antique restorations.", "cn": "眼下我父亲已特意延请了一位在古董乐器修复领域享誉全欧的莫逆世交泰斗级大师，正在工坊深处为其开展极其细致的抢救性修复。"},
                {"en": "Delicate antique instruments crafted before the industrial era cannot withstand the violent percussive demands of modern rhythms.", "cn": "在工业革命大机器时代到来之前由古代巨匠精心雕琢的娇贵古典乐器，其纤细的声学物理机理结构，根本无法承受现代流行打击乐节奏的狂暴摧残蹂躏！"},
                {"en": "Passive voice constructions emphasizing damaged states over perpetrator actions dominate this dramatic cultural anecdote.", "cn": "通篇对被动语态（was damaged / is being repaired）的大量典范运用，高超地将聚光灯焦点死死锚定在文物器物饱受摧残的悲壮物理状态之上！"},
                {"en": "Every musical invention carries the aesthetic imprint of the philosophical era that gave it birth.", "cn": "每一件乐器器物的发明问世，都深深刻骨铭心地承载着孕育诞生它的那个特定历史哲学时代的精神审美烙印！"},
                {"en": "A harpsichord or clavichord speaks with the whisper of whispering silver, not the thunderous roar of modern grand pianos.", "cn": "一架羽管键琴或古钢琴所能吐露的琴声，乃是如同水银泻地般幽微灵动的温柔耳畔私语，而绝非现代九尺施坦威大三角钢琴那排山倒海般的雷霆轰鸣！"},
                {"en": "Cultural preservation demands setting firm boundaries against the casual vandalism of thoughtless entertainment.", "cn": "对人类古老文明遗产的深情守护，向来需要我们在面对轻浮浮躁的泛娱乐化随意践踏毁坏之时，有胆魄划下坚如磐石的尊严禁令红线！"},
                {"en": "The master restorer tuned the newly replaced copper strings with microscopic precision.", "cn": "老修复宗师凭借着几十年的深厚功力，以微米级的显微镜般严苛尺度，反复调校着新换上的纯手工紫铜羊肠琴弦音准张力。"},
                {"en": "Treat historical artifacts with the reverent silence appropriate for speaking with ancestors.", "cn": "以如同在静谧神殿深处同千年先贤古人对话般的虔诚敬畏肃穆心境，去小心翼翼对待每一件历经沧海桑田遗存至今的历史瑰宝吧！"},
                {"en": "Let Bach's contrapuntal polyphony soar softly through the chamber; true classical elegance will outlive all fleeting musical fads.", "cn": "且让巴赫笔下那层峦叠嶂、精妙绝伦的复调对位华彩在琴房中悠然轻盈回荡吧；真正的纯正古典高贵典雅，必将永远万古长青，远远熬过世俗一切短暂流行的浮华泡沫！"}
            ]
        }
    ]
    courses.append(build_course(nce2_meta, nce2_chapters))

    return courses

if __name__ == "__main__":
    print("正在测试教材生成器...")
    c = get_textbook_courses()
    print(f"已生成前 2 门教材，课程数: {len(c)}")
