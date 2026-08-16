---
title: '用 Fortran、C++ 和 C 构建一个真正的 ZIP 炸弹'
date: 2026-07-01
permalink: /zh/posts/2026/07/fortran-zip-bomb/
tags:
  - security
  - fortran
  - systems-programming
---
我一直在玩混合语言构建（Fortran 通过 `iso_c_binding` 调用 C++ 和 C），想要一个比"跨语言把两个数加起来"更有意思的演示。于是我建了 [fortran-zip-bomb](https://github.com/ktwu01/fortran-zip-bomb)：一个小程序，生成一个真正的 **ZIP 炸弹**——一个解压时会扩展成大得多的文件的小压缩包。

> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；[GitHub: ktwu01](https://github.com/ktwu01/)

## ZIP 炸弹到底是什么

ZIP 炸弹利用了 DEFLATE 算法压缩高度重复数据有多出色。
把几兆字节的同一重复字节模式喂给它，它能把体积缩小几个数量级——解压时就得重建完整的、大得多的流。经典的例子是
[42.zip](https://en.wikipedia.org/wiki/Zip_bomb)，一个 42KB 的文件通过六层套娃式的压缩包内嵌，扩展到约 4.5 PB，
每一层都把上一层的放大系数再乘一次。

这个项目不套压缩包——它是一个扁平的 ZIP，含 1000 条重复数据条目——
所以达不到 42.zip 那种离谱的比率，但机制是相同的，而且它是真的：我的生成器产生一个约 21MB 的文件，解压到约 10GB，任何符合标准的 unzip 工具都会乐意（且正确地）把它展开。

历史上，这类炸弹之所以要紧，是因为早期的杀毒扫描器和邮件服务器会试图递归解包它们见到的每个压缩包，所以一个微小的附件就能在任何人打开它之前耗尽磁盘或内存。现代工具用解压大小/比率上限来防御这一点，而这正是你想拿一个真实（而非模拟）载荷去测试的那种检查。

## 为什么它需要一次真正的修复

我最初的一版用手写的游程编码器，而不是真正的 DEFLATE，
并且照样把 ZIP 头的压缩标志设成"deflate"。任何真正的 unzip 工具都会正确地把它当损坏拒绝——它其实不是一个能用的 ZIP 炸弹，只是一个形状像它的文件。我改用 zlib 的裸 deflate（`windowBits = -15`，不带 zlib/gzip 包装，因为 ZIP 本地/中央目录格式期望的就是这样）重做了压缩步骤，并把一个坏掉的、不完整的 CRC32 表换成了 zlib 真正的 `crc32()`。用 `unzip -t` 对每个条目端到端验证过。

## 你自己试试

我放了一个可用的副本作为带门槛的演示——**它需要明确的点击通过，而且你只能在一次性 VM/容器里、且有 10GB+ 空闲磁盘时才应该解压它**：

**[→ Fortran ZIP Bomb demo](/demos/fortran-zipbomb/)**

源码、构建说明（gfortran + g++ + gcc + zlib），以及 Fortran ↔ C++ ↔ C 互操作是怎么连起来的完整讲述，都在 [GitHub 仓库](https://github.com/ktwu01/fortran-zip-bomb)里。