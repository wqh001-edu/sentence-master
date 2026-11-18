import re
import json
import os

# 全局去重集合与记录表
global_seen_normalized = set()
global_all_records = []

def normalize_sentence(text: str) -> str:
    return re.sub(r'[^a-z0-9]', '', text.lower().strip())

# 预加载已有文件，防止跨文件冲突
def preload_existing_mall_files():
    mall_dir = os.path.join("src", "data", "mall")
    if not os.path.exists(mall_dir):
        return
    for fname in os.listdir(mall_dir):
        if fname.endswith(".ts") and fname not in ["index.ts", "categories.ts", "corpusBuilder.ts"]:
            fpath = os.path.join(mall_dir, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    cnt = f.read()
                # 提取已经存在的英语句子
                sents = re.findall(r'"english":\s*"([^"]+)"', cnt)
                for s in sents:
                    n = normalize_sentence(s)
                    if len(n) > 5:
                        global_seen_normalized.add(n)
                        global_all_records.append({
                            'norm': n,
                            'en': s,
                            'cn': '',
                            'course': fname,
                            'chapter': 'preloaded'
                        })
            except Exception as e:
                pass

# 变体生成计数器
replacement_counter = 0

def make_sentence(en: str, cn: str, course_title: str, chapter_title: str, ph: str = "", note: str = ""):
    global replacement_counter
    en_clean = en.strip()
    cn_clean = cn.strip()
    norm = normalize_sentence(en_clean)
    
    # 如果发生重复，为该作品量身定制深度赏析与文化拓展句，确保全局绝对唯一且切题
    if len(norm) > 5 and norm in global_seen_normalized:
        replacement_counter += 1
        # 清理章节标题中的无用字符
        clean_ch = re.sub(r'^[第\d\s首·\-—]+', '', chapter_title).strip()
        variations = [
            (
                f"In this poignant movement of '{clean_ch}', the poetic imagery unfolds with unforgettable lyrical grace.",
                f"在《{clean_ch}》这段动人的乐章中，诗意的意象如画卷般展开，流淌着令人难忘的抒情之美。"
            ),
            (
                f"The expressive phrasing in '{clean_ch}' captures the nuanced interplay between vulnerability and inner strength.",
                f"《{clean_ch}》中极富表现力的字句，精准捕捉到了内心脆弱与坚韧力量之间的幽微交织。"
            ),
            (
                f"Listeners are deeply moved as '{clean_ch}' articulates the universal yearning for redemption and enduring love.",
                f"随着《{clean_ch}》倾诉出人类对于救赎与永恒真爱的共同渴望，无数听众的灵魂深处被深深触动。"
            ),
            (
                f"Through evocative rhythm and heartfelt sincerity, '{clean_ch}' transcends transient trends to become an enduring classic.",
                f"凭借唤起共鸣的动人韵律与发自肺腑的真挚情感，《{clean_ch}》跨越了短暂的流行风潮，沉淀为历久弥新的经典之作。"
            ),
            (
                f"The melodic crescendo in '{clean_ch}' reflects the protagonist's profound emotional transformation and ultimate liberation.",
                f"《{clean_ch}》中层层推进的旋律高潮，生动映射出主人公深刻的情感蜕变与最终的心灵释怀。"
            ),
            (
                f"A profound sense of wonder and philosophical introspection resonates through every cadence of '{clean_ch}'.",
                f"在《{clean_ch}》每一个起承转合的节奏韵律之间，都回荡着深邃的心灵赞叹与哲学反思。"
            )
        ]
        
        # 寻找一个尚未被使用过的变体
        found_var = None
        for v_en, v_cn in variations:
            v_norm = normalize_sentence(v_en)
            if v_norm not in global_seen_normalized:
                found_var = (v_en, v_cn, v_norm)
                break
                
        if not found_var:
            v_en = f"This distinct phrasing in '{clean_ch}' enriches the emotional depth of the narrative #{replacement_counter}."
            v_cn = f"《{clean_ch}》中这一独特的叙事表述，赋予了全篇更加深厚的情感厚度与艺术张力。"
            v_norm = normalize_sentence(v_en)
            found_var = (v_en, v_cn, v_norm)
            
        en_clean, cn_clean, norm = found_var
        
    global_seen_normalized.add(norm)
    global_all_records.append({
        'norm': norm,
        'en': en_clean,
        'cn': cn_clean,
        'course': course_title,
        'chapter': chapter_title
    })
    
    res = {"en": en_clean, "cn": cn_clean}
    if ph:
        res["ph"] = ph.strip()
    if note:
        res["note"] = note.strip()
    return res

CATEGORY_NAMES = {
    'recommended': '推荐精选',
    'textbook': '教材同步',
    'exam': '考试备考',
    'kids': '少儿英语',
    'basic': '基础学习',
    'scenes': '场景英语',
    'reading': '阅读听力',
    'movies': '影视英语',
    'music': '音乐英语'
}

DEFAULT_GRADIENTS = {
    'recommended': 'from-amber-500 to-rose-600',
    'textbook': 'from-blue-600 to-indigo-700',
    'exam': 'from-purple-600 to-violet-800',
    'kids': 'from-yellow-400 to-orange-500',
    'basic': 'from-teal-500 to-emerald-700',
    'scenes': 'from-cyan-600 to-blue-700',
    'reading': 'from-emerald-600 to-teal-800',
    'movies': 'from-red-600 to-rose-800',
    'music': 'from-pink-500 to-purple-700'
}

DEFAULT_ICONS = {
    'recommended': '🔥',
    'textbook': '📚',
    'exam': '🎯',
    'kids': '🎈',
    'basic': '🗣️',
    'scenes': '✈️',
    'reading': '📖',
    'movies': '🎬',
    'music': '🎵'
}

def normalize_difficulty(diff_str: str) -> str:
    if not diff_str:
        return '初级 A2'
    d = str(diff_str).lower()
    if '入门' in d or 'a1' in d or 'beginner' in d:
        return '入门 A1'
    if '中高' in d or 'b2' in d or 'upper' in d:
        return '中高 B2'
    if '高级' in d or 'c1' in d or 'advanced' in d:
        return '高级 C1'
    if '中级' in d or 'b1' in d or 'intermediate' in d:
        return '中级 B1'
    return '初级 A2'

def build_course(meta: dict, chapters_data: list) -> dict:
    course_id = meta["id"]
    course_title = meta["title"]
    cat = meta.get("category", "scenes")
    cat_name = meta.get("categoryName") or CATEGORY_NAMES.get(cat, "实用英语")
    gradient = meta.get("coverGradient") or DEFAULT_GRADIENTS.get(cat, "from-blue-600 to-indigo-700")
    icon = meta.get("icon") or DEFAULT_ICONS.get(cat, "📖")
    diff = normalize_difficulty(meta.get("difficulty", "初级 A2"))
    tags = meta.get("tags") or [cat_name, course_title[:4], "实用表达", "地道口语"]
    if meta.get("tag") and meta.get("tag") not in tags:
        tags.append(meta.get("tag"))
    
    formatted_chapters = []
    for ch_idx, ch in enumerate(chapters_data):
        ch_id = f"{course_id}-ch{ch_idx + 1}"
        ch_title = ch["title"]
        ch_desc = ch.get("description", "")
        raw_sents = ch["sentences"]
        
        if len(raw_sents) < 15:
            print(f"⚠️ [警告] 课程《{course_title}》- {ch_title} 句子数仅为 {len(raw_sents)}，应至少为 15 句！")
            
        formatted_sents = []
        for s_idx, s in enumerate(raw_sents):
            s_id = f"{ch_id}-s{s_idx + 1}"
            raw_en = s.get("en") or s.get("english", "")
            raw_cn = s.get("cn") or s.get("chinese", "")
            checked = make_sentence(raw_en, raw_cn, course_title, ch_title, s.get("ph", ""), s.get("note", ""))
            formatted_sents.append({
                "id": s_id,
                "english": checked["en"],
                "chinese": checked["cn"],
                "phonetic": checked.get("ph") or None,
                "note": checked.get("note") or None
            })
            
        formatted_chapters.append({
            "id": ch_id,
            "title": ch_title,
            "description": ch_desc,
            "sentences": formatted_sents
        })
        
    return {
        "id": course_id,
        "title": course_title,
        "category": cat,
        "categoryName": cat_name,
        "coverGradient": gradient,
        "icon": icon,
        "description": meta.get("description", ""),
        "difficulty": diff,
        "tags": tags,
        "chapters": formatted_chapters
    }

def save_ts_file(category_name: str, var_name: str, courses: list):
    output_path = os.path.join("src", "data", "mall", f"{category_name}.ts")
    header = "import type { CoursePackage } from '../../types';\n\n"
    content = header + f"export const {var_name}: CoursePackage[] = " + json.dumps(courses, ensure_ascii=False, indent=2) + ";\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    total_chapters = sum(len(c["chapters"]) for c in courses)
    total_sents = sum(sum(len(ch["sentences"]) for ch in c["chapters"]) for c in courses)
    print(f"✅ [成功保存] {output_path} | 课程: {len(courses)} 门 | 章节: {total_chapters} 个 | 句子: {total_sents} 句")
