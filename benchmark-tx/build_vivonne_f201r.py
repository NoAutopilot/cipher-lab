#!/usr/bin/env python3
"""VIV-67 (14 Oct 2026, PREREG-VIV67.md): the ink 67 / ink 68 known-plaintext pair -- BnF fr.16105 f.201r (Saint-Gouard to
Charles IX, Madrid 20 Oct 1573; Gallica btv1b9009663p canvas 206 right) against its clerk decipherment ff.205r-205v (ink 68,
"dechiffre de la precedente", canvases 210 right / 211 left) -- the alignment control and, if it passes, a split=dev
BENCHMARK-TX item built with build_vivonne_confirm2.py's recipe (its functions imported, unchanged).

    python3 benchmark-tx/build_vivonne_f201r.py --control-only   # gate only (prints, writes tx/vivk67_result.json)
    python3 benchmark-tx/build_vivonne_f201r.py                  # control + (if PASS) truth, sha256, outputs
    python3 benchmark-tx/build_vivonne_f201r.py --check          # exit 1 if any written file is stale

Inputs: ciphers/fr16104-vivonne-spain-1572/tx/f201r_rec.tsv (reconciled), f201r_passA/passB.tsv (blind), dec67_norm.txt
(tx/viv67_merge_dec.py), dec_f205r/f205v_passA/passB.txt (clerk-split mask). Control (gating): the whole f.201r stream decoded
with the published key and aligned by confirm2's align() to the whole dec67 letter string; window = aligned span +-200; match
share under the published key vs 200 value-shuffled keys (random.Random(20261014)), each re-aligned in the window; PASS iff rank 1
of 201 and real > p95 (sorted[189]). Truth rows as confirm2: forcing key = published-and-C rows of key.tsv; excluded unaligned /
off-key / key-M / letter-off-key / align-uncertain (window 8, 0.5); flags align-conflict, clerk-split. No verifier flags file.
"""
import difflib, hashlib, json, os, random, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_vivonne_confirm2 as c2  # noqa: E402
sa = c2.sa
ROOT, F, TX = c2.ROOT, c2.F, c2.TX
ITEM = 'vivonne1573-f201r-dev'
TRUTH = os.path.join(HERE, ITEM + '.truth.tsv')
SHA = TRUTH + '.sha256'
ODIR = os.path.join(HERE, 'outputs', ITEM)
RESULT = os.path.join(TX, 'vivk67_result.json')
DEC_PAGES = ('f205r', 'f205v')
SEED = 20261014


def clerk_mask(n_letters):
    """c2.clerk_mask for the ink-68 pages and dec67_norm.txt (same rules)."""
    sys.path.insert(0, TX)
    import merge_dec as md
    txt, mask = '', []
    for p in DEC_PAGES:
        rl = lambda q: [l for l in open(os.path.join(TX, 'dec_%s_%s.txt' % (p, q)), encoding='utf-8').read().splitlines() if l.strip()]
        wa = [w for w in ' \n '.join(rl('passA')).split(' ') if w]
        wb = [w for w in ' \n '.join(rl('passB')).split(' ') if w]
        sm = difflib.SequenceMatcher(None, [md.norm(w) for w in wa], [md.norm(w) for w in wb], autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                ws, ag = wa[i1:i2], True
            elif op == 'replace':
                ws, ag = (wa[i1:i2] if md.doubt(wa[i1:i2]) <= md.doubt(wb[j1:j2]) else wb[j1:j2]), False
            else:
                ws, ag = (wa[i1:i2] if op == 'delete' else wb[j1:j2]), False
            for w in ws:
                n = md.norm(w)
                txt += n
                mask += [ag and '?' not in w] * len(n)
    dn = ''.join(chr(97 + x) for x in sa.letters(open(os.path.join(TX, 'dec67_norm.txt'), encoding='utf-8').read()))
    assert len(dn) == n_letters, (len(dn), n_letters)
    out = [False] * len(dn)
    for a, b, size in difflib.SequenceMatcher(None, txt, dn, autojunk=False).get_matching_blocks():
        for t in range(size):
            out[b + t] = mask[a + t]
    return out


def load():
    pub, force, grade = c2.rd_key()
    let = sa.letters(open(os.path.join(TX, 'dec67_norm.txt'), encoding='utf-8').read())
    stream = c2.collapse(c2.raw_tokens(os.path.join(TX, 'f201r_rec.tsv')))
    return pub, force, grade, let, stream


def control(seq, let, key, draws=200):
    amap, dec = c2.align(seq, let, key)
    js = list(amap.values())
    lo, hi = max(0, min(js) - 200), min(len(let), max(js) + 200)
    seg = let[lo:hi]

    def share(k):
        am, dc = c2.align(seq, seg, k)
        n = sum(1 for i in range(len(seq)) if dc[i] >= 0 and i in am)
        h = sum(1 for i in range(len(seq)) if dc[i] >= 0 and i in am and dc[i] == seg[am[i]])
        return h / max(1, n), n
    real, nk = share(key)
    ids, vv = list(key), [key[c] for c in key]
    rng = random.Random(SEED)
    sh = []
    for _ in range(draws):
        rng.shuffle(vv)
        sh.append(share(dict(zip(ids, vv)))[0])
    s = sorted(sh)
    q = 189 if draws == 200 else int(0.95 * draws) - 1  # 200 draws: sorted[189], confirm2's index
    rank = 1 + sum(1 for x in sh if x >= real)
    return {'real': round(real, 4), 'aligned_keyed': nk, 'null_mean': round(sum(sh) / len(sh), 4), 'null_p95': round(s[q], 4),
            'null_max': round(s[-1], 4), 'rank': rank, 'window': [lo, hi], 'n_letters': len(let), 'n_signs': len(seq),
            'verdict': 'PASS' if rank == 1 and real > s[q] else 'FAIL'}


def main():
    pub, force, grade, let, stream = load()
    seq = [t[0] for t in stream]
    res = {'item': ITEM, 'seed': SEED, 'control_published': control(seq, let, pub)}
    full = {}
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(F, 'key.tsv'), encoding='utf-8')]
    ix = {h: k for k, h in enumerate(rows[0])}
    for r in rows[1:]:
        if len(r[ix['meaning']]) == 1 and r[ix['meaning']].isalpha():
            full[r[ix['code']]] = c2.norm_letter(r[ix['meaning']]) if hasattr(c2, 'norm_letter') else r[ix['meaning']]
    res['control_keytsv_report_only'] = control(seq, let, full, draws=50)
    print(json.dumps(res, indent=1))
    if '--check' not in sys.argv:
        json.dump(res, open(RESULT, 'w'), indent=1)
    if '--control-only' in sys.argv or res['control_published']['verdict'] != 'PASS':
        sys.exit(0 if res['control_published']['verdict'] == 'PASS' else 3)
    body, outs = truth(pub, force, grade, let, stream, res['control_published'])
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


def truth(pub, force, grade, let, stream, ctl):
    by_val = {}
    for c, v in force.items():
        by_val.setdefault(v, set()).add(c)
    seq = [t[0] for t in stream]
    amap, dec = c2.align(seq, let, pub)
    cmask = clerk_mask(len(let))
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
        lid = 'f201r_' + line
        if code == 'oo':
            t1 = '|'.join(sorted(by_val[plain] - {'oo'} | {'o'})) if tr else ''
            rows += [(lid, raws[0], 'o', t1, plain, st, flag), (lid, raws[1], 'o', 'o' if tr else '', plain, st, flag)]
            nex[st] = nex.get(st, 0) + 2
        else:
            rows.append((lid, raws[0], code, tr, plain, st, flag))
            nex[st] = nex.get(st, 0) + 1
    ctrl = ('control: f.201r match share, published key %.3f vs 200 value-shuffled keys mean %.3f p95 %.3f max %.3f, rank %d of 201'
            % (ctl['real'], ctl['null_mean'], ctl['null_p95'], ctl['null_max'], ctl['rank']))
    hdr = ('# Vivonne 1573 (BnF fr.16105 f.201r, Saint-Gouard to Charles IX, 20 Oct 1573, ink 67) dev item, split=dev: clerk period '
           'decipherment (ink 68, ff.205r-205v) under the published Tomokiyo key (C rows); built by benchmark-tx/build_vivonne_f201r.py '
           '(VIV-67, PREREG-VIV67.md), recipe of build_vivonne_confirm2.py; no verifier flags yet.\n# %s\n' % ctrl)
    body = hdr + c2.COLS + ''.join('\t'.join(str(x) for x in r) + '\n' for r in rows)
    outs = {}
    for name, path in (('committed', 'f201r_rec.tsv'), ('passA', 'f201r_passA.tsv'), ('passB', 'f201r_passB.tsv')):
        outs[name] = 'line\tpos\tsign\n' + ''.join('f201r_%s\t%d\t%s\n' % (line, i + 1, t)
                                                   for line, toks in c2.raw_tokens(os.path.join(TX, path)) for i, t in enumerate(toks))
    n = len(rows)
    print('positions %d, scored %d; ' % (n, nex.get('scored', 0)) + ', '.join('%s %d' % kv for kv in sorted(nex.items(), key=lambda x: -x[1])))
    fl = [r[6] for r in rows if r[5] == 'scored']
    print('flags on scored: align-conflict %d, clerk-split %d, none %d' % (sum('align-conflict' in f for f in fl),
                                                                          sum('clerk-split' in f for f in fl), sum(not f for f in fl)))
    return body, outs


if __name__ == '__main__':
    main()
