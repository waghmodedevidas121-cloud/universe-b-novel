import re

# Update 01_WORLD_BIBLE/05_Cosmic_Eras_and_The_Seven_Nightmares.md
file1 = r"d:\Web Novel\Brahmand\01_WORLD_BIBLE\05_Cosmic_Eras_and_The_Seven_Nightmares.md"
with open(file1, "r", encoding="utf-8") as f:
    text1 = f.read()

# Replace list in 3.1
old_list = """  1. **Seal 1: कालकूट (Kala-Kut / Kāla-Kūṭa)** — *The Architect of Scarcity* ("Only hunger and debt force mortals to evolve.")
  2. **Seal 2: वृत्र (Vritra / Vṛtra-Chāyā)** — *The Hoarder of the Sky* ("Drag the arrogant sun down into the mud.")
  3. **Seal 3: लौह-भक्षक (Lauha-Bhakshak / Lauha-Bhakṣaka)** — *The Rust of Empires* ("All iron and law eventually rot.")
  4. **Seal 4: शून्य-ज्वाला (Shunya-Jvala / Śūnya-Jvālā)** — *The Cold Delusion* ("Desperate love will burn the world to save one soul.")
  5. **Seal 5: हिम-राक्षस (Hima-Rakshas / Hima-Rākṣasa)** — *The Mercy of Stasis* ("Life is pain; freeze all things into painless crystal.")
  6. **Seal 6: प्राण-शून्यता (Prana-Shunyata / Prāṇa-Śūnyatā)** — *The Faceless Mirror* (स्मृती व चेहरे चोरणारा महा-अंधार; The Deep-Sea Infiltrator).
  7. **Seal 7: श्रुतायुध व महा-तमस (Shrutayudh & Mahā-Tamas)** — *The Fallen Savior* (The Era-2 Hero-King merged with the 7th Horror at the Dead Chasm)."""

new_list = """  1. **Seal 1: कालकेय (Kālakeya)** — *The Architect of Scarcity* ("Only hunger and debt force mortals to evolve.")
  2. **Seal 2: पुलोमा (Puloma)** — *The Hoarder of the Sky* ("Drag the arrogant sun down into the mud.")
  3. **Seal 3: डिंभक (Dimbhaka)** — *The Rust of Empires* ("All iron and law eventually rot.")
  4. **Seal 4: असित (Asita)** — *The Cold Delusion* ("Desperate love will burn the world to save one soul.")
  5. **Seal 5: प्रालेय (Prāleya)** — *The Mercy of Stasis* ("Life is pain; freeze all things into painless crystal.")
  6. **Seal 6: शंबर (Śambara)** — *The Faceless Mirror* (स्मृती व चेहरे चोरणारा महा-अंधार; The Deep-Sea Infiltrator).
  7. **Seal 7: सम्राट श्रुतायुध व महा-तमस (Emperor Śrutāyudha & Mahā-Tamas)** — *The Fallen Savior / The Chained King* (The Era-2 Hero-King merged with the 7th Horror at the Dead Chasm)."""

if old_list in text1:
    text1 = text1.replace(old_list, new_list)
    print("Replaced 3.1 list successfully")
else:
    print("3.1 list target not found")

# Replace Stone-Eyed Crow in line 111
text1 = text1.replace("Kāgabhusuṇḍi (The Stone-Eyed Raven)", "The Stone-Eyed Crow (पाषाण-नेत्री कावळा)")

# Replace Acoustic Dampening line
text1 = text1.replace("Seal 6: Prāṇa-Śūnyatā", "Seal 6: शंबर / The Faceless Mirror")
text1 = text1.replace("Seal 6: Pra?a-Sunyata", "Seal 6: शंबर / The Faceless Mirror")

# Replace Table
old_table = """| **Seal 1** | Deep Crust Subterranean Mantle (Tier 4 Deep Floor) | **The Thermal Venom (Seal 1 / Kāla-Kūṭa)** | Chthonic Basalt Pressure Valves; supervised by Muchukunda & stone-sentinels. | Guild of Seekers (Thermal Audit) | दक्षिणेकडील भूगर्भाची लाव्हा राख होणे; संपूर्ण खंडाचा पाया कोसळणे. |
| **Seal 2** | Sunken Trench of Netherholme | **The Light-Devourer (Seal 2 / Vṛtra-Chāyā)** | Automated Aetheric Light-Siphons; guarded by Obsidian Basalt Runes. | Assembly of Sages (Forensic Audit) | दक्षिणेकडील आकाशातून कायमचा सूर्यप्रकाश नष्ट होणे; कायमचे अंधत्व. |
| **Seal 3** | Abyssal Iron Mines (The Obsidian Chasm Border) | **The Rust Colossus (Seal 3 / Lauha-Bhakshaka)** | The Eisen Clan Wardens; four-inch cold-iron anchors. | Order of Palaks (Border Inspectorate) | हवेतून गंज पसरून १,००० मैलांतील सर्व धातू, रनिक शस्त्रे व चिलखते गंजून नष्ट होणे. |
| **Seal 4** | Western Acid Marsh Basin | **The Cold Void-Flame (Seal 4 / Śūnya-Jvālā)** | Chemical Neutralization Reservoirs; high-density lime vaults. | Order of Palaks & Naga Toxicologists | उणे तापमानाची रासायनिक आग पसरून हवेतील ऑक्सिजन गोठणे. |
| **Seal 5** | Northern Permafrost Rifts | **The Frost Sovereign (Seal 5 / Hima-Rākṣasa)** | Glacial Cryo-Runic Pressure Chambers; monitored by Setu Sapper Corps. | Tri-Departmental Field Taskforce | संपूर्ण उष्णता नष्ट होऊन जिवंत आत्म्यांना काचेसारखे गोठवून टाकणे. |
| **Seal 6** | Central City Subterranean Floor (Beneath Central Coliseum Rotary Shadow Anchor) | **The Soul-Vacuum (Seal 6 / Prāṇa-Śūnyatā)** | High Council Dharmic Barrier Seals; four-layer starlight lattice. | Chief Sage (Annual Constitutional Audit) | मोठी भेग पडून लाखो जिवंत माणसांचे आत्मे थेट अवकाशात खेचले जाणे. |
| **Seal 7** | Abyssal Dead Zone (The Dead Chasm / Seal 7 Pit / Niraya-Kṣetra) | **The Seventh Darkness / Primordial Void (Seal 7 / Mahā-Tamas)** | **Shrutayudh (The Chained King) & Kāgabhusuṇḍi (Stone-Eyed Raven)**; meteoric cold-iron chains. | **Rudra's Department (Direct Trinity Mandate)** | वैश्विक महाप्रलय (*Mahā-Saṁhāra*); Universe B चे सर्व नियम आणि अस्तित्व कायमचे विसर्जित होणे. |"""

new_table = """| **Seal 1** | Deep Crust Subterranean Mantle (Tier 4 Deep Floor) | **The Architect of Scarcity (Seal 1 / कालकेय - Kālakeya)** | Chthonic Basalt Pressure Valves; supervised by Muchukunda & stone-sentinels. | Guild of Seekers (Thermal Audit) | दक्षिणेकडील भूगर्भाची लाव्हा राख होणे; संपूर्ण खंडाचा पाया कोसळणे. |
| **Seal 2** | Sunken Trench of Netherholme | **The Hoarder of the Sky (Seal 2 / पुलोमा - Puloma)** | Automated Aetheric Light-Siphons; guarded by Obsidian Basalt Runes. | Assembly of Sages (Forensic Audit) | दक्षिणेकडील आकाशातून कायमचा सूर्यप्रकाश नष्ट होणे; कायमचे अंधत्व. |
| **Seal 3** | Abyssal Iron Mines (The Obsidian Chasm Border) | **The Rust of Empires (Seal 3 / डिंभक - Dimbhaka)** | The Eisen Clan Wardens; four-inch cold-iron anchors. | Order of Palaks (Border Inspectorate) | हवेतून गंज पसरून १,००० मैलांतील सर्व धातू, रनिक शस्त्रे व चिलखते गंजून नष्ट होणे. |
| **Seal 4** | Western Acid Marsh Basin | **The Cold Delusion (Seal 4 / असित - Asita)** | Chemical Neutralization Reservoirs; high-density lime vaults. | Order of Palaks & Naga Toxicologists | उणे तापमानाची रासायनिक आग पसरून हवेतील ऑक्सिजन गोठणे. |
| **Seal 5** | Northern Permafrost Rifts | **The Mercy of Stasis (Seal 5 / प्रालेय - Prāleya)** | Glacial Cryo-Runic Pressure Chambers; monitored by Setu Sapper Corps. | Tri-Departmental Field Taskforce | संपूर्ण उष्णता नष्ट होऊन जिवंत आत्म्यांना काचेसारखे गोठवून टाकणे. |
| **Seal 6** | Central City Subterranean Floor (Beneath Central Coliseum Rotary Shadow Anchor) | **The Faceless Mirror (Seal 6 / शंबर - Śambara)** | High Council Dharmic Barrier Seals; four-layer starlight lattice. | Chief Sage (Annual Constitutional Audit) | मोठी भेग पडून लाखो जिवंत माणसांचे आत्मे थेट अवकाशात खेचले जाणे. |
| **Seal 7** | Abyssal Dead Zone (The Dead Chasm / Seal 7 Pit / Niraya-Kṣetra) | **The Fallen Savior (Seal 7 / सम्राट श्रुतायुध व महा-तमस)** | **Shrutayudh (The Chained King) & The Stone-Eyed Crow (पाषाण-नेत्री कावळा)**; meteoric cold-iron chains. | **Rudra's Department (Direct Trinity Mandate)** | वैश्विक महाप्रलय (*Mahā-Saṁhāra*); Universe B चे सर्व नियम आणि अस्तित्व कायमचे विसर्जित होणे. |"""

if old_table in text1:
    text1 = text1.replace(old_table, new_table)
    print("Replaced Table successfully")
else:
    print("Table target not found")

with open(file1, "w", encoding="utf-8") as f:
    f.write(text1)

# Update 03_CHARACTERS/04_Asura_Shard_Dossiers_16.md
file2 = r"d:\Web Novel\Brahmand\03_CHARACTERS\04_Asura_Shard_Dossiers_16.md"
with open(file2, "r", encoding="utf-8") as f:
    text2 = f.read()

text2 = text2.replace("Seal 1 (The Thermal Venom)", "Seal 1 (Kālakeya / The Architect of Scarcity)")
text2 = text2.replace("Seal 1 (Thermal Venom)", "Seal 1 (Kālakeya / The Architect of Scarcity)")

with open(file2, "w", encoding="utf-8") as f:
    f.write(text2)

print("Updated 04_Asura_Shard_Dossiers_16.md successfully")
