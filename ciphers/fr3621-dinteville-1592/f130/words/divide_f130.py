#!/usr/bin/env python3
"""DIN-WORDS (3 Oct 2026): word division of f.130r under the job-4 print key, polyphones read in context.
Pre-registered in f130/words/PREREG.md (committed 5cefabfe before any score).

    python3 ciphers/fr3621-dinteville-1592/f130/words/divide_f130.py [--check]

Viterbi segmentation against a fr16 word list; polyphone rows hash {c,d}, v {a,t}, m {u,t}, 0 {e,s,p,c} and U tokens
(wildcards) are resolved by the best path. Statistic D = tokens in dictionary words of length >= 3 / 527. Controls:
200 shuffled keys (rows' value+candidate sets permuted, seed 20261003) and VERIFY-DIN2's 20 wrong-text keys. Writes
result.json, control.tsv, words_tokens.tsv, reading_f130_words.txt (in ../../, the target folder's f130/), judge_input.txt.
--check exits 1 if any committed output is stale (rule 7). No key value is changed.
"""
import csv, gzip, importlib.util, json, math, random, re, sys, unicodedata
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TGT = HERE.parents[1]
ROOT = TGT.parents[1]
CT = TGT / "f130" / "ciphertext_dk.tsv"
KEY = TGT / "f130" / "print" / "key_dk_strict.tsv"
TOK = TGT / "f130" / "print" / "reading_tokens_strict.tsv"  # job-4 per-token grades
TOKG = {}
POLY = {"hash": "cd", "v": "at", "m": "ut", "0": "espc"}
ALT_PEN, WILD_PEN, JUNK, MAXW, MINC = 0.3, 1.0, 6.0, 16, 2
SEED, NSHUF = 20261003, 200
REAL_SIGNS = []
ELIDE = set("aildsnmcty")  # display only: single letters shown as words (a, i/y, elided l d s n m c t)


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.replace("j", "i").replace("v", "u").replace("y", "i")
    return re.sub(r"[^a-z]+", " ", t).split()


def lexicon():
    cnt = Counter()
    for p in sorted((ROOT / "tools/data/fr16").glob("*.txt.gz")):
        with gzip.open(p, "rt", encoding="utf-8", errors="ignore") as f:
            cnt.update(norm(f.read()))
    tot = sum(cnt.values())
    lex = {w: -math.log10(c / tot) for w, c in cnt.items() if c >= MINC and len(w) <= MAXW}
    trie = {}
    for w, c in lex.items():
        node = trie
        for ch in w:
            node = node.setdefault(ch, {})
        node["$"] = (w, c)
    return lex, trie


def load():
    key = {r["sign"]: (r["value"], r["grade"]) for r in csv.DictReader(open(KEY, encoding="utf-8"), delimiter="\t")}
    ct = list(csv.DictReader(open(CT, encoding="utf-8"), delimiter="\t"))
    for r in csv.DictReader(open(TOK, encoding="utf-8"), delimiter="\t"):
        TOKG[(r["line"], r["pos"])] = r["grade"]
    return key, ct


def cands_for(key):
    """sign -> ordered candidate string (key value first)."""
    out = {}
    for s, (v, _) in key.items():
        alt = POLY.get(s, v)
        out[s] = v + "".join(c for c in alt if c != v)
    return out


def runs(ct):
    """list of runs; each run = list of token rows (cipher only); breaks at CLEAR and '.'."""
    out, cur = [], []
    for r in ct:
        if r["sign"].startswith("CLEAR:") or r["sign"] == ".":
            if cur:
                out.append(cur)
            cur = []
        else:
            cur.append(r)
    if cur:
        out.append(cur)
    return out


def segment(run, cand, trie, letters):
    """Viterbi. cand: sign -> candidate string (None = wildcard). Returns list of (start, end, word or None, chosen)."""
    n = len(run)
    sets = [cand.get(r["sign"]) for r in run]
    best = [math.inf] * (n + 1); back = [None] * (n + 1); best[0] = 0.0
    for i in range(n):
        if best[i] == math.inf:
            continue
        c0 = sets[i]
        jc = best[i] + JUNK
        if jc < best[i + 1]:
            best[i + 1] = jc; back[i + 1] = (i, None, c0[0] if c0 else "?")
        stack = [(trie, i, 0.0, "")]
        while stack:
            node, j, pen, s = stack.pop()
            if "$" in node and j > i:
                w, wc = node["$"]
                tot = best[i] + wc + pen
                if tot < best[j]:
                    best[j] = tot; back[j] = (i, w, s)
            if j >= n or j - i >= MAXW:
                continue
            cs = sets[j]
            opts = [(ch, WILD_PEN) for ch in letters] if cs is None else [(ch, 0.0 if k == 0 else ALT_PEN) for k, ch in enumerate(cs)]
            for ch, p in opts:
                if ch in node:
                    stack.append((node[ch], j + 1, pen + p, s + ch))
    segs, j = [], n
    while j > 0:
        i, w, s = back[j]; segs.append((i, j, w, s)); j = i
    return segs[::-1]


def divide(ct, cand, trie, letters):
    rs = runs(ct); out = []; div = 0
    for run in rs:
        segs = segment(run, cand, trie, letters)
        for (i, j, w, s) in segs:
            if w and j - i >= 3:
                div += j - i
        out.append((run, segs))
    return div, out


def wrong_keys():
    spec = importlib.util.spec_from_file_location("verify_din2", TGT / "verify" / "verify_din2.py")
    V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
    A, S = V.A, V.S
    from judge_plaintext import NgramModel, read_corpus
    model = NgramModel([read_corpus(p) for p in sorted((ROOT / "tools" / "data" / "fr16").glob("*.txt.gz"))])
    ct = S.load_ct()
    P = [r["print_norm"] for r in A.PP]
    with gzip.open(ROOT / "tools/data/fr16/lettresindites00marg_djvu.txt.gz", "rt", encoding="utf-8", errors="ignore") as f:
        corpus = V.norm(f.read())
    nw = [len(t.split()) for t in P]; need = sum(nw)
    rnd = random.Random(52001); keys = []; scores = []
    for _ in range(20):
        st = rnd.randrange(len(corpus) // 10, len(corpus) - need - 1)
        seq = corpus[st:st + need]; texts, pos = [], 0
        for k in nw:
            texts.append(" ".join(seq[pos:pos + k])); pos += k
        (_, _, c2, _), nm2 = A.run(texts, "syl")
        top = V.key_from_counts(c2, nm2)
        scores.append(S.stat(model, S.runs(ct, top))[0])
        cand = {}
        for v, c in c2.items():
            s = nm2(v)
            if s == "?":
                continue
            k = len(POLY.get(s, "x"))
            ranked = [x for x, _ in sorted(Counter(c).items(), key=lambda t: (-t[1], t[0])) if x and len(x) == 1 and x.isalpha()]
            if not ranked:  # only multi-letter chunks: take the first letter of the top chunk
                ranked = [A.ia.top_of(c)[0][:1]] if A.ia.top_of(c)[0] else []
            if ranked:
                cand[s] = "".join(ranked[:k])
        for s in REAL_SIGNS:  # a sign keyed by the real key but not by this wrong text never matches a word
            cand.setdefault(s, "-")
        keys.append(cand)
    return keys, scores


def pct(xs, q):
    xs = sorted(xs); return xs[int(q * (len(xs) - 1))]


def main(check=False):
    lex, trie = lexicon()
    key, ct = load()
    cand = cands_for(key)
    REAL_SIGNS[:] = sorted(cand)
    letters = sorted({v for v, _ in key.values()})
    N = sum(1 for r in ct if not r["sign"].startswith("CLEAR:") and r["sign"] != ".")
    real_div, out = divide(ct, cand, trie, letters)
    D = real_div / N
    # control 1
    signs = sorted(cand); rnd = random.Random(SEED); sh = []
    for _ in range(NSHUF):
        l = [cand[s] for s in signs]; rnd.shuffle(l)
        sh.append(divide(ct, dict(zip(signs, l)), trie, letters)[0] / N)
    # control 2
    wk, wscores = wrong_keys()
    wmax = round(max(wscores), 4); wrep = wmax == -1.4399
    wd = [divide(ct, k, trie, letters)[0] / N for k in wk] if wrep else []
    gate = D > max(sh) and D >= pct(sh, 0.95) + 0.10 and (not wrep or D > max(wd))
    res = {"N": N, "real_D": round(D, 4), "real_divided_tokens": real_div,
           "shuffled_key": {"n": NSHUF, "seed": SEED, "mean": round(sum(sh) / len(sh), 4), "p95": round(pct(sh, 0.95), 4),
                            "max": round(max(sh), 4), "ge_real": sum(1 for x in sh if x >= D)},
           "wrong_text": {"reproduced": wrep, "ngram_max": wmax, "n": len(wd),
                          **({"mean": round(sum(wd) / len(wd), 4), "max": round(max(wd), 4),
                              "ge_real": sum(1 for x in wd if x >= D)} if wd else {})},
           "gate": "PASS" if gate else "FAIL", "lexicon_words": len(lex)}
    # outputs
    trows = [["line", "pos", "sign", "key_value", "key_grade", "chosen", "grade", "word_no", "word"]]
    lines = {}; jin = []; wno = 0; ndiv_words = 0; poly_I = 0; wild_I = 0; alt_changed = 0
    tok_line = {}
    for run, segs in out:
        for (i, j, w, s) in segs:
            if w:
                wno += 1; ndiv_words += 1
            for k in range(i, j):
                r = run[k]; sg = r["sign"]; kv, kg = key.get(sg, ("?", "U"))
                ch = s[k - i] if w else (s if s != "?" else kv)
                if sg in POLY:
                    g = "I"; poly_I += 1; alt_changed += ch != kv
                elif sg not in key:
                    g = "I" if w else "U"; wild_I += bool(w); ch = ch if w else "?"
                else:
                    g = kg = TOKG[(r["line"], r["pos"])]
                trows.append([r["line"], r["pos"], sg, kv, kg, ch, g, str(wno) if w else "", w or ""])
                if ch != "?":
                    jin.append(ch)
            seg_txt = []
            for k in range(i, j):
                row = trows[-(j - i) + (k - i)]
                c = row[5]; g = row[6]
                seg_txt.append(c + "'" if g == "I" else (c.upper() if g == "M" else c))
            txt = "".join(seg_txt)
            first_line = run[i]["line"]
            short_junk = w and j - i == 1 and w not in ELIDE  # a 1-letter "word" outside the elision set is shown as undivided
            lines.setdefault(first_line, []).append("{" + txt + "}" if (not w or short_junk) else txt)
        jin.append(" ")
    hdr = ["# Generated by f130/words/divide_f130.py (DIN-WORDS, 3 Oct 2026; PREREG f130/words/PREREG.md); do not edit.",
           "# Key: decode.json job 4 (f130/print/key_dk_strict.tsv), no value changed. lower = C, UPPER = M, x' = I (polyphone",
           "# or wildcard choice in context), {..} = letters not divided into dictionary words, ? = U. Every division is graded I.",
           f"# Divided tokens (words >= 3 letters): {real_div}/{N} = D {res['real_D']}; shuffled-key max {res['shuffled_key']['max']},"
           f" p95 {res['shuffled_key']['p95']}; gate {res['gate']}. Clear words are not shown; each line lists words starting on it.",
           "# Display only: a one-letter path 'word' outside a, i, l, d, s, n, m, c, t is shown in {..}; D is unchanged by this."]
    if not gate:
        hdr.append("# WARNING: the division does not separate from its pre-registered control; treat it as a layout aid, not a reading.")
    res["grades_out"] = dict(Counter(r[6] for r in trows[1:]))
    res["polyphone_tokens_I"] = poly_I; res["polyphone_choices_differing_from_key"] = alt_changed
    res["wildcards_placed_I"] = wild_I; res["dictionary_words"] = ndiv_words
    files = {
        HERE / "result.json": json.dumps(res, indent=1) + "\n",
        HERE / "control.tsv": "i\tshuffled_D\n" + "".join(f"{i}\t{x:.4f}\n" for i, x in enumerate(sh))
                               + "".join(f"w{i}\t{x:.4f}\n" for i, x in enumerate(wd)),
        HERE / "words_tokens.tsv": "".join("\t".join(r) + "\n" for r in trows),
        TGT / "f130" / "reading_f130_words.txt": "\n".join(hdr) + "\n" + "".join(f"{ln}\t{' '.join(ws)}\n" for ln, ws in sorted(lines.items(), key=lambda t: int(t[0][1:]))),
        HERE / "judge_input.txt": re.sub(r" +", " ", "".join(jin)).strip() + "\n",
    }
    if check:
        stale = [str(p.relative_to(TGT)) for p, t in files.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
        print("check: committed outputs match" if not stale else f"check: STALE {stale}")
        return 1 if stale else 0
    for p, t in files.items():
        p.write_text(t, encoding="utf-8")
    print(json.dumps(res, indent=1))
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "tools"))
    sys.exit(main("--check" in sys.argv))
