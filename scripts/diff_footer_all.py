with open('C:/code/BrightTools/worktrees/pull/sections/footer.liquid', 'r', encoding='utf-8') as f:
    pull_footer = f.read()

import difflib
with open('C:/code/BrightTools/sections/footer.liquid', 'r', encoding='utf-8') as f:
    main_footer = f.read()

diff = list(difflib.unified_diff(pull_footer.splitlines(), main_footer.splitlines(), fromfile='pull', tofile='main', n=0))
for d in diff:
    if d.startswith('-') and not d.startswith('---'):
        print("PULL:", d)
    elif d.startswith('+') and not d.startswith('+++'):
        print("MAIN:", d)
