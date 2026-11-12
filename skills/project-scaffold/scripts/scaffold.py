#!/usr/bin/env python3
"""Crea un proyecto con estructura estandarizada y carpeta Documentacion.

Multiplataforma (Windows, Linux, macOS); solo usa la biblioteca estándar.
Ejemplo: python3 scaffold.py --nombre mi-api --backend java --frontend angular --ruta ~/proyectos
"""
import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent

BACKENDS = ("java", "python", "node", "dotnet")
FRONTENDS = ("angular", "vue", "react")
FULLSTACKS = ("java-web", "dotnet-web", "python-web", "node-web")

DOC_SUBDIRS = {
    "backend": ("arquitectura", "api", "base-de-datos", "decisiones", "guias", "operaciones", "pruebas"),
    "frontend": ("arquitectura", "componentes", "diseno-ui", "decisiones", "guias", "pruebas"),
}

SDD_DIR = SKILL_ROOT / "templates" / "sdd"
SDD_TEMPLATES = ("spec.md", "plan.md", "tareas.md")
ODD_DIR = SKILL_ROOT / "templates" / "odd"
METODOLOGIAS = ("sdd", "odd", "ambas", "ninguna")


def new_dir(path: Path, keep: bool = False) -> None:
    path.mkdir(parents=True, exist_ok=True)
    if keep:
        (path / ".gitkeep").touch()


def pascal_case(nombre: str) -> str:
    return "".join(p[:1].upper() + p[1:] for p in re.split(r"[^A-Za-z0-9]+", nombre) if p)


def read_dirs(stack: str, slug: str, pascal: str) -> list[str]:
    dirs_file = SKILL_ROOT / "structures" / f"{stack}.dirs"
    if not dirs_file.exists():
        sys.exit(f"Error: no existe la estructura '{stack}'.")
    lines = (ln.strip() for ln in dirs_file.read_text(encoding="utf-8").splitlines())
    return [ln.replace("{{nombre}}", slug).replace("{{Nombre}}", pascal)
            for ln in lines if ln and not ln.startswith("#")]


def build_layer(stack: str, tipo: str, base: Path, docs_root: Path, slug: str, pascal: str) -> None:
    for rel in read_dirs(stack, slug, pascal):
        new_dir(base / rel, keep=True)

    tipos = ("backend", "frontend") if tipo == "fullstack" else (tipo,)
    for t in tipos:
        for sub in DOC_SUBDIRS[t]:
            new_dir(docs_root / t / sub, keep=True)

    prop_dir = docs_root if tipo == "fullstack" else docs_root / tipo
    shutil.copyfile(SKILL_ROOT / "proposals" / f"{stack}.md", prop_dir / f"estructura-{stack}.md")


def build_specs(docs_root: Path, nombre: str) -> None:
    """Crea Documentacion/specs con la guía SDD, la constitución y las plantillas."""
    specs = docs_root / "specs"
    plantillas = specs / "_plantillas"
    new_dir(plantillas)
    shutil.copyfile(SKILL_ROOT / "references" / "sdd.md", specs / "README.md")
    for name in SDD_TEMPLATES:
        shutil.copyfile(SDD_DIR / name, plantillas / name)
    constitucion = (SDD_DIR / "constitucion.md").read_text(encoding="utf-8")
    constitucion = constitucion.replace("{{proyecto}}", nombre).replace("{{fecha}}", date.today().isoformat())
    (specs / "constitucion.md").write_text(constitucion, encoding="utf-8")


def build_odd(docs_root: Path) -> None:
    """Crea Documentacion/odd con la guía ODD, la plantilla de tarea y tasks/."""
    odd = docs_root / "odd"
    new_dir(odd / "_plantillas")
    new_dir(odd / "tasks", keep=True)
    shutil.copyfile(SKILL_ROOT / "references" / "odd.md", odd / "README.md")
    shutil.copyfile(ODD_DIR / "tarea.md", odd / "_plantillas" / "tarea.md")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nombre", required=True, help="nombre del proyecto")
    p.add_argument("--backend", choices=BACKENDS)
    p.add_argument("--frontend", choices=FRONTENDS)
    p.add_argument("--fullstack", choices=FULLSTACKS, help="un solo proyecto; no se combina con --backend/--frontend")
    p.add_argument("--ruta", default=".", help="directorio destino (por defecto, el actual)")
    p.add_argument("--force", action="store_true", help="permite usar una carpeta destino no vacía")
    p.add_argument("--metodologia", choices=METODOLOGIAS, default="sdd",
                   help="flujo de trabajo: sdd (specs), odd (tareas ligeras), ambas o ninguna (por defecto, sdd)")
    p.add_argument("--sin-sdd", action="store_true", help="obsoleto: quita SDD (equivale a --metodologia odd/ninguna)")
    args = p.parse_args()
    if not (args.backend or args.frontend or args.fullstack):
        p.error("indica --backend, --frontend o --fullstack.")
    if args.fullstack and (args.backend or args.frontend):
        p.error("--fullstack no se combina con --backend ni --frontend.")
    if args.sin_sdd:
        args.metodologia = {"sdd": "ninguna", "ambas": "odd"}.get(args.metodologia, args.metodologia)
    return args


def main() -> None:
    args = parse_args()
    root = Path(args.ruta).expanduser().resolve() / args.nombre
    if root.exists() and any(root.iterdir()) and not args.force:
        sys.exit(f"Error: la carpeta '{root}' ya existe y no está vacía. Usa --force para continuar.")

    slug = re.sub(r"[^a-z0-9]", "", args.nombre.lower())
    pascal = pascal_case(args.nombre)
    docs_root = root / "Documentacion"
    new_dir(docs_root)

    both = bool(args.backend and args.frontend)
    index = [f"# Documentacion de {args.nombre}", "", f"Creado: {date.today().isoformat()}", ""]

    if args.backend:
        build_layer(args.backend, "backend", root / "backend" if both else root, docs_root, slug, pascal)
        index.append(f"- [Backend ({args.backend})](backend/estructura-{args.backend}.md)")
    if args.frontend:
        build_layer(args.frontend, "frontend", root / "frontend" if both else root, docs_root, slug, pascal)
        index.append(f"- [Frontend ({args.frontend})](frontend/estructura-{args.frontend}.md)")
    if args.fullstack:
        build_layer(args.fullstack, "fullstack", root, docs_root, slug, pascal)
        index.append(f"- [Fullstack ({args.fullstack})](estructura-{args.fullstack}.md)")
        index.append("- Documentación de backend: `backend/`; de frontend: `frontend/`")
    if args.metodologia in ("sdd", "ambas"):
        build_specs(docs_root, args.nombre)
        index.append("- [Specs (SDD)](specs/README.md): [constitución](specs/constitucion.md), plantillas en `specs/_plantillas/`")
    if args.metodologia in ("odd", "ambas"):
        build_odd(docs_root)
        index.append("- [Tareas (ODD)](odd/README.md): registros en `odd/tasks/`, plantilla en `odd/_plantillas/`")

    (docs_root / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"Proyecto creado en: {root}")


if __name__ == "__main__":
    main()
