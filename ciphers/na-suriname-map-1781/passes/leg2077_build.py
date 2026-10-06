# GAPS19-na-suriname-map-1781 (account-4), 3 Oct 2026: build ciphertext_2077_legend.tsv from passes/leg2077_merged.tsv
# (leg2077_merge.py: two blind Opus passes) and passes/leg2077_reconcile.tsv (one blind Opus reconciliation call).
# Plain tokens <...> -> w:<text>. Usage: python3 passes/leg2077_build.py [--check]  (exit 1 if the committed file is stale)
import csv,sys
LINE={f'leg77_L{i:02d}':f'2077_L{i:02d}' for i in range(1,21)}  # L01-L03 title, L04 heading, L05-L19 legend rows, L20 line below
M=list(csv.DictReader(open('passes/leg2077_merged.tsv'),delimiter='\t'))
R={}
for r in csv.DictReader((l for l in open('passes/leg2077_reconcile.tsv') if not l.startswith('#')),delimiter='\t'):
    if r['pos'].strip().isdigit(): R[(r['crop'].strip(),int(r['pos']))]=r
    elif r['crop'].strip()=='NAME': R[('NAME',r['pos'].strip())]=r
# GAPS20 (3 Oct 2026): the reconciler's three NAME answers (Part 2 of the brief) rename a neutral shape name to the key's own
# shape name when it answered yes (DIGIT7 -> 7, TALLV -> [v-tall]); an OTHER answer leaves the neutral name (unkeyed).
REN={}
for nm,yes,to in (('r-rot','DIGIT7','7'),('c-curl','TALLV','[v-tall]'),('kappa','LETTERk','k')):
    d=R.get(('NAME',nm))
    if d and d['decision'].strip()==yes: REN['['+nm+']']=to
by={}
for r in M: by.setdefault(r['crop'],[]).append(r)
rows=[]
for c,lst in by.items():
    out=[]
    for i,r in enumerate(lst):
        if r['conf']=='M':
            d=R.get((c,i))
            if d is None: out.append((r['sign'],'M',r['note']+'; not reconciled')); continue
            dec=d['decision'].strip(); A,B=r['note'][2:].split(' B:')
            # decision forms written by the reconciler: 'A [code]' / 'B [code]' (or bare A/B), 'B -' (no glyph),
            # 'SAME x=y' (one shape, two names: the note's 'use X' if given, else the right-hand name, so 6=[d-hook]
            # stays [d-hook], unkeyed -- the reconciler's 'same as numeral 6' is logged in NOTES.md, not applied),
            # or a new code. DROP = no glyph.
            w=dec.split(None,1)
            if w[0] in ('A','B'): dec=w[1].strip() if len(w)>1 else (A if w[0]=='A' else B)
            elif w[0]=='SAME':
                rest=w[1] if len(w)>1 else A; note=d['note']
                if 'use ' in note: dec=note.split('use ',1)[1].split()[0].rstrip(';,.')
                else: dec=rest.split('=')[-1]
            if dec in ('DROP','-'): continue
            out.append((dec,'H' if d['conf'].strip()=='H' else 'M',r['note']+'; reconciled '+d['conf'].strip()+': '+d['note']))
        else: out.append((r['sign'],'H',''))
    for j,(s,g,n) in enumerate(out):
        if s in REN: n=(n+'; ' if n else '')+'NAME '+s+'->'+REN[s]; s=REN[s]
        if s.startswith('<') and s.endswith('>'): s='w:'+s[1:-1]
        rows.append((LINE[c],j,s,g,n))
# R10-SUR (6 Oct 2026, account 2): reader-code split from passes/sigma_split_r10/split.tsv (rationale there); every row gains a
# sign_r9 column holding the reader code as built before the split, so the pre-split ciphertext stays readable.
SPLIT={}
for l in open('passes/sigma_split_r10/split.tsv'):
    f=l.rstrip('\n').split('\t')
    if l.startswith('#') or f[0]=='line': continue
    SPLIT[(f[0],int(f[1]))]=(f[2],f[3])
rows=[r+(r[2],) for r in rows]
for i,r in enumerate(rows):
    if (r[0],r[1]) in SPLIT:
        o,nw=SPLIT[(r[0],r[1])]; assert r[2]==o,(r,o)
        rows[i]=(r[0],r[1],nw,r[3],(r[4]+'; ' if r[4] else '')+'R10-SUR split '+o+'->'+nw,r[5])
assert len(SPLIT)==sum(1 for r in rows if r[2]!=r[5])
head=['# NA 4.VEL 2077 (Plan van de fortress Zelandia, 1781): title cartouche 3 lines, plain heading, the mixed plain/cipher',
'# "Explicatie der Signatuuren" legend a-z and the line below it. Native IIIF region 6650,150,2450,2050 of 10711x5110',
'# (images/2077_legend_native.jpg), crops images/crops_2077_leg (tools/iiif_lines.py, command in NOTES.md GAPS19). Two blind Opus',
'# passes (passes/leg2077_passA.tsv, passB.tsv; brief passes/leg2077_pass_brief.md) aligned by passes/leg2077_merge.py, one blind',
'# Opus reconciliation (passes/leg2077_reconcile.tsv); built by passes/leg2077_build.py. conf H = both passes agree or the',
'# reconciliation rated H; M otherwise. L01-L03 title, L04 heading, L05-L19 legend rows, L20 below. GAPS19 (account-4), 3 Oct 2026.',
'# R10-SUR (6 Oct 2026): [sigma] split into [sigma-knot] (L11:17) and [sigma-hook] (L10:66), passes/sigma_split_r10/split.tsv;',
'# column sign_r9 = reader code before the split.',
'line\tpos\tsign\tconf\tnote\tsign_r9']
text='\n'.join(head+['\t'.join(map(str,r)) for r in rows])+'\n'
if '--check' in sys.argv: sys.exit(0 if open('ciphertext_2077_legend.tsv').read()==text else 1)
open('ciphertext_2077_legend.tsv','w').write(text)
print(len(rows),'signs;',sum(1 for r in rows if r[3]=='H'),'H;',sum(1 for r in rows if r[2].startswith('w:')),'plain')
