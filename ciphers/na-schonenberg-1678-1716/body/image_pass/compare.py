#!/usr/bin/env python3
"""GAPS7 2 Oct 2026: compare the image pass's settled gloss letters (settled.tsv) with the sense-side predictions
(../sense_inferences.tsv) for the 12 unsettled codes, against a control that shuffles the predictions across the
predicted positions (20 seeds, rule 3). Letters are compared under the hand's own equivalences b=v, i=y=j, c=z.
Usage: python3 compare.py [--seeds 20]"""
import csv, random, sys, os
H = os.path.dirname(os.path.abspath(__file__))
CODES = {'23','14','55','96','[blot]',')52','50','34','49','11','31','8)'}
EQ = {'v':'b','y':'i','j':'i','z':'c'}
def norm(s): return ''.join(EQ.get(ch, ch) for ch in s.lower())
seeds = int(sys.argv[sys.argv.index('--seeds')+1]) if '--seeds' in sys.argv else 20
pred = {}
for r in csv.DictReader(open(os.path.join(H,'..','sense_inferences.tsv')), delimiter='\t'):
    if r['code'] in CODES and r['sense_letter'] not in ('(none)','(unread)',''):
        pred[(r['line'], r['pos'])] = (r['code'], r['sense_letter'])
settled = {(r['line'], r['pos']): r for r in csv.DictReader(open(os.path.join(H,'settled.tsv')), delimiter='\t')}
rows = [(k, c, p, settled[k]['letter']) for k,(c,p) in sorted(pred.items()) if k in settled and settled[k]['letter'] not in ('?','')]
def score(ps): return sum(norm(p) == norm(s) for (_,_,_,s), p in zip(rows, ps))
real = score([p for _,_,p,_ in rows])
ctrl = []
for sd in range(1, seeds+1):
    ps = [p for _,_,p,_ in rows]; random.Random(sd).shuffle(ps); ctrl.append(score(ps))
for k,c,p,s in rows: print('%s\t%s\t%s\tpred=%s\tread=%s\t%s' % (k[0],k[1],c,p,s,'agree' if norm(p)==norm(s) else 'DIFFER'))
print('positions with a sense prediction and a settled letter: %d (of %d predicted)' % (len(rows), len(pred)))
print('REAL agreement %d/%d; shuffled predictions (%d seeds): mean %.2f, max %d, at or above real %d' % (
    real, len(rows), seeds, sum(ctrl)/len(ctrl), max(ctrl), sum(x >= real for x in ctrl)))
print('control values:', ctrl)
