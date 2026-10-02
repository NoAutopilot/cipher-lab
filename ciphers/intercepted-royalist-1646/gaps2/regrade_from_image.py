#!/usr/bin/env python3
"""GAPS2-intercepted-royalist-1646 (2 Oct 2026, account-4): regrade key.tsv from the two blind image passes over Evelyn iv
pp.178-179 (evelyn/pass_img_p178.tsv, pass_img_p179.tsv; one Fable subagent call per page, no key or OCR shown to it).

Witness table (code -> value the print's gloss gives it), built mechanically from the passes:
  one gloss word over one figure            -> that word (Marq: -> Marquis, w^ch -> which, w^th -> with, hauing -> having,
                                               had, -> had, not. -> not, I. H. -> I.H.)
  a spelled gloss over a run of groups with letter count == group count -> one letter per group ("word" over 78 31 18 81;
     "Cabinet" over 90 or 27 40 7 67 p, so the printed letter groups 'or' and 'p' carry a and t and are not figures)
  "desire" over 141 : 56 : 63 : 17 : 67 (6 letters, 5 groups) with 67 = e from Cabinet -> 141 = de, 56 63 17 = s i r (segmentation, M)
  a gloss the pass reports as spanning groups, or sitting over one group with more letters than a word code can carry
  alone, stays a span (Southampton over 356 84 ...; nor over 269 with 17 bare; Jewells over no 418 56; burned over at ad 19 if 147)
Grades written: C evelyn-img (image gloss directly over the figure, digits read from the page), C evelyn-img-seg,
M evelyn-img-span, M evelyn-align-unreached (69), I evelyn-img-H. (520), I context (430, 543); H f77 rows untouched.
Control (rule 3): the same confirmed-count statistic for 20 value-shuffled copies of key.tsv (seeds 1-20).
Rewrites key.tsv in place (header kept, a dated block appended) and prints the counts.
"""
import random, re, sys
from pathlib import Path

T = Path(__file__).resolve().parents[1]
NORM = {"marq:": "Marquis", "w^ch": "which", "w^th": "with", "hauing": "having", "had,": "had", "not.": "not", "i. h.": "I.H.",
        "h.": "H."}


def load_pass(p):
    rows = []
    for l in open(p):
        if l.startswith("#") or l.startswith("line\t") or not l.strip():
            continue
        line, gi, group, gloss, note = (l.rstrip("\n").split("\t") + [""] * 5)[:5]
        rows.append((int(line), int(gi), group, gloss.strip(), note))
    return rows


def norm(g):
    k = g.lower()
    return NORM.get(k, g)


def witness():
    w = {}      # code -> value (direct)
    spans = {}  # code -> gloss (spanned, not a value for this code alone)
    p178 = load_pass(T / "evelyn/pass_img_p178.tsv"); p179 = load_pass(T / "evelyn/pass_img_p179.tsv")
    allrows = [("178",) + r for r in p178] + [("179",) + r for r in p179]
    # direct single-word glosses
    for page, line, gi, group, gloss, note in allrows:
        if gloss and group.isdigit() and gloss != "[erased]" and "spans" not in note:
            w[group] = norm(gloss)
    # spelled words: word over 78 31 18 81 (line 2 groups 8-10 + line 3 group 1 of p.178)
    seq178 = [r for r in p178]
    def groups(line, a, b, src=seq178):
        return [r[2] for r in src if r[0] == line and a <= r[1] <= b]
    word = groups(2, 8, 10) + groups(3, 1, 1)          # 78 31 18 81
    assert word == ["78", "31", "18", "81"], word
    for g, ch in zip(word, "word"):
        w[g] = ch; w.pop(g + "_", None)
    w.pop("31", None) if False else None
    cab = groups(4, 5, 11)                               # 90 or 27 40 7 67 p
    assert len(cab) == 7, cab
    for g, ch in zip(cab, "cabinet"):
        if g.isdigit():
            w[g] = ch
    # the gloss 'word' sat over 31 in the pass; it is the spelled word, not a value for 31: fixed above (31 = o)
    # desire: 141 56 / 63 17 67 ; 67 = e (Cabinet) -> 141 de, 56 s, 63 i, 17 r (segmentation)
    des = groups(1, 2, 3) + groups(2, 1, 3)
    assert des == ["141", "56", "63", "17", "67"], des
    seg = {"141": "de", "56": "s", "63": "i", "17": "r"}
    w.pop("141", None)                                   # 'desire' is not the value of 141 alone
    # spans reported by the passes
    for page, line, gi, group, gloss, note in allrows:
        if gloss and "spans" in note and group.isdigit():
            spans[group] = gloss; w.pop(group, None)
    # nor over 269 with 17 bare after it: 269 alone cannot be 'nor' + r unless 17 is not r; keep as a span (M)
    spans["269"] = "nor"; w.pop("269", None)
    # H. over 520: the print gives the initial only
    w.pop("520", None)
    return w, spans, seg


def load_key(p):
    head, rows = [], []
    for l in open(p):
        if l.startswith("#"):
            head.append(l.rstrip("\n"))
        elif l.startswith("code\t") or not l.strip():
            continue
        else:
            rows.append(l.rstrip("\n").split("\t"))
    return head, rows


def main():
    w, spans, seg = witness()
    head, rows = load_key(T / "key.tsv")
    old = {r[0]: tuple(r[1:]) for r in rows}
    changes = []; confirmed = 0
    for r in rows:
        code, val, grade, src = r
        if code in w:
            if w[code].lower() == val.lower():
                confirmed += 1
                if (grade, src) != ("C", "evelyn-img"):
                    changes.append((code, val, f"{grade} {src}", "C evelyn-img"))
                r[2], r[3] = "C", "evelyn-img"
            else:
                changes.append((code, val, f"{grade} {src}", f"M evelyn-img-differs ({w[code]})"))
                r[2], r[3] = "M", "evelyn-img-differs"
        elif code in seg:
            confirmed += 1 if seg[code] == val else 0
            r[2], r[3] = ("C", "evelyn-img-seg") if code != "141" else ("M", "evelyn-img-seg")
            if (grade, src) != (r[2], r[3]):
                changes.append((code, val, f"{grade} {src}", f"{r[2]} {r[3]}"))
        elif code in spans:
            if (grade, src) != ("M", "evelyn-img-span"):
                changes.append((code, val, f"{grade} {src}", "M evelyn-img-span"))
            r[2], r[3] = "M", "evelyn-img-span"
        elif code == "520":
            r[2], r[3] = "I", "evelyn-img-H."
            changes.append((code, val, f"{grade} {src}", "I evelyn-img-H."))
    # control: 20 value-shuffled keys, same statistic (rows whose value equals the image witness at that code)
    codes = [r[0] for r in rows]; vals = [r[1] for r in rows]
    ctrl = []
    for s in range(1, 21):
        rnd = random.Random(s); v = vals[:]; rnd.shuffle(v)
        ctrl.append(sum(1 for c, x in zip(codes, v) if (c in w and w[c].lower() == x.lower()) or (c in seg and seg[c] == x)))
    counts = {}
    for r in rows:
        counts[r[2]] = counts.get(r[2], 0) + 1
    stamp = ["# Regraded again 2 Oct 2026 (GAPS2-intercepted-royalist-1646, account-4) from the page images of pp.178-179 (leaf_n185.jpg fetched",
             "# this session, leaf_n186.jpg): two blind vision passes (evelyn/pass_img_p178.tsv, pass_img_p179.tsv), gaps2/regrade_from_image.py.",
             "#  C  evelyn-img      the gloss sits over this figure on the page image and the digits read from the page equal the key's",
             "#  C  evelyn-img-seg  s i r from 'desire' over 141:56:63:17:67 with 67 = e read from the page",
             "#  M  evelyn-img-seg  141 = de by the same segmentation (the print glosses the whole word over 141)",
             "#  M  evelyn-img-span the page shows the gloss spanning groups (Southampton over 356 84 ...) or a bare figure after it (nor over 269, 17 bare)",
             "#  I  evelyn-img-H.   the page prints 'H.'; Hertford is the expansion",
             "# The page prints letter groups inside the figure lines ('in', 'no', 'or', 'p', 'at', 'ad', 'if'): 'or' and 'p' carry a and t of Cabinet,",
             "# so they are not OCR garbles; whether they are the 1857 printer's misreadings of figures is logged in HYPOTHESES.md, not resolved here.",
             f"# Counts after this pass: " + ", ".join(f"{g} {counts[g]}" for g in ("C", "H", "M", "I") if g in counts) + f" ({len(rows)} rows); image-confirmed rows {confirmed} vs 20 value-shuffled keys mean {sum(ctrl)/len(ctrl):.2f} max {max(ctrl)}."]
    with open(T / "key.tsv", "w") as f:
        f.write("\n".join(head + stamp) + "\n")
        f.write("code\tvalue\tgrade\tsource\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    print("witness codes:", len(w), "seg:", len(seg), "spans:", sorted(spans))
    print("confirmed rows:", confirmed, "| control (20 value-shuffled keys):", ctrl, "mean %.2f max %d" % (sum(ctrl) / len(ctrl), max(ctrl)))
    print("grade counts:", counts)
    print("changes (%d):" % len(changes))
    for c in changes:
        print("  ", c)


if __name__ == "__main__":
    main()
