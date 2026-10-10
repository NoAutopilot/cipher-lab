#!/usr/bin/env python3
"""MS18-R8 step 0 (LANE LEDGER-10 brief): does the Huntington's own page transcription (sources/mssEC18/p<pointer>.json) carry the
decoded body in clear? Same two figures as fv_ms18p_step0.py: all = LCS of decoded content words vs page transcription words / decoded
content words; code = decoded code-group meanings found in the transcription / code-group content words; control = `all` vs 20 other pages (p95).
Decoded with decode.py's No. 1 key on ms18_r8_entries.txt. Disk only."""
import json, random, re, glob, os, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); sys.path.insert(0, T)
import decode
STOP = set("""a an the and or of to in on at by for from with as is are was were be been it its that this these those you your i he him his she her we they them their our not no so if but all any some will may can shall should would have has had do did into than then there here what which who whom per one about more most very s st""".split())
def words(s): return [w for w in re.findall(r"[a-z]+", s.lower()) if w not in STOP and len(w) > 1]
def lcs(a, b):
    m = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            m[i+1][j+1] = m[i][j]+1 if a[i] == b[j] else max(m[i][j+1], m[i+1][j])
    return m[-1][-1]
key = decode.load_key(Path(T)/"key.md")
def tx(p): return words(json.load(open(os.path.join(T, "sources/mssEC18/p%d.json" % p)))["transc"])
pages = sorted(int(re.search(r"p(\d+)", f).group(1)) for f in glob.glob(os.path.join(T, "sources/mssEC18/p*.json")))
random.seed(18)
print("entry\tpointer\tall_overlap\tcode_overlap\tcontrol_all_p95\tstep0")
for header, lines in decode.load_ciphertext(Path(HERE)/"ms18_r8_entries.txt"):
    xid = header.split("|")[0].strip(); p = int(header.split("|")[2])
    r, c = decode.decode_entry(decode.entry_text(lines), key)
    b = re.sub(r"\{[^}]*\}", " ", r)
    code = " ".join(re.findall(r"\[([^\]]*)\]", b)); code = re.sub(r"\(-ed, -ing\)|= ?Er", " ", code)
    allw, codew = words(re.sub(r"[\[\]]", " ", b)), words(code); t = tx(p)
    a = lcs(allw, t) / max(1, len(allw)); cc = sum(1 for w in codew if w in set(t)) / max(1, len(codew))
    ctl = sorted(lcs(allw, tx(q)) / max(1, len(allw)) for q in random.sample([q for q in pages if q != p], 20))
    flag = "clear-copy" if (a >= 0.5 and cc >= 0.5) else "cipher transcription (not a clear copy)"
    print(f"{xid}\t{p}\t{a:.3f} ({lcs(allw,t)}/{len(allw)})\t{cc:.3f}\t{ctl[18]:.3f}\t{flag}")
