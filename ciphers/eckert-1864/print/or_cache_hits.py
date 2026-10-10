#!/usr/bin/env python3
"""OR-CACHE (10 Oct 2026, LANE LEDGER-14): letters-only word-shingle grep of every eckert-1864 entry now at N3 in status.json
(mssEC 18, mssEC 19, and report-only mssEC 25 Fort Monroe) against the volumes that were mislabelled or missing from the print cache.
Entry text = reading.md / reading-no2.md / reading-no9.md section for its tag, brackets stripped, {...} and ---- dropped.
MINRUN 7, not 9: the known-positive control (E252, E258, printed in I/43 pt 1 per NOTES, already N1) reads a longest shared run of 8, so a 9-word gate misses both.
A hit = a run of >= MINRUN consecutive entry words found consecutively in the volume (5-word shingles chained). Control = the same
entries with word order shuffled (seed 1), same threshold, per volume. A hit is a lead for a verifier, never a grade change.
Writes print/or_cache_hits.tsv and print/or_cache_summary.tsv."""
import json, re, gzip, random, sys, os
K, MINRUN = 5, 7
VOL = {  # id on disk -> true series/volume/part (title page, or_volume_map.tsv)
 'warofrebellion431unit_0': 'I/43 pt 1', 'warofrebellion014602rootrich': 'I/46 pt 2', 'warofrebellion44unit': 'I/44',
 'warofrebellion384unit': 'I/38 pt 4', 'warofrebellion385unit': 'I/38 pt 5', 'warofrebellion392unit': 'I/39 pt 2',
 'warofrebellion393unit': 'I/39 pt 3', 'warofrebellion431unit': 'I/47 pt 2 (mislabelled 43.1)'}
D = 'sources/ia-fulltext/print-check/'
R = {}
for f in ('reading.md', 'reading-no2.md', 'reading-no9.md'):
    t = open('ciphers/eckert-1864/' + f, errors='replace').read()
    parts = re.split(r'(?m)^\*\*((?:E\d+|N2-[A-Z]+|O9-[A-Z]+)) \|', t)
    for i in range(1, len(parts), 2):
        body = parts[i + 1].split('\n', 1)[1] if '\n' in parts[i + 1] else ''
        body = re.split(r'(?m)^\*\*[A-Z0-9-]+ \||^## ', body)[0]
        R.setdefault(parts[i], body)
def words(b):
    b = re.sub(r'Code-word tokens.*', '', b); b = re.sub(r'\{[^}]*\}', ' ', b); b = re.sub(r'-{3,}', ' ', b)
    return re.findall(r'[a-z]+', b.lower())
s = json.load(open('status.json')); ent = []
for r in s['results']:
    if 'eckert-1864' not in json.dumps(r) or 'N3' not in (r.get('plaintext_novelty'), r.get('mapping_novelty')): continue
    doc = str(r.get('document_id', '')) + str(r.get('documents', ''))
    grp = 'mssEC18' if 'mssEC 18' in doc else 'mssEC19' if 'mssEC 19' in doc else 'FM-mssEC25' if 'mssEC 25' in doc else 'other'
    m = re.search(r'\((E\d+|N2-[A-Z]+|O9-[A-Z]+)[;,)\s]', r['title']) or re.search(r'\b(E\d+|N2-[A-Z]+|O9-[A-Z]+)\b', r['title'] + doc)
    d = re.search(r'\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* 18\d\d', r['title'])
    w = words(R.get(m.group(1), '')) if m else []
    ent.append((m.group(1) if m else '?', grp, d.group(0) if d else '', w))
def runs(w, sh):
    best = cur = 0; at = -1; bi = -1
    for i in range(len(w) - K + 1):
        if tuple(w[i:i + K]) in sh:
            cur += 1
            if cur > best: best, bi = cur, i - cur + 1
        else: cur = 0
    return (best + K - 1 if best else 0), bi
rnd = random.Random(1); hits = []; summ = []
for v, lab in VOL.items():
    raw = gzip.open(D + v + '_djvu.txt.gz', 'rt', errors='replace').read()
    tok = list(re.finditer(r'[a-z]+', raw.lower())); tw = [m.group(0) for m in tok]
    pos = {}
    cnt = {}
    for i in range(len(tw) - K + 1):
        pos.setdefault(tuple(tw[i:i + K]), i); cnt[tuple(tw[i:i + K])] = cnt.get(tuple(tw[i:i + K]), 0) + 1
    real = ctl = 0; n = 0
    for tag, grp, d, w in ent:
        if len(w) < MINRUN + 2: continue
        n += 1
        L, bi = runs(w, pos)
        if L >= MINRUN:
            real += 1; i = pos[tuple(w[bi:bi + K])]; off = tok[i].start()
            pg = re.findall(r'(?m)^\s*(\d{1,4})\s*$', raw[max(0, off - 6000):off]); ctxt = re.sub(r'\s+', ' ', raw[off:off + 140])
            hits.append((tag, grp, d, v, lab, pg[-1] if pg else '?', L, len(w), cnt[tuple(w[bi:bi + K])], ctxt))
        sw = w[:]; rnd.shuffle(sw)
        if runs(sw, pos)[0] >= MINRUN: ctl += 1
    summ.append((v, lab, n, real, ctl))
with open('ciphers/eckert-1864/print/or_cache_hits.tsv', 'w') as f:
    f.write('entry\tgroup\tentry_date\tvolume_id\ttrue_volume\tpage_guess\tshared_run_words\tentry_words\tfirst_5gram_occurrences_in_volume\thit_text\n')
    for h in sorted(hits, key=lambda x: (x[3], -x[6], x[8])): f.write('\t'.join(map(str, h)) + '\n')
with open('ciphers/eckert-1864/print/or_cache_summary.tsv', 'w') as f:
    f.write('volume_id\ttrue_volume\tentries_tested\treal_hits\tshuffled_control_hits\n')
    for r in summ: f.write('\t'.join(map(str, r)) + '\n')
print('entries', len(ent), 'with text', sum(1 for e in ent if e[3]))
for r in summ: print(r)
