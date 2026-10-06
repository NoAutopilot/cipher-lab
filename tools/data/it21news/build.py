#!/usr/bin/env python3
"""Build it21news (R12D-ERBA3, LANE LANE-RUN12-account-4, 6 Oct 2026): modern Italian prose (2005-2026) for
erba-2006 (a 2013 private Italian note), which it16/it16dip/it19 (16th c., 1800-1830) do not era-match.

Source: the Italian Wikinews (Wikinotizie) XML dump itwikinews-latest-pages-articles.xml.bz2 (dumps.wikimedia.org,
dump of 1 Oct 2026, sha1 in MANIFEST.tsv), CC BY 2.5 (Wikinews' licence). Same shape as it19/pt18: one output file per
fold so a leave-one-file-out false-negative spread can be run (rule 3 fold-count paragraph).

Per main-namespace article: the year comes from its {{data|<day> <month> <YYYY>|...}} template (articles without one
are dropped); wikitext is stripped (templates, tables, refs, files, link markup, headings, lists, quotes kept as
text); paragraphs of >= 25 words with Italian function words >= 22% of tokens are kept, folded (NFKD, no accents,
lower case, letters and spaces only). Folds by year: 2005-06, 2007, 2008, 2009-10, 2011-26. Each fold is capped at
CAP folded letters.
  python3 tools/data/it21news/build.py --dump FILE.xml.bz2
"""
import argparse, bz2, gzip, re, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAP = 500_000
FOLDS = [("y2005_06", 2005, 2006), ("y2007", 2007, 2007), ("y2008", 2008, 2008), ("y2009_10", 2009, 2010),
         ("y2011_26", 2011, 2026)]
IT = set("di che e la il non per del in a si da le al della un una con ma se lo mi gli io e era sua suo i ed come "
         "piu quando dei alla delle nel sono anche gia poi ne ci essere ha aveva fu cosi questo quella quello "
         "loro o tra fra dopo dal dalle degli ai nella sul sulla".split())


def fold(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z]+", " ", s).split()


def strip_templates(t):
    out, depth, i = [], 0, 0
    while i < len(t):
        if t.startswith("{{", i) or t.startswith("{|", i):
            depth += 1; i += 2; continue
        if depth and (t.startswith("}}", i) or t.startswith("|}", i)):
            depth -= 1; i += 2; continue
        if not depth:
            out.append(t[i])
        i += 1
    return "".join(out)


def clean(text):
    text = re.sub(r"&lt;", "<", text); text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"&amp;", "&", text); text = re.sub(r"&quot;", '"', text)
    text = re.sub(r"<ref[^>]*/>", " ", text)
    text = re.sub(r"<ref.*?</ref>", " ", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = strip_templates(text)
    text = re.sub(r"\[\[(?:File|Immagine|Image|Categoria|Category|w:[a-z]{2}):[^\]]*\]\]", " ", text, flags=re.I)
    text = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", text)
    text = re.sub(r"\[\[([^\]]*)\]\]", r"\1", text)
    text = re.sub(r"\[https?://\S+ ([^\]]*)\]", r"\1", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"'{2,}", "", text)
    return text


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dump", required=True)
    a = ap.parse_args()
    raw = bz2.open(a.dump, "rt", encoding="utf-8").read()
    bins = {f[0]: [] for f in FOLDS}
    used = {f[0]: 0 for f in FOLDS}
    arts = {f[0]: 0 for f in FOLDS}
    for page in re.findall(r"<page>(.*?)</page>", raw, re.S):
        if "<ns>0</ns>" not in page:
            continue
        m = re.search(r'<text[^>]*>(.*?)</text>', page, re.S)
        if not m or m.group(1).lstrip().upper().startswith("#REDIRECT"):
            continue
        body = m.group(1)
        d = re.search(r"\{\{\s*data\s*\|[^|}]*?(\d{4})", body, re.I)
        if not d:
            continue
        year = int(d.group(1))
        name = next((f[0] for f in FOLDS if f[1] <= year <= f[2]), None)
        if name is None:
            continue
        took = False
        for para in clean(body).split("\n"):
            para = para.strip()
            if not para or para[0] in "=*#:;|!":
                continue
            w = fold(para)
            if len(w) < 25 or sum(x in IT for x in w) / len(w) < 0.22:
                continue
            n = sum(map(len, w))
            if used[name] + n > CAP:
                continue
            bins[name].append(" ".join(w)); used[name] += n; took = True
        arts[name] += took
    for name, lines in bins.items():
        with gzip.open(HERE / f"{name}.txt.gz", "wt", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(f"{name}\tarticles={arts[name]}\tparagraphs={len(lines)}\tletters={used[name]}")


if __name__ == "__main__":
    main()
