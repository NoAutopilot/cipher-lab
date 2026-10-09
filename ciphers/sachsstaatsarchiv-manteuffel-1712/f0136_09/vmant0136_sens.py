"""V-MANT0136 (verifier, 9 Oct 2026): sensitivity of MANT-0136 gate (b) -- NOT a re-registered gate, an audit check.
Same scorer, key, permutation design, seed and 1000 draws as judge_gate.py; only the token subset changes:
  (1) unglossed under the A1 spans (gloss_A1A/A1B.tsv added), (2) the runs that read under the table only (r04, r06),
  (3) the runs that do not read (r01, r02, r09). Run from the repository root: python3 <this> [--check]"""
import csv, sys, importlib.util
from pathlib import Path
F = Path("ciphers/sachsstaatsarchiv-manteuffel-1712/f0136_09")
sys.argv_saved = sys.argv; sys.argv = [sys.argv[0]]
spec = importlib.util.spec_from_file_location("jg", F / "judge_gate.py"); jg = importlib.util.module_from_spec(spec)
import builtins; _open = builtins.open
class _Sink:  # judge_gate writes judge_gate.out at import; keep its own file untouched
    def __enter__(s): return s
def guarded_open(p, mode="r", *a, **k):
    if "w" in mode and str(p).endswith("judge_gate.out"): return _open("/dev/null", mode, *a, **k)
    return _open(p, mode, *a, **k)
builtins.open = guarded_open; spec.loader.exec_module(jg); builtins.open = _open
sys.argv = sys.argv_saved
rows = [r for r in csv.DictReader((l for l in open(F / "ciphertext.tsv") if not l.startswith("#")), delimiter="\t")]
def spans(files):
    s = set()
    for g in files:
        for r in csv.DictReader(open(F / g), delimiter="\t"): s.update(r["tokids"].split())
    return s
a1 = spans(["gloss_A.tsv", "gloss_B.tsv", "gloss_A1A.tsv", "gloss_A1B.tsv"])
sets = {"unglossed_after_A1": [r["sign"] for r in rows if f"{r['line']}.{r['pos']}" not in a1],
        "reading_runs_r04_r06": [r["sign"] for r in rows if r["line"].endswith(("r04", "r06")) and f"{r['line']}.{r['pos']}" not in a1],
        "nonreading_runs_r01_r02_r09": [r["sign"] for r in rows if r["line"].endswith(("r01", "r02", "r09"))]}
jg.lines.clear()
for n, t in sets.items(): jg.gate(n, t, 136)
txt = "\n".join(jg.lines) + "\n"
out = F / "vmant0136_sens.out"
if "--check" in sys.argv:
    good = out.exists() and out.read_text() == txt; print("vmant0136_sens.out up to date" if good else "STALE"); sys.exit(0 if good else 1)
out.write_text(txt); print(txt, end="")
