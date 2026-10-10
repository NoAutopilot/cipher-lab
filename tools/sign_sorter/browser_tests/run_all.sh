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
# template 2026-10-09.5, owner rule R05 (tap = to the tray, hold = the card, every box; iPhone 13 + iPhone SE + mouse): the no-tray build
# (plain: '?' tiles), the tray build (tray: waiting '2' tiles, tray questions), both with a "Most useful first" box (tray_rank, cluster)
# and the earlier picks (refs: the check-mark tiles); round 2 (10 Oct 2026): region, whose r_L01-r_L03 line strips exercise R02 (the
# lines above and below in the card)
for f in plain tray tray_rank cluster refs region; do run "test_gestures ($f)" test_gestures.js "$OUT/$f.html"; done
[ -n "$EXTRA" ] && run "test_qa ($EXTRA)" test_qa.js "$EXTRA"
exit $fail
