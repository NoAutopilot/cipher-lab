#!/usr/bin/env python3
"""Map folios to canvases in a Gallica (or any IIIF v2) manuscript, from the manifest's own labels, and say where
the map is inconsistent instead of assuming one offset.

  python3 tools/gallica_folio.py ARK [--folio 35 [--side r|v]] [--anchor CANVAS=FOLIO[r|v] ...] [--list]
                                 [--manifest FILE] [--cache DIR] [--json]
  ARK: 'btv1b52521512h', 'ark:/12148/btv1b52521512h', or a gallica.bnf.fr URL containing the ark.

Lesson answered (LEDGER.md and NOTES of fr16092-maisse-1582, fr5160-letellier-1653, fr20140-danzay-1557, 23-24
Sept 2026): four workers flagged inconsistent canvas-to-folio offsets and one probed 25 canvases to find one leaf.
The manifest already carries a label per canvas ('35r', '1-2r', 'NP', 'plat sup.'); this reads every label once.

What it does:
  1. Fetches https://gallica.bnf.fr/iiif/ark:/12148/ARK/manifest.json once (one request, descriptive User-Agent) and
     caches it (default sources/gallica-manifests/ARK.json); later runs read the cache. Stops on HTTP 403/429 or an
     altcha / challenge page and says so; no retry loop.
  2. Parses labels: '35r', 'f. 35v', 'fol. 35', '35 bis r', ranges '1-2r'. 'NP' (non paginé), bindings, guards are
     reported as unlabelled.
  3. Calibrates: for each labelled leaf side, offset k = canvas - (2*folio - 1 for r, 2*folio for v) when the
     manifest images one side per canvas; prints each run of canvases with a constant k, every change of k (an
     unnumbered, bis or missing leaf), and duplicate labels. With --anchor (canvas=folio pairs checked by eye, needed
     when every label is 'NP') it fits canvas = a*folio + b by least squares and prints a and the residuals: a near
     2 means one canvas per page side, near 1 one per leaf or opening; a residual over 1 canvas means the anchors do
     not share one offset.
  4. --folio N: the canvas(es) labelled N (recto and verso), with the native image URL and the canvas size; if no
     canvas carries the label, an estimate from the nearest labelled leaves or anchors, marked ESTIMATE (check by eye).
Exit 0; 2 when the manifest cannot be fetched.

Test: python3 tools/tests/test_gallica_folio.py (offline, on the cached fr.20140 manifest in the repo).
"""
import argparse, json, os, re, sys, time, urllib.error, urllib.request

UA = 'cipher-lab research script (contact via repository)'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABEL = re.compile(r'^\s*(?:f(?:ol)?\.?\s*)?(\d+)(?:\s*-\s*(\d+))?\s*(bis|ter)?\s*([rv])?\s*\.?\s*$', re.I)


def ark_id(s):
    m = re.search(r'(btv1b\w+|bpt6k\w+|\b[a-z0-9]{8,}\b)', s.split('ark:/12148/')[-1])
    return m.group(1) if m else s


def fetch_manifest(ark, cache, path=None):
    if path:
        return json.load(open(path, encoding='utf-8')), 'file'
    cp = os.path.join(cache, ark + '.json')
    if os.path.exists(cp):
        return json.load(open(cp, encoding='utf-8')), 'cached'
    url = f'https://gallica.bnf.fr/iiif/ark:/12148/{ark}/manifest.json'
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
    try:
        body = urllib.request.urlopen(req, timeout=120).read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        sys.exit(f'{url}: HTTP {e.code}; stop (good-citizen rule: no retry loop). Log it in NOTES.md and ROOM.md.')
    except urllib.error.URLError as e:
        sys.exit(f'{url}: {e.reason}; unreachable from here.')
    if 'altcha' in body.lower() or body.lstrip()[:1] != '{':
        sys.exit(f'{url}: challenge or non-JSON page (altcha?); stop, do not retry. Log it in NOTES.md and ROOM.md.')
    time.sleep(1.5)
    os.makedirs(cache, exist_ok=True)
    open(cp, 'w', encoding='utf-8').write(body)
    return json.loads(body), 'fetched'


def canvases(man):
    """[(n, label, width, height, native_url)] with n the 1-based canvas number (Gallica's fN)."""
    if 'sequences' in man:
        cs = man['sequences'][0]['canvases']
        out = []
        for i, c in enumerate(cs, 1):
            lab = c.get('label', '')
            lab = lab if isinstance(lab, str) else json.dumps(lab)
            img = c['images'][0]['resource'].get('@id', '') if c.get('images') else ''
            out.append((i, lab, c.get('width'), c.get('height'), img))
        return out
    out = []                                   # IIIF v3
    for i, c in enumerate(man.get('items', []), 1):
        lab = c.get('label', {})
        lab = next(iter(lab.values()))[0] if isinstance(lab, dict) and lab else str(lab)
        try:
            img = c['items'][0]['items'][0]['body']['id']
        except (KeyError, IndexError):
            img = ''
        out.append((i, lab, c.get('width'), c.get('height'), img))
    return out


def parse(label):
    """(first_folio, last_folio, suffix, side) or None."""
    m = LABEL.match(label)
    if not m:
        return None
    a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
    return a, b, (m.group(3) or '').lower(), (m.group(4) or '').lower()


def page_index(f, side):
    return 2 * f - 1 if side == 'r' else 2 * f


def calibrate(cs):
    """Offset runs over single-leaf labels with a side and no bis/ter: list of (k, first canvas, last canvas, labels)."""
    runs, dup, seen = [], [], {}
    for n, lab, *_ in cs:
        p = parse(lab)
        if not p:
            continue
        if lab in seen:
            dup.append((lab, seen[lab], n))
        seen.setdefault(lab, n)
        a, b, suf, side = p
        if a != b or suf or not side:
            continue
        k = n - page_index(a, side)
        if runs and runs[-1][0] == k and n - runs[-1][2] <= 2:
            runs[-1][2] = n; runs[-1][3].append(lab)
        else:
            runs.append([k, n, n, [lab]])
    return runs, dup


def fit(anchors):
    """Least squares canvas = a*folio + b; returns a, b, residuals."""
    xs = [f for _, f in anchors]; ys = [c for c, _ in anchors]
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    a = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx if sxx else 0
    b = my - a * mx
    return a, b, [(c, f, round(c - (a * f + b), 2)) for c, f in anchors]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('ark'); ap.add_argument('--folio', type=int); ap.add_argument('--side', choices=('r', 'v'))
    ap.add_argument('--anchor', action='append', default=[], help='CANVAS=FOLIO[r|v], checked by eye; repeatable')
    ap.add_argument('--list', action='store_true', help='print every canvas and its label')
    ap.add_argument('--manifest', help='read this manifest file instead of fetching')
    ap.add_argument('--cache', default=os.path.join(ROOT, 'sources', 'gallica-manifests'))
    ap.add_argument('--json', action='store_true', help='print the --folio answer as JSON')
    a = ap.parse_args(argv)
    ark = ark_id(a.ark)
    man, how = fetch_manifest(ark, a.cache, a.manifest)
    cs = canvases(man)
    labelled = [c for c in cs if parse(c[1])]
    print(f'{ark}: {len(cs)} canvases ({how}); {len(labelled)} with a folio label, {len(cs) - len(labelled)} without')
    if a.list:
        for n, lab, w, h, _ in cs:
            print(f'  f{n}\t{lab}\t{w}x{h}')
    runs, dup = calibrate(cs)
    report = dict(ark=ark, canvases=len(cs), labelled=len(labelled), runs=[r[:3] + [r[3][0], r[3][-1]] for r in runs],
                  duplicates=dup)
    if runs:
        print('offset runs (k = canvas - page index; page index = 2*folio-1 recto, 2*folio verso):')
        for k, c0, c1, labs in runs:
            print(f'  canvases f{c0}-f{c1}: {labs[0]}..{labs[-1]}  k={k}')
        ks = sorted({r[0] for r in runs})
        print('  one constant offset' if len(ks) == 1 else f'  INCONSISTENT: {len(ks)} offsets {ks}; use the label, not a formula')
    ranges = [(n, lab) for n, lab, *_ in cs if parse(lab) and parse(lab)[0] != parse(lab)[1]]
    if ranges:
        print('  range labels (one canvas for several leaves): ' + ', '.join(f'f{n}={lab}' for n, lab in ranges[:12]))
    for lab, n1, n2 in dup:
        print(f'  DUPLICATE label {lab!r} on f{n1} and f{n2}')
    anchors = []
    for s in a.anchor:
        c, f = s.split('='); m = re.match(r'(\d+)([rv]?)', f)
        anchors.append((int(c.lstrip('f')), int(m.group(1)) + (0.5 if m.group(2) == 'v' else 0)))
    if len(anchors) >= 2:
        sl, b, res = fit(anchors)
        report['fit'] = dict(slope=round(sl, 3), intercept=round(b, 2), residuals=res)
        print(f'anchor fit: canvas = {sl:.3f} * folio + {b:.2f}; residuals ' +
              ', '.join(f'f{c}={f:g}: {r:+}' for c, f, r in res))
        if len(anchors) == 2:
            print('  two anchors fit any line exactly; the slope is the test')
        if not (0.8 <= sl <= 1.2 or 1.8 <= sl <= 2.2):
            report['fit']['inconsistent'] = True
            print(f'  INCONSISTENT anchors: slope {sl:.2f} is neither ~1 (canvas per leaf) nor ~2 (canvas per side); '
                  'unfoliated, bis or missing leaves lie between them, or an anchor is misread')
        if any(abs(r) > 1 for *_, r in res):
            report['fit']['inconsistent'] = True
            print('  INCONSISTENT anchors: no single offset explains them (bis, missing or unfoliated leaves between)')
    if a.folio is None:
        if a.json:
            print(json.dumps(report))
        return 0
    hits = []
    for n, lab, w, h, img in cs:
        p = parse(lab)
        if p and p[0] <= a.folio <= p[1] and (not a.side or p[3] in (a.side, '')):
            hits.append(dict(canvas=n, label=lab, width=w, height=h, native=img, how='label'))
    if not hits:
        est = None
        if runs:
            near = min(runs, key=lambda r: min(abs(parse(r[3][0])[0] - a.folio), abs(parse(r[3][-1])[0] - a.folio)))
            for side in ([a.side] if a.side else ['r', 'v']):
                n = page_index(a.folio, side) + near[0]
                if 1 <= n <= len(cs):
                    c = cs[n - 1]
                    hits.append(dict(canvas=n, label=c[1], width=c[2], height=c[3], native=c[4],
                                     how=f'ESTIMATE from nearest labelled run k={near[0]} (check by eye)'))
        elif len(anchors) >= 2:
            sl, b, _ = fit(anchors)
            est = int(round(sl * (a.folio + (0.5 if a.side == 'v' else 0)) + b))
            for n in range(max(1, est - 1), min(len(cs), est + 1) + 1):
                c = cs[n - 1]
                hits.append(dict(canvas=n, label=c[1], width=c[2], height=c[3], native=c[4],
                                 how=f'ESTIMATE from anchor fit, centre f{est} (check by eye)'))
    if a.json:
        print(json.dumps(dict(report, folio=a.folio, answer=hits)))
    elif not hits:
        print(f'folio {a.folio}: no canvas carries this label and there is nothing to estimate from; give --anchor pairs')
    for h in hits:
        print(f"folio {a.folio}: canvas f{h['canvas']} label {h['label']!r} {h['width']}x{h['height']} [{h['how']}]\n"
              f"  {h['native']}")
    return hits


if __name__ == '__main__':
    r = main()
    sys.exit(0 if not isinstance(r, int) else r)
