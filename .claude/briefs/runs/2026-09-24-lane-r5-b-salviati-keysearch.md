LANE R5 WORKER B -- M35 SALVIATI: search for a key (Sonnet, cap $4; search only, no solving, no image capture).
Target: ciphers/fr2933-salviati-1525 (Cardinal Giovanni Salviati, legate in Spain, letter of 16 Oct 1525, BnF fr.2933 no.11; Italian
cleartext interleaved with invented signs). Common rules: .claude/briefs/runs/2026-09-24-lane-r5-common.md. Read NOTES.md "Source" and
"Check-solved sweep" first so you do not repeat what is logged.
Find, or log as not found, a cipher key of Giovanni Salviati's legation/nunciature of 1525-26 (or of the papal Secretariat under
Clement VII for Spain in 1524-27, Giberti's office), in this order:
1. On disk: sources/cryptiana/web/ (Tomokiyo; grep vatican*, spanish*, italian*, 'Salviati', 'Giberti', 'Clement VII', 'Castiglione');
   sources/solver-diffs/2026-09-24-cyphersolver-keys.tsv (Bourdeau's 81 published keys) and any other sources/solver-diffs/*.tsv;
   QUEUE.md; CATALOG.md; LANDSCAPE.md.
2. Online, one request at a time per host, >= 1.5 s apart: web search; Archivio Apostolico Vaticano (Segreteria di Stato, Nunziature,
   Spagna 1525-26; Meister 1906 "Die Geheimschrift im Dienste der päpstlichen Kurie" on archive.org full text for 'Salviati');
   Archivio di Stato di Firenze Carte Strozziane (inventory, 'cifra', 'Salviati'); Internet Archive full-text search (be-api fts and
   advancedsearch) for 'Salviati' + 'cifra'/'contrasegni'; Lasry/DECODE publications via OpenAlex (OPENALEX_KEY header) and Semantic
   Scholar (S2_KEY header). Not gallica.bnf.fr, not de-crypt.org.
Output: NOTES.md section "Key search (24 Sept 2026, LANE R5 B)": a table source | searched how | result (found / not found / unreachable),
and for any key found: holding, shelfmark, date, whether it has invented signs like fr.2933's (compare with glyphs/atlas.png), and a
digitised URL. Also one line each if you meet a key source for BnF 5549 (Jan van Nassau) or Bowes-Walsingham 1583; do not chase them.
ROOM done: "for LANE R5: salviati key search <found X at Y | not found in N sources>, cost $<c>". Report request counts per host.
