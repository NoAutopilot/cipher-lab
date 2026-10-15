#!/usr/bin/env python3
"""VIV-70C2 (15 Oct 2026, PREREG-VIV70C.md): the rest of the ink 70 / ink 71 pair -- BnF fr.16105 f.211v (Saint-Gouard to Charles IX,
Madrid 4 Nov 1573, cipher continued from f.211r; btv1b9009663p canvas 217 left) against the part of its clerk decipherment that
f.211r did not reach: tx/dec70_norm.txt letters[533:] (ff.215r-215v; f.211r's aligned span ended at 533, tx/vivk70b_result.json),
trimmed by PREREG-VIV70B's rule (ink 67's ratio 1403/1270 + 200) -- the rule's first blind use on a pair that did not supply its constant.
The gate is build_vivonne_f211r.control() (imported, code unchanged); the truth recipe is build_vivonne_f201v.truth()'s (mirrored);
only the target string, the clerk-split mask and the line ids differ. Also reports the trim rule's own verdict (PREREG-VIV70C):
span of the untrimmed alignment vs the predicted int(n x 1403/1270), PASS iff the gate passes and |span - pred| / pred <= 0.15.

    python3 benchmark-tx/build_vivonne_f211v.py --control-only   # gate only (prints, writes tx/vivk70c_result.json)
    python3 benchmark-tx/build_vivonne_f211v.py                  # control + (if PASS) truth, sha256, outputs
    python3 benchmark-tx/build_vivonne_f211v.py --check          # exit 1 if any written file is stale
"""
import difflib, hashlib, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_vivonne_f211r as b70  # noqa: E402  (control(), trim_len(), confirm2 helpers)
c2 = b70.c2
sa = c2.sa
ROOT, F, TX = c2.ROOT, c2.F, c2.TX
ITEM = 'vivonne1573-f211v-dev'
TRUTH = os.path.join(HERE, ITEM + '.truth.tsv')
SHA = TRUTH + '.sha256'
ODIR = os.path.join(HERE, 'outputs', ITEM)
RESULT = os.path.join(TX, 'vivk70c_result.json')
OFFSET = 533  # f.211r aligned end in dec70 (window [0, 733] - 200)
SEED = b70.SEED


def rd_letters(name):
    return sa.letters(open(os.path.join(TX, name), encoding='utf-8').read())


def target():
    """PREREG-VIV70C: T = dec70 letters[533:]; returns (T, mask) untrimmed."""
    l70 = rd_letters('dec70_norm.txt')
    T = np.asarray(l70[OFFSET:])
    mask = b70.clerk_mask(len(l70))[OFFSET:]
    assert len(mask) == len(T)
    return T, mask


def trim_rule(seq, T, pub, gate):
    """PREREG-VIV70C: span of f.211v in the untrimmed T (c2.align, report only) vs int(n x ratio)."""
    amap, _ = c2.align(seq, T, pub)
    js = list(amap.values())
    span = max(js) - min(js) + 1
    pred = b70.trim_len(len(seq)) - 200
    exercised = pred + 200 < len(T)
    dev = (span - pred) / pred
    v = 'not tested' if not exercised else ('PASS' if gate == 'PASS' and abs(dev) <= 0.15 else 'FAIL')
    return {'untrimmed_letters': len(T), 'aligned_first': min(js), 'aligned_last': max(js), 'span': span, 'predicted': pred,
            'deviation': round(dev, 4), 'exercised': exercised, 'tolerance': 0.15, 'verdict': v}


def load():
    pub, force, grade = c2.rd_key()
    stream = c2.collapse(c2.raw_tokens(os.path.join(TX, 'f211v_rec.tsv')))
    T, mask = target()
    n = b70.trim_len(len(stream))
    return pub, force, grade, T[:n], mask[:n], stream


def main():
    pub, force, grade, let, mask, stream = load()
    seq = [t[0] for t in stream]
    res = {'item': ITEM, 'seed': SEED, 'prereg': 'PREREG-VIV70C.md', 'target_letters': len(let), 'target_untrimmed': len(target()[0]),
           'n_codes': len(seq), 'control_published': b70.control(seq, let, pub)}
    full = {}
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(F, 'key.tsv'), encoding='utf-8')]
    ix = {h: k for k, h in enumerate(rows[0])}
    for r in rows[1:]:
        if len(r[ix['meaning']]) == 1 and r[ix['meaning']].isalpha():
            full[r[ix['code']]] = c2.norm_letter(r[ix['meaning']]) if hasattr(c2, 'norm_letter') else r[ix['meaning']]
    res['control_keytsv_report_only'] = b70.control(seq, let, full, draws=50)
    res['trim_rule'] = trim_rule(seq, target()[0], pub, res['control_published']['verdict'])
    print(json.dumps(res, indent=1))
    if '--check' not in sys.argv:
        json.dump(res, open(RESULT, 'w'), indent=1)
    if '--control-only' in sys.argv or res['control_published']['verdict'] != 'PASS':
        sys.exit(0 if res['control_published']['verdict'] == 'PASS' else 3)
    body, outs = truth(pub, force, grade, let, mask, stream, res['control_published'])
    sha = hashlib.sha256(body.encode()).hexdigest()
    shaline = '%s  %s\n' % (sha, os.path.basename(TRUTH))
    files = [(TRUTH, body), (SHA, shaline)] + [(os.path.join(ODIR, n + '.tsv'), b) for n, b in outs.items()]
    if '--check' in sys.argv:
        stale = [os.path.relpath(p, ROOT) for p, w in files if not os.path.exists(p) or open(p, encoding='utf-8').read() != w]
        print('stale: ' + ', '.join(stale) if stale else 'ok: truth, sha256 and outputs current (%s)' % sha)
        sys.exit(1 if stale else 0)
    os.makedirs(ODIR, exist_ok=True)
    for p, w in files:
        open(p, 'w', encoding='utf-8').write(w)
    print('sha256', sha)


def truth(pub, force, grade, let, cmask, stream, ctl):
    """build_vivonne_f211r.truth()'s rules, line ids f211v_, mask passed in."""
    by_val = {}
    for c, v in force.items():
        by_val.setdefault(v, set()).add(c)
    seq = [t[0] for t in stream]
    amap, dec = c2.align(seq, let, pub)
    ok = lambda k: dec[k] >= 0 and k in amap and dec[k] == let[amap[k]]
    keyed = lambda k: dec[k] >= 0 and k in amap
    rows, nex = [], {}
    for k, (code, line, raws) in enumerate(stream):
        plain = chr(97 + let[amap[k]]) if k in amap else ''
        tr, st, flag = '', 'scored', ''
        if k not in amap:
            st = 'excluded:unaligned'
        elif code not in force:
            st = ('excluded:key-M-' + code) if grade.get(code) == 'M' else 'excluded:off-key'
        elif plain not in by_val:
            st = 'excluded:letter-off-key'
        else:
            nb = [j for j in range(k - c2.WIN, k + c2.WIN + 1) if j != k and 0 <= j < len(stream) and keyed(j)]
            if not nb or sum(1 for j in nb if ok(j)) / len(nb) < c2.WMIN:
                st = 'excluded:align-uncertain'
            else:
                tr = '|'.join(sorted(by_val[plain]))
                fl = []
                if force[code] != plain:
                    fl.append('align-conflict')
                if not cmask[amap[k]]:
                    fl.append('clerk-split')
                flag = ','.join(fl)
        lid = 'f211v_' + line
        if code == 'oo':
            t1 = '|'.join(sorted(by_val[plain] - {'oo'} | {'o'})) if tr else ''
            rows += [(lid, raws[0], 'o', t1, plain, st, flag), (lid, raws[1], 'o', 'o' if tr else '', plain, st, flag)]
            nex[st] = nex.get(st, 0) + 2
        else:
            rows.append((lid, raws[0], code, tr, plain, st, flag))
            nex[st] = nex.get(st, 0) + 1
    ctrl = ('trim rule PREREG-VIV70B (first %d letters of dec70[533:], ink-67 ratio 1403/1270 + 200); control: f.211v match '
            'share, published key %.3f vs 200 value-shuffled keys mean %.3f p95 %.3f max %.3f, rank %d of 201'
            % (len(let), ctl['real'], ctl['null_mean'], ctl['null_p95'], ctl['null_max'], ctl['rank']))
    hdr = ('# Vivonne 1573 (BnF fr.16105 f.211v, Saint-Gouard to Charles IX, Madrid 4 Nov 1573, ink 70) dev item, split=dev: clerk period '
           'decipherment (ink 71, ff.215r-215v from letter 533) under the published Tomokiyo key (C rows); built by '
           'benchmark-tx/build_vivonne_f211v.py (VIV-70C2, PREREG-VIV70C.md), recipe of build_vivonne_confirm2.py; no verifier flags yet.\n# %s\n' % ctrl)
    body = hdr + c2.COLS + ''.join('\t'.join(str(x) for x in r) + '\n' for r in rows)
    outs = {}
    for name, path in (('committed', 'f211v_rec.tsv'), ('passA', 'f211v_passA.tsv'), ('passB', 'f211v_passB.tsv')):
        outs[name] = 'line\tpos\tsign\n' + ''.join('f211v_%s\t%d\t%s\n' % (line, i + 1, t)
                                                   for line, toks in c2.raw_tokens(os.path.join(TX, path)) for i, t in enumerate(toks))
    print('positions %d, scored %d; ' % (len(rows), nex.get('scored', 0)) + ', '.join('%s %d' % kv for kv in sorted(nex.items(), key=lambda x: -x[1])))
    fl = [r[6] for r in rows if r[5] == 'scored']
    print('flags on scored: align-conflict %d, clerk-split %d, none %d' % (sum('align-conflict' in f for f in fl),
                                                                          sum('clerk-split' in f for f in fl), sum(not f for f in fl)))
    return body, outs


if __name__ == '__main__':
    main()
