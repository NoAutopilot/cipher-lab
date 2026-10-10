#!/usr/bin/env python3
"""FV-N2e: dmGetItemInfo for the five non-self hits of fv_n2e_hdl.py (title + the transcription lines carrying the query words)."""
import json, re, time, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
for p, words in [(2696, "Vicksburg|Monroe"), (10383, "Vicksburg|Monroe"), (4681, "Vicksburg|Monroe"), (10284, "Reynolds|Banks"), (10286, "Reynolds|Banks")]:
    d = json.load(urllib.request.urlopen(urllib.request.Request(HB + f"dmGetItemInfo/p16003coll11/{p}/json", headers={"User-Agent": "cipher-lab research script (contact via repository)"}), timeout=60))
    t = d.get("transc") or ""; t = t if isinstance(t, str) else ""
    i = [m.start() for m in re.finditer(words, t)]
    print(p, "|", d.get("title"), "|", " ".join(t[max(0, i[0] - 300): i[0] + 400].split()) if i else "(no match)"); time.sleep(3.3)
