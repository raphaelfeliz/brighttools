with open('C:/code/BrightTools/worktrees/pull/snippets/product-card.liquid', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'product-card__title' in l:
        print(f"Line {i+1}:")
        for j in range(max(0, i-5), min(len(lines), i+10)):
            print(f"{j+1}: {lines[j]}", end='')
