#!/usr/bin/env python3
"""K8472: which cipher book reads a ledger's entries (vocabulary share + clause count vs meaning-shuffled copies).

  k8472_score.py ENTRIES.txt [--label X] [--truth BOOK] [--n 10] [--tsv OUT]
ENTRIES.txt is a '### id | ...' block file in the ciphertext.txt format. Books: no1 (eckert-1864/key.md), no2 (key-no2.md),
no9 (key-no9.md), mssEC15 (eckert-1862/key.md). Per entry and book: share = recognised non-function tokens / non-function
tokens; clauses = number of maximal runs of >= 3 consecutive reading tokens whose adjacent pairs are all attested bigrams in
the corpus (every entry already read with the four books, leave-one-out for an entry that is itself in the corpus). Each book
also gets two meaning-shuffled copies (word rows, seeds 7 and 11). Pre-registered rule: NOTES.md "## K8472".
"""
import argparse, random, re, sys, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
D64 = HERE.parent / "eckert-1864"
sys.path.insert(0, str(D64))
import decode

BOOKS = {"no1": D64 / "key.md", "no2": D64 / "key-no2.md", "no9": D64 / "key-no9.md", "mssEC15": HERE / "key.md"}
CORPUS_SRC = [("no1", D64 / "ciphertext.txt"), ("no2", D64 / "ciphertext-no2.txt"), ("no9", D64 / "ciphertext-no9.txt"),
              ("mssEC15", HERE / "ciphertext.txt")]
FUNC = set("the a an of to and in is are was were be been for on at by with that this it as or not but from have has had will would shall should you your i we he his her their they them there which what who whom if so no all any can may must do does did me my our us".split())
SEEDS = (7, 11)

keys = {b: decode.load_key(p) for b, p in BOOKS.items()}

def shuffled(key, seed):
    rows = [k for k, v in key.items() if v[2] == "word"]
    meanings = [key[k] for k in rows]
    random.Random(seed).shuffle(meanings)
    out = dict(key)
    for k, m in zip(rows, meanings):
        out[k] = m
    return out

variants = {}
for b, k in keys.items():
    variants[b] = k
    for s in SEEDS:
        variants[f"{b}~{s}"] = shuffled(k, s)

def rtoks(reading, flag=False):
    """Reading tokens: decoded '[meaning (note)]' -> meaning words; braces (date/time/tail) dropped. flag=True marks
    tokens that came from a decoded code word with a leading '*'."""
    t = re.sub(r"\{[^}]*\}", " ", reading)
    mark = "*" if flag else ""
    t = re.sub(r"\[([^\]]*)\]", lambda m: " " + " ".join(mark + w for w in re.findall(r"[a-z]+", re.sub(r"\(.*?\)", " ", m.group(1)).lower())) + " ", t)
    return re.findall(r"\*?[a-z]+", t.lower()) if flag else re.findall(r"[a-z]+", t.lower())

def bigrams(toks):
    return list(zip(toks, toks[1:]))

def entry_tokens(text):
    return [w for w in re.findall(r"[a-z]+", re.sub(r"\s*=\s*", "", text.lower())) if w not in FUNC and len(w) > 1]

# corpus of attested bigrams from the four readings, per entry (for leave-one-out)
corpus = collections.Counter()
own = {}   # (book, header) -> Counter of its bigrams
for b, path in CORPUS_SRC:
    for header, lines in decode.load_ciphertext(path):
        text = decode.entry_text(lines)
        r, _ = decode.decode_entry(text, keys[b])
        c = collections.Counter(bigrams(rtoks(r)))
        corpus.update(c)
        own[(b, header.split("|")[0].strip())] = c

def clauses(reading, leave=None):
    """Clause = maximal run of >= 3 consecutive reading tokens, every adjacent pair an attested bigram, containing at
    least one token that came from a decoded code word (so the count depends on the book's meanings)."""
    tk = rtoks(reading, flag=True)
    runs, cur, dec = 0, 1, 0
    prev = None
    for i, bg in enumerate(bigrams(tk)):
        key = (bg[0].lstrip("*"), bg[1].lstrip("*"))
        n = corpus[key] - (leave[key] if leave else 0)
        if n >= 1:
            if cur == 1: dec = 1 if bg[0].startswith("*") else 0
            dec |= 1 if bg[1].startswith("*") else 0
            cur += 1
        else:
            if cur >= 3 and dec: runs += 1
            cur, dec = 1, 0
    if cur >= 3 and dec: runs += 1
    return runs

def score(entries, truth_book=None):
    rows = []
    for header, lines in entries:
        eid = header.split("|")[0].strip()
        text = decode.entry_text(lines)
        tk = entry_tokens(text)
        leave = own.get((truth_book, eid)) if truth_book else None
        rec = {"id": eid, "n": len(tk)}
        for v, key in variants.items():
            share = sum(1 for w in tk if decode.lookup(w, key)[2] is not None) / max(1, len(tk))
            reading, cnt = decode.decode_entry(text, key)
            rec[v] = (round(share, 3), clauses(reading, leave))
        rows.append(rec)
    return rows

def verdict(rows):
    """Pre-registered: entry passes for book B when share_B > every other book's share and clauses_B > both ~ copies of B."""
    wins = {b: 0 for b in BOOKS}
    for r in rows:
        for b in BOOKS:
            if all(r[b][0] > r[o][0] for o in BOOKS if o != b) and all(r[b][1] > r[f"{b}~{s}"][1] for s in SEEDS):
                wins[b] += 1
    return wins

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entries"); ap.add_argument("--truth"); ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--tsv"); ap.add_argument("--label", default="")
    a = ap.parse_args()
    ents = decode.load_ciphertext(Path(a.entries))[: a.n]
    rows = score(ents, a.truth)
    wins = verdict(rows)
    print(f"# {a.label or a.entries}: {len(rows)} entries; books reading by rule (need >= 7 of {len(rows)}): {wins}")
    out = []
    for r in rows:
        line = [r["id"], str(r["n"])]
        for b in BOOKS:
            line.append(f"{b}={r[b][0]:.2f}/{r[b][1]}|~{r[f'{b}~7'][1]},{r[f'{b}~11'][1]}")
        out.append("\t".join(line)); print(out[-1])
    if a.tsv:
        Path(a.tsv).write_text("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
