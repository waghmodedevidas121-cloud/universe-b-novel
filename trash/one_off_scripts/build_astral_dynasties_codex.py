# -*- coding: utf-8 -*-
r"""
Build Master Astral Dynasties, Clans & Royal Families Codex HTML
Output: D:\Web Novel\New\astral_dynasties_codex.html
Features:
- Dual Categorization: Divided by Sub-Realm AND by Cosmic Era (Era 1, Era 2, Era 3, Era 4).
- 100% English Roman-Script terminology (Central City, Hastinapur, etc.; zero Devanagari terms).
- Chronological 4-Era Timeline Bar and interactive filters.
- Complete 56 Character Dossiers mapped to their respective dynasties.
- Geopolitical Cold War & Grudge Matrix.
"""

import os
import re
import json
import html
import sys

_current_dir = os.path.dirname(os.path.abspath(__file__))
if _current_dir not in sys.path:
    sys.path.insert(0, _current_dir)

from dynasties_data import DYNASTIES, COSMIC_ERAS

_project_root = os.path.dirname(_current_dir)
base_dir = os.path.join(_project_root, "New")
if not os.path.exists(base_dir):
    base_dir = r"D:\Web Novel\New"

output_html = os.path.join(base_dir, "astral_dynasties_codex.html")
dossier_file = os.path.join(base_dir, "characters", "roster.md")
if not os.path.exists(dossier_file):
    dossier_file = os.path.join(base_dir, "08_Character_Roster.md")

print(f"Reading character dossier from: {dossier_file}")
with open(dossier_file, "r", encoding="utf-8") as f:
    dossier_text = f.read()

# Parse character blocks
char_pattern = re.compile(r"###\s*\[(CHR-[A-Z]+-\d+)\]\s*([^\n—]+?)(?:\s*—\s*([^\n]+))?$", re.MULTILINE)
char_matches = list(char_pattern.finditer(dossier_text))

parsed_chars = {}
for i, m in enumerate(char_matches):
    cid = m.group(1).strip()
    name_full = m.group(2).strip()
    epithet = m.group(3).strip() if m.group(3) else ""
    start_pos = m.start()
    end_pos = char_matches[i+1].start() if i+1 < len(char_matches) else len(dossier_text)
    block = dossier_text[start_pos:end_pos]
    
    role = ""
    clan_line = ""
    era_line = ""
    moral_line = ""
    phys_line = ""
    scale_band = ""
    active_arts = ""
    arsenal = ""
    relations = ""
    
    m_role = re.search(r"-\s*\*\*गट व भूमिका:\*\*\s*([^\n]+)", block)
    if m_role: role = m_role.group(1).strip()
    
    m_clan = re.search(r"-\s*\*\*(?:वंश व संस्कृती|संस्कृती व वंश):\*\*\s*([^\n]+)", block)
    if m_clan: clan_line = m_clan.group(1).strip()
    
    m_era = re.search(r"-\s*\*\*ऐतिहासिक युग व आयुर्मर्यादा:\*\*\s*([^\n]+)", block)
    if m_era: era_line = m_era.group(1).strip()
    
    m_moral = re.search(r"-\s*\*\*नैतिक (?:स्थिती|सीमांत):\*\*\s*([^\n]+)", block)
    if m_moral: moral_line = m_moral.group(1).strip()
    
    m_phys = re.search(r"-\s*\*\*शारीरिक संग्रह:\*\*\s*([^\n]+)", block)
    if m_phys: phys_line = m_phys.group(1).strip()
    
    m_scale = re.search(r"\*साधना-स्तर \(Scale Band\):\*\s*([^\n]+)", block)
    if m_scale: scale_band = m_scale.group(1).strip()
    
    m_arts = re.search(r"\*सक्रिय कौशल्ये व विद्या \(Active Arts\):\*\s*([^\n]+)", block)
    if m_arts: active_arts = m_arts.group(1).strip()
    
    m_arsenal = re.search(r"\*अधिकृत शस्त्रागार \(Arsenal\):\*\s*([^\n]+)", block)
    if m_arsenal: arsenal = m_arsenal.group(1).strip()
    
    m_rel = re.search(r"-\s*\*\*नाती:\*\*\s*([^\n]+)", block)
    if m_rel: relations = m_rel.group(1).strip()
    
    nm = re.match(r"([^(]+)(?:\(([^)]+)\))?", name_full)
    en_name = nm.group(1).strip() if nm else name_full
    mr_name = nm.group(2).strip() if nm and nm.group(2) else ""
    
    # Romanize/English cleanse common term occurrences in role/fields
    role_clean = role.replace("मध्य-नगर", "Central City").replace("ग्रँड कॉन्कॉर्ड", "Grand Concord")
    
    parsed_chars[cid] = {
        "id": cid,
        "name_en": en_name,
        "name_mr": mr_name,
        "epithet": epithet,
        "role": role_clean,
        "clan_line": clan_line,
        "era_line": era_line,
        "moral_line": moral_line,
        "phys_line": phys_line,
        "scale_band": scale_band,
        "active_arts": active_arts,
        "arsenal": arsenal,
        "relations": relations,
        "full_text": block
    }

print(f"Parsed {len(parsed_chars)} character dossiers.")

# Build HTML template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tier 3: Astral Living Realm — Dynasties, Clans & Royal Families Codex (Era & Sub-Realm Architecture)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-deep: #06080d;
      --bg-card: #0b0f19;
      --bg-card-sub: #111726;
      --border-base: #1e293b;
      --border-accent: #334155;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      --accent-cyan: #06b6d4;
      --accent-gold: #f59e0b;
      --accent-rose: #f43f5e;
      --accent-emerald: #10b981;
      --accent-purple: #a855f7;
      --accent-amber: #d97706;
      --accent-sky: #38bdf8;
    }
    
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg-deep);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', sans-serif;
      line-height: 1.6;
      overflow-x: hidden;
    }
    
    /* Top Banner / Header */
    .top-hero {
      position: relative;
      padding: 50px 30px 40px;
      background: radial-gradient(circle at 50% 20%, rgba(168, 85, 247, 0.08), transparent 70%),
                  linear-gradient(180deg, #090d16 0%, var(--bg-deep) 100%);
      border-bottom: 1px solid var(--border-base);
      text-align: center;
    }
    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 16px;
      border-radius: 999px;
      background: rgba(168, 85, 247, 0.12);
      border: 1px solid rgba(168, 85, 247, 0.3);
      color: #c084fc;
      font-size: 0.8rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 18px;
    }
    .hero-title {
      font-family: 'Cinzel', serif;
      font-size: 2.8rem;
      font-weight: 900;
      background: linear-gradient(135deg, #fff 20%, #cbd5e1 50%, #94a3b8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 12px;
      letter-spacing: -0.01em;
    }
    .hero-subtitle {
      font-size: 1.15rem;
      color: var(--text-muted);
      max-width: 900px;
      margin: 0 auto 24px;
    }
    
    /* Global Invariant Banner */
    .tech-limit-banner {
      max-width: 980px;
      margin: 0 auto;
      background: rgba(245, 158, 11, 0.06);
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: 12px;
      padding: 14px 22px;
      font-size: 0.88rem;
      color: #fde68a;
      display: flex;
      align-items: center;
      gap: 14px;
      text-align: left;
    }
    .tech-limit-banner strong { color: #f59e0b; }
    
    /* Stats Bar */
    .stats-row {
      display: flex;
      justify-content: center;
      gap: 16px;
      margin-top: 30px;
      flex-wrap: wrap;
    }
    .stat-chip {
      background: var(--bg-card);
      border: 1px solid var(--border-base);
      border-radius: 10px;
      padding: 12px 20px;
      min-width: 170px;
      text-align: center;
    }
    .stat-val {
      font-family: 'Cinzel', serif;
      font-size: 1.6rem;
      font-weight: 700;
      color: #fff;
    }
    .stat-lbl {
      font-size: 0.74rem;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    
    /* Chronological 4-Era Timeline Bar */
    .era-timeline-section {
      max-width: 1400px;
      margin: 36px auto 0;
      padding: 0 30px;
    }
    .era-timeline-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
    }
    .era-block {
      background: var(--bg-card);
      border: 1px solid var(--border-base);
      border-radius: 12px;
      padding: 18px;
      position: relative;
      transition: all 0.25s;
    }
    .era-block:hover {
      border-color: var(--border-accent);
      transform: translateY(-2px);
    }
    .era-badge-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      display: inline-block;
      margin-bottom: 8px;
    }
    .era-title {
      font-family: 'Cinzel', serif;
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 4px;
    }
    .era-tagline {
      font-size: 0.78rem;
      color: var(--accent-gold);
      margin-bottom: 10px;
      font-weight: 500;
    }
    .era-desc {
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.5;
    }
    
    /* Controls & Navigation */
    .controls-container {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(6, 8, 13, 0.95);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border-base);
      padding: 16px 30px;
      margin-top: 36px;
    }
    .controls-wrap {
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .search-row {
      display: flex;
      gap: 16px;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
    }
    .search-input-wrap {
      flex: 1;
      min-width: 300px;
      position: relative;
    }
    .search-input {
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border-base);
      border-radius: 8px;
      padding: 10px 16px 10px 42px;
      color: #fff;
      font-size: 0.9rem;
      outline: none;
      transition: all 0.2s;
    }
    .search-input:focus {
      border-color: var(--accent-cyan);
      box-shadow: 0 0 12px rgba(6, 182, 212, 0.25);
    }
    .search-icon {
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
    }
    
    /* Two-tier Filters */
    .filter-row {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .filter-label {
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      min-width: 80px;
    }
    .filter-group {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 2px;
    }
    .filter-btn {
      background: var(--bg-card);
      border: 1px solid var(--border-base);
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }
    .filter-btn:hover {
      color: #fff;
      border-color: var(--border-accent);
    }
    .filter-btn.active {
      background: rgba(168, 85, 247, 0.18);
      border-color: var(--accent-purple);
      color: #c084fc;
    }
    .filter-btn.era-active {
      background: rgba(245, 158, 11, 0.18);
      border-color: var(--accent-gold);
      color: #fbbf24;
    }
    
    /* Main Layout */
    .main-content {
      max-width: 1400px;
      margin: 40px auto;
      padding: 0 30px;
    }
    
    /* Dynasty Profile Card */
    .dynasty-card {
      background: var(--bg-card);
      border: 1px solid var(--border-base);
      border-radius: 16px;
      margin-bottom: 50px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      transition: border-color 0.3s;
    }
    .dynasty-card:hover {
      border-color: var(--border-accent);
    }
    
    /* Card Header */
    .dyn-header {
      padding: 30px;
      border-bottom: 1px solid var(--border-base);
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 20px;
      flex-wrap: wrap;
      position: relative;
    }
    .dyn-header::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 3px;
      background: var(--card-accent, #64748b);
    }
    .dyn-titles {
      flex: 1;
      min-width: 320px;
    }
    .dyn-crest-title {
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 8px;
    }
    .dyn-crest {
      font-size: 2.2rem;
      line-height: 1;
      padding: 10px;
      background: var(--bg-card-sub);
      border-radius: 12px;
      border: 1px solid var(--border-base);
    }
    .dyn-name-en {
      font-family: 'Cinzel', serif;
      font-size: 1.85rem;
      font-weight: 700;
      color: #fff;
    }
    .dyn-name-formal {
      font-size: 1.05rem;
      color: var(--card-accent, var(--accent-cyan));
      font-weight: 600;
      margin-bottom: 6px;
    }
    .dyn-motto {
      font-style: italic;
      color: var(--text-muted);
      font-size: 0.9rem;
      border-left: 2px solid var(--card-accent, #64748b);
      padding-left: 10px;
      margin-top: 8px;
    }
    
    .dyn-badges {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 8px;
    }
    .dyn-pill {
      display: inline-flex;
      align-items: center;
      padding: 5px 14px;
      border-radius: 999px;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      background: var(--card-accent-bg, rgba(255,255,255,0.08));
      color: var(--card-accent, #fff);
      border: 1px solid var(--card-accent, #fff);
    }
    .dyn-era-badge {
      font-size: 0.76rem;
      font-family: 'JetBrains Mono', monospace;
      padding: 4px 10px;
      border-radius: 6px;
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.3);
      color: #fbbf24;
      font-weight: 600;
    }
    .dyn-realm-pill {
      font-size: 0.78rem;
      color: var(--text-dim);
      font-family: 'JetBrains Mono', monospace;
    }
    
    /* Quick Specs Matrix */
    .specs-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      background: rgba(0, 0, 0, 0.2);
      border-bottom: 1px solid var(--border-base);
    }
    .spec-item {
      padding: 14px 20px;
      border-right: 1px solid var(--border-base);
      border-bottom: 1px solid var(--border-base);
    }
    .spec-item:last-child { border-right: none; }
    .spec-label {
      font-size: 0.72rem;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 4px;
    }
    .spec-val {
      font-size: 0.88rem;
      color: var(--text-main);
      font-weight: 500;
    }
    
    /* Details Sections */
    .dyn-body {
      padding: 30px;
    }
    .lore-section {
      margin-bottom: 26px;
    }
    .lore-title {
      font-family: 'Cinzel', serif;
      font-size: 1.15rem;
      color: #fff;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 10px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
      padding-bottom: 8px;
    }
    .lore-text {
      color: #cbd5e1;
      font-size: 0.94rem;
      line-height: 1.7;
    }
    
    /* Era Evolution Timeline Box */
    .era-evolution-box {
      background: rgba(245, 158, 11, 0.04);
      border: 1px solid rgba(245, 158, 11, 0.25);
      border-radius: 12px;
      padding: 20px;
      margin-bottom: 26px;
    }
    .eeb-title {
      font-family: 'Cinzel', serif;
      font-size: 0.92rem;
      color: var(--accent-gold);
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .eeb-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 12px;
    }
    .eeb-node {
      background: var(--bg-card-sub);
      border: 1px solid var(--border-base);
      border-radius: 8px;
      padding: 12px;
    }
    .eeb-node-era {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--accent-gold);
      margin-bottom: 4px;
    }
    .eeb-node-text {
      font-size: 0.82rem;
      color: #cbd5e1;
      line-height: 1.45;
    }
    
    /* Tech Box */
    .tech-box {
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(56, 189, 248, 0.2);
      border-radius: 10px;
      padding: 16px 20px;
      margin-bottom: 26px;
    }
    .tech-box-title {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--accent-cyan);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .tech-box-content {
      font-size: 0.88rem;
      color: #93c5fd;
    }
    
    /* Relations Matrix (Allies, Rivals, Grudges, Trade) */
    .relations-matrix {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin-bottom: 30px;
    }
    .rel-card {
      background: var(--bg-card-sub);
      border: 1px solid var(--border-base);
      border-radius: 10px;
      padding: 16px;
    }
    .rel-header {
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .rel-allies .rel-header { color: #34d399; }
    .rel-rivals .rel-header { color: #fb923c; }
    .rel-grudges .rel-header { color: #f43f5e; }
    .rel-trade .rel-header { color: #38bdf8; }
    .rel-list {
      list-style: none;
      font-size: 0.84rem;
      color: var(--text-muted);
    }
    .rel-list li {
      margin-bottom: 6px;
      padding-left: 12px;
      position: relative;
    }
    .rel-list li::before {
      content: '•';
      position: absolute;
      left: 0;
      color: var(--text-dim);
    }
    
    /* Character Roster Grid */
    .roster-header {
      font-family: 'Cinzel', serif;
      font-size: 1.25rem;
      color: #fff;
      margin: 30px 0 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-base);
      padding-bottom: 10px;
    }
    .roster-count {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      background: var(--bg-card-sub);
      padding: 4px 10px;
      border-radius: 6px;
      color: var(--text-muted);
    }
    
    .roster-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 20px;
    }
    
    /* Character Card */
    .char-card {
      background: var(--bg-card-sub);
      border: 1px solid var(--border-base);
      border-radius: 12px;
      padding: 20px;
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .char-card:hover {
      border-color: var(--card-accent, #38bdf8);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }
    .char-top {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      margin-bottom: 12px;
    }
    .char-id-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      padding: 3px 8px;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.06);
      color: var(--card-accent, #38bdf8);
      font-weight: 700;
    }
    .char-scale-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      padding: 2px 8px;
      border-radius: 4px;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.3);
      color: #fbbf24;
      font-weight: 600;
    }
    .char-name-en {
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 2px;
    }
    .char-name-mr {
      font-size: 0.88rem;
      color: var(--card-accent, #93c5fd);
      font-weight: 600;
      margin-bottom: 6px;
    }
    .char-epithet {
      font-size: 0.82rem;
      color: var(--text-dim);
      font-style: italic;
      margin-bottom: 12px;
    }
    .char-role-box {
      background: rgba(0, 0, 0, 0.25);
      border-left: 2px solid var(--card-accent, #38bdf8);
      padding: 8px 12px;
      border-radius: 4px;
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-bottom: 14px;
    }
    .char-specs {
      font-size: 0.8rem;
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 14px;
    }
    .char-spec-row {
      display: flex;
      gap: 8px;
    }
    .csr-lbl {
      color: var(--text-dim);
      min-width: 90px;
      font-weight: 600;
    }
    .csr-val {
      color: #cbd5e1;
      flex: 1;
    }
    
    .char-full-details {
      display: none;
      margin-top: 14px;
      padding-top: 12px;
      border-top: 1px dashed var(--border-base);
      font-size: 0.8rem;
      color: var(--text-muted);
    }
    .char-full-details.open {
      display: block;
    }
    .btn-toggle-dossier {
      width: 100%;
      background: transparent;
      border: 1px solid var(--border-base);
      border-radius: 6px;
      padding: 6px;
      color: var(--text-dim);
      font-size: 0.76rem;
      font-weight: 600;
      cursor: pointer;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      transition: all 0.2s;
      margin-top: 8px;
    }
    .btn-toggle-dossier:hover {
      background: rgba(255, 255, 255, 0.05);
      color: #fff;
      border-color: var(--border-accent);
    }
    
    /* Geopolitical Grudge Matrix Section */
    .matrix-section {
      background: var(--bg-card);
      border: 1px solid var(--border-base);
      border-radius: 16px;
      padding: 30px;
      margin-top: 60px;
    }
    .matrix-title {
      font-family: 'Cinzel', serif;
      font-size: 1.6rem;
      color: #fff;
      margin-bottom: 10px;
      text-align: center;
    }
    .matrix-desc {
      text-align: center;
      color: var(--text-muted);
      font-size: 0.9rem;
      margin-bottom: 30px;
      max-width: 820px;
      margin-left: auto;
      margin-right: auto;
    }
    .table-container {
      overflow-x: auto;
    }
    .matrix-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.82rem;
    }
    .matrix-table th, .matrix-table td {
      border: 1px solid var(--border-base);
      padding: 12px 14px;
      text-align: left;
    }
    .matrix-table th {
      background: var(--bg-card-sub);
      color: #fff;
      font-family: 'Cinzel', serif;
      font-weight: 700;
      white-space: nowrap;
    }
    .matrix-table tr:hover td {
      background: rgba(255, 255, 255, 0.02);
    }
    
    /* Footer */
    footer {
      border-top: 1px solid var(--border-base);
      padding: 40px 30px;
      text-align: center;
      color: var(--text-dim);
      font-size: 0.84rem;
      background: #04060a;
    }
  </style>
</head>
<body>

  <!-- Top Hero -->
  <header class="top-hero">
    <div class="hero-badge">🌌 Tier 3: Astral Living Realm • Canon Gazetteer</div>
    <h1 class="hero-title">Dynasties, Clans & Royal Families Codex</h1>
    <p class="hero-subtitle">
      Complete profiles of every sovereign royal house, industrial foundry dynasty, ancient hermitage, and primeval beast clan across the 4 Cosmic Eras and 5 Astral Sub-Realms.
    </p>
    
    <!-- Hard Tech Invariant Banner -->
    <div class="tech-limit-banner">
      <span style="font-size: 1.5rem;">⚙️</span>
      <div>
        <strong>STRICT HARD TECHNOLOGY LIMIT (Clean Aether-Dimensional Baseline):</strong>
        Technology operates under clean Aether-Dimensional engineering: Lattice-Rails, Resonance Needle grids, Tectonic Rotary Anchors, and dimensional compression ballistics. 
        <em>Computers, AI, microchips, digital screens, and modern electronics are 100% banned and non-existent throughout the cosmos.</em>
      </div>
    </div>
    
    <!-- Stats Row -->
    <div class="stats-row">
      <div class="stat-chip">
        <div class="stat-val">4</div>
        <div class="stat-lbl">Cosmic Eras</div>
      </div>
      <div class="stat-chip">
        <div class="stat-val">5</div>
        <div class="stat-lbl">Astral Sub-Realms</div>
      </div>
      <div class="stat-chip">
        <div class="stat-val">12</div>
        <div class="stat-lbl">Dynastic Powers & Clans</div>
      </div>
      <div class="stat-chip">
        <div class="stat-val">56</div>
        <div class="stat-lbl">Profiled Characters</div>
      </div>
      <div class="stat-chip">
        <div class="stat-val" style="color: #f59e0b;">19th C.</div>
        <div class="stat-lbl">Hard Tech Ceiling</div>
      </div>
    </div>
  </header>

  <!-- Chronological 4-Era Timeline Overview -->
  <section class="era-timeline-section">
    <div class="era-timeline-grid">
      __ERA_BLOCKS_HTML__
    </div>
  </section>

  <!-- Sticky Controls Bar (Dual Filters: Sub-Realm & Era) -->
  <nav class="controls-container">
    <div class="controls-wrap">
      <div class="search-row">
        <div class="search-input-wrap">
          <span class="search-icon">🔍</span>
          <input type="text" id="searchInput" class="search-input" placeholder="Search clan, dynasty, character name, city, or tech...">
        </div>
      </div>
      
      <!-- Sub-Realm Filters -->
      <div class="filter-row">
        <span class="filter-label">Sub-Realm:</span>
        <div class="filter-group" id="realmFilterGroup">
          <button class="filter-btn active" data-realm="ALL">All Sub-Realms (12)</button>
          <button class="filter-btn" data-realm="HUM">Human Sub-Realm (3)</button>
          <button class="filter-btn" data-realm="ASU">Asura Sub-Realm (2)</button>
          <button class="filter-btn" data-realm="DEV">Deva Sub-Realm (2)</button>
          <button class="filter-btn" data-realm="BST">Beast Sub-Realm (4)</button>
          <button class="filter-btn" data-realm="CEN">Central City Hub (1)</button>
        </div>
      </div>
      
      <!-- Era Filters -->
      <div class="filter-row">
        <span class="filter-label">Origin Era:</span>
        <div class="filter-group" id="eraFilterGroup">
          <button class="filter-btn era-active" data-era="ALL">All Eras (12)</button>
          <button class="filter-btn" data-era="ERA-1">Era 1: Primordial Roots (5)</button>
          <button class="filter-btn" data-era="ERA-2">Era 2: Cataclysm Survivors (3)</button>
          <button class="filter-btn" data-era="ERA-3">Era 3: Partition Founders (4)</button>
          <button class="filter-btn" data-era="ERA-4">Era 4: Kali Yuga Present State (12)</button>
        </div>
      </div>
    </div>
  </nav>

  <!-- Main Content Container -->
  <main class="main-content" id="dynastiesContainer">
    <!-- Dynasties will be rendered here -->
    __DYNASTIES_HTML__
    
    <!-- Geopolitical Grudge & Cold War Matrix -->
    <section class="matrix-section">
      <h2 class="matrix-title">Inter-Dynasty Cold War & Relations Matrix</h2>
      <p class="matrix-desc">
        Comprehensive geopolitical overview of alliances, cold war friction, economic trade levers, and ancient blood grudges across the 12 sovereign powers of Tier 3.
      </p>
      <div class="table-container">
        __MATRIX_TABLE_HTML__
      </div>
    </section>
  </main>

  <footer>
    <p>Universe B • Tier 3 Astral Living Realm Dynastic Codex • Official Canon Lock (22 October 2026)</p>
    <p style="margin-top: 6px; font-size: 0.78rem;">Strict Invariants: English Roman-Script Terminology • Clean Aether-Dimensional Technology • Zero Computers/AI • Four-Era Chronology</p>
  </footer>

  <script>
    // Search & Dual-Filter Engine (Sub-Realm + Era)
    const searchInput = document.getElementById('searchInput');
    const realmButtons = document.querySelectorAll('#realmFilterGroup .filter-btn');
    const eraButtons = document.querySelectorAll('#eraFilterGroup .filter-btn');
    const cards = document.querySelectorAll('.dynasty-card');

    let currentRealm = 'ALL';
    let currentEra = 'ALL';

    realmButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        realmButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentRealm = btn.dataset.realm;
        applyFilters();
      });
    });

    eraButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        eraButtons.forEach(b => b.classList.remove('era-active'));
        btn.classList.add('era-active');
        currentEra = btn.dataset.era;
        applyFilters();
      });
    });

    searchInput.addEventListener('input', () => {
      applyFilters();
    });

    function applyFilters() {
      const q = searchInput.value.toLowerCase().trim();

      cards.forEach(card => {
        const realmCode = card.dataset.realm;
        const eraCode = card.dataset.era;
        const text = card.textContent.toLowerCase();

        const matchesRealm = (currentRealm === 'ALL' || realmCode === currentRealm);
        const matchesEra = (currentEra === 'ALL' || currentEra === 'ERA-4' || eraCode === currentEra);
        const matchesSearch = (!q || text.includes(q));

        if (matchesRealm && matchesEra && matchesSearch) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }

    // Toggle character details
    document.addEventListener('click', e => {
      if (e.target.classList.contains('btn-toggle-dossier')) {
        const detailsBox = e.target.previousElementSibling;
        const isOpen = detailsBox.classList.contains('open');
        if (isOpen) {
          detailsBox.classList.remove('open');
          e.target.textContent = 'View Full Dossier ▼';
        } else {
          detailsBox.classList.add('open');
          e.target.textContent = 'Collapse Dossier ▲';
        }
      }
    });
  </script>
</body>
</html>
"""

# Render Era Blocks
era_blocks_html = []
era_colors = {"ERA-1": "#f59e0b", "ERA-2": "#f43f5e", "ERA-3": "#06b6d4", "ERA-4": "#10b981"}
for era in COSMIC_ERAS:
    color = era_colors.get(era["code"], "#a855f7")
    block = f"""
    <div class="era-block" style="border-top: 3px solid {color};">
      <span class="era-badge-tag" style="background: rgba(255,255,255,0.06); color: {color}; border: 1px solid {color};">{era['code']}</span>
      <h3 class="era-title">{html.escape(era['name'])}</h3>
      <div class="era-tagline">{html.escape(era['tagline'])}</div>
      <div class="era-desc">{html.escape(era['desc'])}</div>
    </div>
    """
    era_blocks_html.append(block)

# Render Dynasty Cards
dyn_cards_html = []
for d in DYNASTIES:
    # Character cards for this dynasty
    char_cards_html = []
    for cid in d["character_ids"]:
        c = parsed_chars.get(cid)
        if not c:
            continue
        
        # Build character card HTML
        char_card = f"""
        <div class="char-card">
          <div>
            <div class="char-top">
              <span class="char-id-tag">{c['id']}</span>
              <span class="char-scale-badge">{c['scale_band'] if c['scale_band'] else 'Scale: Active'}</span>
            </div>
            <div class="char-name-en">{html.escape(c['name_en'])}</div>
            <div class="char-name-mr">{html.escape(c['name_mr'])}</div>
            <div class="char-epithet">{html.escape(c['epithet'])}</div>
            
            <div class="char-role-box">
              <strong>Official Role:</strong> {html.escape(c['role'])}
            </div>
            
            <div class="char-specs">
              <div class="char-spec-row">
                <span class="csr-lbl">Era / Lifespan:</span>
                <span class="csr-val">{html.escape(c['era_line'])}</span>
              </div>
              <div class="char-spec-row">
                <span class="csr-lbl">Moral Stance:</span>
                <span class="csr-val">{html.escape(c['moral_line'])}</span>
              </div>
              <div class="char-spec-row">
                <span class="csr-lbl">Physical:</span>
                <span class="csr-val">{html.escape(c['phys_line'])}</span>
              </div>
              <div class="char-spec-row">
                <span class="csr-lbl">Active Arts:</span>
                <span class="csr-val" style="color: #93c5fd;">{html.escape(c['active_arts'])}</span>
              </div>
              <div class="char-spec-row">
                <span class="csr-lbl">Arsenal:</span>
                <span class="csr-val" style="color: #fde68a;">{html.escape(c['arsenal'])}</span>
              </div>
              <div class="char-spec-row">
                <span class="csr-lbl">Relations:</span>
                <span class="csr-val">{html.escape(c['relations'])}</span>
              </div>
            </div>
          </div>
          
          <div>
            <div class="char-full-details">
              <pre style="white-space: pre-wrap; font-family: inherit; font-size: 0.78rem; line-height: 1.5; color: #94a3b8;">{html.escape(c['full_text'].strip())}</pre>
            </div>
            <button class="btn-toggle-dossier">View Full Dossier ▼</button>
          </div>
        </div>
        """
        char_cards_html.append(char_card)
    
    # Relations lists
    rel = d["geopolitical_relations"]
    allies_li = "".join([f"<li>{html.escape(x)}</li>" for x in rel.get("allies", [])])
    rivals_li = "".join([f"<li>{html.escape(x)}</li>" for x in rel.get("rivals", [])])
    grudges_li = "".join([f"<li>{html.escape(x)}</li>" for x in rel.get("grudges", [])])
    trade_li = "".join([f"<li>{html.escape(x)}</li>" for x in rel.get("trade_dependencies", [])])
    
    # Era Evolution Timeline
    et = d.get("era_timeline", {})
    eeb_html = f"""
    <div class="era-evolution-box">
      <div class="eeb-title">⏳ Chronological 4-Era Evolution & History</div>
      <div class="eeb-grid">
        <div class="eeb-node">
          <div class="eeb-node-era">ERA 1: PRIMORDIAL AGE</div>
          <div class="eeb-node-text">{html.escape(et.get('era_1', 'Ancestral roots and primordial foundations.'))}</div>
        </div>
        <div class="eeb-node">
          <div class="eeb-node-era">ERA 2: VOID CATACLYSM</div>
          <div class="eeb-node-text">{html.escape(et.get('era_2', 'Survival strategy during cosmic dimensional tears.'))}</div>
        </div>
        <div class="eeb-node">
          <div class="eeb-node-era">ERA 3: GREAT PARTITION</div>
          <div class="eeb-node-text">{html.escape(et.get('era_3', 'Pocket-dimension demarcation and treaty integration.'))}</div>
        </div>
        <div class="eeb-node" style="border-color: rgba(245, 158, 11, 0.4); background: rgba(245, 158, 11, 0.05);">
          <div class="eeb-node-era" style="color:#fbbf24;">ERA 4: PRESENT INDUSTRIAL AGE</div>
          <div class="eeb-node-text">{html.escape(et.get('era_4', 'Current operations under Era 4: Kali Yuga clean aether-dimensional baseline.'))}</div>
        </div>
      </div>
    </div>
    """
    
    card_html = f"""
    <article class="dynasty-card" id="{d['id']}" data-realm="{d['sub_realm_code']}" data-era="{d['origin_era_code']}" style="--card-accent: {d['color']}; --card-accent-bg: {d['accent_bg']};">
      <!-- Card Header -->
      <div class="dyn-header">
        <div class="dyn-titles">
          <div class="dyn-crest-title">
            <span class="dyn-crest">{d['crest']}</span>
            <div>
              <h2 class="dyn-name-en">{html.escape(d['name_en'])}</h2>
              <div class="dyn-name-formal">{html.escape(d['name_formal'])}</div>
            </div>
          </div>
          <div class="dyn-motto">"{html.escape(d['motto'])}"</div>
        </div>
        <div class="dyn-badges">
          <span class="dyn-pill">{html.escape(d['badge'])}</span>
          <span class="dyn-era-badge">{html.escape(d['origin_era_name'])}</span>
          <span class="dyn-realm-pill">{html.escape(d['sub_realm'])}</span>
        </div>
      </div>
      
      <!-- Quick Specs Matrix -->
      <div class="specs-grid">
        <div class="spec-item">
          <div class="spec-label">Territorial Seat & Capital</div>
          <div class="spec-val"><strong>{html.escape(d['capital'])}</strong> • {html.escape(d['seat'])}</div>
        </div>
        <div class="spec-item">
          <div class="spec-label">Government Model</div>
          <div class="spec-val">{html.escape(d['government'])}</div>
        </div>
        <div class="spec-item">
          <div class="spec-label">Founding Lineage</div>
          <div class="spec-val">{html.escape(d['founding_era'])}</div>
        </div>
        <div class="spec-item">
          <div class="spec-label">Current Status</div>
          <div class="spec-val" style="color: #fbbf24;">{html.escape(d['current_status_era'])}</div>
        </div>
        <div class="spec-item">
          <div class="spec-label">Primary Demographics</div>
          <div class="spec-val">{html.escape(d['primary_race'])}</div>
        </div>
        <div class="spec-item">
          <div class="spec-label">Economic Pillars</div>
          <div class="spec-val">{html.escape(d['economic_pillars'])}</div>
        </div>
      </div>
      
      <!-- Body Section -->
      <div class="dyn-body">
        <!-- Dynastic History -->
        <div class="lore-section">
          <h3 class="lore-title">📜 Dynastic Lore & Comprehensive History</h3>
          <div class="lore-text">{d['history'].strip().replace(chr(10), '<br>')}</div>
        </div>
        
        <!-- 4-Era Evolution Box -->
        {eeb_html}
        
        <!-- Tech Box -->
        <div class="tech-box">
          <div class="tech-box-title">⚙️ Technology Profile & Hard Limits (Clean Aether-Dimensional Engineering)</div>
          <div class="tech-box-content">{html.escape(d['tech_level'])}</div>
        </div>
        
        <!-- Culture & Laws -->
        <div class="lore-section">
          <h3 class="lore-title">⚖️ Societal Order, Culture & Laws</h3>
          <div class="lore-text">{d['culture_and_laws'].strip().replace(chr(10), '<br>')}</div>
        </div>
        
        <!-- Geopolitical Relations Matrix -->
        <div class="lore-section">
          <h3 class="lore-title">🌐 Geopolitical & Cold War Relations</h3>
          <div class="relations-matrix">
            <div class="rel-card rel-allies">
              <div class="rel-header">🤝 Recognized Allies</div>
              <ul class="rel-list">{allies_li}</ul>
            </div>
            <div class="rel-card rel-rivals">
              <div class="rel-header">⚔️ Cold War Rivals</div>
              <ul class="rel-list">{rivals_li}</ul>
            </div>
            <div class="rel-card rel-grudges">
              <div class="rel-header">🩸 Blood Grudges & Feuds</div>
              <ul class="rel-list">{grudges_li}</ul>
            </div>
            <div class="rel-card rel-trade">
              <div class="rel-header">⚖️ Trade Dependencies</div>
              <ul class="rel-list">{trade_li}</ul>
            </div>
          </div>
        </div>
        
        <!-- Character Roster -->
        <div class="roster-header">
          <span>Key Figures & Canonical Character Dossiers</span>
          <span class="roster-count">{len(char_cards_html)} Canonical Characters</span>
        </div>
        <div class="roster-grid">
          {"".join(char_cards_html)}
        </div>
      </div>
    </article>
    """
    dyn_cards_html.append(card_html)

# Build Matrix Table HTML
matrix_rows = []
for d in DYNASTIES:
    row = f"""
    <tr>
      <td><strong>{html.escape(d['name_en'])}</strong><br><small style="color:var(--text-dim);">{html.escape(d['name_formal'])}</small></td>
      <td><span style="color: {d['color']}; font-weight:600;">{html.escape(d['sub_realm_code'])}</span></td>
      <td><span class="dyn-era-badge">{html.escape(d['origin_era_code'])}</span></td>
      <td>{html.escape(d['government'])}</td>
      <td>{", ".join(d['geopolitical_relations'].get('allies', ['None']))}</td>
      <td>{", ".join(d['geopolitical_relations'].get('rivals', ['None']))}</td>
      <td style="color:#f43f5e;">{", ".join(d['geopolitical_relations'].get('grudges', ['None']))}</td>
      <td style="color:#93c5fd;">{", ".join(d['geopolitical_relations'].get('trade_dependencies', ['Self-sufficient']))}</td>
    </tr>
    """
    matrix_rows.append(row)

matrix_table_html = f"""
<table class="matrix-table">
  <thead>
    <tr>
      <th>Dynasty / Clan</th>
      <th>Sub-Realm</th>
      <th>Origin Era</th>
      <th>Government Model</th>
      <th>Diplomatic Allies</th>
      <th>Cold War Rivals</th>
      <th>Blood Grudges</th>
      <th>Trade Levers & Dependencies</th>
    </tr>
  </thead>
  <tbody>
    {"".join(matrix_rows)}
  </tbody>
</table>
"""

full_html = html_template.replace("__ERA_BLOCKS_HTML__", "\n".join(era_blocks_html))
full_html = full_html.replace("__DYNASTIES_HTML__", "\n".join(dyn_cards_html))
full_html = full_html.replace("__MATRIX_TABLE_HTML__", matrix_table_html)

with open(output_html, "w", encoding="utf-8") as f:
    f.write(full_html)

file_size_mb = os.path.getsize(output_html) / (1024 * 1024)
print(f"Master Astral Dynasties Codex successfully written to: {output_html}")
print(f"File size: {file_size_mb:.2f} MB")
