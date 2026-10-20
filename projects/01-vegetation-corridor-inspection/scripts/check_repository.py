"""Check documentation and pure-Python helpers; does not import/run ArcPy."""
import ast
import importlib.util
import json
from pathlib import Path
import re


def main():
    project = Path(__file__).resolve().parents[1]
    root = project.parents[1]
    for script in (project / 'scripts').glob('*.py'):
        ast.parse(script.read_text(encoding='utf-8'), filename=str(script))
    spec = importlib.util.spec_from_file_location('clearance', project / 'scripts/finalize_clearance.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    cases = [(None, 'Unknown'), (-1, 'Unknown'), (float('nan'), 'Unknown'),
             (0, 'High'), (1.999, 'High'), (2, 'Medium'), (3.999, 'Medium'), (4, 'Low')]
    for distance, expected in cases:
        if module.classify(distance) != expected:
            raise AssertionError((distance, expected))
    if module.resolve(4, 'S-010', ['S-003', 'S-001', 'S-003']) != (
            0.0, 'S-001', 'S-001; S-003', 2, 'Inside3D', 'High'):
        raise AssertionError('Contained-case correction/tie retention failed')
    if module.resolve(3, 'S-002', []) != (3, 'S-002', None, 0, 'Near3D', 'Medium'):
        raise AssertionError('Separated case failed')
    if module.resolve(None, None, [])[-1] != 'Unknown':
        raise AssertionError('Missing case failed')
    summary = json.loads((project / 'results/validation-summary.json').read_text(encoding='utf-8'))
    if sum(summary['screening_counts'].values()) != summary['canopies'] or summary['canopies'] != 241:
        raise AssertionError('Summary counts do not add up')
    if summary['zero_clearance_canopies'] > summary['screening_counts']['High']:
        raise AssertionError('Zero clearance must be a subset of High')
    docs = [root / 'README.md', root / 'docs/README.md', project / 'scripts/README.md']
    docs.extend(project.glob('*.md'))
    for doc in docs:
        for target in re.findall(r'\]\(([^)]+)\)', doc.read_text(encoding='utf-8')):
            if target.startswith(('https://', 'http://', '#')):
                continue
            if not (doc.parent / target.split('#')[0]).exists():
                raise AssertionError(f'Broken local link in {doc}: {target}')
    print('PASS: Python syntax; 8 classification cases; 3 resolution cases; summary totals; local Markdown links.')
    print('ArcPy and live services were not exercised by this check.')


if __name__ == '__main__':
    main()
