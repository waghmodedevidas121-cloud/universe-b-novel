# -*- coding: utf-8 -*-
with open('d:/Web Novel/UNIVERSE B/scripts/validate_ch2.py', 'r', encoding='utf-8') as f:
    text = f.read()

raw_text = text.split('chapter_2_hindi = """')[1].split('"""')[0]
raw_text = raw_text.replace('हस्तिनापुर', 'पूर्वी क्राउनलैंड्स')

hindi_num_words = [
    ('ek', ' एक '), ('do', ' दो '), ('teen', ' तीन '), ('char', ' चार '), 
    ('panch', ' पाँच '), ('panch2', ' पांच '), ('chhah', ' छह '), ('saat', ' सात '), 
    ('aath', ' आठ '), ('nau', ' नौ '), ('das', ' दस '),
    ('gyarah', ' ग्यारह '), ('barah', ' बारह '), ('pandrah', ' पंद्रह '), 
    ('bees', ' बीस '), ('pachas', ' पचास '), ('sau', ' सौ '), 
    ('hazar', ' हजार '), ('lakh', ' लाख ')
]

found_nums = []
for label, hw in hindi_num_words:
    if hw in raw_text:
        found_nums.append(label)

print("Found number labels:", found_nums)
