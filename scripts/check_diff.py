with open('C:/code/BrightTools/assets/theme.css', 'rb') as f1, open('C:/code/BrightTools/worktrees/pull/assets/theme.css', 'rb') as f2:
    t1 = f1.read().replace(b'\r\n', b'\n')
    t2 = f2.read().replace(b'\r\n', b'\n')
    print('Length local:', len(t1), 'Length pull:', len(t2))
    if t1 == t2:
        print('Files are byte-identical after LF normalization!')
    else:
        import difflib
        diff = list(difflib.unified_diff(t2.decode('utf-8', errors='ignore').splitlines(), t1.decode('utf-8', errors='ignore').splitlines(), fromfile='pull', tofile='main', n=2))
        print('\n'.join(diff[:50]))
