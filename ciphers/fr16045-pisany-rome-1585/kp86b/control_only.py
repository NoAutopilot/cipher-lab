#!/usr/bin/env python3
"""Finish a kp86b.py run that was stopped by the session's 30-min background limit after its target scores: runs only
the positive control of one arm, with kp86b.control() unchanged (same seeds 500-504, same e), and merges it with the
logged target rows into the result JSON. Usage: control_only.py ARM ERR LOG OUT"""
import json, os, re, sys, ast
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from kp86b import control, load_key, norm, REMAP_B
arm, err, log, out = sys.argv[1], float(sys.argv[2]), sys.argv[3], sys.argv[4]
ctext = norm(open(os.path.join(H, 'colbert_p51_52.txt')).read())
clear = np.array([ord(c) - 97 for c in ctext], dtype=np.int64)
key = load_key()
if arm == 'B':
    key.update(REMAP_B)
res = {}
for ln in open(log):
    m = re.match(r'^(A|B) (\S+) (\{.*\})$', ln.strip())
    if m and m.group(1) == arm:
        res[m.group(2)] = ast.literal_eval(m.group(3))
res['positive_control'] = control(key, ctext, clear, err)
print(arm, 'control', res['positive_control'])
p = os.path.join(H, out)
J = json.load(open(p)) if os.path.exists(p) else {"clear_letters": len(clear), "err": err, "remap_B": REMAP_B,
                                                    "note": "assembled by control_only.py from the logged target rows"}
J['arm_' + arm] = res
json.dump(J, open(p, 'w'), indent=1)
