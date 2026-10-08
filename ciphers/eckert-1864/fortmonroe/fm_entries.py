#!/usr/bin/env python3
"""FM-PRE stage 1 (8 Oct 2026, LANE LEDGER): entries of Huntington object 5952 (mssEC 25, Fort Monroe Ciphers Received and Sent)
with date, direction, sender/addressee, and the share of tokens in the No. 1 / No. 2 / No. 9 code columns. No decoding.

  fm_entries.py [--out entries-fm.tsv]
Reuses segment/analyse/vocab of ../entries_mssEC19.py (no private copy). Reads ../sources/fortmonroe/p<pointer>.json
(fetched with dmQuery, see ../NOTES.md "## FM-PRE"). A ranking input, not a verdict (rule 10)."""
import argparse, collections, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)
sys.path.insert(0, PARENT)
import entries_mssEC19 as m

SENT = re.compile(r"^\W*(?:ft|fort|fortress|fortr|f)\b\.?\s*(?:monroe|munroe|mon)|^\W*monroe", re.I)
YEAR = re.compile(r"(?:1864|1865|[/\-]\s*6[45]\b|\b6[45]\s*$|\s6[45]\b)")

def year_of(h):
    m_ = re.search(r"1864|1865", h)
    if m_: return int(m_.group())
    m_ = re.search(r"[/\-'\s]\s*(6[45])\s*\W*$", h)
    return 1800 + int(m_.group(1)) if m_ else None

def build():
    codes = m.load_vocab()
    raw = m.segment(m.load_pages("sources/fortmonroe"), 5545, True)
    ents = []
    for e in raw:    # a page-top run-on (no header, first on its page) continues the last entry of the previous page
        if not e["header"] and e["entry_on_page"] == 0 and ents and ents[-1]["pointer"] in (e["pointer"] - 1, e["pointer"]):
            ents[-1]["lines"] += e["lines"]; ents[-1]["cont"] = e["pointer"]
        else:
            e["cont"] = ""; ents.append(e)
    for e in ents: m.analyse(e, codes)
    ents = [e for e in ents if e["words"] >= 3 or e["header"]]
    yr = 1864; prev = 0
    for e in ents:
        h = e["header"]; dm = m.day_month(h); dm = dm if dm and dm[0] else None; y = year_of(h)
        if y: yr = y
        elif dm and dm[0] < prev - 6: yr = 1865
        if dm: prev = dm[0]
        e["dm"] = dm; e["year"] = yr
        e["date"] = f"{yr}-{dm[0]:02d}-{dm[1]:02d}" if dm else ""
        e["direction"] = "sent" if SENT.search(h) else ("received" if h else "?")
        e["sender"] = e["lines"][-1] if e["lines"] else ""
        e["addr"] = e["lines"][0] if e["lines"] else ""
        nf = max(1, sum(1 for w in e["tokens"] if w not in m.FW))
        for k in ("k1", "k2", "k9"): e["s" + k[1]] = round(sum(1 for w in e["tokens"] if w in {"k1": m.K1, "k2": m.K2, "k9": m.K9}[k] and w not in m.FW) / nf, 3)
        sh = {"1": e["s1"], "2": e["s2"], "9": e["s9"]}
        e["share_book"] = max(sh, key=sh.get)
    # book guess: the Naive Bayes of entries_mssEC19.classify trained on the already-read mssEC 19 entries (No. 1 = E, No. 2 = N2, No. 9 = O9);
    # a ranking only: the 1865 token-share band is non-selective against its control (LS3-K), and this ledger carries no 'No. N' label
    train = m.segment(m.load_pages())
    for e in train: m.analyse(e, codes); e["already_read"] = ""
    for kid, (ptr, dm) in m.known_blocks().items():
        for e in train:
            if e["pointer"] == ptr and m.day_month(e["header"]) == dm and not e["already_read"]:
                e["already_read"] = kid; break
    for e in ents: e["already_read"] = ""
    m.classify(train + ents, codes, None)
    for e in ents: e["best_book"] = e["cipher_guess"]
    return codes, ents

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--out", default=os.path.join(HERE, "entries-fm.tsv"))
    a = ap.parse_args(argv)
    codes, ents = build()
    cols = ["pointer", "page", "entry_on_page", "date", "direction", "header", "addr", "sender", "words", "codefrac", "hdr_mark", "cont", "m1", "m2", "m9", "s1", "s2", "s9", "share_book", "best_book"]
    with open(a.out, "w") as f:
        f.write("# FM-PRE (8 Oct 2026): entries of Huntington object 5952 = mssEC 25, from sources/fortmonroe (fm_entries.py); s1/s2/s9 = share of non-function tokens in the code columns of key.md / key-no2.md / key-no9.md; a ranking input, not a verdict.\n")
        f.write("\t".join(cols) + "\n")
        for e in ents: f.write("\t".join(str(e[c]).replace("\t", " ") for c in cols) + "\n")
    c = collections.Counter(e["direction"] for e in ents)
    print(len(ents), dict(c), "no-date", sum(1 for e in ents if not e["date"]), file=sys.stderr)

if __name__ == "__main__":
    main()
