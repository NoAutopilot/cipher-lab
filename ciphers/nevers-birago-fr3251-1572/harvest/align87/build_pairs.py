#!/usr/bin/env python3
"""Build tools/interlinear_align.py input for no.87 (NEVBIR-87ALIGN, 2 Oct 2026).

Cipher side: harvest/ciphertext_f178r.tsv, _f178v.tsv, _f179r.tsv (the committed blind transcription, 853 signs).
Plain side: the clerk's clear decipherment (harvest/f179r_sheet/decipherment_sheet.tsv, GAPS4), split into the three
spans GAPS4 established (f.178r = L01..L03 before "da loro"; f.178v = "da loro" .. "intendo di maniera"; f.179r = "se'l
se" .. end), normalised to one convention (rule 3): struck words dropped, car.la -> carmagnola, ma.ta -> maesta, the per
sign "p" (L14) -> per, j -> i, hyphen/equals line-end marks dropped (v -> u is the tool's own fold).

Codes (numeric, so the tool's floor rule applies; --digits 4 --floor 5000):
  letter signs of the printed table  Tnn -> nn         (0 or 1 letter)
  off-sheet tiles and '?'            -> 1000 + k, one code PER TILE (X_NEW is a bag of shapes; NEVBIR-OFFSHEET),
                                       so a tile's chunk comes from its own context only (0 or 1 letter)
  word signs of the printed table    Tnn -> 6000 + nn  (any chunk length): T11 T15 T26 T29 T46 T78 T84 T89
Which signs are word signs is the one structural fact taken from the printed table; no letter value is seeded.
  python3 build_pairs.py [--shuffle-words SEED | --shift] [--out pairs.tsv]
--shuffle-words SEED: the control -- the sheet's words permuted within each span (same letters, same words, wrong order).
--shift: the control variant -- the three spans' texts rotated (f.178r gets f.179r's text, etc.), each still a real
sentence of the same letter but over the wrong signs.
"""
import argparse, csv, random, re
from pathlib import Path
H = Path(__file__).resolve().parent.parent
WORD = {"T11", "T15", "T26", "T29", "T46", "T78", "T84", "T89"}
ap = argparse.ArgumentParser(); ap.add_argument("--shuffle-words", type=int); ap.add_argument("--shift", action="store_true")
ap.add_argument("--out", default=str(Path(__file__).resolve().parent / "pairs.tsv")); ap.add_argument("--codes")
# --cipher-dir DIR (BIR87-ALIGN, 4 Oct 2026): read ciphertext_<fol>.tsv from DIR instead of harvest/. A sign written "P:<pile>"
# there is an owner pile (sorter/no87): one code per pile, 2000 + k (0/1 letter), or 7000 + k when the pile's family is a word
# sign (any chunk), so each pile's value comes from its own tiles. Committed files carry no "P:" sign: default output unchanged.
ap.add_argument("--cipher-dir")
a = ap.parse_args()

sheet = " ".join(r["text"] for r in csv.DictReader(open(H / "f179r_sheet/decipherment_sheet.tsv"), delimiter="\t"))
sheet = re.sub(r"\[[^\]]*\]", " ", sheet)
sheet = sheet.replace("car.la", "carmagnola").replace("ma.ta", "maesta").replace(" o p il ", " o per il ")
sheet = sheet.replace("=", "").replace(" - ", " ").replace("j", "i")
sheet = re.sub(r"\s+", " ", sheet).strip()
# words broken across the sheet's own line ends (prete|ndea, ima|nte, principalm|ente ...) are joined by the
# tool's letter stream anyway: segment flags only add a bonus, so a split word costs nothing beyond that bonus.
i1 = sheet.index("da loro"); i2 = sheet.index("se'l se")
spans = [sheet[:i1], sheet[i1:i2], sheet[i2:]]
if a.shift:
    spans = [spans[2], spans[0], spans[1]]
if a.shuffle_words is not None:
    rng = random.Random(a.shuffle_words)
    out = []
    for s in spans:
        w = s.split(); rng.shuffle(w); out.append(" ".join(w))
    spans = out

rows, codes, k = [], [], 0
CD = Path(a.cipher_dir) if a.cipher_dir else H
pile = {}
for (fol, span) in zip(("f178r", "f178v", "f179r"), spans):
    toks = []
    for r in csv.DictReader(open(CD / f"ciphertext_{fol}.tsv"), delimiter="\t"):
        s = r["sign"].strip()
        if s.startswith("P:"):
            if s not in pile:
                fam = s[2:].split("-")[0]
                pile[s] = (7000 if fam in WORD else 2000) + len(pile) + 1
            c = pile[s]
        elif s in WORD:
            c = 6000 + int(s[1:])
        elif re.fullmatch(r"T\d+", s):
            c = int(s[1:])
        else:
            k += 1; c = 1000 + k
        toks.append(str(c)); codes.append((c, s, fol, r["line"].split("_")[1], r["pos"], r["conf"]))
    rows.append((fol, span, fol, " ".join(toks)))
with open(a.out, "w") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["plain_line", "plain_raw", "cipher_line", "cipher_raw"])
    w.writerows(rows)
if a.codes:
    with open(a.codes, "w") as f:
        f.write("code\tsign_id\tfolio\tline\tpos\tconf\n")
        for c in codes:
            f.write("\t".join(map(str, c)) + "\n")
print(f"{sum(len(r[3].split()) for r in rows)} signs, {k} per-tile codes, plain letters "
      f"{sum(len(re.sub('[^a-z]', '', r[1].lower())) for r in rows)} -> {a.out}")
