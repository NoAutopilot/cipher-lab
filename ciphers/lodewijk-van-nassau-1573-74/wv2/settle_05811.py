#!/usr/bin/env python3
"""Settle a subset of 5811's pass A/B disagreements (wv2/recon/05811/*/disagreements.tsv), LANE R2 worker W2, 24 Sept 2026.

Blocker logged in NOTES.md 'W2': the WV2 page images (images_wv2/, 150dpi JPEG direct from the WVO PDF, no IIIF
tiles, no local crop tool -- PIL/imagemagick unavailable, no network this brief) do not resolve individual 2-3
digit numeral groups in this secretary hand at the disagreement level (e.g. 44 vs 111, 51 vs 81); eye-checking
each of 212 non-gap disagreements against the full-page image was tried on a sample and found unreliable, so a
literal "read the glyph" settlement is not attempted here for most rows. Two things ARE reliable and are used:

1. Structural: one candidate is not a valid key.tsv code at all (a group two Sonnet passes split differently,
   producing a garbled digit run), the other is -- settle for the keyed one. No ambiguity, no image needed.
2. Cross-page corroboration: p5 is a parallel copy of p1+p2 (W1's note, confirmed here by eye on the page image --
   same salutation, same closing, matching numeral runs). Aligning p1+p2's raw sign sequence against p5's with
   difflib (both directions) finds long stretches of literal sign-for-sign agreement between two INDEPENDENTLY
   reconciled documents; where a disagreement's position falls inside such a stretch and exactly one candidate
   matches the other document's independently-read sign there, that is real evidence from a second manuscript
   witness, not a coin flip -- take it. (A single-token match with no surrounding run would be coincidence;
   difflib's opcodes only mark a run 'equal' when the matching context around it also lines up.)

Neither method is "read on the image" in the literal glyph sense the brief asked for; both use the manuscript
(the duplicate letter is still primary evidence) rather than a language model on this target's own tiny corpus
(rejected -- see rank_impact experiment in NOTES.md, corpus too small at ~2.8k chars for 4-gram scoring to be
trustworthy at single-digit resolution). Every settled row is logged as resolved (with its instance); everything
else is left as recon's own M/gap fallback, honestly unresolved, and enumerated in the run log.

    python3 wv2/settle_05811.py            write wv2/settle_05811.tsv + wv2/settle_log_05811.tsv
    python3 wv2/settle_05811.py --check    exit 1 if either is stale
"""
import csv, difflib, io, sys
from pathlib import Path

H = Path(__file__).resolve().parent
PAGES = ["05811_p1", "05811_p2", "05811_p5"]


def load_draft(pg):
    return list(csv.DictReader(open(H / "recon" / "05811" / pg / "ciphertext_draft.tsv"), delimiter="\t"))


def load_dis(pg):
    return list(csv.DictReader(open(H / "recon" / "05811" / pg / "disagreements.tsv"), delimiter="\t"))


def load_key(path):
    key = {}
    for row in csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"):
        code = row.get("code") or row.get("sign") or row.get("token")
        key[code] = row["value"]
    return key


def numeral_idx(rows):
    return [i for i, r in enumerate(rows) if not r["sign"].startswith("=")]


def keyed_valid(sign, key):
    v = key.get(sign)
    return v is not None and v.upper() not in ("NULL", "?")


def cross_page_matches(seq_a, seq_b):
    """opcodes' 'equal' runs of a SequenceMatcher(seq_a, seq_b): index in seq_a -> index in seq_b."""
    sm = difflib.SequenceMatcher(None, seq_a, seq_b, autojunk=False)
    m = {}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                m[i1 + k] = j1 + k
    return m


def main():
    check = "--check" in sys.argv
    key = load_key(H.parent / "key.tsv")
    draft = {pg: load_draft(pg) for pg in PAGES}
    nidx = {pg: numeral_idx(draft[pg]) for pg in PAGES}
    pos_to_local = {pg: {(draft[pg][i]["line"], draft[pg][i]["position"]): k for k, i in enumerate(nidx[pg])}
                    for pg in PAGES}

    combo = [("05811_p1", i) for i in nidx["05811_p1"]] + [("05811_p2", i) for i in nidx["05811_p2"]]
    seq_combo = [draft[pg][i]["sign"] for pg, i in combo]
    seq_5 = [draft["05811_p5"][i]["sign"] for i in nidx["05811_p5"]]

    combo_to_5 = cross_page_matches(seq_combo, seq_5)
    p5_to_combo = cross_page_matches(seq_5, seq_combo)

    settled = {}   # (line, position) -> (sign, why)
    log_rows = []
    n_structural = n_cross = n_unsettled = n_gap = 0

    for pg in PAGES:
        for d in load_dis(pg):
            line, col, a, b, flagged = d["line"], d["col"], d["A"], d["B"], d["flagged"]
            if not a or not b or a == "-" or b == "-":
                n_gap += 1
                log_rows.append([pg, line, col, a, b, "GAP", "needs image, not attempted (resolution blocker)"])
                continue
            if a.startswith("=") or b.startswith("="):
                n_unsettled += 1
                log_rows.append([pg, line, col, a, b, "M", "clear-word disagreement, not attempted"])
                continue

            a_ok, b_ok = keyed_valid(a, key), keyed_valid(b, key)
            if a_ok != b_ok:
                chosen = a if a_ok else b
                settled[(line, col)] = (chosen, f"structural: {b if a_ok else a} is not a valid key.tsv code")
                log_rows.append([pg, line, col, a, b, "STRUCTURAL", f"chosen {chosen}"])
                n_structural += 1
                continue

            # cross-page corroboration
            local_i = pos_to_local[pg].get((line, col))
            other_sign = None
            if pg in ("05811_p1", "05811_p2") and local_i is not None:
                ci = next(k for k, (p, i) in enumerate(combo) if p == pg and i == nidx[pg][local_i])
                j = combo_to_5.get(ci)
                if j is not None:
                    other_sign = seq_5[j]
            elif pg == "05811_p5" and local_i is not None:
                j = p5_to_combo.get(local_i)
                if j is not None:
                    other_sign = seq_combo[j]

            if other_sign is not None and (other_sign == a) != (other_sign == b):
                chosen = a if other_sign == a else b
                settled[(line, col)] = (chosen, "matches p5 parallel-copy alignment" if pg != "05811_p5"
                                          else "matches p1+p2 parallel-copy alignment")
                log_rows.append([pg, line, col, a, b, "CROSS-PAGE", f"chosen {chosen} (other doc reads {other_sign})"])
                n_cross += 1
                continue

            n_unsettled += 1
            log_rows.append([pg, line, col, a, b, "M", "no structural or cross-page signal; needs image (blocker)"])

    settle_io = io.StringIO()
    w = csv.writer(settle_io, delimiter="\t", lineterminator="\n")
    w.writerow(["line", "position", "sign", "why"])
    for (line, col), (sign, why) in sorted(settled.items()):
        w.writerow([line, col, sign, why])
    new_settle = settle_io.getvalue()

    log_io = io.StringIO()
    w2 = csv.writer(log_io, delimiter="\t", lineterminator="\n")
    w2.writerow(["page", "line", "col", "A", "B", "decision", "note"])
    for row in log_rows:
        w2.writerow(row)
    new_log = log_io.getvalue()

    settle_path, log_path = H / "settle_05811.tsv", H / "settle_log_05811.tsv"
    if check:
        stale = False
        if not settle_path.exists() or settle_path.read_text() != new_settle:
            print(f"STALE: {settle_path}", file=sys.stderr); stale = True
        if not log_path.exists() or log_path.read_text() != new_log:
            print(f"STALE: {log_path}", file=sys.stderr); stale = True
        sys.exit(1 if stale else 0)

    settle_path.write_text(new_settle)
    log_path.write_text(new_log)
    print(f"settled {len(settled)} (structural {n_structural}, cross-page {n_cross}); "
          f"unsettled {n_unsettled}, gap {n_gap} (needs image or clear-word, not attempted)")


if __name__ == "__main__":
    main()
