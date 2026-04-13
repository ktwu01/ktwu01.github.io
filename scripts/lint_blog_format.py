import os
import re
import sys

POSTS_DIR = "_posts/"
AUTHOR_PATTERNS = [
    r"^> Author: \[Koutian Wu\]",
    r"^> 作者：\[Koutian Wu\]"
]

def is_author(line):
    return any(re.match(p, line.strip()) for p in AUTHOR_PATTERNS)

def check_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return f"Error reading file: {e}"

    parts = content.split('---')
    if len(parts) < 3:
        return None # Not a Jekyll post or no front matter
    
    body = '---'.join(parts[2:]).strip()
    lines = [l.strip() for l in body.split('\n') if l.strip()]
    
    if not lines:
        return f"File is empty after front matter"

    first_line = lines[0]
    if is_author(first_line):
        return "First line is an author line. It should be a punchy hook instead."
    
    if len(lines) < 2:
        return "Missing content or author line after the hook."
    
    second_line = lines[1]
    if not is_author(second_line):
        # Check if it's deeper, which we also don't want
        for i in range(2, min(len(lines), 10)):
            if is_author(lines[i]):
                return f"Author line found at position {i+1}, should be in 2nd position."
        return "Missing author attribution in the 2nd position."

    return None

def main():
    errors = []
    print(f"Auditing blog posts in {POSTS_DIR}...")
    
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith(".md"):
            continue
        
        filepath = os.path.join(POSTS_DIR, filename)
        issue = check_file(filepath)
        if issue:
            errors.append(f"FAILED: {filename}\n  -> {issue}")

    if errors:
        print("\n" + "\n".join(errors))
        print(f"\nTotal failures: {len(errors)}")
        sys.exit(1)
    else:
        print("\nAll blog posts follow the correct structure! (Hook -> Author)")

if __name__ == "__main__":
    main()
