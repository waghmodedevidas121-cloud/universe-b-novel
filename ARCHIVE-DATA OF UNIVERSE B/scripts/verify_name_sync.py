import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read master sheet
with open(r'd:\Web Novel\UNIVERSE B\rulebook\COMPLETE_125_CHARACTER_MASTER_SHEET.md', 'r', encoding='utf-8') as f:
    master_lines = f.readlines()

master_dict = {}
for line in master_lines:
    if line.strip().startswith('| `CHR-'):
        parts = [p.strip() for p in line.split('|')[1:-1]]
        cid = parts[0].replace('`', '')
        name = parts[1].replace('*', '')
        dev = parts[2]
        master_dict[cid] = (name, dev)

# Read roster lines
with open(r'd:\Web Novel\UNIVERSE B\New\08_Character_Roster.md', 'r', encoding='utf-8') as f:
    roster_lines = f.readlines()

roster_dict = {}
for line in roster_lines:
    if line.startswith('### [CHR-'):
        m = re.match(r'### \[(CHR-[A-Z]+-[0-9]+)\]\s+([^(—]+)\(([^)]+)\)', line)
        if m:
            cid = m.group(1)
            name = m.group(2).strip()
            dev = m.group(3).strip()
            roster_dict[cid] = (name, dev, line.strip())
        else:
            print("Couldn't parse roster header:", line.strip())

mismatches = []
for cid, (m_name, m_dev) in master_dict.items():
    if cid in roster_dict:
        r_name, r_dev, r_raw = roster_dict[cid]
        # Check if master name is in roster name
        if m_name.lower() not in r_name.lower():
            mismatches.append(f"NAME MISMATCH [{cid}]: Master='{m_name}' vs Roster='{r_name}' (Raw: {r_raw})")
    else:
        # Check if it's one of the extra master characters or in roster
        pass

print(f"Checked {len(master_dict)} characters. Total mismatches: {len(mismatches)}")
for m in mismatches:
    print(" ", m)

