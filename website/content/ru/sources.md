---
title: "Источники и благодарности"
sub: "Откуда взято каждое утверждение, как мы его оценивали и кого благодарим"
layout: sources
---

**Каждое техническое утверждение на этом сайте должно вести обратно к источнику.** Ниже все источники разложены по уровням — «первичные / вторичные» — и объяснено, как мы оценивали каждое утверждение. Данные сайта автоматически перепроверяются раз в день, у каждой записи указана дата проверки.

## 1. Откуда берутся результаты тестов: матрица поддержки RuyiSDK

Все выводы вида «такая-то система на такой-то плате проверена в работе / не работает» **в первую очередь опираются на официальную тестовую матрицу RuyiSDK**:

- Сайт: <https://matrix.ruyisdk.org/>
- Исходный репозиторий (сами данные, на каждую плату и систему — один markdown-файл с YAML front matter): <https://github.com/ruyisdk/support-matrix>
- Как забираются данные: сайт каждый день вытягивает этот репозиторий и разбирает в каждом отчёте поля `sys / sys_ver / sys_var / status / last_update`, превращая их в пары «плата × дистрибутив»
- Ссылка на отчёт выглядит так: `https://matrix.ruyisdk.org/reports/<板>/<系统>/<变体>/` — из ячеек матрицы и из таблиц «отчёты RuyiSDK» на страницах дистрибутивов и плат можно перейти прямо в первоисточник

**Благодарность**: команда RuyiSDK и лаборатория PLCT (Институт программного обеспечения Академии наук Китая) годами ведут эти данные, снятые с реальных плат. Это редкий для экосистемы RISC-V проверяемый сторонний набор тестов. Мы берём его как есть и не изобретаем велосипед.

### Что значат статусы (цитата из CONTRIBUTING.md того репозитория)

| Статус | Значение |
| --- | --- |
| `good` | Полностью работоспособна, можно пользоваться рабочим столом |
| `basic` | В основном работает: загружается, доступна через последовательный порт |
| `part` | Работает только часть функций |
| `cft` | Образ есть, но его ещё нужно проверить на реальной плате |
| `cfh` | В официальных документах или в сообществе поддержка заявлена, но при проверке загрузка не удалась |
| `cfi` | Официальные документы обещают поддержку, но рабочего образа пока нет |
| `wip` | Есть только обещание «когда-нибудь будет», ни образа, ни исходников |

В матрице на сайте ячейки со сплошным значком — это данные, проверенные RuyiSDK; там, где только серая точка, — «наши данные», без испытаний RuyiSDK. В легенде эти два случая явно различаются.

## 2. Официальные источники по дистрибутивам

У всех 26 дистрибутивов ссылки «Скачать» и «Документация и видео» ведут на **официальные** страницы: собственный сайт загрузки дистрибутива, официальную документацию, официальную вики или официальный репозиторий. Типичные примеры:

- Апстрим-дистрибутивы: [debian.org](https://www.debian.org/releases/stable/riscv64/) / [cdimage.debian.org](https://cdimage.debian.org/cdimage/release/current/riscv64/iso-cd/) / [ubuntu.com](https://ubuntu.com/download/risc-v) / [cdimage.ubuntu.com](https://cdimage.ubuntu.com/releases/) / [fedoraproject.org](https://fedoraproject.org/wiki/Architectures/RISC-V) / [get.opensuse.org](https://get.opensuse.org/) / [alpinelinux.org](https://alpinelinux.org/downloads/) / [archlinuxriscv.org](https://archriscv.felixc.at/) / [gentoo.org](https://www.gentoo.org/downloads/) / [nixos.org](https://nixos.org/download/) / [freebsd.org](https://wiki.freebsd.org/riscv) / [netbsd.org](https://www.netbsd.org/ports/riscv/) / [openbsd.org](https://www.openbsd.org/riscv64.html)
- Вендорные сборки: [revyos.com](https://revyos.com/) и [docs.revyos.dev](https://docs.revyos.dev/) (XuanTie TH1520/SG2042), [spacemit.com](https://www.spacemit.com/) и [archive.spacemit.com](https://archive.spacemit.com/) (Bianbu), [openeuler.org](https://www.openeuler.org/zh/download/) и [docs.openeuler.org](https://docs.openeuler.org/), [openkylin.top](https://www.openkylin.top/downloads/) и docs.openkylin.top, [deepin.org](https://www.deepin.org/) и [deepin-community.github.io](https://deepin-community.github.io/sig-deepin-ports/images/riscv64)
- Сборки сообщества: [armbian.com](https://www.armbian.com/download/), [dietpi.com](https://dietpi.com/#download), [irradium.org](https://irradium.org/), bredos.org, релизный репозиторий FVF

Блок «Источник данных» внизу каждой страницы дистрибутива перечисляет все ссылки-основания для этой записи.

## 3. Источники по производителям плат

Характеристики 25 плат и сведения об официальных системах взяты с официальных страниц продуктов, сайтов документации и репозиториев производителей, например:

- [sifive.com](https://www.sifive.com/boards) (HiFive Unmatched / Premier P550), [starfivetech.com](https://www.starfivetech.com/en) и [doc-en.rvspace.org](https://doc-en.rvspace.org/) (VisionFive 2 / VisionFive 2 Lite)
- [sipeed.com](https://sipeed.com/) и [wiki.sipeed.com](https://wiki.sipeed.com/) (LicheePi 4A / Lichee Cluster 4A), [milkv.io](https://milkv.io/) и `milkv.io/docs` (Meles / Mars / Jupiter / Pioneer / Megrez / Titan / Duo)
- [banana-pi.org](https://www.banana-pi.org/) и [docs.banana-pi.org](https://docs.banana-pi.org/) (BPI-F3), [orangepi.org](http://www.orangepi.org/) (RV2), [kendryte.com](https://www.kendryte.com/) и сайт для разработчиков Canaan (K230), [spacemit.com](https://www.spacemit.com/) (K3 Pico-ITX / CoM260)
- Zhcomputing A210 / XuanTie MelonPi: [zhcomputing.com](http://www.zhcomputing.com/) и [developer.zhcomputing.com](https://developer.zhcomputing.com/zh/docs/A210/), отчёт A210_SODIMM_V2 на [matrix.ruyisdk.org](https://matrix.ruyisdk.org/)
- QEMU: раздел про машину RISC-V virt в официальной документации [qemu.org](https://www.qemu.org/docs/master/system/riscv/virt.html)

У нескольких новых плат аппаратные параметры взяты прямо из метаданных плат в матрице RuyiSDK; на таких страницах стоит пометка «сведения о плате взяты из записей тестовой матрицы RuyiSDK; наличие в продаже и цену отдельно не проверяли».

## 4. Измерение AI-софта: доказательство к каждому пункту

На странице поддержки ИИ мы не пишем «по ощущениям»: за каждым утверждением стоит ссылка. В основном это:

- **Документация апстрим-проектов**: [github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) (включая `docs/build-riscv64-spacemit.md` и замеры на ядрах SpacemiT), [github.com/microsoft/onnxruntime](https://github.com/microsoft/onnxruntime), RISC-V-вики [github.com/opencv/opencv](https://github.com/opencv/opencv), RISC-V CI в [github.com/Tencent/ncnn](https://github.com/Tencent/ncnn), [github.com/OAID/Tengine](https://github.com/OAID/Tengine)
- **Сторонние сборки**: [riseproject.dev](https://riseproject.dev/) (колёса PyTorch для RISC-V от RISE), [github.com/felixonmars/archriscv-packages](https://github.com/felixonmars/archriscv-packages)
- **Научные работы**: arXiv 2503.17422 (V-Seek, оптимизация инференса LLM на SG2042)
- **Документация вендорных тулчейнов**: XuanTie HHB (NPU на LicheePi 4A), SpacemiT AI SDK, ESWIN ENNP SDK, Canaan nncase, Zhcomputing TORQ-Toolkit
- **Статьи с реальными замерами**: заметки о работе с конкретными платами в CNX Software, ServeTheHome, The Register, Phoronix и других изданиях

Если публичных доказательств нет, на странице так и написано — «публичных доказательств не найдено», **никаких догадок**.

## 5. Вторичные источники и оговорки

Пересказ в СМИ мы всегда помечаем как пересказ: он не служит первичным основанием и нужен только чтобы показать, что «такое сообщение существует». Обычные источники: CNX Software, Phoronix, ServeTheHome, The Register, The Next Platform, Design & Reuse, а с китайской стороны — ITHome, Jiweinet, Shangguan News, Science and Technology Daily, Caixin. Заявленные производителем производительность и внедрения (например, «32 одновременных инференса — 95,8% от платформы x86», «уже внедрено в нескольких интеллектуальных ЦОД») всегда помечаются как «по данным производителя» и пишутся отдельно от сторонних замеров.

## 6. Методика и оговорки

- **Дата проверки**: у каждой записи есть поле `checked`, на странице показывается дата «проверено». Данные автоматически перепроверяются каждый день в 03:00
- **Не угадываем**: чего не нашли — оставляем пустым. Цену, TDP и точную модель SoC, которые производитель не опубликовал, мы лучше не напишем вовсе, чем подставим правдоподобное число
- **Проверка ссылок**: все внешние ссылки сайта по одной проверяются curl скриптом `scripts/check_urls.py`; битые заменяются на стабильную страницу каталога или официальную страницу загрузки, а если замены нет — удаляются
- **Исправления**: нашли ошибку — откройте issue или MR, укажите конкретную запись и ссылку-основание; правим по доказательствам

## 7. Благодарности

Спасибо этим проектам и командам — данные сайта стоят на их работе:

- **Команда RuyiSDK / лаборатория PLCT (Институт программного обеспечения Академии наук Китая)** — матрица замеров по каждой плате и каждой системе, наш главный источник данных
- **Сообщества и мейнтейнеры дистрибутивов** — Debian, Ubuntu, Fedora, openSUSE, Alpine, Arch Linux RISC-V, Gentoo, NixOS, FreeBSD, NetBSD, OpenBSD, ALT Linux, Buildroot, Yocto и другие
- **Производители и сообщества плат** — SiFive, StarFive, Sipeed, Milk-V, Banana Pi, Orange Pi, SpacemiT, ESWIN, UltraRISC, Canaan, Zhcomputing, PINE64, BIT-BRICK
- **Китайские команды дистрибутивов** — openEuler RISC-V SIG, openKylin, deepin, openRuyi
- **Открытые проекты со стороны ИИ** — llama.cpp, ONNX Runtime, OpenCV, ncnn, Tengine, RISE Project
- **RISC-V International** — спецификации и инфраструктура экосистемы
