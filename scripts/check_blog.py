#!/usr/bin/env python3
"""Run the complete blog formatting and test workflow from one command."""

import argparse
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


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
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    return run_workflow(fix=args.fix)


if __name__ == "__main__":
    raise SystemExit(main())
