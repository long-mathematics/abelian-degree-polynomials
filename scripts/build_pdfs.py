#!/usr/bin/env python3
"""Compile the manuscript sources with local pdfLaTeX; no network or shell escape.

Normal use: python3 scripts/build_pdfs.py
The optional --format argument supports a locally generated pdfLaTeX format.
Auxiliary files stay under build/. PDFs and a source/PDF hash manifest are
updated only after every manuscript compiles without unresolved references.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ("short_curve_rh_proof", "abelian_all_degrees_proof",
          "abelian_comparison_streamlined", "abelian_comparison_elementary",
          "curve_rh_single_scale")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine", default="pdflatex")
    parser.add_argument("--format", type=Path)
    args = parser.parse_args()
    if shutil.which(args.engine) is None:
        parser.error(f"Cannot find {args.engine!r}; install a local TeX distribution.")
    env = os.environ.copy()
    env.setdefault("SOURCE_DATE_EPOCH", str(int(datetime(2026, 11, 27, tzinfo=timezone.utc).timestamp())))
    env.setdefault("FORCE_SOURCE_DATE", "1")
    completed = []
    for name in PAPERS:
        source = ROOT / "papers" / f"{name}.tex"
        work = ROOT / "build" / name
        work.mkdir(parents=True, exist_ok=True)
        command = [args.engine]
        if args.format:
            command.append(f"-fmt={args.format.resolve()}")
        command += ["-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
                    "-file-line-error", f"-output-directory={work}", str(source)]
        for iteration in range(1, 4):
            result = subprocess.run(command, cwd=ROOT, env=env, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (work / f"pass-{iteration}.txt").write_text(result.stdout)
            if result.returncode:
                raise SystemExit(f"{name}: pdfLaTeX failed; inspect {work / f'pass-{iteration}.txt'}\n"
                                 + result.stdout[-5000:])
            log = (work / f"{name}.log").read_text(errors="replace")
            unresolved = re.search(r"undefined references|(?:Citation|Reference) .* undefined|Rerun to get|Label\(s\) may have changed", log)
            if iteration >= 2 and not unresolved:
                break
        else:
            raise SystemExit(f"{name}: unresolved references after three passes")
        if re.search(r"Overfull \\[hv]box|Undefined control sequence|LaTeX Error", log):
            raise SystemExit(f"{name}: layout or TeX error; inspect {work / f'{name}.log'}")
        pdf = work / f"{name}.pdf"
        if not pdf.read_bytes().startswith(b"%PDF-"):
            raise SystemExit(f"{name}: output is not a PDF")
        completed.append((source, pdf, iteration))
    engine_version = subprocess.run([args.engine, "--version"], text=True,
                                    capture_output=True, check=True).stdout.splitlines()[0]
    manifest = {"engine": engine_version, "source_date_epoch": env["SOURCE_DATE_EPOCH"],
                "papers": []}
    for source, pdf, passes in completed:
        target = source.with_suffix(".pdf")
        shutil.copyfile(pdf, target)
        manifest["papers"].append({"source": str(source.relative_to(ROOT)),
                                   "source_sha256": sha256(source),
                                   "pdf": str(target.relative_to(ROOT)),
                                   "pdf_sha256": sha256(target), "passes": passes})
    report = ROOT / "audit" / "build_manifest.json"
    report.parent.mkdir(exist_ok=True)
    report.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
