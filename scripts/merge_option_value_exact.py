with open('C:/code/BrightTools/worktrees/pull/snippets/option-value.liquid', 'r', encoding='utf-8') as f:
    pull_ov = f.read()

target_old = "      <span>{{ label | default: value }}</span>\n    </{{ option_value_tag }}>"

target_new = """      {%- liquid
        assign savings = 0
        if variant.compare_at_price > variant.price
          assign savings = variant.compare_at_price | minus: variant.price | times: 100.0 | divided_by: variant.compare_at_price | round
        endif
      -%}

      {%- if savings > 0 -%}
        <span class="mar26-savings-badge">SAVE {{ savings }}%</span>
      {%- endif -%}

      <span>{{ label | default: value }}</span>
    </{{ option_value_tag }}>"""

assert target_old in pull_ov, "target_old still not found"
merged_ov = pull_ov.replace(target_old, target_new)

with open('C:/code/BrightTools/snippets/option-value.liquid', 'w', encoding='utf-8', newline='\n') as f:
    f.write(merged_ov)

print("Successfully merged snippets/option-value.liquid onto 7.2.0!")
