import re

f = open('src/utils/dictionaryData.ts', encoding='utf-8').read()
matches = re.findall(r'"([a-zA-Z0-9_\'\-]+)":\s*\{\s*pos:\s*"([^"]+)",\s*short:\s*"([^"]+)",\s*meaning:\s*"([^"]+)"', f)

unmapped = []
for word, pos, short, meaning in matches:
    if '地道词汇表达' in meaning or '核心概念' in meaning:
        unmapped.append(word)

print(f"Total fallback tokens: {len(unmapped)}")
print(unmapped)
