import json, os, re

def strip_comments(text):
    return re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)

with open('C:/code/BrightTools/work/theme-upgrade-7.2.0-audit.json', 'r') as f:
    audit = json.load(f)

templates = [item['file'] for item in audit['template_config_drift'] if item['file'].startswith('templates/collection.')]

for rel in templates:
    p_main = os.path.join('C:/code/BrightTools', rel)
    p_pull = os.path.join('C:/code/BrightTools/worktrees/pull', rel)
    with open(p_main, 'r', encoding='utf-8') as f1, open(p_pull, 'r', encoding='utf-8') as f2:
        d1 = json.loads(strip_comments(f1.read()))
        d2 = json.loads(strip_comments(f2.read()))
    t1_main_type = d1.get('sections', {}).get('main', {}).get('type')
    t2_main_type = d2.get('sections', {}).get('main', {}).get('type')
    print(f"{os.path.basename(rel)}: main='{t1_main_type}' ({len(d1.get('sections',{}))} secs) vs pull='{t2_main_type}' ({len(d2.get('sections',{}))} secs)")
