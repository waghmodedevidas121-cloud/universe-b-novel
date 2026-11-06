import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

files = [
    r'd:\Web Novel\UNIVERSE B\rulebook\COMPLETE_125_CHARACTER_MASTER_SHEET.md',
    r'd:\Web Novel\UNIVERSE B\New\characters\roster.md',
    r'd:\Web Novel\UNIVERSE B\New\08_Character_Roster.md'
]

forbidden_words = [
    'रोसो',
    'Rosso',
    'High Governor',
    'High Chancellor',
    'Supreme Siege Marshal',
    'High Caravan-Master',
    'High Admiral',
    'Supreme Aerial Commander',
    'Supreme Military Commander',
    'High Soul-Transit Overseer',
    'High Arbitrator',
    'Grand Marshal'
]

errors = []

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    for fw in forbidden_words:
        if fw in text:
            errors.append(f"[{fpath}] Contains forbidden: '{fw}'")

# Check headers in 08_Character_Roster.md for slashes
with open(r'd:\Web Novel\UNIVERSE B\New\08_Character_Roster.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith('### [CHR-'):
        if '/' in line:
            errors.append(f"[08_Character_Roster.md Line {i+1}] Header has slash: {line.strip()}")

if errors:
    print(f"FAILED WITH {len(errors)} ERRORS:")
    for err in errors:
        print("  -", err)
else:
    print("ALL ROSTER AND CHARACTER FILES 100% CLEAN & VERIFIED!")

