import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
transcript_path = r'C:\Users\HP\.gemini\antigravity\brain\270ab2e1-88fb-4ae6-97c2-133bb1920811\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        data = json.loads(line)
        if data.get('source') == 'USER_EXPLICIT':
            content = data.get('content', '')
            keywords = ['naming', 'name', 'नाव', 'hilda', 'olga', 'morvath', 'jormun', 'silas', 'ambika', 'sulabha', 'manu']
            if any(k in content.lower() for k in keywords):
                step = data.get('step_index')
                print(f"=== STEP {step} ===")
                print(content.strip()[:500])
                print("-" * 40)
