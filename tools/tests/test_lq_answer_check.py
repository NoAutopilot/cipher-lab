#!/usr/bin/env python3
"""Offline test for tools/lq_answer_check.py (CLAUDE.md Usage 8a, the L19 incident of 26
Sept 2026: a Digital Bodleian "no items" search was first filed as "not digitised" before the
holding catalogue's own "Not available online" record, with its ark, was checked).

Covers: (1) the real L19/L24 shape -- a negative image-portal answer with the ark and the
"Not available online" quote present, which must PASS; (2) the pre-fix shape -- the same
negative with neither rung, which must FAIL naming both missing rungs; (3) a negative with
only the ark (no quoted availability phrase) and only the phrase (no ark/catalogue URL),
each failing naming the one rung that's missing; (4) a positive answer (no negative phrase
at all), which always passes regardless of ladder rungs; (5) the ladder-loading helpers
against the real tools/data/catalogue_ladders.tsv on disk, so a change to that file's column
names would be caught here too; (6) --row institution matching against a synthetic
LOCAL-QUEUE.tsv-shaped fixture, and that an unmatched row falls back to "any institution's
holding-catalogue host" rather than refusing to match; (7) kind awareness (the L20 incident,
26 Sept 2026): the real L20 shape (ia-reader, no ladder rungs at all) must PASS, the L19 shape
must still FAIL under kind=browser-check, a kind outside the page-read set (bare 'hathitrust',
catalogue-lookup, no kind) still requires both rungs, and --row/--kind plumbing (kind_for_row,
the CLI's --row-driven lookup, and a --kind override) all resolve correctly.

Run: python3 tools/tests/test_lq_answer_check.py
"""
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import lq_answer_check as lq  # noqa: E402

fails = 0


def report(name, ok, detail=""):
    global fails
    fails += not ok
    print(("PASS" if ok else "FAIL"), name, detail)


REAL_LADDER = lq.load_ladder()

# --- 1. real L19/L24 shape: negative + both rungs present -> PASS -----------------------------
L19_GOOD = (
    "row: L19\nkind: browser-check\ndate: 26 Sept 2026\nrunner: ChatGPT (owner's machine)\n\n"
    "Digital Bodleian returns no items for a search on 'Rawl. A. 24'. The Bodleian Archives and "
    "Manuscripts record (marco.ox.ac.uk, ark:/29072/x08k71nh14zj, 'Rawlinson Manuscripts') lists "
    "MSS. Rawl. A. 24/1-2 as 'Not available online'."
)
code, msg = lq.check(L19_GOOD, REAL_LADDER)
report("L19 good shape exits 0", code == 0, msg)

# --- 2. pre-fix shape: negative, no ark, no quoted availability phrase -> FAIL, both rungs -----
L19_BAD = (
    "row: L19\nkind: browser-check\ndate: 26 Sept 2026\nrunner: ChatGPT (owner's machine)\n\n"
    "Searched Digital Bodleian for 'Rawl. A. 24', 'MS. Rawl. A. 24' and 'Rawlinson A 24': no items."
)
code, msg = lq.check(L19_BAD, REAL_LADDER)
report("L19 bad (pre-fix) shape exits 1", code == 1, msg)
report("L19 bad shape names holding-catalogue rung missing", "holding-catalogue record" in msg, msg)
report("L19 bad shape names availability rung missing", "availability phrase" in msg, msg)

# --- 3a. negative + ark only, no quoted availability phrase -> FAIL, one rung ------------------
ARK_ONLY = (
    "No items found on Digital Bodleian. See marco.ox.ac.uk/ark:/29072/x08k71nh14zj for the record."
)
code, msg = lq.check(ARK_ONLY, REAL_LADDER)
report("ark-only negative exits 1", code == 1, msg)
report("ark-only negative missing only the availability rung",
       "availability phrase" in msg and "holding-catalogue record" not in msg, msg)

# --- 3b. negative + availability phrase only, no ark/catalogue URL -> FAIL, one rung -----------
PHRASE_ONLY = "No items found. The volume is Not available online, per the archive."
code, msg = lq.check(PHRASE_ONLY, REAL_LADDER)
report("phrase-only negative exits 1", code == 1, msg)
report("phrase-only negative missing only the holding-catalogue rung",
       "holding-catalogue record" in msg and "availability phrase" not in msg, msg)

# --- 4. positive answer: always exits 0, whatever rungs are or aren't present -----------------
POSITIVE = (
    "Rawl. A. 24 fol. 73 and 76 are imaged. A period decipherment is written interlinearly on "
    "fol. 76. Leaf images saved as rawl-a24-p73.jpg and rawl-a24-p76.jpg."
)
code, msg = lq.check(POSITIVE, REAL_LADDER)
report("positive answer exits 0", code == 0, msg)

EMPTY_POSITIVE = "Nothing about digitisation was checked; the record was read in full and quoted below."
# "Nothing" is a negative trigger word even mid-sentence, so this is treated as a negative that
# then must show both rungs -- pins the documented behaviour (word-bounded "nothing" always
# counts) rather than silently special-casing it.
code, msg = lq.check(EMPTY_POSITIVE, REAL_LADDER)
report("'nothing' substring still triggers negative gating", code == 1, msg)

# --- 5. ladder-loading helpers against the real file on disk -----------------------------------
report("real ladder file loads with rows", len(REAL_LADDER) > 5, f"{len(REAL_LADDER)} rows")
report("real ladder has expected columns",
       set(REAL_LADDER[0].keys()) >= {
           "institution", "image_portal", "holding_catalogue", "item_record_pattern",
           "request_page", "notes", "source",
       },
       list(REAL_LADDER[0].keys()))
bodleian_hosts = lq.ladder_hosts_for_institution(REAL_LADDER, "Bodleian")
report("Bodleian ladder row resolves marco.ox.ac.uk as a holding-catalogue host",
       any("marco.ox.ac.uk" in h for h in bodleian_hosts), bodleian_hosts)

# --- 6. --row institution matching against a synthetic LOCAL-QUEUE.tsv fixture -----------------
with tempfile.TemporaryDirectory() as tmp:
    fixture_queue = os.path.join(tmp, "LOCAL-QUEUE.tsv")
    with open(fixture_queue, "w", encoding="utf-8") as f:
        f.write("id\tkind\ttarget\tinstruction\tstatus\tresult\n")
        f.write("L19\tbrowser-check\tciphers/thurloe-printed\t"
                "Open Digital Bodleian and search 'Rawl. A. 24'; the Bodleian Archives and "
                "Manuscripts catalogue at archives.bodleian.ox.ac.uk carries the availability flag.\t"
                "queued\t\n")
        f.write("L99\tbrowser-check\tciphers/some-other-target\t"
                "Search an institution not in the ladder at all.\tqueued\t\n")

    real_path = lq.LOCAL_QUEUE_PATH
    lq.LOCAL_QUEUE_PATH = fixture_queue
    try:
        inst = lq.institution_for_row("L19", REAL_LADDER)
        report("row L19 matches Bodleian by host mention in its instruction", inst == "Bodleian", inst)

        inst_unmatched = lq.institution_for_row("L99", REAL_LADDER)
        report("row L99 (no known institution named) matches nothing rather than guessing",
               inst_unmatched is None, inst_unmatched)

        # institution=None (row L99's case) must still fall back to checking against ANY
        # institution's holding-catalogue host, not refuse to check at all.
        code, msg = lq.check(ARK_ONLY, REAL_LADDER, institution=inst_unmatched)
        report("unmatched institution still runs the generic ark/host check", code == 1, msg)
    finally:
        lq.LOCAL_QUEUE_PATH = real_path

# --- CLI smoke test: run the module's main() against a temp file -------------------------------
with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as tf:
    tf.write(L19_GOOD)
    tf_path = tf.name
try:
    rc = lq.main([tf_path])
    report("CLI main() on L19-good file exits 0", rc == 0)
finally:
    os.unlink(tf_path)

# --- 7. kind awareness (26 Sept 2026, the L20 incident) ----------------------------------------
# The L20 shape: an ia-reader row's content-read negative, no catalogue ladder rungs at all --
# must PASS on kind alone, where the pre-fix rule would have bounced it (as PR 24 actually was).
L20_SHAPE = (
    "row: L20\nkind: ia-reader\ndate: 26 Sept 2026\nrunner: browser (owner's archive.org login)\n\n"
    "Borrowed archive.org/details/correspondancede0006jose and read p.647. The index lists 'Mercy' "
    "at pp.15, 20 and 647, but p.647 itself does not quote or summarise the 6 June 1648 instruction "
    "to the abbe de Mercy -- it is a bare listing, not found in the body text there."
)
code, msg = lq.check(L20_SHAPE, REAL_LADDER, kind="ia-reader")
report("L20 shape (ia-reader kind) exits 0 with no ladder rungs", code == 0, msg)

for kind in ("edition-read", "hathitrust-page", "jstor"):
    code, msg = lq.check("Not found in the volume; no hits for the phrase.", REAL_LADDER, kind=kind)
    report(f"bare negative with kind={kind} exits 0 (page-read kind)", code == 0, msg)

# The L19 shape must still FAIL as browser-check (kind requires ladder rungs) even though the
# kind-awareness code path now exists -- the fix must not loosen the rule for the kinds it
# still governs.
code, msg = lq.check(L19_BAD, REAL_LADDER, kind="browser-check")
report("L19 bad shape with kind=browser-check still exits 1", code == 1, msg)

# A kind not in PAGE_READ_KINDS (the bare search-only 'hathitrust' kind, catalogue-lookup, or
# no kind at all) keeps requiring both rungs.
code, msg = lq.check(L19_BAD, REAL_LADDER, kind="hathitrust")
report("bare 'hathitrust' kind (search-only, not a page read) still requires ladder rungs",
       code == 1, msg)
code, msg = lq.check(L19_BAD, REAL_LADDER, kind="catalogue-lookup")
report("catalogue-lookup kind still requires ladder rungs", code == 1, msg)
code, msg = lq.check(L19_BAD, REAL_LADDER, kind=None)
report("no kind (institution/--row absent) still requires ladder rungs", code == 1, msg)

# kind_for_row / --row plumbing against a synthetic LOCAL-QUEUE.tsv fixture including the real
# L20 row shape.
with tempfile.TemporaryDirectory() as tmp:
    fixture_queue = os.path.join(tmp, "LOCAL-QUEUE.tsv")
    with open(fixture_queue, "w", encoding="utf-8") as f:
        f.write("id\tkind\ttarget\tinstruction\tstatus\tresult\n")
        f.write("L20\tia-reader\tciphers/espagnol142-mercy-1648\t"
                "Borrow and read p.647.\tqueued\t\n")
        f.write("L19\tbrowser-check\tciphers/thurloe-printed\t"
                "Search Digital Bodleian.\tqueued\t\n")

    real_path = lq.LOCAL_QUEUE_PATH
    lq.LOCAL_QUEUE_PATH = fixture_queue
    try:
        report("kind_for_row resolves L20 to ia-reader",
               lq.kind_for_row("L20") == "ia-reader", lq.kind_for_row("L20"))
        report("kind_for_row resolves L19 to browser-check",
               lq.kind_for_row("L19") == "browser-check", lq.kind_for_row("L19"))
        report("kind_for_row on an unknown row id returns None",
               lq.kind_for_row("L999") is None, lq.kind_for_row("L999"))

        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as tf:
            tf.write(L20_SHAPE)
            tf_path = tf.name
        try:
            rc = lq.main([tf_path, "--row", "L20"])
            report("CLI main() with --row L20 exits 0 via kind lookup", rc == 0)
        finally:
            os.unlink(tf_path)

        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as tf:
            tf.write(L19_BAD)
            tf_path = tf.name
        try:
            rc = lq.main([tf_path, "--row", "L19"])
            report("CLI main() with --row L19 still exits 1 via kind lookup", rc == 1)
            rc = lq.main([tf_path, "--kind", "ia-reader"])
            report("CLI --kind override passes an L19-shaped negative anyway", rc == 0)
        finally:
            os.unlink(tf_path)
    finally:
        lq.LOCAL_QUEUE_PATH = real_path

rc = lq.main(["/no/such/file/anywhere.md"])
report("CLI main() on a missing file exits 2", rc == 2)

print(f"\n{fails} failure(s)" if fails else "\nall tests passed")
sys.exit(1 if fails else 0)
