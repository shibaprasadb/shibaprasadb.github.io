# 🌐 Personal Website — shibaprasadb.github.io

[![Build and Deploy](https://github.com/shibaprasadb/shibaprasadb.github.io/workflows/Build%20and%20Deploy/badge.svg)](https://github.com/shibaprasadb/shibaprasadb.github.io/actions)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.x-red.svg)](https://jekyllrb.com/)
[![Ruby](https://img.shields.io/badge/Ruby-3.1-red.svg)](https://www.ruby-lang.org/)

> A modern, responsive personal website showcasing data science work, technical writing, and professional insights.

**🔗 Live Site:** [shibaprasadb.github.io](https://shibaprasadb.github.io)

This repository contains the source code for my personal website, built with Jekyll 4. The site serves as a digital hub for my work in data science, analytics, and AI, featuring technical blog posts, professional updates, and a platform for meaningful discussions.

## ✨ Key Features

### 🎨 **Modern Design**
- Custom Jekyll theme with hero landing page
- Sticky navigation bar with smooth scrolling
- Dark/light mode toggle for better accessibility
- Fully responsive layout optimized for all devices

### 📝 **Content Management**
- **Blog System**: Markdown-powered posts in [`_posts/`](./_posts/) with automatic tag generation
- **Smart Filtering**: Client-side tag filtering on [`blog.html`](./blog.html) for seamless browsing
- **Rich Interactions**: Substack newsletter integration and [Giscus](https://giscus.app) comments
- **Static Pages**: Dedicated sections for About, Publications, and Newsletter subscription

### 📊 **Analytics & Performance**
- Integrated GoatCounter and Umami analytics
- Optimized loading with lazy image loading
- SEO-friendly structure and metadata

### 🚀 **Deployment**
- Automated CI/CD pipeline via GitHub Actions
- Zero-downtime deployments to GitHub Pages
- Custom domain support with CNAME configuration

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

- **Ruby 3.1** (version specified in [`.ruby-version`](./.ruby-version))
- **Bundler** for dependency management
  ```bash
  gem install bundler
  ```

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/shibaprasadb/shibaprasadb.github.io.git
cd shibaprasadb.github.io
```

### 2. Install dependencies
```bash
bundle install
```

### 3. Start the development server
```bash
bundle exec jekyll serve
```

🎉 **That's it!** Your site will be available at <http://localhost:4000>

Jekyll supports hot-reloading, so any changes you make will automatically appear after a browser refresh.

### 4. Build for production
```bash
bundle exec jekyll build
```

This generates the static site under `_site/` directory, ready for deployment.

## 📝 Content Management

### ✍️ Creating New Blog Posts

1. **Create a new file** in `_posts/` following the naming convention:
   ```
   YYYY-MM-DD-your-post-title.md
   ```

2. **Add front matter** at the top of your file:
   ```yaml
   ---
   layout: post
   title: "Your Awesome Post Title"
   tags: [data-science, analytics, ai]
   ---
   ```

3. **Write your content** in Markdown below the front matter. The `tags` array enables:
   - Automatic filtering on the blog page
   - Generation of tag archive pages
   - Better content discoverability

### 🎨 Customizing Pages & Navigation

| Component | File Location | Purpose |
|-----------|---------------|---------|
| **Navigation** | [`_includes/nav.html`](./_includes/nav.html) | Edit menu links and structure |
| **Layout** | [`_layouts/default.html`](./_layouts/default.html) | Modify base template, analytics, footer |
| **Static Pages** | Root directory (`.html` files) | About, Publications, Subscribe content |

### 🖼️ Managing Images & Assets

- **Main directory**: [`images/`](./images/) for general assets
- **Post-specific**: Use subfolders like `images/posts/<post-slug>/` for organization
- **Optimization**: Images are lazy-loaded for better performance

**Pro tip**: Keep image file sizes reasonable (< 500KB) for optimal loading times.

## 💬 Community Features

### 📧 Newsletter Integration
- **Substack Integration**: Embedded signup forms on post pages for the **Data Signal** newsletter
- **Seamless Experience**: Readers can subscribe without leaving the site

### 💭 Comments System
- **Powered by Giscus**: GitHub-based discussion system for authentic conversations
- **Configuration**: Update repository and category settings in [`_includes/giscus.html`](./_includes/giscus.html)
- **Moderation**: Leverage GitHub's moderation tools and community guidelines

## 🚢 Deployment

### Automated Deployment
Every push to `main` triggers the automated [Build and Deploy](./.github/workflows/build.yml) workflow:

1. **Environment Setup**: Ruby 3.1 with Bundler caching
2. **Build Process**: `bundle exec jekyll build` generates `_site/`
3. **Deployment**: Publishes to GitHub Pages using `actions/deploy-pages`

### Manual Deployment
For other hosting providers:
```bash
bundle exec jekyll build
# Upload contents of _site/ to your hosting provider
```

## 📊 Project Structure

```
├── _config.yml          # Jekyll configuration
├── _includes/           # Reusable components
├── _layouts/            # Page templates
├── _plugins/            # Custom Jekyll plugins
├── _posts/              # Blog posts
├── images/              # Static assets
├── .github/workflows/   # CI/CD configuration
└── *.html              # Static pages
```

## 📬 Contact

**Shibaprasad Bhattacharya**  
📧 [shibaprasad.b@outlook.com](mailto:shibaprasad.b@outlook.com)  
🌐 [shibaprasadb.github.io](https://shibaprasadb.github.io)

---

<div align="center">
  <p><em>Built with ❤️ using Jekyll and GitHub Pages</em></p>
  <p><sub>This README was enhanced with AI assistance</sub></p>
</div>
