#!/usr/bin/env python3
"""
Simple generator: copies selected folders and converts .txt -> .md
Produces a `site_docs/` folder ready for MkDocs.
"""
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'site_docs'

FOLDERS = ['Docker', 'Git', 'Linux', 'Python', 'ssh', 'VSCode', 'Database']

def ensure_out():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

def copy_folder(name):
    src = ROOT / name
    dest = OUT / name
    if not src.exists():
        return
    dest.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        if item.is_file():
            if item.suffix == '.txt':
                # convert to md
                text = item.read_text()
                # build the markdown content without complex f-string delimiters
                md = "# " + item.stem + "\n\n```\n" + text + "\n```\n"
                (dest / (item.stem + '.md')).write_text(md)
            else:
                shutil.copy(item, dest / item.name)

def make_index():
    idx = OUT / 'index.md'
    lines = ["# Documents\n", "\n", "This site publishes the repository documents.\n", "\n", "## Sections\n", "\n"]
    for f in FOLDERS:
        if (OUT / f).exists():
            lines.append(f"- [{f}]({f}/index.md)\n")
    idx.write_text('\n'.join(lines))

def make_section_indexes():
    for f in FOLDERS:
        d = OUT / f
        if not d.exists():
            continue
        lines = [f"# {f}", "\n", "Files:\n"]
        for file in sorted(d.iterdir()):
            if file.suffix == '.md':
                lines.append(f"- [{file.stem}]({file.name})\n")
        (d / 'index.md').write_text('\n'.join(lines))

def main():
    ensure_out()
    for f in FOLDERS:
        copy_folder(f)
    make_index()
    make_section_indexes()
    print('site_docs generated at', OUT)

if __name__ == '__main__':
    main()
