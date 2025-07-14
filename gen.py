import os

## to auto update the readme with newly pushed wallpapers
output_file = "WALLPAPER_GALLERY.md"
images = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

images.sort()
cols = 3
rows = [images[i:i + cols] for i in range(0, len(images), cols)]

with open(output_file, "w") as f:
    f.write("## Wallpaper Gallery\n\n")
    for row in rows:
        sep = "| " + " | ".join(["---"] * len(row)) + " |\n"
        row_md = "| " + " | ".join(f"![]({img})" for img in row) + " |\n"
        f.write(sep + row_md)

