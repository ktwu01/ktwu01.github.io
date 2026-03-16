# Preprints

This folder is a self-contained Quarkdown workspace for formal paper-style PDF
documents. It is separate from the Jekyll site so your blog build stays
untouched.

## What is here

- `research-grounding-bilateral-vc-phd-programs.qd`: starter paper template in a clean academic layout
- `render.sh`: one-command PDF render helper
- `output/`: generated files after rendering

## Installed toolchain

Quarkdown was installed globally on this machine with Homebrew:

```bash
quarkdown --version
```

Current verified version: `1.14.1`

## Render the PDF

From this directory:

```bash
./render.sh
```

Or directly:

```bash
quarkdown c research-grounding-bilateral-vc-phd-programs.qd --pdf --strict --out output
```

## How to use this template

1. Replace the placeholder text in `research-grounding-bilateral-vc-phd-programs.qd` with your real paper content.
2. Keep the title block, author name, affiliation, and email if they are still correct.
3. Re-run `./render.sh` whenever you want a fresh PDF.

## Naming convention

Use one descriptive `.qd` file per paper so multiple preprints can coexist in
this directory without all being named `main.qd`.

## Notes for arXiv

- This template is meant as a clean academic starting point, not an official arXiv class.
- arXiv submission requirements can vary by category and workflow; when you are ready,
  we can adapt this to a stricter submission format if needed.
