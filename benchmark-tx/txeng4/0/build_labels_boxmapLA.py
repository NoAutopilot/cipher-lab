#!/usr/bin/env python3
"""TXE4-0 REPAIR unit 4 (12 Oct 2026, account 3): rebuild the atlas cluster names on the corrected (label-aware)
box-to-token join, as atlas/RESCORE.md's job (BOXMAP-RESCORE, 11 Oct 2026) already ran once -- this script is the
regenerate-and-check wrapper that job's RESCORE.md named but did not commit under a permanent name.

Runs atlas/no87_map.py --compat (Z2's one named exception: it reads the clerk-sheet alignment to fill the `truth`
column, to a temp file, never committed) then atlas/name_clusters.py --map <that file> --out <temp>, and writes
the result as atlas/labels_boxmapLA.json and atlas/cluster_names_boxmapLA.tsv -- NEW files beside the committed,
unchanged atlas/labels.json (Z4). No consumer reads these by default (atlas/README.md's new section says so).

--check: regenerate into a temp dir and exit 1 if either committed file differs (rule 7); exit 0 if current.
Default (no --check): regenerate and overwrite the two committed files.

Usage: python3 benchmark-tx/txeng4/0/build_labels_boxmapLA.py [--check]
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
A = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572/atlas')
LABELS_OUT = os.path.join(A, 'labels_boxmapLA.json')
NAMES_OUT = os.path.join(A, 'cluster_names_boxmapLA.tsv')


def build(out_dir):
    compat = os.path.join(out_dir, 'compat_map.tsv')
    r = subprocess.run([sys.executable, os.path.join(A, 'no87_map.py'), '--compat', compat],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit('no87_map.py --compat failed: ' + r.stdout + r.stderr)
    named_dir = os.path.join(out_dir, 'named')
    r = subprocess.run([sys.executable, os.path.join(A, 'name_clusters.py'), '--map', compat, '--out', named_dir],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit('name_clusters.py --map failed: ' + r.stdout + r.stderr)
    print(r.stdout.strip())
    return os.path.join(named_dir, 'labels.json'), os.path.join(named_dir, 'cluster_names.tsv')


def main():
    check = '--check' in sys.argv
    with tempfile.TemporaryDirectory() as d:
        labels_tmp, names_tmp = build(d)
        if check:
            ok = (os.path.exists(LABELS_OUT) and open(LABELS_OUT).read() == open(labels_tmp).read() and
                  os.path.exists(NAMES_OUT) and open(NAMES_OUT).read() == open(names_tmp).read())
            print('build_labels_boxmapLA --check:', 'current' if ok else 'STALE')
            return 0 if ok else 1
        for src, dst in ((labels_tmp, LABELS_OUT), (names_tmp, NAMES_OUT)):
            with open(src) as f, open(dst, 'w') as g:
                g.write(f.read())
        print('->', LABELS_OUT, NAMES_OUT)
        return 0


if __name__ == '__main__':
    sys.exit(main())
