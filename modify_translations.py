import re

with open('translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

replacement = r'''    "ev-desc-24": \1,
    "filter-all": "All Events",
    "filter-pres": "Presidential",
    "filter-gov": "Governors",
    "filter-list": "Party List",
    "filter-senate": "Senate",
    "filter-house": "House",
    "ev-title-gov-1": "Reno Governor Debate",
    "ev-desc-gov-1": "Watch Safiya debate on key issues concerning the future of Reno.",
    "ev-title-gov-2": "Reno Community Townhall",
    "ev-desc-gov-2": "An open discussion on local community initiatives and economic growth.",
    "ev-title-gov-3": "Final Reno Rally",
    "ev-desc-gov-3": "The final major rally for the Reno Governor campaign. Stand with Safiya!"'''

content = re.sub(r'    "ev-desc-24": (.*)', replacement, content)

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(content)
