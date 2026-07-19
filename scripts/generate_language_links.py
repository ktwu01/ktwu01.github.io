#!/usr/bin/env python3
"""Validate blog URLs and generate reciprocal language-link data for Jekyll."""

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_POSTS_DIR = REPO_ROOT / "_posts"
DEFAULT_OUTPUT = REPO_ROOT / "_data" / "language_links.json"
FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
PERMALINK = re.compile(
    r"^permalink:\s*(['\"]?)(.*?)\1\s*$", re.MULTILINE
)
CANONICAL_URL = re.compile(
    r"^/(zh/)?posts/(\d{4})/(\d{2})/([^/]+)/$"
)
FORBIDDEN_SUFFIX = re.compile(r"-(?:cn|zh|en)$", re.IGNORECASE)
DATED_FILENAME = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")
SOURCE_LANGUAGE_SUFFIX = re.compile(r"-(?:cn|zh|en)$", re.IGNORECASE)
LANGUAGE_METADATA = {
    "en": {"label": "English"},
    "zh": {"label": "中文"},
}


@dataclass(frozen=True)
class Post:
    path: Path
    permalink: str

    @property
    def language(self):
        return "zh" if self.permalink.startswith("/zh/") else "en"

    @property
    def pair_key(self):
        return self.permalink.removeprefix("/zh")

    @property
    def source_pair_key(self):
        match = DATED_FILENAME.match(self.path.name)
        if not match:
            return self.path.stem
        year, month, _day, slug = match.groups()
        slug = SOURCE_LANGUAGE_SUFFIX.sub("", slug)
        return f"{year}-{month}-{slug.lower()}"


def load_posts(posts_dir):
    posts = []
    for path in sorted(Path(posts_dir).glob("*.md")):
        content = path.read_text(encoding="utf-8")
        front_matter = FRONT_MATTER.match(content)
        permalink = ""
        if front_matter:
            match = PERMALINK.search(front_matter.group(1))
            if match:
                permalink = match.group(2)
        posts.append(Post(path, permalink))
    return posts


def validate_post_url(path, permalink):
    path = Path(path)
    issues = []
    match = CANONICAL_URL.fullmatch(permalink)
    if not match:
        issues.append(
            "permalink must use canonical /posts/YYYY/MM/slug/ or "
            "/zh/posts/YYYY/MM/slug/ form"
        )
        return issues

    zh_prefix, year, month, slug = match.groups()
    language = "zh" if zh_prefix else "en"
    if not 1 <= int(month) <= 12:
        issues.append(f"permalink month must be between 01 and 12: {month}")
    if FORBIDDEN_SUFFIX.search(slug):
        issues.append("public permalink slug must not use a language suffix")

    filename_match = DATED_FILENAME.match(path.name)
    if filename_match:
        file_year, file_month, _day, _slug = filename_match.groups()
        if (year, month) != (file_year, file_month):
            issues.append(
                "permalink year/month must match the post filename date"
            )

    lower_name = path.name.lower()
    if lower_name.endswith("-cn.md") and language != "zh":
        issues.append("-cn.md post must use a /zh/ permalink")
    if lower_name.endswith("-zh.md") and language != "zh":
        issues.append("-zh.md post must use a /zh/ permalink")
    if lower_name.endswith("-en.md") and language != "en":
        issues.append("English-marked source file must use /posts/ permalink")
    return issues


def validate_posts(posts):
    issues = []
    variants_by_key = {}
    source_groups = {}

    for post in posts:
        for issue in validate_post_url(post.path, post.permalink):
            issues.append(f"{post.path.name}: {issue}")
        if not CANONICAL_URL.fullmatch(post.permalink):
            continue

        variant_key = (post.pair_key, post.language)
        previous = variants_by_key.get(variant_key)
        if previous:
            issues.append(
                f"{post.path.name}: duplicate {post.language} variant for "
                f"{post.pair_key} (already used by {previous.path.name})"
            )
        else:
            variants_by_key[variant_key] = post
        source_groups.setdefault(post.source_pair_key, []).append(post)

    for source_key, group in sorted(source_groups.items()):
        languages = {post.language for post in group}
        pair_keys = {post.pair_key for post in group}
        if len(languages) > 1 and len(pair_keys) > 1:
            files = ", ".join(sorted(post.path.name for post in group))
            issues.append(
                f"{files}: mismatched bilingual paths for source pair {source_key}"
            )
    return issues


def build_language_links(posts):
    groups = {}
    for post in posts:
        if CANONICAL_URL.fullmatch(post.permalink):
            group = groups.setdefault(post.pair_key, {})
            if post.language in group:
                raise ValueError(
                    f"duplicate {post.language} variant for {post.pair_key}"
                )
            group[post.language] = post

    links = {}
    for _pair_key, variants in sorted(groups.items()):
        if len(variants) < 2:
            continue
        for language, post in sorted(variants.items()):
            other_variants = []
            for other_language, other_post in sorted(variants.items()):
                if other_language == language:
                    continue
                other_variants.append(
                    {
                        "language": other_language,
                        "label": LANGUAGE_METADATA[other_language]["label"],
                        "url": other_post.permalink,
                    }
                )
            links[post.permalink] = {"variants": other_variants}
    return dict(sorted(links.items()))


def render_json(data):
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--posts-dir", type=Path, default=DEFAULT_POSTS_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    posts = load_posts(args.posts_dir)
    issues = validate_posts(posts)
    if issues:
        print("Blog URL validation failed:")
        for issue in issues:
            print(f"  - {issue}")
        return 1

    rendered = render_json(build_language_links(posts))
    if args.check:
        current = (
            args.output.read_text(encoding="utf-8")
            if args.output.is_file()
            else ""
        )
        if current != rendered:
            print(
                "Generated language-link data is stale; run "
                "python3 scripts/generate_language_links.py"
            )
            return 1
        print("Language-link data is current.")
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(
        f"Wrote {args.output} with {len(build_language_links(posts))} "
        "directional entries."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
