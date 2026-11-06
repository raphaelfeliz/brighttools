import json, re

def strip_comments(text):
    return re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)

for f in ['templates/product.caravan-c-b-page.json', 'templates/product.mar26-caravan-bundle-page.json']:
    with open('C:/code/BrightTools/' + f, 'r', encoding='utf-8') as f1, open('C:/code/BrightTools/worktrees/pull/' + f, 'r', encoding='utf-8') as f2:
        d1 = json.loads(strip_comments(f1.read()))
        d2 = json.loads(strip_comments(f2.read()))
    print(f, "MAIN sections:", list(d1.get('sections', {}).keys()))
    print(f, "PULL sections:", list(d2.get('sections', {}).keys()))
