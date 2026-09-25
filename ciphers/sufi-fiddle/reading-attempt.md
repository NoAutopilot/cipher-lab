# sufi-fiddle: cheap test 3 -- read as Arabic script (25 Sept 2026, LANE B4 worker bSUF3)

Status stays `open`. This is a read attempt, not a claimed solve (rule 10); every token below is
graded M (uncertain) or I (inferred), never H or C. No ar/fa/ota/ms/mrw judge corpus exists in
`tools/data` (CLAUDE.md rule 7 / lanes-7b-COMMON.md item 3), so `tools/judge_plaintext.py` cannot
be run on any candidate below -- **no judge**, by design, not an omission.

Source image: `ciphers/sufi-fiddle/images/Suffi-Fiddle-614.png` (the hand copy "copied by V.
Castle Winter", not the violin panel -- rule 2 applies twice, per NOTES.md's cheap-test-1 section).
This pass re-examined the image directly (5x-upscaled per-line crops, `PIL.Image.LANCZOS`, not
committed -- scratch files only) rather than re-deriving the sign pass; it builds on worker bSUF's
N=165/K=21 sign-id sequence in `ciphertext.txt`, converting each pooled sign label to a specific
Arabic Unicode letter with its own confidence.

## 1. Control (rule 3) -- and why it is weak

A synthetic matched control is not obtainable here: rule 3 asks for a control that shares length,
symbol count, **design** and **language** with the target, and the target's "design" is itself
unknown (a possibly-corrupted hand copy of a possibly-genuine inscription in a script family, not
a cipher system with defined parameters). What can be done instead, and its limits:

- **What a clean control would show.** Take a short genuine Arabic-script text of comparable
  length -- e.g. the Basmala, "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ" (19 letters) plus a short
  Persian couplet such as the opening of Sa'di's "بنی آدم اعضای یکدیگرند" (Rumi/Sa'di-style, ~24
  letters) -- and simulate a careless letter-by-letter hand copy of it: a copyist unfamiliar with
  the script (1) drops or miscounts dots (the single most common Arabic-copying error: ب/ت/ث/ن and
  ج/ح/خ and ف/ق and ع/غ differ only by dot count/position), (2) breaks or joins cursive ligatures
  at the wrong point (splitting one letter's two-stroke form into what looks like two letters, or
  fusing two letters' strokes into what looks like one), (3) loses final/medial/initial positional
  distinctions (a letter's four shape-variants collapsing toward the isolated form), and (4) omits
  or invents short vertical strokes that are alif in the original but noise in the copy, or vice
  versa. Doing this by hand to the Basmala would visibly degrade "بسم الله" toward something with
  the same letter-frequency profile as the target (heavy kaf/lam/waw, a handful of high-dot-count
  letters reduced to their pooled cluster) while making the *specific* letter identities much less
  certain than the *fact that it's Arabic-family script* -- exactly the asymmetry test 1 already
  found (script family: confident; letter identity: not).
- **Why it cannot be built as a real control this pass.** A control has to be run through the same
  transliteration procedure blind, by someone who does not already know the plaintext, to get a
  real letter-accuracy number -- that needs either a second, independent transcriber (not
  available inside one worker's cap) or a second blind pass by this same session pretending not to
  know the answer, which is not a real blind test (the session already read the target). Fabricating
  a number here would violate rule 3's own spirit (a control has to be a real test, not a stated
  expectation).
- **Conclusion:** this test proceeds without a numeric control, flagged weak per the brief's own
  instruction ("you cannot fetch a hand-copied control, so state that the control is weak and
  why"). The qualitative expectation above is the only substitute: *some* letters should transliterate
  correctly even through heavy copying noise, but individual dotted-letter identity is the least
  trustworthy layer of this whole pass, and any single-word "hit" below could as easily be
  copying-noise coincidence as a real word. Confidence markers throughout reflect this.

## 2. Transliteration table (sign id from `ciphertext.txt`, sure / probable / guess)

Mapping used from bSUF's pooled sign labels to a *default* Arabic Unicode letter, with the
alternates the pooling collapsed (NOTES.md: "several dotted-letter clusters ... pooled as one
label each where the dot pattern was not resolvable at this image's resolution"):

| Label | Default letter | Confidence class | Ambiguous with (same visual base) |
|---|---|---|---|
| waw | و | sure | -- (distinctive hook, no dot) |
| kaf | ك | sure | -- (distinctive flag-stroke top, most frequent shape, unambiguous in this hand) |
| alif | ا | sure | -- (plain vertical stroke) |
| lam | ل | probable | occasionally confusable with alif+curve in a careless hand |
| ha | ه | probable | could be a final ة (ta marbuta) where word-final |
| dal | د | probable | ذ (dhal) if an unresolved dot sits above it |
| ra | ر | probable | ز (zay) if an unresolved dot sits above it |
| nun | ن | probable | dot position (over vs. under) not always resolved |
| mim | م | probable | -- (closed loop, fairly distinctive) |
| ya / ya-dotted | ي | probable | ya-dotted tokens are the surer of the two |
| sin | س | probable | ش (shin, 3 dots) where dots unresolved |
| shin | ش | guess | س (sin, 0 dots) -- this is the same pooled cluster as sin |
| fa | ف | guess | ق (qaf, 2 dots vs. fa's 1) -- pooled, dot count not resolved |
| ghayn | غ | guess | ع (ain, 0 dots vs. ghayn's 1) -- pooled |
| ain | ع | guess | غ (ghayn) -- same pooled cluster, inverse |
| ta | ت | guess | ث / ب -- three-way pooled cluster (2 dots above / 3 dots above / 1 dot below) |
| tha | ث | guess | ت / ب -- same cluster |
| ba | ب | guess | ت / ث -- same cluster |
| dad | ض | guess | ص (sad) -- pooled, dot presence not resolved |
| hamza | ء | guess | most likely a misread stroke or an alif-with-hamza (أ/إ) rather than a bare mid-word hamza, which is typographically unusual in ordinary handwriting |

Per-line transliteration (word-groups separated by `|` exactly as `ciphertext.txt` segments them;
`[OBS]` = obscured under the glue repair, excluded; `[UNC]` = the copyist's own uncertain mark):

```
L1  هول (probable/probable/probable) | هاء (probable/sure/guess) | سلد (probable/probable/probable) | و (sure) | فغ (guess/guess)
L2  هع | تو | لكفتو | ضي | ثالكف | غث | بث | كتل | كتد | ءبت | سنابع | شفرغ | لبا
L3  سلنكو [OBS ~6-8] تنكيا | لكا
L4  ضتغ | كو | ضنع | مف | د[UNC] | سيركو | سر | لشبيا | كمر | مود | بيرت | فنغ | مو[OBS ~5-7]نتيد
L5  ككس | ست | مو | مهيد | ككسن | [UNC: ر]
L6  سركو | ممو | تلد | برکت | دو | عولك | عل | كل | عل | لك | لامك[UNC]
L7  سلاك | لك | سولك
```

All letters above are transliterated by sign shape only (I-grade at best: inferred from a hand
copy's visual resemblance, none read from a key or known plaintext); every guess-confidence letter
is a coin-flip within its pooled cluster and should be read as such, not as a settled identity.

## 3. Segmentation attempts by language

No language pass below reaches a coherent multi-word phrase. Tried in the brief's stated order.

**Arabic.** Scanned every word-group above against the likeliest Sufi formulae (Allah اَللّٰه,
Hu هو, ya يا, bismillah بسم الله, la ilaha illa llah لا إله إلا الله, and common tariqa/order
names -- Qadiri, Naqshbandi, Chishti, Mevlevi, Rifa'i). None matches cleanly:
- No group is a clean 4-letter alif-lam-lam-ha run (Allah): the nearest is L6's last group
  "لامك" (lam-alif-mim-kaf), which is lam-alif not alif-lam-lam, and carries the copyist's own
  uncertain mark.
- No 2-sign group reads ha-waw (Hu): L1's first group is ha-waw-**lam** (3 signs), one letter too
  many.
- No group opens ba-sin-mim (bismillah's bi-sm): none present.
- One weak positive: L6 group 4, **برکت** (ba-ra-kaf-ta) is one letter off from **بركة/بركت**
  ("baraka(t)", blessing -- a common word in religious/Sufi inscriptions, and the kind of ta/
  ta-marbuta confusion a hand copy would produce). Graded **M**, not higher: three of its four
  letters are guess-confidence (the ta/tha/ba cluster) or probable (ra), so this could equally be
  copying-noise coincidence given a 3-letter alphabet-sized search space.
- A second, weaker positive: L6 groups 7 and 9, both **عل** (ain-lam), appearing twice in the same
  line, are one letter short of **على** ("'ala", on/upon -- extremely common preposition) if a
  final alif was dropped or miscopied. Graded **M**, lower confidence than برکت (no repair needed
  there beyond a plausible drop, but "ain" itself is guess-confidence).
- L1 group 4, standalone **و** (waw, "and"), is a real, extremely common Arabic word by itself,
  and waw is the surest single-letter class in the mapping above. Graded **M** (a full word
  reading is only as strong as the confidence that this group really is isolated rather than
  joined to a neighbour the copy failed to connect).
- Nothing else recognized.

**Persian.** Same word-groups checked against common Persian function words and Sufi vocabulary
(او/hu, یا/ya, خدا/khoda, عشق/eshq "love", درویش/darvish). برکت (barakat) is a live Persian word too
(loaned from Arabic, same spelling) -- the L6 g4 candidate above carries over unchanged. No other
group matches. No candidate line reading emerges.

**Ottoman Turkish.** Same check against common Ottoman-script function words and Sufi vocabulary
(بركت/bereket is again a live loanword, carrying over the same weak L6 g4 candidate; ﻫﻮ/hu; درویش/
derviş; طریقت/tarikat "order/path"). No group matches طریقت or درویش. No other candidate.

**Malay (Jawi).** Checked against common Jawi function words (دان/dan "and" -- note this is NOT
waw, so L1 g4's "و" does not carry over as a Malay hit; برکت/berkat "blessing" is a live Malay
Islamic loanword spelled identically to the Arabic/Persian/Ottoman form, so the L6 g4 candidate
carries over again) and Islamic-formula words (الله, محمد). No group matches الله or محمد
(Muhammad would need mim-ha-mim-dal; the closest is L6 g2 "ممو", mim-mim-waw, wrong letter 3 and
missing dal). No candidate line reading beyond the recurring berkat guess.

**Maranao (in Arabic/Jawi-derived script).** No dedicated Maranao word list was available this
pass (no corpus on disk, no network per the brief's disk-only constraint); checked only for the
same Arabic-loanword Islamic vocabulary Maranao is known to carry (a Muslim Mindanao language,
per NOTES.md's discussion of Bulliet's own Philippine/Maranao hypothesis) -- berkat/barakat is
exactly this kind of loanword, so the same weak L6 g4 candidate is the only thing to report; no
Maranao-specific root words were checked since no reference list was on hand.

## 4. Grading and counts

Every letter in section 2 is graded **I** (inferred from visual resemblance to a Arabic-family
letterform in a hand copy, not read from any key or known plaintext) at the letter level, with
confidence noted as sure/probable/guess. Counts across all 7 lines (165 signs total per bSUF,
minus 2 excluded-as-obscured spans and int the 2 copyist-flagged-uncertain signs kept but marked):

- sure: 39 (waw x15, kaf x23, alif x1 -- undercount vs. bSUF's own totals because alif appears
  embedded inside several word-groups counted here at word level; this is a spot count, not a
  re-verification of bSUF's N=165)
- probable: roughly 60 (lam, ha, dal, ra, nun, mim, ya/ya-dotted, sin tokens)
- guess: roughly 60 (shin, fa, ghayn, ain, the ta/tha/ba three-way cluster, dad, hamza tokens)
- excluded (obscured/uncertain, per bSUF's own marks): 2 spans + 2 flagged signs, unchanged from
  ciphertext.txt

No token is graded H, C, or S: no key source, no known plaintext, and no cryptanalytic control
exists for this target (section 1). **No judge is reported: no ar/fa/ota/ms/mrw corpus exists in
tools/data, so `tools/judge_plaintext.py` cannot score any candidate above.**

## Best candidate line, and the honest summary

No line has a candidate reading; only three isolated word-level guesses, all graded M:
L1 g4 **و** ("and", Arabic, weak/short-word confidence), L6 g4 **برکت/بركة** ("blessing",
Arabic/Persian/Ottoman/Malay/plausibly-Maranao loanword, the single best candidate of this whole
pass but still resting on three guess-or-probable letters), and L6 g7/g9 **عل** (possibly على,
"on/upon", weaker than either). Everything else transliterates to letter sequences with no
recognized-word or recognized-formula match in any of the five languages tried. This is consistent
with (a) heavy hand-copying corruption of a genuine but now-illegible original, (b) a language or
register this pass's word lists don't cover, or (c) the inscription not being continuous meaningful
prose in any of these languages at all (a devotional pseudo-script, a personal cipher, or letters
copied for their look rather than their sense) -- this test cannot distinguish between those three.
Not a solve; not closed-negative either (no matched control exists to license that verdict, section
1) -- stays `open`.
