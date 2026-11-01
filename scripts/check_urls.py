#!/usr/bin/env python3
"""校验站内数据里所有外链可达性（distros / boards / ai / ruyisdk）。

国内站直连，境外站走代理；000/403/412/429/502/503 退避重试。
用法：~/.hermes/hermes-agent/venv/bin/python scripts/check_urls.py [--limit N]
"""
import argparse
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'website', 'data')
PROXY = 'socks5h://192.168.1.182:1080'

DIRECT = ('debian.org', 'ubuntu.com', 'canonical.com', 'cdimage.', 'archive.spacemit',
          'spacemit', 'revyos', 'sipeed', 'milkv.io', 'github.com', 'gitee.com',
          'sophgo', 'starfivetech', 'bpi', 'banana-pi', 'orangepi', 'kendryte',
          'canaan', 'eswin', 'ultrarisc', 'ruyisdk', 'openeuler', 'openkylin',
          'deepin', 'bianbu', 'xrvm', 'zhcomputing', 'lanxin', 'tenstorrent')


def is_direct(url):
    return any(d in url for d in DIRECT)


def check(url, timeout=45):
    code = '000'
    for attempt in range(3):
        cmd = ['curl', '-sS', '-o', '/dev/null', '-w', '%{http_code}', '-L',
               '--max-time', str(timeout), '-A', 'Mozilla/5.0']
        env = dict(os.environ)
        if is_direct(url):
            for k in ('ALL_PROXY', 'all_proxy', 'http_proxy', 'https_proxy', 'HTTP_PROXY', 'HTTPS_PROXY'):
                env.pop(k, None)
        else:
            cmd += ['--proxy', PROXY]
            for k in ('ALL_PROXY', 'all_proxy', 'http_proxy', 'https_proxy', 'HTTP_PROXY', 'HTTPS_PROXY'):
                env.pop(k, None)
        cmd.append(url)
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 10, env=env)
            code = (out.stdout or '').strip() or '000'
        except subprocess.TimeoutExpired:
            code = '000'
        if code in ('200', '206', '301', '302', '304'):
            return url, code
        if code in ('000', '403', '412', '429', '502', '503'):
            time.sleep(1.5 * (attempt + 1))
            continue
        return url, code
    return url, code


def collect():
    urls = set()
    for name in ('distros', 'boards'):
        p = os.path.join(DATA, 'i18n', 'zh', f'{name}.yaml')
        d = yaml.safe_load(open(p, encoding='utf-8'))
        for it in d['items']:
            for k in ('downloads', 'guides'):
                for x in it.get(k) or []:
                    if x.get('url'):
                        urls.add(x['url'])
    ai = os.path.join(DATA, 'i18n', 'zh', 'ai.yaml')
    d = yaml.safe_load(open(ai, encoding='utf-8'))
    for it in d['items']:
        for r in it.get('runs') or []:
            for u in r.get('evidence') or []:
                urls.add(u)
    rp = os.path.join(DATA, 'ruyisdk.yaml')
    if os.path.isfile(rp):
        d = yaml.safe_load(open(rp, encoding='utf-8'))
        for it in d['items']:
            for r in it.get('reports') or []:
                urls.add(r['url'])
                for k in ('downloads', 'docs'):
                    for u in r.get(k) or []:
                        urls.add(u)
    return sorted(urls)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=0)
    a = ap.parse_args()
    urls = collect()
    if a.limit:
        urls = urls[:a.limit]
    print(f'  待检查 {len(urls)} 个唯一 URL')
    bad = []
    with ThreadPoolExecutor(max_workers=10) as ex:
        for url, code in ex.map(check, urls):
            if code not in ('200', '206', '301', '302', '304'):
                bad.append((code, url))
                print(f'  {code}  {url}')
    print(f'\n  合计 {len(urls)} 个，问题 {len(bad)} 个')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
