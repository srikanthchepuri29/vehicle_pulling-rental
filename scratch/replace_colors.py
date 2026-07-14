import os

css_dir = r"c:\Users\DELL\python\Ride Share\demo\demo\myproject\static\css"

replacements = {
    "#F77D0A": "#007bff",
    "#f77d0a": "#007bff",
    "#d46a07": "#0069d9",
    "#D46A07": "#0069d9",
    "#c76407": "#0062cc",
    "#C76407": "#0062cc",
    "#bb5e06": "#0056b3",
    "#BB5E06": "#0056b3",
    # Additional common orange shades if any
    "247, 125, 10": "0, 123, 255", # RGB orange to blue
}

for root, dirs, files in os.walk(css_dir):
    for file in files:
        if file.endswith(".css"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                modified = False
                for orange, blue in replacements.items():
                    if orange in content:
                        content = content.replace(orange, blue)
                        modified = True
                        print(f"Replaced {orange} with {blue} in {file}")
                
                if modified:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
            except Exception as e:
                print(f"Error processing {file}: {e}")

print("All CSS files processed.")
