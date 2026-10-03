#!/usr/bin/env python3
"""H70: extract dateline/salutation/body/closing/signature from saved Founders pages (docs/*.html) into
letters.txt (one block per letter) and letters.tsv (id, date, title, words, numeral-groups). Offline."""
import glob, re, html
MON = {m: i+1 for i, m in enumerate("January February March April May June July August September October November December".split())}
def clean(s):
    s = re.sub(r"<[^>]+>", " ", s); s = html.unescape(s); return re.sub(r"\s+", " ", s).strip()
rows = []
for p in glob.glob("docs/*.html"):
    t = open(p, errors="ignore").read()
    title = clean(re.search(r"<title>(.*?)</title>", t, re.S).group(1))
    m = re.search(r"(\d{1,2}) (\w+) (\d{4})", title)
    date = f"{m.group(3)}-{MON.get(m.group(2),0):02d}-{int(m.group(1)):02d}" if m else "?"
    b = re.search(r'<div class="innerdiv docbody">(.*?)<div class="innerdiv docback">', t, re.S)
    body = b.group(1) if b else ""
    opener = clean("".join(re.findall(r'<div class="opener">(.*?)</div>', body, re.S)))
    closer = clean("".join(re.findall(r'<div class="closer">(.*?)</div>', body, re.S)))
    paras = [clean(x) for x in re.findall(r"<p[^>]*>(.*?)</p>", re.sub(r'<div class="(opener|closer)">.*?</div>', "", body, flags=re.S), re.S)]
    src = clean("".join(re.findall(r'<div class="note-source">(.*?)</div>', t, re.S)))
    notes = clean("".join(re.findall(r'<div class="note-footnotes?">(.*?)</div>', t, re.S)))[:2000]
    did = p[5:-5].replace("_", "/", 1)
    text = " ".join(paras)
    groups = len(re.findall(r"\b\d{1,4}\.?(?=\s)", text))
    rows.append((date, did, title, opener, text, closer, src, notes, len(text.split()), groups))
rows.sort()
with open("letters.txt", "w") as f:
    for r in rows:
        f.write(f"=== {r[0]} | {r[1]} | {r[2]}\nOPENER: {r[3]}\nBODY: {r[4]}\nCLOSER: {r[5]}\nSOURCE: {r[6]}\nNOTES: {r[7]}\n\n")
with open("letters.tsv", "w") as f:
    f.write("date\tid\ttitle\twords\tnumeral_tokens\turl\n")
    for r in rows: f.write(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[8]}\t{r[9]}\thttps://founders.archives.gov/documents/{r[1]}\n")
print(len(rows), "letters")
