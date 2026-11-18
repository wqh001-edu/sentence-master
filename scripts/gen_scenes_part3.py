# -*- coding: utf-8 -*-
"""
场景英语 Part 3:
5. scene-hospital: 海外看病与药店就医 (10章150句)
6. scene-interview: 外企英文求职面试 (10章150句)
"""

COURSE_SCENE_HOSPITAL = {
    "meta": {
        "id": "scene-hospital",
        "title": "海外看病与药店就医",
        "category": "scenes",
        "difficulty": "初级·实用",
        "description": "涵盖预约挂号、病情主诉、常见病痛、化验检查、药房取药及医疗保险沟通，守护异国健康。",
        "cover": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=600&auto=format&fit=crop&q=80",
        "tag": "医疗健康"
    },
    "chapters": [
        {
            "id": "ch1", "title": "第1章：门诊预约与前台挂号",
            "sentences": [
                {"english": "Good morning, I would like to schedule an urgent medical consultation with a physician.", "chinese": "早上好，我想紧急预约一位全科内科医生进行门诊咨询看病。"},
                {"english": "Do you have an established medical patient file registered with our clinic network?", "chinese": "您之前在我们诊所医疗网络系统中有建立过患者病历档案吗？"},
                {"english": "No, this is my first time visiting your outpatient medical health center.", "chinese": "没有，这是我第一次来贵门诊医疗健康中心就诊。"},
                {"english": "Please fill out this personal health registration form and medical history questionnaire.", "chinese": "请填写这份个人健康登记表以及过往既往病史问卷。"},
                {"english": "Do you hold valid international travel health insurance or private medical coverage?", "chinese": "您持有有效的国际旅行健康医疗保险或者私人商业医疗保单吗？"},
                {"english": "Here are my policy card number and passport for identity verification purposes.", "chinese": "这是我的保险保单卡号以及用于身份核验的护照原件。"},
                {"english": "What is the primary acute physical symptom bringing you to the hospital today?", "chinese": "今天促使您来医院就医看病的最主要急性身体症状是什么？"},
                {"english": "I have been experiencing severe abdominal stomach cramps since yesterday late evening.", "chinese": "从昨天深夜起，我腹部一直出现难以忍受的剧烈绞痛。"},
                {"english": "Dr. Anderson has an available consultation opening at ten-thirty this morning.", "chinese": "安德森大夫今天上午十点半刚好有一个门诊空档可以看诊。"},
                {"english": "Please have a comfortable seat in the waiting reception lounge area.", "chinese": "请在门诊候诊接待大厅的舒适座椅上稍事休息等候。"},
                {"english": "The triage nurse will call your surname aloud when your consultation room is ready.", "chinese": "当下间诊室准备就绪时，分诊护士会在大厅大声叫您的姓氏。"},
                {"english": "How much is the initial general practitioner consultation fee for uninsured visitors?", "chinese": "对于没有本地医保的外国访客，全科医生的初诊挂号看诊费是多少？"},
                {"english": "The standard consultation fee is one hundred and twenty dollars excluding medication.", "chinese": "标准门诊看诊费为一百二十美元，药费和检验费另计。"},
                {"english": "We can provide itemized medical bills for you to claim insurance reimbursements.", "chinese": "我们可以为您出具明细医疗账单，以便您日后向保险公司申请理赔报销。"},
                {"english": "If you experience chest tightness or sudden breathlessness, alert nursing staff immediately.", "chinese": "如果您感到胸闷胸痛或突发呼吸困难，请立即向护士站警示求助。"}
            ]
        },
        {
            "id": "ch2", "title": "第2章：生命体征与分诊评估",
            "sentences": [
                {"english": "Please step inside the triage room so I can check your vital signs.", "chinese": "请进分诊室，我来为您测量一下基础生命体征指标。"},
                {"english": "I will place this digital thermometer probe under your tongue for twenty seconds.", "chinese": "我把这个电子体温计探头放在您的舌下含测二十秒钟。"},
                {"english": "Your body temperature reads 38.6 degrees Celsius, indicating a moderate fever.", "chinese": "您的体温显示为摄氏38.6度，表明目前处于中度发热状态。"},
                {"english": "Please roll up your left shirt sleeve so I can wrap the blood pressure cuff.", "chinese": "请挽起您的左侧衬衫衣袖，好让我帮您绑上血压计袖带。"},
                {"english": "Your blood pressure is one hundred and twenty-five over eighty-two millimeters of mercury.", "chinese": "您的血压读数是收缩压一百二十五、舒张压八十二毫米汞柱。"},
                {"english": "Let me clip this small pulse oximeter onto your index fingertip.", "chinese": "让我把这个小巧的脉搏血氧仪夹在您的右手食指指尖上。"},
                {"english": "Your resting pulse rate is 76 beats per minute and blood oxygen saturation is 98%.", "chinese": "您的静息脉搏是每分钟76次，血氧饱和度达到百分之九十八。"},
                {"english": "Please step onto the electronic scales so we can record your weight and height.", "chinese": "请站上电子秤台，以便我们精确记录您的体重和身高数据。"},
                {"english": "Are you currently pregnant, nursing, or planning to become pregnant very soon?", "chinese": "您目前有处于怀孕期、哺乳期或者近期有备孕计划吗？"},
                {"english": "Are you taking any regular daily prescription drugs, over-the-counter vitamins, or supplements?", "chinese": "您目前平时有长期服用任何处方药、非处方维生素或保健品吗？"},
                {"english": "Do you have any known medical adverse drug allergies, particularly to penicillin antibiotics?", "chinese": "您对哪些药物有已知的过敏反应不良史吗，尤其是对青霉素类抗生素？"},
                {"english": "I am dangerously allergic to penicillin and all synthetic cephalosporin medications.", "chinese": "我对青霉素以及所有人工合成的头孢菌素类药物都有严重过敏史。"},
                {"english": "I will immediately place a bright red allergy alert wristband onto your arm.", "chinese": "我立刻会在您的手腕上戴上一条醒目的红色药物过敏警示腕带。"},
                {"english": "Please rate the severity of your current pain on a scale from one to ten.", "chinese": "如果用1到10分来评估，您给自己目前身体的疼痛程度打几分？"},
                {"english": "The doctor is reviewing your vitals profile and will see you right now.", "chinese": "医生正在查阅您的生命体征记录，马上就为您进行详细诊断。"}
            ]
        },
        {
            "id": "ch3", "title": "第3章：感冒发烧与呼吸道症状",
            "sentences": [
                {"english": "Hello doctor, I have come down with a bad cold accompanied by severe chills.", "chinese": "大夫您好，我患上了严重感冒，伴随着浑身直打寒战发冷。"},
                {"english": "How many days have you been suffering from these respiratory viral flu symptoms?", "chinese": "您出现这些呼吸道病毒性感冒症状已经持续折磨几天了？"},
                {"english": "It started three days ago with a scratchy throat and developed into persistent fever.", "chinese": "三天前最早喉咙发痒干痛，随后逐渐演变成了持续性高烧不退。"},
                {"english": "I have an incessant dry hacking cough that gets considerably worse at night.", "chinese": "我一直不停地剧烈干咳，尤其到了半夜咳嗽得更加严重。"},
                {"english": "Are you coughing up thick yellowish phlegm or any streaks of blood?", "chinese": "您咳嗽时有咳出浓稠的黄绿色痰液或者带有血丝吗？"},
                {"english": "My nasal passages are completely congested and my sinuses throb with pressure.", "chinese": "我的鼻腔完全堵塞不通气，两侧鼻窦胀痛得一阵阵突突直跳。"},
                {"english": "Please tilt your head backward, open your mouth wide, and say 'Ah'.", "chinese": "请把头稍微往后仰，把嘴巴张得大大的，发一声“啊”。"},
                {"english": "Your palatine tonsils and throat pharynx are visibly inflamed and swollen red.", "chinese": "您的腭扁桃体和咽喉咽部黏膜明显充血、红肿发炎。"},
                {"english": "Let me listen to your lungs with the stethoscope; take slow, deep breaths.", "chinese": "让我用听诊器听一听您的肺部呼吸音；请深吸一口气，慢慢呼出。"},
                {"english": "Breathe in deeply through your open mouth and exhale through your nose.", "chinese": "请用张开的嘴巴深深吸气，然后慢慢用鼻子把气呼出来。"},
                {"english": "Your lower bronchial airways sound clear without any audible wheezing or crackles.", "chinese": "您的下支气管听起来很清晰通畅，没有听到任何哮鸣音或湿罗音。"},
                {"english": "We will perform a rapid nasal swab test for influenza A, B, and COVID-19.", "chinese": "我们将为您进行甲型乙型流感及新冠病毒三联快速鼻咽拭子抗原筛查。"},
                {"english": "The rapid viral antigen swab test results will be ready within fifteen minutes.", "chinese": "快速病毒抗原拭子检测的化验结果将在十五分钟内出来。"},
                {"english": "It looks like an acute upper respiratory viral infection requiring plenty of bed rest.", "chinese": "初步看来这是急性上呼吸道病毒感染，需要保证卧床多休息。"},
                {"english": "Drink plenty of warm fluid water and stay well hydrated throughout the day.", "chinese": "全天一定要多喝温水，确保身体时刻处于水分充盈状态。"}
            ]
        },
        {
            "id": "ch4", "title": "第4章：肠胃不适与腹痛腹泻",
            "sentences": [
                {"english": "Doctor, I woke up around midnight with violent stomach nausea and constant vomiting.", "chinese": "大夫，我半夜惊醒，感到一阵阵翻江倒海的恶心，并不停地剧烈呕吐。"},
                {"english": "I have had watery diarrhea bowel movements more than six times since dawn.", "chinese": "从今天天亮到现在，我已经连续拉了六次以上水样稀便了。"},
                {"english": "Did you consume any suspicious street food or undercooked raw seafood recently?", "chinese": "您最近有吃过任何可疑的街头摊贩食品或者未煮熟的生海鲜吗？"},
                {"english": "I ate raw oysters and cold potato salad at an outdoor seafood buffet.", "chinese": "我昨晚在一家露天海鲜自助餐厅吃过生蚝和凉拌土豆沙拉。"},
                {"english": "Please lie down flat on the examination examination table and relax your abdominal muscles.", "chinese": "请平躺在诊察检查床上，尽量放松您的腹部肌肉。"},
                {"english": "Does it feel sharply tender when I apply gentle pressure on your right abdomen?", "chinese": "当我用手指轻轻按压您右下腹部时，有感到尖锐剧烈的压痛吗？"},
                {"english": "There is no rebound tenderness, which largely rules out acute emergency appendicitis.", "chinese": "没有明显的反跳痛体征，这基本上可以排除急性突发性阑尾炎。"},
                {"english": "Your intestinal hyperactive bowel sounds indicate acute bacterial or viral gastroenteritis inflammation.", "chinese": "您的肠鸣音亢进活跃，提示存在急性细菌性或病毒性肠胃炎发炎。"},
                {"english": "We need to collect stool and blood samples to check for pathogen infections.", "chinese": "我们需要采集便样标本和静脉血样，以化验排查病原体感染。"},
                {"english": "The primary clinical danger right now is rapid electrolyte dehydration from fluid loss.", "chinese": "当前最主要的临床危险在于体液大量流失导致的急性电解质脱水。"},
                {"english": "We will administer an intravenous IV drip bag containing saline and essential electrolytes.", "chinese": "我们将为您静脉滴注一袋补充生理盐水和必需电解质的输液补液袋。"},
                {"english": "Take this oral rehydration salts packet dissolved thoroughly in one liter of water.", "chinese": "请将这包口服补液盐散剂完全溶解在一升干净饮用水中分次服用。"},
                {"english": "Stick strictly to a bland BRAT diet: bananas, rice, applesauce, and dry toast.", "chinese": "严格遵循BRAT清淡流食饮食原则：香蕉、白米粥、苹果泥和烤干吐司片。"},
                {"english": "Avoid all greasy fried foods, dairy milk products, caffeine, and spicy condiments.", "chinese": "坚决忌口所有油腻油炸食品、乳类奶制品、咖啡因饮料以及辛辣调料。"},
                {"english": "If the severe diarrhea persists beyond forty-eight hours, return to clinic immediately.", "chinese": "如果剧烈腹泻症状持续超过四十八小时不缓解，请务必立即回院复诊。"}
            ]
        },
        {
            "id": "ch5", "title": "第5章：外伤扭伤与骨科急诊",
            "sentences": [
                {"english": "I tripped over a sidewalk curb and twisted my right ankle very badly.", "chinese": "我不小心在人行道马路牙子上绊倒，把右脚脚踝狠狠扭伤了。"},
                {"english": "I heard an audible popping sound, and my ankle swelled up almost instantly.", "chinese": "当时我听到了一声明显的啪嗒脆响，随后脚踝几乎立刻肿胀鼓包起来。"},
                {"english": "Are you able to bear any weight on your injured right foot?", "chinese": "您受伤的右脚现在还能吃力着地、承受身体哪怕一点点重量吗？"},
                {"english": "No, it is excruciatingly painful whenever I try to put weight on it.", "chinese": "完全不行，只要我试图踩地用力，就会引发难以忍受的钻心剧痛。"},
                {"english": "Let me gently palpate the lateral malleolus bone and surrounding ligament tendons.", "chinese": "让我轻柔触诊按压一下外踝骨突及周围韧带和肌腱组织。"},
                {"english": "We need to take diagnostic X-ray radiographs to determine if there is a fracture.", "chinese": "我们需要为您拍几张X光放射线诊断片，以判断是否存在骨折。"},
                {"english": "The radiology technician will guide you into the radiological imaging examination room.", "chinese": "放射科技师会引导您坐轮椅进入放射影像拍摄检查室。"},
                {"english": "The X-ray films show no bone fractures, but you have a grade two ligament tear.", "chinese": "X光光片显示没有发生骨折断裂，但您出现了二级韧带撕裂挫伤。"},
                {"english": "You must strictly adhere to the RICE protocol: rest, ice, compression, and elevation.", "chinese": "您必须严格执行RICE应急处理原则：休息、冰敷、加压包扎和抬高患肢。"},
                {"english": "Apply crushed ice packs wrapped in a dry cloth for twenty minutes at intervals.", "chinese": "用干毛巾包裹碎冰袋敷在患处，每隔一段时间敷二十分钟。"},
                {"english": "We will fit you with an adjustable supportive walking boot and elastic compression bandage.", "chinese": "我们将为您穿戴一副可调节支撑步行护靴，并绑上弹性加压弹力绷带。"},
                {"english": "Here is a pair of aluminum underarm crutches to help you walk safely.", "chinese": "这是一副铝合金腋下双拐拐杖，协助您安全平稳下地行走。"},
                {"english": "The physical therapist will instruct you on how to adjust and use crutches.", "chinese": "理疗康复师会当面指导您如何根据身高调节并正确使用双拐。"},
                {"english": "Keep your injured foot elevated above heart level when resting on pillows.", "chinese": "躺卧休息时用枕头把受伤的脚垫高，保持高于心脏水平位置。"},
                {"english": "Ligament sprain recovery typically requires four to six weeks of protected healing.", "chinese": "严重的韧带扭伤通常需要四到六周的制动保护才能逐步康复痊愈。"}
            ]
        },
        {
            "id": "ch6", "title": "第6章：皮肤过敏与昆虫叮咬",
            "sentences": [
                {"english": "I woke up covered in intensely itchy red welts all over my skin.", "chinese": "我一早醒来发现全身上下皮肤都长满了奇痒难耐的红色风团疙瘩。"},
                {"english": "These raised red skin patches look like classic acute allergic urticaria hives.", "chinese": "这些凸起皮肤表面的红斑丘疹看起来是典型的急性过敏性荨麻疹。"},
                {"english": "Have you used any new laundry detergent, body wash soaps, or scented lotions?", "chinese": "您最近有更换使用任何新型号洗衣液、沐浴露皂液或香氛身体乳吗？"},
                {"english": "Were you hiking outdoors in wooded bushes or bitten by unfamiliar tropical insects?", "chinese": "您最近有在茂密森林灌木丛中徒步户外，或者被不认识的热带昆虫叮咬过吗？"},
                {"english": "I got bitten on my forearm by an insect, and the redness is spreading rapidly.", "chinese": "我的小臂被一只虫子咬了一口，红肿范围目前正在急剧向外扩散蔓延。"},
                {"english": "Is there a central punctum blister or a characteristic bullseye rash expanding outward?", "chinese": "红肿中心有明显的叮咬小水泡点，还是呈现特征性的向外扩大的靶心红斑？"},
                {"english": "We will draw a pen ink ring around the red margin to monitor progression.", "chinese": "我们将用医用记号笔沿着红肿边缘画一圈，以便密切监测病情进展。"},
                {"english": "Are you experiencing any facial lip swelling, eyelid puffiness, or difficulty swallowing?", "chinese": "您有出现任何面部嘴唇肿胀、眼睑浮肿或喉头吞咽困难的感觉吗？"},
                {"english": "Any signs of throat tightness indicate a life-threatening anaphylactic emergency reaction.", "chinese": "咽喉部任何收紧发紧的症状都预示着危及生命的严重过敏性休克反应。"},
                {"english": "I will give you an immediate intramuscular injection of antihistamine and corticosteroid.", "chinese": "我将立刻为您肌肉注射一支抗组胺药物联合皮质类固醇激素针剂。"},
                {"english": "Here is a topical hydrocortisone anti-inflammatory cream to apply twice daily to lesions.", "chinese": "这是一支外用氢化可的松消炎乳膏，每天涂抹两次于皮疹患处。"},
                {"english": "Take one non-drowsy cetirizine antihistamine allergy tablet every morning with water.", "chinese": "每天清晨随水温服一片不易致嗜睡的西替利嗪抗过敏抗组胺药片。"},
                {"english": "Avoid taking hot showers or scratching the lesions, which exacerbates dermal histamine release.", "chinese": "洗澡切勿使用过热热水，更不要抓挠皮疹，否则会加剧真皮组胺释放。"},
                {"english": "Wear loose, breathable pure cotton garments to avoid irritating fragile hypersensitive skin.", "chinese": "穿宽松透气的全棉衣物，避免摩擦刺激本就处于高敏状态的脆弱皮肤。"},
                {"english": "The hives and allergic swelling should substantially subside within twenty-four to thirty-six hours.", "chinese": "荨麻疹和过敏性肿胀通常会在二十四到三十六小时内显著消退缓解。"}
            ]
        },
        {
            "id": "ch7", "title": "第7章：处方开具与药房取药",
            "sentences": [
                {"english": "Here is your signed official medical doctor's prescription for the necessary medications.", "chinese": "这是为您开具并由主治医生亲笔签字的所必需药物的正式处方单。"},
                {"english": "Where can I find an open community retail pharmacy nearby to fill this prescription?", "chinese": "请问在附近哪里能找到正在开门营业的社区药房来抓取配齐这份处方？"},
                {"english": "There is a 24-hour Walgreens pharmacy located two blocks down on Maple Street.", "chinese": "顺着枫树街往前走两个街区，就有一家24小时全天候营业的沃尔格林药房。"},
                {"english": "Hello pharmacist, I would like to have this physician's prescription filled, please.", "chinese": "药剂师您好，我想请您帮我按照这张医生处方抓药调配药物。"},
                {"english": "Please present your prescription sheet, government photo identity card, and insurance coverage card.", "chinese": "请出示您的纸质处方、带照片的政府有效身份证件以及医疗保险卡。"},
                {"english": "Do you prefer the brand-name medication or an equivalent generic bioidentical substitute?", "chinese": "您更倾向于购买原厂品牌专利原研药，还是成分相同的仿制等效药？"},
                {"english": "The generic formulation contains the exact same active therapeutic ingredients at lower cost.", "chinese": "仿制药含有完全相同的核心活性有效治疗成分，但整体花费会低廉很多。"},
                {"english": "I will take the generic equivalent option to keep prescription drug expenses down.", "chinese": "那我选择仿制等效药选项，这样能节省不少处方购药开支。"},
                {"english": "Please take a numbered ticket and wait near the consultation counter window.", "chinese": "请先取一个排队号牌，在药师用药咨询窗口附近稍等片刻。"},
                {"english": "Your prescription order is prepared and packed safely inside this childproof bottle.", "chinese": "您的处方药物已经调配完毕，并安全封装在这只配有防儿童开启盖的药瓶中。"},
                {"english": "To open the child-resistant cap, push down firmly and twist counter-clockwise.", "chinese": "打开这种防儿童误开安全盖时，需要用力向下按压同时逆时针旋转拧开。"},
                {"english": "The yellow pharmacy label clearly outlines dosage instructions, frequency, and expiration dates.", "chinese": "瓶身黄色药房标签清晰标注了服用剂量、服药频次以及保质有效期限。"},
                {"english": "How much is the total copay cost for these three prescribed medications?", "chinese": "这三样处方药物在医保报销之后，我个人总共需要自付多少自付额？"},
                {"english": "Your insurance covered 80%, leaving an out-of-pocket copay balance of twenty-four dollars.", "chinese": "您的保险报销了百分之八十，剩余需要您自掏腰包支付的自付额为二十四美元。"},
                {"english": "Keep this original pharmacy receipt attached to your prescription copy for tax records.", "chinese": "请将这张药房原始收据附在您的处方副本后妥善保存，以备报税核查。"}
            ]
        },
        {
            "id": "ch8", "title": "第8章：用药指导与禁忌说明",
            "sentences": [
                {"english": "Please step over to the pharmacist counseling window so I can explain your medication.", "chinese": "请移步到药剂师用药指导窗口，由我为您详细讲解药品的正确服用方法。"},
                {"english": "Take one oral capsule every eight hours with a full eight-ounce glass of water.", "chinese": "每隔八小时口服胶囊一粒，送服时请务必饮用满整整一杯八盎司温水。"},
                {"english": "You must take this antibiotic tablet after finishing a hearty meal to prevent nausea.", "chinese": "您必须在吃完饱餐之后再服用这片抗生素药片，以防引发胃部反胃恶心。"},
                {"english": "It is absolutely vital to complete the entire seven-day antibiotic course without stopping.", "chinese": "至关重要的是，必须彻底吃满整整七天的抗生素全程疗程，绝不可中途擅自停药。"},
                {"english": "Do not stop taking the antibiotics simply because you begin feeling much better.", "chinese": "绝不能仅仅因为自己感觉身体好转了许多，就擅自提前中断停止服药。"},
                {"english": "Prematurely stopping antibiotics can lead to dangerous secondary bacterial antimicrobial resistance.", "chinese": "过早停用抗生素极易诱发致命的继发性细菌耐药性与抗药性变异。"},
                {"english": "Avoid consuming any alcohol, beer, or wine while taking this medication course.", "chinese": "在服用该药物治疗周期内，严禁饮用任何烈酒、啤酒或红白葡萄酒。"},
                {"english": "Mixing this drug compound with alcohol can induce severe liver toxicity and vomiting.", "chinese": "将该药物成分与酒精混合同服会引发极其严重的肝脏毒性损伤及剧烈呕吐。"},
                {"english": "This antihistamine allergy medicine may cause significant drowsiness and slower motor reflexes.", "chinese": "这种抗过敏抗组胺药物可能会导致明显的昏昏欲睡感并降低神经运动反射能力。"},
                {"english": "Do not drive motor vehicles, ride bicycles, or operate heavy machinery after ingestion.", "chinese": "服药后严禁驾驶机动车辆、骑行自行车或操作危险重型机械设备。"},
                {"english": "Store these eye drop bottles in your refrigerator between two and eight degrees Celsius.", "chinese": "请将这些眼药水滴眼剂瓶存放在冰箱冷藏室内，保持在摄氏2到8度之间。"},
                {"english": "Discard any remaining ophthalmic drops thirty days after breaking the bottle seal.", "chinese": "开封打破眼药水密封盖三十天后，瓶内所剩余的药液必须全部废弃丢弃。"},
                {"english": "Are there any adverse side effects that require immediate medical emergency attention?", "chinese": "有哪些不良药物副作用是一旦发生就需要立即送医看急诊的？"},
                {"english": "Seek immediate emergency care if you experience skin rash, facial swelling, or breathing difficulty.", "chinese": "若出现全身大面积皮疹、面部浮肿或呼吸费力急促，请立即就医看急诊。"},
                {"english": "Feel free to phone our 24-hour pharmacy helpline if questions arise regarding dosage.", "chinese": "如果在服用剂量上有任何疑问，欢迎随时拨打我们24小时药剂师热线。"}
            ]
        },
        {
            "id": "ch9", "title": "第9章：医疗账单与保险理赔",
            "sentences": [
                {"english": "Could you provide a comprehensive itemized master hospital bill showing all diagnostic codes?", "chinese": "能为我提供一份载有全部疾病诊断代码的详细明细医院综合总账单吗？"},
                {"english": "Our insurance claims adjuster requires standard international ICD-10 diagnostic disease codes.", "chinese": "我们保险公司的理赔精算核赔员需要符合国际标准的ICD-10疾病诊断代码。"},
                {"english": "Here is the certified medical certificate signed by the supervising attending physician.", "chinese": "这是由主管主治医生亲笔签字并加盖公章的正式医疗诊断证明书。"},
                {"english": "Does your international hospital department practice direct cashless billing with Allianz?", "chinese": "贵院国际医疗部与安联全球健康保险有开展直接免现金直付结算合作吗？"},
                {"english": "We offer direct settlement billing agreements with several multinational medical insurers.", "chinese": "我们与多家跨国商业医疗保险集团均签署有直付免现款赔付结算协议。"},
                {"english": "If your insurer is not on our direct list, you must pay upfront first.", "chinese": "如果您所投保的保险公司不在直付合作名录内，您需要先自行垫付医药费。"},
                {"english": "Keep all original signed cash receipts, pharmacy tickets, and diagnostic lab reports.", "chinese": "请完整保留好所有已签字的现金发票原件、药房配药小票及化验检验单。"},
                {"english": "We will stamp official hospital seals on your overseas insurance reimbursement claim form.", "chinese": "我们会在您的海外就医保险理赔申请表格上加盖医院官方正式印鉴印章。"},
                {"english": "What was the breakdown cost for the overnight emergency observation room stay?", "chinese": "急诊过夜观察室留观床位的具体费用拆分明细是怎样的？"},
                {"english": "The emergency room facility fee was three hundred and fifty dollars per night.", "chinese": "急诊室综合监护设施使用费标准为每晚三百五十美元。"},
                {"english": "Can I obtain digital scanned copies of my X-ray and CT imaging scans?", "chinese": "我可以获取一份我的X光平片和CT断层扫描影像的数字化刻录光盘或扫描件吗？"},
                {"english": "The radiology department can burn your medical DICOM image files onto a CD disc.", "chinese": "放射影像科可以把您的DICOM医学格式影像原始文件刻录到一张光盘中。"},
                {"english": "Is there an administrative archival fee for burning medical imaging records onto CD?", "chinese": "刻录医学影像原始档案光盘需要缴纳专门的行政档案制作费吗？"},
                {"english": "A nominal ten-dollar fee is charged to cover secure disc burning and verification.", "chinese": "我们象征性收取十美元工本费，用于覆盖光盘刻录及数据校验成本。"},
                {"english": "Submit all these documented medical proofs to your claims coordinator within sixty days.", "chinese": "请在六十天之内将所有这些带有凭证的就医材料完整提交给理赔专员。"}
            ]
        },
        {
            "id": "ch10", "title": "第10章：术后随访与康复出院",
            "sentences": [
                {"english": "The attending physician has evaluated your recovery progress and authorized your clinical discharge.", "chinese": "主治大夫已全面评估了您的术后康复进展，并正式批准了您的临床出院许可。"},
                {"english": "You have made remarkable physical progress and your surgical incision is healing cleanly.", "chinese": "您的身体机能恢复得非常出色，手术外科切口愈合得相当平整干净。"},
                {"english": "The sterile surgical sutures are scheduled to be removed in seven calendar days.", "chinese": "医用无菌外科手术缝合线预定在整整七个自然日之后予以拆除拆线。"},
                {"english": "Keep the wound dressing dressing dry and do not soak in bathtubs or pools.", "chinese": "请保持伤口敷料辅料干燥清洁，切勿在浴缸或游泳池中浸泡受潮。"},
                {"english": "We will schedule a comprehensive follow-up appointment for next Thursday at two o'clock.", "chinese": "我们将为您安排下周四下午两点进行一次全面的术后复查门诊预约。"},
                {"english": "If you experience high fever above 39 degrees or increasing wound redness, call us.", "chinese": "如果您体温突发高烧超过39度，或伤口红肿范围持续扩大，请立即致电我们。"},
                {"english": "Here is the discharge summary documentation outlining your diagnosis, procedures, and prescriptions.", "chinese": "这是为您出具的出院小结总结文件，详尽概述了诊断结论、手术经过及出院带药。"},
                {"english": "Are there any physical heavy lifting restrictions during the upcoming recovery period?", "chinese": "在接下来的身体康复恢复期内，有什么关于提拿重物的禁忌限制吗？"},
                {"english": "Do not lift any heavy objects weighing over ten pounds for four weeks.", "chinese": "在未来四周之内，严禁提拿搬运任何重量超过十磅的重物。"},
                {"english": "Light walking exercise is strongly recommended to enhance blood circulation and avoid clots.", "chinese": "强烈建议进行适量轻度散步活动，以促进全身血液循环并预防下肢血栓。"},
                {"english": "The hospital wheelchair service is ready to escort you down to your taxi.", "chinese": "医院轮椅护送服务人员已准备就绪，可以一路护送您下楼直到坐上的士。"},
                {"english": "The inpatient pharmacy has delivered all your take-home recovery medications right here.", "chinese": "住院部药房已将您全部的出院带回家康复药物直接送到了床前。"},
                {"english": "Thank you deeply to all the compassionate nurses and doctors for saving my life.", "chinese": "由衷深切感谢所有充满仁爱之心的护士和医生们挽救了我的生命。"},
                {"english": "It was our absolute honor and privilege to take care of your health.", "chinese": "能为您的身体健康保驾护航，是我们全体医护人员由衷的荣幸与职责所在。"},
                {"english": "Take gentle care of yourself, and have a safe, healthy journey back home.", "chinese": "请多多珍重保重身体，祝您归家途上一路平安顺遂、永葆安康！"}
            ]
        }
    ]
}

COURSE_SCENE_INTERVIEW = {
    "meta": {
        "id": "scene-interview",
        "title": "外企英文求职面试",
        "category": "scenes",
        "difficulty": "初级·实用",
        "description": "破冰寒暄、职业背景、STAR核心项目经验、薪资谈判到向考官提问的外企求职通关秘籍。",
        "cover": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=600&auto=format&fit=crop&q=80",
        "tag": "职场发展"
    },
    "chapters": [
        {
            "id": "ch1", "title": "第1章：开场破冰与职业寒暄",
            "sentences": [
                {"english": "Good morning, Ms. Jenkins, thank you very much for inviting me for this interview.", "chinese": "詹金斯女士早上好，非常感谢您邀请我参加今天的这场求职面试。"},
                {"english": "It is an absolute pleasure to meet you; thank you for taking the time.", "chinese": "能与您见面真是我的莫大荣幸；由衷感谢您百忙之中抽出宝贵时间。"},
                {"english": "Did you have any difficulty finding our corporate headquarters building this morning?", "chinese": "今天早晨找我们公司总部大厦的路上还顺利吗，有没有遇到什么困难？"},
                {"english": "Not at all; your transportation directions provided in the invitation email were exceptionally clear.", "chinese": "完全没有，您在邀请邮件中附带的交通指引路线写得异常清晰明了。"},
                {"english": "Would you care for a glass of water, fresh coffee, or hot tea?", "chinese": "您想喝杯温水、新鲜现煮咖啡还是热茶润润喉咙？"},
                {"english": "A glass of water would be wonderful, thank you very much indeed.", "chinese": "来一杯温水就太好了，真的非常感谢您。"},
                {"english": "I have been following your company's innovative technological breakthroughs in AI with admiration.", "chinese": "我一直怀着由衷的钦佩与关注，紧跟贵司在人工智能领域取得的突破性创新。"},
                {"english": "We are thrilled to explore how your professional background aligns with our open vacancy.", "chinese": "我们非常期待深入探讨您的专业背景如何与我们当前的招聘岗位完美契合。"},
                {"english": "I have prepared three printed copies of my updated curriculum vitae and portfolio.", "chinese": "我随身打印准备了三份我最新更新的个人中英文简历以及作品集。"},
                {"english": "Today's interview discussion will last approximately forty-five minutes covering technical and leadership competencies.", "chinese": "今天的面试交流大约持续四十五分钟，将全面涵盖专业技术能力与领导力胜任力。"},
                {"english": "Please feel completely relaxed and treat this conversation as a mutual bilateral exchange.", "chinese": "请您完全放松心情，把我们今天的谈话当作一场彼此平等的双向交流。"},
                {"english": "I am eager to share my career journey and learn more about your team.", "chinese": "我非常热切地渴望分享我的职业成长历程，并进一步了解贵团队的远大蓝图。"},
                {"english": "We appreciate candidates who demonstrate genuine intellectual curiosity and passion for our industry.", "chinese": "我们非常欣赏那些对我们所处行业展现出纯粹求知欲与无限热情的优秀候选人。"},
                {"english": "Let us begin by having you walk through your professional journey and key milestones.", "chinese": "那么就让我们从请您系统梳理一下您的职业发展轨迹和关键里程碑开始吧。"},
                {"english": "I would be delighted to guide you through my professional evolution and accomplishments.", "chinese": "我非常高兴能为您深入梳理并讲解我的专业进阶轨迹与核心职场成就。"}
            ]
        },
        {
            "id": "ch2", "title": "第2章：精彩自我介绍与职业主线",
            "sentences": [
                {"english": "Could you please tell me about yourself and summarize your professional career background?", "chinese": "能请您做个自我介绍，并高度概括一下您的专业职业背景经历吗？"},
                {"english": "I am a full-stack software engineer with over six years of enterprise development experience.", "chinese": "我是一名拥有超过六年大型企业级软件研发实战经验的全栈软件工程师。"},
                {"english": "Throughout my career, I have specialized in building scalable, distributed cloud computing architectures.", "chinese": "在我的整个职业生涯中，我专注于构建高可用、可弹性扩展的分布式云计算系统架构。"},
                {"english": "I graduated with a master's degree in computer science from Shanghai Jiao Tong University.", "chinese": "我硕士毕业于上海交通大学计算机科学与技术专业，获得了工学硕士学位。"},
                {"english": "In my previous role at TechCorp, I led a cross-functional squad of eight developers.", "chinese": "在上一家科技公司任职期间，我带领着一个由八名研发人员组成的跨职能敏捷战队。"},
                {"english": "My core technical stack encompasses TypeScript, React, Node.js, Python, and AWS infrastructure.", "chinese": "我的核心底层技术栈主要涵盖TypeScript、React、Node.js、Python以及AWS云基础设施。"},
                {"english": "I pride myself on bridging technical complexity with tangible business value for corporate stakeholders.", "chinese": "我引以为傲的核心优势在于能将复杂深奥的技术方案转化为利益相关方可见的商业价值。"},
                {"english": "I spearheaded the microservices redesign that improved our platform's throughput by 300%.", "chinese": "我主导推进了微服务化架构重构，将我们整体平台的系统吞吐量大幅提升了百分之三百。"},
                {"english": "Beyond coding, I am deeply committed to mentoring junior colleagues and championing code quality.", "chinese": "在编写代码之外，我全身心投入于指导初级年轻同事成长，并不遗余力捍卫代码卓越品质。"},
                {"english": "What drives my enthusiasm is tackling high-impact ambiguous challenges that empower millions of users.", "chinese": "驱动我内心无尽工作激情的，是去攻克那些具有高影响力、高模糊度、能赋能数百万用户的挑战。"},
                {"english": "I have long admired your enterprise culture emphasizing continuous innovation and radical ownership.", "chinese": "我长期以来极其钦佩贵公司所倡导的持续自我革新以及彻底的主人翁担当精神文化。"},
                {"english": "My background aligns directly with the requirements outlined for this Senior Engineering Manager position.", "chinese": "我的能力背景与贵司本次招聘的高级研发工程经理职位所列的各项要求高度契合。"},
                {"english": "I bring not only robust technical expertise but also proven international team leadership capabilities.", "chinese": "我带来的不仅是深厚扎实的硬核技术功底，更是经过实战检验的跨国跨文化团队领导力。"},
                {"english": "I am seeking a role where I can build world-class products alongside exceptional talents.", "chinese": "我正在寻找一个能够与卓越顶尖人才并肩作战、一同铸就世界级伟大产品的职业舞台。"},
                {"english": "That is an overarching summary of my professional foundation, and I welcome deeper questions.", "chinese": "以上就是关于我专业底色与职业基石的全局概括，非常欢迎您针对具体细节深入提问。"}
            ]
        },
        {
            "id": "ch3", "title": "第3章：核心项目经验与STAR法则",
            "sentences": [
                {"english": "Could you walk me through the most challenging project you delivered using STAR methodology?", "chinese": "您能运用STAR法则，为我详细拆解您主导交付过的最具挑战性的核心项目吗？"},
                {"english": "The Situation: Our legacy payment gateway was suffering from high latency and frequent timeouts.", "chinese": "情境（S）：当时我们的老旧支付网关深陷高延迟泥潭，且在交易高峰期频繁发生接口超时。"},
                {"english": "The Task: I was tasked with re-architecting the payment pipeline within three tight months.", "chinese": "任务（T）：我受命挂帅在短短三个月的极度紧迫周期内，对整套核心支付管道进行彻底重构。"},
                {"english": "The Action: I implemented an asynchronous event-driven architecture using Kafka message queuing and Redis.", "chinese": "行动（A）：我主导落地了基于Kafka消息队列与分布式Redis缓存的高并发异步事件驱动架构。"},
                {"english": "I decoupled the monolithic database bottleneck into independently scalable transactional microservices.", "chinese": "我将原本庞大拥挤的单体数据库性能瓶颈解耦拆分为支持独立横向扩容的事务型微服务。"},
                {"english": "To ensure zero downtime during migration, I instituted a blue-green canary deployment strategy.", "chinese": "为了在架构迁移全过程中确保业务零宕机，我制定并推行了严密的蓝绿金丝雀灰度发布策略。"},
                {"english": "I authored comprehensive end-to-end integration tests to safeguard financial accuracy across every transaction.", "chinese": "我主笔编写了全覆盖的端到端集成测试套件，以此誓死捍卫每笔资金交易账目的百分之百精准。"},
                {"english": "The Result: We slashed average transaction latency from 1.8 seconds down to 120 milliseconds.", "chinese": "结果（R）：我们成功将平均交易耗时延迟从原先的1.8秒断崖式骤降至仅需120毫秒。"},
                {"english": "Our new payment engine successfully processed fifty million dollars during the subsequent Black Friday.", "chinese": "我们崭新的高可用支付引擎在接下来的“黑色星期五”大促期间顺畅处理了五千万美元交易额。"},
                {"english": "System availability reached 99.999% uptime with zero critical production incidents reported.", "chinese": "整体系统可用性高标准达成了99.999%的高可用指标，期间未报告哪怕一起重大线上故障。"},
                {"english": "This success earned our engineering squad the annual corporate Excellence in Innovation Award.", "chinese": "这项具有里程碑意义的卓越战果，使我们研发战队荣膺了集团年度“卓越创新大奖”最高殊荣。"},
                {"english": "How did you manage technical debt while balancing pressing product release roadmaps?", "chinese": "在兼顾追赶紧迫的产品发布上线路线图的同时，您是如何科学治理沉重技术债务的？"},
                {"english": "I negotiated allocating twenty percent of each sprint capacity specifically toward architecture hardening.", "chinese": "我与产品团队达成共识，在每个敏捷迭代冲刺中严格划拨百分之二十的工时专门用于架构加固。"},
                {"english": "Prioritizing technical investments proactively prevented catastrophic system outages down the road.", "chinese": "在技术演进上未雨绸缪地主动前置投资，在后续发展中成功避免了灾难性的线上系统崩塌。"},
                {"english": "Clear metric-driven outcomes validate that robust engineering rigor directly drives commercial growth.", "chinese": "清晰的数据驱动结果无可辩驳地证实：严谨过硬的工程底蕴是直接驱动商业爆发的核心引擎。"}
            ]
        },
        {
            "id": "ch4", "title": "第4章：团队协作与冲突解决",
            "sentences": [
                {"english": "Can you describe a situation where you had a significant disagreement with a colleague?", "chinese": "您能描述一次您与同事或业务伙伴产生重大意见分歧但最终妥善化解的经历吗？"},
                {"english": "In my previous project, the principal product manager and I differed on feature prioritization.", "chinese": "在之前的项目中，资深产品总监与我在下一阶段功能开发的优先级排序上产生了严重分歧。"},
                {"english": "He advocated rushing an unpolished AI feature to beat competitors to market launch.", "chinese": "他主张不惜代价抢先将一个尚未完全打磨成熟的AI功能强行推向市场，以争抢首发先机。"},
                {"english": "I was concerned that immature model accuracy would damage customer brand trust irreparably.", "chinese": "而我则深感担忧，模型识别准确率的过早暴露极可能对客户长久以来的品牌信任造成不可逆损伤。"},
                {"english": "Instead of engaging in emotional arguing, I arranged a dedicated data-driven review session.", "chinese": "我没有陷入情绪化的争执对立，而是主动发起并组织了一场基于客观数据实证的专项研讨会。"},
                {"english": "I ran rapid A/B testing with a closed cohort of one hundred beta customers.", "chinese": "我组织了一个由一百位核心种子内测用户组成的小闭环实验组，迅速开展了A/B对比测试。"},
                {"english": "The beta metrics clearly revealed a 40% frustration drop-off rate on inaccurate responses.", "chinese": "灰度内测的真实数据残酷而清晰地暴露出：不精准的AI应答导致了高达百分之四十的挫败流失率。"},
                {"english": "Armed with empirical data, we collaboratively devised a phased, staged rollout milestone plan.", "chinese": "凭借客观实证数据的有力支撑，我们心平气和地协同制定出了一套分阶段稳步推进的里程碑方案。"},
                {"english": "We released the feature marked as 'Beta Experimental' to manage user expectations properly.", "chinese": "我们在功能上方显眼标注“实验内测版”字样，从而有效管理并对齐了用户的心理预期。"},
                {"english": "Meanwhile, the algorithms team received three additional weeks to optimize classification precision.", "chinese": "与此同时，算法团队赢得了额外宝贵的三周优化时间，成功将分类识别精准度大幅拉升。"},
                {"english": "When the final version launched broadly, customer satisfaction scores reached an all-time high.", "chinese": "当打磨成熟的终版全量面向大众推开时，客户整体净推荐值满意度得分创下了历史最高峰。"},
                {"english": "This experience reinforced my belief that data and empathy dismantle interpersonal friction.", "chinese": "这次经历深刻坚定了我的信条：客观事实数据配合换位同理心，是消弭一切人际摩擦的终极钥匙。"},
                {"english": "I always focus discussions objectively on overarching team goals rather than personal egos.", "chinese": "在面对任何争议分歧时，我永远坚持对事不对人，始终聚焦团队大局目标而非个人虚荣私利。"},
                {"english": "Healthy constructive debate is the absolute lifeblood of high-performing collaborative organizations.", "chinese": "健康而富有建设性的充分辩论与交锋，恰恰是打造卓越高绩效协同组织的真正生命源泉所在。"},
                {"english": "Mutual psychological safety allows every squad member to voice dissenting views constructively.", "chinese": "彼此信任的心理安全感土壤，让团队里的每一位成员都敢于建设性地发出理性不同的反对声音。"}
            ]
        },
        {
            "id": "ch5", "title": "第5章：应对挑战与挫折复盘",
            "sentences": [
                {"english": "Tell me about a time you experienced a significant failure in your career.", "chinese": "请告诉我一次您在以往职业生涯中遭遇过的重大失败或严重挫折的经历。"},
                {"english": "How did you handle the fallout and what key lessons did you internalize?", "chinese": "当时您是如何控制并收拾不良后果局面的，从中您又沉淀内化了哪些至关重要的教训？"},
                {"english": "Early in my career as a tech lead, I underestimated database migration scale.", "chinese": "在我初次担任技术负责人的职业早期，我严重低估了一次海量数据库迁移的规模复杂度。"},
                {"english": "A routine database index rebuild locked production tables for over two agonizing hours.", "chinese": "一次看似常规的数据库索引重建操作，意外导致线上核心生产库表被锁死了整整两个漫长小时。"},
                {"english": "Customers were unable to complete checkout orders during peak afternoon trading hours.", "chinese": "在下午最黄金的交易高峰期，大量付费客户无法正常完成最终的结账下单流程。"},
                {"english": "I immediately owned complete personal accountability without deflecting blame onto junior teammates.", "chinese": "在事故发生的第一时间，我毫无借口地承担起全部个人责任，绝不把锅甩给年轻的下属。"},
                {"english": "I coordinated the incident command channel and rolled back the lock safely.", "chinese": "我沉着坐镇统筹线上紧急故障处置指挥专线，安全稳妥地将引发阻塞的锁表变更回滚。"},
                {"english": "Following resolution, I drafted a blameless post-mortem report analyzing root structural causes.", "chinese": "在故障彻底排除后，我通宵主笔撰写了一份不追责的深度复盘报告，彻查底层根因。"},
                {"english": "We identified gaps in our staging environment data volume compared to production scale.", "chinese": "我们敏锐查明了准生产测试环境在数据体量上与线上真实千万级规模存在的严重脱节断层。"},
                {"english": "I instituted mandatory production change guardrails, automated shadow migrations, and automated rollbacks.", "chinese": "我主导推行了强制性的生产变更红线护栏、自动化影子环境压力演练以及自动回滚熔断机制。"},
                {"english": "We never experienced a database indexing outage in our department ever again.", "chinese": "在此后的岁月里，我们整个技术研发大部门再也没有发生过一起哪怕轻微的索引锁表事故。"},
                {"english": "That costly mistake transformed me into a profoundly rigorous, risk-aware systems architect.", "chinese": "正是那次代价惨痛的严重失误，将我真正淬炼蜕变成为一名极度严谨求实、深具风险敬畏心的系统架构师。"},
                {"english": "Failure is never pleasant, but transparent blameless retrospective turns setbacks into institutional wisdom.", "chinese": "遭遇挫败固然令人扼腕，但公开透明、不咎既往的深耕复盘能将跌倒的教训铸成团队宝贵的制度智慧。"},
                {"english": "Resilience and psychological grit define an engineer's ultimate long-term professional trajectory.", "chinese": "在挫折面前展现出的坚韧抗逆力与心理韧性，最终决定了一名优秀工程师能达到的职业巅峰高度。"},
                {"english": "Every unexpected crisis carries the seeds of profound operational and personal evolution.", "chinese": "每一场始料未及的严峻危机深处，其实都蕴藏着催化系统体系与个人心智脱胎换骨的进化火种。"}
            ]
        },
        {
            "id": "ch6", "title": "第6章：领导力与人才培养",
            "sentences": [
                {"english": "What is your philosophy when it comes to leading and mentoring software engineers?", "chinese": "当谈及领导研发团队以及辅导培养年轻软件工程师时，您的核心管理哲学是什么？"},
                {"english": "I practice servant leadership: my primary responsibility is clearing obstacles for my team.", "chinese": "我始终践行仆人式领导理念：作为管理者，我的天职就是为一线研发团队扫清一切障碍绊脚石。"},
                {"english": "I believe in granting high autonomy coupled with absolute transparency and clear accountability.", "chinese": "我坚定崇尚给予下属充分的高度自主权，同时辅以绝对公开透明的信息共享和清晰的权责对齐。"},
                {"english": "I hold weekly dedicated one-on-one sessions focused purely on personal career development.", "chinese": "我坚持每周为每位组员设立专属一对一深度沟通时段，完全聚焦于他们个人的长期职业成长路径。"},
                {"english": "I mentored a struggling junior developer into becoming a confident tech lead in eighteen months.", "chinese": "我曾悉心辅导一位刚入行时磕磕绊绊的初级新人，在短短一年半内蜕变成为独当一面的技术骨干。"},
                {"english": "I achieved this by breaking complex system architectures into incremental, digestible learning milestones.", "chinese": "我实现这一点的秘诀，在于善于把庞杂庞大的系统架构拆解为循序渐进、易于消化吃透的进阶里程碑。"},
                {"english": "I encouraged her to speak at our engineering all-hands and lead design reviews.", "chinese": "我不断鼓励她登上我们技术研发全员大会的讲台做技术分享，并放手让她主持架构评审会。"},
                {"english": "True leadership is measured not by followers, but by how many leaders you cultivate.", "chinese": "真正卓越的领导力从来不是看你身后跟随着多少随从，而是衡量于你亲手培养孵化出了多少名领袖。"},
                {"english": "How do you handle underperformance within your software engineering teams?", "chinese": "当您麾下的研发团队中出现绩效不达标、表现落后的成员时，您通常如何妥善处置？"},
                {"english": "I initiate candid, compassionate conversations early to diagnose underlying blockers and personal challenges.", "chinese": "我会在萌芽期尽早发起坦诚而充满关怀的面对面交谈，深挖背后的工作阻碍或个人生活困境。"},
                {"english": "Together, we co-create a concrete thirty-day performance improvement plan with weekly measurable milestones.", "chinese": "我们会携手共同制定一份明确清晰的三十天绩效提升改进计划，并设立每周可量化的考核节点。"},
                {"english": "If an individual shows genuine dedication, I invest heavily in providing tailored coaching.", "chinese": "只要当事人展现出脚踏实地改变的由衷决心，我就会倾注极大心血为其提供量身定制的专属指导。"},
                {"english": "Clear expectations and empathetic feedback frequently inspire remarkable turnarounds in disengaged teammates.", "chinese": "毫不含糊的清晰期望加上设身处地的同理心反馈，往往能够奇迹般唤醒消沉低迷员工的无限潜能。"},
                {"english": "Recognizing and publicly celebrating small wins cultivates an environment of collective psychological pride.", "chinese": "敏锐捕捉并在全组公开嘉奖每一个细微的阶段性胜利，能在团队中孕育出强大的集体心理自豪感。"},
                {"english": "A cohesive, empowered engineering culture naturally attracts and retains world-class technical talent.", "chinese": "一个紧密团结、深受赋能信任的工程师文化土壤，自然而然会源源不断吸引并留住全球顶尖英才。"}
            ]
        },
        {
            "id": "ch7", "title": "第7章：职业规划与未来愿景",
            "sentences": [
                {"english": "Where do you envision yourself professionally over the next three to five years?", "chinese": "放眼未来三到五年时间跨度，您对自己有着怎样的专业发展蓝图与职业定位设想？"},
                {"english": "In the short term, I aim to master your core business domain architecture thoroughly.", "chinese": "在短期内，我的首要目标是全面深入吃透贵司核心业务领域的底层系统架构与行业机理。"},
                {"english": "I intend to deliver high-visibility product initiatives that measurably move company revenue needles.", "chinese": "我渴望挂帅交付几项极具公司战略能见度的重量级产品攻坚项目，切实以数据拉升公司的商业营收。"},
                {"english": "Over the medium term, I see myself growing into a Director of Engineering role.", "chinese": "在中期规划中，我期望自己能稳步成长并晋升为统领全局的研发工程总监（Director）角色。"},
                {"english": "I want to lead multi-team engineering organizations spanning dozens of world-class technical professionals.", "chinese": "我希望能够统筹带领跨多业务线的研发矩阵大团队，麾下汇聚数十位国际一流的硬核技术专家。"},
                {"english": "I am passionate about driving technical strategy, organizational topology, and engineering culture at scale.", "chinese": "我对于在宏观层面制定前瞻技术战略演进、优化组织架构拓扑以及规模化塑造工程师文化充满极高热情。"},
                {"english": "I plan to contribute actively to open-source communities representing your brand internationally.", "chinese": "我计划积极代表贵司品牌深度参与全球主流开源社区的共建，在国际顶会舞台上传播技术影响力。"},
                {"english": "How does this specific vacancy align with your long-range career progression trajectory?", "chinese": "目前我们这个空缺招聘岗位，与您深远的长期职业生涯进阶轨迹是如何形成战略契合的？"},
                {"english": "This position offers the exact intersection of cutting-edge technology and massive consumer scale.", "chinese": "这个核心职位恰好处于前沿尖端硬核技术与海量超级C端用户规模的完美黄金交叉十字路口。"},
                {"english": "Your rapid global expansion presents the precise architectural challenges I am primed to solve.", "chinese": "贵司当前雄心勃勃的全球化飞速扩张步伐，恰好抛出了我长期以来蓄势待发、最渴望攻克的大型系统挑战。"},
                {"english": "I want to plant my roots in an organization whose mission resonates with me.", "chinese": "我由衷渴望在一家企业使命与我内心底层价值观产生深刻强烈共鸣的参天大树型组织中深深扎根。"},
                {"english": "Continuous lifelong learning is the compass that guides my ongoing professional development trajectory.", "chinese": "永不止步的终身学习与知行合一，是我在整条漫长职业发展征途中永不偏航的定向指南针。"},
                {"english": "I seek an environment that constantly challenges my capabilities and rewards courageous experimentation.", "chinese": "我孜孜以求一个能持续向我的舒适区极限发起挑战、且鼓励并奖赏无畏探索创新的肥沃环境。"},
                {"english": "I am confident that my contribution here will leave an enduring positive imprint.", "chinese": "我怀有无比充盈的自信：我在这里全情付出的智慧与心血，必将为公司烙下历久弥新的光辉印记。"},
                {"english": "The road ahead is full of potential, and I am ready to conquer it.", "chinese": "通往未来的征程充满了无穷无尽的星辰大海与机遇，而我已整装待发、随时准备奔赴战场！"}
            ]
        },
        {
            "id": "ch8", "title": "第8章：薪资福利与录用谈判",
            "sentences": [
                {"english": "What are your total compensation expectations for this senior engineering leadership role?", "chinese": "针对这个资深研发技术领导岗位，您心目中期望的整体综合薪酬待遇标准大概是多少？"},
                {"english": "Based on market benchmarks for senior staff engineers in this metropolitan tech region...", "chinese": "基于本一线大都市高科技核心园区资深研发专家岗位目前的市场权威薪酬调研水平……"},
                {"english": "I am targeting a total annual package between one hundred sixty and one hundred eighty thousand.", "chinese": "我所期望的年度综合总包薪酬（Total Package）区间大致在十六万至十八万美元之间。"},
                {"english": "This figure includes base salary, annual performance bonus, and long-term equity stock grants.", "chinese": "这个预期总额包含了每年固定基本工资、年度绩效绩效奖金以及长期持有的股权期权激励。"},
                {"english": "Could you provide details regarding your standard corporate bonus structure and vesting schedules?", "chinese": "您能为我详细解读一下贵司标准的年终绩效奖金考核比例以及股票期权的逐年归属行权周期吗？"},
                {"english": "Our equity grants vest over four years with a one-year cliff of 25%.", "chinese": "我们公司的股票期权激励按四年周期均摊归属，首年满一年时按百分之二十五一次性行权归属。"},
                {"english": "What health insurance coverage, retirement matching, and paid leave allowances are included?", "chinese": "整体薪酬福利包中包含了哪些商业高端医疗保险覆盖、企业年金退休金匹配以及带薪年假天数？"},
                {"english": "We offer premium comprehensive healthcare for families and six percent 401k retirement matching.", "chinese": "我们为全体员工及直系家属提供高端全额医疗保障，并享有高达百分之六的企业年金全额按比例匹配。"},
                {"english": "Is there flexibility regarding remote work arrangements or a hybrid office working schedule?", "chinese": "在办公制度方面，贵司是否支持完全居家远程办公，或者采取灵活弹性的混合办公机制？"},
                {"english": "Our engineering staff works two days in the office and three days remotely.", "chinese": "我们技术研发团队目前常态化推行每周两天在公司办公室协作、三天自主居家远程办公。"},
                {"english": "Does the company provide an annual budget for continuous professional learning and conferences?", "chinese": "公司每年是否为员工专门设立有用于终身职业技能深造、图书购买及参加技术大会的津贴预算？"},
                {"english": "We allocate three thousand dollars annually for each engineer's professional development courses.", "chinese": "我们每年为每位研发工程师定额下拨三千美元的专项学习基金，用于支持其各类专业进修与考证。"},
                {"english": "Compensation is important, but finding the right cultural and technical fit is paramount.", "chinese": "丰厚的薪酬固然是衡量价值的重要标尺，但找到企业文化同频与技术理念相合的最佳土壤才是首要重中之重。"},
                {"english": "I am very open to constructive negotiation to arrive at a mutually rewarding agreement.", "chinese": "在待遇方面我始终抱着极其开放务实的态度，非常愿意通过建设性探讨达成彼此共赢的最终协议。"},
                {"english": "I look forward to reviewing the formal written offer letter from your human resources.", "chinese": "我满怀期待能够早日收到并审阅由贵司人力资源部正式签发的官方书面录用聘书（Offer）。"}
            ]
        },
        {
            "id": "ch9", "title": "第9章：向面试官提问与深度探讨",
            "sentences": [
                {"english": "We have covered a lot of ground today; what questions do you have for me?", "chinese": "今天我们深入交流探讨了许多核心维度；现在轮到您了，您有什么问题想向我提问的吗？"},
                {"english": "Thank you for the opportunity; I have prepared several thoughtful questions regarding the team.", "chinese": "非常感谢您给我这个提问机会；针对贵团队的未来发展与日常运作，我特意准备了几个深度问题。"},
                {"english": "What does a typical successful day look like for an engineer in this role?", "chinese": "如果从微观工作日常来看，一位在这个岗位上表现极其卓越的工程师，充实成功的一天通常是如何度过的？"},
                {"english": "What is the single biggest architectural technical bottleneck your team is grappling with currently?", "chinese": "如果只能选一个，贵团队当前在系统架构和技术层面正在全力攻坚克难的最大瓶颈痛点是什么？"},
                {"english": "How would you describe the collaborative dynamic between product managers, designers, and engineers here?", "chinese": "您会如何描绘贵公司内部产品经理、UI设计专家与一线研发工程师之间的协同配合氛围与化学反应？"},
                {"english": "How does executive leadership balance shipping features rapidly versus paying down accumulated technical debt?", "chinese": "在管理层的战略博弈中，公司高管团队通常如何在争分夺秒抢推新业务功能与偿还积重难返的技术债之间达成平衡？"},
                {"english": "What specific metrics will be used to evaluate my performance during the first ninety days?", "chinese": "在入职后至关重要的前九十天磨合期内，公司将主要依据哪些具体的量化指标来衡量我的阶段性产出与表现？"},
                {"english": "What opportunities exist for engineers to transition between different technology stacks and business domains?", "chinese": "贵司内部对于工程师在不同业务领域、技术栈甚至跨国跨部门之间的内部转岗与轮岗提供了怎样的空间与机制？"},
                {"english": "How has the engineering culture evolved as the company scaled beyond one thousand employees?", "chinese": "随着公司人员规模势如破竹般突破一千人大关，您亲身经历的整体工程师文化经历了怎样微妙而深远的演进？"},
                {"english": "What is the next frontier technology breakthrough your executive team is most excited about?", "chinese": "放眼未来科技产业风口，目前最令贵公司核心高管层感到彻夜难眠、兴奋不已的下一个技术颠覆点是什么？"},
                {"english": "What do you personally enjoy most about working at this innovative enterprise?", "chinese": "如果从您个人的切身心声出发，您自己在这个充满创新活力的大型组织中最享受、最深爱的特质是什么？"},
                {"english": "These thoughtful questions demonstrate your profound strategic understanding of software engineering organizations.", "chinese": "您提出的这几个深思熟虑的深刻问题，充分彰显了您对大型软件工程组织机理所拥有的宏观战略认知与敏锐洞察。"},
                {"english": "Your insightful answers have given me immense confidence in your team's inspiring vision.", "chinese": "您刚刚坦诚深刻且极具远见的精彩解答，使我对贵团队所勾勒的宏伟蓝图产生了无可动摇的坚定信心。"},
                {"english": "I am more convinced than ever that this is where I can thrive.", "chinese": "此时此刻的我比以往任何时候都更加深信不疑：这里就是能让我大展宏图、如鱼得水的理想沃土！"},
                {"english": "Thank you for being so remarkably candid, articulate, and welcoming throughout our conversation.", "chinese": "在整个面试交流的全程中，真诚感谢您始终展现出的非凡坦荡、高超表达以及令人如沐春风的温暖接待。"}
            ]
        },
        {
            "id": "ch10", "title": "第10章：面试总结与诚挚致谢",
            "sentences": [
                {"english": "Thank you once again for taking the time to meet with me today.", "chinese": "在今天的面试画上圆满句号之际，再次由衷感谢您拨冗与我进行了这场极其深入的对话。"},
                {"english": "I enjoyed learning about your architectural challenges and ambitious product plans for next year.", "chinese": "我非常享受聆听并了解贵团队当前面临的架构瓶颈挑战，以及明年度充满雄心的宏大产品拓展规划。"},
                {"english": "Our discussion has confirmed that my skills in distributed systems match your immediate needs.", "chinese": "我们刚才全面立体的交流再次有力佐证了：我在分布式高可用系统领域的深厚积累与贵司当前的当务之急完美嵌合。"},
                {"english": "What are the subsequent steps in your recruitment decision process from this point forward?", "chinese": "在接下来的招聘决策流程中，贵司后续的推进环节与关键时间节点大致是如何安排的？"},
                {"english": "Our hiring committee will review all feedback and contact you by next Tuesday.", "chinese": "我们的聘用评审委员会将在本周内汇总全面面试评估反馈，并在下周二之前正式与您取得联系。"},
                {"english": "If any additional portfolio materials or references are required, please do let me know.", "chinese": "如果在后续评估过程中需要我补充提交任何项目作品集支撑材料或背调推荐人联系方式，请随时指示。"},
                {"english": "I will send a formal thank-you follow-up email to your inbox this afternoon.", "chinese": "今天下午我会向您的工作邮箱正式发送一封写满致谢与复盘的跟进邮件（Thank-you Email）。"},
                {"english": "I remain exceptionally enthusiastic about the prospect of joining your world-class engineering organization.", "chinese": "对于未来有幸加入贵司这支世界级顶尖研发团队的美好前景，我始终保持着无与伦比的热切期待。"},
                {"english": "Your corporate values around extreme ownership and intellectual honesty deeply resonate with my own.", "chinese": "贵司所身体力行倡导的极致担当作为与绝对学术求真底色，与我内心的做人做事原则产生了深刻共鸣。"},
                {"english": "I am confident that my technical leadership will deliver tremendous tangible value from day one.", "chinese": "我怀有十足的底气与从容：凭借我的技术沉淀与带队能力，从入职第一天起就能为团队输出实实在在的硬核价值。"},
                {"english": "Please convey my sincere regards and appreciation to the other members of the interviewing panel.", "chinese": "请代我向刚才参与联合面试的其他几位面试官考官转达我诚挚由衷的问候与崇高谢意。"},
                {"english": "I will see you out to the lobby elevators; thank you for coming.", "chinese": "我送您去大堂客用电梯间门口；非常感谢您今天专程拨冗莅临我们公司面试。"},
                {"english": "It has been an absolute pleasure; have a productive remainder of your week.", "chinese": "能与您交流完全是我的荣幸与快乐；预祝您在本周接下来的工作与生活中收获满满、一切顺遂。"},
                {"english": "I eagerly await your recruitment update and hope to collaborate with you soon.", "chinese": "我满怀期待静候贵司的进一步复试或录用进展通知，并深切期盼在不久的将来能与各位携手并肩作战。"},
                {"english": "Goodbye for now, take great care, and have a wonderful pleasant day!", "chinese": "暂且告辞，再见，请您多多保重，祝您度过美好舒心的一天！"}
            ]
        }
    ]
}

print("COURSE_SCENE_HOSPITAL, INTERVIEW ready")
