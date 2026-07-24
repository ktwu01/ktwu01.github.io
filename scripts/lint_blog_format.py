import os
import posixpath
import re
import sys
from urllib.parse import unquote, urlsplit

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from generate_author_notes import (
    expected_author_note,
    has_ambiguous_legacy_language,
    is_author_candidate,
    is_author_line,
    is_disclaimer_line,
    logical_body_lines,
)
from generate_language_links import validate_post_url


POSTS_DIR = "_posts/"
# Local-image rules remain prospective so unrelated legacy content does not
# need an image migration. URL rules are intentionally strict for all posts.
LOCAL_IMAGE_POLICY_START = "2026-07-16"
# Patterns that indicate AI tool-use markup leaked into the file. Any hit is a
# parser-breaking format error and must be removed. Add new patterns here when
# new leak shapes appear. Patterns are built from chr() so this script itself
# does not contain the literal forbidden tokens (which would otherwise self-
# trigger if the file is ever scanned by the same lint).
_LT = chr(60)
_GT = chr(62)
_SLASH = chr(47)
LEAK_PATTERNS = [
    (_LT + _SLASH + "content" + _GT,
     "Leaked closing content tag from tool-use markup"),
    (_LT + _SLASH + "invoke" + _GT,
     "Leaked closing invoke tag from tool-use markup"),
    (_LT + _SLASH + "function_calls" + _GT,
     "Leaked closing function_calls tag from tool-use markup"),
    (_LT + "parameter ",
     "Leaked opening parameter tag from tool-use markup"),
    (_LT + _SLASH + "parameter" + _GT,
     "Leaked closing parameter tag from tool-use markup"),
    ("antml:" + "parameter",
     "Leaked antml namespaced parameter token"),
    ("antml:" + "function_calls",
     "Leaked antml namespaced function_calls token"),
    ("antml:" + "invoke",
     "Leaked antml namespaced invoke token"),
]

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
MARKDOWN_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")


def follows_local_image_policy(filename):
    match = re.match(r"^(\d{4}-\d{2}-\d{2})-", filename)
    return bool(match and match.group(1) >= LOCAL_IMAGE_POLICY_START)


def image_signature_matches(path):
    extension = os.path.splitext(path)[1].lower()
    with open(path, "rb") as image:
        header = image.read(16)

    if extension in (".jpg", ".jpeg"):
        return header.startswith(b"\xff\xd8\xff")
    if extension == ".png":
        return header.startswith(b"\x89PNG\r\n\x1a\n")
    if extension == ".gif":
        return header.startswith((b"GIF87a", b"GIF89a"))
    if extension == ".webp":
        return header.startswith(b"RIFF") and header[8:12] == b"WEBP"
    if extension == ".svg":
        return b"<svg" in header.lower() or header.startswith(b"<?xml")
    return True


def check_local_images(content, repo_root="."):
    """Validate local image URLs, targets, and file signatures."""
    issues = []
    for match in MARKDOWN_IMAGE.finditer(content):
        raw_url = match.group(1).strip("<>")
        parsed = urlsplit(raw_url)
        if parsed.scheme or parsed.netloc or raw_url.startswith("//"):
            continue

        decoded_path = unquote(parsed.path)
        if not decoded_path.startswith("/images/"):
            issues.append(
                f"Local image path must start with /images/: {raw_url}"
            )
            continue
        if "\\" in decoded_path or ".." in decoded_path.split("/"):
            issues.append(f"Local image path contains unsafe traversal: {raw_url}")
            continue

        normalized = posixpath.normpath(decoded_path).lstrip("/")
        target = os.path.join(repo_root, *normalized.split("/"))
        if not os.path.isfile(target):
            issues.append(f"Local image does not exist: {raw_url}")
            continue
        if not image_signature_matches(target):
            issues.append(
                f"Local image content does not match its extension: {raw_url}"
            )
    return issues


def front_matter_value(content, field):
    match = FRONT_MATTER.match(content)
    if not match:
        return None

    value_match = re.search(
        rf"^{re.escape(field)}:\s*(['\"]?)(.*?)\1\s*$",
        match.group(1),
        re.MULTILINE,
    )
    return value_match.group(2) if value_match else None


def check_leaks(content):
    hits = []
    for needle, label in LEAK_PATTERNS:
        if needle in content:
            hits.append(label)
    return hits


# GitHub Pages (Jekyll/Kramdown) requires $$ ... $$ for both inline and block
# math. A single-$ pair containing LaTeX-shaped content silently breaks rendering.
# Allow currency like $50 / $1.5K / $10K through by requiring a LaTeX hint
# character inside the dollars.
SINGLE_DOLLAR_MATH = re.compile(r'(?<!\$)\$([^\$\n]{1,80}?)\$(?!\$)')
LATEX_HINT = re.compile(
    r'[\\\^_=\{\}]|\\frac|\\alpha|\\beta|\\tau|\\rightarrow|\\leftarrow|'
    r'\\sum|\\int|\\partial|\\nabla|\\geq|\\leq|\\approx|\\neq|\\cdot|\\times'
)


def check_single_dollar_math(content):
    hits = []
    in_fence = False
    for lineno, line in enumerate(content.split("\n"), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for m in SINGLE_DOLLAR_MATH.finditer(line):
            inner = m.group(1)
            if LATEX_HINT.search(inner):
                hits.append((lineno, m.group(0)))
    return hits


def check_file_content(content, filepath="2026-07-01-post.md"):
    """Lint already-loaded post content (also convenient for unit tests)."""
    issues = []

    filename = os.path.basename(filepath)
    permalink = front_matter_value(content, "permalink")
    if FRONT_MATTER.match(content):
        issues.extend(validate_post_url(filepath, permalink or ""))

    if follows_local_image_policy(filename):
        issues.extend(check_local_images(content))

    leaks = check_leaks(content)
    for leak in leaks:
        issues.append(leak)

    math_hits = check_single_dollar_math(content)
    for ln, fragment in math_hits:
        issues.append(f"Single-$ LaTeX math at line {ln} ({fragment!r}); GitHub Pages requires $$ ... $$")

    if not FRONT_MATTER.match(content):
        return issues  # Not a Jekyll post or no front matter

    if has_ambiguous_legacy_language(content):
        issues.append(
            "Likely Chinese content must declare lang: zh or use a /zh/ permalink."
        )

    lines = logical_body_lines(content)

    if lines and is_disclaimer_line(lines[0]):
        lines = lines[1:]

    if not lines:
        issues.append("File is empty after front matter")
        return issues

    first_line = lines[0]
    if is_author_line(first_line):
        issues.append("First line is an author line. It should be a punchy hook instead.")
        return issues

    if len(lines) < 2:
        issues.append("Missing content or author line after the hook.")
        return issues

    expected_note = expected_author_note(content)
    author_positions = [
        index for index, line in enumerate(lines) if is_author_candidate(line)
    ]
    if lines[1] != expected_note:
        second_line = lines[1]
        if is_author_candidate(second_line):
            issues.append(
                "Author attribution in the 2nd position is not the canonical "
                "localized note."
            )
            return issues
        for i in range(2, min(len(lines), 10)):
            if is_author_candidate(lines[i]):
                issues.append(f"Author line found at position {i+1}, should be in 2nd position.")
                return issues
        issues.append("Missing author attribution in the 2nd position.")
        return issues

    if len(author_positions) != 1:
        issues.append(
            f"Expected exactly one author attribution; found {len(author_positions)}."
        )

    return issues


def check_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return [f"Error reading file: {e}"]
    return check_file_content(content, filepath)


def main():
    failures = []
    print(f"Auditing blog posts in {POSTS_DIR}...")

    for filename in sorted(os.listdir(POSTS_DIR)):
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(POSTS_DIR, filename)
        issues = check_file(filepath)
        if issues:
            for issue in issues:
                failures.append(f"FAILED: {filename}\n  -> {issue}")

    if failures:
        print("\n" + "\n".join(failures))
        print(f"\nTotal failures: {len(failures)}")
        sys.exit(1)
    else:
        print(
            "\nAll blog posts follow the correct structure "
            "(no AI-leak markup; hook -> deterministic localized author note)."
        )


if __name__ == "__main__":
    main()
