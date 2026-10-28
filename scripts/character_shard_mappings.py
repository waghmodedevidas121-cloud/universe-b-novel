import sys
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Character Shard & Vanguard Mapping Table
# Keys: Canonical ID (e.g., 'CHR-HUM-01')
# Values: (shard_field, vanguard_field)

MAPPINGS = {
    # --- 1. HUMAN SUB-REALM (CHR-HUM-01 to CHR-HUM-15) ---
    "CHR-HUM-01": (
        "Human Planetary Shard (मानव ग्रह-खंड) | Hastinapura (हस्तिनापूर) | ६०–७०% कणखर नश्वर (Baseline Resilient Mortal Sovereign)",
        "Vanguard Registration: N/A (Crown Commander-in-Chief / Civil Administration) | सहजीवी बंध: शून्य (अ-साधक नश्वर)"
    ),
    "CHR-HUM-02": (
        "Human Planetary Shard (मानव ग्रह-खंड) | Hastinapura (हस्तिनापूर) | ६०–७०% कणखर नश्वर (Baseline Resilient Mortal Reformer)",
        "Vanguard Registration: N/A (Imperial Patron of Medicine & Education) | सहजीवी बंध: शून्य"
    ),
    "CHR-HUM-03": (
        "Human Planetary Shard (मानव ग्रह-खंड) | Hastinapura Garrison | Top ५% Awoken High-Human (Awoken Kshatriya Marshal)",
        "Apex S-Rank Vanguard Field Commander | सहजीवी बंध: Gale Stallion (वायू-अश्व) गती व रणनीतिक स्प्रिंट"
    ),
    "CHR-HUM-04": (
        "Human Planetary Shard (मानव ग्रह-खंड) | Frontline Trench Brigade | Top ५% Awoken High-Human (Heavy Vanguard Prince)",
        "A-Rank Vanguard Vanguard Leader | सहजीवी बंध: Ironclad Boar (वज्र-वराह) जड चिलखत व भू-कंपन प्रतिकार"
    ),
    "CHR-HUM-05": (
        "Human Planetary Shard (मानव ग्रह-खंड) | Hastinapura Imperial Chancery | ६०–७०% कणखर नश्वर (Baseline Resilient Diplomatic Jurist)",
        "Vanguard Registration: N/A (Imperial Prime Minister & Civil Law Custodian) | सहजीवी बंध: शून्य"
    ),
    "CHR-HUM-06": (
        "Human Planetary Shard (मानव ग्रह-खंड) | Hastinapura Heavy Locomotive Works | ७०–९५% (~२५%) Anchor-Tuner & Rail Engineer (Dimensional Engineer)",
        "Vanguard Registration: N/A (State Rail Locomotive & Aether-Car Chief Architect) | सहजीवी बंध: शून्य"
    ),
    "CHR-HUM-07": (
        "Human Planetary Shard (मानव ग्रह-खंड) | Kuru Foundry District | ६०–७०% कणखर नश्वर (Baseline Resilient Foundry Director)",
        "Vanguard Registration: N/A (Industrial Labor & Coal Foundry Director) | सहजीवी बंध: शून्य"
    ),
    "CHR-HUM-08": (
        "Human Planetary Shard (मानव ग्रह-खंड) | The Sea Citadel (समुद्र-पत्तनम) | ६०–७०% कणखर नश्वर (Baseline Resilient Merchant Admiral)",
        "Vanguard Registration: N/A (High Admiral & Clandestine Sea Anchor Syndicate Patron) | सहजीवी बंध: शून्य"
    ),
    "CHR-HUM-09": (
        "Human Planetary Shard (मानव ग्रह-खंड) | The Sea Citadel Naval Fleet | ६०–७०% कणखर नश्वर (Baseline Resilient Naval Commodore)",
        "B-Rank Vanguard (Naval Auxiliary Coastal Patrol) | सहजीवी बंध: शून्य (वज्र-पोलादी नौदल तोफखाना)"
    ),
    "CHR-HUM-10": (
        "Human Planetary Shard (मानव ग्रह-खंड) | Coastal Merchant Convoys | ७०–९५% (~२५%) Dimensional Navigator (Spatial Helmswoman)",
        "Vanguard Registration: N/A (Sea Citadel Merchant Fleet Pilot) | सहजीवी बंध: शून्य"
    ),
    "CHR-HUM-11": (
        "Human Planetary Shard (मानव ग्रह-खंड) | Sea Citadel Abyssal Salvage Docks | ६०–७०% कणखर नश्वर (Baseline Resilient Abyssal Diver)",
        "C-Rank Vanguard (Underwater Reconnaissance Auxiliary) | सहजीवी बंध: शून्य (न्युमॅटिक डायव्हिंग सूट)"
    ),
    "CHR-HUM-12": (
        "Human Planetary Shard (मानव ग्रह-खंड) | The Sea Citadel Deep Waters | Top ५% Awoken High-Human (Awoken Harpooner & Privateer)",
        "B-Rank Vanguard Scout (Marine Auxiliary) | सहजीवी बंध: मकर-शिशू (Makara-Shishu / River Drake) जल-प्रवाह व नौका-ओढ बंध"
    ),
    "CHR-HUM-13": (
        "Human Planetary Shard (मानव ग्रह-खंड) | Tapovana Hermitage (तपोवन) | Top ५% Awoken High-Human (Vedic Nadi Ascetic)",
        "Vanguard Registration: N/A (Tapovana Ahimsa Hermit & Forest Sage) | सहजीवी बंध: अरण्य-अहिंसा मैत्री"
    ),
    "CHR-HUM-14": (
        "Human Planetary Shard (मानव ग्रह-खंड) | Tapovana to Central City | Top ५% Awoken High-Human (Awoken Peacemaker Diplomat)",
        "Vanguard Registration: Special Diplomatic Envoy to Grand Concord | सहजीवी बंध: शून्य"
    ),
    "CHR-HUM-15": (
        "Human Planetary Shard (मानव ग्रह-खंड) | Hastinapura Imperial Archives | ६०–७०% कणखर नश्वर (Baseline Resilient Archival Scholar)",
        "Vanguard Registration: N/A (Imperial Library Scholar & Document Conservator) | सहजीवी बंध: शून्य"
    ),

    # --- 2. ASURA SUB-REALM (CHR-ASU-01 to CHR-ASU-15) ---
    "CHR-ASU-01": (
        "Asura Planetary Shard (असुर ग्रह-खंड — The Iron Citadel / वज्र-नगर) | १५% जास्त गुरुत्वाकर्षण | ३०–४०% Combatant Elite",
        "Vanguard Registration: N/A (Grand Architect & Ancient Magma Foundry Founder) | सहजीवी बंध: पाषाण-यंत्र संरेखन"
    ),
    "CHR-ASU-02": (
        "Asura Planetary Shard (असुर ग्रह-खंड — The Iron Citadel) | १५% जास्त गुरुत्वाकर्षण | ३०–४०% Combatant Elite",
        "Vanguard Registration: N/A (Foundry League Sovereign & High Metallurgist Queen) | सहजीवी बंध: शून्य"
    ),
    "CHR-ASU-03": (
        "Asura Planetary Shard (असुर ग्रह-खंड — Heavy Siege Redoubt) | १५% जास्त गुरुत्वाकर्षण | ३०–४०% Combatant Elite",
        "Apex S-Rank Vanguard Champion (Heavy Siege Marshal) | सहजीवी बंध: Magma Tiger (ज्वाला-शार्दूल) थर्मिट चिलखत व भू-कंपन स्फोट"
    ),
    "CHR-ASU-04": (
        "Asura Planetary Shard (असुर ग्रह-खंड — Caldron Bastion) | १५% जास्त गुरुत्वाकर्षण | ३०–४०% Combatant Elite",
        "A-Rank Vanguard Brawler (Shock Assault General) | सहजीवी बंध: Thunder Bear (अशनी-भल्लूक) ऊर्जा-विस्तार व धक्का-शमन"
    ),
    "CHR-ASU-05": (
        "Asura Planetary Shard (असुर ग्रह-खंड — The Obsidian Chasm / शैल-गाढा) | १५% जास्त गुरुत्वाकर्षण | ३०–४०% Combatant Elite",
        "Vanguard Registration: N/A (Mining Baroness & Coal Oligarch) | सहजीवी बंध: शून्य (खाण कामगार सिंडिकेट)"
    ),
    "CHR-ASU-06": (
        "Asura Planetary Shard (असुर ग्रह-खंड — Lower Foundry Chasm) | १५% जास्त गुरुत्वाकर्षण | ३०–४०% Combatant Elite",
        "Vanguard Registration: N/A (Blast-Furnace Smelter Baron) | सहजीवी बंध: शून्य"
    ),
    "CHR-ASU-07": (
        "Asura Planetary Shard (असुर ग्रह-खंड — Smelting Caldera) | १५% जास्त गुरुत्वाकर्षण | ५०–६०% Simple Utility (भट्टी व्यवस्थापन)",
        "Vanguard Registration: N/A (Blast-Furnace Logistics Overseer) | सहजीवी बंध: शून्य"
    ),
    "CHR-ASU-08": (
        "Asura Planetary Shard (असुर ग्रह-खंड — Steam Valve Core) | १५% जास्त गुरुत्वाकर्षण | ५०–६०% Simple Utility (वाफ-दाब तंत्रज्ञ)",
        "Vanguard Registration: N/A (High-Pressure Steam Technician) | सहजीवी बंध: शून्य"
    ),
    "CHR-ASU-09": (
        "Asura Planetary Shard (असुर ग्रह-खंड — Red Crucible Labor Sector) | १५% जास्त गुरुत्वाकर्षण | ३०–४०% Combatant Elite",
        "A-Rank Vanguard Saboteur (Red Crucible Labor Commander) | सहजीवी बंध: Flame Viper (अग्नि-सर्प) स्टीम कॉन्ड्युइट गुप्तता व उष्णता-शोषण"
    ),
    "CHR-ASU-10": (
        "Asura Planetary Shard (असुर ग्रह-खंड — West Trench Perimeter) | १५% जास्त गुरुत्वाकर्षण | ३०–४०% Combatant Elite",
        "A-Rank Vanguard Juggernaut (Bunker-Breaker Commander) | सहजीवी बंध: Iron Bison (वज्र-महिष) टेक्टॉनिक धडक व भिंत-भंजन"
    ),
    "CHR-ASU-11": (
        "Asura Planetary Shard (असुर ग्रह-खंड — Gear-Cutting Foundry) | १५% जास्त गुरुत्वाकर्षण | ५०–६०% Simple Utility (यांत्रिकी कारागीर)",
        "Vanguard Registration: N/A (Precision Gear & Valve Artisan) | सहजीवी बंध: शून्य"
    ),
    "CHR-ASU-12": (
        "Asura Planetary Shard (असुर ग्रह-खंड — Subterranean Chasm Vaults) | १५% जास्त गुरुत्वाकर्षण | ५०–६०% Simple Utility (लंगर अनुनादक)",
        "Vanguard Registration: N/A (Clandestine Shadow-Anchor Resonance Tuner) | सहजीवी बंध: शून्य"
    ),
    "CHR-ASU-13": (
        "Asura Planetary Shard (असुर ग्रह-खंड — Miner Health Infirmary) | १५% जास्त गुरुत्वाकर्षण | ५०–६०% Simple Utility (कामगार रुग्णालय प्रमुख)",
        "Vanguard Registration: N/A (Refinery Labor Clinic Matron) | सहजीवी बंध: शून्य"
    ),
    "CHR-ASU-14": (
        "Asura Planetary Shard (असुर ग्रह-खंड — Deep Obsidian Caverns) | १५% जास्त गुरुत्वाकर्षण | ३०–४०% Combatant Elite",
        "Dormant Legendary Vanguard Rank (प्राचीन सुप्त योद्धा) | सहजीवी बंध: प्रागैतिहासिक पाषाण-निद्रा"
    ),
    "CHR-ASU-15": (
        "Asura Planetary Shard (असुर ग्रह-खंड — Basalt Quarry Pit) | १५% जास्त गुरुत्वाकर्षण | ५०–६०% Simple Utility (दगडी कामगार)",
        "Vanguard Registration: N/A (Quarry Laborer & Stone Mason) | सहजीवी बंध: शून्य"
    ),

    # --- 3. DEVA SUB-REALM (CHR-DEV-01 to CHR-DEV-10) ---
    "CHR-DEV-01": (
        "Deva Planetary Shard (देव ग्रह-खंड — Amaravati / अमरावती) | १००% शून्य-धुराडे कायदा, सौर ऊर्जा | ३०–४०% Solar Elite",
        "Vanguard Registration: N/A (Solar Imperial Sovereign & Celestial Throne Head) | सहजीवी बंध: शून्य"
    ),
    "CHR-DEV-02": (
        "Deva Planetary Shard (देव ग्रह-खंड — Amaravati Prismatic Spire) | १००% शून्य-धुराडे कायदा | ३०–४०% Solar Elite",
        "Vanguard Registration: N/A (Prismatic Sun Council Matron) | सहजीवी बंध: शून्य"
    ),
    "CHR-DEV-03": (
        "Deva Planetary Shard (देव ग्रह-खंड — High Cloud Bastion) | १००% शून्य-धुराडे कायदा | ३०–४०% Solar Elite",
        "Apex S-Rank Vanguard Aerial Ace (Sky Garrison Commander) | सहजीवी बंध: सूर्य-सिंह (Surya-Simha / Solar Gryphon) हायपरसॉनिक प्लाझ्मा व अवकाशीय गस्त"
    ),
    "CHR-DEV-04": (
        "Deva Planetary Shard (देव ग्रह-खंड — Solar Spire Array) | १००% शून्य-धुराडे कायदा | ३०–४०% Solar Elite",
        "Apex S-Rank Vanguard Sun-Breaker (Solar Strike Marshal) | सहजीवी बंध: मरुत-श्येन (Maruta-Shyen / Gale Falcon) ऑप्टिक किरण अडवणूक व वेग-भेद"
    ),
    "CHR-DEV-05": (
        "Deva Planetary Shard (देव ग्रह-खंड — Celestial High Court) | १००% शून्य-धुराडे कायदा | ३०–४०% Solar Elite",
        "Vanguard Registration: N/A (Celestial Court Chief Justice & Solar Arbiter) | सहजीवी बंध: शून्य"
    ),
    "CHR-DEV-06": (
        "Deva Planetary Shard (देव ग्रह-खंड — Solar Lunar Observatory) | १००% शून्य-धुराडे कायदा | ५०–६०% Celestial Service (सौर-शीत औषधशास्त्र)",
        "Vanguard Registration: N/A (Solar Observatory Priestess & Alchemist) | सहजीवी बंध: शून्य"
    ),
    "CHR-DEV-07": (
        "Deva Planetary Shard (देव ग्रह-खंड — Gandharva-Puri / गंधर्व-पुरी) | १००% शून्य-धुराडे कायदा | ५०–६०% Celestial Service (ध्वनी-कलाकार)",
        "Vanguard Registration: N/A (Gandharva Aesthetic Envoy & Sound Artisan) | सहजीवी बंध: शून्य"
    ),
    "CHR-DEV-08": (
        "Deva Planetary Shard (देव ग्रह-खंड — Crystal Spun Workshops) | १००% शून्य-धुराडे कायदा | ५०–६०% Celestial Service (रेशीम विणकर)",
        "Vanguard Registration: N/A (Aether-Silk Master Weaver) | सहजीवी बंध: शून्य"
    ),
    "CHR-DEV-09": (
        "Deva Planetary Shard (देव ग्रह-खंड — Perimeter Floating Outposts) | १००% शून्य-धुराडे कायदा | ३०–४०% Solar Elite",
        "Deva Sky-Fleet Navigator (Direct Celestial Accord Cadre) | सहजीवी बंध: शून्य (देवांना आखाडा व श्वापद-बंध निषिद्ध)"
    ),
    "CHR-DEV-10": (
        "Deva Planetary Shard (देव ग्रह-खंड — Sky Route Terminals) | १००% शून्य-धुराडे कायदा | ५०–६०% Celestial Service (आकाशीय संदेशवाहक)",
        "Celestial Courier Auxiliary (Direct Celestial Accord Cadre) | सहजीवी बंध: शून्य (देवांना आखाडा व श्वापद-बंध निषिद्ध)"
    ),

    # --- 4. BEAST SUB-REALM (CHR-BST-01 to CHR-BST-08) ---
    "CHR-BST-01": (
        "Beast Planetary Shard (श्वापद ग्रह-खंड — The Primeval Canopy, महा-कांतार) | सचेतन सार्वभौम श्वापद-नागरिक (Conscious Sovereign Beast-Folk)",
        "Central League High Sovereign Patron (अग्रगण्य संरक्षक) | सहजीवी बंध: आदिम भू-नाडी अधिष्ठान (स्वेच्छा-सहजीवन प्रणेता)"
    ),
    "CHR-BST-02": (
        "Beast Planetary Shard (श्वापद ग्रह-खंड — Subterranean Rainforest Riverways) | सचेतन सार्वभौम श्वापद-नागरिक (Conscious Sovereign Naga Empress)",
        "Sovereign Naga Empress of Deep Waterways | सहजीवी बंध: कल्पवृक्ष मूळ-जल संतुलन (अ-मानवी सार्वभौम)"
    ),
    "CHR-BST-03": (
        "Beast Planetary Shard (श्वापद ग्रह-खंड — Granite Sky Spires / पक्षी-शैल) | सचेतन सार्वभौम श्वापद-नागरिक (Conscious Sovereign Garuda Empress)",
        "Central Proving Grounds Grand Aerial Patron | सहजीवी बंध: उच्च-आकाशीय वादळ संतुलन (सार्वभौम गरुड सम्राज्ञी)"
    ),
    "CHR-BST-04": (
        "Beast Planetary Shard (श्वापद ग्रह-खंड — High Crag Aerie) | सचेतन सार्वभौम श्वापद-नागरिक (Conscious Sovereign Garuda Prince)",
        "Apex S-Rank Vanguard Beast Sovereign Emissary | सहजीवी बंध: सहजीवी आकाशीय गरुड-सैन्य नेतृत्व"
    ),
    "CHR-BST-05": (
        "Beast Planetary Shard (श्वापद ग्रह-खंड — Twilight Marsh Canopy) | सचेतन सार्वभौम श्वापद-नागरिक (Conscious Sovereign Shadow-Panther Matriarch)",
        "Sovereign Twilight Woods Sentinel | सहजीवी बंध: अरण्य-छाया नाडी संरेखन (छाया-व्याघ्र कुलमाता)"
    ),
    "CHR-BST-06": (
        "Beast Planetary Shard (श्वापद ग्रह-खंड — Sacred Glade) | सचेतन सार्वभौम श्वापद-नागरिक (Conscious Sovereign Stag Shaman Queen)",
        "Sovereign Forest Medical & Seed Custodian | सहजीवी बंध: वनस्पती-प्राण संवर्धन (मृग-शामन सम्राज्ञी)"
    ),
    "CHR-BST-07": (
        "Beast Planetary Shard (श्वापद ग्रह-खंड — Mire Fungal Swamps) | सचेतन सार्वभौम श्वापद-नागरिक (Conscious Sovereign Swamp Shaman)",
        "Sovereign Fungal Medicine Alchemist | सहजीवी बंध: दलदल-बुरशी व विष-शमन विद्या"
    ),
    "CHR-BST-08": (
        "Beast Planetary Shard (श्वापद ग्रह-खंड — Ahimsa Valley Sanctuary) | सचेतन सार्वभौम श्वापद-नागरिक (Conscious Sovereign Elephant Sage)",
        "Sovereign Ahimsa Sanctuary Guardian (अभय-आश्रम ऋषी) | सहजीवी बंध: १००% अ-हिंसा प्राण-वलय"
    ),

    # --- 5. CENTRAL SUB-REALM (CHR-CEN-01 to CHR-CEN-08) ---
    "CHR-CEN-01": (
        "Central Sub-Realm (मध्यवर्ती ग्रह-खंड) | Central City (मध्य-नगर) — ५०,००० चौ. मैल तटस्थ भूमी | Grand Concord Head",
        "Vanguard Registration: Grand Concord Diplomatic Head & Supreme League Patron | सहजीवी बंध: शून्य (तटस्थ मुत्सद्दी)"
    ),
    "CHR-CEN-02": (
        "Central Sub-Realm (मध्यवर्ती ग्रह-खंड) | Central City — The Central Reserve Bank (The Vaults of Truth / The Central Reserve Bank (Akash-Kosha)) | महा चलन-विनिमय नियंत्रक",
        "Vanguard Registration: N/A (Central Bank Governor & League Purse Regulator) | सहजीवी बंध: शून्य"
    ),
    "CHR-CEN-03": (
        "Central Sub-Realm (मध्यवर्ती ग्रह-खंड) | Central City — Neutral Peacekeeper Garrison & Grand Proving Grounds",
        "Supreme Commander of Peacekeeper Vanguard & Proving Grounds Chief Enforcer | सहजीवी बंध: शून्य (अ-प्राणघातक शांतिरक्षक सैन्यदल)"
    ),
    "CHR-CEN-04": (
        "Central Sub-Realm (मध्यवर्ती ग्रह-खंड) | Central City — Concord Judicial Palace",
        "Vanguard Registration: Central Proving Grounds & Inter-Realm Duel Chief Jurist | सहजीवी बंध: शून्य"
    ),
    "CHR-CEN-05": (
        "Central Sub-Realm (मध्यवर्ती ग्रह-खंड) | Central City — Concord Special Audit Bureau",
        "Concord Special Audit Bureau Commander & Rogue Anchor Hunter (ब्यूरो प्रमुख) | सहजीवी बंध: शून्य (लंगर-छापेप्रमुख)"
    ),
    "CHR-CEN-06": (
        "Central Sub-Realm (मध्यवर्ती ग्रह-खंड) | Central City — Central Telegraph Switching Hub",
        "Grand Telegraph Network Director & League Score Broadcaster | सहजीवी बंध: शून्य (तार-गिल्डमास्टर)"
    ),
    "CHR-CEN-07": (
        "Central Sub-Realm (मध्यवर्ती ग्रह-खंड) | Central City — Central Switchboard Complex",
        "Senior Telegraph Operator & Live Match Dispatcher | सहजीवी बंध: शून्य"
    ),
    "CHR-CEN-08": (
        "Central Sub-Realm (मध्यवर्ती ग्रह-खंड) | Central City — Grand Concord Library & Archives",
        "Grand Archivist & Vanguard Ranking Records Custodian | सहजीवी बंध: शून्य (अभिलेख रक्षक)"
    ),

    # --- 6. TIER 2 BUFFER ZONE & SAGES (CHR-SET-01 to CHR-SET-17) ---
    "CHR-SET-01": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | The Setu Academy (सेतु विद्या-पीठ) — ५०,००० मैल तरंगता पाषाण-सेतू",
        "Vanguard Registration: N/A (Vidyapeeth Rector & Esoteric Nadi-Bond Theorist) | सहजीवी बंध: शून्य (ऋषी-शिक्षण)"
    ),
    "CHR-SET-02": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Setu High-Speed Rail Terminal",
        "Vanguard Registration: N/A (Setu High-Speed Rail & Pressure Transit Master) | सहजीवी बंध: शून्य"
    ),
    "CHR-SET-03": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Void Wall Fortress & Western Watchtower",
        "Void Wall Fortress Commandant & Perimeter Sentinel | सहजीवी बंध: शून्य (तटबंदी संरक्षक)"
    ),
    "CHR-SET-04": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Buffer Zone Mobile Audit Unit",
        "Senior Field Auditor & Corruption Inspector | सहजीवी बंध: शून्य (ऋषी खतावणी परीक्षक)"
    ),
    "CHR-SET-05": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | The Setu Standing Army Grand Command (The Setu Standing Army (Setu Mahā-Senā)) & The Grand Aegis Vanguard",
        "Supreme Commander of The Setu Standing Army (Setu Mahā-Senā) & Grand Aegis Vanguard | Secret Pipeline Inductor (व्हॅनगार्ड महा-सेतू गुप्त भरती प्रमुख) | सहजीवी बंध: इंद्राचे अस्त्र-अनुष्ठान"
    ),
    "CHR-SET-06": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Setu Discovery Guild & Ruin Examination Bureau",
        "Discovery Guild Director & Ruin Crypt Examiner (पुरातन यंत्र परीक्षक) | सहजीवी बंध: शून्य"
    ),
    "CHR-SET-07": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Setu Medical & Agricultural Rejuvenation Grounds",
        "Agricultural & Nadi Regeneration Sage (कृषी-नाडी कुलगुरू) | सहजीवी बंध: संजीवनी औषध-बंध"
    ),
    "CHR-SET-08": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Rishi Council Ledger Verification Chambers",
        "Senior Archival Auditor & Karmic Timestamp Examiner | सहजीवी बंध: शून्य"
    ),
    "CHR-SET-09": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Sub-Dimensional Rift Monitoring Post",
        "Rift Telemetry Officer & Void Wave Tracker | सहजीवी बंध: शून्य"
    ),
    "CHR-SET-10": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Setu Citadel Central Bastion",
        "Fortress Bastion Sentinel & Heavy Defense Warden | सहजीवी बंध: शून्य"
    ),
    "CHR-SET-11": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Frontier Patrol Squad Alpha",
        "Border Reconnaissance Officer (सीमांत टेहळणी अधिकारी) | सहजीवी बंध: शून्य"
    ),
    "CHR-SET-12": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Setu Clockwork & Gauge Maintenance Foundry",
        "Setu Master Clockmaker & Mechanical Gauge Inspector | सहजीवी बंध: शून्य"
    ),
    "CHR-SET-13": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Void Beacon Lighthouse Array",
        "Void Beacon Watchman & Spatial Horizon Signaler | सहजीवी बंध: शून्य"
    ),
    "CHR-SET-14": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Buffer Zone Law Enforcement Directorate",
        "Setu Military Police Provost Marshal (शिस्तपालन सेनानी) | सहजीवी बंध: शून्य"
    ),
    "CHR-SET-15": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Grand Aegis Frontline Trench Wall",
        "Grand Aegis Wall Warden & Corrupted Boundary Guard (महा-भिंत रक्षक) | सहजीवी बंध: शून्य"
    ),
    "CHR-SET-16": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Vidyapeeth Scribe Office",
        "Chief Archival Scribe & Treaty Protocol Recorder | सहजीवी बंध: शून्य"
    ),
    "CHR-SET-17": (
        "Tier 2 Buffer Zone (द ग्रेट सेतू) | Inter-Tier Courier Post",
        "Buffer Zone High-Priority Courier Officer (द्रुतगती संदेशवाहक) | सहजीवी बंध: शून्य"
    ),

    # --- 7. TIER 4 CORRUPTED REALM (CHR-ABY-01 to CHR-ABY-08) ---
    "CHR-ABY-01": (
        "Tier 4 Corrupted Realm (अधो-लोक) | Netherhome (नेदरहोम) — ३०% तुटलेला भूभाग पलीकडे Grand Aegis",
        "Threat Vector: Class-Omega Threat Vector (Devil Sovereign) | सहजीवी बंध: विकृत पिशाच-गुलामगिरी"
    ),
    "CHR-ABY-02": (
        "Tier 4 Corrupted Realm (अधो-लोक) | Dread-Hold Iron Foundry",
        "Threat Vector: Vector 1 & 2 Siege Architect (Fiend Ballistics General) | सहजीवी बंध: शून्य"
    ),
    "CHR-ABY-03": (
        "Tier 4 Corrupted Realm (अधो-लोक) | Shadow-Hollow Acid Vats",
        "Threat Vector: Flesh-Weaver Alchemist & Toxic Miasma Cult Architect | सहजीवी बंध: शून्य"
    ),
    "CHR-ABY-04": (
        "Tier 4 Corrupted Realm (अधो-लोक) | Abyssal March Wasteland",
        "Threat Vector: Outlaw Raid Commander (Southern Breach Vector) | सहजीवी बंध: शून्य"
    ),
    "CHR-ABY-05": (
        "Tier 4 Corrupted Realm (अधो-लोक) | Abyssal March Wasteland",
        "Threat Vector: Outlaw Vanguard Striker (Southern Breach Vector) | सहजीवी बंध: शून्य"
    ),
    "CHR-ABY-06": (
        "Tier 4 Corrupted Realm (अधो-लोक) | Rust Haven (भ्रष्ट निर्वासित बाजार)",
        "Threat Vector: Vector 3 Outlaw King (Grand Aegis Scrap Smuggler & Contraband Boss) | सहजीवी बंध: शून्य"
    ),
    "CHR-ABY-07": (
        "Tier 4 Corrupted Realm (अधो-लोक) | Corrupted Shrine of the Broken Spire",
        "Threat Vector: Corrupted Divine Weapon Bearer (High Bounty Outlaw) | सहजीवी बंध: शून्य"
    ),
    "CHR-ABY-08": (
        "Tier 4 Corrupted Realm (अधो-लोक) | The Sunken Crypt of the Seventh Seal",
        "Threat Vector: Ancient Nether Strategist & Rift Breach Mastermind | सहजीवी बंध: शून्य"
    ),

    # --- 8. TIER 1 HIGH COUNCIL & PRIMORDIALS (CHR-DIV-01 to CHR-DIV-13) ---
    "CHR-DIV-01": (
        "Tier 1 Primordial Apex (परम-धाम) | Singularity Apex — क्षीर सागर (Kshira Sagara) उगम",
        "Universal Function: Cosmic Creator (Zero-Direct-Avatar Mandate) | सहजीवी बंध: आदिम चैतन्य स्रोत"
    ),
    "CHR-DIV-02": (
        "Tier 1 Primordial Apex (परम-धाम) | Singularity Apex — क्षीर सागर व अनंत-शेष शय्या",
        "Universal Function: Cosmic Preserver & All-Soul Spiritual Energy Source | सहजीवी बंध: सहस्र-फणी अनंत आधार"
    ),
    "CHR-DIV-03": (
        "Tier 1 Primordial Apex (परम-धाम) | Singularity Apex — महा-संहार व पुनरुज्जीवन गाभा",
        "Universal Function: Cosmic Dissolver (Zero-Direct-Avatar Mandate) | सहजीवी बंध: शून्य (अनादि-अनंत विलय)"
    ),
    "CHR-DIV-04": (
        "Singularity Apex Foundation | Ananta-Shesha Read-Only System Core",
        "Universal Function: Immutable Read-Only Database & Space-Time Stabilizer | सहजीवी बंध: शून्य"
    ),
    "CHR-DIV-05": (
        "Tier 1 High Council Realm | Dharmaraja Court — मृत्यु व कर्म-निवाड्याचे सर्वोच्च न्यायालय",
        "Constitutional Upadhi: First Justice of Karmic Adjudication | सहजीवी बंध: शून्य"
    ),
    "CHR-DIV-06": (
        "Tier 1 High Council Realm | Prana-Sutra Weaving Sanctum",
        "Constitutional Upadhi: Soul-Thread Architect (प्राण-सूत्र शिल्पकार) | सहजीवी बंध: शून्य"
    ),
    "CHR-DIV-07": (
        "Tier 1 High Council Realm | The Grand Hall of Ledgers (The Root Archive / The Grand Hall of Ledgers (The Root Archive / The Grand Hall of Ledgers (Maha-Lekha)-Bhavana))",
        "Constitutional Upadhi: Universal Grand Scribe (महा-लेखक) | सहजीवी बंध: शून्य"
    ),
    "CHR-DIV-08": (
        "Tier 1 High Council Realm | Pan-Astral Defense & Aegis Command",
        "Constitutional Upadhi: Supreme Commander of Pan-Astral Defense | सहजीवी बंध: शून्य"
    ),
    "CHR-DIV-09": (
        "Tier 1 High Council Realm | Forensic Audit & Inviolable Inquiry Chamber",
        "Constitutional Upadhi: Chief Auditor of Cosmic Order & Truth | सहजीवी बंध: शून्य"
    ),
    "CHR-DIV-10": (
        "Tier 1 High Council Realm | Dimensional Physics & Evolution Sanctum",
        "Constitutional Upadhi: Master of Dimensional Engineering & Evolution Testing | सहजीवी बंध: शून्य"
    ),
    "CHR-DIV-11": (
        "Tier 1 High Council Realm | Brahma-Sanctum & Structural Integrity Bureau",
        "Divine Envoy: Plenipotentiary of Lord Brahma | सहजीवी बंध: शून्य"
    ),
    "CHR-DIV-12": (
        "Tier 1 High Council Realm | Cosmic Diplomatic Envoy Bureau",
        "Divine Envoy: Plenipotentiary of Lord Vishnu | सहजीवी बंध: शून्य"
    ),
    "CHR-DIV-13": (
        "Tier 1 High Council Realm & Tier 4 Containment Dead-Zone",
        "Divine Envoy: Operational Ansha of Shiva | सहजीवी बंध: शून्य"
    ),

    # --- 9. THE ALIENS DIASPORA (CHR-ALN-01 to CHR-ALN-06) ---
    "CHR-ALN-01": (
        "Human Planetary Shard (मानव ग्रह-खंड) | Hastinapura (कुरु-एलियन वसाहत / Alien Borough) | The Aliens Diaspora (५% विस्थापित वंशज / ३री पिढी)",
        "Vanguard Registration: N/A (Fourth Estate / नागरी पत्रकार व मुद्रण संचालक) | सहजीवी बंध: शून्य (नश्वर तांत्रिक ज्ञान व मुद्रण यंत्रणा)"
    ),
    "CHR-ALN-02": (
        "Central Astral Realm (मध्य-क्षेत्र) | Central City (आकाश-कोश बँकिंग संकुल / Grand Concord) | The Aliens Diaspora (रोसो फायनान्शियल डायनेस्टी)",
        "Vanguard Registration: N/A (High Financial Comptroller / Sovereign Debt Arbiter) | सहजीवी बंध: शून्य (नश्वर आर्थिक बुद्धिमत्ता)"
    ),
    "CHR-ALN-03": (
        "Asura Planetary Shard (असुर ग्रह-खंड) | The Iron Citadel (Red Crucible आर्सेनल) | The Aliens Diaspora (शस्त्रास्त्र व धातूशास्त्र तंत्रज्ञ)",
        "Vanguard Registration: N/A (Grand Technical Ordnance Director) | सहजीवी बंध: शून्य (कडक भौतिकशास्त्र व धातू अभियांत्रिकी)"
    ),
    "CHR-ALN-04": (
        "Deva Sub-Realm (देव उप-लोक) | Amaravati (Hall of Solar Refraction) | The Aliens Diaspora (प्रिझमॅटिक ऑप्टिक्स व सूर्य-अभ्यासक)",
        "Vanguard Registration: N/A (Deva Court Scholar & Solar Optics Theorist) | सहजीवी बंध: शून्य (अप्राकृतिक देव-अमृताचा लाभांश नाकारणारा)"
    ),
    "CHR-ALN-05": (
        "Tier 4 Corrupted Realm (अधो-लोक सीमांत) | Rust Haven (Scrap Spire & Slum Sump) | The Aliens Diaspora (हद्दपार भूमिगत सिंडिकेट)",
        "Clandestine Fixer / Outlaw Broker (Unregistered) | सहजीवी बंध: शून्य (ध्वनिक-इलेक्ट्रॉनिक जॅमर्स व मेकॅनिकल गियर)"
    ),
    "CHR-ALN-06": (
        "Human Shard / Setu Buffer Border (खड्डा क्र. १३ स्क्रॅप यार्ड / Kuru Railway Frontier) | The Aliens Diaspora (21st-Century Mortal Drifter — Fresh Arrival)",
        "Unregistered Refugee / Mechanical Apprentice | सहजीवी बंध: शून्य (कोणताही गेम HUD नाही, कोणतीही दैवी शक्ती नाही, १००% नश्वर)"
    ),
}

print(f"Total MAPPINGS configured: {len(MAPPINGS)}")
assert len(MAPPINGS) == 100, f"Expected 100 mappings, got {len(MAPPINGS)}"
print("ALL 100 MAPPINGS VERIFIED!")
