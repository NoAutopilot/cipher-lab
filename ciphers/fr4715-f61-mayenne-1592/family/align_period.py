#!/usr/bin/env python3
"""F61-FAMILY (28 Sept 2026): period-gloss key recovery for one interlined leaf of the Mayenne cipher family.

Inputs (per leaf PREFIX, e.g. f274): passes/<PREFIX>_signsA.tsv + _signsB.tsv (two blind Opus shape passes, atlas
codes) reconciled by tools/reconcile_passes.py (nw) into passes/rec<PREFIX>/ciphertext_draft.tsv; passes/<PREFIX>_glossA.tsv
+ _glossB.tsv (two blind Sonnet passes of the period clear words written above each cipher row), reconciled here per
line by difflib on the word sequence (agreed words kept; a word only one pass read is kept at conf L; a word the two
passes spell differently takes pass A's spelling at conf M with B's in the note). Alignment: tools/interlinear_align.py
(the shared Thurloe DP / hard-EM) in --code-prefix @ mode with --null-cost -1 and --clear-consumes (an inline clear
word takes its own span), one pair per band: plain_raw = the band's gloss words in x order, cipher_raw = the band's
atlas codes in order. A second, independent placement is reported alongside: each gloss word assigned to the signs
under it by x position (word x0 -> next word's x0, in native px), with the letters/signs count per word, which shows
where a word is a code group (fewer signs than letters) or carries nulls (more signs than letters).
Output: passes/<PREFIX>_pairs.tsv, _align.tsv, _key.tsv (the tool's), and the rows of key_period.tsv for this leaf
(class, letter, n, leaf, bands). Grade C for every pair: the meaning is the period decipherer's, nothing is fitted.
  python3 align_period.py PREFIX LEAF_LABEL   (from the family folder)
"""
import csv, difflib, json, os, subprocess, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../..")
pre, leaf = sys.argv[1], sys.argv[2]
P = f"{HERE}/passes"; bands = json.load(open(f"{HERE}/sheets/{pre}_bands.json")); sc = bands["scale"]
def segx(box_name):
    return bands["boxes"][box_name][0]
def rd(path):
    return [r for r in csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t")]
# --- signs: reconciled draft + x from pass A (same count per band, NW columns = positions)
draft = rd(f"{P}/rec{pre}/ciphertext_draft.tsv"); A = rd(f"{P}/{pre}_signsA.tsv")
ax = {(r["line"], int(r["pos"])): r for r in A}
bpass = {(r["line"], int(r["pos"])): r for r in rd(f"{P}/{pre}_signsB.tsv")} if os.path.exists(f"{P}/{pre}_signsB.tsv") else {}
signs = defaultdict(list)
for r in draft:
    line, pos = r["line"], int(r["position"]); a = ax.get((line, pos))
    seg = a["segment"] if a else "s1"; x = int(a["x_px"]) / sc + (segx(f"{pre}_{line}_{seg}.jpg") - bands["region"][0]) if a else 0
    code = r["sign"]; note = a["note"] if a else ""
    if code == "DASH": continue   # f.101r: a dash inside the cipher row is a separator, not a sign (dropped from the alignment)
    # f.274 (28 Sept 2026): the two blind readers split one atlas class systematically -- pass A codes both the plain
    # '#/4#' sign and the '2 joined to a crossed 4' sign HASH4, pass B codes the latter 4STEM (alt HASH4). The period
    # gloss reads them differently (d/q under the plain sign, i/x under the '24' sign), so the pair (A, B) defines two
    # classes here: HASH4 (both HASH4) and H24 (A HASH4, B 4STEM), the latter a new atlas row for this hand.
    bx = bpass.get((line, pos))
    if a and bx and a["sign"] == "HASH4" and bx["sign"] == "4STEM": code = "H24"
    elif a and bx and {a["sign"], bx["sign"]} == {"HASH4", "4STEM"}: code = "H24"
    signs[line].append({"pos": pos, "code": code, "conf": r["confidence"], "x": x, "note": note})
# --- gloss: reconcile A and B per line
def words(path):
    out = defaultdict(list)
    for r in rd(path):
        seg = r["segment"] if r["segment"].startswith("s") else "s" + r["segment"]
        x0 = int(r["x0_px"]) / sc + (segx(f"{pre}_{r['line']}_{seg}.jpg") - bands["region"][0])
        # f.101r (F61-FAMILY-2, 28 Sept 2026): the decipherer's long dashes are listed by the gloss passes as kind = dash
        # (word '-'); they carry no letters and are dropped here (they sit over signs the decipherer left unread or over nulls)
        if r["kind"].strip().lower() == "dash" or r["word"].strip() in ("-", "--", "\u2014", "_") or r["word"].strip().endswith("_struck"): continue   # _struck: a word the decipherer crossed out (pass D, chunk 3)
        out[r["line"]].append({"w": r["word"].strip(), "kind": r["kind"], "conf": r["conf"], "x0": x0})
    return out
gloss = {}; gstat = Counter()
REC = f"{P}/{pre}_gloss_rec.tsv"
if os.path.exists(REC):   # a reconciled gloss file (the reconciler's settlement from the leaf, with per-word sources) wins
    for r in rd(REC):
        gloss.setdefault(r["line"], []).append({"w": r["word"], "kind": r["kind"], "conf": r["conf"], "x0": float(r["x0"]), "src": r["src"]})
    gstat["reconciled_file"] = sum(len(v) for v in gloss.values()); GA = GB = {}
else:
    GP = ("C", "D") if os.path.exists(f"{P}/{pre}_glossC.tsv") else ("A", "B")   # f.101r: C/D are the Opus gloss passes
    GA, GB = words(f"{P}/{pre}_gloss{GP[0]}.tsv"), words(f"{P}/{pre}_gloss{GP[1]}.tsv")
for line in sorted(set(GA) | set(GB)):
    a, b = GA.get(line, []), GB.get(line, []); wa, wb = [w["w"].lower() for w in a], [w["w"].lower() for w in b]
    sm = difflib.SequenceMatcher(None, wa, wb, autojunk=False); out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1): out.append(dict(a[i1 + k], conf="h", src="AB")); gstat["agree"] += i2 - i1
        elif tag == "replace":
            for k in range(max(i2 - i1, j2 - j1)):
                if k < i2 - i1:
                    w = dict(a[i1 + k], conf="m", src="A"); w["alt"] = b[j1 + k]["w"] if k < j2 - j1 else ""; out.append(w); gstat["differ"] += 1
                else: out.append(dict(b[j1 + k], conf="l", src="B")); gstat["B-only"] += 1
        elif tag == "delete":
            for k in range(i1, i2): out.append(dict(a[k], conf="l", src="A")); gstat["A-only"] += 1
        else:
            for k in range(j1, j2): out.append(dict(b[k], conf="l", src="B")); gstat["B-only"] += 1
    out.sort(key=lambda w: w["x0"]); gloss[line] = out
print("gloss reconciliation:", dict(gstat))
# --- pairs for the shared tool
with open(f"{P}/{pre}_pairs.tsv", "w") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["plain_line", "plain_raw", "cipher_line", "cipher_raw"])
    for line in sorted(signs):
        plain = " ".join(g["w"] for g in gloss.get(line, []))
        ciph = " ".join(("@" + s["code"]) if s["code"] != "PLAIN" else s["note"].strip().replace(" ", "_") or "PLAIN" for s in signs[line])
        w.writerow([line, plain, line, ciph])
r = subprocess.run([sys.executable, f"{ROOT}/tools/interlinear_align.py", "align", f"{P}/{pre}_pairs.tsv", f"{P}/{pre}_align.tsv", f"{P}/{pre}_key.tsv",
                    "--code-prefix", "@", "--null-cost", "-1", "--clear-consumes"], capture_output=True, text=True)
print("interlinear_align:", r.stdout.strip(), r.stderr.strip()[-300:])
# --- key rows from the tool's per-token alignment: (class, letter) with counts and bands
pairs = Counter(); where = defaultdict(set)
for t in rd(f"{P}/{pre}_align.tsv"):
    if t["kind"] not in ("code",): continue
    code = t["raw"].lstrip("@"); ch = t["plain_chunk"].strip()
    val = ch if ch else "-"
    pairs[(code, val)] += 1; where[(code, val)].add(t["cipher_line"])
with open(f"{P}/{pre}_keyrows.tsv", "w") as f:
    f.write("class\tletter\tn\tleaf\tbands\n")
    for (code, val), n in sorted(pairs.items(), key=lambda kv: (kv[0][0], -kv[1], kv[0][1])):
        f.write(f"{code}\t{val}\t{n}\t{leaf}\t{','.join(sorted(where[(code, val)]))}\n")
# --- x-position placement (independent check)
with open(f"{P}/{pre}_xcheck.tsv", "w") as f:
    f.write("line\tword\tkind\tletters\tsigns\tcodes\n"); tot = Counter()
    for line in sorted(signs):
        gl = gloss.get(line, []); ss = signs[line]
        for i, g in enumerate(gl):
            x0 = g["x0"] - 15; x1 = (gl[i + 1]["x0"] - 15) if i + 1 < len(gl) else 1e9
            under = [s for s in ss if x0 <= s["x"] < x1]
            L = len([c for c in g["w"] if c.isalpha()]); f.write(f"{line}\t{g['w']}\t{g['kind']}\t{L}\t{len(under)}\t{' '.join(s['code'] for s in under)}\n")
            tot["equal" if L == len(under) else ("more_signs" if len(under) > L else "fewer_signs")] += 1
    print("x-placement words:", dict(tot))
print("key rows:", len(pairs), "classes:", len(set(c for c, _ in pairs)))
