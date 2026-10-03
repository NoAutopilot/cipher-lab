# GAPS19-na-suriname-map-1781 (account-4), 3 Oct 2026: build ciphertext_2077_legend.tsv from passes/leg2077_merged.tsv
# (leg2077_merge.py: two blind Opus passes) and passes/leg2077_reconcile.tsv (one blind Opus reconciliation call).
# Plain tokens <...> -> w:<text>. Usage: python3 passes/leg2077_build.py [--check]  (exit 1 if the committed file is stale)
import csv,sys
LINE={f'leg77_L{i:02d}':f'2077_L{i:02d}' for i in range(1,21)}  # L01-L03 title, L04 heading, L05-L19 legend rows, L20 line below
M=list(csv.DictReader(open('passes/leg2077_merged.tsv'),delimiter='\t'))
R={}
for r in csv.DictReader((l for l in open('passes/leg2077_reconcile.tsv') if not l.startswith('#')),delimiter='\t'):
    if r['pos'].strip().isdigit(): R[(r['crop'].strip(),int(r['pos']))]=r
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
        if s.startswith('<') and s.endswith('>'): s='w:'+s[1:-1]
        rows.append((LINE[c],j,s,g,n))
head=['# NA 4.VEL 2077 (Plan van de fortress Zelandia, 1781): title cartouche 3 lines, plain heading, the mixed plain/cipher',
'# "Explicatie der Signatuuren" legend a-z and the line below it. Native IIIF region 6650,150,2450,2050 of 10711x5110',
'# (images/2077_legend_native.jpg), crops images/crops_2077_leg (tools/iiif_lines.py, command in NOTES.md GAPS19). Two blind Opus',
'# passes (passes/leg2077_passA.tsv, passB.tsv; brief passes/leg2077_pass_brief.md) aligned by passes/leg2077_merge.py, one blind',
'# Opus reconciliation (passes/leg2077_reconcile.tsv); built by passes/leg2077_build.py. conf H = both passes agree or the',
'# reconciliation rated H; M otherwise. L01-L03 title, L04 heading, L05-L19 legend rows, L20 below. GAPS19 (account-4), 3 Oct 2026.',
'line\tpos\tsign\tconf\tnote']
text='\n'.join(head+['\t'.join(map(str,r)) for r in rows])+'\n'
if '--check' in sys.argv: sys.exit(0 if open('ciphertext_2077_legend.tsv').read()==text else 1)
open('ciphertext_2077_legend.tsv','w').write(text)
print(len(rows),'signs;',sum(1 for r in rows if r[3]=='H'),'H;',sum(1 for r in rows if r[2].startswith('w:')),'plain')
