#!/usr/bin/env python3
"""Sync we-mp-rss feed URLs into wechat_feeds.json."""

import json
import sqlite3
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
FEEDS_FILE = SCRIPT_DIR / "wechat_feeds.json"
WE_MP_RSS_DB = SCRIPT_DIR.parent / "tools/we-mp-rss-new/data/db.db"
WE_MP_RSS_ORIGIN = "http://localhost:8001"


def main():
    conn = sqlite3.connect(str(WE_MP_RSS_DB))
    cur = conn.cursor()
    cur.execute("SELECT mp_name, id FROM feeds ORDER BY mp_name")
    rows = cur.fetchall()
    conn.close()

    feeds = [
        {"name": name, "url": f"{WE_MP_RSS_ORIGIN}/feed/{fid}.rss"}
        for name, fid in rows
    ]

    with open(FEEDS_FILE, "w") as f:
        json.dump(feeds, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Synced {len(feeds)} feed URLs into {FEEDS_FILE}")


if __name__ == "__main__":
    main()
