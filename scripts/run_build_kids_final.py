# -*- coding: utf-8 -*-
"""
统合少儿英语全部 8 门课程，通过全局查重写入 src/data/mall/kids.ts
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

import builder_core as b
from gen_kids_part1 import COURSE_KIDS_PHONICS
from gen_kids_part2 import COURSE_KIDS_DAILY, COURSE_KIDS_FAIRYTALE, COURSE_KIDS_ANIMALS
from gen_kids_part3 import COURSE_KIDS_COLORS, COURSE_KIDS_MANNERS
from gen_kids_part4 import COURSE_KIDS_SONGS, COURSE_KIDS_NATURE

def main():
    print("=== 开始生成少儿英语分类全部 8 门精品课程 ===")
    b.preload_existing_mall_files()
    print(f"当前全库已有句子基数: {len(b.global_seen_normalized)} 句")

    courses_raw = [
        COURSE_KIDS_PHONICS,
        COURSE_KIDS_DAILY,
        COURSE_KIDS_FAIRYTALE,
        COURSE_KIDS_ANIMALS,
        COURSE_KIDS_COLORS,
        COURSE_KIDS_MANNERS,
        COURSE_KIDS_SONGS,
        COURSE_KIDS_NATURE
    ]

    built_courses = []
    for c in courses_raw:
        built = b.build_course(c["meta"], c["chapters"])
        built_courses.append(built)

    b.save_ts_file("kids", "KIDS_COURSES", built_courses)
    print(f"少儿英语处理完成！当前全库累计唯一句子数: {len(b.global_seen_normalized)} 句")

if __name__ == "__main__":
    main()
