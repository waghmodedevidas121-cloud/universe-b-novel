# UNIVERSE B — PUBLISHING MANIFEST & READING ORDER (WEBSITE LAUNCH SPEC)
**Document ID:** `UB-PUBLISH-MANIFEST-2026`  
**Workspace:** `D:\Web Novel\UNIVERSE B\New\PUBLISHING_MANIFEST.md`  
**Purpose:** Exact upload list, reading order, and gap audit for publishing Season 1 on a public web novel site.

---

## 1. HONEST GAP AUDIT (READ THIS FIRST)

### ✅ What Is Launch-Ready
- Chapter 1 (English + Hindi) — complete arc: glitch → beast-cart → Sheru's cord snaps → gate visible.
- Chapter 2 (English + Hindi) — complete arc: water → gate rejection → scrap-pen → Sheru rescued and bonded.
- Chapter 3 (English + Hindi) — complete arc: registration → Sand-Pit bout → first Spark discharge → purse + pass.

### ⚠️ Three Real Gaps
1. **There is no Story Prologue yet.** `00_World_Genesis_Prologue.md` is a **3,840-word cosmic lore essay** ("THE BREATH OF ETERNITY AND THE FIVE BROKEN SHARDS"). It has no protagonist, no scene, no dialogue. **It is NOT a novel prologue and must NOT be Chapter 0 on the website** — it will kill 90% of new readers on page one. It belongs in a separate **Codex / Lore** tab.
2. **Chapter 1 is underweight: 1,743 English words** vs. the 2,500–3,200 target. Chapter 2 is 2,561 and Chapter 3 is 2,592. Chapter 1 reads fast but is ~30% short — the caravan staging grounds, the wagon master, and the gate crowd need one more expanded beat.
3. **No Prologue, Interlude, Epilogue, or Omake files exist yet** for Volume 1, even though `volume_structure_spec.md` mandates all four.

### 📌 Verdict on "Starting"
The **writing itself starts correctly**. Chapter 1 opens with a cold, sensory, in-scene hook (headache → alien cold → void sky → dead phone → Lava-Bull → pup). That is a textbook strong web-novel opening. What the user is missing is not a story start — it is a **website entry point** that tells a new reader "click here first."

---

## 2. WHAT TO UPLOAD — PHASE 1 (LAUNCH SET)

Upload **only these 6 narrative files**. Nothing else.

| # | Upload Order | File | Language | Words |
| :-- | :--- | :--- | :--- | :--- |
| 1 | Vol 1 · Ch 1 | `19_Season_1_Chapter_1.md` | English | 1,743 |
| 2 | Vol 1 · Ch 1 | `19_Season_1_Chapter_1_Hindi.md` | Hindi Dub | 2,193 |
| 3 | Vol 1 · Ch 2 | `20_Season_1_Chapter_2.md` | English | 2,561 |
| 4 | Vol 1 · Ch 2 | `20_Season_1_Chapter_2_Hindi.md` | Hindi Dub | 3,171 |
| 5 | Vol 1 · Ch 3 | `21_Season_1_Chapter_3.md` | English | 2,592 |
| 6 | Vol 1 · Ch 3 | `21_Season_1_Chapter_3_Hindi.md` | Hindi Dub | 3,149 |

**Total launch content:** ~6,900 English words + ~8,500 Hindi words.

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

1. **Write the real Prologue** — `Prologue: The Glitch in the Rain` (~1,200–1,500 words). Bombay, 7:15 PM monsoon, Dadar bridge, the puddle, the tear. Ends on the white-gold corridor. This becomes the true entry point.
2. **Expand Chapter 1** from 1,743 to ~2,600 words — add the wagon master's dialogue and the staging-ground crowd beat before the gate.
3. **Build a web-ready reader page** for Chapters 1–3 with the English/Hindi toggle.
4. **Then** start Chapter 4 (Outer Bazaar, pawnshop, Reva & Kira).

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
