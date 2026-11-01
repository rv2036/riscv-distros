#!/usr/bin/env python3
"""数据卫生：跨语言枚举归一 + 死链清理。

两个动作：

1. `--normalize`：把误写进枚举字段的中文值归一到程序值（例如厂商那路调研把 audience
   写成「新人推荐」「厂商测试」「仅评估」），五语文件一起扫。枚举字段渲染前会走
   `i18n (printf "audience.%s" …)`，值不对就会在页面上直接印出键名。

2. `--dead-links <文件>`：文件里每行一个坏 URL，把所有语言里 downloads / guides /
   evidence 命中的条目删掉，并打印删了什么。删完要重跑对应语言的构建。

用法：
    python scripts/data_hygiene.py --normalize
    python scripts/data_hygiene.py --dead-links /tmp/rdstr/urlcheck_bad.txt
    python scripts/data_hygiene.py --normalize --dead-links bad.txt --dry-run
"""
import argparse
import glob
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'website', 'data', 'i18n')
LANGS = ('zh', 'en', 'ja', 'ru', 'ko')

# 枚举字段 → 允许的程序值
ENUMS = {
    'audience': {'recommended', 'advanced', 'vendor'},
    'upstream': {'official', 'community', 'downstream'},
    'status': {'on_sale', 'eol', 'hard', 'announced', 'unknown'},
    'level': {'official', 'community', 'partial', 'none'},
    'kind': {'distro', 'buildsystem', 'simulator'},
    'importance': {'high', 'medium', 'low'},
}

ALIAS = {
    '新人推荐': 'recommended', '可直接用': 'recommended', '推荐': 'recommended',
    '需要动手': 'advanced', '需要动手能力': 'advanced', '进阶': 'advanced', '仅评估': 'advanced',
    '厂商测试': 'vendor', '厂商测试用': 'vendor',
    '官方支持': 'official', '上游官方架构': 'official', '社区移植': 'community',
    '厂商下游发行版': 'downstream', '下游': 'downstream',
    '在售': 'on_sale', '停产': 'eol', '难买': 'hard', '预告': 'announced',
    '部分可用': 'partial', '社区可用': 'community', '未支持': 'none',
    '成品发行版': 'distro', '构建系统': 'buildsystem', '模拟器': 'simulator',
}


def fix_enum(value, field):
    if not isinstance(value, str):
        return value
    v = value.strip()
    if v in ENUMS.get(field, set()):
        return v
    if v in ALIAS:
        return ALIAS[v]
    low = v.lower()
    if low in ENUMS.get(field, set()):
        return low
    return value


def walk_items(obj, field, hits):
    """在 items 数组的每个元素（及其嵌套 list 里的 dict）上归一 field。"""
    if isinstance(obj, list):
        for x in obj:
            walk_items(x, field, hits)
    elif isinstance(obj, dict):
        if field in obj:
            old = obj[field]
            new = fix_enum(old, field)
            if new != old:
                hits.append((field, old, new))
                obj[field] = new
        for k, v in obj.items():
            if isinstance(v, (list, dict)):
                walk_items(v, field, hits)


def normalize(dry):
    total = 0
    for lang in LANGS:
        for path in sorted(glob.glob(os.path.join(DATA, lang, '*.yaml'))):
            raw = open(path, encoding='utf-8').read()
            head = ''
            for line in raw.split('\n'):
                if line.startswith('#'):
                    head += line + '\n'
                else:
                    break
            data = yaml.safe_load(raw)
            if not isinstance(data, dict) or 'items' not in data:
                continue
            hits = []
            for field in ENUMS:
                walk_items(data['items'], field, hits)
            if not hits:
                continue
            print(f'  {os.path.relpath(path, ROOT)}: {len(hits)} 处归一')
            seen = set()
            for field, old, new in hits:
                key = (field, old, new)
                if key in seen:
                    continue
                seen.add(key)
                print(f'    {field}: 「{old}」→ {new}')
            total += len(hits)
            if not dry:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(head)
                    f.write(yaml.dump(data, allow_unicode=True, sort_keys=False, width=200))
    print(f'  合计归一 {total} 处' + ('（dry-run，未写盘）' if dry else ''))
    return total


def dead_links(listfile, dry):
    bad = {l.strip() for l in open(listfile, encoding='utf-8') if l.strip() and not l.startswith('#')}
    urls = {re.sub(r'^\S+\s+', '', b) for b in bad}
    print(f'  待清理 URL {len(urls)} 个')
    removed = 0
    for lang in LANGS:
        for path in sorted(glob.glob(os.path.join(DATA, lang, '*.yaml'))):
            raw = open(path, encoding='utf-8').read()
            head = ''
            for line in raw.split('\n'):
                if line.startswith('#'):
                    head += line + '\n'
                else:
                    break
            data = yaml.safe_load(raw)
            if not isinstance(data, dict) or 'items' not in data:
                continue
            changed = []

            def prune(node):
                nonlocal removed
                if isinstance(node, list):
                    keep = []
                    for x in node:
                        if isinstance(x, dict) and x.get('url') in urls:
                            changed.append(x.get('url'))
                            removed += 1
                            continue
                        if isinstance(x, str) and x in urls:
                            changed.append(x)
                            removed += 1
                            continue
                        prune(x)
                        keep.append(x)
                    node[:] = keep
                elif isinstance(node, dict):
                    for k, v in list(node.items()):
                        if isinstance(v, (list, dict)):
                            prune(v)
                        elif isinstance(v, str) and v in urls and k in ('url',):
                            del node[k]

            prune(data['items'])
            if changed:
                print(f'  {os.path.relpath(path, ROOT)}: 删除 {len(changed)} 条')
                for c in sorted(set(changed)):
                    print(f'    - {c}')
                if not dry:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(head)
                        f.write(yaml.dump(data, allow_unicode=True, sort_keys=False, width=200))
    print(f'  合计删除 {removed} 条' + ('（dry-run，未写盘）' if dry else ''))
    return removed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--normalize', action='store_true')
    ap.add_argument('--dead-links')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    if not a.normalize and not a.dead_links:
        ap.print_help()
        return 1
    if a.normalize:
        print('== 枚举归一 ==')
        normalize(a.dry_run)
    if a.dead_links:
        print('== 死链清理 ==')
        dead_links(a.dead_links, a.dry_run)
    return 0


if __name__ == '__main__':
    sys.exit(main())
