"""SUR-372 reconciliation R (worker's crop look, 9 Oct 2026): B as base; each A/B split settled by the rules below,
recorded per span in reconcile_R.log.tsv. Gloss rows and line structure from B (B carries the 14th gloss line A missed).
Agreed tokens are never changed (PREREG: R settles disagreements only)."""
import difflib, re
def rows(f): return [l.rstrip('\n').split('\t') for l in open(f, encoding='utf-8') if l.strip()]
def toks(c): return [t for t in c.split()]
CURLY = {'[other:curly', 'g-like', 'loop]', 'z-like]'}
def canon(ts):
    out=[];i=0
    while i<len(ts):
        t=ts[i]
        if t=='[other:curly':
            while not ts[i].endswith(']'): i+=1
            out.append('[other:curly]'); i+=1; continue
        out.append({'&':'[amp]','0':'o','g':'9','—':'-'}.get(t,t)); i+=1
    return out
# span decisions where the crops were looked at: (lineB, A-span, B-span) -> chosen
CHOOSE = {('L02','4 .',''):'', ('L03','n','w'):'w', ('L09','t','1'):'1', ('L09','[I-bar]','F'):'',
          ('L11','[ij]','S'):'[ij]', ('L11','[ij]','y'):'[ij]', ('L13','3','s'):'3', ('L13','[sigma]','[other:long s]'):'[sigma]',
          ('L13','b','6'):'b', ('L13','y','[ij]'):'y', ('L19','4','y'):'4', ('L21','[sigma]','[other:phi-like circle with stroke]'):'[sigma]',
          ('L21','f','[sh-lig]'):'f', ('L25','d','3'):'d', ('L25','e','c'):'c', ('L25','y','[ij]'):'y'}
A=[r for r in rows('passA.tsv') if r[1]=='cipher']; B=rows('passB.tsv'); log=open('reconcile_R.log.tsv','w'); log.write('lineB\tA\tB\tR\trule\n')
out=open('passR.tsv','w'); k=0
for r in B:
    if r[1]!='cipher': out.write('\t'.join(r)+'\n'); continue
    a=canon(toks(re.sub(r'\{[^}]*\}','',A[k][2]))); b=canon(toks(re.sub(r'\{[^}]*\}','',r[2]))); lid=r[0][-3:]; k+=1
    clear=re.findall(r'\{[^}]*\}', r[2]); a=[t for t in a if not t.startswith('{')]; b=[t for t in b if not t.startswith('{')]
    a2=[t for t in a if t!='_']; b2=[t for t in b if t!='_']
    sm=difflib.SequenceMatcher(None,a2,b2,autojunk=False); res=[]
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        sa,sb=' '.join(a2[i1:i2]),' '.join(b2[j1:j2])
        if op=='equal': res+=b2[j1:j2]; continue
        key=(lid,sa,sb)
        if key in CHOOSE: ch,rule=CHOOSE[key],'crop look'
        elif sb=='[sh-lig]' and sa in ('h','s','f'): ch,rule=sb,'crop look: long-s loop sign'
        elif sa=='.' and sb=='': ch,rule='', 'stray dot (B none)'
        elif sa=='' and sb=='.': ch,rule='', 'stray dot (A none)'
        else: ch,rule=sb,'default B'
        res+=ch.split(); log.write(f'{lid}\t{sa}\t{sb}\t{ch}\t{rule}\n')
    out.write(f"{r[0]}\tcipher\t{' '.join(clear+res)}\n")
print('R lines', k)
