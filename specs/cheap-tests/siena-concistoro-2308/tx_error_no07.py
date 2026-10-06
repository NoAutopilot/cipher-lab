"""R9-SIENA7B (6 Oct 2026): per-sign disagreement between a second blind line-crop pass of no. 7 (pass B, one Sonnet
reader per half-page, Bourdeau's sign legend as the reference sheet, not his transcript) and agent J's transcription
(transcripts/no07.tok, Bourdeau, CC BY 4.0). Token-level Levenshtein alignment (unit costs) of the two whole sequences,
cipher tokens only ("[clear]" markers dropped; a trailing "?" is stripped for the alignment and counted separately).
Rates are per agent-J token: substitutions, insertions (in B only), deletions (in J only). This is reader DISAGREEMENT,
not a measured error of either reader: with independent errors it is roughly eJ + eB, so it bounds agent J's error from
above only if pass B is no worse than J (no known-answer calibration of pass B was run; TRANSCRIPTION.md).

  python3 tx_error_no07.py            # print the figures and the confusion pairs
  python3 tx_error_no07.py --check    # exit non-zero if tx_error_no07.json is stale against the two inputs
"""
import argparse, hashlib, json, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
T = ROOT / "ciphers/siena-concistoro-2308/transcripts"
J = T / "no07.tok"
B = T / "no07_passB_R9-SIENA7B.tsv"
OUT = Path(__file__).with_name("tx_error_no07.json")


def toks_j(drop_l12=False):
    runs = [ln.split() for ln in J.read_text().splitlines() if ln.strip() and not ln.startswith("#")]
    if drop_l12:
        runs = runs[:-2]  # agent J's last two runs are line L12 (no07.txt: L12 has two runs, 18 + 18 tokens)
    return [t for r in runs for t in r]


def toks_b(drop_l12=False):
    out, unsure = [], 0
    for ln in B.read_text().splitlines():
        if ln.startswith("#") or not ln.strip():
            continue
        parts = ln.split("\t")
        if drop_l12 and parts[0] == "L12":
            continue
        for t in (parts[1].split() if len(parts) > 1 else []):
            if t.startswith("[") or t in {".", "/"}:
                continue
            if t.endswith("?"):
                unsure += 1
                t = t.rstrip("?") or "UNK"
            out.append(t)
    return out, unsure


def align(a, b):
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + (a[i - 1] != b[j - 1]))
    i, j, ops = n, m, []
    while i or j:
        if i and j and D[i][j] == D[i - 1][j - 1] + (a[i - 1] != b[j - 1]):
            ops.append(("=" if a[i - 1] == b[j - 1] else "S", a[i - 1], b[j - 1])); i -= 1; j -= 1
        elif i and D[i][j] == D[i - 1][j] + 1:
            ops.append(("D", a[i - 1], None)); i -= 1
        else:
            ops.append(("I", None, b[j - 1])); j -= 1
    return ops[::-1]


def score(drop_l12):
    a = toks_j(drop_l12)
    b, unsure = toks_b(drop_l12)
    ops = align(a, b)
    c = Counter(o[0] for o in ops)
    n = len(a)
    subs = Counter(f"{x}->{y}" for k, x, y in ops if k == "S")
    return {
        "n_J": n, "n_B": len(b), "B_unsure_tokens": unsure,
        "match": c["="], "sub": c["S"], "ins_in_B": c["I"], "del_from_J": c["D"],
        "sub_rate": round(c["S"] / n, 4), "ins_rate": round(c["I"] / n, 4), "del_rate": round(c["D"] / n, 4),
        "disagreement_rate": round((c["S"] + c["I"] + c["D"]) / n, 4),
        "sub_only_rate_of_aligned": round(c["S"] / (c["S"] + c["="]), 4),
        "top_substitutions": subs.most_common(25),
        "J_types": len(set(a)), "B_types": len(set(b)), "B_labels_not_in_J": sorted(set(b) - set(a)),
    }


def compute():
    return {"inputs_sha1": {p.name: hashlib.sha1(p.read_bytes()).hexdigest() for p in (J, B)},
            "primary_L02_L11": score(True), "all_lines_L02_L12": score(False)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    r = compute()
    if ap.parse_args().check:
        old = json.loads(OUT.read_text())
        if old != json.loads(json.dumps(r)):
            print("STALE: tx_error_no07.json differs from a fresh computation"); sys.exit(1)
        print("ok: tx_error_no07.json current"); return
    OUT.write_text(json.dumps(r, indent=1) + "\n")
    for k in ("primary_L02_L11", "all_lines_L02_L12"):
        print(k, json.dumps({x: v for x, v in r[k].items() if x != "top_substitutions"}))
        print("  top substitutions (J->B):", r[k]["top_substitutions"])


if __name__ == "__main__":
    main()
