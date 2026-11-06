import sys
from pathlib import Path

ROOT = Path(r"d:\Web Novel\Brahmand")

# 1. Clean 01_Cosmology_and_The_Trinity_Mandate.md
f1 = ROOT / "01_WORLD_BIBLE" / "01_Cosmology_and_The_Trinity_Mandate.md"
t1 = f1.read_text(encoding="utf-8").replace("\r\n", "\n")

target1 = """3. **Why a mortal Loses Everything:**
   - When 19-year-old a mortal from Mumbai is sucked into the trans-dimensional glitch, he passes through the outermost fringe of the Singularity Apex.
   - His dead smartphone turns into brittle black dust.
   - Any high-tech prototypes, artificial AI chips, power banks, or synthetic crutches are **100% vaporized to zero**.
   - a mortal arrives in Central City with only his biological human body, his worn clothes, ₹11 in useless copper-nickel coins, his engineering intellect, and his raw mortal grit!"""

repl1 = """3. **The Total Dissolution of Foreign Artifacts:**
   - When souls or objects cross the outer perimeter under the Vidhātā Treaty, the extreme spiritual radiance of the Kṣīra Sāgara dissolves all foreign synthetic materials, unnatural constructs, and artificial machinery into fine carbon ash.
   - Only the living soul (*Jīvātman*) and a biological mortal body survive the transit.
   - Transferred souls arrive in Central City stripped of all foreign crutches, possessing only their raw mortal biology, innate will (*Puruṣārtha*), and an unwritten Soul ID."""

assert target1 in t1, "target1 missing in f1"
t1 = t1.replace(target1, repl1)
f1.write_text(t1, encoding="utf-8")
print("SUCCESS: Cleaned f1")

# 2. Clean 05_Cosmic_Eras_and_The_Seven_Nightmares.md
f2 = ROOT / "01_WORLD_BIBLE" / "05_Cosmic_Eras_and_The_Seven_Nightmares.md"
t2 = f2.read_text(encoding="utf-8").replace("\r\n", "\n")

target2 = """### 5.2 The Dadar Station Anomaly: the wielder's Arrival
On an ordinary monsoon night in modern Mumbai:
- 19-year-old **a mortal**, standing under the Dadar station flyover with a dead smartphone and ₹11 change, is caught in an anomalous spatial shear caused by a runaway Shadow Anchor dial in Central City.
- The glitch pulls him across the Singularity Apex of the Kṣīra Sāgara, vaporizing all his technology, and dumps his battered mortal body into a hay-and-dung cart in the outer caravan terminal of Central City.

The wheel has turned. A mortal catalyst with zero gamer cheats has arrived in the ancient cosmos."""

repl2 = """### 5.2 The Dimensional Friction & The Vidhātā Treaty Arrivals
As the Rotary Shadow Anchors destabilize from illegal mining and black-market tampering, the cosmic fabric begins to fray:
- In response to mounting entropy, the **Vidhātā Inter-Brahmāṇḍa Treaty (विधाता-संविद)** permits the incarnation of external catalyst souls bearing unwritten destinies (`[STATUS: RIKTA / UNWRITTEN]`).
- Transferred across the Kṣīra Sāgara boundary, their foreign attachments dissolved, these souls awaken in the outer transit and caravan wards of Central City (such as Aniket, CHR-ALN-06).
- Bound by ancient **Rinānubandha (ऋणानुबंध)**, companion beasts and long-severed karmic threads converge in the lower city, initiating the events of Volume 1.

The wheel has turned. Unranked mortal catalysts with unwritten destinies now walk the ancient cosmos."""

assert target2 in t2, "target2 missing in f2"
t2 = t2.replace(target2, repl2)
f2.write_text(t2, encoding="utf-8")
print("SUCCESS: Cleaned f2")

# 3. Clean 05_Tier_Naming_and_Language_Hierarchy.md
f3 = ROOT / "02_POWER_SYSTEM" / "05_Tier_Naming_and_Language_Hierarchy.md"
t3 = f3.read_text(encoding="utf-8").replace("\r\n", "\n")

target3_a = """### 3.4 Layer 4: Apabhraṁśa & Street Register (अपभ्रंश व मुंबई लोक-बोली)
- **Who Speaks It:** Outer slum carters, dung-cart loaders, and unranked arena feeders.
- **Linguistic Nature:** Raw, earthy, cynical, punchy, conversational, and direct. It strips away all aristocratic pretensions.
- **the wielder's Voice:** a mortal speaks a sharp, street-smart Mumbai Hinglish/Marathi register, blending practical modern observation with gritty survivor pragmatism.
- **Sample Dialogue Tone:**
  > *"दोन तांब्याच्या नाण्यासाठी इतका माज? दादरच्या भाजी मार्केटमध्ये यापेक्षा जास्त दम असतो लोकांत. चल, हात पुढे कर आणि ते कडक भाकरीचा तुकडा दे."*  
  > *(So much arrogance for two copper coins? People in Dadar vegetable market have more spine than this. Come on, hold out your hand and hand over that stale piece of bhakri.)*"""

repl3_a = """### 3.4 Layer 4: Apabhraṁśa & Lower Wards Register (अपभ्रंश व श्रमिक लोक-बोली)
- **Who Speaks It:** Outer slum carters, dung-cart loaders, wandering day-laborers, and unranked arena feeders.
- **Linguistic Nature:** Raw, earthy, cynical, punchy, conversational, and direct. It strips away all aristocratic pretensions.
- **Aniket's Voice:** Aniket speaks a sharp, resilient Prakrit/Apabhraṁśa survivor register, blending keen physical observation with unyielding mortal pragmatism.
- **Sample Dialogue Tone:**
  > *"दोन तांब्याच्या नाण्यासाठी इतका माज? वेशीवरच्या मजुरांमध्ये यापेक्षा जास्त दम असतो. चल, हात पुढे कर आणि तो कोरडा भाकरीचा तुकडा दे."*  
  > *(So much arrogance for two copper coins? Day-laborers at the outer gate have more spine than this. Come on, hold out your hand and hand over that dry piece of flatbread.)*"""

assert target3_a in t3, "target3_a missing in f3"
t3 = t3.replace(target3_a, repl3_a)

target3_b = """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        the wielder'S THREE LINGUISTIC BRIDGES                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Prakrit / Apabhraṁśa Cognates (लोकबोली साम्य):                                       │
│    Central City's trade vernacular (Layer 3 & 4) is the direct ancestor of modern     │
│    Marathi and Hindi. Words like 'Pānī', 'Rakt', 'Bhākrī', 'Māṣa', 'Mala', and 'Chalo' │
│    are immediately intuitive to the wielder's Mumbai street ear!                              │
│                                                                                        │
│ 2. The Acoustic Sing (गूंज ध्वनीशास्त्र):                                               │
│    When high-born champions chant Layer 2 Sanskrit Astras, A listener doesn't translate      │
│    the poetry. He reads the physical acoustics: the 0.2s Gūñja tells him the vector,   │
│    velocity, and elemental heat of the incoming strike!                                │"""

repl3_b = """┌────────────────────────────────────────────────────────────────────────────────────────┐
│                    THE TRANSFERRED SOUL'S THREE LINGUISTIC BRIDGES                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Prakrit / Apabhraṁśa Cognates (लोकबोली साम्य):                                       │
│    Central City's trade vernacular (Layer 3 & 4) shares deep structural roots with    │
│    ancient Prakrit dialects. Words like 'Pānī', 'Rakta', 'Bhākrī', 'Māṣa', and 'Mala' │
│    are immediately decipherable to an observant mortal ear!                            │
│                                                                                        │
│ 2. The Acoustic Sing (गूंज ध्वनीशास्त्र):                                               │
│    When high-born champions chant Layer 2 Sanskrit Astras, an unranked fighter does    │
│    नही need to translate the poetry. He reads the physical acoustics: the 0.2s Gūñja   │
│    tells him the vector, velocity, and elemental heat of the incoming strike!          │"""

assert target3_b in t3, "target3_b missing in f3"
t3 = t3.replace(target3_b, repl3_b)

f3.write_text(t3, encoding="utf-8")
print("SUCCESS: Cleaned f3")
