#!/usr/bin/env python3
"""DigitArq (digitarq.arquivos.pt, ANTT) codex image fetch, for a document already
identified by its docId (the 32-hex id in the fileViewer URL, from /api/docs/search
or /api/docs/details -- see QUEUE.md 'PARES / DigitArq cipher letters').

The public fileViewer works with no login (CC BY-SA 4.0 items), but its own admin-
looking endpoints (/api/rdigital/info/{repId}, /api/rdigital/files/{repId}) 401 for
an anonymous caller and /api/rdigital/{repId} (by representation id) silently returns
an empty page. The endpoint the anonymous viewer itself actually calls, found 24 Sept
2026 by network-capturing a real Chromium load of a fileViewer page (curl alone never
finds it -- it is built client-side from a different id than the ones the admin
endpoints use): GET /api/rdigital/{docId}?fromIndex=N&max=M, keyed by the *document*
id, not the representation id -- paginate over `total` for the full list, each row
{id, name, type, representationID}. That file `id` feeds two more anonymous, no-login
endpoints:
  GET /api/rdigital/thumb?fileId=ID        -- ~141x128 JPEG thumbnail
  GET /api/rdigital/dissemination?fileId=ID -- full working-resolution JPEG (~2000px
                                                wide observed on a 1657-67 codex),
                                                despite a misleading image/tiff
                                                Content-Type header; this is the same
                                                derivative the pan-zoom viewer serves.
No IIIF manifest or info.json was found; there is no bulk/tiled zoom endpoint besides
this per-page dissemination JPEG.

Usage:
  python3 tools/digitarq_fetch.py --help
  python3 tools/digitarq_fetch.py --list DOC_ID --out DIR
      Fetches the full paginated file list to DIR/filelist.json (id, name, type per
      page), one request at a time.
  python3 tools/digitarq_fetch.py --thumbs DOC_ID --out DIR --stride N [--offset K]
      Uses DIR/filelist.json (fetched first if missing) and downloads a thumbnail
      for every Nth file (by name order) starting at offset K, to DIR/thumb_NAME.jpg.
  python3 tools/digitarq_fetch.py --full DOC_ID --out DIR --names NAME1,NAME2,...
      Downloads full working-resolution dissemination JPEGs for the named files only
      (look up names from filelist.json), to DIR/full_NAME.jpg.
  python3 tools/digitarq_fetch.py --montage DIR [--per-sheet 25] [--cols 5]
      Builds labeled contact-sheet JPEGs from DIR/thumb_*.jpg (DIR/montage_NN.jpg),
      so a handful of Read calls can scan hundreds of thumbnails instead of one call
      per image.

Good-citizen rule: one request at a time, >=3s apart (digitarq.arquivos.pt has no
published rate limit but no published allowance either -- treat it as fragile), a
descriptive User-Agent, and no retry loop on 429/403/error pages -- stop and log.
Pair with tools/cipher_page_detector.py (--score/--fit) to rank thumbnails before
spending a full-res request on each; on this codex's 141x128 thumbnails, cross-checked
24 Sept 2026 against 5 top-scored full-res pulls, every hit was a false positive
(dense ordinary cursive/Latin, not cipher) -- the detector alone does not clear a page,
only prioritizes which ones to look at closer.

Offline test: python3 tools/tests/test_digitarq_fetch.py (mocks curl, no network).
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
import time

UA = "cipher-lab research script (contact via repository)"
HOST = "https://digitarq.arquivos.pt"
DELAY = 3.1


def curl_json(url, curl_bin="curl"):
    out = subprocess.run([curl_bin, "-sS", "-A", UA, url], capture_output=True, timeout=60)
    return json.loads(out.stdout)


def curl_bytes(url, path, curl_bin="curl"):
    subprocess.run([curl_bin, "-sS", "-A", UA, "-o", path, url], capture_output=True, timeout=60)


def fetch_filelist(doc_id, out_dir, page_size=600, delay=DELAY, curl_bin="curl"):
    os.makedirs(out_dir, exist_ok=True)
    time.sleep(delay)
    d = curl_json(f"{HOST}/api/rdigital/{doc_id}?fromIndex=0&max={page_size}", curl_bin)
    total = d["total"]
    results = list(d["results"])
    n_requests = 1
    while len(results) < total:
        time.sleep(delay)
        d2 = curl_json(f"{HOST}/api/rdigital/{doc_id}?fromIndex={len(results)}&max={page_size}", curl_bin)
        if not d2["results"]:
            break
        results.extend(d2["results"])
        n_requests += 1
    results.sort(key=lambda f: f["name"])
    path = os.path.join(out_dir, "filelist.json")
    with open(path, "w") as f:
        json.dump(results, f, indent=1)
    return results, n_requests


def cmd_list(args):
    files, n = fetch_filelist(args.list, args.out, delay=args.delay)
    print(f"total={len(files)} requests={n} -> {os.path.join(args.out, 'filelist.json')}")
    return 0


def cmd_thumbs(args):
    path = os.path.join(args.out, "filelist.json")
    if os.path.exists(path):
        files = json.load(open(path))
        n_requests = 0
    else:
        files, n_requests = fetch_filelist(args.thumbs, args.out, delay=args.delay)
    picks = files[args.offset::args.stride]
    print(f"stride={args.stride} offset={args.offset} picks={len(picks)}")
    for item in picks:
        out_path = os.path.join(args.out, f"thumb_{item['name']}.jpg")
        if os.path.exists(out_path):
            continue
        time.sleep(args.delay)
        curl_bytes(f"{HOST}/api/rdigital/thumb?fileId={item['id']}", out_path)
        n_requests += 1
    print(f"done, {n_requests} requests this call")
    return 0


def cmd_full(args):
    path = os.path.join(args.out, "filelist.json")
    files = json.load(open(path))
    idx = {f["name"]: f["id"] for f in files}
    names = args.names.split(",")
    n_requests = 0
    for name in names:
        fid = idx.get(name)
        if fid is None:
            print(f"  {name}: not in filelist.json, skipping", file=sys.stderr)
            continue
        out_path = os.path.join(args.out, f"full_{name}.jpg")
        if os.path.exists(out_path):
            continue
        time.sleep(args.delay)
        curl_bytes(f"{HOST}/api/rdigital/dissemination?fileId={fid}", out_path)
        n_requests += 1
    print(f"done, {n_requests} requests this call")
    return 0


def cmd_montage(args):
    from PIL import Image, ImageDraw

    def natkey(s):
        m = re.search(r"(\d+)", s)
        return int(m.group(1)) if m else 0

    paths = sorted(glob.glob(os.path.join(args.montage, "thumb_*.jpg")), key=natkey)
    if not paths:
        print("no thumb_*.jpg files found", file=sys.stderr)
        return 2
    cell_w, cell_h, label_h, pad = 160, 150, 18, 4
    cols = args.cols
    per_sheet = args.per_sheet
    written = []
    for sheet_i in range(0, len(paths), per_sheet):
        chunk = paths[sheet_i:sheet_i + per_sheet]
        rows = (len(chunk) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * (cell_w + pad) + pad, rows * (cell_h + label_h + pad) + pad), "white")
        draw = ImageDraw.Draw(sheet)
        for i, p in enumerate(chunk):
            r, c = divmod(i, cols)
            x, y = pad + c * (cell_w + pad), pad + r * (cell_h + label_h + pad)
            try:
                im = Image.open(p).convert("RGB")
                im.thumbnail((cell_w, cell_h))
                sheet.paste(im, (x + (cell_w - im.width) // 2, y + (cell_h - im.height) // 2))
            except Exception:
                draw.text((x + 2, y + 2), "ERR", fill="red")
            name = os.path.basename(p).replace("thumb_", "").replace(".jpg", "")
            m = re.search(r"(m\d+)", name)
            draw.text((x + 2, y + cell_h + 2), m.group(1) if m else name[:12], fill="black")
        out = os.path.join(args.montage, f"montage_{sheet_i // per_sheet + 1:02d}.jpg")
        sheet.save(out, quality=85)
        written.append(out)
    for p in written:
        print(p)
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--list", metavar="DOC_ID")
    p.add_argument("--thumbs", metavar="DOC_ID")
    p.add_argument("--full", metavar="DOC_ID")
    p.add_argument("--montage", metavar="DIR")
    p.add_argument("--out", metavar="DIR")
    p.add_argument("--stride", type=int, default=8)
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--names", metavar="NAME1,NAME2,...")
    p.add_argument("--delay", type=float, default=DELAY)
    p.add_argument("--per-sheet", type=int, default=25)
    p.add_argument("--cols", type=int, default=5)
    args = p.parse_args()

    if args.list:
        return cmd_list(args)
    if args.thumbs:
        if not args.out:
            print("--thumbs requires --out DIR", file=sys.stderr)
            return 2
        return cmd_thumbs(args)
    if args.full:
        if not args.out or not args.names:
            print("--full requires --out DIR and --names", file=sys.stderr)
            return 2
        return cmd_full(args)
    if args.montage:
        return cmd_montage(args)
    p.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
