#!/bin/sh
# Re-derive the native source regions deleted by FT4q (3 Oct 2026, AX2-SHRINK pattern) from Gallica IIIF.
# One request per file, 2 s apart, descriptive UA. Usage: sh regen_images.sh [file ...]  (default: every row)
cd "$(dirname "$0")"
UA="cipher-lab research script (contact via repository)"
tail -n +2 images_manifest_full.tsv | while IFS="$(printf '\t')" read f bytes sha url cited; do
  if [ $# -gt 0 ]; then case " $* " in *" $f "*) ;; *) continue;; esac; fi
  [ -f "$f" ] && continue
  curl -sS -A "$UA" -o "$f" "$url" && echo "$(sha256sum "$f" | cut -c1-64)  $f (expected $sha)"
  sleep 2
done
