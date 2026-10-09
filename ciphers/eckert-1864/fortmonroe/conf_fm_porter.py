#!/usr/bin/env python3
"""CONF-FM Part B (9 Oct 2026, account 1, for LANE LEDGER): known-plaintext key test, grade C, NOT a reading.

Four Fort Monroe ledger entries of 8 Dec 1864 (Huntington mssEC 25, pointers 5820 entries 2-3 and 5821 entries 1-2,
transcription eye-checked against line crops by CONF-FM; text in conf_fm_porter_entries.txt) carry four telegrams of
Rear-Admiral D. D. Porter printed in ORN ser. I vol. 11 pp.155-156 (archive.org officialrecordso0011unse). Each code word
the decoder treats as a word/numeral/name is hand-aligned (ALIGN below, fixed BEFORE any score was computed) to the printed
word(s) it stands in for. Score = aligned code words whose Cipher No. 1 meaning (key.md via decode.load_key / lookup)
matches the printed word. Control (rule 3; the ledger's existing method, fm_r4a.py's meaning-shuffled No. 1, here over
--seeds seeds): the same score with the key's word/numeral meanings permuted across code words.
Punctuation, signature and time words (no printed counterpart: the print gives receipt times) are not scored.
Usage: python3 conf_fm_porter.py [--seeds 1000]   (writes nothing; output pasted to conf_fm_porter.out)"""
import argparse, random, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); import decode

# (entry, code word as written, printed word(s) it stands for -- all must match)
ALIGN = [
 ("P1", "paddle", ["8"]), ("P1", "polkaer", ["commander"]), ("P1", "polkaing", ["commanding"]), ("P1", "torch", ["of", "the"]),
 ("P1", "orbit", ["at", "the"]), ("P1", "pagan", ["battery"]), ("P1", "Niagara", ["porter"]),
 ("P2", "Farmer", ["norfolk"]), ("P2", "polkaer", ["commander"]), ("P2", "peach", ["2"]),
 ("P2", "towers", ["monitors"]),          # "money towers" = "moni-tors" by sound in the print; the key has Tower = Over the
 ("P2", "Windhams", ["roads"]), ("P2", "blubber", ["city", "point"]), ("P2", "niagara", ["porter"]),
 ("P3", "polkaer", ["commander"]), ("P3", "Windsor", ["river"]), ("P3", "polkaers", ["commanders"]), ("P3", "saddle", ["guard"]),
 ("P3", "vespers", ["positions"]), ("P3", "staggers", ["lights"]),
 ("P3", "tulip", ["."]),                   # print: a full stop ("show no lights. Arm the tugs")
 ("P3", "niggard", ["arm"]), ("P3", "polkaer", ["commander"]), ("P3", "torch", ["of", "the"]), ("P3", "shallow", ["guard"]),
 ("P3", "blubber", ["city", "point"]), ("P3", "wrangle", ["telegraph"]), ("P3", "whites", ["reports"]), ("P3", "black", ["city", "point"]),
 ("P3", "torch", ["of", "the"]), ("P3", "wreathe", ["telegraph"]), ("P3", "Niagara", ["porter"]),
 ("P4", "Jersey", ["grant"]), ("P4", "blubber", ["city", "point"]), ("P4", "tulip", ["."]), ("P4", "perfume", ["3"]),
 ("P4", "sharons", ["gunboats"]), ("P4", "Windsor", ["river"]),
 ("P4", "Pagan", ["pagan"]),               # print: "Pagan Creek", a place name (plain); key Pagan = Battery
 ("P4", "Ragged", ["ragged"]),             # print: "Ragged Island Creek" (plain); key Ragged = Front
 ("P4", "Smyrna", ["island"]), ("P4", "Vernon", ["point"]), ("P4", "saddle", ["guard"]), ("P4", "waltz", ["surprise"]),
 ("P4", "melody", ["60"]), ("P4", "plaster", ["5"]),   # "65 rebel sailors"
 ("P4", "federal", ["10"]), ("P4", "trance", ["near"]),
 ("P4", "Pagans", ["pagan"]),              # print: "near Pagan Creek"
 ("P4", "Galway", ["richmond"]), ("P4", "spit", ["men"]), ("P4", "Niagara", ["porter"]),
]

def stem(w):  # trailing s dropped (first run scored "Road"/"roads" and "Arms"/"arm" as misses: a matcher artefact, disclosed in NOTES)
    w = w[:-1] if len(w) > 3 and w.endswith("s") else w
    return w[:5]

def meaning_words(key, word):
    core, end, row = decode.lookup(word, key)
    if row is None: return None
    m = re.sub(r"\(.*?\)", " ", row[0].lower())
    return [stem(w) for w in re.findall(r"[a-z]+|\d+", m)]

def match(key, word, printed):
    mw = meaning_words(key, word)
    if mw is None: return False
    return all(stem(p) in mw for p in printed if p != ".") and any(p != "." for p in printed)

def score(key): return [match(key, w, p) for _, w, p in ALIGN]

def shuffled(key, seed):
    rows = [k for k, v in key.items() if v[2] in ("word", "numeral")]
    vals = [key[k] for k in rows]; random.Random(seed).shuffle(vals)
    out = dict(key); out.update(zip(rows, vals)); return out

def main():
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--seeds", type=int, default=1000); a = ap.parse_args()
    key = decode.load_key(HERE / "key.md")
    s = score(key); n = len(ALIGN)
    print(f"aligned code words: {n} (P1 {sum(e=='P1' for e,_,_ in ALIGN)}, P2 {sum(e=='P2' for e,_,_ in ALIGN)}, "
          f"P3 {sum(e=='P3' for e,_,_ in ALIGN)}, P4 {sum(e=='P4' for e,_,_ in ALIGN)})")
    print(f"Cipher No. 1 key: {sum(s)} of {n} read to the printed word")
    for (e, w, p), ok in zip(ALIGN, s):
        if not ok:
            mw = decode.lookup(w, key)[2]; print(f"  miss {e} {w!r}: key {mw[0] if mw else None!r}, print {' '.join(p)!r}")
    ctrl = sorted(sum(score(shuffled(key, sd))) for sd in range(a.seeds))
    print(f"shuffled-key control ({a.seeds} seeds): mean {sum(ctrl)/len(ctrl):.2f}, p99 {ctrl[int(0.99*len(ctrl))]}, max {ctrl[-1]}")
    sys.exit(0 if sum(s) > ctrl[-1] else 1)

if __name__ == "__main__":
    main()
