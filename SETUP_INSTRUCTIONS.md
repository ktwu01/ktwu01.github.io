# Setup Instructions for Koutian Wu

Welcome to your personal academic website! This document provides instructions on how to customize the website with your actual information.

## Quick Start

1. **Update Your Profile Information**
   - Edit `_config.yml` to add your:
     - Email address
     - Location
     - Current employer/institution
     - Academic profile links (Google Scholar, ORCID, ResearchGate, etc.)
     - Social media handles

2. **Add Your Profile Photo**
   - Replace `images/profile.png` with your professional photo
   - Keep the filename as `profile.png` or update the reference in `_config.yml`

3. **Update the About Page**
   - Edit `_pages/about.md` with your personal introduction
   - Add your research interests and current work

4. **Add Your CV Information**
   - Edit `_pages/cv.md` with your:
     - Education history
     - Work experience
     - Skills
     - Awards and honors

## Adding Content

### Publications
- Add new publications by creating files in `_publications/`
- Use `_publications/2009-10-01-paper-title-number-1.md` as a template
- Name files as: `YYYY-MM-DD-short-title.md`

### Talks
- Add talks/presentations in `_talks/`
- Use `_talks/sample-talk.md` as a template

### Teaching
- Add courses in `_teaching/`
- Use `_teaching/2014-spring-teaching-1.md` as a template

### Blog Posts
- Add blog posts in `_posts/`
- Use `_posts/2024-01-01-welcome.md` as a template

## File Management

Upload PDFs and other files to the `files/` directory. They will be accessible at:
`https://ktwu01.github.io/files/filename.pdf`

## Testing Locally

1. Install Jekyll: `bundle install`
2. Run locally: `bundle exec jekyll serve`
3. View at: `http://localhost:4000`

## Need Help?

- Academic Pages documentation: https://academicpages.github.io/
- GitHub Pages documentation: https://docs.github.com/en/pages

## Next Steps

1. Update all placeholder content with your actual information
2. Delete this file once you've completed the setup
3. Commit and push your changes to see them live at https://ktwu01.github.io

Good luck with your academic website!