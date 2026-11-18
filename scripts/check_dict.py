import re

f = open('src/utils/dictionaryData.ts', encoding='utf-8').read()
words = ['the', 'under', 'reservation', 'guaranteed', 'guarantee', 'reserve', 'room', 'name', 'miller']
res = {}
for w in words:
    pattern = r"['\"]" + w + r"['\"]\s*:"
    res[w] = bool(re.search(pattern, f))
print(res)

# 打印词典总词数
matches = re.findall(r"^\s+['\"]?([a-zA-Z0-9_\-]+)['\"]?\s*:\s*\{", f, re.MULTILINE)
print(f"Total entries in CORE_FULL_DICTIONARY approx: {len(matches)}")
