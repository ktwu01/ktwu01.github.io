---
title: 'Building a real ZIP bomb in Fortran, C++, and C'
date: 2026-07-01
permalink: /posts/2026/07/fortran-zip-bomb/
tags:
  - security
  - fortran
  - systems-programming
---

I've been playing with mixed-language builds (Fortran calling into C++ and C via
`iso_c_binding`) and wanted a demo that was more interesting than "add two numbers
across languages." So I built [Fortran-Playground](https://github.com/ktwu01/Fortran-Playground):
a small program that generates a genuine **ZIP bomb** — a small archive that expands
into a much larger file on decompression.

## What a ZIP bomb actually is

A ZIP bomb exploits how well the DEFLATE algorithm compresses highly repetitive data.
Feed it a few megabytes of the same repeated byte pattern and it can shrink that down
by several orders of magnitude — decompression then has to reconstruct the full,
much larger stream. The classic example is
[42.zip](https://en.wikipedia.org/wiki/Zip_bomb), 42KB that expands to ~4.5 petabytes
by nesting archives inside archives six layers deep, each layer multiplying the
amplification of the last.

This project doesn't nest archives — it's a single flat ZIP with 1000 entries of
repetitive data — so it doesn't reach 42.zip's absurd ratios, but the mechanism is the
same and it's real: my generator produces a ~21MB file that decompresses to ~10GB, and
any standards-compliant unzip tool will happily (and correctly) expand it.

Historically, bombs like this mattered because early antivirus scanners and mail
servers would try to recursively unpack every archive they saw, so a tiny attachment
could exhaust disk or memory before anyone opened it. Modern tools defend against this
with decompression size/ratio limits, which is exactly the kind of check you'd want to
test against a real (not simulated) payload.

## Why it needed a real fix

My first pass at this used a hand-rolled run-length encoder instead of real DEFLATE,
and set the ZIP header's compression flag to "deflate" anyway. Any real unzip tool
correctly rejected that as corrupt — it wasn't actually a working ZIP bomb, just a file
shaped like one. I redid the compression step using zlib's raw deflate (`windowBits =
-15`, no zlib/gzip wrapper, since that's what the ZIP local/central-directory format
expects) and swapped a broken partial CRC32 table for zlib's real `crc32()`. Verified
end-to-end with `unzip -t` against every entry.

## Try it yourself

I put a working copy up as a gated demo — **it requires an explicit click-through, and
you should only extract it in a disposable VM/container with 10GB+ free disk**:

**[→ Fortran ZIP Bomb demo](/demos/fortran-zipbomb/)**

Source, build instructions (gfortran + g++ + gcc + zlib), and the full write-up of how
the Fortran ↔ C++ ↔ C interop is wired together are in the
[GitHub repo](https://github.com/ktwu01/Fortran-Playground).
