import markdown
from markdown.extensions.tables import TableExtension
text = "Some Markdown text with table syntax..."
html = markdown.markdown(text, extensions=[TableExtension(use_align_attribute=True)])
