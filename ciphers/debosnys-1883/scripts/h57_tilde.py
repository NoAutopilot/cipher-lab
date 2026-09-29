#!/usr/bin/env python3
"""H57 (29 Sept 2026): tilde re-labelling on the verse, per h57/PREREG.md (pushed 09b2a7eb before any read).
  OUT=<scratch> h57_tilde.py build          crops q01.. under $OUT/crops, key under $OUT/key.tsv (never shown to the reader)
  OUT=<scratch> h57_tilde.py score READS    READS = tsv crop<TAB>yes|no|unsure ; writes h57/result.json"""
import os, sys, csv, json, random, re, gzip, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, os.path.join(root, 'swarm/R2/R2-2')); _a = sys.argv; sys.argv = [sys.argv[0]]
import t_low
sys.argv = _a
OUT = os.environ['OUT']; MARKS = {'BLOB', 'BAR-SOLID', 'HOOK-L', 'DASH-V', 'DASH-H', '_', 'MULTI', 'MARK'}
rows = [r for r in csv.DictReader(open(os.path.join(root, 'ciphertext_c34_draft.tsv')), delimiter='\t') if r['line'].startswith('c4')]
code = {(r['our_line'], r['our_pos']): r['bourdeau_code'] for r in csv.DictReader(open(os.path.join(root, 'h26_alignment.tsv')), delimiter='\t') if r['our_pos']}
def is_t(s): return 'TILDE' in s or 'CURL' in s
def is_tc(c): return c.startswith('N_') or 'TILDE' in c
def build():
    tg, other = [], []
    for r in rows:
        k = (r['line'], r['position']); s = r['sign'].rstrip('?'); c = code.get(k, '')
        if s in MARKS: continue
        (tg if is_t(s) or is_tc(c) else other).append((r['line'], int(r['position']), s, c))
    rng = random.Random(57); dec = rng.sample(other, 15); items = [('target', *x) for x in tg] + [('decoy', *x) for x in dec]
    rng.shuffle(items); os.makedirs(os.path.join(OUT, 'crops'), exist_ok=True); key = []
    for i, (kind, line, pos, s, c) in enumerate(items):
        name = f'q{i + 1:02d}'
        try: t_low.crop_real(line, pos, name, os.path.join(OUT, 'crops'))
        except Exception as e: print('skip', line, pos, e); continue
        key.append((name, kind, line, str(pos), s, c))
    open(os.path.join(OUT, 'key.tsv'), 'w').write('crop\tkind\tline\tposition\tsign\tbourdeau\n' + ''.join('\t'.join(k) + '\n' for k in key))
    print(len(key), 'crops;', sum(k[1] == 'target' for k in key), 'targets,', sum(k[1] == 'decoy' for k in key), 'decoys')
NAS = re.compile(r"(ain|ein|oin|aim|eim|an|am|en|em|in|im|on|om|un|um)(?=[^aeiouyhnm]|$)")
def nasal_rate():
    d = os.path.join(root, '..', '..', 'tools/data/fr19v'); per = []
    for f in sorted(os.listdir(d)):
        if not f.endswith('.txt.gz'): continue
        for l in gzip.open(os.path.join(d, f), 'rt', encoding='utf-8', errors='ignore'):
            l = l.strip().lower()
            if 25 <= len(l) <= 60 and not l.isupper(): per.append(sum(len(NAS.findall(w)) for w in re.findall(r"[a-zàâéèêëîïôûùüç]+", l)))
    return per
def score(reads):
    key = {r['crop']: r for r in csv.DictReader(open(os.path.join(OUT, 'key.tsv')), delimiter='\t')}
    ans = {r[0].strip(): r[1].strip().lower() for r in csv.reader(open(reads), delimiter='\t') if len(r) >= 2}
    dec = [ans.get(c, 'missing') for c, k in key.items() if k['kind'] == 'decoy']; tgt = {c: ans.get(c, 'missing') for c, k in key.items() if k['kind'] == 'target'}
    out = dict(decoys=dict(collections.Counter(dec)), decoy_yes_rate=round(dec.count('yes') / len(dec), 3), targets=dict(collections.Counter(tgt.values())))
    out['gate_pass'] = out['decoy_yes_rate'] <= 0.20
    lines = sorted({r['line'] for r in rows}, key=lambda k: (0 if k.startswith('c4a0') else 1 if k.startswith('c4a') else 2, k))
    for mode in ('yes', 'yes+unsure'):
        acc = {'yes'} if mode == 'yes' else {'yes', 'unsure'}
        per = [sum(1 for c, k in key.items() if k['line'] == l and k['kind'] == 'target' and tgt.get(c) in acc) for l in lines]
        rng = random.Random(1); bs = sorted(sum(rng.choice(per) for _ in per) / len(per) for _ in range(10000))
        out[mode] = dict(per_line=per, mean=round(sum(per) / len(per), 2), ci95=[round(bs[250], 2), round(bs[9749], 2)])
    nr = nasal_rate(); m = sum(nr) / len(nr); rng = random.Random(2)
    bs = sorted(sum(rng.choice(nr) for _ in range(20)) / 20 for _ in range(10000))
    out['nasal_fr19v'] = dict(lines=len(nr), mean=round(m, 2), mean_of_20_lines_95=[round(bs[250], 2), round(bs[9749], 2)])
    out['sektu_per_line'] = 1.5; print(json.dumps(out, indent=1)); json.dump(out, open(os.path.join(root, 'h57', 'result.json'), 'w'), indent=1)
if __name__ == '__main__':
    {'build': build, 'score': lambda: score(sys.argv[2])}[sys.argv[1]]()
