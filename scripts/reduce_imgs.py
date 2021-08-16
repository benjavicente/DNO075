import subprocess
from pathlib import Path
import sys

def main(size = "600x800", *, bg_color = "black"):
    for img_path in Path.cwd().glob("**/*"):
        if not img_path.suffix.endswith(("png", "jpg", "gif")):
            continue

        subprocess.run([
          "convert",
          img_path.resolve(),
          "-quality", "80",
          "-define", "png:compression-level=9",
          "-define", "png:compression-filter=5",
          "-define", "png:compression-strategy=1",
          "-resize", size,
          "-background", bg_color,
          "-gravity", "center",
          "-extent", size,
          img_path.resolve()
        ])

if __name__ =="__main__":
    main(*sys.argv[1:])
