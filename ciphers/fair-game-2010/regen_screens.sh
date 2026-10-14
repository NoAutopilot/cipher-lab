#!/bin/sh
# Re-fetch Rossignol's 25 Fair Game end-credit screenshots (FAIR-CRED, 14 Oct 2026). Images stay untracked.
set -e
D="$(dirname "$0")/images/scratch"; mkdir -p "$D"
UA="cipher-lab research script (contact via repository)"
for n in 01 02; do curl -sS -A "$UA" -o "$D/BFG$n.png" "https://scienceblogs.de/klausis-krypto-kolumne/files/2017/06/BFG$n.png"; sleep 3.2; done
for n in 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25; do
  f="BFG$n.png"; [ "$n" = 04 ] && u="BFG04-1.png" || u="$f"
  curl -sS -A "$UA" -o "$D/$f" "https://klausschmeh.net/wp-content/uploads/2026/06/$u"; sleep 3.2
done
# crops: python3 ciphers/fair-game-2010/cred/make_crops.py
