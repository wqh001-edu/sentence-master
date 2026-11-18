import json

with open('node_modules/ecdict/data/dict.json', 'r', encoding='utf-8') as f:
    dict_data = json.load(f)

targets = {'reservation', 'guarantee', 'guaranteed', 'under', 'the', 'room', 'name', 'miller'}
found = {}

for item in dict_data:
    w = item.get('word', '').lower()
    if w in targets and w not in found:
        found[w] = {
            'phonetic': item.get('phonetic'),
            'translation': item.get('translation')
        }

for k, v in found.items():
    print(f"=== {k} ===")
    print("phonetic:", v['phonetic'])
    print("translation:", repr(v['translation']))
