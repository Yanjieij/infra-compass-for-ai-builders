from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

try:
    import nbformat
except ImportError:  # pragma: no cover
    nbformat = None

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / 'notebooks'

BAD_CONTROL_CHARS = {
    '\x07': 'BEL, usually broken \\approx',
    '\x08': 'BACKSPACE',
    '\x0c': 'FORM FEED, usually broken \\frac',
    '\r': 'CARRIAGE RETURN, usually broken \\right or CR',
}


def fail(msg: str):
    print('FAIL:', msg)
    raise SystemExit(1)


def markdown_text(nb: dict) -> str:
    return '\n'.join(c.get('source', '') for c in nb.get('cells', []) if c.get('cell_type') == 'markdown')


def validate_notebook(path: Path):
    nb = json.loads(path.read_text(encoding='utf-8'))
    if nb.get('nbformat') != 4:
        fail(f'{path}: nbformat is not 4')
    if not all('id' in c for c in nb.get('cells', [])):
        fail(f'{path}: some cells do not have id')

    if nbformat is not None:
        nb_obj = nbformat.read(path, as_version=4)
        nbformat.validate(nb_obj)

    for idx, c in enumerate([c for c in nb.get('cells', []) if c.get('cell_type') == 'code'], 1):
        ast.parse(c.get('source', ''), filename=f'{path}:cell{idx}')

    text = markdown_text(nb)
    for ch, reason in BAD_CONTROL_CHARS.items():
        if ch in text:
            fail(f'{path}: contains control char {repr(ch)} ({reason})')

    if text.count('$$') % 2 != 0:
        fail(f'{path}: unmatched $$ display math delimiter')

    # Coarse inline math check: each non-code markdown line should have paired single-dollar delimiters.
    in_fence = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        single_dollars = len(re.findall(r'(?<!\$)\$(?!\$)', line))
        if single_dollars % 2:
            fail(f'{path}:{lineno}: unmatched inline $ delimiter: {line}')

    mermaid_blocks = re.findall(r'```mermaid\n(.*?)\n```', text, flags=re.S)
    if text.count('```mermaid') != len(mermaid_blocks):
        fail(f'{path}: unclosed mermaid fence')
    for i, block in enumerate(mermaid_blocks, 1):
        stripped = block.strip()
        if not stripped:
            fail(f'{path}: empty mermaid block {i}')
        header = stripped.splitlines()[0]
        if header not in {'flowchart TB', 'flowchart LR', 'sequenceDiagram', 'block-beta'}:
            fail(f'{path}: unexpected mermaid header {header!r}')
        for lineno, line in enumerate(block.splitlines(), 1):
            if line.count('"') % 2:
                fail(f'{path}: mermaid block {i} line {lineno} has odd quotes: {line}')

    image_refs = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text)
    for ref in image_refs:
        target = (path.parent / ref).resolve()
        if not target.exists():
            fail(f'{path}: missing image reference {ref} -> {target}')

    return len(nb.get('cells', [])), len([c for c in nb.get('cells', []) if c.get('cell_type') == 'code']), len(text)


def main():
    notebooks = sorted(NOTEBOOKS.glob('*.ipynb'))
    if not notebooks:
        fail('no notebooks found')
    for path in notebooks:
        cells, code_cells, md_chars = validate_notebook(path)
        print(f'OK {path.relative_to(ROOT)} cells={cells} code={code_cells} md_chars={md_chars}')


if __name__ == '__main__':
    main()
