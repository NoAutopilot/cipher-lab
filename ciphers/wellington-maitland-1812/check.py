#!/usr/bin/env python3
"""Regenerate codebook.tsv from ciphertext.txt and verify the readings.

Checks (exit 1 on any failure):
  1. every code group that occurs more than once carries the same interlinear reading each time;
  2. the interlinear readings, taken in manuscript order, occur in the same order in Gurwood's printed text of
     the letter (sources/gurwood/vol9-1838-p392-393-maitland-2sept1812.txt), i.e. the H readings agree with C;
  3. page numbers are alphabetical: sorting the code groups by page puts their readings in dictionary order;
  4. the committed codebook.tsv equals the regenerated table (run with --write to update it).
Prints the per-grade token counts used in NOTES.md.
"""
import re, sys, os, io

HERE = os.path.dirname(os.path.abspath(__file__))
CT = os.path.join(HERE, 'ciphertext.txt')
CB = os.path.join(HERE, 'codebook.tsv')
GURWOOD = os.path.join(HERE, '..', '..', 'sources', 'gurwood', 'vol9-1838-p392-393-maitland-2sept1812.txt')

GROUP = re.compile(r'(?<![\w?])(\d{1,2})\??([a-z])\??(\d{1,3})\??\{([^}]*)\}')
RUN = re.compile(r'(?<![\w?])([a-z?]{5,})\{([^}]*)\}')
# spelling differences between the 1812 clerk and Gurwood's 1838 text
SPELL = {'cypher': 'cipher', 'alicant': 'alicante', 'inclose': 'enclose', 'tomorrow': 'to-morrow',
         'honour': 'honor'}
# readings of the letter-cipher runs (Tomokiyo, maitland.htm, keys 1-3; S grade) used only for the order check
RUN_READING = {'jckfmbldnghcdxzkzfsdo': 'villa castin', 'jgnckfhbldmfgbcfxg': 'arevalo'}

def tokens(s):
    s = s.lower().replace('’', "'")
    return [t for t in re.split(r'[^a-z0-9\-]+', s) if t]

def parse():
    groups, runs, order = [], [], []
    for line in io.open(CT, encoding='utf-8'):
        if line.startswith('#') or ':' not in line:
            continue
        tag, text = line.split(':', 1)
        for m in GROUP.finditer(text):
            pos, let, page, reading = m.groups()
            doubtful = '?' in m.group(0).split('{')[0]
            groups.append(dict(line=tag, pos=int(pos), letter=let, page=int(page), reading=reading.strip(),
                               doubtful=doubtful, raw=m.group(0).split('{')[0]))
            order.append(('g', m.start(), groups[-1]))
        for m in RUN.finditer(text):
            runs.append(dict(line=tag, cipher=m.group(1), reading=m.group(2).strip()))
            order.append(('r', m.start(), runs[-1]))
        order.sort(key=lambda t: (t[0] == 'x', ))
    return groups, runs

def main():
    write = '--write' in sys.argv
    groups, runs = parse()
    fail = []

    # 1. consistency of repeated groups
    table = {}
    for g in groups:
        key = (g['pos'], g['letter'], g['page'])
        table.setdefault(key, []).append(g['reading'].lower())
    for key, rs in sorted(table.items()):
        if len(set(rs)) > 1:
            fail.append('group %d%s%d read differently: %s' % (key[0], key[1], key[2], sorted(set(rs))))

    # 2. order against Gurwood: walk the manuscript word by word (clear text and readings alike) and find each
    #    word, in order, within a short window of the printed text; only a reading that cannot be placed counts
    #    as a failure (clear words are allowed to fail, e.g. the heading and the address, which Gurwood omits).
    gw = [l for l in io.open(GURWOOD, encoding='utf-8') if not l.startswith('#')]
    gtoks = tokens(' '.join(gw))
    seq = []                                    # (word, is_reading)
    for line in io.open(CT, encoding='utf-8'):
        if line.startswith('#') or ':' not in line:
            continue
        text = re.sub(r'\[[^\]]*\]', ' ', line.split(':', 1)[1])
        pos = 0
        for m in re.finditer(GROUP.pattern + '|' + RUN.pattern, text):
            seq += [(w, False) for w in tokens(text[pos:m.start()])]
            if m.group(4) is not None:
                reading = m.group(4)
            else:
                reading = RUN_READING.get(m.group(5).replace('?', ''), m.group(6))
            seq += [(w, True) for w in tokens(reading)]
            pos = m.end()
        seq += [(w, False) for w in tokens(text[pos:])]
    i = 0
    matched = total = 0
    for w, is_reading in seq:
        w = SPELL.get(w, w)
        j = i
        while j < len(gtoks) and j - i <= 8 and not (gtoks[j].startswith(w) or (w == 'i' and gtoks[j] == '1')):
            j += 1
        found = j < len(gtoks) and j - i <= 8
        if found:
            i = j + 1
        if is_reading:
            total += 1
            if found:
                matched += 1
            else:
                fail.append('reading %r (manuscript word %d) not found in order in Gurwood' % (w, i))

    # 3. page numbers alphabetical
    def dictform(r):
        r = r.lower()
        for p in ('to ', 'i '):
            if r.startswith(p):
                r = r[len(p):]
        return {'tomorrow': 'morrow'}.get(r, r)
    bypage = sorted(set((g['page'], dictform(g['reading'])) for g in groups))
    for (p1, w1), (p2, w2) in zip(bypage, bypage[1:]):
        if p1 < p2 and w1 > w2:
            fail.append('page order broken: %s p.%d before %s p.%d' % (w1, p1, w2, p2))

    # 4. codebook
    rows = ['group\tpage\tletter\tposition\treading\tcount\tdoubtful\tlines']
    bykey = {}
    for g in groups:
        k = (g['page'], g['letter'], g['pos'])
        bykey.setdefault(k, []).append(g)
    for (page, let, pos), gs in sorted(bykey.items()):
        rows.append('\t'.join([gs[0]['raw'].replace('?', ''), str(page), let, str(pos), gs[0]['reading'], str(len(gs)),
                               'yes' if any(g['doubtful'] for g in gs) else '', ','.join(g['line'] for g in gs)]))
    new = '\n'.join(rows) + '\n'
    if write:
        io.open(CB, 'w', encoding='utf-8').write(new)
    else:
        old = io.open(CB, encoding='utf-8').read() if os.path.exists(CB) else ''
        if old != new:
            fail.append('codebook.tsv is stale; run check.py --write')

    # counts
    n_groups = len(groups)
    n_runs = len(runs)
    print('code groups: %d occurrences, %d distinct; letter-cipher runs: %d' % (n_groups, len(bykey), n_runs))
    print('H (interlinear reading present): %d groups + %d runs' % (sum(1 for g in groups if g['reading']),
                                                                   sum(1 for r in runs if r['reading'])))
    print('C (reading confirmed in order by Gurwood): %d of %d reading words' % (matched, total))
    print('S (runs read only by Tomokiyo\'s keys): %d' % sum(1 for r in runs if not r['reading']))
    print('M (doubtful characters): %d groups, %d runs' % (sum(1 for g in groups if g['doubtful']),
                                                        sum(1 for r in runs if '?' in r['cipher'])))
    print('letters used: %s' % ' '.join(sorted(set(g['letter'] for g in groups))))
    for f in fail:
        print('FAIL:', f)
    sys.exit(1 if fail else 0)

if __name__ == '__main__':
    main()
