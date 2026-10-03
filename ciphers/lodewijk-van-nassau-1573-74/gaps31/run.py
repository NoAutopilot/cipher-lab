#!/usr/bin/env python3
"""GAPS31 (3 Oct 2026, account-4): align every band-code token of the Groen-printed list-B letters 5810 and
5811 to Groen's clear print with the shared tools/interlinear_align.py (no private DP), and score the result
under the gate pre-registered in gaps31/PREREG.md (committed before the first scoring run).

Pairs: axcomp/build_pairs.py's own anchor cutter (clear-word runs >= 9 letters located in the plain text),
reused unchanged, with the plain text taken from Groen IV (the same spans axnames/align_names.py uses).
Aligner: interlinear_align.py align --floor 121 --clear-consumes --prior key_full.tsv (the AX-COMP recipe):
codes 1-120 seeded from key_full, codes >= 121 never seeded, so every null/word/band meaning comes from print.

Runs (one per call):  python3 gaps31/run.py target       all tokens as transcribed
                      python3 gaps31/run.py hide         known-answer letter control: the 13 HIDDEN letter codes'
                                                         tokens renamed 760-772 (above the floor, unseeded, unused
                                                         in 5810/5811) so their values must come from print alone
                      python3 gaps31/run.py score        reads gaps31/out/*, writes gaps31/result.tsv
"""
import csv, os, sys, subprocess, importlib.util
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
OUT = os.path.join(HERE, 'out')
TOOL = os.path.join(T, '..', '..', 'tools', 'interlinear_align.py')
LETTERS = ('5810', '5811')
HIDDEN = ['96', '57', '86', '66', '15', '65', '116', '25', '75', '80', '111', '94', '115']
HIDE_AS = {c: str(760 + i) for i, c in enumerate(HIDDEN)}
BAND = ['125', '139', '140', '142', '145', '146', '147', '148', '149', '150', '151']


def _mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


bp = _mod('build_pairs', os.path.join(T, 'axcomp', 'build_pairs.py'))
an = _mod('align_names', os.path.join(T, 'axnames', 'align_names.py'))


def key_full():
    k = {}
    with open(os.path.join(T, 'key_full.tsv')) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            k[r['code']] = (r['value'], r['grade'])
    return k


def make_plain(n):
    fname, s, e = an.PAIRS[n][1][0]
    body = an.groen_body(fname, s, e)
    words = [w for w in body.split() if bp.letters(w)]
    L, widx = [], []
    for k, w in enumerate(words):
        for ch in bp.letters(w):
            L.append(ch)
            widx.append(k)
    return words, ''.join(L), widx


def build(tag, hide=None):
    os.makedirs(OUT, exist_ok=True)
    pairs = []
    for n in LETTERS:
        bp.HERE = OUT
        bp.load_plain = make_plain
        orig = bp.load_cipher
        def lc(nn, orig=orig):
            toks = orig(nn)
            return [(k, HIDE_AS[v] if (hide and k == 'num' and v in HIDE_AS) else v, ln) for k, v, ln in toks]
        bp.load_cipher = lc
        bp.main(n)
        bp.load_cipher = orig
        with open(os.path.join(OUT, 'pairs_%s.tsv' % n)) as f:
            pairs += list(csv.DictReader(f, delimiter='\t'))
    pp = os.path.join(OUT, 'pairs_%s.tsv' % tag)
    with open(pp, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
        for r in pairs:
            w.writerow([r['plain_line'], r['plain_raw'], r['cipher_line'], r['cipher_raw']])
    subprocess.run([sys.executable, TOOL, 'align', pp, os.path.join(OUT, 'align_%s.tsv' % tag),
                    os.path.join(OUT, 'key_%s.tsv' % tag), '--floor', '121', '--clear-consumes',
                    '--prior', os.path.join(T, 'key_full.tsv')], check=True)


def obs(tag, code):
    """per-occurrence chunks of one code in a run: '' = NULL observation."""
    out = []
    with open(os.path.join(OUT, 'align_%s.tsv' % tag)) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['kind'] == 'num' and r['value'] == code:
                out.append((r['cipher_line'], r['idx'], r['plain_chunk']))
    return out


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'pairs':
        for n in LETTERS:
            bp.HERE = OUT; bp.load_plain = make_plain; os.makedirs(OUT, exist_ok=True); bp.main(n)
    elif cmd == 'target':
        build('target')
    elif cmd == 'hide':
        build('hide', hide=True)


def names_obs():
    """names.tsv-side (axnames/occ_*.tsv) observation per occurrence: line:pos -> absorbed ('' = NULL)."""
    d = {}
    for n in LETTERS:
        with open(os.path.join(T, 'axnames', 'occ_%s.tsv' % n)) as f:
            for r in csv.DictReader(f, delimiter='\t'):
                d[(r['code'], r['line'])] = d.get((r['code'], r['line']), []) + [r['absorbed']]
    return d


def score():
    k = key_full()
    nulls = sorted((c for c, (v, g) in k.items() if v == 'NULL' and g == 'C' and 121 <= int(c) <= 144), key=int)
    rows, res = [], {}
    # G1
    called, occ_e, occ_n = 0, 0, 0
    for c in nulls:
        o = obs('target', c)
        e = sum(1 for x in o if x[2] == '')
        occ_e += e; occ_n += len(o)
        ok = len(o) > 0 and e > len(o) / 2
        called += ok
        rows.append(['null-control', c, 'NULL', len(o), e, 'NULL' if ok else 'letter', ''])
    res['G1'] = (called, len(nulls), called / len(nulls) >= 0.80, occ_e / occ_n)
    # G2/G3
    called, fe, tot, vok = 0, 0, 0, 0
    for c in HIDDEN:
        o = obs('hide', HIDE_AS[c])
        e = sum(1 for x in o if x[2] == '')
        fe += e; tot += len(o)
        ok = len(o) > 0 and e < len(o) / 2
        called += ok
        top = Counter(an.letters(x[2]) for x in o if x[2]).most_common(1)
        topv = top[0][0] if top else ''
        vok += (topv == an.letters(k[c][0]))
        rows.append(['letter-control', c, k[c][0], len(o), e, 'letter' if ok else 'NULL', 'top=' + topv])
    q = fe / tot
    res['G2'] = (called, len(HIDDEN), called / len(HIDDEN) >= 0.80, vok)
    res['G3'] = (q, q <= 0.316)
    gate = res['G1'][2] and res['G2'][2] and res['G3'][1]
    nob = names_obs()
    for c in BAND:
        o = obs('target', c)
        if not o:
            continue
        e = sum(1 for x in o if x[2] == '')
        conflicts = []
        for line, idx, ch in o:
            prev = nob.get((c, line))
            if prev is not None and any((p == '') != (ch == '') for p in prev):
                conflicts.append(line)
        lift = gate and e >= 4 and e == len(o) and not conflicts
        rows.append(['band', c, 'chunks=' + '|'.join(x[2] or '-' for x in o), len(o), e,
                     'LIFT NULL C' if lift else 'no change', 'conflicts=' + ','.join(conflicts)])
    with open(os.path.join(HERE, 'result.tsv'), 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['class', 'code', 'truth_or_chunks', 'n', 'empty', 'call', 'note'])
        w.writerows(rows)
    print('G1 nulls called NULL %d/%d pass=%s per-occurrence empty %.3f' % res['G1'])
    print('G2 hidden letters called letter %d/%d pass=%s value right %d' % res['G2'])
    print('G3 q (letter false-empty per occurrence) %.3f pass=%s' % res['G3'])
    print('GATE', 'PASS' if gate else 'FAIL')


if __name__ == '__main__' and sys.argv[1] == 'score':
    score()
