Read CLAUDE.md (rules 1, 3, 10; Access playbook good-citizen rule) and RETRO-2026-09-23.md section 4 A.
Build the list of public-domain editions named there (identifiers from archive.org advancedsearch, one call per
title). Run `tools/ia_numeral_runs.py` over all of them into sources/ia-fulltext/runs.tsv. Controls first: Thurloe
vol. 1, the 1819 Catinat Mémoires and Rommel 1840 must show their printed cipher; if not, stop and report. Keep
clusters with repeat_rate >= 0.3, numerals >= 15, prose_words >= 5; judge each from its context line only, marking
cipher-with-decipherment, cipher-without-decipherment, table, noise. For each cipher-without-decipherment cluster,
grep sources/cryptiana/, and fresh clones of both solver repositories, for the edition and the letter's date. Write
QUEUE.md section "Printed ciphertext (detector test of <date>)" with one row per surviving cluster; report
precision in the top 50, control recall, and survivors. Never promote, never solve. + common tail.
++ b/tools/ia_numeral_runs.py
#!/usr/bin/env python3
"""Find runs of numerals inside otherwise clear printed text, in Internet Archive full text (_djvu.txt).

  python3 tools/ia_numeral_runs.py IDENTIFIER [...] [--cache DIR] [--min-tokens 6] [--share 0.7] [--tsv OUT]

Downloads IDENTIFIER_djvu.txt once per item (cached), marks lines with at least --min-tokens tokens of which at
least --share are 1-4 digit numerals, groups marked lines fewer than four lines apart, and scores each cluster:
numerals, distinct values, repeat rate (cipher repeats; index and table columns mostly do not) and prose words of
4+ letters within three lines either side. One TSV row per cluster with 240 characters of context. Scripts read,
models judge. Lending-only items answer 403 and are reported, not retried. Exit 0 always.
"""
import argparse, os, re, sys, time, urllib.request, urllib.error

NUM = re.compile(r'^\d{1,4}[.,;:]?$')
WORD = re.compile(r'^[A-Za-zÀ-ſ]{4,}[.,;:]?$')

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

def clusters(lines, min_tokens, share):
    out = []
    for i, l in enumerate(lines):
        tk = l.split()
        if len(tk) >= min_tokens and sum(1 for t in tk if NUM.match(t)) / len(tk) >= share:
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
    a = ap.parse_args()
    out = sys.stdout if a.tsv == '-' else open(a.tsv, 'w', encoding='utf-8')
    out.write('identifier\tline\tn_lines\tnumerals\tdistinct\trepeat_rate\tprose_words\tcontext\n')
    for ident in a.ids:
        text, how = fetch(ident, a.cache)
        if text is None:
            print('%s: %s, skipped' % (ident, how), file=sys.stderr)
            continue
        lines = text.split('\n')
        cs = clusters(lines, a.min_tokens, a.share)
        print('%s: %s, %d lines, %d clusters' % (ident, how, len(lines), len(cs)), file=sys.stderr)
        for c in cs:
            n, d, r, p = score(lines, c)
            ctx = ' / '.join(lines[i].strip() for i in range(max(0, c[0] - 1), min(len(lines), c[-1] + 2)))
            out.write('%s\t%d\t%d\t%d\t%d\t%.2f\t%d\t%s\n' % (ident, c[0] + 1, len(c), n, d, r, p,
                                                             ctx[:240].replace('\t', ' ')))

if __name__ == '__main__':
    main()
