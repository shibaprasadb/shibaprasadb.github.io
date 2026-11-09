"""Make Python-Markdown follow the list rules these posts already use.

Kramdown's GFM mode does two things Python-Markdown does not:

- A list can start on the line after a paragraph, with no blank line.
- The paragraph under ``1. `` is indented 3 spaces, not 4.

Both show up in the existing posts. This adjusts the source before parsing
so those lists stay lists. It does not rewrite the post files.
"""

import re

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

_LIST_ITEM = re.compile(r"(?:[-*+]|\d+\.) ")


class GFMListPreprocessor(Preprocessor):
    def run(self, lines):
        in_fence = False
        fixed = []
        for line in lines:
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
            elif not in_fence:
                if (
                    fixed
                    and fixed[-1].strip()
                    and not _LIST_ITEM.match(fixed[-1])
                    and _LIST_ITEM.match(line)
                ):
                    fixed.append("")
                if line.startswith("   ") and not line.startswith("    "):
                    line = " " + line
            fixed.append(line)
        return fixed


class GFMListExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(GFMListPreprocessor(md), "gfm_list", 27)
