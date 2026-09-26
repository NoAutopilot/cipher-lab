#!/usr/bin/env python3
"""
NX-LAU3 (26 Sept 2026) known-answer gate: does BnF fr.3995 no.57's key table
reproduce fr.3625's own 12 gloss-attested code meanings (Bourdeau's
key_lauriere.txt, bourdeau_ref/)?

Real statistic: count of the 12 anchors whose key57 meaning matches
(exactly, or as the same word form for the M-graded multi-alternative
anchors) fr.3625's own established meaning for that code.

Control: 1000 shuffles of key57's own transcribed meanings over its own
codes (the numeral table separately from the name-symbol table, since they
are two structurally different lists on the same sheet), same statistic
recomputed each time. Reports mean, p99, max, so the real count can be
compared against chance.
"""
import random

random.seed(20260926)

# --- key57 numeral-table entries actually transcribed this session (see key57.tsv) ---
NUMERAL_POOL = {
    1: "ba", 15: "be", 29: "bi", 43: "bo",
    2: "ca", 16: "ce", 30: "ci", 44: "co",
    3: "da", 17: "de", 31: "di", 45: "do", 59: "du",
    4: "fa", 18: "fe", 32: "fi", 46: "fo",
    5: "ga", 19: "ge", 33: "gi", 47: "go",
    6: "la", 20: "le", 34: "li", 48: "lo",
    7: "ja", 21: "je", 35: "ji", 49: "jo",
    8: "ma", 22: "me", 36: "mi", 50: "mo",
    9: "na", 23: "ne", 37: "ni", 51: "no",
    10: "pa", 24: "pe", 38: "pi", 52: "po",
    11: "qua", 25: "que", 39: "qui", 53: "quo",
    12: "ra", 26: "re", 40: "ri", 54: "ro",
    13: "sa", 27: "se", 41: "si", 55: "so",
    14: "ta", 28: "te", 42: "ti", 56: "to",
    73: "cc", 74: "dd", 75: "ff", 78: "pp", 79: "ll", 80: "rr", 81: "ss",
    83: "bl", 84: "mn", 85: "nf", 88: "ns", 89: "ng", 90: "gl", 93: "pl",
    94: "by", 95: "cr",
    99: "a", 100: "aux", 101: "au", 102: "au", 103: "aussy", 104: "art",
    135: "bienfait", 136: "bout", 137: "bouclee",
    138: "commandement ou commande", 139: "capitule ou capitulation",
    140: "contente ou contentement", 141: "catholique",
    183: "estre", 184: "est",
    199: "favorise", 200: "fruit", 201: "fondz", 202: "font",
    203: "fault ou fait", 204: "faulte", 205: "fortifie", 206: "facilite",
    207: "formee", 208: "fascher", 209: "foulle", 210: "fantaisie",
    211: "fort", 212: "fentre ou fenestre",
    265: "mont", 274: "mont", 275: "moy", 276: "moua",
    277: "monde ou mesne", 278: "monde", 279: "morgue ou morgueur",
    280: "mal", 281: "malveuillance", 282: "mesdire ou mesdisant",
    283: "negligence", 284: "nouvelle", 285: "necessaire ou necessite",
    286: "non", 287: "nont", 288: "noua", 289: "nul", 290: "neant",
    297: "prisonnier", 298: "peyne",
    307: "quant", 308: "qualite",
    327: "france", 330: "sanct",
    335: "soit", 336: "suffisant ou suffisance", 337: "scavoir",
    338: "trouble", 339: "trouver",
    345: "escrit", 346: "volonte ou vouloir", 347: "vous", 348: "soir",
    353: "espagne ou espagnol",
}

# --- name/title symbol table on the same sheet (f201), left+right columns,
# counted from the full-page read: 38 left-column rows + 35 right-column
# rows = 73 distinct title -> symbol assignments; only one of them ("le
# pape ou sa saincteté") is "pape". We only need the count for the
# permutation (the XX code's chance of landing on "pape" by shuffle). ---
N_SYMBOL_TABLE = 73

def norm(s):
    s = s.lower().strip()
    for a, b in [("é", "e"), ("è", "e"), ("ê", "e"), ("ô", "o"), ("ç", "c"),
                 ("â", "a"), ("î", "i"), ("û", "u"), ("'", " "), ("-", " ")]:
        s = s.replace(a, b)
    return " ".join(s.split())

def alt_set(s):
    """Split an M-grade 'x ou y' / 'x/y' cell into its alternative word-forms."""
    s = norm(s)
    for sep in [" ou ", "/"]:
        if sep in s:
            return set(p.strip() for p in s.split(sep))
    return {s}

# anchors: (label, codes, target_alternatives, grade, combine)
# combine='any'  -> match if ANY code's meaning is in target
# combine='all'  -> match if ALL codes' meanings are in target (compounds)
ANCHORS = [
    ("335_le_roy",  [335], {"le roy"}, "C", "any"),
    ("141_soit",    [141], {"soit"}, "M", "any"),
    ("288_catholique", [288], {"catholique"}, "M", "any"),
    ("346_volonte", [346], {"volonte"}, "C", "any"),
    ("59_du",       [59],  {"du"}, "C", "any"),
    ("25_le_la_que",[25],  {"le", "la", "que"}, "M", "any"),
    ("26_a_de",     [26],  {"a", "de"}, "M", "any"),
    ("101_54_sa_majeste", [101, 54], {"sa", "majeste"}, "M", "all"),
    ("103_56_aussitost",  [103, 56], {"aussitost", "aussi", "tost"}, "M", "all"),
    ("184_auroit",  [184], {"auroit"}, "M", "any"),
    # XX and the que-mark are handled separately below (different pools).
]

def score_numeral(pool):
    """Count how many of the 10 numeral-pool anchors match under this pool."""
    hits = 0
    detail = {}
    for label, codes, targets, grade, combine in ANCHORS:
        vals = [alt_set(pool.get(c, "")) for c in codes]
        matched_each = [bool(v & targets) for v in vals]
        ok = all(matched_each) if combine == "all" else any(matched_each)
        detail[label] = ok
        if ok:
            hits += 1
    return hits, detail

# --- real statistic ---
real_numeral_hits, real_detail = score_numeral(NUMERAL_POOL)
real_XX = 1  # key57's XX = "le pape ou sa saincteté" -- exact match, both transcription passes agree
real_que_mark = 0  # no plain "X"/cross assigned to "que" found anywhere on the sheet (f201 full-page read, confirmed by the independent blind pass)
real_total = real_numeral_hits + real_XX + real_que_mark

print("=== REAL (unshuffled key57) ===")
for label, ok in real_detail.items():
    print(f"  {label}: {'MATCH' if ok else 'mismatch'}")
print(f"  XX (pape): MATCH")
print(f"  que-mark (✗): not present in key57 -- mismatch by construction")
print(f"REAL TOTAL: {real_total} / 12")
print()

# --- shuffle control ---
codes = list(NUMERAL_POOL.keys())
meanings = list(NUMERAL_POOL.values())
N_SHUFFLES = 1000
totals = []
for i in range(N_SHUFFLES):
    shuffled_meanings = meanings[:]
    random.shuffle(shuffled_meanings)
    shuffled_pool = dict(zip(codes, shuffled_meanings))
    numeral_hits, _ = score_numeral(shuffled_pool)
    xx_hit = 1 if random.randrange(N_SYMBOL_TABLE) == 0 else 0
    que_hit = 0  # the que-mark has no cell in either table under any permutation
    totals.append(numeral_hits + xx_hit + que_hit)

totals.sort()
mean = sum(totals) / len(totals)
p99 = totals[int(0.99 * len(totals)) - 1]
mx = totals[-1]

print("=== SHUFFLE CONTROL (1000 shuffles of key57's own meanings over its own codes) ===")
print(f"mean={mean:.3f}  p99={p99}  max={mx}")
print()
print("=== GATE ===")
print(f"target={real_total}  need >=6 AND above shuffle max ({mx})")
gate_pass = real_total >= 6 and real_total > mx
print("GATE PASS" if gate_pass else "GATE FAIL")
