"""BIRAGO-NUM-KEYEYE2 (3 Oct 2026): score the fr.3995 no.74 (f.138v) and no.32 (f.62v) key tables against the f.119 and
f.100r pair-token files with tools/key_crossmatch.py's own pair_stats and calibrated gate, exactly as xmatch_no73.py did,
matched positive control FIRST (synthetic Italian it16dip enciphered with the same key, 240 tokens, 0/10/20/30% token
corruption, 3 seeds). Polyphonic values 'a|b' decode to the first alternative (the tool's rule); a second variant rotates
to the last alternative. Nulls ('-') decode to nothing. python3 num/keyeye/xmatch_no74_no32.py  (run from the target folder)"""
import sys, random
sys.path.insert(0, '../../tools'); sys.path.insert(0, 'num')
import key_crossmatch as kx, analyze
KEYS = {'no74': 'keys/key_fr3995_no74.tsv', 'no32': 'keys/key_fr3995_no32.tsv'}
CTS = {'f119': '../birago-nevers-1571/ciphertext_f119_pairs.txt', 'f100r': 'num/ciphertext_f100_pairs.txt'}
def load(p):
    k = {}
    for ln in open(p):
        if ln.startswith('#') or ln.startswith('code\t'): continue
        c, v = ln.rstrip('\n').split('\t')[:2]
        k[c] = {'value': '' if v == '-' else v}
    return k
def alias(k):
    a = dict(k); a.update({'0' + c: k[c] for c in k if len(c) == 1}); return a
def lastalt(k): return {c: {'value': r['value'].split('|')[-1]} for c, r in k.items()}
def letters_only(k): return {c: r for c, r in k.items() if len(r['value'].split('|')[0]) <= 3}
def toks(p): return [t for ln in open(p) if not ln.startswith('#') for t in ln.split()]
gate = kx.load_gate(); model = kx.get_model('it')
print('gate stat_min', gate['stat_min'], '| coverage floor 0.5 (key_crossmatch MIN coverage)')
for kname, kp in KEYS.items():
    key = load(kp)
    # matched positive control first
    inv = {}
    for c, r in key.items():
        for alt in r['value'].split('|'):
            if alt and len(alt) <= 3: inv.setdefault(alt, []).append(c)
    units = sorted(inv, key=len, reverse=True)
    def encode(txt, rng):
        out, i = [], 0
        while i < len(txt):
            for u in units:
                if txt.startswith(u, i): out.append(rng.choice(inv[u])); i += len(u); break
            else: i += 1
        return out
    codes = list(key); hits = 0
    for err in (0.0, 0.10, 0.20, 0.30):
        for seed in (1, 2, 3):
            rng = random.Random(seed); txt = analyze.italian(600, rng, path='../../tools/data/it16dip').replace('v', 'u').replace('k', 'c').replace('j', 'i')
            s = encode(txt, rng)[:240]
            s = [rng.choice(codes) if rng.random() < err else t for t in s]
            r = kx.pair_stats(key, s, model)['own']; h = kx.passes_gate(r['stat'], gate); hits += h
            print(f"CONTROL {kname} err={err:.2f} seed={seed} n={len(s)} stat={r['stat']:.2f} {'hit' if h else 'miss'}")
    print(f"CONTROL {kname} total {hits}/12")
    for name, p in CTS.items():
        s = toks(p)
        for vn, k in (('as-written', key), ('0d=d alias', alias(key)), ('0d=d alias, last alternative', lastalt(alias(key))),
                      ('0d=d alias, letters/syllables only (persons dropped)', letters_only(alias(key)))):
            r = kx.pair_stats(k, s, model)['own']; dec, cov = kx.decode_with(k, s)
            print(f"TARGET {kname} {name} key={vn} n={len(s)} cov={cov/len(s):.2f} z_ng={r['z_ng']:.2f} z_vf={r['z_vf']} stat={r['stat']:.2f} {'HIT' if kx.passes_gate(r['stat'], gate) else 'below gate'} | {''.join(dec.split())[:70]}")
