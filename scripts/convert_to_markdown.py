"""
Convert the annotated transformer percent-format .py notebook to clean markdown.
Preserves LaTeX math, code blocks, images, and blockquotes.
"""
import re
import sys
from pathlib import Path


def convert(input_path: str, output_path: str, image_prefix: str = "assets/annotated-transformer/") -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    out_lines = []
    in_markdown = False
    in_code = False
    code_buffer = []

    for line in lines:
        # Detect cell markers
        md_match = re.match(r"^# %% \[markdown\]", line)
        code_match = re.match(r"^# %%", line)

        if md_match:
            # Flush code buffer if needed
            if in_code and code_buffer:
                out_lines.append("```python\n")
                out_lines.extend(code_buffer)
                out_lines.append("```\n\n")
                code_buffer = []
                in_code = False
            in_markdown = True
            in_code = False
            continue

        if code_match and not md_match:
            # Flush code buffer and close markdown
            if in_code and code_buffer:
                out_lines.append("```python\n")
                out_lines.extend(code_buffer)
                out_lines.append("```\n\n")
                code_buffer = []
            in_code = True
            in_markdown = False
            continue

        # Skip jupyter metadata lines
        if line.strip().startswith("# jupyter:") or line.strip().startswith("# jupytext:"):
            continue
        if line.strip().startswith("# id=") or line.strip().startswith("# tags="):
            continue
        if line.strip().startswith("# kernelspec:") or line.strip().startswith("# display_name="):
            continue
        if line.strip().startswith("# language:") or line.strip().startswith("# name:"):
            continue
        if line.strip().startswith("# formats:") or line.strip().startswith("# text_representation:"):
            continue
        if line.strip().startswith("# extension:") or line.strip().startswith("# format_name:"):
            continue
        if line.strip().startswith("# format_version:") or line.strip().startswith("# jupytext_version:"):
            continue

        if in_markdown:
            # Strip '# ' prefix, keep empty lines
            if line.startswith("# "):
                out_lines.append(line[2:])
            elif line == "#\n":
                out_lines.append("\n")
            elif line == "#":
                out_lines.append("\n")
            elif line.startswith("#"):
                out_lines.append(line[1:])
            else:
                out_lines.append(line)
        elif in_code:
            if line.strip() == '# %% [markdown]' or line.strip().startswith('# %% '):
                continue
            code_buffer.append(line)

    # Flush remaining code buffer
    if code_buffer:
        out_lines.append("```python\n")
        out_lines.extend(code_buffer)
        out_lines.append("```\n\n")

    content = "".join(out_lines)

    # Clean up: remove reference lines like "# (cite)" patterns handled already
    # Fix image paths to use the site's asset directory
    content = re.sub(
        r'!\[\]\(images/([^)]+)\)',
        f'![\\1]({image_prefix}\\1)',
        content
    )

    # Ensure the images are referenced correctly
    content = re.sub(
        r'<img src="images/([^"]+)"',
        f'<img src="{image_prefix}\\1"',
        content
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Converted {input_path} -> {output_path}")
    print(f"  Total lines output: {len(content.splitlines())}")


if __name__ == "__main__":
    input_path = sys.argv[1] if len(sys.argv) > 1 else "../annotated-transformer/the_annotated_transformer.py"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "../data/annotated-transformer/annotated-transformer.md"
    image_prefix = sys.argv[3] if len(sys.argv) > 3 else "assets/annotated-transformer/"
    convert(input_path, output_path, image_prefix)
