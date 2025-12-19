# Project Status Board

## Current Status / Progress Tracking
- [x] Polish blog post format for `_posts/2025-12-19-vibe-coding-ides-brief-comparison.md`
    - [x] Add blank lines between natural paragraphs
    - [x] Add spaces between Chinese and English characters
    - [x] Fix image paths for GitHub Pages compatibility

## Background and Motivation
The user wants to format a specific blog post `_posts/2025-12-19-vibe-coding-ides-brief-comparison.md` according to style rules defined in `_posts/blog-prompt.mdc`.

## Key Challenges and Analysis
- Need to carefully parse mixed Chinese and English text.
- Need to ensure formatting does not break markdown syntax (links, images).
- Jekyll does NOT serve files from `_posts/` directory that aren't posts. Images must be in `/images/` or `/assets/`.

## Executor's Feedback or Assistance Requests
- [x] Task completed: Format polished for `_posts/2025-12-19-vibe-coding-ides-brief-comparison.md`.
- [x] Fixed image paths: Moved images from `_posts/attachments/` to `/images/vibe-coding-ides/` and updated all 9 image references to use absolute paths.
- [x] Updated `blog-prompt.mdc` with correct image path guidance.

## Lessons
- Jekyll's `_posts/` directory is special - only markdown files following `YYYY-MM-DD-title.md` format are processed. Other files (like images in `_posts/attachments/`) won't be served.
- Best practice for Jekyll/GitHub Pages: Store images in `/images/<post-name>/` and use absolute paths like `/images/vibe-coding-ides/image.png`.
