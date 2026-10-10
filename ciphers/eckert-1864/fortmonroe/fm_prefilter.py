#!/usr/bin/env python3
"""FM-PRE stage 2 (8 Oct 2026, LANE LEDGER): offline pre-filter of the Fort Monroe ledger entries (object 5952 = mssEC 25). No decoding.

  fm_prefilter.py --scratch DIR [--out prefilter-fm.tsv]        DIR/or/<ia id>.txt = IA _djvu.txt of the print volumes (not committed)
Checks (the PF4 three, reusing ../prefilter_ls4.py and ../entries_mssEC19.py):
 (a) PRINT, widened: rare-3-gram window cover of the entry's plain tokens over OR ser. I 33, 36, 40, 42, 43, 44, 45, 46, 51, ORN I/9-11 (I/12: IA download 500 twice, not scanned), OR II/6-8,
     OR III/4-5 and Butler's Private and Official Correspondence vols 3-5 (VOLS below); print-likely = cover >= 7.
 (b) OWN transcription clear (code fraction < 0.12).
 (c) SAME LEAF/NEIGHBOUR and OTHER LEDGER: entries of this ledger within +-1 page, and entries of mssEC 19 (sent) and mssEC 18 within +-3
     days, with >= 0.5 of the entry's 3-grams in the other entry (a cipher copy) or >= 3 shared rare plain tokens on the same date.
     A match to an entry already read is tagged read:<id>; a match to a clear entry is tagged clear.
The network checks (be-api phrase, Huntington full text) are run by fm_net.py on the rows left clean. A ranking, not a verdict (rule 10)."""
import argparse, collections, csv, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); PARENT = os.path.dirname(HERE)
sys.path.insert(0, PARENT); sys.path.insert(0, HERE)
import entries_mssEC19 as m, prefilter_ls4 as pl, fm_entries as fe

ROOT = os.path.abspath(os.path.join(PARENT, "..", ".."))
VOLS = {"warofrebellion33unit": "OR I/33", "warofrebellion361unit": "OR I/36-1", "warofrebellion362unit": "OR I/36-2", "warofrebellion363unit": "OR I/36-3",
        "warofrebellion401unit": "OR I/40-1", "warofrebellion402unit": "OR I/40-2", "warofrebellion403unit": "OR I/40-3",
        "warofrebellion421unit": "OR I/42-1", "warofrebellion422unit": "OR I/42-2", "warofrebellion423unit": "OR I/42-3",
        "warofrebellion431unit": "OR I/47-2",  # OR-CACHE 10 Oct 2026: IA 431unit is I/47 pt 2 (title page), not 43-1; committed prefilter-fm*.tsv rows labelled "OR I/43-1" are I/47-2 text
        "warofrebellion431unit_0": "OR I/43-1", "warofrebellion432unit": "OR I/43-2", "warofrebellion44unit": "OR I/44",
        "warofrebellion451unit": "OR I/45-1", "warofrebellion452unit": "OR I/45-2",
        "warofrebellion461unit": "OR I/46-1", "warofrebellion462unit": "OR I/46-2", "warofrebellion463unit": "OR I/46-3",
        "warofrebellion511unit": "OR I/51-1", "warofrebellion512unit": "OR I/51-2",
        "officialrecordso0009unse": "ORN I/9", "officialrecordso0010unse": "ORN I/10", "officialrecordso0011unse": "ORN I/11", "officialrecordso0012unse": "ORN I/12",
        "warofrebellion0206rootrich": "OR II/6", "warofrebellion0207rootrich": "OR II/7", "warofrebellion0208rootrich": "OR II/8",
        "cu31924079575373": "OR III/4", "cu31924079575381": "OR III/5",
        "privateoffice03butlrich": "Butler Corr. 3", "privateoffice04butlrich": "Butler Corr. 4", "privateoffice05butlrich": "Butler Corr. 5"}

def dnum(dm): return dm[0] * 31 + dm[1] if dm and dm[0] else None
def okdm(dm): return dm if dm and dm[0] else None

def other_ledgers():
    """mssEC 19 (with the read ids of entries-mssEC19.tsv) and mssEC 18 entries, analysed, with (month, day) in dm."""
    codes = m.load_vocab(); out = []
    if fe.S == "ms18": return codes, _other_ms18(codes)
    tsv = {}
    for l in open(os.path.join(PARENT, "entries-mssEC19.tsv"), encoding="utf-8"):
        if l.startswith("#") or l.startswith("pointer\t"): continue
        c = l.rstrip("\n").split("\t"); tsv[(int(c[0]), int(c[2]))] = c
    for vol, pages in (("mssEC19", m.load_pages()), ("mssEC18", pl.pages_mssEC18(None))):
        for e in m.segment(pages):
            m.analyse(e, codes); e["vol"] = vol
            e["dm"] = okdm(m.day_month(e["header"])); e["already_read"] = ""
            if vol == "mssEC19" and (e["pointer"], e["entry_on_page"]) in tsv: e["already_read"] = tsv[(e["pointer"], e["entry_on_page"])][13]
            if e["words"] >= 8: out.append(e)
    return codes, out

def _other_ms18(codes):
    """MS18-PRE: for the sent ledger mssEC 18 the other ledgers are mssEC 19 (with its read ids) and Fort Monroe (object 5952, mssEC 25)."""
    out = []; tsv = {}
    for l in open(os.path.join(PARENT, "entries-mssEC19.tsv"), encoding="utf-8"):
        if l.startswith("#") or l.startswith("pointer\t"): continue
        c = l.rstrip("\n").split("\t"); tsv[(int(c[0]), int(c[2]))] = c
    for vol, pages in (("mssEC19", m.load_pages()), ("mssEC25", m.load_pages("sources/fortmonroe"))):
        for e in m.segment(pages):
            m.analyse(e, codes); e["vol"] = vol
            e["dm"] = okdm(m.day_month(e["header"])); e["already_read"] = ""
            if vol == "mssEC19" and (e["pointer"], e["entry_on_page"]) in tsv: e["already_read"] = tsv[(e["pointer"], e["entry_on_page"])][13]
            if e["words"] >= 8: out.append(e)
    return out

def grams3(tokens):
    return {tuple(tokens[i:i + 3]) for i in range(len(tokens) - 2)}

def dups(e, fm, oth, codes, wc):
    mine = grams3(e["tokens"]); rare = pl.rare_plain(e, codes, wc); tags = []
    if len(mine) < 8: return tags
    for o in fm + oth:
        if o is e: continue
        if o["vol"] == fe.SAME:
            if abs(o["page"] - e["page"]) > 1 or o["page"] == 0: continue
            if e["dm"] and o["dm"] and abs(dnum(e["dm"]) - dnum(o["dm"])) > 3: continue
        else:
            if not (e["dm"] and o["dm"]) or abs(dnum(e["dm"]) - dnum(o["dm"])) > 3: continue
        og = grams3(o["tokens"]); full = len(mine & og) / len(mine)
        sh = len(rare & pl.rare_plain(o, codes, wc)) if (e["dm"] and o["dm"] and e["dm"] == o["dm"]) else 0
        why = []
        if full >= 0.5 and len(og) >= 8: why.append(f"copy{full:.2f}")
        if sh >= 3: why.append(f"{sh}tok")
        if why:
            st = [("read:" + o["already_read"]) if o.get("already_read") else "", "clear" if o["codefrac"] < 0.12 else ""]
            tag = f"{o['vol']}:{o['pointer']}/{o['entry_on_page']}"
            tags.append(f"{tag}[{','.join(why)}{';' + ','.join(s for s in st if s) if any(st) else ''}]")
    return tags

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scratch", required=True); ap.add_argument("--out", default=os.path.join(fe.OUTDIR, "prefilter-%s.tsv" % fe.S))
    a = ap.parse_args(argv)
    avail = {k: v for k, v in VOLS.items() if os.path.exists(os.path.join(a.scratch, "or", k + ".txt"))}
    pl.NEWVOLS = avail
    pl.CACHE = os.path.join(ROOT, "sources", "ia-fulltext", "print-check", fe.CFG["cache"]); os.makedirs(pl.CACHE, exist_ok=True)
    codes, fm = fe.build()
    for e in fm: e["vol"] = fe.SAME; e["already_read"] = ""
    _, oth = other_ledgers()
    ents = fm
    freq, cov, wc = pl.scan_new(ents, codes, a.scratch, os.path.join(pl.CACHE, "scan_%s.json" % fe.S))
    rows = []
    for ei, e in enumerate(fm):
        r = {"pointer": e["pointer"], "page": e["page"], "entry": e["entry_on_page"], "date": e["date"], "direction": e["direction"],
             "words": e["words"], "best_book": e["best_book"], "hdr_mark": e["hdr_mark"], "s1": e["s1"], "s2": e["s2"], "s9": e["s9"],
             "or_cov": cov[ei][0], "or_vol": avail.get(cov[ei][1], ""), "own": "clear" if e["codefrac"] < 0.12 else "cipher"}
        r["dups"] = " ".join(dups(e, fm, oth, codes, wc)) or "none"
        v = []
        if r["or_cov"] >= m.MINCOV: v.append("print-likely")
        if r["own"] == "clear" or "clear]" in r["dups"] or ",clear" in r["dups"]: v.append("clear-sibling")
        # strong = >= 0.5 of the entry's 3-grams are in the other entry (a cipher copy); a bare ">= 3 shared rare tokens on the same date" is
        # recorded in `dups` as a near-neighbour (same-day traffic on one subject) and does not exclude the row
        if re.search(r"mssEC19:[^ ]*\[[^\]]*copy", r["dups"]): v.append("mssEC19-dup")
        if re.search(r"mssEC18:[^ ]*\[[^\]]*copy", r["dups"]): v.append("mssEC18-dup")
        if re.search(r"mssEC25:[^ ]*\[[^\]]*copy", r["dups"]) and fe.S == "ms18": v.append("mssEC25-dup")
        if re.search(fe.SAME + r":[^ ]*\[[^\]]*copy", r["dups"]): v.append("dup")
        if e["words"] < 8: v.append("short")
        r["verdict"] = "+".join(v) if v else "clean"
        rows.append(r)
    cols = ["pointer", "page", "entry", "date", "direction", "words", "best_book", "hdr_mark", "s1", "s2", "s9", "or_cov", "or_vol", "own", "dups", "verdict"]
    with open(a.out, "w") as f:
        f.write("# " + fe.LAB + " (8 Oct 2026): offline pre-filter of Huntington " + fe.OBJ + ", fm_prefilter.py; a ranking, not a verdict (rule 10). Volumes scanned: %s\n" % ", ".join(sorted(avail.values())))
        f.write("\t".join(cols) + "\n")
        for r in rows: f.write("\t".join(str(r[c]).replace("\t", " ") for c in cols) + "\n")
    print(collections.Counter(r["verdict"] for r in rows).most_common(14), file=sys.stderr)

if __name__ == "__main__":
    main()
