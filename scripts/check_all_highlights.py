for f in ['templates/product.mar26-with-bundle-builder.json', 'templates/product.mar26.json']:
    with open('C:/code/BrightTools/' + f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for i in range(35, 52):
        print(f"{f} line {i+1}: {lines[i]}", end='')
