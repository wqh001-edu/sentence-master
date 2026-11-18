# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))
from builder_core import build_course, save_ts_file
import music_part1
import data_music
import gen_music_full
import music_part3

def build_music_all():
    print("🎸 [开始构建] 音乐英语 8 门全集课程...")
    courses = []

    # 1. 披头士 (已在 music_part1 中完成 10 章)
    courses.extend(music_part1.get_music_part1())

    # 2. 泰勒·斯威夫特 (已在 data_music 中完成 10 章)
    courses.append(data_music.get_all_music()[1])

    # 3. 迪士尼经典动画主题曲 (已在 gen_music_full 中完成 10 章)
    courses.append(gen_music_full.generate_music()[2])

    # 4. 阿黛尔 (完成 10 章)
    adele_part1 = music_part3.get_music_part3()[0]
    courses.append(adele_part1)
    # 为阿黛尔补齐后 5 首 (6~10)
    adele_extra_chapters = [
        {
            "title": "第 6 首 · Easy on Me · 对我宽容一点与成长释怀",
            "description": "三十岁自省之作，在婚姻废墟中向孩子与自己吐露脆弱心声。",
            "sentences": [
                {"en": "There ain't no gold in this river that I've been washin' my hands in forever.", "cn": "在这条我长年累月不断濯洗双手的浑浊河流深处，根本就淘洗不出任何闪光的金金砂金。"},
                {"en": "I know there is hope in these waters, but I can't bring myself to swim.", "cn": "我心里清楚这片汪洋深处或许依稀泛着希望的微光，可疲惫不堪的我却再也鼓不起力气纵身潜入游弋。"},
                {"en": "When I am drowning in this silence, baby, let me in.", "cn": "每当我在这一片令人窒息的万籁死寂深渊中快要溺水沉沦时，宝贝，求你向我敞开心门。"},
                {"en": "Go easy on me, baby; I was still a child, didn't get the chance to feel the world around me.", "cn": "请对我宽容体谅一点吧，我的孩子；当年初为人母的我骨子里也还不过只是个懵懂孩童，甚至还未曾来得及从容触摸体察周遭的浩瀚世界。"},
                {"en": "I had no time to choose what I chose to do, so go easy on me.", "cn": "那时的我根本未曾拥有充足的光阴去审慎权衡我做出的每一次重大抉择，所以，请对我宽容一点吧。"},
                {"en": "There ain't no room for things to change when we are both so deeply stuck in our ways.", "cn": "当我们彼此双方都固执己见、死死深陷在各自根深蒂固的处世坚壳里无法自拔时，一切便再无任何挽回变通的余地。"},
                {"en": "You can't deny how hard I have tried; I changed who I was to put you both first, but now I give up.", "cn": "你无论如何也绝无法矢口否认我曾多么拼尽全力去尝试挽救；我曾不惜彻底扭曲磨灭真实的自我，只为把你们父子排在第一位，但如今，我终于决定放手释怀。"},
                {"en": "I had good intentions, and the highest hopes, but I know right now that probably doesn't even show.", "cn": "我最初的出发点怀揣着无可挑剔的纯良初衷，胸膛里曾装满了最热烈美好的崇高期盼，但我心知肚明，在此时此刻一地鸡毛的残局面前，这些表白显得何等苍白无力。"},
                {"en": "A divorce ballad centered on forgiving oneself for not sustaining an unsustainable union.", "cn": "这是一曲聚焦于同自我达成深层次精神和解、原谅自己未能在一场早已难以为继的病态婚姻中勉强苦撑下去的灵魂救赎长歌。"},
                {"en": "Maternal honesty requires admitting that self-preservation is a prerequisite for nurturing others.", "cn": "一位为人母者最崇高纯粹的诚实，莫过于坦然正视并承认：唯有先保全好自身内心的完整健康，方能拥有滋养呵护骨肉至亲的情感资本。"},
                {"en": "Go easy on me, baby; I put my hands up in surrender and walked away with tears.", "cn": "对我宽容体谅一些吧孩子；我高举双手认输投降，在止不住的泪水中平静转身走向崭新的人生篇章。"},
                {"en": "Sometimes the bravest act of love is dismantling a hollow facade before it collapses on everyone.", "cn": "有时候世间最勇敢无畏的崇高大爱，反而是赶在一座早已空洞腐朽的虚伪大厦轰然倒塌砸伤所有人之前，主动将其体面拆除。"},
                {"en": "The solitary piano chords echo with the quiet finality of a courtroom gavel and a mother's sigh.", "cn": "孤单落寞的大三角钢琴琴音低回沉吟，回荡着宛如法庭终审法槌落定般的决然终章，以及一位母亲释怀后悠长的叹息。"},
                {"en": "I had no time to choose what I chose to do, so go easy on me.", "cn": "我当年未曾拥有岁月给予的从容智慧去深思熟虑，所以，请宽容接纳曾经那个不完美的我。"},
                {"en": "Forgiveness begins in the mirror; grant yourself the grace you readily extend to strangers.", "cn": "人世间真正的宽恕与释怀始于直视穿衣镜中的真实自我；由衷赐予你自己那份你平日里总能轻而易举施予陌路生人的博大宽容吧！"}
            ]
        },
        {
            "title": "第 7 首 · When We Were Young · 当我们正当年少与泛黄合影",
            "description": "老友重逢聚会上的时光感慨，害怕老去的容颜与紧紧拥抱的年少温存。",
            "sentences": [
                {"en": "Everybody loves the things you do, from the way you talk to the way you move.", "cn": "在座的所有老朋友都由衷由衷喜欢你举手投足间展现出的万千风采，从你谈吐间的高雅幽默，到你从容漫步时的迷人身姿。"},
                {"en": "Everybody here is watching you, cause you feel like home, you're like a dream come true.", "cn": "满堂相聚的宾客目光无一不在深情聚焦注视着你，只因你的温存让人恍惚感到如沐春风的踏实归属，你宛如一场在现实中成真的唯美幻梦。"},
                {"en": "But if by chance you're here alone, can I have a moment before I go?", "cn": "但倘若今夜造化弄人你正好也是孤身一人赴宴，在我动身离席之前，不知我是否有幸能同你单独借一步温存交谈片刻？"},
                {"en": "Cause I've been by myself all night long, hoping you're someone I used to know.", "cn": "只因我整整一整夜都落寞孤单地独坐在角落里，暗自苦苦企盼你正是我昔日那段青葱岁月里相濡以沫的故人旧识。"},
                {"en": "You look like a movie, you sound like a song; my God, this reminds me of when we were young.", "cn": "你的眉眼宛如一出跌宕起伏的经典光影大片，你的歌喉宛如一首传世长青的悠扬歌谣；天呐这所有的一切，瞬间将我拽回到了当年正当年少时的美好时光！"},
                {"en": "Let me photograph you in this light in case it is the last time that we might be exactly like we were.", "cn": "请允许我趁着这抹温柔的烛光为你定格下一张合影相片吧，万一这恰恰是我们此生最后一次能够完完全全重拾昔日青春神采的相聚呢？"},
                {"en": "Before we realized we'd grown up, we were terrified of getting old, it made us restless.", "cn": "早在我们后知后觉意识到自己早已长大成人之前，我们曾对白发渐生的衰老老去感到毛骨悚然的惊恐，那份迷茫曾让我们惶惶不可终日。"},
                {"en": "It's hard to win it all, but you know you still make my heart race like a wild stallion.", "cn": "在这功利的世俗尘世间想要赢尽一切何其艰难，但你心里清楚：哪怕到了今天，你的一颦一笑依然能让我胸膛深处的心脏如狂暴的野马般剧烈狂跳！"},
                {"en": "It was just like a movie, it was just like a song.", "cn": "那段如火如荼的过往岁月恰似一出永不落幕的胶片电影，恰如一首百转千回的传世长歌。"},
                {"en": "I'm so mad I'm getting old, it makes me reckless; it was just like a song when we were young.", "cn": "我常常对自己无可挽回地日渐衰老苍老感到无比恼火抓狂，这甚至让我变得愈发任性不顾后果；但当我们正当年少风华正茂之时，生活处处皆如天籁神曲！"},
                {"en": "Tobias Jesso Jr.'s vintage seventy's piano voicing echoes Elton John and Carole King.", "cn": "托比亚斯·杰索二世精心设计的七十年代复古钢琴和弦和声，深情致敬回荡着埃尔顿·约翰与卡洛尔·金等老牌流行宗师的黄金风骨。"},
                {"en": "Aging is not the enemy of romance; forgetting the fire of your youth is the true tragedy.", "cn": "生理年龄的苍老从来不是浪漫主义的大敌；在庸常世俗的生活磨损中彻底忘却了青春岁月的滚烫热血烈火，才是人生至深的真正悲剧！"},
                {"en": "Take my trembling hand; let us dance one final slow-dance before midnight strikes the hour.", "cn": "牵起我微微发颤的双手吧；让我们在午夜钟声敲响之前，最后一次伴着老歌跳完这支依依不舍的舒缓慢舞。"},
                {"en": "Let me photograph you in this light, so I can carry your youthful glow through the coming shadows.", "cn": "让我将你此刻沐浴在柔光下的绝代风华永远定格在相片画卷中吧，如此这般，我便能携带着你青春的璀璨光芒，勇敢穿行过前方未知的所有暗夜阴霾。"},
                {"en": "It was just like a movie; it was just like a song when we were young.", "cn": "那一幕幕泛黄过往如影如幻恰似大片，那一曲曲少男少女的欢笑歌谣，正是我们当年正值青春年少的永恒芳华！"}
            ]
        },
        {
            "title": "第 8 首 · Chasing Pavements · 徒劳追逐与十字路口的抉择",
            "description": "十九岁成名处女作，在伦敦人行道上徘徊，究竟该坚持还是放手？",
            "sentences": [
                {"en": "I've made up my mind, don't need to think it over; if I'm wrong, I am right, don't need to look no further.", "cn": "我已然在心头拿定了主意，再也无需患得患失翻来覆去权衡；即便全世界都断定我是错的我亦无怨无悔，再也无需左顾右盼四处张望。"},
                {"en": "This ain't lust, I know this is love, but, if I tell the world, will they even care?", "cn": "这绝非肉欲皮相的一时冲动，我比谁都清楚这是深入骨髓的至纯真爱；然而，倘若我向全世界大声宣告，这冷漠的人间又是否当真有人在乎？"},
                {"en": "Should I give up, or should I just keep chasing pavements, even if it leads nowhere?", "cn": "我究竟该理智认输彻底放弃？还是该执迷不悟继续在冰冷空旷的人行道水泥路面上徒劳追逐奔跑，哪怕它通向的唯有一无所有的虚无死胡同？！"},
                {"en": "Or would it be a waste, even if I knew my place; should I leave it there?", "cn": "亦或者这从始至终不过是一场彻头彻尾的愚蠢挥霍，即便我早已清醒摆正了自己的卑微位置；我是否该就此止步、将这孽缘永远封存原地？"},
                {"en": "Should I give up, or should I just keep chasing pavements, even if it leads nowhere?", "cn": "我到底该当机立断斩断情丝？还是该任凭双脚在空荡荡的马路上狂奔追逐残影，即便前方等待我的唯有无尽深渊？"},
                {"en": "I build myself up and fly higher everyday; I think of what you say and then I fall right back down.", "cn": "我日复一日好不容易重塑起自信的翅膀振翅高飞，可每当我脑海中不由自主回想起你昔日那些冷言冷语时，我便又瞬间直直自高空重重摔落回冰冷泥潭。"},
                {"en": "I try to keep my distance, but the gravitational pull of your memory breaks my resolve.", "cn": "我竭尽全力拼命同你拉开天涯海角的遥远距离，然而你残存记忆那股恐怖的万有引力，总能在顷刻之间击溃我所有的心理防线。"},
                {"en": "The lush string swells and 6/8 acoustic guitar provide a waltz of romantic despair.", "cn": "如潮水般层层递进奔涌的奢华弦乐合奏，配上八分之六拍摇曳的古典木吉他分解和弦，交织成了一支令人心碎神伤的绝望浪漫圆舞曲。"},
                {"en": "An empty pavement reflects the cold neon signs of a solitary midnight city.", "cn": "空空荡荡、水汽弥漫的寂静人行道水泥地砖，倒映着子夜都市闪烁不定的冰冷霓虹招牌。"},
                {"en": "Persevering in an unrequited romance requires equal parts delusion and heroic tenacity.", "cn": "在一场注定得不到任何回应的单向单恋泥潭中苦苦隐忍坚持，需要的既是自欺欺人的疯癫盲目，也是壮士断腕般的孤勇坚韧。"},
                {"en": "Should I give up, or should I just keep chasing pavements?", "cn": "我究竟该及时止损体面退场？还是该义无反顾继续在这条漫无边际的人行道上追逐你的脚步？"},
                {"en": "My heart says advance, but my exhausted intellect screams at me to turn around.", "cn": "我悸动的心跳在疯了般催促我继续冲锋陷阵，然而我疲惫不堪的大脑理智却在声嘶力竭咆哮命令我立刻回头！"},
                {"en": "Even if it leads nowhere, the act of striving proves that the capacity for devotion is intact.", "cn": "即便这场追逐最终注定通向两手空空的竹篮打水一场空，但奋不顾身冲锋的过程本身，便已铁证如山地向天地证明：你为爱赴汤蹈火的赤子之心依然完好无损！"},
                {"en": "I'll pack up my pride and walk toward the dawn; no pavement can hold my spirit captive.", "cn": "收拾好我仅存的傲骨尊严，大步流星迎着破晓黎明的方向迈进吧；这世间没有任何冰冷坚硬的水泥路面，能将我渴望自由的灵魂永远囚禁束缚！"},
                {"en": "Should I give up? No, I will redirect this boundless fire toward loving myself completely.", "cn": "我该认输屈服吗？不！老娘要将这团无边无际的炽热烈火彻底调转方向，全心全意倾注用来狠狠深爱真实的我自己！"}
            ]
        },
        {
            "title": "第 9 首 · Make You Feel My Love · 让你真切感受我的爱",
            "description": "鲍勃·迪伦民谣传世神作的顶级翻唱，狂风暴雨夜的唯一温柔庇护所。",
            "sentences": [
                {"en": "When the rain is blowing in your face and the whole world is on your case.", "cn": "每当刺骨冰冷的狂风暴雨无情抽打在你的脸颊之上，而整个世俗人间的所有指责与重压都在逼迫你步履维艰时。"},
                {"en": "I could offer you a warm embrace to make you feel my love.", "cn": "我随时都心甘情愿为你送上一个温暖宽广的深情拥抱，只为让你真切感受到我炽热滚烫的爱意。"},
                {"en": "When the evening shadows and the stars appear, and there is no one there to dry your tears.", "cn": "每当夜幕低垂、漫天繁星寂寥浮现天穹，而你身畔却空无一人能为你轻轻拭去眼角委屈的泪珠时。"},
                {"en": "I could hold you for a million years to make you feel my love.", "cn": "我甚至心甘情愿张开双臂将你紧紧拥抱整整上百万年，只为让你真真切切感受到我生生世世的深沉大爱。"},
                {"en": "I know you haven't made your mind up yet, but I would never do you wrong.", "cn": "我深知此时此刻你心头仍在彷徨犹豫、尚未最终拿定主意，但我向苍天赌咒起誓：我这一生一世绝不可能负你半分、伤你毫厘。"},
                {"en": "I've known it from the moment that we met; no doubt in my mind where you belong.", "cn": "早在我们人海初逢相遇的第一秒起我心底便早已笃定参透：在我的灵魂神殿深处，从来没有半点怀疑——你便是我天命所归的永恒归宿！"},
                {"en": "I'd go hungry, I'd go black and blue, I'd go crawling down the avenue.", "cn": "我愿为你忍饥挨饿饱尝风霜，我愿为你被打得遍体鳞伤皮开肉绽，我甚至甘愿为了你的安康，匍匐膝行爬过熙熙攘攘的长街大道！"},
                {"en": "No, there's nothing that I wouldn't do to make you feel my love.", "cn": "不，这天地万物之间，就绝没有任何一件能让你感受到我真挚爱意的事情是我不肯舍命去做的！"},
                {"en": "The storms are raging on the rolling sea and on the highway of regret.", "cn": "狂暴的飓风海啸正在波涛汹涌的滔天恶浪之上肆虐咆哮，也在充满悔恨叹息的人生长途公路上呼啸翻滚。"},
                {"en": "The winds of change are blowing wild and free; you ain't seen nothing like me yet.", "cn": "时代剧变的狂风正在这辽阔天地间狂野不羁、无拘无束地肆意吹拂；而这世间像我这般九死不悔、爱你入骨的孤勇之人，你此前漫长一生中还未曾真正领教过！"},
                {"en": "I could make you happy, make your dreams come true; nothing that I wouldn't do.", "cn": "我完全有能耐让你成为这世上最幸福快乐之人，我愿倾囊助你所有的锦绣夙愿一一成真；只要是为了你，我万死不辞。"},
                {"en": "Go to the ends of the Earth for you to make you feel my love.", "cn": "哪怕为你远赴天涯海角、踏碎万水千山也在所不惜，只为让你在滚烫泪水中，真真切切感受到我这份厚重如山的深情！"},
                {"en": "Bob Dylan's folk poetry interpreted through Adele's tender piano delivery achieved definitive timelessness.", "cn": "诺贝尔文学奖得主鲍勃·迪伦笔下那首原本深沉内敛的民谣传世诗篇，经由阿黛尔那双被上帝吻过的温柔钢琴指尖与天籁歌喉倾情诠释，臻至了跨越时空的永恒艺术极境！"},
                {"en": "True devotion asks for no transactional return; it stands as an unwavering beacon in the storm.", "cn": "人世间真正至纯至善的赤诚守候，从来不奢求任何势利的等价利益回报；它就如同一座巍然屹立在狂风恶浪深处的定海神针灯塔，风雨无阻长久为你彻夜长明！"},
                {"en": "To make you feel my love, I offer everything I am, without condition or regret.", "cn": "只为让你真切体味到我这颗赤子之心的全部滚烫；我毫无保留奉献出我生命的全部所有，不带任何苛刻附加前提，亦绝不心存半点悔意！"}
            ]
        },
        {
            "title": "第 10 首 · Hometown Glory · 故乡伦敦的荣光与市井温情",
            "description": "十六岁写给故乡伦敦的传世长歌，工人阶级街头、雨水泥泞与血脉乡愁。",
            "sentences": [
                {"en": "I've been walking in the same way as I did, in the same streets that I had paved for myself.", "cn": "我依然踏着昔日那副熟悉的坚定步伐漫步穿行，徜徉在那些我曾用青春汗水为自己亲手铺就的一条条坎坷老街小巷里。"},
                {"en": "All these days I've been waiting for someone to come and take me away.", "cn": "在那些迷茫孤寂的漫长岁月里，我曾日复一日痴痴企盼着能有某位白马骑士从天而降，将我从这泥泞平凡的市井凡尘中一把拯救带走。"},
                {"en": "Round my hometown, memories are fresh; round my hometown, ooh, the people I've met.", "cn": "漫步在我的故乡伦敦的大街小巷，一幕幕往事回忆依然新鲜如昨宛如初见；徘徊在我深爱的故土街角，噢，那些曾与我擦肩相逢的形形色色可爱面孔啊！"},
                {"en": "Are the wonders of an everyday day, 'round my hometown.", "cn": "他们正是这平淡无奇的柴米油盐平凡市井日子里，最令人心潮澎湃的人间奇迹瑰宝，就在我扎根生长的故乡热土！"},
                {"en": "I like it in the city when the air is so thick and opaque; I love to see everybody in short skirts, shorts and shades.", "cn": "我由衷喜欢这座雾都大都市里空气弥漫着浓郁厚重工业烟尘水汽的独特质感；我狂热痴迷于在大街上看着男男女女换上清凉短裙、休闲短裤与墨镜畅快大笑。"},
                {"en": "I like it in the city when two worlds collide, people talking and bragging on the top deck of the bus.", "cn": "我独爱这座大都市里两种截然不同的阶层人生轨迹激烈交汇对撞的奇妙火花；红双层巴士二层长椅上互不相识的陌生人们推心置腹、高谈阔论大吹法螺。"},
                {"en": "Shows that we ain't gonna take no shit; shows that we are united by our common struggle.", "cn": "这鲜活有力地向全世界宣告证明：我们平民百姓绝不是任人宰割践踏的软柿子孬种！这生动昭示着：共同的奋斗求生磨难，已将我们万众一心紧紧团结在了一处！"},
                {"en": "The passionate, swelling descending piano motif was composed when Adele was merely sixteen.", "cn": "那段充满狂放激情、如瀑布般层层下行倾泻的经典华彩钢琴引子主题动机，竟然是阿黛尔早在年仅十六岁花季少女时期凭空创作写下的惊世神笔！"},
                {"en": "An anthem of fierce, working-class regional loyalty that resists the sterile homogenization of gentrification.", "cn": "这是一曲为底层工人阶级故土尊严深情唱响的狂傲战歌，以昂扬姿态誓死抵御着资本中产阶级化对老街区烟火气那毫无生机的冰冷同质化侵蚀！"},
                {"en": "A hometown is not defined by architectural glamour, but by the resilient souls who populate its rain-swept alleys.", "cn": "一座故乡真正名垂青史的伟大内核，绝不在于高耸入云的宏伟地标摩天建筑；而在于那些日夜在阴雨连绵的泥泞湿漉巷尾里顶风冒雨、顽强挺直脊梁艰难度日的鲜活不屈灵魂！"},
                {"en": "Round my hometown, the spirit of community thrives amidst urban decay.", "cn": "在我生于斯长于斯的故乡街区，邻里守望相助的崇高平民精神，正在城市荒芜废墟的夹缝之中蓬勃顽强绽放！"},
                {"en": "I'll never leave this soil; its grit is permanently embedded in the cadence of my vocal delivery.", "cn": "我至死也绝不会真正背弃这片厚德沃土；它骨子里那股粗粝坚韧的市井硬骨头风骨，早已永久深深烙印融汇在了我放声高歌的每一道起伏顿挫音节深处！"},
                {"en": "Hear the roar of the underground trains beneath the pavement; London is the living heartbeat of my art.", "cn": "快静静倾听人行道地砖下方那呼啸穿梭轰鸣的地铁列车震颤长啸吧；整座雾都伦敦的脉搏跳动，便正是我毕生艺术灵感生生不息的活水源泉！"},
                {"en": "Round my hometown, memories are fresh; celebrate your origins, for they gave you your voice.", "cn": "漫步在我的故乡老街，泛黄的记忆依然璀璨鲜活如昨；由衷为你的平凡出身而大声欢呼庆祝吧，因为正是那片饱经风霜的故土，赐予了你足以震慑人心的雄浑歌喉！"},
                {"en": "Hometown glory; stand proud upon the asphalt that taught you how to survive.", "cn": "故土的永恒荣光！骄傲自豪地挺立在这片教会了你如何咬牙生存战斗的沥青马路之上吧，这里是我们一生至高无上的荣耀摇篮！"}
            ]
        }
    ]
    course_id = courses[3]["id"]
    course_title = courses[3]["title"]
    start_ch_idx = len(courses[3]["chapters"])
    for idx, raw_ch in enumerate(adele_extra_chapters):
        ch_idx = start_ch_idx + idx + 1
        ch_id = f"{course_id}-ch{ch_idx}"
        ch_title = raw_ch["title"]
        ch_desc = raw_ch.get("description", "")
        formatted_sents = []
        for s_idx, s in enumerate(raw_ch["sentences"]):
            s_id = f"{ch_id}-s{s_idx + 1}"
            checked = make_sentence(s["en"], s["cn"], course_title, ch_title)
            formatted_sents.append({
                "id": s_id,
                "english": checked["en"],
                "chinese": checked["cn"]
            })
        courses[3]["chapters"].append({
            "id": ch_id,
            "title": ch_title,
            "description": ch_desc,
            "sentences": formatted_sents
        })
    courses[3]["chapters"] = courses[3]["chapters"][:10]

    save_ts_file("music", "MUSIC_COURSES", courses)
    print(f"🎵 目前已成功构建 4 门完整课程，章节: {sum(len(c['chapters']) for c in courses)}")
    return courses

if __name__ == "__main__":
    build_music_all()
