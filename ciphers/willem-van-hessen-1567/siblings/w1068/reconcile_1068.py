#!/usr/bin/env python3
"""WVO-1068-KEY (account 4, 9-10 Oct 2026): reconcile the two blind passes over WVO 1068 p.2 (10 cipher lines, each under
the period decipherment) into ../ciphertext_1068.tsv, reconcile_1068.tsv and ../key_1068.tsv.

Inputs: passA_L*.tsv (pass A, 1069 class names as a reference vocabulary + NEW:), passB_L*.tsv (pass B, own labels).
Worker's own reconciliation, made against the crops and three own region looks (see NOTES.md WVO-1068-KEY):
  - CLASS: pass B's labels (internally consistent within a band) are unified across the three bands in UNIFY below; where
    pass B lumped shapes that pass A split, the token override in TOKCLASS follows pass A.
  - VALUE: the reconciled gloss letter per sign, VALUES below (the decipherer's line as this worker reads it, checked
    against both passes and, for the words, against the same news in WVO 98 f.67, august-van-saksen-1561-64/align_98.txt).
  - GRADE: H only where pass A's and pass B's literal gloss letters both equal VALUE after normalisation (lower case,
    v->u, j/y->i, long s->s, z/ʒ/ß->z); every other token is M (passes split, one pass blank, or the worker changed a letter
    both passes read the same way, e.g. Kurrent u read as w, round s as b, initial v as z).
Key class grade: H if the class has >= 1 H token and every H token carries the same value; a class whose H tokens disagree
is written with value '?' and grade M (conflict listed in the note); a class with no H token gets its majority VALUE, grade M.

Usage: python3 reconcile_1068.py [--check]   (--check: exit 1 if the committed outputs differ from a regeneration)
"""
import collections, csv, sys
from pathlib import Path

HERE = Path(__file__).parent
SIB = HERE.parent

BANDS = [("L01-03", 1), ("L04-06", 2), ("L07-10", 3)]
DROP_B = {(7, 8)}  # pass B L07 pos 8 'DOT' is an interpunct between words, not a sign (pass A did not count it)

VALUES = {
    1: "e s w i r t a u c h b e i u n s f u r g e w i s",
    2: "g e s a g t d a s w i l h a l m v o n g r o m b a c h",
    3: "u f f z w o l f f g e s c h ? d d r r e u t e r n",
    4: "u n d t - s t a u p i - t z u f f d r e i s s i g t",
    5: "f e n d l e i n l a n s k n e c h t u o m ^konig_zu_frankreich^",
    6: "b e s t a l l u n g h a b e n w i r b i t h e n",
    7: "a b e r e w r l i e b s i e w o l l e n u n s e r",
    8: "u n u e r m e l t n a c h f r a g e n s h a b e n",
    9: "u n d u n s i r e r e r k u n d i g u n g e",
    10: "u e r s t e n d i g e n",
}
# line 2 p17 'v' of 'von' and line 5 p19 'u' of 'vom' differ only by the v/u normalisation applied to the passes.
VALUES[2] = VALUES[2].replace("v o n", "u o n")

UNIFY = {  # (band, pass-B label) -> unified class
    1: {"EIGHTX": "loop-splayed-legs", "RLOOP": "R-loop", "PHOOK": "thorn-p", "ATAIL": "nine-tail", "TCROSS": "cross-on-base",
        "HSCRIPT": "looped-H", "DCROSS": "double-cross", "EIGHTTALL": "tall-8", "HSTEM": "h-bar", "DBAR": "double-post-box",
        "TRI": "triangle", "CHOOK": "hooked-c", "YLOOP": "mercury", "SQ": "open-square", "LOOPTAIL": "l-loop",
        "ALPHA": "alpha-loop", "EIGHT": "compact-8", "XHOOK": "X-hook", "LAMBDA": "lambda", "TWO": "two-slash",
        "NINE": "nine", "NINEL": "nine-long-tail", "OCROSS": "o-cross", "ZED": "Z", "TRIPCROSS": "triple-cross",
        "ELOOP": "l-loop", "PI": "open-pi", "HSQ": "open-pi", "OVAL": "bold-oval", "OB": "v-over-loop", "HASH": "hash",
        "LZ": "script-L-bar", "PFLAT": "hooked-c", "HUMP": "hump-cut", "FCROSS": "cross-on-base"},
    2: {"ELOOP": "l-loop", "SHOOK": "looped-gamma", "TWOCOLON": "two-colon", "HCURS": "looped-H", "OSMALL": "arc-cut",
        "KR": "R-loop", "HLOOP": "looped-H", "NINE": "nine", "EIGHT": "open-8", "B3": "flat-3", "ARROWCIRC": "mars",
        "OL": "arc-cut", "LSTEM": "looped-H", "ZERO": "bold-oval", "GLOOP": "tall-8", "SQ": "open-square", "TWOZ": "two-z",
        "TBASE": "cross-on-base", "LCURL": "pound-L", "BLOB": "blot", "BIGO": "big-circle", "CROSSBOX": "cross-over-box",
        "CURLH": "looped-gamma", "ZCROSS": "two-slash", "CURLE": "pound-L", "ZWAVE": "hook-wave", "XI": "looped-gamma",
        "DCROSS": "double-cross", "ZLOOP": "looped-gamma", "LAMBDA": "looped-lambda", "SIX": "six", "ZT": "looped-gamma",
        "EPS": "hooked-c", "BOXSTEM": "box-stem", "TOWER": "lidded-box", "ZED": "Z", "DPLUS": "d-loop-plus", "LIBRA": "libra",
        "DELTA": "triangle", "XDOT": "X-dot", "DHOOK": "alpha-loop", "PHOOK": "thorn-p", "ATAIL": "nine-tail",
        "IIBAR": "double-post-box"},
    3: {"DBLBAR": "double-cross", "DELTA": "triangle", "ELOOP": "e-loop", "TBASE": "cross-on-base", "ZED": "2-flourish",
        "THORN": "thorn-p", "HTCROSS": "h-cross", "NINE": "nine", "Y": "y-tail", "KAY": "R-loop", "SEVEN": "seven",
        "FIG8": "tall-8", "NLOOP": "looped-gamma", "DBLBAR_DOT": "double-cross-dot", "PLUSBASE": "cross-on-base",
        "CBAR": "e-loop", "OT": "o-cross", "HDOT": "x-loop", "HBAR": "h-bar", "TABLE": "double-post-box", "BOX": "filled-box",
        "TZED": "hooked-double-bar", "ALPHA": "alpha-loop", "RHO": "P-loop", "Q9": "q-on-bar", "EIGHT": "compact-8",
        "CURLO": "curl-o", "ZCROSS": "two-slash", "DARK3": "dark-3", "SIX": "looped-gamma", "ELL": "l-loop", "ZLOOP": "yogh-z", "XI": "x-loop"},
}
TOKCLASS = {  # (line, pos) -> class, where pass A split a shape pass B lumped (or B's label is band-local)
    (2, 1): "alpha-loop",       # B XHOOK, A d-loop-diagonal = B's ALPHA elsewhere
    (3, 6): "seven",            # B ZED, A seven
    (6, 23): "P-loop",          # B EPS, A p-shape (P/rho loop), as band 3 RHO
}
for ln, pos in [(8, 2), (8, 10), (9, 2), (9, 5), (9, 20)]:
    TOKCLASS[(ln, pos)] = "mercury"   # B NLOOP, A horned-cross (= band 1 YLOOP / A mercury)


def norm(g):
    g = g.strip().lower().replace("ſ", "s").replace("ʒ", "z").replace("ß", "z")
    out = []
    for ch in g:
        out.append({"v": "u", "j": "i", "y": "i"}.get(ch, ch))
    return "".join(out)


def rows(p):
    with open(p, encoding="utf-8") as f:
        r = [x for x in csv.reader(f, delimiter="\t") if x and not x[0].startswith("#")]
    return r[1:]


def build():
    toks = []
    for tag, band in BANDS:
        A = rows(HERE / f"passA_{tag}.tsv")
        B = [r for r in rows(HERE / f"passB_{tag}.tsv") if (int(r[0]), int(r[1])) not in DROP_B]
        assert len(A) == len(B), (tag, len(A), len(B))
        for a, b in zip(A, B):
            assert a[0] == b[0]
            toks.append((band, int(a[0]), a, b))
    out, per_line = [], collections.Counter()
    for band, ln, a, b in toks:
        per_line[ln] += 1
        pos = per_line[ln]
        vals = VALUES[ln].split()
        val = vals[pos - 1].replace("_", " ")
        cls = TOKCLASS.get((ln, pos), UNIFY[band][b[2]])
        ga, gb = norm(a[4]), norm(b[4])
        if val.startswith("^"):
            grade = "H" if ga.startswith("konig") and gb.startswith("konig") else "M"
        else:
            grade = "H" if ga == gb == val else "M"
        if val in ("-", "?"):
            grade = "M"
        out.append(dict(line=ln, pos=pos, sign_class=cls, passA_class=a[2], passB_label=b[2], glossA=a[4], glossB=b[4],
                        value=val, grade=grade))
    for ln, n in per_line.items():
        assert n == len(VALUES[ln].split()), (ln, n, len(VALUES[ln].split()))
    return out


def key_from(out):
    by = collections.defaultdict(list)
    for t in out:
        if t["value"] in ("-", "?"):
            by[t["sign_class"]].append(None)
        else:
            by[t["sign_class"]].append(t)
    key = []
    for cls in sorted(by):
        ts = [t for t in by[cls] if t]
        hv = collections.Counter(t["value"] for t in ts if t["grade"] == "H")
        allv = collections.Counter(t["value"] for t in ts)
        n = len(by[cls])
        if len(hv) == 1:
            v = next(iter(hv)); g = "H"
            others = {k: c for k, c in allv.items() if k != v}
            note = f"{hv[v]} H token(s)" + (f"; M tokens elsewhere read {dict(others)}" if others else "")
        elif len(hv) > 1:
            v, g, note = "?", "M", f"H tokens conflict {dict(hv)}"
        elif allv:
            v, c = allv.most_common(1)[0]; g = "M"
            note = f"no H token; reconciled values {dict(allv)}"
        else:
            v, g, note = "?", "M", "no gloss over any occurrence"
        key.append((cls, v, n, g, note))
    return key


def render():
    out = build()
    rec = ["line\tpos\tsign_class\tpassA_class\tpassB_label\tglossA\tglossB\tvalue\tgrade"]
    rec += ["\t".join(str(t[k]) for k in ("line", "pos", "sign_class", "passA_class", "passB_label", "glossA", "glossB",
                                          "value", "grade")) for t in out]
    ct = ["page\tline\tpos\tsign_desc\tvalue\tgrade",
          "# briefnr 1068 (Oranje to Willem van Hessen, 13 Mar 1563, HSAM 3II Korr. 1563 f.27r-30v) p.2 cipher postscript, "
          "every sign; value/grade = the period gloss over it as reconciled (w1068/reconcile_1068.py). WVO-1068-KEY, 10 Oct 2026."]
    ct += [f"2\t{t['line']}\t{t['pos']}\t{t['sign_class']}\t{t['value']}\t{t['grade']}" for t in out]
    key = key_from(out)
    kt = ["sign_desc\tvalue\tcount\tgrade\tnote",
          "# briefnr 1068 (Oranje -> Willem van Hessen, Brussels 13 Mar 1563), sign class -> letter from the contemporary "
          "decipherment written above each cipher line. A `period` key rebuilt by WVO-1068-KEY (account 4, 10 Oct 2026) from "
          "two blind Opus passes + the worker's reconciliation (w1068/reconcile_1068.py). Class names are this letter's own "
          "(not the 1069 names); the 1069 / f.23 concordance is a separate controlled test (w1068/concord_1068.py)."]
    kt += ["\t".join(map(str, k)) for k in key]
    return {HERE / "reconcile_1068.tsv": "\n".join(rec) + "\n", SIB / "ciphertext_1068.tsv": "\n".join(ct) + "\n",
            SIB / "key_1068.tsv": "\n".join(kt) + "\n"}


def main():
    files = render()
    if "--check" in sys.argv:
        bad = [p.name for p, s in files.items() if not p.exists() or p.read_text(encoding="utf-8") != s]
        print("stale: " + ", ".join(bad) if bad else "OK: reconcile_1068.tsv, ciphertext_1068.tsv, key_1068.tsv current")
        sys.exit(1 if bad else 0)
    for p, s in files.items():
        p.write_text(s, encoding="utf-8")
    out = build()
    g = collections.Counter(t["grade"] for t in out)
    print(f"tokens {len(out)}: {dict(g)}; classes {len(key_from(out))}")


if __name__ == "__main__":
    main()
