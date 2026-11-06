import re

for f in ['templates/product.mar26-with-bundle-builder.json', 'templates/product.mar26.json']:
    path = 'C:/code/BrightTools/' + f
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Function to wrap in <p> if not already wrapped
    def wrap_p(match):
        key = match.group(1)
        val = match.group(2)
        if not val.startswith('<p>'):
            val = f'<p>{val}</p>'
        return f'"{key}": "{val}"'

    content = re.sub(r'"(highlight_[123])":\s*"([^"]+)"', wrap_p, content)
    with open(path, 'w', encoding='utf-8', newline='\n') as file:
        file.write(content)
    print(f"Ensured p tags for {f}")
