import os
import sys

sys.path.append(os.curdir)

from pelicanconf import *  # noqa: F403, E402

SITEURL = "https://shibaprasadb.github.io"
RELATIVE_URLS = False
FEED_ALL_ATOM = "feed.xml"
FEED_MAX_ITEMS = 10
DELETE_OUTPUT_DIRECTORY = True
