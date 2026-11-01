#!/usr/bin/env python3
"""把 6 路调研的 JSON 合并成站点的中文数据文件（distros / boards / ai）。

跑法：~/.hermes/hermes-agent/venv/bin/python scripts/merge_research.py
输出：website/data/i18n/zh/{distros,boards,ai}.yaml
"""
import datetime
import json
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = '/tmp/rdstr'
TODAY = datetime.date.today().isoformat()

# 调研用的板卡 id → 本站规范 id
BOARD_ID = {
    'qemu-virt': 'qemu', 'hifive-unmatched': 'unmatched', 'milkv-pioneer': 'pioneer',
    'milkv-meles': 'meles', 'milkv-duo': 'milkv-duo', 'rv2': 'orangepi-rv2',
    'bpi_f3': 'bpi-f3', 'vf2lite': 'visionfive2-lite',
    'visionfive2': 'visionfive2', 'licheepi-4a': 'licheepi-4a',
    'beaglev-ahead': 'beaglev-ahead', 'k3': 'k3', 'a210': 'a210', 'k230': 'k230',
    'megrez': 'megrez', 'titan': 'titan', 'p550': 'p550',
}

BOARD_STATUS = {'在售': 'on_sale', '停产': 'eol', '难买': 'hard',
                '预告': 'announced', '已发布': 'announced', '不详': 'unknown'}

# 板卡展示顺序（越靠前越适合当「第一块板」）
BOARD_ORDER = ['qemu', 'visionfive2', 'licheepi-4a', 'meles', 'k3', 'a210', 'k230',
               'megrez', 'titan', 'unmatched', 'bpi-f3', 'orangepi-rv2', 'p550',
               'visionfive2-lite', 'beaglev-ahead', 'pioneer', 'milkv-duo']
BOARD_FEATURE = {'qemu', 'visionfive2', 'licheepi-4a', 'k3', 'a210'}

DISTRO_ORDER = ['debian', 'ubuntu', 'fedora', 'fvf', 'revyos', 'bianbu', 'armbian',
                'alpine', 'arch', 'opensuse', 'gentoo', 'nixos', 'freebsd', 'netbsd',
                'openbsd', 'alt', 'buildroot', 'yocto', 'openeuler', 'openkylin',
                'deepin', 'openruyi', 'void', 'pld', 'slackware', 'android']
DISTRO_FEATURE = {'debian', 'ubuntu', 'fedora', 'fvf', 'revyos', 'bianbu'}
DOWNSTREAM = {'revyos', 'bianbu', 'deepin', 'fvf', 'bredos', 'irradium', 'rockos', 'tinalinux'}
AUDIENCE = {
    'recommended': {'debian', 'ubuntu', 'fedora', 'fvf', 'revyos', 'bianbu', 'armbian', 'alpine', 'opensuse'},
    'vendor': {'openruyi'},
    'advanced': {'openkylin', 'deepin', 'openeuler'},
}


def load(name):
    with open(os.path.join(SRC, name), encoding='utf-8') as f:
        return json.load(f)


def normalize_upstream(d, ):
    if d['id'] in DOWNSTREAM:
        return 'downstream'
    if d.get('upstream') is True:
        return 'official'
    return 'community'


AUDIENCE_ALIAS = {'新人推荐': 'recommended', '厂商测试': 'vendor', '仅评估': 'advanced',
                  '可直接用': 'recommended', '需要动手': 'advanced'}


def norm_audience(v, did):
    if not v:
        return audience_of(did)
    return AUDIENCE_ALIAS.get(v.strip(), v.strip())


def audience_of(did):
    for k, v in AUDIENCE.items():
        if did in v:
            return k
    return 'advanced'


def board_status(s):
    s = (s or '').strip()
    for k, v in BOARD_STATUS.items():
        if k in s:
            return v
    return 'unknown'


def clean_boards(entries, id_field='distro'):
    out = []
    for b in entries or []:
        bid = b.get('board') or b.get(id_field)
        if not bid:
            continue
        out.append({
            'board': BOARD_ID.get(bid, bid),
            'level': b.get('level', 'community'),
            'note': b.get('note', ''),
        })
    return out


def clean_distro_entries(entries):
    out = []
    for x in entries or []:
        did = x.get('distro')
        if not did:
            continue
        out.append({'distro': did, 'level': x.get('level', 'community'), 'note': x.get('note', '')})
    return out


def main():
    a = load('upstream_a.json')['distros']
    b = load('upstream_b.json')['distros']
    v = load('vendor.json')['distros']
    ba = load('boards_a.json')['boards']
    bb = load('boards_b.json')['boards']
    ai = load('ai_matrix.json')

    # ---------- 发行版 ----------
    distros = []
    for d in a + b + v:
        did = d['id']
        distros.append({
            'id': did,
            'name': d['name'],
            'vendor': '',
            'upstream': normalize_upstream(d),
            'upstream_note': d.get('upstream_note', ''),
            'kind': d.get('kind', 'distro'),
            'based_on': d.get('based_on') or d.get('base', ''),
            'audience': norm_audience(d.get('audience'), did),
            'versions': d.get('versions', []),
            'boards': clean_boards(d.get('boards')),
            'downloads': [{'label': x['label'], 'url': x['url']} for x in d.get('downloads', []) if x.get('url')],
            'guides': [{'label': x['label'], 'url': x['url'], 'type': x.get('type', 'doc'), 'lang': x.get('lang', 'en')}
                       for x in d.get('guides', []) if x.get('url')],
            'gotchas': [g for g in d.get('gotchas', []) if g],
            'doc_langs': d.get('doc_langs', []),
            'derivatives': [x for x in d.get('derivatives', []) if x],
            'note': d.get('note', ''),
            'checked': TODAY,
        })

    # ---------- 开发板 ----------
    boards = []
    for bd in ba + bb:
        bid = BOARD_ID.get(bd['id'], bd['id'])
        boards.append({
            'id': bid,
            'name': bd['name'],
            'soc': bd.get('soc', ''),
            'vendor': bd.get('vendor', ''),
            'spec': bd.get('spec', ''),
            'status': board_status(bd.get('status')),
            'price_note': bd.get('price_note', ''),
            'forms': bd.get('forms', []),
            'official_os': bd.get('official_os', []),
            'distros': clean_distro_entries(bd.get('distros')),
            'downloads': [{'label': x['label'], 'url': x['url']} for x in bd.get('downloads', []) if x.get('url')],
            'guides': [{'label': x['label'], 'url': x['url'], 'type': x.get('type', 'doc'), 'lang': x.get('lang', 'en')}
                       for x in bd.get('guides', []) if x.get('url')],
            'gotchas': [g for g in bd.get('gotchas', []) if g],
            'doc_langs': bd.get('doc_langs', []),
            'note': bd.get('note', ''),
            'checked': TODAY,
        })

    # ---------- 排序与高亮 ----------
    def order_of(item, table):
        return table.index(item['id']) + 1 if item['id'] in table else 900

    distros.sort(key=lambda x: (order_of(x, DISTRO_ORDER), x['id']))
    boards.sort(key=lambda x: (order_of(x, BOARD_ORDER), x['id']))
    for i, d in enumerate(distros, 1):
        d['order'] = i
        d['feature'] = d['id'] in DISTRO_FEATURE
    for i, bd in enumerate(boards, 1):
        bd['order'] = i
        bd['feature'] = bd['id'] in BOARD_FEATURE

    # ---------- AI ----------
    name_of = {b['id']: b['name'] for b in boards}
    ai_items = []
    for i, x in enumerate(ai.get('ai', []), 1):
        bid = BOARD_ID.get(x['board'], x['board'])
        ai_items.append({
            'board': bid,
            'board_name': name_of.get(bid, x['board']),
            'soc': x.get('soc', ''),
            'runs': [{'item': r.get('item', ''), 'state': r.get('state', 'unknown'),
                      'evidence': [u for u in r.get('evidence', []) if u], 'note': r.get('note', '')}
                     for r in x.get('runs', [])],
            'npu': x.get('npu', ''),
            'note': x.get('note', ''),
            'checked': TODAY,
            'order': i,
        })
    ruyi = ai.get('ruyisdk', {})
    ai_data = {
        'ruyisdk': {
            'url': 'https://matrix.ruyisdk.org/',
            'fetched_at': ruyi.get('fetched_at', TODAY),
            'note': ruyi.get('note', ''),
        },
        'items': ai_items,
    }

    # ---------- 写文件 ----------
    outdir = os.path.join(ROOT, 'website', 'data', 'i18n', 'zh')
    os.makedirs(outdir, exist_ok=True)
    heads = {
        'distros': '# 发行版条目（中文母版）\n',
        'boards': '# 开发板条目（中文母版）\n',
        'ai': '# AI 软件支持（中文母版）\n',
    }
    for name, data in (('distros', {'items': distros}),
                       ('boards', {'items': boards}),
                       ('ai', ai_data)):
        path = os.path.join(outdir, f'{name}.yaml')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(heads[name])
            f.write(yaml.dump(data, allow_unicode=True, sort_keys=False, width=200))
        print(f'  {name}.yaml: {os.path.getsize(path)//1024} KB')

    print(f'  发行版 {len(distros)} 个 | 开发板 {len(boards)} 块 | AI 行 {len(ai_items)} 条')
    print('  发行版:', [d['id'] for d in distros])
    print('  开发板:', [b['id'] for b in boards])
    return 0


if __name__ == '__main__':
    sys.exit(main())
