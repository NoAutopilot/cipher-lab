#!/usr/bin/env python3
"""AX-NAMES: build names.tsv (codes > 120 of Lodewijk's 1574 table) from the alignment occurrences
(axnames/occ_<letter>.tsv, written by align_names.py) and the hand-read attestations
(axnames/attest_manual.tsv: period glosses and Groen-printed names at 5797's own clusters).

Occurrence rules (scripted, no eye):
  * adjacent codes > 120 form one cluster; a cluster counts only if >= 3 exact letter matches sit on
    each side within 6 units (anchors) and it absorbs <= 16 printed letters (longer = a transcription gap);
  * a cluster absorbing nothing is one NULL observation for each of its codes;
  * a code is NULL when it has >= 2 NULL observations and they are >= 75% of its observations;
  * a non-empty cluster whose codes, minus the NULL codes, leave exactly one code gives that code a
    word observation (the absorbed letters).
Grades: C when >= 2 independent observations agree, or one bounded observation (anchors >= 5 on both
sides, or a manual row marked bounded=yes); M otherwise, and M with both values when observations
disagree (the majority value is listed first).

Usage: python3 axnames/build_names.py [--exclude LETTER] [--out PATH] [--check]
"""
import argparse, collections, csv, glob, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ONLY = set()
T = os.path.dirname(HERE)


def load_occ(exclude):
    occ = []
    for f in sorted(glob.glob(os.path.join(HERE, "occ_*.tsv"))):
        for r in csv.DictReader(open(f), delimiter="\t"):
            if r["letter"] in exclude:
                continue
            r["unit"] = int(r["unit"]); r["left_anchor"] = int(r["left_anchor"]); r["right_anchor"] = int(r["right_anchor"])
            occ.append(r)
    return occ


def clusters(occ):
    out, cur = [], []
    for r in occ:
        if cur and (r["letter"], r["page"]) == (cur[-1]["letter"], cur[-1]["page"]) and r["unit"] == cur[-1]["unit"] + 1:
            cur.append(r)
        else:
            if cur:
                out.append(cur)
            cur = [r]
    if cur:
        out.append(cur)
    return out


def build(exclude=(), manual=True):
    # "sib" (4613/4615, key.tsv's own source pair) is the aligner's known-answer control, never a names.tsv source
    occ = load_occ(set(exclude) | ({"sib"} if "sib" not in ONLY else set()))
    obs = collections.defaultdict(list)  # code -> [(value, letter, where, bounded)]
    cls = []
    for cl in clusters(occ):
        s = "".join(r["absorbed"] for r in cl)
        la, ra = cl[0]["left_anchor"], cl[-1]["right_anchor"]
        if la < 3 or ra < 3 or len(s) > 16:
            continue
        cls.append((cl, s, la, ra))
    for cl, s, la, ra in cls:
        if s == "":
            for r in cl:
                obs[r["code"]].append(("NULL", r["letter"], f'{r["line"]}:{r["pos"]}', la >= 5 and ra >= 5))
    nulls = {c for c, v in obs.items()
             if sum(1 for o in v if o[0] == "NULL") >= 2 and sum(1 for o in v if o[0] == "NULL") >= 0.75 * len(v)}
    for cl, s, la, ra in cls:
        if s == "":
            continue
        cand = [r for r in cl if r["code"] not in nulls]
        if len(cand) == 1:
            r = cand[0]
            obs[r["code"]].append((s, r["letter"], f'{r["line"]}:{r["pos"]}', la >= 5 and ra >= 5))
    # recompute nulls with word observations included
    unprinted = collections.defaultdict(list)
    if manual:
        for r in csv.DictReader(open(os.path.join(HERE, "attest_manual.tsv")), delimiter="\t"):
            if r["letter"] in exclude:
                continue
            if r["value"] == "UNPRINTED":
                unprinted[r["code"]].append(f'{r["letter"]} {r["where"]}')
                continue
            obs[r["code"]].append((r["value"], r["letter"], r["where"], r["bounded"] == "yes"))
    # a position where Groen printed no word for the code is not a NULL observation
    for c, locs in unprinted.items():
        obs[c] = [o for o in obs.get(c, []) if not (o[0] == "NULL" and any(o[2].split(" ")[0] in l for l in locs))]
    for c in list(obs):
        if not (c.isdigit() and 121 <= int(c) <= 400):
            del obs[c]  # 0, 707 (split misreadings), 1574 (a date): not table codes
    rows = []
    for c in sorted(obs, key=int):
        v = obs[c]
        if not v:
            continue
        cnt = collections.Counter(o[0] for o in v)
        top, n = cnt.most_common(1)[0]
        agree = [o for o in v if o[0] == top]
        letters_ = sorted({o[1] for o in agree})
        if len(cnt) > 1 and n < 0.75 * len(v):
            grade = "M"
            value = " | ".join(f"{k} ({m})" for k, m in cnt.most_common())
        else:
            value = top
            grade = "C" if (n >= 2 or any(o[3] for o in agree)) else "M"
            if top == "NULL" and n < 2:
                grade = "M"
        where = "; ".join(f"{o[1]} {o[2]}" for o in agree[:8]) + (" ..." if len(agree) > 8 else "")
        note = "" if len(cnt) == 1 else "other observations: " + ", ".join(f"{k} x{m}" for k, m in cnt.items() if k != top)
        rows.append([c, value, ",".join(letters_), where, len(v), n, grade, note])
    for c, locs in unprinted.items():
        if c not in obs or not obs[c]:
            rows.append([c, "? (Groen prints no word here)", ",".join(sorted({l.split()[0] for l in locs})), "; ".join(locs), 0, 0, "U", "unread name code: Groen's print leaves the subject out"])
    rows.sort(key=lambda r: int(r[0]))
    return rows


HDR = ["code", "value", "letters", "where (first 8 agreeing)", "observations", "agreeing", "grade", "note"]


def write(rows, path):
    import io
    buf = io.StringIO()
    w = csv.writer(buf, delimiter="\t", lineterminator="\n")
    w.writerow(HDR); w.writerows(rows)
    return buf.getvalue()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--exclude", action="append", default=[])
    ap.add_argument("--out", default=os.path.join(T, "names.tsv"))
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    text = write(build(a.exclude), a.out)
    if a.check:
        if open(a.out).read() != text:
            print("names.tsv is stale", file=sys.stderr); sys.exit(1)
        print("names.tsv up to date"); return
    open(a.out, "w").write(text)


if __name__ == "__main__":
    main()
