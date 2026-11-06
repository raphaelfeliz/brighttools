with open('C:/code/BrightTools/snippets/price-list.liquid', 'r', encoding='utf-8') as f1, open('C:/code/BrightTools/worktrees/pull/snippets/price-list.liquid', 'r', encoding='utf-8') as f2:
    main_pl = f1.read()
    pull_pl = f2.read()

import difflib
diff = list(difflib.unified_diff(pull_pl.splitlines(True), main_pl.splitlines(True), fromfile='pull', tofile='main', n=2))
print(''.join(diff))
