# PREREG addendum pisrs (D4-PISRS, LANE DEFAULT-account-4-20261006-1235, 6 Oct 2026; written and pushed before any score)

Addendum to pis1key/PREREG_pis1key.md part (a). The ONLY change: instead of relabelling every T31 token, relabel only the
9 tokens pis2/t31_tokens.tsv marks SETTLED (R9-PIS2's per-token crop compare), each to its settled cell:
- f.244r (tx86/ciphertext_f244r.tsv, reconciled): L03 i25 -> T45; L03 i35, L06 i15, L07 i28, L09 i30 -> T36.
- f.275r (tx86e/ciphertext_f275r.tsv, reconciled): L04 i39, L09 i3, L12 i5, L14 i28 -> T36.
- tok_index = 0-based index over the line's tokens excluding '/' (as pis2/tokens_pos.tsv; the script asserts each is T31 and
  matches the context column). The other 14 T31 tokens and the unlocated f.244r L09 i26 stay T31.
- Blind passes A/B are not relabelled (their token indices are not the reconciled file's); they are re-run unchanged only
  to show the old numbers reproduce.

Unchanged from PIS1-KEY (a): scripts imported unchanged (pis1key.py run_files/relabel_file/ctrl86/control/identical, which
import kp86/kp86.py and kp86d/kp86d.py), seeds (run_files reseeds 20261004 per call; control seeds 500+s), nulls 1000/1000,
err 0.284 (f.244r) and 0.215 (f.275r), copies and drop strings, positive controls (kp86.py's on f.244r, kp86d.control on f.275r).

GATE (unchanged): the 9-token relabel is SUPPORTED if, on both pages, the reconciled relabelled score > the old reconciled
score and stays above both the key-shuffle p99 and the order p99. Per page reported separately as well.
Consequence (unchanged from (a)): in every outcome key86.tsv is unchanged (no cell value is tested) and the committed
transcriptions tx86/tx86e are unchanged in this job; the T31 tokens stay M. If SUPPORTED, the named next step is committing
the 9 labels into tx86/tx86e with the downstream regeneration (kp86e/t31_grades.py, kp86g/t31_grades_g.py, readings,
decode_key --check) as its own job; if not, the 9 per-token labels are logged as shape evidence only.

Descriptive, not gating: (i) the old all-T31 relabel numbers (pis1key) beside the 9-token ones; (ii) a relabel null: 200
draws relabelling 9 tokens drawn at random from the page's T31 tokens (same per-page count and target labels), nw_score
only, to show whether the specific settled tokens move the score more than arbitrary ones; (iii) identical() counts.
