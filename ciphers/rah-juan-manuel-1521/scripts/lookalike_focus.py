"""Carry the look-alike pass's UNSETTLED symbol tiles into the sorter's focus list (R11-RJMLA, 6 Oct 2026).

A tile id is passage.pos (token position in the reconciled line); the sorter's tiles are glyph_atlas boxes (sorter/signs.tsv,
x in the same iiif_lines crop's pixels). The token's x is estimated exactly as tools/lookalike_pass.py windows does
(even spacing over the inked span of the crop) and the nearest box centre on that line is taken. The estimate can be off by
1-3 tokens on a mixed code/symbol line, so every question says 'about here' and names the readers' labels: it points the
owner at a place, it does not claim the box is the sign. Only tiles with at least one SYMBOL candidate are carried (a split
between two Latin code groups is not a sorter question). Rows are appended after the RUN1-SEG rows, which are kept.

  python3 scripts/lookalike_focus.py --crops DIR194 --crops DIR199   (crops from the commands in NOTES.md; not committed)
"""
import argparse, csv, importlib.util, sys
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent.parent
ROOT = HERE.parent.parent
spec = importlib.util.spec_from_file_location("lp", ROOT / "tools/lookalike_pass.py")
lp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lp)
spec2 = importlib.util.spec_from_file_location("lt", HERE / "scripts/lookalike_tiles.py")
lt = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(lt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--crops", action="append", required=True)
    a = ap.parse_args()
    boxes = {}
    for r in csv.DictReader(open(HERE / "sorter/signs.tsv"), delimiter="\t"):
        boxes.setdefault(r["page"], []).append((int(r["x"]) + int(r["w"]) / 2, r["sid"]))
    keep = [l for l in open(HERE / "sorter/focus.tsv").read().splitlines() if l and "R11-RJMLA" not in l]
    rows, used = [], {l.split("\t")[0] for l in keep}
    for page in ("f194", "f199"):
        n = {}
        for r in csv.DictReader(open(HERE / f"lookalike/{page}_passC.tsv"), delimiter="\t"):
            n[r["passage"]] = n.get(r["passage"], 0) + 1
        T = {(t["passage"], t["pos"]): t for t in csv.DictReader(open(HERE / f"lookalike/{page}_tiles.tsv"), delimiter="\t")}
        R = {(r["passage"], r["pos"]): r for r in csv.DictReader(open(HERE / f"lookalike/{page}_reread.tsv"), delimiter="\t")}
        for k, t in T.items():
            r = R[k]
            firm = r["conf"] in ("H", "M") and not r["label"].startswith("SPLIT")
            if firm and r["label"] in (t["A"], t["B"]):
                continue
            cands = [c for c in t["candidates"].split(",") if lt.SYM(c)]
            if not cands:
                continue
            ln, pos = k[0], int(k[1])
            f = next(Path(d) / f"{ln}.jpg" for d in a.crops if (Path(d) / f"{ln}.jpg").exists())
            S = Image.open(f).convert("L")
            xa, xb = lp._ink_extent(S, 110, 2)
            x = xa + (pos - 0.5) * (xb - xa) / n[ln]
            sp = ln.replace("_", "")
            if sp not in boxes:
                continue
            sid = min(boxes[sp], key=lambda b: abs(b[0] - x))[1]
            if sid in used:   # two tiles on one box: the first question stands
                continue
            used.add(sid)
            rows.append(f"{sid}\tR11-RJMLA look-alike, about here ({ln} token {pos}, position approximate): readers "
                        f"{t['A'] or '-'} / {t['B'] or '-'}, third reader {r['label']} ({r['conf']}); "
                        f"which of {', '.join(sorted(set(cands)))}, or a code word?")
    (HERE / "sorter/focus.tsv").write_text("\n".join(keep + rows) + "\n")
    print(f"kept {len(keep)}, added {len(rows)}")


if __name__ == "__main__":
    sys.exit(main())
