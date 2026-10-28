import os

_current_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_current_dir)
base_dir = os.path.join(_project_root, "New")

terminology_table = """

---

## 8. Universe B: Quick-Reference Canonical Terminology Lock (Categories A, B, C)
*(अंतिम आणि अपरिवर्तनीय संज्ञा-तालिका)*

```
═════════════════════════════════════════════════════════════════════════════════════════════
                 UNIVERSE B: QUICK-REFERENCE CANONICAL TERMINOLOGY LOCK
═════════════════════════════════════════════════════════════════════════════════════════════

[ 1. COMBAT & POWER AXIOMS (100% Natural English) ]
• The Hold         : Channel capacity of the 72,000 meridians (Nadis).
• The Blowout      : Internal channel rupture & black charring from exceeding The Hold.
• Dry / Burnout    : Complete prana exhaustion causing hypoxia, cold sweat & muscle lock.
• Breath Reset     : Mandatory respiratory recovery rhythm between heavy exchanges.
• The Sing         : 0.2-second high-pitched crystal whistle before an aether-slug fires.
• The Purge        : High-heat blue steam eruption during human physical evolution.
• The Molt         : Violent shedding of old hide for diamond-hard scales in bonded beasts.
• The Chime        : Private brass bell resonance heard ONLY in the fighter's skull during crisis.

[ 2. CORE SKILLS & TECHNIQUES (Zero Anime Copy-Paste / Zero Fake Joint Sanskrit) ]
• Sovereign Dread  : Overwhelming willpower aura (replaces Conqueror's Haki).
• Iron Imbuement   : Hardening weapons/flesh with prana (replaces Armament Haki).
• Meridian Sight   : Seeing internal energy flows & weak points (replaces Byakugan/Six Eyes).
• Gale Step        : Sonic burst movement (replaces Shunpo/Flash Step).
• Kinetic Rupture  : Microsecond impact shockwave (replaces Black Flash).
• Void Cleave      : Spatial severance that bypasses armor (replaces World Cutting Slash).
• Will-Binding     : Mental command over weaker minds (replaces Geass).
• Isolation Ward   : Sound-and-energy sealing dome (replaces Curtain/Kekkai).

[ 3. INTER-REALM INFRASTRUCTURE & LOCATIONS ]
• The Five-Arch Rotunda      : Central City's hub plaza (replaces Pancham-Maha-Ghat).
• The 4 Stone Gateways       : 1. Hastinapur High Arch (Human), 2. Caldera Basalt Arch (Asura),
                               3. Sun-Cliff Arch (Deva), 4. Root-Carved Arch (Beast).
• Rotary Shadow Anchors      : Lethal subterranean smuggling dials under 500-ton drop-hammers.
• The Central Reserve Bank   : Issues the Aether-Rupee (replaces Akash-Kosha).
• Soul Reception Depository  : Tier 2 arrival & quarantine warehouse (replaces Pratigraha Godown).
• The Dead Chasm (Seal 7)    : Where King Shrutayudha & The Stone-Eyed Crow guard the 7th Horror.

[ 4. CURRENCIES & EVERYDAY ECONOMICS ]
• 1 Aether-Rupee (AR)        = 100 Silver Panas (SP) = 1,600 Copper Mashas (CM).
• Foundry Iron Bar (FIB)     = 25 Silver Panas (Asura heavy trade unit).
• Solar Gold Sovereign (SGS) = 10 Aether-Rupees (Deva luxury trade unit).
• Daily Wages & Costs        : Miner shift = 3–4 CM | Dal-Bhakri meal = 2 CM | Ginger tea = 1 CM |
                               Chawl room rent = 6 SP/month | .44 Compression Ammo (20 rds) = 3 SP.
═════════════════════════════════════════════════════════════════════════════════════════════
```
"""

index_p = os.path.join(base_dir, "INDEX.md")
with open(index_p, "r", encoding="utf-8") as f:
    c = f.read()
if "UNIVERSE B: QUICK-REFERENCE CANONICAL TERMINOLOGY LOCK" not in c:
    c += terminology_table
    with open(index_p, "w", encoding="utf-8") as f:
        f.write(c)
    print("Added Quick-Reference table to INDEX.md")

naming_p = os.path.join(base_dir, "rules", "naming.md")
with open(naming_p, "r", encoding="utf-8") as f:
    c = f.read()
if "UNIVERSE B: QUICK-REFERENCE CANONICAL TERMINOLOGY LOCK" not in c:
    c += terminology_table
    with open(naming_p, "w", encoding="utf-8") as f:
        f.write(c)
    print("Added Quick-Reference table to rules/naming.md")
