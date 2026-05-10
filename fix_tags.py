import os
import re

posts_dir = '/Users/kw35262/Documents/dev/ktwu01.github.io-1/_posts'

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Find frontmatter
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return False

    frontmatter = match.group(1)
    
    # We need to find tags section
    # Tags usually look like:
    # tags:
    #   - Tag One
    #   - TagTwo
    
    lines = frontmatter.split('\n')
    in_tags = False
    new_lines = []
    modified = False
    
    for line in lines:
        if line.startswith('tags:'):
            in_tags = True
            new_lines.append(line)
        elif in_tags and line.startswith('  - '):
            tag = line[4:]
            new_tag = tag.lower().replace(' ', '-')
            if tag != new_tag:
                modified = True
                new_lines.append(f'  - {new_tag}')
            else:
                new_lines.append(line)
        elif in_tags and not line.startswith(' '):
            in_tags = False
            new_lines.append(line)
        else:
            new_lines.append(line)
            
    if modified:
        new_frontmatter = '\n'.join(new_lines)
        new_content = content[:match.start(1)] + new_frontmatter + content[match.end(1):]
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    return False

modified_files = []
for root, dirs, files in os.walk(posts_dir):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            if fix_file(filepath):
                modified_files.append(filepath)

print(f"Modified {len(modified_files)} files.")
for f in modified_files:
    print(f)
