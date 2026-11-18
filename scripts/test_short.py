import re

def extract_short(meaning_str):
    if not meaning_str:
        return '中文'
    # 移除 [名词] 等前缀
    text = re.sub(r'\[[^\]]+\]\s*', '', meaning_str)
    # 按分号分割
    first_part = text.split('；')[0].split(';')[0].strip()
    # 按逗号分割取前两个
    sub_parts = [p.strip() for p in re.split(r'[,，、/]', first_part) if p.strip()]
    if not sub_parts:
        return first_part[:8]
    if len(sub_parts) == 1:
        return sub_parts[0]
    return f"{sub_parts[0]}, {sub_parts[1]}"

samples = [
    '预订；保留；预留；保留地',
    '有保证的；担保的；必定实现的',
    '在...之下；在...期间；以...名义',
    '这；那；该 (定冠词)',
    '[名词] 房间， 空位， 场所；[动词] 住宿， 居住；[动词] 留宿',
    '[名词] 名字， 名称， 姓名， 名义， 名誉， 文件名；[动词] 命名',
    '米勒 (人名/姓氏)；磨坊主',
    '阿尔布里赫 (墨西哥传统民间幻兽彩绘雕刻)',
    '金缮修复；以金粉修补破损瓷器的日本传统工艺'
]

for s in samples:
    print(f"ORIG: {s}")
    print(f"SHORT: {extract_short(s)}\n")
