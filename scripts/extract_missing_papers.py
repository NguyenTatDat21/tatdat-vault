#!/usr/bin/env python3
"""Extract missing paper markdown files with mineru-kit.

A paper note is expected at `_papers/<paper-id>/<paper-id>.md` and should contain:
- `extracted-pdf: "[[...]]"` in frontmatter (fallback: `<note-stem>-extracted.md`)
- at least one attachment line with `[File path](<file:///...pdf>)`

Examples:
  uvx python scripts/extract_missing_papers.py --dry-run
  uvx python scripts/extract_missing_papers.py --tier standard --max 5
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

EXTRACTED_PDF_RE = re.compile(r"^extracted-pdf:\s*(?P<value>.+?)\s*$", re.MULTILINE)
WIKILINK_RE = re.compile(r"\[\[(?P<target>.+?)\]\]")
PDF_PATH_RE = re.compile(r"\[File path\]\(<file://(?P<path>[^>]+?\.pdf)>\)", re.IGNORECASE)


@dataclass
class PaperJob:
    note_path: Path
    pdf_path: Path
    extracted_path: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract missing _papers markdown with mineru-kit")
    parser.add_argument("--papers-root", default="_papers", help="Root folder containing paper notes (default: _papers)")
    parser.add_argument(
        "--tier",
        default="standard",
        choices=["flash", "basic", "standard", "advanced"],
        help="MinerU parse tier (default: standard)",
    )
    parser.add_argument("--max", type=int, default=0, help="Process at most N missing papers (0 = all)")
    parser.add_argument("--force", action="store_true", help="Re-extract even if extracted markdown already exists")
    parser.add_argument("--dry-run", action="store_true", help="Only print what would be extracted")
    parser.add_argument(
        "--keep-going",
        action="store_true",
        help="Continue on extraction errors (default: stop at first error)",
    )
    parser.add_argument(
        "--mineru-bin",
        default="mineru-kit",
        help="Binary name/path for mineru-kit (default: mineru-kit)",
    )
    return parser.parse_args()


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and ((value[0] == '"' and value[-1] == '"') or (value[0] == "'" and value[-1] == "'")):
        return value[1:-1]
    return value


def resolve_extracted_path(note_text: str, note_path: Path, repo_root: Path) -> Path:
    match = EXTRACTED_PDF_RE.search(note_text)
    if not match:
        return note_path.with_name(f"{note_path.stem}-extracted.md")

    raw_value = strip_quotes(match.group("value"))
    wiki_match = WIKILINK_RE.fullmatch(raw_value)
    if wiki_match:
        target = wiki_match.group("target").split("|", 1)[0].strip()
    else:
        target = raw_value.strip()

    if not target:
        return note_path.with_name(f"{note_path.stem}-extracted.md")

    if not target.endswith(".md"):
        target = f"{target}.md"

    extracted = Path(target)
    if not extracted.is_absolute():
        extracted = repo_root / extracted

    return extracted


def resolve_pdf_path(note_text: str) -> Path | None:
    match = PDF_PATH_RE.search(note_text)
    if not match:
        return None

    decoded = unquote(match.group("path"))
    return Path(decoded)


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def build_mineru_prefix(args: argparse.Namespace) -> list[str]:
    if shutil.which(args.mineru_bin):
        return [args.mineru_bin]

    raise RuntimeError(
        f"{args.mineru_bin!r} not found on PATH. Install mineru-kit or pass --mineru-bin with the executable path."
    )


def find_jobs(repo_root: Path, papers_root: Path, force: bool) -> tuple[list[PaperJob], list[Path], list[tuple[Path, Path]]]:
    jobs: list[PaperJob] = []
    notes_missing_pdf_link: list[Path] = []
    notes_with_missing_pdf_file: list[tuple[Path, Path]] = []

    for note_path in sorted(papers_root.glob("*/*.md")):
        if note_path.name.endswith("-extracted.md"):
            continue

        note_text = note_path.read_text(encoding="utf-8")
        extracted_path = resolve_extracted_path(note_text, note_path, repo_root)

        if not force and extracted_path.exists() and extracted_path.stat().st_size > 0:
            continue

        pdf_path = resolve_pdf_path(note_text)
        if pdf_path is None:
            notes_missing_pdf_link.append(note_path)
            continue

        if not pdf_path.exists():
            notes_with_missing_pdf_file.append((note_path, pdf_path))
            continue

        jobs.append(PaperJob(note_path=note_path, pdf_path=pdf_path, extracted_path=extracted_path))

    return jobs, notes_missing_pdf_link, notes_with_missing_pdf_file


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]

    papers_root = Path(args.papers_root)
    if not papers_root.is_absolute():
        papers_root = repo_root / papers_root

    if not papers_root.exists():
        print(f"papers root not found: {papers_root}", file=sys.stderr)
        return 2

    jobs, missing_link, missing_pdf = find_jobs(repo_root, papers_root, args.force)

    if args.max > 0:
        jobs = jobs[: args.max]

    print(f"Found {len(jobs)} paper(s) to extract.")
    if missing_link:
        print(f"- {len(missing_link)} note(s) missing a PDF File path link")
    if missing_pdf:
        print(f"- {len(missing_pdf)} note(s) reference a missing PDF file")

    if not jobs:
        return 0

    try:
        mineru_prefix = build_mineru_prefix(args)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    failures: list[tuple[PaperJob, int]] = []
    success_count = 0

    for idx, job in enumerate(jobs, start=1):
        print(f"\n[{idx}/{len(jobs)}] {rel(job.note_path, repo_root)}")
        print(f"  pdf: {job.pdf_path}")
        print(f"  out: {rel(job.extracted_path, repo_root)}")

        cmd = [
            *mineru_prefix,
            "parse",
            str(job.pdf_path),
            "-o",
            str(job.extracted_path),
            "--tier",
            args.tier,
            "-f",
            "markdown",
        ]

        if args.dry_run:
            print("  dry-run: " + " ".join(cmd))
            continue

        job.extracted_path.parent.mkdir(parents=True, exist_ok=True)
        result = subprocess.run(cmd)
        if result.returncode == 0:
            success_count += 1
            continue

        failures.append((job, result.returncode))
        print(f"  ERROR: mineru exited with code {result.returncode}", file=sys.stderr)
        if not args.keep_going:
            break

    print("\nSummary")
    print(f"- Success: {success_count}")
    print(f"- Failed:  {len(failures)}")

    if missing_link:
        print("- Missing PDF link in notes:")
        for note in missing_link[:10]:
            print(f"  - {rel(note, repo_root)}")
        if len(missing_link) > 10:
            print(f"  ... and {len(missing_link) - 10} more")

    if missing_pdf:
        print("- Missing PDF files:")
        for note, pdf in missing_pdf[:10]:
            print(f"  - {rel(note, repo_root)} -> {pdf}")
        if len(missing_pdf) > 10:
            print(f"  ... and {len(missing_pdf) - 10} more")

    if failures:
        print("- Failed jobs:")
        for job, code in failures[:10]:
            print(f"  - {rel(job.note_path, repo_root)} (exit {code})")
        if len(failures) > 10:
            print(f"  ... and {len(failures) - 10} more")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
