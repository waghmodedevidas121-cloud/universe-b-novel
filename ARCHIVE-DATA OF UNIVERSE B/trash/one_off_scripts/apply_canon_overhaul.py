import os
import re
import sys

_current_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_current_dir)
base_dir = os.path.join(_project_root, "New")

print(f"Project root: {_project_root}")
print(f"Base dir: {base_dir}")

# We will collect all .md files in New/
target_files = []
for root, dirs, files in os.walk(base_dir):
    if any(x in root for x in ["trash", "__pycache__", ".git"]):
        continue
    for file in files:
        if file.endswith(".md"):
            target_files.append(os.path.join(root, file))

print(f"Found {len(target_files)} markdown files in New/")

# Character replacements dictionary (ordered to avoid partial collisions)
# First we do specific multi-word / regex replacements, then individual terms
char_header_replacements = [
    # Human Shard
    (r"###\s*\[CHR-HUM-04\]\s*Commander Bhim II\s*\(सेनानी भीम द्वितीय\)\s*—\s*खंदक चिलखती सेनानी",
     '### [CHR-HUM-04] Captain Bhima, "The Trench Bull" (भीमा) — खंदक चिलखती सेनानी'),
    (r"###\s*\[CHR-HUM-06\]\s*Master Engineer Rohini-Bai\s*\(मुख्य वाष्प-शिल्पी रोहिणी-बाई\)\s*—\s*लोहमार्गाची शिल्पकार",
     '### [CHR-HUM-06] Rohini, Chief Railwright (लोहमार्ग मुख्य शिल्पकार रोहिणी) — लोहमार्गाची शिल्पकार'),
    (r"###\s*\[CHR-HUM-07\]\s*Superintendent Vance\s*\(रेल्वे अधीक्षक व्हॅन्स\)\s*—\s*घडयाळाचा कारागीर",
     '### [CHR-HUM-07] Yardmaster Alistair Vance, "Clockwork Vance" (यार्डमास्तर अॅलिस्टेर व्हॅन्स) — घड्याळाचा कारागीर'),
    (r"###\s*\[CHR-HUM-08\]\s*High Admiral Silas Suhotra\s*\(महा-नाविक सायलास सुहोत्र\)\s*—\s*चांदीचा सार्वभौम",
     '### [CHR-HUM-08] Lord Admiral Suhotra, "The Silver Shark" (महा-नाविक सुहोत्र) — चांदीचा सार्वभौम'),
    (r"###\s*\[CHR-HUM-09\]\s*Commodore Linnea Brandt\s*\(कमोडोर लिनिया ब्रँड\)\s*—\s*मुक्त खाजगी ताफ्याची सार्वभौम",
     '### [CHR-HUM-09] Commodore Lavanya, "The Sea Wolf" (कमोडोर लावण्या) — मुक्त खाजगी ताफ्याची सार्वभौम'),
    (r"###\s*\[CHR-HUM-11\]\s*Diver Finn\s*\(पाणबुडा फिन\)\s*—\s*खोल खाडीचा तस्कर",
     '### [CHR-HUM-11] Malhar, Deep-Sea Salvager (पाणबुडा मल्हार) — खोल खाडीचा तस्कर'),
    (r"###\s*\[CHR-HUM-15\]\s*Evelyn\s*\(एव्हलिन\)\s*—\s*वनौषधी तज्ज्ञ",
     '### [CHR-HUM-15] Ila, the Herbalist (वैद्य इला) — वनौषधी तज्ज्ञ'),

    # Asura Shard
    (r"###\s*\[CHR-ASU-03\]\s*Iron-Marshal Hilda\s*\(लोह-मार्शल हिल्डा\)\s*—\s*जड तोफखान्याची सेनापती",
     '### [CHR-ASU-03] Marshal Lauhini, "The Siege-Breaker" (मार्शल लौहिणी) — जड तोफखान्याची सेनापती'),
    (r"###\s*\[CHR-ASU-08\]\s*Dr\.\s*Erika\s*\(डॉ\.\s*एरिका\)\s*—\s*विषारी वाष्प व आम्ल-शिल्पी",
     '### [CHR-ASU-08] Ira, Foundry Chemist (रसायनज्ञ इरा) — विषारी वाष्प व आम्ल-शिल्पी'),
    (r"###\s*\[CHR-ASU-09\]\s*Commissar Ulka\s*\(असुर कामगार कमिसार उल्का\)\s*—\s*लाल हातोडा",
     '### [CHR-ASU-09] Ulka, "The Red Hammer" (श्रमिक नेते उल्का) — लाल हातोडा'),
    (r"###\s*\[CHR-ASU-11\]\s*Artisan Astrid\s*\(शिल्पी अॅस्ट्रिड\)\s*—\s*रुनिक शस्त्र व चकती कोरीव कामाची मास्टर",
     '### [CHR-ASU-11] Ashani, Master Smiths-Engraver (मुद्रा-लोहार अशनी) — रुनिक शस्त्र व चकती कोरीव कामाची मास्टर'),
    (r"###\s*\[CHR-ASU-13\]\s*Matron Olga\s*\(असुर अनाथालय प्रमुख ओल्गा\)\s*—\s*खोल खाणींची माता",
     '### [CHR-ASU-13] Amba, "Mother of the Pits" (खाण-माता अंबा) — खोल खाणींची माता'),
    (r"###\s*\[CHR-ASU-15\]\s*Shaila-Bhritya\s*\(शैल-भृत्य\)\s*—\s*बेसाल्ट द्वारपाल",
     '### [CHR-ASU-15] Kinkara, The Basalt Sentinel (किंकर) — बेसाल्ट द्वारपाल'),

    # Deva Shard
    (r"###\s*\[CHR-DEV-01\]\s*Sovereign Aurelius\s*\(देव-सम्राट ऑरेलियस\)\s*—\s*सौर सार्वभौम",
     '### [CHR-DEV-01] Bhanu, The Solar Sovereign (देव-सम्राट भानु) — सौर सार्वभौम'),
    (r"###\s*\[CHR-DEV-02\]\s*High Queen Seraphina\s*\(देव-राणी सेराफिना\)\s*—\s*दैवी खजिना व कायद्याची स्वामिनी",
     '### [CHR-DEV-02] Queen Savitri, Keeper of the Solar Purse (देव-राणी सावित्री) — दैवी खजिना व कायद्याची स्वामिनी'),
    (r"###\s*\[CHR-DEV-03\]\s*Commander Lysandra\s*\(सेनापती लायसँड्रा\)\s*—\s*वायव्य सैन्यदलाची सेनापती",
     '### [CHR-DEV-03] Vaijayanti, Sky-Marshal of Amaravati (सेनापती वैजयंती) — वायव्य सैन्यदलाची सेनापती'),
    (r"###\s*\[CHR-DEV-04\]\s*Marshal Cassian\s*\(सेनापती कॅशियन\)\s*—\s*सुवर्ण व्हॅनगार्ड",
     '### [CHR-DEV-04] Anshuman, Captain of the Sun-Lances (सेनापती अंशुमान) — सुवर्ण व्हॅनगार्ड'),
    (r"###\s*\[CHR-DEV-05\]\s*High Justice Themis\s*\(प्रधान न्यायामूर्ती थेमिस\)\s*—\s*उच्च दैवी न्यायपीठाचा निर्णायक",
     '### [CHR-DEV-05] Justice Dharma, The Blind Arbiter (प्रधान न्यायामूर्ती धर्म) — उच्च दैवी न्यायपीठाचा निर्णायक'),
    (r"###\s*\[CHR-DEV-06\]\s*Priestess Selene\s*\(मुख्य पुरोहिता सेलीन\)\s*—\s*सामंजस्यपूर्ण घंटांची स्वामिनी",
     '### [CHR-DEV-06] Revati, Seer of the Star-Tides (मुख्य पुरोहिता रेवती) — सामंजस्यपूर्ण घंटांची स्वामिनी'),
    (r"###\s*\[CHR-DEV-08\]\s*Master Weaver Julian\s*\(वस्त्र-शिल्पी ज्युलियन\)\s*—\s*सौर-रेशीम कारागीर",
     '### [CHR-DEV-08] Weaver Kavi, Master of the Silk-Looms (वस्त्र-शिल्पी कवी) — सौर-रेशीम कारागीर'),
    (r"###\s*\[CHR-DEV-09\]\s*Archon Theron\s*\(आर्कन थेरॉन\)\s*—\s*खगोलीय विरूपण संशोधक",
     '### [CHR-DEV-09] Chitraratha, Navigator of the Void-Rim (चित्ररथ) — खगोलीय विरूपण संशोधक'),
    (r"###\s*\[CHR-DEV-10\]\s*Courier Zephyr\s*\(दूत झेफिर\)\s*—\s*मरुत-वाहक",
     '### [CHR-DEV-10] Marut, The Wind-Runner (दूत मरुत) — मरुत-वाहक'),

    # Beast Shard
    (r"###\s*\[CHR-BST-01\]\s*Titan Ursus\s*\(शिखर-सम्राट उर्सस\)\s*—\s*चार-शिंगी पर्वत",
     '### [CHR-BST-01] Jambavan, "Old Four-Horns" (शिखर-सम्राट जांबवान) — चार-शिंगी पर्वत'),
    (r"###\s*\[CHR-BST-02\]\s*Serpent Empress Jormun\s*\(नाग-सम्राज्ञी जॉर्मुन\)\s*—\s*खोल मुळांची सार्वभौम",
     '### [CHR-BST-02] Kadru, "The Jade Coil" (नाग-सम्राज्ञी कद्रू) — खोल मुळांची सार्वभौम'),
    (r"###\s*\[CHR-BST-03\]\s*Sky Empress Valkyrie\s*\(गरुड-सम्राज्ञी वाल्किरी\)\s*—\s*उच्च सुयांची सार्वभौम",
     '### [CHR-BST-03] Vinata, "The Golden Maw" (गरुड-सम्राज्ञी विनता) — उच्च सुयांची सार्वभौम'),
    (r"###\s*\[CHR-BST-04\]\s*King Aquila\s*\(गरुड-सम्राट अॅक्विला\)\s*—\s*सुवर्ण नख",
     '### [CHR-BST-04] Sampati, "Iron-Talon" (गरुड-सम्राट संपाती) — सुवर्ण नख'),
    (r"###\s*\[CHR-BST-05\]\s*Void-Matriarch Nyx\s*\(छाया-नेत्री निक्स\)\s*—\s*छाया-द्रोणीची मातृकुलप्रमुख",
     '### [CHR-BST-05] Shyama, "The Shadow-Cat" (छाया-नेत्री श्यामा) — छाया-द्रोणीची मातृकुलप्रमुख'),
    (r"###\s*\[CHR-BST-06\]\s*Queen Freya\s*\(शार्दूल-राणी फ्रेया\)\s*—\s*रक्त-कड्याच्या सीमांची राणी",
     '### [CHR-BST-06] Sarama, "Queen of Blood-Ridge" (शार्दूल-राणी सरमा) — रक्त-कड्याच्या सीमांची राणी'),
    (r"###\s*\[CHR-BST-07\]\s*Shaman Morvath\s*\(शामन मॉर्व्हाथ\)\s*—\s*पशू व मानव यांचा महा-सेतु",
     '### [CHR-BST-07] Shabari, "The Bone-Speaker" (शामन शबरी) — पशू व मानव यांचा महा-सेतु'),
    (r"###\s*\[CHR-BST-08\]\s*Hermit Matanga Eldir\s*\(मतंग एल्डिर\)\s*—\s*शांत वनराईचा संन्यासी",
     '### [CHR-BST-08] Sage Matanga, Keeper of the Silent Glade (महर्षी मतंग) — शांत वनराईचा संन्यासी'),

    # Abyss Shard
    (r"###\s*\[CHR-ABY-08\]\s*Andha-Kāka\s*\(अंध-काक\)\s*—\s*दगड-डोळ्यांचा कावळा",
     '### [CHR-ABY-08] Kagabhushundi, The Stone-Eyed Crow (कागभुशुंडी) — दगड-डोळ्यांचा कावळा'),
    (r"###\s*\[CHR-ABY-08\]\s*Andha-Kaka\s*\(अंध-काक\)\s*—\s*दगड-डोळ्यांचा कावळा",
     '### [CHR-ABY-08] Kagabhushundi, The Stone-Eyed Crow (कागभुशुंडी) — दगड-डोळ्यांचा कावळा'),
]

# Character name mentions across prose, relations, tables
text_replacements = [
    # Full Titles / Names first
    ("Commander Bhim II", 'Captain Bhima, "The Trench Bull"'),
    ("कमांडर भीमसेन द्वितीय", "कॅप्टन भीमा (Captain Bhima)"),
    ("कमांडर भीम द्वितीय", "कॅप्टन भीमा"),
    ("Master Engineer Rohini-Bai", "Rohini, Chief Railwright"),
    ("Superintendent Vance", 'Yardmaster Alistair Vance, "Clockwork Vance"'),
    ("High Admiral Silas Suhotra", 'Lord Admiral Suhotra, "The Silver Shark"'),
    ("Silas Suhotra", "Lord Admiral Suhotra"),
    ("Commodore Linnea Brandt", 'Commodore Lavanya, "The Sea Wolf"'),
    ("Linnea Brandt", "Commodore Lavanya"),
    ("Diver Finn", "Malhar, Deep-Sea Salvager"),
    ("पाणबुडा फिन", "पाणबुडा मल्हार"),
    ("Iron-Marshal Hilda", 'Marshal Lauhini, "The Siege-Breaker"'),
    ("लोह-मार्शल हिल्डा", "मार्शल लौहिणी"),
    ("Dr. Erika", "Ira, Foundry Chemist"),
    ("डॉ. एरिका", "रसायनज्ञ इरा"),
    ("Commissar Ulka", 'Ulka, "The Red Hammer"'),
    ("कमिसार उल्का", 'उल्का ("The Red Hammer")'),
    ("Artisan Astrid", "Ashani, Master Smiths-Engraver"),
    ("शिल्पी अॅस्ट्रिड", "मुद्रा-लोहार अशनी"),
    ("Matron Olga", 'Amba, "Mother of the Pits"'),
    ("ओल्गा", "अंबा"),
    ("Shaila-Bhritya", "Kinkara, The Basalt Sentinel"),
    ("शैल-भृत्य", "किंकर"),
    ("Sovereign Aurelius", "Bhanu, The Solar Sovereign"),
    ("सम्राट ऑरेलियस", "सम्राट भानु"),
    ("High Queen Seraphina", "Queen Savitri, Keeper of the Solar Purse"),
    ("राणी सेराफिना", "राणी सावित्री"),
    ("Commander Lysandra", "Vaijayanti, Sky-Marshal of Amaravati"),
    ("सेनापती लायसँड्रा", "सेनापती वैजयंती"),
    ("Marshal Cassian", "Anshuman, Captain of the Sun-Lances"),
    ("सेनापती कॅशियन", "सेनापती अंशुमान"),
    ("High Justice Themis", "Justice Dharma, The Blind Arbiter"),
    ("न्यायामूर्ती थेमिस", "न्यायामूर्ती धर्म"),
    ("Priestess Selene", "Revati, Seer of the Star-Tides"),
    ("पुरोहिता सेलीन", "पुरोहिता रेवती"),
    ("Master Weaver Julian", "Weaver Kavi, Master of the Silk-Looms"),
    ("ज्युलियन", "कवी"),
    ("Archon Theron", "Chitraratha, Navigator of the Void-Rim"),
    ("थेरॉन", "चित्ररथ"),
    ("Courier Zephyr", "Marut, The Wind-Runner"),
    ("झेफिर", "मरुत"),
    ("Titan Ursus", 'Jambavan, "Old Four-Horns"'),
    ("सम्राट उर्सस", "सम्राट जांबवान"),
    ("Serpent Empress Jormun", 'Kadru, "The Jade Coil"'),
    ("सम्राज्ञी जॉर्मुन", "सम्राज्ञी कद्रू"),
    ("Sky Empress Valkyrie", 'Vinata, "The Golden Maw"'),
    ("सम्राज्ञी वाल्किरी", "सम्राज्ञी विनता"),
    ("King Aquila", 'Sampati, "Iron-Talon"'),
    ("सम्राट अॅक्विला", "सम्राट संपाती"),
    ("Void-Matriarch Nyx", 'Shyama, "The Shadow-Cat"'),
    ("छाया-नेत्री निक्स", "छाया-नेत्री श्यामा"),
    ("Queen Freya", 'Sarama, "Queen of Blood-Ridge"'),
    ("राणी फ्रेया", "राणी सरमा"),
    ("Shaman Morvath", 'Shabari, "The Bone-Speaker"'),
    ("शामन मॉर्व्हाथ", "शामन शबरी"),
    ("Hermit Matanga Eldir", "Sage Matanga, Keeper of the Silent Glade"),
    ("मतंग एल्डिर", "महर्षी मतंग"),
    ("Andha-Kāka", "Kagabhushundi, The Stone-Eyed Crow"),
    ("Andha-Kaka", "Kagabhushundi, The Stone-Eyed Crow"),
    ("अंध-काक", "कागभुशुंडी"),

    # Beast Lineages
    ("वायू-अश्व (Vayu-Ashva / Gale Stallion)", "Gale Stallion (वायू-अश्व)"),
    ("वज्र-वराह (Vajra-Varaha / Iron Boar)", "Ironclad Boar (वज्र-वराह)"),
    ("मकर-शिशू (Makara-Shishu / Sea-Crocodile)", "River Drake (मकर-शिशू)"),
    ("ज्वाला-शार्दूल (Magma-Shardul / Lava Tiger)", "Magma Tiger (ज्वाला-शार्दूल)"),
    ("मॅग्मा-शार्दूल (Magma-Shardul)", "Magma Tiger (ज्वाला-शार्दूल)"),
    ("अशनी-भल्लूक (Ashani-Bhalluka / Storm Bear)", "Thunder Bear (अशनी-भल्लूक)"),
    ("अग्नि-सर्प (Agni-Sarpa)", "Flame Viper (अग्नि-सर्प)"),
    ("वज्र-महिष (Vajra-Mahisha / Iron Bison)", "Iron Bison (वज्र-महिष)"),

    # Power Purges (Anime & Compounds)
    ("Armament Haki (शस्त्र भारणे)", "Iron Imbuement (शस्त्र भारणे)"),
    ("Armament Haki", "Iron Imbuement"),
    ("Conqueror's Haki (क्रांतिकारी संकल्प)", "Sovereign Dread (क्रांतिकारी संकल्प)"),
    ("Conqueror's Haki", "Sovereign Dread"),
    ("Six Eyes / Byakugan (धातू-दोष दृष्टी)", "Meridian Sight (धातू-दोष दृष्टी)"),
    ("Six Eyes / Byakugan", "Meridian Sight"),
    ("Six Eyes / Far-Sight", "Meridian Sight"),
    ("Six Eyes", "Meridian Sight"),
    ("Byakugan", "Meridian Sight"),
    ("Flash Step (Shunpo) / Vayu-Krama", "Gale Step"),
    ("Flash Step (Shunpo)", "Gale Step"),
    ("Flash Step", "Gale Step"),
    ("Black Flash (ध्वनिक अनुनाद / कंपने)", "Kinetic Rupture (ध्वनिक अनुनाद / कंपने)"),
    ("Black Flash / Vajra-Aghata", "Kinetic Rupture"),
    ("Black Flash", "Kinetic Rupture"),
    ("World Cutting Slash / Akasha-Cheda", "Void Cleave"),
    ("World Cutting Slash", "Void Cleave"),
    ("Absolute Command (Geass)", "Will-Binding (वशित्व)"),
    ("Absolute Command (राजनयिक साम-संवाद)", "Will-Binding (राजनयिक साम-संवाद)"),
    ("Absolute Command (वशित्व / अंतिम हुकूम)", "Will-Binding (वशित्व / अंतिम हुकूम)"),
    ("Absolute Command", "Will-Binding"),
    ("Total Hypnosis (Sammohana-Svara)", "Sensory Mirage"),
    ("Total Hypnosis", "Sensory Mirage"),
    ("Spider-Sense", "Danger Instinct"),
    ("Soul Vision (Reikaku)", "Soul-Sight"),
    ("Soul Vision", "Soul-Sight"),
    ("Decay (Respira)", "Necrotic Rot"),
    ("Respira", "Necrotic Rot"),
    ("Creation Rebirth", "Cellular Rebirth"),
    ("Bounded Field (Curtain / Kekkai)", "Isolation Ward"),
    ("Bounded Field (Curtain)", "Isolation Ward"),
    ("Bounded Field", "Isolation Ward"),
    ("Preta Path (Energy Drain)", "Siphon Ward"),
    ("Preta Path", "Siphon Ward"),
    ("Godspeed", "Sonic Stride"),
    ("Vajra Deha (लौह-त्वक् / लोखंडी त्वचा तंत्र)", "Diamond Body / Iron Skin"),
    ("Vajra Deha (श्रमिकांची कणखर त्वचा)", "Diamond Body / Iron Skin (श्रमिकांची कणखर त्वचा)"),
    ("Agni-Needle (अग्नि-शलाका)", "Thermal Lance (अग्नि-शलाका)"),
    ("Agni-Needle", "Thermal Lance"),
    ("Savitra-Nīla (नील सौर-अग्नी)", "Blue Sunfire (नील सौर-अग्नी)"),
    ("Savitra-Nila", "Blue Sunfire"),
    ("Hima-Stasis (काल-गोठवण)", "Kinetic Freeze (काल-गोठवण)"),
    ("Hima-Stasis", "Kinetic Freeze"),
    ("Vajra Lamina (वज्र-पटल)", "Diamond Marrow (वज्र-पटल)"),
    ("Vajra Lamina", "Diamond Marrow"),
    ("Flying Slash (असि-धारा)", "Blade Aura (असि-धारा)"),
    ("Śabda-Bhedī Archery", "Blind-Ear Archery"),
    ("Divya-Śrotra (टेक्टोनिक आवरणातील सूक्ष्म-कंपने हेरणे)", "Far-Hearing (टेक्टोनिक आवरणातील सूक्ष्म-कंपने हेरणे)"),
    ("Divya-Śrotra (भू-कंपन भाषांतर)", "Far-Hearing (भू-कंपन भाषांतर)"),
    ("Divya-Śrotra", "Far-Hearing"),
    ("Divya-Srotra", "Far-Hearing"),
    ("Satya-Drishti", "Truth-Sight"),
    ("Manasika-Kavacha", "Mind-Shield"),
    ("Mrita-Sanjeevani / Soma-Vidya", "Resuscitation Arts / Vitality Brew"),
    ("Mrita-Sanjeevani", "Resuscitation Arts"),
    ("Chakravyuha Formations", "Labyrinth Formation (Spiral Siege Array)"),
    ("Chakravyūha Formations", "Labyrinth Formation (Spiral Siege Array)"),
    ("Kama-Rupa / Virat Asura Rupa", "Flesh-Shifting / War-Titan Form"),
    ("Kāma-Rūpa (कामरूप / स्वैर रूपबदल)", "Flesh-Shifting (कामरूप / स्वैर रूपबदल)"),
    ("Kāma-Rūpa", "Flesh-Shifting"),
    ("Kshetra-Bandhana / Manasika Kshetra", "Domain Expansion / Territory Lock"),
    ("Kshetra-Bandhana", "Domain Expansion / Territory Lock"),
    ("Marma-Adhyaya & Vajra-Mushti", "Vital-Point Striking & Spiked-Knuckle Brawling"),
    ("Sankara-Astra Craft", "Scrap-Ordnance Rigging"),

    # Species Growth Engines
    ("Nadi-Shuddhi (Meridian Purification) & External Talismans", "Meridian Tempering & Breath Alignment"),
    ("Dhatu-Dharana (Thermal Stress & Kinetic Smelting)", "Marrow Smelting & Thermal Hardening"),
    ("Rta-Samyama (Harmonic Celestial Resonance)", "Solar Attunement & Light-Weaving"),
    ("Rta-Samyama & Prakasha-Racana", "Solar Attunement & Light-Weaving"),
    ("Kaya-Kosa (Darwinian Molting & Essence Ingestion)", "Carapace Evolution & The Molt (Kaya-Kosa & Nirmoka)"),
    ("Nadi-Shuddhi & Nadi-Sandhana", "Meridian Tempering & Breath Alignment"),
    ("Dhatu-Dharana & Agni-Sadhana", "Marrow Smelting & Thermal Hardening"),
    ("Kaya-Kosa & Nirmoka", "Carapace Evolution & The Molt (Kaya-Kosa & Nirmoka)"),

    # Cultivation Failures, Diseases & Combat Vows
    ("Subtle Body Rupture (Sūkṣma-Bhaṅga)", "Core Fracture / Nerve Rupture (Sukshma-Bhanga)"),
    ("Subtle Body Rupture (Sukshma-Bhanga)", "Core Fracture / Nerve Rupture (Sukshma-Bhanga)"),
    ("Kāca-Dāha (Glass-Burns)", "Glass-Burns / Slag-Scars (Kaca-Daha)"),
    ("Kaca-Daha", "Glass-Burns / Slag-Scars (Kaca-Daha)"),
    ("Shvasa-Kshaya", "Slag-Lung (Shvasa-Kshaya)"),
    ("Solar Fever", "Sun-Fever / Crown Burn (Solar Fever)"),
    ("Apasvara Toxin", "Discord Venom (Apasvara Toxin)"),
    ("Saṅkalpa-Bandha (Prana-Sima, Kaya-Bali, Satya-Sandha)", "Binding Pledges: (1) Target Restriction Vow, (2) Flesh-Sacrifice Vow, (3) Open-Hand Disclosure"),
    ("Prāṇa-Sīmā (मर्यादित वापर प्रतिज्ञा)", "Target Restriction Vow (Prāṇa-Sīmā / मर्यादित वापर प्रतिज्ञा)"),
    ("Kāyā-Bali (शरीर-बलिदान अट)", "Flesh-Sacrifice Vow (Kāyā-Bali / शरीर-बलिदान अट)"),
    ("Satya-Sandha (उद्देश्य प्रकटीकरण)", "Open-Hand Disclosure Vow (Satya-Sandha / Revealing One's Hand)"),

    # Magic & Underworld
    ('The "Kay-Tyag" (Soul-Only) Filter (काय-त्याग नियम)', 'The Flesh-Severance Law (Soul-Only Filter / Kay-Tyag Law)'),
    ('The "Kay-Tyag" Law', 'The Flesh-Severance Law (Soul-Only Filter / Kay-Tyag)'),
    ("Kay-Tyag Filter", "Flesh-Severance Filter (Kay-Tyag Filter)"),
    ("Atma-Kshaya", "Soul-Rot Contagion (Atma-Kshaya)"),
    ("Dik-Anka", "Spatial Coordinates (Dik-Anka / Void Bearing)"),
    ("Aether Mudra", "Blood-Ward Contract (Aether Mudra)"),
    ("Vikara-Jeevas", "Slag-Fiends / Scrap-Ghouls (Vikara-Jeeva)"),
    ("Vikara-Jeeva", "Slag-Fiends / Scrap-Ghouls (Vikara-Jeeva)"),
    ("Atma-Shuddhi", "Soul Clarity (Atma-Shuddhi)"),
    ("Ātma-Śuddhi", "Soul Clarity (Atma-Shuddhi)"),
    ("Smriti-Shlesha", "Past-Life Echoes (Smriti-Shlesha)"),
    ("Lihito vs. Rikta", "Written Fate vs. Blank Slate (Lihito vs. Rikta)"),
]

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content
    changes_count = 0

    # 1. Header regexes
    for pattern, repl in char_header_replacements:
        matches = len(re.findall(pattern, content))
        if matches > 0:
            content = re.sub(pattern, repl, content)
            changes_count += matches

    # 2. String replacements
    for old_s, new_s in text_replacements:
        if old_s in content:
            c = content.count(old_s)
            content = content.replace(old_s, new_s)
            changes_count += c

    if content != orig_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        rel_p = os.path.relpath(file_path, _project_root)
        print(f"Updated {rel_p}: {changes_count} replacements applied.")
        return True, changes_count
    return False, 0

total_updated = 0
total_changes = 0
for fp in target_files:
    changed, count = process_file(fp)
    if changed:
        total_updated += 1
        total_changes += count

print(f"\nTotal files updated: {total_updated} / {len(target_files)}, Total replacements: {total_changes}")
