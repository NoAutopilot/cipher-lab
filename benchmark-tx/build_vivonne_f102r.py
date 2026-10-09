#!/usr/bin/env python3
"""Build the Vivonne 1573 f.102r DEV item for BENCHMARK-TX.tsv (split=dev; TXP-VIV102, PREREG-txeng2-13 DV1, 9 Oct 2026).

A copy of benchmark-tx/build_vivonne_confirm2.py (TX-CONFIRM-SET-2) re-pointed at the f.102r segment of the same aligned
stream: ITEM, the stream index (f.102r stretch instead of f.103r), line ids f102r_L??, the output dir and the input passes
changed, nothing else (same key forcing, same exclusion rules, same align-conflict / clerk-split flag rule, same control).
The same hand (the Saint-Gouard clerk, 1573) is confirm2's unseen hand, so this leaf is dev only and can never be eval or
confirm ("an item's hand is in one split only", PREREG-txeng2-0 section 0b). No verifier flags file this round (dev): the
TXV-VIV override hook is kept but reads benchmark-tx/vivonne1573-f102r-dev.flags.tsv, which does not exist.

Leaf: BnF fr.16105 f.102r (Gallica btv1b9009663p canvas 105), the first cipher leaf of the June 1573 letter, Saint-Gouard
to Charles IX (ciphers/fr16104-vivonne-spain-1572, N5-VIVK). Crops ciphers/fr16104-vivonne-spain-1572/images/
c105_f102r_L??_s{1,2}.jpg. Truth = the clerk decipherment (fr.16105 ff.104r-108v, tx/dec_norm.txt) aligned to the committed
f.102r + f.102v + f.103r stream by the N5-VIVK banded DP (j0 from tx/vivk_result.json) and forced through the published
Tomokiyo key (C rows); only the f.102r stretch is kept. Control: f.102r match share under the published key vs 200
value-shuffled keys (seed 20261009), each re-aligned by the same DP. Outputs benchmark-tx/outputs/vivonne1573-f102r-dev/
{committed,passA,passB}.tsv from tx/f102r_rec.tsv, f102r_passA.tsv, f102r_passB.tsv.

The recipe in full (exclusions, oo handling, flags) is build_vivonne_confirm2.py's docstring.

    python3 benchmark-tx/build_vivonne_f102r.py           # (re)build, print counts + control + sha256
    python3 benchmark-tx/build_vivonne_f102r.py --check   # rebuild in memory; exit 1 if truth, sha256 or outputs are stale
"""
import difflib, hashlib, json, os, random, re, sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import stream_align as sa  # noqa: E402

F = os.path.join(ROOT, 'ciphers/fr16104-vivonne-spain-1572')
TX = os.path.join(F, 'tx')
OUT = os.path.join(ROOT, 'benchmark-tx')
ITEM = 'vivonne1573-f102r-dev'
TRUTH = os.path.join(OUT, ITEM + '.truth.tsv')
SHA = TRUTH + '.sha256'
ODIR = os.path.join(OUT, 'outputs', ITEM)
WIN, WMIN = 8, 0.5
DEC_PAGES = ('f105v', 'f106r', 'f106v', 'f107r', 'f107v', 'f108r', 'f108v')
COLS = 'line\tpos\tref_sign\ttruth\tplain\tstatus\tflag\n'


def raw_tokens(path):
    """[(line, [raw tokens])] with the filtering of tx/vivk_test.tokens, but without collapsing o o."""
    out = []
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('row\t') or not ln.strip():
            continue
        parts = ln.rstrip('\n').split('\t', 1)
        if len(parts) < 2 or parts[1].strip() == 'DUP':
            continue
        s = re.sub(r'\[PLAIN:[^\]]*\]', ' ', parts[1])
        s = re.sub(r'\[\.\.\.\]|\[[^\]]*\]', ' ', s)
        out.append((parts[0], [t.rstrip('?') for t in s.split() if t.rstrip('?')]))
    return out


def collapse(lines):
    """Collapsed stream [(code, line, [raw pos...])] -- o o -> oo across the whole line, as vivk_test.tokens."""
    st = []
    for line, toks in lines:
        i = 0
        while i < len(toks):
            if toks[i] == 'o' and i + 1 < len(toks) and toks[i + 1] == 'o':
                st.append(('oo', line, [i + 1, i + 2])); i += 2
            else:
                st.append((toks[i], line, [i + 1])); i += 1
    return st


def rd_key():
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(F, 'key.tsv'), encoding='utf-8')]
    hdr, rows = rows[0], rows[1:]
    ix = {h: k for k, h in enumerate(hdr)}
    pub = {f[0]: f[1] for f in (l.rstrip('\n').split('\t') for l in open(os.path.join(F, 'key_tomokiyo.tsv'), encoding='utf-8'))
           if f[0] != 'code'}
    force, grade = {}, {}
    for r in rows:
        c, m, g = r[ix['code']], r[ix['meaning']], r[ix['grade']]
        grade[c] = g
        if c in pub and pub[c] == m and g == 'C' and 'published key' in r[ix['source']]:
            force[c] = m
    return pub, force, grade


def clerk_mask(n_letters):
    """Per letter of tx/dec_norm.txt: True when both blind readings of the clerk's hand wrote the same word there (an
    'equal' run of tx/merge_dec.py's word alignment, no doubt mark '?'), False otherwise. Rebuilt word by word with
    merge_dec's own rules, then mapped onto dec_norm letter by letter (difflib; an unmatched letter is False)."""
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
    dn = ''.join(chr(97 + x) for x in sa.letters(open(os.path.join(TX, 'dec_norm.txt'), encoding='utf-8').read()))
    assert len(dn) == n_letters, (len(dn), n_letters)
    out = [False] * len(dn)
    for a, b, size in difflib.SequenceMatcher(None, txt, dn, autojunk=False).get_matching_blocks():
        for t in range(size):
            out[b + t] = mask[a + t]
    return out


def align(seq, let, key):
    dec = np.array([ord(key[c]) - 97 if c in key else -1 for c in seq])
    d2 = np.where(dec < 0, 26, dec)
    E = np.full((27, 26), -1.0)
    E[np.arange(26), np.arange(26)] = 2.0
    ref = np.arange(len(d2) + 1) * (len(let) / len(d2))
    path, _, _ = sa.band_dp(d2, let, E, ref, 400, 1.0, 1.0, free_start=True)
    return dict(path), dec


def build():
    pub, force, grade = rd_key()
    by_val = {}
    for c, v in force.items():
        by_val.setdefault(v, set()).add(c)
    j0 = json.load(open(os.path.join(TX, 'vivk_result.json')))['j0']
    allet = sa.letters(open(os.path.join(TX, 'dec_norm.txt'), encoding='utf-8').read())
    let = allet[j0:]
    cmask = clerk_mask(len(allet))[j0:]
    pages = [('f102r', raw_tokens(os.path.join(TX, 'f102r_rec.tsv'))), ('f102v', raw_tokens(os.path.join(TX, 'f102v_rec.tsv'))),
             ('f103r', raw_tokens(os.path.join(TX, 'f103r_rec.tsv')))]
    stream = []
    for pg, lines in pages:
        stream += [(pg,) + t for t in collapse(lines)]
    seq = [t[1] for t in stream]
    amap, dec = align(seq, let, pub)
    i0 = next(k for k, t in enumerate(stream) if t[0] == 'f102r')
    i1 = next(k for k, t in enumerate(stream) if t[0] == 'f102v')

    def ok(k):  # aligned, keyed: does the decoded value equal the aligned letter?
        return dec[k] >= 0 and k in amap and dec[k] == let[amap[k]]

    def keyed(k):
        return dec[k] >= 0 and k in amap

    # control on the f.102r stretch: real key vs 200 value-shuffled keys, each re-aligned
    sub = list(range(i0, i1))
    js = [amap[k] for k in sub if k in amap]
    lo, hi = max(0, min(js) - 200), min(len(let), max(js) + 200)
    seg_seq, seg_let = seq[i0:i1], let[lo:hi]

    def share(key):
        am, dc = align(seg_seq, seg_let, key)
        n = sum(1 for k in range(len(seg_seq)) if dc[k] >= 0 and k in am)
        h = sum(1 for k in range(len(seg_seq)) if dc[k] >= 0 and k in am and dc[k] == seg_let[am[k]])
        return h / max(1, n)
    real = share(pub)
    ids, vv = list(pub), [pub[c] for c in pub]
    rng = random.Random(20261009)
    sh = []
    for _ in range(200):
        rng.shuffle(vv)
        sh.append(share(dict(zip(ids, vv))))
    rank = 1 + sum(1 for x in sh if x >= real)
    ctrl = ('control: f.102r match share, published key %.3f vs 200 value-shuffled keys mean %.3f p95 %.3f max %.3f, rank %d of '
            '201' % (real, sum(sh) / len(sh), sorted(sh)[189], max(sh), rank))

    # TXV-VIV (9 Oct 2026): verifier verdicts on the align-conflict positions, keyed by the oo's first raw position (both raw
    # rows of a collapsed oo carry the same verdict); FLAG -> class in the flag column, CORRECT -> truth re-forced, KEEP -> cleared
    flags = {}
    fp = os.path.join(OUT, ITEM + '.flags.tsv')
    if os.path.exists(fp):
        lines = [l for l in open(fp, encoding='utf-8').read().splitlines() if not l.startswith('#')]
        hd = lines[0].split('\t')
        for l in lines[1:]:
            r = dict(zip(hd, l.split('\t')))
            flags[(r['line'], int(r['pos']))] = r
    rows, nex = [], {}
    for k in sub:
        pg, code, line, raws = stream[k]
        plain = chr(97 + let[amap[k]]) if k in amap else ''
        truth, st, flag = '', 'scored', ''
        if k not in amap:
            st = 'excluded:unaligned'
        elif code not in force:
            st = ('excluded:key-M-' + code) if grade.get(code) == 'M' else 'excluded:off-key'
        elif plain not in by_val:
            st = 'excluded:letter-off-key'
        else:
            nb = [j for j in range(k - WIN, k + WIN + 1) if j != k and i0 <= j < i1 and keyed(j)]
            if not nb or sum(1 for j in nb if ok(j)) / len(nb) < WMIN:
                st = 'excluded:align-uncertain'
            else:
                truth = '|'.join(sorted(by_val[plain]))
                fl = []
                if force[code] != plain:
                    fl.append('align-conflict')
                if not cmask[amap[k]]:
                    fl.append('clerk-split')
                fr = flags.get(('f102r_' + line, raws[0]))
                if fr and 'align-conflict' in fl:  # TXV-VIV verdict replaces the automatic align-conflict flag
                    fl.remove('align-conflict')
                    if fr['verdict'] == 'FLAG':
                        fl.insert(0, fr['class'])
                    elif fr['verdict'] == 'CORRECT':
                        cp = fr['correct_plain'] or plain
                        truth = '|'.join(sorted(by_val.get(cp, set()) | set(filter(None, fr['add_signs'].split('|')))))
                        fl.insert(0, 'corrected:' + fr['class'])
                flag = ','.join(fl)
        if code == 'oo':
            t1 = '|'.join(sorted(by_val[plain] - {'oo'} | {'o'})) if truth else ''
            rows.append(('f102r_' + line, raws[0], 'o', t1, plain, st, flag))
            rows.append(('f102r_' + line, raws[1], 'o', 'o' if truth else '', plain, st, flag))
            n_add = 2
        else:
            rows.append(('f102r_' + line, raws[0], code, truth, plain, st, flag))
            n_add = 1
        nex[st] = nex.get(st, 0) + n_add
    hdr = ('# Vivonne 1573 (BnF fr.16105 f.102r, Saint-Gouard to Charles IX) dev item, split=dev: clerk period '
           'decipherment (ff.104r-108v) under the published Tomokiyo key (C rows); built by benchmark-tx/'
           'build_vivonne_f102r.py (TXP-VIV102, PREREG-txeng2-13 DV1). Same hand as confirm2: dev only, never eval/confirm.\n# %s\n' % ctrl)
    body = hdr + COLS + ''.join('\t'.join(str(x) for x in r) + '\n' for r in rows)
    outs = {}
    for name, path in (('committed', 'f102r_rec.tsv'), ('passA', 'f102r_passA.tsv'), ('passB', 'f102r_passB.tsv')):
        outs[name] = 'line\tpos\tsign\n' + ''.join('f102r_%s\t%d\t%s\n' % (line, i + 1, t)
                                                   for line, toks in raw_tokens(os.path.join(TX, path)) for i, t in enumerate(toks))
    return body, outs, nex, ctrl, rows


def main():
    body, outs, nex, ctrl, rows = build()
    sha = hashlib.sha256(body.encode()).hexdigest()
    shaline = '%s  %s\n' % (sha, os.path.basename(TRUTH))
    if '--check' in sys.argv:
        stale = []
        for p, want in [(TRUTH, body), (SHA, shaline)] + [(os.path.join(ODIR, n + '.tsv'), b) for n, b in outs.items()]:
            if not os.path.exists(p) or open(p, encoding='utf-8').read() != want:
                stale.append(os.path.relpath(p, ROOT))
        print('stale: ' + ', '.join(stale) if stale else 'ok: truth, sha256 and outputs current (%s)' % sha)
        sys.exit(1 if stale else 0)
    with open(TRUTH, 'w', encoding='utf-8') as f:
        f.write(body)
    with open(SHA, 'w', encoding='utf-8') as f:
        f.write(shaline)
    os.makedirs(ODIR, exist_ok=True)
    for n, b in outs.items():
        with open(os.path.join(ODIR, n + '.tsv'), 'w', encoding='utf-8') as f:
            f.write(b)
    n_pos = len(rows)
    print('positions %d, scored %d, excluded %d' % (n_pos, nex.get('scored', 0), n_pos - nex.get('scored', 0)))
    print('status counts:', ', '.join('%s %d' % kv for kv in sorted(nex.items(), key=lambda x: -x[1])))
    fl = [r[6] for r in rows if r[5] == 'scored']
    print('flags on scored: align-conflict %d, clerk-split %d, any %d, none %d' % (
        sum('align-conflict' in f for f in fl), sum('clerk-split' in f for f in fl), sum(bool(f) for f in fl),
        sum(not f for f in fl)))
    print('align-conflict share among clerk-agreed scored: %d/%d' % (
        sum(f == 'align-conflict' for f in fl), sum('clerk-split' not in f for f in fl)))
    print(ctrl)
    print('sha256', sha)


if __name__ == '__main__':
    main()
