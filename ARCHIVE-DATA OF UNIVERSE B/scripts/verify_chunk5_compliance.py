import os
import sys

files = [
    r'd:\Web Novel\UNIVERSE B\New\00_World_Genesis_Prologue.md',
    r'd:\Web Novel\UNIVERSE B\New\02_Four_Eras_and_Seals.md',
    r'd:\Web Novel\UNIVERSE B\New\12_Historical_Annals.md',
    r'd:\Web Novel\UNIVERSE B\New\15_Leaderboard_System.md',
    r'd:\Web Novel\UNIVERSE B\New\17_Beast_Codex.md',
    r'd:\Web Novel\UNIVERSE B\New\18_Narrative_Veil_Protocol.md'
]

strict_forbidden = [
    'नहीं',
    'Lattice-Rails',
    'Cartridges',
    'विमान-उद्योग',
    'वाफेचे',
    'वाफेची',
    'High Governor',
    'High Chancellor',
    'Supreme Siege Marshal',
    'Grand Inquisitor',
    'Rosso',
    'लिओ ब्रॅडली',
    'Paundraka'
]

errors = []

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    fname = os.path.basename(fpath)
    for forb in strict_forbidden:
        if forb in text:
            errors.append(f"[{fname}] Contains forbidden term: '{forb}'")

# Specific checks
with open(r'd:\Web Novel\UNIVERSE B\New\12_Historical_Annals.md', 'r', encoding='utf-8') as f:
    t12 = f.read()
if '८५–९०%' not in t12:
    errors.append("[12_Historical_Annals.md] Missing 85-90% trade ratio")
if 'True 4-Bracket' not in t12:
    errors.append("[12_Historical_Annals.md] Missing True 4-Bracket Demographic section")
if 'वज्र-आदेश' not in t12:
    errors.append("[12_Historical_Annals.md] Missing Vajra-Adesh Conscription")

with open(r'd:\Web Novel\UNIVERSE B\New\02_Four_Eras_and_Seals.md', 'r', encoding='utf-8') as f:
    t02 = f.read()
if '#steam-aether-age' in t02:
    errors.append("[02_Four_Eras_and_Seals.md] Contains #steam-aether-age tag")
if '८५–९०%' not in t02:
    errors.append("[02_Four_Eras_and_Seals.md] Missing 85-90% trade ratio")
if 'CHR-DIV-14' not in t02:
    errors.append("[02_Four_Eras_and_Seals.md] Missing CHR-DIV-14 seat")

with open(r'd:\Web Novel\UNIVERSE B\New\17_Beast_Codex.md', 'r', encoding='utf-8') as f:
    t17 = f.read()
if 'Sheru (Official Central Registry: Kuro)' not in t17:
    errors.append("[17_Beast_Codex.md] Missing Sheru / Kuro canonical cross-reference")

with open(r'd:\Web Novel\UNIVERSE B\New\18_Narrative_Veil_Protocol.md', 'r', encoding='utf-8') as f:
    t18 = f.read()
if 'Tony Stark' not in t18:
    errors.append("[18_Narrative_Veil_Protocol.md] Missing Tony Stark principle")
if 'Lord of the Mysteries' not in t18:
    errors.append("[18_Narrative_Veil_Protocol.md] Missing LOTM principle")

if errors:
    print(f"FAILED WITH {len(errors)} ERRORS:")
    for err in errors:
        print("  -", err)
    sys.exit(1)
else:
    print("ALL CHUNK 5 FILES VERIFIED 100% COMPLIANT!")
