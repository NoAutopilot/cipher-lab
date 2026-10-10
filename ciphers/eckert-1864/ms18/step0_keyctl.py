#!/usr/bin/env python3
"""STEP0-KEYCTL (10 Oct 2026, account 1, LANE LEDGER-13): does the Step-0 ruling survive a meaning-shuffled-KEY control on mssEC 18/19? Disk only.

STEP0-RULE controlled step 0 by a shuffled-ORDER null (b) and route constructions, never by shuffling the key's meanings. BOOK-FM65 found on
mssEC 25 that a meaning-shuffled No. 1 hits as often as the true book, because the holder transcription is the cipher copy (plain words + code
words) and (a) measures the plain residue. This re-runs step0_ordered.py's functions unchanged (its source up to "EXTRA = " is exec'd) on:
  set 1 'rule':   the 57 mssEC 18/19 entries STEP0-RULE scored (step0_ordered.tsv kinds sweep, fv-o9b, positive),
  set 2 's057xx': S0-57XX's nine Fort Monroe entries E302-E320,
  set 3 'r9/r10/r11': the step-0 HITs MS18-R9, -R10, -R11 recorded and did not file (No. 1; the filed misses are run too, marked).
Each entry is decoded (decode.decode_entry, as derive() does) under its book and under 3 meaning-shuffled copies of that book (book_fm65.py's
shuffled(), seeds 1-3: the 'word' rows' meanings permuted, numbers and other rows kept). Step 0 (a)/(b)/hit as step0_ordered.measure.
Key-only (a): the ordered content words of the bracketed code meanings only, LCS against the window the true book chose, / their count; the
same window is used under the shuffles (a meaning-shuffled copy changes exactly these tokens and nothing else).
Survives = (book hit AND s1, s2, s3 all miss) OR (key-only book > key-only of every shuffle).
Writes ms18/step0_keyctl.tsv; prints a summary."""
import os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); sys.path.insert(0, T)
import decode
src = open(os.path.join(HERE, "step0_ordered.py")).read(); src = src[:src.index("EXTRA = ")]
g = {"__file__": os.path.join(HERE, "step0_ordered.py")}; exec(compile(src, "step0_ordered_head", "exec"), g)
BOOKF = {"no1": "key.md", "no2": "key-no2.md", "no9": "key-no9.md"}
CTF = {"no1": "ciphertext.txt", "no2": "ciphertext-no2.txt", "no9": "ciphertext-no9.txt"}
keys = {b: decode.load_key(decode.HERE / f) for b, f in BOOKF.items()}
def shuffled(key, seed):   # = book_fm65.shuffled
    rows = [k for k, v in key.items() if v[2] == "word"]; ms = [key[k] for k in rows]; random.Random(seed).shuffle(ms)
    out = dict(key); out.update(zip(rows, ms)); return out
shuf = {b: {sd: shuffled(k, sd) for sd in (1, 2, 3)} for b, k in keys.items()}
CLEAN = lambda s: re.sub(r"\(-ed, -ing\)|= ?Er|\bM\b|\b[HCSI]\b", " ", s)   # = step0_ordered.body's clean
def prep(reading):
    body = re.sub(r"\{tail: (.*)\}\s*$", r"\1", reading.replace("\n", " ").strip())   # as book_fm65 --step0
    allw, codew = g["body"](body)
    b = re.sub(r"\{[^}]*\}", " ", body); b = re.sub(r"</?unclear>", " ", b)
    kseq = g["words"](CLEAN(" ".join(re.findall(r"\[([^\]]*)\]", b))))
    return allw, codew, kseq
def run(eid, text, book, pages, seed):
    wins = g["windows"](g["blocks"](pages)); out = {}
    for tag, key in [("book", keys[book])] + [(f"s{sd}", shuf[book][sd]) for sd in (1, 2, 3)]:
        r, _ = decode.decode_entry(text, key); allw, codew, kseq = prep(r)
        if not allw: out[tag] = None; continue
        m = g["measure"](eid, allw, codew, wins, seed); m["kseq"] = kseq; out[tag] = m
    w = dict(wins)[out["book"]["win"]]
    for tag, m in out.items():
        if m is None: continue
        m["ko"] = g["lcs"](m["kseq"], w) / len(m["kseq"]) if m["kseq"] else None
        m["kon"] = f"{g['lcs'](m['kseq'], w)}/{len(m['kseq'])}"
    return out
ct = {b: {h.split("|")[0].strip(): (h, l) for h, l in decode.load_ciphertext(decode.HERE / f)} for b, f in CTF.items()}
def book_of(eid): return next(b for b in ("no1", "no2", "no9") if eid in ct[b])
EXTRA = {"O9-DF": [9699, 9700], "9793/0": [9793, 9794]}
targets = []
for l in open(os.path.join(HERE, "step0_ordered.tsv")).read().split("\n")[1:]:
    f = l.split("\t")
    if len(f) < 9 or f[0] not in ("sweep", "fv-o9b", "positive", "s057xx"): continue
    eid = f[1]; b = book_of(eid); h, lines = ct[b][eid]
    targets.append(("rule" if f[0] != "s057xx" else "s057xx", eid, b, [int(x) for x in f[2].split("+")], decode.entry_text(lines), f[8]))
R_HITS = {"r9": "9835/1 9877/1 9793/0 9826/0 9806/2 9777/1", "r10": "9823/3 9865/1 9787/1 9733/1 9883/0 9802/1 9874/2 9779/0",
          "r11": "9743/1 9686/2 9869/4 9764/1 9897/1 9862/0 9885/3"}
for r, hits in R_HITS.items():
    for h, lines in decode.load_ciphertext(decode.Path(HERE) / f"ms18_{r}_entries.txt"):
        row = re.search(r"row (\d+/\d+)", h).group(1); p = int(h.split("|")[2])
        targets.append((r, row, "no1", EXTRA.get(row, [p]), decode.entry_text(lines), "HIT" if row in hits.split() else "filed-miss"))
rows = []
for kind, eid, b, pages, text, rec in targets:
    o = run(eid, text, b, pages, sum(map(ord, eid)))
    bk = o["book"]; sh = [o[f"s{sd}"] for sd in (1, 2, 3)]
    shit = "".join("H" if (m and m["hit"]) else "-" for m in sh)
    ko_b = bk["ko"]; ko_s = [m["ko"] if m else None for m in sh]
    ko_beat = ko_b is not None and all(x is None or ko_b > x for x in ko_s)
    surv = (bk["hit"] and shit == "---") or ko_beat
    rows.append(dict(kind=kind, eid=eid, book=b, pages="+".join(map(str, pages)), rec=rec, a=bk["a"], b=bk["b"], hit=bk["hit"],
                     sa=[m["a"] if m else None for m in sh], shit=shit, kob=ko_b, kon=bk["kon"], kos=ko_s, kobeat=ko_beat, surv=surv, win=bk["win"]))
f3 = lambda x: "-" if x is None else f"{x:.3f}"
with open(os.path.join(HERE, "step0_keyctl.tsv"), "w") as f:
    f.write("set\tentry\tbook\tpages\twindow\trecorded\ta_book\tb_p95\thit_book\ta_s1\ta_s2\ta_s3\thits_s123\tkeyonly_book\tkeyonly_lcs/n\tkeyonly_s1\tkeyonly_s2\tkeyonly_s3\tkeyonly_beats_all\tsurvives\n")
    for r in rows:
        f.write("\t".join([r["kind"], r["eid"], r["book"], r["pages"], r["win"], r["rec"], f3(r["a"]), f3(r["b"]), "HIT" if r["hit"] else "-",
                           *map(f3, r["sa"]), r["shit"], f3(r["kob"]), r["kon"], *map(f3, r["kos"]), "yes" if r["kobeat"] else "no",
                           "SURVIVES" if r["surv"] else "-"]) + "\n")
for kind in ("rule", "s057xx", "r9", "r10", "r11"):
    rs = [r for r in rows if r["kind"] == kind]; hs = [r for r in rs if r["hit"]]
    print(f"{kind}: {len(rs)} entries; book hits {len(hs)}; of those, shuffles s1/s2/s3 hit {sum(r['shit'][0]=='H' for r in hs)}/"
          f"{sum(r['shit'][1]=='H' for r in hs)}/{sum(r['shit'][2]=='H' for r in hs)}; all three shuffles miss on {sum(r['shit']=='---' for r in hs)}; "
          f"key-only beats all shuffles on {sum(r['kobeat'] for r in hs)}; survive {sum(r['surv'] for r in hs)} "
          f"({' '.join(r['eid'] for r in hs if r['surv'])})")
