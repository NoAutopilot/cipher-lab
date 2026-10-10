"""Find runs of numerals inside otherwise clear printed text, in Internet Archive full text (_djvu.txt).

  python3 tools/ia_numeral_runs.py IDENTIFIER [...] [--cache DIR] [--min-tokens 6] [--share 0.7] [--tsv OUT]

Downloads IDENTIFIER_djvu.txt once per item (cached), marks lines with at least --min-tokens tokens of which at
least --share are 1-4 digit numerals, groups marked lines fewer than four lines apart, and scores each cluster:
numerals, distinct values, repeat rate (cipher repeats; index and table columns mostly do not) and prose words of
4+ letters within three lines either side. One TSV row per cluster with 240 characters of context. Scripts read,
models judge. Lending-only items answer 403 and are reported, not retried. Exit 0 always.

--inline-run K (THUR-B146, 10 Oct 2026) also marks a line holding K consecutive numeral tokens inside prose, for editions
that print short cipher runs mid-sentence (Birch 1742 vol. 4). Meant to catch: "215. 345. 196. 501. 105." inside a prose line.
Must NOT flag: one stray number or a date ("in 2 dayes", "April 5, 1656") -- K defaults to off and is >= 4 in use.

--markers (MQS-IA-MARKERS, 9 Oct 2026; research/MARY-STUART-TALK-2026-10-09.tsv row M04; after Lasry, Biermann and
Tomokiyo 2023, Cryptologia 47:2, p.108 n.38: Labanoff 1844 printed a cipher passage as ellipses) also reports clusters
of printed gap markers, where an edition left the cipher out instead of printing its numerals: an ellipsis (three or
more dots, optionally spaced, or the ellipsis character) and a bracketed cipher note ([en chiffre], (in cipher),
[Chiffre], weight 3). Marked lines fewer than --marker-gap lines apart form a cluster, flagged at --min-markers.
Meant to catch: three ellipses within a few lines of a letter; one bracketed "en chiffre" note.
Must NOT flag: a table of contents of dot leaders ending in a page number; one isolated editorial ellipsis.
Rows get kind=marker (numeral rows kind=numeral, only when --markers is given; without it output is unchanged).
Grade and evidence: tools/data/tool_shelf.tsv; pre-registration tools/tests/PREREG-MQS-IA-MARKERS.md.
"""
import argparse, os, re, sys, time, urllib.request, urllib.error

NUM = re.compile(r'^\d{1,4}[.,;:]?$')
WORD = re.compile(r'^[A-Za-zÀ-ſ]{4,}[.,;:]?$')
DOTS = re.compile(r'(?:\.\s?){2,}\.|…')
LEADER = re.compile(r'(?:\.\s?){2,}\.?\s*(?:p\.\s*)?(?:\d{1,4}|[ivxlcdm]{1,7})\.?\s*$', re.I)
NOTE = re.compile(r'[\[(][^\])]{0,40}(?:chiffr|cipher|cypher|ziffer|cifra)[^\])]{0,40}[\])]', re.I)

def marker_count(line):
    """Weighted gap markers on one OCR line: ellipses 1 each (dot leaders to a page number excluded), cipher notes 3."""
    notes = len(NOTE.findall(line))
    body = LEADER.sub('', line)
    return len(DOTS.findall(body)) + 3 * notes

def marker_clusters(lines, gap):
    out = []
    for i, l in enumerate(lines):
        m = marker_count(l)
        if m:
            if out and i - out[-1][0][-1] < gap:
                out[-1][0].append(i)
                out[-1][1] += m
            else:
                out.append([[i], m])
    return [(c, m) for c, m in out]

def fetch(ident, cache):
    path = os.path.join(cache, ident + '_djvu.txt')
    if os.path.exists(path):
        return open(path, encoding='utf-8', errors='ignore').read(), 'cached'
    url = 'https://archive.org/download/%s/%s_djvu.txt' % (ident, ident)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (cipher-lab ia_numeral_runs)'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            text = r.read().decode('utf-8', errors='ignore')
    except urllib.error.HTTPError as e:
        return None, 'HTTP %d' % e.code
    os.makedirs(cache, exist_ok=True)
    open(path, 'w', encoding='utf-8').write(text)
    time.sleep(1.5)
    return text, 'fetched'

def longest_run(tk):
    best = cur = 0
    for t in tk:
        cur = cur + 1 if NUM.match(t) else 0
        best = max(best, cur)
    return best

def clusters(lines, min_tokens, share, inline_run=0):
    out = []
    for i, l in enumerate(lines):
        tk = l.split()
        if (len(tk) >= min_tokens and sum(1 for t in tk if NUM.match(t)) / len(tk) >= share) \
                or (inline_run and longest_run(tk) >= inline_run):
            if out and i - out[-1][-1] < 4:
                out[-1].append(i)
            else:
                out.append([i])
    return out

def score(lines, c):
    nums = [t.rstrip('.,;:') for i in range(c[0], c[-1] + 1) for t in lines[i].split() if NUM.match(t)]
    seen, rep = set(), 0
    for n in nums:
        rep += n in seen
        seen.add(n)
    ctx = [lines[i] for i in range(max(0, c[0] - 3), min(len(lines), c[-1] + 4)) if i not in c]
    prose = sum(1 for l in ctx for t in l.split() if WORD.match(t))
    return len(nums), len(seen), rep / len(nums) if nums else 0.0, prose

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ids', nargs='+')
    ap.add_argument('--cache', default='sources/ia-fulltext')
    ap.add_argument('--min-tokens', type=int, default=6)
    ap.add_argument('--share', type=float, default=0.7)
    ap.add_argument('--tsv', default='-')
    ap.add_argument('--inline-run', type=int, default=0, help='also mark a line holding this many consecutive numeral tokens inside prose (THUR-B146, 10 Oct 2026; default off)')
    ap.add_argument('--markers', action='store_true', help='also report clusters of printed gap markers (ellipses, [en chiffre])')
    ap.add_argument('--marker-gap', type=int, default=6, help='marked lines fewer than this apart join a cluster')
    ap.add_argument('--min-markers', type=int, default=3, help='weighted marker count that flags a cluster')
    a = ap.parse_args()
    out = sys.stdout if a.tsv == '-' else open(a.tsv, 'w', encoding='utf-8')
    out.write('identifier\tline\tn_lines\tnumerals\tdistinct\trepeat_rate\tprose_words\tcontext%s\n'
              % ('\tkind\tmarkers' if a.markers else ''))
    for ident in a.ids:
        text, how = fetch(ident, a.cache)
        if text is None:
            print('%s: %s, skipped' % (ident, how), file=sys.stderr)
            continue
        lines = text.split('\n')
        cs = clusters(lines, a.min_tokens, a.share, a.inline_run)
        print('%s: %s, %d lines, %d clusters' % (ident, how, len(lines), len(cs)), file=sys.stderr)
        for c in cs:
            n, d, r, p = score(lines, c)
            ctx = ' / '.join(lines[i].strip() for i in range(max(0, c[0] - 1), min(len(lines), c[-1] + 2)))
            out.write('%s\t%d\t%d\t%d\t%d\t%.2f\t%d\t%s%s\n' % (ident, c[0] + 1, len(c), n, d, r, p,
                                                               ctx[:240].replace('\t', ' '),
                                                               '\tnumeral\t' if a.markers else ''))
        if a.markers:
            mc = [(c, m) for c, m in marker_clusters(lines, a.marker_gap) if m >= a.min_markers]
            print('%s: %d marker clusters flagged' % (ident, len(mc)), file=sys.stderr)
            for c, m in mc:
                ctx = ' / '.join(lines[i].strip() for i in range(c[0], c[-1] + 1))
                out.write('%s\t%d\t%d\t0\t0\t0.00\t0\t%s\tmarker\t%d\n' % (ident, c[0] + 1, c[-1] - c[0] + 1,
                                                                     ctx[:240].replace('\t', ' '), m))

if __name__ == '__main__':
    main()
