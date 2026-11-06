with open('C:/code/BrightTools/worktrees/pull/snippets/product-info.liquid', 'r', encoding='utf-8') as f:
    pull_pi = f.read()

# 1. Add Dealeasy bypass right after {%- for block in section.blocks -%}
dealeasy_bypass = """    {%- comment -%}
      ------------------------------------------------------------------------
      [SURGICAL OVERRIDE: DEALEASY BYPASS]
      Skips rendering Dealasy DOM blocks so app script cannot inject widgets.
      TO REVERSE: Remove the 3-line if block below.
      Git commit reference: c4b3a3d
      ------------------------------------------------------------------------
    {%- endcomment -%}
    {%- if block.type contains 'dealeasy' -%}
      {%- continue -%}
    {%- endif -%}
"""
for_loop = "{%- for block in section.blocks -%}"
assert for_loop in pull_pi
merged_pi = pull_pi.replace(for_loop, for_loop + "\n" + dealeasy_bypass)

# 2. Add 'mar26_gradient_title' block handler before {%- when 'title' -%}
mar26_gradient_title = """          {%- when 'mar26_gradient_title' -%}
            <style>
              @media (max-width: 999px) {
                .mar26-gradient-title-block.hidden-mobile { display: none !important; }
              }
              @media (min-width: 1000px) {
                .mar26-gradient-title-block.hidden-desktop { display: none !important; }
              }
            </style>
            {%- liquid
              assign show_mobile = block.settings.show_on_mobile | default: true
              assign show_desktop = block.settings.show_on_desktop | default: true
              assign top_text = block.settings.text_top
              assign text = block.settings.text
            -%}
            {%- capture visibility_class -%}
              {%- unless show_mobile %} hidden-mobile{% endunless -%}
              {%- unless show_desktop %} hidden-desktop{% endunless -%}
            {%- endcapture -%}
            <div class="product-info__gradient-title v-stack gap-0" style="font-weight: {{ block.settings.font_weight }}; letter-spacing: -0.04em;">
              {%- if top_text != blank -%}
                <span class="mar26-solid-title" style="color: rgb(var(--text-color));">{{ top_text }}</span>
              {%- endif -%}
              {%- if text != blank -%}
                <span class="mar26-gradient-title" style="--gradient-color-1: {{ block.settings.color_1 }}; --gradient-color-2: {{ block.settings.color_2 }}; font-size: inherit; font-weight: inherit; padding-bottom: 0.15em; margin-bottom: -0.15em;">
                  {{ text }}
                </span>
              {%- endif -%}
            </div>
"""

when_title = "{%- when 'title' -%}"
assert when_title in merged_pi
merged_pi = merged_pi.replace(when_title, mar26_gradient_title + "\n          " + when_title)

with open('C:/code/BrightTools/snippets/product-info.liquid', 'w', encoding='utf-8', newline='\n') as f:
    f.write(merged_pi)

print("Successfully merged snippets/product-info.liquid onto 7.2.0!")
