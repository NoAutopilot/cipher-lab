"""Code+mark control curve for fr.2933 no.11 (LANE R4 P, 24 Sept 2026). Rule 3 controls for two models of the marks,
built from the pooled f.54r+f.54v transcription (719 sign tokens, 298 plain boxes, 36 base codes, 126 code+mark types).

Designs (both laid out on the target's own row pattern, tiled cyclically past 1,017 rows; every plain box withholds
2 plaintext letters from the cipher stream, as in make_interleaved.py; the cipher stream is then solved contiguous):
  cm  code+mark as distinct signs: the target's 126 code+mark types, ranked by pooled frequency, are allotted greedily
      to plaintext letters by frequency deficit; each letter picks a homophone with the target type's own frequency
      as weight. Solved with tools/homophonic_anneal.py over the code+mark signs.
  vi  mark as vowel indicator: a consonant followed by a vowel is ONE token, base code for the consonant plus a mark for
      the vowel; any other letter is a bare base code. 36 base codes allotted to the token letters by frequency, the
      10 commonest target mark types allotted to a e i o u by frequency (homophonic marks). Solved by writing each
      token as code symbol then mark symbol, which makes the letter stream exact, and annealing over 46 symbols.
N counts sign tokens. Token accuracy: a token is right when every letter it stands for is right.

  python3 codemark_curve.py control DESIGN N SEED     -> appends a row to ../control_curve.tsv
  python3 codemark_curve.py target DESIGN SEED        -> the pooled target under DESIGN, codemark_target_*.json
"""
import csv, json, os, random, sys, time
from collections import Counter
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
import homophonic_anneal as ha

CORPUS = open(f"{D}/corpus_args.txt").read().split()[1::2]
VAN = os.path.join(D, "..", "..", "..", "tools/data/it16/letterescrittea01vanzgoog.txt")
RESTARTS, ITERS, PER_BOX = int(os.environ.get("CM_RESTARTS", 6)), int(os.environ.get("CM_ITERS", 120000)), 2
VOW = "aeiou"


def rows():
    r = []
    for f in ("ciphertext_f54r.tsv", "ciphertext_f54v.tsv"):
        r += list(csv.DictReader(open(f"{D}/../{f}"), delimiter="\t"))
    return r


def pattern(n_sign):
    """The target's sign/box sequence (True = sign row), tiled until it holds n_sign signs."""
    base = [x["code"] != "_" for x in rows()]
    out, i = [], 0
    while sum(out) < n_sign:
        out.append(base[i % len(base)]); i += 1
    return out


def alloc(units, freqs):
    """Greedy: highest-frequency unit to the letter with the largest remaining deficit. units: [(name, weight)]."""
    tot_u, tot_f = sum(w for _, w in units), sum(freqs.values())
    deficit = {a: f / tot_f for a, f in freqs.items()}
    homs = {a: [] for a in freqs}
    for name, w in units:
        empty = [a for a in homs if not homs[a]]  # every letter gets one unit before any gets two
        a = max(empty, key=lambda a: freqs[a]) if empty else max(deficit, key=deficit.get)
        homs[a].append((name, w)); deficit[a] -= w / tot_u
    return homs


def plain_text():
    return ha.fold(open(VAN, encoding="utf-8").read()[200050:230000])


def build(design, n_sign, seed):
    rng = random.Random(seed + 7000)
    p = plain_text()
    pat = pattern(n_sign)
    tr = rows(); sg = [x for x in tr if x["code"] != "_"]
    toks, i = [], 0  # toks: list of (letters) for each sign row, in order
    for is_sign in pat:
        if not is_sign:
            i += PER_BOX; continue
        if design == "vi" and p[i] not in VOW and i + 1 < len(p) and p[i + 1] in VOW:
            toks.append(p[i:i + 2]); i += 2
        else:
            toks.append(p[i]); i += 1
    if design == "cm":
        units = Counter(f"{x['code']}^{x['marks']}" for x in sg).most_common()
        homs = alloc(units, Counter("".join(toks)))
        seq = []
        for t in toks:
            names, ws = zip(*homs[t])
            seq.append(rng.choices(names, ws)[0])
        return seq, toks, {"K": len({s for s in seq}), "key_K": len(units)}
    # vi: base codes over token-initial letters, marks over the vowels carried
    codes = Counter(x["code"] for x in sg).most_common()
    marks = Counter(x["marks"] for x in sg if x["marks"]).most_common(10)
    chomp = alloc(codes, Counter(t[0] for t in toks))
    mhomp = alloc(marks, Counter(t[1] for t in toks if len(t) == 2))
    seq = []
    for t in toks:
        c, w = zip(*chomp[t[0]]); code = rng.choices(c, w)[0]
        if len(t) == 2:
            m, w = zip(*mhomp[t[1]]); seq.append((code, rng.choices(m, w)[0]))
        else:
            seq.append((code, None))
    return seq, toks, {"marked": sum(1 for s in seq if s[1]) / len(seq)}


def expand(seq):
    """vi tokens -> symbol stream (code, then mark if any) and the token boundaries."""
    out, spans = [], []
    for code, mark in seq:
        a = len(out); out.append("C" + code)
        if mark:
            out.append("M" + mark)
        spans.append((a, len(out)))
    return out, spans


def run(stream, seed):
    # vi: a mark symbol stands for a vowel by hypothesis (without this the solver swaps the roles of codes and marks)
    model = ha.Model([open(c, encoding="utf-8", errors="ignore").read() for c in
                      [os.path.join(D, "..", c) if not os.path.isabs(c) else c for c in CORPUS]], order=3)
    allowed = {s: VOW for s in stream if s.startswith("M")}
    res = ha.solve(stream, model, RESTARTS, ITERS, seed, 1.0, allowed=allowed)
    sc, key = res[0]
    return sc, key, "".join(key[s] for s in stream), model


def control(design, n, seed):
    t0 = time.time()
    seq, toks, info = build(design, n, seed)
    if design == "cm":
        stream, spans = seq, [(i, i + 1) for i in range(len(seq))]
    else:
        stream, spans = expand(seq)
    truth = "".join(toks)
    sc, key, dec, model = run(stream, seed)
    true_sc = ha.score(model, truth, 1.0)
    let = sum(a == b for a, b in zip(dec, truth)) / len(truth)
    tok = sum(dec[a:b] == truth[a:b] for a, b in spans) / len(spans)
    row = [design, n, seed, len(stream), len({*stream}), f"{tok:.1%}", f"{let:.1%}", f"{sc:.1f}", f"{true_sc:.1f}",
           json.dumps(info), f"{time.time() - t0:.0f}s"]
    f = f"{D}/../control_curve.tsv"
    new = not os.path.exists(f)
    with open(f, "a") as fh:
        if new:
            fh.write("design\tN_tokens\tseed\tsymbols\tsymbol_types\ttoken_acc\tletter_acc\tbest_score\ttrue_score\tinfo\ttime\n")
        fh.write("\t".join(map(str, row)) + "\n")
    print("\t".join(map(str, row)))


def target(design, seed):
    sg = [x for x in rows() if x["code"] != "_"]
    if design == "cm":
        stream = [f"{x['code']}^{x['marks']}" for x in sg]
    else:
        stream, _ = expand([(x["code"], x["marks"] or None) for x in sg])
    sc, key, dec, _ = run(stream, seed)
    json.dump({"design": design, "seed": seed, "score": sc, "decoded": dec, "key": key},
              open(f"{D}/codemark_target_{design}_s{seed}.json", "w"), indent=0)
    print(design, seed, f"{sc:.1f}", dec[:200])


if __name__ == "__main__":
    if sys.argv[1] == "control":
        control(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    else:
        target(sys.argv[2], int(sys.argv[3]))
