#!/bin/sh
# Run every sign-sorter browser test on freshly built synthetic fixtures (QA pass, 3 Oct 2026).
#   sh tools/sign_sorter/browser_tests/run_all.sh [OUT_DIR] [EXTRA_PAGE.html]
# EXTRA_PAGE (e.g. a real page such as Birago's) also gets test_qa.js. Exit 1 if any test fails or logs a page error.
set -u
HERE=$(cd "$(dirname "$0")" && pwd); OUT=${1:-$(mktemp -d)}; EXTRA=${2:-}
export PW_EXE=${PW_EXE:-/opt/pw-browsers/chromium} NODE_PATH=${NODE_PATH:-$(npm root -g)}
python3 "$HERE/make_fixtures.py" "$OUT" >/dev/null || exit 1
fail=0
run() { name=$1; shift; log=$(cd "$HERE" && timeout 600 node "$@" 2>&1); rc=$?
  if [ $rc -ne 0 ] || printf '%s' "$log" | grep -q "errors: \[ '"; then echo "FAIL $name"; printf '%s\n' "$log" | tail -15; fail=1; else echo "ok   $name"; fi; }
for t in test_bad test_ctx test_ctx2 test_focus test_mobile_ctx test_sorter test_undo test_s1_extras test_s2_sticky test_s2_picdrag test_s2_pilemerge test_recut test_addbox; do run $t $t.js "$OUT/plain.html" "$OUT/$t.png"; done
run test_cluster_rank test_cluster_rank.js "$OUT/cluster.html" "$OUT/test_cluster_rank.png"
run test_refs test_refs.js "$OUT/refs.html" "$OUT/test_refs.png"
run test_pageview test_pageview.js "$OUT/region.html" "$OUT/test_pageview"
run test_recut_quad test_recut_quad.js "$OUT/plain.html" "$OUT/test_recut_quad" "$OUT/region.html"
run test_qa test_qa.js "$OUT/plain.html" "$OUT/dump"
run test_focus_tray test_focus_tray.js "$OUT"   # template 2026-10-09.1: questions start in the tray (tray.html, tray_rank.html, plain.html)
run test_s2_fix test_s2_fix.js "$OUT"   # template 2026-10-09.6: step 2's Fix the cut (tray.html, plain.html; region.html: lines above and below) and the box-check key (tray_key.html)
# owner rule R09 (11 Oct 2026, Bergh: "slide my finger on the manuscript ... to see its surroundings"): the card's picture moves under a
# finger or a mouse, two fingers pinch the zoom, "Back to the sign", the swipe to the next sign only on the big sign, Fix the cut and the
# brush beside it; iPhone 13 + iPhone SE + mouse, on lines.html (line strips with lines above and below), region.html and plain.html
run test_pan test_pan.js "$OUT"
# owner rule R10 (11 Oct 2026, desktop: "ctrl+click + mouse scroll to zoom in and out"): Ctrl + wheel (and a trackpad pinch) on the card's
# picture zooms it around the pointer in step with the Zoom slider, the page itself does not zoom, a plain wheel scrolls, also while fixing
run test_wheel test_wheel.js "$OUT"
# the edges of R09-R11 found by the adversarial checks of 11 Oct 2026 (template 2026-10-09.7): Ctrl + wheel in the strips keeps the ink under the
# pointer, with the button held, after a lost release, over the enlarged sign; Enter after a nudge click saves; Alt/Ctrl + arrows are the
# browser's; iOS gesture events beside a finger pinch; Fix the cut fits an iPhone SE
run test_wheel_edges test_wheel_edges.js "$OUT"
# template 2026-10-09.5, owner rule R05 (tap = to the tray, hold = the card, every box; iPhone 13 + iPhone SE + mouse): the no-tray build
# (plain: '?' tiles), the tray build (tray: waiting '2' tiles, tray questions), both with a "Most useful first" box (tray_rank, cluster)
# and the earlier picks (refs: the check-mark tiles); round 2 (10 Oct 2026): region, whose r_L01-r_L03 line strips exercise R02 (the
# lines above and below in the card)
for f in plain tray tray_rank cluster refs region; do run "test_gestures ($f)" test_gestures.js "$OUT/$f.html"; done
# owner rule R11 (11 Oct 2026, Matignon f.110): the sign card walks the family it was opened in, stops at its ends, and a decision shows
# the next sign of that family; on the tray build (questions drawn in their piles) and the no-tray build
for f in family family_plain; do run "test_family_nav ($f)" test_family_nav.js "$OUT/$f.html" "$OUT/test_family_nav_$f.png"; done
# owner rule R12 (11 Oct 2026, Matignon f.110: "I need to lock the page in place, it kinda wiggles when you swipe left or right ... allowing me to
# swipe left or right through a pile would be great"; template 2026-10-09.8): a sideways swipe never moves the page; anywhere on the card but its
# picture it steps the card's walk, in step 2 on the pinned sign and above the pile cards it is Skip / Previous; never on a pile card or a pile
# tile; the tray still scrolls sideways; iPhone 13, iPhone SE and a 320 px phone with CDP touch, on plain.html and tray.html
run test_swipe test_swipe.js "$OUT" "$OUT"
[ -n "$EXTRA" ] && run "test_qa ($EXTRA)" test_qa.js "$EXTRA"
exit $fail
