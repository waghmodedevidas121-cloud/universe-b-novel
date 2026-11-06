import json

full_path = r'C:\Users\HP\.gemini\antigravity\brain\6896500a-57f4-4e45-94b1-ceb4fca68f6a\.system_generated\logs\transcript_full.jsonl'
out_path = r'd:\Web Novel\UNIVERSE B\scripts\goldfish_chunk5_clean.md'

with open(full_path, 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('step_index') == 49:
            tool_calls = obj.get('tool_calls', [])
            for tc in tool_calls:
                if tc.get('name') == 'send_message':
                    msg = tc['args']['Message']
                    if msg.startswith('"') and msg.endswith('"'):
                        try:
                            msg = json.loads(msg)
                        except Exception:
                            pass
                    with open(out_path, 'w', encoding='utf-8') as out:
                        out.write(msg)
                    print(f"Extracted full message! Length: {len(msg)}")
                    break
