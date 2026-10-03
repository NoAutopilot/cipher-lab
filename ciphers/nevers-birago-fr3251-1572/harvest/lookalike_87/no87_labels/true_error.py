# NO87-LABELS (3 Oct 2026): true error of the committed no.87 decode against the clerk's clear sheet, per aligned token.
# Run from harvest/: python3 lookalike_87/no87_labels/true_error.py [--list]. Truth = align87/align_real.tsv plain_chunk
# (the clerk sheet aligned by NEVBIR-87ALIGN); decode = reading_f17{8r,8v,9r}_tokens.tsv value. Unaligned tokens are skipped.
import csv,sys
tot=wrong=unk=0; out=[]
for fol in ['f178r','f178v','f179r']:
    toks=list(csv.DictReader(open(f'reading_{fol}_tokens.tsv'),delimiter='\t'))
    al={int(r['idx']):r for r in csv.DictReader(open('align87/align_real.tsv'),delimiter='\t') if r['cipher_line']==fol}
    for i,t in enumerate(toks):
        a=al.get(i)
        if not a or not a['plain_chunk']: continue
        tot+=1; v=t['value']
        if v in ('','?') or t['grade']=='U': unk+=1; out.append((fol,t['line'],t['pos'],t['sign'],v,a['plain_chunk'],'U')); continue
        if v!=a['plain_chunk']: wrong+=1; out.append((fol,t['line'],t['pos'],t['sign'],v,a['plain_chunk'],'wrong'))
print(f'aligned {tot} wrong {wrong} unvalued {unk} true_error {wrong/tot:.4f} (wrong+U {(wrong+unk)/tot:.4f})')
if '--list' in sys.argv:
    for o in out: print(*o,sep='\t')
