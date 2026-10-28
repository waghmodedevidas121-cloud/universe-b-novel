# -*- coding: utf-8 -*-
"""
Syncs New/characters/roster.md and New/08_Character_Roster.md to 120 canonical profiles.
Maintains 100% schema alignment with build_character_codex.py and verify_index.py.
"""
import os
import re

root_dir = r"D:\Web Novel\UNIVERSE B"
roster_path = os.path.join(root_dir, "New", "characters", "roster.md")
mirror_path = os.path.join(root_dir, "New", "08_Character_Roster.md")

# New Character Entries to add / update
new_hum_entries = """
---

### [CHR-HUM-16] Karna (कर्ण) — "The Sunless Arrow"
- **Role & Faction (गट व भूमिका):** Independent Contender & Outcast Archer; Yamuna-Ghat & Hastinapur Iron-Akhara.
- **Planetary Shard & Location (स्थान):** Human Planetary Shard (मानव ग्रह-खंड) | Yamuna-Ghat & Hastinapur
- **Power Bracket & Scale Band (साधना-स्तर):** C-Rank -> B-Rank (Awakened Native Prodigy) | T2 (Ascending Vanguard)
- **Quirk & Magic (सक्रिय कौशल्ये):** Solar-Ash Ignition & Blind-Ear Archery (Ignites arrows with searing ash; shoots targets purely by acoustic tells).
- **Bonded Beast & Mount (सहजीवी बंध):** None (Fiercely independent; walks on foot).
- **Weaponry & Arsenal (शस्त्रागार):** Charred Stage-2 Horn Bow (*Surya-Chap*) & congenital golden collarbone shard.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 19 (Rising Outcast Prodigy).
- **Moral Stance (नैतिक स्थिती):** Chaotic Good / Loyal Neutral. Despises elitism; fiercely loyal to anyone who treats him with dignity.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Found floating in a reed basket on the Yamuna river. At age twelve, walked forty miles barefoot to Drona-Vana Academy, outshot every noble child, and was thrown out because he possessed no clan seal. Taught himself archery by shooting falling leaves in the dark. Aims to win the Proving Games and defeat royal prodigy Arjun.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* C-Rank -> B-Rank | T2 (Ascending Vanguard)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Solar-Ash Ignition: Ash-Arrow Burst, Blind-Ear Acoustic Aim]
  - *अधिकृत शस्त्रागार (Arsenal):* Surya-Chap (Stage-2 Horn Bow) & obsidian-tipped hunting arrows

---

### [CHR-HUM-17] Arjun (अर्जुन) — "The Gale Scion"
- **Role & Faction (गट व भूमिका):** #1 Prodigy of Drona-Vana Royal War Academy; Royal House of Hastinapur.
- **Planetary Shard & Location (स्थान):** Human Planetary Shard (मानव ग्रह-खंड) | Drona-Vana Royal War Academy
- **Power Bracket & Scale Band (साधना-स्तर):** B-Rank Prodigy | T2 (Elite Academic Vanguard)
- **Quirk & Magic (सक्रिय कौशल्ये):** Bolt-Gale Convergence & Ambidextrous Shot (*Savyasachi* — shoots with equal accuracy from either hand).
- **Bonded Beast & Mount (सहजीवी बंध):** Storm-Falcon (Stage 2 Bonded — Crested Firehawk sub-variant).
- **Weaponry & Arsenal (शस्त्रागार):** Stage-2 Silver-Inlaid Greatbow & wind-shear recurve shortbow.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 18 (Royal Academy Prodigy).
- **Moral Stance (नैतिक स्थिती):** Lawful Good. Noble warrior troubled by social hypocrisy.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Orphaned nephew of King Parikshit; trained under General Ugra's harsh boot-camp. Has never lost an academy duel, but privately agonizes over having stayed silent when Karna was unfairly expelled six years ago.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* B-Rank Prodigy | T2 (Elite Academic Vanguard)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Bolt-Gale: Sonic Arrow Slipstream, Ambidextrous Dual Draw]
  - *अधिकृत शस्त्रागार (Arsenal):* Stage-2 Silver-Inlaid Greatbow & lightning-fletched quivers

---

### [CHR-HUM-18] Dhruv (ध्रुव) — "The Broken Scion"
- **Role & Faction (गट व भूमिका):** Rookie Adventurer & Last Bloodline Descendant of Seal 7 (Emperor Shrutayudha); Ekachakra Village to Hastinapur Guild.
- **Planetary Shard & Location (स्थान):** Human Planetary Shard (मानव ग्रह-खंड) | Ekachakra Village & Hastinapur Guild
- **Power Bracket & Scale Band (साधना-स्तर):** Starts at Ember/D-Rank -> Awakens C/B-Rank | T1 -> T2 (Awakening Bloodline)
- **Quirk & Magic (सक्रिय कौशल्ये):** Cold-Iron Resonance & Void-Chain Spark (Channels anti-miasma pulses through meteoric iron).
- **Bonded Beast & Mount (सहजीवी बंध):** Pack-Dog (Stage 0 Juvenile Utility).
- **Weaponry & Arsenal (शस्त्रागार):** Broken Meteoric Chain-Link (Ancestral relic) & chipped iron arming sword.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 18 (Seal-7 Bloodline Heir).
- **Moral Stance (नैतिक स्थिती):** Neutral Good. Reluctant hero driven by duty to family and survival.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Raised by his crippled aunt Pritha in Ekachakra. Believed his ancestor Shrutayudha was simply a heroic king who died in Era 2. When rogue Devils attack, his rusted chain drinks dark miasma like water, drawing the attention of both the Hollow Sect and Inquisitor Devi.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* D-Rank -> C/B-Rank | T1 -> T2 (Awakening Bloodline)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Void-Resonance: Cold-Iron Pulse, Miasma Siphon]
  - *अधिकृत शस्त्रागार (Arsenal):* Broken Meteoric Chain-Link & iron sword

---

### [CHR-HUM-19] Pritha (पृथा) — "The Iron-Chain Matron"
- **Role & Faction (गट व भूमिका):** Former B-Rank Border Vanguard & Matron of Ekachakra Village; Shrutayudha Royal Bloodline.
- **Planetary Shard & Location (स्थान):** Human Planetary Shard (मानव ग्रह-खंड) | Ekachakra Border Village
- **Power Bracket & Scale Band (साधना-स्तर):** Former B-Rank Vanguard (Meridian-Crippled) | T1 (Elder Veteran)
- **Quirk & Magic (सक्रिय कौशल्ये):** Chain-Binding Ward & Ancient Meridian Perception.
- **Bonded Beast & Mount (सहजीवी बंध):** None (Beast perished during border retreat).
- **Weaponry & Arsenal (शस्त्रागार):** Runic walking crutch with concealed stiletto blade.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 42 (Crippled Frontline Veteran).
- **Moral Stance (नैतिक स्थिती):** Lawful Good. Fiercely protective mother-figure carrying dangerous historical truth.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Ventured near the southern border twenty years ago to research Shrutayudha's fate. Intercepted by a High Council Palak who crippled her left leg's meridians and warned that the Setu would erase her family if the truth of Seal 7 came to light.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* Former B-Rank (Meridian-Damaged) | T1 (Elder Veteran)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Wards: Iron-Chain Meridian Snare, Danger Acoustic Sense]
  - *अधिकृत शस्त्रागार (Arsenal):* Runic ironwood walking crutch

---

### [CHR-HUM-20] Reva (रेवा) — "The Frost-Blade"
- **Role & Faction (गट व भूमिका):** Silver-Tag Duelist; Hastinapur Adventurer Guild & Drona-Vana Academy; Himavan Clan (Half-Deva).
- **Planetary Shard & Location (स्थान):** Human Planetary Shard (मानव ग्रह-खंड) | Hastinapur Adventurer Guild
- **Power Bracket & Scale Band (साधना-स्तर):** C-Rank (80–90% Bracket) | T2 (Guild Striker)
- **Quirk & Magic (सक्रिय कौशल्ये):** Permafrost Bite & Ice-Mirror Step (Coats blade in sub-zero frost and creates momentary refractive decoys).
- **Bonded Beast & Mount (सहजीवी बंध):** Rime Viper (Stage 1 Juvenile).
- **Weaponry & Arsenal (शस्त्रागार):** Glass-Steel Rapier & silver parrying dagger.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 18 (Exiled Half-Blood Prodigy).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Guarded, proud, and quietly desperate for genuine camaraderie.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Daughter of an exiled Amaravati Deva handmaiden and a human caravan guard. Banished down the Sun-Cliff Arch at age eight when her mother succumbed to Solar Fever. Member of Neel's Central City inner circle.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* C-Rank (80–90% Bracket) | T2 (Guild Striker)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Frost-Steel: Permafrost Piercing Thrust, Refraction Step]
  - *अधिकृत शस्त्रागार (Arsenal):* Glass-Steel Rapier & silver parrying dagger

---

### [CHR-HUM-21] Shakuni (शकुनी) — "The Dice-Master"
- **Role & Faction (गट व भूमिका):** Border Duke of Gandhara House & Secret Sovereign Patriarch of *The Hollow Sect*.
- **Planetary Shard & Location (स्थान):** Human Planetary Shard (मानव ग्रह-खंड) | Hastinapur Royal Court & Underworld
- **Power Bracket & Scale Band (साधना-स्तर):** A-Rank Rogue Summoner | T3 (Underworld Mastermind)
- **Quirk & Magic (सक्रिय कौशल्ये):** Probability Twist (Bone-Dice) & Illusion-Weaving (Distorts karmic odds and disguises dark summoning circles).
- **Bonded Beast & Mount (सहजीवी बंध):** Night Stalker Panther (Stage 2 Bonded — Corrupted).
- **Weaponry & Arsenal (शस्त्रागार):** Carved Devil-bone dice & concealed poisoned folding fan.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 47 (Aristocratic Conspirator).
- **Moral Stance (नैतिक स्थिती):** Neutral Evil. Vengeful, patient nihilist working to shatter the cosmic seals.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** A smiling, limping border duke who acts as Chancellor Sharadvat's financial adviser by day, while funding illegal Devil-summoning cabals and plotting to reverse the Five-Arch Rotunda mechanisms.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* A-Rank Rogue Mastermind | T3 (Underworld Mastermind)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Cursed Probability: Bone-Dice Karma Twist, Shadow Miasma Screen]
  - *अधिकृत शस्त्रागार (Arsenal):* Devil-bone loaded dice & poisoned folding fan

---

### [CHR-HUM-22] Kamsa (कंस) — "The Slave-Summoner"
- **Role & Faction (गट व भूमिका):** Provincial Warlord of Yamuna-Ghat & Illegal Type-1 Summoner; Bhoja Dynasty.
- **Planetary Shard & Location (स्थान):** Human Planetary Shard (मानव ग्रह-खंड) | Yamuna-Ghat River Fortresses
- **Power Bracket & Scale Band (साधना-स्तर):** B-Rank Warlord | T2 (Provincial Tyrant)
- **Quirk & Magic (सक्रिय कौशल्ये):** Heavy Iron-Skin & Sound-Roar (Thickens skin against blade impacts and looses concussive sonic cries).
- **Bonded Beast & Mount (सहजीवी बंध):** Silt-Breaker Boar (Stage 2 Bonded).
- **Weaponry & Arsenal (शस्त्रागार):** Golden-iron executioner's cleaver & barbed iron net.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 44 (Provincial Despot).
- **Moral Stance (नैतिक स्थिती):** Lawful Evil. Brutal merchant-tyrant who treats Otherworlders as disposable weapons.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Runs an illicit subterranean summoning ring beneath his Yamuna palace, using Rigvedic Oath-Collars to enslave summoned Otherworlders before Kael broke free.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* B-Rank Warlord | T2 (Provincial Tyrant)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Tectonic Force: Iron-Skin Deflection, Stun Roar]
  - *अधिकृत शस्त्रागार (Arsenal):* Golden-iron executioner's cleaver & barbed oath-collars
"""

new_asu_entries = """
---

### [CHR-ASU-16] Rudrakh (रुद्रख / Rudr) — "The Asura Berserker"
- **Role & Faction (गट व भूमिका):** Red Crucible Union Brawler & Proving Games Contender; Disciple of Marshal Hilda.
- **Planetary Shard & Location (स्थान):** Asura Planetary Shard (असुर ग्रह-खंड) | Red Crucible Foundries & Central City
- **Power Bracket & Scale Band (साधना-स्तर):** B-Rank Vanguard | T2 (Rising Heavy Striker)
- **Quirk & Magic (सक्रिय कौशल्ये):** Magma-Blood Overdrive & Spiked-Knuckle Brawling (Heats blood to ignition point, unleashing explosive punches).
- **Bonded Beast & Mount (सहजीवी बंध):** Cinder-Boar (Stage 2 Bonded — Trench-Breaker Line).
- **Weaponry & Arsenal (शस्त्रागार):** Twin volcanic slag cesti (spiked gauntlets) & heavy iron greaves.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 19 (Caldera Contender).
- **Moral Stance (नैतिक स्थिती):** Chaotic Good. Hot-headed, fiercely loyal pit-fighter fighting to fund Matron Olga's orphanage.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Ulka's hot-headed younger cousin. Enters the Proving Games feeder circuit to win bounty gold for orphanages in the smelting slums, quickly forming a brawler rivalry with Karna, Arjun, and Neel.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* B-Rank Vanguard | T2 (Rising Heavy Striker)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Magma-Blood: Slag Ignition Overdrive, Tectonic Impact Gauntlet]
  - *अधिकृत शस्त्रागार (Arsenal):* Twin volcanic slag cesti & heavy iron greaves
"""

new_bst_entries = """
---

### [CHR-BST-09] Tara (तारा / Maya-Ri) — "The Silent Whisperer"
- **Role & Faction (गट व भूमिका):** Shamanic Beast-Whisperer & Scout; Hollow-Grove Shamans & Pan-Astral Adventurer Guild.
- **Planetary Shard & Location (स्थान):** Beast Planetary Shard (श्वापद ग्रह-खंड) | Hollow Ironwood Grove & Central City
- **Power Bracket & Scale Band (साधना-स्तर):** C-Rank (80–90% Bracket) | T2 (Beast Specialist)
- **Quirk & Magic (सक्रिय कौशल्ये):** Dual Soul-Bond Empathy & Pheromone Camouflage (Communicates wordlessly with beasts and synchronizes breathing).
- **Bonded Beast & Mount (सहजीवी बंध):** Ghost-Panther (Stage 2 Bonded) & Rime-Viper (Stage 1 Juvenile).
- **Weaponry & Arsenal (शस्त्रागार):** Ironwood shortbow & bone skinning knives.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 17 (Canopy Shaman Apprentice).
- **Moral Stance (नैतिक स्थिती):** Neutral Good. Quiet, observant protector of forest wildlife and core member of Neel's circle.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Shaman Morvath's apprentice whose vocal cords were damaged during an illegal Devil-raid. Speaks through rhythmic hand-taps and beast gestures; teaches Neel how to achieve true Meridian Synchronization.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* C-Rank (80–90% Bracket) | T2 (Beast Specialist)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Beast Soul-Bond: Meridian Sync Pulse, Silent Forest Camouflage]
  - *अधिकृत शस्त्रागार (Arsenal):* Ironwood shortbow & bone skinning knives

---

### [CHR-BST-10] Takshak (तक्षक) — "The Venom-Lord"
- **Role & Faction (गट व भूमिका):** Rogue Naga Warlord & Rebel Patriarch; Splinter Brood of Bhogavati.
- **Planetary Shard & Location (स्थान):** Beast Planetary Shard (श्वापद ग्रह-खंड) | Sunken Caverns & River-Border Rifts
- **Power Bracket & Scale Band (साधना-स्तर):** S-Rank Rogue Apex Beast | T4 (Sovereign Serpent Warlord)
- **Quirk & Magic (सक्रिय कौशल्ये):** Boiling-Venom Breath & Human Flesh-Shifting (Exhales vapor that melts armor and assumes half-human guise).
- **Bonded Beast & Mount (सहजीवी बंध):** None (Sovereign Apex Predator).
- **Weaponry & Arsenal (शस्त्रागार):** Two curved black-jade daggers dipped in ancient *Halahala* derivative.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 310 (Immortal Serpent Warlord).
- **Moral Stance (नैतिक स्थिती):** Chaotic Evil / Militant Ethnocentric. Despises humanity and seeks the reclamation of all rivers.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Empress Jormun's radical nephew who broke away from the Great Beast Accord, covertly aiding the Hollow Sect to breach river-basin wards.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* S-Rank Rogue Apex Beast | T4 (Sovereign Serpent Warlord)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Naga Primordial: Caustic Vapor Torrent, Jade Scale Carapace]
  - *अधिकृत शस्त्रागार (Arsenal):* Twin black-jade venom daggers
"""

new_aby_section = """# PART 7: THE CORRUPTED REALM (अधो-लोक — Tier 4 Devils, Exiles & Seal 7)
*The Grand Aegis, Netherholme Hunger Throne, Aegis-Light Enclave & The Dead Chasm*

---

### [CHR-ABY-01] Paundra (पौंड्रक / Paundraka) — "The Counterfeit Sovereign"
- **Role & Faction (गट व भूमिका):** Overlord of Netherholme Throne & Sovereign Patriarch of the Hunger Devils.
- **Planetary Shard & Location (स्थान):** Corrupted Realm (अधोलोक — Tier 4) | Netherholme Obsidian Citadel
- **Power Bracket & Scale Band (साधना-स्तर):** Ati-Maharathi (T6 Corrupted Sovereign) | Equivalent to S-Rank+
- **Quirk & Magic (सक्रिय कौशल्ये):** Siphon-Void Dominion & Counterfeit Astra-Mimicry (Drains ambient Prana and projects hollow illusory Astras).
- **Bonded Beast & Mount (सहजीवी बंध):** Abyssal Dread-Hound (Stage 3 Apex Corrupted).
- **Weaponry & Arsenal (शस्त्रागार):** The False Sudarshana (Four-bladed black iron chakra) & bone sceptre.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 2 to Present | Age 1,800+ (Mutated Primordial Devil).
- **Moral Stance (नैतिक स्थिती):** Chaotic Evil / Megalomaniacal. Despises upper-world Devas; seeks to breach the Grand Aegis.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Declared himself a true god after mutating during the Era 2 Cataclysm. Rejects the peaceful sustenance of the Grand Aegis, commanding millions of starving Hunger Devils and conspiring with upper-world cultists to hijack mortal bodies.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* Ati-Maharathi (T6 Corrupted Sovereign)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Void Siphon: Prana Collapse, Counterfeit Chakra Projection]
  - *अधिकृत शस्त्रागार (Arsenal):* The False Sudarshana & obsidian war-sceptre

---

### [CHR-ABY-02] General Vritra (वृत्र / Shataghati) — "The Bone Behemoth"
- **Role & Faction (गट व भूमिका):** Supreme Warlord of the Dread-Hold Legion; Hunger Faction Vanguard.
- **Planetary Shard & Location (स्थान):** Corrupted Realm (अधोलोक — Tier 4) | Dread-Hold Bastion
- **Power Bracket & Scale Band (साधना-स्तर):** Maharathi (T6 Corrupted Warlord) | 100-ft Tectonic Behemoth
- **Quirk & Magic (सक्रिय कौशल्ये):** Mountain-Shatter Stride & Bone-Plate Carapace (Generates seismic shocks with each footstep and shrugs off siege artillery).
- **Bonded Beast & Mount (सहजीवी बंध):** None (Colossal walking fortress).
- **Weaponry & Arsenal (शस्त्रागार):** Basalt siege mace carved from sunken mountain core.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 2 to Present | Age 1,900+ (Ancient Devil Titan).
- **Moral Stance (नैतिक स्थिती):** Lawful Evil. Relentless frontline general bound by harsh warrior hierarchy.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** A cyclopean titan of calcified bone and hardened basalt. Direct rival to Setu General Vajra, awaiting the day the Aegis weakens to clash thunderbolt against mountain-mace.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* Maharathi (T6 Corrupted Warlord)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Tectonic Siege: Seismic Ground Collapse, Unbreakable Bone Carapace]
  - *अधिकृत शस्त्रागार (Arsenal):* Basalt siege mace & iron chain-whips

---

### [CHR-ABY-03] Trishir (त्रिशिरा / Trishira) — "The Three-Minded Weaver"
- **Role & Faction (गट व भूमिका):** Chief Alchemist & Devil Ritualist; Shadow-Hollow Coven.
- **Planetary Shard & Location (स्थान):** Corrupted Realm (अधोलोक — Tier 4) | The Rotting Fens
- **Power Bracket & Scale Band (साधना-स्तर):** Atirathi (T5 Corrupted Sorcerer) | Master Ritualist
- **Quirk & Magic (सक्रिय कौशल्ये):** Tri-Mind Calculation & Tantric Soul-Thread Weaving (Formulates three forbidden rites simultaneously).
- **Bonded Beast & Mount (सहजीवी बंध):** Chasm Drill-Worm (Stage 2 Subterranean).
- **Weaponry & Arsenal (शस्त्रागार):** Lead ritual athame & bone scroll-tubes containing stolen Agamic rites.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 2 to Present | Age 1,600+ (Alchemical Sorcerer).
- **Moral Stance (नैतिक स्थिती):** Neutral Evil. Coldly intellectual researcher of inter-realm soul transfer.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Possesses three conjoined craniums that debate constantly. Author of the forbidden *Abhichara* summoning manuals smuggled to corrupt upper-world dukes like Shakuni.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* Atirathi (T5 Corrupted Sorcerer)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Cursed Alchemy: Miasma Transmutation, Silver-Cord Severing Snare]
  - *अधिकृत शस्त्रागार (Arsenal):* Lead ritual athame & bone talismans

---

### [CHR-ABY-04] King Bali (महाबली / Bali) — "The Golden-Bound Sovereign"
- **Role & Faction (गट व भूमिका):** Sovereign Monarch of the Aegis-Light Enclaves & Patriarch of the Noble Devils.
- **Planetary Shard & Location (स्थान):** Corrupted Realm (अधोलोक — Tier 4) | Aegis-Light Enclave (Inner Rim)
- **Power Bracket & Scale Band (साधना-स्तर):** Ati-Maharathi (T6 Noble Devil Sovereign) | High Noble Tier
- **Quirk & Magic (सक्रिय कौशल्ये):** Aegis-Prana Absorption, Gravity Dominion & Inviolable Contract Law (Absorbs the golden nectar of the Grand Aegis without mutation; enforces absolute pacts).
- **Bonded Beast & Mount (सहजीवी बंध):** Four-horned Obsidian Bull (Stage 3 Apex).
- **Weaponry & Arsenal (शस्त्रागार):** The Golden Sovereign Sceptre & twin broad daggers.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 2 to Present | Age 2,400+ (Primordial Daitya Sovereign).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral / Tragic Noble. Proves that \"Devil\" does not mean evil; protects honorable souls.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** In Era 2, Bali gathered millions of honorable souls trapped in the south and led them to the foot of the Grand Aegis. Knowing the sages built the barrier to feed them justly, Bali established civilized laws, banning soul-cannibalism and resisting Paundra's madness. Permits Mode-A Symbiotic Contracts with worthy mortals.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* Ati-Maharathi (T6 Noble Devil Sovereign)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Aegis Dominion: Golden Prana Bastion, Inviolable Karmic Oath]
  - *अधिकृत शस्त्रागार (Arsenal):* Golden Sovereign Sceptre & obsidian daggers

---

### [CHR-ABY-05] Vibhishan (विभीषण / Vibhi) — "The Exile Arbiter"
- **Role & Faction (गट व भूमिका):** Chief Scholar & Diplomatic Envoy of the Noble Devils; Aegis-Light Enclaves.
- **Planetary Shard & Location (स्थान):** Corrupted Realm (अधोलोक — Tier 4) | Border Outpost & Aegis Line
- **Power Bracket & Scale Band (साधना-स्तर):** Atirathi (T5 Noble Devil Scholar) | Grand Diplomat
- **Quirk & Magic (सक्रिय कौशल्ये):** Soul-Thread Diagnosis & Anti-Miasma Ward (Detects corruption levels in subtle bodies and calms rabid Devils).
- **Bonded Beast & Mount (सहजीवी बंध):** Silver-Wing Swan (Stage 2 Aquatic).
- **Weaponry & Arsenal (शस्त्रागार):** Inscribed palm-leaf treaty scroll & brass defensive bell.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 2 to Present | Age 1,500+ (Daitya Philosopher).
- **Moral Stance (नैतिक स्थिती):** Lawful Good. Diplomatic peacemaker striving to prevent all-out war with the upper shards.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** King Bali's younger brother. Maintains back-channel communications with Inquisitor Satyak on the Setu and coordinates joint patrols with Ash Fortress exiles.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* Atirathi (T5 Noble Devil Scholar)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Sanctuary Arts: Soul-Thread Repair, Miasma Neutralization Field]
  - *अधिकृत शस्त्रागार (Arsenal):* Inscribed treaty scroll & brass resonance bell

---

### [CHR-ABY-06] Nila (नीला / Kali-Ka) — "The Shadow-Dancer"
- **Role & Faction (गट व भूमिका):** Symbiotic Noble Devil Partner & Shade Assassin; Aegis-Light Court to House Noctis.
- **Planetary Shard & Location (स्थान):** Corrupted Realm / Human Shard | Bonded inside Kael's Shadow
- **Power Bracket & Scale Band (साधना-स्तर):** B-Rank -> A-Rank Scaling | Symbiotic Contract Companion
- **Quirk & Magic (सक्रिय कौशल्ये):** Shadow-Cloak, Curse-Eater Parry & Twin Bone-Blades (Travels within bonded partner's shadow; consumes hostile curses).
- **Bonded Beast & Mount (सहजीवी बंध):** None (Forms symbiotic bond with mortal soul).
- **Weaponry & Arsenal (शस्त्रागार):** Twin carved obsidian bone-blades forged from dead chasm minerals.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 3 to Present | Age 400 (Noble Devil Shade).
- **Moral Stance (नैतिक स्थिती):** Chaotic Good. Feisty, sharp-tongued, fiercely loyal to her bonded partner Kael.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** A sharp-witted Noble Devil who entered an equal **Mode-A Symbiotic Contract** with summoned otherworlder Kael. Resides within his shadow, masking his foreign aura from inquisitors and devouring dark miasma in combat.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* B-Rank -> A-Rank Scaling (Symbiotic Partner)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Shadow Arts: Umbral Armor Imbuement, Curse Consumption Parry]
  - *अधिकृत शस्त्रागार (Arsenal):* Twin obsidian bone-blades

---

### [CHR-ABY-07] Hamsa (हंस) — Senior Warden of The Ash Fortress
- **Role & Faction (गट व भूमिका):** Senior Border Warden; The Ash Fortress Multi-Racial Military Command.
- **Planetary Shard & Location (स्थान):** Corrupted Realm (अधोलोक — Tier 4) | The Ash Fortress
- **Power Bracket & Scale Band (साधना-स्तर):** A-Rank Exile Vanguard | T3 (Border Veteran)
- **Quirk & Magic (सक्रिय कौशल्ये):** Ash-Ward Ignition & Heavy Greatsword Cleave (Channels volcanic ash into burning concussive blade sweeps).
- **Bonded Beast & Mount (सहजीवी बंध):** Ironplate Bear (Stage 2 Bonded).
- **Weaponry & Arsenal (शस्त्रागार):** Six-foot serrated bastard sword forged from tempered chasm slag.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 39 (Frontline Exile Commander).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Hardened veteran holding the line between feral Devils and the upper realm.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Exiled from Hastinapur after refusing to massacre a starving border settlement. Now commands the multi-racial outpost of The Ash Fortress, defending the frontier against Paundra's raiders.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* A-Rank Exile Vanguard | T3 (Border Veteran)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Ash & Flame: Smoldering Greatsword Sweep, Iron Wall Stance]
  - *अधिकृत शस्त्रागार (Arsenal):* Six-foot serrated bastard sword & chasm iron buckler

---

### [CHR-ABY-08] Dambha (दंभ / Dimbaka) — Tactical Warden of The Ash Fortress
- **Role & Faction (गट व भूमिका):** Tactical Scout & Trap-Master; The Ash Fortress Multi-Racial Military Command.
- **Planetary Shard & Location (स्थान):** Corrupted Realm (अधोलोक — Tier 4) | The Ash Fortress
- **Power Bracket & Scale Band (साधना-स्तर):** A-Rank Tactical Vanguard | T3 (Trap & Ambush Specialist)
- **Quirk & Magic (सक्रिय कौशल्ये):** Kinetic Wire-Weaving & Slag Tripwires (Erects razor-sharp tripwire labyrinths in under a minute).
- **Bonded Beast & Mount (सहजीवी बंध):** Razor-Ear Caracal (Stage 2 Bonded).
- **Weaponry & Arsenal (शस्त्रागार):** Spool of monomolecular tungsten-steel wire & twin curved gutting daggers.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 39 (Tactical Master).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Calculating survivalist and Hamsa's lifelong brother-in-arms.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Exiled alongside Hamsa; designed the perimeter defense grids and acoustic sensor tripwires of The Ash Fortress, ensuring no feral Devils cross undetected.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* A-Rank Tactical Vanguard | T3 (Trap Specialist)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Tungsten Wires: Kinetic Decapitation Snare, Acoustic Tell Trap]
  - *अधिकृत शस्त्रागार (Arsenal):* Tungsten wire spool & twin hunting daggers

---

### [CHR-ABY-09] Marich (मारीच / Maricha) — "The Golden Deer"
- **Role & Faction (गट व भूमिका):** Underworld Smuggling Kingpin & Master Illusionist; Boss of *The Abyss Shufflers*.
- **Planetary Shard & Location (स्थान):** Corrupted Realm (अधोलोक — Tier 4) | Ash-Roads & Clandestine Micro-Cracks
- **Power Bracket & Scale Band (साधना-स्तर):** A-Rank Illusionist & Smuggler | T3 (Black Market Boss)
- **Quirk & Magic (सक्रिय कौशल्ये):** Flesh-Shifting Mirage & Shadow-Cloak Step (Assumes the guise of any human, beast, or inanimate cargo crate).
- **Bonded Beast & Mount (सहजीवी बंध):** Golden-Antlered Mirage Elk (Stage 2 Bonded).
- **Weaponry & Arsenal (शस्त्रागार):** Concealed spring-loaded stiletto & flash-powder capsules.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 180 (Long-Lived Shifter).
- **Moral Stance (नैतिक स्थिती):** Chaotic Neutral. Opportunistic broker who trades rare ores for mortal salt and gold.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Controls the illegal transit of chasm-mined runic minerals through pre-Partition Rotary Shadow Anchors, maintaining illicit business accounts with Admiral Silas and Renzo Vance.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* A-Rank Illusionist | T3 (Black Market Boss)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Mirage Shifting: Complete Sensory Camouflage, Decoy Mirage Handoff]
  - *अधिकृत शस्त्रागार (Arsenal):* Concealed stiletto & blinding phosphor flash-bombs

---

### [CHR-ABY-10] Kalmash (कल्माष / Kabandh) — "The Flesh-Collector"
- **Role & Faction (गट व भूमिका):** Rogue Mode-B Hijacked Vessel; Hunger Faction Striker & Body Snatcher.
- **Planetary Shard & Location (स्थान):** Corrupted Realm / Human Frontier | Khandava Perimeter
- **Power Bracket & Scale Band (साधना-स्तर):** A-Rank Abomination | T3 (Hijacked Vessel Monstrosity)
- **Quirk & Magic (सक्रिय कौशल्ये):** Chest-Maw Devouring & Elastic Muscle-Tendrils (Chest splits into vertical tooth-lined maw that drains Prana).
- **Bonded Beast & Mount (सहजीवी बंध):** None (Consumes beasts for meat).
- **Weaponry & Arsenal (शस्त्रागार):** Serrated iron meat-hooks & bone-spikes protruding through skin.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Vessel: Age 34 | Inhabiting Devil: Age 900+ (Parasitic Hijack).
- **Moral Stance (नैतिक स्थिती):** Chaotic Evil. Ravenous monster driven by insatiable hunger for living human Prana.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** A former Gold-Tag adventurer whose vessel was violently hijacked during a botched subterranean summoning rite. Now hunts C-Rank reincarnates and rookie adventurer parties along the cursed border.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* A-Rank Abomination | T3 (Hijacked Vessel)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Flesh-Tear: Chest-Maw Prana Devour, Whipping Muscle Tendril Snare]
  - *अधिकृत शस्त्रागार (Arsenal):* Serrated iron meat-hooks & bone spikes

---

### [CHR-ABY-11] Jaras (जरासंध / Jaras) — "The Split-Body Tyrant"
- **Role & Faction (गट व भूमिका):** Badlands Cult Warlord & Slavemaster; Magadha Blood Cult.
- **Planetary Shard & Location (स्थान):** Corrupted Realm (अधोलोक — Tier 4) | Western Slag Waste Fortress
- **Power Bracket & Scale Band (साधना-स्तर):** A-Rank Half-Asura Outlaw | T3 (Immortal Flesh Boss)
- **Quirk & Magic (सक्रिय कौशल्ये):** Flesh-Stitching Regeneration & Corpse-Prana Pratishtha (Can survive bisection; severed halves pull together via red sinew).
- **Bonded Beast & Mount (सहजीवी बंध):** Two-Headed Lava-Mastiff (Stage 2 Bonded).
- **Weaponry & Arsenal (शस्त्रागार):** Two heavy spiked iron cleavers linked by an eight-foot iron chain.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 85 (Regenerative Half-Asura).
- **Moral Stance (नैतिक स्थिती):** Neutral Evil. Sadistic slave-baron who kidnaps Otherworlders for illicit arena fights.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Rules a cyclopean basalt fortress in the western slag wastes. Cannot be slain by blade wounds alone—unless his bisected body is thrown in opposite directions across running water!
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* A-Rank Half-Asura Warlord | T3 (Immortal Flesh Boss)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Sinew Stitch: Instant Bisection Regeneration, Crushing Chain Cleave]
  - *अधिकृत शस्त्रागार (Arsenal):* Chained executioner cleavers & spiked manacles

---

### [CHR-ABY-12] Emperor Shrutayudha (सम्राट श्रुतायुध) — The Living Seventh Horror (Seal 7)
- **Role & Faction (गट व भूमिका):** Primordial Guardian & Tragic Living Seal of the Seventh Horror; Dead Chasm (Seal 7).
- **Planetary Shard & Location (स्थान):** Corrupted Realm (अधोलोक — Tier 4) | The Dead Chasm (Seal 7 Pit)
- **Power Bracket & Scale Band (साधना-स्तर):** Ati-Maharathi++ (T7 Cosmic Entity) | Transcendent Horror Vessel
- **Quirk & Magic (सक्रिय कौशल्ये):** Rudra-Bound Immortal Flesh, Primordial Void Aura & Sovereign Dread (Absorbs anti-existence to prevent universe collapse).
- **Bonded Beast & Mount (सहजीवी बंध):** Kagabhushundi (CHR-ABY-13 — The Stone-Eyed Crow).
- **Weaponry & Arsenal (शस्त्रागार):** 108 meteoric iron anchor-chains bolted into his skeleton & dead bedrock.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 2 to Present | Age 3,200+ (Chained Immortal Emperor).
- **Moral Stance (नैतिक स्थिती):** Tragic Absolute Neutral / Cosmic Martyr. Sacrificed humanity to keep reality intact.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** In Era 2, Emperor Shrutayudha chained himself over the Seventh Horror to keep the young cosmos from rotting. Over three millennia of holding the entity inside his meridians, his flesh mutated and fused with the Horror itself. Mortals believe he died a hero; in truth, he hangs in darkness under lead seals, half-savior and half-apocalypse.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* Ati-Maharathi++ (T7 Cosmic Horror)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Void Anchor: Reality-Rot Suppression, Tectonic Shockwave Scream]
  - *अधिकृत शस्त्रागार (Arsenal):* 108 meteoric iron chains fused into marrow

---

### [CHR-ABY-13] Kaga (काग / Kagabhushundi) — The Stone-Eyed Crow of the Chasm
- **Role & Faction (गट व भूमिका):** Immortal Avian Chronicler & Sentinel of Seal 7; The Dead Chasm.
- **Planetary Shard & Location (स्थान):** Corrupted Realm (अधोलोक — Tier 4) | The Dead Chasm (Seal 7 Rim)
- **Power Bracket & Scale Band (साधना-स्तर):** B-Rank Lithic Avian | T2 (Immortal Watcher)
- **Quirk & Magic (सक्रिय कौशल्ये):** Far-Hearing, Soul-Sight & Tremor-Sense (Perceives conversations across shards and sings ancient verses).
- **Bonded Beast & Mount (सहजीवी बंध):** Companion to Emperor Shrutayudha.
- **Weaponry & Arsenal (शस्त्रागार):** Petrified stone talons & obsidian beak that never weathers.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 2 to Present | Age 3,200+ (Immortal Lithic Avian).
- **Moral Stance (नैतिक स्थिती):** True Neutral. Silent witness to the rise and fall of mortal civilizations.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Perches upon Shrutayudha's chains, chanting Vedic verses in the dark to preserve the chained emperor's remaining human consciousness.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* B-Rank Lithic Avian | T2 (Immortal Watcher)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Vedic Resonances: Soul-Calm Chant, Far-Hearing Acoustic Link]
  - *अधिकृत शस्त्रागार (Arsenal):* Petrified stone beak & talons
"""

new_div_00_entry = """
### [CHR-DIV-00] Maha-Vishnu (महाविष्णु / Karanodakashayi Vishnu) — Lord of the Causal Ocean
- **Role & Faction (गट व भूमिका):** Primordial Multiversal Source & Supreme Observer; Reclining upon the Causal Ocean (Karana Sagara).
- **Planetary Shard & Location (स्थान):** Beyond Space & Time | Karana Sagara (The Causal Ocean)
- **Power Bracket & Scale Band (साधना-स्तर):** Transcendent Multiversal Source | Incomputable
- **Quirk & Magic (सक्रिय कौशल्ये):** Srishti-Shvasa (Cosmic Breath — universes emerge with His exhalation and dissolve with His inhalation).
- **Bonded Beast & Mount (सहजीवी बंध):** Infinite Shesha (Primordial bed of eternal rest).
- **Weaponry & Arsenal (शस्त्रागार):** The Primordial Blueprint of Reality (*Veda-Mula*).
- **Historical Era & Lifespan (ऐतिहासिक युग):** Beginningless & Endless | Timeless
- **Moral Stance (नैतिक स्थिती):** Transcendent Cosmic Source. Completely impartial and detached from worldly disputes.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Exists outside the boundaries of time, space, and individual universes. His single cosmic exhalation births countless parallel realities (including Universe B). Within Universe B, mortals never perceive Him directly, acknowledging Him only as the Primordial Foundation.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* Transcendent Multiversal Source | Incomputable
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Primordial Origin: Universal Emanation, Yoga-Nidra Consciousness]
  - *अधिकृत शस्त्रागार (Arsenal):* The Primordial Cosmic Law (*Sanatana-Dharma*)

---
"""

new_aln_section = """# PART 9: THE ALIENS DIASPORA (द एलियन्स डायस्पोरा — विस्थापित आधुनिक नश्वर)
*Notable Reincarnated Souls, Otherworlders & Glitch-Drifters Across Universe B*

---

### [CHR-ALN-01] Marcus (मार्कस / Marcus Ward) — Grand Chronicler of the Adventurer Guild
- **Role & Faction (गट व भूमिका):** Chief Historian & Archivist; Hastinapur Adventurer Guild & Ward Family Enclave.
- **Planetary Shard & Location (स्थान):** Human Planetary Shard (मानव ग्रह-खंड) | Hastinapur Guild Archives
- **Power Bracket & Scale Band (साधना-स्तर):** C-Rank (80–90% Reincarnate Bracket) | T2 (Academic Chronicler)
- **Quirk & Magic (सक्रिय कौशल्ये):** Chrono-Recall & Linguistic Sieve (Instantly reads and translates dead scripts from pre-Partition ruins).
- **Bonded Beast & Mount (सहजीवी बंध):** Two-Headed Scout Owl (Stage 2 Bonded — Gale Line).
- **Weaponry & Arsenal (शस्त्रागार):** Heavy leather-bound grimoire & silver stylus.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Reincarnated in Era 4 | Age 48 (Former Earth Scholar).
- **Moral Stance (नैतिक स्थिती):** Lawful Good. Obsessive cataloger of true history across the shards.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Reincarnated via the Yama-Vidhata Contract with an intact modern academic mind. Cataloged over 3,000 Adventurer Guild quest reports and was the first to document the 0.2-second acoustic tell (*The Sing*).
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* C-Rank | T2 (Academic Chronicler)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Scholarly Recall: Rapid Linguistic Decryption, Runic Pattern Sight]
  - *अधिकृत शस्त्रागार (Arsenal):* Silver stylus & enchanted grimoire

---

### [CHR-ALN-02] Donna Beatrice Rosso (दॉना बीट्रिस रोसो) — High Arbitrator of the Core-Exchange
- **Role & Faction (गट व भूमिका):** Chief Financial Arbitrator; Central Reserve Bank & Core-Exchange Vaults.
- **Planetary Shard & Location (स्थान):** Central Planetary Shard (मध्यवर्ती क्षेत्र) | Central City Core-Exchange
- **Power Bracket & Scale Band (साधना-स्तर):** C-Rank (80–90% Reincarnate Bracket) | T2 (Financial Sovereign)
- **Quirk & Magic (सक्रिय कौशल्ये):** Appraiser's Eye & Karmic Ledger Lock (Instantly gauges the true energy density and purity of any Beast-Core).
- **Bonded Beast & Mount (सहजीवी बंध):** Silt-Breaker Boar (Stage 1 Domestic Utility).
- **Weaponry & Arsenal (शस्त्रागार):** Pearl-handled derringer-shaped Aether-wand & golden balance scale.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Reincarnated in Era 4 | Age 54 (Former Earth Banker).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Incorruptible banker who honors contracts above all politics.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Reincarnated from a Venetian banking lineage. Structured the 17% customs clearance system between the outer shards and Central City, stabilizing the Aether-Rupee economy.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* C-Rank | T2 (Financial Sovereign)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Appraisal: Prana Core Density Sight, Counterfeit Detection Ward]
  - *अधिकृत शस्त्रागार (Arsenal):* Golden balance scales & runic Aether-wand

---

### [CHR-ALN-03] Wolfgang Adler (वोल्फगांग अॅडलर) — Master of Runic Ballistas & Siege-Bows
- **Role & Faction (गट व भूमिका):** Master Artificer & Mechanical Engineer; Asura Shard Adler Workshop & Agni-Kunda.
- **Planetary Shard & Location (स्थान):** Asura Planetary Shard (असुर ग्रह-खंड) | Agni-Kunda Smelting Works
- **Power Bracket & Scale Band (साधना-स्तर):** B-Rank Vanguard Artificer | T2 (Master Weapon Engineer)
- **Quirk & Magic (सक्रिय कौशल्ये):** Tensional Calibration & Steel Hardening (Enhances elastic limits and penetration of siege ballistas).
- **Bonded Beast & Mount (सहजीवी बंध):** Cinder-Salamander (Stage 1 Smithy Hearth Cleaner).
- **Weaponry & Arsenal (शस्त्रागार):** Heavy repeating crossbow & tungsten engineering calipers.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Reincarnated in Era 4 | Age 61 (Former Earth Ballistics Engineer).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Passionate craftsman who only builds weapons for defense.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Reincarnated mechanical engineer who revolutionized border artillery for both Asura citadels and Hastinapur watch-towers, forging ballistas that launch runic harpoons into flying drakes.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* B-Rank Vanguard | T2 (Master Engineer)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Mechanical Imbuement: Tensional Ballistic Force, Armor-Piercing Draw]
  - *अधिकृत शस्त्रागार (Arsenal):* Custom heavy repeating crossbow & runic calipers

---

### [CHR-ALN-04] Lucian Valois (ल्युसियन वालुआ) — Master of Prismatic Sun-Wards
- **Role & Faction (गट व भूमिका):** Solar Optical Artificer & Barrier Master; Deva Shard Astral Observatory & House Valois.
- **Planetary Shard & Location (स्थान):** Deva Planetary Shard (देव ग्रह-खंड) | Amaravati Astral Observatory
- **Power Bracket & Scale Band (साधना-स्तर):** C-Rank (80–90% Reincarnate Bracket) | T2 (Solar Lens Master)
- **Quirk & Magic (सक्रिय कौशल्ये):** Prismatic Refraction & Light-Shear Shield (Focuses high-altitude solar rays into hard-light barriers).
- **Bonded Beast & Mount (सहजीवी बंध):** Mist Cygnet (Stage 1 Juvenile Swan).
- **Weaponry & Arsenal (शस्त्रागार):** Prismatic quartz-lens focal staff & silver mirror shield.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Reincarnated in Era 4 | Age 42 (Former Earth Glassmaker).
- **Moral Stance (नैतिक स्थिती):** Lawful Good. Gentle craftsman seeking harmony between mortals and Devas.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Former French optical artisan who designs the giant solar collector lenses in Amaravati that distill restorative Soma nectar for curing high-altitude fevers.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* C-Rank | T2 (Solar Lens Master)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Optics: Prismatic Hard-Light Barrier, Refractive Solar Ray]
  - *अधिकृत शस्त्रागार (Arsenal):* Prismatic quartz staff & mirror shield

---

### [CHR-ALN-05] Renzo Vance (रेन्झो व्हॅन्स / "Kite") — Shadow-Broker of Pit #13
- **Role & Faction (गट व भूमिका):** Clandestine Broker & Shadow-Grid Smuggler; Pit #13 & Vance Family Underworld.
- **Planetary Shard & Location (स्थान):** Human Planetary Shard (मानव ग्रह-खंड) | Hastinapur Pit #13
- **Power Bracket & Scale Band (साधना-स्तर):** B-Rank Shadow Broker | T2 (Underworld Information King)
- **Quirk & Magic (सक्रिय कौशल्ये):** Sound-Absorption Bubble & Frequency Tuning (Masks rotary anchor vibrations and unlocks spatial gears).
- **Bonded Beast & Mount (सहजीवी बंध):** Two-Tailed Mirage Fox (Stage 2 Bonded).
- **Weaponry & Arsenal (शस्त्रागार):** Concealed punch daggers & forged frequency-tuning discs.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Reincarnated in Era 4 | Age 39 (Former Earth Underworld Fixer).
- **Moral Stance (नैतिक स्थिती):** True Neutral. Information merchant who deals with all factions equally.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Operates the clandestine elevator network beneath Hastinapur's Pit #13, trading forbidden chasm ores with Marich and Admiral Silas while keeping tabs on Hollow Sect activity.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* B-Rank Shadow Broker | T2 (Information King)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Stealth Mechanics: 30-ft Acoustic Silence Bubble, Spatial Gear Bypass]
  - *अधिकृत शस्त्रागार (Arsenal):* Concealed punch daggers & frequency discs

---

### [CHR-ALN-06] Neel (नील / The Pulse-Reader) — Primary Glitch-Drifter & Unindexed Hero
- **Role & Faction (गट व भूमिका):** Season 1 Protagonist; D-to-S Rank Proving Games Contender; Rookie Adventurer; Unindexed Glitch-Drifter from 21st-Century India.
- **Planetary Shard & Location (स्थान):** Central City Outer Slums -> The Proving Games Coliseum
- **Power Bracket & Scale Band (साधना-स्तर):** D-Rank (Rookie Feeder) -> C/B-Rank (Awakening Ascendant) | T1 -> T2
- **Quirk & Magic (सक्रिय कौशल्ये):** Spark-Pulse, Heartbeat Sync & Structural Weak-Point Sight (Generates electrostatic micro-sparks, synchronizes cardiovascular pulses with bonded beast, and reads fracture points in matter).
- **Bonded Beast & Mount (सहजीवी बंध):** Dusk-Scrapper Hound (Stage 1 Feral -> Stage 2 Ironclad Hound; a battered, one-eared fighter rescued from arena scrap).
- **Weaponry & Arsenal (शस्त्रागार):** Battered short iron gladius, reinforced leather arm-guard & pocket-full of flint bearings.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 19 (Unindexed Engineering Student).
- **Moral Stance (नैतिक स्थिती):** Chaotic Good / Pragmatic Rationalist. Street-smart, loyal, skeptical of religious superstition, allergic to pompous grandstanding.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Slipped through a monsoon rain puddle in modern Mumbai during a spatial glitch. Holds zero gamer blue screens and zero divine cheats (`[STATUS: UNINDEXED / BLANK SLATE]`). Driven by practical survival economics, he enters the D-Tier blood-pits of Central City, climbing the ranks through unorthodox street-smart tactics, psychological gambles, and high-stakes heartbeat synchronization.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* D-Rank -> C/B-Rank | T1 -> T2 (Rising Glitch Contender)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Bio-Sync: Spark-Pulse Discharge, Heartbeat Meridian Reflex Double, Structural Weak-Point Sight]
  - *अधिकृत शस्त्रागार (Arsenal):* Short iron gladius & reinforced buckler

---

### [CHR-ALN-07] Kael (काएल / The Rift-Walker) — Escaped Type-1 Summoned Otherworlder
- **Role & Faction (गट व भूमिका):** Rogue Summoned Striker & Adventurer; Hastinapur Vanguard Guild & House Noctis.
- **Planetary Shard & Location (स्थान):** Human Planetary Shard (मानव ग्रह-खंड) | Hastinapur Adventurer Guild
- **Power Bracket & Scale Band (साधना-स्तर):** C-Rank -> B-Rank | T2 (Escaped Otherworld Striker)
- **Quirk & Magic (सक्रिय कौशल्ये):** Spatial Swap-Clap (*Boogie-Woogie*) & Shadow-Step (Swaps physical positions with any object or entity imbued with Prana via a handclap; steps through shadows via **Mode-A Symbiotic Contract with Noble Devil Nila [CHR-ABY-06]**).
- **Bonded Beast & Mount (सहजीवी बंध):** Symbiotically paired with Noble Devil Nila inside his shadow.
- **Weaponry & Arsenal (शस्त्रागार):** Twin black-iron shortswords & concealed throwing spikes.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Summoned in Era 4 | Age 20 (Escaped Summoned Otherworlder).
- **Moral Stance (नैतिक स्थिती):** Chaotic Good. Fiercely independent survivor who refused to be collared.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Summoned by corrupt Lord Kamsa in Yamuna-Ghat to be an enslaved pit assassin. During the crossing, awakened Spatial Swap-Clap, swapped himself with the high priest, broke the altar, and escaped. Now partners with Neel and Dhruv in the Proving Games.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* C-Rank -> B-Rank | T2 (Otherworld Striker)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Spatial Shift: Handclap Position Swap, Shadow-Step Infiltration]
  - *अधिकृत शस्त्रागार (Arsenal):* Twin black-iron shortswords & throwing spikes

---

### [CHR-ALN-08] Jin (जिन / The Gale-Fist) — Reincarnated Martial Brawler
- **Role & Faction (गट व भूमिका):** Unarmed Martial Arts Specialist; Central City & Hastinapur Iron-Akharas; Tempest Clan.
- **Planetary Shard & Location (स्थान):** Central City & Hastinapur Akharas
- **Power Bracket & Scale Band (साधना-स्तर):** C-Rank -> B-Rank | T2 (Martial Artist)
- **Quirk & Magic (सक्रिय कौशल्ये):** Vacuum Palm & Marma 108-Point Striking (Compresses atmospheric air into concussive palm strikes and targets nerve hubs).
- **Bonded Beast & Mount (सहजीवी बंध):** Silverback Canopy-Ape (Stage 2 Bonded — Canopy Line).
- **Weaponry & Arsenal (शस्त्रागार):** Weighted bronze knuckle-wraps & reinforced silk shin-guards.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Reincarnated in Era 4 | Age 21 (Former Earth Martial Artist).
- **Moral Stance (नैतिक स्थिती):** Chaotic Good / Battle Addict. Lives for the thrill of honorable hand-to-hand combat.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Reincarnated via the Yama-Vidhata Contract with martial muscle memories intact. Refuses weapons, striving to master the ancient 108 Marma points of Universe B. Friendly rival to Rudrakh, Karna, and Neel.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* C-Rank -> B-Rank | T2 (Martial Brawler)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Gale Striking: Vacuum Shockwave Palm, Marma Nerve Disruptor]
  - *अधिकृत शस्त्रागार (Arsenal):* Weighted bronze knuckle-wraps & silk wraps

---

### [CHR-ALN-09] Elena (एलेना / The Rune-Sniper) — Reincarnated Crossbow Sniper
- **Role & Faction (गट व भूमिका):** Long-Range Reconnaissance Sniper; Hastinapur Adventurer Guild; Rostova Family.
- **Planetary Shard & Location (स्थान):** Human Planetary Shard (मानव ग्रह-खंड) | Hastinapur Adventurer Guild
- **Power Bracket & Scale Band (साधना-स्तर):** C-Rank | T2 (Guild Sniper)
- **Quirk & Magic (सक्रिय कौशल्ये):** Hawk-Eye Zoom & Wind-Curve Arrow (Magnifies vision up to 2 miles and curves crossbow bolts around cover).
- **Bonded Beast & Mount (सहजीवी बंध):** Cinder Falcon (Stage 1 Raptor).
- **Weaponry & Arsenal (शस्त्रागार):** Adler-crafted repeating crossbow with runic magazine.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Reincarnated in Era 4 | Age 19 (Former Earth Biathlon Shooter).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Cool-headed marksman who never wastes an arrow.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Apprenticed under Wolfgang Adler before joining the Hastinapur Adventurer Guild. Specializes in taking down high-speed flying wyverns and cursed beasts from extreme ranges.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* C-Rank | T2 (Guild Sniper)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Optics & Trajectory: 2-Mile Hawk Vision, Wind-Curve Bolt Guidance]
  - *अधिकृत शस्त्रागार (Arsenal):* Adler repeating crossbow & enchanted bolt quiver

---

### [CHR-ALN-10] Soren (सोरेन / The Mist-Corsair) — Reincarnated Sea-Hunter
- **Role & Faction (गट व भूमिका):** Maritime Monster Hunter; The Sea Citadel Fleet & Lindqvist Clan.
- **Planetary Shard & Location (स्थान):** Human Planetary Shard (मानव ग्रह-खंड) | The Sea Citadel Harbor
- **Power Bracket & Scale Band (साधना-स्तर):** B-Rank Sea Vanguard | T2 (Marine Leviathan Hunter)
- **Quirk & Magic (सक्रिय कौशल्ये):** Lightning-Harpoon & Sonar-Ping (Electrifies forged whaling harpoons and maps submarine depths via acoustic echo).
- **Bonded Beast & Mount (सहजीवी बंध):** Glacial Shark (Stage 2 Bonded — Ocean-Maw Line).
- **Weaponry & Arsenal (शस्त्रागार):** Heavy lightning-tethered whaling harpoon & boarding cutlass.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Reincarnated in Era 4 | Age 28 (Former Earth Naval Officer).
- **Moral Stance (नैतिक स्थिती):** Chaotic Good. Daring maritime captain who patrols coastal shipping routes against rogue Makaras.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Works closely with Commodore Linnea and deep-sea diver Finn, protecting merchant drakes from deep-trench monsters.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* B-Rank Sea Vanguard | T2 (Marine Leviathan Hunter)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Marine Bolt: Conductive Harpoon Arc, Subsea Sonar Mapping]
  - *अधिकृत शस्त्रागार (Arsenal):* Lightning-tethered harpoon & boarding cutlass
"""

def assemble_roster():
    with open(roster_path, "r", encoding="utf-8") as f:
        text = f.read()

    part_matches = list(re.finditer(r'#+\s+PART\s+[0-9]+:', text))
    starts = [m.start() for m in part_matches]
    
    header = text[:starts[0]]
    header = header.replace("100 Verified Canonical Entities", "120 Verified Canonical Entities")
    header = header.replace("१०० प्रमाणित केनन व्यक्ती", "१२० प्रमाणित केनन व्यक्ती")
    header = header.replace("१०० प्रमाणित व्यक्तींचा", "१२० प्रमाणित व्यक्तींचा")
    header = header.replace("१०० व्यक्तिरेखांचे", "१२० व्यक्तिरेखांचे")
    header = header.replace("नेमके **१०० व्यक्ती**", "नेमके **१२० व्यक्ती**")
    header = header.replace("`CHR-HUM-01` ते `CHR-HUM-15` (१५ नश्वर व्यक्ती)", "`CHR-HUM-01` ते `CHR-HUM-22` (२२ नश्वर व्यक्ती)")
    header = header.replace("`CHR-ASU-01` ते `CHR-ASU-15` (१५ असुर व्यक्ती)", "`CHR-ASU-01` ते `CHR-ASU-16` (१६ असुर व्यक्ती)")
    header = header.replace("`CHR-BST-01` ते `CHR-BST-08` (८ श्वापद-सार्वभौम)", "`CHR-BST-01` ते `CHR-BST-10` (१० श्वापद-सार्वभौम)")
    header = header.replace("`CHR-ABY-01` ते `CHR-ABY-08` (८ अधोलोक व्यक्ती)", "`CHR-ABY-01` ते `CHR-ABY-13` (१३ अधोलोक व्यक्ती)")
    header = header.replace("`CHR-DIV-01` ते `CHR-DIV-13` (१३ वैश्विक व घटनात्मक व्यक्ती)", "`CHR-DIV-00` ते `CHR-DIV-13` (१४ वैश्विक व घटनात्मक व्यक्ती)")
    header = header.replace("`CHR-ALN-01` ते `CHR-ALN-06` (६ उल्लेखनीय पुनर्जन्मित आत्मे व डायस्पोरा)", "`CHR-ALN-01` ते `CHR-ALN-10` (१० उल्लेखनीय पुनर्जन्मित आत्मे व डायस्पोरा)")

    part1 = text[starts[0]:starts[1]].rstrip() + "\n" + new_hum_entries.strip() + "\n\n"
    part2 = text[starts[1]:starts[2]].rstrip() + "\n" + new_asu_entries.strip() + "\n\n"
    part3 = text[starts[2]:starts[3]]
    part4 = text[starts[3]:starts[4]].rstrip() + "\n" + new_bst_entries.strip() + "\n\n"
    part5 = text[starts[4]:starts[5]]
    part6 = text[starts[5]:starts[6]]
    part7 = new_aby_section.strip() + "\n\n"

    part8_raw = text[starts[7]:starts[8]]
    m_div1 = re.search(r'###\s*\[CHR-DIV-01\]', part8_raw)
    if m_div1:
        div_start = m_div1.start()
        part8 = part8_raw[:div_start] + new_div_00_entry.strip() + "\n\n" + part8_raw[div_start:]
    else:
        part8 = part8_raw

    part9 = new_aln_section.strip() + "\n"

    full_text = header + part1 + part2 + part3 + part4 + part5 + part6 + part7 + part8 + part9

    ids = re.findall(r'###\s*\[(CHR-[A-Z]+-\d+)\]', full_text)
    print(f"Total canonical IDs assembled: {len(ids)} (Unique: {len(set(ids))})")
    assert len(ids) == 120, f"Expected 120 IDs, found {len(ids)}!"
    assert len(set(ids)) == 120, f"Expected 120 unique IDs, found {len(set(ids))}!"

    assert "operational Ansha of Shiva" in full_text, "Missing CHR-DIV-13 invariant!"
    assert "Absolute Combat Ban (Inviolable Invariant)" in full_text, "Missing combat ban invariant!"
    assert "[CHR-ALN-06] Neel" in full_text, "Missing Neel entry!"

    with open(roster_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"Successfully updated {roster_path}")

    with open(mirror_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"Successfully mirrored to {mirror_path}")

if __name__ == "__main__":
    assemble_roster()


