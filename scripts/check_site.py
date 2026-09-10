"""Validate generated local resources, anchors and topic navigation under base_url."""
from __future__ import annotations

import argparse
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, text: str):
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.language = None
        self.has_search = False
        self.search_config = None
        self.neighbors: dict[str, list[str]] = {'prev': [], 'next': []}
        self.feed(text)

    def handle_starttag(self, tag: str, attributes: list[tuple[str, str | None]]):
        attrs = dict(attributes)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'html':
            self.language = attrs.get('lang')
        if tag == 'pagefind-searchbox':
            self.has_search = True
        if tag == 'pagefind-config':
            self.search_config = attrs
        if tag == 'a' and attrs.get('rel') in self.neighbors and attrs.get('href'):
            self.neighbors[attrs['rel']].append(attrs['href'])
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])


def check(site: Path, base_url: str, *, require_search: bool = True) -> list[str]:
    site = site.resolve()
    if not site.is_dir() or not (site / 'index.html').is_file():
        return [f'Missing site homepage: {site}']
    base_url = base_url.rstrip('/') + '/'
    origin = urlsplit(base_url)
    prefix = origin.path
    pages = {p.resolve(): Page(p.read_text(encoding='utf-8')) for p in site.rglob('*.html')}
    errors = []
    for path, page in pages.items():
        relative = path.relative_to(site).as_posix()
        # Zola emits an intentional redirect document at posts/page/1/.
        redirect = relative == 'posts/page/1/index.html'
        if page.language != 'cs' and not redirect:
            errors.append(f'{relative}: document language is not cs')
        current_url = urljoin(base_url, relative.removesuffix('index.html') if relative.endswith('/index.html') or relative == 'index.html' else relative)
        if page.has_search:
            settings = page.search_config or {}
            if urljoin(current_url, settings.get('bundle-path', '')) != urljoin(base_url, 'pagefind/') or urljoin(current_url, settings.get('base-url', '')) != base_url:
                errors.append(f'{relative}: search configuration does not match base_url')
        for link in page.links:
            parsed = urlsplit(urljoin(current_url, link))
            if parsed.scheme not in ('http', 'https') or parsed.netloc != origin.netloc:
                continue
            # An explicit absolute URL may point at another project on this host.
            if not parsed.path.startswith(prefix) and parsed.path != prefix.rstrip('/') and urlsplit(link).scheme:
                continue
            if parsed.scheme != origin.scheme or not parsed.path.startswith(prefix):
                if parsed.scheme == origin.scheme and parsed.path == prefix.rstrip('/'):
                    target = site / 'index.html'
                else:
                    errors.append(f'{relative}: link escapes base_url: {link}')
                    continue
            else:
                target = (site / unquote(parsed.path[len(prefix):])).resolve()
            if not target.is_relative_to(site):
                errors.append(f'{relative}: path escapes output: {link}')
                continue
            if target.is_dir():
                target = target / 'index.html'
            if not target.is_file():
                errors.append(f'{relative}: missing resource: {link}')
            elif parsed.fragment and target.suffix == '.html':
                document = pages.get(target)
                fragment = unquote(parsed.fragment)
                if document and fragment not in document.ids:
                    errors.append(f'{relative}: missing anchor: {link}')
    for subject in ('aj', 'cjl', 'asw', 'psp'):
        topics = sorted(p for p in pages if p.relative_to(site).parts[0] == subject and p.parent.name[:2].isdigit())
        for index, path in enumerate(topics):
            current_url = urljoin(base_url, path.relative_to(site).as_posix().removesuffix('index.html'))
            for relation, offset in [('prev', -1), ('next', 1)]:
                neighbor_index = index + offset
                expected = []
                if 0 <= neighbor_index < len(topics):
                    expected = [urljoin(base_url, topics[neighbor_index].relative_to(site).as_posix().removesuffix('index.html'))]
                actual = [urljoin(current_url, link) for link in pages[path].neighbors[relation]]
                if actual != expected:
                    errors.append(f'{path.relative_to(site)}: incorrect {relation} topic navigation')
    if require_search:
        for resource in ['pagefind.js', 'pagefind-entry.json', 'pagefind-component-ui.js', 'pagefind-component-ui.css']:
            if not (site / 'pagefind' / resource).is_file():
                errors.append(f'Missing search resource: {resource}')
    return sorted(set(errors))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=Path('public'))
    parser.add_argument('--base-url', required=True)
    args = parser.parse_args()
    issues = check(args.site, args.base_url)
    for issue in issues:
        print(issue)
    if not issues:
        print('Generated site OK: local URLs, resources, anchors, Czech language and search assets.')
    sys.exit(bool(issues))
