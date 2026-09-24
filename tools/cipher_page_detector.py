#!/usr/bin/env python3
"""Cipher-page layout detector: numpy+PIL only, no OCR.

Scores a page image (or a IIIF canvas fetched at 400 px width) for whether its
LAYOUT looks like an invented-symbol or numeral cipher page rather than running
prose: ink concentrated in short, isolated, spaced tokens (numeral groups,
invented signs) instead of long connected cursive runs; irregular token/gap
widths; a second, thinner interlinear row between main lines. It reads no
character shapes and does no OCR -- it is a pre-filter, not a transcriber.

Usage:
  python3 tools/cipher_page_detector.py --help
  python3 tools/cipher_page_detector.py --fit labels.tsv [--weights FILE]
      labels.tsv columns (tab-separated, header required): path, label, split
      label in {cipher, plain}; split in {train, holdout}. Fits a logistic
      model on the train rows, standardizes on train statistics, reports
      precision/recall/FPR on train and holdout, writes weights JSON.
  python3 tools/cipher_page_detector.py --score IMAGE [--weights FILE]
      Prints one score line (0..1) and the feature vector for a single image.
  python3 tools/cipher_page_detector.py --scan MANIFEST_URL --out DIR
      [--weights FILE] [--max-canvases 300] [--delay 1.5]
      Walks a IIIF v2/v3 manifest one canvas at a time (one request in
      flight, --delay seconds apart, browser User-Agent, at most
      --max-canvases thumbnails), fetches each canvas at width 400 to
      DIR/images/, writes DIR/images/manifest.json (fetch record) and
      DIR/scores.tsv (canvas, label, score, features...). Stops on HTTP
      403/429 or a challenge page; no retry loop (good-citizen rule).

Controls, 24 Sept 2026 (worker detIMG; sources/detector-img/labels.tsv, 41 cipher-page
images from 10 hands -- Gramont, Danzay, Salviati, Seure, Lodewijk van Nassau, August
van Saksen, Blathwayt, Eckert (1862+1864 ledgers), Le Tellier/Brienne fr.5160, Carpi --
plus 43 plain/printed negatives, mostly matched same-dossier controls; held out a third
per class): train n=57 precision=0.808 recall=0.750 fpr=0.172; HOLDOUT n=27
precision=0.750 recall=0.692 fpr=0.214. Gate (recall>=0.85, fpr<=0.15): **FAIL**.
One round of feature changes tried (--autocrop, cropping to the ink bounding box before
the 400px resize, to normalize scale between tight crops and wide-margin full-page
scans): made it worse (holdout recall 0.692->0.538, fpr 0.214->0.286), reverted to
non-default. Per brief: stopped here, no sweep run. Reproduce with
`python3 tools/cipher_page_detector.py --fit sources/detector-img/labels.tsv
--weights tools/cipher_page_detector_weights.json`. See QUEUE.md 'Image detector
(24 Sept 2026)' for what separates and what does not.

Offline test: python3 tools/tests/test_cipher_page_detector.py (4 synthetic
fixtures under tools/tests/fixtures/, no network).
"""
import argparse
import json
import math
import os
import sys
import time
import urllib.request
import urllib.error

import numpy as np
from PIL import Image

USER_AGENT = "cipher-lab research script (contact via repository)"

FEATURE_NAMES = [
    "line_count",
    "tokens_per_line_mean",
    "token_width_norm_mean",
    "token_width_cv",
    "gap_norm_mean",
    "gap_cv",
    "small_token_ink_fraction",
    "token_extent_cv",
    "spacing_norm_mean",
    "spacing_cv",
    "interlinear_fraction",
    "ink_density",
]

DEFAULT_WEIGHTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "cipher_page_detector_weights.json")


# ---------------------------------------------------------------------------
# Image loading and binarization
# ---------------------------------------------------------------------------

def load_gray(path_or_image, target_width=400):
    if isinstance(path_or_image, Image.Image):
        im = path_or_image
    else:
        im = Image.open(path_or_image)
    im = im.convert("L")
    w, h = im.size
    if w != target_width:
        new_h = max(1, round(h * target_width / w))
        im = im.resize((target_width, new_h), Image.BILINEAR)
    return np.asarray(im, dtype=np.uint8)


def load_gray_autocrop(path_or_image, coarse_width=900, final_width=400, margin_frac=0.02):
    """Load, crop tightly to the ink content's bounding box (drops blank
    margins so a wide-bordered full-page scan and a tight crop of the same
    text end up at comparable character scale after the final resize), then
    resize to final_width. Falls back to the uncropped image if no ink is
    found (blank page) or the content already fills the frame."""
    coarse = load_gray(path_or_image, target_width=coarse_width)
    ink = ink_mask(coarse)
    row_profile = ink.mean(axis=1)
    col_profile = ink.mean(axis=0)
    row_active = np.nonzero(row_profile > 0.01)[0]
    col_active = np.nonzero(col_profile > 0.01)[0]
    if len(row_active) == 0 or len(col_active) == 0:
        return load_gray(path_or_image, target_width=final_width)
    h, w = coarse.shape
    top, bot = row_active[0], row_active[-1] + 1
    left, right = col_active[0], col_active[-1] + 1
    pad_r = max(1, int((bot - top) * margin_frac))
    pad_c = max(1, int((right - left) * margin_frac))
    top = max(0, top - pad_r)
    bot = min(h, bot + pad_r)
    left = max(0, left - pad_c)
    right = min(w, right + pad_c)
    cropped = coarse[top:bot, left:right]
    im = Image.fromarray(cropped)
    cw, ch = im.size
    new_h = max(1, round(ch * final_width / cw))
    im = im.resize((final_width, new_h), Image.BILINEAR)
    return np.asarray(im, dtype=np.uint8)


def otsu_threshold(gray):
    hist, _ = np.histogram(gray, bins=256, range=(0, 256))
    hist = hist.astype(np.float64)
    total = hist.sum()
    if total == 0:
        return 127
    sum_all = float(np.dot(np.arange(256), hist))
    sum_b = 0.0
    weight_b = 0.0
    best_var = -1.0
    threshold = 127
    for t in range(256):
        weight_b += hist[t]
        if weight_b == 0:
            continue
        weight_f = total - weight_b
        if weight_f == 0:
            break
        sum_b += t * hist[t]
        mean_b = sum_b / weight_b
        mean_f = (sum_all - sum_b) / weight_f
        var_between = weight_b * weight_f * (mean_b - mean_f) ** 2
        if var_between > best_var:
            best_var = var_between
            threshold = t
    return threshold


def ink_mask(gray):
    t = otsu_threshold(gray)
    below = gray < t
    # treat the minority class as ink, robust to scans with a dark surround
    if below.mean() > 0.5:
        return ~below
    return below


# ---------------------------------------------------------------------------
# Line-band and token segmentation
# ---------------------------------------------------------------------------

def _runs(mask_1d):
    """Contiguous True runs of a 1-D boolean array as (start, end) half-open."""
    runs = []
    n = len(mask_1d)
    i = 0
    while i < n:
        if mask_1d[i]:
            j = i + 1
            while j < n and mask_1d[j]:
                j += 1
            runs.append((i, j))
            i = j
        else:
            i += 1
    return runs


def _merge_runs(runs, max_gap):
    if not runs:
        return runs
    merged = [runs[0]]
    for s, e in runs[1:]:
        ps, pe = merged[-1]
        if s - pe <= max_gap:
            merged[-1] = (ps, e)
        else:
            merged.append((s, e))
    return merged


def find_line_bands(ink):
    h, w = ink.shape
    row_profile = ink.mean(axis=1)
    win = max(3, h // 250)
    kernel = np.ones(win) / win
    smoothed = np.convolve(row_profile, kernel, mode="same")
    peak = smoothed.max()
    if peak <= 0:
        return [], []
    row_thresh = max(0.02, peak * 0.15)
    active = smoothed > row_thresh
    runs = _runs(active)
    runs = _merge_runs(runs, max_gap=max(1, h // 400))
    bands = [(s, e) for s, e in runs if (e - s) >= max(2, h // 500)]
    if not bands:
        return [], []
    heights = np.array([e - s for s, e in bands], dtype=np.float64)
    median_h = float(np.median(heights))
    primary = [(s, e) for (s, e), ht in zip(bands, heights) if ht >= 0.6 * median_h]
    secondary = [(s, e) for (s, e), ht in zip(bands, heights) if ht < 0.6 * median_h]
    return primary, secondary


def find_tokens(ink, band, min_gap_frac=0.3):
    top, bot = band
    height = max(1, bot - top)
    col_profile = ink[top:bot, :].mean(axis=0)
    peak = col_profile.max()
    if peak <= 0:
        return []
    col_thresh = max(0.05, peak * 0.12)
    active = col_profile > col_thresh
    runs = _runs(active)
    min_gap = max(2, height * min_gap_frac)
    runs = _merge_runs(runs, max_gap=min_gap)
    tokens = []
    for s, e in runs:
        sub = ink[top:bot, s:e]
        rows_with_ink = np.any(sub, axis=1)
        if rows_with_ink.any():
            idx = np.nonzero(rows_with_ink)[0]
            extent = int(idx[-1] - idx[0] + 1)
        else:
            extent = 1
        tokens.append({
            "start": s, "end": e, "width": e - s,
            "extent": extent, "ink": int(sub.sum()),
        })
    return tokens


# ---------------------------------------------------------------------------
# Feature extraction
# ---------------------------------------------------------------------------

def _mean(xs):
    return float(np.mean(xs)) if len(xs) else 0.0


def _cv(xs):
    xs = np.asarray(xs, dtype=np.float64)
    if len(xs) < 2:
        return 0.0
    m = xs.mean()
    if m <= 1e-9:
        return 0.0
    return float(xs.std() / m)


def extract_features(gray):
    ink = ink_mask(gray)
    primary, secondary = find_line_bands(ink)

    line_count = len(primary)
    if line_count == 0:
        feats = {name: 0.0 for name in FEATURE_NAMES}
        feats["ink_density"] = float(ink.mean())
        return feats

    band_heights = [e - s for s, e in primary]
    h_unit = float(np.median(band_heights)) if band_heights else 1.0
    h_unit = max(h_unit, 1.0)

    all_widths, all_extents, all_ink, all_gaps = [], [], [], []
    tokens_per_line = []
    for band in primary:
        toks = find_tokens(ink, band)
        tokens_per_line.append(len(toks))
        for tok in toks:
            all_widths.append(tok["width"])
            all_extents.append(tok["extent"])
            all_ink.append(tok["ink"])
        for a, b in zip(toks, toks[1:]):
            all_gaps.append(b["start"] - a["end"])

    total_ink = sum(all_ink) if all_ink else 0
    small_ink = sum(i for w, i in zip(all_widths, all_ink) if w <= 1.3 * h_unit)
    small_token_ink_fraction = (small_ink / total_ink) if total_ink > 0 else 0.0

    centers = [(s + e) / 2.0 for s, e in primary]
    spacings = [b - a for a, b in zip(centers, centers[1:])]

    interlinear_gaps = 0
    for i in range(len(primary) - 1):
        top_end = primary[i][1]
        bot_start = primary[i + 1][0]
        if any(s >= top_end and e <= bot_start for s, e in secondary):
            interlinear_gaps += 1
    interlinear_fraction = (interlinear_gaps / (len(primary) - 1)) if len(primary) > 1 else 0.0

    feats = {
        "line_count": float(line_count),
        "tokens_per_line_mean": _mean(tokens_per_line),
        "token_width_norm_mean": _mean(all_widths) / h_unit,
        "token_width_cv": _cv(all_widths),
        "gap_norm_mean": _mean(all_gaps) / h_unit,
        "gap_cv": _cv(all_gaps),
        "small_token_ink_fraction": float(small_token_ink_fraction),
        "token_extent_cv": _cv(all_extents),
        "spacing_norm_mean": _mean(spacings) / h_unit,
        "spacing_cv": _cv(spacings),
        "interlinear_fraction": float(interlinear_fraction),
        "ink_density": float(ink.mean()),
    }
    return feats


def feature_vector(feats):
    return np.array([feats[name] for name in FEATURE_NAMES], dtype=np.float64)


# ---------------------------------------------------------------------------
# Logistic model: fit (numpy gradient descent) and score
# ---------------------------------------------------------------------------

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))


def fit_logistic(X, y, lr=0.2, l2=0.02, iters=3000):
    n, d = X.shape
    w = np.zeros(d)
    b = 0.0
    y = y.astype(np.float64)
    for _ in range(iters):
        z = X.dot(w) + b
        p = sigmoid(z)
        grad_w = X.T.dot(p - y) / n + l2 * w
        grad_b = (p - y).mean()
        w -= lr * grad_w
        b -= lr * grad_b
    return w, b


def standardize_fit(X):
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    std[std < 1e-9] = 1.0
    return mean, std


def standardize_apply(X, mean, std):
    return (X - mean) / std


def metrics_at(y_true, scores, threshold=0.5):
    y_true = np.asarray(y_true)
    pred = (scores >= threshold).astype(int)
    tp = int(np.sum((pred == 1) & (y_true == 1)))
    fp = int(np.sum((pred == 1) & (y_true == 0)))
    fn = int(np.sum((pred == 0) & (y_true == 1)))
    tn = int(np.sum((pred == 0) & (y_true == 0)))
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    fpr = fp / (fp + tn) if (fp + tn) else 0.0
    return {
        "n": len(y_true), "tp": tp, "fp": fp, "fn": fn, "tn": tn,
        "precision": precision, "recall": recall, "false_positive_rate": fpr,
    }


# ---------------------------------------------------------------------------
# Weights I/O
# ---------------------------------------------------------------------------

def save_weights(path, mean, std, w, b, threshold, extra):
    obj = {
        "features": FEATURE_NAMES,
        "mean": mean.tolist(),
        "std": std.tolist(),
        "weights": w.tolist(),
        "bias": float(b),
        "threshold": threshold,
    }
    obj.update(extra)
    with open(path, "w") as f:
        json.dump(obj, f, indent=1)


def load_weights(path):
    with open(path) as f:
        return json.load(f)


def score_features(feats, weights_obj):
    x = feature_vector(feats)
    mean = np.array(weights_obj["mean"])
    std = np.array(weights_obj["std"])
    w = np.array(weights_obj["weights"])
    b = weights_obj["bias"]
    z = standardize_apply(x, mean, std)
    return float(sigmoid(z.dot(w) + b))


# ---------------------------------------------------------------------------
# --fit
# ---------------------------------------------------------------------------

def read_labels_tsv(path):
    rows = []
    with open(path) as f:
        header = f.readline().rstrip("\n").split("\t")
        idx = {name: i for i, name in enumerate(header)}
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            rows.append({
                "path": parts[idx["path"]],
                "label": parts[idx["label"]],
                "split": parts[idx["split"]] if "split" in idx else "train",
            })
    return rows


def cmd_fit(args):
    rows = read_labels_tsv(args.labels)
    feats_cache = []
    for row in rows:
        gray = (load_gray_autocrop if args.autocrop else load_gray)(row["path"])
        feats = extract_features(gray)
        feats_cache.append(feats)
        if args.verbose:
            print(f"  {row['path']}: {row['label']} {row['split']}", file=sys.stderr)

    train_idx = [i for i, r in enumerate(rows) if r["split"] == "train"]
    hold_idx = [i for i, r in enumerate(rows) if r["split"] == "holdout"]
    if not train_idx:
        print("no training rows (split=train)", file=sys.stderr)
        return 2

    X_all = np.array([feature_vector(f) for f in feats_cache])
    y_all = np.array([1 if r["label"] == "cipher" else 0 for r in rows])

    X_train_raw = X_all[train_idx]
    y_train = y_all[train_idx]
    mean, std = standardize_fit(X_train_raw)
    X_train = standardize_apply(X_train_raw, mean, std)

    w, b = fit_logistic(X_train, y_train)

    train_scores = sigmoid(X_train.dot(w) + b)
    train_metrics = metrics_at(y_train, train_scores)

    hold_metrics = None
    if hold_idx:
        X_hold_raw = X_all[hold_idx]
        y_hold = y_all[hold_idx]
        X_hold = standardize_apply(X_hold_raw, mean, std)
        hold_scores = sigmoid(X_hold.dot(w) + b)
        hold_metrics = metrics_at(y_hold, hold_scores)

    gate_pass = None
    if hold_metrics:
        gate_pass = hold_metrics["recall"] >= 0.85 and hold_metrics["false_positive_rate"] <= 0.15

    save_weights(args.weights, mean, std, w, b, 0.5, {
        "fitted": args.date,
        "n_train": len(train_idx),
        "n_holdout": len(hold_idx),
        "train_metrics": train_metrics,
        "holdout_metrics": hold_metrics,
        "gate_recall_ge_0.85_fpr_le_0.15": gate_pass,
        "labels_file": os.path.relpath(args.labels),
    })

    print(f"train n={len(train_idx)} precision={train_metrics['precision']:.3f} "
          f"recall={train_metrics['recall']:.3f} fpr={train_metrics['false_positive_rate']:.3f}")
    if hold_metrics:
        print(f"holdout n={len(hold_idx)} precision={hold_metrics['precision']:.3f} "
              f"recall={hold_metrics['recall']:.3f} fpr={hold_metrics['false_positive_rate']:.3f}")
        print(f"gate (recall>=0.85, fpr<=0.15): {'PASS' if gate_pass else 'FAIL'}")
    print(f"weights written to {args.weights}")
    return 0


# ---------------------------------------------------------------------------
# --score (single image)
# ---------------------------------------------------------------------------

def cmd_score(args):
    weights_obj = load_weights(args.weights)
    gray = (load_gray_autocrop if args.autocrop else load_gray)(args.score)
    feats = extract_features(gray)
    s = score_features(feats, weights_obj)
    label = "cipher" if s >= weights_obj.get("threshold", 0.5) else "plain"
    print(f"{args.score}\t{s:.4f}\t{label}")
    for name in FEATURE_NAMES:
        print(f"  {name}\t{feats[name]:.4f}", file=sys.stderr)
    return 0


# ---------------------------------------------------------------------------
# --scan (IIIF manifest walk)
# ---------------------------------------------------------------------------

def http_get(url, accept="application/json"):
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": accept,
    })
    return urllib.request.urlopen(req, timeout=30)


def iiif_canvases(manifest):
    """Yield (canvas_id, label, image_service_id) for IIIF v2 or v3 manifests."""
    items = manifest.get("sequences", [{}])[0].get("canvases") if "sequences" in manifest else manifest.get("items", [])
    for canvas in items or []:
        canvas_id = canvas.get("@id") or canvas.get("id") or ""
        label = canvas.get("label")
        if isinstance(label, dict):
            label = next(iter(label.values()), [""])[0] if label else ""
        images = canvas.get("images") or []
        service_id = None
        if images:
            resource = images[0].get("resource", {})
            service = resource.get("service", {})
            service_id = service.get("@id") or service.get("id")
        else:
            for body_item in canvas.get("items", []):
                for anno in body_item.get("items", []):
                    body = anno.get("body", {})
                    service = body.get("service")
                    if isinstance(service, list) and service:
                        service_id = service[0].get("@id") or service[0].get("id")
                    elif isinstance(service, dict):
                        service_id = service.get("@id") or service.get("id")
        yield canvas_id, label or "", service_id


def cmd_scan(args):
    weights_obj = load_weights(args.weights)
    os.makedirs(os.path.join(args.out, "images"), exist_ok=True)

    print(f"fetching manifest {args.scan}", file=sys.stderr)
    try:
        resp = http_get(args.scan)
    except urllib.error.HTTPError as e:
        print(f"manifest fetch failed: HTTP {e.code}", file=sys.stderr)
        return 2
    if resp.status in (403, 429):
        print(f"manifest fetch blocked: HTTP {resp.status}, stopping (no retry)", file=sys.stderr)
        return 2
    manifest = json.loads(resp.read())
    time.sleep(args.delay)

    fetch_log = []
    scored_rows = []
    n_fetched = 0
    for canvas_id, label, service_id in iiif_canvases(manifest):
        if n_fetched >= args.max_canvases:
            print(f"reached --max-canvases {args.max_canvases}, stopping", file=sys.stderr)
            break
        if not service_id:
            continue
        thumb_url = service_id.rstrip("/") + "/full/400,/0/default.jpg"
        safe_id = "".join(c if c.isalnum() else "_" for c in canvas_id)[-80:]
        out_path = os.path.join(args.out, "images", f"{safe_id}.jpg")
        try:
            resp = http_get(thumb_url, accept="image/jpeg")
        except urllib.error.HTTPError as e:
            if e.code in (403, 429):
                print(f"blocked on {canvas_id}: HTTP {e.code}, stopping scan (no retry)", file=sys.stderr)
                break
            print(f"fetch error on {canvas_id}: HTTP {e.code}, skipping", file=sys.stderr)
            time.sleep(args.delay)
            continue
        if resp.status in (403, 429):
            print(f"blocked on {canvas_id}: HTTP {resp.status}, stopping scan (no retry)", file=sys.stderr)
            break
        data = resp.read()
        with open(out_path, "wb") as f:
            f.write(data)
        n_fetched += 1
        fetch_log.append({"canvas": canvas_id, "label": label, "url": thumb_url, "file": out_path})

        gray = (load_gray_autocrop if args.autocrop else load_gray)(out_path)
        feats = extract_features(gray)
        s = score_features(feats, weights_obj)
        pred = "cipher" if s >= weights_obj.get("threshold", 0.5) else "plain"
        scored_rows.append((canvas_id, label, pred, s, feats))
        print(f"  {canvas_id} ({label}): score={s:.3f} {pred}", file=sys.stderr)
        time.sleep(args.delay)

    with open(os.path.join(args.out, "images", "manifest.json"), "w") as f:
        json.dump({"source_manifest": args.scan, "fetched": fetch_log,
                    "user_agent": USER_AGENT}, f, indent=1)

    with open(os.path.join(args.out, "scores.tsv"), "w") as f:
        f.write("canvas\tlabel\tpred\tscore\t" + "\t".join(FEATURE_NAMES) + "\n")
        for canvas_id, label, pred, s, feats in scored_rows:
            f.write(f"{canvas_id}\t{label}\t{pred}\t{s:.4f}\t" +
                    "\t".join(f"{feats[n]:.4f}" for n in FEATURE_NAMES) + "\n")

    print(f"fetched {n_fetched} canvases, scores written to {os.path.join(args.out, 'scores.tsv')}")
    return 0


# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--fit", metavar="LABELS_TSV", dest="labels")
    p.add_argument("--score", metavar="IMAGE")
    p.add_argument("--scan", metavar="MANIFEST_URL")
    p.add_argument("--out", metavar="DIR")
    p.add_argument("--weights", default=DEFAULT_WEIGHTS_PATH)
    p.add_argument("--max-canvases", type=int, default=300)
    p.add_argument("--delay", type=float, default=1.5)
    p.add_argument("--date", default="")
    p.add_argument("--verbose", action="store_true")
    p.add_argument("--autocrop", action="store_true",
                    help="crop to the ink content's bounding box before the 400px resize "
                         "(tried as the one round of feature changes, 24 Sept 2026: "
                         "made the held-out gate worse, recall 0.692->0.538, fpr 0.214->0.286 "
                         "-- kept as an opt-in for a future worker to retest with a larger set, "
                         "not the default)")
    args = p.parse_args()

    if args.labels:
        return cmd_fit(args)
    if args.score:
        return cmd_score(args)
    if args.scan:
        if not args.out:
            print("--scan requires --out DIR", file=sys.stderr)
            return 2
        return cmd_scan(args)
    p.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
