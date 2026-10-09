#!/usr/bin/env python3
"""sameday.py -- the sender's letters near a date as crib candidates and dating evidence.

A partial reading of a cipher letter is compared with the sender's dated letters to anyone (an edition's clear text,
one letter per row) within +-W days of a date. Shared word phrases are ranked by rarity, the window's total is set
against a shuffled-date null, and phrases that run into an unread word propose that word as a crib (grade I: inferred,
never a reading, never a key edit). Idea: Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2) p.125 (a letter dated by
its overlap with a letter to Beaton), p.136 n.97, p.137 n.100; research/MARY-STUART-TALK-2026-10-09.tsv row M46
(MQS-SAMEDAY, 9 Oct 2026). Control and gates: tools/tests/PREREG-MQS-SAMEDAY.md, tools/tests/mqs_sameday_control.py.

Usage:
  sameday.py rank READING.txt --letters LETTERS.tsv --date 1798-10-11 [--window 7] [--exclude ID] [--shuffles 20]
  sameday.py date READING.txt --letters LETTERS.tsv [--window 7] [--top 10] [--exclude ID]
  sameday.py parse EDITION_djvu.txt --sender-re 'Mornington to|Wellesley to' --out LETTERS.tsv [--min-words 120]

READING: plain words; '?', '_' or '[...]' marks an unread word (it breaks phrases). LETTERS.tsv: header
id, date (YYYY-MM-DD), recipient, text. `parse` cuts an OCR edition at 'No. <roman>.' headings (Martin's Wellesley
Despatches layout); other editions write the TSV their own way.

Scope (Usage 8a):
  catches   -- a rare trigram shared with a letter inside the window (test_sameday: window letter ranked, crib proposed);
               a date whose window holds the shared wording ranks above dates that do not (test_date_rank).
  must NOT  -- rank a letter outside +-W days (test_outside_window); count a phrase made only of stopwords
               ("of the said") or one bridging an unread word (test_stopword_and_gap); match the item itself when its
               id is given with --exclude (test_exclude_self).
Output is evidence for a person: crib words are grade I, a date rank is a dating lead, never a date.
"""
import argparse
import math
import random
import re
import statistics
import sys
from collections import Counter, defaultdict
from datetime import date, timedelta

STOP = set("""a an the and or but of to in on at by for with from as is was be been are were it its this that these those
which who whom whose he she they we you i me my our your his her their them him us not no nor so than then there here
have has had do did shall will would should may might can could all any such same said upon into unto per
le la les de des du et en un une que qui il elle ils au aux a ce cette se sa son ses par pour sur pas ne est
el los las del y lo con por para su sus il di da che e non per con al gli della dei""".split())
GAP = re.compile(r"^(\?+|_+|\[.*\])$")
WORD = re.compile(r"[a-zA-ZÀ-ſ]+|\?+|_+|\[[^\]]*\]")


def tokens(text):
    """Folded word tokens; unread marks become None."""
    out = []
    for w in WORD.findall(text):
        out.append(None if GAP.match(w) else w.lower())
    return out


def trigrams(toks):
    """(gram, index of the word after it) for every fully read, not all-stopword trigram."""
    out = []
    for i in range(len(toks) - 2):
        g = toks[i:i + 3]
        if None in g or all(w in STOP for w in g):
            continue
        out.append((tuple(g), i + 3))
    return out


def load_letters(path):
    letters = []
    with open(path, encoding="utf-8") as f:
        head = f.readline().rstrip("\n").split("\t")
        for line in f:
            row = dict(zip(head, line.rstrip("\n").split("\t")))
            if not row.get("date"):
                continue
            row["d"] = date.fromisoformat(row["date"])
            row["toks"] = tokens(row.get("text", ""))
            letters.append(row)
    return letters


class Index:
    def __init__(self, letters):
        self.letters = letters
        self.grams = []  # per letter: gram -> list of next words
        df = Counter()
        for L in letters:
            m = defaultdict(list)
            for g, j in trigrams(L["toks"]):
                m[g].append(L["toks"][j] if j < len(L["toks"]) else None)
            self.grams.append(m)
            df.update(m.keys())
        n = len(letters)
        self.w = {g: math.log((n + 1) / (c + 1)) for g, c in df.items()}

    def weight(self, g):
        return self.w.get(g, math.log(len(self.letters) + 1))


def window_ids(dates, d, window, exclude):
    return [i for i, x in enumerate(dates) if abs((x - d).days) <= window and i not in exclude]


def window_score(idx, rgrams, ids):
    found = set()
    for i in ids:
        found.update(g for g in rgrams if g in idx.grams[i])
    return sum(idx.weight(g) for g in found), found


def cribs(idx, rtoks, ids):
    """Proposals: (gap position, proposed word, trigram, letter ids)."""
    out = []
    for g, j in trigrams(rtoks):
        if j >= len(rtoks) or rtoks[j] is not None:
            continue
        votes, src = Counter(), []
        for i in ids:
            for nxt in idx.grams[i].get(g, []):
                if nxt:
                    votes[nxt] += 1
                    src.append(i)
        if votes:
            out.append((j, votes.most_common(1)[0][0], g, sorted(set(src))))
    return out


def date_ranks(idx, rgrams, dates, window, exclude, candidates):
    scores = {d: window_score(idx, rgrams, window_ids(dates, d, window, exclude))[0] for d in candidates}
    return scores


def avg_rank(scores, d):
    s = scores[d]
    above = sum(1 for v in scores.values() if v > s)
    ties = sum(1 for v in scores.values() if v == s)
    return above + (ties + 1) / 2


def excluded(letters, ids):
    return {i for i, L in enumerate(letters) if L.get("id") in ids}


def cmd_rank(a):
    letters = load_letters(a.letters)
    idx = Index(letters)
    rtoks = tokens(open(a.reading, encoding="utf-8").read())
    rgrams = {g for g, _ in trigrams(rtoks)}
    d = date.fromisoformat(a.date)
    ex = excluded(letters, a.exclude)
    dates = [L["d"] for L in letters]
    ids = window_ids(dates, d, a.window, ex)
    score, found = window_score(idx, rgrams, ids)
    null = []
    for s in range(1, a.shuffles + 1):
        sh = dates[:]
        random.Random(s).shuffle(sh)
        null.append(window_score(idx, rgrams, window_ids(sh, d, a.window, ex))[0])
    p95 = sorted(null)[int(0.95 * (len(null) - 1))] if null else float("nan")
    print(f"window {d} +-{a.window}d: {len(ids)} letters; score {score:.2f}; shuffled-date null mean "
          f"{statistics.mean(null) if null else float('nan'):.2f} p95 {p95:.2f} ({a.shuffles} shuffles)")
    print("phrase\tweight\tletters (id date recipient)")
    for g in sorted(found, key=lambda g: -idx.weight(g))[:a.top]:
        src = [letters[i] for i in ids if g in idx.grams[i]]
        print(" ".join(g) + f"\t{idx.weight(g):.2f}\t" + "; ".join(f"{L['id']} {L['date']} {L.get('recipient', '')}" for L in src))
    print("crib (grade I)\tafter\tposition\tletters")
    for j, w, g, src in cribs(idx, rtoks, ids):
        print(f"{w}\t{' '.join(g)}\t{j}\t" + ", ".join(letters[i]["id"] for i in src))
    return 0


def cmd_date(a):
    letters = load_letters(a.letters)
    idx = Index(letters)
    rtoks = tokens(open(a.reading, encoding="utf-8").read())
    rgrams = {g for g, _ in trigrams(rtoks)}
    ex = excluded(letters, a.exclude)
    dates = [L["d"] for L in letters]
    cands = sorted({x for i, x in enumerate(dates) if i not in ex})
    scores = date_ranks(idx, rgrams, dates, a.window, ex, cands)
    print(f"date\tscore\trank of {len(cands)} (a dating lead, never a date)")
    for d in sorted(cands, key=lambda d: -scores[d])[:a.top]:
        print(f"{d}\t{scores[d]:.2f}\t{avg_rank(scores, d):.1f}")
    return 0


MONTHS = {m: i + 1 for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split())}
DATE_RE = [
    re.compile(r"\b([0-9Il]{1,2})(?:st|nd|rd|th|d)?\.?(?: of)? ([A-Z][a-z]{2,8})\.?,? *(1[6-9][0-9]{2})"),
    re.compile(r"\b([A-Z][a-z]{2,8})\.? ([0-9Il]{1,2})(?:st|nd|rd|th|d)?,? *(1[6-9][0-9]{2})"),
]


def parse_date(line):
    for k, rx in enumerate(DATE_RE):
        for m in rx.finditer(line):
            dd, mon, yy = (m.group(1), m.group(2), m.group(3)) if k == 0 else (m.group(2), m.group(1), m.group(3))
            mo = MONTHS.get(mon[:3].lower())
            if not mo:
                continue
            try:
                return date(int(yy), mo, int(dd.replace("I", "1").replace("l", "1")))
            except ValueError:
                continue
    return None


HEAD = re.compile(r"^No\. [IVXLCl]+\.? *$")


def parse_edition(text, sender_re, min_words, prefix=""):
    lines = text.splitlines()
    starts = [i for i, s in enumerate(lines) if HEAD.match(s.strip())]
    rx = re.compile(sender_re)
    out = []
    for k, i in enumerate(starts):
        end = starts[k + 1] if k + 1 < len(starts) else len(lines)
        head = [s for s in lines[i + 1:i + 5] if s.strip()][:3]
        if not head or not rx.search(" ".join(head[:2])):
            continue
        d = None
        for j, s in enumerate(head):
            d = parse_date(s)
            if d:
                break
        if not d:
            continue
        body_start = i + 1 + lines[i + 1:end].index(head[j]) + 1
        body = " ".join(s.strip() for s in lines[body_start:end] if s.strip())
        body = re.sub(r"-\s+(?=[a-z])", "", body)
        if len(body.split()) < min_words:
            continue
        m = re.search(r"\bto (?:the )?(.+?)[.,]?\s*$", head[0])
        out.append({"id": prefix + lines[i].strip().rstrip("."), "date": d.isoformat(),
                    "recipient": (m.group(1) if m else "")[:60], "text": body.replace("\t", " ")})
    return out


def cmd_parse(a):
    rows = parse_edition(open(a.edition, encoding="utf-8", errors="replace").read(), a.sender_re, a.min_words, a.id_prefix)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write("id\tdate\trecipient\ttext\n")
        for r in rows:
            f.write(f"{r['id']}\t{r['date']}\t{r['recipient']}\t{r['text']}\n")
    print(f"{len(rows)} letters -> {a.out}")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter,
                                epilog=__doc__.split("Usage:")[1])
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("rank", "date"):
        s = sub.add_parser(name)
        s.add_argument("reading")
        s.add_argument("--letters", required=True)
        s.add_argument("--window", type=int, default=7)
        s.add_argument("--exclude", action="append", default=[], help="letter id to leave out (the item itself)")
        s.add_argument("--top", type=int, default=20)
        if name == "rank":
            s.add_argument("--date", required=True)
            s.add_argument("--shuffles", type=int, default=20)
    s = sub.add_parser("parse")
    s.add_argument("edition")
    s.add_argument("--sender-re", required=True)
    s.add_argument("--out", required=True)
    s.add_argument("--min-words", type=int, default=120)
    s.add_argument("--id-prefix", default="", help="prefix for ids (e.g. 'v2 ' when two volumes reuse numbers)")
    a = p.parse_args(argv)
    return {"rank": cmd_rank, "date": cmd_date, "parse": cmd_parse}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
