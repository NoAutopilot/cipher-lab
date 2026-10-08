# H77 -- reader-free dot-position statistic (TOMO-ARM wave 2, 8 Oct 2026, written before any score)

Question: does the position of small marks (dots) relative to the nearest stroke carry a system signature that
separates two period shorthand systems on their own specimens? Only if it does is Armstrong's distribution measured.

Instrument (h77/dotpos.py, no model reader): binarise (Otsu), connected components (8-conn). A component is a DOT if
its bounding-box area < 0.15 x the median area of components on the same image and its aspect ratio is < 2.5; a
STROKE if area >= 0.5 x median. For each dot: the nearest stroke by centre distance (within 3 x median stroke height);
vertical class = above / level / below (dot centre vs stroke box: above top+25% of height, below bottom-25%, else
level); horizontal class = start / middle / end (thirds of the stroke box width, outside = nearest third).
Feature = 9-cell histogram (3 x 3) + dot share (dots / (dots + strokes)).

Control (must be able to fail): specimens on disk, h24/specimens/mavor_plateV_line{1-4}.jpg and
byrom_plateI_line{1-4}.jpg. Split each system into halves A = lines 1-2, B = lines 3-4. Distance = Jensen-Shannon
divergence (base 2) of the 9-cell histograms. Statistic: cross = mean JSD over the 4 cross-system half pairs;
within = mean of JSD(MavorA, MavorB) and JSD(ByromA, ByromB).
GATE (control): cross > within AND a permutation test (dots' system labels permuted across all 8 lines, keeping
line membership, 2000 permutations, seed 20261008) gives p <= 0.01 for the cross-minus-within difference, AND each
system has >= 40 dots. If the gate fails: logged "untested-by-this-tool", Armstrong not scored.
If the gate passes: Armstrong (h74 sorter tiles via their source line crops -- here the line crops images/shorthand/*.jpg,
same pipeline) is reported as JSD to each system with a bootstrap (by line) 95% interval. Reported only as a
likeness ordering between these two systems; not evidence for either system (neither may be right), no reading.
One run, no threshold tuning after seeing numbers.
