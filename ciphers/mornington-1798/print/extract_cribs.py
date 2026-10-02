#!/usr/bin/env python3
"""Cut three grade-C crib files from the Martin 1836 OCR already on disk (no network), for the D623 cipher items whose
subjects they share. Line ranges are raw line numbers in the *_djvu.txt files as served by archive.org (see manifest.tsv);
the OCR is kept uncorrected, only re-ordered where the page layout interleaved two text streams:
  - Vol. 1 pp. viii-x (35304_djvu.txt): the Malartic proclamation, printed French and English in two columns; the OCR
    gives French column then English column per page, so each page is written here as its French block then its
    English block, pages marked. Crib for D623/4 and /5 (3 and 6 Jul 1798, 'despatch in cipher re the Mauritius
    proclamation').
  - Vol. 1 No. XVII pp. 64-65 (35304_djvu.txt): Mornington to General Harris, Fort William, 20 Jun 1798, the
    mobilisation letter on the proclamation. Crib for D623/4-5 (same subject; D623/2-3 are the clear 20 Jun 1798 items).
  - Vol. 2 No. XIII pp. 25-34 (35315_djvu.txt): Mornington to Lieut.-Colonel Kirkpatrick, Fort St George, 5 Jun 1799,
    with the Partition Treaty of Mysore (22 Jun 1799), its Schedules A-D and the Separate Articles printed as the
    footnote under pp. 26-33. The OCR interleaves body and footnote page by page; written here as the letter body
    first, then the footnote, pages marked. Crib for D623/24 (7 Jun 1799, 'memorandum in cipher detailing the
    proposed settlement' of Mysore).
  - Vol. 2 No. LXXXIV p. 311 (35315_djvu.txt): the Marquess Wellesley to Vice-Admiral Rainier, Fort William, 9 Jul 1800
    (discontinue the Batavia expedition; stay in Indian seas; a force to Egypt by the Red Sea under consideration). Candidate
    clear text for D623/36 (9 Jul 1800, 'Extract from a letter to Admiral R, mainly in cipher'; copy /37): same date and
    recipient. Ingram 1970's footnote cites the manuscript as Add MS 13751 f. 77. Added GAPS4-mornington-1798, 2 Oct 2026.
  - Vol. 2 No. LXIX pp. 225-252 (35315_djvu.txt): the Earl of Mornington to Henry Dundas, Fort William, 5 Mar 1800, opening
    on Dundas's approbation of the treaty of Hyderabad and the system for the security of British India. Candidate clear
    text for D623/27 (5 Mar 1800, 'Letter and memorandum, partly in cipher, concerning the treaty of Hyderabad and policies
    for the preservation and consolidation of the British power in India'): same date, sender, recipient and subject. The
    23 Sept 2026 pass ran only the '5th March, 1800' form and matched the stock table on the same page range; 'March 5th,
    1800' was first run on 2 Oct 2026. Added GAPS4-mornington-1798, 2 Oct 2026.
  - Vol. 1 No. XXV (35304_djvu.txt): the Earl of Mornington to J. A. Kirkpatrick, Acting Resident at Hyderabad (Secret),
    Fort William, 8 Jul 1798, transmitting the Malartic proclamation. Clear text of the despatch catalogued as Mss Eur
    F228/65, "Copy of despatch (with decypher) dated 8 Jul 1798 from Wellesley" (BL, Kirkpatrick Collection; searcharchives
    record 040-002288638): a cipher + period decypher + print triple of the same office and week as D623/4-5. Crib/control
    candidate for the key, not a reading. Added GAPS4-mornington-1798, 2 Oct 2026.
Usage: python3 ciphers/mornington-1798/print/extract_cribs.py [--check]   (--check: exit 1 if a committed crib differs)
GAPS3-mornington-1798, 2 Oct 2026.
"""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
V1 = HERE / "35304_djvu.txt"; V2 = HERE / "35315_djvu.txt"

def lines(path):
    return path.read_text(errors="replace").split("\n")

def block(L, a, b):
    """raw lines a..b inclusive, 1-based, blank lines collapsed"""
    out, prev_blank = [], True
    for ln in L[a - 1:b]:
        s = ln.rstrip()
        if not s:
            if not prev_blank: out.append("")
            prev_blank = True
        else:
            out.append(s); prev_blank = False
    while out and out[-1] == "": out.pop()
    return "\n".join(out)

def hdr(*rows):
    return "\n".join("# " + r for r in rows) + "\n\n"

def proclamation(L):
    pages = [("viii", (317, 358), (361, 405), 408), ("ix", (414, 460), (462, 516), None), ("x", (521, 545), (548, 575), None)]
    parts = [hdr(
        "CRIB -- Malartic proclamation, Port North-West (Isle of France), 30 Jan 1798 (10 Pluviose an VI), French with",
        "the period English translation. Printed: Martin, Despatches, Minutes and Correspondence of the Marquess Wellesley,",
        "Vol. 1 (1836), Introduction pp. viii-x (two columns, French left, English right; a footnote on p. viii refers to",
        "the Governor-General's Minute of 12 Aug 1798). Source: archive.org india.history.resource.35304, 35304_djvu.txt",
        "raw lines 314-575 (OCR uncorrected; the two columns are de-interleaved per page by extract_cribs.py, nothing retyped).",
        "Grade C (printed clear text, rule 4) for every token; this is a crib candidate, not a reading of any D623 item.",
        "Crib for: D623/4 (3 Jul 1798) and D623/5 (6 Jul 1798), the 'despatch in cipher re the Mauritius proclamation' and its",
        "duplicate -- the despatch is expected to quote or paraphrase the English translation. GAPS3-mornington-1798, 2 Oct 2026.")]
    parts.append(block(L, 314, 314) + "\n")
    for pg, fr, en, fn in pages:
        parts.append(f"\n## p. {pg} -- French column\n" + block(L, *fr) + "\n")
        parts.append(f"\n## p. {pg} -- English column\n" + block(L, *en) + "\n")
        if fn: parts.append(f"\n## p. {pg} -- footnote\n" + block(L, fn, fn) + "\n")
    return "".join(parts)

def harris(L):
    return hdr(
        "CRIB -- The Earl of Mornington to General Harris, Fort William, 20 Jun 1798 (private; orders to assemble the army on",
        "the coast after the Malartic proclamation). Printed: Martin, Despatches ... of the Marquess Wellesley, Vol. 1 (1836),",
        "No. XVII, pp. 64-65. Source: archive.org india.history.resource.35304, 35304_djvu.txt raw lines 4612-4664 (OCR",
        "uncorrected; the p. 65 running head is kept). Grade C (printed clear text, rule 4) for every token.",
        "Crib for: D623/4 and /5 (3 and 6 Jul 1798, the cipher despatch on the Mauritius proclamation and the measures taken);",
        "the same date and subject as the clear D623/2 and /3 (20 Jun 1798, the proclamation and the mobilisation orders).",
        "Not a reading of any D623 item. GAPS3-mornington-1798, 2 Oct 2026.") + block(L, 4612, 4664) + "\n"

def mysore(L):
    body = [(2075, 2092, 25), (2101, 2113, 26), (2159, 2160, 27), (2213, 2214, 28), (2268, 2269, 29), (2325, 2326, 30),
            (2391, 2392, 31), (2452, 2453, 32), (2521, 2541, 33), (2576, 2584, 34)]
    foot = [(2116, 2153, 26), (2163, 2207, 27), (2217, 2262, 28), (2272, 2319, 29), (2329, 2385, 30), (2395, 2446, 31),
            (2456, 2515, 32), (2544, 2570, 33)]
    parts = [hdr(
        "CRIB -- The Earl of Mornington to Lieut.-Colonel Kirkpatrick, Fort St George, 5 Jun 1799 (the form of the Mysore",
        "settlement: a partition treaty with the Nizam first, then a subsidiary treaty with the Rajah; Seringapatam retained;",
        "Chittledroog refused to the Nizam), with the Partition Treaty of Mysore of 22 Jun 1799 (ten articles, Schedules A-D,",
        "ratifications of 26 Jun and 13 Jul 1799) and its Separate Articles printed by Martin as the footnote under the letter.",
        "Printed: Martin, Despatches ... of the Marquess Wellesley, Vol. 2 (1836), No. XIII, pp. 25-34 (footnote pp. 26-33).",
        "Source: archive.org india.history.resource.35315, 35315_djvu.txt raw lines 2075-2584 (OCR uncorrected; body and",
        "footnote de-interleaved per page by extract_cribs.py, nothing retyped). Grade C (printed clear text, rule 4).",
        "Crib for: D623/24 (7 Jun 1799, Mornington to Dundas, 'memorandum in cipher detailing the proposed settlement' of",
        "Mysore; its clear letter is print/D623-24_candidate_martin1836_v2_p35.txt). The letter of 5 Jun names 'my draft",
        "accompanying this letter'; Martin prints the treaty as executed on 22 Jun, not that draft, so shares, place names and",
        "sums are the expected crib material, not the exact wording of a 7 Jun memorandum. Not a reading of any D623 item.",
        "GAPS3-mornington-1798, 2 Oct 2026.")]
    parts.append("## Letter body (No. XIII)\n")
    for a, b, pg in body: parts.append(f"\n[p. {pg}]\n" + block(L, a, b) + "\n")
    parts.append("\n## Footnote: Partition Treaty of Mysore, 22 Jun 1799, Schedules A-D, Separate Articles\n")
    for a, b, pg in foot: parts.append(f"\n[p. {pg}, foot]\n" + block(L, a, b) + "\n")
    return "".join(parts)

def rainier(L):
    return hdr(
        "CANDIDATE -- The Marquess Wellesley to his Excellency Vice-Admiral Rainier, Fort William, 9 Jul 1800 (the Batavia",
        "expedition discontinued; the squadron to remain in the Indian seas against a French move from Europe or on Egypt by",
        "the Red Sea; a force from India to Egypt under consideration). Printed: Martin, Despatches ... of the Marquess",
        "Wellesley, Vol. 2 (1836), No. LXXXIV, p. 311. Manuscript cited by Ingram 1970 (be-api snippet, print/ingram_fts_results.tsv):",
        "Add MS 13751 f. 77 (BL, 'Copies of letters from Lord Wellesley to Vice Admi. Peter Rainier', searcharchives record",
        "040-002035836 family, 2 Oct 2026). Source: archive.org india.history.resource.35315, 35315_djvu.txt raw lines 16852-16888",
        "(OCR uncorrected: 'Fost William, July 9th, 1808' is Fort William, July 9th, 1800 -- the running head reads 1800).",
        "Grade C (printed clear text, rule 4) for every token. Candidate for: D623/36 (9 Jul 1800, 'Extract from a letter to",
        "Admiral R, mainly in cipher') and its copy D623/37 -- the same date and recipient; whether the cipher extract is a",
        "passage of this letter or a separate enclosure cannot be settled from print. Not a reading of any D623 item.",
        "GAPS4-mornington-1798, 2 Oct 2026.") + block(L, 16852, 16888) + "\n"

def dundas_5mar1800(L):
    return hdr(
        "CANDIDATE -- The Earl of Mornington to the Right Honourable Henry Dundas, Fort William, 5 Mar 1800 ('Although most of",
        "the points touched in your several despatches have already been anticipated ... approbation of the treaty of",
        "Hyderabad'; the system of British security in India, the Nizam, the treaties of Hyderabad and Seringapatam, the",
        "partition, the courts, revenue and army). Printed: Martin, Despatches ... of the Marquess Wellesley, Vol. 2 (1836),",
        "No. LXIX, pp. 225-252. Source: archive.org india.history.resource.35315, 35315_djvu.txt raw lines 12485-13703 (OCR",
        "uncorrected, running heads kept). Grade C (printed clear text, rule 4) for every token. Candidate for: D623/27",
        "(5 Mar 1800, 'Letter and memorandum, partly in cipher, concerning the treaty of Hyderabad and policies for the",
        "preservation and consolidation of the British power in India') -- the same date, sender, recipient and subject;",
        "whether the cipher passages and the memorandum are in this printed text cannot be settled from print. Not a reading",
        "of any D623 item. GAPS4-mornington-1798, 2 Oct 2026.") + block(L, 12485, 13703) + "\n"

def kirkpatrick(L):
    return hdr(
        "CRIB/CONTROL -- The Earl of Mornington to J. A. Kirkpatrick, Esq., Acting Resident at Hyderabad (Secret), Fort William,",
        "8 Jul 1798: transmits an authentic copy of the Malartic proclamation and the measures taken. Printed: Martin, Despatches",
        "... of the Marquess Wellesley, Vol. 1 (1836), No. XXV, from p. 100. Source: archive.org india.history.resource.35304,",
        "35304_djvu.txt raw lines 6102-6912 (OCR uncorrected). Grade C (printed clear text, rule 4) for every token.",
        "Why it is here: BL Mss Eur F228/65 (Kirkpatrick Collection, record 040-002288638, located 2 Oct 2026) is 'Copy of",
        "despatch (with decypher) dated 8 Jul 1798 from Wellesley on policy towards Tipu Sultan following the Proclamation issued",
        "by the French Governor of Mauritius' -- the cipher copy and its period decypher of this very despatch, in the same",
        "office and week as D623/4 (3 Jul) and /5 (6 Jul 1798). If the Governor-General used one cipher for Dundas and for the",
        "Resident, F228/65 + this print is a known-answer control for the D623/41 key; whether it is the same cipher is unknown.",
        "Not a reading of any D623 item. GAPS4-mornington-1798, 2 Oct 2026.") + block(L, 6102, 6912) + "\n"

OUT = {
    "crib_malartic-proclamation-30jan1798_martin1836_v1_pviii-x.txt": (V1, proclamation),
    "crib_mornington-harris-20jun1798_martin1836_v1_p64.txt": (V1, harris),
    "crib_mysore-partition-treaty-22jun1799_martin1836_v2_p25.txt": (V2, mysore),
    "D623-36_candidate_martin1836_v2_p311.txt": (V2, rainier),
    "D623-27_candidate_martin1836_v2_p225.txt": (V2, dundas_5mar1800),
    "crib_mornington-kirkpatrick-8jul1798_martin1836_v1_p100.txt": (V1, kirkpatrick),
}
if __name__ == "__main__":
    check = "--check" in sys.argv; stale = 0
    for name, (src, fn) in OUT.items():
        text = fn(lines(src)); p = HERE / name
        if check:
            if not p.exists() or p.read_text() != text: print(f"STALE {name}"); stale = 1
            else: print(f"ok {name}")
        else:
            p.write_text(text); print(f"wrote {name}: {len(text.splitlines())} lines, {len(text)} bytes")
    sys.exit(stale)
