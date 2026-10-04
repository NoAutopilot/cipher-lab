#!/usr/bin/env bash
# RUN2-NXATL (4 Oct 2026): regenerate the c510-516 (+ c262) family atlas, sequences.tsv and sign_counts.tsv.
# usage: bash regen.sh WORKDIR [--check]   (run from the repo root; needs numpy scipy scikit-image scikit-learn pillow opencv-python-headless)
# Fetches the 7 native canvases of Gallica btv1b9060927q (f510-f516) into WORKDIR if absent (7 requests, 2 s apart).
# Line centres are the committed line_centres.json (made by cen.py from the left 600 px of each block); crops stay in WORKDIR.
set -euo pipefail
W=$1; shift || true; R=$(pwd); N=$R/ciphers/fr16142-noailles-constantinople-1571/run2/nxatl; I=$R/ciphers/fr16142-noailles-constantinople-1571/images
mkdir -p "$W"; cd "$W"
for n in 510 511 512 513 514 515 516; do
  [ -s c$n.jpg ] || { curl -sS -A "Mozilla/5.0" -o c$n.jpg "https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060927q/f$n/full/full/0/native.jpg"; sleep 2; }
done
declare -A REG=([510]="1050,250,3780,5450" [511]="930,600,4050,4990" [512]="1180,40,3680,5480" [513]="900,560,3680,4980" [514]="900,560,3580,5060" [515]="820,600,3700,5130" [516]="1180,380,3650,4950")
for n in 510 511 512 513 514 515 516; do
  C=$(python3 -c "import json;print(','.join(map(str,json.load(open('$N/line_centres.json'))['$n'])))")
  python3 "$R/tools/iiif_lines.py" --image c$n.jpg --region ${REG[$n]} --centres $C --follow-slope 300 --slope-margin 15 \
    --max-width 2400 --overlap 100 --prefix c$n --out crops --debug > /dev/null
done
P=""; for f in "$I"/c262rc_L*_s*.jpg; do b=$(basename $f .jpg); P="$P --page c262_${b#c262rc_}=$f"; done
for f in crops/c51?_L*_s*.jpg; do b=$(basename $f .jpg); P="$P --page $b=$f"; done
rm -rf atl atlf
python3 "$R/tools/glyph_atlas.py" segment $P --out atl > seg_log.txt
python3 -c "
import json,glob,os
m={'c262_'+os.path.basename(f)[7:-4]:f for f in glob.glob('$I/c262rc_L*_s*.jpg')}
m.update({os.path.basename(f)[:-4]:f for f in glob.glob('crops/c51?_L*_s*.jpg')}); json.dump(m,open('pagemap.json','w'))"
python3 "$N/renorm.py" > /dev/null
python3 "$N/filt2.py" atl pagemap.json 100
python3 "$N/build.py" > build_log.txt
python3 "$R/tools/glyph_atlas.py" cluster --out atlf --k 120 --k-marks 24 > /dev/null
cp "$N/labels_clusterid.json" atlf/
python3 "$R/tools/glyph_atlas.py" classify --out atlf --labels atlf/labels_clusterid.json --page all --tsv atlf/classify_all.tsv --topk 3
TOL=$(python3 -c "
import json,hashlib; m=json.load(open('$N/source_manifest.json'))
print('' if all(hashlib.sha1(open(k+'.jpg','rb').read()).hexdigest()==v['sha1'] for k,v in m.items()) else '--tolerant')")
[ -n "$TOL" ] && echo "source canvases differ from source_manifest.json (Gallica re-encode): tolerant check"
cd "$R"
python3 "$N/make_sequences.py" "$W/atlf" "$N" "$@" $TOL
