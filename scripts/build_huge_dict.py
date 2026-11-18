# -*- coding: utf-8 -*-
"""
大词典数据生成器：
整合最全核心英语词典，支持精准词性、中文义、音标、全中文语法解析、例句与短语
"""
import os
import json

def get_base_dict():
    # 常用功能词与超高频核心词集合
    d = {}
    
    # 问候与感叹
    d["hey"] = {"pos": "感叹词", "meaning": "嘿；你好", "phonetic": "/heɪ/", "explanation": "非正式打招呼用语，语气亲近自然。", "example": "Hey, long time no see!", "exampleCn": "嘿，好久不见！"}
    d["hello"] = {"pos": "感叹词", "meaning": "你好；喂", "phonetic": "/həˈloʊ/", "explanation": "最普遍通用的问候语。", "example": "Hello, how are you today?", "exampleCn": "你好，今天怎么样？"}
    d["hi"] = {"pos": "感叹词", "meaning": "嗨；你好", "phonetic": "/haɪ/", "explanation": "熟人间的日常问候。", "example": "Hi there, nice to meet you.", "exampleCn": "嗨，很高兴见到你。"}
    d["welcome"] = {"pos": "动词/形容词", "meaning": "欢迎；受欢迎的", "phonetic": "/ˈwɛlkəm/", "explanation": "表示欢迎或客气回应。", "example": "Welcome to our English study group.", "exampleCn": "欢迎加入我们的英语学习小组。"}
    d["please"] = {"pos": "副词/动词", "meaning": "请；使高兴", "phonetic": "/pliːz/", "explanation": "祈使句中的礼貌用语。", "example": "Please take a comfortable seat.", "exampleCn": "请挑个舒适的位置坐下。"}
    d["thank"] = {"pos": "动词", "meaning": "感谢；道谢", "phonetic": "/θæŋk/", "explanation": "表达感激之情。", "example": "Thank you for your generous help.", "exampleCn": "谢谢你的慷慨帮助。"}
    d["thanks"] = {"pos": "名词/感叹词", "meaning": "感谢；多谢", "phonetic": "/θæŋks/", "explanation": "口语常用致谢表达。", "example": "Thanks a lot for everything.", "exampleCn": "多谢你所做的一切。"}
    d["sorry"] = {"pos": "形容词", "meaning": "对不起的；遗憾的", "phonetic": "/ˈsɒri/", "explanation": "表达歉意或同情。", "example": "I am so sorry for being late.", "exampleCn": "非常抱歉我迟到了。"}
    d["excuse"] = {"pos": "动词/名词", "meaning": "原谅；借口", "phonetic": "/ɪkˈskjuːz/", "explanation": "常用固定搭配 excuse me 用于客气搭话。", "example": "Excuse me, where is the station?", "exampleCn": "打扰一下，请问车站在哪里？"}
    d["bye"] = {"pos": "感叹词", "meaning": "再见", "phonetic": "/baɪ/", "explanation": "道别口语用语。", "example": "Bye, have a wonderful weekend!", "exampleCn": "再见，祝你周末愉快！"}
    d["goodbye"] = {"pos": "感叹词/名词", "meaning": "再见；告别", "phonetic": "/ˌɡʊdˈbaɪ/", "explanation": "正式或日常道别表达。", "example": "They said goodbye at the airport.", "exampleCn": "他们在机场依依惜别。"}
    d["yes"] = {"pos": "副词/感叹词", "meaning": "是的；对", "phonetic": "/jɛs/", "explanation": "肯定回答。", "example": "Yes, I completely agree with you.", "exampleCn": "是的，我完全赞同你的看法。"}
    d["no"] = {"pos": "限定词/副词", "meaning": "没有；不", "phonetic": "/noʊ/", "explanation": "否定词，作限定词或否定答复。", "example": "There is no doubt about it.", "exampleCn": "对此毫无疑问。"}
    d["oh"] = {"pos": "感叹词", "meaning": "哦；哎呀", "phonetic": "/oʊ/", "explanation": "表示惊讶、领悟或情绪变化。", "example": "Oh, I see what you mean.", "exampleCn": "哦，我明白你的意思了。"}
    d["wow"] = {"pos": "感叹词", "meaning": "哇；呀", "phonetic": "/waʊ/", "explanation": "表示惊叹或赞赏。", "example": "Wow, this view is breathtaking!", "exampleCn": "哇，这里的风景真是美得令人屏息！"}
    
    # 常用代词
    d["i"] = {"pos": "代词", "meaning": "我 (第一人称主格)", "phonetic": "/aɪ/", "explanation": "说话者自称的主格形式。", "example": "I love practicing English every day.", "exampleCn": "我热爱每天练习英语。"}
    d["you"] = {"pos": "代词", "meaning": "你；你们 (第二人称)", "phonetic": "/juː/", "explanation": "对话受话者代词，单复数同形。", "example": "You can achieve anything you set your mind to.", "exampleCn": "只要下定决心，你能做到任何事。"}
    d["he"] = {"pos": "代词", "meaning": "他 (第三人称阳性主格)", "phonetic": "/hiː/", "explanation": "指代男性第三人称主格。", "example": "He works diligently toward his dream.", "exampleCn": "他为了自己的梦想勤奋工作。"}
    d["she"] = {"pos": "代词", "meaning": "她 (第三人称阴性主格)", "phonetic": "/ʃiː/", "explanation": "指代女性第三人称主格。", "example": "She is an extraordinary teacher.", "exampleCn": "她是一位极其出色的老师。"}
    d["it"] = {"pos": "代词", "meaning": "它；这 (中性代词)", "phonetic": "/ɪt/", "explanation": "指代事物、动物、天气或作形式主语。", "example": "It is important to stay positive.", "exampleCn": "保持乐观的心态非常重要。"}
    d["we"] = {"pos": "代词", "meaning": "我们 (第一人称复数主格)", "phonetic": "/wiː/", "explanation": "第一人称复数主格。", "example": "Together we can make a difference.", "exampleCn": "携手并进，我们能够创造改变。"}
    d["they"] = {"pos": "代词", "meaning": "他们；她们；它们", "phonetic": "/ðeɪ/", "explanation": "第三人称复数主格。", "example": "They reached their destination safely.", "exampleCn": "他们平安抵达了目的地。"}
    d["me"] = {"pos": "代词", "meaning": "我 (宾格)", "phonetic": "/miː/", "explanation": "作动词或介词的宾语。", "example": "Let me help you with this heavy bag.", "exampleCn": "让我帮你拿这个沉重的包吧。"}
    d["him"] = {"pos": "代词", "meaning": "他 (宾格)", "phonetic": "/hɪm/", "explanation": "作动词或介词的宾语。", "example": "I saw him at the conference yesterday.", "exampleCn": "我昨天在大会上见到了他。"}
    d["her"] = {"pos": "代词/形容词", "meaning": "她 (宾格)；她的 (物主代词)", "phonetic": "/hɜːr/", "explanation": "女性宾格代词或形容词性物主代词。", "example": "Her dedication inspired everyone.", "exampleCn": "她的奉献精神鼓舞了每一个人。"}
    d["us"] = {"pos": "代词", "meaning": "我们 (宾格)", "phonetic": "/ʌs/", "explanation": "第一人称复数宾格。", "example": "Join us for dinner tonight.", "exampleCn": "今晚加入我们一起共进晚餐吧。"}
    d["them"] = {"pos": "代词", "meaning": "他们/她们/它们 (宾格)", "phonetic": "/ðɛm/", "explanation": "第三人称复数宾格。", "example": "Encourage them to do their best.", "exampleCn": "鼓励他们竭尽全力。"}
    d["my"] = {"pos": "限定词/代词", "meaning": "我的 (物主限定词)", "phonetic": "/maɪ/", "explanation": "形容词性物主代词，后接名词。", "example": "My goal is to speak fluent English.", "exampleCn": "我的目标是说一口流利的英语。"}
    d["your"] = {"pos": "限定词/代词", "meaning": "你的；你们的", "phonetic": "/jɔːr/", "explanation": "形容词性物主代词。", "example": "Your hard work will pay off.", "exampleCn": "你的辛勤努力终将有所回报。"}
    d["his"] = {"pos": "限定词/代词", "meaning": "他的", "phonetic": "/hɪz/", "explanation": "物主限定词或名词性物主代词。", "example": "His pronunciation is very natural.", "exampleCn": "他的发音非常自然地道。"}
    d["its"] = {"pos": "限定词", "meaning": "它的", "phonetic": "/ɪts/", "explanation": "物主限定词，指代事物的归属。", "example": "The company celebrated its tenth anniversary.", "exampleCn": "这家公司庆祝了成立十周年。"}
    d["our"] = {"pos": "限定词", "meaning": "我们的", "phonetic": "/ˈaʊər/", "explanation": "形容词性物主代词。", "example": "Our team won the championship.", "exampleCn": "我们团队赢得了冠军。"}
    d["their"] = {"pos": "限定词", "meaning": "他们的；她们的；它们的", "phonetic": "/ðɛər/", "explanation": "形容词性物主代词。", "example": "Their ideas are highly innovative.", "exampleCn": "他们的创意非常具有创新性。"}
    d["this"] = {"pos": "指示代词/限定词", "meaning": "这；这个", "phonetic": "/ðɪs/", "explanation": "指代较近的人、事或概念。", "example": "This is a wonderful opportunity.", "exampleCn": "这是一个极好的机会。"}
    d["that"] = {"pos": "指示代词/连词", "meaning": "那；那个；从句引导词", "phonetic": "/ðæt/", "explanation": "指代较远对象，或引导名词性/定语从句。", "example": "I believe that practice makes perfect.", "exampleCn": "我相信熟能生巧。"}
    d["these"] = {"pos": "指示代词", "meaning": "这些", "phonetic": "/ðiːz/", "explanation": "this 的复数形式。", "example": "These books are very helpful.", "exampleCn": "这些书非常有帮助。"}
    d["those"] = {"pos": "指示代词", "meaning": "那些", "phonetic": "/ðoʊz/", "explanation": "that 的复数形式。", "example": "Those memories will last forever.", "exampleCn": "那些回忆将永远留存。"}
    d["what"] = {"pos": "疑问代词", "meaning": "什么；多么", "phonetic": "/wɒt/", "explanation": "询问事物或感叹句引导词。", "example": "What do you want to accomplish today?", "exampleCn": "你今天想要完成什么？"}
    d["which"] = {"pos": "疑问代词/关系代词", "meaning": "哪一个；哪一些", "phonetic": "/wɪtʃ/", "explanation": "在特定范围内做选择，或引导定语从句。", "example": "Which option do you prefer?", "exampleCn": "你更倾向于哪一个选择？"}
    d["who"] = {"pos": "疑问代词/关系代词", "meaning": "谁", "phonetic": "/huː/", "explanation": "询问人或引导定语从句。", "example": "Who is coming to the presentation?", "exampleCn": "谁会来参加这次汇报？"}
    d["whom"] = {"pos": "代词", "meaning": "谁 (宾格)", "phonetic": "/huːm/", "explanation": "正式语体中作为介词或动词宾语。", "example": "To whom it may concern.", "exampleCn": "致相关人士（敬启者）。"}
    d["whose"] = {"pos": "代词", "meaning": "谁的", "phonetic": "/huːz/", "explanation": "询问所有关系。", "example": "Whose notebook is this on the desk?", "exampleCn": "课桌上的这本笔记本是谁的？"}
    d["where"] = {"pos": "疑问副词/关系副词", "meaning": "在哪里；何处", "phonetic": "/wɛər/", "explanation": "询问地点或引导地点从句。", "example": "Where would you like to travel next?", "exampleCn": "接下来你希望去哪里旅行？"}
    d["when"] = {"pos": "疑问副词/从属连词", "meaning": "何时；当...的时候", "phonetic": "/wɛn/", "explanation": "询问时间或引导时间状语从句。", "example": "When will the next flight depart?", "exampleCn": "下一趟航班什么时候起飞？"}
    d["why"] = {"pos": "疑问副词", "meaning": "为什么；何以", "phonetic": "/waɪ/", "explanation": "询问原因。", "example": "Why is this method so effective?", "exampleCn": "为什么这种方法如此有效？"}
    d["how"] = {"pos": "疑问副词", "meaning": "如何；怎样；多么", "phonetic": "/haʊ/", "explanation": "询问方式、程度、数量或健康状态。", "example": "How have you been lately?", "exampleCn": "你最近过得如何？"}
    
    # 常用介词与连词
    d["in"] = {"pos": "介词/副词", "meaning": "在...里面；在...期间", "phonetic": "/ɪn/", "explanation": "表示空间内部、时间范围或处于某种状态。", "example": "She lives in a vibrant city.", "exampleCn": "她居住在一座充满活力的城市中。"}
    d["on"] = {"pos": "介词/副词", "meaning": "在...上面；关于；处于...状态", "phonetic": "/ɒn/", "explanation": "表示表面接触、具体日期或作为副词表示进行中。", "example": "The book is on the study desk.", "exampleCn": "书在书桌上面。"}
    d["at"] = {"pos": "介词", "meaning": "在(某地点/某时刻)；向", "phonetic": "/æt/", "explanation": "精确的具体地点、特定时刻或目标方向。", "example": "We met at eight o'clock this morning.", "exampleCn": "我们今天早上八点碰了面。"}
    d["to"] = {"pos": "介词/不定式符号", "meaning": "到；向；朝；动词不定式", "phonetic": "/tuː/", "explanation": "方向与目的地介词，或置于动词原形前构成不定式。", "example": "It is a pleasure to meet you.", "exampleCn": "很高兴认识你。"}
    d["for"] = {"pos": "介词/连词", "meaning": "为了；给；持续(时间)", "phonetic": "/fɔːr/", "explanation": "表目的、受惠对象、理由或时间跨度。", "example": "Thank you for your valuable feedback.", "exampleCn": "感谢你宝贵的反馈意见。"}
    d["with"] = {"pos": "介词", "meaning": "和...一起；用；伴随", "phonetic": "/wɪð/", "explanation": "伴随状态、工具手段或特征。", "example": "Walk with confidence and purpose.", "exampleCn": "怀揣自信与目标坚定前行。"}
    d["by"] = {"pos": "介词/副词", "meaning": "通过；被；在...旁边；不迟于", "phonetic": "/baɪ/", "explanation": "表示方式手段、被动施动者、位置或截止时间。", "example": "Success comes by persistent effort.", "exampleCn": "成功源自持之以恒的努力。"}
    d["from"] = {"pos": "介词", "meaning": "来自；从...起；出于", "phonetic": "/frʌm/", "explanation": "起点、出处、来源或两地相隔距离。", "example": "Where did you come from?", "exampleCn": "你从哪里来？"}
    d["about"] = {"pos": "介词/副词", "meaning": "关于；大约；四处", "phonetic": "/əˈbaʊt/", "explanation": "涉及主题，或修饰数量表示大概。", "example": "What do you think about this plan?", "exampleCn": "你对这个方案怎么看？"}
    d["into"] = {"pos": "介词", "meaning": "进入...内部；转变成", "phonetic": "/ˈɪntuː/", "explanation": "动态进入内部或状态发生转化。", "example": "Translate your ideas into meaningful actions.", "exampleCn": "将你的想法转化为富有意义的行动。"}
    d["through"] = {"pos": "介词/副词", "meaning": "穿过；通过；自始至终", "phonetic": "/θruː/", "explanation": "空间贯穿、时间历程或手段途径。", "example": "We learned a great deal through experience.", "exampleCn": "我们通过实践学到了许多东西。"}
    d["over"] = {"pos": "介词/副词", "meaning": "在...上方；越过；结束", "phonetic": "/ˈoʊvər/", "explanation": "垂直上方、跨越或表示完了结束。", "example": "The rainbow spread over the entire horizon.", "exampleCn": "彩虹横跨了整片天际。"}
    d["under"] = {"pos": "介词", "meaning": "在...下面；在...管理下", "phonetic": "/ˈʌndər/", "explanation": "垂直下方或处于某种压力/控制中。", "example": "Stay calm even under high pressure.", "exampleCn": "即便身处高压之下也要保持沉着。"}
    d["between"] = {"pos": "介词", "meaning": "在(两者)之间", "phonetic": "/bɪˈtwiːn/", "explanation": "两者之间的位置、时间或关系。", "example": "Keep this secret strictly between us.", "exampleCn": "严格在我们两人之间保守这个秘密。"}
    d["among"] = {"pos": "介词", "meaning": "在(三者以上)之中", "phonetic": "/əˈmʌŋ/", "explanation": "多者群体包围之中。", "example": "He is very popular among his peers.", "exampleCn": "他在同龄人中极受欢迎。"}
    d["without"] = {"pos": "介词", "meaning": "没有；无", "phonetic": "/wɪðˈaʊt/", "explanation": "否定伴随状态。", "example": "Nothing is impossible without hard work.", "exampleCn": "不付出辛劳便一事无成。"}
    d["against"] = {"pos": "介词", "meaning": "反对；依靠；违背", "phonetic": "/əˈɡɛnst/", "explanation": "对抗、逆向或紧贴倚靠。", "example": "Protect your skin against strong sunlight.", "exampleCn": "保护皮肤免受强烈日晒。"}
    d["during"] = {"pos": "介词", "meaning": "在...期间", "phonetic": "/ˈdjʊərɪŋ/", "explanation": "时间过程之中。", "example": "Take detailed notes during the lecture.", "exampleCn": "在讲座期间做好详尽笔记。"}
    d["after"] = {"pos": "介词/连词", "meaning": "在...之后", "phonetic": "/ˈɑːftər/", "explanation": "时间或空间顺序之后。", "example": "Let us review after class.", "exampleCn": "让我们下课后再行复习。"}
    d["before"] = {"pos": "介词/连词/副词", "meaning": "在...之前；以前", "phonetic": "/bɪˈfɔːr/", "explanation": "时间先于或面对...", "example": "Think twice before speaking.", "exampleCn": "在开口讲话前三思而行。"}
    d["and"] = {"pos": "连词", "meaning": "和；与；而且；那么", "phonetic": "/ænd/", "explanation": "并列连词，连接词、短语或从句。", "example": "Read and listen attentively every day.", "exampleCn": "每天认真倾听与阅读。"}
    d["but"] = {"pos": "连词/介词", "meaning": "但是；然而；除了", "phonetic": "/bʌt/", "explanation": "转折连词，表示对比或相反情况。", "example": "It is difficult, but entirely achievable.", "exampleCn": "这充满困难，但完全可以做到。"}
    d["or"] = {"pos": "连词", "meaning": "或者；否则；还是", "phonetic": "/ɔːr/", "explanation": "选择连词，表示二选一。", "example": "Would you like hot tea or fresh coffee?", "exampleCn": "您想喝热茶还是现磨咖啡？"}
    d["so"] = {"pos": "连词/副词", "meaning": "所以；因此；如此", "phonetic": "/soʊ/", "explanation": "因果连词，或程度副词。", "example": "You worked hard, so you succeeded.", "exampleCn": "你付出了努力，因此你成功了。"}
    d["because"] = {"pos": "连词", "meaning": "因为；由于", "phonetic": "/bɪˈkɔːz/", "explanation": "引导原因状语从句。", "example": "I study because knowledge empowers me.", "exampleCn": "我学习是因为知识赋予我力量。"}
    d["if"] = {"pos": "连词", "meaning": "如果；假如；是否", "phonetic": "/ɪf/", "explanation": "引导条件状语从句或宾语从句。", "example": "If you never try, you will never know.", "exampleCn": "如果你从不尝试，你将永远一无所知。"}
    d["although"] = {"pos": "连词", "meaning": "虽然；尽管", "phonetic": "/ɔːlˈðoʊ/", "explanation": "引导让步状语从句。", "example": "Although it rained, our trip was pleasant.", "exampleCn": "尽管下着雨，我们的旅行依然很愉快。"}
    d["as"] = {"pos": "介词/连词/副词", "meaning": "作为；如同；当...时；因为", "phonetic": "/æz/", "explanation": "多功能词，可作介词、时间/原因/方式连词。", "example": "Treat every challenge as a stepping stone.", "exampleCn": "把每一个挑战都视作垫脚石。"}
    d["than"] = {"pos": "连词/介词", "meaning": "比；比较", "phonetic": "/ðæn/", "explanation": "用于形容词或副词比较级之后。", "example": "Action speaks louder than empty words.", "exampleCn": "行动胜于空谈。"}
    
    # 冠词与限定词
    d["a"] = {"pos": "冠词", "meaning": "一(个/只/本/件) [辅音前]", "phonetic": "/ə/", "explanation": "不定冠词，修饰辅音音素开头的单数可数名词。", "example": "Have a wonderful day ahead.", "exampleCn": "祝你有美好的一天。"}
    d["an"] = {"pos": "冠词", "meaning": "一(个/只/本/件) [元音前]", "phonetic": "/ən/", "explanation": "不定冠词，修饰元音音素开头的单数可数名词。", "example": "It is an absolute honor to be here.", "exampleCn": "来到这里真是一项莫大的荣幸。"}
    d["the"] = {"pos": "定冠词", "meaning": "这(个)；那(些)；特指", "phonetic": "/ðə/", "explanation": "特指对话双方已知或世界上独一无二的事物。", "example": "The sun rises brightly in the east.", "exampleCn": "太阳从东方灿烂升起。"}
    d["all"] = {"pos": "代词/形容词/副词", "meaning": "全部；所有；都", "phonetic": "/ɔːl/", "explanation": "表示全体、所有范围。", "example": "All of us are eager to learn.", "exampleCn": "我们所有人都渴望学习。"}
    d["some"] = {"pos": "限定词/代词", "meaning": "一些；某些；大约", "phonetic": "/sʌm/", "explanation": "表示不确定的数量，常用于肯定句。", "example": "Could you give me some helpful advice?", "exampleCn": "你能给我一些有益的建议吗？"}
    d["any"] = {"pos": "限定词/代词", "meaning": "任何；一些 (疑问/否定)", "phonetic": "/ˈɛni/", "explanation": "用于否定句、疑问句或条件句中表示任何。", "example": "Do you have any further questions?", "exampleCn": "你还有任何进一步的问题吗？"}
    d["every"] = {"pos": "限定词", "meaning": "每一个；每隔", "phonetic": "/ˈɛvri/", "explanation": "强调群体中的每一个个体，后接单数名词。", "example": "Every single step counts toward your goal.", "exampleCn": "迈出的每一步都对达成目标至关重要。"}
    d["each"] = {"pos": "代词/限定词", "meaning": "各个；每个", "phonetic": "/iːtʃ/", "explanation": "着重指单个个体。", "example": "Each student received personal feedback.", "exampleCn": "每位学生都获得了量身定制的反馈。"}
    d["many"] = {"pos": "限定词/代词", "meaning": "许多；很多 (修饰复数)", "phonetic": "/ˈmɛni/", "explanation": "修饰可数名词复数。", "example": "Many talented people contributed to the project.", "exampleCn": "许多有才华的人为这个项目做出了贡献。"}
    d["much"] = {"pos": "限定词/副词", "meaning": "许多；大量；很 (修饰不可数)", "phonetic": "/mʌtʃ/", "explanation": "修饰不可数名词，或作副词修饰比较级。", "example": "Thank you so much for your guidance.", "exampleCn": "非常感谢您的悉心指点。"}
    
    return d

print("Base generator prepared.")
