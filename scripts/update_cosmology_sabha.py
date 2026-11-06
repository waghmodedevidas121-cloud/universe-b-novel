import re
from pathlib import Path

cosmo_file = Path(r"d:\Web Novel\Brahmand\01_WORLD_BIBLE\01_Cosmology_and_The_Trinity_Mandate.md")
content = cosmo_file.read_text(encoding="utf-8")

target = """### 1.1 The Nature of Universe B (Brahmand)
In the mainstream sacred multiverse (*Universe A*), whenever Dharma declines and Adharma runs rampant, the Supreme Preserver directly descends in physical form:
> *"Yadā yadā hi dharmasya glānir bhavati bhārata..."*  
> *(Whenever righteousness declines, I manifest Myself as an Avatāra to protect the virtuous and destroy the wicked.)*

However, **Brahmand (Universe B)** was engineered under a radically different, historic divine mandate. It is not an accidental universe; it is a **Deliberate Cosmic Crucible (स्वकर्तृत्व परीक्षा — The Crucible of Puruṣārtha)**."""

repl = """### 1.1 The Nature of Universe B (Brahmand)
In the mainstream sacred multiverse (*Universe A*), whenever Dharma declines and Adharma runs rampant, the Supreme Preserver directly descends in physical form:
> *"Yadā yadā hi dharmasya glānir bhavati bhārata..."*  
> *(Whenever righteousness declines, I manifest Myself as an Avatāra to protect the virtuous and destroy the wicked.)*

However, **Brahmand (Universe B)** was engineered under a radically different, historic divine mandate. It is not an accidental universe; it is a **Deliberate Cosmic Crucible (स्वकर्तृत्व परीक्षा — The Crucible of Puruṣārtha)**.

### 1.2 The Śvāsōcchvāsa Cakra Offset & The Brahmāṇḍa Sabhā
Our cosmos is separated from the mainstream four-headed universe by several complete **Mahā-Viṣṇu Breath Cycles (श्वासोच्छ्वास चक्रे — Brahma-Saṁhitā 5.48)**. Within this specific breath stream, the **Brahmāṇḍa Sabhā (Council of Multiverses — Caitanya-Caritāmṛta Madhya 21)** deliberated on systemic cosmic stagnation. 

While some universes adhered to the rigid baseline template, our 3-Headed Cosmos was commissioned as an **Evolving Cosmos (एक विकसनशील ब्रह्मांड)** governed by:
1. **The Trimūrti Zero-Avatar Mandate** (Mortal self-reliance over divine crutches).
2. **Dynamic Evolution & Moral Realism** (Dharma, Adharma, Ahaṅkāra, Namratā, and moral grey dilemmas teaching wisdom through action and consequence).
3. **The Vidhātā Inter-Brahmāṇḍa Treaty** (Trans-cosmic soul incarnation with `[STATUS: RIKTA / UNWRITTEN]` destiny and ancient Rinānubandha resonance; see full codex in [06_Inter_Brahmanda_Soul_Administration_and_Treaty.md](file:///d:/Web%20Novel/Brahmand/01_WORLD_BIBLE/06_Inter_Brahmanda_Soul_Administration_and_Treaty.md))."""

normalized = content.replace("\r\n", "\n")
assert target in normalized, "Target not found"
updated = normalized.replace(target, repl)
cosmo_file.write_text(updated, encoding="utf-8")
print("Successfully updated Cosmology with Brahmāṇḍa Sabhā and Treaty references!")
