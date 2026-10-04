#!/usr/bin/env bash
# Regenerate the line crops and debug overlays of ciphers/es132-vargas-mexia-1578/images removed on 4 Oct 2026
# (RUN3-ESSHR, LANE-RUN3) to bring the folder under CLAUDE.md's 30 MB rule. Every removed file was re-derived
# byte-identically from the committed native src_* region before deletion (382 of 383 checked; f119v_L12 was a
# separate --centres re-cut and was kept). Originals are also in git history at commit 351e2659.
# images_manifest_full.tsv lists every file with sha1, source, cited_by and status.
#
# Usage:
#   ./regen_images.sh local [PREFIX...]   # offline: re-cut crops + overlays from the committed src_* copies into images/
#   ./regen_images.sh check [PREFIX...]   # offline: re-cut into a temp dir and sha1-compare with images_manifest_full.tsv
#                                          # (expected: exactly one DIFF, f119v_L12.jpg, the kept --centres re-cut)
#   ./regen_images.sh fetch PREFIX        # network: refetch the native Gallica region (only needed for f41v, whose src
#                                          # is a 1600 px reference copy, and for the dup93 pages f93r-f95r)
# Good-citizen rule for fetch: one gallica.bnf.fr request at a time, >= 1.5 s apart.
set -euo pipefail
cd "$(dirname "$0")"
ROOT=$(git rev-parse --show-toplevel)
P=images/src_ark_12148_btv1b10032556x_
declare -A SRC=(
  [f90v]=f88_280_850_3000_3950 [f119r]=f116_3350_1850_2950_2850 [f119v]=f117_1050_2700_2300_2150
  [f89r]=f86_3450_1580_2950_3200 [f89v]=f87_520_880_2720_3980 [f119vU]=f117_900_1020_2500_1780
  [f120r]=f117_3600_1000_2600_1390 [f90r]=f87_3580_900_2680_3900 [f91r]=f88_3650_860_2650_1020
  [f41r]=f38_3500_1300_3150_3800 [f41v]=f39_650_850_2700_4300
)
# f41v and dup93 commands as recorded in NOTES.md (regions on canvases 39, 90-92)
declare -A FETCH=(
  [f41v]="--canvas 39 --region 650,850,2700,4300 --max-width 1450 --centres 241,365,495,609,731,869,985,1100,1226,1358,1499,1644,1775,1913,2064,2190,2334,2462,2597,2732,2856,3012,3143,3269,3405,3547,3679,3803,3929,4055,4177"
  [f93r]="--canvas 90 --region 3300,1200,3100,3600" [f93v]="--canvas 91 --region 550,880,2750,3950"
  [f94r]="--canvas 91 --region 3450,850,2900,3900" [f94v]="--canvas 92 --region 550,850,2750,3900"
  [f95r]="--canvas 92 --region 3650,280,2800,2200"
)
LOCAL=(f90v f119r f119v f89r f89v f119vU f120r f90r f91r f41r)

recut() {  # recut PREFIX OUTDIR
  python3 "$ROOT/tools/iiif_lines.py" --image "${P}${SRC[$1]}.jpg" --out "$2" --prefix "$1" \
    --follow-slope 300 --slope-margin 40 --debug >/dev/null
}

mode=${1:-}; shift || true
prefixes=("$@"); [ ${#prefixes[@]} -eq 0 ] && prefixes=("${LOCAL[@]}")
case "$mode" in
  local)
    for p in "${prefixes[@]}"; do
      t=$(mktemp -d); recut "$p" "$t"
      # copy only image files that are absent, so a kept file (e.g. f119v_L12) is never overwritten
      for f in "$t"/"$p"_*.jpg; do b=$(basename "$f"); [ -e "images/$b" ] || cp "$f" "images/$b"; done
      rm -rf "$t"; echo "regenerated $p"
    done ;;
  check)
    bad=0
    for p in "${prefixes[@]}"; do
      t=$(mktemp -d); recut "$p" "$t"
      for f in "$t"/"$p"_*.jpg; do
        b=$(basename "$f"); want=$(awk -F'\t' -v k="images/$b" '$1==k{print $3}' images_manifest_full.tsv)
        got=$(sha1sum "$f" | cut -d' ' -f1)
        if [ "$want" = "$got" ]; then :; else echo "DIFF $b"; bad=1; fi
      done
      rm -rf "$t"; echo "checked $p"
    done
    exit $bad ;;
  fetch)
    p=${prefixes[0]}; [ -n "${FETCH[$p]:-}" ] || { echo "no fetch recipe for $p"; exit 2; }
    out=images; [[ $p == f9[345]* ]] && out=images/dup93
    # shellcheck disable=SC2086
    python3 "$ROOT/tools/iiif_lines.py" --ark btv1b10032556x ${FETCH[$p]} --out "$out" --prefix "$p" \
      --follow-slope 300 --slope-margin 40 --debug ;;
  *) sed -n '2,13p' "$0"; exit 2 ;;
esac
