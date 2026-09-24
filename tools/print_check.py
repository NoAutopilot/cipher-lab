#!/usr/bin/env python3
"""Search decoded phrases in print: Internet Archive, HathiTrust (HTRC Extracted Features), Google Books, OpenAlex and
CrossRef, from one phrases file and one sources list, with a log of what could not be reached.

  python3 tools/print_check.py ciphers/<target> [--phrases phrases.txt] [--sources sources.tsv] [--source KIND:VALUE]
                               [--only ia,ia-global,htrc,gbooks,openalex,crossref] [--offline] [--cache DIR]
                               [--no-early-modern] [--max-requests 200]

  phrases.txt  one distinctive decoded phrase per line ('#' comments). Four to eight words that a printed edition would
               carry verbatim work best; spelling as decoded (u/v, i/j and long s are folded, accents ignored).
  sources.tsv  'kind<TAB>value[<TAB>note]', kinds:
                 ia        an Internet Archive identifier (edition, calendar, journal volume)
                 hathi     a HathiTrust catalogue record number     oclc   an OCLC number (both resolved to htids)
                 htid      a HathiTrust volume id                  gbooks  a Google Books volume id
                 openalex  keywords for a scholarship search       crossref keywords for a CrossRef search
Writes TARGET/print-check.tsv (phrase, source, result, detail, url) and TARGET/print-check-hosts.tsv (host, requests,
status). Every phrase is also run, unasked, through the IA full-text search across all items (ia-global), Google Books
and OpenAlex, because the misses that taught this lesson were in sources nobody had listed.

Lesson answered (LEDGER.md, 20-24 Sept 2026): every verifier and check-solved worker re-implemented this search, and
the Jacqueton and RTA prior prints were missed because nobody had listed those sources. A search here is a search
result, not a novelty verdict (CLAUDE.md rule 10): 'no hits' means not found by this method on this date.

Per source:
  ia        a cached _djvu.txt (searched for in sources/ia-fulltext, tools/data, ciphers/*/, and --cache, plain or .gz)
            is searched exactly (normalised) and by proximity (all words in order within a short window, for OCR
            damage); otherwise the djvu text is downloaded once (public items) and cached gzipped; lending-only items
            (403) fall back to be-api full-text search, whose page numbers are not real (CLAUDE.md), so it gives a
            snippet, not a page.
  ia-global be-api.us.archive.org/fts/v1/search?q="phrase" over all items: top identifiers with a snippet.
  htrc      Extracted Features per-page token counts (cached gzipped): pages (scan seq) on which every word of 4+ letters
            of the phrase occurs. A co-occurrence, not a phrase match: open the page to confirm.
  gbooks    Books API volumes?q="phrase"&country=US&key=$GOOGLE_BOOKS_KEY (the key is never printed or written); listed
            volume ids are flagged when they appear among the results.
  openalex  works?search="phrase" and works?search=<keywords>;  crossref  works?query.bibliographic=<keywords or phrase>.
Politeness (CLAUDE.md good-citizen rule): one request at a time, 1.5 s apart per host, descriptive User-Agent (a Chrome
string only for HathiTrust's catalogue API, which needs it); on 403, 429 or a challenge page the host is marked
blocked and not asked again this run. --max-requests caps the run. --offline uses cached texts only.

Test: python3 tools/tests/test_print_check.py (offline, on the cached Bowes correspondence djvu text).
"""
import argparse, collections, glob, gzip, json, os, re, sys, time, unicodedata
import urllib.error, urllib.parse, urllib.request

UA = 'cipher-lab research script (contact via repository)'
CHROME = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KINDS = ('ia', 'hathi', 'oclc', 'htid', 'gbooks', 'openalex', 'crossref')


def norm(s, early=True):
    s = unicodedata.normalize('NFKD', s.replace('ſ', 's'))
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    if early:
        s = s.replace('v', 'u').replace('j', 'i')
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def dehyphen(text):
    return re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)


class Net:
    """One request at a time, >= 1.5 s apart per host, blocked hosts skipped, counts kept."""

    def __init__(self, offline, max_requests):
        self.offline, self.max = offline, max_requests
        self.last, self.count, self.status = {}, collections.Counter(), {}

    def get(self, url, ua=UA, raw=False, shown=None):
        host = urllib.parse.urlparse(url).netloc
        if self.offline:
            return None, 'offline'
        if host in self.status and self.status[host].startswith('blocked'):
            return None, self.status[host]
        if sum(self.count.values()) >= self.max:
            return None, 'max-requests reached'
        wait = self.last.get(host, 0) + 1.5 - time.time()
        if wait > 0:
            time.sleep(wait)
        self.count[host] += 1
        req = urllib.request.Request(url, headers={'User-Agent': ua, 'Accept': '*/*'})
        try:
            body = urllib.request.urlopen(req, timeout=120).read()
            self.last[host] = time.time()
        except urllib.error.HTTPError as e:
            self.last[host] = time.time()
            if e.code in (403, 429):
                self.status[host] = f'blocked: HTTP {e.code} on {shown or url}'
                return None, self.status[host]
            self.status.setdefault(host, 'ok (some errors)')
            return None, f'HTTP {e.code}'
        except (urllib.error.URLError, TimeoutError) as e:
            self.status[host] = f'unreachable: {getattr(e, "reason", e)}'
            return None, self.status[host]
        head = body[:3000].lower()
        if b'altcha' in head or b'cf-chl' in head or b'performing security verification' in head:
            self.status[host] = 'blocked: challenge page'
            return None, self.status[host]
        self.status.setdefault(host, 'ok')
        return (body if raw else body.decode('utf-8', 'replace')), 'ok'

    def json(self, url, **kw):
        body, st = self.get(url, **kw)
        if body is None:
            return None, st
        try:
            return json.loads(body), 'ok'
        except ValueError:
            return None, 'not JSON'


# ------------------------------------------------------------------ text search

def search_text(text, phrase, early=True, window_extra=4):
    """(exact count, first contexts, proximity count) over a normalised text."""
    t = norm(dehyphen(text), early); p = norm(phrase, early)
    exact = [m.start() for m in re.finditer(r'(?<![a-z0-9])' + re.escape(p) + r'(?![a-z0-9])', t)]
    ctx = [t[max(0, i - 60):i + len(p) + 60] for i in exact[:3]]
    words = p.split(); toks = t.split()
    near, first = 0, None
    if len(words) >= 2:
        pos = collections.defaultdict(list)
        for i, w in enumerate(toks):
            pos[w].append(i)
        span = len(words) + window_extra
        for start in pos.get(words[0], []):
            j, ok = start, True
            for w in words[1:]:
                nxt = next((k for k in pos.get(w, []) if j < k <= start + span), None)
                if nxt is None:
                    ok = False; break
                j = nxt
            near += ok
            if ok and first is None:
                first = start
        if near and not exact:
            i = first
            ctx = [' '.join(toks[max(0, i - 8):i + span + 8])]
    return len(exact), ctx, near


def find_cached_djvu(ident, cache):
    pats = [os.path.join(cache, f'{ident}_djvu.txt*'), os.path.join(ROOT, 'sources', '**', f'{ident}_djvu.txt*'),
            os.path.join(ROOT, 'tools', 'data', '**', f'{ident}_djvu.txt*'),
            os.path.join(ROOT, 'ciphers', '**', f'{ident}_djvu.txt*')]
    for p in pats:
        hits = glob.glob(p, recursive=True)
        if hits:
            return hits[0]
    return None


def read_text(path):
    op = gzip.open if path.endswith('.gz') else open
    with op(path, 'rt', encoding='utf-8', errors='ignore') as f:
        return f.read()


def check_ia(ident, phrases, net, cache, early, rows):
    path = find_cached_djvu(ident, cache)
    how = 'cached ' + os.path.relpath(path, ROOT) if path else None
    if not path:
        url = f'https://archive.org/download/{ident}/{ident}_djvu.txt'
        body, st = net.get(url, raw=True)
        if body:
            os.makedirs(cache, exist_ok=True)
            path = os.path.join(cache, f'{ident}_djvu.txt.gz')
            with gzip.open(path, 'wb') as f:
                f.write(body)
            how = 'downloaded djvu text'
        else:
            how = f'djvu text not available ({st})'
    for ph in phrases:
        if path:
            n, ctx, near = search_text(read_text(path), ph, early)
            res = f'{n} exact' if n else (f'{near} near (OCR proximity)' if near else 'no hits')
            rows.append([ph, f'ia:{ident}', res, (how + '; ' + ' | '.join(ctx))[:400],
                         f'https://archive.org/details/{ident}'])
        else:
            q = urllib.parse.quote(f'"{ph}"')
            url = f'https://be-api.us.archive.org/fts/v1/search?q={q}&identifier={ident}'
            d, st = net.json(url)
            if d is None:
                rows.append([ph, f'ia:{ident}', f'not searched ({st})', how, url]); continue
            hits = d.get('hits', {}).get('hits', [])
            snip = ' | '.join(str(h.get('highlight', {}).get('text', [''])[0])[:150] for h in hits[:1])
            rows.append([ph, f'ia:{ident}', f'{len(hits)} item(s) (be-api fts)' if hits else 'no hits',
                         f'{how}; be-api page_num is not a page locator; {snip}'[:400], url])


def check_ia_global(phrases, net, rows):
    for ph in phrases:
        q = urllib.parse.quote(f'"{ph}"')
        url = f'https://be-api.us.archive.org/fts/v1/search?q={q}'
        d, st = net.json(url)
        if d is None:
            rows.append([ph, 'ia-global', f'not searched ({st})', '', url]); continue
        hits = d.get('hits', {}).get('hits', [])
        tot = d.get('hits', {}).get('total', len(hits))
        tot = tot.get('value', len(hits)) if isinstance(tot, dict) else tot
        det = '; '.join(f"{h['fields'].get('identifier', ['?'])[0]} ({(h['fields'].get('meta_title') or ['?'])[0][:50]})"
                        for h in hits[:5])
        rows.append([ph, 'ia-global', f'{tot} item(s)' if hits else 'no hits', det, url])


def resolve_htids(kind, val, net):
    url = f'https://catalog.hathitrust.org/api/volumes/brief/{"recordnumber" if kind == "hathi" else "oclc"}/{val}.json'
    d, st = net.json(url, ua=CHROME)
    if d is None:
        return [], st
    return [i['htid'] for i in d.get('items', []) if 'htid' in i], 'ok'


def check_htrc(htid, phrases, net, cache, early, rows):
    path = os.path.join(cache, 'htrc-ef', re.sub(r'[^A-Za-z0-9._$-]', '_', htid) + '.json.gz')
    if os.path.exists(path):
        pages = json.load(gzip.open(path, 'rt'))
    else:
        url = f'https://data.htrc.illinois.edu/ef-api/volumes/{htid}/pages?pos=false'
        d, st = net.json(url, ua=UA)
        if d is None or 'data' not in d:
            for ph in phrases:
                rows.append([ph, f'htrc:{htid}', f'not searched ({st if d is None else "no EF data"})', '', url])
            return
        pages = [{'seq': p['seq'], 'w': sorted({norm(t, early) for part in ('header', 'body', 'footer')
                                                 for t in ((p.get(part) or {}).get('tokensCount') or {})})}
                 for p in d['data']['pages']]
        os.makedirs(os.path.dirname(path), exist_ok=True)
        json.dump(pages, gzip.open(path, 'wt'))
    for ph in phrases:
        words = [w for w in norm(ph, early).split() if len(w) >= 4]
        seqs = [int(p['seq']) for p in pages if words and set(words) <= set(p['w'])]
        rows.append([ph, f'htrc:{htid}', f'{len(seqs)} page(s) with all words' if seqs else 'no hits',
                     f"words {' '.join(words)}; seq {' '.join(map(str, seqs[:20]))}",
                     f'https://babel.hathitrust.org/cgi/pt?id={htid}' + (f'&seq={seqs[0]}' if seqs else '')])


def check_gbooks(phrases, listed, net, rows):
    key = os.environ.get('GOOGLE_BOOKS_KEY', '')
    for ph in phrases:
        q = urllib.parse.quote(f'"{ph}"')
        shown = f'https://www.googleapis.com/books/v1/volumes?q={q}&country=US&maxResults=10'
        url = shown + (f'&key={key}' if key else '')
        d, st = net.json(url, shown=shown)
        if d is None:
            rows.append([ph, 'gbooks', f'not searched ({st})', '' if key else 'GOOGLE_BOOKS_KEY not set', shown]); continue
        items = d.get('items', [])
        flag = [i['id'] for i in items if i['id'] in listed]
        det = '; '.join(f"{i['id']} {i['volumeInfo'].get('title', '')[:40]} {i['volumeInfo'].get('publishedDate', '')}"
                        for i in items[:5])
        rows.append([ph, 'gbooks', f"{d.get('totalItems', 0)} volume(s)" + (f'; listed: {",".join(flag)}' if flag else '')
                     if items else 'no hits', det, shown])


def check_openalex(queries, net, rows):
    for label, q in queries:
        url = 'https://api.openalex.org/works?per-page=5&search=' + urllib.parse.quote(q)
        d, st = net.json(url)
        if d is None:
            rows.append([label, 'openalex', f'not searched ({st})', '', url]); continue
        res = d.get('results', [])
        det = '; '.join(f"{w.get('display_name', '')[:60]} ({w.get('publication_year')}) {w.get('doi') or w.get('id')}"
                        for w in res)
        rows.append([label, 'openalex', f"{d.get('meta', {}).get('count', 0)} work(s)" if res else 'no hits', det, url])


def check_crossref(queries, net, rows):
    for label, q in queries:
        url = 'https://api.crossref.org/works?rows=5&query.bibliographic=' + urllib.parse.quote(q)
        d, st = net.json(url)
        if d is None:
            rows.append([label, 'crossref', f'not searched ({st})', '', url]); continue
        m = d.get('message', {})
        det = '; '.join(f"{(i.get('title') or [''])[0][:60]} {i.get('DOI')}" for i in m.get('items', []))
        rows.append([label, 'crossref', f"{m.get('total-results', 0)} record(s), top 5 by relevance", det, url])


def load_lines(path):
    if not path or not os.path.exists(path):
        return []
    return [l.strip() for l in open(path, encoding='utf-8') if l.strip() and not l.lstrip().startswith('#')]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('target'); ap.add_argument('--phrases'); ap.add_argument('--sources')
    ap.add_argument('--source', action='append', default=[], help='KIND:VALUE, repeatable')
    ap.add_argument('--only', help='comma list of checks to run')
    ap.add_argument('--offline', action='store_true', help='cached texts only, no network')
    ap.add_argument('--cache', default=os.path.join(ROOT, 'sources', 'ia-fulltext', 'print-check'))
    ap.add_argument('--no-early-modern', action='store_true', help='do not fold u/v and i/j')
    ap.add_argument('--max-requests', type=int, default=200)
    ap.add_argument('--out', help='output TSV (default TARGET/print-check.tsv)')
    a = ap.parse_args(argv)
    early = not a.no_early_modern
    phrases = load_lines(a.phrases or os.path.join(a.target, 'phrases.txt'))
    srcs = []
    for l in load_lines(a.sources or os.path.join(a.target, 'sources.tsv')):
        p = l.split('\t')
        if p[0] in KINDS and len(p) > 1:
            srcs.append((p[0], p[1].strip()))
    srcs += [tuple(s.split(':', 1)) for s in a.source]
    if not phrases:
        ap.error('no phrases (TARGET/phrases.txt or --phrases)')
    only = set(a.only.split(',')) if a.only else None
    run = lambda k: only is None or k in only
    net, rows = Net(a.offline, a.max_requests), []
    for kind, val in srcs:
        if kind == 'ia' and run('ia'):
            check_ia(val, phrases, net, a.cache, early, rows)
    if run('ia-global'):
        check_ia_global(phrases, net, rows)
    if run('htrc'):
        htids = [v for k, v in srcs if k == 'htid']
        for kind, val in srcs:
            if kind in ('hathi', 'oclc'):
                got, st = resolve_htids(kind, val, net)
                htids += got
                if not got:
                    rows.append([f'({kind} {val})', 'htrc', f'no volume ids ({st})', '', ''])
        for h in dict.fromkeys(htids):
            check_htrc(h, phrases, net, a.cache, early, rows)
    if run('gbooks'):
        check_gbooks(phrases, {v for k, v in srcs if k == 'gbooks'}, net, rows)
    kw = [(f'(keywords) {v}', v) for k, v in srcs if k == 'openalex']
    if run('openalex'):
        check_openalex([(p, f'"{p}"') for p in phrases] + kw, net, rows)
    if run('crossref'):
        ck = [(f'(keywords) {v}', v) for k, v in srcs if k in ('crossref', 'openalex')]
        check_crossref(ck or [(p, p) for p in phrases], net, rows)
    date = time.strftime('%d %b %Y', time.gmtime())
    out = a.out or os.path.join(a.target, 'print-check.tsv')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(f'# tools/print_check.py, {date}. A search result, not a novelty verdict (CLAUDE.md rule 10).\n')
        f.write('phrase\tsource\tresult\tdetail\turl\n')
        for r in rows:
            f.write('\t'.join(str(x).replace('\t', ' ').replace('\n', ' ') for x in r) + '\n')
    hosts = os.path.join(os.path.dirname(out), 'print-check-hosts.tsv')
    with open(hosts, 'w', encoding='utf-8') as f:
        f.write('host\trequests\tstatus\n')
        for h in sorted(set(net.count) | set(net.status)):
            f.write(f'{h}\t{net.count[h]}\t{net.status.get(h, "")}\n')
        if a.offline:
            f.write('(offline)\t0\tcached texts only; network checks not run\n')
    hit = [r for r in rows if not (r[2].startswith('no hits') or r[2].startswith('not searched'))]
    print(f'{len(phrases)} phrases, {len(srcs)} listed sources: {len(rows)} rows, {len(hit)} with hits -> {out}')
    print('requests: ' + (', '.join(f'{h} {n}' for h, n in net.count.items()) or 'none'))
    for h, s in net.status.items():
        if not s.startswith('ok'):
            print(f'  {h}: {s}')
    return rows


if __name__ == '__main__':
    main()
    sys.exit(0)
