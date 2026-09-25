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
  python3 codemark_curve.py stats                     -> per-leaf and pooled counts
  --leaves all (anywhere on the line; LANE R6 CM, 25 Sept 2026) pools all eight leaves f.54r-f.57v instead of the
  default f.54r+f.54v, so P's rows reproduce without it. f.57r line 17 pos 15-24 (a later marginal note, leafnotes/f57r.md)
  is dropped from the row pattern. Outputs carry an "_all" suffix (codemark_target_cm_all_s1.json) and a leaves field.
  cmc (LANE R6 CM2, 25 Sept 2026): the cm cipher (same key allotment and CM_NOISE) read through merged symbols, base
      code + mark class (none / dot / digit-led / other; 223 types -> about 110 symbols), so a misread mark inside a
      class cannot split a sign. Its ceiling (the majority letter per merged symbol) is about 88% on the control.
  CM_NOISE=p (LANE R6 CM) replaces a share p of control tokens by a type drawn at the target's frequencies; CM_TOL=p
  (LANE R6 CM2) solves with the error-tolerant anneal (tools/homophonic_anneal.py --noise), suffix _tol<p>.
"""
import csv, json, os, random, sys, time
from collections import Counter
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
import homophonic_anneal as ha

CORPUS = open(f"{D}/corpus_args.txt").read().split()[1::2]
VAN = os.path.join(D, "..", "..", "..", "tools/data/it16/letterescrittea01vanzgoog.txt")
RESTARTS, ITERS, PER_BOX = int(os.environ.get("CM_RESTARTS", 6)), int(os.environ.get("CM_ITERS", 120000)), 2
# CM_NOISE (cm only, LANE R6 CM): share of control tokens replaced by a type drawn at the target's own frequencies,
# a stand-in for transcription error (with-marks pass agreement runs 72-80% per leaf). Default 0 keeps P's rows.
NOISE = float(os.environ.get("CM_NOISE", 0))
# CM_TOL (cm only, LANE R6 CM2, 25 Sept 2026): error-tolerant solve, tools/homophonic_anneal.py anneal_noisy with
# noise=CM_TOL (the share of positions the solver may treat as misread, each corrected under a unigram prior). Rows and
# target files carry a _tol<p> suffix; token accuracy is of the corrected decode, info also gives the key-only accuracy.
TOL = float(os.environ.get("CM_TOL", 0))
# CM_ROBUST=q (LANE R6 CM2): bounded-loss scoring, tools/homophonic_anneal.py RobustModel; suffix _rob<q>.
ROBUST = float(os.environ.get("CM_ROBUST", 0))
VOW = "aeiou"


def mark_class(m):
    """cmc design (LANE R6 CM2): a mark string collapsed to one of four classes: none, dot, digit-led, other."""
    return "0" if m == "" else "d" if m == "dot" else "n" if m[0].isdigit() else "x"


def merge_type(t):
    code, mark = t.split("^", 1)
    return f"{code}^{mark_class(mark)}"


LEAVES_ALL = ("f54r", "f54v", "f55r", "f55v", "f56r", "f56v", "f57r", "f57v")
LEAVES = ("f54r", "f54v")
if "--leaves" in sys.argv:
    _i = sys.argv.index("--leaves"); _v = sys.argv[_i + 1]; del sys.argv[_i:_i + 2]
    LEAVES = LEAVES_ALL if _v == "all" else tuple(_v.split(","))
RSUF = ("" if RESTARTS == 6 else f"_r{RESTARTS}") + (f"_tol{TOL:g}" if TOL else "") + (f"_rob{ROBUST:g}" if ROBUST else "")
SUFFIX = "" if LEAVES == ("f54r", "f54v") else "_all" if LEAVES == LEAVES_ALL else "_" + "-".join(LEAVES)


def excluded(leaf, x):
    """Not body text: f.57r line 17 pos 15-24 is a later marginal note (leafnotes/f57r.md), all plain boxes."""
    return leaf == "f57r" and x["line"] == "17" and float(x["pos"]) >= 15


def rows(leaf=None):
    r = []
    for lf in ([leaf] if leaf else LEAVES):
        r += [dict(x, leaf=lf) for x in csv.DictReader(open(f"{D}/../ciphertext_{lf}.tsv"), delimiter="\t")
              if not excluded(lf, x)]
    return r


def stats():
    out = []
    for lf in list(LEAVES) + [None]:
        r = rows(lf); sg = [x for x in r if x["code"] != "_"]
        out.append([lf or "pooled", len(sg), len({x["code"] for x in sg}), len({(x["code"], x["marks"]) for x in sg}),
                    f"{sum(1 for x in sg if x['marks']) / max(1, len(sg)):.1%}", len(r) - len(sg)])
    print("leaf\tsign_tokens\tbase_codes\tcode_mark_types\tshare_marked\tplain_boxes")
    for o in out:
        print("\t".join(map(str, o)))


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
    if design in ("cm", "cmc"):
        units = Counter(f"{x['code']}^{x['marks']}" for x in sg).most_common()
        homs = alloc(units, Counter("".join(toks)))
        seq = []
        for t in toks:
            names, ws = zip(*homs[t])
            seq.append(rng.choices(names, ws)[0])
        if NOISE:
            un, uw = zip(*units); nrng = random.Random(seed + 9000)
            seq = [nrng.choices(un, uw)[0] if nrng.random() < NOISE else s for s in seq]
        if design == "cmc":
            seq = [merge_type(s) for s in seq]
        return seq, toks, {"K": len({s for s in seq}), "key_K": len(units), **({"noise": NOISE} if NOISE else {})}
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
    if ROBUST:
        model = ha.RobustModel(model, ROBUST)
    allowed = {s: VOW for s in stream if s.startswith("M")}
    res = ha.solve(stream, model, RESTARTS, ITERS, seed, 1.0, allowed=allowed, noise=TOL)
    sc, key = res[0][:2]
    free = res[0][2] if TOL else {}
    return sc, key, "".join(free.get(i, key[s]) for i, s in enumerate(stream)), model, free


def control(design, n, seed):
    t0 = time.time()
    seq, toks, info = build(design, n, seed)
    if design in ("cm", "cmc"):
        stream, spans = seq, [(i, i + 1) for i in range(len(seq))]
    else:
        stream, spans = expand(seq)
    truth = "".join(toks)
    sc, key, dec, model, free = run(stream, seed)
    true_sc = ha.score(model, truth, 1.0)
    let = sum(a == b for a, b in zip(dec, truth)) / len(truth)
    tok = sum(dec[a:b] == truth[a:b] for a, b in spans) / len(spans)
    if ROBUST:
        info = dict(info, robust=ROBUST)
    if TOL:  # key-only accuracy (no per-position corrections) and how many corrections the solver made
        kdec = "".join(key[s] for s in stream)
        info = dict(info, tol=TOL, free=len(free), key_only_tok=f"{sum(kdec[a:b] == truth[a:b] for a, b in spans) / len(spans):.1%}")
    row = [design, n, seed, len(stream), len({*stream}), f"{tok:.1%}", f"{let:.1%}", f"{sc:.1f}", f"{true_sc:.1f}",
           json.dumps(dict(info, leaves=SUFFIX or "f54r+f54v", **({"restarts": RESTARTS} if RESTARTS != 6 else {}))), f"{time.time() - t0:.0f}s"]
    f = f"{D}/../control_curve.tsv"
    new = not os.path.exists(f)
    with open(f, "a") as fh:
        if new:
            fh.write("design\tN_tokens\tseed\tsymbols\tsymbol_types\ttoken_acc\tletter_acc\tbest_score\ttrue_score\tinfo\ttime\n")
        fh.write("\t".join(map(str, row)) + "\n")
    print("\t".join(map(str, row)))


def target(design, seed):
    sg = [x for x in rows() if x["code"] != "_"]
    if design in ("cm", "cmc"):
        stream = [f"{x['code']}^{x['marks']}" for x in sg]
        if design == "cmc":
            stream = [merge_type(t) for t in stream]
    else:
        stream, _ = expand([(x["code"], x["marks"] or None) for x in sg])
    sc, key, dec, _, free = run(stream, seed)
    json.dump({"design": design, "seed": seed, "score": sc, "decoded": dec, "key": key, **({"robust": ROBUST} if ROBUST else {}),
               **({"tol": TOL, "free": {str(i): l for i, l in sorted(free.items())}} if TOL else {})},
              open(f"{D}/codemark_target_{design}{SUFFIX}{RSUF}_s{seed}.json", "w"), indent=0)
    print(design, seed, f"{sc:.1f}", dec[:200])


if __name__ == "__main__":
    if sys.argv[1] == "stats":
        stats()
    elif sys.argv[1] == "control":
        control(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    else:
        target(sys.argv[2], int(sys.argv[3]))
