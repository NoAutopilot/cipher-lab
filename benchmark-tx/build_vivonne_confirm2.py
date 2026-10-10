#!/usr/bin/env python3
"""Build the Vivonne 1573 f.103r confirmation item for BENCHMARK-TX.tsv (split=confirm2; TX-CONFIRM-SET-2, 9 Oct 2026).

LANE TX-ENGINEER-2 guard S2 (.claude/briefs/runs/2026-10-09-account4-lane-tx-engineer-2.md): one known-answer item on a hand
none of the six benchmark items use, built by a session outside the lane, scored by the lane ONCE, at the end, with its
frozen pipeline. The lane does not open this file, its truth TSV, its outputs or this item's line crops before that score.

Leaf: BnF fr.16105 f.103r (Gallica btv1b9009663p canvas 106, right page), Jean de Vivonne, sr de Saint-Gouard, ambassador in
Spain, to Charles IX, Madrid, June 1573 (old ink piece 40; ciphers/fr16104-vivonne-spain-1572, N5-VIVK). A symbol cipher in
the Saint-Gouard 1572-74 key (Latin-cursive-looking signs, digits, marks) in a hand, office, decade and key family none of
the six items use (Birago 1572, Ceppo-Nevers, Dinteville 1592, Spinelli c.1515).

Truth = the sign(s) the clerk's decipherment forces under the published key, per position of the committed (reconciled)
transcription tx/f103r_rec.tsv, the recipe of build_birago87.py / build_spinelli_confirm.py:
  - known text: the clerk's period decipherment of this letter, fr.16105 ff.104r-108v ("dechiffré de la precedente", old ink
    piece 41; N4-VIV2), read in two blind passes per page and merged (tx/dec_f105v..f108v_merged.txt, normalised to
    tx/dec_norm.txt by N5-VIVK). Period clerk decipherment = C; the eye reading of the clerk's hand is noisy (A/B word
    agreement 0.66-0.71), which this build handles by the align-uncertain window and the align-conflict flag below;
  - alignment: the committed sequence f.102r + f.102v + f.103r ("o o" collapsed to oo, DUP lines and [PLAIN]/[...] dropped,
    exactly tx/vivk_test.tokens) decoded with the published key and aligned to dec_norm[j0:] by the same semi-global banded
    DP as tx/key_support.py (tools/stream_align.band_dp, band 400, match 2, mismatch -1, gaps 1; j0 = 1265 from
    tx/vivk_result.json, N5-VIVK's registered anchor). Only the f.103r stretch is kept;
  - key: key.tsv rows whose source is Tomokiyo's published table (henryiii_Vivonne1.png) AND whose grade is C (the clerk
    decipherment supports the value, tx/key_support.py). M rows (S, y, b, A) never force; V (n, from clerk word anchors,
    not the published table) and every label outside the table never force.
A plain letter L forces the SET of those codes whose value is L (homophones), so err_true is value-level, as on no.87.

Excluded (counted, never scored): sign aligned to no letter (unaligned); committed token outside the forcing key
(off-key: V, c, 2, o, braces, residues) or M-graded (key-M-<code>); aligned letter that no forcing code carries
(letter-off-key); align-uncertain: fewer than half of the aligned keyed neighbours within 8 positions either side
(same line stream) decode to their aligned letter (a stretch where the clerk reading or the alignment is unreliable).
Flag column (set at build time, before any reader score; tx_bench --exclude-flagged reports both figures; the align-conflict
flag is replaced per position by the verifier verdicts in benchmark-tx/vivonne1573-f103r-confirm2.flags.tsv, TXV-VIV, 9 Oct 2026:
FLAG -> its class (clerk-doubtful / key-doubtful / alignment-doubtful), CORRECT -> truth re-forced and corrected:<class>, KEEP ->
the align-conflict flag cleared, clerk-split kept where set):
  align-conflict  scored position whose committed sign decodes to a different letter than the aligned one (reader error,
                  clerk-reading error or a one-letter shift: undecidable here);
  clerk-split     the aligned letter sits in a word the two blind readings of the clerk's hand did not write alike (or
                  marked '?'), so the known text itself is doubtful there (clerk_mask()).

oo: the committed transcription writes u's "oo" sign as two tokens "o o" (tx/SIGNS.md). Positions are the RAW tokens of
tx/f103r_rec.tsv so that readers writing "o o" align one-to-one; a collapsed oo forced by u gives its first o the truth
o|a|Zu (any homophone of u) and its second o the truth o; both carry the same status.
Line ids: f103r_L01..L37 (crops ciphers/fr16104-vivonne-spain-1572/images/c106_f103r_L??_s{1,2}.jpg; L27 is a DUP band and
is absent from the truth; L38-L40 are the plain subscription, not cipher).
Control (printed and written to the truth header): match share of the f.103r stretch (decoded value == aligned letter, over
aligned keyed signs) under the published key vs 200 value-shuffled keys (seed 20261009), each re-aligned by the same DP.
Also writes benchmark-tx/outputs/vivonne1573-f103r-confirm2/{committed,passA,passB}.tsv (raw tokens, line/pos/sign):
committed = the reference sequence (home advantage, errs only on its conflicts); passA/passB = N5-VIVK's blind Sonnet passes.

    python3 benchmark-tx/build_vivonne_confirm2.py           # (re)build, print counts + control + sha256
    python3 benchmark-tx/build_vivonne_confirm2.py --check   # rebuild in memory; exit 1 if truth, sha256 or outputs are stale
    python3 benchmark-tx/build_vivonne_confirm2.py --start 6500 [--check]   # RE103 re-anchored item vivonne1573-f103r-confirm2-s6500

--start S (TX-RE103, PREREG-txeng2-20 section RE103, 10 Oct 2026; as build_vivonne_f102r.py's --start, DV1d): the f.103r stretch
alone is aligned (same DP, band 400) to the dec_norm window [S : S+W], W = 3624 = SCAN-103's window (round(1.25 x the frozen
control span), benchmark-tx/txeng2/scan103/scan.json; clipped at the end of dec_norm), S = SCAN-103's best offset, instead of
taking its stretch of the j0-anchored whole-stream alignment. Key forcing, exclusions, the flag rule and the control are
unchanged; TXV-VIV's verdicts are re-applied from the frozen item's flags file by (line, raw position), and only where the new
alignment again sets align-conflict. The item id becomes vivonne1573-f103r-confirm2-s6500 (new truth, sha256 and outputs dir);
the confirm2 item, its truth and outputs stay untouched. The build also prints the selection-fair margin: the control's
published-key share minus SCAN-103's best-over-scan null max (confirm.json best_offset_null.null_best_max).
Without --start the build is byte-identical to the frozen one.
"""
import difflib, hashlib, json, os, random, re, sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import stream_align as sa  # noqa: E402

F = os.path.join(ROOT, 'ciphers/fr16104-vivonne-spain-1572')
TX = os.path.join(F, 'tx')
OUT = os.path.join(ROOT, 'benchmark-tx')
ITEM = 'vivonne1573-f103r-confirm2'
TRUTH = os.path.join(OUT, ITEM + '.truth.tsv')
SHA = TRUTH + '.sha256'
ODIR = os.path.join(OUT, 'outputs', ITEM)
WIN, WMIN = 8, 0.5
DEC_PAGES = ('f105v', 'f106r', 'f106v', 'f107r', 'f107v', 'f108r', 'f108v')
COLS = 'line\tpos\tref_sign\ttruth\tplain\tstatus\tflag\n'
FLAGS = os.path.join(OUT, ITEM + '.flags.tsv')
START, W_START = None, 3624
if '--start' in sys.argv:
    START = int(sys.argv[sys.argv.index('--start') + 1])
    ITEM = 'vivonne1573-f103r-confirm2-s%d' % START
    TRUTH = os.path.join(OUT, ITEM + '.truth.tsv')
    SHA = TRUTH + '.sha256'
    ODIR = os.path.join(OUT, 'outputs', ITEM)


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
    i0 = next(k for k, t in enumerate(stream) if t[0] == 'f103r')
    if START is not None:  # RE103: re-anchor the f.103r stretch alone at dec_norm offset START (window W_START letters)
        let = allet[START:START + W_START]
        cmask = clerk_mask(len(allet))[START:START + W_START]
        am_seg, _ = align(seq[i0:], let, pub)
        amap = {k + i0: j for k, j in am_seg.items()}

    def ok(k):  # aligned, keyed: does the decoded value equal the aligned letter?
        return dec[k] >= 0 and k in amap and dec[k] == let[amap[k]]

    def keyed(k):
        return dec[k] >= 0 and k in amap

    # control on the f.103r stretch: real key vs 200 value-shuffled keys, each re-aligned
    sub = list(range(i0, len(stream)))
    js = [amap[k] for k in sub if k in amap]
    lo, hi = max(0, min(js) - 200), min(len(let), max(js) + 200)
    seg_seq, seg_let = seq[i0:], let[lo:hi]

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
    ctrl = ('control: f.103r match share, published key %.3f vs 200 value-shuffled keys mean %.3f p95 %.3f max %.3f, rank %d of '
            '201' % (real, sum(sh) / len(sh), sorted(sh)[189], max(sh), rank))
    if START is not None:
        nb = json.load(open(os.path.join(OUT, 'txeng2', 'scan103', 'confirm.json')))['best_offset_null']['null_best_max']
        ctrl += '; selection-fair margin %.4f (published %.4f minus SCAN-103 best-over-scan null max %.4f)' % (real - nb, real, nb)

    # TXV-VIV (9 Oct 2026): verifier verdicts on the align-conflict positions, keyed by the oo's first raw position (both raw
    # rows of a collapsed oo carry the same verdict); FLAG -> class in the flag column, CORRECT -> truth re-forced, KEEP -> cleared
    flags = {}
    fp = FLAGS
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
            nb = [j for j in range(k - WIN, k + WIN + 1) if j != k and i0 <= j < len(stream) and keyed(j)]
            if not nb or sum(1 for j in nb if ok(j)) / len(nb) < WMIN:
                st = 'excluded:align-uncertain'
            else:
                truth = '|'.join(sorted(by_val[plain]))
                fl = []
                if force[code] != plain:
                    fl.append('align-conflict')
                if not cmask[amap[k]]:
                    fl.append('clerk-split')
                fr = flags.get(('f103r_' + line, raws[0]))
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
            rows.append(('f103r_' + line, raws[0], 'o', t1, plain, st, flag))
            rows.append(('f103r_' + line, raws[1], 'o', 'o' if truth else '', plain, st, flag))
            n_add = 2
        else:
            rows.append(('f103r_' + line, raws[0], code, truth, plain, st, flag))
            n_add = 1
        nex[st] = nex.get(st, 0) + n_add
    hdr = ('# Vivonne 1573 (BnF fr.16105 f.103r, Saint-Gouard to Charles IX) confirmation item, split=confirm2: clerk period '
           'decipherment (ff.104r-108v) under the published Tomokiyo key (C rows); built by benchmark-tx/'
           'build_vivonne_confirm2.py (TX-CONFIRM-SET-2). LANE TX-ENGINEER-2 scores this ONCE, at the end.\n# %s\n' % ctrl)
    if START is not None:
        hdr = ('# Vivonne 1573 (BnF fr.16105 f.103r, Saint-Gouard to Charles IX) confirmation item confirm2-s%d, split=confirm2: '
               'clerk period decipherment (ff.104r-108v) under the published Tomokiyo key (C rows), f.103r re-anchored at dec_norm '
               'offset %d (build_vivonne_confirm2.py --start %d; TX-RE103, PREREG-txeng2-20 RE103, SCAN-103 best offset). '
               'TXV-VIV verdicts re-applied by (line, raw position).\n# %s\n' % (START, START, START, ctrl))
    body = hdr + COLS + ''.join('\t'.join(str(x) for x in r) + '\n' for r in rows)
    outs = {}
    for name, path in (('committed', 'f103r_rec.tsv'), ('passA', 'f103r_passA.tsv'), ('passB', 'f103r_passB.tsv')):
        outs[name] = 'line\tpos\tsign\n' + ''.join('f103r_%s\t%d\t%s\n' % (line, i + 1, t)
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
