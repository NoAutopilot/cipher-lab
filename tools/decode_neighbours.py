#!/usr/bin/env python3
"""Find DECODE catalogue pairs where a Non-decrypted cipher record shares a
shelfmark with a Decrypted or Partially decrypted record (the Randolph
f.277/f.278 pattern, LESSONS.md 23 September 2026).

Inputs (read-only, from the aaymeloglu/unsolved-ciphers clone):
    ay/catalogue/decode-catalog.csv    -- full DECODE catalogue dump (10,106 rows,
                                           id, c_holder, c_cates, c_author, c_lang,
                                           record_type, status, number_of_pages, url)
    ay/catalogue/decode-records.jsonl  -- richer fields (Sender, Receiver, Region,
                                           Origin City, Start Year/Month/Day, Symbol
                                           Set, Plaintext Language, notes) but only
                                           for Cipher-type Non-decrypted / Partially
                                           decrypted rows (1,187 of the 10,106).

The catalogue's c_holder / Holder string ends, in the great majority of rows, with
a machine-generated code with no internal spaces, e.g.
    "British Library, Cotton MS Caligula C II. f 277. BL_Cotton_MS_Caligula_C_II_277"
Splitting that trailing code on "_" and popping a final numeric-ish segment
("277", "278-279", "6956-41" ...) gives a shelfmark key ("BL_Cotton_MS_Caligula_C_II")
plus a folio/item locator -- exactly the Randolph R4931/R4932 case (folios 277
and 278-279 under the same shelfmark key). Rows whose c_holder has no such
trailing code (about 1% of Cipher rows) fall back to the whole holder text as an
opaque shelfmark key with no folio.

Output: sources/solver-diffs/2026-09-23-decode-neighbours.tsv, one row per
Non-decrypted record that has a same-shelfmark Decrypted/Partially decrypted
neighbour (by adjacent folio, a same-year-or-closer date, or a shared sender+
recipient), or whose own title/notes name a decipherment keyword.
"""
import csv
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRATCH = Path(
    "/tmp/claude-0/-home-user-cipher-lab/9923d5e8-abb3-5917-8998-01d84bdb57a2/scratchpad"
)
CSV_PATH = SCRATCH / "ay" / "catalogue" / "decode-catalog.csv"
JSONL_PATH = SCRATCH / "ay" / "catalogue" / "decode-records.jsonl"
OUT_PATH = REPO / "sources" / "solver-diffs" / "2026-09-23-decode-neighbours.tsv"

TARGET_LANGS = ("english", "french", "italian", "spanish", "latin")
KEYWORDS = [
    "decipher", "deciphered", "decrypt", "clear", "key",
    "chiave", "cifra e chiaro", "déchiffr",
]

FOLIO_RE = re.compile(r"^\d+[a-z]?(?:-\d+[a-z]?)?$", re.I)
VOL_ITEM_RE = re.compile(r"^(\d{3,})-(\d{1,4}[a-z]?)$", re.I)

# Populated by build_vol_prefix_counts() before any normalise_shelfmark()
# call. Some archives (BAV "Barb.lat NNNN") put the manuscript/volume number
# directly before a hyphenated item number ("Barb.lat_6956-19"); popping the
# whole "6956-19" as a folio (correct for a genuine two-folio range such as
# Cotton Caligula's "278-279") would silently drop the volume number from
# the shelfmark key and falsely group Barb.lat 6956 with the unrelated
# Barb.lat 6960. The two are told apart by recurrence: a real volume number
# used as an item prefix (6956) recurs across several sibling records in the
# catalogue, where a genuine folio-range's first half (278 in "278-279")
# does not recur as a hyphen-prefix anywhere else under the same shelfmark.
# This is a heuristic over catalogue metadata, not a guarantee -- see the
# caveats in the output.
VOL_PREFIX_COUNTS = {}


def build_vol_prefix_counts(csv_path):
    counts = {}
    with open(csv_path, encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f)
        for row in r:
            if row["record_type"] != "Cipher":
                continue
            toks = (row["c_holder"] or "").split()
            if not toks:
                continue
            last = toks[-1].rstrip(".,;")
            if "_" not in last:
                continue
            parts = last.split("_")
            prefix = "_".join(parts[:-1]).lower()
            vi = VOL_ITEM_RE.match(parts[-1])
            if vi:
                key = (prefix, vi.group(1))
                counts[key] = counts.get(key, 0) + 1
    return counts


def load_jsonl():
    """id -> dict of extra fields, Cipher / Non-decrypted+Partially decrypted only."""
    out = {}
    with open(JSONL_PATH, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            out[d["id"]] = d
    return out


def parse_lang(c_lang, jsonl_lang):
    """Return the first of TARGET_LANGS found in either field, else ''."""
    hay = f"{c_lang or ''} {jsonl_lang or ''}".lower()
    for lang in TARGET_LANGS:
        if lang in hay:
            return lang.capitalize()
    return ""


def build_bare_number_set(csv_path):
    """Trailing all-digit codes (no hyphen) seen anywhere in the Cipher rows,
    e.g. the "6960" in ".._Barb.lat_6960". See BARE_NUMS docstring above."""
    bare = set()
    with open(csv_path, encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f)
        for row in r:
            if row["record_type"] != "Cipher":
                continue
            toks = (row["c_holder"] or "").split()
            if not toks:
                continue
            last = toks[-1].rstrip(".,;")
            if "_" not in last:
                continue
            seg = last.split("_")[-1]
            if re.match(r"^\d+$", seg):
                bare.add(seg.lstrip("0") or "0")
    return bare


def normalise_shelfmark(holder):
    """Return (shelfmark_key, folio_raw_or_None)."""
    holder = (holder or "").strip()
    if not holder:
        return "", None
    toks = holder.split()
    last = toks[-1]
    if "_" not in last:
        # no machine code found; fall back to the whole string, punctuation
        # and a trailing "f. NNN" style locator stripped, as a best effort.
        base = re.sub(r"[,.]", " ", holder.lower())
        base = re.sub(r"\bf{1,2}ol?s?\.?\s*\d+[a-z]?(-\d+[a-z]?)?\b", " ", base)
        base = re.sub(r"\s+", " ", base).strip()
        return base, None
    raw_code = last.rstrip(".,;")
    parts = raw_code.split("_")
    folio = None
    if parts:
        last_seg = parts[-1]
        prefix = "_".join(parts[:-1]).lower()
        vi = VOL_ITEM_RE.match(last_seg)
        if vi and VOL_PREFIX_COUNTS.get((prefix, vi.group(1)), 0) >= 2:
            # "NNNN-MM": NNNN recurs as an item-number prefix under this same
            # shelfmark elsewhere in the catalogue, so it is the volume
            # number, not a folio -- keep it in the shelfmark and only pop
            # the item/folio half.
            parts[-1] = vi.group(1)
            folio = vi.group(2)
        elif FOLIO_RE.match(last_seg):
            folio = parts.pop()
    shelfmark_key = "_".join(parts).lower()
    if not shelfmark_key:
        shelfmark_key = raw_code.lower()
    return shelfmark_key, folio


def folio_int(folio_raw):
    if not folio_raw:
        return None
    m = re.match(r"^(\d+)", folio_raw)
    return int(m.group(1)) if m else None


def parse_year(cates, jsonl_rec):
    if jsonl_rec and jsonl_rec.get("Start Year"):
        try:
            return int(jsonl_rec["Start Year"])
        except ValueError:
            pass
    m = re.search(r"\d{4}", cates or "")
    return int(m.group(0)) if m else None


def parse_mmdd(jsonl_rec):
    """(month, day) ints from jsonl Start Month/Day, else (None, None)."""
    if not jsonl_rec:
        return None, None
    try:
        mo = int(jsonl_rec.get("Start Month") or 0) or None
    except ValueError:
        mo = None
    try:
        da = int(jsonl_rec.get("Start Day") or 0) or None
    except ValueError:
        da = None
    return mo, da


DATE_CODE_RE = re.compile(r"(\d{4})[-_](\d{2})[-_](\d{2})")


def parse_date_from_code(holder):
    m = DATE_CODE_RE.search(holder or "")
    if not m:
        return None
    y, mo, da = (int(x) for x in m.groups())
    return (y, mo, da)


def date_ordinal(y, mo, da):
    import datetime

    try:
        return datetime.date(y, mo or 1, da or 1).toordinal()
    except ValueError:
        return None


def parse_sender_receiver(csv_row, jsonl_rec):
    if jsonl_rec:
        sender = jsonl_rec.get("Sender") or jsonl_rec.get("Author") or ""
        receiver = jsonl_rec.get("Receiver") or ""
        if sender or receiver:
            return sender, receiver
    # csv c_author is "<name> <Region> <City>"; strip a trailing "Region City"
    # tail heuristically is not reliable, so just keep the raw field as sender.
    return (csv_row.get("c_author") or "").strip(), ""


def name_key(s):
    """Crude surname-ish key for loose sender/receiver matching."""
    s = (s or "").lower()
    s = re.sub(r"[^a-z\s]", " ", s)
    words = [w for w in s.split() if len(w) > 2]
    return words[-1] if words else ""


def keyword_hits(text):
    hay = (text or "").lower()
    return [kw for kw in KEYWORDS if kw in hay]


def main():
    if not CSV_PATH.exists() or not JSONL_PATH.exists():
        print(f"missing input files under {SCRATCH}", file=sys.stderr)
        return 1

    global VOL_PREFIX_COUNTS
    VOL_PREFIX_COUNTS = build_vol_prefix_counts(CSV_PATH)
    jsonl = load_jsonl()

    records = []  # unified record dicts, Cipher type only
    with open(CSV_PATH, encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f)
        for row in r:
            if row["record_type"] != "Cipher":
                continue
            status = row["status"]
            if status not in ("Decrypted", "Partially decrypted", "Non-decrypted"):
                continue
            rid = row["id"]
            jrec = jsonl.get(rid)
            holder = (jrec.get("Holder") if jrec and jrec.get("Holder") else None) or row["c_holder"]
            shelfmark_key, folio_raw = normalise_shelfmark(row["c_holder"])  # csv always has the code
            year = parse_year(row["c_cates"], jrec)
            month, day = parse_mmdd(jrec)
            if month is None and day is None:
                coded = parse_date_from_code(row["c_holder"])
                if coded:
                    year, month, day = coded
            sender, receiver = parse_sender_receiver(row, jrec)
            language = parse_lang(row["c_lang"], jrec.get("Plaintext Language") if jrec else "")
            notes = ""
            if jrec:
                notes = " ".join(
                    str(jrec.get(k, "")) for k in
                    ("Cipher Type (notes)", "Symbol Sets (notes)")
                )
            title_text = f"{holder} {notes}"
            rec = {
                "id": rid,
                "holder_raw": holder,
                "shelfmark_key": shelfmark_key,
                "folio_raw": folio_raw,
                "folio_int": folio_int(folio_raw),
                "year": year,
                "month": month,
                "day": day,
                "sender": sender.strip(),
                "receiver": receiver.strip(),
                "sender_key": name_key(sender),
                "receiver_key": name_key(receiver),
                "language": language,
                "status": status,
                "pages": (jrec.get("No. of Pages") if jrec else "") or row["number_of_pages"],
                "url": row["url"],
                "title_text": title_text,
                "keywords": keyword_hits(title_text),
            }
            records.append(rec)

    by_shelfmark = {}
    for rec in records:
        by_shelfmark.setdefault(rec["shelfmark_key"], []).append(rec)

    out_rows = []
    for shelfmark_key, group in by_shelfmark.items():
        if not shelfmark_key:
            continue
        non_decr = [r for r in group if r["status"] == "Non-decrypted"]
        neighbours = [r for r in group if r["status"] in ("Decrypted", "Partially decrypted")]
        if not non_decr:
            continue
        for nd in non_decr:
            if nd["language"].lower() not in TARGET_LANGS:
                continue
            if not nd["holder_raw"] or nd["holder_raw"].strip() in ("", "?"):
                continue
            best = None
            best_reason = None
            for nb in neighbours:
                if nb["id"] == nd["id"]:
                    continue
                reasons = []
                # adjacent folio
                if nd["folio_int"] is not None and nb["folio_int"] is not None:
                    diff = abs(nd["folio_int"] - nb["folio_int"])
                    if diff <= 3:
                        reasons.append(f"adjacent folio (f.{nd['folio_raw']} vs f.{nb['folio_raw']}, diff {diff})")
                # date within ~30 days
                if nd["year"] and nb["year"]:
                    o1 = date_ordinal(nd["year"], nd["month"], nd["day"])
                    o2 = date_ordinal(nb["year"], nb["month"], nb["day"])
                    if o1 and o2 and abs(o1 - o2) <= 30 and (nd["month"] or nb["month"]):
                        reasons.append(f"date within {abs(o1 - o2)} days")
                # same sender & recipient
                if nd["sender_key"] and nd["sender_key"] == nb["sender_key"]:
                    if nd["receiver_key"] and nd["receiver_key"] == nb["receiver_key"]:
                        reasons.append("same sender & recipient")
                    else:
                        reasons.append("same sender (author) named")
                if reasons:
                    # prefer the strongest: folio-adjacency+sender beats a lone match
                    score = len(reasons) + (2 if any("adjacent folio" in x for x in reasons) else 0)
                    if best is None or score > best[0]:
                        best = (score, nb)
                        best_reason = "; ".join(reasons)
            if best:
                nb = best[1]
                out_rows.append({
                    "id": nd["id"], "shelfmark": shelfmark_key, "folio": nd["folio_raw"] or "",
                    "date": "-".join(str(x) for x in (nd["year"], nd["month"], nd["day"]) if x) or (str(nd["year"]) if nd["year"] else ""),
                    "sender": nd["sender"], "recipient": nd["receiver"], "language": nd["language"],
                    "status": nd["status"], "neighbour_id": nb["id"], "neighbour_folio": nb["folio_raw"] or "",
                    "neighbour_date": "-".join(str(x) for x in (nb["year"], nb["month"], nb["day"]) if x) or (str(nb["year"]) if nb["year"] else ""),
                    "neighbour_status": nb["status"], "why_matched": best_reason,
                })
            elif nd["keywords"]:
                out_rows.append({
                    "id": nd["id"], "shelfmark": shelfmark_key, "folio": nd["folio_raw"] or "",
                    "date": str(nd["year"]) if nd["year"] else "",
                    "sender": nd["sender"], "recipient": nd["receiver"], "language": nd["language"],
                    "status": nd["status"], "neighbour_id": "", "neighbour_folio": "",
                    "neighbour_date": "", "neighbour_status": "",
                    "why_matched": "own title/notes contains: " + ", ".join(nd["keywords"]),
                })

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    cols = ["id", "shelfmark", "folio", "date", "sender", "recipient", "language",
            "status", "neighbour_id", "neighbour_folio", "neighbour_date",
            "neighbour_status", "why_matched"]
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(cols)
        for row in out_rows:
            w.writerow([row[c] for c in cols])

    print(f"wrote {len(out_rows)} rows to {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
