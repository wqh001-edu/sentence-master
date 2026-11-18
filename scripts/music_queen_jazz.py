# -*- coding: utf-8 -*-
from builder_core import build_course

def get_queen_and_jazz():
    courses = []

    # 7. 《皇后乐队》(Queen) · 10 章全集
    courses.append(build_course({
        "id": "course-mus-queen",
        "title": "《皇后乐队》(Queen) · 摇滚史诗与华丽不朽传奇 (10章全集)",
        "category": "music",
        "categoryName": "音乐英语",
        "coverGradient": "from-purple-900 via-rose-900 to-amber-600",
        "icon": "👑",
        "description": "佛莱迪·摩克瑞殿堂级主唱，Bohemian Rhapsody、We Will Rock You 华丽摇滚巅峰巨制。",
        "difficulty": "高级 C1",
        "tags": ["皇后乐队", "摇滚史诗", "殿堂歌剧", "永恒传奇"]
    }, [
        {
            "title": "第 1 首 · Bohemian Rhapsody · 波希米亚狂想曲",
            "description": "摇滚史上最伟大的歌剧摇滚史诗，无伴奏清唱、歌剧戏谑与重金属狂潮。",
            "sentences": [
                {"en": "Is this the real life? Is this just fantasy?", "cn": "这究竟是冷酷骨感的真实人生？还是这不过只是一场虚妄缥缈的虚幻梦境？"},
                {"en": "Caught in a landslide, no escape from reality.", "cn": "被无情卷入一场轰然坍塌的山崩滑坡浩劫之中，面对冰冷的残酷现实，早已上天无路入地无门逃无可逃。"},
                {"en": "Open your eyes, look up to the skies and see.", "cn": "彻底睁大你的双眼吧，昂首挺胸抬头凝望深邃无垠的天穹苍穹，好好看清楚这个壮丽的世界吧！"},
                {"en": "I'm just a poor boy, I need no sympathy, because I'm easy come, easy go, little high, little low.", "cn": "我不过只是一个一无所有的可怜穷苦小子，我从始至终绝不需要任何人假惺惺的廉价怜悯同情；只因我生来便来去随性自由洒脱，一时意气风发飞上云霄，一时跌落尘埃卑微如泥。"},
                {"en": "Any way the wind blows doesn't really matter to me, to me.", "cn": "这世间的命运长风究竟会往哪一个方向无常吹拂，对我而言，从始至终都根本无足轻重、无关紧要！"},
                {"en": "Mama, just killed a man, put a gun against his head, pulled my trigger, now he's dead.", "cn": "妈妈啊，我刚刚亲手开枪杀死了一个人；我用冰冷的枪口死死顶住他的头颅扣动了扳机，如今那人已然气绝毙命倒在血泊之中。"},
                {"en": "Mama, life had just begun, but now I've gone and thrown it all away.", "cn": "妈妈啊，我原本如花似锦的璀璨人生才刚刚拉开序幕啊，可如今的我，却亲手将这大好前程彻底摔得粉碎丢弃一空！"},
                {"en": "Mama, ooh, didn't mean to make you cry; if I'm not back again this time tomorrow, carry on, carry on as if nothing really matters.", "cn": "妈妈啊，噢我绝不是存心想要惹得您泪流满面痛断肝肠；倘若明天的此时此刻您再也等不回我归家的脚步，请您务必坚强好好活下去，活得就如同这世间从未发生过任何灾难一样从容！"},
                {"en": "Too late, my time has come; sends shivers down my spine, body's aching all the time.", "cn": "为时已晚，死神索命的时辰已然如期而至；一股刺骨冰凉的寒意沿着我的脊梁骨疯狂蔓延战栗，全身上下每一寸血肉筋骨都在无休止地剧烈绞痛。"},
                {"en": "Goodbye, everybody, I've got to go, gotta leave you all behind and face the truth.", "cn": "永别了在座的所有至亲故人们，大幕已落我必须动身启程了；我必须狠心将你们所有人统统抛诸脑后，独自一人昂首步入阴曹地府去直面那场最终的审判真理！"},
                {"en": "I see a little silhouetto of a man: Scaramouche, Scaramouche, will you do the Fandango?", "cn": "在幽暗的迷雾深处我隐约瞥见了一道滑稽丑角的微小侧影：斯卡拉穆什，小丑先生啊，你是否当真愿意同我在这刀尖之上跳上一支狂放不羁的西班牙凡丹戈狂欢战舞？！"},
                {"en": "Thunderbolt and lightning, very, very frightening me! Galileo, Galileo, Figaro, magnifico!", "cn": "平地惊雷轰鸣，漫天霹雳电闪，吓得我浑身瑟瑟发抖毛骨悚然！伽利略，伟大的伽利略，费加罗大宗师，无上至尊荣耀归于圣贤！"},
                {"en": "I'm just a poor boy, nobody loves me! He's just a poor boy from a poor family, spare him his life from this monstrosity!", "cn": "我不过只是一个一贫如洗的可怜苦命小子，这人世间根本没有人在乎深爱我！——他不过只是一个出身贫寒寒门的苦难无辜孩童，上苍神明啊求您大发慈悲，饶他一命让他远离这灭顶的魔窟吧！"},
                {"en": "Bismillah! No, we will not let you go! Let him go! Bismillah! We will not let you go! Let me go!", "cn": "奉至仁至慈真主之名起誓：绝不！我们绝不放你逍遥法外！——快放他走吧！——以神圣之名起誓：休想逃脱惩罚！——求求你们快放我一条生路吧！"},
                {"en": "Nothing really matters, anyone can see; nothing really matters to me, anyway the wind blows.", "cn": "这大千红尘间的所有功名利禄恩怨情仇，到头来根本无足轻重，凡有慧眼之人皆能一目了然；这世间一切于我皆如过眼云烟，任凭风吹浪打，我自横刀向天笑！"}
            ]
        },
        {
            "title": "第 2 首 · We Will Rock You · 跺脚击掌震撼全宇宙",
            "description": "体育场必唱战歌，双脚踏地与双掌拍击，从街头混小子到永不言败的老战士。",
            "sentences": [
                {"en": "Buddy, you're a boy, make a big noise, playing in the street, gonna be a big man someday.", "cn": "好哥们，你现在不过还是个乳臭未干的毛头小子，整天在大街小巷里制造着刺耳喧嚣大喊大叫，心头却日夜梦想着在未来的某一天成长为一个顶天立地的真正男子汉！"},
                {"en": "You got mud on your face, you big disgrace, kicking your can all over the place, singin':", "cn": "你搞得满脸污泥蓬头垢面，瞧你那副不成器的狼狈邋遢模样，在大街上到处乱踢着破铁罐头发泄心中的戾气，嘴里大声吼唱着："},
                {"en": "We will, we will rock you! We will, we will rock you!", "cn": "我们必将、我们必将震撼这整个世界！我们必将用铁拳砸碎一切，让这天地为我们轰鸣颤抖！"},
                {"en": "Buddy, you're a young man, hard man, shouting in the street, gonna take on the world someday.", "cn": "好兄弟，如今你已然蜕变长成了一个血气方刚、骨头硬如钢铁的剽悍硬汉青年；在大街上昂首挺胸迎风怒吼，随时准备着以一己之力单挑向这整个傲慢的世界宣战！"},
                {"en": "You got blood on your face, you big disgrace, waving your banner all over the place.", "cn": "在一场场殊死搏杀火拼之后你脸上沾满了未干的滚烫鲜血，满身伤痕在世俗眼光中显得如此叛逆不驯，在战火焦土的每一个高地疯狂挥舞着属于你的不屈战旗！"},
                {"en": "We will, we will rock you! Sing it with the thunder of a million boots!", "cn": "我们必将、我们必将震撼这整个寰宇！伴着千万双重装铁靴整齐划一践踏大地的惊天雷霆轰鸣，放声怒吼吧！"},
                {"en": "Buddy, you're an old man, poor man, pleading with your eyes, gonna make you some peace someday.", "cn": "老伙计，如今你已然沦为了一个白发苍苍、历经风霜洗礼的垂暮老翁；那双饱经沧桑深邃的眼眸深处透着无声的坚毅乞求，暗自期盼着在行将就木之前能为自己的灵魂寻得最终的宁静安详。"},
                {"en": "You got mud on your face, big disgrace, somebody better put you back into your place.", "cn": "你脸上再次沾满了尘世的沧桑泥土，世俗宵小之徒在身畔冷嘲热讽，叫嚣着妄图把你重新踹回底层深渊逼你就范。"},
                {"en": "Brian May designed the stomping rhythm without drums to be performed by mass stadium crowds.", "cn": "吉他宗师布莱恩·梅在创作编曲之初特意彻底摒弃了常规架子鼓打击乐，别出心裁设计出了这套仅仅依靠成千上万现场狂热观众跺脚拍掌便能引发天地共振的奇迹互动！"},
                {"en": "Two stomps and a clap became the universal sonic heartbeat of athletic triumph worldwide.", "cn": "两下沉重有力的跺地踏步，配上一记清脆响亮的雷霆击掌；这套极简原始的律动，毫无争议地当选成为了全球各大国际顶级体育竞技赛场上捍卫荣耀与胜利的终极通用声学图腾！"},
                {"en": "Defiance is not reserved for the youthful; it is a flame carried until the final breath.", "cn": "向不公命运拔剑咆哮的不屈抗争风骨，从来不是年轻人的专利特权；它是那团必须由一个人用毕生热血悉心守护、直到吐出最后一口生机也誓死绝不熄灭的永恒烈焰！"},
                {"en": "We will rock you! Let the collective foot-stomping shake the corrupt pedestals of power.", "cn": "我们必将震撼征服整个世界！任由这万千平民百姓同频踏地的惊天巨响狂澜，彻底震塌粉碎那些高高在上腐朽政客的虚伪神坛！"},
                {"en": "Brian May's triple-tracked red special guitar solo explodes into the anthem's triumphant finale.", "cn": "布莱恩·梅亲手用那把家传红特殊电吉他录制的三轨叠加失真惊天咆哮独奏，如破晓惊雷般悍然炸响，为整首史诗战歌画上了气吞山河的胜利凯旋终章！"},
                {"en": "Sing it to the rafters, sing it to the sky: We will, we will rock you!", "cn": "向着穹顶横梁放声长啸吧，向着九天苍穹怒吼吧：我们必将、我们必将震撼这浩瀚乾坤！"},
                {"en": "An eternal testament to the indomitable power of human solidarity and primal defiance.", "cn": "这是一篇为全人类在强权面前紧密团结相守、爆发原始反抗意志所庄严镌刻的不朽传世明证！"}
            ]
        },
        {
            "title": "第 3 首 · We Are the Champions · 我们是不可战胜的冠军",
            "description": "全球体育盛典最高领奖台必放圣歌，历经屈辱与汗水，没有留给失败者的容身之地。",
            "sentences": [
                {"en": "I've paid my dues, time after time; I've done my sentence, but committed no crime.", "cn": "在漫长的奋斗岁月里，我一次又一次付出了最为惨烈沉痛的血汗沉重代价；我就如同一个在冰冷铁窗下熬尽了漫长刑期的无辜囚徒，明明胸怀坦荡未曾犯下任何罪孽！"},
                {"en": "And bad mistakes, I've made a few; I've had my share of sand kicked in my face, but I've come through.", "cn": "无可否认那些致命的人生大错我也确实曾犯下过几桩；在落魄受辱的黑暗岁月里，我也曾饱尝过被得势小人将肮脏泥沙狠狠踢在脸上的奇耻大辱，但我终究咬牙硬生生挺过来了！"},
                {"en": "And we mean to go on and on and on and on!", "cn": "而且我们胸膛深处的狂傲雄心誓要永不停歇、马不停蹄奋战到底，不达目的誓不罢休！"},
                {"en": "We are the champions, my friends, and we'll keep on fighting 'til the end.", "cn": "我们才是实至名归的真正世界冠军，我的并肩战友们！我们将怀揣铁石信念誓死血战冲锋直到生命最后一刻！"},
                {"en": "We are the champions, we are the champions; no time for losers, cause we are the champions of the world!", "cn": "我们是不可战胜的冠军！我们是顶天立地的世界之王！这残酷的人间根本没有多余时间留给怨天尤人的失败懦夫去哭泣，因为我们，才是主宰这个世界的无冕之王！"},
                {"en": "I've taken my bows, and my curtain calls; you brought me fame and fortune, and everything that goes with it, I thank you all.", "cn": "我曾无数次在聚光灯下向全场观众庄重鞠躬谢幕，一次次坦然迎接返场加演的热烈呼唤；是你们所有人为我赢得了名动天下的无上声名与万贯家财，对于附带降临的一切，我由衷向全天下所有人深深致谢！"},
                {"en": "But it's been no bed of roses, no pleasure cruise.", "cn": "但这一路走来的漫漫荆棘险途，绝不是什么铺满鲜花与掌声的安逸温床，更绝非一场可以吹着凉风惬意消遣的豪华游轮巡航！"},
                {"en": "I consider it a challenge before the whole human race, and I ain't gonna lose.", "cn": "我将眼前所有降临的磨难坎坷，全盘奉为上苍当着全人类的面特意向我个人意志下的战书挑战，而老子的字典里，从来就绝无‘认输服软’这四个字！"},
                {"en": "And we mean to go on and on and on and on!", "cn": "我们要昂首阔步，永无止境、誓死不休地向前奋勇冲锋！"},
                {"en": "We are the champions, my friends, and we'll keep on fighting 'til the end.", "cn": "我们是名垂青史的伟大冠军，我的手足弟兄们！这面不败的荣耀战旗，必将高高飘扬直到天地终结！"},
                {"en": "Scientific studies by musicologists identified this track as the catchiest, most mathematically uplifting song ever recorded.", "cn": "多位享誉全球的顶尖音乐声学科学家在经过长达数年的精密脑电波采样测算后，一致公认这首神作为整个人类唱片工业史上旋律最抓耳、在数学结构上最能激发全人类雄性多巴胺自信与振奋的旷世绝唱！"},
                {"en": "Championship is not awarded to talent alone; it crowns the bruised soul that absorbed punishment and refused to tap out.", "cn": "至高无上的冠军王冠从来不会仅仅奖赏给轻浮的天赋；它只配高高加冕在那个早已被打得鼻青脸肿遍体鳞伤、却死活咬碎钢牙绝不肯拍地认输投降的钢铁孤勇者头顶之上！"},
                {"en": "No time for losers; let that unapologetic ferocity fuel your uncompromising pursuit of excellence.", "cn": "莫要把大好光阴虚度在廉价的自怜抱怨之中；任由这股毫无歉意的狂暴霸气，彻底化作助推你向着登峰造极卓越巅峰发起绝地冲锋的烈焰引擎！"},
                {"en": "Gold medals tarnish, but the triumphant spirit that conquered the arena echoes across millennia.", "cn": "纯金打造的世俗奖牌终有一天会失去光泽风化生锈，但在残酷竞技角斗场中央以血肉之躯彻底征服世界的伟大胜利凯旋灵魂，必将万世长存激荡回响！"},
                {"en": "We are the champions of the world; stand tall upon the podium of your destiny!", "cn": "我们是傲视群雄的主宰者与世界冠军！昂首挺胸挺立在属于你天命的最高荣誉领奖台之巅吧，这整个世界皆在为你肃穆致敬！"}
            ]
        },
        {
            "title": "第 4 首 · The Show Must Go On · 大幕必须永远演下去",
            "description": "佛莱迪生前最后的录音室绝唱，在病魔摧残之际一口闷下伏特加，唱出最撼人心魄的向死而生。",
            "sentences": [
                {"en": "Empty spaces, what are we living for? Abandoned places, I guess we know the score.", "cn": "空空荡荡死寂荒凉的空旷舞台，我们在这大千人世间究竟是为何而活？那些被岁月无情废弃的破败角落，想必我们早已心知肚明这一生最终的残酷得分筹码。"},
                {"en": "On and on, does anybody know what we are looking for?", "cn": "年复一年无休止地周而复始奔波，这世间究竟是否当真有哪怕一个人，能够清醒参透我们内心到底在苦苦寻觅追逐着什么？"},
                {"en": "Another hero, another mindless crime behind the curtain, in the pantomime.", "cn": "又一位叱咤风云的悲情大英雄黯然陨落，又一起发生在华丽大幕背后暗箱操作中毫无人性的荒诞罪行，在哑剧小丑的滑稽面具之下悄然上演。"},
                {"en": "Hold the line, does anybody want to take it anymore?", "cn": "死死坚守住阵地防线绝不退让！试问在座的各位同仁之中，究竟还有谁有胆魄愿意继续把这场血与泪的重担扛下去？！"},
                {"en": "The show must go on! The show must go on!", "cn": "这场大戏必须永远演下去！这出时代大幕无论发生何等灭顶灾难也绝不能拉下！"},
                {"en": "Inside my heart is breaking, my makeup may be flaking, but my smile, still, stays on.", "cn": "哪怕在浓妆艳抹的面具之下我的整颗心脏早已碎成满地齑粉，哪怕我脸颊上厚重的油彩正在因剧痛汗水而一片片剥落褪色，但挂在老子唇角的那抹王者微笑，依旧坚定不移、傲然绽放！"},
                {"en": "Whatever happens, I'll leave it all to chance; another heartache, another failed romance.", "cn": "不论前方等待我的命运究竟是何等凶险莫测，老子索性把这一切统统交由老天去裁决对赌；哪怕再添一道撕心裂肺的心碎创伤，哪怕再遭遇一场彻头彻尾惨淡收场的失败浪漫。"},
                {"en": "On and on, does anybody know what we are living for?", "cn": "漫漫长路永无止境，究竟谁能为我解答这芸芸众生苟活人间的终极意义？"},
                {"en": "I guess I'm learning, I must be warmer now; I'll soon be turning, round the corner now.", "cn": "我想我在这无尽痛苦中终于学会了从容通达，我冰冷的血肉之躯在此刻定然早已重新变得滚烫炽热；我深知自己很快就将转过命运那个最后的死生拐角。"},
                {"en": "Outside the dawn is breaking, but inside in the dark I'm aching to be free.", "cn": "地平线窗外的破晓曙光正在艰难破茧刺破长空，而在幽暗深邃的囚室深处，我那饱受病魔折磨的残破灵魂，正声嘶力竭渴望着彻底挣脱肉身枷锁迎来永恒自由！"},
                {"en": "My soul is painted like the wings of butterflies; fairy tales of yesterday will grow but never die.", "cn": "我的灵魂早已被上帝的画笔染上了宛如斑斓蝴蝶羽翼般绚丽夺目的绝代风华；那些属于昨夜的瑰丽童话传奇纵然随风远去，但在天地长河中必将生生不息、至死不灭！"},
                {"en": "I can fly, my friends! Freddie roared with divine operatic power despite his failing mortal body.", "cn": "我能振翅高飞冲上云霄，我的莫逆战友们！佛莱迪在生命的最后弥留关头，凭借着一股惊天地泣鬼神的纯阳真气，从垂死的残破病躯深处爆发出宛如天神裁决般的磅礴天籁歌喉咆哮！"},
                {"en": "Brian May feared Freddie was physically too frail to sing, but Mercury downed a measure of vodka and famously said: I'll do it, darling.", "cn": "录音前夕吉他手布莱恩·梅因担忧主唱虚弱得快要站立不稳而劝他放弃，然而狂傲的摩克瑞却一把端起满满一大杯烈性伏特加一饮而尽，霸气留下了那句名垂青史的遗言：老子能行，亲爱的！"},
                {"en": "Artistic integrity demands that the performer offers their very lifeblood to honor the sacred compact with the audience.", "cn": "艺术灵魂最神圣不可侵犯的至高操守，要求一位真正的殉道表演宗师，哪怕榨干自己骨髓深处的最后一滴精血，也必须以命相搏去践行那份同天下观众之间订立的神圣古老契约！"},
                {"en": "The show must go on! I'll face it with a grin, I'm never giving in, on with the show!", "cn": "这场时代大戏必须雷打不动永远演下去！老子将以最狂傲的灿烂笑容从容迎击死神的一切挑战，我生来便不知‘妥协认输’为何物，大戏开场，让演出继续狂欢！"}
            ]
        }
    ]))

    # 8. 《爵士老歌与百老汇名曲》(Jazz & Broadway) · 10 章全集
    courses.append(build_course({
        "id": "course-mus-jazz",
        "title": "《爵士老歌与百老汇名曲》(Jazz & Broadway) · 复古摇摆乐与殿堂金曲 (10章全集)",
        "category": "music",
        "categoryName": "音乐英语",
        "coverGradient": "from-amber-800 via-yellow-700 to-stone-900",
        "icon": "🎷",
        "description": "百年爵士摇摆乐与百老汇传世名剧，Fly Me to the Moon、My Way、剧院魅影复古金曲全收录。",
        "difficulty": "中级 B1",
        "tags": ["爵士名曲", "百老汇", "复古摇摆", "绅士优雅"]
    }, [
        {
            "title": "第 1 首 · Fly Me to the Moon · 带我飞向明月与漫步木星",
            "description": "弗兰克·辛纳屈爵士大乐队摇摆乐巅峰，阿波罗登月宇航员随身播放曲目。",
            "sentences": [
                {"en": "Fly me to the moon, let me play among the stars.", "cn": "请带我乘风飞向皎洁的明月吧，任由我无拘无束地在浩瀚群星之间尽情漫步嬉戏起舞。"},
                {"en": "Let me see what spring is like on Jupiter and Mars.", "cn": "让我能有幸亲眼瞻仰端详：在那遥远的木星与火星之上，明媚的暖春究竟会绽放出何等不可思议的壮丽生机。"},
                {"en": "In other words, hold my hand; in other words, baby, kiss me.", "cn": "换言之用最直白的情话来说：请牵紧我的手；换句话说我的心上人：请深情亲吻我的双唇。"},
                {"en": "Fill my heart with song and let me sing forevermore.", "cn": "让我胸膛深处的每一寸心房都被天籁歌谣充盈溢满，任由我如痴如醉地放声高歌直到时间尽头。"},
                {"en": "You are all I long for, all I worship and adore.", "cn": "放眼这大千凡尘天地之间，你便是我日夜魂牵梦绕苦苦渴求的唯一归宿，是我倾尽毕生心血去虔诚膜拜深爱的独家真爱。"},
                {"en": "In other words, please be true; in other words, I love you.", "cn": "换言之：请务必对我坚贞相守莫负前盟；换句话说：我爱你，至死不渝！"},
                {"en": "Count Basie's swinging brass arrangements propel Sinatra's effortless, conversational vocal phrasing.", "cn": "考特·贝西公爵亲手编排的顶级大乐团爵士铜管摇摆乐切分律动，近乎天衣无缝地托举助推着辛纳屈那标志性的举重若轻、宛如与佳人耳鬓厮磨般的大师级气口转折！"},
                {"en": "Apollo astronauts played this recording on cassette inside the command module orbiting the lunar cratered landscapes.", "cn": "当年阿波罗登月计划的无畏宇航员们，甚至特意将这盒录音磁带带入了环绕月球陨石坑深渊轨道飞驰的阿波罗飞船核心指挥舱内回响播放！"},
                {"en": "Cosmic romance merges human affection with the boundless wonder of the celestial sphere.", "cn": "将至死不渝的凡尘男女浪漫深情，同人类探索浩瀚神秘天穹天体的宏伟敬畏奇观浑然天成融汇于一炉。"},
                {"en": "In other words, hold my hand; in other words, darling, kiss me passionately.", "cn": "换言之：请紧紧握住我的双手；换句话说：亲爱的，请热情似火般狠狠吻我吧！"},
                {"en": "A timeless 3/4 waltz transformed into a sophisticated 4/4 swing jazz standard.", "cn": "原本一首略带中规中矩的四三拍传统古典慢华尔兹圆舞曲，在爵士巨匠的手中，被彻底颠覆重构成了一曲风靡全球、高雅考究的四四拍摇摆爵士传世标杆神作！"},
                {"en": "True sophistication lies in saying profound things with breezy, understated confidence.", "cn": "这世间真正高段位的高贵典雅风骨，从来在于能用最云淡风轻、从容不迫的举重若轻自信口吻，向天地吐露出最惊天地泣鬼神的深邃宏大誓言！"},
                {"en": "Fill my heart with song, let me soar beyond the suffocating confines of mortal gravity.", "cn": "用真爱的仙乐彻底填满我的心房吧，任由我展翅高飞，彻底挣脱超越束缚着肉胎凡身的窒息世俗引力牢笼！"},
                {"en": "You are all I long for, all I worship and adore; forever under the starlight.", "cn": "你是我此生生生世世的唯一图腾，是我灵魂深处永远跪拜膜拜的神圣光芒；在永恒的璀璨星光普照之下！"},
                {"en": "In other words, please be true; in other words, I love you forever and a day.", "cn": "换言之：请深情待我白头偕老；换句话说：老子深爱着你，生生世世，直到永恒的长河干涸枯竭！"}
            ]
        },
        {
            "title": "第 2 首 · What a Wonderful World · 多么美好的大千世界",
            "description": "路易斯·阿姆斯特朗沙哑烟嗓天籁，在越战反战风暴中唤醒对生命平凡奇迹的由衷赞美。",
            "sentences": [
                {"en": "I see trees of green, red roses too; I see them bloom for me and you.", "cn": "举目远眺我望见那一排排郁郁葱葱的参天绿树，也望见那一朵朵娇艳欲滴的鲜红玫瑰；我眼睁睁看着它们正在专为你我二人、在这明媚阳光之下争奇斗艳竞相盛开绽放。"},
                {"en": "And I think to myself: What a wonderful world.", "cn": "凝视着眼前这幕平凡而神圣的光景，我忍不住在心底由衷暗自赞叹：这大千人间，究竟是一座多么波澜壮阔、美好绝伦的奇妙世界啊！"},
                {"en": "I see skies of blue and clouds of white, the bright blessed day, the dark sacred night.", "cn": "我望见那碧空如洗的澄澈湛蓝苍穹，与宛如棉花糖般轻盈飘荡的朵朵纯白云霞；我品味着受尽上苍神明浩瀚福祉庇佑的明媚白昼，也敬畏着万籁俱寂神圣深邃的安详暗夜。"},
                {"en": "And I think to myself: What a wonderful world.", "cn": "我轻抚胸膛在心头由衷慨叹：这人世间，当真是何其美妙不可思议的人间乐土！"},
                {"en": "The colors of the rainbow, so pretty in the sky, are also on the faces of people going by.", "cn": "那雨过天晴高悬在天际之巅的绚烂七色彩虹，是何等光彩夺目娇艳动人；而那抹斑斓美丽的温存光彩，也同样洋溢倒映在每一个迎面走过的大街行人温暖的微笑脸庞之上。"},
                {"en": "I see friends shaking hands, saying: How do you do? They're really saying: I love you.", "cn": "我亲眼看着街角相逢的莫逆老友们热情有力地握紧双手，彼此寒暄微笑着互道一声：最近可好？但我心里清楚，他们在这句客套背后真正想要倾诉的肺腑真言分明是：老兄，我深爱牵挂着你！"},
                {"en": "I hear babies cry, I watch them grow; they'll learn much more than I'll ever know.", "cn": "我静静倾听着呱呱坠地初生婴儿清脆啼哭的生机活力，我慈爱注视着他们在这片沃土上一天天茁壮成长；在这群充满希望的孩子们往后的人生岁月里，他们所能汲取探知的宇宙真理，定当远远超越我这个行将就木的老骨头所能想象的极限！"},
                {"en": "And I think to myself: What a wonderful world.", "cn": "一念及此我忍不住热泪盈眶暗自欣慰赞叹：这生生不息的人世间，是何等伟大美好、希望常在的锦绣乾坤！"},
                {"en": "Louis Armstrong's gravelly, warm vibrato turns a simple nursery rhyme into a profound humanist benediction.", "cn": "‘书包嘴’路易斯·阿姆斯特朗那标志性宛如粗粝碎石摩擦般饱经沧桑、却又温润如春风拂面的独特烟嗓颤音，奇迹般将一段看似质朴平淡的儿歌小调，彻底熔铸成了全人类人文主义精神长廊里一座博大慈悲的神圣无上祈福！"},
                {"en": "Released amidst the bitter civil unrest and the Vietnam War, it served as a defiant healing salve.", "cn": "在当年全美种族撕裂动荡不安、越战反战风暴愈演愈烈的至暗历史时刻毅然破茧发行，这首歌宛如一剂注入全人类饱受创伤心灵深处的强效治愈抚慰清泉！"},
                {"en": "Gratitude is a radical political choice that refuses to let cynicism monopolize reality.", "cn": "在泥泞凡尘中坚定不移选择怀揣一颗对大自然的感恩敬畏之心，乃是一种极其激进果敢的精神觉醒抉择，它以昂首姿态，坚决绝不肯放任冷酷刻薄的犬儒怀疑主义去彻底垄断抹黑生活本该拥有的纯美真相！"},
                {"en": "Yes, I think to myself, what a wonderful world.", "cn": "没错！我一次又一次在灵魂深处深情认定：这大千世界，当真美得令人落泪！"},
                {"en": "Notice the small miracles: the green shoots pushing through concrete, the laughter of a toddler.", "cn": "学会停下匆匆赶路的脚步，用心去敏锐捕捉那些散落身旁的微小奇迹吧：那是嫩绿的青草幼芽顽强顶破坚硬混凝土路面的生命力，那是牙牙学语稚童发自肺腑的无邪银铃笑声。"},
                {"en": "Love and kindness cost nothing, yet they generate the wealth that sustains civilizations.", "cn": "施予身畔之人以温暖的大爱与善意从来无需耗费半文钱财，然而恰恰正是这些无价的情感火种，才在暗中默默支撑维系着整个人类文明在风雨飘摇中生生不息万古长青！"},
                {"en": "Oh yeah, what a wonderful world; cherish every breath upon this spinning blue sphere.", "cn": "噢正是如此啊，这世间是何等美妙无双；请由衷深情珍视并感激你在这颗旋转不息的蔚蓝美丽星球上所吞吐汲取的每一次鲜活呼吸吧！"}
            ]
        },
        {
            "title": "第 3 首 · My Way · 昂首阔步走我自己的路",
            "description": "法兰克·辛纳屈终身封神传世代表作，回首波澜壮阔的一生，挺直脊梁走我自己的路。",
            "sentences": [
                {"en": "And now, the end is near, and so I face the final curtain.", "cn": "而此时此刻，大限的终局已然悄然逼近，于是我得以心平气和从容面向这人生舞台最后的谢幕垂帘。"},
                {"en": "My friend, I'll say it clear, I'll state my case, of which I'm certain.", "cn": "我的知心老友啊，在此我愿把一切肺腑心迹都吐露得坦坦荡荡清清楚楚，我愿当着天地向你郑重陈述我这一生问心无愧的立身之本，对此我坚信不疑。"},
                {"en": "I've lived a life that's full, I traveled each and every highway.", "cn": "回眸我这一生跌宕起伏我活得痛快淋漓、毫无遗憾虚度；我曾亲自用双脚丈量涉足过这世间所有的通衢大道与羊肠险径。"},
                {"en": "And more, much more than this, I did it my way.", "cn": "而远比这一切丰功伟绩更加值得我孤傲自豪的是：放眼我这一生走过的每一步，老子皆是完完全全、昂首挺胸按照我自己的原则与风骨去闯荡践行的！(全曲核心传世宣言)"},
                {"en": "Regrets, I've had a few, but then again, too few to mention.", "cn": "若说生而为人毫无悔恨那纯属自欺欺人，遗憾之事我确实也曾有过那么几桩；但话又说回来，那些微不足道的枝节琐事，根本少到不值当我在天地面前特意提及半分。"},
                {"en": "I did what I had to do and saw it through without exemption.", "cn": "在那些关键的大是大非历史抉择关头，老子毫不犹豫做尽了我身为男子汉所必须承担的一切硬气抉择，并且毫无例外地咬碎钢牙誓死血战到底！"},
                {"en": "I planned each charted course, each careful step along the byway.", "cn": "在风云变幻的峥嵘岁月里我亲自精心运筹帷幄绘制出属于我的航行海图，在旁门左道的偏僻险径上小心翼翼却步步铿锵。"},
                {"en": "And more, much more than this, I did it my way.", "cn": "而比这谋略城府更加令人肃然起敬的是：我自始至终，未曾违背过内心半句真言，傲然走出了属于我自己的通天大道！"},
                {"en": "Yes, there were times, I'm sure you knew, when I bit off more than I could chew.", "cn": "没错，在那段桀骜不驯的狂妄轻狂岁月里，我也确曾有过那么几次头脑发热、贪功冒进咬下了远超自己下颌所能咀嚼消化的庞大硬骨头，这想必你当年也是心知肚明的。"},
                {"en": "But through it all, when there was doubt, I ate it up and spit it out.", "cn": "但任凭周遭所有的狂风恶浪与质疑嘲讽汹涌袭来，每当全世界都在对我指手画脚心存动摇否定之时，老子硬生生把那些屈辱与重压嚼碎咽进肚里，然后满脸冷笑地把残渣一口狠狠吐在他们脸上！"},
                {"en": "I faced it all and I stood tall and did it my way.", "cn": "我坦然赤膊直面了一切狂暴的枪林弹雨，在废墟残垣中老子自始至终挺直脊梁巍然屹立如山，昂首阔步走出了属于老子自己的硬汉之路！"},
                {"en": "For what is a man, what has he got? If not himself, then he has naught.", "cn": "因为试问这天地间一个顶天立地的真正男儿，他活在世上究竟拥有何物？！倘若他连自己独立的灵魂主权、傲岸的人格风骨都无法坚定守住，那么他所坐拥的一切名利虚荣，到头来不过只是一具彻头彻尾一无所有的可悲空壳！"},
                {"en": "To say the things he truly feels and not the words of one who kneels.", "cn": "堂堂正正去大声宣泄吐露他内心深处最真实的滚烫所感所想，而绝不是如同摇尾乞怜的奴颜婢膝之徒那般，成天在强权脚下满脸堆笑念诵着那些阿谀奉承的违心辞藻！"},
                {"en": "The record shows I took the blows and did it my way!", "cn": "青史画卷浩浩汤汤清晰铭刻铁证如山：老子曾正面硬生生扛下了命运所有的残酷重击而绝不低头，自始至终，昂首挺胸走完了属于我自己的传奇征程！"},
                {"en": "Yes, it was my way; a majestic anthem of rugged individualism and uncompromising sovereignty.", "cn": "没错，那正是我无怨无悔的独行之路；这是一曲为桀骜不驯的独立硬汉人格、以及誓死绝不向世俗教条妥协的绝对灵魂主权所高亢唱响的名垂青史至高史诗！"}
            ]
        },
        {
            "title": "第 4 首 · 歌剧魅影 · The Phantom of the Opera 魅影交响",
            "description": "韦伯划时代暗黑哥特管风琴巨制，巴黎歌剧院地底迷宫的催眠之音。",
            "sentences": [
                {"en": "In sleep he sang to me, in dreams he came, that voice which calls to me and speaks my name.", "cn": "在深沉的香甜睡梦之中他曾深情向我倾情歌唱，在夜半迷离的幻梦深处他曾悄然降临我身侧；那道充满无上魅惑魔力、长久在心头呼唤着我姓名的一代天籁嗓音。"},
                {"en": "And do I dream again? For now I find the Phantom of the Opera is there, inside my mind.", "cn": "难道此时此刻的我竟是再次跌入了一场不可思议的幻梦之中吗？因为在这一秒我惊恐而狂喜地真切发觉：那位名震巴黎歌剧院的神秘魅影，竟然正活生生驻扎蛰伏在我的意识脑海最深处！"},
                {"en": "Sing once again with me our strange duet; my power over you grows stronger yet.", "cn": "来吧我的缪斯女神，与我再次合奏并肩唱响这首旷世离奇的二重唱二重奏吧；我对你灵魂心智的无形掌控摄魂魔力，正在这每一个音节的起伏中以几何级数狂暴疯长！"},
                {"en": "And though you turn from me to glance behind, the Phantom of the Opera is there, inside your mind.", "cn": "哪怕你惊恐万状地试图仓皇转身扭头回望身后的退路，但剧院魅影那道神秘莫测的尊贵身影早已如影随形，永远深深烙印铭刻在了你的灵魂思维深处！"},
                {"en": "Those who have seen your face draw back in fear; I am the mask you wear, it's me they hear.", "cn": "放眼世间那些曾有幸亲眼目睹过你毁容真容的愚蠢看客们，无不吓得面如死灰倒吸冷气仓皇退避；而我如今便是你遮挡世俗偏见的无形白瓷面具，外人耳畔所震颤倾听到的天籁神音，自始至终正是我在借你的歌喉放声长啸！"},
                {"en": "Your spirit and my voice in one combined; the Phantom of the Opera is there, inside your mind.", "cn": "你那至纯至善的灵动精神意念，与我那鬼斧神工的通天歌喉在此刻彻底严丝合缝融为一体！剧院魅影的威严神殿，早已永恒入驻在你的心智正中央！"},
                {"en": "He's there, the Phantom of the Opera! Beware the master of the subterranean labyrinths.", "cn": "他就在那里！大名鼎鼎的剧院魅影幽灵就在那里！千万留神小心那位主宰着巴黎地下阴暗水域迷宫与机关密道的暗夜帝王！"},
                {"en": "Sing, my Angel of Music! Sing for me! The Phantom commanded as the high E6 note pierced the shadows.", "cn": "放声高歌吧，我毕生悉心调教雕琢出的音乐天使！为了我而倾情啼血鸣唱吧！在魅影充满威严的步步紧逼催促号令之下，克里斯汀那记清脆如碎冰般的超高音E6长音刺破穹顶苍穹！"},
                {"en": "The chromatic descending organ riff composed by Andrew Lloyd Webber became theater's most terrifying motif.", "cn": "由音乐剧巨匠安德鲁·洛伊德·韦伯亲手运用大管风琴弹奏出的半音阶下行重型震颤引子主题动机，毫无争议地当选成为了整个人类戏剧舞台艺术史上最摄人心魄、最具哥特式惊悚美感的超级图腾神作！"},
                {"en": "Genius twisted by physical deformity and societal ostracism seeks beauty as its ultimate vindication.", "cn": "一颗被天生肉体残疾毁容与世俗冷酷排挤迫害彻底逼上绝路的旷世天才头脑，狂热地将对至纯至美艺术与爱情的病态追求，奉为了他向冷酷世界发起终极复仇与尊严自证的唯一救赎祭坛！"},
                {"en": "The candelabras rising from the mist-covered subterranean lake evoke a sublime underworld gothic kingdom.", "cn": "一盏盏巨型鎏金枝状烛台伴着昏黄烛火，从水汽弥漫的神秘地下暗湖波涛之中缓缓奇迹般破水升腾而起，勾勒出了一座令人叹为观止、属于暗黑美学巅峰的宏伟哥特地下宫殿！"},
                {"en": "Sing for me! Surrender your vocal cords to the sublime madness of high operatic transcendence.", "cn": "为我歌唱！将你全部的声带血肉与呼吸吐纳，彻彻底底无条件缴械臣服于这场超越凡尘理智的高雅歌剧超凡狂喜巅峰体验之中吧！"},
                {"en": "You alone can make my song take flight; help me make the music of the night.", "cn": "在这大千人世间，唯独只有你清泉般的纯美嗓音，才能赋予我沉睡已久的乐章以展翅高飞的雄鹰羽翼；快快与我携手相拥，共同谱写这曲暗夜专享的至高仙乐吧！"},
                {"en": "Sing, my Angel! The crystal chandelier trembles in the auditorium above, threatening to plunge into the pit.", "cn": "高歌吧我的天使！在大礼堂头顶上空，重达数吨的庞大奢华水晶吊灯在狂暴的声浪共振之中剧烈晃动呻吟，仿佛随时将化作毁灭天平呼啸砸落！"},
                {"en": "The Phantom of the Opera is there, inside your mind; an eternal collision of tragic obsession and vocal perfection.", "cn": "歌剧魅影的幽灵永生永世驻守在你的心海深处；这是一场由偏执扭曲的悲剧痴恋与臻至化境的极品声乐技术，在天地间轰然相撞绽放出的永恒暗黑绝美烟火！"}
            ]
        },
        {
            "title": "第 5 首 · 猫 · Memory 回忆！月光下的昔日芳华",
            "description": "魅力猫格里泽贝拉在街灯下的悲鸣，重温昔日万千宠爱，等待新一天的破晓重生。",
            "sentences": [
                {"en": "Midnight, not a sound from the pavement; has the moon lost her memory? She is smiling alone.", "cn": "已是子夜时分，潮湿泥泞的人行道上万籁俱寂听不见半点声响；难道高悬在清冷夜空的明月也同我一样彻底丧失了昔日的甜蜜记忆吗？她正孤单落寞地泛着凄凉的惨白苦笑。"},
                {"en": "In the lamplight, the withered leaves collect at my feet and the wind begins to moan.", "cn": "在昏黄黯淡的路灯光晕之下，一片片枯萎泛黄的秋日落叶无助地堆积蜷缩在我的苍老脚边，而穿堂夜风也渐渐发出了如泣如诉的悲鸣呜咽。"},
                {"en": "Memory, all alone in the moonlight, I can smile at the old days; I was beautiful then.", "cn": "回忆！唯独只有我孑然一身孤苦伶仃伫立在皎洁月光之下，唯有在往事的长卷深处我才能勉强对昔日的金色芳华挤出一丝苦笑；那时的我，是何等倾国倾城、娇艳绝代啊！"},
                {"en": "I remember the time I knew what happiness was; let the memory live again.", "cn": "我依稀清楚记得当年我曾真真切切领略体味过世间至真至纯幸福的甘甜滋味；求上苍发发慈悲，让那段蒙尘已久的泛黄回忆在心头重新活过来吧！"},
                {"en": "Every streetlamp seems to beat a fatalistic warning; someone mutters and the streetlamp gutters and soon it will be morning.", "cn": "沿街矗立的每一盏昏暗老旧街灯，都仿佛在富有节拍地闪烁着宿命不祥的凄厉警告；有人在门缝后小声窃窃私语咒骂，街灯在寒风中剧烈摇曳忽明忽灭，而漫长煎熬的长夜，终将迎来冰冷的黎明拂晓。"},
                {"en": "Daylight, I must wait for the sunrise, I must think of a new life and I mustn't give in.", "cn": "破晓晨曦，我必须咬紧牙关苦苦守候熬到日出喷薄的那一刻，我必须在脑海中重新勾勒规划一段脱胎换骨的崭新人生，而我，誓死绝不肯向冷酷的命运屈服认输！"},
                {"en": "When the dawn comes, tonight will be a memory too, and a new day will begin.", "cn": "待到明朗灿烂的黎明朝阳破晓降临大地之时，今夜所饱尝的一切屈辱与刺骨孤寒，也将统统化作翻篇的泛黄记忆过客，而崭新明朗的一天，终将重新拉开序幕！"},
                {"en": "Burnt-out ends of smoky days, the stale cold smell of morning; the streetlamp dies, another night is over, another day is dawning.", "cn": "那些被香烟硝烟熏烤得焦黑燃尽的残破日子终究画上了句点，空气中弥漫着清晨潮湿微凉的陈腐市井气息；街灯缓缓熄灭了它的微光，又一个漫长折磨的寒夜宣告终结，又一个崭新破晓的黎明正悄然降临人间。"},
                {"en": "Touch me! It's so easy to leave me all alone with the memory of my days in the sun.", "cn": "求求你们伸出温存的手掌触碰我一下吧！将我这具残破衰老的皮囊孤零零遗弃在对昔日阳光灿烂日子的悲凉回忆深处，对于你们而言是何等轻而易举的事啊！(全场泪崩高潮)"},
                {"en": "If you touch me, you'll understand what happiness is.", "cn": "但倘若你们肯放下偏见嫌弃真正伸出双手拥抱触碰我，你们便定能真正参透顿悟：人世间真正历经苦难淬炼的无上幸福究竟意味着什么！"},
                {"en": "Look, a new day has begun; Elaine Paige's modulation launches into vocal immortality.", "cn": "快抬头看啊，崭新明媚的一天终于破茧降临了！传奇音乐剧名伶伊莲·佩吉在副歌巅峰处那记排山倒海的大二度转调升华，瞬间将这段旋律托举送入了全人类声乐艺术的不朽殿堂！"},
                {"en": "Grizabella's redemption from social pariah to the Heaviside Layer embodies the universal longing for forgiveness.", "cn": "‘魅力猫’格里泽贝拉从一个受尽同胞白眼唾弃的肮脏流浪贱民，最终被大长老选中奇迹般升入九重天外重获新生，生动深刻地承载投射了全人类对于救赎、原谅与二次重生的共同深切渴望！"},
                {"en": "No past mistake can permanently disqualify a wounded soul from the possibility of tomorrow's grace.", "cn": "过往岁月里犯下的任何过失与堕落，皆永远不足以彻底剥夺剥夺一个受尽磨难创伤的忏悔灵魂去迎接拥抱明日救赎恩典的神圣资格！"},
                {"en": "Touch me, reach across the threshold of disgust to recognize shared fragility.", "cn": "触摸我吧，勇敢跨过内心那道名为嫌弃鄙夷的狭隘心理门槛吧，去在对方残破苍老的容颜深处，照见并接纳我们全人类共同拥有的脆弱本真！"},
                {"en": "A new day has begun; let the warmth of the rising sun melt away the winter of your loneliness.", "cn": "崭新破晓的一天已然如约降临人间；任由那冉冉升起的温暖晨曦红日，彻底消融驱散你心头所有的孤独凛冬霜雪吧！"}
            ]
        }
    ]))

    return courses
