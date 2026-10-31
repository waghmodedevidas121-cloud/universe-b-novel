# -*- coding: utf-8 -*-
import os
import re

# File paths
p_hi = r"D:\Web Novel\UNIVERSE B\Story\18A_Season_1_Volume_1_Prologue_Hindi.md"
p_en = r"D:\Web Novel\UNIVERSE B\Story\18A_Season_1_Volume_1_Prologue.md"
ch1_hi = r"D:\Web Novel\UNIVERSE B\Story\19_Season_1_Chapter_1_Hindi.md"
ch1_en = r"D:\Web Novel\UNIVERSE B\Story\19_Season_1_Chapter_1.md"

# 1. Update Prologue Hindi numbers
with open(p_hi, "r", encoding="utf-8") as f:
    text_p_hi = f.read()

replacements_p_hi = [
    ("छह घंटे से लगातार पानी बरस रहा था।", "6 घंटे से लगातार पानी बरस रहा था।"),
    ("पिछले चालीस मिनट से यही आवाज", "पिछले 40 मिनट से यही आवाज"),
    ("कुल ग्यारह रुपये।", "कुल 11 रुपये।"),
    ("पंद्रह रुपये... या घर तक का ऑटो।", "15 रुपये... या घर तक का ऑटो।"),
    ("Neel उन्नीस साल का था।", "Neel 19 साल का था।"),
    ("करीब छह इंच गहरे गंदे पानी में", "करीब 6 इंच गहरे गंदे पानी में"),
    ("वो बस उन्नीस साल का एक लड़का था, जो कुछ मिनट पहले तक ग्यारह रुपये में", "वो बस 19 साल का एक लड़का था, जो कुछ मिनट पहले तक 11 रुपये में"),
]

for old, new in replacements_p_hi:
    text_p_hi = text_p_hi.replace(old, new)

with open(p_hi, "w", encoding="utf-8") as f:
    f.write(text_p_hi)
print("Updated Prologue Hindi numbers.")

# 2. Update Prologue English numbers
with open(p_en, "r", encoding="utf-8") as f:
    text_p_en = f.read()

replacements_p_en = [
    ("six hours straight", "6 hours straight"),
    ("past forty minutes", "past 40 minutes"),
    ("eleven rupees total", "11 rupees total"),
    ("Fifteen rupees... or an auto-rickshaw home", "15 rupees... or an auto-rickshaw home"),
    ("Neel was nineteen years old", "Neel was 19 years old"),
    ("six inches of filthy runoff", "6 inches of filthy runoff"),
    ("nineteen-year-old kid who, minutes ago, had been debating whether eleven rupees", "19-year-old kid who, minutes ago, had been debating whether 11 rupees"),
]

for old, new in replacements_p_en:
    text_p_en = text_p_en.replace(old, new)

with open(p_en, "w", encoding="utf-8") as f:
    f.write(text_p_en)
print("Updated Prologue English numbers.")

# 3. Update Chapter 1 Hindi (Scenes 1, 2 with digits, and append Scene 3)
scene3_hi = """

Neel गाड़ी के पिछले तख्ते से नीचे कीचड़ में कूद गया।

*छपाक!*

ठंडा, चिपचिपा कीचड़ सीधा उसके घुटनों तक चढ़ गया। फटे हुए स्नीकर्स के अंदर बर्फीला पानी भरते ही बदन में एक सिहरन दौड़ गई। उसने दांत भींचे और लड़खड़ाते हुए संतुलन बनाया।

"अरे ओए! Drifter!" गाड़ीवान की नजर उस पर पड़ी। "वहां क्या नौटंकी कर रहा है? दूर हट गाड़ी से!"

Neel ने उसकी बात का कोई जवाब नही दिया। उसका ध्यान सिर्फ उस 4 इंच मोटे, मजबूत ओक के लट्ठे पर था जो पहिये से 3 कदम दूर कीचड़ में दबा पड़ा था। 

उसने दोनों हाथों से लट्ठे को पकड़ा और पूरी ताकत से कीचड़ से बाहर खींच लिया। लट्ठा भारी था, गीला और फिसलन भरा, पर लकड़ी में कोई सड़न नही थी।

दादर के गैरेज में जब भी कोई भारी टैक्सी नाले में फंसती थी, काका हमेशा चिल्लाते थे—*'अरे अक्ल के अंधे, वजन उठाने के लिए ताकत नही, सही कोण चाहिए!'*

Neel ने नजर दौड़ाई। पहिये के ठीक पीछे, कीचड़ में एक चपटा भारी पत्थर धंसा हुआ था। उसने अपने पैर से उस पत्थर को धकेलकर पहिये के रिम के पास अटकाया, और लट्ठे के नुकीले सिरे को धुरे के ठीक नीचे, उस पत्थर की टेक पर फंसा दिया। 

परफेक्ट लीवर। 

गाड़ीवान चाबुक हाथ में लिए गुस्से में पीछे आया। "तुझे समझ नही आता क्या? ये 2 टन की मालगाड़ी है! तेरे जैसा सूखा डंडा इसे हिलाएगा—"

"तमाशा देखना बंद करो और आगे जाओ!" Neel ने हांफते हुए, पर तीखी आवाज में कहा। उसकी नजरें पहिये पर टिकी थीं। "जब मैं बोलूं, सांड को सीधा आगे खींचना। चाबुक मत मारना, बस लगाम सीधी रखना!"

गाड़ीवान एक पल के लिए ठिठक गया। 19 साल के उस लड़के की आंखों में जो जिद थी, वो किसी भीख मांगने वाले की नही थी। वो गाली बड़बड़ाते हुए वापस आगे की तरफ भागा।

Neel ने लट्ठे के लंबे सिरे पर अपने दोनों हाथ जमाए। 

पैर कीचड़ में फिसल रहे थे। खुद को संभालने के लिए उसने अपना बायां हाथ गाड़ी के निचले तख्ते पर टिकाया—ठीक उस जगह जहां लोहे के छल्ले से वो पिल्ला बंधा था।

अचानक पिल्ले ने झटका खाया, और Neel की हथेली अनजाने में पिल्ले के भीगे, जख्मी माथे से छू गई।

*झ़्ज़ज़ज़ज़त!*

कोई रोशनी नही चमकी। कोई धमाका नही हुआ।

पर उस 0.2 सेकंड के लिए Neel के पूरे बदन में, रीढ़ की हड्डी से लेकर सिर के पिछले हिस्से तक, 72,000 नसों में बिजली का एक बहुत बारीक, सुई जैसा कंप दौड़ गया। 

कानों के ठीक पीछे एक बेहद पतली, धातु जैसी गूंज उठी—*The Sing*।

आधे पल के लिए Neel को लगा जैसे उसका अपना दिल और उस पिल्ले के सीने की तेज धड़कन एक ही ताल पर धड़कने लगी हों। उस नन्हे जानवर के अंदर की जिद्दी आग सीधे Neel की मांसपेशियों में उतर आई। बाजुओं का सुन्नपन पल भर में गायब हो गया, और खून में एक अजीब-सी गर्म ताकत दौड़ गई।

पिल्ले की पीली आंखें चौड़ी हो गईं, पर उसने गुर्राना बंद कर दिया था।

"अब! खींचो!" Neel पूरी छाती के जोर से चीखा।

गाड़ीवान ने पूरी ताकत से सांड की लगाम आगे खींची। "चल शेरा! जोर लगा!"

Lava-Bull ने अपने काले खुर जमीन में गाड़ दिए। उसकी पीठ की नसें लोहे के तारों की तरह तन गईं।

उसी 1 सेकंड में Neel ने अपने पूरे 58 किलो वजन को उस लट्ठे के सिरे पर झोंक दिया। 

*कड़कड़ाट!*

लकड़ी का भारी लट्ठा 2 टन के दबाव से चरमरा उठा। Neel के गले और माथे की नसें फूल गईं, कीचड़ में उसके पैर 6 इंच गहरे धंस गए, पर उसने पकड़ नही छोड़ी। 

*शुलुप्पप!*

कीचड़ की वो जानलेवा पकड़ टूटी।

पहिये के नीचे हवा घुसी, और बैल के एक प्रचंड, आखिरी झटके के साथ वो 2 टन का विशाल पहिया गड्ढे से उछलकर बाहर आ गिरा!

*धड़ाम!*

गाड़ी सीधे 3 फीट आगे सरककर सूखे पत्थरों पर खड़ी हो गई।

Neel कीचड़ में घुटनों के बल गिर पड़ा। दोनों हथेलियां छिल चुकी थीं, फेफड़े धौंकनी की तरह चल रहे थे, और हाथ-पैर बुरी तरह कांप रहे थे।

पर गाड़ी दलदल से बाहर थी।
"""

with open(ch1_hi, "r", encoding="utf-8") as f:
    text_ch1_hi = f.read()

replacements_ch1_hi = [
    ("दो भारी, काले सींग।", "2 भारी, काले सींग।"),
    ("आधा सेकंड भी नही लगेगा।", "0.5 सेकंड भी नही लगेगा।"),
    ("एक सेकंड... तीन सेकंड... पाँच सेकंड।", "1 सेकंड... 3 सेकंड... 5 सेकंड।"),
    ("ग्यारह रुपये और मरा हुआ फोन", "11 रुपये और मरा हुआ फोन"),
    ("करीब आधा मील आगे", "करीब 0.5 मील आगे"),
    ("एक सौ फुट ऊंचा, काले पत्थर का", "100 फुट ऊंचा, काले पत्थर का"),
    ("ग्यारह रुपये जेब में दबाकर", "11 रुपये जेब में दबाकर"),
    ("दो टन की लकड़ी की गाड़ी", "2 टन की लकड़ी की गाड़ी"),
    ("दो Panas देकर", "2 Panas देकर"),
    ("चार इंच मोटे लकड़ी के लट्ठे पर", "4 इंच मोटे लकड़ी के लट्ठे पर"),
]

for old, new in replacements_ch1_hi:
    text_ch1_hi = text_ch1_hi.replace(old, new)

# Append Scene 3
text_ch1_hi = text_ch1_hi.rstrip() + scene3_hi

with open(ch1_hi, "w", encoding="utf-8") as f:
    f.write(text_ch1_hi)
print("Updated Chapter 1 Hindi numbers and appended Scene 3.")

# 4. Update Chapter 1 English (Scenes 1, 2 with digits, and append Scene 3)
scene3_en = """

Neel dropped down from the tailgate straight into the mire.

*SPLASH!*

Cold, viscous mud surged past his calves to his knees. Freezing slurry flooded his torn sneakers, sending a violent shudder up his spine. He ground his molars together and fought for balance.

"Hey, you! Drifter!" The carter's glare locked onto him. "What the hell do you think you're doing? Back away from my freight!"

Neel ignored him completely. His focus was locked onto a 4-inch-thick, weathered oak timber half-submerged in the slush 3 paces away.

He seized the pole with both hands and wrenched it free of the mud's suction. The timber was heavy, slick, and cold, but the grain was rock-solid.

Back in the Dadar garage, whenever a cab dropped a front wheel into an open gutter, the old mechanic would bark—*'Listen, dumbass, you don't beat dead weight with muscle; you beat it with angles!'*

Neel scanned the trench. Half-buried right behind the stuck rim was a flat, heavy slab of ballast stone. Neel kicked the stone into the clay against the iron rim, levering the tapered end of the oak spar directly beneath the axle hub against the stone pivot.

A textbook class-one lever.

The wagon master stormed back along the cart, whip raised. "Are you deaf? That's a 2-ton freight wagon! A scrawny runt with a stick isn't going to budge—"

"Stop shouting and get to the traces!" Neel snapped back between ragged breaths, his eyes glued to the hub. "When I count to three, haul the beast straight forward. Don't use the whip, just keep the reins taut!"

The teamster stopped short. The cold fury in the 19-year-old's eyes wasn't that of a beggar. Cursing under his breath, the man wheeled around and charged back toward the yoke.

Neel wrapped both hands tight around the long end of the timber spar.

His boots were losing purchase in the grease. To steady his stance, his left hand instinctively braced against the lower sideboard—right beside the iron ring where the pup was tethered.

The hound flinched, and Neel's bare palm brushed squarely against its wet, scarred forehead.

*ZZZZZT!*

No blinding flash. No thunderous burst.

Yet for that 0.2-second interval, across all 72,000 nadis running from his tailbone to the crown of his skull, a piercing, thread-thin tremor of live current zipped through his flesh.

Right behind his temples resonated a razor-sharp acoustic chime—*The Sing*.

For half a breath, Neel felt the wild flutter of the pup's heart synchronize seamlessly with his own pulse. The starving beast's ferocious, desperate will to survive poured directly into Neel's sinews. The numbness in his arms vanished, replaced by an electric surge of focused adrenaline.

The pup's amber eyes went wide, but its snarl fell completely silent.

"NOW! HEAVE!" Neel screamed with everything in his chest.

The carter hauled back on the yoke reins with all his bulk. "Pull, Shera! Pull!"

The Lava-Bull dug its basalt hooves deep into the stone bed, its spinal cord knotting like braided steel cable.

In that single 1-second window, Neel hurled all 58 kilos of his body weight down across the end of the spar.

*CRACK-GROAN!*

The heavy oak groaned under the agonizing 2-ton strain. Veins corded across Neel's neck, his sneakers sinking 6 inches deeper into the freezing sludge, but he refused to yield an inch.

*SHLUUURP!*

The mud's vacuum seal ruptured.

Air sucked beneath the iron tire, and with one monumental, shuddering heave from the horned beast, the 2-ton wheel surged up out of the pit and slammed onto the crushed gravel rim!

*THUD!*

The wagon rolled forward 3 full feet, coming to rest safely on solid stone.

Neel collapsed to his knees in the mud. The skin on both his palms was scraped raw, his lungs heaving like bellows, his limbs trembling violently from exhaustion.

But the wagon was free.
"""

with open(ch1_en, "r", encoding="utf-8") as f:
    text_ch1_en = f.read()

replacements_ch1_en = [
    ("Two massive, pitch-black horns.", "2 massive, pitch-black horns."),
    ("less than half a second.", "less than 0.5 seconds."),
    ("One second... three seconds... five seconds.", "1 second... 3 seconds... 5 seconds."),
    ("Eleven rupees and a dead phone", "11 rupees and a dead phone"),
    ("roughly half a mile ahead", "roughly 0.5 miles ahead"),
    ("stood a hundred-foot-tall gate", "stood a 100-foot-tall gate"),
    ("with eleven rupees squeezed", "with 11 rupees squeezed"),
    ("two-ton timber wagon", "2-ton timber wagon"),
    ("Paid two Panas", "Paid 2 Panas"),
    ("stout, four-inch-thick timber lever", "stout, 4-inch-thick timber lever"),
]

for old, new in replacements_ch1_en:
    text_ch1_en = text_ch1_en.replace(old, new)

# Append Scene 3
text_ch1_en = text_ch1_en.rstrip() + scene3_en

with open(ch1_en, "w", encoding="utf-8") as f:
    f.write(text_ch1_en)
print("Updated Chapter 1 English numbers and appended Scene 3.")
