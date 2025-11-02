# shibaprasadb.github.io

Personal website and blog for Shibaprasad Bhattacharya, built with Jekyll and hosted on GitHub Pages.

**Live Site:** https://shibaprasadb.github.io

## Overview

A minimal, responsive personal website featuring technical writing on analytics, product strategy, and data science. The site uses Jekyll's static site generation with custom layouts, a tag-based filtering system, and automated deployment through GitHub Actions.

## Tech Stack

- **Static Site Generator:** Jekyll 4.3
- **Deployment:** GitHub Pages via GitHub Actions
- **Comments:** Giscus (GitHub Discussions)
- **Analytics:** GoatCounter, Umami
- **Newsletter:** Substack integration

## Local Development

### Prerequisites

- Ruby 3.1+ (see `.ruby-version`)
- Bundler (`gem install bundler`)

### Setup

```bash
# Clone repository
git clone https://github.com/shibaprasadb/shibaprasadb.github.io.git
cd shibaprasadb.github.io

# Install dependencies
bundle install

# Start development server
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000` with automatic reload on file changes.

### Build for Production

```bash
bundle exec jekyll build
```

Output will be in the `_site/` directory.

## Project Structure

```
.
├── _config.yml              # Jekyll configuration
├── _includes/               # Reusable components (nav, comments, post lists)
├── _layouts/                # Page templates (default, post, tag)
├── _plugins/                # Custom plugins (tag page generator)
├── _posts/                  # Blog posts (YYYY-MM-DD-title.md format)
├── images/                  # Static assets
├── .github/workflows/       # CI/CD pipeline
└── *.html                   # Static pages (index, blog, publications, subscribe)
```

## Writing Content

### Creating a Blog Post

1. Create a new file in `_posts/` with the naming convention:
   ```
   YYYY-MM-DD-post-title.md
   ```

2. Add front matter:
   ```yaml
   ---
   layout: post
   title: "Your Post Title"
   tags: [tag1, tag2, tag3]
   ---
   ```

3. Write content in Markdown below the front matter.

Tags enable automatic filtering on the blog page and generate individual tag archive pages via the custom plugin in `_plugins/tag_generator.rb`.

### Editing Navigation

Update `_includes/nav.html` to modify the navigation menu.

### Customizing Layouts

- **Base template:** `_layouts/default.html`
- **Post template:** `_layouts/post.html`
- **Tag archive:** `_layouts/tag.html`

## Features

### Tag-Based Filtering

The blog page (`blog.html`) implements client-side tag filtering using vanilla JavaScript. The tag generator plugin automatically creates archive pages for each tag used in posts.

### Comments System

Blog posts include Giscus-powered comments. Configure in `_includes/giscus.html`:
- Repository
- Discussion category
- Theme settings

### Newsletter Integration

Substack newsletter signup forms are embedded on post pages and the dedicated subscribe page (`subscribe.html`).

### Analytics

Two analytics platforms are integrated:
- GoatCounter for privacy-focused metrics
- Umami for detailed analytics

Configuration is in `_layouts/default.html`.

## Deployment

### Automated (Recommended)

Every push to the `main` branch triggers the GitHub Actions workflow (`.github/workflows/build.yml`):

1. Sets up Ruby environment with dependency caching
2. Runs `bundle exec jekyll build`
3. Deploys to GitHub Pages

### Manual Deployment

For alternative hosting:

```bash
bundle exec jekyll build
# Upload _site/ contents to your hosting provider
```

## Configuration

Key settings in `_config.yml`:

```yaml
title: Shibaprasad Bhattacharya
baseurl: ""
url: "https://shibaprasadb.github.io"
future: true  # Allows posts with future dates
```

## Dependencies

Managed via Bundler (see `Gemfile`):

- `jekyll ~> 4.3` - Core static site generator
- `webrick ~> 1.7` - Required for Ruby 3.0+ when running `jekyll serve`

## License

This repository contains personal content and code. Feel free to reference the code structure for your own projects.

## Contact

**Shibaprasad Bhattacharya**
Email: shibaprasad.b@outlook.com
Website: https://shibaprasadb.github.io
