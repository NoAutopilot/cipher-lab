#!/usr/bin/env python3
"""Known-answer power check of gate G1 (witness/key71/PREREG4_g1power.md, GAPS83, 3 Oct 2026).

  python3 scripts/g1_power_check.py [--seeds 20]

Enciphers the 22 gloss texts of witness/f4712_7r_pairs_img.tsv with Tomokiyo's numeric homophones (K1 clean; K2 with
word-codes at p=0.15 and 10 pct substitution; K3 at 20 pct), runs scripts/f4712_7r_gates.py's own numeral mapping and
flat-start alignment, and reports A/S, S and the G1 PASS rate per condition. Writes witness/g1_power.tsv.
"""
import argparse, csv, random, re, subprocess, sys, tempfile, unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from f4712_7r_gates import HERE, REPO, p99, to_numeral, tomokiyo  # noqa: E402

PAIRS = HERE / "witness/f4712_7r_pairs_img.tsv"
COND = {"K1": (0.0, 0.0), "K2": (0.15, 0.10), "K3": (0.15, 0.20)}


def norm(word):
    s = unicodedata.normalize("NFKD", word).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z]", "", s.replace("j", "i").replace("v", "u"))


def encipher(text, homs, rng, pmark, psub):
    out = []
    for w in text.split():
        w = "".join(c for c in norm(w) if c in homs)
        if not w:
            continue
        if rng.random() < pmark:
            out.append(rng.choice("dtb") + str(rng.randint(1, 99)))
            continue
        for c in w:
            out.append(str(rng.randint(1, 99)) if rng.random() < psub else rng.choice(homs[c]))
    return out


def g1(rows, tomo, tmp):
    num = tmp / "pairs_numeral.tsv"
    with open(num, "w", encoding="utf-8") as g:
        g.write("plain_line\tplain_raw\tcipher_line\tcipher_raw\n")
        for i, (plain, toks) in enumerate(rows):
            nt = [t for t in (to_numeral(x) for x in toks) if t]
            g.write(f"S{i}\t{plain}\tS{i}\t{' '.join(nt)}\n")
    akey = tmp / "key.tsv"
    subprocess.run([sys.executable, str(REPO / "tools/interlinear_align.py"), "align", str(num), str(tmp / "al.tsv"),
                    str(akey), "--floor", "100", "--keep-fs"], check=True, stdout=subprocess.DEVNULL)
    learned = {r["value"]: r["meaning"] for r in csv.DictReader(open(akey, encoding="utf-8"), delimiter="\t")}
    letters = {v: m for v, m in learned.items() if int(v) < 100 and len(m) == 1 and v in tomo}
    A, S = sum(1 for v, m in letters.items() if tomo[v] == m), len(letters)
    codes, vals = list(tomo), list(tomo.values())
    rng = random.Random(4712)
    ctl = []
    for _ in range(10000):
        rng.shuffle(vals)
        perm = dict(zip(codes, vals))
        ctl.append(sum(1 for v, m in letters.items() if perm[v] == m))
    q = p99(ctl)
    return A, S, q, (S >= 12 and A / S >= 0.70 and A > q)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seeds", type=int, default=20)
    a = ap.parse_args()
    tomo = tomokiyo()
    homs = {}
    for code, v in tomo.items():
        homs.setdefault(v, []).append(code)
    texts = [r["plain_raw"] for r in csv.DictReader((l for l in open(PAIRS, encoding="utf-8") if not l.startswith("#")),
                                                     delimiter="\t")]
    out = open(HERE / "witness/g1_power.tsv", "w", encoding="utf-8")
    out.write("condition\tseed\tA\tS\tA_over_S\tp99\tG1\n")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        for c, (pm, ps) in COND.items():
            res = []
            for seed in range(1, a.seeds + 1):
                rng = random.Random(seed)
                rows = [(t, encipher(t, homs, rng, pm, ps)) for t in texts]
                A, S, q, ok = g1(rows, tomo, tmp)
                res.append((A, S, q, ok))
                out.write(f"{c}\t{seed}\t{A}\t{S}\t{A / S if S else 0:.3f}\t{q}\t{'PASS' if ok else 'FAIL'}\n")
            r = sorted(A / S if S else 0 for A, S, _, _ in res)
            s = sorted(S for _, S, _, _ in res)
            print(f"{c} (pmark {pm}, psub {ps}): A/S median {r[len(r) // 2]:.3f} min {r[0]:.3f} max {r[-1]:.3f} | "
                  f"S median {s[len(s) // 2]} | G1 PASS {sum(x[3] for x in res)}/{len(res)}")


if __name__ == "__main__":
    main()
