#!/usr/bin/env python3
"""f.21v depth gap (D2-CEP21M, 8 Oct 2026): for each token that breaks a primary H/C/S run (M, U, I, or a NULL/code-class
sign), the run to its left and right inside its passage and the merged run if that token alone were S, beside the AD
from tools/depth_stats.py (summary.json). Runs never cross a passage (prose stands between passages; --break-lines).
Usage: python3 depth_gap.py SUMMARY.json  (writes depth_gap.tsv beside this script; --check exits 1 if it is stale)."""
import csv, json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); HV = os.path.dirname(H)
summ = json.load(open(sys.argv[1])) if len(sys.argv) > 1 and sys.argv[1] != '--check' else None
toks = list(csv.DictReader(open(os.path.join(HV, 'reading_f21v_tokens.tsv')), delimiter='\t'))
pair = {}
for r in csv.DictReader(open(os.path.join(H, 'lookalike', 'confusion.tsv')), delimiter='\t'):
    for ex in r['examples'].split():
        if ex.startswith('f21v:'):
            pair[ex[5:]] = r['label_a'] + '/' + r['label_b']
def letters(t):
    if t['grade'] == 'U' or t['value'] in ('NULL', '?', ''):
        return 0
    return len(t['value'])
def ok(t):
    return t['grade'] in ('H', 'C', 'S') and t['value'] != 'NULL'
AD = summ['AD'] if summ else None; AD34 = summ['AD_R3_4'] if summ else None
rows = []
for i, t in enumerate(toks):
    if ok(t):
        continue
    L = R = 0; j = i - 1
    while j >= 0 and toks[j]['line'] == t['line'] and ok(toks[j]):
        L += letters(toks[j]); j -= 1
    j = i + 1
    while j < len(toks) and toks[j]['line'] == t['line'] and ok(toks[j]):
        R += letters(toks[j]); j += 1
    merged = L + letters(t) + R
    plen = sum(letters(x) for x in toks if x['line'] == t['line'])
    tid = '%s.%s' % (t['line'], t['pos'])
    rows.append([tid, t['sign'], t['value'], t['grade'], pair.get(tid, ''), L, R, merged, plen])
out = os.path.join(H, 'depth_gap.tsv')
hdr = ['token', 'sign', 'value', 'grade', 'confusion_pair', 'run_left', 'run_right', 'merged_if_S', 'passage_letters']
lines = ['\t'.join(hdr)] + ['\t'.join(map(str, r)) for r in rows]
txt = '\n'.join(lines) + '\n'
if '--check' in sys.argv:
    sys.exit(0 if open(out).read().split('\n# ')[0].rstrip('\n') == txt.rstrip('\n') else 1)
foot = '# AD %.1f letters (R %.3f, fr16); AD at R=3.4 %.1f; longest primary run %d; max merged %d; longest passage %d letters\n' % (
    AD, summ['R'], AD34, summ['primary_run'], max(r[7] for r in rows), max(r[8] for r in rows))
open(out, 'w').write(txt + foot)
print(foot.strip())
