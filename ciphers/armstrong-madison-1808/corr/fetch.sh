#!/bin/bash
# fetch.sh URL OUT [extra curl args] -- one request, logged to corr/requests.log, browser UA, 1.6 s pause after.
# Usage from repo root: ciphers/armstrong-madison-1808/corr/fetch.sh <url> <out>
URL="$1"; OUT="$2"; shift 2
LOG="$(dirname "$0")/requests.log"
CODE=$(curl -sS -L -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36" -o "$OUT" -w "%{http_code}" --max-time 60 "$@" "$URL" 2>/dev/null)
SZ=$(stat -c %s "$OUT" 2>/dev/null || echo 0)
echo -e "$(date -u +%Y-%m-%dT%H:%M:%SZ)\t$CODE\t$SZ\t$URL" >> "$LOG"
echo "$CODE $SZ"
sleep 1.6
