# SCAN-103: offset scan of the f.103r (confirm2) stretch (PREREG-txeng2-18 SCAN-103, TXE2-SCAN103, 10 Oct 2026, 00:39-01:0x UTC by date -u)

Read-free, scripts only. scan103.py (sha256 61e0d084cf54659b) reuses ../viv102anchor/anchor.py stream() and the frozen builder's B.align
(band 400) unchanged; statistic = DV1c's j0scan share (keyed, aligned positions whose decoded value equals the aligned letter) on
the f.103r collapsed stretch (stream index i0 = 3524 to end, 1,945 signs). j0 read from vivk_result.json by script (key 'j0' only).
Registered offset R = j0 + lo = **6655** (the builder's own control window let[lo:hi], dec_norm coordinates), registered span
hi - lo = 2,899 letters, window W = round(1.25 x 2899) = **3,624**. dec_norm = 9,554 letters. Seed 20261009 throughout.

## Deviation (declared)
The PREREG grid s = 0..len(dec_norm) - W step 50 ends at 5930, 725 letters before R: the stretch is end-anchored (N5-VIVK) and the
builder's own window is itself clipped at the end of dec_norm, so under the literal grid R could not be scanned at all. The grid was
extended to s = 0..len - span (= 6650) step 50 (134 offsets, 119 of them the PREREG grid), windows past 5930 truncated at the end of
dec_norm (length 2,904-3,624, never below the registered span); R = 6655 itself (off grid) was added as an evaluation point in the
confirm. On the literal PREREG grid alone the best is s = 4200 (real 0.5660, 50-shuffle margin 0.0134) and R is not scannable, which
would also read NOT BEST. Truncation means windows near the end give the DP less room than earlier ones; it is not corrected for.

## Scan (published key vs 50 value-shuffled keys per offset)
Real share is a plateau from 6200 to 6650 (0.593-0.614; margins 0.070-0.099), argmax **s = 6500 (real 0.6139, margin 0.0991)**;
s = 6650 (nearest grid point to R) 0.6043, margin 0.0911. Over the whole scan the 50-shuffle max never exceeds 0.5561 (at s = 0,
where real is 0.5406). Full table:

| s | window | real | shuf mean | shuf max (50) | margin |
|---|---|---|---|---|---|
| 0 | 3624 | 0.5406 | 0.4530 | 0.5561 | -0.0155 |
| 50 | 3624 | 0.5415 | 0.4533 | 0.5413 | 0.0002 |
| 100 | 3624 | 0.5330 | 0.4528 | 0.5539 | -0.0209 |
| 150 | 3624 | 0.5441 | 0.4520 | 0.5510 | -0.0069 |
| 200 | 3624 | 0.5354 | 0.4515 | 0.5526 | -0.0172 |
| 250 | 3624 | 0.5417 | 0.4519 | 0.5502 | -0.0085 |
| 300 | 3624 | 0.5389 | 0.4529 | 0.5481 | -0.0092 |
| 350 | 3624 | 0.5384 | 0.4544 | 0.5507 | -0.0123 |
| 400 | 3624 | 0.5400 | 0.4549 | 0.5532 | -0.0132 |
| 450 | 3624 | 0.5461 | 0.4535 | 0.5484 | -0.0023 |
| 500 | 3624 | 0.5335 | 0.4520 | 0.5367 | -0.0032 |
| 550 | 3624 | 0.5419 | 0.4521 | 0.5440 | -0.0021 |
| 600 | 3624 | 0.5410 | 0.4533 | 0.5473 | -0.0063 |
| 650 | 3624 | 0.5500 | 0.4546 | 0.5530 | -0.0030 |
| 700 | 3624 | 0.5451 | 0.4558 | 0.5539 | -0.0088 |
| 750 | 3624 | 0.5495 | 0.4551 | 0.5522 | -0.0027 |
| 800 | 3624 | 0.5486 | 0.4547 | 0.5457 | 0.0029 |
| 850 | 3624 | 0.5375 | 0.4560 | 0.5354 | 0.0021 |
| 900 | 3624 | 0.5329 | 0.4550 | 0.5457 | -0.0128 |
| 950 | 3624 | 0.5303 | 0.4550 | 0.5461 | -0.0158 |
| 1000 | 3624 | 0.5357 | 0.4552 | 0.5389 | -0.0032 |
| 1050 | 3624 | 0.5325 | 0.4562 | 0.5371 | -0.0046 |
| 1100 | 3624 | 0.5267 | 0.4572 | 0.5393 | -0.0126 |
| 1150 | 3624 | 0.5333 | 0.4566 | 0.5439 | -0.0106 |
| 1200 | 3624 | 0.5340 | 0.4567 | 0.5454 | -0.0114 |
| 1250 | 3624 | 0.5248 | 0.4560 | 0.5341 | -0.0093 |
| 1300 | 3624 | 0.5203 | 0.4540 | 0.5289 | -0.0086 |
| 1350 | 3624 | 0.5184 | 0.4532 | 0.5346 | -0.0163 |
| 1400 | 3624 | 0.5174 | 0.4552 | 0.5355 | -0.0181 |
| 1450 | 3624 | 0.5221 | 0.4540 | 0.5360 | -0.0138 |
| 1500 | 3624 | 0.5191 | 0.4534 | 0.5400 | -0.0209 |
| 1550 | 3624 | 0.5255 | 0.4536 | 0.5388 | -0.0133 |
| 1600 | 3624 | 0.5406 | 0.4530 | 0.5478 | -0.0072 |
| 1650 | 3624 | 0.5377 | 0.4531 | 0.5277 | 0.0100 |
| 1700 | 3624 | 0.5319 | 0.4552 | 0.5336 | -0.0017 |
| 1750 | 3624 | 0.5422 | 0.4542 | 0.5317 | 0.0105 |
| 1800 | 3624 | 0.5498 | 0.4557 | 0.5426 | 0.0072 |
| 1850 | 3624 | 0.5394 | 0.4570 | 0.5445 | -0.0051 |
| 1900 | 3624 | 0.5409 | 0.4576 | 0.5418 | -0.0009 |
| 1950 | 3624 | 0.5405 | 0.4576 | 0.5435 | -0.0030 |
| 2000 | 3624 | 0.5370 | 0.4573 | 0.5328 | 0.0042 |
| 2050 | 3624 | 0.5512 | 0.4570 | 0.5334 | 0.0178 |
| 2100 | 3624 | 0.5572 | 0.4561 | 0.5429 | 0.0143 |
| 2150 | 3624 | 0.5290 | 0.4566 | 0.5438 | -0.0147 |
| 2200 | 3624 | 0.5410 | 0.4543 | 0.5385 | 0.0026 |
| 2250 | 3624 | 0.5401 | 0.4550 | 0.5427 | -0.0026 |
| 2300 | 3624 | 0.5298 | 0.4545 | 0.5241 | 0.0057 |
| 2350 | 3624 | 0.5297 | 0.4517 | 0.5271 | 0.0026 |
| 2400 | 3624 | 0.5360 | 0.4505 | 0.5260 | 0.0100 |
| 2450 | 3624 | 0.5383 | 0.4520 | 0.5281 | 0.0101 |
| 2500 | 3624 | 0.5332 | 0.4511 | 0.5350 | -0.0018 |
| 2550 | 3624 | 0.5367 | 0.4532 | 0.5286 | 0.0080 |
| 2600 | 3624 | 0.5402 | 0.4526 | 0.5282 | 0.0120 |
| 2650 | 3624 | 0.5395 | 0.4549 | 0.5304 | 0.0092 |
| 2700 | 3624 | 0.5334 | 0.4550 | 0.5281 | 0.0053 |
| 2750 | 3624 | 0.5329 | 0.4578 | 0.5342 | -0.0013 |
| 2800 | 3624 | 0.5450 | 0.4574 | 0.5461 | -0.0010 |
| 2850 | 3624 | 0.5456 | 0.4575 | 0.5367 | 0.0089 |
| 2900 | 3624 | 0.5391 | 0.4579 | 0.5422 | -0.0031 |
| 2950 | 3624 | 0.5360 | 0.4592 | 0.5374 | -0.0014 |
| 3000 | 3624 | 0.5326 | 0.4622 | 0.5391 | -0.0065 |
| 3050 | 3624 | 0.5349 | 0.4616 | 0.5475 | -0.0127 |
| 3100 | 3624 | 0.5377 | 0.4610 | 0.5394 | -0.0018 |
| 3150 | 3624 | 0.5360 | 0.4577 | 0.5241 | 0.0119 |
| 3200 | 3624 | 0.5374 | 0.4558 | 0.5419 | -0.0045 |
| 3250 | 3624 | 0.5519 | 0.4566 | 0.5339 | 0.0180 |
| 3300 | 3624 | 0.5421 | 0.4560 | 0.5344 | 0.0078 |
| 3350 | 3624 | 0.5503 | 0.4580 | 0.5332 | 0.0171 |
| 3400 | 3624 | 0.5457 | 0.4557 | 0.5296 | 0.0162 |
| 3450 | 3624 | 0.5413 | 0.4578 | 0.5345 | 0.0068 |
| 3500 | 3624 | 0.5384 | 0.4570 | 0.5317 | 0.0067 |
| 3550 | 3624 | 0.5431 | 0.4568 | 0.5513 | -0.0082 |
| 3600 | 3624 | 0.5354 | 0.4561 | 0.5458 | -0.0104 |
| 3650 | 3624 | 0.5393 | 0.4555 | 0.5509 | -0.0116 |
| 3700 | 3624 | 0.5390 | 0.4540 | 0.5318 | 0.0072 |
| 3750 | 3624 | 0.5399 | 0.4548 | 0.5337 | 0.0062 |
| 3800 | 3624 | 0.5416 | 0.4548 | 0.5301 | 0.0116 |
| 3850 | 3624 | 0.5521 | 0.4542 | 0.5368 | 0.0153 |
| 3900 | 3624 | 0.5525 | 0.4529 | 0.5310 | 0.0215 |
| 3950 | 3624 | 0.5543 | 0.4524 | 0.5366 | 0.0177 |
| 4000 | 3624 | 0.5600 | 0.4529 | 0.5354 | 0.0246 |
| 4050 | 3624 | 0.5601 | 0.4529 | 0.5538 | 0.0064 |
| 4100 | 3624 | 0.5593 | 0.4533 | 0.5488 | 0.0104 |
| 4150 | 3624 | 0.5598 | 0.4543 | 0.5503 | 0.0095 |
| 4200 | 3624 | 0.5660 | 0.4542 | 0.5526 | 0.0134 |
| 4250 | 3624 | 0.5517 | 0.4561 | 0.5365 | 0.0152 |
| 4300 | 3624 | 0.5498 | 0.4549 | 0.5322 | 0.0177 |
| 4350 | 3624 | 0.5413 | 0.4530 | 0.5371 | 0.0042 |
| 4400 | 3624 | 0.5431 | 0.4525 | 0.5288 | 0.0143 |
| 4450 | 3624 | 0.5476 | 0.4518 | 0.5433 | 0.0043 |
| 4500 | 3624 | 0.5461 | 0.4511 | 0.5421 | 0.0041 |
| 4550 | 3624 | 0.5420 | 0.4514 | 0.5432 | -0.0012 |
| 4600 | 3624 | 0.5361 | 0.4498 | 0.5291 | 0.0071 |
| 4650 | 3624 | 0.5417 | 0.4503 | 0.5300 | 0.0116 |
| 4700 | 3624 | 0.5462 | 0.4510 | 0.5228 | 0.0234 |
| 4750 | 3624 | 0.5568 | 0.4511 | 0.5237 | 0.0331 |
| 4800 | 3624 | 0.5366 | 0.4486 | 0.5294 | 0.0071 |
| 4850 | 3624 | 0.5533 | 0.4481 | 0.5290 | 0.0243 |
| 4900 | 3624 | 0.5521 | 0.4484 | 0.5321 | 0.0200 |
| 4950 | 3624 | 0.5606 | 0.4513 | 0.5341 | 0.0265 |
| 5000 | 3624 | 0.5532 | 0.4502 | 0.5348 | 0.0184 |
| 5050 | 3624 | 0.5354 | 0.4515 | 0.5374 | -0.0020 |
| 5100 | 3624 | 0.5354 | 0.4540 | 0.5424 | -0.0070 |
| 5150 | 3624 | 0.5392 | 0.4531 | 0.5408 | -0.0016 |
| 5200 | 3624 | 0.5368 | 0.4547 | 0.5545 | -0.0177 |
| 5250 | 3624 | 0.5411 | 0.4522 | 0.5393 | 0.0018 |
| 5300 | 3624 | 0.5405 | 0.4522 | 0.5404 | 0.0001 |
| 5350 | 3624 | 0.5501 | 0.4533 | 0.5358 | 0.0142 |
| 5400 | 3624 | 0.5501 | 0.4517 | 0.5360 | 0.0141 |
| 5450 | 3624 | 0.5423 | 0.4523 | 0.5442 | -0.0019 |
| 5500 | 3624 | 0.5363 | 0.4530 | 0.5346 | 0.0016 |
| 5550 | 3624 | 0.5532 | 0.4534 | 0.5349 | 0.0183 |
| 5600 | 3624 | 0.5527 | 0.4530 | 0.5391 | 0.0136 |
| 5650 | 3624 | 0.5578 | 0.4523 | 0.5324 | 0.0254 |
| 5700 | 3624 | 0.5563 | 0.4512 | 0.5221 | 0.0342 |
| 5750 | 3624 | 0.5561 | 0.4529 | 0.5411 | 0.0150 |
| 5800 | 3624 | 0.5564 | 0.4550 | 0.5477 | 0.0087 |
| 5850 | 3624 | 0.5623 | 0.4540 | 0.5361 | 0.0261 |
| 5900 | 3624 | 0.5504 | 0.4550 | 0.5332 | 0.0172 |
| 5950 | 3604 | 0.5504 | 0.4545 | 0.5456 | 0.0048 |
| 6000 | 3554 | 0.5466 | 0.4515 | 0.5339 | 0.0126 |
| 6050 | 3504 | 0.5571 | 0.4486 | 0.5313 | 0.0258 |
| 6100 | 3454 | 0.5567 | 0.4457 | 0.5245 | 0.0322 |
| 6150 | 3404 | 0.5563 | 0.4437 | 0.5254 | 0.0309 |
| 6200 | 3354 | 0.5997 | 0.4408 | 0.5206 | 0.0792 |
| 6250 | 3304 | 0.6031 | 0.4378 | 0.5291 | 0.0740 |
| 6300 | 3254 | 0.5928 | 0.4347 | 0.5233 | 0.0695 |
| 6350 | 3204 | 0.5894 | 0.4325 | 0.5227 | 0.0667 |
| 6400 | 3154 | 0.5895 | 0.4315 | 0.5213 | 0.0681 |
| 6450 | 3104 | 0.6020 | 0.4281 | 0.5134 | 0.0887 |
| 6500 | 3054 | 0.6139 | 0.4270 | 0.5147 | 0.0991 |
| 6550 | 3004 | 0.6030 | 0.4233 | 0.5132 | 0.0898 |
| 6600 | 2954 | 0.5960 | 0.4206 | 0.5132 | 0.0828 |
| 6650 | 2904 | 0.6043 | 0.4196 | 0.5132 | 0.0911 |

## Confirm (200 shuffles; selection-fair null = each shuffled key's best share over all 134 offsets)
| point | real | shuf mean | p95 | max | margin vs max | margin vs fair null | rank |
|---|---|---|---|---|---|---|---|
| best s = 6500 | 0.6139 | 0.4311 | 0.5017 | 0.5565 | 0.0574 | **0.0357** | 1/201 |
| grid 6650 | 0.6043 | 0.4265 | 0.4980 | 0.5573 | 0.0469 | 0.0260 | 1/201 |
| registered R = 6655 | 0.6049 | 0.4264 | 0.4980 | 0.5573 | 0.0476 | **0.0267** | 1/201 |

Selection-fair null over the scan: mean 0.4838, p95 0.5460, max 0.5782. Consistency check: R = 6655 reproduces the build's
registered control (real 0.6049, margin vs 200-shuffle max 0.0476, as in DV1c's f.103r base row), so the re-pointed scan measures the
same quantity the S2 record does.

## Gate (declared in the PREREG)
- Arm 1, R is the argmax within one 50-letter step: **fails** -- best 6500, 155 letters before R (6650 and 6655 are 2nd/near-2nd at
  0.6043/0.6049, 0.009-0.010 below the best; the top is a flat plateau, not a distinct peak).
- Arm 2, R's selection-fair margin >= 0.03: **fails** -- 0.0267 (the best offset itself clears it at 0.0357).
Reading (not a gate): unlike f.102r (DV1c, ~750 letters late, R near-null), f.103r's registered alignment sits on the same plateau
as the best offset and beats every shuffled key at every point; the miss is 155 letters and 0.003 of fair margin. Nothing built,
nothing re-scored; any re-anchor is a separate PREREG.

## Inputs (commit, sha256 first 16)
| file | commit | sha256 |
|---|---|---|
| benchmark-tx/build_vivonne_f102r.py | 26f016500 | 49f01caf40ca55fd |
| benchmark-tx/build_vivonne_confirm2.py | ed1d53fe8 | df585f0e74ead75a |
| benchmark-tx/txeng2/viv102anchor/anchor.py | ed1d53fe8 | 07a3782a4efd0860 |
| benchmark-tx/txeng2/viv102anchor/j0scan.py | ed1d53fe8 | 4476e2fb5f1be4ef |
| benchmark-tx/txeng2/viv102anchor/j0confirm.py | ed1d53fe8 | df3e3e07ac08859b |
| ciphers/fr16104-vivonne-spain-1572/tx/vivk_result.json | ed1d53fe8 | e2447da60add9953 |
| ciphers/fr16104-vivonne-spain-1572/tx/dec_norm.txt | ed1d53fe8 | 2d6384b1d24d5654 |
| ciphers/fr16104-vivonne-spain-1572/tx/f102r_rec.tsv | ed1d53fe8 | 2cbc1f6551f0f439 |
| ciphers/fr16104-vivonne-spain-1572/tx/f102v_rec.tsv | ed1d53fe8 | a3198acaf500ede6 |
| ciphers/fr16104-vivonne-spain-1572/tx/f103r_rec.tsv | ed1d53fe8 | 4deb88c03997d652 |
| ciphers/fr16104-vivonne-spain-1572/key.tsv | ed1d53fe8 | 7e3e758f6c6751ff |
| ciphers/fr16104-vivonne-spain-1572/key_tomokiyo.tsv | ed1d53fe8 | 7dcbefed896039e9 |
| tools/stream_align.py | ed1d53fe8 | d970a9f78e9ad68e |
| benchmark-tx/txeng2/scan103/scan103.py | this commit | 61e0d084cf54659b |

Outputs: scan.json, confirm.json, confirm.out. Network requests: 0. Openings of eval truth: 0 (the truth TSV, its outputs folder,
txeng2/s2score/ and every c106_f103r crop were never opened; no truth value, plain letter run or decode printed; vivk_result.json
read by script for j0 only). Wall clock: scan ~5 min, confirm ~18 min on 4 processes.

Verdict: measured: NOT BEST: registered 6655 (real 0.6049, selection-fair margin 0.0267) best 6500 (real 0.6139, selection-fair margin 0.0357), 155 letters apart; margin at registered below the 0.03 gate
