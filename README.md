# Personal Website — shibaprasadb.github.io

This repository contains the source for [shibaprasadb.github.io](https://shibaprasadb.github.io), a personal site built with [Jekyll 4](https://jekyllrb.com/). The site highlights my work in data science, captures long-form writing, and serves as a hub for newsletter subscriptions and contact information.

## Highlights

- **Custom Jekyll theme** with a hero landing page, sticky navigation bar, dark-mode toggle, and responsive layout styles.
- **Writing hub** powered by Markdown posts in [`_posts/`](./_posts/) with:
  - Automatic tag archive generation via [`_plugins/tag_generator.rb`](./_plugins/tag_generator.rb).
  - Client-side filtering on [`blog.html`](./blog.html) to browse posts by tag without leaving the page.
  - Post layout extras such as Substack subscribe embeds and [Giscus](https://giscus.app) discussions for comments.
- **Static pages** for About, Publications, and Subscribe, plus icons and headshots in [`images/`](./images/).
- **Analytics ready**: GoatCounter and Umami scripts are wired in [`_layouts/default.html`](./_layouts/default.html).
- **Continuous delivery** to GitHub Pages using the workflow in [`.github/workflows/build.yml`](./.github/workflows/build.yml).

## Prerequisites

- Ruby 3.1 (matching [`.ruby-version`](./.ruby-version))
- [Bundler](https://bundler.io/) for dependency management (`gem install bundler`)

## Local development

Install dependencies and run the development server:

```bash
bundle install
bundle exec jekyll serve
```

The site will be available at <http://localhost:4000>. Jekyll supports hot-reloading, so saved changes appear after a refresh.

To build the production site locally:

```bash
bundle exec jekyll build
```

This generates the static site under `_site/`.

## Adding content

### New posts

1. Create a Markdown file in `_posts/` using the `YYYY-MM-DD-title.md` naming convention.
2. Include front matter similar to:

   ```yaml
   ---
   layout: post
   title: My New Article
   tags: [analytics, experimentation]
   ---
   ```

3. Write the post in Markdown below the front matter. Use the `tags` array to enable filtering on the blog page and to generate archive pages.

### Static pages & navigation

- Edit shared navigation links in [`_includes/nav.html`](./_includes/nav.html).
- Update the base layout, analytics scripts, or footer in [`_layouts/default.html`](./_layouts/default.html).
- Page-specific content (About, Publications, Subscribe, etc.) lives in the project root as HTML files.

### Images & assets

Store images in the [`images/`](./images/) directory. Posts often use subfolders (for example, `images/posts/<post-slug>/`) to keep assets organised.

## Comments & subscriptions

- Post pages embed a Substack signup iframe so readers can join the **Data Signal** newsletter without leaving the site.
- Comments are handled through Giscus; repository and category identifiers are configured in [`_includes/giscus.html`](./_includes/giscus.html). Update those values if you fork the project or want to point to a different discussion board.

## Deployment

Every push to `main` triggers the [Build and Deploy](./.github/workflows/build.yml) workflow:

1. Checks out the repository and sets up Ruby 3.1 with Bundler caching.
2. Runs `bundle exec jekyll build` to produce `_site/`.
3. Publishes the artifact to GitHub Pages using `actions/deploy-pages`.

To deploy manually, you can run the same build command locally and upload the contents of `_site/` to any static hosting provider.

## Contact

Questions or collaboration ideas? Reach out at [shibaprasad.b@outlook.com](mailto:shibaprasad.b@outlook.com).
