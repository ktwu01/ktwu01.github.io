#!/usr/bin/env python3
"""Run the complete blog formatting and test workflow from one command."""

import argparse
import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from generate_language_links import load_posts


def workflow(fix=False):
    python = sys.executable
    checks = []

    if fix:
        checks.extend(
            [
                ("Generate author notes", [python, "scripts/generate_author_notes.py"]),
                ("Generate language links", [python, "scripts/generate_language_links.py"]),
            ]
        )

    checks.extend(
        [
            ("Check author notes", [python, "scripts/generate_author_notes.py", "--check"]),
            ("Lint blog posts", [python, "scripts/lint_blog_format.py"]),
            ("Check language links", [python, "scripts/generate_language_links.py", "--check"]),
            ("Check bilingual parity", [python, "scripts/check_bilingual_parity.py", "--check"]),
            (
                "Run blog tests",
                [python, "-m", "unittest", "discover", "-s", "tests", "-v"],
            ),
        ]
    )
    return checks


def run_workflow(fix=False, runner=subprocess.run):
    for label, command in workflow(fix=fix):
        print(f"\n==> {label}", flush=True)
        result = runner(command, cwd=REPO_ROOT, check=False)
        if result.returncode:
            print(f"\nBlog workflow failed during: {label}", file=sys.stderr)
            return result.returncode

    mode = "fixed and verified" if fix else "verified"
    print(f"\nBlog content {mode} successfully.")
    return 0


def write_summary():
    """Compact markdown summary of bilingual coverage for CI step summaries."""
    posts, skipped = load_posts(REPO_ROOT / "_posts")
    languages = Counter(post.language for post in posts)
    by_key = {}
    for post in posts:
        by_key.setdefault(post.pair_key, set()).add(post.language)
    paired = sum(1 for langs in by_key.values() if len(langs) == 2)
    monolingual = sum(1 for langs in by_key.values() if len(langs) < 2)

    coverage_baseline = json.loads(
        (REPO_ROOT / "_data" / "language_coverage_baseline.json").read_text(encoding="utf-8")
    )
    parity_baseline = json.loads(
        (REPO_ROOT / "_data" / "parity_baseline.json").read_text(encoding="utf-8")
    )

    summary = (
        "## Blog coverage summary\n\n"
        f"- Posts: {len(posts)} total, {languages.get('en', 0)} English, "
        f"{languages.get('zh', 0)} Chinese\n"
        f"- Translation pairs: {paired}, monolingual posts: {monolingual}\n"
        f"- Missing-language baseline entries: {len(coverage_baseline)}\n"
        f"- Parity baseline entries: {len(parity_baseline)}\n"
    )
    if skipped:
        summary += f"- Skipped (non-post files): {len(skipped)}\n"

    destination = os.environ.get("GITHUB_STEP_SUMMARY")
    if destination:
        with open(destination, "a", encoding="utf-8") as handle:
            handle.write(summary + "\n")
    else:
        print(summary, end="")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate and/or verify all blog metadata, formatting, and tests."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--fix",
        action="store_true",
        help="regenerate derived blog data before running every check",
    )
    mode.add_argument(
        "--check",
        action="store_true",
        help="verify without changing files (the default)",
    )
    mode.add_argument(
        "--summary",
        action="store_true",
        help="print a compact bilingual coverage summary and exit",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if args.summary:
        write_summary()
        return 0
    return run_workflow(fix=args.fix)


if __name__ == "__main__":
    raise SystemExit(main())