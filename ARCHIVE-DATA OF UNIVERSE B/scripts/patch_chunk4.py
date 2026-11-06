import re
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Web Novel\UNIVERSE B\New"

def patch_file(filename, replacements):
    filepath = os.path.join(BASE_DIR, filename)
    print(f"Patching {filename}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original_length = len(content)
    for target, replacement in replacements:
        if target not in content:
            print(f"  [WARNING] Target string not found in {filename}:\n    '{target[:60]}...'")
        else:
            content = content.replace(target, replacement)
            print(f"  [SUCCESS] Replaced: '{target[:40]}...'")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Finished {filename} (len: {original_length} -> {len(content)})\n")

# ==============================================================================
# 1. PATCH 08_Character_Roster.md
# ==============================================================================
roster_replacements = [
    # Header & Counts
    (
        "# 08. Master Character Dossier: 120 Verified Canonical Entities (मुख्य पात्र-संग्रह: १२० प्रमाणित केनन व्यक्ती)",
        "# 08. Master Character Dossier: 121 Verified Canonical Entities (मुख्य पात्र-संग्रह: १२१ प्रमाणित केनन व्यक्ती)"
    ),
    (
        "एकत्रित नोंदी, कृत्रिम लक्ष्ये व डुप्लिकेट प्रोफाईल काढून टाकते. Protagonist slot unassigned.",
        "एकत्रित नोंदी, कृत्रिम लक्ष्ये व डुप्लिकेट प्रोफाईल काढून टाकते. Protagonist: [CHR-ALN-06] Neel (नील / The Sieve's Edge Protagonist)."
    ),
    (
        "- **`CHR-CEN-01` ते `CHR-CEN-08` (८ मध्यवर्ती व्यक्ती):** Central City ग्रँड कॉन्कॉर्ड घुमट, मध्यवर्ती रिझर्व्ह बँक, केंद्रीय साहसी गिल्ड व प्रोव्हिंग गेम्स.",
        "- **`CHR-CEN-01` ते `CHR-CEN-08` (८ मध्यवर्ती व्यक्ती):** Central City मनू-उपाधी (The Iron Sovereign on the Grey Basalt Throne), ७ सार्वभौम आसने, मध्यवर्ती रिझर्व्ह बँक, केंद्रीय साहसी गिल्ड व प्रोव्हिंग गेम्स."
    ),
    (
        "- **`CHR-DIV-00` ते `CHR-DIV-13` (१४ वैश्विक व घटनात्मक व्यक्ती):** सर्वोच्च त्रिमूर्ती (ब्रह्मा, क्षीरोदकशायी विष्णू, शिव) (३), अनंत कोर (१), सहा घटनात्मक उपाधी (६), तीन दैवी प्रतिनिधी (३).",
        "- **`CHR-DIV-00` ते `CHR-DIV-14` (१५ वैश्विक व घटनात्मक व्यक्ती):** सर्वोच्च त्रिमूर्ती (३), अनंत कोर (१), इंद्र-उपाधी (१), सहा घटनात्मक उपाधी (६), तीन दैवी प्रतिनिधी (३)."
    ),
    (
        "**एकूण प्रमाणित केनन व्यक्ती:** नेमके **१२० व्यक्ती**. *(Protagonist slot unassigned; story not started.)*",
        "**एकूण प्रमाणित केनन व्यक्ती:** नेमके **१२१ व्यक्ती**. (Protagonist: **[CHR-ALN-06] Neel (नील)** — Season 1 The Sieve's Edge Protagonist)."
    ),

    # Ghost Names
    ("Disciple of Marshal Hilda", "Disciple of Marshal Lauhini"),
    ("Matron Olga's orphanage", "Matron Amba's orphanage"),
    ("Shaman Morvath's apprentice", "Shabari's apprentice"),
    ("Empress Jormun's radical nephew", "Naga Empress Kadru's radical nephew"),
    ("Inquisitor Satyak on the Setu", "Senior Field Auditor Satyaketu on the Setu"),
    ("Direct rival to Setu General Vajra", "Direct rival to Marshal-General Vajraketu"),
    ("House Noctis", "House Yamuna-Shade (छाया-गृह)"),
    ("with Marich and Admiral Silas while", "with Marich and Lord Admiral Suhotra while"),
    ("trades forbidden chasm ores with Marich and Admiral Silas", "trades forbidden chasm ores with Marich and Lord Admiral Suhotra"),
    ("Works closely with Commodore Linnea and deep-sea diver Finn", "Works closely with Commodore Lavanya and deep-sea diver Malhar"),

    # CHR-CEN-01 Sulabha -> The Manu-Upadhi
    (
"""### [CHR-CEN-01] High Chancellor Sulabha (सुलभा) — Supreme Moderator of the Concord
- **Role & Faction (गट व भूमिका):** Speaker of the Grand Concord Assembly & Patron of the Proving Games.
- **Planetary Shard & Location (स्थान):** Central Astral Realm (मध्य-क्षेत्र) | Central City (The Grand Concord Dome)
- **Power Bracket & Scale Band (साधना-स्तर):** A-Rank (Top 10% Diplomatic Master) | T4 (Grand Assembly Moderator)
- **Quirk & Magic (सक्रिय कौशल्ये):** Will-Binding (Vashitva) & Sanctuary Ward (Her voice commands calm across a hall of ten thousand roaring warriors).
- **Bonded Beast & Mount (सहजीवी बंध):** White Steppe Palfrey (Ceremonial steed).
- **Weaponry & Arsenal (शस्त्रागार):** The Concord Mace (Golden ceremonial gavel).
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 68 (Master Diplomat).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Supreme referee maintaining inter-realm peace.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Keeps the five shards from going to open war through razor-sharp diplomacy, managing the Five-Arch Rotunda where the four great Stone Gateways meet.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* A-Rank (Top 10% Diplomatic Master) | T4 (Grand Assembly Moderator)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Siddhi Authority: Vashitva Voice of Accord, Mass Sanctuary Peace-Dome]
  - *अधिकृत शस्त्रागार (Arsenal):* The Concord Mace (Golden ceremonial gavel) & Assembly Gavel-Stone""",
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
  - *अधिकृत शस्त्रागार (Arsenal):* The Central Aegis-Rod & Basalt Sovereign Decree Seal"""
    ),

    # CHR-CEN-02 Ambika -> Beatrice Rosso
    (
"""### [CHR-CEN-02] High Governor Ambika (अंबिका) — Mistress of the Vaults of Truth
- **Role & Faction (गट व भूमिका):** Governor of the Central Reserve Bank & Regulator of the Beast-Core Exchange.
- **Planetary Shard & Location (स्थान):** Central Astral Realm (मध्य-क्षेत्र) | Central City (Akash-Kosha Banking Vaults)
- **Power Bracket & Scale Band (साधना-स्तर):** B-Rank (Top 10% Elite) | T3 (Central Financial Governor)
- **Quirk & Magic (सक्रिय कौशल्ये):** Gold-Sense & Blood-Seal Contract (Can detect a single counterfeit coin or fake Beast Core in a chest of ten thousand).
- **Bonded Beast & Mount (सहजीवी बंध):** Gilded Mastiff (Stage 2 Vault Guardian).
- **Weaponry & Arsenal (शस्त्रागार):** Vault Master Ledger & Golden Key-Rod.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 52 (Financial Governor).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral. Strict regulator of the Aether-Rupee and gateway tariffs.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Controls the Aether-Rupee and the 17% gateway tariff; funds Investigator Devayani’s taskforce to hunt down illegal Shadow Anchors.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* B-Rank (Top 10% Elite) | T3 (Central Financial Governor)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Economic Metaphysics: Absolute Gold-Sense, Counterfeit-Core Detection, Inviolable Blood-Seal Contract]
  - *अधिकृत शस्त्रागार (Arsenal):* Central Reserve Master Vault Key-Rod & Aether-Rupee Matrix Seal""",
"""### [CHR-CEN-02] High Arbitrator Beatrice Rosso (दॉना बीट्रिस रोसो) — Seat #1 of the 7 Sovereign Seats
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
  - *अधिकृत शस्त्रागार (Arsenal):* Central Reserve Master Vault Key-Rod & Aether-Rupee Matrix Seal"""
    ),

    # Part 8 Header & Addition of Indra-Upadhi
    (
"""# PART 8: TIER 1 HIGH COUNCIL & PRIMORDIAL FIGURES (परम-धाम व The High Council Rotunda (सभा-लोक))
*वैश्विक आधारशिळा, प्रणाली-गाभा व घटनात्मक पदे*""",
"""# PART 8: TIER 1 PARAMA-DHAMA & TIER 2 HIGH COUNCIL CONSTITUTIONAL ENTITIES
*वैश्विक आधारशिळा, सर्वोच्च त्रिमूर्ती, प्रणाली-गाभा, इंद्र-उपाधी व घटनात्मक पदे*"""
    ),
    (
"""### [CHR-DIV-13] Rudra (रूद्र-प्रतिनिधि) — शिव आदेशाचा दैवी प्रतिनिधी (Operational Ansha of Shiva)
- **Role & Faction (गट व भूमिका):** Tier 4 सीमांत व नियंत्रण मृत-क्षेत्र; शिवदेवाचा थेट दूत (Divine Envoy: Operational Ansha of Shiva).
- **Planetary Shard & Location (स्थान):** Tier 1 High Council Realm & Tier 4 Containment Dead-Zone
- **Power Bracket & Scale Band (साधना-स्तर):** T7 (Cosmic Delegate - Operational Force / Rudra Ansha)
- **Vanguard & Soul-Bond (व्हॅनगार्ड व सहजीवी बंध):** Divine Envoy: Operational Ansha of Shiva | सहजीवी बंध: शून्य
- **Lineage & Culture (संस्कृती व वंश):** एकादश रूद्र प्रकटीकरण (Rudra Operational Manifestation).
- **Historical Era & Lifespan (ऐतिहासिक युग व आयुर्मर्यादा):** **Era 1: Satya Yuga (सत्य युग — Primordial Genesis)** | शाश्वत घटनात्मक उपाधी / नित्य अस्तित्व (Eternal Constitutional Upadhi).
- **Moral Stance (नैतिक स्थिती):** Universe B मध्ये प्रकट झालेला Shiva चा एकमेव operational Ansha of Shiva. भ्रष्ट क्षेत्राच्या काठाने नियंत्रण लागू करतो व ७ अंधकारमय व्यक्ती-सीलांची तपासणी करतो.
- **कार्यरत अपरिवर्तनीय:** शुद्धीकरण व लष्करी बळाची अंमलबजावणी कठोरपणे Tier 4 सीमांतावरच. उच्च परिषद कक्षात शून्य लढाऊ अधिकार (जिथे १००% Absolute Combat Ban (Inviolable Invariant) अभेद्य आहे). मनमानी वरदान देऊ शकत नाही किंवा परिषद मतदान बायपास करू शकत नाही.
- **Physical Dossier & Anatomy (शारीरिक संग्रह):** व्याघ्रचर्मधारी, हातात त्रिशूल, नीललोहित तेज, डोळ्यांत संहाराची निखारे.
- **Psychological Profile & Hook (मानसिक प्रोफाईल):** सीमारेषेचे रक्षण आणि सातही सीलांची अखंडता टिकवणे; सातवा थरार विचलित झाल्यास त्वरित नियंत्रण करणे.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* T7 (Cosmic Delegate - Operational Force / Rudra Ansha)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Warfare: Operational Ansha Combat, Zero-Tolerance Dissolution] [Executive Sovereign]
  - *अधिकृत शस्त्रागार (Arsenal):* [Relic: Ansha-Triśūla] & [Relic: Mahakala Dissolution Staff]""",
"""### [CHR-DIV-13] Rudra (रूद्र-प्रतिनिधि) — शिव आदेशाचा दैवी प्रतिनिधी (Operational Ansha of Shiva)
- **Role & Faction (गट व भूमिका):** Tier 4 सीमांत व नियंत्रण मृत-क्षेत्र; शिवदेवाचा थेट दूत (Divine Envoy: Operational Ansha of Shiva).
- **Planetary Shard & Location (स्थान):** Tier 1 High Council Realm & Tier 4 Containment Dead-Zone
- **Power Bracket & Scale Band (साधना-स्तर):** T7 (Cosmic Delegate - Operational Force / Rudra Ansha)
- **Vanguard & Soul-Bond (व्हॅनगार्ड व सहजीवी बंध):** Divine Envoy: Operational Ansha of Shiva | सहजीवी बंध: शून्य
- **Lineage & Culture (संस्कृती व वंश):** एकादश रूद्र प्रकटीकरण (Rudra Operational Manifestation).
- **Historical Era & Lifespan (ऐतिहासिक युग व आयुर्मर्यादा):** **Era 1: Satya Yuga (सत्य युग — Primordial Genesis)** | शाश्वत घटनात्मक उपाधी / नित्य अस्तित्व (Eternal Constitutional Upadhi).
- **Moral Stance (नैतिक स्थिती):** Universe B मध्ये प्रकट झालेला Shiva चा एकमेव operational Ansha of Shiva. भ्रष्ट क्षेत्राच्या काठाने नियंत्रण लागू करतो व ७ अंधकारमय व्यक्ती-सीलांची तपासणी करतो.
- **कार्यरत अपरिवर्तनीय:** शुद्धीकरण व लष्करी बळाची अंमलबजावणी कठोरपणे Tier 4 सीमांतावरच. उच्च परिषद कक्षात शून्य लढाऊ अधिकार (जिथे १००% Absolute Combat Ban (Inviolable Invariant) अभेद्य आहे). मनमानी वरदान देऊ शकत नाही किंवा परिषद मतदान बायपास करू शकत नाही.
- **Physical Dossier & Anatomy (शारीरिक संग्रह):** व्याघ्रचर्मधारी, हातात त्रिशूल, नीललोहित तेज, डोळ्यांत संहाराची निखारे.
- **Psychological Profile & Hook (मानसिक प्रोफाईल):** सीमारेषेचे रक्षण आणि सातही सीलांची अखंडता टिकवणे; सातवा थरार विचलित झाल्यास त्वरित नियंत्रण करणे.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* T7 (Cosmic Delegate - Operational Force / Rudra Ansha)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Warfare: Operational Ansha Combat, Zero-Tolerance Dissolution] [Executive Sovereign]
  - *अधिकृत शस्त्रागार (Arsenal):* [Relic: Ansha-Triśūla] & [Relic: Mahakala Dissolution Staff]

---

### [CHR-DIV-14] The Indra-Upādhi (इंद्र-उपाधी) — Presiding Sovereign of the High Council & Bearer of the Vajra
- **Role & Faction (गट व भूमिका):** Presiding Sovereign of Tier 2 Swarga (The Buffer Zone / Setu-Loka); Presiding Head of the High Council Rotunda (सभा-लोक); Supreme Military Warden of the 360° Spherical Grand Aegis.
- **Planetary Shard & Location (स्थान):** Tier 2 Swarga / The Buffer Zone | Golden Vajra Throne (सुवर्ण वज्र-सिंहासन)
- **Power Bracket & Scale Band (साधना-स्तर):** T7 / T8 (Apex Cosmic Sovereign / High Council Presiding Head)
- **Vanguard & Soul-Bond (व्हॅनगार्ड व सहजीवी बंध):** Universal Function: Commander-in-Chief of Pan-Astral Defense & Grand Aegis Perimeter | सहजीवी बंध: ऐरावत (Airavata — Primordial Four-Tusked White Mastodon)
- **Lineage & Culture (संस्कृती व वंश):** इंद्र घटनात्मक पद (Constitutional Indra Upadhi — Achieved through 100 Ashvamedha Tapas or Peerless Merit, verified by System Ananta).
- **Historical Era & Lifespan (ऐतिहासिक युग व आयुर्मर्यादा):** **Era 1 to Era 4** | घटनात्मक कार्यकाळ (Constitutional Tenure — subject to replacement upon loss of virtue or tapas).
- **Moral Stance (नैतिक स्थिती):** Lawful Neutral (Vigilant Protector). Commands the Setu Legions and oversees the 7 voting blocks of the High Council. Treats mortal ascendants and Deva lords with identical constitutional equality (Warrior Equality).
- **Constitutional Dual-Relationship with Soul Trinity:**
  1. *Metaphysical / Karmic Jurisdiction:* Holds ZERO judicial or veto authority over Yama, Chitragupta, and Vidhātā regarding soul-processing ledgers or Route A destinies (they answer only to Tier 1 Parama-Dhama).
  2. *Spatial / Physical Security:* Holds supreme command over the territorial perimeter and military security of Tier 2 Swarga, providing unassailable sanctuary to the Soul Administration archives against Patala incursions.
- **Physical Dossier & Anatomy (शारीरिक संग्रह):** सूर्यप्रभ सुवर्ण चिलखत, शिरावर वज्र-मुकुट, हातात अमोघ वज्र-अस्त्र, नजरेत तिन्ही लोकांचे लष्करी व धोरणात्मक भान.
- **Psychological Profile & Hook (मानसिक प्रोफाईल):** विश्वाचे बाह्य शत्रूंपासून रक्षण करणे आणि संसदेतील राजकीय गतिरोध मोडून समतोल राखणे.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* T7 / T8 (Apex Cosmic Sovereign)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Cosmic Warfare: Vajra Lightning Discharge, 360° Grand Aegis Command Synchronization, High Council Casting Vote Authority]
  - *अधिकृत शस्त्रागार (Arsenal):* [Primordial Astra: The True Vajra (अमोघ वज्र)], [Relic: Golden Vajra Seal of the High Council]"""
    ),

    # CHR-ALN-02 Beatrice Duplicate -> Matteo Benvenuti
    (
"""### [CHR-ALN-02] Donna Beatrice Rosso (दॉना बीट्रिस रोसो) — High Arbitrator of the Core-Exchange
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
  - *अधिकृत शस्त्रागार (Arsenal):* Golden balance scales & runic Aether-wand""",
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
  - *अधिकृत शस्त्रागार (Arsenal):* Brass calibration scales & runic focal glass"""
    ),

    # CHR-ALN-06 Neel Complete Canonical Dossier
    (
"""### [CHR-ALN-06] Neel (नील / The Pulse-Reader) — Primary Glitch-Drifter & Unindexed Hero
- **Role & Faction (गट व भूमिका):** Season 1 Protagonist; D-to-S Rank Proving Games Contender; Rookie Adventurer; Unindexed Glitch-Drifter from 21st-Century India.
- **Planetary Shard & Location (स्थान):** Central City Outer Slums -> The Proving Games Coliseum
- **Power Bracket & Scale Band (साधना-स्तर):** D-Rank (Rookie Feeder) -> C/B-Rank (Awakening Ascendant) | T1 -> T2
- **Quirk & Magic (सक्रिय कौशल्ये):** [Pulse-Sync & Friction Spark] (Sensory-Instinct & Close-Quarters Striker: Pulse-Sight / Rhythm-Read within 15 paces, Friction Spark / Pulse-Snap onto Marma nerve points, and Dual-Heart Synchronization with companion beast).
- **Bonded Beast & Mount (सहजीवी बंध):** Dusk-Scrapper Hound ("Sheru" / Official Guild Name: "Kuro" — Stage 1 Feral -> Stage 2 Ironclad Hound -> Stage 3 Abyssal Dread-Hound; one-eared Void/Iron scrap survivor).
- **Weaponry & Arsenal (शस्त्रागार):** Battered short iron gladius, reinforced leather arm-guard & pocket-full of flint bearings.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 19 (Unindexed Engineering Student).
- **Moral Stance (नैतिक स्थिती):** Chaotic Good / Pragmatic Rationalist. Street-smart survivor mask, loyal to his circle, skeptical of religious superstition, allergic to pompous grandstanding.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** 100% Original 21st-century human Earth body (not a corpse hijack) wearing wet Bombay college clothes (denim jacket, cotton tee, dark trousers, worn sneakers), college backpack, house keys, and dead smartphone (cracked screen, 0% battery). Orphaned at 16 when parents Aarav & Revati died in a highway collision; zero extended family; lived as a self-reliant ghost in a rented Bombay 1-BHK paying rent through delivery shifts. Crossed the cosmic void via an irregular monsoon spatial glitch, undergoing an emergency Kshira Sagara Metabolic Reboot (72,000 Nadis unsealed). Awoke in the straw-bed of an unhitched Beast-Cart outside Central City outer gates with zero coins, dry throat, and burning Spark-Pulse palms. Holds zero gamer blue screens (`[STATUS: UNINDEXED / BLANK SLATE]`). Mid-IQ in rote magic theory, but 200-IQ in street survival, micro-expression reading, and high-stakes psychological gambles.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* D-Rank -> C/B-Rank | T1 -> T2 (Rising Glitch Contender)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Pulse-Sync & Friction Spark: Pulse-Sight Rhythm-Read (15 paces), Friction Spark / Pulse-Snap, Dual-Heart Synchronization]
  - *अधिकृत शस्त्रागार (Arsenal):* Short iron gladius, reinforced leather buckler & cracked smartphone relic""",
"""### [CHR-ALN-06] Neel (नील) — Unindexed Glitch-Drifter & Season 1 Protagonist
- **Role & Faction (गट व भूमिका):** Season 1 Protagonist; D-to-S Rank Proving Games Contender; Rookie Adventurer; Unindexed Glitch-Drifter from 21st-Century South Mumbai.
- **Planetary Shard & Location (स्थान):** Central City Outer Slums -> The Proving Games Coliseum -> Tier 3 Astral Realm
- **Power Bracket & Scale Band (साधना-स्तर):** D-Rank (Rookie Feeder) -> C/B-Rank (Awakening Ascendant) | T1 -> T2 (Capped at S-Rank Fortress-Breaker Scale)
- **Quirk & Magic (Dual-Vector System):**
  1. *Right Arm (Piṅgalā Conduit):* Atharvan Krutya **GENI** (synthetic Manas from Gemma-4 neural chip) with **Zero-Sing Kinetic Friction Spark** (250–400 Joules contact thermal arc with zero 0.2s acoustic tell; requires instant Apāna thermal flush down into ground).
  2. *Left Arm (Idā Conduit):* **Cursed-Spirit Glove KALI (कलि)** (weathered dark combat glove + spiked black-iron shackle holding ancient Patala Devil Spirit Kali; symbiotic beast-bond with 0% corruption guarantee; dual-spectrum physical & elemental telekinesis strictly bound to owner's Dhāraṇā/Hold and Newton's Third Law).
- **Bonded Beast & Mount (सहजीवी बंध):** Dusk-Scrapper Hound ("Sheru" / Official Guild Name: "Kuro" — Stage 1 Feral -> Stage 2 Ironclad Hound -> Stage 3 Abyssal Dread-Hound; one-eared Void/Iron scrap survivor).
- **Weaponry & Arsenal (शस्त्रागार):**
  - *Right Wrist:* Atharvan Krutya GENI node (shackle-free weathered fingerless combat glove).
  - *Left Fore-Wrist:* Cursed Glove KALI (spiked black-iron shackle manacle permanently clamped around wrist).
  - *Relics from Earth:* Custom titanium flagship prototype (dead battery), Centurion Black Card (useless in fantasy), crumpled ₹10 note + ₹1 coin (₹11 cutting chai change), 0 Panas upon arrival.
- **Historical Era & Lifespan (ऐतिहासिक युग):** Era 4: Kali Yuga | Age 21 (Billionaire Tech Prodigy from Earth).
- **Moral Stance (नैतिक स्थिती):** Pragmatic Realist / Fierce Loyalist (Grey Alignment). Tony Stark swagger masking deep hyper-protective trauma; street-smart, allergic to religious superstition, honors contracts, fiercely defends his circle.
- **Character, Psychology & Hook (वैशिष्ट्ये व पार्श्वभूमी):** Sole heir to the Gadora Industrial & Tech Conglomerate (South Mumbai). Born to late tech titans Aarav Gadora & Suman Gadora. Grew up in a Worli Sea Face penthouse with a state-of-the-art coastal robotics/AI lab. Following his parents' death, fended off predatory takeover attempts from his opportunistic Uncle Kani Gadora and Aunt Cheri. Crossed the cosmic void during a freak monsoon electrical storm, undergoing an emergency Kshira Sagara Metabolic Reboot (72,000 Nadis cleared). Awoke in an unhitched beast-cart outside Central City with zero Panas, burning palms, and no gamer screens (`[STATUS: UNINDEXED / BLANK SLATE]`). 200-IQ in leverage, mechanical strain, micro-expression reading, and high-stakes psychological gambles.
- **Powers, Scale Band & Arsenal (शक्ती, साधना व शस्त्रास्त्रे):**
  - *साधना-स्तर (Scale Band):* D-Rank -> C/B-Rank | T1 -> T2 (Rising Glitch Contender)
  - *सक्रिय कौशल्ये व विद्या (Active Arts):* [Dual-Vector Combat: Zero-Sing Kinetic Friction Spark (Piṅgalā/Right), Cursed Telekinesis & Vector Grasp (Idā/Left via Kali), Apāna Heel-Grounding Flush, Pulse-Sight Rhythm-Read (15 paces), Dual-Heart Synchronization with Sheru]
  - *अधिकृत शस्त्रागार (Arsenal):* Left Spiked Cursed Glove KALI, Right Krutya GENI glove, dead titanium prototype phone & ₹11 transit coin relic"""
    )
]

patch_file("08_Character_Roster.md", roster_replacements)

# ==============================================================================
# 2. PATCH 14_High_Council.md
# ==============================================================================
council_replacements = [
    (
        "Status: [CANON LOCK] Official Canonical Specification of Tier 1 Governance, Parliamentary Law & Ideological Warfare (October 2026)",
        "Status: [CANON LOCK] Official Canonical Specification of Tier 2 Governance, Parliamentary Law & Ideological Warfare (October 2026)"
    ),
    (
        "Tier 1 मधील **High Council Realm (The High Council Rotunda (सभा-लोक))** ही केवळ ढगांवर बसलेली ऋषींची बैठक नाही; ती संपूर्ण बाल्य विश्वाचे (Child Cosmos) ऊर्जा-संतुलन, कर्म-कायदे, आणि सीमा-स्थैर्य नियंत्रित करणारी **सर्वोच्च वैश्विक महा-संसद** आहे.",
        "Tier 2 Swarga / Setu-Loka मधील **High Council Realm (The High Council Rotunda (सभा-लोक))** ही केवळ ढगांवर बसलेली ऋषींची बैठक नाही; ती संपूर्ण बाल्य विश्वाचे (Child Cosmos) ऊर्जा-संतुलन, कर्म-कायदे, आणि सीमा-स्थैर्य नियंत्रित करणारी **सर्वोच्च वैश्विक महा-संसद** आहे."
    ),
    (
        "Authority: Universe B च्या सर्वोच्च संसदीय व्यवस्थेची (High Council Realm / The High Council Rotunda (सभा-लोक)),",
        "Authority: Universe B च्या Tier 2 सर्वोच्च संसदीय व्यवस्थेची (The High Council Rotunda [सभा-लोक] under Indra-Upādhi),"
    ),
    (
"""═════════════════════════════════════════════════════════════════════════════════════════════
                       THE HIGH COUNCIL ROTUNDA (SABHA-LOKA PARLIAMENTARY ROTUNDA)
═════════════════════════════════════════════════════════════════════════════════════════════

                                [ THE UNREACHED APEX ]
                         The Three Pillars of Transcendent Light
                       Brahma (White) • Vishnu (Blue) • Shiva (Violet)
                       (Zero Physical Avatar • Absolute Silence • Supreme Will)
                                         │
     ┌───────────────────────────────────┼───────────────────────────────────┐
     ▼                                   ▼                                   ▼
[ PRAJAPATI GALLERY ]            [ NARADA GALLERY ]                  [ RUDRA GALLERY ]
Structure & Integrity            Intelligence & Equilibrium          Dissolution & Containment
Marichi · Atri · Angiras         Sanatkumara · Vashistha             Nandi · Bhringi
Bhrigu · Daksha                  Shuka (The Living Witness)          (Zero Combat in Chamber)
     │                                   │                                   │
     └───────────────────────────────────┼───────────────────────────────────┘
                                         ▼
     ═══════════════════════════════════════════════════════════════════════════════════
                      [ THE SIX CONSTITUTIONAL UPADHI STALLS ]
     [ THE PERMANENT SYSTEM PILLARS ]          [ THE ROTATING COSMIC UPADHIS ]
     1. Yama-Dharma   (Soul Adjudication)      4. The Chief Sage  (Anomaly Oversight)
     2. Vidhata       (Prana-Sutra Destiny)    5. Mahā-Pālaka     (Pan-Astral Defense)
     3. Chitragupta   (The Grand Hall of Ledgers (Maha-Lekha) Ledgers)     6. Prime Seeker    (Dimensional Physics)
     ═══════════════════════════════════════════════════════════════════════════════════""",
"""═════════════════════════════════════════════════════════════════════════════════════════════
                       THE HIGH COUNCIL ROTUNDA (SABHA-LOKA PARLIAMENTARY ROTUNDA)
═════════════════════════════════════════════════════════════════════════════════════════════

                                [ THE UNREACHED APEX ]
                         Tier 1: Parama-Dhama (Supreme Trinity)
                       Brahma (White) • Vishnu (Blue) • Shiva (Violet)
                       (Zero Physical Avatar • Absolute Silence • Supreme Will)
                                         │
     ┌───────────────────────────────────┼───────────────────────────────────┐
     ▼                                   ▼                                   ▼
[ PRAJAPATI GALLERY ]            [ NARADA GALLERY ]                  [ RUDRA GALLERY ]
Structure & Integrity            Intelligence & Equilibrium          Dissolution & Containment
Marichi · Atri · Angiras         Sanatkumara · Vashistha             Nandi · Bhringi
Bhrigu · Daksha                  Shuka (The Living Witness)          (Zero Combat in Chamber)
     │                                   │                                   │
     └───────────────────────────────────┼───────────────────────────────────┘
                                         │
                                         ▼
     ═══════════════════════════════════════════════════════════════════════════════════
                [ TIER 2: THE GOLDEN VAJRA THRONE OF INDRA-UPĀDHI ]
           Presiding Sovereign of the High Council • Bearer of the Vajra
            Casting Vote in Deadlocks • Supreme Commander of Pan-Astral Defense
     ═══════════════════════════════════════════════════════════════════════════════════
                                         │
                                         ▼
     ═══════════════════════════════════════════════════════════════════════════════════
                      [ THE SIX CONSTITUTIONAL UPADHI STALLS ]
     [ THE PERMANENT SYSTEM PILLARS ]          [ THE ROTATING COSMIC UPADHIS ]
     1. Yama-Dharma   (Soul Adjudication)      4. The Chief Sage  (Anomaly Oversight)
     2. Vidhata       (Prana-Sutra Destiny)    5. Mahā-Pālaka     (Pan-Astral Defense)
     3. Chitragupta   (Maha-Lekha Ledgers)     6. Prime Seeker    (Dimensional Physics)
     ═══════════════════════════════════════════════════════════════════════════════════"""
    ),
    (
        "मानवांच्या विमान-मार्गांवरून",
        "मानवांच्या रथ-मार्गांवरून"
    ),
    (
"""### 1.4 The Soul Triad's Parliamentary Posture: "Boredom to Lightning"
- **The Mundane Boredom (लौकिक राजकारणाचा कंटाळा):**  
  जेव्हा कौन्सिलमध्ये असुरांच्या गंधक-धूरावरून, देवांच्या स्फटिक-निर्यात करांवरून किंवा मानवांच्या विमान-मार्गांवरून तास न् तास चर्चा चालते, तेव्हा यम हनुवटीवर हात ठेवून शांत बसलेले असतात, विधाता आपले प्राणाचे धागे गुंफत बसतात, आणि चित्रगुप्त दफ्तर तपासण्यात मग्न असतात. त्यांना या नश्वर राजकारणात **शून्य रस** असतो.
- **The Instant Shift (जिथे 'आत्मा' आला, तिथे वज्र-शांतता!):**  
  परंतु ज्या क्षणी चर्चेत विषय येतो: *"Tier 4 च्या प्रभावामुळे १०,००० आत्म्यांचे चक्र थांबले आहे"*, किंवा *"Hastinapur मध्ये अर्ध-रिक्त (Ardha-Rikta) बहु-वैश्विक आत्मे आले आहेत"*, किंवा *"Devil Summoning मुळे आत्म्याची काजळी झाली आहे"*...  
  त्याच क्षणी **यमाचे डोळे तीक्ष्णपणे उघडतात**, विधात्याचा धागा थांबतो, आणि चित्रगुप्ताचा सुवर्ण-कलम उचलला जातो. संपूर्ण संसद एका क्षणात शांत होते; कारण प्रत्येकाला ठाऊक आहे की विश्वाचे खरे मालक हे तिघे आहेत, बाकी सर्व केवळ बाह्य पसारा आहे!""",
"""### 1.4 The Soul Triad's Parliamentary Posture: "Boredom to Lightning"
- **The Mundane Boredom (लौकिक राजकारणाचा कंटाळा):**  
  जेव्हा कौन्सिलमध्ये असुरांच्या गंधक-धूरावरून, देवांच्या स्फटिक-निर्यात करांवरून किंवा मानवांच्या रथ-मार्गांवरून तास न् तास चर्चा चालते, तेव्हा यम हनुवटीवर हात ठेवून शांत बसलेले असतात, विधाता आपले प्राणाचे धागे गुंफत बसतात, आणि चित्रगुप्त दफ्तर तपासण्यात मग्न असतात. त्यांना या नश्वर राजकारणात **शून्य रस** असतो.
- **The Instant Shift (जिथे 'आत्मा' आला, तिथे वज्र-शांतता!):**  
  परंतु ज्या क्षणी चर्चेत विषय येतो: *"Tier 4 च्या प्रभावामुळे १०,००० आत्म्यांचे चक्र थांबले आहे"*, किंवा *"Hastinapur मध्ये अर्ध-रिक्त (Ardha-Rikta) बहु-वैश्विक आत्मे आले आहेत"*, किंवा *"Devil Summoning मुळे आत्म्याची काजळी झाली आहे"*...  
  त्याच क्षणी **यमाचे डोळे तीक्ष्णपणे उघडतात**, विधात्याचा धागा थांबतो, आणि चित्रगुप्ताचा सुवर्ण-कलम उचलला जातो. संपूर्ण संसद एका क्षणात शांत होते; कारण प्रत्येकाला ठाऊक आहे की विश्वाचे खरे मालक हे तिघे आहेत, बाकी सर्व केवळ बाह्य पसारा आहे!

### 1.5 The Soul Trinity's Constitutional Dual-Relationship with Indra-Upādhi
- **Metaphysical / Karmic Jurisdiction (सर्वोच्च स्वातंत्र्य):**  
  यम, विधाता आणि चित्रगुप्त हे केवळ Tier 1 मधील सर्वोच्च त्रिमूर्ती आणि दैवी प्रतिनिधींना उत्तरदायी आहेत. **इंद्र-उपाधीला यमाच्या न्यायपीठावर, विधात्याच्या प्राण-सूत्रांवर किंवा चित्रगुप्ताच्या खतावणीवर कोणताही हुकूम किंवा व्हेटो (Veto) चालवण्याचा घटनात्मक अधिकार नाही.**
- **Spatial / Military Jurisdiction (भौतिक संरक्षण):**  
  परंतु आत्मा-प्रशासनाचे प्रत्यक्ष कार्यालय (Soul Administration Complex) Tier 2 Swarga / Setu-Loka मध्ये स्थित असल्याने, त्यांच्या बाह्य सीमांचे रक्षण, दूत-संरक्षण आणि अधोलोक आक्रमणांपासून सुरक्षा पुरवण्याची **सर्वोच्च लष्करी जबाबदारी इंद्र-उपाधीची आहे.**

### 1.6 The Unbroken Cosmic Bridge: High Council to Astral Realm
- **The Macro-to-Civic Hierarchy:**  
  $$\\text{Tier 2 Swarga: High Council (Indra-Upādhi)} \\gg \\text{Tier 3 Astral Realm: The Manu-Upādhi \\& 7 Sovereign Seats}$$
  इंद्र-उपाधी संपूर्ण विश्वाचे लष्करी स्थैर्य व अजगर-कवच सांभाळतात, तर सेंट्रल सिटीमधील **मनू-उपाधी (The Iron Sovereign on the Grey Basalt Throne)** पाचही ग्रह-खंडांमधील नश्वर नागरी कायदे, कर-प्रणाली आणि प्रोव्हिंग गेम्सचे प्रशासन सांभाळतात."""
    )
]

patch_file("14_High_Council.md", council_replacements)

# ==============================================================================
# 3. PATCH 09_Faction_Politics.md
# ==============================================================================
politics_replacements = [
    (
        "वाफेची आणि स्फटिकांची आधुनिक यंत्रे चालवणे",
        "ज्वाला-दाब आणि स्फटिकांची रनिक यंत्रे चालवणे"
    ),
    (
        "| **Garuda Scouts (गरुड)** | उंच पर्वत शिखरे, एअरशिप टॉवर्स | अति-उंच भरारी, दुरवरची टेहळणी | हवाई हल्ले, Blimp Escort Squadrons, टपाल विमानांना आणि पक्षांना हवेत सुरक्षा पुरवणे. |",
        "| **Garuda Scouts (गरुड)** | उंच पर्वत शिखरे, गरुड-बुरुज | अति-उंच भरारी, दुरवरची टेहळणी | हवाई हल्ले, गरुड-रक्षक पथके, आकाशीय संदेशवाहकांना आणि प्रवाशांना हवेत सुरक्षा पुरवणे. |"
    ),
    (
        "शुद्ध सौर-स्फटिक (Solar Quartz), जे विमानांच्या स्फटिक-गाभ्यांसाठी आणि",
        "शुद्ध सौर-स्फटिक (Solar Quartz), जे धावणाऱ्या रथांच्या स्फटिक-गाभ्यांसाठी आणि"
    ),
    (
        "विमान वाहतूक जाळे जागेवर ठप्प होईल",
        "रथ व तांडा वाहतूक जाळे जागेवर ठप्प होईल"
    ),
    (
"""### 5.2 The Central Hub (The Sovereign Referee)
- **स्थान:** सेंट्रल सिटी (पाचही खंडांच्या मध्यभागी तरंगणारा न्यूट्रल झोन).
- **नियंत्रक संस्था:** Central Reserve Bank, Grand Guild Directory, The Concord Enforcers.
- **राजकीय धोरण:** १००% अलिप्तता. कोणत्याही एका वंशाचे वर्चस्व खपवून घेतले जात नाही.
- **सामर्थ्य:** जागतिक चलनावर (Aether-Rupee) नियंत्रण आणि प्रोव्हिंग गेम्सचे (The Proving Games) व्यवस्थापन.""",
"""### 5.2 The Central Hub: The Manu-Upādhi & 7 Sovereign Seats (The Sovereign Referee)
- **स्थान:** सेंट्रल सिटी (पाचही खंडांच्या मध्यभागी तरंगणारा न्यूट्रल झोन).
- **सर्वोच्च शासक:** **The Manu-Upādhi (मनू-उपाधी)** — The Iron Sovereign on the Grey Basalt Throne.
- **घटनात्मक दुवा:** $\\text{Tier 2 High Council (Indra-Upādhi)} \\gg \\text{Tier 3 Central City (Manu-Upādhi)}$.
- **The Seven Sovereign Seats (सात सार्वभौम आसने):**
  1. *Seat of Coin & Credit:* High Arbitrator Beatrice Rosso (Central Reserve Bank & Beast-Core Exchange).
  2. *Seat of Rations & Grain:* Hastinapur Syndicate Liaison.
  3. *Seat of Forge & Metallurgy:* Vidarbha Smithing Guild Grandmaster.
  4. *Seat of Aether-Transport & Caravans:* Southern Chariot Guildmaster.
  5. *Seat of Shadow & Pretas:* Cursed-Zone Frontier Warden.
  6. *Seat of Civic Order:* Municipal Constable General.
  7. *Seat of the Proving Games:* Coliseum Grand Marshal Satyabhama.
- **राजकीय धोरण:** १००% अलिप्तता. कोणत्याही एका वंशाचे वर्चस्व खपवून घेतले जात नाही.
- **सामर्थ्य:** जागतिक चलनावर (Aether-Rupee) नियंत्रण, १७% सीमा-शुल्क (Tariff), आणि प्रोव्हिंग गेम्सचे (The Proving Games) व्यवस्थापन."""
    )
]

patch_file("09_Faction_Politics.md", politics_replacements)

# ==============================================================================
# 4. PATCH 11_Astral_Society.md
# ==============================================================================
society_replacements = [
    (
        "नगर-रक्षक, नियमित सैनिक, रनिक लोहार, विमान-चालक आणि सीमारेषा अधिकारी.",
        "नगर-रक्षक, नियमित सैनिक, रनिक लोहार, रथ-चालक आणि सीमारेषा अधिकारी."
    ),
    (
        "• १ कप गरम आलं-चहा व भाजलेले चणे (विमान-मंच स्टॉल)        ──► १ Copper Masha (CM)",
        "• १ कप गरम आलं-चहा व भाजलेले चणे (रथ-मंच स्टॉल)          ──► १ Copper Masha (CM)"
    ),
    (
        "• १ रात्र: विमान-मंच जवळील डॉर्मिटरी लाकडी कॉट                 ──► २ Copper Masha (CM)",
        "• १ रात्र: रथ-मंच जवळील डॉर्मिटरी लाकडी कॉट                   ──► २ Copper Masha (CM)"
    ),
    (
        "• व्यापारी काफिला जकात शुल्क (Caravan Gateway Toll प्रति माल-विमान) ──► ८ Silver Kārṣāpaṇa (SK)",
        "• व्यापारी काफिला जकात शुल्क (Caravan Gateway Toll प्रति माल-रथ)   ──► ८ Silver Kārṣāpaṇa (SK)"
    ),
    (
        "High Governor Ambika यांच्या हाताखालील **The Central Reserve Bank (The Vaults of Truth)**",
        "High Arbitrator Beatrice Rosso (दॉना बीट्रिस रोसो) यांच्या हाताखालील **The Central Reserve Bank (The Vaults of Truth)**"
    ),
    (
        "राजाचा गुप्त विमान-शस्त्रागार",
        "राजाचा गुप्त अस्त्र-शस्त्रागार"
    ),
    (
        "हस्तिनापूरच्या विमानांना आणि रनिक शस्त्रांना",
        "हस्तिनापूरच्या रथांना आणि रनिक शस्त्रांना"
    ),
    (
        "अस्त्र-शाळेत किंवा विमान कार्यशाळेत",
        "अस्त्र-शाळेत किंवा यंत्रिक कार्यशाळेत"
    ),
    (
        "[ CENTRAL CITY ] ──► Multinational Directory (High Chancellor Sulabha)",
        "[ CENTRAL CITY ] ──► The Manu-Upādhi & 7 Sovereign Seats (High Arbitrator Beatrice Rosso)"
    )
]

patch_file("11_Astral_Society.md", society_replacements)

# ==============================================================================
# 5. PATCH 13_Races_and_Clans.md
# ==============================================================================
races_replacements = [
    (
        "अभ्येद्य विमानांचे चिलखत घडवले",
        "अभ्येद्य रथांचे व तटांचे चिलखत घडवले"
    ),
    (
        "टेलिग्राफच्या विस्तारामुळे काही शहरे किन्नरांच्या पारंपरिक कुरिअर मार्गांचे बजेट कमी करत आहेत.",
        "मंत्र-शिला नाद-जाळ्याच्या विस्तारामुळे काही शहरे किन्नरांच्या पारंपरिक कुरिअर मार्गांचे बजेट कमी करत आहेत."
    ),
    (
        "मानवांची विमाने आणि देवांची स्फटिक यंत्रे",
        "मानवांचे वेगवान रथ आणि देवांची स्फटिक यंत्रे"
    )
]

patch_file("13_Races_and_Clans.md", races_replacements)

# ==============================================================================
# 6. PATCH 16_The_Proving_Games.md
# ==============================================================================
games_replacements = [
    (
        "आणि विमान-मंचांजवळील एथर-नेमबाजी",
        "आणि रथ-मंचांजवळील एथर-नेमबाजी"
    ),
    (
        "│    • Hastinapur Rail Barons  : रेशन, श्वापदांचे पोषाहार, आखाडा खानपान स्टॉल्स.   │",
        "│    • Hastinapur Caravan Barons : रेशन, श्वापदांचे पोषाहार, आखाडा खानपान स्टॉल्स. │"
    ),
    (
        "पारंपारिक शस्त्रे व एथर-काडतुसांची तपासणी.",
        "पारंपारिक शस्त्रे, धनुष्य-बाण व वज्र-शलाकांची तपासणी."
    ),
    # Add Adho-Rangashala in Section 1
    (
"""### 1.2 The Feeder-to-Coliseum Hierarchy (स्थानिक आखाड्यांपासून महा-रंगमंचापर्यंत):
- **स्थानिक आखाडे (Local Sand Pits - D/C-Rank):** प्रत्येक खंडातील प्रमुख शहरांमध्ये स्थानिक गिल्ड आखाडे असतात. येथे नवखे साहसी, स्थानिक मल्ल आणि भटकणारे एलियन्स आपली पात्रता सिद्ध करतात.
- **प्रादेशिक चषक (Regional Sister-Circuits - B-Rank):**
  - *हस्तिनामंडल चषक:* मानवी खंडातील रथ-युद्ध व रनिक तलवारबाजी.
  - *काल्डेरा क्लॅश (Caldera Clash):* असुर खंडातील लाव्हा-खंदक व हातोडा-कुस्ती.
  - *प्रायमीव्हल चॅलेंज (Primeval Canopy):* वानर-नाग श्वापद-शर्यती व विष-चाचण्या.
  - *सीमांत रिंगण (Frontier Rings):* सेतू-सीमा आणि नेदरहोम निर्वासितांच्या लढाया.
- **मध्यवर्ती महा-रंगमंच (The Grand Coliseum - Central City):**""",
"""### 1.2 The Feeder-to-Coliseum Hierarchy (स्थानिक आखाड्यांपासून महा-रंगमंचापर्यंत):
- **Adho-Rangashala (अधो-रंगशाळा — Atala Ceiling Black-Sand Feeder Pits):**
  - *स्थान:* Central City च्या थेट खाली, अतला (Atala Stratum — Patala Layer 1) च्या काळ्या बेसॉल्ट छतावर कोरलेले गुप्त, धोकादायक आखाडे.
  - *धोकादायक नियम:* काळी नेक्रोटिक शून्य-वाळू (Necrotic Void-Sand) जिथे जखमा आपोआप भरत नाहीत; उच्च गती-घर्षण (Kinetic Friction) किंवा अपान दाह-शमनाशिवाय रक्त थांबत नाही.
  - *कॅनन संदर्भ:* **नील (Neel) च्या प्रारंभीच्या लढाया (Chapters 2–5) याच अधो-रंगशाळेत सुरू होतात.** येथे कपटी सावकार, भ्रष्ट पंच आणि तस्करी केलेले प्रेता-गाभे (Preta-Cores) सर्रास वापरले जातात.
- **स्थानिक आखाडे (Local Sand Pits - D/C-Rank):** प्रत्येक खंडातील प्रमुख शहरांमध्ये स्थानिक गिल्ड आखाडे असतात. येथे नवखे साहसी, स्थानिक मल्ल आणि भटकणारे एलियन्स आपली पात्रता सिद्ध करतात.
- **प्रादेशिक चषक (Regional Sister-Circuits - B-Rank):**
  - *हस्तिनामंडल चषक:* मानवी खंडातील रथ-युद्ध व रनिक तलवारबाजी.
  - *काल्डेरा क्लॅश (Caldera Clash):* असुर खंडातील लाव्हा-खंदक व हातोडा-कुस्ती.
  - *प्रायमीव्हल चॅलेंज (Primeval Canopy):* वानर-नाग श्वापद-शर्यती व विष-चाचण्या.
  - *सीमांत रिंगण (Frontier Rings):* सेतू-सीमा आणि नेदरहोम निर्वासितांच्या लढाया.
- **मध्यवर्ती महा-रंगमंच (The Grand Coliseum - Central City):**"""
    ),
    # Add S-Rank Fortress-Breaker cap in Section 2
    (
"""### 2.2 S-Rank Exhibition Matches:
- दोन S-Rank योद्ध्यांची टक्कर झाल्यास संपूर्ण रंगमंचाभोवती Tier 2 सेटू-वॉर्डन्सचे स्फटिक-कवच सक्रिय केले जाते.""",
"""### 2.2 S-Rank Exhibition Matches & The Fortress-Destroyer Scale Cap:
- **दुर्ग-भंजक मर्यादा (The Fortress-Breaker Scale Cap):**  
  Tier 3 Astral Realm मध्ये S-Rank साधकांची शक्ती **दुर्ग-भंजक पातळीवर (Fortress-Destroyer Scale)** नैसर्गिकरित्या मर्यादित (Capped) केली आहे. सेंट्रल सिटीचा आधारभूत बेसॉल्ट आणि टेक्टॉनिक अँकर इतके मजबूत आहेत की अनिर्बंध खंड-विनाशक (Continent-Shattering) स्फोट घडवणे भौतिक नियमांनुसार अशक्य आहे.
- दोन S-Rank योद्ध्यांची टक्कर झाल्यास संपूर्ण रंगमंचाभोवती Tier 2 सेटू-वॉर्डन्सचे त्रि-स्तरीय स्फटिक-कवच सक्रिय केले जाते."""
    ),
    # Add Coliseum Rotary Acoustic Field in Section 5
    (
"""### 5.2 The Rotary Shadow Anchor Mechanism:
- रंगमंचाच्या मध्यभागी एक प्रचंड **चक्र-लंगर (Rotary Shadow Anchor)** आहे. हा लंगर थेट सेंट्रल सिटीच्या टेकड्यांशी आणि सेतूच्या आधारशिळांशी जोडलेला आहे.
- जेव्हा फेऱ्या बदलतात, तेव्हा संपूर्ण आखाडा जमिनीखालील प्रचंड हायड्रॉलिक मेकॅनिझमच्या साहाय्याने फिरवला जातो. एका क्षणात वाळूचे मैदान दलदलीत रूपांतरित होते, किंवा लाव्हा-कुंड्यातून लोखंडी खांब वर येतात!""",
"""### 5.2 The Rotary Shadow Anchor & Seal 6 Acoustic Dampening Field:
- **The Core Metaphysical Engine:**  
  रंगमंचाच्या मध्यभागी एक प्रचंड **चक्र-लंगर (Rotary Shadow Anchor)** आहे. हा लंगर थेट सेंट्रल सिटीच्या टेकड्यांशी आणि सेतूच्या आधारशिळांशी जोडलेला आहे.
- **Seal 6 Acoustic Dampening Field (१०,०००+ प्रेक्षक प्राण-कंपने):**  
  सेंट्रल कोलिझियम हे केवळ खेळाचे मैदान नसून विश्वाचे एक **अत्यावश्यक आध्यात्मिक यंत्र (Metaphysical Containment Engine)** आहे! कोलिझियममध्ये बसलेल्या १,००,००० प्रेक्षकांच्या उत्साही आरोळ्या, टाळ्या आणि गतीज प्राण (Kinetic Prana) चक्र-लंगरावरून थेट खाली झिरपतात.
- हा संयुक्त ध्वनी-कंपन **सील ६ (Prana-Shunyata / शून्य-खिंडार)** च्या विनाशी फ्रिक्वेन्सीला तंतोतंत निष्प्रभ (Counter-Resonance) करतो, ज्यामुळे सेंट्रल सिटीच्या पोटातील सूक्ष्म-भेगा (Micro-Rifts) पूर्णपणे दाबून ठेवल्या जातात!
- **रिंगण रूपांतरण:** जेव्हा फेऱ्या बदलतात, तेव्हा संपूर्ण आखाडा जमिनीखालील प्रचंड यंत्रणेच्या साहाय्याने फिरवला जातो. एका क्षणात वाळूचे मैदान दलदलीत रूपांतरित होते, किंवा लाव्हा-कुंड्यातून लोखंडी खांब वर येतात!"""
    )
]

patch_file("16_The_Proving_Games.md", games_replacements)

print("ALL CHUNK 4 PATCHES COMPLETED SUCCESSFULLY!")
