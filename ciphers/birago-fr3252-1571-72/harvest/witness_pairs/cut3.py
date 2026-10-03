from PIL import Image, ImageOps, ImageFilter
import sys
src,c,x0,x1,name=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),sys.argv[5]
im=Image.open(src).convert('L')
b=im.crop((x0,c-80,x1,c+45))
b=ImageOps.autocontrast(b,cutoff=2)
b=b.resize((b.width*3,b.height*3),Image.LANCZOS)
b.save(name)
