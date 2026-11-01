# -*- coding: utf-8 -*-
"""boards.yaml: name / soc / spec / price_note / forms 的英译。"""

M = {}

# ---- name ----
M["QEMU virt 虚拟机型"] = "QEMU virt (virtual machine)"
M["荔枝派 4A（LicheePi 4A）"] = "LicheePi 4A"
M["进迭时空 SpacemiT K3（Pico-ITX / CoM260）"] = "SpacemiT K3 (Pico-ITX / CoM260)"
M["知合计算 A210（玄铁 MelonPi 开发板）"] = "Zhihe A210 (XuanTie MelonPi dev board)"
M["嘉楠 Canaan K230（Kendryte K230 / CanMV-K230）"] = "Canaan K230 (Kendryte K230 / CanMV-K230)"
M["Milk-V Megrez（ESWIN EIC7700X）"] = "Milk-V Megrez (ESWIN EIC7700X)"
M["Milk-V Titan（UltraRISC DP1000）"] = "Milk-V Titan (UltraRISC DP1000)"
M["Banana Pi BPI-F3（SpacemiT K1）"] = "Banana Pi BPI-F3 (SpacemiT K1)"
M["Orange Pi RV2（Ky X1）"] = "Orange Pi RV2 (Ky X1)"
M["StarFive VisionFive 2 Lite（JH7110S）"] = "StarFive VisionFive 2 Lite (JH7110S)"
M["Milk-V Pioneer（SG2042 服务器向）"] = "Milk-V Pioneer (SG2042, server-oriented)"
M["Milk-V Duo 系列（Duo / Duo 256M / Duo S）"] = "Milk-V Duo series (Duo / Duo 256M / Duo S)"

# ---- soc ----
M["无（QEMU 通用虚拟平台，可配 RV32/RV64，最多 512 核）"] = \
    "None (generic QEMU virtual platform, RV32/RV64 configurable, up to 512 cores)"
M["StarFive JH7110：4×SiFive U74 @1.5GHz + S7 监控核 + E24"] = \
    "StarFive JH7110: 4×SiFive U74 @1.5GHz + S7 monitor core + E24"
M["T-Head TH1520：4×C910 @1.85GHz + C906 + E902，4TOPS NPU"] = \
    "T-Head TH1520: 4×C910 @1.85GHz + C906 + E902, 4TOPS NPU"
M["SpacemiT K3（Key Stone K3）"] = "SpacemiT K3 (Key Stone K3)"
M["ZHIHE A210（4×C920 + 4×C908）"] = "ZHIHE A210 (4×C920 + 4×C908)"
M["Kendryte K230（2×C908）"] = "Kendryte K230 (2×C908)"
M["SiFive Freedom U740 (FU740)：4×U74 @1.2GHz + 1×S71 监控核"] = \
    "SiFive Freedom U740 (FU740): 4×U74 @1.2GHz + 1×S71 monitor core"
M["SpacemiT K1（8×X60）"] = "SpacemiT K1 (8×X60)"
M["Ky X1（8 核 RISC-V AI CPU）"] = "Ky X1 (8-core RISC-V AI CPU)"
M["T-Head TH1520：4×C910 @1.85GHz，4TOPS NPU，BXM-4-64 GPU"] = \
    "T-Head TH1520: 4×C910 @1.85GHz, 4TOPS NPU, BXM-4-64 GPU"
M["SOPHON SG2042：64×XuanTie C920 @2GHz，RVV 0.71，64MB L3"] = \
    "SOPHON SG2042: 64×XuanTie C920 @2GHz, RVV 0.71, 64MB L3"
M["CV1800B（Duo）/ SG2002（Duo 256M）/ SG2000（Duo S）"] = \
    "CV1800B (Duo) / SG2002 (Duo 256M) / SG2000 (Duo S)"

# ---- spec ----
M["纯虚拟平台：最多 512 个 RV64GC 核、CLINT/PLIC、PCIe 主机桥、8 个 virtio-mmio、NS16550 UART、可选 AIA/IOMMU；内存、磁盘、网络全部由命令行参数虚拟，无真实 GPU/VPU/NPU。"] = \
    "Pure virtual platform: up to 512 RV64GC cores, CLINT/PLIC, a PCIe host bridge, 8 virtio-mmio devices, NS16550 UART, optional AIA/IOMMU; memory, disks and networking are all virtualised through command-line options, with no real GPU/VPU/NPU."
M["2/4/8GB LPDDR4，microSD + eMMC（部分版本）、M.2 M-Key NVMe、2×千兆网（v1.3 支持 PoE）、HDMI 2.0、4×USB、40-pin GPIO；另有精简版 VisionFive 2 Lite。"] = \
    "2/4/8GB LPDDR4, microSD + eMMC (some versions), M.2 M-Key NVMe, 2× GbE (v1.3 supports PoE), HDMI 2.0, 4× USB, 40-pin GPIO; there is also a cut-down VisionFive 2 Lite."
M["4/8/16GB LPDDR4X，8/32/128GB eMMC，2×千兆网，WiFi5/BT5，HDMI 2.0 + 4-lane MIPI DSI，2×MIPI CSI，4×USB3，40-pin GPIO。"] = \
    "4/8/16GB LPDDR4X, 8/32/128GB eMMC, 2× GbE, WiFi5/BT5, HDMI 2.0 + 4-lane MIPI DSI, 2× MIPI CSI, 4× USB3, 40-pin GPIO."
M["4/8/16GB LPDDR4X 4266MT/s，eMMC 插槽（选配模块）+ microSD，1×千兆网（支持 PoE），WiFi5/BT5.2（AP6256），4×USB3.0，HDMI 2.0 4K60，MIPI DSI/CSI，40-pin，信用卡大小。"] = \
    "4/8/16GB LPDDR4X 4266MT/s, eMMC socket (optional module) + microSD, 1× GbE (PoE capable), WiFi5/BT5.2 (AP6256), 4× USB3.0, HDMI 2.0 4K60, MIPI DSI/CSI, 40-pin, credit-card sized."
M["8×X100@2.4GHz + 8×A100 AI 核，RVA23/RVV1.0（最高 1024bit），60 TOPS 通用 AI 算力，130 KDMIPS。Pico-ITX：16/32GB LPDDR5-6400、UFS2.2 128/256GB、10GbE SFP+ + 1GbE、2×M.2（M-Key Gen3 x4 / B-Key）、2×USB3.2 Type-C（含全功能 65W PD + 4K DP）+ 4×USB2.0、100×86mm。CoM260：260pin 核心板 + 参考载板，载板与 Jetson Orin Nano 硬件兼容。"] = \
    "8× X100 @2.4GHz + 8× A100 AI cores, RVA23/RVV1.0 (up to 1024-bit), 60 TOPS general AI compute, 130 KDMIPS. Pico-ITX: 16/32GB LPDDR5-6400, UFS2.2 128/256GB, 10GbE SFP+ + 1GbE, 2× M.2 (M-Key Gen3 x4 / B-Key), 2× USB3.2 Type-C (full-featured 65W PD + 4K DP) + 4× USB2.0, 100×86mm. CoM260: a 260-pin compute module plus a reference carrier board, the carrier being hardware-compatible with Jetson Orin Nano."
M["8 核 64 位 RISC-V：4×C920@1.9GHz + 4×C908@1.9GHz，均支持 RVV（128bit）；NPU 12 TOPS@INT8，支持 INT4/INT8/FP8/FP16/BF16 与 Transformer；LPDDR4X 最大 16GB；eMMC5.1；H.265 解码 4K@120fps；板卡为 SODIMM 核心板 + V1/V2/V3 开源底板，8GB LPDDR4X + 32GB eMMC（第三方项目页数据）"] = \
    "8-core 64-bit RISC-V: 4× C920 @1.9GHz + 4× C908 @1.9GHz, all with RVV (128-bit); NPU 12 TOPS@INT8 supporting INT4/INT8/FP8/FP16/BF16 and Transformers; LPDDR4X up to 16GB; eMMC5.1; H.265 decode 4K@120fps; the board is a SODIMM compute module plus V1/V2/V3 open carrier boards, 8GB LPDDR4X + 32GB eMMC (figures from a third-party project page)"
M["双核 64 位 RISC-V C908：大核 1.6GHz 带 RVV1.0，小核 0.8GHz；KPU 6 TOPS 等效算力（INT8/INT16）（K230D 为 1 TOPS）；CanMV-K230 板载 512MB LPDDR4、microSD、HDMI、3×MIPI-CSI、USB；整芯片典型功耗约 2W"] = \
    "Dual-core 64-bit RISC-V C908: big core 1.6GHz with RVV1.0, little core 0.8GHz; KPU rated at 6 TOPS equivalent (INT8/INT16) (1 TOPS on the K230D); the CanMV-K230 board carries 512MB LPDDR4, microSD, HDMI, 3× MIPI-CSI and USB; typical chip power is about 2W"
M["4×SiFive P550@1.8GHz（RV64GBCH，出厂默认 1.4GHz/800mV）；19.95 TOPS@INT8 NPU；IMG AXM-8-256 GPU（OpenGL ES3.2/Vulkan1.2/OpenCL）；8/16/32GB LPDDR5-6400；Mini-ITX 170×170mm；PCIe x8 槽（Gen3 x4）、2×GbE、4×USB3、SATA/M.2 SATA、8K H.265 编解码"] = \
    "4× SiFive P550 @1.8GHz (RV64GBCH, ships at 1.4GHz/800mV); 19.95 TOPS@INT8 NPU; IMG AXM-8-256 GPU (OpenGL ES3.2/Vulkan1.2/OpenCL); 8/16/32GB LPDDR5-6400; Mini-ITX 170×170mm; PCIe x8 slot (Gen3 x4), 2× GbE, 4× USB3, SATA/M.2 SATA, 8K H.265 encode/decode"
M["8×UR-CP100@2.0GHz，RV64GCBHX（RVA22 完整，缺 V 扩展）；最高 64GB DDR4 UDIMM（支持 ECC）；PCIe Gen4 x16、NVMe Gen4 x4、2×GbE、USB3；Mini-ITX；UEFI+ACPI+SMBIOS；可选 BMC 模块；无板载显示输出"] = \
    "8× UR-CP100 @2.0GHz, RV64GCBHX (full RVA22, no V extension); up to 64GB DDR4 UDIMM (ECC supported); PCIe Gen4 x16, NVMe Gen4 x4, 2× GbE, USB3; Mini-ITX; UEFI+ACPI+SMBIOS; optional BMC module; no onboard display output"
M["16GB DDR4 板载，PCIe x16（可插显卡/NVMe）、M.2 Key M、M.2 Key E（WiFi）、千兆网、4×USB 3.0、microSD、SPI Flash；microATX 板型，12V 桶形供电。"] = \
    "16GB DDR4 onboard, PCIe x16 (for a GPU/NVMe), M.2 Key M, M.2 Key E (WiFi), GbE, 4× USB 3.0, microSD, SPI Flash; microATX form factor with 12V barrel power."
M["8×X60（RV64GCVB，RVA22，RVV1.0），2.0 TOPS；IMG BXE-2-32 GPU@819MHz；2/4/8/16GB LPDDR4；8/16/32/128GB eMMC；2×GbE、4×USB3.0、HDMI1.4（1080p）、PCIe2.1（M.2 M-Key + mini PCIe）、WiFi6/BT5.2；148×100mm"] = \
    "8× X60 (RV64GCVB, RVA22, RVV1.0), 2.0 TOPS; IMG BXE-2-32 GPU @819MHz; 2/4/8/16GB LPDDR4; 8/16/32/128GB eMMC; 2× GbE, 4× USB3.0, HDMI1.4 (1080p), PCIe2.1 (M.2 M-Key + mini PCIe), WiFi6/BT5.2; 148×100mm"
M["8 核 64 位 RISC-V（单核性能约 Cortex-A55 的 1.3 倍），2 TOPS CPU 融合算力（无独立 NPU）；2/4/8GB LPDDR4X；eMMC 模块 16–128GB 可选；2×M.2 M-Key（PCIe2.0 x2，支持 NVMe）、2×GbE、WiFi5/BT5、3×USB3+2×USB2、HDMI、89×56mm"] = \
    "8-core 64-bit RISC-V (single-core performance about 1.3× a Cortex-A55), 2 TOPS fused CPU compute (no dedicated NPU); 2/4/8GB LPDDR4X; optional 16–128GB eMMC module; 2× M.2 M-Key (PCIe2.0 x2, NVMe capable), 2× GbE, WiFi5/BT5, 3× USB3 + 2× USB2, HDMI, 89×56mm"
M["4×SiFive P550@1.4GHz（乱序）；16/32GB LPDDR5-6400 + 128GB eMMC；20 TOPS NPU；Imagination GPU；Mini-DTX；PCIe Gen3 x4（x16 槽）、2×GbE、5×USB3、SATA；Ubuntu 24.04 预装（6.6 内核，支持 OTA）"] = \
    "4× SiFive P550 @1.4GHz (out-of-order); 16/32GB LPDDR5-6400 + 128GB eMMC; 20 TOPS NPU; Imagination GPU; Mini-DTX; PCIe Gen3 x4 (x16 slot), 2× GbE, 5× USB3, SATA; Ubuntu 24.04 preinstalled (6.6 kernel, OTA supported)"
M["4×RV64GC@1.25GHz + IMG BXE-4-32 MC1 GPU；2/4/8GB LPDDR4；WiFi6/BT5.4；M.2（PCIe2.0 x1）、GbE、USB2.0/3.0、HDMI 4K@60、40pin GPIO、MIPI-CSI/DSI；microSD/eMMC"] = \
    "4× RV64GC @1.25GHz + IMG BXE-4-32 MC1 GPU; 2/4/8GB LPDDR4; WiFi6/BT5.4; M.2 (PCIe2.0 x1), GbE, USB2.0/3.0, HDMI 4K@60, 40-pin GPIO, MIPI-CSI/DSI; microSD/eMMC"
M["4GB LPDDR4，16GB eMMC（板载），WiFi5/BT5（AP6203BM），千兆网，microHDMI，microSD，2×CSI + 1×DSI，mikroBUS，BeagleBone Black cape 排针。"] = \
    "4GB LPDDR4, 16GB onboard eMMC, WiFi5/BT5 (AP6203BM), GbE, microHDMI, microSD, 2× CSI + 1× DSI, mikroBUS, BeagleBone Black cape headers."
M["4×DDR4 DIMM 最高 128GB（ECC RDIMM/UDIMM），3×PCIe x16（Gen3 x8 信号）、5×SATA、2×2.5GbE、8×USB3、2×M.2、eMMC 模块接口、microSD；mATX 24.4×24.4cm，标准 24-pin ATX 供电，典型功耗 120W。"] = \
    "4× DDR4 DIMM up to 128GB (ECC RDIMM/UDIMM), 3× PCIe x16 (Gen3 x8 signalling), 5× SATA, 2× 2.5GbE, 8× USB3, 2× M.2, an eMMC module connector, microSD; mATX 24.4×24.4cm with standard 24-pin ATX power, 120W typical."
M["Duo：2×C906（1GHz+700MHz）+8051，64MB SIP DRAM；Duo 256M：SG2002 加 1×Cortex-A53，256MB；Duo S：512MB + eMMC 焊盘（部分套装带 8GB）+ WiFi6；均有 100M 网口、USB-C；Duo/256M 为 26×GPIO 焊盘、21×51mm，Duo S 为 2×26-pin 排针、43×43mm。"] = \
    "Duo: 2× C906 (1GHz + 700MHz) + an 8051, 64MB SIP DRAM; Duo 256M: SG2002 plus 1× Cortex-A53, 256MB; Duo S: 512MB + eMMC pads (some kits ship 8GB) + WiFi6; all have a 100M Ethernet port and USB-C; Duo/256M are 26-pin GPIO pads at 21×51mm, Duo S has 2× 26-pin headers at 43×43mm."

# ---- price_note ----
M["免费开源（GPLv2），随各发行版软件源提供"] = \
    "Free and open source (GPLv2), available from every distro's package repos"
M["标准版 2/4/8GB 约 US$60–120（未核实）；VisionFive 2 Lite 渠道实价 US$99.95"] = \
    "Standard 2/4/8GB around US$60–120 (unverified); the VisionFive 2 Lite sells for US$99.95 at retail"
M["8GB 约 US$120、16GB 约 US$180（渠道报价，未核实）"] = \
    "About US$120 for 8GB and US$180 for 16GB (reseller quotes, unverified)"
M["8GB 约 US$90–110（未核实）"] = "8GB around US$90–110 (unverified)"
M["Sipeed 首发价 Pico-ITX 8GB $299、CoM260 套件 $309；32GB/128GB 渠道价 $595–889（Firefly 出货，TinyComputers 评测含税$1175）；国内 Milk-V Jupiter2 8GB 预售约 ¥1799。渠道与关税差异大，属媒体/渠道报价。"] = \
    "Sipeed launch prices: Pico-ITX 8GB $299, CoM260 kit $309; reseller prices for 32GB/128GB run $595–889 (Firefly listings; TinyComputers' review came to $1175 with tax); the domestic Milk-V Jupiter2 8GB pre-order was about ¥1799. Reseller and duty differences are large — these are media/reseller quotes."
M["未公开零售价，开发板主要经玄铁 RV 学院/华秋开源硬件等项目渠道获取，未查到公开报价"] = \
    "No public retail price; boards come mainly through programme channels such as the XuanTie RV Academy and Huaqiu open hardware, and no public quote was found"
M["CanMV-K230 约 $40–60（AliExpress/Newegg 等渠道）；01Studio 套件 $49–88；官方无公开定价（渠道报价）"] = \
    "CanMV-K230 about $40–60 (AliExpress/Newegg and similar); 01Studio kits $49–88; no official list price (reseller quotes)"
M["2024 首发 $199（16GB）/ $269（32GB，Arace）；当前官网仅留 Contact us，无公开零售链接"] = \
    "Launched in 2024 at $199 (16GB) / $269 (32GB, Arace); the site now only offers Contact us with no public retail link"
M["$329（Arace 标准/预售价）；2025 年预购期曾有 $279 档与 $50 抵扣券（媒体）"] = \
    "$329 (Arace standard/pre-order price); during the 2025 pre-order there was a $279 tier plus a $50 voucher (media)"
M["官方页面已标 Discontinued 且无定价；2024 年清库存曾降至 US$299，现以二手为主（价格未核实）"] = \
    "The official page is marked Discontinued with no price; clearance in 2024 dropped to US$299, and second-hand is now the main source (price unverified)"
M["AliExpress/Banana Pi 店铺约 $68（低配）–$190（16GB/128GB）；按内存与 eMMC 配置差异大（渠道报价）"] = \
    "About $68 (base) to $190 (16GB/128GB) at AliExpress/Banana Pi stores; prices vary a lot with RAM and eMMC (reseller quotes)"
M["$30（2GB）起，4GB/8GB 约 $40/$50（媒体与渠道）；AliExpress/Amazon/淘宝有售"] = \
    "From $30 (2GB), about $40/$50 for 4GB/8GB (media and resellers); sold on AliExpress/Amazon/Taobao"
M["Arrow 报价：16GB $381.43、32GB $485.84（2026-11 搜索快照，商品页未直连验证）；早期上市价 $399/$499"] = \
    "Arrow quotes: 16GB $381.43, 32GB $485.84 (search snapshot 2026-11, product page not verified directly); early list prices were $399/$499"
M["Kickstarter 众筹 $19.90 起；零售约 $23（2GB）/ $30（4GB）/ $37（8GB）（Liliputing/CNX，媒体价）"] = \
    "Kickstarter from $19.90; retail about $23 (2GB) / $30 (4GB) / $37 (8GB) (Liliputing/CNX, media prices)"
M["首发约 US$150（BeagleBoard 论坛），现渠道价约 US$160–190（未核实）"] = \
    "Launched around US$150 (BeagleBoard forum); resellers now ask about US$160–190 (unverified)"
M["众筹价：主板 US$1,199（不含 CPU US$899），Pioneer Box 整机 US$1,999；现价需询价（未核实）"] = \
    "Crowdfunding: board US$1,199 (US$899 without CPU), Pioneer Box complete system US$1,999; current pricing is quote-only (unverified)"
M["Duo US$4.99、Duo S US$9.99（Arace 官方店实价）；Duo 256M 约 US$7.99"] = \
    "Duo US$4.99 and Duo S US$9.99 (actual Arace store prices); Duo 256M about US$7.99"

# ---- forms ----
M["CoM260（任务中的 SOM260）"] = "CoM260 (also called SOM260)"
M["SODIMM 核心板 + V3 底板"] = "SODIMM compute module + V3 carrier"
M["A210 算力棒（Dongle）"] = "A210 compute stick (dongle)"
M["单板 SBC"] = "Single-board computer (SBC)"
M["BPI-CM6 核心板"] = "BPI-CM6 compute module"

# ---- vendor ----
M["SpacemiT 进迭时空"] = "SpacemiT"
M["知合计算 Zhihe Computing（板卡品牌：玄铁 MelonPi）"] = \
    "Zhihe Computing (board brand: XuanTie MelonPi)"
M["Canaan 嘉楠科技"] = "Canaan"
M["Milk-V（芯片 ESWIN 奕斯伟）"] = "Milk-V (chip: ESWIN)"
M["Milk-V（芯片超睿 UltraRISC）"] = "Milk-V (chip: UltraRISC)"
M["Banana Pi 香蕉派（芯片 SpacemiT）"] = "Banana Pi (chip: SpacemiT)"
M["香橙派 Orange Pi"] = "Orange Pi"
M["StarFive 赛昉科技"] = "StarFive"
M["BPI-K230D-ZERO（K230D）"] = "BPI-K230D-ZERO (K230D)"
