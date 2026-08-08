#!/usr/bin/env python3
"""Deterministically add the localized Koutian Wu note to every Jekyll post."""

import argparse
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_POSTS_DIR = REPO_ROOT / "_posts"
FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
PERMALINK = re.compile(r"^permalink:\s*(['\"]?)(.*?)\1\s*$", re.MULTILINE)
LANGUAGE = re.compile(r"^lang(?:uage)?:\s*(['\"]?)(.*?)\1\s*$", re.MULTILINE)
AUTHOR_PREFIX = re.compile(
    r"^>\s*(?:Author:|作者[:：])\s*\[Koutian Wu\]\([^)]+\)"
    r"(?:[；;]\s*\[GitHub:\s*ktwu01\]\([^)]+\))?"
)
AUTHOR_LINE = re.compile(AUTHOR_PREFIX.pattern + r"\s*$")
DISCLAIMER_LINE = re.compile(
    r"^>\s*\*\*(?:THIS IS A FAKE BLOG|这是一篇虚构博客)"
)
AUTHOR_NOTES = {
    "en": (
        "> Author: [Koutian Wu](https://www.linkedin.com/in/ktwu01/); "
        "[GitHub: ktwu01](https://github.com/ktwu01/)"
    ),
    "zh": (
        "> 作者：[Koutian Wu](https://www.linkedin.com/in/ktwu01/)；"
        "[GitHub: ktwu01](https://github.com/ktwu01/)"
    ),
}
CJK_CHARACTER = re.compile(r"[\u3400-\u9fff]")
LATIN_CHARACTER = re.compile(r"[A-Za-z]")
CJK_AMBIGUITY_MINIMUM = 100
CJK_AMBIGUITY_RATIO = 0.25


def post_language(front_matter):
    language_match = LANGUAGE.search(front_matter)
    if language_match:
        language = language_match.group(2).lower()
        if language.startswith(("zh", "cn")):
            return "zh"
        if language.startswith("en"):
            return "en"

    match = PERMALINK.search(front_matter)
    if not match:
        return None
    permalink = match.group(2)
    return "zh" if permalink.startswith("/zh/") else "en"


def is_author_line(line):
    return bool(AUTHOR_LINE.match(line.strip()))


def is_author_candidate(line):
    return bool(AUTHOR_PREFIX.match(line.strip()))


def is_disclaimer_line(line):
    return bool(DISCLAIMER_LINE.match(line.strip()))


def has_ambiguous_legacy_language(content):
    """Flag likely Chinese posts whose metadata otherwise defaults to English."""
    match = FRONT_MATTER.match(content)
    if not match or LANGUAGE.search(match.group(1)):
        return False
    if post_language(match.group(1)) != "en":
        return False

    body = content[match.end():]
    cjk_count = len(CJK_CHARACTER.findall(body))
    latin_count = len(LATIN_CHARACTER.findall(body))
    total_letters = cjk_count + latin_count
    return (
        cjk_count >= CJK_AMBIGUITY_MINIMUM
        and cjk_count / max(1, total_letters) >= CJK_AMBIGUITY_RATIO
    )


def expected_author_note(content):
    match = FRONT_MATTER.match(content)
    if not match:
        return None
    language = post_language(match.group(1))
    return AUTHOR_NOTES.get(language)


def logical_body_lines(content):
    """Return nonblank body lines after front matter."""
    match = FRONT_MATTER.match(content)
    if not match:
        return []
    return [line.strip() for line in content[match.end():].splitlines() if line.strip()]


def render_post(content):
    """Return a post with exactly one localized note immediately after its hook."""
    match = FRONT_MATTER.match(content)
    if not match:
        return content

    if has_ambiguous_legacy_language(content):
        raise ValueError(
            "likely Chinese content has neither lang: zh nor a /zh/ permalink"
        )

    language = post_language(match.group(1))
    if language is None:
        return content
    note = AUTHOR_NOTES[language]
    body_lines = content[match.end():].splitlines()
    unsafe_lines = [
        line.strip()
        for line in body_lines
        if is_author_candidate(line) and not is_author_line(line)
    ]
    if unsafe_lines:
        raise ValueError(
            "refusing to discard trailing author-line content: "
            + " | ".join(unsafe_lines)
        )
    body_lines = [line for line in body_lines if not is_author_line(line)]

    nonblank = [i for i, line in enumerate(body_lines) if line.strip()]
    if not nonblank:
        return content

    hook_position = 0
    if is_disclaimer_line(body_lines[nonblank[0]]):
        hook_position = 1
    if len(nonblank) <= hook_position:
        return content

    hook_index = nonblank[hook_position]
    next_content = hook_index + 1
    while next_content < len(body_lines) and not body_lines[next_content].strip():
        next_content += 1

    remainder = body_lines[next_content:]
    continues_note_blockquote = remainder and remainder[0].strip() == ">"
    separator_after_note = [] if continues_note_blockquote else [""]
    normalized_body = (
        body_lines[: hook_index + 1]
        + ["", note]
        + separator_after_note
        + remainder
    )
    trailing_newline = "\n" if content.endswith("\n") else ""
    return content[: match.end()] + "\n".join(normalized_body) + trailing_newline


def iter_posts(posts_dir):
    return sorted(Path(posts_dir).glob("*.md"))


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--posts-dir", type=Path, default=DEFAULT_POSTS_DIR)
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    stale = []
    updated = []
    unsafe = []

    for path in iter_posts(args.posts_dir):
        content = path.read_text(encoding="utf-8")
        try:
            rendered = render_post(content)
        except ValueError as error:
            unsafe.append((path.name, str(error)))
            continue
        if rendered == content:
            continue
        if args.check:
            stale.append(path.name)
        else:
            path.write_text(rendered, encoding="utf-8")
            updated.append(path.name)

    if unsafe:
        print("Author-note generation refused unsafe source lines:")
        for name, error in unsafe:
            print(f"  - {name}: {error}")
        print("Move trailing content to its own line, then rerun the generator.")
        return 1

    if stale:
        print("Author notes are missing, duplicated, misplaced, or noncanonical:")
        for name in stale:
            print(f"  - {name}")
        print("Run python3 scripts/generate_author_notes.py to repair them.")
        return 1

    if args.check:
        print("Author notes are current.")
    else:
        print(f"Updated deterministic author notes in {len(updated)} post(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
