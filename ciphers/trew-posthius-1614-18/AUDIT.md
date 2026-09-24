# AUDIT: Erasmus Posthius to Johann Christoph Eysenmenger, 13 March 1614 and 4 February 1618 (UB Erlangen, Trew Briefsammlung)

Verifier V1 for LANE V4, session_01MLbjBCJpkGuFngnSejoCec (Opus), 24 Sept 2026, 15:52-16:15 UTC by `date -u`.
Adversarial audit under CLAUDE.md rule 10. No decoding; no reading, key or ciphertext changed.

Claim under audit (NOTES.md "Reading (24 Sept 2026, LANE R4 F)"; status.json results row): both cipher passages read
with the 12-pair reciprocal tables written on the leaves, 109 tokens H 96 M 13; 1614 German "ich hab nit gewist das ihr
mein nachtbar wolt werden bei der dihlin ..."; 1618 "der heis ist ein feiner man der abraham kein gelt". Novelty not
claimed by the solver.

## 1. Verdict

| item | class | prior plaintext | prior decipherment of this item | evidence | confidence |
|---|---|---|---|---|---|
| 1618, address-side specimen (Trew, E. Posthius Nr. 8; bavarikon BAV80016370) | **N0** | **yes, published online:** Ärztebriefe record 00001955 (Tilmann Walter) prints the key rows and all eight specimen lines, clear and cipher lines together ("der heid ist ein / sub yuzd zdb uzn / feiner man / wuzmup nqm / der abraham / sup qtpqygn / keim gelt / cuzm xuob.") | **yes:** the leaf pairs each cipher line with its clear line; the database transcribes the pairing | strong: record read 24 Sept 2026 | high |
| 1614, four cipher lines below the letter (Trew, E. Posthius Nr. 2, recto; bavarikon BAV80016364) | **N0** | **yes, in manuscript:** an interlinear decipherment in a small hand above the cipher lines on the leaf itself (legible at native resolution: "ich" over "AWs", "ihr" over "asb", "nach" over "Uiw", "tbar" over "ſorib", "wol[t]" over "ctko"; lines 3-4 faint), each gloss line crossed by a ruled stroke. Not in print: the Ärztebriefe record 00001880 describes the four cipher lines and the key but gives no plaintext | **yes, on the leaf:** the gloss is the decipherment of this very block, word over word | moderate-strong: gloss legible on lines 1-2 and agrees with the solver's reading there; lines 3-4 not read (crop `images/crops/1614_interlinear_gloss.jpg`) | medium-high |

**Safe sentence, 1618 (N0).** "The 1618 specimen on the address side of Posthius's letter of 4 Feb 1618 to Eysenmenger
(UB Erlangen, Trew, E. Posthius Nr. 8) pairs each cipher line with its clear text on the leaf, and the Ärztebriefe
database (www.aerztebriefe.de/id/00001955, Tilmann Walter) already transcribes key, cipher and clear lines. Our key table
regenerates the cipher lines from the leaf's key."

**Unsafe sentence, 1618.** "We read the 1618 cipher" / "the 1618 specimen, unread until now" / any use of "first".

**Safe sentence, 1614 (N0).** "The four German cipher lines below Posthius's letter of 13 March 1614 (Trew, E. Posthius
Nr. 2) carry a contemporary interlinear decipherment on the leaf itself, and the key is written beside them. Our
reading applies the leaf key and agrees with the legible parts of that gloss. The Ärztebriefe record
(www.aerztebriefe.de/id/00001880) describes the cipher and key but prints no plaintext. We found none in print."

**Unsafe sentence, 1614.** "First decipherment of Posthius's 1614 cipher" / "previously unread" / "we broke it".

**Did we first-decipher? No, for either item.** 1618's plaintext stands on the leaf in clear lines and in a public
database record. 1614 was deciphered on the leaf when it was glossed. What this project adds is a reproducible,
token-graded application of the leaf keys (`decode_key.py --check` 0). The 1614 German reading is typed out in full here,
which neither the gloss (partly faint, struck) nor the database gives. This is a documentation contribution, not a
decipherment.

## 2. Why N0 for 1614 without print

Precedent `ciphers/clair1067-brienne-poland-1646/AUDIT.md` s.2: an interlinear decipherment on the leaf is "plaintext and
decipherment of this very item already known", with no print needed (also fr5160-letellier-1653, rah-canada-1869,
thurloe-printed P3). Here the gloss is shorter and fainter than Brienne's, and each gloss line is crossed by a ruled
stroke. That may be a cancellation, or it may be the ruling the glossator wrote along. Either way the decipherment
stands on the leaf and a reader with the image can recover it. The Ärztebriefe regest adds context: Posthius reminds
Eysenmenger of their "pact" to write "inversis literis" so that the friend could make out a word or two but nobody else
could read it all. The key is therefore a pre-agreed system between the two, not a puzzle.
**Fallback if a later auditor rejects the gloss as a decipherment:** the plaintext was then not located anywhere
(section 4), and the class would be N3. It would not reach N4 until Schmidt-Herrling 1940 p.474 and the trew-letters.com
transcription (if any) are read.

## 3. Items as audited

| | 1614 | 1618 |
|---|---|---|
| Date | 13 March 1614 (chronogram "Anno ratIo & eXperientIa MeDICo bona") | 4 Feb 1618 (day from Posthius Nr. 9; torn on original) |
| Sender / recipient | Erasmus Posthius, Heidelberg → J. C. Eisenmenger d.Ä., Heilbronn | same |
| Shelfmark | Trew, E. Posthius Nr. 2 (H62/TREWBR POSTHIUS_ERASMUS[2) | Trew, E. Posthius Nr. 8 (H62/TREWBR POSTHIUS_ERASMUS[8) |
| Ärztebriefe | 00001880 (recto, Tilmann Walter); 00001881 (verso: Eisenmenger's 7-line draft reply) | 00001955 (Tilmann Walter) |
| Ciphertext | 4 lines, 69 tokens | 4 cipher lines in an alternating clear/cipher specimen, 40 tokens |
| Plaintext as read (solver) | "ich hab nit gewist das ihr mein nachtbar wolt werden bei der dihlin uiei gluck darzu" | "der heis ist ein feiner man der abraham kein gelt" |
| Where the plaintext already stands | interlinear gloss on the leaf | clear lines on the leaf; Ärztebriefe 00001955 |
| Solver's search | csBV six sources; IA fts 4 queries (NOTES.md) | same |

Note the database's readings differ in detail from ours ("heid"/"keim" for the clear lines, key rows "Conradbfgbj" and
"salutembedgf/bignopqrwxyz"). Those are transcription variants of the same leaf, not a different text.

## 4. Principal families searched (24 Sept 2026)

| family | status | what | result |
|---|---|---|---|
| Leaf images (holding archive's digitisation) | searched | `images/1614_p1_full_key.jpg` at native resolution, enhanced crop saved as `images/crops/1614_interlinear_gloss.jpg`; `1618_p2_key_crop2.jpg` | 1614 interlinear gloss found; 1618 clear lines pair the cipher lines |
| Ärztebriefe database (BAdW / Würzburg, Frühneuzeitliche Ärztebriefe 1500-1700), which regests the Trew letters | searched | advanced search "Person" = "Posthius, Erasmus" (49 hits); full records 00001880, 00001881, 00001955, 00003151-00003157; ID probes 3100-3180 | **1618 key and specimen transcribed in 00001955; 1614 cipher and key described in 00001880, no plaintext**; Schlagwort "Geheimschrift" on both |
| Schmidt-Herrling 1940 (Trew catalogue), p.474 | cited, not read | cited by every Ärztebriefe record as "Katalogeintrag"; the digitised copy is at urn:nbn:de:bvb:29-bv007329242-0, not fetched | a short catalogue entry; the bavarikon notes quoting it (csBV) print no cipher |
| trew-letters.com | not searched | JS/POST search; csBV's guessed GET 404'd | open |
| Karrer, *Johannes Posthius* (1993) | not read | cited by Ärztebriefe for the father's works list only (pp.549 f.) | the father's catalogue; Erasmus's 1614/1618 letters postdate the father |
| Wagner/Gannon (eds.), *Opus Magnum: Matthäus Merian d.Ä. und die Bebilderung der Alchemie* (Heidelberg 2024, doi 10.11588/arthistoricum.1311) | searched (IA `00-gesamtband`, full djvu text grepped) | Posthius, Eysenmenger, Geheimschrift, Chiffr | cites Posthius to Eisenmenger 21 April 1618 (Fig. 2, prices of *Atalanta fugiens*); no cipher |
| Internet Archive full text (be-api fts) | searched | "nachtbar wolt"; "Erasmus Posthius"; Posthius Eysenmenger; Eysenmenger Posthius Trew; "Eisenmenger" Posthius Heidelberg 1614; "dihlin"; Posthius Geheimschrift; Posthius Chiffre; Eysenmenger Geheimschrift; "Posthius" "Eysenmenger" Brief (plus the solver's 4) | no plaintext; name co-occurrences only (matriculation lists, bibliographies, the Merian volume above) |
| Google Books API (key, country=US) | searched | "Erasmus Posthius" (300: Karrer, Heidelberg matriculation, etc.); "Posthius Eisenmenger" 0; "Trew Briefsammlung Geheimschrift" 0 | nothing on the cipher |
| CrossRef | searched | Erasmus Posthius; Posthius Eisenmenger; Trew Briefsammlung Geheimschrift | Posthius-father articles, Trew digitisation papers; nothing on these letters |
| OpenAlex | unreachable | same three queries; response had no `meta` (error body) | not retried |
| Semantic Scholar | unreachable | same three queries; no data returned (rate limit) | not retried |
| Persée / HAL | not searched | German Renaissance medical correspondence; low yield expected | open |
| HathiTrust bibliographic API | not searched | superseded by the Ärztebriefe find | open |
| DECODE, solver repositories, cipher blogs | searched by csBV, 24 Sept 2026 (NOTES.md s.4-5) | Posthius / Eysenmenger / Eisenmenger | zero hits; not rerun |
| JSTOR | queued | 2 rows in JSTOR-QUEUE.tsv | do not block the class |

## 5. Evidence

- Ärztebriefe 00001955 (Nr. 8), Bemerkungen: "Neben der Adresse Anleitung zu einer Geheimschrift: [Durchgestrichen:
  Conradbdf ..., darunter: klmpq[...]uwx] Conradbfgbj / klmpqstuwxyz / der heid ist ein / sub yuzd zdb uzn / feiner man /
  wuzmup nqm / der abraham / sup qtpqygn / keim gelt / cuzm xuob." Schlagwort: Geheimschrift. Licence CC BY-NC-ND 3.0 DE.
- Ärztebriefe 00001880 (Nr. 2 recto), Inhaltsangabe: "P. wolle E. an ihren 'Pakt' erinnern: P. habe [als Geheimschrift]
  verdrehte Buchstaben (inversis literis) geschrieben, damit P. [sic, E.] das eine oder andere Wort herausfinden, aber
  nicht jeder andere alles lesen könne ... [Es folgen vier Zeilen in Geheimschrift, links daneben zwei Zeilen:]
  'salutembedgf', [dazu zur Auflösung darunter:] 'bignopqrwxyz'." No plaintext given.
- Leaf, 1614: small-hand interlinear letters over each cipher line; legible "ich", "ihr", "nach", "tbar", "wol" sit over
  exactly the cipher groups that the solver's key turns into those words. "salutem" is written above line 1, the key's
  first row as a label.

## 6. Postmortem

**Failure:** the check-solved pass (csBV) and the solver both missed the Ärztebriefe database. It is the one project
that regests the Trew physicians' letters item by item, with Geheimschrift as a subject heading. The solver wrote "Not
searched: ... trew-letters.com transcriptions ... Schmidt-Herrling 1940 text". The check-solved verdict said "No key,
plaintext, or documented attempt for either letter located", and the 1618 plaintext and specimen were online the whole
time. The cue was in NOTES.md itself: Schmidt-Herrling was cited, and every Trew physician letter 1500-1700 is regested in
Ärztebriefe. **Lesson (proposed for `.claude/briefs/verifier.md` and check-solved):** for any Trew Briefsammlung item
(and any physician's letter 1500-1700 in German-speaking holdings), search www.aerztebriefe.de first. Use its advanced
search by Person; the POST form works with a cookie-jar script, and `/id/<8 digits>` gives a stable record. Also check
its Schlagwort "Geheimschrift". Second: the solver flagged the interlinear marks correctly, and that flag alone moved
1614 to N0.

**Corrections made in the folder:** NOTES.md status word `partial` → `found-solved`. Correction notes were added under
the check-solved verdict and the reading section. The status.json results row now carries the class and the safe
sentence.
