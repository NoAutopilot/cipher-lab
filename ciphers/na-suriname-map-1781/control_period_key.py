#!/usr/bin/env python3
"""Rule-3 control for the period key (GAPS13, 2 Oct 2026): count distinct-position hits of a fixed Dutch fortification
vocabulary (4+ letters, pre-registered below, drawn from the plain sibling legends 2038/2042 and AMH 2218 wording) in
the 2039 legend and 2061 block decoded under key_period_codes.tsv, against 1000 keys whose values are shuffled among
the same codes (same value multiset, same coverage). Two-valued entries a|b match either value."""
import csv, random, re, sys
VOCAB = """batterijen batterij bastion bastions magazijn magazyn kruit artillerie corps garde gardes cisterne cisternes
kwartier kwartiers officiers wooning woning voor voorde bezetting bezettinge inspectie laboratorium nieuwe
verdere ijzer yser dito batterie redout fortresse wagt provoost keuken kazerne caserne gevangenis secreet
sluis poort brug gragt wal water""".split()
def load(f):
    toks=[r for r in csv.reader(open(f),delimiter='\t') if r and not r[0].startswith('#')][1:]
    return [(r[0],r[2]) for r in toks]
def keymap(f):
    k={}
    for r in csv.reader(open(f),delimiter='\t'):
        if not r or r[0].startswith('#') or r[0]=='code': continue
        k[r[0]]=r[1]
    return k
def hits(seqs,k):
    n=0
    for seq in seqs:
        opts=[set(k[s].split('|')) if s in k else set() for s in seq]
        for w in VOCAB:
            L=len(w)
            for i in range(len(seq)-L+1):
                if all(w[j] in opts[i+j] or (w[j] in 'ijy' and opts[i+j]&set('ijy')) for j in range(L)): n+=1
    return n
def seqs(f):
    out={}
    for line,s in load(f):
        if s.startswith('w:') or s.startswith('p:'): continue
        out.setdefault(line,[]).append(s)
    return list(out.values())
k=keymap('key_period_codes.tsv')
S=seqs('ciphertext_2039_legend.tsv')+seqs('ciphertext_2061_battery.tsv')
real=hits(S,k)
rng=random.Random(13); codes=list(k); vals=[k[c] for c in codes]; null=[]
for _ in range(int(sys.argv[1]) if len(sys.argv)>1 else 1000):
    rng.shuffle(vals); null.append(hits(S,dict(zip(codes,vals))))
null.sort(); ge=sum(x>=real for x in null)
print(f"real {real}; shuffled-value null mean {sum(null)/len(null):.2f}, p95 {null[int(.95*len(null))]}, max {null[-1]}; null >= real {ge}/{len(null)}")
