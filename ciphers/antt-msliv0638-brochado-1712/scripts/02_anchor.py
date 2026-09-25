import csv, json, re, unicodedata
from collections import defaultdict, Counter

data = json.load(open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/scripts/_segments.json'))

def merge_runs(segs):
    out = []
    for typ, val in segs:
        if typ=='CODE' and out and out[-1][0]=='CODE':
            out[-1] = ('CODE', out[-1][1] + val)
        else:
            out.append((typ, val if typ=='CODE' else val))
    return out

def strip_accents(s):
    return s

results = []
import re as _re
TRAIL_RE = _re.compile(r"\s*V\.(Sa|S[ªa]|mce|Ex[ªa]?)?\.?\s*$", _re.IGNORECASE)
for key, segs, decif in data:
    decif = TRAIL_RE.sub('', decif)
    merged = merge_runs(segs)
    # find anchor positions of PLAIN words in decif (case-insensitive, in order)
    # walk decif with a pointer, consuming plain words in order, greedily
    dpos = 0
    dlow = decif
    spans = []  # list of (type, content, start, end) over decif string, type CODE gets (tokens, start, end) filled after locating anchors
    plains_idx = [i for i,(t,_) in enumerate(merged) if t=='PLAIN']
    # locate each PLAIN word's position in decif starting search from dpos
    anchor_pos = {}
    ok = True
    search_from = 0
    for i,(t,v) in enumerate(merged):
        if t=='PLAIN':
            w = v.strip('.,;:')
            # find case-insensitively
            idx = decif.lower().find(w.lower(), search_from)
            if idx == -1:
                ok = False
                break
            anchor_pos[i] = (idx, idx+len(w))
            search_from = idx+len(w)
    results.append((key, merged, decif, anchor_pos, ok))

json.dump([(list(k), [(t, v) for t,v in m], d, {str(kk):vv for kk,vv in a.items()}, ok) for k,m,d,a,ok in results],
          open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/scripts/_anchors.json','w'), ensure_ascii=False, indent=1)
for key,m,d,a,ok in results:
    print(key, 'OK' if ok else 'ANCHOR-FAIL')
