with open('C:/code/BrightTools/sections/header.liquid', 'r', encoding='utf-8') as f1, open('C:/code/BrightTools/worktrees/pull/sections/header.liquid', 'r', encoding='utf-8') as f2:
    t1 = f1.read()
    t2 = f2.read()

# Let's inspect differences in footer.liquid as well
with open('C:/code/BrightTools/sections/footer.liquid', 'r', encoding='utf-8') as f1, open('C:/code/BrightTools/worktrees/pull/sections/footer.liquid', 'r', encoding='utf-8') as f2:
    f1_txt = f1.read()
    f2_txt = f2.read()

import difflib
diff_f = list(difflib.unified_diff(f2_txt.splitlines(True)[200:], f1_txt.splitlines(True)[200:], fromfile='pull', tofile='main', n=2))
print("Footer diff beyond 200 lines:")
print(''.join(diff_f[:100]))
