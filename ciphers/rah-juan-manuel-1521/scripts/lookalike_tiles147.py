"""Look-alike pass inputs for R9526 ff.147-147v (R14-RJM9526, 6 Oct 2026).

Same construction as scripts/lookalike_tiles.py (R11-RJMLA), whose page_rows() is imported unchanged; only the page differs:
f147 = the two blind passes passes/f147_A.tsv / f147_B.tsv with test147.py's NORM147 (pass B ?1 -> 7). Candidates per tile = the
two readers' labels plus each symbol label's two most frequent confusion partners, the partners counted from lookalike/confusion.tsv
(f.194 + f.199) plus f.147's own equal-length split swaps. Writes lookalike/f147_passC.tsv, lookalike/f147_tiles.tsv.

  python3 scripts/lookalike_tiles147.py [--check]
"""
import collections, csv, importlib.util, io, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


def mod(name, f):
    s = importlib.util.spec_from_file_location(name, HERE / "scripts" / f)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


lt = mod("lt", "lookalike_tiles.py")
t147 = mod("t147", "test147.py")
t1 = lt.t1
t1.DUP["f147"] = set()
for p, m in t147.NORM147.items():
    t1.NORM[("f147", p)] = m
OUT = HERE / "lookalike"


def build():
    key = t1.load_key()
    pc, tl, sw = lt.page_rows("f147", key)
    swaps = collections.Counter(sw)
    with open(OUT / "confusion.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            swaps[(r["label_a"], r["label_b"])] += int(r["count"])
    partners = collections.defaultdict(list)
    for (x, y), c in sorted(swaps.items(), key=lambda kv: (-kv[1], kv[0])):
        partners[x].append(y); partners[y].append(x)

    def tsv(rows, fields):
        s = io.StringIO()
        w = csv.DictWriter(s, fields, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
        return s.getvalue()
    rows = []
    for t in tl:
        cand = [x for x in (t["A"], t["B"]) if lt.SYM(x)]
        for x in list(cand):
            cand += partners[x][:2]
        cand += [x for x in (t["A"], t["B"]) if x and not lt.SYM(x)]
        rows.append(dict(run="rjm9526_f147", passage=t["passage"], pos=t["pos"], passC="~", A=t["A"], B=t["B"],
                         status="split", why="split", candidates=",".join(dict.fromkeys(cand)),
                         before=t["before"], after=t["after"], noteA="", noteB=""))
    return {"f147_passC.tsv": tsv(pc, ["passage", "pos", "sign_id"]),
            "f147_tiles.tsv": tsv(rows, ["run", "passage", "pos", "passC", "A", "B", "status", "why", "candidates",
                                         "before", "after", "noteA", "noteB"])}


def main():
    files = build()
    if "--check" in sys.argv:
        stale = [k for k, v in files.items() if not (OUT / k).exists() or (OUT / k).read_text() != v]
        print("stale: " + ", ".join(stale) if stale else "up to date")
        sys.exit(1 if stale else 0)
    for k, v in files.items():
        (OUT / k).write_text(v)
    print({k: v.count("\n") - 1 for k, v in files.items()})


if __name__ == "__main__":
    main()
