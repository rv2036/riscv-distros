# -*- coding: utf-8 -*-
"""distros.yaml: upstream_note / based_on / versions / derivatives / note 的英译。"""

M = {}

# ---- upstream_note ----
M["Debian 13 (trixie) 起 riscv64 为官方发布架构——官方新闻稿原文：\"This release for the first time officially supports the riscv64 architecture\"；进入主归档 deb.debian.org，不是 ports 附加树（debian.org/ports 列表中 riscv64 标注 13/released）。"] = \
    "riscv64 has been an official release architecture since Debian 13 (trixie) — the official announcement says: \"This release for the first time officially supports the riscv64 architecture\". It lives in the main archive on deb.debian.org, not the ports add-on tree (debian.org/ports lists riscv64 as 13/released)."

M["Canonical 官方构建并托管 riscv64 镜像（\"built and hosted by Canonical\"），riscv64 是 Ubuntu 官方支持架构；26.04 LTS 起 ISA 基线升到 RVA23S64。"] = \
    "Canonical builds and hosts the riscv64 images itself (\"built and hosted by Canonical\"); riscv64 is an officially supported Ubuntu architecture. From 26.04 LTS the ISA baseline moves to RVA23S64."

M["Fedora 官方 wiki 原文：\"riscv64 is currently not an officially supported Fedora architecture\"。镜像由 Fedora RISC-V SIG 维护，放在 dl.fedoraproject.org/pub/alt/risc-v/（alt 树，非主架构），不参与 release blocking。"] = \
    "The official Fedora wiki states: \"riscv64 is currently not an officially supported Fedora architecture\". Images are maintained by the Fedora RISC-V SIG under dl.fedoraproject.org/pub/alt/risc-v/ (an alt tree, not a primary architecture) and do not take part in release blocking."

M["Fedora-V Force（多啦V盟）是独立团队/社区项目，自行编译 Fedora 36→rawhide 的 riscv64 构建并适配板卡；官网自述 \"independently compiling releases from Fedora 36 to rawhide\"，与 Fedora 官方发布流程无隶属关系。"] = \
    "Fedora-V Force is an independent team/community project that compiles its own riscv64 builds from Fedora 36 through rawhide and adapts them to boards; its site says it is \"independently compiling releases from Fedora 36 to rawhide\", and it has no affiliation with Fedora's official release process."

M["下游定制发行版：PLCT Lab（中科院软件所）为玄铁/T-Head（XuanTie）生态维护，复用 Debian 13 (trixie) 软件包仓 + 玄铁定制内核，不是 Debian 官方 port，也不是独立包体系。"] = \
    "Downstream vendor distro: maintained by PLCT Lab (Institute of Software, CAS) for the XuanTie/T-Head ecosystem, reusing the Debian 13 (trixie) package archive plus a XuanTie-customized kernel. It is neither an official Debian port nor an independent package base."

M["下游定制发行版：进迭时空（SpacemiT）官方 OS，明确『基于 Ubuntu 社区源码构建』，APT + deb 包格式；K1 走 Ubuntu 24.04(2.x)/25.04(3.x)，K3 走 Ubuntu 26.04(4.x)。"] = \
    "Downstream vendor distro: the official OS from SpacemiT, explicitly described as built from Ubuntu community sources, using APT and .deb packages; K1 follows Ubuntu 24.04 (2.x)/25.04 (3.x), K3 follows Ubuntu 26.04 (4.x)."

M["官方构建框架（armbian/build）直接出 riscv64 镜像，板卡按 Platinum/Standard/Community 分级；RISC-V 板在官网有独立下载页与镜像清单。"] = \
    "The official build framework (armbian/build) produces riscv64 images directly, with boards graded Platinum/Standard/Community; RISC-V boards get their own download page and image list on the site."

M["riscv64 是 Alpine 官方支持架构：官方 downloads 页与 x86_64/aarch64 并列提供 standard ISO、minirootfs、uboot 镜像，包仓库 main/community 均有 riscv64 构建。"] = \
    "riscv64 is an officially supported Alpine architecture: the downloads page offers standard ISO, minirootfs and uboot images next to x86_64/aarch64, and both the main and community repos build for riscv64."

M["Arch Linux RISC-V 是社区移植（archriscv.felixc.at，Felix Yan 等维护）：在 Arch 源码包上叠加 patch 构建，尚未进入 Arch 官方仓库。官网自述长期目标才是 \"riscv64 can be added to Arch Linux itself as an alternative architecture\"。"] = \
    "Arch Linux RISC-V is a community port (archriscv.felixc.at, maintained by Felix Yan and others): it builds Arch source packages with an extra patch set and is not in the official Arch repos yet. Its site says the long-term goal is only \"riscv64 can be added to Arch Linux itself as an alternative architecture\"."

M["RISC-V 在 download.opensuse.org/ports/ 端口树（ports/riscv/），属社区移植，不是 openSUSE 主架构；只有 Tumbleweed 与 MicroOS，没有 Leap 的 riscv64 版本。"] = \
    "RISC-V sits in the download.opensuse.org/ports/ port tree (ports/riscv/) as a community port, not an openSUSE primary architecture; only Tumbleweed and MicroOS exist — there is no Leap riscv64."

M["官方架构：ARCH=riscv，~riscv keyword，release engineering 出 rv64gc/rv32gc stage3（lp64d/lp64/multilib、openrc/systemd、glibc/musl 全组合）；官方明确暂无 stable keyword 计划。"] = \
    "Official architecture: ARCH=riscv with the ~riscv keyword; release engineering ships rv64gc/rv32gc stage3 for every combination of lp64d/lp64/multilib, openrc/systemd and glibc/musl. The project states there is no plan for a stable keyword."

M["nixpkgs 的 nixpkgs-unstable 与 stable channel 都没有官方 riscv64-linux 支持；官方 wiki 明确写“所有 RISC-V 平台目前都是实验性”，镜像由社区提供。"] = \
    "Neither nixpkgs-unstable nor the stable channels officially support riscv64-linux; the official wiki says all RISC-V platforms are currently experimental, and images come from the community."

M["riscv64 为官方 Tier 2 架构（14.x/15.x/16.x 规划均 Tier 2），提供正式 RELEASE 安装镜像，硬件说明里列明支持平台。"] = \
    "riscv64 is an official Tier 2 architecture (14.x/15.x/16.x are all planned as Tier 2), with formal RELEASE install images and the supported platforms listed in the hardware notes."

M["官方 port（tier 2），NetBSD 11.0 提供 riscv64 安装集与 pkgsrc 预编译包，支持 RV64/SV39。"] = \
    "Official port (tier 2); NetBSD 11.0 provides riscv64 install sets and prebuilt pkgsrc packages, supporting RV64/SV39."

M["riscv64 是官方移植（openbsd.org/riscv64.html），当前目标平台为 SiFive HiFive Unmatched，随每个 release 出 riscv64 安装镜像并定期出 snapshot。"] = \
    "riscv64 is an official port (openbsd.org/riscv64.html); the current target platform is the SiFive HiFive Unmatched, with a riscv64 install image per release and regular snapshots."

M["官方 riscv64 移植：Sisyphus 的 riscv64 仓库 + Regular riscv64 测试镜像（jeos-systemd/lxqt/mate/xfce，rv64gc），由 ALT 团队维护并有 riscv-devel 邮件列表。"] = \
    "Official riscv64 port: a riscv64 repo in Sisyphus plus Regular riscv64 test images (jeos-systemd/lxqt/mate/xfce, rv64gc), maintained by the ALT team with a riscv-devel mailing list."

M["构建系统（不是成品发行版）：树内自带 qemu_riscv32/64_virt、spike、hifive_unmatched、visionfive/visionfive2、sipeed_licheepi_4a 等 defconfig，RISC-V 是一等公民。"] = \
    "A build system, not a ready-made distro: the tree ships defconfigs for qemu_riscv32/64_virt, spike, hifive_unmatched, visionfive/visionfive2, sipeed_licheepi_4a and more — RISC-V is a first-class citizen."

M["构建系统：oe-core 自带 qemuriscv32/qemuriscv64 machine 与 riscv64 tune；具体板卡靠官方 RISC-V 层 meta-riscv（riscv/ 组织下）提供 machine 配置。"] = \
    "Build system: oe-core ships the qemuriscv32/qemuriscv64 machines and a riscv64 tune; concrete boards come from the official RISC-V layer meta-riscv (under the riscv/ org), which provides the machine configs."

M["独立发行版（自身即上游）：openEuler 社区（开放原子基金会）官方多架构同源构建，RISC-V 由 OERV SIG 移植维护，不是 Debian/Ubuntu 定制。"] = \
    "Independent distro (it is its own upstream): the openEuler community (OpenAtom Foundation) builds all architectures from one source tree, with RISC-V ported and maintained by the OERV SIG — not a Debian/Ubuntu customization."

M["独立发行版：openKylin（开放麒麟）社区自建 deb 仓库与 UKUI 桌面，官方定位为独立根社区操作系统，不是 Ubuntu/Debian 直接派生；RISC-V 由 openKylin RISC-V SIG 适配。"] = \
    "Independent distro: the openKylin community builds its own deb repos and the UKUI desktop, positioning itself as an independent root community OS rather than a direct Ubuntu/Debian derivative; RISC-V is adapted by the openKylin RISC-V SIG."

M["下游定制发行版：deepin（深度）社区版继承 Debian 软件包并叠加自有仓库与玲珑包体系；RISC-V 由 deepin-ports SIG 维护，官方标注为『技术预览』。"] = \
    "Downstream vendor distro: the deepin community edition inherits Debian packages and adds its own repos and the linglong package format; RISC-V is maintained by the deepin-ports SIG and officially marked as a technical preview."

M["独立发行版：中科院软件所（ISCAS）发起并长期维护的 RISC-V 原生发行版，自建 RPM 包集与构建流水线（SPECS/dnf），不基于 Debian/Ubuntu/openEuler 的二进制包。"] = \
    "Independent distro: a RISC-V native distro initiated and long maintained by ISCAS (Institute of Software, Chinese Academy of Sciences), with its own RPM package set and build pipeline (SPECS/dnf); it does not build on Debian/Ubuntu/openEuler binaries."

M["无 riscv64 目标：官方仓库只有 x86_64/i686/aarch64/armv6l/armv7l（含 musl 变体），下载页与 /live/current 均无 RISC-V 镜像。"] = \
    "No riscv64 target: the official repos only carry x86_64/i686/aarch64/armv6l/armv7l (including musl variants), and neither the download page nor /live/current has RISC-V images."

M["无 RISC-V 移植：ftp 上 th/3.0 线的二进制仓库只有 i686/x86_64/x32/noarch，官网、Machines 页、镜像列表均无 riscv64 相关内容。"] = \
    "No RISC-V port: the th/3.0 binary repos on the ftp only carry i686/x86_64/x32/noarch, and the site, the Machines page and the mirror list say nothing about riscv64."

M["官方 Slackware 15.0 只发 x86_64（slackware.com 另有官方 ARM 项目 arm.slackware.com）；RISC-V 由非官方 slarm64 移植（sndwvs）跟随 15.0/current 提供软件包与板级镜像。"] = \
    "Official Slackware 15.0 is x86_64 only (slackware.com also runs the official ARM project at arm.slackware.com); RISC-V comes from the unofficial slarm64 port (sndwvs), which tracks 15.0/current with packages and board images."

M["AOSP 主线保留 riscv64 target（build/target/product/aosp_riscv64.mk、module_riscv64.mk），但只在 Cuttlefish 虚拟设备上验证；2024 年 Android Common Kernel/GKI 移除了 RISC-V 支持，Google 称仍在 AOSP 继续。"] = \
    "The AOSP mainline keeps a riscv64 target (build/target/product/aosp_riscv64.mk, module_riscv64.mk) but only validates it on the Cuttlefish virtual device; in 2024 the Android Common Kernel/GKI removed RISC-V support, and Google says work continues in AOSP."

# ---- based_on ----
M["独立"] = "Independent"
M["Debian"] = "Debian"
M["Fedora"] = "Fedora"
M["Debian 13 (trixie) rootfs + 玄铁定制 6.6 内核（TH1520/SG2042 BSP）；旧版 20240720 为 Debian 12 + 5.10 内核"] = \
    "Debian 13 (trixie) rootfs + XuanTie-customized 6.6 kernel (TH1520/SG2042 BSP); the older 20240720 build is Debian 12 + 5.10 kernel"
M["Ubuntu 24.04 LTS（Bianbu 2.x，K1）/ Ubuntu 25.04（Bianbu 3.x，K1）/ Ubuntu 26.04（Bianbu 4.x，K3；厂商论坛口径，官方文档未逐版标注）+ 厂商 BSP 内核 6.6 LTS / 6.18"] = \
    "Ubuntu 24.04 LTS (Bianbu 2.x, K1) / Ubuntu 25.04 (Bianbu 3.x, K1) / Ubuntu 26.04 (Bianbu 4.x, K3; per vendor forum, not stated per release in official docs) + vendor BSP kernel 6.6 LTS / 6.18"
M["Debian/Ubuntu（Armbian build framework）"] = "Debian/Ubuntu (Armbian build framework)"
M["Arch Linux"] = "Arch Linux"
M["独立（源码构建，OpenRC/systemd 可选）"] = "Independent (built from source, OpenRC/systemd optional)"
M["独立（Nix/nixpkgs，systemd）"] = "Independent (Nix/nixpkgs, systemd)"
M["独立（BSD，FreeBSD 内核 + pkg）"] = "Independent (BSD, FreeBSD kernel + pkg)"
M["独立（BSD，NetBSD 内核 + pkgsrc）"] = "Independent (BSD, NetBSD kernel + pkgsrc)"
M["独立（BSD，OpenBSD 内核 + ports/packages）"] = "Independent (BSD, OpenBSD kernel + ports/packages)"
M["独立（RPM/apt-rpm，ALT 自有工具链）"] = "Independent (RPM/apt-rpm, ALT's own toolchain)"
M["自行编译（BusyBox/glibc/musl + 可选包）"] = "Built from source (BusyBox/glibc/musl + optional packages)"
M["自行编译（BitBake + oe-core + meta-riscv）"] = "Built from source (BitBake + oe-core + meta-riscv)"
M["openEuler 24.03 LTS（RPM/dnf，自建源）+ RVCK 6.6 内核；RISC-V 分 RVA20 与 RVA23 两套构建"] = \
    "openEuler 24.03 LTS (RPM/dnf, own repos) + RVCK 6.6 kernel; RISC-V ships as two separate builds, RVA20 and RVA23"
M["独立构建（deb/APT + 自建源，UKUI 桌面）；3.0 用 Linux 7.0 内核，2.0 SP2 为长期稳定版"] = \
    "Independent build (deb/APT + own repos, UKUI desktop); 3.0 uses a Linux 7.0 kernel, 2.0 SP2 is the long-term stable release"
M["Debian 系 + deepin 自有仓库（deepin 25『crimson』）；内核按板卡 6.6/6.12/6.16，DP1000 用主线内核"] = \
    "Debian-based + deepin's own repos (deepin 25 \"crimson\"); kernel 6.6/6.12/6.16 depending on board, mainline kernel on DP1000"
M["独立自建（RPM + dnf，滚动发布）；内核 7.2.6 / LTS 6.18.54，工具链 GCC 16.2 / glibc 自带"] = \
    "Independent, self-built (RPM + dnf, rolling release); kernel 7.2.6 / LTS 6.18.54, toolchain GCC 16.2 with its own glibc"
M["独立（XBPS + runit + musl/glibc）"] = "Independent (XBPS + runit + musl/glibc)"
M["独立（RPM + poldek，波兰社区发行版）"] = "Independent (RPM + poldek, Polish community distro)"
M["独立（pkgtools + slackpkg，BSD 风格 init）"] = "Independent (pkgtools + slackpkg, BSD-style init)"
M["AOSP（Linux 内核 + Android 框架）"] = "AOSP (Linux kernel + Android framework)"

# ---- versions ----
M["13.7 (trixie, 当前稳定, ISO 为 debian-13.7.0-riscv64-netinst.iso)"] = \
    "13.7 (trixie, current stable; ISO is debian-13.7.0-riscv64-netinst.iso)"
M["14 (forky, 开发/测试中)"] = "14 (forky, in development/testing)"
M["26.10 (当前版, RVA23)"] = "26.10 (current, RVA23)"
M["24.04.5 LTS (RVA20, 旧硬件继续支持)"] = "24.04.5 LTS (RVA20, older hardware still supported)"
M["44 (稳定版, 已有 RISC-V 镜像)"] = "44 (stable, RISC-V images available)"
M["45 (Beta/RC, RISC-V 镜像标注 \"non-official, community-contributed\")"] = \
    "45 (Beta/RC, RISC-V images labelled \"non-official, community-contributed\")"
M["Fedora 36 → rawhide（自主构建，覆盖多个 Fedora 版本）"] = \
    "Fedora 36 → rawhide (built independently, covering several Fedora releases)"
M["20260504（2026-05-04，镜像站最新完整镜像）"] = "20260504 (2026-05-04, newest full image on the mirror)"
M["20251226（2025-12-26，官方文档标注的最新版）"] = "20251226 (2025-12-26, newest version listed in the official docs)"
M["20250729（2025-07-29）"] = "20250729 (2025-07-29)"
M["20240720（2024-07-20，5.10 内核 / Debian 12 时代）"] = "20240720 (2024-07-20, 5.10 kernel / Debian 12 era)"
M["Bianbu 2.3.5（K1，Ubuntu 24.04 基线，2026-06 构建 / 2026-08-27 上传）"] = \
    "Bianbu 2.3.5 (K1, Ubuntu 24.04 base, built 2026-06 / uploaded 2026-08-27)"
M["Bianbu 3.0.1（K1，Ubuntu 25.04 基线，2025-08-15）"] = "Bianbu 3.0.1 (K1, Ubuntu 25.04 base, 2025-08-15)"
M["Bianbu 4.0.8（K3，Ubuntu 26.04 基线，2026-10-22）"] = "Bianbu 4.0.8 (K3, Ubuntu 26.04 base, 2026-10-22)"
M["26.8.9（MusePi Pro）"] = "26.8.9 (MusePi Pro)"
M["26.8.3（BPI-F3 / K3 Pico-ITX）"] = "26.8.3 (BPI-F3 / K3 Pico-ITX)"
M["3.24.3 (当前稳定, alpine-standard-3.24.3-riscv64.iso)"] = \
    "3.24.3 (current stable, alpine-standard-3.24.3-riscv64.iso)"
M["edge (开发分支)"] = "edge (development branch)"
M["rolling (ISO archlinux-2026.08.27-riscv64.iso, rootfs archriscv-2026-08-27.tar.zst)"] = \
    "rolling (ISO archlinux-2026.08.27-riscv64.iso, rootfs archriscv-2026-08-27.tar.zst)"
M["Tumbleweed (rolling, 当前 ISO Snapshot20260924)"] = "Tumbleweed (rolling, current ISO Snapshot20260924)"
M["MicroOS 16.0.0 (riscv64, Snapshot20260924)"] = "MicroOS 16.0.0 (riscv64, Snapshot20260924)"
M["rolling（stage3 rv64_lp64d-openrc 20261026T164559Z）"] = \
    "rolling (stage3 rv64_lp64d-openrc 20261026T164559Z)"
M["26.05（官方仅 x86_64/aarch64）"] = "26.05 (official builds for x86_64/aarch64 only)"
M["unstable（riscv64 社区构建）"] = "unstable (community riscv64 builds)"
M["15.1-RELEASE（production，2026-06-16）"] = "15.1-RELEASE (production, 2026-06-16)"
M["14.5-RELEASE（legacy）"] = "14.5-RELEASE (legacy)"
M["11.0（当前 release）"] = "11.0 (current release)"
M["8.0（当前 release）"] = "8.0 (current release)"
M["Sisyphus（rolling，riscv64 port）"] = "Sisyphus (rolling, riscv64 port)"
M["p11（stable 分支，riscv64 仅 Sisyphus 有）"] = "p11 (stable branch; riscv64 exists only in Sisyphus)"
M["2026.08.1（stable，2026-10-22）"] = "2026.08.1 (stable, 2026-10-22)"
M["2025.02.x LTS（最新点版本 2025.02.19，支持到 2028-03）"] = \
    "2025.02.x LTS (latest point release 2025.02.19, supported until 2028-03)"
M["6.1 Blacksail（当前系列）"] = "6.1 Blacksail (current series)"
M["6.0 Wrynose（LTS，支持到 2030-04）"] = "6.0 Wrynose (LTS, supported until 2030-04)"
M["24.03 LTS SP4（2026-06-30 发布；RISC-V RVA23 ISO 2026-09-08）"] = \
    "24.03 LTS SP4 (released 2026-06-30; RISC-V RVA23 ISO 2026-09-08)"
M["24.03 LTS SP3（2026-03-09 转入长期维护；RVA20 + RVA23 双版本）"] = \
    "24.03 LTS SP3 (moved to long-term maintenance 2026-03-09; both RVA20 and RVA23 builds)"
M["openKylin 3.0（2026-08-31 发布；下载页镜像 2026-09-18，RISC-V 镜像 2026-08-28 / 2026-10-29）"] = \
    "openKylin 3.0 (released 2026-08-31; download-page images 2026-09-18, RISC-V images 2026-08-28 / 2026-10-29)"
M["openKylin 2.0 SP2（2026-08-13 长期稳定版；RISC-V 镜像 2025-08-26）"] = \
    "openKylin 2.0 SP2 (2026-08-13 long-term stable; RISC-V images 2025-08-26)"
M["deepin 25.2.0（RISC-V 通用 ISO，2026-07-07）"] = "deepin 25.2.0 (generic RISC-V ISO, 2026-07-07)"
M["deepin 25 crimson preview（按板卡镜像，K3 最新 2026-05-22）"] = \
    "deepin 25 crimson preview (per-board images, newest K3 build 2026-05-22)"
M["deepin next-crimson preview（K3，2026-09-14）"] = "deepin next-crimson preview (K3, 2026-09-14)"
M["2026.09（2026-09-29 构建）"] = "2026.09 (built 2026-09-29)"
M["2026.08（2026-08-26）"] = "2026.08 (2026-08-26)"
M["2026.07（2026-07-23）"] = "2026.07 (2026-07-23)"
M["rolling（live/ROOTFS 20250202）"] = "rolling (live/ROOTFS 20250202)"
M["Th 2025 snapshot（3.0 线）"] = "Th 2025 snapshot (3.0 line)"
M["15.0（官方，x86_64）"] = "15.0 (official, x86_64)"
M["slarm64-riscv64-current / slarm64-riscv64-15.0（非官方移植）"] = \
    "slarm64-riscv64-current / slarm64-riscv64-15.0 (unofficial port)"
M["Android 17（AOSP，2026-06）"] = "Android 17 (AOSP, 2026-06)"
M["main（trunk_staging）"] = "main (trunk_staging)"

# ---- derivatives ----
M["Ubuntu Base (riscv64 rootfs)"] = "Ubuntu Base (riscv64 rootfs)"
M["DeepComputing FML13V01 partner-built Ubuntu"] = "DeepComputing FML13V01 partner-built Ubuntu"
M["Fedora-V Force (FVF)"] = "Fedora-V Force (FVF)"
M["Fedora Remix for RISC-V"] = "Fedora Remix for RISC-V"
M["DietPi 等基于 Armbian/Debian 的衍生版对 VisionFive 2 有非官方支持"] = \
    "Unofficial VisionFive 2 support exists in derivatives such as DietPi (Armbian/Debian based)"
M["postmarketOS"] = "postmarketOS"
M["nixos-riscv64（社区镜像集）"] = "nixos-riscv64 (community image set)"
M["nixos-licheepi4a / nixos-vf2（板级 flake）"] = "nixos-licheepi4a / nixos-vf2 (board-level flakes)"
M["Simply Linux / ALT Mobile（同仓库体系，无 riscv64 构建）"] = \
    "Simply Linux / ALT Mobile (same repo family, no riscv64 builds)"
M["大量厂商 SDK 基于 Buildroot（如部分 D1/K230 SDK）"] = \
    "Many vendor SDKs are Buildroot-based (e.g. some D1/K230 SDKs)"
M["SpacemiT / StarFive / T-Head 等厂商的 Yocto BSP 均基于 oe-core + meta-riscv 模式"] = \
    "Vendor Yocto BSPs from SpacemiT / StarFive / T-Head follow the oe-core + meta-riscv pattern"
M["EulixOS"] = "EulixOS"
M["Eulaceura"] = "Eulaceura"
M["统信 UOS"] = "UnionTech UOS"
M["slarm64（aarch64/riscv64 非官方移植）"] = "slarm64 (unofficial aarch64/riscv64 port)"
M["Slackware ARM（官方 ARM 项目，无 RISC-V）"] = "Slackware ARM (official ARM project, no RISC-V)"

# ---- note ----
M["Debian 是这批里唯一把 riscv64 放进正式发布架构的独立发行版；衍生作品另有 Deepin、RevyOS 等基于 Debian 的 riscv64 系统（未逐项核实）。"] = \
    "Debian is the only independent distro here that made riscv64 an official release architecture; separately there are Debian-based riscv64 systems such as deepin and RevyOS (not verified one by one)."
M["Ubuntu 是板级支持做得最细的一家：官方按板发 preinstalled 镜像，但 26.04 起把门槛抬到 RVA23，老板被锁在 24.04 LTS。"] = \
    "Ubuntu has the most detailed board support: it publishes preinstalled images per board, but 26.04 raised the bar to RVA23, leaving older boards stuck on 24.04 LTS."
M["Fedora 有官方 SIG 和持续构建，但架构身份仍是 \"not officially supported\"，这条要在页面上写清楚，别和 Debian/Ubuntu 并列成\"官方支持\"。"] = \
    "Fedora has an official SIG and continuous builds, but its architecture status is still \"not officially supported\" — the page should say so plainly instead of listing it next to Debian/Ubuntu as officially supported."
M["FVF 本身就是 Fedora 的 RISC-V 下游构建；把它单列一条是为了和 Fedora 官方 SIG 区分开，不要混为一谈。"] = \
    "FVF is itself a downstream RISC-V build of Fedora; it has its own entry to keep it apart from the official Fedora SIG — don't conflate the two."
M["TH1520 板卡的事实标准系统：LicheePi 4A、Milk-V Meles 出厂/官方教程默认刷 RevyOS。新手上手首选，但注意镜像站比文档新，按镜像站目录取最新日期。"] = \
    "The de facto standard on TH1520 boards: LicheePi 4A and Milk-V Meles ship with RevyOS, and the official tutorials flash it too. The best first pick for newcomers, but note that the mirror is newer than the docs — take the latest date from the mirror directory."
M["K1/K3 板卡（BPI-F3、Milk-V Jupiter、MUSE、Pico ITX）唯一有官方桌面体验的系统，开箱 GNOME/LXQt，中文文档完整，是最适合新人的厂商发行版。"] = \
    "The only system with an official desktop experience on K1/K3 boards (BPI-F3, Milk-V Jupiter, MUSE, Pico-ITX): GNOME/LXQt out of the box and complete documentation, making it the friendliest vendor distro for newcomers."
M["国产 RISC-V 板“能开箱用”的最大功臣；K3/BPI-F3 这类新板优先看它。"] = \
    "The main reason domestic RISC-V boards are usable out of the box; look here first for newer boards like K3/BPI-F3."
M["Alpine 的 riscv64 是正式架构，但板级支持面窄——u-boot 包就那五个，超出范围的板子等于自己移植。"] = \
    "Alpine's riscv64 is a real architecture, but board coverage is narrow — there are only those five u-boot packages, so anything outside them means porting it yourself."
M["Arch 的 \"官方\" 只是该移植项目自己的 tested 列表，不等于 Arch 官方支持——页面上要标明是社区 port。"] = \
    "Arch's \"official\" here is only the port's own tested list, not official Arch support — the page should mark it as a community port."
M["MicroOS 是同项目的 riscv64 变体（有 kvm-and-xen qcow2 镜像），不算下游衍生。"] = \
    "MicroOS is a riscv64 variant of the same project (there is a kvm-and-xen qcow2 image), not a downstream derivative."
M["老手友好、新手劝退：文档齐全但全手工安装，适合想深度定制或做嵌入式 rootfs 的人。"] = \
    "Friendly to veterans, discouraging for beginners: complete docs but a fully manual install, good for people who want deep customization or an embedded rootfs."
M["声明式配置很香，但 riscv64 属于“能跑、别指望省心”的状态。"] = \
    "Declarative config is nice, but riscv64 is in a \"it runs, don't expect an easy ride\" state."
M["想要“类 Unix 正经系统 + 官方镜像”的话，FreeBSD 是 RISC-V 上最稳的非 Linux 选择。"] = \
    "If you want a proper Unix-like system with official images, FreeBSD is the most solid non-Linux option on RISC-V."
M["QEMU 上体验顺畅；实机取决于你有没有现成 U-Boot。"] = \
    "Smooth under QEMU; on real hardware it depends on whether you already have a working U-Boot."
M["安全取向、极简；有 Unmatched 的话体验最正统，否则不建议新手入。"] = \
    "Security-focused and minimal; the experience is most orthodox on an Unmatched, otherwise not a beginner's pick."
M["俄系里 RISC-V 支持最完整的一支，镜像开箱可用，适合 QEMU 与 Unmatched 玩家。"] = \
    "The most complete RISC-V support among Russian distros, with images that work out of the box; suited to QEMU and Unmatched users."
M["给新人标注清楚：不是发行版，是“自己做发行版”的工具箱。"] = \
    "Make it clear to newcomers: this is not a distro but a toolbox for building your own."
M["工业/量产向；个人玩家建议先用 Armbian 或 Buildroot 试水。"] = \
    "Aimed at industrial/production use; hobbyists should start with Armbian or Buildroot instead."
M["服务器/企业场景的 RISC-V 底座，RVA23 + Server Platform 规范推进最快；个人开发板用户除非要做服务器验证，否则不如 RevyOS/Bianbu 省事。"] = \
    "An RISC-V base for server/enterprise use, moving fastest on RVA23 + Server Platform; unless you are validating server scenarios, RevyOS/Bianbu will save you trouble on a dev board."
M["国产桌面 OS 的 RISC-V 分支，板卡覆盖随版本割裂（3.0 只认 K3/V100）。适合想评估国产桌面栈的人，不适合作为 TH1520/K1 老板子的日常系统。"] = \
    "The RISC-V branch of a domestic desktop OS, with board coverage split across versions (3.0 only knows K3/V100). Good for evaluating a domestic desktop stack, not as a daily driver on older TH1520/K1 boards."
M["桌面做得最漂亮的国产发行版，但 RISC-V 分支是社区预览性质、按板卡发 tar.xz，适合评估/尝鲜，不建议作为唯一日常系统。"] = \
    "The best-looking domestic desktop distro, but its RISC-V branch is a community preview shipped as per-board tar.xz files — fine for evaluation, not recommended as your only daily system."
M["主要供厂商/生态测试用：官方定位就是『早期验证』——尽早暴露固件、平台语义与内核互操作问题，让厂商少的分叉。普通用户一般不需要装它，日常使用请选 Bianbu / RevyOS / openKylin 这类厂商发行版；想零成本体验可先用它的 QEMU 镜像。"] = \
    "Mostly for vendor/ecosystem testing: it is officially positioned as early validation — surfacing firmware, platform-semantics and kernel interop problems early so vendors fork less. Regular users normally don't need it; for daily use pick a vendor distro such as Bianbu / RevyOS / openKylin, and try its QEMU image if you just want a zero-cost look."
M["现阶段不适合任何 RISC-V 场景，列出仅为说明“小而快”≠“有 RISC-V”。"] = \
    "Not usable for any RISC-V scenario right now; listed only to show that \"small and fast\" does not mean \"has RISC-V\"."
M["可视为“无 RISC-V 支持”，门户里建议标注为暂不支持，避免误导。"] = \
    "Treat it as \"no RISC-V support\"; mark it as unsupported on the portal rather than misleading readers."
M["Slack 老用户想在 RISC-V 上续命可以试 slarm64，新人不要碰。"] = \
    "Long-time Slackware users can try slarm64 to keep the habit alive on RISC-V; beginners should stay away."
M["只适合想看“Android 框架在 RISC-V 上跑起来”的验证性实验，别当可用系统。"] = \
    "Only for experiments that check whether the Android framework boots on RISC-V — don't treat it as a usable system."
