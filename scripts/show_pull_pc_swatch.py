with open('C:/code/BrightTools/worktrees/pull/snippets/product-card.liquid', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'color-swatch__view-more' in l:
        print(f"Line {i+1}:")
        for j in range(max(0, i-5), min(len(lines), i+8)):
            print(f"{j+1}: {lines[j]}", end='')
