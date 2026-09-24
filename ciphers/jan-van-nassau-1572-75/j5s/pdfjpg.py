import re,sys,zlib
from PIL import Image
p=sys.argv[1]; out=sys.argv[2]; d=open(p,'rb').read(); k=0
for m in re.finditer(rb'<<([^>]*?/Subtype\s*/Image.*?)>>\s*stream\r?\n',d,re.S):
    h=m.group(1).decode('latin1'); s=m.end()
    L=int(re.search(r'/Length (\d+)',h).group(1)) if re.search(r'/Length (\d+)\b(?! 0 R)',h) else None
    e=s+L if L else d.find(b'endstream',s)
    w=int(re.search(r'/Width (\d+)',h).group(1)); ht=int(re.search(r'/Height (\d+)',h).group(1))
    cs='RGB' if 'RGB' in h else 'L'; bpc=int(re.search(r'/BitsPerComponent (\d+)',h).group(1))
    raw=zlib.decompress(d[s:e])
    mode = cs if bpc==8 else '1'
    im=Image.frombytes(mode,(w,ht),raw)
    k+=1; im.convert('L').save(f'{out}_p{k}.jpg',quality=85); print(k,w,ht,cs,bpc)
