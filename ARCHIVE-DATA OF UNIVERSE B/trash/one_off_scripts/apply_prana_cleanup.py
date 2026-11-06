import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
new_dir = os.path.join(project_root, "New")

def clean_file(filepath, replacements):
    if not os.path.exists(filepath):
        print(f"Skipping missing file: {filepath}")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    orig = content
    for old, new in replacements:
        content = content.replace(old, new)
    if content != orig:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes needed: {filepath}")

# 1. Master Character Dossiers
dossier_replacements = [
    ("- **व्हॅनगार्ड व श्वापद अनुबंध (Vanguard & Prana-Bond):**", "- **व्हॅनगार्ड व सहजीवी बंध (Vanguard & Soul-Bond):**"),
    ("श्वापद अनुबंध:", "सहजीवी बंध:"),
]
clean_file(os.path.join(new_dir, "08_Character_Roster.md"), dossier_replacements)
clean_file(os.path.join(new_dir, "08_Character_Dossiers_and_Psychology", "01_Master_Character_Dossier_73_Roster_and_Sheets.md"), dossier_replacements)

# 2. 06 Astral Realm Geography & mirror
geo_replacements = [
    ("### 2.3 The Grand Proving Grounds & The Vanguard / Prana-Beast League", "### 2.3 The Grand Proving Grounds & The Master Vanguard & Beast League"),
    ("Vanguard Board & Prana-Beast League", "The Master Vanguard & Beast League"),
    ("Symbiotic Prana-Beast Arena Battles", "Symbiotic Beast Arena Battles (सहजीवी वन्य श्वापद आखाडे)"),
    ("The Wild Prana-Beasts (वन्य प्राण-श्वापदे / Untamed Fauna):", "The Wild Aether-Beasts (वन्य श्वापदे / Untamed Fauna):"),
    ("Wild Prana-Beasts", "Wild Aether-Beasts"),
    ("वन्य प्राण-श्वापद", "वन्य श्वापद"),
    ("वन्य प्राण-श्वापदे", "वन्य श्वापदे"),
    ("Prāṇa-Bandhana Philosophy (प्राण-बंधनाचा पवित्र करार):", "Soul-Bond Philosophy (पवित्र सहजीवी आत्म-बंध):"),
    ("*Prāṇa-Bandhana* चे पवित्र शामन-गुरू", "*Soul-Bond* चे पवित्र शामन-गुरू"),
    ("स्वेच्छेने **Prāṇa-Bandhana** करतात", "स्वेच्छेने **सहजीवी आत्म-बंध (Soul-Bond)** करतात"),
    ("स्वेच्छेने (Consent-based) जोडली जातात, कारण साधकाच्या नाड्या त्यांचे विषारी प्राण शोषून शुद्ध एथर देतात", "स्वेच्छेने (Consent-based) जोडली जातात, कारण साधकाच्या नाड्या त्यांचे विषारी औष्णिक ताण शोषून शुद्ध एथर देतात"),
]
clean_file(os.path.join(new_dir, "06_The_Astral_Realm.md"), geo_replacements)
clean_file(os.path.join(new_dir, "05_Astral_Realm_Five_Sub_Realms", "02_Astral_Realm_Geography_Clans_Timeline_Officers.md"), geo_replacements)

# 3. 02 Cosmic History & mirror
hist_replacements = [
    ("### 3.3 The Prana-Bandhana Accord with Conscious Beast-Folk", "### 3.3 The Great Beast Accord with Conscious Beast-Folk (पवित्र श्वापद तह / आत्म-बंध करार)"),
    ("Prāṇa-Bandhana Accord", "The Great Beast Accord (पवित्र श्वापद करार)"),
    ("Prana-Bandhana Accord", "The Great Beast Accord"),
    ("### 4.3 The Central Vanguard Board & Prana-Beast League (वीर फलक व प्राण-श्वापद स्पर्धा)", "### 4.3 The Master Vanguard & Beast League (वीर फलक व श्वापद आखाडा स्पर्धा)"),
    ("The Grand Vanguard & Prana-Beast League (वीर फलक व आखाडा स्पर्धा)", "The Master Vanguard & Beast League (वीर फलक व श्वापद आखाडा स्पर्धा)"),
    ("Prana-Beast Arena Duels:", "Symbiotic Beast Arena Duels:"),
    ("Wild Prana-Beasts", "Wild Aether-Beasts"),
    ("वन्य प्राण-श्वापद", "वन्य श्वापद"),
]
clean_file(os.path.join(new_dir, "02_Four_Eras_and_Seals.md"), hist_replacements)
clean_file(os.path.join(new_dir, "01_Cosmology_and_Realms", "02_Cosmic_History_The_Four_Eras_and_Seals.md"), hist_replacements)

# 4. 12 Chronological Four Eras & mirror
annals_replacements = [
    ("प्राण-बंधन करार (Prāṇa-Bandhana Accord)", "पवित्र श्वापद करार (The Great Beast Accord / Soul-Bond)"),
    ("The Prāṇa-Bandhana Accord with Conscious Beast-Folk:", "The Great Beast Accord with Conscious Beast-Folk:"),
    ("The Vanguard Ranking Board, Prana-Beast League & The Buffer Zone Pipeline", "The Master Vanguard & Beast League & The Buffer Zone Pipeline"),
    ("The Master Vanguard Ranking Board & Prana-Beast League", "The Master Vanguard & Beast League"),
    ("Wild Prana-Beasts", "Wild Aether-Beasts"),
    ("*Prāṇa-Bandhana* करण्याची शास्त्रीय पद्धत", "*Soul-Bond (सहजीवी आत्म-बंध)* करण्याची शास्त्रीय पद्धत"),
]
clean_file(os.path.join(new_dir, "12_Historical_Annals.md"), annals_replacements)
clean_file(os.path.join(new_dir, "01_Cosmology_and_Realms", "08_Chronological_Four_Eras_Deep_Historical_Annals.md"), annals_replacements)

# 5. INDEX.md
index_replacements = [
    ("Vanguard Hero Board & Prana-Beast League", "The Master Vanguard & Beast League"),
    ("Prana-Beast League", "Beast League"),
    ("Prāṇa-Bandhana Accord", "The Great Beast Accord"),
    ("Prana-Bandhana Accord", "The Great Beast Accord"),
    ("Prana-Bandhana Beast Accord", "Great Beast Accord"),
    ("Wild Prana-Beasts (वन्य प्राण-श्वापदे):", "Wild Aether-Beasts (वन्य श्वापदे):"),
    ("Wild Prana-Beasts", "Wild Aether-Beasts"),
    ("Prāṇa-Bandhana", "Soul-Bond (सहजीवी आत्म-बंध)"),
    ("Prana-Bandhana", "Soul-Bond"),
    ("Prana-Beast Arena Battles:", "Symbiotic Beast Arena Battles:"),
    ("Prana-Beast Arena Battles", "Symbiotic Beast Arena Battles"),
]
clean_file(os.path.join(new_dir, "INDEX.md"), index_replacements)

# 6. Power System Audit
power_replacements = [
    ("Prāṇa-Imbued Ammunition Limits", "Aether-Imbued Ammunition / Breaker Cartridges"),
    ("Prāṇa-Imbued Ammunition Industrial Limit:", "Aether-Imbued Ammunition Industrial Limit:"),
    ("Prāṇa-Bandhan (F-05):", "Soul-Bond / Sahajeevi Bandh (F-05):"),
    ("Prāṇa-Bandhan — The Symbiotic Mortal–Beast Bond", "Soul-Bond — The Symbiotic Mortal–Beast Bond"),
]
clean_file(os.path.join(new_dir, "02_Metaphysics_and_Power_Systems", "09_Power_System_Phase1_Canon_Audit.md"), power_replacements)
clean_file(os.path.join(new_dir, "02_Metaphysics_and_Power_Systems", "08_Power_System_Consistency_Audit.md"), power_replacements)

# 7. Politics & Economics & mirror
econ_replacements = [
    ("Beast Prana-Roots", "Beast Vitality-Roots"),
    ("প্রাণ-भत्ता कपात (Prana-Stipend Cut)", "एथर-भत्ता कपात (Aether-Stipend Cut)"),
    ("प्राणी-गुलामगिरी (Prana-Bandhana चे उल्लंघन)", "प्राणी-गुलामगिरी (The Great Beast Accord चे उल्लंघन)"),
]
clean_file(os.path.join(new_dir, "11_Astral_Society.md"), econ_replacements)
clean_file(os.path.join(new_dir, "05_Astral_Realm_Five_Sub_Realms", "05_Astral_Realm_Politics_Economics_Everyday_Living.md"), econ_replacements)
clean_file(os.path.join(new_dir, "04_Buffer_Zone_The_Setu", "04_Buffer_Zone_Operational_System_and_Regulations.md"), econ_replacements)

print("All target markdown files processed successfully!")
