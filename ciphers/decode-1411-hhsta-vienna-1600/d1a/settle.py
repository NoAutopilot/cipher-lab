#!/usr/bin/env python3
"""D1A-D1411: apply PREREG-D1A-D1411.md's settlement rule to d1a/blind_read.tsv via d1a/tile_key.tsv; exemplar control;
write d1a/settled.tsv. Rule order: control gate; U if either primary read matches neither candidate of its op; S1 both primary
reads equal (sure on >= 1); S2 one read sure = its own transcription and the other unsure with that value or its own
transcription as alternative; S3 both sure, each = own transcription, differing; else U.
  python3 d1a/settle.py [--check]"""
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: list(csv.DictReader(open(os.path.join(H, p)), delimiter="\t"))
K = {r["id"]: r for r in rd("tile_key.tsv")}; B = {r["id"]: r for r in rd("blind_read.tsv")}
ex = [i for i, k in K.items() if k["kind"] == "E"]; hit = sum(B[i]["read"] == K[i]["value"] for i in ex)
acc = hit / len(ex); lines = [f"# exemplar control {hit}/{len(ex)} = {acc:.3f} (gate 0.80): {'PASS' if acc >= .8 else 'NON-TEST'}"]
ops = {}
for i, k in K.items():
    if k["kind"] == "D": ops.setdefault(k["op"], {})[k["copy"]] = (i, k, B[i])
lines.append("op\tp2_line\tp2_pos\tp2_tx\tp2_tile\tp2_read\tp2_conf\tp2_alt\tp5_line\tp5_pos\tp5_tx\tp5_tile\tp5_read\tp5_conf\tp5_alt\tclass\tsettled")
for o in sorted(ops):
    (i2, k2, b2), (i5, k5, b5) = ops[o]["p2"], ops[o]["p5"]; cand = {k2["value"], k5["value"]}
    if acc < .8: c, v = "NON-TEST", ""
    elif b2["read"] not in cand or b5["read"] not in cand: c, v = "U", ""
    elif b2["read"] == b5["read"] and "sure" in (b2["conf"], b5["conf"]): c, v = "S1", b2["read"]
    elif b2["conf"] == "sure" and b5["conf"] == "sure" and b2["read"] == k2["value"] and b5["read"] == k5["value"]: c, v = "S3", ""
    else:
        c, v = "U", ""
        for (bs, ks), (bo, ko) in (((b2, k2), (b5, k5)), ((b5, k5), (b2, k2))):
            if bs["conf"] == "sure" and bs["read"] == ks["value"] and bo["conf"] == "unsure" and ks["value"] in (bo["read"], bo["alt"]):
                c, v = "S2", ks["value"]
    lines.append("\t".join([o, k2["line"], k2["pos"], k2["value"], i2, b2["read"], b2["conf"], b2["alt"],
                            k5["line"], k5["pos"], k5["value"], i5, b5["read"], b5["conf"], b5["alt"], c, v]))
txt = "\n".join(lines) + "\n"; out = os.path.join(H, "settled.tsv")
if "--check" in sys.argv:
    sys.exit(0 if open(out).read() == txt else (print("STALE settled.tsv") or 1))
open(out, "w").write(txt); print(txt)
