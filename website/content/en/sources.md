---
title: "Sources"
sub: "Where every claim on this site comes from, how it was judged, and who we thank"
layout: sources
---

**Every technical claim on this site should trace back to a source you can click.** Below are all of them, laid out by primary and secondary source, with a note on how each claim was judged. The site's data is re-verified automatically once a day, and every entry carries its check date.

## 1. Where the test results come from: the RuyiSDK support matrix

Every "this system does / does not work on this board" claim on the site is based first and foremost on the **official RuyiSDK test matrix**:

- Site: <https://matrix.ruyisdk.org/>
- Source repository (the data itself — one markdown file with YAML front matter per board and system): <https://github.com/ruyisdk/support-matrix>
- How we ingest it: we pull that repository daily and parse the `sys / sys_ver / sys_var / status / last_update` fields of each test report, then map them onto the site's board × distro combinations
- Reports follow the pattern `https://matrix.ruyisdk.org/reports/<板>/<系统>/<变体>/` (board / system / variant). The matrix cells and the "RuyiSDK test report" tables on the distro and board pages link straight to the original

**Thanks**: the RuyiSDK team and PLCT Lab (Institute of Software, Chinese Academy of Sciences) have long maintained this per-board, per-system test data. It is one of the few third-party test sets in the RISC-V ecosystem that can be independently checked, and we rely on it rather than reinventing the wheel.

### What the status values mean (quoted from that repository's CONTRIBUTING.md)

| Status | Meaning |
| --- | --- |
| `good` | Fully usable — good enough to run a desktop environment |
| `basic` | Basically usable: it boots and is workable over a serial console |
| `part` | Only partial functionality |
| `cft` | An image exists, but it still needs to be verified on real hardware |
| `cfh` | Official docs or the community say it is supported, but it fails to boot in testing |
| `cfi` | Official docs claim support, but no usable image exists yet |
| `wip` | Only a "will be supported" claim — no image and no source |

In the site's matrix, a cell with a solid symbol is data measured by RuyiSDK; a cell with only a grey dot is site-sourced information that RuyiSDK has not tested. The legend distinguishes the two.

## 2. Official sources for the distros

For all 26 distro entries, the `Download` and `Install docs` links point at **official** pages: the distro's own download site, official documentation site, official wiki or official repository. The typical groups:

- Upstream distros: [debian.org](https://www.debian.org/releases/stable/riscv64/) / [cdimage.debian.org](https://cdimage.debian.org/cdimage/release/current/riscv64/iso-cd/) / [ubuntu.com](https://ubuntu.com/download/risc-v) / [cdimage.ubuntu.com](https://cdimage.ubuntu.com/releases/) / [fedoraproject.org](https://fedoraproject.org/wiki/Architectures/RISC-V) / [get.opensuse.org](https://get.opensuse.org/) / [alpinelinux.org](https://alpinelinux.org/downloads/) / [archlinuxriscv.org](https://archriscv.felixc.at/) / [gentoo.org](https://www.gentoo.org/downloads/) / [nixos.org](https://nixos.org/download/) / [freebsd.org](https://wiki.freebsd.org/riscv) / [netbsd.org](https://www.netbsd.org/ports/riscv/) / [openbsd.org](https://www.openbsd.org/riscv64.html)
- Vendor downstream systems: [revyos.com](https://revyos.com/) and [docs.revyos.dev](https://docs.revyos.dev/) (XuanTie TH1520/SG2042), [spacemit.com](https://www.spacemit.com/) and [archive.spacemit.com](https://archive.spacemit.com/) (Bianbu), [openeuler.org](https://www.openeuler.org/zh/download/) and [docs.openeuler.org](https://docs.openeuler.org/), [openkylin.top](https://www.openkylin.top/downloads/) and docs.openkylin.top, [deepin.org](https://www.deepin.org/) and [deepin-community.github.io](https://deepin-community.github.io/sig-deepin-ports/images/riscv64)
- Community builds: [armbian.com](https://www.armbian.com/download/), [dietpi.com](https://dietpi.com/#download), [irradium.org](https://irradium.org/), bredos.org, FVF's release repositories

The "Sources for this page" section at the bottom of each distro page lists every link that entry is based on.

## 3. Board vendor sources

Specifications and official system information for the 25 boards come from vendor product pages, vendor documentation sites and vendor repositories, for example:

- [sifive.com](https://www.sifive.com/boards) (HiFive Unmatched / Premier P550), [starfivetech.com](https://www.starfivetech.com/en) and [doc-en.rvspace.org](https://doc-en.rvspace.org/) (VisionFive 2 / VisionFive 2 Lite)
- [sipeed.com](https://sipeed.com/) and [wiki.sipeed.com](https://wiki.sipeed.com/) (LicheePi 4A / Lichee Cluster 4A), [milkv.io](https://milkv.io/) and `milkv.io/docs` (Meles / Mars / Jupiter / Pioneer / Megrez / Titan / Duo)
- [banana-pi.org](https://www.banana-pi.org/) and [docs.banana-pi.org](https://docs.banana-pi.org/) (BPI-F3), [orangepi.org](http://www.orangepi.org/) (RV2), [kendryte.com](https://www.kendryte.com/) and the Canaan developer site (K230), [spacemit.com](https://www.spacemit.com/) (K3 Pico-ITX / CoM260)
- Zhihe Computing A210 / XuanTie MelonPi: [zhcomputing.com](http://www.zhcomputing.com/) and [developer.zhcomputing.com](https://developer.zhcomputing.com/zh/docs/A210/), plus the A210_SODIMM_V2 report in [matrix.ruyisdk.org](https://matrix.ruyisdk.org/)
- QEMU: the RISC-V virt machine chapter of the official docs at [qemu.org](https://www.qemu.org/docs/master/system/riscv/virt.html)

For a few of the newer boards the hardware details come straight from the board metadata in the RuyiSDK matrix; those entries are marked on the page as "board information taken from the RuyiSDK test matrix record; availability and pricing not independently verified".

## 4. The AI software dimension: evidence for every line

The AI support pages don't go on impressions — every judgement has a link behind it, mainly from:

- **Upstream project documentation**: [github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) (including `docs/build-riscv64-spacemit.md` and the measured SpacemiT kernel numbers), [github.com/microsoft/onnxruntime](https://github.com/microsoft/onnxruntime), the RISC-V wiki of [github.com/opencv/opencv](https://github.com/opencv/opencv), the RISC-V CI of [github.com/Tencent/ncnn](https://github.com/Tencent/ncnn), [github.com/OAID/Tengine](https://github.com/OAID/Tengine)
- **Third-party distribution**: [riseproject.dev](https://riseproject.dev/) (RISE's PyTorch wheels for RISC-V), [github.com/felixonmars/archriscv-packages](https://github.com/felixonmars/archriscv-packages)
- **Academic work**: arXiv 2503.17422 (V-Seek, LLM inference optimisation on SG2042)
- **Vendor toolchain documentation**: XuanTie HHB (LicheePi 4A NPU), SpacemiT AI SDK, ESWIN ENNP SDK, Canaan nncase, Zhihe TORQ-Toolkit
- **Hands-on write-ups**: CNX Software, ServeTheHome, The Register, Phoronix and others, on specific boards

Where we could not find public evidence, the page says "no public evidence found" instead of guessing.

## 5. Secondary sources and how we label them

Anything a media outlet reported is marked as second-hand: it never serves as primary evidence and is only there to show that the claim exists. Common sources include CNX Software, Phoronix, ServeTheHome, The Register, The Next Platform and Design & Reuse, plus, on the Chinese side, ITHome, ICSmart, Shanghai Observer, Science and Technology Daily and Caixin. Performance and deployment claims made by vendors themselves (for example "32-way concurrent inference reaches 95.8% of an x86 platform" or "already deployed in intelligent computing centres in multiple regions") are always labelled "vendor-reported" and kept separate from third-party measurements.

## 6. Method and caveats

- **Check dates**: every entry has a `checked` field, shown on the page as a "last checked" date. The data is re-verified automatically at 03:00 every day
- **No guessing**: fields we cannot find are left blank. If a vendor has not published a price, a TDP or the exact SoC model, we would rather leave it out than put in a number that looks reasonable
- **Link checking**: every outbound link on the site is verified one by one with curl by `scripts/check_urls.py`. Dead links are replaced with a stable index page or the official download page; if nothing suitable exists, the link is removed
- **Corrections**: if you spot a problem, open an issue or an MR with the specific entry and the supporting link — we change things according to the evidence

## 7. Acknowledgements

Thanks to these projects and teams; the data on this site is built on their work:

- **The RuyiSDK team / PLCT Lab (Institute of Software, Chinese Academy of Sciences)** — the per-board, per-system test matrix, our single most important data source
- **The distro communities and maintainers** — Debian, Ubuntu, Fedora, openSUSE, Alpine, Arch Linux RISC-V, Gentoo, NixOS, FreeBSD, NetBSD, OpenBSD, ALT Linux, Buildroot, Yocto and others
- **The board vendors and their communities** — SiFive, StarFive, Sipeed, Milk-V, Banana Pi, Orange Pi, SpacemiT, ESWIN, UltraRISC, Canaan, Zhihe, PINE64, BIT-BRICK
- **The Chinese distro teams** — openEuler RISC-V SIG, openKylin, deepin, openRuyi
- **The open-source AI projects** — llama.cpp, ONNX Runtime, OpenCV, ncnn, Tengine, RISE Project
- **RISC-V International** — the specifications and the ecosystem infrastructure
