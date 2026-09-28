#!/usr/bin/env python3
"""F61-FAMILY-5 (28 Sept 2026): write the per-call prompt files passes/prompts_f5/<OUT>_<chunk>_<pass>.txt from
passes/PROMPTS_f124r_gloss.md (letter pass template) and sheets/<OUT>_segments.json.
  python3 gen_prompts_f5.py OUT CHUNK SEGMENT1,SEGMENT2,...   (segment stems, at most 8; passes A and B written)"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
out, chunk, stems = sys.argv[1], sys.argv[2], sys.argv[3].split(",")
WORDS = "--words" in sys.argv   # the word-span template (knob change, 05:2x UTC)
src = open(f"{P}/PROMPTS_f124r_gloss.md").read()
tpl = src[src.index("## Letter pass template") + len("## Letter pass template"):src.index("## f.97r sign passes")].strip()
if WORDS: tpl = src[src.index("## Word-span pass template") + len("## Word-span pass template"):].strip()
J = json.load(open(f"{HERE}/sheets/{out}_segments.json")); by = {s["file"].replace(".jpg", ""): s for s in J["segments"]}
os.makedirs(f"{P}/prompts_f5", exist_ok=True)
segs = [by[s] for s in stems]
paths = "\n".join(f"{HERE}/sheets/{out}/{s['file']}" for s in segs)
skel = "\n".join(f"{s['file'].replace('.jpg','')}: " + " ".join(f"{i}:{'?' if v == '?' else '[' + v + ']'}" for i, v in s["shown"]) for s in segs)
for pas in "AB":
    o = f"{P}/{out}_{'words' if WORDS else 'letters'}{pas}_{chunk}.tsv"
    t = tpl.replace("{ns}", str(len(segs))).replace("{segs}", ", ".join(stems)).replace("{paths}", paths).replace("{skeletons}", skel).replace("{out}", o)
    open(f"{P}/prompts_f5/{out}_{chunk}_{pas}.txt", "w").write(t + "\n")
print("written", chunk, len(segs), "segments")
