with open('C:/code/BrightTools/worktrees/pull/snippets/inventory.liquid', 'r', encoding='utf-8') as f:
    pull_inv = f.read()

# Replace the in_stock block with stock suppression (commit 320ba2a)
old_inv_branch = """        {%- else -%}
          <span class="text-with-icon text-success">
            {%- render 'icon' with 'success' -%}
            {{- 'product.inventory.in_stock' | t -}}
          </span>"""

new_inv_branch = """        {%- else -%}
          <span class="text-with-icon text-warning">{%- render 'icon' with 'warning' -%} {{- 'product.inventory.oversell_stock' | t -}}</span>"""

assert old_inv_branch in pull_inv, "old_inv_branch not found"
merged_inv = pull_inv.replace(old_inv_branch, new_inv_branch)

# Also ensure sold out badge fallback
old_else = "    {%- endif -%}\n  </variant-inventory>\n{%- endif -%}"
new_else = """    {%- else -%}
      <span class="text-with-icon text-error">{%- render 'icon' with 'warning' -%} {{- 'product.general.sold_out_badge' | t | default: 'Sold out' -}}</span>
    {%- endif -%}
  </variant-inventory>
{%- endif -%}"""

assert old_else in merged_inv, "old_else not found"
merged_inv = merged_inv.replace(old_else, new_else)

with open('C:/code/BrightTools/snippets/inventory.liquid', 'w', encoding='utf-8', newline='\n') as f:
    f.write(merged_inv)

print("Successfully merged snippets/inventory.liquid onto 7.2.0!")
