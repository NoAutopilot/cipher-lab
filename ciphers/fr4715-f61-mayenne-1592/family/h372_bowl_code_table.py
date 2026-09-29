#!/usr/bin/env python3
"""H372 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026): one table of the H193 bowl answers by leaf and readers' code, for VERIFY-F61-V11
(PROPOSAL_v8_4tri.md), extending H218 (h218_code_sessions_result.txt) with the H359-design calls of 29 Sept: every call here carried H193's 60 f.176v
strips in the same call, and only calls whose gate passed (>= 17/20) are counted. Token level: a token read by two calls counts once, the later
call's answer (H360 after H359, H365 after H362, H371 after H370, H368 after H231); the disagreement count on re-read tokens is reported per leaf.
Sources (items key, reply files): f.124r H359+H360; f.101r H362+H365; f.61 H194 (count-matched design; its result file) and H367; f.106r H231
(rows 1-6) and H368 (rows 1-18); f.97r H370+H371. f.108v (H199, reproduced by H230) and f.176r/v (H193) are carried from h218's table verbatim;
f.101r's period-letter cross-tab from h365's result verbatim. Descriptive; script-only.   python3 h372_bowl_code_table.py [--check]"""
import csv, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def gate(ans):
    ctl = rd(f"{HERE}/h193_items.tsv")
    return sum((ans.get(r["item"]) == "yes") == (r["group"] == "CP") and ans.get(r["item"]) in ("yes", "no") for r in ctl if r["group"] in ("CP", "AN"))
def calls(step, items, replies):
    """(step, chunk, gate, [(line, pos, code, answer)]) per reply file; chunk '' for single-call steps."""
    it = rd(f"{HERE}/{items}"); out = []
    for ch, f in replies:
        if not os.path.exists(f"{P}/{f}"): continue
        ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/{f}")}; g = gate(ans)
        toks = [(r["line"], r["pos"], r["code"], ans.get(r["item"], "missing")) for r in it if r.get("chunk", "") == ch]
        out.append((step, ch, g, toks))
    return out
LEAVES = [
    ("f.124r (de Diou)", calls("H359", "h359_items.tsv", [("", "h359_reply.tsv")]) +
                         calls("H360", "h360_items.tsv", [(f"c{k}", f"h360_reply_c{k}.tsv") for k in range(1, 5)])),
    ("f.101r (de Diou)", calls("H362", "h362_items.tsv", [("", "h362_reply.tsv")]) +
                         calls("H365", "h365_items.tsv", [(f"c{k}", f"h365_reply_c{k}.tsv") for k in range(1, 5)])),
    ("f.97r (de Diou)", calls("H370", "h370_items.tsv", [("", "h370_reply.tsv")]) +
                        calls("H371", "h371_items.tsv", [("c1", "h371_reply_c1.tsv"), ("c2", "h371_reply_c2.tsv")])),
    ("f.106r (secretary)", calls("H231", "h231_items.tsv", [("", "h231_reply.tsv")]) +
                           calls("H368", "h368_items.tsv", [("c1", "h368_reply_c1.tsv"), ("c2", "h368_reply_c2.tsv")])),
    ("f.61 (target, Mayenne's hand)", calls("H367", "h367_items.tsv", [("", "h367_reply.tsv")])),
]
def main():
    out = ["leaf\tcalls (gate/20)\tcode\tbowl yes\tno bowl\tn\tno-share\tre-read tokens (disagree)"]
    for leaf, cs in LEAVES:
        tok = {}; rer = dis = 0
        for step, ch, g, toks in cs:
            if g < 17: continue
            for l, p, c, a in toks:
                if (l, p) in tok and a in ("yes", "no") and tok[(l, p)][1] in ("yes", "no"):
                    rer += 1; dis += a != tok[(l, p)][1]
                tok[(l, p)] = (c, a)
        by = defaultdict(Counter)
        for c, a in tok.values(): by[c][a] += 1
        cl = " ".join(f"{s}{('-' + ch) if ch else ''} {g}" + ("" if g >= 17 else " FAIL") for s, ch, g, _ in cs)
        for c in sorted(by):
            y, n, u = by[c]["yes"], by[c]["no"], by[c]["n"] + by[c]["missing"]
            out.append(f"{leaf}\t{cl}\t{c}\t{y}\t{n}\t{u}\t{n / max(1, y + n):.2f}\t{rer} ({dis})")
    out.append("")
    out.append("f.61, H194 (count-matched sheets, L03/L05/L08/L11; gate 18/20): " + open(f"{HERE}/h194_bowl_f61_result.txt").read().strip().splitlines()[-1])
    out.append("carried verbatim from h218_code_sessions_result.txt (f.108v H199; f.176r/v H193; f.108r H202):")
    out += ["  " + l for l in open(f"{HERE}/h218_code_sessions_result.txt").read().strip().splitlines()
            if l.startswith(("f.108v\tH199", "f.176", "f.108r L02-L03"))]
    out.append("f.101r period letter by bowl (h365 result): " + next(l for l in open(f"{HERE}/h365_101r_4tri_split_result.txt") if l.startswith("period letter")).strip())
    out.append("f.101r " + next(l for l in open(f"{HERE}/h365_101r_4tri_split_result.txt") if l.startswith("bowl-letter agreement")).strip())
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h372_bowl_code_table_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()
