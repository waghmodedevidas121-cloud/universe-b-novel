import re

path = r'd:\Web Novel\UNIVERSE B\New\18_Narrative_Veil_Protocol.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Section 1 Table with clean titles (no clunky brackets)
old_table_part = """| True Cosmic Concept (Revealed at Vol 3 End!) | 🎭 WHAT IT IS CALLED IN VOLUMES 1–3 (The Disguise) | How the Reader Experiences It in Vol 1–3 |
| :--- | :--- | :--- |
| **Devas (Amaravati)** | **The Solarians / The Highborn of the North Spire** | Readers perceive an arrogant aristocracy of light-wielding, winged sky-nobles observing from high marble balconies. |
| **Asuras (Iron Citadel)** | **The Calderans / The Forge-Kin of the West** | Readers perceive high-gravity volcanic titans, siege engineers, and master metallurgists. |
| **Beasts & Vahanas** | **The Canopy-Kin & Bonded Beasts** | Readers experience a deep, grounded 3-stage physical beast-bonding ecosystem (Zero Pokéballs). |
| **Prana & 72,000 Nadis** | **Aether-Breath & The Vessel Channels** | Fighters strictly use tactical terminology: *"The Hold"*, *"The Blowout"*, *"Going Dry"*, and *"Breath Reset"*. |
| **The 3 Granthis (Knots)** | **The Three Locks (1st, 2nd, & 3rd Seal of the Spine)** | Cultivators know that unlocking the 1st Lock yields C-Rank, and the 2nd Lock unlocks S-Rank mastery. |
| **Ananta's World Chime** | **"The Bell in the Skull" / The Arena Chime** | Understood as an internal biological resonance during near-death survival breakthroughs; the entity ringing the chime remains unknown. |
| **Sanskrit Bija-Mantras** | **"Dead-Tongue Syllables" / Primeval Ignition Words** | High-rank fighters loose monosyllabic ignition vocalizations (*"Ram!", "Krom!"*), regarded by commoners as ancient acoustic triggers. |
| **Yama, Vidhata & Setu** | **"The Upper Citadel" / The Draft** | Central City citizens believe S-Rank victors who receive "The Draft" ascend to an idyllic celestial citadel. |
| **Gudhi Padwa & Diwali** | **The Festival of New Dawn & The 7-Night Lamp Carnival** | Described purely through sensory atmosphere: glowing clay oil-lamps, fried sweets, and youth awakening rites. |
| **Hastinapur Realm** | **The Eastern Crownlands** | Known as the vast agrarian and cavalry kingdom beyond the eastern mist gates. |
| **Amaravati Spire** | **The Northern Solar Spire** | Regarded as the floating sun-citadel above the cloud barrier. |
| **Vajra-Nagara** | **The Western Caldera** | Regarded as the volcanic fortress of basalt foundries and weapon-forges. |"""

new_table_part = """| True Reality (Classified until Vol 3 Climax) | 🎭 Street Register (Volumes 1–3 Cover Terms) | Reader & Character Experience in Vol 1–3 |
| :--- | :--- | :--- |
| **Devas (देव)** | **Skyborn / Solarians** | Arrogant aristocracy of winged sky-nobles observing from high marble balconies. |
| **Asuras (असुर)** | **Forge-Kin / Calderans** | Volcanic titans, siege engineers, and master metallurgists of the western bastions. |
| **Beast-Folk & Vahanas** | **Canopy-Kin & Bonded Beasts** | Grounded 3-stage physical beast-bonding ecosystem (Zero Pokéballs). |
| **Pretas (प्रेत / अधो-दैत्य)** | **Devils / Underworld Fiends** | Mythical boogeymen of the abyss; public belief is they are extinct outside of bedtime ghost stories. |
| **Patala (पाताळ - Tier 4)** | **The Cursed Realm / The Pit** | Sealed zone behind the Grand Aegis; Class-Omega taboo strictly forbids speaking its true name. |
| **Prāṇa (प्राण) & 72,000 Nadis** | **Aether-Breath & Vessel Channels** | Fighters strictly speak in tactical terms: *"The Hold"*, *"The Blowout"*, *"Going Dry"*, *"Breath Reset"*. |
| **The 3 Granthis (Knots)** | **The Three Locks (1st, 2nd, 3rd Lock)** | Spiritual bottlenecks: 1st Lock unlocks C-Rank, 2nd Lock unlocks S-Rank mastery. |
| **Ananta's World Chime** | **The Bell in the Skull** | Internal acoustic resonance during near-death survival breakthroughs under the Crisis Law. |
| **Sanskrit Bīja-Mantras** | **Dead-Tongue Ignition Syllables** | Monosyllabic acoustic triggers (*"Ram!"*, *"Krom!"*) loosed by high-tier warriors. |
| **The Indra-Upādhi (इंद्र-उपाधी)** | **The Sovereign / The Golden Chair** | Unseen celestial ruler of Swarga and warden of the 360° Spherical Grand Aegis. |
| **The Manu-Upādhi (मनू-उपाधी)** | **The Central King / Grey Basalt Throne** | Presiding ruler of Central City presiding above the 7 Sovereign Seats. |
| **The Great Setu & Swarga** | **The Upper Citadel / The Draft** | Arena champions believe S-Rank victors receive "The Draft" into an idyllic heavenly garrison. |
| **Gudhi Padwa (गुढीपाडवा)** | **The Festival of New Dawn** | Spring celebration of cosmic genesis and age-12 youth awakening resonance testing. |
| **Deepavali (दिवाळी)** | **The 7-Night Lamp Carnival** | 7-day pan-astral truce of glowing clay lamps, sweets, and complete cessation of coliseum violence. |"""

if old_table_part in text:
    text = text.replace(old_table_part, new_table_part)
    print("Replaced Table in Section 1")

# Replace Section 3 and Section 4
s3_marker = "## SECTION 3: SEASON 1 PROTAGONIST PROFILE — \"NEEL\""
s5_marker = "## SECTION 5: THE FOUR HIDDEN SEAM FIXES (WATERTIGHT ALIGNMENT)"

idx_s3 = text.find(s3_marker)
idx_s5 = text.find(s5_marker)

if idx_s3 != -1 and idx_s5 != -1:
    new_s3_and_s4 = """## SECTION 3: SEASON 1 CATALYST & PROTAGONIST PROFILE — NEEL

> [!IMPORTANT]
> **FRANCHISE ARCHITECTURE MANDATE:**
> Neel's chapter-by-chapter story, tournament match play-by-plays, and micro-progression belong strictly in the narrative chapter scene drafts, NOT in this macro-worldbuilding bible! In the macro architecture, Neel functions as the **Season 1 Catalyst ("The Tony Stark of Chaturmukh Brahma")** whose role is to introduce the reader to the living world, bridge modern 21st-century tech-rationalism with authentic Vedic metaphysics, and shatter the Narrative Veil at the Volume 3 climax.

```text
================================================================================
CANONICAL PROTAGONIST DOSSIER: NEEL (SEASON 1 ANCHORING STAR)
================================================================================
• Full Name       : Neel
• Apparent Age    : 19 years old (Born: Mumbai, India)
• Physical State  : 100% Original 21st-century human body (Anomalous Physical Glitch).
• Lineage & Origin:
  - 19-year-old Worli coastal tech-lab prodigy, sole surviving heir to Gadora
    Industrial & Tech Conglomerate (hardware, ceramics, spatial resonance prototypes).
  - Parents: Late Aarav Gadora & Suman Gadora (lost when Neel was 14 in an unexplained
    R&D spatial catastrophe).
  - Extended Family: Uncle Kani (corporate shark attempting hostile takeover), Aunt Cheri,
    and cousin Sunny Gadora.
• Starting Gear / Inventory:
  - Bespoke charcoal-grey cashmere-cotton hoodie and tailored joggers.
  - Dead, unhackable prototype titanium smartphone (holding circuit schematics,
    proprietary firmware, and the last saved audio memo from his mother).
  - High-limit Centurion Black Card (worthless in an aether-coin economy).
  - Exactly ₹11 in loose cutting chai change in his pocket!
• Psychological Core:
  - Hyper-observant, cynical-yet-protective, sharp deadpan wit.
  - Tech-rationalist mindset: analyzes mystical phenomena through thermodynamics,
    kinetic resistance, and circuit logic.
  - Zero religious superstition initially: rationalizes Vedic/astral phenomena as
    "alien biology" or "sci-fi physics", which preserves the Narrative Veil for 3 volumes!
• Asymmetric Combat Arsenal (Zero Magic Spells / Grounded Mechanics):
  1. RIGHT ARM (Atharvan Krutya GENI):
     - Transmuted biological interface channeling Zero-Sing Kinetic Friction Sparks (250–400 Joules).
     - Sub-perceptual friction ignition with zero acoustic whine, bypassing the 0.2-second
       "Sing" broadcast tell of standard fighters.
  2. LEFT ARM (Cursed Glove KALI):
     - Shrouded in a spiked black-iron shackle holding an imprisoned Tier 4 Patala Devil Spirit.
     - Provides brutal, physical, heavy-gravity telekinesis (snapping bones, crushing weapons,
       yanking opponents, launching rubble).
     - Bounded strictly by Neel's mental Dhāraṇā (Hold / Concentration) capacity; severe
       recoil/backlash if the Hold slips!
  3. COMPANION BEAST (Sheru / official registration: Kuro):
     - One-eared feral Stage-1 Dusk-Scrapper hound (Void/Iron type).
     - Loyal street brawler providing tandem trips, ankle snaps, and distraction feints.
================================================================================
```

---

## SECTION 4: THE "TONY STARK / LOTM" MULTI-SEASON ANTHOLOGY ENGINE

Universe B (in-world canonical name: **Chaturmukh Brahma — The 4-Headed Cosmos / चतुर्मुख ब्रह्मांड**) is engineered with a **World-First Franchise Philosophy**, drawing direct inspiration from the Marvel Cinematic Universe (MCU) and *Lord of the Mysteries* (LOTM):

```
┌────────────────────────────────────────────────────────────────────────┐
│      THE CHATURMUKH BRAHMA (चतुर्मुख ब्रह्मांड) FRANCHISE ENGINE       │
├────────────────────────────────────────────────────────────────────────┤
│ • THE UNIVERSE: "Chaturmukh Brahma — The 4-Headed Cosmos"              │
│                 (चतुर्मुख ब्रह्मांड / Universe B is the working codename) │
│                                                                        │
│ • THE CATALYST (Season 1): NEEL                                        │
│   - Functions exactly like Tony Stark in Phase 1 of the MCU!           │
│   - Neel's mission: Hook the reader through fast-talking street charm, │
│     cynical tech-rationalism, grounded D-Tier arena struggles, and     │
│     shatter the Narrative Veil at the Volume 3 climax.                 │
│                                                                        │
│ • THE TRUE STAR (The Franchise): THE 4-HEADED COSMOS ITSELF            │
│   - Designed like Lord of the Mysteries (LOTM): Klein Moretti hooked   │
│     readers in Book 1, but readers passionately followed the world     │
│     into Book 2 because the 22 Pathways, the Outer Deities, and the    │
│     cosmology are the true magnetic attraction!                        │
│   - When Neel's personal catalyst arc concludes or branches, the       │
│     audience will follow other terrestrial and celestial protagonists  │
│     (Karna in Hastinapur, Dhruv in Ekachakra, Asura rebels in the      │
│     Calderas, outcasts on the Great Setu) because they love the world! │
└────────────────────────────────────────────────────────────────────────┘
```

### The 70/30 Seasonal Dual-Star Architecture (Volumes 1 to 9)

1. **Season 1 (Volumes 1–3): 100% Neel's Perspective (The Grounding Phase)**
   - **Role:** Grounded survival in Central City, Proving Games climb from D-to-S Rank, navigating Donna Beatrice Vanezza's debt-traps and the subterranean Veiled Grid.
   - **Climax:** The Catastrophic Coliseum Breach -> The Descent of Setu Commander Vajraketu -> The Great Vedic Veil Shatters!

2. **Season 2 (Volumes 4–6): "The Shard Wars & The Buffer Zone" (Dual-Star Expansion)**
   - **Track A (Neel on the Great Setu):** Drafted into the Setu Standing Army under the Vajra-Adesh, learning true Sanskrit Bīja-Mantras and Divyastra handling under Setu Academy Head Shrutasen.
   - **Track B (New Terrestrial Protagonists):** Down in the planetary shards, the lens shifts to fresh point-of-view heroes (e.g. outcast archer **Karna** in Hastinapur or Seal-7 bloodline scion **Dhruv** in Ekachakra), demonstrating that the world thrives beyond any single individual.
   - **Climax:** Convergence during a massive perimeter breach on the Setu viaducts.

3. **Season 3 (Volumes 7–9): "The Ancient Cataclysm & The Abyssal Crusade"**
   - Expands into Era 2 historical flashbacks, revealing the fall of **Emperor Shrutayudh** into Seal 7.
   - Unites all seasonal protagonists across shards for the final campaign across the Grand Aegis.

---

"""
    text = text[:idx_s3] + new_s3_and_s4 + text[idx_s5:]
    print("Replaced Section 3 and Section 4 successfully!")

# Clean bloated titles
text = text.replace('General Vajran', 'Setu Commander Vajraketu')
text = text.replace('Inquisitor Satyak', 'Setu Inquisitor Satyaketu')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("18_Narrative_Veil_Protocol.md updated cleanly!")
