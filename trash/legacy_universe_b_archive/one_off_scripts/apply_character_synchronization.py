import os
import re
import sys
from character_shard_mappings import MAPPINGS

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
f1 = os.path.join(project_root, "New", "08_Character_Roster.md")
f2 = os.path.join(project_root, "New", "08_Character_Dossiers_and_Psychology", "01_Master_Character_Dossier_73_Roster_and_Sheets.md")

with open(f1, "r", encoding="utf-8") as f:
    text = f.read()

pattern = re.compile(r"(###\s*\[(CHR-[A-Z]+-\d+)\][^\n]+\n)([\s\S]*?)(?=(?:\n---\n\s*###|\n# PART|\Z))")

updated_count = 0
not_found = []

def replacer(match):
    global updated_count
    header = match.group(1)
    cid = match.group(2)
    body = match.group(3)

    if cid in MAPPINGS:
        shard_info, vanguard_info = MAPPINGS[cid]
        
        # Check if already present
        if "- **ग्रह-खंड व स्थान (Planetary Shard):**" not in body:
            # Find the role line or first bullet line
            role_match = re.search(r"(-\s*\*\*गट व भूमिका:\*\*[^\n]+\n)", body)
            if role_match:
                insertion = f"- **ग्रह-खंड व स्थान (Planetary Shard):** {shard_info}\n- **व्हॅनगार्ड व श्वापद अनुबंध (Vanguard & Prana-Bond):** {vanguard_info}\n"
                body = body.replace(role_match.group(1), role_match.group(1) + insertion, 1)
            else:
                # If no role line (like DIV characters having अधिकारक्षेत्र), insert after the first bullet
                first_bullet = re.search(r"(-\s*\*\*[^\n]+\n)", body)
                if first_bullet:
                    insertion = f"- **ग्रह-खंड व स्थान (Planetary Shard):** {shard_info}\n- **व्हॅनगार्ड व श्वापद अनुबंध (Vanguard & Prana-Bond):** {vanguard_info}\n"
                    body = body.replace(first_bullet.group(1), first_bullet.group(1) + insertion, 1)
                else:
                    body = f"- **ग्रह-खंड व स्थान (Planetary Shard):** {shard_info}\n- **व्हॅनगार्ड व श्वापद अनुबंध (Vanguard & Prana-Bond):** {vanguard_info}\n" + body
            updated_count += 1
    else:
        not_found.append(cid)

    return header + body

new_text = pattern.sub(replacer, text)

print(f"Total character sections processed: {updated_count}")
if not_found:
    print(f"Characters not in mappings: {not_found}")

# Write to both f1 and f2
with open(f1, "w", encoding="utf-8") as f:
    f.write(new_text)

with open(f2, "w", encoding="utf-8") as f:
    f.write(new_text)

print(f"Successfully updated:\n  {f1}\n  {f2}")
