#!/usr/bin/env python3
"""Create a Markdown index of filenames in a local evidence folder."""
import argparse
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument("folder")
    p.add_argument("--output", default="evidence-index.md")
    a = p.parse_args()
    folder = Path(a.folder).expanduser().resolve()
    if not folder.is_dir():
        raise SystemExit("Folder does not exist.")
    items = sorted(x for x in folder.rglob("*") if x.is_file())
    lines = ["# Evidence File Index", "",
             "> Check that filenames and contents contain no secrets or personal data.", ""]
    lines += [f"- `{x.relative_to(folder).as_posix()}`" for x in items]
    Path(a.output).write_text("\\n".join(lines) + "\\n", encoding="utf-8")
    print(f"Wrote {a.output}: {len(items)} files")

if __name__ == "__main__":
    main()
