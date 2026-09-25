#!/usr/bin/env python3
"""Per-correspondent-block sign inventory for the fr5761 election-embassy key (25 Sept 2026, LANE R8).

Counts alphabet/name-code/null rows per block from the single blind pass key_passB.tsv (all seven
leaves, sections alphabet/names/nulls/other) and cross-checks which sign_code values recur for the
same referent across the two atlas-coded, 3-pass-reconciled blocks in key.tsv (f104, f110) -- the
only leaves with a majority-voted sign_code column to compare. Regenerates sign_inventory.tsv.
"""
import csv
from collections import defaultdict

PASSB = "key_passB.tsv"
KEYTSV = "key.tsv"
OUT = "sign_inventory.tsv"

blocks = defaultdict(lambda: {"alphabet": 0, "names": 0, "nulls": 0, "other": 0, "leaf": None, "correspondent": None})

with open(PASSB, encoding="utf-8") as f:
    r = csv.DictReader(f, delimiter="\t")
    for row in r:
        leaf = row["canvas"]
        corr = row["correspondent"].strip()
        section = row["section"].strip()
        if not corr:
            continue  # the one 'other' row per leaf is the shared document heading, not a block
        key = (leaf, corr)
        blocks[key]["leaf"] = leaf
        blocks[key]["correspondent"] = corr
        if section in ("alphabet", "names", "nulls", "other"):
            blocks[key][section] += 1

# Shared-sign check: same plain referent, same non-UNLISTED sign_code, across different leaves,
# using only the atlas-coded majority key (key.tsv: f104, f110).
# Normalise cross-leaf spelling variants of the same referent (each correspondent's code list
# names the same set of electors/places/persons independently, so spelling drifts pass to pass:
# f104 "Mugance."/f110 "Maguence" = Mainz/Mayence, f104 "Le conte palatin"/f110 "Palatin" = the
# Palatine elector, f104 "Treues"/f110 "Treves" = Trier, f104 "Francisque"/f110 "Francisme" =
# the same name read two ways, f104 "Catholicque"/f110 "Catholicquer" = the same title).
REFERENT_ALIAS = {
    "mugance": "mainz", "maguence": "mainz",
    "le conte palatin": "palatine elector", "palatin": "palatine elector",
    "treues": "treves", "treves": "treves",
    "francisque": "francis(que/me)", "francisme": "francis(que/me)",
    "catholicque": "catholicque(r)", "catholicquer": "catholicque(r)",
}


def norm(plain):
    key = plain.strip().rstrip(".").lower()
    return REFERENT_ALIAS.get(key, key)


plain_to_leaf_code = defaultdict(dict)
with open(KEYTSV, encoding="utf-8") as f:
    r = csv.DictReader(f, delimiter="\t")
    for row in r:
        if row["section"] != "correspondent":
            continue
        code = row["sign_code"].split("|")[0].strip()
        if not code or code == "UNLISTED":
            continue
        plain_to_leaf_code[norm(row["plain"])][row["leaf"]] = code

shared = []
differ = []
for plain, leafcodes in plain_to_leaf_code.items():
    if len(leafcodes) > 1:
        codes = set(leafcodes.values())
        if len(codes) == 1:
            shared.append((plain, leafcodes))
        else:
            differ.append((plain, leafcodes))

NOTE = {
    ("f104", "A monsieur Cordier et Sr de la Motheaugroing"):
        "design: own alphabet a-x (23 letters, y/z unresolved) + 4 nulls + 8 code-names for the same referent set (elector Palatine, Treves, Mainz, Brandenburg, Saxony, Poulougne, Hongrie, Francisque) + Catholicque",
    ("f105", "A monsieur de Langsac"):
        "own block within f105, not yet atlas-coded; f105 leaf carries TWO correspondent blocks back to back, not one",
    ("f105", "A monsieur de la Boulade devers monsieur de Trèves"):
        "second block on the same leaf (f105), immediately after Langsac's; not yet atlas-coded",
    ("f106", "A monsieur de Lagnisay"): "alphabet count 21 (2 short of the usual ~23) in this single blind pass -- unreconciled, may be a missed/merged letter, not yet checked against the image",
    ("f107", "Joachim de Moltzan tenant le marquis de Brandebourg"): "18 code-name rows, largest name list of any block -- not yet atlas-coded",
    ("f108", "Tanquam ad summum pardonems le duc de Saxe"): "heading itself garbled/uncertain in this blind pass (Latin tag, not yet resolved against the image); not yet atlas-coded",
    ("f109", "Le grand archediacre de [Gand] devers le legat qui est en Allemaigne"): "not yet atlas-coded",
    ("f110", "Maistre [Jehan] de Bourdeaulx devers le marquis de Brandebourg"):
        "design: own alphabet a-y (23 letters) + 4 nulls + 12 code-names for the same referent set as f104, plus England and Marguerite of Austria; Mainz shares f104's K34 (same sign), Saxony does not (K20 vs f104's K15)",
}

with open(OUT, "w", encoding="utf-8") as out:
    out.write("leaf\tcorrespondent\talphabet_signs\tcode_name_signs\tnulls\tother\ttotal\tgrade\tnote\n")
    for (leaf, corr), c in sorted(blocks.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        total = c["alphabet"] + c["names"] + c["nulls"] + c["other"]
        grade = "H (key.tsv, 3-pass atlas-coded majority)" if leaf in ("f104", "f110") else "M (key_passB.tsv, single free-text blind pass, not yet atlas-coded/reconciled)"
        note = NOTE.get((leaf, corr), "")
        out.write(f"{leaf}\t{corr}\t{c['alphabet']}\t{c['names']}\t{c['nulls']}\t{c['other']}\t{total}\t{grade}\t{note}\n")

print("Blocks:", len(blocks))
print("Shared sign_code across leaves for the same referent (key.tsv only):")
for plain, leafcodes in shared:
    print(" SAME:", plain, dict(leafcodes))
print("Different sign_code across leaves for the same referent (key.tsv only):")
for plain, leafcodes in differ:
    print(" DIFF:", plain, dict(leafcodes))
