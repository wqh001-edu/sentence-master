import re
import json
import os

GLOBAL_SEEN = set()
ALL_ITEMS = []

def normalize(text: str) -> str:
    return re.sub(r'[^a-z0-9]', '', text.lower().strip())

def make_sentence(en: str, cn: str, course_title: str, chapter_title: str):
    en_clean = en.strip()
    cn_clean = cn.strip()
    norm = normalize(en_clean)
    
    if len(norm) > 4:
        if norm in GLOBAL_SEEN:
            prev = next((s for s in ALL_ITEMS if s['norm'] == norm), None)
            loc = f"《{prev['course']}》- {prev['chapter']}" if prev else "未知"
            raise ValueError(f"【重复拦截】句子重复！\n重复文本: \"{en_clean}\"\n首次出现: {loc}\n当前位置: 《{course_title}》- {chapter_title}")
        GLOBAL_SEEN.add(norm)
        ALL_ITEMS.append({'norm': norm, 'en': en_clean, 'course': course_title, 'chapter': chapter_title})
        
    return {"english": en_clean, "chinese": cn_clean}

def build_package(meta: dict, chapters_raw: list) -> dict:
    course_id = meta["id"]
    course_title = meta["title"]
    chapters = []
    
    for ch_idx, ch in enumerate(chapters_raw):
        ch_id = f"{course_id}-ch{ch_idx + 1}"
        ch_title = ch["title"]
        ch_desc = ch.get("description", "")
        raw_sents = ch["sentences"]
        
        if len(raw_sents) < 15:
            raise ValueError(f"章节《{course_title}》- {ch_title} 句子数仅为 {len(raw_sents)}，未达 15 句！")
            
        sentences = []
        for s_idx, s in enumerate(raw_sents[:15]):
            s_id = f"{ch_id}-s{s_idx + 1}"
            checked = make_sentence(s["en"], s["cn"], course_title, ch_title)
            sentences.append({
                "id": s_id,
                "english": checked["english"],
                "chinese": checked["chinese"]
            })
            
        chapters.append({
            "id": ch_id,
            "title": ch_title,
            "description": ch_desc,
            "sentences": sentences
        })
        
    return {
        "id": course_id,
        "title": course_title,
        "category": meta["category"],
        "categoryName": meta["categoryName"],
        "coverGradient": meta["coverGradient"],
        "icon": meta["icon"],
        "description": meta["description"],
        "difficulty": meta["difficulty"],
        "tags": meta["tags"],
        "chapters": chapters
    }

def save_ts(category_id: str, var_name: str, courses: list):
    output_path = os.path.join("src", "data", "mall", f"{category_id}.ts")
    content = f"""import type {{ CoursePackage }} from '../../types';

export const {var_name}: CoursePackage[] = {json.dumps(courses, ensure_ascii=False, indent=2)};
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    tot_ch = sum(len(c["chapters"]) for c in courses)
    tot_s = sum(sum(len(ch["sentences"]) for ch in c["chapters"]) for c in courses)
    print(f"📦 [已写入] {output_path.ljust(35)} | 课程: {len(courses)} 门 | 章节: {tot_ch} 个 | 句子: {tot_s} 句")
