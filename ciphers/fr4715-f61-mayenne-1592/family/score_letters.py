#!/usr/bin/env python3
"""F61-FAMILY-5 (28 Sept 2026): score letter passes of the gloss recipe against the v3 skeleton (sheets/<OUT>_segments.json).
For each pass file passes/<OUT>_letters<P>_<chunk>.tsv: at the HIDDEN positions (covered by v3 but shown as '?'), the share
whose read letter falls in the v3 set (the positive control: gate 0.8); at the SHOWN positions the same share (a reader that
copies the skeleton scores 1.0 here, so it is reported, not gated). '-' counts as a miss (also reported without '-').
A letter 'falls in the set' when its first character (u/v and i/j folded) is one of the set's letters.
  python3 score_letters.py OUT CHUNK [PASS ...]   (default passes A B, plus the reconciled file passes/rec<OUT>_<chunk>/... if present)"""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
out, chunk = sys.argv[1], sys.argv[2]; passes = sys.argv[3:] or ["A", "B"]
J = json.load(open(f"{HERE}/sheets/{out}_segments.json")); by = {s["file"].replace(".jpg", ""): s for s in J["segments"]}
FOLD = {"v": "u", "j": "i", "y": "i"}
def inset(letters, st):
    l = (letters or "").strip().lower()
    if not l or l == "-": return None
    c = FOLD.get(l[0], l[0]); return c in {FOLD.get(x, x) for x in st.split("/")}
def score(rows, tag):
    hid = [0, 0, 0]; shw = [0, 0, 0]   # in-set, total, dashes
    for r in rows:
        s = by.get(r["segment"]);
        if not s: continue
        pos = int(r["pos"]); hidden = {h[0]: h[2] for h in s["hidden"]}; shown = {i: v for i, v in s["shown"] if v != "?"}
        if pos in hidden: st = hidden[pos]; acc = hid
        elif pos in shown: st = shown[pos]; acc = shw
        else: continue
        v = inset(r["letters"], st); acc[1] += 1
        if v is None: acc[2] += 1
        elif v: acc[0] += 1
    f = lambda a: f"{a[0]}/{a[1]} = {a[0]/a[1]:.3f}" + (f" (without '-': {a[0]}/{a[1]-a[2]} = {a[0]/(a[1]-a[2]):.3f})" if a[2] else "") if a[1] else "n/a"
    print(f"{tag}: hidden {f(hid)}; shown {f(shw)}")
    return hid
for p in passes:
    f = f"{P}/{out}_letters{p}_{chunk}.tsv"
    if os.path.exists(f): score(list(csv.DictReader(open(f), delimiter="\t")), f"pass {p}")
rec = f"{P}/rec{out}_{chunk}/ciphertext_draft.tsv"
if os.path.exists(rec):
    rows = [{"segment": r["line"], "pos": r["position"], "letters": r["sign"]} for r in csv.DictReader(open(rec), delimiter="\t")]
    h = score(rows, "reconciled (agreed positions only)")
