#!/usr/bin/env python3
"""COS-1167 (10 Oct 2026): reference cipher-group / copy-word ratios for R1167 from the committed D4-COST, D4-COST2, D4-COST3
reads and their registered clear spans (sigla expanded as each PREREG fixed them). Group = one '|' field of a pass row holding at
least one cipher sign ({CLEAR}, {CODE} and x removed; a group of x alone is a code group and is counted apart). Span bounds are the
scorers' own (d4cost_score.span_signs, d4cost2_score.spans, d4cost3_score.spans with the amended L07 anchor). Prints one TSV row per
span and pass, plus the range. Usage: python3 align/cos1167_ref.py   (run from the folder)."""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d4cost2_score as d2, d4cost3_score as d3
MARK = {'{CLEAR}', '{CODE}'}

def groups_with_ids(path, prefix):
    seq = []
    for r in csv.DictReader(open(path), delimiter='\t'):
        ln = r['line'].replace(prefix, '')
        for gi, grp in enumerate(r['signs'].split('|')):
            for t in grp.split():
                seq.append((ln, gi, t))
    return seq

def count(seq):
    gids = {(ln, gi) for ln, gi, t in seq if t not in MARK and t != 'x'}
    codes = {(ln, gi) for ln, gi, t in seq if t == 'x'} - gids
    return len(gids), len(codes)

def d4cost(path):
    spans = {r['span']: r for r in csv.DictReader(open(os.path.join(HERE, 'd4cost_spans.tsv')), delimiter='\t')}
    seq = groups_with_ids(path, 'c1_')
    out = {}
    for name, r in spans.items():
        sel = []
        for part in r['cipher'].split(','):
            ln, s = part.split(':', 1)
            line = [x for x in seq if x[0] == ln]
            gs = sorted({x[1] for x in line})
            clear_g = [g for g in gs if any(x[1] == g and x[2] == '{CLEAR}' for x in line)]
            if s == '*': keep = gs
            elif s == '<CLEAR': keep = [g for g in gs if not clear_g or g < clear_g[0]]
            elif s == '>CLEAR': keep = [g for g in gs if not clear_g or g > clear_g[-1]]
            sel += [x for x in line if x[1] in keep]
        if r['stop']:
            toks = [x for x in sel]
            k = next((i for i, x in enumerate(toks) if x[2] == r['stop']), None)
            if k is not None: sel = toks[:k]
        out[name] = (sel, r['clear'])
    return out

def generic(path, prefix, mod, **kw):
    seq = groups_with_ids(path, prefix)
    rows = {}
    for ln, gi, t in seq: rows.setdefault(ln, []).append(t)
    # rebuild the token stream exactly as the scorer does, then map positions back to (line, group)
    tok_stream = mod.stream(path)
    out = {}
    sp = mod.spans(tok_stream, **kw)
    # positions: walk each line's tokens in order, pairing scorer tokens with seq entries (x-marker rule may drop a {CODE})
    for name, toks in sp.items():
        used, sel = set(), []
        for ln, t in toks:
            for j, x in enumerate(seq):
                if j in used or x[0] != ln or x[2] != t: continue
                if any(k > j and seq[k][0] == ln for k in used): continue
                used.add(j); sel.append(x); break
        out[name] = (sel, mod.CLEAR[name])
    return out

def main():
    print('source\tpass\tspan\tcipher_groups\tcode_groups\tcopy_words\tgroups_per_word')
    ratios = []
    jobs = [('D4-COST', 'd4cost_reads', lambda p: d4cost(p)),
            ('D4-COST2', 'd4cost2_reads', lambda p: generic(p, 'c1b_', d2)),
            ('D4-COST3', 'd4cost3_reads', lambda p: generic(p, 'c2_', d3, anchor='L07'))]
    for src, d, fn in jobs:
        for ps in ('passA', 'passB'):
            for name, (sel, clear) in sorted(fn(os.path.join(HERE, d, ps + '.tsv')).items()):
                g, c = count(sel); w = len(clear.split())
                ratios.append(g / w)
                print(f'{src}\t{ps}\t{name}\t{g}\t{c}\t{w}\t{g / w:.3f}')
    print(f'range\t\t\t\t\t\t{min(ratios):.3f}-{max(ratios):.3f}')

if __name__ == '__main__':
    main()
