import re

file_path = r"d:\Web Novel\Brahmand\01_WORLD_BIBLE\05_Cosmic_Eras_and_The_Seven_Nightmares.md"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace line 40
text = text.replace(
    "• पवित्र श्वापद तह (The Great Beast Accord): ७२,००० Nādī-Refinery द्वारे १० पट वेगाने कात टाकणे.",
    "• पवित्र श्वापद तह (The Great Beast Accord): Vessel-Refinery (ऊर्जा-वाहिनी शुद्धीकरण) द्वारे १० पट वेगाने कात टाकणे."
)

# Replace line 50
text = text.replace(
    "• The Mortal Miracle: केवळ मानवाकडे ७२,००० Nādīs व Prāṇāyāma Reset, ज्यामुळे देव व असुरांचे कवच भेदता येते.",
    "• The Mortal Miracle: मानवी शरीरातील लवचिक ऊर्जा-वाहिन्या (Vessel Channels) व Breath Reset, ज्यामुळे देव व असुरांचे जड कवच भेदता येते."
)

# Replace line 151
text = text.replace(
    "2. **The 72,000 Nādī-Refinery Mutual Benefit:** अरण्यातील हिंस्त्र वन्य श्वापदे (Wild Aether-Beasts) जंगलात स्वतःची ऊर्जा सहज शुद्ध करू शकत नाहीत; त्यांना नैसर्गिक कात टाकायला (Kāyā-Kośa Molting) २०० वर्षे लागतात. मानवी किंवा असुरी साधकाच्या ७२,००० नाड्या वन्य श्वापदाच्या कच्च्या ऊर्जेसाठी बाह्य शुद्धीकरण फिल्टर (External Refinery) म्हणून काम करतात.",
    "2. **The Vessel-Refinery Mutual Benefit:** अरण्यातील हिंस्त्र वन्य श्वापदे (Wild Aether-Beasts) जंगलात स्वतःची ऊर्जा सहज शुद्ध करू शकत नाहीत; त्यांना नैसर्गिक कात टाकायला (Kāyā-Kośa Molting) २०० वर्षे लागतात. मानवी साधकाच्या शरीरातील लवचिक ऊर्जा-वाहिन्या (Biological Vessel Channels) वन्य श्वापदाच्या कच्च्या ऊर्जेसाठी बाह्य शुद्धीकरण फिल्टर (External Refinery) म्हणून काम करतात."
)

# Replace line 174
text = text.replace(
    "केवळ मानवी शरीरात **७२,००० नाड्या, इडा-पिंगला-सुषुम्ना आणि काया-कोश** ची पूर्ण रचना आहे. जेव्हा मानवी साधक आपल्या श्वासाचे नियंत्रण (Prāṇāyāma / Breath Reset) धनुर्वेदाशी जोडतो, तेव्हा तो देवांचे सौर-कवच आणि असुरांचे जाड चिलखत लीलया भेदून काढतो!",
    "केवळ मानवी शरीरात **लवचिक ऊर्जा-वाहिन्या (Vessel Channels), सुषुम्ना-मार्ग आणि प्राणायामिक श्वास-नियंत्रण (Breath Reset)** ची संपूर्ण नैसर्गिक रचना आहे. जेव्हा मानवी साधक आपल्या श्वासाचे नियंत्रण धनुर्वेदाशी जोडतो, तेव्हा तो देवांचे सौर-कवच आणि असुरांचे जाड चिलखत लीलया भेदून काढतो!"
)

# Also let's check the Nightmares in 05_Cosmic_Eras_and_The_Seven_Nightmares.md
# Let's inspect where the 7 Nightmares are in this file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 05_Cosmic_Eras_and_The_Seven_Nightmares.md successfully")
