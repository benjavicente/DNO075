import subprocess
from pathlib import Path
import sys


CWD = str(Path.cwd())
STATIC_IMG_STRATEGY = [
    "-quality", "80",
    "-define", "png:compression-level=9",
    "-define", "png:compression-filter=5",
    "-define", "png:compression-strategy=1",
]
GIF_STRATEGY = ["-coalesce", "-deconstruct"]

def main(path=CWD, size="600x800", bg_color="white"):
    for img_path in Path(path).glob("**/*"):
        if not img_path.suffix.endswith(("png", "jpg", "gif")):
            continue

        print(f"Compresing {img_path}")
        is_static = img_path.suffix.endswith(("png", "jpg"))

        subprocess.run([
          "convert",
          img_path.resolve(),
          *([GIF_STRATEGY[0]] if not is_static else []),
          *(STATIC_IMG_STRATEGY if is_static else []),
          "-resize", size,
          "-background", bg_color,
          "-gravity", "center",
          "-extent", size,
          *([GIF_STRATEGY[1]] if not is_static else []),
          img_path.resolve()
        ])

if __name__ =="__main__":
    main(*sys.argv[1:])
