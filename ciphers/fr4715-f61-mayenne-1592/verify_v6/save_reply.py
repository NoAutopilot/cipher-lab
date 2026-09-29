#!/usr/bin/env python3
"""Save a subagent's hand-back text verbatim: python3 save_reply.py TRANSCRIPT PREFIX OUT (finds the last handback 'message' starting PREFIX)."""
import json, sys
def walk(o, acc, pre):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "message" and isinstance(v, str) and v.startswith(pre): acc.append(v)
            else: walk(v, acc, pre)
    elif isinstance(o, list):
        for v in o: walk(v, acc, pre)
acc = []
for l in open(sys.argv[1]):
    try: walk(json.loads(l), acc, sys.argv[2].encode().decode("unicode_escape"))
    except ValueError: pass
open(sys.argv[3], "w").write(acc[-1].strip() + "\n"); print(sys.argv[3], len(acc[-1].strip().splitlines()))
