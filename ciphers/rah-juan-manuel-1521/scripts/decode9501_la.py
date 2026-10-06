#!/usr/bin/env python3
"""R9501 f.34 trial decode rerun after the look-alike pass (R13-RJM34LA, 6 Oct 2026; lookalike/PREREG_f34.md).

Re-uses scripts/decode9501.py unchanged (reconcile, decode_tok, render, key) and folds in lookalike/f34_passD.tsv
(tools/lookalike_pass.py reconcile on lookalike/f34_tiles.tsv): a split '~' token whose tile settled at 2-of-3 takes the
settled label, as a third reader. Its grade follows R12-RJMV's licence for a one-reader token: a table code M, a valued
symbol M (never S -- S needs both blind readers to agree), an unvalued symbol or an out-of-table group U. Every other token
keeps decode9501.py's grade. The 'oot' tiles (agreed out-of-table groups) are never overturned (2-of-3), so they change nothing.

Outputs (decode9501.py's own outputs are left as they are):
  ciphertext_f34_reconciled_la.tsv, grades_f34_tomokiyo_la.tsv, reading_f34_tomokiyo_la.txt, results_decode9501_la.json
  --judge also scores the reading and its shuffled-order control (seeds 1-20, random.Random(seed) on the token list as
  scripts/shuffle_spread9501.py does) with tools/judge_plaintext.py on es1600 and es17c -> results_shuffle_spread9501_la.json (~3 min)

  python3 ciphers/rah-juan-manuel-1521/scripts/decode9501_la.py [--judge] [--check]
"""
import argparse, csv, importlib.util, json, random, re, statistics, subprocess, sys, tempfile
from collections import Counter
from pathlib import Path

H = Path(__file__).resolve().parent.parent
ROOT = H.parent.parent
sp = importlib.util.spec_from_file_location("d", H / "scripts/decode9501.py")
d = importlib.util.module_from_spec(sp)
sp.loader.exec_module(d)
SEEDS = range(1, 21)


def passd():
    out = {}
    with open(H / "lookalike/f34_passD.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            out[(r["passage"], int(r["pos"]))] = r
    return out


def build():
    key, alp = d.t1.load_key(), d.alpha()
    rec, *_ = d.t1.reconcile(d.load("A"), d.load("B"), key)
    pd = passd()
    grades, lines, flat, before = [], [], [], Counter()
    for n in sorted(rec):
        toks = []
        for j, (t, st) in enumerate(rec[n]):
            v, g, kind = d.decode_tok(t, st, key, alp)
            before[g] += 1
            r = pd[("f34_L%02d" % n, j + 1)]
            if r["sign_id"] != t:
                if t != "~" or r["note"] != "lookalike 2-of-3":
                    sys.exit("unexpected passD change at L%02d.%d" % (n, j + 1))
                t, st = r["sign_id"], "lookalike"
                v, g, kind = d.decode_tok(t, "split-code", key, alp)   # one-reader grading: never S
            grades.append((n, j + 1, t, st, kind, v, g))
            toks.append((v, kind))
            flat.append((t, st))
        lines.append((n, toks))
    return key, alp, grades, lines, flat, before


def judge(spec, f):
    o = subprocess.run([sys.executable, str(ROOT / "tools/judge_plaintext.py"), str(spec), "--file", str(f)],
                       capture_output=True, text=True, cwd=ROOT).stdout
    m = re.search(r"(PASS|FAIL) language: score=(-?[\d.]+), null_p99=(-?[\d.]+), real_p05=(-?[\d.]+)", o)
    return {"verdict": m.group(1), "score": float(m.group(2)), "null_p99": float(m.group(3)), "real_p05": float(m.group(4))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--judge", action="store_true")
    a = ap.parse_args()
    key, alp, grades, lines, flat, before = build()
    gc = Counter(g for *_, g in grades)
    la = [x for x in grades if x[3] == "lookalike"]
    res = {"tokens": len(grades), "grades_before": dict(sorted(before.items())), "grades_after": dict(sorted(gc.items())),
           "lookalike_settled": len(la), "lookalike_by_kind_grade": dict(sorted(Counter("%s/%s" % (k, g) for *_, k, v, g in la).items())),
           "lookalike_labels": dict(sorted(Counter(t for _, _, t, *_ in la).items())),
           "split_left": sum(1 for x in grades if x[2] == "~"),
           "key_source": "published (Tomokiyo, Cryptiana: JuanManuel.png alphabet; AlonsoSanchez.htm nomenclator)"}
    outs = {
        "results_decode9501_la.json": json.dumps(res, indent=1, sort_keys=True) + "\n",
        "ciphertext_f34_reconciled_la.tsv": "line\ttokens\n" + "".join(
            "%d\t%s\n" % (n, " ".join(g[2] for g in grades if g[0] == n)) for n, _ in lines),
        "grades_f34_tomokiyo_la.tsv": "line\tpos\ttoken\treaders\tkind\tvalue\tgrade\n" + "".join(
            "%d\t%d\t%s\t%s\t%s\t%s\t%s\n" % g for g in grades),
        "reading_f34_tomokiyo_la.txt": ("# R9501 f.34 trial decode after the look-alike pass (R13-RJM34LA), key published (Tomokiyo), "
                                        "grades in grades_f34_tomokiyo_la.tsv; '_' = unread; letter runs joined, word breaks not marked\n"
                                        + "".join("%d\t%s\n" % (n, d.render(t)) for n, t in lines)),
    }
    if a.judge:
        tmp = Path(tempfile.mkdtemp())
        spec = json.load(open(ROOT / "specs/rah-juan-manuel-1521.json"))
        spec["judge"]["language"] = "es1600"
        (tmp / "s.json").write_text(json.dumps(spec))
        specs = {"es1600": tmp / "s.json", "es17c": ROOT / "specs/rah-juan-manuel-1521.json"}
        tgt = tmp / "t.txt"
        tgt.write_text("".join(d.render(t) + "\n" for _, t in lines))
        jr = {"seeds": list(SEEDS), "target": {k: judge(s, tgt) for k, s in specs.items()}, "shuffled": {k: [] for k in specs}}
        for seed in SEEDS:
            sh = flat[:]
            random.Random(seed).shuffle(sh)
            f = tmp / ("s%02d.txt" % seed)
            f.write_text(d.render([(d.decode_tok(t, "split-code" if st == "lookalike" else st, key, alp)[0],
                                    d.decode_tok(t, "split-code" if st == "lookalike" else st, key, alp)[2]) for t, st in sh]) + "\n")
            for k, s in specs.items():
                jr["shuffled"][k].append(judge(s, f)["score"])
        for k, v in jr["shuffled"].items():
            t = jr["target"][k]["score"]
            jr.setdefault("summary", {})[k] = {"min": min(v), "mean": round(statistics.mean(v), 4), "max": max(v),
                                               "sd": round(statistics.stdev(v), 4), "target": t, "target_above_all": t > max(v)}
        outs["results_shuffle_spread9501_la.json"] = json.dumps(jr, indent=1, sort_keys=True) + "\n"
    if a.check:
        ok = all((H / p).exists() and (H / p).read_text() == s for p, s in outs.items())
        print("up to date" if ok else "STALE")
        sys.exit(0 if ok else 1)
    for p, s in outs.items():
        (H / p).write_text(s)
    print(json.dumps(res, indent=1, sort_keys=True))
    if a.judge:
        print(json.dumps(jr["target"], indent=1), json.dumps(jr["summary"], indent=1))


if __name__ == "__main__":
    main()
