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
# OL1-PAGE amended (PREREG-txeng2-21, TXE2-OL1PAGE): re-cut by the declared per-hand geometric rules, piles = cut kind only.
python3 $O/recut_ol1_boxes.py
python3 tools/sign_sorter.py --signs $D/signs.tsv --labels $D/labels.tsv --pages $D/pages.json --marks $D/marks.tsv \
  --focus $D/focus.tsv --focus-note "These boxes were changed by a geometric rule (split, trimmed, padded, or a detached mark joined to its sign). Check each cut first." \
  --title "Oracle boxes: verify the cuts" \
  --lede "Verify the machine-proposed sign boxes and their reading order on these 35 lines (3 hands). For each box: accept it, or mark it a bad cut and move, split or merge it with Fix the cut; add a box where a sign has none. Never read a value. Time the first 100 signs and write minutes per 100 signs in the result before continuing; stop at 1,500 signs. The two piles are only the machine's cut kind (a sign box, or a small mark with no sign in reach), not a reading." \
  --tile-quality 70 --out $D/oracle_boxes_sorter.html --data-out $D/oracle_boxes_sorter.json --no-preflight
# The tool's blind seed note says the tiles were "first piled by our readers' labels"; here no reader ran (piles = the machine's
# cut kind), so the note is replaced by a true one in both outputs (the only edit to the tool's output; no value, label or guess added).
python3 - "$D/oracle_boxes_sorter.html" "$D/oracle_boxes_sorter.json" <<'PY2'
import sys
old = 'first piled by our readers’ labels; this page shows no key values and no decode choices, so what you decide is blind.'
new = 'piled only by the machine’s cut kind (sign box, mark box): no reader, no label and no machine guess of a value went into this page, so what you decide is blind.'
for p in sys.argv[1:]:
    s = open(p, encoding='utf-8').read(); n = 0
    for o in (old, old.replace('\u2019', '\\u2019')):
        n += s.count(o); s = s.replace(o, new if o == old else new.replace('\u2019', '\\u2019'))
    open(p, 'w', encoding='utf-8').write(s); print(p, 'seed note replaced', n)
PY2
python3 tools/sorter_preflight.py $D/oracle_boxes_sorter.html --cipher-lines $D/cipher_lines.tsv --pages-json $D/pages.json || true   # FAIL 6.9% on record (RESULTS.md "## OL1-PAGE"); withheld
# OL1-PAGE, the next rule (PREREG-txeng2-21): one page per hand from the same re-cut inputs; luzerne boxes padded 4 px a side.
python3 $O/split_per_hand.py
LEDE="Verify the machine-proposed sign boxes and their reading order on these lines (one hand). For each box: accept it, or mark it a bad cut and move, split or merge it with Fix the cut; add a box where a sign has none. Never read a value. Time the first 100 signs and write minutes per 100 signs in the result before continuing; stop at 1,500 signs. The two piles are only the machine's cut kind (a sign box, or a small mark with no sign in reach), not a reading."
for h in vivonne birago luzerne; do
  H=$D/$h
  python3 tools/sign_sorter.py --signs $H/signs.tsv --labels $H/labels.tsv --pages $H/pages.json --marks $H/marks.tsv \
    --focus $H/focus.tsv --focus-note "These boxes were changed by a geometric rule (split, trimmed, padded, or a detached mark joined to its sign). Check each cut first." \
    --title "Oracle boxes ($h): verify the cuts" --lede "$LEDE" \
    --tile-quality 70 --out $D/oracle_boxes_$h.html --data-out $H/oracle_boxes_$h.json --no-preflight
  python3 - "$D/oracle_boxes_$h.html" "$H/oracle_boxes_$h.json" <<'PY2'
import sys
old = 'first piled by our readers’ labels; this page shows no key values and no decode choices, so what you decide is blind.'
new = 'piled only by the machine’s cut kind (sign box, mark box): no reader, no label and no machine guess of a value went into this page, so what you decide is blind.'
for p in sys.argv[1:]:
    s = open(p, encoding='utf-8').read(); n = 0
    for o, nw in ((old, new), (old.replace('\u2019', '\\u2019'), new.replace('\u2019', '\\u2019'))):
        n += s.count(o); s = s.replace(o, nw)
    open(p, 'w', encoding='utf-8').write(s); print(p, 'seed note replaced', n)
PY2
  python3 tools/sorter_preflight.py $D/oracle_boxes_$h.html --cipher-lines $H/cipher_lines.tsv --pages-json $H/pages.json --sheet $H/oracle_boxes_$h.preflight.png || true
done
