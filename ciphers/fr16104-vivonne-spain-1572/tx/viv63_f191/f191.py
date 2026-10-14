#!/usr/bin/env python3
"""VIV-F191 (14 Oct 2026): f.191r (ink 63) four-pass reconciliation, re-decode and statistics, PREREG-VIVF191.md.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv63_f191/f191.py [--stats] [--check]

Passes: A, B = tx/f191r_passA/B.tsv (N6-VIV63, first-cut crops); C, D = viv63_f191/f191r_passC/D.tsv (blind Sonnet, region-
deskewed crops, VIV-F191). Each cleaned with tx/viv63_clean.py's rules (copied: that script runs at import). Columns: star
alignment on A with tools/reconcile_passes.columns (NW); insertion columns after the same A sign are paired across passes by
their order within each pass (the shared tool lists each pass's insertion as its own column; implementation note, NOTES).
Rule (PREREG 3): >= 3 of 4 votes -> settled (a '-' majority drops the column); 2-2 on a tx/viv63_decode RULES pair -> the rule's
sign, settled; else the plurality sign (ties: C if C == D, else A's), FLAGGED; a strict '-' plurality drops the column.
Writes rec.tsv, decode.tsv (never reading_piece63.tsv); --stats also stats.json + owner_questions.tsv; --check: rec/decode stale -> 1.
"""
import collections, json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TX = os.path.dirname(HERE)
T = os.path.dirname(TX)
ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, TX); sys.path.insert(0, os.path.join(ROOT, 'tools'))
import reconcile_passes as rp  # noqa: E402
import reconcile_vivk as rv  # noqa: E402
import viv54_decode as vd  # noqa: E402
import viv63_decode as v63  # noqa: E402

PASSES = {'A': os.path.join(TX, 'f191r_passA.tsv'), 'B': os.path.join(TX, 'f191r_passB.tsv'),
          'C': os.path.join(HERE, 'f191r_passC.tsv'), 'D': os.path.join(HERE, 'f191r_passD.tsv')}
SEED = '20261014VIVF191'


def clean(path):
    out = {}
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('row\t') or not ln.strip():
            continue
        row, codes = (ln.rstrip('\n').split('\t', 1) + [''])[:2]
        if codes.strip().upper() == 'DUP':
            continue
        codes = re.sub(r'\[PLAIN:[^\]]*\]', ' ', codes)
        codes = re.sub(r'\[[^\]]*\]', ' ', codes)
        codes = re.sub(r'(?:^|\s)[H@]\?? n o n(?=\s|$)', ' ', codes)
        toks = [('P' + t[1:] if t.startswith('π') else t).rstrip('?') for t in codes.split()]
        toks = [t for t in toks if t]
        if toks:
            out[row.strip()] = toks
    return out


def nw_agree(x, y):
    pr = rp.nw(x, y)
    return sum(1 for i, j in pr if i is not None and j is not None and x[i] == y[j]), len(pr)


def mapping(P):
    ids = sorted(P['A'])
    ok = 0
    rows = []
    for k, l in enumerate(ids):
        c = P['C'].get(l, [])
        s = lambda m: (lambda a: a[0] / max(1, a[1]))(nw_agree(c, P['A'].get(m, []))) if m else 0
        same = s(l); nb = max(s(ids[k - 1]) if k else 0, s(ids[k + 1]) if k + 1 < len(ids) else 0)
        ok += same > nb; rows.append((l, round(same, 3), round(nb, 3)))
    return ok, rows


def cols(P, line):
    seqs = [[(t, 'H', '') for t in P[p].get(line, [])] for p in 'ABCD']
    ref = seqs[0]
    cs = [[r[0]] + [None] * 3 for r in ref]
    extra = collections.defaultdict(lambda: collections.defaultdict(list))
    for p in (1, 2, 3):
        last = -1
        for i, j in rp.nw([c[0] for c in ref], [c[0] for c in seqs[p]]):
            if i is not None:
                cs[i][p] = seqs[p][j][0] if j is not None else None; last = i
            else:
                extra[last][p].append(seqs[p][j][0])
    def ins(anchor):
        e = extra.get(anchor)
        if not e:
            return []
        n = max(len(v) for v in e.values())
        return [[None] + [e[p][t] if t < len(e[p]) else None for p in (1, 2, 3)] for t in range(n)]
    out = ins(-1)
    for i, c in enumerate(cs):
        out.append(c); out += ins(i)
    return [[x if x is not None else '-' for x in c] for c in out]


def decide(c):
    v = collections.Counter(c)
    top, n = v.most_common(1)[0]
    if n >= 3:
        return (None, False, 'maj') if top == '-' else (top, False, 'maj')
    signs = [s for s in v if s != '-']
    if len(signs) == 2 and v[signs[0]] == 2 and v[signs[1]] == 2:
        w = v63.RULES.get(frozenset(signs))
        if w:
            return w, False, 'rule'
    best = max(v.values())
    tied = [s for s in v if v[s] == best]
    if len(tied) == 1:
        if tied[0] == '-':
            return None, False, 'drop'
        return tied[0], True, 'plural'
    if c[2] == c[3] and c[2] != '-':
        return c[2], True, 'tieCD'
    if c[0] != '-':
        return c[0], True, 'tieA'
    return [s for s in tied if s != '-'][0], True, 'tie'


def build():
    P = {p: clean(f) for p, f in PASSES.items()}
    lines = {}
    rec = ['line\tpos\tsign\tflag\thow\tA\tB\tC\tD']
    for line in sorted(P['A']):
        toks = []
        for c in cols(P, line):
            s, flag, how = decide(c)
            if s is None:
                continue
            toks.append([rv.MAP.get(s, s), flag, how, c])
        seq, i = [], 0
        while i < len(toks):
            if toks[i][0] == 'o' and i + 1 < len(toks) and toks[i + 1][0] == 'o':
                seq.append(['oo', toks[i][1] or toks[i + 1][1], toks[i][2] + '+' + toks[i + 1][2],
                            ['+'.join(z) for z in zip(toks[i][3], toks[i + 1][3])]]); i += 2
            else:
                seq.append(toks[i]); i += 1
        lines[line] = seq
        for k, (s, flag, how, c) in enumerate(seq, 1):
            rec.append(f'{line}\t{k}\t{s}\t{int(flag)}\t{how}\t' + '\t'.join(c))
    k = vd.key()
    dec = ['line\tcodes\tdecode\tgrades']
    for line, seq in lines.items():
        d, g = '', ''
        for s, flag, _, _ in seq:
            if s not in k:
                d += '_'; g += 'U'
            else:
                d += k[s][0]; g += 'M' if (flag or k[s][1] == 'M') else 'H'
        dec.append(f'{line}\t{" ".join(x[0] for x in seq)}\t{d}\t{g}')
    return P, lines, '\n'.join(rec) + '\n', '\n'.join(dec) + '\n'


def before_lines():
    return {l: [[c, f, '', None] for c, f in seq] for l, seq in v63.page_tokens('f191r')[0].items()}


def page_letters(lines):
    k = vd.key(); s, meta = [], []
    for line in sorted(lines):
        for pos, (c, flag, how, cv) in enumerate(lines[line], 1):
            if c not in k:
                s.append('_'); meta.append(dict(line=line, pos=pos, code=c, g='U', votes=cv)); continue
            s.append(k[c][0]); meta.append(dict(line=line, pos=pos, code=c, g='M' if (flag or k[c][1] == 'M') else 'H',
                                                votes=cv, how=how))
    return ''.join(s), meta


def longest_H(s, meta):
    best, i = (0, 0, 0), 0
    while i < len(s):
        if meta[i]['g'] == 'H':
            j = i
            while j < len(s) and meta[j]['g'] == 'H':
                j += 1
            best = max(best, (j - i, i, j)); i = j
        else:
            i += 1
    n, b, e = best
    return dict(letters=n, text=s[b:e], lines=f"{meta[b]['line']}-{meta[e - 1]['line']}" if n else '')


def stats(P, lines):
    import viv63_test as t, viv53G_decode as g, viv53L_stretches as st, judge_plaintext as jp, vivanchor_gates as va, vivk_test as vt
    res = {'seed': SEED}
    # (a) err_2reader per pair
    pairs = {}
    names = 'ABCD'
    for x in range(4):
        for y in range(x + 1, 4):
            a = c = 0
            for l in P['A']:
                ag, n = nw_agree(P[names[x]].get(l, []), P[names[y]].get(l, []))
                a += ag; c += n
            pairs[names[x] + names[y]] = round(1 - a / max(1, c), 3)
    res['err_2reader'] = pairs
    res['line_mapping'] = dict(zip(('same_id_best_of_36', 'rows'), mapping(P)))
    B = before_lines()
    for tag, L in (('before', B), ('after', lines)):
        s, meta = page_letters(L)
        cnt = collections.Counter(m['g'] for m in meta)
        res[tag] = {'tokens': len(meta), 'grades': dict(cnt), 'longest_H_run': longest_H(s, meta)}
    # (c) gates
    t.SEED = SEED
    kk = {c: v for c, (v, gg) in vd.key().items()}
    model = jp.NgramModel([jp.read_corpus(p) for p in t.FR16])
    c1 = vt.tokens(os.path.join(TX, 'f103r_rec.tsv'))
    c54 = [c for page in ('f173r', 'f173v') for _, seq in sorted(vd.page_tokens(page).items()) for c, _ in seq]
    res['C1_f103r'], _ = t.run(model, kk, c1, 200, 'C1')
    res['C2_ink54'], _ = t.run(model, kk, c54, 200, 'C2')
    ctrl = all(res[c]['b2']['pass'] and res[c]['b2']['headroom_ok'] for c in ('C1_f103r', 'C2_ink54'))
    for tag, L in (('before', B), ('after', lines)):
        seq = [x[0] for l in sorted(L) for x in L[l]]
        r, _ = va.wrong(model, kk, seq, 200, 200, SEED + '-' + tag, 'T' + tag)
        r['verdict_b2'] = ('PASS' if r['b2']['pass'] else 'FAIL') if ctrl else 'not a gate'
        r['verdict_wrong_keys'] = 'PASS' if r['c']['pass'] else 'FAIL'
        res[tag]['gates'] = r
    # (d)/(e) V_strict stretches
    V, form = g.strict_vocab()
    res['V_strict'] = len(V)
    for tag, L in (('before', B), ('after', lines)):
        s, meta = page_letters(L)
        tops = st.top(s, V, 5)
        rng = random.Random(SEED + '-stretch-' + tag); t1, t3 = [], []
        segs = s.split('_')
        for _ in range(200):
            flat = list(''.join(segs)); rng.shuffle(flat); it = iter(flat)
            lens = [x[0] for x in st.top('_'.join(''.join(next(it) for _ in sg) for sg in segs), V, 3)]
            lens += [0] * (3 - len(lens)); t1.append(lens[0]); t3.append(sum(lens[:3]) / 3)
        t1.sort(); t3.sort()
        out = []
        for ln, b, e, words in tops:
            m = meta[b:e]
            out.append(dict(letters=ln, lines=f"{m[0]['line']}-{m[-1]['line']}", decoded=s[b:e], words=' '.join(words),
                            grades=''.join(x['g'] for x in m), nonH=sum(x['g'] != 'H' for x in m), b=b, e=e))
        res[tag]['stretch'] = {'top': out, 'real_top1': out[0]['letters'] if out else 0,
                               'real_top3mean': round(sum(o['letters'] for o in out[:3]) / 3, 2),
                               'null_top1_median': jp.pct(t1, 0.5), 'null_top1_p99': jp.pct(t1, 0.99),
                               'null_top3mean_p99': round(jp.pct(t3, 0.99), 2)}
        res[tag]['clears_42_clean'] = any(o['letters'] >= 42 and o['nonH'] == 0 for o in out)
        if tag == 'after':
            q = ['stretch\tstretch_lines\tline\tpos\tcode\tletter\tgrade\thow\tvotes_ABCD\ttile']
            for si, o in enumerate(out, 1):
                for i in range(o['b'], o['e']):
                    m = meta[i]
                    if m['g'] == 'H':
                        continue
                    n = len(lines[m['line']])
                    tile = f"c196_f191r_dr_{m['line']}_s{1 if m['pos'] <= n * 0.55 else 2}"
                    q.append(f"{si}\t{o['lines']}\t{m['line']}\t{m['pos']}\t{m['code']}\t{s[i]}\t{m['g']}\t{m.get('how', '')}\t"
                             f"{'/'.join(m['votes'] or [])}\t{tile}")
            open(os.path.join(HERE, 'owner_questions.tsv'), 'w').write('\n'.join(q) + '\n')
    for tag in ('before', 'after'):
        for o in res[tag]['stretch']['top']:
            o.pop('b'); o.pop('e')
    json.dump(res, open(os.path.join(HERE, 'stats.json'), 'w'), indent=1, ensure_ascii=False)
    return res


def main():
    P, lines, rec, dec = build()
    files = {os.path.join(HERE, 'rec.tsv'): rec, os.path.join(HERE, 'decode.tsv'): dec}
    if '--check' in sys.argv:
        stale = [p for p, x in files.items() if not os.path.exists(p) or open(p, encoding='utf-8').read() != x]
        print('viv63_f191 rec/decode', 'up to date' if not stale else 'STALE: ' + ', '.join(stale)); sys.exit(1 if stale else 0)
    for p, x in files.items():
        open(p, 'w', encoding='utf-8').write(x)
    hows = collections.Counter(x[2] for seq in lines.values() for x in seq)
    print('tokens', sum(len(v) for v in lines.values()), dict(hows))
    if '--stats' in sys.argv:
        r = stats(P, lines)
        print(json.dumps({k: r[k] for k in ('err_2reader',)}, ensure_ascii=False))
        print('mapping same-id best', r['line_mapping']['same_id_best_of_36'])
        for tag in ('before', 'after'):
            x = r[tag]; gt = x['gates']
            print(tag, x['tokens'], x['grades'], 'longestH', x['longest_H_run'], '| b2', gt['s'], gt['b2']['null_p99'], gt['verdict_b2'],
                  '| wrong', gt['c']['real_margin'], gt['c']['margin_p99'], gt['verdict_wrong_keys'],
                  '| stretch', x['stretch']['real_top1'], x['stretch']['real_top3mean'], 'null', x['stretch']['null_top1_median'],
                  x['stretch']['null_top1_p99'], '| clears42', x['clears_42_clean'])
            for o in x['stretch']['top']:
                print('   ', o['letters'], o['lines'], o['words'], o['grades'])
        for c in ('C1_f103r', 'C2_ink54'):
            print(c, r[c]['s'], r[c]['b2'])


if __name__ == '__main__':
    main()
