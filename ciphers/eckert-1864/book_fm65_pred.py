#!/usr/bin/env python3
"""BOOK-FM65 part 2: predict the book for the 71 other 1865 Fort Monroe clean rows from header-side words only (no body reading, no gate).
Features per book on the first 12 tokens of the decode: (d) a decoded number equal to the header's day of month; (t) the first time word against a
time written in the header (header-time rows only); (p) the opening code word reads a place (Washington, Monroe, City Point, Norfolk, Fort Monroe).
Prediction: the book with the most features; ties among books -> the share's best_book of clean-fm.tsv is NOT used; 'No. 1 (month)' where no book
has a feature (all ten test rows across Jan/Feb/Mar read No. 1). Writes book_fm65_pred.tsv."""
import re, sys
sys.argv = ["x"]; exec(open(__file__.replace("book_fm65_pred.py", "book_fm65.py")).read().split('if "--show" in sys.argv:')[0])
PLACES = {"washington", "monroe", "city point", "norfolk", "fort monroe", "baltimore", "annapolis", "new york"}
def htime(h):
    m = re.search(r"(\d{1,2})(?:[.:](\d\d))?\s*([AP])\.?\s*M", h, re.I)
    if not m: return None
    return f"{int(m.group(1))}{'.'+m.group(2) if m.group(2) else ''} {m.group(3).upper()}M"
out = open("book_fm65_pred.tsv", "w"); out.write("row\tdate\tdir\theader_time\tfeat_no1\tfeat_no2\tfeat_no9\tpredicted\n")
for ptr, k in REST:
    e = ent(ptr, k); text = text_of(e); head = " ".join(text.split(" ")[:12]); day = int(e["date"][-2:]); ht = htime(e["header"])
    feats = {}
    for b, key in keys.items():
        r, _ = decode.decode_entry(head, key); f = []
        nums = [int(x) for x in re.findall(r"\[(\d+)\]", r)]
        if day in nums: f.append(f"d{day}")
        tm = re.search(r"\{time: ([^}]*)\}", r)
        if ht and tm and tm.group(1).replace(" ", "") == ht.replace(" ", ""): f.append("t=" + ht)
        cw = re.findall(r"\[([^\]]+)\]", r)
        if cw and cw[0].lower() in PLACES: f.append("p=" + cw[0])
        feats[b] = f
    best = max(len(v) for v in feats.values())
    win = [b for b in feats if len(feats[b]) == best]
    pred = ("no1 (month)" if best == 0 else win[0] if len(win) == 1 else "tie:" + "/".join(win))
    out.write(f"{ptr}/{k}\t{e['date']}\t{e['direction']}\t{ht or ''}\t" + "\t".join(",".join(feats[b]) or "-" for b in BOOKS) + f"\t{pred}\n")
