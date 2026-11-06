import difflib

def diff_files(p1, p2, name):
    with open(p1, 'r', encoding='utf-8') as f1, open(p2, 'r', encoding='utf-8') as f2:
        l1 = f1.readlines()
        l2 = f2.readlines()
    diff = list(difflib.unified_diff(l2, l1, fromfile='pull (7.2.0)', tofile='main (6.12.0)', n=2))
    print(f"=== DIFF FOR {name} ({len(diff)} lines) ===")
    print(''.join(diff[:120]))

diff_files('C:/code/BrightTools/sections/header.liquid', 'C:/code/BrightTools/worktrees/pull/sections/header.liquid', 'header.liquid')
diff_files('C:/code/BrightTools/sections/footer.liquid', 'C:/code/BrightTools/worktrees/pull/sections/footer.liquid', 'footer.liquid')
