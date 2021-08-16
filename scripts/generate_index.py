"Generador de un index.html para el repositorio"

from pathlib import Path
from dataclasses import dataclass

import jinja2

JINJA_TEMPLATE_OPTIONS = dict(
  trim_blocks=True,
  lstrip_blocks=True
)


with Path(__file__).parent.joinpath("index.html.jinja").open() as file:
    INDEX_TEMPLATE = jinja2.Template(file.read(), **JINJA_TEMPLATE_OPTIONS)

@dataclass
class Entrega:
    href: str
    text: str

def main():
    entregas = []
    for dir_entrega in Path("entregas").glob("*/"):
        if not dir_entrega.is_dir(): continue
        text = dir_entrega.name.split("-", maxsplit=1)[1]
        href = dir_entrega.resolve().relative_to(Path.cwd())
        entregas.append(Entrega(href.as_posix(), text))
    output = INDEX_TEMPLATE.render(entregas=entregas)
    with Path("index.html").open("w") as file:
        file.write(output)

if __name__ == "__main__":
    main()
