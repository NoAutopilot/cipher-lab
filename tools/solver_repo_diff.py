#!/usr/bin/env python3
"""Diff QUEUE.md, or a DECODE census TSV, against fresh clones of the two solver repositories.

Two modes:

1. Queue mode (original, no flags): for every QUEUE.md row (Tier A-C tables) it extracts DECODE ids
   (R\\d+ / DECRYPT n) and shelfmark phrases (Add MS n, Harley MS n, Cotton X, SP n/n, MS n), then
   reports every Bourdeau target folder whose profile.json, NOTES.md or transcription names one of
   them (with its `status.class` and `fraction_read`), and every Aymeloglu catalogue/TARGETS/SHORTLIST
   line naming one.

       python3 tools/solver_repo_diff.py BOURDEAU_CLONE AYMELOGLU_CLONE > out.tsv

2. Register mode (--register REGISTER_TSV, added 27 Sept 2026, RETRO-2026-09-27x P3): for every row of a
   register with `archive`, `shelfmark` and `folios` columns (KEY-ADJACENT.tsv), reduce archive+shelfmark
   to volume keys (decode_neighbours_exclude.volume_keys, which normalises fr./français, Clair./
   Clairambault, Colbert/Mélanges de Colbert/500 de Colbert, Baluze, Dupuy and NAF onto one form each,
   plus its existing forms) and DECODE ids (ids_in), and the row's own folios/item numbers to a set of
   folio tokens. Grep fresh Bourdeau profile.json+NOTES.md and Aymeloglu TARGETS/SHORTLIST/README/
   catalogue lines -- including catalog/decode-catalog.csv -- for a volume-key or id match, and print
   `none` (no match anywhere), `partial` (the volume/id matches but no folio or item number in the row is
   confirmed in the matching source -- a shelfmark-only match licenses nothing about which items are
   covered, this section's own headline paragraph 3 lesson), or `full-reading` (a folio/item number or a
   DECODE id matches too), with the matching path.

       python3 tools/solver_repo_diff.py --register KEY-ADJACENT.tsv BOURDEAU_CLONE AYMELOGLU_CLONE

3. Census mode (--census, added 24 Sept 2026, LANE N): for every row of a DECODE RecordsList census
   TSV (tools/decode_list.py's output columns: id, status, record_type, holder_raw, city,
   shelfmark_code, date_range, ...), decides who already holds it: a cipher-lab target folder
   (`ours:<folder>`, or `ours:queue`/`ours:catalog` if only QUEUE.md/CATALOG.md names it), a Bourdeau
   target folder (`bourdeau:<folder>`), an Aymeloglu target folder or tracker line (`aymeloglu:<path>`),
   or `none`. Reuses tools/decode_neighbours_exclude.py's `ids_in`/`volume_keys` (id = DECODE record
   id as "R<id>"; volume = archive+shelfmark reduced to a normalised key, e.g. "bnf français 3040" --
   the same matching this project already validated on the 23 Sept 2026 neighbour-record sweep) so a
   DECODE id and a shelfmark are both checked, not just one.

       python3 tools/solver_repo_diff.py --census CENSUS_TSV --out OUT_TSV BOURDEAU_CLONE AYMELOGLU_CLONE

All modes: scripts read, models judge -- the output is hits to check, not verdicts. Bourdeau: MIT code,
CC BY 4.0 text. Aymeloglu: no licence, cite only.
"""
import argparse, csv, glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode_neighbours_exclude import ids_in, volume_keys, build_bourdeau_index, build_aymeloglu_lines

FOLIO_RE = re.compile(r"\bf(?:olio|ol)?\.?\s*(\d+\s*[rv]?)\b|\bno\.?\s*(\d+)\b", re.I)


def folio_tokens(s):
    """Folio/item numbers a register row (or a solver-repo blob) names, e.g. {'321', '333'} from
    'f.321 (June 1586), f.333 (10 July 1586)' or {'58'} from 'f.81 (no.58)'. Used only to tell a
    volume-level match ('partial') from a match that also confirms the specific item ('full-reading')."""
    out = set()
    for m in FOLIO_RE.finditer(s or ""):
        tok = (m.group(1) or m.group(2) or "").replace(" ", "").lower()
        if tok:
            out.add(tok)
    return out

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def queue_rows(queue_path):
    q = open(queue_path, encoding="utf-8").read()
    rows = []
    for line in q.split("\n"):
        m = re.match(r"\| (\d+) \| (.+?) \| (.+?) \|", line)
        if m:
            rows.append((int(m.group(1)), m.group(2)))
    return rows


def keys(name):
    ks = set(re.findall(r"\bR\d{2,5}\b", name))
    for a, b in re.findall(r"\b(R\d{2,5})-(R\d{2,5})\b", name):
        lo, hi = int(a[1:]), int(b[1:])
        if hi - lo < 60:
            ks |= {f"R{i}" for i in range(lo, hi + 1)}
    ks |= {"DECRYPT " + x for x in re.findall(r"DECRYPT (\d+)", name)}
    ks |= set(re.findall(r"(?:Add(?:itional)?|Harley|Harleian|Cotton|Egerton|Lansdowne|Stowe) MS \d+", name))
    ks |= set(re.findall(r"Caligula [A-E] ?[IVX]+", name))
    ks |= set(re.findall(r"SP ?\d{1,3}/\d{1,4}", name))
    ks |= set(re.findall(r"PRO ?\d{1,3}/\d{1,4}", name))
    ks |= set(re.findall(r"GD\d+/\d+/\d+", name))
    return {k.replace("Additional", "Add") for k in ks}


def norm(s):
    return re.sub(r"\s+", " ", s.replace("Additional", "Add").replace("Harleian", "Harley"))


def run_queue_mode(bour, aym, queue_path=os.path.join(ROOT, "QUEUE.md")):
    rows = queue_rows(queue_path)

    bidx = {}
    for prof in glob.glob(os.path.join(bour, "*", "profile.json")):
        d = os.path.dirname(prof)
        try:
            p = json.load(open(prof, encoding="utf-8"))
        except Exception:
            continue
        st = p.get("outcome") if isinstance(p.get("outcome"), dict) else (p.get("status") if isinstance(p.get("status"), dict) else {})
        blob = norm(json.dumps(p, ensure_ascii=False))
        for extra in ("NOTES.md",):
            fp = os.path.join(d, extra)
            if os.path.exists(fp):
                blob += " " + norm(open(fp, encoding="utf-8", errors="replace").read()[:20000])
        bidx[os.path.basename(d)] = (str(st.get("class", p.get("class", "?"))), str(st.get("fraction_read", p.get("fraction_read", "?"))), blob)

    alines = []
    for fp in glob.glob(os.path.join(aym, "**", "*"), recursive=True):
        if os.path.isfile(fp) and re.search(r"(TARGETS|SHORTLIST|README|catalog|catalogue).*\.(md|jsonl|csv|json)$", fp) and os.path.getsize(fp) < 5_000_000:
            rel = os.path.relpath(fp, aym)
            for ln in open(fp, encoding="utf-8", errors="replace"):
                alines.append((rel, norm(ln.strip())))

    print("rank\tqueue_row\tkeys\tbourdeau_hits\taymeloglu_hits")
    for rank, name in rows:
        ks = keys(name)
        bh = []
        for folder, (cls, frac, blob) in bidx.items():
            hit = [k for k in ks if re.search(r"\b" + re.escape(k) + r"\b", blob)]
            if hit:
                bh.append(f"{folder}[{cls};{frac};{','.join(sorted(hit)[:3])}]")
        ah = []
        for rel, ln in alines:
            hit = [k for k in ks if re.search(r"\b" + re.escape(k) + r"\b", ln)]
            if hit:
                ah.append(f"{rel}:{ln[:90]}")
        print(f"{rank}\t{name[:90]}\t{';'.join(sorted(ks))[:80]}\t{' | '.join(sorted(bh))[:400]}\t{' | '.join(ah[:3])[:300]}")


def build_bourdeau_register_index(bour):
    """folder -> (ids, vols, folio tokens) from every */profile.json (+ full NOTES.md, not just the
    3000-char head census mode uses -- a register row's folio may be named only deep in NOTES.md)."""
    idx = {}
    for prof in glob.glob(os.path.join(bour, "*", "profile.json")):
        folder = os.path.basename(os.path.dirname(prof))
        try:
            p = json.load(open(prof, encoding="utf-8"))
        except Exception:
            continue
        notes_fp = os.path.join(os.path.dirname(prof), "NOTES.md")
        notes = open(notes_fp, encoding="utf-8", errors="replace").read() if os.path.exists(notes_fp) else ""
        blob = json.dumps(p, ensure_ascii=False) + " " + notes
        idx[folder] = (ids_in(blob), volume_keys(blob), folio_tokens(blob))
    return idx


def build_aymeloglu_register_lines(aym):
    """[(relpath, line), ...] from TARGETS/SHORTLIST/README/CATALOGUE/catalog files, .md or .csv --
    register mode's own extension over build_aymeloglu_lines() (24 Sept 2026 census mode), which only
    reads .md files and would miss catalog/decode-catalog.csv (RETRO-2026-09-27x P3)."""
    lines = []
    for fp in glob.glob(os.path.join(aym, "**", "*"), recursive=True):
        name = os.path.basename(fp)
        if os.path.isfile(fp) and re.search(r"(targets|shortlist|readme|catalogue|catalog)", name, re.I) \
                and name.lower().endswith((".md", ".csv", ".jsonl", ".json")):
            for ln in open(fp, encoding="utf-8", errors="replace"):
                lines.append((os.path.relpath(fp, aym), ln.rstrip("\n")))
    return lines


def register_verdict(vols, ids, ftoks, bidx, alines):
    """none / partial / full-reading (with the matching path) for one register row's own (vols, ids,
    ftoks) against a Bourdeau index and Aymeloglu lines -- see the register-mode docstring above."""
    best = ("none", "")
    for folder, (bids, bvols, bftoks) in bidx.items():
        if ids & bids or vols & bvols:
            path = f"bourdeau:{folder}"
            if (ids & bids) or (ftoks & bftoks):
                return "full-reading", path
            if best[0] == "none":
                best = ("partial", path)
    for rel, ln in alines:
        lvols, lids = volume_keys(ln), ids_in(ln)
        if not (ids & lids or vols & lvols):
            continue
        path = f"aymeloglu:{rel}"
        if (ids & lids) or (ftoks & folio_tokens(ln)):
            return "full-reading", path
        if best[0] == "none":
            best = ("partial", path)
    return best


def run_register_mode(register_path, bour, aym):
    bidx = build_bourdeau_register_index(bour)
    alines = build_aymeloglu_register_lines(aym)
    with open(register_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    print("line\tshelfmark\tverdict\tpath")
    for i, r in enumerate(rows, start=2):  # data rows start at TSV line 2 (line 1 is the header)
        haystack = " ".join(r.get(c, "") for c in ("archive", "shelfmark", "folios"))
        vols, ids = volume_keys(haystack), ids_in(haystack)
        ftoks = folio_tokens(r.get("folios", ""))
        verdict, path = register_verdict(vols, ids, ftoks, bidx, alines)
        print(f"{i}\t{r.get('shelfmark', '')[:60]}\t{verdict}\t{path}")


def build_ours_index(repo_root):
    """folder -> (ids, vols) from every ciphers/<t>/{NOTES.md,AUDIT.md}, plus a synthetic
    'queue' and 'catalog' entry for QUEUE.md/CATALOG.md themselves."""
    oidx = {}
    for d in sorted(glob.glob(os.path.join(repo_root, "ciphers", "*"))):
        if not os.path.isdir(d):
            continue
        blob = ""
        for fn in ("NOTES.md", "AUDIT.md"):
            fp = os.path.join(d, fn)
            if os.path.exists(fp):
                blob += " " + open(fp, encoding="utf-8", errors="replace").read()
        if blob.strip():
            oidx[os.path.basename(d)] = (ids_in(blob), volume_keys(blob))
    for fn, tag in ((os.path.join(repo_root, "QUEUE.md"), "queue"), (os.path.join(repo_root, "CATALOG.md"), "catalog")):
        if os.path.exists(fn):
            blob = open(fn, encoding="utf-8", errors="replace").read()
            oidx[tag] = (ids_in(blob), volume_keys(blob))
    return oidx


def census_row_keys(row):
    my_ids = {"R" + row["id"].strip()} if row.get("id", "").strip().isdigit() else set()
    hay = " | ".join(row.get(c, "") for c in ("holder_raw", "shelfmark_code", "city"))
    my_vols = volume_keys(hay)
    sm = row.get("shelfmark_code", "")
    m = re.search(r"BNF_Fran[cç]ais_(\d{3,5})", sm, re.I)
    if m:
        my_vols.add(f"bnf français {m.group(1)}")
    return my_ids, my_vols


def run_census_mode(census_path, out_path, bour, aym, repo_root=ROOT):
    oidx = build_ours_index(repo_root)
    bidx = build_bourdeau_index(bour)
    alines = build_aymeloglu_lines(aym)

    with open(census_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    fields = list(rows[0].keys()) if rows else []
    fields += ["ours_hit", "bourdeau_hit", "aymeloglu_hit", "held_by"]
    with open(out_path, "w", encoding="utf-8", newline="") as out:
        w = csv.DictWriter(out, fieldnames=fields, delimiter="\t")
        w.writeheader()
        counts = {"ours": 0, "bourdeau": 0, "aymeloglu": 0, "none": 0}
        for r in rows:
            my_ids, my_vols = census_row_keys(r)

            o_hit = sorted(f for f, (ids, vols) in oidx.items() if my_ids & ids or my_vols & vols)
            b_hit = sorted(f"{f}[{c}]" for f, (ids, vols, c) in bidx.items() if my_ids & ids or my_vols & vols)
            a_hit = sorted({rel for rel, ln in alines if my_ids & ids_in(ln) or my_vols & volume_keys(ln)})

            if o_hit:
                held = "ours:" + o_hit[0]
                counts["ours"] += 1
            elif b_hit:
                held = "bourdeau:" + b_hit[0].split("[")[0]
                counts["bourdeau"] += 1
            elif a_hit:
                held = "aymeloglu:" + sorted(a_hit)[0]
                counts["aymeloglu"] += 1
            else:
                held = "none"
                counts["none"] += 1

            r["ours_hit"] = ";".join(o_hit)
            r["bourdeau_hit"] = ";".join(b_hit)
            r["aymeloglu_hit"] = ";".join(a_hit)
            r["held_by"] = held
            w.writerow(r)
    return counts


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--census", help="DECODE census TSV (tools/decode_list.py output) to diff, row by row")
    ap.add_argument("--register", help="register TSV with archive/shelfmark/folios columns (KEY-ADJACENT.tsv) to diff, row by row")
    ap.add_argument("--out", help="output TSV path (census mode only; required with --census)")
    ap.add_argument("--queue", default=os.path.join(ROOT, "QUEUE.md"), help="QUEUE.md path (default: repo root)")
    ap.add_argument("bourdeau_clone", help="path to a shallow clone of dbourdeau/cyphersolver")
    ap.add_argument("aymeloglu_clone", help="path to a shallow clone of aaymeloglu/unsolved-ciphers")
    args = ap.parse_args()

    if args.census:
        if not args.out:
            ap.error("--census requires --out")
        repo_root = os.path.dirname(os.path.abspath(args.queue))
        counts = run_census_mode(args.census, args.out, args.bourdeau_clone, args.aymeloglu_clone, repo_root)
        total = sum(counts.values())
        print(f"{total} rows -> ours {counts['ours']}, bourdeau {counts['bourdeau']}, "
              f"aymeloglu {counts['aymeloglu']}, none {counts['none']}", file=sys.stderr)
    elif args.register:
        run_register_mode(args.register, args.bourdeau_clone, args.aymeloglu_clone)
    else:
        run_queue_mode(args.bourdeau_clone, args.aymeloglu_clone, args.queue)


if __name__ == "__main__":
    main()
