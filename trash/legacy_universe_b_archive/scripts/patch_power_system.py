import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r'd:\Web Novel\UNIVERSE B\New\03_Power_System.md'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Nadi & Triveni Axis
old_nadi = '''- **प्रगतीचा मार्ग:**
  1. *Nadi-Shuddhi:* प्राणायाम आणि तपोवनातील वनस्पतींच्या काढ्यांनी 72,000 सूक्ष्म नाड्यांची पद्धतशीर स्वच्छता.
  2. *External Amplification & Runic Craft (यंत्रे, धनुर्वेद व रनिक शस्त्रे):* मानवी शरीरात देवांप्रमाणे अमर्याद ऊर्जा साठवता येत नसल्याने, मानव धनुष्य, रनिक पाती आणि मंत्र-शिलांवर रुन्स कोरतात आणि वैदिक तंत्राला आपली बाह्य मज्जासंस्था बनवतात.'''

new_nadi = '''- **प्रगतीचा मार्ग:**
  1. *Vedic & Yogic Metaphysical Framing:*
     - *(साहित्यिक व विश्वात्मक स्पष्टीकरण: Idā, Piṅgalā, Suṣumnā आणि ७२,००० नाड्यांची लढाऊ कार्ये ही पारंपरिक योगशास्त्रातील संकल्पनांचे एक सर्जनशील, काल्पनिक रूपांतरण [Fictional Adaptation] आहेत; त्यांना थेट ऐतिहासिक किंवा धार्मिक वैदिक तथ्य मानले जाऊ नये).*
     - **The Triveṇī Axis (त्रिवेणी लढाऊ अक्ष):**
       - **Idā (इडा - The Lunar Conduit):** डावी बाजू, शीतलता, मानसिक एकाग्रता, संवेदनशीलता आणि शरीराचे तापमान संतुलित ठेवणे. Water आणि Ice चे साधक प्रामुख्याने इडा नाडीचा वापर करतात.
       - **Piṅgalā (पिङ्गला - The Solar Conduit):** उजवी बाजू, उष्णता, गतिज ताण (kinetic stress), घर्षण, चयापचय आणि स्नायूंचा स्फोटक वापर. Fire, Lightning आणि लढाऊ मल्ल पिंगला नाडीचा वापर करतात.
       - **Suṣumnā (सुषुम्ना - The Central Highway):** मेरुदंडाच्या (पाठीच्या कण्याच्या) पोकळीतून जाणारा सर्वोच्च आध्यात्मिक महामार्ग; सामान्य नश्वर मानवांमध्ये १००% सुप्त व सील केलेला असतो.
     - **The Pañca-Prāṇa Currents (पंच-प्राण लढाऊ कार्ये):**
       - *Prāṇa (प्राण):* वातावरणातील शुद्ध चैतन्य श्वासावाटे आत घेणे.
       - *Apāna (अपान - Earthing Buffer):* अधोमुखी प्रवाह, जो अतिरिक्त ऊर्जा जमिनीत वळवतो.
       - *Samāna (समान):* नाभीमधील चयापचय व तत्त्व-पचन.
       - *Udāna (उदान):* ऊर्ध्वमुखी प्रक्षेपण—घशातून मंत्रोच्चार, गर्जना आणि अस्त्र-प्रक्षेपण.
       - *Vyāna (व्यान):* संपूर्ण ७२,००० नाड्यांमधून रक्त व प्राण फिरवणारे संवहन; मर्यादा ओलांडल्यास नाडी-दाह (Blowout) होतो.
  2. *Nadi-Shuddhi:* प्राणायाम आणि तपोवनातील वनस्पतींच्या काढ्यांनी 72,000 सूक्ष्म नाड्यांची पद्धतशीर स्वच्छता.
  3. *External Amplification & Runic Craft (यंत्रे, धनुर्वेद व रनिक शस्त्रे):* मानवी शरीरात देवांप्रमाणे अमर्याद ऊर्जा साठवता येत नसल्याने, मानव धनुष्य, रनिक पाती आणि मंत्र-शिलांवर रुन्स कोरतात आणि वैदिक तंत्राला आपली बाह्य मज्जासंस्था बनवतात.'''

assert old_nadi in text, 'old_nadi failed'
text = text.replace(old_nadi, new_nadi, 1)

# 2. Bracket 4
old_b4 = '     - **Bracket 4: 90% to 100% (Top 10% — High-Ranked Elites: B, A, & S-Rank):** व्हॅनगार्ड चॅम्पियन्स, कुलप्रमुख, राजेशाही सेनापती, आणि सर्वोच्च अस्त्र-साधक (B-Rank नगर-विनाशक -> A-Rank पर्वत-भेदी -> S-Rank बेट-पातळीवरील Apex अस्त्र धारक व Stage-3 टायटन श्वापद स्वामी).'
new_b4 = '''     - **Bracket 4: 90% to 100% (Top 10% — High-Ranked Elites: B, A, & S-Rank):** व्हॅनगार्ड चॅम्पियन्स, कुलप्रमुख, राजेशाही सेनापती, आणि सर्वोच्च अस्त्र-साधक:
       - **B-Rank: दुर्ग-भंजक (Fortress-Breaker / Battalion-Level):** ३०० ते ५०० सैनिकांची तुकडी किंवा किल्ल्याचे महाद्वार फोडण्याची क्षमता. शहर नष्ट करू शकत नाही.
       - **A-Rank: नगर-वेधक / सेना-संहारक (City-Siege / Army-Ender):** मोठ्या प्रादेशिक राजधानी किंवा शहराच्या वॉर्डचा वेढा घालण्याची वा संरक्षण करण्याची क्षमता.
       - **S-Rank (Tier 3 Astral Realm Apex: दुर्ग-भंजक / नगर-वेधक मर्यादा):** कोणत्याही रँकची ताकद ती कोणत्या Realm मध्ये आहे यावर अवलंबून असते. Astral Realm च्या नश्वर शार्ड्सच्या भौतिक रचनेमुळे Astral मधील S-Rank जास्तीत जास्त किल्ल्याचा पाया किंवा शहराचा भाग हलवू शकतो. (पर्वत-भेदी किंवा वैश्विक शक्ती केवळ Tier 2 Buffer Zone व Tier 1 च्या दैवी योद्ध्यांनाच शक्य आहे).'''

assert old_b4 in text, 'old_b4 failed'
text = text.replace(old_b4, new_b4, 1)

# 3. Axioms 1, 2, 4, 6
old_ax1 = '''│ 1. DHĀRAṆĀ (THE HOLD) & NĀḌĪ-DĀHA (THE SCORCH / THE BLOWOUT):                     │
│    • Shastric Concept : Dhāraṇā (धारणा — Channel Grip & Internal Capacity).       │
│    • Global / Slang   : The Hold (काया-माप) / The Blowout (नाडी-दाह / फाटणे).     │
│    • Concrete Rule    : मानवी/असुरी शरीरातील ७२,००० नाड्यांची ऊर्जा वाहून नेण्याची│
│      क्षमता तांब्याच्या तारांसारखी मर्यादित असते.                                  │
│    • जर D/C-Rank नवशिक्याने स्वतःच्या 'Hold' पलीकडचे उच्च-दाबाचे दिव्यास्त्र किंवा │
│      प्रगत उच्च-ऊर्जा रनिक शस्त्र चालवण्याचा प्रयत्न केला, तर तात्काळ              │
│      'The Blowout' (Nāḍī-Dāha) होतो — त्वचेच्या रंध्रांतून काळा धूर निघून         │
│      हात जळून काळाठिक्कर निकामी होतो.                                             │
│    • Bone-density (अस्थि-घनता) आणि Nadi-Purge च्या महिनान्-महिन्यांच्या साधनेशिवाय│
│      मोठी ताकद पेलणे निसर्गतः अशक्य आहे.                                          │'''

new_ax1 = '''│ 1. DHĀRAṆĀ (THE HOLD) & NĀḌĪ-DĀHA (THE SCORCH / THE BLOWOUT):                     │
│    • Shastric Concept : Dhāraṇā (धारणा — Channel Grip & Internal Capacity).       │
│    • Global / Slang   : The Hold (काया-माप) / The Blowout (नाडी-दाह / फाटणे).     │
│    • Concrete Rule    : मानवी/असुरी शरीरातील ७२,००० नाड्यांची ऊर्जा वाहून नेण्याची│
│      क्षमता तांब्याच्या तारांसारखी मर्यादित असते.                                  │
│    • Three Overload Stages (तीन टप्पे):                                           │
│      - Stage 1 (80-100%): डोळ्यांत लाल रक्तस्त्राव (Petechiae) व तोंडात तांब्याची चव.│
│      - Stage 2 (100-120%): Nāḍī-Dāha; त्वचेच्या रंध्रांतून काळा/निळा धूर निघणे.   │
│      - Stage 3 (>120%): Vitrification; नाड्या वितळून काचेसारख्या फुटून निकामी होणे.│
│    • Bone-density (अस्थि-घनता) आणि Nadi-Purge च्या महिनान्-महिन्यांच्या साधनेशिवाय│
│      मोठी ताकद पेलणे निसर्गतः अशक्य आहे.                                          │'''

assert old_ax1 in text, 'old_ax1 failed'
text = text.replace(old_ax1, new_ax1, 1)

old_ax2 = '''│ 2. ŚŪNYA (DRY / BURNOUT) & BREATH RESET (प्राण-शून्य व प्राणायाम विराम):          │
│    • Shastric Concept : Śūnya (शून्य — The Void State) & Prāṇāyāma (प्राणायाम).   │
│    • Global / Slang   : Dry / Burnout (कोरडा पडणे) & Breath Reset (श्वास-विराम).   │
│    • Concrete Rule    : व्हिडिओ-गेमसारखे काल्पनिक १५-सेकंदांचे कूलडाऊन टाइमर्स    │
│      अस्तित्वात नाहीत; मर्यादा संपूर्ण जैविक आणि रासायनिक आहे.                    │
│    • प्रत्येक बाण, खड्ग-झोत किंवा तत्त्व-वार आज्ञा-चक्रातील प्राण जाळतो. सलग      │
│      अति-वापर केल्यास लढाऊ 'Dry' (Śūnya) होतो — दृष्टी अंधुक होते (Hypoxia),     │
│      थंड घाम फुटतो आणि स्नायू जागच्या जागी लॉक होतात.                             │
│    • प्रत्येक प्रहारानंतर स्वतःची श्वसनगती पूर्ववत (Breath Reset) करणे अनिवार्य   │
│      असते.                                                                        │'''

new_ax2 = '''│ 2. ŚŪNYA (DRY / BURNOUT) & BREATH RESET (प्राण-शून्य व प्राणायाम विराम):          │
│    • Shastric Concept : Śūnya (शून्य — The Void State) & Prāṇāyāma (प्राणायाम).   │
│    • Global / Slang   : Dry / Burnout (कोरडा पडणे) & Breath Reset (श्वास-विराम).   │
│    • Concrete Rule    : व्हिडिओ-गेमसारखे काल्पनिक १५-सेकंदांचे कूलडाऊन टाइमर्स    │
│      अस्तित्वात नाहीत; मर्यादा संपूर्ण जैविक आणि रासायनिक आहे.                    │
│    • प्रत्येक बाण, खड्ग-झोत किंवा तत्त्व-वार आज्ञा-चक्रातील प्राण जाळतो. सलग      │
│      अति-वापर केल्यास लढाऊ 'Dry' (Śūnya) होतो — दृष्टी अंधुक होते (Hypoxia),     │
│      थंड घाम फुटतो आणि स्नायू जागच्या जागी लॉक होतात.                             │
│    • Suṣumnā Backdraft Penalty: कोरड्या (Dry) अवस्थेत हट्टाने अति-वार केल्यास     │
│      आत्मा थेट लाल अस्थिमज्जेतून (bone marrow) जीवन-रस खेचतो; हाडे ठिसूळ होतात.   │
│    • प्रत्येक प्रहारानंतर स्वतःची श्वसनगती पूर्ववत (Breath Reset) करणे अनिवार्य   │
│      असते.                                                                        │'''

assert old_ax2 in text, 'old_ax2 failed'
text = text.replace(old_ax2, new_ax2, 1)

old_ax4 = '''│ 4. GŪÑJA (THE SING) & PRĀṆA DEFLECTION (प्राण-गूंज व अस्त्र-विच्छेदन):             │
│    • Shastric Concept : Gūñja (गूंज — Acoustic Tell of Prāṇa Release).            │
│    • Global / Slang   : The Sing (किंवा The Tell) & Blade Deflection.             │
│    • Combat Dynamic   : धनुष्यातून प्राण-भारित बाण किंवा तलवारीतून तीव्र ऊर्जा-झोत │
│      सुटण्याच्या ०.२ सेकंद आधी पात्यातून/चापातून एक अति-तीक्ष्ण स्फटिक शिट्टीसारखा │
│      नाद ('The Sing') उमटतो.                                                      │
│    • अनुभवी योद्धे हवेतील हा नाद ओळखून तो बाण किंवा वार तलवारीच्या पात्याने       │
│      वळवतात (Blade Deflection) किंवा मर्म-गतीने अंतर कापून थेट वार करतात.         │'''

new_ax4 = '''│ 4. GŪÑJA (THE SING) & PRĀṆA DEFLECTION (प्राण-गूंज व अस्त्र-विच्छेदन):             │
│    • Shastric Concept : Gūñja (गूंज — Acoustic Tell of Prāṇa Release).            │
│    • Global / Slang   : The Sing (किंवा The Tell) & Blade Deflection.             │
│    • Combat Dynamic   : धनुष्यातून प्राण-भारित बाण किंवा तलवारीतून तीव्र ऊर्जा-झोत │
│      सुटण्याच्या ०.२ सेकंद आधी पात्यातून/चापातून एक अति-तीक्ष्ण स्फटिक शिट्टीसारखा │
│      नाद ('The Sing') उमटतो. अनुभवी योद्धे हा नाद ओळखून Blade Deflection करतात.   │
│    • Tactical Counters :                                                          │
│      - Śabda-Rodha (शब्द-रोध मुद्रा): मारेकरी गूंज दाबतात; वेग ४०% कमी होतो.      │
│      - Kūṭa-Gūñja (कूट-गूंज): पात्याच्या खाचेवर दाब देऊन खोटा गूंज नाद काढणे.      │'''

assert old_ax4 in text, 'old_ax4 failed'
text = text.replace(old_ax4, new_ax4, 1)

old_ax6 = '''│ 6. NIRMOKA (THE MOLT) & NĀḌĪ-PURGE (THE PURGE) (जैविक उत्क्रांतीचे पुरावे):       │
│    • Shastric Concept : Nirmoka (निर्मोक — कात टाकणे) & Kāyā-Kośa (काया-कोश).     │
│    • Global / Slang   : The Molt (श्वापदांची कात) & The Purge (मानवाचा वाफ-स्फोट).│
│    • Sensory Reality  : उत्क्रांती ही लेव्हल-अप मेनू नाही. श्वापद आपली जुनी कात    │
│      फाडून रक्ताळलेल्या अंगाने हिऱ्यासारख्या वज्र-खवले उघडतो (The Molt).          │
│      मानव आपल्या सर्व ७२,००० नाड्यांमधून निळ्या रंगाची उच्च-उष्णतेची वाफ सोडतो    │
│      (The Purge), ज्यामुळे शरीराची हाडे व स्नायू वज्रासारखे घट्ट होतात.            │'''

new_ax6 = '''│ 6. NIRMOKA (THE MOLT) & NĀḌĪ-PURGE (THE PURGE) (जैविक उत्क्रांतीचे पुरावे):       │
│    • Shastric Concept : Nirmoka (निर्मोक — कात टाकणे) & Kāyā-Kośa (काया-कोश).     │
│    • Global / Slang   : The Molt (श्वापदांची कात) & The Purge (मानवाचा वाफ-स्फोट).│
│    • Sensory Reality  : उत्क्रांती ही लेव्हल-अप मेनू नाही. श्वापद जुनी कात फाडून   │
│      वज्र-खवले उघडतो; मानव नाड्यांमधून निळी वाफ सोडतो (The Purge).                 │
│    • Combat Micro-Molt (क्षणिक-निर्मोक): रणांगणात प्रचंड उष्णतेने भाजलेली वरची     │
│      त्वचा काचेसारखी गळून पडते, ज्यामुळे शरीराच्या अंतर्गत अवयवांचे उकळणे टळते.   │'''

assert old_ax6 in text, 'old_ax6 failed'
text = text.replace(old_ax6, new_ax6, 1)

# 4. Section 11 replacement
start_s11 = text.find('## 11. The Nine-Type')
end_s11 = text.find('## 12. Five Arena Terrain')
assert start_s11 != -1 and end_s11 != -1, 'Section 11 find failed'

new_s11 = '''## 11. The Ten Elemental Disciplines & The 0th State Void (दहा लढाऊ तत्त्वे व ०-अवस्था शून्य)
*(१०-घटक लढाऊ परस्परसंबंध, ०-अवस्था शून्य, कठोर गणित व प्रतिकार तक्ता — Hard Logic & Elemental Mechanics)*

Universe B मधील प्रत्येक नैसर्गिक व आध्यात्मिक शक्ती एका निश्चित घटकाशी (Element) जोडलेली असते. कोणाचाही विजय हा केवळ "इच्छाशक्ती" किंवा "पॉवर लेव्हल" वर न ठरता, या १० घटकांच्या वैज्ञानिक व लढाऊ परस्परसंबंधांवर ठरतो.

> [!IMPORTANT]
> **The 0th State — Void (शून्य / Śūnya):**  
> हा दहावा Element नाही. ही कोणत्याही तत्त्वाची जादू नसून **Prāṇa च्या पूर्ण अनुपस्थितीची (Absolute Vacuum / Null-State) अवस्था** आहे. हे कोणत्याही साधकाचे जात-घटक नसते; ही एक अशी एन्ट्रॉपिक अवस्था आहे जी सर्व सक्रिय प्राण-लहरी शोषून घेते किंवा निष्प्रभ करते.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                            THE 10-ELEMENTAL HARD INTERACTION MATRIX                              │
│                            (+ 0TH STATE: VOID / PRĀṆA-ŚŪNYATĀ)                                   │
├─────────────┬───────────────────────────────┬───────────────────────────────┬────────────────────┤
│ ATTACK TYPE │ SUPER EFFECTIVE (2.0x DAMAGE) │ WEAK / RESISTED (0.5x DAMAGE) │ CONDITIONAL NULL   │
├─────────────┼───────────────────────────────┼───────────────────────────────┼────────────────────┤
│ 1. FIRE     │ Nature (Incinerates biomass), │ Water (Extinguishes heat),    │ None               │
│  (अग्नि)    │ Ice (Melts thermal armor)     │ Earth (Thermal absorption)    │                    │
├─────────────┼───────────────────────────────┼───────────────────────────────┼────────────────────┤
│ 2. WATER    │ Fire (Smothers flame core),   │ Wind (Disperses into spray),  │ None               │
│  (जल)       │ Earth (Erodes into silt)      │ Nature (Absorbed as sap)      │                    │
├─────────────┼───────────────────────────────┼───────────────────────────────┼────────────────────┤
│ 3. LIGHTNING│ Water (Deadly ionic conduct), │ Lightning (Equal charge),     │ Earth (Grounding   │
│  (विद्युत्) │ Wind (Ionizes air channel)    │ Ice (Low conductivity matrix) │ Buffer - saturated)│
├─────────────┼───────────────────────────────┼───────────────────────────────┼────────────────────┤
│ 4. EARTH    │ Lightning (Earthing buffer),  │ Water (Erosion into mud),     │ None               │
│  (पृथ्वी)   │ Fire (Smothers oxygen intake) │ Nature (Root fracture stress) │                    │
├─────────────┼───────────────────────────────┼───────────────────────────────┼────────────────────┤
│ 5. WIND     │ Earth (Sandblasting peel),    │ Fire (Feeds thermal vortex),  │ None               │
│  (वायु)     │ Nature (Uprooting velocity)   │ Ice (Chilled into blizzards)  │                    │
├─────────────┼───────────────────────────────┼───────────────────────────────┼────────────────────┤
│ 6. NATURE   │ Earth (Deep root fracturing), │ Fire (Rapid combustion risk), │ None               │
│  (प्रकृति)  │ Water (Photosynthetic drain)  │ Ice (Frost-bitten plant cell) │                    │
├─────────────┼───────────────────────────────┼───────────────────────────────┼────────────────────┤
│ 7. ICE      │ Nature (Cryo-shatters fibers),│ Fire (Thermal liquefaction),  │ None               │
│  (हिम)      │ Wind (Freezes air currents)   │ Earth (Dense basalt deflection│                    │
├─────────────┼───────────────────────────────┼───────────────────────────────┼────────────────────┤
│ 8. SUN      │ Darkness (Pierces shadow),    │ Water (Optical refraction),   │ None               │
│  (सूर्य)    │ Spirit (Purges impure miasma) │ Ice (Albedo reflection)       │                    │
├─────────────┼───────────────────────────────┼───────────────────────────────┼────────────────────┤
│ 9. DARKNESS │ Spirit (Corrodes consciousness│ Sun (Instant dissolution),    │ None               │
│  (तमस्)     │ Nature (Withers life-sap)     │ Fire (Illumination dispersion)│                    │
├─────────────┼───────────────────────────────┼───────────────────────────────┼────────────────────┤
│ 10. SPIRIT  │ Mind/Organics (Direct astral),│ Sun (Absorbed into pure light)│ None               │
│  (आत्मन्)   │ Lightning (Disrupts charge)   │ Darkness (Tainted by miasma)  │                    │
├─────────────┼───────────────────────────────┼───────────────────────────────┼────────────────────┤
│ 0th STATE:  │ Universal Absorption of all   │ Pure Physical Kinetic Impact  │ All Direct Pranic  │
│  VOID (शून्य)│ active Prana and spells       │ (Blunt steel / uncharged fist)│ Spells (Absorbed)  │
└─────────────┴───────────────────────────────┴───────────────────────────────┴────────────────────┘
```

### 11.1 Matchup Rationale & Combat Dynamics:
1. **The Grounding Buffer (Lightning vs Earth):** विद्युत प्रहार पृथ्वी-साधकावर आदळल्यास Apāna लहरींद्वारे तो जमिनीत वळवून नुकसान लक्षणीयरीत्या कमी (0.5x किंवा Resist) होते. मात्र हा कोणताही १००% OP चीट-कोड नाही! जर वीज अति-उच्च व्होल्टेजची (A/S-Rank अस्त्र) असेल किंवा माती आधीच संतृप्त (saturated) झाली असेल, अथवा साधक हवेत किंवा पाण्यात असेल, तर ग्राउंडिंग फेल होऊन शरीराला पूर्ण घातक शॉक बसतो.
2. **0th State Void (शून्य - निर्वात प्राण-पोकळी):** हा दहावा Element नसून Prāṇa च्या पूर्ण अनुपस्थितीची अवस्था आहे. शून्यात कोणताही मंत्र, विद्युत, किंवा प्राण-ऊर्जा टिकू शकत नाही—ते सर्व शोषून घेते. परंतु शून्याला स्वतःचा कोणताही मंत्र नसल्याने, त्यावर शुद्ध शारीरिक ताकद (Blunt Kinetic Steel) आणि भौतिक वजनाचा प्रहार १००% प्रभावी ठरतो.
3. **The Fire vs Nature & Ice Dynamic:** अग्नि प्रहार Nature (वनस्पती/बायोमास) आणि Ice (हिम-चिलखत) सहजपणे जाळून किंवा वितळवून टाकतो (२.०x). मात्र Water आणि Earth आगीचा प्रभाव शोषून घेतात.
4. **The Sun vs Darkness & Spirit Dynamic:** Sun (सूर्य-तेज) Darkness (तमस् / शापित अंधकार) आणि विकृत Spirit (अशुद्ध वासना/प्रेत-आत्मे; low-tier slang: Devils) यांना तात्काळ जाळून नष्ट करते. मात्र Darkness हे Spirit (मानसिक चेतना) वर थेट गंज चढवून त्याला विकृत करू शकते.
5. **The Water vs Lightning Dynamic:** पाण्यामध्ये विद्युत-प्रवाह प्रचंड वेगाने पसरतो, ज्यामुळे ओल्या किंवा पाण्यात उभ्या असणाऱ्या योद्ध्याला Lightning प्रहार दुप्पट (२.०x) संहारक ठरतो.

---

'''

text = text[:start_s11] + new_s11 + text[end_s11:]

# 5. Section 13.3 Yantra-Shastra Magitech
old_s13 = '''3. **Heavy Aether-Ballista & Harpoon Catapults (महा-बाण व पाश-यंत्रे):**
   - मोठ्या हिंस्त्र अंतराळ-श्वापदांना (Aether-Beasts) जमिनीवर खिळवून ठेवण्यासाठी सीमावर्ती चौक्यांवर बसवलेले अवाढव्य प्राण-बाण व पाश-यंत्रे.

---'''

new_s13 = '''3. **Heavy Aether-Ballista & Harpoon Catapults (महा-बाण व पाश-यंत्रे):**
   - मोठ्या हिंस्त्र अंतराळ-श्वापदांना (Aether-Beasts) जमिनीवर खिळवून ठेवण्यासाठी सीमावर्ती चौक्यांवर बसवलेले अवाढव्य प्राण-बाण व पाश-यंत्रे.

### 13.3 Vedic Yantra-Shastra Magitech (यंत्र-शास्त्र व अवजड वैदिक तंत्रज्ञान)
- **Zero Modern Tech Invariant:** विश्वात कोळसा, बॉयलर्स, वाफेची इंजिने, पिस्टन्स, गनपावडर, बंदुका, आणि सिलिकॉन इलेक्ट्रॉनिक्स यांवर १००% बंदी कायम आहे.
- **वैदिक न्यूमॅटिक्स व हायड्रॉलिक्स (Aether-Pneumatics):**
  1. *Vāyu-Kāṇḍa (बेसाल्ट विस्तार चेंबर्स):* ज्वालामुखीच्या बेसॉल्ट पाषाणातून व ब्राँझमधून कोरलेले सिलेंडर्स. यामध्ये पाण्याची वाफ नसून **Rasa-Vāyu (पारा व गंधकाचे अस्थिर बाष्प)** वापरले जाते, जे गतिज दाबाने झपाट्याने प्रसरण पावते.
  2. *Sūtra-Valves (रनिक दाब-झडपा):* घन-लोहाच्या स्प्रिंग्स आणि मंत्र-ट्यून केलेल्या मेकॅनिकल लीव्हर्सवर चालणाऱ्या झडपा. या झडपा अतिरिक्त प्राण-दाब हिस-नादाने हवेत सोडून देतात आणि हेवी बॅलिस्टा वा अवजड रनिक आर्मरचा रिकॉइल नियंत्रित करतात.
  3. *Makara-Hydraulics (अथांग जलचर मेद-द्रव):* खोल पाताळ-सागरातील श्वापदांच्या मेदापासून बनवलेले घट्ट, अज्वलनशील द्रव जे महाकाय दरवाजे आणि धनुर्वेद-कॅटापल्ट्सचे धक्के शोषून घेतात.

---'''

assert old_s13 in text, 'old_s13 failed'
text = text.replace(old_s13, new_s13, 1)

# Check for banned words and 'नहीं'
assert 'नहीं' not in text, "Found banned 'नहीं' with bindi!"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('SUCCESS: UNIVERSE B/New/03_Power_System.md updated cleanly with all 5 points!')
