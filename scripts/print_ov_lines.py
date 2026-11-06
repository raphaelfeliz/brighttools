with open('C:/code/BrightTools/worktrees/pull/snippets/option-value.liquid', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(195, 212):
    print(f"{i+1}: {repr(lines[i])}")
