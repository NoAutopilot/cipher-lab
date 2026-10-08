#!/usr/bin/env python3
"""E62-ALN (8 Oct 2026): list the residue entries (pages of print/residue/pages_manifest.tsv) that carry >= 1 M token and share
>= --min distinct 6-grams of words with one OR 1862 volume (LS3-R62's re-grep, re-run because its output was scratch).

Usage: residue_select.py PAGES_DIR OR_DIR [--min 3] > residue_print/selected.tsv
  PAGES_DIR: <pointer>.json per page (as for residue_decode.py); OR_DIR: <ia_identifier>.txt (IA _djvu.txt, not committed).
Columns: pointer, entry (blank-line chunk index, the one or_align.py uses), date, M, C, I, volume, hits.
A 6-gram occurring more than 8 times across the volumes is a formula and ignored (or_match.py rule).
"""
import json, re, glob, os, sys, collections, argparse, importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("decode", HERE.parent / "decode.py"); dec = importlib.util.module_from_spec(spec); spec.loader.exec_module(dec)
ap = argparse.ArgumentParser(); ap.add_argument('pages'); ap.add_argument('ordir'); ap.add_argument('--min', type=int, default=3)
a = ap.parse_args(); N = 6
def words(t):
    t = re.sub(r'<deletion>.*?</deletion>|<del>.*?</del>', ' ', t, flags=re.S)
    return [w.lower() for w in re.findall(r"[A-Za-z]+", re.sub(r'<[^>]+>', ' ', t).replace('&', ' and '))]
idx = collections.defaultdict(collections.Counter)
for f in sorted(glob.glob(os.path.join(a.ordir, '*.txt'))):
    v = os.path.basename(f)[:-4]; w = words(open(f, errors='ignore').read())
    for i in range(len(w) - N + 1): idx[' '.join(w[i:i + N])][v] += 1
key = dec.load_key(); last = None
manifest = {int(r.split('\t')[0]) for r in (HERE / 'residue' / 'pages_manifest.tsv').read_text().splitlines()[1:]}
matched = {int(r.split('\t')[0]) for r in (HERE / 'or_matches.tsv').read_text().splitlines()[1:] if r.split('\t')[0].isdigit()}
print('pointer\tentry\tdate\tM\tC\tI\tvolume\thits')
for p in sorted(manifest - matched):
    f = os.path.join(a.pages, f'{p}.json')
    if not os.path.exists(f): continue
    text = (json.load(open(f)).get('text') or '').strip()
    if not text or p < 4956: continue
    ents = re.split(r'\n\s*\n', text.replace('\r', ''))
    # residue_decode.py drops empty chunks before dating; keep its date carry-over by iterating the same list
    for k, e in enumerate(ents):
        if not e.strip(): continue
        day = dec.parse_day(re.sub(r"\bApl\b", "Apr", e.strip().splitlines()[0])) or last; last = day or last
        r, c = dec.decode_entry(dec.entry_text(e.strip().splitlines()), key, day)
        if not c.get('M'): continue
        w = words(e); hit = collections.defaultdict(set)
        for i in range(len(w) - N + 1):
            g = ' '.join(w[i:i + N]); c2 = idx.get(g)
            if not c2 or sum(c2.values()) > 8: continue
            for v in c2: hit[v].add(g)
        if not hit: continue
        v, gs = max(hit.items(), key=lambda x: len(x[1]))
        if len(gs) >= a.min: print(f"{p}\t{k}\t{day}\t{c['M']}\t{c['C']}\t{c['I']}\t{v}\t{len(gs)}")
