import os

# to auto update the readme with newly pushed wallpapers
output_file = "WALLPAPER_GALLERY.md"
images = [
    f
    for f in os.listdir(".")
    if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".gif"))
]

images.sort()
cols = 3
rows = [images[i : i + cols] for i in range(0, len(images), cols)]

with open(output_file, "w") as f:
    for i, row in enumerate(rows):
        row_md = "| " + " | ".join(f"![]({img})" for img in row) + " |\n"
        if i == 0:
            sep = "| " + " | ".join(["---"] * len(row)) + " |\n"
            f.write(sep + row_md)
        else:
            f.write(row_md)
