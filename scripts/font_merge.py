from fontTools.merge import Merger
from fontTools.ttLib import TTFont

# List your font files in priority order (first wins for duplicates)
font_paths = [
    "../assets/NotoSans-Regular.ttf",
    "../assets/NotoSansJP-Regular.ttf",
    "../assets/NotoSansKR-Regular.ttf",
    "../assets/NotoSansSC-Regular.ttf"
]

# Output path
output_path = "../assets/NotoSans-Merged.ttf"

# Merge fonts
merger = Merger()
merged = merger.merge(font_paths)

# Save merged font
merged.save(output_path)
print(f"Merged font saved to: {output_path}")
