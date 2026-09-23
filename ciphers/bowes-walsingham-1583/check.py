#!/usr/bin/env python3
"""Regenerate the Bowes 1583 reading from ciphertext.txt + key.tsv (rule 7), 23 Sept 2026.

  python3 check.py           compare with the committed reading.tsv; exit 1 if stale or missing
  python3 check.py --write   rewrite reading.tsv

Per token: fragment, position, sign, key value, grade, and the Letter-Book word it sits in (parallel text,
Surtees Soc. vol.14, 1842). Three tokens are graded I: the key gives a letter the parallel word does not have
(listed in REPAIRS, never applied silently; the decoded letter is printed as the key gives it).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))

# (fragment, 0-based position): (letter the parallel word expects, note)
REPAIRS = {
    (1, 6): ("r", "key gives n (sign 11); 'Sir Henry Cobham' expects r: Henri read as Henni"),
    (3, 1): ("", "sign 18 (c) between the g-sign and 'lencarne'; not in 'Glencarne'; slip or misread"),
    (4, 9): ("u", "key gives r (sign 06); 'Huntley' expects u"),
}
# word segmentation of each fragment as read (letters of the decoded text; '?' = unread sign)
WORDS = {
    1: [("sir henri cobham", 14, "CLXXXVII: 'Sir Henry Cobham with 870 and Smallet'")],
    2: [("smallet", 7, "CLXXXVII: 'Smallet' (first mention)")],
    3: [("glencarne", 10, "CLXXXVII: 'credit by and with Glencarne'")],
    4: [("magnyuil huntley ? glencarne ?", 26, "CLXXXVII: 'Manningvile, Huntley, Glencarne, and Montrosse'")],
    5: [("?", 1, "code sign; CLXXXVII next has '870' (not verified)")],
    6: [("mauuissier", 10, "CLXXXVII: 'offer himself to Mauvisier'")],
    7: [("smallet", 7, "CLXXXVII: 'return of Smallet' (second mention, printed 'Smaller')")],
    8: [("? glencarn", 9, "CCXL: 'This day Glencarne and 223'")],
    9: [("his ruthen", 9, "CCXL: 'at Ruthen on his person' / 'his fault at Ruthen'")],
    10: [("? ? ?", 3, "unread; pattern AAB fits the code number 223 of CCXL (not verified)")],
    11: [("? ? him", 5, "unread; last three signs decode to h i m")],
}


def load():
    frags = [[t for t in l.strip().split(";") if t] for l in open(os.path.join(HERE, "ciphertext.txt"))
             if l.strip() and not l.startswith("#")]
    key = {}
    for l in open(os.path.join(HERE, "key.tsv")):
        if l.startswith("#") or l.startswith("sign\t") or not l.strip():
            continue
        s, v, g, _ = l.rstrip("\n").split("\t", 3)
        key[s] = (v, g)
    return frags, key


def render():
    frags, key = load()
    out = ["fragment\tpos\tsign\tvalue\tgrade\tnote"]
    lines, counts = [], {"S": 0, "M": 0, "I": 0, "-": 0}
    for fi, f in enumerate(frags, 1):
        dec = ""
        for pi, s in enumerate(f):
            v, g = key[s]
            note = ""
            if (fi, pi) in REPAIRS:
                g, note = "I", REPAIRS[(fi, pi)][1]
            counts[g] += 1
            dec += v
            out.append(f"F{fi}\t{pi+1}\t{s}\t{v}\t{g}\t{note}")
        w = WORDS[fi][0]
        lines.append(f"#F{fi}\t{dec}\t{w[0]}\t{w[2]}")
    return "\n".join(out + ["#fragment\tdecoded (key only)\tas read\tparallel Letter-Book text"] + lines +
                     [f"#grades\tS {counts['S']}\tM {counts['M']}\tI {counts['I']}\tH 0\tC 0\tunread {counts['-']}\ttotal {sum(counts.values())}"]) + "\n"


if __name__ == "__main__":
    head = "".join(l for l in open(os.path.join(HERE, "reading.tsv")) if l.startswith("# ")) if os.path.exists(os.path.join(HERE, "reading.tsv")) else ""
    new = head + render()
    path = os.path.join(HERE, "reading.tsv")
    if "--write" in sys.argv:
        open(path, "w").write(new); print(new.split("\n#fragment")[1]); sys.exit(0)
    old = open(path).read() if os.path.exists(path) else ""
    if old != new:
        print("STALE: reading.tsv does not match ciphertext.txt + key.tsv; run check.py --write and review", file=sys.stderr)
        sys.exit(1)
    print("OK: reading.tsv regenerates from ciphertext.txt + key.tsv"); sys.exit(0)
