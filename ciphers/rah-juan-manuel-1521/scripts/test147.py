#!/usr/bin/env python3
"""Second held-out test of both letter alphabets: R9526 (Juan Manuel to Charles V, Rome, 6 Jun 1522, BRAH 9/24 ff.147-148)
against the printed chapter in CODOIN XXVI núm. 36 pp.49-50 (R12-RJM147, 6 Oct 2026).

Pre-registration: witness/PREREG_f147.md (committed and pushed before this script was first run on the passes).
Reuses scripts/test42.py (score, keys) and scripts/test1.py (tokens, reconcile, to_pair) unchanged; only the inputs differ:
passes/f147_A.tsv, passes/f147_B.tsv (two blind Sonnet passes; line 1 = f.147 crop L07, 2-3 = f.147 L08-L09, 4-18 = f.147v
L01-L15), passes/gloss_codoin26_p49.tsv (the print). Primary span lines 2-18 (gated); sensitivity span = line 1 after its last
B token + lines 2-18 (reported only).

  python3 scripts/test147.py [--check] [--shuffles 200]      writes results_test147.json; --check exits 1 if stale
"""
import argparse, csv, importlib.util, json, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("t42", HERE / "scripts/test42.py")
t42 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t42)
t1, ia = t42.t1, t42.ia

# pass-local ?n -> shared label, from each pass's own notes only (PREREG_f147.md addendum)
NORM147 = {"A": {}, "B": {"?1": "7"}}


def load(p):
    t1.NORM[("f147", p)] = NORM147[p]
    rows = {}
    with open(HERE / "passes" / f"f147_{p}.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            rows[int(r["line"])] = t1.tokens(r.get("tokens", ""), "f147", p)
    return rows


def run(rec, gloss, key, shuffles):
    raw, kinds, lines = [], [], []
    for n in sorted(rec):
        r, k = t1.to_pair(rec[n], key)
        raw += r; kinds += k; lines += [n] * len(r)
    c = 0
    for i, t in enumerate(raw):
        if t == "@~":
            c += 1
            raw[i] = "@~%d" % c
    ia.WORD_PFX = "%"
    ia.CODE_CHUNK = 2
    pair = {"plain_line": "1", "plain_raw": gloss, "cipher_line": "1", "cipher_raw": " ".join(raw)}
    prepared, results, counts, shown = ia.run_align([pair], floor=0, clear_consumes=True, code_prefix="@",
                                                    null_cost=-1.0, max_chunk=10)
    letters = prepared[0][3]
    offs = [cc for cc in results[0]]
    chunks = [letters[x[0]:x[1]] if x else "" for x in offs]
    code_n = sum(1 for k in kinds if k == "code")
    code_hit = sum(1 for t, k, ch in zip(raw, kinds, chunks) if k == "code" and ia.fold(ch) == ia.fold(t))
    res = {"gloss_letters": len(letters),
           "calibration": {"code_words": code_n, "code_words_matched": code_hit,
                           "share": round(code_hit / code_n, 4) if code_n else None, "gate": t42.CAL_GATE,
                           "verdict": "PASS" if code_n and code_hit / code_n >= t42.CAL_GATE else "FAIL"}}
    sym = [i for i, k in enumerate(kinds) if k == "sym"]
    res["symbol_tokens"] = {"scored": len(sym), "labels": dict(Counter(raw[i][1:] for i in sym))}
    if res["calibration"]["verdict"] == "PASS":
        res["keys"] = {name: {"values": vals, "heldout": t42.score(sym, raw, chunks, vals, shuffles)}
                       for name, vals in t42.keys().items()}
    else:
        res["keys"] = "not scored: calibration gate FAIL (non-test at this alignment)"
    al = [(i, lines[i], kinds[i], raw[i], chunks[i]) for i in range(len(raw))]
    return res, al


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--shuffles", type=int, default=200)
    a = ap.parse_args()
    key = t1.load_key()
    A, B = load("A"), load("B")
    clear = set()  # no clear-line drop: the print carries the clear passages (PREREG_f147.md addendum 1)
    rec, err, agree, tot = t1.reconcile(A, B, key)
    out = {"err_2reader": round(err, 4), "agree_tokens": agree, "max_tokens": tot, "lines": len(rec),
           "clear_lines_dropped": sorted(clear),
           "symbols_agreed": sum(1 for l in rec.values() for t, s in l if s == "agree" and t1.SYMBOL.match(t)),
           "symbols_split": sum(1 for l in rec.values() for t, s in l if s == "split")}
    with open(HERE / "passes/gloss_codoin26_p49.tsv", encoding="utf-8") as f:
        gloss = " ".join(r["text"] for r in csv.DictReader(f, delimiter="\t"))
    prim = {n: v for n, v in rec.items() if n >= 2}
    out["primary_lines_2_18"], al = run(prim, gloss, key, a.shuffles)
    sens = dict(prim)
    if 1 in rec:
        l1 = rec[1]
        bs = [j for j, (t, s) in enumerate(l1) if t == "B"]
        out["line1_last_B_index"] = bs[-1] if bs else None
        if bs:
            sens[1] = l1[bs[-1] + 1:]
    out["sensitivity_line1_tail"], _ = run(sens, gloss, key, a.shuffles)
    out_json = json.dumps(out, indent=1, sort_keys=True) + "\n"
    rc = "line\ttokens\n" + "".join("%d\t%s\n" % (n, " ".join(t for t, _ in rec[n])) for n in sorted(rec))
    als = "i\tline\tkind\ttoken\tchunk\n" + "".join("%d\t%d\t%s\t%s\t%s\n" % r for r in al)
    outs = {"results_test147.json": out_json, "ciphertext_f147_reconciled.tsv": rc, "passes/align_f147_codoin.tsv": als}
    if a.check:
        ok = all((HERE / p).exists() and (HERE / p).read_text() == s for p, s in outs.items())
        print("up to date" if ok else "STALE")
        sys.exit(0 if ok else 1)
    for p, s in outs.items():
        (HERE / p).write_text(s)
    print(out_json)


if __name__ == "__main__":
    main()
