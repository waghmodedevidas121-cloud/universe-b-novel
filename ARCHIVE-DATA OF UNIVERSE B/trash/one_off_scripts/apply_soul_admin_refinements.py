import os
import re

_current_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_current_dir)
base_dir = os.path.join(_project_root, "New")

files = [
    os.path.join(base_dir, "04_Soul_Administration.md"),
    os.path.join(base_dir, "world", "soul_admin.md")
]

for fp in files:
    if not os.path.exists(fp):
        continue
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    # Update note at line 18
    content = re.sub(
        r"> \*\*टीप:\*\* `Pratigraha`, `Ātma-Patra`, `Band 0–IV` ही नावे \*\*प्रस्तावित परिभाषा\*\* आहेत;.*?(?=\n\n---|\n---)",
        r"> **कॅनन लॉक:** The Soul Reception Depository (Pratigraha), Lead-Lined Soul Cylinders (Brass Capsules), The White Couriers, आणि Band 0 ते IV या सर्व संज्ञा Universe B च्या अंतिम आणि अपरिवर्तनीय नियमांनुसार (Canonical Lock) अधिकृतपणे स्थापित झाल्या आहेत.",
        content
    )

    # Route A official dock (X7 resolved) -> Route A official dock
    content = content.replace("Route A official dock (X7 resolved):", "Route A official dock:")

    # [F-02 Resolved] and [F-07 Resolved] removal
    content = content.replace("### 4.0 The Lawful Entry Distinction & Three Soul Vectors [F-02 Resolved]", "### 4.0 The Lawful Entry Distinction & Three Soul Vectors")
    content = content.replace("### 4.1 The 5-Stage Route B State Transition Machine [F-07 Resolved]", "### 4.1 The 5-Stage Route B State Transition Machine")

    # Pratigraha definition
    content = content.replace(
        "**Pratigraha** (प्रतिग्रह — प्रस्तावित नाव) हे Yama कार्यालयाच्या मैदानातील प्रचंड आगमन-गोदाम आहे.",
        "**The Soul Reception Depository (Pratigraha)** — वॉर्डन सेतुव्रताच्या देखरेखीखालील मुख्य आगमन व क्वारंटाईन गोदाम. हे Yama कार्यालयाच्या मैदानातील प्रचंड आगमन-गोदाम आहे."
    )

    # Provisional nature row in table
    content = content.replace(
        "| **Provisional Nature** | हा शिक्का केवळ **प्रक्रियेचा तात्पुरता टप्पा** दर्शवतो.",
        "| **Quarantine & Intake Nature** | हा शिक्का केवळ **प्रक्रियेचा आगमन व क्वारंटाईन टप्पा** दर्शवतो."
    )

    # Power Bands section update
    old_band_sec = r"\*\*Power Bands `\[PROVISIONAL NOMENCLATURE\]`:\*\*.*?(?=\n> \*\*T7 hard cap:\*\*)"
    new_band_sec = """**The Five Canonical Power Bands (Dvāra Gate Readings) [CANON LOCK]:**

| Band | Canonical नाव | अर्थ व क्षमता मर्यादा | सामान्यतः कोण व लोकसंख्या |
| :--- | :--- | :--- | :--- |
| **Band 0** | **Unawakened (सुप्त)** | कोणतीही अलौकिक क्षमता नाही; केवळ नैसर्गिक शारीरिक कणखरता. | सामान्य नश्वर नागरिक (६०–७०% लोकसंख्या). |
| **Band I** | **Awakened (जागृत)** | प्राथमिक प्राण व श्वास-नियंत्रण क्षमता; प्रशिक्षणाने विस्तार. | शिस्तबद्ध सामान्य सैनिक व नवशिक्ये (T1–T2 Ceiling). |
| **Band II** | **Adept (सिद्ध)** | प्रगत नाडी-संरेखन, यंत्र व अस्त्र-धारणा क्षमता. | उच्च पुण्य, शुद्ध साधक (T3–T4 Ceiling). |
| **Band III** | **Ascendant (ऊर्ध्व)** | उच्च-स्तरीय जागृत योद्धे व कुलप्रमुख; दुर्मिळ affinity. | निर्मल आत्मे (T5–T6 Ceiling). |
| **Band IV** | **Sovereign / Transcendent (विमल)** | नश्वर शरीराची सर्वोच्च मर्यादा; सर्व १४ शक्ती-वर्गांसाठी पूर्ण सुसंगतता. | विमल आत्मे (**T7 Hard Mortal Cap**; सर्व १४ शक्ती-वर्गांसाठी पूर्ण सुसंगतता). |
"""
    content = re.sub(old_band_sec, new_band_sec, content, flags=re.DOTALL)

    # Add Canonical Destiny Classifications if not present
    if "### 4.0.1 Canonical Destiny Classifications" not in content:
        destiny_block = """

### 4.0.1 Canonical Destiny Classifications [CANON LOCK]
1. **Written Fate (पूर्वीचे Lihito):** Route A कायदेशीर आत्म्यांचे ३-५ मुख्य वळणांचे पूर्व-नियोजित नशीब.
2. **Half-Written Fate (पूर्वीचे Ardha-Rikta / अर्ध-रिक्त):** ५% एलियन्स वसाहतीचे अर्ध-कोरे नशीब व गतजन्माच्या स्मृती (Past-Life Echoes).
3. **Blank Slate ([STATUS: UNINDEXED / BLANK SLATE]):** Route B अनधिकृत आत्म्यांचे १००% कोरे नशीब (शून्य चीट्स, केवळ स्वतःच्या कृतीतून विकास).
"""
        content = content.replace("### 4.1 The 5-Stage Route B State Transition Machine", destiny_block + "\n### 4.1 The 5-Stage Route B State Transition Machine")

    # In section 6.2 title
    content = content.replace("### 6.2 Dootan’s White Doot-Yānas — *The White Couriers* (पांढरी दूतवाहक)", "### 6.2 The White Couriers (दूतानच्या नेतृत्वाखालील लेव्हिटेटिंग पितळी दूत-याने)")
    content = content.replace("### 6.2 Dootan's White Doot-Yānas — *The White Couriers* (पांढरी दूतवाहक)", "### 6.2 The White Couriers (दूतानच्या नेतृत्वाखालील लेव्हिटेटिंग पितळी दूत-याने)")

    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {fp} with Refinement 2.")

# Parity check
f1 = open(files[0], encoding="utf-8").read()
f2 = open(files[1], encoding="utf-8").read()
print(f"Soul Admin files byte parity: {f1 == f2} ({len(f1)} vs {len(f2)})")
