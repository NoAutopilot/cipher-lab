#!/bin/sh
# Re-cut every RUN2-NXTB crop at full quality from the Gallica native canvases (fr.16142, btv1b9060927q, canvases 515 and 516).
# The committed crops are JPEG q40 copies; the passes read these q90 cuts. Run from the repository root.
set -e
D=${TMPDIR:-/tmp}/nxtb_src; mkdir -p "$D"; O=ciphers/fr16142-noailles-constantinople-1571/run2/nxtb/crops
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
for f in 516 515; do [ -s "$D/f$f.jpg" ] || { curl -sS -A "$UA" -o "$D/f$f.jpg" "https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060927q/f$f/full/full/0/native.jpg"; sleep 2; }; done
python3 tools/iiif_lines.py --image "$D/f516.jpg" --region 1150,700,3600,420 --centres 72,202,334 --follow-slope 300 --slope-margin 15 --max-width 1850 --overlap 100 --prefix c516a --out $O --debug
python3 tools/iiif_lines.py --image "$D/f516.jpg" --region 1150,1330,3600,2030 --centres 101,225,360,484,596,731,866,990,1125,1249,1384,1508,1631,1766,1901 --follow-slope 300 --slope-margin 15 --max-width 1850 --overlap 100 --prefix c516b --out $O --debug
python3 tools/iiif_lines.py --image "$D/f515.jpg" --region 850,600,3600,5200 --centres 89,237,373,496,635,750,872,995,1117,1233,1361,1489,1612,1749,1874,2001,2131,2272,2400,2520,2644,2770,2888,3005,3141,3274,3387,3510,3643,3760,3898,4021,4142,4261,4405,4532,4676,4791,4918,5035 --follow-slope 300 --slope-margin 15 --max-width 1850 --overlap 100 --prefix c515 --out $O --debug
# c516b L04: --follow-slope tracked the ink smear (L05); straight shear by hand instead
(cd ciphers/fr16142-noailles-constantinople-1571/run2/nxtb && python3 shear_L04.py "$D/f516.jpg" crops && python3 tick_s2.py)
