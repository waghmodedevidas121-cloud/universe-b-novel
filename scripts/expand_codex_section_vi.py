import sys
from pathlib import Path

codex_path = Path(r"d:\Web Novel\Brahmand\01_WORLD_BIBLE\00_Sanatan_Encyclopedic_Codex.md")
text = codex_path.read_text(encoding="utf-8").replace("\r\n", "\n")

# 1. Update Sheru etymology
target_sheru = "*Sheru* (शेर — lion-hearted, street mongrel name from Mumbai); *Kuro* (कृष्ण / काळा — shadow-black, darkened mantle)."
repl_sheru = "*Sheru* (शूर / शेर — bold, lion-hearted steadfast companion); *Kṛṣṇa-Śārameya* (कृष्ण-शारमेय — sacred black hound of celestial/karmic lineage)."

assert target_sheru in text, "target_sheru missing"
text = text.replace(target_sheru, repl_sheru)

# 2. Add Section VI: Inter-Brahmāṇḍa Soul Treaty & Multiverse Architecture
section_vi = """
# SECTION VI: INTER-BRAHMĀṆḌA TREATY & MULTIVERSE METAPHYSICS (आंतर-ब्रह्मांड संविद व आत्मा-प्रशासन)

---

### 34. Śvāsōcchvāsa Cakra (श्वासोच्छ्वास चक्र — The Cosmic Breath Cycles)
- **Etymology & Root:** *Śvāsa* (श्वस् — inhalation) + *Ucchvāsa* (उद् + श्वस् — exhalation) + *Cakra* (चक्र — recurring cyclic wheel).
- **Scriptural Authority:** *Brahma-Saṁhitā* 5.48; *Śrīmad Bhāgavata Purāṇa* 2.5.33, 3.11.38.
- **Classical Definition:** The cosmic breathing cycle of Kāraṇodakaśāyī Mahā-Viṣṇu in the Causal Ocean. Trillions of spherical Brahmāṇḍas emerge with His exhalation and dissolve back with His inhalation over 100 Brahmā years.
- **Novel Context & Adaptation:** In *Brahmand — The 3-Headed Cosmos*, our universe exists separated from the mainstream four-headed universe by several complete Mahā-Viṣṇu breath cycles. This temporal and dimensional offset allows for specialized physical and karmic properties distinct from the mainstream baseline.
- **Tactical Mechanics:** Navigating between breath cycles is beyond the power of Devas or mortals; only supreme cosmic ordinances and high-level soul administration treaties can facilitate trans-breath soul migration.
- **Trope Rejection:** Cosmic breath cycles are **नही** random multiverse parallel dimensions or video-game servers. They represent the breathing of the Supreme Singularity.

---

### 35. Brahmāṇḍa Sabhā (ब्रह्मांड सभा — The Council of Multiverses)
- **Etymology & Root:** *Brahmāṇḍa* (ब्रह्मांड — universe) + *Sabhā* (सभा — supreme deliberative assembly, council of elders/rulers).
- **Scriptural Authority:** *Śrīmad Bhāgavata Purāṇa* 10.14; *Śrī Caitanya-Caritāmṛta* Madhya-līlā 21.55–90 (Assembly of multi-headed Brahmas).
- **Classical Definition:** The transcendental assembly where the presiding Brahmas, Prajāpatis, and administrators of diverse material universes convene under the divine will of the Supreme Lord to coordinate cosmic order (*Ṛta*).
- **Novel Context & Adaptation:** The council that deliberated on universal governance within our breath stream. While some universes retained the standard 4-headed baseline, our 3-Headed Cosmos was commissioned as an Evolving Crucible (*Puruṣārtha-Parīkṣā*) governed by dynamic morality and mortal self-reliance.
- **Tactical Mechanics:** The resolutions of the Brahmāṇḍa Sabhā carry the weight of absolute cosmic law across all fourteen realms within the participating universes.
- **Trope Rejection:** The Sabhā is **नही** a galactic UN or a sci-fi space federation. It is a sacred metaphysical assembly of cosmic creators and Upādhi-holders.

---

### 36. Vidhātā-Saṁvid (विधाता-संविद — Inter-Brahmāṇḍa Soul Administration Treaty)
- **Etymology & Root:** *Vidhātā* (विधातृ — the divine dispenser of fate and rebirth) + *Saṁvid* (संविद् — formal treaty, inviolable multilateral compact).
- **Scriptural Authority:** *Śukranīti*; *Manusmṛti* 7; *Kāmandakīya Nītisāra* (Principles of treaty and sovereign agreements).
- **Classical Definition:** A binding administrative agreement executed between cosmic offices governing the flow, legal status, and transmigration of souls.
- **Novel Context & Adaptation:** The formal covenant signed by the Office of Vidhātā and Citragupta with allied Soul Administration Offices of other Brahmāṇḍas. Under this treaty, souls are incarnated into *Brahmand* to resolve deep karmic logjams, receiving certified Soul IDs in the Agra-Sandhānī ledger.
- **Tactical Mechanics:** Transferred souls enter with zero foreign technology (which dissolves at the Kṣīra Sāgara boundary). They enter mortal wombs with clean physical vessels, retaining only their unwritten causal potential.
- **Trope Rejection:** The Vidhātā Treaty is **नही** a cheat-skill reincarnation truck trope. It is a rigorous, demanding karmic transfer governed by cosmic legal codes.

---

### 37. RIKTA-Prārabdha (रिक्त-प्रारब्ध — The Unwritten Destiny Clause)
- **Etymology & Root:** *Rikta* (रिच् — vacant, blank, unwritten, void of pre-inscribed text) + *Prārabdha* (प्र + आ + रभ् — karma commenced, active life-script).
- **Scriptural Authority:** *Yoga Vāsiṣṭha* 2.4–9 (Exaltation of Puruṣārtha over Daiva/Fate); *Bhagavad Gītā* 6.5 (*"Uddhared ātmanātmānaṁ..."*).
- **Classical Definition:** The portion of karmic destiny that is left intentionally unallocated, allowing the soul's current free will and self-effort (*Puruṣārtha*) to dictate outcomes.
- **Novel Context & Adaptation:** The legal status assigned to powerful covenant and catalyst souls under the Vidhātā Treaty (`[STATUS: RIKTA / UNWRITTEN]`). Their life-script is 50% to 100% unwritten.
- **Tactical Mechanics:** A warrior with a RIKTA status cannot rely on astrological favor or predestined victory. If they surrender to Ahaṅkāra (pride), they fall; if they practice rigorous Tapasyā and tactical discipline, they can overturn overwhelming odds.
- **Trope Rejection:** A RIKTA destiny is **नही** an invincible cheat power. It is an excruciating burden of absolute moral and martial accountability.

---

### 38. Rinānubandha (ऋणानुबंध — Trans-Cosmic Karmic Cords)
- **Etymology & Root:** *Ṛṇa* (ऋण — debt, obligation, unfulfilled transaction) + *Anubandha* (अनु + बंध् — binding connection, unbroken attachment).
- **Scriptural Authority:** *Garuḍa Purāṇa* 2.2; *Śrīmad Bhāgavata Purāṇa* 6.16.
- **Classical Definition:** The subtle, indestructible karmic debts of love, loyalty, hostility, or betrayal formed across prior incarnations that compel souls to be reborn in mutual proximity.
- **Novel Context & Adaptation:** Under the Vidhātā Treaty, when a catalyst soul crosses universal boundaries, souls bound to them by intense Rinānubandha are pulled along the causal slipstream into the same realm. Companions (like Aniket and Śerū) and deadly rivals are inexorably drawn together in Central City.
- **Tactical Mechanics:** Rinānubandha cannot be broken by distance or physical walls. It manifests as instinctive trust, unyielding animal loyalty, or unavoidable tactical confrontations.
- **Trope Rejection:** Rinānubandha is **नही** a generic "telepathic pet bond" or "tamed monster link." It is an ancient, two-way karmic debt requiring mutual sacrifice.
"""

target_end = """> [!IMPORTANT]
> **Definitive Lexicon Lock:**  
> All 33 entries in this Codex are certified authentic, scripturally grounded in Sanatan Shastras, fully audited to contain **zero occurrences of nahi with bindi (all 'नही')**, and provide the immutable scholastic bedrock for all future prose in *Brahmand — The 3-Headed Cosmos*."""

repl_end = section_vi + """
---

> [!IMPORTANT]
> **Definitive Lexicon Lock:**  
> All 38 entries in this Codex are certified authentic, scripturally grounded in Sanatan Shastras, fully audited to contain **zero occurrences of nahi with bindi (all 'नही')**, and provide the immutable scholastic bedrock for all future prose in *Brahmand — The 3-Headed Cosmos*."""

assert target_end in text, "target_end missing"
text = text.replace(target_end, repl_end)

codex_path.write_text(text, encoding="utf-8")
print("SUCCESS: 00_Sanatan_Encyclopedic_Codex.md expanded to 38 entries!")
