#!/usr/bin/env python3
"""O9-BOOK (10 Oct 2026, account 1, LANE LEDGER-N2): which book in hand (No. 1 / No. 2 / No. 9) reads ten 1864 mssEC 18 rows guessed No. 9.

Pre-registered in HYPOTHESES.md "## O9-BOOK pre-registration". Instrument A: coherent-word count = word-kind code tokens whose meaning forms, with
the read word on either side, a word bigram seen >= 2 times in the OR text on disk; controls = each book's word-kind meanings permuted (seeds 1-3
gate, 1-20 for a supplementary p95). Entries cut by the shared segmenter (fortmonroe/fm_entries.py with FM_LEDGER=ms18); decode.py reused unchanged.
  python3 o9book.py [--show]     # writes nothing; tee to o9book.out"""
import collections, glob, gzip, os, random, re, sys
os.environ["FM_LEDGER"] = "ms18"
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "fortmonroe"))
import decode, fm_entries
ROWS = [(9926,1),(9880,2),(9709,1),(9772,0),(9694,2),(9699,0),(9808,2),(9845,0),(9830,1),(9673,0)]
BOOKS = {"no1": "key.md", "no2": "key-no2.md", "no9": "key-no9.md"}
PC = os.path.join(HERE, "..", "..", "sources", "ia-fulltext", "print-check")
bi = collections.Counter()
for f in sorted(glob.glob(os.path.join(PC, "warofrebellion*_djvu.txt.gz")) + glob.glob(os.path.join(PC, "officialrecordso*_djvu.txt.gz"))):
    ws = re.findall(r"[a-z]+", gzip.open(f, "rt", errors="ignore").read().lower().replace("'", ""))
    bi.update(zip(ws, ws[1:]))
keys = {n: decode.load_key(decode.HERE / f) for n, f in BOOKS.items()}
def shuffled(key, seed):
    rows = [k for k, v in key.items() if v[2] == "word"]; ms = [key[k] for k in rows]; random.Random(seed).shuffle(ms)
    out = dict(key); out.update(zip(rows, ms)); return out
def score(words, key, show=False):
    n = 0; hits = []
    for i, w in enumerate(words):
        core = w.strip(" .,;:'\"()").replace("\\", "")
        if not core: continue
        _, _, row = decode.lookup(core, key)
        if row is None or row[2] != "word": continue
        mw = re.findall(r"[a-z]+", re.sub(r"\(.*?\)", " ", row[0].lower()))
        if not mw: continue
        p = decode._read_word(words[i-1], key, False, first=False)[0] if i > 0 else None
        q = decode._read_word(words[i+1], key, False, first=True)[0] if i + 1 < len(words) else None
        if (p and bi[(p, mw[0])] >= 2) or (q and bi[(mw[-1], q)] >= 2):
            n += 1; hits.append(f"{p}_[{row[0]}]_{q}")
    return n, hits
codes, ents = fm_entries.build()
show = "--show" in sys.argv
print("row\tdate\theader\t" + "\t".join(f"{b}\t{b}_shuf3max\t{b}_p95_20" for b in BOOKS) + "\tA_verdict")
for ptr, k in ROWS:
    e = next(x for x in ents if x["pointer"] == ptr and x["entry_on_page"] == k)
    text = decode.entry_text([e["header"]] + e["lines"]); words = text.split(" ")
    res = {}; cols = []
    for b, key in keys.items():
        s, hits = score(words, key)
        sh = [score(words, shuffled(key, sd))[0] for sd in range(1, 21)]
        res[b] = (s, max(sh[:3]), sorted(sh)[18], hits)
        cols += [str(s), str(max(sh[:3])), str(sorted(sh)[18])]
    allshuf = max(r[1] for r in res.values())
    win = [b for b in BOOKS if res[b][0] > allshuf and all(res[b][0] > res[c][0] for c in BOOKS if c != b)]
    print(f"{ptr}/{k}\t{e['date']}\t{e['header']}\t" + "\t".join(cols) + "\t" + (win[0] if win else "none"))
    if show:
        print("   TEXT:", text[:600])
        for b in BOOKS:
            r, _ = decode.decode_entry(text, keys[b]); print(f"   {b}:", r.replace("\n", " ")[:700]); print(f"      hits: {res[b][3]}")
# Part 2 (no gate, header words only): for the other 16 rows of the 26, the line above the header, the header, and the first five tokens under each book.
REST = [(9706,1),(9687,1),(9735,0),(9731,2),(9684,1),(9699,1),(9803,0),(9725,1),(9762,1),(9775,1),(9679,0),(9684,0),(9761,0),(9862,1),(9770,2),(9686,1)]
import json
if "--headers" in sys.argv:
    for ptr, k in REST:
        e = next(x for x in ents if x["pointer"] == ptr and x["entry_on_page"] == k)
        page = json.load(open(os.path.join(HERE, "sources", "mssEC18", f"p{ptr}.json")))["transc"].split("\n")
        hi = next((i for i, l in enumerate(page) if l.strip() and l.strip() == e["header"].strip()), None)
        above = page[hi - 1].strip() if hi else ""
        text = decode.entry_text([e["header"]] + e["lines"]); head = " ".join(text.split(" ")[:5])
        print(f"{ptr}/{k}\t{e['date']}\tabove={above!r}\theader={e['header']!r}\topening={head!r}")
        for b, key in keys.items():
            r, _ = decode.decode_entry(head, key); print(f"    {b}: {r.strip()}")
