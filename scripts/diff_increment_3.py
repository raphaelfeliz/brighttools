import difflib

def diff_files(p1, p2, name):
    with open(p1, 'r', encoding='utf-8') as f1, open(p2, 'r', encoding='utf-8') as f2:
        l1 = f1.readlines()
        l2 = f2.readlines()
    diff = list(difflib.unified_diff(l2, l1, fromfile='pull (7.2.0)', tofile='main (6.12.0 custom)', n=2))
    print(f"=== DIFF FOR {name} ({len(diff)} lines) ===")
    print(''.join(diff))

diff_files('C:/code/BrightTools/snippets/product-card.liquid', 'C:/code/BrightTools/worktrees/pull/snippets/product-card.liquid', 'product-card.liquid')
diff_files('C:/code/BrightTools/snippets/price-list.liquid', 'C:/code/BrightTools/worktrees/pull/snippets/price-list.liquid', 'price-list.liquid')
