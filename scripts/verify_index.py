import os
import re

_current_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_current_dir)
base_dir = os.path.join(_project_root, "New")
if not os.path.exists(base_dir):
    base_dir = r"D:\Web Novel\New"

index_file = os.path.join(base_dir, "index.html")
assert os.path.exists(index_file), f"index.html does not exist at {index_file}!"
size_mb = os.path.getsize(index_file) / (1024 * 1024)
print(f"index.html verified on disk: {size_mb:.2f} MB")

with open(index_file, "r", encoding="utf-8") as f:
    html_text = f.read()

checks = [
    ("Rudra Operational Ansha Lock", r"operational Ansha of Shiva"),
    ("High Council Combat Ban", r"Absolute Combat Ban \(Inviolable Invariant\)"),
    ("Route B 5-Stage Machine", r"5-Stage Route B State Transition Machine"),
    ("Ananta Two-Layer Model", r"Two-Layer Permission Architecture"),
    ("Power System Taxonomy", r"Two-Tier Power Taxonomy: Cosmic Law vs\. Mortal Practice"),
    ("Class-Omega Secrecy", r"Known Dimensional Spheres vs\. Class-Omega Secrecy"),
    ("Seven Cosmic Seals", r"The Seven Cosmic Seals \(सप्त महा-बंध — Unified Master Register\)"),
    ("Pratigraha Official Dock", r"STAGE 5B: PRATIGRAHA OFFICIAL DOCK"),
    ("Canonical ID CHR-DIV-13", r"CHR-DIV-13"),
    ("Canonical ID CHR-SET-17", r"CHR-SET-17"),
    ("Canonical ID CHR-ALN-06", r"CHR-ALN-06"),
    ("Ardha-Rikta Multiversal Standard", r"Ardha-Rikta"),
    ("Continuous Fight Arena Evolution", r"Continuous Fight Rule"),
    ("Quad-Referee Coliseum Panel", r"QUAD-REFEREE PANEL"),
    ("Tectonic Rotary Anchor System", r"Tectonic Rotary Anchor"),
    ("The Eternal Four System Pillars", r"THE ETERNAL FOUR"),
    ("Setu Cosmic Warriors Stature", r"Cosmic Warriors"),
    ("The Proving Games Ecosystem", r"The Proving Games"),
    ("Aether-Pneumatics Magitech", r"Aether-Pneumatics"),
    ("The S-Rank Divergence", r"THE S-RANK DIVERGENCE"),
    ("Pan-Astral Feeder Circuits", r"PAN-ASTRAL FIGHTER PROGRESSION"),
    ("Pure Steel Combat Axioms", r"THE SEVEN PURE STEEL COMBAT AXIOMS"),
    ("The Hold Channel Capacity", r"DHĀRAṆĀ \(THE HOLD\)"),
    ("Dry Energy Exhaustion", r"ŚŪNYA \(DRY / BURNOUT\)"),
    ("The Sing Acoustic Tell", r"GŪÑJA \(THE SING\)"),
    ("The Molt Biological Evolution", r"NIRMOKA \(THE MOLT\)"),
    ("Search Highlighting JS", r"highlightSearchTerm"),
    ("Search Direct Doc Selection", r"search-result-item"),
    ("Responsive Table Scroll", r"-webkit-overflow-scrolling:\s*touch")
]

all_passed = True
for name, pattern in checks:
    present = bool(re.search(pattern, html_text))
    status = "PASS" if present else "FAIL"
    print(f"[{status}] {name}")
    if not present:
        all_passed = False

print("\nFinal Canonical Verification:", "ALL SYSTEMS PASS (100%)" if all_passed else "FAILURES DETECTED")
