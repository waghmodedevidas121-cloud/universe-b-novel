import os
import re
import sys

_current_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_current_dir)
base_dir = os.path.join(_project_root, "New")

print(f"Applying Master Canonical Refinements across {base_dir}")

# Load test_bracket_transforms.py
from test_bracket_transforms import bracket_transforms

# 1. Update 08_Character_Roster.md and characters/roster.md
roster_files = [
    os.path.join(base_dir, "08_Character_Roster.md"),
    os.path.join(base_dir, "characters", "roster.md")
]

for rf in roster_files:
    if not os.path.exists(rf):
        continue
    with open(rf, "r", encoding="utf-8") as f:
        content = f.read()

    # Header update (Refinement 3)
    content = re.sub(
        r"\*\*File:\*\*\s*`.*?`",
        r"**File:** `D:\\Web Novel\\New\\characters\\roster.md (100 Verified Canonical Entities)`",
        content,
        count=1
    )

    # Replace Part 10 (Refinement 3)
    old_p10_regex = r"# PART 10: THE PROTAGONIST SLOT — UNASSIGNED \(केंद्रीय नायक\).*?(?=\Z)"
    new_p10 = """# [INVARIANT 4: THE WORLD IS THE MAIN CHARACTER — 100 AUTONOMOUS ENTITIES]

Universe B मध्ये कोणताही एक कृत्रिम किंवा पूर्व-निश्चित नायक (Fixed Protagonist) नाही. विश्वातील १०० च्या १०० प्रमाणित व्यक्ती स्वतंत्र इच्छाशक्ती, स्वतःचे ध्येय आणि स्वायत्त कृती क्षमता (Organic Agency) बाळगून आहेत. जग हेच मुख्य पात्र आहे; कोणताही आत्मा पूर्व-मंजूर चीट्स किंवा प्लॉट आर्मर घेऊन जन्माला येत नाही.
"""
    content = re.sub(old_p10_regex, new_p10, content, flags=re.DOTALL)

    # Refinement 1 Tech patch terms in roster profiles
    content = content.replace("वाफ, कायदा व शिक्षण", "तंत्र, कायदा व शिक्षण")
    content = content.replace("दुहेरी-गेज *गरुड-श्रेणी* चिलखती वाफेच्या इंजिनांच्या मागचे तेजस्वी मन.", "दुहेरी-गेज The Falcon-Class Armored Locomotive लॅटिस-इंजिनांच्या मागचे तेजस्वी मन.")
    content = content.replace("वाफेचे दाब-नियंत्रण", "एथर-कंप्रेशन व दाब-नियंत्रण")
    content = content.replace("वाफेच्या *वरुण-वात* फ्रिगेटची सेनानी.", "The HMS Storm-Tide (Ironclad Frigate) ची सेनानी.")
    content = content.replace("असुर क्षेत्रातील भूमिगत वाफेचे ग्रिड", "असुर क्षेत्रातील भूमिगत लॅटिस-ऊर्जा ग्रिड")
    content = content.replace("नश्वरांच्या औद्योगिक वाफेच्या झपाट्याने वर येण्याबद्दल", "नश्वरांच्या औद्योगिक एथर-तंत्रज्ञानाच्या झपाट्याने वर येण्याबद्दल")
    content = content.replace("आकाशीय वाफेचे होकायंत्र", "आकाशीय एथर-होकायंत्र")
    content = content.replace("वाफेच्या इंजिनांना कवडीची किंमत देत नाही", "लॅटिस-इंजिनांना कवडीची किंमत देत नाही")
    content = content.replace("कोळशाच्या धुराचा कट्टर तिरस्कार", "कच्च्या एथर-स्लॅग व गंधकाच्या धुराचा कट्टर तिरस्कार")
    content = content.replace("जे लोखंडी बॉयलर वितळवते", "जे लोखंडी एथर-प्रेशर चेंबर वितळवते")
    content = content.replace("हस्तिनापूरचे वाफेचे हवेतील फुगे", "हस्तिनापूरच्या एथर-टेहळणी नौका")

    # Refinement 4: Standardize Active Arts and Arsenal using clean bracket notation
    # Split by character headers
    char_blocks = re.split(r"(?=\n###\s*\[CHR-[A-Z]+-[0-9]+\])", content)
    new_blocks = [char_blocks[0]] # Header section

    for block in char_blocks[1:]:
        m_id = re.search(r"###\s*\[(CHR-[A-Z]+-[0-9]+)\]", block)
        if m_id and m_id.group(1) in bracket_transforms:
            cid = m_id.group(1)
            t = bracket_transforms[cid]
            # Replace active arts line
            block = re.sub(
                r"(-\s*\*सक्रिय कौशल्ये व विद्या \(Active Arts\):\*).*?(?=\n\s*-\s*\*अधिकृत शस्त्रागार)",
                r"\1 " + t["arts"],
                block
            )
            # Replace arsenal line
            block = re.sub(
                r"(-\s*\*अधिकृत शस्त्रागार \(Arsenal\):\*).*?(?=\n\s*-\s*\*नाती:|\n\s*---|(?:\n\s*#)|\Z)",
                r"\1 " + t["ars"],
                block
            )
        new_blocks.append(block)

    content = "".join(new_blocks)

    with open(rf, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {rf} with Refinements 1, 3, 4.")

# Verify parity
f1 = open(roster_files[0], encoding="utf-8").read()
f2 = open(roster_files[1], encoding="utf-8").read()
print(f"Roster files byte parity: {f1 == f2} ({len(f1)} vs {len(f2)})")

