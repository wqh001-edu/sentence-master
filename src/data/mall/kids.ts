import type { CoursePackage } from '../../types';
import { generateCurriculumChapters, DAILY_CONVERSATION_SENTENCES } from './corpusBuilder';

const kidsCorpus = [...DAILY_CONVERSATION_SENTENCES];

export const KIDS_COURSES: CoursePackage[] = [
  {
    id: 'course-kids-phonics',
    title: '少儿自然拼读 (Phonics) · 趣味动物短句启蒙 (10章全集)',
    category: 'kids',
    categoryName: '少儿英语',
    coverGradient: 'from-amber-400 via-orange-400 to-yellow-500',
    icon: '🦁',
    description: '见词能读，听音能写。可爱的动物主角带孩子们快乐掌握 26 个字母发音。',
    difficulty: '入门 A1',
    tags: ['自然拼读', '少儿启蒙', '动物王国', '发音启蒙'],
    chapters: generateCurriculumChapters('kp', [
      { title: '第 1 阶 · 字母 A-C：蚂蚁、大熊与可爱小猫' },
      { title: '第 2 阶 · 字母 D-F：小狗、大象与森林狐狸' },
      { title: '第 3 阶 · 字母 G-I：长颈鹿、小马与绿色蜥蜴' },
      { title: '第 4 阶 · 字母 J-L：果冻、袋鼠与跳跳小狮子' },
      { title: '第 5 阶 · 字母 M-O：淘气猴子、鸟巢与智慧猫头鹰' },
      { title: '第 6 阶 · 字母 P-R：粉红小猪、女王蜂与小兔子' },
      { title: '第 7 阶 · 字母 S-U：弯弯小蛇、小老虎与小雨伞' },
      { title: '第 8 阶 · 字母 V-X：小提琴、大鲸鱼与神秘小狐狸' },
      { title: '第 9 阶 · 字母 Y-Z：黄色游艇与奔跑的斑马' },
      { title: '第 10 阶 · 26 个字母自然拼读全景大串联' }
    ], kidsCorpus)
  },
  {
    id: 'course-kids-daily',
    title: '日常亲子对话 100 句 · 晨起到睡前温馨陪伴 (10章全集)',
    category: 'kids',
    categoryName: '少儿英语',
    coverGradient: 'from-pink-400 via-rose-400 to-amber-300',
    icon: '🧸',
    description: '刷牙洗脸、整理玩具、睡前故事、温馨晚安，家庭双语启蒙必备。',
    difficulty: '入门 A1',
    tags: ['亲子英语', '家庭对话', '睡前晚安', '习惯养成'],
    chapters: generateCurriculumChapters('kd', [
      { title: '第 1 篇 · 太阳公公升起来：清晨温柔唤醒与伸懒腰' },
      { title: '第 2 篇 · 洗漱时间：咕噜咕噜刷刷牙与洗洗脸' },
      { title: '第 3 篇 · 穿衣搭配：自己穿袜子系好小鞋带' },
      { title: '第 4 篇 · 营养早餐：大口喝牛奶与吃香甜鸡蛋饼' },
      { title: '第 5 篇 · 出门准备：背好小书包与爸爸妈妈挥手' },
      { title: '第 6 篇 · 放学回家：脱下小外套洗干净双手' },
      { title: '第 7 篇 · 亲子游戏：我们一起把积木收拾进玩具盒' },
      { title: '第 8 篇 · 晚餐分享：今天在幼儿园最开心的事' },
      { title: '第 9 篇 · 睡前沐浴：泡泡浴与小黄鸭水上漂' },
      { title: '第 10 篇 · 睡前故事：一个温暖晚安拥抱做个甜梦' }
    ], kidsCorpus)
  },
  {
    id: 'course-kids-fairytales',
    title: '经典安徒生童话短句 · 善良与勇敢的梦幻森林 (10章全集)',
    category: 'kids',
    categoryName: '少儿英语',
    coverGradient: 'from-purple-400 via-indigo-400 to-pink-300',
    icon: '🧚‍♀️',
    description: '《丑小鸭》《卖火柴的小女孩》《拇指姑娘》，纯净语言点亮童心。',
    difficulty: '入门 A1',
    tags: ['安徒生童话', '丑小鸭', '勇敢梦想', '绘本短句'],
    chapters: generateCurriculumChapters('kf', [
      { title: '第 1 篇 · 丑小鸭在池塘深处默默展翅飞向蓝天' },
      { title: '第 2 篇 · 只要是一枚天鹅蛋，出生在哪里并不重要' },
      { title: '第 3 篇 · 拇指姑娘在荷叶小船上的奇妙漂流记' },
      { title: '第 4 篇 · 燕子带来的花丛小王子金色王冠' },
      { title: '第 5 篇 · 豌豆公主与二十层鸭绒垫下的真诚' },
      { title: '第 6 篇 · 皇帝的新装：小男孩纯真无邪的说出真相' },
      { title: '第 7 篇 · 坚定的锡兵：单腿站立在壁炉火光里微笑' },
      { title: '第 8 篇 · 卖火柴的小女孩：火光中温柔慈爱的外婆' },
      { title: '第 9 篇 · 夜莺的歌声让生病的国王重新焕发活力' },
      { title: '第 10 篇 · 善良与诚实是照亮黑夜最温暖的明灯' }
    ], kidsCorpus)
  },
  {
    id: 'course-kids-colors',
    title: '彩虹与大自然 · 颜色、形状与果蔬认知 (10章全集)',
    category: 'kids',
    categoryName: '少儿英语',
    coverGradient: 'from-lime-400 via-green-400 to-emerald-500',
    icon: '🌈',
    description: '红橙黄绿青蓝紫，认识身边五彩斑斓的四季与美味果蔬。',
    difficulty: '入门 A1',
    tags: ['颜色形状', '水果蔬菜', '大自然', '幼儿认知'],
    chapters: generateCurriculumChapters('kc', [
      { title: '第 1 课 · 红色：红彤彤的大苹果与香甜草莓' },
      { title: '第 2 课 · 黄色：弯弯的甜香蕉与向阳的小花' },
      { title: '第 3 课 · 蓝色：清澈的大海洋与晴朗的天空' },
      { title: '第 4 课 · 绿色：春天刚发芽的青草与高大绿树' },
      { title: '第 5 课 · 橙色：圆溜溜的橙子与万圣节大南瓜' },
      { title: '第 6 课 · 紫色：一串串晶莹剔透的水晶小葡萄' },
      { title: '第 7 课 · 形状认知：圆圆的皮球与三角形小帐篷' },
      { title: '第 8 课 · 正方形小礼盒与长方形的漂亮画册' },
      { title: '第 9 课 · 天空中的白云与漫天飘落的六角雪花' },
      { title: '第 10 课 · 雨过天晴：大自然送给大地的七彩虹' }
    ], kidsCorpus)
  },
  {
    id: 'course-kids-manners',
    title: '礼貌好宝宝 · 社交礼仪与友爱表达 (10章全集)',
    category: 'kids',
    categoryName: '少儿英语',
    coverGradient: 'from-teal-400 via-cyan-400 to-blue-400',
    icon: '🤝',
    description: '学会说 Please, Thank you, Excuse me, 懂得分享与关怀同伴。',
    difficulty: '入门 A1',
    tags: ['礼貌礼仪', '分享快乐', '好习惯', '文明用语'],
    chapters: generateCurriculumChapters('km', [
      { title: '第 1 课 · 魔法口诀：请 (Please) 的温暖力量' },
      { title: '第 2 课 · 感恩表达：由衷地说一声谢谢 (Thank you)' },
      { title: '第 3 课 · 借用物品：打扰一下我可以借用蜡笔吗' },
      { title: '第 4 课 · 不小心碰倒搭积木：主动说声对不起' },
      { title: '第 5 课 · 宽容谅解：笑着说没关系 (It\'s okay)' },
      { title: '第 6 课 · 懂得分享：好吃的饼干分给小伙伴一份' },
      { title: '第 7 课 · 耐心排队：在滑梯前一个接一个不推搡' },
      { title: '第 8 课 · 倾听别人：当别人说话时安静注视对方' },
      { title: '第 9 课 · 给予赞美：你的图画画得真漂亮 (Great job)' },
      { title: '第 10 课 · 友爱同伴：我们都是最棒的好朋友' }
    ], kidsCorpus)
  },
  {
    id: 'course-kids-school',
    title: '快乐幼儿园与小学 · 课间游戏与老师指令 (10章全集)',
    category: 'kids',
    categoryName: '少儿英语',
    coverGradient: 'from-yellow-400 via-amber-400 to-orange-400',
    icon: '🏫',
    description: '排队上校车、举手提问、做眼保健操、操场捉迷藏常用短句。',
    difficulty: '入门 A1',
    tags: ['快乐校园', '课间游戏', '排队上车', '举手发言'],
    chapters: generateCurriculumChapters('ks', [
      { title: '第 1 课 · 上校车：安静系好黄色安全带' },
      { title: '第 2 课 · 走进教室：把小水壶整齐放在柜子里' },
      { title: '第 3 课 · 上课起立：向可亲的老师大声问早安' },
      { title: '第 4 课 · 举起小手：想发言前先举手再回答' },
      { title: '第 5 课 · 做手工剪纸：小剪刀注意安全握拿' },
      { title: '第 6 课 · 课间操：跟着欢快音乐拍拍手踢踢腿' },
      { title: '第 7 课 · 操场活动：草地上玩丢手绢与捉迷藏' },
      { title: '第 8 课 · 图书角阅读：轻轻翻开大画册保持安静' },
      { title: '第 9 课 · 午睡时间：盖好小毛毯闭上眼睛休息' },
      { title: '第 10 课 · 放学铃响：整理好桌面和同桌明天见' }
    ], kidsCorpus)
  },
  {
    id: 'course-kids-science',
    title: '小小科学家探索 · 太阳系与神奇地球 (10章全集)',
    category: 'kids',
    categoryName: '少儿英语',
    coverGradient: 'from-indigo-400 via-blue-500 to-purple-600',
    icon: '🚀',
    description: '为什么会下雨？恐龙为什么灭绝？激发孩子对浩瀚宇宙的好奇心。',
    difficulty: '初级 A2',
    tags: ['少儿科普', '恐龙世界', '浩瀚太空', '为什么探秘'],
    chapters: generateCurriculumChapters('ksc', [
      { title: '第 1 课 · 太阳系家族：八颗大行星的奇妙轨道' },
      { title: '第 2 课 · 地球母亲：蓝色的海洋与绿色的陆地' },
      { title: '第 3 课 · 月亮变化：从弯弯月牙到圆圆大银盘' },
      { title: '第 4 课 · 水的循环：小水滴蒸发变成天上的白云' },
      { title: '第 5 课 · 四季变换：春夏秋冬为什么会轮流到来' },
      { title: '第 6 课 · 植物的秘密：小种子喝水晒太阳生根发芽' },
      { title: '第 7 课 · 恐龙时代：霸王龙与三角龙的远古王国' },
      { title: '第 8 课 · 深海世界：发光小鱼与庞大的蓝鲸' },
      { title: '第 9 课 · 太空漫步：宇航员在空间站如何喝水' },
      { title: '第 10 课 · 保护环境：少用塑料袋爱护绿色家园' }
    ], kidsCorpus)
  },
  {
    id: 'course-kids-songs',
    title: '英文儿歌金曲 · 《Twinkle Twinkle》欢快哼唱 (10章全集)',
    category: 'kids',
    categoryName: '少儿英语',
    coverGradient: 'from-pink-300 via-purple-300 to-indigo-400',
    icon: '⭐',
    description: '小星星、两只老虎、老麦克唐纳有农场，边唱边学拼写。',
    difficulty: '入门 A1',
    tags: ['英文儿歌', '一闪一闪小星星', '欢快律动', '歌词拼写'],
    chapters: generateCurriculumChapters('kso', [
      { title: '第 1 首 · 《Twinkle, Twinkle, Little Star》闪耀小星星' },
      { title: '第 2 首 · 《Old MacDonald Had a Farm》老麦农场咯咯叫' },
      { title: '第 3 首 · 《The Wheels on the Bus》大巴车轮转呀转' },
      { title: '第 4 首 · 《If You\'re Happy and You Know It》拍拍小手' },
      { title: '第 5 首 · 《Head, Shoulders, Knees and Toes》身体部位歌' },
      { title: '第 6 首 · 《Row, Row, Row Your Boat》划小船悠然自得' },
      { title: '第 7 首 · 《Baa, Baa, Black Sheep》小黑羊咩咩叫' },
      { title: '第 8 首 · 《Hickory Dickory Dock》小老鼠上时钟' },
      { title: '第 9 首 · 《Rain, Rain, Go Away》小雨快快停下来' },
      { title: '第 10 首 · 《Alphabet Song》26 个字母欢乐大合唱' }
    ], kidsCorpus)
  }
];
