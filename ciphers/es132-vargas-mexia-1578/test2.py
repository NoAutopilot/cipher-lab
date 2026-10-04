#!/usr/bin/env python3
"""test2.py -- es132-vargas-mexia-1578 test 2 (RUN2-ES132, 4 Oct 2026), scored exactly as PREREG_test2.md says.

Pages f.89r, f.89v (f.89 letter, 19 Sept 1578), f.119v upper and f.120r L05-L08 (amendment 1), none printed by Teulet: gate (b);
f.120r L01-L04 continue Teulet's 15 Oct 1578 paragraph: gate (a) as PREREG_test1 (a), function gate_a (amendment 1).
f.90r and f.91r (f.89 letter, amendment 2, N4-ES132B): gate (b).
S_b (es16 4-gram, test1's model) vs 200 token-order shuffles (ARM-C1) and 200 key shuffles, nulls first; gate S_b > p99 of both.
Calibration for pages under 250 key letters: same-length prefix of test 1's f.90v known-answer lines (blind passes).

Blind passes in test 2 write above-marks by SHAPE (run2/pass_prompt_f89r.md). Shape -> test0 notation, fixed before any decode
from test 1's f.90v crops vs its pass A on the Teulet lines (L10: bar over 4 = 'es', hat over 7ρ = 'con', acute over 4 = 'el';
L05: tilde over 17σ = @m, small r-shaped mark over 24. = @r):
  @hat -> @n, @bar -> @s, @acute -> @l, @tilde -> @m, @rmark -> @r, @dots -> @2 (no letter, as test 0/1);
  @cross, @other and any '?'-qualified mark -> dropped (no letter; counted in the report).
Then passnorm.py (unchanged). {CLEAR:...} tokens are dropped. err_2reader = token disagreement between passes A and B after
normalisation, per line difflib alignment, (A-only + B-only + substituted) / max(len A, len B) summed.
Writes test2_result.json and reading_<page>.txt; --check exits 1 if stale.

--page f41r (ES132-C3, 4 Oct 2026, PREREG_c3_test1.md): Cipher 3 pool test 1 on one open letter page. Scores that page's passes A/B and
reconciled text (all lines) with the same score(), and in the same run the positive control (test 1's f.90v unprinted L01-L09, L27,
passes A/B + reconciled); grades S where gate (b) passes on both blind passes and the control's reconciled text, else M.
Writes c3_test1_<page>_result.json and reading_<page>.txt only (test2_result.json untouched); --check as above.
"""
import sys, json, gzip, random, re, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1] / 'tools'))
from passnorm import norm_line
from test0 import load_key, load_lines, dec_tok, shuffled, reading, norm, known_agreement
from test1 import letters, p99, ES16, ref_text, char_align
import judge_plaintext as jp

SHAPE = {'hat': '@n', 'bar': '@s', 'acute': '@l', 'tilde': '@m', 'rmark': '@r', 'dots': '@2'}
PAGES = {
    'f89r': dict(lines=['L%02d' % i for i in range(1, 24)]),
    'f89v': dict(lines=['L%02d' % i for i in range(1, 41)]),
    'f119vU': dict(lines=['L%02d' % i for i in range(1, 30)]),
    'f120r': dict(lines=['L%02d' % i for i in range(5, 30)]),  # amendment 1 (N4-ES132, 4 Oct 2026): L05-L08 unprinted -> (b)
    'f90r': dict(lines=['L%02d' % i for i in range(1, 41)]),  # amendment 2 (N4-ES132B, 4 Oct 2026)
    'f91r': dict(lines=['L%02d' % i for i in range(1, 41)]),  # amendment 2 (N4-ES132B, 4 Oct 2026)
}
# amendment 1 overlap clause: f.120r L01-L04 continue Teulet's printed 15 Oct 1578 paragraph -> gate (a) exactly as PREREG_test1 (a)
A_PAGES = {
    'f120r': dict(known=['L%02d' % i for i in range(1, 5)], ref='teulet_15oct1578.txt'),
}
DROPPED = {'marks': 0, 'clear': 0}


def shape_tok(t):
    if t.startswith('{CLEAR'):
        DROPPED['clear'] += 1; return None
    q = '?' if t.endswith('?') and not re.search(r'@\w+\?$', t) else ''
    core = t.rstrip('?') if q else t
    parts = core.split('@')
    out = parts[0]
    for m in parts[1:]:
        if m.endswith('?') or m.rstrip('?') not in SHAPE:
            DROPPED['marks'] += 1; continue
        out += SHAPE[m]
    return out + q


def load_pass(p):
    L = {}
    for l in open(p, encoding='utf-8'):
        if l.startswith('#') or not l.strip() or '\t' not in l: continue
        a, b = l.rstrip('\n').split('\t', 1)
        toks = [x for x in (shape_tok(t) for t in b.split()) if x]
        L[a.strip()] = norm_line(' '.join(toks)).split()
    return L


def err2(A, B):
    d = n = 0
    for ln in sorted(set(A) | set(B)):
        a = [t.rstrip('?') for t in A.get(ln, [])]; b = [t.rstrip('?') for t in B.get(ln, [])]
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        d += sum(max(i2 - i1, j2 - j1) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal')
        n += max(len(a), len(b))
    return d, n


def score(toks, key, shuf, model, rr):
    order = []
    for _ in range(200):
        s = list(toks); rr.shuffle(s); order.append(model.score(letters(s, key)))
    keyn = [model.score(letters(toks, k)) for k in shuf]
    txt = letters(toks, key); sb = model.score(txt); N = len(jp.fold(txt))
    real, null, _ = model.controls(max(N, 20), samples=200)
    med = sorted(order)[100]
    return dict(letters=N, S_b=round(sb, 3), order_p99=round(p99(order), 3), order_median=round(med, 3),
                key_p99=round(p99(keyn), 3), gate_b=bool(sb > max(p99(order), p99(keyn))),
                judge_null_p99=round(jp.pct(null, 0.99), 3), judge_real_p05=round(jp.pct(real, 0.05), 3),
                judge_pass=bool(sb > jp.pct(null, 0.99) and sb > jp.pct(real, 0.05)),
                armc1_shuffled_median_judge_pass=bool(med > jp.pct(null, 0.99) and med > jp.pct(real, 0.05)))


def gate_a(page, cfg, key, shuf, corpus):
    """PREREG_test1 (a): S_a char-align vs N1 (200 key shuffles) and N2 (wrong-Teulet windows), nulls first; gate on each blind pass."""
    ref = ref_text(cfg['ref'])
    step = max(50, (len(corpus) - len(ref)) // 500)
    wins = [corpus[i:i + len(ref)] for i in range(0, len(corpus) - len(ref), step)]
    out = {'ref_letters': len(ref), 'n2_windows': len(wins)}
    for name, f in (('passA', f'passes/{page}_passA.tsv'), ('passB', f'passes/{page}_passB.tsv'), ('reconciled', f'ciphertext_{page}.tsv')):
        L = load_pass(HERE / f) if name != 'reconciled' else load_lines(HERE / f)
        kt = [t for ln in cfg['known'] if ln in L for t in L[ln]]
        n1 = [char_align(kt, k, ref)[0] for k in shuf]
        n2 = [char_align(kt, key, w)[0] for w in wins]
        sa, nl = char_align(kt, key, ref)
        g, n = known_agreement(kt, key, ref)
        out[name] = dict(S_a=round(sa, 3), letters=nl, n1_p99=round(p99(n1), 3), n1_max=round(max(n1), 3), n2_p99=round(p99(n2), 3),
                         n2_max=round(max(n2), 3), gate_a=bool(sa > max(p99(n1), p99(n2))), token_agree=f'{g}/{n}',
                         token_agree_frac=round(g / max(1, n), 3))
    R = load_lines(HERE / f'ciphertext_{page}.tsv')
    kinds = [dec_tok(t, key)[1] for ln in cfg['known'] if ln in R for t in R[ln]]
    g = int(out['reconciled']['token_agree'].split('/')[0])  # C = key token agreeing with Teulet's printed period decipherment
    out['grades_reconciled_printed_lines'] = dict(H=0, C=g, S=0, M=sum(k == 'key' for k in kinds) - g, I=0,
                                                  U=sum(k in ('code', 'bad') for k in kinds))
    return out


C3_PAGES = {'f41r': ['L%02d' % i for i in range(1, 41)], 'f41v': ['L%02d' % i for i in range(1, 41)]}  # f41v: RUN3-ES41, PREREG_c3_f41v.md
F90V_UNPRINTED = ['L%02d' % i for i in range(1, 10)] + ['L27']


def main_page(page):
    key = load_key()
    rng = random.Random(1578)
    shuf = [shuffled(key, rng) for _ in range(200)]
    model = jp.NgramModel([gzip.open(p, 'rt', encoding='utf-8').read() for p in ES16])
    res = {'page': page, 'prereg': 'PREREG_c3_test1.md'}
    ctl = res['positive_control_f90v_unprinted'] = {}
    t1 = lambda f: {k: norm_line(' '.join(v)).split() for k, v in load_lines(HERE / f).items()}  # test 1's loader (its notation)
    for name, L in (('passA', t1('passes/f90v_passA.tsv')), ('passB', t1('passes/f90v_passB.tsv')),
                    ('reconciled', load_lines(HERE / 'ciphertext_f90v.tsv'))):
        ctl[name] = score([t for ln in F90V_UNPRINTED if ln in L for t in L[ln]], key, shuf, model, random.Random(1578))
    lines = C3_PAGES[page]
    A, B = load_pass(HERE / f'passes/{page}_passA.tsv'), load_pass(HERE / f'passes/{page}_passB.tsv')
    pr_ = HERE / f'ciphertext_{page}.tsv'
    R = load_lines(pr_) if pr_.exists() else {}
    d, n = err2(A, B); r = res['target'] = {'err_2reader': f'{d}/{n}', 'err_2reader_frac': round(d / max(1, n), 3)}
    for name, L in (('passA', A), ('passB', B), ('reconciled', R)):
        if L: r[name] = score([t for ln in lines if ln in L for t in L[ln]], key, shuf, model, random.Random(1578))
    outs = {}
    if R:
        ok = all(r[x]['gate_b'] for x in ('passA', 'passB')) and ctl['reconciled']['gate_b']
        toks = [t for ln in lines if ln in R for t in R[ln]]
        kinds = [dec_tok(t, key)[1] for t in toks]
        key_q = sum(k == 'key' and t.endswith('?') for t, k in zip(toks, kinds))
        nkey = sum(k == 'key' for k in kinds)
        res['grades_reconciled'] = dict(H=0, C=0, S=(nkey - key_q) if ok else 0, M=key_q if ok else nkey, I=0,
                                        U=sum(k in ('code', 'bad') for k in kinds))
        outs[f'reading_{page}.txt'] = reading(R, key, sorted(set(R) & set(lines)))
    res['dropped_shape_tokens'] = dict(DROPPED)
    outs[f'c3_test1_{page}_result.json'] = json.dumps(res, indent=1) + '\n'
    if '--check' in sys.argv:
        stale = [f for f, s in outs.items() if not (HERE / f).exists() or (HERE / f).read_text(encoding='utf-8') != s]
        print('stale:' if stale else 'OK: committed outputs match', *stale); sys.exit(1 if stale else 0)
    for f, s in outs.items(): (HERE / f).write_text(s, encoding='utf-8')
    print(outs[f'c3_test1_{page}_result.json'])


def main():
    if '--page' in sys.argv:
        return main_page(sys.argv[sys.argv.index('--page') + 1])
    key = load_key()
    rng = random.Random(1578)
    shuf = [shuffled(key, rng) for _ in range(200)]
    model = jp.NgramModel([gzip.open(p, 'rt', encoding='utf-8').read() for p in ES16])
    res, outs = {}, {}
    for page, cfg in PAGES.items():
        pa, pb, pr_ = (HERE / f'passes/{page}_passA.tsv', HERE / f'passes/{page}_passB.tsv', HERE / f'ciphertext_{page}.tsv')
        if not pa.exists(): continue
        A, B = load_pass(pa), (load_pass(pb) if pb.exists() else {})
        R = load_lines(pr_) if pr_.exists() else {}
        r = res[page] = {}
        if B:
            d, n = err2(A, B); r['err_2reader'] = f'{d}/{n}'; r['err_2reader_frac'] = round(d / max(1, n), 3)
        for name, L in (('passA', A), ('passB', B), ('reconciled', R)):
            if not L: continue
            toks = [t for ln in cfg['lines'] if ln in L for t in L[ln]]
            r[name] = score(toks, key, shuf, model, random.Random(1578))
            if r[name]['letters'] < 250:  # calibration on a same-length prefix of f.90v known-answer lines (test 1)
                F = {k: norm_line(' '.join(v)).split() for k, v in load_lines(HERE / f'passes/f90v_pass{name[-1]}.tsv').items()} \
                    if name != 'reconciled' else load_lines(HERE / 'ciphertext_f90v.tsv')
                kt, out = [t for ln in ['L%02d' % i for i in range(10, 27)] if ln in F for t in F[ln]], []
                for t in kt:
                    out.append(t)
                    if len(jp.fold(letters(out, key))) >= r[name]['letters']: break
                r[name]['calib_f90v_prefix'] = score(out, key, shuf, model, random.Random(1578))
        if R:
            kinds = [dec_tok(t, key)[1] for ln in cfg['lines'] if ln in R for t in R[ln]]
            r['grades_reconciled'] = dict(H=0, C=0, S=0, M=sum(k == 'key' for k in kinds), I=0,
                                          U=sum(k in ('code', 'bad') for k in kinds))
            outs[f'reading_{page}.txt'] = reading(R, key, sorted(set(R) & set(cfg['lines'])))
    corpus = norm(''.join(gzip.open(p, 'rt', encoding='utf-8').read() for p in ES16))
    for page, cfg in A_PAGES.items():
        if (HERE / f'passes/{page}_passA.tsv').exists():
            res.setdefault(page, {})['printed_lines_gate_a'] = gate_a(page, cfg, key, shuf, corpus)
            outs[f'reading_{page}.txt'] = reading(load_lines(HERE / f'ciphertext_{page}.tsv'), key,
                                                  sorted(set(load_lines(HERE / f'ciphertext_{page}.tsv'))))
    res['dropped_shape_tokens'] = dict(DROPPED)
    outs['test2_result.json'] = json.dumps(res, indent=1) + '\n'
    if '--check' in sys.argv:
        stale = [f for f, s in outs.items() if not (HERE / f).exists() or (HERE / f).read_text(encoding='utf-8') != s]
        print('stale:' if stale else 'OK: committed outputs match', *stale); sys.exit(1 if stale else 0)
    for f, s in outs.items(): (HERE / f).write_text(s, encoding='utf-8')
    print(outs['test2_result.json'])


if __name__ == '__main__':
    main()
