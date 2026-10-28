import os
import json
import sys

# Ensure scripts directory is on path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from generate_modules import generate_html

project_root = os.path.dirname(current_dir)
base_dir = os.path.join(project_root, "New")
template_path = os.path.join(current_dir, "portal_template.html")

def build_portal():
    print("Generating modules data...")
    modules_data = generate_html()
    data_json = json.dumps(modules_data, ensure_ascii=False)
    
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
        
    final_html = template.replace("###DATA_PLACEHOLDER###", data_json)
    
    output_path = os.path.join(base_dir, "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)
        
    size_mb = round(os.path.getsize(output_path) / (1024 * 1024), 2)
    print(f"Master HTML portal successfully generated at: {output_path} ({size_mb} MB)")

if __name__ == "__main__":
    build_portal()
