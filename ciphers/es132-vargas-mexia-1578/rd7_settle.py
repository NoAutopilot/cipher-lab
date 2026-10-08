#!/usr/bin/env python3
"""rd7_settle.py -- fresh rule-7 re-derivation of the f.89 duplicate settlement (ES132-RD, account 4, 8 Oct 2026).

Written from PREREG_dupsettle.md, key.tsv and the transcription files only; it does NOT import settle_dup.py, test0.py's decoder
or test2's renderer. Steps:
 1. R1-R3 and the 50-token control of PREREG_dupsettle.md, re-implemented here, run on the frozen pre-settlement alignment
    (dup_settlements_pre.tsv, dup_align_pre.tsv) and the duplicate's blind passes (passes/f9*_passA/B.tsv) with the decisions in
    run2/decisions_f9*.tsv. The passes are tokenised by test2.shape_tok + norm_line (the transcription's own normalisation) with
    the per-token {CLEAR:} handling the decisions were indexed against (A3V3-ES9396).
 2. Each of the 119 candidate rows: own decision vs dup_settled.tsv; settled token vs the token now at that position in
    ciphertext_<page>.tsv; pre-settlement token reconstructed from dup_settled's old token.
 3. An own decoder of key.tsv (Cp.30; vowel indicators and marks as key.tsv's header states) decodes every settled token and every
    token of the four unprinted pages; compared with reading_f89r/f89v/f90r/f91r.txt token by token ([...] = code/unreadable).
Writes rd7_settle.tsv and rd7_settle_result.json; --check exits 1 if they are stale.
"""
import sys, re, json, random, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from test2 import shape_tok, norm_line  # transcription normalisation only

PAGES = ['f89r', 'f89v', 'f90r', 'f91r']
DUP = ['f93r', 'f93v', 'f94r', 'f94v', 'f95r']
ANCHOR = ('same', 'variant', 'notation')


def key():
    k, under = {}, {}
    for l in open(HERE / 'key.tsv', encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        s, v = l.rstrip('\n').split('\t')[:2]; k[s] = v
    k['35_'] = 'pl'  # key.tsv header: "35_ (underlined) = pl"
    return k


VOW = {'+': 'a', '.': 'e', 'σ': 'i', 'ρ': 'o', '⊣': 'u'}
PARSE = re.compile(r'^(\{[^}]+\}|\d+|[A-Za-z]+)(_?)([+.σρ⊣]?)((?:@[a-z0-9]+)*)(\??)$')


def decode(t, K):
    """text, or None when the token is a code word / number outside the table / unparsable."""
    if t == '/': return ''
    m = PARSE.match(t)
    if not m: return None
    b, u, v, marks, _ = m.groups()
    if b.startswith('{') or '@c' in marks: return None
    s = K.get(b + u) if u else K.get(b)
    if s is None: return None
    if v: s += ('u' if s == 'q' else '') + VOW[v]
    return s + ''.join(re.findall(r'@([lmnrs])', marks))


def tsv_lines(p):
    return {l.split('\t', 1)[0]: l.rstrip('\n').split('\t', 1)[1].split() for l in open(p, encoding='utf-8')
            if not l.startswith('#') and '\t' in l}


def passes(p):
    L = {}
    for l in open(p, encoding='utf-8'):
        if l.startswith('#') or '\t' not in l or not l.strip(): continue
        a, b = l.rstrip('\n').split('\t', 1)
        L[a.strip()] = norm_line(' '.join(x for x in (shape_tok(t) for t in b.split()) if x)).split()
    return L


def agreement():
    ag = {}
    for pg in DUP:
        D = {}
        for l in open(HERE / f'run2/decisions_{pg}.tsv', encoding='utf-8'):
            if l.startswith('#') or not l.strip(): continue
            c = (l.rstrip('\n').split('\t') + [''])[:3]; D[(c[0], int(c[1]))] = c[2]
        A, B = passes(HERE / f'passes/{pg}_passA.tsv'), passes(HERE / f'passes/{pg}_passB.tsv')
        rec = tsv_lines(HERE / f'ciphertext_{pg}.tsv')
        for ln in sorted(set(A) | set(B)):
            a, b, k = A.get(ln, []), B.get(ln, []), 0
            for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, [t.rstrip('?') for t in a], [t.rstrip('?') for t in b],
                                                              autojunk=False).get_opcodes():
                if op == 'equal':
                    for _ in range(i2 - i1): k += 1; ag[(pg, ln, k)] = True
                    continue
                d = D[(ln, i1 + 1)]
                n = {'A': i2 - i1, 'A?': i2 - i1, 'B': j2 - j1, 'B?': j2 - j1}.get(d, len(d.split()))
                for _ in range(n): k += 1; ag[(pg, ln, k)] = False
            if k != len(rec.get(ln, [])): raise SystemExit(f'agreement walk {pg} {ln}: {k} vs {len(rec.get(ln, []))}')
    return ag


def P(s):
    p, ln, i = s.split(':'); return (p, ln, int(i))


def rule(row, idx, align, AG):
    if not AG.get(P(row[3]), False): return 'keep:R1-not-agreed', None
    if row[6] in ANCHOR: return 'flag-removed', row[1].rstrip('?')
    before = align[idx - 1][6] if idx else 'edge'
    after = align[idx + 1][6] if idx + 1 < len(align) else 'edge'
    if before not in ANCHOR or after not in ANCHOR: return 'keep:R3a-not-isolated', None
    if re.match(r'^(14|0|rum|rom|\{R)', row[4]): return 'keep:R3b-notation-form', None
    return 'replaced', row[4]


def main():
    K, AG = key(), agreement()
    align = [l.rstrip('\n').split('\t') for l in open(HERE / 'dup_align_pre.tsv', encoding='utf-8') if not l.startswith('#')]
    where = {(r[0], r[3]): i for i, r in enumerate(align)}
    committed = [l.rstrip('\n').split('\t') for l in open(HERE / 'dup_settled.tsv', encoding='utf-8') if not l.startswith('#')]
    cmap = {(r[0], r[3]): r for r in committed}
    ct = {pg: tsv_lines(HERE / f'ciphertext_{pg}.tsv') for pg in PAGES + ['f90v']}
    rd = {pg: {l.split('\t', 1)[0]: l.rstrip('\n').split('\t', 1)[1].split() for l in open(HERE / f'reading_{pg}.txt', encoding='utf-8')
               if '\t' in l} for pg in PAGES}
    out, diffs = [], []
    for l in open(HERE / 'dup_settlements_pre.tsv', encoding='utf-8'):
        if l.startswith('#'): continue
        xpos, x, y, ypos, act, kind = l.rstrip('\n').split('\t')
        i = where[(xpos, ypos)]
        dec, new = ('not-applied:teulet-f90v-known-answer', None) if kind != 'unprinted' else rule(align[i], i, align, AG)
        new_tok = new or x
        c = cmap.get((xpos, ypos))
        pg, ln, k = P(xpos)
        now = ct[pg].get(ln, [])[k - 1] if k <= len(ct[pg].get(ln, [])) else None
        txt = decode(new_tok, K)
        # reading_<page>.txt drops '/' tokens; map ciphertext index to reading index
        rtok = None
        if pg in rd:
            nslash = sum(t == '/' for t in ct[pg][ln][:k - 1])
            rl = rd[pg].get(ln, []); rtok = rl[k - 1 - nslash] if k - 1 - nslash < len(rl) else None
        exp = ('[' + new_tok + ']') if txt is None else txt
        ok = dict(decision=c is not None and c[5] == dec, token=c is not None and c[6] == new_tok, ciphertext=now == new_tok,
                  reading=(pg not in rd) or rtok == exp)
        out.append([xpos, x, y, dec, new_tok, c[6] if c else '-', now or '-', exp, rtok or '-'] + ['ok' if all(ok.values()) else
                    'DIFF:' + ','.join(n for n, v in ok.items() if not v)])
        if not all(ok.values()): diffs.append(out[-1])
    # PREREG control, re-run
    pop = [i for i, r in enumerate(align) if r[0] != '-' and r[3] != '-' and P(r[0])[0] in PAGES and not r[1].endswith('?')
           and not r[4].endswith('?')]
    rep = lambda ix: sum(rule(align[i], i, align, AG)[0] == 'replaced' for i in ix)
    s50 = sorted(random.Random(1578).sample(pop, 50))
    # whole-page decode against the committed readings
    page_cmp = {}
    for pg in PAGES:
        n = d = 0; bad = []
        for ln, toks in ct[pg].items():
            mine = [('[' + t + ']') if decode(t, K) is None else decode(t, K) for t in toks if t != '/']
            got = rd[pg].get(ln, [])
            n += max(len(mine), len(got))
            for j in range(max(len(mine), len(got))):
                a = mine[j] if j < len(mine) else None; b = got[j] if j < len(got) else None
                if a != b: d += 1; bad.append(f'{ln}:{j + 1} {a} != {b}')
        page_cmp[pg] = dict(tokens=n, differ=d, first=bad[:5])
    dec_count = {}
    for r in out: dec_count[r[3]] = dec_count.get(r[3], 0) + 1
    res = dict(job='ES132-RD rule-7 re-derivation', rows=len(out), decisions=dec_count, rows_differing=len(diffs),
               settled_applied=sum(r[3] in ('flag-removed', 'replaced') for r in out),
               settled_key_decodable=sum(r[3] in ('flag-removed', 'replaced') and not r[7].startswith('[') for r in out),
               control_50=dict(n=50, replaced=rep(s50), gate_pass=rep(s50) <= 2),
               control_all_firm=dict(n=len(pop), replaced=rep(pop)), page_decode_vs_reading=page_cmp)
    outs = {'rd7_settle.tsv': '# rd7_settle.py (ES132-RD): f89_pos old_tok dup_tok decision_rd settled_tok_rd settled_tok_committed '
                              'ciphertext_now decoded_rd reading_committed verdict\n' + '\n'.join('\t'.join(r) for r in out) + '\n',
            'rd7_settle_result.json': json.dumps(res, indent=1, ensure_ascii=False) + '\n'}
    if '--check' in sys.argv:
        stale = [f for f, v in outs.items() if not (HERE / f).exists() or (HERE / f).read_text(encoding='utf-8') != v]
        print('STALE ' + ' '.join(stale) if stale else 'OK: committed outputs match'); sys.exit(1 if stale else 0)
    for f, v in outs.items(): (HERE / f).write_text(v, encoding='utf-8')
    print(json.dumps(res, ensure_ascii=False))


if __name__ == '__main__':
    main()
