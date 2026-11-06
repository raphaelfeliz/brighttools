import difflib

for f in ['templates/product.mar26-with-bundle-builder.json', 'templates/product.mar26.json']:
    p_main = 'C:/code/BrightTools/' + f
    p_pull = 'C:/code/BrightTools/worktrees/pull/' + f
    with open(p_main, 'r', encoding='utf-8') as f1, open(p_pull, 'r', encoding='utf-8') as f2:
        diff = list(difflib.unified_diff(f2.readlines(), f1.readlines(), fromfile='pull', tofile='main', n=1))
    print(f"=== DIFF {f} ===")
    print(''.join(diff))
