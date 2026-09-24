#!/usr/bin/env python3
"""Exclude neighbour-record pairs that a solver project already works, by volume as well as by id.

Usage: python3 tools/decode_neighbours_exclude.py PAIRS_TSV BOURDEAU_CLONE AYMELOGLU_CLONE > annotated.tsv

Lesson of 23 Sept 2026: matching Bourdeau's profiles by DECODE id alone missed the Pallotto cluster, because
his folder cites the sibling volume's ids. So every shelfmark on both sides is reduced to volume keys
("brah 9/31", "bav barb.lat 6956", "bl add ms 32657", "bnf français 3096", "asna busta 2337", ...) and a pair
is flagged when any Bourdeau folder or Aymeloglu tracker line shares a volume key or an id with it.
Output: the input rows plus columns bourdeau_id_hit, bourdeau_volume_hit, aym_id_hit, aym_volume_hit,
queue_hit, and a final verdict column: "excluded:<reason>" or "survives".
"""
import csv, glob, json, os, re, sys, unicodedata

def ids_in(s):
    out = set(re.findall(r"\bR\d{1,5}\b", s))
    for a, b in re.findall(r"\bR(\d{1,5})\s*[-–]\s*R?(\d{1,5})\b", s):
        lo, hi = int(a), int(b)
        if 0 < hi - lo < 80:
            out |= {f"R{i}" for i in range(lo, hi + 1)}
    return out

def _fold_accents(s):
    """Strip combining diacritics (Mélanges/Melanges, Français/Francais, ...) so shelfmark text from
    different transcribers/scrapers normalises to the same ASCII form before the volume-key regexes run.
    Lesson of 24 Sept 2026: DC6/DC9's census rows held_by 'none' though Bourdeau's NOTES.md names them,
    because 'Mélanges de Colbert' (accented) never matched 'Melanges'/'Mél.' (unaccented or abbreviated)."""
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))

def volume_keys(s):
    s = _fold_accents(s)
    s = s.replace("_", " ").replace("-", " ").replace(".", ". ").lower()
    s = re.sub(r"\s+", " ", s)
    k = set()
    for m in re.findall(r"(?:signatura|salazar(?: y castro)?,?|a )\s*(?:a\s*)?9\s*/\s*(\d{1,3})", s): k.add(f"brah 9/{m}")
    for m in re.findall(r"\b9\s*/\s*(\d{1,3})\b", s):
        if "brah" in s or "rah" in s or "salazar" in s: k.add(f"brah 9/{m}")
    for m in re.findall(r"barb\.?\s*lat\.?\s*(\d{3,5})", s): k.add(f"bav barb.lat {m}")
    for m in re.findall(r"add(?:itional)?\.? ?ms\.? ?(\d{3,6})", s): k.add(f"bl add ms {m}")
    for m in re.findall(r"harley(?:an)? ?ms\.? ?(\d{2,5})", s): k.add(f"bl harley ms {m}")
    for m in re.findall(r"sloane ?ms\.? ?(\d{2,5})", s): k.add(f"bl sloane ms {m}")
    for m in re.findall(r"stowe ?ms\.? ?(\d{2,5})", s): k.add(f"bl stowe ms {m}")
    for m in re.findall(r"(?:cotton(?: ms)?|cott\.?)\s*(caligula|vespas?ian|vespanian|galba|nero|otho|titus|julius|tiberius|claudius|domitian|faustina|augustus|cleopatra)\.?,?\s*([a-e])\.?,?\s*([ivx]+)", s):
        fam = m[0].replace("vespanian", "vespasian"); k.add(f"bl cotton {fam} {m[1]} {m[2]}")
    for m in re.findall(r"(?:francais|fr\.|fr |french\s*(?:mss?|manuscripts?)?\s*)\s*(\d{3,5})", s): k.add(f"bnf français {m}")
    for m in re.findall(r"(?:espagnol|esp\.)\s*(\d{2,4})", s): k.add(f"bnf espagnol {m}")
    for m in re.findall(r"(?:italien|ital\.)\s*(\d{2,5})", s): k.add(f"bnf italien {m}")
    for m in re.findall(r"clairambault\s*(\d{2,4})", s): k.add(f"bnf clairambault {m}")
    for m in re.findall(r"mel(?:anges?)?\.?\s*(?:de\s*)?colbert\.?\s*(\d{1,4})", s): k.add(f"bnf melanges colbert {m}")
    for m in re.findall(r"busta\s*(\d{1,5})", s): k.add(f"busta {m}")
    for m in re.findall(r"affari\.? ?esteri\.? ?(\d{2,5})", s): k.add(f"busta {m}")
    for m in re.findall(r"\bsp ?(\d{1,3})\s*/\s*(\d{1,4})", s): k.add(f"tna sp {m[0]}/{m[1]}")
    for m in re.findall(r"\bpro ?(\d{1,3})\s*/\s*(\d{1,4})", s): k.add(f"tna pro {m[0]}/{m[1]}")
    for m in re.findall(r"(?:estado|est\.),? ?(?:leg\.?|legajo) ?(\d{1,5})", s): k.add(f"ags estado leg {m}")
    for m in re.findall(r"(?:segr(?:eteria|\.)? ?(?:di )?stato,? ?)?(spagna|francia|germania|venezia|napoli|fiandra|portogallo|polonia|savoia)\s*(\d{1,4})", s): k.add(f"asv sds {m[0]} {m[1]}")
    for m in re.findall(r"sds ?(spagna|francia|germania|venezia|napoli|fiandra|portogallo|polonia|savoia)", s): k.add(f"asv sds {m}")
    for m in re.findall(r"i ?1025 ?sds ?(\w+)", s): k.add(f"asv sds {m}")
    for m in re.findall(r"g ?15 caps\.? ?([a-z])\.? ?fasc\.? ?(\d{1,4})", s): k.add(f"mnl g15 caps {m[0]} fasc {m[1]}")
    for m in re.findall(r"mss?/?(\d{3,6})", s):
        if "bne" in s or "biblioteca nacional" in s: k.add(f"bne mss {m}")
    for m in re.findall(r"asve.*?b(?:usta)?\.? ?(\d{1,4})", s): k.add(f"asve busta {m}")
    return k

def build_bourdeau_index(bour):
    """folder -> (ids, volume keys, class), from every */profile.json (+ NOTES.md head)."""
    bidx = {}
    for prof in glob.glob(os.path.join(bour, "*", "profile.json")):
        folder = os.path.basename(os.path.dirname(prof))
        try: p = json.load(open(prof, encoding="utf-8"))
        except Exception: continue
        blob = json.dumps(p, ensure_ascii=False)
        notes = os.path.join(os.path.dirname(prof), "NOTES.md")
        head = open(notes, encoding="utf-8", errors="replace").read(3000) if os.path.exists(notes) else ""
        shelf = " | ".join(d.get("shelfmark", "") for d in p.get("documents", [])) + " | " + p.get("title", "") + " | " + head
        o = p.get("outcome") if isinstance(p.get("outcome"), dict) else {}
        bidx[folder] = (ids_in(blob), volume_keys(shelf), str(o.get("class", "?")))
    return bidx

def build_aymeloglu_lines(aym):
    """[(relpath, line), ...] from TARGETS/SHORTLIST/README/CATALOGUE/ranked .md files."""
    alines = []
    for fp in glob.glob(os.path.join(aym, "**", "*.md"), recursive=True):
        if re.search(r"(TARGETS|SHORTLIST|README|CATALOGUE|ranked)", os.path.basename(fp)):
            for ln in open(fp, encoding="utf-8", errors="replace"):
                alines.append((os.path.relpath(fp, aym), ln.strip()))
    return alines

def main():
    pairs_tsv, bour, aym = sys.argv[1:4]
    bidx = build_bourdeau_index(bour)
    alines = build_aymeloglu_lines(aym)

    queue = open("QUEUE.md", encoding="utf-8").read()
    queue_ids = ids_in(queue); queue_vols = volume_keys(queue)

    rows = list(csv.DictReader(open(pairs_tsv, encoding="utf-8"), delimiter="\t"))
    fields = list(rows[0].keys()) + ["bourdeau_id_hit", "bourdeau_volume_hit", "aym_id_hit", "aym_volume_hit", "queue_hit", "verdict"]
    w = csv.DictWriter(sys.stdout, fieldnames=fields, delimiter="\t"); w.writeheader()
    for r in rows:
        my_ids = {("R" + x.lstrip("Rr")) for x in (r["id"], r["neighbour_id"]) if x}
        my_vols = volume_keys(r["shelfmark"])
        if re.fullmatch(r"\d{3,5}", r["shelfmark"].strip()):  # bare BnF-style number in the scrape
            my_vols |= {f"bnf français {r['shelfmark'].strip()}"}
        bid = sorted(f"{f}[{c}]" for f, (ids, vols, c) in bidx.items() if my_ids & ids)
        bvol = sorted(f"{f}[{c}]" for f, (ids, vols, c) in bidx.items() if my_vols & vols and not (my_ids & ids))
        aid = sorted({rel for rel, ln in alines if my_ids & ids_in(ln)})
        avol = sorted({rel for rel, ln in alines if my_vols & volume_keys(ln)})
        qh = "id" if my_ids & queue_ids else ("volume" if my_vols & queue_vols else "")
        if bid: v = "excluded:bourdeau-id"
        elif bvol: v = "excluded:bourdeau-volume"
        elif aid: v = "excluded:aymeloglu-id"
        elif qh == "id": v = "excluded:queue-id"
        else: v = "survives" + (":queue-volume" if qh else "") + (":aym-volume" if avol else "")
        r.update({"bourdeau_id_hit": ";".join(bid), "bourdeau_volume_hit": ";".join(bvol), "aym_id_hit": ";".join(aid), "aym_volume_hit": ";".join(avol), "queue_hit": qh, "verdict": v})
        w.writerow(r)

if __name__ == "__main__":
    main()
