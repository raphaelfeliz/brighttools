import os
import json

templates_dir = r"C:\code\BrightTools\worktrees\main\templates"
summary_md_path = r"C:\code\BrightTools\docs\documentation\templates\templates.summary.md"

target_templates = []

# Collect all -bt.json templates, index.json, and product templates
for root, dirs, files in os.walk(templates_dir):
    for file in files:
        is_bt = file.endswith('-bt.json')
        is_homepage = (file == 'index.json')
        is_product = (file == 'product.json' or (file.startswith('product.') and file.endswith('.json')))
        
        if is_bt or is_homepage or is_product:
            file_path = os.path.join(root, file)
            rel_name = os.path.relpath(file_path, templates_dir).replace('\\', '/')
            target_templates.append((file, file_path, rel_name))

# Sort: homepage first, then product.json, then custom products, then -bt templates
def get_sort_key(item):
    filename = item[0]
    if filename == 'index.json':
        return (0, '')
    elif filename == 'product.json':
        return (1, '')
    elif filename.startswith('product.'):
        return (2, filename)
    else:
        return (3, filename)

target_templates.sort(key=get_sort_key)

# Parse each template and extract order/sections
parsed_templates = []

for filename, path, rel_name in target_templates:
    with open(path, 'r', encoding='utf-8') as f:
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
            print(f"Error parsing {path}: {e}")
            continue
            
        sections = data.get("sections", {})
        order = data.get("order", [])
        
        ordered_sec_types = []
        ordered_sec_details = []
        unique_sec_types = []
        
        for key in order:
            sec_val = sections.get(key)
            if isinstance(sec_val, dict):
                sec_type = sec_val.get("type", "")
                if sec_type:
                    ordered_sec_types.append(sec_type)
                    ordered_sec_details.append(f"{key} ({sec_type})")
                    if sec_type not in unique_sec_types:
                        unique_sec_types.append(sec_type)
            else:
                # Key might represent just a string in some contexts (unlikely for sections)
                pass
                
        is_homepage = (filename == 'index.json')
        is_default_prod = (filename == 'product.json')
        
        if is_homepage:
            desc_name = "homepage"
        elif is_default_prod:
            desc_name = "default product"
        else:
            desc_name = filename.replace('.json', '')
            
        parsed_templates.append({
            "filename": filename,
            "rel_name": rel_name,
            "description": f"Template for the {desc_name} page, featuring sections: {', '.join(ordered_sec_types) if ordered_sec_types else 'none'}.",
            "active_custom_sections": ", ".join([f'"{t}"' for t in unique_sec_types]),
            "raw_sections": ordered_sec_details
        })

# Write the updated templates.summary.md
with open(summary_md_path, 'w', encoding='utf-8') as out_f:
    out_f.write("# Template Summary (Custom -bt templates, Homepage, & Product templates)\n\n")
    out_f.write("This document registers and describes the custom Shopify templates containing the suffix -bt, the homepage, and product templates used in the BrightTools storefront.\n\n")
    out_f.write("## Custom, Homepage & Product Templates (Summary)\n\n")
    out_f.write("| Template File | Description | Active Custom Sections |\n")
    out_f.write("| --- | --- | --- |\n")
    
    for t in parsed_templates:
        link = f"[{t['filename']}](file:///C:/code/BrightTools/worktrees/main/templates/{t['rel_name']})"
        out_f.write(f"| {link} | {t['description']} | {t['active_custom_sections']} |\n")
        
    out_f.write("\n---\n\n")
    out_f.write("## Raw Registry (AI / Script Optimized)\n\n")
    out_f.write("```yaml\n")
    out_f.write("registry:\n")
    for t in parsed_templates:
        out_f.write(f"  - template: \"{t['rel_name']}\"\n")
        out_f.write("    sections:\n")
        for s in t['raw_sections']:
            out_f.write(f"      - \"{s}\"\n")
    out_f.write("```\n")

print("templates.summary.md updated successfully with products.")
