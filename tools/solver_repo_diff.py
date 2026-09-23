#!/usr/bin/env python3
"""Diff QUEUE.md against fresh clones of the two solver repositories.

Usage: python3 tools/solver_repo_diff.py BOURDEAU_CLONE AYMELOGLU_CLONE > out.tsv

For every queue row (Tier A-C tables) it extracts DECODE ids (R\\d+ / DECRYPT n) and shelfmark phrases
(Add MS n, Harley MS n, Cotton X, SP n/n, MS n), then reports every Bourdeau target folder whose
profile.json, NOTES.md or transcription names one of them (with its `status.class` and `fraction_read`),
and every Aymeloglu catalogue/TARGETS/SHORTLIST line naming one. Scripts read, models judge: the output
is hits to check, not verdicts. Bourdeau: MIT code, CC BY 4.0 text. Aymeloglu: no licence, cite only.
"""
import json, os, re, sys, glob

bour, aym = sys.argv[1], sys.argv[2]
q = open("QUEUE.md", encoding="utf-8").read()
rows = []
for line in q.split("\n"):
    m = re.match(r"\| (\d+) \| (.+?) \| (.+?) \|", line)
    if m:
        rows.append((int(m.group(1)), m.group(2)))

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

# Bourdeau index: folder -> (class, fraction, text blob)
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

# Aymeloglu index: lines from catalogue and tracker files
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
