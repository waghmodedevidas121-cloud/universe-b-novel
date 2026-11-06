import re

path = r'd:\Web Novel\UNIVERSE B\New\08_Character_Roster.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Beatrice Rosso -> Beatrice Vanezza
text = text.replace('Donna Beatrice Rosso (डोना बीट्राइस रोसो)', 'Donna Beatrice Vanezza (डोना बीट्राइस व्हेनेझ्झा)')
text = text.replace('Donna Beatrice Rosso', 'Donna Beatrice Vanezza')
text = text.replace('Rosso Family', 'Vanezza Dynasty')
text = text.replace('Rosso घराणे', 'Vanezza घराणे')

# 2. Update Deva entries
text = text.replace('### [CHR-DEV-01] Bhanu (भानू) - The Solar Sovereign', '### [CHR-DEV-01] Aryaman (अर्यमन्) - Solar Emperor of Amaravati')
text = text.replace('Bhanu (भानू)', 'Aryaman (अर्यमन्)')
text = text.replace('### [CHR-DEV-02] Queen Savitri (राणी सावित्री) - Keeper of the Solar Purse', '### [CHR-DEV-02] Saranya (सरन्यू) - High Empress of Amaravati')
text = text.replace('Queen Savitri (राणी सावित्री)', 'Saranya (सरन्यू)')
text = text.replace('### [CHR-DEV-03] Vaijayanti (वैजयंती) - Sky-Marshal of the Golden Wings', '### [CHR-DEV-03] Marisha (मारिषा) - Supreme Aerial Commander')
text = text.replace('Vaijayanti (वैजयंती)', 'Marisha (मारिषा)')
text = text.replace('### [CHR-DEV-04] Anshuman (अंशुमान) - Captain of the Sun-Lances', '### [CHR-DEV-04] Kiran (किरण) - Captain of the Sun-Lances')
text = text.replace('Anshuman (अंशुमान)', 'Kiran (किरण)')
text = text.replace('### [CHR-DEV-05] Justice Dharma (न्यायाधीश धर्म) - The Blind Arbiter', '### [CHR-DEV-05] Ritam (ऋतम्) - Chief Justice of Amaravati')
text = text.replace('Justice Dharma (न्यायाधीश धर्म)', 'Ritam (ऋतम्)')
text = text.replace('### [CHR-DEV-06] Revati (रेवती) - Seer of the Star-Tides', '### [CHR-DEV-06] Saumya (सौम्या) - High Priestess & Astral Seer')
text = text.replace('Revati (रेवती)', 'Saumya (सौम्या)')
text = text.replace('### [CHR-DEV-07] Lady Chitralekha (चित्रलेखा) - Mistress of Gandharva-Puri', '### [CHR-DEV-07] Chitralekha (चित्रलेखा) - Silk Queen of Gandharva-Puri')
text = text.replace('### [CHR-DEV-08] Kavi (कवी) - Master of the Silk-Looms', '### [CHR-DEV-08] Kaleyan (कालेयन्) - Master Silk-Weaver')
text = text.replace('Kavi (कवी)', 'Kaleyan (कालेयन्)')
text = text.replace('### [CHR-DEV-09] Chitraratha (चित्ररथ) - Navigator of the Void-Rim', '### [CHR-DEV-09] Taran (तारण) - Chief Void Cartographer')
text = text.replace('Chitraratha (चित्ररथ)', 'Taran (तारण)')
text = text.replace('### [CHR-DEV-10] Marut (मरुत) - The Wind-Runner', '### [CHR-DEV-10] Javan (जवन) - Supersonic Royal Courier')
text = text.replace('Marut (मरुत)', 'Javan (जवन)')

# 3. Update Beast entries
text = text.replace('### [CHR-BST-01] Ursus (उर्सुस) - "Old Four-Horns"', '### [CHR-BST-01] Rikshan (ऋक्षन्) - Bear Sovereign')
text = text.replace('Ursus (उर्सुस)', 'Rikshan (ऋक्षन्)')
text = text.replace('### [CHR-BST-02] Jormun (जॉरमुन) - "The Jade Coil"', '### [CHR-BST-02] Kadrin (काद्रिन्) - Empress of Serpents')
text = text.replace('Jormun (जॉरमुन)', 'Kadrin (काद्रिन्)')
text = text.replace('### [CHR-BST-03] Vinata (विनता) - "The Golden Maw"', '### [CHR-BST-03] Suparni (सुपर्णी) - Garuda Empress')
text = text.replace('Vinata (विनता)', 'Suparni (सुपर्णी)')
text = text.replace('### [CHR-BST-04] Sampati (संपाती) - "Iron-Talon"', '### [CHR-BST-04] Shyen (श्येन) - Garuda War-Prince')
text = text.replace('Sampati (संपाती)', 'Shyen (श्येन)')
text = text.replace('### [CHR-BST-05] Shyama (श्यामा) - "The Shadow-Cat"', '### [CHR-BST-05] Nishi (निशि) - Panther Matriarch')
text = text.replace('Shyama (श्यामा)', 'Nishi (निशि)')
text = text.replace('### [CHR-BST-06] Sarama (सरमा) - "Queen of Blood-Ridge"', '### [CHR-BST-06] Sarami (सारमी) - Sabertooth Pack Queen')
text = text.replace('Sarama (सरमा)', 'Sarami (सारमी)')
text = text.replace('### [CHR-BST-07] Morvath (मोर्व्हाथ) - "The Bone-Speaker"', '### [CHR-BST-07] Murva (मूर्वा) - Forest Hermit & Shaman')
text = text.replace('Morvath (मोर्व्हाथ)', 'Murva (मूर्वा)')
text = text.replace('### [CHR-BST-08] Sage Matanga (ऋषी मतंग) - Keeper of the Silent Glade', '### [CHR-BST-08] Matang (मतंग) - Sanctuary Sage')
text = text.replace('### [CHR-BST-09] Tara (तारा / Maya-Ri) - "The Silent Whisperer"', '### [CHR-BST-09] Tara (तारा) - Forest Scout')

# 4. Schwa-deletion cleanups
text = text.replace('Ugrasena (सेनापती उग्रसेन)', 'Ugrasen (सेनापती उग्रसेन)')
text = text.replace('General Ugrasena', 'General Ugrasen')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated 08_Character_Roster.md successfully!")
