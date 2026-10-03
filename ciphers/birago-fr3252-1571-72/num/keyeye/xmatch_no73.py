"""BIRAGO-NUM-KEYEYE (3 Oct 2026): score the fr.3995 no.73 (f.136r) two-figure syllabary against the f.119 and f.100r
pair-token files with tools/key_crossmatch.py's own pair_stats and calibrated gate, with a matched positive control
(synthetic Italian enciphered with this same key, same token count, 0/10/20% token corruption standing in for the
unsettled phase). python3 num/keyeye/xmatch_no73.py  (run from the target folder)"""
import sys, random
sys.path.insert(0, '../../tools'); sys.path.insert(0, 'num')
import key_crossmatch as kx, analyze
KEY = 'keys/key_fr3995_no73_f136r.tsv'
CTS = {'f119': '../birago-nevers-1571/ciphertext_f119_pairs.txt', 'f100r': 'num/ciphertext_f100_pairs.txt'}
key = {}
for ln in open(KEY):
    if ln.startswith('#') or ln.startswith('code\t'): continue
    c, v = ln.rstrip('\n').split('\t')[:2]; key[c] = {'value': v}
alias = dict(key); alias.update({'0' + c: key[c] for c in key if len(c) == 1})   # 01..09 written with a leading 0
def toks(p): return [t for ln in open(p) if not ln.startswith('#') for t in ln.split()]
gate = kx.load_gate(); model = kx.get_model('it')
print('gate stat_min', gate['stat_min'])
for name, p in CTS.items():
    s = toks(p)
    for kn, k in (('as-written', key), ('0d=d alias', alias)):
        r = kx.pair_stats(k, s, model)['own']; dec, cov = kx.decode_with(k, s)
        print(f"TARGET {name} key={kn} n={len(s)} cov={cov/len(s):.2f} z_ng={r['z_ng']:.2f} z_vf={r['z_vf']} stat={r['stat']:.2f} {'HIT' if kx.passes_gate(r['stat'], gate) else 'below gate'} | {''.join(dec.split())[:70]}")
# matched positive control: Italian plaintext parsed greedily into this key's syllables, encoded, corrupted
inv = {}
for c, r in key.items(): inv.setdefault(r['value'], c)
units = sorted(inv, key=len, reverse=True)
def encode(txt):
    out, i = [], 0
    while i < len(txt):
        for u in units:
            if txt.startswith(u, i): out.append(inv[u]); i += len(u); break
        else: i += 1
    return out
codes = list(key)
for err in (0.0, 0.10, 0.20, 0.30):
    for seed in (1, 2, 3):
        rng = random.Random(seed); txt = analyze.italian(480, rng, path='../../tools/data/it16dip').replace('v', 'u').replace('k', 'c').replace('j', 'i')
        s = encode(txt)[:240]
        s = [rng.choice(codes) if rng.random() < err else t for t in s]
        r = kx.pair_stats(key, s, model)['own']
        print(f"CONTROL err={err:.2f} seed={seed} n={len(s)} stat={r['stat']:.2f} {'hit' if kx.passes_gate(r['stat'], gate) else 'miss'}")
