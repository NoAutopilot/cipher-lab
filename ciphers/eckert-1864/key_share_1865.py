#!/usr/bin/env python3
"""LS3-K (b): share of non-function tokens of each mssEC 19 entry found in the code-word columns of key.md (No. 1),
key-no2.md (No. 2) and key-no9.md (No. 9); writes key-share-1865.tsv (1865 unread priority-1 rows with words >= 30, plus
every already-read E/N2/O9 entry as the labelled control) and prints the control and 1865 distributions.
Reuses entries_mssEC19.py (segmentation, tokens, vocab, FW). 1865 = pointer >= 9149 (page 257 opens Jany 2d 1865) or a
header naming 1865. Counts only; no reading. Usage: key_share_1865.py [--write]
"""
import os, re, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import entries_mssEC19 as E

BOOKS = ("1", "2", "9")

def rows():
    codes = E.load_vocab()
    ents = E.segment(E.load_pages())
    for e in ents: E.analyse(e, codes)
    kb, kv = E.known_blocks(), {"1": E.K1, "2": E.K2, "9": E.K9}
    for e in ents: e["already_read"] = ""
    for kid, (ptr, dm) in kb.items():
        for e in ents:
            if e["pointer"] == ptr and E.day_month(e["header"]) == dm and not e["already_read"]:
                e["already_read"] = kid; break
    out = []
    for e in ents:
        nf = [w for w in e["tokens"] if w not in E.FW and len(w) > 1]
        if not nf: continue
        sh = {b: sum(w in kv[b] for w in nf) / len(nf) for b in BOOKS}
        best = max(BOOKS, key=lambda b: sh[b]); srt = sorted(sh.values(), reverse=True)
        e.update(n_nf=len(nf), share=sh, best=best, margin=srt[0] - srt[1])
        out.append(e)
    return out

def pct(v, p):
    v = sorted(v); return v[min(len(v) - 1, int(round(p * (len(v) - 1))))]

def main():
    R = rows()
    ctl = [e for e in R if e["already_read"]]
    lab = {"E": "1", "N": "2", "O": "9"}
    ctl_by = {b: [e for e in ctl if lab[e["already_read"][0]] == b] for b in BOOKS}
    dist = {}
    for b in BOOKS:
        v = [e["share"][b] for e in ctl_by[b]]
        dist[b] = (len(v), statistics.median(v), pct(v, .1), pct(v, .9))
        print(f"control No.{b}: n={len(v)} median={dist[b][1]:.3f} p10={dist[b][2]:.3f} p90={dist[b][3]:.3f}  own-share of correct book")
    pr = {}
    for l in open(os.path.join(E.HERE, "entries-mssEC19.tsv"), encoding="utf-8"):
        if l.startswith("#") or l.startswith("pointer"): continue
        c = l.rstrip("\n").split("\t"); pr[(int(c[0]), int(c[2]), c[3])] = int(c[14])
    tgt = []
    for e in R:
        p = pr.get((e["pointer"], e["entry_on_page"], e["header"]))
        yr = e["pointer"] >= 9149 or "1865" in e["header"]
        if p == 1 and yr and not e["already_read"] and e["words"] >= 30: tgt.append(e)
    rowsout = []
    for e in R:
        if e in tgt: grp = "1865"
        elif e["already_read"]: grp = "control-" + e["already_read"][:1]
        else: continue
        s = e["share"]
        verdict = ""
        if grp == "1865":
            inside = dist[e["best"]][2] <= s[e["best"]] <= dist[e["best"]][3]
            verdict = f"readable with No. {e['best']}" if inside else "book not in hand (Nos. 3/4)"
        rowsout.append((e["pointer"], e["page"], e["entry_on_page"], e["already_read"] or "-", e["header"][:60], grp, e["n_nf"],
                        *(f"{s[b]:.3f}" for b in BOOKS), e["best"], f"{e['margin']:.3f}", verdict))
    t1865 = [r for r in rowsout if r[5] == "1865"]
    print("1865 rows:", len(t1865))
    for b in BOOKS:
        v = [e["share"][b] for e in tgt]
        print(f"1865 share in No.{b}: median={statistics.median(v):.3f} p10={pct(v,.1):.3f} p90={pct(v,.9):.3f}")
    import collections
    print("best book:", collections.Counter(r[10] for r in t1865))
    print("verdict:", collections.Counter(r[12] for r in t1865))
    print("verdict by best:", collections.Counter((r[10], r[12]) for r in t1865))
    # control self-check: fraction of control rows whose best book is the labelled book
    ok = sum(1 for e in ctl if e["best"] == lab[e["already_read"][0]]); print(f"control best==label: {ok}/{len(ctl)}")
    for b in BOOKS:
        c = [e for e in ctl if lab[e["already_read"][0]] == b]
        print(f"  label No.{b}: best==label {sum(e['best']==b for e in c)}/{len(c)}")
    if "--write" in sys.argv:
        with open(os.path.join(E.HERE, "key-share-1865.tsv"), "w", encoding="utf-8") as f:
            f.write("# LS3-K (8 Oct 2026): share of non-function tokens in the code-word columns of key.md (No.1), key-no2.md (No.2), key-no9.md (No.9). group 1865 = unread priority-1 rows, words>=30; control-E/N/O = already-read entries. verdict: best-book share inside that book's control p10-p90. Regenerate: python3 key_share_1865.py --write\n")
            f.write("pointer\tpage\tentry_on_page\tread_id\theader\tgroup\tn_nonfunc\tshare_no1\tshare_no2\tshare_no9\tbest_book\tmargin\tverdict\n")
            for r in rowsout: f.write("\t".join(map(str, r)) + "\n")
main()
