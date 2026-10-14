# fr3982-nevers-toscana-1592 -- hypotheses and family runs (append-only)

Opened 14 Oct 2026 (TUSC-XM). Earlier key screens (no.62, 46, 70, 45, 73) are logged in NOTES.md and q7test/, not here.

## Tomokiyo's Tuscan tables vs f.25 (TUSC-XM, 14 Oct 2026; PREREG-TUSC-XM.md)

Conditional on ciphertext.tsv (error 0.115, upper 0.160; looped sign never rendered as 8; BNF-Q7-ERR). Tables credit S. Tomokiyo.

| table | control: power C0 / C1 0.115 / C2 0.160 / C3 8-loss (n=100) | target: T, p_key (1000 shuffled keys), order p99 | verdict |
|---|---|---|---|
| T1 Guicciardini-Sillery 1593 (after Speziali 1955) | 0.91 / 0.71 / 0.49 / 0.62 | -1.7315, 0.340, -1.5329 (FAIL) | NON-TEST (power < 0.8 at C2 and C3) |
| T2 Guicciardini ca.1590 (after Monts de Savasse 1997) | T2b 0.01 / 0.02 / 0.00 / 0.01 (T2a 0.00 / 0.03 / 0.00 / 0.03) | -1.3954, 0.389, -1.2200 (FAIL) | NON-TEST (instrument cannot read the polyphonic table) |

## Key no.70 alphabet + barred-figure word codes vs f.25 (NO70-WORDS, 14 Oct 2026; PREREG-NO70-WORDS.md)

| key | control: power C1 0.115 / C2 0.160 / C3 8-loss + 0.07 (n=50, 100+100 nulls) | target: S, p_a, p_b (1000+1000 nulls) | verdict |
|---|---|---|---|
| no.70 alphabet + 24 barred figures 54, 56-78 (keys/key_no70_nomenclator.tsv) | 0.94 / 0.76 / 0.70 | -1.2593, 0.060, 0.255 (no fit; no word code on the path) | NON-TEST (power < 0.80 at C2 and C3) |

