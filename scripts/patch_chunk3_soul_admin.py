import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r'd:\Web Novel\UNIVERSE B\New\04_Soul_Administration.md'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Section 1 lead text to position Soul Trinity in Tier 2 Buffer Zone / Swarga High Council
old_sec1_lead = '''ही तीन पदे Divine High Council Realm (The High Council Rotunda (सभा-लोक)) मध्ये स्वायत्त घटनात्मक **Upadhis** म्हणून बसतात. त्यांच्यात **कोणताही स्वार्थ किंवा भ्रष्टाचार नसतो** आणि ती Divine Delegates (Prajapati, Narada, Rudra) पासून पूर्णपणे स्वतंत्र आहेत.'''

new_sec1_lead = '''ही तीन पदे Tier 2 (The Buffer Zone / Swarga) मधील **High Council Soul Precinct (सभा-लोक / आत्मा-प्रशासन विभाग)** मध्ये स्वायत्त घटनात्मक **Upadhis** म्हणून बसतात. त्यांच्यात **कोणताही स्वार्थ किंवा भ्रष्टाचार नसतो** आणि आत्म्यांच्या न्यायनिवाड्यामध्ये ती कोणाच्याही दबावाखाली येत नाहीत.'''

assert old_sec1_lead in text, 'old_sec1_lead not found'
text = text.replace(old_sec1_lead, new_sec1_lead, 1)

# 2. Add Section 1.4: Dual Relationship with Indra-Upadhi
target_after_sec1 = '''- **घटनात्मक कारण:** एकाधिकारशाही आणि पक्षपात रोखण्यासाठी ही सत्ता विभागणी केलेली आहे. कोणतीही एक व्यक्ती एकाच वेळी परवाना देणे, नशीब लिहिणे आणि आयडी देणे अशी तिन्ही कामे करू शकत नाही.

---'''

replacement_after_sec1 = '''- **घटनात्मक कारण:** एकाधिकारशाही आणि पक्षपात रोखण्यासाठी ही सत्ता विभागणी केलेली आहे. कोणतीही एक व्यक्ती एकाच वेळी परवाना देणे, नशीब लिहिणे आणि आयडी देणे अशी तिन्ही कामे करू शकत नाही.

### 1.4 Constitutional Dual-Relationship with Indra-Upādhi (इंद्र-उपाधीशी दुहेरी घटनात्मक संबंध) [CANON LOCK]
आत्मा-प्रशासन त्रिमूर्ती (Yama, Vidhātā, Chitragupta) आणि Tier 2 Buffer Zone चे प्रशासकीय प्रमुख **Indra-Upādhi** यांच्यातील संबंध खालील दोन लोखंडी घटनात्मक तत्त्वांवर आधारित आहेत:
1. **Judicial Independence (न्यायिक व कर्म स्वायत्तता — ०% हस्तक्षेप):**
   - Indra-Upādhi कडे आत्म्यांच्या कर्माचे ऑडिट, नरक/स्वर्ग वाटप, नशिबाचे लेखन (Destiny Architecture), किंवा Soul ID निर्मितीमध्ये **कोणताही थेट आदेश देण्याचा किंवा बदल करण्याचा अधिकार शून्य (0%) आहे**.
   - आत्म्यांच्या न्यायाबाबत ही त्रिमूर्ती थेट Tier 1 मधील **सर्वोच्च त्रिमूर्ती (Brahma, Vishnu, Shiva)** आणि **Divine Delegates (Prajapati, Narada, Rudra-Ansha)** यांना उत्तरदायी आहे. इंद्र त्यांच्या न्यायालयीन निर्णयात हस्तक्षेप करू शकत नाही.
2. **Territorial Security & Physical Sanctuary (भौतिक सुरक्षा, अभय व अंमलबजावणी):**
   - परंतु, Soul Precinct, Pratigraha गोदाम, आणि Dvāra Gate हे Tier 2 (The Buffer Zone / Swarga) च्या प्रादेशिक हद्दीत वसलेले असल्याने, **त्यांच्या कार्यालयांची सुरक्षा, कर्मचाऱ्यांचे संरक्षण, दूत-वाहनांची सुरक्षा (White Couriers Escort), आणि आदेशांची भौतिक अंमलबजावणी ही Indra-Upādhi आणि Buffer Zone च्या सेनेच्या (Setu-Mahasena) थेट अखत्यारीत येते**.
   - थोडक्यात: **"Indra protects the Sanctuary; the Trinity governs the Soul."**

---'''

assert target_after_sec1 in text, 'target_after_sec1 not found'
text = text.replace(target_after_sec1, replacement_after_sec1, 1)

# 3. Add Kshira Sagara Singularity Apex routing in Section 3
target_sec3 = '''### 3.0 Pre-Stage — Collection & Two-Yama Handover [CANON LOCK]

प्रत्येक विश्वाचा स्वतःचा यम असतो. Universe B चा विधाता दुसऱ्या विश्वातून आत्मा **चोरत नाही** — तो त्या विश्वाच्या यमाकडे अधिकृत विनंती करतो.'''

replacement_sec3 = '''### 3.0 Pre-Stage — Collection, Kshira Sagara Singularity Routing & Two-Yama Handover [CANON LOCK]

> [!IMPORTANT]
> **Kshira Sagara: The Sole Primordial IN/OUT Gate (विश्वाचा मूळ उगम):**  
> क्षीर सागर हा साधा समुद्र नसून संपूर्ण विश्वाचा **Cosmic Singularity Apex** आहे. इतर विश्वांतून येणाऱ्या प्रत्येक अधिकृत आत्म्याला (Route A) प्रथम क्षीर सागराच्या शुद्ध चैतन्य-प्रवाहात स्नान करूनच Universe B मध्ये प्रवेश मिळतो. तिथूनच विधाता त्या आत्म्यांना Tier 2 मधील Dvāra Gate / Pratigraha गोदामात कायदेशीरपणे टेलिपोर्ट करतो. (याउलट Route B मधील अनपेक्षित आत्म्यांना ही सिंग्युलॅरिटी भेदताना प्रचंड दाबाचा सामना करावा लागतो; ज्यामध्ये Neel ने भगवान गर्भोदकशायी विष्णूंची वैश्विक परीक्षा उत्तीर्ण करून स्वतःचे मूळ शरीर राखले).

प्रत्येक विश्वाचा स्वतःचा यम असतो. Universe B चा विधाता दुसऱ्या विश्वातून आत्मा **चोरत नाही** — तो त्या विश्वाच्या यमाकडे अधिकृत विनंती करतो.'''

assert target_sec3 in text, 'target_sec3 not found'
text = text.replace(target_sec3, replacement_sec3, 1)

# 4. Standardize Dual-Register terms in text (Jivatma / Preta)
text = text.replace('Devils चा आत्मा summon करू शकतात', 'Pretas (slang: Devils) चा आत्मा summon करू शकतात')
text = text.replace('Rogue Devils', 'Rogue Pretas (Devils)')

# Verify no 'नहीं' with bindi
assert 'नहीं' not in text, "Found banned 'नहीं' with bindi!"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('SUCCESS: UNIVERSE B/New/04_Soul_Administration.md patched cleanly!')
