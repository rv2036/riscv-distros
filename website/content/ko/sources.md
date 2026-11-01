---
title: "출처 및 감사"
sub: "이 사이트의 모든 결론이 어디서 왔는지, 어떻게 판단했는지, 그리고 감사 인사"
layout: sources
---

**이 사이트의 모든 기술적 결론은 출처로 되돌아갈 수 있어야 합니다.** 아래에 모든 출처를 “1차 / 2차”로 나눠 적고, 각 결론을 어떻게 판정했는지 설명합니다. 사이트 데이터는 매일 한 번 자동으로 확인하며, 모든 항목에 확인 날짜가 붙습니다.

## 1. 테스트 결론의 출처: RuyiSDK 지원 매트릭스

사이트 안의 모든 “어떤 시스템이 어떤 보드에서 실측으로 되는/안 되는” 결론은 **1차 근거가 RuyiSDK 공식 테스트 매트릭스**입니다:

- 사이트: <https://matrix.ruyisdk.org/>
- 소스 저장소(데이터 본체, 보드·시스템마다 markdown 한 장 + YAML front matter): <https://github.com/ruyisdk/support-matrix>
- 데이터 수집 방식: 이 사이트는 매일 그 저장소를 가져와 테스트 보고서마다의 `sys / sys_ver / sys_var / status / last_update` 필드를 파싱하고, 사이트 안의 “보드 × 배포판” 조합으로 매핑합니다
- 보고서 링크는 `https://matrix.ruyisdk.org/reports/<보드>/<시스템>/<변형>/` 형태이고, 사이트 매트릭스 칸과 배포판/개발 보드 페이지의 “RuyiSDK 실측 보고서” 표에서 원문으로 바로 들어갈 수 있습니다

**감사**: RuyiSDK 팀과 PLCT Lab(중국과학원 소프트웨어연구소, ISCAS)이 이 보드별 실측 데이터를 오래 유지해 왔습니다. RISC-V 생태계에서 드물게 검증 가능한 제3자 테스트 집합이며, 이 사이트는 그것을 그대로 신뢰하고 바퀴를 다시 만들지 않습니다.

### 상태 열거형의 정의(해당 저장소 CONTRIBUTING.md 인용)

| 상태 | 의미 |
| --- | --- |
| `good` | 완전히 사용 가능하고 데스크톱 환경까지 들어갈 수 있음 |
| `basic` | 기본적으로 사용 가능하며, 부팅되고 시리얼로 쓸 수 있음 |
| `part` | 일부 기능만 갖춤 |
| `cft` | 이미지는 있으나 실기에서 추가 검증이 필요함 |
| `cfh` | 공식 문서/커뮤니티는 지원한다고 하지만 실측 부팅에 실패함 |
| `cfi` | 공식 문서가 지원을 주장하지만 쓸 수 있는 이미지가 없음 |
| `wip` | “나중에 지원할 것”이라는 발표뿐이고 이미지도 소스도 없음 |

사이트 매트릭스에서 칸에 속이 찬 기호가 있는 것은 RuyiSDK 실측 데이터이고, 회색 점만 있는 것은 “이 사이트 자체 자료”로 RuyiSDK 실측을 거치지 않은 것이며, 둘은 범례에서 명확히 구분됩니다.

## 2. 배포판 공식 출처

26개 배포판 항목에서 `다운로드`와 `설치 문서` 링크는 모두 **공식** 페이지를 가리킵니다. 배포판 자체의 다운로드 사이트, 공식 문서 사이트, 공식 위키 또는 공식 저장소입니다. 대표적인 몇 가지 유형:

- 업스트림 배포판: [debian.org](https://www.debian.org/releases/stable/riscv64/) / [cdimage.debian.org](https://cdimage.debian.org/cdimage/release/current/riscv64/iso-cd/) / [ubuntu.com](https://ubuntu.com/download/risc-v) / [cdimage.ubuntu.com](https://cdimage.ubuntu.com/releases/) / [fedoraproject.org](https://fedoraproject.org/wiki/Architectures/RISC-V) / [get.opensuse.org](https://get.opensuse.org/) / [alpinelinux.org](https://alpinelinux.org/downloads/) / [archlinuxriscv.org](https://archriscv.felixc.at/) / [gentoo.org](https://www.gentoo.org/downloads/) / [nixos.org](https://nixos.org/download/) / [freebsd.org](https://wiki.freebsd.org/riscv) / [netbsd.org](https://www.netbsd.org/ports/riscv/) / [openbsd.org](https://www.openbsd.org/riscv64.html)
- 벤더 파생 시스템: [revyos.com](https://revyos.com/)과 [docs.revyos.dev](https://docs.revyos.dev/)(XuanTie TH1520/SG2042), [spacemit.com](https://www.spacemit.com/)과 [archive.spacemit.com](https://archive.spacemit.com/)(Bianbu), [openeuler.org](https://www.openeuler.org/zh/download/)와 [docs.openeuler.org](https://docs.openeuler.org/), [openkylin.top](https://www.openkylin.top/downloads/)과 [docs.openkylin.top](http://docs.openkylin.top/), [deepin.org](https://www.deepin.org/)와 [deepin-community.github.io](https://deepin-community.github.io/sig-deepin-ports/images/riscv64)
- 커뮤니티 빌드: [armbian.com](https://www.armbian.com/download/), [dietpi.com](https://dietpi.com/#download), [irradium.org](https://irradium.org/), bredos.org, FVF의 릴리스 저장소

각 배포판 페이지 맨 아래의 “이 페이지의 출처”에 그 항목의 근거 링크가 모두 나열되어 있습니다.

## 3. 개발 보드 벤더 출처

25개 개발 보드의 사양과 공식 시스템 정보는 벤더 공식 제품 페이지, 공식 문서 사이트, 공식 저장소에서 가져왔습니다. 예를 들면:

- [sifive.com](https://www.sifive.com/boards)(HiFive Unmatched / Premier P550), [starfivetech.com](https://www.starfivetech.com/en)과 [doc-en.rvspace.org](https://doc-en.rvspace.org/)(VisionFive 2 / VisionFive 2 Lite)
- [sipeed.com](https://sipeed.com/)과 [wiki.sipeed.com](https://wiki.sipeed.com/)(LicheePi 4A / Lichee Cluster 4A), [milkv.io](https://milkv.io/)와 `milkv.io/docs`(Meles / Mars / Jupiter / Pioneer / Megrez / Titan / Duo)
- [banana-pi.org](https://www.banana-pi.org/)와 [docs.banana-pi.org](https://docs.banana-pi.org/)(BPI-F3), [orangepi.org](http://www.orangepi.org/)(RV2), [kendryte.com](https://www.kendryte.com/)과 Canaan 개발자 사이트(K230), [spacemit.com](https://www.spacemit.com/)(K3 Pico-ITX / CoM260)
- 즈허컴퓨팅(Zhihe Computing) A210 / XuanTie MelonPi: [zhcomputing.com](http://www.zhcomputing.com/)과 [developer.zhcomputing.com](https://developer.zhcomputing.com/zh/docs/A210/), [matrix.ruyisdk.org](https://matrix.ruyisdk.org/)의 A210_SODIMM_V2 보고서
- QEMU: [qemu.org](https://www.qemu.org/docs/master/system/riscv/virt.html) 공식 문서의 RISC-V virt 머신 장

일부 최신 보드의 하드웨어 파라미터는 RuyiSDK 매트릭스의 보드 메타데이터에서 바로 가져왔고, 그런 항목에는 페이지에 “보드 정보는 RuyiSDK 테스트 매트릭스 기록에서 가져왔으며, 공급과 가격은 별도로 확인하지 않았습니다”라고 적혀 있습니다.

## 4. AI 소프트웨어 차원: 항목마다 근거 제시

AI 지원 페이지는 “느낌”을 쓰지 않고, 판단마다 링크를 달아 두었습니다. 주로 다음에서 옵니다:

- **업스트림 프로젝트 문서**: [github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)(`docs/build-riscv64-spacemit.md`와 SpacemiT 커널 실측 데이터 포함), [github.com/microsoft/onnxruntime](https://github.com/microsoft/onnxruntime), [github.com/opencv/opencv](https://github.com/opencv/opencv)의 RISC-V 위키, [github.com/Tencent/ncnn](https://github.com/Tencent/ncnn)의 RISC-V CI, [github.com/OAID/Tengine](https://github.com/OAID/Tengine)
- **제3자 배포**: [riseproject.dev](https://riseproject.dev/)(RISE의 PyTorch RISC-V 휠), [github.com/felixonmars/archriscv-packages](https://github.com/felixonmars/archriscv-packages)
- **학술**: arXiv 2503.17422(V-Seek, SG2042에서의 LLM 추론 최적화)
- **벤더 툴체인 문서**: XuanTie HHB(LicheePi 4A NPU), SpacemiT AI SDK, ESWIN ENNP SDK, Canaan nncase, 즈허컴퓨팅 TORQ-Toolkit
- **실측 기사**: CNX Software, ServeTheHome, The Register, Phoronix 등이 특정 보드를 직접 만져 본 기록

공개 근거를 찾지 못한 경우 페이지에는 “공개된 근거를 찾지 못했습니다”라고 쓰고, **추측은 쓰지 않습니다**.

## 5. 2차 출처와 기준

언론의 전언은 모두 전언이라고 표시하며 1차 근거로 쓰지 않고, “이 소식이 존재한다”는 것을 설명하는 데만 씁니다. 흔한 출처로는 CNX Software, Phoronix, ServeTheHome, The Register, The Next Platform, Design & Reuse, 그리고 중국어권의 IT之家(ITHome), 芯智讯, 상관신문(上观新闻), 과기일보(科技日报), 차이징(财经)이 있습니다. 벤더가 스스로 밝힌 성능과 구축 현황(예: “32 동시 추론이 x86 플랫폼의 95.8%”, “여러 지역의 지능형 컴퓨팅 센터에 도입”)은 모두 “벤더 발표”로 표시하고 제3자 실측과 분리해 씁니다.

## 6. 방법과 면책

- **확인 날짜**: 모든 항목에 `checked` 필드가 있고, 페이지에는 “최종 확인” 날짜가 표시됩니다. 데이터는 매일 03:00에 자동으로 한 번 다시 확인합니다
- **추측하지 않음**: 찾을 수 없는 필드는 비워 둡니다. 벤더가 공개하지 않은 가격, TDP, 구체적인 SoC 모델은 그럴듯한 숫자를 채우기보다 쓰지 않는 쪽을 택합니다
- **링크 검증**: 사이트의 모든 외부 링크는 `scripts/check_urls.py`가 하나씩 curl로 검증합니다. 끊긴 링크는 안정적인 디렉터리 페이지나 공식 다운로드 페이지로 바꾸고, 바꿀 수 없으면 삭제합니다
- **정정**: 문제를 발견하면 이슈 또는 MR을 열고 구체적인 항목과 근거 링크를 적어 주세요. 근거에 따라 고칩니다

## 7. 감사 인사

이 사이트의 데이터는 아래 프로젝트와 팀의 작업 위에 서 있습니다. 감사합니다:

- **RuyiSDK 팀 / PLCT Lab(중국과학원 소프트웨어연구소)** — 보드별·시스템별 실측 매트릭스, 이 사이트의 가장 핵심적인 데이터 출처
- **각 배포판 커뮤니티와 메인테이너** — Debian, Ubuntu, Fedora, openSUSE, Alpine, Arch Linux RISC-V, Gentoo, NixOS, FreeBSD, NetBSD, OpenBSD, ALT Linux, Buildroot, Yocto 등
- **각 개발 보드 벤더와 커뮤니티** — SiFive, StarFive, Sipeed, Milk-V, Banana Pi, Orange Pi, SpacemiT, ESWIN, UltraRISC, Canaan, 즈허컴퓨팅(Zhihe Computing), PINE64, BIT-BRICK
- **중국어 배포판 팀** — openEuler RISC-V SIG, openKylin, deepin, openRuyi
- **AI 쪽 오픈소스 프로젝트** — llama.cpp, ONNX Runtime, OpenCV, ncnn, Tengine, RISE Project
- **RISC-V International** — 규격과 생태계 기반
