#!/usr/bin/env python3
"""Static regression checks for the V7 Pro Dashboard artifact.

These checks intentionally fail when known production defects remain.
They do not claim browser-level end-to-end coverage.
"""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class HTMLStructure(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title_depth = 0
        self.title_text = []
        self.ids = set()
        self.scripts = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.title_depth += 1
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "script":
            self.scripts += 1

    def handle_endtag(self, tag):
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data):
        if self.title_depth:
            self.title_text.append(data)


def latest_dashboard():
    files = sorted((ROOT / "dashboard").glob("taifex-*.html"))
    if not files:
        raise AssertionError("No dashboard/taifex-*.html artifact found")
    return files[-1]


class V7DashboardStaticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = latest_dashboard()
        cls.html = cls.path.read_text(encoding="utf-8")
        cls.parser = HTMLStructure()
        cls.parser.feed(cls.html)

    def test_html_has_product_title(self):
        title = "".join(self.parser.title_text).strip()
        self.assertNotEqual(title, "React Artifact",
                            "HTML still uses generic React Artifact title")
        self.assertTrue(title, "HTML title is empty")

    def test_root_entry_exists_for_github_pages(self):
        self.assertTrue((ROOT / "index.html").is_file(),
                        "GitHub Pages publishes master/(root), but index.html is missing")

    def test_data_date_matches_source_label(self):
        embedded = re.search(r'var\s+he\s*=\s*\{\s*date\s*:\s*["\'](\d{4}-\d{2}-\d{2})', self.html)
        source = re.search(r'數據來源\s*[·:]\s*(\d{4}-\d{2}-\d{2})', self.html)
        self.assertIsNotNone(embedded, "Could not locate embedded data date")
        self.assertIsNotNone(source, "Could not locate source label date")
        self.assertEqual(embedded.group(1), source.group(1),
                         "Displayed/source data date differs from embedded data date")

    def test_mock_masking_is_not_used_as_truth_label(self):
        self.assertNotIn('id="hide-mock-js-final"', self.html,
                         "Artifact includes a script that hides MOCK sections; verify data provenance instead")

    def test_four_sections_are_represented(self):
        for section in ("總結", "現貨", "期貨", "選擇權"):
            with self.subTest(section=section):
                self.assertIn(section, self.html, f"Missing expected section text: {section}")

    def test_html_has_react_mount_point(self):
        self.assertIn('id="root"', self.html, "Missing React root mount point")

    def test_artifact_not_empty(self):
        self.assertGreater(len(self.html), 10_000, "Dashboard HTML is unexpectedly small")


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(V7DashboardStaticTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
