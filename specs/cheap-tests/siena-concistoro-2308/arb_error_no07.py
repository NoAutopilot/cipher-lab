"""R10-SIENA7C (6 Oct 2026): agent J's sign error on no. 7 from the worker's image arbitration of the agent J / pass B
splits (transcripts/no07_arbitration_R9-SIENA7B.tsv for L03/L08, transcripts/no07_arbitration_R10-SIENA7C.tsv for
L02, L04-L07, L09-L11 and a token-by-token check of L12). Decision rule: PREREG-R10-SIENA7C.md.

One TSV row = one agent J error event. low = B rows / J tokens; high = (B + amb) rows / J tokens; Clopper-Pearson 95%.
The arbitration is not blind and does not see errors both readers share.

  python3 arb_error_no07.py           # print the figures, write arb_error_no07.json
  python3 arb_error_no07.py --check   # exit non-zero if arb_error_no07.json is stale
"""
import argparse, hashlib, json, sys
from pathlib import Path
from math import comb

ROOT = Path(__file__).resolve().parents[3]
T = ROOT / "ciphers/siena-concistoro-2308/transcripts"
FILES = [T / "no07_arbitration_R9-SIENA7B.tsv", T / "no07_arbitration_R10-SIENA7C.tsv"]
TOK = T / "no07.tok"
OUT = Path(__file__).with_name("arb_error_no07.json")
# agent J tokens per line (no07.txt line split; sums to the 363 tokens of no07.tok)
NJ = {"L02": 22, "L03": 23, "L04": 39, "L05": 22, "L06": 49, "L07": 29, "L08": 49, "L09": 33, "L10": 22, "L11": 39, "L12": 36}
BOUNDARY = {("L04", "r"), ("L05", "5 6~ o"), ("L06", "a f a")}  # clear/cipher boundary calls, not sign identity


def _cdf(k, n, p):
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k + 1))


def _solve(f, target):  # f increasing in p on [0, 1]
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) < target else (lo, mid)
    return (lo + hi) / 2


def cp(k, n, a=0.05):
    """Clopper-Pearson interval by exact binomial tail inversion (stdlib only)."""
    lo = 0.0 if k == 0 else _solve(lambda p: 1 - _cdf(k - 1, n, p), a / 2)
    hi = 1.0 if k == n else _solve(lambda p: -_cdf(k, n, p), -a / 2)
    return round(lo, 4), round(hi, 4)


def rows():
    out = []
    for f in FILES:
        hdr = None
        for ln in f.read_text().splitlines():
            if ln.startswith("#") or not ln.strip():
                continue
            p = ln.split("\t")
            if hdr is None:
                hdr = p; continue
            out.append(dict(zip(hdr, p)))
    return out


def figures(rs, lines, drop_boundary=False):
    n = sum(NJ[l] for l in lines)
    sel = [r for r in rs if r["line"] in lines]
    if drop_boundary:
        dropped = sum(len(r["J"].split()) for r in sel if (r["line"], r["J"]) in BOUNDARY)
        n -= dropped
        sel = [r for r in sel if (r["line"], r["J"]) not in BOUNDARY]
    b = sum(r["verdict"] == "B" for r in sel)
    amb = sum(r["verdict"] == "amb" for r in sel)
    return {"n_J": n, "rows": len(sel), "B": b, "amb": amb,
            "low": round(b / n, 4), "low_cp95": cp(b, n),
            "high": round((b + amb) / n, 4), "high_cp95": cp(b + amb, n)}


def verdict(f):
    if f["high"] >= 0.10:
        return "conditional: high estimate at or over the 10% crossover"
    if f["high_cp95"][1] < 0.10:
        return "control-backed on the whole letter (high estimate and its 95% upper bound under 10%)"
    return "control-backed at the point estimate, not at the 95% bound"


def compute():
    assert sum(NJ.values()) == len([t for ln in TOK.read_text().splitlines() if not ln.startswith("#") for t in ln.split()])
    rs = rows()
    prim = [f"L{i:02d}" for i in range(2, 12)]
    r = {"inputs_sha1": {p.name: hashlib.sha1(p.read_bytes()).hexdigest() for p in FILES + [TOK]},
         "primary_L02_L11": figures(rs, prim), "all_L02_L12": figures(rs, prim + ["L12"]),
         "primary_sign_identity_only": figures(rs, prim, drop_boundary=True)}
    r["verdict_primary"] = verdict(r["primary_L02_L11"])
    r["verdict_all"] = verdict(r["all_L02_L12"])
    return r


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    r = compute()
    if ap.parse_args().check:
        if json.loads(OUT.read_text()) != json.loads(json.dumps(r)):
            print("STALE: arb_error_no07.json differs from a fresh computation"); sys.exit(1)
        print("ok: arb_error_no07.json current"); return
    OUT.write_text(json.dumps(r, indent=1) + "\n")
    for k, v in r.items():
        if k != "inputs_sha1":
            print(k, json.dumps(v))


if __name__ == "__main__":
    main()
