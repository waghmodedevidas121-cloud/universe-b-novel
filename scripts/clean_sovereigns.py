import sys
from pathlib import Path

fpath = Path(r"d:\Web Novel\Brahmand\03_CHARACTERS\03_Sovereigns_and_Setu_Commanders.md")
text = fpath.read_text(encoding="utf-8").replace("\r\n", "\n")

text = text.replace(
    "- **Relationship with Neel:** When rumors of Neel's cursed iron shackle (*KĀLĪ*) reach the lower realms, Bali does not send assassins. Recognizing an ancient Era 2 relic, Bali observes from afar, wondering if this mortal from Earth holds the key to purifying the severed abyss.",
    "- **Relationship with Treaty Wanderers:** When rumors of the cursed iron shackle (*KĀLĪ*) wielded by an unranked mortal reach the lower realms, Bali does not send assassins. Recognizing an ancient Era 2 relic, Bali observes from afar, wondering if this treaty soul with an unwritten destiny holds the key to purifying the severed abyss."
)

text = text.replace(
    "- **Respect for Cold Grit:** When Vajraketu scouts the Proving Games for conscripts, he ignores showy aristocrats with golden armor. He looks for fighters who survive with broken ribs and blood in their eyes—warriors like Neel.",
    "- **Respect for Cold Grit:** When Vajraketu scouts the Proving Games for conscripts, he ignores showy aristocrats with golden armor. He looks for fighters who survive with broken ribs and blood in their eyes—warriors like Aniket."
)

text = text.replace(
    "> These seven sovereigns and commanders form the macroscopic chessboard of *Brahmand*. In future story arcs, as Neel climbs the ranks of the Proving Games and unravels the mysteries of the severed Chasm, his trajectory will collide directly with their political interests and martial codes.",
    "> These seven sovereigns and commanders form the macroscopic chessboard of *Brahmand*. In future story arcs, as unranked contenders climb the ranks of the Proving Games and unravel the mysteries of the severed Chasm, their trajectory will collide directly with their political interests and martial codes."
)

fpath.write_text(text, encoding="utf-8")
print("SUCCESS: Cleaned 03_Sovereigns_and_Setu_Commanders.md")
