with open('C:/code/BrightTools/worktrees/pull/assets/theme.css', 'r', encoding='utf-8') as f:
    pull_css = f.read()

custom_prefix = """/* Tighten space below tags above product title (forced in main theme.css) */
.mar26-title-tags {
  margin-bottom: 0.1em !important;
}
.product-info__title {
  margin-top: 0 !important;
}
@media screen and (max-width: 999px) {
  .product-info__block-item {
    padding-left: 0 !important;
    padding-right: 0 !important;
    padding-inline: 0 !important;
  }
}
"""

new_css = custom_prefix + pull_css
with open('C:/code/BrightTools/assets/theme.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(new_css)
print('Successfully merged assets/theme.css with 7.2.0 base + custom styles.')
