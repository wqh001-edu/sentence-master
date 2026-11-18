# -*- coding: utf-8 -*-
from builder_core import build_course

def get_movies_part2():
    courses = []

    # 5. 《星际穿越》(Interstellar)
    courses.append(build_course({
        "id": "course-mov-interstellar",
        "title": "《星际穿越》(Interstellar) · 爱与时空维度的科幻史诗 (10章全集)",
        "category": "movies",
        "categoryName": "影视英语",
        "coverGradient": "from-slate-900 via-indigo-950 to-blue-900",
        "icon": "🚀",
        "description": "诺兰执导科幻神作，穿越浩瀚虫洞与黑洞视界，用超越时空维度的爱拯救人类文明。",
        "difficulty": "高级 C1",
        "tags": ["硬核科幻", "诺兰神作", "黑洞时空", "震撼独白"]
    }, [
        {
            "title": "第 1 幕 · 沙尘暴肆虐的荒芜地球与幽灵书架",
            "description": "地球生态崩溃，库珀在女儿墨菲的书架上发现了神秘引力异常代码。",
            "sentences": [
                {"en": "We used to look up at the sky and wonder at our place in the stars.", "cn": "我们曾经仰望璀璨星空，思索我们在浩瀚宇宙群星之中的位置。"},
                {"en": "Now we just look down and worry about our place in the dirt.", "cn": "而现在我们却只能低头俯瞰黄土，担忧自己在这片荒凉泥土中的苟活容身之处。"},
                {"en": "Mankind was born on Earth, but it was never meant to die here.", "cn": "人类诞生在地球，但人类绝不该注定在这颗星球上走向终结灭绝。"},
                {"en": "Don't go gentle into that good night; rage against the dying of the light.", "cn": "不要温和地走入那良夜；应当在光芒渐熄时愤怒咆哮，竭力抗争！(经典诗句)"},
                {"en": "My daughter thought there was a ghost in her bedroom trying to communicate.", "cn": "我女儿一直以为她卧室的书架后面躲着一个试图与她沟通对话的幽灵。"},
                {"en": "Gravity is the only physical force capable of traversing multiple dimensions.", "cn": "引力是自然界中唯一一种能够自由穿越多重维度的基本物理力量。"},
                {"en": "We must accept that our generation is the very last one capable of survival.", "cn": "我们必须痛苦地接受现实：我们这一代人是地球上最后一批勉强能够存活的人类了。"},
                {"en": "The dust storms have choked the wheat crops and only corn remains.", "cn": "遮天蔽日的沙尘暴彻底扼杀了小麦作物，如今地里仅剩下为数不多的玉米尚能苟延残喘。"},
                {"en": "I gave my little girl a promise that I would return, no matter how far I go.", "cn": "我曾向我的小女儿许下郑重诺言：无论我远行到多么遥远的星海，我必定平安归来。"},
                {"en": "A father should never have to make a promise that he might not be able to keep.", "cn": "一个为人父者永远不该许下一个他可能竭尽全力也无法遵守兑现的誓言。"},
                {"en": "You have to be a parent to truly understand how terrifying the universe is.", "cn": "唯有你真正身为人父人母，才能深切体会面对这冷酷宇宙时内心有多么恐惧。"},
                {"en": "We don't need engineers or dreamers anymore; we simply need caretakers and farmers.", "cn": "如今的社会已经不再需要工程师或梦想家了；我们单纯只需要懂得照料庄稼的农夫。"},
                {"en": "The binary coordinates etched in the dust floor pointed directly to this secret facility.", "cn": "沙尘地板上刻下的神秘二进制坐标，精准无误地指向了这座深藏地底的绝密科研基地。"},
                {"en": "Tell me you're not going to leave me here all alone in the dark.", "cn": "求求你告诉我，你绝对不会把我一个人孤独地抛下，丢在无边无际的黑暗深渊里。"},
                {"en": "I love you, Murph, and I will cross the vast cosmic void to see you again.", "cn": "我深爱着你，墨菲，我即便跨越浩瀚无垠的宇宙虚空，也一定会再次与你相聚。"}
            ]
        },
        {
            "title": "第 2 幕 · 徘徊者飞船点火升空告别母星",
            "description": "离开地球引力井，四位无畏的探险家背负着全人类最后的火种驶向深空。",
            "sentences": [
                {"en": "Stage one separation confirmed; we have officially broken through the atmospheric ceiling.", "cn": "一级火箭分离确认完毕；我们已经正式突破地表大气层顶端，冲向深空。"},
                {"en": "Look back at our blue marble one final time before darkness swallows the horizon.", "cn": "在冰冷深邃的黑暗彻底吞噬地平线之前，最后深情回望一眼我们那颗蔚蓝的母星弹珠吧。"},
                {"en": "Silence in outer space is absolute and deafening to the human spirit.", "cn": "外层空间里的极度死寂是如此纯粹彻底，甚至足以震慑摧垮任何人类的心灵意志。"},
                {"en": "Our primary mission is to assess the viability of three candidate habitable worlds.", "cn": "我们此次出征的首要核心使命，是实地评估三颗候选宜居系外行星的生命承载潜力。"},
                {"en": "Ten years ago, the Lazarus missions sent solitary pioneers into the great unknown.", "cn": "十年前，“拉撒路计划”派遣了数位孤独的勇敢先驱，毅然决然投身于未知的茫茫星海。"},
                {"en": "We owe it to those brave pioneers to follow the breadcrumbs of their telemetry beacons.", "cn": "我们有坚定的道义责任，顺着那些英勇先驱发射的遥测信标信号轨迹一路追寻。"},
                {"en": "Every milligram of fuel has been calculated with ruthless mathematical precision.", "cn": "飞船推进剂的每一毫克消耗，都经过了近乎冷酷无情的严苛数学精准推演计算。"},
                {"en": "Prepare the hibernation chambers; the transit to Saturn will take two long years.", "cn": "迅速准备好深度休眠舱；前往土星轨道的漫长航行将耗费整整两年的漫长时间。"},
                {"en": "Artificial gravity feels strange after floating weightless in microgravity for hours.", "cn": "在微重力环境下失重漂浮数小时之后，重新踩上人造离心重力地板的感觉格外奇妙怪异。"},
                {"en": "The robotic companion TARS possesses a humor setting that can be adjusted freely.", "cn": "智能机器人伙伴塔斯配备了幽默度调节参数，我们可以根据喜好随时自由设定高低。"},
                {"en": "Let's set your humor parameter to seventy-five percent so you don't annoy the crew.", "cn": "咱们把你的幽默参数设定在百分之七十五吧，免得你那冷幽默把全副机组人员惹毛。"},
                {"en": "Survival instincts will be our greatest asset and our most dangerous vulnerability.", "cn": "刻在基因深处的求生本能，既会是我们最宝贵的生存武器，也会成为最危险的致命软肋。"},
                {"en": "We are ambassadors of an entire biological history striving not to perish.", "cn": "我们肩负重任，是整个地球生命演化史的无畏信使，竭尽全力抗争不被历史彻底抹去。"},
                {"en": "Good night, commander; see you on the icy rings of Saturn in twenty-four months.", "cn": "晚安，指挥官；期待二十四个月之后，在土星那冰洁璀璨的光环之畔与您再次并肩。"},
                {"en": "The spaceship drifted like a lonely speck of silver against the velvet black cosmos.", "cn": "宇宙飞船宛如一粒孤独渺小的银色微尘，静静漂泊在天鹅绒般漆黑深邃的茫茫宇宙之中。"}
            ]
        },
        {
            "title": "第 3 幕 · 穿越土星虫洞与四维时空假说",
            "description": "神秘高级文明留下的虫洞球体，连接着千万光年外的遥远黑洞星系。",
            "sentences": [
                {"en": "A wormhole is not a flat portal; in three dimensions, it manifests as a perfect sphere.", "cn": "虫洞绝不是平面圆形隧道；在三维空间直观呈现下，它其实是一个完美的时空球体。"},
                {"en": "Whoever placed this distortion near Saturn is deliberately extending a cosmic lifeline.", "cn": "无论究竟是何方神圣将此时空弯曲通道安放在土星近旁，他们显然是在蓄意向人类施以援手。"},
                {"en": "As we cross the throat of the wormhole, normal space-time topology completely bends.", "cn": "当我们毅然穿梭穿越虫洞咽喉要道时，常规的三维平直时空拓扑结构瞬间发生剧烈扭曲。"},
                {"en": "Light from distant unmapped galaxies cascades across our observation viewport.", "cn": "来自数千万光年之外未被编目的遥远星系幽幽星光，如瀑布般倾泻在我们观测视窗玻璃上。"},
                {"en": "We have emerged into a binary star system anchored by a supermassive black hole.", "cn": "我们成功跃迁脱出，出现在了一个以超大质量旋转黑洞为核心引力锚点的双星宿系统之中。"},
                {"en": "They call the monstrous spinning black hole Gargantua, a behemoth of infinite density.", "cn": "他们将那个吞噬一切的庞大自旋黑洞命名为“卡冈图雅”，一个蕴含无限时空密度的恐怖巨兽。"},
                {"en": "Time dilation near such a colossal gravitational well will be brutally severe.", "cn": "紧贴着如此庞大可怖的超强引力深渊，时间膨胀效应将会残酷到令人胆寒的极致地步。"},
                {"en": "Every decision we make in this gravity gradient costs precious decades back on Earth.", "cn": "我们在这道极端引力陡坡上做出的每一个迟疑抉择，都会让地球上的亲人平白耗费数十年青春。"},
                {"en": "Can you feel the metaphysical weight of time slipping away like grains of dry sand?", "cn": "你是否真切感受到了岁月时光如同干燥细沙般从指缝狂暴溜走的那种形而上沉重窒息感？"},
                {"en": "Physics does not negotiate with human sentimentality or tearful emotional pleas.", "cn": "严酷客观的物理学定律绝不会与人类脆弱的感伤情绪或声泪俱下的哀求讨价还价。"},
                {"en": "We are venturing into realms where classical mechanics dissolves into quantum mysteries.", "cn": "我们正在义无反顾地踏足经典力学彻底瓦解、量子谜题完全主宰一切的神秘禁忌领域。"},
                {"en": "The glowing accretion disk of Gargantua burns brighter than a thousand brilliant suns.", "cn": "卡冈图雅黑洞外围那道耀眼绚烂的发光吸积盘，绽放出的耀斑光辉远超千百个烈日骄阳。"},
                {"en": "Keep the navigation thrusters locked on the orbital trajectory of Miller's planet.", "cn": "务必将姿态导航推进器死死锁定在米勒水行星的引力环绕轨道交汇切线之上。"},
                {"en": "No human beings have ever witnessed such awe-inspiring cosmic architecture firsthand.", "cn": "在人类漫长历史上，此前从未有任何生灵能有幸亲眼目睹如此波澜壮阔、摄人心魄的宇宙结构。"},
                {"en": "Brace for orbital insertion burn; we are diving deep into the gravitational valley.", "cn": "全员做好轨道切入变轨点火抗压准备；我们即将向着万劫不复的极端引力幽谷俯冲而下。"}
            ]
        },
        {
            "title": "第 4 幕 · 米勒水行星：一小时换算地球七年",
            "description": "齐膝深的平静汪洋之下，耸立着如摩天大楼般的四千米滔天巨浪。",
            "sentences": [
                {"en": "One hour on this watery surface equals seven full years back home on Earth.", "cn": "在这片汪洋水行星表面逗留区区一个小时，就等同于母星地球上整整七个春去秋来的寒暑。"},
                {"en": "Do not waste a single second; locate the transponder beacon and retrieve the recorder.", "cn": "争分夺秒，绝不许浪费哪怕一秒钟；立刻定位应答机信标，回收先驱者的数据记录仪！"},
                {"en": "The water level is only knee-deep, stretching endlessly toward the curved horizon.", "cn": "举目四望，这里的水深仅仅齐膝，平静无波，一直向着弯曲的地平线无边无际绵延展开。"},
                {"en": "Where are the mountains you reported seeing on the distant horizon scanner?", "cn": "你刚才在远程地形雷达扫描仪上报告说看到的巍峨远山，究竟伫立在何方？"},
                {"en": "Those aren't mountains; those towering shadows are colossal tidal waves moving toward us!", "cn": "那根本不是什么群山；那些遮天蔽日的巍峨阴影，是正在以超音速向我们扑来的万丈滔天巨浪！"},
                {"en": "Get back to the landing craft immediately before the crest of the wave crushes us!", "cn": "所有人立刻不顾一切撤回着陆飞船舱内，在巨浪峰顶将我们拍成齑粉之前！"},
                {"en": "The engines are completely waterlogged; we have to wait for the drainage purge cycle.", "cn": "主火箭发动机进气道彻底灌满了海水；我们必须焦急等待排空自净循环倒计时结束。"},
                {"en": "We lost Doyle to the ocean swells, and minutes ticked away like irreplaceable centuries.", "cn": "多伊尔不幸被汹涌狂暴的怒涛永远卷走，而宝贵的分秒流逝在此刻犹如无法挽回的漫长世纪。"},
                {"en": "By the time we docked back with the Endurance, twenty-three years had elapsed outside.", "cn": "当我们历经千辛万苦重新对接上耐力号母船时，外面的主时空已经无情流逝了整整二十三年。"},
                {"en": "Our companion Romilly had aged twenty-three years waiting all alone in cold silence.", "cn": "我们留守的伙伴罗米利在冰冷死寂的母船里苦苦守候，独自一人苍老了整整二十三载春秋。"},
                {"en": "I watched twenty-three years of video transmissions from my children in one agonizing afternoon.", "cn": "我在一个痛苦万分的下午，一口气看完了儿女们在这二十三年间发来的所有录像家书。"},
                {"en": "My little boy graduated, got married, and buried his firstborn child without me.", "cn": "我的小男孩大学毕业了，成家立业了，甚至在没有我陪伴的岁月里，悲伤安葬了他的长子。"},
                {"en": "Murph is now the exact same age that I was when I kissed her forehead goodbye.", "cn": "我的小墨菲如今出落得亭亭玉立，年龄正好与当年我亲吻她额头依依惜别时完全一模一样。"},
                {"en": "Time is an unforgiving predator that devours youth, relationships, and human promises.", "cn": "无情的时间是一头嗜血的凶残掠食者，贪婪吞噬着青春、人世羁绊以及人类许下的所有诺言。"},
                {"en": "We can never afford another chronological blunder like that again if we wish to succeed.", "cn": "如果我们还渴望最终取得成功，我们人类此生就再也经不起如此惨烈的时间挥霍失误了。"}
            ]
        },
        {
            "title": "第 5 幕 · 曼恩博士冰原星球的绝望叛变",
            "description": "最受敬仰的科学巨擘，在无边无际的极寒孤独中被生存本能完全腐化。",
            "sentences": [
                {"en": "Dr. Mann was considered the remarkable best of us, the bravest mind of the decade.", "cn": "曼恩博士曾经被公认为我们所有人中最卓越的楷模，是整整十年间思想最勇敢坚毅的领袖。"},
                {"en": "The landscape here is an unforgiving wilderness of frozen clouds and toxic ammonia.", "cn": "这颗星球的地表是一片冷酷无情的荒凉绝境，处处充斥着冻结如铁的冰云与剧毒氨气。"},
                {"en": "He falsified the habitability data because he could not bear dying here all alone.", "cn": "他蓄意伪造了宜居生态的勘测数据，只因他脆弱的心灵根本无法承受孤独死在异乡的绝望。"},
                {"en": "When faced with the prospect of utter oblivion, humanity reveals its darkest cowardice.", "cn": "当直面万劫不复的彻底消亡前景时，人性往往会不可遏制地暴露出其最丑陋阴暗的懦弱。"},
                {"en": "You don't know what it feels like to awaken to infinite silence day after solitary day.", "cn": "你根本无法体会日复一日在无穷无尽的孤寂死寂中绝望醒来，究竟是何等摧残折磨的滋味。"},
                {"en": "Mann cracked Cooper's helmet visor in a savage struggle on the icy precipice.", "cn": "在冰雪悬崖边的一场野蛮殊死肉搏搏斗中，曼恩疯狂打碎了库珀宇航服面罩的有机玻璃。"},
                {"en": "Suffocating on a foreign alien world strips away every layer of civilized dignity.", "cn": "在遥远的外星异界上窒息濒死，会瞬间剥除掉文明社会赋予一个人的所有尊严与体面。"},
                {"en": "Cooper fought frantically for every breath while calling for rescue on an open frequency.", "cn": "库珀在开通的公开应急无线电频道里拼死呼救，为了每一口仅存的氧气进行着殊死挣扎。"},
                {"en": "Mann attempted an unauthorized manual docking with the Endurance command module.", "cn": "利欲熏心的曼恩博士孤注一掷，企图强行以手动模式强行对接耐力号母船的核心指挥舱。"},
                {"en": "The airlock pressure seal failed catastrophically, blowing the station into a violent spin.", "cn": "气闸舱的压力密封环瞬间发生了灾难性结构解体爆炸，直接将整个空间站炸入剧烈狂暴翻滚。"},
                {"en": "The Endurance is rotating at sixty-seven revolutions per minute toward the planetary atmosphere.", "cn": "严重受损的耐力号母船正在以每分钟六十七转的骇人疯狂自转速度，坠向行星厚重的大气层。"},
                {"en": "Case, analyze the rotational frequency of the station and match our spin thruster for thruster.", "cn": "凯斯，立刻精确解析受损空间站的旋转角频率，操控我们的推进器实行一比一同步共振对齐！"},
                {"en": "It's not possible to dock under these extreme angular velocities, Cooper! No, it's necessary.", "cn": "在如此极端的疯狂角速度下根本不可能完成对接，库珀！——不，这不是可不可能，这是必须！"},
                {"en": "By matching the violent spin centimeter by centimeter, Cooper pulled off an aerodynamic miracle.", "cn": "通过厘米级的惊人精度咬合那疯狂翻滚的自转节拍，库珀奇迹般上演了一场载入史册的对接神话。"},
                {"en": "We retrieved the burning ship from the brink of total annihilation at an immense cost.", "cn": "我们付出了极其惨烈的沉痛代价，终于从万劫不复的粉碎深渊边缘硬生生抢救回了燃烧的母船。"}
            ]
        },
        {
            "title": "第 6 幕 · 坠入黑洞卡冈图雅与引力弹弓",
            "description": "燃料告罄之际，库珀选择脱离抛弃自身，将布兰德博士推向最后的希望。",
            "sentences": [
                {"en": "We have insufficient fuel to escape the gravitational clutches of Gargantua.", "cn": "飞船现存的剩余推进燃料，根本不足以让我们合力逃脱超大质量黑洞卡冈图雅的恐怖引力魔爪。"},
                {"en": "The only viable trajectory is a slingshot maneuver scraping past the event horizon.", "cn": "唯一切实可行的脱困轨道方案，就是贴着黑洞事件视界边缘进行一次极度凶险的引力弹弓加速。"},
                {"en": "Newton's third law of motion dictates that you have to leave something behind to move forward.", "cn": "牛顿第三运动定律残酷无情地昭示着：你若渴望向前飞驰，就必须舍弃并留下一些沉重代价。"},
                {"en": "TARS will detach first to transmit quantum telemetry data from within the singularity.", "cn": "塔斯将首先脱离母船舱体，只身坠入黑洞，力图从奇点核心内部发回绝密的量子遥测数据。"},
                {"en": "Cooper decoupled his own craft secretly, sacrificing his life so Brand could survive.", "cn": "库珀暗中决绝按下了手动解脱锁栓，甘愿牺牲自己的生命，只为换取布兰德博士一线生机。"},
                {"en": "Do not detach, Cooper! There is still another way to make the numbers work!", "cn": "千万不要脱离飞船，库珀！我们一定还有其他计算模型能够让燃料平衡运转起来的！"},
                {"en": "Detach confirmed; goodbye, Brand, and plant our seeds on Edmunds' promised world.", "cn": "分离确认完毕；永别了，布兰德，带着全人类最后的胚胎火种，在埃德蒙兹的希望星球上生根发芽吧。"},
                {"en": "The ranger plummeted into an infinite cascade of darkness where all known physics ceased.", "cn": "漫游者飞船呼啸着坠入了深不见底的永恒黑暗瀑布之中，那里的所有已知物理定律皆尽灰飞烟灭。"},
                {"en": "The gravitational gradient tore the metallic hull apart like brittle autumn parchment.", "cn": "狂暴的引力潮汐梯度撕裂坚固的合金飞船外壳，犹如随手撕碎脆弱干燥的秋日羊皮纸卷。"},
                {"en": "Ejecting into the void, Cooper felt himself suspended outside the very concept of time.", "cn": "紧急弹射进虚无的一刹那，库珀惊觉自己仿佛被悬置抽离在了“时间”这一概念的本体维度之外。"},
                {"en": "Sensory overload blinded his eyes as geometric grids folded across higher dimensions.", "cn": "五维几何晶格在更高维度中疯狂交叠折叠，排山倒海般的信息过载瞬间夺去了他的视觉感知。"},
                {"en": "He did not perish in the gravitational crusher; instead, he breached a hypercube construct.", "cn": "他并未在恐怖的引力粉碎机中粉身碎骨；相反，他奇迹般突破闯入了一座宏伟的五维超正方体之中。"},
                {"en": "Whoever built this extra-dimensional sanctuary understood the fragile physiology of mankind.", "cn": "无论究竟是何方神圣构筑了这座跨维度庇护所，他们显然极其深刻洞悉人类脆弱的生理构造特征。"},
                {"en": "Falling through infinite vertical corridors of light, he beheld Murph's childhood bedroom.", "cn": "顺着无穷无尽的垂直光芒回廊悠然飘落，映入他眼帘的，竟是女儿墨菲童年时代的那间卧室。"},
                {"en": "Every tick of the universe had been materialized into an accessible spatial cord.", "cn": "这整个宇宙中流淌过的每一道光阴节拍，在此处竟然全都被具象实体化为了触手可及的琴弦丝线。"}
            ]
        },
        {
            "title": "第 7 幕 · 五维超立方体与引力波时空琴弦",
            "description": "高级文明不是外星人，而是未来进化的人类自己构建的时间图书馆。",
            "sentences": [
                {"en": "This place is a physical construct translating fourth-dimensional time into traversable space.", "cn": "这座奇妙神圣的居所是一座物理构型，将不可逆的四维时间精准具象转化为可以自由穿梭的三维空间。"},
                {"en": "They didn't build this realm for themselves; they built it as a conduit for me to communicate.", "cn": "那些神秘的高维存在绝不是为他们自己建造此地；他们是为我量身定制了这道隔空对话的信道。"},
                {"en": "They are not aliens from another galaxy; they are our very own distant human descendants.", "cn": "他们根本不是来自其他遥远星系的外星异种；他们正是我们人类历经万世进化之后的遥远未来子孙。"},
                {"en": "Humans evolved beyond physical form, transcending the boundaries of three spatial axes.", "cn": "未来的新人类彻底超脱了肉身皮囊的物理桎梏，超凡跃迁脱离了区区三个空间维度的束缚牢笼。"},
                {"en": "Time can be stretched, compressed, or wrapped, but it cannot run backward for mortal flesh.", "cn": "对于肉体凡胎而言，时间可以被引力肆意拉伸、挤压或包裹，却唯独绝不可能自行倒流逆转。"},
                {"en": "Only one singular force in the cosmos can exert an active influence across every dimension.", "cn": "在广袤的大千宇宙之中，唯独只有一种超凡卓绝的磅礴力量，能够跨越所有维度施加实质影响。"},
                {"en": "Love is not an invention of sentimental human poets; love is an observable cosmic resonance.", "cn": "爱绝不是多愁善感的人类诗人凭空捏造的虚幻幻象；爱是宇宙深处真实可观测的一种崇高共振。"},
                {"en": "My connection with Murph is the navigational compass that guided me across the abyss.", "cn": "我与墨菲之间心心相印的血脉相通羁绊，正是一路引领我横渡这万劫虚空深渊的精准导航罗盘。"},
                {"en": "I was her ghost all along; every unexplained event was my desperate cry from the future.", "cn": "原来从始至终，我就是那个神秘的幽灵；书架上每一次无法解释的异象，全是我来自未来的绝望呐喊。"},
                {"en": "I hammered on the dimensional strings, knocking dust and vintage books to the floorboards.", "cn": "我近乎疯狂地狂暴拨动着时空维度的琴弦，将大片大片的沙尘与泛黄的古旧书本震落向地板。"},
                {"en": "I spelled out 'STAY' in Morse code, weeping because my past self would never heed the warning.", "cn": "我用摩斯密码一遍遍绝望拼写着“留下”；我痛哭流涕，只因曾经那个固执的自己终究未曾听从警示。"},
                {"en": "TARS contacted my headset; he had successfully decoded the quantum data of the singularity.", "cn": "塔斯的声音突然在我的无线电耳机中激动响起；他竟然成功彻底破译了黑洞奇点核心的量子方程数据。"},
                {"en": "We can translate this mathematical breakthrough into gravity equations to lift mankind.", "cn": "只要将这一震撼性的数学突破转译为引力工程方程，人类便能掌握反重力技术，举族撤离死地！"},
                {"en": "How can I transmit complex quantum calculations through a wooden bookshelf across time?", "cn": "我究竟该如何隔着重重时空迷雾，通过一面普通的古旧木制书架，将浩繁复杂的量子算式传递出去？"},
                {"en": "The wristwatch! The mechanical wristwatch I left behind on her nightstand before departure!", "cn": "手表！正是我当年在启程远征之前，深情留在她床头柜上的那块精密机械指针腕表！"}
            ]
        },
        {
            "title": "第 8 幕 · 秒针上的摩斯密码与拯救全人类",
            "description": "用引力微粒拨动机械表秒针，成年墨菲终于解开了跨时空的父爱谜题。",
            "sentences": [
                {"en": "Cooper used subtle gravitational pulses to articulate the second hand of the heirloom watch.", "cn": "库珀运用精微入微的引力脉冲波，极其耐心细致地一下一下拨动着那块传家手表的纤细秒针。"},
                {"en": "Tick, pause, tick-tick; the mechanical rhythm pulsed with pure mathematical revelation.", "cn": "滴答，稍歇，滴答滴答；这有条不紊的机械节律之中，跳动闪耀着拯救人类文明的纯粹数学真理。"},
                {"en": "Across light-years and decades, Murph returned to her desolate childhood home in search of answers.", "cn": "跨越漫漫光年与数十载光阴，成年的墨菲毅然重返荒凉寂寥的童年老宅，苦苦搜寻救赎的终极答案。"},
                {"en": "She noticed the abnormal, synchronized twitching of the vintage watch's slender second hand.", "cn": "她终于敏锐地注意到了那块古董手表纤细秒针呈现出的极其反常、富有规律性的奇特抽搐律动。"},
                {"en": "It's not a malfunction; it's a deliberate code! He came back for me through the ghost!", "cn": "这绝不是机械故障失灵；这是蓄意发来的密码！他通过那个幽灵，真的跨越时空回来看我了！"},
                {"en": "Transcribing the dots and dashes, she filled dozens of chalkboards with elegant tensor calculus.", "cn": "飞速抄录下那接连不断的点杠摩斯密码，她兴奋地将数十块巨大黑板填满了精妙绝伦的张量微积分。"},
                {"en": "The riddle of gravitational manipulation has been solved once and for all by a farmer's daughter.", "cn": "困扰了顶尖物理学界半个世纪的引力操控终极世纪谜题，终于由一位农夫的女儿彻底解开！"},
                {"en": "She ran through the research corridors tossing papers into the air, screaming 'Eureka!' in triumph.", "cn": "她狂喜地狂奔在科研大楼的回廊上，将漫天讲义白纸抛洒向空中，满怀胜利凯旋的高呼着“找到了”！"},
                {"en": "With the completed gravitational equation, humanity could launch massive orbital colonies effortlessly.", "cn": "凭借这套大一统的完整引力调控方程，人类终于能够轻而易举地将重达数亿吨的巨型太空城送入轨道。"},
                {"en": "The tesseract began to collapse as its purposeful historical function reached completion.", "cn": "伴随着这一历史使命的功德圆满达成，支撑五维超立方体的时空支柱开始平静地优雅坍缩。"},
                {"en": "Falling unconscious through closing rifts of spacetime, Cooper whispered his final words of gratitude.", "cn": "在缓缓合拢的时空裂隙之中渐渐失去意识下坠，库珀唇边泛起微笑，轻声呢喃出道不尽的感恩之词。"},
                {"en": "The future beings closed the temporal bridge, gently casting him into the vicinity of Saturn.", "cn": "未来的超维生命缓缓闭合了时空隧道的宏伟大桥，温存地将他送回到了土星公转轨道的近旁。"},
                {"en": "A search-and-rescue patrol detected an anomalous thermal signature drifting near the planetary rings.", "cn": "一支巡逻搜救飞船编队在土星环近旁，敏锐捕获到了一道微弱但依然存活的异常生命热源特征。"},
                {"en": "You have been asleep for a very long time, Mr. Cooper; welcome to the dawn of a new era.", "cn": "您已经沉睡了极其漫长而壮阔的岁月了，库珀先生；由衷欢迎您光临人类崭新纪元的灿烂黎明。"},
                {"en": "The impossible sacrifice had paid off; civilization had escaped the suffocating cradle of Earth.", "cn": "看似绝无可能完成的伟大牺牲终于迎来了奇迹硕果；整个人类文明终于成功挣脱了地球那窒息的摇篮。"}
            ]
        },
        {
            "title": "第 9 幕 · 库珀太空城与重见白发女儿",
            "description": "离开时她是十岁幼女，再见时已是百岁垂暮功勋；唯有爱与诺言未曾褪色。",
            "sentences": [
                {"en": "He woke up in an immaculate medical suite overlooking curved landscapes inside an O'Neill cylinder.", "cn": "他在一间一尘不染的高级医疗套房中幽幽苏醒，举目便能俯瞰奥尼尔圆筒太空城内弯曲向上的人造大地。"},
                {"en": "You are currently aboard Cooper Station, named not after you, but after your brilliant daughter.", "cn": "您当前正身处“库珀太空站”内部，而这座空间站的名字并非因您命名，而是为了致敬您非凡的女儿。"},
                {"en": "By the relative standard of Earth calendar years, you are currently one hundred and twenty-four years old.", "cn": "若是按照母星地球公历纪年的相对时间标准来推算，您如今的真实生理与历法年龄已是一百二十四岁了。"},
                {"en": "Yet looking in the mirror, his face was still that of an able-bodied man in his late thirties.", "cn": "然而凝视着穿衣镜中的倒影，他的容颜却依然停留在三十多岁那个身强力壮、血气方刚的干练男子模样。"},
                {"en": "She was placed into cryogenic stasis two weeks ago just to survive long enough to see your face.", "cn": "两周前她毅然决定进入深度低温休眠，仅仅是为了让自己残存的生命多撑几天，好亲眼再看您一面。"},
                {"en": "Entering the hospital room, Cooper saw an elderly matriarch surrounded by generations of family.", "cn": "缓缓推开病房房门，映入库珀眼帘的，是一位白发苍苍、子孙满堂、被数代晚辈簇拥着的可敬老妪。"},
                {"en": "You came back; I always knew deep down in my heart that you would keep your word.", "cn": "你终于回来了；在我心灵深处最柔软的角落，我从始至终坚信你一定会信守当年的誓言。"},
                {"en": "Nobody believed me, but I knew the ghost was my dad coming to rescue us from the dust.", "cn": "当年根本没有任何一个人肯相信我的胡话，但我心里比谁都清楚：那个幽灵就是我无所不能的爸爸！"},
                {"en": "Tears streamed down Cooper's weathered cheeks as he held the frail, spotted hand of his little girl.", "cn": "泪水止不住地滑落过库珀饱经风霜的脸颊，他紧紧握住自己小女儿那双苍老瘦弱、布满老年斑的手。"},
                {"en": "No parent should ever have to watch their own child die of old age, Murph whispered gently.", "cn": "没有任何一位父母应该眼睁睁看着自己的孩子老死在自己怀里，墨菲抚摸着父亲的脸庞轻声温言。"},
                {"en": "You have your own path forward now; do not remain stranded as a living relic of my past.", "cn": "你如今拥有属于你自己的辽阔征程要去开拓；绝不要停下脚步，沦为困在我早已消逝过往里的活化石。"},
                {"en": "Brand is all alone out there, settling a brand-new cradle for mankind under unfamiliar alien stars.", "cn": "布兰德此刻还在遥远深空的彼岸孤军奋战，在陌生的外星繁星之下，独自为人类开辟崭新的生活摇篮。"},
                {"en": "Go to her, Cooper; let the living build tomorrow while we honor what we left behind.", "cn": "去找她吧，库珀；让我们安详长眠致敬曾经的过往，而属于活着的人的使命，是昂首阔步开创明天。"},
                {"en": "He kissed her forehead one final time, a sacred gesture sealing a lifetime of cosmic separation.", "cn": "他最后一次庄严深情地亲吻了她的额头，这一神圣的吻，为这跨越浩瀚星海一生的漫长离别画上了圆满句点。"},
                {"en": "The legacy of Murph Cooper was secured forever in the radiant survival of the human species.", "cn": "墨菲·库珀的崇高功勋与无上荣光，已经与整个人类文明在浩瀚星辰间的永恒繁衍永远融为一体。"}
            ]
        },
        {
            "title": "第 10 幕 · 孤星寻觅与奔向新世界",
            "description": "修复好塔斯机器人，库珀再次驾驶飞船跃入星海，奔向埃德蒙兹星球的布兰德。",
            "sentences": [
                {"en": "Quietly slipping into the maintenance bay, Cooper reactivated his faithful companion TARS.", "cn": "库珀悄然步入寂静的检修机库，亲手重新唤醒了他忠诚无二、患难与共的智能机械伙伴塔斯。"},
                {"en": "What is your cue, Cooper? Stealing an advanced scout craft to embark on an unsanctioned voyage?", "cn": "你下一步有何打算，库珀？难道是打算顺手偷走一艘最先进的侦察飞船，去执行一场未经批准的远征？"},
                {"en": "Setting TARS's honesty parameter to ninety percent, Cooper grinned with familiar roguish determination.", "cn": "将塔斯的诚实度参数顺手调回百分之九十，库珀唇角扬起一抹大家无比熟悉的执拗果决坏笑。"},
                {"en": "A pilot belongs in the boundless expanse of the void, not gardening inside a rotating metal cylinder.", "cn": "一名真正的传奇飞行员生来便属于浩瀚无垠的宇宙深空，绝不该蜷缩在旋转的金属圆筒里伺候花草。"},
                {"en": "Across the wormhole on Edmunds' distant planet, the atmosphere is breathable and the soil fertile.", "cn": "在穿过虫洞之后的埃德蒙兹遥远星球上，空气清新宜人适合呼吸，肥沃的土壤散发着生机。"},
                {"en": "Dr. Brand removed her helmet, feeling the gentle touch of an alien breeze against her skin.", "cn": "布兰德博士缓缓摘下了厚重的宇航服头盔，深情感受着外星轻柔微风拂过她脸庞肌肤的温润触感。"},
                {"en": "She stood by a solitary cairn of stones, honoring the lover who gave his life for this sanctuary.", "cn": "她静静肃立在一座孤独的石堆衣冠冢旁，深深缅怀为了寻觅这片宁静乐土而献出宝贵生命的挚爱。"},
                {"en": "Behind her, the embryonic incubators of the new human civilization hummed with quiet promise.", "cn": "在她身后，孕育着整个人类崭新文明火种的低温胚胎培养舱，正在安静沉稳地发出希望的低鸣。"},
                {"en": "She was alone in the quiet light of an alien sun, preparing for the long wait ahead.", "cn": "在一轮陌生的暖阳洒下的柔和日光中，她孑然独立，平静从容地准备迎接前方漫长未知的等待。"},
                {"en": "The scout craft ignited its ion drives, slicing through the darkness back toward the Saturn anomaly.", "cn": "崭新的侦察飞船骤然点燃璀璨的离子推进器，如一道锐利银色闪电刺破黑暗，重新驶向土星引力奇点。"},
                {"en": "Two brave explorers, separated by light-years of silence, bound by the immortal thread of love.", "cn": "两位无畏的孤勇探险家，纵使相隔着亿万光年的浩瀚死寂，却被大爱这根跨越时空的永恒丝线牢牢紧系。"},
                {"en": "Man was never destined to wither and fade away on a ruined, dust-covered cradle.", "cn": "人类生来就绝不注定在这座破败不堪、黄沙漫天的荒凉摇篮之中枯萎凋零、默默化为历史尘埃。"},
                {"en": "We will cultivate new gardens among the distant stars and build cities beneath foreign constellations.", "cn": "我们必将在遥远彼岸的群星之间开辟出繁花似锦的沃土花园，在异邦星图之下拔地筑起宏伟的万城！"},
                {"en": "Do not go gentle into that good night; our voyage across the cosmos has only just begun.", "cn": "绝不要温和地走入那良夜；我们人类征服浩瀚星辰大海的宏伟壮阔史诗，才刚刚拉开壮丽序幕！"},
                {"en": "Somewhere out there beneath a strange alien sky, she is waiting for him to arrive.", "cn": "在遥远星河彼岸那片未知的异邦苍穹之下，她始终坚信，那个无所不能的男人终将穿越星海如约而至。"}
            ]
        }
    ]))

    return courses
