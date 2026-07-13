import os
import json

templates_dir = r"C:\code\BrightTools\worktrees\main\templates"
sections_dir = r"C:\code\BrightTools\worktrees\main\sections"
registry_path = r"C:\code\BrightTools\docs\documentation\sections\sections.registry.yaml"

# 1. Collect target templates (-bt.json files, index.json, product.json, product.*.json)
target_templates = []
sections_by_template = {} # template_name -> list of section types

for root, dirs, files in os.walk(templates_dir):
    for file in files:
        is_bt = file.endswith('-bt.json')
        is_homepage = (file == 'index.json')
        is_product = (file == 'product.json' or (file.startswith('product.') and file.endswith('.json')))
        
        if is_bt or is_homepage or is_product:
            file_path = os.path.join(root, file)
            target_templates.append(file)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                clean_lines = []
                for line in content.splitlines():
                    if line.strip().startswith('/*') or line.strip().startswith('*') or line.strip().startswith('*/'):
                        continue
                    clean_lines.append(line)
                clean_content = '\n'.join(clean_lines)
                
                try:
                    data = json.loads(clean_content)
                except Exception as e:
                    print(f"Error parsing {file}: {e}")
                    continue
                
                sections_dict = data.get("sections", {})
                order = data.get("order", [])
                
                sec_types = []
                for key in order:
                    sec_val = sections_dict.get(key)
                    if isinstance(sec_val, dict):
                        sec_type = sec_val.get("type")
                        if sec_type:
                            sec_types.append(sec_type)
                
                sections_by_template[file] = sec_types

# 2. Get list of all sections
sections = []
for root, dirs, files in os.walk(sections_dir):
    for file in files:
        if file.endswith('.liquid') or file.endswith('.json'):
            sections.append(file)

sections.sort()

# 3. For each section, find which templates use it
sections_usage = {}
for sec in sections:
    sec_type_name = os.path.splitext(sec)[0]
    used_by = []
    for temp, sec_types in sections_by_template.items():
        if sec_type_name in sec_types:
            used_by.append(temp)
    used_by.sort()
    sections_usage[sec] = used_by

# Group sections by namespace
bt_custom_sections = []
mar26_custom_sections = []
standard_sections = []

for sec in sections:
    name_without_ext = os.path.splitext(sec)[0]
    usage = sections_usage[sec]
    sec_info = {
        "section": sec,
        "used_by_templates": usage
    }
    
    if name_without_ext.startswith('mar26-'):
        mar26_custom_sections.append(sec_info)
    elif name_without_ext.startswith('bt-') or name_without_ext.endswith('-bt'):
        bt_custom_sections.append(sec_info)
    else:
        standard_sections.append(sec_info)

# 4. Write to YAML
with open(registry_path, 'w', encoding='utf-8') as f:
    f.write("# Sections Registry (Cross-Referenced with Templates)\n")
    f.write("# Displays custom and standard sections, showing which target templates utilize them.\n\n")
    
    f.write("bt_custom_sections:\n")
    f.write("  description: \"Custom BrightTools sections using the bt- namespace or suffix.\"\n")
    f.write("  sections:\n")
    for s in bt_custom_sections:
        f.write(f"    - section: \"{s['section']}\"\n")
        f.write("      used_by_templates:\n")
        if s['used_by_templates']:
            for t in s['used_by_templates']:
                f.write(f"        - \"{t}\"\n")
        else:
            f.write("        []\n")
            
    f.write("\nmar26_custom_sections:\n")
    f.write("  description: \"Custom sections using the mar26 namespace.\"\n")
    f.write("  sections:\n")
    for s in mar26_custom_sections:
        f.write(f"    - section: \"{s['section']}\"\n")
        f.write("      used_by_templates:\n")
        if s['used_by_templates']:
            for t in s['used_by_templates']:
                f.write(f"        - \"{t}\"\n")
        else:
            f.write("        []\n")
            
    f.write("\nstandard_sections:\n")
    f.write("  description: \"Standard Shopify theme sections.\"\n")
    f.write("  sections:\n")
    for s in standard_sections:
        f.write(f"    - section: \"{s['section']}\"\n")
        f.write("      used_by_templates:\n")
        if s['used_by_templates']:
            for t in s['used_by_templates']:
                f.write(f"        - \"{t}\"\n")
        else:
            f.write("        []\n")

print("sections.registry.yaml successfully updated with cross-references including products.")
