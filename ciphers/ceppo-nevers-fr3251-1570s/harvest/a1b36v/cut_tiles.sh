#!/bin/sh
# A1B-CEPPO-36V (3 Oct 2026): tight tiles, fr.3252 f.36v, from the committed regions in ../witness_f36/.
# Line bands first cut for locating (scratch, not committed), ImageMagick because PIL is absent in this container
# (tools/iiif_lines.py needs PIL):  convert c38_f36v_{top,mid}.jpg -crop Wx185+X+(centre-120) +repage -auto-level
# Boxes are native px WxH+X+Y; -auto-level, upscaled 3x.  sh cut_tiles.sh -> tiles/*.png
cd "$(dirname "$0")"; W=../witness_f36
t(){ convert $W/$1 -crop $2 +repage -auto-level -resize 300% tiles/$3.png; }
t c38_f36v_mid.jpg 340x120+3150+515 T1   # v36mid_L05 pos 9-11 (target S32 pos 10)
t c38_f36v_mid.jpg 260x130+3080+70  T2   # v36mid_L01 pos 1-3 (target S76/S58 pos 2)
t c38_f36v_mid.jpg 360x110+1540+160 T3   # v36mid_L02 pos 10-12 (target S76/S58 pos 11)
t c38_f36v_mid.jpg 320x120+1620+600 T4   # v36mid_L06 pos 8-10 (target S76/S58 pos 9)
t c38_f36v_mid.jpg 320x120+2100+600 T5   # v36mid_L06 pos 14-16 (target S76/S58 pos 15)
t c38_f36v_top.jpg 360x115+1320+235 T6   # v36top_L02 (target S76/S58 pos 7)
