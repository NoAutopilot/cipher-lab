#!/usr/bin/env python3
"""f.130r: apply f128/key_syl.tsv to f130/ciphertext.tsv and test it against shuffled keys (pre-registered in NOTES.md,
A2-DIN2, 3 Oct 2026).

  python3 ciphers/fr3621-dinteville-1592/f130/score_f130.py           write reading.txt, tokens.tsv, control.tsv, result.json
  python3 ciphers/fr3621-dinteville-1592/f130/score_f130.py --check   exit 1 if the committed outputs are stale

Statistic: mean log10 4-gram P per letter (tools/judge_plaintext.py NgramModel, fr16 corpus, n=4, k=0.01) over all
4-letter windows wholly inside runs of keyed signs; an unkeyed sign or a CLEAR word breaks a run. Control: 1000 keys
with the letter values permuted among the keyed signs (seed 20261003). Grade per token: C if the key row has agree >= 3
and agree/n >= 0.5 and the sign's conf is 'H'; M if keyed otherwise; U if unkeyed.
"""
import csv, json, math, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import NgramModel, read_corpus  # noqa: E402

SEED, NSHUF = 20261003, 1000


def load_key():
    key = {}
    for r in csv.DictReader(open(HERE.parent / "f128" / "key_syl.tsv"), delimiter="\t"):
        n, a = int(r["n"]), int(r["agree"])
        key[r["sign"]] = (r["meaning"], a >= 3 and a / n >= 0.5)
    return key


def load_ct():
    return list(csv.DictReader(open(HERE / "ciphertext.tsv"), delimiter="\t"))


def runs(ct, val):
    out, cur = [], ""
    for r in ct:
        s = r["sign"]
        v = None if s.startswith("CLEAR:") else val.get(s)
        if v:
            cur += v
        else:
            if cur:
                out.append(cur)
            cur = ""
    if cur:
        out.append(cur)
    return out


def stat(model, rs):
    tot, n = 0.0, 0
    for s in rs:
        if len(s) < 4:
            continue
        w = len(s) - 3
        tot += model.score(s) * w; n += w
    return tot / n if n else float("nan"), n


def cover(model, rs):
    L = sum(len(s) for s in rs if len(s) >= 4)
    return sum(model.cover(s) * len(s) for s in rs if len(s) >= 4) / L if L else 0.0


def build(variant=""):
    key = load_key(); ct = load_ct()
    if variant == "o_stem":  # secondary, not pre-registered: 0' read with 0's value (f.128 wrote this glyph as 0), grade M
        key["0'"] = (key["0"][0], False)
    model = NgramModel([read_corpus(p) for p in sorted((ROOT / "tools" / "data" / "fr16").glob("*.txt.gz"))])
    val = {s: v[0] for s, v in key.items()}
    rs = runs(ct, val)
    real, nwin = stat(model, rs)
    rcov = cover(model, rs)
    rnd = random.Random(SEED); signs = sorted(val); letters = [val[s] for s in signs]
    ctrl = []
    for i in range(NSHUF):
        p = letters[:]; rnd.shuffle(p)
        rs2 = runs(ct, dict(zip(signs, p)))
        ctrl.append((stat(model, rs2)[0], cover(model, rs2)))
    sc = sorted(c[0] for c in ctrl)
    ge = sum(1 for c in sc if c >= real)
    res = {"stat": "fr16 4-gram mean log10 P/letter inside keyed runs", "real": round(real, 4), "windows": nwin,
           "shuf_mean": round(sum(sc) / len(sc), 4), "shuf_p95": round(sc[int(0.95 * (len(sc) - 1))], 4),
           "shuf_max": round(sc[-1], 4), "shuffles_ge_real": ge, "n_shuffles": NSHUF,
           "gate_pass": real > sc[int(0.95 * (len(sc) - 1))],
           "cover_real": round(rcov, 4), "cover_shuf_mean": round(sum(c[1] for c in ctrl) / len(ctrl), 4),
           "cover_shuf_p95": round(sorted(c[1] for c in ctrl)[int(0.95 * (len(ctrl) - 1))], 4)}
    # tokens and reading
    tok = ["line\tpos\tsign\tconf\tvalue\tgrade"]; g = {"C": 0, "M": 0, "U": 0}; lines = {}
    for r in ct:
        s = r["sign"]
        if s.startswith("CLEAR:"):
            lines.setdefault(r["line"], []).append("[" + s[6:] + "]"); continue
        if s in key:
            v, ok = key[s]; gr = "C" if ok and r["conf"] == "H" else "M"
        else:
            v, gr = "?", "U"
        g[gr] += 1
        tok.append(f"{r['line']}\t{r['pos']}\t{s}\t{r['conf']}\t{v}\t{gr}")
        lines.setdefault(r["line"], []).append(v if gr == "C" else (v.upper() if gr == "M" else "?"))
    res["grades"] = g; res["variant"] = variant or "primary (pre-registered)"
    reading = ["# f.130r decoded with f128/key_syl.tsv (score_f130.py). lower = C, UPPER = M, ? = unkeyed (U), [..] = clear.",
               f"# grades: C {g['C']} M {g['M']} U {g['U']}"]
    reading += [f"{ln}\t{' '.join(v)}" for ln, v in lines.items()]
    # decode_key.py inputs: its key reader skips a row whose sign is '#' (comment), so '#' is spelled 'hash' in these
    # two derived files only (rule 7 regeneration: tools/decode_key.py ciphers/fr3621-dinteville-1592 --check)
    kr = ["sign\tvalue\tgrade\tsource"]
    for r in csv.DictReader(open(HERE.parent / "f128" / "key_syl.tsv"), delimiter="\t"):
        n, a = int(r["n"]), int(r["agree"])
        kr.append(f"{'hash' if r['sign'] == '#' else r['sign']}\t{r['meaning']}\t{'C' if a >= 3 and a / n >= 0.5 else 'M'}\tf128/key_syl.tsv {a}/{n}")
    dk = ["line\tpos\tsign\tconf"] + [f"{r['line']}\t{r['pos']}\t{'hash' if r['sign'] == '#' else r['sign']}\t{r['conf']}" for r in ct]
    ctl = ["i\tstat\tcover"] + [f"{i}\t{a:.4f}\t{b:.4f}" for i, (a, b) in enumerate(ctrl)]
    return {"reading.txt": "\n".join(reading) + "\n", "tokens.tsv": "\n".join(tok) + "\n",
            "control.tsv": "\n".join(ctl) + "\n", "result.json": json.dumps(res, indent=1) + "\n",
            "key_dk.tsv": "\n".join(kr) + "\n", "ciphertext_dk.tsv": "\n".join(dk) + "\n"}


def main():
    out = build()
    out2 = build("o_stem")
    out.update({"o_stem_" + f: t for f, t in out2.items() if f in ("result.json", "reading.txt")})
    if "--check" in sys.argv:
        bad = [f for f, t in out.items() if not (HERE / f).exists() or (HERE / f).read_text() != t]
        print("check: committed outputs match" if not bad else f"check: STALE {bad}")
        sys.exit(1 if bad else 0)
    for f, t in out.items():
        (HERE / f).write_text(t)
    print(out["result.json"]); print(out["o_stem_result.json"])


if __name__ == "__main__":
    main()
