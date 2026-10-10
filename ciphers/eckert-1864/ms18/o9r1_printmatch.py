#!/usr/bin/env python3
"""O9R-1 (10 Oct 2026): print-match instrument for the four O9R-1 rows that are in print (G2 9808/2, G7 9803/0, G10 9735/0, G11 9686/1).
Statistic: of the word-kind code tokens a book resolves in the ledger entry, how many have a meaning whose content words all occur in the printed item's own text?
Compared: No. 1, No. 2, No. 9, and 20 meaning-shuffled copies of No. 9 (seeds 1-20; same code words, values permuted among word rows). The statistic can differ between target and
control (a shuffle moves the values, not the printed text). Printed texts: OR I/37 pt 2 pp.590, 471; I/37 pt 1 p.414; I/34 pt 2 p.602 (OCR, hand-normalised)."""
import random, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); import decode
PRINT = {
 "G2": "Washington, August 3, 1864. Major-General Couch, Pittsburg, Pa.: As a new raid may immediately follow, and be directed toward Pittsburg, the instructions in regard to blocking up the roads leading from the Cumberland Valley should be carried out. A space could be left in the barriers for teams to pass through, and means to close it, in case of danger. The town and county authorities should do this for their own protection. I will endeavor to send you some engineer officers to assist in this matter. H. W. Halleck, Major-General and Chief of Staff.",
 "G7": "Washington, July 27, 1864 - 9 p. m. Brigadier-General Kelley, Cumberland, Md.: With your railroad facilities you should be able to concentrate nearly all your force on any threatened point. You will be expected to make your arrangements to accomplish this object. H. W. Halleck, Major-General and Chief of Staff.",
 "G10": "Washington, D. C., May 9, 1864 - 10.05 a. m. Brigadier-General Kelley, Cumberland: You remain under General Sigel's orders. Report directly when you have any important information to convey. Three regiments of Ohio militia were ordered to Parkersburg, three to New Creek, three to Cumberland, and three to Harper's Ferry. You can distribute them as you deem best. H. W. Halleck, Major-General and Chief of Staff.",
 "G11": "Washington, D. C., March 14, 1864 - 10.30 p. m. Major-General Steele, Little Rock, Ark.: You command all troops found within the limits of your department when the order establishing it was received. You will arrest any officer within your department who interferes with your authority in this respect. H. W. Halleck, General-in-Chief.",
}
EXP = {"maj": "major", "gen": "general", "genl": "general", "brig": "brigadier", "sec": "secretary", "lieut": "lieutenant", "col": "colonel", "capt": "captain", "mil": "militia"}
STOP = {"of", "the", "a", "an", "to", "in", "and", "or", "is", "be"}
def words(s): return [EXP.get(w, w) for w in re.findall(r"[a-z]+", re.sub(r"\(.*?\)", " ", s.lower()))]
keys = {n: decode.load_key(HERE/f) for n, f in [("no1","key.md"),("no2","key-no2.md"),("no9","key-no9.md")]}
def shuffled(key, seed):
    rows = [k for k, v in key.items() if v[2] == "word"]; m = [key[k] for k in rows]; random.Random(seed).shuffle(m)
    out = dict(key); out.update(zip(rows, m)); return out
def stat(text, key, pw):
    toks = []; decode.decode_entry(text, key, tokens=toks)
    wk = [t for t in toks if t[4] == "word"]
    hit = sum(1 for t in wk if (ws := [w for w in words(t[2]) if w not in STOP]) and all(w in pw for w in ws))
    return hit, len(wk)
print("row\tbook\tmatch/word-tokens")
ents = {h.split("|")[0].strip(): decode.entry_text(l) for h, l in decode.load_ciphertext(HERE/"ms18"/"o9r1_entries.txt")}
for r, ptxt in PRINT.items():
    pw = set(words(ptxt)); text = ents[r]
    res = {n: stat(text, k, pw) for n, k in keys.items()}
    sh = [stat(text, shuffled(keys["no9"], s), pw)[0] for s in range(1, 21)]
    print(f"{r}\tno1 {res['no1'][0]}/{res['no1'][1]}\tno2 {res['no2'][0]}/{res['no2'][1]}\tno9 {res['no9'][0]}/{res['no9'][1]}\tshuffled no9: max {max(sh)} p95 {sorted(sh)[18]} mean {sum(sh)/20:.2f} (20 seeds)")
