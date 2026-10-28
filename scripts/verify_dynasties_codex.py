import os

_current_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_current_dir)
codex_file = os.path.join(_project_root, "New", "astral_dynasties_codex.html")
if not os.path.exists(codex_file):
    codex_file = r'D:\Web Novel\New\astral_dynasties_codex.html'

with open(codex_file, 'r', encoding='utf-8') as f:
    c = f.read()

print('Length:', len(c))
print('Dynasties count:', c.count('class="dynasty-card"'))
print('Characters count:', c.count('class="char-card"'))
print('Has Central City:', 'Central City' in c)
print('Has Devanagari Madhya-Nagara in titles/headings:', 'मध्य-नगर' in c.split('class="dyn-header"')[1:])
print('Has Era 1 blocks:', 'ERA-1' in c)
print('Has Era 2 blocks:', 'ERA-2' in c)
print('Has Era 3 blocks:', 'ERA-3' in c)
print('Has Era 4 blocks:', 'ERA-4' in c)
print('Has 4-Era evolution boxes:', c.count('class="era-evolution-box"'))
print('Has Strict Tech limit:', 'STRICT HARD TECHNOLOGY LIMIT' in c)
