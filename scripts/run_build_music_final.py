# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))

from builder_core import build_course, save_ts_file, preload_existing_mall_files
import music_part1
import data_music
import gen_music_full
import music_part3
import builder_part_music_textbook
import music_final_three
import music_queen_jazz
import data_music_fill

def run_build():
    print("🎵 开始构建【音乐英语】8 门全集课程...")
    # 先预加载已有的 movies.ts
    preload_existing_mall_files()
    
    courses = []
    
    # 1. 披头士 (10章)
    c1 = music_part1.get_music_part1()[0]
    courses.append(c1)
    print(f"  [1/8] 披头士: {len(c1['chapters'])} 章")
    
    # 2. 泰勒·斯威夫特 (10章)
    c2 = data_music.get_all_music()[1]
    courses.append(c2)
    print(f"  [2/8] 泰勒·斯威夫特: {len(c2['chapters'])} 章")
    
    # 3. 迪士尼经典动画 (10章)
    c3 = gen_music_full.generate_music()[2]
    courses.append(c3)
    print(f"  [3/8] 迪士尼经典动画: {len(c3['chapters'])} 章")
    
    # 4. 阿黛尔 (10章)
    adele_base = music_part3.get_music_part3()[0]
    adele_meta = {
        "id": "course-mus-adele",
        "title": "《阿黛尔》(Adele) · 灵魂深情与心碎叙事 (10章全集)",
        "category": "music",
        "categoryName": "音乐英语",
        "coverGradient": "from-zinc-900 via-stone-800 to-amber-950",
        "icon": "🎙️",
        "description": "十六座格莱美奖得主，Someone Like You、Rolling in the Deep 灵魂天籁震撼全集。",
        "difficulty": "中级 B1",
        "tags": ["阿黛尔", "灵魂乐", "深情治愈", "格莱美"]
    }
    adele_chapters_raw = []
    for ch in adele_base["chapters"][:5]:
        adele_chapters_raw.append({
            "title": ch["title"],
            "description": ch["description"],
            "sentences": [{"en": s["english"], "cn": s["chinese"]} for s in ch["sentences"]]
        })
    adele_chapters_raw.extend(data_music_fill.ADELE_EXTRA)
    c4 = build_course(adele_meta, adele_chapters_raw)
    courses.append(c4)
    print(f"  [4/8] 阿黛尔: {len(c4['chapters'])} 章")
    
    # 5. 艾德·希兰 (10章)
    sheeran_meta = {
        "id": "course-mus-sheeran",
        "title": "《艾德·希兰》(Ed Sheeran) · 清新木吉他与温暖叙事民谣 (10章全集)",
        "category": "music",
        "categoryName": "音乐英语",
        "coverGradient": "from-amber-700 via-orange-600 to-yellow-500",
        "icon": "🎸",
        "description": "英伦民谣创作才子，Perfect、Shape of You、Photograph 用一把吉他唱尽人世温柔与深情。",
        "difficulty": "初级 A2",
        "tags": ["黄老板", "吉他民谣", "深情对唱", "浪漫婚礼"]
    }
    # 从 builder_part_music_textbook 中拿到前 5 首
    raw_sheeran_5 = builder_part_music_textbook.build_music_courses()[-1]
    sheeran_chapters_raw = []
    for ch in raw_sheeran_5["chapters"][:5]:
        sheeran_chapters_raw.append({
            "title": ch["title"],
            "description": ch["description"],
            "sentences": [{"en": s["english"], "cn": s["chinese"]} for s in ch["sentences"]]
        })
    sheeran_chapters_raw.extend(data_music_fill.SHEERAN_EXTRA)
    c5 = build_course(sheeran_meta, sheeran_chapters_raw)
    courses.append(c5)
    print(f"  [5/8] 艾德·希兰: {len(c5['chapters'])} 章")
    
    # 6. 酷玩乐队 (10章)
    c6 = music_final_three.get_music_final_three()[0]
    courses.append(c6)
    print(f"  [6/8] 酷玩乐队: {len(c6['chapters'])} 章")
    
    # 7. 皇后乐队 (10章)
    q_j = music_queen_jazz.get_queen_and_jazz()
    queen_base = q_j[0]
    queen_meta = {
        "id": "course-mus-queen",
        "title": "《皇后乐队》(Queen) · 华丽摇滚与不灭荣耀歌剧 (10章全集)",
        "category": "music",
        "categoryName": "音乐英语",
        "coverGradient": "from-yellow-600 via-red-600 to-purple-900",
        "icon": "👑",
        "description": "摇滚殿堂级王者，Bohemian Rhapsody、We Will Rock You 华丽歌剧与体育场赞歌全收录。",
        "difficulty": "中高级 B2",
        "tags": ["皇后乐队", "华丽摇滚", "摇滚歌剧", "热血沸腾"]
    }
    queen_chapters_raw = []
    for ch in queen_base["chapters"][:4]:
        queen_chapters_raw.append({
            "title": ch["title"],
            "description": ch["description"],
            "sentences": [{"en": s["english"], "cn": s["chinese"]} for s in ch["sentences"]]
        })
    queen_chapters_raw.extend(data_music_fill.QUEEN_EXTRA)
    c7 = build_course(queen_meta, queen_chapters_raw)
    courses.append(c7)
    print(f"  [7/8] 皇后乐队: {len(c7['chapters'])} 章")
    
    # 8. 爵士老歌与百老汇 (10章)
    jazz_base = q_j[1]
    jazz_meta = {
        "id": "course-mus-jazz",
        "title": "《爵士老歌与百老汇殿堂》(Jazz & Broadway) · 黄金年代岁月流金 (10章全集)",
        "category": "music",
        "categoryName": "音乐英语",
        "coverGradient": "from-amber-900 via-yellow-800 to-stone-900",
        "icon": "🎷",
        "description": "辛纳屈、阿姆斯特朗、格什温，漫步曼哈顿与百老汇璀璨夜色的摇摆爵士岁月流金。",
        "difficulty": "初中级 A2-B1",
        "tags": ["爵士名伶", "百老汇", "岁月流金", "浪漫经典"]
    }
    jazz_chapters_raw = []
    for ch in jazz_base["chapters"][:5]:
        jazz_chapters_raw.append({
            "title": ch["title"],
            "description": ch["description"],
            "sentences": [{"en": s["english"], "cn": s["chinese"]} for s in ch["sentences"]]
        })
    jazz_chapters_raw.extend(data_music_fill.JAZZ_EXTRA)
    c8 = build_course(jazz_meta, jazz_chapters_raw)
    courses.append(c8)
    print(f"  [8/8] 爵士与百老汇: {len(c8['chapters'])} 章")
    
    # 保存 TS 文件
    save_ts_file("music", "MUSIC_COURSES", courses)
    print("✨ [音乐英语分类构建完成！]")

if __name__ == "__main__":
    run_build()
