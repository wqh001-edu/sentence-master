# -*- coding: utf-8 -*-
import re, json

def norm(text):
    return re.sub(r'[^a-z0-9]', '', text.lower().strip())

def scan_file(file_path):
    print(f"Scanning {file_path}...")
    seen = {}
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for idx, line in enumerate(lines):
        m = re.search(r'["\']en["\']\s*:\s*["\']([^"\']+)["\']', line)
        if m:
            en = m.group(1)
            k = norm(en)
            if len(k) > 4:
                if k in seen:
                    print(f"Duplicate in {file_path}: Line {idx+1} vs Line {seen[k]['line']}")
                    print(f"  EN: {en}")
                else:
                    seen[k] = {"line": idx+1, "en": en}

if __name__ == "__main__":
    import glob
    for p in glob.glob("scripts/*music*.py"):
        scan_file(p)
