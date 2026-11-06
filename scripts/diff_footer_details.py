with open('C:/code/BrightTools/worktrees/pull/sections/footer.liquid', 'r', encoding='utf-8') as f:
    pull_footer = f.read()

import difflib
with open('C:/code/BrightTools/sections/footer.liquid', 'r', encoding='utf-8') as f:
    main_footer = f.read()

diff = list(difflib.unified_diff(pull_footer.splitlines(), main_footer.splitlines(), fromfile='pull', tofile='main', n=1))
print("Differences count:", len(diff))
# Print unique lines in pull
pull_only = [line for line in diff if line.startswith('-') and not line.startswith('---')]
print("Pull only lines count:", len(pull_only))
for p in pull_only[:20]:
    print("PULL ONLY:", p)
