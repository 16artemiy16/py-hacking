from urllib.parse import urlparse


class LinksExtractorResult:
    def __init__(self, url, links):
        self._url = url
        self._links = links

    @property
    def _netloc(self):
        return urlparse(self._url).netloc

    @property
    def links(self):
        return self._links

    @property
    def internal(self):
        is_internal = lambda link: self._netloc == urlparse(link).netloc
        return [l for l in self._links if is_internal(l)]

    @property
    def internal_count(self):
        return len(self.internal)

    @property
    def external(self):
        is_external = lambda link: self._netloc != urlparse(link).netloc
        return [l for l in self._links if is_external(l)]

    @property
    def external_count(self):
        return len(self.external)
