with open('C:/code/BrightTools/sections/header.liquid', 'r', encoding='utf-8') as f1, open('C:/code/BrightTools/worktrees/pull/sections/header.liquid', 'r', encoding='utf-8') as f2:
    l1 = f1.readlines()
    l2 = f2.readlines()

import difflib
# Look for differences beyond line 100
d = list(difflib.unified_diff(l2[100:], l1[100:], fromfile='pull', tofile='main', n=2))
print(''.join(d[:80]))
