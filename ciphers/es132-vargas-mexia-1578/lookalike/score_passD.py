#!/usr/bin/env python3
"""ES132-LOOK (9 Oct 2026): re-score a page with test2.py's own statistic, nulls, seed, gate (b) and f.90v positive control
(PREREG_c3_f51v_recut.md / PREREG_c3_f52r.md, unchanged), adding lookalike/<page>/passD.tsv (tools/lookalike_pass.py reconcile output)
as a fourth reading beside pass A, pass B and the committed reconciled file. No gate, statistic or committed file is changed; passD is
not a blind pass, so the PREREG's primary verdict (both blind passes + control) is reported unchanged beside it.
A passD token carries '?' when its conf is not H (the committed file's 'not settled' flag), for the grade count only.
  python3 lookalike/score_passD.py f51v [--check]   -> lookalike/f51v/c3_test1_f51v_passD_result.json, lookalike/f51v/reading_f51v_passD.txt
"""
import sys, csv, json, gzip, random
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent.parent / 'tools')]
import test2
from test2 import load_pass, strip_clear, err2, score, C3_PAGES, F90V_UNPRINTED, ES16
from test0 import load_key, load_lines, dec_tok, shuffled, reading
from passnorm import norm_line
import judge_plaintext as jp

def load_passD(p):
    L = {}
    for r in csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'):
        L.setdefault(r['passage'], []).append(r['sign_id'] + ('' if r['conf'] == 'H' else '?'))
    return L

def run(page):
    key = load_key(); rng = random.Random(1578)
    shuf = [shuffled(key, rng) for _ in range(200)]
    model = jp.NgramModel([gzip.open(p, 'rt', encoding='utf-8').read() for p in ES16])
    res = {'page': page, 'prereg': f'PREREG_c3_{page}{"_recut" if page == "f51v" else ""}.md (unchanged)', 'job': 'ES132-LOOK'}
    ctl = res['positive_control_f90v_unprinted'] = {}
    t1 = lambda f: {k: norm_line(' '.join(v)).split() for k, v in load_lines(HERE / f).items()}
    for name, L in (('passA', t1('passes/f90v_passA.tsv')), ('passB', t1('passes/f90v_passB.tsv')),
                    ('reconciled', load_lines(HERE / 'ciphertext_f90v.tsv'))):
        ctl[name] = score([t for ln in F90V_UNPRINTED if ln in L for t in L[ln]], key, shuf, model, random.Random(1578))
    lines = C3_PAGES[page]; cA, cB = {}, {}
    A, B = load_pass(HERE / f'passes/{page}_passA.tsv', cA), load_pass(HERE / f'passes/{page}_passB.tsv', cB)
    R0 = load_lines(HERE / f'ciphertext_{page}.tsv'); R = strip_clear(R0, page, cA, cB)
    D0 = load_passD(HERE / f'lookalike/{page}/passD.tsv'); D = strip_clear(D0, page, cA, cB)
    d, n = err2(A, B); r = res['target'] = {'err_2reader': f'{d}/{n}', 'err_2reader_frac': round(d / max(1, n), 3)}
    for name, L in (('passA', A), ('passB', B), ('reconciled', R), ('passD', D)):
        r[name] = score([t for ln in lines if ln in L for t in L[ln]], key, shuf, model, random.Random(1578))
    for name, L in (('reconciled', R), ('passD', D)):
        toks = [t for ln in lines if ln in L for t in L[ln]]; kinds = [dec_tok(t, key)[1] for t in toks]
        ok = r['passA']['gate_b'] and r['passB']['gate_b'] and ctl['reconciled']['gate_b']
        kq = sum(k == 'key' and t.endswith('?') for t, k in zip(toks, kinds)); nk = sum(k == 'key' for k in kinds)
        res[f'grades_{name}'] = dict(H=0, C=0, S=(nk - kq) if ok else 0, M=kq if ok else nk, I=0, U=sum(k in ('code', 'bad') for k in kinds))
    changed = sum(a != b for ln in lines for a, b in zip(R0.get(ln, []), D0.get(ln, [])))
    res['passD_vs_reconciled_tokens_differing'] = changed
    outs = {f'lookalike/{page}/c3_test1_{page}_passD_result.json': json.dumps(res, indent=1) + '\n',
            f'lookalike/{page}/reading_{page}_passD.txt': reading(D0, key, sorted(set(D0) & set(lines)))}
    if '--check' in sys.argv:
        stale = [f for f, s in outs.items() if not (HERE / f).exists() or (HERE / f).read_text(encoding='utf-8') != s]
        print('stale:' if stale else 'OK: committed outputs match', *stale); sys.exit(1 if stale else 0)
    for f, s in outs.items(): (HERE / f).write_text(s, encoding='utf-8')
    print(outs[f'lookalike/{page}/c3_test1_{page}_passD_result.json'])

if __name__ == '__main__':
    run(sys.argv[1])
