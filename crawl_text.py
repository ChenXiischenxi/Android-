#!/usr/bin/env python3
"""抓取 runoob 教程正文与图片，按有无代码块分流。

- 有代码块的页 -> ~/workspace/text/<tutorial>/<file>.md（正文+图片）
- 无代码块的页 -> ~/workspace/nocode/<tutorial>/<file>.md（供 build_manual.py 回填）
- 图片下载到 ~/workspace/images/，正文原位内嵌，并在文末附编号清单

用法: python3 crawl_text.py [--only kotlin|android] [--limit N]
"""
import os
import re
import json
import time
import argparse
import urllib.request
import urllib.error
from html.parser import HTMLParser

ROOT = os.path.expanduser("~/workspace")
CRAWL = os.path.join(ROOT, "crawled")
TEXT = os.path.join(ROOT, "text")
NOCODE = os.path.join(ROOT, "nocode")
IMAGES = os.path.join(ROOT, "images")
UA = ("Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Mobile Safari/537.36")
REFERER = "https://www.runoob.com/"

_img_registry = {}
_img_used = set()
_img_failed = []


def fetch(url, retries=3):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Referer": REFERER})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", errors="replace")
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.2 * (i + 1))
    raise last


def norm_img(src):
    if not src:
        return ""
    if src.startswith("//"):
        return "https:" + src
    if src.startswith("/"):
        return "https://www.runoob.com" + src
    if src.startswith("http"):
        return src
    return ""


def local_name(url):
    base = url.split("?")[0].split("#")[0].rstrip("/").split("/")[-1]
    base = re.sub(r"[^\w.\-]", "_", base) or "img"
    if url in _img_registry:
        return _img_registry[url]
    stem, ext = os.path.splitext(base)
    name, i = base, 1
    while name in _img_used:
        i += 1
        name = f"{stem}-{i}{ext}"
    _img_used.add(name)
    _img_registry[url] = name
    return name


def download(url):
    name = local_name(url)
    path = os.path.join(IMAGES, name)
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return name
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Referer": REFERER})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    if not data:
        raise ValueError("empty body")
    with open(path, "wb") as f:
        f.write(data)
    return name


def extract_body(html):
    """取 div.article-body 的内部 HTML（按 div 深度配对）。"""
    m = re.search(r'<div\s+class="[^"]*\barticle-body\b[^"]*"[^>]*>', html, re.I)
    if not m:
        return None
    start = m.end()
    tag_re = re.compile(r"<(/?)div\b[^>]*>", re.I)
    depth, pos = 1, start
    while depth > 0:
        tm = tag_re.search(html, pos)
        if not tm:
            return html[start:]
        depth += -1 if tm.group(1) else 1
        pos = tm.end()
        if depth == 0:
            return html[start:tm.start()]
    return html[start:]


def remove_div_class(html, cls):
    """按 div 深度删除指定 class 的 div 块（支持嵌套 div）。"""
    out, i = [], 0
    pat = re.compile(r'<div\s+[^>]*class="[^"]*\b' + cls + r'\b[^"]*"[^>]*>', re.I)
    tag_re = re.compile(r"<(/?)div\b[^>]*>", re.I)
    while True:
        m = pat.search(html, i)
        if not m:
            out.append(html[i:])
            break
        out.append(html[i:m.start()])
        depth, pos = 1, m.end()
        while depth > 0:
            tm = tag_re.search(html, pos)
            if not tm:
                pos = len(html)
                break
            depth += -1 if tm.group(1) else 1
            pos = tm.end()
        i = pos
    return "".join(out)


def clean_body(html):
    html = re.sub(r"<(script|style)\b.*?</\1>", "", html, flags=re.S | re.I)
    html = remove_div_class(html, "example")
    html = re.sub(r"<pre\b[^>]*>.*?</pre>", "", html, flags=re.S | re.I)
    html = re.sub(r'<h[1-6][^>]*class="[^"]*\bexample\b[^"]*"[^>]*>.*?</h[1-6]>', "", html,
                  flags=re.S | re.I)
    return html


class Renderer(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self.buf = []
        self.fmt = []
        self.links = []
        self.quote = 0
        self.images = []

    def _flush(self):
        text = "".join(self.buf).replace("\u00a0", " ")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n\s*\n+", "\n", text)
        text = text.strip()
        if text:
            if self.quote > 0:
                text = "\n".join(("> " + ln) if ln.strip() else ">" for ln in text.split("\n"))
            self.blocks.append(text)
        self.buf = []

    def _img(self, attrs):
        url = norm_img(dict(attrs).get("src") or "")
        if not url or "qrcode" in url or url.startswith("data:"):
            return
        self.images.append(url)
        self.buf.append("{{IMG:%s}}" % url)

    def handle_starttag(self, tag, attrs):
        cls = dict(attrs).get("class") or ""
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._flush()
            self.buf.append("\n" + "#" * int(tag[1]) + " ")
        elif tag == "p":
            self._flush()
        elif tag in ("td", "th"):
            self.buf.append(" | ")
        elif tag in ("ul", "ol"):
            self._flush()
        elif tag == "li":
            self._flush()
            self.buf.append("- ")
        elif tag == "blockquote":
            self._flush()
            self.quote += 1
        elif tag == "br":
            self.buf.append("\n")
        elif tag == "hr":
            self._flush()
            self.blocks.append("---")
        elif tag in ("strong", "b"):
            self.buf.append("**")
            self.fmt.append((tag, "**"))
        elif tag in ("em", "i"):
            self.buf.append("*")
            self.fmt.append((tag, "*"))
        elif tag in ("code", "tt"):
            self.buf.append("`")
            self.fmt.append((tag, "`"))
        elif tag == "span":
            if "marked" in cls.split():
                self.buf.append("`")
                self.fmt.append((tag, "`"))
            else:
                self.fmt.append((tag, ""))
        elif tag == "a":
            self.links.append(dict(attrs).get("href") or "")
            self.buf.append("[")
        elif tag == "img":
            self._img(attrs)

    def handle_startendtag(self, tag, attrs):
        if tag == "br":
            self.buf.append("\n")
        elif tag == "img":
            self._img(attrs)

    def handle_endtag(self, tag):
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "div",
                   "table", "tr", "ul", "ol", "blockquote"):
            self._flush()
            if tag == "blockquote":
                self.quote = max(0, self.quote - 1)
            return
        if tag == "a":
            href = self.links.pop() if self.links else ""
            self.buf.append(("](%s)" % href) if href else "]")
            return
        if self.fmt and self.fmt[-1][0] == tag:
            _, cm = self.fmt.pop()
            if cm:
                self.buf.append(cm)

    def handle_data(self, data):
        self.buf.append(data)


def render_body(html):
    body_html = extract_body(html)
    if body_html is None:
        return None, []
    r = Renderer()
    try:
        r.feed(clean_body(body_html))
    except Exception:  # noqa: BLE001
        pass
    r._flush()
    blocks = r.blocks
    if blocks and re.match(r"^#\s", blocks[0]):
        blocks = blocks[1:]
    return "\n\n".join(blocks), r.images


def process_images(urls):
    num_map, order = {}, []
    for u in urls:
        if u not in num_map:
            num_map[u] = len(order) + 1
            order.append(u)
    result = []
    for u in order:
        try:
            result.append((num_map[u], u, download(u), None))
        except Exception as e:  # noqa: BLE001
            result.append((num_map[u], u, None, str(e)))
            _img_failed.append((u, str(e)))
    return num_map, result


def substitute(text, num_map, name_by_url):
    def repl(m):
        u = m.group(1)
        n, name = num_map.get(u), name_by_url.get(u)
        if not n or not name:
            return ""
        return "![图%d](../../images/%s)" % (n, name)
    return re.sub(r"\{\{IMG:(.*?)\}\}", repl, text)


def image_section(result):
    lines = ["### 图片清单", ""]
    for n, u, name, err in result:
        if name:
            lines.append("%d. 图%d -> images/%s （原图：%s）" % (n, n, name, u))
        else:
            lines.append("%d. 图%d -> 下载失败：%s" % (n, n, u))
    return "\n".join(lines)


def crawl(tutorial, limit=None):
    with open(os.path.join(CRAWL, tutorial, "index.json"), encoding="utf-8") as f:
        index = json.load(f)
    os.makedirs(IMAGES, exist_ok=True)
    os.makedirs(os.path.join(TEXT, tutorial), exist_ok=True)
    os.makedirs(os.path.join(NOCODE, tutorial), exist_ok=True)
    pages = index[:limit] if limit else index
    s = {"text": 0, "nocode": 0, "img": 0, "fail": 0}
    for i, p in enumerate(pages, 1):
        url = p["url"]
        try:
            html = fetch(url)
            body, imgs = render_body(html)
        except Exception as e:  # noqa: BLE001
            print(f"[{i}/{len(pages)}] FAIL {url}: {e}")
            s["fail"] += 1
            continue
        if body is None:
            print(f"[{i}/{len(pages)}] NO-BODY {url}")
            body = ""
        num_map, result = process_images(imgs)
        name_by_url = {u: nm for (n, u, nm, _) in result if nm}
        body = substitute(body, num_map, name_by_url)
        if result:
            body = (body + "\n\n" + image_section(result)).strip()
        s["img"] += len(result)

        fname = p["file"]
        if p.get("codes", 0) > 0:
            content = f"# {p['title']}\n\n> 来源: {url}\n\n{body}\n"
            with open(os.path.join(TEXT, tutorial, fname), "w", encoding="utf-8") as f:
                f.write(content)
            s["text"] += 1
            dest = "text"
        else:
            with open(os.path.join(NOCODE, tutorial, fname), "w", encoding="utf-8") as f:
                f.write(body + "\n")
            s["nocode"] += 1
            dest = "nocode"
        print(f"[{i}/{len(pages)}] {p['title']} -> {dest} ({len(result)} imgs)")
        time.sleep(0.3)
    print(f"== {tutorial}: text={s['text']} nocode={s['nocode']} imgs={s['img']} fail={s['fail']}")
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=["kotlin", "android"])
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()
    if args.only != "android":
        crawl("kotlin", args.limit)
    if args.only != "kotlin":
        crawl("android", args.limit)
    if _img_failed:
        print(f"== 图片下载失败 {len(_img_failed)} 个：")
        for u, e in _img_failed[:20]:
            print(f"   {u}  ({e})")


if __name__ == "__main__":
    main()
