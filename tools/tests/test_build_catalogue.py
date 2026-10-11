#!/usr/bin/env python3
"""Offline test for tools/build_catalogue.py (CATALOGUE-SITE-1, 9 Oct 2026). Fixture rows, all two audits:
  A  N4, D2, recovered passages, register line with a job name in brackets  -> listed, job name gone, safe sentence quoted
  B  N3, D1                                                                 -> listed under fragments read
  C  N2, D2                                                                 -> not listed (below N3)
  R  N4, D2, folder debosnys-x                                              -> never listed (restricted)
Must catch: a job name or session id surviving into a page; a counted row missing; an output path under docs/.
Must NOT block: shelfmarks and edition references with capitals and hyphens ("OR I/32 pt 3", "KHA A 11/XIV B/41-42",
"WVO 5797") survive sanitize().
Safe-sentence matcher (READINGS-PUBLIC, 11 Oct 2026), on a fixture AUDIT.md for a three-item folder:
  must catch -- a group template ("Safe sentence for each:", "(all)") or a sentence with a placeholder ("<print, page>", "[or: ...]");
  a sibling's labelled sentence (another E-number in its bullet); a sentence stating N1 for an N3 row; a sentence whose depth words
  ("partially deciphered") rank above a D1 row; an over-claiming register line (replaced by the depth note); a D4 title phrase on a
  D2 row; "ASKS row N" and credential variable names in a register sentence.
  must NOT block -- the row's own labelled sentence (its E-number in the bullet), a table row whose "safe sentence" column carries the
  item's own sentence, the later of two own sentences when both fit, and a single-item folder's sentence that names no id.
Run: python3 tools/tests/test_build_catalogue.py"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build_catalogue as bc  # noqa: E402


def row(title, folder, **f):
    r = {"title": title, "kind": "recovery", "grade": "N4", "date": "5 Oct 2026", "line": "x",
         "link": "https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/" + folder,
         "document_id": "doc " + title, "claim_scope": "recovered-passages", "plaintext_novelty": "N4",
         "mapping_novelty": "N4", "audit_status": "two audits", "depth": "D2", "depth_pct": 40.0,
         "depth_sentence": "The writer names the Landgrave.", "key": "period", "superseded_by": ""}
    r.update(f)
    return r


fails = 0


def check(cond, msg):
    global fails
    if not cond:
        fails += 1
        print("FAIL:", msg)


# sanitize: must catch / must not block
s = bc.sanitize("Partially deciphered (about 67%; D2, DEPTH-MH 8 Oct 2026). Read by AUDIT2-MANT and N8-GRA2 for session_01AbC; "
                "LANE AX (owner account) round 3: OR I/32 pt 3 p.498, KHA A 11/XIV B/41-42, WVO 5797. A check-solved worker made it.")
for bad in ("DEPTH-MH", "AUDIT2-MANT", "N8-GRA2", "session_", "LANE", "worker"):
    check(bad not in s, f"sanitize left {bad!r}: {s}")
for good in ("OR I/32 pt 3 p.498", "KHA A 11/XIV B/41-42", "WVO 5797", "We made it"):
    check(good in s, f"sanitize removed {good!r}: {s}")

with tempfile.TemporaryDirectory() as tmp:
    os.makedirs(os.path.join(tmp, "tools"))
    for f in ("build_dashboard.py", "build_catalogue.py"):
        shutil.copy(os.path.join(ROOT, "tools", f), os.path.join(tmp, "tools"))
    results = [row("Alpha to Beta, WVO 5797", "alpha", line="Partially deciphered (R9-MANTV 6 Oct 2026). Reading: in WVO 5797 two blanks read in part under a period "
                                                       "table; no prior decipherment of these blanks located"),
               row("Bravo fragments", "bravo", depth="D1", plaintext_novelty="N3", grade="N3"),
               row("Charlie", "charlie", plaintext_novelty="N2", grade="N2"),
               row("Restricted", "debosnys-x")]
    json.dump({"results": results, "targets": [{"status": "open"}, {"status": "blocked"}]},
              open(os.path.join(tmp, "status.json"), "w"))
    for fold, st in (("alpha", "partial"), ("bravo", "solved"), ("charlie", "open"), ("debosnys-x", "open")):
        os.makedirs(os.path.join(tmp, "ciphers", fold))
        open(os.path.join(tmp, "ciphers", fold, "NOTES.md"), "w").write(f"# {fold}\n\n{st}\n")
    open(os.path.join(tmp, "ciphers", "alpha", "AUDIT.md"), "w").write(
        "# AUDIT\n\n**Unsafe sentence.** \"The first decipherment of Alpha to Beta, never printed before anywhere at all.\"\n\n"
        "**Safe sentence.** \"In WVO 5797 (Alpha to Beta) two blanks read in part under a period table; no prior decipherment "
        "of these blanks located (VERIFY-X).\"\n")
    p = subprocess.run([sys.executable, "tools/build_catalogue.py", "--out", "out", "--mockup", "mock.html",
                        "--mockup-items", "WVO 5797"], cwd=tmp, capture_output=True, text=True, timeout=60)
    check(p.returncode == 0, f"builder exit {p.returncode}: {p.stderr[-400:]}")
    pages = glob.glob(os.path.join(tmp, "out", "items", "*.html"))
    check(len(pages) == 2, f"expected 2 item pages (A, B), got {len(pages)}")
    idx = open(os.path.join(tmp, "out", "index.html")).read()
    check("Charlie" not in idx and "Restricted" not in idx, "N2 or restricted row listed")
    check("2 targets in work" in idx, "open/blocked targets not reduced to a count")
    allhtml = idx + "".join(open(x).read() for x in pages) + open(os.path.join(tmp, "mock.html")).read()
    check(not re.search(r"R9-MANTV|VERIFY-X|session_", allhtml), "job name survived into a page")
    check("two blanks read in part" in allhtml, "safe sentence not quoted from AUDIT.md")
    check("first decipherment" not in allhtml, "unsafe sentence quoted")
    check("<script src" not in allhtml and "<link" not in allhtml and "<img" not in allhtml, "page carries a remote script, stylesheet or embedded image")
    check("fragments read" in open([x for x in pages if "bravo" in x][0]).read(), "D1 row not worded 'fragments read'")
    p2 = subprocess.run([sys.executable, "tools/build_catalogue.py", "--out", "docs/catalogue"], cwd=tmp,
                        capture_output=True, text=True, timeout=60)
    check(p2.returncode != 0 and not os.path.exists(os.path.join(tmp, "docs")), "docs/ output not refused")


# ---- safe-sentence matcher (READINGS-PUBLIC, 11 Oct 2026): fixture AUDIT.md, three Eckert-like rows in one folder
AUD = """# AUDIT

| ID | N |
|---|---|
| E1 | N1 |

All 2: **N1**, key `period`. Safe sentence for each: "The ledger copy reads, with the period book, to the text printed in <print, page>
and nowhere else that we searched."

- **E2: N1.** Safe sentence: "Read with the period book against the clear copy (pointer 10490), whose plain text is in the holder's
  public transcription; our reading is an independent re-decipherment."
- **E3: N3.** Safe sentence: "Read at grade H with the period book: on 6 Oct 1864 the operator at City Point tells Fort Monroe that
  the railroad is to be extended two miles; not located in print."
- **E3: N3.** Safe sentence: "Read at grade H with the period book: on 6 Oct 1864 the operator at City Point tells Fort Monroe that
  the railroad is to be extended two miles, beyond Warren; not located in print (searched 9 Oct 2026)."

| ID | N | depth | safe sentence |
|---|---|---|---|
| E4 | **N3** | D2 | "Read at grade H with the period book: on 2 May 1864 Fox tells Olcott to send the papers at once; not located in print." |
| E5 | **N3** | D1 | "Read with the period book, partially deciphered (about 70%): on 3 May 1864 Fox tells Olcott the papers are lost; not located." |
"""
with tempfile.TemporaryDirectory() as tmp:
    os.makedirs(os.path.join(tmp, "ciphers", "eck"))
    open(os.path.join(tmp, "ciphers", "eck", "AUDIT.md"), "w").write(AUD)
    cwd = os.getcwd()
    os.chdir(tmp)
    try:
        bc._audit_cache.clear()
        day = {"E3": "6 Oct", "E4": "2 May", "E5": "3 May"}
        mk = lambda e, n, d, line="x": row(f"Eckert 1864: telegram {e}, {day.get(e, '1 Jan')} 1864", "eck",
                                            document_id=f"Huntington mssEC 19 p.1, {e}", plaintext_novelty=f"N{n}", depth=d, line=line)
        s1, _ = bc.best_safe_sentence(mk("E1", 1, "D3"), 1, 5)
        check(s1 == "", f"group template with a placeholder quoted for E1: {s1!r}")
        s2, _ = bc.best_safe_sentence(mk("E6", 1, "D3"), 1, 5)
        check(s2 == "", f"E2's own sentence quoted for its sibling E6: {s2!r}")
        s3, _ = bc.best_safe_sentence(mk("E3", 3, "D2", "the railroad is to be extended beyond Warren"), 3, 5)
        check("beyond Warren" in s3, f"E3's own (later) sentence not quoted: {s3!r}")
        s3b, _ = bc.best_safe_sentence(mk("E2", 3, "D2"), 3, 5)
        check(s3b == "", f"an N1 sentence quoted for an N3 row: {s3b!r}")
        s4, _ = bc.best_safe_sentence(mk("E4", 3, "D2", "Fox tells Olcott to send the papers"), 3, 5)
        check("send the papers" in s4, f"E4's table-row sentence not quoted: {s4!r}")
        s5, _ = bc.best_safe_sentence(mk("E5", 3, "D1", "Fox tells Olcott the papers are lost"), 3, 5)
        check(s5 == "", f"a 'partially deciphered' sentence quoted for a D1 row: {s5!r}")
        single, _ = bc.best_safe_sentence(row("Fox to Olcott, 2 May 1864", "eck", document_id="no id here", plaintext_novelty="N3",
                                               depth="D2", line="Fox tells Olcott to send the papers at once"), 3, 1)
        check("send the papers" in single, f"single-item folder lost its sentence: {single!r}")
    finally:
        os.chdir(cwd)
check(bc.over_claims("Continuous French on 32 of 55 lines.", {"depth": "D1"}), "'continuous French' not an over-claim at D1")
check(not bc.over_claims("Continuous French on 32 of 55 lines.", {"depth": "D2"}), "'continuous French' blocked at D2")
check(not bc.over_claims("Thurloe's office deciphered this system in 1655.", {"depth": "D2"}), "bare 'deciphered' blocked")
check(bc.depth_safe_title("no.86: the whole cipher read with the 1572 key", {"depth": "D2"}) == "no.86: cipher read in part with the 1572 key",
      "D4 title phrase kept on a D2 row")
check(bc.depth_safe_title("the whole cipher read", {"depth": "D4"}) == "the whole cipher read", "D4 title reworded on a D4 row")
san = bc.sanitize("DECODE: login rejected (ASKS row 1); Google Books keyed (&key=$GOOGLE_BOOKS_KEY&country=US); S2_KEY sent.")
check("ASKS" not in san and "_KEY" not in san and "owner-side request" in san, f"request pointer or key name survived: {san}")
it_key = {"cls": "key", "n": 3, "row": {"plaintext_novelty": "N1"}}
check([k for k, _ in bc.class_labels(it_key)] == ["Key N3", "text N1"], f"key item labels: {bc.class_labels(it_key)}")
check("read in full" not in dict((k, e) for k, _, e in bc.CLASSES)["completed-reading"], "count card still says 'read in full'")

print("FAIL" if fails else "ok: test_build_catalogue")
sys.exit(1 if fails else 0)
