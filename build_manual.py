#!/usr/bin/env python3
"""将 crawled/ 下爬取的教程代码块按主题归并为手册章节草稿。

用法: python3 build_manual.py
输入: ~/workspace/crawled/{kotlin,android}/*.md + index.json
输出: ~/workspace/manual/{目录.md, kotlin/*.md, android/*.md}
"""
import os
import re
import json

ROOT = os.path.expanduser("~/workspace")
CRAWL = os.path.join(ROOT, "crawled")
NOCODE = os.path.join(ROOT, "nocode")
OUT = os.path.join(ROOT, "manual")

# 章名 -> 源页 order 列表（order 取自各教程 index.json）
CHAPTERS = {
    "kotlin": [
        ("01-入门与环境搭建", "入门与环境搭建", [1, 2, 3, 4, 5]),
        ("02-基础语法", "基础语法", [7, 8, 9, 10, 11, 12]),
        ("03-函数与-Lambda", "函数与 Lambda", [13, 14, 15, 16]),
        ("04-面向对象", "面向对象", [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]),
        ("05-进阶特性", "进阶特性（空安全/集合/异常/注解/反射）", [30, 31, 32, 33, 34, 35, 36]),
        ("06-协程与互操作", "协程与 Java 互操作、多平台", [37, 38, 39]),
        ("07-工程与规范", "Gradle 构建、测试、编码规范、版本特性", [40, 41, 42, 43]),
    ],
    "android": [
        ("01-开发环境与工程基础", "开发环境与工程基础", list(range(1, 16))),
        ("02-布局与-View-体系", "布局与 View 体系", list(range(16, 23))),
        ("03-常用-UI-控件", "常用 UI 控件", list(range(23, 35))),
        ("04-列表与适配器", "列表、适配器与容器", list(range(35, 48))),
        ("05-弹窗通知与导航", "弹窗、通知与导航", list(range(48, 56))),
        ("06-事件处理与异步", "事件处理与异步", list(range(56, 64))),
        ("07-Activity-与-Intent", "Activity 与 Intent", [64, 65, 66, 74, 75]),
        ("08-Service", "Service", [67, 68, 69]),
        ("09-BroadcastReceiver", "BroadcastReceiver", [70, 71]),
        ("10-ContentProvider", "ContentProvider", [72, 73]),
        ("11-Fragment", "Fragment", list(range(76, 82))),
        ("12-数据存储", "数据存储（文件/SharedPreferences/SQLite）", list(range(82, 86))),
        ("13-网络编程", "网络编程（HTTP/解析/上传下载/WebView/Socket）", list(range(86, 106))),
        ("14-图形与绘图", "图形与绘图（Drawable/Bitmap/Paint/Canvas）", list(range(106, 129))),
        ("15-动画", "动画", list(range(129, 133))),
        ("16-多媒体", "多媒体（音频/视频/相机/录音）", list(range(133, 137))),
        ("17-系统服务与传感器", "系统服务与传感器", list(range(137, 151))),
        ("18-实战项目", "实战项目", list(range(151, 158))),
    ],
}


def parse_crawled(path):
    """从爬取的单页 md 中解析标题、来源、代码块列表。"""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    title = None
    source = None
    m = re.search(r"^#\s+(.+)$", text, re.M)
    if m:
        title = m.group(1).strip()
    m = re.search(r"^>\s*来源:\s*(\S+)\s*$", text, re.M)
    if m:
        source = m.group(1).strip()
    blocks = []
    for bm in re.finditer(r"```(\w+)\n(.*?)```", text, re.S):
        blocks.append((bm.group(1), bm.group(2).rstrip("\n")))
    return title, source, blocks


def build():
    summary = {}
    for tutorial in ("kotlin", "android"):
        idx_path = os.path.join(CRAWL, tutorial, "index.json")
        with open(idx_path, encoding="utf-8") as f:
            index = json.load(f)
        by_order = {p["order"]: p for p in index}
        total_expected = sum(p["codes"] for p in index)

        out_dir = os.path.join(OUT, tutorial)
        os.makedirs(out_dir, exist_ok=True)
        toc_rows = []
        counted = 0
        chapter_files = []

        for fname, chap_title, orders in CHAPTERS[tutorial]:
            lines = [f"# {chap_title}", ""]
            pages = [by_order[o] for o in orders if o in by_order]
            nblocks = 0
            body = []
            for p in pages:
                src_path = os.path.join(CRAWL, tutorial, p["file"])
                title, source, blocks = parse_crawled(src_path)
                title = title or p["title"]
                source = source or p["url"]
                if not blocks:
                    nc_path = os.path.join(NOCODE, tutorial, p["file"])
                    if os.path.exists(nc_path):
                        with open(nc_path, encoding="utf-8") as f:
                            nc = f.read().strip()
                        body.append(f"## {title}\n\n> 来源: {source}\n\n{nc}\n")
                    else:
                        body.append(f"## {title}\n\n> 来源: {source}\n\n_（本页无代码块）_\n")
                    continue
                body.append(f"## {title}\n\n> 来源: {source}\n")
                for i, (lang, code) in enumerate(blocks, 1):
                    body.append(f"```{lang}\n{code}\n```\n")
                nblocks += len(blocks)
            counted += nblocks
            lines.append(f"> 本章归并自 {len(pages)} 页教程代码块，来源见各节。\n")
            lines.extend(body)
            with open(os.path.join(out_dir, fname + ".md"), "w", encoding="utf-8") as f:
                f.write("\n".join(lines).rstrip() + "\n")
            chapter_files.append((fname + ".md", chap_title, nblocks))
            toc_rows.append((fname + ".md", chap_title, len(pages), nblocks))

        if counted != total_expected:
            raise SystemExit(
                f"[{tutorial}] 代码块数不符: 归并 {counted} != 索引 {total_expected}"
            )
        summary[tutorial] = (chapter_files, counted, total_expected)
        print(f"== {tutorial}: {len(chapter_files)} 章, {counted} 代码块 (校验通过)")
        build.__dict__[tutorial] = toc_rows

    # 总目录
    lines = ["# Android 开发手册 · 章节草稿", ""]
    lines.append("> 由 runoob.com 爬取的教程代码块按主题归并生成。代码版权归原作者所有，仅作参考。\n")
    for tutorial, label in (("kotlin", "语言篇 · Kotlin"), ("android", "框架篇 · Android")):
        rows = build.__dict__[tutorial]
        lines.append(f"## {label}\n")
        lines.append("| 章节 | 覆盖页数 | 代码块 |")
        lines.append("|---|---|---|")
        for fname, chap_title, npages, nblocks in rows:
            lines.append(f"| [{chap_title}]({tutorial}/{fname}) | {npages} | {nblocks} |")
        lines.append("")
    with open(os.path.join(OUT, "目录.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    print("== 目录.md 已生成")


if __name__ == "__main__":
    build()
