#!/usr/bin/env python3
"""Fake `curl` for tools/tests/test_digitarq_fetch.py: no network, serves a small
paginated file list and a 1x1 JPEG for any thumb/dissemination fileId. Mimics the
subset of `curl -sS -A UA URL [-o PATH]` that digitarq_fetch.py actually uses."""
import sys
import json
import base64

TOTAL = 5
PAGE = {
    0: [{"id": "1", "name": "m0001.jpg", "type": "IMAGE"}, {"id": "2", "name": "m0002.jpg", "type": "IMAGE"}],
    2: [{"id": "3", "name": "m0003.jpg", "type": "IMAGE"}, {"id": "4", "name": "m0004.jpg", "type": "IMAGE"}],
    4: [{"id": "5", "name": "m0005.jpg", "type": "IMAGE"}],
}

# smallest valid 1x1 JPEG, base64
TINY_JPEG = base64.b64decode(
    "/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0a"
    "HBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/wAALCAABAAEBAREA/8QAFQABAQAAAAAA"
    "AAAAAAAAAAAAAAX/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAX/"
    "xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCdABmX/9k="
)


def main():
    args = sys.argv[1:]
    url = [a for a in args if a.startswith("http")][0]
    out_path = None
    if "-o" in args:
        out_path = args[args.index("-o") + 1]

    if "/api/rdigital/thumb" in url or "/api/rdigital/dissemination" in url:
        data = TINY_JPEG
        if out_path:
            with open(out_path, "wb") as f:
                f.write(data)
        else:
            sys.stdout.buffer.write(data)
        return 0

    if "/api/rdigital/" in url:
        from_idx = 0
        if "fromIndex=" in url:
            from_idx = int(url.split("fromIndex=")[1].split("&")[0])
        results = PAGE.get(from_idx, [])
        payload = json.dumps({"results": results, "total": TOTAL, "fromIndex": from_idx})
        if out_path:
            with open(out_path, "w") as f:
                f.write(payload)
        else:
            sys.stdout.write(payload)
        return 0

    sys.stdout.write(json.dumps({"results": [], "total": 0}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
