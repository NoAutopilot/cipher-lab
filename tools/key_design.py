#!/usr/bin/env python3
"""key_design.py: build KEY-DESIGN.tsv, the structural signature of every key table on disk.

OPTIMIZATION-2026-09-26.md section (d), KEY-DESIGN (26 Sept 2026): the key corpus as an attack corpus. For each
key file tools/key_crossmatch.py finds (ciphers/*/key*.tsv|txt, maxdepth 3, plus tools/keys/key60.tsv), one row
with the office/correspondents/years/language from KEY-OFFICES.tsv (else the folder's NOTES.md), a design family,
and signature numbers computed from the table itself, plus the token statistics of its own ciphertext where
key_crossmatch's own-text pairing finds one. Files that are not code->value tables are kept as rows with
`usable=no` and the reason, never silently dropped. tools/design_prior.py reads this file.

  python3 tools/key_design.py            rewrite KEY-DESIGN.tsv
  python3 tools/key_design.py --check    exit 1 if KEY-DESIGN.tsv is stale (rule 7 shape)
  python3 tools/key_design.py --stdout   print instead of writing

Value classes (first alternative of 'a|b'; '=' and bracket decoration stripped; accents folded):
  null     the value names a null ('null', 'nulle', 'nulles', 'nul', ...)
  letter   one letter
  short    two or three letters (a syllable or a short word: period tables mix both)
  word     four or more letters, not capitalised
  name     capitalised, three or more letters, in a table that does not write everything in capitals
  empty    no value (an unread code)
  other    digits, punctuation, prose notes
Syllable grid: at least 4 consonants each followed by at least 3 distinct vowels among the table's two-letter
values ('ba be bi', 'ca ce ci', ...), the shape of a period syllabary block.
Design family (thresholds stated, not learned; `valued` = codes whose value is not null/empty/other):
  syllabary               syllable grid present and short values >= 30% of valued codes
  code numbers            fewer than 10 distinct letters and words+names+short >= 60% of valued codes
  homophonic              letters >= 85% of valued codes and codes per letter (mean) >= 1.4
  alphabet substitution   letters >= 85% of valued codes, fewer homophones than that
  nomenclator             >= 15 distinct letters and words+names+short >= 10% of valued codes
  mixed                   anything else (usually a partial table rebuilt from one letter)
A table reconstructed from one letter holds only the codes that letter used, so its family is the design as
far as it has been read, not necessarily the whole period key; the `valued` column says how much there is.
"""
import argparse
import hashlib
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
import key_crossmatch as kx  # noqa: E402
import decode_key as dk  # noqa: E402

ROOT = TOOLS.parent
OUT = ROOT / 'KEY-DESIGN.tsv'
OFFICES = ROOT / 'KEY-OFFICES.tsv'

# not code->value key tables, checked by hand 26 Sept 2026 (reason recorded in the row)
NOT_A_KEY = {
    'koehler-1944/families/': 'solver output (a running-key decode), not a key table',
    'koehler-1944/running-key/': 'noise-band statistics table, not a key table',
    'antt-linhares-chave/key_example.tsv': 'worked example (2 rows), not a key table',
    'clair349-este-guise-1556/key_vs_gloss.tsv': 'key-versus-gloss comparison table (derived from key_alpha), not a key',
    'fr3625-lauriere-1593/bourdeau_ref/': 'prose reference table (Bourdeau), not tab-separated code->value rows',
    'fr4715-montholon-1589/witness_f24/key_f24_recovered_UNVALIDATED.tsv':
        'MONT-KEY6 27 Sept 2026: failed interlinear_align.py recovery attempt on f.24, 0/7 conflicts '
        'against no.58\'s own printed dump gloss, not a usable key (see its own header and NOTES.md)',
}
NULL_WORDS = {'null', 'nulle', 'nulles', 'nul', 'nulla', 'nihil', 'nullo', 'nulo'}
VOWELS = set('aeiouy')
# language checked by hand against the folder's own reading (key_crossmatch's detector calls Mercy French)
LANG_OVERRIDE = {'espagnol142-mercy-1648': 'es'}
LANG_WORDS = {'english': 'en', 'french': 'fr', 'german': 'de', 'dutch': 'nl', 'latin': 'la', 'spanish': 'es',
              'portuguese': 'pt', 'italian': 'it', 'swedish': 'sv'}
# code column / value column by header name, most specific first (extends key_crossmatch.robust_load_key:
# thurloe-printed's tables name the CODE 'value' and the plaintext 'meaning'; key57 names it 'meaning';
# szembek's key_direct carries 'gloss_values' as 'u(4); a(1)' -- the first, most frequent gloss is taken)
VALUE_NAMES = ['meaning', 'plaintext', 'plain', 'gloss', 'key_values', 'gloss_values', 'value', 'letter',
               'word_or_phrase']
CODE_NAMES = ['code', 'code_or_sign', 'dc8_token', 'sign_code', 'sign', 'token', 'figure', 'group', 'item', 'sign_desc', 'row', 'system', 'id']

COLUMNS = ['key_path', 'usable', 'reason', 'duplicate_of', 'office', 'correspondents', 'years', 'decade',
           'language', 'design_family', 'n_codes', 'valued', 'distinct_letters', 'homophones_mean',
           'homophones_max', 'nomenclator_words', 'nomenclator_names', 'short_values', 'syllable_grid',
           'nulls_declared', 'empty_values', 'numeral_min', 'numeral_max', 'digit_lengths', 'sign_inventory',
           'own_ciphertexts', 'ct_tokens', 'ct_distinct', 'ct_singleton_share', 'ct_top_share', 'ct_ioc']


def fold(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def load_table(path):
    """{code: value} or (None, reason). Header-by-name when the first data line is a named header row, else
    decode_key.load_key (commented headers), else key_crossmatch.robust_load_key."""
    raw = Path(path).read_text(encoding='utf-8', errors='replace').splitlines()
    lines = [l for l in raw if l.strip() and not l.lstrip().startswith('#')]
    if not lines:
        return None, 'no data lines'
    low = [c.strip().lower() for c in lines[0].split('\t')]
    if len(low) >= 2 and sum(c in kx.KNOWN_HEADER_WORDS or c in VALUE_NAMES for c in low) >= 2:
        vi = next((low.index(n) for n in VALUE_NAMES if n in low), None)
        if vi is None:
            return None, 'no value/plaintext/gloss/meaning column -- not a code->value key table'
        ci = next((low.index(n) for n in CODE_NAMES if n in low and low.index(n) != vi), None)
        if ci is None:
            ci = 0 if vi != 0 else 1
        key = {}
        for l in lines[1:]:
            cells = l.split('\t')
            if len(cells) <= max(ci, vi):
                continue
            code, val = cells[ci].strip(), cells[vi].strip()
            if low[vi] == 'gloss_values':
                val = re.sub(r'\(\d+\)', '', val.split(';')[0]).strip()
            if code:
                key[code] = val
        return (key, None) if key else (None, 'no rows parsed')
    try:
        k = dk.load_key(str(path))
        if k:
            return {c: (r.get('value') or '') for c, r in k.items()}, None
    except Exception:
        pass
    k, why = kx.robust_load_key(path)
    if k is None:
        return None, why
    return {c: r['value'] for c, r in k.items()}, None


def classify_value(v, all_caps_table):
    v = fold(v.split('|')[0]).strip().strip('=[]()?').strip()
    low = v.lower()
    if not v:
        return 'empty', ''
    if low in NULL_WORDS or low.startswith('null'):
        return 'null', ''
    letters = re.sub(r"[^A-Za-z]", '', v)
    if not letters or not re.fullmatch(r"[A-Za-z' .-]+", v):
        return 'other', ''
    if len(letters) == 1:
        return 'letter', letters.lower()
    if len(letters) <= 3:
        return 'short', letters.lower()
    if v[0].isupper() and not all_caps_table:
        return 'name', letters.lower()
    return 'word', letters.lower()


def syllable_grid(shorts):
    by_cons = defaultdict(set)
    for s in shorts:
        if len(s) == 2 and s[0] not in VOWELS and s[1] in VOWELS:
            by_cons[s[0]].add(s[1])
    return sum(1 for vs in by_cons.values() if len(vs) >= 3) >= 4


def signature(key):
    vals = list(key.values())
    alpha_vals = [fold(v) for v in vals if re.search(r'[A-Za-z]', fold(v))]
    all_caps = bool(alpha_vals) and sum(v.upper() == v for v in alpha_vals) / len(alpha_vals) > 0.8
    cls = Counter()
    per_letter = Counter()
    shorts = []
    for v in vals:
        c, norm = classify_value(v, all_caps)
        cls[c] += 1
        if c == 'letter':
            per_letter[norm] += 1
        elif c == 'short':
            shorts.append(norm)
    valued = cls['letter'] + cls['short'] + cls['word'] + cls['name']
    nletters = len(per_letter)
    hom = [n for n in per_letter.values()]
    hom_mean = sum(hom) / len(hom) if hom else 0.0
    grid = syllable_grid(shorts)
    wordish = cls['short'] + cls['word'] + cls['name']
    if not valued:
        fam = 'unknown'
    elif grid and cls['short'] / valued >= 0.3:
        fam = 'syllabary'
    elif nletters < 10 and wordish / valued >= 0.6:
        fam = 'code numbers'
    elif cls['letter'] / valued >= 0.85:
        fam = 'homophonic' if hom_mean >= 1.4 else 'alphabet substitution'
    elif nletters >= 15 and wordish / valued >= 0.1:
        fam = 'nomenclator'
    else:
        fam = 'mixed'
    codes = list(key)
    digit_codes = [int(c) for c in codes if re.fullmatch(r'\d+', c)]
    dl = Counter(len(c) for c in codes if re.fullmatch(r'\d+', c))
    st = kx.sign_type(codes)
    if st == 'symbols' or (st == 'mixed' and sum(bool(re.search(r'[^\x00-\x7f]|[a-z]-[a-z]', c)) for c in codes) > len(codes) / 3):
        st = 'glyphs'
    return dict(design_family=fam, n_codes=len(codes), valued=valued, distinct_letters=nletters,
                homophones_mean=f'{hom_mean:.2f}', homophones_max=max(hom) if hom else 0,
                nomenclator_words=cls['word'] + cls['short'], nomenclator_names=cls['name'],
                short_values=cls['short'], syllable_grid='yes' if grid else 'no', nulls_declared=cls['null'],
                empty_values=cls['empty'],
                numeral_min=min(digit_codes) if digit_codes else '', numeral_max=max(digit_codes) if digit_codes else '',
                digit_lengths=','.join(f'{k}:{dl[k]}' for k in sorted(dl)), sign_inventory=st)


def ct_stats(signs):
    """Token statistics used by KEY-DESIGN.tsv and tools/design_prior.py (same function, one definition)."""
    n = len(signs)
    c = Counter(signs)
    k = len(c)
    if n < 2:
        return dict(n=n, k=k, ttr=0.0, singleton=0.0, top=0.0, top10=0.0, ioc=0.0)
    return dict(n=n, k=k, ttr=k / n, singleton=sum(1 for v in c.values() if v == 1) / k,
                top=c.most_common(1)[0][1] / n, top10=sum(v for _, v in c.most_common(10)) / n,
                ioc=sum(v * (v - 1) for v in c.values()) / (n * (n - 1)))


def read_offices():
    out = {}
    if OFFICES.exists():
        rows = OFFICES.read_text(encoding='utf-8').splitlines()
        hdr = rows[0].split('\t')
        for l in rows[1:]:
            cells = l.split('\t') + [''] * len(hdr)
            out[cells[0]] = dict(zip(hdr, cells))
    return out


def decade_of(*texts):
    for t in texts:
        ys = re.findall(r'(?<!\d)(1[3-9]\d{2})(?!\d)', t or '')
        if ys:
            return f'{int(ys[0]) // 10 * 10}s'
    return '?'


def lang_code(text):
    t = (text or '').lower()
    for w, c in LANG_WORDS.items():
        if w in t:
            return c
    return ''


def not_a_key(rel):
    for pat, why in NOT_A_KEY.items():
        if pat in rel:
            return why
    return None


def build(with_signs=False):
    """List of row dicts (and, with with_signs, each usable row's '_key' and '_signs' for design_prior)."""
    offices = read_offices()
    kept, dropped = kx.find_key_files()
    by_lang = kx.reading_files_by_lang()
    rows, key_metas = [], []
    seen_hash = {}
    for p in kept:
        rel = str(p.relative_to(ROOT))
        folder = kx.folder_of(p)
        status, office_n, years_n, lang_hint = kx.key_meta(p)
        off = offices.get(rel) or next((o for r, o in offices.items() if r.startswith(f'ciphers/{folder}/')), {})
        office = off.get('office') or office_n
        if office.startswith('same'):
            office = next((o['office'] for r, o in offices.items() if r.startswith(f'ciphers/{folder}/')
                           and not o.get('office', '').startswith('same')), office)
        if office in ('', '?'):
            office = f'(folder) {folder}'
        years = off.get('years') or years_n
        if years.startswith('same'):
            years = next((o['years'] for r, o in offices.items() if r.startswith(f'ciphers/{folder}/')
                          and not o.get('years', '').startswith('same')), years)
        if not re.search(r'(?<!\d)1[3-9]\d{2}(?!\d)', years or ''):
            years = '-'.join(re.findall(r'(?<!\d)1[3-9]\d{2}(?!\d)', folder)) or years
        lang = LANG_OVERRIDE.get(folder) or lang_code(off.get('language')) or kx.language_for(folder, lang_hint, by_lang)[0]
        corr = off.get('correspondents') or ''
        if corr.startswith('same'):
            corr = next((o['correspondents'] for r, o in offices.items() if r.startswith(f'ciphers/{folder}/')
                         and not o.get('correspondents', '').startswith('same')), corr)
        row = dict(key_path=rel, office=office.replace('\t', ' '),
                   correspondents=corr.replace('\t', ' '), years=years,
                   decade=decade_of(years, folder), language=lang or '?', _folder=folder)
        why = not_a_key(rel)
        key = None
        if not why:
            key, why = load_table(p)
        if key is not None:
            sig = signature(key)
            if sig['valued'] < 5:
                why = f"only {sig['valued']} codes carry a readable value with this loader"
        if why:
            row.update(usable='no', reason=why)
            rows.append(row)
            continue
        h = hashlib.sha1('\n'.join(f'{c}\t{v}' for c, v in sorted(key.items())).encode()).hexdigest()
        row.update(usable='yes', reason='', duplicate_of=seen_hash.get(h, ''), **sig)
        seen_hash.setdefault(h, rel)
        meta = dict(path=rel, folder=folder)
        key_metas.append((rel, key, meta))
        row['_key'] = key
        rows.append(row)
    for p, why in dropped:
        rows.append(dict(key_path=str(p.relative_to(ROOT)), usable='no',
                         reason='excluded by key_crossmatch name filter: ' + ','.join(why), _folder=kx.folder_of(p)))
    cts, _ = kx.find_ciphertext_files()
    ct_metas = [dict(path=str(p.relative_to(ROOT)), folder=kx.folder_of(p)) for p in cts]
    jobs = {m['folder']: kx.load_decode_jobs(m['folder']) for m in ct_metas}
    kx.compute_own_cts(key_metas, ct_metas, {f: j for f, j in jobs.items() if j})
    own = {rel: meta.get('own_cts', []) for rel, key, meta in key_metas}
    sign_cache = {}
    for row in rows:
        if row.get('usable') != 'yes':
            continue
        paths = own.get(row['key_path'], [])
        signs = []
        for cp in paths:
            if cp not in sign_cache:
                sign_cache[cp] = kx.tokenize_ciphertext(ROOT / cp)[0]
            signs += sign_cache[cp]
        row['own_ciphertexts'] = ';'.join(paths)
        row['_signs'] = signs
        if signs:
            s = ct_stats(signs)
            row.update(ct_tokens=s['n'], ct_distinct=s['k'], ct_singleton_share=f"{s['singleton']:.3f}",
                       ct_top_share=f"{s['top']:.3f}", ct_ioc=f"{s['ioc']:.4f}")
    rows.sort(key=lambda r: r['key_path'])
    if not with_signs:
        for r in rows:
            r.pop('_key', None); r.pop('_signs', None)
    return rows


def render(rows):
    head = ('# KEY-DESIGN.tsv -- built by tools/key_design.py (do not edit by hand; rerun it). One row per key file '
            'key_crossmatch finds; usable=no rows give the reason. Family thresholds: see the tool docstring.\n')
    out = [head, '\t'.join(COLUMNS) + '\n']
    for r in rows:
        out.append('\t'.join(str(r.get(c, '')) for c in COLUMNS) + '\n')
    return ''.join(out)

# --- --matrix (TT-MATRIX, 8 Oct 2026) -------------------------------------------------------------------------------
# Tomokiyo, "Vatican Substitution Ciphers Designed on Alphabetical Matrices" (sources/cryptiana/web/matrix.htm, 2018):
# lay a key's letter codes out by digits and look for regular assignment -- alphabetical runs (Manetti, Nevers no.25,
# de Spes), a vowel-headed matrix filled column by column with paired first digits (Commendone, Leighton's attack),
# blocks of the alphabet in shuffled or reversed order (the Spanish blocked squares of 1585-1590). "Once a couple of
# letters are identified, the whole cipher alphabet may be inferred" (matrix.htm; ormonde.htm "Breakthrough", the
# distance 83-78 = t-o; schiner.htm, the digits 0-4,8,9 counting). LESSONS-TOMOKIYO.md practices 3 and 4.
# Meant to catch: a letter table whose code order follows the alphabet in one series, several homophone series,
# shuffled/reversed blocks, or down the columns of a digit matrix. Must NOT flag: a table whose letters are assigned
# to codes at random (the permuted-key null: label `none`), and it does not label nomenclator or non-numeric codes
# at all (only integer codes carrying one letter are laid out; fewer than 8 gives `too-few`).
MATRIX_ALPHABETS = {
    'it21': 'abcdefghilmnopqrstuxz',      # Manetti's own letter row (matrix.htm)
    'it22': 'abcdefghilmnopqrstuxyz',     # Nevers no.25's row
    'es23': 'abcdefghiklmnopqrstvxyz',    # de Spes' row (Devos Cp.25)
    'en24': 'abcdefghiklmnopqrstuwxyz',   # 17th-c. English, i=j, u=v (ormonde.htm: 83-59 = 24)
    'fr23': 'abcdefghilmnopqrstuxyz&',
    'la23': 'abcdefghiklmnopqrstuxyz',
    'full26': 'abcdefghijklmnopqrstuvwxyz',
}
LANG_ALPHABET = {'it': 'it21', 'es': 'es23', 'en': 'en24', 'fr': 'it22', 'la': 'la23', 'pt': 'es23', 'de': 'full26',
                 'nl': 'full26'}


def matrix_letters(table):
    """[(int code, letter)] from a {code: value} table: integer codes whose value classes as one letter."""
    caps = sum(1 for v in table.values() if v and v.isupper()) > 0.6 * max(1, len(table))
    out = []
    for c, v in table.items():
        c = c.strip()
        if not re.fullmatch(r'\d{1,4}', c):
            continue
        cls, low = classify_value(v or '', caps)
        if cls == 'letter':
            out.append((int(c), low))
    return sorted(out)


def _row_slot(tens, paired):
    """matrix.htm: '1 or 2 or _' is one row, '3 or 4' the next ... ; unpaired, the tens digit is the row."""
    return max(1, (tens + 1) // 2) if paired else tens


def matrix_order(pairs, layout, paired=False):
    """The letter codes in reading order: 'numeric' (code order, rows across) or 'column' (units digit first,
    then down the rows -- the matrix filled column by column)."""
    if layout == 'numeric':
        return sorted(pairs)
    return sorted(pairs, key=lambda p: (p[0] % 10, _row_slot(p[0] // 10, paired), p[0]))


def _segments(seq, rank, gaps=None):
    """Split a letter sequence into maximal runs whose steps are 0 or +1 in `rank` (alphabetical fill with
    homophones repeating a letter); where `gaps` says g-1 codes are missing between two neighbours (a partial key
    rebuilt from one letter shows only the codes the letter used), a step up to g (at most 4) still continues the
    run. Returns [(start_index, end_index)] and the number of breaks."""
    segs, s = [], 0
    for i in range(1, len(seq)):
        d = rank[seq[i]] - rank[seq[i - 1]]
        g = gaps[i - 1] if gaps else 1
        if not (d in (0, 1) or 1 < d <= min(g, 4)):
            segs.append((s, i - 1))
            s = i
    if seq:
        segs.append((s, len(seq) - 1))
    return segs, max(0, len(segs) - 1)


def _gaps(codes, layout, paired):
    """Distance in matrix cells between neighbours in reading order (codes are unchanged by a letter permutation,
    so the null keeps the same gaps). Only digits the key uses count: Manetti 29 -> 32 is one cell (no 0 or 1)."""
    units = sorted({c % 10 for c in codes})
    out = []
    for a, b in zip(codes, codes[1:]):
        if layout == 'numeric':
            out.append(max(1, sum(1 for x in range(a + 1, b + 1) if x % 10 in units)))
        elif a % 10 == b % 10:
            out.append(max(1, _row_slot(b // 10, paired) - _row_slot(a // 10, paired)))
        else:
            out.append(1)
    return out


def paired_digits(pairs):
    """matrix.htm: first digits 1=2, 3=4, ... -- count (2k-1)u / (2k)u code pairs that carry the same letter."""
    by = {c: l for c, l in pairs}
    same = tot = 0
    for c, l in pairs:
        t, u = divmod(c, 10)
        if t % 2 == 1 and (c + 10) in by:
            tot += 1
            same += by[c + 10] == l
    return same, tot


def matrix_analyse(pairs, n_null=200, seed=0):
    """Label and evidence for one key's letter codes. Labels: one-part (alphabetical along the code order, one or
    more homophone series), blockwise one-part (alphabet blocks in shuffled order; `reversed` when the blocks run
    backwards), two-dimensional (alphabetical down the columns of the digit matrix), none, too-few."""
    import random
    res = {'n_letter_codes': len(pairs)}
    if len(pairs) < 8:
        res['label'] = 'too-few'
        return res
    alpha = sorted({l for _, l in pairs})
    rank = {l: i for i, l in enumerate(alpha)}
    same, tot = paired_digits(pairs)
    paired = tot >= 4 and same >= 0.8 * tot
    res['paired_first_digits'] = f'{same}/{tot}'
    rng = random.Random(seed)
    letters = [l for _, l in pairs]
    codes = [c for c, _ in pairs]
    for layout in ('numeric', 'column'):
        order = matrix_order(pairs, layout, paired)
        seq = [l for _, l in order]
        gaps = _gaps([c for c, _ in order], layout, paired)
        segs, br = _segments(seq, rank, gaps)
        null = []
        for _ in range(n_null):
            sh = letters[:]
            rng.shuffle(sh)
            null.append(_segments([l for _, l in matrix_order(list(zip(codes, sh)), layout, paired)], rank, gaps)[1])
        p = (1 + sum(b <= br for b in null)) / (1 + n_null)
        res[layout] = {'breaks': br, 'pairs': len(seq) - 1, 'adjacent': round(1 - br / max(1, len(seq) - 1), 3),
                       'null_breaks_mean': round(sum(null) / n_null, 1), 'p': round(p, 4),
                       'segments': [(seq[a], seq[b], b - a + 1) for a, b in segs]}
    num, col = res['numeric'], res['column']

    def regular(r):
        return r['p'] < 0.01 and r['adjacent'] >= 0.75

    label = 'none'
    if regular(num) and num['adjacent'] >= col['adjacent']:
        segs = [s for s in num['segments'] if s[2] >= 2]
        spans = [(rank[a], rank[b]) for a, b, _ in segs]
        wide = [s for s in spans if s[1] - s[0] + 1 >= 0.6 * len(alpha)]
        if len(segs) <= 1 or len(wide) == len(spans):
            label = 'one-part'
            res['series'] = max(1, len(wide))
        else:
            label = 'blockwise one-part'
            starts = [s[0] for s in spans]
            res['block_order'] = 'reversed' if all(a > b for a, b in zip(starts, starts[1:])) else (
                'ascending' if starts == sorted(starts) else 'shuffled')
    elif regular(col):
        label = 'two-dimensional'
        heads = [min((c, l) for c, l in pairs if c % 10 == u)[1] for u in sorted({c % 10 for c, _ in pairs})]
        res['column_heads'] = ''.join(heads)
        res['vowel_headed'] = f'{sum(h in VOWELS for h in heads)}/{len(heads)}'
    res['label'] = label
    return res


def _index(code, inv, mode, units):
    if mode == 'rank':
        return inv.index(code)
    lo = inv[0]
    return sum(1 for x in range(lo, code) if x % 10 in units)


def matrix_predict(anchors, inventory, alphabet):
    """From a few identified letters, infer the rest of the cipher alphabet under the first regular arrangement the
    anchors fit. anchors {code: letter}; inventory: every code taken to be a letter code (in a live case, the
    letter range of the ciphertext). Hypotheses, tried in order of simplicity:
      enum s   one-part, counting only the units digits the inventory uses (schiner.htm: 0-4,8,9), s codes a letter
      rank     one-part over the inventory's own codes in order
      enum s periodic  as enum, repeating every len(alphabet) (ormonde.htm: 83-59 = 24)
      column   down the columns of the digit matrix, first digits paired (matrix.htm, Commendone); fills only the
               anchors' own columns
    Returns (hypothesis or None, {code: letter})."""
    inv = sorted(set(inventory) | set(anchors))
    A = {l: i for i, l in enumerate(alphabet)}
    anc = [(c, l) for c, l in anchors.items() if l in A]
    if len(anc) < 2:
        return None, {}
    units = {c % 10 for c in inv}
    L = len(alphabet)
    hyps = []
    for mode, s, period in [('enum', 1, False), ('rank', 1, False), ('enum', 1, True), ('enum', 2, False),
                            ('enum', 3, False)]:
        offs = set()
        for c, l in anc:
            i = _index(c, inv, mode, units)
            offs.add(((i // s) - A[l]) % L if period else (i // s) - A[l])
        if len(offs) == 1:
            off = offs.pop()
            pred = {}
            for c in inv:
                r = _index(c, inv, mode, units) // s - off
                if period:
                    r %= L
                if 0 <= r < L:
                    pred[c] = alphabet[r]
            if all(pred.get(c) == l for c, l in anc):
                hyps.append((f'{mode} s{s}' + (' periodic' if period else ''), pred))
    # column hypothesis: within a column, alphabet steps by one row slot
    pred, ok = {}, True
    cols = defaultdict(list)
    for c in inv:
        cols[c % 10].append(c)
    for c, l in anc:
        u = c % 10
        r0 = _row_slot(c // 10, True)
        for x in cols[u]:
            r = A[l] + _row_slot(x // 10, True) - r0
            if 0 <= r < L:
                if x in pred and pred[x] != alphabet[r]:
                    ok = False
                pred[x] = alphabet[r]
    if ok and all(pred.get(c) == l for c, l in anc) and len({c % 10 for c, _ in anc}) < len(anc):
        hyps.append(('column paired', pred))
    if not hyps:
        # last resort, one-part order only (added after the pre-registered control, reported post hoc): between two
        # anchors in code order, the same letter fills the codes between them; a letter gap equal to the number of
        # codes between them fills one letter per code. Nothing is predicted outside the anchors.
        srt = sorted(anc)
        if any(A[b[1]] < A[a[1]] for a, b in zip(srt, srt[1:])):
            return None, {}
        pred = dict(srt)
        for (c1, l1), (c2, l2) in zip(srt, srt[1:]):
            mid = [c for c in inv if c1 < c < c2]
            if l1 == l2:
                pred.update({c: l1 for c in mid})
            elif A[l2] - A[l1] == len(mid) + 1:
                pred.update({c: alphabet[A[l1] + i + 1] for i, c in enumerate(mid)})
        return 'interpolate (one-part, between anchors)', pred
    return hyps[0]


def matrix_report(path, alphabet_name=None, anchors=None, as_json=False, inventory=None):
    import json
    table, why = load_table(path)
    if table is None:
        print(f'{path}: {why}', file=sys.stderr)
        return 2
    pairs = matrix_letters(table)
    res = matrix_analyse(pairs)
    res['key'] = str(path)
    if anchors:
        alpha = MATRIX_ALPHABETS.get(alphabet_name or 'full26', alphabet_name or 'full26')
        hyp, pred = matrix_predict(anchors, inventory or [c for c, _ in pairs] or list(anchors), alpha)
        res['predict'] = {'alphabet': alpha, 'hypothesis': hyp, 'predicted': {str(k): v for k, v in sorted(pred.items())}}
    if as_json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return 0
    print(f"{path}: {res['label']} ({res['n_letter_codes']} letter codes)")
    for k in ('series', 'block_order', 'column_heads', 'vowel_headed', 'paired_first_digits'):
        if k in res:
            print(f'  {k}: {res[k]}')
    for lay in ('numeric', 'column'):
        if lay in res:
            r = res[lay]
            print(f"  {lay}: adjacent {r['adjacent']} ({r['breaks']} breaks / {r['pairs']} steps; permuted-key null mean "
                  f"{r['null_breaks_mean']} breaks, p={r['p']}); runs: "
                  + ' '.join(f'{a}-{b}({n})' for a, b, n in r['segments'][:12]))
    if pairs:
        print('  matrix (rows = tens digit, columns = units digit):')
        by = dict(pairs)
        us = sorted({c % 10 for c in by})
        print('   ' + ''.join(f'{u:>3}' for u in us))
        for t in sorted({c // 10 for c in by}):
            print(f'{t:>3}' + ''.join(f'{by.get(t * 10 + u, "."):>3}' for u in us))
    if 'predict' in res:
        p = res['predict']
        print(f"  predict ({len(anchors)} anchors, alphabet {p['alphabet']}): {p['hypothesis'] or 'no regular arrangement fits'}")
        if p['predicted']:
            print('   ' + ' '.join(f'{k}={v}' for k, v in p['predicted'].items()))
    return 0


MATRIX_CONTROL = [  # (fixture, period alphabet preset by language, Tomokiyo page)
    ('manetti', 'it21', 'matrix.htm'), ('nevers25', 'it22', 'matrix.htm'), ('despes', 'es23', 'matrix.htm'),
    ('commendone', 'it21', 'matrix.htm'), ('ormonde', 'en24', 'ormonde.htm'), ('schiner', 'it21', 'schiner.htm')]
MATRIX_EXPECT = {'manetti': 'one-part', 'nevers25': 'one-part', 'despes': 'one-part', 'commendone': 'two-dimensional',
                 'ormonde': 'one-part', 'schiner': 'one-part'}


def _predict_score(pairs, alpha, rng, draws=20, k=3):
    by = dict(pairs)
    cor = tot = wrong = 0
    for _ in range(draws):
        pool = list(by)
        rng.shuffle(pool)
        anc, seen = {}, set()
        for c in pool:
            if by[c] not in seen and by[c] in alpha:
                anc[c] = by[c]
                seen.add(by[c])
            if len(anc) == k:
                break
        _, pred = matrix_predict(anc, list(by), alpha)
        for c, l in by.items():
            if c in anc:
                continue
            tot += 1
            if c in pred:
                cor += pred[c] == l
                wrong += pred[c] != l
    return cor, wrong, tot


def matrix_control(fixtures_dir, n_perm=20, seed=0):
    """TT-MATRIX known-answer control (tools/tests/PREREG-TT-MATRIX.md): label + 3-anchor prediction on Tomokiyo's
    keys, and the same on letter-permuted copies (the null)."""
    import random
    rng = random.Random(seed)
    lab_ok = 0
    pc = pt = pw = 0
    nn = nnone = 0
    npc = npt = npw = 0
    for name, preset, page in MATRIX_CONTROL:
        table, _ = load_table(Path(fixtures_dir) / f'{name}.tsv')
        pairs = matrix_letters(table)
        r = matrix_analyse(pairs)
        ok = r['label'] == MATRIX_EXPECT[name]
        lab_ok += ok
        alpha = MATRIX_ALPHABETS[preset]
        c, w, t = _predict_score(pairs, alpha, random.Random(seed))
        pc, pw, pt = pc + c, pw + w, pt + t
        nl = Counter()
        for i in range(n_perm):
            ls = [l for _, l in pairs]
            rng.shuffle(ls)
            perm = list(zip([cc for cc, _ in pairs], ls))
            lab = matrix_analyse(perm, seed=i)['label']
            nl[lab] += 1
            c2, w2, t2 = _predict_score(perm, alpha, random.Random(seed + i), draws=1)
            npc, npw, npt = npc + c2, npw + w2, npt + t2
        nn += n_perm
        nnone += nl['none']
        print(f"{name:11s} ({page}, {preset}): label {r['label']}{'' if ok else ' (expected ' + MATRIX_EXPECT[name] + ')'}"
              f"; predict 3 anchors x20: {c}/{t} correct, {w} wrong; null labels {dict(nl)}")
    print(f'LABELS {lab_ok}/{len(MATRIX_CONTROL)} (pass >= 5); NULL none {nnone}/{nn} = {nnone / nn:.3f} (pass >= 0.95); '
          f'PREDICT {pc}/{pt} = {pc / pt:.3f} correct, {pw} wrong (pass >= 0.50); '
          f'NULL PREDICT {npc}/{npt} = {npc / max(1, npt):.3f} correct, {npw} wrong (pass <= 0.15)')
    return 0 if (lab_ok >= 5 and nnone / nn >= 0.95 and pc / pt >= 0.5 and npc / max(1, npt) <= 0.15) else 1


def matrix_sweep(out_path):
    """Live run: every usable key file under ciphers/*/ (key_crossmatch's file set), one row each."""
    rows = []
    for path in kx.find_key_files()[0]:
        rel = str(Path(path).resolve().relative_to(ROOT))
        if not_a_key(rel):
            continue
        table, why = load_table(path)
        if table is None:
            continue
        pairs = matrix_letters(table)
        if len(pairs) < 8:
            continue
        r = matrix_analyse(pairs)
        rows.append([rel, r['label'], str(r['n_letter_codes']), str(r['numeric']['adjacent']), str(r['numeric']['p']),
                     str(r['column']['adjacent']), str(r['column']['p']), r.get('paired_first_digits', ''),
                     str(r.get('series', '')), r.get('block_order', ''), r.get('vowel_headed', '')])
    head = ('# key_design.py --matrix sweep (TT-MATRIX); Tomokiyo matrix.htm. Integer codes carrying one letter only; '
            'p = permuted-key null (200 shuffles, seed 0)\n')
    cols = ['key_path', 'label', 'letter_codes', 'numeric_adjacent', 'numeric_p', 'column_adjacent', 'column_p',
            'paired_first_digits', 'series', 'block_order', 'vowel_headed']
    Path(out_path).write_text(head + '\t'.join(cols) + '\n' + ''.join('\t'.join(r) + '\n' for r in rows), encoding='utf-8')
    print(f'wrote {out_path}: {len(rows)} keys, ' + ', '.join(
        f'{k} {v}' for k, v in Counter(r[1] for r in rows).most_common()))
    return 0



def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--check', action='store_true', help='exit 1 if KEY-DESIGN.tsv differs from a rebuild')
    ap.add_argument('--stdout', action='store_true')
    ap.add_argument('--matrix', metavar='KEY.tsv',
                    help='TT-MATRIX (Tomokiyo practices 3-4, matrix.htm "Vatican Substitution Ciphers Designed on '
                         'Alphabetical Matrices"; ormonde.htm; schiner.htm): lay the key\'s integer letter codes out as '
                         'a digit matrix and label the assignment one-part / blockwise one-part (shuffled or reversed '
                         'blocks) / two-dimensional (down the columns, paired first digits, vowel-headed) / none, with '
                         'a permuted-key null p per layout; with --anchors, infer the rest of the alphabet')
    ap.add_argument('--anchors', metavar='CODE=L,...', help='with --matrix: identified letters, e.g. 83=t,78=o')
    ap.add_argument('--alphabet', default=None,
                    help='with --anchors: period alphabet preset (' + ', '.join(MATRIX_ALPHABETS) + ') or the letters '
                         'themselves; default full26')
    ap.add_argument('--inventory', metavar='LO-HI', help='with --anchors: the codes taken to be letters (default: '
                    'the key\'s own letter codes), e.g. 1-46')
    ap.add_argument('--matrix-sweep', metavar='OUT.tsv',
                    help='TT-MATRIX live run: --matrix over every key file under ciphers/, one row per key')
    ap.add_argument('--json', action='store_true', help='with --matrix: JSON output')
    ap.add_argument('--matrix-control', metavar='DIR', nargs='?', const=str(TOOLS / 'tests' / 'fixtures' / 'matrix'),
                    help='TT-MATRIX known-answer control on Tomokiyo\'s keys (PREREG-TT-MATRIX.md); exit 1 below a line')
    a = ap.parse_args(argv)
    if a.matrix:
        anc = None
        if a.anchors:
            anc = {int(c): l.strip().lower() for c, l in (x.split('=') for x in a.anchors.split(','))}
        inv = None
        if a.inventory:
            lo, hi = (int(x) for x in a.inventory.split('-'))
            inv = list(range(lo, hi + 1))
        return matrix_report(a.matrix, a.alphabet, anc, a.json, inv)
    if a.matrix_control:
        return matrix_control(a.matrix_control)
    if a.matrix_sweep:
        return matrix_sweep(a.matrix_sweep)
    text = render(build())
    if a.check:
        cur = OUT.read_text(encoding='utf-8') if OUT.exists() else ''
        if cur != text:
            print('KEY-DESIGN.tsv is stale: rerun python3 tools/key_design.py', file=sys.stderr)
            return 1
        print('KEY-DESIGN.tsv is current')
        return 0
    if a.stdout:
        sys.stdout.write(text)
        return 0
    OUT.write_text(text, encoding='utf-8')
    n = text.count('\n') - 2
    print(f'wrote {OUT.name}: {n} rows, {sum(1 for l in text.splitlines() if chr(9)+"yes"+chr(9) in l)} usable')
    return 0


if __name__ == '__main__':
    sys.exit(main())
