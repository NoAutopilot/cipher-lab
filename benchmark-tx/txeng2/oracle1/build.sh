#!/bin/sh
# OL1-BOXES (PREREG-txeng2-21, TXE2-OL1BOXES, 10 Oct 2026): regenerate the boxes, overlays and the blind box-verify sorter page
# from the repo root. Read-free: segment (default mode) -> build_ol1_boxes.py -> sign_sorter.py blind -> sorter_preflight.py.
#   sh benchmark-tx/txeng2/oracle1/build.sh            (needs opencv-python-headless for the segment step)
set -e
O=benchmark-tx/txeng2/oracle1; T=${TMPDIR:-/tmp}/ol1_boxes_seg; D=$O/sorter
sha256sum -c $O/manifest.tsv.sha256 --status 2>/dev/null || (cd $O && sha256sum -c manifest.tsv.sha256)
for h in vivonne1573-f102r birago1572-no87 luzerne108a-p1; do
  args=$(awk -F'\t' -v h=$h '$1==h{n=split($3,c,";"); for(i=1;i<=n;i++){f=c[i]; sub(/.*\//,"",f); sub(/\.jpg$/,"",f); printf " --page %s=%s", f, c[i]}}' $O/manifest.tsv)
  python3 tools/glyph_atlas.py segment $args --out $T/$h > /dev/null
done
python3 $O/build_ol1_boxes.py $T
python3 tools/sign_sorter.py --signs $D/signs.tsv --labels $D/labels.tsv --pages $D/pages.json \
  --title "Oracle boxes: verify the cuts" \
  --lede "Verify the machine-proposed sign boxes and their reading order on these 35 lines (3 hands). For each box: accept it, or mark it a bad cut and move, split or merge it with Fix the cut; add a box where a sign has none. Never read a value. Time the first 100 signs and write minutes per 100 signs in the result before continuing; stop at 1,500 signs." \
  --tile-quality 70 --out $D/oracle_boxes_sorter.html --data-out $D/oracle_boxes_sorter.json --no-preflight
# The tool's blind seed note says the tiles were "first piled by our readers' labels"; here no reader ran (one neutral pile),
# so the note is replaced by a true one in both outputs (the only edit to the tool's output; no value, label or guess added).
python3 - "$D/oracle_boxes_sorter.html" "$D/oracle_boxes_sorter.json" <<'PY'
import sys
old = 'first piled by our readers’ labels; this page shows no key values and no decode choices, so what you decide is blind.'
new = 'all in one pile, unsorted: no reader, no label and no machine guess went into this page, so what you decide is blind.'
for p in sys.argv[1:]:
    s = open(p, encoding='utf-8').read(); n = 0
    for o in (old, old.replace('\u2019', '\\u2019')):
        n += s.count(o); s = s.replace(o, new)
    open(p, 'w', encoding='utf-8').write(s); print(p, 'seed note replaced', n)
PY
python3 tools/sorter_preflight.py $D/oracle_boxes_sorter.html --cipher-lines $D/cipher_lines.tsv --pages-json $D/pages.json || true
