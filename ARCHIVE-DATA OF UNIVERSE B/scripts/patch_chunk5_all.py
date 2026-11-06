import re

# ==============================================================================
# 1. PATCH New/12_Historical_Annals.md
# ==============================================================================
path_12 = r'd:\Web Novel\UNIVERSE B\New\12_Historical_Annals.md'
with open(path_12, 'r', encoding='utf-8') as f:
    text_12 = f.read()

# 1.1 Purge steam in line 119
old_119 = "असुरांच्या भट्ट्यांचे ५०० psi वाफेचे धूर आणि लाव्हा-उष्णता मानवी शहरे उद्ध्वस्त करत होती."
new_119 = "असुरांच्या महा-भट्ट्यांची लाव्हा-ज्वाला, विषारी सल्फर-धूर आणि प्रचंड उष्णता मानवी शहरे उद्ध्वस्त करत होती."
text_12 = text_12.replace(old_119, new_119)

# 1.2 Purge steam in line 156
old_156 = "मानवांनी आणि असुरांनी कोळशाचा काळा धूर, जुनाट वाफेची धुराडी टाकून देऊन **स्वच्छ आयामी अभियांत्रिकी (Clean Aether-Dimensional Engineering)** विकसित केली:"
new_156 = "मानवांनी आणि असुरांनी कोळशाचा काळा धूर व जुनाट धुराडी टाकून देऊन **स्वच्छ आयामी एथर-अभियांत्रिकी (Clean Aether-Dimensional Engineering)** विकसित केली:"
text_12 = text_12.replace(old_156, new_156)

# 1.3 Purge Lattice-Rails in line 157
old_157 = "- **Lattice-Rails (जाळीदार लोहमार्ग):** लोखंडी रुळांमधून अवकाशीय ताण (Spatial-Tension) वाहतो, ज्यामुळे गाड्या जमिनीवर घर्षण न करता अति-वेगाने चुंबकीय-एथर तरंगांवर (Magnetic Aether Gliding) धावतात."
new_157 = "- **Beast-Caravan Highways & Runic Paved Ways (रनिक महामार्ग व श्वापद-गाड्या):** जमिनीवर घर्षण कमी करणाऱ्या रनिक पाषाण-पट्ट्यांवरून भारवाही श्वापदे (Aether-Beasts) आणि चिलखती गाड्या (Armored Wagons) अंतर-नगरीय मालवाहतूक चालवतात."
text_12 = text_12.replace(old_157, new_157)

# 1.4 Purge guns/cartridges in line 159
old_159 = "- **Resonance Ballistics:** बंदुका कोळशाच्या किंवा काळ्या दारूच्या धुराने नव्हे, तर **Resonance Pin + Spatial Compression Cartridges** द्वारे सुपरसॉनिक गतीने जड कायनेटिक स्पाइक्स डागतात."
new_159 = "- **Resonance Artillery & Dhanurveda (नाद-अस्त्र व धनुर्वेद):** तोफा किंवा काळ्या दारूच्या बंदुका नव्हे, तर **Resonance Ballistas, Runic Longbows व स्फटिक-बाण** द्वारे एकाग्र प्राण-कंपनांनी जड कायनेटिक स्पाइक्स व अग्नि-शलाका डागल्या जातात."
text_12 = text_12.replace(old_159, new_159)

# 1.5 Replace Section 4.2 with True 4-Bracket Magic Pyramid
idx_42_start = text_12.find("### 4.2 The 3-Tier Demographic Architecture")
idx_42_end = text_12.find("### 4.3")
if idx_42_start != -1 and idx_42_end != -1:
    new_sec_42 = """### 4.2 The True 4-Bracket Demographic & Power Architecture (मानवी ४-स्तरीय लोकसंख्या व जादू रचना) [CANON LOCK]
मानवी उप-लोकातील लोकसंख्या ४ नैसर्गिक स्तरांत विभागलेली आहे (प्रत्येकाकडे नैसर्गिक प्राण किंवा जादूची सूक्ष्म ठिणगी असते; कोणीही संपूर्ण शून्य नाही):
1. **Bracket 1: Dormant Quirks & Tier-0 Ember Magic (०% ते ६०% जनता — ६०% बहुसंख्य वर्ग):**
   - शेतकरी, कारागीर, कनिष्ठ कामगार, स्वयंपाकी व सामान्य कष्टकरी नागरिक.
   - **जैविक व प्राण सामर्थ्य:** पृथ्वीवरील मानवांपेक्षा कितीतरी पट कणखर. Ambient Aether मुळे हाडांची लोह-घनता (१५०–२५० किलो वजन उचलणे), २-३ दिवसांत भरणाऱ्या जखमा, आणि स्वयंपाकाची चूल पेटवणे किंवा पाणी शुद्ध करणे यासारखी अगदी सूक्ष्म 'ठिणगी जादू' (Ember Magic / Supta-Quirks). आयुष्य: ७५ ते ९५ वर्षे.
   - **कॉस्मिक जाणीव:** ०% (Tier 1 किंवा वैश्विक बॅकएंडचे शून्य ज्ञान; यांच्यासाठी विश्व म्हणजे ५ तरंगते ग्रह-तुकडे व अनंत शून्य).
2. **Bracket 2: Active Cultivators & D-Rank Combatants (६०% ते ८०% जनता — २०% मध्यम वर्ग):**
   - नगर-रक्षक (City Guards), रनिक लोहार, प्राथमिक सैन्य, आणि स्थानिक आखाडा मल्ल.
   - **जादू व नाडी सामर्थ्य:** सक्रिय D-Rank प्राण-प्रवाह, मूलभूत शस्त्र-कला, ५-१० फुटांवरून प्राण-शॉकवेव्ह फेकणे, आणि पहिल्या ग्रंथीचा (Brahma-Granthi) प्राथमिक स्पर्श.
3. **Bracket 3: Reincarnated Souls & C-Rank Adepts (८०% ते ९०% जनता — १०% कुशल वर्ग):**
   - गिल्डमास्टर्स, लंगर-चालक, व्हॉइड नेव्हिगेटर्स, सीमांत सैनिक आणि बहु-तत्त्व लढवय्ये.
   - **आयामी व आत्मिक सामर्थ्य:** पहिल्या ग्रंथीचा पूर्ण भेद, गतजन्माच्या स्मृतींची सूक्ष्म जोड (Smriti-Shlesha), टेक्टॉनिक चक्र-लंगरांचे (Rotary Anchors) नियंत्रण आणि गुंतागुंतीच्या रनिक व्यूहांची हाताळणी.
4. **Bracket 4: Awoken High-Humans & S-Rank Elites (९०% ते १००% वर्ग — टॉप १०% एलिट्स):**
   - **अनुशासनबद्ध उत्क्रांती (Disciplined Evolution):** कोणताही लॉटरी विजय नाही. कुरु मिलिटरी अकॅडमी आणि तपोवन गुरुकुलांतून वर्षानुवर्षे नाडी-साधना (Nadi-Sandhana) करून ज्यांनी आपल्या काया-कोशाची कात टाकली आहे (Kāyā-Kośa Molting).
   - **वैशिष्ट्ये:** १५० ते २५०+ वर्षे आयुष्य, वज्र-समान शारीरिक घनता, शुद्ध एथर-वाहकता, दुसऱ्या ग्रंथीचा (Vishnu-Granthi) भेद (S-Rank), आणि वन्य श्वापदांशी जोडलेला **Soul-Bond (सहजीवी आत्म-बंध)**.

"""
    text_12 = text_12[:idx_42_start] + new_sec_42 + text_12[idx_42_end:]

# 1.6 Purge airplane industry in line 193
old_193 = "हस्तिनापूरच्या विमान-उद्योगाला वेठीस धरतात"
new_193 = "हस्तिनापूरच्या नौका व श्वापद-व्यापाराला वेठीस धरतात"
text_12 = text_12.replace(old_193, new_193)

# 1.7 Fix trade ratio to 85/15 in line 200
old_200 = "**७०% मालवाहतूक आता भूमिगत लंगरांद्वारे होते**, ज्यामुळे सेंट्रल बँकेचा 'एथर-रुपया' टॅरिफ आणि सीमाशुल्क निष्प्रभ ठरत आहेत."
new_200 = "**८५–९०% अधिकृत अवजड व्यापार** महा-तीर्थ द्वारांमधून (Monolithic Stone Gateways) व श्वापद-तांड्यांतून (Beast Caravans) सेंट्रल बँकेचा १७% जकात भरून चालतो; तर **१०–१५%** अति-मूल्यवान व धोकादायक काळा बाजार (काळी मुद्रा, सुप्त लंगर-चकत्या, अनोंदणीकृत आत्मे) भूमिगत चक्र-लंगरांद्वारे (Rotary Shadow Anchors) चालवला जातो, ज्यामुळे सेंट्रल बँक व संसदेची झोप उडाली आहे."
text_12 = text_12.replace(old_200, new_200)

# 1.8 Purge planes in line 212
old_212 = "त्याला या आयामी अनुनाद, विमाने, धनुर्वेद आणि पैशांच्या जगात पै-पैचा हिशोब करत स्वतःचे अस्तित्व टिकवावे लागेल!"
new_212 = "त्याला या आयामी अनुनाद, पाषाण-रथ, धनुर्वेद आणि पैशांच्या जगात पै-पैचा हिशोब करत स्वतःचे अस्तित्व टिकवावे लागेल!"
text_12 = text_12.replace(old_212, new_212)

# 1.9 Fix S-Rank Crossroads to Vajra-Adesh Conscription
old_srank = """- **The S-Rank Crossroads (द्विविधा मार्ग):** जेव्हा एखादा योद्धा सलग विजय मिळवून **Apex S-Rank** गाठतो, तेव्हा त्याच्यापुढे दोन मार्ग असतात:
  1. *The Arena Tycoon Route (~८५-९०%):* सेंट्रल सिटीमध्ये राहून एका सामन्याचे ५०,००० सुवर्ण-मुद्रा, आलिशान संगमरवरी महाल, कॉर्पोरेट ब्रँडिंग आणि खाजगी आखाडे चालवणे.
  2. *The Cosmic Route (~१०-१५%):* सेतूच्या महा-सेनेचे गुप्त निमंत्रण स्वीकारून Grand Aegis भिंतीवर जाऊन Tier 4 च्या महा-प्रलयाविरुद्ध **Pan-Astral Standing Military Force** चा सर्वोच्च संरक्षक बनणे."""

new_srank = """- **The S-Rank Military Conscription (The Great Draft / वज्र-आदेश लष्करी भरती):** ग्रँड कॉन्कॉर्ड संविधानानुसार जेव्हा एखादा योद्धा सलग विजय मिळवून **Apex S-Rank** गाठतो, तेव्हा त्याला कायद्याने 'Cosmic Strategic Asset' घोषित केले जाते. ही कोणतीही ऐच्छिक किंवा स्वेच्छा निवृत्ती नसून अनिवार्य **वज्र-आदेश (Vajra-Adesh)** असतो:
  1. *Track A (Active Frontline Vanguard):* थेट सेतूच्या महा-सेनेमध्ये (Setu Standing Army) सक्रिय अधिकारी म्हणून रुजू होऊन Grand Aegis भिंतीवर Tier 4 च्या महा-प्रलयाविरुद्ध आघाडीवर लढणे.
  2. *Track B (Imperial Reserve on 1-Hour Recall):* सेंट्रल सिटीत राहून व्यावसायिक सामने किंवा आखाडे चालवण्याची मुभा, परंतु आणीबाणीचा सायरन वाजताच १ तासाच्या आत सेतूवर हजर राहणे सक्तीचे. या आदेशाचे उल्लंघन केल्यास 'Outlaw Brand' मारून सर्व मालमत्ता जप्त केली जाते."""
text_12 = text_12.replace(old_srank, new_srank)

# 1.10 Master table era 4 technology limit update
old_tbl_limit = "| **तंत्रज्ञान मर्यादा** | यांत्रिकीकरण शून्य | यांत्रिकीकरण प्राथमिक | यांत्रिकीकरण सुरू | **बंदुका/तोफा/रेल्वे/कोळसा/वाफ व संगणक/AI/चिप्स पूर्णपणे १००% निषिद्ध** |"
new_tbl_limit = "| **तंत्रज्ञान मर्यादा** | यांत्रिकीकरण शून्य | यांत्रिकीकरण प्राथमिक | यांत्रिकीकरण सुरू | **तोफा/बंदुका/रेल्वे/कोळसा/वाफ व संगणक/AI/चिप्स पूर्णपणे १००% निषिद्ध** |"
text_12 = text_12.replace(old_tbl_limit, new_tbl_limit)

# 1.11 Schwa cleanups
text_12 = text_12.replace('Shrutayudha', 'Shrutayudh')
text_12 = text_12.replace('Shamika', 'Shamik')

with open(path_12, 'w', encoding='utf-8') as f:
    f.write(text_12)
print("12_Historical_Annals.md updated successfully!")


# ==============================================================================
# 2. PATCH New/02_Four_Eras_and_Seals.md
# ==============================================================================
path_02 = r'd:\Web Novel\UNIVERSE B\New\02_Four_Eras_and_Seals.md'
with open(path_02, 'r', encoding='utf-8') as f:
    text_02 = f.read()

# 2.1 Replace tag #steam-aether-age
text_02 = text_02.replace('#steam-aether-age', '#runic-steel-age')

# 2.2 Purge airplanes in line 223
old_02_223 = "- **Deva Shard (सौर स्फटिक व ऑप्टिक्स):** विमाने व बॅरियर्ससाठी स्फटिक पुरवते; Solar Decay रोखण्यासाठी पशूंच्या शीत-औषधांवर अवलंबून."
new_02_223 = "- **Deva Shard (सौर स्फटिक व ऑप्टिक्स):** संरक्षक ऊर्जा-कवचे (Aether Barriers), स्फटिक-दीप आणि प्रकाशीय उपकरणांसाठी स्फटिक पुरवते; Solar Decay रोखण्यासाठी पशूंच्या शीत-औषधांवर अवलंबून."
text_02 = text_02.replace(old_02_223, new_02_223)

# 2.3 Fix trade ratio in line 258
old_02_258 = "- **७०% मालवाहतूक आता भूमिगत लंगरांद्वारे होते**, ज्यामुळे सेंट्रल बँकेचा 'एथर-रुपया' टॅरिफ आणि सीमाशुल्क निष्प्रभ ठरत आहेत."
new_02_258 = "- **८५–९०% अधिकृत अवजड व्यापार** महा-तीर्थ द्वारांमधून (Monolithic Stone Gateways) व श्वापद-तांड्यांतून (Beast Caravans) सेंट्रल बँकेचा १७% जकात भरून चालतो; तर **१०–१५%** अति-मूल्यवान व धोकादायक काळा बाजार (काळी मुद्रा, सुप्त लंगर-चकत्या, अनोंदणीकृत आत्मे) भूमिगत चक्र-लंगरांद्वारे (Rotary Shadow Anchors) चालवला जातो, ज्यामुळे सेंट्रल बँक व संसदेची झोप उडाली आहे."
text_02 = text_02.replace(old_02_258, new_02_258)

# 2.4 Purge airplanes in Seal 3 consequence (line 277)
old_02_277 = "हवेतून गंज पसरून 1,000 मैलांतील सर्व धातू, रनिक शस्त्रे, चिलखते आणि विमाने गंजून नष्ट होणे."
new_02_277 = "हवेतून गंज पसरून 1,000 मैलांतील सर्व धातू, रनिक शस्त्रे, चिलखते आणि पाषाण-यंत्रे गंजून नष्ट होणे."
text_02 = text_02.replace(old_02_277, new_02_277)

# 2.5 Fix Seal 6 location in table (line 280)
old_02_280 = "| **Seal 6** | Central Abyssal Rift Floor | **The Soul-Vacuum (Seal 6 / Prāṇa-Shūnyatā)** |"
new_02_280 = "| **Seal 6** | Central City Subterranean Floor (Beneath Central Coliseum Rotary Shadow Anchor) | **The Soul-Vacuum (Seal 6 / Prāṇa-Shūnyatā)** |"
text_02 = text_02.replace(old_02_280, new_02_280)

# 2.6 Seat Indra-Upadhi in line 291
old_02_291 = "ब्रह्मा, विष्णू, शिव, अनंत, यम, विधाता, चित्रगुप्त (`CHR-DIV-01` ते `CHR-DIV-13`)"
new_02_291 = "ब्रह्मा, विष्णू, शिव, अनंत, यम, विधाता, चित्रगुप्त, इंद्र-उपाधी (`CHR-DIV-01` ते `CHR-DIV-14`)"
text_02 = text_02.replace(old_02_291, new_02_291)

# 2.7 Schwa fixes in line 293
text_02 = text_02.replace('त्रिशिरा (`CHR-ABY-03`)', 'त्रिशिर (`CHR-ABY-03`)')

# 2.8 Clean character names in line 294
old_02_294 = "डोना बीट्राइस रोसो, वुल्फगँग ॲडलर, लुशियन, काइट रेन्झो, लिओ ब्रॅडली (`CHR-ALN-01` ते `CHR-ALN-06`)"
new_02_294 = "डोना बीट्रिस व्हेनेझ्झा, वुल्फगँग ॲडलर, लुशियन, काइट रेन्झो, नील (`CHR-ALN-01` ते `CHR-ALN-06`)"
text_02 = text_02.replace(old_02_294, new_02_294)

# 2.9 Schwa cleanups
text_02 = text_02.replace('Shrutayudha', 'Shrutayudh')

with open(path_02, 'w', encoding='utf-8') as f:
    f.write(text_02)
print("02_Four_Eras_and_Seals.md updated successfully!")


# ==============================================================================
# 3. PATCH New/00_World_Genesis_Prologue.md
# ==============================================================================
path_00 = r'd:\Web Novel\UNIVERSE B\New\00_World_Genesis_Prologue.md'
with open(path_00, 'r', encoding='utf-8') as f:
    text_00 = f.read()

# 3.1 Delineate 4 Tiers of Cosmic Reality in Section III
idx_s3_00 = text_00.find("### III. The Singularity Apex and the Eternal Four")
idx_s4_00 = text_00.find("### IV. The Four Eras: How the World Was Broken")

if idx_s3_00 != -1 and idx_s4_00 != -1:
    new_s3_00 = """### III. The Singularity Apex & The Four Tiers of Reality

At the highest dimensional point of Universe B—the Singularity Apex—lies the **Kṣīra Sāgara**, the Ocean of Milk.

It is not an ocean of salt and water, nor does it possess a sandy shore, a harbor, or a single wooden ship. It is a blinding, living singularity of pure spiritual energy (Caitanya) and primordial Amṛta. Any mortal flesh or steel vessel that touches its core dissolves instantly into pure light. Here, Garbhodakaśāyī Viṣṇu reclines upon Ananta-Śeṣa, the infinite serpentine foundation of reality, and from this fountainhead flows the vital life-force (Prāṇa) that animates every soul across the four tiers of cosmic reality:

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    THE FOUR TIERS OF COSMIC REALITY                        │
├────────────────────────────────────────────────────────────────────────────┤
│ • TIER 1: PARAMA-DHĀMA (THE SINGULARITY APEX & DIVINE HUB)                │
│   Kṣīra Sāgara, Ananta (System Bedrock), Yama (Judge of Circulation),      │
│   Vidhātā (Fate Weaver), Chitragupta (Grand Scribe), Prajāpati, Nārada,    │
│   and Rudra (Śiva's Containment Wrath). Weaponless, read-only administration.│
│                                                                            │
│ • TIER 2: SWARGA & THE GREAT SETU (COSMIC BUFFER ZONE)                     │
│   Enclosed within the 360° Spherical Grand Aegis. Governed by the rotating  │
│   Indra-Upādhi (CHR-DIV-14 / Golden Throne of Heaven) commanding 33 Koti   │
│   celestials and the elite Pan-Astral Setu Standing Army under Setu         │
│   Commander Vajraketu.                                                     │
│                                                                            │
│ • TIER 3: THE ASTRAL REALM (THE FIVE PLANETARY SHARDS & CENTRAL CITY)       │
│   The mortal reality: Deva, Asura, Beast, Human, and Central City Shards.   │
│   Governed constitutionally by the Manu-Upādhi upon the Grey Basalt        │
│   Throne of Central City, presiding over the 7 Sovereign Seats.             │
│                                                                            │
│ • TIER 4: THE CORRUPTED ABYSS / PATALA (THE 30% QUARANTINE ZONE)            │
│   The subterranean horror realm sealed beneath the Grand Aegis, housing    │
│   unindexed Pretas (Devils), mutated beasts, and the Seven Cosmic Seals.   │
└────────────────────────────────────────────────────────────────────────────┘
```

Because the Supreme Trinity vowed never to micro-manage the daily affairs of the world, they established The Eternal Four within the weaponless sanctuary of the High Council Rotunda (Tier 1):

1. **Ananta (The System Core):** The non-living, soulless, incorruptible bedrock of cosmic law. Ananta has no ego, grants no favors, and projects no childish floating blue screens. It is a read-only cosmic ledger and verification engine. When a mortal crosses the threshold of deathly crisis through sheer action (The Crisis Law), Ananta registers the evolution with a single, private acoustic resonance—The World Chime—that rings like a heavy brass bell solely inside the seeker’s own skull (Ājñā Cakra).
2. **Yama (The Sovereign Judge of Circulation):** The eternal Dharmarāja who governs death, karmic audits, and the lawful entry and exit of souls across the cosmic threshold.
3. **Vidhātā (The Architect of Destiny):** Yama’s primordial friend, who spins the Silver Cord (Soul-Thread), binding a reincarnating soul’s subtle body (Sūkṣma-Śarīra) to its physical flesh (Sthūla-Śarīra) and locking in the three to five moral crossroads of its Written Fate.
4. **Chitragupta (The Grand Scribe):** Yama’s inseparable right hand, keeper of the Grand Hall of Ledgers, who indexes every thought, breath, ancestral debt (Pañca-Ṛṇa), and three-fold disposition (Sattva, Rajas, Tamas) into an append-only Soul ID.

Alongside these four eternal pillars sit three rotating constitutional offices—the Mahā-Pālaka (Supreme Guardian of Defense), the Chief Sage (Supreme Inquisitor of Truth), and the Prime Seeker (Master of Dimensional Physics)—watched over by the three plenipotentiary envoys of the Trinity: Prajāpati, Deva-Rṣi Nārada, and Rudra, the sole operational manifestation of Śiva’s containment wrath.

---

"""
    text_00 = text_00[:idx_s3_00] + new_s3_00 + text_00[idx_s4_00:]

# 3.2 Clean up titles & schwa in Section VI
text_00 = text_00.replace('Ulka ("The Red Hammer")', 'Ulka (Mine-Workers\' Union Leader)')
text_00 = text_00.replace('Investigator Devayani ("The Concord Hound")', 'Devayani (Concord Audit Investigator)')
text_00 = text_00.replace('Marshal-General Vajraketu', 'Setu Commander Vajraketu')
text_00 = text_00.replace('Paundraka', 'Paundrak')
text_00 = text_00.replace('Shrutayudha', 'Shrutayudh')

with open(path_00, 'w', encoding='utf-8') as f:
    f.write(text_00)
print("00_World_Genesis_Prologue.md updated successfully!")


# ==============================================================================
# 4. PATCH New/15_Leaderboard_System.md
# ==============================================================================
path_15 = r'd:\Web Novel\UNIVERSE B\New\15_Leaderboard_System.md'
with open(path_15, 'r', encoding='utf-8') as f:
    text_15 = f.read()

idx_s4_15 = text_15.find("## 4. The Vanguard Leaderboard Architecture: The Central Spire")
idx_s5_15 = text_15.find("## 5. Coliseum Adjudication: The Quad-Referee Panel")

if idx_s4_15 != -1 and idx_s5_15 != -1:
    new_s4_15 = """## 4. The Dual Leaderboard Architecture: Guild Billboard vs. Coliseum Spire
*(दुहेरी फलक रचना: प्रांतिक व्हॅनगार्ड गिल्ड फलक विरूद्ध सेंट्रल स्प्लिट-फ्लॅप स्पायर) [CANON LOCK]*

विश्वात वीरांचे मूल्यमापन आणि जनतेचे लक्ष दोन स्वतंत्र, परंतु एकमेकांशी जोडलेल्या प्रणालींद्वारे नियंत्रित केले जाते:

### 4.1 The Pan-Astral Vanguard Billboard (पाचही उप-लोकांमधील गिल्ड महा-फलक)
पाचही ग्रह-तुकड्यांमधील मुख्य शहरांमध्ये (हस्तिनापूर गिल्ड हॉल, वज्र-नगर असुरी बालेकिल्ला, महा-कांतार रेंजर लॉज, सेतू फ्रंटियर पोस्ट आणि सेंट्रल सिटी नोंदणी कार्यालय) **The Pan-Astral Vanguard Billboard** उभारलेले आहेत. हे साहसी वीरांचे अधिकृत कार्यक्षेत्र आहे:
- **कार्यकक्षा:** अवकाशीय शून्य-श्वापदांची शिकार (Void Rift Hunts), पाताळी टोळ्या व चाच्यांवर बक्षीस पत्रे (Bounty Warrants), मौल्यवान खाण मोहिमांचे संरक्षण, आणि आपत्कालीन बचाव कार्य.
- **रँकिंग श्रेणी (Tiered Licensing):**
  - **S-Rank (Apex Champions):** सेतूच्या महा-सेनेसाठी (Setu Standing Army) अनिवार्य **वज्र-आदेश (Vajra-Adesh)** भरतीस पात्र. सुवर्ण-अंकित पितळी बिल्ला (Golden Sun Insignia).
  - **A-Rank (Guardians):** आंतर-लोकीय सीमा रक्षक, स्टेज-३ काया-कोश सहजीवी श्वापद मालक. रुपेरी गरुड बिल्ला (Silver Eagle Insignia).
  - **B-Rank (Vanguards):** रक्षक पथक प्रमुख, नाडी-शुद्धीचे ५०+ तास, २० विजयी मोहिमा. कांस्य खड्ग बिल्ला (Bronze Blade Insignia).
  - **C/D-Rank (Initiates):** नवशिक्या साधक, प्राथमिक आखाडा योद्धे व गस्ती जवान. लोखंडी टोकन (Iron Sector Token).

### 4.2 The Proving Games Split-Flap Spire (सेंट्रल कोलिझियम मॅकॅनिकल महा-टॉवर)
सेंट्रल कोलिझियमच्या भव्य प्रांगणात उभा असलेला २५० फूट उंच, अष्टकोनी पितळी टॉवर म्हणजे **The Split-Flap Spire**:
- **यांत्रिकी रचना (Clockwork Split-Flap Mechanism):** यात ५,००० खेळाडूंचे रँकिंग (Rank #5,000 ते Rank #1 Apex) दर्शवणारे हजारो मेकॅनिकल पितळी फ्लॅपर्स (Split-Flap Plates) बसवलेले आहेत. हे पूर्णपणे भूमिगत चक्र-लंगरांच्या वायवीय दाबावर (Pneumatic Pressure) चालते.
- **आखाड्यातील थेट अपडेट:** रिंगणात सामना संपताच आणि पंच-मंडळाने निकाल जाहीर करताच, प्राण-दाबमापक सुया थरथरतात, हवेचा तीव्र हिसका बसतो आणि स्प्लिट-फ्लॅप चकत्या 'खट-खट-खट' आवाज करत सेकंदात विजेत्याचे नाव व रँक बदलतात!
- **सार्वजनिक क्रेझ:** या स्पायारवर पहिल्या ५० मध्ये येणाऱ्या वीरांच्या नावांची पितळी पदके आणि स्फटिक-चित्रे संपूर्ण विश्वाच्या बाजारपेठांत विकली जातात.

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│                       THE FOUR TIERS OF VANGUARD RANKING                          │
├───────────────────────────────────────────────────────────────────────────────────┤
│ [ S-RANK (APEX CHAMPIONS) ] ──► The Setu Standing Army (वज्र-आदेश भरती) थेट पात्र.│
│ • पात्रता: किमान ३ अवकाशीय रिफ्ट श्वापदांची शिकार किंवा कोलिझियम ग्रँड फायनल विजय.│
│ • ओळख: सुवर्ण-अंकित पितळी बिल्ला (Golden Sun-Inscribed Brass Insignia).           │
├───────────────────────────────────────────────────────────────────────────────────┤
│ [ A-RANK (GUARDIANS) ]      ──► आंतर-लोकीय सीमा रक्षक व हाय-बाउंटी हंटर्स.        │
│ • पात्रता: सहजीवी श्वापदाची पूर्ण काया-कोश (Kāyā-Kośa Stage 3) उत्क्रांती.        │
│ • ओळख: रुपेरी गरुड बिल्ला (Silver Eagle Insignia).                               │
├───────────────────────────────────────────────────────────────────────────────────┤
│ [ B-RANK (VANGUARDS) ]       ──► प्राचीन खनिजे, गुहा व व्यापारी काफिल्यांचे रक्षक. │
│ • पात्रता: नाडी-शुद्धीचे ५०+ तास, प्रमाणित आखाड्यातील २० विजयी द्वंद्वयुद्धे.     │
│ • ओळख: कांस्य खड्ग बिल्ला (Bronze Blade Insignia).                               │
├───────────────────────────────────────────────────────────────────────────────────┤
│ [ C/D-RANK (INITIATES) ]    ──► स्थानिक नवशिक्या साधक व प्राथमिक आखाडा योद्धे.   │
│ • पात्रता: मूलभूत शस्त्र-चाचणी उत्तीर्ण, नोंदणीकृत प्राण-बंधन करार.                │
│ • ओळख: लोखंडी टोकन (Iron Sector Token).                                          │
└───────────────────────────────────────────────────────────────────────────────────┘
```

---

"""
    text_15 = text_15[:idx_s4_15] + new_s4_15 + text_15[idx_s5_15:]

with open(path_15, 'w', encoding='utf-8') as f:
    f.write(text_15)
print("15_Leaderboard_System.md updated successfully!")


# ==============================================================================
# 5. PATCH New/17_Beast_Codex.md
# ==============================================================================
path_17 = r'd:\Web Novel\UNIVERSE B\New\17_Beast_Codex.md'
with open(path_17, 'r', encoding='utf-8') as f:
    text_17 = f.read()

# 5.1 Cross-reference Sheru / Kuro in Dusk-Hound line
old_dh = """**01. [Dusk-Hound Line] (Void / Iron)**
*Progression:* Dusk Scrapper -> Ironclad Hound -> Abyssal Dread-Hound  
*Visual Appearance:* Begins as a lean, waist-high ash-grey hound with serrated gunmetal teeth. At Stage 2, dark iron bone-plates fuse across its skull, spine, and ribs, with shadow-vapor trailing from its paws. At Stage 3 (10 ft long), it transforms into a massive war-wolf encased in interlocking spiked black-iron plates, boasting a secondary split jaw and glowing violet ocular slits."""

new_dh = """**01. [Dusk-Hound Line] (Void / Iron)**
*Progression:* Dusk Scrapper -> Ironclad Hound -> Abyssal Dread-Hound  
*Canonical Companion Cross-Reference:* **Sheru (Official Central Registry: Kuro)**, companion beast to Season 1 Catalyst Neel (CHR-ALN-06), is an anomalous Stage-1 Dusk Scrapper with an injured left ear tip, possessing dense iron-bone jaw resistance and Void-scavenger instincts.
*Visual Appearance:* Begins as a lean, waist-high ash-grey hound with serrated gunmetal teeth. At Stage 2, dark iron bone-plates fuse across its skull, spine, and ribs, with shadow-vapor trailing from its paws. At Stage 3 (10 ft long), it transforms into a massive war-wolf encased in interlocking spiked black-iron plates, boasting a secondary split jaw and glowing violet ocular slits."""

text_17 = text_17.replace(old_dh, new_dh)

# 5.2 Schwa cleanup: Takshaka -> Takshak
text_17 = text_17.replace('Takshaka', 'Takshak')

with open(path_17, 'w', encoding='utf-8') as f:
    f.write(text_17)
print("17_Beast_Codex.md updated successfully!")

print("All Chunk 5 files patched successfully!")
