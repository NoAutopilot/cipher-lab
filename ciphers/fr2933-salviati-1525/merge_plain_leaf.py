#!/usr/bin/env python3
"""Merge two blind plain-box passes and a settlement into the leaf's reconciled table (SALV-57V, 13 Oct 2026).

  python3 merge_plain_leaf.py f57v [--check]

Reads plain_passA_<leaf>.tsv, plain_passB_<leaf>.tsv (line, pos, word, expanded, conf) and
recon_plain_<leaf>/settled.tsv (line, pos, word, expanded, grade; one row per disagreement from
recon_plain_diff.py). Writes:
  plain_<leaf>.tsv   line, pos, word, expanded, grade  (A = passes agree after case/whitespace
                     normalisation, as recon_plain_diff.py; R/M from settled.tsv) -- the folder's format
  <leaf>_plain.tsv   line, box, A_word, A_conf, B_word, B_conf, text, grade  (per-pass + reconciled)
and replaces the <leaf> rows of plain_boxes.tsv (leaf, line, pos, word, expanded, grade).
--check regenerates in memory and exits 1 if any committed file differs (rule 7).
"""
import csv, io, os, sys

D = os.path.dirname(os.path.abspath(__file__))


def load(path):
    return {(int(r["line"]), r["pos"]): r for r in csv.DictReader(open(path, encoding="utf-8"), delimiter="\t")}


def norm(w):
    return " ".join((w or "").lower().split())


def tsv(header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, delimiter="\t", lineterminator="\n")
    w.writerow(header)
    w.writerows(rows)
    return buf.getvalue()


def build(leaf):
    a = load(os.path.join(D, f"plain_passA_{leaf}.tsv"))
    b = load(os.path.join(D, f"plain_passB_{leaf}.tsv"))
    s = load(os.path.join(D, f"recon_plain_{leaf}", "settled.tsv"))
    if set(a) != set(b):
        sys.exit(f"pass A and pass B pos lists differ: {sorted(set(a) ^ set(b))}")
    keys = sorted(a, key=lambda k: (k[0], float(k[1])))
    plain, perpass = [], []
    for k in keys:
        ra, rb = a[k], b[k]
        if norm(ra["word"]) == norm(rb["word"]):
            word, exp, grade = ra["word"], ra.get("expanded") or rb.get("expanded") or "", "A"
        else:
            if k not in s:
                sys.exit(f"disagreement {k} has no settled row")
            word, exp, grade = s[k]["word"], s[k].get("expanded", ""), s[k]["grade"]
        plain.append([k[0], k[1], word, exp, grade])
        perpass.append([k[0], k[1], ra["word"], ra.get("conf", ""), rb["word"], rb.get("conf", ""), word, grade])
    out = {
        f"plain_{leaf}.tsv": tsv(["line", "pos", "word", "expanded", "grade"], plain),
        f"{leaf}_plain.tsv": tsv(["line", "box", "A_word", "A_conf", "B_word", "B_conf", "text", "grade"], perpass),
    }
    # plain_boxes.tsv: keep other leaves' rows verbatim, replace this leaf's
    # (byte for byte: the file mixes CRLF and LF rows, so lines keep their own endings)
    pb = open(os.path.join(D, "plain_boxes.tsv"), encoding="utf-8", newline="").read().splitlines(keepends=True)
    kept = [ln for ln in pb if not ln.startswith(leaf + "\t")]
    if kept and not kept[-1].endswith("\n"):
        kept[-1] += "\n"
    new = ["\t".join([leaf] + [str(c) for c in r]) + "\n" for r in plain]
    out["plain_boxes.tsv"] = "".join(kept + new)
    return out


def main():
    if len(sys.argv) < 2 or sys.argv[1].startswith("-"):
        print(__doc__); return 0
    leaf = sys.argv[1]
    out = build(leaf)
    if "--check" in sys.argv:
        stale = [n for n, t in out.items() if open(os.path.join(D, n), encoding="utf-8", newline="").read() != t]
        if stale:
            print("STALE: " + ", ".join(stale)); return 1
        print(f"ok: {leaf} plain tables current"); return 0
    for n, t in out.items():
        open(os.path.join(D, n), "w", encoding="utf-8", newline="").write(t)
    print(f"wrote {', '.join(out)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
