"""Typogrify stores smart quotes in titles as HTML entities.

Unescape them so templates can escape once. Otherwise ``&#8217;`` becomes
``&amp;#8217;`` and the apostrophe shows up as source text.
"""

import html

from pelican import signals


def unescape_title(content):
    title = getattr(content, "title", None)
    if isinstance(title, str):
        content.title = html.unescape(title)


def register():
    signals.content_object_init.connect(unescape_title)
