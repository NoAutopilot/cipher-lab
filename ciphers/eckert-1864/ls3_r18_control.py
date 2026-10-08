#!/usr/bin/env python3
"""LS3-R18 (8 Oct 2026): book assignment and matched control for the mssEC 18 entries filed 8 Oct 2026.

For each entry: (a) vocabulary shares (tokens found in key.md / key-no2.md / key-no9.md); (b) under each of the three
books, does the decoded time word equal the ledger's own time in the header line (and the decoded month/day the date
in the header)?  (c) the same two checks under 200 meaning-shuffled copies of each book (meanings permuted among
rows of the same kind: time rows among time rows, numeral rows among numeral rows, word rows among word rows;
seed fixed per book).  The shuffle CAN differ from the real book on these statistics (it moves the time and numeral
rows), so it is a control in rule 3's sense; it does not score grammar (the clause counts are by hand, NOTES).
Usage: python3 ls3_r18_control.py            # print the table
       python3 ls3_r18_control.py --write    # write ls3_r18_readings.md (the chosen-book decodes of the entries above)
       python3 ls3_r18_control.py --check    # exit 1 if ls3_r18_readings.md differs from what is derived now (rule 7)
"""
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import decode  # noqa: E402

BOOKS = {"1": ("key.md", "ciphertext.txt"), "2": ("key-no2.md", "ciphertext-no2.txt"), "9": ("key-no9.md", "ciphertext-no9.txt")}
ENTRIES = {"E78": "1", "N2-BP": "2", "N2-BQ": "2", "O9-BA": "9", "O9-BB": "9",
           "E79": "1", "E80": "1", "E81": "1", "E82": "1", "E83": "1", "E84": "1",
           # LS3-R18b (8 Oct 2026): E85/E87 carry neither a ledger book label nor a testable time word -> key not in hand, listed for the
           # statistics only and left out of ls3_r18_readings.md (NOT_CLAIMED); E86 book 1 (time word), O9-BC book 9 (ledger "9" + time word)
           "E85": "1", "E86": "1", "E87": "1", "O9-BC": "9"}
NOT_CLAIMED = {"E85", "E87"}
SEEDS = 200


def norm_time(s):
    m = re.search(r"(\d{1,2})(?:[.:](\d\d))?\s*([AP])\.?\s*M", s, re.I)
    if not m:
        m = re.fullmatch(r"\s*(12)\s*", s)  # the key's "12" (noon) carries no am/pm
        return "12.00 PM" if m else None
    return f"{int(m.group(1))}.{m.group(2) or '00'} {m.group(3).upper()}M"


def shuffled(key, seed):
    rng = random.Random(seed)
    by_kind = {}
    for w, (m, g, k) in key.items():
        by_kind.setdefault(k, []).append(w)
    out = {}
    for k, ws in by_kind.items():
        if k == "numeral":  # a few numeral rows carry a non-numeric meaning ("number"): left in place
            ws = [w for w in ws if key[w][0].split()[0].isdigit()]
        vals = [key[w] for w in ws]
        rng.shuffle(vals)
        for w, v in zip(ws, vals):
            out[w] = v
    return out


def load_entries():
    ents = {}
    for book, (_, ct) in BOOKS.items():
        for header, lines in decode.load_ciphertext(HERE / ct):
            eid = header.split(" |")[0].strip()
            if eid in ENTRIES:
                ents[eid] = (header, lines)
    return ents


def checks(text, key, hdr_time, hdr_date):
    reading, _ = decode.decode_entry(text, key)
    t = re.findall(r"\{time: ([^}]*)\}", reading)
    d = re.findall(r"\{date: ([^}]*)\}", reading)
    time_ok = hdr_time is not None and bool(t) and norm_time(t[0]) == hdr_time
    date_ok = None if hdr_date is None else (bool(d) and d[0].strip() == hdr_date)
    return time_ok, date_ok


def main():
    keys = {b: decode.load_key(HERE / kf) for b, (kf, _) in BOOKS.items()}
    ents = load_entries()
    print("entry | chosen | tokens | share k1/k2/k9 | time-word agrees with header (book 1/2/9) | shuffled chosen book: time agrees / date agrees (of %d; NT = the header has no hour, not testable)" % SEEDS)
    for eid, chosen in ENTRIES.items():
        header, lines = ents[eid]
        text = decode.entry_text(lines)
        hdr_line = lines[0]
        hdr_time = norm_time(hdr_line)
        mdate = re.search(r"(Apr)\w*\.?\s+(\d{1,2})", hdr_line)
        hdr_date = f"April {int(mdate.group(2))}" if mdate else None
        toks = [re.sub(r"[^a-z]", "", t.lower()) for t in text.split()]
        toks = [t for t in toks if t]
        share = "/".join(str(sum(t in keys[b] for t in toks)) for b in "129")
        real = ["Y" if checks(text, keys[b], hdr_time, hdr_date)[0] else ("n" if hdr_time else "NT") for b in "129"]
        dates = ["Y" if checks(text, keys[b], hdr_time, hdr_date)[1] else "n" for b in "129"]
        tc = dc = 0
        for s in range(SEEDS):
            ok_t, ok_d = checks(text, shuffled(keys[chosen], 1000 + s), hdr_time, hdr_date)
            tc += ok_t
            dc += bool(ok_d)
        print(f"{eid} | book {chosen} | {len(toks)} | {share} | time {'/'.join(real)} date {'/'.join(dates)} | {tc} / {dc}")


def readings():
    keys = {b: decode.load_key(HERE / kf) for b, (kf, _) in BOOKS.items()}
    ents = load_entries()
    parts = []
    for eid, chosen in ENTRIES.items():
        if eid in NOT_CLAIMED:
            continue
        header, lines = ents[eid]
        reading, counts = decode.decode_entry(decode.entry_text(lines), keys[chosen])
        g = ", ".join(f"{k} {v}" for k, v in counts.items() if v)
        parts.append(f"**{header}** (book {chosen})\n\n{reading}\n\nCode-word tokens: {g or 'none'}.\n")
    return "\n".join(parts)


if __name__ == "__main__":
    out = HERE / "ls3_r18_readings.md"
    if "--write" in sys.argv:
        out.write_text(readings(), encoding="utf-8")
        print("ls3_r18_readings.md written")
    elif "--check" in sys.argv:
        if not out.exists() or out.read_text(encoding="utf-8") != readings():
            sys.stderr.write("ls3_r18_readings.md is stale\n")
            sys.exit(1)
        print("ls3_r18_readings.md is current")
    else:
        main()
