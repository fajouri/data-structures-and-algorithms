#!/usr/bin/env python3
"""Check one DSA session's deliverables and optionally exercise trusted code.

Standard-library only; no repository edits. Does not certify academic correctness.
"""

import argparse
import ast
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def run(cmd, cwd, timeout=60):
    try:
        result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, str(exc)
    detail = (result.stderr or result.stdout).strip()
    return result.returncode == 0, detail[-900:]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session", required=True, help="S01 through S20")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument("--execute", action="store_true", help="Run trusted examples/tests/notebooks")
    parser.add_argument("--require-lab", action="store_true", help="Require runnable lab code")
    args = parser.parse_args()

    if not re.fullmatch(r"S(?:0[1-9]|1[0-9]|20)", args.session):
        parser.error("--session must be S01..S20")
    root = args.root.resolve()
    folder = root / "sessions" / args.session
    errors, warnings, checks = [], [], []

    for relative in ("course-plan.md", "COURSE_STATUS.md"):
        if not (root / relative).is_file():
            errors.append(f"Missing course prerequisite: {relative}")
    if not list((root / "module-descriptor").glob("*.pdf")):
        errors.append("Missing official PDF: module-descriptor/*.pdf")
    if not folder.is_dir():
        errors.append(f"Missing session folder: sessions/{args.session}/")
    else:
        for name in ("README.md", "lecture.md", "exercises.md"):
            file = folder / name
            if not file.is_file() or not file.read_text(encoding="utf-8").strip():
                errors.append(f"Missing/empty: sessions/{args.session}/{name}")
            else:
                checks.append(f"Found {name}")

        slides_md, deck = folder / "slides.md", folder / "slides.pptx"
        if not slides_md.is_file() and not deck.is_file():
            errors.append("Missing slide deliverable: slides.md or slides.pptx")
        if slides_md.is_file():
            content = slides_md.read_text(encoding="utf-8")
            if not re.search(r"(?i)speaker\s+notes|teaching\s+notes", content):
                errors.append("slides.md has no recognisable speaker-notes sections")
            else:
                checks.append("slides.md contains speaker-note labels (content needs human review)")
        if deck.is_file():
            if not zipfile.is_zipfile(deck):
                errors.append("slides.pptx is not a valid PPTX/ZIP archive")
            else:
                with zipfile.ZipFile(deck) as zf:
                    notes = [n for n in zf.namelist() if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", n)]
                if not notes:
                    errors.append("slides.pptx contains no native speaker-note slides")
                else:
                    checks.append(f"slides.pptx has {len(notes)} native notes slide(s) (quality needs human review)")

        sources = sorted(p for p in folder.rglob("*") if p.is_file() and p.suffix in {".py", ".cpp", ".cc", ".cxx", ".ipynb"} and not any(s in {"solutions", "instructor-only", "__pycache__"} for s in p.parts))
        if args.require_lab and not sources:
            errors.append("A practical lab was requested, but no code or notebook was found")
        if not sources:
            warnings.append("No code/notebook found; confirm whether the approved plan requires a lab")

        compiler = shutil.which("g++") or shutil.which("clang++")
        for file in sources:
            relative = file.relative_to(root)
            if file.suffix == ".py":
                try:
                    ast.parse(file.read_text(encoding="utf-8"), filename=str(file))
                    checks.append(f"Python syntax: {relative}")
                except (SyntaxError, UnicodeError) as exc:
                    errors.append(f"Python syntax failure {relative}: {exc}")
            elif file.suffix == ".ipynb":
                try:
                    nb = json.loads(file.read_text(encoding="utf-8"))
                    cells = nb["cells"]
                    if not isinstance(cells, list) or not cells:
                        raise ValueError("no cells")
                    for i, cell in enumerate(cells, 1):
                        if cell.get("cell_type") != "code":
                            continue
                        src = cell.get("source", "")
                        code = "".join(src) if isinstance(src, list) else src
                        if any(line.lstrip().startswith(("%", "!")) for line in code.splitlines()):
                            warnings.append(f"Notebook cell {i} in {relative} uses shell/magic syntax; static check skipped")
                            continue
                        ast.parse(code, filename=f"{relative}:cell{i}")
                    checks.append(f"Notebook JSON/Python syntax: {relative}")
                except (ValueError, KeyError, TypeError, SyntaxError, UnicodeError) as exc:
                    errors.append(f"Notebook check failure {relative}: {exc}")
            else:
                if not compiler:
                    warnings.append(f"C++ not checked (compiler unavailable): {relative}")
                else:
                    ok, detail = run([compiler, "-std=c++17", "-Wall", "-Wextra", "-fsyntax-only", str(file)], root)
                    (checks if ok else errors).append(f"C++ syntax {'OK' if ok else 'FAIL'}: {relative} {detail if not ok else ''}".strip())

        if args.execute:
            examples = [p for p in sources if p.suffix == ".py" and "examples" in p.parts]
            for file in examples:
                ok, detail = run([sys.executable, str(file)], file.parent)
                (checks if ok else errors).append(f"Python example {'OK' if ok else 'FAIL'}: {file.relative_to(root)} {detail if not ok else ''}".strip())
            tests_dir = folder / "tests"
            if tests_dir.is_dir() and list(tests_dir.rglob("test_*.py")):
                ok, detail = run([sys.executable, "-m", "unittest", "discover", "-s", str(tests_dir), "-p", "test_*.py"], root)
                (checks if ok else errors).append(f"unittest {'OK' if ok else 'FAIL'}: {detail}")
            notebooks = [p for p in sources if p.suffix == ".ipynb"]
            if notebooks and not shutil.which("jupyter"):
                warnings.append("Notebooks not executed: Jupyter unavailable")
            elif notebooks:
                with tempfile.TemporaryDirectory() as temp:
                    for nb in notebooks:
                        ok, detail = run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "--output-dir", temp, "--output", nb.stem + "-checked", str(nb)], root, timeout=180)
                        (checks if ok else errors).append(f"Notebook execution {'OK' if ok else 'FAIL'}: {nb.relative_to(root)} {detail if not ok else ''}".strip())
            if not examples and not notebooks and not (tests_dir.is_dir() and list(tests_dir.rglob("test_*.py"))):
                warnings.append("No runnable examples/tests/notebooks found for --execute; syntax checks only")
        else:
            warnings.append("Runtime execution not requested; add --execute in a trusted environment")

    print(f"DSA validation: {args.session} (read-only)")
    for label, items in (("PASS", checks), ("WARN", warnings), ("FAIL", errors)):
        for item in items:
            print(f"[{label}] {item}")
    print(f"Result: {len(errors)} error(s), {len(warnings)} warning(s), {len(checks)} check(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
