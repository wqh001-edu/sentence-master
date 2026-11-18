/* eslint-disable */
// 自动生成的大容量英汉词典数据与词形还原数据库 (含精准音标、词性、中文释义与中文详解)
export interface DictItem {
  pos: string;
  meaning: string;
  phonetic?: string;
  explanation?: string;
  example?: string;
  exampleCn?: string;
  family?: string[];
  synonyms?: string[];
  antonyms?: string[];
  collocations?: { phrase: string; meaning: string }[];
}

// 不规则动词形态映射表 (word -> [base_verb, pos_desc, cn_meaning, phonetic])
export const IRREGULAR_VERBS: Record<string, [string, string, string, string]> = {
  "am": [
    "be",
    "动词(第一人称单数)",
    "是",
    "/æm/"
  ],
  "is": [
    "be",
    "动词(第三人称单数)",
    "是",
    "/ɪz/"
  ],
  "are": [
    "be",
    "动词(复数/第二人称)",
    "是",
    "/ɑːr/"
  ],
  "was": [
    "be",
    "动词(过去式单数)",
    "曾是；在",
    "/wʌz/"
  ],
  "were": [
    "be",
    "动词(过去式复数)",
    "曾是；在",
    "/wɜːr/"
  ],
  "been": [
    "be",
    "动词(过去分词)",
    "构成完成时；曾是",
    "/bɪn/"
  ],
  "being": [
    "be",
    "动词(现在分词)",
    "正在是；存在",
    "/ˈbiːɪŋ/"
  ],
  "has": [
    "have",
    "动词(第三人称单数)",
    "有；拥有",
    "/hæz/"
  ],
  "had": [
    "have",
    "动词(过去式/分词)",
    "曾有；已拥有",
    "/hæd/"
  ],
  "having": [
    "have",
    "动词(现在分词)",
    "正在拥有；正在进行",
    "/ˈhævɪŋ/"
  ],
  "does": [
    "do",
    "动词(第三人称单数)",
    "做；助动词",
    "/dʌz/"
  ],
  "did": [
    "do",
    "动词(过去式)",
    "做了；曾做",
    "/dɪd/"
  ],
  "done": [
    "do",
    "动词(过去分词)",
    "已做完；已完成",
    "/dʌn/"
  ],
  "went": [
    "go",
    "动词(过去式)",
    "去了；离去",
    "/wɛnt/"
  ],
  "gone": [
    "go",
    "动词(过去分词)",
    "已去；已走",
    "/ɡɒn/"
  ],
  "saw": [
    "see",
    "动词(过去式)",
    "看见了；明白了",
    "/sɔː/"
  ],
  "seen": [
    "see",
    "动词(过去分词)",
    "已看见；已目睹",
    "/siːn/"
  ],
  "came": [
    "come",
    "动词(过去式)",
    "来了；来到",
    "/keɪm/"
  ],
  "took": [
    "take",
    "动词(过去式)",
    "拿了；花费了",
    "/tʊk/"
  ],
  "taken": [
    "take",
    "动词(过去分词)",
    "被带走；已花费",
    "/ˈteɪkən/"
  ],
  "made": [
    "make",
    "动词(过去式/分词)",
    "制造了；促使",
    "/meɪd/"
  ],
  "got": [
    "get",
    "动词(过去式/分词)",
    "得到了；变得",
    "/ɡɒt/"
  ],
  "gotten": [
    "get",
    "动词(过去分词)",
    "已获得",
    "/ˈɡɒtən/"
  ],
  "gave": [
    "give",
    "动词(过去式)",
    "给了；赋予",
    "/ɡeɪv/"
  ],
  "given": [
    "give",
    "动词(过去分词)",
    "被给予；考虑到",
    "/ˈɡɪvən/"
  ],
  "knew": [
    "know",
    "动词(过去式)",
    "知道；了解",
    "/njuː/"
  ],
  "known": [
    "know",
    "动词(过去分词)",
    "已知的；熟知的",
    "/noʊn/"
  ],
  "thought": [
    "think",
    "动词(过去式/分词)",
    "思考了；曾认为",
    "/θɔːt/"
  ],
  "felt": [
    "feel",
    "动词(过去式/分词)",
    "感觉到了；觉得",
    "/fɛlt/"
  ],
  "found": [
    "find",
    "动词(过去式/分词)",
    "找到了；发觉",
    "/faʊnd/"
  ],
  "left": [
    "leave",
    "动词(过去式/分词)",
    "离开了；留下",
    "/lɛft/"
  ],
  "told": [
    "tell",
    "动词(过去式/分词)",
    "告诉了；讲述",
    "/toʊld/"
  ],
  "became": [
    "become",
    "动词(过去式)",
    "成为了；变成",
    "/bɪˈkeɪm/"
  ],
  "brought": [
    "bring",
    "动词(过去式/分词)",
    "带来了；引起",
    "/brɔːt/"
  ],
  "bought": [
    "buy",
    "动词(过去式/分词)",
    "购买了；买了",
    "/bɔːt/"
  ],
  "caught": [
    "catch",
    "动词(过去式/分词)",
    "抓住了；赶上",
    "/kɔːt/"
  ],
  "taught": [
    "teach",
    "动词(过去式/分词)",
    "教导了；传授",
    "/tɔːt/"
  ],
  "heard": [
    "hear",
    "动词(过去式/分词)",
    "听到了；听说",
    "/hɜːrd/"
  ],
  "ran": [
    "run",
    "动词(过去式)",
    "奔跑了；运转",
    "/ræn/"
  ],
  "stood": [
    "stand",
    "动词(过去式/分词)",
    "站立了；坚持",
    "/stʊd/"
  ],
  "understood": [
    "understand",
    "动词(过去式/分词)",
    "理解了；明白了",
    "/ˌʌndərˈstʊd/"
  ],
  "lost": [
    "lose",
    "动词(过去式/分词)",
    "丢失了；迷失",
    "/lɒst/"
  ],
  "paid": [
    "pay",
    "动词(过去式/分词)",
    "支付了；付出代价",
    "/peɪd/"
  ],
  "met": [
    "meet",
    "动词(过去式/分词)",
    "遇见了；会面",
    "/mɛt/"
  ],
  "sat": [
    "sit",
    "动词(过去式/分词)",
    "坐下了",
    "/sæt/"
  ],
  "spoke": [
    "speak",
    "动词(过去式)",
    "说了；发表讲话",
    "/spoʊk/"
  ],
  "spoken": [
    "speak",
    "动词(过去分词)",
    "口头的；已说",
    "/ˈspoʊkən/"
  ],
  "wrote": [
    "write",
    "动词(过去式)",
    "写了；著述",
    "/roʊt/"
  ],
  "written": [
    "write",
    "动词(过去分词)",
    "书面的；已写成",
    "/ˈrɪtən/"
  ],
  "grew": [
    "grow",
    "动词(过去式)",
    "成长了；种植",
    "/ɡruː/"
  ],
  "grown": [
    "grow",
    "动词(过去分词)",
    "已长大；已成熟",
    "/ɡroʊn/"
  ],
  "flew": [
    "fly",
    "动词(过去式)",
    "飞翔了；飞逝",
    "/fluː/"
  ],
  "flown": [
    "fly",
    "动词(过去分词)",
    "已飞走",
    "/floʊn/"
  ],
  "broke": [
    "break",
    "动词(过去式)",
    "打破了；破碎",
    "/broʊk/"
  ],
  "broken": [
    "break",
    "动词(过去分词/形容词)",
    "破碎的；损坏的",
    "/ˈbroʊkən/"
  ],
  "wore": [
    "wear",
    "动词(过去式)",
    "穿着；佩戴",
    "/wɔːr/"
  ],
  "worn": [
    "wear",
    "动词(过去分词/形容词)",
    "磨损的；破旧的",
    "/wɔːrn/"
  ],
  "chose": [
    "choose",
    "动词(过去式)",
    "选择了；选定",
    "/tʃoʊz/"
  ],
  "chosen": [
    "choose",
    "动词(过去分词)",
    "被选中的",
    "/ˈtʃoʊzən/"
  ],
  "fell": [
    "fall",
    "动词(过去式)",
    "跌落了；降临",
    "/fɛl/"
  ],
  "fallen": [
    "fall",
    "动词(过去分词/形容词)",
    "倒下的；飘落的",
    "/ˈfɔːlən/"
  ],
  "drove": [
    "drive",
    "动词(过去式)",
    "驾驶了；驱使",
    "/droʊv/"
  ],
  "driven": [
    "drive",
    "动词(过去分词)",
    "受驱动的",
    "/ˈdrɪvən/"
  ],
  "slept": [
    "sleep",
    "动词(过去式/分词)",
    "睡着了；睡眠",
    "/slɛpt/"
  ],
  "spent": [
    "spend",
    "动词(过去式/分词)",
    "花费了；度过",
    "/spɛnt/"
  ],
  "built": [
    "build",
    "动词(过去式/分词)",
    "建造了；确立",
    "/bɪlt/"
  ],
  "held": [
    "hold",
    "动词(过去式/分词)",
    "握住了；举行",
    "/hɛld/"
  ],
  "sent": [
    "send",
    "动词(过去式/分词)",
    "寄出了；派遣",
    "/sɛnt/"
  ],
  "kept": [
    "keep",
    "动词(过去式/分词)",
    "保持了；遵守",
    "/kɛpt/"
  ],
  "won": [
    "win",
    "动词(过去式/分词)",
    "赢得了；获胜",
    "/wʌn/"
  ],
  "began": [
    "begin",
    "动词(过去式)",
    "开始了；着手",
    "/bɪˈɡæn/"
  ],
  "begun": [
    "begin",
    "动词(过去分词)",
    "已开始",
    "/bɪˈɡʌn/"
  ],
  "drank": [
    "drink",
    "动词(过去式)",
    "喝了；饮酒",
    "/dræŋk/"
  ],
  "drunk": [
    "drink",
    "动词(过去分词/形容词)",
    "喝醉的",
    "/drʌŋk/"
  ],
  "ate": [
    "eat",
    "动词(过去式)",
    "吃了；进餐",
    "/eɪt/"
  ],
  "eaten": [
    "eat",
    "动词(过去分词)",
    "已吃",
    "/ˈiːtən/"
  ],
  "drew": [
    "draw",
    "动词(过去式)",
    "画了；拖拉",
    "/druː/"
  ],
  "drawn": [
    "draw",
    "动词(过去分词)",
    "被吸引；已绘制",
    "/drɔːn/"
  ],
  "swam": [
    "swim",
    "动词(过去式)",
    "游泳了",
    "/swæm/"
  ],
  "swum": [
    "swim",
    "动词(过去分词)",
    "游过",
    "/swʌm/"
  ],
  "sang": [
    "sing",
    "动词(过去式)",
    "歌唱了",
    "/sæŋ/"
  ],
  "sung": [
    "sing",
    "动词(过去分词)",
    "被咏唱的",
    "/sʌŋ/"
  ],
  "threw": [
    "throw",
    "动词(过去式)",
    "投掷了；抛弃",
    "/θruː/"
  ],
  "thrown": [
    "throw",
    "动词(过去分词)",
    "被扔下",
    "/θroʊn/"
  ],
  "shook": [
    "shake",
    "动词(过去式)",
    "摇动了；颤抖",
    "/ʃʊk/"
  ],
  "shaken": [
    "shake",
    "动词(过去分词)",
    "震惊的；受动摇的",
    "/ˈʃeɪkən/"
  ],
  "forgot": [
    "forget",
    "动词(过去式)",
    "遗忘了",
    "/fərˈɡɒt/"
  ],
  "forgotten": [
    "forget",
    "动词(过去分词)",
    "被遗忘的",
    "/fərˈɡɒtən/"
  ]
};

// 不规则名词复数映射表 (word -> [base_noun, pos_desc, cn_meaning, phonetic])
export const IRREGULAR_PLURALS: Record<string, [string, string, string, string]> = {
  "children": [
    "child",
    "名词(复数)",
    "孩子们",
    "/ˈtʃɪldrən/"
  ],
  "men": [
    "man",
    "名词(复数)",
    "男人们；人类",
    "/mɛn/"
  ],
  "women": [
    "woman",
    "名词(复数)",
    "女人们；妇女",
    "/ˈwɪmɪn/"
  ],
  "people": [
    "person",
    "名词(集合)",
    "人们；人民",
    "/ˈpiːpl/"
  ],
  "feet": [
    "foot",
    "名词(复数)",
    "双脚；英尺",
    "/fiːt/"
  ],
  "teeth": [
    "tooth",
    "名词(复数)",
    "牙齿(复数)",
    "/tiːθ/"
  ],
  "mice": [
    "mouse",
    "名词(复数)",
    "老鼠(复数)",
    "/maɪs/"
  ],
  "geese": [
    "goose",
    "名词(复数)",
    "大雁；鹅(复数)",
    "/ɡiːs/"
  ],
  "oxen": [
    "ox",
    "名词(复数)",
    "公牛(复数)",
    "/ˈɒksən/"
  ],
  "phenomena": [
    "phenomenon",
    "名词(复数)",
    "现象(复数)",
    "/fəˈnɒmɪnə/"
  ],
  "criteria": [
    "criterion",
    "名词(复数)",
    "标准；准则(复数)",
    "/kraɪˈtɪəriə/"
  ],
  "analyses": [
    "analysis",
    "名词(复数)",
    "分析；解析(复数)",
    "/əˈnæləsiːz/"
  ],
  "hypotheses": [
    "hypothesis",
    "名词(复数)",
    "假说；假设(复数)",
    "/haɪˈpɒθəsiːz/"
  ],
  "theses": [
    "thesis",
    "名词(复数)",
    "论文；论点(复数)",
    "/ˈθiːsiːz/"
  ],
  "crises": [
    "crisis",
    "名词(复数)",
    "危机(复数)",
    "/ˈkraɪsiːz/"
  ],
  "bases": [
    "basis",
    "名词(复数)",
    "基础；根据(复数)",
    "/ˈbeɪsiːz/"
  ]
};

// 核心全中文大词典主体
export const CORE_FULL_DICTIONARY: Record<string, DictItem> = {
  "hey": {
    "pos": "感叹词",
    "meaning": "嘿；你好",
    "phonetic": "/heɪ/",
    "explanation": "常用于非正式场合打招呼或吸引注意力。",
    "example": "Hey, how have you been?",
    "exampleCn": "嘿，你最近怎么样？",
    "family": [
      "hey"
    ],
    "collocations": [
      {
        "phrase": "hey usage",
        "meaning": "嘿；你好的基础运用"
      }
    ]
  },
  "hello": {
    "pos": "感叹词",
    "meaning": "你好；喂",
    "phonetic": "/həˈloʊ/",
    "explanation": "最普遍通用的问候语。",
    "example": "Hello everyone, welcome!",
    "exampleCn": "大家好，欢迎光临！",
    "family": [
      "hello"
    ],
    "collocations": [
      {
        "phrase": "hello usage",
        "meaning": "你好；喂的基础运用"
      }
    ]
  },
  "hi": {
    "pos": "感叹词",
    "meaning": "嗨；你好",
    "phonetic": "/haɪ/",
    "explanation": "亲切熟络的打招呼用语。",
    "example": "Hi, nice to see you.",
    "exampleCn": "嗨，很高兴见到你。",
    "family": [
      "hi"
    ],
    "collocations": [
      {
        "phrase": "hi usage",
        "meaning": "嗨；你好的基础运用"
      }
    ]
  },
  "welcome": {
    "pos": "动词/形容词",
    "meaning": "欢迎；受欢迎的",
    "phonetic": "/ˈwɛlkəm/",
    "explanation": "表示欢迎或客气回应。",
    "example": "Welcome to our team.",
    "exampleCn": "欢迎来到我们的团队。",
    "family": [
      "welcome"
    ],
    "collocations": [
      {
        "phrase": "welcome usage",
        "meaning": "欢迎；受欢迎的的基础运用"
      }
    ]
  },
  "please": {
    "pos": "副词/动词",
    "meaning": "请；使高兴",
    "phonetic": "/pliːz/",
    "explanation": "表达礼貌客气的语气词。",
    "example": "Please have a seat.",
    "exampleCn": "请坐。",
    "family": [
      "please"
    ],
    "collocations": [
      {
        "phrase": "please usage",
        "meaning": "请；使高兴的基础运用"
      }
    ]
  },
  "thank": {
    "pos": "动词",
    "meaning": "感谢；道谢",
    "phonetic": "/θæŋk/",
    "explanation": "表达谢意的主要词汇。",
    "example": "Thank you for your kindness.",
    "exampleCn": "谢谢你的好意。",
    "family": [
      "thank"
    ],
    "collocations": [
      {
        "phrase": "thank usage",
        "meaning": "感谢；道谢的基础运用"
      }
    ]
  },
  "thanks": {
    "pos": "名词/感叹词",
    "meaning": "感谢；多谢",
    "phonetic": "/θæŋks/",
    "explanation": "口语常用致谢表达。",
    "example": "Thanks for your great help.",
    "exampleCn": "多谢你的大力相助。",
    "family": [
      "thanks"
    ],
    "collocations": [
      {
        "phrase": "thanks usage",
        "meaning": "感谢；多谢的基础运用"
      }
    ]
  },
  "sorry": {
    "pos": "形容词",
    "meaning": "抱歉的；遗憾的",
    "phonetic": "/ˈsɒri/",
    "explanation": "表达道歉或遗憾。",
    "example": "I am sorry for the delay.",
    "exampleCn": "对不起耽误了。",
    "family": [
      "sorry"
    ],
    "collocations": [
      {
        "phrase": "sorry usage",
        "meaning": "抱歉的；遗憾的的基础运用"
      }
    ]
  },
  "excuse": {
    "pos": "动词/名词",
    "meaning": "原谅；借口",
    "phonetic": "/ɪkˈskjuːz/",
    "explanation": "excuse me 用于礼貌借光或搭话。",
    "example": "Excuse me, may I ask a question?",
    "exampleCn": "打扰一下，我可以问个问题吗？",
    "family": [
      "excuse"
    ],
    "collocations": [
      {
        "phrase": "excuse usage",
        "meaning": "原谅；借口的基础运用"
      }
    ]
  },
  "bye": {
    "pos": "感叹词",
    "meaning": "再见",
    "phonetic": "/baɪ/",
    "explanation": "日常道别语。",
    "example": "Bye, see you tomorrow!",
    "exampleCn": "再见，明天见！",
    "family": [
      "bye"
    ],
    "collocations": [
      {
        "phrase": "bye usage",
        "meaning": "再见的基础运用"
      }
    ]
  },
  "goodbye": {
    "pos": "感叹词/名词",
    "meaning": "再见；告别",
    "phonetic": "/ˌɡʊdˈbaɪ/",
    "explanation": "正式或日常道别表达。",
    "example": "They said goodbye warmly.",
    "exampleCn": "他们热情地道别。",
    "family": [
      "goodbye"
    ],
    "collocations": [
      {
        "phrase": "goodbye usage",
        "meaning": "再见；告别的基础运用"
      }
    ]
  },
  "yes": {
    "pos": "副词/感叹词",
    "meaning": "是的；对",
    "phonetic": "/jɛs/",
    "explanation": "肯定答复。",
    "example": "Yes, that sounds great.",
    "exampleCn": "是的，听起来很棒。",
    "family": [
      "yes"
    ],
    "collocations": [
      {
        "phrase": "yes usage",
        "meaning": "是的；对的基础运用"
      }
    ]
  },
  "no": {
    "pos": "限定词/副词",
    "meaning": "没有；不",
    "phonetic": "/noʊ/",
    "explanation": "否定回答或限定修饰。",
    "example": "There is no rush.",
    "exampleCn": "不用着急。",
    "family": [
      "no"
    ],
    "collocations": [
      {
        "phrase": "no usage",
        "meaning": "没有；不的基础运用"
      }
    ]
  },
  "oh": {
    "pos": "感叹词",
    "meaning": "哦；呀",
    "phonetic": "/oʊ/",
    "explanation": "表示惊讶、领悟或情绪变化。",
    "example": "Oh, I completely understand.",
    "exampleCn": "哦，我完全明白了。",
    "family": [
      "oh"
    ],
    "collocations": [
      {
        "phrase": "oh usage",
        "meaning": "哦；呀的基础运用"
      }
    ]
  },
  "wow": {
    "pos": "感叹词",
    "meaning": "哇；呀",
    "phonetic": "/waʊ/",
    "explanation": "惊叹赞赏语气词。",
    "example": "Wow, that is amazing!",
    "exampleCn": "哇，太神了！",
    "family": [
      "wow"
    ],
    "collocations": [
      {
        "phrase": "wow usage",
        "meaning": "哇；呀的基础运用"
      }
    ]
  },
  "i": {
    "pos": "代词",
    "meaning": "我 (第一人称主格)",
    "phonetic": "/aɪ/",
    "explanation": "说话者自称。",
    "example": "I love English spelling.",
    "exampleCn": "我热爱英语拼写。",
    "family": [
      "i"
    ],
    "collocations": [
      {
        "phrase": "i usage",
        "meaning": "我 (第一人称主格)的基础运用"
      }
    ]
  },
  "you": {
    "pos": "代词",
    "meaning": "你；你们",
    "phonetic": "/juː/",
    "explanation": "第二人称代词，单复同形。",
    "example": "You did a fantastic job.",
    "exampleCn": "你做得非常棒。",
    "family": [
      "you"
    ],
    "collocations": [
      {
        "phrase": "you usage",
        "meaning": "你；你们的基础运用"
      }
    ]
  },
  "he": {
    "pos": "代词",
    "meaning": "他 (主格)",
    "phonetic": "/hiː/",
    "explanation": "第三人称阳性主格。",
    "example": "He arrived right on time.",
    "exampleCn": "他准时到达了。",
    "family": [
      "he"
    ],
    "collocations": [
      {
        "phrase": "he usage",
        "meaning": "他 (主格)的基础运用"
      }
    ]
  },
  "she": {
    "pos": "代词",
    "meaning": "她 (主格)",
    "phonetic": "/ʃiː/",
    "explanation": "第三人称阴性主格。",
    "example": "She speaks English fluently.",
    "exampleCn": "她英语说得很流利。",
    "family": [
      "she"
    ],
    "collocations": [
      {
        "phrase": "she usage",
        "meaning": "她 (主格)的基础运用"
      }
    ]
  },
  "it": {
    "pos": "代词",
    "meaning": "它；这",
    "phonetic": "/ɪt/",
    "explanation": "指代事物、动物或天气。",
    "example": "It is a sunny morning.",
    "exampleCn": "这是一个晴朗的早晨。",
    "family": [
      "it"
    ],
    "collocations": [
      {
        "phrase": "it usage",
        "meaning": "它；这的基础运用"
      }
    ]
  },
  "we": {
    "pos": "代词",
    "meaning": "我们 (主格)",
    "phonetic": "/wiː/",
    "explanation": "第一人称复数主格。",
    "example": "We practice together every day.",
    "exampleCn": "我们每天一起练习。",
    "family": [
      "we"
    ],
    "collocations": [
      {
        "phrase": "we usage",
        "meaning": "我们 (主格)的基础运用"
      }
    ]
  },
  "they": {
    "pos": "代词",
    "meaning": "他们；她们；它们",
    "phonetic": "/ðeɪ/",
    "explanation": "第三人称复数主格。",
    "example": "They achieved their goal.",
    "exampleCn": "他们达成了目标。",
    "family": [
      "they"
    ],
    "collocations": [
      {
        "phrase": "they usage",
        "meaning": "他们；她们；它们的基础运用"
      }
    ]
  },
  "me": {
    "pos": "代词",
    "meaning": "我 (宾格)",
    "phonetic": "/miː/",
    "explanation": "第一人称单数宾格。",
    "example": "Give me a chance to try.",
    "exampleCn": "给我一个尝试的机会。",
    "family": [
      "me"
    ],
    "collocations": [
      {
        "phrase": "me usage",
        "meaning": "我 (宾格)的基础运用"
      }
    ]
  },
  "him": {
    "pos": "代词",
    "meaning": "他 (宾格)",
    "phonetic": "/hɪm/",
    "explanation": "第三人称阳性宾格。",
    "example": "I saw him at the library.",
    "exampleCn": "我在图书馆见到了他。",
    "family": [
      "him"
    ],
    "collocations": [
      {
        "phrase": "him usage",
        "meaning": "他 (宾格)的基础运用"
      }
    ]
  },
  "her": {
    "pos": "代词/形容词",
    "meaning": "她 (宾格)；她的",
    "phonetic": "/hɜːr/",
    "explanation": "第三人称阴性宾格或物主代词。",
    "example": "Her performance was brilliant.",
    "exampleCn": "她的表现精彩绝伦。",
    "family": [
      "her"
    ],
    "collocations": [
      {
        "phrase": "her usage",
        "meaning": "她 (宾格)；她的的基础运用"
      }
    ]
  },
  "us": {
    "pos": "代词",
    "meaning": "我们 (宾格)",
    "phonetic": "/ʌs/",
    "explanation": "第一人称复数宾格。",
    "example": "Join us for lunch today.",
    "exampleCn": "今天和我们一起吃午饭吧。",
    "family": [
      "us"
    ],
    "collocations": [
      {
        "phrase": "us usage",
        "meaning": "我们 (宾格)的基础运用"
      }
    ]
  },
  "them": {
    "pos": "代词",
    "meaning": "他们/她们/它们 (宾格)",
    "phonetic": "/ðɛm/",
    "explanation": "第三人称复数宾格。",
    "example": "Tell them the good news.",
    "exampleCn": "把好消息告诉他们。",
    "family": [
      "them"
    ],
    "collocations": [
      {
        "phrase": "them usage",
        "meaning": "他们/她们/它们 (宾格)的基础运用"
      }
    ]
  },
  "my": {
    "pos": "限定词",
    "meaning": "我的",
    "phonetic": "/maɪ/",
    "explanation": "形容词性物主代词。",
    "example": "My favorite subject is English.",
    "exampleCn": "我最喜欢的学科是英语。",
    "family": [
      "my"
    ],
    "collocations": [
      {
        "phrase": "my usage",
        "meaning": "我的的基础运用"
      }
    ]
  },
  "your": {
    "pos": "限定词",
    "meaning": "你的；你们的",
    "phonetic": "/jɔːr/",
    "explanation": "形容词性物主代词。",
    "example": "Your pronunciation is very clear.",
    "exampleCn": "你的发音非常清晰。",
    "family": [
      "your"
    ],
    "collocations": [
      {
        "phrase": "your usage",
        "meaning": "你的；你们的的基础运用"
      }
    ]
  },
  "his": {
    "pos": "限定词/代词",
    "meaning": "他的",
    "phonetic": "/hɪz/",
    "explanation": "物主代词。",
    "example": "His enthusiasm inspires everyone.",
    "exampleCn": "他的热情鼓舞了所有人。",
    "family": [
      "his"
    ],
    "collocations": [
      {
        "phrase": "his usage",
        "meaning": "他的的基础运用"
      }
    ]
  },
  "its": {
    "pos": "限定词",
    "meaning": "它的",
    "phonetic": "/ɪts/",
    "explanation": "事物的物主限定词。",
    "example": "The cat licked its paws.",
    "exampleCn": "猫咪舔了舔自己的爪子。",
    "family": [
      "its"
    ],
    "collocations": [
      {
        "phrase": "its usage",
        "meaning": "它的的基础运用"
      }
    ]
  },
  "our": {
    "pos": "限定词",
    "meaning": "我们的",
    "phonetic": "/ˈaʊər/",
    "explanation": "第一人称复数物主代词。",
    "example": "Our progress is steady and solid.",
    "exampleCn": "我们的进步扎实而稳定。",
    "family": [
      "our"
    ],
    "collocations": [
      {
        "phrase": "our usage",
        "meaning": "我们的的基础运用"
      }
    ]
  },
  "their": {
    "pos": "限定词",
    "meaning": "他们的；她们的",
    "phonetic": "/ðɛər/",
    "explanation": "第三人称复数物主代词。",
    "example": "Their dedication paid off.",
    "exampleCn": "他们的奉献得到了回报。",
    "family": [
      "their"
    ],
    "collocations": [
      {
        "phrase": "their usage",
        "meaning": "他们的；她们的的基础运用"
      }
    ]
  },
  "this": {
    "pos": "代词/限定词",
    "meaning": "这；这个",
    "phonetic": "/ðɪs/",
    "explanation": "指示近处的人或物。",
    "example": "This is what I wanted.",
    "exampleCn": "这就是我想要的。",
    "family": [
      "this"
    ],
    "collocations": [
      {
        "phrase": "this usage",
        "meaning": "这；这个的基础运用"
      }
    ]
  },
  "that": {
    "pos": "代词/连词",
    "meaning": "那；那个；从句引导词",
    "phonetic": "/ðæt/",
    "explanation": "指示较远对象或引导宾语/定语从句。",
    "example": "I know that you can do it.",
    "exampleCn": "我知道你能行。",
    "family": [
      "that"
    ],
    "collocations": [
      {
        "phrase": "that usage",
        "meaning": "那；那个；从句引导词的基础运用"
      }
    ]
  },
  "these": {
    "pos": "代词/限定词",
    "meaning": "这些",
    "phonetic": "/ðiːz/",
    "explanation": "this 的复数。",
    "example": "These sentences are inspiring.",
    "exampleCn": "这些句子鼓舞人心。",
    "family": [
      "these"
    ],
    "collocations": [
      {
        "phrase": "these usage",
        "meaning": "这些的基础运用"
      }
    ]
  },
  "those": {
    "pos": "代词/限定词",
    "meaning": "那些",
    "phonetic": "/ðoʊz/",
    "explanation": "that 的复数。",
    "example": "Those flowers bloom beautifully.",
    "exampleCn": "那些花朵盛开得真美。",
    "family": [
      "those"
    ],
    "collocations": [
      {
        "phrase": "those usage",
        "meaning": "那些的基础运用"
      }
    ]
  },
  "what": {
    "pos": "疑问代词",
    "meaning": "什么；多么",
    "phonetic": "/wɒt/",
    "explanation": "询问事物内容。",
    "example": "What is your main goal?",
    "exampleCn": "你的主要目标是什么？",
    "family": [
      "what"
    ],
    "collocations": [
      {
        "phrase": "what usage",
        "meaning": "什么；多么的基础运用"
      }
    ]
  },
  "which": {
    "pos": "疑问代词",
    "meaning": "哪一个；哪一些",
    "phonetic": "/wɪtʃ/",
    "explanation": "范围选择疑问代词。",
    "example": "Which lesson should we start?",
    "exampleCn": "我们该从哪一课开始？",
    "family": [
      "which"
    ],
    "collocations": [
      {
        "phrase": "which usage",
        "meaning": "哪一个；哪一些的基础运用"
      }
    ]
  },
  "who": {
    "pos": "疑问代词",
    "meaning": "谁",
    "phonetic": "/huː/",
    "explanation": "询问人物身份。",
    "example": "Who is leading the discussion?",
    "exampleCn": "谁在主持这次讨论？",
    "family": [
      "who"
    ],
    "collocations": [
      {
        "phrase": "who usage",
        "meaning": "谁的基础运用"
      }
    ]
  },
  "whom": {
    "pos": "代词",
    "meaning": "谁 (宾格)",
    "phonetic": "/huːm/",
    "explanation": "正式宾格疑问代词。",
    "example": "With whom did you speak?",
    "exampleCn": "你在和谁通电话？",
    "family": [
      "whom"
    ],
    "collocations": [
      {
        "phrase": "whom usage",
        "meaning": "谁 (宾格)的基础运用"
      }
    ]
  },
  "whose": {
    "pos": "代词",
    "meaning": "谁的",
    "phonetic": "/huːz/",
    "explanation": "所有格疑问代词。",
    "example": "Whose idea was this?",
    "exampleCn": "这是谁的主意？",
    "family": [
      "whose"
    ],
    "collocations": [
      {
        "phrase": "whose usage",
        "meaning": "谁的的基础运用"
      }
    ]
  },
  "where": {
    "pos": "疑问副词",
    "meaning": "在哪里；何处",
    "phonetic": "/wɛər/",
    "explanation": "询问地点。",
    "example": "Where can I find the book?",
    "exampleCn": "我在哪里能找到这本书？",
    "family": [
      "where"
    ],
    "collocations": [
      {
        "phrase": "where usage",
        "meaning": "在哪里；何处的基础运用"
      }
    ]
  },
  "when": {
    "pos": "疑问副词/连词",
    "meaning": "何时；当...时",
    "phonetic": "/wɛn/",
    "explanation": "询问时间或引导时间状语。",
    "example": "When does the train leave?",
    "exampleCn": "火车什么时候发车？",
    "family": [
      "when"
    ],
    "collocations": [
      {
        "phrase": "when usage",
        "meaning": "何时；当...时的基础运用"
      }
    ]
  },
  "why": {
    "pos": "疑问副词",
    "meaning": "为什么；何以",
    "phonetic": "/waɪ/",
    "explanation": "询问原因理由。",
    "example": "Why do birds sing in spring?",
    "exampleCn": "为什么鸟儿在春天歌唱？",
    "family": [
      "why"
    ],
    "collocations": [
      {
        "phrase": "why usage",
        "meaning": "为什么；何以的基础运用"
      }
    ]
  },
  "how": {
    "pos": "疑问副词",
    "meaning": "如何；怎样；多么",
    "phonetic": "/haʊ/",
    "explanation": "询问方式、状态或程度。",
    "example": "How do you solve this puzzle?",
    "exampleCn": "你如何解开这个谜题？",
    "family": [
      "how"
    ],
    "collocations": [
      {
        "phrase": "how usage",
        "meaning": "如何；怎样；多么的基础运用"
      }
    ]
  },
  "be": {
    "pos": "动词",
    "meaning": "是；存在；成为",
    "phonetic": "/biː/",
    "explanation": "系动词或构成被动语态/进行时。",
    "example": "Be honest with yourself.",
    "exampleCn": "对自己真诚。",
    "family": [
      "be"
    ],
    "collocations": [
      {
        "phrase": "be usage",
        "meaning": "是；存在；成为的基础运用"
      }
    ]
  },
  "have": {
    "pos": "动词/助动词",
    "meaning": "有；拥有；构成完成时",
    "phonetic": "/hæv/",
    "explanation": "实义动词拥有或完成时助动词。",
    "example": "I have finished my homework.",
    "exampleCn": "我已经做完了功课。",
    "family": [
      "have"
    ],
    "collocations": [
      {
        "phrase": "have usage",
        "meaning": "有；拥有；构成完成时的基础运用"
      }
    ]
  },
  "do": {
    "pos": "动词/助动词",
    "meaning": "做；干；助动词",
    "phonetic": "/duː/",
    "explanation": "表示行动或构成否定/疑问句。",
    "example": "Do your best every single day.",
    "exampleCn": "每天都拼尽全力。",
    "family": [
      "do"
    ],
    "collocations": [
      {
        "phrase": "do usage",
        "meaning": "做；干；助动词的基础运用"
      }
    ]
  },
  "say": {
    "pos": "动词",
    "meaning": "说；讲；表明",
    "phonetic": "/seɪ/",
    "explanation": "言语表述。",
    "example": "Say what you mean politely.",
    "exampleCn": "礼貌地表达你的意思。",
    "family": [
      "say"
    ],
    "collocations": [
      {
        "phrase": "say usage",
        "meaning": "说；讲；表明的基础运用"
      }
    ]
  },
  "go": {
    "pos": "动词",
    "meaning": "去；走；运行",
    "phonetic": "/ɡoʊ/",
    "explanation": "位移动作或状态改变。",
    "example": "Let us go forward together.",
    "exampleCn": "让我们携手向前。",
    "family": [
      "go"
    ],
    "collocations": [
      {
        "phrase": "go usage",
        "meaning": "去；走；运行的基础运用"
      }
    ]
  },
  "get": {
    "pos": "动词",
    "meaning": "得到；变得；到达",
    "phonetic": "/ɡɛt/",
    "explanation": "获取、成为或到达某处。",
    "example": "Get ready for the new journey.",
    "exampleCn": "为新的旅程做好准备。",
    "family": [
      "get"
    ],
    "collocations": [
      {
        "phrase": "get usage",
        "meaning": "得到；变得；到达的基础运用"
      }
    ]
  },
  "make": {
    "pos": "动词",
    "meaning": "制作；使得；创造",
    "phonetic": "/meɪk/",
    "explanation": "制造或促使某种结果。",
    "example": "Make every moment count.",
    "exampleCn": "让每一刻都富有意义。",
    "family": [
      "make"
    ],
    "collocations": [
      {
        "phrase": "make usage",
        "meaning": "制作；使得；创造的基础运用"
      }
    ]
  },
  "know": {
    "pos": "动词",
    "meaning": "知道；认识；了解",
    "phonetic": "/noʊ/",
    "explanation": "掌握信息或认识某人。",
    "example": "I know the answer now.",
    "exampleCn": "我现在知道答案了。",
    "family": [
      "know"
    ],
    "collocations": [
      {
        "phrase": "know usage",
        "meaning": "知道；认识；了解的基础运用"
      }
    ]
  },
  "think": {
    "pos": "动词",
    "meaning": "想；认为；思考",
    "phonetic": "/θɪŋk/",
    "explanation": "思维认知活动。",
    "example": "Think carefully before acting.",
    "exampleCn": "行动前慎重思考。",
    "family": [
      "think"
    ],
    "collocations": [
      {
        "phrase": "think usage",
        "meaning": "想；认为；思考的基础运用"
      }
    ]
  },
  "take": {
    "pos": "动词",
    "meaning": "拿；花费；采取",
    "phonetic": "/teɪk/",
    "explanation": "获取、占用时间或采取措施。",
    "example": "Take your time to understand.",
    "exampleCn": "慢慢体会并理解。",
    "family": [
      "take"
    ],
    "collocations": [
      {
        "phrase": "take usage",
        "meaning": "拿；花费；采取的基础运用"
      }
    ]
  },
  "see": {
    "pos": "动词",
    "meaning": "看见；明白；领会",
    "phonetic": "/siː/",
    "explanation": "视觉感知或理智领悟。",
    "example": "I see the beautiful rainbow.",
    "exampleCn": "我看见了美丽的彩虹。",
    "family": [
      "see"
    ],
    "collocations": [
      {
        "phrase": "see usage",
        "meaning": "看见；明白；领会的基础运用"
      }
    ]
  },
  "come": {
    "pos": "动词",
    "meaning": "来；到来；达到",
    "phonetic": "/kʌm/",
    "explanation": "朝说话者移动。",
    "example": "Come and join our celebration.",
    "exampleCn": "来加入我们的庆祝吧。",
    "family": [
      "come"
    ],
    "collocations": [
      {
        "phrase": "come usage",
        "meaning": "来；到来；达到的基础运用"
      }
    ]
  },
  "want": {
    "pos": "动词",
    "meaning": "想要；需要",
    "phonetic": "/wɒnt/",
    "explanation": "表达心愿渴望。",
    "example": "I want to speak fluent English.",
    "exampleCn": "我想说一口流利的英语。",
    "family": [
      "want"
    ],
    "collocations": [
      {
        "phrase": "want usage",
        "meaning": "想要；需要的基础运用"
      }
    ]
  },
  "look": {
    "pos": "动词/名词",
    "meaning": "看；瞧；显得",
    "phonetic": "/lʊk/",
    "explanation": "视觉定向或外观神色。",
    "example": "Look at the stars tonight.",
    "exampleCn": "看今晚漫天的繁星。",
    "family": [
      "look"
    ],
    "collocations": [
      {
        "phrase": "look usage",
        "meaning": "看；瞧；显得的基础运用"
      }
    ]
  },
  "use": {
    "pos": "动词/名词",
    "meaning": "使用；运用；用途",
    "phonetic": "/juːz/",
    "explanation": "利用工具或方法。",
    "example": "Use your creativity to solve it.",
    "exampleCn": "发挥你的创造力来解决它。",
    "family": [
      "use"
    ],
    "collocations": [
      {
        "phrase": "use usage",
        "meaning": "使用；运用；用途的基础运用"
      }
    ]
  },
  "find": {
    "pos": "动词",
    "meaning": "找到；发现；发觉",
    "phonetic": "/faɪnd/",
    "explanation": "寻找的结果或体会到。",
    "example": "You will find peace within.",
    "exampleCn": "你会找到内心的平静。",
    "family": [
      "find"
    ],
    "collocations": [
      {
        "phrase": "find usage",
        "meaning": "找到；发现；发觉的基础运用"
      }
    ]
  },
  "give": {
    "pos": "动词",
    "meaning": "给；赋予；奉献",
    "phonetic": "/ɡɪv/",
    "explanation": "传递转移所有权。",
    "example": "Give love and receive joy.",
    "exampleCn": "给予爱心，收获喜悦。",
    "family": [
      "give"
    ],
    "collocations": [
      {
        "phrase": "give usage",
        "meaning": "给；赋予；奉献的基础运用"
      }
    ]
  },
  "tell": {
    "pos": "动词",
    "meaning": "告诉；讲述；辨别",
    "phonetic": "/tɛl/",
    "explanation": "向某人传达信息。",
    "example": "Tell me your favorite story.",
    "exampleCn": "告诉我你最喜爱的故事。",
    "family": [
      "tell"
    ],
    "collocations": [
      {
        "phrase": "tell usage",
        "meaning": "告诉；讲述；辨别的基础运用"
      }
    ]
  },
  "work": {
    "pos": "动词/名词",
    "meaning": "工作；起作用；运转",
    "phonetic": "/wɜːrk/",
    "explanation": "从事劳动或机制起效。",
    "example": "Hard work brings great rewards.",
    "exampleCn": "辛勤耕耘带来丰硕回报。",
    "family": [
      "work"
    ],
    "collocations": [
      {
        "phrase": "work usage",
        "meaning": "工作；起作用；运转的基础运用"
      }
    ]
  },
  "call": {
    "pos": "动词/名词",
    "meaning": "呼叫；称呼；给...打电话",
    "phonetic": "/kɔːl/",
    "explanation": "发声唤人或联络。",
    "example": "Call me whenever you need help.",
    "exampleCn": "任何时候需要帮助就给我打电话。",
    "family": [
      "call"
    ],
    "collocations": [
      {
        "phrase": "call usage",
        "meaning": "呼叫；称呼；给...打电话的基础运用"
      }
    ]
  },
  "try": {
    "pos": "动词/名词",
    "meaning": "尝试；努力；审理",
    "phonetic": "/traɪ/",
    "explanation": "付出努力试验。",
    "example": "Try again with full confidence.",
    "exampleCn": "满怀信心再试一次。",
    "family": [
      "try"
    ],
    "collocations": [
      {
        "phrase": "try usage",
        "meaning": "尝试；努力；审理的基础运用"
      }
    ]
  },
  "ask": {
    "pos": "动词",
    "meaning": "问；请求；邀请",
    "phonetic": "/ɑːsk/",
    "explanation": "提出疑问或请求。",
    "example": "Ask questions when in doubt.",
    "exampleCn": "心存疑问时大胆提问。",
    "family": [
      "ask"
    ],
    "collocations": [
      {
        "phrase": "ask usage",
        "meaning": "问；请求；邀请的基础运用"
      }
    ]
  },
  "need": {
    "pos": "动词/名词",
    "meaning": "需要；必须",
    "phonetic": "/niːd/",
    "explanation": "表达必要性。",
    "example": "We need more practice every day.",
    "exampleCn": "我们需要每天多加练习。",
    "family": [
      "need"
    ],
    "collocations": [
      {
        "phrase": "need usage",
        "meaning": "需要；必须的基础运用"
      }
    ]
  },
  "feel": {
    "pos": "动词/名词",
    "meaning": "感觉；触摸；体会",
    "phonetic": "/fiːl/",
    "explanation": "身心感知与情绪。",
    "example": "Feel the rhythm of the language.",
    "exampleCn": "感受这种语言的韵律美。",
    "family": [
      "feel"
    ],
    "collocations": [
      {
        "phrase": "feel usage",
        "meaning": "感觉；触摸；体会的基础运用"
      }
    ]
  },
  "become": {
    "pos": "动词",
    "meaning": "变成；成为；适合",
    "phonetic": "/bɪˈkʌm/",
    "explanation": "经历变化发展。",
    "example": "You will become more confident.",
    "exampleCn": "你会变得更加自信。",
    "family": [
      "become"
    ],
    "collocations": [
      {
        "phrase": "become usage",
        "meaning": "变成；成为；适合的基础运用"
      }
    ]
  },
  "leave": {
    "pos": "动词/名词",
    "meaning": "离开；留下；假期",
    "phonetic": "/liːv/",
    "explanation": "脱离场所或遗留物品。",
    "example": "Leave your doubts behind.",
    "exampleCn": "把疑虑抛在脑后。",
    "family": [
      "leave"
    ],
    "collocations": [
      {
        "phrase": "leave usage",
        "meaning": "离开；留下；假期的基础运用"
      }
    ]
  },
  "put": {
    "pos": "动词",
    "meaning": "放；安置；表达",
    "phonetic": "/pʊt/",
    "explanation": "摆放位置或用言语表达。",
    "example": "Put words into meaningful practice.",
    "exampleCn": "将词汇投入到有意义的练习中。",
    "family": [
      "put"
    ],
    "collocations": [
      {
        "phrase": "put usage",
        "meaning": "放；安置；表达的基础运用"
      }
    ]
  },
  "mean": {
    "pos": "动词/形容词",
    "meaning": "意思是；意味着；刻薄的",
    "phonetic": "/miːn/",
    "explanation": "表达含义或心意。",
    "example": "What does this phrase mean?",
    "exampleCn": "这个短语是什么意思？",
    "family": [
      "mean"
    ],
    "collocations": [
      {
        "phrase": "mean usage",
        "meaning": "意思是；意味着；刻薄的的基础运用"
      }
    ]
  },
  "keep": {
    "pos": "动词",
    "meaning": "保持；继续；保存",
    "phonetic": "/kiːp/",
    "explanation": "延续状态或遵守诺言。",
    "example": "Keep moving forward steadily.",
    "exampleCn": "坚定沉稳地继续前行。",
    "family": [
      "keep"
    ],
    "collocations": [
      {
        "phrase": "keep usage",
        "meaning": "保持；继续；保存的基础运用"
      }
    ]
  },
  "let": {
    "pos": "动词",
    "meaning": "让；允许；出租",
    "phonetic": "/lɛt/",
    "explanation": "允许施动或许可。",
    "example": "Let your inner light shine bright.",
    "exampleCn": "让你内心的光芒璀璨绽放。",
    "family": [
      "let"
    ],
    "collocations": [
      {
        "phrase": "let usage",
        "meaning": "让；允许；出租的基础运用"
      }
    ]
  },
  "begin": {
    "pos": "动词",
    "meaning": "开始；着手",
    "phonetic": "/bɪˈɡɪn/",
    "explanation": "开启某项事务。",
    "example": "A great journey begins today.",
    "exampleCn": "一段伟大的旅程始于今日。",
    "family": [
      "begin"
    ],
    "collocations": [
      {
        "phrase": "begin usage",
        "meaning": "开始；着手的基础运用"
      }
    ]
  },
  "seem": {
    "pos": "动词",
    "meaning": "似乎；仿佛",
    "phonetic": "/siːm/",
    "explanation": "主观印象显得。",
    "example": "Everything seems peaceful here.",
    "exampleCn": "这里的一切看起来十分祥和。",
    "family": [
      "seem"
    ],
    "collocations": [
      {
        "phrase": "seem usage",
        "meaning": "似乎；仿佛的基础运用"
      }
    ]
  },
  "help": {
    "pos": "动词/名词",
    "meaning": "帮助；协助；救命",
    "phonetic": "/hɛlp/",
    "explanation": "提供援助扶持。",
    "example": "Help each other learn and grow.",
    "exampleCn": "互相帮助，共同成长。",
    "family": [
      "help"
    ],
    "collocations": [
      {
        "phrase": "help usage",
        "meaning": "帮助；协助；救命的基础运用"
      }
    ]
  },
  "talk": {
    "pos": "动词/名词",
    "meaning": "交谈；讲话；演讲",
    "phonetic": "/tɔːk/",
    "explanation": "双向口头交流。",
    "example": "Let us talk about your dreams.",
    "exampleCn": "让我们谈谈你的梦想。",
    "family": [
      "talk"
    ],
    "collocations": [
      {
        "phrase": "talk usage",
        "meaning": "交谈；讲话；演讲的基础运用"
      }
    ]
  },
  "turn": {
    "pos": "动词/名词",
    "meaning": "转弯；变成；轮流",
    "phonetic": "/tɜːrn/",
    "explanation": "旋转方向或轮次。",
    "example": "Turn obstacles into opportunities.",
    "exampleCn": "将障碍转化为机遇。",
    "family": [
      "turn"
    ],
    "collocations": [
      {
        "phrase": "turn usage",
        "meaning": "转弯；变成；轮流的基础运用"
      }
    ]
  },
  "start": {
    "pos": "动词/名词",
    "meaning": "开始；出发；启动",
    "phonetic": "/stɑːrt/",
    "explanation": "启动行动或出发。",
    "example": "Start with small daily habits.",
    "exampleCn": "从每天的小习惯开始。",
    "family": [
      "start"
    ],
    "collocations": [
      {
        "phrase": "start usage",
        "meaning": "开始；出发；启动的基础运用"
      }
    ]
  },
  "show": {
    "pos": "动词/名词",
    "meaning": "展示；显露；演出",
    "phonetic": "/ʃoʊ/",
    "explanation": "呈现展现。",
    "example": "Show the world your unique talent.",
    "exampleCn": "向世界展现你独一无二的才华。",
    "family": [
      "show"
    ],
    "collocations": [
      {
        "phrase": "show usage",
        "meaning": "展示；显露；演出的基础运用"
      }
    ]
  },
  "hear": {
    "pos": "动词",
    "meaning": "听见；听说；审讯",
    "phonetic": "/hɪər/",
    "explanation": "听觉感知。",
    "example": "Can you hear the birds singing?",
    "exampleCn": "你能听见鸟儿在歌唱吗？",
    "family": [
      "hear"
    ],
    "collocations": [
      {
        "phrase": "hear usage",
        "meaning": "听见；听说；审讯的基础运用"
      }
    ]
  },
  "play": {
    "pos": "动词/名词",
    "meaning": "玩耍；演奏；戏剧",
    "phonetic": "/pleɪ/",
    "explanation": "娱乐、弹奏乐器或扮演。",
    "example": "Music plays a vital role in life.",
    "exampleCn": "音乐在生活中扮演着关键角色。",
    "family": [
      "play"
    ],
    "collocations": [
      {
        "phrase": "play usage",
        "meaning": "玩耍；演奏；戏剧的基础运用"
      }
    ]
  },
  "run": {
    "pos": "动词/名词",
    "meaning": "跑；运转；经营",
    "phonetic": "/rʌn/",
    "explanation": "快速移动或机器运作。",
    "example": "Run toward your highest ideals.",
    "exampleCn": "奔向你崇高的理想。",
    "family": [
      "run"
    ],
    "collocations": [
      {
        "phrase": "run usage",
        "meaning": "跑；运转；经营的基础运用"
      }
    ]
  },
  "move": {
    "pos": "动词/名词",
    "meaning": "移动；感动；采取行动",
    "phonetic": "/muːv/",
    "explanation": "空间移动或触动内心。",
    "example": "Her inspiring words moved me deeply.",
    "exampleCn": "她励志的话语深深打动了我。",
    "family": [
      "move"
    ],
    "collocations": [
      {
        "phrase": "move usage",
        "meaning": "移动；感动；采取行动的基础运用"
      }
    ]
  },
  "like": {
    "pos": "动词/介词",
    "meaning": "喜欢；如同；像",
    "phonetic": "/laɪk/",
    "explanation": "喜爱喜好或比喻相似。",
    "example": "I like learning with this app.",
    "exampleCn": "我喜欢用这款应用学习。",
    "family": [
      "like"
    ],
    "collocations": [
      {
        "phrase": "like usage",
        "meaning": "喜欢；如同；像的基础运用"
      }
    ]
  },
  "live": {
    "pos": "动词/形容词",
    "meaning": "生活；居住；现场的",
    "phonetic": "/lɪv/",
    "explanation": "生存度日或居住于某地。",
    "example": "Live every day with passion.",
    "exampleCn": "满怀热情地度过每一天。",
    "family": [
      "live"
    ],
    "collocations": [
      {
        "phrase": "live usage",
        "meaning": "生活；居住；现场的的基础运用"
      }
    ]
  },
  "believe": {
    "pos": "动词",
    "meaning": "相信；信任；认为",
    "phonetic": "/bɪˈliːv/",
    "explanation": "抱有信念信心。",
    "example": "Believe in your limitless potential.",
    "exampleCn": "相信你无限的潜能。",
    "family": [
      "believe"
    ],
    "collocations": [
      {
        "phrase": "believe usage",
        "meaning": "相信；信任；认为的基础运用"
      }
    ]
  },
  "hold": {
    "pos": "动词/名词",
    "meaning": "握住；举行；支撑",
    "phonetic": "/hoʊld/",
    "explanation": "持握或举办活动。",
    "example": "Hold on to your cherished dreams.",
    "exampleCn": "坚守你珍视的梦想。",
    "family": [
      "hold"
    ],
    "collocations": [
      {
        "phrase": "hold usage",
        "meaning": "握住；举行；支撑的基础运用"
      }
    ]
  },
  "bring": {
    "pos": "动词",
    "meaning": "带来；引起；促使",
    "phonetic": "/brɪŋ/",
    "explanation": "把事物带往此处。",
    "example": "Knowledge brings immense freedom.",
    "exampleCn": "知识带来巨大的自由。",
    "family": [
      "bring"
    ],
    "collocations": [
      {
        "phrase": "bring usage",
        "meaning": "带来；引起；促使的基础运用"
      }
    ]
  },
  "happen": {
    "pos": "动词",
    "meaning": "发生；碰巧",
    "phonetic": "/ˈhæpən/",
    "explanation": "事件产生发生。",
    "example": "Great things happen when you try.",
    "exampleCn": "当你付出尝试，奇迹就会发生。",
    "family": [
      "happen"
    ],
    "collocations": [
      {
        "phrase": "happen usage",
        "meaning": "发生；碰巧的基础运用"
      }
    ]
  },
  "write": {
    "pos": "动词",
    "meaning": "书写；写作；著述",
    "phonetic": "/raɪt/",
    "explanation": "文字记录与创作。",
    "example": "Write your own life story proudly.",
    "exampleCn": "骄傲地书写你的人生故事。",
    "family": [
      "write"
    ],
    "collocations": [
      {
        "phrase": "write usage",
        "meaning": "书写；写作；著述的基础运用"
      }
    ]
  },
  "provide": {
    "pos": "动词",
    "meaning": "提供；供给；装备",
    "phonetic": "/prəˈvaɪd/",
    "explanation": "供给所需物品。",
    "example": "Books provide endless wisdom.",
    "exampleCn": "书籍提供无穷的智慧。",
    "family": [
      "provide"
    ],
    "collocations": [
      {
        "phrase": "provide usage",
        "meaning": "提供；供给；装备的基础运用"
      }
    ]
  },
  "sit": {
    "pos": "动词",
    "meaning": "坐；就座；坐落",
    "phonetic": "/sɪt/",
    "explanation": "坐下休息就位。",
    "example": "Sit quietly and enjoy the silence.",
    "exampleCn": "静静坐下，享受宁静。",
    "family": [
      "sit"
    ],
    "collocations": [
      {
        "phrase": "sit usage",
        "meaning": "坐；就座；坐落的基础运用"
      }
    ]
  },
  "stand": {
    "pos": "动词/名词",
    "meaning": "站立；忍受；立场",
    "phonetic": "/stænd/",
    "explanation": "起立或坚持立场。",
    "example": "Stand up for what is right.",
    "exampleCn": "为正义而挺身而出。",
    "family": [
      "stand"
    ],
    "collocations": [
      {
        "phrase": "stand usage",
        "meaning": "站立；忍受；立场的基础运用"
      }
    ]
  },
  "lose": {
    "pos": "动词",
    "meaning": "失去；丢失；输掉",
    "phonetic": "/luːz/",
    "explanation": "遗失或遭遇挫败。",
    "example": "Never lose hope in difficult times.",
    "exampleCn": "在艰难困苦中永不放弃希望。",
    "family": [
      "lose"
    ],
    "collocations": [
      {
        "phrase": "lose usage",
        "meaning": "失去；丢失；输掉的基础运用"
      }
    ]
  },
  "pay": {
    "pos": "动词/名词",
    "meaning": "支付；付出代价；薪资",
    "phonetic": "/peɪ/",
    "explanation": "付款结账或给予注意。",
    "example": "Hard work always pays off in the end.",
    "exampleCn": "辛勤汗水终将换来丰硕回报。",
    "family": [
      "pay"
    ],
    "collocations": [
      {
        "phrase": "pay usage",
        "meaning": "支付；付出代价；薪资的基础运用"
      }
    ]
  },
  "meet": {
    "pos": "动词/名词",
    "meaning": "相遇；碰面；满足",
    "phonetic": "/miːt/",
    "explanation": "会面结识或满足需求。",
    "example": "Nice to meet you in this course.",
    "exampleCn": "很高兴在这门课程中与你相识。",
    "family": [
      "meet"
    ],
    "collocations": [
      {
        "phrase": "meet usage",
        "meaning": "相遇；碰面；满足的基础运用"
      }
    ]
  },
  "include": {
    "pos": "动词",
    "meaning": "包括；包含；列入",
    "phonetic": "/ɪnˈkluːd/",
    "explanation": "容纳在整体之中。",
    "example": "The curriculum includes rich stories.",
    "exampleCn": "课程体系包含丰富生动的故事。",
    "family": [
      "include"
    ],
    "collocations": [
      {
        "phrase": "include usage",
        "meaning": "包括；包含；列入的基础运用"
      }
    ]
  },
  "continue": {
    "pos": "动词",
    "meaning": "继续；持续；延伸",
    "phonetic": "/kənˈtɪnjuː/",
    "explanation": "不中断延展。",
    "example": "Continue practicing every single day.",
    "exampleCn": "每天坚持练习，持之以恒。",
    "family": [
      "continue"
    ],
    "collocations": [
      {
        "phrase": "continue usage",
        "meaning": "继续；持续；延伸的基础运用"
      }
    ]
  },
  "set": {
    "pos": "动词/名词/形容词",
    "meaning": "设置；树立；集合；固定的",
    "phonetic": "/sɛt/",
    "explanation": "安置树立目标。",
    "example": "Set clear goals for your study.",
    "exampleCn": "为你的学习设定明确目标。",
    "family": [
      "set"
    ],
    "collocations": [
      {
        "phrase": "set usage",
        "meaning": "设置；树立；集合；固定的的基础运用"
      }
    ]
  },
  "learn": {
    "pos": "动词",
    "meaning": "学习；得知；掌握",
    "phonetic": "/lɜːrn/",
    "explanation": "获取学问与技能。",
    "example": "Learn from mistakes with gratitude.",
    "exampleCn": "带着感恩的心从错误中吸取经验。",
    "family": [
      "learn"
    ],
    "collocations": [
      {
        "phrase": "learn usage",
        "meaning": "学习；得知；掌握的基础运用"
      }
    ]
  },
  "change": {
    "pos": "动词/名词",
    "meaning": "改变；变革；找零",
    "phonetic": "/tʃeɪndʒ/",
    "explanation": "发生转变或创新。",
    "example": "Small daily changes make big results.",
    "exampleCn": "每天的小改变带来巨大的成果。",
    "family": [
      "change"
    ],
    "collocations": [
      {
        "phrase": "change usage",
        "meaning": "改变；变革；找零的基础运用"
      }
    ]
  },
  "lead": {
    "pos": "动词/名词",
    "meaning": "带领；引导；领导",
    "phonetic": "/liːd/",
    "explanation": "指引方向导向结果。",
    "example": "Good habits lead to success.",
    "exampleCn": "良好的习惯通向成功。",
    "family": [
      "lead"
    ],
    "collocations": [
      {
        "phrase": "lead usage",
        "meaning": "带领；引导；领导的基础运用"
      }
    ]
  },
  "understand": {
    "pos": "动词",
    "meaning": "理解；明白；领会",
    "phonetic": "/ˌʌndərˈstænd/",
    "explanation": "领悟含义与真谛。",
    "example": "I understand grammar much better now.",
    "exampleCn": "我现在对语法的理解深刻得多了。",
    "family": [
      "understand"
    ],
    "collocations": [
      {
        "phrase": "understand usage",
        "meaning": "理解；明白；领会的基础运用"
      }
    ]
  },
  "watch": {
    "pos": "动词/名词",
    "meaning": "注视；观看；手表",
    "phonetic": "/wɒtʃ/",
    "explanation": "留心观察或腕表。",
    "example": "Watch your thoughts become actions.",
    "exampleCn": "留心你的思绪，它们会化作行动。",
    "family": [
      "watch"
    ],
    "collocations": [
      {
        "phrase": "watch usage",
        "meaning": "注视；观看；手表的基础运用"
      }
    ]
  },
  "follow": {
    "pos": "动词",
    "meaning": "跟随；遵循；理解",
    "phonetic": "/ˈfɒloʊ/",
    "explanation": "依照次序或遵照建议。",
    "example": "Follow your passion wherever it leads.",
    "exampleCn": "无论通向何方，追随你的心中热爱。",
    "family": [
      "follow"
    ],
    "collocations": [
      {
        "phrase": "follow usage",
        "meaning": "跟随；遵循；理解的基础运用"
      }
    ]
  },
  "stop": {
    "pos": "动词/名词",
    "meaning": "停止；中止；车站",
    "phonetic": "/stɒp/",
    "explanation": "中断动作行为。",
    "example": "Never stop expanding your horizons.",
    "exampleCn": "永远不要停下拓宽眼界的脚步。",
    "family": [
      "stop"
    ],
    "collocations": [
      {
        "phrase": "stop usage",
        "meaning": "停止；中止；车站的基础运用"
      }
    ]
  },
  "create": {
    "pos": "动词",
    "meaning": "创造；引起；创作",
    "phonetic": "/kriˈeɪt/",
    "explanation": "从无到有构建。",
    "example": "Create something wonderful today.",
    "exampleCn": "今天就去创造一些精彩的事物吧。",
    "family": [
      "create"
    ],
    "collocations": [
      {
        "phrase": "create usage",
        "meaning": "创造；引起；创作的基础运用"
      }
    ]
  },
  "speak": {
    "pos": "动词",
    "meaning": "讲话；说话；演说",
    "phonetic": "/spiːk/",
    "explanation": "发音言语表述。",
    "example": "Speak aloud with pride and joy.",
    "exampleCn": "自豪而喜悦地大声朗读。",
    "family": [
      "speak"
    ],
    "collocations": [
      {
        "phrase": "speak usage",
        "meaning": "讲话；说话；演说的基础运用"
      }
    ]
  },
  "read": {
    "pos": "动词",
    "meaning": "阅读；朗诵；看懂",
    "phonetic": "/riːd/",
    "explanation": "文字识别与领会。",
    "example": "Read good books and expand your mind.",
    "exampleCn": "多读好书，拓宽心胸格局。",
    "family": [
      "read"
    ],
    "collocations": [
      {
        "phrase": "read usage",
        "meaning": "阅读；朗诵；看懂的基础运用"
      }
    ]
  },
  "allow": {
    "pos": "动词",
    "meaning": "允许；准许；留出",
    "phonetic": "/əˈlaʊ/",
    "explanation": "给予许可或许可进行。",
    "example": "Allow yourself to make mistakes.",
    "exampleCn": "允许自己犯错并从中学习。",
    "family": [
      "allow"
    ],
    "collocations": [
      {
        "phrase": "allow usage",
        "meaning": "允许；准许；留出的基础运用"
      }
    ]
  },
  "add": {
    "pos": "动词",
    "meaning": "添加；增加；补充说",
    "phonetic": "/æd/",
    "explanation": "增添成分或数量。",
    "example": "Add joy to every single sentence.",
    "exampleCn": "为每一个句子增添拼写的喜悦。",
    "family": [
      "add"
    ],
    "collocations": [
      {
        "phrase": "add usage",
        "meaning": "添加；增加；补充说的基础运用"
      }
    ]
  },
  "spend": {
    "pos": "动词",
    "meaning": "花费；度过；消耗",
    "phonetic": "/spɛnd/",
    "explanation": "消磨时间或耗费金钱。",
    "example": "Spend time learning meaningful skills.",
    "exampleCn": "花时间掌握有意义的技能。",
    "family": [
      "spend"
    ],
    "collocations": [
      {
        "phrase": "spend usage",
        "meaning": "花费；度过；消耗的基础运用"
      }
    ]
  },
  "grow": {
    "pos": "动词",
    "meaning": "成长；种植；变大",
    "phonetic": "/ɡroʊ/",
    "explanation": "生命孕育茁壮成长。",
    "example": "Watch your language skills grow.",
    "exampleCn": "看着你的语言技能茁壮成长。",
    "family": [
      "grow"
    ],
    "collocations": [
      {
        "phrase": "grow usage",
        "meaning": "成长；种植；变大的基础运用"
      }
    ]
  },
  "open": {
    "pos": "动词/形容词",
    "meaning": "打开；开放的；坦率的",
    "phonetic": "/ˈoʊpən/",
    "explanation": "敞开大门或心情。",
    "example": "Open your heart to new cultures.",
    "exampleCn": "向多元文化敞开包容的心胸。",
    "family": [
      "open"
    ],
    "collocations": [
      {
        "phrase": "open usage",
        "meaning": "打开；开放的；坦率的的基础运用"
      }
    ]
  },
  "walk": {
    "pos": "动词/名词",
    "meaning": "步行；散步；走过",
    "phonetic": "/wɔːk/",
    "explanation": "双足行走活动。",
    "example": "Walk forward step by determined step.",
    "exampleCn": "坚定执着地一步一个脚印前行。",
    "family": [
      "walk"
    ],
    "collocations": [
      {
        "phrase": "walk usage",
        "meaning": "步行；散步；走过的基础运用"
      }
    ]
  },
  "win": {
    "pos": "动词/名词",
    "meaning": "获胜；赢得；成功",
    "phonetic": "/wɪn/",
    "explanation": "取得胜利收获奖赏。",
    "example": "Consistent practice wins every race.",
    "exampleCn": "持之以恒的练习能赢得每一场赛跑。",
    "family": [
      "win"
    ],
    "collocations": [
      {
        "phrase": "win usage",
        "meaning": "获胜；赢得；成功的基础运用"
      }
    ]
  },
  "offer": {
    "pos": "动词/名词",
    "meaning": "提供；提议；录取通知",
    "phonetic": "/ˈɒfər/",
    "explanation": "主动呈递帮助或方案。",
    "example": "This mall offers thousands of sentences.",
    "exampleCn": "该商城提供数以千计的精品地道句子。",
    "family": [
      "offer"
    ],
    "collocations": [
      {
        "phrase": "offer usage",
        "meaning": "提供；提议；录取通知的基础运用"
      }
    ]
  },
  "remember": {
    "pos": "动词",
    "meaning": "记住；牢记；回忆起",
    "phonetic": "/rɪˈmɛmbər/",
    "explanation": "保持记忆不遗忘。",
    "example": "Remember how far you have come.",
    "exampleCn": "牢记你一路走来所取得的成就。",
    "family": [
      "remember"
    ],
    "collocations": [
      {
        "phrase": "remember usage",
        "meaning": "记住；牢记；回忆起的基础运用"
      }
    ]
  },
  "love": {
    "pos": "动词/名词",
    "meaning": "爱；热爱；深爱",
    "phonetic": "/lʌv/",
    "explanation": "真挚强烈的情感。",
    "example": "Do what you genuinely love.",
    "exampleCn": "去做你真正热爱的事情。",
    "family": [
      "love"
    ],
    "collocations": [
      {
        "phrase": "love usage",
        "meaning": "爱；热爱；深爱的基础运用"
      }
    ]
  },
  "consider": {
    "pos": "动词",
    "meaning": "考虑；认为；体贴",
    "phonetic": "/kənˈsɪdər/",
    "explanation": "仔细琢磨衡量。",
    "example": "Consider all factors thoughtfully.",
    "exampleCn": "周详而深思熟虑地考虑所有因素。",
    "family": [
      "consider"
    ],
    "collocations": [
      {
        "phrase": "consider usage",
        "meaning": "考虑；认为；体贴的基础运用"
      }
    ]
  },
  "appear": {
    "pos": "动词",
    "meaning": "出现；显得；似乎",
    "phonetic": "/əˈpɪər/",
    "explanation": "显露踪迹或表面神情。",
    "example": "A bright smile appeared on her face.",
    "exampleCn": "她脸上浮现出灿烂的微笑。",
    "family": [
      "appear"
    ],
    "collocations": [
      {
        "phrase": "appear usage",
        "meaning": "出现；显得；似乎的基础运用"
      }
    ]
  },
  "buy": {
    "pos": "动词/名词",
    "meaning": "购买；买下",
    "phonetic": "/baɪ/",
    "explanation": "金钱换取货物。",
    "example": "Invest in knowledge you never lose.",
    "exampleCn": "投资于知识，你永不贬值。",
    "family": [
      "buy"
    ],
    "collocations": [
      {
        "phrase": "buy usage",
        "meaning": "购买；买下的基础运用"
      }
    ]
  },
  "wait": {
    "pos": "动词/名词",
    "meaning": "等待；等候；侍奉",
    "phonetic": "/weɪt/",
    "explanation": "停留守候期待发生。",
    "example": "Good things come to those who wait.",
    "exampleCn": "美好的事物属于那些耐心坚守的人。",
    "family": [
      "wait"
    ],
    "collocations": [
      {
        "phrase": "wait usage",
        "meaning": "等待；等候；侍奉的基础运用"
      }
    ]
  },
  "serve": {
    "pos": "动词",
    "meaning": "服务；服役；上菜",
    "phonetic": "/sɜːrv/",
    "explanation": "贡献力量或提供餐饮。",
    "example": "Use your skills to serve society.",
    "exampleCn": "用你的技能为社会贡献力量。",
    "family": [
      "serve"
    ],
    "collocations": [
      {
        "phrase": "serve usage",
        "meaning": "服务；服役；上菜的基础运用"
      }
    ]
  },
  "send": {
    "pos": "动词",
    "meaning": "发送；寄出；派遣",
    "phonetic": "/sɛnd/",
    "explanation": "寄送信件或传达。",
    "example": "Send warm greetings to your friends.",
    "exampleCn": "向你的朋友们致以温馨的问候。",
    "family": [
      "send"
    ],
    "collocations": [
      {
        "phrase": "send usage",
        "meaning": "发送；寄出；派遣的基础运用"
      }
    ]
  },
  "expect": {
    "pos": "动词",
    "meaning": "期待；预料；期望",
    "phonetic": "/ɪkˈspɛkt/",
    "explanation": "期盼发生预先设想。",
    "example": "Expect the best and prepare with grit.",
    "exampleCn": "怀最好的期许，以坚韧的心做足准备。",
    "family": [
      "expect"
    ],
    "collocations": [
      {
        "phrase": "expect usage",
        "meaning": "期待；预料；期望的基础运用"
      }
    ]
  },
  "build": {
    "pos": "动词/名词",
    "meaning": "建造；树立；体格",
    "phonetic": "/bɪld/",
    "explanation": "搭建构造体系。",
    "example": "Build a rock-solid foundation.",
    "exampleCn": "打造坚如磐石的语言基础。",
    "family": [
      "build"
    ],
    "collocations": [
      {
        "phrase": "build usage",
        "meaning": "建造；树立；体格的基础运用"
      }
    ]
  },
  "stay": {
    "pos": "动词/名词",
    "meaning": "停留；保持；借宿",
    "phonetic": "/steɪ/",
    "explanation": "留在某地或维持状态。",
    "example": "Stay curious and keep exploring.",
    "exampleCn": "保持好奇心，不断探索未知。",
    "family": [
      "stay"
    ],
    "collocations": [
      {
        "phrase": "stay usage",
        "meaning": "停留；保持；借宿的基础运用"
      }
    ]
  },
  "fall": {
    "pos": "动词/名词",
    "meaning": "落下；跌倒；秋天",
    "phonetic": "/fɔːl/",
    "explanation": "重力下坠或季节秋天。",
    "example": "Leaves fall softly in autumn.",
    "exampleCn": "秋日里落叶轻盈飘落。",
    "family": [
      "fall"
    ],
    "collocations": [
      {
        "phrase": "fall usage",
        "meaning": "落下；跌倒；秋天的基础运用"
      }
    ]
  },
  "cut": {
    "pos": "动词/名词",
    "meaning": "切；削减；剪短",
    "phonetic": "/kʌt/",
    "explanation": "利器切割或减少数量。",
    "example": "Cut through complexity with clarity.",
    "exampleCn": "以清晰的思维斩断复杂的纷扰。",
    "family": [
      "cut"
    ],
    "collocations": [
      {
        "phrase": "cut usage",
        "meaning": "切；削减；剪短的基础运用"
      }
    ]
  },
  "reach": {
    "pos": "动词/名词",
    "meaning": "达到；触及；伸出手臂",
    "phonetic": "/riːtʃ/",
    "explanation": "抵达高度或延伸范围。",
    "example": "Reach for your highest aspirations.",
    "exampleCn": "伸出双手去触碰你最高的理想。",
    "family": [
      "reach"
    ],
    "collocations": [
      {
        "phrase": "reach usage",
        "meaning": "达到；触及；伸出手臂的基础运用"
      }
    ]
  },
  "remain": {
    "pos": "动词",
    "meaning": "保持；剩余；留下",
    "phonetic": "/rɪˈmeɪn/",
    "explanation": "持续某种稳定状态。",
    "example": "Remain calm in the face of pressure.",
    "exampleCn": "面对压力保持镇定从容。",
    "family": [
      "remain"
    ],
    "collocations": [
      {
        "phrase": "remain usage",
        "meaning": "保持；剩余；留下的基础运用"
      }
    ]
  },
  "suggest": {
    "pos": "动词",
    "meaning": "建议；暗示；表明",
    "phonetic": "/səˈdʒɛst/",
    "explanation": "提出提议或暗指。",
    "example": "The teacher suggested daily spelling.",
    "exampleCn": "老师建议每天坚持拼写句子。",
    "family": [
      "suggest"
    ],
    "collocations": [
      {
        "phrase": "suggest usage",
        "meaning": "建议；暗示；表明的基础运用"
      }
    ]
  },
  "raise": {
    "pos": "动词/名词",
    "meaning": "提高；举起；抚养；加薪",
    "phonetic": "/reɪz/",
    "explanation": "抬升高度或培育成长。",
    "example": "Raise your standards and strive high.",
    "exampleCn": "提高自我要求，向更高峰攀登。",
    "family": [
      "raise"
    ],
    "collocations": [
      {
        "phrase": "raise usage",
        "meaning": "提高；举起；抚养；加薪的基础运用"
      }
    ]
  },
  "pass": {
    "pos": "动词/名词",
    "meaning": "通过；经过；传递；通行证",
    "phonetic": "/pɑːs/",
    "explanation": "跨越关卡或时间流逝。",
    "example": "Time passes quickly when learning.",
    "exampleCn": "投入学习时时光总是飞逝。",
    "family": [
      "pass"
    ],
    "collocations": [
      {
        "phrase": "pass usage",
        "meaning": "通过；经过；传递；通行证的基础运用"
      }
    ]
  },
  "sell": {
    "pos": "动词",
    "meaning": "出售；销售；畅销",
    "phonetic": "/sɛl/",
    "explanation": "卖出商品或推销理念。",
    "example": "Honesty is the best policy to sell.",
    "exampleCn": "诚实是推销理念的最佳法则。",
    "family": [
      "sell"
    ],
    "collocations": [
      {
        "phrase": "sell usage",
        "meaning": "出售；销售；畅销的基础运用"
      }
    ]
  },
  "require": {
    "pos": "动词",
    "meaning": "需要；要求；命令",
    "phonetic": "/rɪˈkwaɪər/",
    "explanation": "规则所必要必须。",
    "example": "Fluency requires dedicated practice.",
    "exampleCn": "流利地道需要专注持之以恒的练习。",
    "family": [
      "require"
    ],
    "collocations": [
      {
        "phrase": "require usage",
        "meaning": "需要；要求；命令的基础运用"
      }
    ]
  },
  "report": {
    "pos": "动词/名词",
    "meaning": "汇报；报道；报告",
    "phonetic": "/rɪˈpɔːrt/",
    "explanation": "报告事实陈述工作。",
    "example": "Report your progress with confidence.",
    "exampleCn": "自信地汇报你的学习进展。",
    "family": [
      "report"
    ],
    "collocations": [
      {
        "phrase": "report usage",
        "meaning": "汇报；报道；报告的基础运用"
      }
    ]
  },
  "decide": {
    "pos": "动词",
    "meaning": "决定；判定；决断",
    "phonetic": "/dɪˈsaɪd/",
    "explanation": "做出最终抉择。",
    "example": "Decide to excel starting today.",
    "exampleCn": "从今天起下定决心追求卓越。",
    "family": [
      "decide"
    ],
    "collocations": [
      {
        "phrase": "decide usage",
        "meaning": "决定；判定；决断的基础运用"
      }
    ]
  },
  "pull": {
    "pos": "动词/名词",
    "meaning": "拉；拔；牵引力",
    "phonetic": "/pʊl/",
    "explanation": "施加拉力拽动。",
    "example": "Pull together to achieve great goals.",
    "exampleCn": "齐心协力实现宏伟目标。",
    "family": [
      "pull"
    ],
    "collocations": [
      {
        "phrase": "pull usage",
        "meaning": "拉；拔；牵引力的基础运用"
      }
    ]
  },
  "hope": {
    "pos": "动词/名词",
    "meaning": "希望；期望；寄托",
    "phonetic": "/hoʊp/",
    "explanation": "心怀期盼与光明。",
    "example": "Never lose hope in any storm.",
    "exampleCn": "在任何风雨中都不要丢失希望。",
    "family": [
      "hope"
    ],
    "collocations": [
      {
        "phrase": "hope usage",
        "meaning": "希望；期望；寄托的基础运用"
      }
    ]
  },
  "care": {
    "pos": "动词/名词",
    "meaning": "关心；关怀；照料",
    "phonetic": "/kɛər/",
    "explanation": "体贴照顾挂念。",
    "example": "Take good care of your well-being.",
    "exampleCn": "好好照顾你的身心健康。",
    "family": [
      "care"
    ],
    "collocations": [
      {
        "phrase": "care usage",
        "meaning": "关心；关怀；照料的基础运用"
      }
    ]
  },
  "plan": {
    "pos": "动词/名词",
    "meaning": "计划；规划；打算",
    "phonetic": "/plæn/",
    "explanation": "设计制定行动蓝图。",
    "example": "Plan your schedule thoughtfully.",
    "exampleCn": "深思熟虑地规划你的学习日程。",
    "family": [
      "plan"
    ],
    "collocations": [
      {
        "phrase": "plan usage",
        "meaning": "计划；规划；打算的基础运用"
      }
    ]
  },
  "develop": {
    "pos": "动词",
    "meaning": "发展；培养；开发",
    "phonetic": "/dɪˈvɛləp/",
    "explanation": "成长壮大研制新物。",
    "example": "Develop an ear for spoken English.",
    "exampleCn": "培养对地道英语口语的敏锐听觉。",
    "family": [
      "develop"
    ],
    "collocations": [
      {
        "phrase": "develop usage",
        "meaning": "发展；培养；开发的基础运用"
      }
    ]
  },
  "protect": {
    "pos": "动词",
    "meaning": "保护；保卫；防护",
    "phonetic": "/prəˈtɛkt/",
    "explanation": "免受伤害侵袭。",
    "example": "Protect the natural environment.",
    "exampleCn": "保护自然生态环境。",
    "family": [
      "protect"
    ],
    "collocations": [
      {
        "phrase": "protect usage",
        "meaning": "保护；保卫；防护的基础运用"
      }
    ]
  },
  "time": {
    "pos": "名词",
    "meaning": "时间；时代；次数",
    "phonetic": "/taɪm/",
    "explanation": "时间概念或历史岁月。",
    "example": "Value your precious time.",
    "exampleCn": "珍惜你宝贵的时光。",
    "family": [
      "time"
    ],
    "collocations": [
      {
        "phrase": "time usage",
        "meaning": "时间；时代；次数的基础运用"
      }
    ]
  },
  "year": {
    "pos": "名词",
    "meaning": "年；岁月；年纪",
    "phonetic": "/jɪər/",
    "explanation": "地球公转周期或年龄。",
    "example": "This year is full of opportunities.",
    "exampleCn": "这一年充满了崭新的机遇。",
    "family": [
      "year"
    ],
    "collocations": [
      {
        "phrase": "year usage",
        "meaning": "年；岁月；年纪的基础运用"
      }
    ]
  },
  "people": {
    "pos": "名词",
    "meaning": "人们；人民；民族",
    "phonetic": "/ˈpiːpl/",
    "explanation": "复数人类个体集合。",
    "example": "Kind people make the world brighter.",
    "exampleCn": "善良的人们让世界更加美好。",
    "family": [
      "people"
    ],
    "collocations": [
      {
        "phrase": "people usage",
        "meaning": "人们；人民；民族的基础运用"
      }
    ]
  },
  "way": {
    "pos": "名词",
    "meaning": "道路；方法；方向",
    "phonetic": "/weɪ/",
    "explanation": "路径途径或办事手段。",
    "example": "Where there is a will, there is a way.",
    "exampleCn": "有志者，事竟成。",
    "family": [
      "way"
    ],
    "collocations": [
      {
        "phrase": "way usage",
        "meaning": "道路；方法；方向的基础运用"
      }
    ]
  },
  "day": {
    "pos": "名词",
    "meaning": "天；白天；日子",
    "phonetic": "/deɪ/",
    "explanation": "昼夜周期或晴朗时光。",
    "example": "Have a productive and joyful day.",
    "exampleCn": "祝你有充实而愉快的一天。",
    "family": [
      "day"
    ],
    "collocations": [
      {
        "phrase": "day usage",
        "meaning": "天；白天；日子的基础运用"
      }
    ]
  },
  "man": {
    "pos": "名词",
    "meaning": "男人；人类",
    "phonetic": "/mæn/",
    "explanation": "成年男性或人类泛指。",
    "example": "A wise man listens more than speaks.",
    "exampleCn": "智者倾听多于夸夸其谈。",
    "family": [
      "man"
    ],
    "collocations": [
      {
        "phrase": "man usage",
        "meaning": "男人；人类的基础运用"
      }
    ]
  },
  "thing": {
    "pos": "名词",
    "meaning": "事情；事物；东西",
    "phonetic": "/θɪŋ/",
    "explanation": "抽象事务或具体物品。",
    "example": "The best thing in life is learning.",
    "exampleCn": "人生最美好的事便是终身学习。",
    "family": [
      "thing"
    ],
    "collocations": [
      {
        "phrase": "thing usage",
        "meaning": "事情；事物；东西的基础运用"
      }
    ]
  },
  "woman": {
    "pos": "名词",
    "meaning": "女人；成年女子",
    "phonetic": "/ˈwʊmən/",
    "explanation": "成年女性个体。",
    "example": "She is an accomplished woman.",
    "exampleCn": "她是一位极具才干的优秀女性。",
    "family": [
      "woman"
    ],
    "collocations": [
      {
        "phrase": "woman usage",
        "meaning": "女人；成年女子的基础运用"
      }
    ]
  },
  "life": {
    "pos": "名词",
    "meaning": "生命；生活；一生",
    "phonetic": "/laɪf/",
    "explanation": "生存经历与存在过程。",
    "example": "Life is what you create each day.",
    "exampleCn": "生活全凭你每天如何去创造。",
    "family": [
      "life"
    ],
    "collocations": [
      {
        "phrase": "life usage",
        "meaning": "生命；生活；一生的基础运用"
      }
    ]
  },
  "child": {
    "pos": "名词",
    "meaning": "孩子；儿童",
    "phonetic": "/tʃaɪld/",
    "explanation": "幼童少年。",
    "example": "Every child deserves love and care.",
    "exampleCn": "每个孩子都配得上关爱与呵护。",
    "family": [
      "child"
    ],
    "collocations": [
      {
        "phrase": "child usage",
        "meaning": "孩子；儿童的基础运用"
      }
    ]
  },
  "world": {
    "pos": "名词",
    "meaning": "世界；地球；领域",
    "phonetic": "/wɜːrld/",
    "explanation": "人类社会或自然全球。",
    "example": "English connects you with the world.",
    "exampleCn": "英语让你与广阔的世界紧密相连。",
    "family": [
      "world"
    ],
    "collocations": [
      {
        "phrase": "world usage",
        "meaning": "世界；地球；领域的基础运用"
      }
    ]
  },
  "school": {
    "pos": "名词",
    "meaning": "学校；学派",
    "phonetic": "/skuːl/",
    "explanation": "传道授业教育场所。",
    "example": "School gives us a foundation to rise.",
    "exampleCn": "学校赋予了我们展翅高飞的基石。",
    "family": [
      "school"
    ],
    "collocations": [
      {
        "phrase": "school usage",
        "meaning": "学校；学派的基础运用"
      }
    ]
  },
  "state": {
    "pos": "名词/动词",
    "meaning": "状态；国家；声明",
    "phonetic": "/steɪt/",
    "explanation": "某种情形局面或宣布。",
    "example": "Maintain a peaceful state of mind.",
    "exampleCn": "保持宁静祥和的心境。",
    "family": [
      "state"
    ],
    "collocations": [
      {
        "phrase": "state usage",
        "meaning": "状态；国家；声明的基础运用"
      }
    ]
  },
  "family": {
    "pos": "名词",
    "meaning": "家庭；家族；亲属",
    "phonetic": "/ˈfæmɪli/",
    "explanation": "血缘相依的亲人集体。",
    "example": "Family is the anchor of love.",
    "exampleCn": "家庭是爱与温情的停泊港湾。",
    "family": [
      "family"
    ],
    "collocations": [
      {
        "phrase": "family usage",
        "meaning": "家庭；家族；亲属的基础运用"
      }
    ]
  },
  "student": {
    "pos": "名词",
    "meaning": "学生；学者",
    "phonetic": "/ˈstjuːdənt/",
    "explanation": "在学求知者。",
    "example": "Every student has vast potential.",
    "exampleCn": "每一个学生都蕴藏着无穷的潜能。",
    "family": [
      "student"
    ],
    "collocations": [
      {
        "phrase": "student usage",
        "meaning": "学生；学者的基础运用"
      }
    ]
  },
  "group": {
    "pos": "名词/动词",
    "meaning": "群体；小组；聚集",
    "phonetic": "/ɡruːp/",
    "explanation": "多人集体团队。",
    "example": "Collaborate with your study group.",
    "exampleCn": "与你的学习小组积极协作。",
    "family": [
      "group"
    ],
    "collocations": [
      {
        "phrase": "group usage",
        "meaning": "群体；小组；聚集的基础运用"
      }
    ]
  },
  "country": {
    "pos": "名词",
    "meaning": "国家；故乡；乡村",
    "phonetic": "/ˈkʌntri/",
    "explanation": "主权国或乡野自然。",
    "example": "Love your country and respect others.",
    "exampleCn": "热爱你的祖国，尊重世界各国。",
    "family": [
      "country"
    ],
    "collocations": [
      {
        "phrase": "country usage",
        "meaning": "国家；故乡；乡村的基础运用"
      }
    ]
  },
  "problem": {
    "pos": "名词",
    "meaning": "问题；难题；毛病",
    "phonetic": "/ˈprɒbləm/",
    "explanation": "亟待破解的矛盾与困境。",
    "example": "Break the complex problem down.",
    "exampleCn": "把复杂的问题拆解开来逐个突破。",
    "family": [
      "problem"
    ],
    "collocations": [
      {
        "phrase": "problem usage",
        "meaning": "问题；难题；毛病的基础运用"
      }
    ]
  },
  "hand": {
    "pos": "名词/动词",
    "meaning": "手；协助；传递",
    "phonetic": "/hænd/",
    "explanation": "手掌手臂或递交物品。",
    "example": "Lend a helping hand to neighbors.",
    "exampleCn": "向身边的邻里伸出援助之手。",
    "family": [
      "hand"
    ],
    "collocations": [
      {
        "phrase": "hand usage",
        "meaning": "手；协助；传递的基础运用"
      }
    ]
  },
  "part": {
    "pos": "名词/动词",
    "meaning": "部分；角色；分离",
    "phonetic": "/pɑːrt/",
    "explanation": "整体的一块或戏剧角色。",
    "example": "Spelling is a key part of fluency.",
    "exampleCn": "拼写是语言流利度的关键一环。",
    "family": [
      "part"
    ],
    "collocations": [
      {
        "phrase": "part usage",
        "meaning": "部分；角色；分离的基础运用"
      }
    ]
  },
  "place": {
    "pos": "名词/动词",
    "meaning": "地方；位置；放置",
    "phonetic": "/pleɪs/",
    "explanation": "空间地域或妥善安放。",
    "example": "Find a quiet place to read.",
    "exampleCn": "找一处安静的角落静心阅读。",
    "family": [
      "place"
    ],
    "collocations": [
      {
        "phrase": "place usage",
        "meaning": "地方；位置；放置的基础运用"
      }
    ]
  },
  "case": {
    "pos": "名词",
    "meaning": "情况；实例；箱子",
    "phonetic": "/keɪs/",
    "explanation": "实际事例或法律案件。",
    "example": "In any case, keep your promise.",
    "exampleCn": "无论何种情形，守住你的承诺。",
    "family": [
      "case"
    ],
    "collocations": [
      {
        "phrase": "case usage",
        "meaning": "情况；实例；箱子的基础运用"
      }
    ]
  },
  "week": {
    "pos": "名词",
    "meaning": "周；星期",
    "phonetic": "/wiːk/",
    "explanation": "七天时间周期。",
    "example": "Review what you learned this week.",
    "exampleCn": "认真复习你本周所学到的知识。",
    "family": [
      "week"
    ],
    "collocations": [
      {
        "phrase": "week usage",
        "meaning": "周；星期的基础运用"
      }
    ]
  },
  "company": {
    "pos": "名词",
    "meaning": "公司；陪伴；同伴",
    "phonetic": "/ˈkʌmpəni/",
    "explanation": "商业实体或作伴相随。",
    "example": "I enjoy the company of good books.",
    "exampleCn": "我享受与良书相伴的美妙时光。",
    "family": [
      "company"
    ],
    "collocations": [
      {
        "phrase": "company usage",
        "meaning": "公司；陪伴；同伴的基础运用"
      }
    ]
  },
  "system": {
    "pos": "名词",
    "meaning": "系统；体系；制度",
    "phonetic": "/ˈsɪstəm/",
    "explanation": "有机组织与运行规则。",
    "example": "Build a consistent study system.",
    "exampleCn": "构建一套持之以恒的高效学习体系。",
    "family": [
      "system"
    ],
    "collocations": [
      {
        "phrase": "system usage",
        "meaning": "系统；体系；制度的基础运用"
      }
    ]
  },
  "program": {
    "pos": "名词/动词",
    "meaning": "程序；节目；规划",
    "phonetic": "/ˈproʊɡræm/",
    "explanation": "活动安排或计算机软件。",
    "example": "This software program is powerful.",
    "exampleCn": "这款软件程序功能十分强大。",
    "family": [
      "program"
    ],
    "collocations": [
      {
        "phrase": "program usage",
        "meaning": "程序；节目；规划的基础运用"
      }
    ]
  },
  "question": {
    "pos": "名词/动词",
    "meaning": "问题；疑问；质疑",
    "phonetic": "/ˈkwɛstʃən/",
    "explanation": "提问探索求知。",
    "example": "Never hesitate to ask a question.",
    "exampleCn": "永远不要对提出问题心存顾虑。",
    "family": [
      "question"
    ],
    "collocations": [
      {
        "phrase": "question usage",
        "meaning": "问题；疑问；质疑的基础运用"
      }
    ]
  },
  "government": {
    "pos": "名词",
    "meaning": "政府；政体；治理",
    "phonetic": "/ˈɡʌvərnmənt/",
    "explanation": "国家治理机构。",
    "example": "The government supports education.",
    "exampleCn": "政府大力扶持教育事业的发展。",
    "family": [
      "government"
    ],
    "collocations": [
      {
        "phrase": "government usage",
        "meaning": "政府；政体；治理的基础运用"
      }
    ]
  },
  "number": {
    "pos": "名词/动词",
    "meaning": "数字；号码；编号",
    "phonetic": "/ˈnʌmbər/",
    "explanation": "数学计数或排定次序。",
    "example": "A large number of users joined in.",
    "exampleCn": "海量的用户纷纷加入进来。",
    "family": [
      "number"
    ],
    "collocations": [
      {
        "phrase": "number usage",
        "meaning": "数字；号码；编号的基础运用"
      }
    ]
  },
  "night": {
    "pos": "名词",
    "meaning": "夜晚；黑夜",
    "phonetic": "/naɪt/",
    "explanation": "夕阳西下夜幕降临。",
    "example": "Have a peaceful and restful night.",
    "exampleCn": "祝你度过一个安宁祥和的夜晚。",
    "family": [
      "night"
    ],
    "collocations": [
      {
        "phrase": "night usage",
        "meaning": "夜晚；黑夜的基础运用"
      }
    ]
  },
  "point": {
    "pos": "名词/动词",
    "meaning": "观点；要点；指向",
    "phonetic": "/pɔɪnt/",
    "explanation": "核心论点或尖端指向。",
    "example": "That is a brilliant and valid point.",
    "exampleCn": "这是一个精彩纷呈且极具说服力的观点。",
    "family": [
      "point"
    ],
    "collocations": [
      {
        "phrase": "point usage",
        "meaning": "观点；要点；指向的基础运用"
      }
    ]
  },
  "home": {
    "pos": "名词/副词",
    "meaning": "家；家乡；在家里",
    "phonetic": "/hoʊm/",
    "explanation": "温馨居所与精神归宿。",
    "example": "Home is where the warm heart lives.",
    "exampleCn": "心之所安处，即是最暖的家。",
    "family": [
      "home"
    ],
    "collocations": [
      {
        "phrase": "home usage",
        "meaning": "家；家乡；在家里的基础运用"
      }
    ]
  },
  "water": {
    "pos": "名词/动词",
    "meaning": "水；浇水",
    "phonetic": "/ˈwɔːtər/",
    "explanation": "生命之源清泉玉液。",
    "example": "Drink enough fresh water each day.",
    "exampleCn": "每天喝充足的纯净水。",
    "family": [
      "water"
    ],
    "collocations": [
      {
        "phrase": "water usage",
        "meaning": "水；浇水的基础运用"
      }
    ]
  },
  "room": {
    "pos": "名词",
    "meaning": "房间；空间；余地",
    "phonetic": "/ruːm/",
    "explanation": "室内居室或施展空间。",
    "example": "There is always room for growth.",
    "exampleCn": "追求成长的道路上永远留有广阔空间。",
    "family": [
      "room"
    ],
    "collocations": [
      {
        "phrase": "room usage",
        "meaning": "房间；空间；余地的基础运用"
      }
    ]
  },
  "mother": {
    "pos": "名词",
    "meaning": "母亲；妈妈",
    "phonetic": "/ˈmʌðər/",
    "explanation": "生养培育的伟大女性。",
    "example": "A mother gives unconditional love.",
    "exampleCn": "母亲给予的是毫无保留的无私大爱。",
    "family": [
      "mother"
    ],
    "collocations": [
      {
        "phrase": "mother usage",
        "meaning": "母亲；妈妈的基础运用"
      }
    ]
  },
  "area": {
    "pos": "名词",
    "meaning": "地区；领域；面积",
    "phonetic": "/ˈɛəriə/",
    "explanation": "地理区域或专业范畴。",
    "example": "Focus on your area of greatest strength.",
    "exampleCn": "将精力深耕于你最具优势的核心领域。",
    "family": [
      "area"
    ],
    "collocations": [
      {
        "phrase": "area usage",
        "meaning": "地区；领域；面积的基础运用"
      }
    ]
  },
  "money": {
    "pos": "名词",
    "meaning": "钱；财富；货币",
    "phonetic": "/ˈmʌni/",
    "explanation": "通用交换媒介财富。",
    "example": "Wise people manage money well.",
    "exampleCn": "有智慧的人擅长精明地管理财富。",
    "family": [
      "money"
    ],
    "collocations": [
      {
        "phrase": "money usage",
        "meaning": "钱；财富；货币的基础运用"
      }
    ]
  },
  "story": {
    "pos": "名词",
    "meaning": "故事；小说；历史",
    "phonetic": "/ˈstɔːri/",
    "explanation": "生动叙事传奇经历。",
    "example": "Tell a story that touches the soul.",
    "exampleCn": "讲述一个能触动灵魂深处的美妙故事。",
    "family": [
      "story"
    ],
    "collocations": [
      {
        "phrase": "story usage",
        "meaning": "故事；小说；历史的基础运用"
      }
    ]
  },
  "fact": {
    "pos": "名词",
    "meaning": "事实；真相；实情",
    "phonetic": "/fækt/",
    "explanation": "客观存在真实不虚。",
    "example": "Face facts with courage and logic.",
    "exampleCn": "以理性和勇气直面客观事实。",
    "family": [
      "fact"
    ],
    "collocations": [
      {
        "phrase": "fact usage",
        "meaning": "事实；真相；实情的基础运用"
      }
    ]
  },
  "month": {
    "pos": "名词",
    "meaning": "月；月份",
    "phonetic": "/mʌnθ/",
    "explanation": "日历月份历时。",
    "example": "Practice thirty days a month.",
    "exampleCn": "一个月三十天每天坚持练习。",
    "family": [
      "month"
    ],
    "collocations": [
      {
        "phrase": "month usage",
        "meaning": "月；月份的基础运用"
      }
    ]
  },
  "lot": {
    "pos": "名词/副词",
    "meaning": "许多；命运；签",
    "phonetic": "/lɒt/",
    "explanation": "大量丰富程度副词。",
    "example": "Thanks a lot for your patience.",
    "exampleCn": "非常感谢你所付出的极大耐心。",
    "family": [
      "lot"
    ],
    "collocations": [
      {
        "phrase": "lot usage",
        "meaning": "许多；命运；签的基础运用"
      }
    ]
  },
  "right": {
    "pos": "形容词/名词/副词",
    "meaning": "正确的；右边；权利；恰好",
    "phonetic": "/raɪt/",
    "explanation": "真确合理或合法权益。",
    "example": "You made the absolute right choice.",
    "exampleCn": "你做出了绝对无比正确的抉择。",
    "family": [
      "right"
    ],
    "collocations": [
      {
        "phrase": "right usage",
        "meaning": "正确的；右边；权利；恰好的基础运用"
      }
    ]
  },
  "study": {
    "pos": "动词/名词",
    "meaning": "学习；研究；书房",
    "phonetic": "/ˈstʌdi/",
    "explanation": "潜心钻研汲取学识。",
    "example": "Study English with joy and focus.",
    "exampleCn": "带着喜悦与专注深度研习英语。",
    "family": [
      "study"
    ],
    "collocations": [
      {
        "phrase": "study usage",
        "meaning": "学习；研究；书房的基础运用"
      }
    ]
  },
  "book": {
    "pos": "名词/动词",
    "meaning": "书本；预订",
    "phonetic": "/bʊk/",
    "explanation": "书籍著作或预定座席。",
    "example": "A book is a portal to new worlds.",
    "exampleCn": "一本书就是一扇通往崭新世界的传送门。",
    "family": [
      "book"
    ],
    "collocations": [
      {
        "phrase": "book usage",
        "meaning": "书本；预订的基础运用"
      }
    ]
  },
  "eye": {
    "pos": "名词/动词",
    "meaning": "眼睛；目光；审视",
    "phonetic": "/aɪ/",
    "explanation": "视觉器官凝神注视。",
    "example": "Keep an open eye on opportunities.",
    "exampleCn": "擦亮双眼敏锐捕捉一切机遇。",
    "family": [
      "eye"
    ],
    "collocations": [
      {
        "phrase": "eye usage",
        "meaning": "眼睛；目光；审视的基础运用"
      }
    ]
  },
  "job": {
    "pos": "名词",
    "meaning": "工作；职业；任务",
    "phonetic": "/dʒɒb/",
    "explanation": "岗位差事职务职责。",
    "example": "Do a splendid job on every task.",
    "exampleCn": "全力以赴把每项任务都做得尽善尽美。",
    "family": [
      "job"
    ],
    "collocations": [
      {
        "phrase": "job usage",
        "meaning": "工作；职业；任务的基础运用"
      }
    ]
  },
  "word": {
    "pos": "名词",
    "meaning": "单词；话语；诺言",
    "phonetic": "/wɜːrd/",
    "explanation": "语言词素或恪守誓言。",
    "example": "A single kind word can heal a heart.",
    "exampleCn": "一句温暖善意的话语便能抚慰人心。",
    "family": [
      "word"
    ],
    "collocations": [
      {
        "phrase": "word usage",
        "meaning": "单词；话语；诺言的基础运用"
      }
    ]
  },
  "business": {
    "pos": "名词",
    "meaning": "商业；生意；事务",
    "phonetic": "/ˈbɪznəs/",
    "explanation": "经商买卖事务行当。",
    "example": "Conduct your business with integrity.",
    "exampleCn": "以诚实守信的商道操持你的事业。",
    "family": [
      "business"
    ],
    "collocations": [
      {
        "phrase": "business usage",
        "meaning": "商业；生意；事务的基础运用"
      }
    ]
  },
  "issue": {
    "pos": "名词/动词",
    "meaning": "问题；发行；期刊",
    "phonetic": "/ˈɪʃuː/",
    "explanation": "争端热点或印发颁布。",
    "example": "Address this crucial issue promptly.",
    "exampleCn": "迅速有力地解决这一至关重要的问题。",
    "family": [
      "issue"
    ],
    "collocations": [
      {
        "phrase": "issue usage",
        "meaning": "问题；发行；期刊的基础运用"
      }
    ]
  },
  "side": {
    "pos": "名词/动词",
    "meaning": "侧面；立场；支持",
    "phonetic": "/saɪd/",
    "explanation": "方位侧翼或阵营立场。",
    "example": "Look on the bright side of life.",
    "exampleCn": "永远望向生活阳光明媚的积极一面。",
    "family": [
      "side"
    ],
    "collocations": [
      {
        "phrase": "side usage",
        "meaning": "侧面；立场；支持的基础运用"
      }
    ]
  },
  "kind": {
    "pos": "名词/形容词",
    "meaning": "种类；体贴的；和善的",
    "phonetic": "/kaɪnd/",
    "explanation": "分类归属或友善热忱。",
    "example": "Be kind and compassionate always.",
    "exampleCn": "永远保持和善体贴与慈悲关怀。",
    "family": [
      "kind"
    ],
    "collocations": [
      {
        "phrase": "kind usage",
        "meaning": "种类；体贴的；和善的的基础运用"
      }
    ]
  },
  "head": {
    "pos": "名词/动词",
    "meaning": "头脑；首领；前往",
    "phonetic": "/hɛd/",
    "explanation": "头颅中枢或率领前行。",
    "example": "Head toward your desired goals.",
    "exampleCn": "坚定不移地奔向你心之所向的目标。",
    "family": [
      "head"
    ],
    "collocations": [
      {
        "phrase": "head usage",
        "meaning": "头脑；首领；前往的基础运用"
      }
    ]
  },
  "house": {
    "pos": "名词/动词",
    "meaning": "房子；住宅；容纳",
    "phonetic": "/haʊs/",
    "explanation": "建筑住宅安置居所。",
    "example": "Build your dream house brick by brick.",
    "exampleCn": "一块砖一块砖地筑造起你梦想的家园。",
    "family": [
      "house"
    ],
    "collocations": [
      {
        "phrase": "house usage",
        "meaning": "房子；住宅；容纳的基础运用"
      }
    ]
  },
  "service": {
    "pos": "名词/动词",
    "meaning": "服务；服役；维修",
    "phonetic": "/ˈsɜːrvɪs/",
    "explanation": "提供便利惠及大众。",
    "example": "Excellent customer service matters.",
    "exampleCn": "精益求精的客户服务至关重要。",
    "family": [
      "service"
    ],
    "collocations": [
      {
        "phrase": "service usage",
        "meaning": "服务；服役；维修的基础运用"
      }
    ]
  },
  "friend": {
    "pos": "名词",
    "meaning": "朋友；友人",
    "phonetic": "/frɛnd/",
    "explanation": "知心伙伴患难之交。",
    "example": "A true friend is a treasure for life.",
    "exampleCn": "一位挚友是你此生最宝贵的无价之宝。",
    "family": [
      "friend"
    ],
    "collocations": [
      {
        "phrase": "friend usage",
        "meaning": "朋友；友人的基础运用"
      }
    ]
  },
  "father": {
    "pos": "名词",
    "meaning": "父亲；爸爸",
    "phonetic": "/ˈfɑːðər/",
    "explanation": "深沉威严如山的尊长。",
    "example": "My father taught me perseverance.",
    "exampleCn": "我的父亲教会了我持之以恒的毅力。",
    "family": [
      "father"
    ],
    "collocations": [
      {
        "phrase": "father usage",
        "meaning": "父亲；爸爸的基础运用"
      }
    ]
  },
  "power": {
    "pos": "名词/动词",
    "meaning": "力量；权力；供电",
    "phonetic": "/ˈpaʊər/",
    "explanation": "无穷伟力动能权能。",
    "example": "Knowledge is the ultimate power.",
    "exampleCn": "知识就是至高无上的力量。",
    "family": [
      "power"
    ],
    "collocations": [
      {
        "phrase": "power usage",
        "meaning": "力量；权力；供电的基础运用"
      }
    ]
  },
  "hour": {
    "pos": "名词",
    "meaning": "小时；钟点",
    "phonetic": "/ˈaʊər/",
    "explanation": "六十分钟时光岁月。",
    "example": "Spend an hour reading every evening.",
    "exampleCn": "每晚抽出一个小时静心读书。",
    "family": [
      "hour"
    ],
    "collocations": [
      {
        "phrase": "hour usage",
        "meaning": "小时；钟点的基础运用"
      }
    ]
  },
  "game": {
    "pos": "名词",
    "meaning": "游戏；比赛；博弈",
    "phonetic": "/ɡeɪm/",
    "explanation": "娱乐赛事竞技活动。",
    "example": "Life is not a game of luck.",
    "exampleCn": "人生绝非一场全凭运气的侥幸博弈。",
    "family": [
      "game"
    ],
    "collocations": [
      {
        "phrase": "game usage",
        "meaning": "游戏；比赛；博弈的基础运用"
      }
    ]
  },
  "line": {
    "pos": "名词/动词",
    "meaning": "线条；队伍；台词；排队",
    "phonetic": "/laɪn/",
    "explanation": "线段界限戏剧对白。",
    "example": "Every line in this script is brilliant.",
    "exampleCn": "这个剧本里的每一行台词都精妙绝伦。",
    "family": [
      "line"
    ],
    "collocations": [
      {
        "phrase": "line usage",
        "meaning": "线条；队伍；台词；排队的基础运用"
      }
    ]
  },
  "end": {
    "pos": "名词/动词",
    "meaning": "终点；结尾；结束",
    "phonetic": "/ɛnd/",
    "explanation": "极限边缘终止停顿。",
    "example": "A journey well ended is a success.",
    "exampleCn": "善始善终的旅程就是最大的成功。",
    "family": [
      "end"
    ],
    "collocations": [
      {
        "phrase": "end usage",
        "meaning": "终点；结尾；结束的基础运用"
      }
    ]
  },
  "member": {
    "pos": "名词",
    "meaning": "成员；会员",
    "phonetic": "/ˈmɛmbər/",
    "explanation": "团体组织组成分子。",
    "example": "He is an active member of the club.",
    "exampleCn": "他是俱乐部里极富活力的一员。",
    "family": [
      "member"
    ],
    "collocations": [
      {
        "phrase": "member usage",
        "meaning": "成员；会员的基础运用"
      }
    ]
  },
  "law": {
    "pos": "名词",
    "meaning": "法律；法则；规律",
    "phonetic": "/lɔː/",
    "explanation": "法律规章自然定律。",
    "example": "Respect the law and uphold fairness.",
    "exampleCn": "遵守法律，恪守社会公平正义。",
    "family": [
      "law"
    ],
    "collocations": [
      {
        "phrase": "law usage",
        "meaning": "法律；法则；规律的基础运用"
      }
    ]
  },
  "car": {
    "pos": "名词",
    "meaning": "汽车；轿车；车厢",
    "phonetic": "/kɑːr/",
    "explanation": "四轮机动交通载具。",
    "example": "Drive your car safely and carefully.",
    "exampleCn": "安全谨慎地驾驶你的汽车。",
    "family": [
      "car"
    ],
    "collocations": [
      {
        "phrase": "car usage",
        "meaning": "汽车；轿车；车厢的基础运用"
      }
    ]
  },
  "city": {
    "pos": "名词",
    "meaning": "城市；都市",
    "phonetic": "/ˈsɪti/",
    "explanation": "人口聚居繁华之都。",
    "example": "The city shines with neon lights.",
    "exampleCn": "城市在璀璨霓虹的映衬下熠熠生辉。",
    "family": [
      "city"
    ],
    "collocations": [
      {
        "phrase": "city usage",
        "meaning": "城市；都市的基础运用"
      }
    ]
  },
  "community": {
    "pos": "名词",
    "meaning": "社区；共同体；群体",
    "phonetic": "/kəˈmjuːnɪti/",
    "explanation": "地缘社会利益相连。",
    "example": "Support your local community warmly.",
    "exampleCn": "热情支持关爱你的社区大家庭。",
    "family": [
      "community"
    ],
    "collocations": [
      {
        "phrase": "community usage",
        "meaning": "社区；共同体；群体的基础运用"
      }
    ]
  },
  "name": {
    "pos": "名词/动词",
    "meaning": "名字；名誉；命名",
    "phonetic": "/neɪm/",
    "explanation": "称呼名望题名册封。",
    "example": "Make a proud name for yourself.",
    "exampleCn": "用你的汗水打拼出一片响当当的声名。",
    "family": [
      "name"
    ],
    "collocations": [
      {
        "phrase": "name usage",
        "meaning": "名字；名誉；命名的基础运用"
      }
    ]
  },
  "president": {
    "pos": "名词",
    "meaning": "总统；总裁；主席",
    "phonetic": "/ˈprɛzɪdənt/",
    "explanation": "国家元首机构首脑。",
    "example": "The president delivered a stirring speech.",
    "exampleCn": "主席发表了一篇振奋人心的精彩演讲。",
    "family": [
      "president"
    ],
    "collocations": [
      {
        "phrase": "president usage",
        "meaning": "总统；总裁；主席的基础运用"
      }
    ]
  },
  "team": {
    "pos": "名词/动词",
    "meaning": "团队；队伍；协作",
    "phonetic": "/tiːm/",
    "explanation": "齐心协力并肩作战。",
    "example": "Teamwork turns dream into reality.",
    "exampleCn": "团队协作将美好的憧憬转化为生动现实。",
    "family": [
      "team"
    ],
    "collocations": [
      {
        "phrase": "team usage",
        "meaning": "团队；队伍；协作的基础运用"
      }
    ]
  },
  "minute": {
    "pos": "名词/形容词",
    "meaning": "分钟；微小的；详细的",
    "phonetic": "/ˈmɪnɪt/",
    "explanation": "六十秒钟寸金光阴。",
    "example": "Give me just one minute to explain.",
    "exampleCn": "请给我短短一分钟来做个解释。",
    "family": [
      "minute"
    ],
    "collocations": [
      {
        "phrase": "minute usage",
        "meaning": "分钟；微小的；详细的的基础运用"
      }
    ]
  },
  "idea": {
    "pos": "名词",
    "meaning": "主意；想法；创意",
    "phonetic": "/aɪˈdiːə/",
    "explanation": "灵感思维智慧火花。",
    "example": "A creative idea can change the world.",
    "exampleCn": "一个富有创意的点子足以改变整个世界。",
    "family": [
      "idea"
    ],
    "collocations": [
      {
        "phrase": "idea usage",
        "meaning": "主意；想法；创意的基础运用"
      }
    ]
  },
  "kid": {
    "pos": "名词/动词",
    "meaning": "孩子；小孩；开玩笑",
    "phonetic": "/kɪd/",
    "explanation": "童稚少年逗趣打趣。",
    "example": "Every kid loves listening to fairy tales.",
    "exampleCn": "每个小孩子都痴迷于聆听美丽的童话。",
    "family": [
      "kid"
    ],
    "collocations": [
      {
        "phrase": "kid usage",
        "meaning": "孩子；小孩；开玩笑的基础运用"
      }
    ]
  },
  "body": {
    "pos": "名词",
    "meaning": "身体；躯体；主体",
    "phonetic": "/ˈbɒdi/",
    "explanation": "肉身躯干组织骨干。",
    "example": "Exercise keeps your body strong.",
    "exampleCn": "规律体育锻炼能让你的体魄强健有力。",
    "family": [
      "body"
    ],
    "collocations": [
      {
        "phrase": "body usage",
        "meaning": "身体；躯体；主体的基础运用"
      }
    ]
  },
  "information": {
    "pos": "名词",
    "meaning": "信息；资讯；情报",
    "phonetic": "/ˌɪnfərˈmeɪʃən/",
    "explanation": "知识数据事实汇编。",
    "example": "Accurate information guides decisions.",
    "exampleCn": "精准的信息能够为明智的决策保驾护航。",
    "family": [
      "information"
    ],
    "collocations": [
      {
        "phrase": "information usage",
        "meaning": "信息；资讯；情报的基础运用"
      }
    ]
  },
  "back": {
    "pos": "名词/副词/形容词",
    "meaning": "背部；回来；后面的",
    "phonetic": "/bæk/",
    "explanation": "脊背方位逆向返回。",
    "example": "Welcome back to your daily practice.",
    "exampleCn": "热烈欢迎重返你的每日拼写训练。",
    "family": [
      "back"
    ],
    "collocations": [
      {
        "phrase": "back usage",
        "meaning": "背部；回来；后面的的基础运用"
      }
    ]
  },
  "parent": {
    "pos": "名词",
    "meaning": "父亲；母亲；家长",
    "phonetic": "/ˈpɛərənt/",
    "explanation": "双亲长辈生身父母。",
    "example": "Parents guide their children with love.",
    "exampleCn": "父母用深沉的爱指引孩子成长的方向。",
    "family": [
      "parent"
    ],
    "collocations": [
      {
        "phrase": "parent usage",
        "meaning": "父亲；母亲；家长的基础运用"
      }
    ]
  },
  "face": {
    "pos": "名词/动词",
    "meaning": "脸庞；面容；面对",
    "phonetic": "/feɪs/",
    "explanation": "容貌面部迎面正视。",
    "example": "Face challenges with a bright smile.",
    "exampleCn": "迎着灿烂的微笑勇敢面对重重挑战。",
    "family": [
      "face"
    ],
    "collocations": [
      {
        "phrase": "face usage",
        "meaning": "脸庞；面容；面对的基础运用"
      }
    ]
  },
  "level": {
    "pos": "名词/形容词",
    "meaning": "水平；层次；平坦的",
    "phonetic": "/ˈlɛvəl/",
    "explanation": "高度段位等级标尺。",
    "example": "Reach a higher level of English mastery.",
    "exampleCn": "登临更加卓越高深的英语造诣境界。",
    "family": [
      "level"
    ],
    "collocations": [
      {
        "phrase": "level usage",
        "meaning": "水平；层次；平坦的的基础运用"
      }
    ]
  },
  "office": {
    "pos": "名词",
    "meaning": "办公室；办事处；公职",
    "phonetic": "/ˈɒfɪs/",
    "explanation": "行政办公职场场所。",
    "example": "Step into the modern business office.",
    "exampleCn": "自信从容地迈入现代化的商务写字楼。",
    "family": [
      "office"
    ],
    "collocations": [
      {
        "phrase": "office usage",
        "meaning": "办公室；办事处；公职的基础运用"
      }
    ]
  },
  "door": {
    "pos": "名词",
    "meaning": "门；通道；户",
    "phonetic": "/dɔːr/",
    "explanation": "门户枢纽进出关口。",
    "example": "Open the door to boundless wisdom.",
    "exampleCn": "推开那扇通往无垠智慧的大门。",
    "family": [
      "door"
    ],
    "collocations": [
      {
        "phrase": "door usage",
        "meaning": "门；通道；户的基础运用"
      }
    ]
  },
  "health": {
    "pos": "名词",
    "meaning": "健康；卫生；兴旺",
    "phonetic": "/hɛlθ/",
    "explanation": "身心康泰生机勃勃。",
    "example": "Good health is the foundation of happiness.",
    "exampleCn": "身心健康是一切幸福的源泉与基石。",
    "family": [
      "health"
    ],
    "collocations": [
      {
        "phrase": "health usage",
        "meaning": "健康；卫生；兴旺的基础运用"
      }
    ]
  },
  "person": {
    "pos": "名词",
    "meaning": "人；个人；人物",
    "phonetic": "/ˈpɜːrsən/",
    "explanation": "人类个体独立灵魂。",
    "example": "Be the kind person you wish to meet.",
    "exampleCn": "成为你自己也渴望遇见的那个善良之人。",
    "family": [
      "person"
    ],
    "collocations": [
      {
        "phrase": "person usage",
        "meaning": "人；个人；人物的基础运用"
      }
    ]
  },
  "art": {
    "pos": "名词",
    "meaning": "艺术；技艺；美术",
    "phonetic": "/ɑːrt/",
    "explanation": "审美创造精湛技法。",
    "example": "Art expresses the beauty of the soul.",
    "exampleCn": "艺术生动表达出人类灵魂深处的至美。",
    "family": [
      "art"
    ],
    "collocations": [
      {
        "phrase": "art usage",
        "meaning": "艺术；技艺；美术的基础运用"
      }
    ]
  },
  "history": {
    "pos": "名词",
    "meaning": "历史；历程；史书",
    "phonetic": "/ˈhɪstəri/",
    "explanation": "往昔岁月演化轨迹。",
    "example": "History teaches profound life lessons.",
    "exampleCn": "漫漫历史长河传授着深邃的人生启示。",
    "family": [
      "history"
    ],
    "collocations": [
      {
        "phrase": "history usage",
        "meaning": "历史；历程；史书的基础运用"
      }
    ]
  },
  "party": {
    "pos": "名词",
    "meaning": "聚会；派对；政党",
    "phonetic": "/ˈpɑːrti/",
    "explanation": "欢聚庆典政治组织。",
    "example": "Celebrate at the joyful birthday party.",
    "exampleCn": "在洋溢欢声笑语的生日派对上尽情欢庆。",
    "family": [
      "party"
    ],
    "collocations": [
      {
        "phrase": "party usage",
        "meaning": "聚会；派对；政党的基础运用"
      }
    ]
  },
  "result": {
    "pos": "名词/动词",
    "meaning": "结果；成效；导致",
    "phonetic": "/rɪˈzʌlt/",
    "explanation": "劳作成效终局收获。",
    "example": "Daily effort yields outstanding results.",
    "exampleCn": "日复一日的辛勤耕耘必将结出丰硕成果。",
    "family": [
      "result"
    ],
    "collocations": [
      {
        "phrase": "result usage",
        "meaning": "结果；成效；导致的基础运用"
      }
    ]
  },
  "morning": {
    "pos": "名词",
    "meaning": "早晨；清晨；上午",
    "phonetic": "/ˈmɔːrnɪŋ/",
    "explanation": "破晓拂晓新的一天。",
    "example": "The morning breeze is delightfully refreshing.",
    "exampleCn": "清晨拂面的微风令人感到无比惬意清爽。",
    "family": [
      "morning"
    ],
    "collocations": [
      {
        "phrase": "morning usage",
        "meaning": "早晨；清晨；上午的基础运用"
      }
    ]
  },
  "reason": {
    "pos": "名词/动词",
    "meaning": "理由；原因；理性思考",
    "phonetic": "/ˈriːzən/",
    "explanation": "事理逻辑解释阐明。",
    "example": "There is a profound reason for hope.",
    "exampleCn": "希望的火种之所以不灭，自有一番深刻缘由。",
    "family": [
      "reason"
    ],
    "collocations": [
      {
        "phrase": "reason usage",
        "meaning": "理由；原因；理性思考的基础运用"
      }
    ]
  },
  "research": {
    "pos": "名词/动词",
    "meaning": "研究；钻研；探索",
    "phonetic": "/rɪˈsɜːrtʃ/",
    "explanation": "学术探究科学考证。",
    "example": "Conduct thorough research before writing.",
    "exampleCn": "在提笔成文之前务必开展详尽深入的调查研究。",
    "family": [
      "research"
    ],
    "collocations": [
      {
        "phrase": "research usage",
        "meaning": "研究；钻研；探索的基础运用"
      }
    ]
  },
  "girl": {
    "pos": "名词",
    "meaning": "女孩；姑娘；少女",
    "phonetic": "/ɡɜːrl/",
    "explanation": "年轻女性如花岁月。",
    "example": "The girl solved the puzzle easily.",
    "exampleCn": "那个聪明伶俐的女孩轻而易举解开了难题。",
    "family": [
      "girl"
    ],
    "collocations": [
      {
        "phrase": "girl usage",
        "meaning": "女孩；姑娘；少女的基础运用"
      }
    ]
  },
  "guy": {
    "pos": "名词",
    "meaning": "家伙；伙计；小伙子",
    "phonetic": "/ɡaɪ/",
    "explanation": "口语熟稔称谓小伙。",
    "example": "He is an exceptionally talented guy.",
    "exampleCn": "他是一个才华极其横溢出众的棒小伙。",
    "family": [
      "guy"
    ],
    "collocations": [
      {
        "phrase": "guy usage",
        "meaning": "家伙；伙计；小伙子的基础运用"
      }
    ]
  },
  "moment": {
    "pos": "名词",
    "meaning": "瞬间；片刻；契机",
    "phonetic": "/ˈmoʊmənt/",
    "explanation": "刹那光阴转瞬即逝。",
    "example": "Seize every valuable learning moment.",
    "exampleCn": "紧紧把握住每一次弥足珍贵的求学契机。",
    "family": [
      "moment"
    ],
    "collocations": [
      {
        "phrase": "moment usage",
        "meaning": "瞬间；片刻；契机的基础运用"
      }
    ]
  },
  "air": {
    "pos": "名词/动词",
    "meaning": "空气；大气；通风",
    "phonetic": "/ɛər/",
    "explanation": "无色无味生命之气。",
    "example": "Breathe in the pure mountain air.",
    "exampleCn": "深深呼吸山间清澈纯净的草木空气。",
    "family": [
      "air"
    ],
    "collocations": [
      {
        "phrase": "air usage",
        "meaning": "空气；大气；通风的基础运用"
      }
    ]
  },
  "teacher": {
    "pos": "名词",
    "meaning": "老师；导师；先生",
    "phonetic": "/ˈtiːtʃər/",
    "explanation": "传道受业解惑良师。",
    "example": "A dedicated teacher changes lives.",
    "exampleCn": "一位倾尽心血的良师能彻底改变学子的人生轨迹。",
    "family": [
      "teacher"
    ],
    "collocations": [
      {
        "phrase": "teacher usage",
        "meaning": "老师；导师；先生的基础运用"
      }
    ]
  },
  "force": {
    "pos": "名词/动词",
    "meaning": "力量；武力；强迫",
    "phonetic": "/fɔːrs/",
    "explanation": "强力推力逼迫屈从。",
    "example": "Knowledge is a peaceful mighty force.",
    "exampleCn": "知识是一股润物无声却撼动天地的和平伟力。",
    "family": [
      "force"
    ],
    "collocations": [
      {
        "phrase": "force usage",
        "meaning": "力量；武力；强迫的基础运用"
      }
    ]
  },
  "education": {
    "pos": "名词",
    "meaning": "教育；修养；培植",
    "phonetic": "/ˌɛdʒʊˈkeɪʃən/",
    "explanation": "立德树人开启蒙昧。",
    "example": "Education opens doors of golden promise.",
    "exampleCn": "深厚完善的教育能叩开通往黄金前程的大门。",
    "family": [
      "education"
    ],
    "collocations": [
      {
        "phrase": "education usage",
        "meaning": "教育；修养；培植的基础运用"
      }
    ]
  },
  "good": {
    "pos": "形容词",
    "meaning": "好的；优良的；善的",
    "phonetic": "/ɡʊd/",
    "explanation": "品质优良令人满意。",
    "example": "Have a remarkably good day ahead.",
    "exampleCn": "祝愿你度过一个格外美好舒心的一天。",
    "family": [
      "good"
    ],
    "collocations": [
      {
        "phrase": "good usage",
        "meaning": "好的；优良的；善的的基础运用"
      }
    ]
  },
  "new": {
    "pos": "形容词",
    "meaning": "新的；新鲜的；初次的",
    "phonetic": "/njuː/",
    "explanation": "崭新初创未曾经历。",
    "example": "Welcome to this new learning chapter.",
    "exampleCn": "热烈欢迎翻开这一崭新的学习篇章。",
    "family": [
      "new"
    ],
    "collocations": [
      {
        "phrase": "new usage",
        "meaning": "新的；新鲜的；初次的的基础运用"
      }
    ]
  },
  "first": {
    "pos": "形容词/副词/代词",
    "meaning": "第一的；最初的；首先",
    "phonetic": "/fɜːrst/",
    "explanation": "首要开端次序首位。",
    "example": "Take the first brave step forward.",
    "exampleCn": "勇敢坚定地迈出通向成功的第一步。",
    "family": [
      "first"
    ],
    "collocations": [
      {
        "phrase": "first usage",
        "meaning": "第一的；最初的；首先的基础运用"
      }
    ]
  },
  "last": {
    "pos": "形容词/副词/动词",
    "meaning": "最后的；上一个；持续",
    "phonetic": "/lɑːst/",
    "explanation": "终极收官或延续长久。",
    "example": "This sweet friendship will last forever.",
    "exampleCn": "这份甘醇甜美的挚友深情必将地久天长。",
    "family": [
      "last"
    ],
    "collocations": [
      {
        "phrase": "last usage",
        "meaning": "最后的；上一个；持续的基础运用"
      }
    ]
  },
  "long": {
    "pos": "形容词/副词/动词",
    "meaning": "长的；长久；渴望",
    "phonetic": "/lɔːŋ/",
    "explanation": "长度时间长跨度大。",
    "example": "Long time no see, my dearest friend.",
    "exampleCn": "好久不见了，我最亲爱的朋友。",
    "family": [
      "long"
    ],
    "collocations": [
      {
        "phrase": "long usage",
        "meaning": "长的；长久；渴望的基础运用"
      }
    ]
  },
  "great": {
    "pos": "形容词",
    "meaning": "伟大的；极好的；巨大的",
    "phonetic": "/ɡreɪt/",
    "explanation": "卓越崇高品质拔尖。",
    "example": "You are doing a truly great job.",
    "exampleCn": "你当下的表现真的是可圈可点极其卓越。",
    "family": [
      "great"
    ],
    "collocations": [
      {
        "phrase": "great usage",
        "meaning": "伟大的；极好的；巨大的的基础运用"
      }
    ]
  },
  "little": {
    "pos": "形容词/副词",
    "meaning": "小的；幼小的；很少",
    "phonetic": "/ˈlɪtl/",
    "explanation": "微小稚嫩数量有限。",
    "example": "Little daily habits yield great triumphs.",
    "exampleCn": "点滴细微的日常好习惯能铸就宏大的胜利辉煌。",
    "family": [
      "little"
    ],
    "collocations": [
      {
        "phrase": "little usage",
        "meaning": "小的；幼小的；很少的基础运用"
      }
    ]
  },
  "own": {
    "pos": "形容词/动词",
    "meaning": "自己的；拥有",
    "phonetic": "/oʊn/",
    "explanation": "专属私有独具特色。",
    "example": "Master English with your own unique voice.",
    "exampleCn": "用你独具魅力的独特嗓音精熟驾驭地道英语。",
    "family": [
      "own"
    ],
    "collocations": [
      {
        "phrase": "own usage",
        "meaning": "自己的；拥有的基础运用"
      }
    ]
  },
  "other": {
    "pos": "形容词/代词",
    "meaning": "其他的；另外的",
    "phonetic": "/ˈʌðər/",
    "explanation": "其余群体别开生面。",
    "example": "Always show kindness to other people.",
    "exampleCn": "始终心怀善意体贴关爱身边的其他人。",
    "family": [
      "other"
    ],
    "collocations": [
      {
        "phrase": "other usage",
        "meaning": "其他的；另外的的基础运用"
      }
    ]
  },
  "old": {
    "pos": "形容词",
    "meaning": "年老的；陈旧的；古老的",
    "phonetic": "/oʊld/",
    "explanation": "饱经沧桑岁月洗礼。",
    "example": "Old traditions harbor ancient wisdom.",
    "exampleCn": "古老悠久的传统沉淀着深邃博大的先贤智慧。",
    "family": [
      "old"
    ],
    "collocations": [
      {
        "phrase": "old usage",
        "meaning": "年老的；陈旧的；古老的的基础运用"
      }
    ]
  },
  "big": {
    "pos": "形容词",
    "meaning": "大的；巨大的；重大的",
    "phonetic": "/bɪɡ/",
    "explanation": "体量硕大格局高远。",
    "example": "Dream big and work passionately.",
    "exampleCn": "心怀高远恢弘的宏伟梦想，倾注如火的热情奋力打拼。",
    "family": [
      "big"
    ],
    "collocations": [
      {
        "phrase": "big usage",
        "meaning": "大的；巨大的；重大的的基础运用"
      }
    ]
  },
  "high": {
    "pos": "形容词/副词",
    "meaning": "高的；高级的；高尚的",
    "phonetic": "/haɪ/",
    "explanation": "高度崇高造诣顶尖。",
    "example": "Aim high and never settle for mediocrity.",
    "exampleCn": "立志高远，永不安于碌碌无为的平庸之流。",
    "family": [
      "high"
    ],
    "collocations": [
      {
        "phrase": "high usage",
        "meaning": "高的；高级的；高尚的的基础运用"
      }
    ]
  },
  "different": {
    "pos": "形容词",
    "meaning": "不同的；相异的；各别的",
    "phonetic": "/ˈdɪfrənt/",
    "explanation": "个性迥异别具一格。",
    "example": "Every culture is beautifully different.",
    "exampleCn": "每一种文明文化都在差异中绽放出别样的璀璨。",
    "family": [
      "different"
    ],
    "collocations": [
      {
        "phrase": "different usage",
        "meaning": "不同的；相异的；各别的的基础运用"
      }
    ]
  },
  "small": {
    "pos": "形容词",
    "meaning": "小的；少量的；微弱的",
    "phonetic": "/smɔːl/",
    "explanation": "小巧玲珑纤毫毕现。",
    "example": "Every small effort builds great mastery.",
    "exampleCn": "每一份微小专注的汗水都在筑牢精深造诣的基座。",
    "family": [
      "small"
    ],
    "collocations": [
      {
        "phrase": "small usage",
        "meaning": "小的；少量的；微弱的的基础运用"
      }
    ]
  },
  "large": {
    "pos": "形容词",
    "meaning": "巨大的；大规模的；宽阔的",
    "phonetic": "/lɑːrdʒ/",
    "explanation": "广阔辽阔容量庞大。",
    "example": "A large audience attended the performance.",
    "exampleCn": "庞大可观的热情观众现场出席了这场盛大演出。",
    "family": [
      "large"
    ],
    "collocations": [
      {
        "phrase": "large usage",
        "meaning": "巨大的；大规模的；宽阔的的基础运用"
      }
    ]
  },
  "next": {
    "pos": "形容词/副词",
    "meaning": "下一个；接下来；紧挨着的",
    "phonetic": "/nɛkst/",
    "explanation": "紧随其后次席衔接。",
    "example": "Be prepared for the next exciting milestone.",
    "exampleCn": "为即将到来的下一个激动人心的里程碑做足准备。",
    "family": [
      "next"
    ],
    "collocations": [
      {
        "phrase": "next usage",
        "meaning": "下一个；接下来；紧挨着的的基础运用"
      }
    ]
  },
  "early": {
    "pos": "形容词/副词",
    "meaning": "早的；初期的；早早地",
    "phonetic": "/ˈɜːrli/",
    "explanation": "拂晓先机初期阶段。",
    "example": "The early bird catches the juicy worm.",
    "exampleCn": "早起的鸟儿有虫吃，时不我待占尽先机。",
    "family": [
      "early"
    ],
    "collocations": [
      {
        "phrase": "early usage",
        "meaning": "早的；初期的；早早地的基础运用"
      }
    ]
  },
  "young": {
    "pos": "形容词",
    "meaning": "年轻的；青春的；稚嫩的",
    "phonetic": "/jʌŋ/",
    "explanation": "朝气蓬勃风华正茂。",
    "example": "Stay young in heart and mind forever.",
    "exampleCn": "永葆一颗青春澎湃、热血沸腾的求知初心。",
    "family": [
      "young"
    ],
    "collocations": [
      {
        "phrase": "young usage",
        "meaning": "年轻的；青春的；稚嫩的的基础运用"
      }
    ]
  },
  "important": {
    "pos": "形容词",
    "meaning": "重要的；重大的；有影响力的",
    "phonetic": "/ɪmˈpɔːrtənt/",
    "explanation": "举足轻重不可或缺。",
    "example": "Consistency is far more important than speed.",
    "exampleCn": "持之以恒的定力远比急功近利的速成重要百倍。",
    "family": [
      "important"
    ],
    "collocations": [
      {
        "phrase": "important usage",
        "meaning": "重要的；重大的；有影响力的的基础运用"
      }
    ]
  },
  "few": {
    "pos": "形容词/代词",
    "meaning": "很少；少数；几乎没有",
    "phonetic": "/fjuː/",
    "explanation": "数量稀缺凤毛麟角。",
    "example": "Few obstacles can stop a determined soul.",
    "exampleCn": "这世上几乎没有任何险阻能阻挡一颗坚定决绝的心。",
    "family": [
      "few"
    ],
    "collocations": [
      {
        "phrase": "few usage",
        "meaning": "很少；少数；几乎没有的基础运用"
      }
    ]
  },
  "public": {
    "pos": "形容词/名词",
    "meaning": "公共的；公开的；公众",
    "phonetic": "/ˈpʌblɪk/",
    "explanation": "大众共享毫无遮掩。",
    "example": "Public speaking builds supreme confidence.",
    "exampleCn": "大众公众演讲能淬炼出无可撼动的超凡自信。",
    "family": [
      "public"
    ],
    "collocations": [
      {
        "phrase": "public usage",
        "meaning": "公共的；公开的；公众的基础运用"
      }
    ]
  },
  "bad": {
    "pos": "形容词",
    "meaning": "坏的；糟糕的；劣质的",
    "phonetic": "/bæd/",
    "explanation": "品质低劣令人沮丧。",
    "example": "Turn a bad situation into a triumph.",
    "exampleCn": "将不利困窘的被动局面逆风翻盘扭转为辉煌大捷。",
    "family": [
      "bad"
    ],
    "collocations": [
      {
        "phrase": "bad usage",
        "meaning": "坏的；糟糕的；劣质的的基础运用"
      }
    ]
  },
  "same": {
    "pos": "形容词/代词",
    "meaning": "相同的；同一的",
    "phonetic": "/seɪm/",
    "explanation": "完全一致毫无二致。",
    "example": "We share the exact same learning dream.",
    "exampleCn": "我们心心相印，怀揣着完全相同的求索梦想。",
    "family": [
      "same"
    ],
    "collocations": [
      {
        "phrase": "same usage",
        "meaning": "相同的；同一的的基础运用"
      }
    ]
  },
  "able": {
    "pos": "形容词",
    "meaning": "能够的；有才华的；能干的",
    "phonetic": "/ˈeɪbl/",
    "explanation": "具备能力才干出众。",
    "example": "You are fully able to conquer this sentence.",
    "exampleCn": "你完全具备足够卓越的能力轻松攻克这个长难句。",
    "family": [
      "able"
    ],
    "collocations": [
      {
        "phrase": "able usage",
        "meaning": "能够的；有才华的；能干的的基础运用"
      }
    ]
  },
  "free": {
    "pos": "形容词/动词",
    "meaning": "自由的；免费的；使解脱",
    "phonetic": "/friː/",
    "explanation": "无拘无束自在逍遥。",
    "example": "Feel completely free to express your thoughts.",
    "exampleCn": "请完全自由畅快、无拘无束地抒发表达你的心声。",
    "family": [
      "free"
    ],
    "collocations": [
      {
        "phrase": "free usage",
        "meaning": "自由的；免费的；使解脱的基础运用"
      }
    ]
  },
  "clear": {
    "pos": "形容词/动词",
    "meaning": "清晰的；明澈的；理清",
    "phonetic": "/klɪər/",
    "explanation": "明了清澈一目了然。",
    "example": "Clear pronunciation creates smooth communication.",
    "exampleCn": "清脆地道的标准发音是架起流畅交流的通途。",
    "family": [
      "clear"
    ],
    "collocations": [
      {
        "phrase": "clear usage",
        "meaning": "清晰的；明澈的；理清的基础运用"
      }
    ]
  },
  "real": {
    "pos": "形容词/副词",
    "meaning": "真实的；真诚的；真正的",
    "phonetic": "/rɪəl/",
    "explanation": "客观真实绝无虚假。",
    "example": "Experience real progress with every single line.",
    "exampleCn": "在每一行地道句子的拼写淬炼中体味真正的实质跃升。",
    "family": [
      "real"
    ],
    "collocations": [
      {
        "phrase": "real usage",
        "meaning": "真实的；真诚的；真正的的基础运用"
      }
    ]
  },
  "full": {
    "pos": "形容词",
    "meaning": "满的；充实的；完整的",
    "phonetic": "/fʊl/",
    "explanation": "丰盈充实饱满无缺。",
    "example": "Your heart will be full of proud joy.",
    "exampleCn": "你的心扉定会充盈着无比自豪与欢畅的喜悦。",
    "family": [
      "full"
    ],
    "collocations": [
      {
        "phrase": "full usage",
        "meaning": "满的；充实的；完整的的基础运用"
      }
    ]
  },
  "simple": {
    "pos": "形容词",
    "meaning": "简单的；朴素的；单纯的",
    "phonetic": "/ˈsɪmpl/",
    "explanation": "简明扼要朴素天然。",
    "example": "Keep your daily habits pure and simple.",
    "exampleCn": "让你每天践行的好习惯保持极简纯粹与专注。",
    "family": [
      "simple"
    ],
    "collocations": [
      {
        "phrase": "simple usage",
        "meaning": "简单的；朴素的；单纯的的基础运用"
      }
    ]
  },
  "hard": {
    "pos": "形容词/副词",
    "meaning": "坚硬的；困难的；努力地",
    "phonetic": "/hɑːrd/",
    "explanation": "艰辛困苦拼尽全力。",
    "example": "Work hard, stay humble, and dream grandly.",
    "exampleCn": "脚踏实地埋头苦干，虚怀若谷坚守壮丽梦想。",
    "family": [
      "hard"
    ],
    "collocations": [
      {
        "phrase": "hard usage",
        "meaning": "坚硬的；困难的；努力地的基础运用"
      }
    ]
  },
  "easy": {
    "pos": "形容词/副词",
    "meaning": "容易的；从容的；舒适的",
    "phonetic": "/ˈiːzi/",
    "explanation": "轻而易举从容不迫。",
    "example": "Take it easy and enjoy the practice pace.",
    "exampleCn": "放轻松，慢慢享受并沉浸在舒适的练习节奏中。",
    "family": [
      "easy"
    ],
    "collocations": [
      {
        "phrase": "easy usage",
        "meaning": "容易的；从容的；舒适的的基础运用"
      }
    ]
  },
  "sure": {
    "pos": "形容词/副词",
    "meaning": "确信的；稳妥的；当然",
    "phonetic": "/ʃʊər/",
    "explanation": "笃定无疑必定万全。",
    "example": "I am sure you will achieve massive fluency.",
    "exampleCn": "我坚信你必定能够铸就无比炉火纯青的流利英文。",
    "family": [
      "sure"
    ],
    "collocations": [
      {
        "phrase": "sure usage",
        "meaning": "确信的；稳妥的；当然的基础运用"
      }
    ]
  },
  "safe": {
    "pos": "形容词/名词",
    "meaning": "安全的；保险的；保险柜",
    "phonetic": "/seɪf/",
    "explanation": "平安康宁规避凶险。",
    "example": "Wishing you a safe and memorable trip.",
    "exampleCn": "衷心祝愿你拥有一段平安顺遂且终生难忘的美好旅程。",
    "family": [
      "safe"
    ],
    "collocations": [
      {
        "phrase": "safe usage",
        "meaning": "安全的；保险的；保险柜的基础运用"
      }
    ]
  },
  "true": {
    "pos": "形容词",
    "meaning": "真实的；真诚的；忠实的",
    "phonetic": "/truː/",
    "explanation": "客观真理赤诚如金。",
    "example": "Stay true to your inner calling and values.",
    "exampleCn": "始终坚守你内心深处的真正召唤与崇高价值观。",
    "family": [
      "true"
    ],
    "collocations": [
      {
        "phrase": "true usage",
        "meaning": "真实的；真诚的；忠实的的基础运用"
      }
    ]
  },
  "dark": {
    "pos": "形容词/名词",
    "meaning": "黑暗的；深色的；暗夜",
    "phonetic": "/dɑːrk/",
    "explanation": "光线昏暗深邃暗沉。",
    "example": "Stars shine most brilliantly in the dark.",
    "exampleCn": "群星总是在最漆黑深沉的暗夜里闪烁出最璀璨的光芒。",
    "family": [
      "dark"
    ],
    "collocations": [
      {
        "phrase": "dark usage",
        "meaning": "黑暗的；深色的；暗夜的基础运用"
      }
    ]
  },
  "bright": {
    "pos": "形容词",
    "meaning": "明亮的；聪颖的；欢快的",
    "phonetic": "/braɪt/",
    "explanation": "光辉灿烂才思敏捷。",
    "example": "The future belongs to the bright and brave.",
    "exampleCn": "光辉灿烂的锦绣前程永远属于聪颖睿智且勇毅笃行之人。",
    "family": [
      "bright"
    ],
    "collocations": [
      {
        "phrase": "bright usage",
        "meaning": "明亮的；聪颖的；欢快的的基础运用"
      }
    ]
  },
  "nice": {
    "pos": "形容词",
    "meaning": "美好的；令人愉悦的；友善的",
    "phonetic": "/naɪs/",
    "explanation": "怡然自得和蔼可亲。",
    "example": "It is exceptionally nice to converse with you.",
    "exampleCn": "能与你促膝长谈进行如此愉悦的交流当真是件美事。",
    "family": [
      "nice"
    ],
    "collocations": [
      {
        "phrase": "nice usage",
        "meaning": "美好的；令人愉悦的；友善的的基础运用"
      }
    ]
  },
  "warm": {
    "pos": "形容词/动词",
    "meaning": "温暖的；热情的；使变暖",
    "phonetic": "/wɔːrm/",
    "explanation": "暖意融融体贴入微。",
    "example": "Receive our warmest regards and blessing.",
    "exampleCn": "敬请收下我们最衷心诚挚且充满暖意的深情祝福。",
    "family": [
      "warm"
    ],
    "collocations": [
      {
        "phrase": "warm usage",
        "meaning": "温暖的；热情的；使变暖的基础运用"
      }
    ]
  },
  "cold": {
    "pos": "形容词/名词",
    "meaning": "寒冷的；冷淡的；感冒",
    "phonetic": "/koʊld/",
    "explanation": "冰天雪地严寒凛冽。",
    "example": "Dress warmly against the bitter winter cold.",
    "exampleCn": "多穿些保暖衣裳以抵御凛冬刺骨的凛冽严寒。",
    "family": [
      "cold"
    ],
    "collocations": [
      {
        "phrase": "cold usage",
        "meaning": "寒冷的；冷淡的；感冒的基础运用"
      }
    ]
  },
  "hot": {
    "pos": "形容词",
    "meaning": "炎热的；热烈的；辛辣的",
    "phonetic": "/hɒt/",
    "explanation": "炽热如火激情四溢。",
    "example": "Sip a hot cup of fragrant green tea.",
    "exampleCn": "细细品味一口热气腾腾、香气扑鼻的醇正绿茶。",
    "family": [
      "hot"
    ],
    "collocations": [
      {
        "phrase": "hot usage",
        "meaning": "炎热的；热烈的；辛辣的的基础运用"
      }
    ]
  },
  "cool": {
    "pos": "形容词/动词",
    "meaning": "凉爽的；冷静的；酷炫的",
    "phonetic": "/kuːl/",
    "explanation": "清凉宜人帅气沉着。",
    "example": "Keep your head cool in any heated crisis.",
    "exampleCn": "即便面对任何千钧一发的如火危机也务必保持从容冷静。",
    "family": [
      "cool"
    ],
    "collocations": [
      {
        "phrase": "cool usage",
        "meaning": "凉爽的；冷静的；酷炫的的基础运用"
      }
    ]
  },
  "fast": {
    "pos": "形容词/副词",
    "meaning": "快速的；敏捷的；迅速地",
    "phonetic": "/fɑːst/",
    "explanation": "电光火石迅捷敏锐。",
    "example": "Progress comes fast when you focus fully.",
    "exampleCn": "只要全身心高度专注，飞速的跨越跃迁指日可待。",
    "family": [
      "fast"
    ],
    "collocations": [
      {
        "phrase": "fast usage",
        "meaning": "快速的；敏捷的；迅速地的基础运用"
      }
    ]
  },
  "slow": {
    "pos": "形容词/副词",
    "meaning": "缓慢的；从容的；迟钝的",
    "phonetic": "/sloʊ/",
    "explanation": "不疾不徐稳扎稳打。",
    "example": "Slow and steady progress wins the race.",
    "exampleCn": "不疾不徐、稳扎稳打的沉潜积累终将赢得最后的桂冠。",
    "family": [
      "slow"
    ],
    "collocations": [
      {
        "phrase": "slow usage",
        "meaning": "缓慢的；从容的；迟钝的的基础运用"
      }
    ]
  },
  "heavy": {
    "pos": "形容词",
    "meaning": "沉重的；剧烈的；繁重的",
    "phonetic": "/ˈhɛvi/",
    "explanation": "分量千钧负担极重。",
    "example": "Lift the heavy burden off your shoulders.",
    "exampleCn": "将肩头那沉重如山的千斤重负轻松卸下。",
    "family": [
      "heavy"
    ],
    "collocations": [
      {
        "phrase": "heavy usage",
        "meaning": "沉重的；剧烈的；繁重的的基础运用"
      }
    ]
  },
  "light": {
    "pos": "形容词/名词/动词",
    "meaning": "轻巧的；明亮的；光芒；点燃",
    "phonetic": "/laɪt/",
    "explanation": "轻盈灵巧光芒万丈。",
    "example": "Walk with a light and joy-filled step.",
    "exampleCn": "迈着轻盈从容、洋溢着满满喜悦的欢快步伐。",
    "family": [
      "light"
    ],
    "collocations": [
      {
        "phrase": "light usage",
        "meaning": "轻巧的；明亮的；光芒；点燃的基础运用"
      }
    ]
  },
  "happy": {
    "pos": "形容词",
    "meaning": "快乐的；幸福的；美满的",
    "phonetic": "/ˈhæpi/",
    "explanation": "欣喜若狂幸福安康。",
    "example": "Be happy and grateful for today's gifts.",
    "exampleCn": "对上苍今日所赐予的所有美好心怀无限快乐与感恩。",
    "family": [
      "happy"
    ],
    "collocations": [
      {
        "phrase": "happy usage",
        "meaning": "快乐的；幸福的；美满的的基础运用"
      }
    ]
  },
  "beautiful": {
    "pos": "形容词",
    "meaning": "美丽的；优美的；崇高的",
    "phonetic": "/ˈbjuːtɪfʊl/",
    "explanation": "沉鱼落雁秀色可餐。",
    "example": "English is a richly nuanced and beautiful tongue.",
    "exampleCn": "英语是一门词义幽微婉转且充满至高美感的大美语言。",
    "family": [
      "beautiful"
    ],
    "collocations": [
      {
        "phrase": "beautiful usage",
        "meaning": "美丽的；优美的；崇高的的基础运用"
      }
    ]
  },
  "wonderful": {
    "pos": "形容词",
    "meaning": "极其美妙的；精彩的；神奇的",
    "phonetic": "/ˈwʌndərfʊl/",
    "explanation": "绝妙非凡赞叹称奇。",
    "example": "Have a wonderful, inspiring, and fruitful day.",
    "exampleCn": "祝愿你度过一个无比美妙、深受鼓舞且收获丰厚的一天。",
    "family": [
      "wonderful"
    ],
    "collocations": [
      {
        "phrase": "wonderful usage",
        "meaning": "极其美妙的；精彩的；神奇的的基础运用"
      }
    ]
  },
  "always": {
    "pos": "副词",
    "meaning": "总是；始终；永远",
    "phonetic": "/ˈɔːlweɪz/",
    "explanation": "从无例外一以贯之。",
    "example": "Always believe that something good is about to happen.",
    "exampleCn": "始终坚定相信：有些无比美好的事情正悄然降临。",
    "family": [
      "always"
    ],
    "collocations": [
      {
        "phrase": "always usage",
        "meaning": "总是；始终；永远的基础运用"
      }
    ]
  },
  "never": {
    "pos": "副词",
    "meaning": "从不；决不；永不",
    "phonetic": "/ˈnɛvər/",
    "explanation": "一次没有断然否定。",
    "example": "Never give up on the dreams that define you.",
    "exampleCn": "对于那些塑造你生命本色的崇高梦想，永远绝不言弃。",
    "family": [
      "never"
    ],
    "collocations": [
      {
        "phrase": "never usage",
        "meaning": "从不；决不；永不的基础运用"
      }
    ]
  },
  "often": {
    "pos": "副词",
    "meaning": "经常；常常；屡次",
    "phonetic": "/ˈɒfən/",
    "explanation": "高频重复习以为常。",
    "example": "Review what you learn often to consolidate.",
    "exampleCn": "经常且反复重温所学内容，以求夯实牢固。",
    "family": [
      "often"
    ],
    "collocations": [
      {
        "phrase": "often usage",
        "meaning": "经常；常常；屡次的基础运用"
      }
    ]
  },
  "sometimes": {
    "pos": "副词",
    "meaning": "有时；偶尔；间或",
    "phonetic": "/ˈsʌmtaɪmz/",
    "explanation": "时断时续偶有一见。",
    "example": "Sometimes silence conveys more than spoken words.",
    "exampleCn": "有时候，无声的静默比千言万语更能传递深情厚谊。",
    "family": [
      "sometimes"
    ],
    "collocations": [
      {
        "phrase": "sometimes usage",
        "meaning": "有时；偶尔；间或的基础运用"
      }
    ]
  },
  "usually": {
    "pos": "副词",
    "meaning": "通常；平常；一般而言",
    "phonetic": "/ˈjuːʒuəli/",
    "explanation": "依照惯例十之八九。",
    "example": "He usually begins his day with morning reading.",
    "exampleCn": "他通常习惯以晨曦中的琅琅书声开启崭新的一天。",
    "family": [
      "usually"
    ],
    "collocations": [
      {
        "phrase": "usually usage",
        "meaning": "通常；平常；一般而言的基础运用"
      }
    ]
  },
  "already": {
    "pos": "副词",
    "meaning": "已经；早已；此前",
    "phonetic": "/ɔːlˈrɛdi/",
    "explanation": "既成事实先期达成。",
    "example": "You have already covered an incredible distance.",
    "exampleCn": "回顾过往，你实际上早已走过了令人赞叹的万里长途。",
    "family": [
      "already"
    ],
    "collocations": [
      {
        "phrase": "already usage",
        "meaning": "已经；早已；此前的基础运用"
      }
    ]
  },
  "still": {
    "pos": "副词/形容词",
    "meaning": "仍然；依旧；静止的",
    "phonetic": "/stɪl/",
    "explanation": "延续依旧波澜不惊。",
    "example": "Her passionate dedication is still burning bright.",
    "exampleCn": "她心中那份执着奉献的炽热火光依然在熊熊燃烧。",
    "family": [
      "still"
    ],
    "collocations": [
      {
        "phrase": "still usage",
        "meaning": "仍然；依旧；静止的的基础运用"
      }
    ]
  },
  "just": {
    "pos": "副词/形容词",
    "meaning": "恰好；仅仅；刚才；公正的",
    "phonetic": "/dʒʌst/",
    "explanation": "恰如其分刚正不阿。",
    "example": "You arrived at just the right perfect moment.",
    "exampleCn": "你恰好在这个最完美妥帖的关键时刻准时赶到。",
    "family": [
      "just"
    ],
    "collocations": [
      {
        "phrase": "just usage",
        "meaning": "恰好；仅仅；刚才；公正的的基础运用"
      }
    ]
  },
  "now": {
    "pos": "副词/名词",
    "meaning": "现在；此刻；目前",
    "phonetic": "/naʊ/",
    "explanation": "立足当下只争朝夕。",
    "example": "The power to transform your future is right now.",
    "exampleCn": "重塑并蜕变你辉煌未来的无上伟力，就蕴藏在当下的此刻。",
    "family": [
      "now"
    ],
    "collocations": [
      {
        "phrase": "now usage",
        "meaning": "现在；此刻；目前的基础运用"
      }
    ]
  },
  "then": {
    "pos": "副词/名词",
    "meaning": "然后；那时；那么",
    "phonetic": "/ðɛn/",
    "explanation": "顺承递进忆及当年。",
    "example": "Take a deep breath and then continue.",
    "exampleCn": "深吸一口气，然后接着从容前行。",
    "family": [
      "then"
    ],
    "collocations": [
      {
        "phrase": "then usage",
        "meaning": "然后；那时；那么的基础运用"
      }
    ]
  },
  "here": {
    "pos": "副词/名词",
    "meaning": "这里；在此处；这儿",
    "phonetic": "/hɪər/",
    "explanation": "当前立足空间坐标。",
    "example": "Everything you need to master English is here.",
    "exampleCn": "精熟驾驭卓越英语所需的一切要素，此刻尽皆汇聚于此。",
    "family": [
      "here"
    ],
    "collocations": [
      {
        "phrase": "here usage",
        "meaning": "这里；在此处；这儿的基础运用"
      }
    ]
  },
  "there": {
    "pos": "副词/代词",
    "meaning": "那里；在彼处；存在",
    "phonetic": "/ðɛər/",
    "explanation": "彼岸远方存在句型。",
    "example": "There is a world of wonder waiting for you.",
    "exampleCn": "有一个充满无垠奇迹的宏大世界正翘首期盼着你的探索。",
    "family": [
      "there"
    ],
    "collocations": [
      {
        "phrase": "there usage",
        "meaning": "那里；在彼处；存在的基础运用"
      }
    ]
  },
  "very": {
    "pos": "副词/形容词",
    "meaning": "非常；极其；恰好的",
    "phonetic": "/ˈvɛri/",
    "explanation": "强化程度恰如其分。",
    "example": "Your hard-earned progress is very noticeable.",
    "exampleCn": "你历经刻苦淬炼所取得的实质跃升极其有目共睹。",
    "family": [
      "very"
    ],
    "collocations": [
      {
        "phrase": "very usage",
        "meaning": "非常；极其；恰好的的基础运用"
      }
    ]
  },
  "really": {
    "pos": "副词",
    "meaning": "真正地；确实；真切地",
    "phonetic": "/ˈriːəli/",
    "explanation": "真诚证实毫无虚妄。",
    "example": "I really appreciate your profound dedication.",
    "exampleCn": "我发自肺腑深深感激你所展现出的高度专注与奉献。",
    "family": [
      "really"
    ],
    "collocations": [
      {
        "phrase": "really usage",
        "meaning": "真正地；确实；真切地的基础运用"
      }
    ]
  },
  "also": {
    "pos": "副词",
    "meaning": "也；同样；而且",
    "phonetic": "/ˈɔːlsoʊ/",
    "explanation": "并列增添锦上添花。",
    "example": "Reading aloud also strengthens spoken confidence.",
    "exampleCn": "坚持大声朗读同样能够极大地强化口语表达的笃定自信。",
    "family": [
      "also"
    ],
    "collocations": [
      {
        "phrase": "also usage",
        "meaning": "也；同样；而且的基础运用"
      }
    ]
  },
  "too": {
    "pos": "副词",
    "meaning": "太；过于；也",
    "phonetic": "/tuː/",
    "explanation": "过量过度抑或亦然。",
    "example": "It is never too late to reinvent yourself.",
    "exampleCn": "重塑并绽放一个崭新的自我，任何时候都绝不算晚。",
    "family": [
      "too"
    ],
    "collocations": [
      {
        "phrase": "too usage",
        "meaning": "太；过于；也的基础运用"
      }
    ]
  },
  "well": {
    "pos": "副词/形容词/感叹词",
    "meaning": "好地；健康的；嗯",
    "phonetic": "/wɛl/",
    "explanation": "得心应手身心安康。",
    "example": "Speak well, write well, and live with honor.",
    "exampleCn": "把话说得得体，把字写得考究，活出尊严与体面。",
    "family": [
      "well"
    ],
    "collocations": [
      {
        "phrase": "well usage",
        "meaning": "好地；健康的；嗯的基础运用"
      }
    ]
  },
  "airport": {
    "pos": "名词",
    "meaning": "机场；航空站",
    "phonetic": "/ˈɛərpɔːrt/",
    "explanation": "民航飞机起降与旅客集散场所。",
    "example": "We arrived at the international airport early.",
    "exampleCn": "我们早早抵达了国际机场。",
    "family": [
      "airport"
    ],
    "collocations": [
      {
        "phrase": "airport usage",
        "meaning": "机场；航空站的地道表达"
      }
    ]
  },
  "hotel": {
    "pos": "名词",
    "meaning": "酒店；宾馆",
    "phonetic": "/hoʊˈtɛl/",
    "explanation": "为旅客提供住宿餐饮的商务场所。",
    "example": "The boutique hotel has a lovely sea view.",
    "exampleCn": "这家精品酒店拥有绝美的海景。",
    "family": [
      "hotel"
    ],
    "collocations": [
      {
        "phrase": "hotel usage",
        "meaning": "酒店；宾馆的地道表达"
      }
    ]
  },
  "restaurant": {
    "pos": "名词",
    "meaning": "餐厅；饭店",
    "phonetic": "/ˈrɛstərɒnt/",
    "explanation": "提供正餐美食的就餐场所。",
    "example": "Let us reserve a table at the Italian restaurant.",
    "exampleCn": "让我们在那家意大利餐厅预订一张餐桌吧。",
    "family": [
      "restaurant"
    ],
    "collocations": [
      {
        "phrase": "restaurant usage",
        "meaning": "餐厅；饭店的地道表达"
      }
    ]
  },
  "flight": {
    "pos": "名词",
    "meaning": "航班；飞行",
    "phonetic": "/flaɪt/",
    "explanation": "空中客机航次航程。",
    "example": "Our direct flight departs in two hours.",
    "exampleCn": "我们的直飞航班两小时后起飞。",
    "family": [
      "flight"
    ],
    "collocations": [
      {
        "phrase": "flight usage",
        "meaning": "航班；飞行的地道表达"
      }
    ]
  },
  "ticket": {
    "pos": "名词",
    "meaning": "车票；门票；机票",
    "phonetic": "/ˈtɪkɪt/",
    "explanation": "搭乘交通或观看演出的凭证。",
    "example": "Show your boarding ticket at the gate.",
    "exampleCn": "请在登机口出示您的登机牌。",
    "family": [
      "ticket"
    ],
    "collocations": [
      {
        "phrase": "ticket usage",
        "meaning": "车票；门票；机票的地道表达"
      }
    ]
  },
  "menu": {
    "pos": "名词",
    "meaning": "菜单；选项单",
    "phonetic": "/ˈmɛnjuː/",
    "explanation": "餐饮菜品名目清单。",
    "example": "May I take a look at the dinner menu?",
    "exampleCn": "我可以看一下晚餐菜单吗？",
    "family": [
      "menu"
    ],
    "collocations": [
      {
        "phrase": "menu usage",
        "meaning": "菜单；选项单的地道表达"
      }
    ]
  },
  "coffee": {
    "pos": "名词",
    "meaning": "咖啡；咖啡豆",
    "phonetic": "/ˈkɒfi/",
    "explanation": "香气浓郁的提神热饮。",
    "example": "A hot cup of coffee wakes up the mind.",
    "exampleCn": "一杯滚烫的热咖啡能唤醒清晨的思维。",
    "family": [
      "coffee"
    ],
    "collocations": [
      {
        "phrase": "coffee usage",
        "meaning": "咖啡；咖啡豆的地道表达"
      }
    ]
  },
  "tea": {
    "pos": "名词",
    "meaning": "茶；茶叶",
    "phonetic": "/tiː/",
    "explanation": "甘醇清香的传统饮品。",
    "example": "Enjoying a fragrant cup of jasmine tea.",
    "exampleCn": "细细品尝一杯清香四溢的茉莉花茶。",
    "family": [
      "tea"
    ],
    "collocations": [
      {
        "phrase": "tea usage",
        "meaning": "茶；茶叶的地道表达"
      }
    ]
  },
  "music": {
    "pos": "名词",
    "meaning": "音乐；乐曲",
    "phonetic": "/ˈmjuːzɪk/",
    "explanation": "声音艺术与情感律动。",
    "example": "Music transcends all cultural boundaries.",
    "exampleCn": "音乐跨越一切文化的隔阂与边界。",
    "family": [
      "music"
    ],
    "collocations": [
      {
        "phrase": "music usage",
        "meaning": "音乐；乐曲的地道表达"
      }
    ]
  },
  "song": {
    "pos": "名词",
    "meaning": "歌曲；歌谣",
    "phonetic": "/sɒŋ/",
    "explanation": "配乐演唱的诗词旋律。",
    "example": "Her heartfelt song moved the crowd to tears.",
    "exampleCn": "她发自肺腑的动人歌声令全场观众热泪盈眶。",
    "family": [
      "song"
    ],
    "collocations": [
      {
        "phrase": "song usage",
        "meaning": "歌曲；歌谣的地道表达"
      }
    ]
  },
  "movie": {
    "pos": "名词",
    "meaning": "电影；影片",
    "phonetic": "/ˈmuːvi/",
    "explanation": "光影胶片叙事艺术。",
    "example": "Watching a classic movie on weekend nights.",
    "exampleCn": "在周末的夜晚静静欣赏一部经典电影。",
    "family": [
      "movie"
    ],
    "collocations": [
      {
        "phrase": "movie usage",
        "meaning": "电影；影片的地道表达"
      }
    ]
  },
  "film": {
    "pos": "名词/动词",
    "meaning": "电影；胶片；拍摄",
    "phonetic": "/fɪlm/",
    "explanation": "银幕艺术或电影摄制。",
    "example": "This independent film won international awards.",
    "exampleCn": "这部独立电影斩获了多项国际大奖。",
    "family": [
      "film"
    ],
    "collocations": [
      {
        "phrase": "film usage",
        "meaning": "电影；胶片；拍摄的地道表达"
      }
    ]
  },
  "scene": {
    "pos": "名词",
    "meaning": "场景；场面；景色",
    "phonetic": "/siːn/",
    "explanation": "电影幕次或生活画面。",
    "example": "The final farewell scene was deeply touching.",
    "exampleCn": "电影最终的依依惜别场景感人至深。",
    "family": [
      "scene"
    ],
    "collocations": [
      {
        "phrase": "scene usage",
        "meaning": "场景；场面；景色的地道表达"
      }
    ]
  },
  "character": {
    "pos": "名词",
    "meaning": "角色；性格；汉字",
    "phonetic": "/ˈkærəktər/",
    "explanation": "戏剧人物或道德人品。",
    "example": "She played a courageous character in the drama.",
    "exampleCn": "她在该剧中饰演了一位智勇双全的坚强角色。",
    "family": [
      "character"
    ],
    "collocations": [
      {
        "phrase": "character usage",
        "meaning": "角色；性格；汉字的地道表达"
      }
    ]
  },
  "grammar": {
    "pos": "名词",
    "meaning": "语法；文法",
    "phonetic": "/ˈɡræmər/",
    "explanation": "语言组织与结构法则。",
    "example": "Clear grammar gives precision to your sentences.",
    "exampleCn": "严谨清晰的语法赋予句子无与伦比的精准度。",
    "family": [
      "grammar"
    ],
    "collocations": [
      {
        "phrase": "grammar usage",
        "meaning": "语法；文法的地道表达"
      }
    ]
  },
  "vocabulary": {
    "pos": "名词",
    "meaning": "词汇；词汇量",
    "phonetic": "/vəˈkæbjʊləri/",
    "explanation": "掌握的单词总量体系。",
    "example": "Expand your vocabulary through context reading.",
    "exampleCn": "在语境阅读中持续拓宽你的核心词汇量。",
    "family": [
      "vocabulary"
    ],
    "collocations": [
      {
        "phrase": "vocabulary usage",
        "meaning": "词汇；词汇量的地道表达"
      }
    ]
  },
  "phrase": {
    "pos": "名词/动词",
    "meaning": "短语；习语；措辞",
    "phonetic": "/freɪz/",
    "explanation": "词组固定搭配表达。",
    "example": "Mastering native phrases makes you sound natural.",
    "exampleCn": "精熟掌握母语短语会让你说话极为自然地道。",
    "family": [
      "phrase"
    ],
    "collocations": [
      {
        "phrase": "phrase usage",
        "meaning": "短语；习语；措辞的地道表达"
      }
    ]
  },
  "sentence": {
    "pos": "名词/动词",
    "meaning": "句子；宣判",
    "phonetic": "/ˈsɛntəns/",
    "explanation": "表达完整意思的语言单位。",
    "example": "Spell every sentence with focus and accuracy.",
    "exampleCn": "聚精会神、精准无误地拼写每一个句子。",
    "family": [
      "sentence"
    ],
    "collocations": [
      {
        "phrase": "sentence usage",
        "meaning": "句子；宣判的地道表达"
      }
    ]
  },
  "practice": {
    "pos": "名词/动词",
    "meaning": "练习；实践；惯例",
    "phonetic": "/ˈpræktɪs/",
    "explanation": "反复实操操练巩固。",
    "example": "Daily practice turns clumsy into graceful.",
    "exampleCn": "日复一日的练习能让生涩笨拙化作行云流水。",
    "family": [
      "practice"
    ],
    "collocations": [
      {
        "phrase": "practice usage",
        "meaning": "练习；实践；惯例的地道表达"
      }
    ]
  },
  "skill": {
    "pos": "名词",
    "meaning": "技能；手艺；熟练",
    "phonetic": "/skɪl/",
    "explanation": "后天习得的精湛本领。",
    "example": "Spelling is an invaluable language skill.",
    "exampleCn": "精准拼写是一项弥足珍贵的核心语言技能。",
    "family": [
      "skill"
    ],
    "collocations": [
      {
        "phrase": "skill usage",
        "meaning": "技能；手艺；熟练的地道表达"
      }
    ]
  },
  "confidence": {
    "pos": "名词",
    "meaning": "自信；信心；信任",
    "phonetic": "/ˈkɒnfɪdəns/",
    "explanation": "对自己能力的笃定信任。",
    "example": "Speak with boundless confidence and clarity.",
    "exampleCn": "以无可撼动的自信与明晰清晰自如地表达。",
    "family": [
      "confidence"
    ],
    "collocations": [
      {
        "phrase": "confidence usage",
        "meaning": "自信；信心；信任的地道表达"
      }
    ]
  },
  "fluency": {
    "pos": "名词",
    "meaning": "流利度；流畅",
    "phonetic": "/ˈfluːənsi/",
    "explanation": "表达如行云流水般纯熟。",
    "example": "Achieve effortless spoken fluency with grit.",
    "exampleCn": "以笃定坚毅的恒心练就一口地道流利的口语。",
    "family": [
      "fluency"
    ],
    "collocations": [
      {
        "phrase": "fluency usage",
        "meaning": "流利度；流畅的地道表达"
      }
    ]
  },
  "master": {
    "pos": "名词/动词",
    "meaning": "大师；精通；掌控",
    "phonetic": "/ˈmæstər/",
    "explanation": "登峰造极的大师或全面掌握。",
    "example": "Become a true master of English spelling.",
    "exampleCn": "成为一名名副其实的英语拼写大师。",
    "family": [
      "master"
    ],
    "collocations": [
      {
        "phrase": "master usage",
        "meaning": "大师；精通；掌控的地道表达"
      }
    ]
  },
  "journey": {
    "pos": "名词/动词",
    "meaning": "旅程；旅行；航程",
    "phonetic": "/ˈdʒɜːrni/",
    "explanation": "漫长跋涉求索历程。",
    "example": "Enjoy every step of this learning journey.",
    "exampleCn": "尽情沉浸并享受求学求索旅途中的每一步。",
    "family": [
      "journey"
    ],
    "collocations": [
      {
        "phrase": "journey usage",
        "meaning": "旅程；旅行；航程的地道表达"
      }
    ]
  },
  "future": {
    "pos": "名词/形容词",
    "meaning": "未来；前途；将来的",
    "phonetic": "/ˈfjuːtʃər/",
    "explanation": "无限可能的锦绣明日。",
    "example": "Your dedicated efforts today build your future.",
    "exampleCn": "你今天所倾注的全部心血都在筑造光芒万丈的未来。",
    "family": [
      "future"
    ],
    "collocations": [
      {
        "phrase": "future usage",
        "meaning": "未来；前途；将来的的地道表达"
      }
    ]
  }
};
