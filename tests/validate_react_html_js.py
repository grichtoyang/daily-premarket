#!/usr/bin/env python3
"""Validate every executable inline JavaScript block in a generated React HTML file."""
from __future__ import annotations

import argparse
import subprocess
import tempfile
from html.parser import HTMLParser
from pathlib import Path


class InlineScripts(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.scripts: list[tuple[str, str]] = []
        self._attrs: dict[str, str | None] | None = None
        self._parts: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag.lower() == "script":
            self._attrs = {k.lower(): v for k, v in attrs}
            self._parts = []

    def handle_data(self, data: str) -> None:
        if self._attrs is not None:
            self._parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != "script" or self._attrs is None:
            return
        attrs = self._attrs
        src = attrs.get("src")
        kind = (attrs.get("type") or "").lower()
        code = "".join(self._parts)
        if not src and kind not in {"application/json", "application/ld+json", "importmap"} and code.strip():
            self.scripts.append((kind or "text/javascript", code))
        self._attrs = None
        self._parts = []


def validate(path: Path) -> None:
    parser = InlineScripts()
    parser.feed(path.read_text(encoding="utf-8"))
    if not parser.scripts:
        raise SystemExit(f"No executable inline scripts found: {path}")
    with tempfile.TemporaryDirectory() as tmp:
        for index, (_, code) in enumerate(parser.scripts, 1):
            js = Path(tmp) / f"inline-{index}.js"
            js.write_text(code, encoding="utf-8")
            result = subprocess.run(["node", "--check", str(js)], text=True, capture_output=True)
            if result.returncode:
                raise SystemExit(
                    f"JavaScript syntax FAIL: {path}, inline script #{index}\\n"
                    f"{result.stdout}{result.stderr}"
                )
    print(f"PASS: {path} — {len(parser.scripts)} executable inline scripts")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("html", type=Path)
    validate(ap.parse_args().html)
