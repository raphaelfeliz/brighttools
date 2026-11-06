import json
import shutil
import os

with open('C:/code/BrightTools/work/theme-upgrade-7.2.0-audit.json', 'r') as f:
    audit = json.load(f)

to_copy = audit['pure_vendor_upgrades'] + [f for f in audit['new_in_upstream'] if 'copy' not in f] + ['config/settings_schema.json']

copied = 0
for rel in to_copy:
    src = os.path.join('C:/code/BrightTools/worktrees/pull', rel)
    dst = os.path.join('C:/code/BrightTools', rel)
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        copied += 1
    else:
        print(f"Missing: {src}")

print(f"Copied {copied} files.")
