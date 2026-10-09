#!/usr/bin/env python3
"""B167-228: passes/reconciled_b170f228{r,v}.tsv (bare shape classes) -> ciphertext_b170f228.txt (pipe format, tools/decode_key.py).
Letter values are the f.229 ones (same letter, 25 Aug 1640): the majority letter per shape in passes/reconciled_b170f229{r,v}.tsv,
computed here, never set from f.228's own context. Shapes with no f.229 attestation stay unread as s:<shape> (U). Every letter sign
carries '?' (M), as on f.229. Numerals as seen; {clear} -> w:word. Prints the shape map used.
Usage: python3 b167228/to_pipe.py   (run from the target folder)"""
import re, collections
LET = set('abcdefghilmnopqrstuxyz')
TOK = re.compile(r'\{[^}]*\}|\S+')
votes = collections.defaultdict(collections.Counter)
for f in ('passes/reconciled_b170f229r.tsv', 'passes/reconciled_b170f229v.tsv'):
    for ln in open(f, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('line\t') or not ln.strip():
            continue
        for t in TOK.findall(ln.split('\t', 1)[1]):
            t = t.rstrip('?')
            if t.startswith('s:') and '=' in t:
                shape, _, let = t[2:].partition('=')
                if let in LET:
                    votes[shape][let] += 1
SHAPE = {s: c.most_common(1)[0][0] for s, c in votes.items()}
# SIG-B228 (8 Oct 2026): shapes with no f.229 value get the external-exemplar value of b167228/sig_shape_map.tsv, if any
# (prereg_sig.md: two blind reads matched to Tomokiyo's block or a labelled f.229 tile, decoy gate passed); never from f.228 context.
import os
if os.path.exists('b167228/sig_shape_map.tsv'):
    for ln in open('b167228/sig_shape_map.tsv', encoding='utf-8'):
        if ln.startswith(('#', 'shape\t')) or not ln.strip():
            continue
        sh, let = ln.split('\t')[:2]
        SHAPE.setdefault(sh, let)
        print('external shape', sh, '->', let)
for s, c in sorted(votes.items()):
    print('f229 shape', s, dict(c), '->', SHAPE[s])
out = ['# Baluze 170 f.228r-v (same letter as f.229, 25 Aug 1640, Amiens, bare cipher passage), reconciled by D1-BAL170/D1-BAL170B',
       '# (passes/reconciled_b170f228{r,v}.tsv). B167-228, 8 Oct 2026: letter shapes given the f.229 values (majority per shape,',
       '# b167228/to_pipe.py); L:x? = letter sign, M; s:<shape> = shape with no f.229 value (unread). Numerals as seen.']
unread = collections.Counter()
# SIG-B228 (8 Oct 2026): numeral marks agreed by two blind reads on line strips (b167228/sig_marks.tsv, prereg_sig.md item 6,
# control gate 3/4 PASS) replace an unmarked numeral's transcription; keyed by line and numeral occurrence, code checked.
# SIG-V228 (9 Oct 2026, AUDIT.md '## AUDIT 1 f.228 (SIG-V228)' correction 1): the mark gate's control tested only present marks,
# and SIG-B228B found Sonnet mark detection unusable on this hand; the 15 regrades are withdrawn (tokens back to I via
# key_unmarked.tsv). sig_marks.tsv is kept as a record and no longer applied.
MARK = {}
if False and os.path.exists('b167228/sig_marks.tsv'):
    for ln in open('b167228/sig_marks.tsv', encoding='utf-8'):
        if ln.startswith('line\t') or not ln.strip():
            continue
        l, occ, code, mk = ln.split('\t')[:4]
        MARK[(l, int(occ))] = (code, mk)
# SIG-B228B (8 Oct 2026): per-token u4/4u override (b167228/sig2_shape_map.tsv, prereg_sig2.md: two blind reads matched the tile
# to the same f.229 exemplar, decoy gate 2/3 passed); keyed by line and cipher-token index (clear words not counted), shape checked.
OVR = {}
if os.path.exists('b167228/sig2_shape_map.tsv'):
    for ln in open('b167228/sig2_shape_map.tsv', encoding='utf-8'):
        if ln.startswith('line\t') or not ln.strip():
            continue
        l, col, val = ln.split('\t')[:3]
        OVR[(l, int(col))] = val
for f in ('passes/reconciled_b170f228r.tsv', 'passes/reconciled_b170f228v.tsv'):
    for ln in open(f, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('line\t') or not ln.strip():
            continue
        lid, toks = ln.rstrip('\n').split('\t')
        page, line = lid.split('_', 1)
        res = []
        lkey = lid.replace('b170f228', '').lstrip('_')
        nocc = 0
        ncol = 0
        for t in TOK.findall(toks):
            if not t.startswith('{'):
                ncol += 1
            if (lkey, ncol) in OVR and not t.startswith('{'):
                assert t.rstrip('?') == 's:u4', (lid, ncol, t)
                res.append('L:' + OVR.pop((lkey, ncol)) + '?')
                continue
            if re.fullmatch(r"\d+[':=]?\??", t):
                nocc += 1
                if (lkey, nocc) in MARK:
                    code, mk = MARK.pop((lkey, nocc))
                    assert t.rstrip("?':=") == code, (lid, nocc, t, code)
                    res.append(code + mk)
                    continue
            if t.startswith('{'):
                res += ['w:' + w for w in t[1:-1].split()]
                continue
            q = '?' if t.endswith('?') else ''
            t = t.rstrip('?')
            if t.startswith('s:'):
                shape = t[2:]
                if shape in SHAPE:
                    res.append('L:' + SHAPE[shape] + '?')
                else:
                    unread[shape] += 1
                    res.append('s:' + re.sub(r'[^A-Za-z0-9+|_]', '', shape) + '?')
            else:
                res.append(t + q)
        out.append(f'{page} {line} | ' + ' '.join(res))
assert not MARK, ('sig_marks rows not applied', MARK)
assert not OVR, ('sig2_shape_map rows not applied', OVR)
open('ciphertext_b170f228.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3, 'lines; unread shapes', dict(unread))
