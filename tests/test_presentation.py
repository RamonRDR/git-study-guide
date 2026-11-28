"""Presentation checks; no network, dependencies or learner execution."""
import json
from html.parser import HTMLParser
from pathlib import Path
from struct import unpack
import unittest
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs/assets/learning-hub"
LANGUAGES = ROOT / "docs/assets/language-badges"
READMES = [ROOT / "README.md", ROOT / "docs/localized/README.pt-BR.md",
           ROOT / "docs/localized/README.es.md"]
SIZES = {"banner": (1280, 400), "logo": (1000, 300),
         "repository-preview": (1280, 640), "study-guide-card": (640, 400),
         **{n: (384, 384) for n in ("logo-mark", "logo-mark-light",
                                   "logo-mark-mono-dark", "logo-mark-mono-light")},
         **{"study-git-" + loc: (207, 34) for loc in ("en", "pt-br", "es")}}
class Markup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.images = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a":
            self.links.append(a)
        elif tag == "img":
            self.images.append(a)

class PresentationTests(unittest.TestCase):
    def test_approved_export_dimensions(self):
        for name, dimensions in SIZES.items():
            with self.subTest(name=name):
                data = (ASSETS / (name + ".png")).read_bytes()
                self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
                self.assertEqual(data[12:16], b"IHDR")
                self.assertEqual(unpack(">II", data[16:24]), dimensions)
                svg = ET.parse(ASSETS / (name + ".svg")).getroot()
                self.assertEqual((int(svg.attrib["width"]), int(svg.attrib["height"])), dimensions)
    def test_svg_is_self_contained(self):
        for file in ASSETS.glob("*.svg"):
            with self.subTest(file=file.name):
                root = ET.parse(file).getroot()
                for el in root.iter():
                    self.assertNotIn(el.tag.rsplit("}", 1)[-1], {"script", "image", "foreignObject"})
                    for key, val in el.attrib.items():
                        self.assertFalse(key.rsplit("}", 1)[-1].lower().startswith("on"))
                        if key.rsplit("}", 1)[-1] == "href":
                            self.assertTrue(val.startswith("#"))
    def test_readme_local_html_targets(self):
        for path in READMES:
            with self.subTest(path=path.name):
                parser = Markup()
                parser.feed(path.read_text(encoding="utf-8"))
                self.assertGreater(len(parser.images), 20)
                for tag in parser.links + parser.images:
                    attr = "src" if "src" in tag else "href"
                    raw = tag.get(attr)
                    self.assertTrue(raw)
                    if attr == "src":
                        self.assertTrue(tag.get("alt", "").strip())
                    url = urlsplit(raw)
                    if url.scheme or url.netloc or not url.path:
                        continue
                    target = (path.parent / unquote(url.path)).resolve()
                    self.assertTrue(target.is_relative_to(ROOT))
                    self.assertTrue(target.is_file(), (path, target))
    def test_language_selectors_and_curriculum(self):
        manifest = json.loads((ROOT / "curriculum/manifest.json").read_text(encoding="utf-8"))
        for path, loc in zip(READMES, ("en", "pt-BR", "es")):
            with self.subTest(path=path.name):
                parser = Markup()
                parser.feed(path.read_text(encoding="utf-8"))
                selected = [(path.parent / a["href"]).resolve() for a in parser.links
                            if a.get("href") and not urlsplit(a["href"]).scheme]
                for target in READMES:
                    self.assertIn(target, selected)
                for module in manifest["modules"]:
                    self.assertIn(ROOT / module["index"][loc], selected)
                for lang in ("en", "pt-br", "es"):
                    name = "language-" + lang + "-v2.svg"
                    self.assertIn(LANGUAGES / name, [(path.parent / i["src"]).resolve()
                                  for i in parser.images if not urlsplit(i["src"]).scheme])
                self.assertIn("learning-hub:start", path.read_text(encoding="utf-8"))
