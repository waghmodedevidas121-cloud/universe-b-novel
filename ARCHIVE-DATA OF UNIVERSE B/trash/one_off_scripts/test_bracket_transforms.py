import os
import re
import sys

# Standardize Character Active Arts and Arsenals into Clean Bracket Notation
# Based on Refinement 4 specifications and examples

bracket_transforms = {
    # CHR-HUM
    "CHR-HUM-01": {
        "arts": "[Administration: Sovereign Strategy & Civil Policy Formulation] [Non-Combat]",
        "ars": "[Signet: The Imperial Signet (साम्राज्य सुवर्ण मुद्रा)] & [Sidearm: .44 Concord Service Revolver]"
    },
    "CHR-HUM-02": {
        "arts": "[Diplomacy: Social Mediation, Civic Outreach & Education Governance] [Non-Combat]",
        "ars": "[Relic: Tapovana Deodar Silver Fountain Pen] & [Gear: Ancestral Gold Pocket Watch]"
    },
    "CHR-HUM-03": {
        "arts": "[Gale — Tier 2: Gale Blade], [Weapon — Tier 2: Iron Imbuement]",
        "ars": "[Ordnance: Drop-Lock Trench Carbine #7 (Double-Barrel Breach Aether-Carbine)] & [Melee: Brass-Hilted Cavalry Saber]"
    },
    "CHR-HUM-04": {
        "arts": "[Body — Tier 2: Iron Skin], [Weapon — Tier 2: Iron Imbuement]",
        "ars": "[Ordnance: 15mm Heavy Trench Anti-Materiel Rifle] & [Melee: Ironfang Trench Dagger]"
    },
    "CHR-HUM-05": {
        "arts": "[Jurisprudence: Constitutional Rta-Dharma Scholarship] [Non-Combat]",
        "ars": "[Document: Original Handwritten Kuru Constitution] & [Gear: Polished Teak Staff]"
    },
    "CHR-HUM-06": {
        "arts": "[Engineering: Register C Yantra Craft & Aether-Pressure Regulation] [Non-Combat]",
        "ars": "[Tool: Brass Slide-Rule, Pneumatic Pressure Gauge] & [Gear: Aetheric Spanner]"
    },
    "CHR-HUM-07": {
        "arts": "[Logistics: Rail Grid Operations & Acoustic Telegraph Wiring] [Non-Combat]",
        "ars": "[Tool: Junction Switchboard Keys] & [Gear: Precision Chronometer]"
    },
    "CHR-HUM-08": {
        "arts": "[Torrent — Tier 2: Ocean Current Navigation], [Weapon — Tier 2: Iron Imbuement]",
        "ars": "[Instrument: Prismatic Sextant] & [Sidearm: Saline-Aether Compression Pistol]"
    },
    "CHR-HUM-09": {
        "arts": "[Torrent — Tier 2: Wave Equilibrium], [Impact — Tier 2: Kinetic Rupture]",
        "ars": "[Ordnance: Ironfang Trench Dagger] & [Melee: Whalebone-Steel Double-Edged Cutlass]"
    },
    "CHR-HUM-10": {
        "arts": "[Sensory: Maritime Tempest Prediction & Magnetic Latitude Reading] [Non-Combat]",
        "ars": "[Instrument: Gyroscopic Brass Compass] & [Optics: Brass Telescopic Spyglass]"
    },
    "CHR-HUM-11": {
        "arts": "[Purification — Tier 2: Sub-Oceanic Curse Exorcism], [Alchemy — Tier 2: Poison Alchemy]",
        "ars": "[Gear: High-Pressure Oxygen Diving Suit, Brass Drill] & [Tool: Underwater Aether Torch]"
    },
    "CHR-HUM-12": {
        "arts": "[Shadow — Tier 2: Mist Concealment], [Life — Tier 2: Vitality Circulation]",
        "ars": "[Ordnance: Double-Barrel Trench Carbine] & [Gear: False-Bottom Smuggling Cargo Holds]"
    },
    "CHR-HUM-13": {
        "arts": "[Life — Tier 3: Soma Meridian Healing], [Barrier — Tier 3: Tapovana Sanctuary Ward], [Sensory — Tier 3: Truth-Sight]",
        "ars": "[Relic: Petrified Sal-Tree Sacred Staff] & [Artifact: Seed-Vault Key & Soma Kamandalu]"
    },
    "CHR-HUM-14": {
        "arts": "[Cosmology: Spatial Deformation Calculation, Astrophysics], [Mind — Tier 2: Will-Binding (Diplomatic Conciliation)] [Non-Combat]",
        "ars": "[Instrument: Brass Celestial Astrolabe] & [Archive: Concord Peace Treaty Parchment Register]"
    },
    "CHR-HUM-15": {
        "arts": "[Botanical: Flora Aether Cultivation & Spore-Fungus Research] [Non-Combat]",
        "ars": "[Tool: Glass Propagation Tubes] & [Melee: Copper Grafting Knife]"
    },

    # CHR-ASU
    "CHR-ASU-01": {
        "arts": "[Flame — Tier 3: Magma Control], [Body — Tier 3: Basalt Marrow]",
        "ars": "[Relic: The Tectonic Maul (Obsidian Sledge)] & [Gear: Hydraulic Brass Prosthetic Arm]"
    },
    "CHR-ASU-02": {
        "arts": "[Impact — Tier 3: Acoustic Resonance], [Sensory — Tier 3: Metallurgical Flaw Sight]",
        "ars": "[Tool: Asuran Tuning Fork] & [Relic: Vajra Calibration Rod]"
    },
    "CHR-ASU-03": {
        "arts": "[Body — Tier 3: Diamond Marrow], [Impact — Tier 3: Kinetic Rupture]",
        "ars": "[Ordnance: 80mm Riftbreaker Siege Howitzer] & [Melee: Heavy Iron Cleaver]"
    },
    "CHR-ASU-04": {
        "arts": "[Flame — Tier 3: Magma-Piston Overdrive], [Weapon — Tier 2: Iron Imbuement]",
        "ars": "[Ordnance: Drop-Lock Trench Carbine #7] & [Melee: Heavy Iron Spanner]"
    },
    "CHR-ASU-05": {
        "arts": "[Earth — Tier 3: Tectonic Resonator], [Body — Tier 3: Basalt Marrow]",
        "ars": "[Tool: Obsidian Core Drill] & [Melee: Heavy Ore-Breaker Sledge]"
    },
    "CHR-ASU-06": {
        "arts": "[Flame — Tier 2: Slag Smelting], [Weapon — Tier 2: Iron Imbuement]",
        "ars": "[Melee: Heavy Spiked Iron Mace (Foundry-Pattern)]"
    },
    "CHR-ASU-07": {
        "arts": "[Alchemy — Tier 2: Volcanic Gas Weaponization], [Body — Tier 2: Basalt Skin]",
        "ars": "[Gear: High-Pressure Sulfur Vapor Sprayer] & [Tool: Heavy Foundry Steel Pincers]"
    },
    "CHR-ASU-08": {
        "arts": "[Chemistry: Volcanic Sulfur Refining & Catalytic Synthesis] [Non-Combat]",
        "ars": "[Gear: Thermal Asbestos Gauntlets] & [Tool: Pressure-Rated Glass Distillation Flasks]"
    },
    "CHR-ASU-09": {
        "arts": "[Body — Tier 2: Iron Skin], [Mind — Tier 3: Sovereign Dread (Proletariat Resolve)]",
        "ars": "[Melee: Ironfang Trench Dagger (Notched)] & [Tool: Heavy Mining Pickaxe]"
    },
    "CHR-ASU-10": {
        "arts": "[Weapon — Tier 2: Blade Aura], [Weapon — Tier 2: Iron Imbuement]",
        "ars": "[Melee: Kuru-Asura Hybrid Double-Edged Steel Longsword] & [Ordnance: Drop-Lock Trench Carbine #7]"
    },
    "CHR-ASU-11": {
        "arts": "[Craft: Pranic Weapon-Engraving & Runic Inscription], [Weapon — Tier 2: Iron Imbuement]",
        "ars": "[Tool: Diamond-Tipped Graver] & [Tool: Precision Runic Chipping Hammer]"
    },
    "CHR-ASU-12": {
        "arts": "[Flame — Tier 2: Pyric Tempering], [Body — Tier 2: Basalt Skin]",
        "ars": "[Tool: Basalt Anvil, Heavy-Duty Brass Spanner] & [Instrument: Micro-Gyroscope Calibrator]"
    },
    "CHR-ASU-13": {
        "arts": "[Life — Tier 2: Tissue Regeneration], [Alchemy — Tier 2: Antidote Synthesis] [Non-Combat]",
        "ars": "[Gear: Brass Salve Containers, Sulfur Burn Paste] & [Relic: Matron Guardian Baton]"
    },
    "CHR-ASU-14": {
        "arts": "[Space — Tier 3: Spatial Distortion (Terrifying Presence)], [Body — Tier 4: Ancient Basalt Stasis]",
        "ars": "[Relic: Kaumodaki Fragment (Ancient Primal Maul)] & [Armor: Treta-Era Basalt Seal Plate]"
    },
    "CHR-ASU-15": {
        "arts": "[Body — Tier 3: Basalt Marrow], [Mind — Tier 3: Sovereign Dread]",
        "ars": "[Melee: Muktamukta Steel Chain-Whip]"
    },

    # CHR-DEV
    "CHR-DEV-01": {
        "arts": "[Solar — Tier 4: Sūryāstra], [Speed — Tier 3: Gale Step]",
        "ars": "[Relic: The Sun-Scepter (Solar Lance)] & [Armor: Prismatic Gold Cuirass]"
    },
    "CHR-DEV-02": {
        "arts": "[Solar — Tier 3: Prismatic Radiance], [Sensory — Tier 3: Cosmic Far-Hearing]",
        "ars": "[Relic: The Prismatic Javelin]"
    },
    "CHR-DEV-03": {
        "arts": "[Gale — Tier 4: Vāyavyāstra], [Speed — Tier 3: Gale Step]",
        "ars": "[Relic: Candrahāsa Blade (White Moonbeam Crescent)]"
    },
    "CHR-DEV-04": {
        "arts": "[Thunder — Tier 4: Vajra Resonance], [Speed — Tier 3: Sonic Stride]",
        "ars": "[Divine Relic: Vajra (Lightning Javelin)]"
    },
    "CHR-DEV-05": {
        "arts": "[Torrent — Tier 2: Cloud Navigation], [Sensory — Tier 2: Danger Instinct]",
        "ars": "[Relic: The Cloud-Goad] & [Instrument: Celestial Aetheric Compass]"
    },
    "CHR-DEV-06": {
        "arts": "[Mind — Tier 3: Sensory Mirage (Harmonic Resonance)], [Art: Celestial Gandharva Music]",
        "ars": "[Relic: Seven-Stringed Golden Veena]"
    },
    "CHR-DEV-07": {
        "arts": "[Purification — Tier 3: Curse Exorcism], [Barrier — Tier 3: Isolation Ward]",
        "ars": "[Artifact: Sacred Soma Vessel] & [Relic: Prismatic Crystal Scepter]"
    },
    "CHR-DEV-08": {
        "arts": "[Weapon — Tier 2: Flying Slash], [Solar — Tier 2: Solar Light Flare]",
        "ars": "[Armor: Golden Wing-Plate Armor] & [Relic: The Sun-Dagger (सूर्य-कट्यार)]"
    },
    "CHR-DEV-09": {
        "arts": "[Sensory — Tier 3: Truth-Sight], [Sensory — Tier 3: Cosmic Far-Hearing]",
        "ars": "[Artifact: Celestial Palm-Leaf Scroll] & [Tool: Sun-Gold Stylus]"
    },
    "CHR-DEV-10": {
        "arts": "[Barrier — Tier 2: Isolation Ward], [Barrier — Tier 2: Energy Siphon Ward]",
        "ars": "[Relic: Amaravati Octagonal Aegis Ring]"
    },

    # CHR-BST
    "CHR-BST-01": {
        "arts": "[Body — Tier 3: Gigantification (Mahima)], [Body — Tier 3: Basalt Marrow], [Earth — Tier 3: Tectonic Rupture], [Impact — Tier 3: Kinetic Rupture]",
        "ars": "[Natural: Four Calcified Stone Horns, 12-inch Diamond Claws] & [Defense: Primal Vajra Hide]"
    },
    "CHR-BST-02": {
        "arts": "[Binding — Tier 3: Nāgapāśa (500 psi Coil Constriction)], [Alchemy — Tier 3: Kālakūṭa Venom & Sanjeevani Dew], [Sensory — Tier 3: Telluric Far-Hearing]",
        "ars": "[Armor: Emerald-Scale Impenetrable Hide] & [Natural: 4-Foot Kālakūṭa Fangs & Nāgamaṇi]"
    },
    "CHR-BST-03": {
        "arts": "[Sky — Tier 3: Garuḍāstra Resonance (Golden Beak & Wing-Blades)], [Solar — Tier 3: Blinding Solar Flare], [Speed — Tier 3: Sonic Stride (Mach 2 Dive)]",
        "ars": "[Natural: Gold-Edged Feather Swords & Vajra Talons] & [Relic: Garuḍāstra Harmonics]"
    },
    "CHR-BST-04": {
        "arts": "[Gale — Tier 3: Vāyavyāstra Gale Blades], [Speed — Tier 3: Sonic Stride], [Sensory — Tier 2: Danger Instinct]",
        "ars": "[Natural: Iron-Hard Aerial Talons] & [Armor: Aerodynamic Feather Mantle]"
    },
    "CHR-BST-05": {
        "arts": "[Shadow — Tier 3: Shadow Weaving (Umbilical Slip)], [Speed — Tier 3: Gale Step (Spatial Fold)], [Sensory — Tier 3: Meridian Sight (Spatial Grain)]",
        "ars": "[Armor: Void-Pelt Camouflage Hide] & [Natural: Spatial-Rending Shadow Claws]"
    },
    "CHR-BST-06": {
        "arts": "[Body — Tier 3: Blood-Bone Vajra Frame], [Weapon — Tier 2: Iron Imbuement (Obsidian Fangs)], [Impact — Tier 2: Kinetic Rupture]",
        "ars": "[Natural: 18-Inch Obsidian Fangs, Bone-Crushing Jaws] & [Melee: Ironfang Trench Dagger]"
    },
    "CHR-BST-07": {
        "arts": "[Shadow — Tier 2: Shadow Weaving], [Archery — Tier 2: Blind-Ear Archery], [Sensory — Tier 3: Telluric Far-Hearing (Seismic Decryption)]",
        "ars": "[Weapon: Ancient Ironwood Bow & Venomed Arrows] & [Instrument: Titan-Resonance Bone Flute]"
    },
    "CHR-BST-08": {
        "arts": "[Body — Tier 3: Vajra Frame], [Life — Tier 3: Kaya-Kalpa Cellular Regeneration], [Barrier — Tier 3: Isolation Ward (Sanctuary Glade)]",
        "ars": "[Relic: Ancient Ironwood Staff] & [Artifact: Herbal Kamandalu & Abhaya Mudra]"
    },

    # CHR-CEN
    "CHR-CEN-01": {
        "arts": "[Mind — Tier 3: Will-Binding (Vashitva)], [Barrier — Tier 3: Isolation Ward]",
        "ars": "[Relic: The Concord Mace (Golden Gavel)]"
    },
    "CHR-CEN-02": {
        "arts": "[Finance: Central Reserve Ciphering, Macro-Bullion Valuation & Currency Arbitrage] [Non-Combat]",
        "ars": "[Key: Central Vault Master Keys] & [Ledger: Runic Reserve Ledger]"
    },
    "CHR-CEN-03": {
        "arts": "[Weapon — Tier 2: Iron Imbuement], [Impact — Tier 2: Kinetic Rupture]",
        "ars": "[Ordnance: Drop-Lock Trench Carbines #7 (Non-Lethal Kinetic Slugs)] & [Melee: Formal Officer Saber]"
    },
    "CHR-CEN-04": {
        "arts": "[Sensory — Tier 3: Truth-Sight], [Jurisprudence: Constitutional Inquest & Testimonial Verification]",
        "ars": "[Relic: The Scales of Concord (सत्य-दंडाची मुद्रा)] & [Codex: Kuru-Amaravati Legal Code]"
    },
    "CHR-CEN-05": {
        "arts": "[Thunder — Tier 2: Acoustic Telegraph Strike], [Sensory — Tier 2: Harmonic Far-Hearing]",
        "ars": "[Gear: Aetheric Telegraph Tap Key, Insulated Copper Gauntlets] & [Tool: Lead-Seal Anvil Hammer]"
    },
    "CHR-CEN-06": {
        "arts": "[Thunder — Tier 2: Signal Transmission], [Sensory — Tier 2: Wireline Frequency Reading]",
        "ars": "[Tool: Telegraph Tap Key, Brass Switching Plugs] & [Gear: Insulated Copper Gauntlets]"
    },
    "CHR-CEN-07": {
        "arts": "[Sensory — Tier 2: Meridian Sight (Contraband Detection)], [Intel: Manual Morse Code Decryption]",
        "ars": "[Gear: Brass Headset, Switchboard Key] & [Sidearm: Compact Aether Revolver]"
    },
    "CHR-CEN-08": {
        "arts": "[Speed — Tier 2: Sonic Stride (Laghima Pace)], [Speed — Tier 2: Gale Step]",
        "ars": "[Gear: Sealed Brass Dispatch Containers] & [Avian: Trained Peregrine Courier Falcon]"
    },

    # CHR-SET
    "CHR-SET-01": {
        "arts": "[Barrier — Tier 3: Isolation Ward], [Mind — Tier 3: Telepathy], [Scholarship: Classical Sanskrit Dialectics & Rta Science]",
        "ars": "[Relic: Petrified Black Runic Staff, Crystal Memory Plates] & [Seal: Academy Chancellor Signet]"
    },
    "CHR-SET-02": {
        "arts": "[Space — Tier 3: Dimensional Anchor (Lattice-Rail Track Lock)], [Body — Tier 2: Iron Skin]",
        "ars": "[Gear: Armored Locomotive Master Lever, Brass Whistle] & [Pass: High-Priority Transit Permit]"
    },
    "CHR-SET-03": {
        "arts": "[Earth — Tier 2: Tectonic Stabilization], [Barrier — Tier 2: Isolation Ward]",
        "ars": "[Tool: Basalt Bunker Manifold Tool, Siege Hammer] & [Gear: Anti-Void Shock Absorber Plates]"
    },
    "CHR-SET-04": {
        "arts": "[Sensory — Tier 3: Truth-Sight], [Astral — Tier 3: Soul-Sight], [Barrier — Tier 3: Isolation Ward]",
        "ars": "[Relic: The Auditor's Ledger & 24-Hour Red-Ink Seal]"
    },
    "CHR-SET-05": {
        "arts": "[Body — Tier 3: Vajra Marrow], [Strategy — Tier 3: Chakravyūha Tactical Formation], [Impact — Tier 3: Kinetic Rupture]",
        "ars": "[Divine Relic: Vajra (Lightning Javelin)] & [Relic: The Bastion Great-Mace]"
    },
    "CHR-SET-06": {
        "arts": "[Mind — Tier 3: Telepathy], [Space — Tier 3: Void Cleave], [Barrier — Tier 3: Isolation Ward]",
        "ars": "[Relic: Setu Academy Gold Scepter] & [Tool: Brass Rift-Calipers (ज्ञान-सूत्र मापक-काटे व दुर्बीण)]"
    },
    "CHR-SET-07": {
        "arts": "[Life — Tier 3: Cellular Rebirth (Arboricultural Prana Restoration)], [Alchemy — Tier 2: Poison Alchemy]",
        "ars": "[Relic: The Vitality Lancet (अमृत-शलाका)] & [Gear: Soil-Reading Lens & Sanjeevani Casket]"
    },
    "CHR-SET-08": {
        "arts": "[Sensory — Tier 3: Truth-Sight], [Forensics: Karmic Register Cross-Examination]",
        "ars": "[Archive: Red-Ink Ledger] & [Seal: Brass Inquest Seal]"
    },
    "CHR-SET-09": {
        "arts": "[Shadow — Tier 2: Shadow Weaving], [Sensory — Tier 2: Danger Instinct]",
        "ars": "[Melee: Shadow Blade (Envenomed Edge)] & [Ordnance: Suppressed Trench Carbine]"
    },
    "CHR-SET-10": {
        "arts": "[Barrier — Tier 2: Isolation Ward], [Earth — Tier 2: Basalt Rampart Shaping]",
        "ars": "[Defense: Massive Basalt Tower Shield] & [Weapon: Vajra Spear & Blast-Door Key]"
    },
    "CHR-SET-11": {
        "arts": "[Speed — Tier 2: Sonic Stride (Laghima)], [Weapon — Tier 2: Blade Aura], [Weapon — Tier 2: Iron Imbuement]",
        "ars": "[Melee: Ironfang Trench Dagger] & [Ordnance: Dual Drop-Lock Trench Carbines]"
    },
    "CHR-SET-12": {
        "arts": "[Engineering: Register C Yantra Craft], [Barrier — Tier 2: Isolation Ward], [Thunder — Tier 2: Lightning Strike]",
        "ars": "[Tool: Aetheric Calipers, Barrier Manifold Key] & [Gear: Insulated Copper Gauntlets]"
    },
    "CHR-SET-13": {
        "arts": "[Space — Tier 2: Sub-Space Navigation], [Body — Tier 2: Iron Skin], [Weapon — Tier 2: Iron Imbuement]",
        "ars": "[Gear: Pressurized Brass Gondola Harness, Void Compass] & [Ordnance: Drop-Lock Trench Carbine #7 (Sniper Model)]"
    },
    "CHR-SET-14": {
        "arts": "[Space — Tier 3: Dimensional Anchor (Gateway Lock)], [Sensory — Tier 3: Meridian Sight]",
        "ars": "[Key: Monolithic High Arch Master Key] & [Seal: Lawful Gatekeeper Seal]"
    },
    "CHR-SET-15": {
        "arts": "[Barrier — Tier 3: Isolation Ward], [Astral — Tier 3: Soul Anchor (Depository Intake Protocol)]",
        "ars": "[Relic: Floor D Quarantine Scepter] & [Seal: Stamped Brass Intake Seal ([STATUS: UNINDEXED / BLANK SLATE])]"
    },
    "CHR-SET-16": {
        "arts": "[Database: Chitragupta Register Synchronizer], [Astral — Tier 2: Soul-Sight]",
        "ars": "[Seal: Lekhya Bureau Official Seal, Copper Tablets] & [Optics: Prismatic Verification Lens]"
    },
    "CHR-SET-17": {
        "arts": "[Speed — Tier 3: Sonic Stride (Laghima)], [Speed — Tier 3: Gale Step], [Space — Tier 3: Sub-Space Conduit Slip]",
        "ars": "[Gear: Sealed Karmic Courier Pouch, Conduit Dock Master Key] & [Pass: High Transit Dispensation]"
    },

    # CHR-ABY
    "CHR-ABY-01": {
        "arts": "[Necrosis — Tier 3: Necrotic Rot], [Mind — Tier 3: Sovereign Dread]",
        "ars": "[Relic: The Phosphorus Saw-Wheel & The Black-Glass Blade] & [Relic: Atrophy Flame Scepter]"
    },
    "CHR-ABY-02": {
        "arts": "[Body — Tier 3: Vajra Marrow (Titan-Bone Plating)], [Impact — Tier 3: Kinetic Rupture]",
        "ars": "[Relic: The 1,200-lb Ironclad Maul] & [Armor: Heavy Riveted Boiler-Plate Harness]"
    },
    "CHR-ABY-03": {
        "arts": "[Morphology — Tier 3: Kāmarūpa Vidyā (Mutational Flesh-Welding)], [Alchemy — Tier 3: Poison Alchemy]",
        "ars": "[Tool: Organic Serum Lancets] & [Weapon: Corrosive Flesh-Cleaving Blades]"
    },
    "CHR-ABY-04": {
        "arts": "[Space — Tier 3: Void Cleave], [Shadow — Tier 2: Shadow Weaving]",
        "ars": "[Melee: Shadow Blade (Envenomed Edge)] & [Command: 60-Ton Armored Scrap-Crawler Rig]"
    },
    "CHR-ABY-05": {
        "arts": "[Ordnance: Scrap-Ordnance Rigging], [Flame — Tier 2: Slag Ignition], [Weapon — Tier 2: Iron Imbuement]",
        "ars": "[Ordnance: Modified Drop-Lock Trench Carbine, Scrap Shrapnel Grenades] & [Tool: Heavy Oxy-Aether Welding Torch]"
    },
    "CHR-ABY-06": {
        "arts": "[Morphology — Tier 3: Kāmarūpa Vidyā (Golden Deer Mirage)], [Shadow — Tier 2: Shadow Weaving], [Speed — Tier 2: Gale Step]",
        "ars": "[Vessel: Double-Bottom Smuggler Launch, Stolen Frequency Discs] & [Melee: Venomed Smuggler Cutlass]"
    },
    "CHR-ABY-07": {
        "arts": "[Divine: Rudra-Booned Inviolable Astra Warfare], [Body — Tier 4: Immortal Vajra Frame], [Mind — Tier 4: Sovereign Dread]",
        "ars": "[Relic: Rudra-Booned Immovable Iron War-Mace] & [Bond: Meteoric Cold-Iron Chains of the Seventh Seal]"
    },
    "CHR-ABY-08": {
        "arts": "[Sensory — Tier 3: Telluric Far-Hearing (Tectonic Crust Decryption)], [Sensory — Tier 3: Meridian Sight]",
        "ars": "[Natural: Abyssal Stone Beak, Cold-Iron Feather Pinions] & [Relic: Seventh Seal Iron Lock Sensor]"
    },

    # CHR-DIV
    "CHR-DIV-01": {
        "arts": "[Cosmic: Universal Will-Creation, Cosmic Law, Veda Invariants] [Above Axis B Ladder]",
        "ars": "[Primordial Astra: Brahmaśirāstra], [Primordial Astra: Brahmāṇḍāstra], [Divine Astra: Brahmāstra]"
    },
    "CHR-DIV-02": {
        "arts": "[Cosmic: Infinite Preservation, Singularity Apex Sanctuary, Dharma Protection] [Above Axis B Ladder]",
        "ars": "[Primordial Astra: Sudarśana Cakra], [Primordial Astra: Nārāyaṇāstra], [Divine Bow: Śārṅga], [Relic: Kaumodakī Mace]"
    },
    "CHR-DIV-03": {
        "arts": "[Cosmic: Mahāpralaya Tāṇḍava, Kālāgni Annihilation, Trinetra Dissolution] [Above Axis B Ladder]",
        "ars": "[Primordial Astra: Triśūla], [Primordial Astra: Pāśupatāstra], [Divine Bow: Pināka]"
    },
    "CHR-DIV-04": {
        "arts": "[Cosmic: Inviolable Read-Only Core, Universal Karmic Archive] [Inviolable]",
        "ars": "[System Core: Ananta Ledger (Immutable Truth of All Spheres)]"
    },
    "CHR-DIV-05": {
        "arts": "[Law: Dharmarāja Authority, Karmic Justice, Mortality Threshold], [Astral — Tier 4: Soul Binding]",
        "ars": "[Divine Relic: Yamadaṇḍa / Kāladaṇḍa (Mortality Scepter)] & [Relic: Pāśa (Soul-Noose)]"
    },
    "CHR-DIV-06": {
        "arts": "[Weaving: Prāṇa-Sūtra Fate Architecture, Karmic Bond Calibration], [Astral — Tier 3: Soul-Sight]",
        "ars": "[Relic: Golden Spindle of Destiny (प्राण-सूत्र सुवर्ण तकली)], [Tool: Karmic Lancet] & [Seal: Destiny Seal]"
    },
    "CHR-DIV-07": {
        "arts": "[Ledger: Chitragupta Master Database Archival & Karmic Inscription] [Administrative]",
        "ars": "[Relic: Chitragupta Gold Stylus] & [Archive: Prathamika Ledger of All Souls]"
    },
    "CHR-DIV-08": {
        "arts": "[Defense: Grand Aegis 360° Grid Synchronization, Spatial Perimeter Shielding], [Barrier — Tier 4: Isolation Ward]",
        "ars": "[Relic: The Aegis Scepter], [Seal: Bastion Seal] & [Codex: Pan-Astral Defense Code]"
    },
    "CHR-DIV-09": {
        "arts": "[Audit: Rta Adherence Enforcement, Forensic Anomaly Inquest], [Sensory — Tier 4: Truth-Sight]",
        "ars": "[Relic: The Inquisitor's Seal] & [Document: 24-Hour Red-Ink Audit Warrant]"
    },
    "CHR-DIV-10": {
        "arts": "[Physics: Dimensional Metaphysics, Energy Transduction, Crystal Matrix Engineering], [Space — Tier 3: Spatial Awareness]",
        "ars": "[Relic: Cosmic Anvil, Divine Graver] & [Scepter: Prime Seeker Staff]"
    },
    "CHR-DIV-11": {
        "arts": "[Governance: Universal Architecture & Demographic Regulation] [Administrative]",
        "ars": "[Relic: The Architect's Seal] & [Codex: Brahma-Jnana Statutes]"
    },
    "CHR-DIV-12": {
        "arts": "[Mobility: Tri-Realm Unrestricted Transit], [Sensory — Tier 4: Cosmic Far-Hearing]",
        "ars": "[Relic: Mahatī Vīṇā] & [Mantra: Narayana Resonance]"
    },
    "CHR-DIV-13": {
        "arts": "[Warfare: Operational Ansha Combat, Zero-Tolerance Dissolution] [Executive Sovereign]",
        "ars": "[Relic: Ansha-Triśūla] & [Relic: Mahakala Dissolution Staff]"
    },

    # CHR-ALN
    "CHR-ALN-01": {
        "arts": "[Industry: Aether-Pneumatics Printing, Investigative Journalism & Social Media Analysis] [Non-Combat]",
        "ars": "[Machinery: Aether-Pneumatic Rotary Printing Press], [Archive: Secret Dossier Vault] & [Sidearm: .32 Compact Pocket Derringer]"
    },
    "CHR-ALN-02": {
        "arts": "[Finance: Sovereign Credit Ratings, Inter-Realm Financial Arbitrage, Bond Brokerage] [Non-Combat]",
        "ars": "[Key: Central Reserve Bank Master Vault Key] & [Comms: Aetheric Cipher-Telegraph Transceiver]"
    },
    "CHR-ALN-03": {
        "arts": "[Engineering: Heavy Ballistics, Helical Rifling Lathes, Obsidian Metallurgy] [Non-Combat Engineering]",
        "ars": "[Ordnance: Adler-Pattern 105mm Breech-Loading Siege Cannon], [Tool: Micrometric Lathe Tools] & [Sidearm: .455 Heavy Self-Cocked Revolver]"
    },
    "CHR-ALN-04": {
        "arts": "[Optics: Geometric Refraction Optics, Solar Condensation Analysis, Lattice Mirrors] [Non-Combat]",
        "ars": "[Instrument: Heliostat Prismatic Survey Sextant], [Tool: Spectrometer Kit] & [Gear: Concealed Antidote Flask]"
    },
    "CHR-ALN-05": {
        "arts": "[Scavenging: Acoustic Frequency Tuning, Wireline Telegraph Tapping, Lockpicking & Smoke-Tactics] [Scavenger Arts]",
        "ars": "[Tool: High-Frequency Acoustic Tuning Fork, Setu Signal Jammer], [Sidearm: Dual .38 Heavy Hammerless Revolvers] & [Melee: Trench Knife]"
    },
    "CHR-ALN-06": {
        "arts": "[Secular: 21st-Century Mechanical Intuition (Levers, Hydraulics, Circuit Tear-Down; Zero Magic)] [Secular Mortal Intuition]",
        "ars": "[Tool: Heavy Pipe Wrench, Oil-Can] & [Talisman: Non-Functional Shattered Smartphone]"
    }
}

print(f"Total bracket transforms configured: {len(bracket_transforms)}")
