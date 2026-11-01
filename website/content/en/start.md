---
title: "Getting started"
sub: "From QEMU to real hardware: get the order right, skip a few pitfalls"
layout: start
---

## First decide what you actually want to do

Three typical goals, three very different routes:

- **You just want to see what RISC-V looks like**: use QEMU — you are inside a system in ten minutes and you don't buy a board.
- **You want real hardware for modest development**: buy a board with a mature software stack whose official image boots (list further down this page).
- **You want AI inference or to validate a specific chip**: check the [AI software](ai/) page for someone who already got it running, then decide what to buy.

## Step 1: QEMU (everyone starts here)

QEMU is the default RISC-V emulator, and nearly every distro supports it first. The upside is no shipping wait and a broken install that you simply reinstall; the downside is that performance tells you nothing about real hardware, and driver problems never show up. On the distro pages, any QEMU support is marked "official".

## Step 2: pick a board

Three criteria, in order:

1. **Does the vendor ship an image**: a vendor image is the only thing that boots the moment you plug it in; community ports usually mean building U-Boot yourself.
2. **Is the kernel upstream**: once a kernel is in mainline, distros have a chance of installing directly; boards stuck on a vendor 5.10/6.1 branch usually break on upgrade.
3. **Is anyone using it**: forum, chat and GitHub issue activity decide whether you will find an answer when you are stuck.

## Step 3: after writing the image to the card

- Serial is your first debugging tool; on almost every board the first boot is watched over serial.
- Don't rush to swap distros: get the vendor image booting first to prove the hardware is fine, then experiment with other systems.
- Before switching distros, read the pitfalls on that distro's page — many problems already have a known fix.

## Common misunderstandings

- **"Debian officially supports RISC-V" does not mean "your board can install Debian"**: architecture support (riscv64) and board support (device tree, U-Boot, firmware) are two separate things.
- **"A new kernel version" does not mean "it runs"**: many vendor kernels are private branches with modified device trees and drivers, and they stop booting once replaced.
- **AI accelerators almost always require the vendor SDK**: what standard frameworks can do on RISC-V is mostly CPU inference; the NPU is a separate matter.
