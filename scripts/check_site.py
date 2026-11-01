#!/usr/bin/env python3
"""构建产物自检：页面矩阵、明细页与 feed、hreflang、站内链接。

用法（先构建，再跑）：
    make site-check

退出码 1 = 有闸门没过。
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, "website", "public")

LANGS = ["zh", "en", "ja", "ru", "ko"]
# 每种语言都应存在的页面（相对站点根；zh 在根，其余在 /<lang>/）
PAGES = ["", "start/", "distros/", "boards/", "matrix/", "ai/", "sources/"]
# 明细栏目：其下每个子目录都必须有 index.html + index.xml（分条目的 feed）
DETAIL_DIRS = ["distros", "boards"]
# 每个语言都必须有这些 feed
LANG_FEEDS = ["index.xml", "distros/index.xml", "boards/index.xml", "ai/index.xml"]


def base_of(lang):
    return "" if lang == "zh" else f"{lang}/"


def page_url(lang, page):
    return "/" + (page if lang == "zh" else f"{lang}/{page}")


def find_file(url):
    """把站内 URL 映射到构建产物里的文件。"""
    p = url.split("#")[0].split("?")[0]
    if not p.startswith("/"):
        return None
    rel = p.lstrip("/")
    cand = [
        os.path.join(PUB, rel),
        os.path.join(PUB, rel, "index.html"),
        os.path.join(PUB, rel + ".html"),
        os.path.join(PUB, rel.rstrip("/") + "/index.html"),
    ]
    for c in cand:
        if os.path.isfile(c):
            return c
    return None


def attr(tag, name):
    m = re.search(name + r'=(?:"([^"]*)"|([^\s>]+))', tag)
    if not m:
        return None
    return m.group(1) if m.group(1) is not None else m.group(2)


def main():
    if not os.path.isdir(PUB):
        print("找不到构建产物目录 website/public，请先 make site")
        return 1

    errors = []

    # 1) 页面齐全度矩阵
    missing = 0
    for lang in LANGS:
        for page in PAGES:
            url = page_url(lang, page)
            if not find_file(url):
                errors.append(f"缺少页面 {url}")
                missing += 1
    print(f"页面矩阵: {len(LANGS)} 语言 × {len(PAGES)} 页，缺失 {missing} 处")

    # 2) 明细页：distros/<id>/ 与 boards/<id>/ 必须有页面与自己的 feed
    detail_pages = 0
    detail_missing = 0
    zh_ids = {}
    for lang in LANGS:
        for d in DETAIL_DIRS:
            root = os.path.join(PUB, base_of(lang), d)
            if not os.path.isdir(root):
                errors.append(f"缺少栏目目录 /{base_of(lang)}{d}/")
                detail_missing += 1
                continue
            ids = sorted(x for x in os.listdir(root) if os.path.isdir(os.path.join(root, x)))
            zh_ids[d] = ids if lang == "zh" else zh_ids.get(d, ids)
            for i in ids:
                detail_pages += 1
                if not os.path.isfile(os.path.join(root, i, "index.html")):
                    errors.append(f"明细页缺 HTML: /{base_of(lang)}{d}/{i}/")
                    detail_missing += 1
                if not os.path.isfile(os.path.join(root, i, "index.xml")):
                    errors.append(f"明细页缺 feed: /{base_of(lang)}{d}/{i}/index.xml")
                    detail_missing += 1
    # 五语言的明细页集合必须一致
    for lang in LANGS[1:]:
        for d in DETAIL_DIRS:
            root = os.path.join(PUB, base_of(lang), d)
            if not os.path.isdir(root):
                continue
            ids = sorted(x for x in os.listdir(root) if os.path.isdir(os.path.join(root, x)))
            if ids != zh_ids.get(d):
                missing_ids = set(zh_ids.get(d, [])) - set(ids)
                extra = set(ids) - set(zh_ids.get(d, []))
                errors.append(f"{lang}/{d} 明细页集合与中文不一致 缺={sorted(missing_ids)} 多={sorted(extra)}")
    print(f"明细页: 检查 {detail_pages} 个（distros + boards × {len(LANGS)} 语），问题 {detail_missing} 处")

    # 3) hreflang / x-default
    html_files = []
    for dirpath, _dirnames, filenames in os.walk(PUB):
        for fn in filenames:
            if fn.endswith(".html"):
                html_files.append(os.path.join(dirpath, fn))

    no_xdefault = 0
    checked = 0
    for path in html_files:
        with open(path, encoding="utf-8", errors="ignore") as fh:
            html = fh.read()
        if re.search(r'http-equiv=["\']?refresh', html, re.I):
            continue
        checked += 1
        if not re.search(r'hreflang=["\']?x-default', html, re.I):
            errors.append(f"缺 x-default: {os.path.relpath(path, PUB)}")
            no_xdefault += 1
    print(f"hreflang: 检查 {checked} 页，缺 x-default {no_xdefault} 页")

    # 4) 站内链接与静态资源
    link_total = 0
    link_bad = 0
    for path in html_files:
        with open(path, encoding="utf-8", errors="ignore") as fh:
            html = fh.read()
        html = re.sub(r"<!--.*?-->", "", html, flags=re.S)
        html = re.sub(r"<script.*?</script>", "", html, flags=re.S | re.I)
        for tag in re.findall(r"<a\b[^>]*>|<img\b[^>]*>|<link\b[^>]*>|<source\b[^>]*>", html, re.I):
            target = attr(tag, "href") or attr(tag, "src")
            if not target:
                continue
            if target.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
                continue
            link_total += 1
            if not find_file(target):
                base = os.path.relpath(path, PUB).replace("index.html", "")
                resolved = "/" + os.path.normpath(os.path.join(base, target.lstrip("/"))).lstrip("./")
                if not find_file(resolved):
                    errors.append(f"坏链 {target} 于 {os.path.relpath(path, PUB)}")
                    link_bad += 1
    print(f"站内链接: 检查 {link_total} 个，坏链 {link_bad} 个")

    # 5) feed：存在、条目字段合法、guid 唯一
    feed_counts = {}
    for lang in LANGS:
        for feed in LANG_FEEDS:
            path = os.path.join(PUB, base_of(lang), feed)
            if not os.path.isfile(path):
                errors.append(f"缺 RSS: /{base_of(lang)}{feed}")
                continue
            with open(path, encoding="utf-8", errors="ignore") as fh:
                xml = fh.read()
            items = re.findall(r"<item>(.*?)</item>", xml, re.S)
            feed_counts[(lang, feed)] = len(items)
            guids = re.findall(r"<guid[^>]*>(.*?)</guid>", xml, re.S)
            if len(set(guids)) != len(guids):
                errors.append(f"/{base_of(lang)}{feed} guid 有重复")
            for it in items:
                lack = [t for t in ("title", "link", "guid", "pubDate", "description") if f"<{t}" not in it]
                if lack:
                    errors.append(f"/{base_of(lang)}{feed} 条目缺 {lack}")
                    break
                if 'isPermaLink="false"' not in it:
                    errors.append(f"/{base_of(lang)}{feed} guid 缺 isPermaLink=false")
                    break
                m = re.search(r"<pubDate>(.*?)</pubDate>", it)
                if m and not re.match(r"^[A-Z][a-z]{2}, \d{2} [A-Z][a-z]{2} \d{4} \d{2}:\d{2}:\d{2} [+-]\d{4}$",
                                      m.group(1).strip()):
                    errors.append(f"/{base_of(lang)}{feed} pubDate 格式异常: {m.group(1)[:40]}")
                    break
    empty = [(l, f) for (l, f), n in feed_counts.items() if n == 0]
    for l, f in empty:
        errors.append(f"feed 为空: /{base_of(l)}{f}")
    print("RSS: " + ", ".join(f"{f}={feed_counts.get(('zh', f), 0)}" for f in LANG_FEEDS) + "（zh 条目数）")

    # 6) 首页/明细页 head 里必须有 feed 发现链接
    no_feed_link = 0
    for lang in LANGS:
        for page in ("", "distros/", "boards/"):
            path = os.path.join(PUB, base_of(lang), page, "index.html")
            if not os.path.isfile(path):
                continue
            with open(path, encoding="utf-8", errors="ignore") as fh:
                html = fh.read()
            if "application/rss+xml" not in html:
                errors.append(f"页面缺 feed 发现链接: /{base_of(lang)}{page}")
                no_feed_link += 1
    print(f"RSS 发现链接: 检查 {len(LANGS) * 3} 页，缺 {no_feed_link} 页")

    # 7) 订阅条必须在每个页面 hero 下方出现
    no_strip = 0
    for path in html_files:
        with open(path, encoding="utf-8", errors="ignore") as fh:
            html = fh.read()
        if re.search(r'http-equiv=["\']?refresh', html, re.I):
            continue
        if not re.search(r'<aside class="?subscribe"?', html):
            errors.append(f"缺订阅条: {os.path.relpath(path, PUB)}")
            no_strip += 1
    print(f"订阅条: 检查 {checked} 页，缺 {no_strip} 页")

    if errors:
        print("\n未通过：")
        for e in errors[:40]:
            print("  ·", e)
        if len(errors) > 40:
            print(f"  … 还有 {len(errors) - 40} 条")
        return 1
    print("\n全部通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
