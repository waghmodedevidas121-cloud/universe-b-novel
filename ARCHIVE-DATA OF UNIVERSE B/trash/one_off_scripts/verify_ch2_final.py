# -*- coding: utf-8 -*-
with open('d:/Web Novel/UNIVERSE B/Story/20_Season_1_Chapter_2_Hindi.md', 'r', encoding='utf-8') as f:
    text = f.read()

banned_words = [
    ('halak', 'हलक'), ('kanth', 'कंठ'), ('nathuno', 'नथुनों'), ('nathune', 'नथुने'), 
    ('chechak', 'चेचक'), ('khurdure', 'खुरदुरे'), ('gadivan', 'गाड़ीवान'), 
    ('aundha', 'औंधा'), ('daru', 'दारू'), ('gutkha', 'गुटखा'), ('kanpati', 'कनपटी'), 
    ('jabda', 'जबड़ा'), ('bhabhka', 'भभका'), ('sadandh', 'सड़ांध'), 
    ('pitta', 'पित्त'), ('kul jama', 'कुल जमा'), ('kshan', 'क्षण'), 
    ('netra', 'नेत्र'), ('nayan', 'नयन'), ('hast', 'हस्त'), ('paad', 'पाद'), 
    ('nashwar jism', 'नश्वर जिस्म'), ('kaundh uthi', 'कौंध उठी'), 
    ('cheerti hui', 'चीरती हुई'), ('maano', 'मानो'), ('ek ajeeb si', 'एक अजीब-सी'), 
    ('ajeeb si', 'अजीब सी'), ('ajeeb sa', 'अजीब सा'), ('wah', ' वह '), ('yah', ' यह ')
]

found = [label for label, word in banned_words if word in text]
if found:
    print("Found banned items:", found)
    import sys
    sys.exit(1)
else:
    print("VERIFICATION 100% PASS: ZERO BANNED WORDS IN CHAPTER 2 HINDI MASTER!")
