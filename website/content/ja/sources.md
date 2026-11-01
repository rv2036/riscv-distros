---
title: "出典と謝辞"
sub: "本サイトの各結論の出典、判定方法、そして謝辞"
layout: sources
---

**このサイトの技術的な結論は、どれも出典までたどれるようにしています。** 以下では「一次情報 / 二次情報」に分けてすべての出典を並べ、各結論をどう判定したかを説明します。サイトのデータは毎日 1 回自動で確認しており、各項目には確認日が付いています。

## 1. テスト結果の出典：RuyiSDK サポートマトリクス

サイト内の「あるシステムがあるボードで実測で使える / 使えない」という結論は、**まず RuyiSDK 公式のテストマトリクスを根拠にしています**：

- サイト：<https://matrix.ruyisdk.org/>
- ソースリポジトリ（データ本体。ボード × システムごとに 1 つの markdown + YAML front matter）：<https://github.com/ruyisdk/support-matrix>
- データの取得方法：当サイトは毎日このリポジトリを取得し、各テストレポートの `sys / sys_ver / sys_var / status / last_update` フィールドを解析して、サイト内の「ボード × ディストロ」の組み合わせに対応付けています
- 各レポートのリンクは `https://matrix.ruyisdk.org/reports/<ボード>/<システム>/<バリアント>/` の形式です。サイト内のマトリクスのセルや、ディストロ / ボードページにある「RuyiSDK 実測レポート」の表から、そのまま原文へ飛べます

**謝辞**：RuyiSDK チームと PLCT ラボ（中国科学院ソフトウェア研究所）が、このボードごとの実測データを長期にわたって維持してくれています。RISC-V エコシステムでは珍しい、検証可能な第三者テストセットです。当サイトはこれをそのまま採用し、車輪の再発明はしていません。

### ステータス列挙の定義（同リポジトリの CONTRIBUTING.md より）

| 状態 | 意味 |
| --- | --- |
| `good` | 完全に利用可能。デスクトップ環境まで使えます |
| `basic` | 基本的に利用可能。起動でき、シリアル経由で使えます |
| `part` | 一部の機能だけが使えます |
| `cft` | イメージは入手できますが、実機でのさらなる検証が必要です |
| `cfh` | 公式ドキュメントやコミュニティは対応をうたっていますが、実測では起動に失敗します |
| `cfi` | 公式ドキュメントは対応をうたっていますが、利用できるイメージがまだありません |
| `wip` | 「将来対応する」という言及だけで、イメージもソースもありません |

サイトのマトリクスでは、セルに塗りつぶしの記号が入っているものが RuyiSDK の実測データ、灰色の点だけのものが「当サイト調べ」で RuyiSDK の実測は受けていません。両者は凡例ではっきり区別しています。

## 2. ディストロの公式出典

26 件のディストロの項目では、`ダウンロード` と `導入ガイド` のリンクはすべて**公式**ページを指しています。ディストロ自身のダウンロードサイト、公式ドキュメントサイト、公式 wiki、または公式リポジトリです。代表的なものは次のとおりです：

- 上流ディストロ：[debian.org](https://www.debian.org/releases/stable/riscv64/) / [cdimage.debian.org](https://cdimage.debian.org/cdimage/release/current/riscv64/iso-cd/) / [ubuntu.com](https://ubuntu.com/download/risc-v) / [cdimage.ubuntu.com](https://cdimage.ubuntu.com/releases/) / [fedoraproject.org](https://fedoraproject.org/wiki/Architectures/RISC-V) / [get.opensuse.org](https://get.opensuse.org/) / [alpinelinux.org](https://alpinelinux.org/downloads/) / [archlinuxriscv.org](https://archriscv.felixc.at/) / [gentoo.org](https://www.gentoo.org/downloads/) / [nixos.org](https://nixos.org/download/) / [freebsd.org](https://wiki.freebsd.org/riscv) / [netbsd.org](https://www.netbsd.org/ports/riscv/) / [openbsd.org](https://www.openbsd.org/riscv64.html)
- ベンダー派生システム：[revyos.com](https://revyos.com/) と [docs.revyos.dev](https://docs.revyos.dev/)（XuanTie TH1520/SG2042）、[spacemit.com](https://www.spacemit.com/) と [archive.spacemit.com](https://archive.spacemit.com/)（Bianbu）、[openeuler.org](https://www.openeuler.org/zh/download/) と [docs.openeuler.org](https://docs.openeuler.org/)、[openkylin.top](https://www.openkylin.top/downloads/) と docs.openkylin.top、[deepin.org](https://www.deepin.org/) と [deepin-community.github.io](https://deepin-community.github.io/sig-deepin-ports/images/riscv64)
- コミュニティビルド：[armbian.com](https://www.armbian.com/download/)、[dietpi.com](https://dietpi.com/#download)、[irradium.org](https://irradium.org/)、bredos.org、FVF のリリースリポジトリ

各ディストロのページ末尾にある「出典」の欄が、その項目の根拠リンクのすべてです。

## 3. 開発ボードベンダーの出典

25 枚の開発ボードの仕様と公式システム情報は、ベンダーの公式製品ページ、公式ドキュメントサイト、公式リポジトリから取っています。例：

- [sifive.com](https://www.sifive.com/boards)（HiFive Unmatched / Premier P550）、[starfivetech.com](https://www.starfivetech.com/en) と [doc-en.rvspace.org](https://doc-en.rvspace.org/)（VisionFive 2 / VisionFive 2 Lite）
- [sipeed.com](https://sipeed.com/) と [wiki.sipeed.com](https://wiki.sipeed.com/)（LicheePi 4A / Lichee Cluster 4A）、[milkv.io](https://milkv.io/) と `milkv.io/docs`（Meles / Mars / Jupiter / Pioneer / Megrez / Titan / Duo）
- [banana-pi.org](https://www.banana-pi.org/) と [docs.banana-pi.org](https://docs.banana-pi.org/)（BPI-F3）、[orangepi.org](http://www.orangepi.org/)（RV2）、[kendryte.com](https://www.kendryte.com/) と Canaan の開発者サイト（K230）、[spacemit.com](https://www.spacemit.com/)（K3 Pico-ITX / CoM260）
- 知合計算 A210 / XuanTie MelonPi：[zhcomputing.com](http://www.zhcomputing.com/) と [developer.zhcomputing.com](https://developer.zhcomputing.com/zh/docs/A210/)、[matrix.ruyisdk.org](https://matrix.ruyisdk.org/) の A210_SODIMM_V2 レポート
- QEMU：[qemu.org](https://www.qemu.org/docs/master/system/riscv/virt.html) 公式ドキュメントの RISC-V virt マシンの章

一部の新しいボードでは、ハードウェア仕様を RuyiSDK マトリクスのボードメタデータから直接取っています。該当する項目には「ボード情報は RuyiSDK テストマトリクスの記録によります。供給状況と価格は個別に確認していません」と注記しています。

## 4. AI ソフトの観点：1 件ずつ根拠を示す

AI 対応ページでは「なんとなく」は書きません。各判断の背後にはリンクがあり、主な出典は次のとおりです：

- **上流プロジェクトのドキュメント**：[github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)（`docs/build-riscv64-spacemit.md` と SpacemiT カーネルの実測データを含む）、[github.com/microsoft/onnxruntime](https://github.com/microsoft/onnxruntime)、[github.com/opencv/opencv](https://github.com/opencv/opencv) の RISC-V wiki、[github.com/Tencent/ncnn](https://github.com/Tencent/ncnn) の RISC-V CI、[github.com/OAID/Tengine](https://github.com/OAID/Tengine)
- **第三者による配布**：[riseproject.dev](https://riseproject.dev/)（RISE の PyTorch RISC-V ホイール）、[github.com/felixonmars/archriscv-packages](https://github.com/felixonmars/archriscv-packages)
- **学術**：arXiv 2503.17422（V-Seek、SG2042 上での LLM 推論最適化）
- **ベンダーのツールチェーンドキュメント**：XuanTie HHB（LicheePi 4A の NPU）、SpacemiT AI SDK、ESWIN ENNP SDK、Canaan nncase、知合 TORQ-Toolkit
- **実測記事**：CNX Software、ServeTheHome、The Register、Phoronix などによる各ボードのハンズオン記録

公開された証拠が見つからない場合は、ページに「公開された証拠は見つかりませんでした」と書き、**推測は書きません**。

## 5. 二次情報とその扱い

メディアの伝聞はすべて伝聞として明示し、一次情報としては扱いません。「この話が存在する」ことを示すためだけに使います。よく使う出典は CNX Software、Phoronix、ServeTheHome、The Register、The Next Platform、Design & Reuse、そして中国語圏では IT之家（ITHome）、芯智訊、上観新聞、科技日報、『財経』などです。ベンダーが自ら公表した性能や導入状況（例：「32 並列推論で x86 プラットフォームの 95.8%」「複数の AI 計算センターに導入済み」）は、すべて「ベンダー発表」と明記し、第三者の実測とは分けて書いています。

## 6. 方法と免責

- **確認日**：各項目に `checked` フィールドがあり、ページには「最終確認」の日付が表示されます。データは毎日 03:00 に自動で再確認します
- **推測しない**：確認できないフィールドは空欄にします。ベンダーが公表していない価格、TDP、具体的な SoC 型番は、それらしく見える数字を埋めるより、書かないことを選びます
- **リンク検証**：サイト内の外部リンクはすべて `scripts/check_urls.py` が 1 本ずつ curl で検証します。切れたリンクは安定したディレクトリページや公式ダウンロードページに差し替え、差し替えられないものは削除します
- **訂正**：誤りを見つけたら issue または MR を立て、該当する項目と根拠リンクを明記してください。証拠に基づいて直します

## 7. 謝辞

以下のプロジェクトとチームに感謝します。当サイトのデータは、その成果の上に成り立っています：

- **RuyiSDK チーム / PLCT ラボ（中国科学院ソフトウェア研究所）** —— ボードごと・システムごとの実測マトリクス。当サイトで最も中心となるデータソースです
- **各ディストロのコミュニティとメンテナ** —— Debian、Ubuntu、Fedora、openSUSE、Alpine、Arch Linux RISC-V、Gentoo、NixOS、FreeBSD、NetBSD、OpenBSD、ALT Linux、Buildroot、Yocto など
- **各開発ボードベンダーとコミュニティ** —— SiFive、StarFive、Sipeed、Milk-V、Banana Pi、Orange Pi、SpacemiT、ESWIN、UltraRISC、Canaan、知合計算、PINE64、BIT-BRICK
- **中国語圏のディストロチーム** —— openEuler RISC-V SIG、openKylin、deepin、openRuyi
- **AI 分野のオープンソースプロジェクト** —— llama.cpp、ONNX Runtime、OpenCV、ncnn、Tengine、RISE Project
- **RISC-V International** —— 仕様とエコシステムの基盤
