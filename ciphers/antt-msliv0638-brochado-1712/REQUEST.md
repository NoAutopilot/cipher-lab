# Copy request -- British Library Add MS 20819 (and Add MS 15182, second priority)

**Status:** waiting on the owner (ASKS row 108). Written 3 Oct 2026 by FT4-antt-msliv0638-brochado-1712 (account-4).
Target folder: `ciphers/antt-msliv0638-brochado-1712` (ANTT Manuscritos da Livraria 638, José da Cunha Brochado's
London letter-book, 1710-1715). Stage 2 verdict: partial (NOTES.md line 1; intake gate exit 0, 3 Oct 2026).

## What is wanted, and why

The ANTT volume's own appendix ("Cartas em Cifra e Passages da mesma ... deciffradas", m0279-m0296) deciphers 38
cipher entries, which gave the key (key.tsv). One coded letter has no gloss: **letter 134**, the letter that opens
on page 134 of the letter-book (DigitArq images m0273-m0277), closing "Londres 22 de Outubro de 1713" (closing
date as read on m0277, body_leaves.tsv; the page number on m0277 was not read with confidence). It carries two
coded runs, 70 tokens in all (m0275-r1 + m0276-r1, m0276-r2), beside clear-text mentions of "o novo Enviado",
"seu novo Tractado" and "O Estrangeiro". Our candidate decode of it fails its calibrated judge (NOTES.md,
Remaining gaps), so the cheapest way to settle it is another copy of the same letter in which the coded passage is
deciphered or written out in clear.

The British Library holds two other copies of Brochado's London letters (catalogue records read 3 Oct 2026 through
`searcharchives.bl.uk/catalog/<id>?format=json`; both have an empty "Digitised Content" field, i.e. not digitised):

1. **Add MS 20819** (first priority). Record 040-002091165, ark:/81055/vdc_100000001555.0x000035, part of Add MS
   20785-21005 (Charles, Lord Stuart de Rothesay). Catalogue: *"CARTAS sobre as negociações de Inglaterra escritas
   pello Inviado Extraordinario Joseph da Cunha Brochado aos nossos Plenipotenciarios em Utrecht sobre a nossa
   pax;" dat. London, 20 July, 1710-1 Sept. 1715. Paper. Folio.* ... *Letters and papers, when Portuguese envoy to
   England: 1710-1715.: Portug.: Copies.* Date range 20 Jul 1710 - 1 Sep 1715; extent "1 item"; no folio list in
   the record. Same sender, same years, letters to the Utrecht plenipotentiaries -- very likely the same series
   as the ANTT letter-book (inferred from the title and dates; not yet compared letter by letter).
2. **Add MS 15182** (second priority, only if 20819 lacks the October 1713 letters). Record 032-002086880,
   ark:/81055/vdc_100000000052.0x0001ec. Catalogue: *"CARTAs de Jose da Cunha Brochado, estando por Ministro de
   Portugal na Corte de Londres, desde o anno de 1710 até o de 1714. Dirigidas ao excellentissimo Conde de Vianna,
   Mórdomo Mór. Copiadas das Originaes e fielmente escriptas." Recent transcript. Folio.* Date range 1710-1714.
   A different addressee, so it will not hold letter 134 itself, but a letter to Viana of late October 1713 may
   report the same news (a paraphrase crib); it is a later ("recent") transcript.

## Exact request

Step 1 (ask first, no cost expected): for **Add MS 20819**, the folio numbers of the letters dated London,
**22 October 1713** and **29 October 1713** (the letters on either side; the ANTT copy's letter 135 is dated
29 Oct 1713), or, if the volume has no index, the folio range covering **October-November 1713**.

Step 2: digital images (or photocopies) of those folios -- the 22 Oct 1713 letter in full, about 4-5 folio pages
on the ANTT copy's scale, plus the 29 Oct 1713 letter if cheap.

What to look for on receipt: in the 22 Oct 1713 letter, the passage near "o novo Enviado" / "seu novo Tractado" /
"O Estrangeiro": is it in cipher (then compare the groups with body_ciphertext.tsv m0275-r1/m0276), deciphered
between the lines, or written in clear? Either of the last two turns letter 134 into a key-calibration item (and
possibly found-solved for that passage, rule 10 class N0/N1 for any later reading).

Step 3 (only if Step 1 shows 20819 lacks October 1713): the same question for **Add MS 15182**, letters to the
Conde de Vianna dated October-November 1713.

## Route

British Library item requests, `itemrequests@bl.uk`, or the "online collection item request form" linked from each
catalogue record (forms.office.com link in the record's access note, read 3 Oct 2026). The batched BL enquiry
`outreach/bl-imaging-quote-batch.md` is already gate-7 checked and queued (SEND-QUEUE S2), so these two items were
not added to it (that would void its `checked:` line); they go in the next BL batch or as a separate short enquiry.
Note from that draft: the BL may answer that an original can only be copied from an existing microfilm surrogate, or
needs a reader visit.

No personal data (name, address, payment details) is recorded here or should be, per CLAUDE.md rule 9.
