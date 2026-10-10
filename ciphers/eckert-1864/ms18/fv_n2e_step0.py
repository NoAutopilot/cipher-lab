#!/usr/bin/env python3
"""FV-N2e step 0 (LANE LEDGER-10 Wave 3 Step-0 ruling): N2-IA IB IC ID IG IH.

(a) ordered overlap = LCS of content words (stop words dropped, one case, digits as words) between the decoded body
    (reading-no2.md; header {date/time} markup and the tail's unbracketed check words dropped) and the holder
    transcription of the entry's own lines (ms18/n2r4_entries.txt, cut by N2R-4 from sources/mssEC18/p<pointer>.json;
    each block is checked here to be a substring of the page JSON) / decoded content words;
(b) control = the same LCS against the transcription's words shuffled within the entry, 20 draws, p95 (19th of 20);
(c) key-dependent words = decoded content words not in the transcription at all.
Hit = (a) >= 0.5 and (a) > (b). Disk only.
"""
import json, os, random, re
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
STOP = set("""a an the and or of to in on at by for from with as is are was were be been it its that this these those you your
i he him his she her we they them their our not no so if but all any some will may can shall should would have has had do
did into than then there here what which who whom per about more most very s st""".split())
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
def num(n):
    n = int(n)
    if n < 20: return ONES[n]
    if n < 100: return TENS[n // 10] + ("" if n % 10 == 0 else " " + ONES[n % 10])
    if n < 1000: return ONES[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + num(n % 100))
    return " ".join(ONES[int(d)] for d in str(n))
def words(s):
    s = re.sub(r"\d+", lambda m: " " + num(m.group()) + " ", s.lower())
    return [w for w in re.findall(r"[a-z]+", s) if w not in STOP and len(w) > 1]
ENTRIES = {"N2-IA": ("Z1", 9701), "N2-IB": ("Z2", 9850), "N2-IC": ("Z3", 9755), "N2-ID": ("Z4", 9898),
           "N2-IG": ("Z7", 9906), "N2-IH": ("Z8", 9739)}
def lcs(a, b):
    m = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a)):
        for j in range(len(b)):
            m[i + 1][j + 1] = m[i][j] + 1 if a[i] == b[j] else max(m[i][j + 1], m[i + 1][j])
    return m[-1][-1]
rd = open(os.path.join(T, "reading-no2.md")).read()
blocks = {}
for blk in open(os.path.join(HERE, "n2r4_entries.txt")).read().split("### ")[1:]:
    head, _, body = blk.partition("\n"); blocks[head.split("|")[0].strip()] = body.strip()
def body(eid):
    m = re.search(r"\*\*%s \|.*?\*\*\n\n(.*?)\n\nCode-word tokens" % re.escape(eid), rd, re.S); b = m.group(1)
    tail = re.search(r"\{tail:(.*?)\}", b); tb = " ".join(re.findall(r"\[([^\]]*)\]", tail.group(1))) if tail else ""
    b = re.sub(r"\{[^}]*\}", " ", b) + " " + tb
    return words(re.sub(r"[\[\]]", " ", b))
random.seed(2)
print("entry\tpointer\tblock_in_page_json\ta_ordered\tb_shuffle_p95\tstep0_hit\tc_count\tc_words")
for e, (z, p) in ENTRIES.items():
    page = json.load(open(os.path.join(T, "sources/mssEC18/p%d.json" % p)))["transc"]
    tx_raw = blocks[z]; inpage = all(" ".join(l.split()) in " ".join(page.split()) for l in tx_raw.splitlines() if l.strip() and not l.startswith("#"))
    d = body(e); t = words(tx_raw)
    a = lcs(d, t) / len(d)
    ctl = []
    for _ in range(20):
        s = t[:]; random.shuffle(s); ctl.append(lcs(d, s) / len(d))
    b = sorted(ctl)[18]; ts = set(t)
    c = [w for w in d if w not in ts]
    print(f"{e}\t{p}\t{inpage}\t{a:.3f} ({lcs(d, t)}/{len(d)})\t{b:.3f}\t{'yes' if a >= 0.5 and a > b else 'no'}\t{len(c)}\t{' '.join(c)}")
