# -*- coding: utf-8 -*-
from builder_core import build_course

def get_movies_part3():
    courses = []

    # 6. 《哈利·波特》(Harry Potter)
    courses.append(build_course({
        "id": "course-mov-potter",
        "title": "《哈利·波特》(Harry Potter) · 霍格沃茨魔法世界经典咒语与台词 (10章全集)",
        "category": "movies",
        "categoryName": "影视英语",
        "coverGradient": "from-amber-700 via-red-900 to-slate-900",
        "icon": "⚡",
        "description": "伴随一代人成长的魔法史诗，九又四分之三站台、分院帽、守护神咒与爱战胜黑暗的力量。",
        "difficulty": "中级 B1",
        "tags": ["魔法世界", "哈利波特", "经典咒语", "青春成长"]
    }, [
        {
            "title": "第 1 幕 · 女贞路 4 号与海格的破门而入",
            "description": "大难不死的男孩在楼梯下碗柜里收到雪片般的霍格沃茨录取通知书。",
            "sentences": [
                {"en": "Mr. and Mrs. Dursley were proud to say that they were perfectly normal, thank you very much.", "cn": "家住女贞路4号的德思礼夫妇总是得意洋洋地宣称自己是极其正常的体面人家，拜托，多谢关心。"},
                {"en": "Harry had lived under the stairs in a dark, dusty cupboard for ten miserable years.", "cn": "整整十个凄惨苦难的年头里，哈利一直蜷缩寄宿在楼梯下方那间阴暗逼仄、布满灰尘的破旧碗柜里。"},
                {"en": "Hundreds of owls perched on the roof gutters carrying parchment envelopes sealed with purple wax.", "cn": "数以百计的猫头鹰整整齐齐栖息在屋檐排水沟旁，嘴里衔着用高贵紫色火漆严密加封的羊皮纸信封。"},
                {"en": "The wooden front door burst open with a deafening crash as a giant entered the hut.", "cn": "伴随着一声震耳欲聋的惊天巨响，礁石小屋厚重的木门被轰然撞开，一位身形巍峨的巨人阔步闯入。"},
                {"en": "Yer a wizard, Harry, and a thumpin' good'un, I'd say, once yer trained up a bit.", "cn": "哈利，你可是一个如假包换的巫师啊！而且依我看，只要稍微点拨调教，你绝对是个顶呱呱的大巫师！"},
                {"en": "Uncle Vernon turned purple with uncontrollable fury, shouting that he would not pay for magic lessons.", "cn": "弗农姨父气得满脸通红发紫，暴跳如雷地扯着嗓子咆哮怒吼，坚称自己绝不会给什么见鬼的魔法学校掏一分钱学费。"},
                {"en": "Hagrid handed Harry a squashed cardboard box containing a chocolate birthday cake with green icing.", "cn": "海格小心翼翼递给哈利一个压得扁扁的纸盒，里面盛放着一块用绿色糖霜歪歪扭扭写着祝福的巧克力生日蛋糕。"},
                {"en": "Dry up, Dursley, you great prune! Hagrid roared, brandishing his pink flowery umbrella.", "cn": "闭上你的臭嘴吧，德思礼，你这个大窝囊废！海格猛然扬起手中那柄掩人耳目的粉红色碎花雨伞怒吼道。"},
                {"en": "Magic is real, Harry, and your wonderful parents are famous legends across our entire world.", "cn": "魔法是真实存在的，哈利；而且你那了不起的亲生父母，在我们整个魔法世界里是人人敬仰的传奇英雄。"},
                {"en": "He had never felt so bewildered, terrified, and utterly ecstatic in his entire life.", "cn": "在此之前漫长的人生岁月里，他从未同时品尝过如此交织混杂的迷茫困惑、惊惶无措与发自肺腑的狂喜。"},
                {"en": "Pack your belongings, little lad; tomorrow morning we catch the earliest train to London.", "cn": "麻利收拾好你随身的细软包裹吧，小家伙；明儿个一大清早，咱们就得赶头班列车直奔繁华伦敦。"},
                {"en": "A strange tingling warmth rushed through Harry's fingertips when he held the invitation letter.", "cn": "当哈利颤抖着双手紧紧攥住那封沉甸甸的羊皮纸录取信时，一股奇异温暖的微弱电流瞬间席卷了他的指尖。"},
                {"en": "The lightning bolt scar on his forehead prickled with faint, forgotten memories of emerald light.", "cn": "他前额上那道标志性的闪电状神秘伤疤隐隐发烫刺痛，唤醒了脑海深处早已遗忘的幽幽翠绿光芒记忆。"},
                {"en": "Your name has been down at Hogwarts School of Witchcraft and Wizardry since the day you were born.", "cn": "从你呱呱坠地降临人世的那一天起，你的大名就已经赫然登记在了霍格沃茨魔法学校的花名册之上。"},
                {"en": "Step outside into the cool sea breeze, Harry; your true destiny begins right this moment.", "cn": "跨过门槛迎着清凉咸湿的海风昂首阔步吧，哈利；属于你波澜壮阔的真实宿命，就在这一瞬间正式扬帆起航！"}
            ]
        },
        {
            "title": "第 2 幕 · 九又四分之三站台与霍格沃茨特快列车",
            "description": "推着行李手推车径直穿过坚硬砖墙，登上喷吐浓烟的猩红蒸汽火车。",
            "sentences": [
                {"en": "All you have to do is walk straight at the solid brick barrier between platforms nine and ten.", "cn": "你要做的其实很简单：目不斜视、挺起胸膛，径直朝着第九和第十站台之间那堵坚硬结实的砖墙撞过去！"},
                {"en": "Don't stop and don't be scared you'll crash into it; that's very important if you're nervous.", "cn": "千万别在中途犹犹豫豫停下脚步，也别害怕自己会一头撞扁；心里越是紧张，就越要鼓足勇气一鼓作气冲过去！"},
                {"en": "A glorious scarlet steam engine stood waiting beside a platform packed with bustling wizards.", "cn": "一列流光溢彩、威武雄壮的深红猩红色蒸汽火车头正静静伫立在铁轨旁，身畔站台挤满了熙熙攘攘的各色巫师。"},
                {"en": "Excuse me, do you mind if I sit here? Everywhere else is completely full, Ron asked shyly.", "cn": "打扰一下，请问我能坐这儿吗？其他车厢的座位全都被挤得满满当当了，罗恩红着脸略显腼腆地小声问道。"},
                {"en": "Harry bought everything from the trolley: Chocolate Frogs, Bertie Bott's Every Flavour Beans, and Pumpkin Pasties.", "cn": "哈利豪爽地把餐车上的所有零食全包了：巧克力蛙、比比多味豆，还有热气腾腾金黄诱人的南瓜馅饼。"},
                {"en": "Watch out for the beans! Ron warned. You might get chocolate or peppermint, or you might get earwax!", "cn": "吃那些豆子时可千万留神！罗恩好心提醒道，你可能吃到香甜的巧克力或薄荷味，但也可能冷不丁嚼到一口耳屎味！"},
                {"en": "Has anyone seen a toad? A boy named Neville's lost one, a bossy girl with bushy hair inquired.", "cn": "请问有谁看见一只蟾蜍了吗？有个叫纳威的倒霉男孩把它弄丢了，一个顶着一头蓬松浓密卷发、语气盛气凌人的小姑娘探头问道。"},
                {"en": "Holy cricket, you're Harry Potter! I'm Hermione Granger, by the way, and you're sitting with Ron Weasley.", "cn": "天呐大惊小怪，你居然真的是哈利·波特！顺便自我介绍一下，我叫赫敏·格兰杰，而坐在你对面的想必是罗恩·韦斯莱吧。"},
                {"en": "She pointed her wand and casually cast Oculus Reparo, neatly mending Harry's broken spectacles.", "cn": "她从容不迫地优雅扬起魔杖，随口念诵出一句“恢复如初”，瞬间把哈利鼻梁上用胶带胡乱缠绕的断裂眼镜修复如初。"},
                {"en": "The Hogwarts Express clattered smoothly northward past rolling green hills and mirror-like Scottish lochs.", "cn": "霍格沃茨特快列车在铁轨上发出富有节奏的清脆哐当声，一路风驰电掣向北呼啸飞驰，掠过连绵起伏的翠绿山丘与明镜般的苏格兰湖泊。"},
                {"en": "Draco Malfoy swaggered into the compartment with his two hulking henchmen, sneering at Ron's freckles.", "cn": "德拉科·马尔福带着他那两个形影不离、人高马大的跟班跟屁虫大摇大摆踱进包厢，满脸鄙夷地嘲讽嗤笑着罗恩脸上的雀斑。"},
                {"en": "You'll soon find out that some wizarding families are much better than others, Potter; choose your friends wisely.", "cn": "波特，你很快就会彻底明白，有些巫师纯血家族就是要比其他下等人高贵得多；你交朋友可千万要擦亮眼睛。"},
                {"en": "I think I can tell the wrong sort for myself, thanks, Harry replied with quiet, unwavering defiance.", "cn": "我想我完全有能力自己分辨出谁才是不三不四的势利小人，多谢你的好意提醒，哈利神色平静如水，但眼神中透着绝不退让的冰冷回击。"},
                {"en": "The golden castle of Hogwarts loomed against the ink-black night sky, its hundreds of windows ablaze with welcoming light.", "cn": "巍峨宏伟的霍格沃茨黄金城堡在如泼墨般深邃漆黑的夜空掩映下巍然耸立，数以百计的拱形窗棂在暮色中闪耀着温暖璀璨的迎客烛光。"},
                {"en": "Fleet upon fleet of small wooden boats glided silently across the glassy surface of the enchanted Black Lake.", "cn": "一艘接一艘轻巧古朴的木制小船仿佛拥有灵性一般，悄无声息地列队滑过被施了奇妙守护魔法的如镜黑湖水面。"}
            ]
        },
        {
            "title": "第 3 幕 · 庄严的分院仪式与古老四大学院",
            "description": "戴上能看透灵魂深处的脏旧分院帽，决定一生的学院归属与荣耀。",
            "sentences": [
                {"en": "The Great Hall was illuminated by thousands of floating candles drifting lazily below an enchanted ceiling.", "cn": "宏伟宽敞的霍格沃茨大礼堂被数以千计悬浮在半空中的轻盈蜡烛映照得金碧辉煌，头顶是倒映着浩瀚夜空的奇妙魔法天花板。"},
                {"en": "There's nothing hidden in your head the Sorting Hat cannot see, so try me on and I will tell you where you ought to be.", "cn": "你脑瓜深处藏匿的任何隐秘心思，都休想逃过本分院帽的法眼；快快把我戴在头上吧，我将为你指明最适合安身的荣耀归宿！(分院帽之歌)"},
                {"en": "You might belong in Gryffindor, where dwell the brave at heart, their daring, nerve, and chivalry set them apart.", "cn": "你也许属于格兰芬多学院，那里汇聚着人世间最无所畏惧的真正勇者；他们的非凡胆魄、豪迈气概与崇高骑士精神，令其卓尔不群。"},
                {"en": "You might belong in Hufflepuff, where they are just and loyal, patient, true, and unafraid of toil.", "cn": "你也许该被分入赫奇帕奇，那里的学子刚正不阿、赤胆忠心；他们坚韧耐劳、待人真挚，从不畏惧任何繁重辛勤的汗水付出。"},
                {"en": "Or yet in wise old Ravenclaw, if you've a ready mind, where those of wit and learning will always find their kind.", "cn": "亦或者进入聪慧古雅的拉文克劳，只要你拥有一颗孜孜以求的敏锐头脑；在那个知识殿堂里，富有才智博学多才之士总能觅得同道知己。"},
                {"en": "Or perhaps in Slytherin you'll make your real friends; those cunning folk use any means to achieve their ends.", "cn": "再不然你或许会在斯莱特林结识你一生的挚友；那些城府深沉狡黠机敏之辈，会不惜动用一切手腕谋略来达成其宏伟野心抱负。"},
                {"en": "Not Slytherin, not Slytherin! Harry muttered desperately under his breath as the ancient hat touched his messy hair.", "cn": "千万别是斯莱特林，千万别去斯莱特林！当那顶饱经沧桑褶皱遍布的古旧帽子轻轻扣在他乱蓬蓬的黑发上时，哈利在齿缝间绝望祈求默念。"},
                {"en": "Not Slytherin, eh? the small voice chuckled in his ear. You could be great, you know, it's all here in your head.", "cn": "不想去斯莱特林，嗯哼？那道尖细滑稽的声音在他耳畔咯咯轻笑，你其实大有作为，知道吗？宏图伟业的潜质就沉睡在你的脑海深处。"},
                {"en": "Well, if you're quite sure... better be GRYFFINDOR! the hat shouted aloud to the applauding hall.", "cn": "好吧，既然你内心如此笃定决绝……那么最适合你的归宿莫过于——格兰芬多！分院帽向着爆发出雷鸣般热烈掌声的满堂师生放声长啸！"},
                {"en": "The Gryffindor table erupted into deafening cheers, chanting that they had gotten the boy who lived.", "cn": "格兰芬多长桌旁的全体师生瞬间爆发出震耳欲聋的狂欢欢呼，高举酒杯奔走相告，兴奋高唱着他们迎来了大难不死的男孩。"},
                {"en": "Headmaster Albus Dumbledore stood up with twinkling eyes, welcoming everyone to a splendid new academic term.", "cn": "德高望重的阿不思·邓布利多校长缓缓微笑着起身伫立，镜片后那双深邃湛蓝的眼睛闪烁着慈祥智慧的光芒，温情欢迎大家开启崭新学期。"},
                {"en": "The golden platters suddenly overflowed with roast beef, Yorkshire pudding, buttered peas, and endless flagons of pumpkin juice.", "cn": "金灿灿的巨大餐盘里刹那间凭空堆满了香气四溢的现烤热牛肉、约克郡布丁、黄油青豆，以及畅饮不尽的大壶清爽南瓜汁。"},
                {"en": "Nearly Headless Nick floated jovially over the tables, demonstrating why his neck was severed by forty-five chops.", "cn": "差点没头的尼克幽默风趣地飘荡在长桌上空，绘声绘色地向新生们演示当年刽子手究竟是如何用四十五斧才勉强切断他的脖颈。"},
                {"en": "Walking up the marble staircase, the oil portraits whispered and bowed as the students climbed to Gryffindor Tower.", "cn": "踏上气派宽敞的乳白大理石旋转楼梯，两旁悬挂的巨大油画肖像画中的人物交头接耳窃窃私语，纷纷微笑着躬身向新生致意行礼。"},
                {"en": "Caput Draconis! Percy Weasley barked at the portrait of the Fat Lady, which swung open to reveal the cozy common room.", "cn": "龙渣！级长珀西·韦斯莱对着胖妇人的巨大画像中气十足地报出通行口令，画像应声旋转敞开，露出了温暖如春的公共休息室。"}
            ]
        },
        {
            "title": "第 4 幕 · 地下魔药课斯内普教授的下马威",
            "description": "地窖里翻滚的坩埚与黑袍翻滚的冷酷大师，传授如何将声名酿造进瓶塞。",
            "sentences": [
                {"en": "Professor Snape swept into the cold, shadowy dungeon classroom like an ominous, swooping black bat.", "cn": "斯内普教授那袭漆黑如墨的宽大长袍宛如一只阴森不祥的巨大夜蝠，夹带着刺骨冰冷的凛冽寒风猛然卷入阴暗地窖教室。"},
                {"en": "You are here to learn the subtle science and exact art of potion-making.", "cn": "你们来到这里，是为了潜心研习魔药配制这门精密微妙的严谨科学与丝丝入扣的高超艺术。"},
                {"en": "As there is little foolish wand-waving here, many of you will hardly believe this is magic.", "cn": "由于在我的课堂上几乎用不着像个傻瓜一样胡乱挥舞手中的小木棍，你们当中的许多蠢才恐怕很难相信这也是高深莫测的魔法。"},
                {"en": "I can teach you how to bottle fame, brew glory, and even stopper death itself.", "cn": "我能够倾囊传授你们如何将世俗的名望注入药瓶，如何细细熬煮出璀璨的荣耀，甚至如何将冷酷的死亡本身紧紧锁入软木瓶塞。"},
                {"en": "Potter! Snape barked abruptly. What would I get if I added powdered root of asphodel to an infusion of wormwood?", "cn": "波特！斯内普眼神如淬了毒的冰刃骤然刺来，如果我把水仙根粉末小心倒入艾草浸液之中，究竟会得到什么奇妙药剂？！"},
                {"en": "Hermione's hand shot straight into the air like a rigid flagstaff, eager to display her encyclopedic knowledge.", "cn": "赫敏的手臂如同一根笔挺坚韧的旗杆般瞬间高高举向半空，迫不及待想要向全班展示她那如百科全书般渊博的惊人背诵功底。"},
                {"en": "I don't know, sir, Harry admitted frankly, meeting the professor's cold obsidian eyes without flinching.", "cn": "报告先生，我不知道，哈利毫无惧色地坦然承认，目光毫不退缩地直直迎向教授那双如同两口枯井般冰冷空洞的黑曜石深邃双眸。"},
                {"en": "Clearly, fame isn't everything, is it, Mr. Potter? Snape sneered, lip curling with unmistakable disdain.", "cn": "显而易见，大难不死的光环虚名并不能代替真正的大脑知识，不是吗，波特先生？斯内普薄薄的唇角泛起毫不掩饰的轻蔑讥讽。"},
                {"en": "Asphodel and wormwood make a sleeping potion so powerful it is known as the Draught of Living Death.", "cn": "将水仙根与苦艾草精准调和，能够熬制出一种威力极其恐怖霸道的强效安眠毒剂，在魔法界它被敬畏地冠以“一饮活死人”的凶名。"},
                {"en": "A bezoar is a calcified stone taken from the stomach of a goat, which will save you from most poisons.", "cn": "牛黄是一块从山羊胃囊深处取出的钙化坚硬结石，只要将其塞入受害者咽喉，便足以解开这世上绝大多数烈性剧毒的致命锁喉。"},
                {"en": "And what is the subtle difference between monkshood and wolfsbane, boy?", "cn": "那么最后再告诉我，舟形乌头与狼毒草这二者之间，究竟存在着怎样微乎其微的微妙细致差异，无知的男孩？"},
                {"en": "They are the exact same magical plant, which also goes by the ancient botanical name of aconite.", "cn": "它们在本质上根本就是同一种神奇药用植物，在古老严谨的草药植物学经典名录上，它们拥有一个共同的大名——附子草。"},
                {"en": "Why aren't you all copying down what I just said? Snape thundered at the terrified students.", "cn": "你们这群榆木脑袋为什么还不赶紧抓起羽毛笔，把我刚才说的每一个字工工整整抄在羊皮纸上？！斯内普如平地惊雷般向着全体吓傻的新生厉声喝道。"},
                {"en": "A point will be taken from Gryffindor House for your cheek and inexcusable ignorance, Potter.", "cn": "因为你那令人作呕的傲慢无礼，以及对魔法常识无可救药的愚昧无知，格兰芬多学院将被无情扣除一分，波特！"},
                {"en": "Harry clenched his fists beneath the wooden desk, realizing this dark professor harbored a deep, inexplicable hatred.", "cn": "哈利在课桌下方将双拳捏得咯咯作响，他无比清晰地意识到：眼前这位浑身散发着阴冷寒气的魔药教授，对自己怀揣着一股刻骨铭心、深不见底的莫名仇恨。"}
            ]
        },
        {
            "title": "第 5 幕 · 魁地奇飞天扫帚与抓捕金色飞贼",
            "description": "骑上光轮两千冲上云霄，在狂风与游走球的轰炸中为学院夺得荣耀。",
            "sentences": [
                {"en": "Madam Hooch blew her silver whistle, and fifteen broomsticks kicked off hard from the grassy pitch.", "cn": "霍琦夫人猛然吹响了尖锐明亮的银色哨声，十五把飞天扫帚几乎在同一瞬间用力蹬离绿草如茵的开阔球场，呼啸腾空而起。"},
                {"en": "Harry felt the exhilarating rush of cold wind whistling through his hair as his Nimbus Two Thousand soared.", "cn": "当胯下那把崭新轻盈的“光轮两千”以惊人速度如箭离弦冲上云霄时，哈利只觉刺骨凛冽的狂风在发丝间欢畅呼啸，爽快至极。"},
                {"en": "Quidditch is easy enough to understand: seven players, four balls, and three golden goal hoops on each end.", "cn": "魁地奇比赛的规则其实一目了然极其简单：双方各派七名队员上场，角逐四只用处各异的皮球，球场两端各矗立着三座高耸入云的金色球门圆环。"},
                {"en": "The scarlet Quaffle is thrown by Chasers to score ten points through the opposing hoops.", "cn": "猩红色的“鬼飞球”由专门的追球手们在空中相互飞速传接抛掷，只要将其成功投穿对方防守的金色圆环，即可斩获十分入账。"},
                {"en": "The two heavy iron Bludgers rocketed across the pitch, trying to knock players off their brooms.", "cn": "两只沉重冰冷坚如生铁的“游走球”如脱缰野马般在半空中四处疯狂狂暴横冲直撞，凶狠企图将飞行的队员们硬生生撞落扫帚。"},
                {"en": "The Beaters carry short wooden bats to deflect the violent Bludgers toward the rival team.", "cn": "两名身强体壮的击球手各自手持一柄厚重短木球棒，敏捷精准地将狂暴袭来的游走球凶狠反弹轰击向敌方阵营。"},
                {"en": "And then there is the tiny, walnut-sized Golden Snitch with fluttery silver wings.", "cn": "而在赛场最难以捉摸的虚空高处，还盘旋穿梭着一只仅有核桃般娇小玲珑、生有一对振颤微弱银色羽翼的“金色飞贼”。"},
                {"en": "Catching the Snitch awards an enormous one hundred and fifty points and immediately terminates the match.", "cn": "只要己方的找球手能够先发制人一举将其抓获，不仅能为团队狂揽惊人的一百五十分巨奖，更将瞬间强制鸣哨终结整场殊死鏖战。"},
                {"en": "A glint of brilliant gold flashed near the base of the Slytherin goalposts, moving like liquid light.", "cn": "斯莱特林队球门底座的阴影近旁，蓦然闪过一抹璀璨夺目的灿烂纯金流光，宛如一滴具有鲜活生命的流体闪电般飘忽穿梭。"},
                {"en": "Harry went into an uncontrollable, breathtaking dive, leaning flat against the handle of his broom.", "cn": "哈利毫不犹豫骤然压低扫帚柄身，整个人化作一道笔直下坠的惊天霹雳，以令人窒息的极限神级俯冲撕裂苍穹！"},
                {"en": "The Slytherin Seeker tried to follow, but pulled out at the last second to avoid smashing into the turf.", "cn": "斯莱特林队的找球手原本妄图负隅顽抗紧咬不放，但在距离地面仅剩三尺的生死攸关极限瞬间，因极度恐惧不得不狼狈拉起机头避险。"},
                {"en": "Harry tumbled through the grass, clutching his stomach and choking as though he was about to vomit.", "cn": "哈利顺着惯性整个人在绿茵草皮上连续翻滚了十几个跟头，痛苦弯腰死死捂住胃部剧烈干呕，仿佛随时要当场呕吐出来。"},
                {"en": "He coughed violently, and the glistening Golden Snitch popped right out of his mouth into his palm!", "cn": "他剧烈猛咳了一声，那只扑棱着薄薄银色翅膀、闪闪发光的金色飞贼，竟然骨碌一下从他的嘴巴里直接吐落在了掌心之中！"},
                {"en": "He didn't catch it in his hand, he nearly swallowed it! but a win is a glorious win!", "cn": "他根本不是用双手抓住了它，他差点一口把飞贼给硬生生咽进肚子里去了！但赢了就是赢了，这是一场载入史册的辉煌胜利！"},
                {"en": "Lee Jordan shouted into the magical megaphone as the scarlet stands exploded into ecstatic hysteria.", "cn": "解说员李·乔丹抓起加持了洪亮魔法扩音的巨型大喇叭疯狂嘶吼咆哮，全场鲜红色的格兰芬多看台刹那间陷入狂喜的癫狂海洋！"}
            ]
        },
        {
            "title": "第 6 幕 · 厄里斯魔镜里的深邃渴望与执念",
            "description": "镜中照出的不是你的容貌，而是你心灵深处最迫切、最深沉的欲望。",
            "sentences": [
                {"en": "Harry wandered through the dark, abandoned disused classroom beneath his father's shimmering Invisibility Cloak.", "cn": "披着父亲遗留下的那件流光溢彩、隐匿身形的隐形衣，哈利悄悄漫步穿行在寂静漆黑、早已废弃不用的大理石古旧空教室里。"},
                {"en": "In the center of the room stood a magnificent mirror, tall as the ceiling, with an ornate gold frame.", "cn": "在空旷教室的正中央赫然耸立着一面气派非凡的巨大魔镜，足足高耸抵拢天花板，周身镶嵌着极其繁复典雅的华美鎏金边框。"},
                {"en": "Inscribed along the top were the mysterious words: Erised stra ehru oyt ube cafru oyt on wohsi.", "cn": "镜框顶部镌刻着一串如谜语般晦涩难懂的古怪文字：我显现的并非汝之容颜，而是汝内心最炽热之深切渴望。"},
                {"en": "Looking into the glass, Harry did not see his solitary reflection; he saw a crowd standing right behind him.", "cn": "凝视着澄澈如水的镜面玻璃，哈利惊愕地发现里面映照出的并非他孑然一人的孤独倒影；在他身后，竟密密麻麻并肩伫立着一大群人。"},
                {"en": "A beautiful dark-haired woman with bright green eyes identical to his own was smiling with tears in her eyes.", "cn": "一位拥有一头乌黑秀发、生着一双与哈利如出一辙明亮碧绿眼眸的温存美丽女子，正含着热泪，满眼深情地微笑着注视着他。"},
                {"en": "Beside her stood a tall, untidy-haired man with round glasses, affectionately placing a hand on the boy's shoulder.", "cn": "女子身畔并肩伫立着一位身材修长挺拔、同样顶着一头乱蓬蓬黑发、佩戴圆框眼镜的青年男子，慈爱温厚地将手轻轻搭在男孩肩头。"},
                {"en": "Mum? Dad? Harry whispered, his trembling fingers pressing flat against the cold, unyielding glass.", "cn": "妈妈？……爸爸？哈利喉头哽咽发颤，小声抽泣着轻声呼唤，颤抖滚烫的指尖绝望地紧紧贴在那面冰冷无情、坚硬无比的玻璃镜面上。"},
                {"en": "For the first time in his conscious life, he was gazing directly into the radiant faces of his entire family.", "cn": "这在他记事以来的整个人生岁月里，还是破天荒头一次，能够如此真切、如此近距离地深情凝望全家亲人那散发着温暖光晕的慈祥面庞。"},
                {"en": "It does not do to dwell on dreams and forget to live, remember that, Harry, a soft voice murmured from the shadows.", "cn": "沉溺于虚妄缥缈的梦幻假象之中，从而彻底忘却了现实生活的鲜活步履，这绝非明智之举；孩子，请你务必牢记这一点，一道温和的声音从暗处飘来。"},
                {"en": "Professor Dumbledore was sitting casually on a wooden desk by the moonlit window, observing him with infinite kindness.", "cn": "白发苍苍的邓布利多校长正姿态从容随意地斜倚在月光倾泻的窗台课桌旁，用那双充满无限包容与慈悲智慧的眼眸静静注视着他。"},
                {"en": "The happiest man on earth would look into the mirror and see only himself, exactly as he is.", "cn": "这人世间最幸福快乐、心灵最完满充盈的人若是站在这面魔镜面前，他在镜中看到的将仅仅只是他自己现在的真实模样。"},
                {"en": "Men have wasted away before it, entranced by what they have seen, or been driven mad.", "cn": "多少意志薄弱的人曾经在这面魔镜面前虚度消磨尽了整整一生，被镜中虚幻诱人的泡影彻底勾魂摄魄，甚至最终被活活逼成彻底的疯子。"},
                {"en": "The mirror will be moved to a new home tomorrow, and I ask you not to go looking for it again.", "cn": "明儿个天一亮，这面危险的魔镜就将被秘密移送到一处崭新的安全秘所；作为你的师长，我由衷恳求你今后绝不要再去试图搜寻它的踪迹。"},
                {"en": "If you ever do run across it, you will now be prepared: courage lies in facing real sorrow, not comforting illusions.", "cn": "若是未来的某一天你机缘巧合再次与它狭路相逢，你便早已做好心理防备：真正的非凡勇气，在于坦然直面骨感的真实哀伤，而非蜷缩在虚假的慰藉幻境之中苟活。"},
                {"en": "Harry nodded slowly, bidding farewell to the phantom reflection that could never kiss him goodnight.", "cn": "哈利若有所思地缓缓点了点头，终于下定决心，恋恋不舍地向镜中那团永远无法跨过现实亲吻他道晚安的虚无幻影郑重告别。"}
            ]
        },
        {
            "title": "第 7 幕 · 禁林夜巡与独角兽银白色的纯净血液",
            "description": "古老禁林深处，伏地魔附身的黑袍怪物正在贪婪吮吸纯洁的生命之血。",
            "sentences": [
                {"en": "The Forbidden Forest was shrouded in perpetual midnight mist, ancient pine trees whispering dark secrets.", "cn": "充满凶险未知的禁林常年笼罩在经久不散的永恒子夜迷雾之中，遮天蔽日的万年古松苍柏在阴风中窃窃私语着不可名状的漆黑秘密。"},
                {"en": "Hagrid led the detention party with his giant crossbow loaded, Fang the boarhound whining nervously.", "cn": "海格手中紧握着上膛的沉重巨型合金弩机走在巡查小队最前头开路，那头胆小如鼠的大猎犬“牙牙”神经紧绷地发出不安的呜咽悲鸣。"},
                {"en": "Something in here has been hunting pure, innocent creatures; look at these silvery splashes on the moss.", "cn": "这片幽暗森林深处，显然盘踞着某种专门猎杀世间至纯至善神圣生灵的极恶怪物；你们快看青苔岩石上溅落的这些银白色反光血迹。"},
                {"en": "The blood of a unicorn will keep you alive, even if you are an inch from death, but at a terrible price.", "cn": "哪怕你早已气若游丝、距离死亡深渊仅剩毫厘之遥，独角兽神圣的纯洁血液依然能强行吊住你的残喘性命，但这必须付出惨绝人寰的沉痛代价。"},
                {"en": "From the moment the sacred blood touches your lips, you will have but a half-life, a cursed life.", "cn": "从这神圣无暇的精血沾染上你肮脏嘴唇的罪恶瞬间起，你便将从此陷入万劫不复的深渊，只能苟活在被天地诅咒的半死半生残破躯壳之中。"},
                {"en": "Harry stepped into a moonlit clearing and froze in sheer terror at the gruesome spectacle before him.", "cn": "哈利小心翼翼拨开荆棘踏入一片月光斑驳的林间空地，眼前赫然呈现的一幕可怖骇人景象瞬间让他浑身血液凝固、如坠冰窟。"},
                {"en": "A slender silver-white unicorn lay dead upon the forest floor, its legs splayed at awkward angles.", "cn": "一匹姿态修长优雅、通体泛着皎洁银白色神圣荧光的纯洁独角兽早已惨死在冰冷林地中央，四蹄以诡异扭曲的角度无力瘫软展开。"},
                {"en": "A hooded cloaked figure was crawling like a beast across the fallen leaves, dragging its shapeless black mass.", "cn": "一个浑身严严实实裹在漆黑兜帽长袍里的未知人形怪物，如同一头嗜血野兽般贴着满地枯枝落叶窸窸窣窣爬行，拖拽着毫无生气的庞大阴暗阴影。"},
                {"en": "It lowered its face over the open wound in the animal's neck and began drinking the glistening silver blood.", "cn": "那黑袍怪物俯下狰狞可怖的脸庞，贪婪对准神兽咽喉处汩汩涌出的巨大致命撕裂伤口，大口大口凶残吮吸起那流淌着微光的纯银活血。"},
                {"en": "Harry's scar erupted into blinding, agonizing pain, as though a white-hot poker had been pressed to his skull.", "cn": "哈利额头上的闪电伤疤刹那间爆发出痛彻心扉、近乎令人当场双目失明的剧烈灼痛，仿佛有一块烧得通红炽热的烙铁被硬生生狠狠按在了他的头骨之上。"},
                {"en": "He fell to his knees gasping for breath, unable to tear his terrified gaze away from the monster.", "cn": "他双膝发软扑通一声重重跪倒在地，大口大口绝望倒吸着冷气，却无论如何也无法将惊恐万状的涣散视线从眼前这头可怖魔鬼身上挪开半分。"},
                {"en": "The cloaked figure raised its dripping head, looked directly at the boy, and glided forward with murderous intent.", "cn": "那兜帽怪物缓缓抬起了嘴角犹自滴淌着银白色热血的狰狞头颅，那双毫无生气的血红眼眸直勾勾锁定住瘫倒的男孩，带着浓烈滔天的嗜血杀意无声贴地滑翔扑来！"},
                {"en": "Suddenly, thundering hooves shattered the silence as a magnificent palomino centaur leaped over Harry's head.", "cn": "千钧一发之际，一阵如平地春雷般震耳欲聋的狂暴马蹄践踏声骤然撕裂死寂，一头威风凛凛金发白马身躯的崇高半人马猛然凌空越过哈利头顶！"},
                {"en": "The creature reared on its hind legs and drove the dark entity back into the shadowy thickets with fierce blows.", "cn": "那头神勇半人马前蹄高高人立而起，扬起粗壮坚硬的铁蹄带起狂暴飓风，以雷霆万钧之势将那团漆黑鬼魅硬生生逼退轰回了密不透风的黑暗灌木丛深处。"},
                {"en": "Harry Potter, you must leave this dangerous ground at once; Mars is bright tonight and peril walks among us.", "cn": "哈利·波特，你必须立刻随我火速离开这片杀机四伏的凶险绝地；今夜天穹之上的火星格外猩红耀眼，不可言说的巨大浩劫正悄然行走在我们身侧！"},
                {"en": "Do you not realize who was hiding under that wretched hood? It was Lord Voldemort, waiting for his resurgence.", "cn": "难道你这单纯的孩子当真没有看清那可憎兜帽底下蛰伏的恶魔究竟是谁吗？那正是当年残暴屠戮你的全家的伏地魔，他正蛰伏在此茹毛饮血，静待东山再起！"}
            ]
        },
        {
            "title": "第 8 幕 · 守护神咒与快乐记忆的光芒力量",
            "description": "呼神护卫！面对摄魂怪的极寒绝望，召唤出银白牡鹿驱散一切黑暗阴霾。",
            "sentences": [
                {"en": "Dementors are among the foulest, most terrifying creatures that walk this earth.", "cn": "摄魂怪无疑是肆虐行走在这片人世间最令人作呕、最令人毛骨悚然的极恶至邪生物。"},
                {"en": "They infest the darkest, filthiest places; they glory in decay and despair, draining peace and hope from the air.", "cn": "它们在最阴暗、最污秽的角落里肆意滋生繁衍；它们以世间的枯萎衰败与绝望痛苦为无上荣耀，疯狂抽干空气中仅存的所有安宁与希望。"},
                {"en": "Get too near a Dementor and every good feeling, every happy memory will be mercilessly sucked out of you.", "cn": "一旦你不知死活靠得离摄魂怪太近，你灵魂深处的所有美好情感、每一段珍藏的快乐记忆，都将被它残忍无情地统统榨干吸净。"},
                {"en": "You will be left with nothing but the worst experiences of your past life replaying over and over in agony.", "cn": "留给你的，将只剩下你过往漫长岁月里遭遇过的最痛苦绝望的惨烈经历，如同梦魇般在撕心裂肺的剧痛中一遍又一遍无休止重演。"},
                {"en": "The Patronus Charm is a highly advanced, ancient spell that acts as a positive force field against them.", "cn": "“守护神咒”是一道极其高深莫测、历史悠久的古老超凡魔咒，它能够在施咒者周身构筑起一道坚不可摧的正能量纯阳防护力场。"},
                {"en": "The Patronus is a projection of the very things that the Dementor feeds upon: hope, happiness, the desire to survive.", "cn": "召唤出的神圣守护神，恰恰是将摄魂怪平日赖以吞噬为食的核心源泉凝聚外化投射：那是希望、极致的快乐，以及顽强求生的崇高意志！"},
                {"en": "Unlike a real human being, a Patronus can feel no despair, and so the Dementor cannot harm it.", "cn": "与拥有血肉之躯的脆弱凡人截然不同，守护神是纯粹的心灵光芒造物，它绝不会感知到任何一丝绝望，因此摄魂怪根本伤不到它分毫。"},
                {"en": "Concentrate on the single happiest memory you have ever lived through in your heart, Professor Lupin instructed.", "cn": "彻底摒除脑海中一切杂念，将全副心神死死聚焦在你此生经历过的唯独那一段最幸福、最炽热滚烫的快乐记忆之上，卢平教授极其严肃地悉心指导道。"},
                {"en": "Let that warm memory fill you up from your toes to your hair, raising your wand with absolute conviction.", "cn": "让那段滚烫滚热的美好回忆如暖流般瞬间从你的脚趾尖蔓延灌注到发梢末端，怀揣着绝对不容撼动的铁石信念高高扬起魔杖！"},
                {"en": "EXPECTO PATRONUM! Harry bellowed across the frozen lake as a hundred Dementors descended like black vultures.", "cn": "呼神护卫！当数以百计身披破烂长袍的摄魂怪宛如遮天蔽日的黑色秃鹫群般扑向冻结的湖泊时，哈利向着苍穹爆发出震天动地的惊天怒吼！"},
                {"en": "An enormous, blinding silver stag erupted from the tip of his wand, illuminating the frosted forest like a miniature sun.", "cn": "一头体格巍峨雄壮、浑身绽放着刺目银白色神圣光晕的纯银牡鹿，猛然从他的魔杖顶端呼啸破空喷涌而出，宛如一轮初升的小太阳般瞬间照亮整片冰封森林！"},
                {"en": "The majestic patronus lowered its magnificent antlered head and charged fearlessly into the swirling horde of phantoms.", "cn": "那尊神圣庄严的牡鹿威风凛凛地低下生有华丽鹿角的神圣头颅，毫无惧色地踏破虚空，如一道势不可挡的银白彗星狠狠撞入盘旋肆虐的恶鬼群中！"},
                {"en": "The Dementors shrieked in agony as the radiant silver energy seared their rotten shrouds, scattering them into the night.", "cn": "在这股至纯至阳的炽热银白能量灼烧之下，摄魂怪们身上腐烂的破布裹尸布冒出滚滚白烟，它们发出凄厉痛苦的绝望尖嚎，抱头鼠窜作鸟兽散，仓皇溃退遁入浓墨夜色深处。"},
                {"en": "Harry watched in stunned reverence as the silver stag cantered back across the water and bowed its noble head.", "cn": "哈利呆呆伫立在岸边，怀揣着无以复加的崇敬与震撼，眼睁睁看着那头神圣的纯银牡鹿迈着优雅轻盈的碎步踏浪归来，向他温顺地深深低下高贵的头颅。"},
                {"en": "It was his father's animagus form; in that magical manifestation of pure light, James Potter was still protecting his son.", "cn": "那正是他父亲生前引以为傲的阿尼马格斯化身；在那由纯粹爱与希望凝聚而成的神圣光芒奇迹之中，詹姆·波特跨越生死长河，依然在深情守护着他的至亲骨肉。"}
            ]
        },
        {
            "title": "第 9 幕 · 邓布利多校长的睿智谈话与爱的最强魔法",
            "description": "决定我们一生的不是我们的能力，而是我们的选择；爱是伏地魔永远不懂的力量。",
            "sentences": [
                {"en": "Words are, in my not-so-humble opinion, our most inexhaustible source of magic.", "cn": "依我那向来不算谦逊的个人愚见而论，人类口中吐露的语言辞藻，正是我们这世间最取之不尽、用之不竭的奇妙魔法源泉。"},
                {"en": "They are capable of both inflicting terrible injury, and remedying it with equal potency.", "cn": "它们既拥有造成足以令人痛不欲生的惨烈心灵重创的恐怖杀伤力，也同样兼具着能够以同等奇效抚平治愈一切创伤的无上神力。"},
                {"en": "It is our choices, Harry, that show what we truly are, far more than our abilities.", "cn": "哈利，真正决定我们究竟会成为一个怎样的人的，绝非我们与生俱来拥有多少非凡能力，而是我们在关键时刻做出的内心抉择。"},
                {"en": "You were terrified of being placed into Slytherin, yet you deliberately chose the path of brave Gryffindor.", "cn": "当年你内心深处对被分入斯莱特林充满了本能的抗拒恐惧，然而你最终凭借自己的钢铁意志，毅然决然选择了踏上格兰芬多的无畏勇者征程。"},
                {"en": "Do not pity the dead, Harry; pity the living, and, above all, those who live without love.", "cn": "绝不要去无谓怜悯哀悼那些早已安详长眠的逝者，哈利；去深深怜悯那些依然苟活在世上的人吧，尤其是那些在漫长一生中从未体验过真爱滋味的凄惨灵魂。"},
                {"en": "Voldemort's fundamental flaw has always been his inability to comprehend the mysterious power of love.", "cn": "伏地魔一生致命的根本性认知缺陷，始终在于他那颗扭曲冷酷的黑暗心灵，永远无法真正参透“爱”这一神秘而崇高的终极宇宙力量。"},
                {"en": "Your mother died to save you, and that sacrifice left an ancient, indelible mark upon your very skin.", "cn": "当年你的亲生母亲甘愿牺牲自己的性命只为换取你的生还，那场至纯至善的决绝牺牲，在你稚嫩的血肉之躯上烙下了一道古老神圣、万邪不侵的永恒印记。"},
                {"en": "Not a physical scar, but a lingering spiritual shield carried deep inside your veins.", "cn": "那绝非额头上那道肉眼可见的物理伤疤，而是一座深深流淌、永不磨灭地庇佑在你的静脉血管深处的崇高精神守护盾牌。"},
                {"en": "To have been loved so deeply, even though the person who loved us is gone, will protect us forever.", "cn": "只要一个人曾经被至亲之人如此刻骨铭心、毫无保留地深爱过，纵使那位深爱我们的人早已仙逝远离人世，那份沉甸甸的爱也必将化作永恒的圣光，护佑我们一生一世。"},
                {"en": "Happiness can be found, even in the darkest of times, if one only remembers to turn on the light.", "cn": "哪怕深陷在这人世间最冰冷黑暗、最绝望无助的惨淡逆境岁月里，快乐与光明也依旧唾手可得——只要我们心中始终牢记去伸手拧亮那盏希望的明灯！"},
                {"en": "Death is but the next great adventure to a mind that is well-structured and at peace with itself.", "cn": "对于一个心智健全成熟、早已与自我和世界达成和解的通达智者而言，肉躯的死亡不过只是通往下一场崭新壮阔伟大冒险的从容启程。"},
                {"en": "Differences of habit and language are nothing at all if our aims are identical and our hearts are open.", "cn": "只要我们肩负的崇高奋斗目标完全一致，只要我们彼此的心灵坦诚相待，生活习惯的些许差异与语言习俗的隔阂障碍，在宏大历史面前根本微不足道、不值一提。"},
                {"en": "It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.", "cn": "敢于挺直脊梁当面挺身对抗穷凶极恶的敌人，固然需要莫大的过人非凡胆识；但若想挺身而出、直言不讳地指出挚友犯下的过失错误，所需付出的道德勇气却丝毫不遑多让！"},
                {"en": "We must all face the choice between what is right and what is easy in the tumultuous days ahead.", "cn": "在前方即将到来的动荡风暴岁月里，我们每一个人都将被迫在“恪守正义的艰难长路”与“随波逐流的安逸捷径”这二者之间，做出无比残酷严峻的灵魂拷问抉择。"},
                {"en": "You have fought valiantly, Harry, and no headmaster could ever be prouder of a student than I am of you.", "cn": "孩子，你迄今为止展现出的英勇无畏令人动容；放眼这世间所有名留青史的校长，没有谁能够比此时此刻的我为拥有你这样的学生而感到更加由衷自豪！"}
            ]
        },
        {
            "title": "第 10 幕 · 霍格沃茨最终决战与十九年后的九又四分之三",
            "description": "十九年时光荏苒，大难不死的男孩送孩子踏上火车；伤疤再没痛过，一切平安无恙。",
            "sentences": [
                {"en": "The ancient stone walls of Hogwarts trembled as curses and counter-curses illuminated the shattered courtyard.", "cn": "霍格沃茨千百年风霜洗礼的古老石砌城堡城墙在剧烈震颤哀鸣，赤红与惨绿交织的致命咒语漫天飞舞呼啸，将化作焦土废墟的残破庭院映照得如白昼般刺眼。"},
                {"en": "Statues and suits of armor sprang to life at Professor McGonagall's command to defend the castle.", "cn": "在麦格教授气壮山河的“石墩出动”号令召唤之下，矗立在廊柱两旁成百上千具沉睡千年的古代骑士石雕与青铜盔甲轰然苏醒活化，迈着坚实厚重的步伐大步开赴前线保卫母校！"},
                {"en": "Hogwarts is threatened! Man the boundaries, protect us, do your duty to our beloved school!", "cn": "霍格沃茨危在旦夕！全体重甲守卫迅速坚守边界城防，以你们的钢铁躯躯筑起不可逾越的长城，为我们深爱的母校尽到你们的神圣职责！"},
                {"en": "Molly Weasley stepped forward with blazing eyes, fiercely declaring: NOT MY DAUGHTER, YOU EVIL FIEND!", "cn": "莫丽·韦斯莱夫人挺身而出，双眸中喷涌出护犊情深的熊熊烈焰，向着不可一世的食死徒暴怒长啸：休想碰我女儿一根汗毛，你这个恶贯满盈的恶魔！"},
                {"en": "Neville Longbottom pulled the gleaming Sword of Gryffindor from the Sorting Hat and decapitated the serpent Nagini.", "cn": "看似懦弱笨拙的纳威·隆巴顿猛然从破旧分院帽深处一把拔出寒光四射的格兰芬多神剑，以雷霆万钧之势凌空手起刀落，瞬间将伏地魔最后的魂器巨蛇纳吉尼身首异处！"},
                {"en": "The final Horcrux was destroyed, leaving Tom Riddle mortal, vulnerable, and stripped of his dark immortality.", "cn": "最后一个残存的黑暗魂器终于彻底灰飞烟灭，不可一世的汤姆·里德尔终于彻底被打回了肉体凡胎原形，彻底丧失了他赖以作威作福的虚妄永生光环。"},
                {"en": "Harry and Voldemort circled each other in the center of the Great Hall, locked in the ultimate philosophical duel.", "cn": "在大礼堂破碎的大理石中央，哈利与伏地魔如同两头生死宿命的孤狼般死死锁住对方缓慢兜圈踱步，展开了一场关于生命本质与爱恨生死的终极灵魂对决。"},
                {"en": "You won't kill anyone else tonight, Tom; you don't learn from your mistakes, do you? Love is what beat you.", "cn": "今夜你再也休想肆意夺走任何一个无辜之人的性命了，汤姆；你当真从来不长记性、不会从失败中吸取教训，是吗？击败你的，自始至终都是你嗤之以鼻的浩瀚大爱！"},
                {"en": "Expelliarmus clashed with the killing curse Avada Kedavra in a blinding emerald and gold collision.", "cn": "哈利手中的“除你武器”缴械咒与伏地魔射出的惨绿“阿瓦达索命”终极死咒在半空中悍然轰然对撞，迸发出毁天灭地的金碧交织刺目强光！"},
                {"en": "The Elder Wand refused to murder its true master; the lethal rebound struck Voldemort dead in his tracks.", "cn": "至高无上的老魔杖宁死也绝不肯背叛弑杀它真正的天命主人；反弹折射而回的致命死咒瞬间反噬精准击中伏地魔胸膛，一代黑魔头当场气绝毙命、轰然倒地化为飞灰！"},
                {"en": "The dawn broke cleanly over the Scottish highlands, bathing the battered towers in golden, peaceful morning sun.", "cn": "明朗澄澈的破晓黎明终于驱散了漫长黑夜，如期降临在苏格兰高地辽阔的群山之巅，将金灿灿、宁静祥和的晨曦暖阳温柔洒在满目疮痍的古老塔楼之上。"},
                {"en": "Nineteen years later, the autumn morning arrived crisp and golden on Platform Nine and Three-Quarters.", "cn": "十九载光阴如白驹过隙弹指一挥间，金秋时节清爽宜人、落叶泛金的美丽清晨，再次如约降临在熙熙攘攘的“九又四分之三”站台之上。"},
                {"en": "Albus Severus Potter clung to his father's coat, terrified of being sorted into Slytherin House.", "cn": "年幼的阿不思·西弗勒斯·波特紧紧攥着父亲的大衣下摆，大眼睛里噙着泪花，满心忐忑地担忧自己待会儿会被分院帽无情分入斯莱特林学院。"},
                {"en": "You were named for two headmasters of Hogwarts; one of them was a Slytherin, and he was the bravest man I ever knew.", "cn": "孩子，你的名字是以霍格沃茨历史上两位最卓越非凡的校长之名命名的；而他们当中的那一位，就曾来自斯莱特林学院，而且他是我这辈子所结识过的所有人中，骨头最硬、最英勇无畏的真正男人。"},
                {"en": "The scarlet train pulled away smoothly into the distance; the lightning scar had not pained Harry for nineteen years, and all was well.", "cn": "满载着崭新希望与欢声笑语的猩红蒸汽火车缓缓启动驶向远方；十九年漫长岁月沧海桑田，哈利前额上的伤疤再也没有隐隐作痛过分毫，这尘世间的一切，皆安详美好如初。"}
            ]
        }
    ]))

    return courses
