with open('C:/code/BrightTools/templates/product.bt-brooms.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(43, 54):
    print(lines[i], end='')
