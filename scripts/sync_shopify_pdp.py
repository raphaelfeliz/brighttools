import shutil

for f in ['templates/product.mar26-with-bundle-builder.json', 'templates/product.mar26.json']:
    src = 'C:/code/BrightTools/worktrees/pull/' + f
    dst = 'C:/code/BrightTools/' + f
    shutil.copy2(src, dst)
    print(f"Synced {f} from pull")
