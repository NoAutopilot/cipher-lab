#!/bin/bash
# h34/fetch.sh URL OUT  -- one request, browser UA, logged to requests.log, 1.6 s pause after
url="$1"; out="$2"
code=$(curl -sS -L -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36" --max-time 60 -o "$out" -w "%{http_code}" "$url" 2>/dev/null)
sz=$(stat -c %s "$out" 2>/dev/null || echo 0)
printf '%s\t%s\t%s\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$code" "$sz" "$url" >> requests.log
echo "$code $sz $url"
sleep 1.6
