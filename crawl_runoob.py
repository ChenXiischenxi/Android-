#!/usr/bin/env python3
"""抓取菜鸟教程（runoob.com）Kotlin 教程与 Android 基础入门教程中的代码块。

用法: python3 crawl_runoob.py [--only kotlin|android]
输出: ~/workspace/crawled/<tutorial>/<序号>-<slug>.md 及 index.json
"""
import os
import re
import json
import time
import argparse
import urllib.request
import urllib.error
from html.parser import HTMLParser

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
OUT_ROOT = os.path.expanduser("~/workspace/crawled")
KOTLIN_INDEX = "https://www.runoob.com/kotlin/kotlin-tutorial.html"
ANDROID_INDEX = "https://www.runoob.com/w3cnote/android-tutorial-intro.html"
BLOCK = {"p", "li", "tr", "table", "ul", "ol", "pre", "h1", "h2", "h3", "blockquote"}


def fetch(url, retries=3):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", errors="replace")
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (i + 1))
    raise last


class CodeExtractor(HTMLParser):
    """提取 div.example_code（Kotlin）与 pre（Android）中的代码文本。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.capturing = False
        self.kind = None
        self.depth = 0
        self.buf = []
        self.blocks = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
            return
        if self.skip:
            return
        cls = dict(attrs).get("class") or ""
        if self.capturing:
            if tag == "div":
                self.depth += 1
                self.buf.append("\n")
            elif tag == "br":
                self.buf.append("\n")
            elif tag in BLOCK:
                self.buf.append("\n")
            return
        if tag == "div" and "example_code" in cls.split():
            self._begin("example_code")
        elif tag == "pre":
            self._begin("pre")

    def handle_startendtag(self, tag, attrs):
        if self.skip:
            return
        if self.capturing and tag == "br":
            self.buf.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip or not self.capturing:
            return
        if self.kind == "example_code" and tag == "div":
            self.depth -= 1
            if self.depth == 0:
                self._finish()
        elif self.kind == "pre" and tag == "pre":
            self._finish()
        elif tag in BLOCK:
            self.buf.append("\n")

    def handle_data(self, data):
        if self.skip or not self.capturing:
            return
        self.buf.append(data)

    def _begin(self, kind):
        self.capturing = True
        self.kind = kind
        self.depth = 1
        self.buf = []

    def _finish(self):
        text = clean_code("".join(self.buf))
        if text:
            self.blocks.append(text)
        self.capturing = False
        self.kind = None
        self.depth = 0
        self.buf = []


def clean_code(s):
    s = s.replace("\xa0", " ").replace("\r\n", "\n").replace("\r", "\n")
    out = []
    blank = 0
    for ln in s.split("\n"):
        ln = ln.rstrip()
        if ln.strip() == "":
            blank += 1
            if blank > 2:
                continue
        else:
            blank = 0
        out.append(ln)
    return "\n".join(out).strip("\n")


def page_title(html, fallback):
    m = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
    if not m:
        return fallback
    t = re.sub(r"\s+", " ", m.group(1)).strip()
    t = re.sub(r"\s*[|\-\u2013]\s*\u83dc\u9e1f\u6559\u7a0b.*$", "", t)
    return t or fallback


def slug_from_url(url):
    name = url.rstrip("/").split("/")[-1]
    return re.sub(r"\.html?$", "", name)


def guess_lang(code, default):
    return "xml" if code.lstrip()[:1] == "<" else default


def _dedup(urls):
    seen, out = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def discover_kotlin():
    html = fetch(KOTLIN_INDEX)
    urls = re.findall(r'href="(/kotlin/[a-z0-9\-]+\.html)"', html)
    urls = ["https://www.runoob.com" + u for u in urls]
    # 修正站内拼写错误：/kotlin/otlin-android-setup.html
    urls = [u.replace("/kotlin/otlin-", "/kotlin/kotlin-") for u in urls]
    return _dedup(urls)


def discover_android():
    html = fetch(ANDROID_INDEX)
    urls = re.findall(
        r'href="(https://www\.runoob\.com/w3cnote/android-tutorial-[a-z0-9\-]+\.html)"',
        html,
    )
    return _dedup(urls)


def crawl(name, urls, default_lang):
    out_dir = os.path.join(OUT_ROOT, name)
    os.makedirs(out_dir, exist_ok=True)
    index = []
    for i, url in enumerate(urls, 1):
        try:
            html = fetch(url)
        except Exception as e:  # noqa: BLE001
            print(f"[{i}/{len(urls)}] FAIL {url}: {e}")
            continue
        ex = CodeExtractor()
        ex.feed(html)
        title = page_title(html, slug_from_url(url))
        fname = f"{i:03d}-{slug_from_url(url)}.md"
        lines = [f"# {title}", "", f"> 来源: {url}", ""]
        codes = []
        for ci, code in enumerate(ex.blocks, 1):
            lang = guess_lang(code, default_lang)
            codes.append({"lang": lang, "code": code})
            lines += [f"## 代码块 {ci}", "", f"```{lang}", code, "```", ""]
        if not ex.blocks:
            lines += ["_（本页未提取到代码块）_", ""]
        with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        index.append({"order": i, "title": title, "url": url,
                      "file": fname, "codes": len(ex.blocks)})
        print(f"[{i}/{len(urls)}] {title} -> {fname} ({len(ex.blocks)})")
        time.sleep(0.4)
    with open(os.path.join(out_dir, "index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    total = sum(x["codes"] for x in index)
    print(f"== {name}: {len(index)} pages, {total} code blocks -> {out_dir}")
    return index


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=["kotlin", "android"])
    args = ap.parse_args()
    if args.only != "android":
        crawl("kotlin", discover_kotlin(), "kotlin")
    if args.only != "kotlin":
        crawl("android", discover_android(), "java")


if __name__ == "__main__":
    main()
