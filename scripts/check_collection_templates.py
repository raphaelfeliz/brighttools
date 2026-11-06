import json, os, glob

with open('C:/code/BrightTools/work/theme-upgrade-7.2.0-audit.json', 'r') as f:
    audit = json.load(f)

templates = [item['file'] for item in audit['template_config_drift'] if item['file'].startswith('templates/collection.')]
print(f"Collection templates ({len(templates)}):", templates)

# Let's check differences for each collection template between main and pull
for rel in templates:
    p_main = os.path.join('C:/code/BrightTools', rel)
    p_pull = os.path.join('C:/code/BrightTools/worktrees/pull', rel)
    with open(p_main, 'r', encoding='utf-8') as f1, open(p_pull, 'r', encoding='utf-8') as f2:
        d1 = json.load(f1)
        d2 = json.load(f2)
    t1_main_type = d1.get('sections', {}).get('main', {}).get('type')
    t2_main_type = d2.get('sections', {}).get('main', {}).get('type')
    print(f"{os.path.basename(rel)}: main='{t1_main_type}' vs pull='{t2_main_type}'")
