# UNIVERSE B — PUBLISHING MANIFEST & READING ORDER (WEBSITE LAUNCH SPEC)
**Document ID:** `UB-PUBLISH-MANIFEST-2026`  
**Workspace:** `D:\Web Novel\UNIVERSE B\New\PUBLISHING_MANIFEST.md`  
**Purpose:** Exact upload list, reading order, and gap audit for publishing Season 1 on a public web novel site.

---

## 1. HONEST GAP AUDIT (READ THIS FIRST)

### ✅ What Is Launch-Ready
- **Prologue (English + Hindi)** — 1,418 words. Bombay monsoon, Dadar bridge, the dry sizzle, the vertical seam, the pothole fold. True entry point. **COMPLETE.**
- Chapter 1 (English + Hindi) — 3,095 words. glitch → beast-cart → wagon master's toll warning → staging-ground crowd → sky reveal → Sheru's cord snaps → gate visible. **EXPANDED AND COMPLETE.**
- Chapter 2 (English + Hindi) — complete arc: water → gate rejection → scrap-pen → Sheru rescued and bonded.
- Chapter 3 (English + Hindi) — complete arc: registration → Sand-Pit bout → first Spark discharge → purse + pass.

### ⚠️ One Real Gap
1. **Interlude, Epilogue, and Omake files do not exist yet** for Volume 1, even though `volume_structure_spec.md` mandates all four for a finished volume.

### ✅ Note on the Genesis Prologue
`00_World_Genesis_Prologue.md` (3,840 words) remains **Codex-only**. The real story prologue now exists as `18A_Season_1_Volume_1_Prologue.md` and is the correct Chapter 0.

### 📌 Verdict on "Starting"
The **writing itself starts correctly**. Chapter 1 opens with a cold, sensory, in-scene hook (headache → alien cold → void sky → dead phone → Lava-Bull → pup). That is a textbook strong web-novel opening. What the user is missing is not a story start — it is a **website entry point** that tells a new reader "click here first."

---

## 2. WHAT TO UPLOAD — PHASE 1 (LAUNCH SET)

Upload **only these 6 narrative files**. Nothing else.

| # | Upload Order | File | Language | Words |
| :-- | :--- | :--- | :--- | :--- |
| 0 | Vol 1 · Prologue | `18A_Season_1_Volume_1_Prologue.md` | English | 1,546 |
| 1 | Vol 1 · Prologue | `18A_Season_1_Volume_1_Prologue_Hindi.md` | Hindi Dub | 1,695 |
| 2 | Vol 1 · Ch 1 | `19_Season_1_Chapter_1.md` | English | 3,129 |
| 3 | Vol 1 · Ch 1 | `19_Season_1_Chapter_1_Hindi.md` | Hindi Dub | 3,325 |
| 4 | Vol 1 · Ch 2 | `20_Season_1_Chapter_2.md` | English | 2,561 |
| 5 | Vol 1 · Ch 2 | `20_Season_1_Chapter_2_Hindi.md` | Hindi Dub | 3,135 |
| 6 | Vol 1 · Ch 3 | `21_Season_1_Chapter_3.md` | English | 2,597 |
| 7 | Vol 1 · Ch 3 | `21_Season_1_Chapter_3_Hindi.md` | Hindi Dub | 3,108 |

**Total launch content:** 9,833 English words + 11,263 Hindi words (8 files).

### Do NOT upload in Phase 1
| File / Folder | Reason |
| :--- | :--- |
| `00_World_Genesis_Prologue.md` | Cosmic lore essay. Spoils the Vol 3 veil. Codex only. |
| `01_` to `18_` canon modules | ~90,000 words of internal bible. Contains every twist. |
| `08_Character_Roster.md` | 27,623 words. Massive spoiler risk. Codex only, post-Vol 1. |
| `Research/`, `Gods/`, `Changes/`, `rulebook/`, `trash/` | Internal development material. Never public. |
| `CHANGES_MASTER_RECORD.md`, `INDEX.md` | Internal audit trail. |
| `chapter_1_reader.html` | Local-only reader. Rebuild for web before publishing. |

---

## 3. WEBSITE STRUCTURE (RECOMMENDED)

```text
========================================================================================
                        UNIVERSE B — PUBLIC SITE MAP
========================================================================================
[HOME]
  └── Big "START READING" button  →  /read/chapter-1

[READ]  (primary nav)
  ├── Volume 1: The Mud, the Beast & the D-Tier Blood-Pit
  │     ├── Chapter 1 — The Hay, the Horns, and the Dead Glass
  │     ├── Chapter 2 — Copper, Crusts, and the Scrap-Hound
  │     └── Chapter 3 — The Sand, the Steel, and the First Spark
  └── [Language Toggle: English / हिन्दी Dub]  ← global switch, top right

[CODEX]  (optional, launch later)
  ├── World & Tiers
  ├── Character Dossiers (unlocked entries only)
  └── Beast Codex (unlocked species only)

[ABOUT]  — author note, update schedule
========================================================================================
```

### The single most important page
A short **Start Here** page above Chapter 1:

> **New here?** A 19-year-old Mumbai college student falls through a puddle and wakes in a beast-cart in a frozen void. He has no powers, no coins, and no way home — only a cracked phone and a one-eared stray hound. **Start with Chapter 1 →**

That single paragraph is what is currently missing, not the story.

---

## 4. UPLOAD RULES (DO THESE, ALWAYS)

1. **One chapter = one page.** Never dump multiple chapters per URL.
2. **Never mix languages in one page.** Use the toggle or separate URLs (`/en/` and `/hi/`).
3. **Strip the YAML header block** (the `**File:**`, `**Tags:**`, `**Status:**` lines) before pasting to a website. Those are internal metadata.
4. **Keep the `### [VOLUME 1...]` heading** — it is the volume label readers see.
5. **Hindi page must keep `।` punctuation and `· मनात` monologue tags** — that is the dub voice signature.
6. **Publish 1 chapter per week minimum**, 2 if possible. Web novel sites reward consistency over volume.

---

## 5. RECOMMENDED NEXT ACTIONS (PRIORITY ORDER)

1. ~~**Write the real Prologue**~~ — **DONE.** `18A_Season_1_Volume_1_Prologue.md` (1,546) + `_Hindi.md` (1,695, master track). Cold-open in Bombay monsoon.
2. ~~**Build the writing studio**~~ — **DONE.** `New/universe_b_writer_studio.html` — 8 chapters (4 English + 4 Hindi), 7 codex entries, write/read toggle, localStorage autosave.
3. ~~**Expand Chapter 1**~~ — **DONE.** English 3,129 / Hindi 3,325, Hindi rewritten natively against `rules/hindi_dub_lexicon.md`. Wagon-master toll briefing, staging-ground crowd, sky reveal, three-bell gate opening.
4. **Build a public reader page** (separate from the studio) with a real English/Hindi toggle for website visitors.
5. **Then** start Chapter 4 (Outer Bazaar, pawnshop, Reva & Kira).

---

## 6. CANONICAL STARTING POINT (LOCKED)

```text
========================================================================================
                        OFFICIAL READING ORDER — SEASON 1
========================================================================================
VOLUME 1
  Prologue : The Glitch in the Rain            [TO BE WRITTEN]
  Chapter 1: The Hay, the Horns, and the Dead Glass   [READY]
  Chapter 2: Copper, Crusts, and the Scrap-Hound      [READY]
  Chapter 3: The Sand, the Steel, and the First Spark [READY]
  Chapter 4: Outer Bazaar / Pawnshop / Reva Entry     [NEXT]
  ...
========================================================================================
```
