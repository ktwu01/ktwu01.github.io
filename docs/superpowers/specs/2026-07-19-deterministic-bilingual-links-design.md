# Deterministic Bilingual Links and Strict URL Validation

## Goal

Every bilingual blog post must expose automatic links in both directions without requiring authors to add links inside article bodies. CI must reject every noncanonical blog URL, including legacy posts.

## Canonical URL contract

- English posts use `/posts/YYYY/MM/slug/`.
- Chinese posts use `/zh/posts/YYYY/MM/slug/`.
- A bilingual pair has the same `YYYY/MM/slug` in both languages.
- Public URLs must not use `-cn`, `-zh`, or `-en` as language suffixes.
- The validation applies to all posts. There is no date-based exemption.
- Source filename suffixes may remain internal language markers; the published permalink is authoritative.

Existing posts will be migrated to this contract. All links inside the repository that target an old URL will be updated. Because `jekyll-redirect-from` is already enabled, each changed post will retain its previous public URL in `redirect_from` so external citations continue to resolve.

## Generator and data model

A small Python script will parse post front matter using only repository-supported dependencies. It will:

1. classify language from the permalink prefix;
2. validate the canonical URL shape;
3. derive a language-neutral pair key by removing the leading `/zh` from Chinese URLs;
4. reject duplicate English or Chinese variants for a key;
5. emit a stable, sorted `_data/language_links.json` containing entries for both directions.

Only complete pairs appear in the generated data. A monolingual post remains valid and displays no switcher. The data shape will permit additional language codes later without changing the template contract.

## Rendering

`_layouts/single.html` will call a focused include near the beginning of the article content. The include looks up `page.url` in `site.data.language_links` and renders a compact language navigation element only when variants exist.

- English pages link to the Chinese page with the label `中文`.
- Chinese pages link to the English page with the label `English`.
- Links use `relative_url` so deployments with a base URL continue to work.
- Existing manual language links in post bodies are not required and need not be rewritten unless they target a migrated URL.

## CI behavior

The existing blog lint workflow will run strict URL validation across the complete post archive and run the language-link generator in check mode. Check mode recomputes the data in memory and fails when the committed JSON differs, ensuring contributors regenerate it after adding, removing, or renaming a language variant.

Failures will identify the source file and the expected canonical form. CI will also fail for malformed permalinks, forbidden language suffixes, mismatched bilingual paths, duplicate variants, and stale generated data.

## Migration

The migration will normalize all currently noncanonical bilingual URLs, add recoverable redirects from old URLs, update in-repository references, and regenerate the central data file. It will not change article prose or create translations for monolingual posts.

## Verification

Automated tests will cover:

- strict validation of legacy and new posts;
- valid English and Chinese canonical URLs;
- rejection of public language suffixes;
- complete, one-sided, mismatched, and duplicate variants;
- deterministic generated output and stale-data detection;
- language navigation in both directions;
- a full Jekyll build to detect Liquid or redirect conflicts.

The final repository-wide lint, unit-test suite, generated-data check, internal-link scan, and Jekyll build must all pass.
