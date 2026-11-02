import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

chunk4_files = [
    r"d:\Web Novel\UNIVERSE B\New\08_Character_Roster.md",
    r"d:\Web Novel\UNIVERSE B\New\09_Faction_Politics.md",
    r"d:\Web Novel\UNIVERSE B\New\11_Astral_Society.md",
    r"d:\Web Novel\UNIVERSE B\New\13_Races_and_Clans.md",
    r"d:\Web Novel\UNIVERSE B\New\14_High_Council.md",
    r"d:\Web Novel\UNIVERSE B\New\16_The_Proving_Games.md"
]

tech_banned = ['विमान', 'एअरशिप', 'blimp', 'rail', 'टेलिग्राफ', 'वाफेची', 'काडतूस']
ghost_names = ['Ambika', 'Sulabha', 'Silas', 'Hilda', 'Olga', 'Morvath', 'Jormun', 'Linnea', 'Finn']

print("--- SCANNING CHUNK 4 FILES FOR TECH CONTAMINATION & GHOST NAMES ---")
violations = 0
for fpath in chunk4_files:
    fname = os.path.basename(fpath)
    content = open(fpath, 'r', encoding='utf-8').read()
    for b in tech_banned:
        if b == 'rail':
            matches = re.findall(r'\brail\b|\brails\b|\brailway\b|\brailways\b', content, re.IGNORECASE)
        else:
            matches = re.findall(re.escape(b), content, re.IGNORECASE)
        if matches:
            print(f"  [TECH VIOLATION] {fname}: Found {len(matches)} occurrences of '{b}'")
            violations += len(matches)
    for g in ghost_names:
        matches = re.findall(r'\b' + re.escape(g) + r'\b', content, re.IGNORECASE)
        if matches:
            print(f"  [GHOST NAME] {fname}: Found {len(matches)} occurrences of '{g}'")
            violations += len(matches)

# Check 'नहीं' rule
print("\n--- CHECKING THE 'नहीं' RULE ---")
nahi_violations = 0
for fpath in chunk4_files:
    fname = os.path.basename(fpath)
    content = open(fpath, 'r', encoding='utf-8').read()
    matches = re.findall(r'नहीं', content)
    if matches:
        print(f"  [NAHI VIOLATION] {fname}: Found {len(matches)} occurrences of 'नहीं'")
        nahi_violations += len(matches)

# Check 22 banned words
banned_words_22 = [
    'अचानक', 'खिन्न', 'स्तब्ध', 'क्षणार्धात', 'मूकपणे', 'हळूहळू', 'निःशब्द', 'अनामिक',
    'धक्का बसला', 'घाम फुटला', 'थरकाप', 'विषण्ण', 'अवाक', 'काळजात चर्र झाले',
    'श्वास रोखून', 'डोळे पाणावले', 'कंप सुटला', 'हृदयाचा ठोका चुकला', 'सुन्न',
    'गांगरून', 'चकित', 'उद्विग्न'
]

print("\n--- CHECKING 22 BANNED WORDS ---")
banned_violations = 0
for fpath in chunk4_files:
    fname = os.path.basename(fpath)
    content = open(fpath, 'r', encoding='utf-8').read()
    for bw in banned_words_22:
        matches = re.findall(re.escape(bw), content)
        if matches:
            print(f"  [BANNED WORD] {fname}: Found {len(matches)} occurrences of '{bw}'")
            banned_violations += len(matches)

print("\n=======================================================")
if violations == 0 and nahi_violations == 0 and banned_violations == 0:
    print(">>> 100% PERFECT! ALL CHUNK 4 FILES ARE COMPLETELY CLEAN! <<<")
else:
    print(f"TOTAL ISSUES REMAINING: {violations + nahi_violations + banned_violations}")
print("=======================================================")
