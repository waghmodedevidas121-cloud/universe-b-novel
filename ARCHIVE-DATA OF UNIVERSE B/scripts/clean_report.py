import json

with open(r'd:\Web Novel\UNIVERSE B\scripts\goldfish_chunk5_report.txt', 'r', encoding='utf-8') as f:
    raw = f.read()

try:
    data = json.loads(raw)
except Exception:
    data = raw

with open(r'd:\Web Novel\UNIVERSE B\scripts\goldfish_chunk5_clean.md', 'w', encoding='utf-8') as out:
    out.write(data)
print("Done, length:", len(data))
