import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = r"d:\Web Novel\UNIVERSE B\New"

def apply_patch(filename, old_str, new_str):
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if old_str not in content:
        print(f"[FAIL] In {filename}: Target string not found:\n{old_str[:70]}...")
        return False
    content = content.replace(old_str, new_str, 1)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[SUCCESS] Patched {filename}")
    return True

# 1. 08_Character_Roster.md - Admiral Silas at line 1605
apply_patch(
    "08_Character_Roster.md",
    "Admiral Silas and Renzo Vance.",
    "Lord Admiral Suhotra and Renzo Vance."
)

# 2. 14_High_Council.md - Header Status and Authority
apply_patch(
    "14_High_Council.md",
    "**Status:** [CANON LOCK] Official Canonical Specification of Tier 1 Governance, Parliamentary Law & Ideological Warfare (October 2026)",
    "**Status:** [CANON LOCK] Official Canonical Specification of Tier 2 Governance, Parliamentary Law & Ideological Warfare (October 2026)"
)
apply_patch(
    "14_High_Council.md",
    "**Authority:** Universe B च्या सर्वोच्च संसदीय व्यवस्थेची (High Council Realm / The High Council Rotunda (सभा-लोक)),",
    "**Authority:** Universe B च्या Tier 2 सर्वोच्च संसदीय व्यवस्थेची (The High Council Rotunda [सभा-लोक] under Indra-Upādhi),"
)

# 14_High_Council.md - Sections 1.5 and 1.6
target_14_sec1 = """परंतु ज्या क्षणी चर्चेत विषय येतो: *"Tier 4 च्या प्रभावामुळे १०,००० आत्म्यांचे चक्र थांबले आहे"*, किंवा *"Hastinapur मध्ये अर्ध-रिक्त (Ardha-Rikta) बहु-वैश्विक आत्मे आले आहेत"*, किंवा *"Devil Summoning मुळे आत्म्याची काजळी झाली आहे"*...  
  त्याच क्षणी **यमाचे डोळे तीक्ष्णपणे उघडतात**, विधात्याचा धागा थांबतो, आणि चित्रगुप्ताचा सुवर्ण-कलम उचलला जातो. संपूर्ण संसद एका क्षणात शांत होते; कारण प्रत्येकाला ठाऊक आहे की विश्वाचे खरे मालक हे तिघे आहेत, बाकी सर्व केवळ बाह्य पसारा आहे!

---

## 2. Parliamentary Cycles & Session Cadence (कालगणना, सत्रे व बैठकांचे वेळापत्रक)"""

replacement_14_sec1 = """परंतु ज्या क्षणी चर्चेत विषय येतो: *"Tier 4 च्या प्रभावामुळे १०,००० आत्म्यांचे चक्र थांबले आहे"*, किंवा *"Hastinapur मध्ये अर्ध-रिक्त (Ardha-Rikta) बहु-वैश्विक आत्मे आले आहेत"*, किंवा *"Devil Summoning मुळे आत्म्याची काजळी झाली आहे"*...  
  त्याच क्षणी **यमाचे डोळे तीक्ष्णपणे उघडतात**, विधात्याचा धागा थांबतो, आणि चित्रगुप्ताचा सुवर्ण-कलम उचलला जातो. संपूर्ण संसद एका क्षणात शांत होते; कारण प्रत्येकाला ठाऊक आहे की विश्वाचे खरे मालक हे तिघे आहेत, बाकी सर्व केवळ बाह्य पसारा आहे!

### 1.5 The Soul Trinity's Constitutional Dual-Relationship with Indra-Upādhi
- **Metaphysical / Karmic Jurisdiction (सर्वोच्च स्वातंत्र्य):**  
  यम, विधाता आणि चित्रगुप्त हे केवळ Tier 1 मधील सर्वोच्च त्रिमूर्ती आणि दैवी प्रतिनिधींना उत्तरदायी आहेत. **इंद्र-उपाधीला यमाच्या न्यायपीठावर, विधात्याच्या प्राण-सूत्रांवर किंवा चित्रगुप्ताच्या खतावणीवर कोणताही हुकूम किंवा व्हेटो (Veto) चालवण्याचा घटनात्मक अधिकार नाही.**
- **Spatial / Military Jurisdiction (भौतिक संरक्षण):**  
  परंतु आत्मा-प्रशासनाचे प्रत्यक्ष कार्यालय (Soul Administration Complex) Tier 2 Swarga / Setu-Loka मध्ये स्थित असल्याने, त्यांच्या बाह्य सीमांचे रक्षण, दूत-संरक्षण आणि अधोलोक आक्रमणांपासून सुरक्षा पुरवण्याची **सर्वोच्च लष्करी जबाबदारी इंद्र-उपाधीची आहे.**

### 1.6 The Unbroken Cosmic Bridge: High Council to Astral Realm
- **The Macro-to-Civic Hierarchy:**  
  $$\\text{Tier 2 Swarga: High Council (Indra-Upādhi)} \\gg \\text{Tier 3 Astral Realm: The Manu-Upādhi \\& 7 Sovereign Seats}$$
  इंद्र-उपाधी संपूर्ण विश्वाचे लष्करी स्थैर्य व अजगर-कवच सांभाळतात, तर सेंट्रल सिटीमधील **मनू-उपाधी (The Iron Sovereign on the Grey Basalt Throne)** पाचही ग्रह-खंडांमधील नश्वर नागरी कायदे, कर-प्रणाली आणि प्रोव्हिंग गेम्सचे प्रशासन सांभाळतात.

---

## 2. Parliamentary Cycles & Session Cadence (कालगणना, सत्रे व बैठकांचे वेळापत्रक)"""

apply_patch("14_High_Council.md", target_14_sec1, replacement_14_sec1)

# 3. 09_Faction_Politics.md - Garuda Scouts table line
target_09_garuda = "| **Garuda Scouts (गरुड)** | उंच पर्वत शिखरे, एअरशिप टॉवर्स | अति-उंच भरारी, दुर्बिणीसारखी तीक्ष्ण दृष्टी, हवेतील शिकार | *Sky Recon Wing*; Blimp Escort Squadrons | महा-प्राकारावर हवाई गस्त घालणे; टपाल विमानांना आणि पक्षांना हवेत सुरक्षा पुरवणे. | Order of Palaks (हवाई टेहळणी), Seekers (भेगांचा शोध). |"
replacement_09_garuda = "| **Garuda Scouts (गरुड)** | उंच पर्वत शिखरे, गरुड-बुरुज | अति-उंच भरारी, दुर्बिणीसारखी तीक्ष्ण दृष्टी, हवेतील शिकार | *Sky Recon Wing*; गरुड-रक्षक पथके | महा-प्राकारावर हवाई गस्त घालणे; आकाशीय संदेशवाहकांना आणि प्रवाशांना हवेत सुरक्षा पुरवणे. | Order of Palaks (हवाई टेहळणी), Seekers (भेगांचा शोध). |"
apply_patch("09_Faction_Politics.md", target_09_garuda, replacement_09_garuda)

# 09_Faction_Politics.md - Node 1 & Section 5.2 update
target_09_node = """                  [ 1. CENTRAL BANK & CONCORD ENFORCERS ]
                         (The Central Reserve Bank (Akash-Kosha) / Currency Core)"""
replacement_09_node = """              [ 1. THE MANU-UPĀDHI & 7 SOVEREIGN SEATS ]
                (Central City Grey Basalt Throne / Beatrice Rosso / Currency Core)"""
apply_patch("09_Faction_Politics.md", target_09_node, replacement_09_node)

target_09_bank_desc = """1. **Central Bank (The Central Reserve Bank (Akash-Kosha)) & Concord Enforcers:**
   - *शक्ती:* चलनावरील मक्तेदारी (Aether-Rupee), आंतर-क्षेत्रीय महा-द्वार व व्यापारी परवाने, मंत्र-शिला नियंत्रण आणि Concord Audit Bureau चे सशस्त्र छापे."""
replacement_09_bank_desc = """1. **The Manu-Upādhi & 7 Sovereign Seats (Central City & Akash-Kosha Bank):**
   - *सर्वोच्च सत्ता:* **मनू-उपाधी (The Iron Sovereign on the Grey Basalt Throne)** आणि ७ सार्वभौम आसने (ज्यात Seat #1 High Arbitrator Beatrice Rosso चलन, कर्ज व १७% सीमा-शुल्क नियंत्रित करतात).
   - *घटनात्मक दुवा:* $\\text{Tier 2 High Council (Indra-Upādhi)} \\gg \\text{Tier 3 Central City (Manu-Upādhi)}$.
   - *शक्ती:* चलनावरील मक्तेदारी (Aether-Rupee), आंतर-क्षेत्रीय महा-द्वार व व्यापारी परवाने, मंत्र-शिला नियंत्रण आणि Concord Audit Bureau चे सशस्त्र छापे."""
apply_patch("09_Faction_Politics.md", target_09_bank_desc, replacement_09_bank_desc)

# 4. 11_Astral_Society.md
apply_patch(
    "11_Astral_Society.md",
    "• १ रात्र: विमान-मंच जवळील डॉर्मिटरी लाकडी कॉट                 ──► २ Copper Mashas (CM)",
    "• १ रात्र: रथ-मंच जवळील डॉर्मिटरी लाकडी कॉट                   ──► २ Copper Mashas (CM)"
)
apply_patch(
    "11_Astral_Society.md",
    "• व्यापारी काफिला जकात शुल्क (Caravan Gateway Toll प्रति माल-विमान) ──► ८ Silver Panas (SP)",
    "• व्यापारी काफिला जकात शुल्क (Caravan Gateway Toll प्रति माल-रथ)   ──► ८ Silver Panas (SP)"
)
apply_patch(
    "11_Astral_Society.md",
    "High Governor Ambika यांच्या हाताखालील **The Central Reserve Bank (The Vaults of Truth / The Central Reserve Bank (Akash-Kosha))**",
    "High Arbitrator Beatrice Rosso (दॉना बीट्रिस रोसो) यांच्या हाताखालील **The Central Reserve Bank (The Vaults of Truth / The Central Reserve Bank (Akash-Kosha))**"
)

# 5. 13_Races_and_Clans.md
apply_patch(
    "13_Races_and_Clans.md",
    "असुरांनी उच्च-दाब लाव्हा-भट्ट्या, अवजड रनिक बॅलिस्टा आणि अभेद्य विमानांचे चिलखत घडवले.",
    "असुरांनी उच्च-दाब लाव्हा-भट्ट्या, अवजड रनिक बॅलिस्टा आणि अभेद्य रथांचे व तटांचे चिलखत घडवले."
)

# 6. 16_The_Proving_Games.md - Adho-Rangashala
target_16_adho = """### 1.2 Point Qualification & The Official Combat License (पॉईंट्स लेजर व रिंगण परवाना)"""
replacement_16_adho = """### 1.2 The Subterranean Feeder: Adho-Rangashala (अधो-रंगशाळा — Atala Ceiling Black-Sand Feeder Pits)
- **स्थान व वातावरण:** Central City च्या थेट खाली, अतला (Atala Stratum — Patala Layer 1) च्या काळ्या बेसॉल्ट छतावर कोरलेले क्रूर व गुप्त आखाडे.
- **काळी नेक्रोटिक शून्य-वाळू (Necrotic Void-Sand):** या रिंगणातील वाळू मृत शरीरांच्या रक्ताने आणि व्हॉइड-राखेने काळी पडलेली असते. येथे लागलेल्या जखमा आपोआप भरत नाहीत किंवा गोठत नाहीत; उच्च गती-घर्षण (Kinetic Friction) किंवा तात्काळ अपान दाह-शमनाशिवाय (Apāna Thermal Flush) रक्तस्राव थांबत नाही.
- **कॅनन संदर्भ:** **नील (Neel) च्या प्रारंभिक लढाया (Chapters 2–5) याच अधो-रंगशाळेत सुरू होतात.** येथे कपटी सावकार, भ्रष्ट पंच, तस्कर केलेले प्रेता-गाभे (Preta-Cores) आणि नग्न हातांनी होणाऱ्या बेअर-नकल (Bare-Knuckle) लढाया चालतात.

### 1.3 Point Qualification & The Official Combat License (पॉईंट्स लेजर व रिंगण परवाना)"""
apply_patch("16_The_Proving_Games.md", target_16_adho, replacement_16_adho)

# 16_The_Proving_Games.md - Fortress-Breaker cap
target_16_cap = """*Arena Prowess ≠ Cosmic Survival:* आखाड्यातील १ विरुद्ध १ च्या नियंत्रित लढाईत जिंकणारा प्रत्येक वीर Tier 4 च्या अवकाशीय पोकळीत तग धरू शकत नाही. तेथे कोणतीही सुवर्ण-दोरी नसते; तिथे केवळ सर्वस्व खाऊन टाकणारा काळा धूर असतो. त्यामुळे केवळ १०-१५% मानसिक कणखर वीरच तिकडे टिकतात.

---

## 4. Insane Weapon & Power System Diversity (Tensura + Dhanurveda + Alien Magitech)"""

replacement_16_cap = """*Arena Prowess ≠ Cosmic Survival:* आखाड्यातील १ विरुद्ध १ च्या नियंत्रित लढाईत जिंकणारा प्रत्येक वीर Tier 4 च्या अवकाशीय पोकळीत तग धरू शकत नाही. तेथे कोणतीही सुवर्ण-दोरी नसते; तिथे केवळ सर्वस्व खाऊन टाकणारा काळा धूर असतो. त्यामुळे केवळ १०-१५% मानसिक कणखर वीरच तिकडे टिकतात.

### 3.1 The Fortress-Breaker Scale Cap (दुर्ग-भंजक मर्यादा)
- **Tier 3 Astral Realm Scale Ceiling:**  
  सेंट्रल सिटी आणि संपूर्ण पाच ग्रह-खंडांमध्ये S-Rank साधकांची महा-विनाशक शक्ती **दुर्ग-भंजक पातळीवर (Fortress-Destroyer Scale)** नैसर्गिकरित्या मर्यादित (Capped) आहे.
- **Tectonic Bedrock Dampening:** सेंट्रल सिटीचा आधारभूत काळा बेसॉल्ट आणि टेक्टॉनिक चक्र-लंगर इतका प्रचंड प्राण-भार शोषून घेतात की कोणताही S-Rank योद्धा अनिर्बंध खंड-विनाशक (Continent-Shattering) किंवा विश्व-विध्वंसक स्फोट घडवू शकत नाही. लढाया केवळ किल्ल्यांच्या तटबंद्या, पर्वतांचे कडे किंवा संपूर्ण आखाड्याचे भूप्रदेश उद्ध्वस्त करण्याइतपतच मर्यादित राहतात.

---

## 4. Insane Weapon & Power System Diversity (Tensura + Dhanurveda + Alien Magitech)"""
apply_patch("16_The_Proving_Games.md", target_16_cap, replacement_16_cap)

# 16_The_Proving_Games.md - Rotary Shadow Anchor & Seal 6 Acoustic Dampening Field
target_16_rotary = """Central Coliseum चा १२०-टन ग्रॅनाइट आखाडा स्थिर नसतो; जमिनीखालील **५,०००-टन असुरी हायड्रॉलिक जॅक्स (Hydraulic Aether-Pneumatic Jacks)** व **Tectonic Rotary Anchor System** द्वारे दर फेरीला मैदान बदलते:"""
replacement_16_rotary = """Central Coliseum चा १२०-टन ग्रॅनाइट आखाडा स्थिर नसतो; जमिनीखालील **५,०००-टन असुरी हायड्रॉलिक जॅक्स (Hydraulic Aether-Pneumatic Jacks)** व **Tectonic Rotary Shadow Anchor System** द्वारे दर फेरीला मैदान बदलते.

### 5.1 The Seal 6 Rotary Acoustic Dampening Field (१०,०००+ प्रेक्षक प्राण-ध्वनि):
- **The Core Metaphysical Engine:**  
  सेंट्रल कोलिझियम हे केवळ मनोरंजनाचे मैदान नसून विश्वाचे एक **अत्यावश्यक आध्यात्मिक नियंत्रण यंत्र (Metaphysical Containment Engine)** आहे!
- कोलिझियममध्ये बसलेल्या १,००,००० प्रेक्षकांच्या उत्साही आरोळ्या, टाळ्या आणि सामूहिक गतीज प्राण (Kinetic Prana) चक्र-लंगरावरून थेट सेंट्रल सिटीच्या मुळाशी झिरपतात.
- हा महाकाय ध्वनी-कंपन थेट **सील ६ (Prana-Shunyata / शून्य-खिंडार)** च्या विनाशी कंपनांना तंतोतंत निष्प्रभ (Counter-Resonance Acoustic Dampening) करतो, ज्यामुळे सेंट्रल सिटीच्या पोटातील सूक्ष्म-भेगा (Micro-Rifts) कायमस्वरूपी दाबून ठेवल्या जातात!"""
apply_patch("16_The_Proving_Games.md", target_16_rotary, replacement_16_rotary)

print("Precision patches finished!")
