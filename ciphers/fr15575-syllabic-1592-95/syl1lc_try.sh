#!/usr/bin/env bash
# SYL-1LC (13 Oct 2026, LANE DEFAULT-A2-2013): single-letter-class --try control for the no.54 legend marks on f.228 L01-L08.
# PREREG-SYL-1LC.md. Builds environment E in a scratch dir (f228 ciphertext unchanged; key = f228/key_syllabary.tsv + the
# H-graded no.54 header letter signs of key_no54.tsv except n), then runs the control (one call per masked sign, the sign
# dropped from E's key) and, only if the control passes its gate, the target calls. Never writes a committed key.
# Usage: bash ciphers/fr15575-syllabic-1592-95/syl1lc_try.sh SCRATCH_DIR [control|target]
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
D=ciphers/fr15575-syllabic-1592-95
S=${1:?scratch dir}; MODE=${2:-control}
OPTS=(--lm tools/data/es1600 --window 8 --nulls 100)
build() {  # build ENV_DIR [sign to drop]
  rm -rf "$1"; mkdir -p "$1"
  cp $D/f228/ciphertext.tsv $D/f228/ciphertext_b2.tsv $D/f228/decode.json "$1"/
  { cat $D/f228/key_syllabary.tsv
    awk -F'\t' -v drop="${2:-}" '$3=="letter sign (header)" && $4=="H" && $1!="n" && $1!=drop {print $1"\t"$2"\tH\tSYL-1LC env E: no.54 header letter sign"}' $D/key_no54.tsv
  } > "$1"/key_syllabary.tsv
}
if [ "$MODE" = control ]; then
  for pair in ':=r,:=l' 'y=r,y=s' '9=y,9=e'; do
    true_h=${pair%%,*}; wrong_h=${pair##*,}; sign=${true_h%%=*}
    E="$S/ctl_$(printf %s "$sign" | od -An -tx1 | tr -d ' \n')"
    build "$E" "$sign"
    for h in "$true_h" "$wrong_h"; do
      echo "== control $h (sign dropped from E)"
      python3 tools/decode_key.py "$E" --try "$h" "${OPTS[@]}" --try-log "$S/control_log.tsv" | tail -4
    done
  done
else
  E="$S/target"; build "$E"
  for h in '^=s' '^=l' 'n=en' 'n=l' 'n=e'; do
    echo "== target $h"
    python3 tools/decode_key.py "$E" --try "$h" "${OPTS[@]}" --try-log $D/crossword_log.tsv | tail -4
  done
fi
