#!/usr/bin/env python3
"""Build the fr.3623 f.23r (DECODE 9452, Dinteville to Nevers, Langres 25 Oct [1591], Italian, Birago-style symbols)
known-answer item for BENCHMARK-TX.tsv (TXP-B23, LANE TX-ENGINEER-2, 9 Oct 2026; PREREG benchmark-tx/PREREG-txeng2-0.md 0b +
Amendment 1).

Truth = the period interlinear decipherment written over every cipher line of the leaf (gloss.tsv, two blind Opus reads of
the gloss, reconciled), aligned per line to the reference sign sequence passZ_pipeline.tsv (TXP-B23's reconcile + Sonnet
adjudication, committed BEFORE the gloss was read) with tools/interlinear_align.py under the settings of
ciphers/fr3621-dinteville-1592/f128/print_align/align_print.py (syl mode: floor 100, null_cost -1.0, max_chunk 3, seg_bonus 0,
len_prior 1.0, FOLD_FS False) plus wildcard '?' for gloss letters the decipherer left unexpanded ('+', '|') or that the gloss
readers could not read ('?'). No external key: fr.3623's key record (DECODE 9453) is not used (rebuild only, per the brief).

Key rebuilt from this leaf's alignment: sign -> majority one-letter chunk, n (non-empty chunks), agree (top / n). A sign is
SUPPORTED when n >= 2 and agree >= 0.75 and it is not off-sheet (NEW:... or ?). truth for a scored position = the set of
supported signs whose majority value is the gloss letter (homophones; value-level err_true).

Status per position of passZ:
  excluded:unaligned       no chunk (null) -- e.g. a struck sign the decipherer skipped
  excluded:gloss-unread    the chunk holds the wildcard
  excluded:multi-letter    the chunk is two or more letters
  excluded:off-sheet       passZ sign is NEW:... or ?
  excluded:low-agree       passZ sign not supported (n < 2 or agree < 0.75)
  scored                   one-letter chunk == the sign's majority value (the brief's recipe)
  scored + flag align-conflict   one-letter chunk != the supported sign's majority value, and the chunk letter has a supported
                           homophone set: a probable wrong sign in passZ (or a decipherer slip). Scored so that passZ's
                           wrong-sign positions count; tx_bench --exclude-flagged gives the strict recipe figure beside it.
  excluded:key-conflict    chunk != majority and the chunk letter has no supported sign
Control (GAPS4, harvest/align_sheet.py's statistic as build_birago152.py prints it): share of passZ decoded under the rebuilt
key lying in difflib matching blocks >= 3 against the folded gloss, real key vs 200 value-shuffled keys (seed 1).

  python3 benchmark-tx/build_bir1591-f23r-gloss.py [--check]
--check: rebuild in a temp dir and exit 1 if the committed truth, key or outputs differ (rule 7).
"""
import csv, difflib, hashlib, os, random, re, shutil, sys, tempfile
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import interlinear_align as ia  # noqa: E402
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import truth_variant as tv  # noqa: E402

ia.FOLD_FS = False
TX = os.path.join(ROOT, 'benchmark-tx/txeng2/bir1591-f23r-gloss')
ITEM = 'bir1591-f23r-gloss'
WILD = '?'
MIN_N, MIN_AGREE = 2, 0.75


def rd(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def fold(s):
    s = s.lower().replace('v', 'u').replace('j', 'i').replace('&', 'et')
    return re.sub(r'[^a-z]', '', s)


def matched(dec, clear):
    sm = difflib.SequenceMatcher(None, dec, clear, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks() if b.size >= 3) / max(1, len(dec))


def off_sheet(s):
    return s.startswith('NEW') or s.startswith('?') or not s


def gloss_text(t):
    t = t.replace('+', WILD).replace('|', WILD)
    return re.sub(r'[^A-Za-z?& ]', '', t)


def build(out_root, variant=None):
    z = [(r['line'], int(r['pos']), r['sign'].strip()) for r in rd(os.path.join(TX, 'passZ_pipeline.tsv'))]
    gl = {r['line']: r['text'] for r in rd(os.path.join(TX, 'gloss.tsv'))}
    lines = []
    for ln, _, _ in z:
        if ln not in lines:
            lines.append(ln)
    codes = {}
    pairs = []
    for ln in lines:
        sg = [s for l2, _, s in z if l2 == ln]
        raw = ' '.join(str(codes.setdefault(s, 100 + len(codes))) for s in sg)
        pairs.append({'plain_line': ln, 'plain_raw': gloss_text(gl.get(ln, '')), 'cipher_line': ln, 'cipher_raw': raw})
    inv = {str(c): s for s, c in codes.items()}
    prep, results, counts, shown = ia.run_align(pairs, floor=100, null_cost=-1.0, max_chunk=3, seg_bonus=0.0, len_prior=1.0,
                                               wildcard=WILD)
    trows = ia.token_rows(prep, results, counts, shown)
    assert len(trows) == len(z), (len(trows), len(z))

    key = {}
    for v, cnt in counts.items():
        s = inv[str(v)]
        top, topn = ia.top_of(cnt)
        n = sum(cnt.values())
        key[s] = (top, n, topn, sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[1:])
    sup = {s: k[0] for s, k in key.items() if not off_sheet(s) and k[1] >= MIN_N and k[2] / k[1] >= MIN_AGREE and len(k[0]) == 1}
    homo = {}
    for s, v in sup.items():
        homo.setdefault(v, set()).add(s)

    rows, nsc, nex, nflag = [], 0, Counter(), 0
    for (ln, pos, sign), tr in zip(z, trows):
        chunk, ast = ia.fold(tr[6]), tr[7]
        st, truth, flag = 'scored', '', ''
        if not tr[6]:
            st = 'excluded:unaligned'
        elif WILD in tr[6]:
            st = 'excluded:gloss-unread'
        elif len(chunk) != 1:
            st = 'excluded:multi-letter'
        elif off_sheet(sign):
            st = 'excluded:off-sheet'
        elif sign not in sup:
            st = 'excluded:low-agree'
        elif sup[sign] == chunk:
            truth = '|'.join(sorted(homo[chunk]))
        elif chunk in homo:
            truth = '|'.join(sorted(homo[chunk]))
            flag = 'align-conflict'
        else:
            st = 'excluded:key-conflict'
        if st == 'scored':
            nsc += 1
            nflag += bool(flag)
        else:
            nex[st] += 1
        rows.append((ln, pos, sign, truth, tr[6], st, flag, ast))

    # control
    clear = fold(' '.join(gloss_text(gl.get(ln, '')).replace(WILD, '') for ln in lines))
    seq = [s for _, _, s in z]
    m = {s: k[0] for s, k in key.items() if not off_sheet(s)}

    def dec(mp):
        return fold(''.join(mp.get(s, '') for s in seq))
    real = matched(dec(m), clear)
    ids = sorted(m)
    vv = [m[i] for i in ids]
    rng = random.Random(1)
    sh = []
    for _ in range(200):
        rng.shuffle(vv)
        sh.append(matched(dec(dict(zip(ids, vv))), clear))
    rank = 1 + sum(1 for x in sh if x >= real)
    agrees = sum(1 for t in trows if t[7] == 'agrees')
    ctrl = ('align agrees %d/%d = %.3f; GAPS4 control: rebuilt key matched %.3f vs 200 value-shuffled keys mean %.3f max %.3f, '
            'rank %d of 201; key rows %d, supported (n>=%d, agree>=%.2f, one letter, on-sheet) %d'
            % (agrees, len(trows), agrees / len(trows), real, sum(sh) / len(sh), max(sh), rank, len(key), MIN_N, MIN_AGREE,
               len(sup)))

    if variant:  # PREREG-txeng2-2 R (TXP-REBUILD): line i scored with the key rebuilt from the other lines (grade C-)
        assert variant == 'jackknife', 'this item builds --variant jackknife only'
        return tv.write_variant(out_root, ITEM, variant, tv.jackknife_rows(trows, [(r[0], r[1], r[2]) for r in rows], lambda c: WILD in c, fold, off_sheet), ctrl)
    os.makedirs(os.path.join(out_root, 'benchmark-tx'), exist_ok=True)
    tp = os.path.join(out_root, 'benchmark-tx', ITEM + '.truth.tsv')
    with open(tp, 'w', encoding='utf-8') as f:
        f.write('# fr.3623 f.23r (DECODE 9452) known answer: the period interlinear decipherment on the leaf (gloss.tsv) aligned '
                'to passZ_pipeline.tsv, key rebuilt from this leaf alone; built by benchmark-tx/build_bir1591-f23r-gloss.py\n'
                '# %s\nline\tpos\tref_sign\ttruth\tplain\tstatus\tflag\talign_status\n' % ctrl)
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    with open(tp + '.sha256', 'w') as f:
        f.write(hashlib.sha256(open(tp, 'rb').read()).hexdigest() + '  ' + ITEM + '.truth.tsv\n')
    kd = os.path.join(out_root, 'benchmark-tx/txeng2', ITEM)
    os.makedirs(kd, exist_ok=True)
    with open(os.path.join(kd, 'key_rebuilt.tsv'), 'w', encoding='utf-8') as f:
        f.write('sign\tmeaning\tn\tagree\tshare\tsupported\tothers\n')
        for s in sorted(key):
            top, n, topn, rest = key[s]
            f.write('%s\t%s\t%d\t%d\t%.2f\t%s\t%s\n' % (s, top, n, topn, topn / n, 'yes' if s in sup else 'no',
                                                     ','.join('%s:%d' % kv for kv in rest)))

    od = os.path.join(out_root, 'benchmark-tx/outputs', ITEM)
    os.makedirs(od, exist_ok=True)

    def norm(path, name):
        out = []
        for r in rd(path):
            ln = r.get('line') or 'f23r_' + r['passage']
            out.append((ln, r['pos'], (r.get('sign') or r.get('sign_id')).strip()))
        with open(os.path.join(od, name + '.tsv'), 'w', encoding='utf-8') as f:
            f.write('line\tpos\tsign\n')
            for o in out:
                f.write('\t'.join(o) + '\n')
    for n in ('passA', 'passB', 'passZ_pipeline'):
        norm(os.path.join(TX, n + '.tsv'), n)
    return '%s: %d positions, %d scored (%d flagged align-conflict), excluded %s; %s' % (
        ITEM, len(rows), nsc, nflag, dict(sorted(nex.items())), ctrl)


OUTS = ['benchmark-tx/%s.truth.tsv' % ITEM, 'benchmark-tx/%s.truth.tsv.sha256' % ITEM,
        'benchmark-tx/txeng2/%s/key_rebuilt.tsv' % ITEM] + \
       ['benchmark-tx/outputs/%s/%s.tsv' % (ITEM, n) for n in ('passA', 'passB', 'passZ_pipeline')]


def main():
    if tv.variant_main(build, ITEM):  # --variant keyprint|jackknife [--check] (PREREG-txeng2-2 R)
        return
    if '--check' in sys.argv:
        tmp = tempfile.mkdtemp()
        print(build(tmp))
        bad = [rel for rel in OUTS if not os.path.exists(os.path.join(ROOT, rel)) or
               open(os.path.join(ROOT, rel), 'rb').read() != open(os.path.join(tmp, rel), 'rb').read()]
        shutil.rmtree(tmp)
        print('stale: ' + ', '.join(bad) if bad else 'up to date')
        sys.exit(1 if bad else 0)
    print(build(ROOT))


if __name__ == '__main__':
    main()
