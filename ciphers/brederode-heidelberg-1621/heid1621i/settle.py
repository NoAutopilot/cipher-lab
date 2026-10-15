#!/usr/bin/env python3
"""HEID-1621I (PREREG-HEID1621I.md): fold this worker's eye re-read of the 22 split letter positions (heid1621i/reread_letters.tsv, made on
the native line crops re-derived by regen_crops.sh) into tools/lookalike_pass.py reconcile's fixed 2-of-3 rule, then re-run the 375-vs-379
unit control (45 aligned units; numbers agree 96/96, so a unit agrees iff its letter agrees, case kept). No value is read; nothing decodes.
usage: python3 settle.py [--check]   (--check rebuilds in a temp dir and exits 1 if a committed output differs)
"""
import csv, json, os, subprocess, sys, tempfile, filecmp
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, '..', 'heid1621h'); TOOL = os.path.join(H, '..', '..', '..', 'tools', 'lookalike_pass.py')
# within-witness tile -> (witness, aligned unit) whose reconciled letter it may change (PREREG: only if the reconciled letter lost)
UNIT = {('w375_L05', 3): ('375', 12), ('w375_L07', 1): ('375', 22), ('w375_L07', 4): ('375', 23), ('w375_L11', 7): ('375', 37),
        ('w379_L02', 7): ('379', 2), ('w379_L02', 10): ('379', 3), ('w379_L03', 12): ('379', 8), ('w379_L05', 9): ('379', 12),
        ('w379_L05', 15): ('379', 14), ('w379_L06', 1): ('379', 15), ('w379_L07', 11): ('379', 23), ('w379_L10', 12): ('379', 33),
        ('w379_L12', 5): ('379', 38)}

def rd(p): return list(csv.DictReader(open(p), delimiter='\t'))

def build(out):
    r = subprocess.run([sys.executable, TOOL, 'reconcile', '--tiles', os.path.join(P, 'tiles_letters.tsv'), '--passc', os.path.join(P, 'passC_letters.tsv'),
                        '--reread', os.path.join(H, 'reread_letters.tsv'), '--out', os.path.join(out, 'passD_letters.tsv'),
                        '--focus', os.path.join(out, 'focus_tool.tsv')], capture_output=True, text=True, check=True).stdout.strip()
    pd = {(x['passage'], int(x['pos'])): x for x in rd(os.path.join(out, 'passD_letters.tsv'))}
    tiles = rd(os.path.join(P, 'tiles_letters.tsv'))
    cross = {int(x['posA']): [x['idA'], x['idB']] for x in rd(os.path.join(P, 'agreement_letters.tsv')) if x['passage'] == 'x375_379'}
    before = sum(a == b for a, b in cross.values())
    settled, unsettled, changes = [], [], []
    for t in tiles:
        k = (t['passage'], int(t['pos'])); d = pd[k]
        if d['note'] == 'lookalike UNSETTLED': unsettled.append(t); continue
        settled.append((t, d['sign_id']))
        if t['passage'] == 'x375_379':
            u = int(t['pos']); old = list(cross[u]); cross[u] = [d['sign_id'], d['sign_id']]; changes.append(f"unit {u}: {old[0]}/{old[1]} -> both {d['sign_id']}")
        else:
            if k not in UNIT: continue  # 423 has no second witness: no control unit
            w, u = UNIT[k]; i = 0 if w == "375" else 1
            if cross[u][i] != d['sign_id']: changes.append(f"unit {u} ({w}): reconciled {cross[u][i]} -> {d['sign_id']}"); cross[u][i] = d['sign_id']
    after = sum(a == b for a, b in cross.values())
    res = dict(reconcile=r, tiles=len(tiles), settled=len(settled), unsettled=len(unsettled),
               settled_labels={f"{t['passage']}.{t['pos']}": s for t, s in settled}, control_changes=changes,
               control_before=f"{before}/45", control_after=f"{after}/45", control_agreement=round(after / 45, 3), control_gate=0.90,
               control_pass=after / 45 >= 0.90, misses_after=[f"{u}: 375 {a} / 379 {b}" for u, (a, b) in sorted(cross.items()) if a != b])
    open(os.path.join(out, 'settle_result.json'), 'w').write(json.dumps(res, indent=1) + '\n')
    rr = {(x['passage'], int(x['pos'])): x for x in rd(os.path.join(H, 'reread_letters.tsv'))}
    with open(os.path.join(out, 'focus.tsv'), 'w') as f:
        for t in unsettled:
            n = rr[(t['passage'], int(t['pos']))]['note']
            f.write(f"heid1621i_{t['passage']}_{t['pos']}\t{t['passage']}.{t['pos']}: readers {t['A']}/{t['B']}; eye: {n}; which of {', '.join(sorted({t['A'], t['B']}))}, or another sign?\n")
        f.write("heid1621i_w379_L07_8\tw379_L07.8 (46.47, both readers f, not a split tile): the eye sees a tall long-s without crossbar, the shape settled s at 375 L07.1 and unit 27; f or s?\n")
        f.write("heid1621i_class_64_65\tthe sign after 64.65 (375 L05/L07/L11, 379 L06/L08/L12): one curled sign throughout, named x on 375 and c on 379; is it x, c, or its own sign (distinct from the 22.23 x and the 76.77 plain c)?\n")

OUTS = ['passD_letters.tsv', 'focus_tool.tsv', 'settle_result.json', 'focus.tsv']
if __name__ == '__main__':
    if '--check' in sys.argv:
        with tempfile.TemporaryDirectory() as t:
            build(t); bad = [o for o in OUTS if not filecmp.cmp(os.path.join(t, o), os.path.join(H, o), shallow=False)]
            print('stale:' if bad else 'ok', *bad); sys.exit(1 if bad else 0)
    build(H); print(open(os.path.join(H, 'settle_result.json')).read())
