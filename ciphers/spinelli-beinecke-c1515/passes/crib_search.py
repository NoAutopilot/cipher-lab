#!/usr/bin/env python3
"""Search a sign-coded pass TSV for the symbol run the key predicts for a plaintext crib.

Usage: python3 crib_search.py PASS.tsv "la gubernation d'ispagnia" [--max-nulls N] [--min-frac F]

PASS.tsv columns: line, segment, pos, code, shape, conf (the campaign's blind-pass format). Codes are the
key's letter codes (a, b, c, d1, d2, e, ... homophones as letter+digit), N1..N12 nulls, W1..W6 word codes,
'?' unknown. The crib is lowered, stripped of apostrophes/spaces, and each plaintext letter is matched
against any homophone of that letter (d matches d1/d2, etc.). Nulls (N*) inside a candidate run are skipped
(at most --max-nulls of them); '?' signs count as a wildcard miss. Reports, per line, the best alignment
window as matched/total letters, so a partial match (a misread sign or two) still shows.
Segments of one line are concatenated s1 then s2 with the s1/s2 overlap NOT removed -- so a run straddling
the join may be reported twice, or once with a small gap; the report shows positions so a human can check.
"""
import sys, csv, argparse, re

def load(path):
    rows=[]
    with open(path, newline='') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if not r.get('code'): continue
            rows.append(r)
    lines={}
    for r in rows:
        if r['code'].strip().upper()=='PLAIN': continue
        key=r['line'].strip()
        lines.setdefault(key,[]).append(r)
    for k in lines:
        lines[k].sort(key=lambda r:(r['segment'], int(r['pos'])))
    return lines

def letter_of(code):
    c=code.strip()
    if c in ('?','') or c.startswith('?'): return None
    if c[0] in 'NW' and c[1:].isdigit(): return 'NULL' if c[0]=='N' else 'WORD'
    m=re.match(r'^([a-z])\d?$', c)
    return m.group(1) if m else None

def search(lines, crib, max_nulls):
    plain=[ch for ch in crib.lower() if ch.isalpha()]
    plain=[{'v':'u','j':'i','w':'u'}.get(ch,ch) for ch in plain]
    L=len(plain)
    out=[]
    for lk, signs in lines.items():
        codes=[letter_of(s['code']) for s in signs]
        best=None
        for start in range(len(signs)):
            i=start; matched=0; nulls=0; misses=0; consumed=[]
            for p in plain:
                # skip nulls
                while i<len(signs) and codes[i]=='NULL' and nulls<max_nulls:
                    nulls+=1; i+=1
                if i>=len(signs): break
                if codes[i]==p: matched+=1
                else: misses+=1
                consumed.append(i); i+=1
            if len(consumed)<L: continue
            frac=matched/L
            if best is None or frac>best['frac']:
                best={'frac':frac,'matched':matched,'start':start,'end':consumed[-1],'nulls':nulls,
                      'seq':' '.join(signs[j]['code'] for j in range(start, consumed[-1]+1))}
        if best: out.append((lk,best))
    return sorted(out, key=lambda x:-x[1]['frac'])

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('tsv'); ap.add_argument('crib'); ap.add_argument('--max-nulls',type=int,default=6); ap.add_argument('--min-frac',type=float,default=0.0)
    a=ap.parse_args()
    lines=load(a.tsv)
    plain=''.join(ch for ch in a.crib.lower() if ch.isalpha())
    print(f"crib {plain!r} ({len(plain)} letters); {sum(len(v) for v in lines.values())} signs in {len(lines)} lines")
    for lk,b in search(lines,a.crib,a.max_nulls):
        if b['frac']>=a.min_frac:
            print(f"line {lk}: best {b['matched']}/{len(plain)} = {b['frac']:.2f} at idx {b['start']}-{b['end']} (nulls skipped {b['nulls']}): {b['seq']}")
