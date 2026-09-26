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
holding-catalogue host" rather than refusing to match.

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

rc = lq.main(["/no/such/file/anywhere.md"])
report("CLI main() on a missing file exits 2", rc == 2)

print(f"\n{fails} failure(s)" if fails else "\nall tests passed")
sys.exit(1 if fails else 0)
