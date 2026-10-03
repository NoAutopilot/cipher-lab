"""GAPS39: blind local windows for GAPS33's dropped occurrences, hand-located (gaps39/hand_locate.tsv, fixed before any
reading), plus a fresh 6 C-null + 6 C-letter control. Same window format and decode as gaps33/build.py.
Control: the hand-located dropped controls first (2 C null, 4 C letter), topped up to 6+6 with occurrences used in
neither GAPS33's kept nor its dropped set, located by GAPS33's own rule, seed 39, at most one per code.
Writes windows.txt (shuffled, seed 39) and answers.tsv (never shown to a reader)."""
import csv, os, random, re, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, "gaps33")); sys.path.insert(0, os.path.join(T, "axnames"))
import build as B, align_names as A

def printwin(x, slot):
    a = x["idx"][max(0, slot - 70)]; b = x["idx"][min(len(x["idx"]) - 1, slot + 70)]
    while a > 0 and x["raw"][a - 1] != " ": a -= 1
    while b < len(x["raw"]) and x["raw"][b] != " ": b += 1
    return x["raw"][a:b].strip()

def main():
    occ = {}
    for letter in ("5810", "5811"):
        ct, spans = A.PAIRS[letter]
        raw = re.sub(r"\s+", " ", " ".join(A.groen_body(*sp) for sp in spans))
        pt, idx = B.printmap(raw); toks = A.tokens(ct); dec = [B.val(s) for (_, _, s) in toks]
        for i, (line, pos, s) in enumerate(toks):
            r = B.key.get(s)
            kind = "band" if s in B.BAND else "cnull" if (r and r["grade"] == "C" and r["value"] == "NULL") else \
                   "cletter" if (r and r["grade"] == "C" and len(r["value"]) == 1) else None
            if not s.isdigit() or kind is None: continue
            occ[(letter, line, str(pos))] = dict(letter=letter, line=line, pos=str(pos), code=s, kind=kind,
                                                 true=(r["value"] if r else "?"), i=i, dec=dec, pt=pt, idx=idx, raw=raw)
    def win(x):
        i, d = x["i"], x["dec"]
        return " ".join(t for t in d[max(0, i - 15):i] if t != "") + " [?] " + " ".join(t for t in d[i + 1:i + 16] if t != "")
    items = []
    for r in csv.DictReader(open(os.path.join(H, "hand_locate.tsv")), delimiter="\t"):
        if r["slot"] == "-": continue
        x = occ[(r["letter"], r["line"], r["pos"])]; x["print"] = printwin(x, int(r["slot"])); x["src"] = "hand"; items.append(x)
    used = set()
    for f in ("answers.tsv", "dropped.tsv"):
        for r in csv.DictReader(open(os.path.join(T, "gaps33", f)), delimiter="\t"): used.add((r["letter"], r["line"], r["pos"]))
    rng = random.Random(39)
    for kind in ("cnull", "cletter"):
        have = [x for x in items if x["kind"] == kind]; codes = {x["code"] for x in have}
        pool = sorted((k for k, x in occ.items() if x["kind"] == kind and k not in used)); rng.shuffle(pool)
        for k in pool:
            if len(have) >= 6: break
            x = occ[k]
            if x["code"] in codes: continue
            i, d = x["i"], x["dec"]
            Lq = "".join(d[max(0, i - 40):i]).replace("_", "")[-24:]; Rq = "".join(d[i + 1:i + 41]).replace("_", "")[:24]
            if len(Lq) < 12 or len(Rq) < 12: continue
            sl, _, el = B.sw(Lq, x["pt"]); sr, srt, _ = B.sw(Rq, x["pt"])
            if sl < 20 or sr < 20 or not (0 <= srt - el <= 12): continue
            x["print"] = printwin(x, el); x["src"] = "rule"; have.append(x); items.append(x); codes.add(x["code"])
    rng.shuffle(items)
    with open(os.path.join(H, "windows.txt"), "w") as w, open(os.path.join(H, "answers.tsv"), "w") as a:
        a.write("item\tletter\tline\tpos\tcode\tkind\ttrue\tsrc\n")
        for n, x in enumerate(items, 1):
            w.write(f"ITEM {n}\nCIPHER DECODE: {win(x)}\nPRINT: {x['print']}\n\n")
            a.write(f"{n}\t{x['letter']}\t{x['line']}\t{x['pos']}\t{x['code']}\t{x['kind']}\t{x['true']}\t{x['src']}\n")
    from collections import Counter
    print("items", Counter(x["kind"] for x in items), "src", Counter((x["kind"], x["src"]) for x in items))

if __name__ == "__main__":
    main()
