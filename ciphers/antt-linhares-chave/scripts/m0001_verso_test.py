# Run from ciphers/antt-linhares-chave/: python3 scripts/m0001_verso_test.py  (NEXT-LIN, 2 Oct 2026; needs Pillow and numpy)
# Verso test: flip m0001 horizontally, scale its paper box to m0002's paper box, blend, and write an overlay.
from PIL import Image, ImageOps, ImageChops
import numpy as np, sys
d='images/'
a=Image.open(d+'full_PT-TT-CLNH-0086-11_m0001.jpg.jpg').convert('L')
b=Image.open(d+'full_PT-TT-CLNH-0086-11_m0002.jpg.jpg').convert('L')
def paperbox(im, thr=60):
    arr=np.array(im); mask=arr>thr
    rows=np.where(mask.mean(1)>0.5)[0]; cols=np.where(mask.mean(0)>0.5)[0]
    return (cols[0],rows[0],cols[-1]+1,rows[-1]+1)
# m0001 has a colour checker at the right: restrict to x<1160 before boxing
a_crop=a.crop((0,0,1160,a.height))
ba=paperbox(a_crop); bb=paperbox(b)
print('paper box m0001',ba,'size',ba[2]-ba[0],ba[3]-ba[1])
print('paper box m0002',bb,'size',bb[2]-bb[0],bb[3]-bb[1])
pa=a_crop.crop(ba); pb=b.crop(bb)
pa_f=ImageOps.mirror(pa).resize(pb.size)
# equalise and blend: m0002 in red channel, flipped m0001 in green
pa_e=ImageOps.autocontrast(pa_f, cutoff=2); pb_e=ImageOps.autocontrast(pb, cutoff=2)
rgb=Image.merge('RGB',(pb_e,pa_e,ImageChops.lighter(pa_e,pb_e)))
rgb.save(d+'m0001_verso_overlay.jpg',quality=80)
# normalised cross-correlation of ink maps at zero shift vs best small shift
def ink(im): arr=np.array(im,dtype=float); return (arr< np.percentile(arr,8)).astype(float)
ia=ink(pa_e); ib=ink(pb_e)
def ncc(x,y): x=x-x.mean(); y=y-y.mean(); return float((x*y).sum()/np.sqrt((x*x).sum()*(y*y).sum()))
print('NCC ink(flipped m0001) vs ink(m0002), zero shift: %.3f'%ncc(ia,ib))
# control: unflipped m0001 (same paper, same scale, not mirrored)
pa_u=ImageOps.autocontrast(pa.resize(pb.size),cutoff=2); iu=ink(pa_u)
print('control NCC unflipped m0001 vs m0002: %.3f'%ncc(iu,ib))
# control 2: flipped m0005 (an unrelated leaf on the same unit) vs m0002
c=Image.open(d+'full_PT-TT-CLNH-0086-11_m0005.jpg.jpg').convert('L'); bc=paperbox(c); pc=c.crop(bc)
pc_f=ImageOps.autocontrast(ImageOps.mirror(pc).resize(pb.size),cutoff=2); ic=ink(pc_f)
print('control NCC flipped m0005 vs m0002: %.3f'%ncc(ic,ib))
# best shift search +-30 px for the flipped m0001
best=(-9,0,0)
for dx in range(-30,31,3):
  for dy in range(-30,31,3):
    s=np.roll(np.roll(ia,dy,0),dx,1); v=ncc(s,ib)
    if v>best[0]: best=(v,dx,dy)
print('best NCC flipped m0001 within +-30 px: %.3f at dx=%d dy=%d'%best)
