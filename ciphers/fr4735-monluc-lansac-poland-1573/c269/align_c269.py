#!/usr/bin/env python3
"""MONL-C269A (20 Oct 2026): align the reconciled c269 (f.138v) L01-L10 stream against the ff.140r-141r clear text and write the
decode_key.py inputs for decode.json job c269 (registered gate passed first: score_c269.py, PREREG-MONL-C269A.md).
MONL-C269C (20 Oct 2026, PREREG-MONL-C269C.md): one joint alignment of every read band (BANDS below, in leaf order); a band's tokens
are written (graded) only when its registered gate passed (graded=True); an ungraded band stays in the stream for placement only.

Usage: python3 align_c269.py [--check]
Method: align_c268.py's DP, scores and folds unchanged (key.tsv, Tomokiyo's published Cipher 1 table), against the clear letter from
c268's own aligned end ("...entendans que l|") onward, free start and end. Writes ../ciphertext_c269.tsv (from the graded bands), align_c269.tsv (per token), ../votes_c269.tsv (a vote = the clear
letter a keyed token faces, only from an unbracketed clear word; align_c268's rule). No fills: unkeyed signs stay U. --check exits 1
when any output is stale (rule 7).
"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import align_c268 as A


BANDS = [('c269_reconciled.tsv', True),    # L01-L10, MONL-C269A gate met
         ('c269b_reconciled.tsv', True),   # L11-L22, MONL-C269C decision rule passed (0.650 vs p95 0.425, span delta -1)
         ('c269c_reconciled.tsv', True)]   # L23-L33, MONL-C269C gate passed (0.482 vs p95 0.385, span delta 0)


def run():
    allrec = [(f, g) for fn, g in BANDS if (HERE / fn).exists()
              for f in [l.rstrip('\n').split('\t') for l in open(HERE / fn, encoding='utf-8')][1:]]
    rec = [f for f, g in allrec if g]
    ct = 'line\tpos\tsign\tconf\tpass_a\tpass_b\n' + ''.join('\t'.join(f[:6]) + '\n' for f in rec)
    key = {}
    for l in list(open(HERE.parent / 'key.tsv', encoding='utf-8'))[1:]:
        f = l.rstrip('\n').split('\t'); key[f[0]] = f[2]
    toks = [{'line': f[0], 'pos': int(f[1]), 'sign': f[2], 'conf': f[3], 'value': A.fold(key[f[2]]) if key.get(f[2]) else None,
             'graded': bool(g)} for f, g in allrec]
    words = A.load_clear()
    clear = ''.join(w[2] for w in words)
    unsure = [w[3] for w in words for _ in w[2]]
    # continuation of the c268 stream: c269 is aligned only against the clear text after c268's own aligned end (no clear letter
    # counted twice); the registered gate (score_c269.py) did not use this restriction and was met without it.
    _, _, _, end = A.align(A.load_tokens(), clear)
    assert clear[end - 13:end] == 'entendansquel', clear[end - 13:end]
    clear, unsure = clear[end:], unsure[end:]
    _, path, a, b = A.align(toks, clear)
    rows = [r for r in A.classify(toks, clear, path, unsure) if r['graded']]
    tsv = 'line\tpos\tsign\tconf\ttable\tclear\tkind\tclear_unsure\n' + ''.join(
        f"{r['line']}\t{r['pos']}\t{r['sign']}\t{r['conf']}\t{r['value'] or ''}\t{r['clear']}\t{r['kind']}\t{int(r['unsure'])}\n" for r in rows)
    votes = 'line\tpos\tvalue\n' + ''.join(f"{r['line']}\t{r['pos']}\t{r['clear']}\n" for r in rows
                                         if r['value'] is not None and len(r['clear']) == 1 and not r['unsure'])
    return {HERE.parent / 'ciphertext_c269.tsv': ct, HERE / 'align_c269.tsv': tsv, HERE.parent / 'votes_c269.tsv': votes}, A.stats(rows)


def main():
    outs, st = run()
    if '--check' in sys.argv:
        ok = all(p.exists() and p.read_text(encoding='utf-8') == t for p, t in outs.items())
        print('align_c269: OK' if ok else 'align_c269: STALE'); sys.exit(0 if ok else 1)
    for p, t in outs.items():
        p.write_text(t, encoding='utf-8')
    print(st)


if __name__ == '__main__':
    main()
