with open('C:/code/BrightTools/layout/theme.liquid', 'r', encoding='utf-8') as f1, open('C:/code/BrightTools/worktrees/pull/layout/theme.liquid', 'r', encoding='utf-8') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

import difflib
diff = list(difflib.unified_diff(lines2, lines1, fromfile='pull (7.2.0)', tofile='main (6.12.0 custom)', n=2))
print(''.join(diff))
