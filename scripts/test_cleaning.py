import json
import re

with open('node_modules/ecdict/data/dict.json', 'r', encoding='utf-8') as f:
    dict_data = json.load(f)

# 建立 word -> item 的快速索引（只取小写）
word_dict = {}
for item in dict_data:
    w = item.get('word', '').lower()
    if w and w not in word_dict:
        word_dict[w] = item

test_words = ['reservation', 'guaranteed', 'under', 'the', 'room', 'name', 'miller', 'afternoon', 'good', 'have', 'been', 'expensive', 'quickly']

def clean_translation(trans_str):
    if not trans_str:
        return '中文释义', '实词'
    # 按行拆分
    lines = [l.strip() for l in trans_str.split('\\n') if l.strip()]
    cleaned_lines = []
    first_pos = ''
    for l in lines:
        if l.startswith('[网络]') or l.startswith('[计]') or l.startswith('[医]') or l.startswith('[化]'):
            continue
        cleaned_lines.append(l)
        if not first_pos:
            m = re.match(r'^([a-zA-Z\.]+)\s+', l)
            if m:
                first_pos = m.group(1)
    full_cn = '; '.join(cleaned_lines) if cleaned_lines else trans_str
    return full_cn, first_pos

for w in test_words:
    item = word_dict.get(w)
    if item:
        full_cn, first_pos = clean_translation(item.get('translation', ''))
        print(f"{w} -> ph: /{item.get('phonetic', '')}/ | pos: {first_pos} | meaning: {full_cn}")
    else:
        print(f"{w} -> NOT FOUND")
