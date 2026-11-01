# -*- coding: utf-8 -*-
"""ai.yaml: ruyisdk.note / board_name / soc / npu / note / runs[].note / runs[].item 的英译。"""

M = {}

# ---- ruyisdk.note ----
M["RuyiSDK 官方「RISC-V Board and OS Support Matrix」；前端为 Astro 静态站点，/table/ 页面正文由 JS 渲染，数据直接来自 GitHub 仓库 ruyisdk/support-matrix （每个 板/发行版 目录一个 README.md，YAML frontmatter 即数据源），本次以 git sparse clone 拉取全部 951 个 md 文件后解析，等价于站点数据。矩阵粒度是「能否启动/能否进桌面」的支持等级，不含逐软件包可用性；「RuyiSDK 可直接刷写」另见 ruyi_provisioning。"] = \
    "RuyiSDK's official \"RISC-V Board and OS Support Matrix\". The front end is a static Astro site whose /table/ content is rendered by JS, and the data comes straight from the GitHub repo ruyisdk/support-matrix (one README.md per board/distro directory, with YAML frontmatter as the data source). This snapshot was parsed from all 951 markdown files pulled with a git sparse clone, which is equivalent to the site data. The matrix records support level — whether it boots and whether it reaches a desktop — not per-package availability; for \"RuyiSDK can flash it directly\" see ruyi_provisioning."

# ---- board_name ----
M["QEMU virt 虚拟机型"] = "QEMU virt (virtual machine)"
M["荔枝派 4A（LicheePi 4A）"] = "LicheePi 4A"
M["进迭时空 SpacemiT K3（Pico-ITX / CoM260）"] = "SpacemiT K3 (Pico-ITX / CoM260)"
M["知合计算 A210（玄铁 MelonPi 开发板）"] = "Zhihe A210 (XuanTie MelonPi dev board)"
M["嘉楠 Canaan K230（Kendryte K230 / CanMV-K230）"] = "Canaan K230 (Kendryte K230 / CanMV-K230)"
M["Milk-V Megrez（ESWIN EIC7700X）"] = "Milk-V Megrez (ESWIN EIC7700X)"
M["Milk-V Titan（UltraRISC DP1000）"] = "Milk-V Titan (UltraRISC DP1000)"
M["Milk-V Pioneer（SG2042 服务器向）"] = "Milk-V Pioneer (SG2042, server-oriented)"
M["Milk-V Duo 系列（Duo / Duo 256M / Duo S）"] = "Milk-V Duo series (Duo / Duo 256M / Duo S)"

# ---- soc ----
M["QEMU 模拟 rv64（vlen=256, RVV 1.0）"] = "QEMU-emulated rv64 (vlen=256, RVV 1.0)"
M["SiFive FU740 (4x U74, RV64GC，无 V)"] = "SiFive FU740 (4x U74, RV64GC, no V)"
M["StarFive JH7110 (4x U74, RV64GC，无 V)"] = "StarFive JH7110 (4x U74, RV64GC, no V)"
M["T-HEAD TH1520 (4x C910 @1.85GHz, RV64GCV 0.7.1)"] = \
    "T-HEAD TH1520 (4x C910 @1.85GHz, RV64GCV 0.7.1)"
M["SpacemiT K3 (A100 核, RV64GCV + RVV 1.0)"] = "SpacemiT K3 (A100 cores, RV64GCV + RVV 1.0)"
M["Zhihe A210 (4x C920 @2.3GHz + 4x C908, RV64GCV)"] = \
    "Zhihe A210 (4x C920 @2.3GHz + 4x C908, RV64GCV)"
M["Canaan K230 (C908 + KPU)"] = "Canaan K230 (C908 + KPU)"
M["ESWIN EIC7700X (4x SiFive P550 @1.8GHz, RV64GBCH)"] = \
    "ESWIN EIC7700X (4x SiFive P550 @1.8GHz, RV64GBCH)"
M["UltraRISC UR-DP1000 (8x RISC-V RV64GCBH)"] = "UltraRISC UR-DP1000 (8x RISC-V RV64GCBH)"
M["Sophgo SG2042 (64x XuanTie C920, RVV 0.7.1)"] = "Sophgo SG2042 (64x XuanTie C920, RVV 0.7.1)"
M["SpacemiT K1 (8x X60, RV64GCV + RVV 1.0)"] = "SpacemiT K1 (8x X60, RV64GCV + RVV 1.0)"
M["Sophgo CV1800B (C906 @1GHz, 64/256MB)"] = "Sophgo CV1800B (C906 @1GHz, 64/256MB)"

# ---- npu ----
M["无（纯模拟）"] = "None (emulation only)"
M["无 NPU"] = "No NPU"
M["无 NPU（仅有 GPU/视频编解码）"] = "No NPU (GPU/video codec only)"
M["4 TOPS@INT8，仅厂商闭源 HHB 工具链（int8/int16 定点），无上游开源驱动"] = \
    "4 TOPS@INT8, vendor closed-source HHB toolchain only (int8/int16 fixed point), no upstream open-source driver"
M["4 TOPS@INT8（TH1520），闭源 HHB 工具链"] = "4 TOPS@INT8 (TH1520), closed-source HHB toolchain"
M["K3 主打 CPU+AI 核（SpacemiT IME 扩展），无独立通用 NPU 编程模型；加速走 SpacemiT 私有指令与 AI SDK"] = \
    "K3 leans on CPU+AI cores (SpacemiT IME extensions) with no standalone general-purpose NPU programming model; acceleration goes through SpacemiT's proprietary instructions and AI SDK"
M["12 TOPS@INT8（支持 FP16/BF16/FP8），走厂商 TORQ-Toolkit 闭源工具链"] = \
    "12 TOPS@INT8 (supports FP16/BF16/FP8), via the vendor's closed-source TORQ-Toolkit"
M["KPU（约 1 TOPS 级），经 nncase 编译 kmodel，驱动为厂商 SDK（非上游）"] = \
    "KPU (about 1 TOPS class); kmodels are compiled with nncase, and the driver comes from the vendor SDK (not upstream)"
M["19.95 TOPS@INT8（INT16/FP16），闭源 ENNP SDK，但官方提供 Qwen2/DeepSeek-R1 样例"] = \
    "19.95 TOPS@INT8 (INT16/FP16) through the closed-source ENNP SDK, though official Qwen2/DeepSeek-R1 samples exist"
M["无板载 NPU；官方定位是靠 PCIe Gen4 x16 插独显/AI 加速卡"] = \
    "No onboard NPU; it is designed to take a GPU/AI accelerator over PCIe Gen4 x16"
M["无 NPU（纯 64 核 CPU）"] = "No NPU (64-core CPU only)"
M["无独立 NPU（K1 的 AI 能力走 SpacemiT 私有向量/AI 扩展）"] = \
    "No standalone NPU (K1's AI comes from SpacemiT's proprietary vector/AI extensions)"
M["无独立 NPU；AI 走 SpacemiT X60 的向量/AI 扩展与私有 AI SDK"] = \
    "No standalone NPU; AI runs on the X60's vector/AI extensions plus the proprietary AI SDK"
M["CVITEK TPU（约 0.5 TOPS），闭源 TDL SDK / cvitek 工具链"] = \
    "CVITEK TPU (about 0.5 TOPS) with the closed-source TDL SDK / cvitek toolchain"

# ---- note ----
M["仅用于无硬件时验证编译与功能，不能作为性能依据。"] = \
    "Only for validating compilation and functionality without hardware; it says nothing about performance."
M["ruyi 提供 OpenBSD/Ubuntu/openKylin/openWrt 镜像，生态老牌但无 AI 加速单元。"] = \
    "ruyi provides OpenBSD/Ubuntu/openKylin/openWrt images; a long-standing ecosystem, but with no AI accelerator."
M["最成熟的入门板之一（ruyi 提供 Armbian/openEIC/OpenBSD 镜像），但 SoC 无向量扩展，LLM 只能「能跑、很慢」。"] = \
    "One of the most mature starter boards (ruyi offers Armbian/openEIC/OpenBSD images), but the SoC has no vector extension, so LLMs are \"it runs, slowly\"."
M["CPU 跑 LLM 可行但慢（~6s/token）；NPU 只走 T-Head 闭源 HHB，不能跑 Transformer LLM。"] = \
    "Running an LLM on the CPU works but is slow (~6s/token); the NPU only has the closed T-Head HHB path and cannot run Transformer LLMs."
M["ruyi 可直接刷 RevyOS（含 4G/8G/16G uboot 包）；AI 现状与 LPi4A 一致。"] = \
    "ruyi can flash RevyOS directly (with 4G/8G/16G uboot packages); the AI situation matches the LPi4A."
M["目前 RISC-V SBC 里 AI 软件栈最完整的一档：上游 llama.cpp 直接内置其 kernel。"] = \
    "Currently the most complete AI software stack among RISC-V SBCs: upstream llama.cpp ships its kernels directly."
M["ruyi 已提供 zhihe-a210 的 Debian/buildroot 镜像，但 AI 侧只有厂商宣称，缺公开可复现实测。"] = \
    "ruyi already offers Debian/buildroot images for zhihe-a210, but on the AI side there are only vendor claims and no publicly reproducible benchmark."
M["典型的「视觉 AI 很强、LLM 不适合」的板：nncase 开源，但运行时仍绑定厂商 SDK。"] = \
    "A textbook \"strong at vision AI, unsuited to LLMs\" board: nncase is open source, but the runtime is still tied to the vendor SDK."
M["RISC-V 上少见的「NPU 能跑 LLM 且厂商给了样例」的板；代价是完全绑定 ESWIN 闭源栈。"] = \
    "Rare on RISC-V in that its NPU can run LLMs and the vendor ships samples; the cost is total lock-in to ESWIN's closed stack."
M["Mini-ITX 工作站定位（双 DDR4 ECC 最高 64GB、BMC），AI 要靠外接 PCIe 卡——但目前没有 RISC-V 上可用的公开 GPU/NPU 驱动栈证据。"] = \
    "Positioned as a Mini-ITX workstation (dual DDR4 ECC up to 64GB, BMC), so AI needs a PCIe card — but there is no public evidence of a working GPU/NPU driver stack on RISC-V yet."
M["唯一有大内存（最高 128GB）+ 64 核的 RISC-V 板，能跑 70B 级模型（内存够），但吞吐只有个位数 token/s。"] = \
    "The only RISC-V board with both large memory (up to 128GB) and 64 cores, so 70B-class models fit — but throughput is single-digit token/s."
M["ruyi 提供 armbian-orangepi-rv2-minimal 镜像；性价比最高的「能真跑 LLM」的板之一。"] = \
    "ruyi provides an armbian-orangepi-rv2-minimal image; one of the best value boards that genuinely runs LLMs."
M["当前「开了就能跑 LLM」的代表板：上游 llama.cpp + 厂商预编译包 + Bianbu 三者齐备。"] = \
    "The current poster board for \"LLMs that just run\": upstream llama.cpp, vendor prebuilt packages and Bianbu are all in place."
M["典型 MCU 级视觉板：能跑 YOLO 类小模型，完全不适合 LLM。"] = \
    "A classic MCU-class vision board: fine for small YOLO-style models, thoroughly unsuited to LLMs."

# ---- runs[].item ----
M["npu-sdk (HHB)"] = "npu-sdk (HHB)"
M["spacemit-llama.cpp (厂商)"] = "spacemit-llama.cpp (vendor)"
M["torq-toolkit (厂商)"] = "torq-toolkit (vendor)"
M["ennp-sdk (厂商)"] = "ennp-sdk (vendor)"
M["nncase + KPU"] = "nncase + KPU"
M["cvitek-tpu / tdl-sdk"] = "cvitek-tpu / tdl-sdk"

# ---- runs[].note ----
M["可用 qemu-riscv64 -cpu max,vlen=256 运行上游构建；SpacemiT 文档给出完整 qemu 跑 llama-cli 的命令。仅功能验证，速度无参考意义。"] = \
    "Upstream builds run with qemu-riscv64 -cpu max,vlen=256; SpacemiT's docs give the full command to run llama-cli in QEMU. Functional validation only — the speed means nothing."
M["build_riscv64.sh 依赖 qemu 做交叉编译产物验证；可跑但极慢。"] = \
    "build_riscv64.sh uses QEMU to validate cross-compiled artifacts; it runs, but very slowly."
M["RISE 轮子明确说明「非 QEMU 构建」，qemu 下仅能验证功能。"] = \
    "The RISE wheels explicitly say they are not built for QEMU; under QEMU you can only check that things work."
M["模拟环境可运行，无性能意义。"] = "Runs in emulation; performance figures are meaningless."
M["CI 在 riscv64 上跑通。"] = "CI passes on riscv64."
M["未找到 Unmatched 专项公开实测；上游仅提供源码（release 无 riscv64 二进制），U74 无 RVV，只能走标量路径，预期很慢。"] = \
    "No public Unmatched-specific benchmark found; upstream only ships source (no riscv64 binaries in releases), and U74 has no RVV, so it is scalar-only and expected to be slow."
M["上游含 MLAS RVV kernel 与 tools/scripts/build_riscv64.sh（SiFive 贡献），但无 riscv64 预编译包，需自行交叉编译；RVV kernel 面向 RVV 1.0。"] = \
    "Upstream includes an MLAS RVV kernel and tools/scripts/build_riscv64.sh (contributed by SiFive), but there are no riscv64 prebuilt packages, so cross-compile yourself; the RVV kernel targets RVV 1.0."
M["PyPI 无 riscv64 轮子；RISE 提供 torch 2.13.0 manylinux_2_39_riscv64 轮子（需 glibc≥2.39，如 Ubuntu 24.04/Bianbu）。"] = \
    "PyPI has no riscv64 wheels; RISE provides a torch 2.13.0 manylinux_2_39_riscv64 wheel (needs glibc >= 2.39, e.g. Ubuntu 24.04/Bianbu)."
M["上游 4.x 支持 RISC-V 与 RVV HAL；多数发行版可装或用 RVV 后端自编译。未逐板做性能验证。"] = \
    "Upstream 4.x supports RISC-V and the RVV HAL; most distros can install it or build it with the RVV backend. No per-board performance validation."
M["上游有 linux-riscv64 CI 与 RVV 实现；U74 无 RVV，ncnn 只能标量跑。"] = \
    "Upstream has linux-riscv64 CI and RVV implementations; U74 has no RVV, so ncnn runs scalar-only."
M["tengine-lite 提供 risc-v/lp64dv 的 RVV 卷积 kernel 与 rv64-c906 工具链，仅部分算子优化，属实验性支持。"] = \
    "tengine-lite provides RVV convolution kernels for risc-v/lp64dv and an rv64-c906 toolchain; only some operators are optimised, so support is experimental."
M["社区可编译运行，但 issue #14926 报告在 VF2 上出现 Illegal instruction，需正确设置 RVV/CPU 编译参数；无 V 扩展，纯标量推理，速度很低。"] = \
    "The community can build and run it, but issue #14926 reports Illegal instruction on the VF2, so set the RVV/CPU build flags correctly; with no V extension it is pure scalar inference and very slow."
M["上游有 linux-riscv64 CI 与 RVV 实现；JH7110 无 RVV，ncnn 标量运行。"] = \
    "Upstream has linux-riscv64 CI and RVV implementations; JH7110 has no RVV, so ncnn runs scalar-only."
M["Sipeed 官方 wiki 有 llama.cpp 章节：7B 模型约 6s/token（未用 V 扩展）。C910 是 RVV 0.7.1，上游 RVV 1.0 优化路径用不上，只能标量。"] = \
    "Sipeed's official wiki has a llama.cpp section: about 6s/token for a 7B model (without the V extension). C910 is RVV 0.7.1, so upstream's RVV 1.0 optimisation path does not apply and it stays scalar."
M["上游 riscv64 构建的 MLAS RVV kernel 面向 RVV 1.0，TH1520 的 0.7.1 向量无法直接用，需退回标量。"] = \
    "Upstream's riscv64 MLAS RVV kernel targets RVV 1.0; the TH1520's 0.7.1 vectors can't use it, so it falls back to scalar."
M["RISE 轮子要求 glibc≥2.39 且为 RVV 1.0 优化路径；RevyOS/Debian 上可装但无向量加速。"] = \
    "RISE wheels need glibc >= 2.39 and are optimised for RVV 1.0; they install on RevyOS/Debian but give no vector acceleration."
M["常规可用；RVV HAL 对 0.7.1 支持有限。"] = "Works as usual; the RVV HAL has limited 0.7.1 support."
M["可编译，RVV 优化面向 1.0，0.7.1 上退化为标量。"] = \
    "Builds, but the RVV optimisations target 1.0 and degrade to scalar on 0.7.1."
M["tengine-lite 自带 rv64-c906 toolchain 与 RVV 卷积 kernel，正是为 C906/C910 这类 0.7.1 核准备的，但仅覆盖部分算子。"] = \
    "tengine-lite ships an rv64-c906 toolchain and RVV convolution kernels built for 0.7.1 cores like the C906/C910, but only some operators are covered."
M["官方 wiki 给出 NPU 流程：T-Head HHB 编译器把 ONNX 编译成 NPU 可执行文件（int8/int16 定点），需专用 docker 镜像；闭源工具链，且只支持定点，不适合 LLM。"] = \
    "The official wiki documents the NPU flow: the T-Head HHB compiler turns ONNX into NPU executables (int8/int16 fixed point) inside a dedicated Docker image; the toolchain is closed source and fixed-point only, so it is unsuitable for LLMs."
M["与 LicheePi 4A 同为 TH1520，RevyOS 官方支持该板；llama.cpp 走同一 0.7.1 向量/标量路径（LPi4A 实测约 6s/token）。未找到 Meles 专项公开 benchmark。"] = \
    "Same TH1520 as the LicheePi 4A and officially supported by RevyOS; llama.cpp follows the same 0.7.1 vector/scalar path (about 6s/token measured on the LPi4A). No Meles-specific public benchmark found."
M["同 TH1520：上游 RVV kernel 面向 1.0，此处退化标量。"] = \
    "Same TH1520 story: upstream's RVV kernel targets 1.0, so it degrades to scalar here."
M["可装 RISE 轮子（RevyOS 基于 Debian），无向量加速。"] = \
    "RISE wheels install (RevyOS is Debian-based), with no vector acceleration."
M["常规可用。"] = "Works as usual."
M["可编译，RVV 优化在 0.7.1 上退化。"] = "Builds, with the RVV optimisations degrading on 0.7.1."
M["rv64-c906 工具链适配该类核，仅部分算子。"] = \
    "The rv64-c906 toolchain matches these cores, covering only some operators."
M["Milk-V 官方规格确认 4TOPS@INT8 NPU 支持 TensorFlow/ONNX/Caffe，但走 T-Head 闭源工具链，无开源驱动。"] = \
    "Milk-V's specs confirm a 4TOPS@INT8 NPU with TensorFlow/ONNX/Caffe support, but it goes through the closed T-Head toolchain with no open-source driver."
M["上游 llama.cpp 官方文档专章 build-riscv64-spacemit.md：A100 走 RISCV64_SPACEMIT_IME2，实测 qwen3 0.6B Q4_0 达 pp128 565.8 / tg128 55.8 t/s，qwen3 4B Q4_0 达 pp128 79.7 / tg128 11.3 t/s（8 线程）。"] = \
    "Upstream llama.cpp has a dedicated build-riscv64-spacemit.md: A100 cores use RISCV64_SPACEMIT_IME2, and the measured qwen3 0.6B Q4_0 reaches pp128 565.8 / tg128 55.8 t/s while qwen3 4B Q4_0 reaches pp128 79.7 / tg128 11.3 t/s (8 threads)."
M["SpacemiT 提供预编译 spacemit-llama.cpp.riscv64（已到 0.0.9），配 archive.spacemit.com 模型库；Bit-Brick 文档给出 llama-cli/llama-server 用法。"] = \
    "SpacemiT ships a prebuilt spacemit-llama.cpp.riscv64 (now 0.0.9) with the model library on archive.spacemit.com; Bit-Brick's docs show llama-cli/llama-server usage."
M["RVV 1.0 核可吃满上游 MLAS RVV kernel，需自行编译。"] = \
    "The RVV 1.0 cores fully use upstream's MLAS RVV kernel, but you must build it yourself."
M["Bianbu 等 glibc≥2.39 的发行版可直接装 RISE 的 torch 2.13.0 riscv64 轮子（轮子为 manylinux_2_39_riscv64）。"] = \
    "glibc >= 2.39 distros such as Bianbu can install RISE's torch 2.13.0 riscv64 wheel directly (it is manylinux_2_39_riscv64)."
M["RVV 1.0 + RVV HAL，属最佳组合。"] = "RVV 1.0 plus the RVV HAL — the best combination."
M["RVV 1.0，上游 CI 覆盖。"] = "RVV 1.0, covered by upstream CI."
M["可用，但优化针对 0.7.1 C906，1.0 上收益有限。"] = \
    "Works, but the optimisations target the 0.7.1 C906 and give little on 1.0."
M["archive.spacemit.com/spacemit-ai/ 提供 ModelZoo、llama.cpp、localai、dify 等制品，是当前 RISC-V 上最完整的厂商 AI 栈之一。"] = \
    "archive.spacemit.com/spacemit-ai/ offers ModelZoo, llama.cpp, localai, dify and more — one of the most complete vendor AI stacks on RISC-V today."
M["未找到 A210 上 llama.cpp 的公开实测；C920 为 RVV 0.7.1，上游 1.0 优化路径不可用。"] = \
    "No public llama.cpp benchmark on the A210; the C920 is RVV 0.7.1, so upstream's 1.0 optimisation path is unavailable."
M["未找到该板公开证据（芯片较新，2026 年才 upstream 支持）。"] = \
    "No public evidence for this board (the chip is new, with upstream support only in 2026)."
M["未找到该板公开证据。"] = "No public evidence for this board."
M["RVV 0.7.1，仅标量/有限向量路径；未见该板实测。"] = \
    "RVV 0.7.1, so scalar/limited vector only; no benchmarks for this board."
M["CNX 报道：官方 Linux SDK + TORQ-Toolkit 做模型转换与部署，NPU 支持 INT4/INT8/INT16/FP8/FP16/BF16，宣称 DeepSeek-7B 达 8 tok/s；工具链闭源、文档未公开可得。"] = \
    "CNX reports: the official Linux SDK plus TORQ-Toolkit handle model conversion and deployment, the NPU supports INT4/INT8/INT16/FP8/FP16/BF16, and DeepSeek-7B is claimed at 8 tok/s; the toolchain is closed and its docs are not publicly available."
M["K230 面向视觉推理（KPU），未找到 llama.cpp 公开实测；内存 512MB/1GB 级，LLM 不现实。"] = \
    "The K230 targets vision inference (KPU) and no public llama.cpp benchmark exists; with 512MB/1GB of RAM an LLM is unrealistic."
M["未找到公开证据（官方主推 nncase）。"] = "No public evidence (the vendor pushes nncase)."
M["未找到公开证据；训练侧不适用。"] = "No public evidence; not applicable for training."
M["CanMV/K230 SDK 自带图像处理与摄像头链路，OpenCV 风格 API 可用。"] = \
    "The CanMV/K230 SDK includes image processing and a camera pipeline, and OpenCV-style APIs work."
M["未找到公开证据。"] = "No public evidence."
M["kendryte/nncase 是官方开源深度学习编译器，把 ONNX/TFLite 编译为 KPU kmodel；K230 SDK 文档给出完整 AI 开发流程。"] = \
    "kendryte/nncase is the official open-source deep-learning compiler that turns ONNX/TFLite into KPU kmodels; the K230 SDK docs cover the whole AI workflow."
M["P550 无 RVV，未找到 Megrez 上 llama.cpp 的公开实测；官方 AI 路径是 NPU 而非 CPU。"] = \
    "The P550 has no RVV and there is no public llama.cpp benchmark on the Megrez; the official AI path is the NPU, not the CPU."
M["无 RVV，标量路径；RockOS 可装但无公开 benchmark。"] = \
    "No RVV, so scalar only; RockOS can install it but there is no public benchmark."
M["ESWIN ENNP 平台（闭源）提供 EsQuant 量化、EsAAC 编译、EsSimulator 仿真；官方 runtime sample 直接给出 Qwen2 与 DeepSeek-R1 在 NPU 上的示例（apt install es-sdk-sample-npu-qwen，模型 ZIFENG278/Qwen2-0.5B_ENNP）。"] = \
    "The ESWIN ENNP platform (closed source) provides EsQuant quantisation, EsAAC compilation and EsSimulator emulation; the official runtime sample gives Qwen2 and DeepSeek-R1 examples on the NPU (apt install es-sdk-sample-npu-qwen, model ZIFENG278/Qwen2-0.5B_ENNP)."
M["未找到 Titan 上 llama.cpp 的公开实测；板子新、出货少。"] = \
    "No public llama.cpp benchmark on the Titan; the board is new and ships in small numbers."
M["无 RVV，标量路径；无公开实测。"] = "No RVV, so scalar only; no public benchmark."
M["arXiv 2503.17422 (V-Seek) 在 SG2042 上做 LLM 推理优化：DeepSeek R1 Distill Llama 8B / QWEN 14B 达 4.32 / 2.29 token/s 生成、6.54 / 3.68 token/s prefill。Milk-V 官方另有 InferLLM 文档。"] = \
    "arXiv 2503.17422 (V-Seek) optimises LLM inference on the SG2042: DeepSeek R1 Distill Llama 8B / QWEN 14B reach 4.32 / 2.29 token/s generation and 6.54 / 3.68 token/s prefill. Milk-V also has its own InferLLM docs."
M["64 核可并行，但 RVV 0.7.1 无法用上游 1.0 kernel。"] = \
    "64 cores run in parallel, but RVV 0.7.1 can't use upstream's 1.0 kernel."
M["可装 RISE 轮子；无 0.7.1 向量加速。"] = "RISE wheels install, but there is no 0.7.1 vector acceleration."
M["多核标量可用。"] = "Multi-core scalar works."
M["可编译，0.7.1 上退化标量。"] = "Builds, degrading to scalar on 0.7.1."
M["rv64-c906 kernel 适配 0.7.1，仅部分算子。"] = \
    "The rv64-c906 kernel targets 0.7.1, covering only some operators."
M["Milk-V 官方文档提供 InferLLM（MegEngine）在 Pioneer 上的部署说明。"] = \
    "Milk-V's docs cover deploying InferLLM (MegEngine) on the Pioneer."
M["X60 与 BPI-F3 同核，上游 build-riscv64-spacemit.md 给出 X60 实测表（qwen3 0.6B Q4_0: pp128 49.15 / tg128 11.73 t/s）；另有 Orange Pi RV2 上的 llama.cpp 实验仓库。"] = \
    "The X60 is the same core as the BPI-F3; upstream's build-riscv64-spacemit.md has an X60 results table (qwen3 0.6B Q4_0: pp128 49.15 / tg128 11.73 t/s). There is also an experimental llama.cpp repo for the Orange Pi RV2."
M["可用 SpacemiT 预编译包（K1 同源）。"] = "SpacemiT's prebuilt packages work (same K1 silicon)."
M["RVV 1.0，上游 kernel 可用。"] = "RVV 1.0, upstream kernel usable."
M["glibc≥2.39（如 Ubuntu 24.04 / 新版 Armbian）可装 RISE 轮子；旧镜像 glibc 不足。"] = \
    "glibc >= 2.39 (e.g. Ubuntu 24.04 / recent Armbian) can install RISE wheels; older images have too old a glibc."
M["RVV 1.0 + RVV HAL。"] = "RVV 1.0 plus the RVV HAL."
M["可用，优化非 1.0 专用。"] = "Works; the optimisations are not 1.0-specific."
M["上游 llama.cpp 官方 riscv64-spacemit 文档给出 X60（K1）实测表与量化支持矩阵（Q4_0/Q4_1/Q4_K/Q8_0 可用）；Bit-Brick 官方文档给出 Bianbu 上的完整用法。"] = \
    "Upstream llama.cpp's riscv64-spacemit docs give a measured X60 (K1) table and a quantisation support matrix (Q4_0/Q4_1/Q4_K/Q8_0 work); Bit-Brick's docs cover full usage on Bianbu."
M["SpacemiT 预编译 spacemit-llama.cpp.riscv64.0.0.4+（archive 上已到 0.0.9），支持 llama-cli / llama-server / OpenAI 兼容 API。"] = \
    "SpacemiT's prebuilt spacemit-llama.cpp.riscv64.0.0.4+ (0.0.9 on the archive) supports llama-cli / llama-server / an OpenAI-compatible API."
M["RVV 1.0，上游 MLAS RVV kernel 可用（需自编译）。"] = \
    "RVV 1.0, upstream MLAS RVV kernel works (self-built)."
M["Bianbu 等 glibc≥2.39 发行版可装 RISE torch 2.13.0 riscv64 轮子（manylinux_2_39_riscv64）。"] = \
    "glibc >= 2.39 distros such as Bianbu can install the RISE torch 2.13.0 riscv64 wheel (manylinux_2_39_riscv64)."
M["RVV 1.0，OpenCV RVV HAL 生效。"] = "RVV 1.0, the OpenCV RVV HAL is active."
M["可用但非最优。"] = "Works, but not optimal."
M["SpacemiT AI 制品库（ModelZoo/llama.cpp/localai/dify）可直接取用。"] = \
    "SpacemiT's AI artifact repository (ModelZoo/llama.cpp/localai/dify) is ready to use."
M["内存 64MB/256MB 级，无 RVV、无 FPU 性能余量，不具备实际 LLM 可行性；未找到任何公开跑通记录。"] = \
    "With 64MB/256MB of RAM, no RVV and no FPU headroom, LLMs are not practically feasible; no public success report was found."
M["内存与算力不足，官方 AI 路径是 TPU 而非通用 runtime。"] = \
    "Not enough memory or compute; the official AI path is the TPU rather than a general runtime."
M["不适用。"] = "Not applicable."
M["可做基础图像处理，但内存受限，官方示例走 TDL SDK。"] = \
    "Basic image processing works, but memory is limited and the official samples go through the TDL SDK."
M["未找到公开证据（内存不足以加载常见模型）。"] = \
    "No public evidence (not enough memory to load common models)."
M["Milk-V 官方文档：Duo 系列 SoC 内置 CVITEK TPU，推荐用 TDL SDK；提供 YOLOv5/v8/11/12、MobileNetV2、ResNet18 等样例。闭源 TPU 栈。"] = \
    "Milk-V's docs: the Duo series SoCs include a CVITEK TPU and the TDL SDK is recommended; YOLOv5/v8/11/12, MobileNetV2, ResNet18 and other samples are provided. The TPU stack is closed source."

M["Orange Pi RV2（Ky X1）"] = "Orange Pi RV2 (Ky X1)"
M["Banana Pi BPI-F3（SpacemiT K1）"] = "Banana Pi BPI-F3 (SpacemiT K1)"
