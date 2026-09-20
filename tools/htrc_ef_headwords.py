#!/usr/bin/env python3
"""Locate headwords in a HathiTrust volume through the HTRC Extracted Features API, without touching HathiTrust's
Cloudflare-protected site.

  python3 tools/htrc_ef_headwords.py HTID [HTID ...] [--words alphabet,cipher,...] [--target word=page,...]
                                     [--cache DIR] [--json]

For each volume it downloads the per-page token counts (https://data.htrc.illinois.edu/ef-api/volumes/HTID/pages,
pos=false; about 1-3 MB for a 500-page book, cached in --cache), prints the page count and the median tokens and
lines per page, and for each word the scan sequence numbers (seq, 1-based, front matter included) of the pages on
which the word occurs as a token. Matching is case-insensitive and ignores a trailing hyphen or full stop (dictionary
headwords are set in capitals, often syllabified: "AL-PHA-BET" is not matched, "ALPHABET" and "Alphabet" are).

With --target (default: the Wellington 1812 codebook's page table for the words listed below) it fits a constant
offset seq = printed page + k over the words found, using the first seq of each word (the headword page comes before
the pages where the word is used in definitions only when the word is rare; for common words use the discriminator
list), and reports the residuals, so a candidate whose every residual is zero is the same setting as the target.

The EF dataset covers every HathiTrust volume, in-copyright ones included, so a result here is independent of the
volume's view status. Exit 0 always; the verdict is in the output, not the exit code.
"""
import argparse, json, os, re, statistics, sys, urllib.request

EF = 'https://data.htrc.illinois.edu/ef-api/volumes/%s/pages?pos=false'
META = 'https://data.htrc.illinois.edu/ef-api/volumes/%s/metadata'

# Discriminators from ciphers/wellington-maitland-1812/DICTIONARY.md section 1: word -> printed page in the target.
TARGET = {'alphabet': 14, 'amount': 16, 'another': 19, 'cipher': 79, 'early': 146, 'enable': 151, 'event': 158,
          'fortunate': 184, 'height': 205, 'occupy': 288, 'outside': 297, 'period': 308, 'provision': 332,
          'quarter': 336, 'rejoin': 346, 'require': 349, 'southward': 388, 'spelling': 389, 'supply': 400,
          'theft': 405, 'town': 409, 'troop': 412, 'westward': 432, 'younker': 438, 'youth': 438}


def fetch(url, cache):
    if cache:
        os.makedirs(cache, exist_ok=True)
        path = os.path.join(cache, re.sub(r'[^A-Za-z0-9._$-]', '_', url.split('/volumes/')[1]))
        if os.path.exists(path):
            return json.load(open(path))
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = json.load(urllib.request.urlopen(req, timeout=300))
    if cache:
        json.dump(data, open(path, 'w'))
    return data


# Rare words whose first occurrence in a dictionary is its own headword page: used to fit the offset.
RARE = ('cipher', 'occupy', 'outside', 'rejoin', 'southward', 'westward', 'younker', 'fortunate', 'provision', 'supply')
ALIAS = {'cypher': 'cipher', 'cyphers': 'cipher', 'to-rejoin': 'rejoin'}


def norm(tok):
    w = tok.lower().rstrip('.-,;:').lstrip('-')
    return ALIAS.get(w, w)


def analyse(htid, words, target, cache):
    meta = fetch(META % htid, cache)
    if meta.get('code') != 200:
        return {'htid': htid, 'error': meta.get('message')}
    m = meta['data']['metadata']
    pages = fetch(EF % htid, cache)['data']['pages']
    body_tokens = [p['tokenCount'] for p in pages if p['tokenCount'] > 50]
    body_lines = [p['lineCount'] for p in pages if p['tokenCount'] > 50]
    found = {}
    for p in pages:
        seq = int(p['seq'])
        for part in ('header', 'body', 'footer'):
            sec = p.get(part)
            if not sec:
                continue
            for tok, n in (sec.get('tokensCount') or {}).items():
                w = norm(tok)
                if w in words:
                    found.setdefault(w, []).append(seq)
    out = {'htid': htid, 'title': m.get('title'), 'pubDate': m.get('pubDate'), 'pubPlace': m.get('pubPlace', {}).get('name'),
           'publisher': m.get('publisher', {}).get('name') if isinstance(m.get('publisher'), dict) else m.get('publisher'),
           'pageCount': len(pages), 'median_tokens': statistics.median(body_tokens) if body_tokens else 0,
           'median_lines': statistics.median(body_lines) if body_lines else 0,
           'seqs': {w: sorted(set(s)) for w, s in found.items()}}
    # Constant-offset fit: k from the first occurrence of the rare words (their headword page), then for every word
    # the occurrence nearest to target + k (common words also appear in the grammar and in other entries).
    rare = [(target[w], out['seqs'][w][0]) for w in RARE if w in target and w in out['seqs']]
    if len(rare) >= 3:
        k = statistics.median([s - pg for pg, s in rare])
        out['offset'] = k
        out['fit_words'] = len(rare)
        out['residuals'] = {w: min((s - target[w] - k for s in out['seqs'][w]), key=abs) for w in target if w in out['seqs']}
        out['max_abs_residual'] = max(abs(v) for v in out['residuals'].values())
        out['within2'] = sum(1 for v in out['residuals'].values() if abs(v) <= 2)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('htids', nargs='+')
    ap.add_argument('--words', default=None, help='comma list; default: the target words')
    ap.add_argument('--target', default=None, help='word=page,... ; default: Wellington 1812 table')
    ap.add_argument('--cache', default=os.environ.get('EF_CACHE', ''))
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()
    target = dict(TARGET)
    if a.target:
        target = {k: int(v) for k, v in (kv.split('=') for kv in a.target.split(','))}
    words = set(a.words.split(',')) if a.words else set(target)
    for htid in a.htids:
        try:
            r = analyse(htid, words, target, a.cache)
        except Exception as e:
            r = {'htid': htid, 'error': str(e)}
        if a.json:
            print(json.dumps(r))
            continue
        if 'error' in r:
            print('%s: ERROR %s' % (htid, r['error']))
            continue
        print('%s | %s | %s %s %s | %d scans, median %s tokens / %s lines per page' % (
            htid, (r['title'] or '')[:70], r['pubDate'], r['pubPlace'], (r['publisher'] or '')[:30], r['pageCount'],
            r['median_tokens'], r['median_lines']))
        for w in sorted(words, key=lambda w: target.get(w, 0)):
            s = r['seqs'].get(w, [])
            print('   %-10s target %3s  seq %s' % (w, target.get(w, '-'), ' '.join(map(str, s[:8])) + (' ...' if len(s) > 8 else '')))
        if 'offset' in r:
            print('   offset seq-page = %s from %d rare words; nearest-occurrence residuals: %s ; max |res| = %s ; %d/%d within 2' % (
                r['offset'], r['fit_words'], ' '.join('%s%+d' % (w, v) for w, v in r['residuals'].items()),
                r['max_abs_residual'], r['within2'], len(r['residuals'])))
        else:
            print('   fewer than 3 rare discriminators found: no offset fit (not a full English dictionary of this kind, or OCR too poor)')


if __name__ == '__main__':
    main()
