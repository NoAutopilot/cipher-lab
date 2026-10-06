"""R9-SIENA7 (6 Oct 2026): anchored homophonic fit of no. 7 (363 tokens, K=45) with the seven C gloss values of
glosses_no07.tsv held fixed. Pre-registered in ciphers/siena-concistoro-2308/PREREG-R9-SIENA7.md (pushed before the
scored run). Solver: tools/homophonic_anneal.py (anneal/solve, unchanged). Model: tools/data/it16dip minus the held-out
file gri_33125010469852 (Desjardins II), order 3. Matched control: Italian from the held-out file, cut into 20 windows of
no. 7's own run lengths (the cipher is runs interleaved with clear words, so the concatenation carries the same run-boundary
breaks), enciphered with a random K=45 homophonic key; seven of its signs, chosen to carry the target's fixed letters
(a, n, o, e, r, o, e) at the nearest token counts, are held at their true letters; the same solver reads it.

  python3 run_test_no07.py control --seeds 1 2 3 4 5        # control first (gate in the PREREG)
  python3 run_test_no07.py target --seeds 1 2 3             # only if the control mean meets the gate
  python3 run_test_no07.py shuffled --seeds 1 2 3           # order-shuffled target, same solver (ARM-C1 null)
  python3 run_test_no07.py --check                          # exits non-zero if results_no07.json is stale vs the tok file
"""
import argparse, gzip, hashlib, json, random, sys, time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import homophonic_anneal as H  # noqa: E402

DATA = ROOT / "tools/data/it16dip"
MODEL_FILES = ["bub_gb_laRnTtJmsDAC.txt.gz", "bub_gb_ZJMxff7r4LUC.txt.gz", "letterediprincip01char.txt.gz",
               "letterediprincip02char.txt.gz", "letterediprincip03char.txt.gz"]
HELDOUT = "gri_33125010469852.txt.gz"
TOK = ROOT / "ciphers/siena-concistoro-2308/transcripts/no07.tok"
OUT = Path(__file__).with_name("results_no07.json")
FIX = {"q": "a", "6": "n", "+": "o", "2": "e", "x": "r", "c": "o", "QP": "e"}  # glosses_no07.tsv grade C
RESTARTS, ITERS = 20, 60000


def runs():
    return [l.split() for l in open(TOK, encoding="utf-8") if l.strip() and not l.startswith("#")]


def model():
    texts = [gzip.open(DATA / f, "rt", encoding="utf-8").read() for f in MODEL_FILES]
    return H.Model(texts, 3)


def control_plain(seed, lens):
    t = H.fold(gzip.open(DATA / HELDOUT, "rt", encoding="utf-8").read())
    rng = random.Random(seed)
    return "".join(t[s:s + n] for n in lens for s in [rng.randrange(0, len(t) - n)])


def pick_fixed(seq, truth, target_counts):
    cnt = Counter(seq)
    chosen = {}
    for letter, n in target_counts:
        cands = [s for s in cnt if truth[s] == letter and s not in chosen]
        if cands:
            s = min(cands, key=lambda s: abs(cnt[s] - n))
            chosen[s] = letter
    return chosen


def run_control(seeds, m):
    seq_t = [x for r in runs() for x in r]
    tc = Counter(seq_t)
    target_counts = [(FIX[s], tc[s]) for s in FIX]
    lens = [len(r) for r in runs()]
    rows = []
    for sd in seeds:
        p = control_plain(sd, lens)
        seq, p, truth = H.make_control(p, len(tc), len(seq_t), m, sd)
        fixed = pick_fixed(seq, truth, target_counts)
        fset = set(fixed)
        nfix = sum(1 for x in seq if x in fset)
        row = {"seed": sd, "N": len(seq), "K": len(set(seq)), "fixed_signs": len(fixed), "fixed_tokens": nfix}
        for mode, fx in (("blind", {}), ("anchored", fixed)):
            res = H.solve(seq, m, RESTARTS, ITERS, sd, 1.0, fx)
            key = res[0][1]
            dec = "".join(key[x] for x in seq)
            ok = sum(a == b for a, b in zip(dec, p))
            okf = sum(a == b for a, b, x in zip(dec, p, seq) if x not in fset)
            row[mode] = {"share": round(ok / len(p), 3), "share_unfixed_tokens": round(okf / (len(p) - nfix), 3),
                         "decoded": dec[:120]}
        row["plain"] = p[:120]
        rows.append(row)
        print(json.dumps({k: v for k, v in row.items() if k not in ("plain",)}, ensure_ascii=False), flush=True)
    mean = sum(r["anchored"]["share"] for r in rows) / len(rows)
    return {"rows": rows, "anchored_mean": round(mean, 3),
            "blind_mean": round(sum(r["blind"]["share"] for r in rows) / len(rows), 3)}


def run_target(seeds, m, shuffle=False):
    seq0 = [x for r in runs() for x in r]
    out = []
    for sd in seeds:
        seq = list(seq0)
        if shuffle:
            random.Random(100 + sd).shuffle(seq)
        res = H.solve(seq, m, RESTARTS, ITERS, sd, 1.0, dict(FIX))
        sc, key = res[0][:2]
        dec = "".join(key[x] for x in seq)
        out.append({"seed": sd, "score": round(sc, 2), "key": key, "decoded": dec,
                    "restart_scores": [round(r[0], 1) for r in res]})
        print(sd, round(sc, 1), dec, flush=True)
    return out


def tok_sha():
    return hashlib.sha1(TOK.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", nargs="?", choices=["control", "target", "shuffled"])
    ap.add_argument("--seeds", type=int, nargs="+", default=[1, 2, 3])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    res = json.loads(OUT.read_text()) if OUT.exists() else {}
    if a.check:
        ok = res.get("tok_sha1") == tok_sha() and "control" in res
        print("results_no07.json", "current" if ok else "STALE or missing")
        sys.exit(0 if ok else 1)
    t0 = time.time()
    m = model()
    if a.mode == "control":
        res["control"] = run_control(a.seeds, m)
    else:
        res[a.mode] = run_target(a.seeds, m, shuffle=(a.mode == "shuffled"))
    res.update({"tok_sha1": tok_sha(), "restarts": RESTARTS, "iters": ITERS, "model": MODEL_FILES, "heldout": HELDOUT,
                "fix": FIX})
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1))
    print(f"{a.mode} done in {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
