#!/usr/bin/env python3
"""Normalised letter-word diff of pollaky-1865-1875 ads 3-4 against Bourdeau/Ernst's catokwacopa
transcription (github.com/dbourdeau/cyphersolver, catokwacopa/ads.py, AD1/AD2). Strips dashes,
digits and punctuation (which the two sources notate differently) and compares only the letter
tokens, per CLAUDE.md's lesson on PX-BRODEC (normalise transcription conventions before diffing,
or the gate measures notation, not correctness). Reproduces the numbers in NOTES.md's "Test 2"
section. python3 diff_bourdeau.py
"""
import re

# Bourdeau/Ernst BNA-checked transcription, copied 25 Sept 2026 from a shallow clone of
# github.com/dbourdeau/cyphersolver (catokwacopa/ads.py, MIT licence), deleted after copying.
AD1 = ("W. Str 53. Catokwacopa. Olcabrokorlested. Coomemega. Sesipyyocashostikr. Rep.– Itedconlec mistrl. "
       "Hrsclam 54. 3 caselcluchozamot. 1. 6. 9. Mopredisco. Contoladsemot. Iadfilisat. Qft. Cagap. "
       "Balmnopsemsov. Ap. 138.–Hodsam 55, 6. Iopotonrogfimsecharsenr. Tolshr. Itedjolec. mistrl.–Ding "
       "Declon.–Ereflodbr.")
AD2 = ("W. –Umem 18. Poayatlgerty. Dpeatcnrftin. Nvtinrdn. Dmlurpinrtrcamnr. Etd. – Atndngtnsurs. Otenpu.–"
       "Etfdorshpxn. 18. Ndtsfindseseo. Cotegr Tsvlysdinlge. Ngtndusdcndo. Edrstneirs. Ui. Ndted. "
       "Iolapstedttoc. A.P. 138.–Yxn. 18. 18. Wtubtrfftrstendinhofsvmnr. Dily.–Atdwtsurs. Oatvpu.–Y Arati. "
       "Rileohmae.–This will be intelligible if read in connection with my communication published in this "
       "column on the 8th inst.")

# ciphers/pollaky-1865-1875/ciphertext.txt, ad 3 and ad 4, after pass A/B reconciliation (25 Sept 2026).
OURS3 = ("W. Str 53. Catokwacopa. Olcabrokorlested. Coomemega. Sesipyyocashostikr. Rep.--Itedconlec mistrl. "
         "--Hrsclam 54. 3 caselcluchozamot. 1. 6. 9. Mopredisco. Contoladsemot. Iadfilisat. Qft. Cagap. "
         "Balmnopsemsov. Ap. 138.--Hodsam 55, 6. Iopotonrogfimsecharsenr. Tolshr. Itedjolec. mistrl.--Ding "
         "Declon.--Ereflodbr.")
OURS4 = ("W. --Umem 18. Poayatlgerty. Dpeatcnrftin. Nvtinrdn. Dmlurpinrtrcamnr. Etd. -- Atndngtnsurs. Otenpu.--"
         "Etfdorshpxn. 18. Ndtsfindseseo. Cotegr Tsvlysdinlge. Ngtndusdcndo. Edrstneirs. Ui. Ndted. "
         "Iolapstedttoc. A.P. 138.-- Yxn. 18. 18. Wtubtrfftrstendinhofsvmnr. Dily.--Atdwtsurs. Oatvpu.-- Y Arati. "
         "Rileohmae.--This will be intelligible if read in connection with my communication published in this "
         "column on the 8th inst.")


def letters_only_words(s):
    raw = re.split(r'[\s.,–—-]+', s)
    return [w.lower() for w in raw if w.isalpha()]


def diff(name, a, b):
    wa, wb = letters_only_words(a), letters_only_words(b)
    n = max(len(wa), len(wb))
    diffs = []
    for i in range(n):
        va = wa[i] if i < len(wa) else '<missing>'
        vb = wb[i] if i < len(wb) else '<missing>'
        if va != vb:
            diffs.append((i + 1, va, vb))
    print(f"{name}: {len(wa)} vs {len(wb)} letter-words, {len(diffs)} differences")
    for pos, va, vb in diffs:
        print(f"  word {pos}: ours={va!r} bourdeau={vb!r}")
    return diffs


if __name__ == '__main__':
    d1 = diff("ad3/AD1", OURS3, AD1)
    d2 = diff("ad4/AD2", OURS4, AD2)
    total_words = len(letters_only_words(OURS3)) + len(letters_only_words(OURS4))
    total_diffs = len(d1) + len(d2)
    print(f"TOTAL: {total_diffs} differences out of {total_words} letter-words "
          f"({100 * (total_words - total_diffs) / total_words:.1f}% agreement)")
