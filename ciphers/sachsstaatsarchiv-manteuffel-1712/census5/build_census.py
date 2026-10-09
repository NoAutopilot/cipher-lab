#!/usr/bin/env python3
"""MANT-CEN5: rebuild census_unglossed.tsv from the folder's inventories (disk only, no fetch).
Usage: python3 census5/build_census.py [--check]   (run from the target folder)
One row per 694/08|09 frame any inventory calls code (y/possible/?); evidence = eye (zoom/native) vs sheet only.
Overrides: census5/mant_cen5_looks.tsv (frame<TAB>loc<TAB>code<TAB>glossed<TAB>note) from the MANT-CEN5 sheet looks."""
import csv,glob,re,sys,os,collections
OUT='census_unglossed.tsv'
rec=collections.defaultdict(list)   # (loc,frame)->[dict]
def add(loc,fr,src,code,glossed,note,density='',est='',rng='',scale=''):
    rec[(loc,fr)].append(dict(src=src,code=code,glossed=glossed,note=note,density=density,est=est,rng=rng,scale=scale))
def rows(f):
    for l in open(f):
        if l.startswith('#') or not l.strip(): continue
        yield l.rstrip('\n').split('\t')
for f in sorted(glob.glob('mant0608/inv08?.tsv')):
    for p in rows(f):
        if p[0]=='loc': continue
        add(p[0],p[1],os.path.basename(f),p[5],p[6],p[9],p[7],p[8],'',  'sheet' if 'not eye-checked' in p[9] else 'eye')
for p in rows('mant0608/inventory_stride4.tsv'):
    if p[0]=='loc': continue
    add(p[0],p[1],'inventory_stride4',p[7],p[8],p[11],p[9],p[10],'','sheet' if 'not eye-checked' in p[11] else 'eye')
for p in rows('mant0609/inventory_sample.tsv'):
    if p[0]=='loc': continue
    add(p[0],p[1],'inventory_sample',p[2],p[3],p[4],scale='eye')
for p in rows('mant0609/inventory_stride3.tsv'):
    if p[0]=='loc': continue
    add(p[0],p[1],'inventory_stride3',p[5],p[6],p[7],scale='sheet' if 'not eye-checked' in p[7] else 'eye')
for f,n in (('nzmant2/inventory_0005_0495.tsv','nzmant2'),('r13mant/inventory_0581_plus.tsv','r13mant'),('mant0609/seen_before.tsv','seen_before')):
    for p in rows(f):
        if p[0]=='loc': continue
        add(p[0],p[1],n,p[2],p[3],p[-1] if n=='seen_before' else p[5],rng=p[4],scale='eye')
for p in rows('nzmant/inventory_0581_0592.tsv'):
    if p[0]=='loc': continue
    add(p[0],p[1],'nzmant',p[3],p[4],p[7],rng=p[5],scale='eye')
for p in rows('n9mant/inventory_0504_0578.tsv'):
    if p[0]=='frame': continue
    add('694/08',p[0],'n9mant','y' if p[3].startswith('cipher') else 'n','?',p[4],scale='sheet')
for p in rows('frame_classify_gaps207.tsv'):
    if p[0]=='frame': continue
    add('694/08',p[0],'gaps207','y',p[3],p[7],rng=p[4],scale='native')
for p in rows('frame_inventory.tsv'):
    if p[0]=='loc': continue
    add(p[0],p[1],'frame_inventory',p[3],p[4],p[2],scale='eye')
if os.path.exists('census5/mant_cen5_looks.tsv'):
    for p in rows('census5/mant_cen5_looks.tsv'):
        if p[0]=='frame': continue
        add(p[1],p[0],'MANT-CEN5',p[2],p[3],p[4],est=(re.search(r'about (\d+) tokens',p[4]) or [0,''])[1] if re.search(r'about (\d+) tokens',p[4]) else '',scale='eye')
def norm(c):
    c=c.strip().lower()
    return 'y' if c in('y','yes','code','cipher','code groups present') else ('possible' if c in('possible','?') else ('n' if c in('n','none','-','') else c))
# NOTES section mentions
secs=[]
for fn in ('NOTES.md','AUDIT.md','HYPOTHESES.md'):
    cur=None;buf=[]
    for l in open(fn):
        if l.startswith('## '):
            if cur: secs.append((fn,cur,'\n'.join(buf)))
            cur=l[3:].strip().split(' ')[0].strip('(:');buf=[]
        else: buf.append(l)
    if cur: secs.append((fn,cur,'\n'.join(buf)))
skip=re.compile(r'CEN|CENSUS|INV08|0609|NZ-MANT|GAPS201|GAPS184|GAPS162|A2-SAX|N9-MANT2|YCEN|ABBO')
cropdirs=glob.glob('f[0-9][0-9][0-9][0-9]*')+glob.glob('f4*')
def crops(fr):
    out=[]
    for d in glob.glob('f%s*'%fr):
        out+=[os.path.join(d,x) for x in sorted(os.listdir(d))[:2] if x.lower().endswith(('.jpg','.png'))]
    out+=sorted(glob.glob('census5/eye_*_%s.jpg'%fr))
    for d in glob.glob('*/census'):
        out+=sorted(glob.glob(d+'/*%s*.jpg'%fr))[:1]
    return out[:2]
hdr=['loc','frame','code','gloss','clear_follows','est_code_tokens','density','evidence_scale','sources','already_read_by','crop_path','note']
res=[]
for (loc,fr),L in sorted(rec.items()):
    if loc not in('694/08','694/09'): continue
    codes=[norm(x['code']) for x in L]
    if not any(c in('y','possible') for c in codes): continue
    ypos=[x for x in L if norm(x['code']) in('y','possible')]
    g=[x['glossed'].strip().lower() for x in ypos if x['glossed'].strip() not in('','-','?')]
    gl='yes' if any(x in('y','yes') for x in g) else ('partial' if any(x.startswith(('part','p')) for x in g) else ('no' if any(x in('n','no') for x in g) else '?'))
    fullnote=' | '.join(x['note'] for x in ypos if x['note']); note=fullnote[:260]
    clear='no' if re.search(r'no clear rendering',fullnote) else ('yes' if re.search(r'right (page )?(letter|German|French|clear)|clear (copy|rendering|German|French)|followed by',fullnote,re.I) else '?')
    est=next((x['est'] for x in ypos if x['est']),'')
    dens=next((x['density'] for x in ypos if x['density'] not in('','-')),'')
    scale='native' if any(x['scale']=='native' for x in ypos) else ('eye' if any(x['scale']=='eye' for x in ypos) else 'sheet')
    rb=[]
    for fn,sec,txt in secs:
        if skip.search(sec): continue
        if re.search(r'(?<!\d)%s(?!\d)'%fr,txt): rb.append(sec)
    cr=crops(fr)
    res.append([loc,fr,'y' if any(c=='y' for c in codes) else 'possible',gl,clear,est,dens,scale,','.join(sorted({x['src'] for x in L})),','.join(dict.fromkeys(rb))[:120] or '-',','.join(cr) or '-',note])
out='\t'.join(hdr)+'\n'+'\n'.join('\t'.join(r) for r in res)+'\n'
if '--check' in sys.argv:
    sys.exit(0 if open(OUT).read()==out else 1)
open(OUT,'w').write(out); print(len(res),'rows')
