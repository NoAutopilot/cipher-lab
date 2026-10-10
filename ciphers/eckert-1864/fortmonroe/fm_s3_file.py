#!/usr/bin/env python3
"""FM-S3 (10 Oct 2026): file six rows of fm_s3_entries.txt: F5 E471, F12 E472, F14 E473, F18 E474 into ../ciphertext.txt (Cipher No. 1) and
F2 O9-DL, F4 O9-DM into ../ciphertext-no9.txt (Cipher No. 9, old vocabulary). Transcription only (no image check). Usage: fm_s3_file.py [--dry]. Idempotent."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; T = HERE.parent
S0 = "FM-S3 Step 0 (fm_s3_step0.py, run under No. 1; as information, a hit on mssEC 25 is a non-test): "
def blocks():
    cur = None; out = {}
    for ln in (HERE/"fm_s3_entries.txt").read_text(encoding="utf-8").splitlines():
        if ln.startswith("### "): cur = ln.split("|")[0].replace("###", "").strip(); out[cur] = []; continue
        if cur and ln.strip(): out[cur].append(ln)
    return out
B = blocks()
J = [
 ("ciphertext.txt", "E471", "F5", "Page 33 | 5577 | mssEC 25 (obj 5952, pointer 5577), 3 Mar 1864 Ft Monroe, Sheldon to Maj. Eckert, Washington: number 1 cipher received today; send no ciphers till the cable is repaired; nothing heard from Kilpatrick (kill pat trick, plain) up to 1 PM today (FM-S3; row 5577/0; transcription only)",
  [S0 + "(a) 0.810 (17/21), (b) p95 0.333, HIT (shuffled-key copy 0.810 HIT). No. 1 H8: plunge = 1, Pembroke = Cipher, penfields = Ciphers, Wedge = today (all H, M for the sense of the numeral-and-time words); the rest is plain. Not located in print (phrase grep over 177 cached volumes; no be-api run), Huntington CISOSEARCHALL 'cable repaired Patrick': 0 hits. Short: the code words carry only noun and number words."]),
 ("ciphertext.txt", "E472", "F12", "Page 135 | 5679 | mssEC 25 (obj 5952, pointer 5679), 20 May 1864 1.30 PM Ft Monroe, Sheldon to the Quartermaster General (Meigs), Washington: has Sheridan left the James; must we forage him by the other line (FM-S3; row 5679/0; transcription only)",
  [S0 + "(a) 0.533 (8/15), (b) p95 0.333, HIT (shuffled-key copy 0.533 HIT). No. 1 H12: Sheriden, Left, James, Forage, Colonel/Monroe, Qr Master Genl. Sense is the check (Sheridan's raid, May 1864), M for the addressee and the sign-off. Holder CISOSEARCHALL 'Sheridan Forage James': 1 hit, pointer 4642 (20 May 1864, Ft Monroe to QM Gen: Sheridan at White House wants ponton train, rations, forage): a different telegram on the same subject and day, not a copy. Not located in print (grep over 177 volumes: 'by the other line' occurs only in a 6 Oct 1864 Halleck dispatch, rejected)."]),
 ("ciphertext.txt", "E473", "F14", "Page 89 | 5633 | mssEC 25 (obj 5952, pointer 5633), 26 Apr 1864 Ft Monroe, Sheldon to R. O'Brien at Norfolk, for Captain Clark: [new regime, Edgar's name]; why [publish] Edgar's name; stop your exchanges, this was against orders [Butler] (FM-S3; row 5633/1; transcription only)",
  [S0 + "(a) 0.700 (14/20), (b) p95 0.350, HIT (shuffled-key copy 0.560 HIT). No. 1 H7 but the Norfolk, Butler and number words are M; the clause 'stop your exchanges, this was against orders' is plain. No. 2 reads Knox = Butler (H4, C1); the book is chosen by sense, not by share. Holder CISOSEARCHALL 'Exchanges against orders Clark Norfolk': own pointer only. Not located in print (grep over 177 volumes: none)."]),
 ("ciphertext.txt", "E474", "F18", "Page 285 | 5829 | mssEC 25 (obj 5952, pointer 5829), 13 Dec 1864 City Point, Ingalls (chief quartermaster) via S. H. Beckwith to Sheldon at Ft Monroe, for Col. Webster (chief QM Fort Monroe): has General Butler's fleet left yet; the question E278 (5829/2, same page, Webster's reply of 1 PM: most of the fleet left during last night) answers (FM-S3; row 5829/1; transcription only)",
  [S0 + "(a) 0.667 (6/9), (b) p95 0.444, HIT (shuffled-key copy 0.750 HIT). No. 1 H8; the first clause (Frances fever paradise arsey) is M ('New York's 13 Colonel' does not read; the address to Webster is plain). Sense support is the sibling E278 on the same page, not the key. Holder CISOSEARCHALL 'Ingalls Webster fleet': own pointer only. Not located in print (grep over 177 volumes: none)."]),
 ("ciphertext-no9.txt", "O9-DL", "F2", "Page 3 | 5547 | mssEC 25 (obj 5952, pointer 5547), 3 Feb 1864 New York, J. J. Peck (Syracuse) via Horner to Sheldon at Ft Monroe, for B. F. Butler, Fort Monroe: yours received; I await your orders by telegraph; will leave at once if you deem it necessary; have written you (FM-S3; row 5547/1; old vocabulary; transcription only)",
  [S0 + "(a) 0.739 (17/23), (b) p95 0.304, HIT under No. 1 (No. 1 reads Audit as Rapidan and gives no sense). Book: No. 9 (Audit = B. F. Butler, Hammock = (Fort) Monroe, Vernon = Maj. Gen., all H; the shares picked No. 2, sense picks No. 9, the same Feb 1864 'Audit' address as the unfiled sibling 5569/1 and O9-DM (5546/0)). Holder CISOSEARCHALL 'Peck Syracuse Horner': 2 hits, own pointer and 4424 (not opened). Not located in print (grep over 177 volumes: 'J J Peck' occurs in other dispatches, rejected)."]),
 ("ciphertext-no9.txt", "O9-DM", "F4", "Page 2 | 5546 | mssEC 25 (obj 5952, pointer 5546), 3 Feb 1864 Washington, Eckert to Sheldon, for B. F. Butler: telegraph directly to Maj. Gen. [Hedge Wick, a pun on Sedgwick, M] now in command of the Army of the Potomac in regard to any cooperation; signed by Halleck's word (applause, M) (FM-S3; row 5546/0; old vocabulary; transcription only)",
  [S0 + "(a) 0.550 (11/20), (b) p95 0.300, HIT under No. 1 (No. 1 reads Audit as Rapidan; no sense). Book: No. 9 (Audit = B. F. Butler, supper = Telegraphs, Vernon = Maj. Gen., Walpole = Army, gem = Potomac, applause = Halleck: H7). 'Hedge Wick' is not a key row (M, pun reading Sedgwick, who commanded the Army of the Potomac during Meade's absence of early Feb 1864 only if the date holds: not checked). Holder CISOSEARCHALL 'cooper ration': 14 hits, own pointer plus 13 others not opened. Not located in print (grep over 177 volumes: none for the phrases)."]),
]
dry = "--dry" in sys.argv; texts = {}
for fn, eid, fid, desc, notes in J:
    f = T/fn; texts.setdefault(fn, f.read_text(encoding="utf-8"))
    if f"### {eid} |" in texts[fn]: print("already present", eid); continue
    add = f"### {eid} | {desc}\n" + "\n".join(B[fid] + ["note: " + n for n in notes]) + "\n"
    texts[fn] = texts[fn].rstrip("\n") + "\n\n" + add
    print(("would add " if dry else "added ") + eid)
if not dry:
    for fn, t in texts.items(): (T/fn).write_text(t, encoding="utf-8")
