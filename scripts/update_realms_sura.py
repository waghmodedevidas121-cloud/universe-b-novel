file_path = r"d:\Web Novel\Brahmand\01_WORLD_BIBLE\02_The_Five_Realms_and_Central_City.md"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

target = """### 2.1 Society & Culture
- **The Solar Aristocracy:** The Devas of Tier 3 are living celestial mortals. Unlike the transcendent authorities of Tier 1, these Devas can age (over millennia), bleed, and die. They trace their lineage to Aditi and Kashyapa.
- **Gandharva-Purī:** The artistic and entertainment quarter of the Deva realm, where master acoustic performers tune Bīja-mantras and preserve ancient choral traditions.
- **Geopolitical Stance:** Coldly superior, diplomatically aloof, and deeply bureaucratic. They consider the lower shards to be crude and chaotic. However, they rely on the Asura Shard for runic steel alloys and on Central City for banking clearance.

---"""

replacement = """### 2.1 Society, Biology & Demographics
- **The Solar Aristocracy & Soul Origin:** The Suras (Devas) of Tier 3 are living celestial mortals. Because of the high spiritual karmic vibration of their Jīvātman, they incarnate into noble Sura lineages. They trace their ancestry to Aditi and Kashyapa.
- **Lifespan & Slow Reproduction:**
  * **Sura Baseline Lifespan:** ~1,000 years. Because of their extended life-cycle, their reproduction rate is remarkably slow; children are rare, deeply protected, and celebrated across the entire shard.
  * **Comparative Cosmic Lifespans (सामान्य नागरिक सरासरी आयु):**
    - *Humans (मानव):* 150 – 200 years (healthy mortal baseline in aether-rich atmosphere).
    - *Asuras (असुर):* 600 – 700 years (dense basalt-iron cellular longevity).
    - *Suras (सुर / देव):* ~1,000 years.
    - *Rishis / Sages (तपस्वी ऋषी):* Thousands of years to entire Yugas (sustained by intense Tapasyā and Prāṇāyāma).
- **100% Active Elemental Birthright (जन्मजात सक्रिय तत्त्व-क्षमता):**
  * Unlike humans—where the vast majority are born with dormant/slept traits requiring awakening ceremonies or crisis-triggers—**every Sura child is born with an already ACTIVATED elemental affinity** from the 10 primal elements!
  * Through childhood sādhanā and rigorous discipline, they refine this active birthright into extraordinary martial precision.
- **Gandharva-Purī:** The artistic quarter of the Deva realm, where master acoustic performers tune Bīja-mantras and preserve ancient choral traditions.
- **Multiracial Cosmopolitan Enclaves (अल्पसंख्याक वसाहती):**
  * The Sura Shard is **नही** an exclusive mono-racial bubble. While Suras form the majority ruling class, honored minorities of **Humans** (ambassadors, master textile artisans, high Vedic scholars), **Asuras** (metallurgical consultants, heavy runic architects), and **Beasts** (celestial avian envoys, royal transport steeds) reside in designated districts.
- **Proving Games Circuit & Vanguard Hero Board (शून्य गिल्ड / अधिकृत आखाडा):**
  * The Sura Shard hosts the **Sun-Cliff Celestial Circuit (सूर्य-शिखर आखाडा)**, where Sura adepts compete in high-altitude aerial and kinetic duels.
  * Sura contenders are officially ranked and tracked on the **Global Vanguard Hero Board**.
  * **Zero Adventurer Guilds:** Because there are no wild untamed monster dens or infested crypts on the Sura Shard, Adventurer Guilds do **नही** exist here; external field assignments are handled by direct royal mandates.
- **The Buffer Zone Pipeline (Tier 2 Antariksha-Setu):**
  * Elite high-ranked Sura masters and S-Rank champions are inducted directly into the **Buffer Zone Vanguard (The Solar Guard / Hiraṇya-Vāhinī)** to man the celestial defense towers against Tier 4 abyss horrors.
- **Geopolitical Stance:** Coldly superior, diplomatically aloof, and deeply bureaucratic. They consider the lower shards chaotic, yet depend on the Asura Shard for runic steel alloys and on Central City for commercial banking clearance.

---"""

if target in text:
    text = text.replace(target, replacement)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Updated 02_The_Five_Realms_and_Central_City.md successfully")
else:
    print("Target not found in 02_The_Five_Realms_and_Central_City.md")
