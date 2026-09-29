#!/usr/bin/env python3
"""H344 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: rule 3's ARM-C1 control for H342's order
statistic -- run H342's code unchanged on each leaf with its draft signs SHUFFLED across the whole leaf first (3 shuffles, seeds 3440..3442); on a
shuffled target the real order carries no sequence, so v7's gain must fall into the binned keys' range. Pre-stated: H342's statistic is voided as a
gate on a leaf if v7 shows 'order signal' on >= 1 of that leaf's 3 shuffled targets; H342's held-leaf results stand only on leaves where it shows none.
Leaves: recf101r, recf188r, recf124r, recf97r, rec108v, recf108vg (f.106rall skipped: no order signal to void).   python3 h344_seqgain_shuftarget.py [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ARGS = sys.argv[1:]; out = []
base = open(f"{HERE}/h335_106r_v7_beam.py").read()
inj = 'rows = rd(f"{P}/recf106rall/ciphertext_draft.tsv")'; assert inj in base
h342 = open(f"{HERE}/h342_beam_seqgain.py").read(); h342 = h342[:h342.index("res = {}")]
void = []
for prefix in ("recf101r", "recf188r", "recf124r", "recf97r", "rec108v", "recf108vg"):
    hits = []; det = []
    for seed in (3440, 3441, 3442):
        shuf = base.replace(inj, inj + f"\n_sg = [r['sign'] for r in rows]; __import__('random').Random({seed}).shuffle(_sg)\nfor _r, _s in zip(rows, _sg): _r['sign'] = _s")
        g = {"__file__": f"{HERE}/h342_beam_seqgain.py", "__name__": "h344", "open": (lambda f, *a, _o=open, _s=shuf: type("F", (), {"read": lambda self: _s})() if f.endswith("h335_106r_v7_beam.py") else _o(f, *a))}
        sys.argv = [sys.argv[0]]; exec(compile(h342, f"h342_shuf_{prefix}_{seed}", "exec"), g)
        gv, p95, null, nr, ns = g["leaf"](prefix); hits.append(gv > p95); det.append(f"{gv:.4f}/{p95:.4f}")
    k = sum(hits); void += [prefix] if k else []
    out.append(f"{prefix}: shuffled target, v7 'order signal' in {k}/3 (gain/p95: {' '.join(det)})")
out.append("read-out: " + (f"H342 VOIDED on {' '.join(void)}" if void else "H342's order statistic holds: no order signal on any shuffled target"))
txt = "\n".join(out) + "\n"; rs = f"{HERE}/h344_seqgain_shuftarget_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(rs, "w").write(txt); print(txt, end="")
