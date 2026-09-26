"""AX-4612: block IC (w=5, offsets 0-4) of 4612's numerals 1-120 split by transcription confidence (H = the two blind
passes agreed, M = they differed or one was flagged), against the random-partition null of ic_scan.py; and the same
for 4610 (a letter that reads under key.tsv) as the reference. Also key.tsv's letters for the H-only stream."""
import csv, collections, random
D = 'ciphers/lodewijk-van-nassau-1573-74/'
key = {int(r['code']): r['value'] for r in csv.DictReader(open(D + 'key.tsv'), delimiter='\t') if r['code'].isdigit() and int(r['code']) <= 120}
def ic(seq, cls):
    c = collections.Counter(cls[v] for v in seq); n = len(seq)
    return sum(x * (x - 1) for x in c.values()) / (n * (n - 1)) if n > 1 else 0
def null95(seq, w, draws=300):
    rng = random.Random(1); vals = list(range(1, 121)); out = []
    for _ in range(draws):
        rng.shuffle(vals); out.append(ic(seq, {v: i // w for i, v in enumerate(vals)}))
    out.sort(); return out[len(out) // 2], out[int(draws * .95)]
for nr in ('4612', '4610', '4611'):
    rows = list(csv.DictReader(open(D + f'ciphertext_{nr}.tsv'), delimiter='\t'))
    for conf in ('H', 'M', 'all'):
        s = [int(r['sign']) for r in rows if r['sign'].isdigit() and int(r['sign']) <= 120 and (conf == 'all' or r['confidence'] == conf)]
        if len(s) < 30: continue
        ics = ' '.join(f'o{o}:{ic(s, {v: ((v - 1 - o) % 120) // 5 for v in range(1, 121)}):.4f}' for o in range(5))
        m, p = null95(s, 5)
        print(f'{nr} {conf:3s} N={len(s):4d} w5 {ics} | null med {m:.4f} p95 {p:.4f}')
    hs = [r['sign'] for r in rows if r['confidence'] == 'H']
    if nr == '4612':
        print('4612 H-only stream under key.tsv (clear words as =):')
        print(''.join(key[int(x)] if x.isdigit() and int(x) <= 120 else (' ' + x + ' ' if x.startswith('=') else '#') for x in hs)[:900])
