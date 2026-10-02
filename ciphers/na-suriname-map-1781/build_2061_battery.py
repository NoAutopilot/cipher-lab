#!/usr/bin/env python3
"""Build ciphertext_2061_battery.tsv from the two blind passes and the reconciliation (GAPS8-na-suriname-map-1781,
2 Oct 2026). Inputs in passes/: bat2061_draft.tsv (tools/reconcile_passes.py ciphertext_draft.tsv over the two passes,
after the code-synonym map below), bat2061_disagreements.tsv, bat2061_recon_list.tsv (the 48 non-trivial
disagreements handed to the reconciler) and bat2061_reconC.tsv (its decisions).

conf H = both blind passes read the same sign; M = the passes differed and the reconciler settled it (A, B or its own
reading); a trivial disagreement (a word gap, 0/o, w/[w-loop], m/[m-loop]) keeps pass A's sign at M. Plain material is
written 'w:<text>' (decode_key.py's clear-word prefix): "No", the battery number, a digit standing directly before
[MM] (a gun count), and the label letters. Digits inside a cipher word stay signs. Usage: python3 build_2061_battery.py
"""
import csv, os
here = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(here, 'passes')
def rd(f): return list(csv.DictReader(open(os.path.join(P, f)), delimiter='\t'))
draft = rd('bat2061_draft.tsv'); dis = rd('bat2061_disagreements.tsv')
rl = {(r['band'], r['context_before'], r['A_reads'], r['B_reads']): r['id'] for r in rd('bat2061_recon_list.tsv')}
rc = {r['id']: r for r in rd('bat2061_reconC.tsv')}
disc = {(r['line'], r['col']): r for r in dis}
byline = {}
for r in draft: byline.setdefault(r['line'], []).append(r)
out = []
for line, L in byline.items():
    for i, r in enumerate(L):
        sign, conf, note = r['sign'], 'H', ''
        d = disc.get((line, r['position']))
        if d:
            bef = ' '.join(x['sign'] for x in L[max(0, i - 5):i])
            rid = rl.get((line, bef, d['A'], d['B']))
            if rid and rid in rc:
                c = rc[rid]; sign = c['sign']; conf = 'M'
                note = f"{rid}: A {d['A']} / B {d['B']} -> {c['decision']} ({c['conf']}) {c['note']}".strip()
            else:
                sign = d['A'] if d['A'] != '-' else d['B']; conf = 'M'; note = f"trivial: A {d['A']} / B {d['B']}"
        out.append([line, sign, conf, note])
# battery lines (L01-L06): a weight group (digits then "9 d", read "24gd"/"12gd" on the sheet) is plain, as is a word
# that is a lone digit or begins with "1" before a cipher word (a gun count: "3. bgrtha", "1.rf..."); "0" is the
# plain-circle sign both readers also wrote "o". A word-initial 5 is NOT plain ("5 [delta] h" is the header's "van").
def battery_plain(out):
    words = {}
    for k, (line, sign, conf, note) in enumerate(out):
        if line > 'L06': continue
        w = sum(1 for o in out[:k] if o[0] == line and o[1] in ('|', '-'))
        if sign not in ('|', '-'): words.setdefault((line, w), []).append(k)
    for (line, w), ks in words.items():
        sg = [out[k][1] for k in ks]
        if len(sg) >= 3 and sg[-2:] == ['9', 'd'] and all(x.isdigit() for x in sg[:-1]):
            for k in ks: out[k][1] = 'w:' + out[k][1]
        elif len(sg) == 1 and sg[0].isdigit():
            out[ks[0]][1] = 'w:' + sg[0]
        elif len(sg) > 1 and sg[0] == '1' and not sg[1].isdigit():
            out[ks[0]][1] = 'w:1'
        # "[delta] 6 9 d" / "6 9 d t [psi] 3 0" / "3 9 d w:. t ...": a weight group inside a longer word
        for i in range(len(sg) - 2):
            if sg[i].isdigit() and sg[i + 1] == '9' and sg[i + 2] == 'd' and not out[ks[i]][1].startswith('w:'):
                j = i
                while j > 0 and sg[j - 1].isdigit(): j -= 1
                for k in ks[j:i + 3]: out[k][1] = 'w:' + out[k][1]
    for o in out:
        if o[1] == '0': o[1] = 'o'
out = [list(o) for o in out]
# GAPS12 (2 Oct 2026): sign codes settled by a blind image comparison (one vision call, unlabelled tiles vs 2007A's key
# y and look-alikes; NOTES.md "GAPS12"). Applied after positions are counted; conf stays M.
IMAGE_SETTLED = {
    ('2061_bat_L08', 45): ('v', 'GAPS12 image check: same sign as 2061 v (L08 pos50) and 2007A L2 v of glossed v3=de, not 2007A key y (0.80)'),
    ('2061_bat_L09', 3): ('[y-dots]', 'GAPS12 image check: same sign as 2007A L2 two-dot long-descender y, not 2007A key y (0.85)'),
}
battery_plain(out)
# word index, plain marking
rows = []; word = 0; prev = None
for k, (line, sign, conf, note) in enumerate(out):
    if line != prev: word = 0; prev = line; first = True
    if sign in ('|', '-', ''):
        word += 1; continue
    s = sign
    if s.startswith('w:'):
        pass
    elif s.startswith('<') and s.endswith('>'):
        s = 'w:' + s[1:-1]
    elif s.isdigit():
        nxt = next((o[1] for o in out[k + 1:] if o[0] == line and o[1] not in ('|', '-')), '')
        prv = [o[1] for o in out[:k] if o[0] == line and o[1] not in ('|', '-')]
        if nxt == '[MM]' or (prv and prv[-1] == '<No>'):
            s = 'w:' + s
    rows.append([f'2061_bat_{line}', s, conf, note, word])
with open(os.path.join(here, 'ciphertext_2061_battery.tsv'), 'w') as f:
    f.write("# NA 4.VEL 2061 (Redout Leyden), the No.1-6 battery list, the legend heading and the a-g legend below the glossed\n"
            "# title/battery-header block: native IIIF region 2800,820,2300,900 (images/2061_battery_legend_native.jpg). No\n"
            "# interlinear gloss on any of these 10 lines. GAPS8-na-suriname-map-1781, 2 Oct 2026: two blind Sonnet passes on\n"
            "# tools/iiif_lines.py crops (passes/bat2061_passA.tsv, passB.tsv), aligned by tools/reconcile_passes.py, 48\n"
            "# non-trivial disagreements settled by one blind reconciliation call (passes/bat2061_reconC.tsv). Generated by\n"
            "# build_2061_battery.py; 'w:' = plain (No, numbers before [MM], label letters).\n")
    f.write('line\tpos\tsign\tconf\tnote\tword\n')
    pos = {}
    for line, s, conf, note, w in rows:
        p = pos.get(line, 0); pos[line] = p + 1
        if (line, p) in IMAGE_SETTLED:
            s, extra = IMAGE_SETTLED[(line, p)]; note = f'{note}; {extra}'
        f.write(f'{line}\t{p}\t{s}\t{conf}\t{note}\t{w}\n')
print(len(rows), 'rows;', sum(1 for r in rows if not r[1].startswith('w:')), 'cipher signs;',
      sum(1 for r in rows if not r[1].startswith('w:') and r[2] == 'H'), 'H')
