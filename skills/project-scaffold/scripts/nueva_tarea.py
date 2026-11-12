#!/usr/bin/env python3
"""Crea una tarea ODD (Documentacion/odd/tasks/NNN-slug.md) a partir de la plantilla.

La numeración es compartida con las specs SDD (Documentacion/specs/NNN-*), sin colisiones.
Ejemplo: python3 nueva_tarea.py --nombre "migrar sesiones" --ruta ~/proyectos/mi-api --autor "Ana"
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
NUM = re.compile(r"^(\d{3})-")


def slugify(texto: str) -> str:
    ascii_text = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")


def next_number(*carpetas: Path) -> str:
    numeros = [int(m.group(1)) for c in carpetas if c.is_dir()
               for e in c.iterdir() if (m := NUM.match(e.name))]
    return f"{max(numeros, default=0) + 1:03d}"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nombre", required=True, help="nombre de la tarea")
    p.add_argument("--ruta", default=".", help="raíz del proyecto (por defecto, el directorio actual)")
    p.add_argument("--autor", help="autor del registro")
    args = p.parse_args()

    docs = Path(args.ruta).expanduser().resolve() / "Documentacion"
    if not docs.is_dir():
        sys.exit(f"Error: no existe '{docs}'. Ejecuta primero scaffold.py o indica --ruta.")
    slug = slugify(args.nombre)
    if not slug:
        sys.exit("Error: el nombre debe contener letras o números.")
    tasks = docs / "odd" / "tasks"
    tasks.mkdir(parents=True, exist_ok=True)

    numero = next_number(tasks, docs / "specs")
    propia = docs / "odd" / "_plantillas" / "tarea.md"
    plantilla = propia if propia.exists() else SKILL_ROOT / "templates" / "odd" / "tarea.md"
    texto = (plantilla.read_text(encoding="utf-8").replace("NNN", numero)
             .replace("<nombre de la tarea>", args.nombre)
             .replace("<AAAA-MM-DD>", date.today().isoformat()))
    if args.autor:
        texto = texto.replace("Autor: <nombre>", f"Autor: {args.autor}")
    destino = tasks / f"{numero}-{slug}.md"
    destino.write_text(texto, encoding="utf-8")
    print(f"Tarea creada en: {destino}")


if __name__ == "__main__":
    main()
