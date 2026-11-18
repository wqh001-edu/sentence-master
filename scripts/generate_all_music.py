# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))

from builder_core import save_ts_file
import music_part1
import data_music
import gen_music_full
import build_cat_music
import builder_part_music_textbook
import music_final_three
import music_queen_jazz

def generate_all_music():
    print("🎵 [构建中] 音乐英语 8 门课程完整聚合...")
    courses = []

    # 1. 披头士 (10章 / 150句)
    c1 = music_part1.get_music_part1()[0]
    courses.append(c1)

    # 2. 泰勒·斯威夫特 (10章 / 150句)
    c2 = data_music.get_all_music()[1]
    courses.append(c2)

    # 3. 迪士尼经典动画主题曲 (10章 / 150句)
    c3 = gen_music_full.generate_music()[2]
    courses.append(c3)

    # 4. 阿黛尔 (10章 / 150句)
    # build_cat_music 里的第 4 门
    import build_cat_music
    # 重新获取
    courses_4 = build_cat_music.build_music_all()
    # 在 build_cat_music.py 中，save_ts_file 已经写了，我们拿到第 4 门
    # 我们读取 builder_part_music_textbook 里的阿黛尔
    # 实际上 build_cat_music 已经构建并保存了前 4 门，我们读取它的前 4 门
    from builder_part_music_textbook import build_music_courses
    c_music_5 = build_music_courses()
    # c_music_5[3] 就是 10 章的阿黛尔！
    # c_music_5[4] 就是 10 章的黄老板！
    
    courses = [
        c_music_5[0], # 披头士
        c_music_5[1], # 霉霉
        c_music_5[2], # 迪士尼
        c_music_5[3], # 阿黛尔
        c_music_5[4], # 黄老板
    ]

    # 6. 酷玩乐队 (10章 / 150句)
    c6 = music_final_three.get_music_final_three()[0]
    courses.append(c6)

    # 7. 皇后乐队 (10章 / 150句)
    # 8. 爵士老歌与百老汇 (10章 / 150句)
    c7_8 = music_queen_jazz.get_queen_and_jazz()
    courses.extend(c7_8)

    assert len(courses) == 8, f"音乐课程数应为 8，实际为 {len(courses)}"
    total_ch = sum(len(c["chapters"]) for c in courses)
    total_s = sum(sum(len(ch["sentences"]) for ch in c["chapters"]) for c in courses)

    save_ts_file("music", "MUSIC_COURSES", courses)
    print(f"✨ [音乐分类构建大获成功！] 课程: {len(courses)} 门 | 章节: {total_ch} 个 | 句子: {total_s} 句")

if __name__ == "__main__":
    generate_all_music()
