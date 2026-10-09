#!/usr/bin/env python3
"""Build benchmark item dint-f98v-gloss for BENCHMARK-TX.tsv (TXP-D98, LANE TX-ENGINEER-2, 9 Oct 2026).

Leaf: BnF fr.3619 f.98v (DECODE 9441 page 2), Dinteville to Nevers, Langres, Nov 1591; six cipher lines with a period
interlinear decipherment (gloss) written above them. Brief: .claude/briefs/runs/2026-10-09-account4-txp-gloss.md (recipe
of benchmark-tx/build_dint128.py and f128/print_align/align_print.py).

Reference = benchmark-tx/txeng2/dint-f98v-gloss/passZ_pipeline.tsv (2 blind Opus passes, reconcile, 1 Sonnet
adjudication; committed before the gloss was read). Plain side = gloss.tsv (2 blind Opus gloss reads, reconciled), per
line: struck [..] words and *clear words dropped, '+', '|' and '?' turned into the wildcard '.', j -> i, v -> u by fold.
Alignment: tools/interlinear_align.run_align with align_print.py's syl settings (floor 100, null_cost -1, max_chunk 3,
seg_bonus 0, len_prior 1) plus wildcard '.' and, as a stated deviation, key_print.tsv as the EM prior (weight = its
agree count; unseeded: align agrees 50/246, GAPS4 rank 25/201, 0 scored), so the key_print check is partly circular; one pair per cipher line; reference labels coded 100+k (NEW:* each its code).
Key rebuilt from this leaf: per sign, the single-letter chunks it aligned to: majority letter, count, agree share.
A sign is GATED when its majority count >= 2, agree >= 0.75 and, where its label maps to key_print.tsv rows (reader
labels '+' -> plus, '-:-' -> div, 'a' -> a|al, '4' -> 4|D, else same), at least one mapped row reads the same letter.
A position is SCORED when its aligned chunk is one letter that some gated sign reads; truth = every gated sign reading that
letter (a homophone set). Stated deviation from the brief's literal rule ("that letter is the reference sign's majority
value", which makes the reference score 0 on identity by construction): a scored position whose reference sign is itself
gated to ANOTHER letter stays scored (flag ref-off-key; the reference is wrong there unless the decipherer slipped); a
reference sign that is NOT gated at a position excludes it (low-agree / n<2 / key-conflict / off-sheet), so a sign the leaf
cannot pin is never charged. The literal-rule figure = drop the ref-off-key rows; RESULTS.md prints both.
G03's first two words are dropped (left of the cipher run, over no sign).
Excluded classes: gloss-unread (wildcard in chunk), unaligned, multi-letter, letter-no-gated-sign, off-sheet (NEW:/?),
low-agree, n<2, key-conflict. Flag align-conflict where interlinear_align's own status is conflict/single.
Control: GAPS4 statistic (share of decoded letters in difflib blocks >= 3 against the folded gloss), rebuilt key vs 200
value-shuffled keys (seed 1).
Writes benchmark-tx/dint-f98v-gloss.truth.tsv (+ .sha256), txeng2/dint-f98v-gloss/key_f98v.tsv and
benchmark-tx/outputs/dint-f98v-gloss/{passA,passB,passZ_pipeline}.tsv (line ids f98v_L01..L06, positions renumbered 1..n).
  python3 benchmark-tx/build_dint-f98v-gloss.py [--check]
"""
import csv, difflib, hashlib, os, random, re, shutil, sys, tempfile
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TX = os.path.join(ROOT, 'benchmark-tx/txeng2/dint-f98v-gloss')
KP = os.path.join(ROOT, 'ciphers/fr3621-dinteville-1592/f128/print_align/key_print.tsv')
ITEM = 'dint-f98v-gloss'
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import interlinear_align as ia  # noqa: E402
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import truth_variant as tv  # noqa: E402
ia.FOLD_FS = False
KPMAP = {'+': ['plus'], '-:-': ['div'], 'a': ['a', 'al'], '4': ['4', 'D']}


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def fold(s):
    s = s.lower().replace('v', 'u').replace('j', 'i').replace('&', 'et')
    return re.sub(r'[^a-z]', '', s)


def gloss_plain(t):
    t = re.sub(r'\[[^\]]*\]', ' ', t)
    ws = [w for w in t.split() if not w.startswith('*')]
    return ' '.join(re.sub(r'[+|?]', '.', w).replace('j', 'i') for w in ws)


def matched(dec, clear):
    sm = difflib.SequenceMatcher(None, dec, clear, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size >= 3) / max(1, len(dec))


def build(out_root, variant=None):
    ref = defaultdict(list)
    for r in rd(os.path.join(TX, 'passZ_pipeline.tsv')):
        ref[r['line']].append(r['sign'])
    gl = {'f98v_L' + r['line'][1:]: gloss_plain(r['text']) for r in rd(os.path.join(TX, 'gloss.tsv'))}
    # G03's first two words ('?e Suoillem') stand LEFT of L03's first cipher sign (region x < 300 on the deskewed source,
    # checked on the overlay): a name written beside the run, over no sign; dropped here by rule, never by editing gloss.tsv.
    gl['f98v_L03'] = ' '.join(gl['f98v_L03'].split()[2:])
    codes = {}
    pairs = []
    for ln in sorted(ref):
        raw = ' '.join(str(codes.setdefault(s, 100 + len(codes))) for s in ref[ln])
        pairs.append({'plain_line': ln, 'plain_raw': gl.get(ln, ''), 'cipher_line': ln, 'cipher_raw': raw})
    inv = {c: s for s, c in codes.items()}
    # prior = key_print.tsv through KPMAP, weight = its agree count (stated deviation: the unseeded run never converged on
    # this leaf -- align agrees 50/246, GAPS4 rank 25 of 201 -- while key_print's decode visibly tracks the gloss)
    kpr = {r['sign']: r for r in rd(KP)}
    prior = {}
    for s_, c_ in codes.items():
        for m_ in KPMAP.get(s_, [s_]):
            if m_ in kpr:
                prior.setdefault(c_, Counter())[kpr[m_]['meaning']] += int(kpr[m_]['agree'])
    prep, results, counts, shown = ia.run_align(pairs, floor=100, null_cost=-1.0, max_chunk=3, seg_bonus=0.0,
                                                 len_prior=1.0, wildcard='.', prior=prior)
    trows = ia.token_rows(prep, results, counts, shown)
    assert len(trows) == sum(len(v) for v in ref.values())
    agrees = sum(1 for t in trows if t[7] == 'agrees')
    # key rebuild: single-letter, wildcard-free chunks per sign
    one = defaultdict(Counter)
    for t in trows:
        ch = t[6]
        if len(ch) == 1 and ch != '.':
            one[inv[int(t[4])]][fold(ch) or ch] += 1
    kp = {r['sign']: r['meaning'] for r in rd(KP)}
    key, gated = {}, {}
    for s, cnt in one.items():
        top, n = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[0]
        tot = sum(cnt.values())
        mapped = [m for m in KPMAP.get(s, [s]) if m in kp]
        kpv = '|'.join('%s=%s' % (m, kp[m]) for m in mapped)
        kpok = (not mapped) or any(kp[m] == top for m in mapped)
        offsheet = s.startswith('NEW:') or s == '?'
        why = ('off-sheet' if offsheet else 'n<2' if n < 2 else 'low-agree' if n / tot < 0.75 else
               'key-conflict' if not kpok else 'gated')
        key[s] = (top, tot, n, n / tot, kpv, why, cnt)
        if why == 'gated':
            gated[s] = top
    by_letter = defaultdict(set)
    for s, v in gated.items():
        by_letter[v].add(s)
    # control
    clear = fold(' '.join(gl.get(ln, '').replace('.', '') for ln in sorted(ref)))
    seq = [s for ln in sorted(ref) for s in ref[ln]]
    m = {s: k[0] for s, k in key.items()}

    def dec(mp):
        return ''.join(mp.get(s, '') for s in seq)
    real = matched(dec(m), clear)
    ids = list(m); vv = [m[i] for i in ids]; rng = random.Random(1); sh = []
    for _ in range(200):
        rng.shuffle(vv); sh.append(matched(dec(dict(zip(ids, vv))), clear))
    rank = 1 + sum(1 for x in sh if x >= real)
    ctrl = ('align agrees %d/%d = %.3f; GAPS4 control: rebuilt key matched %.3f vs 200 value-shuffled keys mean %.3f max %.3f, '
            'rank %d of 201' % (agrees, len(trows), agrees / len(trows), real, sum(sh) / len(sh), max(sh), rank))
    rows, nsc, nex, off = [], 0, Counter(), 0
    pos = Counter()
    for t in trows:
        ln, sign, ch, ast = t[0], inv[int(t[4])], t[6], t[7]
        pos[ln] += 1
        st, truth, flag = 'scored', '', ''
        if '.' in ch:
            st = 'excluded:gloss-unread'
        elif not ch:
            st = 'excluded:unaligned'
        elif len(ch) > 1:
            st = 'excluded:multi-letter'
        elif sign.startswith('NEW:') or sign == '?':
            st = 'excluded:off-sheet'
        elif sign not in gated:
            st = 'excluded:' + key[sign][5]
        elif not by_letter.get(fold(ch)):
            st = 'excluded:letter-no-gated-sign'
        else:
            truth = '|'.join(sorted(by_letter[fold(ch)]))
            if gated[sign] != fold(ch):
                flag = 'ref-off-key'; off += 1
            elif ast.startswith('conflict') or ast == 'single':
                flag = 'align-conflict'
        if st == 'scored':
            nsc += 1
        else:
            nex[st] += 1
        rows.append((ln, pos[ln], sign, truth, ch, st, flag, ast))
    if variant:  # PREREG-txeng2-2 R (TXP-REBUILD): second truth from a key independent of the reads
        assert variant in ('keyprint', 'kp2'), 'this item builds --variant keyprint|kp2 only'
        return tv.write_variant(out_root, ITEM, variant, tv.keyprint_rows(trows, [(r[0], r[1], r[2]) for r in rows], lambda c: '.' in c, fold, variant), ctrl)
    os.makedirs(os.path.join(out_root, 'benchmark-tx'), exist_ok=True)
    tp = os.path.join(out_root, 'benchmark-tx', ITEM + '.truth.tsv')
    with open(tp, 'w') as f:
        f.write('# dint-f98v-gloss: fr.3619 f.98v passZ_pipeline vs the period interlinear decipherment on the leaf (DECODE 9441 P2), '
                'key rebuilt from this leaf at count>=2 agree>=0.75 + key_print check; built by benchmark-tx/build_dint-f98v-gloss.py\n'
                '# %s; scored %d of which ref-off-key %d\nline\tpos\tref_sign\ttruth\tplain\tstatus\tflag\talign_status\n' % (ctrl, nsc, off))
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    with open(tp + '.sha256', 'w') as f:
        f.write(hashlib.sha256(open(tp, 'rb').read()).hexdigest() + '  ' + ITEM + '.truth.tsv\n')
    kd = os.path.join(out_root, 'benchmark-tx/txeng2/dint-f98v-gloss')
    os.makedirs(kd, exist_ok=True)
    with open(os.path.join(kd, 'key_f98v.tsv'), 'w') as f:
        f.write('sign\tmeaning\tn\tcount\tagree\tkey_print\tstatus\tothers\n')
        for s in sorted(key):
            top, tot, n, ag, kpv, why, cnt = key[s]
            rest = ','.join('%s:%d' % kv for kv in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[1:])
            f.write('%s\t%s\t%d\t%d\t%.2f\t%s\t%s\t%s\n' % (s, top, tot, n, ag, kpv, why, rest))
    od = os.path.join(out_root, 'benchmark-tx/outputs', ITEM)
    os.makedirs(od, exist_ok=True)
    for name in ('passA', 'passB', 'passZ_pipeline'):
        seqs = defaultdict(list)
        for r in rd(os.path.join(TX, name + '.tsv')):
            ln = r.get('line') or 'f98v_' + r['passage']
            seqs[ln].append((r.get('sign') or r.get('sign_id')).strip())
        with open(os.path.join(od, name + '.tsv'), 'w') as f:
            f.write('line\tpos\tsign\n')
            for ln in sorted(seqs):
                for i, s in enumerate(seqs[ln], 1):
                    f.write('%s\t%d\t%s\n' % (ln, i, s))
    return '%s: %d positions, %d scored (ref-off-key %d), excluded %s; key rows %d, gated %d; %s' % (
        ITEM, len(rows), nsc, off, dict(nex), len(key), len(gated), ctrl)


def main():
    if tv.variant_main(build, ITEM):  # --variant keyprint|kp2|jackknife [--check] (PREREG-txeng2-2 R, -3 R2)
        return
    rels = ['benchmark-tx/%s.truth.tsv' % ITEM, 'benchmark-tx/%s.truth.tsv.sha256' % ITEM,
            'benchmark-tx/txeng2/dint-f98v-gloss/key_f98v.tsv'] + \
           ['benchmark-tx/outputs/%s/%s.tsv' % (ITEM, n) for n in ('passA', 'passB', 'passZ_pipeline')]
    if '--check' in sys.argv:
        tmp = tempfile.mkdtemp(); build(tmp)
        bad = [r for r in rels if not os.path.exists(os.path.join(ROOT, r)) or
               open(os.path.join(ROOT, r), 'rb').read() != open(os.path.join(tmp, r), 'rb').read()]
        shutil.rmtree(tmp)
        print('stale: ' + ', '.join(bad) if bad else 'up to date')
        sys.exit(1 if bad else 0)
    print(build(ROOT))


if __name__ == '__main__':
    main()
