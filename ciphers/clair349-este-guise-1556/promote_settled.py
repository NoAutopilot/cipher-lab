#!/usr/bin/env python3
"""Promote the settled passG/passH reconciliation to ciphertext.tsv (ZX-TR349D, 25 Sept 2026).

Inputs (all committed beside this script):
  settle_aligned.tsv  one row per aligned column of passG.tsv/passH.tsv (tools/reconcile_passes.py's nw alignment):
                      line, pos, status (agree / GLOSS / SIGN), each pass's sign, gloss and note
  settled.tsv         one row per non-agree column (and any added column, pos like 12.5), settled from the lines_h
                      crops: line, pos, sign (DEL drops the column; ? = unsettled), gloss, source, why
Output: ciphertext.tsv  line, position, sign, gloss, confidence, source, why
  confidence H where the two blind passes agree on sign and gloss; M where the column was settled from the image.
  Plain marginal words (kind plain) are not cipher and are left out. `--check` exits 1 if ciphertext.tsv is stale.
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))


def apply_corrections(rows):
    """corrections.tsv (ZX-DEC349, 25 Sept 2026): one row per token recoded from the lines_h image after the
    settle, keyed by line and the ZX-TR349D ciphertext.tsv position (the row order before any correction):
    line, position, old, new, partner, reason, grade. new=DEL drops the token (the second half of a split code)."""
    p = os.path.join(HERE, 'corrections.tsv')
    if not os.path.exists(p):
        return rows
    corr = {(r['line'].zfill(2), int(r['position'])): r
            for r in csv.DictReader(open(p, encoding='utf-8'), delimiter='\t')}
    out, n, last = [], 0, None
    for row in rows:
        ln = row[0]
        n = n + 1 if ln == last else 1
        last = ln
        c = corr.pop((ln, n), None)
        if c is None:
            out.append(row)
            continue
        if c['old'] != row[2]:
            raise SystemExit(f'corrections.tsv {ln}/{n}: old {c["old"]!r} but ciphertext has {row[2]!r}')
        if c['new'] == 'DEL':
            continue
        out.append((ln, row[1], c['new'], row[3], 'M', 'recode', c['reason']))
    if corr:
        raise SystemExit(f'corrections.tsv rows not matched: {sorted(corr)}')
    return out


def build():
    settled = {}
    for r in csv.DictReader(open(os.path.join(HERE, 'settled.tsv'), encoding='utf-8'), delimiter='\t'):
        settled[(r['line'].zfill(2), r['pos'])] = r
    rows = []
    for r in csv.DictReader(open(os.path.join(HERE, 'settle_aligned.tsv'), encoding='utf-8'), delimiter='\t'):
        key = (r['line'], r['pos'])
        if r['status'] == 'agree':
            rows.append((r['line'], float(r['pos']), r['G_sign'], r['G_gloss'], 'H', 'both', 'agree'))
        else:
            s = settled.pop(key, None)
            if s is None:
                raise SystemExit(f'no settled row for {key}')
            if s['sign'] == 'DEL':
                continue
            rows.append((r['line'], float(r['pos']), s['sign'], s['gloss'], 'M', s['source'], s['why']))
    for (ln, pos), s in settled.items():  # added columns
        if s['sign'] != 'DEL':
            rows.append((ln, float(pos), s['sign'], s['gloss'], 'M', 'new', s['why']))
    rows.sort(key=lambda x: (x[0], x[1]))
    rows = apply_corrections(rows)
    out, n, last = [], 0, None
    for ln, _, sign, gloss, conf, src, why in rows:
        n = n + 1 if ln == last else 1
        last = ln
        out.append('\t'.join([ln, str(n), sign, gloss, conf, src, why.replace('\t', ' ')]))
    return 'line\tposition\tsign\tgloss\tconfidence\tsource\twhy\n' + '\n'.join(out) + '\n'


if __name__ == '__main__':
    text = build()
    path = os.path.join(HERE, 'ciphertext.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path, encoding='utf-8').read() == text
        print('ciphertext.tsv', 'current' if ok else 'STALE')
        sys.exit(0 if ok else 1)
    open(path, 'w', encoding='utf-8').write(text)
    print('wrote', path, text.count('\n') - 1, 'rows')
