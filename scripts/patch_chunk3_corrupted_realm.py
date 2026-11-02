import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r'd:\Web Novel\UNIVERSE B\New\07_The_Corrupted_Realm.md'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Title & Tags
old_header = '''# 07. Corrupted Realm: Devils, The Grand Aegis & Underworld Soul Mechanics
**File:** `D:\\Web Novel\\New\\07_The_Corrupted_Realm.md`  
**Tags:** `#corrupted-realm #tier-4 #devils #the-grand-aegis #kay-tyag #soul-filter #netherholme #dread-hold #scrap-crawlers #fake-gods #canon-lock`'''

new_header = '''# 07. Tier 4: Adho-Loka / Patala, Pretas, The Spherical Grand Aegis & Underworld Soul Mechanics
**File:** `D:\\Web Novel\\New\\07_The_Corrupted_Realm.md`  
**Tags:** `#patala #tier-4 #adho-loka #pretas #seven-strata #the-grand-aegis #spherical-containment #kay-tyag #soul-filter #fake-gods #canon-lock`'''

assert old_header in text, 'old_header not found'
text = text.replace(old_header, new_header, 1)

# 2. Update Section 0 & Diagram
old_sec0 = '''**The Corrupted Realm (Tier 4 / Tamo Loka)** चे मूळ रहिवासी **कोणतेही साधे जैविक प्राणी, नश्वर मानव किंवा लोककथांमधील राक्षस नाहीत**.'''
new_sec0 = '''**Adho-Loka / Patala (Tier 4 / The Corrupted Realm)** चे मूळ रहिवासी **कोणतेही साधे जैविक प्राणी, नश्वर मानव किंवा लोककथांमधील राक्षस नाहीत**.'''
assert old_sec0 in text, 'old_sec0 not found'
text = text.replace(old_sec0, new_sec0, 1)

old_line16 = '''इथले रहिवासी अधिकृतपणे **Devils (अधो-दैत्य / Corrupted Soul-Lifeforms)** म्हणून वर्गीकृत आहेत—Era 2 मध्ये पुनर्जन्म चक्र तुटल्यामुळे तयार झालेले आध्यात्मिक जीव:'''
new_line16 = '''इथले रहिवासी अधिकृतपणे **Preta (अधो-जीव / विकृत-जीव; street slang: Devils / Fiends)** म्हणून वर्गीकृत आहेत—Era 2 मध्ये पुनर्जन्म चक्र तुटल्यामुळे तयार झालेले आध्यात्मिक जीव:'''
assert old_line16 in text, 'old_line16 not found'
text = text.replace(old_line16, new_line16, 1)

old_diag_line = '[ BOUND BY THE 360° GRAND AEGIS (5,000-MILE SPIRITUAL SHIELD) ]'
new_diag_line = '[ BOUND BY THE 360° SPHERICAL GRAND AEGIS (COSMIC ENERGY SPHERE) ]'
assert old_diag_line in text, 'old_diag_line not found'
text = text.replace(old_diag_line, new_diag_line, 1)

# 3. Update Section 2: Seven Strata of Patala & Purge Western Clichés
old_sec2_table = '''```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       CORRUPTED REALM (THE CORRUPTED ABYSS / TAMO-LOKA)                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. THE SOVEREIGN ABYSS (Native Devils / The Fake Gods)                      │
│    - Netherholme: Obsidian metropolis; seat of Paundraka the Fake God.      │
│    - Dread-Hold: Brutal chthonic fortress ruled by Fiend General Shataghati.│
│    - Shadow-Hollow: Perpetual mist basin ruled by Alchemist Trishira.       │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. THE ASH FORTRESS (Multi-Racial Exiles, Convicts & Scavengers)            │
│    - The Ash Fortress: Rugged border citadel near the Grand Aegis.          │
│    - The Trench Exchange: Clandestine black market for contraband ores.     │
│    - Wardens: Hamsa & Dimbaka (Exiled Wardens), Maricha (Broker).           │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. THE ABYSSAL DEAD ZONE (Impenetrable Cosmic Seals)                        │
│    - The Dead Chasm (Seal 7 Pit / Niraya-Kshetra): Lightless tectonic chasm holding the 7th Cosmic Seal.  │
│    - The Eternal Sentinel: Shrutayudha & Kagabhushundi, The Stone-Eyed Crow (The Stone-Eyed Raven). │
└─────────────────────────────────────────────────────────────────────────────┘
```'''

new_sec2_table = '''```
┌─────────────────────────────────────────────────────────────────────────────┐
│             ADHO-LOKA / PATALA: THE SEVEN SUBTERRANEAN STRATA               │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. ATALA (The Quarantine Trench & Border Breach Zone)                       │
│    - The Ash Fortress: Border citadel near the 360° Spherical Grand Aegis.   │
│    - The Trench Exchange: Clandestine black market for contraband ores.     │
│    - Wardens: Hamsa & Dimbaka (Exiled Wardens), Maricha (Broker).           │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. VITALA (Bloodstone Caverns & Heavy Mineral Sinks)                        │
│    - Subterranean veins of corrosive sulfur and boiling mineral blood.      │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. SUTALA (Ancient Titan Ruins & Asura Sieve Dungeons)                      │
│    - Niraya-Durga: Obsidian stronghold; seat of Paundraka the Fake God.     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. TALATALA (Abyssal Illusion & Acidic Miasma Swamps)                       │
│    - Rasātala Mist Sinks: Perpetual toxic mist basin ruled by Trishira.     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 5. MAHATALA (Serpentine Bone Chasms & Scrap-Behemoth Yards)                 │
│    - Kālakūṭa Basin: Brutal chthonic fortress ruled by Shataghati.          │
├─────────────────────────────────────────────────────────────────────────────┤
│ 6. RASATALA (Molten Lead & Corrosive Slag Trenches)                         │
│    - Subterranean lava channels and heavy armor-melting acid sinks.         │
├─────────────────────────────────────────────────────────────────────────────┤
│ 7. PATALA PROPER (The Primeval Void Rift & The 7 Seals Anchor)              │
│    - The Dead Chasm (Seal 7 Pit / Niraya-Kshetra): Lightless rift anchor.   │
│    - The Eternal Sentinel: Shrutayudha & Kagabhushundi, The Stone-Eyed Crow. │
└─────────────────────────────────────────────────────────────────────────────┘
```'''

assert old_sec2_table in text, 'old_sec2_table not found'
text = text.replace(old_sec2_table, new_sec2_table, 1)

# Purge remaining references to Netherholme, Dread-Hold, Shadow-Hollow
text = text.replace('Netherholme', 'Niraya-Durga')
text = text.replace('Dread-Hold', 'Kālakūṭa Basin')
text = text.replace('Shadow-Hollow', 'Rasātala Mist Sinks')

# 4. Update Section 3: Spherical Grand Aegis (no flat wall / linear miles)
old_sec3_hdr = '## 3. The Grand Aegis: Reverse-Engineered Miniature Kshira-Core & 5,000-Mile Spiritual Barrier'
new_sec3_hdr = '## 3. The Grand Aegis: Reverse-Engineered Miniature Kshira-Core & 360° Spherical Cosmic Barrier'
assert old_sec3_hdr in text, 'old_sec3_hdr not found'
text = text.replace(old_sec3_hdr, new_sec3_hdr, 1)

old_sec3_body = '''1. **Reverse-Engineered Miniature Kshira-Core (पोषक अमृत-गाभा व कॉस्मिक न्याय):**
   - Era 3 च्या महा-ऋषींनी आणि विश्वकर्माने पवित्र क्षीर सागराच्या जीवनदायी तत्त्वाचा अभ्यास करून हे अभेद्य ५,००० मैलांचे सुवर्ण-कवच निर्माण केले.
   - हे केवळ तुरुंग नसून, Era 2 मधील प्रलयात अडकलेल्या आणि रूपांतरित झालेल्या जीवांवर (Devils) कॉस्मिक न्याय व करुणेचा पुरावा आहे. ही भिंत Tier 4 च्या अधोलोकात मंद, निरंतर पोषक प्राण-अमृत (prāṇic nectar) पाझरवत राहते, ज्यामुळे तिथल्या आत्म्यांना भुकेने तडफडावे लागत नाही किंवा अकारण छळ सहन करावा लागत नाही.
2. **The Absolute Physical Crossing Ban (भौतिक ओलांडणीवर १००% बंदी):**
   - **Base Physical Wall:** ३०० फूट उंच रुनिक बेसॉल्ट भिंत.
   - **The High-Frequency Spiritual Shield:** High Council च्या ग्रीडशी जोडलेला ३६०° आभासी सोनेरी ऊर्जा-पडदा.'''

new_sec3_body = '''1. **Reverse-Engineered Miniature Kshira-Core (पोषक अमृत-गाभा व कॉस्मिक न्याय):**
   - Era 3 च्या महा-ऋषींनी आणि विश्वकर्माने पवित्र क्षीर सागराच्या जीवनदायी तत्त्वाचा अभ्यास करून हे अभेद्य **३६०° Spherical Cosmic Barrier (The Grand Aegis)** चे ऊर्जा-कवच निर्माण केले.
   - हे केवळ तुरुंग नसून, Era 2 मधील प्रलयात अडकलेल्या आणि रूपांतरित झालेल्या जीवांवर (Pretas / street slang: Devils) कॉस्मिक न्याय व करुणेचा पुरावा आहे. हे गोलाकार ऊर्जा-कवच Tier 4 च्या अधोलोकात मंद, निरंतर पोषक प्राण-अमृत (prāṇic nectar) पाझरवत राहते, ज्यामुळे तिथल्या आत्म्यांना भुकेने तडफडावे लागत नाही किंवा अकारण छळ सहन करावा लागत नाही.
2. **The Absolute Physical Crossing Ban (भौतिक ओलांडणीवर १००% बंदी):**
   - **The Spherical Containment Geometry:** ही कोणतीही सपाट भिंत किंवा ठरावीक मैलांचे सपाट मोजमाप नसून, संपूर्ण Tier 4 क्षेत्राला चहूबाजूंनी वेढणारा एक विशाल ३६०° ऊर्जा-गोल (Cosmic Energy Sphere) आहे.
   - **The High-Frequency Spiritual Shield:** High Council च्या ग्रीडशी जोडलेला ३६०° आभासी सोनेरी ४३२ Hz ऊर्जा-पडदा.'''

assert old_sec3_body in text, 'old_sec3_body not found'
text = text.replace(old_sec3_body, new_sec3_body, 1)

# Verify no 'नहीं' with bindi
assert 'नहीं' not in text, "Found banned 'नहीं' with bindi!"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('SUCCESS: UNIVERSE B/New/07_The_Corrupted_Realm.md patched cleanly!')
