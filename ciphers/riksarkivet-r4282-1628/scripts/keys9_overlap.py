#!/usr/bin/env python3
"""GAPS32-riksarkivet-r4282-1628 (3 Oct 2026): do the letter tables of the last nine DECODE key records with letter or
graphic signs (4293 4295 4297 4308 4309 4312 4322 4323 4329) fit R4282 on the signs they share?  Tables read by eye from
170 dpi renders of the full-size PDFs (grade M; see keys_r4293_r4329/manifest.json).  4309's alphabet is the 4275 Mainz
alphabet (tested in key4275_overlap.py); 4322 is a name list, 4329 a two-digit (20-43) letter table plus name lists,
4323 shares one sign (lambda) only, where a permutation control cannot vary: none of those is tested here.
Per key, STRICT = the shared signs whose shape matches an R4282 class without doubt (or R4282's single digits where the
key itself gives single-digit values); WIDE = STRICT plus ambiguous pairs.  v and w -> u in la18's alphabet.
Same statistic and controls as key4275_overlap.py (rule 3): mean la18 Latin unigram log-probability of the letters the
key gives R4282's tokens of those signs, vs (a) the same values permuted among the signs and (b) distinct random Latin
letters, 2000 draws each.  --check re-derives and compares with the committed keys9_overlap.json."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from key4275_overlap import test
from key4327_overlap import HERE

# 4293: third copy of the table; v = lambda, z = 3, y = E (epsilon-like); wide: p = 8 (o/p/q column ambiguous), n = h-shape
K4293 = {'L': 'u', '3': 'z', 'E': 'y'}
K4293W = dict(K4293, **{'8': 'p', 'h': 'n'})
# 4295 numeric homophones: a 3 4 5, c 7, d 8 (single digits only)
K4295N = {'3': 'a', '4': 'a', '5': 'a', '7': 'c', '8': 'd'}
# 4295 struck reciprocal keyword alphabet "erlachbdfgik / mnopqstuwxyz" applied to R4282's Latin-letter shapes
_top, _bot = 'erlachbdfgik', 'mnopqstuwxyz'
REC = {}
for x, y in zip(_top, _bot):
    REC[x], REC[y] = y, x
K4295R = {s: ('u' if REC[s] in 'vw' else REC[s]) for s in 'abcdefghiklmnopqrstuxy' if s in REC}
# 4297: g = lambda, n = x, o = open square; wide: c = 7-like hook, x = S
K4297 = {'L': 'g', 'x': 'n', 'B': 'o'}
K4297W = dict(K4297, **{'7': 'c', 'S': 'x'})
# 4308: a = lambda, b = crossed 4, l = x, n = i-shape, i = h-shape; wide: k = looped delta (R4282 D), r = q-shape, f = o-bar
K4308 = {'L': 'a', '4': 'b', 'x': 'l', 'i': 'n', 'h': 'i'}
K4308W = dict(K4308, **{'D': 'k', 'q': 'r', 'o': 'f'})
# 4312 numeric homophones, single-digit values: D 9, K 7, L 8, O 1, P 5, Q 4, S 3, V 6, W 2
K4312 = {'3': 's', '4': 'q', '5': 'p', '7': 'k', '8': 'l'}

SETS = {'4293 strict': (K4293, 4293), '4293 wide': (K4293W, 42931), '4295 numeric digits': (K4295N, 4295),
        '4295 reciprocal Latin (struck)': (K4295R, 42952), '4297 strict': (K4297, 4297), '4297 wide': (K4297W, 42971),
        '4308 strict': (K4308, 4308), '4308 wide': (K4308W, 43081), '4312 numeric digits': (K4312, 4312)}

def run():
    return {k: test(key, seed) for k, (key, seed) in SETS.items()}

if __name__ == '__main__':
    out = run(); j = HERE / 'keys9_overlap.json'
    if '--check' in sys.argv:
        ok = json.loads(j.read_text()) == out; print('OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    j.write_text(json.dumps(out, indent=1) + '\n')
    for k, r in out.items():
        print(f"{k:32s} signs {r['signs']:2d} cov {r['covered']:4d} real {r['real_mean_logp']:.3f} perm {r['perm_mean']:.3f}/{r['perm_p95']:.3f}/{r['perm_frac_ge_real']:.3f} rand {r['rand_mean']:.3f}/{r['rand_p95']:.3f}/{r['rand_frac_ge_real']:.3f}")
