#!/usr/bin/env python3
"""key_crossmatch.py: can any key table we hold read any ciphertext on disk it was not built for? (LANE KX job 1)

  python3 tools/key_crossmatch.py                 run the full sweep, write KEY-CROSSMATCH.tsv + print a summary
  python3 tools/key_crossmatch.py --help
  python3 tools/tests/test_key_crossmatch.py       offline test: positive control on two small fixtures

Pipeline (CLAUDE.md rules 3, 4, 7; LANE KX job brief 2026-09-25):
  1. Discover every key*.tsv/key*.txt under ciphers/ (excluding scratch names: draft, candidate, atlas, pass,
     conflicts, counts, align, crosscheck, trial) plus the published key tables already on disk
     (tools/keys/key60.tsv). Parse each with tools/decode_key.py's own load_key (imported, not copied) into
     {code: value}. Metadata (office, years, language, design, sign type) is read from the folder's NOTES.md
     and the key file's own header comment, by regex heuristics -- reported, not authoritative.
  2. Discover every ciphertext*.tsv/.txt under ciphers/ (same exclusion list, plus 'recon': intermediate
     reconciliation passes are not independent ciphertexts). Tokenise using the folder's decode.json job that
     names the file when one exists; else try tools/decode_key.py's own format auto-detection; else fall back
     to a plain whitespace/semicolon split treating any alphabetic run of 4+ letters as clear prose (reported
     as 'whitespace' -- CLAUDE.md's documented fallback for a format decode_key.py does not know).
  3. Compatibility filter: same sign type (digits / letters / symbols / mixed) and coverage (share of the
     ciphertext's token occurrences whose code the key contains) >= 0.5 to proceed to scoring; the rest are
     listed with coverage only.
  4. Score: decode with the key (first alternative of an 'a|b' value; unkeyed signs contribute nothing), score
     the folded letter stream with judge_plaintext.py's NgramModel (imported) in the key's language. Corpora:
     tools/data/{de16,fr16,it16} and modern English ship with the repo; la/nl/pt/es/16-17th c. English do not,
     so this script builds one per language from this repo's own reading*.txt/plaintext*.txt files (detected by
     function-word matching, not by folder name) under tools/data/<lang>_repo/, excluding the file under test.
  5. Controls, >=20 draws each: (a) the same key with values shuffled among its own codes; (b) the same
     ciphertext scored by every other compatible key of the same design (the unrelated-key null). z-scores
     against both; verdict hit (z>=4 both, coverage>=0.7), weak (z>=2.5 both), else none.
  6. Positive control: every key must rank its own ciphertext(s) first among all same-sign-type ciphertexts,
     z>=4 vs both controls, before any other row involving it is trusted; a key that fails is marked 'unusable'
     with the reason and excluded from the hit list.

Output: KEY-CROSSMATCH.tsv (all pairs with coverage >= 0.5, plus the positive-control rows) and
KEY-CROSSMATCH.md (method, positive-control table, hit list, at most 40 lines).
"""
import argparse, json, math, os, random, re, statistics, sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import decode_key as dk
import judge_plaintext as jp

CIPHERS = ROOT / 'ciphers'
DATA = TOOLS / 'data'

KEY_EXCLUDE = ['draft', 'candidate', 'atlas', 'pass', 'conflicts', 'counts', 'align', 'crosscheck', 'trial']
CT_EXCLUDE = KEY_EXCLUDE + ['recon']
EXTRA_KEY_FILES = ['tools/keys/key60.tsv']  # published Bourdeau/Tomokiyo table not under ciphers/

STATUS_WORDS = ['open', 'partial', 'solved', 'closed-negative', 'found-solved', 'blocked', 'offline-only']

LANG_NAME_HINTS = {
    'french': 'fr', 'français': 'fr', 'francais': 'fr', 'latin': 'la', 'dutch': 'nl', 'nederlands': 'nl',
    'italian': 'it', 'italiano': 'it', 'spanish': 'es', 'español': 'es', 'castilian': 'es',
    'portuguese': 'pt', 'português': 'pt', 'german': 'de', 'deutsch': 'de', 'english': 'en16', 'swedish': 'sv',
}

# Reading files in this repo are often continuous letter runs with no word spaces (the cipher's own line
# layout, e.g. dupuy452-carpi-1520/reading.txt: "dubontourfaictpar..."), so a word-frequency language
# detector sees only the English '#' comment headers and misclassifies the plaintext underneath (found by
# hand on this file: it scored as Spanish before comment lines were stripped and this switched to bigrams).
# Detection instead compares the folded (jp.fold) character-bigram profile of the candidate text against a
# reference profile per language: fr/de/it reuse the corpora already on disk (tools/data), the five without a
# corpus are anchored on the Lord's Prayer in that language (period-appropriate, public domain many times
# over, a standard bootstrap for exactly this low-resource case) -- used only to classify which existing
# repo file is which language, never as a scoring corpus itself.
REF_SNIPPETS = {
    'la': "Pater noster qui es in caelis sanctificetur nomen tuum adveniat regnum tuum fiat voluntas tua sicut "
          "in caelo et in terra panem nostrum cotidianum da nobis hodie et dimitte nobis debita nostra sicut "
          "et nos dimittimus debitoribus nostris et ne nos inducas in tentationem sed libera nos a malo",
    'nl': "Onze vader die in de hemelen zijt uw naam worde geheiligd uw koninkrijk kome uw wil geschiede "
          "gelijk in de hemel alzo ook op de aarde geef ons heden ons dagelijks brood en vergeef ons onze "
          "schulden gelijk ook wij vergeven onze schuldenaren en leid ons niet in verzoeking maar verlos ons "
          "van den boze want uw is het koninkrijk en de kracht en de heerlijkheid in der eeuwigheid amen",
    'pt': "Pai nosso que estais nos ceus santificado seja o vosso nome venha a nos o vosso reino seja feita a "
          "vossa vontade assim na terra como no ceu o pao nosso de cada dia nos dai hoje perdoai as nossas "
          "dividas assim como nos perdoamos aos nossos devedores e nao nos deixeis cair em tentacao mas "
          "livrai nos do mal amem",
    'es': "Padre nuestro que estas en los cielos santificado sea tu nombre venga a nosotros tu reino hagase "
          "tu voluntad asi en la tierra como en el cielo danos hoy nuestro pan de cada dia perdona nuestras "
          "deudas asi como nosotros perdonamos a nuestros deudores no nos dejes caer en tentacion mas "
          "libranos del mal amen",
    'en16': "Our father which art in heaven hallowed be thy name thy kingdom come thy will be done in earth "
            "as it is in heaven give us this day our daily bread and forgive us our debts as we forgive our "
            "debtors and lead us not into temptation but deliver us from evil for thine is the kingdom and "
            "the power and the glory for ever amen",
}
REPO_CORPUS_LANGS = ('la', 'nl', 'pt', 'es', 'en16')  # languages with no corpus already on disk (item 4)
BUILTIN_REF_LANGS = ('fr', 'de', 'it')  # reference bigram profile comes from the corpus already on disk
# judge_plaintext.py's LANG_CORPORA has no 'it' entry even though tools/data/it16 exists on disk; add it here
# for both language-detection and scoring (get_model) rather than editing judge_plaintext.py's own table.
BUILTIN_LANG_CORPORA = dict(jp.LANG_CORPORA, it=sorted(DATA.glob('it16/*.txt')))

CLEAR_WORD_RE = re.compile(r"^[A-Za-zÀ-ÿ'’-]{4,}$")
_REF_PROFILES = None


# the repo's own house style for reading/plaintext files opens with an English metadata preamble that is not
# '#'-commented (e.g. vanbeuningen-dewitt-1657/plaintext_print.txt: "Source: Brieven aan Johan de Witt...");
# left in, that English noise dilutes or outweighs a short non-English letter body in the language blob.
METADATA_LINE_RE = re.compile(
    r'^(source|transcribed|grade|grades|generated|tokens?:|format|notes?[:\s]|original spelling|footnote|'
    r'regenerate|reconciled|see images|page break)', re.I)
# citation/process noise (URLs, file paths, named tools and archives) can appear mid-file, not only in an
# opening preamble (breda-statengeneraal-1624-25/plaintext_print.txt: 'Google Books volume nZl28...' and
# 'tools/browser_fetch.js screenshot' sit right next to the real Dutch letter body) -- drop any line
# containing this, wherever it falls, rather than only lines starting with it.
METADATA_ANYWHERE_RE = re.compile(
    r'http|\.(png|jpg|jpeg|gz)\b|tools/|images/|archive\.org|gallica|huygens|digitarq|iiif|ark:|'
    r'google books|browser_fetch|hathitrust|worldcat', re.I)


def strip_comments(text):
    return '\n'.join(l for l in text.splitlines()
                      if not l.lstrip().startswith('#') and not METADATA_LINE_RE.match(l.lstrip())
                      and not METADATA_ANYWHERE_RE.search(l))


def ngram_profile(letters, n=3):
    from collections import Counter
    if len(letters) < n:
        return {}
    grams = Counter(letters[i:i + n] for i in range(len(letters) - n + 1))
    total = sum(grams.values())
    return {g: c / total for g, c in grams.items()}


def ref_profiles():
    global _REF_PROFILES
    if _REF_PROFILES is not None:
        return _REF_PROFILES
    profiles = {}
    for lang in BUILTIN_REF_LANGS:
        texts = [jp.read_corpus(p) for p in BUILTIN_LANG_CORPORA[lang]]
        # matched to roughly the same folded length as a REF_SNIPPETS profile (repeated x4): a much bigger
        # slice would give fr/de/it systematically wider trigram coverage than the Lord's-Prayer-only
        # languages and win the cosine comparison by sample-size alone, not by genuine similarity (found by
        # hand: nl and es text was losing to de/fr/it every time until this was capped to match)
        letters = jp.fold(' '.join(texts))[:3200]
        profiles[lang] = ngram_profile(letters)
    for lang, snippet in REF_SNIPPETS.items():
        # the Lord's Prayer alone is short for trigram stats; repeating it doesn't add new information but
        # keeps the profile from being dominated by a handful of unique trigrams at the ends of a short text
        profiles[lang] = ngram_profile(jp.fold(snippet * 4))
    _REF_PROFILES = profiles
    return profiles


def cosine(a, b):
    dot = sum(v * b.get(g, 0.0) for g, v in a.items())
    an = math.sqrt(sum(v * v for v in a.values()))
    bn = math.sqrt(sum(v * v for v in b.values()))
    return dot / (an * bn) if an and bn else 0.0


def detect_lang(text, min_letters=60, min_sim=0.35, min_margin=0.02, sample_cap=4000):
    """Language of `text` by cosine similarity of its folded character-trigram profile to each reference
    profile (see REF_SNIPPETS above): None below min_letters, or when the best match doesn't clear min_sim
    and beat the runner-up by min_margin (closely related languages, e.g. pt/it/es or nl/de, cost accuracy
    at bigram level -- trigrams plus a margin requirement catch most of the confusions found by hand). A
    much longer candidate than the (thin, Lord's-Prayer-scale) reference profiles builds a richer, more
    diffuse trigram vocabulary that lowers cosine similarity against every reference by sample size alone,
    not by genuine dissimilarity (found by hand: thurloe-printed's 88,498-letter blob scored only 0.084
    against its best-matching language, below min_sim, though the text is mostly English) -- capped to the
    same rough scale as the reference profiles."""
    letters = jp.fold(strip_comments(text))
    if len(letters) < min_letters:
        return None
    if len(letters) > sample_cap:
        letters = letters[:sample_cap]
    tp = ngram_profile(letters)
    if not tp:
        return None
    sims = sorted(((cosine(tp, prof), lang) for lang, prof in ref_profiles().items()), reverse=True)
    best_sim, best = sims[0]
    second_sim = sims[1][0] if len(sims) > 1 else 0.0
    if best_sim >= min_sim and (best_sim - second_sim) >= min_margin:
        return best
    return None


# ==================================================================== discovery

def excluded(path_str, patterns):
    low = path_str.lower()
    return [p for p in patterns if p in low]


def find_key_files():
    """(kept, dropped) key file paths under ciphers/ (maxdepth 3) plus EXTRA_KEY_FILES, dropped items as (path, why)."""
    found = []
    for pat in ('key*.tsv', 'key*.txt'):
        for p in CIPHERS.glob('*/' + pat):
            found.append(p)
        for p in CIPHERS.glob('*/*/' + pat):
            found.append(p)
    found = sorted(set(found))
    kept, dropped = [], []
    for p in found:
        rel = str(p.relative_to(ROOT))
        hit = excluded(rel, KEY_EXCLUDE)
        (dropped if hit else kept).append((p, hit) if hit else p)
    for extra in EXTRA_KEY_FILES:
        p = ROOT / extra
        if p.exists():
            kept.append(p)
    return kept, dropped


def find_ciphertext_files():
    found = sorted(set(CIPHERS.glob('**/ciphertext*.tsv')) | set(CIPHERS.glob('**/ciphertext*.txt')))
    kept, dropped = [], []
    for p in found:
        rel = str(p.relative_to(ROOT))
        hit = excluded(rel, CT_EXCLUDE)
        (dropped if hit else kept).append((p, hit) if hit else p)
    return kept, dropped


# tools/keys/key60.tsv (EXTRA_KEY_FILES) is Bourdeau/Tomokiyo's published key no.60, already transcribed a
# second time as ciphers/fr3985-nevers-revol-1593/key.tsv (its header comment names the same source); it has
# no ciphers/<folder> home of its own for the co-location heuristic below to find, but its true home for the
# positive control is known from that header, not guessed.
EXTRA_KEY_HOME = {'tools/keys/key60.tsv': 'fr3985-nevers-revol-1593'}


def folder_of(path):
    rel = Path(path).relative_to(ROOT)
    if str(rel) in EXTRA_KEY_HOME:
        return EXTRA_KEY_HOME[str(rel)]
    return rel.parts[1]  # ciphers/<folder>/...


# ==================================================================== NOTES.md metadata

def notes_meta(folder):
    """(status, office, years, lang_hint) read from ciphers/<folder>/NOTES.md; '?' fields when not found."""
    p = CIPHERS / folder / 'NOTES.md'
    status, office, years, lang_hint = '?', '?', '?', '?'
    if not p.exists():
        return status, office, years, lang_hint
    try:
        lines = p.read_text(encoding='utf-8', errors='replace').splitlines()
    except Exception:
        return status, office, years, lang_hint
    nonblank = [l for l in lines if l.strip()]
    if nonblank:
        first = re.sub(r'[*_`]', '', nonblank[0]).strip().lower()
        if first in STATUS_WORDS:
            status = first
    if status == '?':
        for l in lines[:30]:
            m = re.search(r'\bstatus\s*:\s*\**\s*([a-z-]+)', l, re.I)
            if m and m.group(1).lower() in STATUS_WORDS:
                status = m.group(1).lower(); break
    heading = next((l for l in lines[:20] if l.lstrip().startswith('#')), '')
    m = re.search(r"([A-ZÀ-Ÿ][^()\n]{2,60}?)\s+(?:to|->|→)\s+([A-ZÀ-Ÿ][^()\n,;]{2,60})", heading)
    if m:
        office = f"{m.group(1).strip(' ,')} -> {m.group(2).strip(' .')}"
    ys = re.findall(r'\b(1[4-9]\d{2}|20\d{2})\b', heading) or re.findall(r'\b(1[4-9]\d{2}|20\d{2})\b', folder)
    if ys:
        years = f"{min(ys)}-{max(ys)}" if min(ys) != max(ys) else ys[0]
    text = '\n'.join(lines[:40]).lower()
    for name, code in LANG_NAME_HINTS.items():
        if re.search(r'\b' + re.escape(name) + r'\b', text):
            lang_hint = code; break
    return status, office, years, lang_hint


# Manual corrections, checked by hand against the folder's own reading/plaintext text (never guessed from
# the folder name), for four folders where the trigram classifier above is confirmed wrong or too short to
# call: nl/de and es/it/pt are close enough in character-level statistics, and the Lord's-Prayer reference
# snippets thin enough, that a short or noisy sample can lose to the wrong close relative.
#   vanbeuningen-dewitt-1657: reading.txt is Dutch prose ("Hier voort van dagh tot dagh met groot
#     impatientie", "gebruijcken", "onder anderen"); classifier scores it de 0.431 vs nl 0.410 (checked by
#     hand 25 Sept 2026) -- inside the margin, and the margin itself is de's advantage from a fuller German
#     reference corpus (tools/data/de16) against a two-hundred-word Dutch anchor, not a real signal.
#   breda-statengeneraal-1624-25: plaintext_print.txt body is Dutch ("Brief van het Stedelijk bestuur van
#     Breda aan de Staten Generaal", "Alsoo wy nu in de vierde weke besloten syn"); the classifier saw it as
#     French once the English citation preamble around it was stripped down to a similar de/nl-vs-fr margin.
#   rah-canada-1869: reading.txt is Spanish prose ("hoy 15 noviembre", "ruega al senor don luis gonzalez
#     bravo, haga llegar a manos de su magestad la reina"); RAH is the Real Academia de Historia (Spain).
#   antt-linhares-chave: reading.txt is Portuguese ("para supprir o seu lugar", "o ministerio"; ANTT is the
#     Portuguese national archive) but only 8 lines -- below detect_lang's min_letters floor.
#   dupuy468-anhalt: reading.txt opens "Amicissime potentissime ac christianissime rex ac domine domine
#     obseruandissime. Post humilimam atque humilimam commendationem maiestatem vestram certiorem reddimus"
#     -- unmistakably Latin chancery style (maiestatem vestram, -issime superlatives); classifier scores it
#     it 0.382 vs la 0.276, Italian being close enough to its own ancestor to win on a short sample.
FOLDER_LANG_OVERRIDE = {
    'vanbeuningen-dewitt-1657': 'nl',
    'breda-statengeneraal-1624-25': 'nl',
    'rah-canada-1869': 'es',
    'antt-linhares-chave': 'pt',
    'dupuy468-anhalt': 'la',
}


def reading_files_by_lang():
    """{lang: [(path, folder), ...]} for every reading*.txt/plaintext*.txt under ciphers/. Language is
    detected once per FOLDER from all of that folder's reading/plaintext text concatenated (more letters ->
    a more reliable trigram profile than any one short file alone), then applied to each of its files."""
    by_folder = {}
    for p in sorted(set(CIPHERS.glob('**/reading*.txt')) | set(CIPHERS.glob('**/plaintext*.txt'))):
        try:
            text = p.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue
        by_folder.setdefault(folder_of(p), []).append(p)
    out = {}
    for folder, paths in by_folder.items():
        blob = '\n'.join(strip_comments(p.read_text(encoding='utf-8', errors='replace')) for p in paths)
        lang = FOLDER_LANG_OVERRIDE.get(folder) or detect_lang(blob)
        if lang:
            for p in paths:
                out.setdefault(lang, []).append((p, folder))
    return out


def language_for(folder, lang_hint, by_lang):
    """Primary: detect from this folder's own reading/plaintext file(s); secondary: NOTES.md keyword; else '?'."""
    votes = {}
    for lang, items in by_lang.items():
        n = sum(1 for _, f in items if f == folder)
        if n:
            votes[lang] = n
    if votes:
        return max(votes, key=votes.get), 'reading-file'
    if lang_hint != '?':
        return lang_hint, 'notes-keyword'
    return '?', 'unknown'


# ==================================================================== key parsing / metadata

def sign_type(codes, majority=0.8):
    """The class (digits / letters / symbols) covering >= `majority` of `codes`' occurrences, else 'mixed'.
    A single stray token (an OCR artifact, a line label the whitespace fallback missed) must not flip an
    otherwise-uniform ciphertext or key to 'mixed' and drop it out of every compatibility comparison -- so
    this is a majority vote over occurrences, not 'every code must agree exactly'."""
    from collections import Counter
    def cls(c):
        if re.fullmatch(r'\d+', c):
            return 'digits'
        if re.fullmatch(r'[A-Za-z]+', c):
            return 'letters'
        if re.fullmatch(r'[^A-Za-z0-9]+', c):
            return 'symbols'
        return 'mixed'
    counts = Counter(cls(c) for c in codes)
    total = sum(counts.values())
    if not total:
        return 'mixed'
    best_cls, best_n = counts.most_common(1)[0]
    return best_cls if best_n / total >= majority else 'mixed'


def key_design(key):
    """(design, code_len_hist) from the key's {code: {value, ...}} dict; first alt of 'a|b' values."""
    vals = [row['value'].split('|')[0] for row in key.values() if row.get('value')]
    if not vals:
        return 'unknown', {}
    n_codes, n_distinct = len(vals), len(set(vals))
    homophone_ratio = n_codes / max(1, n_distinct)
    avg_len = statistics.mean(len(v) for v in vals)
    if avg_len <= 1.5:
        base = 'homophonic' if homophone_ratio >= 1.5 else 'monoalphabetic'
    elif avg_len <= 4:
        base = 'nomenclator'
    else:
        base = 'code'
    hist = {}
    for c in key:
        hist[len(c)] = hist.get(len(c), 0) + 1
    return base, hist


def load_key_meta(path):
    """One key's rows plus a metadata dict; None (logged) if unparseable."""
    try:
        key = dk.load_key(str(path))
    except Exception as e:
        return None, f'unparseable: {e}'
    if not key:
        return None, 'no rows parsed'
    folder = folder_of(path)
    status, office, years, lang_hint = notes_meta(folder)
    design, hist = key_design(key)
    meta = dict(path=str(path.relative_to(ROOT)), folder=folder, office=office, years=years,
                lang_hint=lang_hint, design=design, sign_type=sign_type(key.keys()), code_len_hist=hist,
                n_codes=len(key), status=status)
    return key, meta


# ==================================================================== ciphertext tokenisation

def load_decode_jobs(folder):
    p = CIPHERS / folder / 'decode.json'
    if not p.exists():
        return None
    try:
        cfg = json.loads(p.read_text(encoding='utf-8'))
    except Exception:
        return None
    jobs = cfg.get('jobs', [cfg])
    defaults = cfg.get('defaults', {})
    return [dict(defaults, **j) for j in jobs]


def whitespace_signs(text):
    signs = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        for tok in re.split(r'[\s;,]+', line):
            tok = tok.strip('.,;:()[]"\'')
            if not tok or CLEAR_WORD_RE.match(tok):
                continue
            signs.append(tok)
    return signs


def tokenize_ciphertext(path):
    folder = folder_of(path)
    ct_name = path.name
    jobs = load_decode_jobs(folder)
    job = None
    if jobs:
        for j in jobs:
            cj = j.get('ciphertext')
            if cj and os.path.basename(cj) == ct_name:
                job = j; break
    if job is not None:
        try:
            fmt = job.get('format') or dk.detect_format(str(path))
            recs = dk.LOADERS[fmt](str(path), job)
            signs = [r['sign'] for r in recs if r['kind'] == 'sign']
            if len(signs) >= 3:
                return signs, f'decode.json:{fmt}'
        except Exception:
            pass
    try:
        fmt = dk.detect_format(str(path))
        recs = dk.LOADERS[fmt](str(path), {})
        signs = [r['sign'] for r in recs if r['kind'] == 'sign']
        if len(signs) >= 3:
            return signs, f'auto:{fmt}'
    except Exception:
        pass
    text = path.read_text(encoding='utf-8', errors='replace')
    return whitespace_signs(text), 'whitespace'


def has_reading(folder):
    return any((CIPHERS / folder).glob('reading*.txt')) or any((CIPHERS / folder).glob('plaintext*.txt'))


def load_ct_meta(path):
    folder = folder_of(path)
    signs, method = tokenize_ciphertext(path)
    status, office, years, lang_hint = notes_meta(folder)
    return dict(path=str(path.relative_to(ROOT)), folder=folder, signs=signs, tok_method=method,
                status=status, office=office, years=years, lang_hint=lang_hint,
                sign_type=sign_type(signs), has_reading=has_reading(folder))


# ==================================================================== corpora

def build_repo_corpora(out_dir=DATA):
    """Write tools/data/<lang>_repo/*.txt for languages with no corpus on disk; return {lang: [(path, folder)]}."""
    by_lang = reading_files_by_lang()
    manifests = {}
    for lang in REPO_CORPUS_LANGS:
        items = by_lang.get(lang, [])
        if not items:
            continue
        d = out_dir / f'{lang}_repo'
        d.mkdir(parents=True, exist_ok=True)
        used = []
        for src, folder in items:
            dst = d / f'{folder}__{src.name}'
            try:
                dst.write_text(src.read_text(encoding='utf-8', errors='replace'), encoding='utf-8')
                used.append((str(src.relative_to(ROOT)), folder, dst))
            except Exception:
                continue
        (d / 'MANIFEST.tsv').write_text(
            'source\tfolder\n' + '\n'.join(f'{s}\t{f}' for s, f, _ in used) + '\n', encoding='utf-8')
        manifests[lang] = used
    return manifests


_MODEL_CACHE = {}


def get_model(lang, exclude_folder=None, corpora_map=None):
    """A judge_plaintext.NgramModel for `lang`, excluding `exclude_folder`'s own reading file if it is one of
    the repo-built corpus sources (item 4: 'exclude the target's own'). Cached per (lang, exclude_folder) --
    except a BUILTIN_LANG_CORPORA language (fr/de/it/en: a published corpus, not built from this repo's own
    reading files) never depends on exclude_folder, so it is cached once per language, not once per folder
    tested against it (a naive per-folder cache key would rebuild the multi-MB fr16/de16/it16 model for every
    one of ~115 candidate ciphertexts per key -- found by hand when the first full run did not finish in
    several minutes)."""
    builtin = lang in BUILTIN_LANG_CORPORA
    key = (lang, None if builtin else exclude_folder)
    if key in _MODEL_CACHE:
        return _MODEL_CACHE[key]
    texts = []
    if builtin:
        for p in BUILTIN_LANG_CORPORA[lang]:
            texts.append(jp.read_corpus(p))
    elif corpora_map and lang in corpora_map:
        for src_rel, folder, dst in corpora_map[lang]:
            if folder == exclude_folder:
                continue
            texts.append(dst.read_text(encoding='utf-8', errors='replace'))
    if not texts:
        _MODEL_CACHE[key] = None
        return None
    model = jp.NgramModel(texts)
    _MODEL_CACHE[key] = model
    return model


# ==================================================================== decode + score

def decode_with(key, signs):
    out = []
    covered = 0
    for s in signs:
        row = key.get(s)
        if row and row.get('value'):
            out.append(row['value'].split('|')[0])
            covered += 1
    return ' '.join(out), covered


def coverage_of(key, signs):
    if not signs:
        return 0.0
    covered = sum(1 for s in signs if s in key)
    return covered / len(signs)


def length_overlap(key_codes, signs):
    from collections import Counter
    kh = Counter(len(c) for c in key_codes)
    ch = Counter(len(s) for s in signs)
    kt, ct = sum(kh.values()), sum(ch.values())
    if not kt or not ct:
        return 0.0
    lengths = set(kh) | set(ch)
    return sum(min(kh.get(L, 0) / kt, ch.get(L, 0) / ct) for L in lengths)


def shuffled_key(key, rnd):
    codes = list(key)
    vals = [key[c]['value'] for c in codes]
    rnd.shuffle(vals)
    return {c: {'value': v} for c, v in zip(codes, vals)}


def zscore(real, nulls):
    nulls = [n for n in nulls if n is not None]
    if len(nulls) < 2:
        return None
    m, sd = statistics.mean(nulls), statistics.pstdev(nulls)
    if sd == 0:
        return 99.0 if real > m else (-99.0 if real < m else 0.0)
    return (real - m) / sd


def score_pair(key, key_meta, signs, model, n_shuffle=20, seed=0):
    text, covered = decode_with(key, signs)
    real = model.score(text) if text.strip() else -9.9
    rnd = random.Random(seed)
    shuffles = []
    for i in range(n_shuffle):
        sk = shuffled_key(key, rnd)
        stext, _ = decode_with(sk, signs)
        shuffles.append(model.score(stext) if stext.strip() else -9.9)
    return real, shuffles


# ==================================================================== main sweep

def run(alarm=None):
    keys_found, keys_dropped = find_key_files()
    cts_found, cts_dropped = find_ciphertext_files()
    by_lang = reading_files_by_lang()
    corpora_map = build_repo_corpora()

    key_metas, key_rows = [], []
    for p in keys_found:
        key, meta = load_key_meta(p)
        if key is None:
            key_rows.append(dict(path=str(p.relative_to(ROOT)), error=meta))
            continue
        lang, lang_src = language_for(meta['folder'], meta['lang_hint'], by_lang)
        meta['lang'] = lang; meta['lang_src'] = lang_src
        key_metas.append((p, key, meta))

    ct_metas = [load_ct_meta(p) for p in cts_found]
    # own-ciphertext(s) for each key: same folder as the key file (best available heuristic for co-location)
    for p, key, meta in key_metas:
        meta['own_cts'] = [c['path'] for c in ct_metas if c['folder'] == meta['folder']]

    rows = []           # KEY-CROSSMATCH.tsv rows
    pos_control = []    # positive-control table rows
    unusable = []

    for p, key, meta in key_metas:
        candidates = [c for c in ct_metas if c['sign_type'] == meta['sign_type']]
        scored = []
        for c in candidates:
            cov = coverage_of(key, c['signs'])
            lov = length_overlap(key.keys(), c['signs'])
            # exclude the CIPHERTEXT's own folder from the corpus (item 4: "exclude the target's own"),
            # not the key's -- a key and a candidate ciphertext are usually different folders, and the
            # leakage this guards against is the candidate's own plaintext, not the key's
            model = get_model(meta['lang'], exclude_folder=c['folder'], corpora_map=corpora_map)
            if cov < 0.5 or model is None:
                rows.append(dict(ciphertext_path=c['path'], ct_status=c['status'], key_path=meta['path'],
                                  key_office=meta['office'], key_years=meta['years'], key_lang=meta['lang'],
                                  design=meta['design'], coverage=round(cov, 3), score='', z_shuffled='',
                                  z_unrelated='', rank_of_this_key_for_ct='', verdict='none' if model else 'no_corpus'))
                continue
            real, shuffles = score_pair(key, meta, c['signs'], model)
            scored.append((c, cov, lov, real, shuffles, model))
        # unrelated-key null needs every OTHER compatible key of the same design scored on each ct too
        other_keys = [(op, ok, om) for op, ok, om in key_metas
                      if om['path'] != meta['path'] and om['design'] == meta['design']
                      and om['sign_type'] == meta['sign_type']]
        for c, cov, lov, real, shuffles, model in scored:
            z_sh = zscore(real, shuffles)
            null_scores = []
            for op, ok, om in other_keys:
                omodel = model if om['lang'] == meta['lang'] else \
                    get_model(om['lang'], exclude_folder=c['folder'], corpora_map=corpora_map)
                if omodel is None:
                    continue
                otext, ocov = decode_with(ok, c['signs'])
                if not otext.strip():
                    continue
                null_scores.append(omodel.score(otext))
            z_un = zscore(real, null_scores) if len(null_scores) >= 2 else None
            is_own = c['path'] in meta['own_cts']
            if is_own:
                verdict = 'own'
            elif z_sh is not None and z_un is not None and z_sh >= 4 and z_un >= 4 and cov >= 0.7:
                verdict = 'hit'
            elif z_sh is not None and z_un is not None and z_sh >= 2.5 and z_un >= 2.5:
                verdict = 'weak'
            else:
                verdict = 'none'
            rows.append(dict(ciphertext_path=c['path'], ct_status=c['status'], key_path=meta['path'],
                              key_office=meta['office'], key_years=meta['years'], key_lang=meta['lang'],
                              design=meta['design'], coverage=round(cov, 3), score=round(real, 4),
                              z_shuffled=round(z_sh, 2) if z_sh is not None else '',
                              z_unrelated=round(z_un, 2) if z_un is not None else '',
                              rank_of_this_key_for_ct='', verdict=verdict,
                              _real=real, _z_sh=z_sh, _z_un=z_un))
        # positive control: does this key rank its own ciphertext(s) first among same-sign-type candidates?
        if meta['own_cts']:
            ranked = sorted([r for r in rows if r['key_path'] == meta['path'] and r['ciphertext_path'] in
                             [c['path'] for c in candidates] and r.get('_real') is not None],
                            key=lambda r: r['_real'], reverse=True)
            own_rank = next((i + 1 for i, r in enumerate(ranked) if r['ciphertext_path'] in meta['own_cts']), None)
            own_row = next((r for r in ranked if r['ciphertext_path'] in meta['own_cts']), None)
            for i, r in enumerate(ranked):
                if r['ciphertext_path'] in meta['own_cts']:
                    r['rank_of_this_key_for_ct'] = i + 1
            ok = bool(own_row and own_rank == 1 and own_row['_z_sh'] is not None and own_row['_z_un'] is not None
                      and own_row['_z_sh'] >= 4 and own_row['_z_un'] >= 4)
            pos_control.append(dict(key=meta['path'], own_text=', '.join(meta['own_cts']), own_rank=own_rank,
                                     z_sh=own_row['_z_sh'] if own_row else None,
                                     z_un=own_row['_z_un'] if own_row else None, ok=ok,
                                     n_candidates=len(ranked)))
            if not ok:
                unusable.append((meta['path'], f"own-text rank {own_rank} of {len(ranked)}"
                                 if own_rank else "own text not scored (no corpus or coverage<0.5)"))
        else:
            pos_control.append(dict(key=meta['path'], own_text='(no co-located ciphertext found)', own_rank=None,
                                     z_sh=None, z_un=None, ok=None, n_candidates=len(candidates)))

    unusable_paths = {u[0] for u in unusable}
    for r in rows:
        if r['key_path'] in unusable_paths and r['verdict'] not in ('own',):
            r['verdict'] = 'unusable-key'

    return dict(keys_found=keys_found, keys_dropped=keys_dropped, cts_found=cts_found, cts_dropped=cts_dropped,
                key_metas=key_metas, ct_metas=ct_metas, rows=rows, pos_control=pos_control, unusable=unusable,
                corpora_map=corpora_map)


def write_tsv(rows, path):
    cols = ['ciphertext_path', 'ct_status', 'key_path', 'key_office', 'key_years', 'key_lang', 'design',
            'coverage', 'score', 'z_shuffled', 'z_unrelated', 'rank_of_this_key_for_ct', 'verdict']
    order = {'hit': 0, 'weak': 1}
    def sortkey(r):
        z = r.get('z_shuffled')
        z = z if isinstance(z, (int, float)) else -999
        return (order.get(r['verdict'], 2), -z)
    rows = sorted(rows, key=sortkey)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out-tsv', default=str(ROOT / 'KEY-CROSSMATCH.tsv'))
    ap.add_argument('--out-md', default=str(ROOT / 'KEY-CROSSMATCH.md'))
    ap.add_argument('--quiet', action='store_true')
    a = ap.parse_args(argv)
    res = run()
    sorted_rows = write_tsv(res['rows'], a.out_tsv)
    n_ok = sum(1 for pc in res['pos_control'] if pc['ok'])
    n_total = len(res['pos_control'])
    hits = [r for r in sorted_rows if r['verdict'] == 'hit']
    weak = [r for r in sorted_rows if r['verdict'] == 'weak']
    if not a.quiet:
        print(f"positive control: {n_ok} of {n_total} keys rank their own text first; "
              f"{len(hits)} hits, {len(weak)} weak")
        for r in hits + weak:
            print(f"  {r['verdict']}: {r['ciphertext_path']} <- {r['key_path']} "
                  f"cov={r['coverage']} z_sh={r['z_shuffled']} z_un={r['z_unrelated']}")
    return res


if __name__ == '__main__':
    main()
