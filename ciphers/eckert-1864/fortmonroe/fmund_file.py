#!/usr/bin/env python3
"""FM-UND: file two of the eleven undated Fort Monroe entries into ../ciphertext.txt (Cipher No. 1): U3 5616/0 as E622 and the first telegram of U4 5656/0
(5 May 1864, W. W. Shore) as E623 (10 Oct 2026). Not filed (see NOTES '## FM-UND'): U1 5568/0 (clear 10167), U2 5575/0 (clear 4483), U8 5842/0 (clear 7666),
U10 5914/0 (clear 8602), U6 5689/0 (print: OR I/36 pt 3 p.140-141, Butler Corr. IV p.255-256), U7 5759/0 (OR I/36 pt 1 p.786), U9 5902/0 (OR I/47 pt 2 p.300),
U5 5658/0 (Butler Corr. IV, OR I/36 pt 2 p.526), U11 5951/0 (the ledger's title leaf, not a telegram), and the second telegram of U4 (clear copy 4601).
Usage: python3 fmund_file.py [--dry]  Idempotent."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
rows = {}
for ln in (HERE/"fmund_step0.out").read_text().splitlines()[1:]:
    f = ln.split("\t"); rows.setdefault(f[0], {})[f[2]] = f
def s0(F, whole=""):
    a, b = rows[F]["no1"], rows[F]["no1shuf7"]
    return (f"Step 0 (fmund_step0.py{whole}, information only on mssEC 25 under the Wave 2 ruling; the page transcription of the row is its own cipher copy): No. 1 (a) {a[4]} ({a[5]}) vs (b) p95 {a[6]}, {'HIT' if a[7]=='HIT' else 'no hit'}; "
            f"under one meaning-shuffled No. 1 copy (seed 7) (a) {b[4]} vs {b[6]}, {'HIT' if b[7]=='HIT' else 'no hit'}; (c) key-dependent words: {a[9]}. ")
BASE = "FM-UND (10 Oct 2026, account 1, for LANE LEDGER-17): book No. 1 (April-May 1864 Fort Monroe rows per BOOK-FM65's date-to-book table; share table and a No. 1 / No. 2 / No. 9 decode in fmund.out). "
SPEC = {
 "U3": ("E622", "Page 72", "mssEC 25 (obj 5952, pointer 5616; the head of the telegram is on pointer 5615 and is NOT read here), 20 Apr 1864 (date placed from the page 5614 and 5616/1 headers), Washington to Ft Monroe, signed T. T. Eckert (446 pd): a list of steamers and tows by name with times, 'total propellers 2200 & 40 tons 2800 men', '50 canal barges average capacity 150 men', '8 steam tugs', 'send steamers to Chesapeake City to meet and escort the tows down the Bay' (FM-UND; row 5616/0; tail of a longer telegram; transcription only, page image not eye-checked)",
        "H37 of 80 tokens, no M. The clause is the tonnage and tow arithmetic plus the order to send steamers to Chesapeake City ('cheese a peak city', plain) to escort the tows down the Bay; the vessel names (May Flower, Cahill, Briarly, Beverly, Hutchins, Delany, Palmer, Tempest, Ajax, Freeman, Vatterland) are plain words in the row. The decode's opening [Adjt Genl. U.S.] and tail '[signed] meigs [Qr Master Genl U.S.]' are key-row hits on cipher words in the first and last lines and are not used for the sense of the clause (M; the row is signed Eckert). The shuffled No. 1 copy gives nonsense words for the same positions ([Ram], [Etowah], [Weldon], [Ohio]) while the plain words and numerals stay, so the clause does not survive the shuffle where the key matters. Context (M): E294 is the same day's reply from Sheldon (5616/1, Biggs: no steamers to send to sea). A second cipher copy of this tail is in mssEC 18 pointer 9713 (page 'Prolong Spit Zodiac ...', preceded there by the head lines): a witness for the transcription, not a clear copy. Holder search: CISOSEARCHALL on 'Hutchins Delany Palmer Tempest Ajax Freeman' hit only 5616 and 9713; 'Vatterland Bishop steamers Escort tows Bay' only 5616; 'steam tugs canal barges average capacity propellers' only 5616 (no clear copy). Not located in print (letters-only phrase grep, 191 cached volumes: 'send steamers to Chesapeake City ... tows down the bay', 'steam tugs Hutchins Delany ...', 'total propellers', 'Hutchins Delany': none; 'canal barges average capacity' hits warofrebellion33unit only, a loose generic match, not read as this text)."),
 "U4": ("E623", "Page 112", "mssEC 25 (obj 5952, pointer 5656), 5 May 1864 Ft Monroe, Sheldon (to Baltimore, addressee 'season' as in E310, not decoded, M): W. W. Shore is in Baltimore somewhere, was some time ago ordered out of the Department; he is to be caught, arrested and sent to Butler under guard; the evidence is in hand; he is the correspondent of the World from Baltimore as he was from here; the General telegraphed three days ago to arrest him and nothing has been heard since; if necessary a man who knows him can be sent (John I. Davenport, Lieut., Bureau of Information, as read, M) (FM-UND; row 5656/0 first telegram; transcription only, page image not eye-checked)",
        "Only the first telegram of row 5656/0 is filed: the second (6 May 1864, Eckert office: Butler to Grant, Wilson's Wharf, Fort Powhatan, City Point, Hinks's colored troops, 'Flag of truce boat' at the wharf) has the holder clear copy at pointer 4601 (page 160, 'Ft Monroe Va May 6th 64 ... BF Butler Maj Gen') and sits in print (Butler Corr. IV, letters-only phrase grep). This telegram follows E310 (1 May 1864, Butler by Sheldon via G. W. Baldwin to Lew Wallace: Shore to be arrested; 'the General telegraphed you three days ago' fits 2 May). H 17 code-word tokens in this telegram. No. 1 reads it cleanly and gives Baltimore and the plain names Shore and Davenport; the decoded tail '[signed] [Maj Genl U.S. Grant]' is a key-row hit on a cipher word and is not used (M); it ends 'Sweden very warm here today Yours' in the cipher words. Step 0 on the whole row mixes both telegrams (a non-test here, below p95 on the whole row). Holder search: CISOSEARCHALL 'Shore Davenport oakumed evidence Corresp' and 'oakumed sent to me under guard Shore' hit only 5656 (the row itself); 'Wilsons Wharf Fort Powhattan Kautz flag of truce' hit 4601 (second telegram). Not located in print for this telegram (letters-only phrase grep, 191 cached volumes: 'W. W. Shore is in Baltimore somewhere', 'I want him caught and arrested and sent to me under guard', 'he is the correspondent of the World from Baltimore as he was from here', 'arrest him since which we have heard nothing', 'can send you if necessary a man who knows him': none)."),
}
txt = (HERE.parent/"ciphertext.txt").read_text(encoding="utf-8")
body = {}; cur = None
for ln in (HERE/"fmund_entries.txt").read_text(encoding="utf-8").splitlines():
    if ln.startswith("### "): cur = ln.split("|")[0][4:].strip(); body[cur] = []; continue
    if cur and ln.strip(): body[cur].append(ln)
b4 = body["U4"]; k = [i for i, l in enumerate(b4) if l.startswith("May 6th")][0]; body["U4"] = b4[:k]
add = ""
for F, (eid, page, desc, note) in SPEC.items():
    if f"### {eid} |" in txt: continue
    ptr = re.search(r"pointer (\d+)", desc).group(1)
    whole = ", on the whole row, both telegrams" if F == "U4" else ""
    add += f"### {eid} | {page} | {ptr} | {desc}\n" + "\n".join(body[F] + ["note: " + BASE + s0(F, whole) + note]) + "\n\n"
if "--dry" in sys.argv: print(add)
elif add: (HERE.parent/"ciphertext.txt").write_text(txt.rstrip("\n") + "\n\n" + add.rstrip("\n") + "\n", encoding="utf-8")
