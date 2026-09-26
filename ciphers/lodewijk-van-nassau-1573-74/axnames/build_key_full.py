#!/usr/bin/env python3
"""Build key_full.tsv = key.tsv + the names.tsv rows licensed by the LANE AX orchestrator's re-gate (AX-NAMES2,
26 Sept 2026). key.tsv itself is never edited.

Orchestrator's decision (01:42 UTC 26 Sept 2026), applied per class:
 (a) word/name codes read from a contemporary interlinear gloss (5550, 5557) -> grade H; printed by Groen at that very
     cluster of 5797 -> grade C; aligner-only word codes only at C with >= 2 agreeing observations (223 Harlem);
     every single-observation aligner word code stays out.
 (b) NULL codes with >= 4 empty observations and 0 contradicting in names.tsv (139, 140, 142, 149 fall short).
 (c) key.tsv conflicts 123, 128, 136: key_full takes NULL with a note.
Each licence is re-checked against names.tsv here, so a changed names.tsv that no longer supports a row fails loudly.

  python3 axnames/build_key_full.py          write key_full.tsv
  python3 axnames/build_key_full.py --check  exit 1 if key_full.tsv is stale
"""
import csv, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TGT = os.path.dirname(HERE)

GLOSS_H = {  # code: (value, source)
    '153': ('pfaltzgraf', "5550 leaf 2 contemporary interlinear gloss 'Palsgrave' over 153 (x2, runs p2-5, p2-11)"),
    '161': ('landgraf', "5550 leaf 2 contemporary interlinear gloss 'Lantgrave' over 161 (run p2-11, bey 153.161 und)"),
    '171': ('prinzzuoranien', "5550 leaf 2 contemporary interlinear gloss 'der Prince zu Oranien helfe' over 171.141 h-e-l-f-e"),
    '202': ('franckreich', "5550 contemporary interlinear gloss over 202 (x4, runs p1-1, p2-3, p2-9, p2-15)"),
    '336': ('fussvolck', "5557 leaf 1 contemporary interlinear gloss 'Voetvolck' over 336 (line 21)"),
    '350': ('gelt', "5550 leaf 2 contemporary glosses 'gelde' / 'des gelts' over runs ending 350 (x2)"),
}
# 339 is also gloss-attested ('Schutzen', 5557) but key.tsv already holds it (harquebouziers, C, same troop word):
# key.tsv's row is kept and the gloss is recorded in its note.
PRINT_C = {
    '154': ('herzogvonsachsen', "Groen IV pp.223-224 prints 'Bey dem Herzog von Sachsen und' at 5797 p5 'Bey 154.124.144.134 und'"),
    '200': ('herzogvonalba', "Groen IV p.224 prints 'vom Herzog von Alba absondern' at 5797 p6 'von 200.122.132.142 abso-'"),
}
ALIGN_C = {'223': ('harlem', "aligned to Groen IV CDLXVIII (5810) print, 3 of 3 observations agree")}
CONFLICT_NULL = ['123', '128', '136']


def read_tsv(p):
    with open(p, newline='') as f:
        rows = list(csv.reader(f, delimiter='\t'))
    return rows[0], rows[1:]


def build():
    kh, krows = read_tsv(os.path.join(TGT, 'key.tsv'))
    assert kh[:5] == ['code', 'value', 'grade', 'source', 'note'], kh
    nh, nrows = read_tsv(os.path.join(TGT, 'names.tsv'))
    names = {r[0]: dict(zip(nh, r)) for r in nrows}
    key = {r[0]: r[:5] + [''] * (5 - len(r[:5])) for r in krows}
    order = [r[0] for r in krows]
    out = {c: list(v) for c, v in key.items()}
    added = {'H': [], 'C': [], 'NULL': [], 'conflict': []}

    def need(code, cond, why):
        if not cond:
            sys.exit(f'licence failed for {code}: {why} (names.tsv changed?)')

    for code, (val, src) in GLOSS_H.items():
        need(code, code in names and names[code]['grade'] == 'C', 'names.tsv row missing or not C')
        need(code, code not in key, 'already in key.tsv')
        out[code] = [code, val, 'H', src, 'AX-NAMES2 re-gate class (a): contemporary gloss, key-source reading (rule 4 H)']
        added['H'].append(code)
    for code, (val, src) in PRINT_C.items():
        need(code, code in names and names[code]['grade'] == 'C', 'names.tsv row missing or not C')
        need(code, code not in key, 'already in key.tsv')
        out[code] = [code, val, 'C', src, 'AX-NAMES2 re-gate class (a): printed by Groen at this very cluster (rule 4 C)']
        added['C'].append(code)
    for code, (val, src) in ALIGN_C.items():
        n = names.get(code)
        need(code, n and n['grade'] == 'C' and int(n['agreeing']) >= 2 and n['agreeing'] == n['observations'],
             'aligner word code needs C with >= 2 agreeing, none contradicting')
        out[code] = [code, val, 'C', src, 'AX-NAMES2 re-gate class (a): aligner-only word code, >= 2 agreeing observations']
        added['C'].append(code)
    for code, n in sorted(names.items(), key=lambda kv: int(kv[0])):
        if n['value'] != 'NULL' or n['grade'] != 'C':
            continue
        obs, agr = int(n['observations']), int(n['agreeing'])
        if obs < 4 or agr != obs:
            continue
        if code in CONFLICT_NULL:
            k = key[code]
            # graded M, not C: on the known-answer pair itself (4613/4615, R18) 123 stands where the decipherment has
            # 'l' (4613 L18 qu'ilz, L29), 136 where it has 'vingt' (4613 L04) and 128 at the unsettled end of
            # 'Trittheim' (4613 L28) -- NULL there drops plaintext letters (AX-NAMES2 step 2)
            out[code] = [code, 'NULL', 'M', f"names.tsv: NULL in {agr} of {obs} aligned observations (5810/5811/4503 vs Groen)",
                         f"AX-NAMES2 re-gate class (c): overrides key.tsv '{k[1]}' ({k[2]}) -- {k[4]}; key.tsv unchanged"]
            added['conflict'].append(code)
        elif code in key:
            need(code, key[code][1] == 'NULL', f'key.tsv has {key[code][1]} for a names.tsv NULL')
        else:
            out[code] = [code, 'NULL', 'C', f"names.tsv: empty in {agr} of {obs} aligned observations, 0 contradicting",
                         'AX-NAMES2 re-gate class (b): >= 4 empty observations, false-null rate about 0.18^k (axnames/falsenull_diag.out)']
            added['NULL'].append(code)
    need('conflicts', sorted(added['conflict']) == CONFLICT_NULL, f"expected conflicts {CONFLICT_NULL}, got {added['conflict']}")
    out['339'][4] = (out['339'][4] + '; 5557 leaf 1 contemporary gloss reads "Schutzen" over 339 (same troop word, German) -- '
                     'AX-NAMES2: key.tsv row kept')
    num = sorted([c for c in out if c.isdigit()], key=int)
    oth = [c for c in order if not c.isdigit()]
    codes = num + oth
    lines = ['\t'.join(kh[:5])] + ['\t'.join(out[c]) for c in codes]
    return '\n'.join(lines) + '\n', added


def main():
    text, added = build()
    path = os.path.join(TGT, 'key_full.tsv')
    if '--check' in sys.argv:
        cur = open(path).read() if os.path.exists(path) else ''
        if cur != text:
            print('key_full.tsv is stale; run axnames/build_key_full.py', file=sys.stderr)
            sys.exit(1)
        print('key_full.tsv up to date')
    else:
        open(path, 'w').write(text)
    print(' '.join(f"{k} {len(v)} ({','.join(v)})" for k, v in added.items()))


if __name__ == '__main__':
    main()
