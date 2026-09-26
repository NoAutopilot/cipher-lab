LEADS REQUEST, label SO-UNTERSBERG-LEADS

We are an AI-assisted open cipher-research repository (github.com/NoAutopilot/cipher-lab; a person plus AI
agents). We are NOT asking you to verify a reading -- we want leads. Our own comparison work has stalled at
chance level against every witness we could find.

THE ITEM
- A six-line abbreviation-heavy inscription, "Die Propheceyung, so im Undtersperg zu Reichenhall geschehen ist,
  im 1523. Jahr" ("The prophecy that happened at/in the Untersberg near Reichenhall, in the year 1523"), a
  legendary/prophetic text about the Untersberg mountain (Salzburg region), surviving in at least a dozen
  manuscript witnesses.
- Primary source for our working copy: Salzburg Museum, BIB HS 2398 ("opening 11", fol.10v/11), a manuscript
  the museum itself dates 1690-1710 (scribe Lazarus Gitschner), 28 IIIF leaves online.
- Printed transcription of the same and eleven other witnesses: Wilhelm Herzog, "Die Untersbergsage nach den
  Handschriften" (1929), pp.27-50 (archive.org id `herzog_untersbergsage`, full view). Herzog transcribes
  diplomatically; he does not decipher or explain the abbreviations.
- Our files: full comparison/test log https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/untersberg-code/NOTES.md,
  our own blind transcription of opening 11 reconciled against a second pass
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/untersberg-code/reconciled.tsv.
- What we found: a control-backed signal that the text is genuine scribal (suspension) abbreviation, not a
  cipher of meaningless marks (period-after-short-token count 36 vs a synthetic-control mean of 12.0, 100th
  percentile). Our own blind reading against Herzog's diplomatic print agrees on 76 of 110 characters (0.691).
  One recurring ligature in our transcription, which we call "symA" (5 occurrences, lines 2/4/6), does not
  match any standard Cappelli-style Latin abbreviation shape (checked against qu/que/-rum/-us/-orum/con) and
  does not recur with the same value across any two of Herzog's eight other witnesses at better than chance
  (a 200-draw random-position control gives a mean of 1.07/5 matches; symA got 0-1/5).

WHAT WE HAVE ALREADY CHECKED (do not just repeat these)
- All 12 witnesses in Herzog 1929 pp.27-50, both pairwise (our leaf vs one other) and jointly (our leaf vs
  four others at once): neither beats a random-shuffle control (pairwise 3/6 vs shuffle mean 2.10; joint
  11/52 vs shuffle mean 10.87) -- the witnesses agree with each other only at chance level on the specific
  points we tested, so witness collation alone will not resolve this.
- A suspension-abbreviation expander trained on Early New High German only (no Latin abbreviation model wired
  in yet): weak, reads mostly from letter-unigram frequency rather than real abbreviation shapes.

WHAT WOULD ACTUALLY HELP (leads, not a verdict)
1. A real, period-appropriate Latin/German abbreviation reference (Cappelli's own "Lexicon abbreviaturarum"
   or an equivalent German-manuscript-specific abbreviation dictionary) that might identify symA directly,
   beyond the handful of common Latin forms we already ruled out.
2. Has anyone published a full modern edition, translation, or scholarly discussion of the Untersberg prophecy
   text (folklore studies, Alpine-legend studies, a Salzburg regional-history journal) that quotes this exact
   line or discusses its abbreviations, beyond Herzog 1929?
3. Any other manuscript witness of this text not in Herzog's 12 (a library catalogue, a folklore archive) that
   might preserve the same passage more legibly.
4. A scholar of German paleography or Alpine legend/prophecy literature who has written on this specific text
   or its manuscript tradition.
5. Given that witness collation reads at chance and our abbreviation expander is weak, what would you try
   first to identify symA or settle line 6 ("lo[symA]mi vmult" vs our first pass's "loqui vult")?

HOW TO REPORT
- Write your answer as one Markdown file at `ciphers/untersberg-code/second-opinions/chatgpt-leads-2026-09-26.md`
  in github.com/NoAutopilot/cipher-lab. Do not touch any other file. Create branch
  `second-opinion/SO-UNTERSBERG-LEADS` and open a pull request titled exactly
  `[SO-UNTERSBERG-LEADS] leads: Untersberg prophecy text abbreviation, Salzburg Museum HS 2398`.
- Header: `label: SO-UNTERSBERG-LEADS`, `model: <your model name and version>`, `date: <UTC date>`,
  `prompt: PROMPT-chatgpt-leads.md in this folder`, then leads under headings matching items 1-5 above.
- Every citation needs author, title, year, page, and a URL, or mark it "unverified". Never invent a page
  number.
- We are not asking for a verdict on novelty -- only a separate verifier on our side makes that call. Leads
  only.
