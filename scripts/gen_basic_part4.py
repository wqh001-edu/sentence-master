# -*- coding: utf-8 -*-
"""
基础学习分类生成器 Part 4:
7. basic-pronouns: 人称代词与物主代词实战 (10章 x 15句 = 150句)
8. basic-dialogues: 零基础核心生活对话破冰 (10章 x 15句 = 150句)
共 2 门课程，20 章，300 句。
"""

COURSE_BASIC_PRONOUNS = {
    "meta": {
        "id": "basic-pronouns",
        "title": "人称代词与物主代词实战",
        "category": "basic",
        "categoryName": "基础学习",
        "coverGradient": "from-cyan-500 to-blue-700",
        "icon": "👥",
        "description": "系统梳理主格、宾格、形容词性物主代词、名词性物主代词以及反身代词，彻底消除初学者在代词指代上的混乱。",
        "difficulty": "beginner",
        "tags": ["基础学习", "人称代词", "物主代词", "反身代词"]
    },
    "chapters": [
        {
            "title": "第1章：主格代词 (I, You, He, She, It, We, They) 施动主角",
            "description": "掌握主格人称代词充当主语的核心用法与人称配合。",
            "sentences": [
                {"en": "I dedicate two hours every single evening to studying classical English.", "cn": "我每天夜晚都雷打不动抽出整整两个小时，心无旁骛专心研读古典英语。"},
                {"en": "You possess the intellectual potential to accomplish truly extraordinary achievements.", "cn": "你自身分明蕴藏着足以名扬天下、干出一番真正惊天动地伟业的非凡智力潜能。"},
                {"en": "He leads the regional scientific research laboratory with vision and integrity.", "cn": "他以卓越高瞻远瞩的战略视野与光明磊落的人格操守，统领着这家区域顶尖重点科研实验室。"},
                {"en": "She graduated with top academic honors from the medical university faculty.", "cn": "她以全系名列前茅的顶尖学术优异成绩，光荣从著名医科大学临床医学院毕业。"},
                {"en": "It is an absolute honor and joy to collaborate with you.", "cn": "能够同阁下这般才华横溢之士通力协作携手共事，实在是在下一生莫大的荣幸与快事。"},
                {"en": "We must stand together united in the face of unprecedented crises.", "cn": "面对前所未有的世纪严峻危机大考，我们所有人必须精诚团结、同心协力共克时艰。"},
                {"en": "They crossed the stormy ocean to build a community of freedom.", "cn": "他们冒着九死一生的惊涛骇浪横渡狂暴大洋，只为在这片新大陆上开辟出一片自由的乐土。"},
                {"en": "I believe that relentless daily persistence will overcome any insurmountable obstacle.", "cn": "我始终坚信不疑：日复一日滴水穿石的坚持，终将彻底踏平人世间一切看似不可逾越的崇山险阻。"},
                {"en": "You can transform your career trajectory through continuous, disciplined daily education.", "cn": "只要通过持之以恒、高度自律的每日充电深造，你完全有能力彻底重塑蜕变你整个人生的职业轨迹。"},
                {"en": "He speaks with a calm, resonant authority that commands immediate respect.", "cn": "他开口说话时嗓音沉稳磁性、掷地有声，散发出一股令人肃然起敬、瞬间折服的天然威严。"},
                {"en": "She teaches the foundational principles of physics with brilliant, effortless clarity.", "cn": "她以行云流水般通透清晰的讲授方式，深入浅出向学子们传授着理论物理学的底层核心基石。"},
                {"en": "It rains heavily in this tropical coastal valley throughout late autumn.", "cn": "在这片依山傍海的热带沿海深山河谷地带，每逢深秋时节总是细雨霏霏连绵不绝。"},
                {"en": "We celebrate the glorious triumphs of our courageous ancestors with pride.", "cn": "我们满怀无比自豪与崇高敬意，由衷歌颂铭记我们英勇无畏的列祖先烈所立下的不朽功勋。"},
                {"en": "They founded an independent philanthropic institute to support impoverished rural scholars.", "cn": "他们联袂出资创办了一所完全独立的公益慈善基金研究院，专门大力资助扶持贫困山区的寒门学子。"},
                {"en": "Subject pronouns perform the grammatical action and direct the sentence focus.", "cn": "人称代词主格在句法上充当施动的主角，掌舵指引着整座句子核心意义的主谓聚焦点。"}
            ]
        },
        {
            "title": "第2章：宾格代词 (Me, You, Him, Her, It, Us, Them) 受动关怀",
            "description": "动词与介词后的宾格形式，区分 he vs him, she vs her, they vs them。",
            "sentences": [
                {"en": "The professor invited me to assist with his advanced research project.", "cn": "老教授亲自向我发出诚挚邀请，希望我能以核心科研助手的身份参与他的国家级重大攻关项目。"},
                {"en": "Our team will support you through every single step of this.", "cn": "在这场漫长跋涉的每一步征途当中，我们整支后勤专家团队都将毫无保留始终鼎力支持你。"},
                {"en": "We congratulated him warmly upon receiving the prestigious international science medal.", "cn": "当得知他众望所归斩获国际顶尖科学大奖金牌喜讯时，我们全场所有人向他致以了最热烈的祝贺。"},
                {"en": "The university awarded her a comprehensive four-year full tuition fellowship.", "cn": "名校评审委员会经过严格遴选，郑重决议授予她长达四年的全免学费高额全额奖学金。"},
                {"en": "Take this heavy wooden box and place it on the shelf.", "cn": "双手端起这个沉甸甸的木质工具箱，把它平平稳稳地摆放在靠墙书架的第二层隔板上。"},
                {"en": "The inspiring historical documentary moved us to tears of profound gratitude.", "cn": "这部发人深省、荡气回肠的历史纪录片巨作，深深触动了我们所有人，令大家忍不住潸然泪下。"},
                {"en": "Guide them with patience and love until they find their feet.", "cn": "用充足的耐心与深沉的关爱去指引那些年轻人，直到他们能够凭借自己的双脚在大地上自立自强。"},
                {"en": "Listen to me attentively before making an impulsive, irreversible career choice.", "cn": "在头脑发热做出任何冲动冒进、落子无悔的人生重大抉择之前，务必先坐下来洗耳恭听我的肺腑之言。"},
                {"en": "The kind doctor treated him with exceptional skill and deep compassion.", "cn": "那位仁心仁术的知名老主治医师，以精湛绝伦的医术与无微不至的深切悲悯悉心诊治了他。"},
                {"en": "We admire her for her unyielding integrity under severe political pressure.", "cn": "面对极其严酷的狂风暴雨与外部高压，她展现出宁折不弯的如铁操守，这令我们由衷肃然起敬。"},
                {"en": "Clean water is life; protect it and preserve it for posterity.", "cn": "甘洌纯净的水源正是滋养万物的生命之源；必须铁腕保护它保全它，留给我们的子子孙孙后世千秋。"},
                {"en": "Encourage us when we stumble, and rejoice with us in victory.", "cn": "当我们人生偶尔磕绊踉跄跌倒时请向我们投来鼓励的目光，而在我们凯旋摘得桂冠之际请与我们一同欢呼。"},
                {"en": "Teach them the golden principles of honesty, diligence, and public service.", "cn": "手把手向下一代传授光明磊落的诚实、勤勉耕耘的作风以及甘于为大众奉献服务的崇高金科玉律。"},
                {"en": "Object pronouns receive the direct or prepositional action of the verb.", "cn": "人称代词宾格在句法中承担着受动的客体角色，直接接纳及物动词或介词所传递施加的动作力量。"},
                {"en": "Mastering objective forms prevents confusing grammatical solecisms in sophisticated academic writing.", "cn": "精熟辨析人称代词宾格在各种语境下的严谨应用，能从根本上彻底杜绝高阶学术写作中低级语法语病的出现。"}
            ]
        },
        {
            "title": "第3章：形容词性物主代词 (My, Your, His, Her, Its, Our, Their)",
            "description": "修饰名词，表示所属关系，区分 its 与 it's，their 与 there。",
            "sentences": [
                {"en": "My supreme lifelong ambition is to master the art of English.", "cn": "我此生至高无上、矢志不渝的崇高志向，正是彻底精通纯正优雅的英语语言艺术。"},
                {"en": "Your diligent daily effort is already producing remarkable, tangible language improvements.", "cn": "你日复一日脚踏实地的勤勉汗水，当下已经在口语纯熟度上结出了令人赞叹的显著实质硕果。"},
                {"en": "His deep philosophical understanding of world history impressed the senior professors.", "cn": "他对人类波澜壮阔的世界通史所展现出的深邃哲学独到领悟，深深震撼了台下就座的资深老学者。"},
                {"en": "Her dedicated philanthropic foundation provides clean drinking water across remote villages.", "cn": "她名下倾力创立的公益慈善专项基金会，为成百上千个偏远闭塞的贫困山村打井通上了纯净自来水。"},
                {"en": "The ancient cathedral stands tall, its Gothic spire piercing the clouds.", "cn": "那座饱经风霜的古北大教堂巍然屹立，其哥特式的挺拔高耸尖塔宛如一柄利剑直刺苍穹（its 它的）。"},
                {"en": "Our collective family values emphasize honesty, continuous education, and mutual respect.", "cn": "我们全家人世代恪守传承的优良家风家训，始终高度强调诚实正直、终身治学与彼此由衷敬重。"},
                {"en": "Their pioneering software engineering company revolutionized international mobile cloud computing systems.", "cn": "他们合伙创办的那家具有开创颠覆意义的软件工程巨头，彻底革新了全球移动云计算系统的版图。"},
                {"en": "Wash your hands thoroughly with warm water before dining at table.", "cn": "在坐到餐桌旁开开心心享用丰盛佳肴之前，先用温热的水把自己的双手仔仔细细搓洗干净。"},
                {"en": "His private library holds over ten thousand rare classical leatherbound volumes.", "cn": "他私人府邸里的书房藏书馆，珍藏着超过一万余册极其罕见的传世羊皮精装典籍孤本。"},
                {"en": "Her musical talent was nurtured from early childhood by loving parents.", "cn": "她那一身惊艳四座的天籁音乐演奏才华，从咿呀学语的孩提幼年起就得到了慈爱双亲的悉心呵护与培植。"},
                {"en": "The bird flapped its colorful wings and soared into blue sky.", "cn": "大鸟奋力扑闪开它那一对色彩斑斓的硕大羽翼，径直冲向了万里无云的辽阔蔚蓝苍穹。"},
                {"en": "Our loyal neighborhood community gathered to celebrate the national autumn harvest.", "cn": "我们和睦相处、守望相助的街坊社区大家庭汇聚一堂，热热闹闹欢度一年一度的五谷丰登金秋盛典。"},
                {"en": "Their historic ancestral farmhouse was built entirely out of seasoned timber.", "cn": "他们家族祖祖辈辈生息繁衍的那座古朴农舍大院，通体完完全全是由上等的风干坚固木料榫卯构筑而成。"},
                {"en": "Possessive determiners modify nouns by specifying precise personal or institutional ownership.", "cn": "形容词性物主代词宛如一把标尺，通过前置修饰名词，极其清晰明了地界定出人际或实体的权属从属脉络。"},
                {"en": "Never confuse the possessive pronoun its with the contraction it is.", "cn": "铭记铁律：绝对切勿将物主代词 its（它的）与由 it is / it has 缩略缩写而成的 it's 混为一谈！"}
            ]
        },
        {
            "title": "第4章：名词性物主代词 (Mine, Yours, His, Hers, Ours, Theirs)",
            "description": "独立使用，相当于 形物代 + 名词，避免重复，如 This book is mine。",
            "sentences": [
                {"en": "This hardbound English grammar notebook is mine; yours is over there.", "cn": "这本封面素雅的精装英语语法笔记本是我自己的；而你本人的那本在书桌那一头搁着呢（yours）。"},
                {"en": "His research paper was published in June, while hers appeared today.", "cn": "他撰写的那篇学术论文早在今年六月份便已见刊，而她的大作直到今天才正式公开面世（hers）。"},
                {"en": "Their garden is spacious, but ours has far more blooming flowers.", "cn": "他们家院子里的那片花园虽然占地开阔，然而我们家的花园里盛开的花朵却远比他们多得多（ours）。"},
                {"en": "Is this misplaced leather briefcase his, or does it belong elsewhere?", "cn": "这只被不慎遗落在大堂会客沙发上的贵重真皮公文包究竟是他本人的，还是另有所属（his）？"},
                {"en": "The blue bicycle resting near the fence is entirely and proudly mine.", "cn": "倚靠在木栅栏旁边那辆保养得一尘不染的深蓝色山地自行车，完完全全、骄傲地独属于我（mine）！"},
                {"en": "Your dedication is truly inspiring, and ours matches your lofty standards.", "cn": "阁下长期以来所展现出的深沉奉献当真令人动容，而我们团队的干劲也定能完美匹配您的极高标准。"},
                {"en": "Their collaborative proposal won the award, though ours was equally strong.", "cn": "他们联合团队提交的方案最终拔得头筹荣获大奖，尽管我们团队的竞标方案在实力上同样旗鼓相当。"},
                {"en": "This seat beside the window is hers; she stepped away momentarily.", "cn": "靠窗户的这个视野绝佳的观景席位是她专属的；她刚刚只是暂时起身离席片刻，马上就回来。"},
                {"en": "My strategy has proven effective, and I hope his proves triumphant.", "cn": "事实证明我此前制定的战术路径成效斐然，我也由衷期待他那一套打法在实战中同样能够大获全胜。"},
                {"en": "Every nation has its proud heritage; this ancient legacy is ours.", "cn": "天下间每一个主权民族都拥有其自豪的传世文明；而这份厚重深邃的先贤文化遗产正是我们自己的！"},
                {"en": "Independent possessive pronouns stand completely alone without following any modified nouns.", "cn": "名词性物主代词在句法上具有完全独立的完备地位，后面绝对不可以再拖泥带水赘述任何被修饰的名词！"},
                {"en": "Deploy possessive pronouns to eliminate repetitive, clunky nouns from elegant prose.", "cn": "在高级书面行文中有机调遣名词性物主代词，能彻底剔除那些臃肿拙劣、反复出现的冗余名词，使文风洗练。"},
                {"en": "Notice that his and its serve as both determiners and pronouns.", "cn": "留心领悟：代词 his 在句法中身兼二职，既能充当形容词性物主代词修饰名词，又能独立充当名词性物主代词。"},
                {"en": "Clarity of ownership establishes distinct logical boundaries in formal legal arguments.", "cn": "在极其严谨严肃的正式司法法理辩论中，明晰物权所有权的归属界定能确立起泾渭分明的逻辑分水岭。"},
                {"en": "Mastery of possessives endows your bilingual expression with natural, native-level conciseness.", "cn": "精熟融会物主代词两大家族体系，能为你笔下与口中的双语表达注入纯正母语级别的洗练与高雅。"}
            ]
        },
        {
            "title": "第5章：反身代词 (Myself, Yourself, Himself, Herself, Itself, Ourselves)",
            "description": "动作施受同体（主宾同一人）与强调用法（亲自做某事）。",
            "sentences": [
                {"en": "I taught myself advanced computer programming algorithms through disciplined night study.", "cn": "在无数个万籁俱寂的漫漫长夜里，完完全全凭借高度自律的刻苦钻研，我自学精通了高阶算法（myself）。"},
                {"en": "Always believe in yourself, especially when self-doubt clouds your thinking.", "cn": "永远要笃定相信你自己的无限潜能，特别是当外界风凉话与内心的自我怀疑阴霾企图蒙蔽你的时候。"},
                {"en": "He prepared himself thoroughly for the high-stakes international diplomatic summit.", "cn": "为了从容应对这场关乎国家大局与重大利益的高端国际外交峰会，他从头至尾给自己做足了万全准备。"},
                {"en": "She challenged herself to run a full forty-two kilometer marathon.", "cn": "她主动向自己的体能与意志极限发起极限挑战，成功跑完了长达四十二点一九五公里的全程马拉松。"},
                {"en": "The complex digital system rebooted itself automatically after power was restored.", "cn": "当机房后备电力系统恢复供应的那一瞬间，整套精密的大型数字操作系统自动自行重启了（itself）。"},
                {"en": "We must remind ourselves daily that character matters far more than wealth.", "cn": "我们每一个人每天都应当反复警醒叩问自己：崇高的人格操守远比身外聚敛的物质财富重要千百倍。"},
                {"en": "Be true to yourselves, dear students, and pursue your genuine passions.", "cn": "亲爱的学子们，请永远真诚坦荡面对你们自己的内心本色，义无反顾去追寻你们真正热爱的事业！"},
                {"en": "They organized the entire humanitarian fundraising campaign by themselves without external aid.", "cn": "在完全没有借助外界任何机构外力援助的前提下，全凭他们自己这帮年轻人独立筹办了这场慈善义演。"},
                {"en": "The president himself delivered the historic commencement address to the graduates.", "cn": "大学校长本人亲自走上主讲台，为全体应届毕业学子深情发表了这篇载入史册的毕业典礼演讲（himself 强调）。"},
                {"en": "She designed and built this magnificent timber lakeside cabin all by herself.", "cn": "从绘制建筑图纸到亲手伐木打桩砌石，她完完全全凭一己之力建起了这座雄伟的湖畔小木屋。"},
                {"en": "Reflexive pronouns indicate that the subject and object are identical entities.", "cn": "反身代词的核心本源语法功能，在于昭示句子中发出动作的主语与承受动作力量的宾语完完全全是同一人。"},
                {"en": "Intensive pronouns emphasize a preceding noun or pronoun for dramatic rhetorical effect.", "cn": "而当反身代词充当强调代词使用时，紧随在被强调的名词之后，能爆发出极具力量感与戏剧张力的修辞气势。"},
                {"en": "Do not use a reflexive pronoun where a simple personal pronoun suffices.", "cn": "在不需要强调主宾同一或亲力亲为的寻常语境下，切忌滥用反身代词，普通人称代词宾格往往更加洗练得体。"},
                {"en": "Self-mastery is the supreme summit of human philosophical and spiritual evolution.", "cn": "征服驾驭自己内心的弱点、达成终极的自律与自省，是人类哲学修行与精神进化所能登临的至高绝顶。"},
                {"en": "Strengthen your inner resolve, for you alone captain your destiny.", "cn": "百炼成钢铸牢你内心深处不可动摇的坚毅魄力吧，因为唯有你自己才是掌舵你人生宿命航程的唯一船长！"}
            ]
        },
        {
            "title": "第6章：指示代词与替代代词 (This, That, These, Those, One, Ones)",
            "description": "近指与远指，避免名词重复的代词替代艺术。",
            "sentences": [
                {"en": "This is the exact turning point where history shifted course forever.", "cn": "这里正是当年波澜壮阔的历史巨轮彻底发生历史性转折的关键分水岭所在（this 指代近处/当下）。"},
                {"en": "That unforgettable evening in Paris will remain etched in memory eternally.", "cn": "那个在法国巴黎度过的令人魂牵梦萦、毕生难忘的浪漫夜晚，将永生永世铭刻在心底深处（that 远指）。"},
                {"en": "These fundamental grammar lessons are designed to build rock-solid language intuition.", "cn": "眼前大家正在研习的这些核心基础语法篇章，正是为了从底层为学子筑牢坚如磐石的纯正语感而量身定制。"},
                {"en": "Those ancient mountain fortresses protected the valley from foreign invasion centuries ago.", "cn": "那些在远方崇山峻岭间若隐若现的古老石头要塞城堡，在数百年以前曾御敌于国门之外保卫这方水土。"},
                {"en": "This method is far more efficient than the traditional one we used.", "cn": "我们眼前刚刚研发出的这种全新科学算法，其运算效率远远凌驾于过往我们所沿用的老旧方法之上（one 替代）。"},
                {"en": "Fresh organic strawberries are much sweeter than the imported ones in supermarkets.", "cn": "刚从本地果园采摘下来的新鲜有机草莓，尝起来明显比大型超市冷柜里陈列的进口草莓甜得多（ones 复数替代）。"},
                {"en": "That is the noble reason why we wake up early every day.", "cn": "正是出于那份崇高远大、感召人心的神圣使命，我们每天拂晓黎明时分才甘愿闻鸡起舞奋力打拼。"},
                {"en": "These hard-earned achievements belong to every single member of our dedicated team.", "cn": "这些历经千锤百炼辛勤汗水所换来的重大成果，毫无保留地属于我们整支攻坚团队里的每一个成员。"},
                {"en": "Those who dare to fail miserably often achieve the most magnificent victories.", "cn": "那些在人生竞技场上敢于冒着惨烈失败的巨大风险去大胆试错的人，往往最终能斩获最令人叹为观止的辉煌大捷。"},
                {"en": "Compare this innovative smartphone design with that of our main competitor.", "cn": "将我们这款集颠覆性创新于一身的旗舰智能手机架构，同主要竞争对手的产品设计进行详尽全面横向对比。"},
                {"en": "Demonstrative pronouns establish clear spatial, temporal, and psychological proximity in text.", "cn": "指示代词能在文本语篇中建立起极其经纬分明的物理空间远近、历史时间先后以及心理亲疏维度的距离感。"},
                {"en": "Substitute one for singular countable nouns and ones for plurals to avoid clutter.", "cn": "在行文中灵活调遣 one 替代单数可数名词、用 ones 替代复数名词，能彻底扫清文笔拖沓累赘的陈腐气息。"},
                {"en": "That of is the classic academic structure deployed for balanced cross-comparisons.", "cn": "在严谨的高等学术论文比对中，运用 that of 或 those of 结构，能让对比双方在天平两端保持严整工整对仗。"},
                {"en": "Mastering demonstratives sharpens your referential precision across complex narrative paragraphs.", "cn": "炉火纯青驾驭指示代词的指代艺术，能让你在驾驭长篇大论的繁复叙事段落时展现出手术刀般的严密逻辑。"},
                {"en": "Clarity of reference is the bedrock upon which persuasive rhetoric is erected.", "cn": "前后指代关系的严丝合缝、一清二楚，是铸就一切具有强大说服力与震撼力的高级修辞篇章的基石。"}
            ]
        },
        {
            "title": "第7章：不定代词全景解析 (All, Both, Each, Every, Either, Neither)",
            "description": "二者与多者全面区分，单复数谓语动词搭配精讲。",
            "sentences": [
                {"en": "All members of the international delegation voted unanimously to approve the treaty.", "cn": "出席全权大会的国际代表团全体在册成员，一致投下了赞成票，全票通过了这项历史性条约（all 全部）。"},
                {"en": "Both brother and sister graduated with top honors from medical school.", "cn": "这对志同道合、并肩求索的亲兄妹俩，当年双双以全优的傲人顶尖战绩从名牌医科大学荣誉毕业（both 两者都）。"},
                {"en": "Each student received an individualized study roadmap tailored to their needs.", "cn": "班上的每一位学子，都获得了一份根据其个人知识短板与长远诉求量身定制的个性化进阶路线图（each 各自单独）。"},
                {"en": "Every dedicated effort you make today builds a fortress of future capability.", "cn": "你在当下所付出的每一次全神贯注的踏实汗水，都在为筑造你未来不可撼动的核心实力添砖加瓦（every 每一个）。"},
                {"en": "Either of the two proposed technical routes will lead to success.", "cn": "摆在论证桌面上的这两条备选技术攻关路线，走哪一条都完全可行、都能达成最终的圆满成功（either 二选一）。"},
                {"en": "Neither of the conflicting corporate parties was willing to compromise on price.", "cn": "在剑拔弩张的商务谈判桌前，各执一词的两家跨国企业没有哪怕任何一方愿意在核心价格上做出妥协让步（neither 两者都不）。"},
                {"en": "All that glitters is not gold, so look beneath surface appearances.", "cn": "凡是表面闪闪发光的东西未必尽皆是真金，因此看待世间万物务必要擦亮双眼刺破皮相洞察本质。"},
                {"en": "Both methods yield mathematically rigorous results when applied under proper boundary conditions.", "cn": "只要严格在既定的边界约束条件规范下求解，这两种不同的演算方法都能导出数学上无懈可击的严密结论。"},
                {"en": "Each of the fifty historic states possesses its own sovereign legal jurisdiction.", "cn": "联邦版图内这整整五十个历史悠久的主权邦州，各自独立拥有其神圣不可侵犯的完备司法管辖权。"},
                {"en": "Neither candidate gained an absolute majority in the first round of voting.", "cn": "在首轮激烈的普选公开投票角逐中，两位主要竞争候选人均未能在得票率上斩获过半数的绝对多数席位。"},
                {"en": "Indefinite pronouns quantify entities without specifying exact individual names.", "cn": "不定代词以极其宏观概括的笔触，在无需指名道姓逐一列举的前提下，对数量范畴做出极其精准的界定。"},
                {"en": "Notice that neither and either take singular verbs in formal grammatical prose.", "cn": "在极度严肃严谨的书面正式语体中牢记规范：代词 either 与 neither 作主语时，谓语动词严格一律采用单数！"},
                {"en": "Distinguish between distributive each focusing on individuals, and collective every.", "cn": "深刻辨析幽微之别：分配代词 each 核心聚光灯打在形单影只的每一个个体身上，而 every 则着眼于全体总和。"},
                {"en": "Apply precision in quantification to avoid ambiguity in contractual commitments.", "cn": "在起草正式商业法律合同与条约承诺时，以毫无含糊歧义的严谨度选用不定代词，以杜绝一切法律漏洞。"},
                {"en": "Mastering dual pronouns equips your analytical writing with impeccable logical balance.", "cn": "精深掌握二元不定代词的精妙对仗法则，能为你笔下的学术分析论述注入无可挑剔的严密平衡逻辑美。"}
            ]
        },
        {
            "title": "第8章：复合不定代词 (Somebody, Anyone, Nothing, Everything)",
            "description": "some/any/no/every 构成的复合词，形容词后置修饰与单数一致性。",
            "sentences": [
                {"en": "Somebody left this valuable leather notebook on the wooden library table.", "cn": "有哪位不知名的热心读者，把这本贵重精装的真皮笔记本不慎遗忘在了图书馆的实木长桌上（somebody）。"},
                {"en": "Is there anyone available in the office who speaks fluent diplomatic French?", "cn": "在目前整间办公室里，是否碰巧有哪一位同仁能够极其流利纯熟地操着法语进行外交磋商（anyone 疑问句）？"},
                {"en": "Nobody can master a foreign language without investing sustained daily effort.", "cn": "天下间绝无任何一个人能在不倾注持之以恒的每日踏实苦练的前提下，凭空精通一门异国语言（nobody 否定）。"},
                {"en": "Everything happens for a profound reason in the vast tapestry of life.", "cn": "在浮生漫漫生命长河那波澜壮阔的锦缎画卷之中，每一桩降临在你身上的境遇都自有其深邃的深意（everything）。"},
                {"en": "There is something extraordinarily inspiring about witnessing human resilience.", "cn": "亲眼目睹人类在绝境逆境中所迸发出的那种坚韧不拔的如铁韧性，总能让人内心深处产生一种无与伦比的震撼（something）。"},
                {"en": "He did nothing to resolve the escalating conflict between the two departments.", "cn": "面对两个核心职能部门之间日益激化升级的摩擦纷争，他作为主管领导竟然作壁上观没有采取任何作为（nothing）。"},
                {"en": "Can anyone provide definitive evidence to substantiate this startling scientific claim?", "cn": "现场究竟有谁能够拿出确凿无疑、不可辩驳的过硬铁证，来实质性佐证这一惊世骇俗的科学假说呢？"},
                {"en": "Everyone in the grand auditorium rose to their feet in thunderous applause.", "cn": "宏大庄严的大礼堂内所有在场的全场听众无不自发肃然起立，爆发出经久不息、响彻云霄的雷鸣般掌声。"},
                {"en": "Notice that adjectives must follow compound indefinite pronouns as post-positive modifiers.", "cn": "牢牢记准核心必考语法点：当普通形容词修饰复合不定代词时，位置必须倒置、严格一律后置修饰（something new）！"},
                {"en": "Compound indefinite pronouns universally take singular verbs in standard English.", "cn": "在一切规范地道的正统英语表达中，由 body, one, thing 结尾的复合不定代词作主语时，谓语动词一律取单数！"},
                {"en": "Do not combine negative indefinite pronouns like nothing with another negative word.", "cn": "切记双重否定禁忌：严禁在同一个简单句结构中，将 nothing, nobody 等自带否定的代词与 not 叠床架屋混用！"},
                {"en": "Speak something worthwhile that uplifts the weary human spirits around you.", "cn": "开口讲出一些充满真知灼见、富有建设性的话语，去提振温暖身边那些在困顿中艰难跋涉的疲惫心灵。"},
                {"en": "From nothing, great empires and innovative industries were built through grit.", "cn": "从一无所有的蛮荒废墟起步，凭借着敢叫日月换新天的钢铁毅力，先驱们一手筑造起了宏伟帝国与现代产业。"},
                {"en": "Everything worthwhile requires an investment of time, patience, and sweat.", "cn": "人世间一切真正站得住脚、经得起时间考验的伟大之物，无不需要倾注大量的时间、耐性与滚烫的汗水。"},
                {"en": "Mastery of indefinite compounds endows your conversation with effortless, idiomatic rhythm.", "cn": "彻底精深融会复合不定代词的语流运用，能为你平时的跨文化交流谈吐注入如行云流水般的地道纯熟旋律。"}
            ]
        },
        {
            "title": "第9章：相互代词与代词一致性 (Each Other, One Another)",
            "description": "相互代词用法、代词数与性的一致、避免代词歧义与指代悬空。",
            "sentences": [
                {"en": "The two devoted brothers supported each other through decades of hardship.", "cn": "这对深情厚谊、患难与共的手足亲兄弟，在风雨如晦的数十年艰辛岁月里始终彼此扶持风雨同舟（each other）。"},
                {"en": "Scholars in this research collaborative challenge and elevate one another continuously.", "cn": "汇聚在这一多学科顶尖重点实验室里的海内外学者们，日复一日在学术切磋中彼此砥砺相互成就（one another）。"},
                {"en": "Husband and wife promised to love each other through sickness and health.", "cn": "相濡以沫的年轻夫妇庄严立下海枯石烂的结婚誓词：不论贫穷富贵、疾病康宁，彼此一生相守相伴矢志不渝。"},
                {"en": "Teammates must communicate openly with one another to ensure seamless tactical coordination.", "cn": "球场上并肩作战的战友伙伴之间必须保持毫无保留的坦诚沟通，方能确保整套战术配合行云流水天衣无缝。"},
                {"en": "Ensure that every pronoun agrees in number and gender with its antecedent.", "cn": "在行文运笔时以明察秋毫的严谨度核验：确保句中出现的每一个代词，都在单复数形态与性属上同先行词保持严格一致！"},
                {"en": "Avoid ambiguous pronoun references that confuse readers and obscure legal contracts.", "cn": "在法律合同与正式公文中坚决杜绝一切模棱两可、指代不明的含糊代词，以免误导读者并酿成司法纷争大祸。"},
                {"en": "Each student must bring their own certified reference textbook to the exam.", "cn": "在现代开明包容的通用语境中，采用无性别偏向的中性代词 their 修饰先行词 each，早已被国际权威广泛接纳。"},
                {"en": "They looked into each other's eyes and knew words were unnecessary.", "cn": "在那个扣人心弦的瞬间，他们深情凝视着彼此的双眸，刹那间便已彻底懂得：此时无声胜有声，言语已全属多余。"},
                {"en": "Citizens across diverse cultural backgrounds must learn to respect one another.", "cn": "来自五湖四海、秉持多元迥异文化信仰背景的各族广大公民，必须学会跨越分歧、由衷彼此尊重以和睦相处。"},
                {"en": "Traditional rules distinguish reciprocal each other for two from one another for many.", "cn": "在传统经典的规范语法界定中：相互代词 each other 严格专属指代两者之间，而 one another 则统摄三者以上。"},
                {"en": "Never leave a pronoun dangling without a clear, unequivocal antecedent noun.", "cn": "在下笔成文时绝对切忌抛出无头代词：决不可让一个孤立的代词在缺乏清晰明确先行词的前提下悬空漂浮！"},
                {"en": "Reciprocity is the foundational golden rule that sustains all civilized human societies.", "cn": "投桃报李、彼此敬重互惠的对等互利法则，是支撑维系整个人类文明社会大厦有序运转的至高黄金准则。"},
                {"en": "Love one another with genuine warmth, for life is too brief for discord.", "cn": "怀揣着发自肺腑的真诚暖意去深深彼此相爱吧，因为浮生如白驹过隙，根本经不起在勾心斗角纷争怨怼中虚掷。"},
                {"en": "Linguistic harmony mirrors social harmony in clear, elegant, and disciplined expression.", "cn": "语言文字各要素之间严丝合缝的和谐相得益彰，如实生动折射出一个文明社会在思想表达上所达到的自律境界。"},
                {"en": "Master the art of pronominal cohesion to craft seamless, persuasive rhetorical paragraphs.", "cn": "彻底精熟融会代词呼应与语篇衔接的无上艺术，去亲手锻造出如行云流水、令人拍案叫绝的极富说服力的经典华章！"}
            ]
        },
        {
            "title": "第10章：代词大圆满终章与精准指代大成",
            "description": "全代词谱系综合实战演练，彻底扫清指代盲区，登临语言掌控顶峰。",
            "sentences": [
                {"en": "I know who I am, what I believe, and how to achieve my goals.", "cn": "我心如明镜清清楚楚知道我自己是谁，深知我矢志不渝捍卫的信念是什么，更懂得该如何达成宏伟目标！"},
                {"en": "Pronouns replace nouns to bestow speed, elegance, and music upon prose.", "cn": "代词的横空出世，通过洗练巧妙替代冗长重复的名词，赋予了整座语言文字无与伦比的行进速度、优雅风骨与音乐韵律。"},
                {"en": "Treat others as you would wish them to treat your own family.", "cn": "己所不欲勿施于人，以你内心渴望别人对待你至亲挚爱家人的温情体贴标准，去真诚善待身边的每一个人。"},
                {"en": "Neither fear nor doubt shall sway us from our noble, historic path.", "cn": "前方的无论是任何惊涛骇浪的恐惧阻挠，还是暗流涌动的怀疑阴霾，都休想撼动我们勇毅前行的光荣正道！"},
                {"en": "She proved to herself that human willpower can conquer the highest peaks.", "cn": "她用自己一双长满老茧的双脚，向她自己的灵魂彻底证明：人类坚如钢铁的意志力足以踏平世间任何绝顶！"},
                {"en": "Those who walk with integrity illuminate the trail for generations behind them.", "cn": "那些一生行得正、坐得端、以光明磊落人格立世的人，必将为紧随其后千千万万的后世子孙照亮前行的大道。"},
                {"en": "Everything you have diligently learned on this platform belongs permanently to you.", "cn": "你在这座互动拼写学堂里通过每一滴自律汗水所踏实汲取到的学识功底，必将终生永恒、毫无保留地独属于你！"},
                {"en": "Language precision reflects moral clarity, disciplined thinking, and intellectual maturity.", "cn": "在字里行间所展现出的分毫不差的精准度，深刻映照着一个人的道德操守高度、严密逻辑思维与心智心智的成熟。"},
                {"en": "Replace ambiguity with laser-focused clarity in every sentence you speak and write.", "cn": "在未来你所说出的每一句话、亲笔写下的每一行文字之中，以如激光般聚焦的明澈彻底涤荡掉一切模糊含混。"},
                {"en": "Celebrate the extraordinary milestone of completing this core English pronoun curriculum!", "cn": "为你本人今天以超凡的毅力与卓越战绩，全面攻克完成这一套核心英语代词全部十大章节的辉煌胜利而自豪欢呼！"},
                {"en": "Your grammatical foundation in nouns, verbs, tenses, and pronouns is impregnable.", "cn": "你在核心名词、及物动词、系统时态以及庞大代词谱系上的语法童子功基石，此刻已坚不可摧固若金汤！"},
                {"en": "Step proudly forward into the world as an articulate master of language.", "cn": "满怀自信的大将风度昂首阔步迈入广阔的世界舞台吧，作为一名下笔有神、出口成章的真正卓越语言大师！"},
                {"en": "Command every sentence pattern with surgical accuracy and natural native-like eloquence.", "cn": "以如同手术刀般分毫不差的极高严谨度，以及浑然天成如母语般的流畅语感，游刃有余掌控一切复杂句型！"},
                {"en": "Your intellectual wings are spread wide; soar fearlessly toward your brightest dreams!", "cn": "你智慧的黄金双翼此刻已在大风之中奋力展翅舒张开来；毫无畏惧地展翅翱翔吧，直奔你最璀璨绚烂的梦想！"},
                {"en": "The universe of fluent, commanding bilingual expression is yours to illuminate forever!", "cn": "这片博大精深、地道纯正、气势恢宏的双语流利表达大千宇宙，注定由你亲手点亮光芒，万古长青！"}
            ]
        }
    ]
}

COURSE_BASIC_DIALOGUES = {
    "meta": {
        "id": "basic-dialogues",
        "title": "零基础核心生活对话破冰",
        "category": "basic",
        "categoryName": "基础学习",
        "coverGradient": "from-teal-400 to-indigo-600",
        "icon": "💬",
        "description": "专为零基础学员精选的日常生活核心交流高频句，涵盖初次见面、破冰问候、商场购物、餐厅点餐、问路求助与热情道别，开口即能交流。",
        "difficulty": "beginner",
        "tags": ["基础学习", "生活口语", "日常对话", "破冰表达"]
    },
    "chapters": [
        {
            "title": "第1章：初次相识与破冰问候",
            "description": "自我介绍、交换姓名、职业询问与一见如故寒暄。",
            "sentences": [
                {"en": "Hello, nice to meet you, my name is David Zhang from Shanghai.", "cn": "你好，非常高兴认识你，我叫大卫·张，来自美丽的中国上海。"},
                {"en": "It is an absolute pleasure to make your acquaintance this afternoon.", "cn": "今天下午能够有幸结识阁下，实在是在下莫大的荣幸与快事。"},
                {"en": "How do you do? Welcome warmly to our international design conference.", "cn": "您好！热烈欢迎您莅临出席我们本次举办的国际前沿设计大会。"},
                {"en": "What brings you to our vibrant coastal city this sunny week?", "cn": "在这个阳光明媚的美好周里，是什么把您吸引来到我们这座生机勃勃的海滨城市呢？"},
                {"en": "I work as a senior software architect specializing in cloud infrastructure.", "cn": "我在一家大型高科技机构担任资深软件架构师，专门攻坚云计算底层基础设施。"},
                {"en": "Where are you originally from, if I may inquire politely?", "cn": "如果允许我冒昧且有礼貌地问一句的话，请问阁下老家祖籍最初是来自何方呢？"},
                {"en": "I was born in Vancouver, but I grew up in London.", "cn": "我是在加拿大温哥华出生的，但是整个青少年求学时代我都是在英国伦敦长大的。"},
                {"en": "Have you had a chance to explore the historic city center?", "cn": "进城安顿下来之后，你是否已经抽出时间去逛了逛市中心的历史古城街区呢？"},
                {"en": "I am looking forward to our productive collaborative discussions during the summit.", "cn": "在接下来的峰会议程期间，我极其热切期盼着能与您展开成果丰硕的深入探讨。"},
                {"en": "Here is my business contact card with my direct mobile phone number.", "cn": "这是我个人的正式商务名片，上面印有我的直线办公电话与手机号码。"},
                {"en": "Please feel completely free to reach out whenever you visit our headquarters.", "cn": "任何时候您有机会顺道走访我们集团总部大厦，请务必完全放轻松同我联系。"},
                {"en": "Break the ice with a genuine smile and a firm handshake.", "cn": "带上一抹真诚亲切的微笑，伸出右手有力握手，在一瞬间轻松打破初见的拘谨坚冰。"},
                {"en": "Active listening is the secret ingredient that builds instant conversational rapport.", "cn": "全神贯注的主动倾听，是迅速拉近交谈双方心灵距离、建立深厚融洽信任的黄金秘诀。"},
                {"en": "Every great friendship begins with a simple, courteous hello on the road.", "cn": "人世间一切相濡以沫的伟大挚友情谊，无一不是发轫于旅途上一声朴素得体的亲切问候。"},
                {"en": "First impressions set a lasting positive foundation for future professional collaboration.", "cn": "优雅大方、不卑不亢的良好第一印象，能为未来长久互信的深度商务合作奠定坚实基石。"}
            ]
        },
        {
            "title": "第2章：日常闲聊与天气切入",
            "description": "谈论天气、周末计划、交通状况与轻松暖场技巧。",
            "sentences": [
                {"en": "The weather today is exceptionally lovely, sunny and pleasantly warm outside.", "cn": "今天户外的天气当真格外晴朗宜人，阳光和煦明媚，气温舒适如春。"},
                {"en": "It looks like we might get some heavy rain this afternoon.", "cn": "从天边滚滚而来的厚重云层来看，今天下午晚些时候十有八九会下起暴雨。"},
                {"en": "How was your weekend? Did you do anything exciting or fun?", "cn": "你刚才过去的这个周末过得怎么样？有没有出去干点什么好玩刺激的活动？"},
                {"en": "I spent a quiet, relaxing weekend reading books and hiking trails.", "cn": "我度过了一个极其清静从容的周末，安安静静读了几本好书，去近郊徒步吸了吸氧。"},
                {"en": "The morning rush hour highway traffic was unusually congested today.", "cn": "今天早高峰时段城市快速路上的车流拥堵状况，真可以说是罕见地水泄不通。"},
                {"en": "Did you happen to catch the championship football match on television?", "cn": "昨天晚上黄金档电视直播的那场激动人心的足球总决赛，你碰巧看了没有？"},
                {"en": "It feels so refreshing to step out into the cool evening breeze.", "cn": "在忙碌了一整天之后大步踏入户外凉爽宜人的晚风之中，感觉整个人神清气爽。"},
                {"en": "Are you planning any scenic family vacations for the upcoming holiday?", "cn": "面对即将到来的法定长假，你和家里人目前是否正筹划着去哪处名胜度假？"},
                {"en": "The temperature dropped dramatically overnight, so bundle up in warm coats.", "cn": "昨天一夜之间外面的气温断崖式猛降了好大一截，外出一定要多披上一件厚外套保暖。"},
                {"en": "A brief conversation about the weather creates smooth, effortless interpersonal rapport.", "cn": "从人畜无害的天气阴晴冷暖切入闲聊几句，能毫不费力地在陌生人之间迅速破冰。"},
                {"en": "Keep casual small talk lighthearted, optimistic, and welcoming in professional settings.", "cn": "在职场社交场合进行日常寒暄破冰时，时刻保持语气轻快幽默、充满阳光与热情好客。"},
                {"en": "Observing shared surroundings provides endless natural conversation starters without awkward pauses.", "cn": "善于敏锐捕捉两人所身处的共同周边环境，能为你源源不断提供用之不尽的天然聊天切入点。"},
                {"en": "Show authentic curiosity about what others enjoy doing in their leisure time.", "cn": "对他人在工作之余的闲暇闲情雅致与兴趣爱好，主动表达出你发自内心的由衷好奇。"},
                {"en": "Friendly casual dialogue turns ordinary working days into joyful, warm human experiences.", "cn": "亲切友善的日常闲谈交融，能将原本平淡枯燥的工作日点化成充满温情的人间美好体验。"},
                {"en": "Connect with genuine warmth, and watch professional doors swing open wide.", "cn": "以毫无矫饰的真诚暖意去结识拥抱他人，你将亲眼目睹无数通向成功的大门为你轰然敞开。"}
            ]
        },
        {
            "title": "第3章：餐厅点餐与就餐表达",
            "description": "预订座位、查看菜单、推荐特色菜、牛排熟度与结账买单。",
            "sentences": [
                {"en": "Good evening, we have a table reservation under the name of Miller.", "cn": "晚上好，我们之前通过电话预订好了一张四人餐桌，登记的名字是米勒。"},
                {"en": "Could you please bring us the dinner menu and wine list?", "cn": "请问侍者先生，能否麻烦您把今晚的晚间菜单以及酒水单为我们呈递上一份？"},
                {"en": "What house specialty dish would you personally recommend to first-time visitors?", "cn": "对于我们第一次慕名光顾的头回客而言，您个人最推荐店里的哪一道招牌特色大菜？"},
                {"en": "I would love to order the pan-seared sea bass with herbs.", "cn": "我想为我自己点一份主厨特制、配以新鲜香草佐味的香煎深海黑鲈鱼排。"},
                {"en": "How would you like your prime beef steak cooked this evening?", "cn": "尊贵的客人，请问您今晚点选的这客特级谷饲厚切牛排，希望煎到几分熟呢？"},
                {"en": "I prefer my steak cooked medium-rare, tender and juicy, please.", "cn": "请帮我煎到五分熟即可，肉质鲜嫩多汁、火候恰到好处，非常感谢。"},
                {"en": "Could we please have an extra bottle of chilled sparkling water?", "cn": "能不能麻烦服务生再为我们这一桌，加送一瓶冰镇的大瓶气泡矿泉水？"},
                {"en": "Is this delicious seafood soup prepared with fresh local seasonal ingredients?", "cn": "这道风味浓郁的海鲜靓汤，是否完完全全采用本地当天打捞的新鲜时令食材熬制的？"},
                {"en": "Please hold the spicy chili peppers, as I am sensitive to heat.", "cn": "后厨烹饪时请千万切记不要放辣椒，因为我个人体质对辛辣刺激极为敏感不耐受。"},
                {"en": "The presentation of this gourmet appetizer is absolutely stunning like art.", "cn": "这道精致开胃前菜的摆盘造型艺术，当真美轮美奂得如同一幅微缩的现代艺术画。"},
                {"en": "Everything tasted extraordinarily delicious; our compliments to the talented head chef.", "cn": "今晚端上来的每一道菜肴滋味都堪称惊艳绝伦；请务必代我们向才华横溢的行政总厨致敬！"},
                {"en": "Could we please have the dinner bill when you have moment?", "cn": "服务生，等您手头忙完稍有空闲的时候，能否把我们这一桌的结账账单送过来一下？"},
                {"en": "Can we pay by international credit card, or do you prefer cash?", "cn": "请问我们可以刷国际信用卡结账吗，还是说贵餐厅更倾向于收取现金结算？"},
                {"en": "Keep the change as a token of appreciation for your service.", "cn": "剩下的零钱不用找了，权当是对您今晚无微不至的卓越贴心服务的一点由衷谢意小费。"},
                {"en": "Dining out with polite fluency transforms an evening meal into celebration.", "cn": "在海外下馆子就餐时能够操着地道流利的英文从容点餐，能让一顿寻常便饭升华为愉悦庆典。"}
            ]
        },
        {
            "title": "第4章：商场购物与咨询砍价",
            "description": "寻找尺寸、试衣间试穿、询问打折促销、退税与收据。",
            "sentences": [
                {"en": "Excuse me, could you tell me where the women's clothing department is?", "cn": "打扰一下请问营业员，能否告知我一下高级女装精品专区具体设在哪一个楼层？"},
                {"en": "I am looking for a classic wool trench coat in medium size.", "cn": "我正在物色选购一件款式经典正统、中号尺码（M码）的纯羊毛双排扣风衣大衣。"},
                {"en": "Do you have this elegant blue silk dress in a larger size?", "cn": "这件剪裁优雅高贵的深蓝真丝连衣裙，请问库房里是否还留有更大一号的尺码？"},
                {"en": "Where is the customer fitting room so I can try this on?", "cn": "请问顾客试衣间设在哪个方位呢，我想亲自上身试穿一下这件外套的效果。"},
                {"en": "The fitting rooms are located right around the corner on the left.", "cn": "顾客专属更衣试衣间就在前面通道左转、正对着收银台的拐角处。"},
                {"en": "It fits me perfectly around the shoulders and feels exceptionally comfortable.", "cn": "这件衣服穿在我身上肩线裁剪严丝合缝极其合体，面料触感也分外舒适惬意。"},
                {"en": "Is this designer item eligible for the seasonal promotional discount today?", "cn": "请问这款国际大牌设计师款单品，今天是否能够享受换季促销的打折优惠折扣呢？"},
                {"en": "If I purchase two pairs of trousers, do I get a discount?", "cn": "如果我一次性打包购买两条不同颜色的休闲西裤，结账时能否给予相应的额外折扣？"},
                {"en": "Do you provide tax refund services for international overseas tourist travelers?", "cn": "对于持短期旅游签证入境的海外国际观光客，请问贵百货大楼是否提供现场退税服务？"},
                {"en": "Please gift-wrap this delicate crystal vase carefully in a decorative box.", "cn": "麻烦您用精美的礼品包装纸与缎带，把这只易碎的水晶花瓶妥善包装进礼品盒内。"},
                {"en": "Keep your formal purchase receipt in case you need an exchange later.", "cn": "把电脑打印的正式购物小票凭据妥善留存好，万一日后需要办理退换货还需凭票审核。"},
                {"en": "Can I return this unopened merchandise within thirty days for refund?", "cn": "在商品完全未经拆封、完好无损的前提下，请问三十天之内是否可以无条件凭票退款？"},
                {"en": "I will take both of these handcrafted leather shoes, thank you.", "cn": "这两双做工考究的纯手工定制皮鞋我全都买下了，麻烦您帮我打包开票，谢谢。"},
                {"en": "Shopping with confident English allows you to express your exact personal tastes.", "cn": "在海外名店购物时能够自信从容用英语交流，能让你毫不走样地精准挑选心仪好物。"},
                {"en": "Polite negotiation often yields unexpected promotional discounts and delightful customer service.", "cn": "彬彬有礼、有理有节的得体问询砍价，往往总能为你意外解锁意想不到的折扣与超凡待遇。"}
            ]
        },
        {
            "title": "第5章：街头问路与交通指南",
            "description": "迷路求助、询问距离路线、左转右转直行、标志性建筑。",
            "sentences": [
                {"en": "Pardon me, sir, I seem to have lost my way downtown.", "cn": "先生实在不好意思打扰一下，我初来乍到，在市中心这片街区似乎不小心迷失方向了。"},
                {"en": "Could you kindly direct me toward the national historical museum, please?", "cn": "能否麻烦您行个方便，为我指引一下前往国家历史文化博物馆的大体行进方向？"},
                {"en": "Walk straight ahead for three blocks, and then turn left at corner.", "cn": "沿着这条马路一直笔直往前走过三个街区，然后在路口的大银行拐角处向左转弯。"},
                {"en": "Is the ancient cathedral within easy walking distance from this square?", "cn": "那座宏伟的千年大教堂，从我们脚下所站的这处中心广场步行走过去距离远不远？"},
                {"en": "It will take you approximately fifteen minutes on foot to reach it.", "cn": "按照正常的成人步行步速走过去，大概只需要耗费你一刻钟左右的脚程时间。"},
                {"en": "Look out for a towering neoclassical marble building with giant stone columns.", "cn": "留意观察前面：你会看到一座通体由洁白大理石筑就、耸立着巨型罗马柱的新古典主义大厦。"},
                {"en": "You cannot miss it; it sits directly opposite the central post office.", "cn": "你绝对不可能错过的；它正好端端正正坐落在中央邮政总局大楼的正对面。"},
                {"en": "Should I take the local public bus or hail a street taxi?", "cn": "您看我是去路边坐公共汽车过去比较方便，还是直接扬招出租车过去更快一些？"},
                {"en": "Bus route number forty-two drops you off right in front of gate.", "cn": "乘坐四十二路市内公交车，下车站点正好就在博物馆的正门检票口大台阶前。"},
                {"en": "How much is the standard bus fare from here to the harbor?", "cn": "从我们目前所在的上车站点一直坐到海湾客运码头，标准单程公交票价是多少？"},
                {"en": "Cross the wide pedestrian intersection safely when the green walking light signals.", "cn": "耐心等候人行横道绿灯指示图标亮起之后，再安安全全、大步迈过宽阔的十字路口。"},
                {"en": "Thank you ever so much for your warm kindness and helpful directions.", "cn": "对于您如此热情周到、指点迷津的耐心引路指导，在下真是不胜感激涕零之至！"},
                {"en": "Do not hesitate to ask local residents when navigating an unfamiliar metropolis.", "cn": "独自穿行在一座完全陌生异域的大都会街头时，切忌硬撑盲目瞎转，大胆向当地市民问路。"},
                {"en": "Clear landmarks like clock towers, statues, and bridges guide travelers securely.", "cn": "大钟楼、城市雕像以及跨河大桥等醒目的地标建筑，是异乡赶路人永不迷航的最佳罗盘。"},
                {"en": "Travel opens the mind, and gracious communication bridges every cultural distance.", "cn": "远足旅行能彻底打开一个人的心胸格局，而文雅得体的语言沟通能消弭一切文化隔阂。"}
            ]
        },
        {
            "title": "第6章：酒店入住与客房服务",
            "description": "办理入住、房卡钥匙、前台报修、退房时间与行李寄存。",
            "sentences": [
                {"en": "Good afternoon, I would like to check in for my three-night stay.", "cn": "下午好，我们此前在网上预订了三晚的住宿，现在想办理一下入住登记手续。"},
                {"en": "Here is my valid international passport and my digital booking confirmation code.", "cn": "这是我本人的有效国际护照原件，以及手机上收到的数字化预订确认编码。"},
                {"en": "We have assigned you a spacious deluxe room on the tenth floor.", "cn": "我们特意为您排定安排了位于十层高楼层、视野极其开阔的豪华观景行政客房。"},
                {"en": "Your room has a breathtaking panoramic view overlooking the shimmering blue bay.", "cn": "您房间里巨大的全景落地窗外，正对着波光粼粼、千帆竞渡的蔚蓝海湾绝美景致。"},
                {"en": "Here are your electronic keycards; breakfast is served from seven to ten.", "cn": "这是为您配发的两张智能感应房卡；清晨的自助早餐时间为每天早晨七点至十点整。"},
                {"en": "Could you please inform me where the hotel elevator banks are located?", "cn": "能否麻烦服务员告知我一下，通往高层客房的电梯间大厅具体设在哪一侧？"},
                {"en": "The high-speed guest elevators are just past the grand marble fountain.", "cn": "高速客用电梯间就在前台大堂那座宏伟的大理石水景喷泉正后方，直走即是。"},
                {"en": "What is the wireless internet network name and password for hotel guests?", "cn": "请问供入住宾客免费使用的客房高速无线无线网络的名称与连接密码是什么？"},
                {"en": "Could we please request two extra fluffy pillows and clean bath towels?", "cn": "能否麻烦客房楼层服务中心，再为我们客房加送两个蓬松柔软的枕头与干净毛巾？"},
                {"en": "The air conditioning unit in room ten-twelve seems to be malfunctioning.", "cn": "我们入住的十层一零一二号客房内部的中央空调温控面板，目前似乎运转不正常。"},
                {"en": "We will dispatch an experienced maintenance engineer to your room immediately, sir.", "cn": "尊贵的先生实在抱歉，我们马上指派值班的高级机电维修技师即刻上门为您检修排障。"},
                {"en": "What is the standard checkout time tomorrow morning: eleven or twelve noon?", "cn": "请问贵酒店明天正常退房的截止时间是上午十一点整，还是中午十二点整呢？"},
                {"en": "Can we store our heavy suitcases securely with the concierge after checkout?", "cn": "在我们办理完退房手续之后，能否将这几件沉重的大行李箱暂时免费寄存礼宾部？"},
                {"en": "Thank you for making our holiday stay so exceptionally comfortable and memorable.", "cn": "非常感谢贵酒店全休同仁的悉心照料，让我们这次全家度假过得如此舒心惬意与难忘！"},
                {"en": "Professional hospitality makes weary international travelers feel welcomed, cherished, and completely at home.", "cn": "专业典雅、无微不至的星级酒店款待之道，能让风尘仆仆的远洋旅人瞬间感受到宾至如归的温暖。"}
            ]
        },
        {
            "title": "第7章：机场出行与登机出入境",
            "description": "托运行李、换登机牌、安检海关、登机口寻找与转机。",
            "sentences": [
                {"en": "Which airline check-in counter handles international departures to London Heathrow?", "cn": "请问前往英国伦敦希思罗国际机场的跨国直飞航班，是在哪一个值机岛柜台办理？"},
                {"en": "I would like to check in two pieces of luggage and keep this carry-on.", "cn": "我有两件大行李箱需要办理随机托运，这一件小登机拉杆箱我随身携带登机。"},
                {"en": "Place your heavy suitcase upright on the digital luggage weighing scale, please.", "cn": "请把您的大行李箱端端正正竖直放置在电子称重传送带上，配合我们称重核验。"},
                {"en": "Would you prefer a comfortable window seat or a convenient aisle seat?", "cn": "在机舱座位挑选中，您个人更倾向于选一个靠窗的座位，还是更方便出入的过道座？"},
                {"en": "I would love a window seat over the wing if one is available.", "cn": "如果机舱机位尚有富余的话，我个人非常希望能挑一个靠窗、视野开阔的好位子。"},
                {"en": "Here is your official boarding pass; your flight boards at gate twenty-six.", "cn": "这是打印出来的正式登机牌；您的航班将于四十分钟后在二十六号登机口准时登机。"},
                {"en": "Proceed through security screening and border customs clearance without unnecessary delay.", "cn": "拿到登机牌后，请抓紧时间依次通过民航旅客安全检查与出境边防海关检查。"},
                {"en": "Please remove your laptop computer and liquids from your carry-on backpack.", "cn": "请将随身双肩背包里携带的笔记本电脑以及旅行装液体单品，提前取出放入托盘。"},
                {"en": "Walk through the metal detector frame one by one when directed by officers.", "cn": "在值班安检警员的引导指引下，请大家保持间距，一个接一个有序穿过安检安全门。"},
                {"en": "What is the primary purpose of your international visit to our country?", "cn": "在入境审查柜台前，移民官员严肃核验道：“请问您本次入境我国的最主要目的是什么？”"},
                {"en": "I am traveling exclusively for tourism, sightseeing, and academic cultural study.", "cn": "我本次完全是持旅游观光签证入境，纯粹是为了实地游览名胜古迹以及考察学术文化。"},
                {"en": "How long do you intend to reside within the sovereign territory of nation?", "cn": "“在整个入境停留期间，您个人打算在我国境内累计逗留游历多长一段时间？”"},
                {"en": "I will be staying for fourteen days before returning on my booked round-trip flight.", "cn": "我只打算停留整整十四天，手头已经出好了两周后准时返航回国的往返往返机票原件。"},
                {"en": "Stamp your passport, collect your baggage, and step out into an exciting adventure.", "cn": "海关关员核验盖戳放行，从行李转盘提取好随身箱包，跨步踏入异国他乡那充满无限可能的奇妙大冒险！"},
                {"en": "Confident airport communication ensures smooth transitions across international borders and cultures.", "cn": "在世界各大国际机场之间能够沉着自信自如交流，能确保你潇洒畅通无阻游弋穿梭于五洲四海。"}
            ]
        },
        {
            "title": "第8章：看病就医与药房问药",
            "description": "描述症状、预约挂号、医生问诊、药房买药与医嘱遵从。",
            "sentences": [
                {"en": "I would like to schedule an urgent medical consultation with general practitioner.", "cn": "我目前身体突发不适，想紧急挂号预约一位经验丰富的全科主治医师进行门诊诊治。"},
                {"en": "What acute physical symptoms have you been experiencing over past forty-eight hours?", "cn": "接诊医生和蔼地问询道：“在过去四十八小时里，你身体具体出现了哪些急性不适症状？”"},
                {"en": "I have been suffering from a splitting headache and a fever of thirty-eight degrees.", "cn": "我这两天一直头痛欲裂如同针扎一般，体温计实测反复低烧烧到三十八度有余。"},
                {"en": "My throat feels terribly scratchy, sore, and I have a dry, hacking cough.", "cn": "我的嗓子干痒难耐吞咽剧痛，胸腔里还总是不受控制地伴随着阵阵刺激性的干咳。"},
                {"en": "Let me listen to your lungs with this cold metal stethoscope; breathe deeply.", "cn": "请坐直身体，让我用听诊器仔细听一听你的心肺呼吸音；深吸一口气，然后慢慢吐气。"},
                {"en": "Open your mouth wide and say ah so I can inspect your tonsils.", "cn": "把嘴巴尽量张大，嗓子里大声发出“啊——”的声音，让我用压舌板观察一下扁桃体。"},
                {"en": "Your throat is inflamed, indicating a viral upper respiratory tract seasonal infection.", "cn": "你的咽喉充血红肿明显，这表明你目前患上的是典型的上呼吸道季节性病毒性感冒。"},
                {"en": "Drink plenty of warm liquids and get bed rest for three full days.", "cn": "医嘱叮嘱：必须多喝温开水，在接下来的三天时间里放下所有繁杂工作卧床静养。"},
                {"en": "Here is an official written prescription for throat lozenges and fever-reducing medication.", "cn": "这是我为你亲手开具的正式处方笺，凭此单去药房配齐润喉含片以及退烧镇痛止咳药。"},
                {"en": "Take one white pill twice a day after meals with full glass water.", "cn": "药剂师叮嘱道：这种白色小药片每天早晚各服用一次，饭后半小时就着一大杯温水送服。"},
                {"en": "Do these prescribed antibiotics have any drowsy or nauseating side effects on patients?", "cn": "请问医生开出的这些抗生素消炎药，服用后是否会引发嗜睡困倦或者肠胃恶心反胃？"},
                {"en": "Avoid driving heavy machinery while taking this medication as it induces slight drowsiness.", "cn": "由于该药物代谢期间可能会诱发轻微嗜睡，服药期间请绝对严禁从事长途驾驶或高空作业。"},
                {"en": "If your high fever persists beyond three days, return to clinic immediately.", "cn": "倘若三天之后高烧依然顽固不退，务必不要硬拖，第一时间火速重返门诊复诊化验。"},
                {"en": "Clear communication regarding bodily symptoms ensures accurate diagnosis and speedy, full recovery.", "cn": "向主治医生精准详尽交代自身病痛细微症状，是确保医生下准诊断、促成身体迅速康复的关键所在。"},
                {"en": "Cherish your health above all earthly possessions, for vitality is life's crown.", "cn": "把身心健康置于世间一切名利财富之上倍加珍视，因为充沛的生机活力才是生命最耀眼的王冠。"}
            ]
        },
        {
            "title": "第9章：紧急求助与应急排障",
            "description": "报警呼救、火警医疗急救、遗失钱包证件、寻求中国领事馆协助。",
            "sentences": [
                {"en": "Help! Somebody call an emergency ambulance right now; a pedestrian has collapsed!", "cn": "快来人救命啊！赶快谁帮忙拨打一下急救中心的救护车电话，人行道上有一位路人昏厥倒地了！"},
                {"en": "What is the emergency telephone number for police, fire, and medical rescue?", "cn": "在这座异国大都会里，遭遇突发险情时呼叫巡警、消防救援与医疗急救的统一紧急热线是几号？"},
                {"en": "Please stay calm and clearly state your exact physical geographic street location.", "cn": "接警调度员沉稳指引道：“请您务必保持冷静，清晰准确报出您当前所处的具体街道门牌坐标。”"},
                {"en": "We are located at the corner of Fifth Avenue and Pine Street downtown.", "cn": "我们目前正伫立在市中心商业区第五大道与松树街相交的那个大十字路口正中央！"},
                {"en": "Emergency first responders and paramedics are being dispatched to your scene immediately.", "cn": "请在原地坚守做好防护，全副武装的警车与专业院前急救医疗人员正鸣笛火速赶赴现场！"},
                {"en": "I need to report a lost leather wallet containing credit cards and passport.", "cn": "我急需向当地警务分局报案登记：我随身装满各家银行信用卡与护照的皮夹刚刚不慎失窃了。"},
                {"en": "Where is the nearest Chinese embassy or consulate general in this foreign metropolis?", "cn": "在这座繁华庞大的异国大都市里，距离最近的中国驻当地大使馆或总领事馆具体设在何处？"},
                {"en": "The consular protection hotline provides twenty-four-hour emergency assistance to overseas citizens.", "cn": "外交部全球领事保护与服务应急呼叫中心热线，一年三百六十五天二十四小时为海外赤子保驾护航。"},
                {"en": "Keep a physical photocopy of your passport securely separated from your original document.", "cn": "出门在外铭记防身技巧：将护照首页的纸质复印件，同护照原件分门别类放在两个绝不相连的包里。"},
                {"en": "Cancel all lost credit cards immediately by calling the bank's international hotline.", "cn": "一旦发生银行卡遗失失窃，第一时间分秒不差拨打发卡银行的海外紧急挂失冻结专属通道。"},
                {"en": "In any sudden crisis, taking three deep breaths restores rational, decisive action.", "cn": "每当大难临头突遭惊涛骇浪的突发危机时，连续做三次深沉的腹式深呼吸，能瞬间重拾理性的决断力。"},
                {"en": "Never panic in difficult moments, for panic paralyzes the mind's problem-solving faculties.", "cn": "在危如累卵的险恶关头绝对切忌手忙脚乱惊慌失措，因为慌乱会彻底瘫痪大脑调动智慧的机能。"},
                {"en": "Know your basic legal rights and request an accredited diplomatic interpreter if arrested.", "cn": "在异国他乡时刻熟谙自身基本人权边界，在必要时有权依法严正要求官方指派持证专业翻译到场。"},
                {"en": "Courage, presence of mind, and fluent communication will guide you through any storm.", "cn": "过人的胆魄、临危不乱的强大定力以及清晰纯熟的语言自救沟通，必将护佑你冲破一切惊涛骇浪化险为夷。"},
                {"en": "A prepared mind turns perilous emergencies into victorious testimonies of resilience and resourcefulness.", "cn": "一个时刻未雨绸缪做足万全预案的心灵，能将险象环生的生死险境扭转为见证顽强生命力与机敏智慧的凯歌！"}
            ]
        },
        {
            "title": "第10章：深情道别与友谊长存",
            "description": "道别离、互留联系方式、相约再见、致谢与开启崭新征程。",
            "sentences": [
                {"en": "It has been an absolute privilege and joy spending this time with you.", "cn": "在这些弥足珍贵的难忘时光里能够与阁下促膝长谈朝夕相伴，实在是在下此生莫大的荣幸与快事。"},
                {"en": "Thank you from the bottom of my heart for your warm, gracious hospitality.", "cn": "对于阁下及全家在此期间所给予我无微不至、温暖体贴的盛情款待，在下谨致以最深沉的由衷谢忱。"},
                {"en": "Let us definitely stay in close touch through electronic mail and video calls.", "cn": "在未来的漫长岁月里，我们之间务必要通过电子邮件与跨洋视频连线始终保持最紧密的联系。"},
                {"en": "Here is my updated personal WeChat and WhatsApp contact for international messaging.", "cn": "这是我个人最新的微信与海外即时通讯社交账号信息，方便我们随时随地跨越大洋无障碍畅聊。"},
                {"en": "Whenever your future travels bring you to China, our home is open.", "cn": "日后无论何时因公因私阁下的足迹踏足中国大地，我们全家的大门永远为您热情敞开无上欢迎！"},
                {"en": "Safe travels, fair winds, and smooth sailing on your long flight back home.", "cn": "衷心祝愿您返航回国的跨洋漫漫长途航程一路顺风、平安顺遂、起落安妥、起降平稳！"},
                {"en": "May success, good health, and joyful laughter accompany you wherever you travel.", "cn": "愿长盛不衰的功业成功、身心康泰与欢畅的欢声笑语，如影相随时刻伴随在您所走过的每一个足迹身旁。"},
                {"en": "True friendship forged through mutual respect transcends all geographic borders and oceans.", "cn": "建立在彼此由衷由衷尊重与灵魂共鸣之上的真正至交挚友情谊，必将跨越一切地理疆界与千山万水。"},
                {"en": "I will cherish these wonderful golden memories of our collaboration for decades.", "cn": "我们在这段岁月里通力协作所结下的丰硕成果与金色美好回忆，我将在未来的数十年岁月里深情珍藏。"},
                {"en": "Saying goodbye is never easy, but every parting anticipates a joyous reunion.", "cn": "每一次依依惜别总是让人心头涌上万般不舍，然而每一次挥手告别，都在深情期许着下一次更美好的重逢。"},
                {"en": "Until we meet again, my dearest friend, take exceptionally good care of yourself.", "cn": "青山不改绿水长流，在我俩下一次再度执手相逢之前，我最珍贵的知己好友，请务必千万多多保重身体！"},
                {"en": "You have thoroughly mastered all eighty chapters of this comprehensive basic English series!", "cn": "你已经以超凡的自律恒心与滴水穿石的坚韧，彻彻底底攻克征服了整套基础英语全部八十个核心实战章节！"},
                {"en": "You now possess the foundational linguistic power to communicate with the entire world.", "cn": "你手中此刻已经实打实牢牢握住了与整个辽阔大千世界毫无障碍从容对话、纵横驰骋的坚实语言伟力！"},
                {"en": "Speak without hesitation, write without fear, and pursue your dreams with boldness.", "cn": "在人生的广阔竞技场上开口表达时绝不再有半点结巴犹疑，提笔下笔时毫无惧色，放开手脚大胆追寻梦想！"},
                {"en": "Go forward proudly into the boundless horizons of advanced English fluency and excellence!", "cn": "昂首挺胸、自信自豪地大步迈向更高阶、更广袤无垠的纯熟地道英语流利表达与卓越造诣的新天地吧！"}
            ]
        }
    ]
}

print("COURSE_BASIC_PRONOUNS, DIALOGUES ready")
