# R2-1 log

| time (UTC) | step | result |
|---|---|---|
| 07:17 | PREREG.md + r21.py committed (f2c2160a) before any real score | -- |
| 07:17 | first calibration launch wrote every job to one file (argv slip); killed, restarted, nothing scored from it | -- |
| 07:19 | real scores a, b, c, raw (`real_*.json`) | pair a 2.84, b 2.56, c 0.27, raw 0.96 |
| 07:18-07:22 | calibration, 2,880 pairs (`calib_*.jsonl`) | gates pass: a 0.85, b 0.938, c 0.958, raw 0.955 |
| 07:22 | analyze.py -> result.json, RESULT.md | b, c, raw NULL (<= 1-2/40); a NULL by threshold but 10/40 FR-HOMO as low: kill not met |
