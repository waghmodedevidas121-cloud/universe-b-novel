import os
import re

_current_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_current_dir)
base_dir = os.path.join(_project_root, "New")

target_files = []
for root, dirs, files in os.walk(base_dir):
    if any(x in root for x in ["trash", "__pycache__", ".git", "_preview"]):
        continue
    for file in files:
        if file.endswith(".md"):
            target_files.append(os.path.join(root, file))

cleanups = [
    ('The Tectonic Maul (Obsidian Sledge / The Tectonic Maul (Obsidian Sledge))', 'The Tectonic Maul (Obsidian Sledge)'),
    ('The Sun-Scepter (Solar Lance / The Sun-Scepter (Solar Lance))', 'The Sun-Scepter (Solar Lance)'),
    ('The Prismatic Javelin (The Prismatic Javelin — तेजस्वी दैवी भाला)', 'The Prismatic Javelin'),
    ('The Cloud-Goad (The Cloud-Goad (मेघ-अंकुश))', 'The Cloud-Goad'),
    ('The Concord Mace (Golden Gavel / The Concord Mace (Golden Gavel))', 'The Concord Mace (Golden Gavel)'),
    ('The Aegis Scepter (The Aegis Scepter)', 'The Aegis Scepter'),
    ("The Inquisitor's Seal (The Inquisitor's Seal (ऋत-दंडाची मुद्रा))", "The Inquisitor's Seal"),
    ('The Architect\'s Seal (The Architect\'s Seal (सृष्टी-दंडाची मुद्रा))', 'The Architect\'s Seal'),
    ('The Black-Glass Blade (The Black-Glass Blade (तमास-काच खड्ग))', 'The Black-Glass Blade (तमास-काच खड्ग)'),
    ('SAS-ORD-02: 15mm Heavy Trench Anti-Materiel Rifle (15mm Heavy Trench Anti-Materiel Rifle)', 'SAS-ORD-02: 15mm Heavy Trench Anti-Materiel Rifle'),
    ('The Five-Arch Rotunda (Central Gateway Plaza / The Five-Arch Rotunda (Central Gateway Plaza))', 'The Five-Arch Rotunda (Central Gateway Plaza)'),
    ('The Hastinapur High Arch (Human Gate / The Hastinapur High Arch (Human Gate))', 'The Hastinapur High Arch (Human Gate)'),
    ('The Caldera Basalt Arch (Asura Gate / The Caldera Basalt Arch (Asura Gate))', 'The Caldera Basalt Arch (Asura Gate)'),
    ('The Sun-Cliff Arch (Deva Gate / The Sun-Cliff Arch (Deva Gate))', 'The Sun-Cliff Arch (Deva Gate)'),
    ('The Root-Carved Arch (Beast Gate / The Root-Carved Arch (Beast Gate))', 'The Root-Carved Arch (Beast Gate)'),
    ('The Mortal Sea (The Mortal Sea (Nashvar Samudra))', 'The Mortal Sea (Nashvar Samudra)'),
    ('The Mortal Sea (The Mortal Sea)', 'The Mortal Sea (Nashvar Samudra)'),
    ('The Central Reserve Bank (The Vaults of Truth / The Central Reserve Bank (The Vaults of Truth / Akash-Kosha))', 'The Central Reserve Bank (The Vaults of Truth / Akash-Kosha)'),
    ('The Central Reserve Bank (The Central Reserve Bank (The Vaults of Truth / Akash-Kosha))', 'The Central Reserve Bank (The Vaults of Truth / Akash-Kosha)'),
    ('The Central Reserve Bank (The Vaults of Truth / Akash-Kosha) Vaults (The Central Reserve Bank (The Vaults of Truth / Akash-Kosha))', 'The Central Reserve Bank Vaults (Akash-Kosha)'),
    ('The Grand Hall of Ledgers (The Root Archive / The Grand Hall of Ledgers (The Root Archive / Maha-Lekha-Bhavana))', 'The Grand Hall of Ledgers (The Root Archive / Maha-Lekha-Bhavana)'),
    ('The Grand Hall of Ledgers (The Root Archive / The Grand Hall of Ledgers (Maha-Lekha Archive))', 'The Grand Hall of Ledgers (The Root Archive / Maha-Lekha-Bhavana)'),
    ('The Grand Hall of Ledgers (The Root Archive / The Grand Hall of Ledgers (Maha-Lekha))', 'The Grand Hall of Ledgers (The Root Archive / Maha-Lekha-Bhavana)'),
    ('The Grand Hall of Ledgers (The Grand Hall of Ledgers (Maha-Lekha Archive))', 'The Grand Hall of Ledgers (The Root Archive / Maha-Lekha-Bhavana)'),
    ('The Grand Hall of Ledgers (The Grand Hall of Ledgers (Maha-Lekha))', 'The Grand Hall of Ledgers (The Root Archive / Maha-Lekha-Bhavana)'),
    ('The High Council Rotunda & The Supreme Sanctum (The High Council Rotunda (सभा-लोक) & The Supreme Sanctum (Parama-Dhama))', 'The High Council Rotunda & The Supreme Sanctum (Sabha-Loka & Parama-Dhama)'),
    ('The High Council Rotunda (The High Council Rotunda (Sabha-Loka))', 'The High Council Rotunda (Sabha-Loka)'),
    ('The High Council Rotunda (The High Council Rotunda (सभा-लोक))', 'The High Council Rotunda (सभा-लोक)'),
    ('The Setu Standing Army & The Bastion Fortress (The Setu Standing Army (Setu Maha-Sena) & The Bastion Fortress (Vajra-Durga))', 'The Setu Standing Army & The Bastion Fortress (Setu Maha-Sena & Vajra-Durga)'),
    ('The Setu Standing Army (The Setu Standing Army (Setu Mahā-Senā))', 'The Setu Standing Army (Setu Mahā-Senā)'),
    ('The Setu Standing Army (The Setu Standing Army (Setu Maha-Sena))', 'The Setu Standing Army (Setu Maha-Sena)'),
    ('The Bastion Fortress (The Bastion Fortress (The Vajra Fortress))', 'The Bastion Fortress (The Vajra Fortress)'),
    ('The Bastion Fortress (The Bastion Fortress (Vajra-Durga))', 'The Bastion Fortress (Vajra-Durga)'),
    ('Gravitational Pillars (Tectonic Staples / Gravitational Pillars (Tectonic Staples / Guru-Keela))', 'Gravitational Pillars (Tectonic Staples / Guru-Keela)'),
    ('The Golden Twilight (The Golden Twilight (Sāvitra-Prabhā))', 'The Golden Twilight (Sāvitra-Prabhā)'),
    ('The Golden Twilight (The Golden Twilight (Savitra-Prabha))', 'The Golden Twilight (Savitra-Prabha)'),
    ('The Final Dissolution Chamber (The Final Dissolution Chamber (Maha-Vilayana))', 'The Final Dissolution Chamber (Maha-Vilayana)'),
    ('The Red Crucible Union (Ironworkers\' Brotherhood / The Red Crucible Union (Ironworkers\' Brotherhood / Lauha-Shramik Sangha))', 'The Red Crucible Union (Ironworkers\' Brotherhood / Lauha-Shramik Sangha)'),
    ('The Forge Trials (The Forge Trials (Yantra-Pariksha))', 'The Forge Trials (Yantra-Pariksha)'),
    ('The Forge Trials (The Forge Trials (यंत्र-परीक्षा / Yantra-Pariksha))', 'The Forge Trials (Yantra-Pariksha)'),
    ('The Eagle\'s Roost (The Eagle\'s Roost (Suparna-Giri))', 'The Eagle\'s Roost (Suparna-Giri)'),
    ('The Dead Chasm (Seal 7 Pit) & The Corrupted Abyss (The Dead Chasm (Seal 7 Pit / Niraya-Kshetra) & The Corrupted Abyss (Tamo-Loka))', 'The Dead Chasm (Seal 7 Pit) & The Corrupted Abyss (Niraya-Kshetra & Tamo-Loka)'),
    ('The Dead Chasm (Seal 7 Pit / The Dead Chasm (Seal 7 Pit / Niraya-Kshetra))', 'The Dead Chasm (Seal 7 Pit / Niraya-Kshetra)'),
    ('The Corrupted Abyss (The Corrupted Abyss (Tamo-Loka))', 'The Corrupted Abyss (Tamo-Loka)'),
    ('The Clan Council (The Clan Council (Kul-Sabha))', 'The Clan Council (Kul-Sabha)'),
    ('The Provincial Assembly (The Provincial Assembly (Kshetra-Sabha))', 'The Provincial Assembly (Kshetra-Sabha)'),
    ('The Provincial Assemblies (The Provincial Assemblies (Kshetra-Sabhas))', 'The Provincial Assemblies (Kshetra-Sabhas)'),
    ('The White Couriers (Levitating Brass Carriages / The White Couriers (Levitating Brass Carriages / White Doot-Yānas))', 'The White Couriers (Levitating Brass Carriages / White Doot-Yānas)'),
    ('Inter-Realm Soul Requisition Writ (Inter-Realm Soul Requisition Writ (Ātma-Nirgama Patra))', 'Inter-Realm Soul Requisition Writ (Ātma-Nirgama Patra)'),
    ('Certificate of Completed Fate (Release Seal / Certificate of Completed Fate (Release Seal / Purna-Karma))', 'Certificate of Completed Fate (Release Seal / Purna-Karma)'),
    ('High Council Statutory Writs (High Council Statutory Writs (Vidhana-Patra))', 'High Council Statutory Writs (Vidhana-Patra)'),
    ('The 1,200-lb Ironclad Maul (The 1,200-lb Ironclad Maul)', 'The 1,200-lb Ironclad Maul'),
    ('The Phosphorus Saw-Wheel (The Phosphorus Saw-Wheel (यंत्र-चक्र))', 'The Phosphorus Saw-Wheel (यंत्र-चक्र)'),
    ('The Scales of Concord (The Scales of Concord (सत्य-दंडाची मुद्रा))', 'The Scales of Concord (सत्य-दंडाची मुद्रा)'),
    ('The Sun-Dagger (The Sun-Dagger (सूर्य-कट्यार))', 'The Sun-Dagger (सूर्य-कट्यार)'),
]

total_cleaned = 0
for fp in target_files:
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    orig = c
    for o, n in cleanups:
        if o in c:
            c = c.replace(o, n)
    if c != orig:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(c)
        total_cleaned += 1

print(f"Cleaned {total_cleaned} files.")
