"""NEXT-BRO (2 Oct 2026), finish-or-blocker pass gap 1: period-gloss calibration of the pt17/pt18 judge on
THIS volume's own genuine Deciffrada glosses (CLAUDE.md rule 3, the ZX-DEC349 "period gloss" paragraph).

Question: can tools/judge_plaintext.py's language gate PASS genuine period Portuguese prose of this volume at
letter 134's own length (40-70 folded letters) at all?  ZX-BRO2's bucket (judge_bucket.tsv) scored only
leave-one-out DECODES (which carry their own key errors); nobody had scored the glosses themselves -- the
known-genuine plaintext the manuscript's own appendix writes under each cipher line.

Three candidate forms per appendix entry, every one judged by the same NgramModel / controls() the CLI uses
(imported, not re-implemented; models built once per corpus; same seed=1, samples=200 as the CLI, so a
candidate's null_p99/real_p05 here equals what `judge_plaintext.py <spec> --file` prints for the same N):
  gloss        the deciffrada_line (plaintext_appendix.tsv), period abbreviations expanded (scripts/13_normalize
               WORD_ABBREV plus the extra forms attested in these glosses, table EXTRA_ABBREV below -- kept local
               to this script so 06/11's established control numbers are untouched), a trailing lone closing
               'V.' dropped, then the judge's own fold() (accents -> base letter, non-letters stripped).
  gloss_uvfold the same after 13_normalize.fold_letter (v->u, j->i, y->i) -- the convention 15_judge_bucket.py's
               base() applied to every LOO decode, so this form brackets the convention effect.
  coded_only   the gloss letters at the CODED positions only (scripts/_pairs.json, base()-folded as in 15),
               i.e. the perfect decode of the entry's cipher tokens with no clear words -- the exact shape of
               reading_body_letter134.txt (coded tokens concatenated, no plain context).
Entries over 70 folded letters are cut into 65-letter windows on the folded stream exactly as 15_judge_bucket.py
does; only 40-70-letter candidates count toward the bucket statistics (a short tail window is scored, flagged).
Every candidate also gets one letter-shuffled copy (seed 11) scored -- the per-candidate shuffled null the
ZX-DEC349 paragraph compares a gloss against.
Letter 134 (reading_body_letter134.txt, unchanged) is scored beside them, same models, same controls.

Writes gloss_calibration.tsv only. Never touches key.tsv, _pairs.json, any reading or the spec.
"""
import csv, json, os, random, re, statistics, sys
from collections import defaultdict
from importlib import import_module

ROOT = '/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712'
REPO = '/home/user/cipher-lab'
sys.path.insert(0, f'{ROOT}/scripts'); sys.path.insert(0, f'{REPO}/tools')
_norm = import_module('13_normalize')
jp = import_module('judge_plaintext')

ACCENT_MAP = {'ã': 'a', 'á': 'a', 'à': 'a', 'â': 'a', 'é': 'e', 'ê': 'e', 'í': 'i', 'ó': 'o', 'ô': 'o', 'õ': 'o', 'ú': 'u', 'ç': 'c'}
def base(c):
    return _norm.fold_letter(ACCENT_MAP.get(c.lower(), c.lower()))

# abbreviations attested in plaintext_appendix.tsv's deciffrada_line column beyond 13_normalize's table
# (read off the 39 glosses, 2 Oct 2026); period full spellings, lower-case; '±' marks are stripped first.
EXTRA_ABBREV = {
    'v.sa': 'vossa senhoria', 'v.sà': 'vossa senhoria', 'v.exª': 'vossa excellencia', 'n.exª': 'vossa excellencia',
    'v.mce': 'vossa merce', 'grde': 'grande', 'segdo.': 'segundo', 'pa.': 'para', 'pe.': 'padre',
    'aprº': 'a primeiro', 'qe': 'que',
}

def normalize_gloss(g):
    g = g.replace('±', '')
    words = g.split()
    # trailing lone 'V.' is the closing flourish (13_normalize docstring), not a word of the sentence
    if words and words[-1].lower() in ('v.', 'v'):
        words = words[:-1]
    out = []
    for w in words:
        core = w.strip('.,;:!?()[]')
        trail = w[len(w.rstrip('.,;:!?()[]')):] if core else ''
        # keep the abbreviation's own dot for lookup (q. / segdo. / pa. / pe.)
        for cand in (w.lower(), (core + '.').lower(), core.lower()):
            if cand in EXTRA_ABBREV:
                out.append(EXTRA_ABBREV[cand]); break
            e = _norm.expand_word(cand)
            if e != cand:
                out.append(e); break
        else:
            out.append(w)
    return ' '.join(out)

def uvfold(letters):
    return ''.join(_norm.fold_letter(c) for c in letters)

def windows(letters):
    if len(letters) <= 70:
        return [('whole', letters)]
    nwin = (len(letters) + 64) // 65
    return [(f'win{i+1}of{nwin}', letters[i*65:(i+1)*65]) for i in range(nwin)]

# ---- candidates ----
glosses = list(csv.DictReader(open(f'{ROOT}/plaintext_appendix.tsv'), delimiter='\t'))
pairs = json.load(open(f'{ROOT}/scripts/_pairs.json'))
coded = defaultdict(list)
for tok, let, key, span in pairs:
    coded[(key[0], key[1])].append(base(let))

cands = []  # (entry, form, kind, letters)
for r in glosses:
    label = f"{r['leaf']}/{r['entry_label']}"
    norm = normalize_gloss(r['deciffrada_line'])
    L = jp.fold(norm)
    for kind, w in windows(L):
        cands.append((label, 'gloss', kind, w))
    for kind, w in windows(uvfold(L)):
        cands.append((label, 'gloss_uvfold', kind, w))
    c = ''.join(coded.get((r['leaf'], r['entry_label']), []))
    c = jp.fold(c)
    if c:
        for kind, w in windows(c):
            cands.append((label, 'coded_only', kind, w))
l134 = jp.fold(open(f'{ROOT}/reading_body_letter134.txt').read())
cands.append(('letter 134', 'candidate', 'whole', l134))

# ---- models, built once per corpus ----
models = {}
for lang in ('pt', 'pt18'):
    paths = jp.LANG_CORPORA[lang]
    models[lang] = jp.NgramModel([jp.read_corpus(p) for p in paths])
ctrl_cache = {}
def controls(lang, N):
    k = (lang, N)
    if k not in ctrl_cache:
        ctrl_cache[k] = models[lang].controls(N, samples=200)  # seed=1, as the CLI
    return ctrl_cache[k]

def pctile_of(x, xs):
    return 100.0 * sum(1 for v in xs if v <= x) / len(xs)

rows = []
for entry, form, kind, letters in cands:
    N = max(len(letters), 20)
    row = dict(entry=entry, form=form, kind=kind, letters=len(letters), in_40_70_bucket=(40 <= len(letters) <= 70), text=letters)
    sh = list(letters); random.Random(11).shuffle(sh); sh = ''.join(sh)
    for lang, tag in (('pt', 'pt17'), ('pt18', 'pt18')):
        m = models[lang]
        real, null, cov = controls(lang, N)
        sc = m.score(letters); null99, real05 = jp.pct(null, 0.99), jp.pct(real, 0.05)
        row[f'score_{tag}'] = round(sc, 3); row[f'null_p99_{tag}'] = round(null99, 3); row[f'real_p05_{tag}'] = round(real05, 3)
        row[f'pass_{tag}'] = 'PASS' if (sc > null99 and sc > real05) else 'FAIL'
        row[f'null_pctile_{tag}'] = round(pctile_of(sc, null), 1); row[f'real_pctile_{tag}'] = round(pctile_of(sc, real), 1)
        row[f'shuffled_score_{tag}'] = round(m.score(sh), 3)
    rows.append(row)

cols = ['entry', 'form', 'kind', 'letters', 'in_40_70_bucket'] + [f'{a}_{t}' for t in ('pt17', 'pt18') for a in
        ('score', 'null_p99', 'real_p05', 'pass', 'null_pctile', 'real_pctile', 'shuffled_score')] + ['text']
with open(f'{ROOT}/gloss_calibration.tsv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols, delimiter='\t'); w.writeheader()
    for r in rows: w.writerow(r)
print(f"wrote {ROOT}/gloss_calibration.tsv ({len(rows)} rows)")

# ---- summary ----
def summ(form, whole_only=False):
    sel = [r for r in rows if r['form'] == form and r['in_40_70_bucket'] and (r['kind'] == 'whole' or not whole_only)]
    if not sel: return
    print(f"\n== {form} {'(whole entries only)' if whole_only else '(whole + 65-letter windows)'}: n={len(sel)} in 40-70 ==")
    for tag in ('pt17', 'pt18'):
        sc = [r[f'score_{tag}'] for r in sel]; shuf = [r[f'shuffled_score_{tag}'] for r in sel]
        npass = sum(r[f'pass_{tag}'] == 'PASS' for r in sel)
        above_null = sum(r[f'score_{tag}'] > r[f'null_p99_{tag}'] for r in sel)
        l = [r for r in rows if r['entry'] == 'letter 134'][0][f'score_{tag}']
        print(f"  {tag}: PASS {npass}/{len(sel)} ({100*npass/len(sel):.0f}%); above null_p99 {above_null}/{len(sel)}; "
              f"score median {statistics.median(sc):.3f} min {min(sc):.3f} max {max(sc):.3f}; "
              f"shuffled-copy median {statistics.median(shuf):.3f}; "
              f"letter 134 {l:.3f} sits at percentile {pctile_of(l, sc):.1f} of these glosses "
              f"(real-text pctile median of glosses {statistics.median([r[f'real_pctile_{tag}'] for r in sel]):.1f})")
for form in ('gloss', 'gloss_uvfold', 'coded_only'):
    summ(form, whole_only=True); summ(form, whole_only=False)
l = [r for r in rows if r['entry'] == 'letter 134'][0]
print(f"\nletter 134 ({l['letters']} letters): pt17 {l['score_pt17']} [{l['pass_pt17']}, null_p99 {l['null_p99_pt17']}, real_p05 {l['real_p05_pt17']}, null-pctile {l['null_pctile_pt17']}, real-pctile {l['real_pctile_pt17']}, shuffled copy {l['shuffled_score_pt17']}]")
print(f"                           pt18 {l['score_pt18']} [{l['pass_pt18']}, null_p99 {l['null_p99_pt18']}, real_p05 {l['real_p05_pt18']}, null-pctile {l['null_pctile_pt18']}, real-pctile {l['real_pctile_pt18']}, shuffled copy {l['shuffled_score_pt18']}]")
