import os
import json

templates_dir = r"C:\code\BrightTools\worktrees\main\templates"
registry_path = r"C:\code\BrightTools\docs\documentation\templates\templates.registry.yaml"

templates = []

# Collect templates
for root, dirs, files in os.walk(templates_dir):
    for file in files:
        if file.endswith('.json') or file.endswith('.liquid'):
            file_path = os.path.join(root, file)
            rel_name = os.path.relpath(file_path, templates_dir).replace('\\', '/')
            templates.append(rel_name)

# Organize templates
bt_suffix = []
mar26_prefix_or_contains = []
standard = []

for temp in templates:
    name_lower = temp.lower()
    # Check for -bt
    # e.g., collection.brooms-bt.json -> contains '-bt' before extension
    name_without_ext = os.path.splitext(temp)[0]
    
    if name_without_ext.endswith('-bt'):
        bt_suffix.append(temp)
    elif 'mar26' in name_lower:
        mar26_prefix_or_contains.append(temp)
    else:
        standard.append(temp)

# Sort them
bt_suffix.sort()
mar26_prefix_or_contains.sort()
standard.sort()

# Build YAML output
with open(registry_path, 'w', encoding='utf-8') as f:
    f.write("# Templates Registry\n")
    f.write("# Organized by prefix/suffix or standard categories\n\n")
    
    f.write("bt_custom_templates:\n")
    f.write("  description: \"Custom BrightTools templates using the -bt suffix. These are actively used in the Shopify store.\"\n")
    f.write("  templates:\n")
    for temp in bt_suffix:
        f.write(f"    - template: \"{temp}\"\n")
        f.write("      active: true\n")
        
    f.write("\nmar26_custom_templates:\n")
    f.write("  description: \"Custom templates using the mar26 namespace.\"\n")
    f.write("  templates:\n")
    for temp in mar26_prefix_or_contains:
        f.write(f"    - template: \"{temp}\"\n")
        f.write("      active: null # Leave open\n")
        
    f.write("\nstandard_templates:\n")
    f.write("  description: \"Standard Shopify theme templates and customer accounts templates.\"\n")
    f.write("  templates:\n")
    for temp in standard:
        f.write(f"    - template: \"{temp}\"\n")
        f.write("      active: null # Leave open\n")

print("Registry YAML generated successfully.")
