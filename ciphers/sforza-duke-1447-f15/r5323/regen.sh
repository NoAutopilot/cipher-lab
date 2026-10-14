#!/bin/sh
# SFZ-R5323 images (not committed: DECODE files need the holder's permission to publish). One browser login, 12 PDFs by filename
# (filenames and sha1s in ../decode_1597/manifest.json), then the crops the blind readers saw.
set -e; D=${1:-./img}; mkdir -p "$D"
U=""; for f in IMG_R5323_I30301_P IMG_R5324_I30302_P IMG_R5302_I30274_P IMG_R5304_I30276_P IMG_R5305_I30279_P IMG_R5306_I30280_P IMG_R5309_I30285_P IMG_R5310_I30286_P IMG_R5311_I30287_P IMG_R5312_I30288_P IMG_R5313_I30289_P IMG_R5315_I30291_P; do U="$U,https://de-crypt.org/decrypt-custom/filesrv/?file=$f.pdf"; done
NODE_PATH=$(npm root -g) node ../../../tools/decode_browser_login.js 5323 "$D" --fetch "${U#,}" --max-files 12 --delay 1600
cd "$D"; for f in IMG_*.pdf; do pdftoppm -r 150 -png "$f" "${f%.pdf}"; done; pdftoppm -r 300 -png IMG_R5323_I30301_P.pdf hi5323
python3 - <<'PY'
from PIL import Image; import glob
im=Image.open('hi5323-1.png'); im.crop((80,230,1250,700)).save('c5323_left.png'); im.crop((1150,230,2300,700)).save('c5323_right.png')
for f in glob.glob('IMG_R53*-1.png'):
    r=f[5:9]
    if r!='5323':
        i=Image.open(f); w,h=i.size; i.crop((0,0,w,int(h*0.5))).save('ctl_%s.png'%r)
PY
