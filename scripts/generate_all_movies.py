# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))

from builder_core import save_ts_file
import build_movies
import movies_part2
import movies_part3
import movies_part4

def generate_all_movies():
    print("🎬 正在构建影视分类 8 门完整课程...")
    part1 = build_movies.generate_movies()
    part2 = movies_part2.get_movies_part2()
    part3 = movies_part3.get_movies_part3()
    part4 = movies_part4.get_movies_part4()
    
    all_courses = part1 + part2 + part3 + part4
    assert len(all_courses) == 8, f"影视课程数量应为 8，实际为 {len(all_courses)}"
    
    save_ts_file("movies", "MOVIES_COURSES", all_courses)
    print("✨ [影视分类 8 门全集构建成功！]")

if __name__ == "__main__":
    generate_all_movies()
