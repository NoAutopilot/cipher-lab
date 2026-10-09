#!/bin/bash
# usage: fetch.sh TARGETS.tsv OUTDIR  (frame<TAB>loc<TAB>kind); URLs from images/loc694-08-09/frames.tsv; 2.1 s apart; one at a time
T=$1; O=$2; n=0
tail -n +2 "$T" | while IFS=$'\t' read fr loc kind; do
  out="$O/${loc//\//-}_$fr.jpg"; [ -s "$out" ] && continue
  url=$(awk -F'\t' -v l="$loc" -v f="$fr" '$1==l && $2==f{print $3}' images/loc694-08-09/frames.tsv)
  code=$(curl -sS -A "Mozilla/5.0" -o "$out" -w "%{http_code} %{content_type}" "$url")
  echo "$loc $fr $code $(sha256sum "$out" | cut -c1-16)"
  sleep 2.1
done
