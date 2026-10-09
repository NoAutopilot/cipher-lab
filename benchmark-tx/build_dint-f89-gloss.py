#!/usr/bin/env python3
"""Build BENCHMARK-TX item dint-f89-gloss (TXP-D89, LANE TX-ENGINEER-2, 9 Oct 2026; PREREG benchmark-tx/PREREG-txeng2-0.md
0b + Amendment 1; brief .claude/briefs/runs/2026-10-09-account4-txp-gloss.md).

Leaf: BnF fr.3619 f.89 (DECODE record 9440, Dinteville to Nevers, Langres, Nov 1591), DECODE copy 1600 px wide.
Reference = benchmark-tx/txeng2/dint-f89-gloss/passZ_pipeline.tsv (today's pipeline: two blind Opus passes, reconcile,
Opus adjudication of the 65 disagreements), committed before the gloss was read. Truth = the period interlinear
decipherment on the leaf (gloss.tsv: two blind Opus reads, letter-level difflib, disagreeing letters -> '?').

Alignment: tools/interlinear_align.run_align per cipher line (gloss line Lnn over passZ line f89_Lnn), the settings of
ciphers/fr3621-dinteville-1592/f128/print_align/align_print.py primary run (syl: floor 100, null_cost -1.0, max_chunk 3,
seg_bonus 0.0, len_prior 1.0, FOLD_FS False), each sign label its own code; '?' in the gloss is the wildcard (a chunk
containing it is gloss-unread). Leaf key rebuilt from the alignment: per sign, folded chunk counts; majority value,
count, agree share.
A sign is GOOD when its majority chunk is one letter with count >= 2, agree >= 0.75 and -- when the sign (under
benchmark-tx/dint128_label_map.tsv's reverse labels) is in f128/print_align/key_print.tsv -- key_print's meaning equals it.
Scored: the aligned chunk is one letter that has at least one GOOD sign; truth set = every GOOD sign with that letter
(value-level: homophones are interchangeable). passZ's sign at the position is NOT required to be in the set, so a
passZ wrong-sign position counts against passZ (the brief: passZ scores 0 on segmentation, not on identity) -- except
where passZ's sign has that letter as its own majority but is not GOOD (low agree / key_print conflict): excluded, since
the sign may be a real homophone the leaf is too short to confirm; and where passZ's sign is not GOOD but the letter
is one of its values seen >= 2 times (excluded:ambiguous-sign: the reader label covers two key signs, e.g. '4' = key_print
'4' (l) and 'D' (a) under dint128_label_map, or '1' e/i).
Dots: tools/reconcile_passes.py dropped '.' signs by default (no --keep-dots) when passZ was built, before the gloss was
read; passZ was not rebuilt after the gloss read, so the item covers non-dot signs only and the passA/passB outputs drop
their '.' rows too (39 in A, 36 in B). Excluded with a class: unaligned, gloss-unread, multi-letter,
low-count (< 2), low-agree, key-conflict, off-sheet (X_*, NEW:, ?).
Flag align-conflict on a scored position whose left or right neighbour aligned to a chunk that conflicts with that
neighbour's own majority (the alignment's local uncertainty, interlinear_align status 'conflict:*').
Control: GAPS4 statistic (share of decoded letters in difflib matching blocks >= 3 against the folded gloss), rebuilt key
vs 200 value-shuffled keys (seed 1), as build_birago152.py prints.
Outputs: benchmark-tx/dint-f89-gloss.truth.tsv (+ .sha256), benchmark-tx/outputs/dint-f89-gloss/{passA,passB,passZ_pipeline}.tsv
(passA/passB: the joined blind passes, CLEAR rows dropped).
    python3 benchmark-tx/build_dint-f89-gloss.py [--check]
"""
import csv, difflib, hashlib, os, random, re, shutil, sys, tempfile
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TX = os.path.join(ROOT, 'benchmark-tx/txeng2/dint-f89-gloss')
KP = os.path.join(ROOT, 'ciphers/fr3621-dinteville-1592/f128/print_align/key_print.tsv')
ITEM = 'dint-f89-gloss'
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import interlinear_align as ia  # noqa: E402
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import truth_variant as tv  # noqa: E402
ia.FOLD_FS = False


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def fold(s):
    s = s.lower().replace('v', 'u').replace('j', 'i').replace('y', 'i')
    return re.sub(r'[^a-z]', '', s)


def matched(dec, clear):
    sm = difflib.SequenceMatcher(None, dec, clear, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size >= 3) / max(1, len(dec))


def offsheet(s):
    return s.startswith('X_') or s.startswith('NEW:') or s == '?'


def build(out_root, variant=None):
    z = defaultdict(list)
    for r in rd(os.path.join(TX, 'passZ_pipeline.tsv')):
        z[r['line']].append(r['sign'])
    gl = {r['line']: r['text'] for r in rd(os.path.join(TX, 'gloss.tsv'))}
    codes = {}
    pairs = []
    for ln in sorted(z):
        g = gl.get(ln.split('_')[1], '')
        g = g.replace('+', '?').replace('|', '?')
        raw = ' '.join(str(codes.setdefault(s, 100 + len(codes))) for s in z[ln])
        pairs.append({'plain_line': ln, 'plain_raw': g, 'cipher_line': ln, 'cipher_raw': raw})
    inv = {str(c): s for s, c in codes.items()}
    prepared, results, counts, shown = ia.run_align(pairs, floor=100, null_cost=-1.0, max_chunk=3, seg_bonus=0.0,
                                                    len_prior=1.0, wildcard='?')
    trows = ia.token_rows(prepared, results, counts, shown)
    # leaf key from the final alignment (chunks with a wildcard are not counted, as run_align does)
    key = {}
    for v, cnt in counts.items():
        s = inv[str(v)]
        cnt = Counter({fold(k): n for k, n in cnt.items() if fold(k)})
        tot = sum(cnt.values())
        if not tot:
            continue
        top, n = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[0]
        key[s] = (top, n, tot, n / tot, cnt)
    rev = {r['to']: r['from'] for r in rd(os.path.join(ROOT, 'benchmark-tx/dint128_label_map.tsv'))}
    kp = {r['sign']: r['meaning'] for r in csv.DictReader(open(KP, newline=''), delimiter='\t')}  # not rd(): its '#' sign row is data

    def kp_of(s):
        b = s.rstrip("'")
        for lab in (s, b, rev.get(s), rev.get(b), {'+': 'plus', '-:-': 'div'}.get(b)):
            if lab and lab in kp:
                return kp[lab]
        return None

    def good(s):
        if s not in key or offsheet(s):
            return False
        top, n, tot, sh, _ = key[s]
        k = kp_of(s)
        return len(top) == 1 and n >= 2 and sh >= 0.75 and (k is None or k == top)
    by_val = defaultdict(set)
    for s in key:
        if good(s):
            by_val[key[s][0]].add(s)
    rows, nex, nsc = [], Counter(), 0
    status_of = [(r[0], r[1], r[7], r[6]) for r in trows]
    for i, r in enumerate(trows):
        ln, k, rawtok, kind, value, repair, chunk, status = r
        s = inv[rawtok]
        fc = fold(chunk)
        st, truth = 'scored', ''
        if offsheet(s):
            st = 'excluded:off-sheet'
        elif '?' in chunk:
            st = 'excluded:gloss-unread'
        elif not fc or status.startswith('null'):
            st = 'excluded:unaligned'
        elif len(fc) > 1:
            st = 'excluded:multi-letter'
        elif s in key and key[s][0] == fc and not good(s):
            st = 'excluded:low-agree' if kp_of(s) in (None, fc) else 'excluded:key-conflict'  # sign may be a real homophone
        elif s in key and not good(s) and key[s][4].get(fc, 0) >= 2:
            st = 'excluded:ambiguous-sign'  # the label covers >1 key sign or value (e.g. 4 = key_print 4 and D)
        elif by_val.get(fc):
            truth = '|'.join(sorted(by_val[fc]))  # scored: passZ's sign counts wrong when it is not in the set
        elif s not in key or key[s][2] < 2 or key[s][1] < 2:
            st = 'excluded:low-count'
        elif kp_of(s) is not None and kp_of(s) != key[s][0]:
            st = 'excluded:key-conflict'
        else:
            st = 'excluded:low-agree'  # the letter has no sign passing count >= 2, agree >= 0.75 (+ key_print) on this leaf
        flag = ''
        if st == 'scored':
            nb = [status_of[j] for j in (i - 1, i + 1) if 0 <= j < len(status_of) and status_of[j][0] == ln]
            if any(x[2].startswith('conflict') for x in nb):
                flag = 'align-conflict'
            nsc += 1
        else:
            nex[st] += 1
        rows.append((ln, k + 1, s, truth, chunk, st, flag, status))
    # control
    seq = [s for ln in sorted(z) for s in z[ln]]
    clear = fold(' '.join(gl[l] for l in sorted(gl)).replace('?', ''))
    m = {s: key[s][0] for s in key if not offsheet(s)}

    def dec(mp):
        return ''.join(mp.get(s, '') for s in seq)
    real = matched(dec(m), clear)
    ids = list(m); vv = [m[i] for i in ids]
    rng = random.Random(1); sh = []
    for _ in range(200):
        rng.shuffle(vv)
        sh.append(matched(dec(dict(zip(ids, vv))), clear))
    rank = 1 + sum(1 for x in sh if x >= real)
    agrees = sum(1 for r in trows if r[7] == 'agrees')
    nkp = [s for s in key if kp_of(s) is not None and not offsheet(s)]
    nkp_ok = sum(1 for s in nkp if kp_of(s) == key[s][0])
    ctrl = ('align agrees %d/%d = %.3f; GAPS4 control: rebuilt key matched %.3f vs 200 value-shuffled keys mean %.3f max %.3f, '
            'rank %d of 201; leaf key %d signs (%d pass count>=2 agree>=0.75 single letter), key_print overlap %d, agree %d'
            % (agrees, len(trows), agrees / len(trows), real, sum(sh) / len(sh), max(sh), rank, len(key),
               sum(1 for s in key if good(s)), len(nkp), nkp_ok))
    if variant:  # PREREG-txeng2-2 R (TXP-REBUILD): second truth from a key independent of the reads
        assert variant == 'keyprint', 'this item builds --variant keyprint only'
        return tv.write_variant(out_root, ITEM, variant, tv.keyprint_rows(trows, [(r[0], r[1], r[2]) for r in rows], lambda c: '?' in c, fold), ctrl)
    os.makedirs(os.path.join(out_root, 'benchmark-tx'), exist_ok=True)
    tp = os.path.join(out_root, 'benchmark-tx', ITEM + '.truth.tsv')
    with open(tp, 'w') as f:
        f.write('# Dinteville fr.3619 f.89 (DECODE 9440, Nov 1591) known answer: period interlinear decipherment on the leaf '
                '(two blind reads, gloss.tsv) aligned to passZ_pipeline.tsv, leaf key rebuilt (agree >= 2, share >= 0.75) + '
                'key_print check; built by benchmark-tx/build_dint-f89-gloss.py\n# %s\n'
                'line\tpos\tref_sign\ttruth\tplain\tstatus\tflag\talign_status\n' % ctrl)
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    with open(tp + '.sha256', 'w') as f:
        f.write(hashlib.sha256(open(tp, 'rb').read()).hexdigest() + '  ' + ITEM + '.truth.tsv\n')
    kpath = os.path.join(out_root, 'benchmark-tx/txeng2/dint-f89-gloss/key_leaf.tsv')
    os.makedirs(os.path.dirname(kpath), exist_ok=True)
    with open(kpath, 'w') as f:
        f.write('sign\tmeaning\tn\ttotal\tagree\tgood\tkey_print\tothers\n')
        for s in sorted(key, key=lambda s: -key[s][2]):
            top, n, tot, shr, cnt = key[s]
            f.write('%s\t%s\t%d\t%d\t%.2f\t%s\t%s\t%s\n' % (s, top, n, tot, shr, 'y' if good(s) else '',
                    kp_of(s) or '', ','.join('%s:%d' % kv for kv in cnt.most_common() if kv[0] != top)))
    od = os.path.join(out_root, 'benchmark-tx/outputs', ITEM)
    os.makedirs(od, exist_ok=True)
    for P in ('A', 'B'):
        lines = defaultdict(list)
        for r in rd(os.path.join(TX, 'pass%s.tsv' % P)):
            if r['sign_id'] not in ('CLEAR', 'NONE', '', '.'):  # dots: see the docstring
                lines[r['passage']].append(r['sign_id'])
        with open(os.path.join(od, 'pass%s.tsv' % P), 'w') as f:
            f.write('line\tpos\tsign\n')
            for ln in sorted(lines):
                for i, s in enumerate(lines[ln]):
                    f.write('f89_%s\t%d\t%s\n' % (ln, i + 1, s))
    shutil.copyfile(os.path.join(TX, 'passZ_pipeline.tsv'), os.path.join(od, 'passZ_pipeline.tsv'))
    return '%s: %d positions, %d scored, excluded %s; %s' % (ITEM, len(rows), nsc, dict(nex), ctrl)


OUTS = ['benchmark-tx/%s.truth.tsv' % ITEM, 'benchmark-tx/%s.truth.tsv.sha256' % ITEM,
        'benchmark-tx/txeng2/dint-f89-gloss/key_leaf.tsv'] + \
       ['benchmark-tx/outputs/%s/%s.tsv' % (ITEM, n) for n in ('passA', 'passB', 'passZ_pipeline')]


def main():
    if tv.variant_main(build, ITEM):  # --variant keyprint|jackknife [--check] (PREREG-txeng2-2 R)
        return
    if '--check' in sys.argv:
        tmp = tempfile.mkdtemp()
        build(tmp)
        bad = [rel for rel in OUTS if not os.path.exists(os.path.join(ROOT, rel)) or
               open(os.path.join(ROOT, rel), 'rb').read() != open(os.path.join(tmp, rel), 'rb').read()]
        shutil.rmtree(tmp)
        print('stale: ' + ', '.join(bad) if bad else 'up to date')
        sys.exit(1 if bad else 0)
    print(build(ROOT))


if __name__ == '__main__':
    main()
