# shibaprasadb.github.io

This repository hosts my personal website: [shibaprasadb.github.io](https://shibaprasadb.github.io).

The site is generated with [Pelican](https://docs.getpelican.com/).

## Structure

- `pelicanconf.py` – Development settings.
- `publishconf.py` – Production settings.
- `content/pages/` – Static pages like `about.html`, `publications.html`, and the home page.
- `content/posts/` – Blog posts written in Markdown.
- `content/static/style.css` – Global styling.
- `content/images/` – Icons and photographs used on the site.
- `themes/site_theme/` – Custom theme with templates.

## Local development

Install Pelican and Markdown, then build the site:

```bash
pip install pelican markdown
pelican content -o output -s pelicanconf.py
python -m http.server -d output
```

Visit [http://localhost:8000](http://localhost:8000) to preview the site.

---

Contact: [shibaprasad.b@outlook.com](mailto:shibaprasad.b@outlook.com)
