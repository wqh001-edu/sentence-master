import json

with open('node_modules/ecdict/data/lemma.json', 'r', encoding='utf-8') as f:
    lemma_data = json.load(f)
    print("lemma_data type:", type(lemma_data), "len:", len(lemma_data))
    if isinstance(lemma_data, list):
        print("lemma_data[0:3]:", lemma_data[0:3])
    elif isinstance(lemma_data, dict):
        print("sample keys:", list(lemma_data.keys())[:3])

with open('node_modules/ecdict/data/dict.json', 'r', encoding='utf-8') as f:
    dict_data = json.load(f)
    print("dict_data type:", type(dict_data), "len:", len(dict_data))
    if isinstance(dict_data, list):
        print("dict_data[0:2]:", dict_data[0:2])
    elif isinstance(dict_data, dict):
        print("sample keys:", list(dict_data.keys())[:3])
