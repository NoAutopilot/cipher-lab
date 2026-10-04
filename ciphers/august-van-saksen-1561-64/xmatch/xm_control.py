#!/usr/bin/env python3
"""N4-XM (4 Oct 2026): size-matched control for the key_crossmatch lead fr3993-villeroy f159 x AVS ct58/74/57.
Selection and decision rule: PREREG.md beside this file. Uses tools/key_crossmatch.py's own functions."""
import sys, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'tools'))
import key_crossmatch as kx
jp = kx.jp

AVS = 'ciphers/august-van-saksen-1561-64'
CTS = ['ciphertext_58_sample.tsv', 'ciphertext_74.tsv', 'ciphertext_57.tsv']
F159 = 'ciphers/fr3993-villeroy-1595/keys/key_f159_letters.tsv'
gate = kx.load_gate()
by_lang = kx.reading_files_by_lang()
cmap = kx.build_repo_corpora()
cts = {n: kx.load_ct_meta(ROOT / AVS / n) for n in CTS}

def nletters(key):
    return sum(1 for r in key.values() if len(jp.fold((r.get('value') or '').split('|')[0])) == 1)

def load(p):
    key, meta = kx.load_key_meta(p)
    if key is None:
        return None, None
    meta['lang'], _ = kx.language_for(meta['folder'], meta['lang_hint'], by_lang)
    return key, meta

def score(key, lang, c, floor_off=False):
    cov = kx.coverage_of(key, c['signs'])
    model = kx.get_model(lang, exclude_folder=c['folder'], corpora_map=cmap)
    if model is None or (cov < 0.5 and not floor_off):
        return dict(cov=round(cov, 3), stat=None, verdict='none' if model else 'no_corpus')
    ps = kx.pair_stats(key, c['signs'], model, n_shuffle=20, seed=0)['own']
    return dict(cov=round(cov, 3), stat=round(ps['stat'], 2), z_ng=round(ps['z_ng'], 2),
                z_vf=None if ps['z_vf'] is None else round(ps['z_vf'], 2),
                verdict=kx.gate_verdict(ps['stat'], cov, len(c['signs']), gate))

keys, _ = kx.find_key_files()
fkey, fmeta = load(ROOT / F159)
print('f159', fmeta['lang'], 'letters', nletters(fkey), 'rows', len(fkey))
for n, c in cts.items():
    print('  f159', n, len(c['signs']), score(fkey, fmeta['lang'], c))
cands = []
for p in keys:
    rel = str(p.relative_to(ROOT))
    if 'fr3993-villeroy-1595' in rel or 'august-van-saksen-1561-64' in rel:
        continue
    key, meta = load(p)
    if not key:
        continue
    nl = nletters(key)
    if nl < 0.8 * len(key) or not (20 <= nl <= 58):
        continue
    covs = [kx.coverage_of(key, c['signs']) for c in cts.values()]
    cands.append((abs(nl - 39), rel, nl, covs, key, meta))
cands.sort(key=lambda t: (t[0], t[1]))
print('letter-alphabet keys of 20-58 letters:', len(cands))
for d, rel, nl, covs, _, _ in cands:
    print('  ', rel, nl, [round(x, 2) for x in covs])
sel = [t for t in cands if all(x >= 0.5 for x in t[3])][:3]
relaxed = False
if not sel:
    sel = [t for t in cands if any(x >= 0.5 for x in t[3])][:3]; relaxed = True
if not sel:   # PREREG amendment A: top-3 real distinct-folder keys by minimum coverage, floor bypassed
    relaxed = 'amendment A'
    seen = set(); sel = []
    for t in sorted(cands, key=lambda t: (-min(t[3]), t[1])):
        f = t[1].split('/')[1]
        if 'shuf' in t[1] or f in seen:
            continue
        seen.add(f); sel.append(t)
        if len(sel) == 3:
            break
print('SELECTED (relaxed=%s):' % relaxed)
out = []
for d, rel, nl, covs, key, meta in sel:
    for n, c in cts.items():
        a = score(key, meta['lang'], c, floor_off=True)
        b = score(key, fmeta['lang'], c, floor_off=True)
        print('  ', rel, meta['lang'], nl, n, a, '| under %s:' % fmeta['lang'], b)
        out.append(dict(key=rel, lang=meta['lang'], letters=nl, ct=n, own_lang=a, f159_lang=b))
json.dump(dict(relaxed=relaxed, rows=out), open(Path(__file__).with_name('xm_control.json'), 'w'), indent=1)
