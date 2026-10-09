import sys
from PIL import Image
src,out,b=sys.argv[1],sys.argv[2],float(sys.argv[3])
im=Image.open(src)
X0,Y0,W=1740,1130,1700
cs=[17,65,127,171,214,263,305,359,403,476,520,578,634,671,710,752,817,873,928,984,1029,1112,1167]
H=86
for i,c in enumerate(cs,1):
    # strip whose centre row follows y = Y0+c + b*(x-X0) ; shear via affine
    top=Y0+c-H//2
    strip=im.transform((W,H),Image.AFFINE,(1,0,X0,b,1,top-b*X0+b*X0),resample=Image.BICUBIC)
    strip.save(f'{out}/b20s_L{i:02d}.jpg',quality=92)
