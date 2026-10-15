#!/usr/bin/env python3
"""WVO 153 (Oranje to August, 1 Sept 1566), p6 (f.4) cipher postscript, lines 1-20 (1-9 WVO-153-KEY-2, 10 Oct 2026; 10-20 AVS-153, 15 Oct 2026): the worker's reconciliation of
two blind Sonnet passes per band (band 1 = lines 1-3, bands 2-3 = lines 4-9) against the 2x line crops, aligned by hand to
the two contemporary decipherments on p7 (f.5, witness W1) and p8 (f.6, witness W2). Writes ../ciphertext_153.tsv and
../key_153.tsv; --check exits 1 if either committed file is stale (CLAUDE.md rule 7).

Sign classes are this letter's own labels (pass B's shape distinctions, which pass A's 'vb' label did not make):
  digits 0-9 as written; TH = barred oval (theta); L = plain inverted V; Lm = inverted V with an inner bar/hook;
  v = open cup; vb = cup closed by a bar across its top; V = narrow pointed v (line 4 only); d = plain d; dT = d with a
  very tall stem; dD = tall d crossed near the top (dagger); q = loop on a straight stem (no crossbar); g = loop on a stem
  crossed at the foot; phi = circle with a vertical stroke; c = open c-shape; st = barred z / 7 with a ball (S7);
  Zb = barred x/z (line 4 pos 1); S = capital S (line 1 'zu'); 5z = an s-like/5-like sign standing for 'zu' (passes
  read 5); Q, B, M, K = word signs; C16 = the dotted numeral group '.16.'; Zh, Me = the code group read over
  'Stadt Antorff' (line 5); '.' = a dot on the line (no value). Added by AVS-153 (lines 10-20): Ce = epsilon/C-like
  word sign for 'das' (pass A 'c', pass B 'e'; not compared with line 1's 'c' by eye); R = word sign 'E.L.' (Euer Liebden);
  X = x-shape 'y'; 6f = 6 with a long flag (values split s/sch). AVS-W1 (15 Oct 2026): lines 2 and 6's '6~' relabelled 6f
  (sch, M); line 18's extra 6f valued s from W1 'Christlichs' (M).
Token value (u and v normalised to u, as the period writes them) = the letter(s) of the witness text aligned to it (both witnesses agree word for word in lines 1-9 except
where noted). Grade C = aligned to the period decipherment with the passes agreeing on the class; M = the passes split on
the class, the cipher spelling differs from both witnesses, or the class carries more than one value. '-' = no value.
"""
import collections, csv, io, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_CT = HERE.parent / "ciphertext_153.tsv"
OUT_KEY = HERE.parent / "key_153.tsv"

# one string per cipher line: tokens 'class:value' or 'class:value:M' (M = held, with the reason in NOTES), '|' = gap
LINES = {
 1: "3:e 6:s 2:i st:st | 0:a vb:b 3:e TH:r | S:zu .:- | 3:e TH:r vb:b c:a:M TH:r Lm:m 3:e v:n | Q:das | B:der | "
    "dT:c 0:a L:l 5:u:M 2:i v:n 2:i 6:s Lm:m 5:u 6:s | 6:s 4:o | 8:w 3:e 2:i 9:t 9:t",
 2: "3:e 2:i v:n TH:r 3:e 2:i 6:s 6:s 3:e 9:t .:- M:und K:die 0:a 5:u g:g 6:s phi:p 5:u TH:r g:g 2:i 6f:sch:M 3:e | "
    "dT:c 4:o v:n q:f 3:e 6:s 6:s 2:i 4:o v:n | 5:u vb:b 3:e TH:r",
 3: "8:w 0:a d:c 1:h 6:s 6:s 3:e 9:t | dD:d 0:a v:n | 2:i v:n | 0:a L:l L:l 3:e v:n | dD:d 2:i 3:e 6:s 6:s 3:e v:n | "
    "L:l 0:a v:n dD:d 3:e v:n | 6:s:M 3:e 2:i v:n 9:t | v:n 5:u 1:-:M TH:r",
 4: "Zb:z:M 8:w 4:o | V:k 2:i TH:r dT:c 1:h 3:e v:n | B:der | 0:a 5:u g:g 6:s phi:p:M 5:u TH:r g:g 2:i 6:-:M 3:e v:n | "
    "dT:c 4:o v:n q:f:M 3:e 6:s 6:s 2:i 4:o v:n | M:und K:die | 8:w 3:e TH:r:M dD:d:M 3:e v:n",
 5: "2:i v:n dD:d 2:i 3:e 6:s 6:s 3:e TH:r | Zh:-:M Me:-:M e:-:M | 3:e TH:r 1:h 0:a L:l 9:t 3:e v:n | B:der | "
    "0:a v:n dD:d 3:e TH:r | 1:h 0:a 5:u q:f q:f | 2:i st:st:M | dD:d 5:u TH:r dT:c 1:h 0:a 5:u 6:s 6:-:M",
 6: "dT:c 0:a L:l 5:u 2:i v:n 2:i 6f:sch:M | dD:d 0:a TH:r 5:u Lm:m:M vb:b | st:st 1:h 3:e 9:t | 5z:zu:M | "
    "vb:b 3:e 6:s 4:o TH:r g:g 3:e v:n | B:der | C16:Konig_zu_Hispania:M | 8:w 3:e TH:r dD:d 3:e | 5z:zu:M",
 7: "3:e v:n dD:d:M 3:e TH:r 5:u v:n g:g | B:der | TH:r 3:e L:l L:-:M 2:i g:g 2:i 4:o v:n | "
    "8:w 3:e v:n 2:i g:g 3:-:M TH:-:M | 5:u 3:e TH:r 6:s 1:h 3:e v:n | M:und | Lm:m:M 2:i 9:t 9:t",
 8: "TH:r 0:a 9:t 1:h | M:und | 5z:zu:M 9:t 1:h 5:u v:n | 5:u v:n TH:r 5:u g:-:M 2:i 1:-:M 3:e TH:r | "
    "L:l 3:e 5:u 9:t 1:-:M | 2:i 1:h TH:r 3:e | 0:a L:l 9:t 3:e | TH:r 3:e L:l L:-:M 2:i g:g 2:i 4:o v:n",
 9: "Lm:m:M 2:i 9:t 9:t | g:g 2:-:M 8:w 0:a L:l 9:t | 3:e TH:r 1:h 0:a L:l 9:t 3:e v:n | M:und | dD:d 2:i 3:e | "
    "0:a v:n dD:d 3:e TH:r v:n | 5:u 3:e TH:r 5:-:M 4:o L:l g:g 3:e v:n",
 10: "8:w 4:o L:l L:l 3:e v:n | dD:d 0:a TH:r 0:a 5:u 6:s 6:s | dD:d 0:a v:n | 3:e 2:i v:n | g:g TH:r 4:o 6:s 6:s .:- | "
     "vb:b L:l 5:u 3:-:M 9:t | 5:u 3:e TH:r g:g 2:i 3:e 6:s 6:s 3:e v:n",
 11: "3:e TH:r 5:u 4:o L:l g:g 3:e v:n | 8:w 5:u TH:r dD:d 3:e .:- | dD:d 3:e TH:r 8:w 3:e g:g 3:e v:n | 9:-:M 1:h 4:o dT:c 1:h | "
     "5:u 4:o v:n v:n 4:o 9:t 1:h 3:e v:n | M:und",
 12: "g:g 5:u 3:-:M 9:t | Ce:das .:- | R:E.L. | M:und | 0:a v:n dD:d 3:e TH:r | dT:c 1:h 5:u TH:r | M:und | q:f 5:u TH:r st:st 3:e v:n | "
     "5:-:M 2:i dT:c 1:h | dD:d 2:i 3:e 6:s 6:-:M 3:e TH:r | 6:s 0:a dT:c 1:h 3:e v:n",
 13: "Lm:m:M 2:i 9:t | 0:a v:n v:n 1:-:M 3:-:M Lm:m:M 3:e v:n | M:und | vb:b 3:e X:y Lm:m:M | C16:Konig_zu_Hispania | "
     "dD:d 0:a 1:h 2:i 3:-:M v:n | 1:h 0:a v:n dD:d L:l 3:e v:n | 1:h 5:-:M L:l q:f q:f 3:e v:n",
 14: "Ce:das 3:e TH:r | dD:d 2:i 3:e | g:g 3:e L:l 3:e g:g 3:e v:n 1:h 3:e 2:i 9:t | vb:b 3:e dD:d 3:e v:n d:c V:k 3:e v:n | M:und | "
     "6f:s:M 3:e 2:i v:n 3:e | g:g 3:e 1:h 4:o TH:r",
 15: "6:s 0:a Lm:m:M 3:e | 5:u v:n dD:-:M 3:e TH:r 9:t 1:h 0:a v:n 3:e | 1:h 2:i 3:e .:- | Lm:m:M 2:i 9:t:M | "
     "5:u 3:e TH:r 6f:sch:M 4:o v:n 3:e v:n | M:und | B:der | TH:r 3:e L:l L:-:M 2:i",
 16: "g:g 2:i 4:o v:n | 1:h 0:a L:l vb:b 3:e v:n | 8:w 2:i 3:-:M dD:d 3:e TH:r | 6:s 2:i 3:e | Lm:m:M 2:i 9:t | "
     "g:g 3:e 8:w 0:a L:l dD:-:M 9:t | v:n 2:i dT:c 1:h 9:t Zb:-:M",
 17: "5:u 4:o TH:r v:n 1:-:M 3:-:M Lm:m:M 3:e v:n | 8:w 4:o L:l L:-:M 3:e .:- .:- | 1:h 2:i 3:e TH:r 0:a v:n | "
     "8:w 3:e TH:r dD:d 3:e v:n | R:E.L. | 4:o 1:h v:n",
 18: "Zb:z 8:w 3:e 2:i q:f q:-:M 3:e L:l | 3:e 2:i v:n | d:c 1:h TH:r 2:i st:st L:l 2:i dT:c 1:h 6f:s:M | 8:w 3:e TH:r dT:c V:k | "
     "5:u 3:e TH:r TH:r 2:i dT:c 1:h 9:t 3:e v:n",
 19: "M:und .:- | vb:b 3:e X:y | dD:d 2:i 3:e 6:s 6:-:M 3:e v:n | L:l 0:a v:n dD:d 3:e v:n | 3:e 2:i v:n | 3:e 8:w 2:i g:g 3:e 6f:s:M | "
     "L:l 4:o vb:b | 3:e TH:r",
 20: "L:l 0:a v:n g:g 3:e v:n",
}
NOTE = {
 (1, "c"): "erbarmen: open c over a; passes split (c+/c,plus)", (1, "5"): "calvinismus: s-like small sign, passes S/s; 5 = u/v",
 (2, "6f"): "augspurgis(ch)e: pass A 6~; AVS-W1 (PREREG-AVS-W1 rule 2, worker eye, not blind): the long-flag 6 of 6f, value sch, M", (3, "6"): "seint: 6 with a mark above (6~)",
 (3, "1"): "nur: cipher 'nuhr'", (4, "Zb"): "zwo: barred x/z, passes X/Z+", (4, "phi"): "pass B Qc",
 (4, "q"): "confession: both passes read 9 (q-shape vs 9 not settled)", (4, "TH"): "werden: pass B 'e' (small theta)",
 (4, "dD"): "werden: A dT, B DX", (5, "Zh"): "'Stadt Antorff' code group, 3 signs (Z#, M, e), not assigned",
 (5, "st"): "ist: 7 with a ball (S7)", (5, "6"): "durchaus + one 6 more than the witness",
 (6, "6f"): "Caluinis(ch): pass A 6~; AVS-W1 (PREREG-AVS-W1 rule 2): the long-flag 6 of 6f, value sch, M", (6, "Lm"): "darumb: pass B A (plain)", (6, "5z"): "zu: read 5 by both passes",
 (6, "C16"): "'.16.' over 'Konig zu Hispania'", (7, "dD"): "enderung: A dT, B DL (no cross seen)",
 (7, "L"): "cipher 'Relligion'", (7, "3"): "cipher 'weniger', W1 'wenig', W2 omits", (7, "Lm"): "mitt: both passes A/L",
 (8, "g"): "cipher 'vnrugiher' (h/g swapped vs witness)", (8, "1"): "cipher 'leuth ihre', W2 'leute jre'",
 (8, "L"): "cipher 'Relligion'", (9, "Lm"): "mitt: pass B Ab", (9, "2"): "gewalt: cipher 2 (i) where e",
 (9, "5"): "vervolgen: s-like 5 over f (u/v sign); witness 'verfolgen'",
 (10, "3"): "cipher 'bluet', W2 'bluth' (e extra, h missing)", (11, "9"): "cipher '9 hoch' (t before hoch), W2 'hoch'",
 (12, "3"): "cipher 'guet', W2 'guth'", (12, "5"): "sich: s-like sign read 5 by pass A, S by pass B; 5 = u elsewhere, value withheld",
 (12, "6"): "cipher 'diesser', W2 'dieser'", (13, "Lm"): "m written as a plain inverted V (passes L); hook not seen",
 (13, "1"): "cipher 'annhemen', W2 'annehmen' (e/h swapped)", (13, "3"): "e/h swap (annhemen) or cipher 'dahien' vs W2 'dahin'",
 (13, "5"): "cipher 'hulffen', W2 'helffen'", (14, "6f"): "seine: 6 with a flag (pass A vb, pass B S)",
 (15, "Lm"): "m as plain inverted V", (15, "dD"): "cipher 'vnderthane', W2 'vnterthanen'", (15, "9"): "mit: y-like 9 (A 4, B y)",
 (15, "6f"): "verschonen: wide 6 with a long flag over 'sch' (the '6~' of augspurgis(ch)e / Caluinis(ch), lines 2 and 6?)",
 (15, "L"): "cipher 'Relligion'", (16, "3"): "cipher 'wieder', W2 'wider'", (16, "Lm"): "mit: plain inverted V",
 (16, "dD"): "cipher 'gewaldt', W2 'gewalt'", (16, "Zb"): "cipher 'nichtz' (barred x = z), W2 'nichts'",
 (17, "1"): "cipher 'vornhemen', W2 'vornehmen'", (17, "3"): "e/h swap (vornhemen)", (17, "Lm"): "m as plain inverted V",
 (17, "L"): "cipher 'wolle', W2 'wolte'", (18, "q"): "cipher 'zweiffel', W2 'zweifel'",
 (18, "6f"): "christlich + a small flagged 6, W2 'Christlich', W1 'Christlichs' (AVS-W1, PREREG rule 1c: value s; class 6f split s/sch, so M)", (19, "6"): "cipher 'diessen', W2 'diesen'",
 (19, "6f"): "ewiges: the long-flag 6 over s",
}


def tokens():
    for ln in sorted(LINES):
        pos = 0
        for t in LINES[ln].split():
            if t == "|":
                continue
            pos += 1
            parts = t.split(":")
            cls, val = parts[0], parts[1]
            g = "M" if len(parts) > 2 or val == "-" else "C"
            if cls == ".":
                g = "-"
            yield ln, pos, cls, val, g


def build():
    rows = list(tokens())
    ct = io.StringIO()
    ct.write("page\tline\tpos\tsign\tvalue\tgrade\tnote\n")
    ct.write("# WVO 153 p6 (f.4) cipher lines 1-20 (10-20 added by AVS-153, 15 Oct 2026), reconciled from two blind passes per band (w153/recon_153.py); "
             "value = the witness letter(s) aligned to the token (W1 p7/f.5, W2 p8/f.6). WVO-153-KEY-2, 10 Oct 2026.\n")
    for ln, pos, cls, val, g in rows:
        note = NOTE.get((ln, cls), "") if g == "M" else ""
        ct.write(f"p6\t{ln}\t{pos}\t{cls}\t{val}\t{g}\t{note}\n")
    byc = collections.defaultdict(collections.Counter)
    for ln, pos, cls, val, g in rows:
        if cls != "." and val != "-":
            byc[cls][val] += 1
    key = io.StringIO()
    key.write("sign\tvalue\tcount\tgrade\tnote\n")
    key.write("# WVO 153 (Oranje -> August, 1 Sept 1566) p6 lines 1-20 (10-20 AVS-153, 15 Oct 2026): sign class -> value from the two period decipherments "
              "(p7/f.5, p8/f.6). A `period` key rebuilt by WVO-153-KEY-2 (account 4, 10 Oct 2026), w153/recon_153.py. C = every "
              "aligned token gives this value; M = values split, one token only under a held reading, or a code group.\n")
    for cls in sorted(byc, key=lambda c: (-sum(byc[c].values()), c)):
        cnt = byc[cls]
        top, n = cnt.most_common(1)[0]
        tot = sum(cnt.values())
        clean = sum(1 for r in rows if r[2] == cls and r[4] == "C")
        grade = "C" if len(cnt) == 1 and clean >= 1 else "M"
        val = top if len(cnt) == 1 else "|".join(v for v, _ in cnt.most_common())
        note = "n=%d %s" % (tot, ",".join(f"{v}:{c}" for v, c in cnt.most_common()))
        key.write(f"{cls}\t{val}\t{tot}\t{grade}\t{note}\n")
    return ct.getvalue(), key.getvalue(), rows


def main():
    ct, key, rows = build()
    if "--check" in sys.argv:
        stale = [p.name for p, s in ((OUT_CT, ct), (OUT_KEY, key)) if not p.exists() or p.read_text() != s]
        if stale:
            print("STALE:", ", ".join(stale)); sys.exit(1)
        print("check OK: ciphertext_153.tsv and key_153.tsv up to date")
        return
    OUT_CT.write_text(ct); OUT_KEY.write_text(key)
    g = collections.Counter(r[4] for r in rows if r[2] != ".")
    print(f"wrote {OUT_CT.name} ({sum(g.values())} signs: {dict(g)}) and {OUT_KEY.name}")


if __name__ == "__main__":
    main()
