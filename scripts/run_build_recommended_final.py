# -*- coding: utf-8 -*-
"""
统合推荐精选全部 8 门课程，通过全局查重写入 src/data/mall/recommended.ts
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

import builder_core as b
from gen_recommended_part1 import COURSE_REC_SPOKEN_GOLD, COURSE_REC_AMERICAN_THINKING
from gen_recommended_part2 import COURSE_REC_HIGH_EQ_SOCIAL, COURSE_REC_MOVIE_CLASSICS
from gen_recommended_part3 import COURSE_REC_NATIVE_IDIOMS, COURSE_REC_BUSINESS_PRESENTATION
from gen_recommended_part4 import COURSE_REC_STUDY_ABROAD, COURSE_REC_DAILY_MOTTO

def normalize_course_input(c):
    if "meta" in c:
        meta = c["meta"]
    else:
        meta = {
            "id": c["id"],
            "title": c["title"],
            "description": c.get("desc") or c.get("description", ""),
            "category": c.get("category", "recommended"),
            "categoryName": c.get("categoryName", "推荐"),
            "coverGradient": c.get("coverGradient", "from-amber-500 to-rose-600"),
            "icon": c.get("icon", "🌟"),
            "difficulty": c.get("difficulty", "中级 B1"),
            "tags": c.get("tags", ["推荐"])
        }
    return meta, c["chapters"]

def main():
    print("=== 开始生成推荐精选分类全部 8 门高品质课程 ===")
    b.preload_existing_mall_files()
    print(f"当前全库已有句子基数: {len(b.global_seen_normalized)} 句")

    courses_raw = [
        COURSE_REC_SPOKEN_GOLD,
        COURSE_REC_AMERICAN_THINKING,
        COURSE_REC_HIGH_EQ_SOCIAL,
        COURSE_REC_MOVIE_CLASSICS,
        COURSE_REC_NATIVE_IDIOMS,
        COURSE_REC_BUSINESS_PRESENTATION,
        COURSE_REC_STUDY_ABROAD,
        COURSE_REC_DAILY_MOTTO
    ]

    built_courses = []
    for c in courses_raw:
        meta, chapters = normalize_course_input(c)
        built = b.build_course(meta, chapters)
        built_courses.append(built)

    b.save_ts_file("recommended", "RECOMMENDED_COURSES", built_courses)
    print(f"推荐精选处理完成！当前全库累计唯一句子数: {len(b.global_seen_normalized)} 句")

if __name__ == "__main__":
    main()
