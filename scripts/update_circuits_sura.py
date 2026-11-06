file_path = r"d:\Web Novel\Brahmand\02_POWER_SYSTEM\10_The_Proving_Games_Circuits_and_Feeder_Pits.md"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

old_sec2_3 = """## 2. Inviolable Competition Axiom: Absolute Deva Combat Ban

One of the most rigid constitutional laws of the Proving Games is the **Absolute Deva Combat Ban (देवांची रिंगणात लढण्यास १००% बंदी)**:

1. **The Balance-of-Power Invariant:** Suras from Amarāvatī possess immortal physiological cellular density and prāṇic light saturation. If a Sura were permitted to enter a mortal arena, it would instantly distort the competitive integrity of weight classes and nullify the purpose of mortal self-reliance (*Atma-Nirbharta*).
2. **The Sacred Combat Invariant (युद्ध हे 'यज्ञ', तमाशा नाही):** In the Vedic ethos, combat is a sacred rite (*Yuddha-Yajña*) fought for Dharma and cosmic defense. Devas do not view physical combat as impure—their own gods like Indra, Kartikeya, and the Maruts are supreme warriors. However, they consider a commercial gladiatorial ring—where mortals bleed for ticket sales, copper betting coins, and civilian amusement—to be a desecration of martial honor (*Kṣātra-Dharma*). They refuse to turn holy combat into a circus spectacle (*Dyūta-Nāṭya*).
3. **Catastrophic Radiative Mismatch:** Tier 3 Suras are *Tejo-Maya* (high-frequency divine radiance). An unshielded Deva unleashing celestial prāṇa inside a closed stadium would incinerate mortal competitors and melt the surrounding stone tiers, obliterating fair competition.
4. **Spectators & Envoys Only:** Suras are constitutionally restricted to high-altitude white marble balconies (*Deva-Vātāyana*), observing through magnifying crystal lenses as official observers, High Council envoys, or ceremonial prize-conferrers for S-Rank inductees entering the Antariksha-Setu army.

---

## 3. The Four Regional Sister-Circuits (चार अधिकृत प्रांतिक मंडळे)

No unvetted contender can simply walk into Central City's 100,000-seat Coliseum. A fighter must first earn an official **Combat License (रिंगण परवाना)** by qualifying through one of the four regional circuits:"""

new_sec2_3 = """## 2. Sura Combatants & The High-Orbit Protocol (सुर योद्धे व उच्च-कक्षा आखाडा नियम)

Contrary to the misconception that Suras are detached spectators, **Suras actively compete in the Proving Games (सुर योद्धे आखाड्यात अधिकृतपणे उतरतात)** under established constitutional protocols:

1. **Active Elemental Birthright & Cellular Longevity:** Because Suras are born with **100% active elemental affinities** from the 10 primal elements and enjoy a natural lifespan of ~1,000 years, Sura contenders naturally populate high-tier brackets (B, A, and S-Rank) on the Vanguard Hero Board.
2. **The Sura Arena Presence:** Suras participate in both Central City's Main Coliseum and their own regional circuit. While they avoid low-tier street brawling for mere copper scraps, high-ranked Sura duels in the upper brackets draw massive crowds and titanic betting pools in Silver and Gold Coins.
3. **Zero Adventurer Guilds on Sura Shard:** Unlike the other four shards, the Sura Shard contains **zero Adventurer Guilds** because no wild monster-dens or infested ruins exist in Amarāvatī. However, the Sura Shard maintains a prominent branch of the **Global Vanguard Hero Board**, directly tracking all ranked champions.
4. **The Buffer Zone Pipeline (Tier 2 Antariksha-Setu):** Apex S-Rank Sura victors, alongside top human, asura, and beast legends, are inducted directly into the **Setu Standing Army (The Solar Guard / Hiraṇya-Vāhinī)** to man the cosmic buffer against Tier 4 horrors.

---

## 3. The Five Regional Sister-Circuits (पाच अधिकृत प्रांतिक मंडळे)

No unvetted contender can simply walk into Central City's 100,000-seat Coliseum. A fighter must first earn an official **Combat License (रिंगण परवाना)** by qualifying through one of the five regional circuits:"""

if old_sec2_3 in text:
    text = text.replace(old_sec2_3, new_sec2_3)
    print("Replaced Section 2 and 3 header successfully")
else:
    print("Section 2 and 3 target not found")

# Add Section 3.5 after 3.4
old_sec34 = """### 3.4 The Primeval Canopy Trials (श्वापद खंड — किष्किंधा अरण्य-आखाडा)
* **Terrain:** Open rope-and-ironwood suspension platforms strung 1,000 feet in the air between giant primeval redwoods.
* **Combat Focus:** High-altitude aerial agility, archery from swinging vines, predator-riding, and terminal-velocity evasion.
* **Championship Token:** **The Emerald Leaf Crest (हरित-पर्ण मुकुट)**.

---"""

new_sec34_35 = """### 3.4 The Primeval Canopy Trials (श्वापद खंड — किष्किंधा अरण्य-आखाडा)
* **Terrain:** Open rope-and-ironwood suspension platforms strung 1,000 feet in the air between giant primeval redwoods.
* **Combat Focus:** High-altitude aerial agility, archery from swinging vines, predator-riding, and terminal-velocity evasion.
* **Championship Token:** **The Emerald Leaf Crest (हरित-पर्ण मुकुट)**.

### 3.5 The Sun-Cliff Celestial Circuit (सुर खंड — सूर्य-शिखर आखाडा)
* **Terrain:** High-altitude floating white marble platforms suspended above cloud banks, connected by magnetic solar-crystal bridges. High wind-shear.
* **Combat Focus:** Aerial kinetic duelcraft, supersonic Astra archery, solar bladeplay, and light-weaving manipulation.
* **Championship Token:** **The Solar Crest Token (सूर्य-शिखर मुद्रा)**.
* **Guild & Board Status:** Features zero Adventurer Guilds, but maintains the official **Sun-Cliff Branch of the Global Vanguard Hero Board**.

---"""

if old_sec34 in text:
    text = text.replace(old_sec34, new_sec34_35)
    print("Added Section 3.5 successfully")
else:
    print("Section 3.4 target not found")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 10_The_Proving_Games_Circuits_and_Feeder_Pits.md successfully")
