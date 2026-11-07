# BRAHMAND WORKSPACE RULES: 3-STAGE EXECUTION PROTOCOL

## MANDATORY 3-STAGE EXECUTION WORKFLOW (त्रिसूतरी कार्यप्रणाली)

Whenever the user sends a message (delivered with the incoming JSON context and conversation state), the assistant MUST NEVER jump to assumptions, invent unapproved characters, or fabricate narrative decisions. The assistant MUST strictly follow this 3-stage process:

---

### STAGE 1: INCOMING REQUEST & CONTEXT ANALYSIS (सखोल विश्लेषण)
1. **Linguistic & Intent Decoding:**
   - Analyze the user's Marathi, Hinglish, or English instructions word-by-word.
   - Separate explicit commands from exploratory thoughts.
2. **Context & JSON Audit:**
   - Verify active workspace state, existing canon files, and recent user corrections.
3. **Explicit Anti-Goals & Prohibitions (नकारार्थी बंधने):**
   - **ZERO PREMATURE PROTAGONISTS:** NEVER invent, name, or designate any character as the "Protagonist / मुख्य नायक" on your own. The protagonist will ONLY be introduced when the user explicitly commands it.
   - **ZERO ROGUE ASSUMPTIONS:** Do not fabricate unasked weapons, companion pets, special bloodlines, or cheat systems.
   - **STRICT ARCHIVE DATA GOVERNANCE & OUTDATED STATUS (आर्काइव्ह डेटा नियंत्रण नियम):**
     - **ARCHIVE DATA IS OUTDATED:** All files inside `ARCHIVE-DATA OF UNIVERSE B` or legacy archive folders are OUTDATED legacy iterations.
     - **NO DIRECT / AS-IS COPY-PASTE (जसाच्या तसा मजकूर घेण्यास सक्त मनाई):** Never copy-paste or inject raw data from archive folders directly into production without explicit transformation.
     - **MANDATORY USER REVIEW FOR ARCHIVE REFERENCES (युझर रिव्ह्यू बंधनकारक):** When referencing, adapting, or importing concepts from archive data, the assistant MUST explicitly present the proposed points and obtain the USER'S REVIEW & APPROVAL before writing or committing it into active canon.
   - **SANATAN PURITY & CANON LOCK:**
     - The 'नही' Rule: Always `नही` (zero bindi / अनुस्वार-रहित). Never with bindi.
     - Swarga = Tier 2 Buffer Zone (Antariksha-Setu).
     - Suras = Tier 3 Sura Shard (Amarāvatī Spire).
     - Patala = Tier 3 Bila-Svarga (King Bali & Nagas).
     - Tier 4 = Śūnya-Garta (The Corrupted Chasm).
     - Grounding: 100% Vedic / Puranic / Dhanurveda. Zero gamer HUDs, zero video game stats.

---

### STAGE 2: PROMPT SYNTHESIS & EXECUTION BLUEPRINT (प्रॉम्ट / अंतर्गत कार्य-योजना)
Before writing or editing code/files:
1. Formulate a structured internal prompt and action blueprint:
   - What exact files need to be modified or read?
   - What are the exact parameters requested by the user?
   - What boundaries must NOT be crossed?
2. If the user's intent requires a major design choice (e.g. character past life selection, faction allegiance) or draws from archive material, present options or ask clarifying questions rather than deciding unilaterally.

---

### STAGE 3: RIGOROUS EXECUTION & CANONICAL ANSWER (अंतिम उत्तर व अंमलबजावणी)
1. Execute file edits, research, or drafting with surgical precision.
2. Run `python "d:\Web Novel\Brahmand\scripts\verify_brahmand_canon.py"` after modifications to guarantee 100% green canon status.
3. Present a clear, structured, and respectful answer in Marathi/English directly fulfilling the user's request.
