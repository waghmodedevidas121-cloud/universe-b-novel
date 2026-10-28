import os
import re
import sys

_current_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_current_dir)
base_dir = os.path.join(_project_root, "New")

print(f"Project root: {_project_root}")
print(f"Base dir: {base_dir}")

target_files = []
for root, dirs, files in os.walk(base_dir):
    if any(x in root for x in ["trash", "__pycache__", ".git", "_preview"]):
        continue
    for file in files:
        if file.endswith(".md"):
            target_files.append(os.path.join(root, file))

# Add script files that contain texts
target_files.append(os.path.join(_current_dir, "dynasties_data.py"))
target_files.append(os.path.join(_current_dir, "character_shard_mappings.py"))
target_files.append(os.path.join(_current_dir, "portal_template.html"))
target_files.append(os.path.join(_current_dir, "story_html_content.py"))

print(f"Found {len(target_files)} target files to process")

# Ordering is critical: specific longer multi-word strings first, then shorter terms
c_replacements = [
    # 1. Weapons, Relics & Character Gear
    ("Raja Mudra (साम्राज्य सुवर्ण मुद्रा) व .४४ कॅलिबर सर्व्हिस रिव्हॉल्व्हर (Industrial Firearms)",
     "The Imperial Signet (साम्राज्य सुवर्ण मुद्रा) व .44 Concord Service Revolver"),
    ("Raja Mudra (साम्राज्य सुवर्ण मुद्रा)", "The Imperial Signet (साम्राज्य सुवर्ण मुद्रा)"),
    ("Raja Mudra", "The Imperial Signet"),
    ("SAS-ORD-02: Stormshot Heavy Trench Rifle (वज्र-नालिका १५ मिमी रुनिक अँटी-मटेरियल)",
     "SAS-ORD-02: 15mm Heavy Trench Anti-Materiel Rifle (वज्र-नालिका १५ मिमी)"),
    ("Vajra-Nalika 15mm Rifle", "15mm Heavy Trench Anti-Materiel Rifle"),
    ("वज्र-नालिका १५ मिमी रुनिक अँटी-मटेरियल", "15mm Heavy Trench Anti-Materiel Rifle (वज्र-नालिका १५ मिमी)"),
    ("वज्र-नालिका १५ मिमी", "15mm Heavy Trench Anti-Materiel Rifle"),
    ("Mayavi-Mana (Sledgehammer)", "The Tectonic Maul (Obsidian Sledge)"),
    ("मायावी-मान (टेक्टोनिक रुनिक स्लेजहॅमर)", "The Tectonic Maul (Obsidian Sledge / मायावी-मान)"),
    ("मायावी-मान", "The Tectonic Maul (Obsidian Sledge)"),
    ("Surya-Danda", "The Sun-Scepter (Solar Lance)"),
    ("सूर्य-दंड (सौर प्लाझ्मा राजदंड)", "The Sun-Scepter (Solar Lance / सूर्य-दंड)"),
    ("सूर्य-दंड", "The Sun-Scepter (Solar Lance)"),
    ("Jyoti-Shanku", "The Prismatic Javelin"),
    ("ज्योति-शंकु (तेजस्वी दैवी भाला जो सूर्यप्रकाश गतिज किरणात बदलतो)", "The Prismatic Javelin (ज्योति-शंकु — तेजस्वी दैवी भाला)"),
    ("ज्योति-शंकु", "The Prismatic Javelin"),
    ("Megha-Ankusha", "The Cloud-Goad"),
    ("मेघ-अंकुश व आकाशीय वाफेचे होकायंत्र", "The Cloud-Goad (मेघ-अंकुश) व आकाशीय वाफेचे होकायंत्र"),
    ("मेघ-अंकुश", "The Cloud-Goad (मेघ-अंकुश)"),
    ("Surya-Katyar", "The Sun-Dagger"),
    ("सूर्य-कट्यार", "The Sun-Dagger (सूर्य-कट्यार)"),
    ("Sama-Mudra", "The Concord Mace (Golden Gavel)"),
    ("साम-मुद्रा (ग्रँड कॉन्कॉर्ड सुवर्ण न्यायदंड)", "The Concord Mace (Golden Gavel / साम-मुद्रा)"),
    ("साम-मुद्रा", "The Concord Mace (Golden Gavel)"),
    ("Satya-Danda", "The Scales of Concord"),
    ("सत्य-दंडाची मुद्रा व कुरु-अमरावती कायदेशीर संहिता", "The Scales of Concord (सत्य-दंडाची मुद्रा) व कुरु-अमरावती कायदेशीर संहिता"),
    ("सत्य-दंडाची मुद्रा", "The Scales of Concord (सत्य-दंडाची मुद्रा)"),
    ("Satyaketu Patra (ऑडिट खतावणी / २४-तासांची लाल-शाई सील) व सत्य-मुद्रा राजदंड",
     "The Auditor's Ledger & The 24-Hour Red-Ink Seal (सत्यकेतु पत्र व रक्त-मुद्रा) व सत्य-मुद्रा राजदंड"),
    ("Satyaketu Patra & Rakta-Mudra", "The Auditor's Ledger & The 24-Hour Red-Ink Seal"),
    ("Satyaketu Patra", "The Auditor's Ledger"),
    ("Vajra Mudra Great Mace", "The Bastion Great-Mace"),
    ("Vajra Mudra (वज्र मुद्रा) कोरलेली महा-गदा", "The Bastion Great-Mace (वज्र मुद्रा कोरलेली महा-गदा)"),
    ("Jnana-Sutra Calipers", "Brass Rift-Calipers"),
    ("ज्ञान-सूत्र (पितळी मापक-काटे व दुर्बीण)", "Brass Rift-Calipers (ज्ञान-सूत्र मापक-काटे व दुर्बीण)"),
    ("Amrita-Shalaka", "The Vitality Lancet"),
    ("अमृत-शलाका, माती-शोधक भिंग व संजीवनी पेटिका", "The Vitality Lancet (अमृत-शलाका), माती-शोधक भिंग व संजीवनी पेटिका"),
    ("अमृत-शलाका", "The Vitality Lancet (अमृत-शलाका)"),
    ("Yantra-Chakra & Tamas-Kaca Sword", "The Phosphorus Saw-Wheel & The Black-Glass Blade"),
    ("तमास-काच खड्ग व क्षय-ज्वाला राजदंड", "The Black-Glass Blade (तमास-काच खड्ग) व क्षय-ज्वाला राजदंड"),
    ("तमास-काच खड्ग", "The Black-Glass Blade (तमास-काच खड्ग)"),
    ("दातेरी तबकडी (*यंत्र-चक्र*)", "The Phosphorus Saw-Wheel (यंत्र-चक्र)"),
    ("दातेरी तबकडी (यंत्र-चक्र)", "The Phosphorus Saw-Wheel (यंत्र-चक्र)"),
    ("Vajra-Musala", "The 1,200-lb Ironclad Maul"),
    ("Vajra Musala (१,२०० पाउंडांची काटेरी लोखंडी गदा)", "The 1,200-lb Ironclad Maul (१,२०० पाउंडांची काटेरी लोखंडी गदा)"),
    ("काटेरी गदा (*वज्र-मुसल*)", "The 1,200-lb Ironclad Maul (काटेरी गदा / वज्र-मुसल)"),
    ("Vajra Musala", "The 1,200-lb Ironclad Maul"),
    ("Palaka-Danda", "The Aegis Scepter"),
    ("पालक-दंड (Sovereign Aegis Scepter)", "The Aegis Scepter (पालक-दंड)"),
    ("पालक-दंड", "The Aegis Scepter"),
    ("Rta-Danda", "The Inquisitor's Seal"),
    ("ऋत-दंडाची मुद्रा, २४-तासांचे रक्त-मुद्रा वॉरंट", "The Inquisitor's Seal (ऋत-दंडाची मुद्रा), २४-तासांचे रक्त-मुद्रा वॉरंट"),
    ("ऋत-दंडाची मुद्रा", "The Inquisitor's Seal (ऋत-दंडाची मुद्रा)"),
    ("Srishti-Danda", "The Architect's Seal"),
    ("सृष्टी-दंडाची मुद्रा व ब्रह्म-ज्ञान संहिता", "The Architect's Seal (सृष्टी-दंडाची मुद्रा) व ब्रह्म-ज्ञान संहिता"),
    ("सृष्टी-दंडाची मुद्रा", "The Architect's Seal (सृष्टी-दंडाची मुद्रा)"),
    ("SAS-ORD-01: Ironfang (खंदक खंजीर)", "SAS-ORD-01: Ironfang Trench Dagger (खंदक खंजीर)"),
    ("SAS-ORD-01: Ironfang (तुकडे झालेला खंजीर)", "SAS-ORD-01: Ironfang Trench Dagger (तुकडे झालेला खंजीर)"),
    ("SAS-ORD-02: Stormshot Aether-Carbine (दुहेरी-नळी ब्रीच-लोडिंग कार्बाइन)",
     "SAS-ORD-02: Drop-Lock Trench Carbine #7 (दुहेरी-नळी ब्रीच-लोडिंग कार्बाइन)"),
    ("SAS-ORD-02: Stormshot Armored Grenadier Carbine", "SAS-ORD-02: Drop-Lock Trench Carbine #7"),
    ("SAS-ORD-02: Stormshot Heavy Carbines (अ-प्राणघातक गोळ्या)", "SAS-ORD-02: Drop-Lock Trench Carbines #7 (अ-प्राणघातक गोळ्या)"),
    ("SAS-ORD-02: Stormshot Heavy Carbines", "SAS-ORD-02: Drop-Lock Trench Carbines #7"),
    ("SAS-ORD-02: Stormshot Sniper Rifle", "SAS-ORD-02: Drop-Lock Trench Carbine #7 (Sniper Model)"),
    ("SAS-ORD-02: Stormshot Rifle", "SAS-ORD-02: Drop-Lock Trench Carbine #7"),
    ("SAS-ORD-04: Riftbreaker Siege Howitzer (८० मिमी वायवीय तोफ)",
     "SAS-ORD-04: 80mm Riftbreaker Siege Howitzer (८० मिमी वायवीय तोफ)"),
    (".४४ कॅलिबर सर्व्हिस रिव्हॉल्व्हर (Industrial Firearms)", ".44 Concord Service Revolver (.४४ सर्व्हिस रिव्हॉल्व्हर)"),

    # 2. Vehicles, Transit, Documents & Administrative Artifacts
    ("Dootan चे **White Doot-Yānas** (*The White Couriers*)", "Dootan चे **The White Couriers (Levitating Brass Carriages / White Doot-Yānas)**"),
    ("Dootan's White Doot-Yānas — *The White Couriers*", "The White Couriers (Levitating Brass Carriages / White Doot-Yānas)"),
    ("Dootan’s White Doot-Yānas — *The White Couriers*", "The White Couriers (Levitating Brass Carriages / White Doot-Yānas)"),
    ("Dootan च्या *White Doot-Yānas*", "Dootan च्या *The White Couriers (Levitating Brass Carriages / White Doot-Yānas)*"),
    ("White Doot-Yānas (The White Couriers)", "The White Couriers (Levitating Brass Carriages / White Doot-Yānas)"),
    ("White Doot-Yānas Teleport", "The White Couriers (Levitating Brass Carriages) Teleport"),
    ("White Doot-Yānas आणि अधिकृत", "The White Couriers (Levitating Brass Carriages) आणि अधिकृत"),
    ("White Doot-Yānas", "The White Couriers (Levitating Brass Carriages / White Doot-Yānas)"),
    ("White Doot-Yanas", "The White Couriers (Levitating Brass Carriages / White Doot-Yānas)"),
    ("Setu-Vajra-Ratha", "The Setu Ironclad War-Train"),
    ("Garuda-Class armored steam locomotives", "The Falcon-Class Armored Locomotives"),
    ("Garuda-Class Locomotive", "The Falcon-Class Armored Locomotive"),
    ("Garuda-Class", "The Falcon-Class Armored Locomotive"),
    ("Varuna-Vata Frigate", "HMS Storm-Tide (Ironclad Frigate)"),
    ("Varuna's Gale", "HMS Storm-Tide (Ironclad Frigate)"),
    ("Vajra-Tarangini Frigate", "HMS Wave-Breaker (Flagship Frigate)"),
    ("Frigate *Vajra-Tarangini*", "Flagship Frigate *HMS Wave-Breaker*"),
    ("Vajra-Tarangini", "HMS Wave-Breaker"),
    ("Lauha-Garjana", "The Iron Roar (Armored Siege Train)"),
    ("यमाकडे `Ātma-Nirgama Patra` ने विनंती", "यमाकडे `Inter-Realm Soul Requisition Writ (Ātma-Nirgama Patra)` ने विनंती"),
    ("`Ātma-Nirgama Patra` — कोणता आत्मा, का", "`Inter-Realm Soul Requisition Writ (Ātma-Nirgama Patra)` — कोणता आत्मा, का"),
    ("Ātma-Nirgama Patra", "Inter-Realm Soul Requisition Writ (Ātma-Nirgama Patra)"),
    ("Purṇa-Karma प्रमाणपत्र + Release Seal", "Certificate of Completed Fate (Release Seal / Purna-Karma)"),
    ("Purna-Karma Certificate", "Certificate of Completed Fate (Release Seal / Purna-Karma)"),
    ("Purna-Karma", "Certificate of Completed Fate (Purna-Karma)"),
    ("Pravasa-Patra & Transit Mudras", "Stamped Transit Passports & Gateway Permits (Pravasa-Patra)"),
    ("Pravasa-Patra (Travel Warrant)", "Stamped Transit Passports & Gateway Permits (Pravasa-Patra)"),
    ("Vidhana-Patra (Administrative law)", "High Council Statutory Writs (Vidhana-Patra Administrative Law)"),
    ("Vidhana-Patra (Administrative Law)", "High Council Statutory Writs (Vidhana-Patra Administrative Law)"),
    ("Vidhana-Patra Law", "High Council Statutory Writs (Vidhana-Patra Law)"),
    ("Vidhana-Patras", "High Council Statutory Writs (Vidhana-Patras)"),
    ("Vidhana-Patra", "High Council Statutory Writs (Vidhana-Patra)"),
    ("Hastina-Kankan (हस्तिना-कंकण)", "The Hastinapur Iron Torc (हस्तिना-कंकण)"),
    ("Hastina-Kankan", "The Hastinapur Iron Torc"),
    ("Vajra-Mushti Seal (वज्र-मुष्टी मुद्रा)", "The Caldera Brass Gauntlet (वज्र-मुष्टी मुद्रा)"),
    ("Vajra-Mushti Seal", "The Caldera Brass Gauntlet"),
    ("Vanya-Dharma Ring (वन्य-धर्म वलय)", "The Canopy Heartwood Ring (वन्य-धर्म वलय)"),
    ("The Daily Concord Gazette आणि Sachitra Veer-Patrika",
     "The Daily Concord Gazette (सोबत: The Hastinapur Gazette) आणि The Illustrated Vanguard Weekly"),
    ("Sachitra Veer-Patrika", "The Illustrated Vanguard Weekly (सोबत: The Hastinapur Gazette)"),
    ("तपोवनातील कडू विलो-साल काढ्यांवर अवलंबून", "तपोवनातील Bitter Willow-Bark Draught (कडू विलो-साल काढा) वर अवलंबून"),
    ("तपोवन कडू विलो-साल काढ्या", "तपोवन Bitter Willow-Bark Draught (कडू विलो-साल काढा)"),
    ("कडू विलो-साल काढा", "Bitter Willow-Bark Draught (कडू विलो-साल काढा)"),

    # 3. Currencies & Trade Units
    ("| **Iron Slag Ingot (ISI)** | Asura Foundry Syndicate | उच्च-घनतेचे शुद्ध केलेले पोलादी बार | असुरांच्या फाउंड्रीजमधील अवजड धातू खरेदी व लाव्हा खाणकाम | **१ ISI = २५ Silver Panas (०.२५ AR)** |",
     "| **Foundry Iron Bar (FIB)** | Asura Foundry Syndicate | प्रमाणित उच्च-घनतेची पोलादी वीट | असुरांच्या फाउंड्रीजमधील अवजड धातू खरेदी व लाव्हा खाणकाम | **१ FIB = २५ Silver Panas (०.२५ AR)** |"),
    ("| **Solar Mithril (SM)** | Amaravati (Aditya Mint) | शुद्ध सौर-प्रिझम सुवर्ण मुद्रा | देव-लोकातील उच्च विधी वस्त्रे, स्फटिक आयात, आंतरराष्ट्रीय खंडणी | **१ SM = १० Aether-Rupees (१,००० SP)** |",
     "| **Solar Gold Sovereign (SGS)** | Amaravati (Aditya Mint) | शुद्ध सौर-सुवर्ण मुद्रा | देव-लोकातील उच्च विधी वस्त्रे, स्फटिक आयात, आंतरराष्ट्रीय खंडणी | **१ SGS = १० Aether-Rupees (१,००० SP)** |"),
    ("Iron Slag Ingot (ISI)", "Foundry Iron Bar (FIB)"),
    ("Solar Mithril (SM)", "Solar Gold Sovereign (SGS)"),
    ("Solar Mithril", "Solar Gold Sovereign (SGS)"),

    # 4. Locations, Gateways & Institutions
    ("[ PANCHAM-MAHA-GHAT ROTUNDA ]", "[ THE FIVE-ARCH ROTUNDA (CENTRAL GATEWAY PLAZA) ]"),
    ("Pancham-Maha-Ghat Rotunda", "The Five-Arch Rotunda (Central Gateway Plaza / Pancham-Maha-Ghat)"),
    ("Pancham-Maha-Ghat (पंचम-महा-घाट)", "The Five-Arch Rotunda (Central Gateway Plaza / पंचम-महा-घाट)"),
    ("'पंचम-महा-घाट' (Pancham-Maha-Ghat Rotunda)", "The Five-Arch Rotunda (Central Gateway Plaza / पंचम-महा-घाट)"),
    ("Pancham-Maha-Ghat", "The Five-Arch Rotunda (Central Gateway Plaza)"),
    ("[ HASTINA-MAHA-DVARA ]", "[ THE HASTINAPUR HIGH ARCH (HUMAN GATE) ]"),
    ("Hastina-Maha-Dvara (हस्तिना-महाद्वार — मानव खंड)", "The Hastinapur High Arch (Human Gate / Hastina-Maha-Dvara)"),
    ("Hastina-Maha-Dvara", "The Hastinapur High Arch (Human Gate)"),
    ("[ JVALA-TORANA       ]", "[ THE CALDERA BASALT ARCH (ASURA GATE) ]"),
    ("[ JVALA-TORANA ]", "[ THE CALDERA BASALT ARCH (ASURA GATE) ]"),
    ("Jvala-Torana (ज्वाला-तोरण — असुर खंड)", "The Caldera Basalt Arch (Asura Gate / Jvala-Torana)"),
    ("Jvala-Torana", "The Caldera Basalt Arch (Asura Gate)"),
    ("[ SURYA-GHAT DVARA   ]", "[ THE SUN-CLIFF ARCH (DEVA GATE)       ]"),
    ("[ SURYA-GHAT DVARA ]", "[ THE SUN-CLIFF ARCH (DEVA GATE) ]"),
    ("Surya-Ghat Dvara (सूर्य-घाट द्वार — देव खंड)", "The Sun-Cliff Arch (Deva Gate / Surya-Ghat Dvara)"),
    ("Surya-Ghat Dvara", "The Sun-Cliff Arch (Deva Gate)"),
    ("[ VANYA-DHARMA DVARA ]", "[ THE ROOT-CARVED ARCH (BEAST GATE)    ]"),
    ("Vanya-Dharma Dvara (वन्य-धर्म द्वार — श्वापद खंड)", "The Root-Carved Arch (Beast Gate / Vanya-Dharma Dvara)"),
    ("Vanya-Dharma Dvara", "The Root-Carved Arch (Beast Gate)"),
    ("नश्वर समुद्र (Nashvar Samudra — Mortal Sea)", "The Mortal Sea (Nashvar Samudra)"),
    ("नश्वर समुद्र (Nashvar Samudra)", "The Mortal Sea (Nashvar Samudra)"),
    ("Nashvar Samudra (Mortal Sea)", "The Mortal Sea (Nashvar Samudra)"),
    ("Nashvar Samudra", "The Mortal Sea (Nashvar Samudra)"),
    ("Akash-Kosha Central Bank", "The Central Reserve Bank (The Vaults of Truth / Akash-Kosha)"),
    ("Akash-Kosha Vaults", "The Central Reserve Bank Vaults (Akash-Kosha)"),
    ("Akash-Kosha बँक", "The Central Reserve Bank (Akash-Kosha)"),
    ("Akash-Kosha", "The Central Reserve Bank (Akash-Kosha)"),
    ("Maha-Lekha Central Ledger Bureau", "The Grand Hall of Ledgers (The Root Archive / Maha-Lekha-Bhavana)"),
    ("Maha-Lekha-Bhavana", "The Grand Hall of Ledgers (The Root Archive / Maha-Lekha-Bhavana)"),
    ("Maha-Lekha (महा-लेखा)", "The Grand Hall of Ledgers (Maha-Lekha Archive)"),
    ("Maha-Lekha", "The Grand Hall of Ledgers (Maha-Lekha)"),
    ("Sabha-Loka & Parama-Dhama", "The High Council Rotunda & The Supreme Sanctum (Sabha-Loka & Parama-Dhama)"),
    ("THE SABHA-LOKA PARLIAMENTARY ROTUNDA", "THE HIGH COUNCIL ROTUNDA (SABHA-LOKA PARLIAMENTARY ROTUNDA)"),
    ("Sabha-Loka Rotunda", "The High Council Rotunda (Sabha-Loka)"),
    ("सभा-लोक (High Council Realm)", "The High Council Rotunda (सभा-लोक / High Council Realm)"),
    ("सभा-लोक", "The High Council Rotunda (सभा-लोक)"),
    ("Parama-Dhama", "The Supreme Sanctum (Parama-Dhama)"),
    ("Setu Maha-Sena & Vajra-Durga", "The Setu Standing Army & The Bastion Fortress (Setu Maha-Sena & Vajra-Durga)"),
    ("Setu Mahā-Senā Grand Command", "The Setu Standing Army Grand Command (Setu Mahā-Senā)"),
    ("Setu Mahā-Senā", "The Setu Standing Army (Setu Mahā-Senā)"),
    ("Setu Maha-Sena", "The Setu Standing Army (Setu Maha-Sena)"),
    ("The Vajra Fortress (वज्र दुर्ग — Military HQ)", "The Bastion Fortress (The Vajra Fortress / HQ — वज्र दुर्ग)"),
    ("The Vajra Fortress", "The Bastion Fortress (The Vajra Fortress)"),
    ("वज्र-दुर्ग (Vajra-Durga)", "The Bastion Fortress (वज्र-दुर्ग / Vajra-Durga)"),
    ("Vajra-Durga", "The Bastion Fortress (Vajra-Durga)"),
    ("Gravitational Anchors (Guru Keela)", "Gravitational Pillars (Tectonic Staples / Guru-Keela)"),
    ("Gravitational Anchors (Guru-Keela)", "Gravitational Pillars (Tectonic Staples / Guru-Keela)"),
    ("Guru-Keela", "Gravitational Pillars (Tectonic Staples / Guru-Keela)"),
    ("Sāvitra-Prabhā", "The Golden Twilight (Sāvitra-Prabhā)"),
    ("Savitra-Prabha", "The Golden Twilight (Savitra-Prabha)"),
    ("अंतिम विसर्जन कक्षात (*Maha-Vilayana*)", "The Final Dissolution Chamber (अंतिम विसर्जन कक्ष / Maha-Vilayana)"),
    ("Maha-Vilayana", "The Final Dissolution Chamber (Maha-Vilayana)"),
    ("Lauha-Shramik Sangha", "The Red Crucible Union (Ironworkers' Brotherhood / Lauha-Shramik Sangha)"),
    ("लौह-श्रमिक संघ", "The Red Crucible Union (Ironworkers' Brotherhood / Lauha-Shramik Sangha)"),
    ("Yantra-Pariksha (Furnace Trials)", "The Forge Trials (Yantra-Pariksha / Furnace Trials)"),
    ("यंत्र-परीक्षा (Yantra-Pariksha)", "The Forge Trials (यंत्र-परीक्षा / Yantra-Pariksha)"),
    ("Yantra-Pariksha", "The Forge Trials (Yantra-Pariksha)"),
    ("ZONE A: THE PRIMEVAL CANOPY (महा कांतार)", "ZONE A: THE PRIMEVAL CANOPY (महा कांतार)"),
    ("The Primeval Canopy (महा कांतार — आदिम छत्र)", "The Primeval Canopy (महा कांतार — आदिम छत्र)"),
    ("The Suparna Roost (सुपर्ण-गिरी)", "The Eagle's Roost (Suparna-Giri / सुपर्ण-गिरी)"),
    ("Suparna-Giri", "The Eagle's Roost (Suparna-Giri)"),
    ("Niraya-Kshetra & Tamo-Loka", "The Dead Chasm (Seal 7 Pit) & The Corrupted Abyss (Niraya-Kshetra & Tamo-Loka)"),
    ("Niraya-Kshetra", "The Dead Chasm (Seal 7 Pit / Niraya-Kshetra)"),
    ("Niraya Kshetra", "The Dead Chasm (Seal 7 Pit / Niraya-Kshetra)"),
    ("CORRUPTED REALM (TAMO LOKA)", "CORRUPTED REALM (THE CORRUPTED ABYSS / TAMO-LOKA)"),
    ("Tamo-Loka", "The Corrupted Abyss (Tamo-Loka)"),
    ("Kul-Sabha (कुळ-सभा)", "The Clan Council (Kul-Sabha / कुळ-सभा)"),
    ("Kul-Sabha", "The Clan Council (Kul-Sabha)"),
    ("Kshetra-Sabha (क्षेत्र-सभा)", "The Provincial Assembly (Kshetra-Sabha / क्षेत्र-सभा)"),
    ("Kshetra-Sabhas", "The Provincial Assemblies (Kshetra-Sabhas)"),
    ("Kshetra-Sabha", "The Provincial Assembly (Kshetra-Sabha)"),
    ("**Kāla-Kūṭa** *(Primordial Thermal Venom)*", "**The Thermal Venom (Seal 1 / Kāla-Kūṭa)**"),
    ("**Vṛtra-Chāyā** *(Light-Devouring Shadow)*", "**The Light-Devourer (Seal 2 / Vṛtra-Chāyā)**"),
    ("**Lauha-Bhakshaka** *(The Rust Colossus)*", "**The Rust Colossus (Seal 3 / Lauha-Bhakshaka)**"),
    ("**Shūnya-Jvala** *(The Cold Void Flame)*", "**The Cold Void-Flame (Seal 4 / Shūnya-Jvala)**"),
    ("**Hima-Rākshasa** *(The Entropy Sovereign)*", "**The Frost Sovereign (Seal 5 / Hima-Rākshasa)**"),
    ("**Prāṇa-Shūnyatā** *(Soul-Dissolving Void)*", "**The Soul-Vacuum (Seal 6 / Prāṇa-Shūnyatā)**"),
    ("**Mahā-Tamas** *(The Seventh Primordial Horror)*", "**The Seventh Darkness / Primordial Void (Seal 7 / Mahā-Tamas)**"),
    ("ARMORED WAR-TRAIN CORPS", "THE SETU IRONCLAD WAR-TRAIN CORPS"),
]

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content
    changes_count = 0

    for old_s, new_s in c_replacements:
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

print(f"\nTotal files updated: {total_updated} / {len(target_files)}, Total Category C replacements: {total_changes}")
