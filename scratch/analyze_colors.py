import re

file_path = r"c:\Users\DELL\python\Ride Share\demo\demo\myproject\static\css\bootstrap.min-1.css"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all hex colors
hex_colors = set(re.findall(r"#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}", content))

print("Found hex colors:")
for color in sorted(hex_colors):
    # Parse RGB components
    c = color.lstrip('#')
    if len(c) == 3:
        c = "".join([x*2 for x in c])
    try:
        r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
        # Simple heuristic for orange: high red, medium green, low blue
        if r > 180 and g > 50 and g < 150 and b < 50:
            print(f"Orange-like: {color} (R:{r}, G:{g}, B:{b})")
    except Exception as e:
        pass
