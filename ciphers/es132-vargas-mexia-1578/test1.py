#!/usr/bin/env python3
"""test1.py -- es132-vargas-mexia-1578 test 1 (RUN1-ES132, 4 Oct 2026), scored exactly as PREREG_test1.md says.

Reuses test0.py's Cp.30 decoder (key.tsv). Page f.90v (f.89 letter, 19 Sept 1578):
 (a) known answer = the lines carrying Teulet vol.5 pp.161-162 (teulet_19sep1578.txt): character-level alignment S_a
     (share of key-decoded letters inside difflib matching blocks, both sides normalised by test0.norm) vs
     N1 = 200 key shuffles (seed 1578) and N2 = the true-key decode against same-length windows of other Teulet Spanish
     (es16 corpus, which excludes both known-answer letters), step 50. Gate: S_a > max(p99 N1, p99 N2) on each blind pass.
 (b) unprinted lines: S_b = mean log10 4-gram score (tools/judge_plaintext.NgramModel on es16) of the key-decoded letters
     vs 200 token-order shuffles (ARM-C1) and 200 key shuffles. Gate: S_b > p99 of both. The known-answer lines are
     scored the same way as the calibration. The standard judge line (null_p99, real_p05) is reported, not gated.
Writes test1_result.json and reading_f90v.txt from ciphertext_f90v.tsv; --check exits 1 if stale.
"""
import sys, json, gzip, random, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(ROOT / 'tools'))
from passnorm import norm_line
from test0 import load_key, load_lines, dec_tok, norm, shuffled, known_agreement, reading
import judge_plaintext as jp

PAGES = {
    'f90v': dict(ref='teulet_19sep1578.txt', known=['L%02d' % i for i in range(10, 27)],
                 target=['L%02d' % i for i in range(1, 10)] + ['L27'],
                 files=[('reconciled', 'ciphertext_f90v.tsv'), ('passA', 'passes/f90v_passA.tsv'),
                        ('passB', 'passes/f90v_passB.tsv')]),
    'f119r': dict(ref=None, known=[], target=['L%02d' % i for i in range(1, 21)],
                  files=[('reconciled', 'ciphertext_f119r.tsv'), ('passA', 'passes/f119r_passA.tsv'),
                         ('passB', 'passes/f119r_passB.tsv')]),
    # supplementary (not in PREREG): test 0's page re-scored with the test 1 statistics, as a second calibration
    'f119v': dict(ref='teulet_15oct1578.txt', known=['L%02d' % i for i in range(7, 14)],
                  target=['L%02d' % i for i in range(2, 7)],
                  files=[('reconciled', 'ciphertext.tsv'), ('passA', 'passes/passA.tsv'), ('passB', 'passes/passB.tsv')]),
}
ES16 = sorted((HERE / 'es16').glob('teulet5_es_fold*.txt.gz'))


def ref_text(name):
    return norm(''.join(l for l in open(HERE / name, encoding='utf-8') if not l.startswith('#')))


def char_align(toks, key, ref):
    dec = ''.join(norm(t) for t, k in (dec_tok(x, key) for x in toks) if k == 'key')
    if not dec: return 0.0, 0
    sm = difflib.SequenceMatcher(None, dec, ref, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks()) / len(dec), len(dec)


def letters(toks, key):
    return ' '.join(t for t, k in (dec_tok(x, key) for x in toks) if k == 'key')


def p99(xs):
    xs = sorted(xs); return xs[min(len(xs) - 1, int(0.99 * (len(xs) - 1)))]


def main():
    key = load_key()
    rng = random.Random(1578)
    shuf = [shuffled(key, rng) for _ in range(200)]
    corpus = norm(''.join(gzip.open(p, 'rt', encoding='utf-8').read() for p in ES16))
    model = jp.NgramModel([gzip.open(p, 'rt', encoding='utf-8').read() for p in ES16])
    res, outs = {}, {}
    for page, cfg in PAGES.items():
        ref = ref_text(cfg['ref']) if cfg['ref'] else ''
        step = max(50, (len(corpus) - len(ref)) // 500)  # >= 50 letters apart, about 500 windows
        wins = [] if not ref else [corpus[i:i + len(ref)] for i in range(0, len(corpus) - len(ref), step)]
        pr = res[page] = {'ref_letters': len(ref), 'n2_windows': len(wins)}
        for name, f in cfg['files']:
            p = HERE / f
            if not p.exists(): continue
            L = load_lines(p)
            if f.startswith('passes/'):  # blind passes: mechanical notation normaliser (passnorm.py), same for A and B
                L = {k: norm_line(' '.join(v)).split() for k, v in L.items()}
            kt = [t for ln in cfg['known'] if ln in L for t in L[ln]]
            tt = [t for ln in cfg['target'] if ln in L for t in L[ln]]
            if not ref:  # unprinted page: (b) only
                kt = []
            # (a) nulls first, then target
            n1 = [char_align(kt, k, ref)[0] for k in shuf]
            n2 = [char_align(kt, key, w)[0] for w in wins]
            sa, nl = char_align(kt, key, ref)
            g, n = known_agreement(kt, key, ref)
            gate_a = bool(ref) and sa > max(p99(n1), p99(n2))
            # (b) nulls first: ARM-C1 token-order shuffles and key shuffles, for target and known-answer calibration
            rr = random.Random(1578)
            b = {}
            for part, toks in (('target', tt), ('known_calib', kt)):
                if not toks: continue
                order = []
                for _ in range(200):
                    s = list(toks); rr.shuffle(s); order.append(model.score(letters(s, key)))
                keyn = [model.score(letters(toks, k)) for k in shuf]
                txt = letters(toks, key); sb = model.score(txt); N = len(jp.fold(txt))
                real, null, _ = model.controls(max(N, 20), samples=200)
                med_order = sorted(order)[100]
                b[part] = dict(letters=N, S_b=round(sb, 3), order_p99=round(p99(order), 3), order_median=round(med_order, 3),
                               key_p99=round(p99(keyn), 3), gate_b=sb > max(p99(order), p99(keyn)),
                               judge_null_p99=round(jp.pct(null, 0.99), 3), judge_real_p05=round(jp.pct(real, 0.05), 3),
                               judge_pass=bool(sb > jp.pct(null, 0.99) and sb > jp.pct(real, 0.05)),
                               armc1_shuffled_median_judge_pass=bool(med_order > jp.pct(null, 0.99) and med_order > jp.pct(real, 0.05)))
            pr[name] = dict(a=None if not ref else dict(S_a=round(sa, 3), letters=nl, n1_p99=round(p99(n1), 3), n1_max=round(max(n1), 3),
                                   n2_p99=round(p99(n2), 3), n2_max=round(max(n2), 3), gate_a=gate_a,
                                   token_agree=f'{g}/{n}', token_agree_frac=round(g / max(1, n), 3)), b=b)
        if not (HERE / cfg['files'][0][1]).exists(): continue
        Lr = load_lines(HERE / cfg['files'][0][1])
        # rule 4 grades on the reconciled text: C = key token agreeing with the printed period decipherment,
        # M = other key-decoded token, U = nomenclature code / cursive word / unreadable (no value on disk)
        kinds = lambda lines: [dec_tok(t, key)[1] for ln in lines if ln in Lr for t in Lr[ln]]
        kk, tk = kinds(cfg['known']), kinds(cfg['target'])
        cC = known_agreement([t for ln in cfg['known'] if ln in Lr for t in Lr[ln]], key, ref)[0] if ref else 0
        nk = sum(k == 'key' for k in kk) + sum(k == 'key' for k in tk)
        res[page]['grades_reconciled'] = dict(H=0, C=cC, S=0, M=nk - cC, I=0,
                                              U=sum(k in ('code', 'bad') for k in kk + tk))
        outs[f'reading_{page}.txt'] = reading(Lr, key, sorted(set(Lr) & set(cfg['known'] + cfg['target'])))
    outs['test1_result.json'] = json.dumps(res, indent=1) + '\n'
    if '--check' in sys.argv:
        stale = [f for f, s in outs.items() if not (HERE / f).exists() or (HERE / f).read_text(encoding='utf-8') != s]
        print('stale:' if stale else 'OK: committed outputs match', *stale); sys.exit(1 if stale else 0)
    for f, s in outs.items(): (HERE / f).write_text(s, encoding='utf-8')
    print(outs['test1_result.json'])


if __name__ == '__main__':
    main()
