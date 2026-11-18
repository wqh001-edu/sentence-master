# -*- coding: utf-8 -*-
"""
统合基础学习全部 8 门课程，通过全局查重写入 src/data/mall/basic.ts
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

import builder_core as b
from gen_basic_part1 import COURSE_BASIC_PHONETICS
from gen_basic_part2 import COURSE_BASIC_1000WORDS, COURSE_BASIC_PATTERNS, COURSE_BASIC_TENSES
from gen_basic_part3 import COURSE_BASIC_QUESTIONS, COURSE_BASIC_PREPOSITIONS
from gen_basic_part4 import COURSE_BASIC_PRONOUNS, COURSE_BASIC_DIALOGUES

def main():
    print("=== 开始生成基础学习分类全部 8 门精品课程 ===")
    b.preload_existing_mall_files()
    print(f"当前全库已有句子基数: {len(b.global_seen_normalized)} 句")

    courses_raw = [
        COURSE_BASIC_PHONETICS,
        COURSE_BASIC_1000WORDS,
        COURSE_BASIC_PATTERNS,
        COURSE_BASIC_TENSES,
        COURSE_BASIC_QUESTIONS,
        COURSE_BASIC_PREPOSITIONS,
        COURSE_BASIC_PRONOUNS,
        COURSE_BASIC_DIALOGUES
    ]

    built_courses = []
    for c in courses_raw:
        built = b.build_course(c["meta"], c["chapters"])
        built_courses.append(built)

    b.save_ts_file("basic", "BASIC_COURSES", built_courses)
    print(f"基础学习处理完成！当前全库累计唯一句子数: {len(b.global_seen_normalized)} 句")

if __name__ == "__main__":
    main()
