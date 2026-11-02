import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r'd:\Web Novel\UNIVERSE B\New\05_The_Setu.md'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Title & Tags
old_header = '''# 05. Tier 2: The Buffer Zone, Geography, Sectors & Operations
**File:** `D:\\Web Novel\\New\\05_The_Setu.md`  
**Tags:** `#buffer-zone #tier-2 #the-great-setu #antariksha #four-sectors #setu-academy #setu-mahasena #13-officers #operational-regulations #canon-lock`'''

new_header = '''# 05. Tier 2: Swarga / Setu-Loka (The Great Buffer Zone), Geography, Sectors & Operations
**File:** `D:\\Web Novel\\New\\05_The_Setu.md`  
**Tags:** `#buffer-zone #tier-2 #swarga #indra-upadhi #the-great-setu #antariksha #four-sectors #setu-academy #setu-mahasena #high-council #warrior-equality #canon-lock`'''

assert old_header in text, 'old_header not found'
text = text.replace(old_header, new_header, 1)

# 2. Update Section 1 lead text & diagram
old_sec1 = '''Tier 2 (The Buffer Zone / शास्त्रीय *Antariksha*) हा 100% अहिंसक Tier 1 (Divine High Council Realm) आणि खालील Tier 4 (Corrupted Realm) / Tier 3 (Astral Realm) यांच्यामध्ये अधांतरी बांधलेला **एक अजस्त्र, इंजिनिअर्ड सेतू आणि अवकाशीय महामार्ग** आहे. The Setu ची दक्षिण सीमा थेट The Grand Aegis आणि Tier 4 च्या अधो-लोकाशी जोडलेली आहे:

```
                  [ TIER 1: DIVINE HIGH COUNCIL & DIVINE REALM ]
                                        ▲
                                        │ (Deva Gate / High Ascent)
════════════════════════════════════════╪════════════════════════════════════════
                  [ TIER 2: THE BUFFER ZONE / THE GREAT SETU ]
  ┌───────────────────────┬──────────────────────────┬────────────────────────┐
  │  WEST: IRON FRONTIER  │    CENTRAL: GRAND HUB    │ EAST: PRATIGRAHA GROUND │
  │  - The Iron Rampart   │    - Central Hub Ring    │   - Pratigraha Godown   │
  │  - Vajra Fortress(HQ) │    - Setu Academy        │   - Conduit Dock        │
  │  - Barrier Outposts   │    - Engineering Labs    │   - Lekhya Bureau       │
  │  - 5,000-Mile Trenches│    - Court of Inquiry    │   - Surface Rail Gate   │
  └───────────┬───────────┴─────────────┬────────────┴───────────┬────────────┘
              │                         │                        │
  (Facing Corrupted Realm)      (Main Rail Terminal)     (Route A/B Arrival)
════════════════════════════════════════╪════════════════════════════════════════
                                        ▼
    [ QUARANTINE THRESHOLD: 360° SPIRITUAL BARRIER (THE GRAND AEGIS) ]
                                        ▼
    [ TIER 4: THE CORRUPTED REALM (अधो-लोक / Devils & 7 Void Seals) ]
        (Between Buffer Zone & Astral Realm • Pishacha Cannister Drops)
                                        ▼
          [ ADJACENT DIMENSIONAL INTERFACE & KAY-TYAG FILTER ]
                                        ▼
    [ TIER 3: THE ASTRAL LIVING REALM (५ स्वतंत्र उप-लोक / 70% Living Wheel) ]
```'''

new_sec1 = '''Tier 2 (The Buffer Zone / शास्त्रीय *Swarga / Setu-Loka*) हा Tier 1 (Parama-Dhama — Transcendent Divine Realm) आणि खालील Tier 4 (Corrupted Realm / Patala) व Tier 3 (Astral Realm) यांच्यामध्ये अधांतरी उभारलेला **एक अजस्त्र, इंजिनिअर्ड वैश्विक सेतू, सैन्य छावणी व महा-प्रशासकीय बफर झोन** आहे. 

> [!IMPORTANT]
> **The Sovereign of Swarga: Indra-Upādhi (इंद्र-उपाधी):**  
> Tier 2 Swarga हे कोणत्याही एका वंशाचे (केवळ देवांचे) खाजगी राज्य नसून, **सर्व योद्ध्यांसाठी समान हक्क असलेला आंतरराष्ट्रीय बफर झोन (The Buffer Zone of Warrior Equality)** आहे. येथे Devas, Asuras, Humans, Beasts आणि Outworlders सर्वांना त्यांच्या शौर्यानुसार समान प्रतिष्ठा मिळते. या संपूर्ण क्षेत्राचे आणि **The High Council** चे सर्वोच्च प्रशासकीय प्रमुख **Indra-Upādhi** (सुवर्ण वज्र-सिंहासन) असतात.

The Setu ची बाह्य सीमा थेट The 360° Spherical Grand Aegis आणि Tier 4 च्या अधो-लोकाशी जोडलेली आहे:

```
                  [ TIER 1: PARAMA-DHAMA / SUPREME DIVINE ASSEMBLY ]
                  (Brahma · Vishnu · Shiva + Divine Delegates Prajapati/Narada/Rudra)
                                        ▲
                                        │ (Deva Gate / High Ascent)
════════════════════════════════════════╪════════════════════════════════════════
        [ TIER 2: SVARGA / THE GREAT SETU (THE BUFFER ZONE) ]
        (Presided over by INDRA-UPĀDHI • The High Council • Warrior Equality)
  ┌───────────────────────┬──────────────────────────┬────────────────────────┐
  │  WEST: IRON FRONTIER  │    CENTRAL: GRAND HUB    │ EAST: PRATIGRAHA GROUND │
  │  - The Iron Rampart   │    - Indra-Upadhi Throne │   - Pratigraha Godown   │
  │  - Vajra Fortress(HQ) │    - High Council Chamber│   - Soul Trinity Offices│
  │  - Barrier Outposts   │    - Setu-Mahasena HQ    │   - Conduit Dock        │
  │  - Quarantine Trenches│    - Setu Academy        │   - Armored Ratha-Gate  │
  └───────────┬───────────┴─────────────┬────────────┴───────────┬────────────┘
              │                         │                        │
  (Facing 360° Grand Aegis)     (Central Ratha Plaza)    (Route A/B Arrival)
════════════════════════════════════════╪════════════════════════════════════════
                                        ▼
     [ QUARANTINE THRESHOLD: 360° SPHERICAL BARRIER (THE GRAND AEGIS) ]
                                        ▼
      [ TIER 4: PATALA / THE CORRUPTED REALM (अधो-लोक / Pretas & 7 Seals) ]
                                        ▼
          [ ADJACENT DIMENSIONAL INTERFACE & KAY-TYAG FILTER ]
                                        ▼
    [ TIER 3: THE ASTRAL REALM (५ स्वतंत्र Shards • Governed by MANU-UPĀDHI) ]
```'''

assert old_sec1 in text, 'old_sec1 not found'
text = text.replace(old_sec1, new_sec1, 1)

# 3. Purge Victorian Railway & Train words
text = text.replace('Surface Rail Gate', 'Armored Ratha-Gate')
text = text.replace('Main Rail Terminal', 'Central Ratha Plaza')
text = text.replace('Pratigraha Surface Rail Gate', 'Pratigraha Armored Ratha-Gate')
text = text.replace('Buffer Zone चा aether-pneumatic viaduct rail spur', 'Buffer Zone चा aether-pneumatic viaduct ratha conduit')
text = text.replace('Buffer Zone rail', 'Buffer Zone aether-conduit')
text = text.replace('विमान चालक', 'गगन-सारथी (Sky-Beast Charioteer)')
text = text.replace('विमान-वाहतुकीचे बिल', 'आकाशीय वाहतूक महसूल (Aerial Transit Toll)')
text = text.replace('कर्तव्यात निष्काळजीपणा, ट्रेनला उशीर.', 'कर्तव्यात निष्काळजीपणा, रक्षक-दूत किंवा आकाशीय रथास अकारण उशीर.')

# 4. Spherical Grand Aegis (replace linear miles & flat wall phrasing)
text = text.replace('५,००० मैल खंदक-जाळे', '३६०° गोलाकार क्वारंटाईन खंदक-जाळे')
text = text.replace('५,००० मैल लांब खंदक-पट्टा', '३६०° गोलाकार खंदक-पट्टा')
text = text.replace('५,००० मैल लांब खंदक', 'गोलाकार क्वारंटाईन खंदक')
text = text.replace('खंदकाच्या बरोबर पुढे उभा असलेला ३६०-डिग्री अदृश्य सुवर्ण-पडदा / भिंत', 'संपूर्ण क्षेत्राला चहूबाजूंनी वेढणारे ३६०° Spherical Cosmic Barrier (The Grand Aegis) चे अजस्त्र ऊर्जा-कवच')

# 5. Fix Tier 1 vs Tier 2 High Council placement in Setu
text = text.replace('Tier 1 (Divine High Council Realm)', 'Tier 1 (Parama-Dhama — Supreme Divine Assembly)')
text = text.replace('ढगांमधून थेट वर High Council कडे चढणारी महाकाय हायड्रॉलिक-प्राण लिफ्ट', 'ढगांमधून थेट वर Tier 1 Parama-Dhama कडे चढणारी महाकाय हायड्रॉलिक-प्राण लिफ्ट')

# Verify no 'नहीं' with bindi
assert 'नहीं' not in text, "Found banned 'नहीं' with bindi!"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('SUCCESS: UNIVERSE B/New/05_The_Setu.md patched cleanly!')
