#!/usr/bin/env python3
"""Regenerate the Bowes 1583 reading from ciphertext.txt + key.tsv (rule 7), 23 Sept 2026.

  python3 check.py           compare with the committed reading.tsv; exit 1 if stale or missing
  python3 check.py --write   rewrite reading.tsv

Per token: fragment, position, sign, key value, grade, and the Letter-Book word it sits in (parallel text,
Surtees Soc. vol.14, 1842). Three tokens are graded I: the key gives a letter the parallel word does not have
(listed in REPAIRS, never applied silently; the decoded letter is printed as the key gives it).

2 Oct 2026 (NEXT-BOW): Tomokiyo's manuscript check of 24 Sept 2026 (NOTES "Specialist reply") says the token at
F4 pos.26 (his sign 27) is a handwritten 'and' abbreviation, not a cipher sign. ciphertext.txt stays as he
transcribed it (rule 2: never silently repaired); EXCLUDED lists the token, it is printed with value 'and' and
grade '-' and counted apart, so the cipher-token total is 100, not 101. CSP Scotland vi (Boyd 1910) no.584
pp.566-568 (Google Books search-within snippets, NOTES step of 2 Oct 2026) prints an asterisk where the Cotton
original has a cipher word, so the Letter-Book word at each asterisk is the plaintext of that cipher word at a
matched position: F9 ('by * late submission at *' = 'his', 'Ruthen') is graded C from that (CALENDAR_C). F10 sits at
Boyd's 'In this *' where the Letter-Book has '223' and reads as cipher digit-signs 2 2 3 at grade M (key.tsv 02, 03);
F8 sits at Boyd's 'This day --* and "223"' (Letter-Book 'Glencarne') with its leading sign 15 still unread; F11's
03 takes the same value 3 at M and 25 stays unread. See NOTES step of 2 Oct 2026 and align_ccxl.py.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))

# (fragment, 0-based position): (letter the parallel word expects, note)
REPAIRS = {
    (1, 6): ("r", "key gives n (sign 11); 'Sir Henry Cobham' expects r: Henri read as Henni"),
    (3, 1): ("", "sign 18 (c) between the g-sign and 'lencarne'; not in 'Glencarne'; slip or misread"),
    (4, 9): ("u", "key gives r (sign 06); 'Huntley' expects u"),
}
# (fragment, 0-based position): note -- tokens Tomokiyo transcribed that are not cipher signs; excluded from the count
EXCLUDED = {
    (4, 25): ("and", "handwritten 'and' abbreviation, not a cipher sign (Tomokiyo's manuscript check, 24 Sept 2026)"),
}
# fragment: (note) -- every token of the fragment is graded C: Boyd's calendar of the Cotton original (CSP Scotland
# vi no.584, pp.567) prints an asterisk 'In cipher' exactly where the Letter-Book copy (Surtees CCXL) has the word
CALENDAR_C = {
    9: "Boyd p.567 'done by * late submission at *' = Letter-Book CCXL 'by his late submission at Ruthen': his + Ruthen (both copies a3ZZTPid3VQC, 414MAQAAIAAJ)",
}
# word segmentation of each fragment as read (letters of the decoded text; '?' = unread sign)
WORDS = {
    1: [("sir henri cobham", 14, "CLXXXVII: 'Sir Henry Cobham with 870 and Smallet'")],
    2: [("smallet", 7, "CLXXXVII: 'Smallet' (first mention)")],
    3: [("glencarne", 10, "CLXXXVII: 'credit by and with Glencarne'")],
    4: [("magnyuil huntley ? glencarne and", 26, "CLXXXVII: 'Manningvile, Huntley, Glencarne, and Montrosse'; MS MAGNYVIL, 'and' an abbreviation, Montrosse = code 189 (C) in the MS (Tomokiyo, 24 Sept 2026)")],
    5: [("?", 1, "code sign; CLXXXVII next has '870' (not verified)")],
    6: [("mauuissier", 10, "CLXXXVII: 'offer himself to Mauvisier'")],
    7: [("smallet", 7, "CLXXXVII: 'return of Smallet' (second mention, printed 'Smaller')")],
    8: [("? glencarn", 9, "CCXL: 'This day Glencarne and 223' = Boyd p.566 'This day --* and \"223\" have given him understanding': the name is the cipher word, 223 a plain numeral there; sign 15 unread")],
    9: [("his ruthen", 9, "CCXL: 'by his late submission at Ruthen' = Boyd p.567 'done by * late submission at *' (two cipher words on one line, clear words between)")],
    10: [("223", 3, "CCXL: 'In this 223 hath sent for mine advice' = Boyd p.567 'In this * has sent for his advice'; 02 02 03 read as cipher digit-signs 2 2 3 (M)")],
    11: [("3 ? him", 5, "03 = 3 from F10; CCXL 'betwixt 32 and him' (p.532) would want 25 = 2, but 02 is already 2 and Boyd omits that sentence; T3's 'to him' (03 = t) is excluded by F10")],
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
    lines, counts, excluded = [], {"S": 0, "M": 0, "I": 0, "C": 0, "-": 0}, 0
    for fi, f in enumerate(frags, 1):
        dec = ""
        for pi, s in enumerate(f):
            v, g = key[s]
            note = ""
            if (fi, pi) in EXCLUDED:
                v, note = EXCLUDED[(fi, pi)]
                g = "-"; excluded += 1; dec += "+"
                out.append(f"F{fi}\t{pi+1}\t{s}\t{v}\t{g}\t{note} -- not a cipher sign, excluded from the count")
                continue
            if (fi, pi) in REPAIRS:
                g, note = "I", REPAIRS[(fi, pi)][1]
            elif fi in CALENDAR_C and v != "?":
                g, note = "C", CALENDAR_C[fi]
            counts[g] += 1
            dec += v
            out.append(f"F{fi}\t{pi+1}\t{s}\t{v}\t{g}\t{note}")
        w = WORDS[fi][0]
        lines.append(f"#F{fi}\t{dec}\t{w[0]}\t{w[2]}")
    return "\n".join(out + ["#fragment\tdecoded (key only)\tas read\tparallel Letter-Book text"] + lines +
                     [f"#grades\tS {counts['S']}\tM {counts['M']}\tI {counts['I']}\tH 0\tC {counts['C']}\tunread {counts['-']}\ttotal {sum(counts.values())}\texcluded (not cipher signs) {excluded}"]) + "\n"


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
