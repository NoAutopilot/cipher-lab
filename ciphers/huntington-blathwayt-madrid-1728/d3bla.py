#!/usr/bin/env python3
"""D3-BLA residue re-grade (8 Oct 2026, PREREG-D3BLA.md): rules I2 (tie), I3 (sibling glosses), I4 (BLA190 p7 one-system
test) and the shuffled-code controls over the non-C target tokens.

  python3 d3bla.py           write d3bla_summary.json
  python3 d3bla.py --check   exit 1 if d3bla_summary.json is stale
Reads ciphertext.tsv, ciphertext_targets.tsv (+ the I1 overlay d3bla_signs.tsv), key.tsv and the PRE-D3BLA token list (D3BLA_UNIVERSE: the 42 non-C tokens at
origin/main beefb778f). Deterministic (numpy default_rng, seeds 0-999)."""
import csv, json, os, sys, collections, unicodedata
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
UNIVERSE = [  # (line, pos, group) of the 42 non-C tokens before this job
 ('BLA184_p1_L01',2,'1259'),('BLA184_p1_L02',1,'1240'),('BLA184_p1_L03',2,'1240'),('BLA184_p1_L04',1,'1250'),
 ('BLA186_p1_L01',3,'73'),('BLA186_p1_L01',7,'470'),('BLA186_p1_L01',8,'778'),('BLA186_p1_L01',9,'190'),
 ('BLA191_p5_L01',2,'805'),('BLA191_p5_L01',8,'665'),('BLA191_p5_L01',9,'941'),('BLA191_p5_L01',11,'386'),
 ('BLA191_p5_L02',8,'6'),('BLA191_p5_L03',3,'1210'),('BLA191_p5_L03',5,'689'),('BLA191_p5_L04',4,'1250'),
 ('BLA191_p5_L04',8,'460'),('BLA191_p5_L05',3,'285'),('BLA191_p5_L05',10,'1099'),('BLA191_p5_L06',1,'214'),
 ('BLA191_p5_L07',4,'1019'),('BLA191_p5_L07',5,'711'),('BLA191_p5_L07',9,'937'),('BLA191_p5_L08',10,'1118'),
 ('BLA191_p5_L09',1,'1052'),('BLA191_p5_L11',1,'46'),('BLA191_p5_L11',2,'836'),('BLA191_p5_L11',3,'385'),
 ('BLA191_p5_L11',5,'585'),('BLA191_p5_L11',8,'1152'),('BLA191_p5_L12',2,'1018'),('BLA191_p5_L12',3,'26'),
 ('BLA191_p5_L12',4,'591'),('BLA191_p5_L12',5,'1185'),('BLA191_p5_L12',6,'275'),('BLA191_p5_L12',7,'659'),
 ('BLA191_p5_L12',8,'585'),('BLA191_p5_L12',9,'758'),('BLA191_p5_L12',10,'942'),('BLA191_p5_L12',11,'754'),
 ('BLA191_p5_L12',12,'163'),('BLA191_p5_L13',9,'222')]


def rd(n):
    return list(csv.DictReader(open(os.path.join(HERE, n)), delimiter='\t'))


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isalpha())
    out = ''
    for c in s:
        if not out or out[-1] != c:
            out += c
    return out


def tie_one(val):
    """I2 tie rule: 'a|b' is one word in two spellings -> the longer form, else None."""
    if '|' not in val:
        return val
    a, b = val.split('|', 1)
    na, nb = norm(a), norm(b)
    short, lng = sorted((na, nb), key=len)
    if na == nb or (len(short) >= 5 and lng.startswith(short)):
        return max((a, b), key=len)
    return None


def main():
    ct = rd('ciphertext.tsv')
    key = {r['code']: r['value'] for r in rd('key.tsv')}
    tconf = {(r['line'], int(r['pos'])): r['conf'] for r in rd('ciphertext_targets.tsv')}
    for r in rd('d3bla_signs.tsv'):  # I1 sign settlements, overlaid here only (not in settle_image.tsv: gate failed)
        tconf[(r['line'], int(r['pos']))] = r['conf']
    assert len(UNIVERSE) == 42
    # I2/I3 on the target
    def grade(code, conf):
        if code in key:
            v = tie_one(key[code])
            return 'C' if (conf == 'H' and v is not None) else 'M'
        return 'U'  # I3: no H-column gloss (else it would be in key); M-column glosses checked below
    target = {}
    for l, p, g in UNIVERSE:
        target['%s/%d' % (l, p)] = (g, tconf[(l, p)], grade(g, tconf[(l, p)]))
    # I3: glosses of U codes on M columns or as alternatives
    ucodes = sorted({g for g, c, gr in target.values() if gr == 'U'}, key=int)
    i3 = {}
    for g in ucodes:
        hits = [(r['line'], r['pos'], r['conf'], r['gloss']) for r in ct
                if (r['group'] == g or g in r['alt'].replace('B:', ' ').replace('A:', ' ').split()) and r['gloss']]
        i3[g] = hits
    # I4: BLA190 p7 one-system test
    ev = [(r['line'], r['group'], r['gloss']) for r in ct if r['conf'] == 'H' and r['gloss'] and r['group'] not in ('?', '-')]
    other = collections.defaultdict(collections.Counter)
    for l, g, gl in ev:
        if not l.startswith('BLA190_p7'):
            other[g][gl] += 1
    tot = agree = 0
    for l, g, gl in ev:
        if l.startswith('BLA190_p7') and g in other:
            mc = other[g].most_common()
            vals = {k for k, c in mc if c == mc[0][1]}
            tot += 1
            agree += gl in vals
    p7share = agree / tot if tot else None
    # controls
    codes = sorted({r['group'] for r in ct if r['group'] not in ('?', '-')}, key=int)
    confs = [target['%s/%d' % (l, p)][1] for l, p, g in UNIVERSE]
    ucs = [g for l, p, g in UNIVERSE]
    tC = sum(1 for v in target.values() if v[2] == 'C')
    ra, rb = [], []
    for s in range(1000):
        rng = np.random.default_rng(s)
        draw = rng.choice(codes, size=42)
        ra.append(sum(grade(str(c), cf) == 'C' for c, cf in zip(draw, confs)))
        perm = rng.permutation(ucs)
        rb.append(sum(grade(c, cf) == 'C' for c, cf in zip(perm, confs)))
    ra, rb = np.array(ra), np.array(rb)
    out = {'target_C_of_42': tC,
           'target_grades': collections.Counter(v[2] for v in target.values()),
           'tie_rule_promotions': sorted(k for k, v in target.items() if v[2] == 'C' and '|' in key.get(v[0], '')),
           'i3_glosses_for_U_codes': i3,
           'i4_p7': {'columns': tot, 'agree': agree, 'share': round(p7share, 3), 'gate': 0.65,
                     'verdict': 'same system, glosses kept' if p7share >= 0.65 else 'drop p7'},
           'control_a_random_code': {'mean': round(float(ra.mean()), 2), 'p95': float(np.percentile(ra, 95)),
                                     'max': int(ra.max())},
           'control_b_permutation': {'mean': round(float(rb.mean()), 2), 'p95': float(np.percentile(rb, 95)),
                                     'max': int(rb.max()), 'note': 'non-discriminating by construction (PREREG)'},
           'n_codes_drawn_from': len(codes)}
    out['gate_pass'] = tC > out['control_a_random_code']['p95']
    js = json.dumps(out, indent=1, ensure_ascii=False, sort_keys=True) + '\n'
    path = os.path.join(HERE, 'd3bla_summary.json')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path).read() == js
        print('d3bla_summary.json', 'up to date' if ok else 'STALE')
        sys.exit(0 if ok else 1)
    open(path, 'w').write(js)
    print(js)


if __name__ == '__main__':
    main()
