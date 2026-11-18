# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))

from builder_core import save_ts_file, preload_existing_mall_files
import gen_textbook_part1
import gen_textbook_part2
import gen_textbook_part3_renjiao
import gen_textbook_part4_rj8_9
import gen_textbook_part5_wy_oxford

def main():
    print("📚 开始构建【教材同步】8 门全集课程...")
    # 预加载已有 mall 文件的去重 hash（包含 movies.ts, music.ts 等）
    preload_existing_mall_files()
    
    courses = []
    
    # 1 & 2: 新概念1, 新概念2
    c1_2 = gen_textbook_part1.get_textbook_courses()
    courses.extend(c1_2)
    print(f"  [1-2/8] 新概念1 & 新概念2 已加载: {len(c1_2)} 门")
    
    # 3: 新概念3
    c3 = gen_textbook_part2.get_textbook_part2_courses()
    courses.extend(c3)
    print(f"  [3/8] 新概念3 已加载: {len(c3)} 门")
    
    # 4: 人教七年级
    c4 = gen_textbook_part3_renjiao.get_renjiao_courses()
    courses.extend(c4)
    print(f"  [4/8] 人教七年级 已加载: {len(c4)} 门")
    
    # 5 & 6: 人教八年级, 人教九年级
    c5_6 = gen_textbook_part4_rj8_9.get_rj8_rj9_courses()
    courses.extend(c5_6)
    print(f"  [5-6/8] 人教八年级 & 九年级 已加载: {len(c5_6)} 门")
    
    # 7 & 8: 外研高中必修一, 牛津初中
    c7_8 = gen_textbook_part5_wy_oxford.get_wy_oxford_courses()
    courses.extend(c7_8)
    print(f"  [7-8/8] 外研高中必修一 & 牛津初中 已加载: {len(c7_8)} 门")
    
    save_ts_file("textbook", "TEXTBOOK_COURSES", courses)
    print(f"✅ 教材同步课程成功写入 textbook.ts，共 {len(courses)} 门课程！")

if __name__ == "__main__":
    main()
