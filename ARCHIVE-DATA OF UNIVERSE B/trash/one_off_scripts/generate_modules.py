import os
import re
import html
import json
import sys

_current_dir = os.path.dirname(os.path.abspath(__file__))
if _current_dir not in sys.path:
    sys.path.insert(0, _current_dir)

_project_root = os.path.dirname(_current_dir)
base_dir = os.path.join(_project_root, "New")
if not os.path.exists(base_dir):
    base_dir = r"D:\Web Novel\New"

from test_parser import md_to_html
from build_categories import categories

def generate_html():
    modules_data = []
    
    for cat in categories:
        folder_path = os.path.join(base_dir, cat["folder"])
        cat_files = []
        if os.path.exists(folder_path):
            files = sorted(os.listdir(folder_path))
            for f in files:
                if f.endswith(".md"):
                    full_p = os.path.join(folder_path, f)
                    with open(full_p, "r", encoding="utf-8") as fp:
                        content = fp.read()
                    cat_files.append({
                        "filename": f,
                        "title": f.replace(".md", "").replace("_", " "),
                        "size_kb": round(len(content) / 1024, 1),
                        "html_body": md_to_html(content)
                    })
        modules_data.append({
            "folder": cat["folder"],
            "title": cat["title"],
            "icon": cat["icon"],
            "marathi_summary": cat["marathi_summary"],
            "key_points": cat["key_points"],
            "files": cat_files
        })
        
    print(f"Loaded {len(modules_data)} categories with files.")
    return modules_data

if __name__ == "__main__":
    generate_html()
