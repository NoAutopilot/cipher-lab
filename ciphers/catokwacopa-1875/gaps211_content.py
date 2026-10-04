"""GAPS211 (4 Oct 2026, STALE4 for account 4): T' (gaps205_content.py, unchanged) with controls at the design's
3-12-letter omission budget, pre-registered in PREREG-GAPS211.md.

Only the control generator changes: pairs.synth with the omission count o drawn from 3..12 (primary) or from a fixed
band (secondary, descriptive). Statistic, model, E table, target null and seed are gaps205_content's own.

Usage: python3 gaps211_content.py [--check]    (writes / checks content_test_gaps211.json)
"""
import csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pairs  # noqa: E402
import gaps205_content as g  # noqa: E402


def synth(total_lens, letters, rng, dealer, lo, hi):
    """pairs.synth with o in lo..hi instead of 0..3."""
    A, B = [], []
    for n in total_lens:
        o = rng.randint(lo, hi); start = rng.randrange(len(letters) - n - o)
        p = list(letters[start:start + n + o])
        for _ in range(o): p.pop(rng.randrange(len(p)))
        if dealer == 'coin':
            side = [rng.random() < 0.5 for _ in p]
        else:
            k = n // 2 + (rng.random() < 0.5 and n % 2); idx = set(rng.sample(range(n), k))
            side = [i in idx for i in range(n)]
        A.append(''.join(c for c, s in zip(p, side) if s)); B.append(''.join(c for c, s in zip(p, side) if not s))
    return A, B


def arms(tl, letters, uni, big, E, lo, hi, texts, seed0):
    out = {}
    for ai, arm in enumerate(('P-coin', 'P-half', 'U-half')):
        ps = []
        for c in range(texts):
            cr = random.Random(seed0 + 1000 * ai + c)
            if arm == 'U-half':
                cA, _ = synth(tl, letters, cr, 'half', lo, hi); _, cB = synth(tl, letters, cr, 'half', lo, hi)
            else:
                cA, cB = synth(tl, letters, cr, arm[2:], lo, hi)
            ps.append(g.ptest(cA, cB, uni, big, 2000, cr, E)[1])
        ps.sort()
        out[arm] = {'texts': texts, 'perms_each': 2000, 'p_median': round(ps[texts // 2], 5),
                    'share_p_lt_0.001': sum(x < 0.001 for x in ps) / texts,
                    'share_p_lt_0.05': sum(x < 0.05 for x in ps) / texts}
    return out


def run():
    rows = [r for r in csv.DictReader(open(os.path.join(HERE, 'pairs.tsv')), delimiter='\t') if r['letter_line'] == 'y']
    A = [r['ad_8may'] for r in rows]; B = [r['ad_20may'] for r in rows]
    letters = pairs.corpus_letters(); uni, big = g.model(letters)
    E = g.Expect(letters, uni, big)
    t, p = g.ptest(A, B, uni, big, 20000, random.Random(205), E)
    tl = [len(a) + len(b) for a, b in zip(A, B)]
    prim = arms(tl, letters, uni, big, E, 3, 12, 20, 211000)
    power = max(prim['P-coin']['share_p_lt_0.001'], prim['P-half']['share_p_lt_0.001'])
    fpr = prim['U-half']['share_p_lt_0.05']
    valid = power >= 0.5 and fpr <= 0.15
    verdict = ('untestable at 3-12 omissions' if not valid else 'supported' if p < 0.001
               else 'not detected' if p >= 0.05 else 'inconclusive')
    bands = {'%d-%d' % (lo, hi): arms(tl, letters, uni, big, E, lo, hi, 10, 212000 + 10000 * k)
             for k, (lo, hi) in enumerate(((3, 5), (6, 8), (9, 12)))}
    return {'statistic': "T'", 'n_letter_lines': len(A), 'T_obs': round(t, 3), 'perms': 20000, 'seed': 205,
            'p': round(p, 6), 'omission': '3-12', 'controls': prim, 'power': power, 'fpr_U_half': fpr,
            'valid': valid, 'verdict': verdict, 'bands_descriptive': bands}


if __name__ == '__main__':
    out = json.dumps(run(), indent=1) + '\n'; path = os.path.join(HERE, 'content_test_gaps211.json')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path).read() == out
        print('ok: content_test_gaps211.json current' if ok else 'stale: content_test_gaps211.json'); sys.exit(0 if ok else 1)
    open(path, 'w').write(out); print(out)
