#!/usr/bin/env python3
"""G1 (24 Sept 2026): hand alignment of WVO 5109's cipher (05109_p4.jpg bottom 8 lines, 05109_p5.jpg top 10 lines)
against Japikse (1934) no.236, pp.232-233, the spaced passage (plaintext by H. Koot per Japikse's footnote 5).
Writes pairs_5109.tsv and ciphertext_5109.tsv. unit '-' = sign with no plaintext counterpart; conf M = alignment doubtful.
Run with --check to verify committed files are current."""
import sys
# (line, [(sign, unit, conf, note)]); plaintext word boundaries shown by '|' entries (not written).
A = """
A1 d6:d f:e 88:r | 34:v vt:o:M:n_not_written_or_vt=on | ss:E +:g rf:m o:o cc:n 7:t | aab:h x:a 6:t
A2 tn:m hs:i xr:c xb:h | v2:g r:e p:f 88x:r ii:a +:g zz:t | vt:o vi:b
A3 44:v Ib:o cc:n | aaa:S th:-:M:abbreviation_mark_after_S(ondershausen)? | r:e 62:h f:e 8:r | oo:n 01:a
A4 a:c x_:h | gn:l phi:o z:t 101:h 88:r ob:i oo:n +:g 85:e or:n | 77:z
A5 fb:i g:e aab:h f:e ps:n | 34:v f:e 88x:r xm:d r:e cc:n | th:d rp:i
A6 f:e | p:b:M:same_shape_as_p=f_but_aligns_b ss:e:M:blotted 44:v 60:u ]:s z:t r:e | ott:p:M:shape_doubtful g:e 8+:r aaa:s vt:o cc:n
A7 tau:d f:e 3:m | 4000:König | 60:v o:o ox:n | xm:D r:e oo:n g:e 33:m x+:a 8:r
A8 xr:c dd:k | 77:z 48:u | p:f 88:r r:e rp:i xb:h f:e or:n | 34:u ps:n
P1 d6:d | rf:-:M:3_signs_not_in_print hs:-:M lx:-:M | 87:m 86:i 88:r | ii:a cc:n +:g r:e 63:z ss:e ob:i rr:g
P2 6:t | f:e 8:r | 44:w 48:-:M vt:o:M m:l:M | th:d r:e rf:m | of:l 60:u dot7:t
P3 53:z f:e tn:m xn:b 34:u 8+:r ro:g ss:e 88:r | f:e rp:i ps:n | sq:b 88x:r
P4 hs:i ss:e x+x:f | ]:s a:c 101:h 8:r r:e rp:i q:b f:e cc:n | th+:d r:e aaa:s
P5 hs:i oo:n x_:h x:a ne:l z:t | 33:m rp:i 8:r | 60:u 34:-:M or:n xn:b f:e
P6 48:w 60:u ]:s 6:t
P7 34:u p:f | xm:d x:a aaa:s
P7b 77:z
P8 60:u L:s r:e aab:h ss:e ps:n | tau:d 01:a aaa:s | oo:n hs:i xr:c xb:h dot7:t
P9 63:z | +:g g:e rr:g f:e or:n 34:-:M 44:w rp:i d:d r:e 88:r | tau:d r:e c:n | 4000:König
P10 r:g:M ss:e xb:h 01:a oo:n tau:d f:e gn:l zz:t | 60:w 48:e:M r:r:M 88:d:M xnr:e:M
"""
rows=[]
for ln in A.strip().splitlines():
    tag,*toks=ln.split(); word=1; idx=0
    for t in toks:
        if t=='|': word+=1; continue
        p=t.split(':'); idx+=1
        rows.append((tag,idx,word,p[0],p[1],p[2] if len(p)>2 else 'C',p[3].replace('_',' ') if len(p)>3 else ''))
out='line\tidx\tword\tsign\tunit\tconf\tnote\n'+''.join('\t'.join(map(str,r))+'\n' for r in rows)
ct='line\tpos\tsign\tconf\twhy\n'+''.join(f'{r[0]}\t{r[1]}\t{r[3]}\tH\tG1 reading\n' for r in rows)
if '--check' in sys.argv:
    ok=open('pairs_5109.tsv').read()==out and open('ciphertext_5109.tsv').read()==ct
    print('pairs_5109 current' if ok else 'STALE'); sys.exit(0 if ok else 1)
open('pairs_5109.tsv','w').write(out); open('ciphertext_5109.tsv','w').write(ct)
print(len(rows),'units')
