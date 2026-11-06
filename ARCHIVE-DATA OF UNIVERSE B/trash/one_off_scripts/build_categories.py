import os
import re
import html
import json

_current_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_current_dir)
base_dir = os.path.join(_project_root, "New")
if not os.path.exists(base_dir):
    base_dir = r"D:\Web Novel\New"

categories = [
    {
        "folder": "powers",
        "title": "Powers, Combat Metaphysics & Astras",
        "icon": "⚡",
        "marathi_summary": "Universe B चा अभेद्य लढाऊ कणा. यात कोणतेही Gamer Menus किंवा Floating HP Screens नाहीत. Five Pillars (Authority, Energy, Karma, Tapasya, Boons) आणि Secret Sixth Pillar (Atma-Tattva) वर चालणारी संपूर्ण व्यवस्था. Tensura, LOTM, आणि MHA धर्तीवरील 4-Tier Evolution Ladder (Common, Extra, Unique, Ultimate) आणि The Hold, The Blowout, Dry, The Sing, The Molt, The Purge, The Chime या 7 Pure Steel लढाऊ नियमांचे भौतिक व जैविक मेकॅनिक्स.",
        "key_points": [
            "No Video Game Menus — कोणतीही Floating Screen किंवा मोफत लेव्हल-अप नाही, ताकद खरी मेहनत, तपस्या आणि जैविक मर्यादांवर ठरते.",
            "Five Pillars + Atma-Tattva — विश्वाचे पाच मुख्य Pillars आणि कधीही नष्ट न होणारा गुप्त Soul Core (Ātma-Tattva).",
            "4-Tier Ability Evolution Ladder — Prāthamika (Common), Pravīṇa (Extra), Advitīya (Unique / Soul-Imprinted) आणि Parama-Śakti (Ultimate Authority).",
            "Seven Pure Steel Combat Axioms — The Hold ची जैविक क्षमता, The Blowout चा नाडी-दाह, Dry प्राण-शून्यता, The Sing चा प्री-इग्निशन नाद, आणि The Molt/Purge उत्क्रांती.",
            "12 Power Classes & Hard Counters — Pyrokinesis, Cryo, Electrokinesis, Vajra-Deha, Laghima, Spatial Severance, Aether Ballistics आणि Beast Soul-Sync चे परस्पर काउन्टर्स.",
            "Divine Astras & Dhanurveda Arsenal — मानवांना व देवांना कडक नियम असणारे वैश्विक अस्त्र भांडार (Āgneyāstra, Vajra, Brahmashirā, Sudarśana).",
            "Vedic & Agamic Summoning Codex — Pancha-Anga Vidhi, Type-1 Paraloka-Jiva Soul-Recall (Rigveda 10.58/173), Type-2 Devil Abhichara & Kay-Tyag Law, आणि Rakshoghna Exorcism (Rigveda 7.104/10.87)."
        ]
    },
    {
        "folder": "world",
        "title": "Cosmology, Four Tiers & Worldbuilding",
        "icon": "🌌",
        "marathi_summary": "Cosmic Singularity आणि क्षीर सागरापासून सुरू होणारे बाल्य-विश्व (Child Cosmos). Singularity Apex वर Garbhodakashayi Vishnu आणि Ananta-Shesha चे स्थान. चार स्वतंत्र आयामी Tiers: Tier 1 (Divine Realm व High Council), Tier 2 (50,000 मैल लांब The Setu व 13 Named Officers), Tier 3 (पाच उप-लोकांचा Astral Realm), आणि Tier 4 (The Grand Aegis ने वेढलेला Corrupted Realm). कश्यप ऋषींच्या वंशातील १२ सार्वभौम श्वापद कुळे (12 Sovereign Sapient Clans), ५० प्रजातींचा (१५० उत्क्रांत रूपे) व्हिज्युअल बेस्टियरी, आणि नैसर्गिक आत्म-बंध (Prana-Bandhana).",
        "key_points": [
            "Singularity Apex & Kshira Sagara — विश्वाचा उगमबिंदू; Garbhodakashayi Vishnu चे स्थान आणि सर्व आत्म्यांना चैतन्य देणारा अखंड प्राण-स्त्रोत.",
            "Four Tiers Architecture — Divine Realm (Tier 1), The Great Setu (Tier 2), Five Astral Sub-Realms (Tier 3), आणि Corrupted Realm (Tier 4).",
            "The Great Setu & Grand Aegis — अवकाशात तरंगणारा 50,000 मैलांचा महा-सेतू आणि अधो-लोकाला रोखणारे 360° अभेद्य कवच.",
            "Soul Administration Workflow — Yama, Vidhata आणि Chitragupta यांची घटनात्मक स्वायत्त न्यायालये; Route A व Route B आगमन व Pratigraha Official Dock.",
            "High Council & Parliamentary Cycles — सभा-लोक रोटुंडा, तीन संसदीय सत्रे (महा-सत्र, ऋतु-सभा, आत्यायिक) आणि Absolute Combat Ban.",
            "Multi-Species Historical Perspectives — Devas, Asuras, Humans, Beasts आणि Aliens Diaspora च्या नजरेतून चार युगांचा (Genesis, Cataclysm, Partition, Kali) इतिहास.",
            "12 Sovereign Sapient Beast Clans & 50 Visual Species — Suparna/Garuda, Maha-Naga, Vanara, Riksha, Shardula, Dig-Gaja सह १२ राजवंश; Zero Pokéballs / 100% भौतिक अस्तित्व व Nadi-Refinery उत्क्रांती."
        ]
    },
    {
        "folder": "tournaments",
        "title": "The Proving Games & Vanguard Arenas",
        "icon": "⚔️",
        "marathi_summary": "The Proving Games हा विश्वाचा सर्वात मोठा अधिकृत लढाऊ व व्यावसायिक महोत्सव (Early Kali Yuga Genesis). चार प्रांतिक भगिनी-मंडळे (हस्तिनापूर, काल्डेरा, कॅनॉपी, सीमांत सेतू/एलियन) मधून १,००० गुण व परवाना मिळवणारे लढाऊ. देवांची रिंगणात लढण्यास १००% बंदी (Zero Deva Contenders). Beyblade व Pokémon League धर्तीवर ५ श्रेणींची (D, C, B, A, S) सम-रँक रचना, अखंड लढाईचा नियम (Continuous Fight Rule), Shodhana Tuning Forks, Rotary Tectonic Anchors, आणि चार निष्पक्ष पंचांचे (Quad-Referee Panel) लढाऊ न्यायालय.",
        "key_points": [
            "Four Regional Sister-Tournaments — हस्तिनापूर, काल्डेरा, कॅनॉपी व सीमांत सेतू/एलियन मंडळांतून १,००० गुणांची चाळणी.",
            "Absolute Deva Combat Ban — देव केवळ उंचावरील सज्जांतून प्रेक्षक व प्रायोजक; रिंगण केवळ मानव, असुर, श्वापद व एलियन्ससाठी.",
            "5-Tier Divisions (D to S) — सम-श्रेणी लढाऊ नियम (Same-Tier Matchmaking) आणि मुक्त आंतर-लोकीय सोडत (Open Cross-Realm Draw).",
            "Continuous Fight Rule & The Chime — रिंगणात शत्रूचे वार थांबत नाहीत; चालू युद्धातच जैविक उत्क्रांती पेलण्याचा नियम.",
            "Rotary Tectonic Anchors & 5 Hazards — रिंगणातील ५,०००-टन हायड्रॉलिक मेकॅनिकल लंगर आणि भौगोलिक धोके.",
            "S-Rank Divergence — लक्षावधींची कमाई करणारे Arena Tycoons विरूद्ध महासेतूवर विश्वाचे रक्षण करणारे Cosmic Sentinels."
        ]
    },
    {
        "folder": "characters",
        "title": "Characters & Factions Master Dossiers",
        "icon": "👥",
        "marathi_summary": "चारही Tiers मधील १२० अधिकृत व्यक्तींचे सविस्तर वास्तववादी प्रोफाईल्स (60% Global Mythic + 40% Clipped Archaic Sanskrit). प्रत्येकाचा युनिक कॅनोनिकल आयडी (CHR-HUM, CHR-ASU, CHR-DEV, CHR-BST, CHR-CEN, CHR-SET, CHR-ABY, CHR-DIV, CHR-ALN). ५% एलियन्स डायस्पोरा. Deva-Asura शीतयुद्ध आणि संस्थात्मक तणाव. विश्व हे कोणत्याही एका व्यक्तीवर अवलंबून नसून १२० पात्रांच्या वास्तववादी जीवनप्रवाहावर स्थिर आहे.",
        "key_points": [
            "120 Verified Character Dossiers — प्रत्येकाचे वय, कौशल्ये, कमकुवत बाजू, मनोवैज्ञानिक जखमा आणि नातेसंबंध.",
            "Balanced Global-Vedic Naming — ६०% ग्लोबल मिथिक (Aurelius, Lysandra, Valkyrie, Silas) + ४०% क्लिप्ड संस्कृत (Parikshat, Dhriti, Shrutan, Satyak, Vajran, Vritra).",
            "Twin-Function Doctrine & Cold War — Devas ची कायदेशीर सुव्यवस्था विरूद्ध Asuras चे धातू-शास्त्र व फाउंड्रीज.",
            "The Great Beast Accord — प्राण्यांचे संपूर्ण कायदेशीर स्वातंत्र्य आणि स्वेच्छेचा Soul-Bond करार.",
            "Living World Independence — कोणताही पूर्व-निश्चित नायक नाही; संपूर्ण विश्व स्वतंत्र सामाजिक व राजकीय नियमांवर कार्यरत.",
            "Aliens Diaspora — समांतर विश्वांतून हस्तिनापूर एन्क्लेव्हमध्ये स्थायिक झालेली 5% परदेशी नागरी वसाहत."
        ]
    },
    {
        "folder": "rules",
        "title": "Combat Axioms, Novel Craft & World Ecology",
        "icon": "📜",
        "marathi_summary": "कादंबरी लेखनाचे तंत्रज्ञान, संवेदी अँकर्स (कच्चा एथर-स्लॅग, ओझोन, रक्त, धातूचा वास), ५ घटकांची दृश्य रचना, आणि संवादाचे जागतिक नियम. The Pure Steel Combat Axioms चा संपूर्ण संदर्भ. The 3-Volume Narrative Veil Protocol, Veil Dictionary, मुख्य पात्र 'Neel' चे मनोवैज्ञानिक रेखाटन, आणि 70/30 Seasonal Dual-Star Anthology Engine.",
        "key_points": [
            "Pure Steel Combat Axioms — The Hold, The Blowout, Dry, The Sing, The Molt, The Purge, The Chime चे लढाऊ नियम.",
            "3-Volume Narrative Veil Protocol — व्हॉल्यूम १ ते ३ मध्ये हिंदू मायथॉलॉजी झाकण्यासाठी Central City Common Concord संज्ञा (The Solarians, The Calderans, The Upper Citadel) चा पडदा.",
            "Protagonist Neel (The Skeptical Glitch-Drifter) — २१व्या शतकातील भारतीय इंजिनिअरिंग विद्यार्थी; Mid-IQ थिअरी + 200-IQ स्ट्रीट व हारेम इन्स्टिंक्ट; अंधश्रद्धा न मानल्यामुळे ट्विस्ट सुरक्षित राहतो.",
            "70/30 Seasonal Dual-Star Engine — सीझन १ मध्ये नीलचा प्रवास, सीझन २ मध्ये Great Setu + Shards दुहेरी ट्रॅक, आणि सीझन ३ मध्ये Era 2 फ्लॅशबॅक.",
            "Four Watertight Seam Fixes — Two-Tongue Law, Vidhata's Filter, Rotary Shadow Anchors चे ध्वनी-आच्छादन, आणि The Sing चे प्राण-शिट्टी मेकॅनिक्स.",
            "Living Ecosystem & Supply Chains — सहा लोकांचे अस्तित्व-शास्त्र, अन्नासाठी लोखंड आणि औषधांसाठी काचेचा विनिमय."
        ]
    }
]

print(f"Total clean categories configured: {len(categories)}")
