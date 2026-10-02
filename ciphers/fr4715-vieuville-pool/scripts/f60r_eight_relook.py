#!/usr/bin/env python3
"""GAPS-fr4715-vieuville-pool-6 (2 Oct 2026): the 66 L06-L14 8-rule sites re-read in line context by two fresh blind passes.

GAPS-4 graded 66 tokens of f60r_blocks_ciphertext.tsv at I for their first digit: neither GAPS-4 pass wrote an 8, and
the inventory-only segmenter (f60r_blocks.dp) reads an out-of-key pair 0x as 8x ('8<'). GAPS-5 showed on the lower
block that a blind reader who writes 8s puts them where the rule does. Here two new blind Opus passes (A in order, B
reversed), NOT told the rule, the key or any earlier value, re-read the 54 straightened 3x crops of L06-L14 with a
neutral instruction to decide 0/6/8/9 from the full glyph shape. For every zero of the settled stream (the units
segment() turns into f60r_blocks_ciphertext.tsv) this script labels the site P (first digit of an '8<' token: the
rule says 8) or F (second digit of an undotted key code x0: a true 0), aligns each new pass to the settled stream
per line (difflib on bare digits, '0' and '8' treated as equal for the alignment so a reading change does not break
it), and reads what each pass wrote there (first alternative of an (a/b)). A P site moves I -> H only where BOTH
passes write 8 as their reading. Control (rule 3): the same statistic with the P/F labels shuffled among the
aligned P+F sites, 10,000 times (seed 20261002); the labels vary on exactly the axis measured (which zeros the rule
says are 8), so the control can fail differently from the target.

    python3 scripts/f60r_eight_relook.py PASSA.tsv PASSB.tsv [--write]   # --write: witness/f60r_blocks_eight_relook.tsv
"""
import csv, difflib, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f60r_blocks as fb

W = fb.W


def ref_units():
    settled = {}
    for r in csv.DictReader(open(os.path.join(W, 'f60r_blocks_settled.tsv'), encoding='utf-8'), delimiter='\t'):
        settled[(r['line'], r['position'])] = r['sign']
    by = {}
    draft = os.path.join(W, 'f60r_blocks_rec', 'ciphertext_draft.tsv')
    for r in csv.DictReader([l for l in open(draft, encoding='utf-8') if not l.startswith('#')], delimiter='\t'):
        sign = settled.get((r['line'], r['position']), r['sign'])
        if sign in ('', '-', '_'):
            continue
        by.setdefault(r['line'], []).append(sign)
    return by


def labels(units, codes):
    toks = fb.segment_units(units, codes)
    cls, tokpos, ui, pos = ['O'] * len(units), {}, 0, 0
    for t in toks:
        pos += 1
        width = 1 if (t.startswith('w:') or t in ('?', '♀', '▽')) else len(t.replace('8<', '8').lstrip('.'))
        if t.startswith('8<'):
            cls[ui] = 'P'; tokpos[ui] = pos
        elif width == 2 and not t.startswith('.') and t[-1] == '0' and units[ui + 1].lstrip('.=') == '0':
            cls[ui + 1] = 'F'
        ui += width
    return cls, tokpos, sum(t.startswith('8<') for t in toks)


def pass_units(path):
    rows = {r['crop'].strip(): r for r in csv.DictReader(open(path, encoding='utf-8'), delimiter='\t')}
    by = {}
    for L in fb.READ_LINES:
        acc = []
        for s in range(1, 7):
            r = rows.get('f60r_%s_s%d' % (L, s))
            if r:
                acc, _ = fb.overlap_merge(acc, fb.parse(r['text']))
        by[L] = [(u.lstrip('.='), unsure) for u, unsure in acc if not u.startswith('w:')]
    return by


def align(ref, new):
    key = lambda d: '0' if d == '8' else d
    a = [key(u.lstrip('.=')) for u in ref]; b = [key(u) for u, _ in new]
    m = {}
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op in ('equal', 'replace') and i2 - i1 == j2 - j1:
            for k in range(i2 - i1):
                m[i1 + k] = new[j1 + k]
    return m


def main():
    pa, pb = sys.argv[1], sys.argv[2]
    codes = fb.key_codes()
    REF = ref_units(); A = pass_units(pa); B = pass_units(pb)
    sites, nrule = [], 0
    for L in fb.READ_LINES:
        units = [u for u in REF.get(L, []) if not u.startswith('w:')]
        allu = REF.get(L, [])
        cls, tokpos, n8 = labels(allu, codes); nrule += n8
        # index map: allu index -> digit-only index
        dig = [i for i, u in enumerate(allu) if not u.startswith('w:')]
        ma, mb = align(units, A[L]), align(units, B[L])
        for di, i in enumerate(dig):
            if cls[i] in 'PF':
                ra, rb = ma.get(di), mb.get(di)
                sites.append(dict(line=L, unit=i + 1, tok=tokpos.get(i, ''), cls=cls[i],
                                  A=ra[0] if ra else '-', Aun=int(ra[1]) if ra else 0,
                                  B=rb[0] if rb else '-', Bun=int(rb[1]) if rb else 0))
    P = [s for s in sites if s['cls'] == 'P']; F = [s for s in sites if s['cls'] == 'F']
    both = lambda s: s['A'] == '8' and s['B'] == '8'
    one = lambda p: (lambda s: s[p] == '8')
    def share(ss, f):
        return (sum(f(s) for s in ss) / len(ss)) if ss else 0.0
    print('rule sites (8< tokens) in segment: %d; P sites %d, F sites %d' % (nrule, len(P), len(F)))
    for name, f in (('A', one('A')), ('B', one('B')), ('both', both)):
        print('%-4s reads 8: P %d/%d (%.3f)  F %d/%d (%.3f)' % (name, sum(f(s) for s in P), len(P), share(P, f),
                                                               sum(f(s) for s in F), len(F), share(F, f)))
    print('P unaligned: A %d, B %d; P where A,B disagree: %d' % (sum(s['A'] == '-' for s in P), sum(s['B'] == '-' for s in P),
                                                               sum((s['A'] == '8') != (s['B'] == '8') for s in P)))
    tab = {}
    for s in P + F:
        k = (s['cls'], s['A'], s['B']); tab[k] = tab.get(k, 0) + 1
    print('table (class, A, B): ' + ', '.join('%s/%s/%s %d' % (k[0], k[1], k[2], v) for k, v in sorted(tab.items())))
    pf = P + F; labs = [s['cls'] for s in pf]
    rng = random.Random(20261002)
    for name, f in (('both', both), ('A', one('A')), ('B', one('B'))):
        obs = share(P, f) - share(F, f); null = []
        for _ in range(10000):
            rng.shuffle(labs)
            sp = [s for s, l in zip(pf, labs) if l == 'P']; sf = [s for s, l in zip(pf, labs) if l == 'F']
            null.append(share(sp, f) - share(sf, f))
        null.sort()
        p = sum(x >= obs for x in null) / len(null)
        print('control %-4s: statistic P-share minus F-share %.3f; shuffled P/F labels x10000: mean %.3f p95 %.3f max %.3f; p(>=obs) %.4f'
              % (name, obs, sum(null) / len(null), null[9500], null[-1], p))
        labs = [s['cls'] for s in pf]
    moved = [s for s in P if both(s)]
    print('P sites moved I -> H (both passes read 8): %d of %d' % (len(moved), len(P)))
    if '--write' in sys.argv:
        out = os.path.join(W, 'f60r_blocks_eight_relook.tsv')
        with open(out, 'w', encoding='utf-8') as f:
            f.write('line\tunit\ttoken_pos\tclass\tpassA\tA_unsure\tpassB\tB_unsure\tmoved\n')
            for s in sites:
                f.write('%s\t%d\t%s\t%s\t%s\t%d\t%s\t%d\t%s\n' % (s['line'], s['unit'], s['tok'], s['cls'], s['A'], s['Aun'],
                                                               s['B'], s['Bun'], 'H' if s['cls'] == 'P' and both(s) else ''))
        print('wrote', out)


if __name__ == '__main__':
    main()
