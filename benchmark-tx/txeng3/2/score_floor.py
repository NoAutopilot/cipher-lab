#!/usr/bin/env python3
"""TXE3-2 FLOOR scorer (11 Oct 2026): maps the blind classifier's answers (items/<line>/answer.json) to the PREREG-txeng3-2 cause
classes and instruments, computes the control's invented-cause rate and the gate, and writes floor.tsv + a markdown block.
Mapping and statistic exactly as PREREG-txeng3-2.md steps 5-7; the key (floor/control, truth, reads) is joined here, never shown
to a subagent."""
import csv, json, sys, math
from pathlib import Path
from collections import Counter
OUT = Path(__file__).resolve().parent
key = {(r['call'], r['label']): r for r in csv.DictReader((l for l in open(OUT / 'key.tsv') if not l.startswith('#')), delimiter='\t')}
items = {(r['call'], r['label']): r for r in csv.DictReader(open(OUT / 'items.tsv'), delimiter='\t')}
BAD_Q4 = {'abbreviation', 'ampersand', 'struck', 'correction', 'illegible'}

def readers_sign(reads):
    rs = [x for x in reads.split('|') if x and x != '<deleted>']
    return Counter(rs).most_common(1)[0][0] if rs else '<deleted>'

def classify(a, k):
    truth = set(k['truth'].split('|')); rsign = readers_sign(k['reads'])
    cand = [a.get('q3_top1', ''), a.get('q3_top2', '')]
    q1, q2, q4 = a.get('q1', ''), a.get('q2', ''), a.get('q4_issue', 'none')
    hard = str(a.get('hard_pair', '')).lower() == 'true'
    deleted = '<deleted>' in k['reads']
    if q1 in ('cut', 'joined'):
        cls, pair = 'i', ''
    elif q4 in BAD_Q4 or str(a.get('q4_legible', 'true')).lower() == 'false':
        cls, pair = 'iii', ''
    elif q2 in ('faint', 'damaged', 'struck-or-overwritten'):
        cls, pair = 'iv', ''
    elif rsign in cand and (truth & set(cand)) and rsign not in truth:
        cls, pair = 'ii', f"{rsign}~{sorted(truth & set(cand))[0]}"
    elif hard and (rsign in cand or (truth & set(cand))):
        cls, pair = 'ii', f"{cand[0]}~{cand[1]}"
    else:
        cls, pair = 'v', ''
    if cls == 'iii' and k['flag']:
        cls = 'iii-flagged'
    truth_in_top2 = bool(truth & set(cand))
    instr = {'i': 'box check', 'ii': 'owner sorter question' + (' + key-constrained decode (truth in top-2)' if truth_in_top2 else ''),
             'iii': 'truth verifier', 'iii-flagged': 'none (already flagged)', 'iv': 'owner sorter question', 'v': 'none'}[cls]
    if deleted and cls != 'i': instr += '; deletion in some passes: box check beside'
    invented = (q1 != 'whole') or (q2 != 'clean') or (q4 in BAD_Q4) or (str(a.get('q4_legible', 'true')).lower() == 'false') or (cand[0] not in truth)
    return cls, pair, instr, invented, truth_in_top2, rsign

rows = []
for (call, lab), k in sorted(key.items()):
    f = OUT / 'items' / call / 'answer.json'
    a = {}
    if f.exists():
        try:
            for o in json.load(open(f)):
                if o.get('label') == lab: a = o
        except Exception as e:
            print('bad json', f, e, file=sys.stderr)
    if not a:
        rows.append(dict(call=call, label=lab, kind=k['kind'], line=k['line'], pos=k['pos'], plain=k['plain'], truth=k['truth'], reads=k['reads'], flag=k['flag'], classified='no')); continue
    cls, pair, instr, inv, tit, rs = classify(a, k)
    rows.append(dict(call=call, label=lab, kind=k['kind'], line=k['line'], pos=k['pos'], plain=k['plain'], truth=k['truth'], reads=k['reads'], flag=k['flag'],
                     classified='yes', readers_sign=rs, q1=a.get('q1'), q2=a.get('q2'), q3_top1=a.get('q3_top1'), q3_conf1=a.get('q3_conf1'), q3_top2=a.get('q3_top2'), q3_conf2=a.get('q3_conf2'),
                     hard_pair=a.get('hard_pair'), q4_word=a.get('q4_word'), q4_legible=a.get('q4_legible'), q4_issue=a.get('q4_issue'), q5=a.get('q5'),
                     cause_class=cls, pair=pair, instrument=instr, invented_cause=int(inv), truth_in_top2=int(tit),
                     prior_readfree_class=k['err_class']))
cols = ['call','label','kind','line','pos','plain','truth','reads','flag','classified','readers_sign','q1','q2','q3_top1','q3_conf1','q3_top2','q3_conf2','hard_pair','q4_word','q4_legible','q4_issue','q5','cause_class','pair','instrument','invented_cause','truth_in_top2','prior_readfree_class']
with open(OUT / 'floor.tsv', 'w') as f:
    f.write('# TXE3-2 FLOOR (11 Oct 2026): 18 no.87 floor positions (wrong in all six of L A B C E F) + 18 same-line right-sign controls, classified blind by one Sonnet call per line from tile + marked crop + clerk sheet crops + value-blind sign sheet; mapping PREREG-txeng3-2.md step 5; invented_cause per step 6.\n')
    w = csv.DictWriter(f, fieldnames=cols, delimiter='\t', extrasaction='ignore'); w.writeheader(); w.writerows(rows)

def fisher(a, b, c, d):
    # two-sided Fisher exact for [[a,b],[c,d]]
    from math import comb
    n = a + b + c + d; r1 = a + b; c1 = a + c
    def p(x): return comb(r1, x) * comb(n - r1, c1 - x) / comb(n, c1)
    p0 = p(a); return sum(p(x) for x in range(max(0, c1 - (n - r1)), min(r1, c1) + 1) if p(x) <= p0 + 1e-12)

fl = [r for r in rows if r['kind'] == 'floor' and r['classified'] == 'yes']
ct = [r for r in rows if r['kind'] == 'control' and r['classified'] == 'yes']
inv_c = sum(r['invented_cause'] for r in ct); inv_f = sum(r['invented_cause'] for r in fl)
caused_f = sum(1 for r in fl if r['cause_class'] != 'v')
print(f"classified: floor {len(fl)}/18, control {len(ct)}/18")
print(f"control invented-cause rate: {inv_c}/{len(ct)} = {inv_c/max(1,len(ct)):.3f}  (gate <= 0.25); floor any-cause {caused_f}/{len(fl)}; floor invented-by-same-rule {inv_f}/{len(fl)}")
if fl and ct:
    print(f"Fisher two-sided (floor cause vs control invented): p = {fisher(caused_f, len(fl)-caused_f, inv_c, len(ct)-inv_c):.4f}")
    print("control breakdown: q1!=whole", sum(r['q1']!='whole' for r in ct), "q2!=clean", sum(r['q2']!='clean' for r in ct), "q4 issue", sum((r['q4_issue'] in BAD_Q4) or str(r['q4_legible']).lower()=='false' for r in ct), "top1 not in truth", sum(r['q3_top1'] not in set(r['truth'].split('|')) for r in ct), "hard_pair", sum(str(r['hard_pair']).lower()=='true' for r in ct))
    print("floor breakdown:   q1!=whole", sum(r['q1']!='whole' for r in fl), "q2!=clean", sum(r['q2']!='clean' for r in fl), "q4 issue", sum((r['q4_issue'] in BAD_Q4) or str(r['q4_legible']).lower()=='false' for r in fl), "top1 not in truth", sum(r['q3_top1'] not in set(r['truth'].split('|')) for r in fl), "hard_pair", sum(str(r['hard_pair']).lower()=='true' for r in fl), "truth in top2", sum(r['truth_in_top2'] for r in fl), "top1 == readers' sign", sum(r['q3_top1']==r['readers_sign'] for r in fl))
    print("\nfloor classes:", Counter(r['cause_class'] for r in fl).most_common())
    print("control classes:", Counter(r['cause_class'] for r in ct).most_common())
    print("\n| line | pos | plain | truth set | reads L A B C E F | flag | q1 | q2 | top1/top2 (hard) | clerk word / issue | class | pair | instrument |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in fl:
        print(f"| {r['line']} | {r['pos']} | {r['plain']} | {r['truth']} | {r['reads'].replace('|',' ')} | {r['flag'] or '-'} | {r['q1']} | {r['q2']} | {r['q3_top1']}({r['q3_conf1']})/{r['q3_top2']}({r['q3_conf2']}) ({'hard' if str(r['hard_pair']).lower()=='true' else 'clear'}) | {r['q4_word']} / {r['q4_issue']}{'' if str(r['q4_legible']).lower()!='false' else ' (illegible)'} | {r['cause_class']} | {r['pair']} | {r['instrument']} |")
    print("\ninstruments over floor (expected err_true drop if every position the instrument reaches were fixed):")
    byi = Counter(); byi_unfl = Counter()
    for r in fl:
        for tag in ('box check', 'owner sorter question', 'key-constrained decode', 'truth verifier'):
            if tag in r['instrument']:
                byi[tag] += 1
                if not r['flag']: byi_unfl[tag] += 1
    for tag, n in byi.most_common():
        print(f"  {tag}: {n} positions -> as measured -{n/803:.4f} ({n}/803); flagged-excluded -{byi_unfl[tag]/792:.4f} ({byi_unfl[tag]}/792)")
