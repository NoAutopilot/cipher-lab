status: drafted 8 Oct 2026 08:2x UTC by OUT-DEB-D (Sonnet drafter, for lane OUT-DEB / the account-3 orchestrator); NOT gate-7 checked -- do not send before a `checked:` line exists; no mailbox draft created
to: research@adkhistorymuseum.org (the museum's research address, read on https://www.adkhistorymuseum.org/research by OUT-CHECK-DEB-PAPERS 1 Oct 2026; same address as the earlier drafts)
subject: Re: Henry Debosnys papers -- what we have tried since your scans
prior_contact: project mailbox thread 1a0defa3b687c1b2; the museum's reply of 7 Oct 2026 19:51 UTC (ciphers/debosnys-1883/NOTES.md "Museum reply, 7 Oct 2026"); our letter of 6 Oct 2026 (CONTRIBUTIONS.md, SENT 6 Oct 01:56 UTC). Send as a reply in that thread.
rule-1c: other unsent drafts to this address: outreach/debosnys-museum-hires.md (SUPERSEDED 1 Oct, never sent), outreach/debosnys-museum-papers-addendum.md (merged into / folded under debosnys-museum-papers.md, which was SENT 6 Oct 2026 01:56 UTC). Sent in the last 7 days: the 6 Oct letter (answered 7 Oct). outreach/debosnys-museum.md SENT 26 Sept. So this is the only message queued to the address; the gate-7 checker confirms.
holdings: from the museum, the scans of Debosnys's clear-text writings received 28 Sept 2026 -- NOTES.md says the museum holds 26 original foolscap sheets, "all already sent to us on 28 Sept"; RESTRICTED.md says "about 43 images" (Google Drive folder). Both are as recorded; not reconciled here. Resolution: not recorded in the repo. Held off-repo under RESTRICTED.md; listed by file name only in the private repo. Public: the four cryptogram images published on Klaus Schmeh's Cipherbrain blog and the published clear-text poems (incl. the 14-line French poem on the page of cryptogram 3; the Greek/English verso texts as published by others); Farnsworth 2010 credit lines and Bauer 2017 as read in print.
ask: NONE. ATTEMPTS.md ("What would move it") names sharper images of the original cryptogram sheets as the blocking step, and the earlier 29 Sept draft (debosnys-museum-hires.md) asked for them -- but that draft was never sent, and the museum's 7 Oct reply says all 26 sheets it holds were already sent on 28 Sept and asked us to wait for a written record before any further ask. Whether the cryptogram originals are among those sheets, and at what resolution, can only be answered from the restricted scans (which this draft may not describe) and the private inventory, so an ask could be for something already held. The owner/checker may add one question later after that private inventory check; not added here.
restricted: describes, quotes and shows nothing from the museum's scans (RESTRICTED.md rules 1-2); only that they were used for reference. Everything reported comes from ciphers/debosnys-1883/ATTEMPTS.md, which uses the public images.
sign-off: [SIGN-OFF] left blank for the person (rule 9)

# Draft email: Adirondack History Museum, step 3 (what we have tried; no request)

## Text

Dear Carol,

Thank you for your reply of 7 October, and for the plain account of what the museum holds: the 26 original sheets, the other items, and what is and is not known about the donor and the trunks. I am sorry that my letter of 6 October asked for sheets you had already sent. I direct this project and send its letters myself; AI agents (Claude models) do the reading, the searches and the checking, and every step is logged in the open repository linked below.

I said I would write again once we had a written record of the work, rather than send more requests, so this letter asks for nothing. We have written down, in plain English, everything we have tried on Henry Debosnys's four cryptograms, including the attempts that failed, in a file you can read here: https://github.com/NoAutopilot/cipher-lab/blob/main/ciphers/debosnys-1883/ATTEMPTS.md (the whole folder is at https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/debosnys-1883).

The short version: nothing has been read. We have not read a word of the four cryptograms, and we do not have a partial reading.

For each approach we first built a control, a made-up cipher of the same size and design with a known answer, to check that the method could read such a cipher at all. A failure on the real cryptograms counts only if the method succeeded on its control. Everything below is about one design at the image quality we have; none of it is a proof that anything is impossible.

- Transcription. We worked from the published images, in which each sign is very small. Two independent readers, tested on a page with known answers, misread about 15.6 to 17.7 per cent of the signs. We believe that is the limit of the images, not of the readers.
- Letter-for-letter substitution. In French the solver read 0 of 8 real runs against 5 of 8 on its control; in Portuguese 0 of 24 against 4 of 4. In English the real text scored at the 8th percentile against 100 of 100 for the control. These are negatives for that design at the current transcription. Spanish and Latin could not be decided because the controls were weak.
- Syllable and mixed systems. The data fit these best, but the solver for them could not read its own control once copying errors were added, so we could not decide.
- Order of the text. Cryptograms 1 and 2 behave like the control with no language in it, for every kind of cipher that keeps the order of the text, up to about 25 per cent error. That test is weaker on the shorter verse pages.
- Shifting-alphabet, autokey and word-code designs, and pigpen and Copiale-style signs: each control was read and the real text was not, so these designs are disfavoured. Column transposition and "padding" signs could not be decided.
- The sign that looks like X is not a plain word divider (p 0.25 and 0.36 against 0.000 for a control that has word spaces).
- Guessing known text. The clear French poem on the cryptogram-3 page matched none of the cryptograms (0 of 24 tries, while the control always matched), nor did the Greek and English texts on the reverse of cryptogram 4 (0 of 48 each), nor eight period poems tried against cryptogram 4.
- What the numbers do show: one key appears to be shared across all four pages, line endings of the verse page rhyme as if signs stand for sounds (p 0.0001), and picture signs open lines far more often than chance. These are properties of the writing, not a reading.

The main obstacle is image quality. The automatic solvers for the likely designs pass their own controls only when the sign error is below about 5 to 8 per cent; ours is 15 to 18 per cent on the two longest pages. Until that changes, we cannot test the most likely designs.

We used the museum's scans for reference only. Any finding that depended on them would be published only with the museum's written permission, and nothing from them is in the repository.

Thank you again for your time and help. If anything in the file looks wrong to you, I would be glad to hear it.

[SIGN-OFF]
