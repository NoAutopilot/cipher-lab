#!/usr/bin/env python3
"""Offline tests for tools/bnf_findingaid.py --pile (MQS-BNFPILE, 9 Oct 2026); no network.

These are regression tests on the DEVELOPMENT set (the prototype's rules and est_signs were built on fr.2988 and these
saved notices), not evidence of power.  Catches: a bare-item pile (fr.2988, a planted 10-item pile), key sheets counted
apart (fr.3618), volume-level prior work, the neighbour trap, image-triage.  Must NOT: rank a volume whose items are
deciphered (fr.4715) or a key-sheet volume (fr.3618), call a notice with no item list a negative, change the per-item
TSV of --html (byte-identical to the pre-change tool, golden files in tools/tests/data/).

Run: python3 tools/tests/test_bnf_findingaid_pile.py            (tests)
     python3 tools/tests/test_bnf_findingaid_pile.py --controls  (prints the PREREG-MQS-BNFPILE control numbers)
"""
import glob, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import bnf_findingaid as bf  # noqa: E402

D7 = os.path.join(ROOT, 'sources/bnf-findingaids/2026-10-07')
D9 = os.path.join(ROOT, 'sources/bnf-findingaids/2026-10-09')
AEM = os.path.join(ROOT, 'sources/bnf-aem')
DEV = sorted(glob.glob(D7 + '/*.html')) + sorted(glob.glob(AEM + '/*.html'))
F2988 = D9 + '/cc49442s.html'
_cache = {}


def score(path, portals=False):
    k = (path, portals)
    if k not in _cache:
        _cache[k] = bf.score_volume(open(path, errors='ignore').read(), os.path.basename(path)[:-5], ROOT, None, portals)
    return _cache[k]


def all_scores():
    seen, out = set(), []
    for p in DEV + [F2988]:
        r = score(p)
        key = r['ark'] if r['ark'][:2] == 'cc' and not r['ark'].count('_') else p
        if r['cote'] in seen and r['items']:
            continue
        seen.add(r['cote']); out.append(r)
    return out


def test_fr2988_reproduction_and_prior_work():
    r = score(F2988, portals=True)
    assert r['bare'] == 26 and r['est_signs'] == 67600 and r['median_gap'] == 4
    assert 'Lasry' in r['prior_work'] and 'Marie Stuart' in r['prior_work']
    assert r['neighbour_trap'] == 'yes'
    assert r['open_bare'] == 0 and r['open_named'] == 2           # Ranzo f.2, f.9 stay open; f.1 known; 26 Mary items known
    others = [x for x in all_scores() if x['cote'] != 'fr.2988']
    assert max(x['bare'] for x in others) <= 3


def test_deciphered_and_key_volumes_not_ranked():
    r = score(D7 + '/cc577658.html')                              # fr.4715: 40 of 44 deciphered
    assert r['cote'] == 'fr.4715' and r['deciphered'] == 40 and r['cls'] != 'pile'
    r = score(D7 + '/cc50068t.html')                              # fr.3618: two key sheets, no bare item
    assert r['keysheets'] == 2 and r['bare'] == 0 and r['cls'] != 'pile'


def test_volume_level_notice_is_image_triage():
    r = score(D9 + '/cc518506.html')
    assert r['items'] == 0 and r['cls'] == 'image-triage'


def test_all_matched_synthetic_volume_is_excluded():
    s = ('<html><body><h1>Français 2988 • Regius 8513 • Recueil de lettres</h1>'
         '<div>Fol. 1 • 1 Lettre en chiffre de « V° HIERONIMO RANZO ».</div></body></html>')
    r = bf.score_volume(s, 'syn', ROOT, None, True)              # prior_work check 3 reads f.1 as broken by Andersson
    assert r['cls'] == 'excluded', r


def test_existing_outputs_byte_identical():
    for n in ('cc49712p', 'cc50068t'):
        out = subprocess.run([sys.executable, os.path.join(ROOT, 'tools/bnf_findingaid.py'), '--html',
                              D7 + '/%s.html' % n], capture_output=True, text=True).stdout
        assert out == open(os.path.join(ROOT, 'tools/tests/data/golden_%s.tsv' % n)).read(), n


def planted(base_path, n=10):
    s = open(base_path, errors='ignore').read()
    items = ''.join('<div>Fol. %d • %d Pièce en chiffre.</div>' % (4 * i + 200, 900 + i) for i in range(n))
    return s.replace('</body>', items + '</body>')


def sample_scores():
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(ROOT, 'tools/tests/data/bnf_pile_labels.tsv'))][1:]
    notices = {}
    for p in DEV:
        s = open(p, errors='ignore').read()
        t, items = bf.parse(s)
        notices[(bf.title_cote(t), p)] = items
    out = []
    for cote, no, label, stratum, text in rows:
        hit = next((x for (c, _), its in notices.items() if c == cote for x in its if x['no'] == no and x['text'][:90] == text), None)
        assert hit, (cote, no)
        out.append((label, bf.classify_item(hit), stratum))
    return out


def prf(sample, cls):
    tp = sum(1 for l, p, _ in sample if l == cls and p == cls)
    fp = sum(1 for l, p, _ in sample if l != cls and p == cls)
    fn = sum(1 for l, p, _ in sample if l == cls and p != cls)
    return tp, fp, fn


def test_sample_gates():
    smp = sample_scores()
    for cls, g in (('bare', .8), ('keysheet', .8), ('deciphered', .95)):
        tp, fp, fn = prf(smp, cls)
        assert tp / max(tp + fp, 1) >= g and tp / max(tp + fn, 1) >= g, (cls, tp, fp, fn)


def test_planted_pile_ranks_top5():
    base = D7 + '/cc49712p.html'                                  # fr.3251: no bare item
    assert score(base)['bare'] == 0
    rows = [r for r in all_scores() if r['cote'] != 'fr.3251']
    rows.append(bf.score_volume(planted(base), 'planted', ROOT, None, True))
    rows.sort(key=lambda r: (-r['open_bare'], -r['bare']))
    assert rows.index(next(r for r in rows if r['ark'] == 'planted')) < 5


def test_permute_null_catches_concentration_not_spread():
    """--permute (MQS-BNF-S2A): a 10-item pile in one of 20 volumes beats its null; the same 10 bare items spread one
    per volume tie their null (must-not-pass case)."""
    clear = ['Lettre de Henri III au duc de Nevers, 1585.'] * 9
    conc = [['Pièce en chiffre.'] * 10] + [clear + clear[:1]] * 19
    real, null = bf.permute_null(conc, 200)
    assert real == 10 and real > null[189]
    spread = [['Pièce en chiffre.'] + clear for _ in range(10)] + [clear + clear[:1]] * 10
    real, null = bf.permute_null(spread, 200)
    assert real == 1 and not real > null[189]


def test_permute_fr2988_offline():
    p = os.path.join(ROOT, 'sources/bnf-findingaids/2026-10-09/cc49442s.html')
    out = bf.permute_report([p] + sorted(glob.glob(os.path.join(ROOT, 'sources/bnf-findingaids/2026-10-07/*.html')))[:20], 50)
    assert 'real max bare 26' in out and 'real > p95: yes' in out


if __name__ == '__main__':
    if '--controls' in sys.argv:
        smp = sample_scores()
        for cls in ('bare', 'keysheet', 'deciphered'):
            tp, fp, fn = prf(smp, cls)
            print('C2 %-10s tp=%d fp=%d fn=%d precision=%.2f recall=%.2f' % (cls, tp, fp, fn, tp / max(tp + fp, 1), tp / max(tp + fn, 1)))
        for st in ('random', 'stratum2'):
            sub = [x for x in smp if x[2] == st]
            print('C2 stratum %-8s n=%d exact-class agreement %d/%d' % (st, len(sub), sum(1 for l, p, _ in sub if l == p), len(sub)))
        print('C2 misses:', [(l, p) for l, p, _ in smp if l != p])
        base = D7 + '/cc49712p.html'
        rows = [r for r in all_scores() if r['cote'] != 'fr.3251']
        rows.append(bf.score_volume(planted(base), 'planted', ROOT, None, True))
        rows.sort(key=lambda r: (-r['open_bare'], -r['bare']))
        print('C4 planted rank', [r['ark'] for r in rows].index('planted') + 1, 'of', len(rows), '; top5:',
              [(r['cote'], r['open_bare']) for r in rows[:5]])
        # sanity line only: shuffle all cipher-item texts across notices (cannot fail: fr.2988 holds 26 of ~30 bare items)
        import random
        pool = []
        for p in DEV + [F2988]:
            pool += [x for x in bf.parse(open(p, errors='ignore').read())[1]]
        print('sanity shuffle bare-count of the largest pseudo-volume:', end=' ')
        rnd = random.Random(1); txt = [x['text'] for x in pool]; rnd.shuffle(txt)
        k = sum(1 for t in txt[:50] if bf.classify_item({'text': t}) == 'bare')
        print(k, '(of 50 shuffled items; the real fr.2988 holds 26)')
        sys.exit(0)
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
    print('ok')

