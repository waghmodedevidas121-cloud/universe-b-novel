import sys
from pathlib import Path

fpath = Path(r"d:\Web Novel\Brahmand\01_WORLD_BIBLE\00_Sanatan_Encyclopedic_Codex.md")
text = fpath.read_text(encoding="utf-8").replace("\r\n", "\n")

target = """# SECTION V: PROTAGONIST PHENOMENOLOGY (नायक-तत्त्व)

---

### 31. Mārtya-Śarīra (मर्त्य-शरीर — The Mortal Biological Vessel)
- **Etymology & Root:** *Mṛtyu* (मृ — subject to mortality, perishable earth-clay) + *Śarīra* (शॄ — that which decays, biological vessel).
- **Scriptural Authority:** *Śatapatha Brāhmaṇa*; *Caraka Saṁhitā* Śārīrasthāna.
- **Classical Definition:** The physical biological body composed of the five gross elements (*Pāñcabhautika-Śarīra*), subject to hunger, thirst, physical fatigue, and eventual death.
- **Novel Context & Adaptation:** The physical biological vessel of an unascended human. Mortal flesh possesses **zero divine radiance**, zero celestial bloodlines, and zero unnatural enhancements.
- **Tactical Mechanics:** A mortal warrior feels the brutal physical reality of combat: bruised ribs, blistered palms, torn ligaments, and caloric depletion. However, having zero divine radiance makes them virtually invisible to high-tier astral detection arrays.
- **Trope Rejection:** A mortal warrior is **नही** an invincible entity who shrugs off heavy impacts. They survive through physics, positioning, and pain tolerance.

---

### 32. KĀLĪ (काली — The Spiked Iron Shackle)
- **Etymology & Root:** *Kāla* (कल् — black, time, entropic decay, that which devours all matter).
- **Scriptural Authority:** *Mahābhārata* Sauptika Parva (The dark night of Kalaratri); *Atharvaveda*.
- **Canonical Status:** A **Shaapit Shastra (शापित लौह-श्रृंखला)** forged during Era 2 in the depths of Śūnya-Garta.
- **Tactical Mechanics & Bandolier Carry:**
  - *Mass & Resting Carry:* 18 kilograms (40 lbs) of rusted meteoric black iron. Outside combat, the wielder loops it diagonally across chest and waist as an **ascetic iron bandolier**, distributing the deadweight across the pelvic core and spine via Apāna grounding to prevent elbow dislocation.
  - *Physical Length (8 Feet):* 33 interlocking triangular barbed links (~2.8 inches per link), allowing tight coiling into the *Vajra-Kavaca* forearm shield.
  - *Spectral Reach (45 Feet):* In *Pāśa-Bandhana*, the terminal triangular fang unspools a trailing 37-foot tether of condensed Preta-frost shadow-links, reaching 45 feet (13.7 m) total.
  - *Kinetic Execution:* The wielder uses Apāna grounding to hook enemy ankles or lock weapon shafts, using leverage against heavier opponents.
  - *The Parasitic Toll:* Leaches biological calories and spreads sub-zero marrow frost up the wielder's arm during prolonged activation.
- **Trope Rejection:** KALI is **नही** an obedient magic pet weapon. It is a vicious, cold executioner's shackle that must be ruthlessly dominated through will.

---

### 33. Kuro / Śerū (कुरो / शेरू — The Loyal Shadow Hound)
- **Etymology & Root:** *Sheru* (शूर / शेर — bold, lion-hearted steadfast companion); *Kṛṣṇa-Śārameya* (कृष्ण-शारमेय — sacred black hound of celestial/karmic lineage).
- **Scriptural Authority:** *Mahābhārata* Mahāprasthānika Parva (The faithful dog that accompanied Yudhishthira to the gates of Swarga).
- **Canonical Status:** The archetypal loyal shadow-hound companion. Saturated with subtle Preta-currents during abyssal crossings, the hound evolves into an ash-black, shadow-sheathed guardian.
- **Tactical Mechanics:** Serves as the wielder's **living thermal buffer**. Sheru inhales the excess necrotic frost leaking from KĀLĪ, preventing frostbite from advancing past the wielder's elbow, while strengthening his own shadow coat.
- **Preta Saturation Ceiling (प्रेत-संतृप्ती मर्यादा):** Sheru has a strict absorption ceiling. If he consumes too much necrotic frost in a single battle, his internal organs freeze, he vomits black ice, and his mind regresses into feral rabid frenzy. The warrior must keep fights brief to safeguard the hound.
- **Trope Rejection:** Sheru is **नही** a cute fantasy mascot. He is a scarred, one-eared street survivor who bites dirty and guards their companion's back with ferocious loyalty."""

repl = """# SECTION V: ŚARĪRA-TRAYA, PAÑCA-KOŚA & PURUṢĀRTHA (शरीर-त्रय, पञ्चकोश व पुरुषार्थ तत्त्व)

---

### 31. Śarīra-Traya (शरीर-त्रय — The Three Bodies of the Soul)
- **Etymology & Root:** *Śarīra* (शॄ — that which decays, biological/subtle vehicle) + *Traya* (त्रि — three fold).
- **Scriptural Authority & Sanskrit Proof-Text:**
  > **पञ्चीकृतमहाभूतसम्भवं कर्मसञ्चितम् । शरीरं सुखदुःखानां भोगायतनमुच्यते ॥**  
  > *(Śaṅkarācārya's Vivekacūḍāmaṇi 88; Vedāntasāra 45–55; Taittirīya Upaniṣad 2.1–5)*  
  > **शास्त्रीय अर्थ:** पंचीकृत महाभूतांपासून उत्पन्न झालेले, कर्माने साठवलेले स्थूल शरीर हे सुख-दुःखांचे भोगायतन (अनुभवाचे स्थान) आहे.
- **Classical Definition:** In classical Vedānta, every embodied Jīva possesses three nested bodies:
  1. **Sthūla-Śarīra (स्थूल शरीर — Gross Physical Body):** Composed of the five elements, subject to hunger, fatigue, physical impact, and death.
  2. **Sūkṣma-Śarīra (सूक्ष्म शरीर — Subtle Body):** Composed of 17 constituents (5 Prāṇas, 5 sensory faculties, 5 motor faculties, Manas, and Buddhi), surviving physical death to transmigrate.
  3. **Kāraṇa-Śarīra (कारण शरीर — Causal Body):** The seed-body containing latent karmic impressions (*Saṁskāras*), where the Agra-Sandhānī Soul ID frequency is inscribed.
- **Novel Context & Adaptation:** In *Brahmand*, mortals possess **zero divine radiance** in their gross body, meaning celestial tracking arrays cannot detect them easily. Their combat is grounded in raw anatomy, muscle leverage, and bone endurance.
- **Tactical Mechanics:** Bruises, torn tendons, bone fractures, and caloric exhaustion are tangible combat constraints that cannot be bypassed with magic potions.
- **Trope Rejection:** Mortal bodies are **नही** digital avatars with HP pools. Damage is biological and structural.

---

### 32. Pañca-Kośa (पञ्चकोश — The Five Envelopes of Consciousness)
- **Etymology & Root:** *Pañca* (पञ्च — five) + *Kośa* (कोश — sheath, layer, casing enveloping the Atman).
- **Scriptural Authority & Sanskrit Proof-Text:**
  > **कोशोऽन्नमयः प्राणमयश्च मनोमयस्तथा । विज्ञानमय आनन्दमयश्चेति पञ्च ते ॥**  
  > *(Taittirīya Upaniṣad Brahmānandavallī 2.1–5; Pañcadaśī 1.33–42)*  
  > **शास्त्रीय अर्थ:** आत्म्याभोवती पाच आच्छादने असतात: अन्नमय, प्राणमय, मनोमय, विज्ञानमय आणि आनंदमय.
- **Classical Definition:** The five hierarchical levels of mortal experience through which consciousness expresses itself:
  1. *Annamaya-Kośa:* The gross anatomical sheath fed by food.
  2. *Prāṇamaya-Kośa:* The vital respiratory sheath governing the five Prāṇas and kinetic vectors.
  3. *Manomaya-Kośa:* The sensory and emotional processing sheath.
  4. *Vijñānamaya-Kośa:* The sheath of discriminating intellect (*Buddhi*) and tactical calculation.
  5. *Ānandamaya-Kośa:* The causal sheath of latent impressions (*Vāsanās*) closest to the pure Ātman.
- **Novel Context & Adaptation:** Combat in *Brahmand* requires synchronized alignment across kośas. Channeling an *Apāna* grounding vector operates through the *Prāṇamaya-kośa*; tracking the 0.2s *Gūñja* acoustic hum requires the sensory stillness of the *Manomaya-kośa*; analyzing Dhanurveda geometry requires the *Vijñānamaya-kośa*.
- **Tactical Mechanics:** Disrupting an enemy's *Prāṇamaya-kośa* through marma strikes paralyzes physical motion without cutting the flesh.
- **Trope Rejection:** Pañca-Kośa is **नही** an anime "chakra" or "mana pool." It is the authentic Vedic ontology of biological and mental functionality.

---

### 33. Puruṣārtha-Catuṣṭaya (पुरुषार्थ-चतुष्टय — The Four Sovereign Aims of Life)
- **Etymology & Root:** *Puruṣa* (conscious being) + *Artha* (aim, purpose, striving) + *Catuṣṭaya* (fourfold).
- **Scriptural Authority & Sanskrit Proof-Text:**
  > **धर्मार्थकामाः सममेव सेव्या यो ह्येकसेवी स जनो जघन्यः ।**  
  > **धर्मार्थकामेषु यतस्य लोके मोक्षो भवेत्संयतमानसानाम् ॥**  
  > *(Mahābhārata Śānti Parva 123.5; Manusmṛti 2.224; Kauṭilīya Arthaśāstra 1.7)*  
  > **शास्त्रीय अर्थ:** धर्म, अर्थ आणि काम या तिन्हीचे समतोल सेवन केले पाहिजे. जो एकाचेच सेवन करतो तो अधोगतीला जातो. या तिन्हीत संयमाने वागणाऱ्यालाच मोक्ष प्राप्त होतो.
- **Classical Definition:** The comprehensive matrix of legitimate human striving:
  1. **Dharma (धर्म):** Cosmic order, ethical duty, and martial covenants.
  2. **Artha (अर्थ):** Material wealth, civic commerce, weapons, and sovereign security.
  3. **Kāma (काम):** Life desires, emotional fulfillment, and creative joy.
  4. **Mokṣa (मोक्ष):** Ultimate spiritual liberation and transcendence of karmic cycles.
- **Novel Context & Adaptation:** Central City is an economic machine driven by *Artha* (trade, tariffs, arena wages), but when stripped of *Dharma*, it descends into corrupt gladiator exploitation. Contenders fight for *Artha* (silver Panas for food) while facing agonizing moral dilemmas (*Dharma-Saṅkaṭa*).
- **Tactical Mechanics:** Characters who pursue pure *Artha* without *Dharma* (like the bookmaker Kaṁsa) inevitably trigger civic blowback and ruin under the law of *Karma-Phala*.
- **Trope Rejection:** Puruṣārtha is **नही** a video game quest objective. It is the fourfold tension that drives all authentic human civilizations and epic conflicts."""

assert target in text, "Target Section V not found in Codex!"
text = text.replace(target, repl)
fpath.write_text(text, encoding="utf-8")
print("SUCCESS: Section V in 00_Sanatan_Encyclopedic_Codex.md fully cleansed of protagonist baggage!")
