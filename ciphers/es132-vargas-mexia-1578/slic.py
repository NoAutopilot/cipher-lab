#!/usr/bin/env python3
"""slic.py -- es132-vargas-mexia-1578 pre-registered S licence (ES132-SLIC, 8 Oct 2026), exactly as PREREG_slic.md says.

Gates: (a) held-out accuracy P19 -> P15 and P15 -> P19 (k = 2 confirmed cells, >= 0.90, >= 20 S tokens);
(b) 200 value-shuffled Cp.30 keys (test0.shuffled, seed 1578); (c) 20 seeds of injected misreads at the measured
pass-disagreement rate. Only if all pass: regrade of the unprinted target (H/C/S/M/U per letter, longest S stretch, AD).
Writes slic_result.json (and, if the gates pass, reading_slic_<letter>.txt); --check exits 1 if stale.
"""
import sys, json, random, difflib, math
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1] / 'tools'))
from passnorm import norm_line
from test0 import load_key, load_lines, dec_tok, norm, shuffled, TOK
from test2 import load_pass, strip_clear, err2

K = 2
VOWS = set('+.σρ⊣')


def t1(f):  # test 1's loader for the 3-4 Oct passes
    return {k: norm_line(' '.join(v)).split() for k, v in load_lines(HERE / f).items()}


def lp(f, clear=None):
    return load_pass(HERE / f, clear)


def cells(t):
    m = TOK.match(t)
    if not m: return None
    base, und, vow, above, q = m.groups()
    c = [('b', base + und)]
    if vow: c.append(('v', vow))
    c += [('m', a) for a in above.split('@') if a and a in 'lmnrs']
    return c


def agreed_pairs(A, B, lines):
    """list of agreed tokens (in reading order) over the given lines; tokens marked '?' in either pass are not agreed."""
    out = []
    for ln in lines:
        a, b = A.get(ln, []), B.get(ln, [])
        sm = difflib.SequenceMatcher(None, [t.rstrip('?') for t in a], [t.rstrip('?') for t in b], autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != 'equal': continue
            for i, j in zip(range(i1, i2), range(j1, j2)):
                if not a[i].endswith('?') and not b[j].endswith('?'): out.append(a[i])
    return out


def correct_flags(toks, key, ref):
    """per token: True/False if key-decodable (all letters of its normalised segment in a matching block), None otherwise."""
    segs = []
    for t in toks:
        txt, kind = dec_tok(t, key)
        segs.append(norm(txt) if kind == 'key' else None)
    dec = ''.join(s for s in segs if s)
    sm = difflib.SequenceMatcher(None, dec, ref, autojunk=False)
    ok = [False] * len(dec)
    for bl in sm.get_matching_blocks():
        for i in range(bl.a, bl.a + bl.size): ok[i] = True
    out, pos = [], 0
    for s in segs:
        if s is None: out.append(None); continue
        out.append(bool(s) and all(ok[pos:pos + len(s)])); pos += len(s)
    return out


def confirmed(toks, key, ref, k=K):
    cnt = {}
    for t, f in zip(toks, correct_flags(toks, key, ref)):
        if f:
            for c in cells(t): cnt[c] = cnt.get(c, 0) + 1
    return {c for c, n in cnt.items() if n >= k}


def licensed(t, key, conf):
    if dec_tok(t, key)[1] != 'key': return False
    c = cells(t)
    return bool(c) and all(x in conf for x in c)


def gate_a_dir(der, tst, key, k=K):
    conf = confirmed(der['toks'], key, der['ref'], k)
    fl = correct_flags(tst['toks'], key, tst['ref'])
    S = [f for t, f in zip(tst['toks'], fl) if licensed(t, key, conf)]
    n = len(S); good = sum(1 for f in S if f)
    return dict(cells=len(conf), S=n, S_correct=good, acc=round(good / n, 4) if n else 0.0,
                agreed_key=sum(1 for f in fl if f is not None), agreed_key_correct=sum(1 for f in fl if f))


def paragraphs(A19, B19, A15, B15):
    ref = lambda f: norm(''.join(l for l in open(HERE / f, encoding='utf-8') if not l.startswith('#')))
    return {'P19': dict(toks=agreed_pairs(A19, B19, ['L%02d' % i for i in range(10, 27)]), ref=ref('teulet_19sep1578.txt')),
            'P15': dict(toks=agreed_pairs(A15[0], B15[0], ['L%02d' % i for i in range(7, 14)])
                        + agreed_pairs(A15[1], B15[1], ['L%02d' % i for i in range(1, 5)]), ref=ref('teulet_15oct1578.txt'))}


def passes_ok(r):
    return all(r[d]['acc'] >= 0.90 and r[d]['S'] >= 20 for d in ('P19->P15', 'P15->P19'))


def run_a(P, key, k=K):
    return {'P19->P15': gate_a_dir(P['P19'], P['P15'], key, k), 'P15->P19': gate_a_dir(P['P15'], P['P19'], key, k)}


def pct(xs, q):
    xs = sorted(xs); return xs[min(len(xs) - 1, int(q * (len(xs) - 1)))]


# unprinted target: (letter, page, pass loader, lines)
TARGET = [
    ('19sep', 'f89r', 'lp', ['L%02d' % i for i in range(1, 24)]),
    ('19sep', 'f89v', 'lp', ['L%02d' % i for i in range(1, 41)]),
    ('19sep', 'f90r', 'lp', ['L%02d' % i for i in range(1, 41)]),
    ('19sep', 'f90v', 't1', ['L%02d' % i for i in range(1, 10)] + ['L27']),
    ('19sep', 'f91r', 'lp', ['L%02d' % i for i in range(1, 41)]),
    ('15oct', 'f119r', 't1', ['L%02d' % i for i in range(1, 21)]),
    ('15oct', 'f119vU', 'lp', ['L%02d' % i for i in range(1, 30)]),
    ('15oct', 'f119vL', 't1', ['L%02d' % i for i in range(2, 7)]),
    ('15oct', 'f120r', 'lp', ['L%02d' % i for i in range(5, 30)]),
]


CLEARCUT = {}


def load_target(page, loader):
    if page == 'f119vL':
        return t1('passes/passA.tsv'), t1('passes/passB.tsv'), load_lines(HERE / 'ciphertext.tsv')
    if loader == 't1':
        return t1(f'passes/{page}_passA.tsv'), t1(f'passes/{page}_passB.tsv'), load_lines(HERE / f'ciphertext_{page}.tsv')
    cA, cB = {}, {}
    A, B = lp(f'passes/{page}_passA.tsv', cA), lp(f'passes/{page}_passB.tsv', cB)
    R = strip_clear(load_lines(HERE / f'ciphertext_{page}.tsv'), page, cA, cB)
    CLEARCUT[page] = set(cA) | set(cB)
    return A, B, R


def agreed_in_R(R, A, B, ln):
    """per reconciled token: True iff equal (no '?') to the aligned token of pass A and of pass B."""
    r = R.get(ln, [])
    flags = [not t.endswith('?') for t in r]
    for P in (A, B):
        p = P.get(ln, []); hit = [False] * len(r)
        sm = difflib.SequenceMatcher(None, [t.rstrip('?') for t in r], [t.rstrip('?') for t in p], autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                for i, j in zip(range(i1, i2), range(j1, j2)):
                    hit[i] = r[i] == p[j]
        flags = [f and h for f, h in zip(flags, hit)]
    return flags


def main():
    key = load_key()
    A19, B19 = t1('passes/f90v_passA.tsv'), t1('passes/f90v_passB.tsv')
    A15 = (t1('passes/passA.tsv'), lp('passes/f120r_passA.tsv'))
    B15 = (t1('passes/passB.tsv'), lp('passes/f120r_passB.tsv'))
    res = {'prereg': 'PREREG_slic.md', 'k': K}
    # measured disagreement over the unprinted target lines (gate c input, computed first)
    d = n = 0
    T = {}
    for letter, page, loader, lines in TARGET:
        A, B, R = load_target(page, loader)
        T[page] = (A, B, R)
        dd, nn = err2({l: A.get(l, []) for l in lines}, {l: B.get(l, []) for l in lines})
        d += dd; n += nn
    r = d / n
    res['measured_err_2reader'] = f'{d}/{n}'; res['measured_r'] = round(r, 4)
    # (b) control first
    rng = random.Random(1578)
    shuf = [shuffled(key, rng) for _ in range(200)]
    P = paragraphs(A19, B19, A15, B15)
    res['known_answer'] = {p: dict(agreed_tokens=len(P[p]['toks']), ref_letters=len(P[p]['ref'])) for p in P}
    ctl = [run_a(P, k) for k in shuf]
    # (a)
    ga = run_a(P, key)
    res['gate_a'] = ga; res['gate_a_pass'] = passes_ok(ga)
    res['sensitivity_k'] = {str(kk): run_a(P, key, kk) for kk in (1, 3)}
    gb = {}
    ok_b = True
    for dname in ('P19->P15', 'P15->P19'):
        Sn = [c[dname]['S'] for c in ctl]; Ac = [c[dname]['acc'] for c in ctl]
        gb[dname] = dict(S_mean=round(sum(Sn) / 200, 2), S_p95=pct(Sn, 0.95), acc_mean=round(sum(Ac) / 200, 4), acc_p95=pct(Ac, 0.95),
                         true_S=ga[dname]['S'])
        gb[dname]['pass'] = bool(pct(Sn, 0.95) <= 0.25 * ga[dname]['S'] and pct(Ac, 0.95) < 0.90)
        ok_b &= gb[dname]['pass']
    res['gate_b'] = gb; res['gate_b_pass'] = ok_b
    # (c) injection at r/2 per pass, 25% mirrored
    inv = sorted({t for D in (A19, B19, *A15, *B15) for v in D.values() for t in v if not t.endswith('?')})
    seeds = []
    for s in range(1, 21):
        rr = random.Random(s)
        def inj(PA, PB, lines):
            PA = {l: list(v) for l, v in PA.items()}; PB = {l: list(v) for l, v in PB.items()}
            for l in lines:
                for X, Y in ((PA, PB), (PB, PA)):
                    for i in range(len(X.get(l, []))):
                        if rr.random() < r / 2:
                            new = rr.choice(inv); X[l][i] = new
                            if rr.random() < 0.25 and i < len(Y.get(l, [])): Y[l][i] = new
            return PA, PB
        L19 = ['L%02d' % i for i in range(10, 27)]
        a19, b19 = inj(A19, B19, L19)
        a15a, b15a = inj(A15[0], B15[0], ['L%02d' % i for i in range(7, 14)])
        a15b, b15b = inj(A15[1], B15[1], ['L%02d' % i for i in range(1, 5)])
        g = run_a(paragraphs(a19, b19, (a15a, a15b), (b15a, b15b)), key)
        seeds.append(dict(seed=s, **{dn: [g[dn]['acc'], g[dn]['S']] for dn in g}, ok=passes_ok(g)))
    nok = sum(x['ok'] for x in seeds)
    res['gate_c'] = dict(rate_per_pass=round(r / 2, 4), mirror=0.25, seeds_ok=nok, seeds=seeds)
    res['gate_c_pass'] = nok >= 16
    res['all_pass'] = bool(res['gate_a_pass'] and res['gate_b_pass'] and res['gate_c_pass'])
    outs = {}
    if res['all_pass']:
        # pooled: cells correct in P19 and P15 counted together
        cnt = {}
        for p in P.values():
            for t, f in zip(p['toks'], correct_flags(p['toks'], key, p['ref'])):
                if f:
                    for c in cells(t): cnt[c] = cnt.get(c, 0) + 1
        conf = {c for c, nn in cnt.items() if nn >= K}
        res['final_cells'] = len(conf)
        nbase = sum(1 for s in key if s.isdigit())
        HK = nbase * math.log2(20); U = HK / 3.2
        res['AD'] = dict(numeric_bases=nbase, HK_bits=round(HK, 1), R=3.2, unicity=round(U, 1), AD_letters=round(1.5 * U, 1))
        reg = {}
        for letter in ('19sep', '15oct'):
            G = dict(H=0, C=0, S=0, M=0, U=0); text = []; best = cur = 0; bestspan = curspan = ''
            for lt, page, loader, lines in TARGET:
                if lt != letter: continue
                A, B, R = T[page]
                for ln in lines:
                    if ln in CLEARCUT.get(page, ()): cur = 0; curspan = ''  # a clear span breaks the stretch
                    if ln not in R: continue
                    ag = agreed_in_R(R, A, B, ln); words = []
                    for t, a in zip(R[ln], ag):
                        txt, kind = dec_tok(t, key)
                        if kind == 'punct': words.append('/'); continue
                        if kind != 'key':
                            G['U'] += 1; words.append('[' + t + ']'); cur = 0; curspan = ''; continue
                        if a and licensed(t, key, conf):
                            G['S'] += 1; words.append(txt.upper()); cur += len(norm(txt)); curspan += txt
                            if cur > best: best, bestspan = cur, f'{page} {ln}: ' + curspan
                        else:
                            G['M'] += 1; words.append(txt.lower()); cur = 0; curspan = ''
                    text.append(f'{page} {ln}\t' + ' '.join(words))
            reg[letter] = dict(grades=G, longest_S_letters=best, longest_S_ends=bestspan[-120:])
            outs[f'reading_slic_{letter}.txt'] = ('# slic.py (ES132-SLIC, PREREG_slic.md): UPPER = S (licensed), lower = M, [x] = code/U\n'
                                                   + '\n'.join(text) + '\n')
        res['regrade'] = reg
    outs['slic_result.json'] = json.dumps(res, indent=1, ensure_ascii=False) + '\n'
    if '--check' in sys.argv:
        stale = [f for f, s in outs.items() if not (HERE / f).exists() or (HERE / f).read_text(encoding='utf-8') != s]
        print('stale:' if stale else 'OK: committed outputs match', *stale); sys.exit(1 if stale else 0)
    for f, s in outs.items(): (HERE / f).write_text(s, encoding='utf-8')
    print(json.dumps({k: v for k, v in res.items() if k not in ('gate_c',)}, ensure_ascii=False, indent=1)[:4000])
    print('gate_c', res['gate_c']['seeds_ok'], '/20')


if __name__ == '__main__':
    main()
