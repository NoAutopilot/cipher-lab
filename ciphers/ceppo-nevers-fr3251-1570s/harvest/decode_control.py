#!/usr/bin/env python3
"""Decode a reconciled sign sequence of fr.3251 f.11r with the Ceppo-Nevers key, and test it (HARVEST-A, 28 Sept 2026).

Inputs: a TSV with columns passage, pos, sign_id (S## from harvest/sign_sheet_blind.png; '?' = unread), and
harvest/sign_id_map.json (S## -> key value, cut from Tomokiyo's nevers_add1.png; the transcribers never saw it).

1. Reading: each sign -> its key value (null dropped, 'et' -> et, '?' -> '_'), per passage.
2. Target control (rule 3): the real key's mean log10 4-gram score per letter (tools/judge_plaintext.py NgramModel,
   corpus it16dip) against N keys made by shuffling the value column of the same 55-entry sheet (same homophone counts,
   same null count, values moved between signs). Reports rank and z.
3. Power control: M windows of it16dip Italian, the target's own letter count, enciphered with the same key (a random
   homophone per letter; letters the key has no sign for -- b, x, y and k/w -- dropped; j->i, v->u), nulls inserted at the
   target's own null rate, then a fraction ERR of signs replaced by a random other sign (ERR = the two passes' measured
   disagreement), then the same N-shuffle test. The target's result means something only if the control's real key
   ranks first in most windows at that error.

Usage: python3 decode_control.py SEQ.tsv [--shuffles 200] [--windows 20] [--err 0.2] [--seed 1] [--out reading.txt]
"""
import argparse, csv, json, random, statistics, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "tools"))
import judge_plaintext as jp  # noqa: E402


def load_map():
    return {e["id"]: e["value"] for e in json.load(open(HERE / "sign_id_map.json"))}


def decode(seq, m):
    out = []
    for s in seq:
        v = m.get(s)
        if v is None:
            out.append("_")
        elif v == "null":
            continue
        else:
            out.append(v)
    return "".join(out)


def score(model, passages, m):
    # score each passage separately (they are separate cipher insertions), letter-weighted mean
    tot = n = 0
    for seq in passages.values():
        t = decode(seq, m).replace("_", "")
        if len(t) >= 4:
            tot += model.score(t) * (len(t) - 3); n += len(t) - 3
    return tot / n if n else -9.9


def shuffle_test(model, passages, m, N, rng):
    real = score(model, passages, m)
    ids = list(m); vals = [m[i] for i in ids]
    sh = []
    for _ in range(N):
        rng.shuffle(vals)
        sh.append(score(model, passages, dict(zip(ids, vals))))
    rank = 1 + sum(1 for x in sh if x >= real)
    mu, sd = statistics.mean(sh), statistics.pstdev(sh)
    return real, rank, mu, sd, max(sh), (real - mu) / sd if sd else 0.0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("seq"); ap.add_argument("--shuffles", type=int, default=200)
    ap.add_argument("--windows", type=int, default=20); ap.add_argument("--err", type=float, default=0.2)
    ap.add_argument("--seed", type=int, default=1); ap.add_argument("--out")
    ap.add_argument("--corpus", default="it16dip")
    a = ap.parse_args()
    rng = random.Random(a.seed)
    m = load_map()
    passages = {}
    for r in csv.DictReader(open(a.seq), delimiter="\t"):
        passages.setdefault(r["passage"], []).append(r["sign_id"].strip())
    texts = [jp.read_corpus(p) if hasattr(jp, "read_corpus") else jp.load_text(p) for p in jp.LANG_CORPORA[a.corpus]]
    model = jp.NgramModel(texts)
    lines = []
    for k, seq in passages.items():
        lines.append(f"{k}\t{decode(seq, m)}")
    reading = "\n".join(lines) + "\n"
    print(reading)
    if a.out:
        Path(a.out).write_text(reading)
    real, rank, mu, sd, mx, z = shuffle_test(model, passages, m, a.shuffles, rng)
    nsig = sum(len(s) for s in passages.values())
    nnull = sum(1 for s in passages.values() for x in s if m.get(x) == "null")
    nlet = sum(len(decode(s, m).replace("_", "")) for s in passages.values())
    print(f"TARGET: {nsig} signs, {nnull} nulls, {nlet} letters; real key {real:.4f}; {a.shuffles} shuffled keys mean "
          f"{mu:.4f} sd {sd:.4f} max {mx:.4f}; z {z:.2f}; rank {rank} of {a.shuffles + 1}")
    # power control
    corpus = jp.fold("".join(texts)).replace("j", "i").replace("v", "u")
    corpus = "".join(c for c in corpus if c not in "bxykw")
    homs = {}
    for i, v in m.items():
        homs.setdefault(v, []).append(i)
    ids = list(m)
    null_rate = nnull / nsig if nsig else 0.0
    sizes = [len(decode(s, m).replace("_", "")) for s in passages.values()]
    firsts = 0; zs = []
    for w in range(a.windows):
        cp = {}
        for pi, L in enumerate(sizes):
            st = rng.randrange(len(corpus) - L - 1)
            seq = []
            for ch in corpus[st:st + L]:
                if ch not in homs:
                    continue
                seq.append(rng.choice(homs[ch]))
                if rng.random() < null_rate:
                    seq.append(rng.choice(homs["null"]))
            seq = [rng.choice(ids) if rng.random() < a.err else s for s in seq]
            cp[f"c{pi}"] = seq
        r2, rk, mu2, sd2, mx2, z2 = shuffle_test(model, cp, m, a.shuffles, rng)
        firsts += rk == 1; zs.append(z2)
    print(f"POWER CONTROL: {a.windows} it16dip windows, same passage lengths, err {a.err:.2f}: real key rank 1 in "
          f"{firsts}/{a.windows}; z median {statistics.median(zs):.2f} min {min(zs):.2f}")


if __name__ == "__main__":
    main()
