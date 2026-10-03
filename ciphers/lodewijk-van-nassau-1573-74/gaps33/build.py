"""GAPS33: build blind local windows for 5810/5811 band occurrences plus masked C null / C letter controls.

Deterministic (seed 33). Writes windows.txt (what the readers see: no codes, no classes), answers.tsv (item -> kind,
code, true value; never shown to a reader) and dropped.tsv (occurrences whose print location failed the locate rule).
Decode: key_full.tsv; codes >= 121 that are not C/H NULL show as '_' (unknown slot: a letter or nothing); C/H nulls are
dropped; multi-letter values are spelled out; clear words ('=word') are spelled out. The target slot shows as [?].
Locate rule (fixed before any reading): Smith-Waterman (match +2, mismatch -1, gap -2) of the 24 decoded letters left of
the slot (ending at the slot) and the 24 right of it (starting at it) against the print letters; accept if both scores
>= 20 and 0 <= start(R) - end(L) <= 12; the print shown is the original Groen text from 70 letters before end(L) to
70 letters after start(R), word-spaced, with no marker.
"""
import csv, os, random, sys, unicodedata, re
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, "axnames"))
import align_names as A

BAND = {"125", "139", "140", "142", "145", "146", "147", "148", "149", "150", "151"}
key = {r["code"]: r for r in csv.DictReader(open(os.path.join(T, "key_full.tsv")), delimiter="\t")}

def val(s):
    if s.startswith("="): return A.letters(s[1:])
    r = key.get(s)
    if s.isdigit() and r and r["grade"] in "CH":
        return "" if r["value"] == "NULL" else A.letters(r["value"])
    if s.isdigit() and r and r["value"] != "NULL" and r["grade"] in "IM":
        return A.letters(r["value"])
    return "_"

def sw(q, t):
    best, bj = 0, 0; bi_start = 0
    prev = [(0, 0)] * (len(t) + 1)
    for i in range(1, len(q) + 1):
        cur = [(0, 0)] * (len(t) + 1)
        for j in range(1, len(t) + 1):
            m = prev[j - 1][0] + (2 if q[i - 1] == t[j - 1] else -1)
            st = prev[j - 1][1] if prev[j - 1][0] > 0 else j - 1
            c = max((0, j), (m, st), (prev[j][0] - 2, prev[j][1]), (cur[j - 1][0] - 2, cur[j - 1][1]))
            cur[j] = c
            if c[0] > best: best, bj, bi_start = c[0], j, c[1]
        prev = cur
    return best, bi_start, bj  # score, start index in t, end index (exclusive)

def printmap(raw):
    """letters of raw with an index back into raw."""
    out, idx = [], []
    for k, ch in enumerate(raw):
        l = A.letters(ch)
        for c in l: out.append(c); idx.append(k)
    return "".join(out), idx

def main():
    items = []
    for letter in ("5810", "5811"):
        ct, spans = A.PAIRS[letter]
        raw = re.sub(r"\s+", " ", " ".join(A.groen_body(*sp) for sp in spans))
        pt, idx = printmap(raw)
        toks = A.tokens(ct)
        dec = [val(s) for (_, _, s) in toks]
        for i, (line, pos, s) in enumerate(toks):
            if not s.isdigit(): continue
            r = key.get(s)
            if s in BAND: kind = "band"
            elif r and r["grade"] == "C" and r["value"] == "NULL": kind = "cnull"
            elif r and r["grade"] == "C" and len(r["value"]) == 1: kind = "cletter"
            else: continue
            L = "".join(dec[max(0, i - 40):i]); R = "".join(dec[i + 1:i + 41])
            Lq = L.replace("_", "")[-24:]; Rq = R.replace("_", "")[:24]
            items.append(dict(letter=letter, line=line, pos=pos, code=s, kind=kind,
                              true=(r["value"] if r else "?"), i=i, toks=toks, dec=dec, pt=pt, idx=idx, raw=raw, Lq=Lq, Rq=Rq))
    rng = random.Random(33)
    band = [x for x in items if x["kind"] == "band"]
    def sample(kind, n, percode=3):
        pool = [x for x in items if x["kind"] == kind]; rng.shuffle(pool); out, cnt = [], {}
        for x in pool:
            if cnt.get(x["code"], 0) >= percode: continue
            out.append(x); cnt[x["code"]] = cnt.get(x["code"], 0) + 1
            if len(out) == n: break
        return out
    chosen = band + sample("cnull", 40) + sample("cletter", 40)
    kept, dropped = [], []
    for x in chosen:
        if len(x["Lq"]) < 12 or len(x["Rq"]) < 12: dropped.append((x, "short ctx")); continue
        sl, _, el = sw(x["Lq"], x["pt"]); sr, srt, _ = sw(x["Rq"], x["pt"])
        gap = srt - el
        if sl < 20 or sr < 20 or not (0 <= gap <= 12): dropped.append((x, f"locate sl={sl} sr={sr} gap={gap}")); continue
        a = x["idx"][max(0, el - 70)]; b = x["idx"][min(len(x["idx"]) - 1, srt + 70)]
        while a > 0 and x["raw"][a - 1] != " ": a -= 1
        while b < len(x["raw"]) and x["raw"][b] != " ": b += 1
        x["print"] = x["raw"][a:b].strip()
        i = x["i"]
        x["window"] = " ".join(d for d in x["dec"][max(0, i - 15):i] if d != "") + " [?] " + " ".join(d for d in x["dec"][i + 1:i + 16] if d != "")
        kept.append(x)
    # trim controls to 25 each after dropping, keep all band
    bykind = {"band": [], "cnull": [], "cletter": []}
    for x in kept: bykind[x["kind"]].append(x)
    final = bykind["band"] + bykind["cnull"][:25] + bykind["cletter"][:25]
    rng.shuffle(final)
    with open(os.path.join(H, "windows.txt"), "w") as w, open(os.path.join(H, "answers.tsv"), "w") as a:
        a.write("item\tletter\tline\tpos\tcode\tkind\ttrue\n")
        for n, x in enumerate(final, 1):
            w.write(f"ITEM {n}\nCIPHER DECODE: {x['window']}\nPRINT: {x['print']}\n\n")
            a.write(f"{n}\t{x['letter']}\t{x['line']}\t{x['pos']}\t{x['code']}\t{x['kind']}\t{x['true']}\n")
    with open(os.path.join(H, "dropped.tsv"), "w") as d:
        d.write("letter\tline\tpos\tcode\tkind\twhy\n")
        for x, why in dropped: d.write(f"{x['letter']}\t{x['line']}\t{x['pos']}\t{x['code']}\t{x['kind']}\t{why}\n")
    from collections import Counter
    print("kept", Counter(x["kind"] for x in final), "dropped", Counter(x["kind"] for x, _ in dropped))
    print("band kept", Counter(x["code"] for x in final if x["kind"] == "band"))

if __name__ == "__main__":
    main()
