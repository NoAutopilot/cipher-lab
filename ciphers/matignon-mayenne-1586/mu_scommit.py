#!/usr/bin/env python3
"""GAPS3-matignon-mayenne-1586 (3 Oct 2026, account-4): the per-leaf beam's M choices committed as S candidates in a
scratch reading on f143r/f143v/f154/f173 and re-judged per leaf against judge_leaves.py's within-line shuffle control,
behind mu_scommit_prereg.md (pushed before this ran). Adds the pre-registered rule-3 shuffled-target clause (P1).

Nothing is written to key.tsv/exceptions.tsv by this script. Run from the repository root:
  python3 ciphers/matignon-mayenne-1586/mu_scommit.py [--check]
Writes ciphers/matignon-mayenne-1586/mu_scommit.json; --check exits 1 if it is stale.
"""
import sys, json, random
from pathlib import Path
from multiprocessing import Pool
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(ROOT / 'tools'))
import mu_beam as mb  # noqa: E402
import mu_leaf_beam as lb  # noqa: E402

LEAVES = ['f143r', 'f143v', 'f154', 'f173']
NSHUF = 20


def letter_shuffles(lines, mch, n=NSHUF):
    """judge_leaves.py's control: each line's letters shuffled, rng = Random(1), n draws."""
    J = lb.judge()
    per_line = [lb.render([L], [ch]) for L, ch in zip(lines, mch)]
    rng = random.Random(1)
    out = []
    for _ in range(n):
        parts = []
        for s in per_line:
            ls = list(s); rng.shuffle(ls); parts.append(''.join(ls))
        out.append(J.score(''.join(parts)))
    return out


def run_leaf(leaf):
    lm = mb.get_lm()
    J = lb.judge()
    target = lb.leaf_lines()[leaf]
    first = [{} for _ in target]
    mch = lb.beam(lm, target)
    s_first, s_beam = J.score(lb.render(target, first)), J.score(lb.render(target, mch))
    shuf = letter_shuffles(target, mch)
    rises = []
    for s in range(1, NSHUF + 1):
        rnd = random.Random(s)
        sh = [rnd.sample(L, len(L)) for L in target]
        rises.append(J.score(lb.render(sh, lb.beam(lm, sh))) - J.score(lb.render(sh, [{} for _ in sh])))
    rise = s_beam - s_first
    g1, g2, p1 = rise > 0, s_beam > max(shuf), rise > max(rises)
    return dict(leaf=leaf, m_changed=sum(1 for L, ch in zip(target, mch) for p, t in enumerate(L)
                                         if t[0] == 'M' and ch.get(p, 0) != 0),
                score_first=round(s_first, 4), score_scratch=round(s_beam, 4), rise=round(rise, 4),
                letter_shuffle_max=round(max(shuf), 4), letter_shuffle_mean=round(sum(shuf) / NSHUF, 4),
                shuffled_target_rise_max=round(max(rises), 4), shuffled_target_rise_mean=round(sum(rises) / NSHUF, 4),
                G1_rises=g1, G2_above_shuffle_max=g2, P1_rise_above_shuffled_target=p1)


def main():
    with Pool(4) as p:
        rows = p.map(run_leaf, LEAVES)
    if not all(r['G1_rises'] and r['G2_above_shuffle_max'] for r in rows):
        verdict = 'FAIL (G1 or G2 fails on at least one leaf): nothing committed'
    elif not all(r['P1_rise_above_shuffled_target'] for r in rows):
        verdict = 'NON-TEST (G1, G2 pass 4/4 but the rise does not beat the shuffled-target rise on every leaf): nothing committed'
    else:
        verdict = 'COMMIT'
    kc = json.loads((HERE / 'mu_leaf_beam.json').read_text())
    power = {r['leaf']: sum(c['gain']['passed'] for c in r['control']) for r in kc['leaves'] if r['leaf'] in LEAVES}
    out = dict(job='GAPS3-matignon-mayenne-1586', prereg='mu_scommit_prereg.md', leaves=rows,
               known_answer_gain_power_of_3=power, verdict=verdict)
    js = json.dumps(out, indent=1, sort_keys=True)
    f = HERE / 'mu_scommit.json'
    if '--check' in sys.argv:
        stale = not f.exists() or f.read_text() != js
        print('STALE' if stale else 'mu_scommit.json current'); sys.exit(1 if stale else 0)
    f.write_text(js)
    for r in rows:
        print(r)
    print('known-answer power', power)
    print(verdict)


if __name__ == '__main__':
    main()
