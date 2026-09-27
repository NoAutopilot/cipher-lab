#!/usr/bin/env python3
"""bench_check.py: validates BENCHMARK.tsv against its own freeze rules (CLAUDE.md rule 7; BENCH-FREEZE,
27 Sept 2026, brief runs/2026-09-27-parent-ytbiz-bench-freeze.md unit U3).

BENCHMARK.tsv's own header comment (its first line) names the commit sha it was frozen at and says rows are
appended, never edited in place. This script checks that promise mechanically:

  1. every row has a non-empty `truth` label.
  2. no `family` value appears in both the `dev` and `eval` split (CLAUDE.md rule 3's headline paragraph:
     a control/benchmark split is only informative if whole families, not individual pairs, are held out).
  3. every eval row's real repo file paths (ciphertext_path/key_path/plaintext_path) are byte-identical to
     their content at the freeze commit sha -- an eval row is scored out of sample only if what it points at
     has not moved (been re-transcribed, re-keyed, or corrected) since the freeze. A path that is not a real
     git-tracked file at that sha -- a directory (trailing '/'), a free-text description (contains a space),
     an empty cell, or a path that did not exist yet at the freeze sha (e.g. a synthetic spec written in the
     same freeze commit) -- is skipped, not failed: only a path git can actually resolve at the freeze sha is
     checked, so this only ever protects real evidence files, never claims to check what did not exist yet.

Usage:
  python3 tools/bench_check.py [BENCHMARK.tsv]
  python3 tools/tests/test_bench_check.py     offline test: throwaway git repo, no real repo paths

Exit 0 if every check passes, 1 otherwise (rows and reasons printed to stdout either way).
"""
import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT = ROOT / 'BENCHMARK.tsv'
PATH_COLUMNS = ['ciphertext_path', 'key_path', 'plaintext_path']


def freeze_sha(header_line):
    m = re.search(r'frozen at commit ([0-9a-f]{7,40})', header_line)
    return m.group(1) if m else None


def load(path):
    text = Path(path).read_text()
    lines = text.splitlines()
    if not lines or not lines[0].startswith('#'):
        raise SystemExit(f"{path}: missing frozen-header comment line (first line must start with '#')")
    sha = freeze_sha(lines[0])
    if not sha:
        raise SystemExit(f"{path}: header comment does not name a frozen commit sha "
                          f"(expected '... frozen at commit <sha> ...')")
    rows = list(csv.DictReader(lines[1:], delimiter='\t'))
    return sha, rows


def git_show(sha, rel_path, root):
    r = subprocess.run(['git', '-C', str(root), 'show', f'{sha}:{rel_path}'], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def resolvable(root, p):
    """A path this check can actually verify: non-empty, not a directory, no free-text spaces, exists on disk."""
    return bool(p) and not p.endswith('/') and ' ' not in p and (root / p).exists()


def check(path=DEFAULT, root=ROOT):
    """Returns (ok, problems, sha, n_rows). problems is a list of human-readable strings, empty when ok."""
    sha, rows = load(path)
    problems = []
    by_family = {}
    for i, row in enumerate(rows, start=1):
        case = row.get('case_id') or f'row {i}'
        truth = (row.get('truth') or '').strip()
        if not truth:
            problems.append(f"{case}: no truth label")
        split = (row.get('split') or '').strip()
        family = (row.get('family') or '').strip()
        if split and family:
            by_family.setdefault(family, set()).add(split)
        if split != 'eval':
            continue
        for col in PATH_COLUMNS:
            p = (row.get(col) or '').strip()
            if not resolvable(root, p):
                continue
            frozen = git_show(sha, p, root)
            if frozen is None:
                continue  # not a tracked file at the freeze sha -- nothing to compare (e.g. written this freeze)
            current = (root / p).read_text(errors='replace')
            if current != frozen:
                problems.append(f"{case}: eval path {col}={p} changed since the freeze commit {sha}")
    for family, splits in by_family.items():
        if len(splits) > 1:
            problems.append(f"family '{family}' appears in both splits: {sorted(splits)}")
    return (not problems), problems, sha, len(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0].strip(),
                                  formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument('benchmark', nargs='?', default=str(DEFAULT), help='path to BENCHMARK.tsv (default: repo root)')
    args = ap.parse_args()
    ok, problems, sha, n = check(Path(args.benchmark))
    if ok:
        print(f"OK: {n} rows, frozen at {sha[:12]}, every check passed")
        sys.exit(0)
    for p in problems:
        print('FAIL:', p)
    print(f"FAILED: {len(problems)} problem(s) in {n} rows frozen at {sha[:12]}")
    sys.exit(1)


if __name__ == '__main__':
    main()
