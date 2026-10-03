#!/usr/bin/env python3
"""Rate-matched nl18 judge gate for the 4.VEL 2077 legend reading (GAPS22, 3 Oct 2026).

Pre-registered in judge/ratematch_gaps22/prereg.md (commit d303d4ca, pushed before any score). Held-out nl18 prose
(leave-one-file-out) is corrupted with the target's own grade mask (U dropped, M -> random letter, H kept), giving the
PASS distribution; the same mask on letter-shuffled windows gives the null; power is checked per fold before the
target is scored; shuffles of the target give the shuffled-target check. `--pm 0.5` is the non-gating sensitivity run
(M replaced at probability 0.5). Writes judge/ratematch_gaps22/result[_pm<p>].tsv.
Usage: python3 ciphers/na-suriname-map-1781/judge_nl18_ratematch.py [--pm 1.0] [--outdir ratematch_gaps22]
"""
import argparse, csv, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
from judge_plaintext import LANG_CORPORA, NgramModel, fold, pct, read_corpus  # noqa: E402

S = 400; AZ = "abcdefghijklmnopqrstuvwxyz"


def mask():
    with open(HERE / "reading_2077_legend_nieuw_tokens.tsv") as fh:
        return [r["grade"] for r in csv.DictReader(fh, delimiter="\t")]


def corrupt(w, mk, pm, rnd):
    out = []
    for ch, g in zip(w, mk):
        if g == "U":
            continue
        out.append(rnd.choice(AZ) if g == "M" and rnd.random() < pm else ch)
    return "".join(out)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--pm", type=float, default=1.0)
    ap.add_argument("--outdir", default="ratematch_gaps22", help="subdir of judge/ (GAPS45 re-run: ratematch_gaps45)")
    a = ap.parse_args()
    mk = mask(); L = len(mk)
    target = fold("".join(l for l in (HERE / "judge" / "2077_legend_first.txt").read_text().splitlines() if not l.startswith("#")))
    files = LANG_CORPORA["nl18"]; texts = [read_corpus(p) for p in files]
    rows = []
    for k, held in enumerate(files):
        m = NgramModel([t for i, t in enumerate(texts) if i != k]); ht = fold(texts[k])
        rnd = random.Random(100 + k); R, Z = [], []
        for _ in range(S):
            j = rnd.randrange(0, len(ht) - L); w = ht[j:j + L]
            R.append(m.score(corrupt(w, mk, a.pm, rnd)))
            ws = list(w); rnd.shuffle(ws); Z.append(m.score(corrupt("".join(ws), mk, a.pm, rnd)))
        R.sort(); Z.sort(); r05, z99 = pct(R, .05), pct(Z, .99); thr = max(r05, z99)
        power = sum(x > z99 for x in R) / S
        rows.append(dict(fold=k, held_out=held.name, n_corrupt=len(corrupt(ht[:L], mk, a.pm, rnd)),
                         R_p05=round(r05, 4), R_median=round(pct(R, .5), 4), Z_p99=round(z99, 4), thr=round(thr, 4),
                         power=round(power, 4), powered=power >= 0.95, m=m))
        print(f"POWER fold={k} {held.name} R_p05={r05:.3f} R_med={pct(R,.5):.3f} Z_p99={z99:.3f} power={power:.3f}", flush=True)
    npow = sum(r["powered"] for r in rows)
    print(f"powered folds: {npow}/{len(rows)}", flush=True)
    if npow < 5:
        verdict = "NON-TEST at this error (fewer than 5 of 7 folds powered); target not scored"
    else:
        for k, r in enumerate(rows):
            m = r.pop("m"); rnd = random.Random(900 + k); T = []
            for _ in range(S):
                l = list(target); rnd.shuffle(l); T.append(m.score("".join(l)))
            sc = m.score(target)
            r.update(target_N=len(target), target=round(sc, 4), target_pass=sc > r["thr"], T_max=round(max(T), 4),
                     T_pass_rate=round(sum(x > r["thr"] for x in T) / S, 4))
        pw = [r for r in rows if r["powered"]]
        npass = sum(r["target_pass"] for r in pw)
        void = any(r["T_pass_rate"] > 0.05 for r in pw)
        v = "PASS" if npass == len(pw) else ("FAIL" if (len(pw) - npass) > len(pw) / 2 else "MIXED")
        verdict = f"{v} ({npass}/{len(pw)} powered folds); shuffled-target check {'VOID' if void else 'clear'}"
    for r in rows:
        r.pop("m", None)
    out = HERE / "judge" / a.outdir / ("result.tsv" if a.pm == 1.0 else f"result_pm{a.pm}.tsv")
    with open(out, "w") as fh:
        keys = list(rows[0].keys()); fh.write("\t".join(keys) + "\n")
        for r in rows:
            fh.write("\t".join(str(r.get(x, "")) for x in keys) + "\n")
        fh.write(f"# pm={a.pm} samples={S} verdict: {verdict}\n")
    for r in rows:
        print("\t".join(f"{x}={y}" for x, y in r.items()))
    print("VERDICT", verdict)


if __name__ == "__main__":
    main()
