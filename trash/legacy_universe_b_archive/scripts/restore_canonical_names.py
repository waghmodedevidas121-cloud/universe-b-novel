import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Read 08_Character_Roster.md
fpath = r"d:\Web Novel\UNIVERSE B\New\08_Character_Roster.md"
with open(fpath, "r", encoding="utf-8") as f:
    c = f.read()

# Restore CHR-ASU-03 Hilda
c = c.replace("### [CHR-ASU-03] Marshal Lauhini (मार्शल लौहिनी)", "### [CHR-ASU-03] Marshal Hilda (मार्शल हिल्डा)")
c = c.replace("Disciple of Marshal Lauhini", "Disciple of Marshal Hilda")

# Restore CHR-ASU-13 Olga
c = c.replace("### [CHR-ASU-13] Amba (अंबा)", "### [CHR-ASU-13] Olga (ओल्गा)")
c = c.replace("Matron Amba's orphanage", "Matron Olga's orphanage")

# Restore CHR-BST-02 Jormun
c = c.replace("### [CHR-BST-02] Kadru (कद्रू)", "### [CHR-BST-02] Jormun (जोर्मुन)")
c = c.replace("Naga Empress Kadru's radical nephew", "Naga Empress Jormun's radical nephew")

# Restore CHR-BST-07 Morvath
c = c.replace("### [CHR-BST-07] Shabari (शबरी)", "### [CHR-BST-07] Morvath (मोर्व्हाथ)")
c = c.replace("Shabari's apprentice", "Morvath's apprentice")

# Restore CHR-HUM-08 Silas
c = c.replace("### [CHR-HUM-08] Lord Admiral Suhotra (महा-नाविक सुहोत्र)", "### [CHR-HUM-08] Lord Admiral Silas (महा-नाविक सायलास / Silas Suhotra)")
c = c.replace("Lord Admiral Suhotra and Renzo Vance", "Admiral Silas and Renzo Vance")
c = c.replace("trades forbidden chasm ores with Marich and Lord Admiral Suhotra", "trades forbidden chasm ores with Marich and Admiral Silas")

# Restore CHR-HUM-09 Linnea & CHR-HUM-11 Finn
c = c.replace("### [CHR-HUM-09] Commodore Lavanya (कमोडोर लावण्या)", "### [CHR-HUM-09] Commodore Linnea (कमोडोर लिनिया)")
c = c.replace("### [CHR-HUM-11] Malhar (मल्हार)", "### [CHR-HUM-11] Finn (फिन)")
c = c.replace("Commodore Lavanya and deep-sea diver Malhar", "Commodore Linnea and deep-sea diver Finn")

# Restore CHR-CEN-01 Sulabha & CHR-CEN-02 Ambika, with Manu-Upadhi presiding
c = c.replace(
"""### [CHR-CEN-01] The Manu-Upādhi (मनू-उपाधी) — The Iron Sovereign of Central City
- **Role & Faction (गट व भूमिका):** Presiding Sovereign of Tier 3 Astral Realm on the Grey Basalt Throne; Supreme Lawgiver and Protector of the 5 Continental Shards.
- **Planetary Shard & Location (स्थान):** Central Astral Realm (मध्य-क्षेत्र) | Central City (The Grey Basalt Throne Room)
- **Power Bracket & Scale Band (साधना-स्तर):** S-Rank Sovereign Administrator (T5 / S-Rank Fortress-Breaker Scale)
- **Quirk & Magic (सक्रिय कौशल्ये):** [Sovereign Authority: Basalt Ward Synchronization, Grand Concord Decree, Mass Civic Calm]
- **Bonded Beast & Mount (सहजीवी बंध):** Four-horned Basalt Mastodon (Stage 3 Sovereign Mount).
- **Weaponry & Arsenal (शस्त्रागार):** The Central Aegis-Rod & Grey Basalt Sovereign Gavel.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Replaced via the Seven-Shard Conclave (The Chalni-Election).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Supreme civic arbiter preventing inter-shard total war and checking Shard-King expansionism.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Sits upon the uncarved Grey Basalt Throne at the geometric dead center of Central City. Governs in direct coordination with the 7 Sovereign Seats (Coin, Rations, Forge, Caravans, Shadow, Civic Order, Coliseum). Subordinate to the Tier 2 High Council (Indra-Upādhi) in cosmic defense, but holds absolute sovereign authority over mortal civic law across the five shards.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* S-Rank (Fortress-Breaker Ceiling) | T5 (Astral Sovereign)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Sovereign Law: Grey Basalt Tectonic Anchor Tuning, Five-Shard Civic Pact Binding, Mass Discord Dampening]
  - *अधिकृत शस्त्रागार (Arsenal):* The Central Aegis-Rod & Basalt Sovereign Decree Seal

---

### [CHR-CEN-02] High Arbitrator Beatrice Rosso (दॉना बीट्रिस रोसो) — Seat #1 of the 7 Sovereign Seats
- **Role & Faction (गट व भूमिका):** High Arbitrator of the Central Reserve Bank & Regulator of the Beast-Core Exchange (Akash-Kosha Vaults); Seat #1 (Coin & Credit) under the Manu-Upādhi.
- **Planetary Shard & Location (स्थान):** Central Astral Realm (मध्य-क्षेत्र) | Central City (Akash-Kosha Banking Vaults & Core-Exchange)
- **Power Bracket & Scale Band (साधना-स्तर):** B-Rank Elite / Master Appraiser | T3 (Sovereign Financial Arbitrator)
- **Quirk & Magic (सक्रिय कौशल्ये):** [Economic Metaphysics: Absolute Gold-Sense, Prana-Core Density Sight, Counterfeit-Core Detection, Inviolable Blood-Seal Contract].
- **Bonded Beast & Mount (सहजीवी बंध):** Gilded Mastiff (Stage 2 Vault Guardian).
- **Weaponry & Arsenal (शस्त्रागार):** Central Reserve Master Vault Key-Rod & Aether-Rupee Matrix Seal.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Reincarnated from a Venetian banking lineage in Era 4 | Age 54 (Master Sovereign Banker).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Incorruptible sovereign banker who honors contracts above all factional politics.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Controls the Pan-Astral Aether-Rupee matrix, the 17% customs clearing tariffs between shards, and holds the tie-breaking audit power in the Chalni-Election. Subordinate only to the Manu-Upādhi in civic financial jurisdiction.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* B-Rank Elite | T3 (Central Financial Sovereign)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Appraisal & Finance: Prana Core Density Sight, Counterfeit Detection Ward, Inviolable Blood-Seal Contract]
  - *अधिकृत शस्त्रागार (Arsenal):* Central Reserve Master Vault Key-Rod & Aether-Rupee Matrix Seal""",
"""### [CHR-CEN-00] The Manu-Upādhi (मनू-उपाधी) — The Iron Sovereign of Central City
- **Role & Faction (गट व भूमिका):** Presiding Sovereign of Tier 3 Astral Realm on the Grey Basalt Throne; Supreme Lawgiver and Protector of the 5 Continental Shards.
- **Planetary Shard & Location (स्थान):** Central Astral Realm (मध्य-क्षेत्र) | Central City (The Grey Basalt Throne Room)
- **Power Bracket & Scale Band (साधना-स्तर):** S-Rank Sovereign Administrator (T5 / S-Rank Fortress-Breaker Scale)
- **Quirk & Magic (सक्रिय कौशल्ये):** [Sovereign Authority: Basalt Ward Synchronization, Grand Concord Decree, Mass Civic Calm]
- **Bonded Beast & Mount (सहजीवी बंध):** Four-horned Basalt Mastodon (Stage 3 Sovereign Mount).
- **Weaponry & Arsenal (शस्त्रागार):** The Central Aegis-Rod & Grey Basalt Sovereign Gavel.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Replaced via the Seven-Shard Conclave (The Chalni-Election).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Supreme civic arbiter preventing inter-shard total war and checking Shard-King expansionism.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Sits upon the uncarved Grey Basalt Throne at the geometric dead center of Central City. Governs in direct coordination with the 7 Sovereign Seats (Coin, Rations, Forge, Caravans, Shadow, Civic Order, Coliseum). Subordinate to the Tier 2 High Council (Indra-Upādhi) in cosmic defense, but holds absolute sovereign authority over mortal civic law across the five shards.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* S-Rank (Fortress-Breaker Ceiling) | T5 (Astral Sovereign)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Sovereign Law: Grey Basalt Tectonic Anchor Tuning, Five-Shard Civic Pact Binding, Mass Discord Dampening]
  - *अधिकृत शस्त्रागार (Arsenal):* The Central Aegis-Rod & Basalt Sovereign Decree Seal

---

### [CHR-CEN-01] High Chancellor Sulabha (सुलभा) — Supreme Moderator of the Concord
- **Role & Faction (गट व भूमिका):** Speaker of the Grand Concord Assembly & Patron of the Proving Games; reporting to the Manu-Upādhi.
- **Planetary Shard & Location (स्थान):** Central Astral Realm (मध्य-क्षेत्र) | Central City (The Grand Concord Dome)
- **Power Bracket & Scale Band (साधना-स्तर):** A-Rank (Top 10% Diplomatic Master) | T4 (Grand Assembly Moderator)
- **Quirk & Magic (सक्रिय कौशल्ये):** Will-Binding (Vashitva) & Sanctuary Ward (Her voice commands calm across a hall of ten thousand roaring warriors).
- **Bonded Beast & Mount (सहजीवी बंध):** White Steppe Palfrey (Ceremonial steed).
- **Weaponry & Arsenal (शस्त्रागार):** The Concord Mace (Golden ceremonial gavel).
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 68 (Master Diplomat).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Supreme referee maintaining inter-realm peace.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Keeps the five shards from going to open war through razor-sharp diplomacy, managing the Five-Arch Rotunda where the four great Stone Gateways meet under the Manu-Upādhi's charter.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* A-Rank (Top 10% Diplomatic Master) | T4 (Grand Assembly Moderator)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Siddhi Authority: Vashitva Voice of Accord, Mass Sanctuary Peace-Dome]
  - *अधिकृत शस्त्रागार (Arsenal):* The Concord Mace (Golden ceremonial gavel) & Assembly Gavel-Stone

---

### [CHR-CEN-02] High Governor Ambika (अंबिका) — Mistress of the Vaults of Truth
- **Role & Faction (गट व भूमिका):** Governor of the Central Reserve Bank & Regulator of the Beast-Core Exchange (Akash-Kosha Banking Vaults); Seat #1 (Coin & Credit) under the Manu-Upādhi.
- **Planetary Shard & Location (स्थान):** Central Astral Realm (मध्य-क्षेत्र) | Central City (Akash-Kosha Banking Vaults)
- **Power Bracket & Scale Band (साधना-स्तर):** B-Rank (Top 10% Elite) | T3 (Central Financial Governor)
- **Quirk & Magic (सक्रिय कौशल्ये):** Gold-Sense & Blood-Seal Contract (Can detect a single counterfeit coin or fake Beast Core in a chest of ten thousand).
- **Bonded Beast & Mount (सहजीवी बंध):** Gilded Mastiff (Stage 2 Vault Guardian).
- **Weaponry & Arsenal (शस्त्रागार):** Vault Master Ledger & Golden Key-Rod.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 52 (Financial Governor).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Strict regulator of the Aether-Rupee and gateway tariffs.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Controls the Aether-Rupee and the 17% gateway tariff; coordinates with High Arbitrator Beatrice Rosso at the Core-Exchange and funds Investigator Devayani’s taskforce to hunt down illegal Shadow Anchors.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* B-Rank (Top 10% Elite) | T3 (Central Financial Governor)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Economic Metaphysics: Absolute Gold-Sense, Counterfeit-Core Detection, Inviolable Blood-Seal Contract]
  - *अधिकृत शस्त्रागार (Arsenal):* Central Reserve Master Vault Key-Rod & Aether-Rupee Matrix Seal"""
)

# Restore CHR-ALN-02 Beatrice Rosso
c = c.replace(
"""### [CHR-ALN-02] Matteo Benvenuti (मात्तेओ बेन्वेनुती) — Grand Appraiser & Deputy of the Beast-Core Bourse
- **Role & Faction (गट व भूमिका):** Chief Technical Appraiser & Deputy Vaultmaster; Central City Core-Exchange under High Arbitrator Beatrice Rosso.
- **Planetary Shard & Location (स्थान):** Central Planetary Shard (मध्यवर्ती क्षेत्र) | Central City Core-Exchange
- **Power Bracket & Scale Band (साधना-स्तर):** C-Rank (80–90% Reincarnate Bracket) | T2 (Technical Appraiser)
- **Quirk & Magic (सक्रिय कौशल्ये):** Appraiser's Eye & Density Calibration (Gauges the exact elemental purity and Prana density of raw Beast-Cores).
- **Bonded Beast & Mount (सहजीवी बंध):** Silt-Breaker Boar (Stage 1 Domestic Utility).
- **Weaponry & Arsenal (शस्त्रागार):** Heavy brass calipers & runic appraisal lens.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Reincarnated in Era 4 | Age 44 (Former Earth Gemologist).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Methodical craftsman dedicated to objective mineralogical and core calibration.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Reincarnated Florentine gemologist serving as the trusted technical deputy to High Arbitrator Beatrice Rosso, ensuring all Beast-Cores entering the Central Reserve Bank meet exact purity indices.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* C-Rank | T2 (Technical Appraiser)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Appraisal: Prana Core Density Sight, Counterfeit Flaw Detection]
  - *अधिकृत शस्त्रागार (Arsenal):* Brass calibration scales & runic focal glass""",
"""### [CHR-ALN-02] Donna Beatrice Rosso (दॉना बीट्रिस रोसो) — High Arbitrator of the Core-Exchange
- **Role & Faction (गट व भूमिका):** Chief Financial Arbitrator; Central Reserve Bank & Core-Exchange Vaults.
- **Planetary Shard & Location (स्थान):** Central Planetary Shard (मध्यवर्ती क्षेत्र) | Central City Core-Exchange
- **Power Bracket & Scale Band (साधना-स्तर):** C/B-Rank (80–90% Reincarnate Bracket) | T2/T3 (Financial Sovereign)
- **Quirk & Magic (सक्रिय कौशल्ये):** Appraiser's Eye & Karmic Ledger Lock (Instantly gauges the true energy density and purity of any Beast-Core).
- **Bonded Beast & Mount (सहजीवी बंध):** Silt-Breaker Boar (Stage 1 Domestic Utility).
- **Weaponry & Arsenal (शस्त्रागार):** Pearl-handled runic balance scale & Aether-wand.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Reincarnated from a Venetian banking lineage in Era 4 | Age 54 (Former Earth Banker).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Incorruptible banker who honors contracts above all politics.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Reincarnated from a Venetian banking lineage. Structured the 17% customs clearance system between the outer shards and Central City, stabilizing the Aether-Rupee economy.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* C/B-Rank | T2/T3 (Financial Arbitrator)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Appraisal: Prana Core Density Sight, Counterfeit Detection Ward, Inviolable Blood-Seal Contract]
  - *अधिकृत शस्त्रागार (Arsenal):* Golden balance scales & runic appraisal wand"""
)

with open(fpath, "w", encoding="utf-8") as f:
    f.write(c)

# Also patch 11_Astral_Society.md to restore Ambika and Sulabha
fpath_soc = r"d:\Web Novel\UNIVERSE B\New\11_Astral_Society.md"
with open(fpath_soc, "r", encoding="utf-8") as f:
    cs = f.read()

cs = cs.replace(
    "High Arbitrator Beatrice Rosso (दॉना बीट्रिस रोसो) यांच्या हाताखालील **The Central Reserve Bank",
    "High Governor Ambika यांच्या हाताखालील **The Central Reserve Bank"
)
cs = cs.replace(
    "[ CENTRAL CITY ] ──► The Manu-Upādhi & 7 Sovereign Seats (High Arbitrator Beatrice Rosso)",
    "[ CENTRAL CITY ] ──► The Manu-Upādhi & Sovereign Council (High Chancellor Sulabha & Governor Ambika)"
)
with open(fpath_soc, "w", encoding="utf-8") as f:
    f.write(cs)

# Also patch 09_Faction_Politics.md
fpath_pol = r"d:\Web Novel\UNIVERSE B\New\09_Faction_Politics.md"
with open(fpath_pol, "r", encoding="utf-8") as f:
    cp = f.read()

cp = cp.replace(
    "1. *Seat of Coin & Credit:* High Arbitrator Beatrice Rosso (Central Reserve Bank & Beast-Core Exchange).",
    "1. *Seat of Coin & Credit:* High Governor Ambika (Central Reserve Bank) & Beatrice Rosso (Core-Exchange)."
)
with open(fpath_pol, "w", encoding="utf-8") as f:
    f.write(cp)

print("ALL CANONICAL NAMES 100% RESTORED!")
