# AUDIT: Cardinal of Ferrara (Ippolito II d'Este) to the duc de Guise, "4. janvier 1556" o.s. (BnF Clairambault 349, f.3, Gallica canvas f9)

Verifier V7-CL349 (Opus, for LANE V7), 25 Sept 2026, from 22:22 UTC by `date -u`. Adversarial audit under CLAUDE.md
rule 10. No decoding; no key, ciphertext or reading file changed.

Claim under audit (LANE ZX orchestrator, ROOM.md 22:19 UTC 25 Sept 2026, and NOTES.md): the leaf is read from the
period key BnF fr.20974 no.15 (pp.57/69; images on Tomokiyo's guise.htm); a contemporary interlinear decipherment
agrees with the decode on 81.5% of glossed tokens; 1020 tokens H 29, C 260, M 611, I 98, U 22; fr16 judge FAIL; rule-7
re-derivation PASS; check-solved: "Ribier 1666 and Guise Memoires-journaux (Michaud-Poujoulat 1e s. t.6 pp.316-320)
read, letter not printed".

## 1. Verdict

| item | class | key | text | prior plaintext | prior decipherment of this item | confidence |
|---|---|---|---|---|---|---|
| Cipher body of f.3 (33 lines, 1020 tokens, "iay receu les lettres ..." to "... vouldroient [faire]") | **N0** | period | known | **yes, in print:** Guise, *Mémoires-journaux*, in Michaud and Poujoulat, *Nouvelle collection des mémoires*, 1e série t.6 (1839), pp.238-239 (IA `nouvellecollecti06michuoft`), the full letter in clear, dated "De Ferrare, ce 3e jour de janvier 1556" | **yes, twice:** (1) the interlinear decipherment written over all 33 cipher lines of the leaf itself; (2) the printed clear text, which follows the decoded text phrase for phrase | high |

Key: `period` -- rebuilt by this project (LANE YX/ZX) from the period key sheet BnF fr.20974 no.15, pp.57 and 69
(Gallica ark:/12148/btv1b9062131g). Tomokiyo (Cryptiana, guise.htm) identified the key and the letter and shows images
of the key sheet; an image of a period sheet is not a modern key, so the class stays `period`, with the identification
credited to Satoshi Tomokiyo. `text: known` (plaintext in print since 1839).

**Safe sentence.** "The ciphered part of the Cardinal of Ferrara's letter to Guise of 3/4 January 1557 (BnF
Clairambault 349, f.3) was already deciphered on the leaf by an interlinear hand and its text is printed in clear in
Guise's *Mémoires-journaux* (Michaud-Poujoulat 1e sér. t.6, pp.238-239) (N0). Applying the period key of BnF fr.20974
no.15, identified by Tomokiyo, regenerates that text (H 29, C 260, M 611, I 98, U 22 of 1020 tokens): a key-and-leaf
alignment, not a decipherment."

**Unsafe sentences.** "We deciphered / read the Este-Guise letter." "The letter is not printed." "First reading,
previously unread, unpublished." "Key recovered cryptanalytically."

**Did we first-decipher? No.** The leaf was deciphered when it was glossed, and the text was in print in 1839. What
this project added: a sign-level transcription of the leaf, a machine-readable table of key no.15 read from fr.20974,
and a reproducible key-to-ciphertext alignment (`tools/decode_key.py --check`). That is a contribution (a dataset and
a tested key application), and a check of the key sheet against a real ciphertext; it is not a novelty.

## 2. Task 1: how much of the leaf the interlinear decipherment covers

From the images on disk (`images/f9_thumb.jpg`, `images/lines_h/line33_s1.jpg` eye-checked; per-line counts from the
`gloss` column of `ciphertext.tsv`, which the transcription passes filled from the `lines_h` crops): every one of the
33 cipher lines carries interlinear letters over its codes, from line 01 (23 of 24 tokens with a gloss mark) to line
33 (15 of 28; the last line's crop shows glosses u, o, u, f over `10`, `4`, `4`, `104`). Overall 876 of 1118
transcribed positions (dividers included) carry a gloss mark; the gloss is letter-by-letter, not word-by-word, and
leaves some codes unglossed inside every line, but it does not stop part-way down the page. So no per-part split is
needed (unlike clair1067's second-hand areas): the whole cipher body is N0 by the precedent of
`ciphers/clair1067-brienne-poland-1646/AUDIT.md` s.2 (a manuscript interlinear decipherment of this very item on the
leaf is N0 without print) and fr5160-letellier-1653. The Dupuy 468 counter-precedent (first audit declined N0 for an
undescribed manuscript gloss) does not bite here, because the plaintext is also in print (section 3), which by itself
would give N1 and, together with the gloss, N0.

"Contemporary" is probable (16th-century letter forms, a gloss fluent enough to need the key) but not established,
and the hand is not identified; the class does not depend on it.

## 3. The print the check-solved sweep missed

`sources/ia-fulltext/print-check/nouvellecollecti06michuoft_djvu.txt.gz` (already on disk from an earlier print
check), lines 35590-35706: under the running head "Mémoires du duc de Guise [1556]", p.239 (the letter opens at the
foot of p.238): "Avant de s'acheminer en Italie, avec son armée, monsieur le duc de Guyse reçut diverses nouvelles du
dit pais, et entr'autres la lettre suivante de monseigneur le cardinal de Ferrare, dont suit la teneur: «Monsieur,
j'ay receu les lettres que vous a pleu m'escripre du vingt uniesme du mois passé, pour response à ce que Scipion vous
a dict de ma part sur le faict pour lequel il estoit venu par deçà, par lesquelles j'ay esté bien fort aise
d'entendre que les forces que vous menez soient telles que vous mandez ... la pratique du capitaine Livio Grosso ...
n'estant encores retourné ledict Livio que j'ay envoyé vers luy pour adviser et résouldre ensemble des moiens que
faudroit tenir pour l'exécuter ... J'ay envoyé gens en Allemagne, lesquelz ne m'ont encores rien faict entendre, qui
me faict penser que les choses n'y sont si eschauffées comme les ennemys vouldroient faire acroire ..." and it
continues in clear (Rome, the duc d'Albe, Gaeta) to "De Ferrare, ce 3e jour de janvier 1556."

Match against `reading.txt`: lines 01-33 of the decode follow this text in order, phrase by phrase ("iay receu les
lettre[s] [que vous] a ple u mescrire du uingt un iesme du passe [pour] respon[dre] de ce [que] scipion ... les forces
[que vous] mene[z] soient telles [que vous] mande[z] ... [pour] toutes autres ocasions ... la pratique du capitaine
liuio ... meilleure volonte ... ceste heure ... nestant encores retourne ... [Le Roy mre?] vers lui pour aduiser &
resouldre ensemble des moyens que faudra tenir pour ... executer ... iay enuoie en allemaigne ... me fait penser que
les choses ny sont ... comme les enemi[s] vouldroient [f]aire"). The cipher body therefore ends at "faire acroire";
the rest of the printed letter is presumably in clear on the leaf (not checked on f.3v/f.4, outside this audit).

Two differences, logged, not resolved: (a) date: the print says 3 January, the leaf's top-left date reads "4. janvier
1556" (NOTES.md). BnF Clairambault 348 f.304 is catalogued as "Lettre d'Hippolyte d'Este ... au duc de Guise (3
janvier 1557), avec chiffres" (Tomokiyo, guise.htm; BnF notice via sources/solver-diffs/2026-09-24-lane-g2-gallica5.tsv).
The print may rest on that 3 January copy, and Clair 349 f.3 may be a duplicate sent a day later by another route, or
the dates may simply be read differently. Either way the text of this item is in print. (b) The print does not say the
letter was ciphered; the Mémoires-journaux print it among Guise's received letters in clear. Where the decode's word
codes read "[Le Roy mre]" or "[gendarmerie]" and the print has other words, the print is the better witness for a
reader and a useful check on the M-graded word codes (section 5).

## 4. Search log (25 Sept 2026)

| family | what was searched | result |
|---|---|---|
| (a) canonical series | Ribier, *Lettres et mémoires d'estat* (1666), IA `bub_gb_bOnmNv2ZLVoC`, `bub_gb_qWTswSr32NYC` | print_check phrases (section 6); solver's own full read logged no letter |
| (b) recipient's papers | Guise, *Mémoires-journaux*, Michaud-Poujoulat 1e sér. t.6, IA `nouvellecollecti06michuoft`, local djvu grep for Scipion, Livio, "4 janvier 155[67]" | **hit: pp.238-239, the whole letter in clear** (section 3). The check-solved sweep read pp.316-320 and the four Italian letters of 12-20 Dec. 1556 and missed this one |
| (b) sender's side | Baguenault de Puchesse, "Négociations de Henri II avec le duc de Ferrare" (RQH 1868, IA `RevueDesQuestionsHistoriquesA3T5`) | print_check phrases; solver's full read logged no cipher |
| (c) documentary / scholarship | Romier, *Les origines politiques des guerres de religion* t.1-2 (1913-14), IA `lesoriginespolit01romi`, `lesoriginespolit02romi`, local djvu grep | Scipion Piovene, the cardinal's intendant, sent between Ferrara and Guise, discussed; Clair. 349 cited at fol.61 (another letter); no quotation of this letter found by grep for Livio / "janvier 1557" |
| (d) holding archive | BnF catalogue notice for Clair 349 as recorded in NOTES.md and sources/solver-diffs (Lettres orig. ... avec chiffres) | no decipherment mentioned in the notice |
| (e) full text | tools/print_check.py, 10 phrases (phrases.txt), IA ia-global, Google Books (keyed, country=US), OpenAlex, CrossRef, listed sources | see print-check.tsv / print-check-hosts.tsv (section 6) |
| (f) cipher projects | Tomokiyo guise.htm (sources/cryptiana/web/guise.htm): identifies key no.15 and this letter, shows the key sheet, gives no reading; Bourdeau cyphersolver and Aymeloglu unsolved-ciphers fresh `--depth 1` clones grepped for the ark `btv1b9000668z`, "Clairambault 349", "Clair 349": 0 hits (Bourdeau's "cardinal de Ferrare" hits are a Gallica sweep listing of another volume); DECODE catalogue diff: no record for Clair 349 | no reading anywhere |
| (g) scholarship indexes | OpenAlex (Bearer key) and CrossRef via print_check source rows; JSTOR: three rows appended to JSTOR-QUEUE.tsv (25 Sept 2026) | see section 6; JSTOR queued, not blocking (N0 rests on the leaf and the print) |

Unreachable / not done: page image of Michaud t.6 p.239 not viewed (djvu text only; the running heads place it);
Occhipinti and Pastor not searched (a class of N0 cannot move up on them); Calendar of State Papers Venetian/Foreign
1557 not searched, same reason.

## 5. Rule 4 / 7 checks

- `python3 tools/decode_key.py ciphers/clair349-este-guise-1556 --check` (run 25 Sept 2026, this audit):
  "tokens 1020: C 260, H 29, I 98, M 611, U 22 / reading up to date". Matches the claim.
- `python3 tools/judge_plaintext.py specs/clair349-este-guise-1556.json --file .../reading.txt` live: "FAIL language:
  score=-1.085, null_p99=-1.898, real_p05=-0.882, real_median=-0.786, mode=both, N=1185". Reproduces NOTES.md.
- Grades are sane and conservative: key-cell tokens H, gloss-agreeing tokens C, and any token whose image reading was
  M downgraded to M even where key and gloss agree (NOTES.md ZX-DEC349 step 2). No H is claimed for a gloss value.
- Now that the plaintext is in print, the printed text is known plaintext (grade C) for the whole cipher body. A
  future job may re-grade M tokens against it; this audit did not (no decoding).

## 6. print_check

See `print-check.tsv` and `print-check-hosts.tsv` (written by `tools/print_check.py`, 25 Sept 2026). Its "no hits"
rows are search results only; the decisive hit is the local djvu read in section 3, which print_check's fuzzy phrase
match is expected to find in `nouvellecollecti06michuoft` too.

## 7. Postmortem

Failure: the check-solved sweep (YX-CS349, 25 Sept) and the claim's "letter not printed" rested on a search of the
wrong pages of the right volume. The worker read t.6 pp.316-320 and the Italian letters of 12-20 Dec. 1556, and
searched "the surrounding 2,000 lines for 'janvier' near a Ferrare signature block"; the letter sits 8,000 lines
earlier, at pp.238-239, introduced as "la lettre suivante de monseigneur le cardinal de Ferrare", with OCR
"cardiual" and "15ôG" defeating both greps. A phrase search on the decoded text (not run before this audit) finds it at
once: "Scipion", "Livio", "forces que vous menez". Lesson (for the check-solved and solver templates): once a reading
exists, grep the sender-family edition for two or three distinctive decoded words, not only for the sender's name and
date, before writing "not printed".

Over-claims corrected in this folder: NOTES.md line 2 and the check-solved section (point 2b) said the 4 Jan. 1557
letter "is not printed" / "does not print the specific letter"; both now carry a correction pointing here. Files this
audit may not touch and the orchestrator should correct: the "Result so far" / board wording in status.json and
STATUS.md if they say "not printed" or call the result a reading rather than a key alignment of a known text; the
spec's check-solved text if it repeats the claim.
