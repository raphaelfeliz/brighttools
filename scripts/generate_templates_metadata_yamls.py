import os
import json

templates_dir = r"C:\code\BrightTools\worktrees\main\templates"
docs_templates_dir = r"C:\code\BrightTools\docs\documentation\templates"

os.makedirs(docs_templates_dir, exist_ok=True)

# Helper function to generate a simple description
def get_description(name, sections):
    section_types = [s.get("type", "") for s in sections.values() if isinstance(s, dict)]
    sec_str = ", ".join([s for s in section_types if s])
    return f"Template for the {name} page, featuring sections: {sec_str or 'none'}."

def write_manual_yaml(out_path, data):
    with open(out_path, 'w', encoding='utf-8') as out_f:
        out_f.write(f"template: \"{data['template']}\"\n")
        # escape quotes in description
        desc = data['description'].replace('"', '\\"')
        out_f.write(f"description: \"{desc}\"\n")
        out_f.write("sections:\n")
        for s in data['sections']:
            out_f.write(f"  - \"{s}\"\n")

# Process all files in templates_dir
for root, dirs, files in os.walk(templates_dir):
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            rel_name = os.path.relpath(file_path, templates_dir).replace('\\', '/')
            yaml_name = rel_name.replace('.json', '.yaml')
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Stripping potential JSON comments
                clean_lines = []
                for line in content.splitlines():
                    if line.strip().startswith('/*') or line.strip().startswith('*') or line.strip().startswith('*/'):
                        continue
                    clean_lines.append(line)
                clean_content = '\n'.join(clean_lines)
                try:
                    data = json.loads(clean_content)
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")
                    continue
                
                sections = data.get("sections", {})
                section_list = list(sections.keys())
                
                # Retrieve section types
                sections_info = []
                for sec_key, sec_val in sections.items():
                    if isinstance(sec_val, dict):
                        sections_info.append(f"{sec_key} ({sec_val.get('type', '')})")
                    else:
                        sections_info.append(sec_key)
                
                name_without_ext = rel_name.replace('.json', '')
                desc = get_description(name_without_ext, sections)
                
                yaml_data = {
                    "template": rel_name,
                    "description": desc,
                    "sections": sections_info
                }
                
                out_path = os.path.join(docs_templates_dir, yaml_name)
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                write_manual_yaml(out_path, yaml_data)
                    
        elif file.endswith('.liquid'):
            file_path = os.path.join(root, file)
            rel_name = os.path.relpath(file_path, templates_dir).replace('\\', '/')
            yaml_name = rel_name.replace('.liquid', '.yaml')
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple check for sections in liquid
            import re
            sections_found = re.findall(r"{%\s*section\s+'([^']+)'\s*%}", content)
            
            yaml_data = {
                "template": rel_name,
                "description": f"Liquid template for {rel_name.replace('.liquid', '')}.",
                "sections": sections_found
            }
            
            out_path = os.path.join(docs_templates_dir, yaml_name)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            write_manual_yaml(out_path, yaml_data)

print("YAML files generation complete.")
