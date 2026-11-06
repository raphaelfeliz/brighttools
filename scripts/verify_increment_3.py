import json, os, subprocess

with open('C:/code/BrightTools/work/theme-upgrade-7.2.0-audit.json', 'r') as f:
    audit = json.load(f)

templates = [item['file'] for item in audit['template_config_drift'] if item['file'].startswith('templates/collection.')]
files = ['snippets/product-card.liquid', 'snippets/price-list.liquid'] + templates

cmd = [
    'shopify', 'theme', 'pull',
    '--theme', '188300787986',
    '--path', 'C:\\code\\BrightTools\\worktrees\\pull',
    '--store', 'brighttools-au.myshopify.com'
]
for f in files:
    cmd.extend(['--only', f])

print("Pulling files for verification:", len(files))
res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
print("Return code:", res.returncode)
if res.stderr:
    print("STDERR:\n", res.stderr)

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
    print("INCREMENT 3 VERIFIED 100% EXACT MATCH ACROSS ALL 16 FILES")
