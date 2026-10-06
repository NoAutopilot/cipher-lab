#!/usr/bin/env python3
"""Look for received-ledger twins of the mssEC 15 residue entries (GAPS171, 3 Oct 2026).

Usage: received_match.py RES_DIR RECV_DIR [--write | --check]
  RES_DIR:  the residue page texts print/residue_decode.py reads (<pointer>.json, field "text"; manifest
            print/residue/pages_manifest.tsv).
  RECV_DIR: vol01.json, vol02.json, vol03.json, one CONTENTdm dmQuery each (manifest print/residue/received_manifest.tsv):
            https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q=dmQuery/p16003coll11/callid^mssEC%20NN^exact^and/
            title!transc!telnum!callid/title/1024/1/0/0/0/0/0/0/json  -- every page of the received ledger with its
            volunteer transcription (field "transc", Decoding the Civil War, 2016-17, not reconciled to the image).
            mssEC 01 = object 6796 "War Department Ciphers Received Feby. 2 to July 30, 1862"; mssEC 02 = 3820 "Feby. 7
            to June 26, 1862"; mssEC 03 = 2129 "Feby. 22 to May 2, 1862". Not committed (their credit; re-fetch).
  --write rewrites print/residue/received_match.tsv; --check exits 1 if it is stale.
  --vols 04,05,...,14 (D1-ECK62L, 6 Oct 2026): match against these received ledgers instead (volNN.json, same dmQuery
            with mssEC%20NN); output goes to print/residue/received_match_<first>-<last>.tsv and control (b) takes the
            first listed ledger as the reference. Without --vols the run is the GAPS171 one, unchanged.

Method (word 5-grams, the GAPS113 or_match.py idea applied to the received side). A residue entry is decoded with the
dated key (decode.py); its 5-grams are taken from the raw sent text AND from the decoded text (meanings in place of
code words), since a received copy would carry plaintext where the sent copy carries code. A received unit is one
ledger page. 5-grams common to >= 3 pages of either side (address, signature, "by order of" boilerplate) are dropped.
Score = distinct shared 5-grams between the entry and its best received page.
  Null: the same entry with its words shuffled (seeded, 20 draws), best page score; threshold = max(3, null p99 + 1).
  Positive control (a), synthetic coded twins: 60 received entries (seeded), a 40-word window each, every word that is
  a single-word key.md meaning replaced by its code word (the sent-side form) -- recall at rank 1 above threshold.
  Positive control (b), real twins across the three received ledgers themselves (mssEC 02/03 pages against mssEC 01):
  shows the method finds a duplicate entry in two independent volunteer transcriptions.
A twin is a sorting label for a reader, not a reading claim (rule 10); a sent telegram from Washington is normally
not in Washington's received book, so few twins are expected (a negative here is conditional on the transcription).
"""
import csv, io, json, os, random, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import residue_decode as rdc  # noqa: E402

dec = rdc.dec
OUT = HERE / "residue" / "received_match.tsv"
SEED = 171
N = 5


def toks(s):
    s = re.sub(r"<[^>]*>|\{[^}]*\}", " ", s)
    return re.findall(r"[a-z]+", s.lower())


def grams(ws):
    return {tuple(ws[i:i + N]) for i in range(len(ws) - N + 1)}


VOLS = ("01", "02", "03")


def received(recv_dir):
    pages = []
    for v in VOLS:
        for r in json.load(open(os.path.join(recv_dir, f"vol{v}.json")))["records"]:
            t = r.get("transc") if isinstance(r.get("transc"), str) else ""
            if t.strip():
                pages.append({"vol": v, "ptr": int(r["pointer"]), "title": r["title"], "text": t})
    pages.sort(key=lambda p: (p["vol"], p["ptr"]))
    return pages


def sent_entries(res_dir, key):
    out, last = [], None
    skip = rdc.matched()
    for f in sorted(Path(res_dir).glob("*.json"), key=lambda x: int(x.stem)):
        ptr = int(f.stem)
        text = (json.load(open(f)).get("text") or "").strip()
        if ptr in skip or not text or ptr < 4956:
            continue
        for i, e in enumerate(rdc.entries(text), 1):
            day = dec.parse_day(re.sub(r"\bApl\b", "Apr", e.splitlines()[0])) or last
            last = day or last
            t = dec.entry_text(e.splitlines())
            r, _ = dec.decode_entry(t, key, day)
            out.append({"ptr": ptr, "entry": i, "date": day.strftime("%d %b 1862") if day else "",
                        "raw": toks(t), "dec": toks(r.replace("[", " ").replace("]", " "))})
    return out


def index(pages, sent_all):
    pg = [grams(toks(p["text"])) for p in pages]
    df = Counter(g for s in pg for g in s)
    sdf = Counter(g for s in sent_all for g in s)
    common = {g for g, c in df.items() if c >= 3} | {g for g, c in sdf.items() if c >= 3}
    return [s - common for s in pg], common


def best(gs, pg):
    sc = [(len(gs & s), j) for j, s in enumerate(pg)]
    return max(sc) if sc else (0, -1)


def run(res_dir, recv_dir):
    key = dec.load_key()
    pages = received(recv_dir)
    sent = sent_entries(res_dir, key)
    all15 = []  # every residue page in RES_DIR, for the sent-side boilerplate filter
    for f in Path(res_dir).glob("*.json"):
        all15.append(grams(toks(json.load(open(f)).get("text") or "")))
    pg, common = index(pages, all15)
    rng = random.Random(SEED)
    rows, null = [], []
    for s in sent:
        gs = (grams(s["raw"]) | grams(s["dec"])) - common
        sc, j = best(gs, pg)
        for _ in range(20):
            w = s["dec"][:]
            rng.shuffle(w)
            null.append(best(grams(w) - common, pg)[0])
        rows.append((s, sc, j))
    null.sort()
    p99 = null[int(0.99 * (len(null) - 1))]
    thr = max(3, p99 + 1)
    # positive control (a): synthetic coded twins
    inv = {}
    for code, vals in key.items():
        for meaning, grade, *_ in vals:
            m = meaning.lower()
            if re.fullmatch(r"[a-z]+", m) and "time" not in m:
                inv.setdefault(m, code)
    cands = [k for k, p in enumerate(pages) if len(toks(p["text"])) >= 45]
    rng2 = random.Random(SEED + 1)
    pick = rng2.sample(cands, min(60, len(cands)))
    hit_a = 0; subs = 0
    for k in pick:
        w = toks(pages[k]["text"])
        st = rng2.randrange(0, len(w) - 40 + 1)
        win = w[st:st + 40]
        enc = [inv.get(x, x) for x in win]
        subs += sum(1 for a, b in zip(win, enc) if a != b)
        sc, j = best(grams(enc) - common, pg)
        hit_a += (j == k and sc >= thr)
    # positive control (b): real cross-ledger twins (mssEC 02/03 pages against mssEC 01 pages)
    v1 = [k for k, p in enumerate(pages) if p["vol"] == VOLS[0]]
    oth = [k for k, p in enumerate(pages) if p["vol"] != VOLS[0]]
    hit_b = sum(1 for k in oth if max((len(pg[k] & pg[j]) for j in v1), default=0) >= thr)
    summ = {"sent_entries": len(sent), "received_pages": len(pages), "null_draws": len(null), "null_p99": p99,
            "threshold": thr, "ctl_a_recall": f"{hit_a}/{len(pick)}", "ctl_a_code_subs_per_window": round(subs / len(pick), 2),
            ("ctl_b_02_03_pages_with_01_twin" if VOLS == ("01", "02", "03") else
             f"ctl_b_other_pages_with_{VOLS[0]}_twin"): f"{hit_b}/{len(oth)}",
            "twins": sum(1 for _, sc, _ in rows if sc >= thr)}
    return rows, pages, summ


def render(rows, pages, summ):
    buf = io.StringIO()
    buf.write("# " + json.dumps(summ) + "\n")
    w = csv.writer(buf, delimiter="\t", lineterminator="\n")
    w.writerow(["sent_ptr", "entry", "date", "best_score", "twin", "recv_vol", "recv_ptr", "recv_page"])
    for s, sc, j in rows:
        p = pages[j] if j >= 0 else {"vol": "", "ptr": "", "title": ""}
        w.writerow([s["ptr"], s["entry"], s["date"], sc, "twin" if sc >= summ["threshold"] else "",
                    "mssEC " + p["vol"] if sc else "", p["ptr"] if sc else "", p["title"] if sc else ""])
    return buf.getvalue()


def main(argv):
    global VOLS, OUT
    if len(argv) < 3 or argv[1] in ("-h", "--help"):
        print(__doc__); return 0
    if "--vols" in argv:
        VOLS = tuple(argv[argv.index("--vols") + 1].split(","))
        OUT = HERE / "residue" / f"received_match_{VOLS[0]}-{VOLS[-1]}.tsv"
    rows, pages, summ = run(argv[1], argv[2])
    out = render(rows, pages, summ)
    print(json.dumps(summ, indent=1))
    if "--write" in argv:
        OUT.write_text(out); return 0
    if "--check" in argv:
        if not OUT.exists() or OUT.read_text() != out:
            print("received_match.tsv is stale"); return 1
        print("received_match.tsv is current")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
