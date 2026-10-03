#!/usr/bin/env python3
"""BIR-OPEN gate + lattice (PREREG-OPEN.md), run from this folder after oanswers_<part>.tsv exist (qid, answer = a sign id
from the sheet / OTHER / U, conf H/M/L). Per leaf:
  calibration = H decoys answered with their current sign / all H decoys (U and OTHER count as disagreement); gate >= 0.80.
  change rate = targets answered with a sheet sign different from the current one / all targets (reported).
Lattice: ../round2/r2_<leaf>_topk.tsv (24 S + H pinned), except every target position takes the TX-DECODE candidates
(../../<leaf>_topk.tsv) plus the reader's sheet answer added at weight H 0.5 / M 0.3 / L 0.1, renormalised; viterbi lam 4,
beam 64 (printed 1572 key; LM fr for f117, it16dip for f168) -> olat_<leaf>_topk.tsv, olat_<leaf>_lam4.decode.tsv.
The same lattice without reader answers is run as the baseline (oblat_...).
Survivor: target with reader answer != current, conf H or M, lattice chosen == reader answer, on a leaf whose calibration
passed AND whose posnull (oposnull.json, run separately) passes. Writes oscore.json and exceptions_open_<leaf>.tsv
(A1-BIR-VERIFY's rows + survivors)."""
import csv, json, os, sys
sys.path.insert(0, '../../../../../../tools'); import key_decode_lattice as K
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus
H = '../../../'; T = '../../'
KEY = K.read_key(H + 'key_1572_sheet.tsv'); W = {'H': 0.5, 'M': 0.3, 'L': 0.1}
LEAVES = [('f117', 'fr', ['f117a', 'f117b']), ('f168', 'it16dip', ['f168'])]
pos = list(csv.DictReader(open('opositions.tsv'), delimiter='\t'))
pn = json.load(open('oposnull.json')) if os.path.exists('oposnull.json') else {}
lat_only = '--lattice-only' in sys.argv
out = {}
for L, g, parts in LEAVES:
    ans = {}
    for p in parts:
        if os.path.exists(f'oanswers_{p}.tsv'):
            ans.update({r['qid']: r for r in csv.DictReader(open(f'oanswers_{p}.tsv'), delimiter='\t')})
    mine = [p for p in pos if p['leaf'] == L]
    dec = [p for p in mine if p['kind'] == 'hdecoy']; tg = [p for p in mine if p['kind'] == 'target']
    agree = sum(ans.get(p['qid'], {}).get('answer') == p['current'] for p in dec)
    calib = agree / len(dec)
    a_of = {(p['passage'], int(p['pos'])): ans.get(p['qid'], {}) for p in tg}
    changed = [p for p in tg if ans.get(p['qid'], {}).get('answer') in KEY and ans[p['qid']]['answer'] != p['current']]
    same = [p for p in tg if ans.get(p['qid'], {}).get('answer') == p['current']]
    tx = dict((k, c) for k, c in K.read_topk(T + L + '_topk.tsv'))
    base = K.read_topk(f'../round2/r2_{L}_topk.tsv')
    lat, blat = [], []
    for k, c in base:
        if k in a_of:
            c0 = dict(tx.get(k, c)); blat.append((k, {a: v / sum(c0.values()) for a, v in c0.items()}))
            a = a_of[k]; s = a.get('answer', '')
            if s in KEY or s.startswith('X_'):
                c0[s] = c0.get(s, 0) + W.get(a.get('conf', 'L'), 0.1)
            t = sum(c0.values()); lat.append((k, {x: v / t for x, v in c0.items()}))
        else:
            lat.append((k, c)); blat.append((k, c))
    m = NgramModel([read_corpus(p) for p in LANG_CORPORA[g]]); lm = K.LM(m)
    res = {}
    for tag, la in [('olat', lat), ('oblat', blat)]:
        with open(f'{tag}_{L}_topk.tsv', 'w') as f:
            f.write('line\tpos\tcand\tscore\n')
            for k, c in la:
                for x, v in sorted(c.items(), key=lambda kv: -kv[1]):
                    f.write(f'{k[0]}\t{k[1]}\t{x}\t{v:.4f}\n')
        seq, _ = K.viterbi(la, KEY, lm, 4.0, 64); res[tag] = dict(zip([k for k, _ in la], seq))
        with open(f'{tag}_{L}_lam4.decode.tsv', 'w') as f:
            f.write('line\tpos\tchosen\tvalue\n')
            for (k, c), s in zip(la, seq):
                f.write(f"{k[0]}\t{k[1]}\t{s}\t{KEY.get(s, '?')}\n")
    if lat_only:
        print(L, 'lattice written'); continue
    agreeing = [p for p in changed if res['olat'][(p['passage'], int(p['pos']))] == ans[p['qid']]['answer']]
    surv = [p for p in agreeing if ans[p['qid']].get('conf') in ('H', 'M')]
    g_cal = calib >= 0.80; g_pn = pn.get(L, {}).get('gate') == 'PASS'
    keep = surv if g_cal and g_pn else []
    out[L] = dict(n_hdecoy=len(dec), hdecoy_agree=agree, calibration=round(calib, 4), calib_gate='PASS' if g_cal else 'FAIL',
                  n_target=len(tg), target_same=len(same), target_changed=len(changed), change_rate=round(len(changed) / len(tg), 4),
                  target_other_or_U=len(tg) - len(same) - len(changed), lattice_agrees=len(agreeing), lattice_agrees_HM=len(surv),
                  baseline_chosen_eq_reader=sum(res['oblat'][(p['passage'], int(p['pos']))] == ans[p['qid']]['answer'] for p in changed),
                  posnull_gate=pn.get(L, {}).get('gate', 'NOT RUN'),
                  kept=[f"{p['passage']}:{p['pos']} {p['current']}->{ans[p['qid']]['answer']} ({ans[p['qid']]['conf']})" for p in keep],
                  agreeing_not_kept=[f"{p['passage']}:{p['pos']} {p['current']}->{ans[p['qid']]['answer']} ({ans[p['qid']]['conf']})" for p in agreeing if p not in keep])
    with open(f'exceptions_open_{L}.tsv', 'w') as f:
        f.write(open(f'../verify/exceptions_{L}.tsv').read())
        for p in keep:
            s = ans[p['qid']]['answer']
            f.write(f"{L}\t{p['passage']}\t{p['pos']}\t{KEY[s] or 'NULL'}\tS\tBIR-OPEN kept: open blind read {p['current']}->{s} + lattice lam 4 (calibration {calib:.2f}, posnull PASS)\n")
    print(L, {k: v for k, v in out[L].items() if not k.startswith(('kept', 'agreeing_not'))}, 'kept', len(keep))
if not lat_only:
    json.dump(out, open('oscore.json', 'w'), indent=1)
