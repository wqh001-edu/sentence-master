# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))

from builder_core import save_ts_file, preload_existing_mall_files
import gen_exam_part1
import gen_exam_part2
import gen_exam_part3
import gen_exam_part4

def main():
    print("🎓 开始构建【考试备考】8 门全集课程...")
    # 预加载已有 mall 文件的去重 hash（包含 movies.ts, music.ts, textbook.ts 等）
    preload_existing_mall_files()
    
    courses = []
    
    # 1 & 2: 四级 & 六级
    c1_2 = gen_exam_part1.get_exam_part1_courses()
    courses.extend(c1_2)
    print(f"  [1-2/8] 四级 & 六级 已加载: {len(c1_2)} 门")
    
    # 3 & 4: 考研 & 雅思
    c3_4 = gen_exam_part2.get_exam_part2_courses()
    courses.extend(c3_4)
    print(f"  [3-4/8] 考研 & 雅思 已加载: {len(c3_4)} 门")
    
    # 5 & 6: 托福 & 高考
    c5_6 = gen_exam_part3.get_exam_part3_courses()
    courses.extend(c5_6)
    print(f"  [5-6/8] 托福 & 高考 已加载: {len(c5_6)} 门")
    
    # 7 & 8: 中考 & GRE
    c7_8 = gen_exam_part4.get_exam_part4_courses()
    courses.extend(c7_8)
    print(f"  [7-8/8] 中考 & GRE 已加载: {len(c7_8)} 门")
    
    # 保存 TS 文件
    save_ts_file("exam", "EXAM_COURSES", courses)
    print(f"✅ 考试备考课程成功写入 exam.ts，共 {len(courses)} 门课程！")

if __name__ == "__main__":
    main()
