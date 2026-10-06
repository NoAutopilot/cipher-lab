"""Look-alike pass inputs for rah-juan-manuel-1521 (R11-RJMLA, 6 Oct 2026).

Rebuilds test1.py's A/B alignment (same NORM, DUP and difflib opcodes, imported from scripts/test1.py) and writes, per page,
the files tools/lookalike_pass.py needs:
  lookalike/<page>_passC.tsv   passage, pos, sign_id -- the reconciled token sequence of ciphertext_<page>_reconciled.tsv
                               (one row per token; '~' where the readers split)
  lookalike/<page>_tiles.tsv   one tile per '~' of the reconciled TSV that comes from a reader split (test 1's 88 + 114
                               'split symbol tokens'; a '~' both readers wrote is not a split and is not tiled);
                               A, B = the two readers' labels at that position (paired by index inside a split segment; a
                               reader with a shorter segment gives ''), candidates = A, B and their two most frequent
                               confusion partners (symbol labels only)
  lookalike/confusion.tsv      unordered symbol-label swaps with counts, from equal-length split segments on both pages
  lookalike/desc.tsv           label -> shape description (passes/inventory.md, plus the pass-local labels' own notes)

  python3 scripts/lookalike_tiles.py [--check]   (--check: exit 1 if the committed files differ from a rerun)
"""
import collections, csv, difflib, importlib.util, io, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("t1", HERE / "scripts/test1.py")
t1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t1)
OUT = HERE / "lookalike"
# f.199 pass B's own ?n labels (not in the shared inventory; test1.py's NORM leaves them unmapped)
LOCAL = {("f199", "B"): {"?1": "Hb", "?2": "Tri"}}
DESC = {
    "V": "v-shaped sign with a hooked/flourished left stroke", "4": "a numeral-4 shape",
    "T": "crossed double-t, 'tt' with one bar through both, or '#'", "Z": "z / 3 whose tail hangs well BELOW the line (yogh)",
    "3": "a 3-shape sitting ON the line, no long tail", "F": "tall long-s with a loop / figure-8 at its foot",
    "Q": "q or g whose descender is crossed by a horizontal stroke", "A": "open alpha / fish sign",
    "D": "d whose ascender loops back to the left", "R": "small raised 'ro'/'co' sign with a tiny o tucked below",
    "E": "large epsilon / reversed 3 with a big upper bowl", "9": "numeral 9", "X": "a stand-alone x",
    "W": "two linked o's joined with a loop", "B": "a capital-B-like sign",
    "K": "cross / dagger sign, or a circle on a cross (ankh-like)", "Hb": "hooked b/h-like sign",
    "Tri": "small triangle / nabla sign",
}
SYM = lambda t: bool(t) and (t in DESC or bool(t1.SYMBOL.match(t)))


def page_rows(page, key):
    P = {}
    for p in "AB":
        rows = t1.load_pass(page, p)
        m = LOCAL.get((page, p), {})
        P[p] = {n: [m.get(t, t) for t in v] for n, v in rows.items()}
    A, B = P["A"], P["B"]
    passc, tiles, swaps = [], [], collections.Counter()
    for n in sorted(set(A) | set(B)):
        a, b = A.get(n, []), B.get(n, [])
        sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
        line = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                line += [(t, None, None) for t in a[i1:i2]]
                continue
            sa, sb = a[i1:i2], b[j1:j2]
            ka, kb = sum(t in key for t in sa), sum(t in key for t in sb)
            pick_a = ka > kb or (ka == kb and len(sa) >= len(sb))
            pick = sa if pick_a else sb
            if len(sa) == len(sb):
                for x, y in zip(sa, sb):
                    if SYM(x) and SYM(y) and x != y:
                        swaps[tuple(sorted((x, y)))] += 1
            for k, t in enumerate(pick):
                ta = sa[k] if k < len(sa) else ""
                tb = sb[k] if k < len(sb) else ""
                line.append((t if t in key else "~", ta, tb))
        ln = f"{page}_L{n:02d}"
        seq = [t for t, _, _ in line]
        for i, (t, ta, tb) in enumerate(line, 1):
            passc.append(dict(passage=ln, pos=i, sign_id=t))
            if ta is None or t != "~":
                continue
            tiles.append(dict(passage=ln, pos=i, A=ta, B=tb, before=" ".join(seq[max(0, i - 4):i - 1]),
                              after=" ".join(seq[i:i + 3])))
    return passc, tiles, swaps


def build():
    key = t1.load_key()
    files, swaps, per = {}, collections.Counter(), {}
    for page in ("f194", "f199"):
        pc, tl, sw = page_rows(page, key)
        per[page] = (pc, tl)
        swaps.update(sw)
    partners = collections.defaultdict(list)
    for (x, y), c in swaps.most_common():
        partners[x].append(y); partners[y].append(x)

    def tsv(rows, fields):
        s = io.StringIO()
        w = csv.DictWriter(s, fields, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
        return s.getvalue()
    files["confusion.tsv"] = tsv([dict(label_a=x, label_b=y, count=c) for (x, y), c in swaps.most_common()],
                                 ["label_a", "label_b", "count"])
    files["desc.tsv"] = "".join(f"{k}\t{v}\n" for k, v in DESC.items())
    for page, (pc, tl) in per.items():
        files[f"{page}_passC.tsv"] = tsv(pc, ["passage", "pos", "sign_id"])
        rows = []
        for t in tl:
            cand = [x for x in (t["A"], t["B"]) if SYM(x)]
            for x in list(cand):
                cand += partners[x][:2]
            cand += [x for x in (t["A"], t["B"]) if x and not SYM(x)]   # a code group one reader saw there
            rows.append(dict(run=f"rjmla_{page}", passage=t["passage"], pos=t["pos"], passC="~", A=t["A"], B=t["B"],
                             status="split", why="split", candidates=",".join(dict.fromkeys(cand)),
                             before=t["before"], after=t["after"], noteA="", noteB=""))
        files[f"{page}_tiles.tsv"] = tsv(rows, ["run", "passage", "pos", "passC", "A", "B", "status", "why",
                                                 "candidates", "before", "after", "noteA", "noteB"])
    return files


def main():
    files = build()
    if "--check" in sys.argv:
        stale = [k for k, v in files.items() if not (OUT / k).exists() or (OUT / k).read_text() != v]
        print("stale: " + ", ".join(stale) if stale else "up to date")
        sys.exit(1 if stale else 0)
    OUT.mkdir(exist_ok=True)
    for k, v in files.items():
        (OUT / k).write_text(v)
    for page in ("f194", "f199"):
        print(page, "tiles", files[f"{page}_tiles.tsv"].count("\n") - 1,
              "signs", files[f"{page}_passC.tsv"].count("\n") - 1)


if __name__ == "__main__":
    main()
