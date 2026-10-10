#!/usr/bin/env python3
"""FV-MS18q step 0 under the LANE LEDGER-10 Wave 3 "Step-0 ruling" (orchestrator, 10 Oct 2026), disk only.

Per entry (E383 E384 E385 E386 E387 E389):
 (a) ordered overlap = LCS of content words (stop words dropped, one case, digits as words; other numbers as one token) between the decoded body
     (reading.md body line; {date:}/{time:} dropped, {tail:} kept) and the holder transcription of the entry's OWN lines
     (sources/mssEC18/p<pointer>.json "transc", restricted to the lines the entry's ciphertext.txt block copies; each
     line is checked to occur verbatim in the page transcription), / decoded content words;
 (b) control = the same LCS against the entry's transcription words shuffled within the entry, 20 draws, p95;
 (c) key-dependent words = decoded content words NOT in the entry's transcription at all, count and list.
 Hit = (a) >= 0.5 and (a) > (b).
"""
import json, random, re, os
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
STOP = set("""a an the and or of to in on at by for from with as is are was were be been it its that this these those you your
i he him his she her we they them their our not no so if but all any some will may can shall should would have has had do
did into than then there here what which who whom per one about more most very s st""".split())
NUM = {"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine",
       "10":"ten","19":"nineteen","100":"hundred"}
CONTROLS = {"E378": 9820, "E381": 9258}  # known N1 by holder transcription (AUD2-LEDGER-38): must hit
ENTRIES = {"E383": 10048, "E384": 9885, "E385": 9887, "E386": 9841, "E387": 10055, "E389": 9903}
def words(s):
    s = re.sub(r"\d+", lambda m: " %s " % NUM.get(m.group(0), "num" + "".join(chr(97 + int(d)) for d in m.group(0))), s.lower())
    return [w for w in re.findall(r"[a-z]+", s) if w not in STOP and len(w) > 1]
def lcs(a, b):
    m = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            m[i+1][j+1] = m[i][j]+1 if a[i] == b[j] else max(m[i][j+1], m[i+1][j])
    return m[-1][-1]
rd = open(os.path.join(T, "reading.md")).read(); ct = open(os.path.join(T, "ciphertext.txt")).read()
def body(eid):
    m = re.search(r"\*\*%s \|[^\n]*\*\*\n\n(.*?)\n\nCode-word tokens" % eid, rd, re.S); b = m.group(1)
    b = re.sub(r"\{(date|time):[^}]*\}", " ", b); b = re.sub(r"\{tail:", " ", b).replace("}", " ")
    b = re.sub(r"\(-ed, -ing\)", " ", b)
    return b, words(re.sub(r"[\[\]]", " ", b)), words(" ".join(re.findall(r"\[([^\]]*)\]", b)))
def entry_tx(eid, p):
    m = re.search(r"### %s \|[^\n]*\n(.*?)\nnote:" % eid, ct, re.S)
    lines = [l.strip() for l in m.group(1).split("\n") if l.strip()]
    page = re.sub(r"[ \t]+", " ", json.load(open([f for f in (os.path.join(T, "sources/mssEC%d/p%d.json" % (v, p)) for v in (18, 19)) if os.path.exists(f)][0]))["transc"])
    missing = [l for l in lines if re.sub(r"[ \t]+", " ", l) not in page]
    return lines, missing
random.seed(383)
print("entry\tpointer\ta_ordered\tb_shuffle_p95\thit\tc_count\tc_words\tcode_meanings_in_tx\tlines_not_verbatim")
for e, p in list(CONTROLS.items()) + list(ENTRIES.items()):
    raw, bw, codew = body(e); lines, miss = entry_tx(e, p)
    tw = words(" ".join(lines))  # all of the entry's own lines, header (operator, place, date) included
    a = lcs(bw, tw) / len(bw)
    ctl = []
    for _ in range(20):
        s = tw[:]; random.shuffle(s); ctl.append(lcs(bw, s) / len(bw))
    b95 = sorted(ctl)[18]
    tset = set(tw); c = [w for w in bw if w not in tset]
    ci = sum(1 for w in codew if w in tset)
    print(f"{e}\t{p}\t{a:.3f} ({lcs(bw,tw)}/{len(bw)})\t{b95:.3f}\t{'HIT' if (a >= 0.5 and a > b95) else 'no'}\t{len(c)}\t{' '.join(c)}\t{ci}/{len(codew)}\t{len(miss)}" + ("\tcontrol (must hit)" if e in CONTROLS else ""))
