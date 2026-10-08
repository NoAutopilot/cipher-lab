#!/usr/bin/env python3
"""MANT-0609 (8 Oct 2026): merge every frame inventory of Loc. 694/08 and 694/09 on disk into one table.
Reads only committed TSVs in this folder; later sources override earlier ones for the same frame.
Writes mant0609/seen_before.tsv: loc, frame, code (y/possible/n), glossed, range, note, source."""
import csv, os, sys
D = os.path.dirname(os.path.abspath(__file__)) + "/.."
rows = {}
def rd(p):
    with open(os.path.join(D, p)) as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))
def put(loc, fr, code, gl, rng, note, src):
    rows[(loc, fr.zfill(4))] = dict(loc=loc, frame=fr.zfill(4), code=code, glossed=gl, range=rng, note=note[:160], source=src)
def yn(s):
    s = (s or '').strip().lower()
    if s.startswith('y') or s in ('cipher', 'glossed'): return 'y'
    if s.startswith('?') or 'possible' in s or s.endswith('?'): return 'possible'
    return 'n'
for r in rd('frame_inventory.tsv'):
    put(r['loc'], r['frame'], yn(r['cipher']), yn(r['interlinear_decipherment']), '', r['document'], 'frame_inventory.tsv')
for r in rd('frame_batch_gaps201.tsv'):
    c = 'n' if r['class'].startswith('clear') else 'possible' if r['class'].startswith('possible') else 'n'
    put('694/08', r['frame'], c, '', '', r['note'], 'GAPS201')
for r in rd('frame_classify_gaps207.tsv'):
    put('694/08', r['frame'], 'y' if r['class'].startswith('code') or 'control' in r['class'] else 'n', yn(r['glossed']), r['code_range'], r.get('note (eye reads by Opus vision subagents, grade M; no transcription)', ''), 'GAPS207')
for r in rd('frame_rank_gaps189.tsv'):
    put(r['loc'], r['frame'], 'y', yn(r['glossed']), r['code_range'], r['why'], 'GAPS189')
for r in rd('n9mant/inventory_0504_0578.tsv'):
    c = {'clear': 'n', 'cipher?': 'possible'}.get(r['class'], 'y')
    gl = 'y' if r['class'] == 'glossed' or 'words above' in r['note'] else ('n' if c != 'n' else '')
    put('694/08', r['frame'], c, gl, '', r['note'], 'N9-MANT2')
for p, src in (('nzmant/inventory_0581_0592.tsv', 'NZ-MANT'), ('nzmant2/inventory_0005_0495.tsv', 'NZ-MANT2'), ('r13mant/inventory_0581_plus.tsv', 'R13-MANTSCR')):
    for r in rd(p):
        if '(control)' in r['note']: continue
        put(r['loc'], r['frame'], yn(r['code']), yn(r['glossed']), r['range'], r['note'], src)
# transcribed or settled by later sections (NOTES.md): 0085 R13-MANT85, 0195/0060 B0709-A4
put('694/09', '0060', 'y', 'n', 'letter (short name-like runs)', 'read with Krauske table, B0709-A4', 'B0709-A4')
put('694/09', '0195', 'y', 'y (one)', 'letter', 'read with Krauske table, B0709-A4', 'B0709-A4')
for fr in ('0500', '0502'):
    put('694/08', fr, 'y', 'y', 'nomenclator (clear copy of f.409r/v)', 'clear-vs-cipher copy, RUN4-MANT3', 'RUN4-MANT3')
out = os.path.join(D, 'mant0609/seen_before.tsv')
with open(out, 'w') as f:
    w = csv.DictWriter(f, fieldnames=['loc', 'frame', 'code', 'glossed', 'range', 'note', 'source'], delimiter='\t')
    w.writeheader()
    for k in sorted(rows): w.writerow(rows[k])
for loc, n in (('694/08', 592), ('694/09', 302)):
    s = [k for k in rows if k[0] == loc]
    print(loc, 'seen', len(s), 'of', n, 'code y', sum(rows[k]['code'] == 'y' for k in s), 'possible', sum(rows[k]['code'] == 'possible' for k in s))
