file_path = r"d:\Web Novel\Brahmand\01_WORLD_BIBLE\01_Cosmology_and_The_Trinity_Mandate.md"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

import re
text = re.sub(
    r"### 2\.1 The Inquiry of Four-Headed Brahmā?\nLooking upon the architectural blueprints of the new Brahmāṇḍa, Lord Brahmā turned His four heads",
    "### 2.1 The Inquiry of Three-Headed Brahmā (त्रिमुख ब्रह्मा)\nLooking upon the architectural blueprints of the new Brahmāṇḍa, the Three-Headed Lord Brahmā turned His three heads",
    text
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 01_Cosmology_and_The_Trinity_Mandate.md successfully")
