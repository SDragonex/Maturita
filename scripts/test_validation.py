import tempfile
import unittest
from pathlib import Path

from scripts.check_content import read_page
from scripts.check_site import check
from scripts.build import output_path


class ValidationTest(unittest.TestCase):
    def make_site(self, root: Path, href: str):
        (root / 'index.html').write_text(f'<html lang="cs"><a href="{href}">go</a></html>', encoding='utf-8')
        target = root / 'tema'
        target.mkdir()
        (target / 'index.html').write_text('<html lang="cs"><h1 id="čtení">Text</h1></html>', encoding='utf-8')

    def test_accepts_subpath_and_encoded_anchor(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_site(root, '/Maturita/tema/#%C4%8Dten%C3%AD')
            self.assertEqual(check(root, 'https://example.org/Maturita', require_search=False), [])

    def test_rejects_resource_escaping_subpath(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_site(root, '/tema/')
            self.assertTrue(any('escapes base_url' in e for e in check(root, 'https://example.org/Maturita', require_search=False)))

    def test_rejects_missing_fragment(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_site(root, 'tema/#missing')
            self.assertTrue(any('missing anchor' in e for e in check(root, 'https://example.org/', require_search=False)))

    def test_rejects_missing_resource_and_search(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_site(root, 'missing.pdf')
            errors = check(root, 'https://example.org/')
            self.assertTrue(any('missing resource' in e for e in errors))
            self.assertTrue(any('Missing search' in e for e in errors))

    def test_external_link_is_not_treated_as_local(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_site(root, 'https://other.example.org/does-not-exist')
            self.assertEqual(check(root, 'https://example.org/', require_search=False), [])

    def test_absolute_sibling_project_is_external(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_site(root, 'https://example.org/OtherProject/')
            self.assertEqual(check(root, 'https://example.org/Maturita/', require_search=False), [])

    def test_homepage_without_trailing_slash(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_site(root, 'https://example.org/Maturita')
            self.assertEqual(check(root, 'https://example.org/Maturita/', require_search=False), [])

    def test_malformed_metadata_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'bad.md'
            path.write_text('+++\ntitle = "One"\ntitle = "Two"\n+++\nText', encoding='utf-8')
            with self.assertRaises(ValueError):
                read_page(path)

    def test_build_cannot_overwrite_sources(self):
        for target in ['content', '.', 'temp', '../Maturita-other', 'temp/tools', 'temp/tools/zola', 'temp/npm-cache', 'temp/preview', 'temp/builds', 'temp/builds/../tools']:
            with self.subTest(target=target), self.assertRaises(ValueError):
                output_path(target)

    def test_build_accepts_dedicated_outputs(self):
        for target in ['public', 'temp/preview/Maturita', 'temp/root-site', 'temp/builds/experiment']:
            with self.subTest(target=target):
                self.assertEqual(output_path(target).name, Path(target).name)

    def test_search_requires_subpath_configuration(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'index.html').write_text('<html lang="cs"><pagefind-searchbox></pagefind-searchbox></html>', encoding='utf-8')
            self.assertTrue(any('search configuration' in error for error in check(root, 'https://example.org/Maturita/', require_search=False)))

    def test_reversed_topic_navigation_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_site(root, 'aj/01-first/')
            for name, nav in [('01-first', '<a rel="prev" href="../02-second/">wrong</a>'), ('02-second', '<a rel="next" href="../01-first/">wrong</a>')]:
                folder = root / 'aj' / name
                folder.mkdir(parents=True)
                (folder / 'index.html').write_text(f'<html lang="cs">{nav}</html>', encoding='utf-8')
            self.assertTrue(any('topic navigation' in error for error in check(root, 'https://example.org/', require_search=False)))


if __name__ == '__main__':
    unittest.main()
