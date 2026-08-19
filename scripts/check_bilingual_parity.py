#!/usr/bin/env python3
"""Check structural parity between English and Chinese translation pairs.

For every paired blog post (same permalink slug in /posts/ and /zh/posts/),
compare the translated bodies structurally: link targets, images, headings,
fenced code, tables, equations, and inline identifiers. Translation freedom
is preserved: text is never compared word-for-word, only counts and sets.

Google Docs export artifacts are normalized away:
- gstatic faviconV2 link cards resolve to the real target domain
- gstatic lamda "immersive" decorative images are ignored

Known legacy divergences are allowlisted in _data/parity_baseline.json
(pair_key -> list of allowed issue types). New posts must have zero
divergence, and the baseline must not grow.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_language_links import (
    CANONICAL_URL,
    DEFAULT_POSTS_DIR,
    FRONT_MATTER,
    PERMALINK,
    Post,
    load_posts,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASELINE = REPO_ROOT / "_data" / "parity_baseline.json"
MAX_INLINE_DELTA_FRACTION = 0.3
MAX_INLINE_DELTA_ABS = 3

AUTHOR_LINE = re.compile(r"^>\s*(?:Author|作者)[:：]?.*$", re.MULTILINE)
DISCLAIMER_LINE = re.compile(
    r"^>\s*\*\*(?:THIS IS A FAKE BLOG|这是一篇虚构博客)", re.MULTILINE
)
ZH_DAODU_BLOCK = re.compile(r"^>\s*中文导读[:：]?.*$", re.MULTILINE)
CLOSE_BRACKET_LINK = re.compile(r"\]\((https?://[^)\s]+)\)")
CODE_SPAN = re.compile(r"`([^`]+)`")
MARKDOWN_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"^(#{1,4})\s+", re.MULTILINE)
FENCE = re.compile(r"^```", re.MULTILINE)
TABLE_LINE = re.compile(r"^\|.*\|$", re.MULTILINE)
MATH_PAIR = re.compile(r"\$\$")
FAVICON_ARTIFACT = re.compile(r"gstatic\.com/faviconV2")
LAMDA_ARTIFACT = re.compile(r"gstatic\.com/lamda/images/immersives")
DOMAIN_TLDS = (
    "com|org|net|io|ai|edu|gov|mil|me|dev|co|app|info|xyz|tech|site|online|"
    "cn|jp|kr|uk|de|fr|ca|au|us|in|ru|za|mx|br|it|es|nl|se|no|fi|pl|cz|hu|"
    "gr|il|sg|hk|tw|th|vn|my|id|ph|nz|africa|guide"
)
BARE_DOMAIN = re.compile(
    rf"^(?:https?://)?([a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+({DOMAIN_TLDS})$",
    re.IGNORECASE,
)

ISSUE_TYPES = ("links", "images", "headings", "code", "tables", "math", "inline")


def normalize_domain(url):
    parsed = urlparse(url)
    return parsed.netloc.lower().removeprefix("www.").removesuffix(".")


def post_body(path):
    content = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(content)
    body = content[match.end():] if match else content
    body = AUTHOR_LINE.sub("", body)
    body = DISCLAIMER_LINE.sub("", body)
    body = ZH_DAODU_BLOCK.sub("", body)
    return body


def link_targets(body):
    """Domains referenced by markdown links, link cards, or code spans."""
    domains = set()
    for url in CLOSE_BRACKET_LINK.findall(body):
        if FAVICON_ARTIFACT.search(url):
            query = parse_qs(urlparse(url).query)
            target = query.get("url", [""])[0]
            if target.startswith("http"):
                domains.add(normalize_domain(target))
            continue
        if LAMDA_ARTIFACT.search(url):
            continue
        domains.add(normalize_domain(url))
    for span in CODE_SPAN.findall(body):
        match = BARE_DOMAIN.match(span.strip())
        if match:
            domains.add(match.group(1).lower())
    return domains


def image_targets(body):
    """Targets of content images, ignoring Google Docs decorative artifacts.

    Absolute URLs reduce to the host domain; relative paths are kept as-is
    so a dropped or added figure is still detected.
    """
    targets = set()
    for url in MARKDOWN_IMAGE.findall(body):
        if FAVICON_ARTIFACT.search(url) or LAMDA_ARTIFACT.search(url):
            continue
        if url.startswith(("http://", "https://")):
            targets.add(normalize_domain(url))
        else:
            targets.add(url)
    return targets


def heading_levels(body):
    return [len(match.group(1)) for match in HEADING.finditer(body)]


def count_fences(body):
    return len(FENCE.findall(body))


def count_table_lines(body):
    return len(TABLE_LINE.findall(body))


def count_math_blocks(body):
    return len(MATH_PAIR.findall(body)) // 2


def count_inline_code(body):
    return len(CODE_SPAN.findall(body))


def extract_structure(body):
    return {
        "links": link_targets(body),
        "images": image_targets(body),
        "headings": heading_levels(body),
        "code": count_fences(body),
        "tables": count_table_lines(body),
        "math": count_math_blocks(body),
        "inline": count_inline_code(body),
    }


def check_pair(en_path, zh_path):
    """Return (issues, structure) for one translation pair."""
    en_body = post_body(en_path)
    zh_body = post_body(zh_path)
    en_struct = extract_structure(en_body)
    zh_struct = extract_structure(zh_body)

    issues = []
    for issue_type in ("links", "images", "code", "tables", "math"):
        en_value = en_struct[issue_type]
        zh_value = zh_struct[issue_type]
        if en_value == zh_value:
            continue
        if issue_type == "links":
            only_en = sorted(en_value - zh_value)[:5]
            only_zh = sorted(zh_value - en_value)[:5]
            issues.append(
                f"{issue_type}: {len(en_value)} vs {len(zh_value)} targets"
                f"{' (only en: ' + ', '.join(only_en) + ')' if only_en else ''}"
                f"{' (only zh: ' + ', '.join(only_zh) + ')' if only_zh else ''}"
            )
        else:
            issues.append(f"{issue_type}: {en_value} vs {zh_value}")

    en_headings = en_struct["headings"]
    zh_headings = zh_struct["headings"]
    if en_headings != zh_headings:
        issues.append(
            f"headings: {len(en_headings)} vs {len(zh_headings)} "
            f"({en_headings} vs {zh_headings})"
        )

    en_inline = en_struct["inline"]
    zh_inline = zh_struct["inline"]
    if abs(en_inline - zh_inline) > max(
        MAX_INLINE_DELTA_ABS, MAX_INLINE_DELTA_FRACTION * max(en_inline, zh_inline)
    ):
        issues.append(f"inline: {en_inline} vs {zh_inline} identifiers")
    return issues, (en_struct, zh_struct)


def pair_issues(posts, baseline):
    """Return issues grouped by pair key, and resolved stale baseline entries."""
    groups = {}
    for post in posts:
        if CANONICAL_URL.fullmatch(post.permalink):
            groups.setdefault(post.pair_key, {})[post.language] = post

    grouped_issues = {}
    stale_baseline = []
    for pair_key, variants in sorted(groups.items()):
        if len(variants) < 2:
            continue
        en_path = variants["en"].path
        zh_path = variants["zh"].path
        issues, _structure = check_pair(en_path, zh_path)
        allowed = set(baseline.get(pair_key, []))
        remaining = [issue for issue in issues if not issue.startswith(tuple(allowed))]
        if remaining:
            grouped_issues[pair_key] = {
                "en": en_path.name,
                "zh": zh_path.name,
                "issues": remaining,
            }
        if allowed and not issues:
            stale_baseline.append(pair_key)
    return grouped_issues, stale_baseline


def load_baseline(path):
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--posts-dir", type=Path, default=DEFAULT_POSTS_DIR)
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    posts, _skipped = load_posts(args.posts_dir)
    baseline = load_baseline(args.baseline)
    grouped_issues, stale_baseline = pair_issues(posts, baseline)

    for pair_key in stale_baseline:
        print(
            f"Parity baseline entry for {pair_key} is fully resolved; "
            f"remove it from {args.baseline.name}."
        )

    if not grouped_issues:
        print("Bilingual parity is complete for all translation pairs.")
        return 0

    print("Bilingual parity failures (not covered by the parity baseline):")
    for pair_key, detail in sorted(grouped_issues.items()):
        print(f"  - {pair_key}: {detail['en']} vs {detail['zh']}")
        for issue in detail["issues"]:
            print(f"      {issue}")
    print(
        f"Total parity failures: {len(grouped_issues)} pair(s). "
        "Either align the translations, or add the pair to "
        f"{args.baseline.name} only if the divergence is intentional."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
