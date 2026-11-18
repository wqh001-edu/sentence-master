import os
import json
import re

# ==============================================================================
# 全局去重与校验引擎 (Zero-Duplication Engine)
# ==============================================================================
GLOBAL_SEEN = set()
ALL_SENTENCES = []

def normalize(text: str) -> str:
    return re.sub(r'[^a-z0-9]', '', text.lower().strip())

def make_sent(en: str, cn: str, course_name: str, chapter_name: str):
    en_clean = en.strip()
    cn_clean = cn.strip()
    norm = normalize(en_clean)
    
    if len(norm) > 4:
        if norm in GLOBAL_SEEN:
            prev = next((s for s in ALL_SENTENCES if s['norm'] == norm), None)
            loc = f"《{prev['course']}》- {prev['chapter']}" if prev else "未知"
            raise ValueError(f"【重复拦截】句子重复！\n重复文本: \"{en_clean}\"\n初次出现: {loc}\n当前位置: 《{course_name}》- {chapter_name}")
        GLOBAL_SEEN.add(norm)
        ALL_SENTENCES.append({'norm': norm, 'en': en_clean, 'course': course_name, 'chapter': chapter_name})
        
    return {"en": en_clean, "cn": cn_clean}

def build_course(meta: dict, chapters_raw: list) -> dict:
    course_id = meta["id"]
    course_title = meta["title"]
    chapters = []
    
    for ch_idx, ch in enumerate(chapters_raw):
        ch_id = f"{course_id}-ch{ch_idx + 1}"
        ch_title = ch["title"]
        ch_desc = ch.get("description", "")
        raw_sents = ch["sentences"]
        
        if len(raw_sents) < 15:
            raise ValueError(f"章节《{course_title}》- {ch_title} 句子数不足 15 句 (当前: {len(raw_sents)})")
            
        sentences = []
        for s_idx, s in enumerate(raw_sents[:15]): # 严格标准 15 句
            s_id = f"{ch_id}-s{s_idx + 1}"
            checked = make_sent(s["en"], s["cn"], course_title, ch_title)
            sentences.append({
                "id": s_id,
                "english": checked["en"],
                "chinese": checked["cn"]
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

def save_category_file(category_id: str, var_name: str, courses: list):
    output_path = os.path.join("src", "data", "mall", f"{category_id}.ts")
    content = f"""import type {{ CoursePackage }} from '../../types';

export const {var_name}: CoursePackage[] = {json.dumps(courses, ensure_ascii=False, indent=2)};
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    tot_ch = sum(len(c["chapters"]) for c in courses)
    tot_s = sum(sum(len(ch["sentences"]) for ch in c["chapters"]) for c in courses)
    print(f"✅ [成功生成] {output_path.ljust(35)} | 课程: {len(courses)} 门 | 章节: {tot_ch} 个 | 句子: {tot_s} 句")
