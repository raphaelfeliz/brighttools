with open('C:/code/BrightTools/snippets/product-card.liquid', 'r', encoding='utf-8') as f1, open('C:/code/BrightTools/worktrees/pull/snippets/product-card.liquid', 'r', encoding='utf-8') as f2:
    main_pc = f1.read()
    pull_pc = f2.read()

# Let's inspect differences in product-card between pull and main
import difflib
diff = list(difflib.unified_diff(pull_pc.splitlines(True), main_pc.splitlines(True), fromfile='pull', tofile='main', n=1))
for d in diff:
    if (d.startswith('+') and not d.startswith('+++')) or (d.startswith('-') and not d.startswith('---')):
        if any(tok in d for tok in ['jdgm', 'judgeme', 'swatch', 'rating']):
            print(d.strip())
