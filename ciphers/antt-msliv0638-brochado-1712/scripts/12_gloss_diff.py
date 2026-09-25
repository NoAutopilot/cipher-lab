import csv, json, os, re

"""PX-BRODEC2 step 2: re-state the m0179-r1/m0180-r1 vs Carta 80/81 comparison as information, not a
gate (NOTES.md 'Why this job' -- PX-BRODEC's 80% letter-by-letter gate measured the period decipherer's
own abbreviation/paraphrase habit as much as the key). Classifies every disagreement as one of:
  key value          -- a genuine homophone: the code's key.tsv value is a global majority, this
                        occurrence's own true value is a minority the SAME code is also observed as
                        elsewhere in the appendix (key.tsv's 'all_observed_letters' column)
  transcription       -- the body's own transcription-pass disagreement (conf=M), an unresolved glyph
                        (ff?/+?), the 2 tokens (11, 55) PX-BROBODY found in the body image but missing
                        from the appendix's own stored cipher for Carta 80, or (Carta 81) the appendix's
                        own stored token count not matching its own gloss's letter count
  gloss abbrev/para   -- the Deciffrada line itself abbreviates or reads oddly (flagged elsewhere as
                        possibly corrupted for Carta 81's "the")
No threshold; this is a report, using POSITIONAL comparison (code[i] <-> gloss-letter[i], in order) rather
than a flat-string SequenceMatcher diff, because both Carta 80 and Carta 81's own appendix cipher_line is
a single unbroken CODE run with no interspersed plain words (confirmed: plaintext_appendix.tsv's
cipher_line for both entries is 100% digit/single-letter codes) -- so the correct correspondence is
positional, not a generic string alignment, which (tried first, see git history) misattributes multi-
character replace/delete blocks in a way that does not respect the known token structure.
"""

HERE = os.path.dirname(__file__)
ROOT = os.path.join(HERE, '..')

ACCENT_MAP = {'ã':'a','á':'a','à':'a','â':'a','é':'e','ê':'e','í':'i','ó':'o','ô':'o','õ':'o','ú':'u','ç':'c'}
def basefold(c):
    return ACCENT_MAP.get(c.lower(), c.lower())

def fold(s):
    return [basefold(c) for c in s if re.match(r'[A-Za-zÀ-ÿ]', c)]

key_rows = list(csv.DictReader(open(f'{ROOT}/key.tsv'), delimiter='\t'))
key_by_code = {r['code']: r for r in key_rows}

def strip_trailing(s):
    return re.sub(r'\s*V\.?(Sa|S[aª]|mce|Ex[aª]?)?\.?\s*$', '', s, flags=re.IGNORECASE)

def load_appendix(entry_label):
    for row in csv.DictReader(open(f'{ROOT}/plaintext_appendix.tsv'), delimiter='\t'):
        if row['entry_label'] == entry_label:
            return row
    return None

def load_appendix_tokens(entry_label):
    return [r for r in csv.DictReader(open(f'{ROOT}/ciphertext_appendix.tsv'), delimiter='\t')
            if r['entry_label'] == entry_label]

def load_body(run_id):
    return [r for r in csv.DictReader(open(f'{ROOT}/reading_body_tokens.tsv'), delimiter='\t')
            if r['line'] == run_id]

def classify_key(code, gloss_letter):
    row = key_by_code.get(code)
    if not row:
        return None
    obs = json.loads(row['all_observed_letters'])
    obs_folded = {basefold(k): v for k, v in obs.items()}
    if gloss_letter in obs_folded and gloss_letter != basefold(row['value']):
        return f"KEY VALUE (homophone minority): code {code}'s global majority is {row['value']!r} (grade {row['grade']}), but {gloss_letter!r} is an observed minority value for this same code elsewhere in the appendix ({obs})"
    return None

print("== m0179-r1 vs Carta 80 (positional: body's own extra tokens removed first) ==")
appx_row = load_appendix('Carta 80')
gloss_raw = appx_row['deciffrada_line']
gloss_letters = fold(strip_trailing(gloss_raw))
appx_tokens = [r['token'] for r in load_appendix_tokens('Carta 80')]
body_tokens = load_body('m0179-r1')
print(f"  raw Deciffrada gloss (abbreviations as written): {gloss_raw!r}")
print(f"  gloss folded to letters ({len(gloss_letters)}): {''.join(gloss_letters)}")
print(f"  appendix's own stored Carta 80 cipher tokens ({len(appx_tokens)}): {'.'.join(appx_tokens)}")
print(f"  body m0179-r1 tokens ({len(body_tokens)}): {'.'.join(r['sign'] for r in body_tokens)}")

EXTRA_POS = {14: '11', 15: '55'}  # 1-based body positions PX-BROBODY found extra vs the appendix's own copy
body_minus_extra = [r for r in body_tokens if int(r['pos']) not in EXTRA_POS]
print(f"  body tokens with the 2 known extra tokens (pos14=code11, pos15=code55) removed: "
      f"{len(body_minus_extra)} (appendix has {len(appx_tokens)})")
match = [r['sign'] for r in body_minus_extra] == appx_tokens[:13] + ['ff?'] + appx_tokens[14:]
print(f"  remaining body code sequence == appendix's own stored sequence except position14 (body 'ff?' vs appendix 'f'): {match}")
print()
print("  positional comparison, remaining body tokens vs gloss letters (both length 17 once ff?~f is treated as one glyph):")
n_key, n_transcription, n_agree = 0, 0, 0
for i, (r, letter) in enumerate(zip(body_minus_extra, gloss_letters), 1):
    code, val, conf = r['sign'], r['value'], r['conf']
    if val == letter or basefold(val) == letter:
        n_agree += 1
        continue
    if code == 'ff?' or val in ('', '?'):
        n_transcription += 1
        print(f"    pos{i}: body code={code} (unresolved glyph) vs gloss wants {letter!r} -> TRANSCRIPTION (unresolved ff?/f glyph, per PX-BROBODY the appendix's own copy has a single 'f' here)")
        continue
    if conf == 'M':
        n_transcription += 1
        print(f"    pos{i}: body code={code} value={val!r} (transcription-pass conf=M) vs gloss wants {letter!r} -> TRANSCRIPTION (the two blind passes disagreed on this glyph)")
        continue
    kc = classify_key(code, letter)
    if kc:
        n_key += 1
        print(f"    pos{i}: {kc} (gloss wants {letter!r})")
    else:
        print(f"    pos{i}: body code={code} value={val!r} vs gloss wants {letter!r} -> unexplained (not a documented homophone, not a transcription flag)")
print(f"  tally over the 17 positionally-compared tokens: {n_agree} agree, {n_key} KEY VALUE (homophone "
      f"minority), {n_transcription} TRANSCRIPTION (conf=M or the ff?/f glyph). Adding back the 2 extra "
      f"body tokens removed above (both TRANSCRIPTION/appendix-copy-gap): of the 19 raw body tokens, "
      f"{n_agree} agree outright, {n_key} are KEY VALUE homophones, {n_transcription + 2} are TRANSCRIPTION.")
print(f"  NOTE: this positional comparison does NOT match the 87% (15 compared/13 agree, 'm!=n; o!=e') that")
print(f"  conflicts.tsv reports for Carta 80's own internal check (06_decode_agreement.py). That script diffs")
print(f"  the two 17-letter sequences with difflib.SequenceMatcher instead of comparing them position-by-")
print(f"  position; verified directly (see NOTES.md write-up) that on this entry SequenceMatcher's LCS-style")
print(f"  alignment lets 3 of the 7 true positional mismatches slide onto a same-letter coincidence elsewhere")
print(f"  in the 17-letter string and get counted as 'equal', and drops 2 more from the denominator entirely")
print(f"  as an unindexed 'delete' -- inflating Carta 80's apparent self-consistency from a true 58.8% (10/17,")
print(f"  positional) to a reported 86.7% (13/15). Flagged as a measurement bug in 06_decode_agreement.py/")
print(f"  conflicts.tsv, not fixed this pass (out of this job's file scope) -- likely inflates the pipeline's")
print(f"  other same-length-sequence entries too, not just Carta 80.")
print()

print("== m0180-r1 vs Carta 81 ==")
appx_row81 = load_appendix('Carta 81')
gloss_raw81 = appx_row81['deciffrada_line']
gloss_letters81 = fold(strip_trailing(gloss_raw81))
appx_tokens81 = [r['token'] for r in load_appendix_tokens('Carta 81')]
body_tokens81 = load_body('m0180-r1')
print(f"  raw Deciffrada gloss (abbreviations as written, S.d and Communica both carry the manuscript's own '±' mark): {gloss_raw81!r}")
print(f"  gloss folded to letters ({len(gloss_letters81)}): {''.join(gloss_letters81)}")
print(f"  appendix's own stored Carta 81 cipher tokens ({len(appx_tokens81)}): {'.'.join(appx_tokens81)}")
print(f"  body m0180-r1 tokens ({len(body_tokens81)}): {'.'.join(r['sign'] for r in body_tokens81)}")
print()
print(f"  Carta 81 cannot be positionally checked against its OWN gloss the way Carta 80 was: the appendix's own")
print(f"  stored cipher has {len(appx_tokens81)} tokens but its own gloss folds to only {len(gloss_letters81)} letters")
print(f"  ({len(appx_tokens81)-len(gloss_letters81)} more tokens than letters) -- this is exactly why scripts/03_align_pairs.py")
print(f"  excluded this entry from _pairs.json ('0 resolved tokens', conflicts.tsv) and it contributed ZERO")
print(f"  observations to key.tsv: a TRANSCRIPTION-side count mismatch in the appendix's OWN copy, not a body issue.")
print(f"  The body run (m0180-r1, 22 tokens) also does not token-align cleanly against either the appendix's 23")
print(f"  tokens or its 19-letter gloss (PX-BROBODY: several body digit groupings, e.g. '85' at position4, could")
print(f"  be one token or two -- TRANSCRIPTION, unresolved digit-grouping ambiguity, not chased further here).")
print(f"  The gloss text itself is separately flagged (NOTES.md, PX-BROBODY) as likely corrupted: 'the' inside")
print(f"  nominally-Portuguese text ('Luis the Communica±') is not a Portuguese word -- GLOSS cause, compounding")
print(f"  the transcription-side count mismatch, neither of which is a key-value claim.")
print(f"  Conclusion for Carta 81: its low raw agreement (50.0%, PX-BRODEC) is explained by TRANSCRIPTION (the")
print(f"  appendix's own token/letter count mismatch, already excluding it from key.tsv entirely, plus the body's")
print(f"  own digit-grouping ambiguity) and GLOSS corruption -- there is no KEY VALUE evidence to classify here,")
print(f"  because this entry contributed no pairs to the key in the first place (it cannot be checked against")
print(f"  itself the way Carta 80 was).")
