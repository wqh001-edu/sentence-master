import type { CoursePackage } from '../../types';
import { generateCurriculumChapters, DAILY_CONVERSATION_SENTENCES } from './corpusBuilder';

const musicCorpus = [...DAILY_CONVERSATION_SENTENCES];

export const MUSIC_COURSES: CoursePackage[] = [
  {
    id: 'course-music-beatles',
    title: '披头士乐队 (The Beatles) · 摇滚黄金金曲精读 (10章全集)',
    category: 'music',
    categoryName: '音乐英语',
    coverGradient: 'from-amber-600 via-orange-700 to-red-800',
    icon: '🎸',
    description: '《Hey Jude》《Let It Be》《Yesterday》，简短却穿透岁月的英伦经典。',
    difficulty: '入门 A1',
    tags: ['披头士', 'HeyJude', '老歌经典', '优美旋律'],
    chapters: generateCurriculumChapters('bt', [
      { title: '第 1 曲 · 《Hey Jude》抚慰心灵的呐喊与副歌' },
      { title: '第 2 曲 · 《Let It Be》困难岁月的智慧释怀' },
      { title: '第 3 曲 · 《Yesterday》昨日烦恼与经典弦乐' },
      { title: '第 4 曲 · 《In My Life》深情回眸生命中的挚友' },
      { title: '第 5 曲 · 《Here Comes the Sun》冬去春来的暖阳' },
      { title: '第 6 曲 · 《Blackbird》黑鸟展翅飞向光明自由' },
      { title: '第 7 曲 · 《Something》乔治·哈里森经典情歌' },
      { title: '第 8 曲 · 《Come Together》反战摇滚节奏律动' },
      { title: '第 9 曲 · 《All You Need Is Love》爱是全人类解药' },
      { title: '第 10 曲 · 《The Long and Winding Road》漫长曲折之路' }
    ], musicCorpus)
  },
  {
    id: 'course-music-taylor',
    title: '泰勒·斯威夫特 (Taylor Swift) · 抒情乡村到流行金曲 (10章全集)',
    category: 'music',
    categoryName: '音乐英语',
    coverGradient: 'from-pink-500 via-rose-600 to-purple-800',
    icon: '🎤',
    description: '《Love Story》《Blank Space》《Cruel Summer》，生动押韵与巧妙隐喻。',
    difficulty: '初级 A2',
    tags: ['霉霉金曲', '浪漫押韵', '现代流行', '修辞隐喻'],
    chapters: generateCurriculumChapters('ts', [
      { title: '第 1 曲 · 《Love Story》阳台下的罗密欧告白' },
      { title: '第 2 曲 · 《You Belong With Me》看台上的青春暗恋' },
      { title: '第 3 曲 · 《Back to December》十二月寒冬里的真挚歉意' },
      { title: '第 4 曲 · 《Blank Space》名流八卦的反讽自嘲' },
      { title: '第 5 曲 · 《Shake It Off》甩掉流言蜚语的快乐摇摆' },
      { title: '第 6 曲 · 《All Too Well》红围巾与秋天落叶记忆' },
      { title: '第 7 曲 · 《Lover》二十秒心跳定格的浪漫誓言' },
      { title: '第 8 曲 · 《Cardigan》复古开襟衫与治愈回忆' },
      { title: '第 9 曲 · 《Anti-Hero》午夜茶会与自我审视' },
      { title: '第 10 曲 · 《Cruel Summer》炽热夏日心动的副歌' }
    ], musicCorpus)
  },
  {
    id: 'course-music-disney',
    title: '迪士尼经典音乐大碟 · 《Let It Go》与童年回响 (10章全集)',
    category: 'music',
    categoryName: '音乐英语',
    coverGradient: 'from-cyan-500 via-blue-600 to-indigo-800',
    icon: '❄️',
    description: '《冰雪奇缘》《狮子王》《阿拉丁》，朗朗上口、发音饱满清澈。',
    difficulty: '入门 A1',
    tags: ['迪士尼', 'LetItGo', '童年回忆', '音乐剧感'],
    chapters: generateCurriculumChapters('ds', [
      { title: '第 1 首 · 《Let It Go》冰雪女王建立冰之宫殿' },
      { title: '第 2 首 · 《A Whole New World》乘魔毯俯瞰人间' },
      { title: '第 3 首 · 《Can You Feel the Love Tonight》荣耀国度' },
      { title: '第 4 首 · 《Circle of Life》生生不息的非洲大草原' },
      { title: '第 5 首 · 《Beauty and the Beast》古老温情的童话' },
      { title: '第 6 首 · 《Part of Your World》小美人鱼向往陆地' },
      { title: '第 7 首 · 《How Far I\'ll Go》莫阿娜扬帆驶向大洋' },
      { title: '第 8 首 · 《Remember Me》寻梦环游记催泪亲情' },
      { title: '第 9 首 · 《You\'ve Got a Friend in Me》玩具总动员' },
      { title: '第 10 首 · 《When You Wish Upon a Star》向群星许愿' }
    ], musicCorpus)
  },
  {
    id: 'course-music-adele',
    title: '阿黛尔 (Adele) · 深情灵魂乐与动人短语 (10章全集)',
    category: 'music',
    categoryName: '音乐英语',
    coverGradient: 'from-amber-700 via-stone-800 to-black',
    icon: '🎹',
    description: '《Someone Like You》《Rolling in the Deep》，感人至深的过去时表达。',
    difficulty: '初级 A2',
    tags: ['阿黛尔', 'SomeoneLikeYou', '过去时抒情', '深情灵魂乐'],
    chapters: generateCurriculumChapters('ad', [
      { title: '第 1 曲 · 《Someone Like You》释怀与终生祝愿' },
      { title: '第 2 曲 · 《Rolling in the Deep》澎湃心碎鼓点' },
      { title: '第 3 曲 · 《Hello》穿过千百通电话的跨洋问候' },
      { title: '第 4 曲 · 《Make You Feel My Love》甘愿为你遮风挡雨' },
      { title: '第 5 曲 · 《Set Fire to the Rain》在雨中燃烧炽热火焰' },
      { title: '第 6 曲 · 《When We Were Young》致我们无悔的青春' },
      { title: '第 7 曲 · 《Easy On Me》给初入人生的自己一点宽容' },
      { title: '第 8 曲 · 《Chasing Pavements》追逐徒劳无功的盲从' },
      { title: '第 9 曲 · 《Skyfall》007 电影主题曲天幕坠落' },
      { title: '第 10 曲 · 《All I Ask》若这是最后一晚请深情拥抱' }
    ], musicCorpus)
  },
  {
    id: 'course-music-ed-sheeran',
    title: '黄老板 (Ed Sheeran) · 温暖民谣吉他弹唱句 (10章全集)',
    category: 'music',
    categoryName: '音乐英语',
    coverGradient: 'from-orange-500 via-amber-600 to-stone-800',
    icon: '🧡',
    description: '《Shape of You》《Perfect》《Thinking Out Loud》，平实真挚的词汇搭配。',
    difficulty: '入门 A1',
    tags: ['黄老板', '温暖民谣', '吉他弹唱', '浪漫告白'],
    chapters: generateCurriculumChapters('ed', [
      { title: '第 1 篇 · 《Perfect》在黑暗中赤脚起舞的唯美' },
      { title: '第 2 篇 · 《Shape of You》咖啡馆心动的甜蜜旋律' },
      { title: '第 3 篇 · 《Thinking Out Loud》当我七十岁依然爱你' },
      { title: '第 4 篇 · 《Photograph》把记忆藏在一张褪色相片里' },
      { title: '第 5 篇 · 《Castle on the Hill》怀念故乡童年山丘' },
      { title: '第 6 篇 · 《Happier》看见你笑得更开心我便安心' },
      { title: '第 7 篇 · 《Bad Habits》午夜不良习惯的清醒自我审视' },
      { title: '第 8 篇 · 《Shivers》让你心头一阵战栗的炽热心跳' },
      { title: '第 9 篇 · 《The A Team》现实主义底层英伦叙事' },
      { title: '第 10 篇 · 《Eyes Closed》闭上双眼到处都是你的倒影' }
    ], musicCorpus)
  },
  {
    id: 'course-music-coldplay',
    title: '酷玩乐队 (Coldplay) · 唯美英伦星空诗意 (10章全集)',
    category: 'music',
    categoryName: '音乐英语',
    coverGradient: 'from-indigo-600 via-purple-700 to-pink-800',
    icon: '✨',
    description: '《Yellow》《Viva La Vida》《Fix You》，充满想象力与隐喻的歌词。',
    difficulty: '中级 B1',
    tags: ['酷玩乐队', 'Yellow', '唯美诗意', '英伦摇滚'],
    chapters: generateCurriculumChapters('cp', [
      { title: '第 1 篇 · 《Yellow》凝望星空它们都在为你闪耀' },
      { title: '第 2 篇 · 《Fix You》当你竭尽全力却一无所获' },
      { title: '第 3 篇 · 《Viva La Vida》曾经统治世界的王者叹息' },
      { title: '第 4 篇 · 《The Scientist》没有人说过相爱是容易的事' },
      { title: '第 5 篇 · 《Paradise》梦想着少女飞往的无忧乐园' },
      { title: '第 6 篇 · 《Clocks》时钟滴答与不确定未来的选择' },
      { title: '第 7 篇 · 《A Sky Full of Stars》你是一整片灿烂星空' },
      { title: '第 8 篇 · 《Magic》我相信你身上拥有永恒的魔法' },
      { title: '第 9 篇 · 《Something Just Like This》我不想要超能力' },
      { title: '第 10 篇 · 《Adventure of a Lifetime》开启一生冒险' }
    ], musicCorpus)
  },
  {
    id: 'course-music-queen',
    title: '皇后乐队 (Queen) · 摇滚歌剧与冠军之声 (10章全集)',
    category: 'music',
    categoryName: '音乐英语',
    coverGradient: 'from-amber-500 via-red-600 to-purple-900',
    icon: '👑',
    description: '《Bohemian Rhapsody》《We Are the Champions》，波澜壮阔的摇滚史诗。',
    difficulty: '中级 B1',
    tags: ['皇后乐队', '波西米亚狂想曲', '摇滚歌剧', '热血冠军'],
    chapters: generateCurriculumChapters('qn', [
      { title: '第 1 首 · 《We Are the Champions》不屈的冠军战歌' },
      { title: '第 2 首 · 《We Will Rock You》震撼人心的踏步节拍' },
      { title: '第 3 首 · 《Bohemian Rhapsody》歌剧摇滚无上史诗' },
      { title: '第 4 首 · 《Don\'t Stop Me Now》今晚不要拦住我' },
      { title: '第 5 首 · 《Somebody to Love》在孤独世间找寻真爱' },
      { title: '第 6 首 · 《Radio Ga Ga》献给收音机广播的怀旧歌' },
      { title: '第 7 首 · 《Under Pressure》大卫鲍伊合作高压之歌' },
      { title: '第 8 首 · 《Crazy Little Thing Called Love》复古摇摆' },
      { title: '第 9 首 · 《I Want to Break Free》挣脱世俗桎梏自由' },
      { title: '第 10 首 · 《The Show Must Go On》即使心碎好戏开场' }
    ], musicCorpus)
  },
  {
    id: 'course-music-jazz',
    title: '经典爵士与老歌 · 慢调时光中的语法韵律 (10章全集)',
    category: 'music',
    categoryName: '音乐英语',
    coverGradient: 'from-stone-800 via-amber-950 to-black',
    icon: '🎷',
    description: '《Fly Me to the Moon》《Autumn Leaves》，醇厚爵士女伶嗓音，精细咬字。',
    difficulty: '初级 A2',
    tags: ['爵士老歌', '带我飞向月球', '秋叶', '优雅咬字'],
    chapters: generateCurriculumChapters('jz', [
      { title: '第 1 曲 · 《Fly Me to the Moon》在木星与火星漫步' },
      { title: '第 2 曲 · 《Autumn Leaves》秋叶落满窗前的回忆' },
      { title: '第 3 曲 · 《What a Wonderful World》绿树红玫瑰的世界' },
      { title: '第 4 曲 · 《My Way》按照我自己的道路无悔走完' },
      { title: '第 5 曲 · 《Cheek to Cheek》与你贴面慢舞在天堂' },
      { title: '第 6 曲 · 《L-O-V-E》纳金高字母拼写的浪漫告白' },
      { title: '第 7 曲 · 《Cry Me a River》为我哭成一条忧伤的河流' },
      { title: '第 8 曲 · 《Summertime》爵士歌剧夏日惬意摇篮曲' },
      { title: '第 9 曲 · 《Moon River》月亮河畔穿过夜晚的流浪者' },
      { title: '第 10 曲 · 《La Vie en Rose》爵士萨克斯中的玫瑰人生' }
    ], musicCorpus)
  }
];
