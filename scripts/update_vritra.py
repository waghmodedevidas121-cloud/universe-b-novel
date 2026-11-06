file_path = r"d:\Web Novel\Brahmand\01_WORLD_BIBLE\05_Cosmic_Eras_and_The_Seven_Nightmares.md"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace line 95
target1 = """  2. **Seal 2: पुलोमा (Puloma)** — *The Hoarder of the Sky* ("Drag the arrogant sun down into the mud.")"""
repl1 = """  2. **Seal 2: वृत्रासुर (अंधकाराधिपती - Vṛtrāsura)** — *The Hoarder of the Sky* ("Drag the arrogant sun down into the mud.")"""

if target1 in text:
    text = text.replace(target1, repl1)
    print("Replaced line 95 successfully")
else:
    print("target1 not found")

# Replace line 243
target2 = """| **Seal 2** | Sunken Trench of Netherholme | **The Hoarder of the Sky (Seal 2 / पुलोमा - Puloma)** | Automated Aetheric Light-Siphons; guarded by Obsidian Basalt Runes. | Assembly of Sages (Forensic Audit) | दक्षिणेकडील आकाशातून कायमचा सूर्यप्रकाश नष्ट होणे; कायमचे अंधत्व. |"""
repl2 = """| **Seal 2** | Sunken Trench of Netherholme | **The Hoarder of the Sky (Seal 2 / वृत्रासुर - अंधकाराधिपती - Vṛtrāsura)** | Automated Aetheric Light-Siphons; guarded by Obsidian Basalt Runes. | Assembly of Sages (Forensic Audit) | दक्षिणेकडील आकाशातून कायमचा सूर्यप्रकाश नष्ट होणे; कायमचे अंधत्व. |"""

if target2 in text:
    text = text.replace(target2, repl2)
    print("Replaced line 243 successfully")
else:
    print("target2 not found")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 05_Cosmic_Eras_and_The_Seven_Nightmares.md successfully")
