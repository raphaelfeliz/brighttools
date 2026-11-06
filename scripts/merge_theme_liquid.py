with open('C:/code/BrightTools/worktrees/pull/layout/theme.liquid', 'r', encoding='utf-8') as f:
    pull_liquid = f.read()

# Apply the 3 custom additions cleanly on 7.2.0:
# 1. mar26-foundation.css and Judge.me styles right after theme.css
old_head = "{{- 'theme.css' | asset_url | stylesheet_tag: preload: true -}}"
new_head = """{{- 'theme.css' | asset_url | stylesheet_tag: preload: true -}}
    {{- 'mar26-foundation.css' | asset_url | stylesheet_tag -}}

<style>
  .product-card .jdgm-preview-badge .jdgm-star.jdgm-star {
    color: #FDCC0D !important;
}

.product-card .jdgm-widget.jdgm-preview-badge.jdgm--done-setup, .jdgm-stars-collections {
    font-size: 75% !important;
}
</style>"""

assert old_head in pull_liquid, "old_head not found"
merged = pull_liquid.replace(old_head, new_head)

# 2. bt-header-group
assert "{%- sections 'header-group' -%}" in merged, "header-group not found"
merged = merged.replace("{%- sections 'header-group' -%}", "{%- sections 'bt-header-group' -%}")

# 3. mar26-footer-group
assert "{%- sections 'footer-group' -%}" in merged, "footer-group not found"
merged = merged.replace("{%- sections 'footer-group' -%}", "{%- sections 'mar26-footer-group' -%}")

with open('C:/code/BrightTools/layout/theme.liquid', 'w', encoding='utf-8', newline='\n') as f:
    f.write(merged)

print("Successfully merged layout/theme.liquid onto 7.2.0!")
