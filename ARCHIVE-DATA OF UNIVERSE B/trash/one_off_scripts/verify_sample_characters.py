import sys
import os
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
import re

base_dir = r"D:\Web Novel\UNIVERSE B\New"
if not os.path.exists(base_dir):
    base_dir = r"D:\Web Novel\New"
dossier_path = os.path.join(base_dir, "08_Character_Roster.md")
with open(dossier_path, "r", encoding="utf-8") as f:
    text = f.read()

pattern = re.compile(r"###\s*\[(CHR-[A-Z]+-\d+)\][^\n]+\n([\s\S]*?)(?=(?:\n---\n|\n# PART|\Z))")
matches = list(pattern.finditer(text))

test_indices = [0, 3, 15, 17, 30, 32, 40, 48, 56, 73, 81]
for i in test_indices:
    m = matches[i]
    cid = re.search(r"CHR-[A-Z]+-\d+", m.group(0)).group(0)
    lines = [l.strip() for l in m.group(0).split("\n") if l.strip().startswith("- **")]
    print(f"=== {cid} ===")
    for l in lines[:4]:
        print(" ", l)
    print()
