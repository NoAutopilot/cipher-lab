# VERIFY-F61-V8 prompts and disclosures (29 Sept 2026)

- Design, categories and read-outs committed before any vision call or look (585a5abe). One mechanical fix after that commit and before any
  tile existed: the f108g/f108h source-image path (FileNotFoundError); no change to sample, geometry or read-outs.
- Natives fetched once each (family/requests.log, 08:16 UTC): f.188r sha1 1c584b0f, f.101r sha1 313f92b3 (both = MANIFEST).
- The key v8_items.tsv was committed before the calls.
- Verifier's look before the calls (geometry only): one strip of six setN tiles (N046 f.61 C43, N098 f.108r L02 boundary ZHOOK, N027 f.108r L06 4PI,
  N038 f.188r C43, N033 f.101r C43, N001 f.274r gate). The markers sit on the target in all six, and the boundary tile is whole. The f.101r tile shows
  interlined gloss ink above and below the cipher row, as V7 disclosed; the readers get no letter key, so the tiles were kept as cut.
- Three fresh Opus subagents in parallel, each told to open only its own seven sheets. The text is below, verbatim, minus the file paths.

## setF and setG (same text, different sheets, shuffles and ids)
Each tile on these sheets shows a handwritten cipher sign from a 16th-century letter, marked by a red triangle above and below. Classify ONLY the sign
between the two triangles, by shape. Categories:
A = 4-head hash: an angled open figure-4 head sitting on or rising above a hash (#), i.e. the 4's stem is crossed by hash bars.
D = 2-hook ("2#"): a 2-shaped hooked stroke (a curve with a flat or hooked foot) leading into a hash, the whole reading like "2#" or "24" with hash bars.
E = a figure-4 whose stem(s) are NOT crossed by hash bars: e.g. a 4 over two upright stems joined by a bar (like a 4 over a Greek Pi), or a plain 4.
B = looped: two small loops (closed rings) sitting on a hash, with only short verticals.
N = other: anything else (including a plain hash with nothing attached, a "43"-like sign, a different sign) or you cannot tell.
Do not guess what letters these signs mean; shape only. Answer every tile id.

## setN
As above but only three categories: A (as above), B (as above), N = anything else or cannot tell. For every N, add 2-6 words describing the sign.
