"""Convert diary TOML files to blog markdown files.

Output format: data/blogs/<year>/<seq>_<slug>.md
Content: title: <title>
         ---
         <body>
"""

import os
import re
from pathlib import Path

DIARIES_DIR = Path("data/diaries")
BLOGS_DIR = Path("data/blogs")

YEAR_FILES = [
    2019, 2020, 2021, 2022, 2023, 2024, 2025
]


def parse_elements(text):
    elements = []
    blocks = re.split(r'\n\s*\[\[elements\]\]', text)
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        title_match = re.search(r'^title\s*=\s*"(.*?)"', block, re.MULTILINE)
        if not title_match:
            continue
        title = title_match.group(1)
        body_match = re.search(r'body\s*=\s*"""\n?(.*?)"""', block, re.DOTALL)
        if not body_match:
            body_match = re.search(r'body\s*=\s*""""(.*?)"""', block, re.DOTALL)
        if not body_match:
            continue
        body = body_match.group(1).strip()
        elements.append({'title': title, 'body': body})
    return elements


def make_slug(title):
    slug = (
        title.casefold()
        .replace(" ", "-")
        .replace("/", "")
        .replace("'", "")
        .replace("?", "")
        .replace("---", "-")
        .replace(":", "")
        .replace(",", "")
        .replace("\u200b", "")
        .replace("\u200c", "")
    )
    slug = slug.strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug


def convert():
    for year in YEAR_FILES:
        toml_path = DIARIES_DIR / f"{year}.toml"
        if not toml_path.exists():
            print(f"Skipping {toml_path} (not found)")
            continue

        with open(toml_path, encoding="utf-8") as f:
            text = f.read()

        elements = parse_elements(text)

        # Elements are newest-first in the file; reverse to oldest-first
        # so sequence numbers go 01, 02, ... chronologically
        elements_reversed = list(reversed(elements))

        year_dir = BLOGS_DIR / str(year)
        year_dir.mkdir(parents=True, exist_ok=True)

        for i, elem in enumerate(elements_reversed):
            title = elem["title"]
            body = elem["body"]
            slug = make_slug(title)
            seq = str(i + 1).zfill(2)

            md_content = f"title: {title}\n---\n{body}\n"

            md_path = year_dir / f"{seq}_{slug}.md"
            md_path.write_text(md_content, encoding="utf-8")
            print(f"Created {md_path}")


if __name__ == "__main__":
    convert()
