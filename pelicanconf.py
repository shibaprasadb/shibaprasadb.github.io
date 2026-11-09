import re
import unicodedata
from datetime import datetime
from zoneinfo import ZoneInfo

AUTHOR = "Shibaprasad Bhattacharya"
SITENAME = "Shibaprasad Bhattacharya"
SITEURL = ""
TIMEZONE = "Asia/Kolkata"
DEFAULT_LANG = "en"
LOCALE = ("en_US.UTF-8", "C")

NOW = datetime.now(ZoneInfo(TIMEZONE))
BUILD_TIME = int(NOW.timestamp())
BUILD_YEAR = NOW.year

SITE_EMAIL = "shibaprasad.b@outlook.com"
SCHOLAR_URL = "https://scholar.google.com/citations?user=hitU7KwAAAAJ&hl=en"
PAGE_WIDTH = "narrow"

PATH = "."
ARTICLE_PATHS = ["_posts"]
ARTICLE_EXCLUDES = []
PAGE_PATHS = []
STATIC_PATHS = ["images", "style.css", "CNAME", "robots.txt", "README.md"]
OUTPUT_PATH = "_site"
DELETE_OUTPUT_DIRECTORY = True
CACHE_CONTENT = False

IGNORE_FILES = ["**/.*", ".*", ".DS_Store"]

THEME = "theme"
DIRECT_TEMPLATES = []
PAGINATED_TEMPLATES = {}
DEFAULT_PAGINATION = False

TEMPLATE_PAGES = {
    "theme/templates/pages/index.html": "index.html",
    "theme/templates/pages/blog.html": "blog.html",
    "theme/templates/pages/subscribe.html": "subscribe.html",
    "theme/templates/pages/publications.html": "publications.html",
}

# Date and slug come from the filename. Front matter `date` overrides the
# filename date, which is what keeps wb-data-series on April 17.
FILENAME_METADATA = r"(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)"
SLUGIFY_PRESERVE_CASE = True
USE_FOLDER_AS_CATEGORY = False

ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_LANG_SAVE_AS = ""
DRAFT_SAVE_AS = ""
DRAFT_LANG_SAVE_AS = ""
DRAFT_PAGE_SAVE_AS = ""
DRAFT_PAGE_LANG_SAVE_AS = ""
PAGE_SAVE_AS = ""
PAGE_LANG_SAVE_AS = ""

TAG_URL = "tags/{slug}/"
TAG_SAVE_AS = "tags/{slug}/index.html"
TAGS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

WITH_FUTURE_DATES = True
SUMMARY_MAX_LENGTH = 50

TYPOGRIFY = True
TYPOGRIFY_OMIT_FILTERS = ["widont", "caps", "amp", "initial_quotes"]

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["yaml_metadata", "neighbors", "sitemap", "feed_ids", "titles"]
SITEMAP = {"format": "xml"}

FEED_ALL_ATOM = None
FEED_ALL_RSS = None
FEED_ATOM = None
FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
FEED_MAX_ITEMS = 10


def gfm_slugify(value, separator, unicode=False):
    """Heading ids in the style kramdown uses for GFM."""
    if not unicode:
        value = unicodedata.normalize("NFKD", value)
        value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^\w\s-]", "", value).strip()
    return re.sub(r"[\s_]+", separator, value)


MARKDOWN = {
    "extension_configs": {
        "plugins.md_gfm:GFMListExtension": {},
        # No nl2br: like Jekyll, a single line break inside a paragraph is
        # just a space. End a line with two spaces to force a break.
        "markdown.extensions.extra": {},
        "markdown.extensions.smarty": {},
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
            "guess_lang": False,
            "linenums": False,
        },
        "markdown.extensions.toc": {
            "permalink": False,
            "slugify": gfm_slugify,
        },
    },
    "output_format": "html5",
}
