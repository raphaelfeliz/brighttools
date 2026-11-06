with open('C:/code/BrightTools/worktrees/pull/snippets/product-card.liquid', 'r', encoding='utf-8') as f:
    pull_pc = f.read()

# In 7.2.0, the title block is:
old_target = """      {%- else -%}
        <span class="product-card__title"
          ><a href="{{ product.url }}" class="bold" data-instant>{{ product.title }}</a></span
        >
      {%- endif -%}"""

new_target = """      {%- else -%}
        <span class="product-card__title"
          ><a href="{{ product.url }}" class="bold" data-instant>{{ product.title }}</a></span
        >
        <!-- Start of Judge.me code -->
        <div class='jdgm-widget jdgm-preview-badge' data-id='{{ product.id }}'>
          {{ product.metafields.judgeme.badge }}
        </div>
        <!-- End of Judge.me code -->
      {%- endif -%}"""

assert old_target in pull_pc, "Target title block not found in pull_pc"
merged_pc = pull_pc.replace(old_target, new_target)

with open('C:/code/BrightTools/snippets/product-card.liquid', 'w', encoding='utf-8', newline='\n') as f:
    f.write(merged_pc)

print("Successfully merged snippets/product-card.liquid onto 7.2.0!")
