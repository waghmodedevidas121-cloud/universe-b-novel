# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = r"d:\Web Novel\Brahmand"

def clean_file(rel_path, replacements):
    path = os.path.join(ROOT, rel_path)
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    for tgt, rep in replacements:
        if tgt in text:
            text = text.replace(tgt, rep)
        else:
            print(f"Target not found in {rel_path}: {tgt[:30]}...")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Cleaned {rel_path}")

# 1. 01_WORLD_BIBLE/00_Sanatan_Encyclopedic_Codex.md
clean_file(r"01_WORLD_BIBLE\00_Sanatan_Encyclopedic_Codex.md", [
    ("When Neel falls through the dimensional fissure at Dadar Station, his transit through the outer perimeter of these causal waters subjects his modern electronics to catastrophic electromagnetic stress, completely vaporizing all microchips, lithium cells, and AI software.",
     "When an unascended soul or foreign relic crosses the outer perimeter of these causal waters, all foreign micro-structures, unnatural materials, and artificial constructs are subjected to catastrophic electromagnetic stress and completely vaporized."),
    ("Contrast with consecrated Astras. Governs weapons like **KĀLĪ** (Neel's spiked iron shackle).",
     "Contrast with consecrated Astras. Governs weapons like **KĀLĪ** (the archetypal spiked black-iron shackle)."),
    ("Neel arrives with ₹11 Mumbai change (a crumpled ₹10 note and an aluminum-bronze ₹1 coin). The ₹10 note is laughed at as worthless colorful paper; the ₹1 coin is sold as a metallurgical novelty for merely 2 Copper Māṣas.",
     "Foreign coins and fiat paper from outside the cosmos possess zero legal tender value. Paper currency is laughed at as worthless colorful waste; unusual alloys are sold merely as metallurgical scrap for 1 or 2 Copper Māṣas."),
    ("Neel’s physical body in *Brahmand*. Neel possesses **zero divine radiance**, zero immortal bloodlines, and zero cybernetic enhancements.",
     "The physical biological vessel of an unascended human. Mortal flesh possesses **zero divine radiance**, zero celestial bloodlines, and zero unnatural enhancements."),
    ("Neel feels the brutal physical reality of combat: bruised ribs, blistered palms, torn rotator cuffs, and caloric depletion. However, having zero divine radiance makes him virtually invisible to high-tier astral detection arrays.",
     "A mortal warrior feels the brutal physical reality of combat: bruised ribs, blistered palms, torn ligaments, and caloric depletion. However, having zero divine radiance makes them virtually invisible to high-tier astral detection arrays."),
    ("Neel is **नही** an invincible superhero who shrugs off heavy impacts. He survives through physics, positioning, and pain tolerance.",
     "A mortal warrior is **नही** an invincible entity who shrugs off heavy impacts. They survive through physics, positioning, and pain tolerance."),
    ("Outside combat, Neel loops it diagonally across his chest and waist as an **ascetic iron bandolier**, distributing the deadweight across his pelvic core and spine via Apāna grounding to prevent elbow dislocation.",
     "Outside combat, the wielder loops it diagonally across chest and waist as an **ascetic iron bandolier**, distributing the deadweight across the pelvic core and spine via Apāna grounding to prevent elbow dislocation.")
])

# 2. 01_WORLD_BIBLE/01_Cosmology_and_The_Trinity_Mandate.md
clean_file(r"01_WORLD_BIBLE\01_Cosmology_and_The_Trinity_Mandate.md", [
    ("""3. **Why Neel Loses Everything:**
- When 19-year-old Neel from Mumbai is sucked into the trans-dimensional glitch, he passes through the outermost fringe of the Singularity Apex.
- The high-dimensional compression **destroys all modern technology instantly**: his iPhone battery dies, semiconductor chips vaporize into carbon ash, and the artificial neural algorithms of Earth are completely purged.
- Neel arrives in Central City with only his biological human body, his worn clothes, ₹11 in useless copper-nickel coins, his engineering intellect, and his raw mortal grit!""",
     """3. **The Purge of Foreign Technology:**
- When any entity or object from outside the cosmos crosses the high-dimensional barrier of the Singularity Apex, the intense causal compression **destroys all modern technology instantly**: batteries overheat, microchips vaporize into grey carbon ash, and artificial circuits collapse.
- Any mortal survivor arrives in Central City with only their biological human body, plain garments, and raw mortal grit!"""),
    ("│ • Origin of Neel's cursed iron shackle KALI.", "│ • Origin of the cursed abyssal iron shackle KALI.")
])

# 3. 01_WORLD_BIBLE/02_The_Five_Realms_and_Central_City.md
clean_file(r"01_WORLD_BIBLE\02_The_Five_Realms_and_Central_City.md", [
    ("**(Where Neel first arrives in Chapter 1!)**", "**(The primary terminal for inter-realm grain convoys and new arrivals)**")
])

# 4. 01_WORLD_BIBLE/04_Bila_Svarga_Patala_and_The_Corrupted_Chasm.md
clean_file(r"01_WORLD_BIBLE\04_Bila_Svarga_Patala_and_The_Corrupted_Chasm.md", [
    ("### 5.1 How Neel Operates KALI\nNeel acquires KALI from an ancient subterranean ruin outside Central City:\n1. **The Symbiotic Bond:** KALI is bound to Neel’s left wrist. The Preta spirit within the iron is trapped; if Neel dies, the Preta remains locked in a cold corpse. Thus, the spirit is forced to cooperate with Neel's will.\n2. **The Apāna Grounding Pull:** In combat:\n- Neel drops his hips into the ground (Apāna grounding).\n- He whips the heavy barbed chain forward, wrapping it around an enemy's ankle or neck.\n- With a violent hip jerk, he yanks the chain backward, leveraging Newton’s third law.\n- The opponent stumbles into a dead zone, allowing Neel to deliver a mortal physical strike.\n3. **The Brutal Cost:** Every activation sends a shock of freezing necrotic agony through Neel's left forearm, leaving his fingers numb and frostbitten. **There are zero free superpowers!**",
     "### 5.1 How a Mortal Wielder Operates KALI\nKALI is recovered from an ancient subterranean storm drainage conduit outside Central City:\n1. **The Symbiotic Bond:** KALI binds permanently to the wielder's left wrist and forearm. The Preta spirit within the iron is trapped; if the host perishes, the spirit remains entombed in a cold corpse. Thus, the spirit is forced into symbiotic cooperation.\n2. **The Apāna Grounding Pull:** In combat:\n- The warrior drops their hips into the flagstones (Apāna grounding).\n- They whip the heavy barbed chain forward, snaring an enemy's ankle or weapon shaft.\n- With a violent hip torque, they yank the chain backward, leveraging Newton’s third law to pull the heavier adversary off balance.\n3. **The Brutal Cost:** Every activation sends a shock of freezing necrotic agony through the left forearm, leaving fingers numb and frostbitten. **There are zero free superpowers!**")
])

# 5. 01_WORLD_BIBLE/05_Cosmic_Eras_and_The_Seven_Nightmares.md
clean_file(r"01_WORLD_BIBLE\05_Cosmic_Eras_and_The_Seven_Nightmares.md", [
    ("• The Glitch: 19-year-old Neel is pulled from Dadar Station into the Central City outskirts!",
     "• The Void Glitch: Spatial fractures occasionally discharge unindexed foreign matter and souls onto the Central City outskirts!"),
    ("""### 5.2 The Dadar Station Anomaly: Neel's Arrival
- In the final days before the Proving Games Season begins, a localized causal tear opens beneath an urban bridge in Root Universe A (Mumbai, Earth).
- 19-year-old **Neel**, standing under the Dadar station flyover with a dead smartphone and ₹11 change, is caught in an anomalous spatial shear caused by a runaway Shadow Anchor dial in Central City.
- His arrival is **नही** a chosen hero's divine summoning; it is an administrative error in the causal slipstream—a mortal piece of street flotsam washed ashore in a titanic, unforgiving alien cosmos.""",
     """### 5.2 The Causal Void Glitch: Trans-Dimensional Flotsam
- In the days leading up to major celestial alignments, localized causal shears open along the boundary between Universe A and Universe B.
- Unindexed souls or matter caught near an anomalous spatial shear are drawn through the Kshira Sagara boundary and discharged into Central City.
- Such arrivals are **नही** chosen heroes of divine prophecy; they are administrative anomalies in the causal slipstream—mortal flotsam washed ashore in a titanic, unforgiving cosmos that does not care whether they live or die.""")
])

# 6. 02_POWER_SYSTEM/01_The_Six_Epic_Pillars.md
clean_file(r"02_POWER_SYSTEM\01_The_Six_Epic_Pillars.md", [
    ("Elite street fighters like Neel read this localized crystalline shear hum to dive behind basalt bastions or pull armored enemies into the blast zone.",
     "Elite frontline fighters read this localized crystalline shear hum to dive behind basalt bastions or pull armored enemies into the blast zone.")
])

# 7. 02_POWER_SYSTEM/04_The_Proving_Games_and_Split_Flap_Spire.md
clean_file(r"02_POWER_SYSTEM\04_The_Proving_Games_and_Split_Flap_Spire.md", [
    ("Neel's crumpled ₹11 Indian rupee notes from Dadar Station are laughed at as worthless colorful paper scraps by the bookmakers.",
     "Foreign coins and strange paper bills are laughed at as worthless colorful scrap by the bookmakers."),
    ("When Neel enters the sands with his rusted spiked chain (*KALI*), looking like an underfed vagrant, the odds against him are astronomical—creating explosive financial windfalls for those who notice his street ruthlessness.",
     "When an unknown vagrant enters the sands with a rusted chain, looking like an underfed feeder, the odds against them are astronomical—creating explosive financial windfalls for astute gamblers who recognize gritty survival instinct."),
    ("## 7. Neel's Entry into the Proving Games: The Disruption", "## 7. The Unranked Contender's Entry: The Arena Disruption")
])

# 8. 02_POWER_SYSTEM/05_Tier_Naming_and_Language_Hierarchy.md
clean_file(r"02_POWER_SYSTEM\05_Tier_Naming_and_Language_Hierarchy.md", [
    ("and NEEL's inner monologue / dialogue!", "and common street brawler dialogue!"),
    ("- **Who Speaks It:** Outer slum carters, dung-cart loaders, unranked arena feeders, and **Neel**.",
     "- **Who Speaks It:** Outer slum carters, dung-cart loaders, and unranked arena feeders."),
    ("""- **Neel's Voice:** Neel speaks a sharp, street-smart Mumbai Hinglish/Marathi register, blending practical modern observation with gritty survivor pragmatism.
  - *Example:* Instead of saying *"O venerable Asura, spare my mortal prana,"* Neel says: *"Chal nikal! Two Mashas is the price, take it or shove it."*""",
     """- **Street Register Voice:** Unranked pit brawlers speak a sharp, cynical, street-smart register, blending practical trade observation with gritty survivor pragmatism.
  - *Example:* Instead of saying *"O venerable warrior, grant me quarter,"* a pit fighter mutters: *"Two Mashas is the price; take it or choke on your blood."*"""),
    ("## 4. Protagonist Linguistic Mechanics: How Neel Bridges the Gap",
     "## 4. Linguistic Adaptation: How Foreign Travelers Bridge the Gap"),
    ("""A critical worldbuilding question: **Since 100% of modern technology and AI chips were vaporized during the Kshira Sagara crossing, how does Neel understand the inhabitants of Central City without an AI translator?**

The novel firmly rejects the lazy anime trope of an *"All-Tongue Comprehension Skill"* or a magical ear-bud translation chip. Neel's ability to communicate is grounded in **real historical linguistics and street smarts**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        NEEL'S THREE LINGUISTIC BRIDGES                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Prakrit Cognates (प्राकृत साम्य):                                                    │
│    Central City's trade language is Vyavahāra-Prākṛt—an archaic ancestor of Indo-Aryan │
│    languages. Common street terms (Māṣa, Paṇa, Rājā, Mṛtyu, Śata, Anna, Jala, Aśva)    │
│    are immediately intuitive to Neel's Mumbai street ear!                              │
│                                                                                        │
│ 2. Acoustic Astra Tells (अस्त्र-ध्वनीशास्त्र):                                         │
│    When high-born champions chant Layer 2 Sanskrit Astras, Neel doesn't translate      │
│    the poetry. He reads the physical acoustics: the 0.2s Gūñja tells him the vector,   │
│    velocity, and elemental heat of the incoming strike!                                │
│                                                                                        │
│ 3. Tactical Body Language & Numbers:                                                   │
│    In the Proving Games and betting stalls, numbers are universal. A bookmaker holding │
│    up three fingers and pointing at a blood slip means 3 Silver Panas. Neel's street    │
│    hustle does the rest.                                                               │
└────────────────────────────────────────────────────────────────────────────────────────┘
```""",
     """A critical worldbuilding question: **Without magical translation spells, how do travelers and foreign arrivals understand the inhabitants of Central City?**

The novel firmly rejects the lazy anime trope of an *"All-Tongue Comprehension Skill"* or a magical translation interface. Communication is grounded in **real historical linguistics, shared roots, and physical context**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        THE THREE NATURAL LINGUISTIC BRIDGES                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Prakrit Cognates (प्राकृत साम्य):                                                    │
│    Central City's trade language is Vyavahāra-Prākṛt—the root of pan-astral commerce.  │
│    Core terms (Māṣa, Paṇa, Rājā, Mṛtyu, Anna, Jala, Aśva, Lauha) share immediate       │
│    etymological roots across all human trade dialects.                                 │
│                                                                                        │
│ 2. Acoustic Astra Tells (अस्त्र-ध्वनीशास्त्र):                                         │
│    When high-born champions chant Layer 2 Sanskrit Astras, a defender doesn't translate│
│    the poetry. They read the acoustics: the 0.2s Gūñja reveals the vector, velocity,   │
│    and elemental frequency of the incoming strike!                                     │
│                                                                                        │
│ 3. Tactical Body Language & Currency Tokens:                                           │
│    In the Proving Games and betting stalls, numbers are tactile. A bookmaker holding   │
│    up three fingers and pointing at a stamped copper token means 3 Silver Panas.       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```""")
])

print("Finished cleaning World Bible and Power System files!")
