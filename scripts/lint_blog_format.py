import os
import re
import sys

POSTS_DIR = "_posts/"
AUTHOR_PATTERNS = [
    r"^> Author: \[Koutian Wu\]",
    r"^> 作者：\[Koutian Wu\]",
]
DISCLAIMER_PATTERNS = [
    r"^> \*\*THIS IS A FAKE BLOG",
    r"^> \*\*这是一篇虚构博客",
]

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


def is_author(line):
    return any(re.match(p, line.strip()) for p in AUTHOR_PATTERNS)


def is_disclaimer(line):
    return any(re.match(p, line.strip()) for p in DISCLAIMER_PATTERNS)


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


def check_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return [f"Error reading file: {e}"]

    issues = []

    filename = os.path.basename(filepath)
    permalink = front_matter_value(content, "permalink")
    if filename.endswith("-cn.md") and not (
        permalink and permalink.startswith("/zh/")
    ):
        issues.append("-cn.md post must use a /zh/ permalink")

    leaks = check_leaks(content)
    for leak in leaks:
        issues.append(leak)

    math_hits = check_single_dollar_math(content)
    for ln, fragment in math_hits:
        issues.append(f"Single-$ LaTeX math at line {ln} ({fragment!r}); GitHub Pages requires $$ ... $$")

    parts = content.split("---")
    if len(parts) < 3:
        return issues  # Not a Jekyll post or no front matter

    body = "---".join(parts[2:]).strip()
    lines = [l.strip() for l in body.split("\n") if l.strip()]

    if lines and is_disclaimer(lines[0]):
        lines = lines[1:]

    if not lines:
        issues.append("File is empty after front matter")
        return issues

    first_line = lines[0]
    if is_author(first_line):
        issues.append("First line is an author line. It should be a punchy hook instead.")
        return issues

    if len(lines) < 2:
        issues.append("Missing content or author line after the hook.")
        return issues

    second_line = lines[1]
    if not is_author(second_line):
        for i in range(2, min(len(lines), 10)):
            if is_author(lines[i]):
                issues.append(f"Author line found at position {i+1}, should be in 2nd position.")
                return issues
        issues.append("Missing author attribution in the 2nd position.")

    return issues


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
        print("\nAll blog posts follow the correct structure (no AI-leak markup; hook -> author).")


if __name__ == "__main__":
    main()
