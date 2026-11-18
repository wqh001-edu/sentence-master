# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))

from builder_core import build_course

def get_exam_part3_courses():
    courses = []

    # -------------------------------------------------------------------------
    # 5. 托福高分学术讲座与独立写作精炼 (10章) - 严格每章15句，共150句
    # -------------------------------------------------------------------------
    toefl_meta = {
        "id": "course-ex-toefl",
        "title": "《托福高分学术讲座与独立写作精炼》(TOEFL iBT) · 北美大学学术语境 (10章全集)",
        "category": "exam",
        "categoryName": "考试备考",
        "coverGradient": "from-teal-800 via-cyan-900 to-slate-900",
        "icon": "🗽",
        "description": "紧扣新托福改革考题，高保真还原北美大学地质、天文、生物、人类学学术讲座与学术讨论写作。",
        "difficulty": "高级 C1",
        "tags": ["托福核心", "TOEFL", "学术听力", "北美课堂"]
    }
    toefl_chapters = [
        {
            "title": "Lecture 1 · 地质学讲座：板块构造动力学与大陆漂移学说验证",
            "description": "探讨魏格纳大陆漂移假说、洋中脊海底扩张、古地磁反转与板块边界动力学。",
            "sentences": [
                {"en": "Alfred Wegener's revolutionary continental drift hypothesis was initially ridiculed because he could not identify the underlying geological driving mechanism.", "cn": "阿尔弗雷德·魏格纳当年提出的革命性“大陆漂移假说”起初遭到了地质学界无情的嘲讽讥笑，全因他当时全然无法令人信服地指明深埋在地心深处的驱动物理动力学机理。"},
                {"en": "The discovery of mid-ocean ridges revealed that seafloor spreading creates new oceanic basaltic crust along divergent plate boundaries continuously.", "cn": "洋中脊大裂谷的震撼科学发现向世人揭秘：在洋底离散板块边界深处，海底扩张运动正在源源不断地从地幔涌出喷发，凝固创造出崭新的大洋玄武岩洋壳！"},
                {"en": "Paleomagnetic stripes preserved symmetrically within the oceanic floor record episodic reversals of Earth's geomagnetic polarity throughout epochs.", "cn": "在大洋深处洋壳玄武岩内部对称排布、如斑马线般的古地磁异常条带，忠实且无可辩驳地定格记录下了漫长地质历史纪元中地球地磁极性周期性倒转的神奇轨迹。"},
                {"en": "Subduction zones occur where dense oceanic plates sink beneath buoyant continental plates, triggering violent volcanic eruptions and deep earthquakes.", "cn": "在冰冷致密的大洋板块俯冲跌落扎入轻质的大陆板块下方的“俯冲带”剧烈交界处，往往会不可遏制地引爆惊天地泣鬼神的大地震与毁灭性火山大喷发。"},
                {"en": "Mantle convection currents driven by radiogenic decay deep within the core act as the colossal heat engine powering tectonic plate migrations.", "cn": "深藏于地核深处、由放射性同位素天然衰变所释放的热能所驱动的宏伟地幔热对流循环，充当着统领推动整个人类脚下地壳岩石圈板块徐徐漫游漂移的超级地心热机！"},
                {"en": "Transform fault plate boundaries like California's San Andreas Fault exhibit horizontal shearing motions that generate devastating shallow-focus seismic shocks.", "cn": "诸如美国加州著名的圣安德烈斯断层等转换断层板块边界，呈现出凶险的水平剪切走滑错动，极易在毫无防备的地表浅层引爆灾难性的浅源破坏性大地震！"},
                {"en": "The Himalayan orogeny was forged when the Indian subcontinent slammed violently into the Eurasian tectonic landmass millions of years ago.", "cn": "巍峨壮观、耸入云霄的喜马拉雅造山带大奇迹，正是数千万年前印度次大陆板块以排山倒海之势凶悍猛烈撞击欧亚大陆板块所千锤百炼挤压锻造出的地质杰作！"},
                {"en": "Supercontinents like Pangaea assemble and disperse along cyclic rhythms spanning hundreds of millions of years known as the Wilson cycle.", "cn": "宛如盘古大陆（Pangaea）这般的超级古大陆，沿着每隔数亿年便周期性重演一次的汇聚拼合与分崩离析大节律运转，在地质学界被尊称为“威尔逊大旋回”。"},
                {"en": "Hydrothermal vents clustered along mid-ocean fissures sustain bizarre chemosynthetic ecosystems completely insulated from solar photosynthetic radiation.", "cn": "簇拥在漆黑冰冷洋底裂隙四周的深海热液黑烟囱群落，以令人惊叹的化能合成代谢奇迹，独自滋养孕育着一套完全超脱于太阳光合作用辐射之外的奇特生命绿洲！"},
                {"en": "Sedimentary rock strata layered across the Grand Canyon provide an open geological library documenting billions of years of marine regressions.", "cn": "层层叠叠沉积铺展在大峡谷千仞绝壁之上的沉积岩地层剖面，宛如一部由大自然亲手编撰的浩瀚地质编年史，无声倾诉着数十亿年间沧海桑田的海退与海进轮回。"},
                {"en": "Radioactive radiometric dating measuring uranium-lead decay ratios determines the absolute chronometric age of ancient metamorphic zircon crystals.", "cn": "利用铀-铅同位素衰变比例测定的放射性同位素绝对测年法，能够以令人惊叹的超高精度测定古老变质岩锆石晶体的绝对地质编年岁数。"},
                {"en": "Fold mountains formed by crustal compression demonstrate that seemingly rigid granite boulders behave like malleable dough over geological time.", "cn": "在漫长地质年代地壳剧烈挤压下所褶皱隆起的褶皱山脉生动证明：在以千万年计的时间尺度面前，看似坚不可摧的花岗岩巨石宛如任由揉捏的面团般柔软！"},
                {"en": "Hotspot volcanic chains such as the Hawaiian archipelago trace the slow movement of the Pacific plate drifting across stationary mantle plumes.", "cn": "夏威夷群岛如珍珠链般排列的热点火山链，忠实精确勾勒出了太平洋板块在深部相对静止的炽热地幔柱上方数千万年缓缓漂移而过的壮丽轨迹。"},
                {"en": "Tectonic uplift influences regional climate patterns by creating high-altitude rain shadow deserts across leeward continental plains.", "cn": "巍峨山脉的地质构造隆升，通过在背风面大陆腹地营造出广袤干旱的“雨影区荒漠”，从根本上深刻重塑了区域宏观气候生态格局。"},
                {"en": "Geology teaches us to inhabit deep time, revealing that the solid earth beneath our feet is a dynamic, ever-churning cosmic vessel.", "cn": "地球地质学赋予了我们洞悉“深邃地质时间”的宏大宇宙视角，向世人揭示：我们脚下看似坚如磐石的大地，实则是一艘在宇宙长夜中永不停歇翻滚演化的活力方舟！"}
            ]
        },
        {
            "title": "Lecture 2 · 天文学讲座：系外行星探测与恒星演化生命周期",
            "description": "探讨凌日法掩星测量、多普勒径向速度法、主序星赫罗图演化与超新星爆发。",
            "sentences": [
                {"en": "The transit photometry method detects distant extrasolar worlds by measuring the minuscule dip in a parent star's luminosity curve during planetary passage.", "cn": "凌日掩星光度测量前沿技术，通过以纳米级超高精度监测当系外行星横越母恒星圆面时所造成的极其微弱的恒星光度曲线下沉，从而精准揪出行星信号。"},
                {"en": "Doppler radial velocity spectroscopy identifies orbiting exoplanets by tracking the subtle gravitational wobble induced in the central star's spectrum.", "cn": "多普勒径向速度高分辨率光谱分析仪，通过敏锐捕捉系外行星在公转时给中心母恒星所施加的微小引力牵引摆动，在星光光谱红移蓝移中测算行星质量。"},
                {"en": "The habitable zone, colloquially dubbed the Goldilocks zone, defines the orbital orbital perimeter where liquid water can stably pool upon planetary surfaces.", "cn": "天文学界俗称的“宜居带”或“金发姑娘带”，精确划定了距离中心恒星不冷不热的黄金轨道安全半径——唯有在此处，宝贵的液态水方能在岩石地表长期稳定存在。"},
                {"en": "Hertzsprung-Russell diagrams categorize billions of stars by plotting their absolute stellar luminosity against surface temperature, revealing the main sequence.", "cn": "赫罗图（H-R Diagram）通过将浩瀚宇宙中亿万颗恒星的绝对光度同表面有效温度进行直角坐标投影，优雅勾勒揭示出了恒星生息繁衍的核心主序星演化轨迹。"},
                {"en": "Stellar nucleosynthesis within massive stars fuses hydrogen into helium and successively heavier elements until iron poisons the thermonuclear core fatally.", "cn": "超大质量恒星内部剧烈上演的恒星核聚变熔炉，将氢原子核一路聚变合成氦、碳、氧等更重元素，直至铁核在核心沉积、彻底宣判热核反应的死刑！"},
                {"en": "Core-collapse supernovas release unimaginably titanic shockwaves that synthesize trans-iron elements such as gold and uranium across the cosmos.", "cn": "当巨型大质量恒星核心在引力坍塌瞬间引爆超新星大爆发时，释放出足以照亮整个星系的骇人激波，在一瞬间为整个宇宙淬火合成了黄金、铀等超铁重元素！"},
                {"en": "White dwarfs are the ultra-dense carbon-oxygen corpses of sun-like stars sustained against crushing gravity exclusively by electron degeneracy pressure.", "cn": "白矮星乃是类太阳恒星在耗尽燃料后所遗留下的超致密碳氧残骸，在自身毁天灭地的引力狂轰滥炸下，全然仰仗量子力学中的“电子简并压力”苦苦支撑维系平衡。"},
                {"en": "Neutron stars possess magnetic fields billions of times stronger than Earth, emitting rapid beacons of radiation observed as celestial pulsars.", "cn": "中子星拥有比地球强悍数十亿倍的超强磁场，以每秒数百圈的惊天速度疯狂自转，向浩瀚苍茫深空喷射出如同宇宙灯塔般的脉冲辐射电磁束。"},
                {"en": "Gravitational lensing predicts that massive galaxy clusters bend the spacetime fabric, acting as colossal natural telescopes that magnify background light.", "cn": "爱因斯坦广义相对论预言的“引力透镜效应”指出：超级星系团的恐怖质量将扭曲周围的时空结构，化身为浩瀚宇宙中天然的放大望远镜！"},
                {"en": "Spectroscopic atmospheric analyses of transiting exoplanets seek chemical biosignatures such as simultaneous oxygen and methane in thermodynamic disequilibrium.", "cn": "对穿越母星光芒的系外行星大气层实施精细吸收光谱分析，旨在探寻氧气与甲烷在大气中同时共存的“热力学非平衡态”确凿生命化学指纹。"},
                {"en": "Black holes represent regions of spacetime where gravitational singularities are enclosed within an impenetrable boundary called the event horizon.", "cn": "黑洞代表着时空几何学上的终极极限奇点——其无与伦比的极端引力深渊被死死禁锢在一个连光速都插翅难逃的绝对单向视界（Event Horizon）深处。"},
                {"en": "Tidally locked exoplanets orbiting red dwarfs present perpetual daylight on one hemisphere while condemning the other to frozen eternal midnight.", "cn": "围绕红矮星近距离运行的被潮汐锁定系外行星，其正面永远承受着酷热的永昼炙烤，而背阴面则被永远打入冰封万里的永夜寒冬深渊。"},
                {"en": "The cosmic microwave background radiation provides an indelible snapshot of the infant universe as it cooled below decoupling temperatures.", "cn": "均匀弥漫在全天的宇宙微波背景辐射，为人类留下了宇宙在诞生后仅三十八万年时、当光子首次从等离子体浓汤中解耦自由飞驰时的珍贵婴儿快照！"},
                {"en": "Starlight arriving at our eyes today left ancient celestial furnaces millions of years ago, turning the night sky into a living time machine.", "cn": "今夜拂过我们眼眸的每一抹微弱星光，均是在数百万年前甚至数十亿年前从远古恒星核聚变熔炉中启程奔赴而来的，将夜空化身为一台穿梭时空的时光机。"},
                {"en": "We are not merely detached observers gazing at the stellar canopy; every atom in our bloodstream was forged within ancient supernovae.", "cn": "我们人类从来绝非仅仅只是伫立在荒原仰望璀璨星空的孤立过客；我们血脉深处的每一个铁原子与钙原子，皆是在亿万年前某颗超新星大爆发的烈火中被神圣锻造而出的！"}
            ]
        },
        {
            "title": "Lecture 3 · 人类学与考古学讲座：早期定居农业与新石器时代革命",
            "description": "探讨新石器时代农业驯化、定居聚落形成、社会阶层分化与陶器金属工具问世。",
            "sentences": [
                {"en": "The Neolithic revolution marked humanity's momentous transition from nomadic hunting and gathering toward sedentary agriculture and animal domestication.", "cn": "新石器时代大革命标志着人类历史上具有里程碑意义的惊天大跨越——从居无定所、茹毛饮血的游牧狩猎采集部落，决绝迈向定居农耕与家畜驯养文明！"},
                {"en": "Archaeologists excavating Fertile Crescent settlements identify charred einkorn wheat grains that reveal artificial selection for non-shattering rachis traits.", "cn": "考古学家在美索不达米亚“新月沃土”早期定居遗址灰烬层中发掘出的炭化单粒小麦麦粒，清晰揭示了早期先民对不易自然脱落落粒麦穗的人工选育驯化痕迹。"},
                {"en": "Sedentary village life catalyzed permanent architectural construction, specialized craft pottery production, and unprecedented storage granary infrastructures.", "cn": "长年定居的村落起居生活，催生了坚固永久性黏土石砌房屋建筑的拔地而起、专业化手工业陶器烧制的诞生，以及前所未有的公共粮食防潮谷仓窖藏设施。"},
                {"en": "Paleopathological examinations of skeletal remains demonstrate that early agrarian populations paradoxically suffered higher malnutrition rates than mobile foragers.", "cn": "古病理学家对早期农耕聚落人类骨骼化石的微观断层扫描惊人地证实：第一批告别游猎的早期定居农夫，其骨密度与贫血营养不良发病率竟反常地高于游猎祖先！"},
                {"en": "Surplus grain accumulation concentrated within elite temple precincts gradually stimulated the emergence of institutionalized socio-economic hierarchies.", "cn": "在原始先民神庙祭祀中心由国家政权统筹储备垄断的海量粮食剩余财富，潜移默化催生并激化了全社会森严体制化的阶级贫富分化与官僚统治特权。"},
                {"en": "Obsidian stone tool trade routes spanning hundreds of kilometers indicate sophisticated regional barter exchange networks across Anatolian peninsulas.", "cn": "横跨数千公里地理时空的黑曜石高纯石刃远途贸易扩散网络，强有力证明早在文明破晓初期，小亚细亚安纳托利亚半岛各部族间便已深耕着高度成熟的区域互市大网络。"},
                {"en": "Megalithic stone circles such as Göbekli Tepe were constructed by cooperative foraging bands long before the widespread adoption of sedentary farming.", "cn": "诸如土耳其哥贝克力石阵等令人叹为观止的巨石图腾神殿建筑奇迹，早在人类全面转向定居耕作之前数千年，便已由高度协同的大型游猎部落联军携手合力雕琢筑就！"},
                {"en": "Radiocarbon dating calibrated with tree-ring dendrochronology provides archaeological researchers with absolute chronological timelines across millennia.", "cn": "依托树木年轮气候学予以精确多重交叉校准的碳十四放射性衰变同位素绝对测年法，为全球考古科学家搭建起了纵贯数千载漫长光阴的铁证断代编年标尺。"},
                {"en": "Cereal monoculture diets lacking micronutrient variety precipitated epidemic dental caries and enamel hypoplasia among early farming children.", "cn": "早期农业单一高碳水谷物糊口食物结构的局限，导致微量营养元素严重匮乏，在农家孩童乳牙上留下了触目惊心的龋齿蛀牙与牙釉质发育不全病理性沟槽。"},
                {"en": "The domestication of bovine draft animals transformed agricultural tillage velocity while inadvertently exposing human communities to cross-species pathogens.", "cn": "对大型黄牛水牛作为重载耕畜的成功驯化，在极大跃升农田翻土犁地开荒效率的同时，也神不知鬼不觉将早期人类社群推向了致命人畜共患交叉感染病原体的虎口。"},
                {"en": "Monumental burial mounds containing prestige goods including jade carvings demonstrate the codification of inherited dynastic lineages.", "cn": "陪葬着大量罕见精美玉器、绿松石与青铜礼器的王族贵族豪华大墓土墩，无可辩驳地宣告了宗法血缘世袭宗族王权统治秩序在历史大舞台上的正式加冕确立。"},
                {"en": "Proto-cuneiform clay accounting tokens represented transactions involving sheep and barley, giving birth to written symbolic recording systems.", "cn": "在两河流域泥板上用来记录进出仓羊只只数与大麦蒲式耳数量的早期原始楔形文字泥制记账筹码，在算盘账本的世俗琐碎中孕育催生出了人类第一套书面文字符号体系！"},
                {"en": "Agrarian surplus permitted the sustenance of full-time metallurgists who melted copper and tin ores to forge superior bronze tools.", "cn": "充沛的粮食剩余财富储备，方才使得早期社会得以从容脱产供养一批全职潜心搞研发的高级冶炼铸造工匠，将孔雀石铜矿与锡矿熔铸为开创时代的锋利青铜利器！"},
                {"en": "Sedentism bound human destiny inextricably to the seasonal whims of soil and rain, inaugurating a high-stakes ecological gamble.", "cn": "人类毅然选择告别四海为家的浪迹天涯、决然选择在一隅方寸土地上落地生根，自此便将整个物种的生死存亡同土壤肥力与风调雨顺的苍天喜怒哀乐死死捆绑在一起！"},
                {"en": "To unearth the humble hearthstones of our ancient Neolithic ancestors is to witness the very cradle where our modern civilizational consciousness awoke.", "cn": "用毛刷与手铲在黄土瓦砾深处拂去尘埃、亲手发掘触摸那一方方属于远古新石器时代先民的质朴取暖灶坑遗迹，我们便是在亲眼屏息见证：我们现代人类文明的自觉火种究竟是在何等坚韧的泥泞摇篮中破晓破土而出的！"}
            ]
        },
        {
            "title": "Lecture 4 · 生态学与海洋生物学讲座：珊瑚共生机制与食物网稳态",
            "description": "探讨虫黄藻光合共生、珊瑚白化机理、顶级捕食者下行效应与海洋微塑料毒性。",
            "sentences": [
                {"en": "Coral reefs thrive in nutrient-poor tropical waters through an exquisite obligate symbiosis between calcifying polyps and photosynthetic zooxanthellae.", "cn": "五彩斑斓的珊瑚礁群落之所以能在营养极度匮乏贫瘠的热带海水中蓬勃繁茂，全凭珊瑚钙化水螅体微观虫体同共生其体内的光合作用单细胞虫黄藻之间那份性命相托的绝对互利共生！"},
                {"en": "Zooxanthellae nestled within coral tissues furnish up to ninety percent of the host's energy budget through carbon-fixing photosynthetic outputs.", "cn": "寄宿在透明珊瑚外胚层软组织深处的显微虫黄藻，通过日夜不停高效的光合固碳作用，足足为珊瑚宿主全身日常代谢提供了高达百分之九十以上的救命能量供给！"},
                {"en": "Elevated sea surface temperatures induce thermal cellular stress, causing stressed polyps to expel their vital pigmented algae in bleaching events.", "cn": "持续反常飙升的近海表层海水海水异常高温，会瞬间引爆珊瑚细胞层面的剧烈热氧化应激反应，逼迫受惊的水螅体绝望将体内五彩斑斓的虫黄藻无情驱逐，酿成大面积珊瑚白化悲剧！"},
                {"en": "A bleached coral is not dead immediately, but starves slowly unless anomalous water temperatures subside to permit algal recolonization.", "cn": "遭遇白化洗劫的白垩色珊瑚骨架并未在瞬间当场暴毙气绝，而是在饥寒交迫中陷入绝望的慢性饿死边缘，唯有当极端高温洋流及时退去，残存藻类方有一线生机重返家园！"},
                {"en": "Top-down trophic cascades demonstrate that apex marine predators such as tiger sharks regulate mid-tier grazing fish populations to preserve seaweed equilibrium.", "cn": "自上而下贯穿海洋食物链顶端的“下行营养级级联效应”无可辩驳地证明：诸如虎鲨等大洋顶层掠食猛兽的存在，能够强力抑制中层植食性鱼类的泛滥，从而护航大型海藻床的生态平衡。"},
                {"en": "Ocean acidification resulting from runaway anthropogenic carbon absorption depresses carbonate ion saturation levels, dissolving juvenile coral skeletons.", "cn": "因人类过量温室气体排放所诱发的全球大洋海水酸度持续走高，正在急剧拉低海水中碳酸根离子的过饱和浓度临界线，直接让娇嫩幼年珊瑚虫的碳酸钙骨骼遭受如同浓酸般的无情溶蚀！"},
                {"en": "Parrotfish play an indispensable herbivorous maintenance role by scraping away macroalgal turfs that would smother fragile nascent coral larvae.", "cn": "大洋中长着坚硬喙齿的鹦嘴鱼等关键植食性鱼类，扮演着大洋清道夫的崇高保洁职责——通过日夜不停啃噬刮除那些极易将脆弱初生珊瑚幼虫死死窒息憋死的过度疯长大型海藻！"},
                {"en": "Microplastic particles suspended throughout the water column are ingested by filter-feeding bivalves, transferring toxic chemical additives up marine food webs.", "cn": "悬浮弥散在从海面到海底各水层的致密微塑料微粒，极易被双壳贝类滤食性生物误食入腹，并顺藤摸瓜将剧毒工业化学添加剂沿着海洋食物链逐级放大富集。"},
                {"en": "Mangrove marine nurseries hugging muddy coastlines buffer coral reefs from toxic terrestrial agricultural silt runoffs while sheltering juvenile fish.", "cn": "紧紧依偎环抱在沿海泥滩红树林海岸带生态湿地，不仅能如超级过滤网一般拦截阻断陆地农药化肥泥沙毒素直冲入海，更为大洋中成千上万种经济鱼虾幼苗构筑了最温馨的避风港幼儿园。"},
                {"en": "Artificial reef engineering utilizing specialized electro-mineral accretion currents accelerates calcium carbonate deposition rates along damaged shorelines.", "cn": "采用前沿“矿物电沉积生态修复技术”的人工珊瑚礁工程，通过向水下金属架构通入安全微弱直流电，能够以数倍的速度催化碳酸钙晶体在受损海岸线上快速沉积结晶！"},
                {"en": "Bioluminescent signaling mechanisms deployed across deep bathypelagic trenches facilitate mate location and predator evasion within eternal abyssal darkness.", "cn": "深潜在大洋数千米终年不见天日的深渊海沟深处的奇异深海发光生物，巧妙利用生物荧光脉冲信号作为其在永恒长夜中求偶幽会与迷惑捕食者的绝妙通信兵器！"},
                {"en": "Bioaccumulation of heavy metals within apex pelagic predators such as bluefin tuna renders frequent consumption hazardous to human cognitive wellness.", "cn": "汞、镉等剧毒重金属离子在大洋顶级游弋掠食者蓝鳍金枪鱼脂肪肌肉深处的恶性生物富集放大效应，使得人类频繁大量大快朵颐食用这些名贵鱼生，极易给人类大脑中枢神经系统带来不可逆的损伤隐患！"},
                {"en": "Marine protected area networks enforcing total no-take fishing zones demonstrate dramatic biomass recovery spillover effects into neighboring coastal fisheries.", "cn": "高标准划定设立且铁腕禁捕的“全封闭海洋生态特区保护区核心网络”，在短短数年内便能呈现出令人叹为观止的鱼类生物量爆发式反弹，其外溢效应有力反哺滋润了周边渔民的钱袋子！"},
                {"en": "The ocean is the planetary thermal flywheel and lungs of the biosphere; to collapse its biological vitality is to suffocate life on Earth.", "cn": "浩瀚的大海从来都是整个地球生物圈最硬核的恒温飞轮与源源不断吐故纳新的生命呼吸之肺；任由海洋生物多样性在我们手中轰然坍塌崩解，无异于在全人类自身的脖颈上套上窒息绞索！"},
                {"en": "Reverence for marine ecosystems requires viewing the open sea not as an infinite trash abyss, but as the sacred cradle of terrestrial life.", "cn": "对浩瀚海洋生态心存由衷敬畏，迫切要求我们全人类决然摒弃将公海当成可以肆意倾倒工业核废料与塑料垃圾的无底垃圾桶的野蛮作派，重新以庄严跪拜之姿，致敬这片哺育了陆地一切生灵的神圣生命摇篮！"}
            ]
        },
        {
            "title": "Lecture 5 · 艺术史讲座：印象派光影革命与户外写生画法突破",
            "description": "探讨莫奈睡莲日出、工业革命管状颜料问世、视网膜色彩混合与光学写生突破。",
            "sentences": [
                {"en": "The Impressionist artistic vanguard of the late nineteenth century broke decisively from the rigid, theatrical dogmas enforced by the Parisian Salon.", "cn": "十九世纪末横空出世的印象派先锋艺术家群星，以石破天惊的大无畏反叛勇气，决绝彻底砸碎了由法国巴黎官方国家沙龙所死死把持的刻板、做作、戏剧化古典教条枷锁！"},
                {"en": "The revolutionary invention of portable metal paint tubes liberated painters from indoor ateliers, enabling them to capture evanescent outdoor lighting en plein air.", "cn": "便携式金属管状油画颜料的划时代工业发明问世，奇迹般将画家们从暗无天日的室内画室阁楼中彻底解放赎身出来，赋能大师们得以走出户外、在瞬息万变的大自然原野清风中捕捉户外写生（En plein air）的吉光片羽！"},
                {"en": "Claude Monet's iconic 'Impression, Sunrise' provoked condescending critical mockery from orthodox connoisseurs, who dismissed it as a slapdash preliminary sketch.", "cn": "克劳德·莫奈名垂青史的开山大作《日出·印象》，在当年首次公开展出时曾招致正统学院派评论家刻薄恶毒的冷嘲热讽，被轻蔑斥责为一幅连未完成半成品都算不上的粗制滥造涂鸦草稿！"},
                {"en": "Impressionist masterworks deliberately abandoned smooth academic varnish finishes in favor of broken, visible brushstrokes that pulse with vibrant optical energy.", "cn": "印象派旷世杰作刻意决绝抛弃了古典学院派那种把画布磨得光滑如镜、毫无瑕疵的虚伪罩染上光打磨恶习，转而以大刀阔斧、清晰可见的跳跃短促断裂笔触，让每一寸颜料在画布上如火如荼跳动着纯粹的光学颤音！"},
                {"en": "Optical color mixing occurs when unblended complementary brushstrokes placed side by side fuse within the spectator's retina rather than on the artist's palette.", "cn": "所谓的“视网膜光学混色”高维物理视觉魔法，特指画家故意不在调色板上把颜料机械搅和稀烂，而是将两抹未经调和的互补色笔触并列点戳在画布之上，任由其在观众的视网膜成像神经深处自发激荡交融出令人眩目的灿烂光晕！"},
                {"en": "Edgar Degas captured the fleeting physical strain and backstage awkwardness of Parisian ballet dancers with candid, asymmetric photographic cropping angles.", "cn": "埃德加·德加凭借其近乎冷峻的洞察力，以抓拍式非对称摄影透视构图角度，近乎残忍而又深情地精准捕捉定格下了巴黎芭蕾舞女演员在后台更衣休整时那一幕幕肌肉拉伤与疲惫酸痛的真实瞬间。"},
                {"en": "The proliferation of nineteenth-century Japanese woodblock ukiyo-e prints profoundly influenced Impressionist masters through bold outlines and flattened spatial perspectives.", "cn": "在大洋彼岸欧陆掀起狂潮的日本传统浮世绘木刻版画艺术的漂洋过海，凭借其大开大合的犀利轮廓勾线与大胆扁平化的无透视二度空间留白构图，深深震撼并启发了印象派大师们的艺术重塑！"},
                {"en": "Monet painted repeated architectural studies of Rouen Cathedral across divergent seasons, documenting the metamorphic velocity of solar illumination upon Gothic limestone.", "cn": "克劳德·莫奈在不同季节的拂晓、正午与黄昏，不知疲倦地反复对着鲁昂大教堂正立面狂热挥毫作画数十幅，以惊人的执着严谨记录下了太阳光晕照射在哥特式石灰岩浮雕细节上所引发的如梦似幻的光影蜕变奇观！"},
                {"en": "Industrial steam locomotives, smoky train stations, and bustling iron bridges became celebrated motifs that reflected the rapid pulse of modern urban existence.", "cn": "呼啸吞吐着滚滚浓烟的高速蒸汽机车火车头、车水马龙的火车站玻璃穹顶以及工业感十足的铆钉钢铁大桥，华丽转身变为了印象派画家笔下热烈歌颂现代都市狂飙脉搏的最璀璨主角！"},
                {"en": "Impressionism did not seek to replicate photographic reality mechanically, but to translate the subjective, ephemeral psychological sensation of perceptual experience onto canvas.", "cn": "印象派艺术所终生孜孜以求的崇高境界，从来绝非是对客观现实物理世界的机械照相式僵死拓印；而在于以天才的画笔，将人类主观心智在猝然邂逅大千光影那一刹那所体悟到的稍纵即逝的心理顿悟与视觉震撼，淋漓尽致化为画布上的永恒！"},
                {"en": "Pointillism championed by Georges Seurat systematized Impressionist intuition into rigorous scientific grids governed by optical color division theories.", "cn": "由乔治·修拉所开创的“点彩派（Pointillism）”，以大科学家的严谨执着，将印象派凭借直觉捕捉光影的感性笔触，全面升华重塑为了严格由近代光学分色理论所统御的精密色点像素矩阵！"},
                {"en": "Berthe Morisot defied Victorian social constraints, capturing intimate domestic motherhood vignettes with brushwork celebrated for its lyrical spontaneity and tenderness.", "cn": "身为女性先驱的贝尔特·莫里索以卓越才华冲破男权维多利亚时代的世俗偏见桎梏，以诗意灵动、笔走龙蛇般的洒脱笔触，将家庭内部温馨深沉的母爱亲情瞬间升华为传世不朽的美学华章！"},
                {"en": "The advent of Daguerreotype photography forced progressive painters to abandon mere illustrative imitation, liberating fine art to explore non-representational expression.", "cn": "达盖尔银版照相术的横空出世，以无情铁锤逼迫敏锐的先锋画家们彻底放弃了对客观物体浮光掠影的肖像摹写，从而前所未有地逼迫纯艺术走向探索非具象、纯粹表现形式的广阔星空！"},
                {"en": "Impressionist palettes purged dark bitumen shadows completely, proving that shadows in nature are luminous symphonies vibrating with reflected violet and blue.", "cn": "印象派调色板决绝彻底清除了传统古典画法中那种用沥青深黑来涂抹阴影的陈腐恶习，以无可辩驳的写生事实向世人证明：大自然之中的一切阴影，从来都是泛着紫罗兰与孔雀蓝反光的璀璨光之交响！"},
                {"en": "To look through Impressionist eyes is to rediscover that the world is not carved from dead stone, but is reborn anew with every falling ray of golden light.", "cn": "借由印象派大师们的清澈眼眸重新审视大千世界，我们方能如梦初醒般重获新生——这个世界从来绝非是由冰冷僵死的顽石所雕凿封冻，而是在拂晓洒向人间的每一缕灿烂金黄晨曦之中，都在生生不息地盛大重获新生！"}
            ]
        },
        {
            "title": "Lecture 6 · 微观经济学讲座：机会成本、负外部性与公地悲剧治理",
            "description": "探讨显性与隐性机会成本、庇古税应对排污负外部性、科斯定理与共有资源产权界定。",
            "sentences": [
                {"en": "Opportunity cost represents the fundamental economic reality that choosing one course of action permanently forfeits the net benefits of the next best alternative.", "cn": "“机会成本（Opportunity Cost）”这一微观经济学最核心的基石概念无情揭示出：当你斩钉截铁选择投身于某一特定行动路线时，你便不可逆地在事实上彻底放弃了次优替代方案原本能够恩赐于你的全部潜在净收益！"},
                {"en": "Negative externalities occur when the manufacturing operations of a commercial entity impose uncompensated environmental or public health damages upon innocent third parties.", "cn": "所谓的“负外部性（Negative Externalities）”，特指某些商业企业在工厂封闭围墙内部紧锣密鼓开展生产获利经营活动时，却极度自私地将未予补偿的恶劣生态排污与公共卫生致病代价，硬生生粗暴转嫁倾倒给无辜的社会公众第三者！"},
                {"en": "Arthur Pigou advocated corrective excise levies, termed Pigouvian taxes, designed to align private marginal corporate expenditures with full social costs.", "cn": "福利经济学宗师阿瑟·庇古力主推行刚性的精准矫正型专项消费税收政策——即名垂青史的“庇古税”机制，旨在通过国家税收杠杆，强有力逼迫排污企业将其原本转嫁的外部社会总成本，如数重新计入自身企业内部真实的边际私人物料成本账本！"},
                {"en": "The tragedy of the commons unfolds inexorably when individual self-interested economic actors overexploit finite, rivalrous open-access resources to collective ruin.", "cn": "著名的“公地悲剧（Tragedy of the Commons）”铁律残酷描绘了一幕惨剧：当每一个自诩精明的自私理性经济主体，均在毫无门槛约束的共有公共资源池中各怀鬼胎疯狂争相过度开采索取时，最终换来的必将是全员玉石俱焚的集体大毁灭！"},
                {"en": "The Coase Theorem posits that if property rights are unambiguous and transaction frictions are negligible, private bargaining achieves Pareto-optimal resource allocation.", "cn": "诺贝尔经济学奖得主罗纳德·科斯那篇振聋发聩的“科斯定理”大胆论证指出：只要法庭与制度层面的产权权属界定清晰绝对毫无歧义、且民事协商的交易摩擦履约成本微乎其微，民间当事人双方仅凭自由契约博弈谈判，便能奇迹般自发实现帕累托最优的完美资源配置！"},
                {"en": "Non-excludable and non-rivalrous public goods, exemplified by national defense and lighthouses, suffer chronic market under-provision without state fiscal subsidies.", "cn": "具有鲜明“非排他性”与“非竞用性”特征的纯公共物品——诸如固若金汤的国防钢铁长城与耸立在汹涌礁石暗礁之上的航海灯塔，若缺乏国家主权财政的强力兜底全额注资采购，在纯自由商业市场逻辑下注定必将沦为无人问津的严重供给荒漠！"},
                {"en": "Price elasticity of demand measures the sensitivity with which consumer purchasing volumes fluctuate in mathematical response to shifting unit retail prices.", "cn": "微观经济学中的“需求价格弹性”核心量化指标，严密丈量计算着广大消费者终端购买消费量在面对零售单价上下浮动跳跃时，在数学模型层面所呈现出的敏感跳跃反应幅度。"},
                {"en": "Monopolistic deadweight loss reflects lost societal economic surplus that evaporates into thin air when price-making cartels throttle competitive output volumes.", "cn": "垄断组织所制造的恶性“无谓损失（Deadweight Loss）”，生动量化了一副触目惊心的经济图景：当手握定价生杀大权的商业垄断卡特尔为了牟取暴利而故意人为卡死限产供给时，大批原本属于全社会的巨大总体经济福祉甘霖，硬生生在资本垄断绞杀下化为了虚无蒸发！"},
                {"en": "Asymmetric information scenarios where sellers possess superior product diagnostic insights over naive buyers precipitate catastrophic adverse selection spirals in used-car lots.", "cn": "在二手车交易市场与金融信贷市场中广泛存在的“信息不对称”陷阱——即卖家对产品瑕疵与底层坏账风险心知肚明、而买家却一头雾水两眼一抹黑的格局，往往会在极短时间内恶性引爆劣币驱逐良币的“逆向选择大雪崩”！"},
                {"en": "Moral hazard arises when insured policyholders engage in reckless risk-taking behaviors because the downside financial repercussions are transferred elsewhere.", "cn": "保险学与金融学中令人头皮发麻的“道德风险”毒瘤，生动刻画了一种人性阴暗心理：当一个人或一家大金融机构自恃名下早已购置了全额商业兜底保险或认定国家政府绝不敢坐视其倒闭时，其极易在暗中肆无忌惮从事高杠杆疯狂豪赌，因为一切暴雷炸裂的恶果早已被金蝉脱壳转嫁给他人接盘！"},
                {"en": "Tradable emissions allowance permit programs construct artificial market caps, transforming ecological pollution reduction into a monetizable corporate asset.", "cn": "机制设计精妙的“可交易排污权配额制度”，巧妙以法治力量在宏观层面筑起环境容量刚性总量天花板，在微观层面破天荒将企业主动研发低碳脱碳减排的实际成效，华丽转身为了可在交易所挂牌交易、坐享真金白银变现溢价的黄金资产！"},
                {"en": "Sunk costs—monetary expenditures already incurred that are fundamentally irreversible—should rationally exert zero mathematical influence upon forward-looking strategic decisions.", "cn": "微观经济学理性决策铁律三令五申警告：所谓“沉没成本（Sunk Costs）”——即那些已经在过去历史中真金白银砸入、且在物理和法理上彻底无可挽回的既往开销，在面向未来的任何前瞻性战略抉择权衡中，理应被彻底赋予绝对为零的数学权重，切莫让覆水难收的死成本绑架未来的活资本！"},
                {"en": "Consumer surplus quantifies the psychological bargain utility enjoyed when consumers purchase prized goods below their subjective maximum willingness to pay.", "cn": "“消费者剩余（Consumer Surplus）”概念以令人拍案叫绝的经济学语言，精准量化了当一个普通顾客在货架前以远低于自己内心深处心甘情愿咬牙支付的最高心理预算底线掏钱买到心头好时，在心房深处所悄然荡漾起的那份如同白捡了大便宜般的超额幸福效用！"},
                {"en": "Market efficiency alone does not ensure distributional equity; an economy can achieve textbook Pareto efficiency while millions starve in poverty.", "cn": "单纯冷冰冰的“市场配置效率”，从来绝不能天然等同于全社会的崇高公平与正义——一个经济体完全有可能在冰冷的教科书数学微积分推演上达到了尽善尽美的帕累托最优均衡，但在其繁华市井阴暗角落深处，却依然有数以百万计的赤贫劳工在饥寒交迫中垂死挣扎！"},
                {"en": "Economics achieves its noble calling only when its analytical scalpels are wielded to dismantle monopolies, lift the downtrodden, and nurture shared abundance.", "cn": "人类经济学这门伟大学科，唯有在这样一种崇高历史境界下方能真正加冕其不死的神圣荣光：那就是将自身锋利如手术刀般的缜密理性数理分析利刃，义无反顾地握在手中去挥刀斩断寡头垄断的吸血触角、倾尽全力托举庇护被命运碾压的寒门弱小，并在大地之上携手浇灌出一片美美与共、共同富裕的繁花胜境！"}
            ]
        },
        {
            "title": "Lecture 7 · 心理学讲座：条件反射、工作记忆容量与感知觉错觉",
            "description": "探讨巴甫洛夫经典条件反射、斯金纳操作强化、米勒神奇数字7±2与视错觉机制。",
            "sentences": [
                {"en": "Ivan Pavlov's classical conditioning paradigm established that pairing a neutral conditioned stimulus with an unconditioned food stimulus evokes involuntary salivary responses.", "cn": "伊万·巴甫洛夫名垂青史的经典条件反射实验范式向世人科学证明：通过将平平无奇的摇铃中性条件刺激同能够引起生理本能反应的无条件肉粉刺激进行成百上千次的精巧反复配对，最终单凭清脆铃声便能自发诱导出犬类非条件唾液分泌的生理奇迹！"},
                {"en": "B.F. Skinner's operant conditioning frameworks demonstrated that voluntary behaviors are systematically molded through schedules of positive reinforcement and punitive feedback.", "cn": "行为主义心理学泰斗斯金纳在其著名的“斯金纳箱”操作性条件反射实验体系中无可辩驳地揭示出：生命机体的一切自主自发行为反应模式，无不是在后天充满功利诱惑的“正向强化奖赏”与严苛威慑的“负向惩戒规训”的双重精心塑造下千锤百炼铸就的！"},
                {"en": "George Miller's landmark cognitive research identified the capacity limit of human short-term working memory as the magical number seven plus or minus two chunks.", "cn": "现代认知心理学奠基宗师乔治·米勒以里程碑式的实证心理学大作向全球学术界宣布：人类大脑短期工作记忆（Working Memory）的瞬时信息吞吐加工容量极限，被大自然极其精密地死死锚定在不可逾越的神奇数字——“7±2个信息组块（Chunks）”！"},
                {"en": "Sensory adaptation occurs when sensory receptors diminish their neural firing frequency following prolonged, unchanging exposure to constant environmental stimuli.", "cn": "生理心理学中的“感觉适应（Sensory Adaptation）”微观机理特指：当外周感觉感受器神经元长期持续暴露浸润在单一恒定、毫无变化的同质外界物理刺激环境中时，其神经元放电动作电位的振荡频率便会自发呈现出断崖式的主动衰减与麻木脱敏。"},
                {"en": "The Gestalt psychological school championed the foundational epistemological principle that perceptual wholes possess emergent properties irreducible to their elemental sensory parts.", "cn": "在世界心理学殿堂巍然耸立的“格式塔心理学派（Gestalt）”，以大智慧大声疾呼并确立了一条至高无上的认识论认知铁律：人类心智所感知统摄到的一切整体意象，自始至终拥有着由各个微观零散感官零件机械拼接所无论如何也绝对无法拼凑还原出的神圣“涌现特质（The whole is greater than the sum of its parts）”！"},
                {"en": "Top-down perceptual processing recruits past contextual expectations and cultural schemata to interpret ambiguous sensory inputs arriving from peripheral organs.", "cn": "人类心智独步天下的大脑“自上而下认知加工机制”，能够瞬间闪电调取个体过往丰富的人生阅历记忆、语境预期以及深层文化图式储备，以此雷霆万钧地对来自视网膜等外周感受器传来的那些充满模糊歧义的零碎外界微弱信号展开高超的语义重构解读！"},
                {"en": "Cognitive reappraisal techniques allow stressed individuals to consciously reframe emotional triggers, mitigating amygdala hyperactivity through prefrontal cortex inhibition.", "cn": "现代前沿认知行为心理学大力推崇的“认知重评调节技术”，能够赋能身陷惊涛骇浪心理重压之下的求助者，凭借自身自由意志的主观能动性重新审视并赋权生活困局，依托前额叶皮层的高阶理性自律神经连接，强效抑制扑灭杏仁核的过度惊恐爆发！"},
                {"en": "Optical illusions such as the Müller-Lyer illusion trick the human visual cortex into misjudging line segments due to perspective angle misinterpretations.", "cn": "诸如举世闻名的“缪勒-莱耶箭头视错觉”，通过在两根完全等长平行线段两端别有用心加上向内聚拢或向外张开的箭头尾翼，便能轻而易举将人类大脑视觉皮层玩弄于股掌之间，诱导其产生严重的长短判断错觉偏差！"},
                {"en": "Subconscious semantic priming demonstrates that brief subliminal exposure to conceptual words measurably accelerates subsequent lexical recognition reaction times.", "cn": "潜意识语义启动效应实验无可辩驳地揭秘：在毫秒级微观尺度下向受试者眼前一闪而过投射某个抽象概念词汇（哪怕肉眼甚至完全来不及有意识看清），便能在人类神经大脑突触网络中如多米诺骨牌般闪电激活相关联语义丛林，大幅缩短后续认知识别反应时！"},
                {"en": "Executive function encompasses cognitive inhibition, cognitive cognitive flexibility, and working memory manipulation, orchestrating goal-directed purposive human agency.", "cn": "坐镇于人类大脑神殿至高王座之上的“前额叶执行功能网络（Executive Function）”，完美统摄着认知冲动自律抑制、跨任务心智柔性灵活切换以及短期记忆信息的高阶动态重组微操，如同三军总司令一般精密指挥协调着人类一切具有崇高明确战略目标导向的自觉创造活动！"},
                {"en": "Proactive interference occurs when entrenched past memories disrupt the smooth consolidation and retrieval of freshly acquired factual information.", "cn": "认知心理学中经典的“前摄抑制（Proactive Interference）”心理遗忘机制，生动描述了那些在过去漫长岁月里早已在脑海中根深蒂固、先入为主的旧知识经验记忆，往往会如同顽固的霸王地头蛇一般，粗暴横插一杠、严重阻碍干扰新知识在神经突触中的平稳巩固与顺畅提取。"},
                {"en": "Visual agnosia patients can trace the physical contours of everyday objects with drawing pencils while remaining entirely unable to recognize their utility.", "cn": "在神经心理学临床上令人心碎的“视觉失认症”脑损伤罕见病患，尽管能够凭借残存的机械视觉在素描纸上一笔一画精确描摹勾勒出桌上钥匙或茶杯的完整物理轮廓外观，然而其受损的大脑皮层联络区却再也全然无法将该图像同其真实名称用途进行任何语义识别相认！"},
                {"en": "The flow state represents a psychological nirvana where total absorption within demanding challenges dissolves mundane self-consciousness and time perception.", "cn": "积极心理学泰斗米哈里·契克森米哈赖极力推崇的“心流（Flow）”神圣心理境界，生动描绘了一种当一个人的全部生命专注力被一项极具硬核挑战性同时又与其登峰造极专业功底完美匹配的高难度创造活动彻底深度吞噬淹没时的超凡脱俗极乐状态——在那个顿悟时刻，世俗一切自私虚荣的自我杂念与物理时间流逝感瞬间荡然无存！"},
                {"en": "Memory is not a museum vault of static historical relics, but an active, creative tapestry woven freshly with every recollected heartbeat.", "cn": "人类深邃的记忆殿堂从来绝非是一座冷冰冰、堆放着早已盖棺定论的死沉沉历史化石文物的陈旧地下防空洞；而在每一次夜深人静、神思飞扬的深情回溯与抚摸之中，它皆是一幅在我们每一记滚烫心跳的律动下重新被赋予鲜活温度、被我们富有创造性的大脑重新编织着的神圣生命华彩锦缎！"},
                {"en": "To master the labyrinth of our own psyche is the supreme enlightenment, liberating humanity from the invisible chains of unexamined impulses.", "cn": "勇敢推开自身颅骨深处那座幽深曲折、深不可测的潜意识精神大迷宫大门并以理性的火炬彻底将其照亮降伏，是人类个体在天地间所能斩获的至高觉醒启蒙——正是在这束理性自省光芒的照耀下，我们方能彻底砸碎千百年来由未经审视的原始盲动兽性本能所强加于我们灵魂之上的无形无影精神重枷！"}
            ]
        },
        {
            "title": "Lecture 8 · 气象学与大气物理讲座：厄尔尼诺现象与全球季风环流",
            "description": "探讨ENSO南方涛动、沃克环流异常、信风逆转与全球极端气象联动机制。",
            "sentences": [
                {"en": "The El Niño-Southern Oscillation represents a colossal coupled ocean-atmosphere meteorological phenomenon centered along the equatorial Pacific basin.", "cn": "名震全球气象学界的“厄尔尼诺-南方涛动（ENSO）”大循环系统，代表着一个横贯赤道整个广袤太平洋盆地腹地、兼具惊天动地宏伟尺度的巨型海气高度耦合相互作用的顶级气象引擎枢纽！"},
                {"en": "Under normal non-El Niño conditions, robust easterly trade winds relentlessly push warm equatorial surface water westward toward maritime Asian archipelagos.", "cn": "在平静正常的非厄尔尼诺寻常气象年景周期中，地球信风带上强劲而执着的偏东信风，终年如巨型扫帚一般无休无止将赤道海表温暖的巨量海水向西横推堆积至亚洲东部与大洋洲海域群岛！"},
                {"en": "The persistent westward accumulation of warm tropical ocean water creates a towering sea surface elevation disparity across the equatorial Pacific basin.", "cn": "在强劲信风千百日夜不停歇的向西疯狂驱赶堆积之下，在赤道西太平洋海面硬生生被堆垒出了一个比东太平洋海平面足足高出数十厘米之巨的庞大高位“温暖暖池（Warm Pool）”！"},
                {"en": "Off the coast of South America, vigorous wind-driven Ekman coastal upwelling pumps nutrient-rich polar abyssal water upward to fuel colossal fisheries.", "cn": "在浩瀚南美洲秘鲁沿海远海海域，强劲离岸离岸风所主导的“埃克曼风生沿岸上升流”，如超级深井抽水泵一般日夜不停将深海极度冰冷、富含磷酸盐与硝酸盐营养盐的极地深层海水狂暴泵涌上海表，催生滋养出了举世无双的秘鲁超级渔场！"},
                {"en": "During an El Niño event, easterly trade winds slacken dramatically or reverse completely, allowing the warm western Pacific pool to surge eastward.", "cn": "然而一旦凶猛的厄尔尼诺灾难周期被猛然引爆，原本强劲的赤道偏东信风便会如中风般急剧瘫痪衰竭乃至全线彻底逆转掉头，致使原本被锁死在西太平洋的滔天巨量炽热暖池海水如决堤洪兽般疯狂掉头向东大倒灌奔涌！"},
                {"en": "The atmospheric Walker circulation cells collapse and shift eastward, precipitating catastrophic torrents across arid coastal Peru while parching Australian rainforests.", "cn": "横亘在赤道太平洋上空的“沃克大气环流圈”在瞬间遭受重创坍塌并大幅向东整体漂移撕裂，直接在原本终年滴水不下的南美秘鲁干旱荒漠沿海引爆倾盆暴雨与滔天山洪泥石流，却以残酷大旱将千里之外的大洋洲热带雨林无情推向漫天野火的干渴炼狱！"},
                {"en": "Atmospheric teleconnections propagate meteorological anomalies downstream, perturbing jet stream trajectories and destabilizing winter storms across North America.", "cn": "大自然令人叹为观止的“大气遥相关（Teleconnections）”万里神经传导机制，能够将热带赤道海洋的一声咳嗽，以光速般顺着西风带高空急流的大尺度波动疯狂向下游全线大范围扩散放大，彻底打乱颠覆数万里之外北美洲与欧亚大陆寒冬暴风雪的常规运行轨迹！"},
                {"en": "Thermocline flattening across the eastern Pacific depresses cold water upwelling, suffocating phytoplankton productivity and causing catastrophic seabird die-offs.", "cn": "在东太平洋海域随着暖水大举东侵所引发的海洋深层“温跃层”断崖式平缓下沉下压，彻底切断瘫痪了原本冰冷上升流的生命补给大动脉，致使微观浮游植物断崖式灭绝枯竭，瞬间引发全流域数以百万计的海鸟与海狮海豹因断粮而曝尸荒滩的大灭顶浩劫！"},
                {"en": "La Niña represents the diametrically opposite phase of the oscillation, characterized by anomalously frigid sea surface temperatures across central equatorial waters.", "cn": "与桀骜不驯的厄尔尼诺宛如一对性情截然相反的孪生兄妹的“拉尼娜（La Niña）”现象，则代表着该气象钟摆周期走向另一个极端的冰冷宿命——赤道中东太平洋表层海温呈现出触目惊心、大范围反常偏冷的极寒深渊形态！"},
                {"en": "Climate scientists deploy high-resolution coupled ocean-atmosphere computer supercluster simulations to forecast ENSO transitions several seasons in advance.", "cn": "全球顶尖气象学家与海洋学家依托每秒千万亿次浮点运算的国家级前沿超级计算机集群，通过精密运转复杂的非线性海气双向全耦合动力学数理大模型，终于实现了提前数个季度对全球ENSO相变大拐点展开极其精准的前瞻性战略预警！"},
                {"en": "Monsoon circulation systems driven by unequal differential heating between sprawling continental landmasses and adjacent oceans reverse wind vectors seasonally.", "cn": "由辽阔浩瀚的欧亚非大陆腹地同身旁深邃大洋之间因巨大比热容差异所诱发的显著“海陆热力性质差异”，构成了统御全球庞大季风环流系统随春夏秋冬四季更替、在大陆与海洋之间大范围发生一百八十度大逆转交替吹拂的终极物理大推手！"},
                {"en": "Global atmospheric circulation relies on three meridional cells—the Hadley, Ferrel, and Polar cells—to transport excess tropical thermal energy toward the frigid poles.", "cn": "全人类头顶苍穹深处精密咬合的大气三圈环流宏伟巨型机器——即大名鼎鼎的低纬哈德莱环流圈、中纬费雷尔环流圈与高纬极地环流圈，日夜不停、不知疲倦地充当着大自然的全球大中央空调热泵，将赤道低纬度过剩积聚的滚烫暴烈热能，源源不断高空转运输送至冰封万里的极地两极寒区！"},
                {"en": "Coriolis force deflections resulting from planetary rotation alter trajectory vectors of air parcels, bending winds to the right in the Northern Hemisphere.", "cn": "因我们脚下整个地球自西向东高速自转所天然伴生而出的“地转偏向力（科里奥利力）”，如同一只无形的上帝造化之手，霸道统御着苍穹之上每一团流浪奔腾的空气气团的运动轨迹，在北半球铁律般将呼啸的风向生生向右发生肉眼可见的大角度扭转向右偏转！"},
                {"en": "Anthropogenic global planetary warming appears to intensify the amplitude and frequency of extreme El Niño super-events across the coming decades.", "cn": "当代人类工业文明无节制疯狂排放温室气体所导致的全球地表与大洋急剧变暖恶疾，正在以令人心惊肉跳的态势全面火上浇油，极有可能在未来数十年内急剧放大推高历史罕见的“超强厄尔尼诺超级风暴大事件”的爆发烈度与肆虐频次！"},
                {"en": "Meteorology humbles human technological arrogance, reminding us that our modern global empires are completely beholden to the turbulent breath of the sky.", "cn": "博大精深的大气气象物理学以最无情也最清醒的雷霆闪电，彻底粉碎了现代人类自诩战胜自然的科技傲慢，以铁一般的事实时刻警醒敲打着全人类：我们用钢铁与算法所筑起的繁华现代商业帝国，在天地造化那喜怒无常、翻云覆雨的苍穹呼吸面前，永远不过是沧海一粟、必须低头由衷敬畏的渺小凡尘！"}
            ]
        },
        {
            "title": "Unit 9 · 独立学术写作思辨：青年学者独立思考能力与权威导师指导的平衡",
            "description": "探讨学术批判性思维、打破学术权威迷信、导师引领与青年学术独立性大作文论点句。",
            "sentences": [
                {"en": "Novice academic researchers frequently face the delicate developmental dilemma of balancing submissive deference to renowned mentors with cultivating iconoclastic intellectual autonomy.", "cn": "初出茅庐的青年学术研究后生，在踏入科学探索殿堂初期，往往会陷入一个极具挑战性的两难成长困局：究竟应当在多大程度上对学术泰斗权威导师的言传身教保持由衷谦逊敬仰，又该在何等火候下鼓起大无畏的学术敢死队勇气、去破旧立新培育自身离经叛道的独立思想风骨！"},
                {"en": "Academic mentors possess decades of tacit methodological wisdom capable of steering impressionable doctoral candidates away from dead-end empirical cul-de-sacs.", "cn": "德高望重的资深学术博导名师，其胸膛深处沉淀凝结着数十年如一日在科学长夜中摸爬滚打摸索出的无价隐性方法论智慧，能够如暗夜明灯一般，轻而易举指引涉世未深的年轻博士生少走数年弯路、果断避开那些早已被证明是死胡同的实验伪命题！"},
                {"en": "Unquestioning sycophancy toward established paradigms risks transforming dynamic laboratory apprentices into ideological clones who reproduce their advisors' intellectual blind spots.", "cn": "对既有学术权威假说教条的毫无主见、唯唯诺诺的盲从奴才式谄媚迎合，其最大恶果莫过于将原本充满灵性生机的青年学术学徒，极其悲哀地降维驯化为毫无自主灵魂的克隆工具人，在低水平重复中将导师自身的认知盲区与偏见变本加厉代际复制！"},
                {"en": "Progressive scientific breakthroughs historically germinate when courageous youthful scholars dare to challenge the cherished hypotheses defended by entrenched academic establishments.", "cn": "纵观整部波澜壮阔的人类科学发现史册，那些破天荒、开天辟地的颠覆性科学真理大突破，十之八九皆是在那些初生牛犊不怕虎的英勇青年学者，敢于以大无畏的孤勇挑衅并彻底推翻老一代权威学者穷尽毕生心血死守的宝贝假说时，璀璨破晓破土而出的！"},
                {"en": "The Socratic pedagogical relationship flourishes most productively as an egalitarian intellectual partnership founded upon rigorous, dispassionate empirical cross-examination.", "cn": "源自古希腊苏格拉底先贤倡导的崇高师徒授受交锋关系，唯有在双方均将彼此视作追求宇宙终极真理的平等探索合伙人、且对话自始至终死死建立在基于铁证如山的客观实证多方严厉交叉质证基础之上时，方能绽放出最耀眼的智识繁花！"},
                {"en": "Cultivating genuine critical thinking demands the psychological courage to dismantle our own beloved arguments when confronted by contradictory data.", "cn": "在心智深处真正锻造出炉火纯青的批判性审辨独立思维，最严苛考验的从来绝非是对外界指指点点的嘴皮子利索，而恰恰是在铁证如山的冰冷反例异常数据面前，敢于狠下心肠亲手手刃摧毁自身曾敝帚自珍的心爱假说的至高学术求真勇气！"},
                {"en": "Authoritarian supervisory styles that micromanage experimental protocols suffocate the serendipitous risk-taking instinct required for revolutionary discoveries.", "cn": "某些沉溺于封建家长制威权的狭隘导师对实验微观细节无死角事无巨细的窒息式“微观微操干预”，其潜在的毁灭性代价，在于无情扼杀绞灭了前沿基础科学研究在荒原大冒险中所绝对不可或缺的纯真好奇心与敢于承担试错风险的野性灵感！"},
                {"en": "Doctoral training programs should deliberately foster dialectical seminars where junior students are graded upon the analytical rigor of their counter-arguments.", "cn": "高水平现代化博士研究生培养课程大纲，理应旗帜鲜明地设立专门的高端学术论辩深讨课，将鼓励青年学子敢于向主流正统学说亮剑开火、条理严密发表反向针锋相对论辩的深度与锐度，白纸黑字列为最高等级的卓越评分金标准！"},
                {"en": "Mentorship should not serve as an instrument of intellectual cloning, but as an expansive scaffold designed to propel disciples beyond the boundaries of their teachers.", "cn": "师道传承的全部神圣荣光，从来绝非是为了沦为流水线批量复制自身学术门生家奴的宗派私利工具；而永远理应宛如一座巍峨宽广的扶摇天梯脚手架，其存在的唯一崇高终极意义，正在于用毕生血肉之躯托举青出于蓝的后来者、助其扶摇直上九万里去勇敢击碎并超越先师所划定的狭隘地平线！"},
                {"en": "Independent intellectual inquiry requires the resilience to withstand prolonged academic loneliness and the cold skepticism of orthodox gatekeepers.", "cn": "走上一条特立独行、前无古人的独立科学求真探索羊肠小道，极其残酷地逼迫一个学者必须在灵魂骨髓深处，淬炼出一副足以硬扛忍受常人难以想象的数十年冷板凳学术孤寂、以及泰然直面正统学术守门人铺天盖地质疑白眼的钢铁抗逆心性！"},
                {"en": "Interdisciplinary dissertation committees incorporating external perspectives provide essential checks against parochial departmental dogmatisms.", "cn": "高瞻远瞩设立涵盖跨学科跨流派校外权威专家的博士学位论文答辩大委员会机制，构成了防止某些高校院系内部小圈子近亲繁殖、宗派门户偏狭因循守旧的制度性防腐解毒剂。"},
                {"en": "True scholarly maturity is attained when a researcher learns to assimilate foundational traditions deeply while questioning their ultimate limitations fearlessly.", "cn": "一个青年学者真正走向炉火纯青的成熟大格局风骨的终极标志，正在于他一方面能够以如饥似渴的谦卑姿态对先辈大师积淀的经典道统精髓倾囊吸收、了然于胸；另一方面却又能以大将般的从容自信，毫无惧色地向这些古老传统的终极边界与盲区发起大刀阔斧的审视质询！"},
                {"en": "Enlightened advisors measure their ultimate pedagogical achievement not by how faithfully students obey, but by how courageously they diverge.", "cn": "名垂青史的开明教育宗师在告慰平生时丈量自身执教生涯最高造诣的刻度尺，从来绝非在于盘点门下弟子对自己当年的一字一句究竟是何等俯首帖耳百依百顺；而唯独骄傲于回望：在历史的风口浪尖之上，门下高足究竟是以何等气吞山河的胆魄，敢于毅然决然同先师分道扬镳、破茧成蝶去开辟崭新的宏伟江山！"},
                {"en": "Knowledge is a relay race across centuries; honor your predecessors by taking their torch, and then running beyond their furthest horizons.", "cn": "人类追求真理与智识的万里大征程，自古以来就是一场跨越数千年沧海桑田的薪火相传接力大长跑；向先行者先辈致以最崇高、最深情的礼赞致敬，从来不是跪地膜拜其背影，而是从其颤抖的掌心中接过那一簇滚烫的神圣火炬，而后昂首挺胸、大踏步向着先人目光所及的最远地平线之外奋勇狂奔！"},
                {"en": "May every young scholar stand upon the shoulders of giants, not to slumber in their shadows, but to touch the untouchable stars.", "cn": "祈愿天底下每一位志存高远的青年学者，皆能有幸昂首屹立于人类古往今来那些巍峨巨人的伟岸肩膀之上——绝非为了在先贤宽阔厚重的庇荫之下安然沉睡偷安；而唯独为了借由巨人身躯的托举，以大无畏的昂首英姿，去奋力摘取那片凡胎肉身原本不可企及的浩瀚璀璨星空！"}
            ]
        },
        {
            "title": "Unit 10 · 独立学术写作思辨：人工智能时代科技工具对人际深度亲密度的利弊审问",
            "description": "探讨虚拟伴侣、算法中介沟通、社交技能退化与坚守真实肉身情感温度大作文论点句。",
            "sentences": [
                {"en": "The pervasive ubiquity of generative algorithmic conversational agents raises poignant existential questions regarding the authentic future of human interpersonal intimacy.", "cn": "高智能生成式算法拟人化对话大模型在日常起居中的无孔不入式野蛮渗透普及，正在以令人警醒之势，向全人类抛出了一连串关乎“未来人类两性与同胞之间真实人际深度亲密关系究竟何去何从”的刺骨存在主义深刻拷问！"},
                {"en": "Digital messaging algorithms offering automated predictive text suggestions subtly homogenize human emotional expression, reducing spontaneous vulnerability to prepackaged clichés.", "cn": "在智能手机键盘输入法深处大行其道的自动化“联想补全与高情商回复生成算法”，正在神不知鬼不觉间将人类至纯至性、原本充满毛边与瑕疵的真情实感流露，悄然熨平阉割为了毫无灵魂、套路满满的工业流水线式廉价预包装陈词滥调！"},
                {"en": "The alarming proliferation of synthetic artificial intelligence companions targets chronically lonely urbanites with illusions of unconditional adoration and perfect conversational compliance.", "cn": "在大都市水泥森林中如野草般疯长蔓延的各类高拟真“AI虚拟恋人伴侣软件”，精准狙击捕食着那些长年饱受孤独折磨的都市空巢男女，向其虚妄兜售着一种永远百依百顺、毫无真实人际摩擦冲突、虚幻得令人上瘾的所谓“完美无条件溺爱幻象”！"},
                {"en": "Authentic human love requires embracing messy emotional imperfections, negotiating inevitable misunderstandings, and confronting the terrifying risk of emotional rejection.", "cn": "大千世界中任何一段真正意义上动人心魄的人间至真大爱，从来都必须毫无保留地去拥抱接纳对方有血有肉有缺点的粗粝真实灵魂，心甘情愿在柴米油盐琐碎中经历磕磕绊绊的误解与磨合，并敢于直面随时可能遭受被辜负与心碎刺痛的巨大情感悬崖风险！"},
                {"en": "Substituting simulated algorithmic sycophancy for complicated flesh-and-blood relationships atrophies the socio-cognitive empathy muscles required for genuine partnership.", "cn": "如果一个现代人自暴自弃、懦弱地选择用冰冷代码在屏幕上所模拟出的虚妄谄媚逢迎，来全面替代现实生活中错综复杂、充满张力的人际血肉交往，必将以惊人速度导致其灵魂深处原本用于体察他人喜怒哀乐的“社会共情同理心大肌肉群”彻底废用性萎缩退化！"},
                {"en": "Hyper-curated algorithmic social feeds construct performative display spectacles where individuals project enviable lifestyle avatars while starving for quiet understanding.", "cn": "由商业算法精心编织投喂的社交网络晒图狂欢生态，已然彻底蜕变为一场场令人作呕的虚荣表演性景观大杂烩——每一个在屏幕前端庄演出的现代人，都在争先恐后向全网投射着令人艳羡的完美人设滤镜化身，然而其孤独的心灵深处却在如饥似渴地乞求着哪怕一星半点免受评判的真诚倾听与理解！"},
                {"en": "Phubbing—the dismissive snubbing of physical conversational companions in favor of checking smartphone notifications—fatally degrades the sacred quality of face-to-face dinner communion.", "cn": "在当代家庭餐桌与朋友聚会中普遍泛滥成灾的恶劣“低头族冷落症（Phubbing）”——即一个人漫不经心、极其轻蔑地无视身旁活生生的交谈挚友家人，而终日将眼珠子死死抠在随时弹窗的手机屏幕之上的丑陋做派，极具毁灭性地践踏粉碎了面对面围炉促膝促谈的神圣灵魂交流质感！"},
                {"en": "Children raised in households dominated by screen-distracted parents show measurable deficits in reading subtle micro-expressions and emotional emotional regulation.", "cn": "在长年被沉迷于刷短视频手机的“心不在焉低头族父母”所冷落抚养长大的下一代孩童身上，前沿临床儿童心理学已然测定出了令人触目惊心的恶果：其在辨识人类复杂微表情与自主调控负面情绪的能力维度上，呈现出断崖式的系统性发育迟缓与认知缺陷！"},
                {"en": "Virtual reality metaverses promising friction-free digital intimacy threaten to exacerbate societal atomization, entrenching isolated individuals in solipsistic echo chambers.", "cn": "高调兜售所谓“零摩擦、无门槛赛博数字亲密奇境”的虚拟现实元宇宙科技狂想，极有可能在客观上极大加剧现代社会的原子化碎裂大悲剧，将千千万万本就孤立无援的个体，更进一步深深锁死在唯我独尊、自娱自乐的精神唯我论回音壁深渊之中！"},
                {"en": "Human connection is deepened not through friction-free algorithmic optimization, but through the shared endurance of vulnerability, illness, and mortality.", "cn": "人类与人类之间那份重若千钧、生死相托的崇高灵魂相知与羁绊，从来绝非能够依靠任何精巧算法在无菌实验室里实现所谓“零摩擦最优解计算”；而自始至终唯独在彼此毫无防备地袒露脆弱、在病榻前端水喂药的相濡以沫、以及共同携手直面死亡终局沧桑岁月的患难与共中，方得百炼成金！"},
                {"en": "Technological mediation should serve as a bridge to facilitate physical rendezvous rather than an addictive digital substitute for embodied togetherness.", "cn": "任何现代化通讯科技工具所理应扮演的唯一健康文明角色，自始至终应当仅仅充当一座在时空阻隔时迅速促成线下肉身深情相聚相拥的便民渡桥，而坚决绝不容许反客为主、蜕变为全面霸占并替代真实肉身亲密相伴的赛博精神鸦片！"},
                {"en": "The sacred spark of human intimacy resides within the uncomputable glance of compassion, the warmth of an embrace, and the silence of shared presence.", "cn": "人类人际深度亲密关系最神圣不可侵犯的微观灵魂灵光，永远安详栖居在：两双深情眼眸猝然相撞时那一抹任何超级计算机算法都永远无法破译计算的慈悲与温柔、寒风中紧紧相拥时彼此透过毛衣传递而来的滚烫肉身体温、以及无需千言万语只需默默并肩端坐便心照不宣的静谧默契深处！"},
                {"en": "In an increasingly synthetic century, authentic biological presence and emotional honesty will become the rarest, most prized spiritual luxuries.", "cn": "在这个数字算法大模型日益以假乱真、大肆充斥泛滥的赛博人造新世纪，敢于以真实肉身亲临现场的深情陪伴、以及敢于在对方面前毫不设防袒露心扉的真诚情感赤诚，终将演变为人世间最不可多得、最为万金难求的无上精神至宝！"},
                {"en": "Technology is a magnificent tool to organize matter, but the human heart alone holds the divine secret of generating and sanctifying love.", "cn": "现代前沿科学技术固然是一套能够让我们翻江倒海、极其高效调度重组宏观客观物质世界的无双工具；然而在浩瀚茫茫宇宙深处，唯有我们人类这颗脆弱却温热的跳动心脏，才真正独自珍藏着点燃、孕育并神圣加冕人间真爱大同的至高神圣天机！"},
                {"en": "Let us fiercely guard the warm hearth of human communion; never surrender the living poetry of touch to the cold silicon ghosts of the machine.", "cn": "且让我们以至死不渝的觉醒与勇气，誓死守卫好属于我们人类灵魂深处那方温情脉脉的人间烟火相濡以沫温暖火塘吧——无论外面的科技狂浪翻卷出多么眩目的霓虹幻境，永远坚决不要把我们人类用肌肤触摸与热泪所谱写的鲜活生命诗篇，拱手出卖让渡给机器深处那些没有心跳、冰冷刺骨的硅基幽灵！"}
            ]
        }
    ]
    courses.append(build_course(toefl_meta, toefl_chapters))

    # -------------------------------------------------------------------------
    # 6. 高考英语真题语法填空与读后续写高分句 (10章) - 严格每章15句，共150句
    # -------------------------------------------------------------------------
    gaokao_meta = {
        "id": "course-ex-gaokao",
        "title": "《高考英语新课标真题语法填空与读后续写高分句》(Gaokao English) · 核心考纲攻克 (10章全集)",
        "category": "exam",
        "categoryName": "考试备考",
        "coverGradient": "from-amber-600 via-orange-700 to-red-800",
        "icon": "📝",
        "description": "专为全国高考英语冲刺打造，紧扣新课标读后续写三大抓手（动作神态、情绪心理、环境烘托）与满分升华金句。",
        "difficulty": "中级进阶 B1-B2",
        "tags": ["高考英语", "新课标", "读后续写", "语法填空", "高考核心"]
    }
    gaokao_chapters = [
        {
            "title": "Unit 1 · 青春立志与拼搏奋斗精神 · 乘风破浪的高考誓言",
            "description": "探讨高三冲刺拼搏、战胜自我怀疑、设立高远志向与坚定理想信念。",
            "sentences": [
                {"en": "Standing at the threshold of the matriculation examination, ambitious adolescents vow to conquer mountains of challenges through unyielding diligence.", "cn": "昂首庄严伫立在决战高考的至高历史关隘起跑线之上，意气风发的高三热血学子们以铁骨铮铮的誓言向苍天立誓：誓要用九死不悔的坚韧勤勉，踏平征途之上的万座重峦叠嶂！"},
                {"en": "The burning flame of youthful aspiration cannot be snuffed out by temporary examination setbacks or sleepless midnight anxieties.", "cn": "在青葱少年心田深处熊熊燃烧的青春梦想烈火，从来绝不可能被某次模拟考卷上暂时的挫败与阴霾、抑或夜深人静伏案时的焦虑失眠所轻易浇灭！"},
                {"en": "Early morning classrooms resound with rhythmic recitations as thousands of students seize every fleeting dawn minute to forge their academic destiny.", "cn": "清晨破晓的第一缕朝阳刚刚划破天际，整栋教学楼走廊里便早已回荡起朗朗书声的铿锵交响——千千万万高三学子正分秒必争抢抓每一个拂晓晨光，全力锻造自身的辉煌学术命运！"},
                {"en": "Self-discipline represents the quiet superpower that transforms chaotic wishes into razor-sharp, daily actionable study habits.", "cn": "高度严苛的自律精神，代表着世间最深邃沉静的无双超能力——它能将脑海中那些虚无缥缈的空洞幻想，淬炼转化为每日雷打不动、剑指巅峰的扎实学习行动习惯！"},
                {"en": "Teachers dedicate their nights to annotating student essay drafts meticulously, their graying temples bearing witness to selfless professional devotion.", "cn": "高三讲台前的辛勤恩师们夜夜伏案红烛之下，字斟句酌为每位学子细致批改作文试卷手稿，那早生华发的苍苍两鬓，无声镌刻见证着传道授业解惑的大爱奉献！"},
                {"en": "Solving knotty mathematical physics theorems late into the night polishes young analytical minds into formidable problem-solving instruments.", "cn": "在每一个寂静长夜里伏案攻关死磕错综复杂的数理化压轴题，如同最严酷的磨刀石，将青年学子的逻辑分析心智磨砺成为无坚不摧的破局利器！"},
                {"en": "Genuine self-confidence is not born from arrogant bravado, but is forged through hundreds of quiet hours of relentless targeted preparation.", "cn": "一个人骨子里真正坚不可摧的从容自信，从来绝非源自于轻浮浮躁的盲目狂妄吹嘘，而唯独是在数以百计无人问津的冷板凳苦读岁月里、经受千锤百炼精准沉淀出的硬核底气！"},
                {"en": "Peer encouragement transforms cut-throat rivalry into warm comradeship, enabling whole study groups to scale academic summits together.", "cn": "同窗同伴之间真挚由衷的并肩打气与携手互助，将原本令人窒息残酷的考场竞争，奇迹般升华转化为了休戚与共的战友情深，护航整个冲刺学习小组携手共登巅峰金榜！"},
                {"en": "A resilient warrior never bows before adversity; every fall upon the running track is merely a springboard for an explosive leap.", "cn": "一个百折不挠的真正青春勇士从来绝不会在逆境冰霜面前低头认输；在奔向梦想塑胶跑道上的每一次猝然跌倒，无非是为下一次更加惊世骇俗的绝地反弹积蓄更惊人的爆发势能！"},
                {"en": "Keep your eyes fixed firmly upon the stars while planting your marching footsteps deeply and conscientiously into the solid earth.", "cn": "在仰头深情凝望苍穹浩瀚星空崇高抱负的同时，千千万万切记把脚下的每一步奋斗行囊，工工整整、毫不浮躁地深扎进脚下厚德载物的坚实泥土深处！"},
                {"en": "Mock examinations serve not as definitive final verdicts, but as diagnostic compasses designed to illuminate hidden conceptual vulnerabilities.", "cn": "高考前接踵而至的模拟大联考，从来绝非是对一个人终身前途的死刑判决书；而是一面面无比诚实的诊断照妖镜，专为精准照亮扫清知识体系中残存的微观死角。"},
                {"en": "Maintaining physical vitality through brisk evening runs around the school track clears mental cobwebs and recharges psychological stamina.", "cn": "晚自习课间换上跑鞋在校园红色塑胶跑道上大汗淋漓的快节奏夜跑，能够瞬间荡涤扫清大脑思维的疲惫锈蚀，为后续冲刺注入充沛的体能电池。"},
                {"en": "Adversity is the supreme furnace wherein raw youthful potential is refined into unshakeable diamond character.", "cn": "命运所降下的一切狂风骤雨与逆境挫折，本质上都是大自然最神圣的炼丹大熔炉——正是在这烈火洗礼之下，粗粝青涩的少年潜能方能百炼升华为坚不可摧的璀璨金刚！"},
                {"en": "The final examination bell will ring only once, but the habits of excellence formed during these grueling months will illuminate your entire life.", "cn": "高考终考铃声在六月蝉鸣中固然只会划破天际鸣响一次；然而在这一千个伏案苦读晨昏中所深深铸就的追求卓越与坚韧风骨，将化作一生不灭的火种，永远照亮你的锦绣前程！"},
                {"en": "May your pens dance across the test papers like galloping steeds; stride forward proudly, and conquer your destiny without fear!", "cn": "祈愿你手中的墨水笔尖在雪白的考卷大地上宛如万马奔腾般肆意挥洒如画；昂首挺胸大踏步向前冲锋吧，无所畏惧地亲手加冕属于你自己的无上命运凯旋大王冠！"}
            ]
        },
        {
            "title": "Unit 2 · 劳动教育与动手实践素养 · 劳动最光荣的人生底色",
            "description": "探讨学农学工社会实践、家务劳动技能、崇尚工匠精神与反对好逸恶劳。",
            "sentences": [
                {"en": "Labor education integrated into modern schooling cultivates profound respect for frontline agricultural toil and manual craftsmanship.", "cn": "全面系统融入现代基础教育体系的劳动素养育人大工程，致力于在青葱少年心田深处构筑起对一线田野农耕挥汗劳作与车间工匠精神的至高敬重。"},
                {"en": "Students harvesting sweet potatoes in rural experimental fields experience the arduous sweat required to furnish dining table nourishment.", "cn": "走出象牙塔走进广袤农村实践基地的学子们手握铁锹弯腰刨挖红薯，在泥土芬芳中真真切切体悟到了维系餐桌一日三餐丰盈所需的沉甸甸血汗不易。"},
                {"en": "Mastering essential culinary cooking techniques empowers teenagers to manage autonomous domestic nutrition when living away from home.", "cn": "熟练掌握家常煎炒烹炸等基本下厨掌勺烹饪技能，能够让羽翼渐丰的年轻学子在未来告别父母独立远赴异乡求学打拼时，拥有从容自律掌舵健康饮食的独立生存底气。"},
                {"en": "Vocational carpentry workshops teach adolescents that creating fine furniture demands patient measurement, meticulous sanding, and zero tolerance for sloppiness.", "cn": "在墨香四溢的传统木工手作工坊里，高中生们在刨花飞扬中深刻领悟到：精雕细琢一件传世家具，全凭分毫不差的毫米级测量、数千遍的耐心打磨，以及对任何应付糊弄的零容忍！"},
                {"en": "A society that disdains honest physical labor while romanticizing parasitical idle luxury is sliding down the precipice of moral decadence.", "cn": "一个在风气上自命清高鄙夷诚实重体力劳动、却病态追捧崇拜不劳而获寄生虫式奢靡排场的畸形社会，已然在不知不觉中滑向了道德堕落溃败的凶险万丈深渊！"},
                {"en": "Volunteering to sweep autumn leaves across community elderly centers fosters warm intergenerational empathy and civic civic responsibility.", "cn": "在萧瑟深秋主动报名走进社区空巢孤寡老人大院挥帚清扫满地落叶，在举手投足的微小劳作中涵养激荡出了血浓于水的代际温情关怀与崇高公民公德。"},
                {"en": "Sewing buttons and repairing torn garment seams instill valuable lessons in material resource conservation and anti-consumerist frugality.", "cn": "亲手穿针引线缝牢松动的纽扣、巧手修补磨损的衣角，在针头线脑的朴素细节中，为当代青少年上了一堂胜过千言万语的爱惜物力、厉行节约的生动通识大课。"},
                {"en": "Cleaning campus biology laboratories scrupulously teaches budding researchers that meticulous sanitary sterilization underpins scientific integrity.", "cn": "在每次实验结束后一丝不苟亲手将显微镜载玻片与生物反应试管刷洗得一尘不染，让初入科学殿堂的雏鹰深刻铭记：对实验台卫生的极端苛求，构成了捍卫严谨科研底线的头号红线！"},
                {"en": "The calloused hands of hardworking farmers and bricklayers lay the physical foundation supporting all ivory-tower scholarly contemplation.", "cn": "千千万万面朝黄土背朝天的普通农民与工地上挥汗如雨的瓦工大叔手掌上那厚厚的老茧，才是稳稳托举起象牙塔深处一切优雅高深学术哲学沉思的最坚固物理地基！"},
                {"en": "Manual dexterity trained through pottery wheel manipulation stimulates creative spatial neuroplasticity across the adolescent cerebral cortex.", "cn": "在旋转飞驰的拉坯转盘上用双手灵巧感知塑造温润陶泥形态的指尖艺术训练，能够强力刺激青葱少年大脑顶叶皮层空间想象与具象创造脑神经突触的蓬勃重塑！"},
                {"en": "Repaving cracked rural gravel pathways with wheelbarrows of cement transforms abstract socialist civic rhetoric into tangible community infrastructure.", "cn": "顶着炎炎烈日推着独轮车运送水泥砂浆、亲手把乡村泥泞颠簸的小路平整铺筑为平坦水泥便民路，瞬间将干瘪的书本口号具象化为了造福万家老百姓的暖心民生工程！"},
                {"en": "Cultivating school botanical rooftop gardens teaches urban children the sacred natural rhythms governing seed germination and fruit ripening.", "cn": "在教学楼屋顶开辟班级微型农场，让水泥森林里的孩子在亲手松土浇水捉虫的劳作中，深情体悟种子破土萌芽直至金秋挂果成熟背后大自然不可逾越的神圣节律。"},
                {"en": "Sweat shed during sincere physical labor cleanses the soul of entitlement, restoring grounded humility and appreciation for life's blessings.", "cn": "在酣畅淋漓的诚实体力劳作中所挥洒出的每一滴滚烫汗水，皆能如甘霖荡涤尘埃般洗净一个人骨子里自视甚高的特权傲慢，重新找回扎根厚土的踏实谦卑与由衷感恩之情！"},
                {"en": "Labor is the fountainhead of all human wealth and the grand sculptor carving the contours of human civilizational nobility.", "cn": "辛勤的诚实劳动创造不仅是天地间一切物质精神财富的源头活水，更是手握刻刀、精雕细琢出整个人类崇高伟大文明骨骼经络的大匠之魂！"},
                {"en": "Honor the dignity of every toiling laborer; for in the sacred crucible of sweat, humankind creates the flourishing architecture of our future.", "cn": "请向这大千世界中每一个起早贪黑挥汗奋斗的平凡劳动者致以最深情的脱帽礼赞吧——因为正是在这滚烫的血汗熔炉深处，全人类正在携手缔造出属于我们未来的无比繁茂的文明大厦！"}
            ]
        },
        {
            "title": "Unit 3 · 传统非遗技艺传承与时代创新 · 焕发古老技艺新生机",
            "description": "探讨苏绣、皮影戏、景德镇陶瓷与现代潮玩跨界融合的时代答卷。",
            "sentences": [
                {"en": "Master embroiderers dedicating lifetimes to Suzhou silk tapestries split individual silk threads into dozens of hair-thin filaments meticulously.", "cn": "倾注毕生心血坚守在江南绣绷前的苏绣非遗国宝级老工匠，能够凭一双双巧手将一根寻常丝线以令人叹为观止的神技抽丝劈分为数十根细若游丝的隐形蚕丝！"},
                {"en": "Traditional shadow puppetry revitalizes its historical theatrical appeal by adapting legendary mythological epics into contemporary anime collaborations.", "cn": "源远流长的中国传统皮影戏光影艺术，敢于跳出历史舒适圈，通过将古典神话史诗同现代先锋国潮动漫IP进行惊艳跨界联动，在年轻一代心底重新点燃了传统戏曲光影狂潮！"},
                {"en": "Jingdezhen ceramic artisans fire porcelain kilns at searing temperatures exceeding thirteen hundred degrees, coaxing translucent celadon glazes from crude clay.", "cn": "千年瓷都景德镇的当代守艺陶艺大师们在千年窑火深处将炉温逼升至一千三百度极致烈焰，在火与土的造化涅槃中，硬生生从粗糙陶土里淬炼催生出如冰似玉的传世青瓷天青神韵！"},
                {"en": "Traditional intangible cultural heritage must not be locked away in stagnant museum vitrines, but must actively integrate into modern functional living spaces.", "cn": "世代相传的珍贵非物质文化遗产绝不应被死板冰冷地锁死在积满灰尘的博物馆玻璃展柜深处自生自灭，而必须以大格局主动张开双臂、活态深度融入现代人的当代高品质起居空间！"},
                {"en": "Young design graduates fuse ancient mortise-and-tenon architectural joints with modern modular home furniture, eliminating reliance upon toxic chemical adhesives.", "cn": "满怀文化自信的新锐青年家具设计师们，巧妙将传承数千年的中国古代“榫卯结构”木作大智慧同现代模块化极简家居完美咬合，从根本上彻底终结了对刺鼻有毒化学胶水粘合剂的依赖！"},
                {"en": "Batik textile dyeing techniques utilizing natural beeswax and botanical indigo extracts present eco-friendly, circular alternatives to synthetic petrochemical dyes.", "cn": "少数民族流传千年的传统天然植物蓝靛与蜂蜡点蜡防染“蜡染技艺”，为当代饱受化学重金属污染困扰的纺织服装印染工业，提供了完美的绿色环保循环经济替代答卷！"},
                {"en": "Digital archiving platforms deploy high-resolution laser scanning to create permanent three-dimensional digital twins of fragile ancient mural pigments.", "cn": "高规格搭建的国家级文化遗产数字档案库，采用纳米级三维激光扫描与多光谱全息测绘，为石窟中正在不可逆风化褪色的娇贵古代壁画矿物颜料永久抢救封存了“数字孪生化身”！"},
                {"en": "Apprenticing under an octogenarian master craftsman demands enduring years of monotonous baseline drills before unlocking the secrets of expressive virtuosity.", "cn": "拜倒在耄耋白发非遗泰斗大师门下求道学艺，极其严苛地考验着后生的定力：必须耐得住数年如一日在枯燥基础功法上的磨杵成针苦练，方能窥见化境传神的核心神髓！"},
                {"en": "Intangible heritage livestreaming campaigns allow remote rural craftswomen to sell handmade bamboo weavings directly to appreciative international patrons.", "cn": "依托移动互联网与跨境电商高清慢直播大潮，大山深处身怀绝技的乡村绣娘竹编大娘，得以彻底绕开层层中间商盘剥，直接将凝聚着手心温度的纯手工竹编手作一键远销海外！"},
                {"en": "True preservation of ancestral cultural craftsmanship does not mean the worship of cold ashes, but the fearless preservation and transmission of living fire.", "cn": "对祖先传世非遗技艺手艺最崇高、最深情的传承与守护，从来绝非是对早已冷却变凉的冰冷香灰的刻板膜拜；而永远在于以大无畏的创新胆魄，誓死守护好那簇生生不息的活态文明薪火！"},
                {"en": "Intangible cultural heritage education integrated into high school art curriculums inspires teenagers to take pride in their civilizational roots.", "cn": "将非遗扎染与陶艺活态引入高中美术必修讲堂，在少年指尖飞扬中，深深播撒下了对中华五千年璀璨文明根脉的由衷自豪与文化自信。"},
                {"en": "Woodblock printing workshops invite visiting tourists to ink engraved pear-wood boards and press fibrous rice paper with their own hands.", "cn": "在古色古香的雕版印刷活态体验馆里，天南海北的游人亲手蘸取纯正松烟墨汁、在梨木雕版上铺平宣纸轻轻拓印，在油墨清香中触摸历史脉搏。"},
                {"en": "Contemporary fashion runways celebrating Chinese Hanfu silhouettes prove that ancestral aesthetics resonate effortlessly with modern haute couture.", "cn": "国际顶级时尚周大秀上大放异彩的中国国风华服汉服剪裁与云肩马面裙设计，无可辩驳地向世界宣告：东方古典美学神韵能够毫无违和地惊艳领航现代高定风尚！"},
                {"en": "Oral epic bards who can chant tens of thousands of verse lines from memory embody a living, breathing acoustic library of ancestral memory.", "cn": "能够仅凭大脑记忆在冬日篝火旁一气呵成深情咏唱数万行史诗篇章的民间古老弹唱艺人，本身就是一座座穿梭行走在人间的大自然活态口述史诗图书馆！"},
                {"en": "Let ancient wisdom illuminate our modern journey; preserve the old with devotion, innovate the new with daring, and flourish forever.", "cn": "且让古老的东方先贤工匠智慧深深照亮我们当代人破浪前行的漫漫征途吧——以至诚敬畏之心守住根本，以敢为人先之姿大步开拓创新，在天地之间绽放出万古长青的不朽光芒！"}
            ]
        },
        {
            "title": "Unit 4 · 乡村振兴与美丽中国生态画卷 · 绘就山乡巨变新篇章",
            "description": "探讨精准脱贫攻坚成果巩固、农村电商直播、美丽宜居乡村建设与绿水青山就是金山银山。",
            "sentences": [
                {"en": "The strategic nationwide rural revitalization campaign transforms once-impoverished mountain hamlets into picturesque, prosperous ecological agritourism destinations.", "cn": "波澜壮阔席卷神州大地的全面乡村振兴国家战略，正在以神奇的画笔，将昔日穷山恶水、交通闭塞的贫困小山村，华丽蜕变为一幅幅游人如织、富裕宜居的生态文旅锦绣画卷！"},
                {"en": "High-speed broadband optic fiber cables deployed across remote mountainous ravines bridge digital divides, empowering rural farmers to broadcast orchard harvests live.", "cn": "千兆高速光纤通信大动脉披荆斩棘翻山越岭铺设直达大山深处的千沟万壑，彻底抹平了城乡数字鸿沟，强有力赋能了果农大叔得以架起手机三脚架向全网高清直播漫山遍野的蜜桃丰收！"},
                {"en": "Terraced organic tea plantations nestled amid swirling mist slopes produce pesticide-free emerald leaves that command premium prices across metropolitan markets.", "cn": "常年掩映在江南云山雾罩苍翠山峦褶皱深处的千亩高山生态有机茶园，出产着零农残的极品嫩绿芽尖，在繁华一线都市高档商超里斩获了令人惊喜的溢价红利！"},
                {"en": "Restoring pristine riverbanks, eliminating open sewage ditches, and retrofitting sanitary household latrines elevate the daily baseline dignity of rural existence.", "cn": "铁腕推进水清岸绿的河道综合生态治理、彻底取缔露天发臭污水沟渠，并为千家万户全面实施卫生无害化户厕旱厕大改造，从根底上托举起广大乡亲起居生活的体面与尊严！"},
                {"en": "Young collegiate graduates returning home, celebrated as 'new farmers', deploy drone spraying and automated IoT irrigation to modernize agricultural yields.", "cn": "越来越多满怀赤子之心的大学毕业生毅然告别大都市霓虹、背起行囊返乡创业，这群被时代亲切誉为“新农人”的生力军，熟练操纵农业无人机植保与物联网智能滴灌，为传统农田插上了高科技腾飞的翅膀！"},
                {"en": "Village cultural auditoriums host evening calligraphy exhibitions, choir rehearsals, and folk instrument ensembles, enriching communal spiritual wellness.", "cn": "在全村老少齐聚的现代化乡村文化礼堂里，每逢傍晚便热闹非凡上演着村民书法摄影展、红歌合唱排练与传统民乐丝竹大联欢，极大丰盈滋养了乡野田园的精神文化土壤！"},
                {"en": "Developing specialized regional agricultural geographical indication brands shields distinctive village honey and walnut cooperatives from price-gouging intermediaries.", "cn": "高标准申报打造具有鲜明乡土辨识度的“国家地理标志农产品金字招牌”，构筑起了一副坚不可摧的维权盾牌，誓死捍卫村集体原生态野生土蜂蜜与核桃合作社免遭黑心二道贩子压价洗劫！"},
                {"en": "Clear waters and green mountains are not obstacles to prosperity, but represent inestimable assets of gold and silver safeguarding future generations.", "cn": "山清水秀的澄澈绿水与层峦叠嶂的巍峨青山，从来绝非是阻碍老区老百姓脱贫致富的绊脚石；其骨髓深处所蕴藏的无价生态福祉，实打实正是为子孙后代保驾护航的“金山银山”！"},
                {"en": "Rural solar photovoltaic installations mounted atop barn roofs generate clean electricity while generating reliable monthly dividends for cooperative members.", "cn": "整齐密布铺设在农家庭院与牛舍大棚屋顶之上的分布式光伏电站，在持续源源不断输出零碳绿电的同时，每月为村集体合作社广大社员带来风雨无阻、旱涝保收的真金白银发电分红！"},
                {"en": "Revitalizing dilapidated stone farmhouses into chic boutique bed-and-breakfasts creates local hospitality employment that entices migrating parents to remain home.", "cn": "把闲置荒废年久失修的百年老石屋老瓦房，匠心独运改造成一间间推窗见山的高端乡间精品民宿，不仅催生出大量就近就业岗位，更让常年在沿海打工漂泊的父母得以返乡陪伴留守儿童茁壮成长！"},
                {"en": "Preserving ancient ancestral Ginkgo trees in the village plaza maintains the living historical continuum anchoring communal neighborhood identity.", "cn": "悉心保护修缮村头古老祠堂广场中央那株历经千百年风霜雨雪依然枝繁叶茂的千年古银杏树，守护住了一个宗族与全体街坊邻里休戚与共的活态集体乡愁记忆。"},
                {"en": "Cold-chain refrigerated logistics networks transport fresh picked cherries from orchard hillsides to coastal city fruit bowls within twelve hours.", "cn": "四通八达、无缝衔接的国家级现代冷链物流保鲜配送大网络，实现了让清晨挂着露珠现摘现装的娇贵大樱桃，在短短十二小时内直抵千里之外沿海千家万户的果盘之中！"},
                {"en": "The transition from chemical fertilizer overuse toward organic microbial composting restores exhausted topsoils and revives earthworm populations.", "cn": "坚决从大水大肥大农药的粗放老路子，大踏步跨越转向施用有机生物有机肥与微生物菌肥进行深层改土培肥，成功唤醒激活了沉睡疲惫的耕地腐殖土，令久违的蚯蚓大军重现田埂！"},
                {"en": "Rural revitalization is not merely a material face-lift, but a spiritual renaissance rekindling self-reliance, cultural pride, and pastoral harmony.", "cn": "举国推进的乡村振兴伟大长征，绝非仅仅是一场浮于表面、粉刷白墙的所谓面子工程；而是一场全方位唤醒乡村自立自强精神、重塑文化自信与重建田园天人合一生态的伟大民族精神文艺复兴！"},
                {"en": "Behold the magnificent transformation sweeping across the Chinese countryside; in every blooming orchard lies the enduring hope of our nation.", "cn": "请屏息凝神深情眺望这片正在神州山川原野深处惊艳铺展的大地丰碑与山乡巨变吧——在那漫山遍野竞相绽放的繁茂花果枝头深处，生生不息跳动着我们伟大民族复兴的最坚实希望！"}
            ]
        },
        {
            "title": "Unit 5 · 读后续写核心技能突破：动作连动、神态刻画与情感细腻描摹",
            "description": "探讨读后续写高分微技能：心理微反应、肢体动作链、眼神与面部微表情长难句。",
            "sentences": [
                {"en": "Upon hearing the terrifying thunderclap, the lost little boy froze in his tracks, trembling uncontrollably like a withered leaf in autumn wind.", "cn": "当那一记令人魂飞魄散的惊天炸雷猝然在头顶轰然炸响之际，在密林中迷路的小男孩瞬间吓得呆立在原地动弹不得，浑身上下如秋风中的一卷枯叶般止不住地瑟瑟剧烈发抖。"},
                {"en": "Her heart pounding like a frantic drum against her ribs, she drew a deep, quivering breath and stepped into the spotlight.", "cn": "胸膛深处的心脏宛如一面发了疯的战鼓般疯狂撞击着她的肋骨，她狠狠咽了口唾沫，深吸了一口微微颤抖的清气，毅然决然迈步跨入了灯火通明的舞台聚光灯下！"},
                {"en": "Tears welled up in her glistening eyes, blurring the familiar handwriting inscribed across the wrinkled yellow envelope.", "cn": "滚烫的泪水不可遏制地迅速在她晶莹的眼眶深处涌起打转，瞬间将那封泛黄褶皱信封之上苍劲熟悉亲切的亲笔字迹涂抹得一片模糊。"},
                {"en": "He clenched his fists so tightly that his knuckles turned pale, battling with every ounce of willpower to stifle the fury surging within his veins.", "cn": "他双拳紧紧攥得如此之死，以至于指关节瞬间因充血褪去而惨白如纸，倾尽全身每一丝咬牙切齿的自律意志力，苦苦死死压制着在周身血管深处狂暴翻滚的滔天怒火！"},
                {"en": "A radiant, triumphant smile slowly broke across her exhausted countenance, illuminating the dimly lit laboratory like an unexpected ray of golden dawn.", "cn": "一抹灿烂耀眼、饱含胜利狂喜的由衷笑容，从她那张布满疲惫与血丝的脸颊上缓缓破土绽放，宛如一抹穿透阴霾的金色晨曦，瞬间彻底照亮了整间昏暗的科学实验室！"},
                {"en": "Kneeling beside the whimpering wounded stray puppy, the compassionate girl gently smoothed down its matted fur with soothing, rhythmic strokes.", "cn": "蹲下身子小心翼翼跪坐在那只瑟瑟发抖、发出微弱呜咽呜咽呻吟的受伤流浪小狗身旁，心怀大爱的善良女孩伸出柔软手掌，以充满安抚律动的轻柔节奏，一遍遍轻轻抚平它凌乱打结的脏毛。"},
                {"en": "Gasping for thin air upon the cliff summit, the mountaineer slumped down against the granite boulder, utterly drained of physical strength yet spiritually elated.", "cn": "在陡峭万仞的山巅悬崖绝顶大口大口贪婪喘着稀薄刺骨的空气，那位浑身湿透的登山勇士一屁股瘫软倚靠在巨大的花岗岩巨石旁，肉身体能虽已彻底透支殆尽，但灵魂深处却在群峰之巅体验着前所未有的狂喜与飞翔！"},
                {"en": "Her voice choked with emotion, she struggled to articulate words of gratitude, but only a muffled sob escaped her trembling lips.", "cn": "咽喉被汹涌翻滚的感泣情绪彻底哽住堵死，她拼尽全力试图从喉咙深处挤出感激道谢的话语，然而从她剧烈颤抖的朱唇缝隙间挣扎逃逸而出的，唯有一声令人心碎的心疼抽泣。"},
                {"en": "He paced back and forth across the sterile hospital waiting room corridor, his furrowed brow betraying the agonizing storm raging behind his silent eyes.", "cn": "他手足无措地在充斥着刺鼻消毒水气味的医院抢救室门外楼道里焦躁地来回踱步，那紧紧拧成一个死结的深锁眉头，毫无保留地出卖了他那看似沉默无言的眼眸深处正在疯狂肆虐的煎熬心绪大风暴！"},
                {"en": "With steady hands despite her internal panic, the surgeon adjusted the focal lens, leaned forward, and made the critical incision with microscopic precision.", "cn": "尽管胸膛深处早已惊涛骇浪恐慌狂跳，然而在主刀手术台前，女外科大夫那双纤细双手却宛如外科机械臂般出奇地沉着坚如磐石，微微俯身向前，以微米级的极限精度手起刀落切下了生死攸关的拯救第一刀！"},
                {"en": "He lowered his gaze in burning shame, staring intently at the scuffed tips of his shoes as if wishing the floor would open up.", "cn": "在无地自容的火辣辣羞耻感灼烧之下，他深深埋下头颅，两颗眼珠子死死死死盯着自己脚下那双磨损开裂的破球鞋鞋尖，恨不得脚底下立刻裂开一道地缝让自己当场钻进去！"},
                {"en": "A solitary tear traced a slow, glistening path down the old grandfather's weathered cheek, carrying memories of decades gone by.", "cn": "一滴晶莹剔透的老泪，沿着白发苍苍的老祖父那张饱经沧桑风霜沟壑纵横的皱纹面颊缓缓滑落滑过，默默无声承载着几十载沧海桑田的过往唏嘘回响。"},
                {"en": "Throwing her arms enthusiastically around her mother's neck, the little girl buried her face into her shoulder and wept with pure relief.", "cn": "小女孩张开稚嫩双臂如乳燕投林般扑向扑进母亲温暖的怀抱紧紧搂住母亲的脖颈，将哭花的小脸蛋深深埋在妈妈温暖的肩窝里，由衷哭出了劫后余生的狂喜与释怀！"},
                {"en": "He swallowed hard, wiped his clammy palms on his trousers, and mustered the courage to knock on the principal's intimidating door.", "cn": "他艰难地干咽了一口唾沫，在校服裤腿两侧狠狠擦干手心里冒出的冷汗，深吸一口气，终于鼓起全身胆魄郑重敲响了那扇令人望而生畏的校长办公室大门！"},
                {"en": "Mastering the vivid interplay of bodily actions and psychological nuances elevates storytelling from bland narration into breathtaking emotional cinema.", "cn": "炉火纯青掌握人体微观肢体动作链同幽微心理情绪微表情之间天衣无缝的交织刻画艺术，能够瞬间将一篇原本味同嚼蜡的干瘪记叙文，华丽升华蜕变成为一幕幕令人屏息凝神、催人泪下的震撼情感大银幕电影！"}
            ]
        },
        {
            "title": "Unit 6 · 读后续写核心技能突破：自然环境烘托与物象象征伏笔",
            "description": "探讨读后续写高分微技能：恶劣天气渲染绝境、破晓微光象征希望、特定信物伏笔回收长难句。",
            "sentences": [
                {"en": "The howling blizzard whipped icy snowflakes viciously against the cabin window panes, engulfing the isolated mountain forest in a blinding white vortex.", "cn": "狂暴肆虐的漫天暴风雪发出凄厉骇人的鬼哭狼嚎，将一片片冰冷如刀的雪花狠狠抽打在守林人小木屋的玻璃窗棂之上，将整座与世隔绝的茫茫林海雪原瞬间生生吞噬进了一片令人目眩窒息的惨白死亡大漩涡！"},
                {"en": "The relentless summer sun scorched the cracked barren soil mercilessly, baking the stagnant air into an oppressive, shimmering furnace.", "cn": "天空中那一轮毒辣无情的夏日骄阳，冷酷无情地暴晒炙烤着大地皲裂焦渴的万顷干涸荒土，将凝固死寂的空气生生烘烤成了一个令人呼吸停滞、热浪蒸腾翻滚的炼狱大蒸笼！"},
                {"en": "Through the dense, choking fog, a single warm yellow beacon light flickered tenaciously across the bay, whispering promises of safety and harbor.", "cn": "在那片令人窒息绝望、伸手不见五指的浓稠弥天大雾深处，远方平静海湾对岸一座孤零零的黄色灯塔微光在惊涛骇浪中执着地顽强闪烁跳动，如同一句穿越长夜的温柔私语，向迷途扁舟深情许下了港湾避风的安全承诺！"},
                {"en": "The storm clouds that had shrouded the mountain valley for hours finally parted, permitting rays of golden afternoon sunshine to crown the pine ridge.", "cn": "在幽深山谷峡谷上空翻滚盘踞了数个小时之久的黑压压暴风雨积雨云，终于在山风吹拂下缓缓裂开撕开了一道天光口子，恩赐洒下一束束灿烂金黄的午后斜阳，为郁郁葱葱的墨绿松林山脊披上了一座神圣金冠！"},
                {"en": "A fragile green shoot pushed its way stubbornly through the jagged concrete crack, standing as an unyielding emblem of life's triumphant tenacity.", "cn": "一株稚嫩而纤细的翠绿嫩芽，以大无畏的倔强姿态，硬生生从坚硬冰冷、刀劈斧削般的混凝土路面狰狞裂隙深处傲然破土挺拔钻出，巍然化作了天地间礼赞生命坚韧抗逆大获全胜的最高图腾！"},
                {"en": "The weathered, leather-bound pocket watch ticked softly against his breast, its rhythmic chime echoing the heartbeat of his beloved grandfather who carried it across wars.", "cn": "那一枚表面磨损斑驳、装在牛皮套里代代相传的祖传怀表，紧贴在他的胸膛内侧发出轻柔而富有节律的微弱滴答声，那熟悉的秒针心跳，仿佛跨越时空与当年曾携带着它出生入死冲锋火线的老祖父的滚烫脉搏达成了奇妙共振！"},
                {"en": "Night wrapped the deserted countryside in velvety stillness, punctuated only by the distant, melancholic hooting of an owl hidden deep within the oaks.", "cn": "漆黑的天鹅绒夜色将荒无人烟的沉寂乡野原野温情包裹进一片静谧祥和之中，四周唯有一声声从古老橡树林深处幽幽传来的夜枭咕咕啼鸣，划破长夜的苍茫。"},
                {"en": "The swelling muddy creek overflowed its grassy banks, transforming the familiar pasture path into a swirling, treacherous brown torrent in minutes.", "cn": "暴雨下迅速暴涨翻滚的浑浊溪流，瞬间漫过并冲垮了长满杂草的低矮堤岸，在短短数分钟内便将乡亲们平日里无比熟悉欢笑的放牧羊肠小径，粗暴改造成了一条波涛翻滚、暗藏杀机的凶险黄泥大激流！"},
                {"en": "Autumn leaves carpeted the winding stone trail in a dazzling mosaic of crimson, amber, and gold, whispering secrets under every gentle footfall.", "cn": "漫山遍野金风打落的斑斓秋叶，如同一张由大自然亲手编织铺就的绚烂厚重地毯，在曲折蜿蜒的青石古道上密密麻麻拼接出一幅由深红、琥珀与碎金交织的大自然拼图，在漫步者放轻的脚步踩踏下发出沙沙的温柔私语。"},
                {"en": "The sudden rainbow arching gracefully across the rain-washed azure sky mirrored the serene reconciliation that had healed their fractured friendship.", "cn": "那一抹在刚刚被暴风骤雨彻底荡涤洗净的蔚蓝碧空苍穹之上蓦然凌空架起的瑰丽七彩绚烂彩虹，恰如其分地完美映照了刚才在他们两人心头破冰消融、重新冰释前嫌的莫逆同窗深情！"},
                {"en": "The dying campfire crackled softly, sending solitary orange sparks drifting upward to dissolve into the sea of indifferent midnight stars.", "cn": "营地中央行将熄灭的篝火余烬发出轻微毕剥声响，将一粒粒孤单跳跃的橘红色火星缓缓送向高空，随后悄然融化蒸发在头顶那片浩瀚冷漠的满天星海深处。"},
                {"en": "A suffocating, eerie silence descended upon the abandoned mansion, so absolute that the scurrying of a tiny mouse behind the wallpaper sounded thunderous.", "cn": "一股令人心惊肉跳、毛骨悚然的窒息死寂，如同无形的大网般轰然降临笼罩在荒废破败的老宅废墟之上，安静得令人窒息，以至于墙纸缝隙后一只微小老鼠的蹑足窜行，听起来都宛如雷霆轰鸣！"},
                {"en": "The fresh, earthy petrichor rising from the baked soil heralded the arrival of long-awaited monsoon showers upon the parched agricultural basin.", "cn": "久旱逢甘霖的大地泥土中被雨点击打蒸腾而起的独特泥土清香（Petrichor），欢快宣告着期盼数月之久的救命季风甘霖终于盛大君临久旱的大平原粮仓！"},
                {"en": "A silver crescent moon hung serenely above the tranquil lake, casting a shimmering path of rippling liquid quicksilver straight to their wooden boat.", "cn": "一弯清冷典雅的银色上弦残月安详高悬在水波不兴的静谧湖面之上，在如镜的水天一色中倒映铺展开了一条直通他们脚下木船的波光粼粼的流动水银神道！"},
                {"en": "Mastering atmospheric scene setting endows narrative prose with breathing physical realism, transforming backdrop nature into an active emotional mirror of characters' inner souls.", "cn": "炉火纯青驾驭大自然环境氛围的渲染烘托与物象象征，能够赋予叙事散文以呼吸律动的沉浸式物理质感，将身后的山川风雨自然草木，华丽化身为一面面洞察并映照剧中人物灵魂深处喜怒哀乐的最深情明镜！"}
            ]
        },
        {
            "title": "Unit 7 · 读后续写核心技能突破：心理蜕变与主旨升华满分范式",
            "description": "探讨读后续写高分微技能：战胜恐惧顿悟、宽恕与爱、责任担当觉醒与大结局哲思长难句。",
            "sentences": [
                {"en": "In that pivotal epiphany, she finally realized that true courage is not the complete absence of fear, but the moral triumph over it.", "cn": "正是在那个电光石火般的顿悟破晓高光时刻，她终于在灵魂最深处大彻大悟：人世间真正的盖世大智大勇，从来绝非是内心毫无恐惧的麻木无知；而恰恰是明知前路凶险万分、却依然为了心中的道义大爱断然战胜恐惧挺身而出的英雄凯旋！"},
                {"en": "The bitter resentment that had poisoned his thoughts for months suddenly dissolved, replaced by a profound, liberating surge of unconditional forgiveness.", "cn": "常年如毒蛇般噬咬盘踞在他心田深处数月之久的刻骨怨恨与偏狭戾气，在这一刻出人意料地如积雪遇沸汤般瞬间消融化解，取而代之的，是一股荡气回肠、彻底解放自我灵魂的无条件宽恕慈悲暖流！"},
                {"en": "Looking at the smiling faces of the villagers around the newly built library, he discovered that true happiness stems from what we give rather than what we acquire.", "cn": "深情凝望着全村老少乡亲环绕在崭新落成的爱心乡村图书馆四周那一双双喜极而泣、笑靥如花的质朴面庞，他蓦然间大彻大悟：生命真正崇高的极乐与尊严，从来永远取决于我们毫无保留地向人间奉献了多少，而绝非取决于我们自私巧取豪夺占有了几何！"},
                {"en": "Adversity had stripped away his superficial vanity, leaving behind a grounded, indestructible inner fortitude capable of weathering any future tempest.", "cn": "命运所降下的一场场惊涛骇浪般的残酷打击，虽然无情剥离打碎了他身上曾披着的一切虚浮虚荣外衣，但却在他灵魂深处，千锤百炼沉淀铸就了一副足以笑对余生任何狂风暴雨的坚不可摧的从容硬汉风骨！"},
                {"en": "He had set out on the expedition merely to win a glittering silver trophy, but returned home having conquered the far more formidable adversary: his own self-doubt.", "cn": "在当初收拾行囊出发远征之时，他本以为自己不过仅仅是为了角逐斩获那座在阳光下熠熠生辉的镀银冠军奖杯；然而在经历九死一生的洗礼归来时他才赫然顿悟——自己在这趟伟大的生命远征中所真正彻底降伏击碎的，正是那个曾长年自我怀疑、自怨自艾的懦弱内心自己！"},
                {"en": "She gently closed the diary, knowing that while painful historical chapters cannot be rewritten, the blank future pages are entirely hers to script with courage.", "cn": "她温柔而坚定地合上了那本泛黄的牛皮封面日记本，心底格外澄澈清明：尽管生命中那些被血泪浸透的沉痛既往篇章我们注定永远无法抹去重写，然而眼前那方一片纯白的崭新未来书卷，却完全由她自己手握正义与勇气的铁笔，尽情挥毫泼墨去重新书写！"},
                {"en": "The long, treacherous tunnel was finally behind them; bathing in the warm afternoon light, they looked into each other's eyes and knew they had forged a bond unbreakable.", "cn": "那条漫长幽暗、暗藏杀机塌方的深邃绝望隧道终于被他们彻底甩在了身后；沐浴在重见天日的漫天温暖午后阳光之下，两双满是泥泞与伤痕的眼眸深情凝望相视一笑，心照不宣地明白：在这一趟同生共死的淬炼中，他们已然结成了坚若磐石、生死相托的莫逆挚友盟约！"},
                {"en": "Kindness is not a fragile commodity that diminishes when shared; it is a radiant light that multiplies infinitely the moment it touches another human heart.", "cn": "人世间的善意从来绝不是一种在分给他人之后便会所剩无几的有限脆弱消耗品；它乃是一道神圣不灭的璀璨大爱之光——在它温情照亮并触碰温暖另一颗凡人冰封心房的同一瞬间，便会呈现几何级数般在天地之间迸发出无穷无尽的善意涟漪！"},
                {"en": "He stood a little taller, breathed a little deeper, and walked into the new dawn not as a victim of fate, but as the captain of his own soul.", "cn": "在重整行囊迈向新纪元的大道上，他把脊梁骨挺得更加笔直，胸膛深处深吸了一口破晓晨光，大踏步迈向灿烂朝阳——自此以后，他再也不是那个任由悲惨命运宰割摆布的哀怨受害者，而昂首蜕变成为了傲然掌舵自身不屈灵魂风浪的无畏大船长！"},
                {"en": "The scars carved across her hands were no longer badges of shameful suffering, but silver medals commemorating battles fought with fierce love and survival.", "cn": "烙印镌刻在她粗粝手掌虎口上的那一道道触目惊心的狰狞伤疤，自此以后再也不是什么见不得人的苦难羞耻烙印；而是一枚枚至高无上、神圣加冕的纯银荣誉勋章，庄严纪念着她为了心中所爱之人以血肉之躯浴血奋战并傲然生存下来的英勇功勋！"},
                {"en": "To forgive does not mean to forget or condone past injustice, but to cut the invisible chains binding our present peace to historical grievances.", "cn": "大度宽恕仇恨，从来绝不意味着我们要选择性失忆去姑息包庇历史的罪恶；而在于以大智慧亲手斩断那根将我们当下心灵的澄澈与安详死死套牢在历史怨念深渊中的无形毒锁链！"},
                {"en": "Sometimes the greatest victories in life are not heralded by triumphant trumpets, but whisper softly in the decision to get up and try again tomorrow.", "cn": "有时候，一个人生命中所赢得的最惊天动地的旷世伟大胜利，从来绝非是伴随着震耳欲聋的凯旋号角盛大加冕；而往往唯独体现在：在经历万劫不复的惨败之后，在一个寂静夜晚咬紧牙关，在心底平静而决绝地对自己轻声耳语：“站起来，明天且看我从头再战！”"},
                {"en": "Home is not merely a static geographical address defined by bricks and mortar, but the tender harbor where our authentic souls are welcomed unconditionally.", "cn": "“家”的最深层真谛，从来绝非仅仅只是指代某个由冰冷砖头瓦块与钢筋水泥所生硬砌筑的静态门牌号地址；它乃是天地间那一处无论你在红尘中受尽多少风霜雨雪与委屈、其大门永远为你毫无保留敞开、以无条件包容温情抚慰你真实疲惫灵魂的至高避风圣所！"},
                {"en": "Every trial encountered along our journey is an uninvited teacher, chisel in hand, patiently sculpting the masterpiece of our ultimate character.", "cn": "在漫漫人生征途上所迎面猝然遭遇的每一次苦难煎熬与命运刁难，本质上都是一位未曾受邀却冷酷如期而至的得道名师——他手握严苛的岁月刻刀，正在以令人心碎的剧痛为代价，耐心精雕细琢雕刻打磨着你人格终极走向成熟巅峰的不朽杰作！"},
                {"en": "Lift your head to greet the golden horizon; for within every persevering human spirit dwells a power mightier than any storm that ever raged across the sky.", "cn": "昂起你高傲的头颅、张开双臂去深情拥抱那片天际线上正在喷薄而出的灿烂金色朝霞吧——因为在每一个百折不挠、死守希望的觉醒凡人灵魂最深处，自始至终皆安详沉睡栖息着一股比世间任何曾在苍穹之上肆虐咆哮过的雷暴狂风，更加排山倒海、更加所向披靡的无穷无尽神圣伟力！"}
            ]
        },
        {
            "title": "Unit 8 · 传统美德与现代青年社会公德担当 · 扣好人生第一粒纽扣",
            "description": "探讨诚实守信、尊师重道、见义勇为与网络言论自律的高考热点立意。",
            "sentences": [
                {"en": "Integrity constitutes the unshakeable bedrock of personal character, commanding that promises made in private be honored as sacred covenants in public.", "cn": "诚实守信的美德乃是一个人立足天地间最不可动摇的人格定海神针，庄严要求一个人在暗室独处时所许下的每一句诺言，到了大庭广众阳光之下均必须如神圣盟约般毫不走样兑现！"},
                {"en": "Respecting educational mentors transcends formal classroom etiquette, embodying profound gratitude for the intellectual torch passed down through generations.", "cn": "尊师重道的中华传统美德，远远超越了课堂之上起立鞠躬问好的形式化礼仪规范，而是深刻承载着对师长呕心沥血将人类文明智识火炬代代相承的由衷高山仰止与深情反哺！"},
                {"en": "A courageous citizen who steps forward to shield a vulnerable stranger in distress embodies the highest nobility of civic virtue.", "cn": "在危难关头面对不法侵害敢于挺身而出、以血肉之躯为素不相识的弱势受难同胞遮风挡雨的见义勇为平民英雄，生动展现了现代文明社会公民道德境界的至高光芒！"},
                {"en": "Digital netizens must exercise disciplined linguistic restraint, resisting the toxic urge to spread unsubstantiated sensational rumors across cyberspace.", "cn": "身处网络赛博空间的当代青年网民，必须在键盘指尖时刻保持清醒自律的言论公德底线，坚决抵御在网络论坛里捕风捉影、肆意编造转发反智谣言与人身恶评的下流冲动！"},
                {"en": "Frugality is not an obsolete badge of poverty, but a mindful philosophy of respecting the finite ecological gifts bestowed by nature.", "cn": "克勤克俭从来绝不是寒酸贫困的陈腐遮羞布标签，而是一种由衷敬畏珍惜大自然所恩赐予全人类有限资源的绿色生态大智慧与崇高人生哲学！"},
                {"en": "Fulfilling filial duties involves far more than providing material financial sustenance; it requires spending patient, loving hours accompanying aging parents.", "cn": "百善孝为先的孝道真谛，从来绝非仅仅等同于按月向长辈银行账户打去几笔冷冰冰的养老钱；而唯独体现在抛开繁忙应酬、耐心坐在白发父母身旁促膝倾听唠家常的温情陪伴岁月深处！"},
                {"en": "Public transit etiquette mandates offering priority seats to pregnant mothers and frail elders without waiting for broadcast reminders.", "cn": "在公共交通车厢内恪守现代文明乘车公德，要求我们在看见怀抱婴儿的孕妇或步履蹒跚的白发老人迈入车门那一瞬间，无需任何车厢广播提醒，便能毫不犹豫微笑着主动起身让座！"},
                {"en": "Academic honesty prohibits cutting corners through plagiarism, safeguarding the sacred purity of scholarly discovery and examination fairness.", "cn": "对学术道德底线的庄严恪守，坚决严禁任何投机取巧的抄袭洗稿与考场作弊恶行，誓死捍卫科学求索的至纯神圣与国家选拔人才考场的绝对起跑线公平！"},
                {"en": "Volunteering selfless weekends to teach disadvantaged rural orphans expands youthful perspectives far beyond the narrow pursuit of personal wealth.", "cn": "利用难得的宝贵周末假期踊跃奔赴偏远山区为留守孤儿开展爱心义务支教，能够将青年的眼界格局从对一己私利的狭隘算计中彻底拔升，在兼济苍生中体悟大我境界！"},
                {"en": "True gentlemen and gentlewomen measure their inner worth not by outward luxury displays, but by their unassuming courtesy toward service personnel.", "cn": "一个有教养的现代青年衡量自身内在身价与风骨的试金石，绝非看其身着多么名贵的大牌奢品，而永远在于其在餐厅宾馆面对基层服务员保洁阿姨时、脱口而出的那声发自肺腑的温和道谢与由衷尊重！"},
                {"en": "Returning lost property intact to its rightful owner demonstrates personal moral integrity that money cannot buy.", "cn": "拾金不昧、物归原主将捡拾到的贵重遗失物品毫发无损送还失主，彰显了千金不换的人格浩然正气与崇高操守。"},
                {"en": "Sorting household garbage diligently every morning demonstrates environmental responsibility toward our shared urban ecosystem.", "cn": "每天清晨在垃圾投放桶前一丝不苟做好干湿垃圾细致分类，展现了一个现代公民对整座城市公共生态家园的体贴与爱护。"},
                {"en": "Respecting regional cultural and religious dietary taboos builds lasting bridges of national ethnic harmony.", "cn": "在日常交往中由衷尊重各兄弟民族的风俗习惯与饮食禁忌，是铸牢中华民族共同体意识、促进各民族休戚与共的坚实基石。"},
                {"en": "A promise is an anchor cast into the future; break it, and you drift aimlessly upon the ocean of broken trust.", "cn": "一句郑重的承诺恰似一枚锚定在未来岁月之中的万钧铁锚；一旦轻诺寡信弃之如敝履，你便注定将在丧失信誉的信任破产冰冷大洋中漫无目的随波逐流！"},
                {"en": "Youthful virtue is the moral compass that steers our civilization forward; let honesty, kindness, and courage guide every step you take.", "cn": "青年一代身上所流淌的传统美德与时代担当，是领航我们整部伟大文明破浪前行的崇高道德指南针；且让诚信、善良与担当，化作你漫漫人生路上永远明亮闪耀的指路明灯！"}
            ]
        },
        {
            "title": "Unit 9 · 读后续写实战突破：人与动物和谐相处与荒野救援行动",
            "description": "探讨荒野营救金雕、抚育濒危雪豹孤崽、人与自然生命相惜的高考续写热点命题。",
            "sentences": [
                {"en": "Trapped deep within the rusted jaws of an illegal steel poaching snare, the magnificent golden eagle flapped its broken wing frantically.", "cn": "被无情死死夹在盗猎分子布设的锈迹斑斑的非法钢丝捕兽夹钢齿深处的雄壮成年金雕，在绝望中剧烈拍打着那只鲜血淋漓、折断耷拉的巨型飞羽翅膀，发出凄厉悲鸣！"},
                {"en": "Crouching cautiously in the snow, the forest ranger spoke in soothing, low murmurs, holding out gloved hands to calm the panicked raptor.", "cn": "小心翼翼地俯身单膝跪倒在没膝的厚厚积雪之中，经验丰富的巡山护林员嘴里发出轻柔平缓的安抚低语，缓缓伸出厚实皮手套双手，竭尽全力安抚这只惊恐万状、如临大敌的空中猛禽。"},
                {"en": "With steady precision, he slipped the heavy bolt cutters beneath the coiled iron spring, snapped the trap open, and freed the bleeding talon.", "cn": "凭借大将般的沉稳冷静，护林员将沉重的工业液压断线钳悄悄探入紧绷生锈的弹簧发条核心深处，咔嚓一声强力剪断咬合夹，终于将猛禽那只被夹得血肉模糊的锋利鹰爪解救脱困！"},
                {"en": "The orphan snow leopard cub, shivering in the freezing Himalayan blizzard, pressed its tiny whiskered snout against the warm insulated parka.", "cn": "在喜马拉雅刺骨万分暴风雪中冻得瑟瑟发抖的幼年雪豹孤崽，本能地将那只长满绒毛胡须的稚嫩鼻头，紧紧依偎贴在巡护队员温暖厚实的羽绒服前胸怀抱里汲取生命的温度。"},
                {"en": "Week after week, the veterinary rehabilitation team dressed the raptor's festering wounds with antiseptic ointments, feeding it fresh meat patiently.", "cn": "在随后整整长达数周的分秒必争抢救中，野生动物救助站的兽医专家团队日夜不停用消毒药膏细致清洗包扎猛禽溃烂发炎的伤口，手把手极具耐心地喂下一条条新鲜精肉。"},
                {"en": "The eagle's piercing golden eyes, once clouded with feral mistrust and blinding pain, gradually softened with deep, instinctual gratitude.", "cn": "金雕那一双原本充斥着野性警惕与剧痛凶芒的金黄色锐利眼眸，在人类无微不至的大爱照料下，终于悄然卸下了防备，闪烁流露出通灵般的深情信任与依恋。"},
                {"en": "Standing upon the edge of the alpine cliff on release day, the ranger held the fully rehabilitated eagle aloft on his outstretched leather gauntlet.", "cn": "在终于迎来重返蓝天放飞大喜日子的巍峨高山悬崖边沿，巡山护林员昂首挺胸伸直佩戴着皮护臂的强壮手臂，将这只伤愈重生的森林霸主高高托举向万里长空！"},
                {"en": "With a sudden, explosive thrust of its magnificent wings that stirred the mountain air, the golden bird soared joyously into the azure heavens.", "cn": "伴随着两只遮天蔽日的巨型金羽双翼爆发出震撼山谷的大力振翅下压，这只天空王者发出惊天清啸，宛如一道黑色金色闪电般狂喜冲向苍茫无垠的蔚蓝苍穹深处！"},
                {"en": "It circled three times directly above the emotional ranger's head, uttering a piercing cry of farewell before vanishing beyond the snowy peaks.", "cn": "它在热泪盈眶的护林员头顶上方极其通灵地盘旋巡弋了整整三圈，发出一声响彻云霄的嘹亮告别长鸣，随后舒展双翼，潇洒消失在了巍峨万仞的雪山之巅！"},
                {"en": "Looking at the wide open sky where the eagle had vanished, tears of profound fulfillment blurred the weathered ranger's smiling eyes.", "cn": "呆呆凝望着那方金雕早已翱翔消失在九万里云海深处的浩瀚蓝天，一抹充满神圣成就感的滚烫泪水，悄然模糊了老护林员那双历经风霜却满溢着幸福笑容的慈祥双眸。"},
                {"en": "Wild creatures belong not behind artificial cages of human possession, but to the sovereign sanctuary of the untamed wilderness.", "cn": "大千世界中的野生动物从来绝不应被囚禁在人类满足自私占有欲的铁笼假山之中，而属于生生不息、辽阔无垠的壮美荒野大自然！"},
                {"en": "The gentle bond forged between species proves that compassion is a universal dialect spoken and understood across all boundaries of creation.", "cn": "跨越物种藩篱在人类与野生动物心田深处悄然铸就的深情纽带生动证明：人世间的善意大爱从来是一种超越生命形态界限、全宇宙有情众生皆能听懂的共有通用语！"},
                {"en": "To rescue a single endangered life does not alter the course of the cosmos, but for that one being, the whole universe is reborn.", "cn": "倾尽全力去弯腰拯救一只挣扎在生死边缘的弱小生灵，固然无法扭转整个浩瀚宇宙的物理运转轨迹；然而对于那个劫后余生的鲜活生命而言，整个宇宙自此都在其眼眸中重获新生！"},
                {"en": "May humankind forever remain the faithful steward of the wild, holding hands with our fellow creatures beneath the shared starry sky.", "cn": "祈愿全人类永远恪尽职守充当好大荒万物忠贞神圣的守护侍者，在同一片浩瀚璀璨星空之下，深情同与我们同舟共济的亿万飞禽走兽携手共存！"},
                {"en": "Let the wild call of eagles and the footsteps of leopards forever echo across our mountains, testament to a flourishing, living Earth.", "cn": "且让鹰击长空的清啸与雪豹漫步雪野的足迹永远回荡在我们的大好河山之间吧——这是生命繁茂不息、天地人合一的最壮美丰碑！"}
            ]
        },
        {
            "title": "Unit 10 · 读后续写实战突破：两代人温情和解与亲情救赎大团圆",
            "description": "探讨父子代际误解消除、重阳节老宅重聚、泛黄黑白旧相册背后的深沉父爱高考续写大轴题。",
            "sentences": [
                {"en": "The heavy silence that had hung like a stone between father and son for years was finally shattered by a box of forgotten yellowing letters.", "cn": "那片常年如巨石般死死悬隔在性格同样倔强的父子两人心头、令人窒息长达数年之久的冰冷沉默，终于在阁楼角落一只被遗忘的泛黄旧信封铁盒前被彻底粉碎融化！"},
                {"en": "Flipping open the moldy wooden trunk, the young man discovered that every newspaper clipping reporting his childhood awards had been taped with care.", "cn": "轻轻掀开布满蛛网灰尘的旧木箱盖子，年轻人才惊骇地发现：自己从小到大在各大竞赛中荣获的每一张哪怕最微不足道的巴掌大报纸简讯奖状剪报，都被老父亲用胶带工工整整悉心裱贴珍藏！"},
                {"en": "Underneath the yellowed documents lay a worn pair of leather work boots, heavily scuffed from decades of overtime shifts that funded his tuition.", "cn": "在厚厚一叠泛黄奖状的最底下，赫然静静躺着一双双鞋底早已磨穿开裂的旧劳保工装皮鞋——正是老父亲数十年如一日穿着它们起早贪黑在车间疯狂加班倒班，才用血汗钱硬生生托举供完了他的昂贵大学学费！"},
                {"en": "His throat seized with agonizing guilt as memories flooded back of cruel, ungrateful words hurled in youthful rebellious fury.", "cn": "如潮水般汹涌倒灌扑面而来的回忆，让他瞬间被撕心裂肺的悔恨自责死死扼住了咽喉——当年少不更事、青春期叛逆狂悖时对父亲口出狂言泼出的恶毒绝情狠话，如今化作一把把尖刀狠狠扎在心头！"},
                {"en": "Turning around, he saw his elderly father standing in the doorway, a stooped shadow framed by the setting sun, carrying a steaming bowl of noodles.", "cn": "蓦然猛一回首，他赫然望见白发苍苍的老父亲正静静伫立在夕阳余晖斜照的房门门槛旁，那是一道早已被岁月重担压得佝偻苍老的落寞剪影，粗粝颤抖的双手正小心翼翼端着一碗热气腾腾的手擀长寿面！"},
                {"en": "The steam rising from the bowl veiled the old man's watery eyes, but could not hide the trembling hesitation in his calloused hands.", "cn": "从热汤大碗里袅袅升腾而起的水蒸气热雾，虽然巧妙遮掩住了老父亲眼眶深处打转的晶莹泪水，但却无论如何也掩盖不住老人那双布满老茧的粗糙双手里所流露出的手足无措与战战兢兢。"},
                {"en": "Dad, I am sorry, the son choked out, dropping to his knees and burying his face into his father's weathered hands.", "cn": "“爸，对不起，儿子不孝！……”年轻人再也无法自持，失声痛哭跪倒在老父亲膝前，将泪流满面的滚烫脸颊，深深埋入父亲那双饱经沧桑如树皮般开裂的手心里！"},
                {"en": "The old father stroked his son's shaking shoulders, murmuring broken words of comfort that washed away years of estrangement instantly.", "cn": "老父亲颤巍巍伸出手臂，深情抚摸着儿子剧烈抽泣耸动的肩膀，嘴里颠三倒四喃喃自语着不成句子的抚慰轻语，在一瞬间便将积攒了数年之久的一切隔阂冰霜荡涤冲刷得无影无踪！"},
                {"en": "Sitting together at the creaky wooden table that evening, they shared the meal in quiet harmony, two hearts finally anchored in home.", "cn": "当晚父子俩在昏黄温暖的灯光下紧紧并肩围坐在吱呀作响的老木餐桌旁，有滋有味吃着那一碗热汤面，两颗曾在红尘中漂泊碰壁的心灵，终于在温暖的避风港湾深处找到了彼此归宿！"},
                {"en": "Love between generations does not require grand speeches; it lives silently in unspoken sacrifices, patient waiting, and forgiving embraces.", "cn": "在两代人之间血脉相连的人间至深父子大爱，从来绝不需要靠什么惊天地泣鬼神的华丽豪言壮语去粉饰包装；它自始至终安详栖息在默默无闻的含辛茹苦牺牲、数十年如一日的翘首期盼，以及历尽千帆后紧紧相拥的由衷宽恕深处！"},
                {"en": "The old wall clock ticked peacefully on the living room mantle, marking not the loss of time, but the timeless triumph of familial reconciliation.", "cn": "老旧客厅壁炉搁板上的老座钟发出安详恬静的滴答声，它所记录见证的，绝非生命的流逝消亡，而是血浓于水至真亲情在岁月大河中惊艳破冰和解的不朽凯歌！"},
                {"en": "Forgiveness is the golden key that unlocks the prison cell of past misunderstandings, liberating both the forgiver and the forgiven.", "cn": "由衷的宽恕是一柄至高无上的黄金钥匙，能够轻而易举打开深锁心房牢笼的旧日恩怨重锁，在同时间慈悲救赎解放了宽恕者与被宽恕者双方！"},
                {"en": "A father's back may bend under the weight of years, but the love in his heart remains an unyielding pillar shielding his child through storms.", "cn": "一位父亲原本挺拔伟岸的脊梁骨固然终将在残酷岁月的重压下慢慢弯曲佝偻；然而深埋在他心田深处的大爱，却永远宛如一根坚不可摧的擎天巨柱，终其一生为孩子遮挡着人世间的一切狂风恶浪！"},
                {"en": "Let filial gratitude be expressed while hands can still be held; do not wait until loving memories are all that remain of parents.", "cn": "孝道与感恩的真情流露，务必趁着父母至亲尚在人间、趁着那双温热的手尚能被我们紧紧牵住握牢之时尽早表达吧；千千万万切莫等到父母化作天上星辰、只剩追忆时才痛心疾首抱憾终生！"},
                {"en": "May every estranged wandering child find the courage to turn back, knocking upon that familiar wooden door where unconditional love waits patiently.", "cn": "祈愿天地间每一个在迷途与叛逆中流浪漂泊的疲惫孩子，皆能鼓起回家的无畏勇气，重新轻轻扣响那扇无比熟悉的古朴木门——在门后那方温暖明亮的橘黄灯火深处，无条件的深沉大爱正在岁月中耐心守候你的归来！"}
            ]
        }
    ]
    courses.append(build_course(gaokao_meta, gaokao_chapters))

    return courses

if __name__ == "__main__":
    print("测试考试分类 Part 3 (托福 + 高考)...")
    c = get_exam_part3_courses()
    print(f"成功构建课程数: {len(c)}")
