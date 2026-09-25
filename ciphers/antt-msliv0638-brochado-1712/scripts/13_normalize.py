"""ZX-BRO (25 Sept 2026): the spelling-convention normalization RETRO-2026-09-25h proposal 2 named and
YX-BRO79 left open ("still open for whichever entry needs it") -- one shared function, applied to BOTH
sides of any diff between a decode and a period gloss, so a spelling-convention difference (not a
transcription or key error) never counts as a disagreement. CLAUDE.md rule 3's own lesson (PX-BRODEC):
normalize both sides to one convention before diffing, or the gate measures whichever side transcribes
more literally.

Scope, single-letter level (what 06_decode_agreement.py and 11_loo_control.py compare): accents already
folded upstream (ACCENT_MAP/ACCENTS in those two scripts) -- this module adds the letter-identity variants
period Portuguese orthography treats as the same sound/letter and this scribe visibly interchanges:
  u <-> v   (period 'v' written as 'u' and vice versa -- e.g. this document's own 'suspensão'/'suspensaõ')
  i <-> j   (period 'j' written as 'i')
  y -> i    (period 'y' standing in for 'i', e.g. Tomokiyo-documented Portuguese secretary hands)
folded to one canonical form each (v->u, j->i, y->i) so a homophone that differs only by this convention
agrees rather than mismatches.

Scope, word level (gloss text, before any letter-count/token-count alignment check): common period
abbreviations this appendix's own Deciffrada lines use, expanded to their full period spelling so a
coded span's token count is compared against the SAME letter count the scribe intended, not the
shorthand's letter count (the Carta 79 "pra"/"para" bug YX-BRO79 fixed by hand is the general case this
table targets for every OTHER entry, without re-doing each one by hand):
  q.        -> que
  q.mos     -> quaes  (attested this document, m0280 Carta 13: "q.mos" decodes/glosses as "quaes")
  hé        -> he     (kept as its own period spelling of "e"/"é" -- not expanded further, already one
                        case/accent-folded token, listed here only so callers see it was considered)
  S.d±      -> Senhor Dom   (CLAUDE.md's own PX-BRODEC lesson: "S.d±" for "Snr D.")
  V.        -> Vossa   (letter-closing abbreviation; this document glosses "V.Sa" as "a V.Sa" -- V. alone
                        is the closing flourish, expanded only when followed by 'Sa'/'Sà' in the source)
  N.Exª     -> Vossa Exª  (already spelled out in this document's own Carta 13 gloss; listed for
                        completeness, not currently re-applied since Carta 13 already carries it in full)

This module does NOT re-run 01_segment.py..04_build_key.py (that would re-derive _pairs.json itself,
touching every entry's alignment, not just the 5 named this job) -- it is applied only inside the
comparison functions (06/11), i.e. it can only turn an apparent mismatch into an agreement, never add or
remove an aligned pair. Per this job's brief: never tune the control, and a mis-paired entry (token-count
still not matching gloss-letter-count after expansion) stays excluded from both real and synthetic, not
hand-patched into _pairs.json.
"""

LETTER_FOLD = {'v': 'u', 'j': 'i', 'y': 'i'}

WORD_ABBREV = {
    'q.': 'que',
    'q.mos': 'quaes',
    'v.': 'vossa',
    's.d±': 'senhor dom',
}


def fold_letter(c: str) -> str:
    """Single-letter spelling-convention fold, applied AFTER the existing accent fold. Idempotent,
    case-insensitive input expected (callers already lowercase before calling this)."""
    return LETTER_FOLD.get(c, c)


def expand_word(w: str) -> str:
    """Word-level abbreviation expansion for gloss text, case-insensitive, applied before any
    letter-count comparison. Unknown words pass through unchanged."""
    key = w.lower()
    return WORD_ABBREV.get(key, w)


def normalize_letter(c: str, accent_fold_fn) -> str:
    """Compose the existing accent fold (passed in from the caller's own ACCENT_MAP/ACCENTS table, so
    this module does not duplicate or drift from it) with this module's u/v, i/j, y/i fold."""
    return fold_letter(accent_fold_fn(c))


if __name__ == '__main__':
    import sys
    tests = [('v', 'u'), ('j', 'i'), ('y', 'i'), ('a', 'a'), ('q.', 'que'), ('Q.', 'que'),
              ('q.mos', 'quaes'), ('bornex', 'bornex')]
    ok = True
    for inp, want in tests:
        got = fold_letter(inp) if len(inp) == 1 else expand_word(inp)
        status = 'ok' if got == want else 'FAIL'
        if got != want:
            ok = False
        print(f"{status}  {inp!r} -> {got!r} (want {want!r})")
    sys.exit(0 if ok else 1)
