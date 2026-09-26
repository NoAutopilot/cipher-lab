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
        status, office_n, years_n, lang_hint = kx.notes_meta(folder)
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


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--check', action='store_true', help='exit 1 if KEY-DESIGN.tsv differs from a rebuild')
    ap.add_argument('--stdout', action='store_true')
    a = ap.parse_args(argv)
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
