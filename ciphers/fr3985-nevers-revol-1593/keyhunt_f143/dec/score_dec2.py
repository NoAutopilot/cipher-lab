# F143-DEC2, 11 Oct 2026: decode-level key-family test registered in PREREG-F143-DEC2.md.
# Usage: python3 score_dec2.py [--check]   (--check exits 1 if the committed score_dec2.txt is stale)
import csv, os, random, sys, io
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, '..', '..', '..', '..')
sys.path.insert(0, os.path.join(R, 'tools'))
import judge_plaintext as J

def rows(p, lines=None):
    with open(p) as f:
        rr = list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))
    return [r for r in rr if lines is None or r['line'].strip() in lines]

key = {}
for r in rows(os.path.join(R, 'tools/keys/key60.tsv')):
    v = (r['value'] or '').split('|')[0].strip()
    key[r['sign'].strip()] = v
signs = list(key)

def tags(rr):
    return [r['tag'].strip().rstrip('?') for r in rr]

def decode(tt, k):
    out = []
    for t in tt:
        v = k.get(t, '')
        if v and v not in ('NULL', '?'):
            out.append(v)
    return ''.join(out)

M = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA['fr16']])

def shuffled(tt, n=1000, seed=1):
    rnd = random.Random(seed); vals = [key[s] for s in signs]; sc = []
    for _ in range(n):
        rnd.shuffle(vals); k = dict(zip(signs, vals))
        sc.append(M.score(decode(tt, k)))
    sc.sort(); return sc

def p95(xs): return xs[int(0.95 * len(xs))]

L58 = {'L05', 'L06', 'L07', 'L08'}
arms = [
    ('T pass R (fresh, Sonnet) f.143r L05-L08', rows(os.path.join(H, 'passR.tsv'), L58)),
    ('T pass P (KH1-F) f.143r L05-L08', rows(os.path.join(H, '..', 'passP.tsv'), L58)),
    ('T pass Q (KH1-F, report only) f.143r L06-L08', rows(os.path.join(H, '..', 'passQ.tsv'), {'L06', 'L07', 'L08'})),
    ('M reverse arm fr.4715 f.61r (Mayenne key)', rows(os.path.join(H, 'passM.tsv'))),
    ('C positive control fr.3986 f.152 passD (no.60)', rows(os.path.join(R, 'ciphers/fr3986-nevers-revol-1593/atlas_heldout/heldout298_passD.tsv'))),
]
out = io.StringIO(); res = {}
print('arm\tsigns\tin_key60\tletters\tS_key60\tshuf_mean\tshuf_p95\tshuf_max\tkey60_rank_of_1001', file=out)
for lab, rr in arms:
    tt = tags(rr); txt = decode(tt, key); s = M.score(txt); sh = shuffled(tt)
    rank = 1 + sum(x >= s for x in sh)
    res[lab[0] + lab.split()[2] if lab.startswith('T') else lab[0]] = (s, p95(sh))
    print(f"{lab}\t{len(tt)}\t{sum(t in key for t in tt)}\t{len(J.fold(txt))}\t{s:.4f}\t{sum(sh)/len(sh):.4f}\t{p95(sh):.4f}\t{sh[-1]:.4f}\t{rank}", file=out)
    print(f"  decode: {J.fold(txt)}", file=out)
sR, pR = res['TR']; sP, pP = res['TP']; sM, _ = res['M']; sC, pC = res['C']
print('', file=out)
nt1 = sM >= pR or sM >= pP; nt2 = sC <= pC
print(f"gate 1 (non-test if M >= T shuffled p95): M {sM:.4f} vs p95 R {pR:.4f}, P {pP:.4f} -> {'NON-TEST' if nt1 else 'ok'}", file=out)
print(f"gate 2 (non-test if C <= its shuffled p95): C {sC:.4f} vs p95 {pC:.4f} -> {'NON-TEST' if nt2 else 'ok'}", file=out)
cR = sR > pR and sR > sM; cP = sP > pP and sP > sM
v = 'NON-TEST' if (nt1 or nt2) else ('PASS' if cR and cP else ('FAIL' if not cR and not cP else 'SPLIT (not passed)'))
print(f"gate 3: pass R clears {cR}; pass P clears {cP}", file=out)
print(f"VERDICT: {v}", file=out)
txt = out.getvalue(); dst = os.path.join(H, 'score_dec2.txt')
if '--check' in sys.argv:
    ok = os.path.exists(dst) and open(dst).read() == txt
    print('check OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(dst, 'w').write(txt); print(txt)
