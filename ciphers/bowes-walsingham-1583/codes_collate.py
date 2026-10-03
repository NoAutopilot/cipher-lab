#!/usr/bin/env python3
"""Gap 3 collation (GAPS59, 3 Oct 2026): every number codes_scan.py finds in the Surtees 1842 OCR, filtered for
non-codes (front matter, folio numbers, page headers, dates, years, sums, single digits), dated by the letter it sits
in, and collated per code across the Letter-Book. Writes codes_collation.tsv (one row per kept occurrence) and
codes_collation_filter.tsv (the dropped hits with the rule that dropped them). Same hits as codes_scan.tsv (asserted).
--check exits 1 if either file is stale. No identification is made here; codes.py holds the grades."""
import re, sys, csv, bisect, collections
T = open('corpus/correspondenceof00bowerich_djvu.txt', encoding='utf-8').read().split('\n')
HEAD = re.compile(r'BOWES\s+CORRESPONDENCE|^\s*\d+\s+[A-Z]\s*\d*\s*$|^\s*\d+\s*$')
LET = re.compile(r'^([CLXVI]{2,}[.IL]?)\s*[.—-]')
SKIP_AFTER = re.compile(r'^\s*(l\.|li\.|lib|pounds?|crowns?|marks?|men|horse|foot|days?|years?|miles?|s\.|d\.|th\b|st\b|hundred|thousand|francs|ells|shillings)', re.I)
MON = r'(jan|feb|mar|apr|may|maij|maii|jun|jul|aug|sep|oct|nov|dec)'
flat = []; letter = '?'; heads = []
for i, l in enumerate(T):
    m = LET.match(l)
    if m: letter = m.group(1); heads.append((i + 1, letter))
    if HEAD.search(l) or 'Letter-Book' in l or re.search(r'\bp\.\s*\d', l): continue
    flat.append((i + 1, letter, l))
text = ' '.join(l for _, _, l in flat); pos = []; c = 0
for n, let, l in flat: pos.append((c, n, let)); c += len(l) + 1
starts = [p[0] for p in pos]
# letter dates: first year 1577-1584 in the heading line and the next 4 lines (old-style years as printed)
date = {}
for ln, let in heads:
    blk = re.sub(r'\s+', ' ', ' '.join(T[ln - 1:ln + 4]))
    y = re.search(r'15\s?([78]\d)', blk)
    if y and 77 <= int(y.group(1)) <= 84: date[ln] = '15' + y.group(1)
hl = [h[0] for h in heads]
def letter_of(line):
    k = bisect.bisect_right(hl, line) - 1
    if k < 0: return ('?', 0, '?')
    y = date.get(heads[k][0])
    if not y:  # heading carries no year: the previous dated letter's year, marked ~
        y = next(('~' + date[h[0]] for h in reversed(heads[:k]) if h[0] in date), '?')
    return (heads[k][1], heads[k][0], y)
MANUAL = {  # (code, OCR line): reason -- read by eye, GAPS59 3 Oct 2026; OCR damage the regexes above miss
 ('16', 3402): 'date (16*th April)', ('580', 3723): 'year (1.580)', ('13', 23526): 'sum (13,633 English)',
 ('170', 10858): 'page number', ('24', 9214): 'count (the 24 gentlemen, LXVIII)', ('24', 9944): 'date (24 Oc-tober)', ('01', 4826): 'OCR of "of"', ('381', 21732): 'page number', ('477', 26689): 'page number', ('509', 28328): 'page number'}
def rule(v, pre, post, near, line):
    for (c, ln), why in MANUAL.items():
        if c == v and abs(ln - line) <= 3: return 'manual: ' + why
    if line < 2000: return 'front-matter/introduction'
    if re.search(r'fo[lb1]\.?,?\s*$', pre, re.I): return 'folio'
    if re.search(r'C\s*O\s*R\s*R|ORRES|RRESP|CORIt|COKKES|ON\s*DKX|O\w?R\w{0,2}E\w{0,3}[SP]\w{0,3}[OX]\w*DE[NX]\w*CE|DEXCE|conREs', near, re.I): return 'page-header'
    if re.search(r'NRLF|LIBRARY|BELOW|Richmond|loans|\(4/94\)', near): return 'back matter'
    if re.search(r'(MS|Art)\.?\s*\S{0,6}\s*$', pre) or re.search(r'Letter-Book', near): return 'reference'
    if re.search(r'\bMr\.\s*$', pre): return 'initial'
    if re.match(r"\s*(or\s+\d|/|'\d|\.\s*\d+s|\.\s*;|\s*gentlemen|souldiers|horsmen|horsemen|fotemen|footmen|shot\b|Englishmen|French\s+crowns|persons|houses|dead\b|toonnes|servants)", post) or re.search(r'\d\s+or\s*$', pre): return 'count or sum'
    if re.match(r'\s*(of\s+)?(the\s+)?' + MON, post, re.I) or re.search(MON + r'\w*\.?,?\s*$', pre, re.I): return 'date'
    if re.match(r'\s*,\s*\d{3}', post) or re.search(r'\d\s*[,?]\s*$', pre): return 'sum (,000)'
    if (v == '15' and re.match(r'\s*\d\d\b', post)) or (len(v) == 2 and re.search(r'\b15\s*$', pre)): return 'year split'
    if re.match(r'\s*\[?\s*-\s*\d', post) or re.match(r'\s*\]', post): return 'year'
    if re.search(r'\bc\.?\s*$|\bcap\.?\s*$|\bp\.\s*$', pre, re.I): return 'reference'
    if len(v) == 1: return 'single digit'
    return ''
keep, drop = [], []
for m in re.finditer(r'(?<![\w/])(\d{1,4}|1S9|8/0)(?![\w/])', text):
    num = m.group(1).replace('S', '8').replace('/', '7')
    if 1500 <= int(num) <= 1699: continue
    if SKIP_AFTER.match(text[m.end():m.end() + 12]): continue
    k = bisect.bisect_right(starts, m.start()) - 1; line = pos[k][1]
    pre = text[max(0, m.start() - 16):m.start()]; post = text[m.end():m.end() + 30]
    near = text[max(0, m.start() - 40):m.end() + 40]
    ctx = re.sub(r'\s+', ' ', text[max(0, m.start() - 100):m.end() + 100])
    let, hline, yr = letter_of(line)
    r = rule(num, pre, post, near, line)
    (drop if r else keep).append([num, m.group(1), str(line), let, yr, r, ctx])
scan = list(csv.DictReader(open('codes_scan.tsv'), delimiter='\t'))
assert len(scan) == len(keep) + len(drop), (len(scan), len(keep), len(drop))
o1 = 'code\tprinted\tline\tletter\tyear\tcontext\n' + ''.join('\t'.join(r[:5] + [r[6]]) + '\n' for r in keep)
o2 = 'code\tprinted\tline\tletter\tyear\tdropped_by\tcontext\n' + ''.join('\t'.join(r) + '\n' for r in drop)
if '--check' in sys.argv:
    ok = open('codes_collation.tsv').read() == o1 and open('codes_collation_filter.tsv').read() == o2
    print('OK: codes_collation current' if ok else 'STALE: codes_collation'); sys.exit(0 if ok else 1)
open('codes_collation.tsv', 'w').write(o1); open('codes_collation_filter.tsv', 'w').write(o2)
print(len(scan), 'scan hits;', len(keep), 'kept;', dict(collections.Counter(r[5] for r in drop)))
