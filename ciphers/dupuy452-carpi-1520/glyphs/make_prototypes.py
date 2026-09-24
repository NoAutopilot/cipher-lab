#!/usr/bin/env python3
"""One-shot: build prototypes.npz (the labelled shape exemplars classify.py matches against) from
the by-eye labelling of cluster.py's run on the 5776-sign segmentation of 23 Sept 2026
(cluster_labels_run1.json + manual_labels_run1.json). For each labelled pure cluster the core
members (distance to the k-means centre below the cluster median, at most 60) are kept; every
manually labelled sign is kept. Stores the bitmap and the raw size/placement values, so the
prototypes stay valid when segment.py changes.

PROVENANCE ONLY: prototypes.npz is the frozen artefact classify.py uses. This script needs the
run-1 segmentation (signs_run1.tsv / clusters_run1.tsv, 5776 signs, and the signs_bitmaps.npz and
all_signs() of segment.py as it stood before the slope fit, background normalisation and rule
removal were added later on 23 Sept 2026), so it will not rerun against the current segment.py;
it records how each prototype was chosen."""
import csv, json, os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, "signs_run1.tsv")), delimiter="\t"))
assert len(rows) == 5776, "prototypes are defined on the 5776-sign run"
bm = np.load(os.path.join(HERE, "signs_bitmaps.npz"))["bm"]
lines = {(r["page"], r["line"]): float(r["y_centre"]) for r in csv.DictReader(open(os.path.join(HERE, "lines.tsv")), delimiter="\t")}
cl = list(csv.DictReader(open(os.path.join(HERE, "clusters_run1.tsv")), delimiter="\t"))
cmap = {k: v for k, v in json.load(open(os.path.join(HERE, "cluster_labels_run1.json"))).items() if not k.startswith("_")}
man = {k: v for k, v in json.load(open(os.path.join(HERE, "manual_labels_run1.json"))).items() if not k.startswith("_")}
manual = {s: lab for lab, ss in man.items() for s in ss}
pick = {}
by = {}
for c in cl:
    by.setdefault(c["cluster"], []).append((float(c["dist"]), int(c["sid"])))
for k, mem in by.items():
    lab = cmap[k]
    if lab == "MIX":
        continue
    mem.sort()
    for d, s in mem[:min(60, max(3, len(mem) // 2))]:
        if s not in manual:
            pick[s] = lab
pick.update(manual)
# second-round labels keyed page/line/x
key = {(r["page"], int(r["line"]), int(r["x"])): int(r["sid"]) for r in rows}
for lab, ks in json.load(open(os.path.join(HERE, "manual_labels_run2.json"))).items():
    if lab.startswith("_"):
        continue
    for p, l, x in ks:
        pick[key[(p, l, x)]] = lab
# third round: single-type by-eye settlements in overrides.tsv (unsplit signs only)
for o in csv.DictReader((l for l in open(os.path.join(HERE, "overrides.tsv")) if not l.startswith("#")), delimiter="\t"):
    k = (o["page"], int(o["line"]), int(o["x"]))
    if k in key and "," not in o["type"] and o["type"] not in ("?", "DROP"):
        pick[key[k]] = o["type"]
    elif k in key and o["type"] == "DROP":
        pick[key[k]] = "FRAG"
# Del prototypes that enclose no hole are carets (cluster 61 mixed the two): relabel lam
import sys
sys.path.insert(0, HERE)
import classify, segment
_signs, _ = segment.all_signs()
for s_, lab in list(pick.items()):
    if lab == "Del" and classify.holes(_signs[s_]["mask"]) == 0:
        pick[s_] = "lam"
sids = sorted(pick)
assert all(int(_signs[k]["x"]) == int(rows[k]["x"]) for k in sids)
out = dict(sid=np.array(sids), label=np.array([pick[s] for s in sids]), bm=bm[sids],
           h=np.array([float(rows[s]["h"]) for s in sids]), w=np.array([float(rows[s]["w"]) for s in sids]),
           dy=np.array([float(rows[s]["y"]) + float(rows[s]["h"]) / 2 - _signs[s]["line_y"] for s in sids]))
np.savez_compressed(os.path.join(HERE, "prototypes.npz"), **out)
from collections import Counter
print(len(sids), "prototypes", sorted(Counter(out["label"]).items(), key=lambda x: -x[1]))
