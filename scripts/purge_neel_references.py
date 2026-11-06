# -*- coding: utf-8 -*-
"""
Script to systematically remove all Neel-specific references from the worldbuilding
and power system files in Brahmand, replacing them with objective, world-first lore.
Preserves 100% adherence to the 'नही' rule.
"""
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"d:\Web Novel\Brahmand"

def patch_file(rel_path, replacements):
    path = os.path.join(ROOT_DIR, rel_path)
    if not os.path.exists(path):
        print(f"File not found: {rel_path}")
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = 0
    for target, repl in replacements:
        if target in content:
            content = content.replace(target, repl)
            count += 1
        else:
            print(f"  Target not found in {rel_path}: {target[:40]}...")
            
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Patched {count} items in {rel_path}")

# 1. 02_POWER_SYSTEM/02_Elements_Preta_and_Cursed_Weapons.md
p2_replacements = [
    ("The signature weapon of **Neel**, the 19-year-old mortal protagonist cast into the Astral Cosmos.",
     "The archetypal Shaapit Shastra: an executioner's chain forged in the Era 2 abyss and bound to a mortal vessel."),
    ("Bound to Neel's Left Forearm & Wrist", "Bound to the Wielder's Left Forearm & Wrist"),
    ("wraps tightly around Neel's left forearm", "wraps tightly around the wielder's left forearm"),
    ("When Neel lashes out", "When the wielder lashes out"),
    ("whenever Neel's pulse spikes above 140 BPM", "whenever the wielder's pulse spikes above 140 BPM"),
    ("Outside combat, Neel unspools the chain", "Outside combat, the wielder unspools the chain"),
    ("In battle, he snaps it back down", "In battle, the warrior snaps it back down"),
    ("Neel whips his left arm forward using a pitcher's shoulder snap", "The warrior whips their left arm forward with a sharp shoulder snap"),
    ("Neel drives his heels into the flagstones", "The warrior drives their heels into the flagstones"),
    ("Neel contracts the 33 links rapidly around his left forearm", "The warrior contracts the 33 links rapidly around their left forearm"),
    ("up Neel's humerus, bruising muscle tissue and requiring him to brace his right hand behind his left wrist",
     "up the wielder's humerus, bruising muscle tissue and requiring bracing with the opposite hand"),
    ("frosting Neel's breath into white mist", "frosting the warrior's breath into white mist"),
    ("The Parasitic Toll & Neel's Survival Paradox", "The Parasitic Toll & The Mortal Vessel Paradox"),
    ("coiled around Neel's mortal flesh", "coiled around the wielder's mortal flesh"),
    ("creeping toward Neel's shoulder", "creeping toward the wielder's shoulder"),
    ("Why Neel Can Wield KALI Without Perishing", "Why a Mortal Vessel Can Wield KALI Without Perishing"),
    ("Why does a mortal 19-year-old street survivor from Mumbai not have his soul devoured by this abyssal shackle within seconds?",
     "Why does an unranked mortal human not have their soul devoured by this abyssal shackle within seconds?"),
    ("Neel possesses **zero divine radiance**.", "An unascended mortal possesses **zero divine radiance**."),
    ("His body is pure, gritty, mortal earth-clay", "Their body is pure, gritty, mortal earth-clay"),
    ("Neel's companion, the shadow hound **Kuro (Sheru)**, acts as an external soul-radiator. Kuro consumes the excess necrotic frost leaking from KĀLĪ, preventing frostbite from advancing past Neel's elbow.",
     "A companion beast (such as a loyal shadow-hound) acts as an external soul-radiator, consuming excess necrotic frost leaking from KĀLĪ to prevent frostbite advancing past the wielder's elbow."),
    ("where he snaps at Neel.", "where the hound snaps indiscriminately."),
    ("forces Neel to strictly ration", "forces the wielder to strictly ration"),
    ("when Neel fights not for divine glory or pride, but to protect his companion and secure another day of life—his dormant **Atma-Tattva** ignites.",
     "when an unranked mortal fights not for vanity or pride, but in selfless defense of life—the dormant **Ātma-Tattva** ignites."),
    ("sub-zero frostbite on Neel's fingers", "sub-zero frostbite on mortal fingers")
]
patch_file(r"02_POWER_SYSTEM\02_Elements_Preta_and_Cursed_Weapons.md", p2_replacements)

# 2. 02_POWER_SYSTEM/04_The_Proving_Games_and_Split_Flap_Spire.md
p4_replacements = [
    ("### 7.1 Neel's Entrance: The Feeder from the Gutter", "### 7.1 The Feeder from the Gutter: Mortal Contenders"),
    ("Neel enters the Proving Games not out of hunger for divine prestige, but out of absolute, desperate survival:",
     "Unranked mortal contenders enter the Proving Games not out of hunger for divine prestige, but out of absolute, desperate survival:"),
    ("- **He has zero food and zero currency:** Central City does not hand out charity. Bread costs 2 Copper Mashas; clean water costs 1 Masha. Entering the lowest qualification bout of the Proving Games is the only way a penniless mortal can earn legal coin and avoid starvation.",
     "- **Zero Charity:** Central City does not hand out alms. Bread costs 2 Copper Mashas; clean water costs 1 Masha. Entering the lowest qualification bouts is the only legal way a penniless vagrant can earn coin and avoid starvation."),
    ("- **The Anti-Hero Playstyle:** Neel does not fight with aristocratic elegance or noble martial forms. He fights like an alley cat: throwing blinding sand into eyes, using KALI's chain to hook Achilles tendons, feigning agony to lure arrogant opponents into over-committing, and executing bone-snapping Apāna ground-locks.",
     "- **Grounded Pit Brawling:** Desperate mortals do not fight with aristocratic elegance or noble martial forms. They fight like alley cats: throwing blinding sand into eyes, using chains to hook Achilles tendons, feigning agony to lure arrogant opponents into over-committing, and executing bone-snapping Apāna ground-locks."),
    ("- **The Spire's First Flip for Neel:** When Neel chokes out an arrogant ranked veteran in his debut match, the subterranean gears groan, and flap #4,912 clatters open to reveal: **NEEL (मर्त्य — HUMAN REALM)**.",
     "- **The Spire's Turn:** When an unknown feeder chokes out an arrogant ranked veteran in a debut match, the subterranean gears groan, and flap #4,912 clatters open to reveal an unranked mortal's name under the Human Realm header."),
    ("[ SPLIT-FLAP SPIRE BOARD #4912 ]", "[ SPLIT-FLAP SPIRE SAMPLE BOARD #4912 ]"),
    ("│  #4912 : NEEL  [MORTAL]      │", "│  #4912 : MORTAL CONTENDER    │")
]
patch_file(r"02_POWER_SYSTEM\04_The_Proving_Games_and_Split_Flap_Spire.md", p4_replacements)

# 3. 02_POWER_SYSTEM/05_Tier_Naming_and_Language_Hierarchy.md
p5_replacements = [
    ("Rookie Neel (Arrival), Pit Brawlers", "Rookie Vagrants, Pit Brawlers"),
    ("Mundane Scrap Iron | Raw Melee | Scraps & Mumbai ₹11 Change", "Mundane Scrap Iron | Raw Melee | Scraps & Cowrie Shells"),
    ("## 4. Neel's Linguistic Adaptation: The Street Translator", "## 4. Linguistic Adaptation: The Non-Native Street Ear"),
    ("Neel arrives in Central City speaking modern Mumbai Hinglish and street Marathi. He possesses **zero magical translation spells** and zero divine comprehension buffs. How does he survive?",
     "Foreign travelers and unascended mortals arrive in Central City speaking regional vernaculars. They possess **zero magical translation spells** and zero divine comprehension buffs. How do they survive?"),
    ("Neel doesn't need an AI translator because street survival in Mumbai already trained him to decode multilingual urban chaos:",
     "Travelers do not need an artificial translator because survival in multilingual trade hubs relies on shared linguistic roots:"),
    ("Neel's Marathi and Hindi vocabulary shares direct linguistic roots with Vyavahāra-Prākṛt and Apabhraṁśa.",
     "Mortal trade dialects share direct linguistic roots with Vyavahāra-Prākṛt and Apabhraṁśa."),
    ("Neel recognizes", "A listener recognizes"),
    ("Neel doesn't translate", "A listener doesn't translate"),
    ("The 0.2s Gūñja tells him", "The 0.2s Gūñja reveals"),
    ("Neel's street hustle does the rest.", "Natural street trade instinct does the rest."),
    ("3. **Neel and Street Commoners (Tier 1 & 2)** must speak punchy, realistic, cynical, and grounded dialogue (**Layer 4 Street Register**).",
     "3. **Street Commoners (Tier 1 & 2)** must speak punchy, realistic, cynical, and grounded dialogue (**Layer 4 Street Register**)."),
    ("4. **Never mix them up:** A high Deva archer should never speak like a Mumbai street vendor, and Neel should never sound like an ancient Vedic priest.",
     "4. **Never mix them up:** A high Deva archer should never speak like an alley merchant, and a street brawler should never sound like an ancient Vedic priest.")
]
patch_file(r"02_POWER_SYSTEM\05_Tier_Naming_and_Language_Hierarchy.md", p5_replacements)

# 4. 01_WORLD_BIBLE/00_Sanatan_Encyclopedic_Codex.md
p0_replacements = [
    ("Elite martial prodigies like Neel do not look at glowing lights.", "Elite martial prodigies do not look at glowing lights."),
    ("Neel uses this 0.2-second localized hum to dive behind basalt bastions or pull armored enemies into the blast zone.",
     "Frontline warriors use this 0.2-second localized hum to dive behind basalt bastions or pull armored enemies into the blast zone."),
    ("It is Neel's ultimate dormant asset as a mortal human.", "It is the ultimate dormant asset of a mortal human vessel."),
    ("Neel's sole weapon. A heavy, rusted black-iron shackle from Era 2 bound to his left forearm.",
     "An archetypal Shaapit Shastra. A heavy, rusted black-iron shackle from Era 2 bound to a mortal vessel."),
    ("Outside combat, Neel unspools KĀLĪ from his wrist", "Outside combat, the wielder unspools KĀLĪ from the wrist"),
    ("33 iron links spiral tightly around Neel's forearm", "33 iron links spiral tightly around the forearm"),
    ("Neel uses Apāna grounding to hook enemy ankles", "The wielder uses Apāna grounding to hook enemy ankles"),
    ("spreads sub-zero marrow frost up Neel's arm", "spreads sub-zero marrow frost up the wielder's arm"),
    ("Neel's sole companion who leaped with him during the Dadar Station glitch. Saturated with subtle Preta-currents during the crossing, Sheru evolved into an ash-black, shadow-sheathed hound.",
     "The archetypal loyal shadow-hound companion. Saturated with subtle Preta-currents during abyssal crossings, the hound evolves into an ash-black, shadow-sheathed guardian."),
    ("Serves as Neel's **living thermal buffer**.", "Serves as the wielder's **living thermal buffer**."),
    ("preventing frostbite from advancing past Neel's elbow", "preventing frostbite from advancing past the wielder's elbow"),
    ("guards Neel's back with ferocious loyalty.", "guards their companion's back with ferocious loyalty."),
    ("Neel must keep fights brief to safeguard his dog.", "The warrior must keep fights brief to safeguard the hound.")
]
patch_file(r"01_WORLD_BIBLE\00_Sanatan_Encyclopedic_Codex.md", p0_replacements)

# 5. 04_STORY_AND_CHAPTERS/01_Multi_Season_Anthology_Engine.md
p1_replacements = [
    ("The astral world has functioned for millennia; Neel must adapt or be crushed.",
     "The astral world has functioned for millennia; mortal champions must adapt or be crushed."),
    ("Season 1 follows Neel, a mortal catalyst from Earth cast into Central City",
     "Season 1 establishes Central City and the five autonomous realms through the brutal Proving Games"),
    ("Neel does not stay trapped in tournament arcs; by Season 2, he is a hired caravan specialist under Alarka",
     "Season 1 champions transition into caravan veterans under Alarka in Season 2"),
    ("Neel deduces metaphysics through the pragmatic lens of a Mumbai tinkerer:",
     "Grounded protagonists deduce metaphysics through observation of physical phenomena:"),
    ("Neel's Mumbai street ear intuitively pieces together", "A street ear intuitively pieces together")
]
patch_file(r"04_STORY_AND_CHAPTERS\01_Multi_Season_Anthology_Engine.md", p1_replacements)

print("\n--- ALL REMEDIATIONS COMPLETE! ---")
