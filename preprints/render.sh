#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

DOC_FILE="research-grounding-bilateral-vc-phd-programs.qd"

quarkdown c "$DOC_FILE" --pdf --strict --out output
