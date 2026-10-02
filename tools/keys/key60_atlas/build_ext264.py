import csv, os
from PIL import Image, ImageDraw, ImageFont
R='tools/keys/key60_atlas'; src=Image.open(f'{R}/src/c264_region.jpg').convert('L')
# sign_id, tag, form, value, x0,y0,x1,y1 (native, c264_region.jpg), context, gloss word, print
rows=[
 ('A53','L40','L with loop and o (as leaf 298 writes qui)','qui',505,1975,610,2035,'[qui]tes','quites','soient quites & absous'),
 ('A54','8','8','t',666,1975,706,2035,'qui[t]es','quites','soient quites & absous'),
 ('A55','r','r-shaped','s',826,1975,876,2035,'quite[s]','quites','soient quites & absous'),
 ('A56','r','r-shaped','s',1945,1868,1998,1918,'lor[s]','lors','que deslors ses suiets'),
 ('A57','c','c (table: c = s and c = a)','s',2098,1868,2142,1918,'se[s]','ses','que deslors ses suiets'),
 ('A58','ue','u + e','e',2425,1868,2488,1918,'subj[e]cts','subjects','ses suiets soient quites'),
 ('A59','ue','u + e','e',465,2235,550,2290,'troisi[e]sme','troisiesme','La troisieme'),
 ('A60','20','20 (a-u-me: this hand writes 20 as two figures here)','u',1590,2225,1670,2295,'roya[u]me','roy\'me','Rois de ce Royaume'),
 ('A61','=','two bars with an oblique stroke (table: = and =/= both d)','d',285,2355,340,2425,'la [d]venir','l\'advenir','qu\'a l\'aduenir'),
 ('A62','//','two slants','c',1825,2355,1880,2425,'sa[c]re','sacre','a leur Sacre'),
]
tile=190; ctx=70; per=6
font=ImageFont.load_default()
tiles=[]
with open(f'{R}/atlas264ext.tsv','w') as f:
    f.write('sign_id\ttag\tform\tvalue_under_gloss\tcontext\tx0\ty0\tx1\ty1\tgloss_word\tprint\n')
    for sid,tag,form,val,x0,y0,x1,y1,ctxt,gw,pr in rows:
        f.write('\t'.join(map(str,[sid,tag,form,val,ctxt,x0,y0,x1,y1,gw,pr]))+'\n')
        cx,cy=(x0+x1)//2,(y0+y1)//2; half=max(x1-x0,y1-y0)//2+ctx
        c=src.crop((cx-half,cy-half,cx+half,cy+half)).resize((tile,tile),Image.LANCZOS)
        d=ImageDraw.Draw(c); s=tile/(2*half)
        d.rectangle([ (x0-cx+half)*s,(y0-cy+half)*s,(x1-cx+half)*s,(y1-cy+half)*s ],outline=0,width=2)
        lab=Image.new('L',(tile,44),255); dl=ImageDraw.Draw(lab)
        dl.text((2,1),f'{sid} {tag} = {val}',fill=0,font=font); dl.text((2,15),form[:34],fill=0,font=font); dl.text((2,29),ctxt,fill=0,font=font)
        t=Image.new('L',(tile,tile+44),255); t.paste(c,(0,0)); t.paste(lab,(0,tile)); tiles.append(t)
base=Image.open(f'{R}/contact_sheet_264only.png').convert('L')
nrows=(len(tiles)+per-1)//per; block=Image.new('L',(base.size[0],60+nrows*(tile+44+6)),255)
db=ImageDraw.Draw(block); db.text((4,4),'EXTENSION (GAPS, 2 Oct 2026): leaf-264 lower lines, c264_region.jpg, aligned on the printed Instruction (Memoires de Nevers ii 498)',fill=0,font=font)
db.text((4,18),'box = the sign; same leaf and hand as A01-A52; no leaf-298 material',fill=0,font=font)
for i,t in enumerate(tiles): block.paste(t,(4+(i%per)*(tile+40),40+(i//per)*(tile+44+6)))
out=Image.new('L',(base.size[0],base.size[1]+block.size[1]),255); out.paste(base,(0,0)); out.paste(block,(0,base.size[1]))
out.save(f'{R}/contact_sheet_264ext.png'); print(out.size, len(rows),'rows')
