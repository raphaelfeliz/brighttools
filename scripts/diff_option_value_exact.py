with open('C:/code/BrightTools/snippets/option-value.liquid', 'r', encoding='utf-8') as f1, open('C:/code/BrightTools/worktrees/pull/snippets/option-value.liquid', 'r', encoding='utf-8') as f2:
    main_ov = f1.read()
    pull_ov = f2.read()

import difflib
diff = list(difflib.unified_diff(pull_ov.splitlines(True), main_ov.splitlines(True), fromfile='pull', tofile='main', n=2))
print(''.join(diff))
