# Deterministic Bilingual Links Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enforce canonical English and Chinese blog URLs across the complete archive and render automatically generated language links in both directions.

**Architecture:** A focused Python module parses post front matter, validates public URLs, groups variants by the URL remaining after `/zh` is removed, and writes deterministic Jekyll data. The existing linter delegates URL checks to that module, CI verifies the generated file is current, and a Liquid include renders the matching variants.

**Tech Stack:** Python 3 standard library, `unittest`, Jekyll/Liquid, JSON, GitHub Actions, `jekyll-redirect-from`.

## Global Constraints

- English posts use `/posts/YYYY/MM/slug/`.
- Chinese posts use `/zh/posts/YYYY/MM/slug/`.
- Public URLs must not end in `-cn`, `-zh`, or `-en`.
- Validation applies to every post without a date exemption.
- Every changed URL retains its previous URL through `redirect_from`.
- Update all in-repository links that target migrated URLs.
- Do not edit article prose or create missing translations.

---

### Task 1: Strict URL validator and deterministic data generator

**Files:**
- Create: `scripts/generate_language_links.py`
- Create: `tests/test_language_links.py`
- Modify: `scripts/lint_blog_format.py`

**Interfaces:**
- Produces: `load_posts(posts_dir: Path) -> list[Post]`, `validate_posts(posts: list[Post]) -> list[str]`, `build_language_links(posts: list[Post]) -> dict[str, dict]`, and `render_json(data: dict) -> str`.
- CLI: `python3 scripts/generate_language_links.py [--check] [--posts-dir PATH] [--output PATH]`.
- The blog linter consumes `validate_post_url(path, permalink) -> list[str]` from the generator module.

- [ ] **Step 1: Write failing URL and generation tests**

Create fixture posts in temporary directories inside tests. Assert that `/posts/2026/07/topic/` and `/zh/posts/2026/07/topic/` form a two-way entry, that malformed/day-segment paths and language-suffixed slugs fail, that a `-cn.md` source outside `/zh/` fails, duplicate language variants fail, monolingual posts produce no entry, and reversed input order produces byte-identical JSON.

```python
def test_builds_both_directions(self):
    posts = [
        Post(Path("2026-07-19-topic.md"), "/posts/2026/07/topic/"),
        Post(Path("2026-07-19-topic-cn.md"), "/zh/posts/2026/07/topic/"),
    ]
    self.assertEqual(build_language_links(posts)["/posts/2026/07/topic/"]["variants"],
                     [{"language": "zh", "label": "中文", "url": "/zh/posts/2026/07/topic/"}])
```

- [ ] **Step 2: Run tests and confirm they fail**

Run: `python3 -m unittest tests/test_language_links.py -v`
Expected: FAIL because `scripts/generate_language_links.py` does not exist.

- [ ] **Step 3: Implement the generator and validator**

Use a frozen `Post(path, permalink)` dataclass, a full-match URL regex, URL-prefix language classification, basename-marker consistency checks, duplicate detection, sorted keys/variants, UTF-8 JSON with `ensure_ascii=False`, and a trailing newline. `--check` compares expected bytes with the committed file and exits nonzero with a regeneration command when stale.

```python
CANONICAL_URL = re.compile(r"^/(zh/)?posts/(\d{4})/(\d{2})/([^/]+)/$")
FORBIDDEN_SUFFIX = re.compile(r"-(?:cn|zh|en)$", re.IGNORECASE)

def pair_key(post):
    return post.permalink.removeprefix("/zh")
```

- [ ] **Step 4: Remove prospective-only validation from the old linter**

Delete `URL_POLICY_START` and `follows_url_policy`. Import the new URL validator by adding the scripts directory to `sys.path`, run it for every Markdown post, and keep the existing image policy unchanged unless its own prospective gate is required.

- [ ] **Step 5: Run focused tests**

Run: `python3 -m unittest tests/test_language_links.py tests/test_blog_lint.py -v`
Expected: all tests pass before repository-wide migration is checked.

- [ ] **Step 6: Commit the validator and tests**

```bash
git add scripts/generate_language_links.py scripts/lint_blog_format.py tests/test_language_links.py tests/test_blog_lint.py
git commit -m "Enforce canonical blog language URLs"
```

### Task 2: Migrate legacy URLs and internal references

**Files:**
- Modify: affected `_posts/*.md` front matter and in-repository Markdown references.
- Create: `_data/language_links.json`

**Interfaces:**
- Consumes the generator CLI from Task 1.
- Produces a complete repository state accepted by strict validation.

- [ ] **Step 1: Capture the failing archive audit**

Run: `python3 scripts/generate_language_links.py --check`
Expected: FAIL listing each legacy URL that violates the contract.

- [ ] **Step 2: Normalize every violating permalink**

For each Chinese source marker (`-cn.md` or `-zh.md`), use `/zh/posts/YYYY/MM/<published-slug-with-language-suffix-removed>/`. For English posts, use `/posts/YYYY/MM/<published-slug-with-language-suffix-removed>/`. Remove an extra day path segment. Add the exact former permalink to `redirect_from`, preserving any existing redirect entries.

```yaml
permalink: /zh/posts/2024/08/lead-utexas/
redirect_from:
  - /posts/2024/08/lead-utexas-cn/
```

- [ ] **Step 3: Align known bilingual pairs**

Where English and Chinese sources share a filename key after removing `-cn`, `-zh`, or `-en`, make their canonical `YYYY/MM/slug` identical. Resolve collisions explicitly and fail rather than overwriting a post.

- [ ] **Step 4: Rewrite internal references mechanically**

Build the exact old-to-new URL map from the migration and replace only complete URL tokens in tracked text files. Run `rg` for every old URL and require zero remaining references except `redirect_from` declarations.

- [ ] **Step 5: Generate central data**

Run: `python3 scripts/generate_language_links.py`
Expected: writes sorted `_data/language_links.json` and reports the number of complete pairs.

- [ ] **Step 6: Verify migration and commit**

Run: `python3 scripts/lint_blog_format.py && python3 scripts/generate_language_links.py --check`
Expected: both commands pass.

```bash
git add _posts _data/language_links.json
git commit -m "Migrate blog posts to canonical language URLs"
```

### Task 3: Render the automatic language navigation

**Files:**
- Create: `_includes/language-switcher.html`
- Modify: `_layouts/single.html`
- Modify: `_sass/layout/_page.scss`
- Create or modify: `tests/test_language_switcher.py`

**Interfaces:**
- Consumes `site.data.language_links[page.url].variants`.
- Produces a `<nav class="page__language-switcher" aria-label="Language versions">` containing variant links.

- [ ] **Step 1: Write failing template contract tests**

Assert that the include reads the current URL with bracket lookup, loops over `variants`, applies `relative_url`, renders variant labels, and that `single.html` includes it before article content.

- [ ] **Step 2: Run the test and confirm failure**

Run: `python3 -m unittest tests/test_language_switcher.py -v`
Expected: FAIL because the include is absent.

- [ ] **Step 3: Add the include and layout hook**

```liquid
{% assign language_entry = site.data.language_links[page.url] %}
{% if language_entry and language_entry.variants.size > 0 %}
  <nav class="page__language-switcher" aria-label="Language versions">
    {% for variant in language_entry.variants %}
      <a href="{{ variant.url | relative_url }}" hreflang="{{ variant.language }}">{{ variant.label }}</a>
    {% endfor %}
  </nav>
{% endif %}
```

- [ ] **Step 4: Add minimal theme-aligned styling**

Style the navigation as compact metadata with normal link colors, spacing, and no layout shift. Do not add JavaScript.

- [ ] **Step 5: Run template tests and build**

Run: `python3 -m unittest tests/test_language_switcher.py -v && bundle exec jekyll build`
Expected: tests pass and Jekyll exits zero.

- [ ] **Step 6: Commit rendering**

```bash
git add _includes/language-switcher.html _layouts/single.html _sass/layout/_page.scss tests/test_language_switcher.py
git commit -m "Render automatic bilingual post links"
```

### Task 4: CI integration and final verification

**Files:**
- Modify: `.github/workflows/blog-lint.yml`
- Modify: `CONTRIBUTING.md`

**Interfaces:**
- CI invokes generator `--check` after blog lint and before unit tests.
- Contributor documentation exposes the one regeneration command.

- [ ] **Step 1: Add generator paths and stale-data check to CI**

Include `scripts/generate_language_links.py`, `_data/language_links.json`, `_includes/language-switcher.html`, and `_layouts/single.html` in workflow path filters. Add:

```yaml
- name: Check generated language links
  run: python3 scripts/generate_language_links.py --check
```

- [ ] **Step 2: Document author workflow**

Document canonical English/Chinese permalink forms and require `python3 scripts/generate_language_links.py` after adding or renaming a translation.

- [ ] **Step 3: Run the complete verification set**

Run:

```bash
python3 scripts/lint_blog_format.py
python3 scripts/generate_language_links.py --check
python3 -m unittest discover -s tests -v
bundle exec jekyll build
git diff --check
```

Expected: every command exits zero, and generated pages contain reciprocal `hreflang="en"` and `hreflang="zh"` links for a sampled pair.

- [ ] **Step 4: Commit CI and documentation**

```bash
git add .github/workflows/blog-lint.yml CONTRIBUTING.md
git commit -m "Check bilingual link data in CI"
```

- [ ] **Step 5: Push the completed branch**

Run: `git status --short && git log --oneline origin/main..HEAD && git push origin main`
Expected: clean status and a successful fast-forward push.
