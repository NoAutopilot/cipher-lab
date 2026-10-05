#!/usr/bin/env python3
"""RUN6-PIS (5 Oct 2026): the f.275r half of `pis1key.py relabel`, which PIS1-KEY2's run lost to a session time limit.
Same pages tuple, rule, files, seeds (run_files reseeds 20261004 per call), control and 'supported' rule as pis1key.relabel(),
imported unchanged; only the f.244r entry (already complete in relabel_run.log) is skipped.
    python3 pis1key/relabel_f275r.py   -> pis1key/relabel_result_f275r.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pis1key as P

key = P.load_key(); d = 'tx86e'; fs = ['ciphertext_f275r.tsv', 'passA.tsv', 'passB.tsv']
cl, drop, err, rule = 'kp86d/colbert_p121_123.txt', 'Mais croyant que Monsieur de Luxembourg', 0.215, P.sub_all('T36')
clear, ptext = P.clear_of(cl, drop)
old = [f'{d}/{f}' for f in fs]
new = [P.relabel_file(f'{d}/{f}', f'pis1key/tx_relabel/{d}_{f}', rule) for f in fs]
r = {"err": err, "old": P.run_files(key, old, clear), "new": P.run_files(key, new, clear)}
v = P.relabel_file(old[0], 'pis1key/tx_relabel/tx86e_ciphertext_f275r_mergecut.tsv', P.merge_cut)
r["descriptive_mergecut"] = P.run_files(key, [v], clear)
r["positive_control"] = P.control(key, ptext, clear, err, r["new"][new[0]]["decoded_letters"])
print('f275r control', r["positive_control"]["passed"], '/5', flush=True)
r["supported"] = bool(r["new"][new[0]]["score"] > r["old"][old[0]]["score"] and r["new"][new[0]]["above_both"])
r["would_be_identical"] = P.identical(new[0], cl, key, {'T31': 'T36'})
json.dump({"f275r": r}, open(os.path.join(P.H, 'relabel_result_f275r.json'), 'w'), indent=1)
