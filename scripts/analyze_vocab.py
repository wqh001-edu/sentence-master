import re
import json
import glob

# 提取 src/data/mall/ 下所有生成的 ts 文件中的句子
all_words = set()
files = glob.glob('src/data/mall/*.ts')

for filepath in files:
    if filepath.endswith('index.ts') or filepath.endswith('categories.ts'):
        continue
    content = open(filepath, encoding='utf-8').read()
    # 匹配 english: "..." 或 '...'
    matches = re.findall(r'["\']english["\']\s*:\s*["\']([^"\']+)["\']', content)
    for sent in matches:
        # 分词
        tokens = re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)?", sent.lower())
        for t in tokens:
            all_words.add(t)

print(f"Total files scanned: {len(files)}")
print(f"Total unique English words in the entire curriculum: {len(all_words)}")

# 输出一部分看看
sample = sorted(list(all_words))[:50]
print("Sample words:", sample)
