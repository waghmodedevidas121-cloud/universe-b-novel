# -*- coding: utf-8 -*-
with open('d:/Web Novel/UNIVERSE B/scripts/validate_ch2.py', 'r', encoding='utf-8') as f:
    text = f.read()

raw_text = text.split('chapter_2_hindi = """')[1].split('"""')[0]

import re
for label, word in [('EK', ' एक '), ('DO', ' दो '), ('TEEN', ' तीन ')]:
    matches = [m.start() for m in re.finditer(word, raw_text)]
    for idx in matches:
        snippet = raw_text[max(0, idx-20):min(len(raw_text), idx+30)]
        print(f"[{label}]:", snippet.encode('ascii', errors='replace').decode('ascii'))
