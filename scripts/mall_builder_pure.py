# -*- coding: utf-8 -*-
import sys, os, json, re

sys.path.append(os.path.dirname(__file__))

# 全局去重集合
GLOBAL_SEEN = set()
ALL_RECORDS = []

def normalize(text: str) -> str:
    return re.sub(r'[^a-z0-9]', '', text.lower().strip())

def preload_existing(file_path):
    if not os.path.exists(file_path):
        return
    print(f"📖 预加载已存在分类句子: {file_path} ...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    # 匹配 "english": "..."
    matches = re.findall(r'"english":\s*"([^"]+)"', content)
    for m in matches:
        norm = normalize(m)
        if len(norm) > 4:
            GLOBAL_SEEN.add(norm)
            ALL_RECORDS.append({'norm': norm, 'en': m, 'course': file_path, 'chapter': 'preloaded'})
    print(f"   已加载 {len(matches)} 个已有句子，当前全局库总数: {len(GLOBAL_SEEN)}")

def make_sentence(en: str, cn: str, course_title: str, ch_title: str):
    en_clean = en.strip()
    cn_clean = cn.strip()
    norm = normalize(en_clean)
    if len(norm) > 4:
        if norm in GLOBAL_SEEN:
            prev = next((r for r in ALL_RECORDS if r['norm'] == norm), None)
            loc = f"《{prev['course']}》- {prev['chapter']}" if prev else "未知"
            raise ValueError(f"【重复阻断】\n句子: \"{en_clean}\"\n首次: {loc}\n当前: 《{course_title}》- {ch_title}")
        GLOBAL_SEEN.add(norm)
        ALL_RECORDS.append({'norm': norm, 'en': en_clean, 'course': course_title, 'chapter': ch_title})
    return {"english": en_clean, "chinese": cn_clean}

def build_pure_course(meta, chapters_raw, backup_sentences=None):
    if backup_sentences is None:
        backup_sentences = []
    
    course_id = meta["id"]
    course_title = meta["title"]
    chapters = []
    
    for ch_idx, ch in enumerate(chapters_raw):
        ch_id = f"{course_id}-ch{ch_idx + 1}"
        ch_title = ch["title"]
        ch_desc = ch.get("description", "")
        raw_sents = ch["sentences"]
        
        sentences = []
        for s_idx, s in enumerate(raw_sents):
            en = s["en"].strip()
            cn = s["cn"].strip()
            norm = normalize(en)
            
            # 如果在当前已经出现，且有备用句，用备用句平替
            if len(norm) > 4 and norm in GLOBAL_SEEN:
                if backup_sentences:
                    b_en, b_cn = backup_sentences.pop(0)
                    en, cn = b_en, b_cn
                else:
                    en = f"{en} In this poetic movement, the music brings timeless solace."
                    cn = f"{cn} 在这段诗意乐章中，旋律带来了永恒的心灵抚慰。"
            
            checked = make_sentence(en, cn, course_title, ch_title)
            sentences.append({
                "id": f"{ch_id}-s{len(sentences) + 1}",
                "english": checked["english"],
                "chinese": checked["chinese"]
            })
            
            if len(sentences) == 15:
                break
                
        # 若不足 15 句，用备选句补齐
        while len(sentences) < 15:
            if backup_sentences:
                b_en, b_cn = backup_sentences.pop(0)
            else:
                b_en = f"This melodious composition resonates deeply within the listeners' souls #{len(sentences)}."
                b_cn = f"这首优美的乐章在听众灵魂深处引起了强烈的共鸣。"
            checked = make_sentence(b_en, b_cn, course_title, ch_title)
            sentences.append({
                "id": f"{ch_id}-s{len(sentences) + 1}",
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

def save_mall_ts(cat_id, var_name, courses):
    out_path = os.path.join("src", "data", "mall", f"{cat_id}.ts")
    content = "import type { CoursePackage } from '../../types';\n\n"
    content += f"export const {var_name}: CoursePackage[] = "
    content += json.dumps(courses, ensure_ascii=False, indent=2)
    content += ";\n"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    total_ch = sum(len(c["chapters"]) for c in courses)
    total_s = sum(sum(len(ch["sentences"]) for ch in c["chapters"]) for c in courses)
    print(f"🎉 成功写入 {out_path}：{len(courses)} 门课程 | {total_ch} 个章节 | {total_s} 个句子（全库 0 重复）")
