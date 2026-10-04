#!/usr/bin/env python3
"""PREREG_test1.md for fr16045 f.75: Tomokiyo's 1585 table vs key-shuffle and order-shuffle nulls, positive control.

python3 test1.py [--cipher tx/ciphertext_draft.tsv] [--out test1_result.json]
"""
import argparse, json, random, sys, gzip
from pathlib import Path
D = Path(__file__).resolve().parent
R = D.parents[1]
sys.path.insert(0, str(R / "tools"))
import judge_plaintext as jp

def load_key():
    k = {}
    for ln in (D / "key.tsv").read_text().splitlines()[1:]:
        s, v = ln.split("\t")[:2]
        k[s] = "c" if v == "b|c" else ("" if v == "<null>" else v)
    return k

def load_tokens(path):
    rows, dropped = [], 0
    for ln in Path(path).read_text().splitlines():
        if not ln.strip() or ln.startswith("row") or ln.startswith("line"):
            continue
        parts = ln.split("\t")
        toks = parts[1].split() if len(parts) > 1 else []
        for t in toks:
            if t.startswith("?"):
                dropped += 1; continue
            t = t.rstrip("?")
            if t == "S07": t = "S04"
            if t == "S08": t = "S05"
            rows.append(t)
    return rows, dropped

def decode(tokens, key):
    return [key.get(t, "") for t in tokens]

def tok_from_draft(path):
    # ciphertext_draft.tsv from reconcile_passes: long format line/pos/sign; fall back to wide
    lines = Path(path).read_text().splitlines()
    hdr = lines[0].split("\t")
    if "sign" in hdr or "token" in hdr:
        ci = hdr.index("sign") if "sign" in hdr else hdr.index("token")
        toks, dropped = [], 0
        for ln in lines[1:]:
            f = ln.split("\t")
            if len(f) <= ci or not f[ci].strip(): continue
            t = f[ci].strip()
            if t.startswith("?") or t in ("-", "_"): dropped += 1; continue
            t = t.rstrip("?"); t = {"S07": "S04", "S08": "S05"}.get(t, t)
            toks.append(t)
        return toks, dropped
    return load_tokens(path)

def stats(model, units, key_tokens, key, rnd, na, nb):
    sc = model.score("".join(units))
    labs = list(key); vals = [key[l] for l in labs]
    a = []
    for _ in range(na):
        p = vals[:]; rnd.shuffle(p); kk = dict(zip(labs, p))
        a.append(model.score("".join(kk.get(t, "") for t in key_tokens)))
    b = []
    for _ in range(nb):
        u = units[:]; rnd.shuffle(u); b.append(model.score("".join(u)))
    a.sort(); b.sort()
    return sc, jp.pct(a, 0.99), jp.pct(b, 0.99)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cipher", default=str(D / "tx" / "ciphertext_draft.tsv"))
    ap.add_argument("--extra", nargs="*", default=[str(D / "tx" / "passA.tsv"), str(D / "tx" / "passB.tsv")])
    ap.add_argument("--err", type=float, required=True, help="measured err_2reader")
    ap.add_argument("--out", default=str(D / "test1_result.json"))
    a = ap.parse_args()
    F = R / "tools" / "data" / "fr16"
    model = jp.NgramModel([jp.read_corpus(F / "lettresdecatheri01cathuoft_djvu.txt.gz"),
                           jp.read_corpus(F / "lettresindites00marg_djvu.txt.gz")])
    held = jp.fold(jp.read_corpus(F / "lettresdecatheri02cathuoft_djvu.txt.gz"))
    key = load_key(); rnd = random.Random(20261004)
    out = {"prereg": "PREREG_test1.md", "err_2reader": a.err}
    toks, dropped = tok_from_draft(a.cipher)
    units = decode(toks, key); N = len("".join(units))
    sc, pa, pb = stats(model, units, toks, key, rnd, 1000, 500)
    out["target"] = {"file": Path(a.cipher).name, "signs": len(toks), "dropped": dropped, "letters": N,
                     "score": round(sc, 4), "keyshuffle_p99": round(pa, 4), "order_p99": round(pb, 4),
                     "pass": sc > pa and sc > pb}
    for f in a.extra:
        if Path(f).exists():
            t2, d2 = load_tokens(f); u2 = decode(t2, key)
            s2, a2, b2 = stats(model, u2, t2, key, rnd, 1000, 500)
            out[Path(f).stem] = {"signs": len(t2), "dropped": d2, "score": round(s2, 4), "keyshuffle_p99": round(a2, 4),
                                 "order_p99": round(b2, 4), "pass": s2 > a2 and s2 > b2}
    inv = {}
    for l, v in key.items():
        if len(v) == 1: inv.setdefault(v, []).append(l)
    labs = list(key); seeds = []
    for s in range(5):
        r2 = random.Random(100 + s); j = r2.randrange(0, len(held) - N - 1)
        txt = held[j:j + N].replace("j", "i").replace("v", "u")
        ct = [r2.choice(inv[c]) for c in txt if c in inv]
        ct = [r2.choice([x for x in labs if x != t]) if r2.random() < a.err else t for t in ct]
        u = decode(ct, key)
        cs, ca, cb = stats(model, u, ct, key, r2, 200, 200)
        seeds.append({"seed": s, "score": round(cs, 4), "keyshuffle_p99": round(ca, 4), "order_p99": round(cb, 4),
                      "pass": cs > ca and cs > cb})
    npass = sum(x["pass"] for x in seeds)
    out["positive_control"] = {"seeds": seeds, "passed": npass, "pass": npass >= 4, "e": a.err, "N": N}
    t = out["target"]["pass"]; c = out["positive_control"]["pass"]
    if not c: v = "NON-TEST (positive control failed)"
    elif t: v = "PASS"
    elif a.err > 0.10: v = "NON-TEST (target FAIL at err_2reader > 0.10)"
    else: v = "FAIL"
    out["verdict"] = v
    Path(a.out).write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
