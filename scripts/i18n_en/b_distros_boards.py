# -*- coding: utf-8 -*-
"""distros.yaml: boards[].note 的英译。"""

M = {}

M["官方 riscv64 netinst 在 QEMU virt 上安装，是 d-i 的主要目标平台"] = \
    "The official riscv64 netinst installs on QEMU virt; it is a primary target platform for d-i"
M["通用 riscv64 镜像 + 板端 U-Boot/UEFI 启动；Debian 不发布板级镜像"] = \
    "Generic riscv64 image booted via the board's own U-Boot/UEFI; Debian does not publish board images"
M["同上，JH7110 板用厂商 U-Boot 提供 UEFI 后装通用镜像"] = \
    "As above: JH7110 boards use the vendor U-Boot to provide UEFI, then install the generic image"
M["TH1520 需厂商 U-Boot/内核，Debian 主线无板级支持"] = \
    "TH1520 needs a vendor U-Boot/kernel; Debian mainline has no board support"
M["同为 TH1520 平台，情况与 LicheePi 4A 类似"] = \
    "Same TH1520 platform, so the situation matches LicheePi 4A"
M["SpacemiT K3 需厂商 BSP；Debian 主线支持情况未确认"] = \
    "SpacemiT K3 needs the vendor BSP; mainline Debian support is unconfirmed"
M["知合 A210 需厂商固件/内核，无 Debian 官方支持"] = \
    "Zhihe A210 needs vendor firmware/kernel; no official Debian support"
M["Canaan K230 为 MCU 类 SoC，主线支持有限"] = \
    "Canaan K230 is an MCU-class SoC with limited mainline support"
M["EIC7700 板可走通用 UEFI 镜像，未在 Debian 文档确认"] = \
    "EIC7700 boards can use the generic UEFI image; not confirmed in Debian docs"
M["DP1000 同上，未在 Debian 文档确认"] = "DP1000 as above; not confirmed in Debian docs"
M["SG2042 可走通用镜像，未在 Debian 文档确认"] = "SG2042 can use the generic image; not confirmed in Debian docs"
M["SpacemiT K1 板，通用镜像 + 板端 U-Boot"] = "SpacemiT K1 board: generic image + board U-Boot"
M["26.10 / 26.04.1 LTS 提供 Desktop、Server live installer 与 preinstalled 镜像，官方页有 QEMU 安装说明"] = \
    "26.10 / 26.04.1 LTS provide Desktop and Server live installers plus preinstalled images; the official page has QEMU instructions"
M["24.04.5 LTS 提供 ubuntu-24.04.5-preinstalled-server-riscv64+unmatched.img.xz"] = \
    "24.04.5 LTS provides ubuntu-24.04.5-preinstalled-server-riscv64+unmatched.img.xz"
M["jh7110 镜像（24.04.5 LTS +jh7110，覆盖 VisionFive 2 / VisionFive 2 Lite）"] = \
    "jh7110 image (24.04.5 LTS +jh7110, covering VisionFive 2 / VisionFive 2 Lite)"
M["官方板卡列表里没有 LicheePi 4A（只有 Sipeed LicheeRV Dock），需自建/社区镜像"] = \
    "LicheePi 4A is not in the official board list (only the Sipeed LicheeRV Dock is), so you need your own or a community image"
M["官方板卡列表无 Milk-V Meles"] = "Milk-V Meles is not in the official board list"
M["SpacemiT K3 平台（CoM260、picoITX、DeepComputing FML13V05）自 26.10 起支持"] = \
    "SpacemiT K3 platforms (CoM260, picoITX, DeepComputing FML13V05) supported since 26.10"
M["官方板卡列表无知合 A210"] = "Zhihe A210 is not in the official board list"
M["官方板卡列表无 Canaan K230"] = "Canaan K230 is not in the official board list"
M["官方板卡列表无 Milk-V Megrez"] = "Milk-V Megrez is not in the official board list"
M["官方板卡列表无 Milk-V Titan"] = "Milk-V Titan is not in the official board list"
M["官方板卡列表无 Milk-V Pioneer"] = "Milk-V Pioneer is not in the official board list"
M["官方板卡列表只有 Milk-V Mars（同 K1），无 Orange Pi RV2"] = \
    "The official list only has Milk-V Mars (same K1), no Orange Pi RV2"
M["官方板卡列表无 Banana Pi BPI-F3"] = "Banana Pi BPI-F3 is not in the official board list"
M["官方支持，用 mainline 内核即可（Hardware 页 QEMU 条目）"] = \
    "Officially supported with the mainline kernel (QEMU entry on the Hardware page)"
M["Hardware 页未列 SiFive Unmatched（只列了 Premier P550）"] = \
    "SiFive Unmatched is not on the Hardware page (only Premier P550 is)"
M["StarFive JH7110 条目官方支持；不需要 NVMe/PCIe 时可用 mainline 内核"] = \
    "Officially supported under the StarFive JH7110 entry; use the mainline kernel if you don't need NVMe/PCIe"
M["Hardware 页未列 LicheePi 4A / TH1520"] = "LicheePi 4A / TH1520 are not on the Hardware page"
M["Hardware 页未列 Milk-V Meles"] = "Milk-V Meles is not on the Hardware page"
M["SpacemiT K3 条目：K3 Pico-ITX、Milk-V Jupiter 2、K3-CoM260、DC-ROMA III (FML13V05)"] = \
    "SpacemiT K3 entry: K3 Pico-ITX, Milk-V Jupiter 2, K3-CoM260, DC-ROMA III (FML13V05)"
M["Hardware 页未列知合 A210"] = "Zhihe A210 is not on the Hardware page"
M["Hardware 页未列 Canaan K230"] = "Canaan K230 is not on the Hardware page"
M["ESWIN EIC7700X 条目官方支持（Milk-V Megrez、HiFive Premier P550）"] = \
    "Officially supported under the ESWIN EIC7700X entry (Milk-V Megrez, HiFive Premier P550)"
M["UltraRISC UR-DP1000 条目官方支持（Milk-V Titan）"] = \
    "Officially supported under the UltraRISC UR-DP1000 entry (Milk-V Titan)"
M["SOPHGO SG2042 条目官方支持（Milk-V Pioneer）"] = \
    "Officially supported under the SOPHGO SG2042 entry (Milk-V Pioneer)"
M["SpacemiT M1/K1 条目官方支持（含 Orange Pi RV 2、BPI-F3、Milk-V Jupiter）"] = \
    "Officially supported under the SpacemiT M1/K1 entry (covers Orange Pi RV 2, BPI-F3, Milk-V Jupiter)"
M["SpacemiT M1/K1 条目官方支持（Banana Pi BPI-F3）"] = \
    "Officially supported under the SpacemiT M1/K1 entry (Banana Pi BPI-F3)"
M["FVF 自称适配市面主流 RISC-V 开发板；未逐板核实"] = \
    "FVF claims support for mainstream RISC-V boards; not verified board by board"
M["同上，未逐板核实"] = "As above; not verified board by board"
M["主力参考板，SD/eMMC 双启动，镜像与文档最全"] = \
    "The main reference board: SD/eMMC boot, the most complete images and docs"
M["Milk-V Meles，官方镜像 20260504 + 刷写教程"] = "Milk-V Meles: official image 20260504 plus a flashing tutorial"
M["Milk-V Pioneer（SG2042），镜像 20260504"] = "Milk-V Pioneer (SG2042): image 20260504"
M["以 coreboot+OpenSBI+EDK2 固件形式提供（Ruyi Firmware），非完整 OS 镜像"] = \
    "Provided as coreboot+OpenSBI+EDK2 firmware (Ruyi Firmware), not a full OS image"
M["Banana Pi BPI-F3（K1），官方支持列表在列；同系还有 Milk-V Jupiter、MUSE Card/Pi/Pi Pro/Box/Book"] = \
    "Banana Pi BPI-F3 (K1) is on the supported list; the same family also has Milk-V Jupiter and MUSE Card/Pi/Pi Pro/Box/Book"
M["K3 平台：Pico ITX 与 CoM260 Kit，Bianbu 4.x 专属"] = \
    "K3 platforms: Pico-ITX and CoM260 Kit, Bianbu 4.x only"
M["MusePi Pro 为 Platinum（内核 6.18.55 current / 6.6.100 legacy）；K3 Pico-ITX 亦为 Platinum"] = \
    "MusePi Pro is Platinum (kernel 6.18.55 current / 6.6.100 legacy); K3 Pico-ITX is Platinum too"
M["Standard 级，内核 6.18.45；另有 Bianbu 变体"] = "Standard tier, kernel 6.18.45; a Bianbu variant also exists"
M["Community 级，仅 Debian 13 minimal（6.18.58）"] = "Community tier, Debian 13 minimal only (6.18.58)"
M["Community 级，vendor 内核 6.6.20，Ubuntu/Debian 三镜像"] = \
    "Community tier, vendor kernel 6.6.20, three Ubuntu/Debian images"
M["官方提供 u-boot-qemu 包，QEMU 为标准开发路径"] = \
    "An official u-boot-qemu package exists; QEMU is the standard development path"
M["官方提供 u-boot-unmatched / u-boot-unleashed 包"] = "Official u-boot-unmatched / u-boot-unleashed packages exist"
M["官方提供 u-boot-starfive 包（StarFive JH7110 系）"] = "An official u-boot-starfive package exists (StarFive JH7110 family)"
M["无 u-boot-th1520 类官方包，需自备引导"] = "No official u-boot-th1520-style package; bring your own bootloader"
M["TH1520 平台，同上"] = "TH1520 platform, as above"
M["官方有 u-boot-spacemit 包（SpacemiT 平台，以 K1 系为主）；K3 是否单独覆盖未确认"] = \
    "An official u-boot-spacemit package exists (SpacemiT platforms, mainly K1); whether K3 is covered separately is unconfirmed"
M["无官方 u-boot 包"] = "No official u-boot package"
M["SpacemiT K1 板，可能复用 u-boot-spacemit，未确认"] = \
    "SpacemiT K1 board, possibly reusing u-boot-spacemit; unconfirmed"
M["官方明确 \"tested\"：QEMU 在 mainline linux 包支持列表内"] = \
    "Explicitly \"tested\" upstream: QEMU is on the supported list of the mainline linux package"
M["HiFive Unmatched / Unleashed 在 tested 列表内"] = "HiFive Unmatched / Unleashed are on the tested list"
M["VisionFive v2（及 Milk-V Mars）在 tested 列表内"] = "VisionFive v2 (and Milk-V Mars) are on the tested list"
M["仅在 [unsupported] 仓库提供 TH1520 实验内核"] = "Only an experimental TH1520 kernel in the [unsupported] repo"
M["TH1520 平台，走 [unsupported] 实验内核路径，未单列"] = \
    "TH1520 platform via the [unsupported] experimental kernel; not listed separately"
M["未在支持列表；官方称 AX45MP 以外板子可能需 BSP/自定义内核"] = \
    "Not on the supported list; upstream says boards other than AX45MP may need a BSP or custom kernel"
M["未在支持列表，需 BSP/自定义内核"] = "Not on the supported list; needs a BSP or custom kernel"
M["仅作为赞助测试板被致谢，无正式支持条目"] = \
    "Only credited as a sponsored test board; no formal support entry"
M["ESWIN EIC7700 作为测试板被致谢，无正式支持条目"] = \
    "ESWIN EIC7700 is credited as a test board; no formal support entry"
M["未在支持列表"] = "Not on the supported list"
M["仅在 [unsupported] 仓库提供 SG2042 实验内核"] = "Only an experimental SG2042 kernel in the [unsupported] repo"
M["BananaPi F3 作为测试板被致谢，无正式支持条目"] = \
    "BananaPi F3 is credited as a test board; no formal support entry"
M["Tumbleweed riscv64 DVD/NET ISO 可在 QEMU 直接安装（通用镜像）"] = \
    "The Tumbleweed riscv64 DVD/NET ISO installs directly in QEMU (generic image)"
M["无板级镜像，通用 ISO + 板端 UEFI/U-Boot"] = "No board images; generic ISO + the board's UEFI/U-Boot"
M["有第三方实机安装录像，但 openSUSE 无官方板级镜像"] = \
    "There is third-party footage of a real-hardware install, but openSUSE has no official board image"
M["TH1520 无官方支持"] = "No official TH1520 support"
M["SpacemiT K3 无官方支持"] = "No official SpacemiT K3 support"
M["无官方支持"] = "No official support"
M["通用镜像 + 板端 UEFI，未确认"] = "Generic image + board UEFI; unconfirmed"
M["qemu-system-riscv64 与 qemu-riscv64 user-mode 均可；官方 wiki 有专门 QEMU 安装页"] = \
    "Both qemu-system-riscv64 and qemu-riscv64 user-mode work; the official wiki has a dedicated QEMU install page"
M["社区成员持有并在 wiki 硬件清单登记（SiFive FU740）"] = \
    "Community members own it and listed it in the wiki hardware table (SiFive FU740)"
M["JH7110，wiki 标注 Active / 上游内核跟进"] = "JH7110; the wiki marks it Active with mainline kernel work in progress"
M["TH1520（C910），社区登记可跑标准安装"] = "TH1520 (C910); community reports the standard install works"
M["Milk-V Pioneer Box（SG2042，64 核）有开发者实机"] = \
    "Developers have real Milk-V Pioneer Box hardware (SG2042, 64 cores)"
M["Ky X1（X60），社区登记"] = "Ky X1 (X60); community-listed"
M["SpacemiT K1（RVV 1.0），社区登记"] = "SpacemiT K1 (RVV 1.0); community-listed"
M["可模拟，但 wiki 明确提示部分程序在 QEMU 下会 segfault"] = \
    "Emulation works, but the wiki warns that some programs segfault under QEMU"
M["最早的社区移植目标（zhaofengli/nixos-riscv64）"] = \
    "The earliest community port target (zhaofengli/nixos-riscv64)"
M["JH7110，社区镜像 + misuzu/nixos-vf2 flake"] = "JH7110: community image plus the misuzu/nixos-vf2 flake"
M["ryan4yin/nixos-licheepi4a 社区 flake"] = "Community flake ryan4yin/nixos-licheepi4a"
M["硬件说明列出 QEMU 与 Spike"] = "The hardware notes list QEMU and Spike"
M["SiFive HiFive Unmatched（FU740）官方支持"] = "SiFive HiFive Unmatched (FU740) officially supported"
M["StarFive VisionFive 2（JH7110）官方支持"] = "StarFive VisionFive 2 (JH7110) officially supported"
M["官方文档专门讲 qemu 启动"] = "The official docs cover QEMU boot specifically"
M["端口页列 StarFive VisionFive 2 / Milk-V Mars CM"] = \
    "The port page lists StarFive VisionFive 2 / Milk-V Mars CM"
M["当前唯一“主目标”平台"] = "Currently the only primary target platform"
M["平台页列入 VisionFive / VisionFive 2，但需先做固件调整才能启动"] = \
    "The platform page lists VisionFive / VisionFive 2, but firmware tweaks are needed before it boots"
M["镜像设计为可直接在 qemu 启动，wiki 有 QEMU 专页"] = \
    "The image is designed to boot directly in QEMU; the wiki has a QEMU page"
M["wiki 提供 HiFive Unmatched/Unleashed 写盘与启动说明"] = \
    "The wiki has imaging and boot instructions for HiFive Unmatched/Unleashed"
M["qemu_riscv64_virt / _efi / nommu，rv32 同套"] = "qemu_riscv64_virt / _efi / nommu, with the same set for rv32"
M["visionfive2_defconfig（树内）"] = "visionfive2_defconfig (in tree)"
M["hifive_unmatched_defconfig（树内）"] = "hifive_unmatched_defconfig (in tree)"
M["sipeed_licheepi_4a_defconfig（树内）"] = "sipeed_licheepi_4a_defconfig (in tree)"
M["oe-core 原生 qemuriscv64/qemuriscv32"] = "Native qemuriscv64/qemuriscv32 in oe-core"
M["meta-riscv 的 bananapi-f3（主线内核/U-Boot，仍需厂商 FSBL）"] = \
    "meta-riscv's bananapi-f3 (mainline kernel/U-Boot, still needs the vendor FSBL)"
M["meta-riscv 的 k3-com260 / k3-pico-itx（含 -mainline 变体）"] = \
    "meta-riscv's k3-com260 / k3-pico-itx (including -mainline variants)"
M["meta-riscv 的 licheepi-4a"] = "meta-riscv's licheepi-4a"
M["meta-riscv 的 visionfive2"] = "meta-riscv's visionfive2"
M["meta-riscv 的 orangepi-rv2（主线内核/U-Boot + 厂商 FSBL）"] = \
    "meta-riscv's orangepi-rv2 (mainline kernel/U-Boot + vendor FSBL)"
M["meta-riscv 的 zhihe-a210：OSU-OSL 主线内核，仅 TFTP netboot，无 bootloader recipe"] = \
    "meta-riscv's zhihe-a210: OSU-OSL mainline kernel, TFTP netboot only, no bootloader recipe"
M["Milk-V Pioneer（SG2042），官方安装文档 RISC-V-Pioneer1.3"] = \
    "Milk-V Pioneer (SG2042); the official install guide is RISC-V-Pioneer1.3"
M["官方安装文档单列，TH1520 平台"] = "Has its own official install doc; TH1520 platform"
M["SP3 起支持 SpacemiT K3（COM260 验证，SD + GMAC），首个进入 LTS 的 RVA23 SoC"] = \
    "SpacemiT K3 supported since SP3 (validated on COM260, SD + GMAC), the first RVA23 SoC to enter LTS"
M["官方 QEMU 安装文档，最适合先试"] = "Official QEMU install docs; the easiest way to try it first"
M["23.03 起支持 VisionFive 2，24.03 文档未单列"] = \
    "VisionFive 2 supported since 23.03; not listed separately in the 24.03 docs"
M["3.0 提供 SpacemiT K3 Server / Embedded 镜像"] = "3.0 provides SpacemiT K3 Server / Embedded images"
M["2.0 SP2 提供 LicheePi4A 镜像（2.5G，2025-08-26）"] = "2.0 SP2 provides a LicheePi4A image (2.5G, 2025-08-26)"
M["2.0 SP2 提供 Milk-V Pioneer 镜像（3.0G）"] = "2.0 SP2 provides a Milk-V Pioneer image (3.0G)"
M["2.0 SP2 提供 RVA23 QEMU 镜像（1.8G）"] = "2.0 SP2 provides an RVA23 QEMU image (1.8G)"
M["2.0 SP2 有 SpacemiT K1 镜像（未点名 BPI-F3，需自行验证）"] = \
    "2.0 SP2 has a SpacemiT K1 image (BPI-F3 is not named; verify yourself)"
M["TH1520 设备定制镜像（u-boot 启动，内核 6.6）"] = \
    "Device-specific TH1520 image (U-Boot boot, kernel 6.6)"
M["K3 设备定制镜像，最新 25-crimson-preview"] = "Device-specific K3 image, newest 25-crimson-preview"
M["SG2042（MilkV Pioneer），linuxboot 启动，内核 6.6/6.12/6.16"] = \
    "SG2042 (MilkV Pioneer), LinuxBoot boot, kernel 6.6/6.12/6.16"
M["JH7110，内核 5.15/6.6/6.12，u-boot 启动"] = "JH7110, kernel 5.15/6.6/6.12, U-Boot boot"
M["UltraRISC DP1000（MilkV Titan），主线内核 + UEFI"] = "UltraRISC DP1000 (MilkV Titan), mainline kernel + UEFI"
M["ESWIN EIC7700（MilkV Megrez），u-boot 启动"] = "ESWIN EIC7700 (MilkV Megrez), U-Boot boot"
M["QEMU 主线内核 + UEFI"] = "QEMU, mainline kernel + UEFI"
M["SpacemiT K1 设备定制镜像"] = "Device-specific SpacemiT K1 image"
M["官方提供 QEMU/virt 镜像与 RVA23 虚拟化说明，是最省事的试用方式"] = \
    "An official QEMU/virt image plus RVA23 virtualization notes; the least effort way to try it"
M["Ruyi Firmware（coreboot+OpenSBI+EDK2）在 SpacemiT K3 Pico ITX 上验证固件→桌面全流程"] = \
    "Ruyi Firmware (coreboot+OpenSBI+EDK2) validates the whole firmware-to-desktop path on SpacemiT K3 Pico-ITX"
M["slarm64 提供 visionfive_2 镜像目录"] = "slarm64 provides a visionfive_2 image directory"
M["slarm64 提供 lichee_pi_4a 镜像目录"] = "slarm64 provides a lichee_pi_4a image directory"
M["Cuttlefish（cvd）是官方唯一运行方式，需 qemu ≥ 8.1（9.0+ 对 V 扩展更稳）"] = \
    "Cuttlefish (cvd) is the only official way to run it and needs qemu >= 8.1 (9.0+ is steadier for the V extension)"
