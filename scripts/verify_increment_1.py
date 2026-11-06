import filecmp
import os

files = ['layout/theme.liquid', 'assets/theme.css']
all_match = True

for rel in files:
    p_main = os.path.join('C:/code/BrightTools', rel)
    p_pull = os.path.join('C:/code/BrightTools/worktrees/pull', rel)
    with open(p_main, 'rb') as f1, open(p_pull, 'rb') as f2:
        c1 = f1.read().replace(b'\r\n', b'\n')
        c2 = f2.read().replace(b'\r\n', b'\n')
        if c1 == c2:
            print(f"VERIFIED EXACT MATCH: {rel}")
        else:
            print(f"MISMATCH: {rel}")
            all_match = False

if all_match:
    print("ALL VERIFIED SUCCESSFULLY")
