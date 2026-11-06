# UNIVERSE B — ARCHIVAL TRASH REPOSITORY & AUDIT GENEALOGY
**Folder:** `D:\Web Novel\UNIVERSE B\trash\`  
**Status:** [STRUCTURED ARCHIVE & AUDIT TRAIL]  
**Authority:** Cross-referenced with `Changes/04_LEGACY_EVOLUTION_AND_TRASH_RECOVERY_MAP.md`

---

## 1. Directory Architecture

This directory preserves all legacy drafts, obsolete rules, redundant root files, and one-off development scripts from early development phases (V0.1, V1, and V2 transitions) without polluting the active canonical novel engine.

```text
trash/
├── World/                       # Phase 1: V0.1 Foundational Drafts (Modules 01–40)
├── legacy_mirrors/              # Phase 2: V1 Category Mirrors & Audits
├── archive_preliminary/         # Early preliminary chapter and tier breakdowns
├── legacy_drafts/               # Superseded chapter drafts and intermediate scene fragments
├── legacy_rules_and_world/      # Outdated power system bibles and truncated writing guides
├── legacy_previews_and_html/    # Retired HTML preview dashboards and standalone viewers
├── one_off_scripts/             # One-time migration, patching, and scratch python scripts
└── root_duplicates/             # Redundant root copies (duplicate playbook, merge.py, combined dumps)
```

---

## 2. Directory Contents & Descriptions

| Subdirectory | Purpose & Contents | Canonical Successor |
| :--- | :--- | :--- |
| `World/` | Original 40 foundational lore documents from V0.1. | `New/world/`, `New/powers/`, `New/characters/` |
| `legacy_mirrors/` | V1 categorical split mirrors. | `New/` categorized subsystems |
| `archive_preliminary/` | Early preliminary tier and character files. | `rulebook/`, `New/characters/roster.md` |
| `legacy_drafts/` | Superseded drafts of Prologue, Chapter 1, 2, and 3. | `Story/` (Active dual-track novel prose) |
| `legacy_rules_and_world/` | Early V1 power system bibles, 465-line bible draft. | `rulebook/master_writing_flow_bible.md` (877-line full bible) |
| `legacy_previews_and_html/`| Old HTML reports and intermediate preview snapshots. | `New/universe_b_writer_studio.html`, `New/index.html` |
| `one_off_scripts/` | Scratch scripts (`test_*.py`, `apply_*.py`, etc.). | `scripts/build_universe_b_studio.ps1`, `scripts/patch_studio_ui.py`, `scripts/verify_index.py` |
| `root_duplicates/` | Old root copies (`UNIVERSE_B_DIRECTORS_PLAYBOOK.md`, `merge.py`, `UNIVERSE_B_COMBINED.txt`). | `rulebook/UNIVERSE_B_DIRECTORS_PLAYBOOK.md` |

---

## 3. Preservation & Audit Policy
Files in `trash/` are kept for historical traceability, reference, and recovery. They are excluded from the active build toolchain and should never be directly referenced in active story prose.
