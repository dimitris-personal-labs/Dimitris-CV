#!/usr/bin/env python3
"""Read citation metrics from the public Google Scholar profile and save them
to data/scholar.js for the website.

Usage (from the repository folder):

    python3 tools/update_scholar.py

Runs automatically every week through .github/workflows/update-scholar.yml.
Google Scholar has no official API, so this reads the public profile page.
If Google refuses the request (for example with a "robot check" page), the
script leaves the existing numbers untouched and exits without error.
Uses only the Python standard library.
"""

import datetime
import json
import os
import re
import sys
import urllib.request

SCHOLAR_ID = "HO6cbW8AAAAJ"
PROFILE_URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "scholar.js")


def fetch(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/130.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse(page):
    rows = dict(
        (name, (int(total), int(recent)))
        for name, total, recent in re.findall(
            r'<td class="gsc_rsb_sc1"><a[^>]*>([^<]+)</a></td>'
            r'<td class="gsc_rsb_std">(\d+)</td><td class="gsc_rsb_std">(\d+)</td>', page)
    )
    if not {"Citations", "h-index", "i10-index"} <= rows.keys():
        return None

    since = re.search(r'<th class="gsc_rsb_sth">Since (\d{4})</th>', page)
    years = [int(y) for y in re.findall(r'<span class="gsc_g_t"[^>]*>(\d{4})</span>', page)]
    counts = [int(c) for c in re.findall(r'<span class="gsc_g_al">(\d+)</span>', page)]
    per_year = ([{"year": y, "count": c} for y, c in zip(years, counts)]
                if years and len(years) == len(counts) else [])

    return {
        "citations": rows["Citations"][0],
        "citationsRecent": rows["Citations"][1],
        "hIndex": rows["h-index"][0],
        "hIndexRecent": rows["h-index"][1],
        "i10Index": rows["i10-index"][0],
        "i10IndexRecent": rows["i10-index"][1],
        "recentSince": int(since.group(1)) if since else None,
        "citationsPerYear": per_year,
    }


def read_existing():
    try:
        text = open(OUT, encoding="utf-8").read()
        return json.loads(text[text.index("{"):text.rindex("}") + 1])
    except (OSError, ValueError):
        return None


def main():
    try:
        page = fetch(PROFILE_URL)
    except Exception as exc:  # network error, HTTP 429, ...
        print(f"Could not reach Google Scholar ({exc}); keeping the existing numbers.")
        return 0

    stats = parse(page)
    if stats is None:
        print("Google Scholar did not return the profile (possibly a robot check); "
              "keeping the existing numbers.")
        return 0

    existing = read_existing() or {}
    old = {k: existing.get(k) for k in stats}
    if old == stats:
        print("No change:", stats["citations"], "citations, h-index", stats["hIndex"])
        return 0

    data = {
        "profile": f"https://scholar.google.com/citations?user={SCHOLAR_ID}",
        "updated": datetime.date.today().isoformat(),
        **stats,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("// Google Scholar metrics, written by tools/update_scholar.py.\n"
                "// Updated automatically every week; don't edit by hand.\n"
                "window.CV_SCHOLAR = " + json.dumps(data, indent=2) + ";\n")
    print("Updated:", data["citations"], "citations, h-index", data["hIndex"],
          "i10-index", data["i10Index"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
