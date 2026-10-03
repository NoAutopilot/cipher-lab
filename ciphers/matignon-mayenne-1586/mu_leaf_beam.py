#!/usr/bin/env python3
"""GAPS-matignon-mayenne-1586 gap 1 (3 Oct 2026, account-4): the bMATBEAM beam, M-only, per leaf, on the seven
read-leaves, behind the gates pre-registered in mu_leaf_beam_prereg.md (pushed before this ran).

Reuses mu_beam.py unchanged (LM, emit, viterbi_line, build_control). U held fixed as TOK; M chosen by exact per-line
Viterbi. Control (A) per leaf first; target scored only on leaves whose control passes. Judge = the spec's fr16 model.
Run from the repository root: python3 ciphers/matignon-mayenne-1586/mu_leaf_beam.py [--check]
Writes ciphers/matignon-mayenne-1586/mu_leaf_beam.json; --check exits 1 if it is stale.
"""
import sys, json, random, collections
from pathlib import Path
from multiprocessing import Pool
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(ROOT / 'tools'))
import mu_beam as mb  # noqa: E402
from judge_plaintext import NgramModel, read_corpus, fold  # noqa: E402

LEAVES = ['f143r', 'f143v', 'f150', 'f154', 'f173', 'f196', 'f201']
SEEDS = (1, 2, 3)
NSHUF = 20
_J = None


def judge():
    global _J
    if _J is None:
        spec = json.loads((ROOT / 'specs/matignon-mayenne-1586.json').read_text())
        _J = NgramModel([read_corpus(ROOT / p) for p in spec['judge']['corpora']])
    return _J


def leaf_lines():
    """target lines per leaf, in mu_beam's token form, from reading_tokens.tsv (same order as load_target)."""
    import csv
    per = collections.OrderedDict()
    for r in csv.DictReader(open(HERE / 'reading_tokens.tsv'), delimiter='\t'):
        v, g = r['value'], r['grade']
        if g == 'U':
            tok = ('U', r['sign'], None)
        elif g == 'M':
            tok = ('M', r['sign'], [mb.fold_text(x) for x in v.split('|')])
        else:
            tok = ('H', r['sign'], [mb.NULL if v == '*' else mb.fold_text(v)])
        per.setdefault(r['line'].split('-')[0], collections.OrderedDict()).setdefault(r['line'], []).append(tok)
    return {k: list(v.values()) for k, v in per.items()}


def render(lines, mch):
    """letters as judge_leaves.py renders them: H value, chosen M alternative, U and '*' dropped."""
    out = []
    for L, ch in zip(lines, mch):
        for pos, (k, s, c) in enumerate(L):
            if k == 'U':
                continue
            out.append(c[ch.get(pos, 0)] if k == 'M' else c[0])
    return fold(''.join(out))


def beam(lm, lines):
    u = {t[1]: mb.TOK for L in lines for t in L if t[0] == 'U'}
    return [mb.viterbi_line(lm, L, u, lm.bpc)[1] for L in lines]


def gain(lm, lines):
    J = judge()
    mch = beam(lm, lines)
    first = [{} for _ in lines]
    return J.score(render(lines, mch)) - J.score(render(lines, first)), mch


def gain_test(lm, lines):
    g, mch = gain(lm, lines)
    nulls = []
    for s in range(1, NSHUF + 1):
        rnd = random.Random(s)
        nulls.append(gain(lm, [rnd.sample(L, len(L)) for L in lines])[0])
    return dict(gain=round(g, 4), null_max=round(max(nulls), 4), null_mean=round(sum(nulls) / len(nulls), 4),
                passed=bool(g > max(nulls) and g >= 0.010)), mch


def run_leaf(leaf):
    lm = mb.get_lm()
    target = leaf_lines()[leaf]
    held = mb.words_of(f'{mb.D}/lettresdecatheri02cathuoft_djvu.txt.gz')
    uni = collections.Counter(''.join(held))
    ctl = []
    for seed in SEEDS:
        lines, tl, utrue = mb.build_control(target, mb.load_key(), held, seed)
        gt, mch = gain_test(lm, lines)
        mok = mn = base = first = 0
        maj = collections.defaultdict(collections.Counter)
        for L, T_, ch in zip(lines, tl, mch):
            for pos, (k, s, c) in enumerate(L):
                if k == 'M':
                    mn += 1; mok += ch.get(pos, 0) == T_[pos]; first += T_[pos] == 0
                    base += max(range(len(c)), key=lambda j: uni.get(c[j][0], 0)) == T_[pos]
                    maj[s][T_[pos]] += 1
        ctl.append(dict(seed=seed, m_n=mn, m_acc=round(mok / mn, 4), m_freq_base=round(base / mn, 4),
                        m_first_base=round(first / mn, 4),
                        m_oracle_majority=round(sum(v.most_common(1)[0][1] for v in maj.values()) / mn, 4), gain=gt))
    mean = lambda k: sum(c[k] for c in ctl) / len(ctl)
    a = mean('m_acc') >= mean('m_freq_base') + 0.10
    b = max(mean('m_freq_base'), mean('m_first_base')) < 0.95
    c = sum(x['gain']['passed'] for x in ctl) >= 2
    res = dict(leaf=leaf, n_tokens=sum(len(L) for L in target), control=ctl,
               ctl_m_acc=round(mean('m_acc'), 4), ctl_freq_base=round(mean('m_freq_base'), 4),
               ctl_first_base=round(mean('m_first_base'), 4), gate_a=a, gate_b=b, gate_c=c, testable=a and b and c)
    if res['testable']:
        gt, mch = gain_test(lm, target)
        J = judge()
        res['target'] = dict(gt, first_score=round(J.score(render(target, [{} for _ in target])), 4),
                             beam_score=round(J.score(render(target, mch)), 4),
                             m_changed=sum(1 for L, ch in zip(target, mch) for p, t in enumerate(L)
                                           if t[0] == 'M' and ch.get(p, 0) != 0))
    return res


def main():
    with Pool(4) as p:
        rows = p.map(run_leaf, LEAVES)
    testable = [r for r in rows if r['testable']]
    passed = [r for r in testable if r['target']['passed']]
    if len(testable) < 4:
        verdict = 'NON-TEST AT THIS N (fewer than 4 of 7 leaves testable)'
    elif len(passed) >= 4 and 2 * len(passed) >= len(testable):
        verdict = 'PASS'
    else:
        verdict = 'FAIL -- beam retired for this target (rule 3 third-attempt clause)'
    out = dict(job='GAPS-matignon-mayenne-1586 gap 1', prereg='mu_leaf_beam_prereg.md', leaves=rows,
               testable=len(testable), passed=len(passed), verdict=verdict)
    js = json.dumps(out, indent=1, sort_keys=True)
    f = HERE / 'mu_leaf_beam.json'
    if '--check' in sys.argv:
        stale = not f.exists() or f.read_text() != js
        print('STALE' if stale else 'mu_leaf_beam.json current'); sys.exit(1 if stale else 0)
    f.write_text(js)
    for r in rows:
        t = r.get('target', {})
        print(r['leaf'], 'ctl M', r['ctl_m_acc'], 'freq', r['ctl_freq_base'], 'first', r['ctl_first_base'],
              'ctl gains', [x['gain']['gain'] for x in r['control']], 'nullmax', [x['gain']['null_max'] for x in r['control']],
              'abc', r['gate_a'], r['gate_b'], r['gate_c'], '| T', t)
    print(verdict, f'testable {len(testable)}/7 passed {len(passed)}')


if __name__ == '__main__':
    main()
