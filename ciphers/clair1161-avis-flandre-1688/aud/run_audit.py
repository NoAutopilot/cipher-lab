#!/usr/bin/env python3
"""D2-C1161AUD (5 Oct 2026): planted agreed-token audit on th/z/S/4 (tools/lookalike_pass.py audit, TX-AGREEAUDIT).
The tool's audit() draws from every agreed position; this wrapper only narrows the pool to positions the merged
transcription (la/passC.tsv) labels th, z, S or 4 and both blind readers agreed on, taken from la/align_abc.tsv
(D2-C1161LA's per-line A/B/C alignment, status 'agree'), by replacing lookalike_pass.agreed_positions for this call.
Everything else (seeded sample, plants = most frequent confusion partner from la/confusion.tsv, k candidates) is the tool's.
  python3 aud/run_audit.py      (from the target folder or anywhere; writes aud/c1161aud_audit_items.tsv + prompt)
"""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import lookalike_pass as lp
TG = {"th", "z", "S", "4"}
AG = {(r["passage"], int(r["pos"])) for r in csv.DictReader(open(os.path.join(T, "la", "align_abc.tsv")), delimiter="\t")
      if r["status"] == "agree" and r["merged"] in TG}

def agreed(passa, passb, passc):
    return [(ln, pos, s, (ln, pos) in AG) for ln, pos, s in lp._norm(os.path.join(T, "la", "passC.tsv"))]

lp.agreed_positions = agreed
pc = os.path.join(T, "la", "passC.tsv")
smap = os.path.join(HERE, "empty_sheet_map.json"); json.dump([], open(smap, "w"))
print(lp.audit(pc, pc, pc, os.path.join(T, "la", "confusion.tsv"), sample=120, plant=0.17, seed=51, k=3, include=None,
               crops_glob=None, sheet=os.path.join(HERE, "none.png"), sheet_map=smap, out=HERE, run="c1161aud",
               hide_passc=True))
print("agreed th/z/S/4 pool:", len(AG))
