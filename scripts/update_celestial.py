import os

file_path = r"d:\Web Novel\Brahmand\01_WORLD_BIBLE\07_Celestial_Mechanics_and_Diurnal_Cycles.md"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

target = """43:    - Mortals in Tier 3 **cannot see** Tier 1 (*Parama-Dhāma*), Tier 2 (*Antariksha-Setu*), or Tier 4 (*Śūnya-Garta*). Those realms vibrate on distinct dimensional frequencies and are shielded by the Grand Aegis Ozone Layer, remaining 100% invisible to optical sight and mundane telescopes.
44: 
45: ---"""

# Check if target is present without line numbers
target_clean = """   - Mortals in Tier 3 **cannot see** Tier 1 (*Parama-Dhāma*), Tier 2 (*Antariksha-Setu*), or Tier 4 (*Śūnya-Garta*). Those realms vibrate on distinct dimensional frequencies and are shielded by the Grand Aegis Ozone Layer, remaining 100% invisible to optical sight and mundane telescopes.

---"""

insertion = """   - Mortals in Tier 3 **cannot see** Tier 1 (*Parama-Dhāma*), Tier 2 (*Antariksha-Setu*), or Tier 4 (*Śūnya-Garta*). Those realms vibrate on distinct dimensional frequencies and are shielded by the Grand Aegis Ozone Layer, remaining 100% invisible to optical sight and mundane telescopes.

### 1.2 How Celestial Light Crosses the Infinite Void (शून्यातून प्रकाशाचे वहन व वायुमंडळ प्रज्वलन)
1. **The Vacuum Paradox (पोकळी अंधारी का दिसते?):**
   - वास्तव खगोलशास्त्रात जसे अंतराळात (Space Vacuum) कोट्यवधी मैल प्रवास करताना आजूबाजूला पूर्ण काळोख असतो आणि प्रकाश केवळ पृथ्वीच्या वातावरणावर आदळल्यावरच निळे आकाश व ऊन तयार होते, अगदी तसेच ब्रह्मांडात घडते.
   - Infinite Void (अनंत अवकाशीय शून्य) मध्ये हवा, बाष्प किंवा धुलिकण नसल्याने तिथे प्रकाशाचे विकिरण (Rayleigh Scattering) होत **नही**. त्यामुळे पोकळी पूर्णपणे काळीभोर दिसते.
2. **The Prāṇa-Sūtra Beams (प्राण-सूत्रांचे अखंड वहन):**
   - सूर्य-मंडळ (*आदित्य-बिंब*) आणि चंद्र-मंडळ (*सोम-बिंब*) हे Tier 3 च्या सर्वोच्च झेनिथवर (Zenith) परिभ्रमण करतात.
   - हे केवळ सामान्य आगीचे गोळे नसून ऋग्वेदानुसार तेजोमय दिव्य मंडळे आहेत, ज्यांमधून अति-उच्च वारंवारतेचे (High Vibrational Coherence) **'प्राण-सूत्र' (Prāṇic Light Filaments / रश्मी)** बाहेर पडतात.
   - हे किरण लेझरसारख्या सरळ रेषेत अनंत शून्याला भेदून प्रवास करतात. शून्यातील गुरुत्वाकर्षण यांना खाऊन टाकू शकत **नही**, कारण प्रकाशाची गती आणि आध्यात्मिक कंपन-शक्ती पोकळीच्या आकुंचन-बळापेक्षा श्रेष्ठ असते.
3. **The Atmospheric Ignition (वायुमंडळात प्रवेश व दिवसाचा उदय):**
   - जोपर्यंत सूर्यकिरण शून्यातून प्रवास करतात, तोपर्यंत ते अदृश्य भासतात.
   - परंतु जसा हा प्रकाश त्या त्या खंडाच्या **२० ते ३० मैलांच्या वायुमंडळात (Atmospheric Envelope)** प्रवेश करतो, तसा तो हवेतील ऑक्सिजन, बाष्प आणि भूमीच्या एथरशी घर्षण पावतो (*Rayleigh-Prāṇa Dispersion*).
   - या घर्षणातून त्या त्या खंडाचे संपूर्ण आकाश प्रज्वलित होते आणि दिवस उजाडतो!
   - मानवी खंडात सोनेरी-निळे ऊन, श्वापद खंडात पाचू-हिरवट छटा, आणि असुर खंडात तांबूस-केशरी आभा निर्माण होते.
4. **The Som-Kiraṇa Lunar Cycle (चंद्राचे शीतल अमृत-किरण):**
   - रात्रीच्या प्रहरात चंद्र-मंडळाचे शीतल सोम-किरण (Chandra-Jyotsnā) शून्यातून उतरतात, जे दिवसाची दाहक उष्णता शमवून वनस्पती, औषधी आणि जीवांच्या ७२,००० नाड्यांचे पोषण करतात.

---"""

if target_clean in text:
    text = text.replace(target_clean, insertion)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully inserted 1.2 into 07_Celestial_Mechanics_and_Diurnal_Cycles.md")
else:
    print("target_clean not found, check text")
