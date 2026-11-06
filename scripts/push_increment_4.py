import json, subprocess

with open('C:/code/BrightTools/work/theme-upgrade-7.2.0-audit.json', 'r') as f:
    audit = json.load(f)

pdp_templates = [item['file'] for item in audit['template_config_drift'] if item['file'].startswith('templates/product.')]
files = [
    'snippets/product-info.liquid',
    'snippets/option-value.liquid',
    'snippets/inventory.liquid'
] + pdp_templates

cmd = [
    'shopify', 'theme', 'push',
    '--theme', '188300787986',
    '--path', 'C:\\code\\BrightTools',
    '--store', 'brighttools-au.myshopify.com'
]
for f in files:
    cmd.extend(['--only', f])

print("Pushing Increment 4 files:", len(files))
res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
print("Return code:", res.returncode)
print("STDOUT:\n", res.stdout)
if res.stderr:
    print("STDERR:\n", res.stderr)
