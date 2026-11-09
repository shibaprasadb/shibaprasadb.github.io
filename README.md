# shibaprasadb.github.io

Personal website and blog for Shibaprasad Bhattacharya, built with Pelican and hosted on GitHub Pages.

**Live Site:** https://shibaprasadb.github.io

## Overview

A minimal, responsive personal website featuring technical writing on analytics, product strategy, and data science. Posts are Markdown files in `_posts/`. Pelican renders the same URLs the Jekyll site used, and GitHub Actions deploys the result.

## Tech Stack

- **Static Site Generator:** Pelican 4.12
- **Deployment:** GitHub Pages via GitHub Actions
- **Comments:** Giscus (GitHub Discussions)
- **Analytics:** Umami
- **Newsletter:** Substack integration
- **RSS/Atom Feed:** `/feed.xml`

## Local Development

### Prerequisites

- Python 3.12

### Setup

```bash
git clone https://github.com/shibaprasadb/shibaprasadb.github.io.git
cd shibaprasadb.github.io

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Preview

```bash
pelican --autoreload --listen
```

The site is served at `http://localhost:8000` and reloads when files change.

### Production build

```bash
pelican -s publishconf.py
```

Output is written to `_site/`.

## Project Structure

```
.
├── pelicanconf.py           # Site settings
├── publishconf.py           # Production URLs and the Atom feed
├── requirements.txt
├── theme/templates/         # Layouts (base, post, tag, pages)
├── plugins/                 # Feed id override
├── _posts/                  # Blog posts (YYYY-MM-DD-title.md)
├── images/                  # Static assets
└── .github/workflows/       # CI/CD pipeline
```

## Writing Content

Add `_posts/YYYY-MM-DD-slug.md`, put images in `images/posts/YYYY-MM-DD-slug/`, then push to `main`.

```markdown
---
title: "Post title"
date: 2026-11-15
tags: ["data-stories"]
description: "One-line summary for previews and search."
image: "https://shibaprasadb.github.io/images/posts/2026-11-15-slug/thumbnail.png"
selected: true
---

Post body in Markdown.
```

`selected: true` shows the post on the homepage. Always fill in `description`. Without it, the preview text falls back to the opening of the post.

The date in front matter wins over the filename date. The slug is the filename after the date, with its capitalization kept, so a file named `2025-09-02-BeyondSubstack.md` stays at `/2025/09/02/BeyondSubstack.html`.

Tag pages are generated at `/tags/<tag>/`.

## Deployment

Every push to `main` runs `.github/workflows/build.yml`: it installs the Python dependencies, runs `pelican -s publishconf.py`, and deploys `_site/` to GitHub Pages.

## License

This repository contains personal content and code. Feel free to reference the code structure for your own projects.

## Contact

**Shibaprasad Bhattacharya**
Email: shibaprasad.b@outlook.com
Website: https://shibaprasadb.github.io
