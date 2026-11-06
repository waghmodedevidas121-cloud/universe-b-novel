import os
import re
import json

_current_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_current_dir)
base_dir = os.path.join(_project_root, "New")
if not os.path.exists(base_dir):
    base_dir = r"D:\Web Novel\New"

output_html = os.path.join(base_dir, "character_codex.html")
source_dossier = os.path.join(base_dir, "characters", "roster.md")
if not os.path.exists(source_dossier):
    source_dossier = os.path.join(base_dir, "08_Character_Roster.md")

cat_metadata = {
    "HUM": {
        "title": "Human Sub-Realm",
        "mr": "मानव उप-लोक (हस्तिनापूर व समुद्र-पत्तनम)",
        "color": "var(--accent-cyan)",
        "badge_color": "rgba(6, 182, 212, 0.2)",
        "icon": "🏛️"
    },
    "ASU": {
        "title": "Asura Sub-Realm",
        "mr": "असुर उप-लोक (Vajra-Nagara व शैल-गाढा)",
        "color": "var(--accent-gold)",
        "badge_color": "rgba(245, 158, 11, 0.2)",
        "icon": "🌋"
    },
    "DEV": {
        "title": "Deva Sub-Realm",
        "mr": "देव उप-लोक (अमरावती व गंधर्व-पुरी)",
        "color": "var(--accent-rose)",
        "badge_color": "rgba(244, 63, 94, 0.2)",
        "icon": "☁️"
    },
    "BST": {
        "title": "Beast Sovereigns",
        "mr": "श्वापद-सार्वभौम (महा-कांतार व आदिम कुळे)",
        "color": "var(--accent-emerald)",
        "badge_color": "rgba(16, 185, 129, 0.2)",
        "icon": "🐾"
    },
    "CEN": {
        "title": "Central Astral",
        "mr": "मध्य-क्षेत्र (ग्रँड कॉन्कॉर्ड व आकाश-कोश)",
        "color": "var(--accent-purple)",
        "badge_color": "rgba(168, 85, 247, 0.2)",
        "icon": "⚖️"
    },
    "SET": {
        "title": "The Setu / Buffer Zone",
        "mr": "सेतु व बफर झोन (वज्र-दुर्ग व विद्या-पीठ)",
        "color": "var(--accent-cyan-light)",
        "badge_color": "rgba(56, 189, 248, 0.2)",
        "icon": "🛡️"
    },
    "ABY": {
        "title": "Abyssal Corrupted Realm",
        "mr": "अधोलोक व भ्रष्ट क्षेत्र (नेदरहोम व Dread-Hold)",
        "color": "#f43f5e",
        "badge_color": "rgba(244, 63, 94, 0.25)",
        "icon": "💀"
    },
    "DIV": {
        "title": "Divine & Constitutional",
        "mr": "वैश्विक व घटनात्मक व्यक्ती (सर्वोच्च त्रिमूर्ती व अनंता)",
        "color": "#fbbf24",
        "badge_color": "rgba(251, 191, 36, 0.25)",
        "icon": "🔱"
    },
    "ALN": {
        "title": "The Aliens Diaspora",
        "mr": "द एलियन्स डायस्पोरा (विस्थापित आधुनिक नश्वर)",
        "color": "var(--accent-cyan)",
        "badge_color": "rgba(6, 182, 212, 0.25)",
        "icon": "🚀"
    }
}

def parse_characters():
    with open(source_dossier, "r", encoding="utf-8") as f:
        text = f.read()

    pattern = r"###\s*\[(CHR-[A-Z]+-\d+)\]\s*([^(—\n]+)(?:\(([^)]+)\))?\s*(?:—\s*([^\n]+))?"
    matches = list(re.finditer(pattern, text))
    
    characters = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        body = text[start:end]
        
        char_id = m.group(1).strip()
        name = m.group(2).strip()
        name_mr = m.group(3).strip() if m.group(3) else ""
        epithet = m.group(4).strip() if m.group(4) else ""
        
        code = char_id.split("-")[1]
        cat_info = cat_metadata.get(code, {
            "title": "General", "mr": "सर्वसाधारण", "color": "var(--accent-cyan)", "badge_color": "rgba(6, 182, 212, 0.2)", "icon": "👤"
        })
        
        role_m = re.search(r"-\s*\*\*.*?(?:Role|गट व भूमिका|अधिकारक्षेत्र).*?:\*\*\s*([^\n]+)", body, re.I)
        culture_m = re.search(r"-\s*\*\*.*?(?:Culture|Lineage|वंश व संस्कृती|संस्कृती व वंश).*?:\*\*\s*([^\n]+)", body, re.I)
        era_m = re.search(r"-\s*\*\*.*?(?:Era|ऐतिहासिक युग).*?:\*\*\s*([^\n]+)", body, re.I)
        moral_m = re.search(r"-\s*\*\*.*?(?:Moral|नैतिक स्थिती|नैतिक सीमांत).*?:\*\*\s*([^\n]+)", body, re.I)
        anatomy_m = re.search(r"-\s*\*\*.*?(?:Anatomy|शारीरिक संग्रह).*?:\*\*([\s\S]*?)(?=(?:-\s*\*\*|\n---|\Z))", body, re.I)
        
        psycho_m = re.search(r"-\s*\*\*.*?(?:Psychological|मानसिक प्रोफाईल|Character, Psychology & Hook).*?:\*\*([\s\S]*?)(?=(?:-\s*\*\*|\n---|\Z))", body, re.I)
        
        scale_m = re.search(r"\*(?:साधना-स्तर \(Scale Band\)|Scale Band):\*\s*([^\n]+)", body, re.I)
        if not scale_m:
            scale_m = re.search(r"-\s*\*\*.*?(?:Power Bracket & Scale Band|साधना-स्तर).*?:\*\*\s*([^\n]+)", body, re.I)
            
        arts_m = re.search(r"\*(?:सक्रिय कौशल्ये व विद्या \(Active Arts\)|Active Arts):\*\s*([^\n]+)", body, re.I)
        if not arts_m:
            arts_m = re.search(r"-\s*\*\*.*?(?:Quirk & Magic|सक्रिय कौशल्ये).*?:\*\*\s*([^\n]+)", body, re.I)
            
        weapons_m = re.search(r"\*(?:अधिकृत शस्त्रागार \(Arsenal\)|Arsenal):\*\s*([^\n]+)", body, re.I)
        if not weapons_m:
            weapons_m = re.search(r"-\s*\*\*.*?(?:Weaponry & Arsenal|अधिकृत शस्त्रागार|शस्त्रागार).*?:\*\*\s*([^\n]+)", body, re.I)
        
        relations_m = re.search(r"-\s*\*\*.*?(?:Relations|नाती).*?:\*\*\s*([^\n]+(?:\n\s+[^\n]+)*)", body, re.I)
        shard_m = re.search(r"-\s*\*\*.*?(?:Planetary Shard|स्थान|ग्रह-खंड).*?:\*\*\s*([^\n]+)", body, re.I)
        vanguard_m = re.search(r"-\s*\*\*.*?(?:Vanguard|सहजीवी|श्वापद|Soul-Bond|Prana-Bond).*?:\*\*\s*([^\n]+)", body, re.I)
        
        # Format anatomy
        clean_anatomy = anatomy_m.group(1).strip() if anatomy_m else "मानक नश्वर शरीर."
        clean_anatomy = re.sub(r"\s+", " ", clean_anatomy)
        
        # Format psychology
        clean_psycho = ""
        if psycho_m:
            lines = psycho_m.group(1).strip().splitlines()
            cleaned_lines = []
            for l in lines:
                l_s = l.strip()
                if l_s.startswith("*") or l_s.startswith("-"):
                    cleaned_lines.append(l_s.lstrip("*- ").strip())
            clean_psycho = " • ".join(cleaned_lines)
        if not clean_psycho:
            clean_psycho = "सभ्यतेचे कर्तव्य, व्यक्तिगत निष्ठा व संस्थात्मक नियमांचे पालन."
            
        clean_relations = relations_m.group(1).strip() if relations_m else "संबंधित क्षेत्रातील समकालीन सहकाऱ्यांशी कार्यरत संबंध."
        clean_relations = re.sub(r"\s+", " ", clean_relations)
        
        characters.append({
            "id": char_id,
            "name": name,
            "name_mr": name_mr,
            "epithet": epithet,
            "category_code": code,
            "category_title": cat_info["title"],
            "category_mr": cat_info["mr"],
            "accent_color": cat_info["color"],
            "badge_color": cat_info["badge_color"],
            "icon": cat_info["icon"],
            "role": role_m.group(1).strip() if role_m else "क्षेत्र अधिकारी",
            "culture": culture_m.group(1).strip() if culture_m else "स्थानिक रक्तरेषा व सांस्कृतिक परंपरा",
            "era": era_m.group(1).strip() if era_m else "Era 4: Kali Yuga (वर्तमान कलि युग)",
            "shard": shard_m.group(1).strip() if shard_m else "Astral Sub-Realm",
            "vanguard": vanguard_m.group(1).strip() if vanguard_m else "Standard Status",
            "moral": moral_m.group(1).strip() if moral_m else "कायदेशीर तटस्थ (Lawful Neutral)",
            "anatomy": clean_anatomy,
            "psychology": clean_psycho,
            "scale_band": scale_m.group(1).strip() if scale_m else "T1 (Mortal)",
            "active_arts": arts_m.group(1).strip() if arts_m else "Non-Combat Arts",
            "arsenal": weapons_m.group(1).strip() if weapons_m else "Standard Secular Equipment",
            "relationships": clean_relations
        })
        
    return characters

def generate_html(characters):
    chars_json = json.dumps(characters, ensure_ascii=False)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Universe B — Master Character Dossier (120 Canonical Entities)</title>
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
  max-width: 1480px;
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
  font-size: 2.1rem;
  letter-spacing: 2px;
  background: linear-gradient(135deg, #fff 30%, var(--accent-gold-light) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.logo-area p {{
  color: var(--text-muted);
  font-size: 0.92rem;
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
  max-width: 1480px;
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
  min-width: 320px;
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

/* Realm / Category Pills */
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
  padding: 7px 14px;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.2s;
  user-select: none;
  display: flex;
  align-items: center;
  gap: 6px;
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
  max-width: 1480px;
  margin: 0 auto 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  color: var(--text-dim);
  font-family: var(--font-mono);
}}

/* Character Cards Grid */
.cards-grid {{
  max-width: 1480px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(460px, 1fr));
  gap: 22px;
}}

.char-card {{
  background: var(--bg-card);
  backdrop-filter: blur(14px);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 22px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
  position: relative;
  overflow: hidden;
}}

.char-card::before {{
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: var(--card-accent, var(--accent-cyan));
}}

.char-card:hover {{
  transform: translateY(-3px);
  border-color: rgba(255, 255, 255, 0.28);
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.45);
}}

.card-top {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
}}

.char-id {{
  font-family: var(--font-mono);
  font-size: 0.82rem;
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
  flex-wrap: wrap;
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
.badge-realm {{ background: rgba(148, 163, 184, 0.12); color: #cbd5e1; border: 1px solid rgba(148, 163, 184, 0.2); }}

.card-title h3 {{
  font-family: var(--font-display);
  font-size: 1.3rem;
  color: #fff;
  letter-spacing: 0.5px;
}}

.card-title .vernacular {{
  color: var(--text-muted);
  font-size: 0.9rem;
  font-weight: 400;
  margin-top: 2px;
}}

.card-title .epithet-badge {{
  display: inline-block;
  background: rgba(251, 191, 36, 0.12);
  border: 1px solid rgba(251, 191, 36, 0.28);
  color: var(--accent-gold-light);
  font-size: 0.76rem;
  font-family: var(--font-mono);
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 4px;
  margin-top: 4px;
}}

/* Identity & Sociological Spec */
.identity-box {{
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

.spec-val.role {{
  color: #fff;
  font-weight: 600;
}}

.spec-val.moral {{
  color: var(--accent-cyan-light);
}}

/* Anatomy & Psychology Callouts */
.section-callout {{
  border-left: 2px solid;
  padding-left: 10px;
  font-size: 0.82rem;
  line-height: 1.45;
}}

.callout-anatomy {{
  border-color: var(--accent-cyan);
  background: rgba(6, 182, 212, 0.05);
  padding: 8px 10px;
  border-radius: 0 6px 6px 0;
}}

.callout-anatomy .lbl {{
  color: var(--accent-cyan-light);
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 2px;
}}

.callout-power {{
  border-color: var(--accent-gold);
  background: rgba(245, 158, 11, 0.06);
  padding: 10px;
  border-radius: 0 6px 6px 0;
}}

.callout-power .lbl {{
  color: var(--accent-gold-light);
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 4px;
}}

.power-line {{
  font-size: 0.84rem;
  margin-bottom: 3px;
}}

.power-tag {{
  color: var(--accent-gold-light);
  font-weight: 600;
  font-family: var(--font-mono);
  font-size: 0.78rem;
}}

.callout-psycho {{
  border-color: var(--accent-purple);
  background: rgba(168, 85, 247, 0.05);
  padding: 8px 10px;
  border-radius: 0 6px 6px 0;
}}

.callout-psycho .lbl {{
  color: #c084fc;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 2px;
}}

.callout-relations {{
  border-color: var(--text-dim);
  background: rgba(148, 163, 184, 0.04);
  padding: 8px 10px;
  border-radius: 0 6px 6px 0;
  font-size: 0.8rem;
  color: var(--text-muted);
}}

.callout-relations .lbl {{
  color: var(--text-dim);
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 2px;
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
    <h1>UNIVERSE B • MASTER CHARACTER DOSSIER</h1>
    <p>120 Verified Canonical Entities • Full Psychological Profiles, Anatomy, Scale Bands &amp; Dhanurveda Arsenal</p>
  </div>
  <div class="nav-links">
    <a href="index.html" class="btn-nav">← Master Portal</a>
    <a href="ability_codex.html" class="btn-nav">⚡ Ability Codex (83)</a>
  </div>
</header>

<div class="controls-panel">
  <div class="search-row">
    <div class="search-input-box">
      <span class="search-icon">🔍</span>
      <input type="text" id="searchInput" placeholder="Search by character name, Marathi title, ID, weapon, role, or active ability..." oninput="filterCharacters()">
    </div>
    <div class="select-filters">
      <select id="tierFilter" onchange="filterCharacters()">
        <option value="ALL">All Scale Bands (T0–T7+)</option>
        <option value="T0">T0 Supreme Trinity</option>
        <option value="T1">T1 Mortal Baseline</option>
        <option value="T2">T2 Mortal Plus / Craftsman</option>
        <option value="T3">T3 Trained Baseline</option>
        <option value="T4">T4 Trained Expert</option>
        <option value="T5">T5 Awakened Master</option>
        <option value="T6">T6 Ascendent / Apocalyptic</option>
        <option value="T7">T7+ Cosmic Transcendent</option>
      </select>
      <select id="eraFilter" onchange="filterCharacters()">
        <option value="ALL">All Historical Eras (सर्व युगे)</option>
        <option value="Era 1">Era 1: Primordial Genesis (आदि-युग)</option>
        <option value="Era 2">Era 2: Void Cataclysm (महा-भ्रंश युग)</option>
        <option value="Era 3">Era 3: The Great Partition (महा-विभाजन युग)</option>
        <option value="Era 4">Era 4: Kali Yuga (वर्तमान कलि युग)</option>
      </select>
      <select id="moralFilter" onchange="filterCharacters()">
        <option value="ALL">All Moral Alignments</option>
        <option value="कायदेशीर">Lawful Alignments (कायदेशीर)</option>
        <option value="तटस्थ">Neutral Alignments (तटस्थ)</option>
        <option value="अराजक">Chaotic Alignments (अराजक)</option>
        <option value="सज्जन">Good Alignments (सज्जन)</option>
        <option value="वाईट">Evil Alignments (वाईट / करडा)</option>
      </select>
    </div>
  </div>

  <div class="category-pills" id="categoryPills">
    <div class="pill active" onclick="setCategory('ALL', this)">All Entities (120)</div>
    <div class="pill" onclick="setCategory('HUM', this)">🏛️ Humans (22)</div>
    <div class="pill" onclick="setCategory('ASU', this)">🌋 Asuras (16)</div>
    <div class="pill" onclick="setCategory('DEV', this)">☁️ Devas (10)</div>
    <div class="pill" onclick="setCategory('BST', this)">🐾 Beasts (10)</div>
    <div class="pill" onclick="setCategory('CEN', this)">⚖️ Central Astral (8)</div>
    <div class="pill" onclick="setCategory('SET', this)">🛡️ Buffer Zone Setu (17)</div>
    <div class="pill" onclick="setCategory('ABY', this)">💀 Abyssal Corrupted (13)</div>
    <div class="pill" onclick="setCategory('DIV', this)">🔱 Divine &amp; Trinity (14)</div>
    <div class="pill" onclick="setCategory('ALN', this)">🚀 The Aliens (10)</div>
  </div>
</div>

<div class="stats-bar">
  <span id="resultsCount">Showing {len(characters)} of {len(characters)} Entities</span>
  <span>Universe B Canon Matrix • 120 Verified Canonical Entities</span>
</div>

<div class="cards-grid" id="cardsGrid">
  <!-- Populated by JS -->
</div>

<script>
const CHARACTERS = {chars_json};

let currentCategory = 'ALL';

function renderCards(list) {{
  const grid = document.getElementById("cardsGrid");
  document.getElementById("resultsCount").innerText = `Showing ${{list.length}} of ${{CHARACTERS.length}} Entities`;
  
  if (list.length === 0) {{
    grid.innerHTML = `<div class="no-results">No canonical characters match the selected criteria.</div>`;
    return;
  }}
  
  let html = "";
  for (const c of list) {{
    const tierShort = c.scale_band.split(' ')[0];
    
    html += `
    <div class="char-card" style="--card-accent: ${{c.accent_color}}">
      <div class="card-top">
        <span class="char-id">${{c.id}}</span>
        <div class="badges-row">
          <span class="badge badge-canon">[CANON]</span>
          <span class="badge badge-tier">${{tierShort}}</span>
          <span class="badge badge-realm">${{c.category_title}}</span>
        </div>
      </div>
      
      <div class="card-title">
        <h3>${{c.name}}</h3>
        <div class="vernacular">${{c.name_mr ? c.name_mr : ''}}</div>
        ${{c.epithet ? `<div class="epithet-badge">${{c.epithet}}</div>` : ''}}
      </div>
      
      <div class="identity-box">
        <div class="spec-item">
          <span class="spec-label">Historical Era &amp; Lifespan</span>
          <span class="spec-val" style="color: var(--accent-gold); font-weight: 600;">⏳ ${{c.era}}</span>
        </div>
        <div class="spec-item">
          <span class="spec-label">Planetary Shard &amp; Demographics</span>
          <span class="spec-val" style="color: var(--accent-cyan-light); font-weight: 600;">🪐 ${{c.shard}}</span>
        </div>
        <div class="spec-item">
          <span class="spec-label">Vanguard League &amp; Soul-Bond</span>
          <span class="spec-val" style="color: #34d399; font-weight: 600;">🦅 ${{c.vanguard}}</span>
        </div>
        <div class="spec-item">
          <span class="spec-label">Role &amp; Faction</span>
          <span class="spec-val role">${{c.role}}</span>
        </div>
        <div class="spec-item">
          <span class="spec-label">Lineage &amp; Culture</span>
          <span class="spec-val">${{c.culture}}</span>
        </div>
        <div class="spec-item">
          <span class="spec-label">Moral Stance</span>
          <span class="spec-val moral">${{c.moral}}</span>
        </div>
      </div>
      
      <div class="section-callout callout-power">
        <div class="lbl">⚡ Powers, Scale Band &amp; Arsenal</div>
        <div class="power-line"><span class="power-tag">Scale Band:</span> ${{c.scale_band}}</div>
        <div class="power-line"><span class="power-tag">Active Arts:</span> ${{c.active_arts}}</div>
        <div class="power-line"><span class="power-tag">Arsenal:</span> ${{c.arsenal}}</div>
      </div>
      
      <div class="section-callout callout-anatomy">
        <div class="lbl">🧬 Physical Dossier &amp; Anatomy</div>
        <div>${{c.anatomy}}</div>
      </div>
      
      <div class="section-callout callout-psycho">
        <div class="lbl">🧠 Psychological Profile</div>
        <div>${{c.psychology}}</div>
      </div>
      
      <div class="section-callout callout-relations">
        <div class="lbl">🔗 Faction Relations &amp; Bonds</div>
        <div>${{c.relationships}}</div>
      </div>
    </div>`;
  }}
  grid.innerHTML = html;
}}

function setCategory(catCode, elem) {{
  currentCategory = catCode;
  document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
  elem.classList.add('active');
  filterCharacters();
}}

function filterCharacters() {{
  const query = document.getElementById("searchInput").value.toLowerCase().trim();
  const tier = document.getElementById("tierFilter").value;
  const era = document.getElementById("eraFilter").value;
  const moral = document.getElementById("moralFilter").value;
  
  const filtered = CHARACTERS.filter(c => {{
    if (currentCategory !== 'ALL' && c.category_code !== currentCategory) return false;
    if (tier !== "ALL" && !c.scale_band.includes(tier)) return false;
    if (era !== "ALL" && !c.era.includes(era)) return false;
    if (moral !== "ALL" && !c.moral.includes(moral)) return false;
    
    if (query) {{
      const matchText = (c.id + " " + c.name + " " + c.name_mr + " " + c.epithet + " " + c.role + " " + c.culture + " " + c.era + " " + c.moral + " " + c.anatomy + " " + c.psychology + " " + c.scale_band + " " + c.active_arts + " " + c.arsenal + " " + c.relationships).toLowerCase();
      if (!matchText.includes(query)) return false;
    }}
    return true;
  }});
  
  renderCards(filtered);
}}

// Initial Render
renderCards(CHARACTERS);
</script>

</body>
</html>"""

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    size_kb = round(os.path.getsize(output_html) / 1024, 1)
    print(f"Generated standalone Master Character Dossier UI at: {output_html} ({size_kb} KB)")

if __name__ == "__main__":
    chars = parse_characters()
    print(f"Parsed {len(chars)} characters.")
    generate_html(chars)
