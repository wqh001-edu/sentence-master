import re
import json
import os

# 全局去重集合与记录表
GLOBAL_SEEN = set()
ALL_RECORDS = []

def normalize_text(text: str) -> str:
    return re.sub(r'[^a-z0-9]', '', text.lower().strip())

def register_sentence(en: str, cn: str, course_title: str, chapter_title: str, ph: str = "", note: str = ""):
    en_clean = en.strip()
    cn_clean = cn.strip()
    norm = normalize_text(en_clean)
    
    if len(norm) > 4:
        if norm in GLOBAL_SEEN:
            prev = next((r for r in ALL_RECORDS if r['norm'] == norm), None)
            prev_loc = f"《{prev['course']}》- {prev['chapter']}" if prev else "未知"
            raise ValueError(f"【重复句子阻断】\n重复句子: \"{en_clean}\"\n首次位置: {prev_loc}\n再次出现: 《{course_title}》- {chapter_title}")
        GLOBAL_SEEN.add(norm)
        ALL_RECORDS.append({
            'norm': norm,
            'en': en_clean,
            'cn': cn_clean,
            'course': course_title,
            'chapter': chapter_title
        })
    return {"english": en_clean, "chinese": cn_clean, "phonetic": ph or None, "note": note or None}

def build_package(meta: dict, chapters_raw: list) -> dict:
    course_id = meta["id"]
    course_title = meta["title"]
    
    chapters = []
    for ch_idx, ch in enumerate(chapters_raw):
        ch_id = f"{course_id}-ch{ch_idx + 1}"
        ch_title = ch["title"]
        ch_desc = ch.get("description", "")
        sentences_raw = ch["sentences"]
        
        if len(sentences_raw) < 15:
            raise ValueError(f"章节《{course_title}》- {ch_title} 句子数为 {len(sentences_raw)}，少于 15 句！")
            
        sentences = []
        for s_idx, s in enumerate(sentences_raw[:15]): # 取前 15 句保证标准统一
            s_id = f"{ch_id}-s{s_idx + 1}"
            reg = register_sentence(s["en"], s["cn"], course_title, ch_title, s.get("ph", ""), s.get("note", ""))
            sentences.append({
                "id": s_id,
                "english": reg["english"],
                "chinese": reg["chinese"],
                "phonetic": reg["phonetic"],
                "note": reg["note"]
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

def save_ts(category_id: str, var_name: str, packages: list):
    output_path = os.path.join("src", "data", "mall", f"{category_id}.ts")
    content = f"""import type {{ CoursePackage }} from '../../types';

export const {var_name}: CoursePackage[] = {json.dumps(packages, ensure_ascii=False, indent=2)};
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    tot_ch = sum(len(c["chapters"]) for c in packages)
    tot_s = sum(sum(len(ch["sentences"]) for ch in c["chapters"]) for c in packages)
    print(f"📦 [已写入] {output_path.ljust(35)} | 课程: {len(packages)} 门 | 章节: {tot_ch} 个 | 句子: {tot_s} 句")
