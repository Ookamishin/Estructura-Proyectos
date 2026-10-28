#!/usr/bin/env python3
"""Crea la carpeta de una feature SDD (Documentacion/specs/NNN-nombre) con spec, plan y tareas.

Multiplataforma (Windows, Linux, macOS); solo usa la biblioteca estándar.
Ejemplo: python3 nueva_spec.py --nombre "login de usuarios" --ruta ~/proyectos/mi-api --autor "Ana"
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
import unicodedata
from datetime import date
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ("spec.md", "plan.md", "tareas.md")
FEATURE_DIR = re.compile(r"^(\d{3})-")
INDEX_HEADING = "## Features (SDD)"


def slugify(texto: str) -> str:
    ascii_text = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")


def next_number(specs: Path) -> str:
    numeros = [int(m.group(1)) for d in specs.iterdir() if d.is_dir() and (m := FEATURE_DIR.match(d.name))]
    return f"{max(numeros, default=0) + 1:03d}"


def template_dir(specs: Path) -> Path:
    """Prefiere las plantillas del proyecto (pueden estar personalizadas) sobre las de la skill."""
    propias = specs / "_plantillas"
    if all((propias / t).exists() for t in TEMPLATES):
        return propias
    return SKILL_ROOT / "templates" / "sdd"


def fill(texto: str, numero: str, nombre: str, autor: str | None) -> str:
    texto = (texto.replace("NNN", numero)
                  .replace("<nombre de la feature>", nombre)
                  .replace("<AAAA-MM-DD>", date.today().isoformat()))
    return texto.replace("Autor: <nombre>", f"Autor: {autor}") if autor else texto


def update_index(docs_root: Path, carpeta: str, numero: str, nombre: str) -> None:
    index = docs_root / "README.md"
    lineas = index.read_text(encoding="utf-8").rstrip("\n").splitlines() if index.exists() else []
    if INDEX_HEADING not in lineas:
        lineas += ["", INDEX_HEADING, ""]
    lineas.append(f"- [{numero} {nombre}](specs/{carpeta}/spec.md)")
    index.write_text("\n".join(lineas) + "\n", encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nombre", required=True, help="nombre de la feature (p. ej. \"login de usuarios\")")
    p.add_argument("--ruta", default=".", help="raíz del proyecto (por defecto, el directorio actual)")
    p.add_argument("--autor", help="autor de los documentos")
    args = p.parse_args()

    docs_root = Path(args.ruta).expanduser().resolve() / "Documentacion"
    specs = docs_root / "specs"
    if not docs_root.is_dir():
        sys.exit(f"Error: no existe '{docs_root}'. Ejecuta primero scaffold.py o indica --ruta.")
    slug = slugify(args.nombre)
    if not slug:
        sys.exit("Error: el nombre debe contener letras o números.")
    specs.mkdir(exist_ok=True)

    numero = next_number(specs)
    carpeta = f"{numero}-{slug}"
    destino = specs / carpeta
    destino.mkdir()
    origen = template_dir(specs)
    for name in TEMPLATES:
        texto = (origen / name).read_text(encoding="utf-8")
        (destino / name).write_text(fill(texto, numero, args.nombre, args.autor), encoding="utf-8")
    if not (specs / "README.md").exists():
        shutil.copyfile(SKILL_ROOT / "references" / "sdd.md", specs / "README.md")

    update_index(docs_root, carpeta, numero, args.nombre)
    print(f"Feature creada en: {destino}")


if __name__ == "__main__":
    main()
