"""
推荐精选分类 Part 4:
- COURSE_REC_STUDY_ABROAD: 留学生海外求学生活全景指南 (10章, 150句)
- COURSE_REC_DAILY_MOTTO: 晨起暮读：每日英文哲思金句 (10章, 150句)
"""

COURSE_REC_STUDY_ABROAD = {
    "id": "rec-study-abroad",
    "title": "留学生海外求学生活全景指南",
    "desc": "海外高校注册报到、选课规划、导师Office Hour沟通、学术研讨辩驳、文献阅读与作业论文、租房相处与生活日常全景地道口语与学术句式。",
    "category": "recommended",
    "categoryName": "推荐",
    "difficulty": "中高 B2",
    "icon": "🎓",
    "coverGradient": "from-sky-700 to-indigo-900",
    "tags": ["留学生", "海外求学", "学术交流", "校园生活", "高频表达"],
    "chapters": [
        {
            "id": "rec-study-ch01",
            "title": "第 1 章: 新生入学与注册报到",
            "sentences": [
                {"english": "Excuse me, could you point me toward the international student admissions office?", "chinese": "打扰一下，请问国际学生招生办公室怎么走？"},
                {"english": "I need to collect my student identification card and campus orientation packet.", "chinese": "我需要领取我的学生证和新生入学指导资料包。"},
                {"english": "All newly admitted students must submit certified vaccination records before class enrollment.", "chinese": "所有新录取的学生在正式选课前必须提交经过认证的疫苗接种记录。"},
                {"english": "The orientation leader guided us through the central library and laboratory complexes.", "chinese": "迎新辅导员带我们参观了中心图书馆和实验楼群。"},
                {"english": "Please ensure your passport and study permit remain valid throughout your academic tenure.", "chinese": "请确保你的护照和留学签证在整个就读期间始终处于有效期内。"},
                {"english": "You can activate your institutional email account using the credentials sent yesterday.", "chinese": "你可以使用昨天发给你的凭据激活你的大学官方邮箱账户。"},
                {"english": "Is there a designated shuttle bus operating between the airport and the north campus residence?", "chinese": "请问机场与北校区宿舍之间有专门的接驳车运行吗？"},
                {"english": "International students are required to attend the mandatory immigration regulation briefing.", "chinese": "国际留学生必须参加强制性的移民法规和签证条例说明会。"},
                {"english": "The student services center offers complimentary assistance with local banking setup.", "chinese": "学生服务中心为开设当地银行账户提供免费的指导与协助。"},
                {"english": "Our university provides peer mentor programs to help newcomers assimilate smoothly.", "chinese": "我们大学提供学长导师结对计划，帮助新生尽快适应融入新环境。"},
                {"english": "Make sure to pick up your room keys from the housing reception desk before five o'clock.", "chinese": "请务必在下午五点之前前往住宿前台领取你的宿舍钥匙。"},
                {"english": "The campus health center requires all attendees to purchase qualifying medical coverage.", "chinese": "校医院要求所有在校生购买符合资格规定的医疗健康保险。"},
                {"english": "You will receive a personalized campus map detailing dining halls and lecture halls.", "chinese": "你会收到一份标注了各个学生食堂和教学大楼的个性化校园地图。"},
                {"english": "What documents are required to complete the on-site identity verification procedure?", "chinese": "完成现场身份核实程序需要准备哪些材料？"},
                {"english": "Welcome everyone to our diverse academic community and exciting intellectual journey.", "chinese": "欢迎各位加入我们多元包容的学术大家庭，开启精彩的求学之旅。"}
            ]
        },
        {
            "id": "rec-study-ch02",
            "title": "第 2 章: 课程大纲解读与选课退换",
            "sentences": [
                {"english": "Let us carefully examine the grading breakdown outlined in the course syllabus.", "chinese": "让我们仔细阅读课程大纲中注明的成绩评分细则。"},
                {"english": "The instructor emphasized that seminar participation accounts for twenty percent of the overall evaluation.", "chinese": "导师强调研讨课的发言参与度占总评成绩的百分之二十。"},
                {"english": "I am currently placed on the waiting list for advanced cognitive psychology.", "chinese": "我目前排在高级认知心理学课程的候补名单中。"},
                {"english": "Students may drop or add courses without academic penalty during the first two weeks.", "chinese": "学生在前两周内可以增选或退选课程，不会影响学业档案记录。"},
                {"english": "This introductory statistics class serves as a mandatory prerequisite for econometrics.", "chinese": "这门基础统计学课程是修读计量经济学的必修先修课。"},
                {"english": "You need to obtain a special departmental override permit if the section is already full.", "chinese": "如果该教学班已经满员，你需要获得系里的特别选课准许审批。"},
                {"english": "Does this lecture series require purchasing a specific online homework platform access code?", "chinese": "这门系列讲座课程需要购买特定的在线作业平台访问激活码吗？"},
                {"english": "Balancing four intensive honors seminars this semester might become overly demanding.", "chinese": "本学期同时兼顾四门高难度的荣誉研讨课可能会让人吃不消。"},
                {"english": "The professor uploaded supplemental reading articles directly to the course management portal.", "chinese": "教授已将补充阅读文献直接上传到了课程网络学习平台。"},
                {"english": "Check whether your transferred credits satisfy the general education distribution standards.", "chinese": "请核对你转入的学分是否满足通识教育各个大类的分布要求。"},
                {"english": "The deadline for switching to a pass-or-fail grading option expires next Friday.", "chinese": "将评分方式改为及格/不及格考核的截止时间是下周五。"},
                {"english": "We must submit the preliminary project proposal before the midterm recess commences.", "chinese": "我们必须在期中放假开始之前提交初步的项目开题报告。"},
                {"english": "The course content covers both classical theories and groundbreaking contemporary research findings.", "chinese": "课程内容既涵盖了经典基础理论，也融入了前沿的前沿实证研究成果。"},
                {"english": "Consult your academic counselor before finalizing your semester credit schedule.", "chinese": "在最终确认本学期的选课修读计划前，最好先咨询你的专业学业顾问。"},
                {"english": "Failure to complete prerequisite sequences may delay your anticipated graduation timeline.", "chinese": "未能按时修满先修课程可能会推迟你预期的正常毕业时间。"}
            ]
        },
        {
            "id": "rec-study-ch03",
            "title": "第 3 章: 导师 Office Hour 沟通交流",
            "sentences": [
                {"english": "Thank you for scheduling time during your office hours to discuss my research direction.", "chinese": "非常感谢您在答疑答询时间抽空与我探讨我的课题研究方向。"},
                {"english": "I encountered several perplexing ambiguities while analyzing the primary historical data.", "chinese": "在分析这一一手历史文献数据时，我遇到了一些令人困惑的模糊之处。"},
                {"english": "Could you provide some constructive feedback on the methodology section of my draft?", "chinese": "您能就我初稿中的研究方法章节提供一些建设性的指导意见吗？"},
                {"english": "I want to clarify the theoretical framework referenced in your third lecture.", "chinese": "我想进一步请教您在第三堂讲座中提及的核心理论框架。"},
                {"english": "Professor Miller suggested that I narrow down the thesis scope to achieve greater depth.", "chinese": "米勒教授建议我适当缩小论文题目的切入范围，以便展开更透彻的论述。"},
                {"english": "I am seeking your formal approval to pursue an independent honors thesis next year.", "chinese": "我希望能获得您的正式批准，以便在明年开展独立的荣誉学位课题研究。"},
                {"english": "Is it possible to receive an extension on the term paper due to sudden illness?", "chinese": "因突发身体不适，请问我的期末学期论文是否有可能申请适度延期？"},
                {"english": "Your insightful critique helped me restructure the logical flow of my argumentation.", "chinese": "您深刻独到的点评帮助我重新梳理了整篇论证的逻辑主线。"},
                {"english": "I have brought the revised bibliography containing the latest peer-reviewed monographs.", "chinese": "我带来了重新修订的参考文献目录，里面补充了最新的同行评审专著。"},
                {"english": "Would you recommend any influential academic journals relevant to our current project?", "chinese": "关于我们当前的项目，您能推荐几本相关领域具有影响力的权威学术期刊吗？"},
                {"english": "I would appreciate your guidance on selecting potential doctoral programs and supervisors.", "chinese": "如果您能在申请博士研究生院校和导师选择上给予指点，我将不胜感激。"},
                {"english": "The advisor encouraged students to bring rough conceptual drafts rather than polished conclusions.", "chinese": "导师鼓励大家带着初步的想法草稿来讨论，而不是非要等到得出完美结论。"},
                {"english": "I wanted to make sure my interpretation aligns with the intended analytical focus.", "chinese": "我想确认一下我的分析理解是否契合这门课所倡导的研究切入视角。"},
                {"english": "Thank you for your generous encouragement; it truly bolstered my academic confidence.", "chinese": "感谢您的鼓励与提携，这极大增强了我在学术探究道路上的信心。"},
                {"english": "I will incorporate all your suggestions and send the revised version before Monday.", "chinese": "我会吸纳您的所有宝贵意见，并在下周一之前将修改后的文稿发送给您。"}
            ]
        },
        {
            "id": "rec-study-ch04",
            "title": "第 4 章: 研讨会提问与学术探讨",
            "sentences": [
                {"english": "I would like to raise a respectful counterargument to the viewpoint presented earlier.", "chinese": "我想对刚才提出的那个观点提出一段客气而审慎的商榷与反驳。"},
                {"english": "How does your hypothesis account for the notable anomalies observed in sample three?", "chinese": "你的理论假说该如何合理解释在第三组样本中观察到的显著异常现象？"},
                {"english": "The author seems to assume a causal link where only statistical correlation exists.", "chinese": "作者似乎在此把仅仅属于统计层面的相关性主观当成了必然的因果联系。"},
                {"english": "Could you elaborate on the underlying mechanism that produces this unusual effect?", "chinese": "你能详细阐述一下引发这种罕见效应的底层运作机理吗？"},
                {"english": "I partially agree with that assessment, although several crucial factors warrant deeper scrutiny.", "chinese": "我部分赞同该研判，但仍有若干关键影响因素需要进行更深入的探究。"},
                {"english": "Building upon what my colleague just noted, qualitative interviews reveal nuanced emotional patterns.", "chinese": "在刚才同仁发言的基础之上，定性访谈其实揭示出了更为细致的情感走向。"},
                {"english": "We must be cautious about generalizing findings derived from such a limited sample.", "chinese": "基于如此有限的样本所推导出的研究结论，我们在推广概括时务必保持审慎。"},
                {"english": "What theoretical traditions informed the development of your empirical analytical model?", "chinese": "请问是哪些理论流派的思想指引了你这套实证分析模型的构建？"},
                {"english": "Let us examine whether alternative hypotheses might yield equally convincing explanations.", "chinese": "让我们探讨一下是否存在其他替代假设，能够给出同样令人信服的解释。"},
                {"english": "The discussion highlighted profound discrepancies between classical assumptions and observed experimental realities.", "chinese": "这场研讨突显了经典理论预设与实验观察现实之间的深刻脱节。"},
                {"english": "Could we interpret this behavioral outcome from a comparative institutional perspective instead?", "chinese": "我们能否改换从比较制度主义的学术视角来重新解读这一行为结果？"},
                {"english": "I find the methodology innovative, though replication studies remain imperative for validation.", "chinese": "我认为该方法颇具开创性，不过开展重复验证研究对确证结论仍必不可少。"},
                {"english": "Does the existing literature offer comparable cases across developing socioeconomic environments?", "chinese": "现有文献库中是否在发展中国家或转型社会环境中提供过类似对比案例？"},
                {"english": "That question goes straight to the heart of the ongoing scholarly dispute.", "chinese": "那个问题切中要害，直接击中了当前学界争论最激烈的核心焦点。"},
                {"english": "Collaborative intellectual friction often sparks the most transformative insights during seminars.", "chinese": "在研讨会中，彼此思想观点的碰撞与激荡往往能孕育出最富洞察力的真知灼见。"}
            ]
        },
        {
            "id": "rec-study-ch05",
            "title": "第 5 章: 图书馆学术检索与文献阅读",
            "sentences": [
                {"english": "You can access peer-reviewed journals using the university library virtual private gateway.", "chinese": "你可以通过大学图书馆的虚拟专属通道直接检索访问国际同行评审期刊。"},
                {"english": "Boolean operators help refine your academic database search queries with remarkable precision.", "chinese": "合理运用布尔逻辑运算符能够以极高的精准度优化筛选学术数据库中的检索式。"},
                {"english": "I reserved a quiet study cubicle on the fourth floor for concentrated reading.", "chinese": "我在图书馆四楼预约了一间独立静音研读室，以便专心阅读文献。"},
                {"english": "The reference librarian demonstrated how to organize citations efficiently using modern software.", "chinese": "文献检索馆员向大家演示了如何借助现代文献管理软件高效整理参考文献。"},
                {"english": "Interlibrary loan services allow students to request scarce monographs from partner institutions.", "chinese": "校际互借服务允许广大学生向其他合作高校机构借阅本校未藏的稀缺学术专著。"},
                {"english": "Synthesizing disparate scholarly articles requires identifying common thematic threads and contradictions.", "chinese": "综合梳理多篇不同学者的论文需要敏锐捕捉其中的共同研究脉络与分歧矛盾。"},
                {"english": "Always evaluate the credibility, author credentials, and methodological rigor of every source.", "chinese": "对引用的每一篇文献，都必须严格评估其可信度、作者资质及方法论严密性。"},
                {"english": "The university archives preserve original manuscripts accessible only under guided supervision.", "chinese": "大学特藏档案馆珍藏着多份原始手稿，仅限在专业工作人员指导陪同下查阅。"},
                {"english": "I spent the entire afternoon skimming abstracts to determine which papers deserved thorough reading.", "chinese": "我花了一整个下午浏览论文摘要，以甄别哪些文献值得展开精读研磨。"},
                {"english": "Pay close attention to the limitations section, as it frequently suggests future research avenues.", "chinese": "请密切关注文献中的局限性章节，因为那里通常会启迪未来的学术突破方向。"},
                {"english": "Remember to renew your checked-out books online before the scheduled due date arrives.", "chinese": "记得在借阅到期日到来之前，在图书馆线上系统中办理图书续借手续。"},
                {"english": "Annotating critical arguments in the margins helps solidify comprehension and critical reflection.", "chinese": "在文献空白页边标注核心论点与旁注，有助于深化文本理解与批判性思考。"},
                {"english": "The repository houses thousands of digitized doctoral dissertations covering centuries of thought.", "chinese": "该学术仓储库收录了数以万计的数字化博士学位论文，跨越了几个世纪的思想历程。"},
                {"english": "Formulating an exhaustive literature review establishes a sturdy intellectual foundation for research.", "chinese": "构建一份详尽周密的文献综述，能为开展前沿学术探究奠定扎实严谨的理论根基。"},
                {"english": "Ensure all electronic book chapters and PDFs are backed up onto secure storage.", "chinese": "务必确保将所有电子书章节与文献PDF文件同步备份至安全的云端存储中。"}
            ]
        },
        {
            "id": "rec-study-ch06",
            "title": "第 6 章: 小组项目合作与任务分工",
            "sentences": [
                {"english": "Let us outline the project milestones and assign clear individual responsibilities today.", "chinese": "让我们今天确定项目的各个关键节点，并明确划分每位组员的职责分工。"},
                {"english": "I can take charge of data collection and statistical modeling using Python.", "chinese": "我可以负责使用Python进行前期数据清洗抓取与统计计量建模分析。"},
                {"english": "Who would like to synthesize our combined research findings into the slide deck?", "chinese": "有哪位组员愿意挑起大梁，将大家的研究成果汇总整合成演示文稿？"},
                {"english": "We should establish a shared online workspace to collaborate asynchronously on our draft.", "chinese": "我们应当搭建一个共享在线协作工作区，以便团队随时进行异步撰写与批注。"},
                {"english": "Meeting twice each week will keep everyone accountable to our established project timeline.", "chinese": "每周开展两次工作例会能够让每位成员紧跟我们既定的项目推进时间表。"},
                {"english": "I noticed an inconsistency between our theoretical assumptions and the preliminary empirical figures.", "chinese": "我注意到我们的理论假设推导与初步的实证统计数据之间存在一处口径不一致。"},
                {"english": "Everyone must review their respective sections for clarity and concise formatting beforehand.", "chinese": "每个人都必须提前通读并润色各自负责的章节，确保表达清晰、格式规范统一。"},
                {"english": "Let us rehearse our final presentation thoroughly to ensure seamless transitions between speakers.", "chinese": "让我们完整彩排一次最终的答辩演示，确保每位发言人之间的转承衔接天衣无缝。"},
                {"english": "Constructive collaboration means valuing diverse perspectives while maintaining rigorous shared academic standards.", "chinese": "富有成效的团队合作意味着在秉持严谨学术标准的同时，充分尊重并融合多元视角。"},
                {"english": "Please upload your updated analytical summary to the cloud directory by Thursday midnight.", "chinese": "请在周四午夜前将你最新更新的分析总结报告上传至团队云端目录中。"},
                {"english": "We need to anticipate potential tough questions that the panel might pose.", "chinese": "我们需要预先推演评委或导师在答辩提问环节可能会抛出的尖锐问题。"},
                {"english": "Dividing the literature review into conceptual themes made the workload much more manageable.", "chinese": "把文献综述部分按主题板块进行拆分认领，使整体工作负荷变得更加均衡适度。"},
                {"english": "Effective group dynamics require transparent communication and swift resolution of scheduling conflicts.", "chinese": "高效顺畅的团队协作需要坦诚透明的信息沟通，以及对日程冲突的迅速协调解决。"},
                {"english": "Our collective effort produced a much richer analytical framework than individual solo endeavors.", "chinese": "大家群策群力的集体智慧所构建出的分析框架，远比个人单打独斗更加丰富深刻。"},
                {"english": "Congratulations team; our hard work culminated in an outstanding and highly praised presentation.", "chinese": "祝贺大家！我们的辛勤付出换来了一场极为出色且广受好评的精彩结题汇报。"}
            ]
        },
        {
            "id": "rec-study-ch07",
            "title": "第 7 章: 论文初稿撰写与修改答疑",
            "sentences": [
                {"english": "A compelling thesis statement should present an arguable claim rather than a mere fact.", "chinese": "一个引人入胜的论点陈述应当提出一个具有可辩驳性的命题，而非单纯陈述既定事实。"},
                {"english": "Be meticulous about citing all borrowed assertions to uphold uncompromising academic integrity.", "chinese": "必须严谨细致地引用所有借鉴的学术论断，恪守不可动摇的学术诚信底线。"},
                {"english": "The campus writing center offers personalized consultations for revising sentence structure and argument flow.", "chinese": "大学写作中心提供一对一的个性化指导，帮助学生润色句子结构和优化论证脉络。"},
                {"english": "I need to eliminate redundant filler words to respect the strict word limit.", "chinese": "我需要删去那些繁冗多余的套话废话，以恪守严格的论文篇幅字数限制。"},
                {"english": "Ensure that your paragraph transitions establish coherent intellectual bridges between supporting arguments.", "chinese": "确保各段落之间的过渡句能在各个支撑论据之间架起连贯流畅的逻辑桥梁。"},
                {"english": "The reviewer noted that the methodology section requires far more transparent operational details.", "chinese": "审稿人指出方法论章节需要提供更加详尽透明的操作细节和实施流程。"},
                {"english": "Proofreading backward from the final paragraph often helps catch subtle typographical errors.", "chinese": "从文末段落倒序向前进行校对，往往能极其敏锐地发现细微的排版与拼写疏漏。"},
                {"english": "Passive voice can occasionally obscure the scholarly actor responsible for a particular initiative.", "chinese": "通篇滥用被动语态有时会掩盖开展某项具体研究举措的实际责任主体。"},
                {"english": "Check your citations against the designated institutional manual, whether APA, MLA, or Chicago.", "chinese": "请严格对照学校规定的引文格式体例（无论是APA、MLA还是芝加哥格式）逐条核对引用。"},
                {"english": "The introductory remarks should hook the reader and clearly frame the research significance.", "chinese": "导论开篇应当迅速吸引读者的阅读兴趣，并清晰界定出本项研究的核心理论与现实价值。"},
                {"english": "Plagiarism software will screen all uploaded submissions against global scholarly publications and past archives.", "chinese": "查重检测软件将把所有提交的文稿与全球已发表学术成果和往届文献库进行全量比对。"},
                {"english": "I rewrote the conclusion three times to ensure it resonated with memorable analytical weight.", "chinese": "我把结论部分反复修改重写了三遍，确保它结语有力、蕴含深刻耐读的理论分量。"},
                {"english": "Peer feedback revealed that my opening argument assumed prior knowledge the reader might lack.", "chinese": "同学间的互评反馈提醒我，我的开篇论述默认了读者本可能不具备的某些前置背景知识。"},
                {"english": "Formatting margins and page numbers properly reflects professional craftsmanship in academic submission.", "chinese": "规范设置页边距和页码等排版格式，体现了提交正式学术文稿时严谨专业的治学素养。"},
                {"english": "Submitting a polished draft brings immense intellectual satisfaction after months of painstaking research.", "chinese": "在经历数月艰辛深入的研磨探索后，提交一份精细打磨的定稿令人倍感充实与欣慰。"}
            ]
        },
        {
            "id": "rec-study-ch08",
            "title": "第 8 章: 校外租房与舍友日常生活",
            "sentences": [
                {"english": "We are looking for a furnished two-bedroom apartment within walking distance of campus.", "chinese": "我们正在寻找一套离学校步行可达、家具家电一应俱全的两居室公寓。"},
                {"english": "Does the monthly rental fee include central heating, municipal water, and high-speed internet?", "chinese": "请问每月租金里是否已经包含了集中供暖费、市政水费以及高速网络宽带费？"},
                {"english": "Carefully inspect the lease agreement for hidden clauses regarding security deposit deductions.", "chinese": "请仔细研读租赁合同条款，留意有关退房押金扣除的各项隐性约定。"},
                {"english": "We established a weekly chore chart to keep shared kitchen and living spaces tidy.", "chinese": "我们制定了一份每周家务轮值表，以保持公共厨房和起居空间的整洁有序。"},
                {"english": "Could you please keep the music volume down after ten in the evening?", "chinese": "晚上十点以后，能麻烦你尽量把音乐音量调小一点吗？"},
                {"english": "The landlord promised to send an authorized technician to repair the leaking faucet.", "chinese": "房东承诺会安排持有专业资质的维修师傅前来检修那个漏水的水龙头。"},
                {"english": "Splitting grocery costs evenly helps maintain fairness among roommates sharing communal meals.", "chinese": "平摊食品采购开销有助于在搭伙合餐的舍友之间维护和谐公平的相处氛围。"},
                {"english": "Let us notify each other well in advance whenever we plan to invite overnight guests.", "chinese": "无论我们谁打算邀请朋友留宿过夜，都最好提前知会对方并达成共识。"},
                {"english": "Subletting your room during the summer recess requires formal written permission from management.", "chinese": "在暑假期间将你的房间转租出去，必须获得物业管理处的正式书面许可。"},
                {"english": "Taking out the recycling containers on designated pickup days avoids municipal penalties.", "chinese": "在指定的垃圾清运日将可回收垃圾箱推至路边，可以避免产生市政违规罚款。"},
                {"english": "Living cooperatively with international roommates fosters mutual tolerance and rich cultural appreciation.", "chinese": "与来自不同国家的留学生同居一室，能够培养包容互谅的心态和深厚的文化鉴赏力。"},
                {"english": "Always lock the front deadbolt whenever you depart, even for a brief errand.", "chinese": "每次出门即便只是离开一会儿去办点小事，也请务必随手反锁好大门防盗锁。"},
                {"english": "We agreed to split utility bills automatically through a shared mobile banking application.", "chinese": "我们一致同意通过共享手机银行应用程序设置水电燃气账单的自动分摊扣款。"},
                {"english": "The residential neighborhood boasts quiet streets, grocery markets, and convenient bus lines.", "chinese": "该居住社区街道静谧安全，周边生鲜超市与便民公交路线一应俱全。"},
                {"english": "A considerate housemate communicates openly about personal boundaries and study space requirements.", "chinese": "一个善解人意的室友会就个人边界与专注学习空间需求与他人进行坦诚沟通。"}
            ]
        },
        {
            "id": "rec-study-ch09",
            "title": "第 9 章: 校园社团活动与跨文化社交",
            "sentences": [
                {"english": "The student involvement fair features over two hundred athletic, cultural, and academic societies.", "chinese": "学生社团招新巡礼展出了两百多个涵盖体育竞技、文化艺术与学术探索的学生社团。"},
                {"english": "Joining the university debate society sharpened my extemporaneous speaking and logical precision.", "chinese": "加入大学辩论社极大地磨炼了我的即兴口头表达能力与严密逻辑思辨水平。"},
                {"english": "International festival night invites students from every continent to share authentic cuisines.", "chinese": "国际文化节之夜盛情邀请来自五大洲的各国学子同台分享地道的家乡传统美食。"},
                {"english": "Volunteering with local community charities provides wonderful opportunities to practice everyday conversation.", "chinese": "参与当地社区慈善公益志愿活动，为练习日常地道英语口语提供了绝佳的交流契机。"},
                {"english": "Navigating cross-cultural nuance requires an open mind and a willingness to listen generously.", "chinese": "体察并理解跨文化交流中的微妙差异，需要怀抱开放包容的心态与宽厚倾听的诚意。"},
                {"english": "Our intramural soccer team advanced to the regional semifinals after a thrilling match.", "chinese": "我们校内业余足球队在一场惊心动魄的比赛后，成功挺进了大区半决赛。"},
                {"english": "Attending university public lectures allows you to interact directly with distinguished world scholars.", "chinese": "参加大学举办的名家学术通识讲座，能让你有机会与享誉世界的杰出学者面对面交流。"},
                {"english": "The campus outdoor adventure club organizes weekend hiking excursions in state national parks.", "chinese": "校园户外探险俱乐部经常组织在州立国家公园进行的周末徒步远足探索活动。"},
                {"english": "Embrace opportunities to step outside your comfort zone and converse with unfamiliar peers.", "chinese": "要敢于拥抱挑战，走出自己的心理舒适区，主动结识不同文化背景下的同龄伙伴。"},
                {"english": "Cultural misunderstandings can almost always be dissolved through candid humor and mutual goodwill.", "chinese": "文化差异所带来的偶尔误会与隔阂，几乎总能通过坦诚幽默与彼此善意化为无形。"},
                {"english": "Participating in model United Nations conferences broadens one's perspective on multilateral diplomacy.", "chinese": "积极参与模拟联合国大会活动，能够显著拓宽一个人对于多边国际外交事务的宏观视野。"},
                {"english": "The international student lounge hosts weekly casual coffee conversations open to everyone.", "chinese": "国际留学生多功能交流中心每周都会举办面向全体同学的轻松随性咖啡畅聊聚会。"},
                {"english": "Building meaningful friendships across cultures is among the most rewarding aspects of studying abroad.", "chinese": "跨越国界与文化阻隔建立深厚真挚的友谊，是海外求学生涯中最令人欣慰的收获之一。"},
                {"english": "Share your own traditions while showing genuine curiosity about the heritage of others.", "chinese": "在自信展示本国优美传统的同时，也要对他人源远流长的文化遗产报以由衷的好奇。"},
                {"english": "Campus life is vastly enriched when students contribute their unique life perspectives freely.", "chinese": "当广大学子毫无保留地贡献出自己独特的人生经历与视角时，大学校园生活将变得格外斑斓多姿。"}
            ]
        },
        {
            "id": "rec-study-ch10",
            "title": "第 10 章: 实习面试求职与毕业离校",
            "sentences": [
                {"english": "The university career development center hosts resume polishing workshops and mock interview simulations.", "chinese": "大学职业生涯发展中心经常组织简历精修工作坊以及高仿真模拟面试演练。"},
                {"english": "International students must apply for curricular practical training authorization prior to accepting paid work.", "chinese": "国际学生在正式接受带薪实习工作之前，必须依法申请CPT课程实习授权许可。"},
                {"english": "Craft a tailored cover letter explaining why your academic background aligns with the internship role.", "chinese": "撰写一封具有针对性的求职求聘自荐信，清晰说明你的专业学业背景为何契合该实习岗位。"},
                {"english": "Networking with alumni during industry banquets often uncovers unadvertised professional opportunities.", "chinese": "在行业酒会中与杰出校友建立联络脉络，往往能发掘出许多未公开发布的优质就业机会。"},
                {"english": "Prepare concise storytelling responses utilizing the situation, task, action, and result framework.", "chinese": "善于运用情境、任务、行动与结果（STAR）经典框架，准备简练有力的面试故事陈述。"},
                {"english": "Always send a gracious follow-up thank-you note within twenty-four hours after any formal interview.", "chinese": "在任何正式面试结束后二十四小时之内，务必向面试官发送一封得体大方的致谢跟进邮件。"},
                {"english": "Ensure all outstanding laboratory equipment and library accounts are cleared before graduation checkout.", "chinese": "在办理毕业离校手续之前，确保归还所有借用的实验仪器设备并结清图书馆账户。"},
                {"english": "The registrar will mail your official diploma to your designated permanent mailing address.", "chinese": "教务长办公室会将你的正式毕业学位证书邮寄至你预留的常住永久通信地址。"},
                {"english": "Ordering caps, gowns, and honorary stoles ahead of time guarantees proper sizing for commencement.", "chinese": "提前预订学士帽、学位服与荣誉绶带，能够确保毕业典礼当天服饰尺码合身得体。"},
                {"english": "Standing on the commencement stage alongside beloved peers marks an unforgettable lifetime milestone.", "chinese": "与朝夕相处的同窗挚友并肩屹立在毕业典礼舞台之上，标志着人生一座难忘的里程碑。"},
                {"english": "The skills, resilience, and friendships forged during your studies will empower your future career.", "chinese": "在求学生涯中所磨砺出的专业本领、坚韧心智与同窗情谊，必将为你未来的职业道路赋能蓄力。"},
                {"english": "Keep in touch with mentors whose guidance illuminated your intellectual and personal growth.", "chinese": "请与那些曾在你的学术求索与个人成长之路上指引明灯的恩师导师保持长久联系。"},
                {"english": "Joining the global alumni network unlocks professional mentorship across major metropolitan cities.", "chinese": "加入全球校友网络联合会，能在全球各大核心都会城市中获得业界前辈的职业导师指导。"},
                {"english": "Every challenge overcome overseas transforms into lifelong independence and quiet inner confidence.", "chinese": "在海外异乡所战胜的每一个风雨挫折，最终都沉淀为伴随一生的独立自主与笃定自信。"},
                {"english": "As you embark upon the next horizon, carry your hard-earned wisdom with pride and humility.", "chinese": "当你扬帆驶向崭新的人生广阔天地时，请带着历经磨砺换得的真知卓见，既自信自豪，又谦逊求真。"}
            ]
        }
    ]
}

COURSE_REC_DAILY_MOTTO = {
    "id": "rec-daily-motto",
    "title": "晨起暮读：每日英文哲思金句",
    "desc": "精选触动心灵的智慧箴言与生命沉思，涵盖自律、成长、逆境突围、心灵平静与真挚爱意，配以优雅中英文释义，滋养语言与精神世界。",
    "category": "recommended",
    "categoryName": "推荐",
    "difficulty": "中级 B1",
    "icon": "✨",
    "coverGradient": "from-amber-600 to-rose-700",
    "tags": ["晨读金句", "心灵哲思", "励志成长", "地道优美", "精神滋养"],
    "chapters": [
        {
            "id": "rec-motto-ch01",
            "title": "第 1 章: 晨光拂晓与崭新起点",
            "sentences": [
                {"english": "Every morning brings a pristine blank canvas waiting for your deliberate creative brushstrokes.", "chinese": "每一个破晓清晨都是一块崭新的纯净画布，静待你挥毫写下用心雕琢的生命诗篇。"},
                {"english": "The sun rises without fanfare, yet illuminates the entire sleeping world with steady warmth.", "chinese": "旭日东升从不喧哗张扬，却以恒久沉静的暖意拂照整个沉睡的大地。"},
                {"english": "Awaken with deliberate gratitude, for today offers opportunities that yesterday could not contain.", "chinese": "带着觉察与感恩悠然醒来吧，因为今天蕴藏的无限契机是昨日未曾拥有的新篇。"},
                {"english": "A fresh beginning requires nothing more than the courage to take one sincere step forward.", "chinese": "一个崭新的起点，所需要的不过是怀抱真诚信念向前迈出坚实一步的纯粹勇气。"},
                {"english": "Breathe in the crisp morning air and release all lingering regrets into the departing night.", "chinese": "深吸一口清晨微凉甘冽的空气，将所有滞留心头的过往遗憾随逝去的夜色一同释怀。"},
                {"english": "Your mindset at dawn quietly orchestrates the emotional melody of the unfolding day.", "chinese": "你黎明破晓时的心境与思维，悄然定下了这一整天生命交响乐的温和主调。"},
                {"english": "Do not seek an extraordinary life; make ordinary moments extraordinarily alive and meaningful.", "chinese": "不必刻意追逐惊世骇俗的传奇，且把每一个平凡质朴的寻常瞬间过得生机盎然、丰盈充沛。"},
                {"english": "Small intentional acts performed at sunrise establish an anchor of composure for the storm.", "chinese": "在清晨微光中专注做下的微小正念之举，能为抵御午后生活的风浪铸就一枚从容定锚。"},
                {"english": "Today you hold the quiet authority to rewrite old patterns and embrace gentle renewal.", "chinese": "今天，你拥有平静而坚定的主权，去重塑陈旧惯性，拥抱生命如初的温柔蜕变。"},
                {"english": "Let the morning light remind you that hope returns with unwavering celestial regularity.", "chinese": "且让那一抹晨曦提醒你：希望的归来如同日月星辰运转一般，坚定不移、永不失约。"},
                {"english": "Greet the dawn not with rushed anxiety, but with patient wonder for life itself.", "chinese": "迎候黎明破晓，无须脚步匆匆焦虑仓皇，而当对生命本体的存在抱以耐心的赞叹与敬畏。"},
                {"english": "The world awakens afresh each day, offering you permission to begin again without guilt.", "chinese": "天地万物每天都在重新苏醒，它慷慨地赋予你重新开始的权力，毫无沉重与挂碍。"},
                {"english": "A quiet cup of tea at daybreak can restore peace to a hurried mind.", "chinese": "拂晓时分静品一杯温茶，足以让终日奔忙焦虑的思绪重归澄澈安宁。"},
                {"english": "Stand tall like the ancient trees that welcome both golden sunrise and howling wind.", "chinese": "像参天古木那般坦荡昂首吧，既欣然拥抱灿烂金阳，亦无惧狂风凛冽的呼啸洗礼。"},
                {"english": "May your heart be light, your focus clear, and your steps steadfast this morning.", "chinese": "愿你今晨心境明澈从容，心神专注澄静，足下步履笃定从容、行稳致远。"}
            ]
        },
        {
            "id": "rec-motto-ch02",
            "title": "第 2 章: 习惯的力量与专注自律",
            "sentences": [
                {"english": "We do not rise to the level of our hopes; we fall to the discipline of our habits.", "chinese": "我们并不会直接攀升至希望的高度，而是最终沉淀为自律习惯所构筑的真实基石。"},
                {"english": "Small daily disciplines repeated consistently build monuments of achievement over decades.", "chinese": "数十年如一日坚持践行的微小自律，终将聚沙成塔，铸就令人肃然起敬的成就丰碑。"},
                {"english": "True freedom is not doing whatever you please, but possessing mastery over your impulses.", "chinese": "真正的自由绝非随心所欲放纵欲望，而是拥有驾驭自身冲动与杂念的克制与定力。"},
                {"english": "Focus is the art of saying a respectful no to a thousand distracting temptations.", "chinese": "专注的艺术，在于懂得以庄重坚定的姿态，向成百上千种让人分心的诱惑说不。"},
                {"english": "The secret of exceptional skill hides within the quiet monotony of deliberate practice.", "chinese": "卓越超群技艺的全部奥秘，恰恰深藏于日复一日专注刻意练习的寂寞与单调之中。"},
                {"english": "Do not wait for elusive inspiration to work; let discipline summon inspiration through labor.", "chinese": "切莫枯等飘忽不定的灵感乍现才开始动手；要靠坚毅自律的行动在劳作中唤醒灵感。"},
                {"english": "Discipline weighs ounces in daily effort, while regret burdens the soul with heavy tons.", "chinese": "日常克己自律的付出不过轻如毫厘，而虚度光阴后的悔恨却重若万钧、压迫心灵。"},
                {"english": "Guard your morning hours fiercely, for they hold the greatest creative potency of your day.", "chinese": "请竭力捍卫你宝贵的晨间时光，因为那里蕴含着你一天中最具创造力的充沛心力。"},
                {"english": "Consistency transforms the mundane into mastery through patient, unheralded repetition.", "chinese": "持之以恒的定力，在耐心而无声的反复磨砺中，能将平凡琐碎化为通透神妙的精深造诣。"},
                {"english": "A single hour of deep uninterrupted focus accomplishes more than days of fragmented multitasking.", "chinese": "一小时摒除杂念的深度专注，远比数天在多任务之间来回切换的浮躁劳碌更富成效。"},
                {"english": "Build habits that serve your long-term vision rather than satisfying momentary fleeting comforts.", "chinese": "要构建服务于长远生命愿景的健康习惯，而非沉溺于迎合一时转瞬即逝的舒适安逸。"},
                {"english": "When motivation wanes, let established daily structure carry your progress forward effortlessly.", "chinese": "当一时的激情退潮之际，让早已融于血液的日常秩序从容推动你的步伐向前迈进。"},
                {"english": "You become what you repeatedly attend to; choose your mental focal points with reverence.", "chinese": "你所反复凝视与聚焦的事物终将塑造你自身；请以敬畏虔诚之心抉择你心灵安放的焦点。"},
                {"english": "Mastery demands neither genius nor luck, but persistent dedication in the face of plateau.", "chinese": "通往炉火纯青的彼岸既非仰赖天才也非倚仗侥幸，而是在漫长平台期中仍旧甘之如饴的坚守。"},
                {"english": "Every finished task adds a sturdy brick to the temple of your self-respect.", "chinese": "每一项善始善终圆满完成的任务，都是在为你内心自尊自爱的宏伟殿堂添砖加瓦。"}
            ]
        },
        {
            "id": "rec-motto-ch03",
            "title": "第 3 章: 逆境中的韧性与破茧重生成长",
            "sentences": [
                {"english": "The oak tree gains its deepest strength by weathering harsh winds on open plains.", "chinese": "参天橡树之所以能根深叶茂，正是因为历经了开阔旷野中肆虐凛冽寒风的反复洗礼。"},
                {"english": "Adversity does not break the resilient spirit; it burns away superficial illusions of security.", "chinese": "逆境与磨难击不垮坚韧的灵魂；它只是无情焚毁了那些关于安全感的浮华幻象。"},
                {"english": "When the path forward appears blocked, look closer: the obstacle itself becomes the teacher.", "chinese": "当前行之路似乎被巨石封堵，不妨走近细看：那块横亘眼前的绊脚石本身就是点化你的导师。"},
                {"english": "A diamond is simply a lump of coal that endured extraordinary pressure without surrender.", "chinese": "钻石不过是一块曾经承受过难以想象的极限高压、却从未破碎屈服的纯粹碳石。"},
                {"english": "You are far stronger than the temporary grief currently clouding your mental horizon.", "chinese": "你内在蕴藏的力量，远比此刻笼罩在你心灵天际线上的短暂哀愁要坚固强大得多。"},
                {"english": "Scars are not emblems of shame; they are silent testaments to battles survived with dignity.", "chinese": "身上的伤痕从不是羞耻的印记；它们是带着尊严与勇气挺过风雨拼杀的无声勋章。"},
                {"english": "The darkest hour of midnight holds the secret promise that dawn is already gathering strength.", "chinese": "午夜最幽深莫测的浓重黑暗，早已悄然孕育着黎明破晓那一抹蓄势待发的温润光芒。"},
                {"english": "Resilience is not the absence of falling, but the instinct to rise one more time.", "chinese": "真正的坚韧绝非从未跌倒摔痛，而是在倒地之后依然本能地咬牙重新站立起来。"},
                {"english": "In the furnace of difficulty, character is forged with durable metallurgical grace.", "chinese": "在艰难困苦的烈火熔炉之中，人的崇高风骨被淬炼得如同纯钢般百折不挠、沉稳优雅。"},
                {"english": "Trust the unfolding process even when the final outcome remains hidden from view.", "chinese": "即便终点尚未在眼前展现清晰轮廓，也请依然深信这番生命蜕变进程中的每一步沉淀。"},
                {"english": "Every winter eventually surrenders its bitter chill to the unstoppable surge of green spring.", "chinese": "哪怕再漫长酷烈的极寒严冬，最终都必将在势不可挡的满园春色与生机面前坦然退让。"},
                {"english": "Do not curse the storm; learn to navigate the waves with seasoned seamanship and grit.", "chinese": "不要一味诅咒肆虐的风暴；要学会在惊涛骇浪中锤炼出老练沉着的水手本领与坚毅骨气。"},
                {"english": "Pain passes like traveling clouds, leaving behind a sky purified of needless vanities.", "chinese": "痛苦如过眼云烟终会飘散远去，为苍穹留下一片洗尽铅华、澄澈辽阔的宁静与透彻。"},
                {"english": "You were made for profound growth, and growth demands outgrowing obsolete shells of comfort.", "chinese": "你生来便注定要实现深远的精神蜕变，而蜕变成长必须勇敢褪去早已逼仄过时的安逸旧壳。"},
                {"english": "Stand firm in your truth; after the tempest subsides, your core values will remain intact.", "chinese": "请坚守内心的真理与良知；暴风骤雨平息过后，你最珍视的核心价值必将岿然屹立如初。"}
            ]
        },
        {
            "id": "rec-motto-ch04",
            "title": "第 4 章: 接纳不完美与自我慈悲",
            "sentences": [
                {"english": "Perfection is a sterile illusion; the beauty of life thrives in cracked and weathered authenticity.", "chinese": "完美不过是一种冰冷僵死的虚妄幻象；生命的真正大美往往在带有裂痕与风霜的真实中蓬勃绽放。"},
                {"english": "Treat yourself with the same gentle patience you would extend to a cherished child.", "chinese": "请以你在面对心爱孩童时那般温柔耐心的体恤与包容，善待那个疲惫奔波的自己。"},
                {"english": "You do not need to prove your worth to anyone; your existence is already sacred.", "chinese": "你无须费尽心机向任何人证明自己的价值；你的存在本身就已经是独一无二的生命奇迹。"},
                {"english": "Release the exhausting burden of trying to be everything to everyone at all times.", "chinese": "彻底卸下那份试图在所有时刻取悦所有人、扮演全能角色的身心俱疲的沉重枷锁吧。"},
                {"english": "Kintsugi teaches us that broken pottery mended with gold becomes more precious than before.", "chinese": "金缮修复的古老智慧启示我们：用碎金修补过的破损器物，往往比完好无损时更加贵重动人。"},
                {"english": "Forgive your younger self for mistakes committed while operating under limited understanding.", "chinese": "请宽恕当年那个因为认知局限与阅历不足而懵懂犯错的自己，与过去的青涩彻底和解。"},
                {"english": "Self-compassion provides a soothing sanctuary when external circumstances feel abrasive and cold.", "chinese": "当外界的风霜冷酷坎坷之时，向内的自我慈悲能为你构筑一座温暖宁谧的避风港湾。"},
                {"english": "Allow yourself to rest without interpreting pause as laziness or failure of will.", "chinese": "允许自己坦然停下脚步歇息，切莫将适时的调养与休整误读为懒惰或意志的衰颓。"},
                {"english": "Your vulnerabilities are not flaws; they are tender gateways where authentic empathy connects.", "chinese": "你的脆弱从不是什么人格缺陷；它们是让深沉真挚的同理心与人际温情得以交融的温柔入口。"},
                {"english": "Comparison is the subtle thief that robs you of joy and gratitude for your own journey.", "chinese": "盲目的攀比是一只狡黠的盗贼，悄无声息地偷走你对自身独特生命轨迹的喜悦与感恩。"},
                {"english": "Speak softly to the quiet ache within; healing occurs through loving acceptance, not harsh reprimand.", "chinese": "请对内心隐秘的隐痛轻声细语；灵魂的愈合源自慈爱的全然接纳，而非严厉的自我苛责。"},
                {"english": "You are allowed to be a masterpiece and a work in progress simultaneously.", "chinese": "你完全可以既是一尊底蕴深厚的大美杰作，同时也是一座仍在精雕细琢中的生命工坊。"},
                {"english": "Let go of the timeline you imagined; trust the organic rhythm of your own flourishing.", "chinese": "放下头脑中预设的人生刻板时间表吧；且请全然信任属于你自身花开花落的自然节奏。"},
                {"english": "True grace begins when you stop measuring your human dignity against external checklists.", "chinese": "当你不再用外界世俗的清单来衡量一个生命庄严的尊严之时，真正的从容优雅方才降临。"},
                {"english": "You are enough just as you are in this breath, complete and worthy of love.", "chinese": "就在此时此刻这悠悠一呼一吸之间，当下的你已经足够完整，全然配得上世间一切深情与厚爱。"}
            ]
        },
        {
            "id": "rec-motto-ch05",
            "title": "第 5 章: 细微确幸与生活中的感恩",
            "sentences": [
                {"english": "Gratitude turns what we already possess into more than enough for deep contentment.", "chinese": "由衷的感恩能将我们眼前业已拥有的一切，化作足以令人内心安然丰盛的充盈滋养。"},
                {"english": "Notice the silver edge on morning clouds and the cheerful chirping of sparrows outside.", "chinese": "留心凝望晨云边缘那一抹泛光的银边，侧耳倾听窗外麻雀清脆欢快的啼鸣。"},
                {"english": "Happiness rarely hides in massive grand events; it dwells in warm bread and laughter.", "chinese": "幸福极少潜藏在轰轰烈烈的宏大事件里；它更常寓于刚出炉面包的麦香与随性的欢笑中。"},
                {"english": "Thankfulness is an inner posture that invites peace to take root in everyday chaos.", "chinese": "感恩是一种内在的生命仪态，能在日常纷繁喧嚣的生活底色中，让平和从容深扎根基。"},
                {"english": "Cherish the familiar aroma of morning coffee brewing while raindrops tap upon the windowsill.", "chinese": "细细品味清晨咖啡升腾而起的熟悉醇香，听窗外细雨轻轻叩击着落满微尘的窗棂。"},
                {"english": "A thankful heart acts like an acoustic chamber that magnifies every note of simple joy.", "chinese": "一颗常怀感恩的心宛如一间精妙的混响琴室，能将最质朴微小的欢愉音符放大得余音绕梁。"},
                {"english": "Look around your room: countless hands labored across the globe to furnish your quiet comfort.", "chinese": "环顾你的居室四周吧：全球各地无数双劳作者的双手，共同织就了你此刻享有的静谧舒适。"},
                {"english": "To love the ordinary is to discover heaven tucked quietly into grocery aisles and laundromats.", "chinese": "学会热爱平常生活的细碎点滴，就等同于在日常超市货架与洗衣店的柴米油盐中发现了世间桃源。"},
                {"english": "Write down three blessings before retiring to sleep; watch how peacefully your spirit rests.", "chinese": "在入夜安歇前随手记下三件今日蒙受的恩典；细细体味你的心灵将如何重归安详静谧。"},
                {"english": "The world is saturated with wonders, waiting only for eyes humble enough to notice.", "chinese": "这世界本就处处充盈着造化的神奇与诗意，它仅仅等待着一双足够谦卑澄澈的眼睛去发现。"},
                {"english": "A shared meal eaten with laughter nourishes the soul far deeper than lavish solitary feasts.", "chinese": "与挚友知己围坐谈笑共进的简朴便餐，对心灵的温润抚慰远胜过那些奢华孤寂的盛宴。"},
                {"english": "Never overlook the gift of a healthy breath and the strength to stand tall today.", "chinese": "切莫轻视今日能够畅快呼吸新鲜空气的馈赠，以及双腿稳稳屹立大地的健康与力量。"},
                {"english": "Gratitude does not deny life's sorrows; it shines a steady candle amidst prevailing darkness.", "chinese": "感恩从不否认人世间的悲欢与坎坷；它只是在漫漫黑夜之中，点亮并守护一根不灭的烛火。"},
                {"english": "Savor the unscripted simplicity of this afternoon: nothing urgent, everything in its place.", "chinese": "细细品味这个未经刻意排练的闲暇午后：并无急迫待办的火警，世间万物各安其位。"},
                {"english": "When you count your blessings, you realize you are already wealthy beyond measure.", "chinese": "当你静下心来细数生命中的所得所遇，你便会豁然顿悟：自己早已坐拥无量丰足的财富。"}
            ]
        },
        {
            "id": "rec-motto-ch06",
            "title": "第 6 章: 静水流深与内在专注宁静",
            "sentences": [
                {"english": "Silence is not the absence of sound, but the presence of profound self-awareness.", "chinese": "寂静绝非声音的虚无缺失，而是深沉觉察与灵魂自我觉醒的庄严显现。"},
                {"english": "Still waters run deep; the quietest minds frequently harbor the most penetrating wisdom.", "chinese": "静水方能流深；那些表面看起来最为沉默沉静的心灵，往往蕴含着最为洞若观火的智慧。"},
                {"english": "Step away from the clamor of opinions and listen to the murmuring wisdom of your heart.", "chinese": "从外界纷乱杂沓的舆论喧嚣中抽身退步吧，静下心来倾听内心深处那汩汩流淌的本真智慧。"},
                {"english": "Solitude is where we meet ourselves without masks, pretense, or the need to impress.", "chinese": "独处是一场圣洁的相遇：在那里我们无需面具伪装，也不必迎合外界，只与赤诚的自己相拥。"},
                {"english": "In a culture addicted to noise, deliberate quietness is an act of revolutionary courage.", "chinese": "在一个对浮躁喧嚣上瘾成疾的时代里，葆有主动寻觅寂静的定力是一种极具革命性的勇气。"},
                {"english": "The lake reflects the sky perfectly only when its surface is free from turbulence.", "chinese": "唯有当湖面平息了所有的波澜与涟漪之时，它才能将万里长空的澄澈纤毫毕现地倒映其中。"},
                {"english": "Cultivate an interior sanctuary where external storms cannot breach your core tranquility.", "chinese": "在内心深处修筑一座坚不可摧的安宁圣所吧，任凭外界狂风暴雨呼啸，亦无法撼动你分毫。"},
                {"english": "Do not mistake busyness for purpose; a carousel moves frantically yet arrives nowhere.", "chinese": "切莫把整日盲目的忙碌误当成崇高的人生使命；旋转木马狂乱转动，却终究未曾前行半步。"},
                {"english": "Peace is not the elimination of difficulty, but the calm center within the vortex.", "chinese": "安宁并非指世间从此再无风浪波折，而是指在狂风风眼的中心依然保有一份不动如山的静气。"},
                {"english": "Take five conscious deep breaths; return your scattered awareness back home to this body.", "chinese": "做五次沉静深长的觉知呼吸吧；将你四散游离的神思重新唤回当下这具鲜活安详的躯体中。"},
                {"english": "A serene spirit perceives solutions that remain invisible to a mind blinded by panic.", "chinese": "一颗从容恬淡的心灵，能够敏锐捕捉到那些在恐慌焦躁蒙蔽之下完全隐匿无踪的破局答案。"},
                {"english": "The mountain does not announce its majesty; it simply stands immovable through shifting seasons.", "chinese": "崇山峻岭从不向世人炫耀自身的巍峨雄伟；它只是在岁月的沧桑更迭中傲然屹立、岿然不动。"},
                {"english": "Guard the gates of your attention as carefully as you guard your home against intruders.", "chinese": "请像警惕外人非法闯入你的家宅那般，严密守护好你心灵专注力的大门与领地。"},
                {"english": "True power rests not in explosive shouts, but in unshakeable, measured composure.", "chinese": "真正撼动人心的力量绝非体现在歇斯底里的咆哮之中，而蕴含于坚如磐石、有理有节的从容泰然。"},
                {"english": "Let the evening quiet wash over you like cool mountain rain after a scorching summer day.", "chinese": "且让这落日余晖后的静谧夜色，如夏日酷暑后的一场甘洌山雨，缓缓洗涤去你一天的身心尘劳。"}
            ]
        },
        {
            "id": "rec-motto-ch07",
            "title": "第 7 章: 友谊的温度与真挚理解",
            "sentences": [
                {"english": "A true friend is one who walks in when the rest of the world walks away.", "chinese": "真正的挚友，是在全世界纷纷离你而去之际，依然义无反顾默默走向你的那个人。"},
                {"english": "The highest privilege of companionship is being heard and accepted without qualification.", "chinese": "人世间陪伴相守的最高礼遇，莫过于自己的心声能被对方全然倾听，且毫无保留地被全然接纳。"},
                {"english": "Friendship is not about who you have known longest, but who proved dependable when needed.", "chinese": "友谊的深浅从不取决于认识彼此岁月的长短，而在于当你身处低谷时谁用行动给过你可靠的托举。"},
                {"english": "Shared laughter doubles our joy, while shared sorrow halves the bitter weight of grief.", "chinese": "与知己分享的欢笑能让喜悦成倍绽放，而倾诉分担的忧愁能将沉痛的苦涩化去大半。"},
                {"english": "Listen to understand another person's heart rather than merely preparing your next clever rebuttal.", "chinese": "请带着由衷理解对方心境的温情去倾听，而不是在脑海里一味打磨自己下一句机敏的反驳辞令。"},
                {"english": "Kindness is an unspoken language that the deaf can hear and the blind can see.", "chinese": "发自内心的纯粹善良是一门无声的世界语言，失聪者能听懂其温度，失明者亦能感知其光明。"},
                {"english": "Small thoughtful gestures of affection build emotional reservoirs that sustain relationships across years.", "chinese": "日常琐碎中体贴入微的关怀举动，能汇聚成深厚的情感蓄水池，滋养着岁月中长青的情谊。"},
                {"english": "Never underestimate the profound healing carried in a warm hug and sincere reassurance.", "chinese": "切莫轻视一个温暖有力的拥抱和一句真挚肯定的安抚，其中蕴含着润物无声的疗愈力量。"},
                {"english": "Be the friend who remembers forgotten birthdays and asks how someone's soul is faring.", "chinese": "做那个会细心记挂他人琐碎日常、并会真诚探问对方心灵近来是否安好的知心友人吧。"},
                {"english": "Distance means very little when two kindred spirits remain tethered by mutual respect.", "chinese": "当两颗息息相通的灵魂因彼此敬重而紧紧相连时，千里关山与万水之隔便显得微不足道。"},
                {"english": "Do not hoard your love; express appreciation while your loved ones are here to listen.", "chinese": "切莫将爱意深藏心底吝于表达；趁着深爱的人尚在身旁聆听，抓紧向他们倾诉由衷的赞美与感恩。"},
                {"english": "A conversation with a wise and empathetic friend can untangle knots within troubled minds.", "chinese": "与一位睿智通达且富有同理心的好友促膝长谈，足以解开困扰心头许久的情感死结。"},
                {"english": "Forgive easily, communicate transparently, and preserve the precious bond against pride.", "chinese": "常怀宽容宽恕之心，保持坦荡透明的沟通，莫让无谓的傲慢与自尊损害了彼此珍贵的情谊。"},
                {"english": "The world becomes a warmer hearth when illuminated by the glow of genuine loyalty.", "chinese": "当有赤诚不渝的真挚情义在暗中相照时，整个冷酷的人间都会化为一座温暖明亮的围炉。"},
                {"english": "Hold close the rare souls who saw your shadows and loved your light anyway.", "chinese": "请紧紧拥抱那些曾见过你最幽暗深处的脆弱与阴影、却依然毫不犹豫深爱着你光芒的罕见灵魂。"}
            ]
        },
        {
            "id": "rec-motto-ch08",
            "title": "第 8 章: 保持好奇与终身求索",
            "sentences": [
                {"english": "Curiosity is the compass that guides the restless intellect toward untamed territories of truth.", "chinese": "好奇心是一枚灵动的生命罗盘，指引着永不满足的求知头脑驶向未知真理的无垠疆域。"},
                {"english": "Never stop asking why; behind familiar assumptions lies a universe of deeper mechanisms.", "chinese": "永远不要停止追问‘为什么’；在那些看似习以为常的常识预设背后，往往深藏着宏大的宇宙机制。"},
                {"english": "To remain curious throughout life is to drink perpetually from the fountain of youth.", "chinese": "在一生中始终保持孩童般敏锐的好奇心，就等同于在永葆青春活力与生机的灵泉边终身畅饮。"},
                {"english": "An open mind welcomes new evidence even when it upsets comfortably held preconceptions.", "chinese": "一个开放开明的心智，即便在面对颠覆自己既有舒适成见的新证据时，亦能从容敞开胸怀予以接纳。"},
                {"english": "Read widely beyond your field; creative leaps occur at the cross-pollination of disciplines.", "chinese": "博览群书，广泛涉猎专业以外的知识吧；最惊艳的创造性跃升，往往在学科跨界碰撞融合处迸发。"},
                {"english": "A person who asks questions may appear foolish for five minutes; a person who never asks remains foolish forever.", "chinese": "主动发问的人或许会显得有五分钟的青涩，但从不发问的人却注定要忍受终身的蒙昧与无知。"},
                {"english": "Marvel at the intricate design of a flower petal as intensely as a distant galaxy.", "chinese": "像赞叹遥远深邃星系那般，由衷惊叹一瓣花朵脉络中蕴含的鬼斧神工与精妙造化吧。"},
                {"english": "Knowledge is a vast ocean; the wiser you become, the clearer you perceive your own shores.", "chinese": "知识是一汪浩瀚无垠的沧海；一个人越是变得睿智通达，就越能清醒体认到自身认知的边界与浅陋。"},
                {"english": "Cultivate fascination with the world; boredom is merely failure to pay closer attention.", "chinese": "去深情体察这个光怪陆离的大千世界吧；所谓的无聊与乏味，不过是未曾细致专注凝视的借口。"},
                {"english": "Every human you meet carries knowledge about a world you have never experienced.", "chinese": "你生命中遇到的每一个普通过客，身上都携带着一段你未曾亲身领略过的广袤天地与人生阅历。"},
                {"english": "Let your questions be deeper than your conclusions, for conclusions close the door to discovery.", "chinese": "让你心中的发问远比既定的结论更为深邃吧，因为仓促的定论往往会过早关上探索未知的大门。"},
                {"english": "Explore old paths with new eyes and you will discover treasures hidden in plain sight.", "chinese": "尝试带着崭新的凝视视角去重访故地旧途，你会惊讶地发现那些一直明摆在眼前的隐秘宝藏。"},
                {"english": "Intellectual humility is the fertile soil where enduring wisdom takes root and thrives.", "chinese": "在求知路上的谦逊自省，恰是一片最肥沃的土壤，唯有在此处，永恒的真知与大智慧才能扎根繁衍。"},
                {"english": "The ultimate goal of education is not filling a vessel, but kindling an inextinguishable flame.", "chinese": "教育的终极要义绝非向一个空容器里机械灌注死板知识，而是点燃一簇永不熄灭的求知圣火。"},
                {"english": "Remain a lifelong student of the universe, and every sunrise will feel like matriculation day.", "chinese": "终身做这宏大宇宙一名谦逊求索的学子吧，那么每一次旭日东升都会让你宛如置身开学典礼般心潮澎湃。"}
            ]
        },
        {
            "id": "rec-motto-ch09",
            "title": "第 9 章: 活在当下与轻装前行",
            "sentences": [
                {"english": "Yesterday is a closed book, tomorrow is an unwritten promise, but today is life itself.", "chinese": "昨日是一本早已合上的青史，明日是一卷尚待落笔的期许，唯有当下这一刻才是鲜活流动的生命本体。"},
                {"english": "Do not let the ghost of past failures haunt the bright corridors of current opportunities.", "chinese": "切莫让往昔失败的过往幽灵，徘徊游荡在你当前唾手可得的明媚机遇长廊之中。"},
                {"english": "To carry grudges is to drink poison while expecting the other person to suffer.", "chinese": "在心中积压怨恨与仇怼，无异于自己端起毒鸩饮下，却荒唐地期盼着别人因此遭受剧痛折磨。"},
                {"english": "Simplicity is the deliberate elimination of the nonessential so the essential may speak.", "chinese": "所谓纯粹与至简，正是坚决剔除一切非本质的浮华与累赘，好让生命最本质的真谛从容发声。"},
                {"english": "Pack lightly on your spiritual journey; heavy baggage only tires the traveler before sunset.", "chinese": "在心灵求索的漫漫征途上请务必轻装简行；过于沉重的思想行李只会在日落黄昏前耗尽旅人的气力。"},
                {"english": "Presence is the rarest and most precious gift you can offer to anyone you encounter.", "chinese": "全神贯注身心合一的全然临在，是你能够馈赠给身旁所遇之人的最为罕见且珍贵的礼物。"},
                {"english": "Notice your feet touching the earth right now; you are here, alive, and anchored.", "chinese": "细心感受你的双足此刻沉稳踏在这片坚实大地上的触感；你身在此处，生机盎然，根基稳固。"},
                {"english": "Release the urge to micromanage outcomes; align your efforts and let the universe unfold.", "chinese": "放下那份试图掌控操纵每一个细微结果的控制执念；倾尽全力行该行之事，其余交予天道造化。"},
                {"english": "Worry does not empty tomorrow of sorrow; it empties today of its vitality and joy.", "chinese": "无谓的忧虑并不能洗去明日可能降临的哀愁；它只会无情榨干并透支今日应有的生机与欢愉。"},
                {"english": "Clear physical clutter from your desk; feel how effortlessly mental space opens up beside it.", "chinese": "动手彻底清理桌面上的杂物琐碎吧；细细体味伴随而来的，是头脑思维空间何等通透从容的舒展。"},
                {"english": "Drink your morning water with attention, savor each mouthful as the very nectar of vitality.", "chinese": "带着专注品饮清晨那杯甘泉吧，细细体味每一口水润如生命灵药般浸润周身经络的舒畅。"},
                {"english": "Holding on tightly often causes more agony than courageously opening your fingers and letting go.", "chinese": "死死不放的执迷往往比勇敢摊开手掌坦然释怀带来更痛彻心扉的折磨与沉沦。"},
                {"english": "The present moment is an eternal doorway: step through it and step out of anxiety.", "chinese": "当下这个瞬间是一扇通往永恒的大门：深吸一口气跨步迈过去，你便彻底挣脱了焦虑的罗网。"},
                {"english": "Live not for applause, but for the quiet satisfaction of knowing you walked with honor.", "chinese": "不要为了外界虚妄的掌声而活，而要为了内心那份深知自己步履坦荡、无愧于心的笃定而前行。"},
                {"english": "Breathe out the past, breathe in the now, and step gently into the awaiting afternoon.", "chinese": "呼出所有过往尘埃，吸入此时此刻的芬芳，迈着轻盈安然的脚步走向那等待着你的恬静午后。"}
            ]
        },
        {
            "id": "rec-motto-ch10",
            "title": "第 10 章: 暮色沉淀与对明天的期许",
            "sentences": [
                {"english": "As the sun dips below the horizon, let gratitude settle upon your soul like evening dew.", "chinese": "当夕阳缓缓隐入远方的地平线，让由衷的感恩如夜晚凝结的甘露般，静静浸润安抚你的灵魂。"},
                {"english": "You have fought today's battles with dignity; now lay down your armor and rest.", "chinese": "你已经带着尊严与从容打完了今日该打的战役；现在，请解下沉重的战甲，安心沉睡歇息。"},
                {"english": "The night sky does not compete with the sun; it reveals the infinite splendor of galaxies.", "chinese": "繁星点点的夜空从不与烈日争抢锋芒；它静静拉开天幕，展现出浩瀚星系无与伦比的深邃与壮美。"},
                {"english": "Reflect on today's small triumphs rather than ruminating upon what remained uncompleted.", "chinese": "多去回味今天所取得的哪怕最细微的胜利，而切莫深陷于那些未能尽善尽美的未竞之事中反刍叹息。"},
                {"english": "Sleep is sacred restoration; surrender your fatigue into the gentle cradle of the dark.", "chinese": "安详的睡眠是一场神圣的修复与滋养；将你满身的疲惫安然交付给夜色温柔无边的摇篮吧。"},
                {"english": "Tomorrow awaits with fresh mercy, clean sheets of opportunity, and boundless renewing grace.", "chinese": "崭新的明天正怀揣着全新的慈悲、洁净无瑕的机遇画卷以及无限抚慰人心的恩典静候着你。"},
                {"english": "Forgive whoever caused you injury today; do not allow anger to board your nighttime ship.", "chinese": "原谅今天曾让你感到委屈受伤的人吧；莫让忿恨与怨怒登上你驶向甜美梦乡的静夜之舟。"},
                {"english": "Close your eyes knowing that you planted good seeds whose harvest will arrive in due season.", "chinese": "阖上双眼吧，深知你今天已经亲手播撒下了美好的善种，丰硕的收成必将在合适时节如期而至。"},
                {"english": "The quiet stars above have watched over centuries of dreamers, and they watch over you tonight.", "chinese": "头顶苍穹上那些沉默注视的古老繁星，曾照耀过千百年来无数逐梦人的身影，今夜它们依然深情凝望着你。"},
                {"english": "Rest deeply, for the world needs your unique light and renewed vitality when morning comes.", "chinese": "安然深睡吧，因为当明晨第一缕阳光洒向大地时，这个世界依然渴望着你独特的光芒与勃发的生机。"},
                {"english": "Let the rhythm of your peaceful breathing anchor you in profound trust for the future.", "chinese": "让安详平缓的呼吸节奏，化作你对未来的深深信赖与无畏从容的磐石基座。"},
                {"english": "Even the mightiest rivers rest in placid lakes before continuing their long journey to the sea.", "chinese": "即便是奔腾千里的最壮丽江河，在继续浩荡奔向大海前，也会在恬静明澈的高山深湖中短暂停歇沉淀。"},
                {"english": "May your dreams be gentle, your mind untroubled, and your soul anchored in steadfast peace.", "chinese": "愿你今夜好梦轻柔，心无烦忧挂碍，灵魂稳稳安歇在笃定而深沉的祥和安宁之中。"},
                {"english": "Tonight, say a quiet thank you to your body for carrying you faithfully through another day.", "chinese": "今夜，请在心底轻声对自己的身躯道一声感谢，感恩它忠实而坚韧地陪伴你走过了又一个充实的人间昼夜。"},
                {"english": "Goodnight, dear traveler; peace be upon your slumber, and joy await your tomorrow.", "chinese": "晚安，亲爱的旅人；愿平静抚慰你的沉睡，愿无限欢欣与光明守候在你的明日破晓时分。"}
            ]
        }
    ]
}

if __name__ == "__main__":
    print(f"rec-study-abroad: {len(COURSE_REC_STUDY_ABROAD['chapters'])} chapters, {sum(len(c['sentences']) for c in COURSE_REC_STUDY_ABROAD['chapters'])} sentences")
    print(f"rec-daily-motto: {len(COURSE_REC_DAILY_MOTTO['chapters'])} chapters, {sum(len(c['sentences']) for c in COURSE_REC_DAILY_MOTTO['chapters'])} sentences")
