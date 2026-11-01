#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""由 zh 数据生成 en 数据：只替换文本值，结构与受保护字段原样保留。

用法：
    python scripts/build_en.py distros [--dry]
"""
import importlib
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = os.path.join(ROOT, "website", "data", "i18n", "zh")
EN = os.path.join(ROOT, "website", "data", "i18n", "en")
sys.path.insert(0, os.path.join(ROOT, "scripts"))

CJK = re.compile(r"[\u3000-\u303f\u3400-\u4dbf\u4e00-\u9fff\uff00-\uffef]")

MODULES = {
    "distros": ["i18n_en.a_distros_core", "i18n_en.b_distros_boards", "i18n_en.c_distros_labels"],
    "boards": ["i18n_en.d_boards", "i18n_en.d2_boards"],
    "ai": ["i18n_en.e_ai"],
}


def load_map(name, verbose=False):
    m = {}
    conflicts = []
    for mod_name in MODULES[name]:
        mod = importlib.import_module(mod_name)
        for k, v in mod.M.items():
            if k in m and m[k] != v:
                conflicts.append((k, m[k], v))
            m[k] = v
    if conflicts:
        print("!! 同一中文串出现不同译文：")
        for k, a, b in conflicts:
            print("   ", k[:60], "|", a[:40], "|", b[:40])
    return m


def walk(node, m, missed, path=""):
    if isinstance(node, dict):
        return {k: walk(v, m, missed, path + "/" + k) for k, v in node.items()}
    if isinstance(node, list):
        return [walk(v, m, missed, path + "[]") for v in node]
    if isinstance(node, str):
        if node in m:
            return m[node]
        if CJK.search(node):
            missed.append((path, node))
        return node
    return node


def main():
    name = sys.argv[1]
    dry = "--dry" in sys.argv
    m = load_map(name)
    src = os.path.join(ZH, f"{name}.yaml")
    with open(src, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    missed = []
    out = walk(data, m, missed)
    print(f"[{name}] 已映射 {len(m)} 条；未译中文串 {len(missed)} 条")
    for path, s in missed:
        print(f"  MISS {path}: {s}")
    # 未被用到的映射键
    used = set()

    def collect(node):
        if isinstance(node, dict):
            for v in node.values():
                collect(v)
        elif isinstance(node, list):
            for v in node:
                collect(v)
        elif isinstance(node, str):
            used.add(node)

    collect(data)
    unused = [k for k in m if k not in used]
    if unused:
        print(f"  未使用的映射键 {len(unused)} 条（说明键名对不上）：")
        for k in unused[:20]:
            print("    UNUSED", k[:80])
    if dry or missed:
        return 1 if missed else 0
    os.makedirs(EN, exist_ok=True)
    dst = os.path.join(EN, f"{name}.yaml")
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write("# Generated from website/data/i18n/zh/%s.yaml; keep structure identical.\n" % name)
        yaml.dump(out, fh, allow_unicode=True, sort_keys=False, width=100000, default_flow_style=False)
    print(f"  写入 {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
