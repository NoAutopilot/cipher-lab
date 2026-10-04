# DESENCLOS-PREMISE (account 3 worker) -- 4 Oct 2026 00:3x UTC (account-3 orchestrator)

Why: the BnF Département des Manuscrits (reply of 3-4 Oct 2026 to the owner's 1 Oct message on Espagnol 144 f.22, Mercy 1648)
pointed us to Dr Camille Desenclos (maître de conférences, Université de Picardie Jules Verne; Centre Jean-Mabillon associate;
https://www.chartes.psl.eu/annuaire/camille-desenclos, read 4 Oct 2026), whose research axis is "Naissance et essor de la
cryptographie française (années 1520 - années 1680)", begun on a BnF Mark Pigott grant. Our audits cite her only once (Desenclos
2018, a key). Her work is a premise source (CLAUDE.md rule 1 / rule 10) we have not searched for most of our BnF targets.

Model Opus 5.5. Cap USD 10, box 75 min, stop at 80% of either. Claim in ROOM.md first (tools/room.py), done line at the end.
Good-citizen rule; host table in CLAUDE.md; keys only via env, never printed.

1. Bibliography: list her publications (thesis 2014 and its published form, articles, chapters, the Pigott project outputs,
   any book on cryptography, conference papers, blog/Carnet Hypotheses posts, edited key collections) from HAL (api.archives-
   ouvertes.fr), theses.fr, OpenAlex (OPENALEX_KEY header), Semantic Scholar (S2_KEY), Persée, OpenEdition, CrossRef, Google Books
   API (&country=US, GOOGLE_BOOKS_KEY). Write sources/desenclos/2026-10-04/bibliography.tsv (year, title, venue, url, open full text y/n).
2. For every BnF-held target with a reading counted or outward-facing (status.json results + CONTRIBUTIONS.md rows: at least
   espagnol142-mercy-1648, ceppo-nevers-fr3251-1570s / nevers-birago-fr3251-1572, fr3416-nevers-fils-1589, fr3621 Dinteville 1592,
   fr2980-gramont, fr20140-danzay-1557, dupuy452-carpi-1520, dupuy468-anhalt; add any other BnF fonds target you find in status.json),
   search her open full texts (HAL PDFs, OpenEdition HTML) by shelfmark, folio, sender/recipient, date, and key name. Log per target:
   searched what, hit or no hit, quoted sentence if hit. Paywalled items: one JSTOR-QUEUE.tsv row each (phrase family + shelfmark
   family, CLAUDE.md verifier template step 2(g)); a book not open: LOCAL-QUEUE row only after tools/key_livecheck.py.
3. Any hit that prints a decipherment, a key or a clear text of one of our items: append a dated "Desenclos check" section to that
   target's AUDIT.md, downgrade the N-class if warranted (rule 10, with the citation), and list every outward file (outreach/*.md,
   CONTRIBUTIONS.md rows, SECOND-OPINIONS-QUEUE rows) whose sentence is now wrong -- correct repo files, flag sent ones in ROOM for
   the orchestrator. No hit: a one-line "Desenclos check, 4 Oct 2026: no hit (sources)" in each AUDIT.md.
4. Draft outreach/desenclos-intro.md (French, then a separator and the full English version, outreach/README.md rules 1, 1a, 6, 7, 8):
   header status/to/subject/prior_contact/targets/sign-off ([SIGN-OFF]). to: "the address on her Université de Picardie or
   Chartes directory page (link both; copy it from the page when sending)" -- do NOT write any personal email address into the repo.
   prior_contact: search CONTRIBUTIONS.md and outreach/ for Desenclos (the Gmail mailbox is not reachable from this session; say so).
   Content: who we are (disclosure sentence), the BnF's referral, the Mercy f.22 reading (state it exactly as AUDIT.md's current safe
   sentence and figures, rule 10 wording, a proposed cryptanalytic reading with its uncertain-sign share), and one concrete question
   (does she know a prior decipherment or key for Espagnol 144 ff.20-22, and would she be willing to look at the reading). Add a short
   list of our other BnF French readings only if step 2 found nothing contradicting them, each with its AUDIT.md safe sentence. Links:
   repo folder, Gallica ark at the leaf, AUDIT.md. Do not send anything.
5. Do NOT write the gate-7 `checked:` line yourself (a separate session does). Push by explicit path; tools/file_shrink_guard.py on
   every pre-existing file you touched; done line with commit, per-target hit/no-hit counts, request counts per host.
Report what was found and where it was not found; do not classify novelty beyond correcting an AUDIT.md the evidence contradicts.
