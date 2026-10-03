#!/usr/bin/env python3
"""VERIFY-DIN (account-3 verifier, 3 Oct 2026): independent checks on the A2-DIN2/A2-DIN3 f.130r result.

  python3 ciphers/fr3621-dinteville-1592/verify/verify_din.py           write verify/result.json
  python3 ciphers/fr3621-dinteville-1592/verify/verify_din.py --check   exit 1 if verify/result.json is stale

Re-uses the solvers' own functions (f130/score_f130.py, f130/repair_f130.py) unchanged; adds:
 1. fresh-seed reruns of both controls (seeds 31001-31003 for the key_syl shuffle, 31001-31002 for the repair control);
 2. a frequency-banded shuffle (letters permuted only within blocks of 4 signs adjacent in f.130 frequency rank), a
    stronger null than the free shuffle because it keeps "frequent sign -> frequent letter";
 3. known-answer test of the repair climb on the real text: each held key_syl C row is freed in turn (with the 17 free
    rows), climbed from 5 random starts, and scored for recovering its gloss value; plus the gloss agreement of the
    raw climbed values of the 13 free key_syl rows against chance;
 4. power control: a synthetic homophonic French cipher of f.130's own run structure (527 signs) + an f.128-sized
    segment (183), 33 sign types, plaintext from lettresdecatheri02 (held out), judged by a 4-gram model built from the
    other two fr16 files only; transcription error 0 / 5.5 / 11 / 16.5% (substitutions + indels); key with 0 / 4 / 8
    wrong rows; true-key-vs-1000-shuffles rank, and repair-climb recovery of 13 freed rows (+4 unkeyed) at each error
    level. Real f.130 is rescored under the same held-out model for comparison.
"""
import csv, importlib.util, json, math, random, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TGT = HERE.parent
ROOT = TGT.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import NgramModel, read_corpus, fold  # noqa: E402


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


S = load("score_f130", TGT / "f130" / "score_f130.py")
R = load("repair_f130", TGT / "f130" / "repair_f130.py")
AZ = R.AZ
FR16 = sorted((ROOT / "tools" / "data" / "fr16").glob("*.txt.gz"))


def pct(xs, q):
    xs = sorted(xs); return xs[int(q * (len(xs) - 1))]


def summ(real, xs):
    return {"real": round(real, 4), "mean": round(sum(xs) / len(xs), 4), "p95": round(pct(xs, 0.95), 4),
            "max": round(max(xs), 4), "ge_real": sum(1 for x in xs if x >= real), "n": len(xs)}


def keysyl_shuffle(model, ct, key, seed, banded=False):
    val = {s: v[0] for s, v in key.items()}
    real = S.stat(model, S.runs(ct, val))[0]
    signs = sorted(val); rnd = random.Random(seed); out = []
    if banded:
        cnt = Counter(r["sign"] for r in ct)
        order = sorted(signs, key=lambda s: -cnt.get(s, 0))
        blocks = [order[i:i + 4] for i in range(0, len(order), 4)]
    for _ in range(1000):
        if banded:
            v = {}
            for b in blocks:
                l = [val[s] for s in b]; rnd.shuffle(l); v.update(zip(b, l))
        else:
            l = [val[s] for s in signs]; rnd.shuffle(l); v = dict(zip(signs, l))
        out.append(S.stat(model, S.runs(ct, v))[0])
    return summ(real, out)


def repair_setup(model):
    key = R.load_key(); gl = R.gloss_letters(); ct, f128 = R.texts()
    signs = sorted(set(key) | set(R.FREE)); sid = {s: i for i, s in enumerate(signs)}
    W = R.build_windows(ct, f128, set(signs), sid); T = R.table(model)
    base = [AZ.index(key[s][0]) if s in key else AZ.index("e") for s in signs]
    return key, gl, signs, sid, W, T, base


def repair_control(setup, seed):
    key, gl, signs, sid, W, T, base = setup
    free_ids = [sid[s] for s in R.FREE]; touch = {f: [w for w in W if f in w] for f in free_ids}
    rv, _ = R.climb(T, W, base, free_ids, touch); rv, _ = R.reject(rv, base, free_ids, signs, gl)
    real = R.score(T, W, rv)
    rnd = random.Random(seed); ks = sorted(key); letters = [key[s][0] for s in ks]; out = []
    for _ in range(1000):
        p = letters[:]; rnd.shuffle(p); v0 = list(base)
        for s, l in zip(ks, p):
            v0[sid[s]] = AZ.index(l)
        cv, _ = R.climb(T, W, v0, free_ids, touch); cv, _ = R.reject(cv, v0, free_ids, signs, gl)
        out.append(R.score(T, W, cv))
    return summ(real, out)


def known_answer_real(setup):
    key, gl, signs, sid, W, T, base = setup
    held = [s for s in sorted(key) if s not in R.FREE and key[s][1] >= 3 and key[s][1] / key[s][2] >= 0.5]
    rnd = random.Random(31010); rows = {}
    for s in held:
        free = [sid[x] for x in R.FREE] + [sid[s]]; touch = {f: [w for w in W if f in w] for f in free}
        hits = 0
        for _ in range(5):
            v0 = list(base)
            for f in free:
                v0[f] = rnd.randrange(26)
            cv, _ = R.climb(T, W, v0, free, touch)
            hits += AZ[cv[sid[s]]] == key[s][0]
        rows[s] = hits
    # raw climbed values of the 13 free key_syl rows vs the gloss letter sets
    free_ids = [sid[x] for x in R.FREE]; touch = {f: [w for w in W if f in w] for f in free_ids}
    rv, _ = R.climb(T, W, base, free_ids, touch)
    fk = [s for s in R.FREE if s in key]
    agree = {s: AZ[rv[sid[s]]] in gl.get(s, {}) for s in fk}
    chance = sum(len(gl.get(s, {})) / 26 for s in fk)
    return {"held_rows": len(held), "recovered_majority": sum(1 for h in rows.values() if h >= 3),
            "recovered_any_of_5": sum(1 for h in rows.values() if h >= 1), "per_row_hits_of_5": rows,
            "free_keysyl_rows": len(fk), "raw_climb_agrees_gloss": sum(agree.values()),
            "raw_climb_agree_detail": {s: (AZ[rv[sid[s]]], bool(a)) for s, a in agree.items()},
            "chance_expected_agree": round(chance, 2)}


# ---------------------------------------------------------------- power control (synthetic, held-out model)
def synth(text_letters, struct, nsign, rnd, err):
    """encrypt plaintext along struct (list of segment lengths) with a homophonic key of nsign types; add err."""
    freq = Counter(text_letters); tot = sum(freq.values())
    letters = [l for l, _ in freq.most_common()]
    alloc = {l: 0 for l in letters}
    # each letter by frequency gets one sign until nsign-? then extra homophones to the largest by remainder
    base_n = min(len(letters), 22)
    for l in letters[:base_n]:
        alloc[l] = 1
    for _ in range(nsign - base_n):
        l = max(letters[:base_n], key=lambda x: freq[x] / tot * nsign / (alloc[x] + 1)); alloc[l] += 1
    key, signs_of, sid = {}, {}, 0
    for l in letters[:base_n]:
        signs_of[l] = list(range(sid, sid + alloc[l]))
        for s in signs_of[l]:
            key[s] = l
        sid += alloc[l]
    pt = [l for l in text_letters if l in signs_of]
    segs, i = [], 0
    for n in struct:
        segs.append([rnd.choice(signs_of[l]) for l in pt[i:i + n]]); i += n
    noisy = []
    for seg in segs:
        out = []
        for s in seg:
            u = rnd.random()
            if u < err * 2 / 3:
                out.append(rnd.choice([x for x in range(nsign) if x != s]))
            elif u < err * 5 / 6:
                continue
            elif u < err:
                out.append(s); out.append(rnd.randrange(nsign))
            else:
                out.append(s)
        noisy.append(out)
    return key, noisy


def windows(segs):
    return [tuple(seg[i:i + 4]) for seg in segs for i in range(len(seg) - 3)]


def power(model_ho, T, ct, rnd_seed=31020):
    rnd = random.Random(rnd_seed)
    raw = fold(read_corpus(FR16[1]))  # lettresdecatheri02 (held out of model_ho)
    struct = []
    cur = 0
    for r in ct:
        if r["sign"].startswith("CLEAR:"):
            if cur:
                struct.append(cur)
            cur = 0
        else:
            cur += 1
    if cur:
        struct.append(cur)
    struct.append(183)  # f.128-sized segment, as repair_f130 scores f.130 + f.128
    nsign = 33
    res = {}
    for err in (0.0, 0.055, 0.11, 0.165):
        for wrong in (0, 4, 8):
            ranks, reals, rec, recs = [], [], [], []
            for rep in range(5):
                j = rnd.randrange(200000, len(raw) - 5000)
                key, segs = synth(raw[j:j + 3000], struct, nsign, rnd, err)
                W = windows(segs)
                val = [AZ.index(key[s]) for s in range(nsign)]
                kv = list(val)
                for s in rnd.sample(range(nsign), wrong):
                    kv[s] = rnd.randrange(26)
                real = R.score(T, W, kv); reals.append(real)
                sh = []
                for _ in range(300):
                    p = kv[:]; rnd.shuffle(p); sh.append(R.score(T, W, p))
                ranks.append(sum(1 for x in sh if x >= real))
                # repair known-answer: free 17 rows (13 randomised from the true key + 4 start 'e'), climb
                free = rnd.sample(range(nsign), 17)
                v0 = list(val)
                for f in free:
                    v0[f] = rnd.randrange(26)
                touch = {f: [w for w in W if f in w] for f in free}
                cv, _ = R.climb(T, W, v0, free, touch)
                ok = sum(1 for f in free if cv[f] == val[f]); rec.append(ok / len(free))
                cnt = Counter(s for seg in segs for s in seg)
                # recovery restricted to signs with >= 10 occurrences (the S-graded real signs: v' 23, 0' 14, plus 20,
                # c 16 are >= 10; div 4, r 3, NEW 1+1 are not)
                big = [f for f in free if cnt[f] >= 10]
                recs.append((sum(1 for f in big if cv[f] == val[f]), len(big)))
            res[f"err{err}_wrong{wrong}"] = {
                "true_key_score_mean": round(sum(reals) / len(reals), 4),
                "shuffles_ge_real_of_300": ranks,
                "repair_recovery_mean": round(sum(rec) / len(rec), 3),
                "repair_recovery_signs_ge10": f"{sum(a for a, _ in recs)}/{sum(b for _, b in recs)}"}
    return res


def build():
    out = {}
    model = NgramModel([read_corpus(p) for p in FR16])
    ct = S.load_ct(); key = S.load_key()
    out["keysyl_shuffle_fresh"] = {str(sd): keysyl_shuffle(model, ct, key, sd) for sd in (31001, 31002, 31003)}
    out["keysyl_banded_shuffle"] = {str(sd): keysyl_shuffle(model, ct, key, sd, banded=True) for sd in (31001, 31002)}
    setup = repair_setup(model)
    out["repair_control_fresh"] = {str(sd): repair_control(setup, sd) for sd in (31001, 31002)}
    out["known_answer_real"] = known_answer_real(setup)
    # held-out model (no lettresdecatheri02) for the power control and a like-for-like rescore of the real leaf
    model_ho = NgramModel([read_corpus(FR16[0]), read_corpus(FR16[2])])
    T = R.table(model_ho)
    key_r, gl, signs, sid, W, _, base = setup
    rep = {}
    for r in csv.DictReader(open(TGT / "f130" / "repair" / "key_repaired.tsv"), delimiter="\t"):
        rep["#" if r["sign"] == "hash" else r["sign"]] = r["value"]
    rv = [AZ.index(rep[s]) for s in signs]
    out["real_under_heldout_model"] = {"repaired_key_f130_f128_runs": round(R.score(T, W, rv), 4),
                                       "keysyl_seed_f130_f128_runs": round(R.score(T, W, base), 4)}
    out["power_control"] = power(model_ho, T, ct)
    return json.dumps(out, indent=1, sort_keys=True) + "\n"


def main():
    t = build()
    if "--check" in sys.argv:
        ok = (HERE / "result.json").exists() and (HERE / "result.json").read_text() == t
        print("check: committed outputs match" if ok else "check: STALE result.json"); sys.exit(0 if ok else 1)
    (HERE / "result.json").write_text(t); print(t)


if __name__ == "__main__":
    main()
