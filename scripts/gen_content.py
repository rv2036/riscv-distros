#!/usr/bin/env python3
"""从 data/i18n/<lang>/*.yaml 生成明细页骨架。

每个发行版 → content/<lang>/distros/<id>.md（layout: distro，带自己的 RSS）
每块开发板 → content/<lang>/boards/<id>.md（layout: board，带自己的 RSS）

数据改完重新跑一次即可；脚本只写 front matter，正文留空（内容全在 data 里）。
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE = os.path.join(ROOT, "website")
LANGS = ["zh", "en", "ja", "ru", "ko"]

# 不引入 yaml 依赖：只为拿 id / name，逐行解析足够
def read_items(path):
    """返回 [(id, name)]，从 yaml 的 items 列表里取（容忍缩进差异）。"""
    out = []
    cur = {}
    if not os.path.isfile(path):
        return out
    in_items = False
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        if re.match(r"^items:\s*$", line):
            in_items = True
            continue
        if not in_items:
            continue
        m = re.match(r"^\s*-\s+id:\s*(.+?)\s*$", line)
        if m:
            if cur.get("id"):
                out.append((cur["id"], cur.get("name", cur["id"])))
            cur = {"id": m.group(1).strip().strip('"').strip("'")}
            continue
        m = re.match(r"^\s+name:\s*(.+?)\s*$", line)
        if m and not cur.get("name"):
            cur["name"] = m.group(1).strip().strip('"').strip("'")
    if cur.get("id"):
        out.append((cur["id"], cur.get("name", cur["id"])))
    return out


def write_page(path, title, extra):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    body = (
        "---\n"
        f"title: {title}\n"
        f"{extra}"
        'outputs: ["html", "rss"]\n'
        "---\n"
    )
    existing = ""
    if os.path.isfile(path):
        existing = open(path, encoding="utf-8").read()
    if existing == body:
        return False
    open(path, "w", encoding="utf-8").write(body)
    return True


def main():
    total = 0
    for lang in LANGS:
        ddir = os.path.join(WEBSITE, "data", "i18n", lang)
        for kind, key in (("distros", "distro"), ("boards", "board")):
            items = read_items(os.path.join(ddir, f"{kind}.yaml"))
            for iid, name in items:
                path = os.path.join(WEBSITE, "content", lang, kind, f"{iid}.md")
                layout = "distro" if key == "distro" else "board"
                extra = f'layout: {layout}\n{key}: "{iid}"\n'
                if write_page(path, '"%s"' % name.replace('"', '\\"'), extra):
                    total += 1
    print(f"明细页骨架：写入/更新 {total} 个文件")
    return 0


if __name__ == "__main__":
    sys.exit(main())
