# -*- coding: utf-8 -*-
"""
基础学习分类生成器 Part 2:
包含:
2. basic-1000words: 零基础核心高频1000词造句 (10章 x 15句 = 150句)
3. basic-patterns: 英语五大基本句型大突破 (10章 x 15句 = 150句)
4. basic-tenses: 零基础日常时态速成 (10章 x 15句 = 150句)
"""

COURSE_BASIC_1000WORDS = {
    "meta": {
        "id": "basic-1000words",
        "title": "零基础核心高频1000词造句",
        "category": "basic",
        "categoryName": "基础学习",
        "coverGradient": "from-green-500 to-emerald-700",
        "icon": "📝",
        "description": "专为初学者精选的英语高频 1000 词造句实战课，把孤立的单词融入真实、自然的生活与学术句子中，实现见词能读、听词能懂、提笔能写。",
        "difficulty": "beginner",
        "tags": ["基础学习", "高频词汇", "造句实战", "基础进阶"]
    },
    "chapters": [
        {
            "title": "第1章：日常起居与作息词汇",
            "description": "wake, brush, wash, breakfast, morning, clock, routine 造句。",
            "sentences": [
                {"en": "I always wake up early at six o'clock every single morning.", "cn": "我每天清晨六点准时早早醒来，从不赖床。"},
                {"en": "She brushes her teeth carefully with mint toothpaste after eating.", "cn": "进食之后，她总是用薄荷牙膏仔仔细细把牙齿刷得干干净净。"},
                {"en": "He washes his face with warm water to awaken his senses.", "cn": "他用温热的清水洗了把脸，让自己混沌的感官瞬间清醒过来。"},
                {"en": "Our family gathers around the kitchen table to enjoy hot breakfast.", "cn": "我们全家人围坐在厨房的餐桌旁，开开心心享用热腾腾的早餐。"},
                {"en": "The golden morning sun spreads warmth through the open bedroom window.", "cn": "金灿灿的晨曦阳光，透过敞开的卧室窗户向室内洒满无尽暖意。"},
                {"en": "The antique wooden wall clock chimes steadily on the hour.", "cn": "古朴典雅的实木挂钟在每个整点时分，都沉稳准时地鸣响报时。"},
                {"en": "Establishing a healthy daily routine boosts your productivity and mental clarity.", "cn": "建立起规律健康的日常作息习惯，能大幅提升你的工作效率与思维敏锐度。"},
                {"en": "He combs his hair neatly in front of the hallway mirror.", "cn": "他在门厅的穿衣镜前，有条不紊地将自己的头发梳理得整整齐齐。"},
                {"en": "Put on a comfortable cotton shirt and sturdy walking shoes today.", "cn": "今天换上一件柔软透气的纯棉衬衫，穿上一双结实舒适的步行鞋。"},
                {"en": "She sips a cup of hot black coffee while reviewing notes.", "cn": "她一边小口品尝着滚烫的黑咖啡，一边细致复习手头的重要笔记。"},
                {"en": "Never rush through your morning rituals in stressful, chaotic haste.", "cn": "切勿在焦虑混乱的匆忙慌乱中，草草了结你清晨宝贵的洗漱起居时光。"},
                {"en": "A peaceful morning sets a harmonious tone for the entire day.", "cn": "一个平静祥和、井井有条的清晨，能为整整一天的生活定下从容安详的基调。"},
                {"en": "He stretches his arms and legs to relieve muscle stiffness.", "cn": "他舒展拉伸着四肢胳膊与腿部，以此缓解晨起肌肉的紧绷僵硬。"},
                {"en": "Pack your leather briefcase with all essential documents before heading out.", "cn": "在踏出家门之前，把所有必不可少的核心文件整齐装入皮质公文包。"},
                {"en": "Step outside into the crisp fresh air with joy and anticipation.", "cn": "满怀喜悦与对美好一天的期许，大步迈入户外清冽纯净的空气之中。"}
            ]
        },
        {
            "title": "第2章：校园求知与学习装备",
            "description": "book, pencil, notebook, library, teacher, study, question 造句。",
            "sentences": [
                {"en": "A classic library book opens the door to ancient philosophical wisdom.", "cn": "一本图书馆珍藏的古典大作，能为你叩开通往先贤博大哲学智慧的大门。"},
                {"en": "Sharpen your wooden graphite pencil before starting the math exam.", "cn": "在数学考试正式打铃开考之前，把你的木质铅笔削得尖尖齐齐。"},
                {"en": "Write down new vocabulary words neatly in your hardbound notebook.", "cn": "把你今天刚学到的生词与短语，工工整整誊抄在你精装的笔记本上。"},
                {"en": "The university library provides a quiet sanctuary for serious, deep reading.", "cn": "大学图书馆为心怀求索之志的广大学子，提供了一处沉潜深度阅读的静谧圣殿。"},
                {"en": "Our dedicated English teacher explains difficult grammar structures with incredible patience.", "cn": "我们兢兢业业的英语老师，以令人赞叹的极大耐心透彻讲解复杂的语法结构。"},
                {"en": "He studies foreign languages for two hours every evening without fail.", "cn": "每天夜晚他都会雷打不动抽出整整两个小时，心无旁骛研习外语。"},
                {"en": "Never hesitate to ask an insightful question during classroom discussions.", "cn": "在课堂专题讨论环节，永远不要犹豫迟疑提出富有真知灼见的好问题。"},
                {"en": "Solve the challenging algebra equation step by step on the blackboard.", "cn": "在黑板上一环扣一环、条理分明地解开这道颇具挑战性的代数方程题。"},
                {"en": "Every young student has unlimited potential waiting to be tapped.", "cn": "每一个风华正茂的年轻学子，都蕴藏着等待被深度激发的无垠潜能。"},
                {"en": "Review past examination papers to identify recurring patterns of mistakes.", "cn": "认真重温复盘过往的历年真题试卷，精准找出自己反复出现的薄弱错漏盲点。"},
                {"en": "Knowledge acquired through diligent effort remains rooted in the mind forever.", "cn": "通过脚踏实地的勤勉汗水所汲取到的学识，必将终生深植在你的脑海之中。"},
                {"en": "Borrow reference dictionaries from the reading room to verify spelling.", "cn": "从工具书阅览室借出权威词典，以此逐字逐句核实英文拼写的准确无误。"},
                {"en": "Listen attentively when the professor discusses historical turning points.", "cn": "当资深老教授在讲台上深入剖析历史关键转折点时，务必全神贯注侧耳倾听。"},
                {"en": "Education is not the filling of a bucket, but lighting fire.", "cn": "教育从来都不是往空木桶里机械注水，而是点燃学子心中那一簇求索的火种。"},
                {"en": "Cherish every precious academic opportunity to broaden your mental horizons.", "cn": "倍加珍惜在求学求知阶段所降临的每一次契机，全方位拓宽你的思想格局。"}
            ]
        },
        {
            "title": "第3章：职场沟通与工作推进",
            "description": "office, meeting, project, email, report, client, colleague 造句。",
            "sentences": [
                {"en": "Step into the bright, modern office ready to tackle challenging tasks.", "cn": "迈入宽敞明亮的现代化写字楼办公室，做足万全准备去攻克艰巨任务。"},
                {"en": "The weekly strategy meeting will commence promptly at ten o'clock sharp.", "cn": "每周例行的战略发展研讨会，将在上午十点整准时召开开幕。"},
                {"en": "Our engineering project achieved all key milestones ahead of original schedule.", "cn": "我们工程团队负责推进的核心项目，提前超越原定计划全面攻克了所有关键里程碑。"},
                {"en": "Send a formal confirmation email to the international client right now.", "cn": "立刻向跨国商务大客户发送一封措辞得体、严谨规范的书面确认邮件。"},
                {"en": "Review the quarterly financial report with meticulous, detail-oriented scrutiny.", "cn": "以一丝不苟、明察秋毫的严苛审查标准，从头至尾审阅本季度的财务报告。"},
                {"en": "Treat every prospective business client with supreme courtesy and honesty.", "cn": "以至高无上的诚敬礼貌与恪守诚信的商业信誉，对待每一位潜在的业务合作伙伴。"},
                {"en": "Cooperate smoothly with your creative colleagues across different functional departments.", "cn": "与跨越不同职能部门的充满创意的同事们紧密协作、行云流水般协同作战。"},
                {"en": "Deliver an articulate presentation that convinces company executives completely.", "cn": "发表一场条理清晰、极富说服力的精彩商业提案，彻底赢得公司高管的由衷赞赏。"},
                {"en": "Manage your tight work deadlines without sacrificing professional quality standards.", "cn": "在紧锣密鼓严守交付截止日期的同时，绝不向专业品质标准做出哪怕半点妥协。"},
                {"en": "A successful career is built upon integrity, resilience, and teamwork.", "cn": "一份长盛不衰的辉煌职业生涯，深植于坚守诚信、百折不挠与卓越的团队协作。"},
                {"en": "Negotiate fair contract terms that benefit both collaborating corporate parties.", "cn": "经过深思熟虑谈判协商出公平合理的合同条款，实现互利共赢互利互惠。"},
                {"en": "Keep accurate records of all commercial transactions and client correspondences.", "cn": "对所有的商业交易往来以及客户邮件信函，进行严密精准的归档留痕记录。"},
                {"en": "Effective communication eliminates misunderstandings and speeds up executive decision-making.", "cn": "高效清晰的职场双向沟通，能从源头消除一切误解，大幅加速高层决策进程。"},
                {"en": "Take initiative to solve unexpected workplace problems before they escalate.", "cn": "在意外突发的职场棘手问题尚未恶化蔓延之前，主动出击将其消灭在萌芽之中。"},
                {"en": "Professional excellence is an ongoing pursuit, not a single destination.", "cn": "追求卓越非凡的职业素养是一场永无止境的持续修炼，而非一次性的短暂终点。"}
            ]
        },
        {
            "title": "第4章：都市生活与公共出行",
            "description": "subway, ticket, traffic, corner, station, bridge, street 造句。",
            "sentences": [
                {"en": "Take the rapid underground subway to bypass heavy surface road traffic.", "cn": "搭乘四通八达的地下高速地铁，轻松绕开地面拥堵不堪的城市交通早高峰。"},
                {"en": "Purchase your train ticket at the automated digital kiosk machine.", "cn": "在火车站那台智能化的自动售票终端机前，便捷自助购买你的乘车车票。"},
                {"en": "Rush hour road traffic crawls slowly across the central downtown bridge.", "cn": "在上下班通勤的高峰期，桥面上的滚滚车流在市中心大桥上如蜗牛般缓缓挪动。"},
                {"en": "Wait for your friend on the bustling corner beside the bookstore.", "cn": "在书店旁边那座人来人往热闹喧嚣的街角路口，静候你好友的身影出现。"},
                {"en": "The central railway station connects thousands of commuters to regional cities.", "cn": "宏大的中央铁路客运枢纽中心，把成千上万名通勤旅客输送到周边各大城镇。"},
                {"en": "A suspension bridge spans gracefully across the wide, deep harbor mouth.", "cn": "一座巍峨雄伟的现代化大悬索桥，优雅绝伦地横跨在水深港阔的宽阔海湾出海口。"},
                {"en": "Walk down the historic cobblestone street lined with charming cafes.", "cn": "漫步在两旁布满情调小咖啡馆的古老鹅卵石历史文化街区的小街上。"},
                {"en": "Look both directions before stepping onto the designated pedestrian crossing.", "cn": "在迈步踏上标线清晰的人行横道斑马线之前，先向左顾右盼仔细确认安全。"},
                {"en": "City parks provide refreshing green oases amid concrete urban skyscrapers.", "cn": "星罗棋布的城市公园，在钢筋水泥高耸入云的摩天大楼森林间筑起座座绿色绿洲。"},
                {"en": "Follow the electronic navigation map to reach your appointed destination.", "cn": "紧密遵照智能手机电子导航地图的语音指引，顺利抵达你预先指定的目的地。"},
                {"en": "Public transportation networks reduce carbon emissions and urban road congestion.", "cn": "四通八达的公共交通网络，能大幅减少碳排放并有效缓解城市交通拥堵难题。"},
                {"en": "Ask the friendly transit information officer for guidance when lost.", "cn": "在偌大的换乘大厅万一迷失方向，主动向值班的交通导乘人员礼貌问路。"},
                {"en": "Keep your personal transit cards secure inside your front jacket pocket.", "cn": "把你个人的公交交通卡，妥善妥帖存放在上衣内侧带拉链的贴身口袋里。"},
                {"en": "The energetic pulse of a cosmopolitan city inspires creative young souls.", "cn": "一座国际化大都市那蓬勃跳动的时代脉搏，时刻激发着无数青年才俊的创意思维。"},
                {"en": "Navigate complex urban terrain with alertness, poise, and urban savvy.", "cn": "以机警沉着的从容气度与精明的都市智慧，游刃有余穿行于繁复的大都会之中。"}
            ]
        },
        {
            "title": "第5章：餐饮美食与味蕾盛宴",
            "description": "restaurant, menu, soup, steak, vegetable, dessert, coffee 造句。",
            "sentences": [
                {"en": "We reserved a quiet corner table at an authentic Italian restaurant.", "cn": "我们在一家地道正宗的意大利风情餐厅，提前预订好了一张靠窗僻静的角落雅座。"},
                {"en": "Examine the extensive dinner menu before choosing your favorite appetizers.", "cn": "在点选心仪的开胃头盘小吃之前，仔细翻阅浏览这份菜品琳琅满目的晚餐菜单。"},
                {"en": "A bowl of hot chicken soup warms you through and through.", "cn": "一碗热气腾腾、香气四溢的浓醇鸡汤，能从里到外彻底驱散你全身的寒意。"},
                {"en": "He ordered a medium-rare grilled beef steak with roasted garlic.", "cn": "他点了一份五分熟、火候恰到好处的烤牛排，配以喷香浓郁的烤大蒜瓣。"},
                {"en": "Eat fresh green vegetables daily to supply your body with minerals.", "cn": "每天摄入足量新鲜绿叶蔬菜，源源不断为身体供给不可或缺的矿物质与纤维素。"},
                {"en": "A slice of decadent dark chocolate cake was served for dessert.", "cn": "餐后侍者端上了一块浓郁醇厚、入口即化的上等黑巧克力蛋糕作为餐后甜点。"},
                {"en": "Freshly roasted coffee beans brew into a fragrant, stimulating morning drink.", "cn": "现磨深度烘焙的香醇咖啡豆，萃取冲泡成一杯香气四溢、提神醒脑的清晨妙品。"},
                {"en": "Chew your food mindfully to appreciate the subtle harmony of spices.", "cn": "细嚼慢咽、专注地品味食物，去深切领略各种香料之间幽微精妙的相得益彰。"},
                {"en": "Compliment the head chef on the exquisite presentation of every dish.", "cn": "对行政总厨在每一道精美菜肴造型摆盘上所倾注的匠心巧思，由衷致以赞赏。"},
                {"en": "Always remember to leave a courteous tip for exceptional table service.", "cn": "在享受到周到细致、无可挑剔的贴心餐桌服务之后，记得礼貌留下相应小费。"},
                {"en": "Sharing good food with beloved family strengthens the bonds of kinship.", "cn": "与挚爱的至亲家人围坐共享珍馐美食，能让血浓于水的亲情纽带愈加牢固深厚。"},
                {"en": "Traditional local cuisine reflects centuries of culinary culture and heritage.", "cn": "每一个地方独具风味的特色传统菜肴，都折射着数百年传承的深厚烹饪文化底蕴。"},
                {"en": "Sip sparkling water with a fresh slice of yellow lemon wedge.", "cn": "在气泡苏打水里切入一片新鲜明黄的柠檬薄片，慢条斯理地优雅啜饮。"},
                {"en": "Balanced culinary nutrition fuels both intense mental work and athletic stamina.", "cn": "均衡合理的膳食营养搭配，既能为高强度的脑力劳作供能，又能充沛体魄耐力。"},
                {"en": "Hospitality expressed through food touches the deepest chords of human connection.", "cn": "通过饮食佳肴所倾情传递的款待之道，能深深触动人与人之间最真挚的心灵共鸣。"}
            ]
        },
        {
            "title": "第6章：大自然、四季与户外探索",
            "description": "forest, mountain, river, ocean, sky, weather, season 造句。",
            "sentences": [
                {"en": "The primeval forest shelters thousands of rare and endangered wildlife species.", "cn": "这片浩瀚古老的原始森林，庇护滋养着数以千计珍稀濒危的野生动植物种群。"},
                {"en": "Snow-capped mountain peaks pierce high into the crystal-clear azure sky.", "cn": "皑皑白雪覆盖的崇山峻岭绝顶，刺破苍穹耸立在万里无云的蔚蓝晴空之下。"},
                {"en": "The mighty river carves deep canyons through solid rock over millennia.", "cn": "奔腾不息的滚滚大河历经数万年沧桑洗礼，在坚硬的岩石之中冲刷出深邃的大峡谷。"},
                {"en": "The mysterious deep ocean remains largely unexplored by human scientific research.", "cn": "深邃幽暗的浩瀚大洋深处，在很大程度上至今依然是人类科学尚未涉足的神秘领域。"},
                {"en": "Gaze up at the boundless night sky sprinkled with countless constellations.", "cn": "抬头仰望那片无垠深邃的静谧夜空，上面点缀着数以亿计散发微光的古老星座。"},
                {"en": "Unpredictable mountain weather requires hikers to pack versatile waterproof layers.", "cn": "变幻莫测的高山极端天气，要求户外徒步探险者必须随身备足全套防雨保暖衣物。"},
                {"en": "Every distinct season brings its own unique rhythm of natural transformation.", "cn": "大自然的每一个轮转季节，都携带着其独一无二、无可替代的生息蜕变节拍。"},
                {"en": "Hike quietly along marked woodland trails to observe songbirds nesting.", "cn": "沿着标线清晰的林间幽静小径悄然漫步，悉心观察鸣禽在枝头筑巢育雏。"},
                {"en": "Drink cold water flowing from the pure mountain spring with gratitude.", "cn": "怀揣着感恩之情，捧饮一口从高山岩缝间汩汩流淌而出的纯净甘甜泉水。"},
                {"en": "Preserve untouched wilderness so that future generations inherit thriving ecosystems.", "cn": "全力保全人迹罕至的原生态荒野净土，以便我们的后世子孙能够继承繁荣的生态。"},
                {"en": "The autumn leaves paint the rolling hills in brilliant scarlet hues.", "cn": "金秋的落叶宛如神来之笔，把绵延起伏的层峦叠嶂尽皆染成了绚烂夺目的猩红。"},
                {"en": "Breathe the refreshing pine scent released by evergreen needles in wind.", "cn": "深深呼吸风中常青松针所释放出的令人心旷神怡、神清气爽的清幽松木香气。"},
                {"en": "Nature heals human anxiety through its tranquil, eternal laws of balance.", "cn": "大自然凭借其永恒恒常、静水流深的天然平衡法则，抚慰治愈着人类内心的焦虑。"},
                {"en": "Take nothing but inspiring photographs, and leave nothing but light footprints.", "cn": "在踏足大自然时，除了珍贵的唯美照片什么也别带走，除了浅浅的足迹什么也别留下。"},
                {"en": "Living in harmonious reverence with nature is humanity's highest earthly duty.", "cn": "怀揣由衷敬畏与大自然万物和谐共生融为一体，是人类在这个星球上的至高天职。"}
            ]
        },
        {
            "title": "第7章：家庭亲情与人际社交",
            "description": "family, parent, friend, neighbor, child, love, share 造句。",
            "sentences": [
                {"en": "A close-knit family offers unconditional love through life's triumphs and trials.", "cn": "一个和睦温暖的亲密家庭，在人生的顺境辉煌与逆境磨难中都给予着无私的爱意。"},
                {"en": "Loving parents guide their children with gentle wisdom, patience, and compassion.", "cn": "慈爱的父母用温柔的智慧、无限的耐心与慈悲宽仁，悉心指引着孩子们长大成人。"},
                {"en": "A loyal friend stands firmly beside you when fair-weather companions flee.", "cn": "一位忠贞不渝的挚友，在那些酒肉之交作鸟兽散的关键危难时刻依然坚定伴你身旁。"},
                {"en": "A good neighbor lends a helping hand whenever unexpected troubles arise.", "cn": "一位善良敦厚的街坊好邻居，在突遭意外困境之时总会毫不犹豫主动伸出援手。"},
                {"en": "Every innocent child deserves safety, wholesome nourishment, and joyful education.", "cn": "天下间每一个天真无邪的幼小孩子，都配得上获得安全庇护、充足营养与快乐教育。"},
                {"en": "Genuine love is not selfish possession, but selfless commitment and care.", "cn": "真正的至深至爱从来都不是狭隘自私的占有，而是无怨无悔的奉献牺牲与体贴关怀。"},
                {"en": "Share your blessings and knowledge freely with those who need guidance.", "cn": "慷慨大度地将你所拥有的福泽与学识，毫无保留地分享给那些渴望得到指引的人。"},
                {"en": "Celebrate family anniversaries and milestone birthdays with heartfelt homemade banquets.", "cn": "在家庭重大结婚纪念日与亲人重要寿辰之际，亲手烹饪温馨的家宴开怀欢庆。"},
                {"en": "Listen with undivided attention when a friend shares their deepest worries.", "cn": "当知心好友向你敞开心扉倾诉内心深处的苦闷隐忧时，务必全神贯注侧耳倾听。"},
                {"en": "Forgive honest mistakes quickly so bitterness never takes root inside you.", "cn": "迅速坦荡地宽恕他人的无心过失，决不让仇恨与怨怼的毒草在自己心田生根发芽。"},
                {"en": "Treat elders with supreme reverence, honoring their lifetime of labor.", "cn": "以至高无上的尊崇敬意对待年迈长辈，由衷致敬他们倾尽一生付出的辛勤汗水。"},
                {"en": "A harmonious neighborhood community builds a fortress of safety for children.", "cn": "一个融洽和睦、邻里守望相助的社区大家庭，能为孩子们筑造起一道安全的坚强壁垒。"},
                {"en": "Kind words spoken in private often change the trajectory of lives.", "cn": "在私下里轻声说出的温暖体贴关怀之语，往往能彻底扭转一个人一生的奋斗轨迹。"},
                {"en": "Cultivate lifelong friendships founded upon shared noble virtues and integrity.", "cn": "悉心培育那些建立在共同崇高美德修养与光明磊落操守之上的万年长青挚友情谊。"},
                {"en": "Love binds diverse hearts together in an unbreakable tapestry of kinship.", "cn": "无私真挚的爱，将天下千万颗各不相同的心紧紧编织进一幅坚不可摧的亲情锦缎。"}
            ]
        },
        {
            "title": "第8章：健康医疗与身心滋养",
            "description": "health, doctor, hospital, medicine, exercise, body, sleep 造句。",
            "sentences": [
                {"en": "Maintaining physical and mental health is the foundation of all success.", "cn": "悉心维系身心两健的强健体魄与健全心智，是人生建功立业达成一切成功的基石。"},
                {"en": "A compassionate doctor listens to patient concerns with utmost professional empathy.", "cn": "一位仁心仁术的崇高医生，总是以极高的专业素养与同理心体察病患的疾苦关切。"},
                {"en": "Modern hospital facilities utilize cutting-edge medical equipment to save lives.", "cn": "设备精良的现代化综合医院，广泛应用尖端先进的医疗仪器全力抢救垂危生命。"},
                {"en": "Take prescribed medicine exactly according to the licensed pharmacist's directions.", "cn": "严格遵照执业药剂师的专业医嘱与用药指南，按时按量服用配给的处方药物。"},
                {"en": "Engage in vigorous cardiovascular exercise at least three times every week.", "cn": "坚持每周至少进行三次挥汗如雨、充分调动心肺功能的中高强度有氧体育锻炼。"},
                {"en": "Your physical body is a magnificent instrument that requires mindful maintenance.", "cn": "你自己的血肉之躯是一具精密绝伦的神奇仪器，需要你时刻用心去悉心呵护保养。"},
                {"en": "Eight hours of deep, restful sleep restores vital brain energy completely.", "cn": "每晚保证八个小时深沉安详的优质睡眠，能让消耗殆尽的大脑精力彻底恢复如初。"},
                {"en": "Drink plenty of clean water throughout the day to stay hydrated.", "cn": "在一天当中的各个时间段适量饮用足量纯净水，确保身体各机能时刻保持水分充盈。"},
                {"en": "Wash your hands frequently with antibacterial soap to prevent contagious infections.", "cn": "养成经常用抗菌洗手液清洗双手的卫生好习惯，彻底阻断各种传染性病菌的侵袭。"},
                {"en": "Schedule regular annual physical checkups to detect potential illnesses early.", "cn": "每年定期安排一次全面的系统性健康体检，以求在潜伏期尽早排查发现潜在疾患。"},
                {"en": "Nutritious balanced meals give your body sustained vitality throughout the day.", "cn": "营养均衡合理的一日三餐膳食搭配，能赋予身体全天候绵延不绝的充沛生机活力。"},
                {"en": "Practice mindfulness and deep breathing exercises to relieve psychological stress.", "cn": "积极练习冥想静坐与腹式深呼吸法，以科学有效的手段舒缓化解心理重压焦虑。"},
                {"en": "Protect your precious eyesight by resting your eyes after screen work.", "cn": "在紧盯电脑电子屏幕劳作之后适时远眺放松，全力保护自己弥足珍贵的双眼视力。"},
                {"en": "A healthy mind thriving inside a healthy body is life's treasure.", "cn": "在强健有力的体魄中孕育一颗豁达通透的健康灵魂，是造物主赐予生命的最佳礼物。"},
                {"en": "Never sacrifice your well-being in the blind pursuit of transient goals.", "cn": "切勿在盲目追逐过眼云烟般短暂虚名的狂热中，挥霍透支牺牲掉自己的身心健康。"}
            ]
        },
        {
            "title": "第9章：商贸购物与财务管理",
            "description": "money, bank, price, cost, market, save, spend 造句。",
            "sentences": [
                {"en": "Money is a useful servant, but an exceedingly dangerous master.", "cn": "金钱是一名称职好用的得力仆人，然而一旦被其反噬，它就会沦为一个极其危险的暴君。"},
                {"en": "Deposit your surplus savings securely inside a reputable commercial bank.", "cn": "将你结余下来的多余资金积蓄，安全稳妥地存入信誉卓著的合规商业银行账户中。"},
                {"en": "Compare the retail price and quality before purchasing expensive electronic equipment.", "cn": "在掏钱选购昂贵的大宗数码电子设备之前，务必货比三家仔细衡量价格与制造质量。"},
                {"en": "Calculate the total cost of ownership including maintenance and insurance fees.", "cn": "把日后必不可少的保养维修费与商业保险费通盘计算在内，精准核算全生命周期成本。"},
                {"en": "The weekend farmers market offers locally grown produce at affordable rates.", "cn": "周末热闹开市的农夫早市集市，以极其亲民实惠的价格供应产自本地的新鲜蔬果。"},
                {"en": "Save a fixed percentage of your monthly income for emergency reserves.", "cn": "每月雷打不动将固定比例的薪资收入存储起来，作为未雨绸缪应对不时之需的应急储备。"},
                {"en": "Spend your hard-earned financial resources wisely on education and health.", "cn": "把你辛勤耕耘所换来的宝贵财务积蓄，明智睿智地投资在能让你终生升值的教育与健康上。"},
                {"en": "Keep accurate receipts of all major business purchases for tax deduction.", "cn": "将所有重大的企业商业采购发票凭据妥善分门别类留存，以备年终合规申报税务抵扣。"},
                {"en": "Avoid impulsive shopping habits triggered by flashy advertising and promotions.", "cn": "时刻保持清醒自律，坚决克制由铺天盖地的眼花缭乱广告促销所诱发的非理性冲动消费。"},
                {"en": "Financial literacy empowers individuals to build long-term economic independence.", "cn": "精深的财商素养与科学理财观念，能赋予每一个普通人铸就长期经济独立自主的底气。"},
                {"en": "Budget your monthly household expenses carefully to avoid falling into debt.", "cn": "精打细算、一丝不苟地做好家庭每月的收支预算编制，坚决杜绝因盲目超支而深陷债务泥潭。"},
                {"en": "Invest patiently in assets that generate stable, long-term compound growth.", "cn": "怀揣长线思维与足够耐性，扎实投资于那些能够带来稳健复利倍增效应的核心优质资产。"},
                {"en": "True wealth is measured not by possessions, but by financial freedom.", "cn": "一个人真正的财富厚度，绝非取决于名下堆砌的物质虚荣，而在于他所拥有的自由抉择权。"},
                {"en": "Generosity toward worthwhile charitable causes brings genuine inner fulfillment.", "cn": "对造福社会的公益慈善事业解囊相助慷慨奉献，能换来心灵深处最充实丰盈的由衷快乐。"},
                {"en": "Master money with discipline and wisdom so it serves your noble purposes.", "cn": "以高度的自律操守与深邃的理财智慧驾驭金钱，让它始终为践行你崇高的人生志向服务。"}
            ]
        },
        {
            "title": "第10章：梦想蓝图与自我实现",
            "description": "dream, goal, courage, success, effort, future, achieve 造句。",
            "sentences": [
                {"en": "Dwell in possibility and hold steadfast to your most cherished lifelong dream.", "cn": "时刻仰望无限可能的高空，对你内心深处珍藏一生的崇高梦想始终坚守笃定如初。"},
                {"en": "Break down your ambitious long-term goal into practical, weekly targets.", "cn": "将你高瞻远瞩的宏大长期目标，拆解成一个个切实行之有效、步步为营的每周具体指标。"},
                {"en": "Courage is not the absence of fear, but triumph over it.", "cn": "真正的英勇无畏从来都不是没有丝毫恐惧，而在于拥有战胜并彻底驾驭恐惧的魄力。"},
                {"en": "Lasting success is the cumulative result of small, unnoticed daily disciplines.", "cn": "能够经得起时间淘洗的长久成功，是无数个默默无闻、日复一日的高度自律积攒出的必然回报。"},
                {"en": "Dedicate your honest effort and sweat without expecting instantaneous glory.", "cn": "默默倾注你最踏实的勤勉汗水与全部心血，从不急功近利奢望任何一蹴而就的虚名速成。"},
                {"en": "The future belongs entirely to those who prepare for it with passion.", "cn": "光辉灿烂的未来，只属于那些在当下每一天都倾注满腔热忱、为之未雨绸缪做足准备的人。"},
                {"en": "You have the talent, intellect, and willpower to achieve remarkable things.", "cn": "你完全具备卓越的天赋才智、敏锐的头脑与钢铁般的意志力，去干出一番惊天动地的大事业。"},
                {"en": "Overcome self-doubt by reflecting upon all the obstacles you conquered before.", "cn": "每当心头涌现自我怀疑的阴霾时，多回想回顾一番过往岁月里你曾经亲手踩碎的无数荆棘险阻。"},
                {"en": "Continuous improvement across daily habits leads inevitably to extraordinary excellence.", "cn": "在日常看似微不足道的点滴习惯中追求精进，必将水到渠成造就登峰造极的非凡造诣。"},
                {"en": "Surround yourself with visionary thinkers who elevate your standards and ideals.", "cn": "让你身边聚集着胸怀远大抱负的思想者与同行者，让他们的高洁品格拉升你的眼界与志向。"},
                {"en": "Celebrate the gradual progress you make each day on this spelling journey.", "cn": "在这场英语拼写淬炼的伟大征途上，为你自己每天所取得的点滴扎实跃升而由衷欢呼。"},
                {"en": "Your focused dedication today is shaping a bright tomorrow for your family.", "cn": "你今天所倾注的全部专注与汗水，正在为你深爱的至亲家人亲手塑造成一个美好的明天。"},
                {"en": "Never compromise your integrity for the sake of short-lived convenience.", "cn": "在漫长的人生马拉松赛道上，切勿为了贪图一时短暂省事的便利而典当出卖自己的人格操守。"},
                {"en": "You have conquered all ten chapters of high-frequency core vocabulary usage!", "cn": "你已经以超凡的自律与恒心，全面攻克完成了这套高频核心一千词全部十大章节的实战造句！"},
                {"en": "Step proudly forward into the boundless ocean of fluent English mastery!", "cn": "带着无尽的自豪与从容自信，大步迈入地道流利驾驭卓越英语的无边浩瀚汪洋！"}
            ]
        }
    ]
}

COURSE_BASIC_PATTERNS = {
    "meta": {
        "id": "basic-patterns",
        "title": "英语五大基本句型大突破",
        "category": "basic",
        "categoryName": "基础学习",
        "coverGradient": "from-blue-600 to-indigo-800",
        "icon": "📐",
        "description": "系统剖析英语语法的骨架中枢：主谓（SV）、主谓宾（SVO）、主系表（SVC）、主谓双宾（SVOO）和主谓宾补（SVOC），彻底理清英文句子结构脉络。",
        "difficulty": "beginner",
        "tags": ["基础学习", "句型结构", "语法框架", "造句逻辑"]
    },
    "chapters": [
        {
            "title": "第1章：主谓句型 (S + V) 极简之美",
            "description": "主语 + 不及物动词，掌握独立成句的动作结构，如 birds sing, sun rises。",
            "sentences": [
                {"en": "The golden morning sun rises peacefully in the east.", "cn": "金灿灿的初升晨阳，在东方天际平缓祥和地冉冉升起。"},
                {"en": "Little woodland birds sing cheerfully in the leafy branches.", "cn": "林间欢快灵巧的小鸟，在繁茂如盖的枝头叽叽喳喳放声啼鸣。"},
                {"en": "The exhausted marathon runner rested on the grassy lawn.", "cn": "精疲力竭的马拉松长跑选手，在青草茵茵的草坪上安详歇息。"},
                {"en": "Dark rain clouds vanished completely under the midday heat.", "cn": "浓重阴沉的密布雨云，在正午骄阳的烘烤下完完全全消散无踪。"},
                {"en": "The baby slept deeply throughout the silent, frosty night.", "cn": "年幼娇嫩的小婴儿在寂静严寒的漫漫冬夜里，睡得香甜无比。"},
                {"en": "Fresh spring flowers bloom gloriously across the green meadow.", "cn": "烂漫鲜艳的初春花朵，在广阔连绵的绿色草甸间尽情娇艳盛开。"},
                {"en": "He walked briskly along the quiet avenue before breakfast.", "cn": "在用早餐之前，他迈着矫健利落的大步沿着幽静的林荫大道散步。"},
                {"en": "The old steam train arrived right on scheduled time.", "cn": "那列古老沉稳的老式蒸汽机车，分秒不差准点进站抵达站台。"},
                {"en": "Time flies fast when you are immersed in deep study.", "cn": "当你全身心沉浸在深度的求索研读中时，光阴岁月总是飞逝如梭。"},
                {"en": "The wounded soldier recovered quickly in the hospital ward.", "cn": "受伤的英勇战士在医院病房的悉心照料下，身体迅速康复痊愈。"},
                {"en": "Cold snow fell softly upon the silent mountain village.", "cn": "冰凉纯洁的漫天白雪，轻柔无声地飘落在寂静安详的高山村落上。"},
                {"en": "The curious puppy jumped over the wooden garden fence.", "cn": "那只生性好奇活泼的小狗，欢天喜地纵身一跃跳过了木栅栏。"},
                {"en": "Financial markets fluctuate according to global investor sentiment.", "cn": "瞬息万变的金融资本市场，时刻跟随着全球投资者的心理情绪剧烈波动。"},
                {"en": "The candle burned steadily on the quiet scholar's desk.", "cn": "洁白的蜡烛在伏案学者静谧的书桌上，恒久沉稳地静静燃烧发光。"},
                {"en": "Subject plus intransitive verb expresses pure, complete action.", "cn": "主语搭配不及物动词，能够以极简洗练的笔触表达纯粹完整的动作行为。"}
            ]
        },
        {
            "title": "第2章：主谓宾句型 (S + V + O) 实义传递",
            "description": "主语 + 及物动词 + 宾语，英语最常用的核心表达句式。",
            "sentences": [
                {"en": "The diligent student reads profound philosophy books every weekend.", "cn": "勤奋笃学的优秀学子，每个周末都沉潜研读深奥的哲学典籍。"},
                {"en": "She plays the classical violin with breathtaking emotional intensity.", "cn": "她以令人屏息赞叹的充沛情感张力，娴熟演奏着古典小提琴名曲。"},
                {"en": "The experienced surgeon performed a delicate heart operation successfully.", "cn": "经验丰富的外科主任医师，顺利圆满完成了一台极其精细的心脏手术。"},
                {"en": "Our engineering team built a groundbreaking software operating system.", "cn": "我们实力雄厚的工程研发团队，攻克打造了一套具有开创意义的操作系统。"},
                {"en": "The kind mother baked sweet honey cookies for her children.", "cn": "慈爱善良的母亲亲手为放学回家的孩子们，烤制了香甜可口的蜂蜜曲奇。"},
                {"en": "He planted ten green apple trees in his backyard garden.", "cn": "他在自己后院的花园果园里，亲手栽种下了十棵翠绿的苹果树苗。"},
                {"en": "The dedicated teacher answered every difficult grammar question patiently.", "cn": "兢兢业业的老师以极大的耐心，逐一解答了每一个艰深的疑难语法问题。"},
                {"en": "Farmers harvest ripe golden wheat across the vast plains.", "cn": "辛勤的农夫们在广袤的平原大地上，欢欢喜喜收割成熟的金黄小麦。"},
                {"en": "The brave firefighter rescued a frightened kitten from the tree.", "cn": "勇敢无畏的消防救援战士，从高高的树梢上救下了一只受惊吓的小猫。"},
                {"en": "She speaks three foreign languages fluently with remarkable natural confidence.", "cn": "她以令人钦佩的自然从容自信，极其流利纯熟地说着三门外语。"},
                {"en": "The ambitious author wrote a bestselling historical novel last winter.", "cn": "雄心勃勃的知名作家在去年隆冬时节，著就了一部风靡一时的历史畅销巨作。"},
                {"en": "We respect the universal human rights of every global citizen.", "cn": "我们发自肺腑由衷尊重地球上每一位世界公民所享有的普世基本人权。"},
                {"en": "The research scientist proved the revolutionary mathematical theorem rigorously.", "cn": "专注科研的数学科学家，以极其严谨完备的逻辑论证了革命性的数学定理。"},
                {"en": "Drink fresh clean water regularly to nourish your internal organs.", "cn": "经常足量饮用新鲜纯净水，以此悉心滋润养护你的体内各大器官。"},
                {"en": "A transitive verb directs energetic action onto a receiving object.", "cn": "及物动词充当强劲的纽带，将主语充沛的动作力量精准传递施加于宾语之上。"}
            ]
        },
        {
            "title": "第3章：主系表句型 (S + V + C) 状态描摹",
            "description": "主语 + 连系动词 (be, look, seem, feel, smell, become) + 表语。",
            "sentences": [
                {"en": "The crisp autumn evening air smells fresh and pleasantly cool.", "cn": "金秋黄昏微凉清爽的户外空气，闻起来沁人心脾、格外舒适宜人。"},
                {"en": "Her innovative design proposal sounds extraordinarily promising to executives.", "cn": "她这份极具前瞻创新的设计提案，在公司高管听来显得极具发展前途。"},
                {"en": "He feels completely confident about passing the upcoming bar exam.", "cn": "对于顺利考过即将到来的这场司法职业资格大考，他感到成竹在胸自信满满。"},
                {"en": "The ancient stone castle looks mysterious beneath the silvery moonlight.", "cn": "那座古老的欧洲石头城堡，在皎洁银色月光的映照下显得格外神秘莫测。"},
                {"en": "Fresh organic strawberries taste delightfully sweet and refreshingly tart.", "cn": "新鲜刚摘下来的有机草莓，尝起来酸甜适口、回味无穷，令人精神为之一振。"},
                {"en": "The young student became an accomplished scholar through relentless dedication.", "cn": "经过数十载孜孜不倦的潜心治学，那个年轻学子蜕变成了著作等身的学者。"},
                {"en": "She remained calm and poised throughout the high-pressure crisis.", "cn": "面对千钧一发的高压严峻危机，她自始至终保持着令人钦佩的从容镇定。"},
                {"en": "The weather turned bitterly cold as the winter blizzard approached.", "cn": "随着狂暴的冬日暴风雪步步逼近，天地间的气温在一瞬间骤降到了冰点。"},
                {"en": "His heartfelt apology seemed sincere and touching to everyone present.", "cn": "在现场所有人看来，他那番发自肺腑的真诚致歉显得格外诚恳感人。"},
                {"en": "Integrity is the most valuable virtue in human social interaction.", "cn": "光明磊落的操守与诚实，是人类全部社交往来活动中最为珍贵的崇高美德。"},
                {"en": "The silky smooth fabric felt luxurious against her sensitive skin.", "cn": "如丝绸般柔滑亲肤的高档面料，轻触在她娇嫩的肌肤上倍感奢华舒适。"},
                {"en": "Leaves turn brilliant scarlet and gold in late October each year.", "cn": "在每年十月深秋时节，漫山遍野的树叶纷纷蜕变成夺目的猩红与纯金。"},
                {"en": "Her deep dedication to public education grew stronger with age.", "cn": "她投身于大众公共教育事业的那颗炽热赤子之心，随着岁月流逝愈发笃定深厚。"},
                {"en": "Staying humble is essential when you achieve major career triumphs.", "cn": "在你取得职业生涯重大里程碑辉煌成就之时，保持虚怀若谷至关重要。"},
                {"en": "Linking verbs connect the subject to its descriptive subject complement.", "cn": "系动词宛如一座优雅的彩虹桥，将主语与描摹其状态属性的表语紧密相连。"}
            ]
        },
        {
            "title": "第4章：主谓双宾句型 (S + V + IO + DO) 赠予转移",
            "description": "主语 + 及物动词 + 间接宾语(人) + 直接宾语(物)，如 give sb. sth.。",
            "sentences": [
                {"en": "The proud grandmother gave the newborn baby a silver bracelet.", "cn": "满心欢喜的祖母，将一只沉甸甸的纯银吉祥手镯赠予了刚降生的胖重孙。"},
                {"en": "He bought his beloved wife a stunning diamond eternity ring.", "cn": "他为深爱的相濡以沫的妻子，精心选购了一枚璀璨夺目的永恒钻石戒指。"},
                {"en": "The senior professor taught eager undergraduate students modern quantum physics.", "cn": "这位德高望重的资深老教授，亲自为朝气蓬勃的本科生传授前沿量子物理学。"},
                {"en": "She sent her overseas business partners a formal seasonal greeting.", "cn": "她向远在重洋之外的跨国商务合作伙伴们，寄出了一封措辞庄重典雅的节日贺函。"},
                {"en": "Could you please pass me that heavy wooden salad bowl?", "cn": "您可以顺手把餐桌那一头那个沉甸甸的木质沙拉大碗递给我一下吗？"},
                {"en": "The company offered the outstanding software engineer an attractive salary.", "cn": "公司为这位才华横溢的出类拔萃软件架构师，开出了极其丰厚的优渥年薪。"},
                {"en": "He told the fascinated listening children an exciting adventure tale.", "cn": "他向身旁听得入了神的一帮孩子们，绘声绘色讲述了一个惊险刺激的冒险传奇。"},
                {"en": "Mother made her hungry son a bowl of warm noodles.", "cn": "慈爱的母亲为饥肠辘辘下自习归来的儿子，亲手煮了一大碗热气腾腾的鸡蛋面。"},
                {"en": "The generous foundation awarded the brilliant student a four-year scholarship.", "cn": "慷慨宏大的慈善教育基金会，为这位寒门天才学子颁发了长达四年的全额奖学金。"},
                {"en": "Show your international guests the warm hospitality of our hometown.", "cn": "向来自远方海内外的尊贵国际宾朋，热情展现我们故乡淳朴厚道的热情好客。"},
                {"en": "He lent his reliable neighbor a set of gardening power tools.", "cn": "他毫不犹豫地把自家一套完好趁手的电动园艺工具，借给了隔壁可靠的邻居。"},
                {"en": "Write your elderly grandparents a handwritten letter full of affection.", "cn": "用真挚滚烫的笔触，亲手为你年迈的爷爷奶奶写上一封充满温情的亲笔家信。"},
                {"en": "The hotel concierge booked the tired travelers two opera tickets.", "cn": "宾馆前台那位彬彬有礼的礼宾司管家，为疲惫的旅人们订好了两张当晚的歌剧门票。"},
                {"en": "Indirect objects receive the benefit of the direct object transferred.", "cn": "间接宾语通常代表人，是动作所转移付出的直接宾语实物的最终受惠受体。"},
                {"en": "You can transform this pattern using prepositions to or for.", "cn": "借助介词 to 或 for，你可以游刃有余地将该双宾句型灵活转化为介词短语结构。"}
            ]
        },
        {
            "title": "第5章：主谓宾补句型 (S + V + O + OC) 状态补充",
            "description": "主语 + 及物动词 + 宾语 + 宾语补足语，如 make him happy, call him leader。",
            "sentences": [
                {"en": "Continuous disciplined effort will make your ambitious dreams come true.", "cn": "持之以恒、高度自律的辛勤汗水，必将让你心中那些宏大的梦想化作现实。"},
                {"en": "The committee appointed the senior diplomat ambassador to the United Nations.", "cn": "评审委员会郑重决议，任命这位资深老练的外交官出任常驻联合国全权特命大使。"},
                {"en": "We painted the living room walls a bright sunny yellow.", "cn": "我们齐心协力动手，把客厅整面大白墙粉刷成了温暖明媚的向日葵明黄色。"},
                {"en": "The unexpected good news made everyone in the office ecstatic.", "cn": "这一突如其来的重大喜讯，让整间办公室里的所有同仁无不欣喜若狂欢欣鼓舞。"},
                {"en": "They elected the visionary community organizer mayor of the metropolis.", "cn": "广大市民以压倒性的选票，选举这位富有远见卓识的社区领袖出任大都会市长。"},
                {"en": "Keep the laboratory floor completely clean and dry at all times.", "cn": "时刻保持高精尖科研实验室的地面绝对一尘不染、干爽整洁，严防任何滑倒事故。"},
                {"en": "The jury found the accused defendant innocent of all criminal charges.", "cn": "经过深入核查全部如山铁证，陪审团一致裁决被告人在所有刑事指控上完全无罪。"},
                {"en": "I consider this profound literary work an undisputed modern masterpiece.", "cn": "我由衷将这部思想深邃的鸿篇巨制文学经典，视作当之无愧的现当代传世巅峰杰作。"},
                {"en": "She named her loyal golden retriever puppy Charlie after her grandfather.", "cn": "为了缅怀自己挚爱的慈祥外祖父，她给那只忠诚的金毛寻回犬幼犬起名叫做查理。"},
                {"en": "His calm leadership kept the panicked passengers calm during turbulence.", "cn": "在遭遇强烈空中气流剧烈颠簸时，他临危不乱的沉着指挥让全舱乘客保持了冷静。"},
                {"en": "Exercise and balanced nutrition keep your physical body strong and healthy.", "cn": "适量规律的体育锻炼与营养均衡的科学膳食，能让你的血肉之躯时刻保持强健体魄。"},
                {"en": "The loud construction noise drove the studying students almost crazy.", "cn": "窗外工地上震耳欲聋的施工噪音，吵得正在专心自习的学子们几乎抓狂烦躁。"},
                {"en": "We found the ancient stone trail blocked by fallen timber.", "cn": "我们实地勘察时猛然发现，那条古老的石头山道已被倾倒的枯木巨石彻底封堵。"},
                {"en": "An object complement completes the sense of the direct object.", "cn": "宾语补足语不可或缺，它与直接宾语构成不可分割的复合结构以补足完整句义。"},
                {"en": "Mastering complementation unlocks sophisticated command of modern English syntax.", "cn": "精熟驾驭宾语补足语的丰富多态变化，是登上现代高级英语句法巅峰的必经通途。"}
            ]
        },
        {
            "title": "第6章：There be 存在句型全景透视",
            "description": "表示某处存在某物，掌握主谓就近原则与时态拓展。",
            "sentences": [
                {"en": "There is a magnificent ancient oak tree in our backyard.", "cn": "在我们家的后院花园正中央，伫立着一棵苍翠挺拔、树龄逾百年的参天大橡树。"},
                {"en": "There are forty eager young students sitting in the classroom.", "cn": "整整四十名求知若渴、风华正茂的年轻学子，端端正正端坐在阶梯教室之中。"},
                {"en": "There was a sudden, violent thunderclap that shook the windows.", "cn": "突然之间平地炸响了一声震耳欲聋的惊雷，震得整栋楼的玻璃窗户剧烈作响。"},
                {"en": "There were thousands of cheering fans packed inside the sports stadium.", "cn": "数以万计欢呼雀跃的狂热体育迷，把整座宏大的现代化体育场塞得水泄不通。"},
                {"en": "There will be many exciting new opportunities for determined scholars.", "cn": "对于那些矢志不渝、笃定前行的求索学者而言，前方必将涌现出无限崭新的机遇。"},
                {"en": "There have been dramatic advancements in clean solar energy technology recently.", "cn": "近些年以来，在清洁低碳的太阳能技术领域已经涌现出了突飞猛进的突破进展。"},
                {"en": "There must be an honest, logical explanation for this mystery.", "cn": "对于眼前发生的这桩离奇谜题，其背后必定存在着一个客观合乎逻辑的科学解释。"},
                {"en": "There seems to be a slight misunderstanding between the partners.", "cn": "在两位并肩创业的合伙人之间，当下似乎悄然滋生出了一丝微小的误会隔阂。"},
                {"en": "There is no doubt that daily consistent practice brings mastery.", "cn": "毫无疑问，日复一日持之以恒的高标准刻苦练习，必将促成技艺登峰造极。"},
                {"en": "There is a book and two pens on the wooden desk.", "cn": "木质写字台上工工整整摆放着一本厚重的书，以及两支墨水充盈的钢笔。"},
                {"en": "There are two pens and a book lying on the table.", "cn": "桌面上端端正正平放着两支钢笔，以及一本封面素雅的精装典籍。"},
                {"en": "Notice how the proximity principle governs verb agreement in existential sentences.", "cn": "密切注意并领会：在 There be 存在句中，系动词的单复数严格遵从“就近一致原则”。"},
                {"en": "There lies a sleepy fishing village along the rugged coastline.", "cn": "沿着那条嶙峋崎岖的漫长海岸线，静卧着一座民风淳朴、与世无争的小渔村。"},
                {"en": "There stands a towering marble lighthouse guiding ships safely home.", "cn": "巍然耸立着一座通体由洁白大理石砌造的雄伟灯塔，日夜指引着远洋船只平安返航。"},
                {"en": "Existential structures paint a vivid picture of presence and spatial location.", "cn": "存在句型通过空间与存在的巧妙交融，勾勒出一幅幅形象生动、栩栩如生的画面。"}
            ]
        },
        {
            "title": "第7章：祈使句与情感感叹句精粹",
            "description": "祈使句祈请指令与 What/How 引导的强烈情感感叹句。",
            "sentences": [
                {"en": "Always speak the honest truth, regardless of the temporary consequences.", "cn": "无论眼前的暂时利害得失如何，永远都要挺直脊梁说真诚坦荡的大实话。"},
                {"en": "Please take off your outdoor shoes before entering the house.", "cn": "在踏步进入温馨的家门之前，请有礼貌地换下穿在室外的外行鞋。"},
                {"en": "Never judge someone before you have walked in their shoes.", "cn": "在真正设身处地体验过他人所历经的泥泞沧桑之前，永远切勿轻率妄下断语。"},
                {"en": "Be kind and compassionate to every living soul you encounter.", "cn": "对你漫漫人生旅途当中所邂逅的每一个鲜活生命，都要心怀仁善与慈悲温情。"},
                {"en": "Listen closely to the advice of mentors who love you.", "cn": "对那些倾尽心血挚爱关怀你的师长先贤所提出的良药苦口诤言，务必洗耳恭听。"},
                {"en": "Do not let transient setbacks extinguish your inner burning passion.", "cn": "决不要让那些过眼云烟般的短暂挫折，扑灭你胸膛深处熊熊燃烧的炽热热爱。"},
                {"en": "What a magnificent, breathtaking sunset paints the western horizon tonight!", "cn": "今晚西边天际那抹晚霞是何等壮丽恢弘、令人屏息凝神赞叹的造化奇观啊！"},
                {"en": "What an extraordinary accomplishment this team achieved through unity!", "cn": "这支队伍凭借着万众一心的精诚团结，取得了多么了不起的非凡大成就啊！"},
                {"en": "What wonderful, inspiring words of wisdom the professor shared today!", "cn": "这位老教授今天在讲堂上与我们分享的人生至理名言，是多么令人豁然开朗啊！"},
                {"en": "How beautifully the morning songbird sings from the high branches!", "cn": "清晨高踞枝头的那只林间百灵鸟，啼鸣出的歌声是多么婉转清澈、动人心魄啊！"},
                {"en": "How swiftly time flows past when one is immersed in study!", "cn": "当一个人沉醉在知识的海洋中潜心钻研时，光阴岁月流淌得是何其迅捷飞快啊！"},
                {"en": "How generous and kind your loving family has been to us!", "cn": "你那充满温情与大爱的全家人待我们是何等慷慨体贴、亲切如春风拂面啊！"},
                {"en": "Imperative sentences omit the implied subject you to convey urgency.", "cn": "祈使句巧妙隐去了不言自明的人称主语 you，以此传递出直接有力、雷厉风行的指令。"},
                {"en": "Exclamations express spontaneous surges of human emotion with distinct structure.", "cn": "感叹句借助精妙严谨的语法架构，将人类心灵深处奔涌而出的强烈情感生动宣泄。"},
                {"en": "Command language with authority, and express wonder with poetic enthusiasm.", "cn": "用坚如磐石的笃定权威去发号施令，用诗意澎湃的热忱去由衷赞叹世间的美好！"}
            ]
        },
        {
            "title": "第8章：并列复合句 (Fanboys 连词纽带)",
            "description": "for, and, nor, but, or, yet, so 并列连词构建平衡对称复句。",
            "sentences": [
                {"en": "She practiced speaking daily, and her oral fluency improved dramatically.", "cn": "她坚持每天雷打不动大声开口操练口语，她的表达流利度随之获得了惊人的飞跃。"},
                {"en": "The path was rugged, but the travelers pressed on courageously.", "cn": "前方的道路崎岖泥泞险象环生，然而勇敢的跋涉者们依然义无反顾奋勇向前挺进。"},
                {"en": "Study hard every day, or you will regret wasted opportunities.", "cn": "每天都要争分夺秒下真功夫刻苦攻读，否则日后你必将为虚度年华而悔恨莫及。"},
                {"en": "He did not give up, nor did he ever lose hope.", "cn": "他不仅没有向困难举白旗妥协退缩，心中希望的火种也未曾有过丝毫的黯淡动摇。"},
                {"en": "The exam was challenging, yet every prepared student passed with honors.", "cn": "尽管试卷命题极具深度与挑战性，但每一位做足万全准备的学子都斩获了优异佳绩。"},
                {"en": "She felt deeply tired, so she retired early for the night.", "cn": "她感到全身的骨头架子都透着深沉的倦意，于是早早洗漱上床就寝安歇了。"},
                {"en": "He loved reading classical poetry, for words gave him solace.", "cn": "他一往情深痴迷于研读古典诗词，因为那些传世文字总能在暗夜里抚慰他的灵魂。"},
                {"en": "Knowledge provides immense power, and character gives that power wisdom.", "cn": "渊博的学识赋予人改天换地的无上伟力，而崇高的人格则为这股伟力注入了智慧的缰绳。"},
                {"en": "The storm was howling outside, yet the cabin remained warm.", "cn": "户外风狂雨骤寒风呼啸如雷，而温暖的小木屋里却炉火熊熊安宁舒适如阳春。"},
                {"en": "You can choose comfort, or you can choose profound growth.", "cn": "你可以贪图安逸偏安一隅，或者你也可以勇挑重担去拥抱脱胎换骨的深刻蜕变。"},
                {"en": "He made no excuses, nor did he blame his teammates.", "cn": "他没有为自己的失利寻找半句推脱之辞，更没有把责任归咎甩锅给身边的队友。"},
                {"en": "She dedicated her career to research, so breakthroughs arrived steadily.", "cn": "她将整个人生毕生精力全部奉献给了基础科学研究，重大科研突破自然水到渠成。"},
                {"en": "Coordinating conjunctions connect two grammatically independent clauses in equal balance.", "cn": "并列连词宛如坚实牢靠的天平，将两个语法上平分秋色、各自独立的完整分句连为一体。"},
                {"en": "Punctuate compound sentences with a comma placed before coordinating conjunctions.", "cn": "在书面正式表达中，切记在并列连词的前方加上一个规范的逗号，以使句法条理井然。"},
                {"en": "Symmetry and balance form the architectural beauty of compound English prose.", "cn": "工整对仗与平衡对称的严谨布局，构筑起了英语并列复合句宏伟壮丽的建筑美学。"}
            ]
        },
        {
            "title": "第9章：复合句主从句入门 (从属连词连结)",
            "description": "because, although, if, when, while 引导的状语从句系统掌握。",
            "sentences": [
                {"en": "Because he prepared thoroughly, he answered every interview question masterfully.", "cn": "正因为他在面试前做足了万全的详尽准备，他极其老练从容地对答了所有提问。"},
                {"en": "Although the mountain trail was steep, we reached the peak.", "cn": "尽管通往绝顶的崇山栈道极其险峻陡峭，我们依然凭借钢铁般的意志成功登顶。"},
                {"en": "If you never test your limits, you will never grow.", "cn": "如果你从不敢于向自己的体能与智力极限发起挑战，你将永远无法实现蜕变成长。"},
                {"en": "When morning sunlight pierced through clouds, the sleepy valley awakened.", "cn": "当破晓清晨的一缕缕纯金阳光穿透层层云雾，沉睡中的幽深山谷瞬间苏醒了。"},
                {"en": "While the professor was lecturing, attentive students took detailed notes.", "cn": "当白发苍苍的老教授在讲台上纵论古今之时，台下专心致志的学子们奋笔疾书。"},
                {"en": "Since you have made your decision, pursue it with dedication.", "cn": "既然你已经深思熟虑做出了最终抉择，那就义无反顾、倾注全部身心去拼搏践行。"},
                {"en": "Unless you practice spelling daily, you cannot build solid fluency.", "cn": "除非你能够坚持每天高标准、雷打不动练拼写，否则你绝不可能筑牢纯熟的语感。"},
                {"en": "As soon as the signal was given, the runners accelerated.", "cn": "发令枪响起的发令信号刚一发出，蓄势待发的田径健儿们便如离弦之箭绝尘而去。"},
                {"en": "He kept writing steadily even though his fingers ached painfully.", "cn": "即便写字写到指关节都泛起阵阵酸痛，他手中的笔尖依然沉稳不停歇地飞速书写。"},
                {"en": "Wherever you travel in this vast world, stay humble always.", "cn": "无论你漫长的一生走到大千世界的哪一个角落，内心深处都要时刻坚守谦逊虚怀。"},
                {"en": "Subordinate clauses depend entirely upon the main independent clause syntactically.", "cn": "从属从句在句法语义逻辑上，必须完全依附于主句这个参天大树方能完整立足。"},
                {"en": "Place a comma after the dependent clause when it introduces.", "cn": "当状语从句置于主句之前作为句首状语引入时，在主从句之间务必加上规范逗号。"},
                {"en": "Complex sentences reflect nuanced, multi-layered causal logic and chronological relationships.", "cn": "主从复合句能极其细腻深邃地映射出客观事物之间错综复杂、多维交织的因果与时空脉络。"},
                {"en": "Mastering subordination transforms simple choppy thoughts into elegant literary prose.", "cn": "精深掌握主从句转换技法，能将原本生硬支离破碎的简单句，升华为行云流水的优美散文。"},
                {"en": "Write with architectural clarity, ensuring every subordinate element serves the main thesis.", "cn": "像营造宫殿般严谨运笔构思，确保每一个从属分支构件都众星捧月般烘托核心主旨。"}
            ]
        },
        {
            "title": "第10章：五大基本句型大熔炉综合演练",
            "description": "句型识别、转换与混合长难句解构，打通英文语法任督二脉。",
            "sentences": [
                {"en": "The brave scholar spoke the truth, and the audience listened.", "cn": "勇敢的学者昂首挺胸直抒胸臆讲出真理，全场肃然起敬的听众无不凝神屏息倾听。"},
                {"en": "Hard work made the poor apprentice a master of his craft.", "cn": "数十年如一日的刻苦淬炼，让当年那个贫寒稚嫩的学徒工终成一代名扬天下的匠作宗师。"},
                {"en": "She gave her faithful friend a precious handwritten book of poetry.", "cn": "她将一本倾尽心血亲笔工整抄写的珍贵诗集，深情赠予了自己风雨相伴的知心好友。"},
                {"en": "The clear mountain stream looked inviting beneath the scorching midday sun.", "cn": "在正午酷暑烈日的炙烤之下，那一股清澈见底的潺潺高山山泉显得格外诱人惬意。"},
                {"en": "There is an unbreakable bond between disciplined practice and exceptional fluency.", "cn": "在高度自律的日常刻苦操练与出类拔萃的纯熟流利度之间，存在着坚不可摧的必然纽带。"},
                {"en": "When morning arrived, the tired traveler continued his long trek.", "cn": "当东方破晓天光大亮之时，洗去浑身倦意的旅人重拾行囊，继续踏上他的漫漫长途跋涉。"},
                {"en": "Identify the core grammatical skeleton before analyzing complex subordinate clauses.", "cn": "在着手深度剖析冗长繁复的主从长难句之前，先一眼看穿提炼出句子的核心主谓骨架。"},
                {"en": "The five basic sentence patterns are the immutable foundation of English.", "cn": "英语五大基本句型，构成了整座巍峨宏大英语语言大厦历久弥坚、颠扑不破的立足基石。"},
                {"en": "Combine diverse patterns skillfully to create rhythmic, musical sentence flow.", "cn": "游刃有余、炉火纯青地组合穿插各类句式，方能营构出抑扬顿挫、宛如天籁的行文旋律。"},
                {"en": "Patience and understanding solve complicated human conflicts far better than anger.", "cn": "设身处地的耐性与由衷理解，在化解人类错综复杂的纷争矛盾时远比暴怒咆哮管用百倍。"},
                {"en": "Practice breaking down everyday sentences into their fundamental syntactic roles.", "cn": "在日常阅读中养成好习惯，自觉将遇见的每一个句子拆解为其最本质的句法成分角色。"},
                {"en": "Grammar is not a prison of rules, but the architecture of liberty.", "cn": "语法从来都不是禁锢思维的森严牢笼，而是赋予思想展翅高飞、精准表达的宏伟建筑。"},
                {"en": "You have thoroughly conquered the five basic sentence patterns of English!", "cn": "你已经以超凡的领悟力与踏实的努力，彻彻底底融会贯通攻克了英语五大核心基本句型！"},
                {"en": "Construct your thoughts with clarity, precision, and commanding linguistic power.", "cn": "以清晰明澈的逻辑、严谨精准的构词以及无可撼动的语言力量，筑造抒发你的思想！"},
                {"en": "Step confidently into advanced reading and sophisticated bilingual expression today!", "cn": "从今天起，昂首挺胸、自信从容地跨入高阶学术阅读与地道精深双语表达的宏阔天地！"}
            ]
        }
    ]
}

COURSE_BASIC_TENSES = {
    "meta": {
        "id": "basic-tenses",
        "title": "零基础日常时态速成",
        "category": "basic",
        "categoryName": "基础学习",
        "coverGradient": "from-amber-500 to-red-600",
        "icon": "⏳",
        "description": "彻底理清英文时态的时间线维度，从一般现在时、一般过去时、一般将来时，到进行时态与完成时态，让表达时态严谨规范、地道纯正。",
        "difficulty": "beginner",
        "tags": ["基础学习", "时态进阶", "动词变形", "语境造句"]
    },
    "chapters": [
        {
            "title": "第1章：一般现在时 (Present Simple) 常态与真理",
            "description": "客观真理、日常习惯、第三人称单数加 s/es 规则精讲。",
            "sentences": [
                {"en": "The golden sun rises in the east and sets in the west.", "cn": "金灿灿的太阳恒久在东方冉冉升起，在西方徐徐降落。"},
                {"en": "Water boils at one hundred degrees Celsius under standard atmospheric pressure.", "cn": "在一个标准大气压之下，纯净水在达到摄氏一百度时沸腾开锅。"},
                {"en": "He exercises vigorously in the fitness center three times a week.", "cn": "他坚持每周三次在健身中心大汗淋漓地进行高强度体育锻炼。"},
                {"en": "She teaches English literature with infectious passion at our university.", "cn": "在我们大学的讲台上，她以极富感染力的炽热热忱讲授着英国文学。"},
                {"en": "My elder brother works as a dedicated civil engineer in Seattle.", "cn": "我亲爱的大哥在西雅图一家知名机构，担任尽职尽责的土木工程师。"},
                {"en": "The Earth orbits around the sun once every three hundred sixty-five days.", "cn": "地球沿着椭圆轨道环绕太阳公转一周，正好耗时三百六十五天有余。"},
                {"en": "I always review my spelling vocabulary notes before going to sleep.", "cn": "在每晚熄灯就寝之前，我总是雷打不动认真复习我的拼写单词笔记。"},
                {"en": "Cats wash their clean faces carefully with their soft little paws.", "cn": "爱干净的小猫咪，总是用它那柔软轻巧的小爪子仔仔细细洗脸。"},
                {"en": "The high-speed bullet train departs from the station every thirty minutes.", "cn": "风驰电掣的高速动车组列车，每隔三十分钟便准点从车站呼啸发车。"},
                {"en": "Honest people keep their solemn promises under all difficult circumstances.", "cn": "光明磊落、诚实守信的正人君子，在任何艰难困苦的境遇下都恪守誓言。"},
                {"en": "Notice the third-person singular suffix added to the base verb form.", "cn": "仔细观察并牢记：在一般现在时中，主语为第三人称单数时动词须加词尾 s 或 es。"},
                {"en": "Plants require sunlight, fertile soil, and fresh water to flourish.", "cn": "大千世界的花草植物，需要充足的阳光、肥沃的沃土与甘露方能茁壮繁茂。"},
                {"en": "She speaks several international languages with effortless, native-like ease.", "cn": "她能游刃有余、毫不费力地操着数门国际通用语言进行地道流利的交流。"},
                {"en": "General truths and habitual actions belong in the present simple tense.", "cn": "放之四海而皆准的客观真理，以及人们习以为常的日常习惯动作，皆归属于一般现在时。"},
                {"en": "Mastering regular verb inflections ensures professional grammatical accuracy in writing.", "cn": "精熟掌握规则动词的屈折变化形态，是确保书面语篇达到专业级语法精度的基石。"}
            ]
        },
        {
            "title": "第2章：一般过去时 (Past Simple) 往事与历史",
            "description": "规则动词加 ed 与不规则动词过去式，描述过去已完结的事件。",
            "sentences": [
                {"en": "He graduated with top academic honors from university last summer.", "cn": "在去年夏天，他以全校名列前茅的顶尖学术优异成绩从大学光荣毕业。"},
                {"en": "Our ancestors crossed vast oceans in search of freedom and dignity.", "cn": "我们的先辈们横渡波涛汹涌的茫茫大洋，去追寻自由的阳光与人性的尊严。"},
                {"en": "She bought a charming stone cottage near the peaceful blue lake.", "cn": "她在平静如明镜的碧蓝湖畔，全资买下了一座景色宜人的石头小木屋。"},
                {"en": "The brave explorers reached the South Pole through terrible howling blizzards.", "cn": "英勇无畏的极地探险家们冒着狂暴肆虐的呼啸暴风雪，奇迹般挺进抵达了南极点。"},
                {"en": "Yesterday morning I wrote three detailed chapters of my new book.", "cn": "昨天上午，我一气呵成、心无旁骛写完了自己新书整整三个详尽的核心章节。"},
                {"en": "The ancient Roman Empire expanded across three continents in antiquity.", "cn": "在远古时代，强盛一时的古罗马帝国版图曾横跨欧、亚、非三大洲。"},
                {"en": "He made a solemn promise to his dying father long ago.", "cn": "在很久很久以前，他在弥留之际的生身父亲床榻前，许下了一个庄严的誓言。"},
                {"en": "They walked ten miles along the muddy riverbank without complaining.", "cn": "他们沿着泥泞不堪的崎岖河岸并肩行军了十英里，一路上没有半句怨言。"},
                {"en": "The famous scientist discovered penicillin by fortunate accident in his laboratory.", "cn": "那位名垂青史的科学家，在实验室里凭借一次幸运的偶然意外发现了青霉素。"},
                {"en": "We celebrated our graduation with joyous laughter and joyful tears together.", "cn": "我们汇聚一堂，伴着欢畅的大笑与感动的热泪，共同欢庆我们终生难忘的毕业盛典。"},
                {"en": "Irregular past tense verbs must be memorized through extensive daily reading.", "cn": "英语中那些不规则动词的过去式变形，必须在日积月累的海量语境阅读中熟稔于心。"},
                {"en": "A specific past time indicator anchors the completed event firmly.", "cn": "一个具体明确的过去时间状语标志词，能将已然完结的历史事件牢牢锚定在时间轴上。"},
                {"en": "The great artist painted a haunting portrait of his beloved hometown.", "cn": "那位大师级画家饱蘸深情，亲手为自己魂牵梦萦的热爱故乡创作了一幅传世肖像。"},
                {"en": "History teaches profound moral lessons through triumphs and tragic human mistakes.", "cn": "浩瀚的史册通过过往人类辉煌的胜利与惨痛的悲剧，向后世传递着深刻的道德镜鉴。"},
                {"en": "Recount past memories with vivid verbs that bring historical moments alive.", "cn": "用生动传神、充满画面感的强力动词去追溯往昔，让历史的华彩瞬间跃然纸上。"}
            ]
        },
        {
            "title": "第3章：一般将来时 (Future Simple) 展望与规划",
            "description": "will + 动词原形 与 be going to，表达未来计划、心愿与预测。",
            "sentences": [
                {"en": "I will conquer every challenging English sentence with absolute determination.", "cn": "我必将怀揣钢铁般坚决的坚定意志，彻底攻克每一个艰深地道的英文长难句。"},
                {"en": "We are going to visit our grandparents in the countryside tomorrow.", "cn": "我们全家已经做好了周全计划，明天一大早就去乡下探望可亲的爷爷奶奶。"},
                {"en": "Artificial intelligence will transform global healthcare and education fundamentally.", "cn": "日新月异的人工智能科技，必将从底层根本上重塑全球的医疗保障与教育格局。"},
                {"en": "She is going to study international commercial law at Oxford University.", "cn": "她已经打点好行装，即将启程远赴牛津大学深造攻读国际商法专业。"},
                {"en": "Look at those dark storm clouds; it is going to rain.", "cn": "快看天际那黑压压翻滚的阴沉雨云，眼看着马上就要下起倾盆大雨了。"},
                {"en": "They will build a high-speed railway connecting the two coastal metropolises.", "cn": "他们将投资修建一条崭新的高标准客运专线高铁，把沿海两座核心大都市紧密相连。"},
                {"en": "I will support you through whatever challenges tomorrow may bring forward.", "cn": "无论未知的明日将带来何等严峻的狂风暴雨，我都将毫无保留始终做你的坚强后盾。"},
                {"en": "The sun will rise at six fifteen tomorrow morning as usual.", "cn": "明天清晨六点十五分，那一轮明媚的太阳必将如同往昔一般准时跃出地平线。"},
                {"en": "He will probably receive the prestigious promotion by the end of year.", "cn": "到了今年岁末年关之时，他十有八九能够顺利斩获那份众望所归的晋升嘉奖。"},
                {"en": "What will you do after you achieve complete bilingual spoken fluency?", "cn": "当你真正达成炉火纯青、如母语般自如的双语口语纯熟度之后，你打算干什么？"},
                {"en": "Use be going to when evidence shows an event is imminent.", "cn": "当眼前已然出现显而易见的客观事实迹象时，运用 be going to 结构表达即将发生。"},
                {"en": "Use will for spontaneous decisions, solemn promises, and long-term predictions.", "cn": "运用 will 能够极其恰切地表达现场做出的果断决断、庄严的誓言诺言以及长远预测。"},
                {"en": "Tomorrow is a blank white canvas waiting for your bold brushstrokes.", "cn": "崭新的明天是一张纤尘不染的洁白画布，正翘首期盼着你挥毫泼洒浓墨重彩的画笔。"},
                {"en": "Hope anchors the human soul securely in the stormy sea of life.", "cn": "对未来的美好期许，是人类灵魂在波涛汹涌的沧海洪流中不被倾覆的最稳固铁锚。"},
                {"en": "Plan your future with strategic wisdom, and execute with disciplined daily effort.", "cn": "以高瞻远瞩的战略智慧运筹帷幄规划未来，以脚踏实地的自律汗水大步坚决执行。"}
            ]
        },
        {
            "title": "第4章：现在进行时 (Present Continuous) 正在发生",
            "description": "be (am/is/are) + doing，描摹此时此刻正在进行的生动画面。",
            "sentences": [
                {"en": "Listen closely! The nightingale is singing a haunting melody in trees.", "cn": "侧耳细听！一只夜莺正在茂密的树梢枝头，深情啼鸣着一曲婉转动人的天籁。"},
                {"en": "Look outside the window; gentle snowflakes are falling softly right now.", "cn": "快推开窗户往外看，纯白轻盈的雪花此刻正轻柔无声地漫天飘落大地。"},
                {"en": "He is writing an important research manuscript at his wooden desk.", "cn": "他此刻正端坐在木质书桌前，全神贯注起草撰写一篇至关重要的学术科研文稿。"},
                {"en": "The children are laughing joyfully while building a giant snowman outside.", "cn": "孩子们正在户外欢声笑语打成一片，齐心协力堆起一个大大的圆滚雪人。"},
                {"en": "Our engineering team is developing a groundbreaking medical diagnostic instrument.", "cn": "我们尖端的工程专家团队，当前正在紧锣密鼓研制一款革命性的医疗诊断仪器。"},
                {"en": "Why are you looking at that antique oil painting so intently?", "cn": "你为什么如此全神贯注、目不转睛地久久凝视着那一幅古典欧洲油画呢？"},
                {"en": "The climate across our fragile planet is changing at an alarming rate.", "cn": "我们赖以生存的这颗脆弱星球上的全球气候，目前正以令人揪心的速度发生剧变。"},
                {"en": "She is practicing her violin scales to prepare for the concert.", "cn": "为了给即将到来的独奏音乐会做足准备，她此刻正聚精会神练习小提琴音阶。"},
                {"en": "Dark rain clouds are gathering ominously above the distant mountain range.", "cn": "乌云密布、阴沉压顶的雷雨云层，此刻正以遮天蔽日之势在远山之巅迅速汇聚。"},
                {"en": "The economy of the developing region is expanding rapidly this year.", "cn": "今年以来，该新兴发展中地区的实体经济正在以极其迅猛的势头强劲向好扩张。"},
                {"en": "Stative verbs describing mental conditions are rarely used in continuous tenses.", "cn": "表述恒常心理认知或所有关系的静态动词，通常极少用于进行时态结构当中。"},
                {"en": "Form the present continuous using the proper auxiliary be plus present participle.", "cn": "运用相应人称的助动词 be 搭配动词的现在分词 -ing，构筑起生动的现在进行时。"},
                {"en": "Live fully in the present moment while working toward your future.", "cn": "在向着远大未来脚踏实地奋力打拼的同时，全情投入、淋漓尽致活在当下的每一分每一秒。"},
                {"en": "Capturing ongoing actions creates a sense of immediate, cinematic realism.", "cn": "精准捕捉正在进行中的生动动作，能赋予语言文字一种如电影特写般强烈的临场感。"},
                {"en": "Breathe deeply, for you are creating a masterpiece of living history.", "cn": "深吸一口气吧，因为你此时此刻的奋斗足迹，正亲手谱写着一部波澜壮阔的鲜活史诗。"}
            ]
        },
        {
            "title": "第5章：过去进行时 (Past Continuous) 过去特定时刻",
            "description": "was/were + doing，描述过去某一时刻正在发生的背景画面。",
            "sentences": [
                {"en": "I was reading a classic novel when the telephone suddenly rang.", "cn": "当客厅的电话铃声骤然大作时，我当时正捧着一本古典文学巨著读得入迷。"},
                {"en": "The cold wind was howling loudly while we were walking home.", "cn": "当我们顶风冒雪走在回家的路上时，刺骨的凛冽寒风正在耳畔呼啸作响。"},
                {"en": "She was playing the grand piano when the unexpected guests arrived.", "cn": "当那些不速之客突然敲门到访时，她当时正坐在大三角钢琴前弹奏乐章。"},
                {"en": "What were you doing at eight o'clock yesterday evening, young man?", "cn": "昨天晚上八点整的那个时间段，你年轻人在干什么呢？"},
                {"en": "The surgeon was performing a complex procedure when the power failed.", "cn": "正当医院主干供电突然发生意外跳闸时，主刀医生当时正在开展复杂的精细手术。"},
                {"en": "Rain was pouring down in torrents as we navigated the mountains.", "cn": "当我们驾驶车辆穿行在崇山峻岭间时，暴雨正以瓢泼倾盆之势倾泻而下。"},
                {"en": "They were discussing important quarterly business strategy when I entered the room.", "cn": "当我推门迈入会议室时，高管们当时正在热烈研讨至关重要的季度商业战略。"},
                {"en": "The little boy was crying bitterly because he had lost his puppy.", "cn": "那个可怜的小男孩当时哭得痛彻心扉，因为他不慎弄丢了心爱的小狗狗。"},
                {"en": "Golden autumn leaves were dancing in the air throughout the afternoon.", "cn": "整个悠闲的午后时光里，金黄色的秋叶都在微风吹拂的半空中轻盈飞舞起舞。"},
                {"en": "The professor was explaining the complex theory while students listened intently.", "cn": "老教授在讲台上深入浅出剖析理论，与此同时全班学子正在台下聚精会神倾听。"},
                {"en": "Past continuous sets the descriptive background for a sudden interrupting event.", "cn": "过去进行时常常充当丰满的叙事背景大幕，用以烘托那件突然打断发生的一般过去时事件。"},
                {"en": "Notice the auxiliary was used with singular subjects and were with plurals.", "cn": "牢牢记准助动词的单复数：单数主语搭配 was，复数主语与第二人称则严格搭配 were。"},
                {"en": "Simultaneous past actions can be joined smoothly with the conjunction while.", "cn": "借助连词 while 的巧妙穿针引线，可以将过去同一时段并行发生的两个动作融会贯通。"},
                {"en": "Reconstruct past historical scenes with vivid, moving temporal descriptions.", "cn": "借助生动流转的过去进行时时态，将历史尘封的昔日风貌如画卷般鲜活重现。"},
                {"en": "Time capsules of memory come alive through dynamic past continuous phrasing.", "cn": "封存在岁月记忆胶囊深处的陈年往事，借由过去进行时的生动勾勒而重获新生。"}
            ]
        },
        {
            "title": "第6章：现在完成时 (Present Perfect) 经历与影响",
            "description": "have/has + done，连接过去与现在，强调动作对现在的影响或至今的经历。",
            "sentences": [
                {"en": "I have thoroughly mastered all foundational English grammatical rules.", "cn": "我已经彻彻底底、融会贯通精熟掌握了全部基础英语核心语法规则。"},
                {"en": "She has visited more than thirty countries across five diverse continents.", "cn": "在漫漫环球求索历程中，她的足迹已经遍及了横跨五大洲的三十二个国家。"},
                {"en": "Our dedicated scientific team has published over fifty peer-reviewed papers.", "cn": "我们恪尽职守的顶尖科研团队，迄今已在国际同行评议权威期刊发表了五十余篇论文。"},
                {"en": "Have you ever seen the magnificent green northern aurora in person?", "cn": "在有生之年的过往岁月里，你曾有幸亲身亲眼目睹过那道曼妙幽绿的北极光吗？"},
                {"en": "He has lived in this historic seaside village since early childhood.", "cn": "从情窦初开的孩提幼年时代起，他就一直在这座饱经沧桑的海滨古村落定居。"},
                {"en": "They have already completed the first four modules of this course.", "cn": "他们当下实际上早已圆满攻克完成了这门高阶核心精品课程的前四个大模块。"},
                {"en": "The train has just departed from platform five into the distance.", "cn": "那列满载旅客的客运列车刚刚驶离五号站台，向着辽阔的地平线疾驰而去。"},
                {"en": "Medical researchers have made miraculous breakthroughs in fighting viral illnesses.", "cn": "前沿医学研究专家在抗击恶性病毒性传染病战役中，已经斩获了奇迹般的重大突破。"},
                {"en": "She has not yet decided which university scholarship offer to accept.", "cn": "至于究竟最终接受哪一所知名大学所开出的全额奖学金，她目前尚未拿定主意。"},
                {"en": "We have known each other for more than twenty loyal years.", "cn": "我们彼此相识相知相濡以沫、互为知己挚友，迄今为止已经超过了整整二十个年头。"},
                {"en": "Never combine the present perfect with a specific finished past time marker.", "cn": "切记铁律：现在完成时绝对不可以与表示已然完结的具体过去时间点（如 yesterday）连用。"},
                {"en": "Use for to indicate a duration, and since for a starting point.", "cn": "牢记搭配：介词 for 后接持续的一段时间跨度，而介词 since 后接历史的精确发端时刻。"},
                {"en": "The present perfect bridges the gap between historical action and current reality.", "cn": "现在完成时宛如一座贯通古今的宏伟桥梁，将过往发生的行为与当下的现实紧密相连。"},
                {"en": "Count the milestones you have reached with proud, well-deserved satisfaction.", "cn": "带着由衷自豪与理所应当的心满意足，细细数点你一路走来所跨越的崇高里程碑。"},
                {"en": "Your persistent dedication has opened doors to boundless international horizons.", "cn": "你长期以来持之以恒的倾情奉献，已经为你叩开了一扇扇通往广阔国际视野的大门。"}
            ]
        },
        {
            "title": "第7章：过去完成时 (Past Perfect) 过去的过去",
            "description": "had + done，强调在过去某一动作或时刻之前就已经完成的事件。",
            "sentences": [
                {"en": "The express train had already departed before we reached the platform.", "cn": "就在我们气喘吁吁一路狂奔赶到站台之前，那列特快列车实际上早已驶离发车了。"},
                {"en": "She had finished all her homework before dinner was served tonight.", "cn": "在今晚热气腾腾的晚餐端上餐桌之前，她早就利索地把所有家庭功课全部做完了。"},
                {"en": "By the time the police arrived, the clever thief had escaped.", "cn": "等到巡警鸣着警笛赶赴案发现场之时，那个狡猾的窃贼早已逃之夭夭不见踪影了。"},
                {"en": "He had never witnessed such breathtaking natural beauty until that journey.", "cn": "在启程踏上那趟奇妙旅途之前，他这辈子还从未亲眼目睹过如此摄人心魄的自然至美。"},
                {"en": "They had lived in London for ten years before moving here.", "cn": "在下定决心举家搬迁来到这里定居之前，他们曾在雾都伦敦生活了整整十年之久。"},
                {"en": "She realized that she had left her leather handbag in the cafe.", "cn": "她猛然倒吸一口凉气醒悟过来：自己把贵重的真皮手提包落在了刚才那家咖啡馆里。"},
                {"en": "The storm had ceased by the time dawn broke over the mountains.", "cn": "到了晨曦拂晓普照群山之巅的那一刻，肆虐了整整一夜的狂风暴雨终于全然止息。"},
                {"en": "He had studied English grammar diligently before he traveled across Europe.", "cn": "在踏上纵贯欧洲大陆的远行之前，他曾一丝不苟、夜以继日苦练攻读过英语语法。"},
                {"en": "When we reached the movie theater, the film had already started.", "cn": "当我们火急火燎赶到电影院大厅时，大银幕上的电影正片其实早就已经开场放映了。"},
                {"en": "The crops had withered completely because it had not rained for months.", "cn": "田地里的庄稼全都枯萎焦黄了，因为在此之前已经长达数月之久滴雨未降了。"},
                {"en": "The past perfect establishes clear chronological sequence between two past actions.", "cn": "过去完成时能极其明晰精准地厘定出：在过去的两个历史动作之中，究竟谁先谁后。"},
                {"en": "Use the auxiliary had paired with the invariant past participle form.", "cn": "该时态一律采用统一的助动词 had，搭配动词的过去分词形式，人称变换其形不变。"},
                {"en": "Clauses introduced by by the time frequently trigger the past perfect.", "cn": "由时间状语连词短语 by the time 引导的从句，在语境中往往天然呼应触发过去完成时。"},
                {"en": "Narrate historical sequences with temporal sophistication using the past perfect.", "cn": "运用过去完成时，以极其严密精湛的时序逻辑层次，优雅叙述往昔的历史风云脉络。"},
                {"en": "Reflecting upon past prerequisites illuminates the foundation of current achievement.", "cn": "深情回顾那些在过去先决达成的坚实前提，能彻底明晰照亮当下丰功伟绩的源头所在。"}
            ]
        },
        {
            "title": "第8章：将来进行与将来完成时高阶拓展",
            "description": "will be doing 与 will have done，描摹未来特定时刻的状态与未来完成的功业。",
            "sentences": [
                {"en": "This time tomorrow, I will be flying high above the Pacific Ocean.", "cn": "到了明天这个时候，我本人将正坐在一万米高空上翱翔飞越浩瀚的太平洋。"},
                {"en": "By next December, our team will have completed the entire rail tunnel.", "cn": "等到明年十二月来临之际，我们施工队伍必将完工贯通整条宏大的穿山海底隧道。"},
                {"en": "She will be giving an important keynote speech at nine o'clock tomorrow.", "cn": "在明天早晨九点整的那个时间点，她将正站在讲台上向全场发表重磅主旨演讲。"},
                {"en": "By the end of this month, you will have spelled one thousand sentences.", "cn": "等到本月底收官复盘之时，你本人将已经精准拼写攻克了整整一千个地道长难句！"},
                {"en": "They will be celebrating their golden wedding anniversary in two weeks.", "cn": "再过短短两周时间，老两口就将汇聚全家亲眷，隆重庆祝他们相濡以沫的金婚大典。"},
                {"en": "Scientists will have found effective cures for many ailments within decades.", "cn": "在未来数十年的岁月长河里，科研专家们必将攻关寻获根治诸多顽疾的特效良方。"},
                {"en": "Will you be attending the international academic conference in Paris next summer?", "cn": "明年夏季在巴黎举办的那场国际顶尖学术研讨峰会，届时您是否会抽空莅临出席呢？"},
                {"en": "By the time he retires, he will have served forty honorable years.", "cn": "等到他光荣退休的那一天到来之时，他将已经在自己的工作岗位上勤勉履职了整整四十年。"},
                {"en": "The astronaut will be orbiting the Earth while we are sleeping tonight.", "cn": "当今晚我们全人类在大地上安详入梦时，宇航员将正驾驶飞船在轨道上环绕地球巡游。"},
                {"en": "By this time next year, she will have mastered advanced bilingual translation.", "cn": "到了明年此时此刻，她将已经彻彻底底精熟驾驭了高阶专业级双语笔译与同传。"},
                {"en": "Future continuous envisions active ongoing participation at a specific future juncture.", "cn": "将来进行时以充满远见的目光，勾勒设想在未来的某一个特定时段节点上正在发生的场景。"},
                {"en": "Future perfect looks backward from a future standpoint onto an accomplishment.", "cn": "将来完成时则立足于未来某一个崇高的终点线向回眺望，检阅已然大功告成的辉煌战果。"},
                {"en": "Project your aspirations forward in time and visualize their triumphant completion.", "cn": "将你心中的崇高志向大胆投射到未来的时空之中，在脑海中清晰预演它们圆满功成的盛况。"},
                {"en": "Mastering advanced tenses unlocks elite fluency in sophisticated professional discourse.", "cn": "精深掌握这两大高阶时态的运用，能为你推开通向国际高端专业级话语交流的至高殿堂。"},
                {"en": "Time is an elastic continuum of human purpose, perseverance, and triumph.", "cn": "时间是人类胸怀崇高抱负、历经坚韧跋涉并最终铸就凯歌的一条富有无限弹性的生命长河。"}
            ]
        },
        {
            "title": "第9章：时态呼应与主从复合时态法则",
            "description": "主过从必过、客观真理除外、主将从现经典语法规则。",
            "sentences": [
                {"en": "If it rains heavily tomorrow, we will stay indoors and read.", "cn": "如果明天下起倾盆大雨，我们全家就留在温馨的室内静心品茗读书（主将从现）。"},
                {"en": "He told me that he was preparing for the judicial examination.", "cn": "他昨天亲口告诉我，他当时正在为即将到来的全国统一法律职业资格大考做准备。"},
                {"en": "The teacher explained that light travels much faster than sound waves.", "cn": "物理老师在课堂上深入浅出阐明：光波传播的速度远远超越了声音震动的声波。"},
                {"en": "As soon as he arrives at the airport, I will call you.", "cn": "一旦他的航班平安降落滑行抵达机场航站楼，我立刻第一时间给你拨通电话。"},
                {"en": "She said she had already finished reading the thick historical biography.", "cn": "她微笑着轻声说道，那本厚达数百页的煌煌人物传记大作她其实早就通读完毕了。"},
                {"en": "When spring comes, the frozen mountain rivers will thaw completely.", "cn": "当温煦和煦的春姑娘重返人间之时，冰封严寒的高山江河必将彻底消融解冻。"},
                {"en": "He believed that truth would ultimately triumph over deceit and injustice.", "cn": "他始终深信不疑：真理的万丈光芒终将彻底驱散一切虚妄欺诈与不公阴霾。"},
                {"en": "Unless you practice every day, your language fluency will not improve.", "cn": "除非你能够痛下决心坚持每天脚踏实地操练，否则你的口语纯熟度决计无法突破。"},
                {"en": "She knew that her beloved mother was sleeping peacefully in bedroom.", "cn": "她心中十分清楚，自己深爱的慈母此刻正安详平稳地在里间卧室内沉睡歇息。"},
                {"en": "The ancient philosopher proved that the Earth is a spherical planet.", "cn": "那位古希腊先贤哲人严谨论证了：我们所生活的地球本质上是一颗悬浮的大球体。"},
                {"en": "Apply the present tense in conditional adverbial clauses referring to future.", "cn": "在由 if, unless 等引导的条件状语从句中，谈及未来之事一律遵循“主将从现”法则。"},
                {"en": "Shift subordinate verbs one step into the past when reporting speech.", "cn": "在间接引语转述他人言论时，从句动词时态在逻辑上严格顺延“主过从过”后退一档。"},
                {"en": "Universal physical laws and eternal truths resist temporal backshifting in subordinate clauses.", "cn": "放之四海而皆准的永恒科学定律与客观真理，在宾语从句中超然物外、绝不随主句倒退。"},
                {"en": "Syntactic harmony across complex clauses reflects disciplined, sophisticated linguistic thinking.", "cn": "在繁复交错的长难复合句中保持严丝合缝的时态和谐呼应，折射出严谨高深的语言心智。"},
                {"en": "Precision in temporal relationships is the hallmark of articulate, educated speech.", "cn": "在时态时空脉络上做到分毫不差、严丝合缝，是有教养、高素质文明谈吐的灵魂标尺。"}
            ]
        },
        {
            "title": "第10章：时态大圆满终章与双语融会贯通",
            "description": "全时态自由切换演练，掌控过去、现在与未来的语言驾驭力。",
            "sentences": [
                {"en": "I studied hard in the past, I practice now, and I will succeed.", "cn": "在过去我曾挥汗如雨苦读，在当下我心无旁骛操练，在未来我必定登顶功成！"},
                {"en": "Every accomplished master was once an uncertain and clumsy beginner.", "cn": "天下间任何一位造诣登峰造极的传世大师，在当年也曾是一个懵懂稚嫩的初学者。"},
                {"en": "By the time you finish this program, you will have transformed yourself.", "cn": "等到你彻底圆满攻克完成这整套实战体系之时，你整个人必将实现脱胎换骨的蜕变！"},
                {"en": "He has dedicated his entire career to helping underprivileged students thrive.", "cn": "他倾尽了自己整整一生的宝贵职业生涯，全心全意帮助那些家境贫寒的学子成才立业。"},
                {"en": "She was working late when the breakthrough formula finally flashed clearly.", "cn": "当那道开创性的绝妙公式灵光在脑海中豁然贯通闪现时，她当时正深夜挑灯奋战。"},
                {"en": "There is a profound beauty in mastering the temporal dimensions of English.", "cn": "随心所欲、炉火纯青地驾驭掌握英语的时态时空维度，蕴含着一种深邃崇高的大美。"},
                {"en": "Actions anchor our character, while verbs breathe living life into language.", "cn": "踏踏实实的实际行动塑造了我们的人格操守，而千变万化的动词赋予了语言磅礴生命力。"},
                {"en": "Confidence grows from daily incremental mastery, not from wishful thinking.", "cn": "无可撼动的强大从容自信，脱胎于日复一日点滴扎实的积累精进，而非虚无缥缈的幻想。"},
                {"en": "Express past heritage, present reality, and future hope with equal elegance.", "cn": "以同样优雅端庄的大将风度，自如抒发过去的深厚底蕴、当下的脚踏实地与未来的无限希望。"},
                {"en": "Punctuate your sentences with precision, and speak your convictions with courage.", "cn": "以如同钟表般严苛的精度规范好每一个标点符号，以勇毅坚决的魄力大声讲出你的信念！"},
                {"en": "You have thoroughly mastered all fundamental tenses of the English language!", "cn": "你已经彻彻底底、融会贯通攻克掌握了英语语言全部核心基础时态体系！"},
                {"en": "Language is the royal vehicle of reason, emotion, and human connection.", "cn": "语言是人类理性求索、情感交融抒发以及跨越山海心心相印的至尊通途载体。"},
                {"en": "Your disciplined dedication has laid a rock-solid foundation for lifelong mastery.", "cn": "你长期以来高度自律的倾情付出，已经为铸就终身精熟驾驭卓越英语奠定了坚如磐石的基座。"},
                {"en": "Go forward boldly, speak without hesitation, and write with profound eloquence.", "cn": "大步流星勇敢向前迈进吧，开口交流时不再有丝毫犹疑怯懦，下笔成文时充满锦绣文采！"},
                {"en": "The whole world of fluent English expression belongs proudly to you today!", "cn": "从今天起，整个辽阔纯正、地道流利的地道英语表达大千世界，骄傲地完完全全属于你！"}
            ]
        }
    ]
}

print("COURSE_BASIC_1000WORDS, PATTERNS, TENSES ready")
