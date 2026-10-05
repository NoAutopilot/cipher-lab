#!/usr/bin/env python3
"""RUN6-AVS62: Rachfahl II.1 p.209 quotation of the 13 Aug 1562 Zettel (= WVO 74) as known plaintext against
ciphertext_74.tsv under key_74.tsv. Implements avs62/prereg_avs62.md exactly. Writes avs62/result.tsv and
avs62/sign_witness.tsv; --check exits 1 if the committed files differ from a fresh run."""
import csv, difflib, random, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
CRIB = ("Wir aber in diesen Niederlanden sind noch still; zwar sind wir darum ersucht worden, haben's aber mit Glimpf "
        "abgeschlagen und möchten wohl leiden, daß unser König in Hispania desgleichen auch tue")
START, END = ("p3", 9, 22), ("p3", 13, 31)

def norm_word(w):
    w = w.lower()
    for a, b in (("ä", "a"), ("ö", "o"), ("ü", "u"), ("ß", "ss"), ("y", "i"), ("v", "u")):
        w = w.replace(a, b)
    w = re.sub(r"[^a-z]", "", w).replace("h", "").replace("dt", "t")
    w = re.sub(r"d$", "t", w).replace("ie", "i")
    return re.sub(r"(.)\1+", r"\1", w)

def norm_words(words): return "".join(norm_word(w) for w in words)

def rows(path):
    with open(path, encoding="utf-8") as f: return list(csv.DictReader(f, delimiter="\t"))

key = {r["sign"]: r["value"] for r in rows(os.path.join(T, "key_74.tsv"))}
ct = rows(os.path.join(T, "ciphertext_74.tsv"))
pairs = rows(os.path.join(T, "pairs_74.tsv"))
pos = lambda r: (r["page"], int(r["line"]), int(r["idx"]))
order = lambda p: (p[0], p[1], p[2])
span = [r for r in ct if order(START) <= order(pos(r)) <= order(END)]
pspan = [r for r in pairs if order(START) <= order(pos(r)) <= order(END)]
assert [r["sign"] for r in span] == [r["sign"] for r in pspan], "ciphertext/pairs disagree on span"

def decode(signs, k):
    # words: group by pairs word id so final-d rule applies per word
    return [k.get(s.rstrip("?"), "?") for s in signs]

def words_from(units, rowsref):
    out, cur, last = [], [], None
    for u, r in zip(units, rowsref):
        wid = (r["page"], r["line"], r["word"])
        if last is not None and wid != last: out.append("".join(cur)); cur = []
        cur.append(u); last = wid
    out.append("".join(cur)); return out

S = lambda a, b: difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
crib_words = CRIB.split(); crib = norm_words(crib_words)
signs = [r["sign"] for r in span]
dec = norm_words(words_from(decode(signs, key), pspan))
known = norm_words(words_from([r["unit"] for r in pspan], pspan))
rng = random.Random(62); vals = list(key.values()); ks = list(key.keys())
n1 = []
for _ in range(1000):
    v = vals[:]; rng.shuffle(v); kk = dict(zip(ks, v))
    n1.append(S(norm_words(words_from(decode(signs, kk), pspan)), crib))
n2 = []
for _ in range(1000):
    w = crib_words[:]; rng.shuffle(w); n2.append(S(dec, norm_words(w)))
allsig = [r["sign"] for r in ct]; L = len(signs)
i0 = ct.index(span[0]); n3 = []
for i in range(0, len(ct) - L + 1):
    if abs(i - i0) < L: continue  # windows overlapping the span are not "wrong span"
    n3.append(S(norm_words(decode(allsig[i:i + L], key)), crib))
p99 = lambda x: sorted(x)[int(0.99 * len(x)) - 1]
g1, g2, g3 = p99(n1), p99(n2), max(n3)
s_real, s_known = S(dec, crib), S(known, crib)
ok = lambda s: s > g1 and s > g2 and s > g3
out = [("item", "value"), ("span_signs", L), ("crib_norm", crib), ("decode_norm", dec), ("f19_units_norm", known),
       ("S_known_control", f"{s_known:.4f}"), ("known_control_pass", ok(s_known)),
       ("S_real", f"{s_real:.4f}"), ("N1_shuffled_key_p99", f"{g1:.4f}"), ("N1_mean", f"{sum(n1)/len(n1):.4f}"),
       ("N2_shuffled_crib_p99", f"{g2:.4f}"), ("N2_mean", f"{sum(n2)/len(n2):.4f}"),
       ("N3_wrong_span_max", f"{g3:.4f}"), ("N3_windows", len(n3)),
       ("gate", "PASS" if ok(s_known) and ok(s_real) else ("NON-TEST" if not ok(s_known) else "FAIL"))]
# per-sign witness: map each decoded sign's normalised chars into the alignment
wit = [("line", "idx", "sign", "key_74", "rachfahl_match")]
if ok(s_known) and ok(s_real):
    # conservative attribution: a sign is witnessed only when every char of its normalised word sits in a matching block
    groups, cur, last = [], [], None
    for j, r in enumerate(pspan):
        wid = (r["page"], r["line"], r["word"])
        if last is not None and wid != last: groups.append(cur); cur = []
        cur.append(j); last = wid
    groups.append(cur)
    vd = decode(signs, key); chars, owner = "", []
    for gi, grp in enumerate(groups):
        w = norm_word("".join(vd[j] for j in grp)); chars += w; owner += [gi] * len(w)
    hit = [0] * len(groups); size = [owner.count(g) for g in range(len(groups))]
    for blk in difflib.SequenceMatcher(None, chars, crib, autojunk=False).get_matching_blocks():
        for c in range(blk.a, blk.a + blk.size): hit[owner[c]] += 1
    full = {g for g in range(len(groups)) if size[g] and hit[g] == size[g]}
    wit[0] = ("line", "idx", "sign", "key_74", "word_decode", "rachfahl_word_match")
    for gi, grp in enumerate(groups):
        wdec = "".join(vd[j] for j in grp)
        for j in grp:
            r = span[j]
            wit.append((r["line"], r["idx"], r["sign"], vd[j], wdec, "yes" if gi in full else "no"))

def dump(path, data):
    s = "".join("\t".join(map(str, x)) + "\n" for x in data); p = os.path.join(HERE, path)
    if "--check" in sys.argv:
        return open(p, encoding="utf-8").read() == s
    open(p, "w", encoding="utf-8").write(s); return True
okc = dump("result.tsv", out) & dump("sign_witness.tsv", wit)
for x in out: print(*x, sep="\t")
sys.exit(0 if okc else 1)
