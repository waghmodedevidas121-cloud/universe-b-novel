import os

file_path = r"d:\Web Novel\Brahmand\02_POWER_SYSTEM\04_The_Proving_Games_and_Split_Flap_Spire.md"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

target = """  imports beast champions.                                     wager tokens (Pana & Suvarna)."""

replacement = """  imports beast champions.                                     wager tokens (Silver & Gold Coins)."""

if target in text:
    text = text.replace(target, replacement)
    print("Replaced tokens line successfully")
else:
    print("Tokens line target not found")

target2 = """- **The Currency of Wagers:** Bets are placed in **Silver Coins (पण)** and **Gold Coin (सुवर्ण)**. Foreign coins and strange paper bills are laughed at as worthless colorful scrap by the bookmakers."""
replacement2 = """- **The Currency of Wagers:** Bets are placed strictly in **चांदी के सिक्के (Silver Coins)** and **सोने के सिक्के (Gold Coins)**. Foreign coins and strange paper bills are laughed at as worthless colorful scrap by the bookmakers."""

if target2 in text:
    text = text.replace(target2, replacement2)
    print("Replaced currency line successfully")
else:
    print("Currency line target not found")

target3 = """- **Zero Charity:** Central City does not hand out alms. Bread costs 2 Copper Coins; clean water costs 1 Masha."""
replacement3 = """- **Zero Charity:** Central City does not hand out alms. Bread costs 2 Copper Coins; clean water costs 1 Copper Coin."""

if target3 in text:
    text = text.replace(target3, replacement3)
    print("Replaced clean water line successfully")
else:
    print("Clean water line target not found")

# Now append Section 8 if not already present
section_8 = """
---

## 8. The Dual Ranking Engine: The Hero Board vs. The Vanguard Adventurer Guilds
*(वीर-फलक व साहसी गिल्ड्स: दुहेरी श्रेणी व महा-सेतू भरती प्रणाली)*

To prevent contenders from becoming arena-only "paper tigers", the Astral Cosmos operates on a synchronized **Dual Ranking Engine (दुहेरी श्रेणी यंत्रणा)** connecting Central City's Split-Flap Spire with the frontier Adventurer Guilds:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        THE DUAL ASTRAL PROGRESSION ENGINE                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. THE HERO BOARD (वीर-फलक / Split-Flap Spire - Central City):                         │
│    • Tracks the Top 5,000 active tournament gladiators across all Five Shards.         │
│    • Ranks determine political standing, commercial sponsors, and high-purse bouts.   │
│                                                                                        │
│ 2. THE VANGUARD ADVENTURER GUILDS (साहसी गिल्ड / Pan-Astral Guildhalls):               │
│    • Overseen pan-astral by Guildmaster Agastya (अगस्त्य).                             │
│    • Branches in Hastināpur, Caldera Foundry, Primeval Canopy, and Central City.       │
│    • Issues Metal Rank Tags: Copper -> Iron -> Silver -> Gold -> Mythril/Vajra.        │
│    • Handles real-world field contracts: Wild Beast Hunts (Beast Cores), Crypt Raids,  │
│      Void Rift Incursions, and Rogue Devil Suppression.                                │
│                                                                                        │
│ 3. THE ANTI-"PAPER TIGER" RULE (आखाड्याबाहेरील प्रत्यक्ष मोहीम अनिवार्य):              │
│    • A contender CANNOT advance past C-Rank, B-Rank, or A-Rank on the Hero Board solely│
│      by winning stadium matches!                                                       │
│    • High Council law mandates that fighters must present verified field completion of │
│      Adventurer Guild Crisis Quests (slaying wild beasts, clearing cursed crypts) to   │
│      qualify for Spire rank promotions.                                                │
│                                                                                        │
│ 4. THE PIPELINE TO THE GREAT SETU (सेतू महा-सेनेतील थेट भरती):                         │
│    • Warriors who attain Apex S-Rank on the Hero Board are conscripted/inducted into   │
│      the Setu Standing Army at Tier 2 (Antariksha-Setu).                               │
│    • There, they discover that arena duels were merely a training forge; the true war  │
│      is defending the cosmos against Tier 4 horrors behind the Grand Aegis!            │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
"""

if "## 8. The Dual Ranking Engine" not in text:
    # Insert before the last block or append
    text = text + section_8
    print("Appended Section 8 successfully")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)
print("File updated successfully")
