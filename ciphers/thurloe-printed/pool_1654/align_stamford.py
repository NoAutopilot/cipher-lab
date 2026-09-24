#!/usr/bin/env python3
"""Align William Stamford's 1654/5 cipher letters (Birch 1742, vol. 3) with Birch's printed
"The same letter decypherd" paragraphs, and build a value -> meaning key (grade C).

The cipher paragraphs are inline: clear words, numerals 1-43 (single letters, about two homophones
each), a few higher numerals (code words: 81, 130, 158 ...), and a circled-dot sign (OCR "©" or a
lone "O") for "the lord protector". Birch prints the decipherment as one continuous modernised
paragraph after each letter, not interlined, so the pairing is done by dynamic programming over the
whole letter: each small numeral takes one plaintext letter, a code numeral or the sign one to four
whole words, a clear word the matching plaintext word; numerals may be nulls, plaintext letters
may be unmatched (Birch modernised the spelling: "mee" -> "me"). Letter costs are re-estimated
from the alignment and the pass repeated (EM-style, hard assignments).

No cryptanalysis: every meaning comes from the printed decipherment. Input is the committed
gzipped OCR (sources/ia-fulltext/thurloe-gz/collectionofstat03thur_djvu.txt.gz).

    python3 align_stamford.py            # prints a summary; decode_stamford.py writes the files
"""
import gzip
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DJVU_GZ = ROOT / "sources/ia-fulltext/thurloe-gz/collectionofstat03thur_djvu.txt.gz"
CORPORA = [ROOT / "tools/data/pg1661_holmes.txt", ROOT / "tools/data/pg2701_mobydick.txt"]

# djvu line spans (1-based, inclusive), from NOTES.md section 12.2
SPANS = {
    "P4": {"cipher": (15469, 15645)},
    "P5_P6": {"cipher": (22886, 23062), "plain": (23066, 23144)},
    "P7": {"cipher": (23233, 23347), "plain": (23351, 23422)},
}
# P4 blocks where the OCR interleaves two narrow columns and reads numerals as short words
# ("am", "in", "it", "the"): tokenized with strict=True
P4_COLUMN_BLOCKS = [(15529, 15551), (15563, 15600)]
CODE_MIN = 44          # numerals >= this are treated as code words (44-49 may also be letters)
THETA = "@"            # the circled-dot sign


def djvu_lines():
    with gzip.open(DJVU_GZ, "rt", encoding="utf-8", errors="replace") as f:
        return f.read().split("\n")


JUNK_LINE = re.compile(r"^\s*\d\s+(I\s+)?[A-Za-z]+\s*$|STATE\s+PAPERS|THURLOE\s+ESQ|^\s*\d{1,3}\s*$|^\s*[A-Z]?[a-z]{0,2}\.?\s*:?\s*$")
JUNK_SUB = [
    re.compile(r"Vol\.\s+\S+\.?(\s+\d+\s+[A-Z])?"),
    re.compile(r"\b[Pp][-.]\s*\d[\d\s',]*[-.]"),
    re.compile(r"A\.\s*D\.\s*1\s*6\s*5\s*[4±]\.?[;,]?"),
    re.compile(r"\S*[VN][VNJX]J\S*|\S*/'[VN]\S*"),
    re.compile(r"■+"),
]
SHORT_WORDS = set("a i o is in it be by me he so to of on or no do go my us we up an as at if am".split())
CONF = str.maketrans({"i": "1", "I": "1", "l": "1", "L": "1", "o": "0", "O": "0", "°": "0"})


def clean_lines(lines, a, b):
    out = []
    for ln in lines[a - 1:b]:
        if JUNK_LINE.search(ln):
            continue
        for rx in JUNK_SUB:
            ln = rx.sub(" ", ln)
        out.append(ln)
    return out


def tokenize(lines, strict=False):
    """strict (P4): in a line that is at least 30 percent numerals, a word of three letters or fewer is
    taken as an OCR misreading of a numeral (unit '?'), not as a clear word.
    -> list of units: ('N', value, raw) numeral, ('?', raw) unreadable numeral-like token,
    ('T', raw) circled-dot sign, ('W', word) clear word."""
    toks = []
    for ln in lines:
        parts = ln.split()
        nnum = sum(1 for t in parts if re.search(r"\d", t))
        dense = strict and parts and nnum >= 0.3 * len(parts)
        for t in parts:
            if dense and re.fullmatch(r"[A-Za-z]{1,3}[.,']?", t) and not re.fullmatch(r"[IilO]{1,2}[.\-]", t):
                t = "\x00" + t
            toks.append(t)
        toks.append("\n")
    units = []
    pending = ""
    for k, t in enumerate(toks):
        if t == "\n":
            continue
        # join a hyphenated word across a line break
        if pending:
            t = pending + t
            pending = ""
        nxt_nl = k + 1 < len(toks) and toks[k + 1] == "\n"
        if nxt_nl and re.fullmatch(r"[A-Za-z]{2,}-", t):
            pending = t[:-1]
            continue
        if t.startswith("\x00"):
            units.append(("?", t[1:]))
            continue
        if t in ("©", "O", "0,", "O,", "©,", "0") and not units[-1:] == [("W", "a")]:
            units.append(("T", t))
            continue
        s = t.strip("'\"`,;:()[]\\^_")
        m = re.fullmatch(r"(\d{1,3})[.\-,;:']*", s)
        if m:
            units.append(("N", int(m.group(1)), t))
            continue
        m = re.fullmatch(r"(\d{1,3})[.\-](\d{1,3})[.\-,]*", s)
        if m:
            units.append(("N", int(m.group(1)), t))
            units.append(("N", int(m.group(2)), t))
            continue
        # numeral with an OCR letter/digit confusion: repair only the unambiguous l/i/o set
        m = re.fullmatch(r"([0-9ilIoO]{1,3})[.\-]", s)
        if m and re.search(r"\d", m.group(1)) or (m and m.group(1) in ("II", "ii", "Il")):
            v = m.group(1).translate(CONF)
            units.append(("N", int(v), t))
            continue
        w = re.sub(r"[^A-Za-z]", "", t)
        if re.search(r"\d", t) or (len(s) <= 4 and re.fullmatch(r".{1,3}[.\-]", s)
                                   and len(w) <= 2 and w.lower() not in SHORT_WORDS):
            units.append(("?", t))
            continue
        if w:
            if w in ("sir", "Sir") and not units:
                continue
            units.append(("W", w.lower()))
    return units


# ---- long-s resolution for the OCR'd plaintext -------------------------------------------------
_VOCAB = None


def vocab():
    global _VOCAB
    if _VOCAB is None:
        c = Counter()
        for p in CORPORA:
            c.update(re.findall(r"[a-z]+", p.read_text(encoding="utf-8", errors="replace").lower()))
        _VOCAB = c
    return _VOCAB


def unlong_s(w):
    """Birch prints long s, which the OCR reads as f. Choose the f/s pattern the corpus knows."""
    idx = [i for i, ch in enumerate(w) if ch == "f"]
    if not idx or len(idx) > 5:
        return w
    V = vocab()
    best, bestsc = None, -1
    for mask in range(1 << len(idx)):
        cand = list(w)
        for b, i in enumerate(idx):
            if mask >> b & 1:
                cand[i] = "s"
        cand = "".join(cand)
        sc = max(V.get(cand, 0), V.get(cand[:-1], 0) * 0.5 if cand.endswith("e") else 0,
                 V.get(cand + "e", 0) * 0.3)
        if sc > bestsc:
            best, bestsc = cand, sc
    if bestsc > 0:
        return best
    # fallback: f before a consonant other than r/l/f/y is long s
    return re.sub(r"f(?=[bcdhkmnpqtw])", "s", w)


def plain_words(lines):
    ws = []
    for u in tokenize(lines):
        if u[0] == "W":
            ws.append(unlong_s(u[1]))
    # drop Birch's heading words
    while ws and ws[0] in ("the", "same", "fame", "f", "ami", "letter", "decypherd", "decypher", "d", "sir"):
        ws.pop(0)
    return ws


def norm(w):
    w = unlong_s(w.lower())
    w = w.replace("y", "i").replace("j", "i").replace("v", "u")
    w = re.sub(r"(.)\1", r"\1", w)
    return w.rstrip("e") or w


def word_cost(cw, pw):
    a, b = norm(cw), norm(pw)
    if a == b:
        return 0.0
    if len(a) >= 4 and len(b) >= 4 and (a in b or b in a or edit1(a, b)):
        return 0.6
    return None


def edit1(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) <= 1
    if len(a) > len(b):
        a, b = b, a
    return any(b[:i] + b[i + 1:] == a for i in range(len(b)))


# ---- alignment ----------------------------------------------------------------------------------
NULL_N, SKIP_P, W_DEL, W_SUB = 2.4, 1.3, 1.8, 2.6


def is_code(v):
    return v >= CODE_MIN


def letter_costs(votes):
    def cost(v, x):
        c = votes.get(v)
        if not c:
            return 1.0
        tot = sum(c.values())
        p = (c.get(x, 0) + 0.2) / (tot + 5.2)
        return min(3.0, -math.log(p) * 0.9)
    return cost


def align(units, words, votes=None, band=450):
    """Hard DP alignment of cipher units to the plaintext word list.
    Returns list of (unit_index, unit, plain_chunk or None, kind)."""
    letters, wstart, wend = [], set(), {}
    for w in words:
        s = len(letters)
        wstart.add(s)
        letters.extend(w)
        wend[s] = len(letters)
    ends_after = {}  # start -> [end of 1, 2, 3, 4 words]
    starts = sorted(wstart)
    for k, s in enumerate(starts):
        ends_after[s] = [wend[starts[k + m]] if k + m < len(starts) else None for m in range(4)]
        ends_after[s] = [e for e in ends_after[s] if e is not None]
    L, n = len(letters), len(units)
    cost = letter_costs(votes or {})
    # expected plaintext position per unit, for the band
    ln = [len(u[1]) if u[0] == "W" else (6 if u[0] in "T" or (u[0] == "N" and is_code(u[1])) else 1)
          for u in units]
    tot = sum(ln) or 1
    exp, acc = [], 0
    for x in ln:
        exp.append(acc * L / tot)
        acc += x
    exp.append(L)
    INF = float("inf")
    D = [dict() for _ in range(n + 1)]
    BP = [dict() for _ in range(n + 1)]
    D[0][0] = 0.0

    def relax(i, j, c, frm, kind):
        if c < D[i].get(j, INF):
            D[i][j] = c
            BP[i][j] = (frm, kind)

    for i in range(n + 1):
        lo, hi = max(0, int(exp[i]) - band), min(L, int(exp[i]) + band)
        row = D[i]
        for j in range(lo, hi + 1):   # plaintext-letter skips within the row, left to right
            if j in row and j + 1 <= L:
                relax(i, j + 1, row[j] + SKIP_P, (i, j), "skip")
        if i == n:
            break
        u = units[i]
        for j, c0 in list(row.items()):
            if u[0] == "N":
                v = u[1]
                relax(i + 1, j, c0 + NULL_N, (i, j), "null")
                if not is_code(v) or v < 50:
                    if j < L:
                        relax(i + 1, j + 1, c0 + cost(v, letters[j]), (i, j), "let")
                if is_code(v) and j in ends_after:
                    for m, e in enumerate(ends_after[j]):
                        relax(i + 1, e, c0 + 0.8 + 0.6 * m, (i, j), "code")
            elif u[0] in "T?":
                relax(i + 1, j, c0 + (2.0 if u[0] == "?" else 2.6), (i, j), "null")
                if u[0] == "?" and j < L:
                    relax(i + 1, j + 1, c0 + 1.1, (i, j), "let?")
                if j in ends_after:
                    for m, e in enumerate(ends_after[j]):
                        relax(i + 1, e, c0 + (0.5 if u[0] == "T" else 1.6) + 0.5 * m, (i, j), "code")
            else:  # clear word
                relax(i + 1, j, c0 + W_DEL, (i, j), "wdel")
                if j in ends_after:
                    e = ends_after[j][0]
                    wc = word_cost(u[1], "".join(letters[j:e]))
                    relax(i + 1, e, c0 + (W_SUB if wc is None else wc), (i, j),
                          "word" if wc is not None else "wsub")
                    if len(ends_after[j]) > 1:
                        relax(i + 1, ends_after[j][1], c0 + W_SUB + 1.0, (i, j), "wsub")
    # trace back
    j = L if L in D[n] else min(D[n], key=lambda jj: D[n][jj] + SKIP_P * (L - jj))
    out = []
    i = n
    while i > 0 or j > 0:
        (pi, pj), kind = BP[i][j]
        if kind != "skip":
            out.append((pi, units[pi], "".join(letters[pj:j]) if j > pj else None, kind, pj))
        i, j = pi, pj
    out.reverse()
    return out, D[n].get(L)


def collect(al):
    votes = defaultdict(Counter)
    codes = defaultdict(Counter)
    for i, u, chunk, kind, pj in al:
        if kind == "let" and u[0] == "N":
            votes[u[1]][chunk] += 1
        elif kind == "code":
            key = u[1] if u[0] == "N" else THETA if u[0] == "T" else None
            if key is not None:
                codes[key][chunk] += 1
    return votes, codes


def run_letter(name, lines, votes=None, iters=5):
    sp = SPANS[name]
    units = tokenize(clean_lines(lines, *sp["cipher"]))
    words = plain_words(clean_lines(lines, *sp["plain"]))
    return iterate([(units, words)], votes, iters)


def iterate(pairs, votes=None, iters=5):
    """pairs: list of (units, words). Shared letter votes across the pairs."""
    als = []
    for it in range(iters):
        als = [align(u, w, votes)[0] for u, w in pairs]
        nv = defaultdict(Counter)
        for al in als:
            v, _ = collect(al)
            for k, c in v.items():
                nv[k].update(c)
        votes = nv
    return als, votes


def best(c):
    (x, n), = c.most_common(1)
    return x, n, sum(c.values())


if __name__ == "__main__":
    lines = djvu_lines()
    pairs = []
    for name in ("P5_P6", "P7"):
        sp = SPANS[name]
        pairs.append((tokenize(clean_lines(lines, *sp["cipher"])), plain_words(clean_lines(lines, *sp["plain"]))))
        u = pairs[-1][0]
        print(name, "units", len(u), "N", sum(1 for x in u if x[0] == "N"), "?", sum(1 for x in u if x[0] == "?"),
              "T", sum(1 for x in u if x[0] == "T"), "W", sum(1 for x in u if x[0] == "W"), "plain words", len(pairs[-1][1]))
    als, votes = iterate(pairs)
    for v in sorted(votes):
        x, n, t = best(votes[v])
        print(v, x, n, t, dict(votes[v].most_common(4)))
    codes = defaultdict(Counter)
    for al in als:
        for k, c in collect(al)[1].items():
            codes[k].update(c)
    for k in codes:
        print("code", k, dict(codes[k]))
