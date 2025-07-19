import os

output_file = "WALLPAPER_GALLERY.md"
images = sorted(
    [
        f
        for f in os.listdir(".")
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".gif"))
    ]
)

cols = 3
rows = [images[i : i + cols] for i in range(0, len(images), cols)]

with open(output_file, "w") as f:
    f.write("## Wallpaper Gallery\n\n")

    f.write("| " + " | ".join([" "] * cols) + " |\n")
    f.write("| " + " | ".join(["---"] * cols) + " |\n")

    for row in rows:
        row_md = "| " + " | ".join(f"![]({img})" for img in row) + " |\n"
        f.write(row_md)
