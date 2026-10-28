#!/usr/bin/env python3
"""Valida las specs SDD (spec.md, plan.md, tareas.md) antes de avanzar de fase.

Multiplataforma (Windows, Linux, macOS); solo usa la biblioteca estándar.
Ejemplos:
  python3 validar_spec.py Documentacion/specs/001-login --fase plan
  python3 validar_spec.py ~/proyectos/mi-api          # todas las features del proyecto
Fases: spec (solo la spec), plan (spec aprobada y lista para planear), tareas (plan listo), implementar (tareas listas).
Código de salida 1 si hay errores.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FASES = ("spec", "plan", "tareas", "implementar")
ESTADOS_APROBADOS = ("aprobada", "en implementación", "en implementacion", "implementada")
REQ_ID = re.compile(r"\bRN?F-\d{3}\b")
REQ_ROW = re.compile(r"^\|\s*(RN?F-\d{3})\s*\|[^|]*\|\s*([^|]*?)\s*\|", re.M)
STORY = re.compile(r"^###\s+(H\d+)\b.*?(?=^###\s|^##\s|\Z)", re.M | re.S)
CRITERIO = re.compile(r"dado\b.*\bcuando\b.*\bentonces\b|\bcuando\b.*\bdebe\b", re.I)
PLACEHOLDER = re.compile(r"<[^<>\n]{2,80}>")
TASK = re.compile(r"^- \[([ xX])\]\s+(T\d{3})\b(.*)$", re.M)


class Reporte:
    def __init__(self, nombre: str) -> None:
        self.nombre, self.errores, self.avisos, self.info = nombre, [], [], []

    def imprimir(self) -> None:
        print(f"\n== {self.nombre} ==")
        for prefijo, items in (("ERROR", self.errores), ("AVISO", self.avisos), ("INFO", self.info)):
            for item in items:
                print(f"  [{prefijo}] {item}")
        if not (self.errores or self.avisos):
            print("  OK")


def sin_codigo(texto: str) -> str:
    texto = re.sub(r"```.*?```", "", texto, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", texto)


def seccion(texto: str, titulo: str) -> str:
    m = re.search(rf"^##\s+{titulo}.*?(?=^##\s|\Z)", texto, re.M | re.S | re.I)
    return m.group(0) if m else ""


def revisar_placeholders(texto: str, archivo: str, rep: Reporte) -> None:
    pendientes = PLACEHOLDER.findall(sin_codigo(texto))
    if pendientes:
        rep.avisos.append(f"{archivo}: {len(pendientes)} marcadores sin completar (p. ej. {pendientes[0]})")


def validar_spec(texto: str, fase: str | None, rep: Reporte) -> tuple[set[str], bool]:
    limpio = sin_codigo(texto)
    dudas = limpio.count("[POR ACLARAR")
    if dudas:
        rep.errores.append(f"spec.md: {dudas} [POR ACLARAR] sin resolver")
    reqs = dict(REQ_ROW.findall(limpio))
    if not reqs:
        rep.errores.append("spec.md: no hay requisitos RF-/RNF- en la tabla de requisitos")
    historias = {m.group(1): m.group(0) for m in STORY.finditer(limpio)}
    if not historias:
        rep.errores.append("spec.md: no hay historias de usuario (### H1 …)")
    for hid, cuerpo in historias.items():
        if not CRITERIO.search(cuerpo):
            rep.errores.append(f"spec.md: {hid} sin criterio Dado/Cuando/Entonces o CUANDO…DEBE")
    for rid, historia in reqs.items():
        if rid.startswith("RF-") and historia not in historias:
            rep.errores.append(f"spec.md: {rid} no está ligado a una historia existente ('{historia or '—'}')")
    if not re.search(r"\w", seccion(limpio, "Fuera de alcance").partition("\n")[2]):
        rep.avisos.append("spec.md: sección 'Fuera de alcance' vacía")
    m = re.search(r"Estado:\s*([^\n·|]+)", texto)
    estado = m.group(1).strip() if m else "desconocido"
    rep.info.append(f"estado de la spec: {estado}")
    if fase and fase != "spec" and estado.lower() not in ESTADOS_APROBADOS:
        rep.errores.append(f"spec.md: estado '{estado}'; debe estar 'Aprobada' para avanzar a {fase}")
    revisar_placeholders(texto, "spec.md", rep)
    return set(reqs), estado.lower() in ESTADOS_APROBADOS


def validar_plan(texto: str, reqs: set[str], rep: Reporte) -> None:
    limpio = sin_codigo(texto)
    for fila in re.findall(r"^\|([^|\n]+)\|([^|\n]*)\|", seccion(limpio, "Verificación contra"), re.M):
        principio, cumple = fila[0].strip(), fila[1].strip()
        if principio and principio != "Principio" and not set(principio) <= set("-: ") and not cumple:
            rep.avisos.append(f"plan.md: principio '{principio}' sin verificar contra la constitución")
    pruebas = seccion(limpio, "Estrategia de pruebas")
    for rid in sorted(r for r in reqs if r.startswith("RF-") and r not in pruebas):
        rep.errores.append(f"plan.md: {rid} sin prueba en 'Estrategia de pruebas'")
    revisar_placeholders(texto, "plan.md", rep)


def validar_tareas(texto: str, reqs: set[str], rep: Reporte) -> None:
    tareas = TASK.findall(sin_codigo(texto))
    if not tareas:
        rep.errores.append("tareas.md: no hay tareas con formato '- [ ] T001 …'")
        return
    vistos, cubiertos = set(), set()
    for _, tid, resto in tareas:
        if tid in vistos:
            rep.errores.append(f"tareas.md: {tid} duplicada")
        vistos.add(tid)
        if "Req:" not in resto:
            rep.errores.append(f"tareas.md: {tid} sin 'Req:' (usa 'Req: —' si no cubre un requisito)")
        if "Hecho cuando:" not in resto:
            rep.errores.append(f"tareas.md: {tid} sin 'Hecho cuando:'")
        ids = set(REQ_ID.findall(resto.split("Hecho cuando:")[0]))
        for rid in sorted(ids - reqs):
            rep.errores.append(f"tareas.md: {tid} referencia {rid}, que no existe en la spec")
        cubiertos |= ids
    for rid in sorted(r for r in reqs if r.startswith("RF-") and r not in cubiertos):
        rep.errores.append(f"tareas.md: {rid} no lo cubre ninguna tarea")
    hechas = sum(1 for marca, _, _ in tareas if marca.lower() == "x")
    rep.info.append(f"progreso: {hechas}/{len(tareas)} tareas completadas")
    revisar_placeholders(texto, "tareas.md", rep)


def validar_feature(carpeta: Path, fase: str | None) -> Reporte:
    rep = Reporte(carpeta.name)
    leer = lambda n: (carpeta / n).read_text(encoding="utf-8") if (carpeta / n).exists() else None
    spec, plan, tareas = leer("spec.md"), leer("plan.md"), leer("tareas.md")
    if spec is None:
        rep.errores.append("falta spec.md")
        return rep
    reqs, aprobada = validar_spec(spec, fase, rep)
    if fase is None:
        # Sin fase: una spec en borrador aún no tiene plan ni tareas que revisar (solo plantillas).
        nivel = len(FASES) if aprobada else 0
    else:
        nivel = FASES.index(fase)
    for idx, nombre, texto, validar in ((2, "plan.md", plan, validar_plan), (3, "tareas.md", tareas, validar_tareas)):
        if texto is not None and nivel >= idx:
            validar(texto, reqs, rep)
        elif fase and nivel >= idx:
            rep.errores.append(f"falta {nombre} para avanzar a {fase}")
    return rep


def features(ruta: Path) -> list[Path]:
    if (ruta / "spec.md").exists():
        return [ruta]
    specs = ruta / "Documentacion" / "specs" if (ruta / "Documentacion").is_dir() else ruta
    return sorted(d for d in specs.glob("[0-9][0-9][0-9]-*") if d.is_dir())


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("ruta", nargs="?", default=".", help="carpeta de una feature, Documentacion/specs o raíz del proyecto")
    p.add_argument("--fase", choices=FASES, help="fase a la que se quiere avanzar (sin fase: valida lo que exista)")
    args = p.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    carpetas = features(Path(args.ruta).expanduser().resolve())
    if not carpetas:
        sys.exit(f"Error: no se encontraron features SDD en '{args.ruta}'.")
    reportes = [validar_feature(c, args.fase) for c in carpetas]
    for rep in reportes:
        rep.imprimir()
    errores = sum(len(r.errores) for r in reportes)
    print(f"\nResultado: {errores} errores, {sum(len(r.avisos) for r in reportes)} avisos.")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
