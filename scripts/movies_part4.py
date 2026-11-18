# -*- coding: utf-8 -*-
from builder_core import build_course

def get_movies_part4():
    courses = []

    # 7. 《摩登家庭》(Modern Family) · 10 章全集
    courses.append(build_course({
        "id": "course-mov-modern",
        "title": "《摩登家庭》(Modern Family) · 美国家庭温情幽默生活美语 (10章全集)",
        "category": "movies",
        "categoryName": "影视英语",
        "coverGradient": "from-sky-500 via-indigo-600 to-amber-500",
        "icon": "🏡",
        "description": "加州阳光下的三组欢喜美国家庭，真实鲜活的美式家庭会话、父母经、夫妻相处与温情治愈金句。",
        "difficulty": "中级 B1",
        "tags": ["美剧经典", "家庭生活", "地道口语", "温馨治愈"]
    }, [
        {
            "title": "第 1 幕 · 普里切特与邓菲家族的三种现代生活",
            "description": "酷爸菲尔、严母克莱尔、老硬汉杰与抓马夫夫，不同寻常的多元大家庭。",
            "sentences": [
                {"en": "We're from three different families, but somehow we all fit together like a messy, noisy puzzle.", "cn": "虽然我们来自三条截然不同的人生轨迹与家庭形态，但在冥冥之中，我们却如同乱糟糟但严丝合缝的拼图般融为了一体。"},
                {"en": "I'm a cool dad; that's my thing, I surf the web, I text, LOL: laugh out loud, WTF: why the face?", "cn": "我可是一位紧跟潮流的酷老爸；这是我的标志性人设！我天天网上冲浪、发短信！比如LOL是大笑，WTF是为什么愁眉苦脸！(菲尔经典误解)"},
                {"en": "Claire is the organizational backbone of the house; without her, the kids would be feral beasts.", "cn": "克莱尔是整个家庭绝对不可动摇的组织管理主心骨；如果缺了她雷厉风行的打理，这群熊孩子早就退化成野兽了。"},
                {"en": "Jay married a gorgeous Colombian woman named Gloria, who is vibrant, loud, and half his age.", "cn": "老杰迎娶了一位名叫歌洛利亚的美艳哥伦比亚大美女，她热情似火、嗓门宏亮，而且年龄足足比杰小了一大半。"},
                {"en": "Mitchell and Cameron just flew back from Vietnam holding an adorable adopted baby girl named Lily.", "cn": "米奇尔和卡梅隆刚搭乘跨洋国际航班从越南领养归来，怀里紧紧抱着他们可爱至极的宝贝养女小莉莉。"},
                {"en": "Family is not just about shared DNA; it's about showing up when someone needs a shoulder to cry on.", "cn": "所谓的家人，绝不仅仅是指血管里流淌着相同的DNA染色体；而是当有人委屈难过时，你随时都在他身侧送上坚实的肩膀。"},
                {"en": "Haley is texting her boyfriend upstairs while Alex is reading a four-hundred-page biochemistry textbook.", "cn": "大女儿海莉正躲在二楼卧室疯狂给小男友发甜言蜜语短信，而二女儿艾利克斯却正捧着一本四百页的生物化学大部头专心啃读。"},
                {"en": "Luke got his head stuck in the banister again because he wanted to see if his ears could fold.", "cn": "调皮的小儿子卢克又一次把整颗脑袋死死卡在了楼梯扶手栏杆里，理由仅仅是他突发奇想测试一下自己的耳朵能不能像折纸一样折叠。"},
                {"en": "Manny wears a silk smoking jacket and drinks espresso like a fifty-year-old retired European count.", "cn": "早熟的曼尼小小年纪就天天套着一件奢华丝绸晨袍，慢条斯理品着浓缩意式咖啡，言行举止活脱脱像个退休的五十岁欧洲伯爵。"},
                {"en": "Marriage is a partnership where one person is always right, and the other person is the husband.", "cn": "所谓的世俗婚姻其实就是一种奇妙的合伙机制：其中一方永远正确无误，而另一方则恰好是老实巴交的倒霉丈夫。"},
                {"en": "Cameron played the Lion King soundtrack on full volume as he dramatically presented the baby to the family.", "cn": "卡梅隆把音响里的《狮子王》神圣主题曲音量开到震耳欲聋的最大档，满怀戏剧张力地单手托举起婴儿，向全体惊呆的亲戚庄严亮相展示。"},
                {"en": "Jay winced at the spectacle, desperately wishing his son would choose a quieter hobby than showmanship.", "cn": "老硬汉杰看着眼前这出抓马大戏忍不住痛苦揉着太阳穴，打心底里暗暗祈求儿子今后能挑个比浮夸演戏稍微安静收敛点的正常爱好。"},
                {"en": "Gloria laughed warmly, welcoming the child with open arms and a spirited Colombian blessing.", "cn": "歌洛利亚却毫不介意地爽朗哈哈大笑，敞开温暖怀抱一把将婴儿搂入怀中，操着一口浓郁口音送上热情洋溢的哥伦比亚祝福。"},
                {"en": "Nobody in this household is normal, and honestly, that's our greatest hidden superpower.", "cn": "在这个庞大吵闹的屋檐之下，其实压根没有哪一个人算得上世俗眼中的“正常人”；而说句公道话，这恰恰是我们家最引以为傲的隐形超能力。"},
                {"en": "Gather everyone at the dining room table; Sunday family dinner is completely mandatory!", "cn": "把所有人立刻通通轰到餐厅长桌前集合！在我们家，每周日的家庭大聚餐是绝对强制性出席、概不接受请假的铁律！"}
            ]
        },
        {
            "title": "第 2 幕 · 菲尔·邓菲的现代父爱哲学与神奇魔术",
            "description": "Phil's-osophy 菲式生活大智慧，当世界上最棒的酷爸和兼职房产金牌销售。",
            "sentences": [
                {"en": "Watch a sunrise at least once a day, Phil proclaimed proudly from his self-help notebook.", "cn": "一天至少看一次壮丽的日出！菲尔手捧着他亲笔撰写的励志秘笈，满脸自豪得瑟地大声宣读自己的传世座右铭。"},
                {"en": "If you love something, set it free, unless it's a tiger; then keep it in a sturdy cage.", "cn": "如果你深爱一样事物，就应当放手任它自由翱翔；但如果那是一头猛虎，你还是赶紧把它死死锁在结实的铁笼里吧！"},
                {"en": "Real estate is not about houses; it's about matchmaking emotional humans with square footage.", "cn": "我所从事的房地产经纪行业本质上卖的绝不是砖瓦房屋；而是充当一根温情红娘红线，将情感丰富的人类与温馨的生活空间完美撮合。"},
                {"en": "I mastered the French drop coin sleight-of-hand when I was merely eight years old.", "cn": "早在老子区区八岁那年，我就已经出神入化地彻底精通了法式落币这个高难度的近景魔术手法！"},
                {"en": "A magician never reveals his secrets, Claire, especially when the trick completely backfires.", "cn": "一个拥有职业操守的真正魔术师永远绝不会泄露他的机密，克莱尔，尤其是当那个魔术当场彻底翻车搞砸的时候！"},
                {"en": "Never be afraid to be ridiculous; the world has enough boring, serious people already.", "cn": "永远不要畏惧在旁人面前显得滑稽搞笑、荒诞不经；这冰冷乏味的人世间，早就充斥着太多无聊透顶、正襟危坐的无趣之徒了。"},
                {"en": "I built a miniature treehouse in the backyard with a fully operational electric pulley elevator.", "cn": "我在后院的大橡树上亲手为孩子们搭建了一座梦幻般的微型树屋，里面甚至还配备了一部能够正常运转通电的滑轮电动小电梯！"},
                {"en": "Every time Luke laughs at one of my silly jokes, I feel like a billionaire.", "cn": "每当小卢克被我随口讲的某个无厘头烂梗逗得前仰后合哈哈大笑时，我都打心底里觉得自己比坐拥百亿的超级富豪还要富有满足。"},
                {"en": "Claire thinks I coddle the children, but childhood should be full of wonder and trampoline backflips.", "cn": "克莱尔老是指责我太溺爱放纵孩子，但童年本来就该充满数不尽的奇思妙想，以及在蹦床上欢畅无忧的后空翻啊！"},
                {"en": "I'm not saying I'm the perfect husband, but I did buy her a label maker for our tenth anniversary.", "cn": "我可从没大言不惭自夸说自己是个十全十美的完美模范丈夫，但我确实在十周年结婚纪念日那天，贴心送了她一台高档标签打印机！"},
                {"en": "Cheerleading in college taught me rhythm, flexibility, and how to catch flying humans gracefully.", "cn": "大学时期参加男子啦啦队担任核心主力的宝贵经历，教会了我绝佳的节拍韵律感、身体柔韧性，以及如何优雅稳当地凌空接住飞人！"},
                {"en": "Always look people in the eye, shake their hand firmly, and remember their dog's birthday.", "cn": "在社交职场上，永远要坦诚直视对方的双眼，有力地握紧他们的手掌，并且务必牢记他们家爱犬的生日！"},
                {"en": "The secret to life is finding someone who makes you laugh so hard your soda comes out of your nose.", "cn": "人这一辈子幸福的真谛，莫过于能有幸找到一个知心伴侣，她能把你逗得捧腹大笑，甚至让刚喝进嘴里的冰镇汽水直接从鼻孔里喷出来！"},
                {"en": "I am putting my foot down, Claire; we are definitely keeping this vintage arcade machine in the living room!", "cn": "克莱尔，这次我可要拿出一家之主的威严坚决表态了：这台复古街机游戏机，必须雷打不动安放在咱们客厅最显眼的C位！"},
                {"en": "Sweetheart, I love you more than all the popcorn in the movie theaters across North America.", "cn": "亲爱的老婆大人，我对你的深深爱意，比全北美所有电影院里炸出来的金黄爆米花堆在一起还要多得多！"}
            ]
        },
        {
            "title": "第 3 幕 · 歌洛利亚的热情大嗓门与哥伦比亚往事",
            "description": "Gloria 的浓郁西语发音、麻辣性格、母爱护短与杰的唯命是从。",
            "sentences": [
                {"en": "In my village in Colombia, if someone insults your cooking, you challenge them to a machete dance!", "cn": "当年在我们哥伦比亚老家的小山村里，要是敢有哪个不怕死的胆敢侮辱你烧的饭菜难吃，你当场就得拔出大砍刀跟他跳刀尖生死舞！"},
                {"en": "Jay, do not tell me to lower my voice; this is not yelling, this is just my normal Colombian passion!", "cn": "杰，少在那指手画脚命令我把嗓门压低！这根本就不是在吵架嚷嚷，这纯粹只是我骨子里最天然的哥伦比亚热情奔放而已！"},
                {"en": "Manny is a delicate poetic genius who deserves to be pampered with hot empanadas every single morning.", "cn": "我们家曼尼可是一位心思细腻纯良的旷世诗意天才，理所应当在每一个清晨都享受到我亲手为他现烤的酥脆肉馅大馅饼！"},
                {"en": "You think I married Jay for his money? Have you seen how handsome he looks when he pays the bill?", "cn": "你真以为老娘当年嫁给杰是图他的臭钱吗？难道你们就没亲眼注意过，每当他掏钱包买单时那副霸气侧漏的帅气模样有多迷人吗？！"},
                {"en": "Stella the French bulldog is stealing my husband's affection; he feeds her prime rib while I get leftovers!", "cn": "那只叫斯特拉的小法国斗牛犬分明就是在明目张胆跟我抢夺丈夫的专房宠爱！杰天天拿顶级牛排喂它，我却只能吃剩菜！"},
                {"en": "I am a fantastic driver; the police officer who pulled me over was just completely enchanted by my smile.", "cn": "我的驾驶车技简直堪称无可挑剔行云流水；刚才那个把我拦在路边的交警，分明就是被我迷人的微笑给彻底勾魂迷住了嘛！"},
                {"en": "Never look down on someone who speaks broken English; it means they speak another language fluently.", "cn": "永远不要戴着有色眼镜去轻视嘲讽一个英语说得结结巴巴的外国人；因为那恰恰证明，他在另一种古老母语的世界里能说会道、对答如流！"},
                {"en": "I wear high heels to the supermarket because a proud Latin woman never presents herself as sloppy.", "cn": "我哪怕只是出门去下楼的超市买根葱，也必须踩上一双十厘米高跟鞋！因为一个自豪高贵的拉丁女人，绝不允许自己蓬头垢面展现出半分邋遢！"},
                {"en": "Jay tried to teach me American golf, but I accidentally launched the golf cart into the country club pond.", "cn": "杰前几天兴致勃勃硬要教我学打美式高尔夫，结果一个不留神，我一脚油门把他的高尔夫球车直接怼进了乡村俱乐部的人工水池里！"},
                {"en": "In Colombia, we respect our grandmothers, we dance until sunrise, and we always protect our babies with fire.", "cn": "在我们哥伦比亚故土，我们对白发先祖怀揣崇高敬意，我们踏着节奏通宵达旦起舞到天明，而且当有人胆敢欺负我们的骨肉孩子时，做母亲的绝对会化作护短的烈火狂兽！"},
                {"en": "Manny wrote a sonnet for an older girl who didn't even notice him, and it broke my maternal heart into pieces.", "cn": "曼尼给一个高年级女孩写了一首字字泣血的深情十四行诗，结果人家看都没看一眼直接扔了，这当场把为娘的心给彻底揉碎成了一地齑粉！"},
                {"en": "I put hot chili pepper flakes in the pancake batter to give Jay's sluggish circulation a much-needed kick.", "cn": "我在今天早晨摊的松饼面糊里特意重重抓了两大把魔鬼辣椒碎，专门给杰那日益迟缓的血液循环来上一记立竿见影的强心猛药！"},
                {"en": "When life gives you lemons, Jay, you squeeze them into tequila and turn up the Latin salsa music!", "cn": "当生活冷不丁朝你砸来酸涩苦涩的柠檬时，杰，你应该顺手把它们挤进烈酒龙舌兰杯子里，然后把拉丁骚莎舞曲的音响开到最大狂欢！"},
                {"en": "I love this grumpy old American man with every fiber of my being, even when he snores like a freight train.", "cn": "我全心全意深爱着眼前这个脾气倔强暴躁的美国小老头，哪怕每当夜幕降临、他躺在枕头边打呼噜像一列轰隆隆鸣笛的重型货运火车！"},
                {"en": "Family is our armor against the cruel world; whoever tries to hurt them must deal with me first!", "cn": "这个家庭是我们抵御外界冷酷人世的最坚固铠甲；不论未来是谁胆敢企图伤害他们，就必须先踩过老娘我的尸体！"}
            ]
        },
        {
            "title": "第 4 幕 · 卡梅隆与米奇尔的抓马夫夫育儿日常",
            "description": "敏感又戏精的乡村农场男孩 Cameron，与理性纠结的律师 Mitchell 的互补之爱。",
            "sentences": [
                {"en": "Mitchell, you are catastrophizing again! Cameron gasped dramatically with an exaggerated hand flutter.", "cn": "米奇尔，你又在毫无根据地把微不足道的小事脑补成灭顶之灾了！卡梅隆双手戏剧性地捂住胸口，倒吸一口夸张的冷气惊呼道。"},
                {"en": "I was raised on a cattle farm in Missouri, Mitchell; I know how to birth a cow and arrange a floral centerpiece!", "cn": "老子可是在密苏里州广阔的肉牛养殖农场里土生土长摸爬滚打长大的，米奇尔！我既能撸起袖子给母牛稳稳接生，又能心细如发插出惊艳全场的晚宴花艺中轴！"},
                {"en": "Fizbo the clown is not just a costume; Fizbo is an artistic alter ego born of pure performance joy!", "cn": "小丑“菲兹波”绝不仅仅只是一套滑稽花哨的演出皮囊道具；菲兹波是我源自纯粹舞台表演欢愉、倾注毕生心血孕育而成的艺术第二人格！"},
                {"en": "Please don't bring Fizbo to Lily's pre-school birthday party; you terrorized three toddlers last year.", "cn": "拜托求求你千万别把菲兹波那一套带到莉莉的幼儿园生日派对上来了；你去年扮演小丑时，把三个牙牙学语的小毛头吓得当场哭抽了过去！"},
                {"en": "I am an environmental lawyer because I care about justice, clean water, and avoiding confrontation with strangers.", "cn": "我之所以立志成为一名环保专职律师，是因为我内心渴望捍卫法律正义、保护清澈水源，同时也是为了在现实生活中尽可能避免当面与生人起肢体冲突。"},
                {"en": "Lily just used her first sarcastic tone of voice, and I don't know whether to ground her or congratulate her.", "cn": "小莉莉刚才破天荒头一次用上了极其刻薄老练的讽刺冷嘲口吻，我此刻甚至陷入了巨大的迷茫：究竟是该当场罚她禁足面壁，还是由衷拍手祝贺她青出于蓝？"},
                {"en": "Cameron bought an eight-foot stuffed giraffe for the nursery without consulting the household budget.", "cn": "卡梅隆事先压根没有翻看一眼家庭开支账本，就头脑发热擅自买回来一只八英尺高、把整个育儿室塞得满满当当的巨大长颈鹿毛绒玩偶！"},
                {"en": "You are emotionally manipulative, Cameron! And you are repressed and chronically unspontaneous, Mitchell!", "cn": "你简直就是在用你的眼泪进行情感绑架，卡梅隆！——而你则是个内心压抑冷漠、从来不知自发浪漫为何物的死板老顽固，米奇尔！"},
                {"en": "Two hours later, they were harmonizing a show tune while spoon-feeding organic strained peas to their baby.", "cn": "两个小时之后，刚刚吵得不可开交的夫夫二人，竟然已经并肩琴瑟和鸣轻哼着百老汇经典选段，默契十足地一勺一勺给怀里的宝贝喂着有机细腻的青豆泥。"},
                {"en": "Parenting is terrifying because every single mistake feels like you are permanently ruining a human life.", "cn": "为人父母之所以令人神经衰弱胆战心惊，是因为你犯下的每一个看似微不足道的纰漏差错，都会让你自责觉得正在亲手彻底毁掉一条崭新的无辜生命。"},
                {"en": "Cameron's dramatic gasps can be heard from three blocks away whenever he drops an heirloom china saucer.", "cn": "每当卡梅隆失手摔碎一只祖传瓷碟时，他嘴里倒抽出的戏剧性凄惨哀嚎声，隔着整整三个街区都能听得清清楚楚。"},
                {"en": "We complement each other: I stop you from floating away into fantasy, and you stop me from burying myself in misery.", "cn": "我们二人是天造地设的互补绝配：我负责拉紧手中的风筝线，阻止你彻底飘上虚幻云端；而你则负责伸出援手，拉住我不让我一头扎进苦闷悲观的泥潭。"},
                {"en": "Lily rolled her eyes at both her fathers, demonstrating maturity far beyond her four calendar years.", "cn": "早熟的小莉莉对着自己这两个戏精老爸毫不客气地翻了一个巨大的白眼，展现出了远远超出她区区四岁生理年龄的冷艳早熟与淡定。"},
                {"en": "Our home may be a theater of endless chaos, but there is never a single shortage of overwhelming love.", "cn": "虽然我们的小家注定是一座永无休止上演着抓马闹剧的喧嚣剧场，但在这一方屋檐之下，却从来没有哪怕一天缺少过浓烈得化不开的真挚大爱。"},
                {"en": "Pass the white wine, Mitchell; tomorrow is another day to overthink our entire parenting existence.", "cn": "把那瓶冰镇白葡萄酒递给我吧，米奇尔；等到明儿个太阳升起，咱们有的是漫漫大好光阴，继续为咱们的育儿人生过度焦虑、瞎操碎心。"}
            ]
        },
        {
            "title": "第 5 幕 · 家族感恩节大聚餐与爱是一切答案",
            "description": "火鸡烤糊、秘密曝光、鸡飞狗跳之后的温情大团圆，平凡家庭最伟大的羁绊。",
            "sentences": [
                {"en": "Thanksgiving at the Pritchett household is like a high-stakes tactical military operation with cranberry sauce.", "cn": "在普里切特家族操办筹备一场感恩节晚宴，其紧张激烈程度丝毫不亚于一场浇灌了蔓越莓酸甜果酱的顶级高风险战术特种军事演习。"},
                {"en": "Phil attempted to cook the turkey using an experimental rapid-heat satellite parabolic dish in the garden.", "cn": "菲尔突发奇想大搞发明创造，企图利用安在后花园草坪里的一面实验性卫星抛物面聚热雷达锅，来给大火鸡进行急速辐射烧烤。"},
                {"en": "Naturally, the lawn caught fire and the turkey launched itself fifty feet into the neighbor's swimming pool.", "cn": "顺理成章、毫不意外的是，后院的绿茵草皮瞬间燃起了熊熊大火，而那只烤得焦黑的大火鸡则如火箭升空般凌空飞窜五十英尺，径直扎进了隔壁邻居家的人工泳池里。"},
                {"en": "Claire was having a nervous breakdown in the kitchen because her secret pumpkin pies had not set properly.", "cn": "克莱尔在厨房操作台前急得濒临神经崩溃边缘，只因她精心秘制揉捏的面点南瓜派内馅，迟迟无法达到理想的凝固成型状态。"},
                {"en": "Jay sat calmly on the porch sipping scotch, remarking that every Thanksgiving catastrophe builds character.", "cn": "老硬汉杰却独自从容不迫地倚靠在走廊摇椅上品着苏格兰威士忌，老神在在地点评道：每一次感恩节翻车大灾难，都是锤炼磨砺家族性格的绝佳试金石。"},
                {"en": "Haley admitted she had dropped out of community college, while Alex confessed she was utterly burnt out from perfectionism.", "cn": "大姐海莉终于红着眼圈当众坦白承认自己偷偷退了社区大学的学籍，而学霸二姐艾利克斯也声泪俱下倾诉自己快被令人窒息的完美主义彻底逼疯压垮了。"},
                {"en": "Secret resentments bubbled to the surface until Gloria slammed a heavy cast-iron skillet onto the counter.", "cn": "积压多年的隐秘埋怨与琐碎委屈如同沸水般接连泛起，直到歌洛利亚满面怒容，将一口沉重厚实的铸铁煎锅狠狠砸在料理台大理石上发出巨响。"},
                {"en": "SILENCE! Look at each other! Gloria roared. We are healthy, we are together, and we are not starving!", "cn": "都给老娘统统闭嘴！抬头好好看看身边的彼此！歌洛利亚如雌狮般咆哮怒喝道，我们全须全尾健健康康，我们并肩相守团聚在一处，而且我们谁也没饿死！"},
                {"en": "Manny recited a Thanksgiving poem he wrote about gratitude, perseverance, and the sweetness of shared meals.", "cn": "曼尼优雅起身深情朗诵了他昨夜亲笔创作的感恩节长诗，字里行间流淌着关于感恩、隐忍坚守，以及围坐一堂共进家常便饭的甜美滋味。"},
                {"en": "We ended up ordering Chinese takeout: greasy egg rolls, orange chicken, and fortune cookies on paper plates.", "cn": "最终折腾了半宿的大家不得不认命点了一大堆中餐外卖：摆在廉价一次性纸盘子上的油滋滋炸春卷、酸甜陈皮鸡，还有藏着吉言的幸运小饼干。"},
                {"en": "Sitting cross-legged on the living room floor, Jay proposed a heartfelt toast to his wildly eccentric family.", "cn": "全体老小不分长幼盘腿席地围坐在客厅地板中央，杰缓缓举起手中的纸杯，向眼前这群脾性各异、千奇百怪的至亲家人致以了发自肺腑的真诚祝酒辞。"},
                {"en": "I wouldn't trade a single minute of this noisy, infuriating chaos for all the serene mansions in Beverly Hills.", "cn": "就算拿全比弗利山庄所有奢华幽静的高门府邸摆在老子面前，我也绝不肯拿咱们此刻吵吵闹闹、令人抓狂的鸡飞狗跳去换哪怕一分一秒。"},
                {"en": "Sometimes the people who drive you the craziest are the exact same ones who keep you anchored to sanity.", "cn": "在这个光怪陆离的人世间，有的时候，恰恰是那些平日里把你逼得快要原地发疯抓狂的家人，才是在暗中默默拉紧锚链、守护着你内心仅存理智的终极避风港。"},
                {"en": "The cameras pulled back through the illuminated front window as the entire household laughed through their tears.", "cn": "伴随着全家老小在欢笑与释然的泪水中紧紧相拥冰释前嫌，记录日常的镜头穿过温暖透亮的明亮窗棂缓缓向后摇出。"},
                {"en": "We're not the Cleavers, and we're definitely not normal, but we are Modern Family, and we love fiercely.", "cn": "我们绝不是上世纪传统肥皂剧里规规矩矩的模范榜样，我们也注定与循规蹈矩的平庸无缘；但我们就是独一无二的《摩登家庭》，我们的爱，烈焰滔天、坚不可摧！"}
            ]
        },
        {
            "title": "第 6 幕 · 杰与小法斗斯特拉的独宠日常与水疗体验",
            "description": "老硬汉的铁汉柔情，全家吃剩菜，唯有宠物狗斯特拉独享顶级水疗与菲力牛排。",
            "sentences": [
                {"en": "Jay Pritchett built an entire closet manufacturing empire with grit, sweat, and zero emotional vulnerability.", "cn": "杰·普里切特早年凭借着钢铁般顽强的坚毅拼劲、数不尽的辛酸汗水以及对示弱矫情的零容忍，硬生生打造出了一座傲视业界的庞大壁橱制造帝国。"},
                {"en": "When the family first brought home Stella the French bulldog, Jay insisted she sleep in the garage.", "cn": "当年孩子们头一次把那只叫斯特拉的法斗幼犬领回家时，杰满脸铁面无私地严正声明：这畜生只配睡在冰冷的地下车库里！"},
                {"en": "Two weeks later, Jay was tucking the dog into custom goose-down blankets and singing her soft lullabies.", "cn": "仅仅过了两周不到，老杰就已经天天满脸慈祥地用订制的高级纯白鹅绒小被子把狗狗严严实实裹好，轻声哼着温柔摇篮曲哄她入睡了。"},
                {"en": "Gloria watched in disbelief as her husband prepared organic baby carrots and cooked salmon for the pet.", "cn": "歌洛利亚难以置信地眼睁睁看着平日里不可一世的霸气大老板丈夫，竟然系着围裙心细如发地为宠物狗慢炖新鲜有机胡萝卜配香煎三文鱼。"},
                {"en": "Stella has sensitive digestion, Gloria! Jay yelled defensively, brushing the dog's velvet wrinkles with chamomile cream.", "cn": "歌洛利亚你懂个屁！人家斯特拉的肠胃有多娇嫩敏感你又不是不知道！杰急得扯着嗓门强词夺理辩解，手里还正小心翼翼拿着洋甘菊护肤霜擦拭着狗脸上的褶子。"},
                {"en": "You don't understand the profound, unspoken bond between an aging American patriarch and his bulldog.", "cn": "你们这群不懂事的小崽子，根本无法体会一位饱经沧桑的垂暮美国老硬汉与他的忠诚法国斗牛犬之间那份深沉无言的崇高默契！"},
                {"en": "Jay took Stella to an elite canine day spa where she received a lavender aromatherapy mud bath.", "cn": "杰背着全家人偷偷把斯特拉带进了一家收费昂贵的比弗利顶级宠物日间水疗中心，让这只小胖狗惬意享受了一整套薰衣草芳香矿物泥浴。"},
                {"en": "Manny complained that he hadn't received that much grandfatherly affection in his entire fourteen years.", "cn": "曼尼满腹委屈地在旁边小声抗议发牢骚：在老子过去长达十四年的整个人生岁月里，享受过的慈祥祖辈关爱加在一起，居然还不如一条狗的一个周末！"},
                {"en": "The dog accidentally fell into the swimming pool, and Jay leaped in fully clothed with his wallet in his pocket.", "cn": "有一回斯特拉脚底打滑不慎掉进了后院深水泳池里，老杰连身上的高级西装都没顾得上脱，钱包还在裤兜里，就毫不犹豫噗通一声纵身扑入水中舍命相救！"},
                {"en": "You didn't even jump in when my mother fell into the fountain at the mall! Gloria shouted in righteous fury.", "cn": "当年老娘的亲妈在商场大厅不小心一头跌进许愿喷泉池子里时，你老人家可是站在岸边袖手旁观连手指头都没动一下！歌洛利亚气得大发雷霆尖叫道。"},
                {"en": "That was different; your mother was sitting in six inches of water throwing coins at the security guard!", "cn": "那情况能一样吗？！你丈母娘当年坐在区区六英寸深的浅水坑里，手里还正抓着一把硬币凶狠地往赶来救人的保安脸上猛砸呢！"},
                {"en": "Stella chewed up Gloria's favorite designer leopard-print stiletto, and Jay blamed the humidity.", "cn": "斯特拉趁屋里没人，偷偷把歌洛利亚最珍爱的一双大牌豹纹细高跟名鞋给嚼得稀烂，而老杰却厚颜无耻地把责任统统推卸给了南加州的空气潮湿。"},
                {"en": "A dog never judges your past mistakes, never asks for tuition money, and always greets you like a hero.", "cn": "一只忠诚的爱犬永远不会吹毛求疵审判你过往犯下的人生过失，永远不会管你伸手要高昂的大学学费，而且每当你推门回家时，她都会把你当成救世大英雄一样狂摇尾巴！"},
                {"en": "Gloria eventually found Stella sleeping peacefully on Jay's chest while both of them snored in rhythmic harmony.", "cn": "歌洛利亚最终推开书房房门，看到斯特拉正乖巧安详地趴在杰宽阔起伏的胸膛上打盹，一人一狗的沉重呼噜声此起彼伏，奏出了一曲奇妙和谐的催眠乐章。"},
                {"en": "Beneath that crusty, sarcastic exterior, old Jay Pritchett possessed a marshmallow heart that belonged to a dog.", "cn": "在老杰·普里切特那副平日里嘴硬心软、刻薄讽刺的坚硬坚果外壳之下，其实深藏着一颗早已被一只法斗小狗彻底融化成棉花糖的纯情心灵。"}
            ]
        },
        {
            "title": "第 7 幕 · 曼尼的小小情圣早熟人生与咖啡馆创作",
            "description": "十四岁的外表下住着八十岁的古老浪漫灵魂，品意式浓缩，写催人泪下的情诗。",
            "sentences": [
                {"en": "Manny Delgado entered the world with the gravitas of a Renaissance diplomat and the heart of a doomed poet.", "cn": "曼尼·德尔加多降临到这个人世间的第一天起，就浑身自带一股文艺复兴时期外交家的沉稳庄严气场，以及一个注定饱尝相思之苦的悲情诗人之心。"},
                {"en": "He refused to wear cargo shorts to middle school, opting instead for tailored burgundy linen suits and fedoras.", "cn": "他上初中时坚决拒绝套上同龄男生常穿的土气工装短裤，而是特立独行换上一身量身剪裁的高贵酒红色亚麻西服，头顶绅士软呢帽大步穿过走廊。"},
                {"en": "A true gentleman never drinks skim milk, Jay; skim milk is merely water lying about being milk.", "cn": "一位真正懂得品味人生的得体绅士绝不喝脱脂牛奶，杰；所谓的脱脂牛奶，不过只是装模作样谎称自己是牛奶的寡淡清水罢了！"},
                {"en": "Manny fell in love with a high school senior girl because she wore a vintage beret and read French existentialism.", "cn": "曼尼无可救药地疯狂暗恋上了一位读高三的学姐，理由极其浪漫脱俗：只因那个女孩头戴一顶复古法式贝雷帽，平日里总爱坐在长椅上静读法国存在主义哲学。"},
                {"en": "He spent three evenings composing an epic love ballad on his classical acoustic guitar.", "cn": "他连着熬了整整三个通宵长夜，用他那把古典民谣尼龙吉他，字斟句酌地为心上人谱写出一曲悲天悯人的宏伟爱情抒情长诗。"},
                {"en": "Gloria patted his cheek encouragingly, promising that one day a sensible woman would worship his poetic soul.", "cn": "歌洛利亚慈爱宠溺地轻抚着儿子圆滚滚的面颊打气鼓励，斩钉截铁许诺：总有一天，这世上会有一个懂货识珠的明智好姑娘，将他高贵的诗意灵魂奉为神明！"},
                {"en": "Jay advised him to stop writing sonnets and try throwing a football around the park like a normal teenager.", "cn": "老硬汉杰则恨铁不成钢地在旁泼冷水，劝这小家伙赶紧把那些酸溜溜的情诗撕了，像个阳刚正常的小子一样去公园草地上狠狠扔两记橄榄球！"},
                {"en": "I don't play football, Jay; athletics is merely aggressive geometry in brightly colored synthetic spandex.", "cn": "我才不屑于去碰那些粗鲁野蛮的橄榄球呢，杰；所谓的竞技体育，不过只是一群大汉穿着花里胡哨的化纤紧身裤在泥浆里进行带有攻击性的几何冲撞罢了！"},
                {"en": "When the girl gently turned him down at the school dance, Manny sat by the punch bowl with stoic dignity.", "cn": "当那个漂亮女孩在校园迎新舞会上委婉礼貌地回绝了他的邀舞请求时，曼尼神色自若地端坐在水果冷饮碗旁，展现出了超越年龄的坚毅隐忍尊严。"},
                {"en": "Rejection is the raw fertilizer from which great literature blossoms, he declared, taking a sip of ginger ale.", "cn": "残酷的拒绝与失恋，恰恰是孕育浇灌出名垂青史的伟大文学作品的最肥沃天然养料！他从容端起高脚玻璃杯品了一口姜汁汽水，淡淡感慨道。"},
                {"en": "Luke tried to cheer him up by challenging him to eat a raw hot dog bun in under fifteen seconds.", "cn": "卢克为了让好兄弟开心起来，煞有介事地朝他下战书发起极限挑战：敢不敢在十五秒之内生吞下一整根干燥无味的热狗白面包皮！"},
                {"en": "You are a barbarian, Luke, but you are my brother, and I accept your culinary duel.", "cn": "卢克，虽然你骨子里是个无可救药的粗野野蛮人，但你毕竟是我血浓于水的手足挚友，这趟滑稽荒诞的美食决斗，老子接下了！"},
                {"en": "Manny would grow up to attend college, write theater plays, and forever remain the hopeless romantic of the clan.", "cn": "曼尼日后终将昂首步入高等学府，亲手编排名噪一时的百老汇舞台戏剧，并成为这个庞大家族里至死不渝的浪漫主义绝唱守护者。"},
                {"en": "Never lose that tender tenderness in your eyes, Manny, because cynics are everywhere, but lovers are rare.", "cn": "曼尼，请你无论经历世事如何变迁，都千万不要丢掉你眼眸深处那份温润纯良的善意柔情；因为愤世嫉俗的看客满大街都是，而满腔赤诚的深情之人世间罕见。"},
                {"en": "The young man straightened his silk necktie in the mirror, fully prepared to have his heart broken once again.", "cn": "这位少年在穿衣镜前一丝不苟地整理扶正了自己的真丝小领结，嘴角扬起微笑，早已从容做好了再次为世间纯美爱情碰得头破血流的豁达准备。"}
            ]
        },
        {
            "title": "第 8 幕 · 艾利克斯的学霸求索与海莉的成长阵痛",
            "description": "加州理工学霸二姐的巨大焦虑，与时尚达人大姐 Haley 在碰壁中寻找自我定位。",
            "sentences": [
                {"en": "Alex Dunphy possessed an intellectual quotient higher than the rest of her immediate household combined.", "cn": "艾利克斯·邓菲那颗惊为天人的超级大脑智商数值，甚至比这间屋檐下其余所有家庭成员的智商加在一起还要高出一大截。"},
                {"en": "She stayed awake until three in the morning every night studying multivariable calculus and organic chemistry.", "cn": "每一个夜深人静的深夜时分，她都孤灯独坐苦战到凌晨三点，全神贯注钻研着深奥晦涩的多元微积分与错综复杂的有机化学方程式。"},
                {"en": "Nobody understands the suffocating pressure of being the only capable adult in an entire nuclear family.", "cn": "你们根本没有任何一个人能够体会：当一个人身为全家唯一心智成熟、清醒靠谱的顶梁柱成年人时，肩头背负着怎样令人窒息的沉重心理重压！"},
                {"en": "Meanwhile, her older sister Haley was obsessed with boys, Coachella outfits, and social media follower counts.", "cn": "与此同时，她那生得如花似玉的亲姐姐海莉，脑瓜里却成天塞满了帅气男生、科切拉音乐节的火辣穿搭，以及社交网络主页上蹭蹭上涨的粉丝关注点赞量。"},
                {"en": "Haley could coordinate an entire wardrobe in forty seconds, but couldn't calculate a fifteen percent dinner tip.", "cn": "海莉能够在短短四十秒之内极其毒辣精准地完成一整套绝美潮流穿搭风格的搭配，却唯独算不明白一顿晚宴百分之十五的服务小费究竟是多少钱。"},
                {"en": "You think I have it easy? Haley snapped in a rare moment of tearful vulnerability during high school finals.", "cn": "你真以为我成天没心没肺笑嘻嘻就活得很轻松是吗？！在高中毕业大考前夕的一场罕见争执中，海莉终于在泪崩的脆弱瞬间委屈地声泪俱下质问。"},
                {"en": "Everyone expects you to succeed, Alex, but everyone quietly assumes that I am going to fail completely.", "cn": "全天下所有人都在翘首以盼等着看你金榜题名功成名就，艾利克斯！但所有人在背地里却早已认定了：我海莉这辈子注定是个一事无成的蠢花瓶！"},
                {"en": "Alex paused, looking at her older sister with genuine empathy for the first time in years.", "cn": "艾利克斯浑身一震猛然愣在原地，在两姐妹漫长数年的针锋相对岁月里，她破天荒头一次对眼前这个亲姐姐涌起了一股由衷的怜惜与共情。"},
                {"en": "Sisters fight like sworn adversaries, but when real heartbreak strikes, they build a fortress around each other.", "cn": "亲姐妹之间平日里吵起架来狠戾得宛如不共戴天的生死宿敌；但每当现实的重击与失恋的风雨无情降临时，她们却会在第一时间化作彼此最坚不可摧的坚固堡垒。"},
                {"en": "Alex got accepted into the prestigious California Institute of Technology to study experimental physics.", "cn": "功夫不负有心人，艾利克斯最终凭借无可挑剔的卓越全优履历，昂首荣获了享誉全球的加利福尼亚理工学院实验物理学专业的录取通知书！"},
                {"en": "Haley navigated retail jobs, photography internships, and finally found her calling as a dynamic fashion stylist.", "cn": "而海莉在历经了百货专柜柜员、时尚摄影助理等一系列屡遭碰壁的底层打拼磨砺之后，终于凭借天生绝佳的敏锐审美，找到了属于自己的时尚造型师天职！"},
                {"en": "Success is not measured on a standardized academic test; it's about finding the arena where your gifts shine.", "cn": "一个人一生的成就与价值，从来不该由一张冷冰冰的标准化应试答卷来草率定义；它的真谛在于：你是否能最终寻觅到那片足以让你天赋大放异彩的辽阔舞台！"},
                {"en": "They sat on Haley's bedroom carpet eating pints of cookie dough ice cream, laughing at old yearbooks.", "cn": "姐妹俩并肩盘腿坐在海莉卧室温馨的地毯上，大勺大勺分享着一桶香甜的曲奇冰淇淋，翻看着泛黄的高中毕业纪念册笑得前仰后合。"},
                {"en": "I'm always going to be smarter than you, Haley. And I'm always going to be prettier, Alex. Deal.", "cn": "反正不管过去多少年，我在智商上永远都要比你聪明得多，海莉。——而老娘在颜值容貌上也永远都要比你漂亮得多，艾利克斯。一言为定，成交！"},
                {"en": "The bond between two sisters who survived adolescence under Phil and Claire's roof was unbreakable.", "cn": "在菲尔和克莱尔这对欢喜奇葩父母的屋檐之下摸爬滚打熬过青春期阵痛的两姐妹，她们之间的血脉羁绊早已坚不可摧、牢不可破。"}
            ]
        },
        {
            "title": "第 9 幕 · 菲尔与克莱尔的情人节：克莱夫与茱莉安娜",
            "description": "每年情人节固定上演的酒店秘密浪漫，高档风衣、电梯乌龙与十年如一日的激情。",
            "sentences": [
                {"en": "Every Valentine's Day, Phil and Claire transform into their fictional alter egos: Clive Bixby and Juliana.", "cn": "在每一年浪漫的情人节之夜，菲尔与克莱尔都会默契十足地彻底改头换面，化身为他们虚构多年的神秘特工第二人格：克莱夫·比克斯比与茱莉安娜。"},
                {"en": "Clive is a suave international businessman who designs high-end bespoke audio equipment for millionaires.", "cn": "西装革履的“克莱夫”人设是一名风度翩翩、周游列国的跨国高阶商务精英，专职为全球超级富豪量身打造顶级定制音响发烧设备。"},
                {"en": "Juliana is a mysterious, seductive woman of mystery who frequents upscale hotel cocktail lounges alone.", "cn": "而风情万种的“茱莉安娜”则是一位行踪飘忽不定、美艳不可方物的神秘绝色佳人，常常独自一人流连于奢华五星级酒店的幽暗鸡尾酒廊吧台。"},
                {"en": "Excuse me, miss, is this bar stool taken? Phil asked with his best husky baritone impression.", "cn": "打扰一下这位美丽的女士，请问您身旁这张高脚吧台椅有人预订了吗？菲尔极力压低嗓音，操着自以为最性感迷人的低沉男中音搭讪道。"},
                {"en": "It is now, Juliana purred, twirling her martini glass and giving him a dangerous, sultry glance.", "cn": "现在它归你了，先生，茱莉安娜唇边泛起勾魂夺魄的浅笑呢喃道，指尖优雅轻晃着马天尼酒杯，向他投去一抹杀伤力十足的危险魅惑眼波。"},
                {"en": "Role-playing allowed them to escape the domestic grind of carpools, grocery lists, and broken garbage disposals.", "cn": "这种充满刺激仪式感的角色扮演游戏，让他们得以在这一夜暂时逃离现实生活中接送孩子拼车、琐碎柴米油盐账单以及堵塞下水道的枯燥日常琐事。"},
                {"en": "Claire wore a scandalous trench coat with nothing underneath, planning an unforgettable romantic surprise.", "cn": "克莱尔那晚大胆穿上了一件剪裁大胆的高级风衣，里面几乎真空上阵，满心笃定要给眼前的老夫老妻来上一场终生难忘的浪漫惊喜。"},
                {"en": "Unfortunately, while riding the hotel escalator, the belt of her trench coat got hopelessly tangled in the mechanical teeth.", "cn": "然而造化弄人极其不幸的是，当她神采奕奕搭乘酒店大堂手扶电梯下楼时，风衣下摆那根长长的系带竟然被电梯运转的机械齿轮死死绞了进去！"},
                {"en": "Clive, my coat is stuck! Claire hissed in panic as the escalator continued to descend mercilessly.", "cn": "克莱夫！快救命啊，老娘的大衣被电梯绞住了！随着手扶电梯无情地持续下行，克莱尔急得在原地惊恐万状地咬牙切齿压低嗓音呼救！"},
                {"en": "Phil tried to pull the belt free, but only managed to rip the fabric, exposing her lingerie to incoming hotel guests.", "cn": "菲尔慌忙上前死命去拽那根卡死的系带，结果忙中出错刺啦一声直接把布料撕开了一个大口子，把妻子性感的贴身内衣暴露在了大堂迎面而来的宾客眼前！"},
                {"en": "Cover your eyes, tourists! Phil shouted chivalrously, throwing his tweed jacket over her bare shoulders.", "cn": "在座的所有外地游客通通把眼睛闭上，不许偷看！菲尔当机立断展现出纯正的骑士精神大吼一声，一把脱下身上的粗花呢西装大衣死死裹在妻子赤裸的双肩上！"},
                {"en": "The fire department had to be called to cut Claire free with heavy hydraulic rescue shears.", "cn": "最终酒店不得不紧急呼叫了当地消防特勤队赶到现场，动用了沉重厚实的水压剪刀，才狼狈不堪地把克莱尔从电梯机械巨口下抢救脱困出来。"},
                {"en": "They ended up sitting on the curb outside in the chilly night air, eating greasy street tacos and laughing uncontrollably.", "cn": "折腾到大半夜的夫妻俩最终只能蓬头垢面并肩并坐街边马路牙子上，迎着清凉刺骨的夜风大口啃着路边摊买来的油腻塔可卷饼，笑得前仰后合喘不过气来。"},
                {"en": "Twenty years of marriage, Phil whispered softly, and you still take my breath away every single day.", "cn": "转眼间咱们风风雨雨携手走过了整整二十年婚姻岁月，菲尔深情款款地贴着妻子的耳畔轻声低语，而在每一个日出日落的平凡日子里，你依然美得让我心跳骤停。"},
                {"en": "Claire kissed his cheek tenderly, realizing that true passion isn't about luxury; it's about making mistakes together.", "cn": "克莱尔温存地将热吻印在他饱经风霜的脸颊上，她此刻比谁都清楚：世间真正的炽热激情绝不在于五星级酒店的奢靡，而在于无论发生多大的尴尬糗事，你们依然能携手开怀大笑面对。"}
            ]
        },
        {
            "title": "第 10 幕 · 毕业典礼的泪水与家族永不散场的大合照",
            "description": "孩子长大离巢，门厅的门廊灯依然每晚为归人点亮；爱是一切的答案。",
            "sentences": [
                {"en": "The day had finally arrived: Luke and Manny were donning their blue caps and gowns for high school commencement.", "cn": "那个让全家翘首以盼、感慨万千的大日子终于如约而至：卢克和曼尼双双套上了笔挺的深蓝色学士袍，整理好方帽，准备迎接属于他们的高中毕业盛典。"},
                {"en": "Claire stood in front of the hallway mirror fixing her makeup, struggling to suppress a flood of maternal tears.", "cn": "克莱尔伫立在门厅玄关的穿衣镜前最后补着妆容，却无论如何也难以彻底压制住眼眶里决堤般奔涌而出的激动母爱热泪。"},
                {"en": "Where did eighteen years go? It feels like yesterday Luke was running around the living room with a bucket on his head.", "cn": "这漫长匆匆的十八年岁月究竟都溜去哪儿了？仿佛就在昨天，小卢克还顶着一只塑料红水桶在客厅地板上跌跌撞撞到处乱窜呢。"},
                {"en": "Jay sat in the auditorium clutching Gloria's hand, remembering when Manny was a chubby boy who couldn't throw a baseball.", "cn": "老硬汉杰端坐在礼堂长椅上紧紧攥着妻子歌洛利亚温软的手掌，脑海深处不由自主浮现出当年曼尼刚进家门时那个笨手笨脚连棒球都扔不直的微胖小豆丁。"},
                {"en": "When the headmaster announced their names, Phil jumped to his feet, blowing an illegal air horn that deafened three rows.", "cn": "当校长在主席台上庄严宣读出两位少年的名字时，菲尔如弹簧般激动得一蹦三尺高，猛然按响了违禁携带进场的巨响气笛喇叭，把前排三行家长震得两耳嗡嗡作响。"},
                {"en": "That's my son and my brother-in-law! Phil bellowed at the top of his lungs with unbridled parental pride.", "cn": "快看台上最帅的那两个小子！那是我如假包换的亲生儿子，还有我的宝贝小舅子！菲尔扯着嗓门毫无顾忌地咆哮狂呼，浑身上下洋溢着毫无保留的自豪与骄傲。"},
                {"en": "Caps were tossed into the brilliant blue California sky like a cloud of jubilant blue birds.", "cn": "数百顶学士方帽在同一瞬间被欢呼着高高抛向加利福尼亚碧空如洗的明媚蓝天，宛如一大群展翅高飞、奔向辽阔未来的欢腾青鸟。"},
                {"en": "Afterward, the entire sprawling clan gathered on the front lawn of the Dunphy residence for the ultimate family photograph.", "cn": "散席之后，这支庞大而吵闹的大家族全体老小齐刷刷汇聚在邓菲宅邸那片绿草如茵的开阔前院草坪上，准备定格下一张载入史册的家族终极全家福大合影。"},
                {"en": "Cam was directing traffic, Gloria was adjusting Lily's hair ribbon, and Stella was happily licking Jay's loafers.", "cn": "卡梅隆挥舞着双手在现场手舞足蹈指挥站位，歌洛利亚正细心为亭亭玉立的小莉莉抚平发带，而斯特拉则满心欢喜地大口舔着杰脚上的昂贵乐福皮鞋。"},
                {"en": "Phil set the tripod camera timer for ten seconds and sprinted into the frame, diving across the lawn.", "cn": "菲尔将三脚架上的单反相机延时自拍参数严密设定在十秒倒计时，随后拔腿以百米冲刺的骇人速度狂奔冲回画幅，整个人如饿虎扑食般飞扑滑入人群正中央！"},
                {"en": "Three, two, one, CHEESE! twenty voices cried out simultaneously as the camera shutter clicked.", "cn": "三，二，一，大家一起喊茄子！二十道中气十足、高低错落的欢快嗓门在同一瞬间异口同声爆发出震天长啸，伴随着相机快门咔嚓一声清脆定格！"},
                {"en": "Life is unpredictable, messy, and frequently breaks your heart into jagged little shards.", "cn": "真实的生活从来都是不可预测的、充满泥泞羁绊的，而且在漫长岁月中，它总会一次次无情将你的心狠狠摔碎成满地锯齿状的尖锐碎片。"},
                {"en": "But when you have people who love you unconditionally, those broken pieces get glued back together with gold.", "cn": "但只要你的身畔始终伫立着这样一群无条件深爱着你、包容着你所有缺点的家人，那些散落一地的残破碎片，终将被真挚的大爱以纯金液汁严丝合缝重新粘合如初。"},
                {"en": "As twilight settled over Los Angeles, the porch light above the front door remained illuminated for whoever needed to return.", "cn": "当温柔如诗的暮色暮霭缓缓低垂笼罩在繁华的洛杉矶天际线之上时，玄关门廊上方那盏泛着暖黄色光晕的门灯依旧静静彻夜长明，守候着任何一位渴望归家的游子。"},
                {"en": "Goodbye, Dunphys; goodbye, Pritchetts; thank you for teaching us that love is the modern world's greatest miracle.", "cn": "永别了，吵吵闹闹的邓菲一家；永别了，倔强坚韧的普里切特全族；由衷感谢你们用长达十一年的温暖陪伴，向全世界生动诠释了一道真理：唯有爱，才是这个摩登现代世界里最不可思议的崇高奇迹！"}
            ]
        }
    ]))

    # 8. 《漫威电影宇宙》(Marvel MCU) · 10 章全集
    courses.append(build_course({
        "id": "course-mov-marvel",
        "title": "《漫威电影宇宙》(Marvel MCU) · 超级英雄热血金句与终局史诗 (10章全集)",
        "category": "movies",
        "categoryName": "影视英语",
        "coverGradient": "from-red-600 via-rose-800 to-indigo-950",
        "icon": "🛡️",
        "description": "漫威十年无限传奇，从钢铁侠破茧成蝶到美队“复仇者集结”，用热血台词重温凡人之躯比肩神明。",
        "difficulty": "高级 C1",
        "tags": ["漫威宇宙", "复仇者联盟", "超级英雄", "热血台词"]
    }, [
        {
            "title": "第 1 幕 · 钢铁侠：我是托尼·斯塔克与凡人之躯",
            "description": "从自私的军火巨头到穿上铁甲守护世界，用凡人的智慧与血肉比肩神明。",
            "sentences": [
                {"en": "I am Iron Man, Tony Stark announced casually at the press conference, throwing away his prepared cue cards.", "cn": "我就是钢铁侠！在聚光灯闪烁的新闻发布会上，托尼·斯塔克随手潇洒扔掉了军方起草好的官方发言卡片，云淡风轻地向全世界宣示。"},
                {"en": "They say that the best weapon is the one you never have to fire; I respectfully prefer the weapon you only have to fire once.", "cn": "有人大言不惭宣称最精妙的威慑武器是那种永远无需开火的摆设；而我本人则由衷更推崇那种只需要狠狠开火一次就能彻底平定战局的雷霆神器！"},
                {"en": "In that dark Afghan cave, with a box of scraps and sheer mechanical genius, he forged his miniature arc reactor.", "cn": "在阿富汗那座暗无天日的阴冷潮湿山洞深处，仅仅凭借着一箱破烂废铁与巧夺天工的机械天才，他亲手为自己锻造出微型方舟反应堆心脏。"},
                {"en": "JARVIS, sometimes you gotta run before you can walk; initiate full thruster sequence now!", "cn": "贾维斯，有时候人要想学会从容走路，就必须先豁出命去大步奔跑；立刻给我全面点燃足底最大推力发射序列！"},
                {"en": "If we can't protect the Earth, you can be damned well sure we'll avenge it with everything we've got.", "cn": "倘若我们当真无法守护这颗美丽母星免遭践踏，那么老子向你郑重保证：我们必将倾尽全副身家性命，让侵略者血债血偿、百倍奉还！"},
                {"en": "My armor was never a distraction or a hobby; it was a cocoon, and now I'm a changed man.", "cn": "我打造的这具钢铁战甲，从来不是什么逃避现实的玩票或消遣闲暇爱好；它是一座让我脱胎换骨的生命之茧，而如今，我早已是一个崭新纯粹的男人。"},
                {"en": "You can take away my suits, my waterfront mansion, and all my fancy toys, but one thing remains true.", "cn": "你可以尽管蛮横剥夺走我名下所有的钢铁战衣，砸烂我的海滨豪华庄园，没收我所有炫酷昂贵的高科技玩具，但唯独有一条铁打的真理你休想抹杀。"},
                {"en": "A hero is not defined by the vibranium or titanium that encases his flesh, but by the fire in his soul.", "cn": "衡量一个真正英雄的崇高标尺，绝不在于包裹在他血肉之躯外层的是振金还是昂贵钛合金，而在于他灵魂深处熊熊燃烧不灭的正义烈火！"},
                {"en": "Following protocol has never kept the monsters in the dark from slaughtering innocent civilians.", "cn": "墨守成规地按部就班走官僚审批程序，可从来未能成功阻止过潜伏在黑暗深处的嗜血怪物去残酷屠戮无辜平民百姓。"},
                {"en": "Steve, you know that I respect you, but your blind optimism is going to get us all killed one day.", "cn": "史蒂夫，你心里清楚我一直由衷敬重你的为人，但你骨子里那种盲目幼稚的道德乐观主义，迟早有一天会把我们全副机组人员送上绝路。"},
                {"en": "I saw a cold wormhole opening in the black sky above Manhattan, raining alien leviathans down upon us.", "cn": "我曾在曼哈顿上空漆黑如墨的云层之巅，亲眼目睹一道冰冷虫洞凭空撕裂展开，将无数遮天蔽日的巨型外星机械利维坦暴风骤雨般倾泻向人间！"},
                {"en": "A suit of armor around the entire world is what we need to safeguard our fragile human future.", "cn": "唯有在整个地球的大气层外围铸就起一道坚不可摧的全球防御铁幕铠甲，才是捍卫我们脆弱人类文明未来的唯一救赎法宝！"},
                {"en": "He flew that nuclear warhead into the portal knowing full well that there was no return ticket.", "cn": "当年他双手托举着那枚足以毁灭城池的超重型战术核弹头义无反顾冲入异界虫洞时，心里比谁都清楚：这趟去路，根本就没有返程车票。"},
                {"en": "I don't trust a guy without a dark side; call me old-fashioned, but flawless saints don't exist.", "cn": "我向来本能地怀疑那些标榜自己浑身上下毫无阴暗面的道貌岸然之徒；就算笑我思想守旧也罢，这世上压根就不存在什么毫无瑕疵的圣洁圣人。"},
                {"en": "Tony Stark proved that a mortal mind armed with limitless courage can stare down the cosmos and prevail.", "cn": "托尼·斯塔克用自己滚烫的一生向全宇宙雄辩证明：一颗凡人之躯的聪慧头脑只要武装上无畏的浩然胆魄，便足以昂首俯瞰诸神浩瀚星河，傲然屹立不倒！"}
            ]
        },
        {
            "title": "第 2 幕 · 美国队长：我可以和你耗一整天",
            "description": "布鲁克林的瘦弱小子，用血肉之躯扛起星条旗圆盾，永不退缩的道德灯塔。",
            "sentences": [
                {"en": "I can do this all day, the bruised and bloodied Steve Rogers declared, raising his clenched fists again.", "cn": "我可以陪你这么耗上一整天！哪怕浑身被打得皮开肉绽、鼻青脸肿，瘦弱的史蒂夫·罗杰斯依然一次次顽强咬牙站起，再次扬起紧握的双拳。"},
                {"en": "The serum didn't just amplify his physical musculature; it magnified everything inside his righteous heart.", "cn": "超级士兵血清当年所大幅强化激发的，绝不仅仅只是他体表虬结暴起的强健肌肉群；它更是将他纯良正直心灵深处的所有美德放大了万倍。"},
                {"en": "A weak man knows the true value of strength, and knows what it means to feel profound compassion.", "cn": "一个曾经深切体验过弱小无助滋味的底层凡人，才真正懂得强大的宝贵分量，才真正明白对弱者怀揣深切悲悯究竟意味着什么。"},
                {"en": "Whatever happens tomorrow, promise me one thing: that you will stay who you are, not a perfect soldier, but a good man.", "cn": "无论明天的实验究竟会迎来怎样的结局，答应我唯一一件事：务必始终如一做你自己——绝不要沦为冷血完美的战争机器，而是做个堂堂正正的善良男儿！"},
                {"en": "The price of freedom is notoriously high, but it's a price that I am always willing to pay alone.", "cn": "在这个险恶世道上争取自由的代价向来昂贵高昂，但只要是为了捍卫公理，哪怕只有我孤身一人赴汤蹈火，我也心甘情愿照单全收！"},
                {"en": "Even if everyone is telling you that something wrong is something right, you plant yourself like a tree beside the river of truth.", "cn": "即便全世界所有权威口径都在异口同声把卑鄙勾当粉饰为绝对正义，你也必须如同一棵参天大树般死死扎根在真理的长河之畔！"},
                {"en": "You tell the whole arrogant world: No, you move!", "cn": "你要迎着狂风，掷地有声地向着傲慢的整个世界庄严宣告：不，该挪窝让路的，是你们！(美队经典信仰宣言)"},
                {"en": "When the government demanded everyone register and surrender autonomy, Rogers refused to sign the Sokovia Accords.", "cn": "当各方强权逼迫超级英雄全员签字交出行动自主权时，罗杰斯目光坚毅如铁，毅然决然拒绝在丧权辱格的《索科维亚协议》上签字妥协。"},
                {"en": "The safest hands are still our own; we cannot abdicate our personal moral responsibility to bureaucrats.", "cn": "这世上最安全、最值得托付性命的双手，永远是我们自己这双沾满老茧的手；我们绝不能把沉甸甸的个人良知责任，拱手让渡给冷血平庸的政客官僚。"},
                {"en": "Bucky has been brainwashed by Hydra assassins for decades, but deep beneath the winter soldier, he is still my brother.", "cn": "巴基虽然惨遭九头蛇余孽毫无人性的洗脑摧残整整半个世纪，但在那具冰冷的“冬日战士”杀人皮囊之下，他从始至终都是我同生共死的结拜手足兄弟！"},
                {"en": "I'm with you to the end of the line, pal, Rogers whispered softly as the helicarrier crashed into the Potomac River.", "cn": "我陪你并肩战斗直到生命轨迹的终点要道，老兄！当失控燃烧的重型空天母舰轰然解体坠向波托马克河时，罗杰斯抛弃盾牌轻声温言。"},
                {"en": "Before we get started on this mission, does anyone want to get out? he asked calmly inside the crowded elevator.", "cn": "在我们正式动手开打之前，请问在座的哪位识相的朋友想要体面出电梯离开？在逼仄密闭的拥挤电梯间里，他神色平静地环视九头蛇密探问道。"},
                {"en": "He threw himself onto an unexploded grenade during boot camp, proving his innate sacrificial valor.", "cn": "早在新兵入伍受训的第一周，当一枚冒着白烟的哑弹手榴弹滚落身侧时，他毫不犹豫飞身用单薄胸膛死死扑压上去，瞬间证明了他骨子里的自我牺牲勇气。"},
                {"en": "Compromise where you can, but where you can't, stand your ground with unrelenting moral courage.", "cn": "在能够求同存异的枝节末端上尽可宽宏让步，但在关乎原则大是大非的核心底线前，你必须怀揣着九死不悔的崇高道德风骨寸步不让！"},
                {"en": "Captain America was not a symbol of nationalist supremacy, but a timeless embodiment of human resilience.", "cn": "“美国队长”这面旗帜所承载的内核，从始至终绝非盲目狭隘的霸权图腾，而是全人类在狂风骤雨打击下百折不挠、誓死抗争的崇高精神丰碑！"}
            ]
        },
        {
            "title": "第 3 幕 · 雷神索尔与绿巨人浩克：阿斯加德与常驻怒火",
            "description": "阿斯加德不是一个地方，而是人民；那是我的秘密，队长，我随时都在发怒。",
            "sentences": [
                {"en": "Asgard is not a physical place; Asgard has always been where our surviving people stand united.", "cn": "阿斯加德从来就不是指宇宙星图上某一处具体的冰冷砖石疆域；只要我们大难不死的幸存同胞万众一心并肩伫立之处，那便永远是阿斯加德！"},
                {"en": "Are you Thor, the God of Hammers? Odin asked gently in a vision; that hammer was only meant to channel your lightning.", "cn": "难道你自命不凡是所谓的“锤子之神”吗，孩子？奥丁在虚幻幻境中慈爱地拷问道，那柄雷神之锤，当年不过只是用来引导约束你体内奔涌神力的凡尘法器罢了！"},
                {"en": "With blinding bolts of crackling blue plasma surging through his eyes, Thor unleashed the wrath of the heavens.", "cn": "伴随着狂暴刺目的湛蓝等离子体电弧在眼眶中汹涌翻滚奔腾，雷神索尔彻底觉醒，向着漫山遍野的死灵大军倾泻下天神裁决的苍穹狂怒！"},
                {"en": "Loki, you are a phenomenal schemer, but you will always be a petty trickster destined to fail.", "cn": "洛基，你确实是个算无遗策、手段通天的旷世阴谋大家，但你骨子里却永远只是个自私自利、注定在自作聪明中迎来败局的跳梁小丑。"},
                {"en": "I have lived for fifteen hundred years, slaughtered twice as many enemies, and yet this grief feels brand new.", "cn": "老子在浩瀚九界纵横驰骋活了整整一千五百年，手刃屠戮过的穷凶极恶之敌远超这个数目的两倍，然而此时此刻家破人亡的锥心之痛，却依旧痛彻心扉如初。"},
                {"en": "Dr. Banner, now might be a really good time for you to get angry! Captain America called out amidst the alien onslaught.", "cn": "班纳博士，眼下群魔乱舞的紧要关头，恐怕正是你大动肝火、大发雷霆的绝佳良机！美国队长在漫天外星机械巨兽咆哮声中扯着嗓子大喊。"},
                {"en": "That's my secret, Cap; I'm always angry, Bruce Banner replied calmly, transforming into the colossal emerald Hulk.", "cn": "那正是深藏在我心底的最大机密，队长：我从始至终，每分每秒都在狂暴盛怒之中！布鲁斯·班纳神色平静如水淡淡一笑，身躯骤然膨胀化作万夫莫开的擎天巨兽绿巨人！"},
                {"en": "Puny god! Hulk grunted in disgust, smashing the haughty villain repeatedly into the polished marble floor.", "cn": "好弱鸡的神！浩克满脸嫌弃地粗声咕哝了一句，抓起不可一世的傲慢反派脚踝，如摔打破麻袋般疯狂狠狠狂暴砸向光洁如镜的大理石地板！"},
                {"en": "The dual dichotomy between Bruce's gentle scientific intellect and Hulk's savage primal fury tormented him.", "cn": "布鲁斯体内温文尔雅的博学科学家理智，与浩克那毁天灭地的蛮荒野性原始狂怒之间不可调和的剧烈冲突，无时无刻不在折磨撕裂着他的灵魂。"},
                {"en": "I don't want to hurt anybody, but when the monster breaks out of the cage, collateral damage is inevitable.", "cn": "我从始至终绝不想伤害无辜苍生，但一旦关押在心底的暴戾巨兽撕破牢笼破壁而出，毁天灭地的战火余波便注定无可挽回地降临人间。"},
                {"en": "Bring me Thanos! Thor thundered as the bifrost beam blasted through the clearing in Wakanda.", "cn": "把灭霸那厮给我揪出来受死！当璀璨炫目的彩虹桥神圣光柱轰然撕裂瓦坎达战场的焦土长空时，雷神索尔手持暴风战斧破空咆哮怒喝！"},
                {"en": "The Stormbreaker ax sheared through incoming energy blasts like a fiery comet of divine retribution.", "cn": "暴风战斧呼啸盘旋飞驰，宛如一颗携带着天罚神罚的熊熊燃烧彗星，势如破竹般硬生生劈开了迎面轰击而来的毁灭性能量光束。"},
                {"en": "You should have gone for the head! the mad titan rasped with blood trickling down his chest.", "cn": "你刚才那一斧头……本来应该对准老子的项上人头砍下来的！满身横肉的疯狂泰坦灭霸任凭胸膛鲜血狂涌，嘴角泛起残忍冷笑嘶哑嗤笑道。"},
                {"en": "Losing everything he loved drove the thunder god into deep depression and solitary guilt.", "cn": "亲眼看着至亲骨肉与神域子民在眼前接连横死殒命，这位昔日不可一世的天神彻底跌入了重度抑郁与痛彻心扉的深不见底内疚深渊。"},
                {"en": "True strength is not measured in physical brawn, but in the humility to stand back up after failing catastrophically.", "cn": "衡量一个人真正的硬汉力量，绝不在于浑身暴起的蛮力肌肉，而在于遭遇了灾难性惨败之后，依然能有勇气在废墟泥泞中重新站直脊梁！"}
            ]
        },
        {
            "title": "第 4 幕 · 奇异博士与灭霸：千万人选其一的胜率",
            "description": "十四百万零六百零五次时间线推演，只有一个结局能够让人类彻底逆风翻盘。",
            "sentences": [
                {"en": "I went forward in time to view alternate futures, Doctor Strange revealed with trembling hands.", "cn": "我动用了时间宝石的神力，在意识流中强行逆流前往未来，全面推演审视了所有的平行时间线结局，奇异博士双手发颤面色惨白地缓缓透露。"},
                {"en": "How many did you see? Fourteen million, six hundred and five. How many do we win? Exactly one.", "cn": "你一共推演看到了多少种未来？整整一千四百万零六百零五种。……那我们一共赢了多少次？——唯独只有区区一次！"},
                {"en": "Dormammu, I've come to bargain! Stephen Strange declared inside an endless temporal loop.", "cn": "多玛姆，老子今天是特意来找你谈判讲道理的！斯特兰奇在被死死锁定的无限时间闭环回廊深处，面对不可名状的黑暗主宰从容不迫地宣誓宣战。"},
                {"en": "Pain is an illusion; death is a minor setback when you command the mystical Eye of Agamotto.", "cn": "肉体承受的剧痛不过是区区虚幻的神经电流幻觉；当你能从容执掌阿戈摩托之眼的至高奥秘时，肉身的死亡不过是一场随时可以推倒重来的微小挫折。"},
                {"en": "Thanos believed that the universe's resources were strictly finite while biological population expanded exponentially.", "cn": "灭霸那偏执疯狂的末日世界观坚信：整个宇宙蕴藏的生存资源在总量上是绝对有限的，而大千生灵的繁衍扩张速度却是呈指数级暴增的。"},
                {"en": "The hardest choices require the strongest wills, the purple warlord mused, staring down at the ruins of his homeworld.", "cn": "在这大千宇宙之中，最艰难残酷的终极历史抉择，往往需要最铁石心肠、最刚毅果决的无上意志去亲手推行！这位紫色霸主伫立在母星废墟之巅喃喃自语。"},
                {"en": "With all six Infinity Stones glowing upon the golden gauntlet, I could simply snap my fingers and half of life ceases to exist.", "cn": "只要将全部六颗无限原石齐聚于黄金铸造的手套之上，老子只需要轻轻打一个清脆响指，全宇宙半数的生灵便会在刹那间化作历史尘埃！"},
                {"en": "I call that cosmic mercy, not cruelty; it is the only path toward permanent celestial balance.", "cn": "老子将这种大刀阔斧的壮士断腕义举称之为浩瀚的宇宙级慈悲，而非残暴杀戮；这是引领万物苍生迈向永恒生态平衡的唯一救赎之道！"},
                {"en": "You're a monster who slaughtered my people and threw your own daughter into the Soul Stone abyss!", "cn": "你是个彻头彻尾灭绝人性的恶魔屠夫！你血腥屠戮了我的全部族人，甚至连你亲生养育的女儿，都被你亲手推下悬崖摔得粉身碎骨当了祭品！"},
                {"en": "The snap of his gauntlet unleashed a deafening thunderclap, and across the globe, heroes turned into drifting ash.", "cn": "伴随着那只镶嵌满宝石的手套清脆一响，一声震碎万界的惊天霹雳炸响，放眼全球，无数叱咤风云的英雄豪杰刹那间身躯沙化、随风飘散化为漫天飞灰！"},
                {"en": "Mr. Stark? I don't feel so good, Peter Parker whimpered, clutching Tony's coat as his legs dissolved into dust.", "cn": "斯塔克先生？……我感觉浑身好难受、好不舒服，小蜘蛛彼得·帕克大眼睛里噙满泪水哽咽抽泣，死死抓着托尼的大衣下摆，而他的双腿却正无可挽回地消散成虚无的灰尘。"},
                {"en": "I don't wanna go, sir, please, I don't wanna go, the teenager pleaded before blowing away into the quiet wind.", "cn": "求求您先生，我还不想死……我真的还不想走，这名年仅十六岁的高中生在彻底随风飘散在冷风中之前，发出了人世间最绝望无助的哀求。"},
                {"en": "Tony knelt in the alien red dirt, staring at his empty, ash-covered palms in deafening, traumatized silence.", "cn": "托尼整个人失魂落魄地重重跪倒在外星猩红色的泥土之中，呆呆凝视着自己沾满灰白色余烬的空荡荡双手，陷入了痛彻骨髓、震耳欲聋的心灵死寂。"},
                {"en": "We lost, all of us; we lost family, we lost friends, and we lost a piece of our very humanity.", "cn": "我们全盘皆输了，彻底一败涂地；我们失去了血肉至亲，我们失去了肝胆相照的挚友，我们甚至在这场浩劫中，永远丧失了我们人性中最珍贵的部分。"},
                {"en": "Strange handed over the Time Stone willingly, knowing that Tony Stark had to survive for that solitary one chance.", "cn": "当年奇异博士之所以心甘情愿主动奉上时间宝石，是因为他在冥冥之中早已算准：托尼·斯塔克必须活下去，那是换取未来绝地翻盘唯一希望的先决筹码！"}
            ]
        },
        {
            "title": "第 5 幕 · 终局之战：复仇者，集结！",
            "description": "集结十年漫威全体英雄，向灭霸大军发起冲锋；爱你三千遍，凡人比肩神明。",
            "sentences": [
                {"en": "Five years after the catastrophic decimation, Scott Lang emerged from the quantum realm with a spark of hope.", "cn": "在那场毁灭半数生灵的大浩劫整整漫长五年之后，“蚁人”斯科特·朗奇迹般从微观量子领域脱困而出，带来了彻底扭转历史的希望火种。"},
                {"en": "Time travel via the quantum realm was no longer comic book fantasy; it was our desperate scientific Hail Mary.", "cn": "借助量子领域的奇妙隧道实现跨时空穿梭，从此不再是虚妄荒诞的漫画科幻假想；它是全人类在穷途末路之际搏命一击的绝地科学豪赌！"},
                {"en": "Natasha Romanoff made the ultimate sacrifice at the cliff of Vormir so Clint Barton could bring the Soul Stone home.", "cn": "在沃米尔星那道深不见底的万丈深渊绝壁之畔，“黑寡妇”娜塔莎毅然决然做出了决绝的终极牺牲，只为让鹰眼能够把灵魂宝石活着带回地球。"},
                {"en": "Captain America stood alone amidst the smoldering debris of the compound, tightening the strap on his broken shield.", "cn": "美国队长孑然一身傲然伫立在化作废墟焦土的基地残垣断壁中央，紧咬牙关，极其冷静地伸手勒紧了紧缚在臂膀上那面早已被砍裂劈碎的半截破盾。"},
                {"en": "Across the smoking battlefield, Thanos's vast alien armada descended like an apocalyptic horde of locusts.", "cn": "在硝烟弥漫的开阔地平线彼端，灭霸麾下那支遮天蔽日、一眼望不到尽头的浩瀚外星异族侵略大军，如末日蝗虫风暴般铺天盖地压境而来。"},
                {"en": "Suddenly, static crackled through his radio earpiece, followed by a voice: Cap, can you hear me? On your left.", "cn": "千钧一发之际，一阵滋啦作响的无线电静电杂音骤然划破死寂，紧接着耳麦里传来一声无比熟悉的轻笑：队长，能听见我说话吗？——看你的左后方！"},
                {"en": "Colossal glowing spark circles carved through the dark sky as Doctor Strange opened mystical portals across the universe.", "cn": "一道道金光四射、流光溢彩的璀璨魔法传送火花圆环狂暴撕裂漆黑天穹，奇异博士联手各大法师，在全宇宙不同维度之间强行架设起了神圣的跃迁长廊！"},
                {"en": "Out stepped T'Challa, Shuri, the Wakandan armies, the Guardians of the Galaxy, Spider-Man, and legions of Sorcerers.", "cn": "黑豹特查拉陛下、苏睿公主、瓦坎达皇家禁卫军、银河护卫队全员、身手敏捷的小蜘蛛，以及成千上万各怀绝技的秘法师大军迈着雷霆步伐阔步踏出！"},
                {"en": "Every hero who had turned to dust five years ago had returned, standing shoulder to shoulder for one final stand.", "cn": "五年前在那场灾难中化作漫天飞灰的所有英雄豪杰，如今全员浴血归来，肩并肩筑起了一道横亘在天地之间坚不可摧的无敌血肉长城！"},
                {"en": "The shattered hammer Mjolnir flew across the air and slammed firmly into Steve Rogers' worthy grip.", "cn": "雷神之锤“妙尔尼尔”发出尖锐破空的呼啸之声，如一道银白闪电划破长空，稳稳当当落入了真正配得上执掌它的史蒂夫·罗杰斯掌心！"},
                {"en": "Steve drew a breath, summoned the lightning to crackle across the hammer, and whispered the immortal command.", "cn": "史蒂夫深吸一口满是硝烟与热血的冷冽空气，引动九天雷霆在雷神锤周身狂暴跃动共鸣，随后向着全宇宙英雄沉稳低吼出那句名垂青史的神圣指令："},
                {"en": "AVENGERS... assemble! he roared, leading the charge as thousands of warriors surged forward in a roaring tidal wave.", "cn": "复仇者……集结！他拔剑怒吼如平地春雷炸响，率领着身后数以万计的英雄战士如排山倒海般的滔天巨浪，怒吼着向着强敌席卷冲锋！"},
                {"en": "Tony Stark lunged at Thanos, wrestling for the Infinity Gauntlet and deftly absorbing the six stones into his nano-armor.", "cn": "在生死存亡的最后关头，托尼·斯塔克舍生忘死猛扑向灭霸，在殊死争夺扭打之间，神不知鬼不觉地运用纳米战甲将六颗原石尽数吸纳转移至自己右手！"},
                {"en": "Thanos snapped his naked fingers with a smug grin: I am inevitable. Nothing happened.", "cn": "满脸得瑟狞笑的灭霸傲慢地打响了空空如也的食指并宣称：老子就是天命所归！——然而四周一片死寂，什么都没有发生。"},
                {"en": "Tony raised his armored right hand, raw cosmic energy burning through his flesh, and whispered: And I... am... Iron Man.", "cn": "托尼缓缓抬起了那只被六颗原石狂暴宇宙能量严重灼伤撕裂的右手，直视仇敌的冷酷双眸，一字一顿从容低语道：而我……就是……钢铁侠！"},
                {"en": "SNAP! The blinding flash erased Thanos and his armies into smoke; Tony slumped against the debris, breathing his final breath.", "cn": "啪！一声清脆响指！璀璨刺目的圣光瞬间将不可一世的灭霸大军彻底吹散为虚无灰烬；托尼耗尽了生命最后一丝气力，平静瘫坐在废墟残垣旁，安详闭上了双眼。"},
                {"en": "Pep sat beside him, gently kissing his cheek: You can rest now, Tony. The heart in the metallic arc reactor finally went dark.", "cn": "小辣椒跪坐在他身畔，泪如雨下却温存地亲吻着他的脸颊：你终于可以好好休息了，托尼。胸膛金属方舟反应堆里那颗搏动了十年的炽热机械心脏，终于缓缓熄灭了光芒。"},
                {"en": "At his funeral, a small hologram of Tony smiled at his little daughter Morgan: I love you three thousand.", "cn": "在他的湖畔葬礼上，托尼生前录制的一段微型全息投影微笑着注视着年幼的小女儿摩根，温情道出那句感动全球的告别：宝贝，我爱你三千遍。"}
            ]
        },
        {
            "title": "第 6 幕 · 银河护卫队：星爵的金曲磁带与我是格鲁特",
            "description": "废柴天团横行宇宙，卡带金曲、话痨浣熊与用生命构筑护盾的树人格鲁特。",
            "sentences": [
                {"en": "Peter Quill pressed play on his vintage Sony Walkman, dancing across the alien ruins of Morag to seventies rock.", "cn": "彼得·奎尔熟练按下了他那台古董索尼随身听的播放键，伴随着七十年代激昂欢快的经典摇滚旋律，独自一人在外星荒凉废墟莫拉格的石阶上骚气摇摆起舞。"},
                {"en": "I'm Star-Lord, man! Legendary outlaw? Guys, Quill protested when nobody recognized his self-invented moniker.", "cn": "老子可是大名鼎鼎的星爵啊，兄弟！名震全宇宙的传奇通缉大盗好吗？！当外星佣兵们满脸懵逼没人认得出他时，奎尔急赤白脸地为自己那响亮的外号抗议辩解。"},
                {"en": "Rocket Raccoon adjusted his oversized laser cannon, cursing that he was not a rodent, but a biomechanical marvel.", "cn": "火箭浣熊骂骂咧咧调整着那门比他身高还宽一倍的巨型激光重炮，气急败坏申明：老子绝不是什么卑贱的老鼠啮齿动物，老子是巧夺天工的生物机械奇迹！"},
                {"en": "I am Groot, the gentle wooden colossus rumbled softly, extending a blooming twig of flowers to a crying orphan child.", "cn": "我是格鲁特！这尊温柔憨厚的参天木质树人巨兽发出沉稳浑厚的咕噜低鸣，从指尖缓缓绽放抽出一枝粉白相间的小野花，温情递向眼前哭泣抽泣的外星孤儿。"},
                {"en": "Drax the Destroyer took every metaphor completely literally: Nothing goes over my head; my reflexes are too fast, I would catch it.", "cn": "“毁灭者”德拉克斯从始至终把这世间所有的修辞隐喻当成字面大白话来较真：没有什么东西能从我头顶飞过！我的神经反射太迅捷敏锐了，我随手凌空就能一把接住它！"},
                {"en": "Gamora drew her lethal blade, reminding the dysfunctional crew that they were wanted by Nova Corps across the Andromeda Galaxy.", "cn": "卡魔拉寒光一闪拔出了随身佩戴的致命短刃，面若冰霜提醒这群极度不靠谱的奇葩搭档：新星军团的通缉令早已贴满了仙女座星系的每一个主要空港！"},
                {"en": "When the dark asteroid vessel plunged into Xandar, Groot wrapped his living wooden branches into an impenetrable protective sphere.", "cn": "当罗南庞大的暗黑星舰呼啸坠毁撞向山达尔母星地表时，树人格鲁特毫不犹豫将自己鲜活的血肉枝桠疯长蔓延，化作一座坚不可摧的终极球形防护牢笼。"},
                {"en": "Groot, why are you doing this? You're going to die! Rocket sobbed with real tears streaming down his furry muzzle.", "cn": "格鲁特，你疯了吗？！你为什么要这么做？！你会当场粉身碎骨灰飞烟灭的！火箭浣熊大颗大颗滚烫的泪水止不住地滑落过毛茸茸的吻部痛哭失声。"},
                {"en": "Groot gently wiped away the tear with a leafy thumb, whispering his very first new sentence: WE... ARE... GROOT.", "cn": "格鲁特生满嫩绿树叶的拇指温存擦去了挚友眼角的泪珠，在他漫长的一生中破天荒头一次轻声改口吐露出一句全新的神圣箴言：我……们……是……格鲁特！"},
                {"en": "The explosion disintegrated the outer canopy into millions of glowing amber embers, saving every member of the team.", "cn": "惊天动地的解体大爆炸瞬间将树人的外层躯干炸成了漫天飞舞、如梦似幻的无数金黄余烬，却用自己的粉身碎骨保全了飞船内每一个并肩作战的至亲伙伴。"},
                {"en": "Quill planted a splintered wooden twig into a pot of soil, and weeks later, a tiny baby Groot was dancing to the Jackson 5.", "cn": "奎尔心细如发地将一截残存的开裂树枝小心插进陶土花盆里细心浇水，数周之后，一个娇小玲珑的可爱小树人格鲁特已经在花盆里伴着杰克逊五兄弟的金曲欢畅扭腰扭胯了！"},
                {"en": "We may be a bunch of jackasses standing in a circle, but the galaxy isn't going to save itself.", "cn": "或许咱们这群人平日里看起来就是一帮围成一圈互相掐架的蠢货混球，但这浩瀚星河的无数苍生可不会凭空自己拯救自己！"},
                {"en": "Quill opened the gift his dying mother gave him decades ago: Awesome Mix Volume Two on a pristine magnetic cassette.", "cn": "奎尔终于鼓起勇气拆开了三十年前母亲临终前留给他的神圣遗物：一盒用崭新磁带精选录制的名垂影史的《劲歌金曲第二辑》！"},
                {"en": "Ain't no mountain high enough to keep this cosmic found family from watching each other's backs through eternity.", "cn": "这大千星辰大海之中，没有任何一座崇山峻岭能够阻隔阻挡这支拼凑而成的宇宙家人，在永恒时空之中誓死为彼此镇守后方脊背！"},
                {"en": "The Guardians soared into the star-sprinkled abyss, ready to steal batteries, bicker loudly, and protect the innocent.", "cn": "银河护卫队的飞船轰鸣着跃迁扎入繁星点缀的深邃虚空深处，时刻准备着去偷盗高能电池、去扯着嗓子日常斗嘴，以及去舍命守护这世间最纯真的公理！"}
            ]
        },
        {
            "title": "第 7 幕 · 蜘蛛侠：能力越大，责任越大",
            "description": "皇后区的好邻居高中生，在失去至亲与自我牺牲中真正理解责任的重量。",
            "sentences": [
                {"en": "Peter Parker was just an awkward, nerdy high school kid from Queens trying to pass his algebra exams.", "cn": "彼得·帕克原本只是纽约皇后区一个性格内向木讷、成天为代数期末考试焦头烂额的高中理科小书呆子。"},
                {"en": "A single bite from a genetically altered radioactive spider rewrote his DNA, gifting him superhuman agility.", "cn": "然而一只经过基因改造的放射性变异蜘蛛落下的致命一口，瞬间改写了他体内的全部DNA双螺旋链，赋予了他超乎凡胎的惊人敏捷与壁虎神力。"},
                {"en": "With great power comes great responsibility, Uncle Ben had imparted just days before his tragic murder in the street.", "cn": "能力越大，肩头背负的责任就越重！本叔叔在街头遭遇惨无人道的枪杀惨剧前夕，曾深情而庄重地向他传授了这句铭刻一生的传世座右铭。"},
                {"en": "When you can do the things that I can, but you don't, and then the bad things happen, they happen because of you.", "cn": "当你明明拥有能够力挽狂澜的超凡能力却选择作壁上观袖手旁观，随后不幸的惨剧在世间发生时，那么那场悲剧的发生，你难辞其咎！"},
                {"en": "Tony Stark recruited the boy by tracking him down to his cramped apartment, admiring his homemade web-shooters.", "cn": "托尼·斯塔克顺藤摸瓜一路精准追踪到了他逼仄狭小的小公寓里，满怀赞赏地亲自检验打量着这个少年自制的简陋蛛丝发射器。"},
                {"en": "If you're nothing without that advanced Stark Industries suit, Peter, then you shouldn't have it in the first place.", "cn": "彼得，倘若剥离了那套斯塔克工业倾囊打造的高科技战甲之后你本人便一文不值、毫无担当，那么你从一开始就根本不配穿上它！"},
                {"en": "Trapped beneath tons of crushing concrete rubble, the young hero cried out in darkness before finding his inner reserve of grit.", "cn": "被死死压在重达数吨坍塌粉碎的钢筋混凝土废墟阴暗深处，年仅十五岁的少年英雄曾绝望哭喊呼救，直到他在灵魂深处重新点燃了那团不屈的坚毅火种。"},
                {"en": "He hoisted the impossible slab off his spine with trembling sinews, proving that the heart makes the hero, not the cloth.", "cn": "凭借着浑身颤抖暴起的血肉筋骨，他咆哮着硬生生从脊梁上扛起了那块看似绝无可能掀翻的万斤巨石，向天地雄辩证明：锻造真正英雄的内核是炽热的心灵，而非昂贵的战甲布料！"},
                {"en": "He fought the Vulture on the wing of a stealth cargo jet, saving the lives of the very villains who sought his destruction.", "cn": "他在隐形货运客机的巨大机翼之巅与凶残的反派秃鹰殊死搏杀，却在最后关头冒着机毁人亡的危险，拼死救下了那个千方百计想要置他于死地的仇敌性命。"},
                {"en": "I'm just your friendly neighborhood Spider-Man, ma'am, he waved politely to a neighborhood bodega owner.", "cn": "阿姨您太客气了，我不过只是咱们皇后区街坊邻里身边随处可见的热心好邻居“蜘蛛侠”罢了！他礼貌地向街边杂货铺老板挥手致意。"},
                {"en": "In the multiverse crisis, three generations of Peter Parkers stood atop the Statue of Liberty, curing their historical adversaries.", "cn": "在波澜壮阔的多元宇宙危机交汇时刻，横跨整整二十年的三代蜘蛛侠破天荒并肩伫立在自由女神像之巅，携手用智慧救赎治愈了他们各自宿命中的全部强敌！"},
                {"en": "Aunt May sacrificed her life, repeating the immortal words: with great power, there must also come great responsibility.", "cn": "梅姨在浩劫中献出了她宝贵的生命，在临终之际再次深情回响起了那句不朽的神圣名言：孩子，能力越大，肩头就必须扛起同等沉重的崇高责任！"},
                {"en": "To heal the fractured fabric of reality, Peter asked Doctor Strange to cast a spell erasing him from everyone's memory.", "cn": "为了彻底缝合修补即将分崩离析的宇宙现实裂痕，彼得毅然决然恳求奇异博士施展终极遗忘魔咒，将他存在过的所有痕迹从全宇宙所有挚爱之人的记忆中彻底抹去。"},
                {"en": "Ned and MJ no longer knew his face, yet he walked away into the snowy Manhattan night with quiet, selfless resolve.", "cn": "死党内德与一生挚爱MJ再也认不出他眼前这张满是疲惫的面孔，但他却将眼泪咽进肚里，怀揣着无私决绝的从容大义，悄然转身隐没在漫天飞雪的曼哈顿寒夜深处。"},
                {"en": "Sewing a new red-and-blue suit on a cheap thrift machine, the solitary protector swung into the skyscrapers to defend his city.", "cn": "用一台廉价的二手老旧缝纫机亲手缝制出一套朴素经典的崭新红蓝战衣，这位举目无亲、一无所有的孤独守护者如流星般凌空荡向摩天大楼林立的城市天际线，去捍卫他深爱的家园！"}
            ]
        },
        {
            "title": "第 8 幕 · 黑豹特查拉：瓦坎达万岁与科技大同",
            "description": "隐匿非洲的超科技文明，打破闭关锁国，将振金与和平智慧分享给全人类。",
            "sentences": [
                {"en": "Hidden behind an impenetrable holographic cloaking shield in East Africa lay the wondrous golden kingdom of Wakanda.", "cn": "在东非广阔莽原深处一座坚不可摧的巨型全息隐形力场屏障掩映之下，静静隐匿着一座令人叹为观止、兼具古老传统与超级科技的黄金国度——瓦坎达。"},
                {"en": "Vibranium is not merely an indestructible space-age metal; it is the miraculous lifeblood of their entire civilization.", "cn": "天外陨石带来的神奇“振金”绝不仅仅只是一种无坚不摧的稀世太空合金；它是滋养灌溉整个瓦坎达文明腾飞繁荣的奇迹血脉源泉。"},
                {"en": "In my culture, death is not the end; it's more of a stepping-off point to the ancestral ancestral plane.", "cn": "在我们瓦坎达悠久的文化传统之中，肉体的死亡从来不是生命的终点；它更像是一处从容迈向彼岸、与列祖列宗英灵长相厮守的崭新精神起点。"},
                {"en": "T'Challa consumed the heart-shaped herb, communing with the spirits of ancient panther monarchs beneath the aurora skies.", "cn": "特查拉庄严服下了神圣的心形草神药，在泛着极光紫芒的神圣星空草甸之上，与历代黑豹先王不朽的崇高英灵展开了跨越维度的深邃灵魂对话。"},
                {"en": "A wise man builds bridges in times of crisis, while the foolish and arrogant man builds walls of isolation.", "cn": "放眼古往今来，每当时代的大危机与大变革降临时，胸怀天下的明达智者选择广修沟通互鉴的友谊大桥；而愚蠢傲慢之徒，却只会一味构筑壁垒森严的封闭高墙！"},
                {"en": "Killmonger brought a furious challenge of generational rage, demanding the empire arm the oppressed worldwide with vibranium.", "cn": "流落异邦多年的堂弟“杀人魔头”携带着世代积压的滔天怒火杀回王都，厉声质问控诉为何坐拥绝世神兵却闭门锁国，勒令向全球受苦苍生倾囊分发振金大炮！"},
                {"en": "You were wrong all of you! T'Challa shouted at the spirit of his father; we turned our backs on the world out of fear!", "cn": "你们所有人都做错了！当年所有人都犯下了历史大错！特查拉在英灵殿前向着父王的虚影掷地有声地痛斥咆哮：我们当年纯粹是因为骨子里的恐惧自私，才冷血背弃了外面水深火热的人世间！"},
                {"en": "I will not let your mistakes decide who I am; I will right this wrong for the sake of future generations.", "cn": "我绝不允许你们当年犯下的历史过失来框定我的道德人格！为了千秋万代的无辜子孙，我特查拉必将在我的任期内彻底匡正这一长达数世纪的错误！"},
                {"en": "The Dora Milaje warriors locked their vibranium spears in unison, chanting their fierce loyalty to the rightful throne.", "cn": "皇家女子亲卫队“朵拉·米拉洁”的英勇女战士们整齐划一将手中的振金长矛狠狠杵向岩石地面发出金石轰鸣，齐声高唱着誓死效忠天命正统王座的铿锵战歌！"},
                {"en": "WAKANDA FOREVER! King T'Challa bellowed with his arms crossed in royal salute, charging headlong into the fray.", "cn": "瓦坎达万岁！特查拉国王双臂在胸前交叉摆出神圣的黑豹王室十字战礼，放声暴喝，如同一头威风凛凛的黑色矫健猎豹率先扑入敌阵血肉拼杀！"},
                {"en": "He disarmed his radical cousin atop the high-speed maglev tracks, refusing to execute him in cold, vengeful blood.", "cn": "在呼啸飞驰的真空超导磁悬浮列车轨道之巅，他精准卸掉了激进堂弟的杀人凶刃，却无论如何也坚决拒绝带着冷酷复仇的嗜血去残忍处决自己的至亲骨肉。"},
                {"en": "Bury me in the ocean with my ancestors who jumped from the slave ships, Killmonger whispered, because they knew death was better than bondage.", "cn": "把我安葬在浩瀚大洋深处吧，去陪伴那些当年宁可毅然纵身跳下贩奴黑船的勇敢先祖们，堂弟在弥留之际虚弱吐露，因为他们心里比谁都清楚：死亡，远胜于屈辱苟活在冰冷镣铐之中！"},
                {"en": "Standing before the United Nations assembly, King T'Challa announced that Wakanda would share its knowledge and resources globally.", "cn": "巍然伫立在联合国大会的全球聚光灯讲台之前，特查拉国王庄严向全世界郑重宣布：瓦坎达从此将全面向全人类开放共享其所有的顶尖科学智慧与发展资源！"},
                {"en": "More connects us than separates us; we must find a way to look after one another as if we were one single tribe.", "cn": "在浩瀚苍穹之下，将我们大千生灵紧紧联系在一起的共同羁绊，远胜于那些人为制造的狭隘隔阂；我们必须学会像守护同一个古老部落那样，彼此休戚与共、倾情守望！"},
                {"en": "Chadwick Boseman's radiant legacy as the Black Panther will shine across generations of young dreamers forever.", "cn": "查德维克·博斯曼所塑造的黑豹王者形象与崇高人格光辉，必将如同夜空中最耀眼的璀璨北极星般，世代长久照亮无数胸怀凌云壮志的年轻梦想家！"}
            ]
        },
        {
            "title": "第 9 幕 · 绯红女巫与幻视：爱与悲伤的深刻哲思",
            "description": "如果悲伤不是爱的延续，那它又会是什么？混沌魔法与西景镇的虚幻心碎。",
            "sentences": [
                {"en": "Wanda Maximoff was forged in the furnace of grief, having lost her parents to Stark manufactured missiles in Sokovia.", "cn": "旺达·马克西莫夫整个人生轨迹完全是在刻骨铭心的丧亲剧痛熔炉中千锤百炼锻造而成的；年仅十岁时，斯塔克工业制造的炸弹在索科维亚无情夺走了她双亲的性命。"},
                {"en": "Vision was not merely an artificial synthetic android; he was a philosophical entity powered by the Mind Stone.", "cn": "幻视绝不仅仅只是一具由冰冷人造组织合成的生化仿生人；他是一个头顶镶嵌着心灵宝石、日夜苦苦探寻生命崇高真谛的真正哲学智者。"},
                {"en": "I have never eaten a meal or slept a night, Vision mused, yet I feel a profound human yearning when I look at you.", "cn": "我漫长一生中从未真正吃过一顿热饭，也从未经历过一晚香甜的睡眠，幻视神色温柔地凝视着她呢喃道，然而每当我深情凝望你的眼眸时，我体内却真切翻涌起一股做梦般的人类向往。"},
                {"en": "In the quiet corners of the Avengers facility, they cooked paprikash and found solace in shared solitude.", "cn": "在复仇者联盟基地远离喧嚣的僻静厨房一角，他们曾并肩耐心地慢炖着家乡风味的红椒鸡，在彼此惺惺相惜的孤独之中觅得了灵魂最安详的宁静慰藉。"},
                {"en": "You could never hurt me, Wanda; I only feel you, Vision comforted her as she was forced to shatter the stone in his forehead.", "cn": "你这一生绝不可能真正伤害我分毫，旺达；在我的感知系统里，我此刻感受到的全部唯独只有你，当旺达被迫含泪施法摧毁他额头的心灵宝石时，幻视温存宽慰道。"},
                {"en": "She had to execute the love of her life with her own magical hands, only to watch Thanos rewind time and slaughter him again.", "cn": "她不得不亲手用自己的魔法将一生挚爱当场粉碎处决，然而转瞬之间，残忍的灭霸却悍然拨动时间倒流，当着她的面将复活的爱人再次残暴捏死！"},
                {"en": "What is grief, if not love persevering? Vision had once asked her during a rainy afternoon in the quiet bedroom.", "cn": "如果直面失去的无尽悲伤不是深沉爱意在苦难岁月中顽强不屈的坚毅延续，那它在这人世间又还能算作什么呢？在昔日一个阴雨连绵的宁静午后，幻视曾轻声向她发问。"},
                {"en": "That singular line of poignant philosophical poetry captured the eternal beauty and agony of human affection.", "cn": "那句字字泣血、精妙绝伦的哲学诗性箴言，瞬间精准击中了人类情感深处既美好绝伦又痛彻骨髓的终极宿命二重性。"},
                {"en": "Consumed by absolute despair, Wanda's untapped chaos magic erupted, warping reality across the entire suburban town of Westview.", "cn": "当直面爱人冰冷解剖图纸的那一刹那，旺达的心智被滔天的绝望彻底吞噬，她体内沉睡已久的混沌魔法狂暴爆发，凭空将整个西景镇强行改写成了上世纪复古情景喜剧的幻境！"},
                {"en": "She fabricated a perfect domestic suburban paradise with white picket fences, two twin boys, and a resurrected Vision.", "cn": "她凭借不可思议的造物伟力，硬生生编织出了一座带有白色木栅栏小洋房、一对活泼双胞胎男孩以及爱人奇迹般重生的无瑕温馨世外桃源。"},
                {"en": "You are my sadness and my hope, but mostly, you're my love, Wanda whispered as the mystical hex boundary began to disintegrate.", "cn": "你是我生命中无法言说的至深哀伤，你也是我照亮人生的微弱希望，但归根结底，你从始至终都是我全心全意深爱的男人！当结界光幕缓缓化为飞灰消散时，旺达泪流满面轻吻道。"},
                {"en": "We have said goodbye before, so it stands to reason that we will say hello again, Vision smiled serenely before fading into light.", "cn": "在此之前，我们也曾依依不舍经历过撕心裂肺的诀别，所以按照严密的逻辑推论：在未来的某一天，我们必定会在这世间的某个角落再次相逢微笑道声你好，幻视在彻底化作纯白光粒子消散前从容微笑道。"},
                {"en": "The Darkhold corrupted her grief-stricken soul, transforming the tragic mourning widow into the terrifying Scarlet Witch.", "cn": "古代黑魔法典籍《黑暗神书》的至邪魔力无情侵蚀了她那颗饱受摧残的悲伤灵魂，硬生生将这位凄惨哀恸的未亡人，腐化成了血洗多元宇宙、令人闻风丧胆的恐怖“绯红女巫”！"},
                {"en": "She tore through alternate universes searching for her fictional children, only to realize she had become the ultimate nightmare.", "cn": "她不惜大开杀戒踏碎无数平行宇宙的现实屏障，只为苦苦寻觅那对并不存在的虚构孩儿，直到孩子眼中流露出对她滔天的恐惧时，她才如梦方醒惊觉自己早已沦为了全宇宙最可怕的梦魇恶魔。"},
                {"en": "With a final tragic act of redemption, Wanda brought down the dark throne of Wundagore mountain upon herself, burying the evil forever.", "cn": "怀揣着绝望生命最后的救赎微光，旺达亲手引爆轰塌了万达格山顶的黑暗神殿王座，甘愿将自己与世间所有的至邪典籍永远深埋在万丈巨石废墟之下。"}
            ]
        },
        {
            "title": "第 10 幕 · 洛基的体面救赎与多元宇宙的永恒王座",
            "description": "恶作剧之神不再追求统治凡人，而是牺牲自身永恒自由，用双手编织时间之树。",
            "sentences": [
                {"en": "Loki began his journey as the arrogant adopted frost giant prince who constantly plotted against his brother Thor.", "cn": "洛基的整个人生篇章，始于一个自命不凡、心胸狭隘的冰霜巨人遗孤王子身份，他在嫉妒与自卑的泥潭中日夜处心积虑算计着兄长雷神索尔。"},
                {"en": "I am burdened with glorious purpose! he famously declared, commanding the terrified citizens of Stuttgart to kneel before him.", "cn": "我生来便肩负着光荣伟大的神圣使命！在德国斯图加特的广场之上，他手持心灵权杖傲然俯瞰着全场噤若寒蝉的无辜市民，厉声喝令所有人向他臣服下跪！"},
                {"en": "Is not this simpler? Is this not your natural state? It is the unspoken truth of humanity that you crave subjugation.", "cn": "难道这不更轻松省事吗？难道这不正是你们这群凡夫俗子的天然本性吗？全人类心照不宣却耻于承认的丑陋真相就是：你们骨子里天生就渴望被绝对强权狠狠奴役践踏！"},
                {"en": "An elderly German gentleman slowly stood up in defiance: Not to men like you; there are always men like you.", "cn": "一位曾亲历过二战纳粹集中营浩劫的白发苍苍德国老绅士，在刺骨寒风中颤巍巍却脊梁笔挺地缓缓站起身：向你这样自命不凡的狂徒下跪绝无可能；这世上从来都不缺像你这种自作聪明的暴君！"},
                {"en": "When the Time Variance Authority arrested him for timeline deviations, Loki discovered that the Infinity Stones were used as mere paperweights.", "cn": "当超脱主宇宙的时间变异管理局以扰乱时间线的罪名将他逮捕归案时，洛基惊愕欲绝地发现：那些平日里诸神争得头破血流的无上无限宝石，在此处竟然被当成随手丢弃的廉价镇纸！"},
                {"en": "Seeing his entire destined life roll out on a celluloid projector reel completely shattered his theatrical narcissistic illusions.", "cn": "亲眼看着自己注定惨死在灭霸铁掌之下的命运剧本在电影放映机光束中一幕幕冰冷流淌展开，他内心经营了一生的自恋虚妄戏剧感刹那间轰然粉碎坍塌。"},
                {"en": "He realized that his entire villainous career of petty malice was not glory, but an insecure cry for attention and love.", "cn": "他终于痛苦万分地大彻大悟：自己前半生那些搬弄是非、睚眦必报的恶棍勾当，从来不是什么狗屁光荣使命，那不过只是一个缺乏安全感的可怜孩子在变相乞求被关注与被爱的绝望哀嚎！"},
                {"en": "Mobius became his very first genuine friend, treating the disgraced god not as an uncontrollable monster, but as an evolving man.", "cn": "特工莫比乌斯成为了他漫长一千五百年神生之中破天荒结识的第一个真正挚友；莫比乌斯从未将他视作无可救药的定时炸弹，而是将他当成一个能够向善蜕变的血肉之人。"},
                {"en": "I know what kind of god I need to be, Loki whispered with solemn clarity as the Temporal Loom melted into cataclysmic oblivion.", "cn": "我终于彻底大彻大悟我究竟该成为一位怎样的神明了，当维系万界的巨型时间织布机即将发生灾难性超载大爆炸时，洛基神色无比从容澄澈地轻声自语。"},
                {"en": "He walked out onto the exposed cosmic gantry without a spacesuit, temporal radiation tearing at his divine royal green robes.", "cn": "他没有套上任何宇航防护服，孑然一身从容迈步走上了暴露在虚空狂暴乱流之中的时间跳桥；毁灭性的时间辐射疯狂撕扯撕裂着他身上那袭深绿色的王室长袍。"},
                {"en": "With his bare hands, he grabbed the dying, tangled threads of billions of timeline branches, pumping his own magical lifeblood into them.", "cn": "他毫不犹豫伸出赤手空拳，一把死死抓住了数十亿条濒临枯萎崩溃的垂死时间线丝线，将自己体内的全部神力精血如烈火般源源不断灌注其中！"},
                {"en": "His regal green and gold horns crowned his brow as his cape billowed into infinite emerald leaves across the vast void.", "cn": "象征着恶作剧之神神格的华丽黄金犄角王冠威严浮现在前额，他背后翻滚的披风在浩瀚虚空中如繁茂的翡翠枝叶般向着无尽时空浩浩荡荡蔓延舒展！"},
                {"en": "Ascending the crumbling stone staircase into the celestial throne at the end of time, Loki took his solitary, eternal seat.", "cn": "沿着悬浮在天地尽头的古老残破大理石神圣台阶一步一步踏上虚空王座，洛基终于平静从容地端坐在了属于他的永恒孤独神座之上。"},
                {"en": "Holding the universe together like the roots of the legendary World Tree Yggdrasil, he sacrificed his companionship so his friends could live.", "cn": "用双手死死扣住这漫天时间线，将整个多元宇宙凝聚撑起宛如古老北欧神话中巍峨的世界之树“尤克特拉希尔”；他心甘情愿舍弃了渴望一生的相伴欢愉，只为换取莫比乌斯与所有挚爱之人能够活在自由阳光之下。"},
                {"en": "The god of mischief had died, and in his place sat the God of Stories, bearing the weight of all reality with noble, silent grace.", "cn": "昔日那个偷鸡摸狗、惹是生非的恶作剧邪神早已安详逝去；而在那永恒王座之巅巍然伫立的，是一位用血肉之躯默默背负起多元宇宙所有悲欢离合的真正“故事之神”，流淌着圣洁无言的绝世芳华！"}
            ]
        }
    ]))

    return courses
