import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
portal_template_path = os.path.join(current_dir, "portal_template.html")

with open(portal_template_path, "r", encoding="utf-8") as f:
    template = f.read()

# 1. Add Story Chronicle CSS before </style>
story_css = """
/* =========================================================================
   STORY CHRONICLE & IMMERSIVE NOVEL-GRADE PORTAL STYLES
   ========================================================================= */
.story-chronicle-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 10px 10px 60px 10px;
  animation: chronicleFadeIn 0.35s ease-out;
}

@keyframes chronicleFadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

.story-hero-banner {
  background: radial-gradient(circle at 15% 20%, rgba(245, 158, 11, 0.2) 0%, transparent 45%),
              radial-gradient(circle at 85% 80%, rgba(6, 182, 212, 0.16) 0%, transparent 50%),
              linear-gradient(135deg, rgba(15, 23, 42, 0.96) 0%, rgba(5, 8, 17, 0.98) 100%);
  border: 1px solid var(--border-gold);
  border-radius: 20px;
  padding: 38px 34px;
  margin-bottom: 32px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.12);
  position: relative;
  overflow: hidden;
}

.story-hero-tagline {
  font-family: var(--font-mono);
  font-size: 0.74rem;
  letter-spacing: 2.5px;
  color: var(--accent-gold-light);
  text-transform: uppercase;
  font-weight: 700;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.story-hero-title {
  font-family: var(--font-display);
  font-size: 2.25rem;
  font-weight: 800;
  line-height: 1.28;
  background: linear-gradient(120deg, #ffffff 0%, var(--accent-gold-light) 60%, var(--accent-gold) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 16px;
}

.story-hero-lead {
  font-size: 1.05rem;
  color: #e2e8f0;
  line-height: 1.8;
  max-width: 900px;
  margin-bottom: 22px;
}

.story-hero-chips {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.story-act-card {
  background: rgba(15, 23, 42, 0.72);
  backdrop-filter: blur(14px);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 30px 28px;
  margin-bottom: 26px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.35);
  transition: all 0.25s ease;
  position: relative;
}

.story-act-card:hover {
  border-color: rgba(245, 158, 11, 0.4);
  transform: translateY(-2px);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.45);
}

.story-act-card.featured-gold {
  border-color: rgba(245, 158, 11, 0.35);
  background: linear-gradient(145deg, rgba(245, 158, 11, 0.08) 0%, rgba(15, 23, 42, 0.85) 60%);
}

.story-act-card.featured-cyan {
  border-color: rgba(6, 182, 212, 0.35);
  background: linear-gradient(145deg, rgba(6, 182, 212, 0.08) 0%, rgba(15, 23, 42, 0.85) 60%);
}

.story-act-card.featured-rose {
  border-color: rgba(244, 63, 94, 0.35);
  background: linear-gradient(145deg, rgba(244, 63, 94, 0.08) 0%, rgba(15, 23, 42, 0.85) 60%);
}

.story-act-card.featured-emerald {
  border-color: rgba(16, 185, 129, 0.35);
  background: linear-gradient(145deg, rgba(16, 185, 129, 0.08) 0%, rgba(15, 23, 42, 0.85) 60%);
}

.story-act-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
  flex-wrap: wrap;
  gap: 10px;
}

.story-act-badge {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  padding: 4px 12px;
  border-radius: 20px;
  background: rgba(245, 158, 11, 0.18);
  color: var(--accent-gold-light);
  border: 1px solid var(--border-gold);
}

.story-act-badge.cyan {
  background: rgba(6, 182, 212, 0.18);
  color: var(--accent-cyan-light);
  border-color: var(--border-cyan);
}

.story-act-badge.rose {
  background: rgba(244, 63, 94, 0.18);
  color: #fda4af;
  border-color: rgba(244, 63, 94, 0.4);
}

.story-act-badge.emerald {
  background: rgba(16, 185, 129, 0.18);
  color: #34d399;
  border-color: rgba(16, 185, 129, 0.4);
}

.story-act-title {
  font-family: var(--font-display);
  font-size: 1.48rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 14px;
  line-height: 1.35;
}

.story-prose {
  font-size: 1.02rem;
  line-height: 1.82;
  color: #cbd5e1;
  margin-bottom: 16px;
}

.story-prose p {
  margin-bottom: 14px;
}

.story-prose strong {
  color: #ffffff;
  font-weight: 600;
}

.story-callout {
  border-left: 3px solid var(--accent-gold);
  background: rgba(245, 158, 11, 0.08);
  padding: 16px 20px;
  border-radius: 0 12px 12px 0;
  margin: 18px 0;
  font-style: italic;
  color: #f1f5f9;
  line-height: 1.7;
}

.story-callout strong {
  font-style: normal;
  color: var(--accent-gold-light);
}

/* Shard Showcase Grid */
.shard-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
  gap: 18px;
  margin: 24px 0;
}

.shard-card {
  background: rgba(9, 14, 28, 0.92);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  padding: 22px 20px;
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
}

.shard-card:hover {
  transform: translateY(-4px);
  border-color: var(--accent-gold);
  box-shadow: 0 14px 30px rgba(0, 0, 0, 0.5);
}

.shard-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

.shard-card-title {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 700;
  color: #ffffff;
  display: flex;
  align-items: center;
  gap: 8px;
}

.shard-pop-badge {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  padding: 3px 8px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.4);
  font-weight: 600;
}

.shard-stat-list {
  list-style: none;
  font-size: 0.85rem;
  color: #cbd5e1;
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 12px 0;
  flex-grow: 1;
}

.shard-stat-list li strong {
  color: var(--accent-cyan-light);
}

.shard-secret-box {
  background: rgba(245, 158, 11, 0.1);
  border: 1px dashed var(--border-gold);
  border-radius: 8px;
  padding: 10px 12px;
  font-size: 0.8rem;
  color: #fef08a;
  line-height: 1.5;
  margin-top: 10px;
}

/* Threat Cards Grid */
.threat-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 14px;
  margin: 20px 0;
}

.threat-card {
  background: rgba(9, 14, 28, 0.85);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 16px 18px;
  border-left: 3px solid var(--accent-rose);
}

.threat-card h5 {
  font-family: var(--font-display);
  font-size: 1rem;
  color: #fff;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.threat-card p {
  font-size: 0.84rem;
  color: #cbd5e1;
  margin: 0;
  line-height: 1.55;
}

/* Loops Flow */
.loop-step-card {
  background: rgba(9, 14, 28, 0.85);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 18px 22px;
  margin-bottom: 12px;
  border-left: 3px solid var(--accent-cyan);
}

.loop-step-card h5 {
  font-family: var(--font-display);
  font-size: 1.05rem;
  color: #ffffff;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.loop-step-card p {
  font-size: 0.86rem;
  color: #cbd5e1;
  margin: 0;
  line-height: 1.6;
}

/* Story Nav Switchers */
.story-nav-section {
  padding: 12px 14px 6px;
  border-bottom: 1px solid var(--border-color);
  margin-bottom: 8px;
}

.nav-section-label {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: var(--text-dim);
  letter-spacing: 1.5px;
  text-transform: uppercase;
  margin-bottom: 8px;
  padding-left: 4px;
  font-weight: 700;
}

.story-mode-switch-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: linear-gradient(135deg, var(--accent-gold) 0%, #d97706 100%);
  color: #050811;
  font-family: var(--font-sans);
  font-size: 0.8rem;
  font-weight: 700;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.2s;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.3);
}

.story-mode-switch-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 18px rgba(245, 158, 11, 0.45);
}
"""

if "/* Story Chronicle & Immersive Narrative Styling */" not in template:
    template = template.replace("</style>", story_css + "\n</style>")

print("CSS inserted successfully!")
