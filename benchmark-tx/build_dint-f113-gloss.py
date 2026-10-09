#!/usr/bin/env python3
"""Build benchmark item dint-f113-gloss for BENCHMARK-TX.tsv (TXP-D113, LANE TX-ENGINEER-2, 9 Oct 2026).

Leaf: BnF fr.3619 f.113 (DECODE record 9443, image IMG_R9443_I44629_P.jpg, 1600 x 2264 px), Dinteville, Langres, Nov 1591.
Order kept (brief .claude/briefs/runs/2026-10-09-account4-txp-gloss.md): crops, two blind Opus passes, reconcile +
adjudication -> passZ_pipeline.tsv were committed before gloss.tsv was read.

Reference = passZ_pipeline.tsv (this worker's reconcile + Sonnet adjudication; home advantage). Truth = the period
interlinear decipherment on the leaf (gloss.tsv: two blind Opus reads of the gloss rows, reconciled) aligned per cipher line
to passZ's sign sequence by tools/interlinear_align.py with the settings of f128/print_align/align_print.py (syl mode:
floor 100, null_cost -1.0, max_chunk 3, seg_bonus 0, len_prior 1, FOLD_FS False), gloss '+', '|' and '?' (a sign the
decipherer left unexpanded or a word unreadable) kept as the wildcard '?'.
Key rebuilt from that alignment (sign -> majority letter, n, agree share). A position is scored only when its aligned chunk is
one letter, that letter is the sign's majority value with n >= 2 and agree >= 0.75 on this leaf, and the sign is either absent
from f128/print_align/key_print.tsv or carries the same meaning there. Truth = every sign meeting that rule with the same
letter (a | set). Excluded (counted): gloss-unread, unaligned, multi-letter, low-agree (n < 2 or agree < 0.75 or the chunk is
not the majority), key-conflict (key_print gives another meaning), off-sheet (NEW:/?).
Flag 'align-conflict' on a scored position next to (+-1) a position interlinear_align marks conflict or null.
By construction a passZ sign on a scored position is in its truth set, so passZ can err only by insertion/deletion against
itself (0); its misreads land in the excluded classes (low-agree, key-conflict) and are counted there, not scored.
Deviation (SEED, stated in RESULTS.md): the pre-registered unseeded run (align_print.py settings, no prior) FAILED on this
leaf -- 0 scored, align agrees 51/186, GAPS4 real 0.022 vs shuffled mean 0.071, rank 200 of 201: five whole-line pairs give the
hard-EM too little anchoring (f128 aligned per gloss word). The build therefore seeds the first E-step with key_print.tsv's
counts (meaning: agree, plus 'others'); later iterations use this leaf's own counts only. This makes the key_print check
partly built in: a scored position still needs this leaf's gloss letter as the sign's leaf majority at n >= 2, agree >= 0.75.
Control: GAPS4 statistic (share of decoded letters in difflib blocks >= 3 against the folded gloss), real rebuilt key vs 200
value-shuffled keys (seed 1).
  python3 benchmark-tx/build_dint-f113-gloss.py [--check]
"""
import csv, difflib, hashlib, os, random, re, shutil, sys, tempfile
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TX = os.path.join(ROOT, 'benchmark-tx/txeng2/dint-f113-gloss')
KP = os.path.join(ROOT, 'ciphers/fr3621-dinteville-1592/f128/print_align/key_print.tsv')
ITEM = 'dint-f113-gloss'
LABEL_KP = {'-:-': 'div', '+': 'plus'}  # reader-table labels -> key_print labels
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import interlinear_align as ia  # noqa: E402
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import truth_variant as tv  # noqa: E402

ia.FOLD_FS = False
SEED = True


def rd(p, comments=True):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader((l for l in f if not (comments and l.startswith('#'))), delimiter='\t'))


def fold(s):
    s = s.lower().replace('v', 'u').replace('j', 'i').replace('y', 'i')
    return re.sub(r'[^a-z]', '', s)


def matched(dec, clear):
    sm = difflib.SequenceMatcher(None, dec, clear, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size >= 3) / max(1, len(dec))


def offsheet(s):
    return s.startswith('NEW') or s == '?'


def build(out_root, variant=None):
    z = rd(os.path.join(TX, 'passZ_pipeline.tsv'))
    lines = defaultdict(list)
    for r in z:
        lines[r['line']].append(r['sign'].strip())
    gl = {r['line']: r['text'] for r in rd(os.path.join(TX, 'gloss.tsv'))}
    order = [ln for ln in sorted(lines) if ln in gl]
    codes = {}
    pairs = []
    for ln in order:
        raw = ' '.join(str(codes.setdefault(s, 100 + len(codes))) for s in lines[ln])
        txt = re.sub(r'[+|]', '?', gl[ln])
        pairs.append({'plain_line': ln, 'plain_raw': txt, 'cipher_line': ln, 'cipher_raw': raw})
    inv = {c: s for s, c in codes.items()}
    kp_rows = {r['sign']: r for r in rd(KP, comments=False)}
    prior = {}
    for s, c in codes.items():  # SEED (deviation, see docstring): key_print's counts as the first E-step's prior
        r = kp_rows.get(LABEL_KP.get(s, s))
        if r:
            cnt = Counter({fold(r['meaning']): int(r['agree'])})
            for o in filter(None, r['others'].split(',')):
                m, n = o.split(':')
                cnt[fold(m)] += int(n)
            prior[c] = cnt
    prep, results, counts, shown = ia.run_align(pairs, floor=100, null_cost=-1.0, max_chunk=3, seg_bonus=0.0,
                                                len_prior=1.0, wildcard='?', prior=prior if SEED else None)
    trows = ia.token_rows(prep, results, counts, shown)
    # rebuilt key from the alignment
    key = {}
    for v, cnt in counts.items():
        top, topn = ia.top_of(cnt)
        n = sum(cnt.values())
        key[inv[v]] = (top, n, topn, topn / n if n else 0.0)
    kp = {r['sign']: r['meaning'] for r in rd(KP, comments=False)}

    def kp_of(s):
        return kp.get(LABEL_KP.get(s, s))
    good = {}
    for s, (top, n, topn, ag) in key.items():
        if offsheet(s) or len(top) != 1 or n < 2 or ag < 0.75:
            continue
        if kp_of(s) is not None and kp_of(s) != top:
            continue
        good[s] = top
    by_val = defaultdict(set)
    for s, v in good.items():
        by_val[v].add(s)

    # control
    clear = fold(''.join(gl[ln] for ln in order).replace('?', ''))
    seq = [s for ln in order for s in lines[ln]]
    mp = {s: k[0] for s, k in key.items()}

    def dec(m):
        return fold(''.join(m.get(s, '') for s in seq))
    real = matched(dec(mp), clear)
    ids = sorted(mp)
    vv = [mp[i] for i in ids]
    rng = random.Random(1)
    sh = []
    for _ in range(200):
        rng.shuffle(vv)
        sh.append(matched(dec(dict(zip(ids, vv))), clear))
    rank = 1 + sum(1 for x in sh if x >= real)
    agrees = sum(1 for t in trows if t[7] == 'agrees')
    kp_in = [s for s in good if kp_of(s) is not None]
    ctrl = ('align agrees %d/%d = %.3f; GAPS4 control: real rebuilt key matched %.3f vs 200 value-shuffled keys mean %.3f '
            'max %.3f, rank %d of 201; key rows rebuilt %d, kept (n>=2, agree>=0.75, key_print-consistent) %d, of which in '
            'key_print %d (all agree by rule); dropped for key_print conflict %s'
            % (agrees, len(trows), agrees / max(1, len(trows)), real, sum(sh) / len(sh), max(sh), rank, len(key), len(good),
               len(kp_in), ','.join(sorted(s for s, k in key.items() if kp_of(s) is not None and kp_of(s) != k[0]
                                           and len(k[0]) == 1 and k[1] >= 2 and k[3] >= 0.75)) or 'none'))

    rows, nsc, nex = [], 0, Counter()
    bad_status = [t[7].startswith('conflict') or t[7] == 'null-or-unaligned' for t in trows]
    for i, t in enumerate(trows):
        ln, idx, chunk, status = t[0], t[1], t[6], t[7]
        s = inv[int(t[2])]
        chunk_f = fold(chunk) if '?' not in chunk else chunk
        st, truth = 'scored', ''
        if offsheet(s):
            st = 'excluded:off-sheet'
        elif '?' in chunk:
            st = 'excluded:gloss-unread'
        elif not chunk or status == 'null-or-unaligned':
            st = 'excluded:unaligned'
        elif len(chunk_f) != 1:
            st = 'excluded:multi-letter'
        else:
            top, n, topn, ag = key[s]
            if kp_of(s) is not None and kp_of(s) != chunk_f:
                st = 'excluded:key-conflict'
            elif s not in good or good[s] != chunk_f:
                st = 'excluded:low-agree'
            else:
                truth = '|'.join(sorted(by_val[chunk_f]))
        flag = ''
        if st == 'scored':
            nsc += 1
            same = [j for j in (i - 1, i + 1) if 0 <= j < len(trows) and trows[j][0] == ln]
            if any(bad_status[j] for j in same):
                flag = 'align-conflict'
        else:
            nex[st] += 1
        rows.append((ln, idx + 1, s, truth, chunk, st, flag, status))

    if variant:  # PREREG-txeng2-2 R (TXP-REBUILD): second truth from a key independent of the reads
        assert variant == 'keyprint', 'this item builds --variant keyprint only'
        return tv.write_variant(out_root, ITEM, variant, tv.keyprint_rows(trows, [(r[0], r[1], r[2]) for r in rows], lambda c: '?' in c, fold), ctrl)
    os.makedirs(os.path.join(out_root, 'benchmark-tx'), exist_ok=True)
    tp = os.path.join(out_root, 'benchmark-tx', ITEM + '.truth.tsv')
    with open(tp, 'w', encoding='utf-8') as f:
        f.write('# fr.3619 f.113 (DECODE 9443) known answer: the period interlinear decipherment on the leaf (gloss.tsv) aligned '
                'to passZ_pipeline.tsv, key rebuilt from this leaf at n>=2 agree>=0.75 + key_print check; built by '
                'benchmark-tx/build_dint-f113-gloss.py\n# %s\nline\tpos\tref_sign\ttruth\tplain\tstatus\tflag\talign_status\n'
                % ctrl)
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    with open(tp + '.sha256', 'w') as f:
        f.write(hashlib.sha256(open(tp, 'rb').read()).hexdigest() + '  ' + ITEM + '.truth.tsv\n')
    kt = os.path.join(out_root, 'benchmark-tx/txeng2/dint-f113-gloss/key_rebuilt.tsv')
    os.makedirs(os.path.dirname(kt), exist_ok=True)
    with open(kt, 'w', encoding='utf-8') as f:
        f.write('sign\tmeaning\tn\tagree\tagree_share\tkey_print\tkept\n')
        for s in sorted(key):
            top, n, topn, ag = key[s]
            f.write('%s\t%s\t%d\t%d\t%.2f\t%s\t%s\n' % (s, top, n, topn, ag, kp_of(s) or '', 'yes' if s in good else 'no'))

    od = os.path.join(out_root, 'benchmark-tx/outputs', ITEM)
    os.makedirs(od, exist_ok=True)
    for name in ('passA', 'passB', 'passZ_pipeline'):
        out = []
        for r in rd(os.path.join(TX, name + '.tsv')):
            ln = r.get('line') or r['passage']
            out.append((ln, r['pos'], (r.get('sign') or r.get('sign_id')).strip()))
        with open(os.path.join(od, name + '.tsv'), 'w', encoding='utf-8') as f:
            f.write('line\tpos\tsign\n')
            for o in out:
                f.write('\t'.join(o) + '\n')
    return '%s: %d positions, %d scored, excluded %s; %s' % (ITEM, len(rows), nsc, dict(nex), ctrl)


def main():
    if tv.variant_main(build, ITEM):  # --variant keyprint|jackknife [--check] (PREREG-txeng2-2 R)
        return
    if '--check' in sys.argv:
        tmp = tempfile.mkdtemp()
        build(tmp)
        bad = []
        for rel in ['benchmark-tx/%s.truth.tsv' % ITEM, 'benchmark-tx/%s.truth.tsv.sha256' % ITEM,
                    'benchmark-tx/txeng2/dint-f113-gloss/key_rebuilt.tsv'] + \
                ['benchmark-tx/outputs/%s/%s.tsv' % (ITEM, n) for n in ('passA', 'passB', 'passZ_pipeline')]:
            a, b = os.path.join(ROOT, rel), os.path.join(tmp, rel)
            if not os.path.exists(a) or open(a, 'rb').read() != open(b, 'rb').read():
                bad.append(rel)
        shutil.rmtree(tmp)
        print('stale: ' + ', '.join(bad) if bad else 'up to date')
        sys.exit(1 if bad else 0)
    print(build(ROOT))


if __name__ == '__main__':
    main()
