# VERIFY-BIRAGO-SMALL (3 Oct 2026): value-blind shuffled montage of the 12 no.87 tiles labelled T50/T46, panels lettered A-L, seed 4417.
# Run from harvest/: python3 lookalike_87/verify_blind/mk.py OUTDIR  (writes OUTDIR/vb/p*.png, blind.png, key.tsv; ImageMagick, no PIL).
import csv,glob,subprocess,random,sys,os
S=sys.argv[1]
tiles=[t for t in csv.DictReader(open('lookalike_87/tiles.tsv'),delimiter='\t') if t['sign'] in ('T50','T46')]
cnt={}
for fol in ['f178r','f178v','f179r']:
    for r in csv.DictReader(open(f'ciphertext_{fol}.tsv'),delimiter='\t'):
        cnt[r['line']]=max(cnt.get(r['line'],0),int(r['pos']))
def wh(f): return [int(x) for x in subprocess.check_output(['identify','-format','%w %h',f]).split()]
random.seed(4417); random.shuffle(tiles)
key=open(S+'/vb/key.tsv','w'); panels=[]
for i,t in enumerate(tiles):
    fol=t['folio']; L=t['line'].split('_')[1]
    segs=sorted(glob.glob(f'{fol}/{fol}_{L}_s*.jpg'))
    line=f'{S}/vb/line{i}.png'; subprocess.run(['convert',*segs,'+append',line],check=True)
    W,H=wh(line); n=cnt[t['line']]; p=int(t['pos']); cx=int((p-0.5)/n*W); half=int(W/n*2)
    x0=max(0,cx-half); out=f'{S}/vb/p{i}.png'
    subprocess.run(['convert',line,'-crop',f'{2*half}x{H}+{x0}+0','+repage','-resize','150%','-background','white','-gravity','north','-splice','0x22','-pointsize','18','-fill','red','-annotate','+0+0',chr(65+i),out],check=True)
    panels.append(out); key.write(f"{chr(65+i)}\t{t['line']}\t{t['pos']}\t{t['sign']}\n")
subprocess.run(['convert',*panels,'-append',S+'/vb/blind.png'],check=True)
