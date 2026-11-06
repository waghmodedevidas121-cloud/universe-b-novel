import os

f1 = open("D:/Web Novel/UNIVERSE B/New/08_Character_Roster.md", encoding="utf-8").read()
with open("D:/Web Novel/UNIVERSE B/New/characters/roster.md", "w", encoding="utf-8") as f:
    f.write(f1)

print("Synchronized characters/roster.md with 08_Character_Roster.md")
