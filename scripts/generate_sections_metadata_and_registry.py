import os
import re
import json

sections_dir = r"C:\code\BrightTools\worktrees\main\sections"
docs_sections_dir = r"C:\code\BrightTools\docs\documentation\sections"

os.makedirs(docs_sections_dir, exist_ok=True)

sections_data = []

# Regex to find {% schema %}...{% endschema %}
schema_re = re.compile(r"{%\s*schema\s*%}(.*?){%\s*endschema\s*%}", re.DOTALL)

def write_manual_yaml(out_path, data):
    with open(out_path, 'w', encoding='utf-8') as out_f:
        out_f.write(f"section: \"{data['section']}\"\n")
        desc = data['description'].replace('"', '\\"')
        out_f.write(f"description: \"{desc}\"\n")
        out_f.write("blocks:\n")
        for b in data.get('blocks', []):
            out_f.write(f"  - \"{b}\"\n")
        out_f.write("settings:\n")
        for s in data.get('settings', []):
            out_f.write(f"  - \"{s}\"\n")

for root, dirs, files in os.walk(sections_dir):
    for file in files:
        file_path = os.path.join(root, file)
        rel_name = os.path.relpath(file_path, sections_dir).replace('\\', '/')
        
        name_without_ext = os.path.splitext(file)[0]
        yaml_name = rel_name.replace('.liquid', '.yaml').replace('.json', '.yaml')
        
        section_name = name_without_ext
        blocks_info = []
        settings_info = []
        
        if file.endswith('.liquid'):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            match = schema_re.search(content)
            if match:
                schema_str = match.group(1).strip()
                try:
                    schema_json = json.loads(schema_str)
                    section_name = schema_json.get('name', section_name)
                    
                    # Extract blocks
                    blocks = schema_json.get('blocks', [])
                    for b in blocks:
                        if isinstance(b, dict) and 'type' in b:
                            blocks_info.append(f"{b['type']} ({b.get('name', '')})")
                            
                    # Extract settings
                    settings = schema_json.get('settings', [])
                    for s in settings:
                        if isinstance(s, dict) and 'id' in s:
                            settings_info.append(f"{s['id']} ({s.get('type', '')})")
                except Exception as e:
                    pass
            
            desc = f"Liquid section template for {section_name}."
            
        elif file.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    # For sections group files
                    desc = f"JSON section group configuration for {section_name}."
                    # Extract sections/settings if available
                    for sec_key, sec_val in data.get('sections', {}).items():
                        settings_info.append(f"{sec_key} ({sec_val.get('type', '')})")
                except Exception as e:
                    desc = f"JSON section file: {section_name}."
        
        yaml_data = {
            "section": rel_name,
            "description": desc,
            "blocks": blocks_info,
            "settings": settings_info
        }
        
        sections_data.append({
            "name": rel_name,
            "description": desc
        })
        
        out_path = os.path.join(docs_sections_dir, yaml_name)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        write_manual_yaml(out_path, yaml_data)

# Generate registry
mar26_sections = []
bt_sections = []
standard_sections = []

for sec in sections_data:
    name = sec['name']
    name_without_ext = os.path.splitext(name)[0]
    
    if name_without_ext.startswith('mar26-'):
        mar26_sections.append(sec)
    elif name_without_ext.startswith('bt-') or name_without_ext.endswith('-bt'):
        bt_sections.append(sec)
    else:
        standard_sections.append(sec)

mar26_sections.sort(key=lambda x: x['name'])
bt_sections.sort(key=lambda x: x['name'])
standard_sections.sort(key=lambda x: x['name'])

registry_path = os.path.join(docs_sections_dir, "sections.registry.yaml")
with open(registry_path, 'w', encoding='utf-8') as f:
    f.write("# Sections Registry\n")
    f.write("# Organized by prefix/suffix namespaces\n\n")
    
    f.write("bt_custom_sections:\n")
    f.write("  description: \"Custom BrightTools sections using the bt- namespace or suffix.\"\n")
    f.write("  sections:\n")
    for s in bt_sections:
        f.write(f"    - section: \"{s['name']}\"\n")
        f.write("      active: true\n")
        
    f.write("\nmar26_custom_sections:\n")
    f.write("  description: \"Custom sections using the mar26 namespace.\"\n")
    f.write("  sections:\n")
    for s in mar26_sections:
        f.write(f"    - section: \"{s['name']}\"\n")
        f.write("      active: null\n")
        
    f.write("\nstandard_sections:\n")
    f.write("  description: \"Standard Shopify theme sections.\"\n")
    f.write("  sections:\n")
    for s in standard_sections:
        f.write(f"    - section: \"{s['name']}\"\n")
        f.write("      active: null\n")

print("Sections YAML and registry generated successfully.")
