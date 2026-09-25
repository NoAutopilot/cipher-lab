"""LANE R7 CM3 (25 Sept 2026): tabulate pass A/B disagreement classes, pass C votes and the settled direction across the seven leaves with recon_box_* folders; the basis of the measured error rate in NOTES.md "CM3". Run from ciphers/fr2933-salviati-1525/."""
import csv, glob
from collections import Counter
def load(p):
    return {(r['line'].strip(), r['pos'].strip()): r for r in csv.DictReader(open(p), delimiter='\t')}
def cls(ca, cb):
    if ca == 'MISSING' or cb == 'MISSING': return 'missing'
    a, b = ca == '_', cb == '_'
    if a != b: return 'sign_plain'
    if ca != cb: return 'code'
    return 'marks'
LEAVES = ['f54v','f55r','f55v','f56r','f56v','f57r','f57v']
tot = Counter(); N = 0; NS = 0
for lf in LEAVES:
    ct = list(csv.DictReader(open(f'ciphertext_{lf}.tsv'), delimiter='\t'))
    n = len(ct); ns = sum(1 for r in ct if r['code'] != '_')
    dis = list(csv.DictReader(open(f'recon_box_{lf}/disagreements.tsv'), delimiter='\t'))
    c = Counter(cls(r['code_a'], r['code_b']) for r in dis)
    tot += c; N += n; NS += ns
    print(lf, 'rows', n, 'signs', ns, 'dis', len(dis), dict(c), f"d={len(dis)/n:.3f}")
print('ALL rows', N, 'signs', NS, 'dis', sum(tot.values()), dict(tot), f"d={sum(tot.values())/N:.3f}")
print('pairwise disagreement per row by class:', {k: f"{v/N:.4f}" for k, v in tot.items()})
# pass C vote on f55v/f57v: at each A/B disagreement, does C side with A, B, or neither?
for lf in ['f55v', 'f57v']:
    A, B, C = load(f'passA_{lf}.tsv'), load(f'passB_{lf}.tsv'), load(f'passC_{lf}.tsv')
    S = load(f'recon_box_{lf}/settled.tsv')
    dis = list(csv.DictReader(open(f'recon_box_{lf}/disagreements.tsv'), delimiter='\t'))
    vote = Counter(); byc = Counter(); cwrong = Counter()
    for r in dis:
        k = (r['line'], r['pos']); ca, cb = r['code_a'], r['code_b']
        cc = C[k]['code'] if k in C else 'MISSING'
        cl = cls(ca, cb)
        v = 'A' if cc == ca and cc != cb else 'B' if cc == cb and cc != ca else 'neither'
        vote[v] += 1; byc[(cl, v)] += 1
        s = S[k]['code'] if k in S else None
        if s is not None and cc != s: cwrong[cl] += 1
    print(lf, 'C votes', dict(vote), 'by class', dict(byc), 'C != settled', dict(cwrong), 'of', len(dis))
