# DEB-SWARM-F sources (29 Sept 2026)

Masonic and fraternal cipher keys collected for the Debosnys comparison. Every item accessed 29 Sept 2026. A fuller
source log from the collecting subagent (every URL tried and its HTTP result, Templar/Rosicrucian/Agrippa notes) is
kept unedited in `SOURCES_raw_subagent.md`.

## 1. Royal Arch ("pigpen") cipher, period print -- read on the page

- David Bernard, *Light on Masonry* (Utica: W. Williams, 1829), p. 138 (key figure: a # and a separate X, then the
  26 signs under A-Z; "beginning at top of this diagram at the left hand angle ... the same with a dot is B"), p. 143
  (narrative). Internet Archive `lightonmasonrya00berngoog`, leaf 150 = p. 138:
  https://archive.org/download/lightonmasonrya00berngoog/page/leaf150_w1400.jpg . Crop kept as
  `data/img/bernard_1829_p138_key.png`.
  Design: 13 frame pieces (nine # cells in reading order, then four X wedges), each used bare for one letter and
  dotted for the next: A-R from the # (A = ┘, C = ⊔, E = └, G = ⊐, I = ▢, K = ⊏, M = ┐, O = ⊓, Q = ┌, each followed
  by its dotted form), S-Z from the wedges (S V, U <, W Λ, Y >, each followed by its dotted form). J has its own sign.
  This differs from the modern "grid, dotted grid, X, dotted X" layout.
- Avery Allyn, *A Ritual of Freemasonry* (1831), p. 141, and Malcolm C. Duncan, *Masonic Ritual and Monitor* (1866;
  IA copy an undated later printing), pp. 248-249: same wording ("right angles, in various attitudes, with the
  addition of a dot ... 26 distinct characters"); text read, plates not viewed.
- Albert G. Mackey, *Encyclopaedia of Freemasonry* (1874; IA scan of a later revised printing), s.v. "Cipher
  Writing": Agrippa's nine chambers, the French St Andrew's-cross addition, Rockwell's printing in the Georgia
  *Ahiman Rezon*. Text only.
- Secondary only: Wikipedia "Pigpen cipher" (modern layouts; Rosicrucian 9-cell with 1-3 dots). Knights Templar
  Maltese-cross cipher: only a 20th-century reprint (Bothwell-Gosse, via freemasonry.bcy.ca); no per-letter shapes
  seen; not used for a key.

## 2. Copiale cipher -- key and full text, known answer

- Kevin Knight, Beata Megyesi, Christiane Schaefer, "The Copiale Cipher", *Proceedings of the 4th Workshop on
  Building and Using Comparable Corpora* (ACL, 2011), https://aclanthology.org/W11-1202.pdf . Figure 2 (transcription
  scheme with the glyphs; crop kept as `data/img/knight2011_fig2_scheme.png`) and Figure 6 (plaintext letter for
  every transcription code). What the paper reports, in our words: homophonic letters (all five circumflexed
  vowels = E; several symbols each for N, R, I ...), unaccented Roman letters = word spaces (not nulls), a colon that
  repeats the previous consonant, symbols for letter groups (SCH, ST, CH, SS, EN/EM), capitalized Roman letters at
  paragraph starts that "look nice, but are meaningless", and large symbols that are logograms for names of people
  and organizations.
- Stockholm University project page, "The Copiale Cipher"
  (https://www.su.se/english/research/research-catalogue/research-projects/d/decipherment-of-historical-manuscripts/the-copiale-cipher):
  the full transcription (`data/copiale-transcription.txt`, August 2011, 1,921 lines) and the line-aligned German
  decipherment (`data/copiale-deciphered.txt`). Header of both lists the logograms: o.. society, star secret, nee
  master, tri.. lodge, bigx freemason, gate table-shaped, lip oculist, bigl position of feet, tribig lodge, sci God,
  toe power. Copied unmodified; credited to the Copiale team.
- The key we use (`copiale_value` column of `reader1_copiale.tsv`) is read from Figure 6 through Figure 2's code
  names: e.g. fem -> A, mal -> V, cross -> SCH, tri -> O, lam -> T, three -> R, bar -> S, x. -> G, c. -> L, no -> Ö,
  grc -> SS, gam -> H/K, unaccented Roman letters -> space.

## 3. Folger manuscript -- design known only at second hand

- D. H. Bennett, "An Unsolved Puzzle Solved" (NSA Cryptologic publication; https://media.defense.gov/2021/Jun/30/2002752891/-1/-1/0/UNSOLVED%20PUZZLE.PDF):
  HTTP 403 to curl and WebFetch (one retry each); the Wayback route failed. Not read.
- S. Brent Morris, *The Folger Manuscript: The Cryptanalysis and Interpretation of an American Masonic Manuscript*
  (Masonic Book Club vol. 23, 1992): presumably prints key and text; no online copy found.
- California Freemason, "The Code Breakers" (28 Aug 2020), https://freemason.org/2020/08/28/the-code-breakers/ :
  Robert B. Folger's manuscript, New York, 1827, "A History of Royal Arch Masonry"; each figure composed of several
  characters nested in groups inside boxes; 42 pct of boxed groups carry a horizontal line near the top; whole-word
  figures for AND, HIS, THEY; the plaintext a Master Mason lecture of a French-style lodge.
  So no Folger key or text is available to us: the Folger control asked for in the brief is **unreachable** from
  the cloud this session. The design parallel (composite signs built from stacked elements, many with horizontal
  bars) is noted in LOG.md as a lead, untested.
