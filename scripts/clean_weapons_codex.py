import sys
from pathlib import Path

fpath = Path(r"d:\Web Novel\Brahmand\02_POWER_SYSTEM\02_Elements_Preta_and_Cursed_Weapons.md")
text = fpath.read_text(encoding="utf-8").replace("\r\n", "\n")

# Replace Section 4 title and box
text = text.replace(
    "## 4. Master Dossier: KĀLĪ (काली — The Spiked Iron Shackle)",
    "## 4. Master Classification: Śāpita Śastra (शापित शस्त्र — Corrupted Abyssal Chains of Era 2)"
)

text = text.replace(
    "WEAPON DOSSIER: KĀLĪ (काली)",
    "METAPHYSICAL DOSSIER: ABYSSAL SHAAPIT SHASTRA (शापित शस्त्र)"
)

text = text.replace(
    "• Primary Carrier: Bound to the Wielder's Left Forearm & Wrist",
    "• Primary Deployment: Bound to a Mortal Warrior's Forearm or Carried via Bandolier"
)

text = text.replace(
    "• Sub-Entity Resonance: Symbiotic Conduit with Kuro/Sheru (Shadow Hound)",
    "• Sub-Entity Resonance: Symbiotic Thermal Radiator via Companion Beast (Shadow Hound)"
)

text = text.replace(
    "[ VISUAL ANATOMY OF KĀLĪ: THE SPIKED SHACKLE ]",
    "[ ANATOMY OF AN ABYSSAL EXECUTIONER CHAIN ]"
)

text = text.replace(
    "2. **Kuro's Thermal Buffering & Preta Saturation Ceiling (प्रेत-संतृप्ती मर्यादा):**\n"
    "   A companion beast (such as a loyal shadow-hound) acts as an external soul-radiator, consuming excess necrotic frost leaking from KĀLĪ to prevent frostbite advancing past the wielder's elbow.\n"
    "   - *The Anti-Buff Ceiling:* Kuro does **नही** enjoy an infinite power buff. He has a strict **Preta Saturation Ceiling**. If Kuro absorbs too much sub-zero miasma in a single engagement, his internal organs begin to freeze, he vomits black ice, and his mind regresses into feral, rabid bloodlust where the hound snaps indiscriminately. This physiological limit forces the wielder to strictly ration KĀLĪ's deployment to short, decisive bursts.",
    "2. **Companion Beast Thermal Buffering & Preta Saturation Ceiling (प्रेत-संतृप्ती मर्यादा):**\n"
    "   A bonded companion beast (such as an ancient shadow-hound / Kṛṣṇa-Śārameya) can serve as an external soul-radiator, absorbing excess necrotic frost leaking from cursed iron relics to prevent frostbite from advancing past the warrior's elbow.\n"
    "   - *The Anti-Buff Ceiling:* The beast does **नही** possess infinite absorption capacity. It is bound by a strict **Preta Saturation Ceiling**. If the hound absorbs too much sub-zero miasma in a single battle, its internal organs begin to freeze, it vomits black ice, and its consciousness regresses into feral, rabid bloodlust. This physiological ceiling forces the warrior to strictly ration the relic's deployment to short, decisive tactical strikes."
)

fpath.write_text(text, encoding="utf-8")
print("SUCCESS: Cleaned 02_Elements_Preta_and_Cursed_Weapons.md!")
