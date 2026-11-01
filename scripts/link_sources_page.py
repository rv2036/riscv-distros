#!/usr/bin/env python3
"""把「来源与致谢」页里以纯文本列出的来源域名升级成可点击链接。

清单页里为了可读性写的是域名（`debian.org`、`sipeed.com` 这类），对读者来说
能直接点开才有用。这个脚本对五种语言的 sources.md 做同一件事：把已知域名的
纯文本出现替换成 markdown 链接。已经包在链接里的（`[...]`、`<...>`、代码块里
的整行 URL 除外）不重复处理。

用法：python3 scripts/link_sources_page.py [--dry-run]
"""
import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'website', 'content')

# 域名 → 规范链接（都验证过 200）
DOMAINS = {
    'matrix.ruyisdk.org': 'https://matrix.ruyisdk.org/',
    'debian.org': 'https://www.debian.org/releases/stable/riscv64/',
    'cdimage.debian.org': 'https://cdimage.debian.org/cdimage/release/current/riscv64/iso-cd/',
    'ubuntu.com': 'https://ubuntu.com/download/risc-v',
    'cdimage.ubuntu.com': 'https://cdimage.ubuntu.com/releases/',
    'fedoraproject.org': 'https://fedoraproject.org/wiki/Architectures/RISC-V',
    'get.opensuse.org': 'https://get.opensuse.org/',
    'alpinelinux.org': 'https://alpinelinux.org/downloads/',
    'archlinuxriscv.org': 'https://archriscv.felixc.at/',
    'gentoo.org': 'https://www.gentoo.org/downloads/',
    'nixos.org': 'https://nixos.org/download/',
    'freebsd.org': 'https://wiki.freebsd.org/riscv',
    'netbsd.org': 'https://www.netbsd.org/ports/riscv/',
    'openbsd.org': 'https://www.openbsd.org/riscv64.html',
    'altlinux.org': 'https://en.altlinux.org/',
    'revyos.com': 'https://revyos.com/',
    'docs.revyos.dev': 'https://docs.revyos.dev/',
    'spacemit.com': 'https://www.spacemit.com/',
    'archive.spacemit.com': 'https://archive.spacemit.com/',
    'openeuler.org': 'https://www.openeuler.org/zh/download/',
    'docs.openeuler.org': 'https://docs.openeuler.org/',
    'openkylin.top': 'https://www.openkylin.top/downloads/',
    'deepin.org': 'https://www.deepin.org/',
    'deepin-community.github.io': 'https://deepin-community.github.io/sig-deepin-ports/images/riscv64',
    'armbian.com': 'https://www.armbian.com/download/',
    'dietpi.com': 'https://dietpi.com/#download',
    'irradium.org': 'https://irradium.org/',
    'sifive.com': 'https://www.sifive.com/boards',
    'starfivetech.com': 'https://www.starfivetech.com/en',
    'doc-en.rvspace.org': 'https://doc-en.rvspace.org/',
    'sipeed.com': 'https://sipeed.com/',
    'wiki.sipeed.com': 'https://wiki.sipeed.com/',
    'milkv.io': 'https://milkv.io/',
    'banana-pi.org': 'https://www.banana-pi.org/',
    'docs.banana-pi.org': 'https://docs.banana-pi.org/',
    'orangepi.org': 'http://www.orangepi.org/',
    'kendryte.com': 'https://www.kendryte.com/',
    'zhcomputing.com': 'http://www.zhcomputing.com/',
    'developer.zhcomputing.com': 'https://developer.zhcomputing.com/zh/docs/A210/',
    'qemu.org': 'https://www.qemu.org/docs/master/system/riscv/virt.html',
    'riseproject.dev': 'https://riseproject.dev/',
    'ultrarisc.com': 'https://www.ultrarisc.com/',
    'eswincomputing.com': 'https://www.eswincomputing.com/',
    # AI 侧的具体仓库（代码段里出现的是完整路径）
    'github.com/ggml-org/llama.cpp': 'https://github.com/ggml-org/llama.cpp',
    'github.com/microsoft/onnxruntime': 'https://github.com/microsoft/onnxruntime',
    'github.com/opencv/opencv': 'https://github.com/opencv/opencv',
    'github.com/Tencent/ncnn': 'https://github.com/Tencent/ncnn',
    'github.com/OAID/Tengine': 'https://github.com/OAID/Tengine',
    'github.com/felixonmars/archriscv-packages': 'https://github.com/felixonmars/archriscv-packages',
    'github.com/ruyisdk/support-matrix': 'https://github.com/ruyisdk/support-matrix',
}

CODE_SPAN = re.compile(r'`[^`\n]*`')
LINK = re.compile(r'\[[^\]]*\]\([^)]*\)|<https?://[^>]*>|https?://\S+')


NESTED = re.compile(r'\[\[([^\]]+)\]\(([^)]+)\)\]\(([^)]+)\)')
BAD_TAIL = re.compile(r'\((https?://[^)\s]+?)%29\)')


def normalize(text):
    """幂等修复：折叠嵌套链接、去掉 URL 尾部误捕的右括号。"""
    prev = None
    while prev != text:
        prev = text
        text = NESTED.sub(lambda m: f'[{m.group(1)}]({m.group(2)})' if m.group(2) == m.group(3)
                          else f'[{m.group(1)}]({m.group(2)})', text)
    text = BAD_TAIL.sub(lambda m: f'({m.group(1)})', text)
    return text


def upgrade(text):
    """逐行处理：跳过代码块与已有的链接/自动链接，只替换纯文本域名。"""
    out = []
    in_fence = False
    for line in text.split('\n'):
        if line.strip().startswith('```'):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue

        # 先把已有链接换成占位符，避免二次处理
        keep = []

        def stash(m):
            keep.append(m.group(0))
            return f'\x00{len(keep)-1}\x00'

        line = LINK.sub(stash, line)

        def stash_code(m):
            inner = m.group(0)[1:-1].strip()
            # 代码段里正好是一个已知域名时，升级成链接；其他代码段原样保护
            if inner in DOMAINS:
                return f'[{inner}]({DOMAINS[inner]})'
            return stash(m)

        line = CODE_SPAN.sub(stash_code, line)

        # 长域名先替换，避免 sipeed.com 抢先匹配 wiki.sipeed.com
        for dom in sorted(DOMAINS, key=len, reverse=True):
            url = DOMAINS[dom]
            line = re.sub(r'(?<![\w./-])' + re.escape(dom) + r'(?![\w./-])',
                          f'[{dom}]({url})', line)
        line = re.sub(r'\x00(\d+)\x00', lambda m: keep[int(m.group(1))], line)
        out.append(line)
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    total = 0
    for lang in ('zh', 'en', 'ja', 'ru', 'ko'):
        for path in glob.glob(os.path.join(CONTENT, lang, 'sources.md')):
            src = open(path, encoding='utf-8').read()
            new = normalize(upgrade(normalize(src)))
            added = new.count('](') - src.count('](')
            if new != src:
                total += added
                print(f'  {os.path.relpath(path, ROOT)}: 新增 {added} 个链接')
                if not a.dry_run:
                    open(path, 'w', encoding='utf-8').write(new)
            else:
                print(f'  {os.path.relpath(path, ROOT)}: 无需改动')
    print(f'  合计新增链接 {total} 个' + ('（dry-run）' if a.dry_run else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
