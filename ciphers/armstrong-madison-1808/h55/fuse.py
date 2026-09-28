#!/usr/bin/env python3
"""H55: fuse the two exposures of the page-2/3 leaf-spread (NARA M34 roll 14 frames 0031 and 0032, H17) for the
shorthand line crops B35 read (images/shorthand/page2_*, page3_*). For each crop: locate it in each frame by normalized
cross-correlation (coarse at 1/4 scale, refined at native in a window), cut the same-size region from both frames,
register frame 32's region onto frame 31's with an ECC affine fit (translation+rotation+scale), average the two, and
write h55/fused/<crop>.jpg plus a side-by-side check image. Prints match scores; a crop whose native NCC is under 0.5 in
either frame is reported and not fused.
usage: python3 h55/fuse.py [OUTDIR]  (output images are not committed; h55/fuse_log.tsv is)"""
import os, sys, cv2, numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(H, "fused"); os.makedirs(out, exist_ok=True)
F = {f: cv2.imread(os.path.join(T, "images", f"M34-014-00{f}.jpg"), cv2.IMREAD_GRAYSCALE) for f in ("31", "32")}
def locate(tpl, img):
    s = 0.25
    r = cv2.matchTemplate(cv2.resize(img, None, fx=s, fy=s, interpolation=cv2.INTER_AREA),
                          cv2.resize(tpl, None, fx=s, fy=s, interpolation=cv2.INTER_AREA), cv2.TM_CCOEFF_NORMED)
    _, _, _, (x, y) = cv2.minMaxLoc(r); x, y = int(x / s), int(y / s); pad = 24
    x0, y0 = max(0, x - pad), max(0, y - pad); win = img[y0:y0 + tpl.shape[0] + 2 * pad, x0:x0 + tpl.shape[1] + 2 * pad]
    r = cv2.matchTemplate(win, tpl, cv2.TM_CCOEFF_NORMED); _, v, _, (dx, dy) = cv2.minMaxLoc(r)
    return x0 + dx, y0 + dy, v
log = ["crop\tx31\ty31\tncc31\tx32\ty32\tncc32\tecc\tstatus"]
names = sorted(f for f in os.listdir(os.path.join(T, "images", "shorthand")) if f.startswith(("page2_", "page3_")) and f.endswith(".jpg"))
for n in names:
    tpl = cv2.imread(os.path.join(T, "images", "shorthand", n), cv2.IMREAD_GRAYSCALE)
    h, w = tpl.shape; (x1, y1, v1), (x2, y2, v2) = locate(tpl, F["31"]), locate(tpl, F["32"])
    if min(v1, v2) < 0.5:
        log.append(f"{n}\t{x1}\t{y1}\t{v1:.3f}\t{x2}\t{y2}\t{v2:.3f}\t\tNOT FUSED (low match)"); continue
    a = F["31"][y1:y1 + h, x1:x1 + w].astype(np.float32); b = F["32"][y2:y2 + h, x2:x2 + w].astype(np.float32)
    warp = np.eye(2, 3, dtype=np.float32)
    try:
        cc, warp = cv2.findTransformECC(a, b, warp, cv2.MOTION_AFFINE, (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 200, 1e-5), None, 5)
    except cv2.error:
        cc = float("nan")
    b2 = cv2.warpAffine(b, warp, (w, h), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REPLICATE)
    # contrast-match the two exposures before averaging (the frames differ in exposure)
    b2 = (b2 - b2.mean()) / (b2.std() + 1e-6) * a.std() + a.mean()
    fused = np.clip((a + b2) / 2, 0, 255).astype(np.uint8)
    cv2.imwrite(os.path.join(out, n), fused, [cv2.IMWRITE_JPEG_QUALITY, 92])
    cv2.imwrite(os.path.join(out, "check_" + n), np.vstack([a.astype(np.uint8), np.clip(b2, 0, 255).astype(np.uint8), fused]), [cv2.IMWRITE_JPEG_QUALITY, 80])
    log.append(f"{n}\t{x1}\t{y1}\t{v1:.3f}\t{x2}\t{y2}\t{v2:.3f}\t{cc:.3f}\tfused")
open(os.path.join(H, "fuse_log.tsv"), "w").write("\n".join(log) + "\n"); print("\n".join(log))
