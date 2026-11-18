import json
import re
import glob

# 1. 提取所有在课程中出现的单词
all_tokens = set()
files = glob.glob('src/data/mall/*.ts')

for filepath in files:
    if filepath.endswith('index.ts') or filepath.endswith('categories.ts'):
        continue
    content = open(filepath, encoding='utf-8').read()
    matches = re.findall(r'["\']english["\']\s*:\s*["\']([^"\']+)["\']', content)
    for sent in matches:
        tokens = re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)?", sent.lower())
        for t in tokens:
            all_tokens.add(t)

print(f"Total tokens found in courses: {len(all_tokens)}")

# 2. 读取 ecdict 数据
print("Loading ecdict dict.json...")
with open('node_modules/ecdict/data/dict.json', 'r', encoding='utf-8') as f:
    dict_list = json.load(f)

print("Indexing ecdict...")
ecdict_map = {}
for item in dict_list:
    w = item.get('word', '').lower()
    if w and w not in ecdict_map:
        ecdict_map[w] = item

print(f"Total entries in ecdict: {len(ecdict_map)}")

# 3. 统计有多少 token 在 ecdict 中
found = 0
missing = []
for t in all_tokens:
    if t in ecdict_map:
        found += 1
    else:
        # 去掉 's 或 't
        base_t = t.split("'")[0]
        if base_t in ecdict_map:
            found += 1
        else:
            missing.append(t)

print(f"Direct match in ecdict: {found} / {len(all_tokens)} ({found / len(all_tokens) * 100:.2f}%)")
print(f"Missing tokens: {len(missing)}")
if missing:
    print("Sample missing tokens:", missing[:30])
