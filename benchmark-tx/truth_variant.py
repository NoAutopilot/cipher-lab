#!/usr/bin/env python3
"""Second truth builds for the round-0b gloss items, from a key independent of the reads (TXP-REBUILD, LANE TX-ENGINEER-2,
9 Oct 2026; PREREG benchmark-tx/PREREG-txeng2-2.md section R). Imported by the four build scripts' `--variant` option; never
run on its own, never edits a truth file by hand.

keyprint (dint-f89/f98v/f113-gloss): S(L) = every sign whose ciphers/fr3621-dinteville-1592/f128/print_align/key_print.tsv
majority value is L with agree/n >= 0.75 and n >= 3, written in the reader vocabulary (benchmark-tx/dint128_label_map.tsv:
D -> 4, al -> a, zh -> m; plus -> +, div -> -:-), so a merged reader label sits in S(L) for every letter of its members
(reader '4' is in S(a) through D and in S(l) through 4). A primed reader label (0', v') is its own sheet cell and is not
in key_print, so never in S(L). A position is scored when its aligned gloss chunk is one letter L (no wildcard: gloss
conf not '?'), S(L) is non-empty and the alignment is not flagged uncertain; truth = S(L), whatever passZ reads there.
"Flagged uncertain" is one rule for all three leaves: a same-line neighbour (+-1) whose interlinear_align status is
conflict:* (f89's declared align-conflict rule). The position's OWN status is not used: 'conflict'/'single' there compares
the chunk with passZ's own sign's leaf majority, which would exclude passZ's misreads by construction (the round-0b flaw).

jackknife (bir1591-f23r-gloss, no outside key): line i is scored with the key rebuilt from all OTHER lines of the leaf's
alignment (per sign: wildcard-free non-empty chunks, majority one letter, n >= 2, agree >= 0.75, on-sheet); truth =
S_-i(L); same exclusion classes and neighbour rule. Grade C- (the same readers' errors on other lines still shape the key).
"""
import csv, hashlib, os
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KP = os.path.join(ROOT, 'ciphers/fr3621-dinteville-1592/f128/print_align/key_print.tsv')
LMAP = os.path.join(ROOT, 'benchmark-tx/dint128_label_map.tsv')
EXTRA = {'plus': '+', 'div': '-:-'}


def reader_label_map(path=LMAP):
    with open(path, newline='') as f:
        rows = list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))
    m = {r['from']: r['to'] for r in rows}
    m.update(EXTRA)
    return m


def kp_inverse(fold, kp_path=KP, min_n=3, min_agree=0.75):
    """letter -> set of reader labels (key_print majority value, agree/n >= min_agree, n >= min_n)."""
    lm = reader_label_map()
    S = defaultdict(set)
    with open(kp_path, newline='') as f:  # not comment-filtered: its '#' sign row is data
        for r in csv.DictReader(f, delimiter='\t'):
            n, ag = int(r['n']), int(r['agree'])
            if n >= min_n and ag / n >= min_agree:
                S[fold(r['meaning'])].add(lm.get(r['sign'], r['sign']))
    return dict(S)


def _neighbour_uncertain(trows, i):
    ln = trows[i][0]
    return any(0 <= j < len(trows) and trows[j][0] == ln and str(trows[j][7]).startswith('conflict') for j in (i - 1, i + 1))


def _base_class(chunk, status, unread, fold):
    if unread(chunk):
        return 'excluded:gloss-unread'
    if not fold(chunk) or str(status).startswith('null'):
        return 'excluded:unaligned'
    if len(fold(chunk)) > 1:
        return 'excluded:multi-letter'
    return None


def keyprint_rows(trows, keys, unread, fold):
    """trows: interlinear_align.token_rows; keys: [(line, pos, passZ sign)] in the same order (the default build's rows)."""
    S = kp_inverse(fold)
    out = []
    for i, (t, (ln, pos, sign)) in enumerate(zip(trows, keys)):
        chunk, status = t[6], t[7]
        st, truth = _base_class(chunk, status, unread, fold), ''
        if st is None:
            L = fold(chunk)
            if not S.get(L):
                st = 'excluded:letter-no-keyprint-sign'
            elif _neighbour_uncertain(trows, i):
                st = 'excluded:align-uncertain'
            else:
                st, truth = 'scored', '|'.join(sorted(S[L]))
        out.append((ln, pos, sign, truth, chunk, st, '', status))
    return out


def jackknife_rows(trows, keys, unread, fold, offsheet, min_n=2, min_agree=0.75):
    per_line = defaultdict(lambda: defaultdict(Counter))
    for t, (ln, pos, sign) in zip(trows, keys):
        ch = t[6]
        if unread(ch) or str(t[7]).startswith('null') or not fold(ch):
            continue
        per_line[ln][sign][fold(ch)] += 1
    lines = sorted(per_line)
    S_minus = {}
    for li in set(k[0] for k in keys):
        tot = defaultdict(Counter)
        for lj in lines:
            if lj != li:
                for s, c in per_line[lj].items():
                    tot[s].update(c)
        S = defaultdict(set)
        for s, c in tot.items():
            if offsheet(s):
                continue
            top, n = sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))[0]
            N = sum(c.values())
            if len(top) == 1 and N >= min_n and n / N >= min_agree:
                S[top].add(s)
        S_minus[li] = S
    out = []
    for i, (t, (ln, pos, sign)) in enumerate(zip(trows, keys)):
        chunk, status = t[6], t[7]
        st, truth = _base_class(chunk, status, unread, fold), ''
        if st is None:
            L = fold(chunk)
            if not S_minus[ln].get(L):
                st = 'excluded:letter-no-jackknife-sign'
            elif _neighbour_uncertain(trows, i):
                st = 'excluded:align-uncertain'
            else:
                st, truth = 'scored', '|'.join(sorted(S_minus[ln][L]))
        out.append((ln, pos, sign, truth, chunk, st, '', status))
    return out


def write_variant(out_root, item, variant, rows, header):
    tp = os.path.join(out_root, 'benchmark-tx', '%s.truth.%s.tsv' % (item, variant))
    os.makedirs(os.path.dirname(tp), exist_ok=True)
    sc = sum(1 for r in rows if r[5] == 'scored')
    ex = Counter(r[5] for r in rows if r[5] != 'scored')
    with open(tp, 'w') as f:
        f.write('# %s\n# variant %s (benchmark-tx/truth_variant.py, PREREG-txeng2-2 R): %d positions, %d scored, excluded %s\n'
                'line\tpos\tref_sign\ttruth\tplain\tstatus\tflag\talign_status\n' % (header, variant, len(rows), sc, dict(ex)))
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    with open(tp + '.sha256', 'w') as f:
        f.write(hashlib.sha256(open(tp, 'rb').read()).hexdigest() + '  ' + os.path.basename(tp) + '\n')
    return '%s %s: %d positions, %d scored, excluded %s' % (item, variant, len(rows), sc, dict(ex))


def variant_rels(item, variant):
    return ['benchmark-tx/%s.truth.%s.tsv' % (item, variant), 'benchmark-tx/%s.truth.%s.tsv.sha256' % (item, variant)]


def variant_main(build, item, root=ROOT):
    """`--variant NAME [--check]` in a build script's main(); returns False when no --variant was given."""
    import shutil, sys, tempfile
    if '--variant' not in sys.argv:
        return False
    v = sys.argv[sys.argv.index('--variant') + 1]
    if '--check' in sys.argv:
        tmp = tempfile.mkdtemp()
        build(tmp, v)
        bad = [rel for rel in variant_rels(item, v) if not os.path.exists(os.path.join(root, rel)) or
               open(os.path.join(root, rel), 'rb').read() != open(os.path.join(tmp, rel), 'rb').read()]
        shutil.rmtree(tmp)
        print('stale: ' + ', '.join(bad) if bad else 'up to date')
        sys.exit(1 if bad else 0)
    print(build(root, v))
    return True
