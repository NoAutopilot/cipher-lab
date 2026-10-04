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
for t in test_bad test_ctx test_ctx2 test_focus test_mobile_ctx test_sorter test_undo test_s1_extras test_s2_sticky test_s2_picdrag test_s2_pilemerge test_recut; do run $t $t.js "$OUT/plain.html" "$OUT/$t.png"; done
run test_cluster_rank test_cluster_rank.js "$OUT/cluster.html" "$OUT/test_cluster_rank.png"
run test_refs test_refs.js "$OUT/refs.html" "$OUT/test_refs.png"
run test_pageview test_pageview.js "$OUT/region.html" "$OUT/test_pageview"
run test_qa test_qa.js "$OUT/plain.html" "$OUT/dump"
[ -n "$EXTRA" ] && run "test_qa ($EXTRA)" test_qa.js "$EXTRA"
exit $fail
