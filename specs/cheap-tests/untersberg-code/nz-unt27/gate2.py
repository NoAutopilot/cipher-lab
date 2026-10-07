"""NZ-UNT27 gate 2 (PREREG-NZ-UNT27): count positions whose raw description, in each pass, names a hooked/looped/curled
top AND a descender (or a stem running below the baseline); joint = same aligned column (via reconcile agreement.tsv
column order is per pass, so joint is matched on crop+description by line/pos in each pass's own numbering, then
checked against the aligned draft). Control: crop D signs 11 and 15 (bUNT8 symA, L4 tok5/tok7) flagged as SIGN."""
import csv, re, sys
D = sys.argv[1]
TOP = re.compile(r"hook|loop|curl")
DESC = re.compile(r"descend|descender|below baseline")
for p in (1, 2):
    rows = list(csv.DictReader(open(f"{D}/pass{p}_raw.tsv"), delimiter="\t"))
    hits = [(r["line"], r["pos"], r["sign"]) for r in rows if r["line"] != "D" and r["sign"].startswith("SIGN:")
            and TOP.search(r["sign"].lower()) and DESC.search(r["sign"].lower())]
    ctrl = [r["pos"] for r in rows if r["line"] == "D" and r["pos"] in ("11", "15") and r["sign"].startswith("SIGN:")]
    print(f"pass{p}: control symA flagged at D{ctrl} -> {'HIT' if ctrl else 'MISS'}; symA-like on tablet/scroll: {len(hits)}")
    for h in hits: print("   ", *h)
