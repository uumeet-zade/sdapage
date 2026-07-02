import re

with open("SDAlogo.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# We only want to keep path1 (the red rose).
# We delete path15 (text) and path16 (background/outline).
svg = re.sub(r'<path[^>]*id="path15"[^>]*/>', '', svg, flags=re.DOTALL)
svg = re.sub(r'<path[^>]*id="path16"[^>]*/>', '', svg, flags=re.DOTALL)

with open("Rose.SVG", "w", encoding="utf-8") as f:
    f.write(svg)

print("Restored rose.")
