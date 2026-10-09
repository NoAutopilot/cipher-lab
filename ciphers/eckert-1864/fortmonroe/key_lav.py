#!/usr/bin/env python3
"""KEY-LAV (9 Oct 2026, account 1, for LANE LEDGER): two key questions on Cipher No. 1, method of KEY-TW/KEY-BLIND.

(a) Lavender = Gen. C. C. Washburn(e). key.md already carries the row at H (mssEC 43 p.[17], pointer 413), and
    FV-MS18c read it at E330 against OR I/39 pt 3 p.379. Here the value is tested at every occurrence: the filed
    ones in ciphertext*.txt (E169, E330) and the two unfiled ones in mssEC 18 (9870/1, 9893/2, text from the
    Huntington's own CONTENTdm transcription cached in sources/mssEC18/, image not checked here). Control: the same
    contexts, each given a person drawn at random (fixed seed) from key.md's person meanings. Candidate and control
    windows are shuffled and printed with ids hidden (--blind); the reader writes R/N/U to key_lav_verdicts.tsv and
    commits it before --unmask.

(b) Tulip in No. 1 entries: Open (H, p.22 l.14) or Period (S, KEY-TW). The rule, fixed before the run:
    Tulip = Open when the token is inflected (tuliped, tuliping...) or the word before it is in PRED (a verb that
    takes "open" as its complement: remain, keep, be ...); otherwise Tulip = Period. --tulip lists every filed
    occurrence (ciphertext.txt No. 1, plus the unfiled 9893/1 and No. 2 as a side check) with the rule's verdict,
    and a null: the share of all key-word occurrences whose preceding word is in PRED (how often the rule would
    fire on a random token).

Usage: python3 key_lav.py --help | --contexts | --blind | --unmask | --tulip
--contexts prints the unmasked candidate windows; a blind reader runs --blind first and never --contexts.
"""
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
T = HERE.parent
sys.path.insert(0, str(T))
import decode  # noqa: E402

SEED = 20261009
VALUE = "Gen C. C. Washburne"
VERDICTS = HERE / "key_lav_verdicts.tsv"
PERSON = re.compile(r"\b(Gen|Genl|General|Maj|Brig|Col|Adm|Admiral|Capt|Commodore|Secretary|President|Gov)\b")
PRED = {"remain", "remains", "remained", "keep", "keeps", "kept", "be", "is", "are", "was", "were", "been", "left",
        "lie", "lies", "lay", "hold", "holds", "held", "stand", "stands", "stood", "lain", "being"}
UNFILED = [("9870/1 (unfiled; mssEC 18 obj 10074; Fowler, Memphis, Wash. 17 Oct 1864, No 1 2 pm)", "mssEC18/p9870.json",
            "Fowler Memphis", "430 pm"),
           ("9893/2 (unfiled; mssEC 18 obj 10074; RS Fowler [Memphis], Wash. 9 Nov 1864, No 1)", "mssEC18/p9893.json",
            "RS Fowler", "\n\n\n")]


def transc(name):
    d = json.loads((T / "sources" / name).read_text())
    found = []

    def walk(o, k=""):
        if isinstance(o, dict):
            for a, b in o.items():
                walk(b, a)
        elif isinstance(o, list):
            for b in o:
                walk(b, k)
        elif isinstance(o, str) and k == "transc":
            found.append(o)
    walk(d)
    return found[0]


def unfiled_lines(name, start, stop):
    t = transc(name)
    i = t.index(start)
    j = t.find(stop, i + len(start))
    return t[i:j if j > 0 else None].strip().splitlines()


def contexts():
    """(label, lines) for every occurrence of lavender."""
    out = []
    for path in sorted(T.glob("ciphertext*.txt")):
        for header, lines in decode.load_ciphertext(path):
            if any(re.search(r"(?i)\blavender\b", ln) for ln in lines if not ln.startswith("plain")):
                if any(ln.startswith("plain") and "lavender" in ln.lower() for ln in lines):
                    continue  # E169: the period instruction defining the word (plain there), not a use
                out.append((f"{path.name}: {header[:150]}", lines))
    for label, name, a, b in UNFILED:
        out.append((label, unfiled_lines(name, a, b)))
    return out


def persons(key):
    seen = {}
    for w, (meaning, grade, kind) in key.items():
        if kind == "word" and PERSON.search(meaning) and "washburn" not in meaning.lower():
            seen.setdefault(meaning, w)
    return sorted(seen)


def render(key, lines, value):
    k = dict(key)
    g = key["lavender"][1]
    k["lavender"] = (value, g, "word")
    k["loadstone"] = (value, g, "word")
    text = decode.entry_text(lines)
    reading, _ = decode.decode_entry(text, k)
    return reading


def items(key):
    ctx = contexts()
    pool = persons(key)
    rng = random.Random(SEED)
    ctl = rng.sample(pool, len(ctx))
    its = [("cand", lab, lines, VALUE) for lab, lines in ctx]
    its += [("ctl", lab, lines, v) for (lab, lines), v in zip(ctx, ctl)]
    rng.shuffle(its)
    return its, len(pool)


def fisher_one_sided(a, n1, c, n2):
    """P(candidate reads >= a) under the hypergeometric null, margins fixed."""
    from math import comb
    tot, k = n1 + n2, a + c
    return sum(comb(n1, x) * comb(n2, k - x) for x in range(a, min(n1, k) + 1)) / comb(tot, k)


def tulip(key):
    rows = []
    for path in (T / "ciphertext.txt", T / "ciphertext-no2.txt"):
        for header, lines in decode.load_ciphertext(path):
            words = decode.entry_text(lines).split(" ")
            for i, w in enumerate(words):
                c = re.sub(r"[^a-z]", "", w.split("~")[0].rstrip("\\").lower())
                if c in ("tulip", "tuslip") or (c.startswith("tulip") and len(c) > 5):
                    rows.append((path.name, header[:40], words, i, c))
    t = transc("mssEC18/p9893.json")
    w1 = t[: t.index("RS Fowler")].split()
    rows += [("unfiled 9893/1", "Kingston Ga 8 Nov 1864", w1, i, "tulip") for i, x in enumerate(w1)
             if x.lower() == "tulip"]
    print("## Tulip rule: Open if inflected or the word before is in PRED, else Period")
    agree = 0
    for src, h, words, i, c in rows:
        prev = re.sub(r"[^a-z]", "", words[i - 1].split("~")[0].lower()) if i else ""
        verdict = "Open" if (c not in ("tulip", "tuslip") or prev in PRED) else "Period"
        win = " ".join(x.split("~")[0].rstrip("\\") for x in words[max(0, i - 5): i + 6])
        print(f"{src}\t{h}\tprev={prev}\t{verdict}\t... {win} ...")
    # null: how often a random code-word token sits after a PRED word
    n = hit = 0
    for header, lines in decode.load_ciphertext(T / "ciphertext.txt"):
        words = decode.entry_text(lines).split(" ")
        for i in range(1, len(words)):
            c = re.sub(r"[^a-z]", "", words[i].lower())
            if c in key and key[c][2] == "word":
                n += 1
                hit += re.sub(r"[^a-z]", "", words[i - 1].lower()) in PRED
    print(f"null: {hit} of {n} key-word tokens ({hit / n:.3f}) follow a PRED word")
    return agree


def main(argv):
    if "--help" in argv or "-h" in argv or not argv:
        print(__doc__)
        return 0
    key = decode.load_key()
    if "--tulip" in argv:
        tulip(key)
        return 0
    if "--contexts" in argv:
        for lab, lines in contexts():
            print(f"## {lab}\n  as written: {' '.join(lines)}\n  with value: {render(key, lines, VALUE)}\n")
        return 0
    its, npool = items(key)
    if "--blind" in argv:
        print(f"# {len(its)} windows; each gives code word LAVENDER (and Loadstone) one person; judge R/N/U from the "
              f"text, the date, the place and the addressee. Person pool {npool}, seed {SEED}.")
        for n, (_, lab, lines, v) in enumerate(its):
            hdr = re.sub(r"E\d+ \| |\(.*$|mssEC.*?\), ", "", lab)
            print(f"\n{n:02d}\tvalue = {v}\n  {render(key, lines, v)}")
        return 0
    if "--unmask" in argv:
        judg = {}
        for line in VERDICTS.read_text().splitlines():
            if line and not line.startswith("#") and not line.startswith("n\t"):
                n, mark = line.split("\t")[:2]
                judg[int(n)] = mark.strip()
        res = {}
        for kind in ("cand", "ctl"):
            rows = [(n, it) for n, it in enumerate(its) if it[0] == kind]
            r = sum(judg.get(n) == "R" for n, _ in rows)
            res[kind] = (r, len(rows))
            print(f"{kind}\treads {r} of {len(rows)}\t" +
                  "; ".join(f"{n}{judg.get(n, '?')} {it[3]} @ {it[1][:40]}" for n, it in rows))
        (a, n1), (c, n2) = res["cand"], res["ctl"]
        print(f"Fisher one-sided p = {fisher_one_sided(a, n1, c, n2):.4f}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
