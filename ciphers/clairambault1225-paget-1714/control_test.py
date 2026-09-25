#!/usr/bin/env python3
"""Matched control for clairambault1225-paget-1714 cryptanalysis attempt 1.

Builds a synthetic French nomenclator cipher of the SAME shape as the target
(same token/code counts, same glossed-span shapes) but with a TRUE, self-
consistent fixed bigram-per-code table (built by construction), then runs the
identical crib-extraction + cross-validation procedure used on the real
target, to see whether that procedure extends beyond the directly-glossed
codes on a well-behaved control of the same design.
"""
import random, re, sys

random.seed(20260925)

# --- period-style French filler text (18th c. diplomatic register, written for this control,
#     not sourced -- a synthetic passage, per rule 3, matched in register/length only). ---
FILLER = """
Monseigneur j'ay receu la lettre qu'il a plu a Vostre Excellence de m'escrire le
dernier jour du mois passe je luy en rends tres humbles graces il m'escrit
encore de la ville qu'il y sera jusqu'a la fin du mois prochain et qu'il me
prie de luy marquer si j'ay receu quelque avis touchant les affaires dont il
m'a parle mais une mort subite l'a surpris en n'ayant donne ordre a sa
succession de maniere que ceux qui verront les eclaircissements necessres
connoistront que tant qu'on ne les donnera pas il ne sera pas possible d'en
venir au fait j'ay remarque qu'ils concourent tous avec empressement a
traiter cette affaire et comme je luy avois deja fait sceu les conferences
qu'on a eu sur ce sujet on verra bientost quelques personnes venir icy pour
en trouver l'issue les nouvelles de la cour sont que le prince party depuis
le vingt du mois a este receu avec de grands honneurs et que la paix generale
sera signee avant la fin de l'annee je suis avec tres profond respect
Monseigneur de vostre excellence le tres humble et tres obeissant serviteur
""".lower()
FILLER = re.sub(r"[^a-z' \n]", "", FILLER)
WORDS = [w for w in FILLER.replace("\n", " ").split(" ") if w]

def bigram_split(word):
    """Split a word into 2-letter chunks, a trailing single letter if odd length."""
    letters = [c for c in word if c.isalpha()]
    chunks = []
    i = 0
    while i < len(letters):
        if len(letters) - i == 1:
            chunks.append(letters[i]); i += 1
        else:
            chunks.append(letters[i] + letters[i+1]); i += 2
    return chunks

# Two synthetic proper names, matched in letter-count/shape to the real target's
# two confirmed glosses: an 8-letter name (like "Lomeliny", -> 4 clean bigrams)
# and a 5-letter word with an elided apostrophe (like "l'abbe" -> 5 letters -> 3 codes).
NAME_A = "castelan"     # 8 letters, like Lomeliny
NAME_B = "londe"        # 5 letters (as if "l'onde"), like l'abbe

chunks_a = bigram_split(NAME_A)   # 4 chunks
chunks_b = bigram_split(NAME_B)   # 3 chunks (2,2,1)

# Build the FULL code table: every distinct bigram/letter chunk that appears anywhere
# in a long "obscured" run of the filler text gets ONE persistent random code (true,
# self-consistent key, by construction) so codes legitimately recur across the control
# the way they do in the real ciphertext.
all_chunks = []
for w in WORDS:
    all_chunks.extend(bigram_split(w))
all_chunks.extend(chunks_a)
all_chunks.extend(chunks_b)

distinct_chunks = sorted(set(all_chunks))
codes_pool = random.sample(range(2, 693), len(distinct_chunks))
chunk_to_code = dict(zip(distinct_chunks, codes_pool))
code_to_chunk = {v: k for k, v in chunk_to_code.items()}

# Trim the filler's own encoded stream down so total coded tokens ~500 and distinct
# codes ~122, matching the real target's counts (500 tokens, 122 distinct codes).
target_tokens, target_codes = 500, 122
stream = []
for w in WORDS:
    stream.extend(bigram_split(w))
# repeat/cycle the filler stream to reach ~500 tokens like the real letter 2's density
while len(stream) < target_tokens - len(chunks_a) - 2*len(chunks_b):
    stream.extend(stream[:80])
stream = stream[: target_tokens - len(chunks_a) - 2*len(chunks_b)]

# cap distinct codes at ~122 by re-using the most frequent chunks for anything beyond
from collections import Counter
freq = Counter(stream)
keep_chunks = set(c for c, _ in freq.most_common(target_codes - len(set(chunks_a+chunks_b))))
keep_chunks |= set(chunks_a) | set(chunks_b)
def fold(c):
    if c in keep_chunks:
        return c
    kc = sorted(keep_chunks)
    idx = sum(ord(ch) for ch in c) % len(kc)
    return kc[idx]
stream = [fold(c) for c in stream]

# insert NAME_B (like "l'abbe") 3 TIMES (like the real target's 3 repeats of 145.31.67),
# and NAME_A once, right after one of NAME_B's repeats (mirrors "l'abbe Lomeliny").
full_stream = chunks_b + chunks_a + stream[: len(stream)//2] + chunks_b + stream[len(stream)//2:] + chunks_b

codes_seq = [chunk_to_code[c] for c in full_stream]
distinct_codes_used = sorted(set(codes_seq))

print(f"control: total coded tokens = {len(codes_seq)}, distinct codes = {len(distinct_codes_used)}")

# --- The GLOSSES revealed to the solver (same as the real brief: only these 2 groups
#     are given as cribs; the solver does not otherwise know code_to_chunk). ---
gloss_b_codes = [chunk_to_code[c] for c in chunks_b]           # like 145.31.67
gloss_ab_codes = gloss_b_codes + [chunk_to_code[c] for c in chunks_a]  # like 145.31.67.148.186.147.176
print("gloss B codes (like l'abbe):", gloss_b_codes, "->", chunks_b)
print("gloss A+B codes (like l'abbe NAME):", gloss_ab_codes)

# --- Step 1 of the real procedure: derive per-code bigram values from the CLEAN
#     divisions the glosses give (bigram_split of the known gloss word, in order). ---
derived = {}
for code, chunk in zip([chunk_to_code[c] for c in chunks_a], chunks_a):
    derived[code] = chunk
for code, chunk in zip([chunk_to_code[c] for c in chunks_b], chunks_b):
    derived[code] = chunk
print("derived per-code values from glosses:", derived)

# --- Step 2: cross-validate -- does any derived code recur ELSEWHERE in the control's
#     other coded spans, and if so, is the SAME value consistent every time it recurs
#     (the exact check that failed on the real target for code 147)? ---
contradictions = 0
confirmations = 0
recovered_extra = set()
for i, code in enumerate(codes_seq):
    if code in derived:
        true_chunk = full_stream[i]
        if true_chunk == derived[code]:
            confirmations += 1
        else:
            contradictions += 1
        if i not in range(0, 0):  # placeholder, no-op
            pass
        recovered_extra.add(code)

# token accuracy achievable this way: every token whose code is in `derived` is now
# correctly read (since the control's key is self-consistent by construction).
correctly_read_tokens = sum(1 for c in codes_seq if c in derived)
print(f"control: cross-check confirmations={confirmations} contradictions={contradictions}")
print(f"control: codes carrying a derived value = {len(derived)} of {len(distinct_codes_used)} distinct codes used "
      f"({100*len(derived)/len(distinct_codes_used):.1f}%)")
print(f"control: tokens correctly readable via these derived codes = {correctly_read_tokens} of {len(codes_seq)} "
      f"({100*correctly_read_tokens/len(codes_seq):.1f}%)")
