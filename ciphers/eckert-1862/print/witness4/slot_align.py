#!/usr/bin/env python3
"""GAPS191, 3 Oct 2026: sent-side witnesses for Koran, Lamb, Luna, Indus (and any WORDS given).
For every occurrence of a code word in the mssEC 15 volunteer transcription (dmQuery dump, field `transc`), take the
ledger's own words on both sides (K=8 each), find the OR passage that shares the most of them in order (any volume in
OR_DIR), and report the printed word that fills the code word's slot (the OR span between the matched left and right
anchors, difflib). Control (--shuffle N): the same procedure with each occurrence's context swapped to a random other
occurrence's context (shuffled pairing), counting how often the slot then yields the same printed meaning.
Usage: slot_align.py VOL15_JSON OR_DIR OUT_TSV [--words Koran,Lamb,Luna,Indus] [--shuffle 200]
Inputs not committed (volunteer transcription and IA OCR, re-fetch: see NOTES.md GAPS191)."""
import json, re, glob, os, sys, argparse, random, collections, difflib
ap = argparse.ArgumentParser(); ap.add_argument('vol'); ap.add_argument('ordir'); ap.add_argument('out')
ap.add_argument('--words', default='Koran,Lamb,Luna,Indus'); ap.add_argument('--shuffle', type=int, default=200)
ap.add_argument('--seed', type=int, default=1); a = ap.parse_args(); K = 8
W = lambda t: re.findall(r'[a-z]+', re.sub(r'<deletion>.*?</deletion>|<[^>]+>', ' ', t.lower().replace('&', ' and ')))
CW = {w.lower() for w in a.words.split(',')}
vols = {}
for f in glob.glob(os.path.join(a.ordir, '*.txt')):
    ws = W(open(f, errors='ignore').read())
    if len(ws) > 1000: vols[os.path.basename(f)[:-4]] = ws
idx = collections.defaultdict(list)
for v, ws in vols.items():
    for i, w in enumerate(ws): idx[w].append((v, i))
occ = []
for r in sorted(json.load(open(a.vol))['records'], key=lambda r: int(r['pointer'])):
    t = r['transc'] if isinstance(r['transc'], str) else ''
    ws = W(t)
    for i, w in enumerate(ws):
        if w in CW: occ.append((r['pointer'], i, w, ws[max(0, i - K):i], ws[i + 1:i + 1 + K]))
def slot(L, R):
    # vote (binned to 3 words) for the OR position of the slot from the context words that are not frequent; then
    # difflib-align ledger context to the OR window and return the OR words between the last matched left word and
    # the first matched right word (the printed span filling the code word's slot)
    votes = collections.Counter()
    for j, w in enumerate(L):
        if len(idx[w]) > 3000 or w in CW: continue
        for v, p in idx[w]: votes[(v, (p + (len(L) - j)) // 3)] += 1
    for j, w in enumerate(R):
        if len(idx[w]) > 3000 or w in CW: continue
        for v, p in idx[w]: votes[(v, (p - (j + 1)) // 3)] += 1
    if not votes: return None
    (v, b), n = votes.most_common(1)[0]
    if n < 5: return None
    c = b * 3; lo = max(0, c - len(L) - 6); win = vols[v][lo:c + len(R) + 8]
    led = L + ['<slot>'] + R; sm = difflib.SequenceMatcher(None, led, win, autojunk=False)
    lmap = {}
    for blk in sm.get_matching_blocks():
        for k in range(blk.size): lmap[blk.a + k] = blk.b + k
    left = [lmap[k] for k in range(len(L)) if k in lmap]; right = [lmap[k] for k in range(len(L) + 1, len(led)) if k in lmap]
    if not left or not right: return None
    span = win[max(left) + 1:min(right)]
    if not 1 <= len(span) <= 6: return None
    return (v, ' '.join(span), len(left) + len(right))
rows = []
for p, i, w, L, R in occ:
    s = slot(L, R)
    printed = s[1] if s else ''
    rows.append((p, i, w, ' '.join(L), ' '.join(R), s[0] if s else '', s[2] if s else 0, printed))
with open(a.out, 'w') as f:
    f.write('pointer\tword_index\tcode_word\tleft\tright\tvolume\tanchors\tprinted_in_slot\n')
    for r in rows: f.write('\t'.join(map(str, r)) + '\n')
# shuffled-pairing control: pair occurrence k's code word with occurrence m's context; a hit is the slot yielding
# the meaning the real alignment gave occurrence k
real = {(r[0], r[1]): r[7] for r in rows if r[7]}
rnd = random.Random(a.seed); hits = []
for _ in range(a.shuffle):
    perm = list(range(len(occ))); rnd.shuffle(perm); h = 0
    for k, m in enumerate(perm):
        key = (occ[k][0], occ[k][1])
        if key not in real or m == k: continue
        s = slot(occ[m][3], occ[m][4])
        if s and s[1] == real[key]: h += 1
    hits.append(h)
hits.sort()
print('occurrences', len(occ), 'aligned', len(real), 'ctrl_mean', sum(hits) / len(hits), 'ctrl_p95', hits[int(.95 * len(hits))], 'ctrl_max', hits[-1])
