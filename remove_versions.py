import os
import glob

directory = "z:/ISP/color&design phase/"
html_files = glob.glob(os.path.join(directory, "*.html"))

files_to_remove = ["version6_luxury.html", "version7_hud.html", "version11_wireframe.html"]

strings_to_remove = [
    '<a href="version6_luxury.html" class="px-3 py-2 text-neutral-600 hover:bg-indigo-50 hover:text-indigo-600 rounded-lg transition-colors">Version 6 Luxury</a>\n',
    '<a href="version7_hud.html" class="px-3 py-2 text-neutral-600 hover:bg-indigo-50 hover:text-indigo-600 rounded-lg transition-colors">Version 7 HUD</a>\n',
    '<a href="version11_wireframe.html" class="px-3 py-2 text-neutral-600 hover:bg-indigo-50 hover:text-indigo-600 rounded-lg transition-colors">Version 11 Wireframe</a>\n',
    '<a href="version6_luxury.html" class="px-3 py-2 text-neutral-600 hover:bg-indigo-50 hover:text-indigo-600 rounded-lg transition-colors">Version 6 Luxury</a>',
    '<a href="version7_hud.html" class="px-3 py-2 text-neutral-600 hover:bg-indigo-50 hover:text-indigo-600 rounded-lg transition-colors">Version 7 HUD</a>',
    '<a href="version11_wireframe.html" class="px-3 py-2 text-neutral-600 hover:bg-indigo-50 hover:text-indigo-600 rounded-lg transition-colors">Version 11 Wireframe</a>'
]

# Process each html file to remove links
for file in html_files:
    if os.path.basename(file) in files_to_remove:
        continue

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    for s in strings_to_remove:
        indented_s = "            " + s
        if indented_s in content:
            content = content.replace(indented_s, "")
        elif s in content:
            content = content.replace(s, "")

    # Cleanup empty lines left behind if any
    content = '\n'.join([line for line in content.split('\n') if line.strip() != ""])

    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in {file}")

# Delete the actual files
for f_name in files_to_remove:
    path = os.path.join(directory, f_name)
    if os.path.exists(path):
        os.remove(path)
        print(f"Deleted {f_name}")
