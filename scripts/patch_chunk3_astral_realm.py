import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r'd:\Web Novel\UNIVERSE B\New\06_The_Astral_Realm.md'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update lines 89-93 (Supreme Governance of Central City)
old_gov = '''- **सर्वोच्च प्रशासकीय नेतृत्व:**
  - *High Chancellor Sulabha:* ग्रँड कॉन्कॉर्ड असेंब्लीच्या सर्वोच्च अध्यक्षा.
  - *High Governor Ambika:* आकाश-कोश मध्यवर्ती बँकेची महा-प्रशासक.
  - *Magistrate Sudeva & Chief Magistrate Vikarna:* मध्यवर्ती सर्वोच्च न्यायालयाचे अभ्रष्ट धर्मदंड.'''

new_gov = '''- **सर्वोच्च प्रशासकीय नेतृत्व व सप्त-पीठे (The Manu-Upādhi & The 7 Sovereign Seats) [CANON LOCK]:**
  - **The Supreme Executive: THE MANU-UPĀDHI (मनू-उपाधी — The Grey Basalt Throne):** Central City आणि ५ नश्वर Astral Shards चा सर्वोच्च वैधानिक व प्रशासकीय प्रमुख.
  - **The Seven Sovereign Seats (सप्त-सार्वभौम पीठे):**
    1. *Seat of Coin & Credit:* **Beatrice Rosso** (High Arbitrator of the Central Reserve Bank / मध्यवर्ती आकाश-कोश महा-बँक).
    2. *Seat of the Sun (Deva):* Solar Primus.
    3. *Seat of the Anvil (Asura):* High Artificer of Asura-Nagara.
    4. *Seat of the Blade (Human):* Chief Justice of Hastinapura.
    5. *Seat of the Fang (Beast):* Grand Chieftain of the Beast Shard.
    6. *Seat of the Vanguard:* Grand Marshal of the Proving Games.
    7. *The Shadow Seat:* Arbiter of Outworlder / Jīvātma Diaspora.
  - **Constitutional Subordination:** Tier 2 Buffer Zone मधील **The High Council (Indra-Upādhi)** हे Tier 3 मधील **Manu-Upādhi आणि 7 Sovereign Seats** च्या घटनात्मकदृष्ट्या वरिष्ठ (Superior Authority) आहे.'''

assert old_gov in text, 'old_gov not found'
text = text.replace(old_gov, new_gov, 1)

# 2. Update Section 2.2 diagram and text
old_diagram = '''```
                      [ HIGH CHANCELLOR SULABHA AL-MANSUR ]
                      Supreme Diplomatic Moderator (Grand Concord)
                                        │
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
[ AKASH KOSHA CENTRAL BANK ]    [ THE GRAND EXCHANGE ]         [ CENTRAL MANTRA-STONE GRID ]
High Gov. Ambika       Resource & Ammunition Quotas   Master Uttanka
- Issues Central Aether-Rupee   - Manages Mineral Embargoes    - Monopolies all Inter-Realm
- Freezes Foreign Gold Bullion  - Sets Slag-Ore & Grain Tariffs   Acoustic Communications
```'''

new_diagram = '''```
                      [ THE MANU-UPĀDHI · GREY BASALT THRONE ]
                      (Supreme Administrator of Central City & 5 Astral Shards)
                                        │
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
[ CENTRAL RESERVE BANK ]        [ THE GRAND EXCHANGE ]         [ CENTRAL MANTRA-STONE GRID ]
Beatrice Rosso (High Arbitrator) Resource & Ammunition Quotas   Master Uttanka
- Issues Central Aether-Rupee   - Manages Mineral Embargoes    - Monopolizes Inter-Realm
- Freezes Foreign Gold Bullion  - Sets Slag-Ore & Grain Tariffs   Acoustic Communications
```'''

assert old_diagram in text, 'old_diagram not found'
text = text.replace(old_diagram, new_diagram, 1)

# 3. Replace Ambika with Beatrice Rosso
text = text.replace('गव्हर्नर **Ambika** च्या नियंत्रणाखाली', '**Beatrice Rosso** (High Arbitrator) च्या नियंत्रणाखाली')
text = text.replace('अंबिका त्याचे परदेशी तिजोरीतील सोने गोठवते', 'Beatrice Rosso त्याचे परदेशी तिजोरीतील सोने गोठवते')

# 4. Fix "बुलेटप्रूफ"
old_bullet = 'बुलेटप्रूफ Aether-Silk कापड'
new_bullet = 'वज्र-अभंग अस्त्र-रोधक Aether-Silk कापड'
assert old_bullet in text, 'old_bullet not found'
text = text.replace(old_bullet, new_bullet)

# 5. Fix "विमान" and "बलून"
text = text.replace('हस्तिनापूरचे एकही विमान', 'हस्तिनापूरचा एकही गगन-रथ')
text = text.replace('विमानांच्या स्फटिक-गाभ्यांसाठी', 'आकाशीय रथांच्या स्फटिक-गाभ्यांसाठी')
text = text.replace('कोणतीही एथर-टेहळणी नौका किंवा बलून', 'कोणतीही एथर-टेहळणी गगन-नौका किंवा तरंग-फ्लोट')

# 6. S-Rank hard cap in Section 2.3
target_s_rank = 'रँकिंगसाठी नोंदणी करतात (S-Rank, A-Rank, B-Rank, C-Rank).'
replacement_s_rank = 'रँकिंगसाठी नोंदणी करतात (S-Rank, A-Rank, B-Rank, C-Rank) — जिथे Tier 3 Astral Shards च्या भौगोलिक नाजूकतेमुळे S-Rank ची मर्यादा strictly दुर्ग-भंजक / नगर-वेधक (Fortress-Breaker scale) मर्यादेपर्यंतच मर्यादित असते.'
assert target_s_rank in text, 'target_s_rank not found'
text = text.replace(target_s_rank, replacement_s_rank, 1)

# Verify no 'नहीं' with bindi
assert 'नहीं' not in text, "Found banned 'नहीं' with bindi!"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('SUCCESS: UNIVERSE B/New/06_The_Astral_Realm.md patched cleanly!')
