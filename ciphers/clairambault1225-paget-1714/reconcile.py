#!/usr/bin/env python3
"""Reconcile passA.tsv/passB.tsv into ciphertext.tsv for clairambault1225-paget-1714.

Why this target has its own reconciler instead of a bare `tools/reconcile_passes.py
passA.tsv passB.tsv` call: the two blind passes each invented their own per-manuscript-line
numbering (f61L_01, f61L_02, ...), and disagreed by one line in several places (mainly
whether a page's old-series pagination stamp got its own line), which cascades into a
near-total line-ID mismatch for every line after the split and tanks the tool's line-keyed
alignment (33.7% on the raw files). Fix applied here, in order:
  1. Drop any manuscript line that is 100% pagenum tokens (the stamp), then renumber the
     remaining lines 01.. sequentially per image, per pass independently -- this removes
     the single largest source of drift (both passes still agree almost everywhere else).
  2. Flatten each image's remaining tokens into one ordered sequence (position 1..N) and
     align pass A against pass B token-by-token with tools/reconcile_passes.py's own
     Needleman-Wunsch aligner (imported, not reimplemented -- CLAUDE.md Usage 8), one
     alignment per image instead of per manuscript-line. This is legitimate here because
     each image is continuous running prose read top-to-bottom with no column break within
     an image (the page-halves were already split at the book gutter when the crops were
     cut); it would not be legitimate for a source with real multi-column layout.
  3. kind (clear/cipher/insertion-clear/...) is carried through from whichever pass's row
     the aligned token came from, not re-inferred from token.isdigit() -- clear-text dates
     ("19.", "25.", "1714") are digit strings too, and classifying by digit-ness alone
     miscounts them as cipher groups (caught and fixed during this session: an early isdigit()
     draft misclassified the "1714" in both datelines as a cipher code).

Run: python3 reconcile.py   (from this directory, or with cwd anywhere -- paths are relative
to this script's own folder). Writes ciphertext.tsv. Exits non-zero if passA.tsv/passB.tsv
are missing.
"""
import csv, sys, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
import reconcile_passes as rp

LETTER_MAP = {
    'f60R': 1, 'f61L': 1, 'f61R': 1, 'f62L': 1, 'f62R': 1, 'f63L': 1, 'f63R': 1,
    'f64L': 1, 'f64R': 1, 'f65L': 1,
    'f65R': 2, 'f66L': 2, 'f66R': 2,
}
IMAGES = list(LETTER_MAP)


def normalize(path):
    """Drop pagenum-only lines, renumber remaining lines 01.. per image, return rows flattened per image in order."""
    rows = list(csv.DictReader(open(path), delimiter='\t'))
    by_line = collections.defaultdict(list)
    order = []
    for r in rows:
        if r['line'] not in by_line:
            order.append(r['line'])
        by_line[r['line']].append(r)
    by_image = collections.defaultdict(list)
    for lid in order:
        group = by_line[lid]
        if {g['kind'] for g in group} == {'pagenum'}:
            continue
        img = lid.split('_')[0]
        by_image[img].extend(group)
    return by_image


def main():
    check = '--check' in sys.argv
    a_path = os.path.join(HERE, 'passA.tsv')
    b_path = os.path.join(HERE, 'passB.tsv')
    if not (os.path.exists(a_path) and os.path.exists(b_path)):
        sys.exit('passA.tsv and passB.tsv must exist in this folder')
    A = normalize(a_path)
    B = normalize(b_path)

    out_rows = []
    for img in IMAGES:
        a = A.get(img, [])
        b = B.get(img, [])
        pairs = rp.nw([r['token'] for r in a], [r['token'] for r in b])
        pos = 0
        for i, j in pairs:
            pos += 1
            ra = a[i] if i is not None else None
            rb = b[j] if j is not None else None
            if ra and rb:
                same_tok = ra['token'] == rb['token']
                same_kind = ra['kind'] == rb['kind']
                token = ra['token']
                kind = ra['kind'] if same_kind else f"{ra['kind']}/{rb['kind']}"
                grade = 'H' if same_tok and same_kind else 'M'
                why = 'agree' if same_tok and same_kind else 'differ'
                alt = '' if (same_tok and same_kind) else (
                    f"A:{ra['token']}({ra['kind']},{ra['conf']})/B:{rb['token']}({rb['kind']},{rb['conf']})"
                )
            elif ra:
                token, kind, grade, why = ra['token'], ra['kind'], 'M', 'gap-B'
                alt = f"A-only:{ra['token']}({ra['kind']},{ra['conf']})"
            else:
                token, kind, grade, why = rb['token'], rb['kind'], 'M', 'gap-A'
                alt = f"B-only:{rb['token']}({rb['kind']},{rb['conf']})"
            out_rows.append({
                'letter': LETTER_MAP[img], 'line': img, 'position': pos,
                'token': token, 'kind': kind, 'grade': grade, 'alt': alt, 'why': why,
            })

    out_path = os.path.join(HERE, 'ciphertext.tsv')
    fieldnames = ['letter', 'line', 'position', 'token', 'kind', 'grade', 'alt', 'why']
    new_text = '\t'.join(fieldnames) + '\n' + ''.join(
        '\t'.join(str(r[k]) for k in fieldnames) + '\n' for r in out_rows)
    n_h = sum(1 for r in out_rows if r['grade'] == 'H')
    n_m = sum(1 for r in out_rows if r['grade'] == 'M')
    if check:
        old_text = open(out_path, encoding='utf-8').read() if os.path.exists(out_path) else None
        if old_text != new_text:
            sys.exit(f'{out_path} is stale: re-running reconcile.py from the committed passA.tsv/passB.tsv '
                      f'produces a different file. Re-run without --check to regenerate it.')
        print(f'{out_path}: {len(out_rows)} rows ({n_h} H, {n_m} M) -- matches committed file, not stale')
        return
    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        f.write(new_text)
    print(f'{out_path}: {len(out_rows)} rows ({n_h} H, {n_m} M)')


if __name__ == '__main__':
    main()
