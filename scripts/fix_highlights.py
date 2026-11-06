for f in ['templates/product.mar26-with-bundle-builder.json', 'templates/product.mar26.json']:
    path = 'C:/code/BrightTools/' + f
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Wrap bare text in <p>...</p> for rich_text schema compliance in Shopify 7.2.0
    if f == 'templates/product.mar26-with-bundle-builder.json':
        old = '"highlight_3": "Machine washable up to 100 times"'
        new = '"highlight_3": "<p>Machine washable up to 100 times</p>"'
    else:
        old = '"highlight_3": "Non-stick bristles"'
        new = '"highlight_3": "<p>Non-stick bristles</p>"'
    
    assert old in content, f"Could not find {old} in {f}"
    content = content.replace(old, new)
    with open(path, 'w', encoding='utf-8', newline='\n') as file:
        file.write(content)
    print(f"Fixed {f}")
