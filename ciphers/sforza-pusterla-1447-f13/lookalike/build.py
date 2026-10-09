#!/usr/bin/env python3
"""SFZ-LOOK (9 Oct 2026): adapter from f.13's wide passes to tools/lookalike_pass.py's long formats, for the look-alike
pass on the named pairs T=/b-, d/g, q/V (NOTES.md Remaining gaps, gap 2).

Reference sequence ("passC" in the tool's sense) = ciphertext_f13_passC.tsv, the blind Sonnet read of the level crops in
images/level/ (the crops the windows are cut from). Reader A = pass A (SFZ-P, Opus); reader "B" in the tool's columns = pass
C's own label, so that the tool's 2-of-3 rule reads: a firm re-read that matches pass A or pass C settles the tile. Pass B
(two-line crops, drifting line breaks, 61% A-B disagreement) is kept as a column for the record only and never settles a tile.
Normalisation (lattice_decode.py's rule): `g ÷` is one sign `g÷`; a pass-C token `x/y?` is label x, alternative y, conf M;
a trailing `?` gives conf M.

Pre-registered before any re-read (SFZ-LOOK, 9 Oct 2026, ~14:0x UTC):
  * target tiles: every C position whose aligned A label differs from C's label (or from C's alternative) and where the
    pair {A, C} (or {C, C-alt}) is one of {T=,b-}, {d,g}, {q,V}, {q=,V} (the brief's q/V pair; on f.13 the realised
    A-C swap is V/q=, 4 times, so q= is included -- amended before any re-read); candidates = the pair's two labels plus any other label
    A or C gave there;
  * control tiles (matched: same pairs, same windows, same prompt, not marked): positions where A and C carry the same
    label (conf H, no alternative) from {T=, b-, d, g, q, q=, V}, up to 3 per label (pass B ignored: it is the outlier), seeded (seed 7); candidates = that label and its pair partner;
  * control gate: the re-read reproduces the three-reader label on >= 0.80 of control tiles at conf H/M, else the re-read
    is a non-test and no label changes;
  * the lattice decode + judge are rerun only if a target tile's label changes under the tool's reconcile rule.
  python3 ciphers/sforza-pusterla-1447-f13/lookalike/build.py
Writes lookalike/{passC.tsv,agreement.tsv,tiles_target.tsv,tiles_all.tsv,confusion_f13.tsv} and prints counts.
"""
import csv, collections, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TGT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(TGT, '..', '..', 'tools'))
from lookalike_pass import _align  # noqa: E402

PAIRS = [frozenset(p) for p in (('T=', 'b-'), ('d', 'g'), ('q', 'V'), ('q=', 'V'))]
PARTNER = {'T=': 'b-', 'b-': 'T=', 'd': 'g', 'g': 'd', 'q': 'V', 'V': 'q', 'q=': 'V'}


def load(fn):
    out = collections.OrderedDict()
    for l in open(os.path.join(TGT, fn)):
        if l.startswith('#') or '\t' not in l:
            continue
        ln, s = l.rstrip('\n').split('\t', 1)
        toks, i, raw = [], 0, s.split()
        while i < len(raw):
            t = raw[i]
            if t.rstrip('?') == 'g' and i + 1 < len(raw) and raw[i + 1].rstrip('?') == '÷':
                t = 'g÷' + ('?' if raw[i].endswith('?') or raw[i + 1].endswith('?') else ''); i += 1
            conf = 'M' if t.endswith('?') else 'H'
            t = t.rstrip('?')
            lab, alt = (t.split('/', 1) + [''])[:2]
            toks.append((lab, alt, conf)); i += 1
        out[ln] = toks
    return out


def main():
    A, B, C = (load(f'ciphertext_f13_pass{x}.tsv') for x in 'ABC')
    ag, pc, tiles, ctrl_pool = [], [], [], collections.defaultdict(list)
    conf_cnt = collections.Counter()
    for ln, toks in C.items():
        if ln == 'f13_SIG':
            continue
        ref = [t[0] for t in toks]
        a = _align(ref, [t[0] for t in A.get(ln, [])])
        b = _align(ref, [t[0] for t in B.get(ln, [])])
        for i, ((lab, alt, cf), x, y) in enumerate(zip(toks, a, b), 1):
            pc.append(dict(passage=ln, pos=i, sign_id=lab, conf=cf))
            st = 'agree' if x == lab else ('split-gap' if x is None else 'split')
            if x and x != lab:
                conf_cnt[tuple(sorted((x, lab)))] += 1
            ag.append(dict(passage=ln, posA=i, idA=x or '', idC=lab, altC=alt, idB_record=y or '', status=st))
            ctx_b = ' '.join(t[0] for t in toks[max(0, i - 4):i - 1]); ctx_a = ' '.join(t[0] for t in toks[i:i + 3])
            labs = {l for l in (x, lab, alt) if l}
            hit = [p for p in PAIRS if (x and frozenset((x, lab)) == p) or (alt and frozenset((lab, alt)) == p)]
            if hit:
                cand = sorted(set(hit[0]) | labs)
                tiles.append(dict(run='sfzlook', passage=ln, pos=i, passC=lab, A=x or '', B=lab, status='split',
                                  why='split', kind='target', candidates=','.join(cand), before=ctx_b, after=ctx_a,
                                  passB_record=y or '', altC=alt))
            elif x == lab and lab in PARTNER and cf == 'H' and not alt:
                ctrl_pool[lab].append(dict(run='sfzlook', passage=ln, pos=i, passC=lab, A=x, B=lab, status='split',
                                           why='control', kind='control', candidates=','.join(sorted((lab, PARTNER[lab]))),
                                           before=ctx_b, after=ctx_a, passB_record=y, altC=alt))
    rnd = random.Random(7)
    ctrl = []
    for lab in sorted(ctrl_pool):
        ctrl += rnd.sample(ctrl_pool[lab], min(3, len(ctrl_pool[lab])))
    allt = tiles + ctrl
    rnd.shuffle(allt)   # interleave so position in the montage never marks a control
    def w(name, rows):
        with open(os.path.join(HERE, name), 'w', newline='') as o:
            d = csv.DictWriter(o, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n'); d.writeheader(); d.writerows(rows)
    w('passC.tsv', pc); w('agreement.tsv', ag); w('tiles_target.tsv', tiles); w('tiles_all.tsv', allt)
    w('confusion_f13.tsv', [dict(label_a=k[0], label_b=k[1], n=n) for k, n in conf_cnt.most_common()])
    print(f'signs {len(pc)}; A-C split {sum(r["status"]=="split" for r in ag)}, gap {sum(r["status"]=="split-gap" for r in ag)}; '
          f'target tiles {len(tiles)} ({collections.Counter(min(t["candidates"].split(","), key=len) for t in tiles)}); '
          f'control tiles {len(ctrl)} {dict(collections.Counter(c["passC"] for c in ctrl))}')
    print('top A-C confusions:', conf_cnt.most_common(12))


if __name__ == '__main__':
    main()
