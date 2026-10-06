#!/usr/bin/env python3
"""R7A-VIV53 (6 Oct 2026): ink 53 re-decode after the gap-tile window re-read, under PREREG-R7VIV53G.md.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53G_decode.py [--check]
    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53G_decode.py --decoys     # (ii) control gate only
    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53G_decode.py --gates      # (iv) b2 + wrong keys + V_strict stretches

Inputs per page: tx/lookalike53L/<page>/passD.tsv + agreement.tsv (the N7-VIV53L primary) and tx/lookalike53G/<page>/items.tsv +
53G_<page>_reread.tsv (the blind window re-read). Decoy gate (ii): firm-correct >= 0.80 and firm-NONE <= 0.10 over all decoys,
else nothing is folded in. Fold-in (iii): a gap tile whose firm (H/M) re-read equals its present label (same code after the MAP)
is settled present; firm NONE removes the token; anything else leaves it as N7-VIV53L had it (flagged). Everything after that is
tx/viv53L_decode.py's page_tokens() logic unchanged. Writes reading_piece53_G.tsv and piece53_G_decode.txt (--check: exit 1 if stale);
--gates writes tx/viv53G_result.json.
"""
import csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv53L_decode as vl  # noqa: E402

PAGES = vl.PAGES
MAP = vl.MAP
FIRM = ('H', 'M')


def answers(page):
    d = os.path.join(HERE, 'lookalike53G', page)
    its = {r['item']: r for r in csv.DictReader(open(os.path.join(d, 'items.tsv')), delimiter='\t')}
    rr = {r['item'].strip(): r for r in csv.DictReader(open(os.path.join(d, f'53G_{page}_reread.tsv')), delimiter='\t')}
    out = []
    for i, it in its.items():
        a = rr.get(i, {})
        out.append(dict(it, ans=(a.get('label') or '').strip(), conf=(a.get('conf') or '').strip().upper()))
    return out


def decoys():
    n = ok = none = 0
    for p in PAGES:
        for a in answers(p):
            if a['kind'] != 'decoy':
                continue
            n += 1
            firm = a['conf'] in FIRM
            ok += firm and MAP.get(a['ans'], a['ans']) == MAP.get(a['label'], a['label'])
            none += firm and a['ans'] == 'NONE'
    return dict(n=n, correct=ok, none=none, correct_rate=round(ok / n, 3), none_rate=round(none / n, 3),
                pass_=ok / n >= 0.80 and none / n <= 0.10)


def verdicts(page):
    """(passage, pos) -> 'present' | 'absent' | 'kept' for the gap tiles; plus counts for the report."""
    v, cnt = {}, {'present': 0, 'absent': 0, 'kept': 0, 'echo': 0, 'none': 0, 'other': 0}
    for a in answers(page):
        if a['kind'] != 'gap':
            continue
        same = MAP.get(a['ans'], a['ans']) == MAP.get(a['label'], a['label'])
        cnt['echo' if same else 'none' if a['ans'] == 'NONE' else 'other'] += 1
        firm = a['conf'] in FIRM
        r = 'present' if firm and same else 'absent' if firm and a['ans'] == 'NONE' else 'kept'
        v[(a['passage'], a['pos'])] = r; cnt[r] += 1
    return v, cnt


def page_tokens(page, fold=True):
    d = os.path.join(HERE, 'lookalike53L', page)
    st = {(r['passage'], r['posA']): r['status'] for r in csv.DictReader(open(os.path.join(d, 'agreement.tsv')), delimiter='\t')}
    gv = verdicts(page)[0] if fold else {}
    rows = {}
    for r in csv.DictReader(open(os.path.join(d, 'passD.tsv')), delimiter='\t'):
        s = st[(r['passage'], r['pos'])]
        g = gv.get((r['passage'], r['pos']))
        if g == 'absent':
            continue
        settled = s == 'agree' or (s == 'split' and r['note'] in vl.SETTLE) or (s == 'gap' and g == 'present')
        lab = MAP.get(r['sign_id'], r['sign_id'])
        rows.setdefault(r['passage'].split('_', 1)[1], []).append(
            (lab, not settled, 'K' if (s == 'split' and settled) or (s == 'gap' and g == 'present') else ''))
    out = {}
    for line, toks in rows.items():
        seq, i = [], 0
        while i < len(toks):
            if toks[i][0] == 'o' and i + 1 < len(toks) and toks[i + 1][0] == 'o':
                seq.append(('oo', toks[i][1] or toks[i + 1][1], toks[i][2] + toks[i + 1][2])); i += 2
            else:
                seq.append(toks[i]); i += 1
        seq2, i = [], 0
        while i < len(seq):
            if seq[i][0] == ':' and i + 1 < len(seq) and seq[i + 1][0] == ':':
                seq2.append((':', seq[i][1] or seq[i + 1][1], 'J' + seq[i][2] + seq[i + 1][2])); i += 2
            else:
                seq2.append(seq[i]); i += 1
        out[line] = seq2
    return out


def build():
    fold = decoys()['pass_']
    orig = vl.page_tokens
    vl.page_tokens = lambda p: page_tokens(p, fold)
    try:
        return vl.build()
    finally:
        vl.page_tokens = orig


def strict_vocab():
    import collections, re
    import viv63_test as t
    import judge_plaintext as jp
    import viv54L_stretch as s4
    cnt = collections.Counter()
    for p in t.FR16:
        for w in re.findall(r"[^\W\d_]+", jp.read_corpus(p).lower()):
            n = re.sub('[^a-z]', '', jp.fold(w)).replace('v', 'u').replace('j', 'i')
            if n:
                cnt[n] += 1
    V = {w for w, c in cnt.items() if c >= 100 and len(w) >= 3} | set(s4.STRICT_SHORT)
    return V, {w: w for w in V}


def stretches(mod_tokens, V, form, nnull, seed):
    import viv53L_stretches as st
    import judge_plaintext as jp
    orig = st.vl.page_tokens
    st.vl.page_tokens = mod_tokens
    try:
        P = st.pages()
    finally:
        st.vl.page_tokens = orig
    allst = []
    for page, (s, meta) in P.items():
        for ln, b, e, words in st.top(s, V, 5):
            m = meta[b:e]; lines = sorted({x['line'] for x in m})
            allst.append(dict(page=page, lines=f'{lines[0]}-{lines[-1]}' if len(lines) > 1 else lines[0], letters=ln, decoded=s[b:e],
                              words=' '.join(words), n_words=len(words), M=sum(x['M'] for x in m), K=sum(x['K'] for x in m),
                              J=sum(x['J'] for x in m), line_ends=len(lines) - 1))
    allst.sort(key=lambda r: -r['letters'])
    rng = random.Random(seed); t1, t3 = [], []
    for _ in range(nnull):
        lens = []
        for s, _m in P.values():
            segs = s.split('_'); flat = list(''.join(segs)); rng.shuffle(flat); it = iter(flat)
            lens += [x[0] for x in st.top('_'.join(''.join(next(it) for _ in seg) for seg in segs), V, 3)]
        lens.sort(reverse=True); t1.append(lens[0]); t3.append(sum(lens[:3]) / 3)
    t1.sort(); t3.sort()
    return {'top': allst[:10], 'real_top1': allst[0]['letters'], 'real_top3mean': round(sum(r['letters'] for r in allst[:3]) / 3, 2),
            'null_top1_median': jp.pct(t1, 0.5), 'null_top1_p99': jp.pct(t1, 0.99),
            'null_top3mean_median': round(jp.pct(t3, 0.5), 2), 'null_top3mean_p99': round(jp.pct(t3, 0.99), 2)}


def gates(draws=200, nwrong=200):
    import viv63_test as t, viv54_decode as vd, viv53b_test as vb, vivk_test as vt, judge_plaintext as jp
    SEED = '20261053G'
    k = {c: v for c, (v, g) in vd.key().items()}
    model = jp.NgramModel([jp.read_corpus(p) for p in t.FR16])
    t.SEED = SEED
    fold = decoys()['pass_']
    c1 = vt.tokens(os.path.join(HERE, 'f103r_rec.tsv'))
    c2 = [c for page in ('f173r', 'f173v') for _, seq in sorted(vd.page_tokens(page).items()) for c, _ in seq]
    pages = {p: [c for _, seq in sorted(page_tokens(p, fold).items()) for c, _, _ in seq] for p in PAGES}
    whole = [c for p in PAGES for c in pages[p]]
    res = {'seed': SEED, 'draws': draws, 'decoys': decoys(), 'fold_applied': fold,
           'gap_verdicts': {p: verdicts(p)[1] for p in PAGES}}
    res['C1_full'], _ = t.run(model, k, c1, draws, 'C1')
    res['C2_full'], _ = t.run(model, k, c2, draws, 'C2')
    res['whole'], _ = t.run(model, k, whole, draws, 'whole')
    res['verdict_b_ii'] = vb.gate(res, ('C1_full', 'C2_full'), 'whole')
    codes = sorted(k); rng = random.Random(SEED + '-wrong'); margins, passes = [], 0
    for i in range(nwrong):
        v = [k[c] for c in codes]; rng.shuffle(v)
        r, _ = t.run(model, dict(zip(codes, v)), whole, draws, f'wrong{i}')
        margins.append(r['s'] - r['b2']['null_p99']); passes += r['b2']['pass']
    margins.sort()
    real_m = res['whole']['s'] - res['whole']['b2']['null_p99']; p99 = jp.pct(margins, 0.99)
    res['c'] = {'wrong_keys': nwrong, 'b2_passes': passes, 'share': round(passes / nwrong, 3),
                'margin_median': round(jp.pct(margins, 0.5), 4), 'margin_p99': round(p99, 4), 'margin_max': round(margins[-1], 4),
                'real_margin': round(real_m, 4), 'pass': real_m > p99}
    V, form = strict_vocab()
    res['V_strict'] = len(V)
    res['stretch_before_53L'] = stretches(vl.page_tokens, V, form, 200, SEED + '-stretch')
    res['stretch_after_53G'] = stretches(lambda p: page_tokens(p, fold), V, form, 200, SEED + '-stretch')
    json.dump(res, open(os.path.join(HERE, 'viv53G_result.json'), 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({x: res[x] for x in ('decoys', 'fold_applied', 'gap_verdicts', 'verdict_b_ii', 'c', 'V_strict')}, indent=1))
    for x in ('C1_full', 'C2_full', 'whole'):
        print(x, res[x]['letters'], res[x]['s'], 'b2 p99', res[x]['b2']['null_p99'], res[x]['b2']['pass'], res[x]['b2']['headroom_ok'])
    for x in ('stretch_before_53L', 'stretch_after_53G'):
        r = res[x]
        print(x, 'top1', r['real_top1'], 'top3', r['real_top3mean'], 'null med/p99', r['null_top1_median'], r['null_top1_p99'],
              r['null_top3mean_median'], r['null_top3mean_p99'])
        for s in r['top'][:5]:
            print('  ', s['page'], s['lines'], s['letters'], 'M', s['M'], 'K', s['K'], 'J', s['J'], 'ends', s['line_ends'], '|', s['words'])


def main():
    if '--decoys' in sys.argv:
        print(json.dumps(decoys())); return
    if '--gates' in sys.argv:
        return gates()
    text, letters, n, joins = build()
    p1, p2 = os.path.join(T, 'reading_piece53_G.tsv'), os.path.join(T, 'piece53_G_decode.txt')
    if '--check' in sys.argv:
        ok = all(os.path.exists(p) and open(p, encoding='utf-8').read() == s for p, s in ((p1, text), (p2, letters)))
        print('reading_piece53_G.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(p1, 'w', encoding='utf-8').write(text); open(p2, 'w', encoding='utf-8').write(letters)
    tot = sum(n.values())
    print(f'tokens {tot}: H {n["H"]} M {n["M"]} U {n["U"]}; ": :" pairs joined {joins}; letters {len(letters) - 1}')
    for p in PAGES:
        print(p, verdicts(p)[1])


if __name__ == '__main__':
    main()
