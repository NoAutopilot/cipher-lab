import csv, json, re, unicodedata
from collections import defaultdict, Counter

"""PX-BROKEY2 fix (25 Sept 2026): the original anchor script located each PLAIN word by a raw
case-insensitive substring search in deciffrada_line, which (a) matched short words *inside* longer
ones ("tem" inside "intendem", "a" inside almost every word -- the actual cause of Carta 13 and Carta
15's total ANCHOR-FAIL, confirmed against the image: every plain word in the cipher line is genuinely
present in the plaintext, just not where a naive substring search finds it first) and (b) aborted the
*whole entry* on the first word it could not place, discarding every pair the entry could otherwise
have contributed. This version matches whole decif WORDS in order (never a substring inside another
word), tolerates the scribe's own abbreviations and period-spelling variants (hand-checked against the
image for the specific cases below), tolerates a plain chunk and a decif word landing on opposite sides
of a space (one glued word in the cipher line for two decif words, or vice versa), and degrades
gracefully: a plain word that still can't be placed is skipped, not fatal to the rest of the entry --
03_align_pairs.py then bounds each CODE run by the *nearest* resolved anchor on each side instead of
only its immediate neighbour.
"""

ACCENTS = str.maketrans('ãáàâéêíóôõúç', 'aaaaeeiooouc')

def core(word):
    w = word.strip('.,;:()').lower().translate(ACCENTS)
    return w

# Hand-checked equivalences (image, this pass): honorific abbreviation whose leading letter the scribe
# and the compiler wrote differently (Carta 58, m0282: cipher plain word "N.Exã", deciffrada "V.Exª" --
# both mean "Vossa Excelência"); "dous"/"dois" (Carta 73, m0286: cipher plain word "dous", deciffrada
# "dois" -- both valid period spellings of "two", not a misreading).
HONORIFIC_RE = re.compile(r'^[nv]ex[aã]?$')
DOUS_DOIS = {'dous': 'doi', 'dois': 'doi'}

def canon(word):
    c = core(word)
    if HONORIFIC_RE.match(c):
        return 'HONORIFIC'
    return DOUS_DOIS.get(c, c)

def words_with_spans(text):
    return [(m.group(0), m.start(), m.end()) for m in re.finditer(r'\S+', text)]

def word_match(a, b):
    """a, b: raw word strings (already stripped of the appendix's own trailing V./V.Sa/etc by the caller).
    Exact after canon(); or one canon() is an abbreviation-prefix of the other (>=1 char, the longer one's
    *own written form* ends in a period -- the scribe's own signal it is short for something)."""
    ca, cb = canon(a), canon(b)
    if ca == cb:
        return True
    a_dot, b_dot = a.rstrip(',;:()').endswith('.'), b.rstrip(',;:()').endswith('.')
    shorter, longer = (ca, cb) if len(ca) <= len(cb) else (cb, ca)
    shorter_is_a = len(ca) <= len(cb)
    shorter_dot = a_dot if shorter_is_a else b_dot
    longer_dot = b_dot if shorter_is_a else a_dot
    if shorter and longer.startswith(shorter) and (shorter_dot or longer_dot) and shorter != longer:
        return True
    return False


def find_next(plain_word, decif_words, idx):
    """Search decif_words[idx:] for a match, trying (in order): the single next word; the next word
    merged with the one after it (one cipher plain word split across two decif words, e.g. "aporta" ->
    "a porta"); an unbounded forward search for a match further on (a code run before this plain word
    can stand for many decif words -- Carta 61's "teríamos" is 7 words past the search start -- that is
    normal and exactly how a leading code run's span gets its correct end boundary, not a sign this word
    is wrong; a false match this way would need the SAME whole word to recur later for something else,
    which is much rarer than the old version's within-word substring collisions).
    Returns (new_idx_after_match, match_start, match_end) using the position of the WORD(S) ACTUALLY
    MATCHED, never idx itself -- attributing skipped-over decif text to this word's span instead of to
    the preceding code run was the bug that halved the pair count on the first version of this fix."""
    if idx < len(decif_words) and word_match(plain_word, decif_words[idx][0]):
        return idx + 1, decif_words[idx][1], decif_words[idx][2]
    if idx + 1 < len(decif_words):
        merged = decif_words[idx][0].rstrip('.,;:()') + decif_words[idx + 1][0]
        if word_match(plain_word, merged):
            return idx + 2, decif_words[idx][1], decif_words[idx + 1][2]
    for j in range(idx + 1, len(decif_words)):
        if word_match(plain_word, decif_words[j][0]):
            return j + 1, decif_words[j][1], decif_words[j][2]
    return None


def merge_runs(segs):
    out = []
    for typ, val in segs:
        if typ == 'CODE' and out and out[-1][0] == 'CODE':
            out[-1] = ('CODE', out[-1][1] + val)
        else:
            out.append((typ, val if typ == 'CODE' else val))
    return out


data = json.load(open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/scripts/_segments.json'))

TRAIL_RE = re.compile(r"\s*V\.(Sa|S[ªa]|mce|Ex[ªa]?)?\.?\s*$", re.IGNORECASE)

results = []
n_ok, n_partial, n_unresolved_words = 0, 0, 0
for key, segs, decif_raw in data:
    decif = TRAIL_RE.sub('', decif_raw)
    merged = merge_runs(segs)
    dwords = words_with_spans(decif)
    plains_idx = [i for i, (t, _) in enumerate(merged) if t == 'PLAIN']
    anchor_pos = {}
    widx = 0
    resolved, unresolved = 0, 0
    for i, (t, v) in enumerate(merged):
        if t != 'PLAIN':
            continue
        w = v.strip('.,;:')
        if not w:
            continue
        found = find_next(w, dwords, widx)
        if found is None:
            unresolved += 1
            n_unresolved_words += 1
            continue
        nxt, start, end = found
        anchor_pos[i] = (start, end)
        widx = nxt
        resolved += 1
    ok = unresolved == 0  # true both for a fully-resolved entry and for one with no PLAIN words at all
    if ok:
        n_ok += 1
    elif resolved > 0:
        n_partial += 1
    results.append((key, merged, decif, anchor_pos, ok))

json.dump([(list(k), [(t, v) for t, v in m], d, {str(kk): vv for kk, vv in a.items()}, ok) for k, m, d, a, ok in results],
          open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/scripts/_anchors.json', 'w'), ensure_ascii=False, indent=1)
for key, m, d, a, ok in results:
    n_plain = sum(1 for t, _ in m if t == 'PLAIN')
    n_anchored = len(a)
    status = 'OK' if ok else ('PARTIAL %d/%d' % (n_anchored, n_plain) if n_anchored else 'ANCHOR-FAIL')
    print(key, status)
print()
print(f"entries: {len(results)} full-OK={n_ok} partial={n_partial} zero-anchor={len(results)-n_ok-n_partial}, "
      f"unresolved plain words={n_unresolved_words}")
