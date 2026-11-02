import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = r"d:\Web Novel\UNIVERSE B\New"

def apply_fix(filename, old_s, new_s):
    fpath = os.path.join(BASE_DIR, filename)
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()
    if old_s not in c:
        print(f"[FAIL] {filename}: old string not found: {old_s[:40]}")
        return False
    c = c.replace(old_s, new_s, 1)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"[SUCCESS] {filename} fixed")
    return True

# 1. 09_Faction_Politics.md
apply_fix(
    "09_Faction_Politics.md",
    "(ट्रेन, फॅक्टरी, कोळसा, बॉयलर्स, पिस्टन्स, बंदुका किंवा टेलिग्राफ तारा)",
    "(वाफेची इंजिने, फॅक्टरी, कोळसा, बॉयलर्स, पिस्टन्स, बंदुका किंवा आधुनिक तारा)"
)

# 2. 14_High_Council.md
apply_fix(
    "14_High_Council.md",
    "(Zero Rail)",
    "(शून्य लोहमार्ग / संपूर्ण तरंगते यान)"
)

# 3. 11_Astral_Society.md
apply_fix(
    "11_Astral_Society.md",
    "कारखान्यातून अचानक कामावरून काढून टाकले जाणे",
    "कारखान्यातून कोणत्याही क्षणी कामावरून काढून टाकले जाणे"
)
apply_fix(
    "11_Astral_Society.md",
    "परंतु हळूहळू निस्तेज होणारे सौर-कुलीन",
    "परंतु काळाच्या ओघात निस्तेज होणारे सौर-कुलीन"
)

# 4. 16_The_Proving_Games.md
apply_fix(
    "16_The_Proving_Games.md",
    "प्रहार करून क्षणार्धात अर्धांगवायू",
    "प्रहार करून एका फटक्यात अर्धांगवायू"
)

print("Remaining 5 fixes applied!")
