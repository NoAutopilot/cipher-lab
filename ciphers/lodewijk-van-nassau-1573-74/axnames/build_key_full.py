#!/usr/bin/env python3
"""Build key_full.tsv = key.tsv + the names.tsv rows licensed by the LANE AX orchestrator's re-gate (AX-NAMES2,
26 Sept 2026), plus the AX-GLOSS grade-H finds and the AX-MERGE v2 orchestrator decision (26 Sept 2026). key.tsv
itself is never edited.

AX-NAMES2 orchestrator decision (01:42 UTC 26 Sept 2026), applied per class:
 (a) word/name codes read from a contemporary interlinear gloss (5550, 5557) -> grade H; printed by Groen at that very
     cluster of 5797 -> grade C; aligner-only word codes only at C with >= 2 agreeing observations (223 Harlem);
     every single-observation aligner word code stays out.
 (b) NULL codes with >= 4 empty observations and 0 contradicting in names.tsv (139, 140, 142, 149 fall short).
 (c) key.tsv conflicts 123, 128, 136: key_full takes NULL with a note.

AX-MERGE v2 orchestrator decision (02:26 UTC 26 Sept 2026), verbatim: "(1) AX-NAMES2's class-(c) flag is upheld: on
the known-plaintext pair 4613/4615 code 123 stands for l and 136 for vingt, so key_full does NOT override them to
NULL; they keep key.tsv's values at grade M with a note 'NULL in 13/13 (123) and 8/8 (136) aligned observations in
5810/5811 -- dual use or aligner bias, unresolved'. 128 ('?' in key.tsv) goes to NULL at M. (2) Add from AX-GLOSS,
grade H (4496's contemporary interlinear gloss): 192 = Roi d'Espagne, 221 = Hollande." This revises class (c) to
keep 123/136 at key.tsv's own value (128 unchanged from AX-NAMES2) and adds the two AX-GLOSS codes, which sit
outside names.tsv's aligner pipeline (192 is names.tsv grade U -- Groen leaves the subject blank at 5549 PS1 --
and 221 has no names.tsv row at all), so their licence is checked against axgloss/gloss_attest.tsv instead.

Each licence is re-checked against names.tsv / gloss_attest.tsv here, so a changed source file that no longer
supports a row fails loudly.

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
# AX-GLOSS finds (26 Sept 2026): codes >120 attested by a contemporary interlinear gloss on 4496, outside the
# names.tsv aligner pipeline (192 is names.tsv grade U; 221 has no names.tsv row). Licence checked against
# axgloss/gloss_attest.tsv's confidence column, not against names.tsv.
AXGLOSS_H = {
    '192': ('roidespagne', "4496 (WVO PDF p4) contemporary interlinear gloss \"R. d'Espagne\" over 192 (row1, "
            "'...124.192. pour...'), confirmed by two independent blind Sonnet passes (AX-GLOSS, "
            "axgloss/gloss_attest.tsv); names.tsv previously graded this code U (0 observations -- Groen's print "
            "leaves the subject out at 5549 PS1)"),
    '221': ('hollande', "4496 (WVO PDF p4) contemporary interlinear gloss 'Hollando' over 221, repeated 3x on the "
            "same page always over 221, confirmed by two independent blind Sonnet passes (AX-GLOSS, "
            "axgloss/gloss_attest.tsv); corroborated unglossed in 4614 p1 'tiré de la Haye en 221' (context: "
            "withdrew from The Hague to Holland)"),
}
CONFLICT_NULL = ['128']
# AX-MERGE v2 (02:26 UTC 26 Sept 2026): 123/136 no longer overridden to NULL -- the orchestrator upheld AX-NAMES2's
# class-(c) flag and kept key.tsv's own value at grade M instead, with a note recording the NULL-in-aligner-
# observations conflict as unresolved.
CONFLICT_KEEP_M = ['123', '136']
CONFLICT_KEEP_NOTE = ("NULL in 13/13 (123) and 8/8 (136) aligned observations in 5810/5811 -- dual use or aligner "
                      "bias, unresolved")


def read_tsv(p):
    with open(p, newline='') as f:
        rows = list(csv.reader(f, delimiter='\t'))
    return rows[0], rows[1:]


def read_gloss_attest():
    p = os.path.join(TGT, 'axgloss', 'gloss_attest.tsv')
    with open(p, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def build():
    kh, krows = read_tsv(os.path.join(TGT, 'key.tsv'))
    assert kh[:5] == ['code', 'value', 'grade', 'source', 'note'], kh
    nh, nrows = read_tsv(os.path.join(TGT, 'names.tsv'))
    names = {r[0]: dict(zip(nh, r)) for r in nrows}
    gloss_rows = read_gloss_attest()
    key = {r[0]: r[:5] + [''] * (5 - len(r[:5])) for r in krows}
    order = [r[0] for r in krows]
    out = {c: list(v) for c, v in key.items()}
    added = {'H': [], 'C': [], 'NULL': [], 'conflict': [], 'conflict_kept_M': []}

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
    for code, (val, src) in AXGLOSS_H.items():
        matches = [r for r in gloss_rows
                   if r.get('code_the_gloss_sits_over') == code and r.get('confidence') == 'H']
        need(code, matches, 'gloss_attest.tsv has no H-confidence row for this code (AX-GLOSS changed?)')
        need(code, code not in key, 'already in key.tsv')
        out[code] = [code, val, 'H', src,
                     "AX-MERGE orchestrator decision (02:26 UTC 26 Sept 2026): AX-GLOSS grade H, 4496's "
                     "contemporary interlinear gloss (rule 4 H)"]
        added['H'].append(code)
    for code, n in sorted(names.items(), key=lambda kv: int(kv[0])):
        if n['value'] != 'NULL' or n['grade'] != 'C':
            continue
        obs, agr = int(n['observations']), int(n['agreeing'])
        if obs < 4 or agr != obs:
            continue
        if code in CONFLICT_NULL:
            k = key[code]
            # graded M, not C: on the known-answer pair itself (4613/4615, R18) 128 sits at the unsettled end of
            # 'Trittheim' (4613 L28) -- NULL there drops plaintext letters (AX-NAMES2 step 2)
            out[code] = [code, 'NULL', 'M', f"names.tsv: NULL in {agr} of {obs} aligned observations (5810/5811/4503 vs Groen)",
                         f"AX-NAMES2 re-gate class (c): overrides key.tsv '{k[1]}' ({k[2]}) -- {k[4]}; key.tsv unchanged"]
            added['conflict'].append(code)
        elif code in CONFLICT_KEEP_M:
            # AX-MERGE v2: orchestrator upheld the class-(c) flag but kept key.tsv's own value at M instead of NULL
            # -- on the known-answer pair itself (4613/4615) 123 stands for 'l' and 136 for 'vingt' (AX-NAMES2 step 2).
            k = key[code]
            need(code, k[2] == 'M', f'key.tsv grade for {code} is {k[2]}, expected M')
            out[code] = [code, k[1], 'M', k[3],
                         f"AX-MERGE orchestrator decision (02:26 UTC 26 Sept 2026): class-(c) flag upheld, "
                         f"key.tsv value kept ({k[4]}); {CONFLICT_KEEP_NOTE}"]
            added['conflict_kept_M'].append(code)
        elif code in key:
            need(code, key[code][1] == 'NULL', f'key.tsv has {key[code][1]} for a names.tsv NULL')
        else:
            out[code] = [code, 'NULL', 'C', f"names.tsv: empty in {agr} of {obs} aligned observations, 0 contradicting",
                         'AX-NAMES2 re-gate class (b): >= 4 empty observations, false-null rate about 0.18^k (axnames/falsenull_diag.out)']
            added['NULL'].append(code)
    need('conflicts', sorted(added['conflict']) == CONFLICT_NULL, f"expected conflicts {CONFLICT_NULL}, got {added['conflict']}")
    need('conflicts_kept', sorted(added['conflict_kept_M']) == CONFLICT_KEEP_M,
         f"expected conflict_kept_M {CONFLICT_KEEP_M}, got {added['conflict_kept_M']}")
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
