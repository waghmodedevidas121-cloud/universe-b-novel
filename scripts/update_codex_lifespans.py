file_path = r"d:\Web Novel\Brahmand\01_WORLD_BIBLE\00_Sanatan_Encyclopedic_Codex.md"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

target = """### 25. Śāpita Śastra (शापित शस्त्र — Cursed Weaponry)
- **Etymology & Root:** *Śāpita* (cursed, bound by tragic decree) + *Śastra* (handheld weapon).
- **Scriptural Authority:** *Atharvaveda* (hymns on battle-binding and weapon cleansing); *Agni Purāṇa*.
- **Classical Definition:** A weapon forged in sacrilege, tempered in the blood of catastrophic betrayals, or saturated with unpurified Preta-Tattva.
- **Novel Context & Adaptation:** Contrast with consecrated Astras. Governs weapons like **KĀLĪ** (the archetypal spiked black-iron shackle).
- **Tactical Mechanics:** A cursed weapon demands a continuous physical toll: for every crushing blow it inflicts, it extracts biological calories and biological warmth from the wielder, whispering maddening cries into their mind.
- **Trope Rejection:** A cursed weapon is **नही** an edgy cosmetic item with a stat bonus. It is a dangerous, parasitic liability that will kill an undisciplined wielder.

---

# SECTION IV: ARTHASHASTRA & GOVERNANCE"""

replacement = """### 25. Śāpita Śastra (शापित शस्त्र — Cursed Weaponry)
- **Etymology & Root:** *Śāpita* (cursed, bound by tragic decree) + *Śastra* (handheld weapon).
- **Scriptural Authority:** *Atharvaveda* (hymns on battle-binding and weapon cleansing); *Agni Purāṇa*.
- **Classical Definition:** A weapon forged in sacrilege, tempered in the blood of catastrophic betrayals, or saturated with unpurified Preta-Tattva.
- **Novel Context & Adaptation:** Contrast with consecrated Astras. Governs weapons like **KĀLĪ** (the archetypal spiked black-iron shackle).
- **Tactical Mechanics:** A cursed weapon demands a continuous physical toll: for every crushing blow it inflicts, it extracts biological calories and biological warmth from the wielder, whispering maddening cries into their mind.
- **Trope Rejection:** A cursed weapon is **नही** an edgy cosmetic item with a stat bonus. It is a dangerous, parasitic liability that will kill an undisciplined wielder.

---

### 26. Catur-Varṇa Jīva-Kāla (चतुर्वर्ण जीव-काल — Comparative Cosmic Lifespans & Elemental Birthrights)
- **Etymology & Root:** *Catur* (four) + *Varṇa* (order/class of living beings) + *Jīva* (living soul) + *Kāla* (lifespan/duration of biological incarnation).
- **Scriptural Authority:** *Manusmṛti* 1.83–84 (*"Arogāḥ sarvasiddhārthāścaturvarṣaśatāyuṣaḥ..."*); *Viṣṇu Purāṇa* 2.3; *Śrīmad Bhāgavata Purāṇa*.
- **Classical Definition:** The baseline biological lifespan and metaphysical potential ordained for distinct biological orders within a specific cosmic epoch (*Yuga*).
- **Novel Context & Adaptation (सामान्य नागरिक सरासरी आयु व जन्मजात तत्त्व-अधिकार):**
  1. *Humans (मानव):* 150 – 200 years (healthy mortal baseline living under clean aetheric currents). 94–95% are born with dormant/slept traits, requiring formal awakening or severe physical crisis to ignite active power.
  2. *Asuras (असुर):* 600 – 700 years (prolonged longevity driven by dense basalt-iron cellular structure and high thermal tolerance).
  3. *Suras (सुर / देव):* ~1,000 years. Their extended biological life-cycle dictates a notably slow reproduction rate; children are rare and deeply treasured. Because of their Jīvātman's high karmic elevation, **100% of Sura children are born with already ACTIVATED elemental affinities** from the 10 primal elements (Zero Slept birthrate).
  4. *Rishis / Sages (तपस्वी ऋषी):* Thousands of years to multiple Yugas. Their lifespan is **नही** tied to ordinary racial biology; it is sustained by intense Tapasyā, Prāṇāyāma, and non-draining meditative absorption.
- **Tactical Mechanics:** Sura adepts start their martial careers with innate kinetic advantages due to their active birthright, while humans compensate through tactical versatility, Tapasya-breakthroughs (*Kṛti*), and sheer biological adaptability.
- **Trope Rejection:** Lifespans are **नही** "immortal health bars" or video-game level caps. They reflect biological cellular regeneration rates and prāṇic density.

---

# SECTION IV: ARTHASHASTRA & GOVERNANCE"""

if target in text:
    text = text.replace(target, replacement)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Inserted Entry 26 into 00_Sanatan_Encyclopedic_Codex.md successfully")
else:
    print("Target not found in 00_Sanatan_Encyclopedic_Codex.md")
