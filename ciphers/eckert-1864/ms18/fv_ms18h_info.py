"""FV-MS18h (9 Oct 2026): dmGetItemInfo for the CONTENTdm hits that could be clear copies (6320 transpires+Stanley; 9780 and 8998 Urbana).
Prints title and the lines of the transcription around the hit word. Usage: python3 ms18/fv_ms18h_info.py (network; 3.3 s apart)."""
import json, re, time, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
for p, w in [(6320, 'transpires'), (9780, 'Urbana'), (8998, 'Urbana')]:
    d = json.load(urllib.request.urlopen(urllib.request.Request(HB + f"dmGetItemInfo/p16003coll11/{p}/json", headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60))
    t = d.get('transc') or ''; t = t if isinstance(t, str) else ''
    i = t.lower().find(w.lower())
    print(p, '|', (d.get('title') or '')[:100], '|', re.sub(r'\s+', ' ', t[max(0, i - 400):i + 300]) if i >= 0 else 'word not in transc', flush=True)
    time.sleep(3.3)
print('requests 3')
