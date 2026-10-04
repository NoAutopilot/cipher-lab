#!/usr/bin/env python3
"""test2.py -- es132-vargas-mexia-1578 test 2 (RUN2-ES132, 4 Oct 2026), scored exactly as PREREG_test2.md says.

Pages f.89r, f.89v (f.89 letter, 19 Sept 1578) and f.119v upper, none printed by Teulet, so only gate (b) runs:
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
"""
import sys, json, gzip, random, re, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[1] / 'tools'))
from passnorm import norm_line
from test0 import load_key, load_lines, dec_tok, shuffled, reading
from test1 import letters, p99, ES16
import judge_plaintext as jp

SHAPE = {'hat': '@n', 'bar': '@s', 'acute': '@l', 'tilde': '@m', 'rmark': '@r', 'dots': '@2'}
PAGES = {
    'f89r': dict(lines=['L%02d' % i for i in range(1, 24)]),
    'f89v': dict(lines=['L%02d' % i for i in range(1, 41)]),
    'f119vU': dict(lines=['L%02d' % i for i in range(1, 30)]),
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


def main():
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
    res['dropped_shape_tokens'] = dict(DROPPED)
    outs['test2_result.json'] = json.dumps(res, indent=1) + '\n'
    if '--check' in sys.argv:
        stale = [f for f, s in outs.items() if not (HERE / f).exists() or (HERE / f).read_text(encoding='utf-8') != s]
        print('stale:' if stale else 'OK: committed outputs match', *stale); sys.exit(1 if stale else 0)
    for f, s in outs.items(): (HERE / f).write_text(s, encoding='utf-8')
    print(outs['test2_result.json'])


if __name__ == '__main__':
    main()
