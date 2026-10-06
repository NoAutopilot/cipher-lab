#!/usr/bin/env python3
"""R9526 retest (R14-RJM9526, 6 Oct 2026): test147.py's run() unchanged, with the two input changes fixed in
witness/PREREG_f147b.md (pushed 8aeea08d0 before any read or scoring):
  1. gloss: the f.150 clerk's own text (passes/f150_clerk.tsv, one Sonnet read) from "Los de genova" to the end of its crop L07,
     joined to the CODOIN XXVI print (passes/gloss_codoin26_p49.tsv) after the print's counterpart of the clerk's last word;
  2. splits: lookalike/f147_passD.tsv (tools/lookalike_pass.py reconcile on scripts/lookalike_tiles147.py's 85 tiles) -- a split '~'
     settled 2-of-3 takes the settled label; unsettled stays '~'.
GATED run = both changes, primary span (lines 2-18). Reported only: baseline (must equal results_test147.json), gloss only,
splits only, and the sensitivity span of the gated run.

  python3 scripts/test147b.py [--check] [--shuffles 200]   writes results_test147b.json, ciphertext_f147_reconciled_la.tsv,
                                                           passes/gloss_f147b.tsv, passes/align_f147b.tsv
"""
import argparse, csv, importlib.util, json, re, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
_s = importlib.util.spec_from_file_location("t147", HERE / "scripts/test147.py")
t147 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(t147)
t1 = t147.t1


def fold(w):
    return "".join(c for c in unicodedata.normalize("NFD", w.lower()) if c.isalpha())


NUM = {"2": "dos", "ij": "dos", "ii": "dos", "ijo": "dos"}


def clerk_words():
    words = []
    with open(HERE / "passes/f150_clerk.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            words += r["text"].split()
    if "//" in words:
        words = words[words.index("//") + 1:]
    else:
        words = words[[fold(w) for w in words].index("los"):]
    out, i = [], 0
    while i < len(words):
        w = words[i]
        i += 1
        if w in ("/", "//") or w.startswith("[?"):
            continue
        w = w.rstrip("?")
        fw = fold(w)
        if not fw and w.strip("/") == "":
            continue
        if fw in ("q", "qe") or w in ("q~", "q̃"):
            out.append("que"); continue
        if fw == "v" and i < len(words) and fold(words[i]) in ("md", "mt", "m"):
            out.append("V. M."); i += 1; continue
        if fw in ("vmd", "vm"):
            out.append("V. M."); continue
        if fw in ("s", "sd") and w.endswith("."):
            out.append("santidad"); continue
        if w.lower() in NUM:
            out.append(NUM[w.lower()]); continue
        if fw:
            out.append(w.strip("/"))
    return out


def gloss_b():
    with open(HERE / "passes/gloss_codoin26_p49.tsv", encoding="utf-8") as f:
        pw = " ".join(r["text"] for r in csv.DictReader(f, delimiter="\t")).split()
    fp = [fold(w) for w in pw]
    cw = clerk_words()
    v = fp.index("venir")
    last = fold(cw[-1])
    join = next((j for j in range(v, min(v + 7, len(fp))) if fp[j] == last), None)
    rule = "last clerk word '%s' = print word %d" % (last, join) if join is not None else None
    if join is None:
        join = fp.index("seguridad")
        rule = "fallback at print 'seguridad' (word %d)" % join
    return cw, pw[join + 1:], rule


def apply_passd(rec):
    pd = {}
    with open(HERE / "lookalike/f147_passD.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            pd[(r["passage"], int(r["pos"]))] = r
    out, n_set = {}, 0
    for n, line in rec.items():
        new = []
        for j, (t, st) in enumerate(line):
            r = pd[("f147_L%02d" % n, j + 1)]
            if r["sign_id"] != t:
                if t != "~":
                    sys.exit("unexpected passD change at L%02d.%d" % (n, j + 1))
                if r["sign_id"] not in ("~", ""):
                    t, st = r["sign_id"], "lookalike"
                    n_set += 1
            new.append((t, st))
        out[n] = new
    return out, n_set


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--shuffles", type=int, default=200)
    a = ap.parse_args()
    key = t1.load_key()
    A, B = t147.load("A"), t147.load("B")
    rec, err, agree, tot = t1.reconcile(A, B, key)
    rec_la, n_set = apply_passd(rec)
    with open(HERE / "passes/gloss_codoin26_p49.tsv", encoding="utf-8") as f:
        g0 = " ".join(r["text"] for r in csv.DictReader(f, delimiter="\t"))
    cw, tail, rule = gloss_b()
    g1 = " ".join(cw + tail)
    prim = lambda r: {n: v for n, v in r.items() if n >= 2}
    out = {"err_2reader": round(err, 4), "splits_settled_applied": n_set,
           "tilde_left": sum(1 for l in rec_la.values() for t, _ in l if t == "~"),
           "gloss": {"clerk_words": len(cw), "join": rule, "print_words_after_join": len(tail)}}
    out["baseline_reported"], _ = t147.run(prim(rec), g0, key, 0)
    out["gloss_only_reported"], _ = t147.run(prim(rec), g1, key, 0)
    out["splits_only_reported"], _ = t147.run(prim(rec_la), g0, key, 0)
    for k in ("baseline_reported", "gloss_only_reported", "splits_only_reported"):
        out[k].pop("keys", None)
    out["GATED_both_primary_lines_2_18"], al = t147.run(prim(rec_la), g1, key, a.shuffles)
    sens = prim(rec_la)
    bs = [j for j, (t, s) in enumerate(rec_la[1]) if t == "B"]
    if bs:
        sens[1] = rec_la[1][bs[-1] + 1:]
    out["sensitivity_line1_tail"], _ = t147.run(sens, g1, key, a.shuffles)
    oj = json.dumps(out, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    rc = "line\ttokens\n" + "".join("%d\t%s\n" % (n, " ".join(t for t, _ in rec_la[n])) for n in sorted(rec_la))
    gl = "part\ttext\n" + "clerk_f150\t%s\nprint_tail\t%s\n" % (" ".join(cw), " ".join(tail))
    als = "i\tline\tkind\ttoken\tchunk\n" + "".join("%d\t%d\t%s\t%s\t%s\n" % r for r in al)
    outs = {"results_test147b.json": oj, "ciphertext_f147_reconciled_la.tsv": rc, "passes/gloss_f147b.tsv": gl,
            "passes/align_f147b.tsv": als}
    if a.check:
        ok = all((HERE / p).exists() and (HERE / p).read_text() == s for p, s in outs.items())
        print("up to date" if ok else "STALE")
        sys.exit(0 if ok else 1)
    for p, s in outs.items():
        (HERE / p).write_text(s)
    print(oj)


if __name__ == "__main__":
    main()
