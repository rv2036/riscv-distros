# riscv-distros.org

给**第一次测试或使用 RISC-V 的人**看的门户站：哪个发行版能在哪块板子上跑、镜像去哪下、有哪些坑。

- 站点：<https://riscv-distros.org>
- 本仓（内网 GitLab）：`https://github.com/rv2036/riscv-distros`
- GitHub 镜像（部署在这里）：<https://github.com/rv2036/riscv-distros>
- 语言：简体中文（根路径）/ English / 日本語 / Русский / 한국어
- 明暗两套配色，跟随系统并可手动切换

## 五个栏目

| 栏目 | 路径 | 内容 |
| --- | --- | --- |
| **入门** | `/start/` | 从 QEMU 到真机的顺序、选板三条标准、常见误解 |
| **发行版** | `/distros/` | 每个发行版一页：上游状态、基于什么、版本、下载、教程与视频、坑、下游衍生 |
| **开发板** | `/boards/` | 每块板一页：SoC、规格、在售状态、官方系统、能装哪些发行版、下载、坑 |
| **支持矩阵** | `/matrix/` | 行是开发板、列是发行版，格子标官方/社区/部分三档 |
| **AI 软件** | `/ai/` | 每块板能跑什么（llama.cpp / ONNX Runtime / PyTorch …），只收录有公开证据的 |

## 收录口径

- **每条都要指得回一手来源**：厂商文档、官方仓库、发行版 wiki。媒体转述要标明是转述。
- **查不到的留空，不猜**：没有公开证据的写「未找到公开证据」，不替厂商说好话。
- 每个条目都带 `checked`（核查日期），读者能判断信息新旧。
- 「上游官方支持」和「社区移植」严格区分：架构支持（riscv64）≠ 板级支持（设备树 / U-Boot / 固件）。
- 厂商定制发行版要写清**基于什么**（多数是自定制内核 + Debian/Ubuntu 的 rootfs）。
- openRuyi 这类主要供厂商测试的系统，标为「厂商测试用」，不默认推荐。

## 数据驱动

内容全在 `website/data/i18n/<lang>/`，模板只负责渲染；加一条数据跑一次生成脚本即可。

```
website/
  hugo.toml                 # 五语言：zh（根）/ en / ja / ru / ko
  content/<lang>/           # 首页、start、matrix、ai，以及 distros/ 与 boards/ 两个栏目
  data/i18n/<lang>/
    distros.yaml            # 发行版条目
    boards.yaml             # 开发板条目
    ai.yaml                 # AI 软件支持（含 RuyiSDK 测试矩阵入口）
  i18n/<lang>.toml          # 界面文案（五种语言的键集合必须完全相同）
  layouts/                  # index + _default/{start,distros,distro,boards,board,matrix,ai,rss}
  assets/css/main.css       # 明暗双主题
  static/                   # favicon.svg、CNAME
scripts/
  gen_content.py            # 由 data 生成 distros/<id>.md、boards/<id>.md 明细页骨架
  check_site.py             # 自检闸门
```

### 条目字段

`distros.yaml`：

```yaml
- id: debian                 # 唯一 id，也是 URL
  name: Debian
  upstream: official         # official / community / downstream
  kind: distro               # distro / buildsystem
  based_on: 独立
  audience: recommended      # recommended / advanced / vendor
  versions: ["13 trixie"]
  boards: [{ board: unmatched, level: official, note: "" }]   # level: official/community/partial
  downloads: [{ label: "", url: "" }]
  guides: [{ label: "", url: "", type: doc, lang: en }]        # type: doc / video
  gotchas: ["…"]
  doc_langs: [en]
  derivatives: ["…"]
  note: 一句话结论
  checked: "2026-11-01"
  order: 1
  feature: true              # 首页高亮
```

`boards.yaml` 同构，字段为 `soc / vendor / spec / status / price_note / official_os / distros / downloads / guides / gotchas / doc_langs`；
`ai.yaml` 每条板一行：`board / soc / runs[{item,state,evidence[],note}] / npu / note`。

### 加一条内容

```bash
cd ~/riscv-distros
git fetch origin -q && git checkout -b <主题> origin/main
# 改 website/data/i18n/zh/*.yaml → 同步其余四语
~/.hermes/hermes-agent/venv/bin/python scripts/gen_content.py   # 新增条目要生成明细页
make site-check
```

新增条目只改中文，其余语言会**回退显示中文**（刻意的回退设计，不是 bug），所以四语要同步翻译。

## RSS

每个语言四份 + 每个明细页一份：

| Feed | 内容 |
| --- | --- |
| `/index.xml` | 全部更新（发行版 + 开发板合并，按核查日期倒序） |
| `/distros/index.xml` | 发行版栏目 |
| `/boards/index.xml` | 开发板栏目 |
| `/ai/index.xml` | AI 软件栏目 |
| `/distros/<id>/index.xml` | 单个发行版的更新 |
| `/boards/<id>/index.xml` | 单块开发板的更新 |

`guid` 用 `distro:<id>` / `board:<id>` 这类稳定标识并标 `isPermaLink="false"`，改标题不会让订阅端重推。

## 订阅

每个页面 hero 下方有订阅条：左侧邮件表单、右侧 RSS 入口。

- 后端地址在 `hugo.toml` 的 `[params] newsletter_endpoint`，**现在留空** → 输入框与按钮 `disabled`
- 填入端点后表单自动变成可提交（`method="post"`，带 `email` 与 `lang`），不需要改模板

## 构建与自检

```bash
make site         # 构建到 website/public
make site-serve   # 本地预览 http://localhost:1325/
make site-check   # 页面矩阵 / 明细页与 feed / hreflang / 站内链接 / 订阅条
```

需要 Hugo **0.147.9 extended**；`--cleanDestinationDir` 不可省。

自检闸门覆盖：五语言 × 6 页齐全、每个 `distros/<id>/` 与 `boards/<id>/` 都有页面和 feed、五语言明细页集合一致、hreflang 全有 x-default、站内链接 0 坏、feed 条目字段合法且 guid 唯一、每页都有订阅条。

## 部署

push 到 `main` 触发 `.github/workflows/pages.yml`；只有主仓 `rv2036/riscv-distros` 会走 `configure-pages`、产物上传与 `deploy`，下游 fork 只跑构建与自检。

## 许可

站点内容 CC BY-SA 4.0。
