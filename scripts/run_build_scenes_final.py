# -*- coding: utf-8 -*-
"""
统合场景英语全部 8 门课程，通过全局查重写入 src/data/mall/scenes.ts
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

import builder_core as b
from gen_scenes_part1 import COURSE_SCENE_AIRPORT, COURSE_SCENE_HOTEL
from gen_scenes_part2 import COURSE_SCENE_RESTAURANT, COURSE_SCENE_SHOPPING
from gen_scenes_part3 import COURSE_SCENE_HOSPITAL, COURSE_SCENE_INTERVIEW
from gen_scenes_part4 import COURSE_SCENE_TRAFFIC, COURSE_SCENE_BUSINESS

def main():
    print("=== 开始生成场景英语分类全部 8 门精品课程 ===")
    b.preload_existing_mall_files()
    print(f"当前全库已有句子基数: {len(b.global_seen_normalized)} 句")

    courses_raw = [
        COURSE_SCENE_AIRPORT,
        COURSE_SCENE_HOTEL,
        COURSE_SCENE_RESTAURANT,
        COURSE_SCENE_SHOPPING,
        COURSE_SCENE_HOSPITAL,
        COURSE_SCENE_INTERVIEW,
        COURSE_SCENE_TRAFFIC,
        COURSE_SCENE_BUSINESS
    ]

    built_courses = []
    for c in courses_raw:
        built = b.build_course(c["meta"], c["chapters"])
        built_courses.append(built)

    b.save_ts_file("scenes", "SCENES_COURSES", built_courses)
    print(f"场景英语处理完成！当前全库累计唯一句子数: {len(b.global_seen_normalized)} 句")

if __name__ == "__main__":
    main()
