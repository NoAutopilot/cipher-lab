"""BIRAGO-NUM-KEYEYE3 (3 Oct 2026): score the fr.3995 no.71 (f.133r) letter alphabet against the f.119 and f.100r pair-token
files exactly as xmatch_no74_no32.py did (tools/key_crossmatch.py pair_stats, calibrated gate stat_min 3.292), matched
positive control FIRST: synthetic text enciphered with this key's letter codes, 240 tokens, 0/10/20/30% token corruption,
3 seeds; run for the Italian model (it16dip text, as KEYEYE/KEYEYE2) and the French model (fr16 text; the table is French).
The table is code+mark: dotted codes are words, overlined codes persons; the pair tokens carry no marks, so only the plain
letter codes are scored. python3 num/keyeye/xmatch_no71.py  (run from the target folder)"""
import sys, random, glob, gzip, re
sys.path.insert(0, '../../tools'); sys.path.insert(0, 'num')
import key_crossmatch as kx
KP = 'keys/key_fr3995_no71_f133r.tsv'
CTS = {'f119': '../birago-nevers-1571/ciphertext_f119_pairs.txt', 'f100r': 'num/ciphertext_f100_pairs.txt'}
key = {}
for ln in open(KP):
    if ln.startswith('#') or ln.startswith('code\t'): continue
    c, v = ln.rstrip('\n').split('\t')[:2]; key[c] = {'value': v}
alias = dict(key); alias.update({'0' + c: key[c] for c in key if len(c) == 1})
_C = {}
def sample(lang, n, rng):
    if lang not in _C:
        t = ''.join(gzip.open(f, 'rt', errors='ignore').read() for f in sorted(glob.glob(f'../../tools/data/{lang}/*.txt.gz')))
        _C[lang] = re.sub('[^a-z]', '', t.lower().replace('j', 'i').replace('k', 'c').replace('w', 'u').replace('v', 'u'))
    t = _C[lang]; s = rng.randrange(0, len(t) - n); return t[s:s + n]
inv = {}
for c, r in key.items(): inv.setdefault(r['value'], []).append(c)
def toks(p): return [t for ln in open(p) if not ln.startswith('#') for t in ln.split()]
gate = kx.load_gate(); codes = list(key)
print('gate stat_min', gate['stat_min'], '| coverage floor', gate.get('min_coverage', 0.5))
for lang, corp in (('it', 'it16dip'), ('fr', 'fr16')):
    model = kx.get_model(lang); hits = 0
    for err in (0.0, 0.10, 0.20, 0.30):
        for seed in (1, 2, 3):
            rng = random.Random(seed)
            s = [rng.choice(inv[ch]) for ch in sample(corp, 900, rng) if ch in inv][:240]
            s = [rng.choice(codes) if rng.random() < err else t for t in s]
            r = kx.pair_stats(key, s, model)['own']; h = kx.passes_gate(r['stat'], gate); hits += h
            print(f"CONTROL {lang} err={err:.2f} seed={seed} n={len(s)} stat={r['stat']:.2f} {'hit' if h else 'miss'}")
    print(f"CONTROL {lang} total {hits}/12")
    for name, p in CTS.items():
        s = toks(p)
        for vn, k in (('as-written', key), ('0d=d alias', alias)):
            r = kx.pair_stats(k, s, model)['own']; dec, cov = kx.decode_with(k, s)
            print(f"TARGET {lang} {name} key={vn} n={len(s)} cov={cov/len(s):.2f} stat={r['stat']:.2f} "
                  f"{'HIT' if kx.passes_gate(r['stat'], gate) else 'below gate'}{' (under coverage floor)' if cov/len(s) < 0.5 else ''} | {''.join(dec.split())[:60]}")
