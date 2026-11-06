import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
f1 = os.path.join(project_root, "New", "12_Historical_Annals.md")
f2 = os.path.join(project_root, "New", "01_Cosmology_and_Realms", "08_Chronological_Four_Eras_Deep_Historical_Annals.md")

with open(f1, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Section 3.1 & 3.2
old_s3 = """### 3.1 The Great Sundering: Five Isolated Pocket Dimensions
युग २ च्या संकटातून वाचल्यानंतर प्रजातींमध्ये संसाधनांवरून भीषण संघर्ष सुरू झाला:
- देवांचे अमर शरीर आणि मानवांची नश्वर जैविक मर्यादा एकत्र राहू शकत नव्हती. असुरांच्या भट्ट्यांचे धूर देवांना सहन होत नव्हते.
- **The Dimensional Split:** त्रिमूर्तीच्या नियमांनुसार आणि ऋषींच्या सल्ल्याने, Tier 3 चे **पाच स्वतंत्र Pocket-Dimensions मध्ये विभाजन करण्यात आले**:
  1. *Deva Sub-Realm (उत्तर):* तरंगती ढगांची पठारे (Amaravati).
  2. *Asura Sub-Realm (पश्चिम):* भूमिगत मॅग्मा फाउंड्रीज (The Iron Citadel).
  3. *Beast Sub-Realm (दक्षिण):* १००,००० मैलांचे आदिम अरण्य (The Primeval Canopy).
  4. *Human Sub-Realm (पूर्व):* नश्वर पाळणा (Hastinapur & The Sea Citadel).
  5. *Central City (मध्य):* निःशस्त्रीकृत तटस्थ केंद्र.
- **The Aetheric Spatial Void:** या उप-लोकांच्या दरम्यान एक प्राणघातक अवकाशीय पोकळी निर्माण करण्यात आली, ज्यामुळे पायी चालत किंवा साध्या जहाजाने एका लोकातून दुसऱ्या लोकात जाणे अशक्य झाले.

### 3.2 The Grand Concord & The Prana-Bandhana Accord
युद्धाची शक्यता संपवण्यासाठी सर्व सत्तांनी सेंट्रल सिटी येथे **The Grand Concord** हा ऐतिहासिक करार केला:
1. **Central City Demilitarization:** मध्यवर्ती शहरात कोणत्याही सत्तेला सैन्य ठेवण्यास बंदी घालण्यात आली.
2. **Akash-Kosha Central Bank:** युद्धांना आळा घालण्यासाठी सर्व आंतरराष्ट्रीय व्यापार Central City च्या 'एथर-रुपया' चलनातून करण्याचे ठरले.
3. **The Prāṇa-Bandhana Accord:** श्वापद लोकांशी शांतता राखण्यासाठी वन्य प्राण्यांची शिकार, गुलामगिरी किंवा पिंजऱ्यात बंद करणे कायद्याने मृत्युदंडाचा गुन्हा ठरवण्यात आला. मानवांशी केवळ संमतीने आध्यात्मिक बंध (Soul Bond) करण्याची मुभा देण्यात आली."""

new_s3 = """### 3.1 The Great Sundering: Five Floating Planetary Shards (पाच तरंगते ग्रह-तुकडे)
युग २ च्या संकटातून वाचल्यानंतर प्रजातींमध्ये संसाधनांवरून भीषण संघर्ष सुरू झाला:
- देवांचे अमर प्रकाशमय शरीर आणि मानवांची नश्वर जैविक मर्यादा एकत्र राहू शकत नव्हती. असुरांच्या भट्ट्यांचे ५०० psi वाफेचे धूर आणि लाव्हा-उष्णता मानवी शहरे उद्ध्वस्त करत होती.
- **The Planetary Shard Cleaving (ग्रह-खंड विच्छेदन):** त्रिमूर्तीच्या नियमांनुसार आणि ऋषींच्या सल्ल्याने, अखंड भूमीचे **पाच स्वतंत्र तरंगत्या ग्रह-तुकड्यांमध्ये (Five Floating Planetary Shards — Grah-Khanda)** विभाजन करण्यात आले. प्रत्येकाचे स्वतंत्र गुरुत्वाकर्षण, क्षितिज आणि हवामान आहे:
  1. *Deva Planetary Shard (उत्तर):* तरंगती स्फटिक पठारे (Amaravati), १००% शून्य-धुराडे कायदा, सौर ऊर्जा. लोकसंख्या: ५०–६०% आकाशीय सेवा व संवर्धन; ३०–४०% सौर योद्धे व अर्काॅन.
  2. *Asura Planetary Shard (पश्चिम):* १५% जास्त गुरुत्वाकर्षण, लाव्हा नद्या व बेसाल्ट फाउंड्रीज (Vajra-Nagara, The Iron Citadel). लोकसंख्या: ५०–६०% साधी उपयुक्तता जादू (घरगुती उष्णता, साधी भट्टी); ३०–४०% लढाऊ तंत्रज्ञ व अवजड सैनिक.
  3. *Beast Planetary Shard (दक्षिण):* १००,००० मैलांचे आदिम अरण्य (The Primeval Canopy, महा-कांतार). सचेतन श्वापद-नागरिक (Conscious Sovereign Beast-Folk — वानर, नाग, गरुड नागरिक) आणि अरण्यातील हिंस्त्र वन्य प्राण-श्वापदे.
  4. *Human Planetary Shard (पूर्व):* नश्वर पाळणा (Hastinapura, The Sea Citadel व तपोवन). लोकसंख्या: ९४–९५% सुप्त नश्वर (Slept Mortals — बाहेरील विश्वाचे शून्य ज्ञान, वाफ व कोळशावर चालणारे); ५–६% Awoken साधक/एलिट. १८वे-१९वे शतक वाफेची इंजिने, दगडी कोळशाची धुराडी, मॅन्युअल टेलिग्राफ, .४४ कॅलिबर बोल्ट-ॲक्शन तोफा.
  5. *The Central Sub-Realm & Central City (मध्य):* ५०,००० चौरस मैलांचा पूर्ण तटस्थ मध्यवर्ती ग्रह-तुकडा, निःशस्त्रीकृत जागतिक राजधानी, ग्रँड कॉन्कॉर्ड घुमट व आकाश-कोश मध्यवर्ती बँक.
- **The Infinite Aetheric Void & Monolithic Stone Gateways:** या पाचही ग्रह-तुकड्यांच्या दरम्यान प्राणघातक Infinite Void (अनंत अवकाशीय पोकळी) पसरली आहे, ज्यामुळे अवकाशात पायी चालणे अशक्य झाले. चारही उप-लोकांना केवळ Central City च्या Pancham-Maha-Ghat ला जोडणारी १००-फूट उंच **Monolithic Stone Gateways (महा-तीर्थ द्वारे)** उभारण्यात आली, जी निश्चित प्रहरांच्या मुहूर्ताला उघडतात; त्याशिवाय प्रवास अशक्य आहे. भूमिगत पातळीवर तस्करांचे प्राणघातक Rotary Shadow Anchors कार्यरत आहेत.

### 3.2 The Grand Concord & The Prana-Bandhana Accord
युद्धाची शक्यता संपवण्यासाठी सर्व सत्तांनी सेंट्रल सिटी येथे **The Grand Concord** हा ऐतिहासिक करार केला:
1. **Central City Demilitarization:** मध्यवर्ती शहरात कोणत्याही सत्तेला सैन्य ठेवण्यास बंदी घालण्यात आली.
2. **Akash-Kosha Central Bank:** युद्धांना आळा घालण्यासाठी सर्व आंतरराष्ट्रीय व्यापार Central City च्या 'एथर-रुपया' चलनातून करण्याचे ठरले, ज्यावर ५% ट्रान्झिट फी आकारली जाते.
3. **The Prāṇa-Bandhana Accord with Conscious Beast-Folk:** श्वापद लोकांशी शांतता राखण्यासाठी सचेतन Beast-Folk (वानर, नाग, गरुड) यांना पूर्ण स्वतंत्र नागरिकत्वाचा दर्जा दिला गेला; त्यांची शिकार किंवा गुलामगिरी मृत्युदंडाचा गुन्हा ठरली. अरण्यातील हिंस्त्र वन्य श्वापदांशी (Wild Prana-Beasts) स्वेच्छेने (Consent-based) नाडी-शुद्धी व जलद काया-कोश (Kāyā-Kośa Molting) उत्क्रांतीसाठी *Prāṇa-Bandhana* करण्याची शास्त्रीय पद्धत विकसित झाली."""

if old_s3 in text:
    text = text.replace(old_s3, new_s3)
    print("Replaced Section 3.1 & 3.2 successfully!")
else:
    print("WARNING: Could not find exact old_s3")

# 2. Add Section 4.6 before Section 5
old_s5 = "## 5. Master Comparative Table: Evolution Across the 4 Eras"
new_s46 = """### 4.6 The Vanguard Ranking Board, Prana-Beast League & The Buffer Zone Pipeline
*(सेंट्रल व्हॅनगार्ड लीग, पाच दैनंदिन संकटे व महा-सेतू सैन्याची सर्वोच्च गुप्त भरती)*
- **The Cold War Pressure Valve:** पाचही ग्रह-तुकड्यांमधील थेट युद्धाला आळा घालण्यासाठी Central City मध्ये **The Master Vanguard Ranking Board & Prana-Beast League** चे भव्य क्रीडा आखाडे सुरू करण्यात आले. येथे सर्व उप-लोकांतील ३०–४०% लढाऊ योद्धे आणि मानवी ५–६% Awoken साधक आपल्या सहजीवी वन्य श्वापदांसह (Drakes, Panthers, Boars) रिंगणात उतरतात.
- **माध्यम व जन-संस्कृती:** रोटरी प्रेस वर्तमानपत्रे आणि मॅन्युअल टेलिग्राफद्वारे सामन्यांचे स्कोअर, वीर-रँकिंग आणि चित्रे घराघरांत पोहोचतात. मुलांमध्ये पितळी वीर-पदके (Brass Medals) आणि पोस्टर्सची प्रचंड क्रेझ निर्माण झाली आहे.
- **पाच दैनंदिन संकटे (Five Everyday Threat Vectors):** व्हॅनगार्ड योद्धे केवळ आखाड्यात लढत नाहीत, तर पाच खऱ्या संकटांशी मुकाबला करतात:
  1. *Void Rift Beasts (अंतराळ-श्वापदे):* ग्रह-तुकड्यांच्या मधल्या अवकाशीय पोकळीतून सीमावर्ती खाणींवर किंवा रेल्वे कॉरिडॉर्सवर धडकणारी महाकाय अंतराळ-श्वापदे.
  2. *Rogue Occult Cults (The Hollow Sect):* भूमिगत गुप्त संघटना ज्या बेकायदेशीरपणे Tier 4 मधील पिशाचांचे विषारी मियाझ्मा संसर्ग पसरवतात.
  3. *Void Pirates & Outlaws (आयामी चाचे व बक्षिसे):* व्यापारी जहाजे लुटणाऱ्या बंडखोर असुरी, मानवी व पशू टोळ्या, ज्यांच्यावर सेंट्रल बोर्डकडून मोठी बक्षीस पत्रे (Bounties) निघतात.
  4. *Ancient Crypt Golems (पुरातन युद्ध-यंत्रे):* Era 2 च्या प्रलयात जमिनीखाली गाडलेली २००० वर्षे जुनी भयंकर युद्ध-यंत्रे, जी खाणी खोदताना अचानक जागी होतात.
  5. *Sanctioned Coliseums (अधिकृत द्वंद्वयुद्ध):* जनतेच्या मनोरंजनासाठी आणि रँकिंग गुणांसाठी होणारे आंतर-प्रजातीय औपचारिक द्वंद्वयुद्ध.
- **The Supreme Buffer Zone Pipeline (महा-सेतू भरती पाईपलाईन):** सेंट्रल बोर्डवर लढणाऱ्या ९०% सामान्य वीरांना वाटते की ते केवळ प्रसिद्धी आणि बक्षिसांसाठी लढत आहेत. परंतु प्रत्यक्षात हा बोर्ड **The Great Setu (Buffer Zone) महा-सेनेसाठी सर्वोच्च निवड चाळणी** आहे! जेव्हा एखादा वीर **Apex S-Rank** वर पोहोचतो, तेव्हा त्याला Marshal-General Vajraketu च्या गुप्त निमंत्रणावरून महा-सेतूवर नेऊन विश्वाचे खरे वास्तव दाखवले जाते आणि Grand Aegis च्या खंदकात **Pan-Astral Standing Military Force** चा सर्वोच्च संरक्षक म्हणून तैनात केले जाते!

""" + old_s5

if old_s5 in text and "### 4.6 The Vanguard Ranking Board" not in text:
    text = text.replace(old_s5, new_s46)
    print("Added Section 4.6 successfully!")

# Write to f1 and f2
with open(f1, "w", encoding="utf-8") as f:
    f.write(text)

with open(f2, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Updated {f1} and {f2} successfully!")
