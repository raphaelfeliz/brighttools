with open('C:/code/BrightTools/worktrees/pull/snippets/option-value.liquid', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'color_swatch_style' in l or 'block-swatch' in l:
        print(f"Line {i+1}: {l}", end='')
