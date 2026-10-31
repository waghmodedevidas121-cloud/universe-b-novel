import os
import re

_current_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_current_dir)
base_dir = os.path.join(_project_root, "New")

replacements = [
    # 1. cosmology / 01_Cosmic_Foundation
    ("ग्रीस, बंदुकीची दारू, कोळशाचा धूर आणि खलाशांच्या संभाषणाने",
     "ग्रीस, कॉम्प्रेस्ड एथर-काडतुसे, ओझोन आणि मॅग्मा-स्लॅगची धग आणि खलाशांच्या संभाषणाने"),
    ("ग्रीस, बंदुकीची दारू, कोळशाचा धूर",
     "ग्रीस, कॉम्प्रेस्ड एथर-काडतुसे, ओझोन आणि मॅग्मा-स्लॅगची धग"),

    # 2. system / 03_Power_System
    ("४००–५०० psi steam-piston torque", "४००–५०० psi Aether-Piston & Magma Torque"),
    ("कोळशाच्या धुराचा झोत लागल्यास देवाची आंतरिक लय बिघडते आणि तीव्र मळमळ सुरू होते",
     "कच्च्या एथर-स्लॅगच्या व गंधकाच्या वाफेचा (Sulfurous Slag Exhaust) झोत लागल्यास देवाची आंतरिक लय बिघडते आणि तीव्र मळमळ सुरू होते"),
    ("कोळशाच्या धुराचा झोत लागल्यास देवाची लय बिघडते",
     "कच्च्या एथर-स्लॅगच्या व गंधकाच्या वाफेचा (Sulfurous Slag Exhaust) झोत लागल्यास देवाची आंतरिक लय बिघडते"),
    ("बॉयलर किंवा गोळीवर सर्किट कोरताना", "एथर-चेंबर किंवा गोळीवर सर्किट कोरताना"),
    ("फुटणाऱ्या बॉयलरामध्ये तीन सेकंदात", "फुटणाऱ्या एथर-प्रेशर चेंबरमध्ये तीन सेकंदात"),
    ("हात कोळशासारखा जळून निकामी होतो", "हात जळून काळाठिक्कर निकामी होतो"),

    # 3. the_setu / 05_The_Setu
    ("ऊर्जा पुरवणारे प्रचंड हाय-प्रेशर बॉयलर्स", "ऊर्जा पुरवणारे प्रचंड हाय-प्रेशर एथर-कंप्रेशन चेंबर्स"),
    ("हवेत तरंगणाऱ्या वाफेच्या टेहळणी नौका.",
     "हवेत तरंगणाऱ्या एथर-टेहळणी नौका (Aether-Buoyant Recon Dirigibles)."),
    ("हवेत ओझोन, आयनीकृत प्राण, बॉयलरची वाफ आणि जुन्या कागदांचा सुवास दरवळतो.",
     "हवेत ओझोन, आयनीकृत प्राण, एथर-कंप्रेशन आणि जुन्या कागदांचा सुवास दरवळतो."),
    ("रूळ, वाफ, कोळसा — काहीही नाही", "रूळ, वाफ, धूर — काहीही नाही"),

    # 4. corrupted_realm / 07_The_Corrupted_Realm
    ("जुन्या वाफेच्या बॉयलर्सच्या प्लेट्स", "जुन्या एथर-प्रेशर चेंबर्सच्या प्लेट्स"),
    ("२-इंच जाड बॉयलर-प्लेट चिलखत", "२-इंच जाड वज्र-पोलादी पत्री चिलखत (Heavy Pressure-Plate Armor)"),
    ("रिव्हेटेड बॉयलर्सच्या पोलादी पत्र्यांनी", "रिव्हेटेड प्रेशर-चेंबरच्या पोलादी पत्र्यांनी"),

    # 5. leaderboard / proving_games
    ("Asura Heavy Steam Hoists", "Asura Heavy Aether-Hydraulic Hoists (५,०००-टन हायड्रॉलिक जॅक्स)"),
    ("स्टीम बॉयलर्सचे दाब-नियम", "हाय-प्रेशर चेंबर्सचे दाब-नियम"),

    # 6. faction_politics / 09_Faction_Politics
    ("असुरांच्या कोळशावर १००% अवलंबून आहेत", "असुरांच्या पोलादी वीट (Foundry Iron Bars) वर १००% अवलंबून आहेत"),
    ("उच्च-दाब बॉयलर पत्र्यांशिवाय त्यांचे कोणतेही वाफेचे इंजिन किंवा तोफ बनू शकत नाही",
     "उच्च-दाब एथर-चेंबर पत्र्यांशिवाय त्यांचे कोणतेही लॅटिस-इंजिन किंवा तोफ बनू शकत नाही"),
    ("उच्च-दाब टंगस्टन स्टीम-वॉल्व्ह्ज, आणि ५०० psi क्षमतेचे बॉयलर कव्हर",
     "उच्च-दाब टंगस्टन मॅग्मा-वॉल्व्ह्ज, आणि ५०० psi क्षमतेचे एथर-प्रेशर कव्हर"),
    ("कोळशाच्या धुराची प्राणघातक ॲलर्जी", "गंधक व कच्च्या एथर-स्लॅगच्या धुराची प्राणघातक ॲलर्जी"),

    # 7. races_and_clans / 13_Races_and_Clans
    ("जगाला कोळशाच्या धूरात गुदमरवून टाकतील", "जगाला स्लॅग व गंधकाच्या धूरात गुदमरवून टाकतील"),
    ("४०० psi बॉयलर नियंत्रण", "४०० psi एथर-प्रेशर चेंबर नियंत्रण"),
    ("लाकूड आणि कोळशासाठी", "लाकूड आणि एथर-खनिजांसाठी"),
    ("धान्यावर कोळशाचे कृत्रिम निर्बंध लादणे", "धान्यावर लोह-वीट व एथर-काडतुसांचे कृत्रिम निर्बंध लादणे"),

    # 8. astral_realm / 06_The_Astral_Realm
    ("कोळशाच्या धुराला अजिबात तोंड देऊ शकत नाहीत", "गंधक व स्लॅगच्या धुराला अजिबात तोंड देऊ शकत नाहीत"),
    ("लोकोमोटिव्ह बॉयलरला वितळवू शकते", "लोकोमोटिव्ह प्रेशर-चेंबरला वितळवू शकते"),
    ("कोणतेही स्टीम-एअरशिप किंवा बलून", "कोणतीही एथर-टेहळणी नौका किंवा बलून"),
    ("हवेमध्ये धूर किंवा कोळशाचा लवलेश नसतो", "हवेमध्ये धूर किंवा काजळीचा लवलेश नसतो"),
    ("हवेत धूर किंवा कोळशाची काजळी नसते", "हवेत धूर किंवा काजळी नसते"),

    # 9. history / 12_Historical_Annals
    ("वाफ व कोळशावर चालणारे", "लॅटिस-रेल व एथर-काडतुसांवर चालणारे"),
    ("दगडी कोळशाची धुराडी", "मॅग्मा-फाउंड्रीज"),
]

target_files = []
for root, dirs, files in os.walk(base_dir):
    if any(x in root for x in ["trash", "__pycache__", ".git", "_preview"]):
        continue
    for file in files:
        if file.endswith(".md"):
            target_files.append(os.path.join(root, file))

for fp in target_files:
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    orig = content
    for old_s, new_s in replacements:
        if old_s in content:
            content = content.replace(old_s, new_s)
    if content != orig:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        rel = os.path.relpath(fp, _project_root)
        print(f"Applied tech patch to {rel}")

# Mirror check between top-level and subfolder files
mirrors = [
    ("01_Cosmic_Foundation.md", "world/cosmology.md"),
    ("02_Four_Eras_and_Seals.md", "world/history.md"),
    ("03_Power_System.md", "powers/system.md"),
    ("04_Soul_Administration.md", "world/soul_admin.md"),
    ("05_The_Setu.md", "world/the_setu.md"),
    ("06_The_Astral_Realm.md", "world/astral_realm.md"),
    ("07_The_Corrupted_Realm.md", "world/corrupted_realm.md"),
    ("08_Character_Roster.md", "characters/roster.md"),
    ("09_Faction_Politics.md", "characters/factions.md"),
    ("11_Astral_Society.md", "world/society.md"),
    ("13_Races_and_Clans.md", "characters/races.md"),
    ("15_Leaderboard_System.md", "tournaments/leaderboard.md"),
    ("16_The_Proving_Games.md", "tournaments/proving_games.md"),
]

for src, dst in mirrors:
    p1 = os.path.join(base_dir, src)
    p2 = os.path.join(base_dir, dst.replace("/", os.sep))
    if os.path.exists(p1) and os.path.exists(p2):
        c1 = open(p1, encoding="utf-8").read()
        c2 = open(p2, encoding="utf-8").read()
        if c1 != c2:
            # Sync p2 from p1 (except if p1 has header difference, ensure parity)
            with open(p2, "w", encoding="utf-8") as f:
                f.write(c1)
            print(f"Synced {dst} from {src} for 100% parity.")
        else:
            print(f"Parity verified: {src} == {dst} ({len(c1)} bytes)")
