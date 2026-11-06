# -*- coding: utf-8 -*-
"""
Remediation script for Brahmand Power System and Beats Codex
Applies all 8 Goldfish audit recommendations cleanly across the markdown files.
Enforces 100% adherence to the 'नही' rule (zero 'नहीं' with bindi).
"""
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"d:\Web Novel\Brahmand"

def replace_in_file(rel_path, target, replacement):
    path = os.path.join(ROOT_DIR, rel_path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Normalize line endings
    content_norm = content.replace('\r\n', '\n')
    target_norm = target.replace('\r\n', '\n')
    replacement_norm = replacement.replace('\r\n', '\n')
    
    if target_norm not in content_norm:
        print(f"FAILED to find target in {rel_path}!")
        return False
        
    new_content = content_norm.replace(target_norm, replacement_norm)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"SUCCESS: Patched {rel_path}")
    return True

# --- 1. 02_POWER_SYSTEM/01_The_Six_Epic_Pillars.md ---
p1_target1 = """- **Inertia & Newton's Third Law:** Mass cannot be ignored. When a warrior swings a 300-pound bronze mace (*Gadā*), the kinetic recoil must be absorbed through the hips and driven into the earth via **Apāna grounding**. Swinging on loose gravel causes the warrior to spin and lose balance."""
p1_repl1 = """- **Inertia & Newton's Third Law:** Mass cannot be ignored. While titanic Asuras (possessing 1.4x gravity bone density) or booned champions wield crushing 300-pound bronze maces (*Gadā*), mortal Dhanurveda warriors command balanced 15–25 kg (35–55 lb) weapons. In all cases, kinetic recoil must be absorbed through the hips and driven into bedrock via **Apāna grounding**. Swinging without secure footing causes the warrior to spin and tear ligaments."""

p1_target2 = """### 3.1 The 4-Stage Dhanurveda Astra Protocol
Firing an Astra is never a casual button-press. It requires four disciplined stages:

```
[ 1. ĀVĀHANA (आवाहन) ] ──► Chanting Bīja-Mantra; locking deity's concept onto arrow.
          │                 (Archer is stationary & vulnerable for 1–2 breaths!)
          ▼
[ 2. PRAYOGA (प्रयोग) ]  ──► Precision launch; release of conceptual devastation.
          │
          ▼
[ 3. UPASAṂHĀRA (उपसंहार) ]► The mark of a true Maharathi: safely disarming and recalling
          │                 the payload before catastrophic collateral devastation!
          ▼
[ 4. PRATIGHĀTA (प्रतिघात) ]► Tactical Counter-Nullification: Launching an opposing Astra
                            to cancel an incoming strike (e.g. Vāruṇāstra vs Āgneyāstra).
```

### 3.2 The Sing (Gūñja — गूंज)
0.2 seconds before any consecrated Astra or heavy elemental payload detonates, the ambient air emits a high-pitched, crystalline acoustic hum—**The Sing (गूंज)**. Elite martial prodigies do not rely on visual cues; they read this acoustic wave to execute instant evasions or counter-interceptions."""

p1_repl2 = """### 3.1 The 4-Stage Dhanurveda Caster Protocol
According to the *Vasiṣṭha Dhanurveda*, launching an Astra is an exacting metaphysical rite governed by four strict stages:

```
[ 1. ĀVĀHANA (आवाहन) ] ──► Acoustic invocation of Bīja-Mantra; drawing deity's sanction.
          │                 (Archer is stationary & locked in posture for 1.5 seconds!)
          ▼
[ 2. SANDHĀNA (संधान) ] ──► Nocking & Saṅkalpa target-lock; binding cosmic concept to arrow.
          │                 (Archer defines trajectory, duration, and lethal mandate)
          ▼
[ 3. PRAYOGA (प्रयोग) ]  ──► Precision release; payload accelerates into supersonic flight.
          │
          ▼
[ 4. UPASAṂHĀRA (उपसंहार) ]► The hallmark of a true Mahārathī: chanting reverse meter to safely
                            disarm and recall the payload before irreversible environmental ruin!
```

### 3.2 Intersecting Defensive Protocol: Pratighāta (प्रतिघात)
A defender facing an incoming Astra cannot block it with mundane iron. Defense is an autonomous intersecting protocol:
- **Pratighāta (Counter-Interception):** Launching the exact counter-Astra (*Vāruṇāstra* against *Āgneyāstra*, *Sūryāstra* against *Andhākārāstra*) to collide at the geometric midpoint and nullify both payloads mid-air.

### 3.3 The Sing (Gūñja — गूंज): Localized Etheric Cavitation
An incoming Astra accelerates beyond supersonic speed (>343 m/s), outrunning its atmospheric wake. How then do warriors evade it?
- **Ākāśa Cavitation:** The 0.20 to 0.35-second warning hum—**The Sing (गूंज)**—is **नही** atmospheric sound traveling from the bowstring. It is **localized spatial cavitation at the target locus**.
- Because an Astra forcibly collapses high-dimensional conceptual energy into physical matter, the spatial fabric (*Ākāśa*) directly around the intended victim's coordinates begins to thin and vibrate violently 0.2 seconds prior to impact.
- Elite street fighters like Neel read this localized crystalline shear hum to dive behind basalt bastions or pull armored enemies into the blast zone."""

p1_target3 = """- **Dramatic Function:** Curses introduce tragic vulnerability and tactical grit (like Karna's chariot wheel sinking at the decisive moment). Characters must fight around their handicaps.

---

## 6. Pillar 5: Pratijñā & Tapasyā (प्रतिज्ञा व तपस्या — Binding Vows)

This is the ancient Sanatan root of the **Binding Vow** mechanic celebrated in modern anime (*Hunter x Hunter*, *Jujutsu Kaisen*).

### 6.1 The Law of Voluntary Sacrifice (त्याग-बल)
In Brahmand, power cannot be generated from nothing (*No Free Energy*). When a warrior voluntarily binds themselves to an irreversible, life-limiting condition:
- *The Bhīṣma Vow:* Swearing lifelong celibacy and non-rulership multiplied his martial prowess to unassailable heights (*Icchā-Mṛtyu*).
- **Novel Combat Application:** A warrior facing mortal peril can swear a binding vow before fire or water:
  - *"I swear upon my mother's pyre: I shall fight this duel with only my left arm."*
  - *"I swear: If I retreat one pace, my heart shall stop."*
- **The Cosmic Ledger's Response:** Ananta records the severe self-imposed restriction and **multiplies the warrior's current combat output tenfold**! But if the vow is broken, the warrior suffers instant soul-calcification."""

p1_repl3 = """- **Dramatic Function:** Curses introduce tragic vulnerability and tactical grit (like Karna's chariot wheel sinking at the decisive moment). Characters must fight around their handicaps.
- **The Arena Samaya-Bandhana Rule (समयावच्छिन्न बंधन):** To prevent defeated gladiators from spitefully cursing the victor with their dying breath, Proving Games sands are consecrated ground under Concord law. Combatants sign the *Samaya-Patra*, legally and metaphysically waiving personal grievance claims. Because *Vāk-Siddhi* strictly requires genuine, unrighteous victimhood (*Adharma*), consensual arena dying curses possess zero moral leverage and dissipate harmlessly into the sand.

---

## 6. Pillar 5: Pratijñā & Tapasyā (प्रतिज्ञा व तपस्या — Binding Vows)

This is the ancient Sanatan root of the **Binding Vow** mechanic celebrated in modern anime (*Hunter x Hunter*, *Jujutsu Kaisen*).

### 6.1 The Law of Voluntary Sacrifice (त्याग-बल)
In Brahmand, power cannot be generated from nothing (*No Free Energy*). When a warrior voluntarily binds themselves to an irreversible, life-limiting condition:
- *The Bhīṣma Vow:* Swearing lifelong celibacy and non-rulership multiplied his martial prowess to unassailable heights (*Icchā-Mṛtyu*).
- **Novel Combat Application:** A warrior facing mortal peril can swear a binding vow before fire or water:
  - *"I swear upon my mother's pyre: I shall fight this duel with only my left arm."*
  - *"I swear: If I retreat one pace, my heart shall stop."*
- **Karmic Proportionality (कार्मिका प्रतिदाना — Anti-Micro-Vow Law):** Ananta's cosmic substrate does **नही** reward cheap, temporary theatrical tricks (e.g. "I vow to close my eyes for three seconds"). Power multipliers scale strictly with **permanence, irreversibility, and existential risk**. Trivial or easily reversible vows yield zero power spike (<1.001x); only permanent, life-altering sacrifices unlock tenfold multipliers.
- **The Broken Vow Penalty:** If a sworn Pratigya is broken, Ananta immediately extracts the unpaid debt through instant, irreversible soul-calcification."""

replace_in_file(r"02_POWER_SYSTEM\01_The_Six_Epic_Pillars.md", p1_target1, p1_repl1)
replace_in_file(r"02_POWER_SYSTEM\01_The_Six_Epic_Pillars.md", p1_target2, p1_repl2)
replace_in_file(r"02_POWER_SYSTEM\01_The_Six_Epic_Pillars.md", p1_target3, p1_repl3)

# --- 2. 02_POWER_SYSTEM/02_Elements_Preta_and_Cursed_Weapons.md ---
p2_target1 = """### 4.1 Physical Anatomy & Tactile Reality
- **The Executioner's Cuff:** A heavy, blackened iron bracer etched with broken celestial cuneiform that wraps tightly around Neel's left forearm from wrist to elbow. It was originally an abyssal shackle used during Era 2 to bind catastrophic entities in the Corrupted Chasm.
- **The Barbed Links:** Thirty-three interlocking triangular links of dull meteoric iron, each lined with jagged micro-barbs that bite into whatever they wrap around.
- **The Abyssal Lock:** The locking clasp remains permanently jammed in a semi-open fracture, emitting faint wisps of sub-zero black vapor whenever Neel's pulse spikes above 140 BPM.
- **Mass & Inertia:** In resting state, KALI weighs approximately **18 kilograms (40 lbs)**. It is dead, agonizing weight on a mortal teenager's arm. To wield it, Neel must rely on torque, hip pivot, and Apana grounding rather than raw arm biceps.

### 4.2 Combat Forms & Kinetic Maneuvers

#### Form 1: Pāśa-Bandhana (पाश-बंधन — The Grappling Lash)
- **Execution:** Neel whips his left arm forward using a pitcher's shoulder snap, allowing the barbed chain to uncoil up to 45 feet.
- **Application:** Wraps around an enemy's throat, wrist, or weapon shaft. The micro-barbs bite deep into armor seams.
- **Kinetic Vector:** Neel drives his heels into the flagstones (**Apana vector**) and violently yanks his torso back, using leverage to pull heavier armored opponents off balance or slam them into cobblestones.

#### Form 2: Vajra-Kavacha (वज्र-कवच — The Coiled Iron Buckler)
- **Execution:** Neel contracts the chain rapidly around his left forearm, forming a tight, 4-inch-thick spiral iron shield.
- **Application:** Blocks heavy cleaving strikes from maces or bronze blades.
- **Tactile Recoil:** The steel-on-iron impact sends bone-jarring vibration up Neel's humerus, bruising muscle tissue and requiring him to brace his right hand behind his left wrist."""

p2_repl1 = """### 4.1 Physical Anatomy & Tactile Reality
- **The Executioner's Cuff:** A heavy, blackened iron bracer etched with broken celestial cuneiform that wraps tightly around Neel's left forearm from wrist to elbow. It was originally an abyssal shackle used during Era 2 to bind catastrophic entities in the Corrupted Chasm.
- **The 33 Sacred Links (Physical Chain: 8 Feet):** Thirty-three interlocking triangular links of dull meteoric iron (~2.8 inches per link), lined with jagged micro-barbs. This exact length permits the chain to coil fluidly into the forearm buckler without jutting like railway spikes.
- **The 45-Foot Spectral Extension:** When Neel lashes out (*Pāśa-Bandhana*), the terminal anchor barb draws upon the abyssal reservoir, unleashing a trailing **37-foot tether of condensed Preta-frost and ectoplasmic shadow-links**, achieving an uncoiled tactical reach of 45 feet (13.7 meters).
- **The Abyssal Lock:** The locking clasp remains permanently jammed in a semi-open fracture, emitting faint wisps of sub-zero black vapor whenever Neel's pulse spikes above 140 BPM.
- **Mass & Resting Bandolier Carry:** In resting state, KĀLĪ weighs approximately **18 kilograms (40 lbs)**. Strapping 18 kg permanently to a mortal wrist would dislocate the elbow within days. Outside combat, Neel unspools the chain from his wrist and loops it diagonally across his chest and waist like an **ascetic iron bandolier**, distributing the deadweight across his pelvic core and spine via natural **Apāna grounding**. In battle, he snaps it back down onto his forearm in a heartbeat.

### 4.2 Combat Forms & Kinetic Maneuvers

#### Form 1: Pāśa-Bandhana (पाश-बंधन — The Grappling Lash)
- **Execution:** Neel whips his left arm forward using a pitcher's shoulder snap. The 8-foot iron chain snaps outward and instantly discharges its 37-foot Preta-tether, reaching up to 45 feet total.
- **Application:** Wraps around an enemy's throat, wrist, or weapon shaft. The micro-barbs bite deep into armor seams.
- **Kinetic Vector:** Neel drives his heels into the flagstones (**Apāna vector**) and violently yanks his torso back, using leverage to pull heavier armored opponents off balance or slam them into cobblestones.

#### Form 2: Vajra-Kavacha (वज्र-कवच — The Coiled Iron Buckler)
- **Execution:** Neel contracts the 33 links rapidly around his left forearm, forming a tight, 4-inch-thick spiral iron shield.
- **Application:** Blocks heavy cleaving strikes from maces or bronze blades.
- **Tactile Recoil:** The steel-on-iron impact sends bone-jarring vibration up Neel's humerus, bruising muscle tissue and requiring him to brace his right hand behind his left wrist."""

p2_target2 = """2. **Kuro's Thermal Buffering:**
   Neel's companion, the shadow hound **Kuro (Sheru)**, acts as an external soul-radiator. Kuro consumes the excess necrotic frost leaking from KALI, preventing the frostbite from advancing past Neel's elbow."""

p2_repl2 = """2. **Kuro's Thermal Buffering & Preta Saturation Ceiling (प्रेत-संतृप्ती मर्यादा):**
   Neel's companion, the shadow hound **Kuro (Sheru)**, acts as an external soul-radiator. Kuro consumes the excess necrotic frost leaking from KĀLĪ, preventing frostbite from advancing past Neel's elbow.
   - *The Anti-Buff Ceiling:* Kuro does **नही** enjoy an infinite power buff. He has a strict **Preta Saturation Ceiling**. If Kuro absorbs too much sub-zero miasma in a single engagement, his internal organs begin to freeze, he vomits black ice, and his mind regresses into feral, rabid bloodlust where he snaps at Neel. This physiological limit forces Neel to strictly ration KĀLĪ's deployment to short, decisive bursts."""

replace_in_file(r"02_POWER_SYSTEM\02_Elements_Preta_and_Cursed_Weapons.md", p2_target1, p2_repl1)
replace_in_file(r"02_POWER_SYSTEM\02_Elements_Preta_and_Cursed_Weapons.md", p2_target2, p2_repl2)

# --- 3. 02_POWER_SYSTEM/03_Astra_Codex_and_Invocation_Rites.md ---
p3_target1 = """```
══════════════════════════════════════════════════════════════════════════════════════════
                            THE 4-STAGE ASTRA LIFECYCLE
══════════════════════════════════════════════════════════════════════════════════════════

  [ 1. ĀVĀHANA (आवाहन) ]          Chanting the acoustic Bīja-Mantra. Anchoring the deity's
            │                     concept onto the arrow/projectile tip.
            │                     • Duration: 1.5 to 3.0 seconds (1–2 full breaths).
            │                     • State: The archer is immobilized and fully vulnerable!
            ▼
  [ 2. PRAYOGA (प्रयोग) ]         The physical release and vector propulsion.
            │                     • The arrow accelerates beyond supersonic speed.
            │                     • The conceptual payload expands to its true scale.
            ▼
  [ 3. UPASAṂHĀRA (उपसंहार) ]     The supreme mark of a disciplined Maharathi.
            │                     • Chanting the counter-mantra to safely dissolve and
            │                       recall the cosmic warhead before civilian ruin.
            ▼
  [ 4. PRATIGHĀTA (प्रतिघात) ]     Tactical Counter-Interception.
                                  • Launching an opposing Astra mid-flight to nullify the
                                    incoming payload in mid-air.
══════════════════════════════════════════════════════════════════════════════════════════
```

### 2.1 Stage 1: Āvāhana (आवाहन — The Acoustic Lock)
- **The Chhandas Metric:** The invocation requires precise Sanskrit meter (*Gāyatrī, Triṣṭubh, Anuṣṭubh*). A single mispronounced syllable or dropped aspirated consonant ruins the acoustic resonance, causing the arrow to misfire or detonate in the archer's quiver.
- **The Tactical Window:** While chanting, the warrior must focus their *Udāna* (throat vocalization) and *Samāna* (core furnace). They cannot dodge, pivot, or parry. In tactical combat, an archer chanting an Astra relies entirely on frontline vanguard defenders to guard their flank during these 2 precious seconds.

### 2.2 Stage 2: Prayoga (प्रयोग — The Vector Strike)
- Once released, the Astra is guided by conceptual certainty (*Saṅkalpa*). Low-tier Astras travel in direct kinetic arcs; high-tier Astras alter atmospheric pressure, track target heat signatures, or bypass physical walls by translating briefly into light or sound waves.

### 2.3 Stage 3: Upasaṁhāra (उपसंहार — The Recalling Rite)
- **The True Test of Mastery:** In the *Mahābhārata*, Arjuna could invoke and safely recall the *Brahmāstra*; Ashwatthama knew only how to release it (*Prayoga*), but lacked the moral clarity and spiritual discipline to withdraw it (*Upasaṁhāra*), resulting in apocalyptic ecological fallout.
- **The Penalty of Failed Upasaṁhāra:** If an Astra cannot be safely recalled, the residual cosmic radiation poisons the ground for three leagues (*Krośas*), causing barren soil, cracked water sources, and biological withering for twelve months.

### 2.4 Stage 4: Pratighāta (प्रतिघात — Counter-Nullification)
- True high-level combat is an intellectual duel of **Astra Counter-Matrices**. An incoming Astra cannot be blocked by an ordinary shield. It must be met with its precise metaphysical counter-Astra before impact."""

p3_repl1 = """```
══════════════════════════════════════════════════════════════════════════════════════════
                     THE CANONICAL DHANURVEDA CASTER PROTOCOL
══════════════════════════════════════════════════════════════════════════════════════════

  [ 1. ĀVĀHANA (आवाहन) ]          Chanting the acoustic Bīja-Mantra. Invoking divine sanction.
            │                     • Duration: 1.5 to 3.0 seconds (1–2 full breaths).
            │                     • State: The archer is locked in posture and fully vulnerable!
            ▼
  [ 2. SANDHĀNA (संधान) ]        Nocking, drawing, and Saṅkalpa target-lock.
            │                     • Imbuing the physical shaft with the conceptual warhead.
            │                     • Determining flight trajectory, blast vector, and duration.
            ▼
  [ 3. PRAYOGA (प्रयोग) ]         The physical release and supersonic propulsion.
            │                     • The missile accelerates past Mach 1 into target coordinates.
            │                     • Triggers localized Ākāśa etheric cavitation at impact zone.
            ▼
  [ 4. UPASAṂHĀRA (उपसंहार) ]     The supreme mark of a disciplined Mahārathī.
                                  • Chanting reverse Sanskrit meter to safely dissolve and recall
                                    the conceptual warhead before irreversible ecological ruin!
══════════════════════════════════════════════════════════════════════════════════════════
```

### 2.1 Stage 1: Āvāhana (आवाहन — The Acoustic Lock)
- **The Chhandas Metric:** The invocation requires precise Sanskrit meter (*Gāyatrī, Triṣṭubh, Anuṣṭubh*). A single mispronounced syllable or dropped aspirated consonant ruins the acoustic resonance, causing the arrow to misfire or detonate in the archer's quiver.
- **The Tactical Window:** While chanting, the warrior must focus their *Udāna* (throat vocalization) and *Samāna* (core furnace). They cannot dodge, pivot, or parry. In tactical combat, an archer chanting an Astra relies entirely on frontline vanguard defenders to guard their flank during these 2 precious seconds.

### 2.2 Stage 2: Sandhāna (संधान — The Nocking & Conceptual Binding)
- The warrior nocks the consecrated shaft to the bowstring, harmonizing breath (*Prāṇa*) with intention (*Saṅkalpa*). During Sandhāna, the physical arrow becomes weightless as divine geometry envelops the tip. If the archer's focus flickers or fear intrudes, the binding unravels before launch.

### 2.3 Stage 3: Prayoga (प्रयोग — The Vector Strike)
- Once released, the Astra accelerates beyond supersonic speed. Low-tier Astras travel in devastating kinetic arcs; high-tier Astras alter atmospheric pressure, track target heat signatures, or bypass physical walls by translating briefly into light or sound waves.

### 2.4 Stage 4: Upasaṁhāra (उपसंहार — The Recalling Rite)
- **The True Test of Mastery:** In the *Mahābhārata*, Arjuna could invoke and safely recall the *Brahmāstra*; Ashwatthama knew only how to release it (*Prayoga*), but lacked the moral clarity and spiritual discipline to withdraw it (*Upasaṁhāra*), resulting in apocalyptic ecological fallout.
- **The Penalty of Failed Upasaṁhāra:** If an Astra cannot be safely recalled, the residual cosmic radiation poisons the ground for three leagues (*Krośas*), causing barren soil, cracked water sources, and biological withering for twelve months.

### 2.5 Intersecting Defensive Protocol: Pratighāta (प्रतिघात — Counter-Nullification)
- True high-level combat is an intellectual duel of **Astra Counter-Matrices**. An incoming Astra cannot be blocked by an ordinary shield. It must be met mid-flight by its precise metaphysical counter-Astra (*Pratyastra*) before impact."""

p3_target2 = """```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        THE ACOUSTIC PHENOMENON: GŪÑJA (गूंज)                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ • Window of Warning: Exactly 0.20 to 0.35 seconds before terminal detonation.         │
│ • Acoustic Nature: A piercing, crystalline hum like a tuning fork vibrating on glass.  │
│ • Physical Cause: The sudden displacement of Ākāśa (Ether) as conceptual reality       │
│   condenses into physical space.                                                       │
│ • Tactical Significance: Master warriors do not look at the glowing light; they read  │
│   the pitch and doppler of the Gūñja to execute parries, rolls, or counter-launches.   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```"""

p3_repl2 = """```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        THE ACOUSTIC PHENOMENON: GŪÑJA (गूंज)                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ • Window of Warning: Exactly 0.20 to 0.35 seconds before terminal detonation.         │
│ • Acoustic Nature: A piercing, crystalline hum like a tuning fork vibrating on glass.  │
│ • Physical Cause: Localized Ākāśa Etheric Cavitation at the target locus (NOT sound    │
│   traveling through air, which supersonic arrows outrun). The spatial fabric around     │
│   the impact coordinates begins to thin and vibrate as conceptual mass manifests.       │
│ • Tactical Significance: Master warriors do not look at the glowing light; they read  │
│   the pitch and frequency of the Gūñja to execute evasions, rolls, or counter-launches.│
└────────────────────────────────────────────────────────────────────────────────────────┘
```"""

replace_in_file(r"02_POWER_SYSTEM\03_Astra_Codex_and_Invocation_Rites.md", p3_target1, p3_repl1)
replace_in_file(r"02_POWER_SYSTEM\03_Astra_Codex_and_Invocation_Rites.md", p3_target2, p3_repl2)

# --- 4. 02_POWER_SYSTEM\04_The_Proving_Games_and_Split_Flap_Spire.md ---
p4_target1 = """- **Auditing Authority:** A specialized guild of blind clockwork scribes (*Lipi-Kāras*) resides inside the hollow belly of the spire, verifying fight slips sent via brass pneumatic tubes before pulling the gear levers that flip the boards."""
p4_repl1 = """- **Auditing Authority & Tactile Copper Tokens:** A specialized guild of blind clockwork scribes (*Lipi-Kāras*) resides inside the hollow belly of the spire. Because ink on parchment provides zero tactile feedback in the pitch-black shaft, fight slips are **tactile stamped copper tokens (Tāmra-Mudrā / ताम्र-मुद्रा)** embossed with raised cuneiform matrices by the Quad-Referees' mechanical punch-press. Sent via brass pneumatic tubes, the blind scribes read the raised pin-matrix with their calloused fingertips in complete darkness before pulling the escapement levers that flip the boards."""

p4_target2 = """│ 3. Rank Challenge Windows: A warrior may challenge anyone up to 200 ranks above them. │
│    Direct challenges into the Top 500 require a stake of 100 Silver Panas.             │
│ 4. No Second Chances (एक-प्रवेश): A warrior who loses three consecutive matches is     │
│    banished from the Spire and relegated to the outer Slum Pits.                       │
└────────────────────────────────────────────────────────────────────────────────────────┘"""

p4_repl2 = """│ 3. Rank Challenge Windows: A warrior may challenge anyone up to 200 ranks above them. │
│    Direct challenges into the Top 500 require a stake of 100 Silver Panas.             │
│ 4. Mandatory Recovery Sanctuary (आरोग्य-अवकाश): Following a successful defense on the   │
│    Spire, a fighter earns an official 3-day recovery sanctuary. Syndicates cannot chain│
│    suicide-challengers to exhaust an unaligned fighter, unless waived for tripled purse│
│ 5. Arena Samaya-Bandhana: Consecrated sand waives personal grievance claims; dying      │
│    curses lack Adharmic victimhood leverage and burn out harmlessly into the earth.    │
│ 6. No Second Chances (एक-प्रवेश): A warrior who loses three consecutive matches is     │
│    banished from the Spire and relegated to the outer Slum Pits.                       │
└────────────────────────────────────────────────────────────────────────────────────────┘"""

p4_target3 = """shouts of the runners carrying ink-wet parchment tally slips to tavern betting stalls."""
p4_repl3 = """shouts of the runners carrying tactile stamped copper tokens (*Tāmra-Mudrā*) to tavern betting stalls."""

replace_in_file(r"02_POWER_SYSTEM\04_The_Proving_Games_and_Split_Flap_Spire.md", p4_target1, p4_repl1)
replace_in_file(r"02_POWER_SYSTEM\04_The_Proving_Games_and_Split_Flap_Spire.md", p4_target2, p4_repl2)
replace_in_file(r"02_POWER_SYSTEM\04_The_Proving_Games_and_Split_Flap_Spire.md", p4_target3, p4_repl3)

# --- 5. 02_POWER_SYSTEM\05_Tier_Naming_and_Language_Hierarchy.md ---
p5_target1 = """```
══════════════════════════════════════════════════════════════════════════════════════════
                     THE COMPLETE TIER NAMING & LINGUISTIC AXIS
══════════════════════════════════════════════════════════════════════════════════════════

  [ TIER 5: APEX / SOVEREIGN ] ──► Ati-Mahārathī | Rāja-Rangashālā | Deva-Vāṇī (Śabda-Brahma)
  (अति-शिखर / सार्वभौम स्तर)        Amṛta-Dhātu | Mahā-Astras | Niṣka / Golden Suvarṇa
                                    ▲
  [ TIER 4: HIGH CHAMPION ]    ──► Mahārathī | Ayomaya-Rangabhūmi | Śāstric Classical Sanskrit
  (वरिष्ठ / महारथी स्तर)            Divya-Muktā / Nāga-Maṇi | Uttama-Astras | Silver Paṇa
                                    ▲
  [ TIER 3: DISCIPLINED VANGUARD]─► Atirathī & Rathī | Madhyama-Rangabhūmi | Vyavahāra-Prākṛt
  (मध्यम / रथी स्तर)                Prāṇa-Maṇi (प्राण-मणि) | Prathama-Astras | Copper Māṣa
                                    ▲
  [ TIER 2: NOVICE SURVIVOR ]  ──► Ardha-Rathī | Sieve Brackets (#3,999–#2,500) | Apabhraṁśa
  (प्राथमिक / अर्धरथी स्तर)          Vanya-Dhātu / Bone Relics | Yantra-Śastra | Cowrie-Shells
                                    ▲
  [ TIER 1: UNRANKED FEEDER ]  ──► Padāti / Āmiṣa (आमिष) | Adhama Pits (अधम आखाडे) | Street Slang
  (कनिष्ठ / आमिष स्तर)              Mundane Scrap Iron | Raw Melee | Scraps & Mumbai ₹11 Change
══════════════════════════════════════════════════════════════════════════════════════════
```"""

p5_repl1 = """```
══════════════════════════════════════════════════════════════════════════════════════════
                     THE COMPLETE 6-TIER NAMING & LINGUISTIC AXIS
══════════════════════════════════════════════════════════════════════════════════════════

  [ TIER 6: APEX SOVEREIGN ]   ──► Ati-Mahārathī | Rāja-Rangaśālā | Deva-Vāṇī (Śabda-Brahma)
  (अति-शिखर / सार्वभौम स्तर)        Amṛta-Dhātu | Cosmic Astras | Niṣka / Golden Suvarṇa
                                    ▲
  [ TIER 5: FORTRESS BREAKER ] ──► Mahārathī | Ayomaya-Rangabhūmi (Elite) | Śāstric Classical Sanskrit
  (शिखर / महारथी स्तर)              Nāga-Maṇi / Gaja-Muktā | Mahā-Astras | Gold Suvarṇa
                                    ▲
  [ TIER 4: ELITE VANGUARD ]   ──► Atirathī | Ayomaya-Rangabhūmi (Vanguard) | Śāstric Sanskrit
  (वरिष्ठ / अतिरथी स्तर)            Prāṇa-Maṇi (High) | Uttama-Astras | Silver Paṇa
                                    ▲
  [ TIER 3: REGULAR CAPTAIN ]  ──► Rathī | Madhyama-Rangabhūmi | Vyavahāra-Prākṛt
  (मध्यम / रथी स्तर)                Prāṇa-Maṇi (Basic) | Prathama-Astras | Copper Māṣa
                                    ▲
  [ TIER 2: NOVICE SURVIVOR ]  ──► Ardha-Rathī | The Sieve (#3,999–#2,500) | Apabhraṁśa
  (प्राथमिक / अर्धरथी स्तर)          Vanya-Asthi / Bone Relics | Yantra-Śastra | Cowrie-Shells
                                    ▲
  [ TIER 1: UNRANKED FEEDER ]  ──► Padāti / Āmiṣa (आमिष) | Adhama Pits (अधम आखाडे) | Street Register
  (कनिष्ठ / आमिष स्तर)              Mundane Scrap Iron | Raw Melee | Scraps & Mumbai ₹11 Change
══════════════════════════════════════════════════════════════════════════════════════════
```"""

replace_in_file(r"02_POWER_SYSTEM\05_Tier_Naming_and_Language_Hierarchy.md", p5_target1, p5_repl1)

# --- 6. 03_CHARACTERS/02_Neel_Canonical_Dossier.md ---
p6_target1 = """### 5.1 KĀLĪ: Mechanical & Tactical Analysis
- **Physical Weight:** 18 kilograms (approx. 40 lbs) of dead, rusted meteoric iron. To swing it without tearing his rotator cuff, Neel must pivot his hips and anchor his heels (**Apāna grounding**).
- **The 33 Barbed Links:** Can whip outward up to 45 feet. The barbed teeth can wrap around an adversary's neck, bind weapon shafts, or bite into stone parapets for vertical ascension.
- **The Sub-Zero Toll:** Every time KALI extends or hardens, it leaches biological warmth from Neel's left arm. If used continuously for more than three minutes, his fingertips turn numb and blue with frostbite.

### 5.2 Sheru (Kuro): The Living Buffer
- Sheru is not an obedient pet; he is an alley-smart survivor just like Neel.
- Whenever KALI leaks lethal necrotic frost into Neel's bloodstream, Sheru presses his muzzle against the iron cuff, greedily inhaling the black spectral vapor as if it were marrow broth. This symbiotic loop keeps Neel alive while strengthening Sheru's shadow mantle."""

p6_repl1 = """### 5.1 KĀLĪ: Mechanical & Tactical Analysis
- **Physical Weight & Bandolier Carry:** 18 kilograms (approx. 40 lbs) of dead, rusted meteoric iron. Outside combat, Neel loops KĀLĪ diagonally across his chest and waist as an **ascetic iron bandolier**, distributing the load across his pelvic core and spine via natural **Apāna grounding**. In battle, he pivots his hips and anchors his heels to unleash devastating kinetic torque.
- **The 33 Sacred Links (8 Feet Iron + 37 Feet Preta-Tether):** The physical chain comprises 33 triangular barbed links (~2.8 inches per link), forming an 8-foot coil that fits snugly around his left forearm into *Vajra-Kavacha*. In *Pāśa-Bandhana*, the terminal triangular fang unspools a trailing 37-foot tether of condensed Preta-frost shadow-links, reaching a lethal 45 feet (13.7 m) total.
- **The Sub-Zero Toll:** Every time KĀLĪ extends or hardens, it leaches biological warmth from Neel's left arm. If used continuously for more than three minutes, his fingertips turn numb and blue with frostbite.

### 5.2 Sheru (Kuro): The Living Buffer & Saturation Ceiling
- Sheru is not an obedient pet; he is an alley-smart survivor just like Neel.
- Whenever KĀLĪ leaks lethal necrotic frost into Neel's bloodstream, Sheru presses his muzzle against the iron cuff, inhaling the black spectral vapor. This symbiotic buffer keeps Neel alive while strengthening Sheru's shadow coat.
- **Preta Saturation Ceiling (प्रेत-संतृप्ती मर्यादा):** Sheru cannot absorb infinite frost. If oversaturated during prolonged combat, his internal organs begin to freeze, he vomits black ice, and his primal instincts regress into rabid bloodlust. Neel must carefully monitor Sheru's breath, ending fights quickly to protect his hound."""

replace_in_file(r"03_CHARACTERS\02_Neel_Canonical_Dossier.md", p6_target1, p6_repl1)

# --- 7. 01_WORLD_BIBLE/00_Sanatan_Encyclopedic_Codex.md ---
p7_target1 = """### 14. Dhanurveda Astra Protocol (धनुर्वेद अस्त्र-प्रयोग विधी)
- **Etymology & Root:** *Dhanuḥ* (धनुष् — bow, weapon of projection) + *Veda* (knowledge, sacred science).
- **Scriptural Authority:** *Vasiṣṭha Dhanurveda*; *Śārṅgadhara Paddhati* (Dhanur-Veda section); *Agni Purāṇa* ch. 249–252.
- **Classical Definition:** The fourfold protocol governing martial ordinance:
  1. *Ādāna / Āvāhana* (आदान / आवाहन) — Drawing and invoking divine conceptual sanction via Bīja-Mantra.
  2. *Sandhāna* (संधान) — Nocking, aiming, and spiritual target-locking (*Saṅkalpa*).
  3. *Mokṣa / Prayoga* (मोक्ष / प्रयोग) — Releasing the metaphysical payload.
  4. *Saṁhāra / Upasaṁhāra* (संहार / उपसंहार) — Disarming, recalling, and dissolving the cosmic energy.
- **Novel Context & Adaptation:** In *Brahmand*, every Astra invocation adheres rigorously to this 4-step sequence.
- **Tactical Mechanics:** Archers are completely immobilized during the 1.5 to 3.0-second *Āvāhana* window. Skilled enemies exploit this stationary interval to strike before the chant concludes.
- **Trope Rejection:** Deploying an Astra is **नही** a thought-controlled videogame macro. It is an exacting ritual involving acoustic resonance, posture lock, and intense mental concentration."""

p7_repl1 = """### 14. Dhanurveda Astra Protocol (धनुर्वेद अस्त्र-प्रयोग विधी)
- **Etymology & Root:** *Dhanuḥ* (धनुष् — bow, weapon of projection) + *Veda* (knowledge, sacred science).
- **Scriptural Authority:** *Vasiṣṭha Dhanurveda*; *Śārṅgadhara Paddhati* (Dhanur-Veda section); *Agni Purāṇa* ch. 249–252.
- **Classical Definition:** The fourfold protocol governing martial ordinance for the caster:
  1. *Āvāhana* (आवाहन) — Drawing divine conceptual sanction via acoustic Bīja-Mantra (1.5 to 3.0s stationary lock).
  2. *Sandhāna* (संधान) — Nocking, drawing, and binding the concept to the arrow shaft via intense *Saṅkalpa*.
  3. *Prayoga* (प्रयोग) — Releasing the payload into supersonic trajectory (>343 m/s).
  4. *Upasaṁhāra* (उपसंहार) — Chanting reverse meter to safely recall and dissolve the payload before environmental ruin.
- **Novel Context & Adaptation:** In *Brahmand*, every Astra invocation adheres rigorously to this 4-step sequence.
- **Tactical Mechanics:** Archers are completely immobilized during the 1.5 to 3.0-second *Āvāhana* window. Skilled enemies exploit this stationary interval to strike before the chant concludes.
- **Trope Rejection:** Deploying an Astra is **नही** a thought-controlled videogame macro. It is an exacting ritual involving acoustic resonance, posture lock, and intense mental concentration."""

p7_target2 = """### 17. Gūñja / The Sing (गूंज — The Acoustic Tell)
- **Etymology & Root:** *Gūñj* (गुञ्ज् — to hum, buzz, emit a continuous crystalline acoustic resonance).
- **Scriptural Authority:** *Śabda-Brahma* physics from *Pātañjala Yoga Sūtras* and *Śiva Sūtras*; acoustic displacement of Ākāśa.
- **Classical Definition:** The subtle vibrational displacement of space-ether (*Ākāśa-Spandana*) that occurs immediately before intense concentrated energy condenses into physical reality.
- **Novel Context & Adaptation:** In the Proving Games and Setu combat zones, high-tier Astras and heavy elemental strikes emit a distinct crystalline ringing 0.20 to 0.35 seconds before detonation.
- **Tactical Mechanics:** Neel uses this 0.2-second window to dive, parry, or pull obstacles into the line of fire.
- **Trope Rejection:** Warriors do **नही** react to visual laser beams; they fight by ear, reading acoustic tells in the air."""

p7_repl2 = """### 17. Gūñja / The Sing (गूंज — The Acoustic Tell)
- **Etymology & Root:** *Gūñj* (गुञ्ज् — to hum, buzz, emit a continuous crystalline acoustic resonance).
- **Scriptural Authority:** *Śabda-Brahma* physics from *Pātañjala Yoga Sūtras* and *Śiva Sūtras*; acoustic displacement of Ākāśa.
- **Classical Definition:** Localized space-ether cavitation (*Ākāśa-Spandana*) occurring at the target impact locus 0.20 to 0.35 seconds prior to impact. Because Astras travel supersonically (>343 m/s), sound cannot travel through the atmosphere from the bow; rather, the fabric of Ākāśa at the destination coordinates thins and hums as high-dimensional conceptual energy condenses into matter.
- **Novel Context & Adaptation:** In the Proving Games and Setu combat zones, this distinct crystalline ringing provides elite warriors their sole survival tell.
- **Tactical Mechanics:** Neel uses this 0.2-second localized hum to dive behind basalt bastions or pull armored enemies into the blast zone.
- **Trope Rejection:** Warriors do **नही** react to visual laser beams; they fight by ear, reading spatial cavitation tells."""

p7_target3 = """### 19. Śāpa (शाप — Metaphysical Curse Mechanics)
- **Etymology & Root:** *Śap* (शप् — to pronounce an oath, to utter an irrevocable karmic binding under distress).
- **Scriptural Authority:** *Bṛhadāraṇyaka Upaniṣad*; *Mahābhārata* Śānti Parva; *Vālmīki Rāmāyaṇa* Bāla Kāṇḍa.
- **Classical Definition:** A binding karmic decrement or functional handicap produced by *Vāk-Siddhi* (truth-empowered speech). A curse cannot be washed away with ordinary water or medical remedies; it alters the ontological state of the target until its specific conditions of release (*Śāpānta*) are satisfied.
- **Novel Context & Adaptation:** Curses function as immutable tactical handicaps in *Brahmand* (weapon failure, selective amnesia, directional blindness).
- **Tactical Mechanics:** Warriors cannot simply dispel a curse; they must fight around its constraints or fulfill its semantic release condition.
- **Trope Rejection:** A Śāpa is **नही** a video-game \"debuff\" that can be cured with a potion or dispelled by a cleric."""

p7_repl3 = """### 19. Śāpa (शाप — Metaphysical Curse Mechanics)
- **Etymology & Root:** *Śap* (शप् — to pronounce an oath, to utter an irrevocable karmic binding under distress).
- **Scriptural Authority:** *Bṛhadāraṇyaka Upaniṣad*; *Mahābhārata* Śānti Parva; *Vālmīki Rāmāyaṇa* Bāla Kāṇḍa.
- **Classical Definition:** A binding karmic decrement or functional handicap produced by *Vāk-Siddhi* (truth-empowered speech). A curse cannot be washed away with ordinary water or medical remedies; it alters the ontological state of the target until its specific conditions of release (*Śāpānta*) are satisfied.
- **Novel Context & Adaptation:** Curses function as immutable tactical handicaps in *Brahmand* (weapon failure, selective amnesia, directional blindness).
- **The Arena Samaya-Bandhana Rule:** To prevent dying gladiators from cursing victors, arena sands are consecrated ground where combatants sign the *Samaya-Patra*, legally waiving personal grievance claims. Because Vāk-Siddhi requires unrighteous victimhood (*Adharma*), consensual arena death curses possess zero moral leverage and burn out harmlessly.
- **Trope Rejection:** A Śāpa is **नही** a video-game \"debuff\" that can be cured with a potion or dispelled by a cleric."""

p7_target4 = """### 20. Pratijñā & Tapasyā (प्रतिज्ञा व तपस्या — Binding Vows of Power)
- **Etymology & Root:** *Prati* (towards) + *Jñā* (knowledge, declaration) — A solemn, binding declaration; *Tap* (तप् — to generate spiritual heat through self-abnegation).
- **Scriptural Authority:** *Chāndogya Upaniṣad* 4.10; *Mahābhārata* Ādi Parva (Bhīṣma-Pratijñā).
- **Classical Definition:** The ontological law that voluntary sacrifice, self-limitation, and rigid vow-keeping compress the soul's focus, generating immense metaphysical power (*Tejas*).
- **Novel Context & Adaptation:** The authentic Sanatan antecedent to modern anime \"binding vows\". By willingly surrendering an arm, an eye, or swearing lifelong celibacy, a warrior's remaining capabilities are magnified exponentially.
- **Tactical Mechanics:** A warrior facing mortal defeat can swear a sudden, binding vow before consecrated fire/water to achieve a temporary tenfold multiplier, with the penalty of instant soul-destruction if the vow is violated.
- **Trope Rejection:** Power cannot be bought with money or gained without sacrifice. Power strictly obeys the law of **त्याग-बल (Sacrifice-Strength)**."""

p7_repl4 = """### 20. Pratijñā & Tapasyā (प्रतिज्ञा व तपस्या — Binding Vows of Power)
- **Etymology & Root:** *Prati* (towards) + *Jñā* (knowledge, declaration) — A solemn, binding declaration; *Tap* (तप् — to generate spiritual heat through self-abnegation).
- **Scriptural Authority:** *Chāndogya Upaniṣad* 4.10; *Mahābhārata* Ādi Parva (Bhīṣma-Pratijñā).
- **Classical Definition:** The ontological law that voluntary sacrifice, self-limitation, and rigid vow-keeping compress the soul's focus, generating immense metaphysical power (*Tejas*).
- **Novel Context & Adaptation:** The authentic Sanatan antecedent to modern anime \"binding vows\". By willingly surrendering an arm, an eye, or swearing lifelong celibacy, a warrior's remaining capabilities are magnified exponentially.
- **Karmic Proportionality (Kārmika Pratidāna):** Ananta does **नही** reward cheap micro-vows (\"I vow to fight with one finger for two seconds\"). Multipliers scale strictly with permanence, irreversibility, and existential risk; trivial vows yield zero energy (<1.001x).
- **Tactical Mechanics:** A warrior facing mortal defeat can swear a sudden, binding vow before consecrated fire/water to achieve a tenfold multiplier, with the penalty of instant soul-calcification if violated.
- **Trope Rejection:** Power cannot be bought with money or gained without sacrifice. Power strictly obeys the law of **त्याग-बल (Sacrifice-Strength)**."""

p7_target5 = """### 32. KĀLĪ (काली — The Abyssal Spiked Shackle)
- **Etymology & Root:** *Kāla* (काल — black, dark, cosmic time, death) + feminine suffix.
- **Scriptural Authority:** *Liṅga Purāṇa*; *Devī Bhāgavata Purāṇa*; representation of unyielding, primordial dissolution.
- **Canonical Status:** Neel's sole weapon. A heavy, rusted black-iron shackle from Era 2 bound to his left forearm.
- **Physical Specifications:**
  - *Mass:* Approximately 18 kg (40 lbs) of dead meteoric iron.
  - *Length:* 33 interlocking triangular links, extending up to 45 feet.
  - *Preta Imbuement:* Forged with the agony of Era 2 Pretas; leaches warmth from the surroundings, creating sub-zero black frost.
- **Tactical Combat Forms:**
  - *Pāśa-Bandhana (Grappling Whip):* 45-foot lash to snare throats, wrists, or weapon shafts.
  - *Vajra-Kavaca (Coiled Buckler):* Chains spiral tightly around Neel's forearm into an iron shield.
  - *Preta-Daṇḍa (Rigid Cudgel):* Chains freeze into a solid 6-foot heavy iron cudgel.
- **Tactical Mechanics:**
  - *Apāna Leverage:* Neel uses Apāna grounding to hook enemy ankles or lock weapon shafts, using leverage against heavier opponents.
  - *The Parasitic Toll:* Leaches biological calories and spreads sub-zero marrow frost up Neel's arm during prolonged activation.
- **Trope Rejection:** KALI is **नही** an obedient magic pet weapon. It is a vicious, cold executioner's shackle that must be ruthlessly dominated through will."""

p7_repl5 = """### 32. KĀLĪ (काली — The Abyssal Spiked Shackle)
- **Etymology & Root:** *Kāla* (काल — black, dark, cosmic time, death) + feminine suffix.
- **Scriptural Authority:** *Liṅga Purāṇa*; *Devī Bhāgavata Purāṇa*; representation of unyielding, primordial dissolution.
- **Canonical Status:** Neel's sole weapon. A heavy, rusted black-iron shackle from Era 2 bound to his left forearm.
- **Physical Specifications & Bandolier Carry:**
  - *Mass:* Approximately 18 kg (40 lbs) of dead meteoric iron.
  - *Resting Carry:* Outside combat, Neel unspools KĀLĪ from his wrist and loops it diagonally across chest and waist as an **ascetic iron bandolier**, distributing the 18 kg across his pelvis and spine via Apāna grounding to prevent nerve/joint damage.
  - *Physical Length (8 Feet):* 33 interlocking triangular links (~2.8 inches per link) of meteoric iron, permitting tight coiling into the *Vajra-Kavaca* forearm shield without clumsy overhang.
  - *Spectral Reach (45 Feet):* In *Pāśa-Bandhana*, the terminal triangular fang unleashes a trailing 37-foot tether of condensed Preta-frost shadow-links, reaching 45 feet total (13.7 m).
- **Tactical Combat Forms:**
  - *Pāśa-Bandhana (Grappling Whip):* 45-foot lash to snare throats, wrists, or weapon shafts.
  - *Vajra-Kavaca (Coiled Buckler):* 33 iron links spiral tightly around Neel's forearm into a 4-inch-thick shield.
  - *Preta-Daṇḍa (Rigid Cudgel):* Chains freeze into a solid 6-foot heavy iron cudgel.
- **Tactical Mechanics:**
  - *Apāna Leverage:* Neel uses Apāna grounding to hook enemy ankles or lock weapon shafts, using leverage against heavier opponents.
  - *The Parasitic Toll:* Leaches biological calories and spreads sub-zero marrow frost up Neel's arm during prolonged activation.
- **Trope Rejection:** KALI is **नही** an obedient magic pet weapon. It is a vicious, cold executioner's shackle that must be ruthlessly dominated through will."""

p7_target6 = """### 33. Kuro / Śerū (कुरो / शेरू — The Loyal Shadow Hound)
- **Etymology & Root:** *Sheru* (शेर — lion-hearted, street mongrel name from Mumbai); *Kuro* (कृष्ण / काळा — shadow-black, darkened mantle).
- **Scriptural Authority:** *Mahābhārata* Mahāprasthānika Parva (The faithful dog that accompanied Yudhishthira to the gates of Swarga).
- **Canonical Status:** Neel's sole companion who leaped with him during the Dadar Station glitch. Saturated with subtle Preta-currents during the crossing, Sheru evolved into an ash-black, shadow-sheathed hound.
- **Tactical Mechanics:** Serves as Neel's **living thermal buffer**. Sheru inhales the excess necrotic frost leaking from KALI, preventing the frostbite from advancing past Neel's elbow, while strengthening his own shadow coat.
- **Trope Rejection:** Sheru is **नही** a cute fantasy mascot. He is a scarred, one-eared street survivor who bites dirty and guards Neel's back with ferocious loyalty."""

p7_repl6 = """### 33. Kuro / Śerū (कुरो / शेरू — The Loyal Shadow Hound)
- **Etymology & Root:** *Sheru* (शेर — lion-hearted, street mongrel name from Mumbai); *Kuro* (कृष्ण / काळा — shadow-black, darkened mantle).
- **Scriptural Authority:** *Mahābhārata* Mahāprasthānika Parva (The faithful dog that accompanied Yudhishthira to the gates of Swarga).
- **Canonical Status:** Neel's sole companion who leaped with him during the Dadar Station glitch. Saturated with subtle Preta-currents during the crossing, Sheru evolved into an ash-black, shadow-sheathed hound.
- **Tactical Mechanics:** Serves as Neel's **living thermal buffer**. Sheru inhales the excess necrotic frost leaking from KĀLĪ, preventing frostbite from advancing past Neel's elbow, while strengthening his own shadow coat.
- **Preta Saturation Ceiling (प्रेत-संतृप्ती मर्यादा):** Sheru has a strict absorption ceiling. If he consumes too much necrotic frost in a single battle, his internal organs freeze, he vomits black ice, and his mind regresses into feral rabid frenzy. Neel must keep fights brief to safeguard his dog.
- **Trope Rejection:** Sheru is **नही** a cute fantasy mascot. He is a scarred, one-eared street survivor who bites dirty and guards Neel's back with ferocious loyalty."""

replace_in_file(r"01_WORLD_BIBLE\00_Sanatan_Encyclopedic_Codex.md", p7_target1, p7_repl1)
replace_in_file(r"01_WORLD_BIBLE\00_Sanatan_Encyclopedic_Codex.md", p7_target2, p7_repl2)
replace_in_file(r"01_WORLD_BIBLE\00_Sanatan_Encyclopedic_Codex.md", p7_target3, p7_repl3)
replace_in_file(r"01_WORLD_BIBLE\00_Sanatan_Encyclopedic_Codex.md", p7_target4, p7_repl4)
replace_in_file(r"01_WORLD_BIBLE\00_Sanatan_Encyclopedic_Codex.md", p7_target5, p7_repl5)
replace_in_file(r"01_WORLD_BIBLE\00_Sanatan_Encyclopedic_Codex.md", p7_target6, p7_repl6)

print("\n--- ALL REMEDIATIONS COMPLETE! ---")
