import os

output_file = "UNIVERSE_B_COMBINED.txt"
with open(output_file, "w", encoding="utf-8") as outfile:
    for root, dirs, files in os.walk("."):
        # Trash aani preview folders skip kara
        if any(x in root for x in ["trash", "__pycache__", ".git"]):
            continue
        for file in files:
            if file == output_file:
                continue
            if file.endswith((".md", ".txt")):
                path = os.path.join(root, file)
                outfile.write(f"\n\n{'='*50}\n# FILE: {path}\n{'='*50}\n\n")
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as infile:
                        outfile.write(infile.read())
                except Exception as e:
                    outfile.write(f"Error reading file: {e}")

print("Done! File created: UNIVERSE_B_COMBINED.txt")