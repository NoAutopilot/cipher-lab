#!/usr/bin/env python3
"""TXV-GROEN (PREREG-txeng2-21 section WIT-FLAGS, 10 Oct 2026; verifier, LANE TX-ENGINEER-2 account-4): the f.103r closing
stretch's clerk-split flags checked against Groen van Prinsterer IV pp.90*-91* (IA archivesoucorre03housgoog), a printed copy
independent of the clerk decipherment.

Inputs: the on-disk IA OCR (pulled and normalised exactly as ../witanchor/wit_groen.py: same regex, same fold, the p.90* clean
part and the p.91* damaged part kept apart); ciphers/fr16104-vivonne-spain-1572/tx/dec_norm.txt (merged clerk reading) and the
two blind clerk reads tx/dec_<page>_passA/passB.txt (the build's clerk_mask inputs; merge_dec.norm per word); the --offsets dump
of the frozen item (benchmark-tx/txeng2/witflags/offsets.tsv: line, pos, dec_offset, status, flag). Opens no reader pass of
f.103r, no crop, no cipher sign.

Alignment: each part's best window over dec_norm by wit_groen's best() (step 10, refined at step 1); must agree within 5 letters
with WIT-GROEN's offsets (clean 8937, damaged 9270) else STOP. Evidence: difflib matching blocks of length >= 4 between the part
and dec_norm[o:o+L]; a letter outside a block is NO-EVIDENCE. Comparison in wit_groen's fold (v->u, j->i, y->i, k->c).
Verdicts, for every scored position with dec_offset in 8937-9459 whose flag carries clerk-split: witness == merged clerk letter
-> CONFIRM; == the other blind clerk read's letter there -> CONFLICT; else NO-EVIDENCE. (Under the block-only evidence rule a
witness letter inside a block equals dec_norm's letter by construction, so CONFLICT cannot occur; recorded, not changed.)
A position covered by both parts (overlap 9270-9307) is CONFIRM if either part confirms; part = the confirming part (clean
first), else the part whose window holds it (clean first).

Controls, run and written before any verdict file: (a) ceiling = share of the window's clerk-agreed scored positions (flag
without clerk-split) with witness == clerk inside a block; (b) selection-fair null = 200 letter-shuffled copies of the clean
part and 50 of the damaged (seed 20261010, as wit_groen), each at its own best window over dec_norm by the same best() (step 20,
as wit_groen's null), the same CONFIRM rule at the same clerk-split positions -> CONFIRM counts. Declared before the run: the
null max used by the gate is the conservative clean null max + damaged null max (a combined count can never exceed it); the
paired combined distribution (clean i + damaged i mod 50) is reported beside it. Gate: INFORMATIVE iff real CONFIRM count >
null max AND ceiling >= 0.60; else NON-TEST (the witness file is still written, the build is not run with it).

Run from the repo root: python3 -I benchmark-tx/txeng2/witflags/wit_flags.py
Writes: benchmark-tx/txeng2/witflags/controls.json (first), benchmark-tx/vivonne1573-f103r-confirm2.witness.tsv,
benchmark-tx/txeng2/witflags/ceiling.tsv, benchmark-tx/txeng2/witflags/result.json.
"""
import difflib, gzip, json, os, random, re, sys, unicodedata
from multiprocessing import Pool

ROOT = os.getcwd()
HERE = os.path.join(ROOT, 'benchmark-tx/txeng2/witflags')
TX = os.path.join(ROOT, 'ciphers/fr16104-vivonne-spain-1572/tx')
DEC_PAGES = ('f105v', 'f106r', 'f106v', 'f107r', 'f107v', 'f108r', 'f108v')
WLO, WHI = 8937, 9459
PRIOR = {'p90_clean': 8937, 'p91_damaged': 9270}
FOLD = str.maketrans('vjyk', 'uiic')


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isascii() and c.isalpha())
    return s.translate(FOLD)


ocr = gzip.open('sources/ia-fulltext/print-check/archivesoucorre03housgoog_djvu.txt.gz', 'rt', encoding='utf-8', errors='replace').read()
m1 = re.search(r"L.Empereur\s+fait\s+asseur", ocr); assert m1
m2 = re.search(r"rem[ée]dier\s+ses\s+af\S*aires", ocr[m1.start():]); assert m2
raw = ocr[m1.start():m1.start() + m2.end()]
parts = re.split(r"\n\s*[—-]\s*9\S*\s*[—-]\s*\n", raw)
if len(parts) != 2:
    parts = [raw[:raw.find('Siegcn')], raw[raw.find('Siegcn'):]]
SEGS = [norm(x) for x in parts]
DEC_RAW = ''.join(c for c in open(os.path.join(TX, 'dec_norm.txt'), encoding='utf-8').read().lower() if 'a' <= c <= 'z')
DEC = norm(open(os.path.join(TX, 'dec_norm.txt'), encoding='utf-8').read())
assert len(DEC) == len(DEC_RAW) == 9554 and DEC == DEC_RAW.translate(FOLD)


def best(seq, step=10):
    L = len(seq); bestr, besto = -1.0, None
    for o in range(0, max(1, len(DEC) - L + 1), step):
        r = difflib.SequenceMatcher(None, seq, DEC[o:o + L], autojunk=False).ratio()
        if r > bestr: bestr, besto = r, o
    for o in range(max(0, besto - step), min(len(DEC) - L, besto + step) + 1):
        r = difflib.SequenceMatcher(None, seq, DEC[o:o + L], autojunk=False).ratio()
        if r > bestr: bestr, besto = r, o
    return bestr, besto


def evidence(seq, o):
    """{dec offset: witness letter} for letters inside matching blocks of length >= 4."""
    ev = {}
    for a, b, size in difflib.SequenceMatcher(None, seq, DEC[o:o + len(seq)], autojunk=False).get_matching_blocks():
        if size >= 4:
            for t in range(size):
                ev[o + b + t] = seq[a + t]
    return ev


def pass_letters(q):
    """Per dec_norm offset, the letter one blind clerk read (passA / passB) has there: the pass's words normalised by
    merge_dec.norm, concatenated over the pages, aligned to dec_norm by difflib; equal runs and equal-length replace runs map
    one-to-one, anything else is ''."""
    sys.path.insert(0, TX)
    import merge_dec as md
    txt = ''
    for p in DEC_PAGES:
        ls = [l for l in open(os.path.join(TX, 'dec_%s_%s.txt' % (p, q)), encoding='utf-8').read().splitlines() if l.strip()]
        txt += ''.join(md.norm(w) for w in ' \n '.join(ls).split(' ') if w)
    out = [''] * len(DEC_RAW)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, txt, DEC_RAW, autojunk=False).get_opcodes():
        if op == 'equal' or (op == 'replace' and i2 - i1 == j2 - j1):
            for t in range(j2 - j1):
                out[j1 + t] = txt[i1 + t]
    return out


def null_one(args):
    k, seed_seq = args
    o = best(seed_seq, step=20)[1]
    return k, o, evidence(seed_seq, o)


def main():
    offs = [l.rstrip('\n').split('\t') for l in open(os.path.join(HERE, 'offsets.tsv'), encoding='utf-8')][1:]
    win = [r for r in offs if r[3] == 'scored' and r[2] and WLO <= int(r[2]) <= WHI]
    split = [r for r in win if 'clerk-split' in r[4]]
    agreed = [r for r in win if 'clerk-split' not in r[4]]
    labels = ['p90_clean', 'p91_damaged']
    al = {}
    for lab, s in zip(labels, SEGS):
        r, o = best(s)
        if abs(o - PRIOR[lab]) > 5:
            print('STOP: %s re-derived offset %d vs WIT-GROEN %d' % (lab, o, PRIOR[lab])); sys.exit(2)
        al[lab] = {'ratio': round(r, 4), 'offset': o, 'end': o + len(s), 'letters': len(s), 'ev': evidence(s, o)}
    ev_c, ev_d = al['p90_clean']['ev'], al['p91_damaged']['ev']

    def confirm(off, ec, ed):
        c = DEC[off]
        return ec.get(off) == c or ed.get(off) == c

    # (a) ceiling on clerk-agreed scored positions
    ceil_hits = [r for r in agreed if confirm(int(r[2]), ev_c, ev_d)]
    ceiling = len(ceil_hits) / max(1, len(agreed))
    # (b) selection-fair null
    rng = random.Random(20261010)
    jobs = []
    for k, (lab, s) in enumerate(zip(labels, SEGS)):
        for i in range(200 if k == 0 else 50):
            sh = list(s); rng.shuffle(sh); jobs.append((lab, ''.join(sh)))
    with Pool(4) as pool:
        res = pool.map(null_one, jobs, chunksize=5)
    split_offs = [int(r[2]) for r in split]
    nc = [sum(1 for off in split_offs if ev.get(off) == DEC[off]) for lab, o, ev in res if lab == 'p90_clean']
    nd = [sum(1 for off in split_offs if ev.get(off) == DEC[off]) for lab, o, ev in res if lab == 'p91_damaged']
    paired = sorted(nc[i] + nd[i % len(nd)] for i in range(len(nc)))
    q = lambda xs: sorted(xs)[int(0.95 * len(xs)) - 1]
    null_max = max(nc) + max(nd)
    controls = {'section': 'PREREG-txeng2-21 WIT-FLAGS', 'window': [WLO, WHI], 'scored_in_window': len(win),
                'clerk_split_in_window': len(split), 'clerk_agreed_in_window': len(agreed),
                'alignment': {k: {x: v[x] for x in ('ratio', 'offset', 'end', 'letters')} for k, v in al.items()},
                'ceiling': {'hits': len(ceil_hits), 'of': len(agreed), 'share': round(ceiling, 4)},
                'null': {'clean_n': len(nc), 'clean_max': max(nc), 'clean_p95': q(nc), 'clean_mean': round(sum(nc) / len(nc), 3),
                         'damaged_n': len(nd), 'damaged_max': max(nd), 'damaged_p95': q(nd),
                         'damaged_mean': round(sum(nd) / len(nd), 3),
                         'paired_max': paired[-1], 'paired_p95': q(paired), 'gate_null_max': null_max}}
    json.dump(controls, open(os.path.join(HERE, 'controls.json'), 'w'), indent=1)
    print('controls written: ceiling %d/%d = %.4f; null clean max %d p95 %d, damaged max %d p95 %d, gate null max %d' % (
        len(ceil_hits), len(agreed), ceiling, max(nc), q(nc), max(nd), q(nd), null_max))

    pa, pb = pass_letters('passA'), pass_letters('passB')

    def row(r):
        off = int(r[2])
        c = DEC[off]
        oth = {x.translate(FOLD) for x in (pa[off], pb[off]) if x and x.translate(FOLD) != c}
        part = 'clean' if ev_c.get(off) == c else 'damaged' if ev_d.get(off) == c else (
            'clean' if off in ev_c or al['p90_clean']['offset'] <= off < al['p90_clean']['end'] else 'damaged')
        w = ev_c.get(off) if part == 'clean' else ev_d.get(off)
        if w is not None and w == c:
            v, why = 'CONFIRM', 'witness letter equals the merged clerk letter inside a matching block >= 4 (%s part)' % part
        elif w is not None and w in oth:
            v, why = 'CONFLICT', 'witness letter equals the other blind clerk read'
        else:
            v, why = 'NO-EVIDENCE', 'outside every matching block of length >= 4'
        return [r[0], r[1], r[2], DEC_RAW[off], pa[off] or '-', pb[off] or '-', w or '-', part, v, why]
    cols = 'line\tpos\tdec_offset\tclerk_letter\tpassA_letter\tpassB_letter\twitness_letter\tpart\tverdict\treason\n'
    vrows = [row(r) for r in split]
    head = ('# TXV-GROEN witness verdicts (PREREG-txeng2-21 section WIT-FLAGS, 10 Oct 2026; verifier session, LANE TX-ENGINEER-2 '
            'account-4): every scored position of vivonne1573-f103r-confirm2 with dec_offset in %d-%d whose flag carries clerk-split, '
            'checked against Groen van Prinsterer IV pp.90*-91* (IA archivesoucorre03housgoog; a manuscript copy independent of the '
            'clerk decipherment), benchmark-tx/txeng2/witflags/wit_flags.py. Evidence: difflib matching blocks >= 4 only. Applied '
            'by build_vivonne_confirm2.py --witness only when the declared gate says INFORMATIVE (see txeng2/witflags/RESULTS.md).\n'
            % (WLO, WHI))
    open(os.path.join(ROOT, 'benchmark-tx/vivonne1573-f103r-confirm2.witness.tsv'), 'w', encoding='utf-8').write(
        head + cols + ''.join('\t'.join(x) + '\n' for x in vrows))
    crows = [row(r) for r in agreed]
    open(os.path.join(HERE, 'ceiling.tsv'), 'w', encoding='utf-8').write(
        '# ceiling table (clerk-AGREED scored positions in the window; never verdicts, never applied)\n' + cols
        + ''.join('\t'.join(x) + '\n' for x in crows))
    cnt = {}
    for x in vrows:
        cnt.setdefault(x[7], {}).setdefault(x[8], 0); cnt[x[7]][x[8]] += 1
    real = sum(1 for x in vrows if x[8] == 'CONFIRM')
    verdict = 'INFORMATIVE' if (real > null_max and ceiling >= 0.60) else 'NON-TEST'
    out = dict(controls, verdicts_by_part=cnt, confirm=real, conflict=sum(1 for x in vrows if x[8] == 'CONFLICT'),
               no_evidence=sum(1 for x in vrows if x[8] == 'NO-EVIDENCE'), gate=verdict)
    json.dump(out, open(os.path.join(HERE, 'result.json'), 'w'), indent=1)
    print('verdicts by part:', cnt)
    print('CONFIRM %d vs gate null max %d; ceiling %.4f -> %s' % (real, null_max, ceiling, verdict))


if __name__ == '__main__':
    main()
