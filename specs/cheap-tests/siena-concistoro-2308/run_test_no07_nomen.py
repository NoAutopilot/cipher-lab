"""R10-SIENA7N (6 Oct 2026): no. 7 (363 tokens, K=45) under a homophonic + nomenclator design: each sign decodes to a
letter or to one whole word from a registered vocabulary (the nomenclator layer, Bourdeau's R4750 Latin-word nomenclator
as the design reference), with the seven C gloss values of glosses_no07.tsv held fixed (as R9-SIENA7). Pre-registered in
ciphers/siena-concistoro-2308/PREREG-R10-SIENA7N.md (pushed before the scored run). Solver:
tools/homophonic_anneal.py solve_nomen() (added for this job). Model: tools/data/it16dip minus the held-out Desjardins II
file, order 3 (not era-matched; no 15th-c. Italian corpus on disk).
Matched control: held-out Italian cut into no. 7's 20 run lengths counted in TOKENS, where each occurrence of one of the
NOMEN words is one token and every other letter one token; letters enciphered with K-len(NOMEN)=35 homophones (largest
remainder by frequency), each NOMEN word with one sign of its own; seven letter signs nearest the target's fixed counts
held fixed; then a share `err` of unfixed tokens replaced by a random other sign (J's measured error bracket).

  python3 run_test_no07_nomen.py control --err 0 0.035 0.07 --seeds 1 2 3 4 5   # control first (gate at err 0.07)
  python3 run_test_no07_nomen.py target --seeds 1 2 3                            # only if the gate passes
  python3 run_test_no07_nomen.py shuffled --seeds 1 2 3                          # ARM-C1 null
  python3 run_test_no07_nomen.py --check
"""
import argparse, gzip, hashlib, json, random, re, sys, time, unicodedata
from collections import Counter
from multiprocessing import Pool
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import homophonic_anneal as H  # noqa: E402

DATA = ROOT / "tools/data/it16dip"
MODEL_FILES = ["bub_gb_laRnTtJmsDAC.txt.gz", "bub_gb_ZJMxff7r4LUC.txt.gz", "letterediprincip01char.txt.gz",
               "letterediprincip02char.txt.gz", "letterediprincip03char.txt.gz"]
HELDOUT = "gri_33125010469852.txt.gz"
TOK = ROOT / "ciphers/siena-concistoro-2308/transcripts/no07.tok"
OUT = Path(__file__).with_name("results_no07_nomen.json")
FIX = {"q": "a", "6": "n", "+": "o", "2": "e", "x": "r", "c": "o", "QP": "e"}  # glosses_no07.tsv grade C
# solver vocabulary (what any sign may stand for besides a letter) and the control's nomenclator (a subset)
VOCAB = ["che", "et", "per", "non", "il", "la", "di", "de", "del", "della", "con", "sua", "suo", "signoria", "signore",
         "duca", "re", "papa", "milano", "siena"]
NOMEN = ["che", "per", "non", "di", "la", "il", "con", "del", "signoria", "sua"]
RESTARTS, ITERS, WORD_PROB, WORD_BONUS = 12, 60000, 0.2, 1.0
_M = None


def runs():
    return [l.split() for l in open(TOK, encoding="utf-8") if l.strip() and not l.startswith("#")]


def model():
    global _M
    if _M is None:
        _M = H.Model([gzip.open(DATA / f, "rt", encoding="utf-8").read() for f in MODEL_FILES], 3)
    return _M


def heldout_words():
    t = unicodedata.normalize("NFKD", gzip.open(DATA / HELDOUT, "rt", encoding="utf-8").read().lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return [H.fold(w) for w in re.findall(r"[a-z]+", t) if H.fold(w)]


def control_units(seed, lens):
    words = heldout_words()
    rng = random.Random(seed)
    out = []
    for n in lens:
        i, run = rng.randrange(0, len(words) - 400), []
        while len(run) < n:
            w = words[i]; i += 1
            run.extend([w] if w in NOMEN else list(w))
        out.append(run[:n])
    return [u for r in out for u in r]


def encipher(units, K, seed):
    rng = random.Random(seed + 1000)
    lc = Counter(u for u in units if len(u) == 1 and u not in NOMEN)
    letters = [a for a, _ in lc.most_common()]
    alloc = {a: 1 for a in letters}
    extra = K - len(NOMEN) - len(letters)
    while extra > 0:
        a = max(letters, key=lambda a: lc[a] / alloc[a]); alloc[a] += 1; extra -= 1
    homs, i = {}, 0
    for a in letters:
        homs[a] = [f"s{i + j}" for j in range(alloc[a])]; i += alloc[a]
    for w in NOMEN:
        homs[w] = [f"w_{w}"]
    seq = [rng.choice(homs[u]) for u in units]
    truth = {s: a for a, ss in homs.items() for s in ss}
    return seq, truth


def pick_fixed(seq, truth, target_counts):
    cnt, chosen = Counter(seq), {}
    for letter, n in target_counts:
        cands = [s for s in cnt if truth[s] == letter and s not in chosen]
        if cands:
            chosen[min(cands, key=lambda s: abs(cnt[s] - n))] = letter
    return chosen


def control_one(args):
    sd, err = args
    m = model()
    seq_t = [x for r in runs() for x in r]
    tc = Counter(seq_t)
    units = control_units(sd, [len(r) for r in runs()])
    seq, truth = encipher(units, len(tc), sd)
    fixed = pick_fixed(seq, truth, [(FIX[s], tc[s]) for s in FIX])
    if err:
        erng, signs = random.Random(500 + sd), sorted(set(seq))
        seq = [erng.choice([s for s in signs if s != x]) if x not in fixed and erng.random() < err else x for x in seq]
    sc, key = H.solve_nomen(seq, m, RESTARTS, ITERS, sd, 1.0, VOCAB, WORD_PROB, fixed, WORD_BONUS)[0]
    ok = sum(key[x] == u for x, u in zip(seq, units))
    fset = set(fixed)
    unf = [(x, u) for x, u in zip(seq, units) if x not in fset]
    wtok = [(x, u) for x, u in zip(seq, units) if u in NOMEN]
    return {"seed": sd, "err": err, "N": len(seq), "K": len(set(seq)), "fixed_signs": len(fixed),
            "fixed_tokens": len(seq) - len(unf), "nomen_tokens": len(wtok),
            "token_acc": round(ok / len(seq), 3), "token_acc_unfixed": round(sum(key[x] == u for x, u in unf) / len(unf), 3),
            "nomen_recall": round(sum(key[x] == u for x, u in wtok) / max(1, len(wtok)), 3),
            "word_signs_assigned": sorted(v for v in key.values() if len(v) > 1),
            "decoded": "".join(key[x] for x in seq)[:120], "plain": "".join(units)[:120]}


def target_one(args):
    sd, shuffle = args
    m = model()
    seq = [x for r in runs() for x in r]
    if shuffle:
        random.Random(100 + sd).shuffle(seq)
    res = H.solve_nomen(seq, m, RESTARTS, ITERS, sd, 1.0, VOCAB, WORD_PROB, dict(FIX), WORD_BONUS)
    sc, key = res[0]
    return {"seed": sd, "score": round(sc, 2), "key": key, "decoded": "".join(key[x] for x in seq),
            "word_signs": {s: v for s, v in key.items() if len(v) > 1}, "restart_scores": [round(r[0], 1) for r in res]}


def tok_sha():
    return hashlib.sha1(TOK.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", nargs="?", choices=["control", "target", "shuffled"])
    ap.add_argument("--seeds", type=int, nargs="+", default=[1, 2, 3])
    ap.add_argument("--err", type=float, nargs="+", default=[0.0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--procs", type=int, default=4)
    a = ap.parse_args()
    res = json.loads(OUT.read_text()) if OUT.exists() else {}
    if a.check:
        ok = res.get("tok_sha1") == tok_sha() and "control" in res
        print("results_no07_nomen.json", "current" if ok else "STALE or missing")
        sys.exit(0 if ok else 1)
    t0 = time.time()
    with Pool(a.procs) as pool:
        if a.mode == "control":
            rows = pool.map(control_one, [(sd, e) for e in a.err for sd in a.seeds])
            ctl = res.setdefault("control", {})
            for e in a.err:
                rr = [r for r in rows if r["err"] == e]
                ctl[str(e)] = {"rows": rr, "mean_token_acc": round(sum(r["token_acc"] for r in rr) / len(rr), 3)}
                print(e, ctl[str(e)]["mean_token_acc"], [r["token_acc"] for r in rr], [r["nomen_recall"] for r in rr])
        else:
            res[a.mode] = pool.map(target_one, [(sd, a.mode == "shuffled") for sd in a.seeds])
            for r in res[a.mode]:
                print(r["seed"], r["score"], r["word_signs"], r["decoded"][:200])
    res.update({"tok_sha1": tok_sha(), "restarts": RESTARTS, "iters": ITERS, "word_prob": WORD_PROB, "word_bonus": WORD_BONUS, "model": MODEL_FILES,
                "heldout": HELDOUT, "fix": FIX, "vocab": VOCAB, "nomen": NOMEN})
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1))
    print(f"{a.mode} done in {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
