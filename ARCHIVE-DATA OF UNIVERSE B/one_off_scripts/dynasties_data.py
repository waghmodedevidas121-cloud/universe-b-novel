# -*- coding: utf-8 -*-
"""
Canonical Dynasties, Clans & Royal Families of Tier 3 (Astral Living Realm)
All terms, titles, cities, and lore strictly in English (Roman script).
Divided by Cosmic Eras and Sub-Realms.
"""

COSMIC_ERAS = [
    {
        "code": "ERA-1",
        "name": "Era 1: Satya Yuga (The Primordial Golden Age)",
        "tagline": "Satya & Treta Epochs • Primordial Solar/Lunar Foundations & Titan Beasts",
        "desc": "The unbroken cosmic era before the Sundering. The Kshira Sagara flowed directly through the Singularity Apex, nurturing god-kings, solar avatars, ancient Nagas, and primordial titans in timeless harmony."
    },
    {
        "code": "ERA-2",
        "name": "Era 2: Tretā Yuga (The Void Cataclysm)",
        "tagline": "The Ashvattha Fracture • Dimensional Collapse & Survival Redoubts",
        "desc": "Cosmic crisis when the cosmic tree fractured, opening spatial rifts to the Void. Dynasties survived by sealing themselves in volcanic magma redoubts (Vajra-Nagara), sacred ascetic groves (Tapovana), and weaving resonance barrier fabrics."
    },
    {
        "code": "ERA-3",
        "name": "Era 3: Dvāpara Yuga (The Great Partition)",
        "tagline": "The Four Quadrants Divided • Demilitarization & The Grand Concord",
        "desc": "The living cosmos was phase-shifted into five parallel pocket dimensions (Human, Asura, Deva, Beast, and Central City). The Grand Concord was signed, demilitarizing Central City, outlawing beast slavery via The Great Beast Accord, and opening deep mining cartels."
    },
    {
        "code": "ERA-4",
        "name": "Era 4: Kali Yuga (The Present Era of Shards & Dimensional Resonance)",
        "tagline": "Clean Aether-Dimensional Baseline • 3-Tier Demographics & 5% Aliens Diaspora",
        "desc": "The present era of asymmetric effort and clean Aether-Dimensional engineering: Grounded Beast-Carts, Resonance Needle grids, Tectonic Rotary Anchors, and Tapasya-Yantrika fusion. Mortals live across a true 4-bracket magic pyramid alongside a 5% Aliens minority diaspora. Zero computers, AI, microchips, coal smoke, or instant cheats."
    }
]

DYNASTIES = [
    # -------------------------------------------------------------------------
    # ERA 1 FOUNDATIONS (Ancient Primordial Dynasties surviving into Era 4)
    # -------------------------------------------------------------------------
    {
        "id": "dyn-aditya",
        "name_en": "Aditya Solar Imperial Dynasty",
        "name_formal": "The Solar Throne of Golden Amaravati",
        "origin_era_code": "ERA-1",
        "origin_era_name": "Era 1: Primordial Solar Lineage",
        "current_status_era": "Era 4: Sovereign Celestial Hegemony",
        "sub_realm": "Deva Sub-Realm (Celestial Heights)",
        "sub_realm_code": "DEV",
        "badge": "Solar Imperial Aristocracy",
        "color": "#f43f5e",
        "accent_bg": "rgba(244, 63, 94, 0.12)",
        "crest": "☀️",
        "seat": "Amaravati Floating Cloud-Plateau & Solar Spire",
        "capital": "Amaravati",
        "government": "Imperial Solar Bench with Dharmic High Court",
        "motto": "Rtasya Pantham Na Jahati • Truth & Cosmic Order Above the Clouds",
        "founding_era": "Era 1: The Primordial Golden Age",
        "primary_race": "Devas (Golden-haloed celestial immortals sustained by Solar Amrita)",
        "economic_pillars": "Refined Celestial Aether Crystals, Solar Prism Collectors, Celestial Marble, Astrological Observatories",
        "tech_level": "Zero Combustion / Pure Celestial Prismatic (Prism Mirrors, Frictionless Cloud-Gliders, Cosmic Astrolabes; Strictly Prohibits Coal & Steam Smog)",
        "history": """
            The Aditya Dynasty traces its lineage to the primordial Sun deity at the dawn of the cosmos in Era 1. Bhanu, The Solar Sovereign and Queen Savitri rule from the golden spires of Amaravati, suspended upon perpetual cloud plateaus above the mortal sky.
            
            Having survived the Void Cataclysm of Era 2 by raising solar prismatic shields, the Devas maintained their pristine isolation through Era 3's Great Partition. In the present Era 4: Kali Yuga, the Aditya Dynasty fiercely enforces a zero-smog mandate across its airspace, looking down with disdain upon mortal industry while privately worrying about the rapid militarization of human and Asuran dimensional artillery.
        """,
        "culture_and_laws": """
            - Zero Smog Mandate: Combustion boilers, industrial emissions, and heavy machinery are strictly illegal within Deva territorial boundaries under penalty of immediate atmospheric expulsion.
            - Cosmic Stewardship: Devas view themselves as the eternal custodians of cosmic order (Rta), creating a patronizing aristocratic rift with mortal humans and industrial Asuras.
            - Prismatic Navigation: All transport is conducted via frictionless solar gliders and wind slipstreams directed by celestial navigators.
        """,
        "era_timeline": {
            "era_1": "Reigned as the supreme solar rulers over an undivided golden universe; worshipped as guardians of universal light.",
            "era_2": "Erected the Solar Aegis over Amaravati, reflecting void anomalies back into outer space during the cataclysm.",
            "era_3": "Secured the northern celestial quadrant during the Great Partition, demilitarizing direct surface occupation.",
            "era_4": "Monopolizes celestial crystal refining; engages in economic and diplomatic cold war against Asuran industrialization."
        },
        "geopolitical_relations": {
            "allies": ["Grand Concord Judicial Directorate in Central City", "Soma-Vansh & Gandharva-Puri Harmonic Guilds"],
            "rivals": ["Maya Dynasty (Hostility over Asuran industrial emissions encroaching upon celestial cloud buffers)", "Hastinapur Industrial League"],
            "grudges": ["Ancient Vedic grudges against Asuran Chthonic clans dating back to the Churning of the Ocean"],
            "trade_dependencies": ["Exports pure refined crystalline aether; imports ceremonial aether-silk and precision astrolabes"]
        },
        "character_ids": [
            "CHR-DEV-01", "CHR-DEV-02", "CHR-DEV-03", "CHR-DEV-04", 
            "CHR-DEV-05", "CHR-DEV-06", "CHR-DEV-09", "CHR-DEV-10"
        ]
    },
    {
        "id": "dyn-bharata",
        "name_en": "Bharata Dynasty & Kuru-Panchala League",
        "name_formal": "The Royal House of Hastinapur & Mortal Council",
        "origin_era_code": "ERA-1",
        "origin_era_name": "Era 1: Ancient Lunar Vamsha (Rebuilt in Era 4)",
        "current_status_era": "Era 4: Constitutional Industrial Monarchy",
        "sub_realm": "Human Sub-Realm (Mortal Cradle)",
        "sub_realm_code": "HUM",
        "badge": "Ruling Royal Dynasty",
        "color": "#06b6d4",
        "accent_bg": "rgba(6, 182, 212, 0.12)",
        "crest": "👑",
        "seat": "Hastinapur Grand Spire & Grand Mahā-Dvāra Plaza",
        "capital": "Hastinapur",
        "government": "Constitutional Monarchy with Imperial Privy Council & Worker Assembly",
        "motto": "Dharmo Rakshati Rakshitah • Law & Vedic Archery Shield the Mortal Realm",
        "founding_era": "Era 1: The Primordial Golden Age (Reformed in Era 4)",
        "primary_race": "Human Mortal (True 4-Bracket Magic Pyramid: Bracket 1: 0-60% Ember Magic, Bracket 2: 60-80% D-Rank Active Magic, Bracket 3: 80-90% C-Rank Reincarnates, Bracket 4: 90-100% Vanguard Elites)",
        "economic_pillars": "Beast-Cart & Chariot Construction, River Plain Agriculture, Runic Forges, Textile Mills",
        "tech_level": "Vedic High-Fantasy & Runic Craft (Grounded Beast-Carts, Dhanurveda, Runic Blades, Acoustic Mantra-Stones, Tectonic Rotary Anchors; Zero 19th-C. Firearms, Railways, Steam, or AI/Electronics)",
        "history": """
            The Bharata Dynasty originates in the ancient Lunar Lineage (Chandra-Vamsha) and Emperor Bharata in Era 1. After catastrophic devastation in the ancient Kurukshetra war and enduring the Void Cataclysm of Era 2, the human mortal cradle was phase-shifted into its own pocket dimension during Era 3's Great Partition.
            
            Recognizing their mortal biological limits, King Parikshit and Queen Madravati led an unprecedented transformation in Era 4: Kali Yuga. Refusing to rely on passive hermits or divine miracles, Hastinapur pioneered runic engineering, Beast-Cart highways, acoustic mantra grids, and Dhanurveda infantry formations, turning Hastinapur into the bastion of human self-reliance with a 5% Aliens borough.
        """,
        "culture_and_laws": """
            - The Great Beast Accord Enforcement: Human slavery and animal exploitation are capital crimes under Hastinapur constitutional code.
            - Public Welfare & Education: Queen Madravati instituted mandatory primary schooling for factory children and mobile medical clinics.
            - Mortal Resilience: Embracing the True 4-Bracket magic reality where everyone possesses elemental ember magic or quirks, disciplined runic formations and Dhanurveda archery allow humans to stand toe-to-toe with gods and demons.
        """,
        "era_timeline": {
            "era_1": "Sacred kingship ruling the fertile plains of Kurukshetra; high Vedic ritualism and chariot warfare.",
            "era_2": "Hastinapur walls sheltered millions of fleeing mortal refugees during spatial tearing events.",
            "era_3": "Realized mortal biological fragility in a partitioned realm; signed treaties with Central City.",
            "era_4": "Pioneered the Vedic High-Fantasy renaissance: established grand highways for Beast-Carts and forged master runic bows and blades."
        },
        "geopolitical_relations": {
            "allies": ["Northern Tapovana Hermitage (Spiritual alliance)", "Grand Concord Directorate in Central City"],
            "rivals": ["Maya Dynasty (Technological cold war)", "Aditya Solar Dynasty (Tariff friction over expansion)"],
            "grudges": ["Historical border skirmishes with Asuran ballistas; 30-year wound on King Parikshit"],
            "trade_dependencies": ["Imports obsidian armor plates and Vajra-steel from Asuras; exports river grain and agricultural surplus"]
        },
        "character_ids": [
            "CHR-HUM-01", "CHR-HUM-02", "CHR-HUM-03", "CHR-HUM-04", 
            "CHR-HUM-05", "CHR-HUM-06", "CHR-HUM-07"
        ]
    },
    {
        "id": "dyn-ursine",
        "name_en": "Vajra-Bhalluka Ursine Clan",
        "name_formal": "The Iron-Bone Titan Sovereigns of Shaila-Kuta",
        "origin_era_code": "ERA-1",
        "origin_era_name": "Era 1: Primordial Titan Age",
        "current_status_era": "Era 4: Primeval Territorial Guardians",
        "sub_realm": "Beast Sub-Realm (Primeval Expanse)",
        "sub_realm_code": "BST",
        "badge": "Armored Titan Vanguard",
        "color": "#10b981",
        "accent_bg": "rgba(16, 185, 129, 0.12)",
        "crest": "🐻",
        "seat": "Shaila-Kuta Granite Ridge & Primordial Cave Spire",
        "capital": "Shaila-Kuta",
        "government": "Titan Elder Matriarchy & Alpha Chieftain Council",
        "motto": "Achalo Ham Vajrakayah • Immovable as the Mountain, Iron-Bones of the Earth",
        "founding_era": "Era 1: The Primordial Golden Age",
        "primary_race": "Ursine Divine Beasts (Calcified iron-dense bone & basalt fur)",
        "economic_pillars": "Territorial Hardwood Lumber, Underground Root Honey, Seismic Geological Crystals",
        "tech_level": "Zero Technology / Pure Primordial Bio-Armor (Living Vajra-Deha, Calcified Horns, Kinetic Shockwave Strikes)",
        "history": """
            The Vajra-Bhalluka Clan is the most ancient titan beast lineage in the Beast Sub-Realm, dating back to Era 1. Led by Jambavan, "Old Four-Horns", a 25-foot four-horned mountain bear with calcified stone-bone plating, this clan has guarded the primeval canopy for centuries.
            
            They care nothing for human parliamentary politics, Asuran aether-chambers, or Deva celestial chimes. Their sole mandate is enforcing the territorial sanctity of the deep forest under The Great Beast Accord, crushing any illegal poachers or loggers with seismic shockwaves.
        """,
        "culture_and_laws": """
            - Absolute Forest Sanctity: Unauthorized felling of ancient world-trees or trapping living beasts is punishable by instant crushing.
            - Meditative Hibernation: Jambavan remains in deep hibernation for seasons at a time, awakening only when regional boundaries are breached.
            - Shaman Bridge: Sage Matanga serves as their sole designated voice to human settlement leagues.
        """,
        "era_timeline": {
            "era_1": "Roamed the boundless primordial world before continental divisions occurred.",
            "era_2": "Sheltered smaller beast species within underground basalt caves during the Void Cataclysm.",
            "era_3": "Ratified The Great Beast Accord with Central City, banning beast trafficking across all sub-realms.",
            "era_4": "Repels human timber and mining expeditions attempting to cut logging corridors through the primeval canopy."
        },
        "geopolitical_relations": {
            "allies": ["Shabari, \"The Bone-Speaker\" (Diplomatic envoy to Central City)", "Nagavanshi Brood of Bhogavati"],
            "rivals": ["Human Timber Prospectors", "Asuran Sulfur Prospectors"],
            "grudges": ["Fierce vendetta against black-market beast traders and captive fighting pits"],
            "trade_dependencies": ["Zero; entirely self-reliant upon natural primeval jungle bounty"]
        },
        "character_ids": [
            "CHR-BST-01", "CHR-BST-08"
        ]
    },
    {
        "id": "dyn-naga",
        "name_en": "Nagavanshi Serpent Dominion",
        "name_formal": "The Brood Council of Sunken Bhogavati",
        "origin_era_code": "ERA-1",
        "origin_era_name": "Era 1: Primordial Patala Lineage",
        "current_status_era": "Era 4: Subterranean Memory & Venom Lords",
        "sub_realm": "Beast Sub-Realm (Primeval Expanse)",
        "sub_realm_code": "BST",
        "badge": "Subterranean Venom & Memory Lords",
        "color": "#059669",
        "accent_bg": "rgba(5, 150, 105, 0.12)",
        "crest": "🐍",
        "seat": "Bhogavati Subterranean Waterways & World-Tree Roots",
        "capital": "Bhogavati",
        "government": "Matriarchal Serpent Brood Council",
        "motto": "Smrtya Vishena Cha Jivyate • In Ancient Memory and Deadly Venom, We Rule Below",
        "founding_era": "Era 1: The Primordial Golden Age",
        "primary_race": "Nagas, Colossal Vipers & Amphibious Venom-Lords",
        "economic_pillars": "Rare Neurotoxins, Cellular Rejuvenation Nectar, Deep Jade, Bioluminescent Fungi",
        "tech_level": "Biological & Alchemical Sovereignty (Venom-Spore Distillation, Living Root Networks; Zero Machinery)",
        "history": """
            Bhogavati is a vast subterranean metropolis of flooded grottoes and entangled world-tree roots beneath the Beast Sub-Realm. Kadru, "The Jade Coil", a 180-foot emerald-scaled sovereign, governs this ancient realm of racial memories and deadly toxins.
            
            Dating back to the earliest Era 1 subterranean clans, the Nagavanshis hold deep genetic memories of the cosmic past. Their venom glands produce both lethal paralytics and miraculous cellular rejuvenation serums. A historic peace treaty brokered by Envoy Astika preserves an unbroken friendship between Bhogavati and Northern Tapovana.
        """,
        "culture_and_laws": """
            - Genetic Memory: Ancestral histories and grudges are passed down through bloodlines; an offense against a Naga ancestor is never forgotten.
            - Subterranean Sovereignty: Regardless of who claims the surface, the subterranean aquifers and tree roots remain sovereign Naga territory.
        """,
        "era_timeline": {
            "era_1": "Dwelled in the deepest underground realms of Patala, guarding cosmic treasures.",
            "era_2": "Burrowed into seismic roots to survive surface void tears during the cataclysm.",
            "era_3": "Signed the non-aggression peace accord with Envoy Astika, ending surface serpent wars.",
            "era_4": "Trades life-saving cellular serums to Tapovana while guarding underground aquifers from Asura deep drills."
        },
        "geopolitical_relations": {
            "allies": ["Northern Tapovana Hermitage (Astika peace brotherhood)", "Vajra-Bhalluka Ursine Clan"],
            "rivals": ["Suparna Avian Royal House (Ancient predator-prey cold truce)", "Asura Deep-Bore Drillers"],
            "grudges": ["Ancestral grievance over human serpent-sacrifice rituals in ancient historical epochs"],
            "trade_dependencies": ["Supplies rare regenerative nectar to Tapovana in exchange for medicinal seeds"]
        },
        "character_ids": [
            "CHR-BST-02"
        ]
    },
    {
        "id": "dyn-suparna",
        "name_en": "Suparna Avian Royal House",
        "name_formal": "The High Sky Eyrie of Khaga-Shikhara",
        "origin_era_code": "ERA-1",
        "origin_era_name": "Era 1: Primordial Garuda Bloodline",
        "current_status_era": "Era 4: High Apex Sky Sovereigns",
        "sub_realm": "Beast Sub-Realm (Primeval Expanse)",
        "sub_realm_code": "BST",
        "badge": "High Apex Sky Predators",
        "color": "#34d399",
        "accent_bg": "rgba(52, 211, 153, 0.12)",
        "crest": "🦅",
        "seat": "Khaga-Shikhara Granite Needles & High Cloud Eyrie",
        "capital": "Khaga-Shikhara",
        "government": "High Aerial Eyrie Council & Wing-Warriors Assembly",
        "motto": "Pakshair Vidaryate Nabhah • With Golden Pinions, We Cleave the Firmament",
        "founding_era": "Era 1: The Primordial Golden Age",
        "primary_race": "Suparna Divine Birds, Great Eagles & Falcon-Lords",
        "economic_pillars": "High-Atmosphere Scouting, Wind Crystals, Spatial Slipstream Navigation",
        "tech_level": "Biological Aerodynamics (Supersonic Dive, Wing-Blade Shockwaves, Golden Feathers; Zero Machinery)",
        "history": """
            Khaga-Shikhara consists of soaring granite needle spires piercing the clouds in the western Beast Sub-Realm. Vinata, "The Golden Maw" and Sampati, "Iron-Talon" lead this noble race of golden-winged raptors possessing 80-foot wingspans.
            
            Originating in Era 1 as descendants of Garuda, they patrol the upper stratosphere separating the Beast Sub-Realm from the Aetheric Spatial Void. While ancient instincts pit them against the subterranean Nagas, modern treaties mediated by Central City keep their rivalry locked in an armed peace.
        """,
        "culture_and_laws": """
            - Skyborne Sovereignty: Setting foot upon the earth is considered undignified for royal eagles; all councils occur on granite pinnacles.
            - Supersonic Vigilance: Young scouts are trained to dive at Mach 2 speeds to intercept unauthorized aircraft or void anomalies.
        """,
        "era_timeline": {
            "era_1": "Ruled the high heavens as aerial champions during the dawn of the cosmos.",
            "era_2": "Flew high-altitude reconnaissance missions to guide allied survivors around void ruptures.",
            "era_3": "Agreed to demilitarized flight corridors under the Grand Concord charter.",
            "era_4": "Patrols outer rim atmospheres against Corrupted Realm incursions; monitors Deva solar gliders."
        },
        "geopolitical_relations": {
            "allies": ["Central City Outer Rim Air Patrol Division"],
            "rivals": ["Deva Solar Aeronauts (Jurisdictional friction over upper corridor flight paths)", "Nagavanshis (Ancestral instinctive truce)"],
            "grudges": ["Deep hatred of ground-based anti-air flak cannons and wire traps"],
            "trade_dependencies": ["Harvests atmospheric wind crystals used in precision chronometers"]
        },
        "character_ids": [
            "CHR-BST-03", "CHR-BST-04"
        ]
    },

    # -------------------------------------------------------------------------
    # ERA 2 SURVIVOR REDOUBTS (Forged during the Void Cataclysm)
    # -------------------------------------------------------------------------
    {
        "id": "dyn-maya",
        "name_en": "Maya Dynasty & Danava Foundry League",
        "name_formal": "The Magma-Citadel of Vajra-Nagara",
        "origin_era_code": "ERA-2",
        "origin_era_name": "Era 2: Void Cataclysm Magma Redoubt",
        "current_status_era": "Era 4: Technocratic Heavy Foundry Monarchy",
        "sub_realm": "Asura Sub-Realm (Chthonic Foundries)",
        "sub_realm_code": "ASU",
        "badge": "Technocratic Magma-Monarchy",
        "color": "#f59e0b",
        "accent_bg": "rgba(245, 158, 11, 0.12)",
        "crest": "🌋",
        "seat": "Vajra-Nagara Iron Citadel & Geothermal Heart",
        "capital": "Vajra-Nagara",
        "government": "Meritocratic Technocracy governed by The Forge Trials (The Forge Trials (Yantra-Pariksha) / Furnace Trials)",
        "motto": "Lohena Dharyate Vishvam • By Molten Vajra-Steel and Resonance, We Endure",
        "founding_era": "Era 2: The Void Cataclysm",
        "primary_race": "Asura / Danava (High bone density, sulfur-tolerant biology)",
        "economic_pillars": "Ultra-Heavy Metallurgy, Runic Ratha & Cart Plating, Heavy Slag-Ballistas, Hydraulic Prosthetics, High-Density Alloys",
        "tech_level": "Peak Chthonic Mechanical & Magma Foundry (Cast-Steel Chambers, High-Pressure Valves, Acoustic Resonance Drills, Runic Smelting; Absolutely Zero Microchips or Digital Screens)",
        "history": """
            Grand Architect Maya is revered as the greatest mechanical mind in the cosmos. When the Void Cataclysm of Era 2 ruptured the firmament, Maya channeled subterranean basalt and volcanic magma to erect the impregnable fortress of Vajra-Nagara. Together with Forge-Queen Mandor, they converted warlike Asuran clans into a disciplined industrial technocracy.
            
            Leadership in the Maya Dynasty is never inherited; it must be won through the The Forge Trials (Yantra-Pariksha)—a rigorous examination in thermodynamics, metallurgy, and runic mechanics. Today, Vajra-Nagara is the heavy metallurgical core of Tier 3, producing double-plated armored Ratha chassis and heavy siege ballistas under Marshal Lauhini, "The Siege-Breaker" and General Prahasa.
        """,
        "culture_and_laws": """
            - Merit of the Furnace: Social status is determined by runic and metallurgical skill; whoever can forge a flawless runic basalt plate earns civic honor.
            - Veteran Rehabilitation: Artisan Kshema engineers hydraulic brass prosthetics free of charge for miners and soldiers injured in deep magma excavations.
            - Defensive Pragmatism: Prefers industrial trade over war, viewing combat as an unnecessary waste of refined steel and kinetic force.
        """,
        "era_timeline": {
            "era_1": "Ancient Danava artisans practicing primal masonry and underground architecture.",
            "era_2": "Architect Maya forged Vajra-Nagara as a subterranean magma sanctuary during the Void Cataclysm.",
            "era_3": "Established the meritocratic The Forge Trials (Yantra-Pariksha) and built the first aether-hydraulic mine hoists.",
            "era_4": "Manufactures heavy Ratha & Cart armor plating, runic siege ballistas, and obsidian high-pressure runic cores."
        },
        "geopolitical_relations": {
            "allies": ["Hastinapur Industrial Guilds (Secret engineering correspondence between Maya & Rohini-Bai)"],
            "rivals": ["Aditya Solar Dynasty (Disdain for Deva celestial arrogance)", "Deep Basin Mining Barons (Labor quota friction)"],
            "grudges": ["Bitterness over casualties in Era 3 border wars; wary of Deva aerial raids"],
            "trade_dependencies": ["Exports heavy alloy plating and runic weapon cores; depends on mortal river plains for food supplies"]
        },
        "character_ids": [
            "CHR-ASU-01", "CHR-ASU-02", "CHR-ASU-03", "CHR-ASU-04", 
            "CHR-ASU-10", "CHR-ASU-11", "CHR-ASU-12", "CHR-ASU-13", "CHR-ASU-14"
        ]
    },
    {
        "id": "dyn-tapovana",
        "name_en": "Northern Tapovana Hermitage & Sage Order",
        "name_formal": "The Sacred Council of Tapovana Hermitage",
        "origin_era_code": "ERA-2",
        "origin_era_name": "Era 2: Void Cataclysm Sacred Sanctuary",
        "current_status_era": "Era 4: Monastic Botanical Sanctuary & Neutral Arbiter",
        "sub_realm": "Human Sub-Realm (Mortal Cradle)",
        "sub_realm_code": "HUM",
        "badge": "Sacred Vedic Hermitage",
        "color": "#10b981",
        "accent_bg": "rgba(16, 185, 129, 0.12)",
        "crest": "🌿",
        "seat": "Shal-Grove Valley & Sacred Botanical Sanctum",
        "capital": "Tapovana Hermitage",
        "government": "Council of Vedic Sages (Guru-Shishya Monastic Assembly)",
        "motto": "Shamena Labhyate Shantih • In Pure Silence, Prana Sustains the Cosmos",
        "founding_era": "Era 2: The Void Cataclysm",
        "primary_race": "Human Rishis, Hybrid Ascetics & Botanical Scholars",
        "economic_pillars": "Rare Ayurvedic Formulations, Anti-Venom Spores, Celestial Herb Farming, Spiritual Mediation",
        "tech_level": "Zero Machinery (Strict Prohibition on Machinery & Smog; Pure Herbal Alchemy, Astrolabes, and Pranayama Resonance)",
        "history": """
            Tapovana Hermitage is the most revered spiritual sanctuary in the mortal world. During the Era 2 Void Cataclysm, Maharshi Shamika sealed the sacred Shal-groves behind an inviolable vow of non-violence (Ahimsa), shielding pristine flora and living seed banks from toxic fallout.
            
            In Era 3, Envoy Astika formulated the monumental peace pact ending hostilities between serpents, Asuras, and humans. In Era 4: Kali Yuga, Tapovana remains completely free of machinery, operating free herbal sanatoriums where botanists like Ila cure metal-dust lung ailments and physical strain.
        """,
        "culture_and_laws": """
            - Absolute Ahimsa: Drawing weapons, cutting sacred Shal trees, or discharging firearms within Tapovana carries instant banishment.
            - Free Healing: Medical aid is rendered universally to humans, Asuras, and beasts alike without monetary fees.
        """,
        "era_timeline": {
            "era_1": "Ancient forest hermitages where Rishis communed directly with the Kshira Sagara and taught royal disciples.",
            "era_2": "Maharshi Shamika sealed the sacred Shal-groves with Ahimsa vows to protect living seed banks from void fallout.",
            "era_3": "Acharya Astika negotiated the historic non-aggression concordat between Serpents, Asuras, and Humans.",
            "era_4": "Operates free herbal clinics treating metal-dust ailments and fatigue; strictly bans machinery."
        },
        "geopolitical_relations": {
            "allies": ["Queen Madravati's Welfare Council", "Nagavanshi Serpent Brood (Eternal peace pact via Astika)", "Central City Peace Council"],
            "rivals": ["Aggressive developers who attempt to clear forest tracts for mining and expansion"],
            "grudges": ["Deep grief over ecological encroachment from Asura and Human industrial basins"],
            "trade_dependencies": ["Self-sufficient; provides miracle healing tinctures in exchange for zero interference"]
        },
        "character_ids": [
            "CHR-HUM-13", "CHR-HUM-14", "CHR-HUM-15"
        ]
    },
    {
        "id": "dyn-soma",
        "name_en": "Soma-Vansh & Gandharva Harmonic Guilds",
        "name_formal": "The Harmonic Assembly of Gandharva-Puri",
        "origin_era_code": "ERA-2",
        "origin_era_name": "Era 2: Void Cataclysm Resonance Weaving",
        "current_status_era": "Era 4: Autonomous Acoustic Silk Guild",
        "sub_realm": "Deva Sub-Realm (Celestial Heights)",
        "sub_realm_code": "DEV",
        "badge": "Harmonic Weavers & Lunar Aristocracy",
        "color": "#e879f9",
        "accent_bg": "rgba(232, 121, 249, 0.12)",
        "crest": "🌙",
        "seat": "Gandharva-Puri Cloud-Terraces & Resonance Looms",
        "capital": "Gandharva-Puri",
        "government": "Autonomous Artisan Assembly under Soma-Vansh Patronage",
        "motto": "Nadena Vyajyate Rupam • From Sacred Resonance, Form is Woven",
        "founding_era": "Era 2: The Void Cataclysm",
        "primary_race": "Gandharvas, Kinnaras & Celestial Artisans",
        "economic_pillars": "Aether-Silk Weaving, Harmonic Resonance Instruments, Ballistic Tapestries, Cultural Arts",
        "tech_level": "Acoustic Resonance Engineering (Harmonic Looms, Sound-Fiber Spinners, Frequency Tuners; Strictly Zero Electronics)",
        "history": """
            Perched upon serene iridescent clouds east of Amaravati, Gandharva-Puri was established in Era 2 when celestial musicians discovered that specific harmonic frequencies could knit shattered spatial fabrics together. Lady Chitralekha and Master Weaver Julian perfected this craft into the art of Aether-Silk.
            
            By spinning sound waves into physical threads, they produce lightweight garments capable of deflecting supersonic kinetic arrows and sharp astra shrapnel. Kings of Hastinapur and Asuran marshals alike pay fortunes in gold to purchase these puncture-proof vestments, granting Gandharva-Puri profound diplomatic immunity.
        """,
        "culture_and_laws": """
            - Symphonic Governance: Community disputes are resolved through musical resonance and harmonic consensus rather than adversarial trials.
            - Protection of the Craft: The exact acoustic formulas used to spin Aether-Silk are guarded as sacred state secrets.
        """,
        "era_timeline": {
            "era_1": "Celestial bards and court musicians performing sacred hymns in the unbroken cosmos.",
            "era_2": "Discovered that harmonic acoustic vibrations could stabilize dimensional rifts during the cataclysm.",
            "era_3": "Chartered as an autonomous guild under the Soma-Vansh, supplying protective garments across all sub-realms.",
            "era_4": "Manufactures master protective Aether-Silk vestments sought after by military commanders across all five quadrants."
        },
        "geopolitical_relations": {
            "allies": ["Aditya Solar Throne (Patronage)", "Queen Madravati's Cultural Centers"],
            "rivals": ["Black-market counterfeit syndicates attempting to duplicate Aether-Silk"],
            "grudges": ["None; maintains absolute artistic and commercial neutrality"],
            "trade_dependencies": ["Supplies protective robes across all sub-realms in exchange for celestial gold"]
        },
        "character_ids": [
            "CHR-DEV-07", "CHR-DEV-08"
        ]
    },

    # -------------------------------------------------------------------------
    # ERA 3 FOUNDATIONS (Formed during the Great Partition & Cold Peace)
    # -------------------------------------------------------------------------
    {
        "id": "dyn-concord",
        "name_en": "Grand Concord Directorate & Apex Neutral Guilds",
        "name_formal": "The Supreme Demilitarized Directorate of Central City",
        "origin_era_code": "ERA-3",
        "origin_era_name": "Era 3: The Great Partition Neutral Sovereign",
        "current_status_era": "Era 4: Demilitarized Global Arbiter & Central Bank",
        "sub_realm": "Central Sub-Realm (Central City)",
        "sub_realm_code": "CEN",
        "badge": "Neutral Demilitarized Apex Directorate",
        "color": "#a855f7",
        "accent_bg": "rgba(168, 85, 247, 0.12)",
        "crest": "⚖️",
        "seat": "Grand Concord Rotunda, The Central Reserve Bank Vaults (The Central Reserve Bank (Akash-Kosha)) & Central Mantra-Stone Spire",
        "capital": "Central City",
        "government": "Multinational Demilitarized Directorate, Supreme Judiciary & Autonomous Guild Presidium",
        "motto": "Satyameva Jayate Nanrtam • Truth, Sound Ledger, and Balanced Peace",
        "founding_era": "Era 3: The Great Partition",
        "primary_race": "Cosmopolitan Multi-Species Neutral Citizens (Human, Asura, Deva, Beast Scholars)",
        "economic_pillars": "Aether-Rupee Reserve Currency, Global Central Banking, Mantra-Stone Exchange Network, Neutral Arbitration, Historical Archives",
        "tech_level": "Vedic Precision Mechanical & Acoustic Mantra Communications (Acoustic Resonance Arrays, Stone Presses, Steel Vaults, Pocket Chronometers; Strictly Zero Firearms, Railways, Steam Engines, or AI/Electronics)",
        "history": """
            Central City is the geopolitical hub of Tier 3. Following the catastrophic warfare of Era 3, all major powers signed the historic Grand Concord treaty, designating Central City as a 100% Demilitarized Zone to prevent cosmic mutually assured destruction.
            
            No kingdom is permitted to march troops within its borders. High Chancellor Sulabha presides over the multinational parliament; High Governor Ambika manages the The Central Reserve Bank (Akash-Kosha) central bank; Magistrate Sudeva delivers incorruptible justice; and Guildmaster Uttanka oversees the global acoustic mantra-stone communications network. If any monarch initiates unprovoked war, Central City can freeze their currency and sever mantra-frequency relays within 24 hours, bringing their economy to an immediate halt.
        """,
        "culture_and_laws": """
            - Total Demilitarization: Only Grand Marshal Satyabhama's 20,000 peacekeepers—armed strictly with non-lethal weapons—are permitted to bear arms. Lethal war astras and projectile weapons are prohibited.
            - Aether-Rupee Monetary Anchor: All international trade across the five quadrants is settled in Central City's gold-backed Aether-Rupee.
            - The Sacred Frequency: Guildmaster Uttanka's mantra-stone exchange guarantees uncensored diplomatic, market, and emergency transmissions across all borders.
        """,
        "era_timeline": {
            "era_1": "The sacred central axis where primordial beings assembled for cosmic consultations.",
            "era_2": "Ground zero of spatial stabilization efforts led by Sages and ancient architects.",
            "era_3": "Established as a permanent demilitarized city-state through the Grand Concord Treaty.",
            "era_4": "Controls the global acoustic mantra exchange, The Central Reserve Bank (Akash-Kosha) currency reserves, and multinational arbitration courts."
        },
        "geopolitical_relations": {
            "allies": ["Universal diplomatic alignment with all four outer sub-realms through treaty mandates"],
            "rivals": ["Corrupted Realm cults and border warlords who seek to derail the Grand Concord"],
            "grudges": ["Vigilant against any resurgence of imperial hegemonies"],
            "trade_dependencies": ["Controls the global money supply and information grid; completely neutral arbiter"]
        },
        "character_ids": [
            "CHR-CEN-01", "CHR-CEN-02", "CHR-CEN-03", "CHR-CEN-04", 
            "CHR-CEN-05", "CHR-CEN-06", "CHR-CEN-07", "CHR-CEN-08"
        ]
    },
    {
        "id": "dyn-coastal",
        "name_en": "Coastal Merchant League & Naval Clans",
        "name_formal": "The Maritime Admiralty of Samudra-Pattanam",
        "origin_era_code": "ERA-3",
        "origin_era_name": "Era 3: The Great Partition Maritime Boom",
        "current_status_era": "Era 4: Plutocratic Naval Trade Monopoly",
        "sub_realm": "Human Sub-Realm (Mortal Cradle)",
        "sub_realm_code": "HUM",
        "badge": "Maritime Merchant Oligarchy",
        "color": "#38bdf8",
        "accent_bg": "rgba(56, 189, 248, 0.12)",
        "crest": "⚓",
        "seat": "Samudra-Pattanam Deep Docks & Lighthouse Citadel",
        "capital": "Samudra-Pattanam",
        "government": "Plutocratic Maritime Admiralty & Merchant Council",
        "motto": "Velayitam Dhanam Raksham • The Deep Waters Yield to Iron & Silver",
        "founding_era": "Era 3: The Great Partition",
        "primary_race": "Human Seafarers & Amphibious Guild Specialists",
        "economic_pillars": "Trans-Oceanic Freight, Deep Trench Salvage, Salt Cartels, Naval Banking & War Bonds",
        "tech_level": "Marine Dimensional Engineering (Aether-Propelled Frigates, Brass Diving Bells, Gyro-Compasses; Strictly Zero Firearms, Railways, Steam Engines, or Electronics)",
        "history": """
            Samudra-Pattanam is the wealthiest seaport in the mortal realm. While inland Hastinapur organized regional trade routes, seafaring merchant families banded together to form the Coastal League in Era 3. Under Lord Admiral Suhotra, "The Silver Shark", they established a monopoly over all navigable sea lanes across the Mortal Sea (The Mortal Sea (Nashvar Samudra)).
            
            Operating heavily armored runic frigates and aether-turbines, the League is a plutocracy backed by private naval firepower. They finance the Hastinapur royal treasury's merchant bonds, giving Lord Admiral Suhotra immense indirect leverage over King Parikshit's domestic policies.
        """,
        "culture_and_laws": """
            - Admiralty Law: Commercial profit is paramount; ships of all species are welcomed in harbor provided port dues and customs duties are cleared.
            - Deep Salvage Guild: Master divers like Malhar, Deep-Sea Salvager use brass diving bells to recover pre-Sundering artifacts from sunken trenches.
        """,
        "era_timeline": {
            "era_1": "Coastal fisher clans and early shallow-water traders under inland kingly tributes.",
            "era_2": "Harbor fortifications built as the seas surged during tectonic cataclysms.",
            "era_3": "Formed the unified Merchant League following the Great Partition to monopolize trans-oceanic transit corridors.",
            "era_4": "Constructed aether-driven runic frigates, reinforced hulls, deep salvage diving bells, and established naval banking."
        },
        "geopolitical_relations": {
            "allies": ["Samudra-Pattanam Harbor Guard", "Central Banking Exchange of Central City"],
            "rivals": ["Asuran River War-Vessel Squadrons (Tariff dispute over iron ore transport)"],
            "grudges": ["Hastinapur Crown's unpaid naval wartime bonds"],
            "trade_dependencies": ["Needs Hastinapur grain and Asuran armor plating; controls maritime routes to southern beast archipelagos"]
        },
        "character_ids": [
            "CHR-HUM-08", "CHR-HUM-09", "CHR-HUM-10", "CHR-HUM-11", "CHR-HUM-12"
        ]
    },
    {
        "id": "dyn-mining",
        "name_en": "Parvata-Khani Seven Mining Clans",
        "name_formal": "The Deep Basin Cartel of Shaila-Gadha",
        "origin_era_code": "ERA-3",
        "origin_era_name": "Era 3: The Great Partition Deep Mining",
        "current_status_era": "Era 4: Mining Baron Oligarchy & Labor Front",
        "sub_realm": "Asura Sub-Realm (Chthonic Foundries)",
        "sub_realm_code": "ASU",
        "badge": "Mining Oligarchy & Proletariat Front",
        "color": "#fb923c",
        "accent_bg": "rgba(251, 146, 60, 0.12)",
        "crest": "⛏️",
        "seat": "Shaila-Gadha Caldera & Deep Obsidian Pits",
        "capital": "Shaila-Gadha",
        "government": "Oligarchic Mining Syndicate conflicted by Underground Labor Unions",
        "motto": "Khanena Prapyate Tejah • From the Black Depths We Carve the World's Heat",
        "founding_era": "Era 3: The Great Partition",
        "primary_race": "Subterranean Asuras & Chthonic Labor Miners",
        "economic_pillars": "Raw Aether-Slag Extraction, Raw Obsidian Extraction, Sulfur Refining, Diamond Drills, Heavy Mineral Logistics",
        "tech_level": "Chthonic Mining Engineering (Heavy Runic Hoists, Obsidian Hammers, Pneumatic Drills, Sulfur Respirators; Strictly Zero Electronics)",
        "history": """
            Shaila-Gadha is the deepest volcanic rift basin in the Asura Sub-Realm. Here, seven ancient clan houses (Shaila, Loha, Ratna, Khaani, Dhatu, Shila, Giri) unified in Era 3 to control mineral extraction. Baroness Simhika commands private monopolies over 70% of anthracite minerals and raw obsidian in Tier 3.
            
            Due to lethal working conditions and toxic gas leaks, the mines have become a hotbed of class rebellion. Ulka's 'Red Crucible' underground labor union wages clandestine strike warfare against Simhika's private security forces, demanding an 8-hour shift limit, respirators, and injury pensions.
        """,
        "culture_and_laws": """
            - The Ore Quota: Corporate profit is tallied strictly in tonnage; mine owners prioritize cargo departure schedules above miners' health.
            - Labor Resistance: Ulka's union cells organize wildcat strikes and sabotage equipment to enforce worker safety protections.
        """,
        "era_timeline": {
            "era_1": "Scattered subterranean outcasts and independent basalt diggers operating without corporate charter.",
            "era_2": "Sought refuge in deep volcanic fault lines during void sky breaches, discovering rich obsidian veins.",
            "era_3": "Seven patriarchs signed the Shaila-Kula-Sangha cartel accord, seizing private monopoly over mineral basins.",
            "era_4": "Controls 70% of anthracite minerals and obsidian in Tier 3; locked in strike warfare with Ulka's Red Crucible labor front."
        },
        "geopolitical_relations": {
            "allies": ["Vajra-Nagara Smelters (Commercial supplier)", "Hastinapur Aether-Fuel Depots"],
            "rivals": ["Central City Labor Investigators (Anti-corruption warrants)", "Maya Dynasty (Price gouging disputes)"],
            "grudges": ["Fierce internal feud between Baroness Simhika's enforcers and Ulka's Red Crucible rebels"],
            "trade_dependencies": ["Monopoly supplier of anthracite minerals and Vajra-steel to all human and Asura foundries"]
        },
        "character_ids": [
            "CHR-ASU-05", "CHR-ASU-06", "CHR-ASU-07", "CHR-ASU-08", "CHR-ASU-09", "CHR-ASU-15"
        ]
    },
    {
        "id": "dyn-shadow",
        "name_en": "Shadow-Tigers & Vanara Vanguard",
        "name_formal": "The Twilight Federation of Gupta-Kandara",
        "origin_era_code": "ERA-3",
        "origin_era_name": "Era 3: The Great Partition Peacekeepers",
        "current_status_era": "Era 4: Guerrilla Rangers & Diplomatic Bridge",
        "sub_realm": "Beast Sub-Realm (Primeval Expanse)",
        "sub_realm_code": "BST",
        "badge": "Jungle Guerrilla & Diplomatic Peacekeepers",
        "color": "#a7f3d0",
        "accent_bg": "rgba(167, 243, 208, 0.12)",
        "crest": "🐅",
        "seat": "Gupta-Kandara Twilight Swamp & Salt Ridge Outpost",
        "capital": "Gupta-Kandara",
        "government": "Tribal Shamanic Circle & Ranger Federation",
        "motto": "Setureva Vijayate • The Bridge of Life Endures Through Vigilance",
        "founding_era": "Era 3: The Great Partition",
        "primary_race": "Shadow Panthers, Saber-Cats, Vanara Rangers & Human Shamans",
        "economic_pillars": "Jungle Trail Guiding, Salt Marsh Trading, Anti-Poaching Intelligence, Rare Herb Gathering",
        "tech_level": "Tribal-Mechanical Hybrid (Stealth Camouflage, Bone Whistles, Pheromone Markers, Recurve Bows; Zero Electronics)",
        "history": """
            Gupta-Kandara is a concealed redoubt hidden among murky mangrove swamps in the southern Beast Sub-Realm. Founded in Era 3 following the signing of The Great Beast Accord, this alliance brings together shadow stalkers like Shyama, "The Shadow-Cat", Sarama, "Queen of Blood-Ridge", and human diplomat Shabari, "The Bone-Speaker".
            
            Acting as peacekeepers between beasts and human civilization, they execute guerrilla strikes against illegal trafficking cartels. Shabari represents beast civil rights as an accredited ambassador within Central City's Grand Concord assembly.
        """,
        "culture_and_laws": """
            - The Great Beast Accord Enforcement: Enslaving wild beasts or running animal fighting arenas is punishable by summary execution.
            - The Silent Step: Shyama's stalkers are master stealth infiltrators, stepping between ambient shadows to ambushing poachers.
        """,
        "era_timeline": {
            "era_1": "Nomadic jungle packs roaming independently without interspecies treaties.",
            "era_2": "Vanaras and feline predators banded together to defend watering holes from void predators.",
            "era_3": "Formed the official Ranger Federation to enforce The Great Beast Accord.",
            "era_4": "Carries out surgical anti-poaching operations while Shabari lobbies in Central City."
        },
        "geopolitical_relations": {
            "allies": ["Central City Peacekeeping Bureau", "Hastinapur Reform Faction"],
            "rivals": ["Black-Market Syndicate of Samudra-Pattanam (Poaching cartels)"],
            "grudges": ["Fierce hatred against beast slave traders and animal gladiatorial pits"],
            "trade_dependencies": ["Trades salt minerals and guiding services for medical bandages and iron tips"]
        },
        "character_ids": [
            "CHR-BST-05", "CHR-BST-06", "CHR-BST-07"
        ]
    }
]
