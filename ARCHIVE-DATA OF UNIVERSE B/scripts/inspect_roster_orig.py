import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
output = subprocess.check_output(['git', 'show', '0c8eb46:New/08_Character_Roster.md'], cwd=r'd:\Web Novel\UNIVERSE B', encoding='utf-8')
lines = output.splitlines()

ids_to_check = ['CHR-ASU-03', 'CHR-ASU-13', 'CHR-BST-07', 'CHR-BST-02', 'CHR-HUM-08', 'CHR-HUM-09', 'CHR-HUM-11', 'CHR-CEN-01', 'CHR-CEN-02']
for idx, l in enumerate(lines):
    for cid in ids_to_check:
        if cid in l and l.startswith('### ['):
            print(f'Line {idx+1}: {l}')
            for k in range(idx+1, min(len(lines), idx+6)):
                print(f'   {lines[k]}')
            print('='*50)
