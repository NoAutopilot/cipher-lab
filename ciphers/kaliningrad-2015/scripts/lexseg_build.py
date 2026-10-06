#!/usr/bin/env python3
"""lexseg_build.py (R12-KAL8, 6 Oct 2026): train corpora and held-out lexicons for scripts/lexseg.py on the remaining
kaliningrad-2015 schemes. Offline, deterministic.

  python3 ciphers/kaliningrad-2015/scripts/lexseg_build.py OUTDIR

Russian (s1, s1s, s3 via tools/translit_ru.py; s3_soft = s3 --soft-letters): train = Synodal Bible books outside 40-66
(tools/data/ru19), lexicon = word types of books 40-66 (the New Testament) in the same scheme, length >= 4, count >= 2
-- R10-KAL7's rule. German (de20): train = the five files other than Effi Briest and Frau Jenny Treibel; lexicon = word
types of those two held-out files, folded with homophonic_anneal.fold, length >= 4, count >= 2.
Writes OUTDIR/train_<u>.txt.gz and OUTDIR/lex_<u>.txt.
"""
import collections, glob, gzip, os, re, subprocess, sys, tempfile
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import homophonic_anneal as ha  # noqa: E402

out = sys.argv[1]
os.makedirs(out, exist_ok=True)


def lexicon(words, path):
    c = collections.Counter(w for w in words if len(w) >= 4)
    lex = sorted(w for w, n in c.items() if n >= 2)
    open(path, "w", encoding="utf-8").write("\n".join(lex) + "\n")
    return len(lex)


ru = sorted(glob.glob(os.path.join(ROOT, "tools/data/ru19/*.txt.gz")))
nt = [f for f in ru if 40 <= int(os.path.basename(f)[:2]) <= 66]
ot = [f for f in ru if f not in nt]
with tempfile.TemporaryDirectory() as td:
    for name, files in (("tr", ot), ("nt", nt)):
        os.mkdir(os.path.join(td, name))
        for f in files:
            os.symlink(f, os.path.join(td, name, os.path.basename(f)))
    for unit, scheme, soft in (("s1", "s1", []), ("s1s", "s1s", []), ("s3", "s3", []), ("s3_soft", "s3", ["--soft-letters"])):
        for name in ("tr", "nt"):
            dst = os.path.join(out, f"train_{unit}.txt.gz") if name == "tr" else os.path.join(td, f"nt_{unit}.txt")
            subprocess.run([sys.executable, os.path.join(ROOT, "tools/translit_ru.py"), "--scheme", scheme, *soft,
                            os.path.join(td, name), dst], check=True, stdout=subprocess.DEVNULL)
        words = open(os.path.join(td, f"nt_{unit}.txt"), encoding="utf-8").read().split()
        print(unit, "lexicon", lexicon(words, os.path.join(out, f"lex_{unit}.txt")))

held = ("pg5323_Effi_Briest", "pg46184_Frau_Jenny_Treibel")
de = sorted(glob.glob(os.path.join(ROOT, "tools/data/de20/*.txt.gz")))
tr = [f for f in de if not os.path.basename(f).startswith(held)]
with gzip.open(os.path.join(out, "train_de.txt.gz"), "wt", encoding="utf-8") as g:
    for f in tr:
        g.write(gzip.open(f, "rt", encoding="utf-8").read() + "\n")
words = []
for f in de:
    if os.path.basename(f).startswith(held):
        words += [ha.fold(w) for w in re.findall(r"\w+", gzip.open(f, "rt", encoding="utf-8").read())]
print("de lexicon", lexicon(words, os.path.join(out, "lex_de.txt")), "train files", len(tr))
