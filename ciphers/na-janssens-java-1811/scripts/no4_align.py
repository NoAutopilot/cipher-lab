#!/usr/bin/env python3
"""No.4 set (GAPS8, 2 Oct 2026): gloss table 205R-207L vs raw cipher 204R vs the sealed plain copy 208R-209L.

Usage: python3 scripts/no4_align.py [--seeds 20]   (run from the target folder)

1. Codes: the gloss table's code column (blind pass, no4/gloss_*.tsv) against the independent blind read of the raw
   cipher page (no4/raw_204R.tsv), aligned by difflib; disagreements -> no4/code_disagreements.tsv.
2. Reading: the gloss words in table order -> no4/reading_no4.txt (grade C per position: a period decipherment).
3. Control (rule 3): tools/interlinear_align.py aligns the gloss table's code sequence to the plain copy's letters
   (hard EM, --digits 4 --word-prior: the gloss values seed the first iteration as the hypothesis under test, then
   each code's chunk is whatever the plain copy's letters support in order); per position, the plain-copy chunk is
   compared with the gloss (letters only, lower case, accents folded). The same tool on the same codes in shuffled order
   (each code keeps its own gloss), --seeds seeds, gives the null. Order is the axis the statistic depends on, so the
   control can fail differently from the target. Also char-level LCS of reading vs plain copy, same shuffles.
4. Per code: the gloss value(s) against the plain-copy-aligned value(s); a code whose gloss and plain-copy values
   disagree is logged in no4/conflicts_no4.tsv, never settled by majority (rule 4).
"""
import argparse
import csv
import difflib
import os
import random
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
TOOL = os.path.join(T, '..', '..', 'tools', 'interlinear_align.py')
PAGES = ['205R', '206L', '206R', '207L']


def fold(s):
    s = unicodedata.normalize('NFD', s or '')
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower()
    return ''.join(c for c in s if 'a' <= c <= 'z')


def load_gloss(reconciled=True):
    """gloss cells in table order; no4/reconcile.tsv (the reconciliation pass) overrides code and gloss per cell."""
    rec = {}
    rp = os.path.join(T, 'no4', 'reconcile.tsv')
    if reconciled and os.path.exists(rp):
        with open(rp, encoding='utf-8') as f:
            rec = {r['where']: r for r in csv.DictReader(f, delimiter='\t')}
    cells = []
    for p in PAGES:
        with open(os.path.join(T, 'no4', 'gloss_%s.tsv' % p), encoding='utf-8') as f:
            for r in csv.DictReader(f, delimiter='\t'):
                r['code'] = ''.join(ch for ch in (r.get('code') or '') if ch.isdigit())
                w = '%s:%s' % (p, r['order'])
                if w in rec:
                    if rec[w].get('settled_code', '').strip():
                        r['code'] = ''.join(ch for ch in rec[w]['settled_code'] if ch.isdigit())
                    if rec[w].get('settled_gloss', '').strip():
                        r['gloss'] = rec[w]['settled_gloss'].strip()
                    r['note'] = ((r.get('note') or '') + ' reconciled ' + rec[w].get('conf', '')).strip()
                if not r['code']:
                    continue
                cells.append(r)
    return cells


def load_raw():
    with open(os.path.join(T, 'no4', 'raw_204R.tsv'), encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for ca in a:
        cur = [0]
        for j, cb in enumerate(b):
            cur.append(prev[j] + 1 if ca == cb else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]


def reading_text(cells):
    out = ''
    for c in cells:
        g = (c['gloss'] or '').strip()
        crossed = 'crossed' in (c.get('note') or '').lower()
        if crossed or not g:
            continue
        join = g.endswith('-') or g.endswith('=')
        g = g.rstrip('-= ').strip()
        out += g + ('' if join else ' ')
    return out.strip()


def run_tool(codes, plain, cells):
    with tempfile.TemporaryDirectory() as d:
        kp = os.path.join(d, 'prior.tsv')
        with open(kp, 'w', encoding='utf-8', newline='') as f:
            w = csv.writer(f, delimiter='\t', lineterminator='\n')
            w.writerow(['code', 'value'])
            for c in cells:
                if fold(c['gloss']) and 'crossed' not in (c.get('note') or '').lower():
                    w.writerow([c['code'], c['gloss']])
        pairs = os.path.join(d, 'p.tsv')
        with open(pairs, 'w', encoding='utf-8', newline='') as f:
            w = csv.writer(f, delimiter='\t', lineterminator='\n')
            w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
            # accents folded first: the tool keeps only a-z, so 'expédition' would lose its é
            plain_f = ''.join(ch for ch in unicodedata.normalize('NFD', plain) if unicodedata.category(ch) != 'Mn')
            w.writerow(['208R-209L', plain_f, '204R/205R-207L', ' '.join(codes)])
        al, ky = os.path.join(d, 'a.tsv'), os.path.join(d, 'k.tsv')
        subprocess.run([sys.executable, TOOL, 'align', pairs, al, ky, '--floor', '0', '--digits', '4',
                        '--prior', kp, '--word-prior'], check=True,
                       stdout=subprocess.DEVNULL)
        with open(al, encoding='utf-8') as f:
            rows = list(csv.DictReader(f, delimiter='\t'))
    return [r['plain_chunk'] for r in rows]


def position_agreement(cells, chunks):
    n = agree = 0
    for c, ch in zip(cells, chunks):
        g = fold(c['gloss'])
        if not g or 'crossed' in (c.get('note') or '').lower():
            continue
        n += 1
        agree += fold(ch) == g
    return agree, n


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--seeds', type=int, default=20)
    a = ap.parse_args()
    cells = load_gloss()
    raw = load_raw()
    gcodes = [c['code'].strip() for c in cells]
    rcodes = [r['code'].strip() for r in raw]

    # 1. codes, two independent reads
    sm = difflib.SequenceMatcher(a=gcodes, b=rcodes, autojunk=False)
    same = sum(b.size for b in sm.get_matching_blocks())
    with open(os.path.join(T, 'no4', 'code_disagreements.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['op', 'gloss_idx', 'gloss_codes', 'gloss_where', 'raw_codes', 'raw_where'])
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                continue
            w.writerow([op, i1 + 1, ' '.join(gcodes[i1:i2]),
                        ' '.join('%s:%s' % (c['leaf'], c['order']) for c in cells[i1:i2]),
                        ' '.join(rcodes[j1:j2]),
                        ' '.join('%s:%s' % (r['line'], r['pos']) for r in raw[j1:j2])])
    print('codes: gloss table %d, raw 204R %d, matched in order %d (%.1f%% of gloss, %.1f%% of raw)'
          % (len(gcodes), len(rcodes), same, 100 * same / len(gcodes), 100 * same / len(rcodes)))

    # 2. reading
    rd = reading_text(cells)
    with open(os.path.join(T, 'no4', 'reading_no4.txt'), 'w', encoding='utf-8') as f:
        f.write('# No.4 (3 Aout 1811), raw cipher 204R read through its own period gloss 205R-207L, table order;\n'
                '# every token grade C (period decipherment of this very text). scripts/no4_align.py, GAPS8 2 Oct 2026.\n')
        f.write(rd + '\n')

    # 3. control against the sealed plain copy
    with open(os.path.join(T, 'no4', 'SEALED_plain_208R-209L.txt'), encoding='utf-8') as f:
        plain = f.read()
    plain_l = fold(plain)
    chunks = run_tool(gcodes, plain, cells)
    ag, n = position_agreement(cells, chunks)
    lc = lcs(fold(rd), plain_l) / len(plain_l)
    nulls_pos, nulls_lcs = [], []
    for s in range(a.seeds):
        rng = random.Random(s)
        sh = cells[:]
        rng.shuffle(sh)
        ch = run_tool([c['code'].strip() for c in sh], plain, cells)
        x, m = position_agreement(sh, ch)
        nulls_pos.append(x / m)
        nulls_lcs.append(lcs(fold(reading_text(sh)), plain_l) / len(plain_l))
    nulls_pos.sort()
    nulls_lcs.sort()
    print('position agreement gloss vs plain-copy alignment: %d/%d = %.3f; shuffled-order null (%d seeds) '
          'mean %.3f max %.3f' % (ag, n, ag / n, a.seeds, sum(nulls_pos) / len(nulls_pos), nulls_pos[-1]))
    print('char LCS reading vs plain copy: %.3f of %d plain letters; shuffled null mean %.3f max %.3f'
          % (lc, len(plain_l), sum(nulls_lcs) / len(nulls_lcs), nulls_lcs[-1]))

    # 4. per code
    gl, pl = defaultdict(Counter), defaultdict(Counter)
    for c, ch in zip(cells, chunks):
        if 'crossed' in (c.get('note') or '').lower():
            continue
        gl[c['code'].strip()][fold(c['gloss'])] += 1
        pl[c['code'].strip()][fold(ch)] += 1
    nconf = 0
    with open(os.path.join(T, 'no4', 'conflicts_no4.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['code', 'gloss_values', 'plaincopy_values', 'note'])
        for code in sorted(gl, key=lambda x: int(x) if x.isdigit() else 0):
            if not any(gl[code]):
                continue
            if set(gl[code]) != set(pl[code]):
                nconf += 1
                w.writerow([code, ','.join('%s:%d' % kv for kv in gl[code].items()),
                            ','.join('%s:%d' % kv for kv in pl[code].items()),
                            'gloss and plain-copy alignment differ; logged, not settled (rule 4)'])
    print('codes with gloss/plain-copy value conflict: %d of %d (no4/conflicts_no4.tsv)'
          % (nconf, sum(1 for k in gl if any(gl[k]))))

    # 5. merge file for scripts/merge_leaf.py: the gloss value per cell (grade C, period decipherment); a cell whose
    # plain-copy chunk differs carries 'uncertain' in its note, so merge_leaf grades a new code M, never the
    # plain-copy value in its place (rule 4: the conflict is logged, not settled)
    with open(os.path.join(T, 'no4', 'no4_merge.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['leaf', 'order', 'code', 'gloss', 'note'])
        nm = 0
        for c, ch in zip(cells, chunks):
            note = (c.get('note') or '')
            if 'crossed' in note.lower():
                w.writerow(['no4-' + c['leaf'], c['order'], c['code'], c['gloss'], 'crossed-out'])
                continue
            g = fold(c['gloss'])
            if not g or fold(ch) == g:
                nt = ''   # punctuation cells have no letters to check; kept at the gloss's own grade
            else:
                nm += 1
                nt = 'uncertain: plain copy 208R-209L aligns %r here' % ch
            w.writerow(['no4-' + c['leaf'], c['order'], c['code'], c['gloss'].rstrip('-= ').strip(), nt])
    print('merge file no4/no4_merge.tsv: %d cells, %d marked uncertain' % (len(cells), nm))


if __name__ == '__main__':
    main()
