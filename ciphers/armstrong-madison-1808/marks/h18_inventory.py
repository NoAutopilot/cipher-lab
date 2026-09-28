#!/usr/bin/env python3
"""Campaign step H18 (28 Sept 2026): inventory of marks attached to numeral groups, reconciled over readers and
witnesses, with a value-recurrence test.

Inputs: marks/h18_passes/<page>_<witness>_<pass>.tsv -- one blind Sonnet reader's report per page per witness (page 1 has
one frame, so two readers on the same sheets), lines "line<n> TAB first groups TAB marked groups TAB conf", marked groups
as "GROUP:HIGH|LOW:detail; ...". A mark is ACCEPTED when two independent reports (the other witness, or the other reader
on page 1) list the same group value with the same class on the same page (line numbers differ between the witnesses' crop
manifests by an offset, so the match is by page + group + class); a mark seen once is HELD (grade M).

Test: do marks recur on the same VALUE? Statistic = number of distinct values carrying an accepted mark at every one of
their occurrences in ciphertext_ms.txt (value-bound marks), vs a null that keeps the marked positions and shuffles the
values among all groups of the same digit length (2,000 draws). Also reports marks by class and, for LOW marks, by the
digit they sit under (frame 956's printed rules give meaning to last / penult / antepenult).
Writes marks/h18_inventory.tsv and prints the summary.
"""
import collections, csv, glob, random, re
from pathlib import Path
HERE = Path(__file__).resolve().parent; T = HERE.parent
rng = random.Random(20260928)
reports = collections.defaultdict(list)   # (page, line) -> list of (witness, pass, group, cls, detail, conf)
for f in sorted(glob.glob(str(HERE/'h18_passes'/'*.tsv'))):
    page, wit, pas = Path(f).stem.split('_')
    for raw in open(f, encoding='utf-8'):
        raw = raw.strip()
        if not raw or raw.startswith('#'): continue
        cells = raw.split('\t')
        if len(cells) < 3: continue
        m = re.match(r'line\s*(\d+)', cells[0]);
        if not m: continue
        ln = int(m.group(1)); marks = cells[2].strip(); conf = cells[3].strip() if len(cells) > 3 else ''
        if marks.upper().startswith('NONE'): continue
        for item in re.split(r';\s*', marks):
            parts = item.split(':', 2)
            if len(parts) < 2: continue
            g = re.sub(r'\D', '', parts[0]); cls = parts[1].strip().upper()[:4]
            det = parts[2].strip() if len(parts) > 2 else ''
            if g: reports[(page, ln)].append((wit, pas, g, cls, det, conf))
rows = []
bypage = collections.defaultdict(list)
for (page, ln), items in reports.items():
    for it in items: bypage[page].append((ln,)+it)
for page, items in sorted(bypage.items()):
    byg = collections.defaultdict(list)
    for it in items: byg[(it[3], it[4])].append(it)   # key: (group, class); the two witnesses' line numbers differ by an offset
    for (g, cls), its in byg.items():
        ln = '/'.join(sorted({str(i[0]) for i in its})); its = [i[1:] for i in its]
        sources = {(i[0], i[1]) for i in its}
        status = 'accepted' if len(sources) >= 2 else 'held'
        under = ''
        if cls == 'LOW':
            d = ' '.join(i[4].lower() for i in its)
            for k in ('last', 'penult', 'antepenult', 'first', 'second'):
                if k in d: under = k; break
        rows.append((page, ln, g, cls, under, status, len(sources), ' | '.join(f'{i[0]}/{i[1]}: {i[4]} ({i[5]})' for i in its)))
with open(HERE/'h18_inventory.tsv', 'w') as f:
    f.write('page\tline\tgroup\tclass\tunder_digit\tstatus\tn_sources\tdetails\n')
    for r in rows: f.write('\t'.join(map(str, r))+'\n')
acc = [r for r in rows if r[5] == 'accepted']; held = [r for r in rows if r[5] == 'held']
print(f'marks reported: {len(rows)} (accepted {len(acc)}, held {len(held)})')
print('accepted by class:', collections.Counter(r[3] for r in acc), ' LOW by digit:', collections.Counter(r[4] for r in acc if r[3] == 'LOW'))
# value recurrence
body = [l for l in (T/'ciphertext_ms.txt').read_text(encoding='utf-8').splitlines() if l.strip() and not l.startswith('#')]
groups = [re.sub(r'[\^\?]', '', t) for l in body for t in l.split() if re.fullmatch(r'\d+[\^\?]?', t)]
occ = collections.Counter(groups)
marked_vals = collections.Counter(r[2] for r in acc)
bound = [v for v, n in marked_vals.items() if occ.get(v, 0) >= 2 and n >= occ[v]]
multi = [v for v in marked_vals if occ.get(v, 0) >= 2]
print(f'accepted-marked distinct values {len(marked_vals)}; of those occurring >=2 times in the letter: {len(multi)}; marked at EVERY occurrence: {len(bound)} {bound}')
# null: keep the number of marked occurrences per digit length, draw values at random among groups of that length
def draw():
    by_len = collections.defaultdict(list)
    for g in groups: by_len[len(g)].append(g)
    picks = collections.Counter()
    for r in acc:
        picks[rng.choice(by_len[len(r[2])])] += 1
    return sum(1 for v, n in picks.items() if occ[v] >= 2 and n >= occ[v])
if acc:
    null = sorted(draw() for _ in range(2000))
    print(f'null (values shuffled within digit length, 2000 draws): mean {sum(null)/2000:.2f}, p95 {null[1899]}, max {null[-1]}; target {len(bound)}')
