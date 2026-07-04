import re

with open('translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

replacement = r'''    "filter-all": "All Events",
    "filter-all-cand": "All Candidates",
    "filter-exec": "Executive",'''

content = re.sub(r'    "filter-all": "All Events",', replacement, content)

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(content)
