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


def check_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return [f"Error reading file: {e}"]

    issues = []

    leaks = check_leaks(content)
    for leak in leaks:
        issues.append(leak)

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
