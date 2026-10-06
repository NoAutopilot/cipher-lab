"""Look-alike pass inputs for R9501 f.34 (R13-RJM34LA, 6 Oct 2026).

Same construction as scripts/lookalike_tiles.py (R11-RJMLA), on the f.34 passes as scripts/decode9501.py reads them (NORM34,
pass B's reverse LINE_MAP, test1.py's reconcile picks), so the tiles are exactly the split '~' tokens of
ciphertext_f34_reconciled.tsv. Writes:
  lookalike/f34_passC.tsv   passage, pos, sign_id -- ciphertext_f34_reconciled.tsv, one row per token
  lookalike/f34_tiles.tsv   one tile per reader-split '~' (status split; A, B = the readers' labels at that position, paired by
                            index inside the split segment, '' where a reader's segment is shorter); candidates = A, B and their
                            two most frequent confusion partners (lookalike/confusion.tsv, f.194/f.199, plus f.34's own swaps)
                            -- and one tile per agreed out-of-table group of the four the brief names (y, g, rob, ez), status
                            'oot', candidates = the group as read plus every table code at edit distance 1 (an eye check: both
                            readers agree there, so the 2-of-3 rule cannot overturn it; the re-read is a pointer only)
  lookalike/f34_confusion.tsv  f.34's own symbol swaps (equal-length split segments)

  python3 scripts/lookalike_tiles34.py [--check]   (--check: exit 1 if the committed files differ from a rerun)
"""
import collections, csv, difflib, importlib.util, io, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
def _mod(name, path):
    s = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m
d = _mod("d9501", HERE / "scripts/decode9501.py")
t1 = d.t1
OUT = HERE / "lookalike"
OOT = ("y", "g", "rob", "ez")
DESC_EXTRA = {"y": "a Latin y (letter group, as read)", "g": "a Latin g (letter group, as read)"}


def ed1(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    return 0 < sum(x != y for x, y in zip(a, b)) + abs(len(a) - len(b)) <= 1 if len(a) == len(b) else \
        any(a[:i] + a[i + 1:] == b for i in range(len(a))) or any(b[:i] + b[i + 1:] == a for i in range(len(b)))


def build():
    key = t1.load_key()
    A, B = d.load("A"), d.load("B")
    SYM = lambda t: bool(t) and bool(t1.SYMBOL.match(t))
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
            pick = sa if (ka > kb or (ka == kb and len(sa) >= len(sb))) else sb
            if len(sa) == len(sb):
                for x, y in zip(sa, sb):
                    if SYM(x) and SYM(y) and x != y:
                        swaps[tuple(sorted((x, y)))] += 1
            for k, t in enumerate(pick):
                line.append((t if t in key else "~", sa[k] if k < len(sa) else "", sb[k] if k < len(sb) else ""))
        ln = f"f34_L{n:02d}"
        seq = [t for t, _, _ in line]
        for i, (t, ta, tb) in enumerate(line, 1):
            passc.append(dict(passage=ln, pos=i, sign_id=t))
            ctx = dict(before=" ".join(seq[max(0, i - 4):i - 1]), after=" ".join(seq[i:i + 3]))
            if ta is not None and t == "~":
                tiles.append(dict(passage=ln, pos=i, A=ta, B=tb, status="split", **ctx))
            elif ta is None and t in OOT:
                tiles.append(dict(passage=ln, pos=i, A=t, B=t, status="oot", **ctx))
    pooled = collections.Counter(swaps)
    with open(OUT / "confusion.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            pooled[tuple(sorted((r["label_a"], r["label_b"])))] += int(r["count"])
    partners = collections.defaultdict(list)
    for (x, y), c in pooled.most_common():
        partners[x].append(y); partners[y].append(x)
    rows = []
    for t in tiles:
        if t["status"] == "oot":
            cand = [t["A"]] + sorted(k for k in key if ed1(t["A"], k))
            if len(t["A"]) == 1:
                cand += ["K", "Q", "Z"]          # a one-letter Latin read may be a symbol (brief: y/g for K/Q)
        else:
            cand = [x for x in (t["A"], t["B"]) if SYM(x)]
            for x in list(cand):
                cand += partners[x][:2]
            cand += [x for x in (t["A"], t["B"]) if x and not SYM(x)]
        rows.append(dict(run="rjm34la_f34", passage=t["passage"], pos=t["pos"], passC="~" if t["status"] == "split" else t["A"],
                         A=t["A"], B=t["B"], status=t["status"], why=t["status"], candidates=",".join(dict.fromkeys(cand)),
                         before=t["before"], after=t["after"], noteA="", noteB=""))

    def tsv(rs, fields):
        s = io.StringIO()
        w = csv.DictWriter(s, fields, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rs)
        return s.getvalue()
    return {"f34_passC.tsv": tsv(passc, ["passage", "pos", "sign_id"]),
            "f34_tiles.tsv": tsv(rows, ["run", "passage", "pos", "passC", "A", "B", "status", "why", "candidates", "before",
                                        "after", "noteA", "noteB"]),
            "f34_confusion.tsv": tsv([dict(label_a=x, label_b=y, count=c) for (x, y), c in swaps.most_common()],
                                     ["label_a", "label_b", "count"])}


def main():
    files = build()
    if "--check" in sys.argv:
        stale = [k for k, v in files.items() if not (OUT / k).exists() or (OUT / k).read_text() != v]
        print("stale: " + ", ".join(stale) if stale else "up to date")
        sys.exit(1 if stale else 0)
    for k, v in files.items():
        (OUT / k).write_text(v)
    t = files["f34_tiles.tsv"]
    print("signs", files["f34_passC.tsv"].count("\n") - 1, "split tiles", t.count("\tsplit\tsplit\t"),
          "oot tiles", t.count("\toot\toot\t"))


if __name__ == "__main__":
    main()
