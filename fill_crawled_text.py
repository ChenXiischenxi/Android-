#!/usr/bin/env python3
"""把 crawled/ 中无代码块页的占位替换为教程正文（取自 nocode/）。

用法: python3 fill_crawled_text.py
输入: crawled/{kotlin,android}/index.json + nocode/{kotlin,android}/*.md
输出: 就地更新 crawled/{kotlin,android}/<无代码页>.md
"""
import os
import json

ROOT = os.path.expanduser("~/workspace")
CRAWL = os.path.join(ROOT, "crawled")
NOCODE = os.path.join(ROOT, "nocode")


def main():
    total = 0
    for tutorial in ("kotlin", "android"):
        with open(os.path.join(CRAWL, tutorial, "index.json"), encoding="utf-8") as f:
            index = json.load(f)
        n = 0
        for p in index:
            if p.get("codes", 0) > 0:
                continue
            nc_path = os.path.join(NOCODE, tutorial, p["file"])
            if not os.path.exists(nc_path):
                print(f"MISS nocode: {tutorial}/{p['file']}")
                continue
            with open(nc_path, encoding="utf-8") as f:
                body = f.read().strip()
            out = f"# {p['title']}\n\n> 来源: {p['url']}\n\n{body}\n"
            with open(os.path.join(CRAWL, tutorial, p["file"]), "w", encoding="utf-8") as f:
                f.write(out)
            n += 1
        print(f"== {tutorial}: 补齐 {n} 个无代码块文件")
        total += n
    print(f"== 共 {total} 个")


if __name__ == "__main__":
    main()
