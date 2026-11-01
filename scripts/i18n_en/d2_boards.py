# -*- coding: utf-8 -*-
"""boards.yaml: distros[].note / downloads[].label / guides[].label / gotchas[] / note 的英译。"""

M = {}

# ---- distros[].note ----
M["Debian 13 起 riscv64 为正式架构，官方 netinst ISO 可直接装进 virt"] = \
    "riscv64 is a first-class architecture since Debian 13; the official netinst ISO installs straight into virt"
M["官方 riscv64 cloud image，配 EDK2(pflash) 或 -kernel 启动"] = \
    "Official riscv64 cloud image, booted with EDK2 (pflash) or -kernel"
M["Fedora RISC-V 提供 QEMU 安装说明与镜像"] = "Fedora RISC-V provides QEMU install docs and images"
M["只有 riscv64 minirootfs，无 virt ISO，需自备内核/initramfs"] = \
    "riscv64 minirootfs only, no virt ISO; bring your own kernel/initramfs"
M["archriscv 提供 riscv64 ISO，可在 QEMU 启动"] = "archriscv provides a riscv64 ISO that boots in QEMU"
M["openSUSE Ports 提供 riscv64；官网对 curl 返回 403，未验证直链"] = \
    "openSUSE Ports has riscv64; the site returns 403 to curl, so the direct link is unverified"
M["stage3 riscv64 + 手册支持 QEMU 系统"] = "riscv64 stage3 plus handbook coverage for QEMU systems"
M["有 riscv64 端口，QEMU 镜像需自行构建"] = "The riscv64 port exists; you build the QEMU image yourself"
M["riscv64 非官方支持等级，需交叉构建"] = "riscv64 is not an official support tier; cross-build required"
M["ALT Ports riscv64 提供 QEMU 镜像"] = "ALT Ports riscv64 provides a QEMU image"
M["riscv64 支持 QEMU virt"] = "riscv64 supports QEMU virt"
M["riscv64 端口支持 QEMU"] = "The riscv64 port supports QEMU"
M["openEuler RISC-V SIG 提供 QEMU 镜像"] = "The openEuler RISC-V SIG provides a QEMU image"
M["qemu_riscv64_virt_defconfig，一行 make 起系统"] = "qemu_riscv64_virt_defconfig — one make and the system boots"
M["qemuriscv64 machine 官方支持"] = "qemuriscv64 machine officially supported"
M["StarFive 官方 Debian 202510（Trixie + Wayland 桌面），另有主线 Debian 13 官方安装器可装"] = \
    "StarFive's official Debian 202510 (trixie + Wayland desktop); mainline Debian 13's official installer also works"
M["StarFive 官方 Ubuntu 24.04.3（202510）+ Canonical jh7110 预装镜像"] = \
    "StarFive's official Ubuntu 24.04.3 (202510) plus Canonical's jh7110 preinstalled image"
M["Fedora RISC-V 官方测试板之一"] = "One of the Fedora RISC-V official test boards"
M["openSUSE Ports 提供 riscv64；官网 403，未验证直链"] = \
    "openSUSE Ports has riscv64; the site returns 403, so the direct link is unverified"
M["archriscv 提供 VF2 rootfs/ISO"] = "archriscv provides a VF2 rootfs/ISO"
M["riscv64 minirootfs 可用"] = "riscv64 minirootfs works"
M["Armbian 官方支持 VisionFive 2"] = "Armbian officially supports VisionFive 2"
M["Gentoo wiki 有 VisionFive 2 专页"] = "The Gentoo wiki has a dedicated VisionFive 2 page"
M["NetBSD/riscv 支持 JH7110"] = "NetBSD/riscv supports JH7110"
M["OpenBSD/riscv64 支持 JH7110"] = "OpenBSD/riscv64 supports JH7110"
M["FreeBSD 有 JH7110 支持"] = "FreeBSD has JH7110 support"
M["社区维护，需自建镜像"] = "Community-maintained; build your own image"
M["StarFive SDK 基于 Buildroot，产出 SPL/U-Boot/FIT"] = \
    "The StarFive SDK is Buildroot-based and produces SPL/U-Boot/FIT"
M["社区 meta-starfive 层"] = "Community meta-starfive layer"
M["openEuler RISC-V SIG 提供镜像"] = "The openEuler RISC-V SIG provides images"
M["deepin RISC-V 移植版"] = "deepin RISC-V port"
M["openKylin 有 VF2 镜像"] = "openKylin has a VF2 image"
M["官方主推，最新系统镜像 20251226（Debian 系 + kernel 6.6）"] = \
    "The vendor's recommended system; newest image 20251226 (Debian-based + kernel 6.6)"
M["主线 Debian 13 能在 LPi4A 启动，但需自备 U-Boot/DTB，没有官方安装器镜像"] = \
    "Mainline Debian 13 boots on the LPi4A, but you need your own U-Boot/DTB — there is no official installer image"
M["只有 ubuntu-base rootfs，需自行配内核与引导"] = \
    "Only an ubuntu-base rootfs; set up the kernel and bootloader yourself"
M["Fedora-V Force 提供 TH1520 镜像"] = "Fedora-V Force provides TH1520 images"
M["archriscv 支持 TH1520"] = "archriscv supports TH1520"
M["Armbian 官方支持 LicheePi 4A"] = "Armbian officially supports LicheePi 4A"
M["Gentoo wiki 有 TH1520 专页"] = "The Gentoo wiki has a dedicated TH1520 page"
M["社区仓库 nixos-licheepi4a（复用 RevyOS 内核/U-Boot）"] = \
    "Community repo nixos-licheepi4a (reusing the RevyOS kernel/U-Boot)"
M["社区 openKylin 镜像"] = "Community openKylin image"
M["RevyOS 用 Buildroot 构建 boot/rootfs"] = "RevyOS builds boot/rootfs with Buildroot"
M["官方主推，20251226 系统镜像（kernel 6.6）；Milk-V 官方镜像页已改为指向 RevyOS Docs"] = \
    "The vendor's recommended system, image 20251226 (kernel 6.6); Milk-V's image page now points to the RevyOS docs"
M["openEuler RISC-V SIG 提供 Meles 镜像"] = "The openEuler RISC-V SIG provides Meles images"
M["Debian wiki 的 RISC-V 页面提到 TH1520/Meles，可走 debian-ports 自建"] = \
    "The Debian wiki RISC-V page mentions TH1520/Meles; you can self-build from debian-ports"
M["RevyOS 构建链基于 Buildroot，可自出 boot/rootfs"] = \
    "The RevyOS build chain is Buildroot-based, so you can produce your own boot/rootfs"
M["出厂预装 Bianbu Desktop 3.0；archive 已到 4.0.8（2026-10-16 构建，LXQt/Minimal，含 UEFI 变体）"] = \
    "Ships with Bianbu Desktop 3.0; the archive is at 4.0.8 (built 2026-10-16, LXQt/Minimal, with a UEFI variant)"
M["SpacemiT archive 提供 ubuntu-26.04-preinstalled-desktop-riscv64 镜像；官网规格页列 Ubuntu 26.04"] = \
    "The SpacemiT archive provides an ubuntu-26.04-preinstalled-desktop-riscv64 image; the spec page lists Ubuntu 26.04"
M["Debian 13 GNOME/XFCE/Minimal 镜像（2026-07-30 构建）"] = \
    "Debian 13 GNOME/XFCE/Minimal images (built 2026-07-30)"
M["官方 SDK 提供 buildroot 配置与镜像"] = "The official SDK provides Buildroot configs and images"
M["官网规格页称支持 OpenKylin，未见公开镜像下载"] = \
    "The spec page says OpenKylin is supported, but no public image download was found"
M["官网规格页称支持 Deepin，未见公开镜像下载"] = \
    "The spec page says deepin is supported, but no public image download was found"
M["官网规格页称支持 Fedora，未见 K3 专用官方镜像"] = \
    "The spec page says Fedora is supported, but there is no K3-specific official image"
M["a210-evb 桌面 Debian 预编译镜像（SDK v2.9.0）"] = \
    "Prebuilt a210-evb desktop Debian image (SDK v2.9.0)"
M["zhihe_a210_defconfig，官方 Buildroot SDK"] = "zhihe_a210_defconfig in the official Buildroot SDK"
M["k230_linux_sdk 默认 Buildroot 方案（k230_canmv/k230_evb defconfig）"] = \
    "k230_linux_sdk's default Buildroot setup (k230_canmv/k230_evb defconfigs)"
M["SDK 支持 make debian，官方有《K230 Debian/Ubuntu 系统指南》"] = \
    "The SDK supports make debian, and there is an official K230 Debian/Ubuntu guide"
M["SDK 支持 make ubuntu，同上指南"] = "The SDK supports make ubuntu, same guide"
M["RockOS（PLCT 维护的 Debian 优化版，面向 EIC77 系列）"] = \
    "RockOS (a PLCT-maintained tuned Debian for the EIC77 family)"
M["Fedora 41 镜像由 Fedora-V Force（FVF）构建，非 Fedora 官方镜像"] = \
    "The Fedora 41 image is built by Fedora-V Force (FVF), not an official Fedora image"
M["Gentoo wiki 有 Megrez 安装页（社区维护）"] = \
    "The Gentoo wiki has a Megrez install page (community-maintained)"
M["UltraRISC 官方 Ubuntu 24.04 Desktop（rvck-titan，2026-06-05 构建）"] = \
    "UltraRISC's official Ubuntu 24.04 Desktop (rvck-titan, built 2026-06-05)"
M["Fedora 44 Server Omni（Fedora RISC-V 官方镜像，配 GRUB/DTB 步骤）"] = \
    "Fedora 44 Server Omni (official Fedora RISC-V image, with GRUB/DTB steps)"
M["openKylin 2.0 SP2（ultrarisc-titan，2026-06-22 构建）"] = \
    "openKylin 2.0 SP2 (ultrarisc-titan, built 2026-06-22)"
M["Canonical 官方 preinstalled 镜像 ubuntu-24.04.5-...+unmatched.img.xz，仍在 24.04 LTS 支持范围内"] = \
    "Canonical's official preinstalled ubuntu-24.04.5-...+unmatched.img.xz, still within 24.04 LTS support"
M["SiFive Freedom U SDK（FUSDK，Buildroot/Yocto 混合）是厂商参考系统，含 U-Boot/OpenSBI"] = \
    "The SiFive Freedom U SDK (FUSDK, a Buildroot/Yocto hybrid) is the vendor reference system, including U-Boot/OpenSBI"
M["Debian 官方 riscv64 安装器可用，Debian wiki 有该板专页"] = \
    "Debian's official riscv64 installer works, and the Debian wiki has a page for this board"
M["Fedora RISC-V 长期把 Unmatched 列为参考板"] = \
    "Fedora RISC-V has long listed Unmatched as a reference board"
M["openSUSE Ports 提供 riscv64；官网 403，未验证该板镜像"] = \
    "openSUSE Ports has riscv64; the site returns 403, so this board's image is unverified"
M["FreeBSD/riscv 支持 Unmatched"] = "FreeBSD/riscv supports Unmatched"
M["OpenBSD/riscv64 社区报告可用"] = "Community reports say OpenBSD/riscv64 works"
M["Gentoo RISC-V 项目覆盖 U74 平台"] = "The Gentoo RISC-V project covers U74 platforms"
M["曾有社区镜像，Armbian 官网现已下架该板页面"] = \
    "Community images existed, but Armbian has since removed this board's page"
M["openEuler RISC-V SIG 有面向该板的镜像"] = "The openEuler RISC-V SIG has an image for this board"
M["openKylin RISC-V 版本曾支持"] = "An openKylin RISC-V release supported it in the past"
M["deepin RISC-V 移植版可用"] = "The deepin RISC-V port works"
M["官方主推 Bianbu（SpacemiT K1 镜像，v1.0.7 起支持 16GB）"] = \
    "Bianbu is the vendor's pick (SpacemiT K1 image; 16GB supported since v1.0.7)"
M["Armbian 标准支持，提供 Debian/Ubuntu 镜像（仅 SD 启动）"] = \
    "Armbian Standard support with Debian/Ubuntu images (SD boot only)"
M["经 Armbian 提供"] = "Provided via Armbian"
M["经 Armbian 提供（非 Canonical 官方）"] = "Provided via Armbian (not Canonical official)"
M["Banana Pi 文档页挂出的第三方镜像"] = "A third-party image linked from the Banana Pi docs"
M["同上，第三方镜像"] = "As above, a third-party image"
M["Ubuntu 24.04 Server/GNOME（厂商 6.6 内核，orangepi-build 可自编）"] = \
    "Ubuntu 24.04 Server/GNOME (vendor 6.6 kernel, buildable with orangepi-build)"
M["Armbian 提供 Debian/Ubuntu 构建"] = "Armbian provides Debian/Ubuntu builds"
M["BredOS（Arch 衍生）在官网列为第三方镜像"] = \
    "BredOS (an Arch derivative) is listed as a third-party image on the site"
M["Ubuntu 24.04 预装，SiFive 发布 2025.11.00（内核 6.12.33）"] = \
    "Ubuntu 24.04 preinstalled; SiFive released 2025.11.00 (kernel 6.12.33)"
M["Fedora 42 起支持，Fedora 44 起走 Omni 内核"] = "Supported since Fedora 42; Omni kernel since Fedora 44"
M["freedom-u-sdk Yocto BSP（含 bootchain 固件）"] = \
    "freedom-u-sdk Yocto BSP (including bootchain firmware)"
M["SiFive 博客称已推进 Debian 支持，需自行准备镜像"] = \
    "A SiFive blog says Debian support is in progress; prepare the image yourself"
M["StarFive Debian 镜像（debian.starfivetech.com）"] = "StarFive Debian image (debian.starfivetech.com)"
M["ubuntu-24.04.3-preinstalled-desktop-riscv64+vf2-lite 镜像（StarFive 发布，2025-10-16）"] = \
    "ubuntu-24.04.3-preinstalled-desktop-riscv64+vf2-lite (released by StarFive, 2025-10-16)"
M["StarFive Buildroot SDK（VisionFive2 仓库）"] = "StarFive Buildroot SDK (VisionFive2 repo)"
M["官方唯一 Linux 桌面镜像 xuantie-ubuntu-23.04-20230705（Ubuntu 23.04 已 EOL）"] = \
    "The only official Linux desktop image, xuantie-ubuntu-23.04-20230705 (Ubuntu 23.04 is EOL)"
M["官方 Yocto 生产镜像 2023-06-10，出厂预装"] = \
    "Official Yocto production image 2023-06-10, preinstalled at the factory"
M["RevyOS 的 beagle 目录停在 20231210，之后没再更新"] = \
    "RevyOS's beagle directory stops at 20231210 with no updates since"
M["Fedora-V Force 提供 BeagleV Ahead 镜像"] = "Fedora-V Force provides BeagleV-Ahead images"
M["主线 Debian 没有官方安装器支持，只能自建 rootfs"] = \
    "Mainline Debian has no official installer support; build the rootfs yourself"
M["当前官方主推，RevyOS 20260504 提供 pioneer/pisces 两套固件与镜像"] = \
    "Currently the vendor's recommended system; RevyOS 20260504 ships pioneer/pisces firmware and images"
M["Milk-V 官方文档以 Fedora 38 为安装示例，Fedora RISC-V 支持 SG2042"] = \
    "Milk-V's docs use Fedora 38 as the install example; Fedora RISC-V supports SG2042"
M["openEuler RISC-V SIG 面向服务器场景支持 SG2042"] = \
    "The openEuler RISC-V SIG supports SG2042 for server scenarios"
M["openKylin 有 RISC-V 服务器镜像"] = "openKylin has a RISC-V server image"
M["debian-ports 有 riscv64 基础包，但没有官方 Pioneer 镜像"] = \
    "debian-ports has base riscv64 packages but no official Pioneer image"
M["无 Canonical 官方镜像，需自行搭 rootfs"] = "No Canonical image; build the rootfs yourself"
M["官方 V1/V2 Buildroot SDK，烧卡即用，是最稳的系统"] = \
    "Official V1/V2 Buildroot SDKs — flash and go, the steadiest system"
M["Fedora 41 镜像（Fedora-V Force，ISCAS 镜像站）"] = "Fedora 41 image (Fedora-V Force, ISCAS mirror)"
M["Fishwaldo/scpcom 的 sophgo-sg200x-debian，覆盖 256M/S"] = \
    "Fishwaldo/scpcom's sophgo-sg200x-debian, covering 256M/S"
M["Ubuntu 22.04 社区镜像（bassusteur）"] = "Ubuntu 22.04 community image (bassusteur)"
M["社区 Arch 镜像"] = "Community Arch image"
M["社区 Alpine 镜像（cwt）"] = "Community Alpine image (cwt)"
M["社区维护，功能有限"] = "Community-maintained with limited features"
M["meta-milkv 层"] = "meta-milkv layer"
M["openEuler 有 Duo 镜像"] = "openEuler has a Duo image"

# ---- downloads[].label ----
M["QEMU 官方文档：RISC-V virt 机型"] = "QEMU docs: the RISC-V virt machine"
M["QEMU 下载页"] = "QEMU download page"
M["Ubuntu 24.04 riscv64 cloud image"] = "Ubuntu 24.04 riscv64 cloud image"
M["Debian 13.7 riscv64 netinst ISO"] = "Debian 13.7 riscv64 netinst ISO"
M["Arch Linux RISC-V ISO"] = "Arch Linux RISC-V ISO"
M["Alpine riscv64 minirootfs"] = "Alpine riscv64 minirootfs"
M["Buildroot 下载"] = "Buildroot downloads"
M["StarFive 官方 Debian 202510（v0.15.0）"] = "StarFive's official Debian 202510 (v0.15.0)"
M["StarFive 官方 Ubuntu 24.04.3（202510）"] = "StarFive's official Ubuntu 24.04.3 (202510)"
M["Canonical Ubuntu jh7110 预装镜像（VF2/Mars/Star64 通用）"] = \
    "Canonical Ubuntu jh7110 preinstalled image (shared by VF2/Mars/Star64)"
M["StarFive VisionFive2 SDK / 固件"] = "StarFive VisionFive2 SDK / firmware"
M["Debian wiki: 在 VisionFive 2 上安装 Debian"] = "Debian wiki: installing Debian on VisionFive 2"
M["Armbian VisionFive 2"] = "Armbian VisionFive 2"
M["Arch Linux RISC-V 镜像目录"] = "Arch Linux RISC-V image directory"
M["RVspace 论坛：Debian 202510 发布贴（含兼容性反馈）"] = \
    "RVspace forum: Debian 202510 release thread (with compatibility feedback)"
M["RevyOS LicheePi 4A 镜像（20251226）"] = "RevyOS LicheePi 4A image (20251226)"
M["RevyOS 刷机总览（含 U-Boot env 重置说明）"] = \
    "RevyOS flashing overview (including the U-Boot env reset)"
M["Sipeed Wiki 镜像集合（英文）"] = "Sipeed Wiki image collection (English)"
M["Sipeed Wiki 镜像集合（中文，信息最全）"] = \
    "Sipeed Wiki image collection (Chinese, the most complete)"
M["Sipeed 官方下载盘（规格/原理图/工具）"] = "Sipeed download share (specs/schematics/tools)"
M["Armbian LicheePi 4A"] = "Armbian LicheePi 4A"
M["NixOS on LicheePi 4A（社区）"] = "NixOS on LicheePi 4A (community)"
M["Fedora RISC-V builder（chainsx）"] = "Fedora RISC-V builder (chainsx)"
M["Gentoo TH1520 部署指南"] = "Gentoo TH1520 deployment guide"
M["deepin RISC-V 镜像"] = "deepin RISC-V image"
M["openKylin LPi4A 镜像（社区）"] = "openKylin LPi4A image (community)"
M["RevyOS Meles 镜像（20251226）"] = "RevyOS Meles image (20251226)"
M["Milk-V 官方镜像页（指向 RevyOS）"] = "Milk-V image page (points to RevyOS)"
M["刷写到 eMMC（fastboot 步骤）"] = "Flashing to eMMC (fastboot steps)"
M["安装总览（SD/SPI/eMMC 三种方式）"] = "Install overview (SD/SPI/eMMC)"
M["RevyOS 文档站"] = "RevyOS documentation site"
M["openEuler RISC-V SIG"] = "openEuler RISC-V SIG"
M["Bianbu K3 镜像（含 4.0.8）"] = "Bianbu K3 images (including 4.0.8)"
M["Debian 13 K3 镜像"] = "Debian 13 K3 image"
M["Ubuntu 26.04 K3 镜像"] = "Ubuntu 26.04 K3 image"
M["Buildroot K3 镜像"] = "Buildroot K3 image"
M["A210 Debian 桌面镜像（v2.9.0）"] = "A210 Debian desktop image (v2.9.0)"
M["A210 Buildroot 镜像（v2.9.0）"] = "A210 Buildroot image (v2.9.0)"
M["K230 Linux SDK 每日构建镜像"] = "K230 Linux SDK daily build images"
M["CanMV（MicroPython）固件 Releases"] = "CanMV (MicroPython) firmware releases"
M["K230 Linux SDK 源码"] = "K230 Linux SDK source"
M["RockOS/Debian 镜像与 bootloader（megrez-build releases）"] = \
    "RockOS/Debian images and bootloader (megrez-build releases)"
M["Fedora 41（FVF）Megrez 镜像"] = "Fedora 41 (FVF) Megrez image"
M["Ubuntu 24.04（UltraRISC 官方，分卷 7z）"] = "Ubuntu 24.04 (UltraRISC official, split 7z)"
M["Fedora 44 RISC-V 镜像目录"] = "Fedora 44 RISC-V image directory"
M["openKylin 2.0 SP2 for Titan"] = "openKylin 2.0 SP2 for Titan"
M["Ubuntu 24.04.5 LTS（Unmatched 预装镜像）"] = "Ubuntu 24.04.5 LTS (Unmatched preinstalled image)"
M["SiFive Freedom U SDK（源码）"] = "SiFive Freedom U SDK (source)"
M["Debian wiki: 在 Unmatched 上安装 Debian"] = "Debian wiki: installing Debian on Unmatched"
M["Fedora RISC-V 安装指南"] = "Fedora RISC-V installation guide"
M["FreeBSD RISC-V 说明"] = "FreeBSD RISC-V notes"
M["OpenBSD/riscv64"] = "OpenBSD/riscv64"
M["BPI-F3 全量镜像页（Bianbu/Debian/Ubuntu/Fedora/openSUSE/Arch/Gentoo/Armbian）"] = \
    "BPI-F3 full image page (Bianbu/Debian/Ubuntu/Fedora/openSUSE/Arch/Gentoo/Armbian)"
M["SpacemiT K1 Bianbu 官方镜像仓库"] = "SpacemiT K1 Bianbu official image repository"
M["Armbian for BPI-F3"] = "Armbian for BPI-F3"
M["RV2 官方镜像下载页（Ubuntu/Orange Pi OS/OpenWRT，Google Drive）"] = \
    "RV2 official image page (Ubuntu/Orange Pi OS/OpenWRT, Google Drive)"
M["Armbian for Orange Pi RV2"] = "Armbian for Orange Pi RV2"
M["Ubuntu 镜像 Releases（SiFive 官方）"] = "Ubuntu image releases (SiFive official)"
M["freedom-u-sdk（Yocto/BSP 与 bootchain）"] = "freedom-u-sdk (Yocto/BSP and bootchain)"
M["StarFive Debian 镜像入口"] = "StarFive Debian image entry"
M["VisionFive2 仓库 Releases（Ubuntu/Debian/Buildroot 镜像与 SDK）"] = \
    "VisionFive2 repo releases (Ubuntu/Debian/Buildroot images and SDK)"
M["BeagleBoard 官方镜像站（全部板型）"] = "BeagleBoard image site (all board models)"
M["官方 Ubuntu 23.04（2023-07-05）"] = "Official Ubuntu 23.04 (2023-07-05)"
M["官方 Yocto（2023-06-10，出厂镜像）"] = "Official Yocto (2023-06-10, factory image)"
M["RevyOS BeagleV-Ahead 镜像（20231210）"] = "RevyOS BeagleV-Ahead image (20231210)"
M["Xuantie Ubuntu 源码仓库（2023-07-05 release）"] = \
    "XuanTie Ubuntu source repo (2023-07-05 release)"
M["Fedora-V Force RISC-V 镜像站"] = "Fedora-V Force RISC-V mirror"
M["硬件设计与 issue tracker"] = "Hardware design and issue tracker"
M["RevyOS SG2042 镜像目录（20260504）"] = "RevyOS SG2042 image directory (20260504)"
M["RevyOS 官方安装指南（Milk-V Pioneer）"] = "RevyOS install guide (Milk-V Pioneer)"
M["Milk-V Pioneer 安装步骤（英文，含 Fedora 示例）"] = \
    "Milk-V Pioneer install steps (English, with a Fedora example)"
M["Milk-V Pioneer 下载汇总（硬件/源码）"] = "Milk-V Pioneer download roundup (hardware/source)"
M["Milk-V 官方镜像汇总（含第三方镜像表）"] = \
    "Milk-V image roundup (including a third-party image table)"
M["官方 Buildroot SDK V1 releases"] = "Official Buildroot SDK V1 releases"
M["官方 Buildroot SDK V2 releases（256M/S 的 RISC-V+ARM 双镜像）"] = \
    "Official Buildroot SDK V2 releases (RISC-V+ARM dual images for 256M/S)"
M["Fedora 41 Duo 镜像（ISCAS）"] = "Fedora 41 Duo image (ISCAS)"
M["Debian（sophgo-sg200x-debian）"] = "Debian (sophgo-sg200x-debian)"
M["Alpine 社区镜像（PoC）"] = "Alpine community image (PoC)"

# ---- guides[].label ----
M["QEMU wiki: RISC-V 平台说明"] = "QEMU wiki: RISC-V platform notes"
M["Debian wiki: RISC-V 端口"] = "Debian wiki: RISC-V port"
M["Fedora: RISC-V 安装指南"] = "Fedora: RISC-V installation guide"
M["Gentoo RISC-V 项目"] = "Gentoo RISC-V project"
M["openEuler RISC-V SIG"] = "openEuler RISC-V SIG"
M["StarFive VisionFive2 SDK 文档（README，含固件烧写/恢复）"] = \
    "StarFive VisionFive2 SDK docs (README, including firmware flashing/recovery)"
M["Debian wiki 安装指南"] = "Debian wiki install guide"
M["Gentoo wiki: StarFive VisionFive 2"] = "Gentoo wiki: StarFive VisionFive 2"
M["RVspace 官方社区（中英文）"] = "RVspace community (Chinese and English)"
M["Fedora RISC-V 安装指南"] = "Fedora RISC-V installation guide"
M["Sipeed Wiki 板卡介绍（英文）"] = "Sipeed Wiki board overview (English)"
M["Sipeed Wiki 板卡介绍（中文）"] = "Sipeed Wiki board overview (Chinese)"
M["RevyOS 文档站"] = "RevyOS documentation site"
M["RuyiSDK 支持矩阵（各发行版实测状态）"] = \
    "RuyiSDK support matrix (measured status per distro)"
M["Meles 概览与规格（英文）"] = "Meles overview and specs (English)"
M["Meles 硬件说明（版本/供电/接口）"] = "Meles hardware notes (versions/power/interfaces)"
M["Meles 概览与规格（中文）"] = "Meles overview and specs (Chinese)"
M["Meles 安装说明（中文）"] = "Meles installation notes (Chinese)"
M["K3 Pico-ITX 官方产品页（规格含 OS 列表）"] = \
    "K3 Pico-ITX product page (specs including the OS list)"
M["K3-CoM260 官方产品页"] = "K3-CoM260 product page"
M["SpacemiT K3 芯片文档入口"] = "SpacemiT K3 chip documentation entry"
M["Banana Pi K3 Pico-ITX 规格与上手（英文）"] = \
    "Banana Pi K3 Pico-ITX specs and getting started (English)"
M["K3 参考设计与 SDK 发布计划（官方论坛）"] = \
    "K3 reference design and SDK release plan (official forum)"
M["Banana Pi K3 公售公告（2026-05）"] = "Banana Pi K3 public sales announcement (2026-05)"
M["TinyComputers K3 Pico-ITX 深度评测（含坑）"] = \
    "TinyComputers in-depth K3 Pico-ITX review (including pitfalls)"
M["A210 产品规格书（中文）"] = "A210 product brief (Chinese)"
M["A210 产品规格书（英文）"] = "A210 product brief (English)"
M["SDK 快速上手（镜像/编译/烧录）"] = "SDK quick start (images/build/flash)"
M["A210 镜像烧录指南（SODIMM V1/V2/V3、算力棒）"] = \
    "A210 flashing guide (SODIMM V1/V2/V3, compute dongle)"
M["CanMV-K230 快速入门（中文）"] = "CanMV-K230 quick start (Chinese)"
M["K230 Linux SDK 文档（中文）"] = "K230 Linux SDK docs (Chinese)"
M["K230 Debian/Ubuntu 系统指南"] = "K230 Debian/Ubuntu system guide"
M["NuttX CanMV-K230 板级文档（英文）"] = "NuttX CanMV-K230 board docs (English)"
M["Megrez 概览与规格（中文）"] = "Megrez overview and specs (Chinese)"
M["Megrez 安装系统/启动说明（分区扩容等）"] = \
    "Megrez install/boot notes (partition resizing and more)"
M["ENNP SDK 开发指南（NPU）"] = "ENNP SDK developer guide (NPU)"
M["Gentoo on Megrez（社区）"] = "Gentoo on Megrez (community)"
M["Titan 概览与规格（中文）"] = "Titan overview and specs (Chinese)"
M["Titan 安装 Ubuntu 24.04（写盘+启动）"] = "Installing Ubuntu 24.04 on Titan (imaging + boot)"
M["Fedora on Milk-V Titan（官方 Wiki）"] = "Fedora on Milk-V Titan (official wiki)"
M["SiFive 官方产品页（含规格与 Discontinued 标记）"] = \
    "SiFive product page (specs plus the Discontinued marker)"
M["SiFive 文档中心"] = "SiFive documentation centre"
M["Ubuntu 官方安装指南（HiFive Unmatched）"] = "Ubuntu install guide (HiFive Unmatched)"
M["BPI-F3 文档（英文，规格/镜像/烧录）"] = "BPI-F3 docs (English, specs/images/flashing)"
M["BPI-F3 文档（中文）"] = "BPI-F3 docs (Chinese)"
M["BPI-F3 上手（SD/eMMC 烧录）"] = "BPI-F3 getting started (SD/eMMC flashing)"
M["Banana Pi RISC-V 论坛 BPI-F3 版块"] = "Banana Pi RISC-V forum, BPI-F3 section"
M["Orange Pi RV2 Wiki（英文，含烧录/GPIO/内核）"] = \
    "Orange Pi RV2 Wiki (English, with flashing/GPIO/kernel)"
M["RV2 中文产品页"] = "RV2 Chinese product page"
M["orangepi-build（内核/镜像构建）"] = "orangepi-build (kernel/image build)"
M["P550 官方产品页（规格/购买链接）"] = "P550 product page (specs/purchase links)"
M["Fedora on P550（固件要求/串口/安装）"] = \
    "Fedora on P550 (firmware requirements/serial/install)"
M["VisionFive 2 Lite 产品与规格（英文）"] = "VisionFive 2 Lite product and specs (English)"
M["VisionFive 2 Lite 文档中心（英文）"] = "VisionFive 2 Lite documentation centre (English)"
M["VisionFive 2 Lite 文档中心（中文）"] = "VisionFive 2 Lite documentation centre (Chinese)"
M["RVspace 中文 Wiki"] = "RVspace Chinese wiki"
M["BeagleBoard 官方文档：BeagleV-Ahead"] = "BeagleBoard docs: BeagleV-Ahead"
M["产品页（规格/购买渠道）"] = "Product page (specs/purchase channels)"
M["OpenBeagle 项目主页"] = "OpenBeagle project home"
M["官方论坛 BeagleV-Ahead 分区"] = "Official forum, BeagleV-Ahead section"
M["Pioneer 概览与规格（英文）"] = "Pioneer overview and specs (English)"
M["Pioneer 概览与规格（中文）"] = "Pioneer overview and specs (Chinese)"
M["Pioneer 已知问题列表"] = "Pioneer known-issues list"
M["RevyOS 文档站（镜像/刷写）"] = "RevyOS docs (images/flashing)"
M["Duo 概览（英文）"] = "Duo overview (English)"
M["Duo 快速上手"] = "Duo quick start"
M["Duo 256M 说明"] = "Duo 256M notes"
M["Buildroot SDK 构建指南"] = "Buildroot SDK build guide"
M["上游主线支持状态（逐项 patch 进度）"] = "Mainline support status (patch-by-patch progress)"
M["主线 Linux 支持说明"] = "Mainline Linux support notes"

# ---- gotchas ----
M["-bios default 只加载 OpenSBI，没有 U-Boot/EDK2；启动 Ubuntu/Fedora cloud image 需用 pflash 加载 32MiB EDK2 固件，否则黑屏"] = \
    "-bios default only loads OpenSBI, with no U-Boot/EDK2; booting an Ubuntu/Fedora cloud image needs pflash with a 32MiB EDK2 firmware, otherwise you get a black screen"
M["virt 没有 GPU/VPU/NPU，别用它验证图形、视频硬解或 AI 加速"] = \
    "virt has no GPU/VPU/NPU — don't use it to validate graphics, hardware video decoding or AI acceleration"
M["串口固定是 ttyS0；-nographic 模式退出要按 Ctrl-A 再按 X"] = \
    "The serial port is always ttyS0; to quit -nographic mode press Ctrl-A then X"
M["Ubuntu 26.04 起要求 RVA23S64，旧版 QEMU 缺扩展会起不来；24.04 仍是 RVA20 基线"] = \
    "From Ubuntu 26.04 RVA23S64 is required, so older QEMU builds without the extensions won't boot; 24.04 is still RVA20"
M["Alpine riscv64 只发 minirootfs，没有 virt ISO，需要自己准备内核和 initramfs"] = \
    "Alpine riscv64 ships only a minirootfs with no virt ISO, so prepare the kernel and initramfs yourself"
M["U-Boot/SPL 在 QSPI Flash 里，镜像与固件强绑定：202310 之后的镜像要求 QSPI 内 U-Boot ≥ v3.1.5，否则要先刷 u-boot-spl.bin.normal.out + visionfive2_fw_payload.img"] = \
    "U-Boot/SPL lives in QSPI flash and images are tightly bound to firmware: images after 202310 need U-Boot >= v3.1.5 in QSPI, otherwise flash u-boot-spl.bin.normal.out + visionfive2_fw_payload.img first"
M["启动顺序是 QSPI → SD/eMMC/NVMe，DIP 开关拨错会从错误介质启动"] = \
    "Boot order is QSPI → SD/eMMC/NVMe; a wrong DIP switch boots from the wrong medium"
M["v1.2 老板子刷 Debian 202510 有失败报告，建议先升级固件或改用主线 Debian"] = \
    "There are failure reports for Debian 202510 on older v1.2 boards; upgrade the firmware first or use mainline Debian"
M["StarFive 官方 Debian 202510 不支持 USB 启动；主线 Debian 13 能从 USB 启动但没有 HDMI/GPU/VPU 驱动"] = \
    "StarFive's official Debian 202510 can't boot from USB; mainline Debian 13 can, but without HDMI/GPU/VPU drivers"
M["VisionFive 2 Lite 与标准版 U-Boot/DTB 不同，镜像不能混用"] = \
    "VisionFive 2 Lite uses different U-Boot/DTB from the standard board — images are not interchangeable"
M["eMMC/SD 启动有已知 errata，优先 NVMe 或高质量 SD 卡"] = \
    "eMMC/SD boot has known errata; prefer NVMe or a good SD card"
M["GPU 是 Imagination BXM-4-64，只有厂商闭源 blob，主线内核下没有 GPU 加速；NPU 需要 T-Head 专用 SDK"] = \
    "The GPU is an Imagination BXM-4-64 with a vendor closed-source blob only, so there is no GPU acceleration under mainline; the NPU needs the T-Head-specific SDK"
M["2023.8.1 之前出货的 16GB 批次 U-Boot 识别内存有 bug，必须刷 16G 专用 u-boot，否则大内存应用会崩"] = \
    "16GB boards shipped before 2023.8.1 have a U-Boot memory-detection bug; flash the 16G-specific u-boot or memory-hungry apps crash"
M["刷机要按住 BOOT 键再上电进 fastboot（USB 2345:7654），普通上电进不了下载模式"] = \
    "To flash, hold BOOT while powering on to enter fastboot (USB 2345:7654); a normal power-up won't enter download mode"
M["从 ≤20240720 的 RevyOS 升级，必须先 `env default -a -f; env save` 重置 U-Boot 环境变量"] = \
    "Upgrading from RevyOS <= 20240720 requires `env default -a -f; env save` to reset the U-Boot environment first"
M["8GB 与 16GB 版本的 boot.ext4 设备树不同，混刷会起不来"] = \
    "The 8GB and 16GB versions use different device trees in boot.ext4; mixing them means no boot"
M["2026-09 起 RevyOS 在推 coreboot+EDK2 新固件（取代 U-Boot SPL），属于实验性质，刷前确认板型"] = \
    "Since 2026-09 RevyOS has been pushing new coreboot+EDK2 firmware (replacing U-Boot SPL); it is experimental — confirm your board variant before flashing"
M["4GB 版与 8GB/16GB 版的 U-Boot SPL 不同（u-boot-with-spl-meles-4g.bin vs meles.bin），刷错直接变砖"] = \
    "The 4GB and 8GB/16GB boards need different U-Boot SPL files (u-boot-with-spl-meles-4g.bin vs meles.bin); the wrong one bricks the board"
M["20251226 起改用 kernel 6.6，刷系统前必须先升级 SPI Flash 里的固件"] = \
    "From 20251226 it uses kernel 6.6, so upgrade the firmware in SPI flash before flashing the system"
M["eMMC 是选配模块；要从 eMMC 启动必须先刷好 SPI NOR，否则只能从 SD 启动"] = \
    "eMMC is an optional module; booting from it requires SPI NOR to be flashed first, otherwise you can only boot from SD"
M["刷 eMMC 走 fastboot（T-HEAD USB download gadget 2345:7654），要按 Download 键进下载模式"] = \
    "Flashing eMMC goes through fastboot (T-HEAD USB download gadget 2345:7654), and you must hold the Download button to enter download mode"
M["板子有 V1.x 多个硬件版本（丝印在正面），DTB/镜像要对应"] = \
    "The board has several V1.x hardware revisions (marked on the front silkscreen) that need matching DTBs/images"
M["PoE 供电要自己往排针 PIN2/PIN4 喂 5V，不是标准 802.3af 受电"] = \
    "PoE power means feeding 5V into header PIN2/PIN4 yourself; it is not standard 802.3af powered-device input"
M["出厂 Bianbu 4.0.4 用厂商内核 6.18.3-generic，非 mainline；K3 参考设计与 SDK 自 2026-05 起分批释放，文档与硬件验证同步推进"] = \
    "The factory Bianbu 4.0.4 uses vendor kernel 6.18.3-generic, not mainline; K3 reference designs and SDKs have been released in batches since 2026-05, with docs and hardware validation moving together"
M["16 核枚举但单任务最多调度 8 核，KVM/虚拟机实测不可用（TinyComputers 2026-09 评测）"] = \
    "16 cores are enumerated but a single task schedules on at most 8, and KVM/VMs did not work in testing (TinyComputers review, 2026-09)"
M["评测中万兆 SFP+ 未 link，仅千兆口可用；10GbE 驱动/光模块兼容需实测"] = \
    "In the review the 10GbE SFP+ never linked and only the GbE port worked; 10GbE driver/transceiver compatibility needs testing"
M["渠道价差极大且需自付关税；Milk-V Jupiter2 文档目前仍是 stub，主要靠 SpacemiT 官方文档"] = \
    "Reseller prices vary wildly and duty is extra; the Milk-V Jupiter2 docs are still a stub, so rely on SpacemiT's official docs"
M["无零售渠道与公开报价，开发板以评估/合作渠道为主，普通开发者难买到"] = \
    "No retail channel or public price; boards go mainly through evaluation/partner channels, so ordinary developers struggle to buy one"
M["A210 与 A200 镜像不通用：官方 Ubuntu 只给 A200，A210 只有 Debian/Buildroot"] = \
    "A210 and A200 images are not interchangeable: the official Ubuntu only covers A200, while A210 has Debian/Buildroot only"
M["GitHub/Gitee 无官方 BSP 仓库（检索 0 结果），内核与驱动以厂商 SDK 包形式发布，社区几乎无第三方发行版支持"] = \
    "There is no official BSP repo on GitHub/Gitee (zero search results); the kernel and drivers ship inside vendor SDK packages, and the community has almost no third-party distro support"
M["厂商数据：单芯片 DeepSeek-7B 约 8 tok/s，4 die 级联 25 tok/s，实际以自测为准"] = \
    "Vendor figures: about 8 tok/s for DeepSeek-7B on a single chip and 25 tok/s with 4 dies cascaded; measure it yourself"
M["AMP 异构：默认小核跑 Linux、大核跑 RT-Smart/CanMV；只有大核带 V 扩展，向量负载必须放对核"] = \
    "AMP heterogeneous design: by default the little core runs Linux and the big core RT-Smart/CanMV; only the big core has the V extension, so vector workloads must land on the right core"
M["官方 Linux 主线是 Buildroot；Debian/Ubuntu 要自己 make debian / make ubuntu 构建，无现成官方桌面镜像"] = \
    "The official Linux path is Buildroot; Debian/Ubuntu must be built with make debian / make ubuntu, and there are no ready official desktop images"
M["固件必须匹配：CanMV IDE 只认文件名以 CanMV-K230_micropython 开头的固件，刷 K230 SDK 镜像连不上"] = \
    "Firmware must match: CanMV IDE only accepts files named CanMV-K230_micropython*, and a K230 SDK image won't connect"
M["nncase 工具链闭源且与固件版本强绑定；早期构建文档只有中文"] = \
    "The nncase toolchain is closed source and tightly bound to firmware versions; early build docs are Chinese only"
M["出厂 CPU 默认 1.4GHz/800mV，需按文档手动调频才能到 1.8GHz，否则性能低于宣传"] = \
    "The CPU ships at 1.4GHz/800mV; you must raise it to 1.8GHz by hand per the docs or performance falls short of the marketing"
M["首次启动不自动扩分区，根分区仅 6GB，必须用 gparted 手动扩容，否则很快写满/重启进不了桌面"] = \
    "First boot does not grow the partition and root is only 6GB; expand it with gparted or it fills up quickly and reboots into no desktop"
M["Fedora 镜像来自 Fedora-V Force（F41），不是 Fedora 官方构建；无 Ubuntu 官方镜像"] = \
    "The Fedora image comes from Fedora-V Force (F41), not an official Fedora build; there is no official Ubuntu image"
M["无公开零售渠道（官网只剩 Contact us），2026 年实际较难买到"] = \
    "No public retail channel (the site only offers Contact us), so in 2026 it is genuinely hard to buy"
M["UR-DP1000 没有 V（向量）扩展，严格说达不到 RVA23，AI/向量负载性能吃亏"] = \
    "UR-DP1000 has no V (vector) extension, so strictly it misses RVA23, which hurts AI/vector workloads"
M["主板无 HDMI/显示输出，必须独显或纯串口/SSH 使用"] = \
    "The board has no HDMI/display output; use a discrete GPU or work purely over serial/SSH"
M["当前为厂商内核，官方称 2026 Q4 才计划上游 Linux mainline"] = \
    "It currently runs a vendor kernel; upstream Linux mainline is only planned for 2026 Q4"
M["DDR4 UDIMM 需按官方支持列表选型；预购交付周期长（曾有 45 天+），且需自付关税"] = \
    "Pick DDR4 UDIMMs from the official support list; pre-order lead times are long (45 days+ at times) and duty is extra"
M["没有板载显示输出，必须插 PCIe 显卡或用串口；调试必须接 USB-UART(FTDI) 才能看到 OpenSBI/U-Boot 日志"] = \
    "No onboard display output — add a PCIe GPU or use serial; debugging needs a USB-UART (FTDI) to see OpenSBI/U-Boot logs"
M["12V/6A 桶形电源，供电不足会随机重启或 DDR 训练失败"] = \
    "It needs a 12V/6A barrel supply; under-powering causes random reboots or DDR training failures"
M["启动介质由 MSEL 拨码决定（SD/SPI Flash），拨错直接不启动；SPI 固件损坏要靠 JTAG 恢复"] = \
    "The boot medium is set by the MSEL switches (SD/SPI flash); the wrong setting means no boot, and a corrupted SPI firmware needs JTAG recovery"
M["官方已停产，Ubuntu 24.04 是最后一个受支持的 LTS 镜像，内核偏旧，新发行版基本不再出该板镜像"] = \
    "Officially discontinued: Ubuntu 24.04 is the last supported LTS image, the kernel is old, and new distros largely skip this board"
M["PCIe 显卡需外接供电，部分卡在 U-Boot 阶段没有输出，要等 Linux 起来才亮"] = \
    "PCIe GPUs need external power, and some cards show nothing during U-Boot — they only light up once Linux starts"
M["Bianbu 镜像分 SD 卡版（*.img.zip）与 eMMC 版（*.zip），刷错无法启动"] = \
    "Bianbu images come in SD (*.img.zip) and eMMC (*.zip) variants; the wrong one won't boot"
M["官方只主推 Bianbu；Debian/Ubuntu 主要靠 Armbian 社区镜像，且 Armbian 仅支持 SD 启动"] = \
    "The vendor pushes Bianbu only; Debian/Ubuntu come mainly from Armbian community images, and Armbian supports SD boot only"
M["早期 Bianbu（<v1.0.7）不支持 16GB 内存版本"] = "Early Bianbu (<v1.0.7) does not support the 16GB memory version"
M["HDMI 仅 1.4/1080p，不适合 4K 桌面"] = "HDMI is 1.4/1080p only — not suitable for a 4K desktop"
M["Ubuntu 24.04 是厂商 6.6 内核（orange-pi-6.6-ky），不是 mainline，升级内核需谨慎"] = \
    "Ubuntu 24.04 uses the vendor 6.6 kernel (orange-pi-6.6-ky), not mainline; upgrade the kernel with care"
M["“2 TOPS”是 CPU 融合算力，没有独立 NPU，跑大模型只能靠 CPU/RVV"] = \
    "\"2 TOPS\" is fused CPU compute with no dedicated NPU, so LLMs run on CPU/RVV only"
M["8 核实际性能仍偏低（Phoronix/多方评测：不及同期 4 核 ARM 板），不适合当桌面主力"] = \
    "Real-world 8-core performance is still low (Phoronix and others rate it below a contemporary 4-core ARM board), so it is no desktop workhorse"
M["官方镜像托管在 Google Drive，国内下载不便；eMMC 需另购模块"] = \
    "Official images are hosted on Google Drive, which is awkward from China; eMMC needs a separately purchased module"
M["固件必须与镜像版本匹配：bootchain 过旧时 Fedora 直接不启动，需先刷最新 firmware"] = \
    "Firmware must match the image: an old bootchain leaves Fedora unbootable, so flash the newest firmware first"
M["无原生 NVMe 槽，只能插 PCIe 转接卡；板载只有 2×GbE"] = \
    "No native NVMe slot — use a PCIe adapter; onboard networking is just 2× GbE"
M["iGPU 只支持 OpenGL ES，OpenGL 需 MESA_LOADER_DRIVER_OVERRIDE=zink；接独显时 GRUB 菜单不显示"] = \
    "The iGPU supports OpenGL ES only; OpenGL needs MESA_LOADER_DRIVER_OVERRIDE=zink, and with a discrete GPU the GRUB menu doesn't display"
M["国内无正规渠道，需 Arrow 等海外代理，运费/关税另计"] = \
    "No official channel in China; buy through overseas distributors such as Arrow, with shipping and duty on top"
M["不要 apt dist-upgrade：CNX 实测升级 207 个包后重启 gnome-shell 占满单核、系统近乎无响应"] = \
    "Don't apt dist-upgrade: CNX upgraded 207 packages and after a reboot gnome-shell pinned a core and the system became nearly unresponsive"
M["GPU 固件 rgx.fw 常报加载失败（PVR_K 错误），3D 加速依赖镜像内匹配的固件"] = \
    "The GPU firmware rgx.fw often fails to load (PVR_K errors); 3D acceleration depends on firmware matching the image"
M["性能约为 Raspberry Pi 3B 级别（JH7110S 1.25GHz 降频版），不适合重负载"] = \
    "Performance is roughly Raspberry Pi 3B level (JH7110S at a reduced 1.25GHz) — not for heavy loads"
M["这是 VisionFive 2 的降配版，不是 VisionFive 3"] = \
    "This is a cut-down VisionFive 2, not a VisionFive 3"
M["官方镜像停在 2023 年（Ubuntu 23.04 / Yocto 2023-06），Ubuntu 23.04 早已 EOL，apt 源基本不可用"] = \
    "Official images stopped in 2023 (Ubuntu 23.04 / Yocto 2023-06); Ubuntu 23.04 is long EOL and its apt repos are mostly dead"
M["RevyOS 的 beagle 镜像也停在 20231210，等于没有持续维护的发行版"] = \
    "RevyOS's beagle image also stops at 20231210, which leaves no continuously maintained distro"
M["刷 eMMC 需要 USB-C 进 fastboot + Xuantie 专用工具链产物，从 SD 卡启动反而简单"] = \
    "Flashing eMMC needs USB-C fastboot plus artifacts from the XuanTie toolchain; booting from SD is far simpler"
M["只有 4GB RAM，跑桌面偏紧；microHDMI 需要转接头"] = \
    "Only 4GB RAM, which is tight for a desktop; microHDMI needs an adapter"
M["WiFi 是 AP6203BM，需要配套 firmware blob，主线内核支持不完整"] = \
    "WiFi is an AP6203BM needing its own firmware blob, with incomplete mainline support"
M["cape 排针是 3.3V 逻辑，接 5V cape 会烧"] = \
    "The cape headers are 3.3V logic — a 5V cape will fry them"
M["Milk-V 文档的 Download 页 Image 区已空（迁移到 RevyOS），别在旧页面找系统镜像"] = \
    "The Image area of Milk-V's Download page is empty now (moved to RevyOS) — don't look for system images there"
M["内存挑条：必须按官方 DDR 支持列表选 RDIMM/UDIMM，否则 DDR 训练失败不开机"] = \
    "Choose memory carefully: pick RDIMM/UDIMM from the official DDR support list or DDR training fails and it won't boot"
M["需要标准 ATX 24-pin + CPU 8-pin 供电，散热器必须装（120W 典型功耗）"] = \
    "It needs standard ATX 24-pin plus CPU 8-pin power, and a cooler is mandatory (120W typical)"
M["没有板载显示输出，需要 PCIe 显卡；部分显卡在 LinuxBoot/U-Boot 阶段无输出"] = \
    "No onboard display output — add a PCIe GPU; some cards show nothing during LinuxBoot/U-Boot"
M["固件（LinuxBoot/EDK2 + MCU）升级有变砖风险，必须按官方顺序刷"] = \
    "Firmware upgrades (LinuxBoot/EDK2 + MCU) can brick the board; follow the official order exactly"
M["早期批次 ASM2824 PCIe switch 有兼容性问题，先查 buglist"] = \
    "Early batches have ASM2824 PCIe switch compatibility issues — check the buglist first"
M["64MB 的 Duo 内存太小，V2 镜像里的 AI 应用跑不动，官方明确建议 64M 用 V1 镜像"] = \
    "The 64MB Duo has too little RAM for the AI apps in V2 images; the vendor explicitly recommends V1 images for 64M boards"
M["默认只有 USB-NCM 网卡（192.168.42.1），没有 DHCP，主机要手动配同网段 IP；root 密码 milkv"] = \
    "By default there is only a USB-NCM network interface (192.168.42.1) with no DHCP, so set a host IP in the same subnet; the root password is milkv"
M["主线内核支持不完整：minimal 从 6.7、GPIO 6.8、clock/SPI/I2C/MMC/USB 6.9–6.10 才进，camera/VPU/NPU/部分 clock 仍在 review"] = \
    "Mainline support is partial: minimal landed in 6.7, GPIO in 6.8, clock/SPI/I2C/MMC/USB in 6.9–6.10, and camera/VPU/NPU and some clocks are still under review"
M["Duo 256M/S 带 ARM Cortex-A53 核，RISC-V 与 ARM 镜像不能混刷"] = \
    "Duo 256M/S include an ARM Cortex-A53 core; RISC-V and ARM images are not interchangeable"
M["没有 HDMI，Duo S 也只有 MIPI DSI；想接屏要另买转接板"] = \
    "There is no HDMI — even the Duo S only has MIPI DSI; add an adapter board to connect a screen"
M["Duo S 有 BOOT 开关，拨错进不了下载/启动模式；供电只要 5V/1A，别接快充头硬灌"] = \
    "The Duo S has a BOOT switch; the wrong position blocks download/boot mode, and 5V/1A is enough power — don't force a fast charger into it"

# ---- note ----
M["所有板子的公共起点：先在 virt 上验证内核/rootfs，再上真机，能省掉大量刷机排错时间。"] = \
    "The common starting point for every board: validate the kernel/rootfs on virt first, then move to real hardware — it saves a lot of flashing and debugging time."
M["生态最全、发行版覆盖最广的 JH7110 板，新人第一块 RISC-V 板的首选之一；注意批次固件差异。 另有 openwrt/dietpi/guix 等社区衍生版（未列入标准发行版 id）。"] = \
    "The JH7110 board with the widest ecosystem and distro coverage, and one of the best first RISC-V boards; watch for firmware differences between batches. Community derivatives such as openwrt/dietpi/guix exist too (not listed as standard distro ids)."
M["TH1520 里资料最全、社区最大的板；RevyOS 桌面可用，但 GPU/NPU 闭源是硬伤。 另有 openwrt 等社区衍生版（未列入标准发行版 id）。"] = \
    "The best-documented TH1520 board with the largest community; the RevyOS desktop works, but closed-source GPU/NPU support is the weak spot. Community derivatives such as openwrt exist too (not listed as standard distro ids)."
M["和 LicheePi 4A 同 SoC、更小更便宜，但社区规模小一截，镜像基本只有 RevyOS 一条路。"] = \
    "Same SoC as the LicheePi 4A, smaller and cheaper, but with a noticeably smaller community and essentially only RevyOS for images."
M["官方命名为 K3-CoM260（260pin SO-DIMM 核心板），任务中的 SOM260 即此形态；Pico-ITX 与 CoM260 共用 SoC/SDK 与系统镜像。K3 于 2026-04-30 全球开卖，2026-05 进入量产公售。"] = \
    "Officially named K3-CoM260 (a 260-pin SO-DIMM compute module), which is the SOM260 form factor in the brief; the Pico-ITX and CoM260 share the SoC/SDK and system images. K3 went on global sale on 2026-04-30 and reached volume public sales in 2026-05."
M["型号消歧：芯片是知合计算 A210（阿基米德系列，玄铁 C920/C908 核），开发板品牌写作“玄铁 MelonPi”。Ubuntu 镜像只覆盖 A200（a200-evb），A210 不通用。"] = \
    "Model disambiguation: the chip is Zhihe A210 (Archimedes series, XuanTie C920/C908 cores), while the board brand is written \"XuanTie MelonPi\". The Ubuntu image only covers the A200 (a200-evb) and does not work on the A210."
M["CanMV（MicroPython 固件）是出货量最大、资料最全的形态；Linux 侧官方主推 Buildroot。Apache NuttX 另有 CanMV-K230 板级支持（非发行版）；RuyiSDK 支持矩阵已收录 CanMV K230(D)，可 ruyi device provision 取镜像。"] = \
    "CanMV (MicroPython firmware) is the highest-volume, best-documented form; on the Linux side the vendor pushes Buildroot. Apache NuttX has separate CanMV-K230 board support (not a distro), and the RuyiSDK support matrix already covers the CanMV K230(D), so `ruyi device provision` can fetch images."
M["Megrez 是 EIC7700X 最早量产的 Mini-ITX 板；同芯片还有 SiFive HiFive Premier P550（更贵、Ubuntu 官方支持更好）。"] = \
    "Megrez was the first EIC7700X board in volume production (Mini-ITX); the same chip also appears in the SiFive HiFive Premier P550, which is dearer but has better official Ubuntu support."
M["定位是“能插显卡的 RISC-V 工作站/轻服务器”，首选 OS 为 Ubuntu；Fedora 44 起改用 Omni 内核。"] = \
    "Positioned as a RISC-V workstation/light server that takes a GPU, with Ubuntu as the first-choice OS; from Fedora 44 it uses the Omni kernel."
M["历史上的 RISC-V 桌面标杆，现在更适合二手捡漏/教学；新人上手成本高（串口+拨码+供电），不推荐作为第一块板。 另有 openwrt 等社区衍生版（未列入标准发行版 id）。"] = \
    "The historic RISC-V desktop reference, now better suited to second-hand bargains or teaching; the setup cost for newcomers (serial + DIP switches + power) is high, so it is not recommended as a first board. Community derivatives such as openwrt exist too (not listed as standard distro ids)."
M["K1 是 2024-2025 出货量最大的高性能 RISC-V SBC 芯片之一，BPI-F3 生态最杂（官方 Bianbu + 社区 Armbian/Fedora/openSUSE/Arch/Gentoo 都有镜像）。RuyiSDK 支持矩阵也收录了 BPI-F3。"] = \
    "K1 was one of the highest-volume high-performance RISC-V SBC chips in 2024-2025, and the BPI-F3 has the most varied ecosystem (official Bianbu plus community Armbian/Fedora/openSUSE/Arch/Gentoo images). The RuyiSDK support matrix covers the BPI-F3 too."
M["Ky X1 与 SpacemiT K1 高度同源（8×X60 类核，业界普遍认为是改名版），但厂商未正面确认；因此不能直接套用 Bianbu K1 镜像。"] = \
    "Ky X1 is closely related to SpacemiT K1 (8× X60-class cores, widely believed to be a rebrand, though the vendor has not confirmed it), so Bianbu K1 images cannot simply be reused."
M["与 Milk-V Megrez 同芯片（EIC7700X），但 P550 有官方 Ubuntu 预装+OTA，软件成熟度高于 Megrez；另有 Red Hat RHEL 10 开发者预览支持。"] = \
    "Same chip as the Milk-V Megrez (EIC7700X), but the P550 ships official Ubuntu with OTA, so its software is more mature; there is also Red Hat RHEL 10 developer preview support."
M["VisionFive 3 未发布：StarFive 2026 年的新品是面向服务器的 Dubhe-100 RISC-V IP，SBC 产品线只更新到 VisionFive 2 Lite（2025-08 众筹、2025-10 量产）。rvspace 另称原生支持 OpenWrt（非发行版 id）。"] = \
    "There is no VisionFive 3: StarFive's 2026 launch is the server-oriented Dubhe-100 RISC-V IP, and the SBC line only moved to the VisionFive 2 Lite (crowdfunded 2025-08, in production 2025-10). rvspace separately claims native OpenWrt support (not a distro id)."
M["硬件做工好、cape 生态强，但软件是 TH1520 三兄弟里最差的：官方镜像三年没更新，只适合当收藏/教学。"] = \
    "Good build quality and a strong cape ecosystem, but the worst software of the three TH1520 boards: the official image has not been updated in three years, so it is only good for collecting or teaching."
M["唯一能当「RISC-V 工作站/服务器」用的板子，价格与功耗都是另一个量级；适合做 64 核并行编译、CI runner，不适合入门。 另有 opencloudos 等社区衍生版（未列入标准发行版 id）。"] = \
    "The only board that works as a RISC-V workstation/server, at a completely different price and power level; good for 64-core parallel builds and CI runners, not for beginners. Community derivatives such as opencloudos exist too (not listed as standard distro ids)."
M["US$5 级别的入门神器，适合学嵌入式 Linux/RTOS，不适合当桌面；买之前先确认是 64M 还是 256M/S，镜像完全不通用。 另有 openwrt 等社区衍生版（未列入标准发行版 id）。"] = \
    "A US$5-class starter board, good for learning embedded Linux/RTOS and useless as a desktop; check whether you have a 64M or a 256M/S before buying, since the images are completely incompatible. Community derivatives such as openwrt exist too (not listed as standard distro ids)."
