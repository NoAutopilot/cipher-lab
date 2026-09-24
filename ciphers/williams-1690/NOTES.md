Status: found-solved

# 30 Jun 1690, unknown (London) to John Williams — Bodleian MS. Eng. misc. c. 382, p. 223

Check-solved pass, LANE N2 worker csEM, 24 Sept 2026 (`date -u` at session start: 2026-09-24 10:48 UTC). Brief:
`.claude/briefs/runs/2026-09-24-lane-n2-csEM.md`. Source row: QUEUE.md EM5 (LANE N2 scout scEM2, 24 Sept 2026,
from `sources/emlo/cipher-letters-2026-09-24.tsv`).

## The item

EMLO abstract (quoted in QUEUE.md EM5): "Two simple substitution ciphers used interchangeably where plain
text letters of the alphabet have been substituted for other letters of the alphabet, removed a certain
number of places. The cipher is used intermittently throughout the letter." Abstract present: "A letter
concerning Scottish affairs. The author advises the recipient on acquaintances to trust and how to deal with
money issues." EM5's own open question was whether that abstract describes only the clear portions or the
whole letter including the ciphered parts.

## Search log and the answer

**Identifying the volume.** WebSearch (`"Eng. misc. c. 382" Wallis Bodleian cipher deciphered`) surfaces the
Bodleian Archives & Manuscripts finding-aid record for this exact shelfmark (`archives.bodleian.ox.ac.uk/
repositories/2/resources/3901`, "Volume of copies by John Wallis of political correspondence deciphered by
him for the government"). The finding-aid page itself 503'd on WebFetch (both attempts this pass, and once
more from the EM4 pass a few minutes earlier — three total, not retried further), but WebSearch's own summary
of it, built from the page's indexed text, states unambiguously: **"MS. Eng. misc. c. 382 is a volume of
copies by John Wallis of political correspondence deciphered by him for the government, with keys to the
ciphers used, from 1669-70, 1688-95, and 1702-3... At folio iii is an account by Wallis of his experience of
deciphering letters, dated 17 March 1703."** This is the same shelfmark EMLO gives for EM5 (p. 223) and for
EM3 (pp. 221, 224-225) — same volume, not a coincidence.

**Reading.** A volume whose finding-aid title is literally "copies... deciphered by [Wallis] for the
government... with keys to the ciphers used" is, on its face, Wallis's own output file of solved material —
the mirror image of MS. e Musaeo 203 (EM4), which is explicitly his 1653 intake file and names its four
holdout letters as *not* deciphered. Nothing in the finding-aid summary or in EMLO's abstract for this item
says this one letter is an exception the way EM4's four are (no "[Abstract unavailable because not
deciphered]" placeholder, no note that the cipher passages defeated Wallis). The 1690 date sits inside the
volume's stated 1688-95 span. The most likely reading of "cipher used intermittently throughout the letter"
plus a normal, complete-sounding abstract ("advises... on acquaintances to trust and how to deal with money
issues") is that Wallis's own copy already carries the ciphered passages in clear — i.e. **this letter was
already read, by Wallis, as part of assembling this very volume**, and EMLO's abstract describes the whole
letter, cipher included, not just its clear stretches.

**Caveat.** This is inferred from the finding-aid's volume-level description (via a WebSearch summary of a
page I could not load directly — the finding-aid itself 503'd three times) and from EMLO's own abstract text,
not from reading the manuscript or a transcription of this specific letter. It is not a quotation of a
source that names this exact letter by date (rule 10 / M9 lesson: no source read this pass says "the 30 June
1690 letter to Williams, solved"). Graded **M** (uncertain / inferred), not H or C.

**Other sources.** WebSearch for `"John Williams" 1690 Scottish affairs cipher letter Bodleian "Eng. misc"`
found nothing naming this specific letter (results were CELM catalogue landing pages and unrelated Williamses).
Bourdeau's and Aymeloglu's clones (already cloned for EM4, grepped again): no hit for "Williams" matching this
context (their only Williams-adjacent DECODE rows are 1670s-80s Secretary Williamson material, a different
person, different decade). DECODE not queried directly (host reserved this run). Digital Bodleian: browser
search for `"Eng. misc. c. 382"` returned **"No items found"** (see wallis-emus203-undeciphered/NOTES.md §1f
for the same fetch — one search covered both EM3/EM5's shared shelfmark and EM4's), so no image route
confirmed either.

## Verdict

**found-solved (F1/F2, tentative — M-grade, not verified by a primary read).** The letter is very likely
already deciphered, by Wallis himself, as part of the same government-copy volume EMLO drew the abstract
from; nothing supports treating it as unsolved. Not scored `open`, and no nomination line posted. This is a
**correction candidate for EM3** too (Austen 25 Feb 1691 and Sedley 3 Mar 1691, same shelfmark MS. Eng. misc.
c. 382, pp. 224-225) — flagged in ROOM.md and QUEUE.md rather than acted on, since EM3 is outside this
brief's two named targets (EM4, EM5) and the brief says never start a target it does not name.

**What would move this from M to H:** archives.bodleian.ox.ac.uk's actual finding-aid text (currently 503,
Bodleian-side outage per the EM4 note) or a folio-level look at the volume (Digital Bodleian has no image
under this shelfmark) naming this letter's own deciphered copy and key, or Beeley & Scriba's edition /
Beeley's articles on Wallis-as-decipherer if they discuss this letter by date.

## Requests (this pass)

WebSearch 2 (folded into the EM4 pass's totals where the same query served both items — see that file's
count for the shared Digital Bodleian and clone work). archives.bodleian.ox.ac.uk: 0 further direct hits (used
up in EM4). No subagents.

## Files

None (no ciphertext transcribed — check-solved only).
