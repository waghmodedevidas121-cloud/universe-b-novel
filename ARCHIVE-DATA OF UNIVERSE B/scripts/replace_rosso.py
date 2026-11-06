import os

paths = [r'd:\Web Novel\UNIVERSE B\New', r'd:\Web Novel\UNIVERSE B\rulebook']

for base in paths:
    for fname in os.listdir(base):
        if fname.endswith('.md'):
            fpath = os.path.join(base, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = content.replace('Donna Beatrice Rosso', 'Donna Beatrice Vanezza')
            new_content = new_content.replace('Beatrice Rosso', 'Donna Beatrice Vanezza')
            new_content = new_content.replace('Rosso Family', 'Vanezza Dynasty')
            new_content = new_content.replace('Rosso Dynasty', 'Vanezza Dynasty')
            new_content = new_content.replace('Rosso घराणे', 'Vanezza घराणे')
            new_content = new_content.replace('रोसो घराणे', 'व्हेनेझ्झा घराणे')
            if new_content != content:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated Rosso in {fname}")

print("Completed Rosso -> Vanezza replacement.")
