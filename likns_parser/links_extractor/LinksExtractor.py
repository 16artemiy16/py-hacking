import re
from urllib.request import urlopen
from urllib.parse import urljoin

from .LinksExtractorResult import *


class LinksExtractor:
    def __init__(self, url):
        self._url = url

    def fetch(self):
        res = urlopen(self._url)
        content = res.read().decode(res.headers.get_content_charset())
        raw_links = LinksExtractor._find_links_in_text(content)
        links = self._process_raw_links(raw_links)
        return LinksExtractorResult(self._url, links)

    @property
    def _netloc(self):
        return urlparse(self._url).netloc

    @staticmethod
    def _find_links_in_text(text):
        return re.findall(r'<a\s+(?:[^>]*?\s+)?href=(["\'])(.*?)\1', text)

    def _process_raw_links(self, raw_links):
        pull = lambda pair: pair[1]
        is_empty = lambda l: len(l) == 0
        is_anchor = lambda l: l[0] == '#'

        links = [pull(l) for l in raw_links]
        without_empty = [l for l in links if not is_empty(l)]
        without_anchors = [l for l in without_empty if not is_anchor(l)]

        return [urljoin(self._url, l) for l in without_anchors]
