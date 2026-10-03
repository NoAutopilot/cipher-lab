#!/usr/bin/env python3
"""Decode the mssEC 15 ledger pages that print/or_match.py did not match to the Official Records (GAPS113: 60 of 161
text pages; 59 re-fetched with text on 3 Oct 2026) with the dated key in key.md, and judge the result. GAPS132, 3 Oct 2026.

Usage: residue_decode.py PAGES_DIR [--write | --check]
  PAGES_DIR: <pointer>.json per page from https://hdl.huntington.org/digital/api/collections/p16003coll11/items/<pointer>/false
             (field "text": the Decoding the Civil War volunteer transcription, 2016-17, not reconciled against the image).
  Only pages absent from print/or_matches.tsv are read. Not committed: the page texts (their credit; re-fetch).
  --write rewrites print/residue/readings.md and print/residue/pages.tsv; --check exits 1 if either is stale.

Per entry (cut at blank lines; the date is the entry's own head line, else the last date seen on the page or before):
every key.md token is read by decode.py's dated rule and graded with its row's grade (C, I) or M (outside every
witness range, or two values covering the date: rule 4). Words not in key.md stay as written: most are clear words,
but a code word missing from key.md is indistinguishable from a clear English word (the vocabulary is ordinary
words), so the counts below are of key.md tokens only, plus `oov`, the tokens that are in no English corpus word list
(proper names, misspellings, or unknown code words) -- a lower bound on unread code, not a grade.
Judge: tools/judge_plaintext.py with specs/eckert-1862.json ("en": no 1860s corpus exists in tools/data; the en folds
spread 0.44-0.64, tools/data/en/README.md, so a FAIL/PASS is of unknown reliability). Control: the same pages decoded
with key.md's meanings permuted across its words (seeded), scored by the same judge, on (a) the whole text and (b) the
code-word windows (each key token's meaning with three words either side), the only part the permutation can move.
A page is 'reading ready' (for a separate verifier; not a status, not a novelty claim) when it carries >= 1 key token,
none graded M, and its decode passes the judge.
"""
import importlib.util, json, glob, os, re, sys, random, csv, io
from pathlib import Path

HERE = Path(__file__).resolve().parent
FOLDER = HERE.parent
REPO = FOLDER.parent.parent
spec_ = importlib.util.spec_from_file_location("decode", FOLDER / "decode.py"); dec = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(dec)
spec_ = importlib.util.spec_from_file_location("jp", REPO / "tools" / "judge_plaintext.py"); jp = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(jp)
_models = {}
_Ngram = jp.NgramModel
jp.NgramModel = lambda texts: _models.setdefault(id(jp), _Ngram(texts))  # one corpus per run: build the model once
SPEC = json.load(open(REPO / "specs" / "eckert-1862.json"))
OUT = HERE / "residue"
SEED = 1862


def matched():
    rows = (HERE / "or_matches.tsv").read_text().splitlines()[1:]
    return {int(r.split("\t")[0]) for r in rows if r.split("\t")[0].isdigit()}


def entries(text):
    return [e.strip() for e in re.split(r"\n\s*\n", text.replace("\r", "")) if e.strip()]


def vocab():
    ws = set()
    for p in list((REPO / "tools" / "data" / "en").glob("pg*.txt")) + [REPO / "tools/data/pg1661_holmes.txt", REPO / "tools/data/pg2701_mobydick.txt"]:
        ws |= set(re.findall(r"[a-z]+", p.read_text(errors="ignore").lower()))
    return ws


def windows(reading):
    w = reading.split()
    keep = set()
    for i, t in enumerate(w):
        if "[" in t or "]" in t:
            keep |= set(range(max(0, i - 3), i + 4))
    return " ".join(w[i] for i in sorted(keep) if i < len(w))


def run(pages_dir):
    key = dec.load_key()
    rng = random.Random(SEED)
    words = list(key)
    perm = [rows for rows in key.values()]
    rng.shuffle(perm)
    shuf = dict(zip(words, perm))  # each code word gets another word's rows (meanings, grades, dates)
    voc = vocab()
    skip = matched()
    pages, rd, ctl = [], [], []
    last = None
    for f in sorted(glob.glob(os.path.join(pages_dir, "*.json")), key=lambda x: int(os.path.basename(x)[:-5])):
        ptr = int(os.path.basename(f)[:-5])
        try:
            d = json.load(open(f))
        except Exception:
            continue
        text = (d.get("text") or "").strip()
        if ptr in skip or not text or ptr < 4956:
            continue
        cnt = {"C": 0, "I": 0, "M": 0}; oov = 0; ne = 0; first = None; prd, pct_ = [], []
        for e in entries(text):
            day = dec.parse_day(re.sub(r"\bApl\b", "Apr", e.splitlines()[0])) or last  # the ledger writes April "Apl"
            last = day or last
            first = first or day
            t = dec.entry_text(e.splitlines())
            r, c = dec.decode_entry(t, key, day)
            r2, _ = dec.decode_entry(t, shuf, day)
            for k, v in c.items():
                cnt[k] = cnt.get(k, 0) + v
            oov += sum(1 for w in re.findall(r"[A-Za-z]+", re.sub(r"\[[^\]]*\]|\{[^}]*\}", " ", r)) if w.lower() not in voc and len(w) > 1)
            ne += 1
            prd.append(f"*{day.strftime('%d %b') if day else 'undated'}*  {r}")
            pct_.append(r2)
        body = "\n\n".join(prd)
        plain = "\n".join(re.sub(r"\{[^}]*\}", " ", x.split("  ", 1)[1]) for x in prd)
        jr = jp.judge(SPEC, plain)["checks"]["language"]
        n_key = sum(cnt.values())
        ready = n_key >= 1 and cnt["M"] == 0 and jr["pass"]
        pages.append({"pointer": ptr, "page": d.get("title"), "first_date": first.strftime("%d %b 1862") if first else "",
                      "entries": ne, "C": cnt["C"], "I": cnt["I"], "M": cnt["M"], "oov": oov,
                      "judge": "PASS" if jr["pass"] else "FAIL", "score": jr["score"], "real_p05": jr["real_p05"],
                      "ready": "reading ready" if ready else ""})
        rd.append((ptr, d.get("title"), body))
        ctl.append("\n".join(re.sub(r"\{[^}]*\}", " ", x) for x in pct_))
    real_all = "\n".join(re.sub(r"\{[^}]*\}|\*[^*]*\*", " ", b) for _, _, b in rd)
    shuf_all = "\n".join(ctl)
    summary = {
        "real_full": jp.judge(SPEC, real_all)["checks"]["language"],
        "shuffled_key_full": jp.judge(SPEC, shuf_all)["checks"]["language"],
        "real_windows": jp.judge(SPEC, windows(real_all))["checks"]["language"],
        "shuffled_key_windows": jp.judge(SPEC, windows(shuf_all))["checks"]["language"],
    }
    return pages, rd, summary


def render(pages, rd, summary):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(pages[0]), delimiter="\t", lineterminator="\n")
    w.writeheader(); w.writerows(pages)
    tot = {k: sum(p[k] for p in pages) for k in ("entries", "C", "I", "M", "oov")}
    md = ["# mssEC 15 residue pages decoded with the dated key (GAPS132, 3 Oct 2026)", "",
          "Generated by `print/residue_decode.py` -- do not edit by hand. Source text: the Decoding the Civil War volunteer",
          "transcription (2016-17) on each Huntington Digital Library page record (p16003coll11), NOT reconciled against the",
          "image; code words in [brackets] read by key.md's dated rule, grade per pages.tsv. Thomas T. Eckert Papers, mssEC 15,",
          "The Huntington Library, San Marino, California. Telegrams in these pages were not found in OR ser. I vols. 7, 9-12 by",
          "print/or_match.py (GAPS113); that is a search result, not a novelty verdict (rule 10).", "",
          f"Pages {len(pages)}, entries {tot['entries']}; key.md tokens C {tot['C']}, I {tot['I']}, M {tot['M']}; oov {tot['oov']}.",
          "", "Judge (en corpus, fold caveat in the script docstring): " + "; ".join(
              f"{k} score {v['score']} vs real_p05 {v['real_p05']}, null_p99 {v['null_p99']} -> {'PASS' if v['pass'] else 'FAIL'} (N {v['N']})"
              for k, v in summary.items()), ""]
    for ptr, title, body in rd:
        md += [f"## {ptr} {title}", "", body, ""]
    return buf.getvalue(), "\n".join(md).rstrip() + "\n"


def main(argv):
    if not argv or argv[0].startswith("-"):
        print(__doc__); return 2
    pages, rd, summary = run(argv[0])
    tsv, md = render(pages, rd, summary)
    if "--write" in argv:
        OUT.mkdir(exist_ok=True)
        (OUT / "pages.tsv").write_text(tsv); (OUT / "readings.md").write_text(md)
        print("written", len(pages), "pages")
    elif "--check" in argv:
        ok = (OUT / "pages.tsv").read_text() == tsv and (OUT / "readings.md").read_text() == md
        print("residue readings are current" if ok else "residue readings are stale"); return 0 if ok else 1
    else:
        sys.stdout.write(tsv)
    print(json.dumps(summary, indent=1), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
