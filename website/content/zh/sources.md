---
title: "来源与致谢"
sub: "站上每条结论的来源、判定方法与致谢"
layout: sources
---

**这个站上每一条技术结论都应当能点回到来源。** 下面按「一手 / 二手」分层列出全部来源，并说明每条结论是怎么判定的。站点数据每日自动核查一次，每个条目都带核查日期。

## 一、测试结论的来源：RuyiSDK 支持矩阵

站内所有「某系统在某板上实测可用/不可用」的结论，**首选依据是 RuyiSDK 官方测试矩阵**：

- 站点：<https://matrix.ruyisdk.org/>
- 源仓库（数据本体，每板每系统一份 markdown + YAML front matter）：<https://github.com/ruyisdk/support-matrix>
- 数据抓取方式：本站每日拉取该仓库，解析每一份测试报告的 `sys / sys_ver / sys_var / status / last_update` 字段，映射成站内的「板 × 发行版」组合
- 每条报告的链接形如 `https://matrix.ruyisdk.org/reports/<板>/<系统>/<变体>/`，站内矩阵格子和发行版/开发板页面里的「RuyiSDK 实测报告」表都可以直接点进原文

**致谢**：RuyiSDK 团队与 PLCT 实验室（中国科学院软件研究所）长期维护这套逐板实测的数据，这是 RISC-V 生态里少见的、可复核的第三方测试集。本站直接采信它，不重复造轮子。

### 状态枚举的定义（引自该仓库 CONTRIBUTING.md）

| 状态 | 含义 |
| --- | --- |
| `good` | 完整可用，可以进桌面环境使用 |
| `basic` | 基本可用，能启动、能通过串口使用 |
| `part` | 只具备部分功能 |
| `cft` | 有镜像可用，但还需要在真机上进一步验证 |
| `cfh` | 官方文档/社区说支持，但实测启动失败 |
| `cfi` | 官方文档声称支持，但还没有可用镜像 |
| `wip` | 只有「将来会支持」的宣称，无镜像无源码 |

站点矩阵里，格子带实心符号的是 RuyiSDK 实测数据；只有灰点的是「本站资料」，未经 RuyiSDK 实测，两者图例上有明确区分。

## 二、发行版官方来源

26 个发行版条目里，`下载` 与 `安装文档` 链接全部指向**官方**页面：发行版自己的下载站、官方文档站、官方 wiki 或官方仓库。典型的几类：

- 上游发行版：[debian.org](https://www.debian.org/releases/stable/riscv64/) / [cdimage.debian.org](https://cdimage.debian.org/cdimage/release/current/riscv64/iso-cd/) / [ubuntu.com](https://ubuntu.com/download/risc-v) / [cdimage.ubuntu.com](https://cdimage.ubuntu.com/releases/) / [fedoraproject.org](https://fedoraproject.org/wiki/Architectures/RISC-V) / [get.opensuse.org](https://get.opensuse.org/) / [alpinelinux.org](https://alpinelinux.org/downloads/) / [archlinuxriscv.org](https://archriscv.felixc.at/) / [gentoo.org](https://www.gentoo.org/downloads/) / [nixos.org](https://nixos.org/download/) / [freebsd.org](https://wiki.freebsd.org/riscv) / [netbsd.org](https://www.netbsd.org/ports/riscv/) / [openbsd.org](https://www.openbsd.org/riscv64.html)
- 厂商下游系统：[revyos.com](https://revyos.com/) 与 [docs.revyos.dev](https://docs.revyos.dev/)（玄铁 TH1520/SG2042）、[spacemit.com](https://www.spacemit.com/) 与 [archive.spacemit.com](https://archive.spacemit.com/)（Bianbu）、[openeuler.org](https://www.openeuler.org/zh/download/) 与 [docs.openeuler.org](https://docs.openeuler.org/)、[openkylin.top](https://www.openkylin.top/downloads/) 与 docs.openkylin.top、[deepin.org](https://www.deepin.org/) 与 [deepin-community.github.io](https://deepin-community.github.io/sig-deepin-ports/images/riscv64)
- 社区构建：[armbian.com](https://www.armbian.com/download/)、[dietpi.com](https://dietpi.com/#download)、[irradium.org](https://irradium.org/)、bredos.org、FVF 的发布仓库

每个发行版页面底部的「本页来源」列出的就是该条目的全部依据链接。

## 三、开发板厂商来源

25 块开发板的规格与官方系统信息，来自厂商官方产品页、官方文档站与官方仓库，例如：

- [sifive.com](https://www.sifive.com/boards)（HiFive Unmatched / Premier P550）、[starfivetech.com](https://www.starfivetech.com/en) 与 [doc-en.rvspace.org](https://doc-en.rvspace.org/)（VisionFive 2 / VisionFive 2 Lite）
- [sipeed.com](https://sipeed.com/) 与 [wiki.sipeed.com](https://wiki.sipeed.com/)（LicheePi 4A / Lichee Cluster 4A）、[milkv.io](https://milkv.io/) 与 `milkv.io/docs`（Meles / Mars / Jupiter / Pioneer / Megrez / Titan / Duo）
- [banana-pi.org](https://www.banana-pi.org/) 与 [docs.banana-pi.org](https://docs.banana-pi.org/)（BPI-F3）、[orangepi.org](http://www.orangepi.org/)（RV2）、[kendryte.com](https://www.kendryte.com/) 与嘉楠开发者站（K230）、[spacemit.com](https://www.spacemit.com/)（K3 Pico-ITX / CoM260）
- 知合计算 A210 / 玄铁 MelonPi：[zhcomputing.com](http://www.zhcomputing.com/) 与 [developer.zhcomputing.com](https://developer.zhcomputing.com/zh/docs/A210/)、[matrix.ruyisdk.org](https://matrix.ruyisdk.org/) 的 A210_SODIMM_V2 报告
- QEMU：[qemu.org](https://www.qemu.org/docs/master/system/riscv/virt.html) 官方文档的 RISC-V virt 机型章节

少数新板的硬件参数直接取自 RuyiSDK 矩阵里的板卡元数据，这些条目在页面上注明「板上信息取自 RuyiSDK 测试矩阵记录；供货与价格未单独核实」。

## 四、AI 软件维度：逐条给证据

AI 支持页面不给「感觉」，每条判断背后都挂了链接，主要来自：

- **上游项目文档**：[github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)（含 `docs/build-riscv64-spacemit.md` 与 SpacemiT kernel 实测数据）、[github.com/microsoft/onnxruntime](https://github.com/microsoft/onnxruntime)、[github.com/opencv/opencv](https://github.com/opencv/opencv) 的 RISC-V wiki、[github.com/Tencent/ncnn](https://github.com/Tencent/ncnn) 的 RISC-V CI、[github.com/OAID/Tengine](https://github.com/OAID/Tengine)
- **第三方分发**：[riseproject.dev](https://riseproject.dev/)（RISE 的 PyTorch RISC-V 轮子）、[github.com/felixonmars/archriscv-packages](https://github.com/felixonmars/archriscv-packages)
- **学术**：arXiv 2503.17422（V-Seek，SG2042 上的 LLM 推理优化）
- **厂商工具链文档**：玄铁 HHB（LicheePi 4A NPU）、SpacemiT AI SDK、ESWIN ENNP SDK、嘉楠 nncase、知合 TORQ-Toolkit
- **实测文章**：CNX Software、ServeTheHome、The Register、Phoronix 等对具体板子的上手记录

找不到公开证据的，页面上写「未找到公开证据」，**不写推测**。

## 五、二手来源与口径

媒体转述一律标注为转述，不作为一手依据，只用来说明「这条消息存在」。常见来源包括 CNX Software、Phoronix、ServeTheHome、The Register、The Next Platform、Design & Reuse，以及中文侧的 IT之家、芯智讯、上观新闻、科技日报、《财经》。厂商自报的性能与部署情况（例如「32 并发推理达 x86 平台 95.8%」「已在多地智算中心落地」）一律标注「厂商公布」，与第三方实测分开写。

## 六、方法与免责

- **核查日期**：每个条目带 `checked` 字段，页面上显示「最后核查」日期。数据每日 03:00 自动复查一遍
- **不猜**：查不到的字段留空；厂商未公布的价格、TDP、具体 SoC 型号，宁可不写，也不填一个看起来合理的数字
- **链接校验**：站内所有外链由 `scripts/check_urls.py` 逐条 curl 验证；失效的链接会被换成稳定的目录页或官方下载页，换不了的直接删掉
- **勘误**：发现问题请开 issue 或 MR，标明具体条目与依据链接，我们按证据改

## 七、致谢

感谢这些项目与团队，本站的数据建立在他们的工作之上：

- **RuyiSDK 团队 / PLCT 实验室（中国科学院软件研究所）** —— 逐板逐系统的实测矩阵，本站最核心的数据来源
- **各发行版社区与维护者** —— Debian、Ubuntu、Fedora、openSUSE、Alpine、Arch Linux RISC-V、Gentoo、NixOS、FreeBSD、NetBSD、OpenBSD、ALT Linux、Buildroot、Yocto 等
- **各开发板厂商与社区** —— SiFive、StarFive、Sipeed、Milk-V、Banana Pi、Orange Pi、SpacemiT、ESWIN、UltraRISC、嘉楠、知合计算、PINE64、BIT-BRICK
- **中文发行版团队** —— openEuler RISC-V SIG、openKylin、deepin、openRuyi
- **AI 侧的开源项目** —— llama.cpp、ONNX Runtime、OpenCV、ncnn、Tengine、RISE Project
- **RISC-V International** —— 规范与生态基础设施
