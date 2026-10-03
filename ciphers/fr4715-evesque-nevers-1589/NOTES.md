open
Gomberville (ed.), *Les Mémoires de M. le duc de Nevers* (1665; Google Books H2eV4wAmIr0C and three other copies) full-text searched by this worker (NV-INTAKE, 3 Oct 2026) via the Books API with `&country=US`: "Nouembre 1589" 0 hits, "Novembre 1589" 0, "17 Nouembre" 0; positive control "Rethelois" 3 -- letter not printed there.

# BnF fr.4715 f.38 (no.17), "Evesque" to the duc de Nevers, 17 November 1589, key no.25 -- NV-03

Intake only (NV-INTAKE, account 2 for the account-3 orchestrator, brief `.claude/briefs/runs/2026-10-03-acct3-nv-intake.md`).
Source row: NEVERS-VEIN.tsv NV-03. No image read in this job; no ciphertext on disk yet.

- Holding: BnF Français 4715, Gallica ark:/12148/btv1b52509819x, c91 (38r), c92 (38v) per manifest labels (scout).
  38r-38v are clear French with ~2 lines of figures at the foot of 38v (~35 two-digit); the scout saw a few interlinear
  marks over the figures at 900 px.
- BnF dépouillement (sources/bnf-aem/cc577658_francais4715.html), verbatim: "Fol. 38 • 17 Lettre avec chiffre. Au dos on
  lit, de la main du duc de Nevers, le mot « Evesque » et la date du « 17 novembre 1589 »."
- Tomokiyo (nevers.htm, "Nevers Collection no.25, no.26"), verbatim: "no.9 (f.27) \"Evesque\" to Duke of Nevers?, 2 December
  1589 no.17 (f.38) \"Evesque\" to Duke of Nevers?, 17 November 1589 ... No.25 of the Nevers collection is used in these. It
  is not no.70 of the Nevers collection. ... For f.38, see \"39\" used as a null." -- he identified the key from f.38's
  figures (so he has looked at its cipher) but prints no reading of f.38. bnf4715.htm has no section for no.17.

## Check-solved (NV-INTAKE, 3 Oct 2026)

(1) web -- below, nothing; (2) print -- Gomberville 1665, absent; (3) community lists -- Tomokiyo quoted above (key
identified, no reading); (4) DECODE -- no record; (5) Bourdeau -- only the fr.4715 Gallica manifest/notice in
research/gallica_sweep/; (6) Aymeloglu -- nothing. Cabinet Noir reads fr.4715 n27/n35/n37/n47/n48/n58 (Montholon),
not n17/f.38. Verdict: **open** (low; ~35 tokens; premise (c) unsettled -- see below).

## Solver repositories and Cabinet Noir (NV-INTAKE, 3 Oct 2026)

Shallow clones, 3 Oct 2026 03:13 UTC: el-descifrador/cabinet-noir HEAD 47b6db9 (Cabinet Noir v1.0, 29 Sept 2026,
CC BY 4.0), dbourdeau/cyphersolver HEAD 4aedb40, aaymeloglu/unsolved-ciphers HEAD d2800bb. Grepped every file for the
shelfmark (3993, 3416, 4712, 4715 + folio), the Gallica arks (btv1b9059229n, btv1b9058240c, btv1b52509819x,
btv1b9058289m) and the key numbers (no.25, no.70, duchess no.1/2/4).
- Cabinet Noir: reads only Montholon letters (fr.3414 ff.126-127; fr.4715 n27 f.50, n35 f.58, n37 f.60, n47 f.70,
  n48 f.71, n58 f.81; vues 115, 131, 135, 155, 157, 177 of btv1b52509819x) with keys Vieuville-Nevers and fr.3995 no.71.
  Its only fr.4712 mention is f.7r (vue 15), used as the period pair for no.71. No fr.3993, fr.3416, fr.4715 f.38 or
  fr.4712 f.10, no key no.25 or no.70.
- Bourdeau: targets nevers1574/1587/1588/1589/1593/1595. nevers1595 is fr.3993 no.102 ff.148r-149r (Nevers to
  Villeroy, 16 Aug 1595), not ff.71-72; its NOTES.md says "the Balagny and Charles de Gonzague ciphers of the same weeks
  are different systems" from the f.148 cipher and lists fr.3995 nos.68-74 as "Italian or figures only" -- no.70 was
  looked at for a different letter and not applied to any Charles de Gonzague letter. fr.3416, fr.4712 and fr.4715 f.38:
  only in the raw nevers.htm/league.htm copies under research/gallica_siblings/src/ and the fr.4715 manifest/notice in
  research/gallica_sweep/ (a sweep, no reading). targets/napoleon/unsolved.htm repeats Tomokiyo's line "BnF fr.4712
  contains some undeciphered letters".
- Aymeloglu: no hit for these shelfmarks (the decode-catalog.csv hits on 3993/3416/4712 are DECODE record ids of
  unrelated items).
- DECODE: our catalogue snapshots in sources/decode/ (records-non-decrypted-2026-09-24-diff.tsv, keys-all-2026-09-28*.tsv,
  keys-na-p58/p59-128) carry no record for BnF Français 3993, 3416, 4712 or 4715; DECODE's Nevers records there are
  fr.3975/3976 (Bourdeau's targets). Not re-queried live this session.

## Web and blog check (NV-INTAKE, 3 Oct 2026)

Plain web searches: (1) `"Français 4715" Nevers "17 novembre 1589" chiffre Evesque` -- Wikipedia (François I/II of
Nevers, County of Nevers), HISCOD 04715fr (unrelated finding aid), data.bnf.fr Claude d'Angennes: none about this letter;
(2) `"fr.4715" OR "fr. 4715" Nevers cipher letter 1589 "Evesque" deciphered` -- Desenclos & Lasry 1592, HistoCrypt pdf,
HSE pdf, 2022 Philip II news: nothing on f.38; (3) distinctive phrase: none on disk; (4) title covered by 1-2. Nothing
plausible to open.
Blog site searches (shared by NV-01/02/03/09, 3 Oct 2026): `site:ciphermysteries.com Nevers cipher Gonzague` -- no ciphermysteries.com page returned; `site:scienceblogs.de klausis-krypto-kolumne Nevers Gonzague` -- Cipherbrain 2019/01 archive, page/60, a Louis XIV letter post (31 Jan 2019) and "Norbert Biermann solves encrypted letters from the 17th century": none about a Nevers family letter; `site:cryptiana.blogspot.com Nevers` -- no Cryptiana blog page returned; Tomokiyo's own pages read from the local mirror (nevers.htm, bnf4715.htm, league.htm). Recurring hit: Desenclos & Lasry, HistoCrypt, "deciphering a letter from the King of France to the Duke of Nevers (1592)" (dspace.ut.ee cb0c82a2) -- a Henri IV letter, not this one.

## Premise check (NV-INTAKE, 3 Oct 2026)

(a) Folder's own files: new folder; ciphers/fr4715-vieuville-pool lists f.38 only as a physical neighbour -- not found.
(b) Other solvers: Tomokiyo identified no.25 from f.38's figures (quoted above) but no rendering exists in his pages;
Cabinet Noir, Bourdeau, Aymeloglu -- not found.
(c) Physical neighbours, from the dépouillement (images not viewed, no image reads in this job): **f.39 (no.18) is
"Lettre portant en tête ces mots, de la main du duc de Nevers : « Deschifrement de ma seur ». On y lit : « Le chasteau
d'Angers a esté pris par l'entremise de mon beau filz par Le Hallot... »"** -- a decipherment bound on the next leaf. It
is headed as the decipherment of a letter from Nevers' sister, not of the "Evesque" letter, so it is probably not f.38's
gloss, but it must be viewed before any key work. f.37 (no.16) "Lettre en chiffre, avec déchiffrement, concernant ...
la prise de Chaumont en Bassigny. 1590 ?" (no gloss of f.38 by its description). The 38r clear text itself may be a
decipherment written out (scout's flag) and the interlinear marks over the figures may be a partial gloss: **unsettled**
-- view c91, c92 and f.39 (c93) at native resolution first.
(d) Recipient side: Nevers (Gomberville 1665) absent; the sender is unidentified ("Evesque"), so no sender edition.

## Intake gate

`python3 tools/intake_gate_check.py fr4715-evesque-nevers-1589` (NV-INTAKE, 3 Oct 2026):

```
fr4715-evesque-nevers-1589: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```

## While waiting

Next step depends on nobody: view c91-c93 (38r, 38v, 39r) at native resolution to settle premise (c) -- is 38r the
written-out decipherment, do the marks gloss the figures, is f.39 its decipherment (one Sonnet image call per canvas,
~USD 1.5 x 3 = ~USD 4.5, or fold into NV-02's run, which needs key no.25 anyway). If it stays open: two blind passes of
the ~35 figures + reconciliation, then key no.25 with the glossed fr.4715 ff.27, 59, 68, 69 as known-answer control.

`python3 tools/next_steps.py --wait-only | grep fr4715-evesque-nevers-1589` (NV-INTAKE, 3 Oct 2026, 03:29 UTC): no line.
