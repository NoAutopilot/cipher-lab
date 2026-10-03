#!/usr/bin/env python3
"""Word-align mssEC 15 ledger entries to the Official Records print of the same telegram and propose
code word -> meaning pairs (grade C, from print). GAPS118, 3 Oct 2026.

Usage: or_align.py PAGES_DIR OR_TXT MATCHES_TSV OUT_DIR [--volume 3warofrebellion11secrrich] [--seed 1] [--shuffles 200]
  PAGES_DIR, OR_TXT: as for or_match.py (not committed; re-fetch from the URLs in its docstring).
  MATCHES_TSV: print/or_matches.tsv; only the rows for --volume are aligned.

Method. A page's volunteer transcription is cut into entries at blank lines. An entry is anchored to the
volume by its rare word 5-grams (the or_match.py rule: a 5-gram occurring more than 8 times in the volume is a
formula); an entry with fewer than 3 anchors is left out. The print window is the anchored span plus 40 words
each side; difflib aligns the entry's words to the window. A replaced block of 1 ledger word against 1-3 printed
words, where the ledger word is not a spelling variant of the printed text (difflib ratio < 0.6 against the
joined printed words) and not a filler/time token, is a candidate pair. tools/interlinear_align.py was not used:
it aligns cipher groups to letters of a plain line (Thurloe, Nassau); here both sides are words and most words
are identical, so a word-level diff is the fitting instrument.

Outputs in OUT_DIR: align_pairs.tsv (every candidate occurrence: pointer, entry, ledger word, printed words,
OR page), proposals.tsv (per ledger word: meanings with counts, number of telegrams, key.md value if any,
status), heldout.tsv (fit/test split on telegrams, real vs shuffled-pairing control).
Entries whose print windows overlap are one telegram (the ledger copies a few twice). Held-out rule (fixed before
scoring): fit = telegrams with even group index, test = odd, so no telegram sits on both sides. A fit-side meaning is the
most frequent printed phrase for the word across fit telegrams. Test accuracy = share of test occurrences of a
fit word whose printed phrase equals the fit meaning (case-folded). Control: the same test entries aligned to a
print window drawn from a different matched telegram (a random derangement of entry -> window), same scoring,
--shuffles draws; the control is reported in hits (its scored count is often 0-2, so a rate is meaningless),
the real figure against the control mean and p95. Printed meanings are normalised: rank words dropped, a final
possessive 's' dropped, 're enforce*' folded, and an OCR variant (difflib ratio >= 0.8) folded into the first
form seen ('eichmond' -> 'richmond'); abbreviations (secy/secretary, first/st) are not candidates.
"""
import json, re, os, sys, glob, difflib, collections, argparse, random
ap = argparse.ArgumentParser()
ap.add_argument('pages'); ap.add_argument('ortxt'); ap.add_argument('matches'); ap.add_argument('out')
ap.add_argument('--volume', default='3warofrebellion11secrrich'); ap.add_argument('--seed', type=int, default=1)
ap.add_argument('--shuffles', type=int, default=200)
a = ap.parse_args(); N = 5
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from decode import load_key  # noqa: E402
KEY = load_key()
FILLER = set('signed sig finis etc im for the union whats news cold day hurry keep shirt on deep water'.split())
TIME = {'ann', 'agnes', 'anna', 'amelia', 'alice', 'betsy', 'barney', 'barbara', 'cora', 'clara', 'catharine',
        'cornelia', 'clotilda', 'delia', 'deborah', 'dorothy', 'emma', 'eugenia', 'emily', 'elizabeth', 'fanny',
        'florence', 'francis', 'gertrude', 'harriet', 'hannah', 'helen', 'henrietta', 'imogene', 'jennie', 'julia',
        'katy', 'lucy', 'laura', 'libby', 'mary', 'martha', 'minnie', 'nancy', 'nelly', 'rosalie', 'rosetta',
        'rebecca', 'reliance', 'sarah', 'suzan', 'topsy', 'viola'}

def words(t):
    t = re.sub(r'<deletion>.*?</deletion>', ' ', t, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t).replace('&', ' and ')
    return re.findall(r"[A-Za-z]+", t)

ow, opg, cur = [], [], ''
HDR = re.compile(r'^\s*(\d{1,4})\s+[A-Z][A-Z .,\'-]{6,}|[A-Z.\]]\s+(\d{1,4})\s*$')
for line in open(a.ortxt, errors='ignore'):
    m = HDR.search(line)
    if m: cur = m.group(1) or m.group(2)
    w = words(line); ow += w; opg += [cur] * len(w)
owl = [w.lower() for w in ow]
idx = collections.defaultdict(list)
for i in range(len(owl) - N + 1): idx[' '.join(owl[i:i + N])].append(i)

ptrs = sorted({int(r.split('\t')[0]) for r in open(a.matches).read().splitlines()[1:] if r.split('\t')[3] == a.volume})
entries = []  # (pointer, k, ledger words, (lo, hi) window)
for p in ptrs:
    f = os.path.join(a.pages, f'{p}.json')
    if not os.path.exists(f): continue
    text = json.load(open(f)).get('text') or ''
    for k, chunk in enumerate(re.split(r'\n\s*\n', text)):
        w = words(chunk); wl = [x.lower() for x in w]; anchors = []
        for i in range(len(wl) - N + 1):
            hit = idx.get(' '.join(wl[i:i + N]))
            if hit and len(hit) <= 8: anchors += hit
        if len(anchors) < 3: continue
        anchors.sort(); med = anchors[len(anchors) // 2]
        near = [x for x in anchors if abs(x - med) < 3 * len(w) + 50]
        entries.append((p, k, w, (max(0, min(near) - 40), max(near) + N + 40)))

def subseq(x, y):
    it = iter(y); return all(c in it for c in x)

RANK = {'general', 'genl', 'gen', 'major', 'maj', 'brigadier', 'x'}
CANON = []  # printed forms already seen; an OCR variant (ratio >= 0.8) folds into the first seen
def norm(rp):
    ws = [x for x in rp.split() if x not in RANK]
    if len(ws) > 1 and ws[-1] == 's': ws = ws[:-1]
    j = ' '.join(ws)
    if j.replace(' ', '') in {'reenforcement', 'reenforcements', 'reenforced', 'reenforcements'}: return 're enforcements'
    for c in CANON:
        if difflib.SequenceMatcher(None, j.replace(' ', ''), c.replace(' ', '')).ratio() >= 0.8: return c
    CANON.append(j); return j

def pairs_for(w, win):
    lo, hi = win; L = [x.lower() for x in w]; R = owl[lo:hi]; out = []
    sm = difflib.SequenceMatcher(None, L, R, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != 'replace' or i2 - i1 != 1 or not 1 <= j2 - j1 <= 3: continue
        lw = L[i1]; rp = ' '.join(R[j1:j2])
        if lw in FILLER or lw in TIME or len(lw) < 3: continue
        if difflib.SequenceMatcher(None, lw, rp.replace(' ', '')).ratio() >= 0.6: continue
        if subseq(lw, rp.replace(' ', '')) or subseq(rp.replace(' ', ''), lw): continue  # secy/secretary, first/st
        out.append((w[i1], norm(rp), opg[lo + j1]))
    return out

def matched(lw, rp):
    """Equal up to the printed text's extra rank/given-name words: 'halleck' matches 'general halleck'."""
    return lw == rp or lw in rp.split() or rp in lw.split()

grp, ends = [], []
for _, _, _, (lo, hi) in entries:
    g = next((gi for gi, (glo, ghi) in enumerate(ends) if lo < ghi and glo < hi), None)
    if g is None: ends.append((lo, hi)); g = len(ends) - 1
    grp.append(g)
os.makedirs(a.out, exist_ok=True)
real = [pairs_for(w, win) for (_, _, w, win) in entries]
with open(os.path.join(a.out, 'align_pairs.tsv'), 'w') as fo:
    fo.write('pointer\tentry\tledger_word\tprinted\tor_page\n')
    for (p, k, _, _), ps in zip(entries, real):
        for lw, rp, pg in ps: fo.write(f'{p}\t{k}\t{lw}\t{rp}\t{pg}\n')

# proposals: per ledger word, printed phrases and the number of distinct telegrams
occ = collections.defaultdict(list)
for t, ps in enumerate(real):
    for lw, rp, _ in ps: occ[lw.lower()].append((grp[t], rp))
with open(os.path.join(a.out, 'proposals.tsv'), 'w') as fo:
    fo.write('ledger_word\tn_occ\tn_telegrams\ttop_meaning\ttop_count\tall_meanings\tkey_md\tstatus\n')
    for lw, lst in sorted(occ.items(), key=lambda x: (-len({t for t, _ in x[1]}), x[0])):
        c = collections.Counter(rp for _, rp in lst); top, tc = c.most_common(1)[0]
        tel = len({t for t, _ in lst}); tels_top = len({t for t, rp in lst if rp == top})
        kms = [r[0] for r in KEY.get(lw, [])]; km = '/'.join(kms)  # key.md is dated since GAPS127: one row per value
        if kms and any(matched(k.lower(), top) for k in kms): st = 'agrees-key'
        elif km: st = 'conflicts-key'
        elif tels_top >= 2: st = 'propose'
        else: st = 'single'
        fo.write(f"{lw}\t{len(lst)}\t{tel}\t{top}\t{tc}\t{'; '.join(f'{m}:{n}' for m, n in c.most_common())}\t{km}\t{st}\n")

def score(test_pairs, fit):
    hit = tot = 0
    for ps in test_pairs:
        for lw, rp, _ in ps:
            m = fit.get(lw.lower())
            if m: tot += 1; hit += matched(m, rp)
    return hit, tot

fit_idx = [i for i in range(len(entries)) if grp[i] % 2 == 0]; test_idx = [i for i in range(len(entries)) if grp[i] % 2 == 1]
fc = collections.defaultdict(collections.Counter)
for i in fit_idx:
    for lw, rp, _ in real[i]: fc[lw.lower()][rp] += 1
fit = {lw: c.most_common(1)[0][0] for lw, c in fc.items()}
h, t = score([real[i] for i in test_idx], fit)
rng = random.Random(a.seed); ctrl = []
wins = [entries[i][3] for i in test_idx]
for _ in range(a.shuffles):
    perm = list(range(len(wins)))
    while any(x == y for x, y in zip(perm, range(len(wins)))): rng.shuffle(perm)
    sp = [pairs_for(entries[i][2], wins[perm[j]]) for j, i in enumerate(test_idx)]
    sh, st_ = score(sp, fit); ctrl.append(sh)
ctrl.sort(); mean = sum(ctrl) / len(ctrl); p95 = ctrl[int(0.95 * len(ctrl)) - 1]  # control in hits, not rate: its scored count is often 0-2
# known-answer check: existing key.md C/I entries recovered by the alignment
ka = [(lw, r[0]) for lw in occ for r in KEY.get(lw, []) if r[1] in ('C', 'I')]
with open(os.path.join(a.out, 'heldout.tsv'), 'w') as fo:
    fo.write('entries\tfit_telegrams\ttest_telegrams\tfit_words\ttest_hits\ttest_scored\treal_acc\tctrl_hits_mean\tctrl_hits_p95\tshuffles\n')
    fo.write(f"{len(entries)}\t{len(fit_idx)}\t{len(test_idx)}\t{len(fit)}\t{h}\t{t}\t{h / t if t else 0:.3f}\t{mean:.2f}\t{p95}\t{a.shuffles}\n")
print(f'telegrams {len(ends)}; entries aligned {len(entries)} on {len({e[0] for e in entries})} pages; candidate occurrences {sum(map(len, real))}; distinct ledger words {len(occ)}')
print(f'held-out: fit words {len(fit)}, test {h}/{t} = {h / t if t else 0:.3f}; shuffled-pairing control hits mean {mean:.2f} p95 {p95} ({a.shuffles} draws)')
print(f'known-answer (key.md C/I words seen): {len(ka)}')
