#!/usr/bin/env python3
"""把 RuyiSDK 支持矩阵（ruyisdk/support-matrix 仓库）转成站点的数据文件。

输入：support-matrix 仓库的本地克隆路径（默认 /tmp/support-matrix）
输出：website/data/ruyisdk.yaml（语言中立：只有 id / 枚举 / URL / 日期）
      + /tmp/rdstr/ruyisdk_matrix.json（原始抽取结果，供排查）

用法：
    git clone --depth 1 https://github.com/ruyisdk/support-matrix.git /tmp/support-matrix
    ~/.hermes/hermes-agent/venv/bin/python scripts/gen_ruyisdk_data.py [仓库路径]
"""
import datetime
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_YAML = os.path.join(ROOT, 'website', 'data', 'ruyisdk.yaml')
SITE = 'https://matrix.ruyisdk.org'

# RuyiSDK 板卡目录名 → 本站 board id（未列出的板不进矩阵，但报告仍可在 RuyiSDK 站点查）
BOARD_MAP = {
    'A210_SODIMM_V2': 'a210',
    'K3-Pico-ITX': 'k3',
    'CoM260_Kit': 'k3-som260',
    'Meles': 'meles',
    'LicheePi4A': 'licheepi-4a',
    'VisionFive2': 'visionfive2',
    'VisionFive2_Lite': 'visionfive2-lite',
    'VisionFive': 'visionfive',
    'Unmatched': 'unmatched',
    'Megrez': 'megrez',
    'Titan': 'titan',
    'DP1000-EVB': 'dp1000-evb',
    'K230': 'k230',
    'BPI-F3': 'bpi-f3',
    'OrangePi-RV2': 'orangepi-rv2',
    'Pioneer': 'pioneer',
    'Jupiter': 'jupiter',
    'Jupiter2': 'jupiter2',
    'Mars': 'mars',
    'STAR64': 'star64',
    'Duo': 'milkv-duo',
    'Duo256m': 'milkv-duo',
    'Duo_S': 'milkv-duo',
    'Muse_Pi_Pro': 'muse-pi-pro',
    'Bit-Brick_K1': 'bit-brick-k1',
    'LicheeCluster4A': 'lichee-cluster-4a',
    'LicheeConsole4A': 'lichee-console-4a',
    'Premier_P550': 'p550',
}

# RuyiSDK 系统目录名 → 本站 distro id
SYS_MAP = {
    'Ubuntu': 'ubuntu', 'Debian': 'debian', 'Fedora': 'fedora', 'openSUSE': 'opensuse',
    'ArchLinux': 'arch', 'Alpine': 'alpine', 'Gentoo': 'gentoo', 'NixOS': 'nixos',
    'Slackware': 'slackware', 'Guix': 'guix', 'Armbian': 'armbian', 'DietPi': 'dietpi',
    'Bianbu': 'bianbu', 'RevyOS': 'revyos', 'BredOS': 'bredos', 'irradium': 'irradium',
    'eweOS': 'eweos', 'RockOS': 'rockos', 'Tizen': 'tizen', 'postmarketOS': 'postmarketos',
    'TinaLinux': 'tinalinux', 'BuildRoot': 'buildroot', 'Yocto': 'yocto', 'OpenWrt': 'openwrt',
    'openEuler': 'openeuler', 'openKylin': 'openkylin', 'Deepin': 'deepin',
    'OpenCloudOS': 'opencloudos', 'openCloudOS': 'opencloudos', 'OpenHarmony': 'openharmony',
    'FreeBSD': 'freebsd', 'OpenBSD': 'openbsd', 'NetBSD': 'netbsd', 'xv6': 'xv6',
}

# 只为 MCU / RTOS 服务的系统：本站（Linux 发行版门户）不计入矩阵
RTOS = {'RT-Thread', 'FreeRTOS', 'Zephyr', 'NuttX', 'LiteOS', 'ThreadX', 'uCOSII',
        'Melis', 'UniProton'}

FM = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.S)
KEY = re.compile(r'^(\w+):\s*(.*)$', re.M)


def front_matter(path):
    try:
        text = open(path, encoding='utf-8', errors='ignore').read()
    except OSError:
        return {}
    m = FM.match(text)
    if not m:
        return {}
    return {k: v.strip().strip('"').strip("'") for k, v in KEY.findall(m.group(1))}


def first_urls(text, *labels):
    urls = []
    for label in labels:
        for m in re.finditer(re.escape(label) + r'[^\n]*?(https?://[^\s)>\]"]+)', text):
            u = m.group(1).rstrip('.,;')
            if u not in urls:
                urls.append(u)
    return urls


def main():
    repo = sys.argv[1] if len(sys.argv) > 1 else '/tmp/support-matrix'
    if not os.path.isdir(repo):
        print(f'仓库不存在：{repo}（先 git clone --depth 1 https://github.com/ruyisdk/support-matrix.git {repo}）')
        return 1

    board_meta = {}
    pairs = []
    raw = {'boards': {}, 'systems': {}}

    for board in sorted(os.listdir(repo)):
        bdir = os.path.join(repo, board)
        if not os.path.isdir(bdir) or board.startswith('.') or board in ('assets', 'report-template'):
            continue
        bm = front_matter(os.path.join(bdir, 'README.md'))
        board_meta[board] = {
            'product': bm.get('product', board),
            'cpu': bm.get('cpu', ''),
            'cpu_core': bm.get('cpu_core', ''),
            'ram': bm.get('ram', ''),
            'vendor': bm.get('vendor', ''),
        }
        raw['boards'][board] = {}
        for sysname in sorted(os.listdir(bdir)):
            sdir = os.path.join(bdir, sysname)
            if not os.path.isdir(sdir):
                continue
            reports = []
            for dirpath, _dn, fns in os.walk(sdir):
                for fn in sorted(fns):
                    if not fn.endswith('.md') or fn.endswith('_zh.md'):
                        continue
                    path = os.path.join(dirpath, fn)
                    fm = front_matter(path)
                    if not fm.get('sys'):
                        continue
                    text = open(path, encoding='utf-8', errors='ignore').read()
                    rel = os.path.relpath(path, sdir)[:-3].replace(os.sep, '/')
                    reports.append({
                        'ver': fm.get('sys_ver', '') if fm.get('sys_ver') != 'null' else '',
                        'var': fm.get('sys_var', '') if fm.get('sys_var') != 'null' else '',
                        'status': (fm.get('status', '') or '').lower(),
                        'date': fm.get('last_update', '') or fm.get('last_updated', ''),
                        'url': f'{SITE}/reports/{board}/{sysname}/{rel}/',
                        'downloads': first_urls(text, 'Download Links', 'Download Link', 'Download'),
                        'docs': first_urls(text, 'Reference Installation Document',
                                           'Installation Document', 'Reference Document'),
                    })
            if not reports:
                continue
            statuses = sorted({r['status'] for r in reports if r['status']})
            raw['boards'][board][sysname] = statuses
            pairs.append({
                'board_raw': board,
                'sys_raw': sysname,
                'board': BOARD_MAP.get(board),
                'distro': SYS_MAP.get(sysname),
                'rtos': sysname in RTOS,
                'statuses': statuses,
                'last_update': max((r['date'] for r in reports if r['date']), default=''),
                'reports': sorted(reports, key=lambda r: (r['date'], r['ver']), reverse=True),
            })

    # 只保留本站关心（能映射到 id）且不是 RTOS 的组合
    keep = [p for p in pairs if p['board'] and p['distro'] and not p['rtos']]
    keep.sort(key=lambda p: (p['board'], p['distro']))

    today = datetime.date.today().isoformat()
    lines = [
        '# RuyiSDK 支持矩阵（自动生成，勿手改）',
        '# 来源：https://github.com/ruyisdk/support-matrix → https://matrix.ruyisdk.org',
        f'# 生成于 {today}',
        '',
        'source:',
        f'  site: "{SITE}"',
        '  repo: "https://github.com/ruyisdk/support-matrix"',
        f'  fetched_at: "{today}"',
        '  note: "RuyiSDK 官方测试矩阵：逐板逐系统在真机上的实测报告"',
        '',
        '# status 枚举（取自仓库 CONTRIBUTING.md）',
        'status_legend:',
        '  - "good"',
        '  - "basic"',
        '  - "part"',
        '  - "cft"',
        '  - "cfh"',
        '  - "cfi"',
        '  - "wip"',
        '',
        'items:',
    ]
    for p in keep:
        lines.append(f"  - board: {p['board']}")
        lines.append(f"    board_name: \"{board_meta.get(p['board_raw'], {}).get('product', p['board_raw'])}\"")
        lines.append(f"    distro: {p['distro']}")
        lines.append(f"    distro_name: \"{p['sys_raw']}\"")
        lines.append(f"    status: {p['statuses'][0] if p['statuses'] else 'unknown'}")
        lines.append(f"    last_update: \"{p['last_update']}\"")
        lines.append('    reports:')
        for r in p['reports']:
            lines.append(f"      - ver: \"{r['ver']}\"")
            lines.append(f"        var: \"{r['var']}\"")
            lines.append(f"        status: \"{r['status']}\"")
            lines.append(f"        date: \"{r['date']}\"")
            lines.append(f"        url: \"{r['url']}\"")
            # 报告里记录的下载/文档深链接会随发布滚掉（实测 45 条 404/超时），
            # 本站已有自己维护的 downloads，这里只保留稳定的报告 URL。
    open(OUT_YAML, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')

    os.makedirs('/tmp/rdstr', exist_ok=True)
    json.dump({'source': {'site': SITE, 'fetched_at': today},
               'board_meta': board_meta, 'pairs': keep, 'raw_boards': raw['boards']},
              open('/tmp/rdstr/ruyisdk_matrix.json', 'w'), ensure_ascii=False, indent=1)

    print(f'  板卡（RuyiSDK 侧）{len(board_meta)} 块 | 报告组合 {len(pairs)} 个 | 本站可用 {len(keep)} 个')
    boards = sorted({p['board'] for p in keep})
    distros = sorted({p['distro'] for p in keep})
    print(f'  映射到本站：{len(boards)} 块板 × {len(distros)} 个发行版')
    print(f'    板: {boards}')
    print(f'    发行版: {distros}')
    print(f'  → {OUT_YAML}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
