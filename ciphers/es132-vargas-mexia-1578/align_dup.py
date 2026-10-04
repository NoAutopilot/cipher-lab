#!/usr/bin/env python3
"""align_dup.py -- token-by-token DP alignment of the duplicate cipher copy (f.93r-f.95r) of Philip II's 19 Sept 1578
letter against the f.89 letter (f.89r-f.91r) (A3V3-ES9396, 4 Oct 2026). Reads only committed ciphertext_*.tsv and key.tsv;
changes no reading and no key.

Alignment: global over the duplicate, free end gaps on the f.89 side (semi-global; the duplicate may be transcribed only in
part), Needleman-Wunsch with scores exact 4, same decoded text 2 (test0.dec_tok with key.tsv), same base number 1, other -2,
gap -3. Tokens are compared without '?' and without '{CLEAR...}' tokens (dropped, as test2 does).

Classes per aligned pair (f.89 token x, duplicate token y):
  same      x == y (after stripping '?')
  variant   x != y but both decode to the same plaintext under key.tsv (homophone/notation choice by the clerk, or a mark
            the key ignores) -- counted as copy variant, not reader error
  differ    different decoded text (or one side undecodable) -- candidate reader error on one side, or a clerk's variant
  gap       a token present on one side only (indel)
err_true estimate = differ / (same + variant + differ) on aligned pairs whose both tokens are unflagged; reported with N.
Writes dup_align.tsv (every aligned row) and dup_settlements.tsv (each f.89 '?' token aligned to an unflagged duplicate
token: confirm / propose), prints the summary JSON. --check: exit 1 if the committed outputs are stale.
"""
import sys, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from test0 import load_key, load_lines, dec_tok

REF = ['f89r', 'f89v', 'f90r', 'f90v', 'f91r']
DUP = ['f93r', 'f93v', 'f94r', 'f94v', 'f95r']
UNPRINTED = {'f89r', 'f89v', 'f90r', 'f91r'}  # the 113 '?' tokens of NOTES.md are on these pages (f.90v is Teulet's)


def stream(pages):
    out = []
    for p in pages:
        f = HERE / ('ciphertext_%s.tsv' % p)
        if not f.exists(): continue
        L = load_lines(f)
        for ln, toks in L.items():
            for i, t in enumerate(toks):
                if t.startswith('{CLEAR') or t == '/': continue
                out.append((p, ln, i + 1, t))
    return out


def base(t):
    m = re.match(r'^(\{[^}]*\}|\d+|[A-Za-z]+)', t)
    return m.group(1) if m else t


def main():
    key = load_key()
    dec = lambda t: dec_tok(t, key)[0]
    R, D = stream(REF), stream(DUP)
    r = [t[3].rstrip('?') for t in R]; d = [t[3].rstrip('?') for t in D]
    rd = [dec(t) for t in r]; dd = [dec(t) for t in d]

    def sim(i, j):
        if r[i] == d[j]: return 4
        if rd[i] is not None and rd[i] == dd[j]: return 2
        if base(r[i]) == base(d[j]): return 1
        return -2
    G = -3
    n, m = len(r), len(d)
    # semi-global: free leading/trailing gaps in the reference (rows i), costed gaps in the duplicate (cols j)
    S = [[0.0] * (m + 1) for _ in range(n + 1)]
    P = [[0] * (m + 1) for _ in range(n + 1)]
    for j in range(1, m + 1): S[0][j] = S[0][j - 1] + G; P[0][j] = 2
    for i in range(1, n + 1): S[i][0] = 0; P[i][0] = 1
    for i in range(1, n + 1):
        Si, Sp = S[i], S[i - 1]
        for j in range(1, m + 1):
            a = Sp[j - 1] + sim(i - 1, j - 1); b = Sp[j] + G; c = Si[j - 1] + G
            if a >= b and a >= c: Si[j] = a; P[i][j] = 0
            elif b >= c: Si[j] = b; P[i][j] = 1
            else: Si[j] = c; P[i][j] = 2
    i = max(range(n + 1), key=lambda k: S[k][m]); i_end = i; j = m
    pairs = []
    while j > 0:
        if i == 0: pairs.append((None, j - 1)); j -= 1; continue
        p = P[i][j]
        if p == 0: pairs.append((i - 1, j - 1)); i -= 1; j -= 1
        elif p == 1: pairs.append((i - 1, None)); i -= 1
        else: pairs.append((None, j - 1)); j -= 1
    pairs.reverse(); i_start = i
    rows, cnt, cnt_clean = [], {}, {}
    sett = []
    for a, b in pairs:
        x = R[a] if a is not None else None; y = D[b] if b is not None else None
        if x is None or y is None: cls = 'gap'
        elif r[a] == d[b]: cls = 'same'
        elif rd[a] is not None and rd[a] == dd[b]: cls = 'variant'
        else: cls = 'differ'
        cnt[cls] = cnt.get(cls, 0) + 1
        clean = x is not None and y is not None and not x[3].endswith('?') and not y[3].endswith('?')
        if clean: cnt_clean[cls] = cnt_clean.get(cls, 0) + 1
        rows.append('\t'.join([
            '%s:%s:%d' % x[:3] if x else '-', x[3] if x else '-', (rd[a] or '') if x else '',
            '%s:%s:%d' % y[:3] if y else '-', y[3] if y else '-', (dd[b] or '') if y else '', cls]))
        if x and y and x[3].endswith('?') and not y[3].endswith('?'):
            act = 'confirm' if cls == 'same' else ('confirm-text' if cls == 'variant' else 'propose')
            sett.append('\t'.join(['%s:%s:%d' % x[:3], x[3], y[3], '%s:%s:%d' % y[:3], act, 'unprinted' if x[0] in UNPRINTED else 'teulet-f90v']))
    al = cnt_clean.get('same', 0) + cnt_clean.get('variant', 0) + cnt_clean.get('differ', 0)
    qref = [t for t in R[i_start:i_end] if t[3].endswith('?')]
    summary = dict(
        ref_tokens=len(R), dup_tokens=len(D), ref_span=('%s:%s:%d' % R[i_start][:3], '%s:%s:%d' % R[i_end - 1][:3]) if R and D else None,
        classes_all=cnt, classes_both_unflagged=cnt_clean, aligned_both_unflagged=al,
        err_true_upper=round(cnt_clean.get('differ', 0) / al, 4) if al else None,
        variant_rate=round(cnt_clean.get('variant', 0) / al, 4) if al else None,
        ref_q_in_span=len(qref), ref_q_in_span_unprinted=sum(t[0] in UNPRINTED for t in qref),
        settlements=dict(total=len(sett), unprinted=sum(s.endswith('unprinted') for s in sett),
                         confirm=sum('\tconfirm\t' in s for s in sett), confirm_text=sum('\tconfirm-text\t' in s for s in sett),
                         propose=sum('\tpropose\t' in s for s in sett)))
    outs = {
        'dup_align.tsv': '# align_dup.py (A3V3-ES9396): f89_pos f89_tok f89_text dup_pos dup_tok dup_text class\n' + '\n'.join(rows) + '\n',
        'dup_settlements.tsv': '# align_dup.py (A3V3-ES9396): f.89 \'?\' tokens aligned to an unflagged duplicate token. For a later rule-7 job; NOT applied.\n'
                               '# f89_pos\tf89_tok\tdup_tok\tdup_pos\taction\tpage_kind\n' + '\n'.join(sett) + '\n',
        'dup_align_summary.json': json.dumps(summary, indent=1, ensure_ascii=False) + '\n'}
    if '--check' in sys.argv:
        stale = [k for k, v in outs.items() if not (HERE / k).exists() or (HERE / k).read_text(encoding='utf-8') != v]
        print('STALE ' + ' '.join(stale) if stale else 'SAME'); sys.exit(1 if stale else 0)
    for k, v in outs.items(): (HERE / k).write_text(v, encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == '__main__':
    main()
