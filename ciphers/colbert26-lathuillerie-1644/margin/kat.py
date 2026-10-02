"""A2-COL4: known-answer test of key_f23.tsv on the f.23 rotated margin postscript (not used to build the key).
Statistic: per unit, walk the codes in order; a code scores if its key value is found in the unit's gloss (letters only,
lowercase, v->u, j->i) at or after the end of the previous match (ordered greedy). Reported for C-grade codes and for all
coded values. Control: the same walk against windows of equal length cut at random from the f.23 main-text gloss
(interlinear/f23w_pairs.tsv, concatenated in order), 2000 draws per unit; the score depends on which gloss the run meets,
so the control can fail differently from the real gloss. Usage: python3 margin/kat.py"""
import csv, random, re, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s): return re.sub(r'[^a-z]', '', s.lower()).replace('v', 'u').replace('j', 'i')
key = {r['code']: (norm(r['value']), r['grade']) for r in csv.DictReader(open(f'{T}/key_f23.tsv'), delimiter='\t')}
units = list(csv.DictReader(open(f'{H}/f23m_reconciled.tsv'), delimiter='\t'))
bank = norm(''.join(r['plain_raw'] for r in csv.DictReader(open(f'{T}/interlinear/f23w_pairs.tsv'), delimiter='\t')))
def walk(codes, gloss, grades):
    p = 0; hit = n = 0
    for c in codes:
        if c not in key or key[c][1] not in grades: continue
        n += 1; i = gloss.find(key[c][0], p)
        if i >= 0: hit += 1; p = i + len(key[c][0])
    return hit, n
rng = random.Random(1646)
print('unit\tset\treal\tn\tcontrol_mean\tcontrol_p95\tcontrol_max\tP(control>=real)')
tot = {}
for u in units:
    codes = u['codes'].split(); g = norm(u['gloss'])
    print('#', u['unit'], ' '.join(f"{c}={key[c][0]}/{key[c][1]}" if c in key else f"{c}=-" for c in codes))
    for name, grades in (('C', {'C'}), ('all', {'C', 'M'})):
        h, n = walk(codes, g, grades)
        ctrl = []
        for _ in range(2000):
            s = rng.randrange(0, len(bank) - len(g)); ctrl.append(walk(codes, bank[s:s + len(g)], grades)[0])
        ctrl.sort(); pge = sum(x >= h for x in ctrl) / len(ctrl)
        print(f"{u['unit']}\t{name}\t{h}\t{n}\t{sum(ctrl)/len(ctrl):.2f}\t{ctrl[int(.95*len(ctrl))]}\t{ctrl[-1]}\t{pge:.4f}")
        t = tot.setdefault(name, [0, 0, []]); t[0] += h; t[1] += n; t[2].append(ctrl)
for name, (h, n, cs) in tot.items():
    pooled = [sum(x) for x in zip(*cs)]; pooled.sort()
    print(f"ALL\t{name}\t{h}\t{n}\t{sum(pooled)/len(pooled):.2f}\t{pooled[int(.95*len(pooled))]}\t{pooled[-1]}\t{sum(x>=h for x in pooled)/len(pooled):.4f}")
