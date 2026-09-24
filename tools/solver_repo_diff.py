#!/usr/bin/env python3
"""Diff QUEUE.md, or a DECODE census TSV, against fresh clones of the two solver repositories.

Two modes:

1. Queue mode (original, no flags): for every QUEUE.md row (Tier A-C tables) it extracts DECODE ids
   (R\\d+ / DECRYPT n) and shelfmark phrases (Add MS n, Harley MS n, Cotton X, SP n/n, MS n), then
   reports every Bourdeau target folder whose profile.json, NOTES.md or transcription names one of
   them (with its `status.class` and `fraction_read`), and every Aymeloglu catalogue/TARGETS/SHORTLIST
   line naming one.

       python3 tools/solver_repo_diff.py BOURDEAU_CLONE AYMELOGLU_CLONE > out.tsv

2. Census mode (--census, added 24 Sept 2026, LANE N): for every row of a DECODE RecordsList census
   TSV (tools/decode_list.py's output columns: id, status, record_type, holder_raw, city,
   shelfmark_code, date_range, ...), decides who already holds it: a cipher-lab target folder
   (`ours:<folder>`, or `ours:queue`/`ours:catalog` if only QUEUE.md/CATALOG.md names it), a Bourdeau
   target folder (`bourdeau:<folder>`), an Aymeloglu target folder or tracker line (`aymeloglu:<path>`),
   or `none`. Reuses tools/decode_neighbours_exclude.py's `ids_in`/`volume_keys` (id = DECODE record
   id as "R<id>"; volume = archive+shelfmark reduced to a normalised key, e.g. "bnf français 3040" --
   the same matching this project already validated on the 23 Sept 2026 neighbour-record sweep) so a
   DECODE id and a shelfmark are both checked, not just one.

       python3 tools/solver_repo_diff.py --census CENSUS_TSV --out OUT_TSV BOURDEAU_CLONE AYMELOGLU_CLONE

Both modes: scripts read, models judge -- the output is hits to check, not verdicts. Bourdeau: MIT code,
CC BY 4.0 text. Aymeloglu: no licence, cite only.
"""
import argparse, csv, glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode_neighbours_exclude import ids_in, volume_keys, build_bourdeau_index, build_aymeloglu_lines

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
    else:
        run_queue_mode(args.bourdeau_clone, args.aymeloglu_clone, args.queue)


if __name__ == "__main__":
    main()
