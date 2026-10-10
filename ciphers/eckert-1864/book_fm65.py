#!/usr/bin/env python3
"""BOOK-FM65 (10 Oct 2026, account 1, LANE LEDGER-13): does any book in hand (No. 1 / No. 2 / No. 9) read the 1865 clean rows of the Fort Monroe
ledger (mssEC 25, fortmonroe/clean-fm.tsv)? book65.py (BOOK-65) pointed at the Fort Monroe pages (fm_entries default ledger). Pre-registered in
HYPOTHESES.md "## BOOK-FM65 pre-registration". Disk only.
  python3 book_fm65.py --show --shufshow      # part 1: the ten test rows, A counts + decodes under each book and 3 shuffled copies
  python3 book_fm65.py --headers              # part 2: the other 71 rows, line above / header / first tokens under each book
  python3 book_fm65.py --step0 PRED.tsv [--shuf N]   # part 3: step0_ordered (a)/(b) under the predicted book (PRED.tsv: row<TAB>book);
                                                     # --shuf N runs the same rows under the book's meaning-shuffled copy, seed N"""
import collections, glob, gzip, json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "fortmonroe"))
import decode, fm_entries
ROWS = [(5854,1),(5856,0),(5878,1),(5886,0),(5897,0),(5904,1),(5905,0),(5918,0),(5924,0),(5936,0)]
BOOKS = {"no1": "key.md", "no2": "key-no2.md", "no9": "key-no9.md"}
CLEAN = [l.split("\t") for l in open(os.path.join(HERE, "fortmonroe", "clean-fm.tsv")).read().split("\n")[2:] if "\t1865-" in l]
ALL65 = [(int(r[1]), int(r[3])) for r in CLEAN]
REST = [x for x in ALL65 if x not in ROWS]
keys = {n: decode.load_key(decode.HERE / f) for n, f in BOOKS.items()}
codes, ents = fm_entries.build()
def ent(ptr, k): return next(x for x in ents if x["pointer"] == ptr and x["entry_on_page"] == k)
def page(ptr): return json.load(open(os.path.join(HERE, "sources", "fortmonroe", f"p{ptr}.json")))["transc"].split("\n")
def above(e):
    pg = page(e["pointer"]); hi = next((i for i, l in enumerate(pg) if l.strip() and l.strip() == e["header"].strip()), None)
    return pg[hi - 1].strip() if hi else ""
def shuffled(key, seed):
    rows = [k for k, v in key.items() if v[2] == "word"]; ms = [key[k] for k in rows]; random.Random(seed).shuffle(ms)
    out = dict(key); out.update(zip(rows, ms)); return out
def text_of(e): return decode.entry_text([e["header"]] + e["lines"])
if "--show" in sys.argv:
    PC = os.path.join(HERE, "..", "..", "sources", "ia-fulltext", "print-check"); bi = collections.Counter()
    for f in sorted(glob.glob(os.path.join(PC, "warofrebellion*_djvu.txt.gz")) + glob.glob(os.path.join(PC, "officialrecordso*_djvu.txt.gz"))):
        ws = re.findall(r"[a-z]+", gzip.open(f, "rt", errors="ignore").read().lower().replace("'", "")); bi.update(zip(ws, ws[1:]))
    def score(words, key):
        n = 0
        for i, w in enumerate(words):
            core = w.strip(" .,;:'\"()").replace("\\", "")
            if not core: continue
            _, _, row = decode.lookup(core, key)
            if row is None or row[2] != "word": continue
            mw = re.findall(r"[a-z]+", re.sub(r"\(.*?\)", " ", row[0].lower()))
            if not mw: continue
            p = decode._read_word(words[i-1], key, False, first=False)[0] if i > 0 else None
            q = decode._read_word(words[i+1], key, False, first=True)[0] if i + 1 < len(words) else None
            if (p and bi[(p, mw[0])] >= 2) or (q and bi[(mw[-1], q)] >= 2): n += 1
        return n
    print("row\tdate\tdir\theader\t" + "\t".join(f"{b}\t{b}_shuf3max\t{b}_p95_20" for b in BOOKS))
    for ptr, k in ROWS:
        e = ent(ptr, k); text = text_of(e); words = text.split(" "); cols = []
        for b, key in keys.items():
            sh = sorted(score(words, shuffled(key, sd)) for sd in range(1, 21)); s3 = max(score(words, shuffled(key, sd)) for sd in (1, 2, 3))
            cols += [str(score(words, key)), str(s3), str(sh[18])]
        print(f"{ptr}/{k}\t{e['date']}\t{e['direction']}\t{e['header']}\t" + "\t".join(cols))
        print("   ABOVE:", repr(above(e))); print("   TEXT:", text[:1100])
        for b in BOOKS:
            r, _ = decode.decode_entry(text, keys[b]); print(f"   {b}:", r.replace("\n", " ")[:1100])
            if "--shufshow" in sys.argv:
                for sd in (1, 2, 3):
                    r, _ = decode.decode_entry(text, shuffled(keys[b], sd)); print(f"   {b}~s{sd}:", r.replace("\n", " ")[:600])
if "--headers" in sys.argv:
    for ptr, k in REST:
        e = ent(ptr, k); text = text_of(e); head = " ".join(text.split(" ")[:8])
        print(f"{ptr}/{k}\t{e['date']}\t{e['direction']}\tabove={above(e)!r}\theader={e['header']!r}\topening={head!r}")
        for b, key in keys.items():
            r, _ = decode.decode_entry(head, key); print(f"    {b}: {r.strip()}")
if "--step0" in sys.argv:
    # step0_ordered.py's functions (words, lcs, blocks, windows, measure) -- imported by exec of its def section only, so its main sweep is not re-run
    src = open(os.path.join(HERE, "ms18", "step0_ordered.py")).read(); ns = {"__file__": os.path.join(HERE, "ms18", "step0_ordered.py")}
    exec(src.split("ents = {}")[0], ns); exec("def _p(): pass\n" + src[src.index("def body("):src.index("EXTRA = {")], ns)
    pred = [l.split("\t")[:2] for l in open(sys.argv[sys.argv.index("--step0") + 1]).read().split("\n") if "\t" in l and not l.startswith("#")]
    print("row\tbook\twindow\ta_ordered\tlcs/n\tb_shuffle_p95\thit\tc_count")
    for row, b in pred:
        if b not in keys: continue
        ptr, k = map(int, row.split("/")); e = ent(ptr, k)
        sd = int(sys.argv[sys.argv.index("--shuf") + 1]) if "--shuf" in sys.argv else 0   # --shuf N: the same under a meaning-shuffled copy (rule 3 check)
        r, _ = decode.decode_entry(text_of(e), shuffled(keys[b], sd) if sd else keys[b])
        body = re.sub(r"\{tail: (.*)\}\s*$", r"\1", r.replace("\n", " ").strip())   # the signature tail is decoded text; time/date words dropped
        allw, codew = ns["body"](body)
        if not allw: print(f"{row}\t{b}\t-\tno words"); continue
        m = ns["measure"](row, allw, codew, ns["windows"](ns["blocks"]([ptr])), sum(map(ord, row)))
        print(f"{row}\t{b}\t{m['win']}\t{m['a']:.3f}\t{m['lcs']}/{m['n']}\t{m['b']:.3f}\t{'HIT' if m['hit'] else '-'}\t{m['c']}")
