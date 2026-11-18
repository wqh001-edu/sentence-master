# -*- coding: utf-8 -*-
"""
统合阅读听力全部 8 门课程，通过全局查重写入 src/data/mall/reading.ts
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

import builder_core as b
from gen_reading_part1 import COURSE_READING_FABLES, COURSE_READING_BIOGRAPHY
from gen_reading_part2 import COURSE_READING_VOA, COURSE_READING_TED
from gen_reading_part3 import COURSE_READING_HISTORY, COURSE_READING_SCIENCE
from gen_reading_part4 import COURSE_READING_NATURE, COURSE_READING_WISDOM

def main():
    print("=== 开始生成阅读听力分类全部 8 门精品课程 ===")
    b.preload_existing_mall_files()
    print(f"当前全库已有句子基数: {len(b.global_seen_normalized)} 句")

    courses_raw = [
        COURSE_READING_FABLES,
        COURSE_READING_BIOGRAPHY,
        COURSE_READING_VOA,
        COURSE_READING_TED,
        COURSE_READING_HISTORY,
        COURSE_READING_SCIENCE,
        COURSE_READING_NATURE,
        COURSE_READING_WISDOM
    ]

    built_courses = []
    for c in courses_raw:
        built = b.build_course(c["meta"], c["chapters"])
        built_courses.append(built)

    b.save_ts_file("reading", "READING_COURSES", built_courses)
    print(f"阅读听力处理完成！当前全库累计唯一句子数: {len(b.global_seen_normalized)} 句")

if __name__ == "__main__":
    main()
