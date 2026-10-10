"""FV-N1C-b (LANE LEDGER-12, 10 Oct 2026): IIIF leaf images (2400 px) of the nine entries' pointers for the eye check; scratch only, not committed.
One hdl take (ROOM.md take/release). Usage: python3 ms18/fv_n1cb_hdl.py SCRATCHDIR  (network; 3 s apart; one retry after 25 s on a drop)."""
import sys, time, urllib.request
OUT = sys.argv[1]; UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
PTR = [9678, 9757, 9758, 9724, 9771, 9804, 9727, 9764, 9798, 9832]
n = 0
for p in PTR:
    url = f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg'
    for attempt in (1, 2):
        try:
            n += 1; img = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read(); break
        except Exception as e:
            print(p, 'error', e, flush=True); img = None
            if attempt == 1: time.sleep(25)
    if img: open(f'{OUT}/leaf{p}.jpg', 'wb').write(img); print(p, len(img), flush=True)
    time.sleep(3)
print('requests', n)
