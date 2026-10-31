import os
import re
import json

_current_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_current_dir)
base_dir = os.path.join(_project_root, "New")
if not os.path.exists(base_dir):
    base_dir = r"D:\Web Novel\New"

output_html = os.path.join(base_dir, "ability_codex.html")
source_md = os.path.join(base_dir, "powers", "abilities.md")

category_prefixes = {
    1: ("ELE", "Elemental & Primordial", "cyan", "Prāṇa / Tapasya"),
    2: ("SPA", "Spatial & Dimensional", "purple", "Yantra / Mantra"),
    3: ("TEM", "Time & Chrono-Kinetic", "rose", "LOCKED / Axis A"),
    4: ("PSI", "Mental, Psychic & Illusion", "emerald", "Tapasya / Mantra"),
    5: ("SOL", "Soul, Spirit & Astral", "gold", "Tapasya / Astra"),
    6: ("LIF", "Life, Death & Healing", "emerald", "Prāṇa / Mantra"),
    7: ("BOD", "Physical Overdrive & Body", "gold", "Tapasya / Prāṇa"),
    8: ("WEA", "Weapons Mastery & Dhanurveda", "cyan", "Yantra / Tapasya"),
    9: ("AST", "Divine Astras & Relics", "rose", "Astra / Boons"),
    10: ("SEA", "Sealing, Barriers & Wards", "purple", "Yantra / Mantra"),
    11: ("TRN", "Transformation & Morphology", "gold", "Mantra / Prāṇa"),
    12: ("SEN", "Sensory, Eyes & Detection", "cyan", "Tapasya"),
    13: ("DOM", "Domain & Boundary Expansion", "rose", "All 5 Unified"),
    14: ("ATM", "Ātma-Tattva Manifestations", "gold", "Secret Sixth Principle")
}

evolution_data = {
    "Pyrokinesis": ("Evolvable", "Brahma-Granthi unsealed", "Agni-Bāṇa (Concentrated Needle Ray)", "Sub-atomic heat piercing through Kinetic Lamina"),
    "Hydrokinesis": ("Branch-Evolvable", "Tapasya water-immersion", "Branch A: Blood-Stasis / Branch B: Absolute Mist Mirage", "A: Internal fluid paralysis; B: Spatial optical refraction"),
    "Aerokinesis": ("Branch-Evolvable", "Sky-tether severance", "Branch A: Vacuum Blade Storm / Branch B: Supersonic Sonic Cushion", "A: Armor bypass slicing; B: Shockwave redirection"),
    "Geokinesis & Terramancy": ("Mastery-Only", "Basalt compression practice", "Vajra-Prithvi Armor", "Denser crystalline shielding resistant to heavy artillery"),
    "Electrokinesis": ("Evolvable", "Vishnu-Granthi breakthrough", "Vajra-Nadi Rail-Discharge", "Instant internal nervous-system frying velocity"),
    "Cryokinesis": ("Evolvable", "Absolute-zero meditation", "Hima-Stasis Prison", "Freezes kinetic velocity of oncoming projectiles"),
    "Photokinesis / Solar": ("Branch-Evolvable", "Surya-Sadhana initiation", "Branch A: Divine Smite Flare / Branch B: Laser Scalpel", "A: Anti-undead purification; B: Micro-surgical excision"),
    "Umbrakinesis / Shadow": ("Branch-Evolvable", "Tamas absorption vow", "Branch A: Spatial Shadow Step / Branch B: Void Suffocation Veil", "A: Dimension fold step; B: Light & air blackout"),
    "Blink / Short Teleport": ("Mastery-Only", "Spatial coordinate tuning", "Continuous Flash Step (5x chained)", "Chains 5 short teleports with zero momentum loss"),
    "Spatial Severance": ("Evolvable", "Rudra-Granthi resonance", "Akasha-Khanda (Horizon Shear)", "Cleaves 50 meters of spatial fabric directly"),
    "Pocket Dimension Vault": ("Mastery-Only", "Aether fold expansion", "Expanded Sub-Space Armory", "Triple storage capacity with instantaneous weapon retrieval"),
    "Dimensional Lock": ("Evolvable", "Spatial anchor refinement", "Absolute Dimensional Stasis Field", "Prevents all teleportation and spatial phase-shifts within 200m"),
    "Gravitational Control": ("Branch-Evolvable", "Core mass calibration", "Branch A: Micro-Singularity Pull / Branch B: Absolute Repulsion Dome", "A: Crushing localized gravity; B: Kinetic projectile deflection"),
    "Tactical Foresight": ("Mastery-Only", "Ajna chakra focus", "Precognition 10-Second Horizon", "Expands precognitive window from 2s to 10s"),
    "Time Dilation / Acceleration": ("Mastery-Only", "Neural clock acceleration", "Micro-Second Hyper-Perception", "Allows 10x faster tactical thought without bodily thermal burn"),
    "Localized Temporal Stasis": ("Non-Evolving", "Axis A Permission boundary", "Static Temporal Anchor", "Fixed duration barrier; inaccessible through Axis B training"),
    "Chrono-Rewind": ("Non-Evolving", "Class-Omega Cosmic Law", "Forbidden Causality Snap", "Permanent karmic debt; strictly non-improvable"),
    "Telepathy & Mind-Link": ("Mastery-Only", "Manomaya-Kosha tuning", "Encrypted Tactical Hive-Link", "Multi-target mental bridge impenetrable by amateur psychics"),
    "Sensory Hijacking": ("Branch-Evolvable", "Mayic resonance training", "Branch A: Full Sensory Deprivation / Branch B: Phantom Pain Synesthesia", "A: Total blindness/deafness; B: Induced physical shock"),
    "Fear Induction & Despair": ("Evolvable", "Asura blood-resonance", "Aura of Visceral Paralysis", "Forces autonomic nervous system lockup on targets below T4"),
    "Absolute Command": ("Evolvable", "Authority royal mandate", "Sovereign Decree (Vashitva)", "Direct soul-vessel binding that resists standard mental barriers"),
    "Soul Perception": ("Mastery-Only", "Silver Cord observation", "Full Karmic Signature Spectrum", "Detects hidden identities, vessel damage, and foreign possession"),
    "Soul-Piercing Strike": ("Evolvable", "Ojas sharpening discipline", "Sukshma-Bheda (Astral Piercer)", "Directly cuts astral cord while leaving physical armor untouched"),
    "Spirit Ejection / Possession": ("Mastery-Only", "Astral body stabilization", "Seamless Parakaya-Pravesha", "Smooth vessel transition with 50% reduced recoil shock"),
    "Soul Binding / Anchoring": ("Branch-Evolvable", "Runic seal weaving", "Branch A: Relic Binding / Branch B: Boundary Soul Ward", "A: Seals spirits into weapons; B: Erects spirit-denial barrier"),
    "Cellular Regeneration": ("Branch-Evolvable", "Prana-metabolic alignment", "Branch A: Accelerated Flesh-Weave / Branch B: Cellular Detoxification", "A: Instant closing of arterial wounds; B: Automatic poison purging"),
    "Toxin Synthesis & Neutralization": ("Mastery-Only", "Naga venom guild alchemy", "Universal Antidote Formulation", "Neutralizes synthetic and organic toxins in seconds"),
    "Necrotic Rot & Decay": ("Evolvable", "Karmic dissolution focus", "Apocalyptic Ash Decomposition", "Dissolves non-magical solid matter into organic slag"),
    "Resuscitation Arts": ("Non-Evolving", "Yama Exit Window Rule", "Golden Window Mṛta-Sanjīvanī", "Strictly bound to Yama's pre-release clearance time limit"),
    "Vajra-Deha": ("Evolvable", "Granthi piercing + molten bath", "Indra-Vajra Flesh (Grade 2)", "Flesh density completely deflects 19th-c rifle fire"),
    "Superhuman Velocity": ("Branch-Evolvable", "Laghima siddhi cultivation", "Branch A: Sonic Flash Dash / Branch B: Aether Gliding", "A: Ground speed Mach 1.5; B: Zero-friction aether surfing"),
    "Colossal Expansion": ("Mastery-Only", "Mahima mass density control", "Mountain-Breaker Titan Stance", "Doubles weight and kinetic mass without sacrificing mobility"),
    "Kinetic Impact Amplification": ("Evolvable", "Vyana vayu compression", "Thunderclap Shockwave Strike", "Acoustic concussion that shatters internal organs through armor"),
    "Blade Aura": ("Branch-Evolvable", "Weapon soul resonance", "Branch A: Asi-Dhara Shockwave / Branch B: Micro-Molecular Edge", "A: 100m flying slash; B: Diamond-cutting edge"),
    "Infallible Archery": ("Mastery-Only", "Dhanurveda line-of-sight sight", "Seeking Wind Arrow Mastery", "Curves trajectory around physical fortifications"),
    "Weapon Imbuement": ("Branch-Evolvable", "Pranic conduit etching", "Branch A: High-Frequency Resonance / Branch B: Thermal Imbuement", "A: Armor-piercing vibration; B: Molten impact payload"),
    "Living Weapon Bond": ("Evolvable", "Soul-sync pact with weapon", "Awakened Relic Symbiosis", "Weapon acts autonomously as an external combat limb"),
    "Cataclysmic Piercing Arrows": ("Mastery-Only", "Dhanurveda Visarjana mastery", "Brahmāstra Upasamhāra Precision", "Flawless retraction with zero environmental curse"),
    "Homing Absolute Annihilation": ("Non-Evolving", "Supreme Trinity Arsenal", "Sudarshana Inevitable severing", "Absolute tracking, unaffected by mortal training"),
    "Absolute Inviolable Armor": ("Non-Evolving", "Divine Boon Contract", "Kavacha-Kundala Invariance", "100% baseline damage immunity; cannot be evolved or upgraded"),
    "Swarm Ordinance Weapons": ("Mastery-Only", "Mass invocation discipline", "Nārāyaṇāstra Million-Spear Rain", "Widens salvo density across battlefield"),
    "Absolute Isolation Ward": ("Mastery-Only", "Geometric ward anchoring", "Aether-Barred Sanctuary Dome", "Zero audio, signal, or spiritual energy leakage across perimeter"),
    "Chakravyūha Formations": ("Mastery-Only", "Military spatial orchestration", "12-Ring Concentric Trap", "Dynamic rotating frontline that grinds enemy battalions"),
    "Energy Drain Seals": ("Evolvable", "Reverse pranic siphon runes", "Vampiric Aether Siphon", "Converts absorbed enemy mantras directly into user's shield"),
    "Exorcism & Curse Cleansing": ("Mastery-Only", "Shastra liturgy mastery", "Karmic Cleansing Litany", "Purges malignant astral parasites without biological harm"),
    "Kāma-Rūpa": ("Branch-Evolvable", "Asuric morphology shift", "Branch A: Perfect Inanimate Mimicry / Branch B: Hybrid Beast Form", "A: Indistinguishable from objects; B: Claws, wings, armor"),
    "Beast-Spirit Manifestation": ("Evolvable", "Prāṇa-Bandhan resonance", "Apex Titan Avatāra", "Manifests spectral 10-meter beast construct around body"),
    "Titan / Battle Form Release": ("Mastery-Only", "Asuric biological overcharge", "Four-Armed Asura War-Stance", "Multi-weapon wielding with fourfold striking frequency"),
    "Energy-Pathway Sight": ("Mastery-Only", "Nādī perception clarity", "Acupoint Weakness Mapping", "Pinpoints exact blockage and vulnerability in enemy armor"),
    "Omnidirectional Danger Sense": ("Mastery-Only", "Ajna antenna awakening", "Zero-Blindspot Reflex Arc", "Instinctive dodge triggers prior to conscious awareness"),
    "Truth Perception": ("Evolvable", "Satya-Drishti breakthrough", "Veil-Piercing Eye of Truth", "Shatters high-level illusions and spatial folding barriers"),
    "Cosmic Clairaudience": ("Mastery-Only", "Aetheric frequency receiver", "Planetary Signal Intercept", "Monitors telegraph wires and distant vocal declarations"),
    "Domain Expansion": ("Evolvable", "All Granthis pierced + Domain Anchor", "Inviolable Conceptual Domain", "100% sure-hit technique activation inside radius"),
    "Ātma-Tattva Manifestation": ("Non-Evolving", "Immutable Core", "Sovereign Inviolability", "Absolute cosmic anomaly immunity; cannot be evolved or altered")
}

def parse_powers():
    with open(source_md, "r", encoding="utf-8") as f:
        content = f.read()
    
    abilities = []
    current_cat_num = 0
    current_cat_title = ""
    
    lines = content.splitlines()
    for line in lines:
        cat_match = re.match(r"^### Category (\d+):\s*(.*)", line.strip())
        if cat_match:
            current_cat_num = int(cat_match.group(1))
            current_cat_title = cat_match.group(2).strip()
            continue
            
        row_match = re.match(r"^\|\s*\*\*([^*]+)\*\*\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|", line.strip())
        if row_match and current_cat_num > 0:
            name_raw = row_match.group(1).strip()
            manifest = row_match.group(2).strip()
            limits = row_match.group(3).strip()
            pillars = row_match.group(4).strip()
            
            clean_name = name_raw.split("(")[0].strip()
            vernacular = ""
            if "(" in name_raw:
                vernacular = name_raw.split("(")[1].replace(")", "").strip()
                
            prefix, cat_short, color, vehicle = category_prefixes.get(current_cat_num, ("GEN", "General", "cyan", "Prāṇa"))
            cat_count = len([a for a in abilities if a["category_num"] == current_cat_num]) + 1
            ability_id = f"ABL-{prefix}-{cat_count:02d}"
            
            evo_info = evolution_data.get(clean_name, (
                "Mastery-Only", 
                "Sustained Tapasya & Granthi tuning", 
                f"{clean_name} Mastery Grade", 
                "30% reduction in Prāṇa throughput cost and 2x precision"
            ))
            
            tier_band = "T4 (Trained)"
            if current_cat_num in [1, 7, 8, 12]:
                tier_band = "T3–T4 (Mortal to Trained)"
            elif current_cat_num in [2, 4, 6, 10, 11]:
                tier_band = "T4–T5 (Crossover to Awakened)"
            elif current_cat_num in [3, 9, 13]:
                tier_band = "T5–T6 (Awakened to Ascendent)"
            elif current_cat_num == 14:
                tier_band = "T7+ (Cosmic Transcendent / Inviolable)"
                
            abilities.append({
                "id": ability_id,
                "name": clean_name,
                "vernacular": vernacular,
                "category_num": current_cat_num,
                "category_name": current_cat_title,
                "category_short": cat_short,
                "prefix": prefix,
                "color": color,
                "vehicle": vehicle,
                "tier_band": tier_band,
                "manifestation": manifest,
                "limits": limits,
                "pillars": pillars,
                "evolution_type": evo_info[0],
                "evolution_trigger": evo_info[1],
                "evolution_form": evo_info[2],
                "evolution_effects": evo_info[3]
            })
            
    if not any(a["name"] == "Domain Expansion" for a in abilities):
        abilities.append({
            "id": "ABL-DOM-01",
            "name": "Domain Expansion",
            "vernacular": "क्षेत्र-बंधन / वास्तव-अधिलिखन",
            "category_num": 13,
            "category_name": "Domain, Territory & Boundary Expansion",
            "category_short": "Domain Expansion",
            "prefix": "DOM",
            "color": "rose",
            "vehicle": "All 5 Unified",
            "tier_band": "T6 (Ascendent)",
            "manifestation": "Internal mental landscape overwriting outer physical space; imparts 100% statutory Sure-Hit attribute to user's attacks.",
            "limits": "Massive Prāṇa exhaustion; counterable by superior Domain density, outside geometric barrier strikes, or destroying core anchor.",
            "pillars": "Authority + Energy + Tapasya",
            "evolution_type": "Evolvable",
            "evolution_trigger": "Rudra-Granthi unsealed + Anchor refinement",
            "evolution_form": "Inviolable Conceptual Domain",
            "evolution_effects": "Expands radius to 500m with zero external barrier seam"
        })
        
    if not any(a["name"] == "Ātma-Tattva Manifestation" for a in abilities):
        abilities.append({
            "id": "ABL-ATM-01",
            "name": "Ātma-Tattva Manifestation",
            "vernacular": "गुप्त आत्मतत्त्व विसंगती",
            "category_num": 14,
            "category_name": "Ātma-Tattva Manifestations (Secret Sixth Principle)",
            "category_short": "Ātma-Tattva",
            "prefix": "ATM",
            "color": "gold",
            "vehicle": "Secret Sixth Principle",
            "tier_band": "T7+ (Cosmic Transcendent / Inviolable)",
            "manifestation": "Complete ontological resistance to soul-erasure, destiny rewrites, and Ananta ledger tampering. Anomaly armor.",
            "limits": "Non-quantifiable, cannot be invoked as an active combat spell, immutable by any cosmic weapon.",
            "pillars": "Secret Sixth Principle",
            "evolution_type": "Non-Evolving",
            "evolution_trigger": "None (Eternal & Immutable)",
            "evolution_form": "Eternal Core",
            "evolution_effects": "Absolute immunity to erasure"
        })
        
    return abilities

def generate_html(abilities):
    abilities_json = json.dumps(abilities, ensure_ascii=False)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Universe B — Ability Codex & Power Profile UI</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {{
  --bg-void: #050811;
  --bg-primary: #090d1a;
  --bg-card: rgba(22, 32, 58, 0.65);
  --bg-card-solid: #131c31;
  --bg-card-hover: rgba(30, 45, 78, 0.85);
  --border-color: rgba(148, 163, 184, 0.16);
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --text-dim: #64748b;
  --accent-gold: #f59e0b;
  --accent-gold-light: #fbbf24;
  --accent-cyan: #06b6d4;
  --accent-cyan-light: #38bdf8;
  --accent-emerald: #10b981;
  --accent-rose: #f43f5e;
  --accent-purple: #a855f7;
  --font-display: 'Cinzel', serif;
  --font-body: 'Plus Jakarta Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  background: var(--bg-void);
  color: var(--text-main);
  font-family: var(--font-body);
  line-height: 1.5;
  min-height: 100vh;
  padding: 24px;
}}

header {{
  max-width: 1400px;
  margin: 0 auto 24px;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  flex-wrap: wrap;
  gap: 16px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border-color);
}}

.logo-area h1 {{
  font-family: var(--font-display);
  font-size: 2rem;
  letter-spacing: 2px;
  background: linear-gradient(135deg, #fff 30%, var(--accent-gold-light) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.logo-area p {{
  color: var(--text-muted);
  font-size: 0.9rem;
  margin-top: 4px;
}}

.nav-links {{
  display: flex;
  gap: 12px;
  align-items: center;
}}

.btn-nav {{
  background: rgba(6, 182, 212, 0.12);
  border: 1px solid rgba(6, 182, 212, 0.3);
  color: var(--accent-cyan-light);
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 0.85rem;
  font-family: var(--font-mono);
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s;
}}

.btn-nav:hover {{
  background: rgba(6, 182, 212, 0.25);
  border-color: var(--accent-cyan);
  transform: translateY(-2px);
}}

/* Filter Controls */
.controls-panel {{
  max-width: 1400px;
  margin: 0 auto 24px;
  background: var(--bg-card);
  backdrop-filter: blur(12px);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}}

.search-row {{
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
}}

.search-input-box {{
  flex: 1;
  min-width: 280px;
  position: relative;
}}

.search-input-box input {{
  width: 100%;
  background: rgba(9, 13, 26, 0.9);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 12px 16px 12px 42px;
  color: #fff;
  font-size: 0.95rem;
  font-family: var(--font-body);
  outline: none;
  transition: border-color 0.2s;
}}

.search-input-box input:focus {{
  border-color: var(--accent-cyan);
  box-shadow: 0 0 12px rgba(6, 182, 212, 0.2);
}}

.search-icon {{
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-dim);
  font-size: 1.1rem;
}}

.select-filters {{
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}}

select {{
  background: rgba(9, 13, 26, 0.9);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 10px 14px;
  color: var(--text-main);
  font-size: 0.85rem;
  font-family: var(--font-body);
  outline: none;
  cursor: pointer;
}}

select:focus {{
  border-color: var(--accent-cyan);
}}

/* Category Pills */
.category-pills {{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}}

.pill {{
  background: rgba(148, 163, 184, 0.08);
  border: 1px solid rgba(148, 163, 184, 0.15);
  color: var(--text-muted);
  font-size: 0.78rem;
  font-family: var(--font-mono);
  font-weight: 600;
  padding: 6px 12px;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.2s;
  user-select: none;
}}

.pill:hover {{
  background: rgba(148, 163, 184, 0.18);
  color: #fff;
}}

.pill.active {{
  background: rgba(6, 182, 212, 0.2);
  border-color: var(--accent-cyan);
  color: var(--accent-cyan-light);
  box-shadow: 0 0 8px rgba(6, 182, 212, 0.25);
}}

.stats-bar {{
  max-width: 1400px;
  margin: 0 auto 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  color: var(--text-dim);
  font-family: var(--font-mono);
}}

/* Ability Cards Grid */
.cards-grid {{
  max-width: 1400px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(430px, 1fr));
  gap: 20px;
}}

.ability-card {{
  background: var(--bg-card);
  backdrop-filter: blur(14px);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
  position: relative;
  overflow: hidden;
}}

.ability-card::before {{
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: var(--card-accent, var(--accent-cyan));
}}

.ability-card:hover {{
  transform: translateY(-3px);
  border-color: rgba(255, 255, 255, 0.25);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
}}

.card-top {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
}}

.ability-id {{
  font-family: var(--font-mono);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 1px;
  color: var(--card-accent, var(--accent-cyan-light));
  background: rgba(0, 0, 0, 0.4);
  padding: 3px 8px;
  border-radius: 4px;
  border: 1px solid rgba(255, 255, 255, 0.08);
}}

.badges-row {{
  display: flex;
  gap: 6px;
  align-items: center;
}}

.badge {{
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 3px 7px;
  border-radius: 4px;
}}

.badge-canon {{ background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }}
.badge-tier {{ background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }}
.badge-evo {{ background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3); }}
.badge-mastery {{ background: rgba(6, 182, 212, 0.15); color: #38bdf8; border: 1px solid rgba(6, 182, 212, 0.3); }}
.badge-static {{ background: rgba(148, 163, 184, 0.12); color: #94a3b8; border: 1px solid rgba(148, 163, 184, 0.2); }}

.card-title h3 {{
  font-family: var(--font-display);
  font-size: 1.25rem;
  color: #fff;
  letter-spacing: 0.5px;
}}

.card-title .vernacular {{
  color: var(--text-muted);
  font-size: 0.88rem;
  font-weight: 400;
  font-family: var(--font-body);
  margin-top: 2px;
}}

.category-tag {{
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--card-accent, var(--accent-cyan));
  font-weight: 600;
  margin-top: 2px;
}}

/* Specification Grid inside Card */
.spec-box {{
  background: rgba(9, 13, 26, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}}

.spec-item {{
  display: flex;
  flex-direction: column;
  gap: 2px;
}}

.spec-label {{
  font-family: var(--font-mono);
  font-size: 0.68rem;
  text-transform: uppercase;
  color: var(--text-dim);
  letter-spacing: 0.5px;
  font-weight: 700;
}}

.spec-val {{
  font-size: 0.86rem;
  color: #cbd5e1;
}}

.spec-val.pillars {{
  color: var(--accent-gold-light);
  font-weight: 600;
}}

.spec-val.vehicle {{
  color: var(--accent-cyan-light);
}}

/* Limits & Evolution Callouts */
.section-callout {{
  border-left: 2px solid;
  padding-left: 10px;
  font-size: 0.82rem;
  line-height: 1.45;
}}

.callout-limits {{
  border-color: var(--accent-rose);
  background: rgba(244, 63, 94, 0.06);
  padding: 8px 10px;
  border-radius: 0 6px 6px 0;
}}

.callout-limits .lbl {{
  color: var(--accent-rose);
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 2px;
}}

.callout-evo {{
  border-color: var(--accent-purple);
  background: rgba(168, 85, 247, 0.06);
  padding: 8px 10px;
  border-radius: 0 6px 6px 0;
}}

.callout-evo .lbl {{
  color: #c084fc;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 2px;
}}

.callout-evo .evo-target {{
  color: #fff;
  font-weight: 600;
}}

.no-results {{
  grid-column: 1 / -1;
  text-align: center;
  padding: 60px 20px;
  color: var(--text-dim);
  font-size: 1.1rem;
}}
</style>
</head>
<body>

<header>
  <div class="logo-area">
    <h1>UNIVERSE B • ABILITY CODEX</h1>
    <p>Individual Power System Profiles, Granthi Evolution Tracks &amp; Tactical Counterplay</p>
  </div>
  <div class="nav-links">
    <a href="index.html" class="btn-nav">← Back to Master Portal</a>
  </div>
</header>

<div class="controls-panel">
  <div class="search-row">
    <div class="search-input-box">
      <span class="search-icon">🔍</span>
      <input type="text" id="searchInput" placeholder="Search by ability name, Sanskrit title, ID, counterplay, or mechanics..." oninput="filterAbilities()">
    </div>
    <div class="select-filters">
      <select id="tierFilter" onchange="filterAbilities()">
        <option value="ALL">All Scale Bands (T1–T7)</option>
        <option value="T3">T3–T4 Mortal to Trained</option>
        <option value="T4">T4 Trained Baseline</option>
        <option value="T5">T4–T5 Awakened</option>
        <option value="T6">T5–T6 Ascendent</option>
        <option value="T7">T7+ Transcendent / Inviolable</option>
      </select>
      <select id="evoFilter" onchange="filterAbilities()">
        <option value="ALL">All Evolution Types</option>
        <option value="Evolvable">Evolvable (Qualitative Shift)</option>
        <option value="Branch-Evolvable">Branch-Evolvable (Specialization)</option>
        <option value="Mastery-Only">Mastery-Only (Refinement)</option>
        <option value="Non-Evolving">Non-Evolving (Immutable)</option>
      </select>
    </div>
  </div>

  <div class="category-pills" id="categoryPills">
    <div class="pill active" onclick="setCategory(0, this)">All Categories (54)</div>
    <div class="pill" onclick="setCategory(1, this)">1. Elemental (8)</div>
    <div class="pill" onclick="setCategory(2, this)">2. Spatial (5)</div>
    <div class="pill" onclick="setCategory(3, this)">3. Time [Locked] (4)</div>
    <div class="pill" onclick="setCategory(4, this)">4. Mental / Maya (4)</div>
    <div class="pill" onclick="setCategory(5, this)">5. Soul / Astral (4)</div>
    <div class="pill" onclick="setCategory(6, this)">6. Life / Death (4)</div>
    <div class="pill" onclick="setCategory(7, this)">7. Body Overdrive (4)</div>
    <div class="pill" onclick="setCategory(8, this)">8. Weapons Art (4)</div>
    <div class="pill" onclick="setCategory(9, this)">9. Astras &amp; Relics (4)</div>
    <div class="pill" onclick="setCategory(10, this)">10. Sealing &amp; Wards (4)</div>
    <div class="pill" onclick="setCategory(11, this)">11. Morph &amp; Beast (3)</div>
    <div class="pill" onclick="setCategory(12, this)">12. Sensory &amp; Eyes (4)</div>
    <div class="pill" onclick="setCategory(13, this)">13. Domain (1)</div>
    <div class="pill" onclick="setCategory(14, this)">14. Ātma-Tattva (1)</div>
  </div>
</div>

<div class="stats-bar">
  <span id="resultsCount">Showing 54 of 54 Abilities</span>
  <span>Universe B Canon Matrix • Two-Axis Architecture</span>
</div>

<div class="cards-grid" id="cardsGrid">
  <!-- Populated by JS -->
</div>

<script>
const ABILITIES = {abilities_json};

let currentCategory = 0;

function getEvoBadgeClass(type) {{
  if (type === "Evolvable") return "badge-evo";
  if (type === "Branch-Evolvable") return "badge-evo";
  if (type === "Mastery-Only") return "badge-mastery";
  return "badge-static";
}}

function renderCards(list) {{
  const grid = document.getElementById("cardsGrid");
  document.getElementById("resultsCount").innerText = `Showing ${{list.length}} of ${{ABILITIES.length}} Abilities`;
  
  if (list.length === 0) {{
    grid.innerHTML = `<div class="no-results">No abilities match the selected filters.</div>`;
    return;
  }}
  
  let html = "";
  for (const a of list) {{
    const evoClass = getEvoBadgeClass(a.evolution_type);
    const accentVar = a.color === "cyan" ? "var(--accent-cyan)" : 
                     a.color === "purple" ? "var(--accent-purple)" : 
                     a.color === "rose" ? "var(--accent-rose)" : 
                     a.color === "emerald" ? "var(--accent-emerald)" : "var(--accent-gold)";
                     
    html += `
    <div class="ability-card" style="--card-accent: ${{accentVar}}">
      <div class="card-top">
        <span class="ability-id">${{a.id}}</span>
        <div class="badges-row">
          <span class="badge badge-canon">[CANON]</span>
          <span class="badge badge-tier">${{a.tier_band.split(' ')[0]}}</span>
          <span class="badge ${{evoClass}}">${{a.evolution_type}}</span>
        </div>
      </div>
      
      <div class="card-title">
        <h3>${{a.name}}</h3>
        <div class="vernacular">${{a.vernacular ? a.vernacular : ''}}</div>
        <span class="category-tag">Cat ${{a.category_num}}: ${{a.category_short}}</span>
      </div>
      
      <div class="spec-box">
        <div class="spec-item">
          <span class="spec-label">Axis A Pillars (Cosmic Governance)</span>
          <span class="spec-val pillars">${{a.pillars}}</span>
        </div>
        <div class="spec-item">
          <span class="spec-label">Axis B Vehicle (Practitioner Craft)</span>
          <span class="spec-val vehicle">${{a.vehicle}} • Scale: ${{a.tier_band}}</span>
        </div>
        <div class="spec-item">
          <span class="spec-label">Manifestation &amp; Mechanics</span>
          <span class="spec-val">${{a.manifestation}}</span>
        </div>
      </div>
      
      <div class="section-callout callout-limits">
        <div class="lbl">⚠️ Tactical Limits &amp; Hard Counters</div>
        <div>${{a.limits}}</div>
      </div>
      
      <div class="section-callout callout-evo">
        <div class="lbl">⚡ Evolution Track (${{a.evolution_type}})</div>
        <div><span class="evo-target">Trigger:</span> ${{a.evolution_trigger}}</div>
        <div><span class="evo-target">Evolved Form:</span> ${{a.evolution_form}}</div>
        <div style="color: var(--text-muted); font-size: 0.78rem; margin-top: 2px;">${{a.evolution_effects}}</div>
      </div>
    </div>`;
  }}
  grid.innerHTML = html;
}}

function setCategory(catNum, elem) {{
  currentCategory = catNum;
  document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
  elem.classList.add('active');
  filterAbilities();
}}

function filterAbilities() {{
  const query = document.getElementById("searchInput").value.toLowerCase().trim();
  const tier = document.getElementById("tierFilter").value;
  const evo = document.getElementById("evoFilter").value;
  
  const filtered = ABILITIES.filter(a => {{
    if (currentCategory !== 0 && a.category_num !== currentCategory) return false;
    if (tier !== "ALL" && !a.tier_band.includes(tier)) return false;
    if (evo !== "ALL" && a.evolution_type !== evo) return false;
    
    if (query) {{
      const matchText = (a.id + " " + a.name + " " + a.vernacular + " " + a.manifestation + " " + a.limits + " " + a.pillars + " " + a.evolution_form).toLowerCase();
      if (!matchText.includes(query)) return false;
    }}
    return true;
  }});
  
  renderCards(filtered);
}}

// Initial Render
renderCards(ABILITIES);
</script>

</body>
</html>"""

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    size_kb = round(os.path.getsize(output_html) / 1024, 1)
    print(f"Generated standalone Ability Codex UI at: {output_html} ({size_kb} KB)")

if __name__ == "__main__":
    items = parse_powers()
    generate_html(items)
