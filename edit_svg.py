import re

with open("Rose.SVG", "r", encoding="utf-8") as f:
    svg = f.read()

# I want to delete path15 (black) and path16 (white straight lines - text).
# And I want to keep path1 (the curved rose) but change its fill to #ffffff.

# Delete path15
svg = re.sub(r'<path[^>]*id="path15"[^>]*/>', '', svg, flags=re.DOTALL)
# Delete path16
svg = re.sub(r'<path[^>]*id="path16"[^>]*/>', '', svg, flags=re.DOTALL)

# Change path1 fill to white
svg = re.sub(r'fill:#d7003a', r'fill:#ffffff', svg)

with open("Rose.SVG", "w", encoding="utf-8") as f:
    f.write(svg)

print("SVG edited.")
