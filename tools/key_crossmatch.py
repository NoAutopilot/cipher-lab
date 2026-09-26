#!/usr/bin/env python3
"""key_crossmatch.py: can any key table we hold read any ciphertext on disk it was not built for? (LANE KX job 1)

  python3 tools/key_crossmatch.py                 run the full sweep, write KEY-CROSSMATCH.tsv + print a summary
  python3 tools/key_crossmatch.py --calibrate     fit the gate on the verified readings (KEY-CROSSMATCH-CAL.tsv)
  python3 tools/key_crossmatch.py --since-hours 25 --post-room
                                                  nightly: pairs whose key or ciphertext changed, hits to ROOM.md
  python3 tools/key_crossmatch.py --help
  python3 tools/tests/test_key_crossmatch.py       offline test: positive control on two small fixtures

Pipeline (CLAUDE.md rules 3, 4, 7; LANE KX job briefs 2026-09-25, jobs 1 and 1b):
  1. Discover every key*.tsv/key*.txt under ciphers/ (excluding scratch names: draft, candidate, atlas, pass,
     conflicts, counts, align, crosscheck, trial) plus the published key tables already on disk
     (tools/keys/key60.tsv). Parse each with tools/decode_key.py's own load_key (imported, not copied) into
     {code: value}, falling back to this script's own robust_load_key when dk.load_key raises or clearly read
     an un-stripped header row as data (job 1b fix A: header words like 'line'/'system'/'row'/'sign_desc' that
     dk's own header sniffing does not recognise, plus 'code'-headed tables whose value column is named
     'plaintext' rather than 'value'). Metadata (office, years, language, design, sign type) is read from the
     folder's NOTES.md and the key file's own header comment, by regex heuristics -- reported, not authoritative.
  2. Discover every ciphertext*.tsv/.txt under ciphers/ (same exclusion list, plus 'recon': intermediate
     reconciliation passes are not independent ciphertexts). Tokenise using the folder's decode.json job that
     names the file when one exists; else try tools/decode_key.py's own format auto-detection; else this
     script's own robust_tsv_signs (a header-name-driven TSV sign extractor, for files dk's stricter 'tsv'
     format detector or a stale decode.json miss); else a plain whitespace/semicolon split treating any
     alphabetic run of 4+ letters as clear prose (reported as 'whitespace').
  3. Own-text (positive-control) pairing (job 1b fix A): a key's own ciphertext(s) come from its folder's
     decode.json job list when one exists (authoritative -- a key decode.json does not name, e.g.
     huntington-luzerne-destouches-1781/key_tomokiyo.tsv, gets no forced pairing); else, for a folder with
     exactly one key, every ciphertext in the folder (the old rule, still correct there); else a shared 3+
     digit run in both basenames or the key's "person name" in the ciphertext's own "Cipher system:" header
     line, with the one remaining unmatched key in a folder getting whatever is left over. See
     compute_own_cts()'s docstring for the full reasoning and worked examples (thurloe-printed,
     august-van-saksen-1561-64, jan-van-nassau-1572-75).
  4. Compatibility filter: same sign type (digits / letters / symbols / mixed) and coverage (share of the
     ciphertext's token occurrences whose code the key contains) >= 0.5 to proceed to scoring; the rest are
     listed with coverage only. Two lists of named pairs (KNOWN_PAIRS, NEGATIVE_PAIRS) are forced into the
     sweep regardless of this filter, per the job brief's rule-3 requirement to report a matched control's
     numbers even when the result is a clean negative.
  5. Score: decode with the key (first alternative of an 'a|b' value; unkeyed signs contribute nothing), score
     the folded letter stream with judge_plaintext.py's NgramModel (imported) in the key's language. Corpora:
     tools/data/{de16,fr16,it16} and modern English ship with the repo; la/nl/pt/es/16-17th c. English do not,
     so this script builds one per language from this repo's own reading*.txt/plaintext*.txt files (detected by
     function-word matching, not by folder name) under tools/data/<lang>_repo/, excluding the file under test.
  6. Controls (job 1b fix B): (a) the same key with values shuffled among its own codes, >=20 draws, z-score
     (z_shuffled); (b) judge_plaintext.py's own calibrated language control -- NgramModel.controls(N, samples)
     draws real-text and letter-shuffled windows of the same length N from the scoring corpus itself, so it
     needs no second same-design key (the old "unrelated key" null was unmeasurable for most designs, which
     had only 2-5 keys on disk). pass_null: score beats the shuffled-window 99th percentile. pass_real: score
     beats the real-text 5th percentile. dictword_share: fraction of the decoded letters a greedy dictionary
     segmentation covers (a second, cheap signal, not itself a gate). Verdict: hit (coverage>=0.7, z_shuffled>=4,
     pass_real and pass_null), weak (coverage>=0.5, z_shuffled>=3, pass_null), else none.
  7. Positive control: every key must rank its own ciphertext(s) first among all same-sign-type ciphertexts,
     own-quality (z_shuffled>=4, pass_real, pass_null), before any other row involving it is trusted; a key
     that fails is marked 'unusable' with the reason and excluded from the hit list.

  8. (XMATCH-CAL, 26 Sept 2026: supersedes the verdict rules of items 6-7.) Verdicts come from a gate fitted by
     --calibrate on the verified readings (VERIFIED_PAIRS): stat = max(z 4-gram, z value-frequency) against 20
     class-shuffled-value keys, hit when stat >= the gate on a ciphertext of >= MIN_TOKENS tokens with coverage
     >= 0.5, 'short' when it clears on a shorter text. Numbers and caveats: KEY-CROSSMATCH.md, KEY-CROSSMATCH-CAL.tsv.

Output: KEY-CROSSMATCH.tsv (all pairs with coverage >= 0.5, plus the forced known/negative pairs and the
positive-control rows) and KEY-CROSSMATCH.md (method, positive-control table, hit list, at most 50 lines).
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


# ---------------------------------------------------------------- robust key loading (LANE KX job 1b, fix A)
# dk.load_key only recognises a plain-text (uncommented) header row when its FIRST cell is literally 'code',
# 'sign' or 'token' (tools/decode_key.py with_header); any other real column name (line, system, row, group,
# item, figure, sign_desc, type -- all found on disk in this repo's own key tables) means the header row is
# never stripped and is read as a bogus first DATA row instead (e.g. key['system'] = {'value': 'sign'}), which
# both pollutes the key and, worse, can silently overwrite real codes that share a header word by coincidence.
# Two keys (clair1067-brienne-poland-1646 and fr5160-letellier-1653's key_brienne_1647/1651.tsv, header
# 'code<TAB>plaintext') fail even harder: 'code' IS stripped correctly, but dk.load_key's vi = col(header,
# 'value') finds no 'plaintext' column at all and crashes (r[None]) -- these were unparseable before this fix.
# Rather than change decode_key.py (out of this job's file scope, and it is the reference for folders with a
# decode.json -- CLAUDE.md rule 7, job brief note "tools/decode_key.py's own decoding is the reference"), this
# adds a second, more permissive loader used ONLY as a fallback: when dk.load_key raises, or when its first
# parsed code is itself a column-name word (strong evidence the header leaked into the data).
KNOWN_HEADER_WORDS = {
    'code', 'sign', 'token', 'value', 'grade', 'source', 'note', 'line', 'pos', 'position', 'index', 'idx',
    'folio', 'conf', 'confidence', 'system', 'group', 'row', 'type', 'id', 'key', 'entry_label', 'token_type',
    'sign_desc', 'top', 'bot', 'item', 'figure', 'n', 'units', 'occurrences', 'other_values', 'evidence',
    'gloss', 'meaning', 'kind', 'alphabet', 'nulls', 'nomenclator', 'trim', 'trailing_period', 'book_page',
    'book_col', 'rank', 'alt', 'letter', 'plaintext', 'glossed_h_columns', 'groups_keyed_by_other_items',
    'same_value', 'share', 'positions', 'image_ref', 'layer', 'is_null', 'leaf', 'src_pos', 'page',
    'page_of_letter', 'is_null', 'grades', 'gloss_raw',
}
# code column: prefer an explicit 'code'/'sign'/'token' name (dk's own convention) before the looser
# alternatives this repo's other key tables actually use (checked by hand against every file above).
CODE_COL_PRIORITY = ['code', 'sign_code', 'sign', 'token', 'group', 'item', 'figure', 'sign_desc', 'row',
                      'system', 'id', 'key']
# value column: a key table with none of these names has no plaintext/meaning column at all and is not a
# code->value lookup (huntington-blathwayt-madrid-1728/key_items.tsv: a per-item coverage STATISTICS table,
# 'item glossed_H_columns groups_keyed_by_other_items same_value share' -- caught by this list, not guessed).
# 'plain' is fr5761-election-1519/key.tsv's own name for the plaintext letter (its code column is 'sign_code'
# -- code and value are the two ends of this table's own name for each, not dk.load_key's names for either).
VALUE_COL_PRIORITY = ['value', 'plain', 'plaintext', 'gloss', 'meaning']


def pick_col(names_priority, low_header):
    for n in names_priority:
        if n in low_header:
            return low_header.index(n)
    return None


def robust_load_key(path):
    """Fallback key loader: treats the first non-comment line as a header if dk.load_key could not use it,
    matches the code/value columns by name (CODE_COL_PRIORITY / VALUE_COL_PRIORITY) instead of position, and
    refuses to guess a value column that isn't there. Returns (key, None) or (None, reason)."""
    try:
        raw = Path(path).read_text(encoding='utf-8', errors='replace').splitlines()
    except Exception as e:
        return None, f'unreadable: {e}'
    lines = [l for l in raw if l.strip() and not l.lstrip().startswith('#')]
    if not lines:
        return None, 'no data lines'
    header_cells = lines[0].split('\t')
    low = [c.strip().lower() for c in header_cells]
    value_idx = pick_col(VALUE_COL_PRIORITY, low)
    if value_idx is None:
        return None, 'no value/plaintext/gloss/meaning column -- not a code->value key table'
    code_idx = pick_col(CODE_COL_PRIORITY, low)
    if code_idx is None:
        code_idx = 0
    key = {}
    for l in lines[1:]:
        cells = l.split('\t')
        if len(cells) <= max(code_idx, value_idx):
            continue
        code, value = cells[code_idx].strip(), cells[value_idx].strip()
        if not code:
            continue
        key[code] = {'value': value, 'source': '', 'note': ''}
    if not key:
        return None, 'no rows parsed'
    return key, None


def load_key_meta(path):
    """One key's rows plus a metadata dict; None (logged) if unparseable."""
    try:
        key = dk.load_key(str(path))
    except Exception:
        key = None
    if key:
        first_code = next(iter(key), None)
        if first_code is not None and first_code.strip().lower() in KNOWN_HEADER_WORDS:
            key = None  # dk.load_key's header wasn't stripped -- fall through to the robust loader
    if not key:
        key, reason = robust_load_key(path)
        if key is None:
            return None, reason
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


# sign column: same priority as CODE_COL_PRIORITY's code side, plus 'sign_desc' for the glyph-description
# tables that have no Unicode code point of their own (willem-van-hessen-1567/siblings/ciphertext_1069.tsv).
CT_SIGN_COL_PRIORITY = ['sign', 'token', 'code', 'group', 'sign_desc']
# a column carrying either of these marks a row as clear prose / a non-signal filler, not a cipher sign
# (clair1108-duvergier/ciphertext.tsv 'layer'=clear|cipher; antt-linhares-chave/ciphertext.tsv 'is_null').
CT_KIND_COL = ['layer', 'kind']
CT_KIND_SKIP_VALUES = {'clear', 'word', 'plain'}
CT_NULL_COL = ['is_null']


def robust_tsv_signs(path):
    """Fallback tokenizer for a well-formed TSV ciphertext file whose header dk.detect_format/LOADERS does not
    recognise (h[0] must be literally 'line' for dk's own 'tsv' format, e.g. clair1108-duvergier/ciphertext.tsv
    has 'leaf' first and dk falls to its 'rows' format, which expects a completely different shape and yields
    <3 signs) -- or whose decode.json job points at a differently-named file that never matches this one
    (clair1108-duvergier/decode.json job names 'signs.tsv'; the file on disk is 'ciphertext.tsv'). Finds the
    sign column by name (CT_SIGN_COL_PRIORITY) rather than position, and skips rows a 'layer'/'kind' or
    'is_null' column marks as clear text / not a signal, same convention as the whitespace fallback's
    CLEAR_WORD_RE and dk.clear_word()."""
    try:
        raw = path.read_text(encoding='utf-8', errors='replace').splitlines()
    except Exception:
        return None
    lines = [l for l in raw if l.strip() and not l.lstrip().startswith('#')]
    if len(lines) < 2:
        return None
    header = lines[0].split('\t')
    low = [c.strip().lower() for c in header]
    sign_idx = pick_col(CT_SIGN_COL_PRIORITY, low)
    if sign_idx is None:
        return None
    kind_idx = pick_col(CT_KIND_COL, low)
    null_idx = pick_col(CT_NULL_COL, low)
    signs = []
    for l in lines[1:]:
        cells = l.split('\t')
        if len(cells) <= sign_idx:
            continue
        if kind_idx is not None and len(cells) > kind_idx and cells[kind_idx].strip().lower() in CT_KIND_SKIP_VALUES:
            continue
        if null_idx is not None and len(cells) > null_idx and cells[null_idx].strip().lower() in ('true', '1', 'yes'):
            continue
        tok = cells[sign_idx].strip()
        if not tok or dk.clear_word(tok) is not None:
            continue
        signs.append(tok)
    return signs if len(signs) >= 3 else None


# jan-van-nassau-1572-75/ciphertext_5551.tsv's own header states its convention explicitly: "Format:
# tools/decode_key.py 'tsv' (line pos token conf), clear_prefix '='" -- but this folder has no decode.json, so
# the auto:tsv tier calls dk.LOADERS['tsv'] with an EMPTY job ({}), which never sets clear_prefix and leaves
# '=van'/'=will'/'=?' as literal sign tokens instead of the clear (non-cipher) words they are (dk.clear_word()
# only recognises its own 'w:' and '[PLAIN:...]' conventions, not this folder's '='). Applied as a final pass
# regardless of which tier produced the signs, since decode.json can be present for other files in the same
# folder without covering this one, and the auto tiers pass job={} unconditionally.
def drop_equals_clear(signs):
    return [s for s in signs if not (s.startswith('=') and len(s) > 1)]


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
                return drop_equals_clear(signs), f'decode.json:{fmt}'
        except Exception:
            pass
    try:
        fmt = dk.detect_format(str(path))
        recs = dk.LOADERS[fmt](str(path), {})
        signs = [r['sign'] for r in recs if r['kind'] == 'sign']
        if len(signs) >= 3:
            return drop_equals_clear(signs), f'auto:{fmt}'
    except Exception:
        pass
    robust = robust_tsv_signs(path)
    if robust is not None:
        return drop_equals_clear(robust), 'robust_tsv'
    text = path.read_text(encoding='utf-8', errors='replace')
    return drop_equals_clear(whitespace_signs(text)), 'whitespace'


def has_reading(folder):
    return any((CIPHERS / folder).glob('reading*.txt')) or any((CIPHERS / folder).glob('plaintext*.txt'))


def load_ct_meta(path):
    folder = folder_of(path)
    signs, method = tokenize_ciphertext(path)
    status, office, years, lang_hint = notes_meta(folder)
    return dict(path=str(path.relative_to(ROOT)), folder=folder, signs=signs, tok_method=method,
                status=status, office=office, years=years, lang_hint=lang_hint,
                sign_type=sign_type(signs), has_reading=has_reading(folder))


# ==================================================================== own-text (positive-control) pairing
# (LANE KX job 1b, fix A) folder_of() collapses everything under ciphers/<folder>/... to one name, so "same
# folder" was standing in for "own ciphertext" -- correct for a folder with exactly one key, wrong for one
# with several. thurloe-printed alone has 9 key_*.tsv files at its top level and ~23 P<n>/ciphertext.txt
# letters below them; only some of those letters have an identified cipher system (their own header names it,
# e.g. "Cipher system: Blake's cipher"), the rest are still unidentified -- the old heuristic called EVERY
# P<n> letter "own" text for EVERY key in the folder, which is both wrong (a key can't fail a positive control
# on text nobody ever claimed it reads) and exactly backwards for what this lane is for (reading those
# unidentified letters is the actual cross-match candidate, not a positive-control failure). august-van-saksen
# has the analogous problem one level down (key_53/74/98.tsv, each built for one specific ciphertext_NN.tsv --
# but its own decode.json already states the pairing explicitly, job by job).
# Three tiers, most authoritative first:
#  1. decode.json job list: authoritative when it exists. A key not named by any job in its folder's
#     decode.json gets no forced own-text (huntington-luzerne-destouches-1781/key_tomokiyo.tsv is not
#     decode.json's key.tsv -- correctly reported as "no co-located ciphertext", not forced onto ciphertext.tsv).
#  2. no decode.json, exactly one key in the folder: unambiguous, same as the old same-folder rule.
#  3. no decode.json, several keys: try two positive signals per (key, ciphertext) pair -- a shared 3+-digit
#     run in both basenames (key_53.tsv <-> ciphertext_53.tsv; key_1069.tsv <-> ciphertext_1069.tsv;
#     key_1659_f86only.tsv <-> ciphertext_f86.tsv) or the key's "person name" (key_blake_extended.tsv ->
#     "blake") appearing in the ciphertext's own "Cipher system:" header line. A key matched to nothing keeps
#     an empty own_cts UNLESS it is the single remaining unmatched key in the folder after the others have
#     claimed theirs, in which case it gets what's left (process of elimination: jan-van-nassau-1572-75's
#     key_5549.tsv digit-matches ciphertext_5549.tsv/_ps.tsv, leaving key_1572.tsv -- the shared office table,
#     no digits of its own -- the remaining ciphertexts, which is exactly right). An empty own_cts is reported
#     as "no co-located ciphertext found", never as a failure (rule 3: no negative without a matched control).
DIGIT_RUN_RE = re.compile(r'\d{2,}')
KEY_NAME_STRIP_SUFFIX_RE = re.compile(
    r'_(extended|ext|items|candidates|nomenclator|only|from_gloss|example|f\d+only)$', re.I)
_CT_HEADER_CACHE = {}


def ct_header_text(rel_path):
    if rel_path not in _CT_HEADER_CACHE:
        text = ''
        try:
            for l in (ROOT / rel_path).read_text(encoding='utf-8', errors='replace').splitlines()[:15]:
                m = re.search(r'cipher system\s*:\s*(.*)', l, re.I)
                if m:
                    text = m.group(1); break
        except Exception:
            pass
        _CT_HEADER_CACHE[rel_path] = text
    return _CT_HEADER_CACHE[rel_path]


def key_person_name(key_basename):
    stem = re.sub(r'\.(tsv|txt)$', '', key_basename, flags=re.I)
    stem = re.sub(r'^key_', '', stem, flags=re.I)
    stem = KEY_NAME_STRIP_SUFFIX_RE.sub('', stem)
    m = re.match(r'^([a-zA-Z]+)', stem)
    return m.group(1).lower() if m else None


def compute_own_cts(key_metas, ct_metas, decode_jobs_by_folder):
    """Sets meta['own_cts'] on every (path, key, meta) in key_metas, per the three tiers above."""
    from collections import defaultdict
    folder_keys = defaultdict(list)
    for p, key, meta in key_metas:
        folder_keys[meta['folder']].append((p, key, meta))
    for folder, items in folder_keys.items():
        same_folder_cts = [c for c in ct_metas if c['folder'] == folder]
        jobs = decode_jobs_by_folder.get(folder)
        if jobs:
            for p, key, meta in items:
                key_base = Path(p).name
                names = {os.path.basename(j['ciphertext']) for j in jobs
                         if j.get('key') and os.path.basename(j['key']) == key_base and j.get('ciphertext')}
                meta['own_cts'] = [c['path'] for c in same_folder_cts if os.path.basename(c['path']) in names]
            continue
        if len(items) <= 1:
            for p, key, meta in items:
                meta['own_cts'] = [c['path'] for c in same_folder_cts]
            continue
        assigned, claimed = {}, set()
        for p, key, meta in items:
            key_base = Path(p).name
            kd = set(DIGIT_RUN_RE.findall(key_base))
            name = key_person_name(key_base)
            matches = []
            for c in same_folder_cts:
                cd = set(DIGIT_RUN_RE.findall(os.path.basename(c['path'])))
                if kd & cd or (name and name in ct_header_text(c['path']).lower()):
                    matches.append(c['path'])
            assigned[p] = matches
            claimed.update(matches)
        unresolved = [p for p, key, meta in items if not assigned[p]]
        if len(unresolved) == 1:
            assigned[unresolved[0]] = [c['path'] for c in same_folder_cts if c['path'] not in claimed]
        for p, key, meta in items:
            meta['own_cts'] = assigned[p]


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
    attach_freqs(model, texts)
    _MODEL_CACHE[key] = model
    return model


def attach_freqs(model, texts):
    """Word and letter relative frequencies from the same corpus texts, for value_freq_score (XMATCH-CAL)."""
    from collections import Counter
    words = Counter()
    for t in texts:
        words.update(jp.fold(w) for w in re.findall(r"[^\W\d_]+", t))
    words.pop('', None)
    letters = Counter(model.raw)
    model.word_tot = sum(words.values()) or 1
    model.letter_tot = sum(letters.values()) or 1
    model.wordfreq, model.letterfreq = words, letters


def value_freq_score(key, signs, model, floor=1e-7):
    """Mean log10 corpus frequency of each decoded token's value: a single letter by its letter share, a longer
    value by its share as a whole word (floor for a value never seen as a word, e.g. a syllable or a name). A
    true key sends the text's frequent codes to the language's frequent letters and words ('de', 'la', 'e');
    a value-shuffled key does not. The letter 4-gram score cannot see this for a code whose values are all
    whole words, because any shuffle of words still reads as words (XMATCH-CAL: 7 of 18 verified pairs had
    n-gram z_shuffled < 2 for that reason)."""
    tot = n = 0
    for sg in signs:
        row = key.get(sg)
        if not row or not row.get('value'):
            continue
        v = jp.fold(row['value'].split('|')[0])
        if not v:
            continue
        f = (model.letterfreq.get(v, 0) / model.letter_tot) if len(v) == 1 else (model.wordfreq.get(v, 0) / model.word_tot)
        tot += math.log10(max(f, floor)); n += 1
    return tot / n if n else None


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


# ==================================================================== calibrated language control (fix B)
# The "unrelated key of the same design" z-score (a second key of the same design, scored on the same
# ciphertext, as the null) was the second positive-control bottleneck: most designs have only 2-5 keys on
# disk, so z_unrelated was unmeasurable for 5 keys and a real-but-thin, under-4 z for 7 more (KEY-CROSSMATCH.md,
# 25 Sept 2026 run). judge_plaintext.py already implements a calibrated control that does not depend on having
# enough sibling keys: NgramModel.controls(N, samples) draws real-text windows AND letter-shuffled windows of
# the SAME length N from the scoring corpus itself, so it works with as few as one key. This replaces
# z_unrelated with judge_plaintext's own two checks: the decode must score above the null (shuffled-window)
# 99th percentile (mechanical: could this be by chance at all) AND above the real-text 5th percentile
# (calibrated: does it read as well as genuine period prose of the same length, not merely non-random).
CONTROLS_SAMPLES = 60
_CONTROLS_CACHE = {}


def lang_controls(model, N, samples=CONTROLS_SAMPLES):
    """(real, null, cov) sorted score lists for windows near length N (bucketed to the nearest 20 letters so
    many same-length-ish candidates share one cache entry -- ~115 ciphertexts x up to 56 keys would otherwise
    rebuild this per exact N, and NgramModel.controls's shuffled-window draws are the sweep's main cost)."""
    if N <= 0:
        return None
    bucket = max(20, round(N / 20) * 20)
    key = (id(model), bucket)
    if key not in _CONTROLS_CACHE:
        _CONTROLS_CACHE[key] = model.controls(bucket, samples=samples)
    return _CONTROLS_CACHE[key]


def score_one_pair(key, meta, c, corpora_map, n_shuffle=20, seed=0, controls_samples=CONTROLS_SAMPLES, gate=None):
    """Full scoring for one (key, ciphertext) pair: coverage gate, shuffled-key control (z_shuffled), and the
    calibrated real-text / null-window controls (pass_real, pass_null, dictword_share). Returns a dict with
    the tsv-ready fields plus _real/_z_sh for ranking; verdict is 'none'/'no_corpus'/'hit'/'short'/'uncalibrated' (gate_verdict) -- the
    caller overrides to 'own' by own_cts membership, which this function does not know about."""
    cov = coverage_of(key, c['signs'])
    model = get_model(meta['lang'], exclude_folder=c['folder'], corpora_map=corpora_map)
    out = dict(coverage=round(cov, 3), score='', z_shuffled='', z_valuefreq='', stat='', n_tokens=len(c['signs']),
               pass_real='', pass_null='', dictword_share='', _real=None, _z_sh=None, _stat=None)
    if cov < 0.5 or model is None:
        out['verdict'] = 'none' if model else 'no_corpus'
        return out
    ps = pair_stats(key, c['signs'], model, n_shuffle=n_shuffle, seed=seed)
    real, z_sh, z_vf, stat = ps['own']['score'], ps['own']['z_ng'], ps['own']['z_vf'], ps['own']['stat']
    text, _ = decode_with(key, c['signs'])
    N = len(jp.fold(text))
    ctrl = lang_controls(model, N, samples=controls_samples)
    if ctrl:
        real_c, null_c, _cov_c = ctrl
        pass_null = real > jp.pct(null_c, 0.99)
        pass_real = real > jp.pct(real_c, 0.05)
        dictword_share = round(model.cover(text), 3)
    else:
        pass_null = pass_real = False
        dictword_share = 0.0
    out.update(score=round(real, 4), z_shuffled=round(z_sh, 2) if z_sh is not None else '',
               z_valuefreq=round(z_vf, 2) if z_vf is not None else '', stat=round(stat, 2) if stat is not None else '',
               n_tokens=len(c['signs']),
               pass_real=pass_real, pass_null=pass_null, dictword_share=dictword_share, _real=real, _z_sh=z_sh,
               _stat=stat)
    out['verdict'] = gate_verdict(stat, cov, len(c['signs']), gate or load_gate())
    return out


def gate_verdict(stat, coverage, n_tokens, gate):
    """hit: clears the calibrated gate (KEY-CROSSMATCH-CAL.tsv) in the stratum it was fitted on; short: clears
    the stat but the ciphertext is below the calibrated length, where no gate separated verified pairs from the
    null (a lead to read by eye, not a hit); none otherwise. With no gate file on disk, 'uncalibrated'."""
    if gate is None:
        return 'uncalibrated'
    if stat is None or coverage < gate['min_coverage'] or stat < gate['stat_min']:
        return 'none'
    return 'hit' if n_tokens >= gate['min_tokens'] else 'short'


# ==================================================================== calibrated gate (XMATCH-CAL, 26 Sept 2026)
# The 25 Sept verdict required pass_real, which cleared for none of the 35 own-text pairs, including the
# independently verified readings: the gate was set by the corpus, not by our own known-good decodes. The gate is
# now fitted to them. Positive controls: every own-text pair whose reading is verified (status.json N3/N4 after
# two audits, V-GATE2 26 Sept 2026 18:03; plus oxenstierna, which the brief names as independently verified).
# Null: the same key with its values shuffled among its own codes, 20 draws per pair, each draw scored as if it
# were a candidate (its z against the other 19 draws: leave-one-out). A shuffled-value key is exactly "a key of
# the same design, the same value set, the wrong mapping" -- the thing a cross-match hit must beat. Two
# statistics: z_shuffled (the decode against its own key-shuffle null) and lang_pos, the decode's place between
# the corpus's shuffled-window 99th percentile (0) and its real-window 5th percentile (1) at the same length --
# a continuous version of pass_null/pass_real. The gate is the pair (z_min, pos_min) = the smallest value any
# verified pair reaches on each, so every verified pair is admitted by construction; the false-positive rate is
# the share of null draws that clear both. Fitted by `--calibrate`, stored in GATE_FILE, read by the sweep.
GATE_FILE = DATA / 'key_crossmatch_gate.json'
CAL_TSV = ROOT / 'KEY-CROSSMATCH-CAL.tsv'
# (key path, ciphertext path, tier, why) -- tier 'verified' fits the gate; tier 'print' (plaintext already in
# print, N0/N1 rows) is scored and reported as a check on the gate, never used to fit it.
VERIFIED_PAIRS = [
    ('ciphers/fr2980-gramont/key.tsv', 'ciphers/fr2980-gramont/ciphertext.txt', 'verified', 'N4 two audits (f.29r)'),
    ('ciphers/fr2980-gramont/key_extension_f30.tsv', 'ciphers/fr2980-gramont/ciphertext_f30.tsv', 'verified', 'N4 two audits (f.30)'),
    ('ciphers/fr20140-danzay-1557/key.tsv', 'ciphers/fr20140-danzay-1557/ciphertext.txt', 'verified', 'N3/N4 two audits'),
    ('ciphers/fr20140-danzay-1557/key.tsv', 'ciphers/fr20140-danzay-1557/ciphertext_f36.tsv', 'verified', 'N3/N4 two audits'),
    ('ciphers/lodewijk-van-nassau-1573-74/key.tsv', 'ciphers/lodewijk-van-nassau-1573-74/ciphertext_4610.tsv', 'verified', 'N3/N4 two audits'),
    ('ciphers/lodewijk-van-nassau-1573-74/key.tsv', 'ciphers/lodewijk-van-nassau-1573-74/ciphertext_4611.tsv', 'verified', 'N3/N4 two audits'),
    ('ciphers/lodewijk-van-nassau-1573-74/key.tsv', 'ciphers/lodewijk-van-nassau-1573-74/ciphertext_4612.tsv', 'verified', 'N3/N4 two audits'),
    ('ciphers/lodewijk-van-nassau-1573-74/key.tsv', 'ciphers/lodewijk-van-nassau-1573-74/ciphertext_4616.tsv', 'verified', 'N3/N4 two audits'),
    ('ciphers/lodewijk-van-nassau-1573-74/key.tsv', 'ciphers/lodewijk-van-nassau-1573-74/ciphertext_5797.tsv', 'verified', 'N4 two audits (5797)'),
    ('ciphers/august-van-saksen-1561-64/key_53.tsv', 'ciphers/august-van-saksen-1561-64/ciphertext_53.tsv', 'verified', 'N4 two audits'),
    ('ciphers/august-van-saksen-1561-64/key_74.tsv', 'ciphers/august-van-saksen-1561-64/ciphertext_57.tsv', 'verified', 'N4 two audits'),
    ('ciphers/august-van-saksen-1561-64/key_98.tsv', 'ciphers/august-van-saksen-1561-64/ciphertext_126.tsv', 'verified', 'N4 two audits'),
    ('ciphers/jan-van-nassau-1572-75/key_1572.tsv', 'ciphers/jan-van-nassau-1572-75/ciphertext_5551.tsv', 'verified', 'N3 two audits (5551)'),
    ('ciphers/espagnol142-mercy-1648/key.tsv', 'ciphers/espagnol142-mercy-1648/ciphertext.tsv', 'verified', 'N3 two audits'),
    ('ciphers/antt-linhares-chave/key.tsv', 'ciphers/antt-linhares-chave/ciphertext.tsv', 'verified', 'N3/N4 two audits'),
    ('ciphers/vanbeuningen-dewitt-1657/key.tsv', 'ciphers/vanbeuningen-dewitt-1657/ciphertext.tsv', 'verified', 'N1/N3 two audits'),
    ('ciphers/huntington-blathwayt-madrid-1728/key.tsv', 'ciphers/huntington-blathwayt-madrid-1728/ciphertext_targets.tsv', 'verified', 'N4 two audits'),
    ('ciphers/oxenstierna-gustav-adolf-1632/key.tsv', 'ciphers/oxenstierna-gustav-adolf-1632/ciphertext_key.tsv', 'verified', 'named verified in the XMATCH-CAL brief'),
    ('ciphers/clair1067-brienne-poland-1646/key_1646.tsv', 'ciphers/clair1067-brienne-poland-1646/ciphertext.txt', 'print', 'N0'),
    ('ciphers/fr5160-letellier-1653/key_1659_f86only.tsv', 'ciphers/fr5160-letellier-1653/ciphertext_f86.tsv', 'print', 'N0'),
    ('ciphers/huntington-luzerne-destouches-1781/key.tsv', 'ciphers/huntington-luzerne-destouches-1781/ciphertext.tsv', 'print', 'N0'),
    ('ciphers/rah-canada-1869/key.tsv', 'ciphers/rah-canada-1869/ciphertext.tsv', 'print', 'N0'),
    ('ciphers/clair349-este-guise-1556/key_decode.tsv', 'ciphers/clair349-este-guise-1556/ciphertext.tsv', 'print', 'N0'),
    ('ciphers/gunther-van-schwarzburg-1561/key.tsv', 'ciphers/gunther-van-schwarzburg-1561/ciphertext.tsv', 'print', 'N0'),
    ('ciphers/szembek-bk1560/key.tsv', 'ciphers/szembek-bk1560/ciphertext.tsv', 'print', 'N0'),
    ('ciphers/rah-morillo-1817/key_5186.tsv', 'ciphers/rah-morillo-1817/ciphertext_5186.tsv', 'print', 'N0'),
    ('ciphers/trew-posthius-1614-18/key.tsv', 'ciphers/trew-posthius-1614-18/ciphertext_1614.tsv', 'print', 'N0'),
    ('ciphers/antt-fcc-costacabral-1865/key.tsv', 'ciphers/antt-fcc-costacabral-1865/ciphertext.tsv', 'print', 'N0'),
    ('ciphers/bowes-walsingham-1583/key.tsv', 'ciphers/bowes-walsingham-1583/ciphertext.txt', 'print', 'N1'),
    ('ciphers/thurloe-printed/key_montagu.tsv', 'ciphers/thurloe-printed/P11/ciphertext.txt', 'print', 'N0'),
]


MIN_TOKENS = 100   # below this many ciphertext tokens no gate separated verified pairs from the null (CAL.tsv)
MIN_COVERAGE = 0.5


def loo_z(scores):
    """Leave-one-out z of each score against the others (a null draw treated as if it were a candidate)."""
    return [zscore(s, scores[:i] + scores[i + 1:]) for i, s in enumerate(scores)]


def lang_pos(score, real_c, null_c):
    """0 at the corpus's shuffled-window 99th percentile, 1 at its real-window 5th percentile (same length)."""
    lo, hi = jp.pct(null_c, 0.99), jp.pct(real_c, 0.05)
    return 0.0 if hi == lo else (score - lo) / (hi - lo)


def gate_stat(z_ng, z_vf):
    """The gated statistic: the better of the letter 4-gram z and the value-frequency z, each against the same
    shuffled-value keys. Letter-valued keys are read by the first, word-valued codes by the second."""
    vals = [z for z in (z_ng, z_vf) if z is not None]
    return max(vals) if vals else None


def shuffled_key_by_class(key, rnd):
    """Values shuffled among codes of the same value class only (single letter / longer value / null or empty).
    A plain value shuffle also breaks the design's own structure ('letters on the low codes, words above'),
    so any text whose frequent codes fall where the key keeps its letters beat it: the first calibrated sweep
    found Lodewijk van Nassau's 1574 table 'reading' a 1636 Hessen letter and a 1712 Portuguese appendix that
    way. Shuffling within class keeps that structure in the null and tests only the mapping itself."""
    classes = {}
    for c, row in key.items():
        v = jp.fold((row.get('value') or '').split('|')[0])
        classes.setdefault(0 if not v else (1 if len(v) == 1 else 2), []).append(c)
    out = {}
    for codes in classes.values():
        vals = [key[c]['value'] for c in codes]
        rnd.shuffle(vals)
        out.update({c: {'value': v} for c, v in zip(codes, vals)})
    return out


def pair_stats(key, signs, model, n_shuffle=20, seed=0):
    """Own and shuffled-value-key statistics on one token list: dict(own=(z_ng, z_vf, stat, score), nulls=[...])."""
    rnd = random.Random(seed)
    sks = [shuffled_key_by_class(key, rnd) for _ in range(n_shuffle)]
    def ng(k):
        t, _ = decode_with(k, signs)
        return model.score(t) if t.strip() else -9.9
    ng_real, vf_real = ng(key), value_freq_score(key, signs, model)
    ng_sh = [ng(k) for k in sks]
    vf_sh = [value_freq_score(k, signs, model) for k in sks]
    vf_ok = vf_real is not None and all(v is not None for v in vf_sh)
    z_ng = zscore(ng_real, ng_sh)
    z_vf = zscore(vf_real, vf_sh) if vf_ok else None
    own = dict(score=ng_real, z_ng=z_ng, z_vf=z_vf, stat=gate_stat(z_ng, z_vf))
    lz_ng = loo_z(ng_sh)
    lz_vf = loo_z(vf_sh) if vf_ok else [None] * n_shuffle
    nulls = [dict(score=s, z_ng=a, z_vf=b, stat=gate_stat(a, b)) for s, a, b in zip(ng_sh, lz_ng, lz_vf)]
    return dict(own=own, nulls=nulls)


def calibrate_pair(key, meta, c, corpora_map, n_shuffle=20, seed=0, n_order=5):
    """Own decode + n_shuffle shuffled-value decodes (the null) + n_order decodes of the token-order-shuffled
    ciphertext (rule 3, RETRO-APPLY-T: the family's own decode of shuffled text)."""
    model = get_model(meta['lang'], exclude_folder=c['folder'], corpora_map=corpora_map)
    if model is None:
        return None
    signs = c['signs']
    ps = pair_stats(key, signs, model, n_shuffle=n_shuffle, seed=seed)
    text, _ = decode_with(key, signs)
    N = len(jp.fold(text))
    ctrl = lang_controls(model, N)
    pos = lang_pos(ps['own']['score'], ctrl[0], ctrl[1]) if ctrl else None
    rnd = random.Random(seed + 7)
    orders = []
    for i in range(n_order):
        sh = list(signs); rnd.shuffle(sh)
        orders.append(pair_stats(key, sh, model, n_shuffle=n_shuffle, seed=seed + 100 + i)['own'])
    return dict(own=dict(ps['own'], pos=pos, N=N), nulls=ps['nulls'], orders=orders,
                coverage=round(coverage_of(key, signs), 3), n_tokens=len(signs))


def passes_gate(stat, gate):
    return stat is not None and stat >= gate['stat_min']


def fp_rate(stat_min, null_stats):
    n = len(null_stats)
    k = sum(1 for x in null_stats if x is not None and x >= stat_min)
    return k, n


def choose_gate(verified, null_stats, target_reject=0.99):
    """verified: list of dicts with stat, n_tokens, coverage (tier 'verified' only); null_stats: the null draws'
    stats from pairs in the gated stratum. Returns the gate for the stratum n_tokens >= MIN_TOKENS and
    coverage >= MIN_COVERAGE (the smallest stat any verified pair there reaches, so all are admitted), its
    false-positive rate, and the admit-all gate over every verified pair with its own false-positive rate."""
    strat = [v for v in verified if v['n_tokens'] >= MIN_TOKENS and v['coverage'] >= MIN_COVERAGE]
    below = [v for v in verified if v not in strat]
    stat_min = math.floor(min(v['stat'] for v in strat) * 1000) / 1000  # floor: the minimum itself is admitted
    k, n = fp_rate(stat_min, null_stats['stratum'])
    ns = sorted((x for x in null_stats['stratum'] if x is not None), reverse=True)
    p99 = ns[max(0, int(0.01 * len(ns)) - 1)] if ns else None
    all_min = math.floor(min(v['stat'] for v in verified) * 1000) / 1000
    ka, na = fp_rate(all_min, null_stats['all'])
    return dict(statistic='max(z_ngram, z_valuefreq) vs 20 class-shuffled-value keys', stat_min=stat_min,
                min_tokens=MIN_TOKENS, min_coverage=MIN_COVERAGE,
                n_verified_in_stratum=len(strat), n_verified_below=len(below),
                below_stratum=[f"{v['key_path']} <- {v['ciphertext_path']} (n={v['n_tokens']}, cov={v['coverage']}, stat={v['stat']:.2f})" for v in below],
                fp=k, n_null=n, fp_rate=round(k / n, 4) if n else None, null_stat_p99=round(p99, 3) if p99 is not None else None,
                margin_over_null_p99=round(stat_min - p99, 3) if p99 is not None else None,
                meets_target=bool(n and k / n <= 1 - target_reject),
                admit_all_stat_min=all_min, admit_all_fp=ka, admit_all_n_null=na,
                admit_all_fp_rate=round(ka / na, 4) if na else None)


def load_gate(path=None):
    path = Path(path) if path else GATE_FILE
    return json.loads(path.read_text()) if path.exists() else None


def calibrate(out_tsv=CAL_TSV, gate_file=GATE_FILE, n_shuffle=20):
    """Score every VERIFIED_PAIRS pair on disk, fit the gate on tier 'verified', write the TSV and gate file."""
    by_lang = reading_files_by_lang()
    corpora_map = build_repo_corpora()
    rows, skipped = [], []
    for kp, cp, tier, why in VERIFIED_PAIRS:
        kpath, cpath = ROOT / kp, ROOT / cp
        if not kpath.exists() or not cpath.exists():
            skipped.append((kp, cp, 'not on disk')); continue
        key, meta = load_key_meta(kpath)
        if key is None:
            skipped.append((kp, cp, f'key unparseable: {meta}')); continue
        meta['lang'], _ = language_for(meta['folder'], meta['lang_hint'], by_lang)
        c = load_ct_meta(cpath)
        res = calibrate_pair(key, meta, c, corpora_map, n_shuffle=n_shuffle)
        if res is None:
            skipped.append((kp, cp, f"no scoring corpus for language '{meta['lang']}'")); continue
        o = res['own']
        rows.append(dict(tier=tier, why=why, key_path=kp, ciphertext_path=cp, lang=meta['lang'],
                         coverage=res['coverage'], n_tokens=res['n_tokens'], N_letters=o['N'], score=o['score'],
                         z_ng=o['z_ng'], z_vf=o['z_vf'], stat=o['stat'], lang_pos=o['pos'],
                         _nulls=res['nulls'], _orders=res['orders']))
    ver = [r for r in rows if r['tier'] == 'verified']
    def in_strat(r):
        return r['n_tokens'] >= MIN_TOKENS and r['coverage'] >= MIN_COVERAGE
    null_stats = dict(stratum=[d['stat'] for r in ver if in_strat(r) for d in r['_nulls']],
                      all=[d['stat'] for r in ver for d in r['_nulls']])
    gate = choose_gate(ver, null_stats)
    for r in rows:
        r['in_stratum'] = in_strat(r)
        r['admitted'] = r['in_stratum'] and passes_gate(r['stat'], gate)
        r['null_max'] = max((d['stat'] for d in r['_nulls'] if d['stat'] is not None), default=None)
        r['null_pass'] = sum(1 for d in r['_nulls'] if passes_gate(d['stat'], gate))
        r['order_pass'] = sum(1 for d in r['_orders'] if passes_gate(d['stat'], gate))
    pr = [r for r in rows if r['tier'] == 'print' and r['in_stratum']]
    gate.update(n_print_in_stratum=len(pr), print_admitted=sum(r['admitted'] for r in pr),
                order_shuffle_pass=sum(r['order_pass'] for r in ver if r['in_stratum']),
                order_shuffle_n=sum(len(r['_orders']) for r in ver if r['in_stratum']),
                n_shuffle=n_shuffle, fitted='tools/key_crossmatch.py --calibrate (XMATCH-CAL, 26 Sept 2026)')
    cols = ['tier', 'why', 'key_path', 'ciphertext_path', 'lang', 'coverage', 'n_tokens', 'N_letters', 'score',
            'z_ng', 'z_vf', 'stat', 'lang_pos', 'in_stratum', 'admitted', 'null_max', 'null_pass', 'order_pass']
    def fmt(v):
        return f'{v:.3f}' if isinstance(v, float) else ('' if v is None else str(v))
    with open(out_tsv, 'w', encoding='utf-8') as f:
        f.write(f"# XMATCH-CAL gate: {gate['statistic']} >= {gate['stat_min']} for ciphertexts with >= {MIN_TOKENS} tokens "
                f"and coverage >= {MIN_COVERAGE}. Admits {gate['n_verified_in_stratum']} of {gate['n_verified_in_stratum']} "
                f"verified pairs in that stratum; shuffled-value null draws passing: {gate['fp']} of {gate['n_null']} "
                f"(rate {gate['fp_rate']}, null p99 {gate['null_stat_p99']}, margin {gate['margin_over_null_p99']}). "
                f"Admit-all gate (every verified pair, any length): >= {gate['admit_all_stat_min']}, null pass "
                f"{gate['admit_all_fp']} of {gate['admit_all_n_null']} (rate {gate['admit_all_fp_rate']}). "
                f"Print-tier admitted {gate['print_admitted']} of {gate['n_print_in_stratum']}. Token-order-shuffled own "
                f"decodes passing {gate['order_shuffle_pass']} of {gate['order_shuffle_n']} (see KEY-CROSSMATCH.md).\n")
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(fmt(r.get(c)) for c in cols) + '\n')
        for kp, cp, why in skipped:
            f.write('\t'.join(['skipped', why, kp, cp] + [''] * (len(cols) - 4)) + '\n')
    Path(gate_file).write_text(json.dumps(gate, indent=1) + '\n')
    return gate, rows, skipped


# ---------------------------------------------------------------- known-reuse and negative pairs (job §2, §3)
# Named explicitly in the job brief, reported even when coverage or sign-type would otherwise drop them from
# the ordinary sweep (a key/ciphertext of a different sign type never enters `candidates`, so a genuine
# negative on, say, a digit key against a mixed-sign ciphertext would otherwise never get a row at all --
# rule 3 requires the numbers be reported, not just implied by absence).
KNOWN_PAIRS = [
    ('lodewijk-van-nassau-1573-74/key.tsv', 'jan-van-nassau-1572-75/ciphertext_5549_ps.tsv',
     "Lodewijk's 1574 table on Jan's 5549 postscript (J5S)"),
    ('jan-van-nassau-1572-75/key_5549.tsv', 'jan-van-nassau-1572-75/ciphertext_5549',
     "key_5549 (byte-for-byte copy of Lodewijk's table, NOTES.md s.?) on Jan's own 5549 letters"),
    ('clair1067-brienne-poland-1646/key_brienne_1647.tsv', 'fr5160-letellier-1653/ciphertext',
     'Brienne 1647 table, same file in both folders (clair1067 -> fr5160)'),
    ('clair1067-brienne-poland-1646/key_brienne_1651.tsv', 'fr5160-letellier-1653/ciphertext',
     'Brienne 1651 table, same file in both folders (clair1067 -> fr5160)'),
    ('fr5160-letellier-1653/key_brienne_1647.tsv', 'clair1067-brienne-poland-1646/ciphertext',
     'Brienne 1647 table, same file in both folders (fr5160 -> clair1067)'),
    ('fr5160-letellier-1653/key_brienne_1651.tsv', 'clair1067-brienne-poland-1646/ciphertext',
     'Brienne 1651 table, same file in both folders (fr5160 -> clair1067)'),
]
NEGATIVE_PAIRS = [
    ('rah-canada-1869/key', 'rah-morillo-1817/ciphertext', 'RAH 1869 (Canada) key vs the RAH Morillo 1817 texts'),
    ('rah-morillo-1817/key', 'rah-canada-1869/ciphertext', 'reverse: RAH Morillo 1817 key vs the 1869 Canada text'),
    ('willem-van-hessen-1567/siblings/key_174_nomenclator.tsv', 'jan-van-nassau-1572-75/ciphertext',
     'Willem-van-Hessen 1567 nomenclator vs the 1572-75 Nassau letters'),
    ('jan-van-nassau-1572-75/key_1572.tsv', 'willem-van-hessen-1567/siblings/ciphertext_1069.tsv',
     'Nassau 1572 key vs Willem-van-Hessen 1069 (reverse of the pair the job brief names)'),
    ('la-garde-1577/key', 'fr3985-nevers-revol-1593/ciphertext', 'la-garde 1577 key(s) vs a Nevers (fr3985) ciphertext'),
    ('fr3985-nevers-revol-1593/key', 'la-garde-1577/ciphertext', 'reverse: fr3985 Nevers key vs la-garde 1577'),
    ('jan-van-nassau-1572-75/key_1572.tsv', 'rah-canada-1869/ciphertext', '1570s Nassau key vs 1869 RAH text (century gap)'),
    ('jan-van-nassau-1572-75/key_1572.tsv', 'huntington-luzerne-destouches-1781/ciphertext',
     '1570s Nassau key vs 1781 Huntington text (century gap)'),
]


def force_pairs(pairs_list, key_metas, ct_metas, corpora_map, rows, mark_known):
    """Scores every (key, ciphertext) combination named by a folder/path substring pair, adding a row to
    `rows` (tagged known_pair) for any combination the ordinary sweep did not already score (different sign
    types, or dropped by the compatibility filter). Returns a short results list for the report."""
    results = []
    for key_sub, ct_sub, label in pairs_list:
        keys = [(p, key, meta) for p, key, meta in key_metas if key_sub in str(p.relative_to(ROOT)).replace(os.sep, '/')]
        cts = [c for c in ct_metas if ct_sub in c['path']]
        if not keys:
            results.append(dict(label=label, key=key_sub, ct=ct_sub, note='key not found on disk')); continue
        if not cts:
            results.append(dict(label=label, key=key_sub, ct=ct_sub, note='ciphertext not found on disk')); continue
        for p, key, meta in keys:
            kp = str(p.relative_to(ROOT))
            for c in cts:
                existing = next((r for r in rows if r['key_path'] == kp and r['ciphertext_path'] == c['path']), None)
                if existing:
                    if mark_known:
                        existing['known_pair'] = 'yes'
                    results.append(dict(label=label, key=kp, ct=c['path'], coverage=existing['coverage'],
                                         z_shuffled=existing['z_shuffled'], verdict=existing['verdict']))
                    continue
                res = score_one_pair(key, meta, c, corpora_map)
                row = dict(ciphertext_path=c['path'], ct_status=c['status'], key_path=kp,
                           key_office=meta['office'], key_years=meta['years'], key_lang=meta['lang'],
                           design=meta['design'], coverage=res['coverage'], score=res['score'],
                           z_shuffled=res['z_shuffled'], z_valuefreq=res['z_valuefreq'], stat=res['stat'],
                           n_tokens=res['n_tokens'], pass_real=res.get('pass_real', ''),
                           pass_null=res.get('pass_null', ''), dictword_share=res.get('dictword_share', ''),
                           rank_of_this_key_for_ct='', known_pair=('yes' if mark_known else 'no'),
                           verdict=res['verdict'], gate_verdict=res['verdict'], _real=res['_real'],
                           _z_sh=res['_z_sh'], _stat=res['_stat'])
                rows.append(row)
                results.append(dict(label=label, key=kp, ct=c['path'], coverage=row['coverage'],
                                     z_shuffled=row['z_shuffled'], verdict=row['verdict']))
    return results


# ==================================================================== main sweep

def run(alarm=None, since_paths=None, gate=None, force=True):
    """Full sweep; with since_paths (repo-relative paths changed since a git ref) only pairs whose key or
    ciphertext is in that set are scored, and the forced known/negative pairs are skipped (nightly mode)."""
    gate = gate or load_gate()
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

    # own-ciphertext(s) for each key: decode.json job list when it exists (authoritative), else same-folder
    # when unambiguous, else a digit/header-name match with process-of-elimination for the one leftover key
    # (fix A's own_cts redesign -- see compute_own_cts's docstring above)
    decode_jobs_by_folder = {}
    for folder in {meta['folder'] for _, _, meta in key_metas} | {c['folder'] for c in ct_metas}:
        jobs = load_decode_jobs(folder)
        if jobs:
            decode_jobs_by_folder[folder] = jobs
    compute_own_cts(key_metas, ct_metas, decode_jobs_by_folder)

    rows = []           # KEY-CROSSMATCH.tsv rows
    pos_control = []    # positive-control table rows
    unusable = []

    for p, key, meta in key_metas:
        candidates = [c for c in ct_metas if c['sign_type'] == meta['sign_type']]
        if since_paths is not None and meta['path'] not in since_paths:
            candidates = [c for c in candidates if c['path'] in since_paths]
        if not candidates:
            continue
        ranked_scores = []  # (real_score, ct_path) for own-text ranking
        for c in candidates:
            res = score_one_pair(key, meta, c, corpora_map, gate=gate)
            is_own = c['path'] in meta['own_cts']
            verdict = 'own' if is_own else res['verdict']
            rows.append(dict(ciphertext_path=c['path'], ct_status=c['status'], key_path=meta['path'],
                              key_office=meta['office'], key_years=meta['years'], key_lang=meta['lang'],
                              design=meta['design'], coverage=res['coverage'], score=res['score'],
                              z_shuffled=res['z_shuffled'], z_valuefreq=res['z_valuefreq'], stat=res['stat'],
                              n_tokens=res['n_tokens'], pass_real=res['pass_real'], pass_null=res['pass_null'],
                              dictword_share=res['dictword_share'], rank_of_this_key_for_ct='', known_pair='no',
                              verdict=verdict, gate_verdict=res['verdict'], _real=res['_real'], _z_sh=res['_z_sh'],
                              _stat=res['_stat']))
            if res['_stat'] is not None:
                ranked_scores.append((res['_stat'], c['path']))
        # positive control: does this key rank its own ciphertext(s) first among same-sign-type candidates,
        # own-quality (z_sh>=4, passes both calibrated controls) -- job brief §1
        if meta['own_cts']:
            ranked_scores.sort(key=lambda t: t[0], reverse=True)
            own_rank = next((i + 1 for i, (sc, path) in enumerate(ranked_scores) if path in meta['own_cts']), None)
            for i, (sc, path) in enumerate(ranked_scores):
                if path in meta['own_cts']:
                    for r in rows:
                        if r['key_path'] == meta['path'] and r['ciphertext_path'] == path:
                            r['rank_of_this_key_for_ct'] = i + 1
            own_row = next((r for r in rows if r['key_path'] == meta['path']
                             and r['ciphertext_path'] in meta['own_cts']), None)
            ok = bool(own_row and own_rank == 1 and own_row['gate_verdict'] == 'hit')
            pos_control.append(dict(key=meta['path'], own_text=', '.join(meta['own_cts']), own_rank=own_rank,
                                     z_sh=own_row['_z_sh'] if own_row else None, ok=ok, n_candidates=len(ranked_scores)))
            if not ok:
                reason = (f"own-text rank {own_rank} of {len(ranked_scores)}, cov={own_row['coverage']}"
                          if own_rank else "own text not scored (no corpus or coverage<0.5)")
                unusable.append((meta['path'], reason))
        else:
            pos_control.append(dict(key=meta['path'], own_text='(no co-located ciphertext found)', own_rank=None,
                                     z_sh=None, ok=None, n_candidates=len(candidates)))

    unusable_paths = {u[0] for u in unusable}
    for r in rows:
        if r['key_path'] in unusable_paths and r['verdict'] not in ('own',):
            r['verdict'] = 'unusable-key'

    if force and since_paths is None:
        known_pairs = force_pairs(KNOWN_PAIRS, key_metas, ct_metas, corpora_map, rows, mark_known=True)
        negative_pairs = force_pairs(NEGATIVE_PAIRS, key_metas, ct_metas, corpora_map, rows, mark_known=False)
    else:
        known_pairs, negative_pairs = [], []
    neg_scored = [r for r in negative_pairs if 'verdict' in r]
    neg_false_positives = [r for r in neg_scored if r['verdict'] in ('hit', 'short')]

    return dict(keys_found=keys_found, keys_dropped=keys_dropped, cts_found=cts_found, cts_dropped=cts_dropped,
                key_metas=key_metas, ct_metas=ct_metas, rows=rows, pos_control=pos_control, unusable=unusable,
                corpora_map=corpora_map, known_pairs=known_pairs, negative_pairs=negative_pairs,
                neg_scored=neg_scored, neg_false_positives=neg_false_positives)


def write_tsv(rows, path):
    cols = ['ciphertext_path', 'ct_status', 'key_path', 'key_office', 'key_years', 'key_lang', 'design',
            'coverage', 'n_tokens', 'score', 'z_shuffled', 'z_valuefreq', 'stat', 'pass_real', 'pass_null',
            'dictword_share',
            'rank_of_this_key_for_ct', 'known_pair', 'verdict']
    order = {'hit': 0, 'short': 1}
    def sortkey(r):
        z = r.get('stat')
        z = z if isinstance(z, (int, float)) else -999
        return (order.get(r['verdict'], 2), -z)
    rows = sorted(rows, key=sortkey)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')
    return rows


def changed_paths(ref, root=ROOT):
    """Repo-relative paths changed between git ref and HEAD (plus uncommitted changes), for --since."""
    import subprocess
    out = subprocess.run(['git', '-C', str(root), 'diff', '--name-only', ref], capture_output=True, text=True, check=True)
    return {l.strip() for l in out.stdout.splitlines() if l.strip()}


def ref_hours_ago(hours, root=ROOT, branch='origin/main'):
    """The last commit on branch at least `hours` old -- the nightly routine's --since ref."""
    import subprocess
    hours = int(math.ceil(hours))  # git's date parser reads '6 hours ago', not '6.0 hours ago'
    def find():
        out = subprocess.run(['git', '-C', str(root), 'rev-list', '-1', f'--before={hours} hours ago', branch],
                             capture_output=True, text=True, check=True)
        return out.stdout.strip() or None
    ref = find()
    if ref is None:
        # a cloud session's clone is shallow (50-60 commits, about 20 minutes of this repository's traffic on
        # 26 Sept 2026): deepen once to cover the window, then look again
        subprocess.run(['git', '-C', str(root), 'fetch', '-q', f'--shallow-since={hours + 2} hours ago', 'origin',
                        branch.split('/', 1)[-1]], capture_output=True, text=True)
        ref = find()
    return ref


def select_since(key_paths, ct_paths, changed):
    """(key, ciphertext) pairs a --since run scores: every pair where either side changed. Pure, for the test."""
    return [(k, c) for k in key_paths for c in ct_paths if k in changed or c in changed]


# Folders known to share one office's tables (a hit between them is a known relation, not a lead).
SIBLING_FOLDERS = [
    {'lodewijk-van-nassau-1573-74', 'jan-van-nassau-1572-75'},   # key_5549 is a copy of Lodewijk's 1574 table (J5S)
    {'clair1067-brienne-poland-1646', 'fr5160-letellier-1653'},   # Brienne's 1647/1651 tables in both folders
]


# Cross-folder hits already read by eye and settled (XMATCH-CAL, 26 Sept 2026, KEY-CROSSMATCH.md); the nightly
# run labels them 'adjudicated' and does not post them again.
ADJUDICATED = {
    ('ciphers/clair1108-duvergier/key_1696.tsv', 'ciphers/espagnol142-mercy-1648/ciphertext.tsv'):
        'design kin only: shares the generic a=10 b=12 c=14 d=16 e=18 f=20 run; Mercy is read by its own key',
    ('ciphers/clair1108-duvergier/key_1696.tsv', 'ciphers/bowes-walsingham-1583/ciphertext.txt'):
        'probable false positive: 1 shared code value, n=101 at the stratum floor, English text scored as French',
}


def relation(row):
    """'own' / 'known pair' / 'same folder' / 'sibling' / 'new lead' for a gated row."""
    if row.get('verdict') == 'own':
        return 'own'
    if row.get('known_pair') == 'yes':
        return 'known pair'
    if (row['key_path'], row['ciphertext_path']) in ADJUDICATED:
        return 'adjudicated'
    kf = Path(row['key_path']).parts[1] if row['key_path'].startswith('ciphers/') else folder_of(ROOT / row['key_path'])
    cf = Path(row['ciphertext_path']).parts[1]
    if kf == cf:
        return 'same folder'
    if any(kf in fam and cf in fam for fam in SIBLING_FOLDERS):
        return 'sibling'
    return 'new lead'


def room_line(row, gate):
    """ROOM.md signal text for one gated row (nightly mode posts one per hit/short, most first)."""
    return (f"for the parent: xmatch {row['gate_verdict']} ({relation(row)}): {row['key_path']} reads "
            f"{row['ciphertext_path']} stat={row['stat']} (gate {gate['stat_min']}, null p99 "
            f"{gate['null_stat_p99']}) cov={row['coverage']} n={row['n_tokens']} -- read by eye before any claim")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out-tsv', default=None, help='default KEY-CROSSMATCH.tsv for a full sweep, none for --since')
    ap.add_argument('--quiet', action='store_true')
    ap.add_argument('--calibrate', action='store_true',
                    help='fit the gate on VERIFIED_PAIRS, write KEY-CROSSMATCH-CAL.tsv and the gate file, stop')
    ap.add_argument('--since', metavar='REF', help='nightly mode: score only pairs whose key or ciphertext changed since REF')
    ap.add_argument('--since-hours', type=float, metavar='H',
                    help='nightly mode with REF = the last origin/main commit at least H hours old')
    ap.add_argument('--post-room', action='store_true',
                    help='post each non-own hit/short to ROOM.md via tools/room.py (nightly routine)')
    a = ap.parse_args(argv)
    if a.calibrate:
        gate, rows, skipped = calibrate()
        print(json.dumps(gate))
        for r in rows:
            print(f"  {r['tier']:8} {r['key_path']} <- {r['ciphertext_path']} n={r['n_tokens']} cov={r['coverage']} "
                  f"stat={r['stat']:.2f} adm={r['admitted']} nullpass={r['null_pass']} order_pass={r['order_pass']}")
        for sk in skipped:
            print('  skipped', *sk)
        return gate
    gate = load_gate()
    if gate is None:
        sys.exit('no gate file (tools/data/key_crossmatch_gate.json): run --calibrate first')
    since = None
    if a.since or a.since_hours:
        ref = a.since or ref_hours_ago(a.since_hours)
        if not ref:
            sys.exit('no commit old enough for --since-hours')
        since = changed_paths(ref)
        if not a.quiet:
            n_k = sum(1 for x in since if re.search(r'/key[^/]*\.(tsv|txt)$', x))
            n_c = sum(1 for x in since if re.search(r'/ciphertext[^/]*\.(tsv|txt)$', x))
            print(f'--since {ref}: {len(since)} changed paths, {n_k} key files, {n_c} ciphertext files')
    res = run(since_paths=since, gate=gate)
    out_tsv = a.out_tsv or (None if since is not None else str(ROOT / 'KEY-CROSSMATCH.tsv'))
    sorted_rows = write_tsv(res['rows'], out_tsv) if out_tsv else sorted(
        res['rows'], key=lambda r: -(r['_stat'] if r.get('_stat') is not None else -999))
    n_ok = sum(1 for pc in res['pos_control'] if pc['ok'])
    n_total = sum(1 for pc in res['pos_control'] if pc['ok'] is not None)
    gated = [r for r in sorted_rows if r.get('gate_verdict') in ('hit', 'short')]
    leads = [r for r in gated if relation(r) not in ('own', 'same folder')]
    if not a.quiet:
        print(f"gate: stat >= {gate['stat_min']} (n >= {gate['min_tokens']}, cov >= {gate['min_coverage']}); "
              f"own-text pairs ranked first and clearing it: {n_ok} of {n_total}; non-own rows clearing it: "
              f"{sum(1 for r in leads if r['gate_verdict'] == 'hit')} hit, "
              f"{sum(1 for r in leads if r['gate_verdict'] == 'short')} short")
        for r in leads:
            print('  ' + room_line(r, gate))
        if since is None:
            fp = res['neg_false_positives']
            print(f"negative pairs: {len(fp)} of {len(res['neg_scored'])} scored cleared the gate (false positives)")
    if a.post_room:
        import subprocess
        for r in [r for r in leads if relation(r) == 'new lead'][:5]:
            subprocess.run([sys.executable, str(TOOLS / 'room.py'), 'key_crossmatch nightly (tools/key_crossmatch.py)',
                            room_line(r, gate)], check=False)
    return res


if __name__ == '__main__':
    main()
