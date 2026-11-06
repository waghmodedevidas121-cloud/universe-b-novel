# -*- coding: utf-8 -*-
import os
import re

hi_path = r"D:\Web Novel\UNIVERSE B\Story\19_Season_1_Chapter_1_Hindi.md"
en_path = r"D:\Web Novel\UNIVERSE B\Story\19_Season_1_Chapter_1.md"

# 1. Update Hindi Scene 2
with open(hi_path, "r", encoding="utf-8") as f:
    hi_content = f.read()

# Target start of Scene 2: from line with "चल," Neel ने बैग कंधे पर
split_marker_hi = 'Neel ने सूखी रोटी चबाई। ठंडी और बेस्वाद, पर उस वक्त वो किसी दावत से कम नही लगी।'

if split_marker_hi not in hi_content:
    print("ERROR: split_marker_hi not found!")
    exit(1)

scene1_hi, old_scene2_hi = hi_content.split(split_marker_hi, 1)

new_scene2_hi = """

"चल," Neel ने बैग कंधे पर टांगते हुए कहा। "अब जरा देखूं कि इस दुनिया का मेन गेट किधर है—"

उसका फटा स्नीकर जैसे ही गाड़ी के निचले पायदान पर पड़ा, उसका दायां हाथ अनजाने में पिल्ले के सिर पर टिक गया।

*ZZZZZT!*

जैसे किसी खुले स्विच बोर्ड में अचानक उंगली छू गई हो—हथेली और काले रोएं के बीच करंट का एक तीखा झटका लगा।

Neel के हाथों में जो सुन्न करने वाली खुजली मची थी, वो एक झटके में शोले की तरह भड़क उठी। पिल्ले के माथे पर एक पतली नीली चिंगारी नाची, और उस झटके से जानवर के जबड़े भींच गए। उसने घबराकर अपनी गर्दन पीछे खींची—

*तड़क!*

सड़ी हुई रस्सी बीच से टूट गई, और पिल्ला झटके से आजाद हो गया।

उसी एक पल में दूर का सारा शोर Neel के दिमाग से गायब हो गया।

*धक। धक। धक।*

उसका दिल और पिल्ले के सीने की धड़कन दोनों एक ही ताल पर आ गए। आधे सेकंड के लिए Neel को पिल्ले के पिछले पैर की पुरानी चोट की टीस अपने बदन में महसूस हुई, और पिल्ले ने जैसे Neel के सिर का वो भारी दर्द भांप लिया।

दोनों की सांसें एक हो गईं।

"ये क्या बवाल है..." Neel ने हाथ पीछे खींचकर हथेली देखी। चमड़ी के नीचे एक नीली जालीदार रेखा चमकी और फिर नस में समा गई।

पिल्ला अब बिल्कुल शांत था। वो आगे बढ़ा, Neel की गीली जींस को सूंघा, और अपना जख्मी माथा धीरे से उसकी पिंडली से टिका दिया। वो गर्म, मासूम सा स्पर्श... Neel के सीने का सारा तनाव पल भर में ढीला पड़ गया।

तभी पुआल पर एक भारी परछाई गिरी और सारी रोशनी निगल गई।

गाड़ी के पिछले तख्ते पर एक आदमी खड़ा था। नाटा, चौड़ा, जैसे किसी ने भारी ओक का दरवाजा उखाड़कर कीचड़ में खड़ा कर दिया हो। उसका चमड़े का एप्रन पेट के उभार में ढल चुका था, और कमर में खुफिया छुरी की तरह एक चिरी हुई गिनती-लकड़ी ठुसी हुई थी। हाथ में मिट्टी का कुल्हड़ था, और वो किसी ऐसे आदमी की बेरहम सब्र से मुंह चला रहा था जिसने तीस साल से एक ही नाश्ता चबाया हो।

"जाग गया," आदमी ने सपाट आवाज में कहा। "अच्छा हुआ। लाश का टोल बच गया।"

Neel का गला सूखा था। "कहाँ... कहाँ हूँ मैं?"

"South Flats. Staging Ground ग्यारह।" गाड़ीवान ने ठुड्डी से दूर इशारा किया, बिना उस तरफ देखे। "शहर उस फाटक के पार है। तू बाहर है। तेरी औकात इतनी ही है, और ये मेरा सिरदर्द नही।"

"और आप कौन हैं?"

"उस गाड़ी का मालिक जिस पर तू खून बहा रहा था।" उसने कुल्हड़ से घूंट भरा। "तू पूर्वी चौकी के पास नाले में मुंह के बल पड़ा कीचड़ पी रहा था। नाले में लावारिस लाश मिल जाए तो चार Panas जुर्माना और इंस्पेक्टर के साथ पूरी सुबह की मगजमारी। इसलिए तुझे पुआल में फेंक दिया। अब शुक्रिया बोल और कट ले।"

Neel ने सिर के पीछे हाथ फेरा। खून नही था, बस वो चुभती हुई भारी दर्द वही थी। "मैं कितनी देर बेहोश रहा?"

"दो घंटी। तीन गिन ले, अगर वो वक्त भी जोड़ना है जो तूने पुआल में हवा से बड़बड़ाते हुए काटा।" आदमी की नजर उसके कपड़ों पर टिकी—जींस, भीगे स्नीकर्स, और गले में लटकता नीला कॉलेज कार्ड। "Drifter।"

लहजे में कोई हैरानी नही थी, बस वही बेपरवाही थी जो सड़क पर किसी लावारिस कुत्ते को देखकर होती है।

"तू कहीं से भी टपका हो," वो आगे बोला। "तेरे पास कोई मोहर नही है, कोई कागज नही, कोई गिल्ड टैग नही। पीछे कोई ऐसा माई का लाल नही जो आकर कहे कि तू उसका आदमी है। कभी-कभार ऐसे नमूने गिरते हैं। गेट के क्लर्क के पास ऐसे कचरे के लिए एक ही नाम है—unindexed।"

*unindexed। न कोई रिकॉर्ड, न कोई पहचान। मतलब इस दुनिया के लिए मेरा कोई वजूद ही नही।*

"मुझे उस शहर के अंदर जाना है," Neel ने दूर प्राचीर की तरफ देखकर कहा।

"तो तीन तांबे के Panas निकाल।"

"तीन Panas?"

"तीन। यही सरकारी टोल है। किसान हो, ठेलेवाला हो या कोई बड़ा व्यापारी—जिसके पास पीतल का गिल्ड पास नही, वो तीन देगा।" आदमी ने कुल्हड़ घुमाया। "और हां, मैं तुझे एक फूटी कौड़ी उधार नही देने वाला। उन्नीस साल से इस सड़क पर माल ढो रहा हूँ, आज तक किसी बेनाम भिखारी से पैसा वसूल नही हुआ।"

"और अगर मैं बिना पैसे के सीधे गेट की तरफ चला जाऊँ तो?"

"तो क्लर्क हाथ फैलाएगा। तू खाली जेब दिखाएगा। वो बस एक सीटी बजाएगा, और पहरेदारों के दो भाले तुझे घसीटकर दाईं तरफ फेंक देंगे।" गाड़ीवान ने ठुड्डी से दूर की बाड़ की तरफ इशारा किया। "वहाँ कीचड़ का एक बाड़ा है। सिर पर कोई छत नही, एक ही खंभे से तीस आदमी बंधे रहते हैं। दोपहर तक हाथ में हथौड़ा थमाकर South Trench में उतार देंगे—दिन भर उस दीवार से नमक-घास की जहरीली जड़ें खुरचते रहो, जो अगली सुबह फिर उग आती हैं।"

"और अगर कोई काम करने से मना कर दे?"

"तो उसे दूसरे दरवाजे से धकेल देते हैं। Sand-Pits। खून का बाजार।" उसके होठों पर एक कड़वी हंसी खिंची। "सस्ते लड़ाके, सस्ती मौतें, और जो शाम तक जिंदा बच जाए उसके लिए कुछ तांबे के सिक्के। दोनों ही रास्तों में कोई अपने पूरे दांत बचाकर बाहर नही निकलता।"

Neel ने अपने हाथ देखे। पतली उंगलियां, कलम की स्याही के पुराने निशान, और खुरचे हुए पोर। ये हाथ पिछले तीन साल से सिर्फ किताबें और सस्ते मोबाइल पकड़ते आए थे, कभी जिंदगी बचाने के लिए किसी से भिड़े नही थे।

*तीन Panas। या तो दिन भर की रोटी और सिर छुपाने की जगह, या फिर शहर का एंट्री पास। दोनों का जुगाड़ नामुमकिन है।*

मुंबई की वही पुरानी तंगी यहाँ भी उसका पीछा नही छोड़ रही थी।

"लड़के।" गाड़ीवान ने आवाज दी।

"क्या?"

"कुत्ता।"

Neel ने नीचे देखा। वो पिल्ला अब भी उसकी पिंडली से चिपका हुआ था, एक कान तानकर गाड़ीवान को ऐसी नफरत से घूर रहा था जैसे कोई पुराना बैरी हो।

"वो मेरा नही है," Neel ने कहा।

"कागज पर मेरा है। Caldera के एक ढुलैये से दो Panas में रस्सी समेत खरीदा था।" आदमी ने चिढ़कर सिर हिलाया। "जिंदगी के सबसे फालतू दो सिक्के। न गाड़ी खींचता है, न पहरा देता है, और न कुछ ऐसा खाता है जो पहले से मरा हुआ न हो। सोचा था गेट पार करते वक्त बाड़े में फेंक दूंगा और रस्सी किसी को एक Masha में बेच दूंगा।"

Neel ने जमीन पर पड़ी दो टुकड़ों वाली रस्सी देखी। "रस्सी तो टूट चुकी।"

"देख रहा हूँ।" गाड़ीवान की आंखें पहले रस्सी पर गईं, फिर पिल्ले के चेहरे पर, और आखिर में Neel के दाएं हाथ पर। उसकी सपाट आंखों में एक पल के लिए भारी संदेह चमका। "तूने तोड़ी?"

"अपने आप टूटी। सड़ी हुई थी।"

"हूँ..." उसने कुल्हड़ गाड़ी के तख्ते पर रखा और Neel के हाथ को गौर से देखा। उन्नीस साल जानवरों के बीच रहने वाले आदमी की नजर बहुत तेज होती है। "तेरी उंगलियों में से गुनगुनाहट की आवाज आ रही है, Drifter। मुझे यहाँ तक साफ सुनाई दे रही है।"

Neel ने मुट्ठी भींच ली। कलाई से लेकर छोटी उंगली तक वही पतली, गर्म खिंचाव की लकीर अब भी धड़क रही थी।

"वो... वो static electricity है," उसने बात बनाई।

"static कभी गुनगुनाती नही।" गाड़ीवान दो कदम पीछे हटा और गाड़ी के पहिये से पूरा फासला बना लिया। "मैं उस दीवार के बनने से पहले से runic माल ढो रहा हूँ। अपनी मनहूस उंगलियां मेरे बैल से दूर ही रखना।"

वो मुड़ा और Staging Ground के शोर में गायब हो गया।

क्योंकि अब पूरा पड़ाव जाग चुका था।

सैकड़ों गाड़ियां नाक-से-पूंछ तक लंबी कतारों में फंसी थीं। पहियों के नीचे भारी रोड़े ठुसे थे और धुरियों पर इतना काला ग्रीस लगा था कि नीचे की कीचड़ में चमक रहा था। उनके बीच तरह-तरह के जानवर बंधे थे—सिर्फ वो बेसाल्ट जैसे काले Lava-Bull ही नही, बल्कि धारीदार खाल वाले तेज जानवर और एक भारी-भरकम स्लेटी सांड जिसके गाल से मुड़ा हुआ सींग बाहर निकला हुआ था।

बदबू परतों में आ रही थी—भीगी खाल, लोहारों की भट्टियों का तपता लोहा, सड़ा हुआ दलिया, और जानवरों की लीद। प्राचीर से सींग बजा—दो छोटे, एक लंबा। मुनादी वाले चबूतरे पर खड़े होकर तख्ती से नाम चिल्ला रहे थे और गाड़ीवान पैसों के हिसाब पर एक-दूसरे की छाती पर चढ़ रहे थे। पहियों के बीच से बच्चे चपटी टोकरियां लेकर लीद बटोरने के लिए दौड़ रहे थे ताकि कोई दूसरा बच्चा पहले न उठा ले।

और गाड़ियों के उस पार, कमजोर आदमियों की एक लंबी कतार चुपचाप खड़ी थी, जिन्हें एक ओवरसियर छड़ी से गिन रहा था। बावन... तिरपन...

पूरे मैदान में एक भी आदमी ऊपर नही देख रहा था।

Neel ने नजर उठाई।

सामने आधा मील दूर, कोहरे के उस पार Central City की वो विशाल सफेद प्राचीर फैली थी। और उसके ऊपर सिर्फ धूसर, सर्द आसमान था—जहाँ न कोई सूरज था, न कोई पंछी।

"घूर मत।"

Neel मुड़ा। वो गाड़ीवान दस कदम दूर खड़ा था।

"पहली बार आने वाले ऐसे ही घूरते हैं, फिर उनका दिमाग सटक जाता है और हफ्ते भर कांपते रहते हैं। जमीन देख और चल।"

"ये जगह आखिर है क्या?" Neel की आवाज खुद उसे बहुत छोटी लगी।

गाड़ीवान ने उसे एक सर्द नजर से देखा। "Central City। पांचों Shards का चौराहा। तीसरी घंटी पर फाटक खुलेगा। अगर तब तक कीचड़ में खड़ा रहा, तो पूरी उम्र यहीं कट जाएगी।"

*ढूँऽऽऽऽऽऽऽण!*

पहली घंटी बज उठी।

Neel के दांत बज गए। पूरी कतार की गाड़ियां कांप उठीं, और सैकड़ों बैलों के झुंड एक साथ जागकर आगे की तरफ जोर लगाने लगे।

फिर दूसरी घंटी बजी।

और आखिर में, बहुत दूर से, तीसरी घंटी का गूंजता हुआ नाद आया।

Neel फाटक की तरफ मुड़ा।

आधा मील आगे, दो मील लंबी सफेद प्राचीर के बीच, काले बेसाल्ट पत्थर से तराशा गया सौ फीट ऊंचा दरवाजा धीरे-धीरे खुल रहा था। उसके बीच से नीली Aether-mist का एक चमकदार गलियारा बह रहा था। Western Caldera की गाड़ियां और हथियारबंद लोग सुबह के Muhurta window में धीरे-धीरे आगे सरक रहे थे।

दरवाजे की मेहराब पर बड़े अक्षरों में तराशा हुआ नाम Neel साफ पढ़ सकता था:

**CENTRAL CITY — THE CROSSROADS OF THE FIVE SHARDS.**

Neel ने बुझा हुआ फोन जैकेट की अंदरूनी जेब में गहरा खिसकाया। भीगे बैग का तस्मा कंधे पर कसा, और अपने स्नीकर के पास खड़े उस एक कान वाले काले पिल्ले को देखा।

"सुन Sheru," Neel ने सूखी हंसी के साथ कहा। "मुझे नही पता कि ये कौन सा नरक है। पर एक बात पक्की है—अगर आज शाम तक हमने इस शहर से कुछ Panas नही निकाले, तो रात को इसी कीचड़ में कुत्ते की मौत मरना तय है।"

पिल्ले ने नाक से एक भारी, गर्म फूंक छोड़ी।

और उसके बाद, मुंबई का वो उन्नीस साल का लड़का Central City के खूनी अखाड़ों की तरफ अपना पहला कदम बढ़ा गया।

---
"""

with open(hi_path, "w", encoding="utf-8") as f:
    f.write(scene1_hi + split_marker_hi + new_scene2_hi)

print("Hindi Chapter 1 Scene 2 successfully updated!")

# 2. Update English Scene 2
with open(en_path, "r", encoding="utf-8") as f:
    en_content = f.read()

split_marker_en = "Neel chewed his own stale crust. It was cold and rubbery, but right then it tasted better than anything he could remember."

if split_marker_en not in en_content:
    print("ERROR: split_marker_en not found!")
    exit(1)

scene1_en, old_scene2_en = en_content.split(split_marker_en, 1)

new_scene2_en = """

"All right," Neel muttered, slinging his bag over one shoulder as he prepared to drop down. "Let's see where the main gate of this madhouse is—"

The moment his torn sneaker hit the cart's lower iron step, his right hand instinctively reached down and rested upon the pup's scarred brow.

*ZZZZZT!*

Like accidentally jamming a finger into an exposed wall socket—a sharp, vicious shock of current arced between his palm and the rough black fur.

The dull, tingling numbness that had plagued his hands since waking erupted into a live current. A thin crackle of blue static danced across the pup's skull, and the shock snapped the animal's jaws shut. In a panic, the hound jerked its neck back—

*SNAP!*

The rotten tether snapped clean through, and the pup sprang free.

In that single instant, the distant roar of the staging ground vanished completely from Neel's ears.

*Thump. Thump. Thump.*

His heartbeat and the rapid flutter of the pup's pulse locked into a single harmonic cadence. For half a second, Neel felt the dull ache of the pup's scarred hind leg in his own body, and the hound shuddered as it perceived the heavy ache lodged in Neel's skull.

Their breathing fused into one.

"What kind of madness is this..." Neel wrenched his hand back, staring at his palm. Beneath his skin, an azure circuit-like tracery flared briefly before sinking deep into his lifeline.

The pup wasn't growling anymore. Free of its rope, it stepped forward, sniffed Neel's waterlogged denim hem, and rested its scarred head firmly against his shin. That warm, innocent touch... every knot of tension in Neel's chest unspooled all at once.

Then a heavy shadow dropped across the straw, blotting out the ambient light.

Standing at the tailgate was a burly, barrel-chested man who looked as though someone had ripped an oak door off its hinges and planted it in the mud. A stiffened leather apron hugged his gut, and jammed into his belt like a hidden dagger was a split wooden tally-stick. He held a clay cup in one calloused fist, chewing with the cold, joyless patience of someone who had eaten the identical breakfast for thirty years.

"Awake," the man stated flatly. "Good. Saves me the corpse-tax."

Neel's mouth felt like sandpaper. "Where... where am I?"

"South Flats. Staging Ground eleven." The wagon master jerked his chin toward the distant horizon without bothering to look. "City's past that wall. You're out here. That's your whole story, and it isn't my problem."

"And who are you?"

"The man whose cart you've been bleeding on." He took a slow sip. "Found you face down in the drainage ditch near the east post, drinking mud. A stray body in the ditch means four Panas in fines and half a morning dealing with the magistrate. So I dumped you in the hay. Now say your thanks and clear out."

Neel pressed two fingers behind his ear. No blood, but that heavy ache was still throbbing. "How long was I out?"

"Two bells. Call it three if you count the time you spent babbling to the sky." The carter's gaze raked over Neel's clothes—the jeans, the soaked sneakers, and the blue lanyard dangling from his collar. "Drifter."

There was no surprise in his voice, only the flat indifference reserved for an uncollared dog on the roadside.

"Wherever you dropped from," the man continued, "you've got no seal, no guild medallion, no paperwork. No family backing you up with a clan claim. Every now and then, trash falls out of the sky. The gate clerks have a single word for your kind—unindexed."

*"unindexed. No records, no identity. In this world, I don't even exist."*

"I need to get inside that city," Neel said, glancing toward the distant rampart.

"Then pull out three copper Panas."

"Three Panas?"

"Three. That's the gate toll. Farmers, draymen, caravan bosses—anyone without an official merchant's brass badge pays three." The man tilted his cup. "And don't look at me for credit. I've hauled freight on this highway for nineteen years, and I've never seen a copper returned by a nameless drifter."

"What happens if I just walk up to the gate without coin?"

"The clerk holds out his palm. You show him empty pockets. He blows a whistle, and two guard-spears shove you into the pen on the right." The teamster pointed his chin toward a distant palisade. "Mud floor, no roof, thirty men chained to a timber rail. By noon they'll hand you an iron chisel and drop you into the South Trench—scraping toxic salt-grass roots off stone walls that sprout them back before sunrise."

"And if someone refuses the labor?"

"They shove him through the other arch. Sand-Pits. The blood bazaar." The carter's mouth twisted in a humorless smirk. "Cheap fighters, cheap slaughter, and a fistful of copper for whoever's still standing at sunset. Either way, nobody walks away with all their teeth."

Neel looked down at his own hands. Slender fingers, ink stains near the nails, raw scraped knuckles. For three years, those hands had handled nothing heavier than engineering textbooks and cheap styluses; they had never fought for their life.

*Three Panas. Either food and a dry floor for the night, or an entry token through the gates. Scraping both together is impossible.*

The grinding math of Mumbai had followed him across worlds.

"Boy," the wagon master grunted.

"What?"

"The hound."

Neel glanced down. The black pup remained pressed against his calf, one ear cocked, glaring at the carter with ancient venom.

"He's not mine," Neel said.

"On paper, he's mine. Bought him off a Caldera hauler for two Panas, cord included." The man scowled, disgusted with his own investment. "Worst two coppers I ever spent. Won't pull, won't guard, and won't touch meat that isn't already dead. Figured I'd dump him at the cull-pen at the gate and sell the cord for a Masha."

Neel glanced at the severed rope lying in the muck. "The cord's already broken."

"I can see that." The carter's eyes moved from the rope to the pup's face, then settled on Neel's right hand. A heavy, dangerous suspicion flickered across his gaze. "You cut that?"

"Snapped on its own. Rotten fiber."

"Hmm..." The carter set his clay cup on the cart rim, studying Neel's knuckles with the sharp eye of a man who had diagnosed cattle diseases for two decades. "Your fingers are humming, Drifter. I can hear the buzz from here."

Neel clenched his fist tight. Beneath his skin, that thin, warm thread of current was still pulsing from wrist to pinky.

"It's... just static electricity," Neel deflected.

"Static doesn't hum in fifths." The carter took two deliberate steps back, putting the full breadth of the iron wheel between them. "I was hauling runic freight before that wall was quarried. Keep your cursed fingers away from my Lava-Bull."

He turned on his heel and melted into the growing roar of Staging Ground eleven.

Because the entire staging camp was roaring to life.

Hundreds of beast-carts stood bumper-to-tail in massive chocked rows. Iron-banded wheels were blocked with dressed stone, their axles slathered in thick grease that glistened black in the mud. Between them surged teams of colossal draft beasts—not just the basalt Lava-Bulls, but striped savanna horn-beasts and an enormous grey brute with a spiraled horn erupted straight through its own cheekbone.

The reek came in waves—wet hide, the red glow of roadside smithy forges, boiling sour porridge, and animal dung. A brass horn sounded from the ramparts—two short blasts, one long. Criers shouted manifests from raised stone platforms while teamsters squared up over freight rates. Between the rolling wheels, ragged children darted through the muck with wicker baskets, scooping fresh manure before rival gatherers could reach it.

And beyond the carts, a ragged line of unindexed men stood in silence, being counted off with an overseer's rod. Fifty-two... fifty-three...

In the entire staging ground, not a single person looked up.

Neel raised his eyes.

Half a mile ahead, through the thinning mist, the colossal white stone ramparts of Central City stretched across the horizon like a frozen wave. And above it hung only that bleak, overcast slate-grey sky—no sun, no birds, only the chill.

"Don't stare."

Neel spun around. The wagon master stood ten paces away, eyeing him cold.

"First-timers always gawk. Then their wits scramble and they shake for a week. Look at the mud and keep your feet moving."

"What is this place?" Neel asked, his voice swallowed by the sheer scale of it all.

The carter gave him a frigid glance. "Central City. Crossroads of the Five Shards. Gate opens on the third bell. If you're still standing in this mud when the clapper drops, you'll rot out here all season."

*DHOOONNNNNNN!*

The first great bell detonated from atop the ramparts.

Neel felt the vibration rattle in his molars. Every cart in the staging ground shuddered, and hundreds of harnessed beasts leaned into their traces as one.

Then the second bell toll rang across the flats.

And finally, from far across the expanse, came the deep, reverberating toll of the third bell.

Neel turned toward the gateway.

Half a mile ahead, set into the center of a two-mile-long white stone rampart, the hundred-foot-tall black basalt gate of Central City began to groan open. Through its yawning mouth billowed a luminous corridor of breathable blue Aether-mist. Freight carts from the Western Caldera and cloaked mercenaries began shuffling forward as the morning Muhurta window unlocked the inspection barriers.

Carved across the basalt lintel in sharp, monumental characters, Neel's newly awakened senses deciphered the inscription with effortless clarity:

**CENTRAL CITY — THE CROSSROADS OF THE FIVE SHARDS.**

Neel drove the dead smartphone deep into his inner jacket pocket. He hitched the strap of his waterlogged backpack over his shoulder, then looked down at the one-eared black pup standing resolute beside his sneaker.

"Listen up, Sheru," Neel murmured, a grim, reckless grin tugging at his lips. "I don't know what kind of hell we've landed in. But one thing's dead certain—if we don't squeeze some Panas out of this city before sundown, we're sleeping in this freezing mud tonight."

The pup snorted, venting a sharp puff of hot breath into the air.

And with that, the nineteen-year-old from Mumbai took his first step forward, wading through the mud toward the blood-soaked arenas of Central City.

---
"""

with open(en_path, "w", encoding="utf-8") as f:
    f.write(scene1_en + split_marker_en + new_scene2_en)

print("English Chapter 1 Scene 2 successfully updated!")
