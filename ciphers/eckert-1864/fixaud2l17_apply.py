#!/usr/bin/env python3
"""FIX-AUD2-L17 (10 Oct 2026, owner account, for LANE LEDGER-17 / the orchestrator): apply the s.5/s.6 corrections of
AUDIT 2 (AUD2-LEDGER17-1) for E585 E581, AUDIT 2 (AUD2-LEDGER17-2) for E594 E591 and AUDIT 2 (AUD2-LEDGER17-3) s.6 for
E623 E622 to ciphertext.txt as header edits, decoder directive lines and one 'note: FIX-AUD2-L17' line per entry.
Same method as fixl17c_apply.py (reused run()); reading.md only by decode.py --write. Idempotent: skips a block that
already has a 'FIX-AUD2-L17' note. E622 also needs two direct line fixes (image-checked by AUD2-LEDGER17-3): the
duplicated 'Mandate' on the vessel-list line (5615) and the missing 'pedlar' on the signature-tail line (5616); both
are applied once, guarded by checking the old text is still present. key.md is not edited."""
import fixl15_apply as base
base.MARK = 'FIX-AUD2-L17 (10 Oct 2026'
base.E.clear(); base.LF.clear()
E = base.E
def S(e, h=(), d=(), n=''): E[e] = dict(h=list(h), d=list(d), n=n)
def N(src, body): return "FIX-AUD2-L17 (10 Oct 2026, owner account, for LANE LEDGER-17 / the orchestrator; %s): %s" % (src, body)

S('E581',
  h=[("(FM-S65A; row 5862/0; read from the transcription, no image)",
      "(FM-S65A; row 5862/0; image-read by FV-L17a and AUD2-LEDGER17-1, matches the transcription; N3 D2: dateline "
      "corrected from 1864 to 1865 on the leaf, a new-year slip (AUD2-LEDGER17-1); external context only (O'Brien "
      "pp.180-181; E521 the question), not a check of the text)")],
  d=['plain-at: queen#1'],
  n=N('AUD2-LEDGER17-1 s.5, AUDIT FV-L17a s.3/s.5',
      "'River [Danger]' -> River Queen, the vessel name (plain, lower-case 'queen' on the leaf; Queen = Danger is a "
      "key-row collision): H 6 + 1 plain of 7 (was H 7, the collision counted as a code word). 'Fanny' (11 AM) and "
      "'gown' (= gone, plain-phonetic) stand as read, already H/plain by the key; FM-S65A's M on them is withdrawn. "
      "Class N3 D2 (kept, both audits): the clause reads and does not survive the shuffled-key control (FM-S65A); "
      "context only, O'Brien pp.180-181 and E521 (the question this answers). Dateline: the leaf's '1864' is "
      "overwritten '1865' (a new-year slip, AUD2-LEDGER17-1). Not N4: The Papers of Ulysses S. Grant vol. 13 not "
      "searched (Google Books 429, three sessions)."))

S('E585',
  h=[("(FM-S65A; row 5872/2; read from the transcription, no image)",
      "(FM-S65A; row 5872/2; image-read by FV-L17a and AUD2-LEDGER17-1, matches the transcription; N3 D3: both "
      "Division words (quitman l.1, Quincy l.2) overwritten in darker ink on the leaf (AUD2-LEDGER17-1); external "
      "non-statistical check: holder 7687 (Sheridan, 6 Jan 1865, 'the men have fully 40 rounds of ammunition on "
      "their persons', printed OR I/46 pt 2 pp.55-56), Grant's 12 Jan order sending Sheridan's troops at Fort "
      "Monroe on to Savannah and Morgan forwarding the 1st Brig., 2d Div., 19th Corps (OR I/46 pt 2 pp.105-107), "
      "Grover at Savannah 18 Jan (OR I/47 pt 2 p.90))")],
  d=['variant: polking=Polkaing:H'],
  n=N('AUD2-LEDGER17-1 s.5, AUDIT FV-L17a s.3/s.5',
      "'polking' = Commanding ('polka' = Command + -ing, H; lift M), closing 'Brevet [Major] [General] ... "
      "Commanding'; H 15 of 15 (was H 14). 'Eugenia Snake plank quitman hope pelton' (9.30 AM / Head Quarters / 2 / "
      "Division / 19 / Corps) are ordinary H key rows; FM-S65A's M on them is withdrawn. Class N3 D3 (kept, both "
      "audits): the ammunition figure is corroborated in print (Sheridan, OR I/46 pt 2 pp.55-56), the unit and its "
      "movement independently in OR I/46 pt 2 pp.105-107 and OR I/47 pt 2 p.90; the shuffled-key control leaves the "
      "numerals standing, so this corroborates content, not the key (the key-separable part is the unit-title "
      "line, which no shuffle keeps). Not N4: The Papers of Ulysses S. Grant vol. 13 not searched (Google Books "
      "429, three sessions)."))

S('E591',
  h=[("for Commodore William Radford, commanding the 5th Division (the row has '100 Radford', '5', 'Division', "
      "read from the code words), New Ironsides: no torpedoes on hand;",
      "for Commodore William Radford commanding the 5th Division, New Ironsides, Bermuda [Hundred] ('Burr Muddy', "
      "the clerk's plain-phonetic spelling of Bermuda, I; the key row Bermuda = White River misfires here, as in "
      "E624): no torpedoes on hand;"),
     ("(FM-S65B; row 5908/0; 37 tokens)",
      "(FM-S65B; row 5908/0; 37 tokens; image-read by FV-L17b and AUD2-LEDGER17-2; N3 D3: antecedent ORN I/12, "
      "Radford's own 14 Feb 1865 telegram to Wise ('I have made a requisition for 20 torpedoes that will stand "
      "immersion'), and the sister telegram E557 (5907/1))")],
  d=['variant: polking=Polkaing:H', 'merge: burr+muddy', 'gloss: burrmuddy=Bermuda:I'],
  n=N('AUD2-LEDGER17-2 s.3/s.5, AUDIT FV-L17b s.6',
      "'polking' = Commanding (H, as E585). 'Burr Muddy' = Bermuda (I, plain-phonetic, as E293 'Burr muddy to "
      "paradise Webster' = Bermuda [Hundred] to [Colonel] Webster), not a line indicator -- FV-L17b's 'Muddy = key "
      "row, line indicator: 5 lines' is withdrawn. 'Sub [Marine]' reads Submarine in sense (Sub plain + squadron = "
      "Marine, H), now also supported by holder 9944 (25 Jan 1865, Wise to Gregory: 'submarine torpedoes'), the "
      "Bureau's own term. Counts: Farmer, plaster, quincy, zodiac, wrangled, harrow, squadron, youth, polkaer, "
      "polking = 10 H/C; Burr Muddy = Bermuda I = 10 H/C + 1 I of 11, nothing unread (was 9 H of 11). Class N3 D3 "
      "(kept, both audits). Not N4: Grant Papers vol. 13 unsearched (429, three sessions), NARA RG 45 unread, two "
      "be-api queries unchecked (502)."))

S('E594',
  h=[("(the same code word is C-checked in row 5896/1, whose holder clear copy 8561 reads 'from Gen Sherman' where "
      "the cipher has 'Kitchen') (FM-S65B; row 5941/2; 28 tokens)",
      "(the same code word is C-checked in row 5896/1, whose holder clear copy 8561 reads 'from Gen Sherman' where "
      "the cipher has 'Kitchen') (FM-S65B; row 5941/2; 28 tokens; N2 (AUD2-LEDGER17-2): the telegram's sending and "
      "substance are printed by both parties -- Sherman, Memoirs (1875) vol. 2 ch. XXIII ('reaching Fortress "
      "Monroe on the morning of the 27th, where I landed and telegraphed to my brother, Senator Sherman, at "
      "Washington, inviting him to come down and return with me to Goldsboro') and John Sherman, Recollections of "
      "Forty Years (1895) vol. 1 pp.353-354; the telegram's own wording was not located in print)")],
  n=N('AUD2-LEDGER17-2 s.3/s.5',
      "no decoder change: 9 of 9 H/C stands. Class N3 -> N2 (plaintext_novelty; mapping_novelty stays N3): "
      "Sherman's own Memoirs (vol. 2 ch. XXIII) and his brother's Recollections (vol. 1 pp.353-354) name this "
      "telegram's sending (Fortress Monroe, morning of 27 Mar 1865) and its purpose (to come down and return with "
      "him to Goldsboro); the telegram's own words were not located in print. SO-ECKERT-E594 withdrawn (N2, the "
      "E28 precedent)."))

S('E623',
  h=[("mssEC 25 (obj 5952, pointer 5656), 5 May 1864 Ft Monroe, Sheldon (to Baltimore, addressee 'season' as in "
      "E310, not decoded, M): W. W. Shore is in Baltimore somewhere, was some time ago ordered out of the "
      "Department; he is to be caught, arrested and sent to Butler under guard; the evidence is in hand; he is "
      "the correspondent of the World from Baltimore as he was from here; the General telegraphed three days ago "
      "to arrest him and nothing has been heard since; if necessary a man who knows him can be sent (John I. "
      "Davenport, Lieut., Bureau of Information, as read, M) (FM-UND; row 5656/0 first telegram; transcription "
      "only, page image not eye-checked)",
      "mssEC 25 (obj 5952, pointer 5656), 5 May 1864 12.30 PM Ft Monroe, Lieut. John I. Davenport, Office Bureau "
      "of Information, to Maj. Gen. Lew Wallace at Baltimore ('season', C, as E168/E310 and holder clear copy "
      "10291): W. W. Shore is in Baltimore somewhere, was some time ago ordered out of the Department; he is to "
      "be caught, arrested and sent to me (Davenport) under guard; the evidence is in hand; he is the "
      "correspondent of the World from Baltimore as he was from here; the General telegraphed three days ago to "
      "arrest him and nothing has been heard since; if necessary a man who knows him can be sent (FM-UND, "
      "FV-L17c, AUD2-LEDGER17-3; row 5656/0 first telegram; image-read by AUD2-LEDGER17-3; N1: holder clear copy "
      "10299 (Page 157), already on file in AUDIT (FV-FM9e) s.2; under the Wave 2 RULING (i) this row is not "
      "filed, and stays here with this N1 note under the lane ruling of 10 Oct 2026; SO-ECKERT-E623 withdrawn)")],
  d=['plain-at: world#1', 'gloss: season=Maj._Gen._Lew_Wallace:C', 'plain-at: john#1'],
  n=N('AUD2-LEDGER17-3 s.3/s.6, AUDIT FV-L17c s.5',
      "addressee 'season' = Maj. Gen. Lew Wallace, Baltimore (C, as E168/E310, holder clear copy 10291), not M; "
      "'the [Valley]' -> the World (plain, 'world' collides with the key row Valley = Presence); the tail's "
      "'John' is the plain first name (collides with the key row Maj Genl U.S. Grant), not a second signature -- "
      "read Lieut. John I. Davenport, Office Bureau of Information. Class N1 (was N3): the Huntington's own clear "
      "copy, pointer 10299 (Page 157), is the clear copy of this telegram, already on file in AUDIT.md (FV-FM9e) "
      "s.2 and missed by FM-UND and FV-L17c; under the Wave 2 RULING (i) this row is not filed, and stays in "
      "ciphertext.txt with this N1 note (as E582/E587/E624 under the lane ruling of 10 Oct 2026). SO-ECKERT-E623 "
      "withdrawn."))

S('E622',
  h=[("(FM-UND, FM-UND2; rows 5614/2, 5616/0; transcription only, page images not eye-checked)",
      "(FM-UND, FM-UND2; rows 5614/2, 5616/0; image-read by AUD2-LEDGER17-3 (leaves 5615, 5616), matching the "
      "corrected transcription; N3 relay (no clear copy at any pointer after 18 fresh queries, not in OR ser. I "
      "for 19-21 Apr, not in Grant Papers vol. 10, not in OR ser. II vol. 7), N2 vessel list (Wise to Meigs, "
      "Philadelphia, 19 Apr 1864, OR I/33 p.915; holder clear copy 4546-4548); D3: every figure agrees with the "
      "print once Pioneer reads 256 tons (the transcription's duplicated 'Mandate' removed); tail 'translate "
      "Pekin & pedlar every time' is Meigs's own instruction to render both words as commas throughout (Pekin, "
      "Pedlar = Comma, key.md p.19 l.7), not an unread clause)")],
  n=N('AUD2-LEDGER17-3 s.4/s.6, AUDIT FV-L17c s.5',
      "5615 'pioneer plank prolong mandate Mandate' -> the second 'Mandate' is a transcription duplicate "
      "(image-checked); the numeral run plank+prolong+mandate+plague now gives Pioneer [256] tons, matching the "
      "print exactly (mssEC 18 copy 9712 also has one 'mandate'); FM-UND2's 'pioneer [306] ... M' is superseded. "
      "5616 'translate Pekin & every time' -> 'translate Pekin & pedlar every time' (image-checked, pedlar "
      "present): Pekin and Pedlar are both the key row for Comma (p.19 l.7), so the tail is an operator's "
      "instruction to render both as commas throughout the list, not an unread clause or an M. Relay N3 (not "
      "located after this audit's 18 holder queries, OR ser. I 1864 parts, Grant Papers 10, OR ser. II vol. 7); "
      "vessel list N2 (printed OR I/33 p.915, holder clear copy 4546-4548). Depth D3 kept."))

LINE_FIXES = [
    ("tons plague wine spit zebra pioneer plank prolong mandate Mandate",
     "tons plague wine spit zebra pioneer plank prolong mandate"),
    ("yoke meigs Bender translate Pekin & every time",
     "yoke meigs Bender translate Pekin & pedlar every time"),
]


def line_fixes(path):
    text = open(path, encoding='utf-8').read()
    n = 0
    for old, new in LINE_FIXES:
        if new in text and old not in text:
            continue  # already applied
        if old not in text:
            print('LINE FIX MISS', old[:60]); continue
        if text.count(old) != 1:
            print('LINE FIX AMBIGUOUS', text.count(old), old[:60]); continue
        text = text.replace(old, new, 1); n += 1
    open(path, 'w', encoding='utf-8').write(text)
    print(path, n, 'line fixes')


if __name__ == '__main__':
    line_fixes('ciphertext.txt')
    base.run('ciphertext.txt')
