# Group H sources: what the Copiale decipherment actually did

Read by DEB-SWARM-H on 29 Sept 2026 (03:1x-03:3x UTC). Both papers were fetched from the ACL Anthology as PDF and read in full.

- **[K11]** K. Knight, B. Megyesi, C. Schaefer, "The Copiale Cipher", *Proc. 4th Workshop on Building and Using
  Comparable Corpora* (BUCC), ACL 2011, pp. 2-9. https://aclanthology.org/W11-1202.pdf
- **[K06]** K. Knight, A. Nair, N. Rathod, K. Yamada, "Unsupervised Analysis for Decipherment Problems",
  *Proc. COLING/ACL 2006 Poster Sessions*, pp. 499-506. https://aclanthology.org/P06-2065.pdf. This is the automatic
  attack that [K11] section 4 cites ("The attack method is given in [Knight et al, 2006]").

## Data used for the known-answer control (public, line level)

- Ciphertext: `learnable-typewriter/copiale` on Hugging Face, `annotation.json` (1,775 line images with labels in
  [K11]'s Figure 2 transcription names: `lam`, `bas`, `hd` and so on; 73,391 tokens). Copied to
  `data/copiale_cipher_lines_learnable-typewriter.json`. The dataset card gives no licence; it is used here only as a
  test input.
- Plaintext: `leitro/Decipher-from-Pixels-Copiale`, `copiale_gt/{train,valid,test}.gt` (GitHub, MIT licence, copied
  with its LICENSE as `data/LICENSE-leitro-gt`), the line-level German plaintext used in "Learning to Decipher from
  Pixels -- A Case Study of Copiale" (HistoCrypt 2026).
- The Uppsala project pages (stp.lingfil.uu.se / cl.lingfil.uu.se `~bea/copiale/`) and the Wayback Machine both
  reset the connection from this container on 29 Sept 2026 (proxy log: tunnel closed mid-exchange), one retry each;
  not used.
- Join (`prep_copiale.py`): line id `NN_k` in the cipher file is page `2NN-2`, line `k+1` in the plaintext file
  (`NNB_k` is page `2NN-1`). Checked by decoding: the gold labels (the [K11] Figure 6 key applied to the
  transcription, `copiale_key.py`) agree with the published plaintext at a mean letter similarity of **0.990 over
  1,701 lines** (1,696 at 0.9 or better, 1 below 0.7). The gold labels are what "recovered" is measured against.

## What [K11] did, step by step, in its own words

1. **Transcription.** About 90 cipher letters, including the 26 unaccented Roman letters a-z, dotted, underlined,
   circumflexed and fancy variants, and "an eclectic mix of symbols, including some Greek letters". Eight large
   symbols (9, @, #, %, 2, *, ±, ¬). "We transcribed a total of 16 pages (10,840 letters). We carried out our analysis
   on those pages, after stripping catchwords and down-casing all Roman letters."
2. **Frequencies and clustering.** Digraph and trigraph counts; "we automatically clustered the cipher letters based
   on their contexts": for each letter, a vector of counts of the letters that precede it, concatenated with one of the
   letters that follow it; "two letters a and b [are] similar if the cosine distance between v(a) and v(b) is small";
   bottom-up (agglomerative) clustering with SciPy (their Figure 4). Result: circumflexed letters behave alike, "the
   unaccented Roman letters form a natural grouping, as do underlined letters".
3. **First approach, failed.** Theory: Roman letters carry the message and every other symbol is a null. Simple
   substitution attacks on the Roman-letter sequence, "first assuming German source, then English, then Latin, then
   forty other candidate European and non-European languages", by the [K06] method, "which automatically combines
   plaintext-language identification with decipherment". "No language identified itself as a more likely plaintext
   candidate than the others."
4. **Homophonic attack, failed.** "We then gave up our theory regarding NULLs and posited a homophonic cipher." They
   first "confirmed that our computer attack does in fact work on a synthetic homophonic cipher" (it identified the
   language and gave "a reasonable, if imperfect, decipherment"). On the Copiale: "all resulting decipherments were
   nonsense, though there was a very slight numerical preference for German".
5. **Second approach, succeeded, by hand.** German chosen for three reasons: the book is in Germany, the slight
   numerical preference, and "Philipp 1866" spelled with double p. Then a hand attack: German "C is almost always
   followed by H" and cipher `?` is almost always followed by `-`, so `?`=C, `-`=H; the most frequent cipher trigraph
   `?-^` against German CHT gave `^`=T, "and this led to a cascade of others. We retracted any hypothesis that resulted
   in poor German digraphs and trigraphs". The cluster map extended each finding to its neighbours ("once we
   established a substitution like y=I, we could immediately add Y=I and !=I"); all circumflexed letters went to E.
6. **Spaces found from the partial reading.** Reading "CEREMONIE?DER?AUFNAHME", "it became clear that the unaccented
   Roman letters serve as spaces in the cipher ... The non-Roman letters are not NULLs -- they carry virtually all the
   information." Paragraph-initial capitals are Roman letters too, "which look nice, but are meaningless".
7. **Special symbols.** Colon `:` doubles the previous consonant (found by trying A-Z in the untranslatable
   ABSCHNIT?); `T` = SCH (found from GESELLSCHAFT in a dictionary), which "opened the door for other multi-plaintext-letter
   substitutions" (7 = ST, / = CH, G = EN/EM).
8. **Native correction.** "We brought full native-German expertise to bear", correcting hypothesised
   decipherments line by line.
9. **Logograms.** The eight large symbols "appear to be logograms, standing for the names of (doubly secret) people
   and organizations" ("the 9 asks him whether he desires to be 2"). The book describes the initiation of "DER
   CANDIDAT" into a secret society.

## What [K06] adds (the automatic part)

- EM: "we first use expectation-maximization (EM) (Dempster, Laird, and Rubin, 1977) to set all free parameters to
  maximize P(c) ... We then use the Viterbi algorithm to choose the p maximizing P(p) P(c|p)"; random restarts, the
  run with the best P(c) kept; a trigram source model with the channel probabilities cubed during decoding.
- The 80 languages: section 7, "Brute-Force Phonetic Decipherment": "We built 80 different source models from
  sequences we downloaded from the UN Universal Declaration of Human Rights website"; decipher against all 80 and
  order the results by post-training P(c). This is the "comparison with 80 languages".

## Wikipedia's summary checked against the papers

| Wikipedia says | Papers say | Verdict |
|---|---|---|
| homophonic cipher | [K11] s.4-5, Fig. 6 | confirmed |
| seven symbols for e | Fig. 6 row E: five circumflexed vowels plus `)` and `Z` = 7 cipher letters | confirmed |
| unaccented Roman letters act as spaces | [K11] s.5 | confirmed |
| some symbols for whole words | the eight large symbols "appear to be logograms" for people and organisations | confirmed, with [K11]'s own hedge ("appear to be") |
| comparison with 80 languages pointed to German | [K11]: German, English, Latin and "forty other" languages, which gave "a very slight numerical preference for German" in the homophonic attack; the 80-model screen is [K06]'s, run there on Don Quixote | **partly**: the Copiale screen was about 43 languages and its preference was "very slight"; German was chosen on three grounds, two of them outside the screen |
| expectation-maximisation | EM is [K06]'s method, the one that **failed** on the Copiale; the reading came from the hand attack of s.5 | **misleading**: EM was tried and gave nonsense; the decipherment was manual |

## What this group automates (and how it differs)

The step that worked in [K11] was human: a German reader extending digraph guesses through the cluster map. Group H
replaces it with a simulated-annealing homophonic solve against a quadgram model *with word spaces* (`hsolve_h.c`),
in which a sign may also take the value "space" (so the solve finds the space class itself, the fact [K11] found
from "CEREMONIE?DER"), seeded from the context-vector clusters of step 2. Language choice follows [K06]: solve in each
language, rank by fit; here fit is the solve's per-character log-likelihood minus that of held-out real text of the
same language at the same length, minus the letter-curve divergence (without that term a degenerate "iiii" solve in
a Latin corpus full of Roman numerals ranked first). The multi-letter values (SCH, CH, ST, EN), the doubling colon and
the logograms are not modelled: a token is counted right when the solve gives the first letter of its gold value.
