"""Build the key-image comparison sheet for eh, Tb and the two crosses (A2-GRA, 2 Oct 2026).
Inputs on disk only: Tomokiyo's table (sources/cryptiana/web/francisGramont.png), Lasry's table
(sources/cryptiana/web/GL/BnF_fr3071_f17.png), the leaf atlas (atlas/atlas_f29.png), the f.30 line crops
(images/crops_f30) and the f.30r cross crops (crops/f30r_top). No network."""
from PIL import Image, ImageDraw
import os
R = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(R, '..'); S = os.path.join(T, '../../sources/cryptiana/web')
tom = Image.open(f'{S}/francisGramont.png').convert('L'); las = Image.open(f'{S}/GL/BnF_fr3071_f17.png').convert('L')
atl = Image.open(f'{T}/atlas/atlas_f29.png').convert('L')
k = 1710/1500
panels = [
 ('Tomokiyo d e (cols x78-135)', tom.crop((75, 0, 140, 190)), 3),
 ('Tomokiyo n o p q (x285-390)', tom.crop((283, 0, 392, 190)), 3),
 ('Tomokiyo s t (x415-470)', tom.crop((415, 0, 472, 190)), 3),
 ('Tomokiyo row 5 + nulls (y135-165)', tom.crop((95, 132, 640, 168)), 2),
 ('Lasry D E (x135-220)', las.crop((133, 55, 222, 190)), 2),
 ('Lasry O P (x495-580)', las.crop((493, 55, 582, 230)), 2),
 ('Lasry T SS (x720-760, 0-140 at y300)', las.crop((718, 55, 762, 140)), 2),
 ('Lasry Unknown row', las.crop((0, 400, 270, 454)), 2),
 ('Leaf f.29r eh', atl.crop((int(0*k), int(1580*k), int(500*k), int(1685*k))), 1),
 ('Leaf f.29r Tb + T', atl.crop((int(1000*k), int(740*k), int(1500*k), int(945*k))), 1),
]
for nm in ['L03_CROSS', 'L07_CROSS', 'L11_CROSS', 'L12_lz']:
    im = Image.open(f'{T}/crops/f30r_top/{nm}.jpg').convert('L'); im.thumbnail((360, 260)); panels.append(('f.30r ' + nm, im, 1))
for nm in ['f30r_L04a', 'f30r_L04b']:
    im = Image.open(f'{T}/images/crops_f30/{nm}.jpg').convert('L'); panels.append(('f.30 ' + nm + ' (eh at pos 6,16,36)', im, 1))
W = 1400; rows = []; 
out = []
y = 0
for lab, im, sc in panels:
    im = im.resize((im.width*sc, im.height*sc))
    if im.width > W: im = im.resize((W, int(im.height*W/im.width)))
    out.append((lab, im)); 
H = sum(im.height + 22 for _, im in out)
sheet = Image.new('L', (W, H), 255); d = ImageDraw.Draw(sheet)
for lab, im in out:
    d.text((4, y + 4), lab, fill=0); sheet.paste(im, (0, y + 20)); y += im.height + 22
sheet.save(f'{R}/sheet.png'); print(sheet.size)
