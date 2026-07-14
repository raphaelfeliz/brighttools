# SOP: Convert Liquid to HTML Post-Mortem Pills

## 1. Regex Pitfalls with Style Tag Extraction
- **Issue**: Standard regex patterns like `re.findall(r"<style>(.*?)</style>", content, re.DOTALL)` can match prematurely if the word `<style>` appears inside Liquid comments prior to the actual CSS block.
- **Pill**: Avoid loose regex searches on files containing comments. Use exact line ranges or parser-based extraction to isolate `<style>` tags.

## 2. Liquid Template Expression Resolution
- **Issue**: Shopify Liquid variables (`{{ ... }}`) and logical tags (`{% if ... %}`) in CSS variables or attributes break standard browser styling engines.
- **Pill**: Cleanly parse and translate all Liquid logical branches and settings values into static CSS equivalents based on the target mock theme settings before writing to the HTML file.

## 3. Style Sheets and Layout Dependencies
- **Issue**: Custom component styles often rely on CSS variables declared in `theme.css` or global framework CSS that are not inlined in the local component CSS.
- **Pill**: Ensure `theme.css` and foundation style sheets are referenced via valid relative file paths (`../worktrees/main/assets/theme.css`) to preserve container grids and typography variables.
