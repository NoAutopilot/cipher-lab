#!/usr/bin/env python3
"""VIV-67B (14 Oct 2026, PREREG-VIV67B.md): the rest of the ink 67 / ink 68 pair -- BnF fr.16105 f.201v (Saint-Gouard to Charles IX,
Madrid 20 Oct 1573, cipher continued from f.201r; Gallica btv1b9009663p canvas 207 left) against the part of its clerk decipherment
that f.201r did not reach: the last 401 letters of tx/dec67_norm.txt followed by ff.206r-206v (ink 68, canvases 211 right / 212 left;
tx/viv67_merge_dec.py f206r f206v --out dec67b_norm.txt), trimmed by PREREG-VIV70B's rule (ink 67's ratio 1403/1270 + 200).
The gate is build_vivonne_f211r.control() and the truth recipe build_vivonne_f211r.truth()'s (both imported or mirrored, code
unchanged); only the target string, the clerk-split mask and the line ids differ.

    python3 benchmark-tx/build_vivonne_f201v.py --control-only   # gate only (prints, writes tx/vivk67b_result.json)
    python3 benchmark-tx/build_vivonne_f201v.py                  # control + (if PASS) truth, sha256, outputs
    python3 benchmark-tx/build_vivonne_f201v.py --check          # exit 1 if any written file is stale
"""
import difflib, hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_vivonne_f211r as b70  # noqa: E402  (control(), trim_len(), confirm2 helpers)
import build_vivonne_f201r as b67  # noqa: E402  (dec67 clerk mask)
c2 = b70.c2
sa = c2.sa
ROOT, F, TX = c2.ROOT, c2.F, c2.TX
ITEM = 'vivonne1573-f201v-dev'
TRUTH = os.path.join(HERE, ITEM + '.truth.tsv')
SHA = TRUTH + '.sha256'
ODIR = os.path.join(HERE, 'outputs', ITEM)
RESULT = os.path.join(TX, 'vivk67b_result.json')
DEC_PAGES = ('f206r', 'f206v')
TAIL = 401
SEED = b70.SEED


def rd_letters(name):
    return sa.letters(open(os.path.join(TX, name), encoding='utf-8').read())


def clerk_mask_b():
    """c2.clerk_mask's rules for ff.206r-206v against dec67b_norm.txt (as build_vivonne_f211r.clerk_mask, pages and file substituted)."""
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
    dn = ''.join(chr(97 + x) for x in rd_letters('dec67b_norm.txt'))
    out = [False] * len(dn)
    for a, b, size in difflib.SequenceMatcher(None, txt, dn, autojunk=False).get_matching_blocks():
        for t in range(size):
            out[b + t] = mask[a + t]
    return out


def target():
    """PREREG-VIV67B: T = last 401 letters of dec67 + dec67b; returns (T, mask) untrimmed."""
    l67 = rd_letters('dec67_norm.txt')
    T = list(l67[-TAIL:]) + list(rd_letters('dec67b_norm.txt'))
    mask = b67.clerk_mask(len(l67))[-TAIL:] + clerk_mask_b()
    assert len(mask) == len(T)
    return T, mask


def load():
    pub, force, grade = c2.rd_key()
    stream = c2.collapse(c2.raw_tokens(os.path.join(TX, 'f201v_rec.tsv')))
    T, mask = target()
    n = b70.trim_len(len(stream))
    return pub, force, grade, T[:n], mask[:n], stream


def main():
    pub, force, grade, let, mask, stream = load()
    seq = [t[0] for t in stream]
    res = {'item': ITEM, 'seed': SEED, 'prereg': 'PREREG-VIV67B.md', 'target_letters': len(let), 'target_untrimmed': len(target()[0]),
           'n_codes': len(seq), 'control_published': b70.control(seq, let, pub)}
    full = {}
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(F, 'key.tsv'), encoding='utf-8')]
    ix = {h: k for k, h in enumerate(rows[0])}
    for r in rows[1:]:
        if len(r[ix['meaning']]) == 1 and r[ix['meaning']].isalpha():
            full[r[ix['code']]] = c2.norm_letter(r[ix['meaning']]) if hasattr(c2, 'norm_letter') else r[ix['meaning']]
    res['control_keytsv_report_only'] = b70.control(seq, let, full, draws=50)
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
    """build_vivonne_f211r.truth()'s rules, line ids f201v_, mask passed in."""
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
        lid = 'f201v_' + line
        if code == 'oo':
            t1 = '|'.join(sorted(by_val[plain] - {'oo'} | {'o'})) if tr else ''
            rows += [(lid, raws[0], 'o', t1, plain, st, flag), (lid, raws[1], 'o', 'o' if tr else '', plain, st, flag)]
            nex[st] = nex.get(st, 0) + 2
        else:
            rows.append((lid, raws[0], code, tr, plain, st, flag))
            nex[st] = nex.get(st, 0) + 1
    ctrl = ('trim rule PREREG-VIV70B (first %d letters of dec67[-401:] + dec67b, ink-67 ratio 1403/1270 + 200); control: f.201v match '
            'share, published key %.3f vs 200 value-shuffled keys mean %.3f p95 %.3f max %.3f, rank %d of 201'
            % (len(let), ctl['real'], ctl['null_mean'], ctl['null_p95'], ctl['null_max'], ctl['rank']))
    hdr = ('# Vivonne 1573 (BnF fr.16105 f.201v, Saint-Gouard to Charles IX, Madrid 20 Oct 1573, ink 67) dev item, split=dev: clerk period '
           'decipherment (ink 68, end of f.205v + ff.206r-206v) under the published Tomokiyo key (C rows); built by '
           'benchmark-tx/build_vivonne_f201v.py (VIV-67B, PREREG-VIV67B.md), recipe of build_vivonne_confirm2.py; no verifier flags yet.\n# %s\n' % ctrl)
    body = hdr + c2.COLS + ''.join('\t'.join(str(x) for x in r) + '\n' for r in rows)
    outs = {}
    for name, path in (('committed', 'f201v_rec.tsv'), ('passA', 'f201v_passA.tsv'), ('passB', 'f201v_passB.tsv')):
        outs[name] = 'line\tpos\tsign\n' + ''.join('f201v_%s\t%d\t%s\n' % (line, i + 1, t)
                                                   for line, toks in c2.raw_tokens(os.path.join(TX, path)) for i, t in enumerate(toks))
    print('positions %d, scored %d; ' % (len(rows), nex.get('scored', 0)) + ', '.join('%s %d' % kv for kv in sorted(nex.items(), key=lambda x: -x[1])))
    fl = [r[6] for r in rows if r[5] == 'scored']
    print('flags on scored: align-conflict %d, clerk-split %d, none %d' % (sum('align-conflict' in f for f in fl),
                                                                          sum('clerk-split' in f for f in fl), sum(not f for f in fl)))
    return body, outs


if __name__ == '__main__':
    main()
