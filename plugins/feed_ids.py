"""Keep Atom entry ids on the post URL, without the .html suffix.

jekyll-feed uses the post id (`/2026/11/01/fundprintv2`), not a tag: URI.
A tag: URI would make feed readers treat the last 10 posts as new.
"""

from pelican import signals


def fix_feed_ids(context, feed):
    del context
    feed_url = feed.feed.get("feed_url")
    if feed_url:
        feed.feed["id"] = feed_url
    for item in feed.items:
        link = item.get("link") or ""
        if link.endswith(".html"):
            item["unique_id"] = link[:-5]
        elif link:
            item["unique_id"] = link


def register():
    signals.feed_generated.connect(fix_feed_ids)
