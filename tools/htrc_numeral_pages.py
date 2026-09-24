#!/usr/bin/env python3
"""Flag probable printed-cipher pages in a HathiTrust volume from the Extracted Features (EF) API's
per-page token counts alone -- no word order, no page image, so a flag is a lead, not a reading.

  python3 tools/htrc_numeral_pages.py HTID [HTID ...] [--cache DIR] [--tsv OUT.tsv]
                                       [--min-instances 25] [--min-distinct 12] [--min-repeat 0.3]
                                       [--tail-frac 0.08] [--cluster-gap 3] [--json]

For each page it sums header+body+footer tokensCount, keeps tokens that are bare 1-4 digit numerals,
drops a plausible 4-digit year (1400-1930) and a single numeral within 60 of the page's own scan
sequence (a likely running page number), and scores the rest: instances (numeral token count, with
repeats), distinct (numeral types), repeat_rate = (instances - distinct) / instances. A page is
flagged when instances >= --min-instances, distinct >= --min-distinct and repeat_rate >= --min-repeat
(a cipher repeats a small alphabet of code numbers; a table of contents or index mostly does not).

Two pre-filters drop likely false positives before they are reported (CLAUDE.md's printed-ciphertext
detector lessons of 24 Sept 2026, ported from tools/ia_numeral_runs.py's OCR-line version):
  - the last --tail-frac of the volume by page count (back-of-volume indexes/Regesten);
  - a page whose numeral values, sorted, rise in mostly increasing, evenly spaced steps (a table of
    contents or a page-number list), via --cluster-gap-free ascending_run().

Flagged pages within --cluster-gap of each other (by scan sequence) are merged into one cluster row
in the TSV/--json output: htid, start_seq, end_seq, n_pages, instances, distinct, repeat_rate,
top_values (the most frequent numeral tokens on the cluster's pages). Exit code is always 0; the
verdict is in the output. Judging a cluster as a real cipher (vs. false positive) needs the page
image or the OCR text nearby -- this script only narrows where to look (sources/htrc/NOTES.md).
"""
import argparse
import json
import os
import re
import statistics
import sys
import time
import urllib.request

EF = 'https://data.htrc.illinois.edu/ef-api/volumes/%s/pages?pos=false'
NUM_RE = re.compile(r'^\d{1,4}$')
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')


def fetch(htid, cache):
    if cache:
        os.makedirs(cache, exist_ok=True)
        path = os.path.join(cache, re.sub(r'[^A-Za-z0-9._$-]', '_', htid) + '.json')
        if os.path.exists(path):
            return json.load(open(path))
    req = urllib.request.Request(EF % htid, headers={'User-Agent': UA})
    data = json.load(urllib.request.urlopen(req, timeout=300))
    if cache:
        json.dump(data, open(path, 'w'))
    return data


def page_numerals(page, seq):
    """Sum numeral tokens across header/body/footer for one EF page dict."""
    counts = {}
    total_tokens = 0
    for part in ('header', 'body', 'footer'):
        sec = page.get(part)
        if not sec:
            continue
        total_tokens += sec.get('tokenCount', 0)
        for tok, n in (sec.get('tokensCount') or {}).items():
            counts[tok] = counts.get(tok, 0) + n
    numerals = {}
    for tok, n in counts.items():
        if not NUM_RE.match(tok):
            continue
        v = int(tok)
        if len(tok) == 4 and 1400 <= v <= 1930:
            continue  # plausible year, not a cipher figure
        numerals[v] = numerals.get(v, 0) + n
    running = [v for v, n in numerals.items() if n == 1 and abs(v - seq) <= 60]
    if len(running) == 1:
        del numerals[running[0]]
    instances = sum(numerals.values())
    distinct = len(numerals)
    repeat_rate = (instances - distinct) / instances if instances else 0.0
    return {'instances': instances, 'distinct': distinct, 'repeat_rate': repeat_rate,
            'values': numerals, 'total_tokens': total_tokens}


def ascending_run(values, repeat_rate, max_median_gap=30, min_len=8, min_monotone_frac=0.85,
                   max_repeat_for_filter=0.5):
    """True if the sorted distinct values look like a page-number list (a table of contents/index).

    Tuned once against the Thurloe vol. 1 control (24 Sept 2026): EF gives no word order, so "ascending"
    here can only mean "the set of distinct numeral values, sorted, rises in small, even steps" -- and a
    compact homophonic/nomenclator alphabet (e.g. 0-99) has exactly that shape purely because it is
    bounded, with no relation to a real table of contents. The untuned filter dropped this volume's known
    cipher clusters (seq 372, 757, 759, 761, 762; repeat_rate 0.64-0.80) as false "ascending runs". A real
    index/table cites most page numbers once (repeat_rate typically 0.1-0.3 on this volume's own back
    matter, seq ~800-830); a reused code alphabet does not. Gating this filter to repeat_rate below
    max_repeat_for_filter keeps it useful for borderline table-like pages without destroying a dense
    cipher's true positive -- see sources/htrc/NOTES.md section 1.
    """
    if repeat_rate >= max_repeat_for_filter:
        return False
    vs = sorted(values)
    if len(vs) < min_len:
        return False
    diffs = [b - a for a, b in zip(vs, vs[1:])]
    pos = sum(1 for d in diffs if d > 0)
    if pos / len(diffs) < min_monotone_frac:
        return False
    return statistics.median(diffs) <= max_median_gap


def score_pages(pages, min_instances, min_distinct, min_repeat, tail_frac):
    n = len(pages)
    cutoff = int(n * (1 - tail_frac))
    rows = []
    for i, p in enumerate(pages):
        seq = int(p['seq'])
        stats = page_numerals(p, seq)
        passes = (stats['instances'] >= min_instances and stats['distinct'] >= min_distinct
                  and stats['repeat_rate'] >= min_repeat)
        dropped_reason = None
        flagged = passes
        if passes and i >= cutoff:
            dropped_reason, flagged = 'tail-index', False
        elif passes and ascending_run(stats['values'].keys(), stats['repeat_rate']):
            dropped_reason, flagged = 'ascending-run', False
        rows.append({'seq': seq, 'index': i, 'passes_threshold': passes, 'flagged': flagged,
                     'dropped_reason': dropped_reason, **stats})
    return rows


def cluster(rows, gap):
    flagged = [r for r in rows if r['flagged']]
    flagged.sort(key=lambda r: r['seq'])
    clusters = []
    cur = []
    for r in flagged:
        if cur and r['seq'] - cur[-1]['seq'] > gap:
            clusters.append(cur)
            cur = []
        cur.append(r)
    if cur:
        clusters.append(cur)
    out = []
    for c in clusters:
        top = {}
        for r in c:
            for v, n in r['values'].items():
                top[v] = top.get(v, 0) + n
        top_sorted = sorted(top.items(), key=lambda kv: -kv[1])[:10]
        out.append({
            'start_seq': c[0]['seq'], 'end_seq': c[-1]['seq'], 'n_pages': len(c),
            'instances': sum(r['instances'] for r in c),
            'distinct': len(top),
            'repeat_rate': round(statistics.mean(r['repeat_rate'] for r in c), 3),
            'top_values': ','.join('%d:%d' % (v, n) for v, n in top_sorted),
        })
    return out


def analyse(htid, cache, min_instances, min_distinct, min_repeat, tail_frac, gap):
    data = fetch(htid, cache)
    if data.get('code') and data.get('code') != 200:
        return {'htid': htid, 'error': data.get('message', 'EF API error')}
    pages = data['data']['pages']
    rows = score_pages(pages, min_instances, min_distinct, min_repeat, tail_frac)
    dropped = sum(1 for r in rows if r['passes_threshold'] and not r['flagged'])
    clusters = cluster(rows, gap)
    return {'htid': htid, 'n_pages': len(pages), 'n_flagged_pages': sum(1 for r in rows if r['flagged']),
            'n_prefilter_dropped': dropped, 'clusters': clusters}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('htids', nargs='+')
    ap.add_argument('--cache', default=os.environ.get('EF_CACHE', ''))
    ap.add_argument('--tsv', default=None, help='write one row per cluster to this path')
    ap.add_argument('--min-instances', type=int, default=25)
    ap.add_argument('--min-distinct', type=int, default=12)
    ap.add_argument('--min-repeat', type=float, default=0.3)
    ap.add_argument('--tail-frac', type=float, default=0.08)
    ap.add_argument('--cluster-gap', type=int, default=3, help='max scan-seq gap to merge flagged pages')
    ap.add_argument('--sleep', type=float, default=1.5, help='seconds between EF fetches not already cached')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()

    results = []
    for i, htid in enumerate(a.htids):
        cached = a.cache and os.path.exists(os.path.join(a.cache, re.sub(r'[^A-Za-z0-9._$-]', '_', htid) + '.json'))
        if i > 0 and not cached:
            time.sleep(a.sleep)
        try:
            r = analyse(htid, a.cache, a.min_instances, a.min_distinct, a.min_repeat, a.tail_frac, a.cluster_gap)
        except Exception as e:
            r = {'htid': htid, 'error': str(e)}
        results.append(r)
        if a.json:
            print(json.dumps(r))
            continue
        if 'error' in r:
            print('%s: ERROR %s' % (htid, r['error']))
            continue
        print('%s | %d pages | %d flagged pages (%d dropped by pre-filter) | %d clusters' % (
            r['htid'], r['n_pages'], r['n_flagged_pages'], r['n_prefilter_dropped'], len(r['clusters'])))
        for c in r['clusters']:
            print('   seq %s-%s (%d pp) instances=%d distinct=%d repeat=%.2f top=%s' % (
                c['start_seq'], c['end_seq'], c['n_pages'], c['instances'], c['distinct'],
                c['repeat_rate'], c['top_values']))

    if a.tsv:
        with open(a.tsv, 'w') as fh:
            fh.write('htid\tstart_seq\tend_seq\tn_pages\tinstances\tdistinct\trepeat_rate\ttop_values\n')
            for r in results:
                if 'error' in r:
                    continue
                for c in r['clusters']:
                    fh.write('%s\t%d\t%d\t%d\t%d\t%d\t%.3f\t%s\n' % (
                        r['htid'], c['start_seq'], c['end_seq'], c['n_pages'], c['instances'],
                        c['distinct'], c['repeat_rate'], c['top_values']))

    return 0


if __name__ == '__main__':
    sys.exit(main())
