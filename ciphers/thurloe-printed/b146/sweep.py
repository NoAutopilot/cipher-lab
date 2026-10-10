"""THUR-B146 sweep: group ia_numeral_runs --inline-run 4 clusters of Birch 1742 vols into letters.

python3 b146/sweep.py [--check]   (reads the IA djvu cache in $B146_CACHE; manifest.tsv holds sha1s)
Declared filter (before vols 1/4/6 were read): cluster numerals >= 10 and outside the volume's index.
Pure text work; no decoding. Output: hits.tsv (one row per letter group), control.tsv (positive controls).
"""
import csv, os, re, statistics, sys, subprocess
C = os.environ.get('B146_CACHE')
HERE = os.path.dirname(os.path.abspath(__file__))
V6 = 'bim_eighteenth-century_a-collection-of-the-stat_thurloe-john_1742_6'
VOLS = {'1': ('collectionofstat01thur', 66310), '3': ('collectionofstat03thur', 10**9),
        '4': ('collectionofstat04thur', 74452), '6': (V6, 104842)}
MONTH = re.compile(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|Januar|Febr|Marc|Apri|June|July|Augu|Sept|Octo|Nove|Dece)\w*\.?\s*,?\s*\d', re.I)
HEAD = re.compile(r"^[\s\W]{0,3}(?:[A-Z][\w.',&;\- ]{2,}?\bto\b[\w.',&;\- ]{3,}|An? (?:intercepted )?letter[\w.',&;\- ]{0,60}|Intelligence[\w.',&;\- ]{0,60})\.?\s*$")
KEYS = [('blake', 'key_blake*.tsv'), ('mountagu|montagu', 'key_montagu*.tsv'), ('fauconberg', 'key_fauconberg*.tsv'),
        ('downing', 'key_downing.tsv'), ('lockhart', 'key_lockhart.tsv'), ('butler', 'key_butler.tsv'),
        ('stamford|w\\. ?s\\.|calais', 'pool_1654/key_stamford.tsv'), ('manning|johnson|burton', 'key_johnson1/2.tsv, key_burton.tsv'),
        ('steele', 'key_steele.tsv')]

def pagemap(lines):
    hd = [i for i, l in enumerate(lines) if re.search(r'STATE\s*PAPERS\s*OF|JOHN\s*THURLOE|JohN\s*THURLOE', l, re.I) and len(l) < 70]
    vals = []
    for k, i in enumerate(hd):
        m = re.findall(r'\b[0-9liIoO]{1,4}\b', lines[i])
        v = None
        if m:
            t = m[0] if re.match(r'\s*[0-9liIoO]', lines[i]) and 'STATE' in lines[i].upper() else m[-1]
            t = t.translate(str.maketrans('liIoO', '11100'))
            if t.isdigit(): v = int(t)
        vals.append(v)
    offs = [(k, v - k) for k, v in enumerate(vals) if v]
    pages = []
    for k in range(len(hd)):
        near = [o for kk, o in offs if abs(kk - k) <= 12]
        pages.append(k + int(statistics.median(near)) if near else None)
    return hd, pages, vals

def page_of(hd, pages, vals, ln):
    import bisect
    k = bisect.bisect_right(hd, ln) - 1
    if k < 0 or pages[k] is None or ln - hd[k] > 400: return ''
    return '%d%s' % (pages[k], '' if vals[k] == pages[k] else '~')

def heading_before(lines, ln, back=700):
    for i in range(ln, max(0, ln - back), -1):
        l = lines[i].strip()
        if 8 <= len(l) <= 90 and HEAD.match(l) and not re.search(r'\d{2}', l) and len(l.split()) <= 16 \
                and i > 0 and not lines[i - 1].strip():
            return i
    return None

def date_after(lines, h):
    for i in range(h, min(len(lines), h + 12)):
        if MONTH.search(lines[i]) and re.search(r'1[67]\d\d|\[\d{4}|\b16\b', lines[i]): return lines[i].strip()[:60]
    for i in range(h, min(len(lines), h + 12)):
        if MONTH.search(lines[i]): return lines[i].strip()[:60]
    return ''

def gloss(lines, c0, c1, h=None):
    """printed decipherment, two independent signs: (a) 'decipher' wording from the letter heading to c1+40 (cap 450 lines);
    (b) interlinear alternation: >= 60% of the numeral lines (>= 5 numerals) in the cluster window have a digit-free
    neighbour line of >= 3 tokens (the gloss row Birch prints between cipher rows)."""
    lo = h if h is not None and c0 - h <= 450 else max(0, c0 - 6)
    txt = ' '.join(lines[lo:c1 + 40])
    sign = []
    if re.search(r'de-?\s?c[iy]\s?ph|dec\s?y\s?ph', txt, re.I): sign.append('decipher-word')
    num_l = [i for i in range(max(0, c0 - 1), min(len(lines), c1 + 2)) if sum(1 for t in lines[i].split() if re.match(r'^\d{1,4}[.,;:\-]?$', t)) >= 5]
    def free(i):
        return 0 <= i < len(lines) and lines[i].strip() and not re.search(r'\d', lines[i]) and len(lines[i].split()) >= 3
    alt = sum(1 for i in num_l if free(i - 1) or free(i + 1))
    if num_l and alt / len(num_l) >= 0.6: sign.append('interlinear-alt')
    return '+'.join(sign) or 'no'

def load(vol):
    ident, idx = VOLS[vol]
    lines = open(os.path.join(C, ident + '_djvu.txt'), encoding='utf-8', errors='ignore').read().split('\n')
    rows = [r for r in csv.DictReader(open(os.path.join(C, 'runs_inline.tsv')), delimiter='\t') if r['identifier'] == ident]
    return ident, idx, lines, rows

def groups(vol, th=10):
    ident, idx, lines, rows = load(vol)
    hd, pages, vals = pagemap(lines)
    G = {}
    for r in rows:
        ln = int(r['line']) - 1
        if int(r['numerals']) < th or ln + 1 >= idx: continue
        h = heading_before(lines, ln)
        key = h if h is not None else ('nohead', ln // 400)
        g = G.setdefault(key, dict(vol=vol, ident=ident, head=h, cl=[]))
        g['cl'].append((ln, int(r['n_lines']), int(r['numerals']), int(r['distinct']), float(r['repeat_rate']), int(r['prose_words'])))
    out = []
    for key, g in G.items():
        h = g['head']; cl = g['cl']
        c0 = min(c[0] for c in cl); c1 = max(c[0] + c[1] for c in cl)
        htxt = lines[h].strip() if h is not None else ''
        key_hit = ', '.join(k for pat, k in KEYS if re.search(pat, htxt, re.I)) or ''
        gl = gloss(lines, c0, c1, h)
        out.append(dict(vol=vol, page=page_of(hd, pages, vals, c0), line_first=c0 + 1, line_last=c1, heading=htxt[:90],
                        date=date_after(lines, h) if h is not None else '', n_clusters=len(cl), numerals=sum(c[2] for c in cl),
                        longest_cluster=max(c[2] for c in cl), max_repeat=max(c[4] for c in cl), printed_decipherment=gl,
                        shared_key=key_hit, read_check=READ.get((vol, c0 + 1), ''),
                        on_file=ONFILE_V1 if FAMILY.search(htxt) and vol == '1' else ''))
    return sorted(out, key=lambda r: r['line_first'])

# Worker's reading of the OCR text around a hit (no image, no vision call), keyed by (vol, line_first).
READ = {
 ('6', 86578): 'gloss: interlinear gloss words between the numeral rows (OCR-garbled) -> printed decipherment',
 ('1', 62868): 'gloss: spaced-letter interlinear rows under the numerals -> printed decipherment',
 ('6', 35425): 'gloss: interlinear word fragments between rows -> printed decipherment (probable)',
 ('6', 36187): 'gloss: interlinear fragments (mentioned / in that business / person employed / jealousy of) -> printed decipherment (probable)',
 ('1', 32198): 'no gloss rows seen: numerals inline inside the printed English summary of an intercepted letter',
 ('1', 31246): 'no gloss rows seen (not read beyond the cluster line)',
 ('1', 43962): 'no gloss rows seen; this is the vol. 1 control cipher of RETRO-2026-09-23 s.4A (sources/ia-fulltext/NOTES.md)',
 ('6', 25671): 'OCR is symbol noise on this leaf; cannot tell from text -> page image needed',
 ('6', 74562): 'OCR is symbol noise on this leaf; cannot tell from text -> page image needed',
 ('6', 77385): 'OCR is symbol noise around the cluster; cannot tell from text -> page image needed',
 ('6', 75081): 'OCR is symbol noise around the cluster; cannot tell from text -> page image needed',
}
FAMILY = re.compile(r'Beverning|Vande\s+Perre|de\s+Witt|Dutch\s+amb|Nieuport|Newport|De\s+Groot', re.I)
ONFILE_V1 = 'Beverning/Vande Perre 1653 family is on file (CATALOG.md:139, LANDSCAPE.md:43)'
COLS = 'vol page line_first line_last heading date n_clusters numerals longest_cluster max_repeat printed_decipherment shared_key read_check on_file'.split()

def control():
    """Vol 3: the folder's own P4-P10, P26-P28 windows (index.tsv). Per volume: KH2-F / THU-1 known-item windows."""
    idx = {r['row']: r for r in csv.DictReader(open(os.path.join(HERE, '..', 'index.tsv')), delimiter='\t')}
    known = [('3', 'P%d' % n, *map(int, idx['P%d' % n]['window_lines'].split('-'))) for n in (4, 5, 6, 7, 8, 9, 10, 26, 27, 28)]
    known += [('4', 'M-Lyons51359', 51359, 51611), ('4', 'M-Lagos60576', 60576, 60618), ('4', 'Blake55548', 55548, 55911),
              ('1', 'M1-19May1656', 62335, 62563), ('1', 'M2-11Sep1656', 62564, 62798),
              ('6', 'Downing-Dec1657', 99333, 99732), ('6', 'Downing-Lockhart92632', 92632, 92700), ('6', 'Downing-Lockhart94019', 94019, 94100)]
    res, cache = [], {}
    for vol, name, a, b in known:
        G = cache.setdefault(vol, groups(vol))
        hit = [g for g in G if g['line_last'] >= a - 5 and g['line_first'] <= b + 5]
        res.append(dict(vol=vol, item=name, window='%d-%d' % (a, b), found='yes' if hit else 'no',
                        decipherment_flag=';'.join(sorted({g['printed_decipherment'] for g in hit})) or '-', groups_hit=len(hit)))
    return res

if __name__ == '__main__':
    check = '--check' in sys.argv
    allr = []
    for v in ('1', '4', '6'): allr += groups(v)
    ctl = control()
    import io
    def dump(rows, cols):
        b = io.StringIO(); w = csv.DictWriter(b, cols, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows)
        return b.getvalue()
    for name, txt in (('hits.tsv', dump(allr, COLS)), ('control.tsv', dump(ctl, list(ctl[0])))):
        path = os.path.join(HERE, name)
        if check:
            if not os.path.exists(path) or open(path).read() != txt:
                print('STALE', name); sys.exit(1)
        else:
            open(path, 'w').write(txt)
    if check: print('ok'); sys.exit(0)
    g3 = groups('3')
    print('groups per vol', {v: sum(1 for r in allr if r['vol'] == v) for v in '146'}, 'vol3', len(g3))
    for r in ctl: print(r)
