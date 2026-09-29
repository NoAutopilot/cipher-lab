H177c (runner 7, 29 Sept 2026): the 45 cipher rows of fr.3984 f.176v (Gallica btv1b9060633d canvas 328, native 4951x6659, fetched once,
requests.log). Centres are the row-ink peaks of the left third (x 1050-2000), region y from 600; rows rise to the right, so --track 40.
Crops are NOT committed (the folder is over the 30 MB rule); regenerate with:
  python3 cut_bands.py <native f.176v> 1050,600,3880,5060 <outdir> f176v --up 62 --down 55 --seg 1400 --overlap 120 --scale 1.0 --track 40 --centres 122,233,332,440,547,635,740,854,972,1080,1193,1289,1404,1517,1622,1733,1834,1949,2050,2169,2273,2381,2483,2603,2709,2822,2935,3043,3154,3267,3376,3485,3591,3704,3807,3924,4037,4147,4267,4383,4482,4609,4716,4826,4945
Three segments per row (s1..s3); s3 carries the page gutter shadow at its right.
